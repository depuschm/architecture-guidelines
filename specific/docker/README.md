<!-- rule-prefix: DOCKER -->
# Docker (containers and images)

Scope: building container images with Docker, running them securely, and running multi-container applications with Docker Compose, mostly for local development and single-host deployments. For running containers on a cluster, see [Kubernetes](../kubernetes/README.md); for building and publishing images in CI, see [GitHub Actions](../github-actions/README.md). Secrets and supply-chain rules in [general/security.md](../../general/security.md) also apply.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Building best practices](https://docs.docker.com/build/building/best-practices/) (Docker Docs): **the baseline for Dockerfiles**: multi-stage builds, base images, `.dockerignore`, ephemeral containers, pinning, rebuilding, and advice for each Dockerfile instruction.
- `8` [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) (OWASP): **the baseline for container security**: the daemon socket, users, capabilities, privilege escalation, read-only file systems, resource limits, scanning and supply chain.
- `8` [Docker Compose](https://docs.docker.com/compose/) (Docker Docs): defining and running multi-container applications, including startup order, secrets, multiple Compose files and production use.
- `7` [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker): a consensus hardening benchmark for the Docker host, daemon and containers.
- `7` [NIST SP 800-190, Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final) (2017): the security concerns that containers bring, with recommendations for addressing them.

## Key rules

### Images

- `9` `DOCKER-1` **Run the application as a non-root user: create a user in the Dockerfile and switch to it with `USER`.** Running as an unprivileged user is the best way to prevent privilege escalation if the container is compromised. ([Docker, Building best practices: USER](https://docs.docker.com/build/building/best-practices/#user), [OWASP, Rule #2: Set a user](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-2-set-a-user))
- `9` `DOCKER-2` **Never pass secrets to a build through `ARG`, `ENV` or copied files. Use secret mounts or SSH mounts.** Build arguments and environment variables persist in the final image. ([Docker, Build secrets](https://docs.docker.com/build/building/secrets/))
- `8` `DOCKER-3` **Pin base images to a tag plus digest, and let a bot such as Dependabot update both.** Tags are mutable: the same tag can point to a different image when you rebuild. The general rule is `SEC-15` in [general/security.md](../../general/security.md). ([Docker, Pin base image versions](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions), [GitHub, Dependabot supported ecosystems: Docker](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories#docker))
- `7` `DOCKER-4` **Use multi-stage builds so that the final image contains only what the application needs to run, on a small base image from a trusted source.** The final image is smaller, and it leaves out build tools and packages it doesn't need. ([Docker, Multi-stage builds](https://docs.docker.com/build/building/multi-stage/), [Building best practices: choose the right base image](https://docs.docker.com/build/building/best-practices/#choose-the-right-base-image))
- `7` `DOCKER-5` **Rebuild images often, with `--pull` to fetch fresh base images, so that security fixes in the base image reach production.** ([Docker, Rebuild your images often](https://docs.docker.com/build/building/best-practices/#rebuild-your-images-often))
- `7` `DOCKER-6` **Start the main process with the exec form, such as `ENTRYPOINT ["app"]`, so that it runs as PID 1 and receives `SIGTERM`.** The shell form runs it under `/bin/sh -c`, which doesn't pass signals, so the app can't shut down gracefully. If the process doesn't reap child processes, run the container with `--init`. ([Dockerfile reference, ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint), [docker container run](https://docs.docker.com/reference/cli/docker/container/run/))
- `6` `DOCKER-7` **Order Dockerfile instructions from least to most often changed: copy the dependency manifests and install dependencies before copying the source code.** Otherwise every code change reinstalls all dependencies. ([Docker, Optimize cache usage: order your layers](https://docs.docker.com/build/cache/optimize/#order-your-layers))
- `6` `DOCKER-8` **Keep the build context small with a `.dockerignore` file.** It keeps unwanted files out of the build and speeds it up, especially with a remote builder. ([Docker, Build context: .dockerignore files](https://docs.docker.com/build/concepts/context/#dockerignore-files), [Building best practices: exclude with .dockerignore](https://docs.docker.com/build/building/best-practices/#exclude-with-dockerignore))
- `6` `DOCKER-9` **Give each container one concern: run the web app, the database and the cache as separate containers.** Separate containers are easier to scale horizontally and to reuse. ([Docker, Decouple applications](https://docs.docker.com/build/building/best-practices/#decouple-applications))

### Supply chain

- `8` `DOCKER-10` **Scan images for known vulnerabilities in CI, fail the build above an agreed severity, and keep scanning the images you have deployed.** ([OWASP, Rule #9: Integrate container scanning tools into your CI/CD pipeline](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-9-integrate-container-scanning-tools-into-your-cicd-pipeline), [Trivy, Container image](https://trivy.dev/docs/latest/target/container_image/))
- `6` `DOCKER-11` **Attach SBOM and provenance attestations to the images you publish, and sign them so that deployments can verify where an image came from.** ([Docker, Build attestations](https://docs.docker.com/build/metadata/attestations/), [OWASP, Rule #13: Enhance supply chain security](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-13-enhance-supply-chain-security), [Sigstore, Signing containers](https://docs.sigstore.dev/cosign/signing/signing_with_containers/))

### Running containers

- `9` `DOCKER-12` **Never mount the Docker socket into a container, and never expose the daemon over unauthenticated TCP.** Access to the socket is root access to the host. ([OWASP, Rule #1: Do not expose the Docker daemon socket](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-1-do-not-expose-the-docker-daemon-socket-even-to-the-containers), [Docker Engine security](https://docs.docker.com/engine/security/))
- `7` `DOCKER-13` **Run containers with least privilege: never use `--privileged`, drop all capabilities and add back only those needed, set `no-new-privileges`, and use a read-only root file system where possible.** ([OWASP, Rule #3: Limit capabilities](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-3-limit-capabilities-grant-only-specific-capabilities-needed-by-a-container), [Rule #4: Prevent in-container privilege escalation](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-4-prevent-in-container-privilege-escalation), [Rule #8: Set filesystem and volumes to read-only](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-8-set-filesystem-and-volumes-to-read-only))
- `7` `DOCKER-14` **Give containers runtime secrets as Compose or orchestrator secrets, mounted as files, rather than as environment variables.** Environment variables are visible to all processes and can end up in logs. ([Docker, Manage secrets securely in Docker Compose](https://docs.docker.com/compose/how-tos/use-secrets/), [OWASP, Rule #12: Utilize Docker Secrets](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html#rule-12-utilize-docker-secrets-for-sensitive-data-management))

### Compose

- `6` `DOCKER-15` **Make services wait for their dependencies to be ready, not only started: give the dependency a `healthcheck` and use `depends_on` with `condition: service_healthy`.** Compose otherwise waits only until a container is running. ([Docker, Control startup and shutdown order in Compose](https://docs.docker.com/compose/how-tos/startup-order/), [Dockerfile reference, HEALTHCHECK](https://docs.docker.com/reference/dockerfile/#healthcheck))
- `6` `DOCKER-16` **Keep one base `compose.yaml` and put environment-specific changes in extra files, such as `compose.override.yaml` for development and `compose.production.yaml` for production. In production, don't bind-mount application code.** ([Docker, Use Compose in production](https://docs.docker.com/compose/how-tos/production/#modify-your-compose-file-for-production), [Merge Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Docker build checks](https://docs.docker.com/build/checks/): built into `docker build`. Run `docker build --check`, and add `# check=error=true` to the Dockerfile so that violations fail the build. [`JSONArgsRecommended`](https://docs.docker.com/reference/build-checks/json-args-recommended/) flags shell-form `ENTRYPOINT` and `CMD`, and [`SecretsUsedInArgOrEnv`](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/) flags secret-like names in `ARG` and `ENV`. Checks `DOCKER-6`, and partly `DOCKER-2`.
- `6` [Trivy](https://trivy.dev/docs/latest/target/container_image/): scans images for known vulnerabilities and embedded secrets. [`trivy image --exit-code 1 --severity HIGH,CRITICAL`](https://trivy.dev/docs/latest/references/configuration/cli/trivy_image/) fails CI on serious findings. Checks `DOCKER-10`, and partly `DOCKER-2`.
- `6` [Docker Scout policy evaluation](https://docs.docker.com/scout/policy/): `docker scout policy` evaluates images locally or in CI. Its Severity-Based Vulnerability, Default Non-Root User, No outdated base images and Supply Chain Attestations policies partly check `DOCKER-10`, `DOCKER-1`, `DOCKER-5` and `DOCKER-11`.
- `6` [Hadolint](https://github.com/hadolint/hadolint): a Dockerfile linter that also runs ShellCheck on `RUN` instructions, with `--failure-threshold` to choose which severities fail CI. [DL3025](https://github.com/hadolint/hadolint/wiki/DL3025) flags shell-form `CMD` and `ENTRYPOINT`, [DL3002](https://github.com/hadolint/hadolint/wiki/DL3002) a final `USER root`, and [DL3006](https://github.com/hadolint/hadolint/wiki/DL3006) and [DL3007](https://github.com/hadolint/hadolint/wiki/DL3007) untagged or `latest` base images. Checks `DOCKER-6`, and partly `DOCKER-1` and `DOCKER-3`.

## Tutorials and further reading

- `7` [Get started](https://docs.docker.com/get-started/) (Docker Docs): the official introduction to containers, images, registries, Dockerfiles, multi-stage builds and Compose.
- `7` [Docker guides](https://docs.docker.com/guides/) (Docker Docs): language-specific guides, such as Node.js, Python, Go and .NET, that containerize an app, set up local development in containers and run tests.
- `6` [Docker Hardened Images](https://docs.docker.com/dhi/) (Docker Docs): minimal, continuously patched base images with SBOMs and provenance. The core images are free under Apache 2.0.
- `5` [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/) (Docker Docs): sync or rebuild services automatically while you edit code.
- `5` [Development Containers](https://containers.dev/): an open specification for defining a full development environment as a container.
