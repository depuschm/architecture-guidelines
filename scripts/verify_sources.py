#!/usr/bin/env python3
"""Check that the sources in sources.csv are alive, not retired, and recently verified.

Usage:
  python3 scripts/verify_sources.py              Fetch every source. Fail on broken links and on pages that
                                                 look retired: redirected to a home, 404 or "deprecated" page,
                                                 titled "not found", or an untitled page marked noindex.
                                                 These still answer HTTP 200, so a plain link checker
                                                 misses them.
  python3 scripts/verify_sources.py --stale      List sources whose verified date is older than --max-age
                                                 days (default 365), oldest first. No network needed.
  Options: --max-age DAYS, --strict (with --stale: exit 1 if any source is stale), --verbose.

Sources excluded in lychee.toml (sites that block automated requests) are skipped.
"""

import argparse
import concurrent.futures
import datetime
import http.cookiejar
import re
import sys
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


def excluded_patterns():
    config = rank.ROOT / "lychee.toml"
    if not config.exists():
        return []
    with config.open("rb") as handle:
        return [re.compile(pattern) for pattern in tomllib.load(handle).get("exclude", [])]


def normalise(url):
    parts = urllib.parse.urlsplit(url)
    return parts.netloc.lower().removeprefix("www."), parts.path.rstrip("/") or "/"


def fetch(url, attempts=2):
    """Return (status, final url, html) — status 0 means a network error."""
    last = (0, url, "")
    for _ in range(attempts):
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
        try:
            with opener.open(request, timeout=30) as response:
                body = response.read(300_000).decode("utf-8", errors="replace")
                return response.status, response.geturl(), body
        except urllib.error.HTTPError as error:
            last = (error.code, error.geturl() or url, "")
            if error.code not in (502, 503, 504):  # gateway errors are often temporary: retry them
                return last
            time.sleep(5)
        except Exception as error:  # timeouts, DNS, TLS
            last = (0, url, str(error))
    return last


def classify(url):
    """Return (verdict, detail). Verdicts: ok, broken, retired, blocked, suspect, unreachable."""
    status, final, body = fetch(url)
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
    return "ok", f"moved to {final}" if moved else ""


def check_links(verbose):
    sources = rank.load_sources()
    excluded = excluded_patterns()
    urls = [url for url in sources if not any(pattern.search(url) for pattern in excluded)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(zip(urls, pool.map(classify, urls)))
    failures = 0
    for verdict in ("broken", "retired", "suspect", "blocked", "unreachable", "ok"):
        for url, (found, detail) in sorted(results.items()):
            if found != verdict or (verdict == "ok" and not (verbose and detail)):
                continue
            failures += verdict in ("broken", "retired")
            print(f"{verdict.upper():<11} {url}  {detail}")
    counts = {verdict: sum(1 for v, _ in results.values() if v == verdict) for verdict in
              ("ok", "broken", "retired", "suspect", "blocked", "unreachable")}
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
