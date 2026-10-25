# Specific guidelines

One folder per platform or service. Each folder adopts the platform's official guidance where it exists, and adds short, sourced rules only where needed. The [general guidelines](../general/README.md) still apply.

### Games

- [Game development](gamedev/README.md): engine-independent game architecture (game loop, multiplayer, save data, frame budgets).
- [Unity](unity/README.md): game and real-time 3D projects.
- [Godot](godot/README.md): games built with Godot 4 and GDScript.
- [Unreal Engine](unreal/README.md): Unreal Engine 5 games in C++ and Blueprint.

### Web and back end

- [Web front end](web/README.md): framework-independent accessibility, performance, security and resilience.
- [React](react/README.md): web front ends.
- [Next.js](nextjs/README.md): full-stack React apps with the App Router.
- [Vue](vue/README.md): Vue 3 apps, with Pinia, Vue Router and Nuxt.
- [Svelte and SvelteKit](svelte/README.md): Svelte 5 and SvelteKit apps.
- [Node.js](nodejs/README.md): back-end services in TypeScript.
- [Python](python/README.md): Python applications and services, including FastAPI and Django.
- [.NET / ASP.NET Core](dotnet/README.md): back-end services and web apps.

### Mobile

- [Android](android/README.md): native Android apps.
- [Flutter](flutter/README.md): cross-platform apps.

### Infrastructure and automation

- [Docker](docker/README.md): container images, container security and Docker Compose.
- [Kubernetes](kubernetes/README.md): running workloads on Kubernetes.
- [AWS](aws/README.md): workloads on Amazon Web Services.
- [Terraform](terraform/README.md): infrastructure as code with Terraform or OpenTofu.
- [GitHub Actions](github-actions/README.md): CI/CD and automation workflows.

## Adding a platform

Copy [`_template/`](_template/README.md) to a new lower-case folder and follow [CONTRIBUTING.md](../CONTRIBUTING.md#4-adding-a-platform-folder).
