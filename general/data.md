# Data

Decide who owns data, how consistent it must be, and how it changes over time.

## Adopted references

- [Designing Data-Intensive Applications](https://dataintensive.net/) (Martin Kleppmann): the reference book on storage, replication, partitioning, transactions and stream processing.
- [microservices.io data management patterns](https://microservices.io/patterns/data/database-per-service.html) (Chris Richardson): database per service, saga, outbox, CQRS and API composition.
- [Consistency models](https://jepsen.io/consistency) (Jepsen): precise definitions of what each consistency level guarantees.

## Key rules

- **Give each service or module exclusive ownership of its data.** Other parts of the system go through its API, not its tables. ([microservices.io, Database per service](https://microservices.io/patterns/data/database-per-service.html))
- **Keep data consistent across services with sagas, not distributed transactions.** ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html), [Azure, Saga pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga))
- **Publish events atomically with state changes using a transactional outbox.** ([microservices.io, Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html))
- **Choose the consistency level per use case and make eventual consistency visible in the design.** ([Vogels, Eventually Consistent](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html), [Jepsen, Consistency models](https://jepsen.io/consistency))
- **Evolve database schemas through small, versioned migrations kept in source control.** ([Sadalage/Fowler, Evolutionary Database Design](https://martinfowler.com/articles/evodb.html))
- **Choose storage technology per need, but count the operational cost of every extra datastore.** ([Fowler, Polyglot Persistence](https://martinfowler.com/bliki/PolyglotPersistence.html))
- **At organisational scale, treat analytical data as a product owned by domain teams (data mesh).** ([Dehghani, Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html))

## Tutorials and further reading

- [Designing Data-Intensive Applications](https://dataintensive.net/): the book's site, with resources.
