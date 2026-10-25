---
status: accepted
date: 2026-10-24
decision-makers: depuschm
---

# Reference existing guidelines first, and back every written rule with a source

## Context and Problem Statement

We want one place for architecture best practices across general topics and specific platforms such as Unity. Much of this guidance already exists in official platform guides, standards and well-known books. How much should we write ourselves, and how do we keep what we write trustworthy?

## Decision Drivers

* Trust: readers and AI agents must be able to check every statement.
* Maintenance: a small team can't keep a large self-written handbook current.
* Usefulness: readers need a curated path, not a pile of links.

## Considered Options

* Write our own complete handbook
* Curate links only, like an awesome list
* Reference first: adopt existing guides, and write short rules only where needed, each with a source

## Decision Outcome

Chosen option: "Reference first", because it keeps the authoritative sources in charge of the details while still giving readers our curated choices and decisions.

### Consequences

* Good, because every rule links to a source that supports it, so statements can be verified.
* Good, because official guides keep themselves current; we only track whether our links still hold.
* Bad, because our content depends on external pages that move or change. Verified dates on every source, `scripts/verify_sources.py` and the `reverify-sources` skill address that.

### Confirmation

* `scripts/check_citations.py` fails CI if any list item in `general/` or `specific/` lacks a link.
* Link checks (lychee) and `scripts/verify_sources.py` catch broken and retired sources.
* Fact-check passes compared each rule against its source when the repository was created.

## Pros and Cons of the Options

### Write our own complete handbook

* Good, because it reads consistently.
* Bad, because it duplicates official guidance and goes stale.
* Bad, because statements can't be traced to a source.

### Curate links only

* Good, because it's cheap.
* Bad, because it doesn't record decisions, such as which style guide we adopt, or rules that combine sources.

## More Information

The rules for contributors are in [CONTRIBUTING.md](../../CONTRIBUTING.md).
