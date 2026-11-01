---
name: architecture-review
description: Review a codebase, a pull request or a design document against the Architecture Guidelines, applying the general rules plus the rules for every platform it detects, from game engines, game services and graphics to web front ends, back ends, databases, mobile and desktop apps, cloud and CI. Produces a findings report where every finding cites the guideline it is based on and that guideline's source link. Use when asked for an architecture review, design review, structural assessment or "is this well architected?" check, or before a large refactoring.
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
| Game (any engine) | A Unity, Godot, Unreal, GameMaker or other game project, or a custom game loop | `specific/gamedev/`, plus the engine's folder below |
| Unity | `ProjectSettings/ProjectVersion.txt`, `Assets/` with `.meta` files | `specific/unity/` (all files). For deep game work in Unity, Godot, Unreal or GameMaker, use the `game-architecture` skill |
| Mobile game | A game that builds for iOS or Android: Android or iOS build settings in the engine project, an `AndroidManifest.xml` or Xcode project, or StoreKit or Play Billing code | `specific/mobile-games/`, plus `specific/gamedev/` and the engine's folder |
| Steam or PC game | `steam_appid.txt`, `steam_api64.dll` or `libsteam_api.so`, SteamPipe `app_build_*.vdf` scripts, `steamcmd` or `butler push` in CI, or a Steamworks binding (Steamworks.NET, Facepunch.Steamworks, GodotSteam, `OnlineSubsystemSteam` in `DefaultEngine.ini`) | `specific/steam/`, plus `specific/gamedev/` and the engine's folder |
| Game servers | Agones manifests (`apiVersion: agones.dev/v1` with `kind: GameServer`, `Fleet`, `FleetAutoscaler` or `GameServerAllocation`) or an Agones SDK; the GameLift server SDK (`Aws::GameLift::Server`, `GameLiftServerAPI`), `AWS::GameLift::*` or `aws_gamelift_*` resources; Nakama runtime code (`InitModule`, `@heroiclabs/nakama-runtime`) or a `heroiclabs/nakama` image; an Unreal `*Server.Target.cs`, `com.unity.dedicated-server` in `Packages/manifest.json`, or `dedicated_server=true` in Godot's `export_presets.cfg` | `specific/game-servers/`, plus `specific/gamedev/`, the engine's folder, and `specific/kubernetes/` for Agones |
| Web game | A game that runs in a browser: a `phaser`, `three`, `pixi.js` or `@babylonjs/core` dependency with a game loop; a Unity Web build (`Build/*.loader.js`, `*.framework.js`, `*.wasm`, `*.data`); a Godot export preset with `platform="Web"` in `export_presets.cfg`; GameMaker HTML5 or GX.games builds; or a Poki or CrazyGames SDK | `specific/web-games/`, plus `specific/gamedev/`, `specific/graphics/`, `specific/web/` and the engine's folder |
| Graphics and shaders | Shader files (`*.shader`, `*.shadergraph`, `*.hlsl`, `*.glsl`, `*.vert`, `*.frag`, `*.wgsl`, `*.metal`, `*.gdshader`, `*.usf`), or code that calls a GPU API directly: Vulkan, Direct3D 12, Metal, WebGL or WebGPU, or a web 3D library such as three.js or Babylon.js | `specific/graphics/`, plus the engine's folder |
| Godot | `project.godot`, `.gd` and `.tscn` files | `specific/godot/` (all files) |
| Unreal Engine | A `.uproject` file, `*.Build.cs` and `*.Target.cs` files, `Config/DefaultEngine.ini` | `specific/unreal/` (all files) |
| GameMaker | A `.yyp` project file, `objects/*/*.yy` files and GML event files such as `Create_0.gml` | `specific/gamemaker/` (all files) |
| Web front end | HTML, CSS or JavaScript served to browsers: `index.html`, a bundler config (`vite.config.*`, `webpack.config.*`), or a front-end framework | `specific/web/`, plus the framework's folder below |
| React | `package.json` with a `react` dependency | `specific/react/` |
| Next.js | `next.config.js`, `next.config.mjs` or `next.config.ts`, or a `next` dependency in `package.json` | `specific/nextjs/`, plus `specific/react/` |
| Vue | `*.vue` files, a `vue` dependency in `package.json`, or `nuxt.config.*` | `specific/vue/`, plus `specific/web/` |
| Svelte | `*.svelte` files, `svelte.config.js`, or an `@sveltejs/kit` dependency | `specific/svelte/`, plus `specific/web/` |
| Angular | `angular.json`, or an `@angular/core` dependency in `package.json`; an `@angular/ssr` dependency means server-side rendering | `specific/angular/`, plus `specific/web/` and `specific/typescript/`, and `specific/nodejs/` with `@angular/ssr` |
| Astro | `astro.config.mjs`, `.ts` or `.js`, an `astro` dependency in `package.json`, or `.astro` files in `src/pages/` | `specific/astro/`, plus `specific/web/`, the folder of any UI framework used in islands, and `specific/web-hosting/` when an adapter targets Vercel, Netlify or Cloudflare |
| TypeScript | `tsconfig.json`, or `*.ts` and `*.tsx` files | `specific/typescript/`, plus the platform's folder |
| Node.js | `package.json` for a server: dependencies such as `express`, `fastify`, `@nestjs/core` or `hono`, or a `start` script that runs `node` | `specific/nodejs/` |
| Python | `pyproject.toml`, `requirements*.txt`, `uv.lock`, `setup.py`, or Django's `manage.py` | `specific/python/` |
| Go | `go.mod` (with `go.sum`) or `go.work`, `*.go` files, or `cmd/<name>/main.go` | `specific/go/`, plus `specific/game-servers/` when `go.mod` requires `agones.dev/agones` or `github.com/heroiclabs/nakama-common`, and `specific/postgres/` with `github.com/jackc/pgx` |
| .NET | `*.sln`, `*.slnx`, `*.csproj` (outside a Unity project) | `specific/dotnet/` |
| GraphQL | `*.graphql` or `*.gql` schema files, a `graphql` dependency, or a GraphQL server library (for example Apollo Server, GraphQL Yoga, Strawberry, Hot Chocolate) | `specific/graphql/` |
| PostgreSQL | SQL migrations for PostgreSQL, `postgres://` or `postgresql://` connection strings, a PostgreSQL driver (`pg`, `psycopg`, `asyncpg`, `Npgsql`), or a `postgres` service in a Compose file | `specific/postgres/` |
| MongoDB | `mongodb://` or `mongodb+srv://` connection strings; a MongoDB driver or ODM dependency (for example `mongodb`, `mongoose`, `pymongo`, `motor`, `MongoDB.Driver`, `go.mongodb.org/mongo-driver`, `spring-boot-starter-data-mongodb`); a `mongo` service in a Compose file; or `mongodbatlas_*` Terraform resources | `specific/mongodb/` |
| SQLite | `.db`, `.sqlite` or `.sqlite3` files, or `sqlite:` URLs; SQLite dependencies or imports (for example Python `sqlite3`, `better-sqlite3`, `sqflite`, `androidx.room`, `Microsoft.Data.Sqlite`, `rusqlite`, `GRDB`, `SQLite.swift`, `mattn/go-sqlite3`, `modernc.org/sqlite`) | `specific/sqlite/`, plus `specific/android/` with Room, `specific/flutter/` with `sqflite`, and `specific/gamedev/` when a game uses it for saves |
| Redis or Valkey | `redis://` or `rediss://` URLs, a Redis client dependency (for example `redis`, `ioredis`, `StackExchange.Redis`, `go-redis`), or a `redis` or `valkey` service in a Compose file | `specific/redis/` |
| Firebase | `firebase.json`, `.firebaserc`, `firestore.rules`, `storage.rules`, `database.rules.json` or `firestore.indexes.json`; `google-services.json` or `GoogleService-Info.plist`; or `firebase`, `firebase-admin` or `firebase-functions` dependencies | `specific/firebase/`, plus `specific/gcp/` for IAM, secrets and billing |
| Supabase | `supabase/config.toml`, `supabase/migrations/` or `supabase/functions/`; `@supabase/supabase-js`, `@supabase/ssr` or `supabase_flutter` dependencies; or `SUPABASE_URL` and Supabase key variables | `specific/supabase/` and `specific/postgres/` |
| Apache Kafka | A Kafka client dependency (for example `kafkajs`, `confluent-kafka`, `org.apache.kafka:kafka-clients`, `Confluent.Kafka`, `franz-go`), `bootstrap.servers` settings, or a `kafka` service in a Compose file | `specific/kafka/` |
| RabbitMQ | An AMQP client (for example `amqplib`, `pika`, `RabbitMQ.Client`, `amqp091-go`, Spring AMQP), `amqp://` or `amqps://` URLs, `rabbitmq.conf`, or a `rabbitmq` service in a Compose file | `specific/rabbitmq/` |
| Android | Gradle files that apply `com.android.application` or `com.android.library` | `specific/android/` |
| Flutter | `pubspec.yaml` that depends on the `flutter` SDK | `specific/flutter/` |
| iOS | An Xcode project or workspace (`*.xcodeproj`, `*.xcworkspace`) with `*.swift` sources, `Package.swift`, SwiftUI or UIKit imports, `PrivacyInfo.xcprivacy` or `*.entitlements`, outside a game engine's or React Native's generated `ios/` folder | `specific/ios/`, plus `specific/mobile-games/` for games |
| React Native or Expo | `package.json` with a `react-native` or `expo` dependency, `app.json` or `app.config.*` with an `expo` key, `eas.json`, `metro.config.js`, or Expo Router files such as `app/_layout.tsx` | `specific/react-native/`, plus `specific/react/` and `specific/typescript/`, and `specific/ios/` and `specific/android/` for code in `ios/` and `android/` |
| Desktop app (Electron or Tauri) | An `electron` dependency, `forge.config.*` or `electron-builder` config, or `BrowserWindow`, `contextBridge` or `ipcMain` in code; or a `src-tauri/` folder with `tauri.conf.json`, a `Cargo.toml` with `tauri`, or `src-tauri/capabilities/*.json` | `specific/desktop/`, plus `specific/web/`, the front-end framework's folder, and `specific/nodejs/` for Electron's main process |
| Docker | `Dockerfile` or `Containerfile`, `compose.yaml` or `docker-compose.yml`, `.dockerignore` | `specific/docker/` |
| Kubernetes | YAML files with `apiVersion:` and `kind:`, `Chart.yaml`, `kustomization.yaml` | `specific/kubernetes/` |
| OpenTelemetry | OpenTelemetry SDK packages (`@opentelemetry/*`, `opentelemetry-*`, `OpenTelemetry.*`), `OTEL_*` environment variables, or a Collector configuration with `receivers`, `exporters` and `service.pipelines` | `specific/opentelemetry/` |
| AWS | `cdk.json`, CloudFormation/SAM templates with `AWS::` types, Terraform `provider "aws"` | `specific/aws/` |
| Microsoft Azure | `*.bicep` files, `bicepconfig.json`, ARM templates (`azuredeploy.json`), or Terraform `provider "azurerm"` | `specific/azure/` |
| Google Cloud | Terraform `provider "google"`, `cloudbuild.yaml`, `app.yaml`, or Google Cloud client libraries | `specific/gcp/` |
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
| Personal data: accounts, profiles, analytics or advertising SDKs, consent, account deletion | `general/privacy.md` |
| User-facing text, translations, dates, numbers, time zones | `general/localization.md` |
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
