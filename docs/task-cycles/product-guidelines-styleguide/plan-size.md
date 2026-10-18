# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 2 | 379930 | 151972 | fits | — |
| 2 | 2 | 315201 | 126081 | fits | — |
| 3 | 2 | 263656 | 105463 | fits | — |
| 4 | 4 | 437927 | 175171 | fits | — |
| 5 | 10 | 112663 | 45066 | fits | — |
| 6 | 10 | 112619 | 45048 | fits | — |
| 7 | 10 | 112965 | 45186 | fits | — |
| 8 | 3 | 224772 | 89909 | fits | — |

Command, from the worktree root at `8ea4679` (foundation stage closed): `python -B task-cycle/slice_size.py .runs/task-cycles/product-guidelines-styleguide/plan.md` — exit code 0.
