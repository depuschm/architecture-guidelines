<!-- rule-prefix: OTEL -->
# OpenTelemetry

Scope: instrumenting services for traces, metrics and logs with OpenTelemetry, and running the OpenTelemetry Collector between services and observability backends. The general rules are in [general/operations-reliability.md](../../general/operations-reliability.md): instrument with OpenTelemetry and follow its semantic conventions (`OPS-11`), and monitor the four golden signals (`OPS-2`). Keeping secrets and personal data out of logs is `SEC-4` in [general/security.md](../../general/security.md). For language-specific setup, see [.NET](../dotnet/README.md) (`DOTNET-8`) and the language pages of the OpenTelemetry documentation; for exporting telemetry from serverless platforms, see [Serverless and edge hosting](../web-hosting/README.md) (`HOST-13`).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [OpenTelemetry documentation](https://opentelemetry.io/docs/): **the baseline**: concepts, signals, context propagation, instrumentation per language, zero-code instrumentation, sampling and the Collector.
- `8` [Collector](https://opentelemetry.io/docs/collector/) (OpenTelemetry docs): when to use a Collector, its configuration, the agent and gateway deployment patterns, scaling and internal telemetry.
- `8` [Collector configuration best practices](https://opentelemetry.io/docs/security/config-best-practices/) and [Collector hosting best practices](https://opentelemetry.io/docs/security/hosting-best-practices/) (OpenTelemetry docs): securing the Collector's configuration, network exposure, permissions and resource use.
- `8` [Trace Context](https://www.w3.org/TR/trace-context/) (W3C Recommendation): the `traceparent` and `tracestate` HTTP headers that OpenTelemetry propagates by default.
- `8` [Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/) (OpenTelemetry docs): data minimization, and removing, hashing or truncating sensitive attributes with Collector processors.
- `7` [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/): standard names for attributes, spans, metrics, events and resources, per area such as HTTP, databases and messaging.

## Key rules

### Resources and naming

- `8` `OTEL-1` **Set `service.name` explicitly in every service, with the same value for all instances of the service, and add `service.version` and `deployment.environment.name` as resource attributes.** Otherwise the SDK reports `unknown_service`. Set them with `OTEL_SERVICE_NAME` and `OTEL_RESOURCE_ATTRIBUTES`, and let the SDK's resource detectors add host, container, Kubernetes and cloud attributes. ([OpenTelemetry, Resources](https://opentelemetry.io/docs/concepts/resources/#semantic-attributes-with-sdk-provided-default-value), [Service semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/service/))
- `6` `OTEL-2` **Before you name a custom attribute or metric, look for it in the semantic conventions; when none fits, prefix the new name with your company's reverse domain name, such as `com.acme.`, or with your application's name.** Don't reuse an existing semantic convention namespace as the prefix: OpenTelemetry or other instrumentation may later use the same name for something else. ([Semantic conventions, Naming: recommendations for application developers](https://opentelemetry.io/docs/specs/semconv/general/naming/#recommendations-for-application-developers))

### Instrumentation and context

- `8` `OTEL-3` **Propagate trace context across every process boundary, including queues: keep the default W3C Trace Context propagator for HTTP and gRPC, and have producers attach the context to each message.** Without it, consumer traces can't be connected to the producers that caused them. ([OpenTelemetry, Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/), [W3C, Trace Context](https://www.w3.org/TR/trace-context/), [Semantic conventions for messaging spans: context propagation](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-spans/#context-propagation))
- `7` `OTEL-4` **Start with zero-code instrumentation or instrumentation libraries for your frameworks and clients, then add code-based spans, attributes and metrics for the business operations that matter.** Zero-code instrumentation covers the edges of the application, such as requests, database calls and queue calls, but usually not your own code. ([OpenTelemetry, Instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/), [Zero-code](https://opentelemetry.io/docs/concepts/instrumentation/zero-code/))
- `7` `OTEL-5` **Correlate logs with traces: keep your logging library, connect it to OpenTelemetry with a log appender (bridge) so that each record carries the active trace and span IDs, and prefer structured logs.** ([OpenTelemetry, Logs: log appender / bridge](https://opentelemetry.io/docs/concepts/signals/logs/#log-appender--bridge), [OpenTelemetry Logging: log correlation](https://opentelemetry.io/docs/specs/otel/logs/#log-correlation))
- `7` `OTEL-6` **Keep span names and metric attributes low-cardinality: use route templates such as `/users/{id}` instead of raw paths, and keep user IDs, request IDs and other unbounded values off metric attributes.** Every attribute combination costs memory. The metrics SDK keeps at most 2000 combinations per metric by default and folds the rest into one data point marked `otel.metric.overflow=true`. ([OpenTelemetry, Metrics: cardinality limits](https://opentelemetry.io/docs/concepts/signals/metrics/#cardinality-limits), [Tracing API: span](https://opentelemetry.io/docs/specs/otel/trace/api/#span), [Semantic conventions for HTTP metrics](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/))
- `6` `OTEL-7` **Treat trace context from outside as untrusted: ignore or sanitize incoming trace headers from callers you don't trust, don't send internal context to external services, and never put credentials or personal data in baggage.** ([OpenTelemetry, Context propagation: security best practices](https://opentelemetry.io/docs/concepts/context-propagation/#security-best-practices))

### Sampling

- `6` `OTEL-8` **Choose sampling deliberately: don't sample when you produce little data, use consistent probability (head) sampling to cut volume cheaply, and add tail sampling in a Collector tier when you must keep every error or slow trace.** All spans of a trace must reach the same tail-sampling Collector, so route them by trace ID with the load-balancing exporter. ([OpenTelemetry, Sampling](https://opentelemetry.io/docs/concepts/sampling/), [Gateway deployment pattern](https://opentelemetry.io/docs/collector/deploy/gateway/), [Tail sampling processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md))

### Collector

- `8` `OTEL-9` **Make `memory_limiter` the first processor in every Collector pipeline, set `GOMEMLIMIT` to about 80% of the Collector's hard memory limit, and batch data after sampling and filtering, preferably with the exporter's `sending_queue` batching.** Without limits, a burst of telemetry can crash the Collector with an out-of-memory error. ([OpenTelemetry Collector, Recommended processors](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/README.md#recommended-processors), [Memory limiter processor: best practices](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/memorylimiterprocessor/README.md#best-practices), [Exporter helper](https://github.com/open-telemetry/opentelemetry-collector/blob/main/exporter/exporterhelper/README.md))
- `8` `OTEL-10` **Secure every Collector: bind receivers to `localhost` or a specific interface instead of `0.0.0.0`, require TLS and authentication on receivers that other hosts send to, keep credentials in a secret store or environment variables, and include only the components you use.** ([OpenTelemetry, Collector configuration best practices](https://opentelemetry.io/docs/security/config-best-practices/), [Protect against denial of service attacks](https://opentelemetry.io/docs/security/config-best-practices/#protect-against-denial-of-service-attacks), [Collector hosting best practices](https://opentelemetry.io/docs/security/hosting-best-practices/))
- `7` `OTEL-11` **Send telemetry over OTLP to an OpenTelemetry Collector, running as an agent next to the service or as a gateway, rather than from each service straight to a vendor.** The Collector then handles retries, batching, encryption and filtering of sensitive data, and services don't need vendor-specific exporters. ([OpenTelemetry, Collector: when to use a collector](https://opentelemetry.io/docs/collector/#when-to-use-a-collector), [Deploy the Collector](https://opentelemetry.io/docs/collector/deploy/))

### Sensitive data

- `8` `OTEL-12` **Keep secrets and personal data out of telemetry: don't record what you don't need, and remove, hash or truncate what instrumentation captures anyway, for example with the Collector's `redaction`, `attributes`, `transform` or `filter` processors.** You are responsible for what instrumentation libraries capture, too, and a hash of a small value space, such as numeric user IDs, can be reversed. ([OpenTelemetry, Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/), [Collector configuration best practices: scrub sensitive data](https://opentelemetry.io/docs/security/config-best-practices/#scrub-sensitive-data))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `6` [Weaver live check](https://github.com/open-telemetry/weaver/blob/main/crates/weaver_live_check/README.md): an OpenTelemetry tool that receives the telemetry your tests emit over OTLP, compares it with the semantic conventions or your own registry, and exits with an error when it finds a violation, such as an attribute missing from the registry. Rego policies add your own checks. Partly checks `OTEL-2` and `OPS-11`.
- `5` [Collector `validate` command](https://opentelemetry.io/docs/collector/configuration/#location): `otelcol validate --config=…` checks a Collector configuration without starting it, so that CI can reject an invalid one. It rejects a `memory_limiter` without a memory limit or check interval, but doesn't require one. Partly checks `OTEL-9`.

## Tutorials and further reading

- `7` [Getting started](https://opentelemetry.io/docs/getting-started/) (OpenTelemetry docs): where to start as a developer or as an operator.
- `7` [OpenTelemetry Demo](https://opentelemetry.io/docs/demo/) (OpenTelemetry docs): a multi-language microservice application, instrumented with OpenTelemetry, to run with Docker or Kubernetes and explore.
- `6` [Training](https://opentelemetry.io/training/) (OpenTelemetry): the free Linux Foundation course *Getting Started with OpenTelemetry* and the OpenTelemetry Certified Associate certification.
