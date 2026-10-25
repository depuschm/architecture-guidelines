#!/usr/bin/env python3
"""Check and maintain the 1-10 scores of guideline entries and sources.

Every reference entry and every key rule in general/ and specific/ starts with
its score in backticks, for example "- `9` **Rule.** ...". Reference entries
take their score from sources.csv (the score of their first link). Key rules
carry their own score. Lists are sorted by score, highest first. SOURCES.md is
generated from sources.csv. The scoring criteria are in RANKING.md.

Usage:
  python3 scripts/rank.py check   Verify scores, sort order, sources.csv and SOURCES.md (used by CI).
  python3 scripts/rank.py fix     Apply scores from sources.csv, sort lists, add the legend line,
                                  add new links to sources.csv (score left empty for you to fill in),
                                  remove unused ones, and regenerate SOURCES.md.
"""

import csv
import io
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDELINE_DIRS = ["general", "specific"]
SOURCES_CSV = ROOT / "sources.csv"
SOURCES_MD = ROOT / "SOURCES.md"
RANKING_MD = ROOT / "RANKING.md"

LIST_ITEM = re.compile(r"^( *)(?:[-*+]|\d+[.)]) +(.*)$")
HEADING = re.compile(r"^(#{1,6}) +(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
SCORE = re.compile(r"^`(\d+)` +")
LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
RULES_SECTION = "Key rules"

# (lowest score, highest score, name for sources, name for rules)
TIERS = [
    (9, 10, "Start here", "Strongly recommended"),
    (6, 8, "Recommended", "Recommended"),
    (1, 5, "Further reading", "Conditional"),
]


def guideline_files():
    for directory in GUIDELINE_DIRS:
        for path in sorted((ROOT / directory).rglob("*.md")):
            if not any(part.startswith("_") for part in path.relative_to(ROOT).parts):
                yield path


def legend_line(path):
    ranking = os.path.relpath(RANKING_MD, path.parent).replace(os.sep, "/")
    return (
        f"> Entries are sorted by score from 1 to 10 ([criteria]({ranking})): "
        "9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional."
    )


class Item:
    def __init__(self, start, end, indent):
        self.start, self.end, self.indent = start, end, indent
        self.children = []  # nested lists, each a list of Items


def parse_items(lines, start, stop, indent):
    """Parse sibling list items at `indent` in lines[start:stop]. Lists must be tight (no blank lines)."""
    items = []
    i = start
    while i < stop:
        match = LIST_ITEM.match(lines[i])
        if not match or len(match.group(1)) != indent:
            break
        j = i + 1
        while j < stop and lines[j].strip() and not HEADING.match(lines[j]):
            inner = LIST_ITEM.match(lines[j])
            if inner and len(inner.group(1)) <= indent:
                break
            j += 1
        item = Item(i, j, indent)
        k = i + 1
        while k < j:
            inner = LIST_ITEM.match(lines[k])
            if inner:
                children, k = parse_items(lines, k, j, len(inner.group(1)))
                item.children.append(children)
            else:
                k += 1
        items.append(item)
        i = j
    return items, i


def top_level_lists(lines):
    """Return [(h2 section, items)] for every top-level list outside code blocks."""
    lists, section, in_fence, i = [], None, False, 0
    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            heading = HEADING.match(line)
            if heading:
                if len(heading.group(1)) == 2:
                    section = heading.group(2)
            elif LIST_ITEM.match(line):
                items, end = parse_items(lines, i, len(lines), len(LIST_ITEM.match(line).group(1)))
                lists.append((section, items))
                i = end
                continue
        i += 1
    return lists


def own_text(lines, item):
    """The item's text without its nested lists."""
    parts = [LIST_ITEM.match(lines[item.start]).group(2)]
    for k in range(item.start + 1, item.end):
        if LIST_ITEM.match(lines[k]):
            break
        parts.append(lines[k].strip())
    return " ".join(parts)


class Context:
    def __init__(self, sources, fix):
        self.sources, self.fix = sources, fix
        self.problems = []
        self.ranked_items = 0


def render_item(lines, item, section, path, ctx):
    """Return (kind, score, lines) for one item, with its nested lists rendered."""
    first = lines[item.start]
    match = LIST_ITEM.match(first)
    text = own_text(lines, item)
    links = LINK.findall(SCORE.sub("", text, count=1))
    kind = "rule" if section == RULES_SECTION else ("reference" if links else None)
    score = None
    where = f"{path.relative_to(ROOT)}:{item.start + 1}"
    if kind:
        ctx.ranked_items += 1
        current = SCORE.match(match.group(2))
        current = int(current.group(1)) if current else None
        if kind == "reference":
            url = links[0][1]
            entry = ctx.sources.get(url)
            score = entry["score"] if entry else None
            if score is None:
                ctx.problems.append(f"{where}: no score in sources.csv for {url}")
        else:
            score = current
            if score is None:
                ctx.problems.append(f"{where}: key rule has no score, start it with `N` (1-10)")
        if score is not None and not 1 <= score <= 10:
            ctx.problems.append(f"{where}: score {score} is outside 1-10")
        if score is not None and current != score:
            if ctx.fix:
                rest = SCORE.sub("", match.group(2), count=1)
                first = first[: match.start(2)] + f"`{score}` " + rest
            else:
                shown = f"`{current}`" if current is not None else "no score"
                ctx.problems.append(f"{where}: has {shown}, but sources.csv says `{score}` (run rank.py fix)")
    out = [first]
    k = item.start + 1
    for children in item.children:
        out.extend(lines[k:children[0].start])
        out.extend(render_list(lines, children, section, path, ctx))
        k = children[-1].end
    out.extend(lines[k:item.end])
    return kind, score, out


def render_list(lines, items, section, path, ctx):
    rendered = [render_item(lines, item, section, path, ctx) for item in items]
    kinds = {kind for kind, _, _ in rendered}
    if None in kinds and len(kinds) > 1:
        ctx.problems.append(f"{path.relative_to(ROOT)}:{items[0].start + 1}: list mixes ranked and unranked items")
    elif None not in kinds and all(score is not None for _, score, _ in rendered):
        ordered = sorted(rendered, key=lambda r: -r[1])
        if [r[1] for r in ordered] != [r[1] for r in rendered]:
            if ctx.fix:
                rendered = ordered
            else:
                ctx.problems.append(f"{path.relative_to(ROOT)}:{items[0].start + 1}: list is not sorted by score (run rank.py fix)")
    return [line for _, _, block in rendered for line in block]


def process_file(path, ctx):
    lines = path.read_text(encoding="utf-8").split("\n")
    before = ctx.ranked_items
    out, position = [], 0
    for section, items in top_level_lists(lines):
        out.extend(lines[position:items[0].start])
        out.extend(render_list(lines, items, section, path, ctx))
        position = items[-1].end
    out.extend(lines[position:])
    if ctx.ranked_items > before and not any("RANKING.md" in line for line in out):
        if ctx.fix:
            out = insert_legend(out, legend_line(path))
        else:
            ctx.problems.append(f"{path.relative_to(ROOT)}: legend line linking RANKING.md is missing (run rank.py fix)")
    return "\n".join(out)


def insert_legend(lines, legend):
    """Insert the legend after the first paragraph that follows the H1."""
    i = next((n for n, line in enumerate(lines) if line.startswith("# ")), -1) + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines) and lines[i].strip() and not HEADING.match(lines[i]):
        i += 1
    return lines[:i] + ["", legend] + lines[i:]


