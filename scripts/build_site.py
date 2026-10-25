#!/usr/bin/env python3
"""Build the documentation website with Zensical.

Stages the repository's Markdown into build/site-src/, then builds build/site/:

- README.md becomes the home page, and SKILL.md files become their skill's index page.
- Relative links to files that aren't part of the site (CSV files, scripts, LICENSE, …)
  are rewritten to their GitHub URLs, so no link breaks.
- Every rule gets an anchor, and rule IDs in RULES.md and the checklists link to it.
- The navigation is generated from the indexes, so new files and platforms appear automatically.

Usage: python3 scripts/build_site.py [--serve]    (needs `pip install zensical`)
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
STAGE = BUILD / "site-src"
REPO_URL = "https://github.com/depuschm/architecture-guidelines"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
RULE_LINE = re.compile(r"^(\s*- `\d+` )`([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d+)`", re.M)
SCORE_ITEM = re.compile(r"^(\s*- )`(\d+)` ", re.M)
SCORES_CSS = """/* Score chips, coloured by level (see RANKING.md). */
.score { display: inline-block; min-width: 1.6em; padding: 0 .35em; border-radius: .6em; font-size: .75em;
  font-weight: 700; text-align: center; line-height: 1.6; vertical-align: .1em; color: #fff; }
.score-high { background: #2e7d32; }
.score-mid { background: #1565c0; }
.score-low { background: #757575; }
"""
ID_CELL = re.compile(r"(?<![\[\w])`([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d+)`(?!\])")


def site_pages():
    """Map repository paths to staged paths for every page on the site."""
    pages = {Path("README.md"): Path("index.md")}
    for name in ("RANKING.md", "SOURCES.md", "RULES.md", "CONTRIBUTING.md"):
        pages[Path(name)] = Path(name)
    for folder in ("general", "specific", "checklists", "docs/decisions"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            relative = path.relative_to(ROOT)
            if not any(part.startswith("_") for part in relative.parts):
                pages[relative] = relative
    for path in sorted((ROOT / "skills").glob("*/*.md")):
        relative = path.relative_to(ROOT)
        pages[relative] = relative.with_name("README.md") if path.name == "SKILL.md" else relative
    pages[Path("evals/README.md")] = Path("evals/README.md")
    return pages


def rewrite_links(text, source, staged, pages):
    """Point relative links at staged pages, or at GitHub for files that aren't on the site."""

    def replace(match):
        target = match.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            return match.group(0)
        path_part, _, fragment = target.partition("#")
        resolved = (ROOT / source.parent / path_part).resolve()
        try:
            repo_path = resolved.relative_to(ROOT)
        except ValueError:
            return match.group(0)
        anchor = f"#{fragment}" if fragment else ""
        if repo_path in pages:
            relative = Path(*[".."] * len(staged.parent.parts)) / pages[repo_path] if staged.parent.parts else pages[repo_path]
            return f"{match.group(1)}{relative.as_posix()}{anchor}{match.group(3)}"
        kind = "tree" if resolved.is_dir() else "blob"
        return f"{match.group(1)}{REPO_URL}/{kind}/main/{repo_path.as_posix()}{anchor}{match.group(3)}"

    return LINK.sub(replace, text)


def link_rule_ids(text, staged, rule_pages):
    """In RULES.md and checklists, link each rule ID to its anchor in the guideline file."""

    def replace(match):
        rule_id = match.group(1)
        if rule_id not in rule_pages:
            return match.group(0)
        target = Path(*[".."] * len(staged.parent.parts)) / rule_pages[rule_id] if staged.parent.parts else rule_pages[rule_id]
        return f"[`{rule_id}`]({target.as_posix()}#{rule_id})"

    return ID_CELL.sub(replace, text)


def score_chips(text):
    """Turn the leading `N` of list items into a coloured chip."""

    def replace(match):
        score = int(match.group(2))
        level = "high" if score >= 9 else "mid" if score >= 6 else "low"
        return f'{match.group(1)}<span class="score score-{level}" title="Score {score} of 10">{score}</span> '

    return SCORE_ITEM.sub(replace, text)


def stage():
    if STAGE.exists():
        shutil.rmtree(STAGE)
    pages = site_pages()
    rule_pages = {}
    texts = {}
    for source, staged in pages.items():
        text = (ROOT / source).read_text(encoding="utf-8")
        text = rewrite_links(text, source, staged, pages)
        if source.parts[0] in ("general", "specific"):
            for match in RULE_LINE.finditer(text):
                rule_pages[match.group(2)] = staged
            text = RULE_LINE.sub(lambda m: f'{m.group(1)}<span id="{m.group(2)}"></span>`{m.group(2)}`', text)
            text = score_chips(text)
        texts[staged] = text
    for staged, text in texts.items():
        if staged.name == "RULES.md" or staged.parts[0] == "checklists":
            text = link_rule_ids(text, staged, rule_pages)
        target = STAGE / staged
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    (STAGE / "assets").mkdir(exist_ok=True)
    (STAGE / "assets" / "scores.css").write_text(SCORES_CSS, encoding="utf-8")
    return pages


def title(path):
    for line in (STAGE / path).read_text(encoding="utf-8").split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def ordered_links(index):
    """Relative .md links in the order an index page lists them."""
    text = (STAGE / index).read_text(encoding="utf-8")
    found = []
    for target in re.findall(r"\]\(([^)#\s]+\.md)", text):
        path = (index.parent / target)
        normalised = Path(*[p for p in path.parts if p != "."])
        parts = []
        for part in normalised.parts:
            if part == ".." and parts:
                parts.pop()
            else:
                parts.append(part)
        candidate = Path(*parts)
        if (STAGE / candidate).exists() and candidate not in found:
            found.append(candidate)
    return found


def section(index, extra=()):
    """An index page followed by the pages it links to inside its folder, then any others."""
    folder = index.parent
    pages = [index]
    for path in list(ordered_links(index)) + sorted(extra):
        if path.parent == folder and path not in pages:
            pages.append(path)
    for path in sorted((STAGE / folder).glob("*.md")):
        relative = path.relative_to(STAGE)
        if relative not in pages:
            pages.append(relative)
    return pages


def toml_string(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def nav_entry(label, pages):
    items = ", ".join(toml_string(p.as_posix()) for p in pages)
    return f"{{ {toml_string(label)} = [{items}] }}"


def navigation():
    entries = [f'{{ "Home" = "index.md" }}']
    entries.append(nav_entry("General", section(Path("general/README.md"))))
    platforms = []
    for folder in ordered_links(Path("specific/README.md")):
        if folder.name == "README.md" and folder.parent.parts[:1] == ("specific",):
            platforms.append(nav_entry(title(folder), section(folder)))
    entries.append(f'{{ "Platforms" = [{toml_string("specific/README.md")}, {", ".join(platforms)}] }}')
    checklists = sorted(p.relative_to(STAGE) for p in (STAGE / "checklists").glob("*.md"))
    checklists.sort(key=lambda p: (p.stem != "general", p.stem))
    entries.append(nav_entry("Checklists", checklists))
    entries.append(nav_entry("Reference", [Path("RULES.md"), Path("SOURCES.md"), Path("RANKING.md")]))
    skills = sorted(p.relative_to(STAGE) for p in (STAGE / "skills").glob("*/README.md"))
    entries.append(nav_entry("AI skills", skills + [Path("evals/README.md")]))
    entries.append(nav_entry("Decisions", section(Path("docs/decisions/README.md"))))
    entries.append(f'{{ "Contributing" = "CONTRIBUTING.md" }}')
    return "nav = [\n  " + ",\n  ".join(entries) + ",\n]\n"


def write_config():
    base = (ROOT / "zensical.toml").read_text(encoding="utf-8")
    generated = 'docs_dir = "site-src"\nsite_dir = "site"\nextra_css = ["assets/scores.css"]\n' + navigation()
    config = base.replace("[project]\n", "[project]\n" + generated, 1)
    path = BUILD / "zensical.toml"
    path.write_text(config, encoding="utf-8")
    return path


def main():
    stage()
    config = write_config()
    command = ["zensical", "serve" if "--serve" in sys.argv else "build", "--config-file", str(config)]
    if "--serve" not in sys.argv:
        command += ["--clean", "--strict"]
    return subprocess.call(command)


if __name__ == "__main__":
    sys.exit(main())
