---
name: unity-architecture
description: Design or review the architecture of a Unity project, covering folder and assembly-definition structure, ScriptableObject usage, dependency wiring and singletons, events, UI separation (MVP), asset loading with Addressables, performance hygiene and tests, based on Unity's official guidance as cited in the Architecture Guidelines. Use in Unity projects (Assets/, ProjectSettings/) when asked how to structure a system or feature, to review or refactor for scale, or to assess technical debt.
argument-hint: "[review | design <feature>]"
---

# Unity architecture

Apply the Unity guidelines to design new systems or review an existing project.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Read:

- `<root>/specific/unity/README.md`, `project-structure.md`, `code-architecture.md`, `content-and-performance.md` and `testing.md`
- `<root>/general/principles.md`

Cite rules by file and rule title, with the source link copied exactly from the guideline file.

## 1. Understand the project

- Read `ProjectSettings/ProjectVersion.txt` for the Unity version. Some advice depends on it; for example, `Awaitable` needs Unity 2023.1 or later.
- Read `Packages/manifest.json` for the packages in use, such as Addressables, Entities, Netcode, Input System, Test Framework, and DI containers from scoped registries.
- Skip generated and third-party folders in all searches: `Library/`, `Temp/`, `Logs/`, `obj/`, `Build*/`, and any vendor folders under `Assets/`.

## 2a. Design mode (new feature or system)

Propose a design that covers each point. Cite the rule behind each choice.

1. **Assemblies**: which assembly the code goes in, and which references it is allowed.
2. **Data**: which tunable or shared data becomes ScriptableObject assets, and which runtime state lives in plain C# objects.
3. **Behaviour**: plain C# classes for the logic, and thin MonoBehaviours as adapters. Use the State or Command patterns where they fit.
4. **Communication**: C# events, UnityEvents or ScriptableObject event channels, and who subscribes and unsubscribes.
5. **Dependencies**: how collaborators are provided, through serialized references, injection or a DI container. Avoid new singletons.
6. **UI**: View and Presenter split.
7. **Content**: what's loaded through Addressables, and when it's released.
8. **Tests**: which logic gets Edit Mode tests and which flows need Play Mode tests.

Show a small code skeleton only if the user asks for one.

## 2b. Review mode (existing project)

Collect evidence with these checks, then evaluate it against the rules.

| Area | How to check |
| --- | --- |
| Assemblies | Find `*.asmdef` under `Assets/`. If there are none, everything is in `Assembly-CSharp`. Read the `references` arrays and look for cycles or wrong-way dependencies, such as gameplay code referencing UI or Editor code |
| Folders | Look at the top-level layout of `Assets/`: is first-party code separated from third-party code, is naming consistent, and how big are any `Resources/` folders? |
| Version control | Check that `.gitignore` excludes `Library/` and `Temp/`. Check for `m_SerializationMode: 2` (Force Text) in `ProjectSettings/EditorSettings.asset`, and visible meta files in `ProjectSettings/VersionControlSettings.asset` if that file exists |
| Global state | Grep for `static .* Instance`, `FindObjectOfType`, `FindFirstObjectByType`, `FindAnyObjectByType`, `GameObject.Find(` and `SendMessage(` |
| Large classes | List the largest `.cs` files and check them for MonoBehaviours with too many responsibilities |
| Events | Compare `+=` subscriptions in `OnEnable`/`Awake`/`Start` with the matching `-=` in `OnDisable`/`OnDestroy` |
| Content loading | Grep `Resources.Load`. Compare Addressables `LoadAssetAsync`/`InstantiateAsync` calls with `Release`/`ReleaseInstance` calls |
| Per-frame code | Look for allocations (`new List`, LINQ, string concatenation, `GetComponent`) inside `Update`, `FixedUpdate` and `LateUpdate` |
| Play Mode options | If domain reload is off (the default from Unity 6.6; in older versions, `m_EnterPlayModeOptionsEnabled: 1` in `EditorSettings.asset`), check that static fields and static event subscriptions are reset, for example with `[RuntimeInitializeOnLoadMethod]` |
| Tests | Find test assemblies (asmdefs that reference the test runner or NUnit) and count `[Test]` and `[UnityTest]`. Check whether CI runs them |

Treat grep hits as leads, not verdicts. Read the code before reporting a finding.

## 3. Report

Use the report format from the `architecture-review` skill: a summary, then a findings table (severity, finding, evidence `path:line`, guideline, source), recommendations, and observations not covered by the guidelines. Mention what the project does well.
