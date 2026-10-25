# Android

Scope: native Android apps in Kotlin, including Jetpack Compose.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

Google's official architecture guidance is comprehensive. **Follow it as-is.** This file only highlights the core rules.

- `10` [Guide to app architecture](https://developer.android.com/topic/architecture): **the baseline.**
- `9` [Recommendations for Android architecture](https://developer.android.com/topic/architecture/recommendations): a prioritised checklist of strongly recommended and recommended practices. Use it for reviews.
- `9` [Now in Android](https://github.com/android/nowinandroid): the official, fully featured reference app.
- `8` [Guide to Android app modularization](https://developer.android.com/topic/modularization) and [common modularization patterns](https://developer.android.com/topic/modularization/patterns).
- `7` [Architecture samples](https://github.com/android/architecture-samples): smaller samples of the recommended architecture.

## Key rules

- `9` **Use a UI layer and a data layer, and add a domain layer only when logic is complex or reused.** ([Guide to app architecture](https://developer.android.com/topic/architecture), [Domain layer](https://developer.android.com/topic/architecture/domain-layer))
- `9` **Keep a single source of truth for each data type, and use unidirectional data flow: state flows down, events flow up.** ([Guide to app architecture](https://developer.android.com/topic/architecture))
- `9` **Expose UI state from ViewModels as observable streams, and keep UI elements free of business logic.** ([UI layer](https://developer.android.com/topic/architecture/ui-layer), [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel))
- `8` **Access data only through repositories in the data layer.** ([Data layer](https://developer.android.com/topic/architecture/data-layer))
- `8` **Use dependency injection (Hilt).** ([Dependency injection in Android](https://developer.android.com/training/dependency-injection), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android))
- `7` **Follow the coroutine best practices: inject dispatchers, make suspend functions main-safe, and don't expose mutable state.** ([Best practices for coroutines](https://developer.android.com/kotlin/coroutines/coroutines-best-practices))
- `6` **Build offline-first where possible, with the local database as the source of truth.** ([Guide to app architecture](https://developer.android.com/topic/architecture), [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first))
- `5` **Modularise by feature and layer as the app and team grow.** ([Modularization guide](https://developer.android.com/topic/modularization))

## Tutorials and further reading

- `8` [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course): Google's free course, which teaches the recommended architecture.
- `7` [Architecting your Compose UI](https://developer.android.com/develop/ui/compose/architecture).
- `7` [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals).
