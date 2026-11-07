# Handoff — the return step (step 11), the one author resumed

Worktree: `C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions` (work from its root),
branch `task/merge-review-questions`, head `a5d6d5f`. The whole change passed its review (`PASS 3601aba`)
and the fix of its Minor findings passed its own (`PASS a5d6d5f`); the orchestrator's gate on `a5d6d5f`
exited 0 (765 tests in 9 directories).

Take the return step as `task-cycle/skill/return_step.md` gives — read it whole (it is in this
worktree; note that the change itself edited that file: read the version at head). Read
`task-cycle/skill/foundation_step.md` whole too, since the return step writes as the foundation step
writes. Compare with the code the entries the change writes (WAY-306, WAY-307), those the task names
(*Decisions in play*: WAY-150, WAY-162, WAY-11, WAY-135) and those the search of the foundation found,
and the `task-cycle` entry of the part map, and correct in the same change whatever no longer
matches. Rows of *Settlements to record*: both are written (WAY-306 = row 1, WAY-307 = row 2); the
entry for *To do* 2 is no entry by the task (WAY-11 unchanged). The task and its answers bind; the five
sentences of *To do* 1–4 stay as they are. Frozen task:
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\task.md`.

If nothing no longer matches, commit nothing and say so. If you commit, commit by explicit paths, English
message, no push, no whole gate.

Report in full to
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\reports\09-return-step-report.md`
with the fields of the record's *Return step* section (foundation compared with code, decisions written
or changed, invariants, environment facts, glossary terms, part-map changes, projected entries, rows of
*Settlements to record* written), each check's command and exit code, and **Searches not found or
unclear**. Return status, commits, one-line check result and the report path.
