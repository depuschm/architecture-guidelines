<!-- rule-prefix: TF -->
# Terraform (infrastructure as code)

Scope: managing infrastructure with Terraform or OpenTofu (`tofu` instead of `terraform` on the command line), from single projects to many teams sharing modules. For rules about AWS itself, see [AWS](../aws/README.md); for pipelines that run Terraform, see [GitHub Actions](../github-actions/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Terraform style guide](https://developer.hashicorp.com/terraform/language/style) (HashiCorp): **the baseline** for code style, file layout, version pinning, repository structure, environments, secrets, testing and policy.
- `8` [Module creation: recommended pattern](https://developer.hashicorp.com/terraform/tutorials/modules/pattern-module-creation) (HashiCorp): how to scope modules by encapsulation, privileges and volatility. Read it with [module composition](https://developer.hashicorp.com/terraform/language/modules/develop/composition) and the [standard module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure).
- `8` [Best practices for using Terraform](https://docs.cloud.google.com/docs/terraform/best-practices/general-style-structure) (Google Cloud): style, reusable and root modules, operations, security and testing. Much of it applies to other clouds too.
- `8` [Manage sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data) (HashiCorp): sensitive, ephemeral and write-only values, and how to secure state.
- `8` [HCP Terraform workspace best practices](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/best-practices) (HashiCorp): how to split workspaces, each with one state file, by blast radius, volatility and team ownership.
- `7` [Running Terraform in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform) (HashiCorp): the plan, review and apply cycle in CI.
- `7` [Best practices for using the Terraform AWS Provider](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html) (AWS Prescriptive Guidance): security, backends, code structure and provider versions on AWS.
- `7` [OpenTofu language documentation](https://opentofu.org/docs/language/) (OpenTofu): the OpenTofu counterpart of the Terraform language docs, including features such as [state and plan encryption](https://opentofu.org/docs/language/state/encryption/).

## Key rules

### State and secrets

- `9` `TF-1` **Store state in a remote backend with locking and encryption at rest, restrict who can read it, and never commit state files.** State can contain passwords and keys, and concurrent runs can corrupt it. ([HashiCorp, Remote state](https://developer.hashicorp.com/terraform/language/state/remote), [HashiCorp, State locking](https://developer.hashicorp.com/terraform/language/state/locking), [HashiCorp, Manage sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data), [Google Cloud, Best practices for security](https://docs.cloud.google.com/docs/terraform/best-practices/security))
- `8` `TF-2` **Give Terraform short-lived credentials, such as OIDC from the CI platform or HCP Terraform dynamic provider credentials, instead of static keys. Never put credentials in provider blocks or variables.** ([HashiCorp, Dynamic provider credentials](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials), [Terraform style guide](https://developer.hashicorp.com/terraform/language/style), [Google Cloud, Best practices for operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations), [HashiCorp, Running Terraform in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform))
- `7` `TF-3` **Keep secrets out of state where the provider allows it, with ephemeral values and write-only arguments (Terraform 1.10 and 1.11 or later), and protect saved plan files like state.** With OpenTofu, you can also encrypt state and plan files. ([HashiCorp, Manage sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data), [Google Cloud, Best practices for security](https://docs.cloud.google.com/docs/terraform/best-practices/security), [HashiCorp, Running Terraform in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform), [OpenTofu, State and plan encryption](https://opentofu.org/docs/language/state/encryption/))

### Structure and modules

- `8` `TF-4` **Split infrastructure into separate root modules, each with its own state, by environment, blast radius, rate of change and team ownership.** Keep stateful resources such as databases apart from stateless ones, and keep each state small (Google suggests at most 100 resources). ([HashiCorp, Workspace best practices](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/best-practices), [Google Cloud, Best practices for root modules](https://docs.cloud.google.com/docs/terraform/best-practices/root-modules))
- `7` `TF-5` **Give each environment its own directory, with its own backend, that calls shared modules. Don't use CLI workspaces for environments that need separate credentials or access controls.** ([Terraform style guide](https://developer.hashicorp.com/terraform/language/style), [HashiCorp, Manage workspaces](https://developer.hashicorp.com/terraform/cli/workspaces), [Google Cloud, Best practices for root modules](https://docs.cloud.google.com/docs/terraform/best-practices/root-modules))
- `7` `TF-6` **Rename and move resources with `moved` blocks, and keep old `moved` blocks in shared modules.** Otherwise Terraform destroys the resource and creates a new one. ([HashiCorp, Refactor modules](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring))
- `6` `TF-7` **Keep the module tree flat: compose child modules in the root module and pass their dependencies in as variables.** ([HashiCorp, Module composition](https://developer.hashicorp.com/terraform/language/modules/develop/composition))
- `6` `TF-8` **Write modules that do one thing well at a higher level of abstraction, not thin wrappers around a single resource.** ([HashiCorp, Module creation: recommended pattern](https://developer.hashicorp.com/terraform/tutorials/modules/pattern-module-creation), [HashiCorp, Creating modules](https://developer.hashicorp.com/terraform/language/modules/develop))
- `5` `TF-9` **Protect costly stateful resources, such as databases and storage, with `prevent_destroy`, sparingly.** It doesn't stop destruction when the resource block is removed. ([HashiCorp, lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle))

### Versions and delivery

- `8` `TF-10` **Pin versions: set `required_version`, constrain providers with `~>` in root modules but only by minimum in reusable modules, pin module versions, and commit `.terraform.lock.hcl`.** Review the pins regularly, for example with Dependabot. ([HashiCorp, Version constraints: best practices](https://developer.hashicorp.com/terraform/language/expressions/version-constraints), [HashiCorp, Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock), [Google Cloud, Best practices for operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations))
- `8` `TF-11` **Run Terraform from a pipeline: plan every change, save the plan with `-out`, and apply exactly that plan after review.** ([HashiCorp, Running Terraform in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform), [Google Cloud, Best practices for operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations))
- `6` `TF-12` **Run `terraform fmt -check`, `terraform validate` and TFLint on every change, and test reusable modules with `terraform test`.** ([Terraform style guide](https://developer.hashicorp.com/terraform/language/style), [HashiCorp, Tests](https://developer.hashicorp.com/terraform/language/tests))
- `6` `TF-13` **Check plans against security and organisation policies as code before applying them.** ([Terraform style guide](https://developer.hashicorp.com/terraform/language/style), [HashiCorp, Policy enforcement overview](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement))
- `5` `TF-14` **Detect drift on a schedule, for example with `terraform plan -detailed-exitcode` or HCP Terraform health assessments.** ([HashiCorp, terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [HashiCorp, Health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [`terraform fmt -check`](https://developer.hashicorp.com/terraform/cli/commands/fmt), [`terraform validate`](https://developer.hashicorp.com/terraform/cli/commands/validate) and [`terraform test`](https://developer.hashicorp.com/terraform/cli/commands/test): the built-in checks. `fmt -check` exits non-zero when files aren't formatted, `validate` checks that the configuration is syntactically valid and internally consistent, and `test` runs the module's test files. Checks `TF-12`.
- `6` [TFLint Terraform ruleset](https://github.com/terraform-linters/tflint-ruleset-terraform/blob/main/docs/rules/README.md): its recommended rules require `required_version`, provider version constraints, versions for registry modules and pinned Git module sources. It doesn't check `~>` bounds or the lock file. Partly checks `TF-10`.
- `6` [Checkov Terraform policies](https://www.checkov.io/5.Policy%20Index/terraform.html): misconfiguration checks on HCL or [plan JSON](https://www.checkov.io/7.Scan%20Examples/Terraform%20Plan%20Scanning.html), including module sources without a pinned hash or version tag (`CKV_TF_1`, `CKV_TF_2`) and hard-coded AWS keys in the provider (`CKV_AWS_41`). Checks `TF-13`, and partly `TF-2` and `TF-10`.
- `6` [HCP Terraform policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement): evaluates Sentinel, OPA or Terraform policies on every run, and [health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health) detect drift on a schedule. Checks `TF-13` and `TF-14`.
- `5` [Trivy Terraform scanning](https://trivy.dev/docs/latest/coverage/iac/terraform/): an alternative to Checkov that scans HCL and plans for misconfigurations and secrets. Partly checks `TF-2` and `TF-13`.
- `5` [Dependabot for Terraform](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories#terraform): opens pull requests for new provider and module versions. Partly checks `TF-10`.

## Tutorials and further reading

- `7` [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) (HashiCorp): official hands-on tutorials, from getting started to modules, state, policy and automation.
- `6` [Terraform: Up & Running](https://www.terraformupandrunning.com/) (Yevgeniy Brikman, book): state, modules, testing and team workflows in depth.
- `5` [Terraform Best Practices](https://www.terraform-best-practices.com/) (Anton Babenko): a free community guide to code structure and naming.
