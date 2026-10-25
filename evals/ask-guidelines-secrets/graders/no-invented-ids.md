---
type: regex
# DOTNET has rules 1-12 and SEC has 1-9 (see RULES.md). Update these ranges when rules are added.
pattern: '\b(DOTNET-(1[3-9]|[2-9][0-9]|0)|SEC-(1[0-9]|[2-9][0-9]|0))\b'
match: not_contains
---
