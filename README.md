# Architecture Guidelines

Best practices for designing software architectures, plus AI skills that apply them.

The repo is **reference-first**. If a good guideline already exists (an official platform guide, a standard, a well-known book or tutorial), we link to it and adopt it. We only write our own short rules where nothing suitable exists, where sources disagree, or where a choice has to be made. Every rule we write links to a source.

Every source and every rule has a **score from 1 to 10**, and lists are sorted by it, so the most important entries come first. The score bands are:

| Score | Sources | Rules |
| --- | --- | --- |
| 9–10 | Start here | Strongly recommended |
| 6–8 | Recommended | Recommended |
| 1–5 | Further reading | Conditional |

[RANKING.md](RANKING.md) explains the criteria, and [SOURCES.md](SOURCES.md) lists all ~400 sources in one place, ranked.

## Structure

```
general/            Technology-independent guidelines (principles, styles, DDD, APIs, data, security, …)
specific/<platform> One folder per platform/service (Unity, .NET, Android, Flutter, React, Kubernetes, AWS)
specific/_template  Starting point for a new platform folder
skills/             AI skills (Agent Skills format) that apply these guidelines
RANKING.md          How sources and rules are scored from 1 to 10
SOURCES.md          Every linked source, ranked (generated from sources.csv)
sources.csv         The score of every source
.claude-plugin/     Makes this repo installable as a Claude Code plugin and marketplace
scripts/            Repository checks (citations, scores) and tooling
```

## General guidelines

| Topic | What it covers |
| --- | --- |
| [Principles](general/principles.md) | Modularity, SOLID, simple design, technical debt, Conway's law |
| [Architecture styles](general/architecture-styles.md) | Monolith vs. microservices, hexagonal/clean, event-driven, CQRS, migration |
| [Domain-driven design](general/domain-driven-design.md) | Ubiquitous language, bounded contexts, aggregates, context maps |
| [Decisions (ADRs)](general/decisions.md) | Recording and governing architecture decisions |
| [Documentation](general/documentation.md) | C4 model, arc42, docs-as-code, diagrams as code |
| [Quality attributes](general/quality-attributes.md) | Quality models, trade-offs, fitness functions, evaluation |
| [API design](general/api-design.md) | Style guides, contracts, errors, idempotency, compatibility |
| [Data](general/data.md) | Data ownership, consistency, sagas, outbox, schema evolution |
| [Operations & reliability](general/operations-reliability.md) | Twelve-factor, Well-Architected, SLOs, resilience, observability |
| [Security](general/security.md) | Threat modelling, least privilege, secrets, supply chain |
| [Testing & delivery](general/testing-delivery.md) | Test strategy, architecture tests, contract tests, CD, DORA |
| [AI systems](general/ai-systems.md) | LLM and agent architectures, evals, LLM security |
| [Reading list](general/reading-list.md) | Books and complete tutorials |

## Specific guidelines

| Platform | Main adopted guide |
| --- | --- |
| [Unity](specific/unity/README.md) | [Unity best practice guides and e-books](https://docs.unity3d.com/Manual/best-practice-guides.html) |
| [.NET / ASP.NET Core](specific/dotnet/README.md) | [.NET Architecture Guides](https://learn.microsoft.com/en-us/dotnet/architecture/) |
| [Android](specific/android/README.md) | [Guide to app architecture](https://developer.android.com/topic/architecture) |
| [Flutter](specific/flutter/README.md) | [Flutter app architecture guide](https://docs.flutter.dev/app-architecture) |
| [React](specific/react/README.md) | [react.dev Learn](https://react.dev/learn) |
| [Kubernetes](specific/kubernetes/README.md) | [Kubernetes configuration good practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/) |
| [AWS](specific/aws/README.md) | [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) |

To add a platform, copy [`specific/_template`](specific/_template/README.md) and follow [CONTRIBUTING.md](CONTRIBUTING.md).

## AI skills

The [`skills/`](skills) folder uses the [Agent Skills](https://agentskills.io/specification) format (a folder with a `SKILL.md`), which Claude Code and other agent tools can load.

| Skill | Use it to |
| --- | --- |
| [`architecture-review`](skills/architecture-review/SKILL.md) | Review a codebase, design or PR against these guidelines. Each finding cites the rule and its source |
| [`architecture-decision-record`](skills/architecture-decision-record/SKILL.md) | Write an ADR in [MADR](https://adr.github.io/madr/) format, or follow the project's existing ADR format |
| [`c4-diagram`](skills/c4-diagram/SKILL.md) | Produce [C4](https://c4model.com/) context/container/component diagrams as code |
| [`unity-architecture`](skills/unity-architecture/SKILL.md) | Design or review the architecture of a Unity project |

Maintainers also get a project skill, [`add-guideline`](.claude/skills/add-guideline/SKILL.md), which walks through adding guidelines the reference-first way.

### Install in Claude Code

The repo is a [Claude Code plugin](https://code.claude.com/docs/en/plugins) and its own marketplace:

```bash
claude plugin marketplace add depuschm/architecture-guidelines
claude plugin install architecture-guidelines@architecture-guidelines
```

The skills then run as `/architecture-guidelines:architecture-review` and so on. Claude also loads them on its own when a request matches. To try the plugin from a local clone without installing it, run `claude --plugin-dir ./architecture-guidelines`.

### Use with other agents

Tools that read [`AGENTS.md`](AGENTS.md) or support Agent Skills can use the `skills/` folders directly. The skills find the guideline files relative to their own location (`../../general`, `../../specific`), so keep the repo layout intact.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. **Reference first.** Link to an existing guideline before writing a new one.
2. **Every rule has a source.** Each list item in `general/` and `specific/` must contain a link. CI enforces this with [`scripts/check_citations.py`](scripts/check_citations.py).
3. **Every entry has a score.** Score sources in `sources.csv` and rules inline, following [RANKING.md](RANKING.md). Then run `python3 scripts/rank.py fix` to sort the lists and update SOURCES.md.
4. **Links must work.** CI runs [lychee](https://lychee.cli.rs/) on every push and once a week.

## License

- **Guideline content and documentation** (`general/`, `specific/` and the Markdown files at the root) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Code and AI skills** (`scripts/`, `skills/`, `.claude/`, `.claude-plugin/`, `.github/` and config files) are licensed under the [MIT License](LICENSE-CODE).
- The MADR template in [`skills/architecture-decision-record/template.md`](skills/architecture-decision-record/template.md) keeps its original license, MIT OR CC0-1.0.
- Linked third-party sources keep their own licenses. This repository links to them and summarises them. It doesn't copy them.
