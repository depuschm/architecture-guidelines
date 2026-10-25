<!-- rule-prefix: WEB -->
# Web front end (framework-independent)

Scope: any web front end, whatever the framework or build tool, with a focus on accessibility, performance, security and resilience. Framework-specific rules are in [React](../react/README.md), and the [general guidelines](../../general/README.md) still apply.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) (W3C Recommendation): **the baseline for accessibility.** Testable success criteria at levels A, AA and AAA.
- `9` [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) (W3C WAI): patterns for custom widgets such as tabs, menus, comboboxes and dialogs, with the roles, states and keyboard support each one needs.
- `9` [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) (OWASP): **the baseline for XSS defences**, including output encoding, HTML sanitization, safe sinks and the escape hatches in frameworks.
- `8` [The most effective ways to improve Core Web Vitals](https://web.dev/articles/top-cwv) (web.dev): the highest-impact fixes for loading, responsiveness and layout stability, in priority order.
- `8` [HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html) (OWASP): which security headers to send, with recommended values.
- `8` [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) (OWASP): how to build, deploy and test a CSP.
- `7` [Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) (MDN): guides and references for accessible HTML, CSS, JavaScript and ARIA.
- `7` [Baseline](https://web.dev/baseline) (web.dev): which web platform features work across the core browsers, as Newly or Widely available.
- `7` [Web Vitals](https://web.dev/articles/vitals) (web.dev): the Core Web Vitals (LCP, INP and CLS), their "good" thresholds and how to measure them.

## Key rules

### Accessibility

- `9` `WEB-1` **Target WCAG 2.2 Level AA as the minimum for every page and component.** It's the level that public-sector rules such as the UK government's require. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/), [GOV.UK Service Manual, Understanding WCAG 2.2](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag))
- `9` `WEB-2` **Use native HTML elements, such as `button`, `a`, `input` and `select`, before ARIA.** Native elements come with keyboard support, roles and states. If you give an element an ARIA role instead, you have to build the behaviour that role promises yourself. ([MDN, ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA), [APG, Read me first: No ARIA is better than bad ARIA](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/))
- `7` `WEB-3` **Run automated accessibility checks in CI, and also test by hand with a keyboard and a screen reader.** Automated checks find only part of the problems: axe-core finds 57% of WCAG issues on average. ([axe-core](https://github.com/dequelabs/axe-core), [MDN, Accessibility tooling and assistive technology](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Tooling))

### Performance

- `7` `WEB-4` **Measure Core Web Vitals from real users at the 75th percentile, separately for mobile and desktop, and set priorities from that field data.** Use lab tests, which are reproducible, to debug and to compare changes. ([web.dev, Web Vitals](https://web.dev/articles/vitals), [web.dev, Why lab and field data can be different](https://web.dev/articles/lab-and-field-data-differences))
- `7` `WEB-5` **Ship less JavaScript: split off code that the first render doesn't need, remove unused code, and use Baseline platform features instead of JavaScript reimplementations.** ([web.dev, The most effective ways to improve Core Web Vitals](https://web.dev/articles/top-cwv))
- `7` `WEB-6` **Give every image and embed explicit dimensions, offer sizes that fit the layout with `srcset` and `sizes`, and lazy-load only images outside the initial viewport.** ([web.dev, The most effective ways to improve Core Web Vitals](https://web.dev/articles/top-cwv), [web.dev, Browser-level image lazy loading](https://web.dev/articles/browser-level-image-lazy-loading), [web.dev, Responsive images](https://web.dev/learn/design/responsive-images))
- `7` `WEB-7` **Put a content hash or version in the URLs of static assets and cache them for a long time with `immutable`, and serve HTML with `Cache-Control: no-cache` (plus `private` when it's personalised) so that it's always revalidated.** ([MDN, HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching))

### Security

- `9` `WEB-8` **Render untrusted data through the framework's automatic escaping or `textContent`, and sanitize it with DOMPurify before it reaches an HTML sink such as `innerHTML` or React's `dangerouslySetInnerHTML`.** ([OWASP, Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [OWASP, DOM based XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html))
- `7` `WEB-9` **Send security headers with every response: `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, a `Referrer-Policy`, and the CSP `frame-ancestors` directive against framing.** ([OWASP, HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html))
- `7` `WEB-10` **Add a strict, nonce- or hash-based Content Security Policy as a second layer of defence against XSS, and try it in `Content-Security-Policy-Report-Only` mode before enforcing it.** ([OWASP, Content Security Policy](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html), [web.dev, Mitigate XSS with a strict CSP](https://web.dev/articles/strict-csp))
- `6` `WEB-11` **Load third-party scripts with Subresource Integrity, or serve your own reviewed copies.** ([MDN, Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity), [OWASP, Third Party JavaScript Management](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html))

### Compatibility and resilience

- `6` `WEB-12` **Choose a Baseline target, such as Baseline Widely available, from your users' browser data, and set it once in Browserslist so that build and lint tools share it.** ([web.dev, How to choose your Baseline target](https://web.dev/articles/how-to-choose-your-baseline-target), [web.dev, Use Baseline with Browserslist](https://web.dev/articles/use-baseline-with-browserslist))
- `5` `WEB-13` **Build core user journeys with progressive enhancement: HTML that works on its own first, then CSS and JavaScript that enhance it, so that a script that fails to load doesn't stop users.** ([GOV.UK Service Manual, Building a robust frontend using progressive enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement), [MDN, Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [axe-core rules](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md): automated checks tagged by WCAG version and level, including `aria-allowed-role`, `aria-required-children` and `nested-interactive` for misused ARIA. Run them in end-to-end tests with [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md). Partly checks `WEB-1`, `WEB-2` and `WEB-3`.
- `6` [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md): fails CI when lab metrics, resource sizes such as total script bytes, or individual audits such as `unsized-images` miss your assertions. Lab tests can't measure INP. Partly checks `WEB-4`, `WEB-5` and `WEB-6`.
- `6` [Size Limit](https://github.com/ai/size-limit): fails CI when the size or estimated download and run time of your JavaScript, dependencies included, exceeds a budget. Partly checks `WEB-5`.
- `6` [eslint-plugin-no-unsanitized](https://github.com/mozilla/eslint-plugin-no-unsanitized) (Mozilla): flags assignments to `innerHTML` and calls such as `insertAdjacentHTML` or `document.write` that don't go through an escaping function. Partly checks `WEB-8`.
- `6` [HTTP Observatory CLI](https://github.com/mdn/mdn-http-observatory) (MDN): scans a deployed site and grades its CSP, HSTS, `X-Content-Type-Options`, framing protection, `Referrer-Policy`, cookies and Subresource Integrity. Run it against a staging deployment in CI. Checks `WEB-9`, and partly `WEB-10` and `WEB-11`.
- `6` [@eslint/css `use-baseline`](https://github.com/eslint/css/blob/main/docs/rules/use-baseline.md): flags CSS properties, values, at-rules and selectors outside your Baseline target, unless they're guarded with `@supports`. Partly checks `WEB-12`.
- `5` [eslint-plugin-compat](https://github.com/amilajack/eslint-plugin-compat): flags JavaScript web APIs that the browsers in your Browserslist config don't support. Partly checks `WEB-12`.

## Tutorials and further reading

- `7` [Learn Performance](https://web.dev/learn/performance) (web.dev): a course on web performance concepts and techniques, from resource loading to images, fonts and JavaScript.
- `7` [Learn Accessibility](https://web.dev/learn/accessibility) (web.dev): an evergreen course and reference on accessible design and development.
- `7` [Accessibility on the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) (MDN Learn): a module on accessible HTML, CSS, JavaScript, WAI-ARIA and testing with assistive technology.
- `6` [Learn Images](https://web.dev/learn/images) (web.dev): an in-depth course on image formats, compression and responsive images.
