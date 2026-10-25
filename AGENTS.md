# Instructions for AI agents

This repository is a curated, source-linked collection of software architecture guidelines plus AI skills that apply them.

## Using the guidelines (in other projects)

- Guidelines live in `general/` (technology-independent) and `specific/<platform>/`.
- When you apply or cite a guideline, use the rule's ID (for example `SEC-3`, listed in [RULES.md](RULES.md)) and include the rule's source link.
- Every source and rule has a score from 1 to 10 ([RANKING.md](RANKING.md)), and lists are sorted by it. Read the highest-scored entries first. Use rule scores to weigh findings: 9–10 strongly recommended, 6–8 recommended, 1–5 conditional.
- Don't invent rules or links. If no guideline covers a question, say so.
- Skills in `skills/` show the intended workflows (architecture review, enforcing guidelines in CI, ADRs, C4 diagrams, Unity architecture).

## Editing this repository

Follow [CONTRIBUTING.md](CONTRIBUTING.md). The rules that matter most:

1. **Reference first.** If an authoritative guideline exists, add it under "Adopted references" instead of rewriting it.
2. **Every list item in `general/` and `specific/` must contain a link** to a source that supports it. Prose paragraphs are for context only.
3. **Verify every link you add** by fetching it. Make sure it loads and actually supports the statement. Never add a URL from memory without checking it.
4. **Score every new entry** following [RANKING.md](RANKING.md): sources in `sources.csv`, rules inline. Then run `python3 scripts/rank.py fix`, which assigns rule IDs. Never edit or reuse rule IDs by hand.
5. Run `python3 scripts/check_citations.py` and `python3 scripts/rank.py check` after editing guideline files.
6. When adding a platform folder, update the indexes in `README.md` and `specific/README.md` and the detection table in `skills/architecture-review/SKILL.md`.
