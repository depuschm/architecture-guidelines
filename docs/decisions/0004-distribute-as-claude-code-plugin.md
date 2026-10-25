---
status: accepted
date: 2026-10-25
decision-makers: depuschm
---

# Distribute the skills as a Claude Code plugin that tracks every commit

## Context and Problem Statement

The AI skills need the guideline files next to them, and users should receive improvements without manual copying. How do we distribute them?

## Decision Drivers

* Skills must be able to read the guideline files they cite.
* Users should get updates with little effort.
* Other agent tools should still be able to use the skills.

## Considered Options

* Ask users to copy the `skills/` folders into their projects
* A plugin with versioned releases (bump `version` for each release)
* A plugin without a fixed version, so every commit is a release

## Decision Outcome

Chosen option: "A plugin without a fixed version". The repository is both the plugin and its own marketplace. Installed copies include the guideline files, which skills reach through `${CLAUDE_PLUGIN_ROOT}`. Claude Code only updates a plugin when its computed version changes. Without a `version` field, it [tracks commits](https://code.claude.com/docs/en/plugins/host-marketplace.md), so every merged change reaches users.

### Consequences

* Good, because guideline fixes reach users without a release step.
* Good, because the `skills/` folders follow the [Agent Skills format](https://agentskills.io/specification), so other tools can use them too.
* Bad, because users can't pin an older state. If that's needed later, switch to versioned releases.

### Confirmation

CI runs `claude plugin validate .`, and a test install lists all skills.
