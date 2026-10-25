# Architecture styles

How to choose and combine structural styles such as monoliths, microservices, layered, hexagonal/clean and event-driven.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Azure Architecture Center: architecture styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/): each style with its benefits, challenges and when to use it. Use it as the default catalogue when comparing styles.
- `9` [Azure cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/): a pattern catalogue with problem, solution and when to use each pattern.
- `9` [Microservices](https://martinfowler.com/articles/microservices.html) (Lewis and Fowler): the defining article on microservice characteristics.
- `8` [Microservice Architecture pattern language](https://microservices.io/patterns/index.html) (Chris Richardson): patterns for decomposition, data, communication and deployment.
- `8` [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) (Hohpe and Woolf): the vocabulary for messaging and integration.

## Key rules

### Monolith or microservices

- `8` **Start with a well-structured monolith and split it once the boundaries are understood.** Most successful microservice systems started as monoliths that grew too big. ([Fowler, Monolith First](https://martinfowler.com/bliki/MonolithFirst.html))
- `8` **Have rapid provisioning, basic monitoring and rapid deployment in place before adopting microservices.** ([Fowler, Microservice Prerequisites](https://martinfowler.com/bliki/MicroservicePrerequisites.html))
- `8` **Organise services around business capabilities and let each service own its data.** ([Lewis and Fowler, Microservices](https://martinfowler.com/articles/microservices.html), [microservices.io, Database per service](https://microservices.io/patterns/data/database-per-service.html))
- `7` **Treat microservices as a premium you pay to manage complexity.** Don't pay it for systems that aren't complex enough to need it. ([Fowler, Microservice Premium](https://martinfowler.com/bliki/MicroservicePremium.html))
- `6` **Consider a modular monolith: one deployable with strictly enforced module boundaries.** ([Shopify Engineering, Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity), [Modular Monolith with DDD reference implementation](https://github.com/kgrzybek/modular-monolith-with-ddd))

### Inside an application

- `9` **Keep the domain independent of UI, frameworks and databases, so that dependencies point inwards.** Hexagonal, Onion and Clean Architecture all express this. ([Cockburn, Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture), [Palermo, Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/), [Martin, The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html))
- `7` **Layer presentation, domain and data, but in larger systems make domain modules the top-level split.** ([Fowler, Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html))

### Events and messaging

- `7` **Apply CQRS only to the specific parts of a system that need it.** For most systems it adds risky complexity. ([Fowler, CQRS](https://martinfowler.com/bliki/CQRS.html), [Azure, CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs))
- `7` **Use event sourcing where a full history of changes is a requirement, not as a default persistence model.** ([Fowler, Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), [Azure, Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing))
- `5` **Say which event-driven pattern you mean: event notification, event-carried state transfer, event sourcing or CQRS.** They have very different trade-offs. ([Fowler, What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html))

### Evolving existing systems

- `8` **Replace legacy systems incrementally behind a facade (Strangler Fig) rather than with a big-bang rewrite.** ([Fowler, Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html), [Azure, Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig))
- `6` **Put an anti-corruption layer between your model and legacy or external models.** ([Azure, Anti-corruption Layer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer))
- `5` **When extracting services, start with a simple, loosely coupled capability and decouple by business capability, not by technical layer.** ([Dehghani, How to break a Monolith into Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html))

## Tutorials and further reading

- `8` [Azure: microservices architecture style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices): a guided path through designing microservices.
- `7` [Building Microservices, 2nd edition](https://samnewman.io/books/building_microservices_2nd_edition/) (Sam Newman).
- `5` [Serverless Architectures](https://martinfowler.com/articles/serverless.html) (Mike Roberts): what serverless is, with its benefits and drawbacks.
