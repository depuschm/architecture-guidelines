<!-- rule-prefix: PLATFORM -->
# <Platform name>

<!--
Copy this folder to specific/<platform>/ and replace every placeholder, including the rule prefix on line 1
(upper-case and unique, for example GODOT). Reference first: if the platform has an official architecture
guide, adopt it and keep "Key rules" short. Every list item must contain a link to a source that supports it
(checked by scripts/check_citations.py). Every reference entry and key rule starts with its score, 1-10
(see RANKING.md). Write new rules without an ID: `python3 scripts/rank.py fix` assigns IDs, adds new links
to sources.csv for you to score, sorts the lists and adds the legend line. Delete this comment when done.
-->

Scope: what kinds of projects these guidelines apply to, and which versions.

## Adopted references

- `10` [Official architecture guide title](https://example.com/official-guide): what it covers. **Follow it as the baseline.**
- `8` [Official sample or reference app](https://example.com/sample): what it demonstrates.

## Key rules

Only rules the adopted references don't already cover, or choices between options they leave open.

- `8` `PLATFORM-1` **Short imperative rule.** One sentence of explanation. ([Source title](https://example.com/source))

## How to enforce

Tools that check the key rules automatically, in CI, the IDE or a commit hook.

- `7` [Tool name](https://example.com/tool-docs): what it checks. Checks `PLATFORM-1`.

## Tutorials and further reading

- `7` [Complete course or tutorial](https://example.com/course): what you will learn.
