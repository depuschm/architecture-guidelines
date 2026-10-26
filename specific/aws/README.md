<!-- rule-prefix: AWS -->
# AWS

Scope: workloads on Amazon Web Services.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html): **the baseline, used for every workload review.** Its [pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) each have a detailed whitepaper:
  - `8` [Security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
  - `8` [Reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
  - `7` [Operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)
  - `7` [Performance efficiency](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
  - `7` [Cost optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
  - `5` [Sustainability](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- `9` [AWS Builders' Library](https://builder.aws.com/learn/topics/builders-library): how Amazon designs and operates its own services.
- `8` [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) (whitepaper).
- `7` [AWS Architecture Center](https://aws.amazon.com/architecture/): reference architectures and diagrams.
- `7` [AWS Prescriptive Guidance: cloud design patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/introduction.html).
- `7` [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html).
- `6` Well-Architected lenses for specific workloads, for example the [Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) and the [Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html).

## Key rules

- `9` `AWS-2` **Use a multi-account structure with AWS Organizations, separating workloads and environments into their own accounts.** ([Organizing your AWS environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html))
- `8` `AWS-1` **Give people access through IAM Identity Center federation and workloads through IAM roles, so that both use temporary credentials instead of IAM users with long-term access keys.** Least privilege (`SEC-1`) and short-lived workload credentials (`SEC-14`) are in [general/security.md](../../general/security.md). ([IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html))
- `8` `AWS-3` **Design for Availability Zone failure, and understand AWS fault isolation boundaries.** ([AWS fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html), [Static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones))
- `8` `AWS-4` **Define AWS infrastructure with the CDK or CloudFormation, and follow the CDK best practices for structuring apps, constructs and stacks.** The general rule on infrastructure as code is `OPS-14` in [general/operations-reliability.md](../../general/operations-reliability.md). ([AWS CDK best practices](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html))
- `8` `AWS-6` **Choose a disaster recovery strategy from your RTO and RPO: backup and restore, pilot light, warm standby, or multi-site active/active.** ([Disaster recovery of workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html))
- `7` `AWS-5` **Review each workload against the Well-Architected Framework early in design and before go-live, and again after significant architecture changes.** ([AWS Well-Architected, The review process](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html))
- `7` `AWS-7` **Set organisation-wide guardrails with service control policies.** ([AWS Organizations, SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html))
- `6` `AWS-8` **In Lambda functions, separate the handler from the core logic, and reuse the execution environment for clients and connections.** ([AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), handler best practices for [C#](https://docs.aws.amazon.com/lambda/latest/dg/csharp-handler.html) and [Python](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html))
- `6` `AWS-9` **Tag resources consistently for ownership, cost allocation and automation.** ([Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html))
- `3` `AWS-10` **Contain the blast radius of failures with cell-based or shuffle-sharded designs where scale demands it.** Cells add complexity and cost, so reserve them for systems that are too big or too critical to fail. ([Reducing the scope of impact with cell-based architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html), [Workload isolation using shuffle-sharding](https://builder.aws.com/content/3F06NpJ8YeoIGP8VHTw4n81pFn8/workload-isolation-using-shuffle-sharding))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html): validates IAM policies against policy grammar and AWS best practices, and [also validates service control policies](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html). Partly checks `AWS-1` and `AWS-7`.
- `7` [Security Hub, AWS Foundational Security Best Practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html): continuous checks such as no full `*` administrative policies, access-key rotation, no root access keys, and multiple Availability Zones for Auto Scaling groups, load balancers, RDS and Lambda. The [Resource Tagging standard](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-tagging.html) finds untagged resources. Partly checks `AWS-1`, `AWS-3` and `AWS-9`.
- `6` [cdk-nag rules](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md): checks CDK apps before deployment, for example for wildcard IAM permissions or RDS without multi-AZ ([AWS blog](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/)). Partly checks `AWS-1`, `AWS-3` and `AWS-4`.
- `6` [AWS Config, required-tags rule](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html): checks that resources carry the tags you specify, and [CloudFormation drift detection](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html) finds stacks changed outside infrastructure as code. Checks `AWS-9`, and partly `AWS-4`.
- `6` [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html): assesses whether an application meets its RTO and RPO targets, including during an Availability Zone disruption, and can [assess daily](https://docs.aws.amazon.com/resilience-hub/latest/userguide/scheduled-assessment.html). Partly checks `AWS-6` and `AWS-3`.

## Tutorials and further reading

- `6` [AWS multi-Region fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/).
- `5` [Serverless Land](https://serverlessland.com/): serverless patterns and workshops.
- `4` [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/): hands-on labs, now mainly for cost optimisation (Cloud Intelligence Dashboards, CUR queries) and the Well-Architected Tool.
- `4` [AWS Skill Builder](https://skillbuilder.aws/): official training.
