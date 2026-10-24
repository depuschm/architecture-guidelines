---
name: add-guideline
description: Add or update a guideline in this Architecture Guidelines repository, the reference-first way. Finds and adopts existing authoritative guides before writing new rules, verifies every link, keeps the file format, updates the indexes, and runs the citation check. Use when asked to add a topic, rule, source, tutorial or new platform folder (for example "add Godot guidelines" or "add a rule about caching").
argument-hint: "[topic or platform]"
---

# Add a guideline

Follow [CONTRIBUTING.md](../../../CONTRIBUTING.md). This skill turns it into steps.

## 1. Place it

- Technology-independent → a file in `general/`. Extend an existing file before creating a new one.
- Platform or service → `specific/<platform>/`. For a new platform, copy `specific/_template/README.md` to `specific/<platform>/README.md`.

## 2. Find existing guidance first

Search for authoritative sources, in this order: official vendor documentation, standards, recognised practitioners' primary publications, then maintained community guides.

- **If a source covers the topic well**, add it under **Adopted references** with a one-line description. Don't restate it.
- **Write a Key rule only if** no single source covers the point, sources disagree, or a choice has to be made. Every rule still needs a supporting link.

## 3. Verify every link

For each URL you add:

1. Fetch it and confirm it loads (HTTP 200 after redirects). Watch for soft 404s, where the site redirects to its home page or shows a "not found" page with status 200.
2. Confirm the page actually supports the statement you attach to it. Quote it to yourself before writing the rule.
3. If the URL permanently redirects, use the final, canonical URL.
4. Link to the most specific page, not a site's home page.

Never add a URL from memory without fetching it.

## 4. Write it in the house format

```markdown
- **Short imperative rule.** One sentence of explanation. ([Source title](https://…))
```

Every list item in `general/` and `specific/` needs at least one link. Keep rules to one or two sentences.

## 5. Update the indexes (new files or platforms)

- `README.md`: the general or specific table.
- `general/README.md` or `specific/README.md`.
- For a new platform: the detection table in `skills/architecture-review/SKILL.md`.

## 6. Check

```bash
python3 scripts/check_citations.py
lychee --config lychee.toml './**/*.md'   # if lychee is installed
```

Fix any failures. Then summarise what you added and list every new source URL.
