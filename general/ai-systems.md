<!-- rule-prefix: AI -->
# AI systems

Architecture guidance for systems that use large language models, agents and machine learning.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Anthropic): workflow and agent patterns, and when to use each.
- `9` [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): the main security risks of LLM-based systems.
- `7` [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): governance and risk management for AI systems.
- `7` [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/) (Thoughtworks via martinfowler.com): patterns such as RAG, evals and guardrails.
- `7` [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html): a review checklist for generative AI workloads.
- `7` [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) (Google): engineering practices for ML systems.
- `7` [Model Context Protocol](https://modelcontextprotocol.io/) and [Agent Skills](https://agentskills.io/specification): open standards for connecting agents to tools and for packaging agent know-how.

## Key rules

- `9` `AI-1` **Treat model inputs and outputs as untrusted.** Defend against prompt injection, and limit tool permissions to avoid excessive agency. ([OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/))
- `7` `AI-2` **Start with the simplest solution, such as a single model call with retrieval.** Add agentic complexity only when it measurably improves results. ([Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents))
- `7` `AI-3` **Build evaluations early and run them on every change to prompts, models or tools.** ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), [Thoughtworks, GenAI patterns: evals](https://martinfowler.com/articles/gen-ai-patterns/))
- `7` `AI-4` **Use workflows (predefined code paths) for well-defined tasks, and agents only where the model must decide the steps itself.** ([Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents))
- `7` `AI-5` **Design tools specifically for agents, and put as much effort into the agent interface as you would into a human one: clear, distinct names, focused scope and actionable error messages.** ([Anthropic, Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents), [Building effective agents, appendix 2](https://www.anthropic.com/research/building-effective-agents))
- `6` `AI-6` **Treat context as a finite resource and curate what goes into it.** ([Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents))
- `5` `AI-7` **Budget for the hidden technical debt of ML systems: data dependencies, feedback loops and glue code.** ([Sculley et al., Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html))
- `5` `AI-8` **Don't be afraid to launch without machine learning.** A simple heuristic baseline is a valid first version. ([Google, Rules of ML, rule #1](https://developers.google.com/machine-learning/guides/rules-of-ml))

## Tutorials and further reading

- `6` [Azure Architecture Center: AI and machine learning](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/): reference architectures.
- `5` [Anthropic skills repository](https://github.com/anthropics/skills): example Agent Skills.
