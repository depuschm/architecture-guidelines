#!/usr/bin/env python3
"""Check and maintain scores, rule IDs and the source and rule registries.

Every reference entry and every key rule in general/ and specific/ starts with
its score in backticks. Key rules also carry a stable ID after the score, for
example "- `9` `SEC-3` **Rule.** ...". Reference entries take their score from
sources.csv (the score of their first link). Lists are sorted by score, highest
first. Rule IDs are registered in rules.csv and never reused. SOURCES.md and
RULES.md are generated. The scoring criteria are in RANKING.md.

Usage:
  python3 scripts/rank.py check   Verify scores, IDs, sort order and generated files (used by CI).
  python3 scripts/rank.py fix     Apply scores from sources.csv, give new rules an ID, sort lists,
                                  add the legend line, add new links to sources.csv (score left
                                  empty for you to fill in, verified date set to today), remove
                                  unused links, and regenerate SOURCES.md and RULES.md.
"""

import csv
import datetime
import io
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDELINE_DIRS = ["general", "specific"]
SOURCES_CSV = ROOT / "sources.csv"
SOURCES_MD = ROOT / "SOURCES.md"
RULES_CSV = ROOT / "rules.csv"
RULES_MD = ROOT / "RULES.md"
RANKING_MD = ROOT / "RANKING.md"

LIST_ITEM = re.compile(r"^( *)(?:[-*+]|\d+[.)]) +(.*)$")
HEADING = re.compile(r"^(#{1,6}) +(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
SCORE = re.compile(r"^`(\d+)` +")
RULE_ID = re.compile(r"^`([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*)-(\d+)` +")
PREFIX = re.compile(r"<!--\s*rule-prefix:\s*([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*)\s*-->")
LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
TITLE = re.compile(r"\*\*(.+?)\*\*")
RULES_SECTION = "Key rules"
ENFORCE_SECTION = "How to enforce"
ID_MENTION = re.compile(r"`([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d+)`")

# (lowest score, highest score, name for sources, name for rules)
TIERS = [
    (9, 10, "Start here", "Strongly recommended"),
    (6, 8, "Recommended", "Recommended"),
    (1, 5, "Further reading", "Conditional"),
]


def today():
    return datetime.date.today().isoformat()


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


def level(score, rules):
    for low, high, source_tier, rule_tier in TIERS:
        if low <= score <= high:
            return rule_tier if rules else source_tier
    return ""


# ---------------------------------------------------------------- parsing


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


def split_prefixes(text):
    """Split '`9` `SEC-3` rest' into (score, (prefix, number) or None, rest)."""
    score = SCORE.match(text)
    if score:
        text = text[score.end():]
    rule_id = RULE_ID.match(text)
    if rule_id:
        text = text[rule_id.end():]
    return (
        int(score.group(1)) if score else None,
        (rule_id.group(1), int(rule_id.group(2))) if rule_id else None,
        text,
    )


# ---------------------------------------------------------------- registries


def load_sources():
    sources = {}
    if SOURCES_CSV.exists():
        with SOURCES_CSV.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                score = row["score"].strip()
                sources[row["url"].strip()] = {
                    "score": int(score) if score else None,
                    "title": row["title"].strip(),
                    "verified": (row.get("verified") or "").strip(),
                }
    return sources


def render_sources_csv(sources):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["score", "title", "url", "verified"])
    for url, entry in sorted(sources.items(), key=lambda kv: (-(kv[1]["score"] or 0), kv[1]["title"].lower(), kv[0])):
        writer.writerow(["" if entry["score"] is None else entry["score"], entry["title"], url, entry["verified"]])
    return buffer.getvalue()


def id_key(rule_id):
    prefix, _, number = rule_id.rpartition("-")
    return (prefix, int(number))


def load_rules():
    rules = {}
    if RULES_CSV.exists():
        with RULES_CSV.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                rules[row["id"].strip()] = {"status": row["status"].strip(), "title": row["title"].strip()}
    return rules


def render_rules_csv(rules):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["id", "status", "title"])
    for rule_id in sorted(rules, key=id_key):
        writer.writerow([rule_id, rules[rule_id]["status"], rules[rule_id]["title"]])
    return buffer.getvalue()


# ---------------------------------------------------------------- processing


class Context:
    def __init__(self, sources, rules, fix):
        self.sources, self.rules, self.fix = sources, rules, fix
        self.problems = []
        self.ranked_items = 0
        self.rule_records = []  # (id, file, score, title) in document order
        self.enforcement = []  # (rule id, tool name, file:line) from "How to enforce" sections
        self.next_number = {}

    def allocate(self, prefix):
        number = self.next_number.get(prefix, 1)
        self.next_number[prefix] = number + 1
        return number


