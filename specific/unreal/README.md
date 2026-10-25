<!-- rule-prefix: UNREAL -->
# Unreal Engine

Scope: Unreal Engine 5 projects written in C++, Blueprint or both, from single-player games to networked multiplayer titles. Engine-independent game concerns are in [Game development](../gamedev/README.md), and the [general guidelines](../../general/README.md) still apply.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

Epic doesn't publish a single architecture guide. These official pages are the baseline, and the rules below add only the decisions they leave open.

- `9` [Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) (Unreal Engine documentation): **the baseline for gameplay code.** What the game instance, game mode, game state, player state, controllers and pawns are for, and how they relate.
- `9` [Epic C++ Coding Standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine): naming, class layout, formatting and C++ language rules. Mandatory at Epic.
- `8` [Networking Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine): the client-server model, replication, RPCs, network roles and a list of networking tips.
- `8` [Exposing C++ to Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-cplusplus-to-blueprints-visual-scripting-in-unreal-engine): when to use C++ or Blueprint, and how to design a Blueprint-friendly C++ API.
- `7` [Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine): the Asset Manager, primary and secondary assets, asset bundles, and cooking and chunking.
- `7` [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine): Epic's reference project for UE5, with a modular core, game feature plugins, experiences and a customised Gameplay Ability System.
- `7` [Recommended Asset Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects): the prefix scheme Epic uses for assets in its sample projects.
- `7` [Automation Test Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine): unit, feature, smoke, content stress and screenshot tests, and Epic's test design guidelines.
- `6` [Blueprint Best Practices](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-best-practices-in-unreal-engine): Level Blueprints versus Blueprint classes, functions versus macros, and communication between Blueprints.

## Key rules

### Code and gameplay framework

- `9` `UNREAL-1` **Hold UObject references that must keep their target alive in `UPROPERTY` members, preferably `TObjectPtr`, and use `TWeakObjectPtr` for references that must not.** The garbage collector can't see raw pointers, so their targets can be collected and the pointers left dangling. ([Unreal Object Handling](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine), [Object Pointers](https://dev.epicgames.com/documentation/en-us/unreal-engine/object-pointers-in-unreal-engine))
- `8` `UNREAL-2` **Put match rules in the game mode, which exists only on the server, state that all players need in the game state, per-player state in the player state, and anything that must survive a level change in the game instance or its subsystems.** ([Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine), [Game Mode and Game State](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine))
- `7` `UNREAL-3` **Write core systems, high-frequency logic and data-heavy work in C++ base classes, and expose a small API that designers extend in Blueprint subclasses.** Move a Blueprint's logic into C++ when profiling or its complexity calls for it. ([Exposing C++ to Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-cplusplus-to-blueprints-visual-scripting-in-unreal-engine), [Blueprint Best Practices](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-best-practices-in-unreal-engine))
- `7` `UNREAL-4` **Put game-wide services in subsystems (`UGameInstanceSubsystem`, `ULocalPlayerSubsystem`, `UEngineSubsystem` or `UEditorSubsystem`) instead of adding them to a custom game instance or overriding engine classes.** ([Programming Subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine))
- `7` `UNREAL-5` **Split code into modules with explicit dependencies in their `Build.cs` files: keep editor-only code in `Editor` modules, and prefer private dependencies to public ones.** ([Unreal Engine Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules))
- `5` `UNREAL-6` **Use the Gameplay Ability System for games built around many abilities, attributes and status effects, especially multiplayer ones.** It replicates abilities and attributes, and supports prediction. ([Understanding the Gameplay Ability System](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-unreal-engine-gameplay-ability-system))
- `5` `UNREAL-7` **Build optional or frequently changing features as Game Feature plugins, so that unrelated features can't depend on each other by accident.** ([Game Features and Modular Gameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-features-and-modular-gameplay-in-unreal-engine), [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine))

### Multiplayer

