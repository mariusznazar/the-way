# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 2 | 68681 | 27473 | fits | — |
| 2 | 2 | 33706 | 13483 | fits | — |
| 3 | 2 | 30296 | 12119 | fits | — |
| 4 | 4 | 109036 | 43615 | fits | — |
| 5 | 2 | 273482 | 109393 | fits | — |
| 6 | 2 | 272048 | 108820 | fits | — |
| 7 | 2 | 272479 | 108992 | fits | — |
| 8 | 1 | 32080 | 12832 | fits | — |
