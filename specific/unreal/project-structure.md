<!-- rule-prefix: UNREAL -->
# Unreal Engine: project structure

Modules and plugins, asset naming, version control, and builds and iteration.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [Unreal Engine Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules) (Unreal Engine documentation): **the baseline for code structure.** Creating modules, their `Build.cs` dependencies, and the `Public` and `Private` folders.
- `7` [Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine) (Unreal Engine documentation): plugin anatomy, code and content in plugins, and which plugins and modules may depend on which.
- `7` [Recommended Asset Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects): the prefix scheme Epic uses for assets in its sample projects.
- `7` [Using Perforce as Source Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine) (Unreal Engine documentation): setting up a server, the typemap, the ignore file and workspaces, and connecting the editor.

## Key rules

### Modules and plugins

- `7` `UNREAL-5` **Split code into modules with explicit dependencies in their `Build.cs` files: keep editor-only code in `Editor` modules, and prefer private dependencies to public ones.** ([Unreal Engine Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules))
- `5` `UNREAL-7` **Build optional or frequently changing features as Game Feature plugins, so that unrelated features can't depend on each other by accident.** ([Game Features and Modular Gameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-features-and-modular-gameplay-in-unreal-engine), [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine))

### Assets and naming

- `6` `UNREAL-35` **Agree on an asset naming convention early in development, starting from Epic's `[AssetTypePrefix]_[AssetName]_[Descriptor]_[OptionalVariantLetterOrNumber]` scheme, and keep each person's experiments in their own Developers folder, which no asset outside it may reference.** References into a Developers folder can make cooking fail, so also add the folder to *Directories to never cook*. Turn the naming convention into a Data Validation rule (`UNREAL-13`). ([Unreal Engine, Recommended Asset Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects), [Developers Folder](https://dev.epicgames.com/documentation/en-us/unreal-engine/developers-folder-in-unreal-engine))
- `5` `UNREAL-36` **After moving or renaming assets, fix up the redirectors they leave behind, in the Content Browser or with the `ResavePackages` commandlet and `-fixupredirects`, and submit the resaved packages.** A redirector lets packages that aren't loaded find the moved asset, but stale redirectors stop you from deleting the asset or creating a new one with the old name. ([Unreal Engine, Asset Redirectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-redirectors-in-unreal-engine))

### Version control

- `7` `UNREAL-37` **Start from the `UnrealEngine.gitignore` template in github/gitignore, which ignores `Binaries/`, `Intermediate/`, `Saved/` and `DerivedDataCache/`, or, with Perforce, from Epic's example `.p4ignore`.** The engine and Unreal Build Tool regenerate these folders, and this is how Unreal projects apply `GAMEDEV-22`. To give people who don't compile an editor build, see `UNREAL-39`. ([github/gitignore, UnrealEngine.gitignore](https://github.com/github/gitignore/blob/main/UnrealEngine.gitignore), [Unreal Engine, Directory Structure](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-directory-structure), [Using Perforce as Source Control: P4 Ignore](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine#p4ignore))
- `7` `UNREAL-38` **Connect the editor to revision control, and turn on its automatic checkout or checkout prompt on modification, so that assets are checked out, and with that locked, before anyone changes them.** The editor supports Perforce out of the box. With Git, use an editor plugin that supports Git LFS locks, such as Anchorpoint. This applies `GAMEDEV-16`. ([Unreal Engine, Source Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/source-control-in-unreal-engine), [Using Anchorpoint as Source Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-anchorpoint-as-source-control-for-unreal-engine))
- `7` `UNREAL-15` **Keep One File Per Actor on (the default with World Partition), so that several people can change actors in the same level at once.** Actor changes are saved to separate files, so the level file doesn't have to be checked out and locked. See [game development: version control](../gamedev/README.md) for choosing Git LFS or Perforce. ([Unreal Engine, One File Per Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine))

### Builds and iteration

- `5` `UNREAL-39` **Script CI builds, cooks and tests with BuildGraph, and give artists and designers the editor binaries that CI builds, for example through Unreal Game Sync with Perforce, so that they don't have to compile.** Epic uses BuildGraph for its own games' pipelines, and Unreal Game Sync can sync a compressed editor build made by CI. ([Unreal Engine, BuildGraph](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine), [Unreal Game Sync](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine))
- `5` `UNREAL-40` **Iterate on C++ with Live Coding, which is on by default and is significantly faster and more flexible than Hot Reload, and keep Object Reinstancing on so that structural changes reach existing objects.** Live Coding works in the editor, in Play In Editor and in desktop builds attached to the editor, but not on consoles or mobile devices. ([Unreal Engine, Live Coding](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-live-coding-to-recompile-unreal-engine-applications-at-runtime))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `8` [Unreal Build Tool, module dependencies](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules): a module can include headers only from the modules listed in its `Build.cs` dependency lists, and headers in another module's `Private` folder aren't available to it, so code that uses an undeclared module fails to build. Partly checks `UNREAL-5`.

