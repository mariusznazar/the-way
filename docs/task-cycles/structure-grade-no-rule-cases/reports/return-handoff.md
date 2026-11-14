# Handoff — the return step

You are the one author of this change, resumed for the return step, on your class (`cheaper`). The
whole-change review returned `PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8` with no finding of any
grade, so no fix runs.

- Worktree: `the root of the task's worktree`, branch
  `task/structure-grade-no-rule-cases`, head `5554f5d`, base `1be90579bf3daa618dd87c06bd56042eabb642c1`.
- Stage: the return step. Read `task-cycle/skill/return_step.md` whole (it names the foundation step
  by `task-cycle/skill/foundation_step.md`, which you have read; read the `SKILL.md` of an element
  at the path it gives when you write an entry of that element). Compare, as it gives, the
  foundation entries the change edits (WAY-363), those the task names (WAY-362, WAY-360), those
  your search of the foundation found, and the part map of the touched parts, with the files of the
  repository, and correct in the same change whatever no longer matches. Write no invariant for
  behaviour merely because none covers it.
- Frozen task: `docs/task-cycles/structure-grade-no-rule-cases/task.md`. Your earlier report:
  `docs/task-cycles/structure-grade-no-rule-cases/reports/author-report.md`. The review's report is
  yours to read only through this: it found no blocking finding and no Minor finding, and said that
  `task-cycle/review/whole_change.md` already covers the third case through "the product's
  guidelines hold no such rule".
- Do not run the whole gate; the orchestrator runs it. Run the focused checks the step calls for
  with command and exit code.
- If the step finds nothing to change, commit nothing and say so.

## Report

Write the full report to
`docs/task-cycles/structure-grade-no-rule-cases/reports/return-report.md`
with the fields the record's *Return step* section lists (foundation compared with code, decisions
written or changed, invariants, environment facts, glossary terms, part-map changes, projected
entries, rows of *Settlements to record*), and **Unread material** and **Searches not found or
unclear** sections (`none` where there is nothing). Return status, commits, a one-line check result
and the report's path.
