# Fix report — Minor findings of the review of the whole change

Status: `done`. Commit `d496942` on `task/decisions-as-material-at-refinement` (fix range starts at the reviewed head `3cf2a09`). Worktree clean.

Files changed (`git show --stat d496942`): `foundations/decisions.md`, `elements/common/way_of_working.md`, `project-level/skill/read_foundation.md`, `project-level/technology/task_run.md`, `project-level/technology/running_product.md`, `project-level/task/skill/orchestrated_mode.md`, `project-level/task/skill/resolve_gaps.md`.

## Finding 1 — fixed

Chose the clause, not the shown-option form. The question at the start of a definition asks before any concrete option exists, so it cannot carry the consent; turning it into the shown-option form would need an option with a decision named, which does not yet exist at that step, and would make a second, earlier presentation of the same change. The clause says what the question is.
- `project-level/skill/read_foundation.md:8-12`: "ask whether the project is meant to change it or to fit it (WAY-30); the question only frames the conversation, and the consent to a change is the human's choice of the option that changes the decision, not the answer to it (WAY-314)."
- WAY-111 binding sentence: same clause. Its *Verification* lines ("asks whether the project changes or fits it") stay true and are unchanged.
- Check: `grep -rn "fits it" project-level foundations` shows the two places with the clause; `foundation_check.py` exit 0.
- Cost of this way: the question stays and is one more exchange in a definition; the other way (drop it) would cost the framing of what the project touches.

## Finding 2 — fixed

At a definition's step 4 the refinement rule wins; the full question applies only to an entry written outside such a refinement. Question 2's answer is not undone: the definition's refinement keeps "only for a quoted contradiction of the human's own sentence" (`definition_variant.md` collision move) and "questions of what an entry needs and the source does not give" stay, being no question against an answer.
- WAY-113 binding sentence: "...which the question quotes, and that holds as well for the entries written during that refinement; in a task's cycle and where an entry is written outside such a refinement it is asked as above...".
- `elements/common/way_of_working.md` ("How a skill asks", third bullet after the question against the answer): added "That holds as well for the entries written during that refinement, such as the projected entries of a definition. In a task's cycle and where an entry is written outside such a refinement, the question stands as the bullet above gives it".
- Check: reading of WAY-113, `way_of_working.md` and `definition_variant.md` step 4 together: no two sentences can now both apply to step 4.

## Finding 3 — fixed (the "may" way)

Chose "may open" and dropped the *Verification* violation that required opening. Reason: the task's point 5 asks only to remove the reservation "opens only on the human's word" from WAY-165 and WAY-267, and its *To do* point 1 says the agent "może sam pokazać" (may show); question 5 keeps the approved definition's projected decisions out. A mandatory opening is a stronger rule than any of these says.
- WAY-165 binding sentence: "the step may open a decision of the foundation that leaves part of it unanswered as it may open any such decision (WAY-313), the list shown to the human saying in one sentence what that decision leaves unsaid".
- WAY-165 *Verification*: complies — the item "ends `— open` ... where the step opens it", the list says what the decision leaves unsaid; violates — "an agent waits, in a run at a task, for a word of the human before it opens a logs decision silent on the record's life" (the old reservation), the clause requiring `— open` removed.
- WAY-165 *Rationale*: names the word "may" as deliberate, as in WAY-313 (the list of every run touching a matter would otherwise grow), and that the list still says what the decision leaves unsaid so the human can open the item.
- `project-level/technology/task_run.md`: "you may open its item `— open` here as at a definition ...; the list, with the item open or still `— held by`, says in one sentence what the decision leaves unsaid, and the human may open it by a change to the list."
- Way not taken: keep opening mandatory and name it as a step beyond WAY-313. Its cost would have been a rule the task did not ask for, a list that grows with an item over every silent decision, and a violation for an agent that reasonably keeps one held. Cost of the way taken: a run may leave a silent logs decision `— held by`, and the agent of the cycle then improvises the record's life (the cost WAY-165's Rationale already names); the sentence in the list is what lets the human open it.
- Check: WAY-165, WAY-313, WAY-267 and `task_run.md` read together say the same ("may"); `foundation_check.py` exit 0.

## Finding 4 — fixed (wrapping only, no wording change)

Wrapped at 100 characters: `running_product.md:40`, `orchestrated_mode.md:48`, `resolve_gaps.md:18-19`, and in `foundations/decisions.md` the WAY-134 lines (3399/3408 area), WAY-165 *Verification* (the lines of 4739-4744 area) and WAY-267 (8040 area), plus the lines the fix itself added.
- Check: `git diff -U0 3cf2a09 | grep '^+' | grep -v '^+++' | awk 'length($0)>101'` returns no line; `git diff --check` clean.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors").
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK.
- `python -B gate/run_tests.py project-level` — exit 0, 271 tests OK.
- `python -B gate/run_tests.py task-cycle` — exit 0, 187 tests OK.
- `python -B agent-instructions/skill_entry_points.py` (check mode) — exit 0, "entry points are current" (no `description` changed).
- Not run: the full gate (the orchestrator's); `installation` not rerun — the fix touches no file it reads that the first run had not covered by content of the same kind, and its first run passed (exit 0, 44 tests) on the unfixed head; say so if you want it rerun.

## Own-work check

Requirement most likely not met: that the fix stays as small as the findings ask and creates no new contradiction between WAY-165, WAY-313 and `task_run.md`. Check: after the edits I read the three places together and grepped for the old phrases ("until the human says a word", "such a decision as it opens", "stands `— open` here as at a definition") — none remain; `foundation_check.py` and the focused directories pass. The fix adds no new rule beyond the findings' suggested ways.

## Reaches beyond the dispatch

- `project-level/skill/read_foundation.md` (finding 1): not named in my first handoff; I read it in the first run to judge the orchestrator's extra places and left it unchanged then; the fix edits it now, as the coordinator directed.
- `foundations/decisions.md` WAY-111, `project-level/task/skill/final_review.md` (no change): read to check that no other step asks about a decision change.

## Searches not found or unclear

- none (every place named by the findings was found; the reviewer's line numbers 3399 and 8040 were approximate and I wrapped the nearby lines the awk check flagged).
