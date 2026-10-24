# Operations and reliability

Build systems that are observable, resilient to failure and cheap to operate.

## Adopted references

- [The Twelve-Factor App](https://12factor.net/): baseline rules for building deployable, scalable services.
- Cloud well-architected frameworks. Use your provider's framework for reviews:
  - [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) (see also [specific/aws](../specific/aws/README.md))
  - [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
  - [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
- [Google SRE books](https://sre.google/books/) (free online): service level objectives, monitoring, incident response and postmortems.
- [AWS Builders' Library](https://aws.amazon.com/builders-library/): how Amazon builds and operates resilient distributed systems.
- [Azure cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/): resilience patterns such as Retry, Circuit Breaker, Bulkhead and Queue-Based Load Leveling.
- [OpenTelemetry documentation](https://opentelemetry.io/docs/): the vendor-neutral standard for traces, metrics and logs.

## Key rules

### Reliability targets

- **Define SLOs from user-facing SLIs, and use the error budget to balance reliability against release speed.** ([Google SRE book, Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Embracing Risk](https://sre.google/sre-book/embracing-risk/), [SRE workbook, Implementing SLOs](https://sre.google/workbook/implementing-slos/))
- **Monitor the four golden signals for every user-facing service: latency, traffic, errors and saturation.** ([Google SRE book, Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/))

### Resilience

- **Put a timeout on every remote call, and retry only with capped exponential backoff and jitter.** ([AWS Builders' Library, Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [Azure, Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry))
- **Stop calling a failing dependency with a circuit breaker, and isolate resources with bulkheads.** ([Fowler, Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html), [Azure, Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead))
- **Design to prevent cascading failures, for example with load shedding and by avoiding retry storms.** ([Google SRE book, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), [AWS Builders' Library, Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/))
- **Avoid fallback paths that are rarely exercised.** Prefer designs that keep working the same way during failure (static stability). ([AWS Builders' Library, Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/), [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/))
- **Buffer bursts of load with queues between producers and consumers.** ([Azure, Queue-Based Load Leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling))
- **Verify resilience with controlled chaos experiments.** ([Principles of Chaos Engineering](https://principlesofchaos.org/))

### Operability

- **Keep config in the environment, treat backing services as attached resources, and run stateless processes.** ([Twelve-Factor App, III Config](https://12factor.net/config), [IV Backing services](https://12factor.net/backing-services), [VI Processes](https://12factor.net/processes))
- **Expose health endpoints that load balancers and orchestrators can probe.** ([Azure, Health Endpoint Monitoring pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring))
- **Instrument with OpenTelemetry and follow its semantic conventions, so telemetry is portable and correlated.** ([OpenTelemetry, Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/), [Semantic conventions](https://opentelemetry.io/docs/specs/semconv/))
- **Run blameless postmortems and track their action items.** ([Google SRE book, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/))

## Tutorials and further reading

- [Site Reliability Engineering, table of contents](https://sre.google/sre-book/table-of-contents/): the full SRE book, free online.
