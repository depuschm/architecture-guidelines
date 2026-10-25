<!-- rule-prefix: UNITY-TEST -->
# Unity: testing

Automated tests for Unity projects and the architecture that makes them possible.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `9` [Unity Test Framework](https://docs.unity3d.com/Manual/test-framework/test-framework-introduction.html) (Unity Manual): **the baseline.** It covers Edit Mode and Play Mode tests built on NUnit.
- `8` [Unity Test Framework course](https://docs.unity3d.com/Manual/test-framework/course/overview.html) (Unity Manual): a complete hands-on tutorial.
- `6` [How to run automated tests for your games with the Unity Test Framework](https://unity.com/how-to/automated-tests-unity-test-framework) (Unity).

## Key rules

- `8` `UNITY-TEST-1` **Design for testability: keep logic in plain C# classes behind thin MonoBehaviours, and inject dependencies.** ([Unity, How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales), [Humble Object pattern](http://xunitpatterns.com/Humble%20Object.html))
- `8` `UNITY-TEST-2` **Run the tests from the command line in batch mode as part of the build, so CI runs them on every change.** ([Unity Test Framework, Run tests from the command line](https://docs.unity3d.com/Manual/test-framework/run-tests-from-command-line.html), [Unity, How to architect code as your project scales](https://unity.com/how-to/how-architect-code-your-project-scales))
- `7` `UNITY-TEST-3` **Write plain NUnit `[Test]` tests in Edit Mode for logic that doesn't need Play mode, and use `[UnityTest]` Play Mode tests for runtime behaviour that spans frames or needs a scene.** ([Unity Test Framework, Edit Mode vs. Play Mode tests](https://docs.unity3d.com/Manual/test-framework/edit-mode-vs-play-mode-tests.html))
- `7` `UNITY-TEST-4` **Put tests in their own test assemblies that reference the assemblies under test.** Test assemblies can't reference `Assembly-CSharp`, so code under test must live in a custom assembly. ([Unity Test Framework, Edit Mode vs. Play Mode tests](https://docs.unity3d.com/Manual/test-framework/edit-mode-vs-play-mode-tests.html), [Unity Manual, Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html))
