# Documentation

Describe architectures so that different audiences can understand them, and keep the descriptions current.

## Adopted references

- [The C4 model](https://c4model.com/) (Simon Brown): **our default for architecture diagrams.** It has four levels: system context, container, component and code. The [`c4-diagram`](../skills/c4-diagram/SKILL.md) skill uses it.
- [arc42](https://arc42.org/overview) ([documentation](https://docs.arc42.org/home/)): **our default structure for architecture documentation.** Use its sections as a checklist.
- [Diátaxis](https://diataxis.fr/): how to split documentation into tutorials, how-to guides, reference and explanation.
- [Docs as Code](https://www.writethedocs.org/guide/docs-as-code/) (Write the Docs): treat documentation with the same tools and workflow as code.

## Key rules

- **Start with a system context diagram and a container diagram.** Add component diagrams only where they add value. ([C4 model, diagrams](https://c4model.com/diagrams))
- **Give every diagram a title, a key or legend, and labelled, directed relationships.** ([C4 model, notation](https://c4model.com/diagrams/notation))
- **Use the C4 abstractions (person, software system, container, component) consistently, whatever the notation.** ([C4 model, abstractions](https://c4model.com/abstractions))
- **Keep diagrams as text in the repository so they can be reviewed and diffed.** Use, for example, Structurizr DSL or Mermaid, which GitHub renders. Mermaid's C4 syntax is still experimental. ([Write the Docs, Docs as Code](https://www.writethedocs.org/guide/docs-as-code/), [Structurizr](https://structurizr.com/), [Mermaid C4 diagrams](https://mermaid.js.org/syntax/c4.html), [GitHub, creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams))
- **Store, version and review documentation alongside the code.** ([Write the Docs, Docs as Code](https://www.writethedocs.org/guide/docs-as-code/), [docs-as-co.de](https://docs-as-co.de/))
- **Don't mix tutorials, how-to guides, reference and explanation in one document.** ([Diátaxis, The map](https://diataxis.fr/map/))

## Tutorials and further reading

- [arc42 documentation and examples](https://docs.arc42.org/home/).
- [The C4 model](https://c4model.com/): the site includes FAQs, examples and tooling lists.
