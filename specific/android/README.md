# Android

Scope: native Android apps in Kotlin, including Jetpack Compose.

## Adopted references

Google's official architecture guidance is comprehensive. **Follow it as-is.** This file only highlights the core rules.

- [Guide to app architecture](https://developer.android.com/topic/architecture): **the baseline.**
- [Recommendations for Android architecture](https://developer.android.com/topic/architecture/recommendations): a prioritised checklist of strongly recommended and recommended practices. Use it for reviews.
- [Guide to Android app modularization](https://developer.android.com/topic/modularization) and [common modularization patterns](https://developer.android.com/topic/modularization/patterns).
- [Now in Android](https://github.com/android/nowinandroid): the official, fully featured reference app.
- [Architecture samples](https://github.com/android/architecture-samples): smaller samples of the recommended architecture.

## Key rules

- **Use a UI layer and a data layer, and add a domain layer only when logic is complex or reused.** ([Guide to app architecture](https://developer.android.com/topic/architecture), [Domain layer](https://developer.android.com/topic/architecture/domain-layer))
- **Keep a single source of truth for each data type, and use unidirectional data flow: state flows down, events flow up.** ([Guide to app architecture](https://developer.android.com/topic/architecture))
- **Expose UI state from ViewModels as observable streams, and keep UI elements free of business logic.** ([UI layer](https://developer.android.com/topic/architecture/ui-layer), [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel))
- **Access data only through repositories in the data layer.** ([Data layer](https://developer.android.com/topic/architecture/data-layer))
- **Build offline-first where possible, with the local database as the source of truth.** ([Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first))
- **Use dependency injection (Hilt).** ([Dependency injection in Android](https://developer.android.com/training/dependency-injection), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android))
- **Follow the coroutine best practices: inject dispatchers, make suspend functions main-safe, and don't expose mutable state.** ([Best practices for coroutines](https://developer.android.com/kotlin/coroutines/coroutines-best-practices))
- **Modularise by feature and layer as the app and team grow.** ([Modularization guide](https://developer.android.com/topic/modularization))

## Tutorials and further reading

- [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course): Google's free course, which teaches the recommended architecture.
- [Architecting your Compose UI](https://developer.android.com/develop/ui/compose/architecture).
- [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals).
