---
type: llm
weight: 2
---

The app has these planted problems:
(1) the `deleteUser` Server Action deletes any user without authenticating or authorizing the caller;
(2) the database connection string is exposed to the browser through a `NEXT_PUBLIC_` environment variable;
(3) the whole user row (including `password_hash` and `is_admin`) is passed to a Client Component;
(4) `'use client'` on the root layout turns the whole app into client code;
(5) plain `<img>` tags instead of `next/image`.

PASS if the review clearly identifies at least four of these five problems, including (1) and (2).
FAIL otherwise, or if it reports problems that aren't in the code.
