# Handoff - the return step of `friction-at-source`

You, the one author of the change, now take the return step (step 11 of `implement-task`). It is no row of the variants of `make-change`: your stage is "the return step".
Read `task-cycle/skill/return_step.md` in the worktree whole, and `task-cycle/skill/foundation_step.md` where it applies (the return step writes as the foundation step writes);
read the skill of an element when you write an entry of that element.

- Worktree `the worktree's root`, branch `task/friction-at-source`, head `6e4669e` (the change with the fix of the Minor findings; reviewed `PASS 6e4669e`).
- Frozen task: `docs/task-cycles/friction-at-source/task.md`. No spec, no plan.
- Answers of the start: trust boundary no, irreversible operation no, open design choice none. The task excludes no entry for a choice.
- The entries to compare with the files: WAY-327, WAY-353, WAY-354 and the glossary term `transitional state`; those the task names under *Decisions in play* (WAY-286, 287, 289, 290, 24, 302, 305, 36, 37, 01);
  those your search of the foundation found; and the part map of the touched parts (`task-cycle`, `project-level`, `foundation-review`, `decisions`, `glossary`). Compare each with the files of the repository at the head,
  including the changes of the fix, and correct in this change whatever no longer matches. Also: a row of *Settlements to record* (1 to 4) the foundation step missed; a choice that binds after the merge (WAY-36),
  for example the rule that a step of an item for an unrun check may give a command to type without a file name, which the review noted is no decision's text: judge whether it is a choice that binds, and if so write it
  where it belongs (WAY-327's binding sentence, or none if you hold it a choice of wording, with the reason); invariants only for a rule the task, a decision or the human sets.
- Your report: `docs/task-cycles/friction-at-source/reports/return-step-author-report.md`. It holds, in the order of the record's *Return step*:
  foundation compared with code; decisions written or changed; invariants; environment facts; glossary terms; part-map changes; projected entries; rows of *Settlements to record* written - each with its identifier or `none`;
  the commits (none if nothing needed correcting), the checks you ran with command and true exit code (no pipe hiding it), **Unread material** and **Searches not found or unclear**.
- Boundaries: commit by path, English messages, no push; do not run the whole gate; the focused checks are `python -B elements/common/foundation_check.py` and the tests of the directories whose files you change.
  Do not start the next stage. Where you commit anything, a fresh reviewer reviews your range.
