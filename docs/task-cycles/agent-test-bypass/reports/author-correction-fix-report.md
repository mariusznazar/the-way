# Author report — the fix of the review of correction 1

**Status:** done. **Commit:** the one commit of this fix on `637d7787` (2 files, `git log --oneline -1` shows it; see the return message). I hold the finding right and contested nothing.

## The finding and how the fix meets it

The finding (Important, `Contradiction: yes`): my correction made a row that adopts an outside practice and repeats the human's choice between ways shown start `waiting`, in `elements/common/skill/task_variant.md` and `project-level/task/skill/find_settlements.md`. WAY-134 (binding sentence, *violates* example and *Rejected*) keeps that such a row enters accepted; the task template and `build_table.md` say so; the human's answer asks for the left-out parts among the ways the person weighs and in the row, not for a new state. My choice 3 had no ground in the answer, and its reason (accepted rows let the parts slip through) is wrong, since an accepted row can get the question.

The fix takes the reviewer's narrowest way, which my reading of WAY-134 and of the answer supports:
- `elements/common/skill/task_variant.md`, step 2: such a row is built `accepted`, as any row that repeats a choice is. Its *Source* names a question whose *Not chosen* keeps the parts of the practice the human turned down, or holds them itself. Where the source keeps none, the question of "How a skill asks" shows the parts the practice leaves out as ways before the table closes, and the parts the human turns down go into the row's *Source* with their cost or reason, as step 4 gives for a question against a choice, so that the decision's *Rejected* takes them (WAY-134).
- `project-level/task/skill/find_settlements.md`: the same, in one paragraph ("enters `accepted` as the human's choice, like any row that repeats one … a question shows the parts as ways before the table closes, and the parts the human turns down go into the row's *Source*").

## Every place that says what state such a row is built in (searched again)

- `elements/common/skill/task_variant.md` (step 2 bullet, the *State* bullet, step 5): changed the new bullet; the *State* bullet ("a row that repeats a choice … starts `accepted`") and step 5 stand and now agree.
- `project-level/task/skill/find_settlements.md`: changed (above); its earlier paragraph "enters the table already `accepted`" agrees.
- `project-level/task/template.md` (*Settlements to record*): says a row that repeats a choice enters accepted; unchanged; my two earlier additions there (a question that settles an adoption shows the parts among its ways; the row names the parts the human turned down) name no state and agree.
- `elements/common/skill/build_table.md`: "built `accepted`, not `waiting`"; unchanged and agrees.
- `elements/decisions/template.md`: names no state; unchanged.
- WAY-134 and WAY-100 (`foundations/decisions.md`): my text names no state ("the refinement shows the human, among the ways of the question …"); the first paragraph, the *violates* example and the *Rejected* of WAY-134 stand and now agree with the step. Unchanged.
- The Minor finding 2 of the review (the wording "the parts the practice leaves out") is not part of this fix, as the handoff says; I did not change that wording.

## Files changed

`elements/common/skill/task_variant.md` and `project-level/task/skill/find_settlements.md` (together 9 added, 7 removed).

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests); `python -B gate/run_tests.py project-level` — exit 0 (279 tests). Not run: the full gate.

## Own-work check

- Requirement most likely not met: that no copy of the step makes such a row wait and the copies agree.
- Check: `reports/author-correction-check.py` extended with three assertions: no passage on a "practice from outside" in the four files of the step (`task_variant.md`, `find_settlements.md`, the task template, `build_table.md`) says `waiting`/`waits` before its `(WAY-134)`; `task_variant.md` and `find_settlements.md` mention `accepted`; the task template keeps "A row that repeats a choice the human made between ways shown enters accepted".
- What it showed: on the fixed tree 16 of 16 ok, exit 0; on the reviewed head `637d7787` it failed the "no copy makes such a row wait" assertion (exit 1, one failure) and passed the other two, so the first tells the fixed text from the unfixed. The second assertion passes on the reviewed head too, since the word `accepted` stands in the files elsewhere; it guards only against deleting the word. A first version of the "wait" pattern carried a stray control character and passed on the reviewed head; I found it by running the check on that head and rewrote the pattern before relying on it. Pattern reading cannot show that a refiner follows one meaning; the review must.

## Reaches beyond the handoff

None beyond reading the files named, `build_table.md` and the task template included.

## Unread material

`reports/review-correction-report.md`: not read (the findings file sufficed).

## Searches not found or unclear

`none`

## Working copies

`.runs/author-correction-fix/` of the worktree held a copy of six files at the reviewed head (`base/`), the check script and the outputs of the checks; removed. Kept in `reports/`: the extended `author-correction-check.py`. No worktree or clone was made.
