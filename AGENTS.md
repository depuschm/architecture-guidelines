# Instructions for AI agents

This repository is a curated, source-linked collection of software architecture guidelines plus AI skills that apply them.

## Using the guidelines (in other projects)

- Guidelines live in `general/` (technology-independent) and `specific/<platform>/`.
- When you apply or cite a guideline, name the file and rule, and include the rule's source link.
- Don't invent rules or links. If no guideline covers a question, say so.
- Skills in `skills/` show the intended workflows (architecture review, ADRs, C4 diagrams, Unity architecture).

## Editing this repository

Follow [CONTRIBUTING.md](CONTRIBUTING.md). The rules that matter most:

1. **Reference first.** If an authoritative guideline exists, add it under "Adopted references" instead of rewriting it.
2. **Every list item in `general/` and `specific/` must contain a link** to a source that supports it. Prose paragraphs are for context only.
3. **Verify every link you add** by fetching it. Make sure it loads and actually supports the statement. Never add a URL from memory without checking it.
4. Run `python3 scripts/check_citations.py` after editing guideline files.
5. When adding a platform folder, update the indexes in `README.md` and `specific/README.md` and the detection table in `skills/architecture-review/SKILL.md`.
