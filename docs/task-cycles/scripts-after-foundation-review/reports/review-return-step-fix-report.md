PASS b84bc4a23dface495ec57682c28f3b276b789b42

# Review of the fix of the return step's blocking finding

Range `8c6d6688cc9eff8a839ee4718bad435fb5583fcc..b84bc4a23dface495ec57682c28f3b276b789b42`; `git rev-parse HEAD` is the head. One commit, one file: `foundations/decisions.md` (WAY-344, clause `tests:` of *Verification*).

## The finding of the findings file

**1. Important (blocking), the clause `tests:` of WAY-344 lists the register of problems among the files whose missing field gives exit code 1 — fixed.**
The word-level diff of the fix removes exactly "register of problems," and changes "gate times," to "gate times or"; the rest of the changed lines is a re-filling of the paragraph, with no word added or dropped (checked with `git diff --word-diff`). The clause now reads "at a field missing in the file of the measures, the file of the gate times or a stage report, gives the values that need it as unknown, writes its result and ends with exit code 1 and a line `Error:`". The register stays in the clause only through "a table of weights or of the costs of an occurrence which lacks a level gives the result, unknown values and the line `Error:` that names the level", which the code does (`check_levels` and `main` write the result and give exit 1) and which the two tests of a missing level hold (tagged with a line `decision:`). The register's exit 2 for a missing heading, table or column is now stated only in the *Rationale*, as before the return step; no sentence of the entry or of the clause contradicts `register_table` / `read_register` / `main` (`audit_count.py`) or `test_a_register_lacking_a_field_ends_the_run_with_an_error_naming_it`. The defect no longer exists on the new head.

## New findings in the fix diff

None. The change touches no code, no test, no line `decision:`, no sentence of the binding paragraphs, and no invariant; the meaning of the decision is unchanged and the entry is edited in place (WAY-07). The longest line of the re-filled paragraph is 100 columns, as the neighbouring lines.

Minor findings 2 and 3 of the earlier report are not in the findings file and were not fixed, as the method gives; they stay as Minor notes and block nothing.

## WAY-03

No test altered; no line `decision:` added, moved or dropped by the fix.

## Checks

- `python -B elements/common/foundation_check.py`: exit 0, "0 errors"; one `listed:` line, for `guidelines-file-place` (a sentence changed by an earlier commit of the change, as before the fix).
- `git diff --word-diff=porcelain --word-diff-regex='[^[:space:]]+' <base>..<head>`: shows only the removal of "register of problems," and "times," becoming "times or", plus line re-filling: exit 0.
- Not run: any test (the fix changes no code and no test); the report of the fix states it ran `test_a_register_lacking_a_field` and `lacks_a_level` (3 tests, exit 0), which I ran myself in the first review.

## Reaches beyond the handoff

None.

## Working copies

None made; no `.runs/review-return/` directory left.

## Unread material

- `reports/return-step-fix-report.md` and the findings file were read whole. The decision WAY-344 was read whole in the first review and the changed paragraph again here; WAY-339 is untouched by the fix and was not reread.
- `process-audit/audit_count.py` was not reread; I relied on my first review's reading of `register_table`, `read_register` and `main`.

## Searches not found or unclear

none
