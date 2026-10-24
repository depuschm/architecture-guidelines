# Unity

Scope: Unity projects (Unity 6 and recent LTS versions), from small games to large multi-team productions. These guidelines build on the [general guidelines](../../general/README.md).

## Adopted references

Unity publishes thorough official guidance. **Follow these as the baseline.** The files below add only cross-cutting rules and decisions.

- [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook) (Unity e-book): SOLID and the main game programming patterns, applied in Unity C#.
- [Design patterns course (Unity 6)](https://learn.unity.com/course/design-patterns-unity-6) (Unity Learn): a complete tutorial version of the patterns e-book, with sample code.
- [Create modular game architecture with ScriptableObjects](https://unity.com/resources/create-modular-game-architecture-with-scriptable-objects-ebook) (Unity e-book): data containers, event channels, runtime sets and enums built on ScriptableObjects.
- [Create a C# style guide](https://unity.com/resources/create-code-c-sharp-style-guide-e-book) (Unity e-book): naming, formatting and code-organisation conventions.
- [Best practices for organizing your Unity project](https://unity.com/how-to/organizing-your-project) (Unity): folder structure, naming and version control.
- [How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales) (Unity): avoiding technical debt as a project grows.
- [Advanced programming and code architecture](https://unity.com/how-to/advanced-programming-and-code-architecture) (Unity): an index of Unity's architecture articles.
- [Ultimate guide to profiling Unity games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6) (Unity e-book).
- [Optimize performance for mobile, XR and web games](https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6) and [for consoles and PCs](https://unity.com/resources/console-pc-game-performance-optimization-unity-6) (Unity e-books).
- [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) (Robert Nystrom): engine-independent, free online, and the background to many of the patterns above.

## Guidelines in this folder

- [Project structure](project-structure.md): folders, assemblies, packages and version control.
- [Code architecture](code-architecture.md): patterns, ScriptableObjects, dependencies, events and lifecycle.
- [Content and performance](content-and-performance.md): asset loading, memory and profiling.
- [Testing](testing.md): Unity Test Framework, testable design and CI.

## Sample projects

- [Game programming patterns demo](https://github.com/Unity-Technologies/game-programming-patterns-demo): companion project to the patterns e-book.
- [PaddleGameSO](https://github.com/UnityTechnologies/PaddleGameSO): companion project to the ScriptableObjects e-book.
- [Chop Chop (Open Project 1)](https://github.com/UnityTechnologies/open-project-1): a complete game built in the open, using ScriptableObject-based architecture.
- [Boss Room](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop): a multiplayer co-op sample using Netcode for GameObjects.
- [ECS samples](https://github.com/Unity-Technologies/EntityComponentSystemSamples): samples for the Entities package (DOTS).
- [Unite 2017: Game Architecture with Scriptable Objects](https://github.com/roboryantron/Unite2017) (Ryan Hipple): the talk's sample project, and the origin of the event-channel and runtime-set patterns. ([Talk video](https://www.youtube.com/watch?v=raQ3iHhE_Kk))
