---
name: architecture-review
description: Review a codebase, a pull request or a design document against the Architecture Guidelines (general rules plus platform-specific rules for game development, Unity, Godot, Unreal Engine, mobile games, web front ends, React, Next.js, Vue, Svelte, TypeScript, Node.js, Python, .NET, GraphQL, PostgreSQL, Redis, Kafka, RabbitMQ, Android, Flutter, Docker, Kubernetes, OpenTelemetry, AWS, serverless hosting (Vercel, Netlify, Cloudflare), Terraform, GitHub Actions and GitLab CI/CD). Produces a findings report where every finding cites the guideline it is based on and that guideline's source link. Use when asked for an architecture review, design review, structural assessment or "is this well architected?" check, or before a large refactoring.
argument-hint: "[path | PR/branch | design doc]"
---

# Architecture review

Review the target against this repository's guidelines. Each finding has to be traceable to a written rule and its source.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path (the skill isn't running as a plugin), the root is two directories above this `SKILL.md` file. You need:

- `<root>/general/README.md`: the index of general guidelines
- `<root>/specific/<platform>/`: the platform guidelines

## 1. Scope

Work out what to review from the request (`$ARGUMENTS` if given):

- **Whole repository or a directory**: map the structure first, then go deep where risk is highest.
- **Pull request or branch**: review the diff (`git diff <base>...HEAD`), and judge it against the existing architecture.
- **Design document**: review the proposal itself, and ask for the missing information you need.

If the scope is unclear and the repository is large, ask once. Otherwise state your assumption and continue.

## 2. Detect platforms

| Platform | Signals | Guidelines |
| --- | --- | --- |
| Game (any engine) | A Unity, Godot, Unreal or other game project, or a custom game loop | `specific/gamedev/`, plus the engine's folder below |
| Unity | `ProjectSettings/ProjectVersion.txt`, `Assets/` with `.meta` files | `specific/unity/` (all files). For deep game work in Unity, Godot or Unreal, use the `game-architecture` skill |
| Mobile game | A game that builds for iOS or Android: Android or iOS build settings in the engine project, an `AndroidManifest.xml` or Xcode project, or StoreKit or Play Billing code | `specific/mobile-games/`, plus `specific/gamedev/` and the engine's folder |
| Godot | `project.godot`, `.gd` and `.tscn` files | `specific/godot/` |
| Unreal Engine | A `.uproject` file, `*.Build.cs` and `*.Target.cs` files, `Config/DefaultEngine.ini` | `specific/unreal/` |
| Web front end | HTML, CSS or JavaScript served to browsers: `index.html`, a bundler config (`vite.config.*`, `webpack.config.*`), or a front-end framework | `specific/web/`, plus the framework's folder below |
| React | `package.json` with a `react` dependency | `specific/react/` |
| Next.js | `next.config.js`, `next.config.mjs` or `next.config.ts`, or a `next` dependency in `package.json` | `specific/nextjs/`, plus `specific/react/` |
| Vue | `*.vue` files, a `vue` dependency in `package.json`, or `nuxt.config.*` | `specific/vue/`, plus `specific/web/` |
| Svelte | `*.svelte` files, `svelte.config.js`, or an `@sveltejs/kit` dependency | `specific/svelte/`, plus `specific/web/` |
| TypeScript | `tsconfig.json`, or `*.ts` and `*.tsx` files | `specific/typescript/`, plus the platform's folder |
| Node.js | `package.json` for a server: dependencies such as `express`, `fastify`, `@nestjs/core` or `hono`, or a `start` script that runs `node` | `specific/nodejs/` |
| Python | `pyproject.toml`, `requirements*.txt`, `uv.lock`, `setup.py`, or Django's `manage.py` | `specific/python/` |
| .NET | `*.sln`, `*.slnx`, `*.csproj` (outside a Unity project) | `specific/dotnet/` |
| GraphQL | `*.graphql` or `*.gql` schema files, a `graphql` dependency, or a GraphQL server library (for example Apollo Server, GraphQL Yoga, Strawberry, Hot Chocolate) | `specific/graphql/` |
| PostgreSQL | SQL migrations for PostgreSQL, `postgres://` or `postgresql://` connection strings, a PostgreSQL driver (`pg`, `psycopg`, `asyncpg`, `Npgsql`), or a `postgres` service in a Compose file | `specific/postgres/` |
| Redis or Valkey | `redis://` or `rediss://` URLs, a Redis client dependency (for example `redis`, `ioredis`, `StackExchange.Redis`, `go-redis`), or a `redis` or `valkey` service in a Compose file | `specific/redis/` |
| Apache Kafka | A Kafka client dependency (for example `kafkajs`, `confluent-kafka`, `org.apache.kafka:kafka-clients`, `Confluent.Kafka`, `franz-go`), `bootstrap.servers` settings, or a `kafka` service in a Compose file | `specific/kafka/` |
| RabbitMQ | An AMQP client (for example `amqplib`, `pika`, `RabbitMQ.Client`, `amqp091-go`, Spring AMQP), `amqp://` or `amqps://` URLs, `rabbitmq.conf`, or a `rabbitmq` service in a Compose file | `specific/rabbitmq/` |
| Android | Gradle files that apply `com.android.application` or `com.android.library` | `specific/android/` |
| Flutter | `pubspec.yaml` that depends on the `flutter` SDK | `specific/flutter/` |
| Docker | `Dockerfile` or `Containerfile`, `compose.yaml` or `docker-compose.yml`, `.dockerignore` | `specific/docker/` |
| Kubernetes | YAML files with `apiVersion:` and `kind:`, `Chart.yaml`, `kustomization.yaml` | `specific/kubernetes/` |
| OpenTelemetry | OpenTelemetry SDK packages (`@opentelemetry/*`, `opentelemetry-*`, `OpenTelemetry.*`), `OTEL_*` environment variables, or a Collector configuration with `receivers`, `exporters` and `service.pipelines` | `specific/opentelemetry/` |
| AWS | `cdk.json`, CloudFormation/SAM templates with `AWS::` types, Terraform `provider "aws"` | `specific/aws/` |
| Serverless and edge hosting | `vercel.json`, `netlify.toml`, or `wrangler.toml`, `wrangler.json` or `wrangler.jsonc` | `specific/web-hosting/` |
| Terraform or OpenTofu | `*.tf` or `*.tofu` files, `.terraform.lock.hcl` | `specific/terraform/` |
| GitHub Actions | `.github/workflows/*.yml`, `action.yml` | `specific/github-actions/` |
| GitLab CI/CD | `.gitlab-ci.yml`, or CI/CD components in `templates/` | `specific/gitlab-ci/` |

