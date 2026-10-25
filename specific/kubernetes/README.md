# Kubernetes

Scope: designing and running application workloads on Kubernetes clusters.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) (Kubernetes): **the baseline for cluster and workload security reviews.**
- `8` [Kubernetes configuration good practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/) (Kubernetes): **the baseline for manifests.**
- `8` [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes): a hardening benchmark for clusters.
- `7` [Production best practices checklist](https://learnkube.com/production-best-practices) (LearnKube): a practical workload readiness checklist.
- `7` [Helm chart best practices](https://helm.sh/docs/chart_best_practices/) and [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/).
- `7` [OpenGitOps principles](https://opengitops.dev/): declarative, versioned, pulled and continuously reconciled delivery.

## Key rules

### Workloads

- `9` **Give every container CPU and memory requests and a memory limit. Set CPU limits only where needed, for example on sensitive workloads.** ([Kubernetes, Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), [LearnKube, Production best practices](https://learnkube.com/production-best-practices), [Kubernetes, Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/))
- `9` **Configure readiness, liveness and startup probes for their distinct purposes.** Check back-end services only in the readiness probe, never in the liveness probe. ([Kubernetes, Liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/), [Configure probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/))
- `8` **Handle `SIGTERM` and shut down gracefully within the termination grace period.** ([Kubernetes, Pod lifecycle: termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/))
- `8` **Run multiple replicas, spread them across nodes and zones, and protect them with PodDisruptionBudgets.** ([Kubernetes, Topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/), [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/))
- `8` **Deploy images by a specific version tag or by digest, never `:latest`.** Only digests are immutable. ([Kubernetes, Images](https://kubernetes.io/docs/concepts/containers/images/))
- `5` **Scale stateless workloads horizontally with the HorizontalPodAutoscaler.** ([Kubernetes, Autoscaling workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/))
- `4` **Apply the recommended `app.kubernetes.io/*` labels.** ([Kubernetes, Recommended labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/))

### Security

- `9` **Grant least-privilege RBAC, and give each workload its own service account.** ([Kubernetes, RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/), [RBAC: service account permissions](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#service-account-permissions), [Service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/))
- `8` **Enforce the Restricted Pod Security Standard for application namespaces.** ([Kubernetes, Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/))
- `8` **Start each namespace from a default-deny NetworkPolicy and allow only the traffic you need.** ([Kubernetes, Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/), [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/))
- `8` **Encrypt Secrets at rest, restrict who can read them, and consider an external secret store.** ([Kubernetes, Good practices for Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/))
- `5` **Decide your tenancy model (namespaces, clusters) explicitly.** ([Kubernetes, Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/))

### Delivery

- `6` **Keep all manifests declarative and in Git, and let an agent reconcile the cluster to them (GitOps).** ([OpenGitOps principles](https://opengitops.dev/))

## Tutorials and further reading

- `7` [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) (official).
