<!-- rule-prefix: GAMEMAKER-PERF -->
# GameMaker: content and performance

Profiling, the VM and YYC outputs, memory and garbage collection, texture and audio groups, rooms and instances, and saving. Batching, surfaces, texture pages and shaders are in [Rendering and shaders](rendering.md), and frame budgets and save-data versioning are in [Game development](../gamedev/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [Best Practices When Programming](https://manual.gamemaker.io/lts/en/Additional_Information/Best_Practices_When_Programming.htm) (GameMaker Manual): local variables, arrays and data structures, collisions, texture swaps and vertex batches, particles and surfaces.
- `7` [How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games) (GameMaker, 2024): texture groups, flushing and prefetching, dynamic textures, blend modes and batching, sound settings, and faster GML.
- `7` [The Debugger](https://manual.gamemaker.io/lts/en/IDE_Tools/The_Debugger.htm) and [The Debug Overlay](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Debugging/The_Debug_Overlay.htm) (GameMaker Manual): breakpoints, the Profiler, memory and frame-time graphs, and an in-game overlay with custom debug views.

## Key rules

### Profiling and compilation

- `7` `GAMEMAKER-PERF-1` **Profile the game on every target device, during development and before and after each optimisation, with the Debugger's Profiler and the Debug Overlay.** The overlay's FPS window shows the frame time against the game speed and the texture swaps and vertex batches, and the overlay also shows memory use and the garbage collector. This applies `GAMEDEV-12` and `GFX-3`. ([GameMaker Manual, The Profiler](https://manual.gamemaker.io/lts/en/IDE_Tools/The_Debugger/The_Profiler.htm), [The Debugger](https://manual.gamemaker.io/lts/en/IDE_Tools/The_Debugger.htm), [The Debug Overlay: FPS](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Debugging/The_Debug_Overlay.htm#fps))
- `6` `GAMEMAKER-PERF-2` **Test and debug on the VM, but build the release of a CPU-heavy game with YYC on the platforms that offer it, measure its performance in that build, and clear the compiler cache before every final build.** YYC compiles GML to native code and can make logic-heavy games two to three times faster, while the Debugger runs your code on the VM. ([GameMaker Manual, Compiling](https://manual.gamemaker.io/lts/en/Introduction/Compiling.htm), [YoYo Compiler](https://manual.gamemaker.io/lts/en/Settings/YoYo_Compiler.htm), [The Debugger](https://manual.gamemaker.io/lts/en/IDE_Tools/The_Debugger.htm))

### Memory and loading

- `7` `GAMEMAKER-PERF-3` **Destroy everything you create at run time that has a destroy function, such as data structures, surfaces and buffers, usually in the Clean Up event, and use arrays and structs rather than DS lists and maps.** These resources aren't garbage-collected, while arrays and structs are. Leave the garbage collector on; turning it off isn't recommended. ([GameMaker Manual, Garbage Collection](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Garbage_Collection/Garbage_Collection.htm), [Data Structures](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Data_Structures/Data_Structures.htm), [Object Events: Clean Up](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Object_Properties/Object_Events.htm), [gc_enable](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Garbage_Collection/gc_enable.htm))
- `7` `GAMEMAKER-PERF-4` **Assign sprites, tile sets and fonts to texture groups by where they're used, such as one group per level and one for the menus, and keep groups that only some rooms need out of memory: make them dynamic, load them with `texturegroup_load()` before they're needed, and unload them afterwards.** Drawing from a dynamic group that isn't loaded loads it on the spot, which can freeze the game for a moment, so turn on explicit mode with `texturegroup_set_mode(true)` to catch it. Dynamic groups aren't supported on HTML5. ([GameMaker Manual, Texture Groups](https://manual.gamemaker.io/lts/en/Settings/Texture_Groups.htm), [Dynamic Textures](https://manual.gamemaker.io/lts/en/Settings/Texture_Information/Dynamic_Textures.htm), [GameMaker, How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games))
- `6` `GAMEMAKER-PERF-5` **Choose each sound's compression by its length and use, and put sounds that only some rooms need in audio groups that you load with `audio_group_load()`.** Keep short sound effects uncompressed, compress long or rarely used ones, and compress and stream music from disk. Every sound in the default audio group, except streamed ones, is loaded into memory when the game starts. ([GameMaker, How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games), [GameMaker Manual, Audio Groups](https://manual.gamemaker.io/lts/en/Settings/Audio_Groups.htm))

### Rooms and instances

- `6` `GAMEMAKER-PERF-6` **Build static scenery from tile layers rather than instances with sprites, and check collisions against the tile map where the level fits a grid.** Tiles have a much lower processing overhead than sprites, and collision functions such as `place_meeting()` accept a tile map. ([GameMaker Manual, Animated Tiles](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Tile_Set_Editors/Animated_Tiles.htm), [Tile Set Editor](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Tile_Sets.htm), [place_meeting](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Movement_And_Collisions/Collisions/place_meeting.htm), [Best Practices When Programming](https://manual.gamemaker.io/lts/en/Additional_Information/Best_Practices_When_Programming.htm))
- `5` `GAMEMAKER-PERF-7` **If you deactivate instances outside the view, do it every few steps or when the camera moves, never every step or in a Draw event, and reactivate persistent instances at least one step before the room changes.** Deactivating every step can itself cost performance, and a persistent instance that is deactivated isn't carried into the next room. ([GameMaker Manual, Deactivating Instances](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Asset_Management/Instances/Deactivating_Instances/Deactivating_Instances.htm))

### Saving

- `7` `GAMEMAKER-PERF-8` **Follow the manual's advice against losing saves: write each save to a new file, check it, then replace the old one, validate a save, for example with a checksum, before loading it, and keep files open only briefly.** Serialise save data with `json_stringify()` and `json_parse()`, the JSON functions the manual recommends for new projects. This applies `GAMEDEV-10` and `GAMEDEV-11`. On HTML5, saves go to the browser's local storage, which may hold only 1 to 5 MB. ([GameMaker Manual (Beta), The File System: preventing data loss](https://manual.gamemaker.io/beta/en/Additional_Information/The_File_System.htm), [GameMaker Manual, The File System](https://manual.gamemaker.io/lts/en/Additional_Information/The_File_System.htm), [Guide To Using JSON](https://manual.gamemaker.io/lts/en/Additional_Information/Guide_To_Using_JSON.htm))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Dynamic texture groups, explicit mode](https://manual.gamemaker.io/lts/en/Settings/Texture_Information/Dynamic_Textures.htm): after `texturegroup_set_mode(true)`, an image from a dynamic texture group that wasn't loaded first isn't drawn, an error goes to the output log, and an optional fallback sprite shows where it happened, so test runs catch implicit loads. Partly checks `GAMEMAKER-PERF-4`.
