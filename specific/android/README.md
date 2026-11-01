<!-- rule-prefix: ANDROID -->
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

### Architecture

- `9` `ANDROID-1` **Use a UI layer and a data layer, and add a domain layer only when logic is complex or reused.** ([Guide to app architecture](https://developer.android.com/topic/architecture), [Domain layer](https://developer.android.com/topic/architecture/domain-layer))
- `9` `ANDROID-2` **Keep a single source of truth for each data type, and use unidirectional data flow: state flows down, events flow up.** ([Guide to app architecture](https://developer.android.com/topic/architecture))
- `9` `ANDROID-3` **Expose UI state from ViewModels as observable streams, and keep UI elements free of business logic.** ([UI layer](https://developer.android.com/topic/architecture/ui-layer), [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel))
- `8` `ANDROID-4` **Access data only through repositories in the data layer.** ([Data layer](https://developer.android.com/topic/architecture/data-layer))
- `8` `ANDROID-5` **Use dependency injection (Hilt).** ([Dependency injection in Android](https://developer.android.com/training/dependency-injection), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android))
- `7` `ANDROID-6` **Follow the coroutine best practices: inject dispatchers, make suspend functions main-safe, and don't expose mutable state.** ([Best practices for coroutines](https://developer.android.com/kotlin/coroutines/coroutines-best-practices))
- `6` `ANDROID-7` **Build offline-first where possible, with the local database as the source of truth.** ([Guide to app architecture](https://developer.android.com/topic/architecture), [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first))
- `5` `ANDROID-8` **Modularise by feature and layer as the app and team grow.** ([Modularization guide](https://developer.android.com/topic/modularization))

### Accessibility

- `7` `ANDROID-9` **Make every screen usable with TalkBack and Switch Access: describe each meaningful image and icon with a `contentDescription`, pass `null` for decorative ones, expose the role and state of custom components through Compose semantics, and make each touch target at least 48dp by 48dp.** Material components such as `Button` and `IconButton` already have the minimum size and built-in semantics, but custom elements need both set by hand; scan each screen with the Accessibility Scanner app as well. This applies `A11Y-9` and `A11Y-10`. ([Android, Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps), [Compose, Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics), [Android, Test your app's accessibility](https://developer.android.com/guide/topics/ui/accessibility/testing))
- `6` `ANDROID-10` **Set text sizes in `sp`, and test every screen at the largest font size, which is 200% since Android 14, so that text follows the user's setting without being cut off.** Don't use `sp` for padding or fixed heights, and convert between `sp` and pixels with `TypedValue.applyDimension()` and `TypedValue.deriveDimension()` instead of calculating with `fontScale`, because the scaling is nonlinear. This applies `A11Y-12`. ([Android 14, Non-linear font scaling to 200%](https://developer.android.com/about/versions/14/features#non-linear-font-scaling))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `6` [Konsist, architecture assertions](https://docs.konsist.lemonappdev.com/writing-tests/architecture-assert): Kotlin tests that check which layers may depend on which; set the direction to match the Android guide. Its [Android snippets](https://docs.konsist.lemonappdev.com/samples/starter-test-snippets/android-test-snippets) also check that ViewModel properties are `Flow`s and that repositories live in a repository package. Partly checks `ANDROID-1`, `ANDROID-3` and `ANDROID-4`.
- `6` [Compose accessibility checks](https://developer.android.com/develop/ui/compose/accessibility/testing#checks): with the `ui-test-junit4-accessibility` dependency, `enableAccessibilityChecks()` on the `AndroidComposeTestRule` runs the Accessibility Test Framework on each test action and fails the test on missing labels, small touch targets, low contrast and traversal order problems. For Views, [Espresso's `AccessibilityChecks.enable()`](https://developer.android.com/training/testing/espresso/accessibility-checking) runs the same checks. Partly checks `ANDROID-9`.
- `5` [detekt, coroutines rules](https://detekt.dev/docs/rules/coroutines/): `InjectDispatcher` flags hard-coded dispatchers, following the same Android best-practices page. Partly checks `ANDROID-6`.
- `5` [Android Lint, ContentDescription](https://googlesamples.github.io/android-custom-lint-rules/checks/ContentDescription.md.html): flags images and image buttons without a `contentDescription` in layout files, and [SpUsage](https://googlesamples.github.io/android-custom-lint-rules/checks/SpUsage.md.html) flags text sizes in `dp`. Both check XML layouts only, not Compose code. Partly checks `ANDROID-9` and `ANDROID-10`.
- `4` [Slack compose-lints](https://slackhq.github.io/compose-lints/rules/): Android Lint checks for Jetpack Compose. `ComposeViewModelForwarding` flags ViewModels passed down the UI tree, which breaks unidirectional data flow. Partly checks `ANDROID-2`.
- `4` [Module Graph Assert](https://github.com/jraska/modules-graph-assert): a Gradle plugin that fails the build when a module depends on one it isn't allowed to. It guards the module structure but doesn't create it. Partly checks `ANDROID-8`.

## Tutorials and further reading

- `8` [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course): Google's free course, which teaches the recommended architecture.
- `7` [Architecting your Compose UI](https://developer.android.com/develop/ui/compose/architecture).
- `7` [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals).
