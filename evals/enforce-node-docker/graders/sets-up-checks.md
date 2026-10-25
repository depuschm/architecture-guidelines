---
type: llm
weight: 2
---

The repository has a Dockerfile (`FROM node:latest`, no `USER`, shell-form `CMD`) and a workflow (`actions/checkout@v4` not pinned to a commit SHA, no `permissions` block), and no automated checks for either.

PASS if the agent changed or added CI configuration so that both the Dockerfile and the workflows are checked automatically (for example Hadolint, `docker build --check` or Trivy for the Dockerfile, and zizmor, actionlint or CodeQL for the workflows), and the final reply says which rules each check enforces.
FAIL if it only gave advice without changing files, added only one of the two kinds of checks, or claimed checks or results it didn't actually set up.
