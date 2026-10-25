# Unity: content and performance

Asset loading, memory management and profiling.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Ultimate guide to profiling Unity games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6) (Unity e-book): **the baseline profiling workflow.**
- `8` [Optimize performance for mobile, XR and web games](https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6) and [for consoles and PCs](https://unity.com/resources/console-pc-game-performance-optimization-unity-6) (Unity e-books): **platform-specific optimisation checklists.**
- `8` [Addressables package manual](https://docs.unity3d.com/Packages/com.unity.addressables@latest/).
- `6` [Advanced programming and code architecture](https://unity.com/how-to/advanced-programming-and-code-architecture) (Unity): scripting performance tips covering the PlayerLoop, update managers, caching and pooling.

## Key rules

- `9` **Profile early and on target devices, and measure before and after every optimisation.** ([Unity, Ultimate guide to profiling](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6), [Unity Manual, Profiler](https://docs.unity3d.com/Manual/Profiler.html))
- `8` **Pair every Addressables load with a release.** Addressables uses reference counting, and unreleased handles keep assets in memory. ([Addressables, Release assets from memory](https://docs.unity3d.com/Packages/com.unity.addressables@4.1/manual/memory-assets.html))
- `8` **Avoid managed allocations in per-frame code paths to prevent garbage-collector spikes.** ([Unity Manual, Optimizing managed memory](https://docs.unity3d.com/Manual/performance-optimizing-code-managed-memory.html))
- `7` **Keep the `Resources` folder for prototypes and small bootstrap data. Load game content through Addressables (or AssetBundles).** ([Unity Manual, Load resources at runtime](https://docs.unity3d.com/Manual/LoadingResourcesatRuntime.html), [Addressables overview](https://docs.unity3d.com/Packages/com.unity.addressables@4.1/manual/AddressableAssetsOverview.html))
- `7` **Pool objects that are created and destroyed often, such as projectiles, effects and UI list items, using `UnityEngine.Pool`.** ([Unity Scripting API, ObjectPool](https://docs.unity3d.com/ScriptReference/Pool.ObjectPool_1.html), [Unity Learn, Object pooling](https://learn.unity.com/course/design-patterns-unity-6/tutorial/use-object-pooling-to-boost-performance-of-c-scripts-in-unity))
