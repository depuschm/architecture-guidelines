---
status: accepted
date: 2026-10-25
decision-makers: depuschm
---

# Give every rule a stable ID that is never reused

## Context and Problem Statement

Reviews, ADRs and pull requests need to cite rules. Lists are sorted by score ([ADR-0002](0002-score-sources-and-rules.md)), so a rule's position changes whenever scores change. How do we cite a rule reliably?

## Decision Drivers

* A citation must keep pointing at the same rule after rewording, re-scoring and re-sorting.
* IDs should show where a rule lives.
* Adding a rule should need no manual bookkeeping.

## Considered Options

* Cite by file and position or line number
* Cite by rule title
* Per-file prefix plus a number, such as `SEC-3`, assigned by a script and recorded in a registry

## Decision Outcome

Chosen option: "Per-file prefix plus a number", because it's short and stable, and it shows the topic at a glance. Each file declares its prefix in a `<!-- rule-prefix: … -->` comment. `scripts/rank.py fix` assigns the next free number. [rules.csv](../../rules.csv) records every ID, including retired ones, so an ID is never reused.

### Consequences

* Good, because reviews and ADRs can cite rules that stay valid, and [RULES.md](../../RULES.md) lists them all.
* Good, because "How to enforce" entries can name the IDs they check, and the script validates them.
* Bad, because moving a rule to another file means retiring its ID and creating a new one.

### Confirmation

`scripts/rank.py check` fails CI on missing, duplicate, wrong-prefix or reused IDs.
