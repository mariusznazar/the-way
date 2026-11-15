PASS 61171e9fd7d0be708b3e16e0ecdba64c83728fd8

# Review of the fix of slice 9's blocking finding (range b6f800c..61171e9, one commit)

`git rev-parse HEAD` is `61171e9fd7d0be708b3e16e0ecdba64c83728fd8`, the head given. Read: `reports/slice-9-findings.md`, `reports/executor-9-fix-report.md`, `task-cycle/review/fix.md`, and the diff of the range computed by me.

## The finding of the findings file

**I1 (Important) — fixed.** The values of the ancestry check (`Process pin` of a fixed issue) and the per-issue values (`the fix of issue ...`, `waiting of issue ...`) are no longer in the pair table. `analyse` now keeps two lists: `held` (`register.refused` and the problems whose cycle is not read) and `unknown` (every other value); `Analysis` has the new field `held`; `render` writes `analysis.unknown + versions.unknown + measured.unknown` (deduplicated, in order) into the first table, one row each, and groups only `analysis.held` into the pair table. The sentence of the module description, the sentence of the list of sections, the comment on `EXAMPLES` and the intro paragraph of the section now say that the register's held-back values are grouped and their full list stays in the register, and that every other unknown value is given in full; that agrees with the code. The defect (loss of the cycle, repository and reason of every pin beyond three, with a false claim that the register keeps them) no longer exists on the new head.
Evidence: the diff of `analyse` and `render`; the new test `RegisterCount.test_each_cycle_whose_pin_is_unknown_for_a_fixed_issue_keeps_its_own_row` has four cycles (more than the three examples of a pair), asserts each one's own row `[product, cycle, "Process pin"]` in the first table in order, the reason `lacks commit` in each, and no `Process pin` row in the pair table; it would fail on the grouping of `b6f800c` (the executor's red run on that commit: exit 1, 1 failure, which I did not repeat). The four tests of the per-row values (`Process pin`, `ambiguous`, shallow clone, `the fix of issue`) read the first table again, as before the slice.

## What the fix broke

Nothing Critical or Important. Looked at: `Analysis(...)` is built in one place only (`grep`), so the new field has no other constructor to miss; the pair table still takes the same two kinds of value as before (refused rows and problems of an unread cycle), so its tests, the 830-row test and the crafted-text test, still hold; the first table now also holds `analysis.unknown`, whose cells go through `cell()` as the versions' did, so no new unescaped text reaches the result; the output stays deterministic (lists deduplicated by `dict.fromkeys`, insertion-ordered).

## Minor (blocks nothing)

- M1 of the slice review (one line for each issue) no longer applies: the per-issue values are back in the first table, one row each, as they were before the slice. Nothing left of it.
- The executor's report says the test the findings file named does not exist under that name; the findings file wrote a shortened name of `test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side`. No effect.

## Declined to judge

- `process-audit/SKILL.md` lines 161-162 (the stale statement about row `<n>` of *Problems*) stay with the later slice of the plan that brings that file to the count (`plan.md` line 117), as in the slice review.

## WAY-03

No invariant test and no test holding a `decision:` line changed. Four tests that the slice changed to read the pair table read the first table again; one test added.

## Checks run

1. `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` — 228 tests, `OK`, exit 0 (the output went to a file under `.runs/`, removed afterwards).
2. The focused command of the slice (`-k Run -k RegisterCount -k CraftedInput`) I did not run again: the whole file, which includes it, passed on the head. The executor's red run and its test of the series script (`test_audit_series_scripts.py`) I did not repeat.
3. No run of the whole gate (WAY-160).

## Reach beyond the dispatch

None beyond the files the handoff names and the plan line 117 (already read in the slice review).

## Unread material

`process-audit/audit_count.py` read in the diff of the range and the unchanged lines around it, not whole; `process-audit/test_audit_count.py` read in the diff of the range. `reports/review-9-report.md` is my own earlier report. The executor's logs under `reports/` were not opened.

## Searches not found or unclear

none

## Working copies

None made for this review. A log file I wrote to `.runs/review-9-whole.txt` was removed. `.runs/review-9/` (the scratch of the slice review) was removed earlier. No wait-timer or background watcher is left running: the one background command of this review finished (exit 0).
