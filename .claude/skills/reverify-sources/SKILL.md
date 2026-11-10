---
name: reverify-sources
description: Re-verify the oldest or failing sources in this Architecture Guidelines repository. Checks that each page still exists and still says what the guidelines cite it for, then updates its verified date, or fixes the rules and replaces the source when it changed or was retired. Use when asked to re-check, refresh or audit sources, when CI reports broken, retired or stale sources, or for periodic maintenance.
argument-hint: "[number of sources, default 20 | URL]"
---

# Re-verify sources

Sources drift. Pages move, get retired, or change their advice (for example, Unity 6.6 changed its domain-reload default). Each source in `sources.csv` has a `verified` date, the last time someone confirmed the page still supports what the guidelines cite it for.

## 1. Pick the batch

- If the user named URLs, use those.
- Otherwise start with the parked pages: the URLs in the "Temporarily unavailable" part of `exclude` in `lychee.toml`. The link checks skip them, so only this re-check notices when they're back.
- Then run `python3 scripts/verify_sources.py` and take every BROKEN, RETIRED, SUSPECT and MOVED source. MOVED means a permanent redirect (301 or 308): the link still works, but should point to the new address.
- Then fill the batch from `python3 scripts/verify_sources.py --stale --max-age 0`, oldest first. Default batch size: 20.

## 2. Check each source

1. Find where it's cited: its "Used in" files in `SOURCES.md`, or `grep -rn "<url>" general specific`.
2. Fetch the page. Confirm the final URL is the same page, not a home, 404 or "deprecated" page.
3. For each place it's cited, read the rule or entry and confirm the page **still says that**. Quote the supporting passage to yourself.

If the page is there:

- **Still supports everything**: set its `verified` column in `sources.csv` to today's date (YYYY-MM-DD).
- **Content changed**: reword the affected rules to match, or find a better source. Follow the `add-guideline` skill for new sources (verify, score). A rule keeps its ID when reworded.
- **It redirects permanently (MOVED)**: handle it as a moved page, in step 1 below.

If the page is broken, retired or missing, go through these steps in order, and stop at the first that applies:

1. **Look for a new address first.** Moving is the most common reason a page disappears, much more common than a page being retired, so don't park or remove a page until you have looked. Check:
   - redirects, and the site's home or news page for a move notice
   - whether other links to the same site broke too, which means the whole site moved, for example to a new domain or from GitHub to Codeberg
   - the project's repository README, or the archived repository's notice, for a new home
   - the site's own search or sitemap, and a web search for the page's title

   If you find the page at a new address, it **moved**. Update the link in the guideline files and `sources.csv`, keep its `#anchor`, and read the new page before relying on it. A new address can be less specific than the old page: rfc-editor.org, for example, redirects `/rfc/rfc9110` to an info page without the RFC's text, so link the full text, `/rfc/rfc9110.html`, instead. When a whole site moved, update all of its links in one go and check that each new address loads.
2. **Retired, with a successor or an equivalent**: the site marks the page as retired or names a successor, or another current official page covers the same points. Replace it, after reading the replacement.
3. **It may come back**: for example, only one language edition is gone, search engines still list the page, an older version of it still exists, or the site gives no retirement notice. Don't remove it. Keep it cited and park its exact URL in the "Temporarily unavailable" part of `exclude` in `lychee.toml`, with today's date and the reason.
4. **Nothing else applies**: ask the repository owner before removing the entry or the rule. A removed rule's ID is retired automatically and never reused.

For parked pages:

- **Back again**: check it as above, and remove it from the "Temporarily unavailable" list.
- **Still gone**: look for a new address again, as in step 1, since sites often move after a pause.
- **Parked for three months or more**: list it in your summary and ask the repository owner whether to keep waiting, cite another source or remove the entry.

Never update a `verified` date without reading the page.

## 3. Finish

```bash
python3 scripts/rank.py fix
python3 scripts/check_citations.py
python3 scripts/rank.py check
```

Summarise per source: verified unchanged, updated (what changed and in which rule IDs), replaced, parked or unparked, and any removal the owner needs to decide on.
