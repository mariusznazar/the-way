# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 3 | 396463 | 158586 | fits | — |
| 2 | 4 | 179729 | 71892 | fits | — |
| 3 | 5 | 363896 | 145559 | fits | — |
| 4 | 3 | 183360 | 73344 | fits | — |
| 5 | 10 | 295854 | 118342 | fits | — |
| 6 | 10 | 295182 | 118073 | fits | — |
| 7 | 10 | 290478 | 116192 | fits | — |
