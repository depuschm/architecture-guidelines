<!-- rule-prefix: GODOT -->
# Godot: code architecture

How to structure scenes, nodes and scripts so that the game stays easy to change: scene design and communication, scripting languages and style, input and UI layout, multiplayer, and threads. Engine-independent patterns, such as components, fixed time steps and authoritative servers, are in [Game development](../gamedev/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) (Godot docs): formatting, naming conventions and code order.
- `7` [Static typing in GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html) (Godot docs): typed variables and functions, and the warnings that help you keep code typed.
- `7` [High-level multiplayer](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html) (Godot docs): peers and connections, RPCs with their transfer modes and channels, authentication, and secure multiplayer design.
- `7` [Optimization using Servers](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html) (Godot docs): bypassing the scene tree and driving the rendering, physics and audio servers directly through RIDs, for tens of thousands of objects once other optimisations are exhausted.

## Key rules

### Scenes and nodes

- `8` `GODOT-3` **Design scenes to work on their own: keep what a scene needs inside it, and let the parent supply any outside dependency.** The parent can connect to the scene's signals or set its properties, Callables and node references. ([Godot, Scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html))
- `7` `GODOT-4` **Let parents call methods on and set properties of their children, and let children report what happened through signals.** Siblings communicate through a common ancestor. Name signals with past-tense verbs, such as `item_collected`. ([Godot, Scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html), [Using signals](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html))
- `7` `GODOT-5` **Use autoloads only for broad-scoped systems that manage their own data, such as a quest or dialogue system.** Share helper functions with `static func` in a `class_name` script, and share data with a custom Resource. ([Godot, Autoloads versus regular nodes](https://docs.godotengine.org/en/stable/tutorials/best_practices/autoloads_versus_regular_nodes.html))
- `6` `GODOT-6` **Reference other nodes through `@export` properties or scene-unique names (`%Name`), not long hard-coded node paths.** These references keep working when nodes move in the scene tree. ([Godot interfaces](https://docs.godotengine.org/en/stable/tutorials/best_practices/godot_interfaces.html), [Scene unique nodes](https://docs.godotengine.org/en/stable/tutorials/scripting/scene_unique_nodes.html))
- `5` `GODOT-7` **Make game-specific concepts scenes, and use named script classes for reusable tools shared across projects.** ([Godot, When to use scenes versus scripts](https://docs.godotengine.org/en/stable/tutorials/best_practices/scenes_versus_scripts.html))
- `5` `GODOT-8` **Use `RefCounted` or `Resource` classes instead of nodes for data and logic that don't need to be in the scene tree.** ([Godot, When and how to avoid using nodes for everything](https://docs.godotengine.org/en/stable/tutorials/best_practices/node_alternatives.html))

### Scripts

- `7` `GODOT-21` **Choose the scripting languages early: GDScript suits most game code, C# suits teams that already know it, as long as you don't ship to the web, and C++ through GDExtension suits performance-critical algorithms.** You can mix them in one project. Godot 4 can't export C# projects to the web, its C# support on Android and iOS is experimental, and C# code can pause for garbage collection. ([Godot, Scripting languages](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_languages.html), [C# basics](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html), [CPU optimization: languages](https://docs.godotengine.org/en/stable/tutorials/performance/cpu_optimization.html#languages), [About godot-cpp](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html))
- `7` `GODOT-9` **Use static typing throughout, and set the `untyped_declaration` warning to Error so that untyped declarations stop a script from compiling.** Typed code catches more errors before it runs, and it runs faster. ([Godot, Static typing in GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html), [GDScript warning system](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html))
- `7` `GODOT-11` **Move objects and run game logic in `_physics_process`, and turn on physics interpolation so that motion stays smooth at any frame rate.** Use `_process` only for work that must follow the rendered frame rate. ([Godot, Using physics interpolation](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/using_physics_interpolation.html), [Godot notifications](https://docs.godotengine.org/en/stable/tutorials/best_practices/godot_notifications.html), [game development: fixed time steps](../gamedev/README.md))
- `6` `GODOT-10` **Follow the GDScript style guide, including its code order.** Consistency within the team matters more than any single convention. ([Godot, GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html))

### Input and UI

- `7` `GODOT-22` **Read player input through actions defined in the Input Map, not specific keys or buttons, and handle gameplay input events in `_unhandled_input()` rather than `_input()`, so that UI controls receive them first.** One action can map to several keys and gamepad buttons, and you can build runtime rebinding on top of the Input Map (`GAMEDEV-18`). ([Godot, Using InputEvent](https://docs.godotengine.org/en/stable/tutorials/inputs/inputevent.html), [InputMap](https://docs.godotengine.org/en/stable/classes/class_inputmap.html))
- `6` `GODOT-23` **Set the base window size, stretch mode and stretch aspect at the start, following the docs' recommended settings for your kind of game, and lay out UI with anchors and Container nodes so that it adapts to every resolution and aspect ratio.** Games that aren't pixel art usually take the `canvas_items` stretch mode and the `expand` aspect, the default for projects created in Godot 4.7 and later; pixel-art games take `viewport` with integer scaling. ([Godot, Multiple resolutions: common use case scenarios](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html#common-use-case-scenarios), [Using Containers](https://docs.godotengine.org/en/stable/tutorials/ui/gui_containers.html))

### Multiplayer and threads

- `7` `GODOT-24` **In multiplayer games, replicate spawned scenes with `MultiplayerSpawner` and properties with `MultiplayerSynchronizer`, keep the server the multiplayer authority over gameplay state, and give each player authority only over a child node that sends their input.** Validate the arguments of every RPC that clients may call (`any_peer`) before applying them, using `multiplayer.get_remote_sender_id()` to know who sent it. This applies `GAMEDEV-5`. ([Godot, High-level multiplayer: secure multiplayer design](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html#secure-multiplayer-design), [MultiplayerSpawner](https://docs.godotengine.org/en/stable/classes/class_multiplayerspawner.html), [MultiplayerSynchronizer](https://docs.godotengine.org/en/stable/classes/class_multiplayersynchronizer.html), [Multiplayer in Godot 4.0: Scene Replication](https://godotengine.org/article/multiplayer-in-godot-4-0-scene-replication/))
- `6` `GODOT-25` **Don't change the active scene tree from another thread: build or load nodes outside the tree in the worker thread and add them on the main thread with `call_deferred()`, don't load the same resource from several threads at once, and protect data that threads share with a `Mutex`.** Check which engine classes a thread may use first; the rendering and physics servers are thread-safe only after you turn on their threading project settings. ([Godot, Thread-safe APIs](https://docs.godotengine.org/en/stable/tutorials/performance/thread_safe_apis.html), [Using multiple threads](https://docs.godotengine.org/en/stable/tutorials/performance/using_multiple_threads.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [GDScript warning system](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html): set [`untyped_declaration`](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-debug-gdscript-warnings-untyped-declaration) to Error in Project Settings, and scripts with untyped variables, parameters or return types no longer compile. Checks `GODOT-9`.
- `5` [gdlint](https://github.com/Scony/godot-gdscript-toolkit/wiki/3.-Linter) and [gdformat](https://github.com/Scony/godot-gdscript-toolkit/blob/master/README.md) (gdtoolkit): gdlint checks names against the style guide's conventions and the order of class definitions, and `gdformat --check` fails when a file would be reformatted. Both exit with a non-zero code, so they work in CI or a pre-commit hook. Partly checks `GODOT-10`.

## Tutorials and further reading

- `6` [Make a Finite State Machine in Godot 4](https://www.gdquest.com/tutorial/godot/design-patterns/finite-state-machine/) (GDQuest): when a state machine helps, and how to build one with a single state variable or with one node per state, with the trade-offs of each.
