---
name: game-architecture
description: Design or review the architecture of a game project in Unity, Godot, Unreal Engine or a custom engine, covering code and scene structure, data-driven design, communication between systems, dependencies and singletons, content loading, the game loop, save data, multiplayer, performance budgets, version control for large assets, accessibility and tests, based on the engine's official guidance as cited in the Architecture Guidelines. Use in game projects (Unity Assets/ and ProjectSettings/, Godot project.godot, Unreal .uproject) when asked how to structure a system or feature, to review or refactor for scale, or to assess technical debt.
argument-hint: "[review | design <feature>]"
---

# Game architecture

Apply the game development guidelines to design new systems or review an existing game project.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Always read:

- `<root>/specific/gamedev/README.md`: engine-independent rules (`GAMEDEV`) for the game loop, code structure, multiplayer, save data, performance, version control and accessibility
- `<root>/general/principles.md`

Then read the engine's guidelines:

| Engine | Detect by | Read |
| --- | --- | --- |
| Unity | `ProjectSettings/ProjectVersion.txt`, `Assets/` with `.meta` files | `<root>/specific/unity/README.md`, `project-structure.md`, `code-architecture.md`, `content-and-performance.md` and `testing.md` |
| Godot | `project.godot` | `<root>/specific/godot/README.md` |
| Unreal Engine | a `.uproject` file | `<root>/specific/unreal/README.md` |
| Custom engine or framework | a game loop in your own code, for example on SDL, raylib, MonoGame or Bevy | the game development file only |

If the game ships on iOS or Android, also read `<root>/specific/mobile-games/README.md`.

Cite rules by ID (for example `GODOT-3` or `UNITY-STRUCT-1`), with their score and title, and copy the source link exactly from the guideline file. Rules are sorted by score (1–10, see `<root>/RANKING.md`), so the most important ones come first in each section. Use the score as a severity hint. Where a file's "How to enforce" section names a tool for a rule, recommend it alongside the fix.

## 1. Understand the project

- **Engine version.** Unity: `ProjectSettings/ProjectVersion.txt`. Godot: `config/features` in `project.godot`. Unreal: `EngineAssociation` in the `.uproject` file. Some advice depends on it; for example, Unity's `Awaitable` needs Unity 2023.1 or later.
- **Packages and plugins.** Unity: `Packages/manifest.json` (Addressables, Entities, Netcode, Input System, Test Framework, DI containers). Godot: `addons/` and the `[autoload]` and `[editor_plugins]` sections of `project.godot`. Unreal: the `Modules` and `Plugins` lists in the `.uproject` file, and each module's `*.Build.cs`.
- **Targets.** Which platforms the game ships on, whether it's multiplayer, and the target frame rate. Ask if you can't tell, because frame budgets and multiplayer rules depend on them.
- **Skip generated and third-party folders** in all searches. Unity: `Library/`, `Temp/`, `Logs/`, `obj/`, `Build*/` and vendor folders under `Assets/`. Godot: `.godot/` and third-party plugins in `addons/`. Unreal: `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/` and marketplace plugins.

## 2a. Design mode (new feature or system)

Propose a design that covers each point that applies. Cite the rule behind each choice, from the engine file where it has one and from the game development file otherwise.

1. **Structure**: where the code goes. Unity: which assembly, and which references it may have. Godot: which scenes, and which parent wires them together. Unreal: which module, and which gameplay framework class owns what.
2. **Data**: which tuning values and entity types become designer-editable data. Unity: ScriptableObject assets. Godot: custom Resources saved as `.tres` files. Unreal: data assets, registered as primary assets if they load on demand.
3. **Behaviour**: composition over inheritance. Unity: plain C# classes for logic, with thin MonoBehaviours as adapters. Godot: self-contained scenes, with plain `RefCounted` or `Resource` classes for logic that doesn't need the scene tree. Unreal: C++ base classes with a small API that Blueprints extend, and subsystems for game-wide services.
4. **Communication**: who notifies whom. Unity: C# events, UnityEvents or ScriptableObject event channels. Godot: parents call down, children report up through signals. Unreal: delegates, and replicated properties with RepNotify in multiplayer.
5. **Dependencies**: how collaborators are provided. Avoid new singletons and global lookups: Unity serialized references or injection, Godot `@export` properties or unique names and few autoloads, Unreal subsystems.
6. **Time**: simulation in fixed steps with interpolation for rendering (`_physics_process` in Godot, `FixedUpdate` for physics in Unity).
7. **Content**: what loads on demand and when it's released. Unity: Addressables. Unreal: soft references and async loading.
8. **Save data**: a versioned schema with migrations, and a safe write that keeps the last good save.
9. **Multiplayer**, if any: what the server owns, what is predicted on the client, and what is replicated.
10. **Accessibility**: which Game Accessibility Guidelines apply, starting with remapping, text size, colour blindness and subtitles.
11. **Tests**: which logic gets unit tests, which flows need engine-level tests, and how CI runs them headless.

Show a small code skeleton only if the user asks for one.

## 2b. Review mode (existing project)

Collect evidence with the checks for every project and for the engine, then evaluate it against the rules. Treat grep hits as leads, not verdicts: read the code before reporting a finding.

**Every project:**

