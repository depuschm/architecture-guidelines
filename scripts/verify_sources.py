#!/usr/bin/env python3
"""Check that the sources in sources.csv are alive, not retired, and recently verified.

Usage:
  python3 scripts/verify_sources.py              Fetch every source. Fail on broken links and on pages that
                                                 look retired: redirected to a home, 404 or "deprecated" page,
                                                 titled "not found", or an untitled page marked noindex.
                                                 These still answer HTTP 200, so a plain link checker
                                                 misses them. Also list sources that moved: a permanent
                                                 redirect (301 or 308) to a new address. They still work,
                                                 so they don't fail, but their links should be updated.
  python3 scripts/verify_sources.py --stale      List sources whose verified date is older than --max-age
                                                 days (default 365), oldest first. No network needed.
  Options: --max-age DAYS, --strict (with --stale: exit 1 if any source is stale), --verbose.

Sources excluded in lychee.toml (sites that block automated requests) are skipped.
"""

import argparse
import concurrent.futures
import contextlib
import datetime
import http.cookiejar
import re
import sys
import threading
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rank  # noqa: E402

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
RETIRED_PATH = re.compile(r"(^|/)(deprecated|404|not-?found|page-not-found|error)(/|\.|$)", re.IGNORECASE)
RETIRED_TITLE = re.compile(r"\b(404|page not found|not found|no longer available)\b", re.IGNORECASE)
# Only the title is checked: many sites embed "no longer available" UI strings in every page's HTML.
SUSPECT_TITLE = re.compile(r"\b(deprecated|archived|retired)\b", re.IGNORECASE)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META = re.compile(r"<meta\b[^>]*>", re.IGNORECASE)
# github.com answers bursts of requests with HTTP 504, so go slowly there, as lychee.toml does:
# at most this many requests at a time, with a pause after each.
SLOW_HOSTS = {"github.com": 2}
SLOW_HOST_PAUSE = 0.5
HOST_SLOTS = {host: threading.BoundedSemaphore(limit) for host, limit in SLOW_HOSTS.items()}


def excluded_patterns():
    config = rank.ROOT / "lychee.toml"
    if not config.exists():
        return []
    with config.open("rb") as handle:
        return [re.compile(pattern) for pattern in tomllib.load(handle).get("exclude", [])]


def normalise(url):
    parts = urllib.parse.urlsplit(url)
    return parts.netloc.lower().removeprefix("www."), parts.path.rstrip("/") or "/"


class RecordingRedirects(urllib.request.HTTPRedirectHandler):
    """Follows redirects like the default handler, and remembers each one's status code and target."""

    def __init__(self):
        self.hops = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.hops.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def permanent_target(hops):
    """Where the leading permanent redirects (301, 308) end, or None if the first redirect isn't one.
    Temporary redirects after them, for example to a docs site's current version, don't count."""
    target = None
    for code, newurl in hops:
        if code not in (301, 308):
            break
        target = newurl
    return target


@contextlib.contextmanager
def host_slot(url):
    """Limit how many requests run at once against a slow host, and pause after each."""
    slot = HOST_SLOTS.get(urllib.parse.urlsplit(url).netloc.lower().removeprefix("www."))
    if slot is None:
        yield
        return
    with slot:
        yield
        time.sleep(SLOW_HOST_PAUSE)


def fetch(url, attempts=3):
    """Return (status, final url, html, permanent target) — status 0 means a network error."""
    with host_slot(url):
        return fetch_now(url, attempts)


def fetch_now(url, attempts):
    last = (0, url, "", None)
    for attempt in range(attempts):
        redirects = RecordingRedirects()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()), redirects)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
        try:
            with opener.open(request, timeout=30) as response:
                body = response.read(300_000).decode("utf-8", errors="replace")
                return response.status, response.geturl(), body, permanent_target(redirects.hops)
        except urllib.error.HTTPError as error:
            last = (error.code, error.geturl() or url, "", None)
            if error.code not in (502, 503, 504):  # gateway errors are often temporary: retry them
                return last
            time.sleep(5 * (attempt + 1))
        except Exception as error:  # timeouts, DNS, TLS
            last = (0, url, str(error), None)
    return last


