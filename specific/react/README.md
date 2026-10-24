# React

Scope: web front ends built with React, either on their own or inside a framework.

## Adopted references

- [react.dev: Learn React](https://react.dev/learn): **the baseline.** The official tutorial covers component design and state management.
- [Rules of React](https://react.dev/reference/rules): rules that React code must follow to behave correctly.
- [Thinking in React](https://react.dev/learn/thinking-in-react): the official method for breaking a UI into components and state.
- [Bulletproof React](https://github.com/alan2207/bulletproof-react): an opinionated, production-ready project architecture.
- [Patterns.dev](https://www.patterns.dev/): design, rendering and performance patterns.

## Key rules

- **Start new apps with a framework, or with a build tool such as Vite when you have specific constraints.** ([react.dev, Creating a React App](https://react.dev/learn/creating-a-react-app))
- **Keep components and hooks pure. Side effects belong in event handlers or Effects.** ([react.dev, Keeping components pure](https://react.dev/learn/keeping-components-pure), [Rules of React](https://react.dev/reference/rules))
- **Keep state minimal.** Don't store what you can derive during render, and avoid duplicated or contradictory state. ([react.dev, Choosing the state structure](https://react.dev/learn/choosing-the-state-structure))
- **Put state where it's used, and lift it only as far as the closest common parent.** ([react.dev, Sharing state between components](https://react.dev/learn/sharing-state-between-components), [Dodds, Colocation](https://kentcdodds.com/blog/colocation))
- **Don't use Effects to transform data or handle user events.** ([react.dev, You might not need an Effect](https://react.dev/learn/you-might-not-need-an-effect))
- **Try props and composition before reaching for context.** ([react.dev, Passing data deeply with context](https://react.dev/learn/passing-data-deeply-with-context))
- **Treat server state (fetched and cached data) separately from UI state, for example with TanStack Query.** ([TanStack Query overview](https://tanstack.com/query/latest/docs/framework/react/overview), [Dodds, Application state management with React](https://kentcdodds.com/blog/application-state-management-with-react))
- **Extract reusable stateful logic into custom hooks.** ([react.dev, Reusing logic with custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks))
- **Organise larger apps by feature, not by file type.** ([Bulletproof React, project structure](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md), [Feature-Sliced Design](https://feature-sliced.design/))
- **Move non-view logic (domain, data access) out of components as the app grows.** ([Modularizing React Applications with Established UI Patterns](https://martinfowler.com/articles/modularizing-react-apps.html))
- **Test the way users use the UI, not implementation details.** ([Testing Library, Guiding principles](https://testing-library.com/docs/guiding-principles))
- **Track Core Web Vitals as the user-facing performance budget.** ([web.dev, Web Vitals](https://web.dev/articles/vitals))

## Tutorials and further reading

- [Micro Frontends](https://martinfowler.com/articles/micro-frontends.html) (Cam Jackson): when splitting a front end across teams is worth the cost.
- [Server Components](https://react.dev/reference/rsc/server-components) (react.dev).
