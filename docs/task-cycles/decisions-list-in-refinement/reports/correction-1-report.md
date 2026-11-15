# Correction 1 report — decisions-list-in-refinement

**Status:** done

**Commit range from `f50e58f`:** `f50e58f..ddbdaf2` (one commit, `ddbdaf2`; I amended my own unpushed commit once to rewrap two lines over 100 characters). Not pushed.

## The remarks, each as made, and how

Remark 1 (the only one that is mine): "The widened check of quotations names only guesses 'settled in the repository'. Name also a guess the second agent judged settled by the task document itself, in the skill and in the decision (one phrase each), so that the refining agent opens that quotation too."

Made:
- `project-level/task/skill/final_review.md` step 3: "judging it already settled in the repository or in the task document or most likely right". The step's next words, "open the file the critique quotes from", already reach the task document when the quotation is from it.
- `foundations/decisions.md` WAY-378, binding sentence: "on the critique's verdict that the repository or the task document already settles it or that it is most likely right".
- Same entry, the "complies" example, which repeated the phrase: "6 already settled in the repository or the task document". Nothing else of the entry changed; its meaning is the same, widened by the remark. WAY-377 repeats no such phrase (its second agent already "settles each guess against the repository and the document").
- The rest of the lines I touched are rewrapping to 100 characters of the same sentences.

Remarks 2 and 3 (let through, no task), 4 to 8 (accepted) and the last paragraph (merge of the target branch, the orchestrator's): no work, as the handoff says.

## Return step again, for what the correction touches

Compared WAY-377 and WAY-378 (whole) with `final_review.md` steps 1-4, the bullet of `orchestrated_mode.md` and section 6 of `SKILL.md`. They say the same: the condition, the two agents and their input and class, the bound, the file and who writes it, the quotation check over the matters shown and the guesses kept from the human (now settled in the repository or the task document, or most likely right), the limit of about four, the silence where nothing is open. `orchestrated_mode.md` and `SKILL.md` name the check only by pointing to `final_review.md`, so they needed no change. Nothing no longer matched; nothing else changed. N1 of the fix review is closed by this correction.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0 (after the amend).
- `python -B instruction-files/check_instructions.py .` — 0 error, 0 warn, exit 0.
- `python -B gate/run_tests.py project-level` — 278 tests OK, exit 0 (before the amend, which only rewrapped two lines of `foundations/decisions.md`; `foundation_check.py` run again after it).
- Not run: the whole gate (the orchestrator's).

## Own-work check

Requirement most likely not met: that the skill and the decision say the same, and that the phrase "settled in the repository" stands nowhere else. Check: grep of `project-level/task/skill/*.md` and `foundations/decisions.md` for "settled in the repository" and "already settles"; the hits are `final_review.md` step 3 and WAY-378's sentence and example, all now widened; no other place repeats the phrase. Reading check, plus the three runs above.

## Reaches beyond the handoff

None.

## Working copies

`.runs/author/` held the output of the test run; removed (`.runs/` holds `orchestrator/` and `task-cycles/`). `git status` is clean.

## Unread material

- `reports/review-fix-1-report.md` and the earlier reports: not read; the handoff names finding N1 and the files.
- WAY-377 and WAY-378: read whole. The other decisions of the task: not re-read; the correction does not touch them.

## Searches not found or unclear

- none
