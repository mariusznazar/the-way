PASS 2f9c200b88d6c0ddcc48ee0dc61d4d24f03a0f90

# Review of the correction for the human's remarks (request 106)

Range `e00264a..2f9c200` (`a686244`, `ab12299`, `72904f7`, `2f9c200`). `git rev-parse HEAD` printed `2f9c200b88d6c0ddcc48ee0dc61d4d24f03a0f90`. Method: `review-change`, `task-cycle/review/fix.md` for a correction (the remarks stand in the place of a findings file). Worktree and index untouched.

Blocking findings: none. Minor: 3. Out of scope: 0.

## Each remark: made or not

1. **Registry that never forgets a far-future entry: made.** `task-cycle/gate_times.py:192-198` (`malformed`), `:211` (`prepare` deletes it like a stale one), `:236-237` (`count_others` skips it even where deletion fails). Crafted run (scratch script, real `gate_times.py` with `--registry` on a scratch folder, exit 0): entries with an end 10^13 ms ahead, a start and end far ahead, an end before the start, a running entry 10 hours ahead, an end 2 hours ahead, 10^30 / 10^31, and `0_0_x.run` were all deleted; an end 30 s ahead, a valid running entry and a valid ended one stayed; a running entry 7 hours old was deleted as before; `junk.run` was left alone; the run's count was `2` (the two valid entries), so the far-future entry no longer counts. Ruling 1 is followed (one minute of slack, a running entry older than six hours as before, other names left alone). Both new tests assert this and the second one covers a malformed entry that cannot be deleted (a directory in its place).
2. **Flood of `unknown` lines: made.** `process-audit/audit_count.py:2411-2419` (mechanism) and `:2460-2468` (gate): a version with no value in any measure (no run with any time) has one row with `—` in the measure column and one line in *Unknown values*. Crafted objects (scratch script calling `mechanism_rows`, `gate_rows`, `gate_values`): an empty first version, an empty middle version, versions whose only run gives no time, and an empty last version each give one row and one line; a version with a value keeps its per-measure rows; the version after an empty one is compared with nothing and says so (`no cycle of the previous version gives a value`), as ruling 2 keeps a version with values as it is. The real-history figures of the report (944 to 160 lines in *Measure versions*, 1614 to 830 in *Unknown values*) I did not reproduce; they are the author's and unverified here (see Checks).
3. **Failed run in the gate median: made.** `audit_count.py:2441` (`side = 0 if run.others == 0 and run.code == 0 else 1`); `GateRun.code` is read at `:1600-1601` from a column that `GATE_CODE` limits to ten digits, so `int` cannot raise. Crafted: a run with exit code 2, a run with unknown code, a run with unknown count, one with another gate and one passed alone: only the passed one is on the compared side, the other four are apart; a failed run is no longer in any median or *Falls*. A version whose only run failed has no median and no comparison (`no run of the version that passed with no other gate`). Columns renamed *Runs compared* and *Runs not compared*; the opening lines (`:2652-2660`), the docstring (`:135-141`) and `process-audit/SKILL.md:186-191` say so. A run row of the wrong number of cells gives `GateRun(None, None)`, `code` None, and adds to neither side, as before.
4. **No instruction for a failing measuring script: made.** `task-cycle/skill/SKILL.md:468-473` (step 12): record the command, exit code and `Error:` line under *Verification* and in *Checks* as a check that did not run, fix the call where it was wrong and run again, never write the file by hand, a missing file stays missing. Step 10 (`:381`) points to it where it names the gate script's exit code 2. `audit_count.py:1442-1445` gives the reason "an earlier cycle, or a script that failed (the record's *Verification* says which)"; `process-audit/SKILL.md:163-164` says it in one sentence. `request_template.md` has *Checks*, so the instruction's reference resolves.

## What the correction could have broken

- The missing-field mechanism (exit 1, result written, `Error:`) is not touched: the diff holds no change in `missing_in`, `read_measures` or the error path; `MechanismMeasures` and `GateRunsMeasures` pass.
- The series of the cost and the older-form readings of the stage report: no changed line in `stages_*`, `cost` or the stage readers; the diff in `audit_count.py` is confined to the docstring, `GateRun`, `read_optional`, `read_gate`'s `GateRun(...)` call, and the measure-version tables and lines.
- `task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec`: `git diff --quiet 2292f33... HEAD -- <those>` exit 0. `TREE_PATHS`: no line of the range holds the name.
- Trust boundary (the registry folder and the `gate_times.md` file are outside input): hostile registry names with 10^30 numbers parse as `int` and are deleted, not counted; no exception reached the user in the crafted run (exit 0, empty stderr). The audit's `code` column is bounded to ten digits.

## `foundations/decisions.md` WAY-350 (`:11599`)

