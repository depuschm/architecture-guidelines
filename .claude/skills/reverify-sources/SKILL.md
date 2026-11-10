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
- Then run `python3 scripts/verify_sources.py` and take every BROKEN, RETIRED and SUSPECT source.
- Then fill the batch from `python3 scripts/verify_sources.py --stale --max-age 0`, oldest first. Default batch size: 20.

## 2. Check each source

1. Find where it's cited: its "Used in" files in `SOURCES.md`, or `grep -rn "<url>" general specific`.
2. Fetch the page. Confirm the final URL is the same page, not a home, 404 or "deprecated" page.
3. For each place it's cited, read the rule or entry and confirm the page **still says that**. Quote the supporting passage to yourself.

Then:

- **Still supports everything**: set its `verified` column in `sources.csv` to today's date (YYYY-MM-DD). If it moved permanently, replace the URL with the new canonical one in the guideline files and `sources.csv`.
- **Content changed**: reword the affected rules to match, or find a better source. Follow the `add-guideline` skill for new sources (verify, score). A rule keeps its ID when reworded.
- **Unavailable, but it may come back**: for example, only one language edition is gone, search engines still list the page, an older version of it still exists, or the site gives no retirement notice. Don't remove it. Keep it cited and park its exact URL in the "Temporarily unavailable" part of `exclude` in `lychee.toml`, with today's date and the reason.
- **A parked page is back**: check it as above, and remove it from the "Temporarily unavailable" list.
- **Moved or retired for good**: the site redirects to a new page, names a successor, or marks the page as retired. Replace it with the new page or an equivalent current source.
- **No replacement exists**: ask the repository owner before removing the entry or the rule. A removed rule's ID is retired automatically and never reused.

Never update a `verified` date without reading the page.

## 3. Finish

```bash
python3 scripts/rank.py fix
python3 scripts/check_citations.py
python3 scripts/rank.py check
```

Summarise per source: verified unchanged, updated (what changed and in which rule IDs), replaced, parked or unparked, and any removal the owner needs to decide on.
