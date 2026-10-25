<!-- rule-prefix: K8S -->
# Kubernetes

Scope: designing and running application workloads on Kubernetes clusters. For building the container images, see [Docker](../docker/README.md).

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

- `9` `K8S-1` **Give every container CPU and memory requests and a memory limit. Set CPU limits only where needed, for example on sensitive workloads.** ([Kubernetes, Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), [LearnKube, Production best practices](https://learnkube.com/production-best-practices), [Kubernetes, Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/))
- `9` `K8S-2` **Configure readiness, liveness and startup probes for their distinct purposes.** Check back-end services only in the readiness probe, never in the liveness probe. ([Kubernetes, Liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/), [Configure probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/))
- `8` `K8S-4` **Run multiple replicas, spread them across nodes and zones, and protect them with PodDisruptionBudgets.** ([Kubernetes, Topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/), [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/))
- `8` `K8S-5` **Deploy images by a specific version tag or by digest, never `:latest`.** Only digests are immutable. ([Kubernetes, Images](https://kubernetes.io/docs/concepts/containers/images/))
- `7` `K8S-3` **Handle `SIGTERM` and shut down gracefully within the termination grace period.** ([Kubernetes, Pod lifecycle: termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/))
- `5` `K8S-6` **Scale stateless workloads horizontally with the HorizontalPodAutoscaler.** ([Kubernetes, Autoscaling workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/))
- `4` `K8S-7` **Apply the recommended `app.kubernetes.io/*` labels.** ([Kubernetes, Recommended labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/))

### Security

- `9` `K8S-8` **Grant least-privilege RBAC, and give each workload its own service account.** ([Kubernetes, RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/), [RBAC: service account permissions](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#service-account-permissions), [Service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/))
- `8` `K8S-9` **Enforce the Restricted Pod Security Standard for application namespaces.** ([Kubernetes, Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/))
- `8` `K8S-10` **Start each namespace from a default-deny NetworkPolicy and allow only the traffic you need.** ([Kubernetes, Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/), [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/))
- `8` `K8S-11` **Encrypt Secrets at rest, restrict who can read them, and consider an external secret store.** ([Kubernetes, Good practices for Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/))
- `5` `K8S-12` **Decide your tenancy model (namespaces, clusters) explicitly.** ([Kubernetes, Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/))

### Delivery

- `6` `K8S-13` **Keep all manifests declarative and in Git, and let an agent reconcile the cluster to them (GitOps).** ([OpenGitOps principles](https://opengitops.dev/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `8` [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/): the built-in admission controller. Label a namespace `pod-security.kubernetes.io/enforce: restricted` and non-compliant pods are rejected. Checks `K8S-9`.
- `6` [kube-linter checks](https://docs.kubelinter.io/#/generated/checks): lints manifests in CI. Its default checks cover the `latest` tag, missing CPU requests and memory limits, missing anti-affinity or topology spread, the default service account, pods without a NetworkPolicy, and access to Secrets; probe checks are opt-in. Checks `K8S-1` and `K8S-5`, and partly `K8S-2`, `K8S-4`, `K8S-8`, `K8S-10` and `K8S-11`.
- `6` [Kyverno policy library](https://kyverno.io/policies/): admission policies that enforce rules inside the cluster, for example [requests and memory limits](https://kyverno.io/policies/best-practices/require-pod-requests-limits/require-pod-requests-limits/), a [default-deny NetworkPolicy for every new namespace](https://kyverno.io/policies/best-practices/add-network-policy/add-network-policy/), a [PodDisruptionBudget per workload](https://kyverno.io/policies/other/require-pdb/require-pdb/), [probes](https://kyverno.io/policies/best-practices/require-probes/require-probes/) and the [`app.kubernetes.io/name` label](https://kyverno.io/policies/best-practices/require-labels/require-labels/). Checks `K8S-1` and `K8S-10`, and partly `K8S-2`, `K8S-4` and `K8S-7`.
- `5` [Polaris checks](https://polaris.docs.fairwinds.com/checks/reliability/): an alternative to kube-linter, with reliability, [efficiency](https://polaris.docs.fairwinds.com/checks/efficiency/) and [security](https://polaris.docs.fairwinds.com/checks/security/) checks that [run in CI](https://polaris.docs.fairwinds.com/infrastructure-as-code/). It flags missing probes, the `latest` tag, missing PodDisruptionBudgets, and missing requests and memory limits (turn off `cpuLimitsMissing` to match `K8S-1`). Checks `K8S-1`, `K8S-2` and `K8S-5`, and partly `K8S-4` and `K8S-8`.
- `5` [OPA Gatekeeper library](https://open-policy-agent.github.io/gatekeeper-library/website/): an alternative policy engine, with policies for [disallowed image tags](https://open-policy-agent.github.io/gatekeeper-library/website/validation/disallowedtags/), [required probes](https://open-policy-agent.github.io/gatekeeper-library/website/validation/requiredprobes/) and [container requests](https://open-policy-agent.github.io/gatekeeper-library/website/validation/containerrequests/). Checks `K8S-5`, and partly `K8S-1` and `K8S-2`.

## Tutorials and further reading

- `7` [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) (official).
