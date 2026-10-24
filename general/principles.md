# Principles

Design principles that apply regardless of technology, team size or architecture style.

## Adopted references

- [Software Architecture Guide](https://martinfowler.com/architecture/) (Martin Fowler): the entry point for what architecture is and why internal quality matters.
- [Architectural principles](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles) (Microsoft): a compact, technology-agnostic list. It covers separation of concerns, encapsulation, dependency inversion, explicit dependencies, single responsibility, DRY, persistence ignorance and bounded contexts.
- [The Principles of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod) (Robert C. Martin): the original SOLID and package-design principles.
- [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html) (Kent Beck via Martin Fowler): the four rules of simple design.

## Key rules

### Focus

- **Spend architecture effort on the decisions that are hard to change.** Architecture is "the important stuff, whatever that is". Usually that means the decisions people wish they could get right early, the ones they perceive as hard to change. ([Fowler, Software Architecture Guide](https://martinfowler.com/architecture/), [Who Needs an Architect?](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf))
- **Reduce irreversibility where you can.** Much of an architect's job is finding ways to make decisions reversible, so fewer of them become "architecture". ([Fowler, Who Needs an Architect?](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf))
- **Treat internal quality as a speed investment, not a cost.** Cruft slows feature delivery within weeks, so high internal quality makes software cheaper to change. ([Fowler, Is High Quality Software Worth the Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html), [Design Stamina Hypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html))

### Modularity

- **Separate concerns and encapsulate decisions behind interfaces.** Each module should hide its internals and expose a well-defined contract. ([Microsoft, Architectural principles](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles))
- **Decompose by design decisions likely to change, not by processing steps.** ([Parnas, On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623), [open copy](https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf))
- **Gather together the things that change for the same reasons; separate those that change for different reasons.** ([Martin, The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html))
- **Point dependencies at abstractions and make them explicit.** High-level policy should not depend on low-level details, and a class should declare what it needs, for example in its constructor. ([Microsoft, Architectural principles](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles), [Martin, Principles of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod))
- **Keep each piece of knowledge in one place (DRY).** ([Microsoft, Architectural principles](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles))

### Simplicity

- **Don't build capabilities for presumed future needs (YAGNI), but do keep the code easy to change.** YAGNI doesn't apply to refactoring and other work that makes the software easier to modify. ([Fowler, Yagni](https://martinfowler.com/bliki/Yagni.html))
- **Prefer the simplest design that passes the tests, reveals intention, has no duplication and has the fewest elements.** ([Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html))
- **Take on technical debt deliberately and prudently, and know when you're doing it.** ([Fowler, Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html))

### Socio-technical design

- **Expect system structure to mirror communication structure (Conway's law).** Design teams and architecture together. ([Fowler, Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html), [Conway, original paper](https://www.melconway.com/Home/Conways_Law.html))
- **Shape teams to get the architecture you want (Inverse Conway Maneuver).** ([Thoughtworks Technology Radar](https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver))
- **Draw team boundaries to manage cognitive load, using clear team types and interaction modes.** ([Team Topologies key concepts](https://teamtopologies.com/key-concepts), [Fowler, Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html))
- **Aim for an architecture where teams can test and deploy independently.** It is one of the capabilities that drive delivery performance. ([DORA, Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/))

## Tutorials and further reading

- [Is Design Dead?](https://martinfowler.com/articles/designDead.html) (Martin Fowler): how design works in evolutionary, agile development.
- [Sacrificial Architecture](https://martinfowler.com/bliki/SacrificialArchitecture.html) (Martin Fowler): when it's right to plan to throw code away.
- [Refactoring.Guru: design patterns](https://refactoring.guru/design-patterns): an illustrated tutorial on the classic design patterns.
