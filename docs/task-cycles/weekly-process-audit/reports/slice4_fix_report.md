# Slice 4 fix report — the review's two blocking findings

**Status:** done

**Commit:** `9392230` — Tie the share of fix rounds only where the records allow it (range `269d7be..9392230`; 2 files, `audit_count.py` +94/−35, `test_audit_count.py` +84/−7).

## Findings

### 1. The share of fix rounds can be silently wrong — fixed

**Choice of the tie, and why.** I looked for a tie stronger than a word count and found none in the records or in `stages.md`:
- The archive's *Events* rows name the reports and the orchestrator's stage labels (`fix dispatch`, `fix returned`), never the subagent's stage name. A search of every archived `cycle.md` for a row with a `(general-purpose)` stage name found none.
- *Review rounds* names report paths, not subagents.
- Times do not tie: the record's times and `stages.md`'s start times are in different forms and zones.
- `stages.md` names a subagent (`One author: … — turn 2`), not the round a turn served. A resumed author with a fix in its second turn cannot be told from its first turn by name.

So the narrowest reliable rule is: **a share is given only where the record names no fix round and no stage names one.** Then the share is `0.0%`. Where the record names a round, the share is `unknown` with the reason. The cost is still given.

What changed in `process-audit/audit_count.py`:
- `add_cost` no longer ties counts. Fix rounds are read from *Events* and from the *Review rounds* line; both must name the same reports, or the share is `unknown` ("do not agree"). A record without a *Review rounds* line gives `unknown` ("an earlier form").
- The orchestrator's rows (`orchestrator`, `orchestrator while in parallel: …`) are excluded from the name check, by `is_orchestrator_row`.
- The module docstring describes the rule.

Each run of the finding's scenarios now gives `unknown` (the resumed author, the parallel rows) rather than the 99.6 % and 49.7 %.

**Tests** (each fails on `269d7be`, then passes):
- `Cost.test_resumed_turns_named_with_fix_do_not_give_a_share` — the resumed-author form; `269d7be` gives a number.
- `Cost.test_orchestrator_rows_naming_fix_subagents_are_in_no_fix_round` — the parallel rows; `269d7be` gives a number.
- `Cost.test_a_cycle_naming_no_fix_round_and_no_fix_stage_has_a_share_of_zero` — the one case where a share is given (`0.0%`); `269d7be` gives `unknown`, because it counted the orchestrator's parallel row as a fix stage.
- `Cost.test_review_rounds_naming_a_fix_the_events_lack_leave_the_share_unknown` — the *Review rounds* line is read too (the finding said only *Events* was read); `269d7be` gives `0.0%`.
- `Cost.test_a_record_without_a_review_rounds_line_leaves_the_share_unknown` — new behaviour; `269d7be` gives a share.
- `Cost.test_fix_stages_the_record_does_not_name_leave_only_the_share_unknown` — existing; its reason text changed, and it fails on `269d7be` only on that text. Its behaviour (share `unknown`) was already right.

**Changed existing tests (named):**
- `Cost.test_a_fix_round_at_a_test_price_list_gives_the_cost_and_no_share` (was `…_gives_the_cost_and_the_share`): the hand-worked share of 26.9 % is replaced by `unknown`. The cost (0.010950) and the round count (1) are still checked. This is the intended change: the share can no longer be given for that record.
- `fix_record()` fixture: now writes a *Review rounds* line matching its *Events* (or `none yet`), as the template does.

### 2. A cost of 0.000000 where tokens are absent — fixed

`priced` no longer prices a `—` row (the mark `cycle_stages.py` writes for a stage with no token usage) as zero. It gives `unknown` with the reason "stage … has no token usage in its transcript, so its cost is not known". The share is `unknown` too (the existing cost-unknown path).

Test: `Cost.test_a_stage_with_no_token_usage_leaves_the_cost_unknown`; on `269d7be` it gives `0.000000`.

