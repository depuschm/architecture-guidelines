<!-- rule-prefix: OPS -->
# Operations and reliability

Build systems that are observable, resilient to failure and cheap to operate.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html): the review framework for AWS workloads. See also [specific/aws](../specific/aws/README.md).
- `9` [The Twelve-Factor App](https://12factor.net/): baseline rules for building deployable, scalable services.
- `9` [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/): the review framework for Azure workloads.
- `9` [Google SRE books](https://sre.google/books/) (free online): service level objectives, monitoring, incident response and postmortems.
- `9` [AWS Builders' Library](https://aws.amazon.com/builders-library/): how Amazon builds and operates resilient distributed systems.
- `9` [Azure cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/): resilience patterns such as Retry, Circuit Breaker, Bulkhead and Queue-Based Load Leveling.
- `9` [OpenTelemetry documentation](https://opentelemetry.io/docs/): the vendor-neutral standard for traces, metrics and logs.
- `8` [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework): the review framework for Google Cloud workloads.

## Key rules

### Reliability targets

- `8` `OPS-2` **Monitor the four golden signals for every user-facing service: latency, traffic, errors and saturation.** ([Google SRE book, Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/))
- `7` `OPS-1` **Define SLOs from user-facing SLIs, and use the error budget to balance reliability against release speed.** ([Google SRE book, Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Embracing Risk](https://sre.google/sre-book/embracing-risk/), [SRE workbook, Implementing SLOs](https://sre.google/workbook/implementing-slos/))

### Resilience

- `9` `OPS-3` **Put a timeout on every remote call, and retry only with capped exponential backoff and jitter.** ([AWS Builders' Library, Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [Azure, Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry))
- `8` `OPS-4` **Design to prevent cascading failures, for example with load shedding and by avoiding retry storms.** ([Google SRE book, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), [AWS Builders' Library, Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/))
- `7` `OPS-5` **Stop calling a failing dependency with a circuit breaker, and isolate resources with bulkheads.** ([Fowler, Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html), [Azure, Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead))
- `6` `OPS-6` **Avoid fallback paths that are rarely exercised.** Prefer designs that keep working the same way during failure (static stability). ([AWS Builders' Library, Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/), [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/))
- `5` `OPS-7` **Buffer bursts of load with queues between producers and consumers.** ([Azure, Queue-Based Load Leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling))
- `4` `OPS-8` **Verify resilience with controlled chaos experiments.** ([Principles of Chaos Engineering](https://principlesofchaos.org/))

### Operability

- `8` `OPS-9` **Keep config in the environment, treat backing services as attached resources, and run stateless processes.** ([Twelve-Factor App, III Config](https://12factor.net/config), [IV Backing services](https://12factor.net/backing-services), [VI Processes](https://12factor.net/processes))
- `7` `OPS-10` **Expose health endpoints that load balancers and orchestrators can probe.** ([Azure, Health Endpoint Monitoring pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring))
- `7` `OPS-11` **Instrument with OpenTelemetry and follow its semantic conventions, so telemetry is portable and correlated.** ([OpenTelemetry, Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/), [Semantic conventions](https://opentelemetry.io/docs/specs/semconv/))
- `7` `OPS-12` **Run blameless postmortems and track their action items.** ([Google SRE book, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/))

## Tutorials and further reading

- `8` [Site Reliability Engineering, table of contents](https://sre.google/sre-book/table-of-contents/): the full SRE book, free online.
