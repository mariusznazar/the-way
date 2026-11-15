PASS 3b296184aa8780986f9e38e823784f62d491abc1

# Review of correction 1 (range `db0c5f8..3b29618`, one commit)

Reviewed: the correction for the human's remarks of `reports/correction-1-remarks.md`. `git rev-parse HEAD` = `3b296184aa8780986f9e38e823784f62d491abc1`, the head given. Diff: `foundations/decisions.md` +14/-18, `guidelines/testing.md` +1/-1.

## Remarks: made or not

1. **Fix Minor finding 4 (WAY-395, `--today`) — made.**
   - `foundations/decisions.md:10145-10147` (binding sentence of WAY-395) now reads that *Time and randomness* "has the test give the script its time, by replacing the clock function of the script in the process of the test or by giving a fixed time to a script that takes one, and no fixed pause".
   - The *complies* example of WAY-395 (`foundations/decisions.md:10158-10160`) changed the same way. It no longer names `--today`.
   - `guidelines/testing.md:181` (recipe `unit`) changed to the same wording. The recipes at lines 193, 205, 217 and 229 read "as in `unit`", so they follow.
   - Both means named are real. `task-cycle/test_gate_times.py:83` replaces `gate_times.now_ms` in the process of the test. `process-audit/test_audit_count.py` (for example line 634) gives `--today` to `process-audit/audit_count.py:3257`, which takes that option. `task-cycle/gate_times.py` has no `--today` and the decision no longer says it has.
   - A search of the whole repository outside `.runs` for `--today`, "reaches the script from outside" and "from outside the script" leaves no place that still names `--today` as the means of WAY-395. No test carries a line `decision: WAY-395`, so no quotation broke.
2. **Fix Minor finding 3 (pairs of examples in WAY-380, WAY-388 to WAY-391) — made.** I compared each removed clause with the invariant text in `foundations/invariants.md`:
   - **WAY-380** (`foundations/decisions.md:9744-9750`): two clauses removed.
     - The *complies* clause "the test of the invariant runs Ruff with the flag that ignores comments turning rules off" is the `--ignore-noqa` of `ruff-blocking-rules` (`foundations/invariants.md:430`, `agent-instructions/test_linter_invariant.py:79`).
     - The *violates* clause "a comment that turns a blocking rule off stays in a file" is also held: with `--ignore-noqa`, a line that breaks a blocking rule is reported whatever comment stands on it.
     - What is kept is not held by the invariant, which runs Ruff with `ruff.toml` and does not check the configuration's content or whether an example rule blocks. The kept clauses are: the fault fixed in its own file with the configuration unchanged, the move of a rule by a change of the decision, a rule turned off in the configuration with no change of the decision, and a rule of the examples that blocks.
   - **WAY-388** (`:9975-9979`): removed "a generator writes a file in a run with no `--write`", which `generator-writes-only-with-write` holds (`invariants.md:450`).
   - **WAY-389** (`:9999-10003`): removed "removes or rewrites something in a run without `--apply`", which `repository-changer-acts-only-when-told` holds (`invariants.md:460`).
   - **WAY-390** (`:10020-10023`): removed "ends with the exit code 1 for every failure of the command", which `command-runner-passes-exit-code` holds (`invariants.md:470`).
   - **WAY-391** (`:10040-10043`): removed "reads its input or writes output when it is imported", which `shared-module-import-runs-nothing` holds (`invariants.md:480`).
   - Each of the four keeps the pair for the designation of the exemplar: the guidelines of the kind list the file as `exemplar`, and no other file takes that status. No invariant or test holds that part, so `elements/decisions/template.md:245-248` allows the pair, and the form "invariants only" (template lines 253-257) did not apply.
3. **Let through (Minor findings 1, 2, 5, 6, 7; answer 1)** — nothing changed for them, as the remarks bind. The diff touches only the six entries and the one guideline line above.

Nothing the remarks did not ask for changed. The *complies* example of WAY-395 is part of finding 4, since it quoted `--today`.

## Findings

### Critical
none

### Important
none

