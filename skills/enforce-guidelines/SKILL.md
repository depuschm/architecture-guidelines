---
name: enforce-guidelines
description: Set up automated checks for the Architecture Guidelines in a project. Detects the project's platforms, picks the linters, scanners and built-in checks that the guidelines' "How to enforce" sections name, and wires them into CI, commit hooks or editor config, with each check labelled by the rule IDs it enforces. Use when asked to automate or enforce the guidelines, add linters or security scanners to CI, harden a pipeline, or "make CI check our architecture rules".
argument-hint: "[path] [--plan-only]"
---

# Enforce guidelines

Turn the guidelines that tools can check into automated checks in the target project. Only use tools that the guidelines name. Every check you add must say which rules it enforces.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path (the skill isn't running as a plugin), the root is two directories above this `SKILL.md` file. You need:

- `<root>/RULES.md`: every rule with its score and a **Checked by** column, which lists the tools that check it.
- `<root>/specific/<platform>/` and `<root>/general/`: the **How to enforce** section of each file explains how to run each tool, and which rule IDs it checks fully or partly.
- `<root>/skills/architecture-review/SKILL.md`, section "Detect platforms": the table of signals that identify each platform.

## 1. Detect platforms and existing tooling

1. Find the platforms with the detection table. A repository often matches several, for example Node.js, Docker and GitHub Actions.
2. Inventory what the project already runs: CI configuration (`.github/workflows/`, `.gitlab-ci.yml` and others), commit hooks (`.pre-commit-config.yaml`, Husky, lefthook), linter configs (`eslint.config.*`, `pyproject.toml` tool sections, `.hadolint.yaml` and others), and package scripts. Extend what exists rather than adding a parallel setup.

## 2. Plan

1. For each detected platform, plus the general files that apply (`general/security.md`, `general/testing-delivery.md`, and `general/authentication.md`, `general/privacy.md`, `general/localization.md`, `general/releases.md` or `general/repositories.md` when the project signs users in, handles personal data, ships in several languages, publishes releases or is a monorepo), read the **How to enforce** section. Collect each tool with the rule IDs it checks, and look up each rule's score in `RULES.md`.
2. Choose the set to add:
   - Prefer, in this order: checks built into a tool the project already uses (for example `docker build --check`, a compiler's strict mode), extra rules for a linter it already runs, then new tools.
   - Where the guidelines list alternatives for the same rules (for example kube-linter or Polaris, Trivy or Docker Scout), pick one and say why.
   - Rank by the highest rule score each tool covers. Skip tools that only partly check low-scored (1–5) rules unless they're nearly free.
3. Decide where each check runs: CI on every pull request for anything that must block a merge, a commit hook for fast checks, and editor config for feedback while typing.
4. Write the plan as a table: tool, rules it checks (ID and score, marking partial checks), where it runs, and the files you'll change.

If `--plan-only` was given, stop here and present the plan. If the plan adds more than three tools, or changes when existing CI jobs fail, show it and ask before making changes. Otherwise continue.

## 3. Implement

- **Label every check.** Name each CI step or hook after what it checks and add the rule IDs, for example `name: Dockerfile lint (DOCKER-1, DOCKER-3, DOCKER-6)` or a `# Checks …` comment, so that a failure leads back to the rule.
- **Pin versions.** Pin each tool to an exact version. In GitHub Actions workflows, follow `specific/github-actions/README.md`: read-only `permissions` at the top (`GHA-1`), actions pinned to a full commit SHA with a version comment (`GHA-2`; resolve it with `git ls-remote --tags https://github.com/OWNER/REPO`. If you can't look SHAs up, because there is no shell or no network, pin the exact release tag instead, never write a SHA from memory, and list those actions in the report as a `GHA-2` follow-up), no untrusted input expanded in `run:` (`GHA-3`), and `persist-credentials: false` on checkout. If the project has no Dependabot or Renovate config, add one for the ecosystems you touched, so the pins don't go stale.
- **Run each check once locally** where the tool is available, and fix configuration errors before you finish.
- **Existing violations.** If a new check fails on code that already exists, don't silently disable rules. Fix small numbers of violations, or use the tool's baseline or changed-files mode, or add the check as non-blocking at first. Say which you chose, and why.
- Don't add tools the guidelines don't name. If the user asks for one, add it and say that it isn't part of the guidelines.

## 4. Report

```markdown
## Automated checks added

**Platforms detected:** <list> · **Where:** <files changed>

| Check | Runs in | Rules enforced | Blocking? |
| --- | --- | --- | --- |
| <tool and mode> | <CI job / hook / editor> | `DOCKER-6` (7), `DOCKER-2` (9, partly) | Yes |

### Found on the first run
<violations the new checks reported, and what you did about them>

### Still manual
<the highest-scored rules for these platforms that no tool checks, from the matching checklists in `<root>/checklists/`. They need review instead.>
```

Keep the "Still manual" list to the 5–10 highest-scored rules, and link the full checklist for the rest.