A repository can match several platforms. Unity projects contain generated `.csproj` files, so don't apply the ASP.NET Core rules to them.

## 3. Load the relevant guidelines

Always read `general/principles.md` and `general/architecture-styles.md`. Add the other general files that match what you find:

| You find | Read |
| --- | --- |
| HTTP/gRPC endpoints, public SDKs, message schemas | `general/api-design.md` |
| Databases, migrations, events between services | `general/data.md` |
| Deployment config, retries/timeouts, monitoring | `general/operations-reliability.md` |
| Auth, secrets, user data, dependencies | `general/security.md`, and `general/authentication.md` for sign-in and sessions |
| Versioning, tags, release pipelines, changelogs | `general/releases.md` |
| Repository layout, monorepo tooling, CODEOWNERS, branch rules | `general/repositories.md` |
| Tests, CI pipelines | `general/testing-delivery.md` |
| LLM or ML calls, agents | `general/ai-systems.md` |
| Complex business logic | `general/domain-driven-design.md` |
| ADRs and architecture docs (or their absence) | `general/decisions.md`, `general/documentation.md` |
| Quality requirements, SLOs | `general/quality-attributes.md` |

Then read the platform folders. Where a platform file adopts an external checklist (for example the Android or Flutter recommendation pages), use that checklist. Fetch it if you have web access.

## 4. Gather evidence

Map before you judge:

- Top-level structure and the module/package/assembly boundaries (`.asmdef`, `ProjectReference`, Gradle modules, workspace packages, import paths).
- **Dependency direction**: which modules reference which. Look for cycles, and for domain code that depends on UI, framework or infrastructure code.
- Entry points, configuration and secret handling, external integrations.
- Tests: whether they exist, what kinds, and whether CI runs them.
- Architecture documentation: ADRs, diagrams, README.

In large repositories, sample representative files instead of reading everything. Record file paths and line numbers as you go.

## 5. Evaluate

- Report only findings that map to a rule in the loaded guideline files. Cite the rule by its ID (for example `DATA-1`), and give its score and title as written. `<root>/RULES.md` lists all IDs.
- Rules and sources are sorted by score (1–10, see `<root>/RANKING.md`). Check the highest-scored rules first, and read the highest-scored adopted references first.
- Copy source links **exactly** from the guideline file. Never invent a rule or a URL.
- Keep evidence (what the code does) separate from judgement (why it matters).
- Note what's done well, briefly. It tells the team what to keep.
- Put observations that no guideline covers in a separate section, marked as opinion.

Severity. Start from the rule's score, then adjust for the actual impact in this codebase:

- **High** (usually rules scored 9–10): likely to cause incidents, security exposure or data loss, or it blocks planned change.
- **Medium** (usually 6–8): raises the cost of change, or erodes a boundary.
- **Low** (usually 1–5): inconsistency or hygiene.

## 6. Report

Use this structure:

```markdown
## Architecture review: <scope>

**Platforms:** <detected> · **Guidelines applied:** <list of guideline files>

### Summary
<2–4 sentences: overall shape, top risks, strengths>

### Findings
| # | Severity | Finding | Evidence | Guideline | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | High | <what is wrong and why it matters> | `path/to/file.cs:42` | `DATA-1` (9): "Give each service or module exclusive ownership of its data" | [microservices.io, Database per service](https://microservices.io/patterns/data/database-per-service.html) |

### Recommendations
1. <Concrete next step, linked to finding numbers. For decisions with real trade-offs, suggest an ADR (see the `architecture-decision-record` skill).>
2. <Where the guideline file's "How to enforce" section names a tool that checks a violated rule, recommend adding it, so the finding can't come back unnoticed.>

### Not covered by the guidelines
- <Observation (opinion, no source)> → candidate for a new guideline
```

Don't change code during a review unless the user asks.
