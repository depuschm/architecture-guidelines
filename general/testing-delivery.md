<!-- rule-prefix: TEST -->
# Testing and delivery

Test strategies that support the architecture, and delivery practices that keep it changeable.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) (Ham Vocke): **our default test strategy**, with worked examples.
- `9` [DORA](https://dora.dev/): research-backed capabilities and metrics for software delivery performance.
- `8` [Software Engineering at Google](https://abseil.io/resources/swe-book) (free online): testing, code review and large-scale change.
- `7` [Testing Strategies in a Microservice Architecture](https://martinfowler.com/articles/microservice-testing/) (Toby Clemson): test types for distributed systems.
- `7` [Trunk Based Development](https://trunkbaseddevelopment.com/): the branching model that supports continuous integration.

## Key rules

- `8` `TEST-1` **Write many fast unit tests, fewer integration tests and very few end-to-end tests.** ([Vocke, The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), [Google Testing Blog, Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html))
- `8` `TEST-2` **Keep the software deployable at all times, and prioritise that over new features.** ([Fowler, Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html))
- `7` `TEST-3` **Integrate small changes into the main branch at least daily.** ([Trunk Based Development](https://trunkbaseddevelopment.com/))
- `6` `TEST-4` **Enforce architecture rules such as layering and dependency direction with automated tests.** ([ArchUnit](https://www.archunit.org/) for Java, [ArchUnitNET](https://github.com/TNG/ArchUnitNET) for .NET)
- `6` `TEST-5` **Test service boundaries with contract tests rather than relying on slow, brittle end-to-end integration suites.** ([Pact, Introduction](https://docs.pact.io/), [Fowler, Contract Test](https://martinfowler.com/bliki/ContractTest.html))
- `6` `TEST-6` **Decouple deployment from release with feature toggles, and remove toggles once they've served their purpose.** ([Hodgson, Feature Toggles](https://martinfowler.com/articles/feature-toggles.html))
- `6` `TEST-7` **Measure software delivery throughput and instability with the DORA metrics, and use them to improve, not to compare teams.** ([DORA metrics guide](https://dora.dev/guides/dora-metrics/))

## Tutorials and further reading

- `7` [Software Engineering at Google, table of contents](https://abseil.io/resources/swe-book/html/toc.html).
- `6` [Test Double](https://martinfowler.com/bliki/TestDouble.html) (Martin Fowler): the vocabulary of mocks, stubs and fakes.
