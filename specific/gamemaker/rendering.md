<!-- rule-prefix: GAMEMAKER-GFX -->
# GameMaker: rendering and shaders

Vertex batches and texture swaps, GPU state, surfaces, scaling to the display, texture pages and shaders. The engine-independent rendering rules are in [Graphics and GPU rendering](../graphics/README.md). Profiling, texture groups and memory are in [Content and performance](content-and-performance.md), and frame budgets are in [Game development](../gamedev/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

The drawing sections of the GameMaker Manual are the baseline. The rules below add the settings and habits that are easy to miss.

- `7` [How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games) (GameMaker, 2024): texture pages and groups, the depth buffer, blend modes and batching, alpha testing and blending, and layer begin and end scripts.
- `7` [Guide To Using Shaders](https://manual.gamemaker.io/lts/en/Additional_Information/Guide_To_Using_Shaders.htm) and [The Shader Editor](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Shaders.htm) (GameMaker Manual): writing vertex and fragment shaders, uniforms, texture coordinates on texture pages, and which shader languages each target supports.
- `7` [Surfaces](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Drawing/Surfaces/Surfaces.htm) (GameMaker Manual): the application surface, custom surfaces and the rules for using them.
- `5` [The Basics Of Scaling - The Game Camera](https://gamemaker.io/en/blog/the-basics-of-scaling-the-game-view) (GameMaker blog, 2019): fitting the game to any display and aspect ratio with cameras, viewports and the application surface.

## Key rules

### Batches and GPU state

- `7` `GAMEMAKER-GFX-1` **Keep texture swaps and vertex batches low: draw instances that need the same blend mode or shader together, from one controller object or through layer begin and end scripts, instead of letting each instance set and reset the state.** Changing the blend mode or shader, setting uniforms, changing the render target and drawing shapes all break the batch. Turn off *Separate Texture Page* for sprites that don't need it, and watch both counts in the Debug Overlay. This applies `GFX-10`. ([GameMaker Manual, Best Practices When Programming](https://manual.gamemaker.io/lts/en/Additional_Information/Best_Practices_When_Programming.htm), [GameMaker, How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games), [The Debug Overlay: FPS](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Debugging/The_Debug_Overlay.htm#fps))
- `7` `GAMEMAKER-GFX-2` **Undo every GPU state change on every code path before the code that made it ends: `shader_reset()` after `shader_set()`, `surface_reset_target()` after `surface_set_target()`, and the blend mode and other `gpu_set_*` settings back to their defaults.** Otherwise everything drawn afterwards uses the changed state. Feather reports missing resets, for example as `GM2000`, `GM2003` and `GM2005`. ([GameMaker Manual, Feather Messages: GM2000](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Code_Editor_Properties/Feather_Messages.htm#gm2000), [GM2003](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Code_Editor_Properties/Feather_Messages.htm#gm2003), [GM2005](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Code_Editor_Properties/Feather_Messages.htm#gm2005))

### Surfaces and scaling

- `7` `GAMEMAKER-GFX-3` **Treat every surface except the application surface as volatile: check `surface_exists()` before each use and re-create the surface if it's gone, create and draw to surfaces in Draw events, keep them no larger than the view, and free them with `surface_free()`.** A surface lives only in video memory and can be lost when the window loses focus or the app is minimised. In 2D games, call `surface_depth_disable(true)` before creating surfaces that don't need a depth buffer. ([GameMaker Manual, Surfaces](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Drawing/Surfaces/Surfaces.htm), [Best Practices When Programming](https://manual.gamemaker.io/lts/en/Additional_Information/Best_Practices_When_Programming.htm), [GameMaker, How To Optimise Your Games](https://gamemaker.io/en/tutorials/how-to-optimise-your-games))
- `6` `GAMEMAKER-GFX-4` **Fit the game to each display with a camera and viewport, and resize the application surface to match, instead of relying on the Full Scale option, which stretches the image and ignores the aspect ratio. For pixel art, also turn off *Interpolate colours between pixels*, which is on by default, in each platform's Game Options.** Keep the application surface at the display size or smaller, so that the GPU scales it up rather than down. ([GameMaker, The Basics Of Scaling - The Game Camera](https://gamemaker.io/en/blog/the-basics-of-scaling-the-game-view), [GameMaker Manual, application_surface](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Drawing/Surfaces/application_surface.htm), [Windows Game Options](https://manual.gamemaker.io/lts/en/Settings/Game_Options/Windows.htm))

### Texture pages and shaders

- `6` `GAMEMAKER-GFX-5` **Make every image fit on the smallest texture page of any platform you ship to, check the pages with the Preview button in each platform's Game Options, and turn on mipmaps for texture groups that the camera zooms in and out on or that a 3D game uses.** An image larger than the page is scaled down until it fits, so it can look blurred on targets with smaller pages. GPU-compressed texture formats, set per texture group, need YoYo Games' GPU texture compression extension (`GFX-13`). ([GameMaker Manual, Texture Pages](https://manual.gamemaker.io/lts/en/Settings/Texture_Information/Texture_Pages.htm), [Texture Groups](https://manual.gamemaker.io/lts/en/Settings/Texture_Groups.htm), [Texture Compression](https://manual.gamemaker.io/lts/en/Settings/Texture_Information/Texture_Compression.htm))
- `6` `GAMEMAKER-GFX-6` **Write shaders in GLSL ES, the only shader language that works on every target, follow its specification strictly, and check `shader_is_compiled()` at start-up before you use any shader that isn't simple GLSL ES.** Look up uniforms once, in the Create event, and remember that texture coordinates in a shader refer to the whole texture page, so pass the sprite's area from `sprite_get_uvs()`. ([GameMaker Manual, The Shader Editor](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Shaders.htm), [shader_is_compiled](https://manual.gamemaker.io/lts/en/GameMaker_Language/GML_Reference/Asset_Management/Shaders/shader_is_compiled.htm), [Guide To Using Shaders](https://manual.gamemaker.io/lts/en/Additional_Information/Guide_To_Using_Shaders.htm))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Feather messages](https://manual.gamemaker.io/lts/en/The_Asset_Editors/Code_Editor_Properties/Feather_Messages.htm): the code editor reports code paths that leave a changed state behind, such as the blend mode (`GM2000`), the shader (`GM2003`), the render target (`GM2005`, `GM2046`), pushed GPU state (`GM2035`, `GM2042`) and other `gpu_set_*` settings (`GM2048` to `GM2056`). Checks `GAMEMAKER-GFX-2`.