def load_sources():
    sources = {}
    if SOURCES_CSV.exists():
        with SOURCES_CSV.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                score = row["score"].strip()
                sources[row["url"].strip()] = {"score": int(score) if score else None, "title": row["title"].strip()}
    return sources


def render_sources_csv(sources):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["score", "title", "url"])
    for url, entry in sorted(sources.items(), key=lambda kv: (-(kv[1]["score"] or 0), kv[1]["title"].lower(), kv[0])):
        writer.writerow(["" if entry["score"] is None else entry["score"], entry["title"], url])
    return buffer.getvalue()


def collect_links():
    """Return {url: [(file, link text, is the first link of a reference entry)]} in document order."""
    used = {}
    for path in guideline_files():
        relative = path.relative_to(ROOT).as_posix()
        lines = path.read_text(encoding="utf-8").split("\n")
        primary = set()
        for section, items in top_level_lists(lines):
            stack = list(items)
            while stack:
                item = stack.pop()
                stack.extend(child for children in item.children for child in children)
                links = LINK.findall(own_text(lines, item))
                if section != RULES_SECTION and links:
                    primary.add(links[0][1])
        in_fence = False
        for line in lines:
            if FENCE.match(line):
                in_fence = not in_fence
            elif not in_fence:
                for text, url in LINK.findall(line):
                    used.setdefault(url, []).append((relative, text, url in primary))
    return used


