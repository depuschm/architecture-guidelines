# Skill evals

Test cases for the plugin's skills, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Each case is a realistic prompt plus graders. Every case runs with the plugin and without it, so the results show what the skills add.

| Case | Checks |
| --- | --- |
| `ask-guidelines-secrets` | A .NET secrets question is answered with real rule IDs (`DOTNET-1`, `SEC-2`) and their source links, and no invented IDs |
| `unity-review` | A small Unity project with planted problems (singleton, per-frame lookups and allocations, `Resources.Load`, no assembly definitions or `.gitignore`) is reviewed. The review finds the problems and cites Unity rule IDs and Unity sources |
| `nextjs-review` | A small Next.js app with planted problems (an unauthorized Server Action, a secret behind `NEXT_PUBLIC_`, a whole database row passed to a Client Component, `'use client'` on the root layout, plain `<img>` tags) is reviewed, citing `NEXTJS` rule IDs and Next.js sources |
| `godot-review` | A small Godot project with planted problems (an autoload that owns everything, untyped GDScript, long node paths, movement in `_process`, saves decoded with `allow_objects`) is reviewed, citing `GODOT` rule IDs and Godot sources |
| `enforce-node-docker` | A Node.js service with a Dockerfile and an unpinned workflow gets automated checks for both in CI, and the reply names the rule IDs each check enforces |
| `adr-postgres` | A decision is recorded as a MADR file in `docs/decisions/0001-*.md`, with considered options and downsides |
| `c4-container` | A system description becomes a Mermaid C4 container diagram with a database, an external system, technology on every relationship, and listed assumptions. Plain Claude scores almost as well here, so this case mainly guards against regressions |
| `no-trigger-unrelated` | An unrelated coding request doesn't fire any of the plugin's skills |

## Run them

From the repository root:

```bash
claude plugin eval . --scaffold --allow-tools Write Edit
```

- `--scaffold` runs each case's `fixture.sh`, which creates its fixture project.
- `--allow-tools Write Edit` lets the ADR case write its file and the enforce case change CI configuration.
- Add `--runs 1 --ablation none` for a quick, cheaper check while iterating.

Every run is a real model call that counts against your usage. A full run with three runs per case and both arms costs a few dollars at list prices.

In CI, the **Skill evals** workflow runs the suite when started by hand from the Actions tab. It needs an `ANTHROPIC_API_KEY` repository secret.

## Maintenance

- `ask-guidelines-secrets/graders/no-invented-ids.md` encodes the valid ID ranges for `DOTNET` and `SEC`. Update it when rules are added to those files.
- When a case fails, run it alone with `--case <name> --runs 1 --ablation none --keep-temp` and read the kept trace.
