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

- `10` **Keep secrets out of source.** Use the Secret Manager in development and a vault in production. ([Microsoft, Safe storage of app secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets))
- `9` **Go async all the way and never block on async code with `.Result` or `.Wait()`.** ([Microsoft, ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices), [Fowler, Async guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md))
- `8` **Use the built-in DI container and follow its lifetime guidelines.** For example, don't resolve scoped services from singletons. ([Microsoft, Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection), [Dependency injection guidelines](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/guidelines))
- `8` **Add standard resilience (timeouts, retries, circuit breakers) to outgoing HTTP calls.** ([Microsoft, Build resilient HTTP apps](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience))
- `7` **Structure apps with Clean Architecture.** The application core defines interfaces, infrastructure implements them, and the core never references infrastructure. ([Microsoft, Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures))
- `7` **Return errors as ProblemDetails, and handle exceptions centrally.** ([Microsoft, Handle errors in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling))
- `7` **Expose health checks for load balancers and orchestrators.** ([Microsoft, Health checks](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks))
- `7` **Instrument with OpenTelemetry.** ([Microsoft, .NET observability with OpenTelemetry](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel))
- `7` **Enable nullable reference types in all projects.** ([Microsoft, Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/null-safety/nullable-reference-types))
- `7` **Test the HTTP pipeline with in-memory integration tests (`WebApplicationFactory`), and enforce layering with architecture tests.** ([Microsoft, Integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), [ArchUnitNET](https://github.com/TNG/ArchUnitNET))
- `6` **Bind configuration to strongly typed classes with the options pattern.** ([Microsoft, Options pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options))
- `6` **Follow the EF Core performance guidance for queries and change tracking.** ([Microsoft, EF Core performance](https://learn.microsoft.com/en-us/ef/core/performance/))

## Tutorials and further reading

- `7` [Aspire](https://aspire.dev/): tooling for building, running and observing distributed .NET apps locally and in the cloud.
- `6` [Clean Architecture template (Ardalis)](https://github.com/ardalis/CleanArchitecture) and [Clean Architecture template (Jason Taylor)](https://github.com/jasontaylordev/CleanArchitecture): community starting points.
- `6` [Testing in .NET](https://learn.microsoft.com/en-us/dotnet/core/testing/) (Microsoft).
