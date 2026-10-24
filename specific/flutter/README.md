# Flutter

Scope: cross-platform apps built with Flutter and Dart.

## Adopted references

The Flutter team publishes an official architecture guide. **Follow it as-is.**

- [Flutter app architecture](https://docs.flutter.dev/app-architecture): **the baseline.** It covers [concepts](https://docs.flutter.dev/app-architecture/concepts), the [guide](https://docs.flutter.dev/app-architecture/guide) and a [case study](https://docs.flutter.dev/app-architecture/case-study).
- [Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations): a prioritised checklist. Use it for reviews.
- [Design patterns](https://docs.flutter.dev/app-architecture/design-patterns): offline-first, command, result and other patterns.
- [Compass sample app](https://github.com/flutter/samples/tree/main/compass_app): the reference app for the guide.
- [Effective Dart](https://dart.dev/effective-dart): style, documentation, usage and design rules for Dart.

## Key rules

- **Separate the UI layer (views and view models) from the data layer (repositories and services), and add a domain layer of use cases only when needed.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- **Make repositories the source of truth for app data, with services that wrap external APIs.** ([Flutter, Guide to app architecture](https://docs.flutter.dev/app-architecture/guide))
- **Use unidirectional data flow and immutable data models.** ([Flutter, Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations))
- **Model user actions as commands, and model operation outcomes as `Result` values instead of throwing across layers.** ([Flutter, Command pattern](https://docs.flutter.dev/app-architecture/design-patterns/command), [Result pattern](https://docs.flutter.dev/app-architecture/design-patterns/result))
- **Pick one state management approach for the app and use it consistently.** ([Flutter, State management options](https://docs.flutter.dev/data-and-backend/state-mgmt/options))
- **Cover logic with unit tests, widgets with widget tests, and critical flows with integration tests.** ([Flutter, Testing overview](https://docs.flutter.dev/testing/overview))

## Tutorials and further reading

- [Offline-first support](https://docs.flutter.dev/app-architecture/design-patterns/offline-first).
- [Performance best practices](https://docs.flutter.dev/perf/best-practices).
