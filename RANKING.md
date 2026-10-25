# Ranking criteria

Every source and every key rule in this repository has a score from 1 to 10. Scores decide the order of each list (highest first). They group entries into three levels, and they give reviews a severity hint.

## Levels

The level names follow the conventions of well-known guideline collections. Android's [architecture recommendations](https://developer.android.com/topic/architecture/recommendations) use *strongly recommended*, *recommended* and *optional*. Flutter's [recommendations](https://docs.flutter.dev/app-architecture/recommendations) use *strongly recommend*, *recommend* and *conditional*.

| Score | Sources | Key rules |
| --- | --- | --- |
| 9–10 | **Start here**: read these first | **Strongly recommended**: follow unless you have a documented reason not to |
| 6–8 | **Recommended**: read when working on the topic | **Recommended**: follow in most projects |
| 1–5 | **Further reading**: for depth or special cases | **Conditional**: follow when the situation calls for it |

## Scoring sources

Judge each source on five criteria:

1. **Authority**: is it the official source, a standard, or the work of the person who defined the concept?
2. **Coverage**: does it cover the whole topic, or one detail of it?
3. **Currency**: is it maintained and up to date for current versions?
4. **Access**: is the full content freely available online?
5. **Actionability**: does it give concrete guidance that changes decisions?

Then pick the score whose description fits best:

| Score | The source is… | Examples |
| --- | --- | --- |
| 10 | The definitive, official, current guide for a whole topic, which this repository adopts as the baseline | Android *Guide to app architecture*, OWASP ASVS, the C4 model |
| 9 | An essential primary source: a core standard, or the defining work on a concept, broad and current | RFC 9110, *The Twelve-Factor App*, the Google SRE book |
| 8 | A highly authoritative source on an important sub-topic | an official documentation page that backs a key rule, a defining article by the originator of a pattern |
| 7 | Authoritative but narrower or less current | official documentation for one feature, a widely used reference implementation, a respected book that isn't freely available |
| 6 | Good supporting material that overlaps with higher-ranked sources | a clear explanation, a worked example, a useful template |
| 5 | Useful in specific contexts, or a secondary explanation of something covered better elsewhere | a tool's home page, a community guide |
| 4 | Narrow, tool-specific or community material with limited scope | |
| 3 | Dated or only partly relevant | an article that predates current versions |
| 1–2 | Kept for completeness only: archived, superseded or hard to access | |

A reference entry (in "Adopted references", "Sample projects", "Tutorials and further reading" or the reading list) shows the score of its **first link**.

## Scoring key rules

Judge each rule on four criteria:

1. **Impact if ignored**: does breaking it cause incidents, security exposure, data loss or blocked change, or only friction?
2. **Breadth**: does it apply to almost every project, or only in some situations?
3. **Consensus**: do several authoritative sources agree, or does an official source mark it as strongly recommended?
4. **Cost to fix later**: is it cheap to adopt now and expensive to retrofit?

| Score | The rule… |
| --- | --- |
| 10 | Prevents severe problems (security breaches, data loss, outages), applies to almost every system, and has universal consensus |
| 9 | Is a strong default for nearly every project, and official sources mark it as strongly recommended or as a MUST |
| 8 | Is important for most projects: ignoring it causes significant problems that are costly to reverse |
| 7 | Is recommended for most projects, with a clear benefit at modest cost |
| 6 | Improves quality, but ignoring it is easy to recover from |
| 5 | Is valuable in common but not universal situations, for example at a certain scale, team size or domain complexity |
| 3–4 | Applies only in specific circumstances |
| 1–2 | Is niche |

Within a topic subsection, rules are sorted by score. Rules with the same score keep their written order.

## How scores are used

- **Ordering**: every list of ranked entries is sorted by score, highest first.
- **Overview**: [SOURCES.md](SOURCES.md) lists every source in one place, grouped by level.
- **Reviews**: the [`architecture-review`](skills/architecture-review/SKILL.md) skill uses rule scores as a severity hint. Breaking a 9–10 rule is usually *High*, 6–8 *Medium* and 1–5 *Low*, adjusted for the actual impact.

## Calibration

Scores are judgements, so they are checked with blind second opinions. On 2026-10-25, an independent reviewer scored a stratified sample of 50 rules and 50 sources against this file, without seeing the existing scores:

- 90% of rule scores and 92% of source scores were within one point of each other.
- Rules scored 8 were systematically about one point higher than the second opinion. All 53 rules at 8 were re-checked against the difference between 8 ("costly to reverse, for most projects") and 7 ("clear benefit at modest cost"). Twenty-two were lowered.
- The few items two or more points apart were re-scored after reviewing both reasons.

Repeat the exercise after large additions: sample entries across files and score bands, have someone score them blind, and re-check any band where the difference is systematic.

## Changing a score

- **Sources**: edit the `score` column in [sources.csv](sources.csv).
- **Key rules**: edit the number at the start of the rule.

Then run `python3 scripts/rank.py fix`. It updates the scores shown in the guideline files, re-sorts the lists and regenerates SOURCES.md. `python3 scripts/rank.py check` (also run in CI) fails if anything is unscored, unsorted or out of sync.

Scores are judgements. When you change one, explain why in the pull request, citing the criteria above.
