<!-- rule-prefix: NEXTJS -->
# Next.js

Scope: web apps built with Next.js and the App Router, following the current (Next.js 16) documentation. These guidelines build on [React](../react/README.md): follow its rules for components, state and testing, and the rules here for rendering, data access, caching and the boundary between server and client code.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Next.js Docs: App Router](https://nextjs.org/docs/app): **the baseline.** The Getting Started chapters cover project structure, Server and Client Components, fetching and mutating data, caching, revalidating and error handling.
- `9` [How to think about data security in Next.js](https://nextjs.org/docs/app/guides/data-security): choosing a data-handling model, the Data Access Layer, Server Action security, tainting, and an audit checklist.
- `7` [How to optimize your Next.js application for production](https://nextjs.org/docs/app/guides/production-checklist): the official production checklist for rendering, data fetching, UI, security, metadata and bundle size.
- `7` [How to implement authentication in Next.js](https://nextjs.org/docs/app/guides/authentication): sessions, authorization in a Data Access Layer, and optional optimistic checks in Proxy.

## Key rules

- `9` `NEXTJS-1` **Treat every Server Action as a public endpoint: authenticate, authorize and validate its input inside the action.** Actions are reachable by direct POST requests, so checks in Proxy, a layout or the page that renders the form aren't enough. ([Next.js, Server Actions: Security](https://nextjs.org/docs/app/guides/server-actions#security), [Data security](https://nextjs.org/docs/app/guides/data-security), [Production checklist](https://nextjs.org/docs/app/guides/production-checklist))
- `9` `NEXTJS-2` **Give an environment variable the `NEXT_PUBLIC_` prefix only if its value may be public.** Next.js inlines these values into the client JavaScript at build time. Keep secrets unprefixed and out of the repository, as [general/security.md](../../general/security.md) requires. ([Next.js, Environment variables](https://nextjs.org/docs/app/guides/environment-variables), [Production checklist](https://nextjs.org/docs/app/guides/production-checklist))
- `8` `NEXTJS-3` **Put data access in a server-only Data Access Layer that checks authorization and returns minimal data transfer objects (DTOs).** Next.js recommends this model for new projects; choose one data-handling model and don't mix them. ([Next.js, Data security](https://nextjs.org/docs/app/guides/data-security), [Markbåge, How to Think About Security in Next.js](https://nextjs.org/blog/security-nextjs-server-components-actions))
- `8` `NEXTJS-4` **Pass Client Components, and return from Server Actions, only the fields the UI renders.** Props and action results are serialized and sent to the browser, so passing whole database records exposes private fields. ([Next.js, The Server and Client Boundary](https://nextjs.org/docs/app/guides/server-and-client-boundary), [Server Actions: Security](https://nextjs.org/docs/app/guides/server-actions#security))
- `7` `NEXTJS-5` **Add `import 'server-only'` to modules that use secrets or the database.** Importing such a module into a Client Component then fails the build. ([Next.js, Preventing environment poisoning](https://nextjs.org/docs/app/getting-started/server-and-client-components#preventing-environment-poisoning))
- `7` `NEXTJS-6` **Keep `"use client"` boundaries small: mark the interactive components, not whole layouts or pages, and pass server-rendered content to them as `children` or props.** Everything a `"use client"` file imports goes into the client bundle. ([Next.js, Reducing JS bundle size](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size), [Interleaving Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#interleaving-server-and-client-components))
- `7` `NEXTJS-7` **Decide caching per data source, and invalidate the cache in every mutation that changes the data.** With Cache Components, mark cached functions or components with `use cache` and give each a `cacheLife`; tag data that mutations change with `cacheTag`, and call `updateTag` or `revalidateTag` from the Server Action. ([Next.js, Caching](https://nextjs.org/docs/app/getting-started/caching), [Revalidating](https://nextjs.org/docs/app/getting-started/revalidating))
- `6` `NEXTJS-8` **Read data in Server Components and change it with Server Actions.** Don't fetch your own Route Handlers from Server Components, which adds a server request, and don't expect Server Actions to run in parallel: the client dispatches them one at a time. ([Next.js, Production checklist](https://nextjs.org/docs/app/guides/production-checklist), [Server Actions: Sequential dispatch](https://nextjs.org/docs/app/guides/server-actions#sequential-dispatch-on-the-client))
- `6` `NEXTJS-9` **Avoid request waterfalls: start independent requests in parallel, and stream slow parts behind `<Suspense>` or `loading.js`.** ([Next.js, Parallel data fetching](https://nextjs.org/docs/app/getting-started/fetching-data#parallel-data-fetching), [Streaming](https://nextjs.org/docs/app/getting-started/fetching-data#streaming))
- `6` `NEXTJS-10` **Return expected errors, such as failed validation, from Server Actions as values, and let `error.js` and `global-error.js` boundaries catch uncaught exceptions.** ([Next.js, Error handling](https://nextjs.org/docs/app/getting-started/error-handling))
- `6` `NEXTJS-11` **Use `next/image`, `next/font` and `next/script` instead of plain `<img>` tags, font links and script tags.** They serve correctly sized images in modern formats, self-host fonts without layout shift, and defer third-party scripts. ([Next.js, Image optimization](https://nextjs.org/docs/app/getting-started/images), [Font optimization](https://nextjs.org/docs/app/getting-started/fonts), [Production checklist](https://nextjs.org/docs/app/guides/production-checklist))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [`server-only` import guard](https://nextjs.org/docs/app/getting-started/server-and-client-components#preventing-environment-poisoning): built into Next.js, which fails the build when a Client Component imports a module marked with `import 'server-only'`. Checks `NEXTJS-5`, and partly `NEXTJS-3`.
- `7` [eslint-config-next](https://nextjs.org/docs/app/api-reference/config/eslint): the official ESLint config; use its `core-web-vitals` preset. `@next/next/no-img-element`, `google-font-display`, `no-page-custom-font` and `no-sync-scripts` flag plain images, badly loaded fonts and blocking scripts. Checks `NEXTJS-11`.
- `6` [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md): fails CI when lab metrics such as LCP and CLS, or a resource budget such as `resource-summary:script:size`, exceed your limits. Partly checks `NEXTJS-6` and `NEXTJS-11`.

## Tutorials and further reading

- `7` [Next.js Learn: App Router course](https://nextjs.org/learn/dashboard-app): the free official course, which builds a full-stack dashboard with a database, mutations, error handling and authentication.
- `7` [How to Think About Security in Next.js](https://nextjs.org/blog/security-nextjs-server-components-actions) (Sebastian Markbåge, 2023): the original article behind the data security guide, with an audit checklist.
- `7` [The Server and Client Boundary](https://nextjs.org/docs/app/guides/server-and-client-boundary) (Next.js): how the server and client module graphs, serialized props and rendering environments fit together.
