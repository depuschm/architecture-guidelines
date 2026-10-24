# Unity: project structure

Folders, assemblies, packages and version control.

## Adopted references

- [Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project) (Unity): **follow it for folder layout and naming.**
- [Introduction to assemblies in Unity](https://docs.unity3d.com/Manual/assembly-definitions-intro.html) and [Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html) (Unity Manual).
- [Version control](https://docs.unity3d.com/Manual/VersionControl.html) (Unity Manual).

## Key rules

### Folders and naming

- **Agree on one folder structure and naming convention, write it down, and keep your own assets separate from third-party assets.** ([Unity, Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project))
- **Know Unity's reserved folder names (`Editor`, `Resources`, `StreamingAssets`, `Plugins`, …) and use them only for their purpose.** ([Unity Manual, Special folder names](https://docs.unity3d.com/Manual/SpecialFolders.html))
- **Apply the C# naming and style conventions from Unity's style guide consistently, and enforce them in code review.** ([Unity, Naming and code style tips](https://unity.com/how-to/naming-and-code-style-tips-c-scripting-unity), [C# style guide e-book](https://unity.com/resources/create-code-c-sharp-style-guide-e-book))

### Assemblies and packages

- **Split code into assemblies with Assembly Definition files once the project grows.** Only changed assemblies recompile, and references between assemblies have to be declared, which makes dependency direction explicit. ([Unity Manual, Introduction to assemblies](https://docs.unity3d.com/Manual/assembly-definitions-intro.html), [Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html))
- **Mirror the architecture in assemblies, for example `Game.Core` (no engine-specific dependencies where practical), `Game.Gameplay`, `Game.UI`, `Game.Editor` and `*.Tests`, so that wrong-way references fail to compile.** ([Unity Manual, Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html), [general: point dependencies inwards](../../general/architecture-styles.md))
- **Move systems that several projects share into custom UPM packages that follow the standard package layout.** ([Unity Manual, Creating custom packages](https://docs.unity3d.com/Manual/CustomPackages.html), [Package layout](https://docs.unity3d.com/Manual/cus-layout.html))

### Version control

- **Keep `.meta` files visible and committed, and keep asset serialization on Force Text, so that assets diff and merge.** Both are the defaults. Don't change them. ([Unity Manual, Version control settings](https://docs.unity3d.com/Manual/class-VersionControlSettings.html), [Editor settings: Asset Serialization](https://docs.unity3d.com/Manual/class-EditorManager.html))
- **Start from the community Unity `.gitignore` so that generated folders such as `Library/` and `Temp/` are never committed.** ([github/gitignore, Unity.gitignore](https://github.com/github/gitignore/blob/main/Unity.gitignore))
- **Configure UnityYAMLMerge (Smart Merge) as the merge tool for scenes and prefabs.** ([Unity Manual, Smart Merge](https://docs.unity3d.com/Manual/SmartMerge.html))

### Iteration speed

- **Consider turning off domain and scene reload on entering Play Mode for faster iteration.** If you do, reset static state yourself, because static fields keep their values between play sessions. ([Unity Manual, Configurable Enter Play Mode](https://docs.unity3d.com/Manual/configurable-enter-play-mode.html), [Domain reloading](https://docs.unity3d.com/Manual/domain-reloading.html))