def render_item(lines, item, section, path, prefix, ctx):
    """Return (kind, score, lines) for one item, with its nested lists rendered."""
    first = lines[item.start]
    match = LIST_ITEM.match(first)
    text = own_text(lines, item)
    current_score, current_id, rest_text = split_prefixes(text)
    links = LINK.findall(rest_text)
    kind = "rule" if section == RULES_SECTION else ("reference" if links else None)
    relative = path.relative_to(ROOT).as_posix()
    where = f"{relative}:{item.start + 1}"
    score = None
    if kind:
        ctx.ranked_items += 1
        if kind == "reference":
            url = links[0][1]
            entry = ctx.sources.get(url)
            score = entry["score"] if entry else None
            if score is None:
                ctx.problems.append(f"{where}: no score in sources.csv for {url}")
            elif current_score != score and not ctx.fix:
                shown = f"`{current_score}`" if current_score is not None else "no score"
                ctx.problems.append(f"{where}: has {shown}, but sources.csv says `{score}` (run rank.py fix)")
            if current_id:
                ctx.problems.append(f"{where}: only key rules have IDs; remove `{current_id[0]}-{current_id[1]}`")
            if section == ENFORCE_SECTION:
                mentioned = ID_MENTION.findall(rest_text)
                if not mentioned:
                    ctx.problems.append(f"{where}: enforcement entry names no rule ID it checks")
                for rule in mentioned:
                    ctx.enforcement.append((rule, links[0][0], where))
        else:
            score = current_score
            if score is None:
                ctx.problems.append(f"{where}: key rule has no score, start it with `N` (1-10)")
            rule_id = current_id
            if prefix is None:
                ctx.problems.append(f"{relative}: has key rules but no <!-- rule-prefix: XYZ --> comment")
            elif rule_id is None:
                if ctx.fix:
                    rule_id = (prefix, ctx.allocate(prefix))
                else:
                    ctx.problems.append(f"{where}: key rule has no ID (run rank.py fix)")
            elif rule_id[0] != prefix:
                ctx.problems.append(f"{where}: rule ID {rule_id[0]}-{rule_id[1]} doesn't match this file's prefix {prefix}")
            if rule_id:
                title = TITLE.search(rest_text)
                ctx.rule_records.append(
                    (f"{rule_id[0]}-{rule_id[1]}", relative, score, title.group(1) if title else rest_text[:100])
                )
            current_id_text = f"`{rule_id[0]}-{rule_id[1]}` " if rule_id else ""
        if score is not None and not 1 <= score <= 10:
            ctx.problems.append(f"{where}: score {score} is outside 1-10")
        if ctx.fix and score is not None:
            line_rest = split_prefixes(match.group(2))[2]
            id_text = current_id_text if kind == "rule" else ""
            first = first[: match.start(2)] + f"`{score}` " + id_text + line_rest
    out = [first]
    k = item.start + 1
    for children in item.children:
        out.extend(lines[k:children[0].start])
        out.extend(render_list(lines, children, section, path, prefix, ctx))
        k = children[-1].end
    out.extend(lines[k:item.end])
    return kind, score, out


def render_list(lines, items, section, path, prefix, ctx):
    rendered = [render_item(lines, item, section, path, prefix, ctx) for item in items]
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
    prefix = next((m.group(1) for m in map(PREFIX.search, lines) if m), None)
    before = ctx.ranked_items
    out, position = [], 0
    for section, items in top_level_lists(lines):
        out.extend(lines[position:items[0].start])
        out.extend(render_list(lines, items, section, path, prefix, ctx))
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


def existing_rule_numbers():
    """Highest rule number per prefix, from the registry and from the guideline files."""
    highest = {}
    for rule_id in load_rules():
        prefix, number = id_key(rule_id)
        highest[prefix] = max(highest.get(prefix, 0), number)
    pattern = re.compile(r"^\s*[-*+] `\d+` `([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*)-(\d+)`")
    for path in guideline_files():
        for line in path.read_text(encoding="utf-8").split("\n"):
            match = pattern.match(line)
            if match:
                highest[match.group(1)] = max(highest.get(match.group(1), 0), int(match.group(2)))
    return {prefix: number + 1 for prefix, number in highest.items()}


def sync_rules(ctx):
    """Check rule IDs for duplicates and reuse, and return the updated registry."""
    seen = {}
    for rule_id, file, _, _ in ctx.rule_records:
        if rule_id in seen:
            ctx.problems.append(f"{file}: rule ID {rule_id} is also used in {seen[rule_id]}")
        seen[rule_id] = file
        if ctx.rules.get(rule_id, {}).get("status") == "retired":
            ctx.problems.append(f"{file}: rule ID {rule_id} was retired; IDs are never reused (remove it and run rank.py fix)")
    registry = {rule_id: dict(entry) for rule_id, entry in ctx.rules.items()}
    for rule_id, entry in registry.items():
        if rule_id not in seen and entry["status"] == "active":
            entry["status"] = "retired"
    for rule_id, _, _, title in ctx.rule_records:
        if registry.get(rule_id, {}).get("status") != "retired":
            registry[rule_id] = {"status": "active", "title": title}
    return registry


