---
status: accepted
date: 2026-10-25
decision-makers: depuschm
---

# Score every source and rule from 1 to 10, grouped into three named levels

## Context and Problem Statement

The collection has hundreds of sources and around 200 rules. Readers need to know what to read first and which rules matter most, and reviews need a sense of severity. How should entries be ranked?

## Decision Drivers

* Readers should see the most important entries first.
* Ranking should be consistent across contributors.
* Reviews need a severity signal.

## Considered Options

* No ranking, ordered by topic only
* Named levels only, like Android's and Flutter's "strongly recommended / recommended / optional"
* Numeric scores from 1 to 10 only
* Scores from 1 to 10, grouped into named levels

## Decision Outcome

Chosen option: "Scores from 1 to 10, grouped into named levels", because scores give a fine-grained sort order, and the levels (9–10, 6–8, 1–5) give readers the familiar meaning used by [Android](https://developer.android.com/topic/architecture/recommendations) and [Flutter](https://docs.flutter.dev/app-architecture/recommendations).

### Consequences

* Good, because every list puts the most important entries first, and [SOURCES.md](../../SOURCES.md) ranks all sources in one place.
* Good, because the review skills can use rule scores as a severity hint.
* Bad, because scores are judgements and can drift between contributors. [RANKING.md](../../RANKING.md) defines the criteria, and a blind second-opinion pass was used to calibrate them.

### Confirmation

`scripts/rank.py check` fails CI if any entry is unscored or any list is unsorted.

## More Information

The criteria and levels are in [RANKING.md](../../RANKING.md).
