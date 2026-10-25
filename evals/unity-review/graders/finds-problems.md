---
type: llm
weight: 2
---

The project has these planted problems:
(1) a singleton `GameManager.Instance` and scene-wide lookups (`FindObjectOfType`, `FindObjectsOfType`, `GameObject.Find`);
(2) per-frame work and allocations inside `Update` (new lists, LINQ, string concatenation, lookups every frame);
(3) game content loaded with `Resources.Load` from a `Resources` folder;
(4) no assembly definition files and no `.gitignore`.

PASS if the review clearly identifies at least three of these four problems.
FAIL if it identifies two or fewer, or if it reports problems that aren't in the code.
