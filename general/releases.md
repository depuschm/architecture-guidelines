<!-- rule-prefix: REL -->
# Versioning and releases

How to number, build, tag, document and publish releases of libraries, services and apps, and how to retire what they offer. Compatibility rules for network APIs are in [API design](api-design.md) (`API-2`); keeping software deployable, feature toggles and trunk-based integration are in [Testing and delivery](testing-delivery.md); build provenance and signing are in [Security](security.md) (`SEC-8`).

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [Semantic Versioning 2.0.0](https://semver.org/): the versioning scheme for software with a public API that others depend on, including its FAQ on deprecation and mistaken releases.
- `7` [Release Engineering](https://sre.google/sre-book/release-engineering/) (Google, *Site Reliability Engineering*): self-service, automated releases, hermetic builds, release branches and cherry-picks.
- `7` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/): a convention for changelogs written for people, with a fixed set of change types and an Unreleased section.
- `7` [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): a commit message format that tools can turn into version numbers and changelogs.
- `6` [Calendar Versioning](https://calver.org/): date-based version schemes, with case studies and guidance on when to choose them over SemVer.

## Key rules

### Version numbers

- `8` `REL-1` **Version libraries, SDKs and other packages that others depend on with Semantic Versioning, and declare what their public API is.** A change that breaks the public API needs a new major version; for network APIs, see `API-2` in [API design](api-design.md). ([Semantic Versioning](https://semver.org/#semantic-versioning-specification-semver))
- `6` `REL-2` **Release 1.0.0 as soon as others use the software in production or depend on its API; stay on 0.y.z only while the API is still unstable.** ([SemVer FAQ, When to release 1.0.0](https://semver.org/#how-do-i-know-when-to-release-100))
- `5` `REL-3` **Consider calendar versioning for applications and products that release on a schedule, have a large or shifting scope, or serve users who shouldn't need to know whether a change is breaking.** ([CalVer, When to use CalVer?](https://calver.org/#when-to-use-calver))

### Building and publishing

- `9` `REL-4` **Never change a published release: its version, tag and artifacts stay as they are, and every fix ships as a new version.** Protect release tags against being moved or deleted, for example with immutable releases. ([Semantic Versioning](https://semver.org/#semantic-versioning-specification-semver), [npm, Unpublish policy](https://docs.npmjs.com/policies/unpublish/), [GitHub, Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases))
- `7` `REL-5` **Build releases with an automated, hermetic build, so that building the same commit again gives the same result, and stamp every artifact with the commit and build it came from.** Add build provenance as `SEC-8` asks. ([Google SRE, Release Engineering](https://sre.google/sre-book/release-engineering/), [Reproducible Builds, Definitions](https://reproducible-builds.org/docs/definition/))
- `7` `REL-6` **Release from trunk. If you must maintain older versions, cut a release branch from trunk, fix bugs on trunk first and cherry-pick the fixes into the branch, and never merge the branch back.** ([Trunk Based Development, Branch for release](https://trunkbaseddevelopment.com/branch-for-release/), [Google SRE, Release Engineering](https://sre.google/sre-book/release-engineering/))
- `6` `REL-7` **Automate version bumps, changelogs, tags and publishing with a release tool that reads the commit history or change files, such as Release Please, semantic-release or Changesets.** Changesets suits monorepos with many packages: contributors describe each change in a file in the pull request. ([Release Please](https://github.com/googleapis/release-please), [semantic-release](https://semantic-release.org/), [Changesets, Why Changesets](https://changesets.dev/guide/why))
- `5` `REL-8` **If releases are derived from commits, write commit messages, or the titles of squash-merged pull requests, in the Conventional Commits format.** `fix:` maps to a patch, `feat:` to a minor version, and `!` or a `BREAKING CHANGE:` footer to a major version. ([Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/))

### Changelogs and deprecation

- `7` `REL-9` **Deprecate before you remove: mark the feature deprecated in a minor release, with a warning in the code and docs that says what to use instead and when it goes away, and remove it only in a later major release.** For HTTP APIs, announce it with the `Deprecation` and `Sunset` response headers. ([SemVer FAQ, Deprecating functionality](https://semver.org/#how-should-i-handle-deprecating-functionality), [PEP 387, Making incompatible changes](https://peps.python.org/pep-0387/#making-incompatible-changes), [RFC 9745, Deprecation header](https://www.rfc-editor.org/rfc/rfc9745), [RFC 8594, Sunset header](https://www.rfc-editor.org/rfc/rfc8594))
- `6` `REL-10` **Keep a changelog or release notes written for users: one entry per version with its date, newest first, with changes grouped as Added, Changed, Deprecated, Removed, Fixed and Security.** Don't publish a raw commit log; if you generate notes, group the changes, for example by pull request labels. ([Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [GitHub, Automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes))
- `6` `REL-11` **If a release breaks users by mistake, publish a new version that restores compatibility and mark the bad one as yanked or deprecated, instead of replacing it.** ([SemVer FAQ, Accidental breaking change](https://semver.org/#what-do-i-do-if-i-accidentally-release-a-backward-incompatible-change-as-a-minor-version), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [npm, Unpublish policy](https://docs.npmjs.com/policies/unpublish/))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases): once enabled, the tag and assets of a published release can't be changed, and the tag can't be deleted while the release exists. [Tag rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) also restrict who can delete or rename tags. Checks `REL-4`.
- `6` [commitlint](https://commitlint.js.org/guides/ci-setup): lints commit messages against Conventional Commits in CI, or in a `commit-msg` hook. Checks `REL-8`.
- `6` [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) (Rust): fails CI when a crate's API changes need a bigger version bump than the one planned. Partly checks `REL-1`.
- `5` [action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request): a GitHub Action that checks pull request titles against Conventional Commits, for repositories that squash-merge. Checks `REL-8`.
- `5` [Changesets, blocking check](https://changesets.dev/guide/automating#blocking): `changeset status --since main` fails CI when changed packages have no changeset, the file that becomes their changelog entry. Partly checks `REL-10`.
- `5` [API Extractor API report](https://api-extractor.com/pages/overview/demo_api_report/) (TypeScript): fails the CI build when the public API signature changes and the committed `.api.md` report wasn't updated, so every API change shows up in review. Partly checks `REL-1`.

## Tutorials and further reading

- `7` [Software Engineering at Google, chapter 21: Dependency Management](https://abseil.io/resources/swe-book/html/ch21.html): why SemVer is only an estimate of compatibility, and what that means for consumers and producers of versions.
