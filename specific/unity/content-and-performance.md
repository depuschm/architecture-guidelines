<!-- rule-prefix: UNITY-PERF -->
# Unity: content and performance

Asset loading, memory management, profiling and localization.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Ultimate guide to profiling Unity games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6) (Unity e-book): **the baseline profiling workflow.**
- `8` [Optimize performance for mobile, XR and web games](https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6) and [for consoles and PCs](https://unity.com/resources/console-pc-game-performance-optimization-unity-6) (Unity e-books): **platform-specific optimisation checklists.**
- `8` [Addressables package manual](https://docs.unity3d.com/Packages/com.unity.addressables@latest/).
- `6` [Advanced programming and code architecture](https://unity.com/how-to/advanced-programming-and-code-architecture) (Unity): scripting performance tips covering the PlayerLoop, update managers, caching and pooling.

## Key rules

### Loading, memory and profiling

- `8` `UNITY-PERF-1` **Profile with the Unity Profiler connected to a build running on the target device, early and before and after every optimisation, not only in the Editor.** Frame-time budgets per platform are `GAMEDEV-12` in [game development](../gamedev/README.md). ([Unity, Ultimate guide to profiling](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6), [Unity Manual, Profiling your application](https://docs.unity3d.com/Manual/profiler-profiling-applications.html), [Unity Manual, Profiler](https://docs.unity3d.com/Manual/Profiler.html))
- `8` `UNITY-PERF-2` **Pair every Addressables load with a release.** Addressables uses reference counting, and unreleased handles keep assets in memory. ([Addressables, Release assets from memory](https://docs.unity3d.com/Packages/com.unity.addressables@4.1/manual/memory-assets.html))
- `8` `UNITY-PERF-3` **Avoid managed allocations in per-frame code paths to prevent garbage-collector spikes.** ([Unity Manual, Optimizing managed memory](https://docs.unity3d.com/Manual/performance-optimizing-code-managed-memory.html))
- `7` `UNITY-PERF-4` **Keep the `Resources` folder for prototypes and small bootstrap data. Load game content through Addressables (or AssetBundles).** ([Unity Manual, Load resources at runtime](https://docs.unity3d.com/Manual/LoadingResourcesatRuntime.html), [Addressables overview](https://docs.unity3d.com/Packages/com.unity.addressables@4.1/manual/AddressableAssetsOverview.html))
- `6` `UNITY-PERF-5` **Pool objects that are created and destroyed often, such as projectiles, effects and UI list items, using `UnityEngine.Pool`.** ([Unity Scripting API, ObjectPool](https://docs.unity3d.com/ScriptReference/Pool.ObjectPool_1.html), [Unity e-book, Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook))

### Localization

- `7` `UNITY-PERF-6` **Localize with the Unity Localization package: keep text in String Tables, make entries that insert values or counts Smart Strings, which take named placeholders and choose plural forms by the CLDR rules, and swap language-specific textures, audio and other assets through Asset Tables.** This applies `I18N-1`, `I18N-2` and `I18N-3`. Check layouts with the package's pseudo-localization before translation starts (`I18N-14`). ([Unity, Localization package](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/index.html), [String Tables](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html), [Smart Strings](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/Smart/SmartStrings.html), [Plural Localization Formatter](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/Smart/Plural-Formatter.html), [Asset Tables](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/AssetTables.html), [Pseudo-Localization](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/Pseudo-Localization.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Unity Project Auditor, Code view](https://docs.unity3d.com/Manual/project-auditor/code-view-reference.html): reports code issues by CPU and memory impact, and marks issues in code called every frame as Major. It recognises per-frame code only through Update methods and coroutines. [Runs from the command line](https://docs.unity3d.com/Manual/project-auditor/run-from-command-line.html) in CI. Partly checks `UNITY-PERF-3`.
- `6` [Microsoft.Unity.Analyzers](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/main/doc/index.md): flags allocating Unity API calls that have cheaper alternatives, for example `RaycastAll` instead of `RaycastNonAlloc` (UNT0028). To run them in Unity's own compile and CI, [install them as Roslyn analyzers](https://docs.unity3d.com/Manual/install-existing-analyzer.html) and [promote their warnings to errors with a ruleset](https://docs.unity3d.com/Manual/analyzer-scope-and-diagnostics.html). Partly checks `UNITY-PERF-3`.
- `6` [Unity Performance Testing package](https://docs.unity3d.com/Packages/com.unity.test-framework.performance@latest/): measures profiler markers and custom metrics in the Editor and in built players, from tests that run in CI. It records results; comparing them with a baseline is up to you. Partly checks `UNITY-PERF-1`.
