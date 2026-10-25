<!-- rule-prefix: REPO -->
# Repositories and monorepos

How to split code into repositories, structure a monorepo, assign ownership of code, and protect the branch that everyone integrates into. Integrating into trunk at least daily (`TEST-3`) and automated tests for dependency rules (`TEST-4`) are in [Testing and delivery](testing-delivery.md); team boundaries and Conway's law are in [Principles](principles.md); release branches and tags are in [Versioning and releases](releases.md). For workflow files on GitHub, also follow [GitHub Actions](../specific/github-actions/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [Software Engineering at Google, chapter 16: Version Control and Branch Management](https://abseil.io/resources/swe-book/html/ch16.html): a single source of truth, the One-Version Rule, why to avoid long-lived branches, release branches, and monorepos.
- `8` [Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html) (Martin Fowler): mainline, healthy branch, integration and release patterns, and how Git-flow, GitHub Flow and trunk-based development combine them.
- `8` [Trunk-based development](https://dora.dev/capabilities/trunk-based-development/) (DORA): the research-backed practices (three or fewer active branches, merging into trunk at least daily, no code freezes), common pitfalls, and how to measure them.
- `7` [Why Google Stores Billions of Lines of Code in a Single Repository](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/) (Potvin and Levenberg, *Communications of the ACM*, 2016): the benefits and costs of a monorepo at very large scale, including the tooling it needs.
- `6` [monorepo.tools](https://monorepo.tools/) (Nx): what a monorepo is and isn't, the costs of many separate repositories, and a comparison of monorepo tools. Written by a tool vendor.

## Key rules

### Repository layout

- `7` `REPO-1` **Keep one version of each dependency across the code you build together (the One-Version Rule), whatever the repository layout.** Teams adding a dependency on an internal library or third-party package shouldn't have to choose a version; several versions lead to diamond dependencies and wasted effort. ([Software Engineering at Google, The "One-Version" Rule](https://abseil.io/resources/swe-book/html/ch16.html#the_quotation_markone_versionquotation), [Monorepos](https://abseil.io/resources/swe-book/html/ch16.html#monorepos))
- `7` `REPO-2` **In a monorepo, make each project a package with declared dependencies and a public entry point, and don't import another project's internal files.** If you're writing `../` to reach into another package, depend on the package instead, and check the allowed dependencies between projects in CI, as `TEST-4` asks. ([monorepo.tools, What is a monorepo?](https://monorepo.tools/#what-is-a-monorepo), [Turborepo, Structuring a repository](https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository), [Nx, Enforce module boundaries](https://nx.dev/docs/features/enforce-module-boundaries))
- `6` `REPO-3` **Choose between one repository and several on purpose, and record the decision in an ADR: a monorepo suits projects that change together and share code, but needs build tooling that scales with it.** Separate repositories are easier to scale and give teams autonomy, but sharing code and changing several projects at once then need published versions and coordinated upgrades. ([Software Engineering at Google, Monorepos](https://abseil.io/resources/swe-book/html/ch16.html#monorepos), [Potvin and Levenberg, Why Google Stores Billions of Lines of Code in a Single Repository](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/), [monorepo.tools, The polyrepo tax](https://monorepo.tools/#polyrepo-concept))
- `6` `REPO-4` **In a monorepo, let CI build and test only the projects a change affects, with a tool that knows the project graph, and cache task results.** ([Nx, Run only tasks affected by a PR](https://nx.dev/docs/features/ci-features/affected), [Turborepo, `run --affected`](https://turborepo.dev/docs/reference/run#--affected))

### Branches, ownership and review

- `8` `REPO-5` **Protect the default branch: merge only through pull requests with passing status checks, block force pushes and deletion, and don't let administrators bypass the rules.** Require at least one approving review when the project has more than one active maintainer. ([GitHub, About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitHub, About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [GitLab, Branch rules](https://docs.gitlab.com/user/project/repository/branches/branch_rules/), [OpenSSF Scorecard, Branch-Protection](https://github.com/ossf/scorecard/blob/main/docs/checks.md#branch-protection))
- `6` `REPO-6` **Give every part of the repository an owner in a `CODEOWNERS` file, including the file itself, and require review from code owners on the default branch.** `GHA-9` asks the same for workflow files. ([GitHub, About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [GitLab, Code Owners](https://docs.gitlab.com/user/project/codeowners/))
- `6` `REPO-7` **Keep changes small and respond to review requests within one business day, so that branches stay short-lived.** A slow, heavy review process makes developers batch up changes, which undermines trunk-based development. ([Google, Speed of code reviews](https://google.github.io/eng-practices/review/reviewer/speed.html), [Google, Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html), [DORA, Trunk-based development](https://dora.dev/capabilities/trunk-based-development/))
- `5` `REPO-8` **When many people merge into one busy branch, use a merge queue, so that each change is tested together with the changes merged ahead of it before it lands.** ([GitHub, Managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue), [GitLab, Merge trains](https://docs.gitlab.com/ci/pipelines/merge_trains/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Nx `enforce-module-boundaries` rule](https://nx.dev/docs/kb/enforce-module-boundaries) (JavaScript and TypeScript): a lint rule that checks imports between projects against tag-based constraints, and flags circular dependencies between projects. Partly checks `REPO-2`.
- `6` [OpenSSF Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md#branch-protection): Branch-Protection scores the default and release branches' protection settings, and [Code-Review](https://github.com/ossf/scorecard/blob/main/docs/checks.md#code-review) checks that recent changes were reviewed before they merged; the highest Branch-Protection tiers also require review from code owners. Checks `REPO-5`, and partly `REPO-6`.
- `6` [dependency-cruiser](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md#group-matching) (JavaScript and TypeScript): `forbidden` rules with group matching stop one package from importing another's internals, and fail CI on violations. Partly checks `REPO-2`.
- `6` [Import Linter independence contracts](https://import-linter.readthedocs.io/en/stable/contract_types/independence/) (Python): fail when modules that should be independent import each other, even indirectly. Partly checks `REPO-2`.
- `5` [Syncpack `lint`](https://syncpack.dev/command/lint/) (JavaScript): fails CI when packages in a monorepo use different versions of the same dependency. [Sherif](https://github.com/QuiiBz/sherif/blob/main/README.md)'s `multiple-dependency-versions` rule does the same. Partly checks `REPO-1`.
- `4` [`turbo boundaries`](https://turborepo.dev/docs/reference/boundaries) (experimental): reports imports of files outside a package's directory and of packages it doesn't declare as dependencies, and checks tag rules. Partly checks `REPO-2`.

## Tutorials and further reading

- `6` [Crafting your repository](https://turborepo.dev/docs/crafting-your-repository) (Turborepo): a guide, meant to be read in order, to structuring a JavaScript monorepo, managing dependencies, creating internal packages, and setting up tasks, caching and CI.
- `6` [Workspace](https://pnpm.io/workspaces) (pnpm): setting up a multi-package workspace, and the `workspace:` protocol that links internal packages from the repository instead of a registry.
- `5` [Improving monorepo performance](https://docs.gitlab.com/user/project/repository/monorepos/) (GitLab): why large repositories get slow in Git, and how to keep clones and CI fast.
