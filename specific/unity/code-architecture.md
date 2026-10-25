# Unity: code architecture

How to structure gameplay and application code so it stays changeable as the project grows.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook) and its [demo project](https://github.com/Unity-Technologies/game-programming-patterns-demo): **the baseline for patterns in Unity C#.**
- `9` [Create modular game architecture with ScriptableObjects (Unity 6 edition)](https://unity.com/resources/create-modular-game-architecture-scriptableobjects-unity-6): **the baseline for ScriptableObject-based architecture.**
- `8` [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) (Robert Nystrom).
- `7` [How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales) (Unity).

## Key rules

### Structure

- `8` **Keep logic that doesn't need the engine in plain C# classes, with MonoBehaviours as thin adapters.** The logic can then be unit tested without scenes. ([Unity, How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales), [Humble Object pattern](http://xunitpatterns.com/Humble%20Object.html))
- `7` **Separate UI from game logic with Model-View-Presenter (or MVC).** Views display state and forward input, and presenters hold no rendering code. ([Unity Learn, MVC and MVP patterns](https://learn.unity.com/course/design-patterns-unity-6/tutorial/build-a-modular-codebase-with-mvc-and-mvp-programming-patterns))
- `5` **Model complex behaviour, such as characters, AI and game flow, with the State pattern instead of growing `switch` statements.** ([Unity Learn, State pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/develop-a-modular-flexible-codebase-with-the-state-programming-pattern), [Nystrom, State](https://gameprogrammingpatterns.com/state.html))
- `4` **Wrap player and AI actions in commands when you need undo, replay, rebinding or queuing.** ([Unity Learn, Command pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/use-the-command-pattern-for-flexible-and-extensible-game-systems), [Nystrom, Command](https://gameprogrammingpatterns.com/command.html))

### Data and ScriptableObjects

- `8` **Put designer-tunable, shared data in ScriptableObject assets, not hard-coded values or copies on every prefab.** ([Unity, Separate game data and logic with ScriptableObjects](https://unity.com/how-to/separate-game-data-logic-scriptable-objects), [Unity Manual, ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html))
- `8` **Don't use ScriptableObjects as save-game storage.** Changes made at runtime persist in the Editor but not in a built player, so use a separate persistence mechanism. ([Unity Manual, ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html))
- `4` **Use ScriptableObject-based enums when designers need to add values without code changes.** ([Unity, ScriptableObject-based enums](https://unity.com/how-to/scriptableobject-based-enums))

### Dependencies and communication

- `8` **Make dependencies explicit through serialized references, constructor or method injection, or a DI container (for example VContainer), rather than singletons and scene-wide `Find` lookups everywhere.** ([Unity, Architect your code with ScriptableObjects](https://unity.com/how-to/architect-game-code-scriptable-objects), [Unity Scripting API, GameObject.Find](https://docs.unity3d.com/ScriptReference/GameObject.Find.html), [VContainer](https://vcontainer.hadashikick.jp/), [general: make dependencies explicit](../../general/principles.md))
- `8` **Don't rely on the order in which Unity calls the same event function (`Awake`, `Start`, …) on different objects.** Initialise in explicit phases or set Script Execution Order deliberately. ([Unity Manual, Order of execution for event functions](https://docs.unity3d.com/Manual/execution-order.html))
- `7` **Decouple systems with events.** Use C# events or UnityEvents for local wiring, and ScriptableObject event channels between scenes and systems. ([Unity Learn, Observer pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern), [Unity, ScriptableObject event channels](https://unity.com/how-to/scriptableobjects-event-channels-game-code), [Unity Manual, UnityEvents](https://docs.unity3d.com/Manual/unity-events.html))

### Async and scale

- `6` **For asynchronous code, use `Awaitable` with async/await (Unity 2023.1+) or coroutines, and know which thread each continuation runs on.** ([Unity Manual, Asynchronous programming with Awaitable](https://docs.unity3d.com/Manual/async-await-support.html), [Coroutines](https://docs.unity3d.com/Manual/Coroutines.html))
- `5` **For multiplayer, choose the netcode stack with the Multiplayer Center and study Boss Room before designing your own architecture.** ([Multiplayer Center](https://docs.unity3d.com/Packages/com.unity.multiplayer.center@latest/), [Netcode for GameObjects](https://docs.unity3d.com/Packages/com.unity.netcode.gameobjects@latest/), [Boss Room sample](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop))
- `5` **Choose the UI system (UI Toolkit or uGUI) per use case using Unity's comparison.** ([Unity Manual, Comparison of UI systems](https://docs.unity3d.com/Manual/UI-system-compare.html), [UI Toolkit for advanced Unity developers](https://docs.unity3d.com/Manual/best-practice-guides/ui-toolkit-for-advanced-unity-developers/bpg-uiad-index.html))
- `4` **Choose the Entities package (DOTS/ECS) deliberately for large simulations.** It is a data-oriented architecture, not a drop-in optimisation for GameObject code. ([Entities package manual](https://docs.unity3d.com/Packages/com.unity.entities@latest/), [ECS samples](https://github.com/Unity-Technologies/EntityComponentSystemSamples))
