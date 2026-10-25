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

## 2. File format

Every guideline file in `general/` and `specific/` uses these sections. Leave out any section that would be empty.

```markdown
# Topic

One or two sentences on scope.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): … (added by rank.py fix)

## Adopted references

- `9` [Title](https://…): what it covers and when to use it.

## Key rules

- `8` **Short imperative rule.** One sentence of explanation. ([Source](https://…))

## Tutorials and further reading

- `6` [Title](https://…): what you will learn.
```

Rules:

- **Every list item must contain a link.** A parent item whose sub-items each have a link is fine. Prose paragraphs give context only. Don't put rules in them.
- **Every reference entry and key rule starts with its score** in backticks. See [Scores](#3-scores) below.
- Link to the most specific page that supports the statement, not to a site's home page.
- Keep rules short. If a rule needs more than two sentences, the source probably deserves an "Adopted references" entry instead.
- Don't paste large excerpts from sources. Summarise in your own words and link.

## 3. Scores

Every source and every key rule has a score from 1 to 10. [RANKING.md](RANKING.md) defines the criteria and levels.

- **Sources**: the score lives in [sources.csv](sources.csv), one row per URL. A reference entry shows the score of its first link.
- **Key rules**: the score is written at the start of the rule, for example `` `8` **Rule.** ``.

After adding or changing entries, run:

```bash
python3 scripts/rank.py fix
```

The command adds new links to `sources.csv` with an empty score and removes unused ones. It also copies scores into the reference entries, sorts every list by score, and regenerates [SOURCES.md](SOURCES.md). Fill in the empty scores, then run it again. Lists must be tight (no blank lines between items) to be sorted.

## 4. Adding a platform folder

1. Copy `specific/_template/` to `specific/<platform>/` (lower-case, hyphenated).
2. Fill in `README.md`. Split into more files only when the README gets long (see `specific/unity/`).
3. Add the platform to the table in the root [README.md](README.md) and in [specific/README.md](specific/README.md).
4. Add its detection hints to the platform table in [skills/architecture-review/SKILL.md](skills/architecture-review/SKILL.md).

## 5. Checks

Run these before opening a pull request:

```bash
python3 scripts/check_citations.py                     # every list item has a link
python3 scripts/rank.py check                          # every entry is scored, lists are sorted, SOURCES.md is current
lychee --config lychee.toml './**/*.md'                # links resolve (https://lychee.cli.rs/)
claude plugin validate .                               # plugin and marketplace manifests are valid
```

CI runs the same checks on every push and pull request, and runs the link check weekly to catch link rot.

### Sites that block automated link checks

Some sites return `403` to bots even when the page exists. They are listed in [`lychee.toml`](lychee.toml) under `exclude`. Check those links by hand, and only add a domain to the list after confirming in a browser that the page works.

## 6. Licensing of contributions

By contributing, you agree that guideline content is licensed under [CC BY 4.0](LICENSE), and code and skills under [MIT](LICENSE-CODE), as described in the [README](README.md#license).

## 7. Changing the skills

Skills live in `skills/<name>/SKILL.md` ([Agent Skills format](https://agentskills.io/specification)). Keep the `name` field equal to the folder name. Keep `description` under 1024 characters and lead with what the skill does and when to use it. Skills must cite guideline files and their sources, and must not invent rules or links.
