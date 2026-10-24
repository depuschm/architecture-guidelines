# API design

Design interfaces between systems that are consistent, evolvable and safe to call.

## Adopted references

Pick **one** style guide per organisation and follow it. Don't mix them.

- [Google API Improvement Proposals (AIPs)](https://google.aip.dev/): detailed, resource-oriented rules for HTTP/JSON and gRPC APIs. ([Google Cloud API design guide](https://docs.cloud.google.com/apis/design) is the older companion.)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines): Azure and Microsoft Graph conventions.
- [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/): a complete, opinionated guide that is easy to adopt as-is.
- [Azure: RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design): a shorter introduction to the basics.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) and [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest): contract formats for synchronous and event-driven APIs.
- [OWASP API Security Top 10](https://owasp.org/API-Security/): the most common API security risks.

## Key rules

- **Design the API contract first and review it before implementing it.** ([Zalando, API First](https://opensource.zalando.com/restful-api-guidelines/))
- **Model HTTP APIs around resources and standard methods, not ad-hoc RPC verbs.** ([AIP-121, Resource-oriented design](https://google.aip.dev/121))
- **Use HTTP methods and status codes as their specification defines them.** ([RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110))
- **Return machine-readable errors in the Problem Details format.** ([RFC 9457, Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457))
- **Paginate list endpoints from day one.** ([AIP-158, Pagination](https://google.aip.dev/158))
- **Make operations safe to retry, using idempotency keys where the method isn't naturally idempotent.** ([AWS Builders' Library, Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [IETF draft, Idempotency-Key header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/))
- **Evolve APIs in backward-compatible ways.** Treat breaking changes as a new major version. ([AIP-180, Backwards compatibility](https://google.aip.dev/180), [Semantic Versioning](https://semver.org/))
- **With enough users, every observable behaviour will be depended on by someone, whether documented or not (Hyrum's law).** ([Hyrum's Law](https://www.hyrumslaw.com/))
- **Verify compatibility between providers and consumers with consumer-driven contract tests.** ([Robinson, Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html), [Pact](https://docs.pact.io/))
- **For gRPC and Protocol Buffers, follow the official dos and don'ts on field numbering and evolution.** ([Protocol Buffers, dos and don'ts](https://protobuf.dev/best-practices/dos-donts/), [gRPC guides](https://grpc.io/docs/guides/))

## Tutorials and further reading

- [GraphQL best practices](https://graphql.org/learn/best-practices/).
- [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) (Stripe).
