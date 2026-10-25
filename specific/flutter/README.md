<!-- rule-prefix: FLUTTER -->
# Flutter

Scope: cross-platform apps built with Flutter and Dart.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

The Flutter team publishes an official architecture guide. **Follow it as-is.**

- `10` [Flutter app architecture](https://docs.flutter.dev/app-architecture): **the baseline.** It covers [concepts](https://docs.flutter.dev/app-architecture/concepts), the [guide](https://docs.flutter.dev/app-architecture/guide) and a [case study](https://docs.flutter.dev/app-architecture/case-study).
- `9` [Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations): a prioritised checklist. Use it for reviews.
- `8` [Compass sample app](https://github.com/flutter/samples/tree/main/compass_app): the reference app for the guide.
- `8` [Effective Dart](https://dart.dev/effective-dart): style, documentation, usage and design rules for Dart.
- `7` [Design patterns](https://docs.flutter.dev/app-architecture/design-patterns): offline-first, command, result and other patterns.

## Key rules

- `9` `FLUTTER-1` **Separate the UI layer (views and view models) from the data layer (repositories and services), and add a domain layer of use cases only when needed.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- `8` `FLUTTER-2` **Make repositories the source of truth for app data, with services that wrap external APIs.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- `8` `FLUTTER-3` **Use unidirectional data flow and immutable data models.** ([Flutter, Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations))
- `7` `FLUTTER-4` **Cover logic with unit tests, widgets with widget tests, and critical flows with integration tests.** ([Flutter, Testing overview](https://docs.flutter.dev/testing/overview))
- `6` `FLUTTER-5` **Choose a state management approach that fits the app and the team, and use it consistently for app state. `setState` is fine for widget-local state.** ([Flutter, State management options](https://docs.flutter.dev/data-and-backend/state-mgmt/options), [Ephemeral vs. app state](https://docs.flutter.dev/data-and-backend/state-mgmt/ephemeral-vs-app))
- `5` `FLUTTER-6` **Model user actions as commands, and model operation outcomes as `Result` values instead of throwing across layers.** ([Flutter, Command pattern](https://docs.flutter.dev/app-architecture/design-patterns/command), [Result pattern](https://docs.flutter.dev/app-architecture/design-patterns/result))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [Dart analyzer](https://dart.dev/tools/analysis) with [flutter_lints](https://pub.dev/packages/flutter_lints): the lint set the Flutter team recommends. [`must_be_immutable`](https://dart.dev/tools/diagnostics/must_be_immutable) and [`prefer_final_fields`](https://dart.dev/tools/linter-rules/prefer_final_fields) catch mutable fields in data models. Partly checks `FLUTTER-3`.
- `4` [DCM, avoid-banned-imports](https://dcm.dev/docs/rules/common/avoid-banned-imports/) (commercial): bans imports per folder, for example UI code importing services directly. Checks `FLUTTER-1`.
- `4` [bloc_lint, avoid_flutter_imports](https://bloclibrary.dev/lint-rules/avoid_flutter_imports/) (for apps that use Bloc): keeps Flutter out of business logic components, and [avoid_public_fields](https://bloclibrary.dev/lint-rules/avoid_public_fields/) keeps state exposed only through the state object. Partly checks `FLUTTER-1` and `FLUTTER-3`.

## Tutorials and further reading

- `7` [Performance best practices](https://docs.flutter.dev/perf/best-practices).
- `6` [Offline-first support](https://docs.flutter.dev/app-architecture/design-patterns/offline-first).
