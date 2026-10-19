# Affected code review handoff — coding guidelines (task cycle step 11, after the assessment's settlement)

You review the range `5a00041..a839ea7`; you wrote none of it, no check and no invariant sentence of
this task. Follow the Superpowers 6.4.1 code-reviewer template, read whole from
`/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/superpowers-6.4.1/skills/requesting-code-review/code-reviewer.md`
(its "Declined to judge" list included). Read-only on `/home/user/the-way`; scratch worktrees
under the scratchpad, removed after. Never use the Artifact tool or a publishing tool; never ask
Mariusz anything.

- **What changed in the range:** the return step `355a240` (invariant `guidelines-check-kind-index/1`
  edited in place: "git lists" → "git tracks"; part `task-cycle` *Depends on* gains
  `product-guidelines`); ruling C39 `f34e477` (the coding skill's audit covers every kind the product
  holds files of — no deferral); C40 `28b42a2` (invariant test: an untracked kind file is no error;
  rename); the independent assessment's settlement (`reports/assessment-settlement.md`):
  `a677bc4` (WAY-203 reworded, WAY-204 renewed), `8242720` (styleguide template and skill point to
  the test cases), `a839ea7` (two invariant tests).
- **Requirements:** frozen task `docs/task-cycles/coding-guidelines/task-frozen.md` (row 7 for
  WAY-203, rows 3 and 22 for the skill, row 11 and C19 for test cases), spec `spec.md`, the
  assessment `reports/assessment.md` (remarks I1–I3) and its settlement, rulings C39–C40 in
  `cycle.md`.
- **Package:** `reports/affected-review-package.diff`.
- **Deliberate breaks** (WAY-69, WAY-08), each from the invariant's final sentence in
  `foundations/invariants.md`, in a scratch worktree at `a839ea7`, running
  `python3 -B gate/run_tests.py product-guidelines`, recording that a test citing the invariant
  fails (outputs `reports/affected-break-*.txt`):
  1. `guidelines-check-kind-index/1` as edited ("git tracks"): make the check count an untracked
     `guidelines/coding.md` (and untracked kind files) as present.
  2. `guidelines-check-example-files/1`, clause "a block left open to the end of the file": make the
     check treat the end of the file as closing an open block.
  3. `guidelines-check-kind-index/1`, a row whose *File* names a tracked file not of the form
     `guidelines/coding-<kind>.md`: drop that report.
  An undetected break is a finding.
- Grade findings Critical/Important/Minor with file:line; mark findings outside the task's scope.

Write your report to `reports/affected-review.md`; return verdict, counts, blocking findings, and
each break's result.
