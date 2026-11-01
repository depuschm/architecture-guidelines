<!-- rule-prefix: GODOT -->
# Godot: testing

Automated tests for Godot projects with GUT or gdUnit4, the design that makes code testable, keeping tests out of exports, and running tests in CI. The engine-independent testing rules are in [Testing and delivery](../../general/testing-delivery.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `6` [GUT documentation](https://gut.readthedocs.io/en/latest/) (GUT, Godot Unit Test): writing tests in GDScript, doubles, stubs and spies, awaiting and simulating frames, memory checks, and the command line.
- `6` [gdUnit4 documentation](https://godot-gdunit-labs.github.io/gdUnit4/latest/) (gdUnit4): tests in GDScript and C#, fluent assertions, mocks and spies, the Scene Runner, orphan node detection, and the command-line tool and GitHub Action for CI.

## Key rules

- `7` `GODOT-14` **Write automated tests with GUT or gdUnit4, and run them headless in CI on every change.** ([GUT, Command line](https://gut.readthedocs.io/en/latest/Command-Line.html), [gdUnit4, Continuous integration](https://godot-gdunit-labs.github.io/gdUnit4/latest/faq/ci/), [Godot, Command line tutorial](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html))
- `7` `GODOT-37` **Unit-test game logic in isolation, in `RefCounted` classes and other scripts that you can create with `new()`, and test whole scenes in integration tests with gdUnit4's Scene Runner or GUT's `simulate()` and input sender, for behaviour that spans frames or depends on input.** Keeping that logic out of nodes is `GODOT-8` in [code architecture](code-architecture.md). ([gdUnit4, Unit testing](https://godot-gdunit-labs.github.io/gdUnit4/latest/testing/unit-testing/), [Integration testing](https://godot-gdunit-labs.github.io/gdUnit4/latest/testing/integration-testing/), [Scene Runner](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/sceneRunner/), [GUT, Simulate](https://gut.readthedocs.io/en/latest/Simulate.html), [Mocking Input](https://gut.readthedocs.io/en/latest/Mocking-Input.html))
- `6` `GODOT-38` **Let the code under test receive its dependencies, as `GODOT-3` describes for scenes, so that tests can replace them with GUT doubles and stubs or gdUnit4 mocks and spies.** GUT's doubles leave out native engine methods by default, and gdUnit4's mocks work only for GDScript, so use a .NET mocking library such as Moq in C#. ([Godot, Scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html), [GUT, Doubles](https://gut.readthedocs.io/en/latest/Doubles.html), [gdUnit4, Mocking](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/mock/))
- `6` `GODOT-39` **Keep tests and the test framework out of release exports: put tests in their own folder, such as `res://test/`, and add it and the framework's addon folder (`addons/gut/*` or `addons/gdunit4/*`) to the exclude filter of every export preset.** gdUnit4 isn't meant for production builds, and exporting with it installed can crash the export. ([gdUnit4, Export failures with the plugin installed](https://godot-gdunit-labs.github.io/gdUnit4/latest/faq/solutions/#export-failures-with-gdunit4-plugin-installed), [GUT, Install](https://gut.readthedocs.io/en/latest/Install.html), [Godot, Exporting projects: resource options](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html#resource-options))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `5` [GUT command line](https://gut.readthedocs.io/en/latest/Command-Line.html): runs the tests outside the editor and returns 1 when any test fails. It can also [export JUnit XML results](https://gut.readthedocs.io/en/latest/Export-Test-Results.html). Checks `GODOT-14`.
- `5` [gdUnit4 command line tool](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd/): runs test suites outside the editor, returns 100 on test failures, and writes HTML and JUnit reports. A [GitHub Action](https://godot-gdunit-labs.github.io/gdUnit4/latest/faq/ci/) wraps it for CI. Checks `GODOT-14`.
