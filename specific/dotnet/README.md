# .NET / ASP.NET Core

Scope: back-end services, web APIs, web apps and worker services on modern .NET.

## Adopted references

- [.NET Architecture Guides](https://learn.microsoft.com/en-us/dotnet/architecture/) (Microsoft): **the baseline.** A hub of free e-books, including:
  - [Architect Modern Web Applications with ASP.NET Core and Azure](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/): monolithic and Clean Architecture web apps.
  - [.NET Microservices: Architecture for Containerized .NET Applications](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/): DDD, CQRS and microservices in .NET.
  - [Architecting Cloud Native .NET Applications for Azure](https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/).
- [ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices) (Microsoft): performance and reliability rules.
- [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/) (Microsoft): for designing reusable libraries and public APIs.
- [C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) (Microsoft).
- [eShop reference application](https://github.com/dotnet/eShop) (Microsoft): a current reference architecture.
- [ASP.NET Core diagnostic scenarios: async guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md) (David Fowler).

## Key rules

- **Structure apps with Clean Architecture.** The application core defines interfaces, infrastructure implements them, and the core never references infrastructure. ([Microsoft, Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures))
- **Use the built-in DI container and follow its lifetime guidelines.** For example, don't resolve scoped services from singletons. ([Microsoft, Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection), [Dependency injection guidelines](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/guidelines))
- **Bind configuration to strongly typed classes with the options pattern.** ([Microsoft, Options pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options))
- **Keep secrets out of source.** Use the Secret Manager in development and a vault in production. ([Microsoft, Safe storage of app secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets))
- **Go async all the way and never block on async code with `.Result` or `.Wait()`.** ([Microsoft, ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices), [Fowler, Async guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md))
- **Add standard resilience (timeouts, retries, circuit breakers) to outgoing HTTP calls.** ([Microsoft, Build resilient HTTP apps](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience))
- **Return errors as ProblemDetails, and handle exceptions centrally.** ([Microsoft, Handle errors in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling))
- **Expose health checks for load balancers and orchestrators.** ([Microsoft, Health checks](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks))
- **Instrument with OpenTelemetry.** ([Microsoft, .NET observability with OpenTelemetry](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel))
- **Enable nullable reference types in all projects.** ([Microsoft, Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/null-safety/nullable-reference-types))
- **Test the HTTP pipeline with in-memory integration tests (`WebApplicationFactory`), and enforce layering with architecture tests.** ([Microsoft, Integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), [ArchUnitNET](https://github.com/TNG/ArchUnitNET))
- **Follow the EF Core performance guidance for queries and change tracking.** ([Microsoft, EF Core performance](https://learn.microsoft.com/en-us/ef/core/performance/))

## Tutorials and further reading

- [Aspire](https://aspire.dev/): tooling for building, running and observing distributed .NET apps locally and in the cloud.
- [Clean Architecture template (Ardalis)](https://github.com/ardalis/CleanArchitecture) and [Clean Architecture template (Jason Taylor)](https://github.com/jasontaylordev/CleanArchitecture): community starting points.
- [Testing in .NET](https://learn.microsoft.com/en-us/dotnet/core/testing/) (Microsoft).
