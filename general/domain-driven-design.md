# Domain-driven design

Model complex business domains and find good boundaries for modules, services and teams.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [DDD Reference](https://www.domainlanguage.com/ddd/reference/) (Eric Evans): the authoritative summary of DDD patterns and definitions.
- `8` [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process) (DDD Crew): a step-by-step path from business goals to bounded contexts and code.
- `7` [Context Mapping](https://github.com/ddd-crew/context-mapping) and [Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas) (DDD Crew): templates for designing and documenting contexts and their relationships.
- `7` [Using domain analysis to model microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) (Microsoft): DDD applied to service boundaries, with a worked example.
- `7` [EventStorming](https://www.eventstorming.com/) (Alberto Brandolini): a workshop format for exploring a domain together.

## Key rules

- `8` **Build a ubiquitous language with domain experts and use it everywhere: in conversations, documents and code.** ([Fowler, Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html))
- `8` **Split large domains into bounded contexts, each with its own model, and make the relationships between them explicit.** ([Fowler, Bounded Context](https://martinfowler.com/bliki/BoundedContext.html), [DDD Crew, Context Mapping](https://github.com/ddd-crew/context-mapping))
- `7` **Spend modelling effort on the core domain; buy or simplify generic subdomains.** ([Evans, DDD Reference](https://www.domainlanguage.com/ddd/reference/))
- `7` **Use aggregates as consistency boundaries.** Keep them small, reference other aggregates by identity, and use eventual consistency between them. ([Vernon, Effective Aggregate Design](https://www.dddcommunity.org/library/vernon_2011/), [Fowler, DDD Aggregate](https://martinfowler.com/bliki/DDD_Aggregate.html))
- `6` **Put behaviour next to the data it changes and avoid anemic domain models.** ([Fowler, Anemic Domain Model](https://martinfowler.com/bliki/AnemicDomainModel.html))
- `6` **Model concepts that are defined by their attributes as immutable value objects.** ([Fowler, Value Object](https://martinfowler.com/bliki/ValueObject.html))

## Tutorials and further reading

- `7` [Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html) (Martin Fowler): an overview with links to the key concepts.
- `5` [Domain-Driven Design Quickly](https://www.infoq.com/minibooks/domain-driven-design-quickly/) (InfoQ, free e-book): a short introduction to Evans' book.
- `5` [Welcome to DDD](https://github.com/ddd-crew/welcome-to-ddd) (DDD Crew): definitions of DDD's key concepts and pointers for getting started.
