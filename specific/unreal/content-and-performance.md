<!-- rule-prefix: UNREAL -->
# Unreal Engine: content and performance

Asset loading, memory, garbage collection, profiling, large worlds, content validation and localization. Materials, shaders and scalability are in [Rendering and shaders](rendering.md), and frame budgets are in [Game development](../gamedev/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `7` [Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine): the Asset Manager, primary and secondary assets, asset bundles, and cooking and chunking.
- `7` [Common Memory and CPU Performance Considerations](https://dev.epicgames.com/documentation/en-us/unreal-engine/common-memory-and-cpu-performance-considerations-in-unreal-engine) (Unreal Engine documentation): **the baseline for gameplay performance.** Garbage collection, object pooling, Tick versus timers and callbacks, asynchronous and parallel work, and shader compilation hitches.
- `6` [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine) (Unreal Engine documentation): the profiling workflow, frame budgets and the profiling tools.

## Key rules

### Loading, memory and profiling

- `8` `UNREAL-10` **Reference assets that aren't always needed with soft references (`TSoftObjectPtr`, `TSoftClassPtr`), and load them asynchronously.** A hard reference loads its target whenever the object that holds it loads, and chains of them can load most of a game at startup. ([Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine), [Asynchronous Asset Loading](https://dev.epicgames.com/documentation/en-us/unreal-engine/asynchronous-asset-loading-in-unreal-engine))
- `8` `UNREAL-11` **Profile early and often on the target hardware, with Unreal Insights.** The editor is no substitute for the device. ([Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine), [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine))
- `6` `UNREAL-12` **Register the content you load on demand, such as levels and data assets, as primary assets with the Asset Manager, and use asset bundles to control which secondary assets load with them.** ([Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine))
- `6` `UNREAL-32` **Keep garbage-collection hitches out of gameplay: pool Actors that are spawned and destroyed often when the CPU budget is tight, and collect garbage manually where a spike is tolerable, such as behind a loading screen.** Collection spikes are worst after many objects have been destroyed. Otherwise rely on the automatic collector, and tune its settings only when profiling shows the need. This applies `GAMEDEV-13`. ([Unreal Engine, Common Memory and CPU Performance Considerations](https://dev.epicgames.com/documentation/en-us/unreal-engine/common-memory-and-cpu-performance-considerations-in-unreal-engine))
- `6` `UNREAL-33` **Find out what an asset pulls into memory with the Reference Viewer and its Size Map, and track memory at run time on each target platform with the Low-Level Memory Tracker and Memory Insights.** The Reference Viewer shows hard and soft references separately, and Memory Insights finds leaks and growth between two points in time, for example across a level transition. ([Unreal Engine, Reference Viewer](https://dev.epicgames.com/documentation/en-us/unreal-engine/reference-viewer-in-unreal-engine), [Low-Level Memory Tracker](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-low-level-memory-tracker-in-unreal-engine), [Memory Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/memory-insights-in-unreal-engine))
- `5` `UNREAL-34` **Build large open worlds with World Partition, which stores the world in one level divided into grid cells and streams the cells by distance, instead of dividing the map into sublevels and streaming them by hand.** ([Unreal Engine, World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine))

### Content validation

- `6` `UNREAL-13` **Turn content rules, such as naming conventions and size or performance budgets, into Data Validation rules, and run the `DataValidation` commandlet in CI.** ([Data Validation](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-validation-in-unreal-engine))

### Localization

- `7` `UNREAL-16` **Keep all user-facing text in `FText`, created from text properties in assets, `LOCTEXT` macros in C++ or String Tables, and build messages with `FText::Format` and its `plural`, `ordinal` and `gender` argument modifiers.** Gather, export, import and compile the text with the Localization Dashboard, and give translators the exported PO files rather than the built-in Translation Editor. This applies `I18N-1`, `I18N-2` and `I18N-3`. ([Unreal Engine, Text Localization](https://dev.epicgames.com/documentation/en-us/unreal-engine/text-localization-in-unreal-engine), [Localization Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/localization-tools-in-unreal-engine), [Localization Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/localization-overview-for-unreal-engine))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Data Validation commandlet](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-validation-in-unreal-engine): `UnrealEditor-Cmd <Project>.uproject -run=DataValidation` runs the project's validation rules over its assets in CI: C++ rules by default, and Blueprint and Python rules once you enable them. The editor also runs them when an asset is saved. Checks `UNREAL-13`.
