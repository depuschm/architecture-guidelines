# Decisions

Record architecture decisions so the reasoning survives after the people who made them have moved on.

## Adopted references

- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/): **our default ADR template.** The [`architecture-decision-record`](../skills/architecture-decision-record/SKILL.md) skill uses it.
- [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Michael Nygard): the original lightweight ADR format.
- [adr.github.io](https://adr.github.io/): an overview of ADR formats and tooling.
- [ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) and [best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/best-practices.html) (AWS Prescriptive Guidance): how teams propose, review and adopt ADRs.
- [Architecture decision record](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record) (Azure Well-Architected): what to record and when.
- [Architecture decision records overview](https://docs.cloud.google.com/architecture/architecture-decision-records) (Google Cloud).
- [Architecture decision record examples and templates](https://github.com/joelparkerhenderson/architecture-decision-record) (Joel Parker Henderson): many alternative templates and examples.

## Key rules

- **Write an ADR for every architecturally significant decision.** It records context, decision, status and consequences, and it fits on a page or two. ([Nygard, Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions))
- **Keep ADRs in the repository next to the code as numbered Markdown files, for example `docs/decisions/0001-use-postgresql.md`.** ([MADR](https://adr.github.io/madr/))
- **Record the options you considered and why you rejected them, not just the option you chose.** ([MADR template](https://adr.github.io/madr/))
- **Say how compliance will be confirmed, for example with a design or code review, an architecture test such as ArchUnit, or a fitness function.** ([MADR template, "Confirmation" section](https://adr.github.io/madr/), [Thoughtworks, Architectural fitness function](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function))
- **Don't rewrite accepted decisions. Supersede them with a new ADR and link the two.** ([Nygard, Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), [AWS, ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html))
- **Decentralise decisions with an advice process.** Anyone can decide after asking the people affected and those with expertise, and ADRs record the outcome. ([Harmel-Law, Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html))

## Tutorials and further reading

- [Lightweight Architecture Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) (Thoughtworks Technology Radar).
- [adr-tools](https://github.com/npryce/adr-tools): command-line tooling for Nygard-style ADRs.