### Minor
1. **WAY-388's kept *complies* clause rests on a part a test already holds, and that part is not in WAY-388's sentences** (`foundations/decisions.md:9977-9978`).
   - The clause is "and the file ends with exit code 2 where a field it reads is missing, as WAY-344 gives".
   - `agent-instructions/test_skill_entry_points.py:198-227` holds exactly this behaviour by lines `decision: WAY-344`. The binding sentences of WAY-388 (`:9969-9970`) do not state it at all; only its *Rationale* mentions it.
   - The template allows a pair only for "the part of the sentences that no invariant and no test checks" (`elements/decisions/template.md:245-247`). The remarks asked only for examples that repeat an invariant, so the correction rightly left it.
   - Effect: a second written copy of a tested rule, which can drift. Nobody reads anything wrongly today.
   - The line lies outside this diff (unchanged context), so this is a note (fix.md) and not within what the remarks bind.
2. **Uneven line break in WAY-395** (`foundations/decisions.md:10148`).
   - The line "<directory>`, which the gate narrows to a directory and no further. The field" is left short, before "*Time limit* reads …" on the next line.
   - Polish only. The repository has made reflow commits for such lines before (for example `cecc49e`).

No finding is out of scope.

**Considered, not a finding:** the new wording names "replacing the clock function of the script" as a way to give time. The testing template says "the code under test never replaced" (`product-guidelines/testing/template.md:238`) and "the clock … given from outside" (line 242). WAY-395's *Doubles* already allows "a double only of the clock". A replaced clock function such as `now_ms` (`task-cycle/gate_times.py:117-118`, a one-line wrapper of `time.time_ns`) is that double, not the logic under test. So the wording matches the decision and the tests, as the remark asked.

**Considered, not a finding:** many tests of `task-cycle/test_gate_times.py` run the script in a subprocess with its real clock (`run_gate`, line 66) and assert nothing about time. The binding sentence "has the test give the script its time" says no more on this than the old "has the time given from outside the script" did. The correction did not widen the rule.

## Declined to judge
none

## Checks
- `git diff db0c5f8..3b29618` and `git log db0c5f8..3b29618` — one commit, 2 files, +15/-19.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 242 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 37 tests, OK (expected failures=2).
- Manual: searched the repository (outside `.runs`) for `--today`, `now_ms`, "reaches the script from outside", "from outside the script", "Time and randomness", and for the words of each removed example. Result: no stale copy. The two remaining similar phrases are `foundations/decisions.md:8650`, another decision about the flag, and `guidelines/coding.md:30`, a *Bad* example of a guideline. Neither is a copy of a removed pair.
- Manual: searched for lines `decision: WAY-380|388|389|390|391|395`. There are none, so no quotation is affected.
- `git status --short` before and after the runs — empty. The reviewed worktree is unchanged.
- Not run: the full gate, which the handoff reserves for the orchestrator.

## Reach beyond the dispatch
- `foundations/invariants.md:428-487` (the five invariants by identifier), to judge whether each removed clause is held.
- `agent-instructions/test_linter_invariant.py` (whole), to confirm `--ignore-noqa` is in the invariant's test.
- `task-cycle/test_gate_times.py:60-109`, `task-cycle/gate_times.py:280-319` and `process-audit/audit_count.py:3257` (by search), to confirm what the tests do for time.
- `agent-instructions/test_skill_entry_points.py:196-227`, to judge the kept *complies* clause of WAY-388.
- `product-guidelines/testing/template.md:236-245`, to check the new wording against the template that WAY-392 adopts.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/request.md`, its *Minor findings* section (lines 162-174), for the words of findings 3 and 4.

## Working copies
None made. The checks ran in the reviewed worktree without changing it (`git status` empty before and after). The directory `.runs/review-correction-1/` was not created. Nothing remains.

## Unread material
- The report of the review of the fix of the whole change, which the handoff names among the reviews that gave the two Minor findings: not opened. I took the words of both findings from `request.md:168-169` and `reports/review-return-report.md:22-34`.
- `task-cycle/skill/foundation_step.md`: not read. I made the WAY-33 search by grep over the whole repository instead.
- `elements/decisions/template.md`: read by search for "Verification" with context (lines 29-45, 64-80, 102-118, 158-176, 219-272), not whole.
- `reports/review-return-report.md`: lines 20-35 (its *Minor* section) read, not the whole file.

## Searches not found or unclear
- `--today` in `task-cycle/gate_times.py`: not found, as expected. That absence is what finding 4 was about.
