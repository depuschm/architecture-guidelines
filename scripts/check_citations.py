#!/usr/bin/env python3
"""Check the repository's citation rule.

1. Every leaf list item and every table data row in Markdown files under
   general/ and specific/ must contain at least one link (its source).
   Folders whose name starts with "_" (templates) are skipped.
2. Relative links in all Markdown files must point to files that exist.

Usage: python3 scripts/check_citations.py
Exit code 1 if any problem is found.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDELINE_DIRS = ["general", "specific"]
SKIP_DIRS = {".git", "node_modules"}

LIST_ITEM = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+(.*)$")
HEADING = re.compile(r"^\s*#{1,6}\s")
FENCE = re.compile(r"^\s*(```|~~~)")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEPARATOR = re.compile(r"^\s*\|?(\s*:?-+:?\s*\|)+\s*:?-*:?\s*\|?\s*$")
LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)|<(https?://[^>\s]+)>")
INLINE_CODE = re.compile(r"`[^`]*`")


def strip_code_and_comments(lines):
    """Yield (line_number, text), blanking fenced code blocks and HTML comments."""
    in_fence = False
    in_comment = False
    for number, line in enumerate(lines, start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            yield number, ""
            continue
        if in_fence:
            yield number, ""
            continue
        text = line
        if in_comment:
            end = text.find("-->")
            if end == -1:
                yield number, ""
                continue
            text = text[end + 3:]
            in_comment = False
        while "<!--" in text:
            start = text.find("<!--")
            end = text.find("-->", start + 4)
            if end == -1:
                text = text[:start]
                in_comment = True
                break
            text = text[:start] + text[end + 3:]
        yield number, text.rstrip("\n")


def links_in(text):
    for match in LINK.finditer(INLINE_CODE.sub("", text)):
        yield match.group(1) or match.group(2)


def check_citations(path, lines):
    """Return problems for list items and table rows without a link."""
    problems = []
    items = []  # dicts: line, indent, text, list_id
    list_id = 0
    current = None
    previous_blank = False
    table_state = None  # None, "header", "body"

    for number, line in strip_code_and_comments(lines):
        if not line.strip():
            previous_blank = True
            table_state = None
            continue

        if TABLE_ROW.match(line):
            current = None
            if table_state is None:
                table_state = "header"
            elif table_state == "header" and TABLE_SEPARATOR.match(line):
                table_state = "body"
            elif table_state == "body" and not any(links_in(line)):
                problems.append(f"{path}:{number}: table row has no source link: {line.strip()[:80]}")
            previous_blank = False
            continue
        table_state = None

        if HEADING.match(line):
            list_id += 1
            current = None
        elif match := LIST_ITEM.match(line):
            current = {"line": number, "indent": len(match.group(1)), "text": match.group(2), "list_id": list_id}
            items.append(current)
        else:
            indent = len(line) - len(line.lstrip())
            if current is not None and (indent > current["indent"] or not previous_blank):
                current["text"] += " " + line.strip()
            else:
                list_id += 1
                current = None
        previous_blank = False

    for index, item in enumerate(items):
        following = items[index + 1] if index + 1 < len(items) else None
        is_parent = following is not None and following["list_id"] == item["list_id"] and following["indent"] > item["indent"]
        if not is_parent and not any(links_in(item["text"])):
            problems.append(f"{path}:{item['line']}: list item has no source link: {item['text'][:80]}")
    return problems


def check_relative_links(path, lines):
    """Return problems for relative links whose target file does not exist."""
    problems = []
    for number, line in strip_code_and_comments(lines):
        for target in links_in(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0].split("?", 1)[0]
            if file_part and not (ROOT / path.parent / file_part).exists():
                problems.append(f"{path}:{number}: broken relative link: {target}")
    return problems


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def main():
    problems = []
    checked = 0
    for path in markdown_files():
        relative = path.relative_to(ROOT)
        lines = path.read_text(encoding="utf-8").splitlines()
        problems += check_relative_links(relative, lines)
        parts = relative.parts
        if parts[0] in GUIDELINE_DIRS and not any(part.startswith("_") for part in parts):
            checked += 1
            problems += check_citations(relative, lines)

    for problem in problems:
        print(problem)
    if problems:
        print(f"\n{len(problems)} problem(s) found. Every guideline statement needs a source link (see CONTRIBUTING.md).")
        return 1
    print(f"OK: {checked} guideline files checked, every list item and table row has a source link.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
