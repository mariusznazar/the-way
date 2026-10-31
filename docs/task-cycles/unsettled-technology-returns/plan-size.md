# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 8 | 361674 | 144670 | fits | — |
| 2 | 7 | 245875 | 98350 | fits | — |
| 3 | 4 | 235486 | 94195 | fits | — |
| 4 | 5 | 260531 | 104213 | fits | — |
| 5 | 5 | 282480 | 112992 | fits | — |
| 6 | 3 | 255351 | 102141 | fits | — |
