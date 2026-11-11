# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 2 | 50242 | 20097 | fits | — |
| 2 | 2 | 67605 | 27042 | fits | — |
| 3 | 3 | 122296 | 48919 | fits | — |
| 4 | 3 | 49643 | 19858 | fits | — |
| 5 | 2 | 21134 | 8454 | fits | — |
| 6 | 2 | 24366 | 9747 | fits | — |
| 7 | 4 | 63170 | 25268 | fits | — |
