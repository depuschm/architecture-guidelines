<!-- rule-prefix: QA -->
# Quality attributes

Make the "-ilities" (performance, availability, security, maintainability, …) explicit, trade them off on purpose, and verify them continuously.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [arc42 Quality Model](https://quality.arc42.org/): quality attributes with definitions, example requirements and their relation to ISO/IEC 25010.
- `8` [Azure Well-Architected pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars): reliability, security, cost optimisation, operational excellence and performance efficiency, with the trade-offs between them.
- `7` [ATAM: Method for Architecture Evaluation](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/) (SEI): a structured method for evaluating an architecture against prioritised quality-attribute scenarios.
- `7` [Building Evolutionary Architectures](https://evolutionaryarchitecture.com/) (Ford, Parsons, Kua, Sadalage): fitness functions and incremental change.

## Key rules

- `8` `QA-1` **Write quality requirements as concrete, measurable scenarios, not adjectives.** "Fast" isn't a requirement. ([arc42 Quality Model](https://quality.arc42.org/), [SEI, ATAM: Method for Architecture Evaluation](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/))
- `8` `QA-2` **Pick the few (three to five) quality goals that drive the design and make the trade-offs between them explicit.** ([arc42, section 1: quality goals](https://docs.arc42.org/section-1/), [Azure Well-Architected pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars))
- `6` `QA-3` **Protect key characteristics with automated architectural fitness functions that run in the delivery pipeline.** ([Thoughtworks Technology Radar, Architectural fitness function](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function), [Building Evolutionary Architectures](https://evolutionaryarchitecture.com/))
- `4` `QA-4` **When the architecture is a key business asset, evaluate it with stakeholders against prioritised scenarios early, before committing.** ([SEI, ATAM: Method for Architecture Evaluation](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/))

## Tutorials and further reading

- `7` [Fundamentals of Software Architecture](https://fundamentalsofsoftwarearchitecture.com/) (Richards and Ford): architecture characteristics and how to identify them.
