# Handoff — the return step (resumed one author)

You are resumed as the one author of this cycle, for the return step. The orchestrator's
delegation and answers in `reports/author-handoff.md` stand. Nothing here is a human's approval.

- Stage: **the return step** (step 11 of `implement-task`). It takes none of `make-change`'s
  variant rows. Read whole `task-cycle/skill/return_step.md`, and `task-cycle/skill/foundation_step.md`
  because the return step writes as the foundation step writes; read the skill of an element when you
  write an entry of that element.
- Worktree: `the task's worktree root`, branch
  `task/backlog-line-for-plan-tasks`, head `9d5743d7648b4a5095fba28a7d6ab100cd078c3b`, tree clean.
  The change so far: `74fbd01`, `9eb2bd6`, `9d5743d` over base `52f8164`.
- Frozen task: `docs/task-cycles/backlog-line-for-plan-tasks/task.md` (read whole; *Settlements to
  record* rows 1-5, *Decisions in play*).
- What to compare with the files of the repository, and correct in the same change:
  - the entries the change writes or changes: WAY-154, WAY-107, WAY-320, WAY-27;
  - the entries the task names: WAY-144, WAY-147, WAY-328 (unchanged by the task, compare only);
  - the entries the search of the foundation found for you, and the part map of the touched parts
    (`decisions`, `project-level`, `agent-instructions`; the fix also touched three files of
    `product-guidelines`, so read its map entry too);
  - the rows of *Settlements to record* 1-5, each made true by the entries and the skill text.
- Choices of the cycle that may bind after the merge (WAY-36) and that you decide on as the return
  step gives: Q1, the derivation of the `🆔` identifier (record `cycle.md`, Q1, and your own choice
  1 of `reports/author-report.md`, with what the fix added about its assumptions in
  `project-level/task_line.md`); your choices 2-5 of that report (the new file
  `project-level/task_line.md`; a task with an existing line; the placement of the orchestrator's
  correction of dependencies in `route_changes.md`; a refiner writing the `task-rules` entry after
  the human's agreement); and the fallback the review asked for in B1 (a line made late, and made
  ready by the orchestrator at acceptance where none stands). For each, write an entry where
  WAY-36 requires it, or leave it a row of the questions table, and say which and why in your
  report.
- Settlement rows the foundation step wrote: your report names row and identifier for each.
- You write an invariant only for a rule the task, a decision or the human sets; never for
  behaviour merely because no invariant covers it. No entry is deferred.
- Checks: `python -B elements/common/foundation_check.py` and, for any file you change,
  `python -B instruction-files/check_instructions.py .`, each with command and exit code. Not the
  `project-level` directory and not the full gate; the orchestrator runs it after the return step.
- Commits: explicit paths, English messages, on the task branch. If you commit nothing, say so and
  why.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/return-report.md`
  — for each compared entry and the part map what no longer matched and its correction, or none;
  decisions, invariants, environment facts, glossary terms, part-map changes, projected entries and
  settlement rows written or changed, or none each; **Unread material**, **Searches not found or
  unclear**, your own-work check, the checks with commands and exit codes. Return status, commits,
  a one-line check result and the report path.
