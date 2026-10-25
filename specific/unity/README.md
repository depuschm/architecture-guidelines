# Unity

Scope: Unity projects (Unity 6 and recent LTS versions), from small games to large multi-team productions. These guidelines build on the [general guidelines](../../general/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

Unity publishes thorough official guidance. **Follow these as the baseline.** The files below add only cross-cutting rules and decisions.

- `10` [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook) (Unity e-book): SOLID and the main game programming patterns, applied in Unity C#.
- `9` [Best practice guides](https://docs.unity3d.com/Manual/best-practice-guides.html) (Unity Manual): **the index of Unity's official e-books and guides**, including scripting, architecture, DOTS and multiplayer.
- `9` [Create modular game architecture with ScriptableObjects (Unity 6 edition)](https://unity.com/resources/create-modular-game-architecture-scriptableobjects-unity-6) (Unity e-book): data containers, event channels, runtime sets and enums built on ScriptableObjects.
- `9` [Ultimate guide to profiling Unity games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6) (Unity e-book).
- `8` [Create a C# style guide (Unity 6 edition)](https://unity.com/resources/c-sharp-style-guide-unity-6) (Unity e-book): naming, formatting and code-organisation conventions.
- `8` [Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project) (Unity): folder structure, naming and version control.
- `8` [Optimize performance for mobile, XR and web games](https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6) and [for consoles and PCs](https://unity.com/resources/console-pc-game-performance-optimization-unity-6) (Unity e-books).
- `8` [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) (Robert Nystrom): engine-independent, free online, and the background to many of the patterns above.
- `7` [How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales) (Unity, 2019): avoiding technical debt as a project grows.

## Guidelines in this folder

- [Project structure](project-structure.md): folders, assemblies, packages and version control.
- [Code architecture](code-architecture.md): patterns, ScriptableObjects, dependencies, events and lifecycle.
- [Content and performance](content-and-performance.md): asset loading, memory and profiling.
- [Testing](testing.md): Unity Test Framework, testable design and CI.

## Sample projects

- `7` [Boss Room](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop): a multiplayer co-op sample using Netcode for GameObjects.
- `6` [Game programming patterns demo](https://github.com/Unity-Technologies/game-programming-patterns-demo): companion project to the patterns e-book.
- `6` [PaddleGameSO](https://github.com/UnityTechnologies/PaddleGameSO): companion project to the ScriptableObjects e-book.
- `5` [ECS samples](https://github.com/Unity-Technologies/EntityComponentSystemSamples): samples for the Entities package (DOTS).
- `5` [Unite 2017: Game Architecture with Scriptable Objects](https://github.com/roboryantron/Unite2017) (Ryan Hipple): the talk's sample project, with simple ScriptableObject variables, game events and runtime sets. ([Talk video](https://www.youtube.com/watch?v=raQ3iHhE_Kk))
- `4` [Chop Chop (Open Project 1)](https://github.com/UnityTechnologies/open-project-1): an open-source game demo built on ScriptableObject event channels. Development ended in December 2021.
