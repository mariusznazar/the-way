# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 3 | 71324 | 28530 | fits | — |
| 2 | 2 | 41354 | 16542 | fits | — |
| 3 | 2 | 44881 | 17953 | fits | — |
