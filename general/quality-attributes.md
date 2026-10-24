# Quality attributes

Make the "-ilities" (performance, availability, security, maintainability, …) explicit, trade them off on purpose, and verify them continuously.

## Adopted references

- [arc42 Quality Model](https://quality.arc42.org/): quality attributes with definitions, example requirements and their relation to ISO/IEC 25010.
- [Azure Well-Architected pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars): reliability, security, cost optimisation, operational excellence and performance efficiency, with the trade-offs between them.
- [ATAM: Method for Architecture Evaluation](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/) (SEI): a structured method for evaluating an architecture against prioritised quality-attribute scenarios.
- [Building Evolutionary Architectures](https://evolutionaryarchitecture.com/) (Ford, Parsons, Kua, Sadalage): fitness functions and incremental change.

## Key rules

- **Write quality requirements as concrete, measurable scenarios, not adjectives.** "Fast" isn't a requirement. ([arc42 Quality Model](https://quality.arc42.org/), [SEI, ATAM](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/))
- **Pick the few (three to five) quality goals that drive the design and make the trade-offs between them explicit.** ([arc42, section 1: quality goals](https://docs.arc42.org/section-1/), [Azure Well-Architected pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars))
- **Protect key characteristics with automated architectural fitness functions that run in the delivery pipeline.** ([Thoughtworks Technology Radar, Architectural fitness function](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function), [Building Evolutionary Architectures](https://evolutionaryarchitecture.com/))
- **When the architecture is a key business asset, evaluate it with stakeholders against prioritised scenarios early, before committing.** ([SEI, ATAM: Method for Architecture Evaluation](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/))

## Tutorials and further reading

- [Fundamentals of Software Architecture](https://fundamentalsofsoftwarearchitecture.com/) (Richards and Ford): architecture characteristics and how to identify them.
