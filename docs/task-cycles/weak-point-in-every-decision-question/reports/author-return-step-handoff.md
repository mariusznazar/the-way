# Handoff — the return step

You are the one author, resumed, for the return step of the cycle.

- Method for this stage: `task-cycle/skill/return_step.md` (read whole), which writes as
  `task-cycle/skill/foundation_step.md` writes; no variant row of `make-change` applies, the stage is
  the return step. Read the `SKILL.md` of an element (`elements/<element>/skill/SKILL.md`) when you
  write an entry of that element.
- Worktree `the root of the worktree`, branch
  `task/weak-point-in-every-decision-question`; the change as reviewed and fixed is at head
  `d542af0` (whole-change review PASS `a3c97df`, fix review PASS `d542af0`). Base `bfb2e10`.
- Frozen task: `.runs/task-cycles/weak-point-in-every-decision-question/task.md`. No spec, no plan.
- Compare the foundation entries the change edits (WAY-113, WAY-155, WAY-174, WAY-378), those the
  task names (WAY-123, WAY-100) and those your search of the foundation found, and the part map of
  the touched parts, with the files of the repository, and correct in the same change whatever no
  longer matches. It writes an invariant only for a rule the task, a decision or the human sets.
- Two things the reviewers left to you to look at: (1) the part map's *Depends on* of
  `process-audit` against the new text pointers from `process-audit/SKILL.md` to
  `elements/common/way_of_working.md` (the reviewer found no rule that governs text pointers; decide
  by the part map's own rules and say so in the report); (2) the new Minor of the fix review
  (`project-level/lead/skill/route_changes.md:19` 111 characters, `task-cycle/skill/request_template.md:425`
  140 characters, against a wrap of about 100) — the reviewer marked it Minor and the cycle does not
  fix it, so leave it unless your own comparison needs those lines.
- Checks: `python -B elements/common/foundation_check.py` and focused `python -B gate/run_tests.py
  <directory>` for each directory you change; never the full gate (the orchestrator's). Commit by
  path only if the comparison finds something to correct; where nothing needs correcting, commit
  nothing and say so.
- Directory for working copies: `.runs/author/` (as before).
- Report path: `.runs/task-cycles/weak-point-in-every-decision-question/reports/author-return-step-report.md`,
  with the sections the method gives, **Unread material** and **Searches not found or unclear**.
