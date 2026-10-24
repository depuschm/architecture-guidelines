# AI systems

Architecture guidance for systems that use large language models, agents and machine learning.

## Adopted references

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Anthropic): workflow and agent patterns, and when to use each.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): the main security risks of LLM-based systems.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): governance and risk management for AI systems.
- [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/) (Thoughtworks via martinfowler.com): patterns such as RAG, evals and guardrails.
- [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html): a review checklist for generative AI workloads.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) (Google): engineering practices for ML systems.
- [Model Context Protocol](https://modelcontextprotocol.io/) and [Agent Skills](https://agentskills.io/specification): open standards for connecting agents to tools and for packaging agent know-how.

## Key rules

- **Start with the simplest solution, such as a single model call with retrieval.** Add agentic complexity only when it measurably improves results. ([Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents))
- **Use workflows (predefined code paths) for well-defined tasks, and agents only where the model must decide the steps itself.** ([Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents))
- **Design tools specifically for agents, and put as much effort into the agent interface as you would into a human one: clear, distinct names, focused scope and actionable error messages.** ([Anthropic, Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents), [Building effective agents, appendix 2](https://www.anthropic.com/research/building-effective-agents))
- **Treat context as a finite resource and curate what goes into it.** ([Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents))
- **Build evaluations early and run them on every change to prompts, models or tools.** ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), [Thoughtworks, GenAI patterns: evals](https://martinfowler.com/articles/gen-ai-patterns/))
- **Treat model inputs and outputs as untrusted.** Defend against prompt injection, and limit tool permissions to avoid excessive agency. ([OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/))
- **Budget for the hidden technical debt of ML systems: data dependencies, feedback loops and glue code.** ([Sculley et al., Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html))
- **Don't be afraid to launch without machine learning.** A simple heuristic baseline is a valid first version. ([Google, Rules of ML, rule #1](https://developers.google.com/machine-learning/guides/rules-of-ml))

## Tutorials and further reading

- [Azure Architecture Center: AI and machine learning](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/): reference architectures.
- [Anthropic skills repository](https://github.com/anthropics/skills): example Agent Skills.
