# Unity: code architecture

How to structure gameplay and application code so it stays changeable as the project grows.

## Adopted references

- [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook) and the [Design patterns course (Unity 6)](https://learn.unity.com/course/design-patterns-unity-6): **the baseline for patterns in Unity C#.**
- [Create modular game architecture with ScriptableObjects](https://unity.com/resources/create-modular-game-architecture-with-scriptable-objects-ebook): **the baseline for ScriptableObject-based architecture.**
- [How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales) (Unity).
- [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) (Robert Nystrom).

## Key rules

### Structure

- **Separate UI from game logic with Model-View-Presenter (or MVC).** Views display state and forward input, and presenters hold no rendering code. ([Unity Learn, MVC and MVP patterns](https://learn.unity.com/course/design-patterns-unity-6/tutorial/build-a-modular-codebase-with-mvc-and-mvp-programming-patterns))
- **Keep logic that doesn't need the engine in plain C# classes, with MonoBehaviours as thin adapters.** The logic can then be unit tested without scenes. ([Unity, How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales), [Humble Object pattern](http://xunitpatterns.com/Humble%20Object.html))
- **Model complex behaviour, such as characters, AI and game flow, with the State pattern instead of growing `switch` statements.** ([Unity Learn, State pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/develop-a-modular-flexible-codebase-with-the-state-programming-pattern), [Nystrom, State](https://gameprogrammingpatterns.com/state.html))
- **Wrap player and AI actions in commands when you need undo, replay, rebinding or queuing.** ([Unity Learn, Command pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/use-the-command-pattern-for-flexible-and-extensible-game-systems), [Nystrom, Command](https://gameprogrammingpatterns.com/command.html))

### Data and ScriptableObjects

- **Put designer-tunable, shared data in ScriptableObject assets, not hard-coded values or copies on every prefab.** ([Unity, Separate game data and logic with ScriptableObjects](https://unity.com/how-to/separate-game-data-logic-scriptable-objects), [Unity Manual, ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html))
- **Don't use ScriptableObjects as save-game storage.** Changes made at runtime persist in the Editor but not in a built player, so use a separate persistence mechanism. ([Unity Manual, ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html))
- **Use ScriptableObject-based enums when designers need to add values without code changes.** ([Unity, ScriptableObject-based enums](https://unity.com/how-to/scriptableobject-based-enums))

### Dependencies and communication

- **Decouple systems with events.** Use C# events or UnityEvents for local wiring, and ScriptableObject event channels between scenes and systems. ([Unity Learn, Observer pattern](https://learn.unity.com/course/design-patterns-unity-6/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern), [Unity, ScriptableObject event channels](https://unity.com/how-to/scriptableobjects-event-channels-game-code), [Unity Manual, UnityEvents](https://docs.unity3d.com/Manual/unity-events.html))
- **Make dependencies explicit through serialized references, constructor or method injection, or a DI container (for example VContainer), rather than singletons and scene-wide `Find` lookups everywhere.** ([Unity, Architect your code with ScriptableObjects](https://unity.com/how-to/architect-game-code-scriptable-objects), [VContainer](https://vcontainer.hadashikick.jp/), [general: make dependencies explicit](../../general/principles.md))
- **Don't rely on the order in which Unity calls the same event function (`Awake`, `Start`, …) on different objects.** Initialise in explicit phases or set Script Execution Order deliberately. ([Unity Manual, Order of execution for event functions](https://docs.unity3d.com/Manual/execution-order.html))

### Async and scale

- **For asynchronous code, use `Awaitable` with async/await (Unity 2023.1+) or coroutines, and know which thread each continuation runs on.** ([Unity Manual, Asynchronous programming with Awaitable](https://docs.unity3d.com/Manual/async-await-support.html), [Coroutines](https://docs.unity3d.com/Manual/Coroutines.html))
- **Choose the Entities package (DOTS/ECS) deliberately for large simulations.** It is a data-oriented architecture, not a drop-in optimisation for GameObject code. ([Entities package manual](https://docs.unity3d.com/Packages/com.unity.entities@latest/), [ECS samples](https://github.com/Unity-Technologies/EntityComponentSystemSamples))
- **For multiplayer, choose the netcode stack with the Multiplayer Center and study Boss Room before designing your own architecture.** ([Multiplayer Center](https://docs.unity3d.com/Packages/com.unity.multiplayer.center@latest/), [Netcode for GameObjects](https://docs.unity3d.com/Packages/com.unity.netcode.gameobjects@latest/), [Boss Room sample](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop))
- **Choose the UI system (UI Toolkit or uGUI) per use case using Unity's comparison.** ([Unity Manual, Comparison of UI systems](https://docs.unity3d.com/Manual/UI-system-compare.html), [UI Toolkit for advanced Unity developers](https://docs.unity3d.com/Manual/best-practice-guides/ui-toolkit-for-advanced-unity-developers/bpg-uiad-index.html))