**Choice:** I treat any `—` row as unknown, not only a section where every row is `—`. Rejected: zero for a stage with no usage, since the transcript may simply not have been read (`cycle_stages.py` lists that case in its warnings). Cost if wrong: a cycle with a legitimately tokenless stage gets `unknown`.

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B -m unittest test_audit_count.Cost`, with `269d7be`'s `audit_count.py` in place (the file restored afterwards, `cmp` identical) | 1 | 8 failures of 14: the six new tests (the zero-round share, the changed hand-worked share, the missing *Review rounds* line, the tokenless stage, the parallel rows, the resumed turns) and the review-rounds test, plus `…_does_not_name_leave_only_the_share_unknown`, which fails only on its changed reason text. Six pass on `269d7be` because their behaviour was already right (model, ceiling, token count, cached above input, price list twice, the earlier form) |
| `python -B -m unittest test_audit_count.Cost`, fixed code | 0 | 14 tests OK |
| `python -B gate/run_tests.py process-audit`, final | 0 | 61 tests OK |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | checked 279 files, 0 listed |
| run on this repository, stdin closed, temporary locations file and results directory: `python -B process-audit/audit_count.py --locations <scratchpad>\run4\locations.json <&-` | 0 | `Wrote count-2026-11-11.md and count-latest.md: 69 cycles in 1 of 1 repositories.` All 69 cycles give *Cost* and *Fix rounds share* `unknown` (67 earlier-form `stages.md`, 2 without `stages.md`), as before |

Not run: the full suite (WAY-160).

## Own-work check (WAY-164)

- **Requirement most likely unmet:** a share or cost given that the records and `stages.md` do not support (a count coincidence, a zero for a stage with no usage, a share computed where the record names rounds that the stages cannot be tied to).
- **Check:** the six new or changed tests, run on `269d7be` and on the fix; the run on this repository.
- **What it showed:** on `269d7be`, every scenario of the findings gives a figure (the resumed author, the parallel rows, the tokenless stage, the *Review rounds* disagreement). On the fix, each gives `unknown` or the honest `0.0%` only where no round is named anywhere.

## Questions

1. **Does the orchestrator want the stronger link now?** As it stands the share is `0.0%` or `unknown`, so the measure is mostly absent. A reliable share needs a link that the stages write. The cheapest option I can see: `cycle_stages.py` writes, for each subagent turn, the report path its prompt names (the transcript has the prompt). Recommended: take it as a separate change to the stage format. It changes `stages.md`, so it starts a new series (WAY-336), and `cycle_stages.py` reads the prompt as untrusted text. Cost if not done: the share stays `unknown` in every cycle that has a fix. Recommended answer: yes, as a separate task.

## Concerns

- In practice the share will be `unknown` in every cycle with a fix round. That is the rule the review asked for, but it leaves the share measure empty until the question above is decided.
- A `0.0%` relies on the record: a fix that no *Events* row or *Review rounds* line names, and whose stage carries no fix or review word, gives `0.0%`. The record is the source of rounds, as the slice says; a record that omits a fix would be wrong on the record's own terms.
- A stage name starting with `orchestrator while in parallel: ` from a subagent's own description is treated as the orchestrator's row. The names come from `cycle_stages.py`'s pattern; a subagent description with that exact prefix is not plausible, but it is not defended against.

## Reaches beyond the handoff

- `task-cycle/change/fix.md`, read whole (named by the handoff).
- The archived records, by `git show`: a search for *Events* rows naming a `(general-purpose)` stage, to test whether a stronger tie exists in the records. None found.
- `cycle_stages.py` `build_rows` (grep for the parallel row name), to confirm the orchestrator row naming.

## Unread material

- `review_slice4_report.md` (the full review): not read; the handoff gives the findings file as the list to fix, and the findings file holds both findings whole.
- The findings file as I read it holds only the two blocking findings; the Minor findings 3–6 and the out-of-scope finding are not in it, so I neither read nor fixed them.

## Searches not found or unclear

- A subagent name in the archived *Events* rows: searched for `(general-purpose)`, `(Explore)`, `(Plan)` in archived `cycle.md` rows; none found.
- Whether a *Review rounds* line in the archive always names fix reports in the form the Events use: not checked across the archive. A mismatch gives `unknown`, so the failure is safe.
- The `orchestrator while in parallel: ` prefix as the only form of parallel rows: taken from `cycle_stages.py` `build_rows`; not checked against every archived `stages.md`.
