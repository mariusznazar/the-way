# Handoff — the return step

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator
(`implement-task`); nothing here is that person's approval. Do not ask the human; questions go to
the orchestrator in your report.

## Where and what

- Worktree: `the root of the task's worktree (the repository root)`; branch
  `task/invariant-method-on-finished-change`; base `46bba355e51bc671a4af604e11757d91574949b6`;
  reviewed head `7c3161a` (whole-change review `PASS e3fcc20`, review of the fix `PASS 7c3161a`).
- You are the one author, resumed. Stage: the return step (step 11 of `implement-task`). Read
  `task-cycle/skill/return_step.md` in full and follow it; read the skill of an element when you write
  an entry of that element. Commit by path, English message, do not push. Do not run the full gate
  (the orchestrator is running it now on `7c3161a`; do not change tracked files until you are told
  it finished — this message is sent after it did).
- Frozen task: `.runs/task-cycles/invariant-method-on-finished-change/task.md`.

## What to compare

- The entries the change wrote or changed: WAY-61, WAY-321, invariant `test-method-citation`; the
  entries the task names (*Decisions in play*: WAY-61, WAY-16, WAY-65, WAY-63, WAY-160); the entries
  your search of the foundation (WAY-33) found; the part map of the touched parts (`decisions`,
  `invariants`, `elements-common`, `foundation-check-command`) — each with the code and the files of the
  repository. Correct in the same change whatever no longer matches.
- Rows of *Settlements to record*: rows 1–3 are written (row 1 WAY-61, row 2 WAY-321, row 3
  `test-method-citation`); confirm, and write nothing a row did not set.
- The return step writes an invariant only for a rule the task, a decision or the human sets; the
  rule here is row 3's. Write no environment fact or glossary term unless `return_step.md` calls for
  it (WAY-95 test for words such as "citing test", "finished change").
- Known open points to judge, not to widen: WAY-61's *Scope* does not name `task-cycle` (the
  author's earlier note); the six statements of the cycle's gate runs (`task-cycle/plan/SKILL.md`
  `:169-172`) — the task's *Context* records, for a planned slice, that the invariant test
  `test_the_way_foundation_passes` reports a `test` entry written before its test; the task carries no
  item for it. Report them; change nothing outside the task.

## Report

Write `.runs/task-cycles/invariant-method-on-finished-change/reports/return-step-report.md`: for each
comparison what no longer matched and its correction or `none`; decisions, invariants, environment
facts, glossary terms, part-map changes and rows written or `none`; the commits (or `none` if you
changed nothing); **Searches not found or unclear**. Return status, commits, one-line check result
and the report path.
