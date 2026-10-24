# Security

Design security in from the start rather than adding it at the end.

## Adopted references

- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/): **our security requirements checklist** for applications.
- [OWASP Top 10](https://owasp.org/Top10/): the most critical web application risks. Use it for awareness, not as a complete checklist.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): concise, practical guidance per topic.
- [OWASP Secure Product Design Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html): secure design principles at the architecture level.
- [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final): practices for a secure development lifecycle.
- [CISA Secure by Design](https://www.cisa.gov/securebydesign): principles for shipping products that are secure by default.
- [NCSC secure design principles](https://www.ncsc.gov.uk/collection/cyber-security-design-principles) (UK National Cyber Security Centre).

## Key rules

- **Threat model early and revisit it as the design changes.** Ask: what are we working on, what can go wrong, what are we going to do about it, and did we do a good enough job? ([Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html))
- **Use STRIDE to enumerate threats per component, data flow and trust boundary.** ([Microsoft, Threat Modeling Tool threats (STRIDE)](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html))
- **Deny by default, enforce least privilege, and check authorisation server-side on every request.** ([OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))
- **Don't grant implicit trust based on network location. Authenticate and authorise every access (zero trust).** ([NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final))
- **Keep secrets out of code and repositories.** Store them in a secrets manager, scope access tightly, and rotate them. ([OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html))
- **Log security-relevant events, and keep secrets and sensitive personal data out of logs by removing, masking, hashing or encrypting them.** ([OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html))
- **Secure service-to-service communication and identity in distributed systems.** ([OWASP Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html))
- **Protect the software supply chain with build provenance and continuous dependency health checks.** ([SLSA](https://slsa.dev/), [OpenSSF Scorecard](https://scorecard.dev/))
- **Ship secure defaults so customers don't have to harden the product themselves.** ([CISA Secure by Design](https://www.cisa.gov/securebydesign))

## Tutorials and further reading

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): see also [AI systems](ai-systems.md).
