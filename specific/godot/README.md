# Godot

Scope: games and apps built with Godot 4, mainly in GDScript. Documentation links point to the current stable release. These guidelines build on the [engine-independent game development guidelines](../gamedev/README.md) and the [general guidelines](../../general/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

The Godot documentation has an official best practices section. **Follow it as the baseline.** The files below add only points that are easy to miss and choices the documentation leaves open.

- `10` [Best practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html) (Godot docs): **the baseline.** Scene organization, scenes versus scripts, autoloads versus regular nodes, interfaces, notifications, data and logic preferences, project organization and version control.

## Guidelines in this folder

- [Project structure](project-structure.md): folders and file formats, version control, addons, export presets and per-platform settings.
- [Code architecture](code-architecture.md): scenes and nodes, scripting languages and style, input and UI layout, multiplayer and threads.
- [Content and performance](content-and-performance.md): profiling, loading and freeing, asset import, data and saving, and localization.
- [Rendering and shaders](rendering.md): renderers, pipeline compilation, materials and shaders, MultiMesh and level of detail.
- [Testing](testing.md): GUT and gdUnit4, testable code, keeping tests out of exports, and CI.

## Sample projects

- `6` [Godot demo projects](https://github.com/godotengine/godot-demo-projects) (Godot Foundation): official demos for each Godot version, including networking, multiple resolutions, threaded loading and the servers API.

## Tutorials and further reading

- `7` [Step by step](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html) (Godot docs): the official introduction to nodes, scenes, scripting and signals.
- `7` [Your first 2D game](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/index.html) and [Your first 3D game](https://docs.godotengine.org/en/stable/getting_started/first_3d_game/index.html) (Godot docs): complete step-by-step projects.
