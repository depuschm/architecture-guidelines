<!-- rule-prefix: REACT -->
# React

Scope: web front ends built with React, either on their own or inside a framework.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [react.dev: Learn React](https://react.dev/learn): **the baseline.** The official tutorial covers component design and state management.
- `9` [Rules of React](https://react.dev/reference/rules): rules that React code must follow to behave correctly.
- `9` [Thinking in React](https://react.dev/learn/thinking-in-react): the official method for breaking a UI into components and state.
- `7` [Bulletproof React](https://github.com/alan2207/bulletproof-react): an opinionated, production-ready project architecture.
- `6` [Patterns.dev](https://www.patterns.dev/): design, rendering and performance patterns.

## Key rules

- `9` `REACT-1` **Keep components and hooks pure. Side effects belong in event handlers or Effects.** ([react.dev, Keeping components pure](https://react.dev/learn/keeping-components-pure), [Rules of React](https://react.dev/reference/rules))
- `8` `REACT-2` **Keep state minimal.** Don't store what you can derive during render, and avoid duplicated or contradictory state. ([react.dev, Choosing the state structure](https://react.dev/learn/choosing-the-state-structure))
- `8` `REACT-3` **Don't use Effects to transform data or handle user events.** ([react.dev, You might not need an Effect](https://react.dev/learn/you-might-not-need-an-effect))
- `7` `REACT-4` **Put state where it's used, and lift it only as far as the closest common parent.** ([react.dev, Sharing state between components](https://react.dev/learn/sharing-state-between-components), [Dodds, Colocation](https://kentcdodds.com/blog/colocation))
- `7` `REACT-5` **Treat server state (fetched and cached data) separately from UI state, for example with TanStack Query.** ([TanStack Query overview](https://tanstack.com/query/latest/docs/framework/react/overview), [Dodds, Application state management with React](https://kentcdodds.com/blog/application-state-management-with-react))
- `7` `REACT-6` **Test the way users use the UI, not implementation details.** ([Testing Library, Guiding principles](https://testing-library.com/docs/guiding-principles))
- `6` `REACT-7` **Start new apps with a framework, or with a build tool such as Vite when you have specific constraints.** ([react.dev, Creating a React App](https://react.dev/learn/creating-a-react-app))
- `6` `REACT-8` **Try props and composition before reaching for context.** ([react.dev, Passing data deeply with context](https://react.dev/learn/passing-data-deeply-with-context))
- `6` `REACT-9` **Extract reusable stateful logic into custom hooks.** ([react.dev, Reusing logic with custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks))
- `6` `REACT-10` **Organise larger apps by feature, not by file type.** ([Bulletproof React, project structure](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md), [Feature-Sliced Design](https://feature-sliced.design/))
- `6` `REACT-11` **Move non-view logic (domain, data access) out of components as the app grows.** ([Modularizing React Applications with Established UI Patterns](https://martinfowler.com/articles/modularizing-react-apps.html))
- `6` `REACT-12` **Track Core Web Vitals as the user-facing performance budget.** ([web.dev, Web Vitals](https://web.dev/articles/vitals))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `8` [eslint-plugin-react-hooks](https://react.dev/reference/eslint-plugin-react-hooks): the official lint rules, including the React Compiler checks. [`purity`](https://react.dev/reference/eslint-plugin-react-hooks/lints/purity) flags impure components and hooks, and [`set-state-in-effect`](https://react.dev/reference/eslint-plugin-react-hooks/lints/set-state-in-effect) flags data transformed or state derived in Effects. Checks `REACT-1` and `REACT-3`, and partly `REACT-2`.
- `6` [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md): fails CI when lab metrics such as LCP, CLS and Total Blocking Time exceed your budget. Lab tests can't measure INP; [TBT is its lab proxy](https://web.dev/articles/vitals). Partly checks `REACT-12`.
- `5` [eslint-plugin-testing-library](https://testing-library.com/docs/ecosystem-eslint-plugin-testing-library/): flags tests that reach into DOM nodes or containers instead of using user-facing queries. Checks `REACT-6`.
- `5` [eslint-plugin-boundaries](https://www.jsboundaries.dev/docs/overview/): enforces which folders may import which, for example no imports across features, or from components into data access. Checks `REACT-10`, and partly `REACT-11`.

## Tutorials and further reading

- `6` [Micro Frontends](https://martinfowler.com/articles/micro-frontends.html) (Cam Jackson): when splitting a front end across teams is worth the cost.
- `6` [Server Components](https://react.dev/reference/rsc/server-components) (react.dev).