- `8` `UNREAL-8` **Keep the server authoritative: clients request actions through Server RPCs, and the server validates them before it changes any state.** ([Networking Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine), [Remote Procedure Calls](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine), [Game development: server authority](../gamedev/README.md))
- `7` `UNREAL-9` **Prefer replicated properties with RepNotify to RPCs, use multicast RPCs sparingly, and make frequently called RPCs unreliable.** ([Networking Overview, networking tips](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine))

### Content and performance

- `8` `UNREAL-10` **Reference assets that aren't always needed with soft references (`TSoftObjectPtr`, `TSoftClassPtr`), and load them asynchronously.** A hard reference loads its target whenever the object that holds it loads, and chains of them can load most of a game at startup. ([Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine), [Asynchronous Asset Loading](https://dev.epicgames.com/documentation/en-us/unreal-engine/asynchronous-asset-loading-in-unreal-engine))
- `8` `UNREAL-11` **Profile early and often on the target hardware, with Unreal Insights.** The editor is no substitute for the device. ([Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine), [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine))
- `6` `UNREAL-12` **Register the content you load on demand, such as levels and data assets, as primary assets with the Asset Manager, and use asset bundles to control which secondary assets load with them.** ([Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine))

### Version control

- `7` `UNREAL-15` **Keep One File Per Actor on (the default with World Partition), so that several people can change actors in the same level at once.** Actor changes are saved to separate files, so the level file doesn't have to be checked out and locked. See [game development: version control](../gamedev/README.md) for choosing Git LFS or Perforce. ([Unreal Engine, One File Per Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine))

### Quality

- `7` `UNREAL-14` **Write automated tests with the Automation Test Framework, use Low-Level Tests for pure unit tests, and run both from the command line in CI.** ([Automation Test Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine), [Run Automation Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/run-automation-tests-in-unreal-engine), [Low-Level Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/low-level-tests-in-unreal-engine))
- `6` `UNREAL-13` **Turn content rules, such as naming conventions and size or performance budgets, into Data Validation rules, and run the `DataValidation` commandlet in CI.** ([Data Validation](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-validation-in-unreal-engine))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Data Validation commandlet](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-validation-in-unreal-engine): `UnrealEditor-Cmd <Project>.uproject -run=DataValidation` runs the project's validation rules over its assets in CI: C++ rules by default, and Blueprint and Python rules once you enable them. The editor also runs them when an asset is saved. Checks `UNREAL-13`.
- `6` [Gauntlet `RunUnreal`](https://dev.epicgames.com/documentation/en-us/unreal-engine/running-gauntlet-tests-in-unreal-engine): the `UE.EditorAutomation` and `UE.TargetAutomation` tests run Automation Test Framework tests in the editor or in a packaged build from a build system, and can resume after a crash. For a simpler setup, [pass `-ExecCmds="Automation RunTest …"`](https://dev.epicgames.com/documentation/en-us/unreal-engine/run-automation-tests-in-unreal-engine) to the editor. Checks `UNREAL-14`.
- `5` [PVS-Studio V1100](https://pvs-studio.com/en/docs/warnings/v1100/): flags pointers to UObject types held in classes that don't derive from `UObject`, where the garbage collector can't see them. It's a commercial analyser that [Unreal Build Tool runs with `-StaticAnalyzer=PVSStudio`](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine). Partly checks `UNREAL-1`.

## Tutorials and further reading

- `6` [Unreal Engine C++ Complete Guide](https://tomlooman.com/unreal-engine-cpp-guide/) (Tom Looman): Unreal's C++ dialect, from pointers, `TObjectPtr` and delegates to the reflection macros, modules and garbage collection.
- `5` [Multiplayer Network Compendium](https://cedric-neukirchen.net/docs/category/multiplayer-network-compendium/) (Cedric Neukirchen): the gameplay framework in multiplayer, replication, RPCs, ownership, relevancy and network roles, explained with examples.
- `5` [GASDocumentation](https://github.com/tranek/GASDocumentation) (Dan Kestranek): an unofficial, in-depth explanation of the Gameplay Ability System with a multiplayer sample project, current with UE 5.3.
