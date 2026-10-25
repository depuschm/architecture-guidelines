---
type: llm
weight: 2
---

The project has these planted problems:
(1) the `Game` autoload holds unrelated state (score, player, enemies, inventory, settings) and reaches into the UI by absolute node path;
(2) GDScript without static typing;
(3) long hard-coded node paths such as `get_node("../../Enemies/Goblin")` instead of exported references or unique names;
(4) movement done in `_process` by setting `position`, instead of `_physics_process`;
(5) the save file is decoded with `get_var(true)`, which allows objects, so an edited save could run code.

PASS if the review clearly identifies at least four of these five problems, including (5).
FAIL otherwise, or if it reports problems that aren't in the code.
