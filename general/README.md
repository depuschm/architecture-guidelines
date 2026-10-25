# General guidelines

Technology-independent guidance. Platform-specific guidance in [`../specific`](../specific/README.md) builds on these files.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Start here

If you only read three external sources, read these:

- `10` [The C4 model](https://c4model.com/): a shared way to describe and diagram any architecture.
- `9` [Software Architecture Guide](https://martinfowler.com/architecture/) (Martin Fowler): what architecture is, why it matters, and a curated index of articles.
- `9` [Azure Architecture Center: architecture styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/) and [cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/): a vendor-neutral-enough catalogue of styles and patterns, each with "when to use" guidance.

## Topics

- [Principles](principles.md): modularity, SOLID, simple design, technical debt, socio-technical design.
- [Architecture styles](architecture-styles.md): monolith first, microservices, hexagonal/clean, event-driven, CQRS, migration.
- [Domain-driven design](domain-driven-design.md): strategic and tactical DDD.
- [Decisions](decisions.md): architecture decision records and decision-making.
- [Documentation](documentation.md): C4, arc42, docs-as-code.
- [Quality attributes](quality-attributes.md): quality models, trade-offs, fitness functions.
- [API design](api-design.md): style guides, contracts, compatibility.
- [Data](data.md): ownership, consistency, distributed transactions, schema evolution.
- [Operations and reliability](operations-reliability.md): cloud frameworks, SRE, resilience, observability.
- [Security](security.md): threat modelling, secure design, supply chain.
- [Testing and delivery](testing-delivery.md): test strategy, architecture tests, continuous delivery.
- [AI systems](ai-systems.md): LLM and agent-based systems.
- [Reading list](reading-list.md): books and complete tutorials.