def display_path(file):
    return file[: -len("/README.md")] if file.endswith("/README.md") else file[: -len(".md")]


def render_sources_md(sources, used):
    out = [
        "# Sources",
        "",
        "Every source linked from the guidelines, grouped by score. The criteria are in [RANKING.md](RANKING.md).",
        "",
        "This file is generated from [sources.csv](sources.csv) by `python3 scripts/rank.py fix`. Change scores in the CSV, not here.",
        "",
    ]
    for low, high, tier, _ in TIERS:
        rows = [(url, entry) for url, entry in sources.items() if entry["score"] and low <= entry["score"] <= high]
        rows.sort(key=lambda row: (-row[1]["score"], row[1]["title"].lower()))
        out += [f"## {tier} ({low}–{high})", "", f"{len(rows)} sources.", "", "| Score | Source | Used in |", "| --- | --- | --- |"]
        for url, entry in rows:
            files = sorted({file for file, _, _ in used.get(url, [])})
            used_in = ", ".join(f"[{display_path(f)}]({f})" for f in files)
            title = entry["title"].replace("|", "\\|")
            out.append(f"| {entry['score']} | [{title}]({url}) | {used_in} |")
        out.append("")
    return "\n".join(out)


def sync_sources(sources, used, ctx):
    """Add new links (unscored) and drop unused ones. Returns the updated mapping."""
    updated = {url: entry for url, entry in sources.items() if url in used}
    for url in sorted(set(sources) - set(used)):
        ctx.problems.append(f"sources.csv: {url} is not used in any guideline (run rank.py fix to remove it)")
    for url, uses in used.items():
        if url not in updated:
            preferred = next((text for _, text, primary in uses if primary), uses[0][1])
            updated[url] = {"score": None, "title": preferred}
            ctx.problems.append(f"sources.csv: {url} has no score yet")
        elif updated[url]["score"] is None:
            ctx.problems.append(f"sources.csv: {url} has no score yet")
        elif not 1 <= updated[url]["score"] <= 10:
            ctx.problems.append(f"sources.csv: {url} has score {updated[url]['score']}, outside 1-10")
    return updated


def run(fix):
    used = collect_links()
    ctx = Context(load_sources(), fix)
    sources = sync_sources(ctx.sources, used, ctx)
    ctx.sources = sources

    for path in guideline_files():
        original = path.read_text(encoding="utf-8")
        result = process_file(path, ctx)
        if fix and result != original:
            path.write_text(result, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")

    expected = {SOURCES_CSV: render_sources_csv(sources), SOURCES_MD: render_sources_md(sources, used)}
    for path, content in expected.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            if fix:
                path.write_text(content, encoding="utf-8")
                print(f"updated {path.relative_to(ROOT)}")
            else:
                ctx.problems.append(f"{path.relative_to(ROOT)} is out of date (run rank.py fix)")
    return ctx


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("check", "fix"):
        print(__doc__)
        return 2
    if sys.argv[1] == "fix":
        run(fix=True)
    ctx = run(fix=False)
    for problem in ctx.problems:
        print(problem)
    if ctx.problems:
        print(f"\n{len(ctx.problems)} problem(s). Scoring criteria: RANKING.md")
        return 1
    print(f"OK: {ctx.ranked_items} ranked entries and {len(ctx.sources)} sources are scored, sorted and in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
