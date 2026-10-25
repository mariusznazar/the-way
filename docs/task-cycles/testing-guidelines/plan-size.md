# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 1 | 277184 | 110874 | fits | — |
| 2 | 2 | 234970 | 93988 | fits | — |
| 3 | 4 | 381964 | 152786 | fits | — |
| 4 | 3 | 341143 | 136458 | fits | — |
| 5 | 5 | 133475 | 53390 | fits | — |
