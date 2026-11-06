# Handoff — the return step (make-change), task `glossary-three-questions`

You are the one author, resumed, for the return step (step 11 of `implement-task`). The return step is
not one of the rows of `task-cycle/change/SKILL.md`'s table of variants: your stage is named here.
Read `task-cycle/skill/return_step.md` whole (the worktree's copy); it holds what you compare and
write. Read the skill of an element (`elements/<element>/skill/SKILL.md`) when you write an entry of it.

- Worktree: `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions`, branch `task/glossary-three-questions`,
  head `049e84e9fdea1784f348b29e7f20f33491e02ec5` (the reviewed head, `PASS` of the review of the fix; the
  full gate was run on it by the orchestrator). Commit by explicit paths, English messages, nothing under
  `.runs/`. If you commit anything, say so with the range; a fresh reviewer then reviews that range.
- The frozen task: `docs/task-cycles/glossary-three-questions/task.md`.
- The entries the change writes or changes: WAY-11, WAY-95, WAY-97, WAY-99, WAY-104, WAY-293 in
  `foundations/decisions.md`, with the files `elements/glossary/template.md`, `task-cycle/review/SKILL.md`,
  `elements/common/way_of_working.md`, `elements/glossary/skill/decide_entry.md`, `task-cycle/record_template.md`,
  `task-cycle/skill/return_step.md`. The part map: `foundations/part_map.md` (parts `decisions`, `glossary`,
  `task-cycle`, `elements-common`). The task named WAY-95, 97, 99, 104, 161, 263, 226, 72, 171 as decisions in play.
- Reports you may need: your `author.md`, `fix-1.md`; the reviews `review-1.md` and `review-fix-1.md`, where the
  Minor and out-of-scope findings stand — those are not fixed (WAY-161) and are no foundation entries; the
  return step is not a place to fix them.
- Do not run the product's gate. Run the focused checks of what you change, if you change anything
  (`python -B elements/common/foundation_check.py .` and `python -B gate/run_tests.py <directory>`).
- Report to: `docs/task-cycles/glossary-three-questions/reports/return-step.md`
  with, in this order, the fields the record's *Return step* section holds (foundation compared with code;
  decisions, invariants, environment facts, glossary terms, part-map changes, projected entries, rows of
  *Settlements to record* written — each an identifier or `none`) and **Searches not found or unclear**.
  Return only: status, commits (or `none`), a one-line check result, report path.