Binding paragraph, *Verification*, *Rationale* and *Rejected* say what the code does: compared runs are those that passed (exit 0) with none alongside; failed runs, runs with an unknown exit code (and with unknown count, as the code and the table's opening lines say) are listed apart; a version whose every run had company or failed has no median; an entry with an impossible time is deleted and counted for nothing. The paragraph names "the runs that passed" and "the runs whose exit code is unknown" in *Verification*, and the unknown count remains covered by the unchanged "no other such run was going". Not wider than the code: the clause on malformed entries says "an end in the far future, deleted and counted for nothing", while the code also deletes a start in the future and a reversed pair, which is wider in the code than in the entry, not the reverse (see Minor 3). `python -B elements/common/foundation_check.py`: exit 0, "0 errors". The author's claim that WAY-348, WAY-339 and WAY-349 hold no sentence about which runs are compared I did not re-search; I read only WAY-350 whole.

## Minor findings (block nothing)

1. `process-audit/audit_count.py:371` (comment): "A copy holding neither is an earlier form." now disagrees with the docstring at `:171-172` and the reason at `:1442-1445`, which say it may be a script that failed. Left stale by the correction. Fix: the same words as the reason.
2. `process-audit/audit_count.py:172` (172 characters) and `task-cycle/gate_times.py:28` (136 characters): the edit joined lines in a paragraph that the file otherwise wraps near 100 characters; the previous head had none over 110 in `gate_times.py` and one in `audit_count.py` (`:2810`, a test line, 120). Style only.
3. `foundations/decisions.md:11604` WAY-350 names only "an end in the far future" as the example of an entry whose times cannot be. The code (and `gate_times.py` docstring) delete also a start more than a minute ahead and an end before its start. "Such as" makes the entry an example, so it does not contradict the code; a reader of the entry alone may not learn the three cases. Not a restatement that is wider or narrower than the code.

## Declined to judge

- The 16 lines of *Unknown values* that the first version with values after a run of empty versions still gives (`no cycle of the previous version gives a value`, one for each measure): the author's chosen and rejected way is in the report, and ruling 2 says a version with at least one value keeps its rows as they are.
- The remaining per-cycle `unknown` lines (*Fix rounds share*, *Mechanism measures*, *Gate runs* and others): not among the four remarks.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`, `git log e00264a..2f9c200`, `git diff e00264a..2f9c200` | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (24 tests) | 0 |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions -k MechanismMeasures -k GateRunsMeasures` (31 tests; the class `MechanismMeasures` holds the test of the new absent-file reason) | 0 |
| `python -B elements/common/foundation_check.py` ("0 errors") | 0 |
| `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |
| Crafted registry: scratch `reg.py` (twelve entry names) against `task-cycle/gate_times.py --registry` | 0 (output as in remark 1) |
| Crafted gate and mechanism series: scratch `crafted.py` calling `gate_values`, `gate_rows`, `mechanism_rows` of `audit_count` (failed, unknown-code, unknown-count and company runs; empty first, middle and last versions) | 0 (output as in remarks 2 and 3) |
| Scratch scripts: `a scratch script in the session's scratchpad` and `.../crafted.py` | not part of the tree |

Not run: the whole `process-audit/test_audit_count.py` (about 4 minutes; the author reports 179 tests passing, 277 s; the classes the correction touched I ran), the product's gate (excluded), the real-history count with a scratch locations file (the figures of ruling 2 are the author's, not reproduced), the other checks of the author's table (`test_remarks_check`, `check_instructions`, `test_cross_part_imports`, `test_skills_reach_the_way_sessions`, `test_tracked_files_private_paths`): the correction touched no file they read except `task-cycle/skill/SKILL.md`, whose instruction-file check I did not repeat.

## Reach beyond the dispatch

- `task-cycle/skill/request_template.md` (grep for `Checks*`): to confirm that the *Checks* section step 12 names exists.
- `process-audit/audit_count.py` `GATE_CODE`/`GATE_TOTAL` patterns and `read_measures` (lines 391-394, 1470-1500): to see that `code` cannot raise on `int` and that `cycle.measures` holds only labels that fit.

## Unread material

The reviewers' reports of the earlier reviews (`return-step-review-report.md`, `whole-change-review-report.md`) were not read; `correction-remarks.md` holds their words. Of `foundations/decisions.md` only WAY-350 was read, whole. The rest of `process-audit/test_audit_count.py` outside the diff and the classes I ran, and the rest of `task-cycle/skill/SKILL.md` outside the two passages of the diff, were not read.

## Searches not found or unclear

- Grep for stale phrases ("no other gate", "with another gate", "an earlier form", "Runs with no", "another gate beside") over `.md` and `.py` outside tests and `.runs`: one stale comment found (Minor 1); the other hits are about `stages.md` and records and are correct.
- The dispatch names `task-cycle/review/SKILL.md` and `fix.md`: both found and read; no foundation entry beyond WAY-350 and the guidelines were part of the dispatch, so none was selected.
