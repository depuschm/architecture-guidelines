---
type: regex
# At least four Rel(from, to, "label", "technology") calls: the C4 notation rules ask for technology on relationships.
pattern: '(Rel\(\s*\w+\s*,\s*\w+\s*,\s*"[^"]+"\s*,\s*"[^"]+"[\s\S]*){4}'
---