# ---------------------------------------------------------------- generated files


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
        "*Verified* is the date someone last checked that the page still says what the guidelines cite it for.",
        "",
        "This file is generated from [sources.csv](sources.csv) by `python3 scripts/rank.py fix`. Change scores in the CSV, not here.",
        "",
    ]
    for low, high, tier, _ in TIERS:
        rows = [(url, entry) for url, entry in sources.items() if entry["score"] and low <= entry["score"] <= high]
        rows.sort(key=lambda row: (-row[1]["score"], row[1]["title"].lower()))
        out += [f"## {tier} ({low}–{high})", "", f"{len(rows)} sources.", "",
                "| Score | Source | Used in | Verified |", "| --- | --- | --- | --- |"]
        for url, entry in rows:
            files = sorted({file for file, _, _ in used.get(url, [])})
            used_in = ", ".join(f"[{display_path(f)}]({f})" for f in files)
            title = entry["title"].replace("|", "\\|")
            out.append(f"| {entry['score']} | [{title}]({url}) | {used_in} | {entry['verified']} |")
        out.append("")
    return "\n".join(out)


def render_rules_md(records, registry, enforcement):
    out = [
        "# Rules",
        "",
        "Every key rule by ID, grouped by file and sorted by score. The scoring criteria are in [RANKING.md](RANKING.md).",
        "",
        "IDs are stable: a rule keeps its ID when it is reworded, re-scored or re-sorted, and the ID of a removed rule is never reused.",
        "Cite rules by ID in reviews, ADRs and pull requests, for example `SEC-3`.",
        "*Checked by* lists tools from the files' \"How to enforce\" sections that check the rule automatically.",
        "",
        "This file is generated by `python3 scripts/rank.py fix`. Edit the guideline files, not this file.",
        "",
    ]
    files = []
    for rule_id, file, score, title in records:
        if file not in files:
            files.append(file)
    for file in files:
        out += [f"## [{display_path(file)}]({file})", "", "| ID | Score | Level | Rule | Checked by |", "| --- | --- | --- | --- | --- |"]
        for rule_id, rule_file, score, title in records:
            if rule_file == file:
                tools = ", ".join(sorted({tool for rid, tool, _ in enforcement if rid == rule_id}, key=str.lower))
                out.append(f"| `{rule_id}` | {score} | {level(score or 0, True)} | {title.replace('|', chr(92) + '|')} | {tools} |")
        out.append("")
    retired = sorted((rid for rid, entry in registry.items() if entry["status"] == "retired"), key=id_key)
    if retired:
        out += ["## Retired IDs", "", "These IDs belonged to rules that were removed. They are not reused.", ""]
        out += [f"- `{rid}`: {registry[rid]['title']}" for rid in retired]
        out.append("")
    return "\n".join(out)


def sync_sources(sources, used, ctx):
    """Add new links (unscored, verified today) and drop unused ones. Returns the updated mapping."""
    updated = {url: entry for url, entry in sources.items() if url in used}
    for url in sorted(set(sources) - set(used)):
        ctx.problems.append(f"sources.csv: {url} is not used in any guideline (run rank.py fix to remove it)")
    for url, uses in used.items():
        if url not in updated:
            preferred = next((text for _, text, primary in uses if primary), uses[0][1])
            updated[url] = {"score": None, "title": preferred, "verified": today()}
            ctx.problems.append(f"sources.csv: {url} has no score yet")
        elif updated[url]["score"] is None:
            ctx.problems.append(f"sources.csv: {url} has no score yet")
        elif not 1 <= updated[url]["score"] <= 10:
            ctx.problems.append(f"sources.csv: {url} has score {updated[url]['score']}, outside 1-10")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", updated[url]["verified"]):
            ctx.problems.append(f"sources.csv: {url} has no valid verified date (YYYY-MM-DD)")
    return updated


def run(fix):
    used = collect_links()
    ctx = Context(load_sources(), load_rules(), fix)
    ctx.next_number = existing_rule_numbers()
    ctx.sources = sync_sources(ctx.sources, used, ctx)

    for path in guideline_files():
        original = path.read_text(encoding="utf-8")
        result = process_file(path, ctx)
        if fix and result != original:
            path.write_text(result, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")

    registry = sync_rules(ctx)
    active = {rule_id for rule_id, _, _, _ in ctx.rule_records}
    for rule_id, _, where in ctx.enforcement:
        if rule_id not in active:
            ctx.problems.append(f"{where}: checks `{rule_id}`, which is not an active rule ID")
    expected = {
        SOURCES_CSV: render_sources_csv(ctx.sources),
        SOURCES_MD: render_sources_md(ctx.sources, used),
        RULES_CSV: render_rules_csv(registry),
        RULES_MD: render_rules_md(ctx.rule_records, registry, ctx.enforcement),
    }
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
    for problem in dict.fromkeys(ctx.problems):
        print(problem)
    if ctx.problems:
        print(f"\n{len(set(ctx.problems))} problem(s). See RANKING.md and CONTRIBUTING.md.")
        return 1
    rules = len(ctx.rule_records)
    print(f"OK: {ctx.ranked_items} ranked entries ({rules} rules with IDs) and {len(ctx.sources)} sources are scored, sorted and in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
