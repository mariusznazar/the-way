# Findings for the fix — Minor findings of the review of the whole change (within the task)

Cut word for word from `reports/review.md` (first line `PASS a15de0906961981bc58982f97cb1443875341518`). No blocking finding exists. Each finding below is within the task and is fixed before the request opens; answer with evidence any you hold wrong. Finding 3 concerns `reports/assessment.md`, which is not committed.

1. `elements/common/skill/SKILL.md:32-33` - "where you start at step 2, 4 or 5 and have not read it,
   read it first". Within the task. A resumed use whose first row is still `waiting` (the resume rule
   at `SKILL.md:35-36`) starts at step 3, not at 2, 4 or 5, so by the letter the sentence does not
   reach it when it comes to step 4 or 5. The route is not lost: the pointers at `SKILL.md:56-57` and
   `:61-62` name the variant file and have the agent carry out its lines, and the entry point reads a
   file when the step that names it comes (WAY-127, WAY-259). What can be lost is "in full": such an
   agent may read only the "Step 4" section and miss the variant's "What the caller gives". Little
   rides on it, because the table in `SKILL.md` names the source and the mode of each variant. A
   wording such as "where you come to step 2, 4 or 5 without having read it, read it first" would
   cover every start. Evidence: hand walk of a resumed task-mode use (below).
2. `elements/common/skill/task_variant.md:38-39` - "An accepted row stays a row, and the task's cycle
   writes its entry (WAY-134). In its place, a row that carries a choice ...". Within the task. On the
   base (`SKILL.md:95-96`) "In its place" followed "this step does not run" and meant step 4. That
   clause now stands only in `SKILL.md:56-57`, so inside `task_variant.md` the nearest antecedent of
   "its" is "its entry". The meaning reaches the agent through the heading "Step 4 - in place of row by
   row" and `SKILL.md` "carry out in its place the lines for step 4 of `task_variant.md`", so no rule
   changes; the sentence reads awkwardly to an agent that opens the file by its path. "In place of
   step 4, ..." would close it. Evidence: 6-word window comparison of base and new files (checks
   below), which places this run among the reworded ones.
3. `.runs/task-cycles/find-foundation-entries-shape/reports/assessment.md` proposal 3 and "Before the
   table". Within the task (To do 1 and 5). `instruction-files/judging.md:32-33` says removals are
   proposed as "When to remove a rule" (`judging.md:72-81`) gives. Proposal 3 (remove the sentence on
   future callers, base `SKILL.md:12-14`) names none of that section's conditions and gives only "no
   step depends on it". The judgement also skipped the search of records that `judging.md:7-9` puts
   before the table (the author says so openly). The verdicts of the table rest on cost or a carried
   decision, which `judging.md:32` allows, so no row's verdict is wrong for lack of the search. But the
   request will show the human a removal without the ground the method asks for. The proposal should
   say which condition it meets, or that the sentence is a statement of plan and no rule, so that the
   section does not apply.
