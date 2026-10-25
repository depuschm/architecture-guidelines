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

- `9` **Separate the UI layer (views and view models) from the data layer (repositories and services), and add a domain layer of use cases only when needed.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- `8` **Make repositories the source of truth for app data, with services that wrap external APIs.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- `8` **Use unidirectional data flow and immutable data models.** ([Flutter, Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations))
- `7` **Cover logic with unit tests, widgets with widget tests, and critical flows with integration tests.** ([Flutter, Testing overview](https://docs.flutter.dev/testing/overview))
- `6` **Choose a state management approach that fits the app and the team, and use it consistently for app state. `setState` is fine for widget-local state.** ([Flutter, State management options](https://docs.flutter.dev/data-and-backend/state-mgmt/options), [Ephemeral vs. app state](https://docs.flutter.dev/data-and-backend/state-mgmt/ephemeral-vs-app))
- `5` **Model user actions as commands, and model operation outcomes as `Result` values instead of throwing across layers.** ([Flutter, Command pattern](https://docs.flutter.dev/app-architecture/design-patterns/command), [Result pattern](https://docs.flutter.dev/app-architecture/design-patterns/result))

## Tutorials and further reading

- `7` [Performance best practices](https://docs.flutter.dev/perf/best-practices).
- `6` [Offline-first support](https://docs.flutter.dev/app-architecture/design-patterns/offline-first).
