<!-- rule-prefix: SEC -->
# Security

Design security in from the start rather than adding it at the end.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [OWASP Application Security Verification Standard (ASVS)](https://asvs.owasp.org/): **our security requirements checklist** for applications.
- `9` [OWASP Top 10](https://top10.owasp.org/): the most critical web application risks. Use it for awareness, not as a complete checklist.
- `9` [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): concise, practical guidance per topic.
- `8` [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final): practices for a secure development lifecycle.
- `7` [OWASP Secure Product Design Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html): secure design principles at the architecture level.
- `7` [CISA Secure by Design](https://www.cisa.gov/securebydesign): principles for shipping products that are secure by default.
- `7` [NCSC secure design principles](https://www.ncsc.gov.uk/collection/cyber-security-design-principles) (UK National Cyber Security Centre).

## Key rules

- `10` `SEC-1` **Deny by default, enforce least privilege, and check authorisation server-side on every request.** ([OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))
- `10` `SEC-2` **Keep secrets out of code and repositories.** Store them in a secrets manager, scope access tightly, and rotate them. ([OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html))
- `9` `SEC-3` **Threat model early and revisit it as the design changes.** Ask: what are we working on, what can go wrong, what are we going to do about it, and did we do a good enough job? ([Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html))
- `8` `SEC-4` **Log security-relevant events, and keep secrets and sensitive personal data out of logs by removing, masking, hashing or encrypting them.** ([OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html))
- `8` `SEC-5` **Secure service-to-service communication and identity in distributed systems.** ([OWASP Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html))
- `8` `SEC-6` **Ship secure defaults so customers don't have to harden the product themselves.** ([CISA Secure by Design](https://www.cisa.gov/securebydesign))
- `7` `SEC-7` **Don't grant implicit trust based on network location. Authenticate and authorise every access (zero trust).** ([NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final))
- `7` `SEC-8` **Protect the software supply chain with build provenance and continuous dependency health checks.** ([SLSA](https://slsa.dev/), [OpenSSF Scorecard](https://scorecard.dev/))
- `6` `SEC-9` **Use STRIDE to enumerate threats per component, data flow and trust boundary.** ([Microsoft, Threat Modeling Tool threats (STRIDE)](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [GitHub secret scanning push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection): blocks pushes that contain hardcoded credentials before they reach the repository. Checks `SEC-2`.
- `6` [Gitleaks](https://github.com/gitleaks/gitleaks): detects passwords, API keys and tokens in git repositories and files, as a pre-commit hook or GitHub Action. Checks `SEC-2`.
- `6` [OpenSSF Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md): run as a GitHub Action; they score dependency-update tooling, known vulnerabilities, and signed releases with SLSA provenance. Partly checks `SEC-8`.
- `6` [Dependabot alerts](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts) and [version updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates): alert on vulnerable dependencies and keep them up to date. Partly checks `SEC-8`.
- `6` [GitHub artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations): signed build provenance for your artifacts, verifiable with `gh attestation verify`. Partly checks `SEC-8`.
- `6` [CodeQL, clear-text logging of sensitive data](https://codeql.github.com/codeql-query-help/python/py-clear-text-logging-sensitive-data/) ([JavaScript](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-logging/)): code-scanning queries that flag sensitive data written to logs. Partly checks `SEC-4`.

## Tutorials and further reading

- `9` [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): see also [AI systems](ai-systems.md).
