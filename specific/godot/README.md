<!-- rule-prefix: GODOT -->
# Godot

Scope: games and apps built with Godot 4, mainly in GDScript. Documentation links point to the current stable release. These guidelines build on the [engine-independent game development guidelines](../gamedev/README.md) and the [general guidelines](../../general/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

The Godot documentation has an official best practices section. **Follow it as the baseline.** The rules below add only points that are easy to miss and choices the documentation leaves open.

- `10` [Best practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html) (Godot docs): **the baseline.** Scene organization, scenes versus scripts, autoloads versus regular nodes, interfaces, notifications, data and logic preferences, project organization and version control.
- `8` [GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) (Godot docs): formatting, naming conventions and code order.
- `7` [Static typing in GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html) (Godot docs): typed variables and functions, and the warnings that help you keep code typed.
- `7` [Project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) and [Version control systems](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html) (Godot docs): folder layout, file naming, and which files to commit or ignore.
- `7` [General optimization tips](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html) (Godot docs): how to measure performance, find the bottleneck and optimise it, including CPU versus GPU bottlenecks.

## Key rules

### Project and version control

- `9` `GODOT-1` **Commit the `.import` files next to your assets and the `.uid` files next to your scripts and shaders, and ignore the `.godot/` folder.** Generate the `.gitignore` and `.gitattributes` from the project manager or *Project > Version Control*. ([Godot, Version control systems](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html), [Import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html), [UID changes coming to Godot 4.4](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/))
- `6` `GODOT-2` **Use snake_case for file and folder names (C# scripts excepted), and keep third-party code in `addons/`.** Exported projects use a case-sensitive file system, so a case mismatch can break the game only after export. ([Godot, Project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html))

### Scenes and nodes

- `8` `GODOT-3` **Design scenes to work on their own: keep what a scene needs inside it, and let the parent supply any outside dependency.** The parent can connect to the scene's signals or set its properties, Callables and node references. ([Godot, Scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html))
- `7` `GODOT-4` **Let parents call methods on and set properties of their children, and let children report what happened through signals.** Siblings communicate through a common ancestor. Name signals with past-tense verbs, such as `item_collected`. ([Godot, Scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html), [Using signals](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html))
- `7` `GODOT-5` **Use autoloads only for broad-scoped systems that manage their own data, such as a quest or dialogue system.** Share helper functions with `static func` in a `class_name` script, and share data with a custom Resource. ([Godot, Autoloads versus regular nodes](https://docs.godotengine.org/en/stable/tutorials/best_practices/autoloads_versus_regular_nodes.html))
- `6` `GODOT-6` **Reference other nodes through `@export` properties or scene-unique names (`%Name`), not long hard-coded node paths.** These references keep working when nodes move in the scene tree. ([Godot interfaces](https://docs.godotengine.org/en/stable/tutorials/best_practices/godot_interfaces.html), [Scene unique nodes](https://docs.godotengine.org/en/stable/tutorials/scripting/scene_unique_nodes.html))
- `5` `GODOT-7` **Make game-specific concepts scenes, and use named script classes for reusable tools shared across projects.** ([Godot, When to use scenes versus scripts](https://docs.godotengine.org/en/stable/tutorials/best_practices/scenes_versus_scripts.html))
- `5` `GODOT-8` **Use `RefCounted` or `Resource` classes instead of nodes for data and logic that don't need to be in the scene tree.** ([Godot, When and how to avoid using nodes for everything](https://docs.godotengine.org/en/stable/tutorials/best_practices/node_alternatives.html))

### Scripts

- `7` `GODOT-9` **Use static typing throughout, and set the `untyped_declaration` warning to Error so that untyped declarations stop a script from compiling.** Typed code catches more errors before it runs, and it runs faster. ([Godot, Static typing in GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html), [GDScript warning system](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html))
- `7` `GODOT-11` **Move objects and run game logic in `_physics_process`, and turn on physics interpolation so that motion stays smooth at any frame rate.** Use `_process` only for work that must follow the rendered frame rate. ([Godot, Using physics interpolation](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/using_physics_interpolation.html), [Godot notifications](https://docs.godotengine.org/en/stable/tutorials/best_practices/godot_notifications.html), [game development: fixed time steps](../gamedev/README.md))
- `6` `GODOT-10` **Follow the GDScript style guide, including its code order.** Consistency within the team matters more than any single convention. ([Godot, GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html))

### Data and saving

- `7` `GODOT-12` **Model designer-edited game data as custom Resource classes saved as `.tres` files.** A loaded resource is one cached instance that every user shares, so set `resource_local_to_scene` or `duplicate()` it before changing it per instance. ([Godot, Resources](https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html), [Resource.resource_local_to_scene](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource-property-resource-local-to-scene), [Godot interfaces](https://docs.godotengine.org/en/stable/tutorials/best_practices/godot_interfaces.html))
- `7` `GODOT-13` **Write saves and settings to `user://`, and don't decode objects (`allow_objects`) from files that players can edit or share.** `res://` is usually read-only in an exported game, and decoded objects can run code. ([Godot, File paths in Godot projects](https://docs.godotengine.org/en/stable/tutorials/io/data_paths.html), [Saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html), [FileAccess.get_var](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess-method-get-var), [game development: save data](../gamedev/README.md))

### Localization

- `7` `GODOT-15` **Localize with Godot's translation system: add CSV or gettext PO translations under *Project Settings > Localization*, look up text with `tr()` and `tr_n()` or a Control's automatic translation, fill named placeholders with `String.format()`, and switch languages with `TranslationServer.set_locale()`.** This applies `I18N-1`, `I18N-2` and `I18N-3`. Turn on pseudolocalization in the advanced Project Settings, under *Internationalization*, to find untranslated and overflowing text (`I18N-14`). ([Godot, Internationalizing games](https://docs.godotengine.org/en/stable/tutorials/i18n/internationalizing_games.html), [Localization using gettext](https://docs.godotengine.org/en/stable/tutorials/i18n/localization_using_gettext.html), [Pseudolocalization](https://docs.godotengine.org/en/stable/tutorials/i18n/pseudolocalization.html), [TranslationServer](https://docs.godotengine.org/en/stable/classes/class_translationserver.html))

### Testing

- `7` `GODOT-14` **Write automated tests with GUT or gdUnit4, and run them headless in CI on every change.** ([GUT, Command line](https://gut.readthedocs.io/en/latest/Command-Line.html), [gdUnit4, Continuous integration](https://godot-gdunit-labs.github.io/gdUnit4/latest/faq/ci/), [Godot, Command line tutorial](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [GDScript warning system](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html): set [`untyped_declaration`](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-debug-gdscript-warnings-untyped-declaration) to Error in Project Settings, and scripts with untyped variables, parameters or return types no longer compile. Checks `GODOT-9`.
- `5` [gdlint](https://github.com/Scony/godot-gdscript-toolkit/wiki/3.-Linter) and [gdformat](https://github.com/Scony/godot-gdscript-toolkit/blob/master/README.md) (gdtoolkit): gdlint checks names against the style guide's conventions and the order of class definitions, and `gdformat --check` fails when a file would be reformatted. Both exit with a non-zero code, so they work in CI or a pre-commit hook. Partly checks `GODOT-10`.
- `5` [GUT command line](https://gut.readthedocs.io/en/latest/Command-Line.html): runs the tests outside the editor and returns 1 when any test fails. It can also [export JUnit XML results](https://gut.readthedocs.io/en/latest/Export-Test-Results.html). Checks `GODOT-14`.
- `5` [gdUnit4 command line tool](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd/): runs test suites outside the editor, returns 100 on test failures, and writes HTML and JUnit reports. A [GitHub Action](https://godot-gdunit-labs.github.io/gdUnit4/latest/faq/ci/) wraps it for CI. Checks `GODOT-14`.

## Tutorials and further reading

- `7` [Step by step](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html) (Godot docs): the official introduction to nodes, scenes, scripting and signals.
- `7` [Your first 2D game](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/index.html) and [Your first 3D game](https://docs.godotengine.org/en/stable/getting_started/first_3d_game/index.html) (Godot docs): complete step-by-step projects.