| Area | How to check |
| --- | --- |
| Version control | Check the `.gitignore` for the engine's generated folders, and `.gitattributes` for Git LFS tracking and `lockable` binary types. Look for large binaries committed without LFS |
| Game loop | Find where movement and game logic run, and whether the simulation uses a fixed time step |
| Save data | Find the save code. Is there a version number and a migration path? Is the new save written separately before replacing the old one? |
| Accessibility | Look for input remapping, text size, colour-blind and subtitle options in settings code and menus |
| Tests | Find the test framework, count the tests, and check whether CI runs them |

**Unity:**

| Area | How to check |
| --- | --- |
| Assemblies | Find `*.asmdef` under `Assets/`. If there are none, everything is in `Assembly-CSharp`. Read the `references` arrays and look for cycles or wrong-way dependencies, such as gameplay code referencing UI or Editor code |
| Folders | Look at the top-level layout of `Assets/`: is first-party code separated from third-party code, is naming consistent, and how big are any `Resources/` folders? |
| Serialization | Check for `m_SerializationMode: 2` (Force Text) in `ProjectSettings/EditorSettings.asset`, and visible meta files in `ProjectSettings/VersionControlSettings.asset` if that file exists |
| Global state | Grep for `static .* Instance`, `FindObjectOfType`, `FindFirstObjectByType`, `FindAnyObjectByType`, `GameObject.Find(` and `SendMessage(` |
| Large classes | List the largest `.cs` files and check them for MonoBehaviours with too many responsibilities |
| Events | Compare `+=` subscriptions in `OnEnable`/`Awake`/`Start` with the matching `-=` in `OnDisable`/`OnDestroy` |
| Content loading | Grep `Resources.Load`. Compare Addressables `LoadAssetAsync`/`InstantiateAsync` calls with `Release`/`ReleaseInstance` calls |
| Per-frame code | Look for allocations (`new List`, LINQ, string concatenation, `GetComponent`) inside `Update`, `FixedUpdate` and `LateUpdate` |
| Play Mode options | If domain reload is off (the default from Unity 6.6; in older versions, `m_EnterPlayModeOptionsEnabled: 1` in `EditorSettings.asset`), check that static fields and static event subscriptions are reset, for example with `[RuntimeInitializeOnLoadMethod]` |

**Godot:**

| Area | How to check |
| --- | --- |
| Version control | Check that `.godot/` is ignored and that `.import` and `.uid` files are committed next to their assets and scripts |
| Autoloads | Read the `[autoload]` section of `project.godot`, then each autoload script: does it run one broad system with its own data, or hold unrelated state for everything? |
| Node references | Grep `get_node(`, `$` and `%` paths for `../` segments and absolute `/root/` paths |
| Static typing | Look for `var` declarations without a type or `:=`, and functions without a return type. Check `debug/gdscript/warnings/untyped_declaration` in `project.godot` |
| Physics | Look for movement (`position +=`, `velocity`, `move_and_slide`) inside `_process`, and check `physics/common/physics_interpolation` |
| Data | Find `extends Resource` classes and `.tres` files. Look for code that changes a loaded resource without `duplicate()` or `resource_local_to_scene` |
| Saves | Find `FileAccess` writes: saves must go to `user://`. Grep `get_var(true`, `bytes_to_var_with_objects` and `allow_objects` on data players can edit |
| Naming | Look for file and folder names that aren't snake_case, and third-party code outside `addons/` |

**Unreal Engine:**

| Area | How to check |
| --- | --- |
| Modules | Read each `*.Build.cs`: are dependencies private unless public headers need them, and does editor-only code (for example an `UnrealEd` dependency) sit in an `Editor` module? |
| Object references | In headers, look for `UObject`-derived pointer members (`U…*`, `A…*`) without `UPROPERTY`, and raw pointers where `TObjectPtr` or `TWeakObjectPtr` belong |
| Gameplay framework | Find the game mode, game state, player state, player controller and game instance classes. Is each piece of state in the class that should own it? Are services added to a custom game instance instead of subsystems? |
| Networking | Find `UFUNCTION(Server` and `NetMulticast` functions: does the server validate each request before changing state? Are frequently called RPCs `Reliable`? Would replicated properties with RepNotify fit better? |
| Asset references | Look for hard references to large assets in `UPROPERTY` members, `ConstructorHelpers::FObjectFinder` and synchronous `LoadObject` calls where soft references and async loading belong |
| Asset Manager | Check the Asset Manager settings in `Config/DefaultGame.ini` for primary asset types |
| Levels | For levels that several people edit, check whether they use One File Per Actor (the default with World Partition) |
| Quality | Find automation tests and Data Validation rules, and check whether CI runs them |

## 3. Report

Every finding must include the rule's **source link**, copied exactly from the guideline file. A finding without its source breaks this repository's core rule. Use this structure:

```markdown
## Game architecture review: <project>

**Engine:** <engine and version> · **Targets:** <platforms, multiplayer, frame rate> · **Guidelines applied:** specific/gamedev, specific/<engine>, general/principles.md

### Summary
<2–4 sentences: overall shape, top risks, what the project does well>

### Findings
| # | Severity | Finding | Evidence | Rule | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | High | <what is wrong and why it matters> | `scripts/game.gd:12` | `GODOT-13` (7): "Write saves and settings to `user://`, and don't decode objects…" | [Godot, Saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html) |

### Recommendations
1. <Concrete next step, linked to finding numbers. Name a tool from the file's "How to enforce" section where one exists.>

### Not covered by the guidelines
- <Observation (opinion, no source)>
```

Severity starts from the rule's score: 9–10 usually High, 6–8 Medium, 1–5 Low, adjusted for the actual impact.
