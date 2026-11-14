# Fix report: findings of the whole-change review

Fix range: `888eb6150e13bee2337368114c4f1cd760b3d274..913fe45`. Variant of `task-cycle/change/SKILL.md`: the fix of a review's findings, read as `task-cycle/change/fix.md`.

Status: done

Commit: `913fe45` Fix the review findings on the reading limit measurement (files: `task-cycle/slice_size.py`, `foundations/decisions.md`; 21 lines added and 23 removed in total across the two files)

## Each finding

1. Blocking, source fidelity. Fixed. The 25% now belongs to the 20 slices ("those 20 took 25% of the input tokens of all executors"), and the runs are "5 of its 10 long runs of executors", the task's wording; "longest" is gone from both files (grep: no match in either). The 21 000 figure reads "above 150 000 tokens" in both the script's description and WAY-371 *Rationale*. The 175 000 and 125 000 rejected values were restated in the same pattern: "those 10 would take 12%" and "those 34 would take 34%", the share attached to the slices as the task's *Questions to settle* gives it.
2. Minor, `CONTEXT_WINDOW_TOKENS` unused. Fixed by removal. A search outside `.runs/` found only its definition and its docstring bullet; no test or other file uses it. Removed the constant and its bullet. The source quote is kept only where it explains the estimate: the bullet now reads "CHARACTERS_PER_TOKEN comes from ... its note on the context window says '1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer'". The "Compare models" table quote is cut, as nothing rests on it.
3. Minor, "wide margin" sentence. Fixed. The sentence now reads "The limits are corrected as cycles bring data:", true of both limits; `CHANGE_LIMIT` keeps its "starting value with no source" bullet.
4. Minor, WAY-371 binding text. Fixed. The binding sentence now states only the value and what the script reports; the conversion sentence is removed from the entry. It stays in the script's description, where it already stood, with its source.
5. Minor, WAY-371 *Verification* "violates". Fixed. Now "the limit is set to any value other than 150 000 tokens", without the quarter.

Not fixed: finding 6 (outside the task) is not in the findings file and was not touched.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Task-cycle suite | `python -B gate/run_tests.py task-cycle` | 0 | 394 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| Constant still values as before | `python -B -c` importing `slice_size` from `task-cycle` | 0 | `READ_LIMIT_TOKENS` 150000, `CHARACTERS_PER_TOKEN` 2.5 |

Not run: the full gate (the orchestrator runs it). No test changed in this fix; the boundary test of the previous commit still covers the limit.

## Own-work check

- Requirement: the script's measurement and WAY-371 carry the same numbers, with the 25% on the slices and the runs called "long runs of executors", and no wording stronger than the task.
- Check: `grep -n -i longest` over both files, and `grep` for "21 000" and "25%" to read where each stands; then the gate and foundation check above.
- Showed: no "longest" left; 25% reads after the 20 slices in both files; 21 000 reads "above 150 000" in both.
- Removing the constant: a mutation of the limit or the characters constant is still caught by the boundary test; the constant had no reader, so removal cannot change any verdict. The gate's 394 tests pass.

## Unread material

- `reports/review-whole-findings.md` and `reports/fix-handoff.md`: read whole.
- `task-cycle/change/fix.md`: read whole.
- `task.md`: not re-read in this fix; the orchestrator's rulings in the fix handoff quoted its *Need* lines, which I checked from the earlier read.
- `foundations/decisions.md` WAY-136 *Rejected* (commit `888eb61`): not re-read in this fix; the review did not name it.
- Nothing else named by the dispatch is unread.

## Searches not found or unclear

- Other users of `CONTEXT_WINDOW_TOKENS` outside `.runs/`: none (found only in `task-cycle/slice_size.py`, now removed).
- Any use of "longest" in the measurement wording: none left in `task-cycle/slice_size.py` or `foundations/decisions.md`; the two other hits of "longest" in `foundations/decisions.md` (WAY-3xx lines 144 and 3098) concern other decisions and are not part of this change.
- A source for the 12% and 34% attribution to the slices: the task gives "tokenów wejścia wykonawców" with the count of slices; I attached the share to the slices as the task's *Questions to settle* reads, and did not find a passage that states it more narrowly.

## Choices made

- `CONTEXT_WINDOW_TOKENS` removed rather than kept, as the orchestrator's ruling says; its source quote cut to the note that the characters-per-token estimate rests on. Alternative: keep the constant; cost would be a dead constant that readers wonder about.
- The rejected values in WAY-371 keep the share attached to the slices, as the task reads it, with "those 10" and "those 34" in place of the bare percentages. Cost if wrong: a reader might take the share for the runs; the sentence now names the slices.
