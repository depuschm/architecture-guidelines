<!-- rule-prefix: UNITY-STRUCT -->
# Unity: project structure

Folders, assemblies, packages and version control.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `8` [Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project) (Unity): **follow it for folder layout and naming.**
- `8` [Introduction to assemblies in Unity](https://docs.unity3d.com/Manual/assembly-definitions-intro.html) and [Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html) (Unity Manual).
- `7` [Version control](https://docs.unity3d.com/Manual/VersionControl.html) (Unity Manual).

## Key rules

### Folders and naming

- `7` `UNITY-STRUCT-1` **Agree on one folder structure and naming convention, write it down, and keep your own assets separate from third-party assets.** ([Unity, Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project))
- `6` `UNITY-STRUCT-2` **Know Unity's reserved folder names (`Editor`, `Resources`, `StreamingAssets`, `Plugins`, …) and use them only for their purpose.** ([Unity Manual, Special folder names](https://docs.unity3d.com/Manual/SpecialFolders.html))
- `6` `UNITY-STRUCT-3` **Agree on a team C# style guide, starting from Unity's example and adapting it. Apply it consistently, and enforce formatting with an EditorConfig file.** ([C# style guide e-book (Unity 6 edition)](https://unity.com/resources/c-sharp-style-guide-unity-6), [Unity, Naming and code style tips](https://unity.com/how-to/naming-and-code-style-tips-c-scripting-unity))

### Assemblies and packages

- `8` `UNITY-STRUCT-4` **Split code into assemblies with Assembly Definition files once the project grows.** This cuts recompilation time. A custom assembly can only use the assemblies it references, and cyclic references aren't allowed, which makes dependency direction explicit. ([Unity Manual, Introduction to assemblies](https://docs.unity3d.com/Manual/assembly-definitions-intro.html), [Referencing assemblies](https://docs.unity3d.com/Manual/assembly-definitions-referencing.html))
- `7` `UNITY-STRUCT-5` **Mirror the architecture in assemblies, for example `Game.Core` (no engine-specific dependencies where practical), `Game.Gameplay`, `Game.UI`, `Game.Editor` and `*.Tests`, so that wrong-way references fail to compile.** ([Unity Manual, Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html), [general: point dependencies inwards](../../general/architecture-styles.md))
- `4` `UNITY-STRUCT-6` **Move systems that several projects share into custom UPM packages that follow the standard package layout.** ([Unity Manual, Creating custom packages](https://docs.unity3d.com/Manual/CustomPackages.html), [Package layout](https://docs.unity3d.com/Manual/cus-layout.html))

### Version control

- `10` `UNITY-STRUCT-7` **Keep `.meta` files visible and committed, and keep asset serialization on Force Text, so that assets diff and merge.** Both are the defaults. Don't change them. ([Unity Manual, Version control settings](https://docs.unity3d.com/Manual/class-VersionControlSettings.html), [Editor settings: Asset Serialization](https://docs.unity3d.com/Manual/class-EditorManager.html))
- `9` `UNITY-STRUCT-8` **Start from the community Unity `.gitignore` so that generated folders such as `Library/` and `Temp/` are never committed.** ([github/gitignore, Unity.gitignore](https://github.com/github/gitignore/blob/main/Unity.gitignore))
- `6` `UNITY-STRUCT-9` **Configure UnityYAMLMerge (Smart Merge) as the merge tool for scenes and prefabs.** ([Unity Manual, Smart Merge](https://docs.unity3d.com/Manual/SmartMerge.html))

### Iteration speed

- `5` `UNITY-STRUCT-10` **Enter Play mode without domain reload for faster iteration.** This is the default and Unity's recommendation from Unity 6.6. In 6.0–6.5, choose *Reload Scene only*. Reset static state yourself, because static fields and static event subscribers keep their values between Play mode sessions. ([Unity Manual, Domain reloading](https://docs.unity3d.com/Manual/domain-reloading.html), [Configurable Enter Play Mode](https://docs.unity3d.com/Manual/configurable-enter-play-mode.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Unity compiler with assembly definitions](https://docs.unity3d.com/Manual/assembly-definitions-referencing.html): code can only use assemblies its assembly definition references, and cyclic references aren't allowed, so wrong-way dependencies fail to compile. Checks `UNITY-STRUCT-4` and `UNITY-STRUCT-5`.
- `7` [dotnet format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format): checks code against `.editorconfig`, and with `--verify-no-changes` it fails CI when formatting differs. Without generated project files it can only check whitespace (`dotnet format whitespace --folder`). Checks `UNITY-STRUCT-3`.
- `7` [Unity Project Auditor, domain reloading issues](https://docs.unity3d.com/Manual/project-auditor/domain-reloading-issues.html): a Roslyn analyzer that finds static fields that keep their value between Play mode runs. Turn on *Use Roslyn Analyzers* first, and [run it from the command line](https://docs.unity3d.com/Manual/project-auditor/run-from-command-line.html) in CI. Partly checks `UNITY-STRUCT-10`.
