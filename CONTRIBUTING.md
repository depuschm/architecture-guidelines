# Contributing

## 1. Reference first

Before writing anything, look for an existing guideline that covers the topic. Prefer sources in this order:

1. Official documentation from the platform or vendor (Unity, Microsoft, Google, AWS, Kubernetes, …)
2. Standards and specifications (RFCs, ISO, OpenAPI, OWASP, NIST)
3. Recognised practitioners and their primary publications (books, original articles)
4. Well-maintained community guides and reference implementations

If such a source exists, **add it under "Adopted references"** with one line saying what it covers and when to use it. Don't restate its content.

Write your own rule under "Key rules" only when:

- no single source covers the point, or several sources need to be combined,
- sources disagree and we have to pick one, or
- the team needs to choose between options the sources leave open.

Even then, the rule must link to the source(s) that support it.

**General rule or platform rule?** Check [RULES.md](RULES.md) before adding a rule. If a general rule already states the principle, a platform rule should add only the platform's how-to (the API, setting or tool) and name the general rule's ID, not restate it. When three or more platform files need the same principle, add it to `general/` and keep the platform rules to their how-to.

## 2. File format

Every guideline file in `general/` and `specific/` uses these sections. Leave out any section that would be empty.

```markdown
<!-- rule-prefix: TOPIC -->
# Topic

One or two sentences on scope.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): … (added by rank.py fix)

## Adopted references

- `9` [Title](https://…): what it covers and when to use it.

## Key rules

- `8` `TOPIC-1` **Short imperative rule.** One sentence of explanation. ([Source](https://…))

## How to enforce

- `7` [Tool](https://…): what it checks automatically. Checks `TOPIC-1`.

## Tutorials and further reading

- `6` [Title](https://…): what you will learn.
```

Rules:

- **Every list item must contain a link.** A parent item whose sub-items each have a link is fine. Prose paragraphs give context only. Don't put rules in them.
- **Every reference entry and key rule starts with its score** in backticks. **Key rules also have an ID.** See [Scores, IDs and freshness](#3-scores-ids-and-freshness) below.
- **"How to enforce"** lists tools that check rules automatically (in CI, the IDE or a commit hook). Name the rule IDs each tool checks, and link the tool's documentation of that check.
- Link to the most specific page that supports the statement, not to a site's home page.
- Keep rules short. If a rule needs more than two sentences, the source probably deserves an "Adopted references" entry instead.
- Don't paste large excerpts from sources. Summarise in your own words and link.

## 3. Scores, IDs and freshness

**Scores.** Every source and every key rule has a score from 1 to 10. [RANKING.md](RANKING.md) defines the criteria and levels.

- **Sources**: the score lives in [sources.csv](sources.csv), one row per URL. A reference entry shows the score of its first link.
- **Key rules**: the score is written at the start of the rule, for example `` `8` `SEC-3` **Rule.** ``.

**Rule IDs.** Every key rule has a stable ID, made of the file's prefix and a number, such as `SEC-3` or `UNITY-STRUCT-2`. The prefix is declared on the file's first line as `<!-- rule-prefix: SEC -->`.

- New rules get the next free number automatically. Don't pick numbers yourself.
- A rule keeps its ID when it's reworded, re-scored or re-sorted.
- When a rule is removed, its ID is retired in [rules.csv](rules.csv) and never reused. To move a rule to another file, remove it and add it as a new rule there.
- [RULES.md](RULES.md) lists every rule by ID.

**Freshness.** Each source has a `verified` date in `sources.csv`, the last time someone confirmed the page still says what the guidelines cite it for.

- New links get today's date. You must have verified them (see AGENTS.md).
- Sources older than a year show up in the CI summary. Re-verify them with the `reverify-sources` project skill, or by hand: read the page, then update the date or fix the rule.

After adding or changing entries, run:

```bash
python3 scripts/rank.py fix
```

The command:

- adds new links to `sources.csv` with an empty score and removes unused ones,
- copies scores into the reference entries and gives new rules an ID,
- sorts every list by score,
- regenerates [SOURCES.md](SOURCES.md) and [RULES.md](RULES.md).

Fill in the empty scores, then run it again. Lists must be tight (no blank lines between items) to be sorted.

## 4. Adding a platform folder

1. Copy `specific/_template/` to `specific/<platform>/` (lower-case, hyphenated).
2. Fill in `README.md`, and set a new, unique rule prefix in its first line. Split into more files only when the README gets long (see `specific/unity/`). Each file with key rules needs its own prefix.
3. Add the platform to the table in the root [README.md](README.md) and in [specific/README.md](specific/README.md).
4. Add its detection hints to the platform table in [skills/architecture-review/SKILL.md](skills/architecture-review/SKILL.md).

## 5. Checks

Run these before opening a pull request:

```bash
python3 scripts/check_citations.py                     # every list item has a link
python3 scripts/rank.py check                          # scores, IDs, sort order, SOURCES.md and RULES.md
python3 scripts/verify_sources.py                      # no broken or retired sources (needs network)
python3 scripts/verify_sources.py --stale              # sources not verified in the last year
lychee --config lychee.toml './**/*.md'                # links resolve (https://lychee.cli.rs/)
claude plugin validate .                               # plugin and marketplace manifests are valid
zizmor .                                               # workflows follow GHA-1 to GHA-4 (https://docs.zizmor.sh/)
```

To preview the website, install the generator once and build or serve it:

```bash
pip install -r requirements.txt
python3 scripts/build_site.py            # builds build/site/ in strict mode, like CI
python3 scripts/build_site.py --serve    # live preview at http://localhost:8000
```

The script stages the Markdown and generates the navigation from the indexes, so a new file or platform appears on the site once it's linked from its index. Links to files that aren't on the site, such as CSV files and scripts, point to GitHub.

CI runs the same checks on every push and pull request, and weekly to catch link rot and retired pages. `verify_sources.py` catches pages that still answer HTTP 200 but redirect to a home, 404 or "deprecated" page, or that serve an empty page marked `noindex`, which a plain link checker misses. A titled page marked `noindex` is reported as suspect: Unity Learn, for example, marks retired courses that way.

### Sites that block automated link checks

Some sites return `403` to bots even when the page exists. They are listed in [`lychee.toml`](lychee.toml) under `exclude`. Check those links by hand, and only add a domain to the list after confirming in a browser that the page works.

## 6. Licensing of contributions

By contributing, you agree that guideline content is licensed under [CC BY 4.0](LICENSE), and code and skills under [MIT](LICENSE-CODE), as described in the [README](README.md#license).

## 7. Changing the skills

Skills live in `skills/<name>/SKILL.md` ([Agent Skills format](https://agentskills.io/specification)). Keep the `name` field equal to the folder name. Keep `description` under 1024 characters and lead with what the skill does and when to use it. Skills must cite guideline files and their sources, and must not invent rules or links. After changing a skill, run its evals (see [evals/README.md](evals/README.md)), and add a case when you add a skill.
