# Unreal Engine

Scope: Unreal Engine 5 projects written in C++, Blueprint or both, from single-player games to networked multiplayer titles. Engine-independent game concerns are in [Game development](../gamedev/README.md), GPU rendering is in [Graphics and GPU rendering](../graphics/README.md), and the [general guidelines](../../general/README.md) still apply.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

Epic doesn't publish one architecture guide for the whole engine. Instead, each page in this folder adopts the official Unreal Engine documentation for its topic as the baseline, and its rules add only the decisions that documentation leaves open. Lyra shows how Epic puts these pieces together in one project.

- `7` [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine): Epic's reference project for UE5, with a modular core, game feature plugins, experiences and a customised Gameplay Ability System.

## Guidelines in this folder

- [Project structure](project-structure.md): modules and plugins, asset naming, version control, and builds and iteration.
- [Code architecture](code-architecture.md): the gameplay framework, C++ and Blueprint, Tick, data and save games, input, UI and multiplayer.
- [Content and performance](content-and-performance.md): asset loading, memory, garbage collection, profiling, large worlds, content validation and localization.
- [Rendering and shaders](rendering.md): PSO precaching, the shared Derived Data Cache, materials, Nanite and Lumen, and device profiles.
- [Testing](testing.md): the Automation Test Framework and its test types, test design, and tests of packaged builds with Gauntlet.

## Tutorials and further reading

- `6` [Unreal Engine C++ Complete Guide](https://tomlooman.com/unreal-engine-cpp-guide/) (Tom Looman): Unreal's C++ dialect, from pointers, `TObjectPtr` and delegates to the reflection macros, modules and garbage collection.
- `5` [Multiplayer Network Compendium](https://cedric-neukirchen.net/docs/category/multiplayer-network-compendium/) (Cedric Neukirchen): the gameplay framework in multiplayer, replication, RPCs, ownership, relevancy and network roles, explained with examples.
- `5` [GASDocumentation](https://github.com/tranek/GASDocumentation) (Dan Kestranek): an unofficial, in-depth explanation of the Gameplay Ability System with a multiplayer sample project, current with UE 5.3.
