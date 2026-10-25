<!-- rule-prefix: VUE -->
# Vue

Scope: web apps built with Vue 3, the Composition API and Single-File Components, with Pinia for shared state and Vue Router for routing, plus Nuxt (version 4) where it changes the architecture: server rendering, data fetching and server routes. Framework-independent rules for accessibility, performance and security, such as WCAG, Core Web Vitals, sanitizing HTML before `v-html` and Content Security Policy, are in [Web front end](../web/README.md). Nuxt server routes are backend code, so the [Node.js](../nodejs/README.md) and [Security](../../general/security.md) guidelines also apply to them.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Vue.js Guide](https://vuejs.org/guide/introduction.html): **the baseline.** Essentials, components, composables, the Scaling Up chapters (Single-File Components, tooling, routing, state management, testing and server-side rendering), the Best Practices chapters (production deployment, performance, accessibility and security) and TypeScript.
- `9` [Vue Style Guide](https://vuejs.org/style-guide/): the official Vue-specific coding rules in four priorities. Follow Priority A (Essential) and Priority B (Strongly Recommended); eslint-plugin-vue has a rule category for each priority.
- `9` [Nuxt documentation](https://nuxt.com/docs/4.x/getting-started/introduction): **the baseline for Nuxt apps**: rendering modes, data fetching, state management, server routes, runtime config and best practices.
- `8` [Vue.js, Security](https://vuejs.org/guide/best-practices/security.html): what Vue escapes for you, the remaining HTML, URL, style and JavaScript injection risks, and coordination with the backend.
- `8` [Pinia](https://pinia.vuejs.org/introduction.html): the official store library: defining stores, state, getters, actions, plugins, server-side rendering and testing.
- `8` [Vue Router guide](https://router.vuejs.org/guide/): the official router: dynamic and nested routes, navigation guards, route meta fields, lazy loading and typed routes.
- `7` [Vue.js, Performance](https://vuejs.org/guide/best-practices/performance.html): Vue-specific page load and update optimizations, such as choosing the architecture, code splitting, props stability, list virtualization and reducing reactivity overhead.
- `7` [Nuxt performance](https://nuxt.com/docs/4.x/guide/best-practices/performance): Nuxt's built-in features for links, hybrid rendering, lazy components and lazy hydration, the core modules for images, fonts and third-party scripts, and common problems.

## Key rules

### Components and reactivity

- `8` `VUE-1` **Never mutate props, including nested properties of object props: emit an event so that the parent changes its own state, or use `defineModel()` for two-way binding.** Props form a one-way-down binding, and mutating them lets a child change its parent's state in ways that are hard to follow. ([Vue.js, One-way data flow](https://vuejs.org/guide/components/props.html#one-way-data-flow), [Component v-model](https://vuejs.org/guide/components/v-model.html))
- `7` `VUE-2` **Write application components as Single-File Components with the Composition API and `<script setup>`.** The guide recommends this combination for full applications and the Options API for apps without build tools or with low complexity. ([Vue.js, Which to choose?](https://vuejs.org/guide/introduction.html#which-to-choose), [`<script setup>`](https://vuejs.org/api/sfc-script-setup.html))
- `7` `VUE-3` **Derive values with `computed`, keep computed getters free of side effects, and use watchers only for side effects in reaction to state changes.** A getter must not mutate other state, make requests or change the DOM, and its value is a read-only snapshot. ([Vue.js, Computed properties: best practices](https://vuejs.org/guide/essentials/computed.html#best-practices), [Watchers](https://vuejs.org/guide/essentials/watchers.html))
- `7` `VUE-4` **Declare props and emitted events with types, such as `defineProps<Props>()`, and type-check `.vue` files in CI with `vue-tsc`.** Vite only transpiles TypeScript and doesn't type-check it. ([Vue.js, Using Vue with TypeScript](https://vuejs.org/guide/typescript/overview.html), [Style Guide, Use detailed prop definitions](https://vuejs.org/style-guide/rules-essential.html#use-detailed-prop-definitions))
- `6` `VUE-5` **Extract reusable stateful logic into composables: name them `useX`, accept refs or getters and read them with `toValue()`, return a plain object of refs, and call them synchronously in `<script setup>` or `setup()`.** ([Vue.js, Composables: conventions and best practices](https://vuejs.org/guide/reusability/composables.html#conventions-and-best-practices))

### State and data fetching

- `9` `VUE-6` **In server-rendered apps, never keep user or request data in module-level state: create the app, router and stores for each request, and in Nuxt keep shared state in `useState` or Pinia, not in refs exported from a module.** The server reuses modules across requests, so one user's data can leak into another user's response. ([Vue.js, Cross-request state pollution](https://vuejs.org/guide/scaling-up/ssr.html#cross-request-state-pollution), [Nuxt, State management: best practices](https://nuxt.com/docs/4.x/getting-started/state-management#best-practices), [Pinia, Why should I use Pinia?](https://pinia.vuejs.org/introduction.html#Why-should-I-use-Pinia-))
- `7` `VUE-7` **Use Pinia for state that many components share, instead of hand-rolled global `reactive()` objects.** Pinia adds DevTools integration, server-side rendering support, plugins and type inference. Vuex is in maintenance mode. ([Vue.js, State management: Pinia](https://vuejs.org/guide/scaling-up/state-management.html#pinia), [Pinia, Introduction](https://pinia.vuejs.org/introduction.html))
- `7` `VUE-8` **In Nuxt, load the data a page renders with `useFetch` or `useAsyncData`, keep `$fetch` for requests that user events trigger, and use `pick` or `transform` to keep only the fields the page renders.** `$fetch` alone in setup can fetch the data twice, on the server and again during hydration. The composables forward the server's result to the browser in the page payload. ([Nuxt, The need for useFetch and useAsyncData](https://nuxt.com/docs/4.x/getting-started/data-fetching#the-need-for-usefetch-and-useasyncdata), [Minimize payload size](https://nuxt.com/docs/4.x/getting-started/data-fetching#minimize-payload-size))
- `6` `VUE-9` **Render the same output on the server and in the browser: use SSR-safe composables, keep browser-only code in `onMounted()` or `<ClientOnly>`, and don't render values that differ between the two, such as the current time.** Hydration mismatches delay interactivity and can leave buttons and forms without event listeners. ([Nuxt, Nuxt and hydration](https://nuxt.com/docs/4.x/guide/best-practices/hydration), [Vue.js, Hydration mismatch](https://vuejs.org/guide/scaling-up/ssr.html#hydration-mismatch))

### Routing and rendering

- `7` `VUE-10` **Use server-side rendering or static generation, for example with Nuxt, when page load performance or SEO matters, and a client-side SPA only when they don't. In Nuxt, set the rendering mode per route with `routeRules`.** ([Vue.js, Performance: choosing the right architecture](https://vuejs.org/guide/best-practices/performance.html#choosing-the-right-architecture), [Vue.js, Why SSR?](https://vuejs.org/guide/scaling-up/ssr.html#why-ssr), [Nuxt, Hybrid rendering](https://nuxt.com/docs/4.x/guide/concepts/rendering#hybrid-rendering))
- `7` `VUE-11` **Lazy-load route components with dynamic imports.** The Vue performance guide strongly recommends it for apps that use Vue Router: each route becomes a separate chunk that loads on the first visit. ([Vue.js, Code splitting](https://vuejs.org/guide/best-practices/performance.html#code-splitting), [Vue Router, Lazy loading routes](https://router.vuejs.org/guide/advanced/lazy-loading.html))
- `6` `VUE-12` **After each route change, move focus back to the start of the page, just before a skip link to the main content.** ([Vue.js, Accessibility: skip link](https://vuejs.org/guide/best-practices/accessibility.html#skip-link))

### Security

- `9` `VUE-13` **Never use untrusted content as a Vue template, and never mount Vue on server-rendered HTML that contains user-provided content.** Template expressions run as JavaScript, also during server-side rendering. For `v-html`, follow the XSS rules in [Web front end](../web/README.md). ([Vue.js, Security: Rule No.1](https://vuejs.org/guide/best-practices/security.html#rule-no-1-never-use-non-trusted-templates), [Potential dangers](https://vuejs.org/guide/best-practices/security.html#potential-dangers))
- `9` `VUE-14` **Give an environment variable the `VITE_` prefix, or put a value in Nuxt's `runtimeConfig.public`, only if it may be public.** Vite bundles `VITE_` variables into the client code, and Nuxt adds public runtime config to every page payload. Keep secrets in private `runtimeConfig` keys, and don't render them or pass them to `useState`. ([Vite, Env variables](https://vite.dev/guide/env-and-mode#env-variables), [Nuxt, Runtime config](https://nuxt.com/docs/4.x/guide/going-further/runtime-config))

### Testing

- `6` `VUE-15` **Run unit and component tests with Vitest, give each component its own component test, and in those tests interact with the component as a user would instead of mocking its child components.** ([Vue.js, Testing: component testing](https://vuejs.org/guide/scaling-up/testing.html#component-testing))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [eslint-plugin-vue](https://eslint.vuejs.org/rules/): the official linter for Single-File Components, with rule categories that follow the Style Guide's priorities. [`vue/no-mutating-props`](https://eslint.vuejs.org/rules/no-mutating-props.html) flags mutated props, and [`vue/no-side-effects-in-computed-properties`](https://eslint.vuejs.org/rules/no-side-effects-in-computed-properties.html) and [`vue/no-async-in-computed-properties`](https://eslint.vuejs.org/rules/no-async-in-computed-properties.html) flag impure computed getters. Among the opt-in rules, [`vue/component-api-style`](https://eslint.vuejs.org/rules/component-api-style.html) allows only `<script setup>` and the Composition API, and [`vue/define-props-declaration`](https://eslint.vuejs.org/rules/define-props-declaration.html) and [`vue/define-emits-declaration`](https://eslint.vuejs.org/rules/define-emits-declaration.html) require type-based declarations. In Nuxt, the [ESLint module](https://eslint.nuxt.com/packages/module) generates a project-aware config that includes the plugin's recommended rules. Checks `VUE-1`, `VUE-2` and `VUE-3`, and partly `VUE-4`.
- `7` [vue-tsc](https://github.com/vuejs/language-tools/blob/master/packages/tsc/README.md): type-checks `.vue` files from the command line. Run `vue-tsc --noEmit` in CI, or [`nuxt typecheck`](https://nuxt.com/docs/4.x/api/commands/typecheck) in a Nuxt app. Partly checks `VUE-4`.

## Tutorials and further reading

- `7` [Vue.js Tutorial](https://vuejs.org/tutorial/): the official interactive tutorial, which introduces Vue's core features step by step in the browser, in either API style.
- `6` [Vue Test Utils guide](https://test-utils.vuejs.org/guide/): the official component testing library's guide, from mounting components to testing emitted events, forms, slots, asynchronous behaviour, HTTP requests and Vue Router.
- `6` [Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq.html) (Vue.js): why the Composition API exists, and how it compares with the Options API and React Hooks.
- `6` [Vue patterns](https://www.patterns.dev/vue/) (Patterns.dev): Vue-specific patterns such as composables, `<script setup>`, state management, provide/inject and dynamic components.
