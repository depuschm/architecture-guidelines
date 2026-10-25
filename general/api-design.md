<!-- rule-prefix: API -->
# API design

Design interfaces between systems that are consistent, evolvable and safe to call.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

Pick **one** style guide per organisation and follow it. Don't mix them.

- `9` [Google API Improvement Proposals (AIPs)](https://google.aip.dev/): detailed, resource-oriented rules for HTTP/JSON and gRPC APIs. ([Google Cloud API design guide](https://docs.cloud.google.com/apis/design) is the older companion.)
- `9` [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/): a complete, opinionated guide that is easy to adopt as-is.
- `9` [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) and [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest): contract formats for synchronous and event-driven APIs.
- `8` [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines): Azure and Microsoft Graph conventions.
- `8` [OWASP API Security Top 10](https://api-security.owasp.org/): the most common API security risks.
- `7` [Azure: RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design): a shorter introduction to the basics.

## Key rules

- `9` `API-1` **Make operations safe to retry, using idempotency keys where the method isn't naturally idempotent.** ([AWS Builders' Library, Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [IETF draft, Idempotency-Key header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/))
- `9` `API-2` **Evolve APIs in backward-compatible ways.** Treat breaking changes as a new major version. ([AIP-180, Backwards compatibility](https://google.aip.dev/180), [Semantic Versioning](https://semver.org/))
- `8` `API-3` **Use HTTP methods and status codes as their specification defines them.** ([RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110))
- `7` `API-4` **Design the API contract first and review it before implementing it.** ([Zalando, API First](https://opensource.zalando.com/restful-api-guidelines/))
- `7` `API-5` **Model HTTP APIs around resources and standard methods, not ad-hoc RPC verbs.** ([AIP-121, Resource-oriented design](https://google.aip.dev/121))
- `7` `API-6` **Paginate list endpoints from day one.** ([AIP-158, Pagination](https://google.aip.dev/158))
- `6` `API-7` **Return machine-readable errors in the Problem Details format.** ([RFC 9457, Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457))
- `6` `API-8` **With enough users, every observable behaviour will be depended on by someone, whether documented or not (Hyrum's law).** ([Hyrum's Law](https://www.hyrumslaw.com/))
- `6` `API-9` **Verify compatibility between providers and consumers with consumer-driven contract tests.** ([Robinson, Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html), [Pact](https://docs.pact.io/))
- `6` `API-10` **For gRPC and Protocol Buffers, follow the official dos and don'ts on field numbering and evolution.** ([Protocol Buffers, dos and don'ts](https://protobuf.dev/best-practices/dos-donts/), [gRPC guides](https://grpc.io/docs/guides/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [buf breaking](https://buf.build/docs/breaking/): compares Protobuf schemas with a previous version in CI and reports breaking changes, including [deleted fields whose numbers weren't reserved](https://buf.build/docs/breaking/rules/). Checks `API-2` and `API-10`.
- `7` [Google API Linter](https://linter.aip.dev/): lints Protobuf-defined APIs against the AIPs, for example [`page_size` on List methods](https://linter.aip.dev/158/request-page-size-field) and [Get support for every resource](https://linter.aip.dev/121/resource-must-support-get). Checks `API-6`, and partly `API-5`.
- `7` [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy): blocks a deployment unless contract tests show the new version is compatible with the versions already deployed. Checks `API-9`.
- `6` [oasdiff, breaking changes](https://github.com/oasdiff/oasdiff/blob/main/docs/BREAKING-CHANGES.md): reports breaking changes between two OpenAPI versions, and fails CI with `--fail-on ERR`. Checks `API-2`.
- `6` [Spectral OpenAPI rules](https://github.com/stoplightio/spectral/blob/develop/docs/reference/openapi-rules.md): lints OpenAPI documents in CI. The built-in ruleset checks basics, such as at least one 2xx or 3xx response per operation, and custom rulesets can encode your chosen style guide. Partly checks `API-3`.

## Tutorials and further reading

- `6` [GraphQL best practices](https://graphql.org/learn/best-practices/).
- `6` [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) (Stripe).
