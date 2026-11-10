<!-- rule-prefix: GODOT -->
# Godot: project structure

Folders and file names, file formats, version control, addons, export presets and per-platform settings. Version control for large binary assets in any engine is in [Game development](../gamedev/README.md), and keeping secrets out of repositories is in [Security](../../general/security.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `7` [Project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) and [Version control systems](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html) (Godot docs): folder layout, file naming, and which files to commit or ignore.
- `7` [Exporting projects](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html) (Godot docs): export presets and templates, which files an export includes, where the export configuration and credentials are kept, and exporting from the command line.

## Key rules

### Version control

- `9` `GODOT-1` **Commit the `.import` files next to your assets and the `.uid` files next to your scripts and shaders, and ignore the `.godot/` folder.** Generate the `.gitignore` and `.gitattributes` from the project manager or *Project > Version Control*. This is how Godot projects apply `GAMEDEV-22`. ([Godot, Version control systems](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html), [Import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html), [UID changes coming to Godot 4.4](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/))
- `7` `GODOT-31` **Save scenes and resources in the text formats, `.tscn` and `.tres`, rather than the binary `.scn` and `.res`, so that they stay readable and easy to manage in version control.** Exports still convert them to binary, because the `editor/export/convert_text_resources_to_binary` project setting is on by default. ([Godot, TSCN file format](https://docs.godotengine.org/en/stable/engine_details/file_formats/tscn.html), [ProjectSettings, convert_text_resources_to_binary](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-editor-export-convert-text-resources-to-binary))
- `6` `GODOT-32` **If you store large assets in Git LFS (`GAMEDEV-15`), set it up before the first commit, starting from the example `.gitattributes` in Godot's version control documentation, which also tracks Godot's binary formats such as `.scn`, `.res`, `.mesh` and `.lmbake`.** Files committed before LFS was set up stay in normal Git history until you re-add or migrate them. ([Godot, Version control systems: Git LFS](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html#git-lfs))

### Folders, files and addons

- `6` `GODOT-2` **Use snake_case for file and folder names (C# scripts excepted), and keep third-party code in `addons/`.** Exported projects use a case-sensitive file system, so a case mismatch can break the game only after export. ([Godot, Project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html))
- `6` `GODOT-33` **Keep scripts and assets close to the scenes that use them, and move, rename or delete files only in Godot's FileSystem dock, so that references to them don't break.** If you move a script or shader outside Godot, move its `.uid` file with it and re-save the scenes that use it. ([Godot, Project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html), [File system: drawbacks](https://docs.godotengine.org/en/stable/tutorials/scripting/filesystem.html#drawbacks), [UID changes coming to Godot 4.4](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/))
- `5` `GODOT-34` **Install third-party addons from the Asset Library or a tagged stable release, not from a repository's latest commit, and keep each one in its own `addons/<name>/` folder.** An editor plugin's `plugin.cfg` records its version. Package your own systems that several projects share the same way. ([Godot, Installing plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/installing_plugins.html), [Making plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html))

### Export and platform settings

- `7` `GODOT-35` **Commit `export_presets.cfg`, keep signing keys, passwords and encryption keys out of the repository, and automate release builds with `--export-release`.** Godot keeps those secrets in `.godot/export_credentials.cfg`, which is ignored with the rest of `.godot/`, and CI can pass them in environment variables such as `GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD`. This applies `SEC-2`. ([Godot, Exporting projects: configuration files](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html#configuration-files), [exporting from the command line](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html#exporting-from-the-command-line), [Exporting for Android: environment variables](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html#environment-variables))
- `5` `GODOT-36` **Put platform- and build-specific project settings in feature-tag overrides, such as `.mobile`, `.web`, `.debug` or a custom tag set in an export preset, and read those settings with `ProjectSettings.get_setting_with_override()`.** `get_setting()` ignores the overrides, and custom feature tags apply only to exported builds, not when you run the project from the editor. ([Godot, Feature tags](https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html))
