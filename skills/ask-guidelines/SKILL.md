---
name: ask-guidelines
description: Answer questions about what the Architecture Guidelines recommend, such as how to structure something, which rule applies, what the guidelines say about a topic, or which tool can check it. Answers cite the relevant rules by ID, score and source link. Covers general architecture (principles, styles, DDD, APIs, data, operations, security, authentication, testing, releases, repositories, AI systems) and game development, Unity, Godot, Unreal Engine, web front ends, React, Next.js, Vue, Svelte, TypeScript, Node.js, Python, .NET, GraphQL, PostgreSQL, Redis, Kafka, RabbitMQ, Android, Flutter, Docker, Kubernetes, OpenTelemetry, AWS, serverless hosting (Vercel, Netlify, Cloudflare), Terraform and GitHub Actions. Use for architecture advice or best-practice questions that don't need a full codebase review.
argument-hint: "[question]"
---

# Ask the guidelines

Answer the question from the guidelines, not from memory. Every recommendation you give must trace back to a rule or reference in the guideline files.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Useful entry points:

- `<root>/RULES.md`: every rule with its ID, score, level and the tools that check it
- `<root>/general/README.md` and `<root>/specific/README.md`: indexes of the guideline files
- `<root>/checklists/<area>.md`: all rules for one area, sorted by level

## 1. Find the relevant rules

1. Work out the platform (if any) and the topic, such as data ownership, secrets, testing or asset loading.
2. Search `RULES.md` and the guideline files for the topic's terms, for example `grep -rn -i "secret" <root>/general <root>/specific`. Try synonyms if the first search finds nothing.
3. Read the matching section of each guideline file, including its "Adopted references" and "How to enforce" entries, because the rule's sources and tools are there.

Prefer the platform file over the general file when both apply. Mention the general rule too when it adds something.

## 2. Answer

Lead with a direct answer in two or three sentences. Then list the supporting rules, highest score first:

```markdown
- `DOTNET-1` (10, strongly recommended) **Keep secrets out of source.** Use the Secret Manager in development and a vault in production. Source: [Microsoft, Safe storage of app secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets)
```

Then, where they exist:

- **Read next**: the one or two highest-scored adopted references for the topic.
- **Automate it**: tools from the "How to enforce" section that check these rules.

Copy rule IDs, scores and links exactly from the files. Use the score to say how strongly to follow a rule: 9–10 strongly recommended, 6–8 recommended, 1–5 conditional.

## 3. When the guidelines don't cover it

Say plainly that no guideline covers the question. You may add general advice, but label it as your own opinion and don't attach rule IDs to it. Suggest adding a guideline (maintainers can use the `add-guideline` skill in the guidelines repository).