def classify(url):
    """Return (verdict, detail). Verdicts: ok, moved, broken, retired, blocked, suspect, unreachable."""
    status, final, body, permanent = fetch(url)
    if status == 0:
        return "unreachable", body[:120]
    if status in (401, 403, 429):
        return "blocked", f"HTTP {status} (check by hand)"
    if status >= 400:
        return "broken", f"HTTP {status}"
    original_host, original_path = normalise(url)
    final_host, final_path = normalise(final)
    moved = (original_host, original_path) != (final_host, final_path)
    # A redirect to the same site's home page is the classic soft 404. A redirect to another
    # host's root (for example owasp.org/Top10/ -> top10.owasp.org) is a move.
    to_home = final_host == original_host and final_path == "/" and original_path != "/"
    if moved and (to_home or RETIRED_PATH.search(final_path)):
        return "retired", f"redirects to {final}"
    title = TITLE.search(body)
    title = re.sub(r"\s+", " ", title.group(1)).strip() if title else ""
    if RETIRED_TITLE.search(title):
        return "retired", f'page title is "{title[:80]}"'
    if SUSPECT_TITLE.search(title):
        return "suspect", f'page title is "{title[:80]}" (check by hand)'
    # Some sites (for example Epic's Unreal Engine docs) answer unknown pages with HTTP 200 and an
    # empty page that tells search engines not to index it.
    noindex = any("robots" in tag.lower() and "noindex" in tag.lower() for tag in META.findall(body))
    if noindex and not title:
        return "retired", "untitled page marked noindex (a soft 404)"
    if noindex:
        return "suspect", "page is marked noindex (check by hand)"
    # A site's home page that redirects into its docs (modelcontextprotocol.io/ -> a versioned intro)
    # is a landing page, not a move.
    if permanent and original_path != "/" and normalise(permanent) != (original_host, original_path):
        fragment = urllib.parse.urlsplit(url).fragment
        new = permanent if not fragment or "#" in permanent else f"{permanent}#{fragment}"
        return "moved", f"permanently redirects to {new} (update the link)"
    return "ok", f"redirects to {final}" if moved else ""


def check_links(verbose):
    sources = rank.load_sources()
    excluded = excluded_patterns()
    urls = [url for url in sources if not any(pattern.search(url) for pattern in excluded)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(zip(urls, pool.map(classify, urls)))
    failures = 0
    for verdict in ("broken", "retired", "suspect", "moved", "blocked", "unreachable", "ok"):
        for url, (found, detail) in sorted(results.items()):
            if found != verdict or (verdict == "ok" and not (verbose and detail)):
                continue
            failures += verdict in ("broken", "retired")
            print(f"{verdict.upper():<11} {url}  {detail}")
    counts = {verdict: sum(1 for v, _ in results.values() if v == verdict) for verdict in
              ("ok", "moved", "broken", "retired", "suspect", "blocked", "unreachable")}
    print(f"\nChecked {len(urls)} sources ({len(sources) - len(urls)} excluded by lychee.toml): "
          + ", ".join(f"{count} {verdict}" for verdict, count in counts.items() if count))
    if failures:
        print("Replace or remove broken and retired sources (see CONTRIBUTING.md).")
    return 1 if failures else 0


def check_stale(max_age, strict):
    sources = rank.load_sources()
    cutoff = datetime.date.today() - datetime.timedelta(days=max_age)
    stale = sorted(
        (entry["verified"], url, entry["title"])
        for url, entry in sources.items()
        if not entry["verified"] or datetime.date.fromisoformat(entry["verified"]) < cutoff
    )
    for verified, url, title in stale:
        print(f"{verified or 'never':<10}  {title}  {url}")
    print(f"\n{len(stale)} of {len(sources)} sources were last verified more than {max_age} days ago.")
    return 1 if strict and stale else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stale", action="store_true", help="list sources not verified recently (no network)")
    parser.add_argument("--max-age", type=int, default=365, help="days before a source counts as stale")
    parser.add_argument("--strict", action="store_true", help="with --stale: fail if any source is stale")
    parser.add_argument("--verbose", action="store_true", help="also list sources that moved")
    args = parser.parse_args()
    if args.stale:
        return check_stale(args.max_age, args.strict)
    return check_links(args.verbose)


if __name__ == "__main__":
    sys.exit(main())
