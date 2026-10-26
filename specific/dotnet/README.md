<!-- rule-prefix: DOTNET -->
# .NET / ASP.NET Core

Scope: back-end services, web APIs, web apps and worker services on modern .NET.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [.NET Architecture Guides](https://learn.microsoft.com/en-us/dotnet/architecture/) (Microsoft): **the baseline.** A hub of free e-books, including:
  - `9` [Architect Modern Web Applications with ASP.NET Core and Azure](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/): monolithic and Clean Architecture web apps.
  - `8` [.NET Microservices: Architecture for Containerized .NET Applications](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/): DDD, CQRS and microservices in .NET.
  - `6` [Architecting Cloud Native .NET Applications for Azure](https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/).
- `9` [ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices) (Microsoft): performance and reliability rules.
- `8` [eShop reference application](https://github.com/dotnet/eShop) (Microsoft): a current reference architecture.
- `8` [ASP.NET Core diagnostic scenarios: async guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md) (David Fowler).
- `7` [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/) (Microsoft): for designing reusable libraries and public APIs.
- `7` [C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) (Microsoft).

## Key rules

- `9` `DOTNET-1` **Load secrets through configuration providers: user secrets (the Secret Manager) in development, and Azure Key Vault or another vault in production, never `appsettings.json` or source code.** This is how .NET apps follow `SEC-2` in [general/security.md](../../general/security.md). ([Microsoft, Safe storage of app secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets))
- `9` `DOTNET-2` **Go async all the way and never block on async code with `.Result` or `.Wait()`.** ([Microsoft, ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices), [Fowler, Async guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md))
- `8` `DOTNET-3` **Use the built-in DI container and follow its lifetime guidelines.** For example, don't resolve scoped services from singletons. ([Microsoft, Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection), [Dependency injection guidelines](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/guidelines))
- `8` `DOTNET-4` **Add `AddStandardResilienceHandler` from `Microsoft.Extensions.Http.Resilience` to outgoing `HttpClient`s.** It applies timeouts, retries with backoff and a circuit breaker, as `OPS-3` and `OPS-5` in [general/operations-reliability.md](../../general/operations-reliability.md) ask. ([Microsoft, Build resilient HTTP apps](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience))
- `7` `DOTNET-5` **When the domain has real business logic, structure the solution with Clean Architecture: an application core that defines interfaces, and infrastructure projects that implement them and that the core never references.** This is the .NET form of `STYLE-6` in [general/architecture-styles.md](../../general/architecture-styles.md), which also says when the layers aren't worth it. ([Microsoft, Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures))
- `7` `DOTNET-6` **Register `AddProblemDetails` and `UseExceptionHandler`, so that errors are returned as ProblemDetails and exceptions are handled in one place.** The general rule is `API-7` in [general/api-design.md](../../general/api-design.md). ([Microsoft, Handle errors in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling))
- `7` `DOTNET-7` **Map separate liveness and readiness endpoints with `MapHealthChecks`, selecting the checks for each by tag.** The general rule is `OPS-10` in [general/operations-reliability.md](../../general/operations-reliability.md); on Kubernetes, see `K8S-2`. ([Microsoft, Health checks](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks))
- `7` `DOTNET-8` **Instrument with the OpenTelemetry .NET SDK, or with the .NET Aspire service defaults, which configure it for you.** The general rule is `OPS-11` in [general/operations-reliability.md](../../general/operations-reliability.md). ([Microsoft, .NET observability with OpenTelemetry](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel))
- `7` `DOTNET-9` **Enable nullable reference types in all projects.** ([Microsoft, Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/null-safety/nullable-reference-types))
- `7` `DOTNET-10` **Test the HTTP pipeline with in-memory integration tests (`WebApplicationFactory`), and enforce layering with architecture tests.** ([Microsoft, Integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), [ArchUnitNET](https://github.com/TNG/ArchUnitNET))
- `6` `DOTNET-11` **Bind configuration to strongly typed classes with the options pattern.** ([Microsoft, Options pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options))
- `6` `DOTNET-12` **Follow the EF Core performance guidance for queries and change tracking.** ([Microsoft, EF Core performance](https://learn.microsoft.com/en-us/ef/core/performance/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Built-in DI scope validation](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/overview#scope-validation): in the Development environment, the default service provider fails when scoped services are resolved from the root provider or injected into singletons. [Integration tests run in Development by default](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), so they catch it. Checks `DOTNET-3`.
- `7` [Nullable warnings as errors](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/errors-warnings): `<WarningsAsErrors>nullable</WarningsAsErrors>` makes nullability warnings fail the build. Set it for every project in [Directory.Build.props](https://learn.microsoft.com/en-us/visualstudio/msbuild/customize-by-directory). Checks `DOTNET-9`.
- `7` [CA1849](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1849): flags blocking calls inside async methods when an async version exists. It's off by default; enable it, and [build with `-warnaserror`](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview) to fail on it. Partly checks `DOTNET-2`.
- `7` [GitHub secret scanning push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection): blocks pushes that contain credentials. See [general/security.md](../../general/security.md) for more secret scanners. Checks `DOTNET-1`.
- `6` [ArchUnitNET](https://archunitnet.readthedocs.io/en/latest/guide/): architecture tests, for example that the core namespace doesn't depend on infrastructure, or that modules are free of cycles. Checks `DOTNET-5` and `DOTNET-10`.
- `6` [Microsoft.VisualStudio.Threading.Analyzers, VSTHRD002](https://microsoft.github.io/vs-threading/analyzers/VSTHRD002.html) and [VSTHRD103](https://microsoft.github.io/vs-threading/analyzers/VSTHRD103.html): warn about synchronous waits on tasks, such as `.Wait()`, `.Result` and `.GetAwaiter().GetResult()`. Enable only these rules; others in the package assume Visual Studio extensions. Checks `DOTNET-2`.

## Tutorials and further reading

- `7` [Aspire](https://aspire.dev/): tooling for building, running and observing distributed .NET apps locally and in the cloud.
- `6` [Clean Architecture template (Ardalis)](https://github.com/ardalis/CleanArchitecture) and [Clean Architecture template (Jason Taylor)](https://github.com/jasontaylordev/CleanArchitecture): community starting points.
- `6` [Testing in .NET](https://learn.microsoft.com/en-us/dotnet/core/testing/) (Microsoft).
