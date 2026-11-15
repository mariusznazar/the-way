# Author return step report — decisions-list-in-refinement

**Status:** done. Nothing needed correcting; I committed nothing. The branch head stays `b084a4a`.

## Return step items

- **Foundation compared with code, and what no longer matched.** Range `9cbc6b2..b084a4a`. I compared WAY-377 and WAY-378 (the entries the change wrote), WAY-374, WAY-120, WAY-113, WAY-229, WAY-100, WAY-134, WAY-124 and WAY-154 (the entries the task names) and the part-map entries of `project-level` and `decisions` (read whole) with `project-level/task/skill/final_review.md`, `orchestrated_mode.md` and `SKILL.md` section 6. Matched, point by point: the condition (*Decisions in play* is not `none`, or the task changes a skill or an instruction file); two fresh agents of one class cheaper than the refining agent's, named in general terms; the first agent's input (the complete document and the full entries, nothing of the conversation); the second agent's read access; the bound of WAY-374 and the silence where nothing is found; at most about four matters, most consequential first, with ways, cost and a recommendation (WAY-113); the file in the ignored `.runs/` directory with its path given to the human; the check of the quotations behind both the matters shown and the guesses kept from the human (WAY-120, as fixed in fix 1); who writes the file in each mode (WAY-154: the refiner starts no agent in the orchestrated refinement). WAY-229 binds the executor, the one author and the cycle's reviewers, not refinement agents, so no collision and no `narrows`. WAY-124 holds: the step runs before the complete document is shown for acceptance. Nothing no longer matched, so no correction.
- **Decisions written or changed.** WAY-377 (row 1) and WAY-378 (row 2), both written in the foundation step and changed once in fix 1 (WAY-378's binding sentence, example, *Rationale*, *Rejected*; WAY-377's *Rationale*). No other decision changed. No choice that binds after the merge was found beyond the two rows.
- **Invariants.** None written or changed; no invariant of `project-level`, `decisions` or `every` is touched by the change.
- **Environment facts.** None. The one outside practice (the AI Tech Leaders course) is not open to a reader of the repository, so WAY-377's *Rationale* describes what the notes hold, as WAY-100 and WAY-27 give; no citation there would call a decision into question if it stopped being true.
- **Glossary terms.** None. No word of the new text takes a meaning a reader of the field would not give it (WAY-95); "decisions in play" and "critique" stay as the skills use them.
- **Part-map changes.** None. `project-level` already answers for "the refinement of a task before its implementation cycle", `decisions` for the log; no file left its part and no dependency changed (the change imports nothing).
- **Projected entries.** None; the task is independent.
- **Rows of *Settlements to record* written and where.** Row 1 → decision WAY-377, in `foundations/decisions.md`, section "Task refinement and readiness". Row 2 → decision WAY-378, same place. Both are `row <n>` entries; none is `projected` or `the cycle's`.
- **Pair of examples and tests.** Both decisions carry a pair of examples; no test holds a sentence of either, so no part leaves the pair and no clause `tests:` is written (no line `decision: WAY-377` or `WAY-378` exists).
- **Known open item, not fixed.** The fix review's Minor finding N1: the widened quotation check in `final_review.md` step 3 names "settled in the repository" only, while the critique's step and WAY-377 say "the repository or the document". Not widened, as the handoff says.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0.
- `python -B gate/run_tests.py agent-instructions` — 27 tests OK, exit 0 (the tests of the skill entry points; the skills' descriptions did not change).
- Search of the whole foundation and the tracked files for `final_review`, `Review and hand off`, `decisions-list` and the wording of the step (WAY-33): the hits are the four files of the change and `foundations/decisions.md`; no other file, entry or test names the step or the file.
- Not run: the whole gate (forbidden); `project-level` and `elements/common` tests (run in fix 1 on the same files, nothing changed since).

## Own-work check

Requirement most likely not met: that the entries and the three skill files still say the same after fix 1, and that nothing in the foundation names the old state. Check: read WAY-377 and WAY-378 as they stand against the final text of the skill files (above) and searched the tracked files for other mentions (above). It showed one remaining difference, N1, listed above and left to the request; no other.

## Working copies

`.runs/author/` held the output of the focused test run; removed (`.runs/` holds only `orchestrator/` and `task-cycles/`). `git status` is clean.

## Unread material

- WAY-113, WAY-134, WAY-124, WAY-154: read through their binding sentences (the index and the task's quotations) in the earlier stages and again for this comparison in the sentences that bear on the step; their *Rationale* and *Rejected* not re-read. WAY-374, WAY-120, WAY-100, WAY-229, WAY-377, WAY-378: read whole.
- `reports/review-whole-report.md` and `reports/review-fix-1-report.md`: not read; the handoff gives the fix review's result and the finding N1.
- The invariants of `project-level`, `decisions` and `every`: not re-read; none concerns the content of a skill step or of a decision's sentences.

## Searches not found or unclear

- none
