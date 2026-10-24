# Unity: testing

Automated tests for Unity projects and the architecture that makes them possible.

## Adopted references

- [Unity Test Framework](https://docs.unity3d.com/Manual/test-framework/test-framework-introduction.html) (Unity Manual): **the baseline.** It covers Edit Mode and Play Mode tests built on NUnit.
- [Unity Test Framework course](https://docs.unity3d.com/Manual/test-framework/course/overview.html) (Unity Manual): a complete hands-on tutorial.
- [How to run automated tests for your games with the Unity Test Framework](https://unity.com/how-to/automated-tests-unity-test-framework) (Unity).

## Key rules

- **Test pure logic with fast Edit Mode tests, and use Play Mode tests only for behaviour that needs the engine loop, physics or scenes.** ([Unity Test Framework introduction](https://docs.unity3d.com/Manual/test-framework/test-framework-introduction.html), [Unity, Automated tests with UTF](https://unity.com/how-to/automated-tests-unity-test-framework))
- **Put tests in their own test assemblies that reference the assemblies under test.** ([Unity Test Framework, Getting started](https://docs.unity3d.com/Manual/test-framework/getting-started.html), [Unity Manual, Assembly definitions](https://docs.unity3d.com/Manual/assembly-definition-files.html))
- **Design for testability: keep logic in plain C# classes behind thin MonoBehaviours, and inject dependencies.** ([Code architecture](code-architecture.md), [Humble Object pattern](http://xunitpatterns.com/Humble%20Object.html))
- **Run the test suite in CI from the command line in batch mode on every change.** ([Unity Test Framework, Command-line reference](https://docs.unity3d.com/Manual/test-framework/reference-command-line.html))
