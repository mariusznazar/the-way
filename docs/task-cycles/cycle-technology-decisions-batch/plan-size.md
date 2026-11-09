# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 2 | 58779 | 23512 | fits | — |
| 2 | 2 | 40122 | 16049 | fits | — |
| 3 | 4 | 86008 | 34404 | fits | — |
| 4 | 3 | 92860 | 37144 | fits | — |
| 5 | 1 | 47812 | 19125 | fits | — |
| 6 | 7 | 99406 | 39763 | fits | — |
| 7 | 4 | 40662 | 16265 | fits | — |
| 8 | 3 | 42539 | 17016 | fits | — |
| 9 | 1 | 22044 | 8818 | fits | — |
| 10 | 1 | 29147 | 11659 | fits | — |
| 11 | 1 | 42095 | 16838 | fits | — |
