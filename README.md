# Architecture Guidelines

Best practices for designing software architectures, plus AI skills that apply them.

**Read it as a website:** [depuschm.github.io/architecture-guidelines](https://depuschm.github.io/architecture-guidelines/), with search, dark mode and a link to every rule.

The repo is **reference-first**. If a good guideline already exists (an official platform guide, a standard, a well-known book or tutorial), we link to it and adopt it. We only write our own short rules where nothing suitable exists, where sources disagree, or where a choice has to be made. Every rule we write links to a source.

Every source and every rule has a **score from 1 to 10**, and lists are sorted by it, so the most important entries come first. The score bands are:

| Score | Sources | Rules |
| --- | --- | --- |
| 9–10 | Start here | Strongly recommended |
| 6–8 | Recommended | Recommended |
| 1–5 | Further reading | Conditional |

[RANKING.md](RANKING.md) explains the criteria, and [SOURCES.md](SOURCES.md) lists every source in one place, ranked, with the date each was last verified.

Every rule also has a **stable ID**, such as `SEC-3` or `UNITY-STRUCT-2`, so reviews, ADRs and pull requests can cite it. [RULES.md](RULES.md) lists all rules by ID. Where a tool can check a rule automatically, the guideline file names it under **How to enforce**.

## Structure

```
general/            Technology-independent guidelines (principles, styles, DDD, APIs, data, security, …)
specific/<platform> One folder per platform or service (games, web, data, mobile, infrastructure, automation)
specific/_template  Starting point for a new platform folder
skills/             AI skills (Agent Skills format) that apply these guidelines
checklists/         One checklist per area, for pull requests and design reviews (generated)
docs/decisions/     Architecture decision records for this repository
RANKING.md          How sources and rules are scored from 1 to 10
SOURCES.md          Every linked source, ranked (generated from sources.csv)
RULES.md            Every rule by ID (generated)
sources.csv         Score and last-verified date of every source
rules.csv           Registry of rule IDs, including retired ones (never reused)
.claude-plugin/     Makes this repo installable as a Claude Code plugin and marketplace
scripts/            Repository checks (citations, scores, IDs, source freshness) and tooling
zensical.toml       Website configuration, built by scripts/build_site.py
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
| [Authentication & sessions](general/authentication.md) | Identity providers, OAuth 2.0 and OpenID Connect, sessions, passwords, MFA, passkeys, recovery |
| [Testing & delivery](general/testing-delivery.md) | Test strategy, architecture tests, contract tests, CD, DORA |
| [Versioning & releases](general/releases.md) | SemVer, immutable releases, release automation, changelogs, deprecation |
| [Repositories & monorepos](general/repositories.md) | Monorepo or polyrepo, module boundaries, code ownership, branch protection |
| [AI systems](general/ai-systems.md) | LLM and agent architectures, evals, LLM security |
| [Reading list](general/reading-list.md) | Books and complete tutorials |

## Specific guidelines

| Area | Platform | Main adopted guide |
| --- | --- | --- |
| Games | [Game development](specific/gamedev/README.md) | [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) and [Fast-Paced Multiplayer](https://www.gabrielgambetta.com/client-server-game-architecture.html) |
| Games | [Unity](specific/unity/README.md) | [Unity best practice guides and e-books](https://docs.unity3d.com/Manual/best-practice-guides.html) |
| Games | [Godot](specific/godot/README.md) | [Godot best practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html) |
| Games | [Unreal Engine](specific/unreal/README.md) | [Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) and [Epic C++ Coding Standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) |
| Web and back end | [Web front end](specific/web/README.md) | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) and [Core Web Vitals](https://web.dev/articles/top-cwv) |
| Web and back end | [React](specific/react/README.md) | [react.dev Learn](https://react.dev/learn) |
| Web and back end | [Next.js](specific/nextjs/README.md) | [Next.js Docs: App Router](https://nextjs.org/docs/app) |
| Web and back end | [Vue](specific/vue/README.md) | [Vue.js guide](https://vuejs.org/guide/introduction.html) and [Nuxt docs](https://nuxt.com/docs/4.x/getting-started/introduction) |
| Web and back end | [Svelte and SvelteKit](specific/svelte/README.md) | [Svelte docs](https://svelte.dev/docs/svelte/overview) and [SvelteKit docs](https://svelte.dev/docs/kit/introduction) |
| Web and back end | [Node.js](specific/nodejs/README.md) | [Don't Block the Event Loop](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop) and [Security Best Practices](https://nodejs.org/learn/getting-started/security-best-practices) |
| Web and back end | [Python](specific/python/README.md) | [Python Packaging User Guide](https://packaging.python.org/en/latest/) and [Django deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) |
| Web and back end | [.NET / ASP.NET Core](specific/dotnet/README.md) | [.NET Architecture Guides](https://learn.microsoft.com/en-us/dotnet/architecture/) |
| Data | [PostgreSQL](specific/postgres/README.md) | [PostgreSQL documentation](https://www.postgresql.org/docs/current/) and [Don't Do This](https://wiki.postgresql.org/wiki/Don%27t_Do_This) |
| Data | [Redis and caching](specific/redis/README.md) | [Manage Redis](https://redis.io/docs/latest/operate/oss_and_stack/management/) and [Azure caching guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching) |
| Mobile | [Android](specific/android/README.md) | [Guide to app architecture](https://developer.android.com/topic/architecture) |
| Mobile | [Flutter](specific/flutter/README.md) | [Flutter app architecture guide](https://docs.flutter.dev/app-architecture) |
| Infrastructure | [Docker](specific/docker/README.md) | [Docker building best practices](https://docs.docker.com/build/building/best-practices/) and [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) |
| Infrastructure | [Kubernetes](specific/kubernetes/README.md) | [Kubernetes configuration good practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/) |
| Infrastructure | [OpenTelemetry](specific/opentelemetry/README.md) | [OpenTelemetry documentation](https://opentelemetry.io/docs/) |
| Infrastructure | [AWS](specific/aws/README.md) | [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) |
| Infrastructure | [Serverless and edge hosting](specific/web-hosting/README.md) | [Vercel production checklist](https://vercel.com/docs/production-checklist) and [Cloudflare Workers best practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) |
| Infrastructure | [Terraform](specific/terraform/README.md) | [Terraform style guide](https://developer.hashicorp.com/terraform/language/style) |
| Automation | [GitHub Actions](specific/github-actions/README.md) | [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) |

To add a platform, copy [`specific/_template`](specific/_template/README.md) and follow [CONTRIBUTING.md](CONTRIBUTING.md).

## Checklists

Every rule of an area in one list, grouped by level and sorted by score, with the tools that can check each rule automatically. Paste one into a pull request, design review or project kickoff:

[General](checklists/general.md) · [Game development](checklists/gamedev.md) · [Unity](checklists/unity.md) · [Godot](checklists/godot.md) · [Unreal](checklists/unreal.md) · [Web](checklists/web.md) · [React](checklists/react.md) · [Next.js](checklists/nextjs.md) · [Vue](checklists/vue.md) · [Svelte](checklists/svelte.md) · [Node.js](checklists/nodejs.md) · [Python](checklists/python.md) · [.NET](checklists/dotnet.md) · [PostgreSQL](checklists/postgres.md) · [Redis](checklists/redis.md) · [Android](checklists/android.md) · [Flutter](checklists/flutter.md) · [Docker](checklists/docker.md) · [Kubernetes](checklists/kubernetes.md) · [OpenTelemetry](checklists/opentelemetry.md) · [AWS](checklists/aws.md) · [Hosting](checklists/web-hosting.md) · [Terraform](checklists/terraform.md) · [GitHub Actions](checklists/github-actions.md)

## AI skills

The [`skills/`](skills) folder uses the [Agent Skills](https://agentskills.io/specification) format (a folder with a `SKILL.md`), which Claude Code and other agent tools can load.

| Skill | Use it to |
| --- | --- |
| [`ask-guidelines`](skills/ask-guidelines/SKILL.md) | Answer "what do our guidelines say about X?" with the relevant rules by ID, score and source |
| [`architecture-review`](skills/architecture-review/SKILL.md) | Review a codebase, design or PR against these guidelines. Each finding cites the rule and its source |
| [`architecture-decision-record`](skills/architecture-decision-record/SKILL.md) | Write an ADR in [MADR](https://adr.github.io/madr/) format, or follow the project's existing ADR format |
| [`c4-diagram`](skills/c4-diagram/SKILL.md) | Produce [C4](https://c4model.com/) context/container/component diagrams as code |
| [`enforce-guidelines`](skills/enforce-guidelines/SKILL.md) | Set up the checks named under **How to enforce** in a project's CI, commit hooks or editor, each labelled with the rule IDs it enforces |
| [`unity-architecture`](skills/unity-architecture/SKILL.md) | Design or review the architecture of a Unity project |

The skills are tested with [evals](evals/README.md) that compare runs with and without the plugin. In the latest full run, every case passed 3 of 3 runs with the plugin. The plugin raised the score by +1.00 on ADRs, +0.75 on guideline questions and +0.50 on Unity reviews, mainly through rule IDs and source links that plain Claude doesn't produce. The newest cases (Next.js and Godot reviews, and setting up checks in CI) have each passed a single run so far.

Maintainers also get two project skills: [`add-guideline`](.claude/skills/add-guideline/SKILL.md) adds guidelines the reference-first way, and [`reverify-sources`](.claude/skills/reverify-sources/SKILL.md) re-checks stale or retired sources.

### Install in Claude Code

The repo is a [Claude Code plugin](https://code.claude.com/docs/en/plugins) and its own marketplace:

```bash
claude plugin marketplace add depuschm/architecture-guidelines
claude plugin install architecture-guidelines@architecture-guidelines
```

The skills then run as `/architecture-guidelines:architecture-review` and so on. Claude also loads them on its own when a request matches.

The plugin has no fixed version, so every commit to `main` is a new release. To receive updates automatically, open `/plugin`, go to **Marketplaces**, select `architecture-guidelines` and choose **Enable auto-update**. Otherwise, update by hand with `claude plugin update architecture-guidelines@architecture-guidelines`. To try the plugin from a local clone without installing it, run `claude --plugin-dir ./architecture-guidelines`.

### Use with other agents

Tools that read [`AGENTS.md`](AGENTS.md) or support Agent Skills can use the `skills/` folders directly. The skills find the guideline files relative to their own location (`../../general`, `../../specific`), so keep the repo layout intact.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. **Reference first.** Link to an existing guideline before writing a new one.
2. **Every rule has a source.** Each list item in `general/` and `specific/` must contain a link. CI enforces this with [`scripts/check_citations.py`](scripts/check_citations.py).
3. **Every entry has a score.** Score sources in `sources.csv` and rules inline, following [RANKING.md](RANKING.md). Then run `python3 scripts/rank.py fix`, which also gives new rules their ID, sorts the lists and updates SOURCES.md and RULES.md.
4. **Links must work and stay current.** CI runs [lychee](https://lychee.cli.rs/) and [`scripts/verify_sources.py`](scripts/verify_sources.py) on every push and once a week. The script also catches retired pages, and the job summary lists sources not verified in the last year.

### Automation

| What runs | When | Where |
| --- | --- | --- |
| Citation, score and rule ID checks, and plugin validation | Every push and pull request | [`checks.yml`](.github/workflows/checks.yml) |
| Workflow security audit with [zizmor](https://docs.zizmor.sh/), so this repository follows its own [GitHub Actions rules](specific/github-actions/README.md) | Every push and pull request | [`checks.yml`](.github/workflows/checks.yml) |
| Link check and retired-page detection | Every push and pull request, and weekly | [`checks.yml`](.github/workflows/checks.yml) |
| Sources not verified for a year fail the weekly run, and a failed weekly run opens (or updates) an issue | Weekly | [`checks.yml`](.github/workflows/checks.yml) |
| Website build in strict mode (broken links fail it), deployed to GitHub Pages | Pull requests build it, pushes to `main` deploy it | [`site.yml`](.github/workflows/site.yml) |
| Update pull requests for GitHub Actions and the site generator | Weekly | [`dependabot.yml`](.github/dependabot.yml) |
| Skill evals against real models | When started by hand (needs an `ANTHROPIC_API_KEY` secret) | [`evals.yml`](.github/workflows/evals.yml) |

Issue templates cover suggesting a source, disputing a score, reporting an outdated source and requesting a platform. The decisions behind how this repository works are recorded in [docs/decisions](docs/decisions/README.md).

## License

- **Guideline content and documentation** (`general/`, `specific/` and the Markdown files at the root) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Code and AI skills** (`scripts/`, `skills/`, `.claude/`, `.claude-plugin/`, `.github/` and config files) are licensed under the [MIT License](LICENSE-CODE).
- The MADR template in [`skills/architecture-decision-record/template.md`](skills/architecture-decision-record/template.md) keeps its original license, MIT OR CC0-1.0.
- Linked third-party sources keep their own licenses. This repository links to them and summarises them. It doesn't copy them.
