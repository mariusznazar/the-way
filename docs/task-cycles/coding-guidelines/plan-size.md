# Plan size — coding-guidelines

- Command, from the repository root `/home/user/the-way` at `64344a3` (foundation stages closed; ruling C23): `python3 -B task-cycle/slice_size.py docs/task-cycles/coding-guidelines/plan.md`
- Python: 3.13.16 (the repository declares 3.14; cycle choice O3)
- Exit code: 0 (every slice fits)
- Measured: 2026-10-18, with every foundation range recomputed at `64344a3` and F4's test files as they stand there. Still to be added before dispatch (plan table "Reads that move or appear…"): S1's `product-guidelines/template.md` growth (about 2 000 estimated tokens; S2–S6), S2's `product-guidelines/coding/template.md` (at most about 10 000; S3, S4, S6), S6's `product-guidelines/coding/SKILL.md` (about 7 000; S7–S11). Estimated after them: S2 about 218 000, S4 about 197 000, S6 about 188 000, S3 about 176 000, S11 about 100 000, S1 101 000, S5 about 87 000, S7–S10 about 53 000 each — all under 250 000.

## Report

# Slice sizes

Too large: more than 250000 estimated tokens to read, a quarter of a 1000000-token context window at 2.5 characters a token, or more than 10 files to change.

| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |
|---|---|---|---|---|---|
| 1 | 1 | 251970 | 100788 | fits | — |
| 2 | 3 | 540809 | 216324 | fits | — |
| 3 | 2 | 411197 | 164479 | fits | — |
| 4 | 2 | 463556 | 185423 | fits | — |
| 5 | 1 | 212148 | 84860 | fits | — |
| 6 | 4 | 440359 | 176144 | fits | — |
| 7 | 8 | 114108 | 45644 | fits | — |
| 8 | 8 | 113742 | 45497 | fits | — |
| 9 | 8 | 114344 | 45738 | fits | — |
| 10 | 8 | 114052 | 45621 | fits | — |
| 11 | 3 | 231793 | 92718 | fits | — |
exit code: 0
