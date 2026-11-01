# GameMaker

Scope: games made with GameMaker in GameMaker Language (GML), on GameMaker LTS 2026 (2026.0 and the updates planned until early 2028) and its GMS2 runtime, with the VM and YYC outputs. LTS is GameMaker's default release channel and, since LTS 2026.0, the version where YoYo Games focuses development; new features appear first in the Beta channel. YoYo Games [ended the monthly release track](https://gamemaker.io/en/blog/winter-update-2024) after its 2024 releases, and [2024.14](https://gamemaker.io/en/blog/release-2024-14), the last major release before LTS 2026.0, led into it through release candidates, so the rules also hold for 2024.14 unless they name a newer feature. GMRT, the new runtime, is still in beta and isn't covered. Documentation links point to the LTS manual. These guidelines build on [Game development](../gamedev/README.md), [Graphics and GPU rendering](../graphics/README.md), [Mobile games](../mobile-games/README.md) for iOS and Android releases, and the [general guidelines](../../general/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

The GameMaker Manual is the baseline. YoYo Games doesn't publish an architecture guide, so the pages below adopt the manual's pages for their topic and add the choices and pitfalls it leaves to you.

- `9` [GameMaker Manual](https://manual.gamemaker.io/lts/en/Content.htm) (YoYo Games): **the baseline.** The IDE, the asset editors, project settings, GML and the function reference.
- `8` [Best Practices When Programming](https://manual.gamemaker.io/lts/en/Additional_Information/Best_Practices_When_Programming.htm) (GameMaker Manual): coding style, local variables, arrays and data structures, collisions, texture swaps and vertex batches, particles and surfaces.
- `6` [GameMaker LTS 2026.0](https://gamemaker.io/en/blog/lts-2026-release) (GameMaker blog, 2026): what LTS 2026 adds, its release plan to early 2028, and the GMS2 runtime becoming feature complete. The [Spring 2026 update](https://gamemaker.io/en/blog/update-spring-2026) gives the roadmap for GMRT, the Prefab Builder and new languages.

## Guidelines in this folder

- [Project structure](project-structure.md): version control, asset naming, versions and release channels, configurations, command-line builds and sharing code.
- [Code architecture](code-architecture.md): objects, events and instances, global state, functions, structs and types, async events, state machines, UI and multiplayer.
- [Content and performance](content-and-performance.md): profiling, VM and YYC, memory, texture and audio groups, rooms and instances, and saving.
- [Rendering and shaders](rendering.md): vertex batches and GPU state, surfaces, scaling, texture pages and shaders.
- [Testing](testing.md): GML testing libraries, smoke tests with Igor, and Sync Test for rollback multiplayer.

## Tutorials and further reading

- `6` [How to Get Started with GameMaker in 2026](https://gamemaker.io/en/tutorials/get-started-gamemaker-2026) (GameMaker): the official starting point, with 15-minute first games, the project templates in the IDE and recommended tools.
- `6` [Make Your Own Role-Playing Game](https://gamemaker.io/en/tutorials/how-to-make-an-rpg) (GameMaker, 2025): a free video series that builds a complete RPG in GML, from movement and enemies to combat, stats and dialogue, with project files.
- `6` [Quick Start Guide](https://manual.gamemaker.io/lts/en/Quick_Start_Guide/Quick_Start_Guide.htm) (GameMaker Manual): the game loop, sprites, sounds, tile sets, objects and instances, rooms, drawing and sequences.
