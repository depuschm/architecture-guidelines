<!-- rule-prefix: GAMEMAKER-TEST -->
# GameMaker: testing

Automated tests for GameMaker projects: GML testing libraries, smoke tests of builds with Igor, and Sync Test for rollback multiplayer. GameMaker has no built-in unit-test framework. The engine-independent testing rules are in [Testing and delivery](../../general/testing-delivery.md), and compiling every change in CI is in [Project structure](project-structure.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `7` [Building & Testing via Command Line](https://manual.gamemaker.io/lts/en/Settings/Building_via_Command_Line.htm) (GameMaker Manual): the Igor test command and its `tests.json` file.
- `6` [Guide to GameMaker Testing Library](https://gamemaker.io/en/tutorials/gamemaker-testing-library-tutorial) (GameMaker, 2025): writing suites, sections and tests with GMTL, testing objects over several frames, and simulating input.
- `5` [GameMaker Testing Library documentation](https://github.com/DAndrewBox/GM-Testing-Library/blob/main/Docs/Documentation.md) (DAndrewBox): GMTL's suites, assertions, lifecycle hooks, object helpers and input simulation, for GameMaker 2023.4 and later, including LTS 2026.
- `4` [Crispy](https://bfrymire.github.io/crispy/) (bfrymire): a smaller unit-testing framework in GML, with test runners, suites, cases and test discovery, for GameMaker LTS 2022 and later.

## Key rules

- `6` `GAMEMAKER-TEST-1` **Test the logic in script functions and constructors, and the behaviour of objects over several frames, with a GML testing library such as GMTL, and run the tests every time you run the game in development.** GMTL tests call functions directly, create instances with `create()`, advance frames with `waitFor()`, and simulate keyboard, mouse and gamepad input; by default they run when the game starts and print their results to the output. ([GameMaker, Guide to GameMaker Testing Library](https://gamemaker.io/en/tutorials/gamemaker-testing-library-tutorial), [GMTL documentation](https://github.com/DAndrewBox/GM-Testing-Library/blob/main/Docs/Documentation.md))
- `6` `GAMEMAKER-TEST-2` **Smoke-test every target build automatically with Igor's test command.** Igor builds each project or test listed in a `tests.json` file for the platforms and devices you name, and fails a test when the project doesn't compile within the timeout or crashes before the wait time ends. ([GameMaker Manual, Building & Testing via Command Line](https://manual.gamemaker.io/lts/en/Settings/Building_via_Command_Line.htm#s3))
- `5` `GAMEMAKER-TEST-3` **If you use Rollback Multiplayer, test every change in Sync Test, on Windows, macOS or GX.games, before you test online.** Sync Test runs the game's code twice in each frame, reports synchronisation errors in the output log, and gives remote players random or mock input. ([GameMaker Manual, Rollback System](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Rollback/Rollback_System.htm), [Rollback Multiplayer](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Rollback/Rollback_Multiplayer.htm))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `6` [Igor test command](https://manual.gamemaker.io/lts/en/Settings/Building_via_Command_Line.htm#s3): run from a CI job, it builds and runs the tests in `tests.json` and marks each one as passed or failed. Checks `GAMEMAKER-TEST-2`.
