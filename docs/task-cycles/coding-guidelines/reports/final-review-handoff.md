# Final whole-branch review handoff — coding guidelines (task cycle step 9, "The end of a code review")

You are the final whole-branch reviewer. You did not write any of this change. Follow the
Superpowers 6.4.1 code-reviewer template, read whole from
`/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/superpowers-6.4.1/skills/requesting-code-review/code-reviewer.md`
(the prompt inside its fenced block is your instruction; it includes the "Declined to judge" list).
Read-only on `/home/user/the-way`; for a working copy use `git worktree add` under the scratchpad
and remove it after. Never use the Artifact tool or any publishing tool. Never ask Mariusz anything.

- **What was implemented:** the coding guidelines as the second discipline of the-way's product
  guidelines — 22 decisions (WAY-167 and WAY-168 edited in place, WAY-193–WAY-212 new), glossary
  terms "exemplar" and "standing check", part-map failure modes, `guidelines-check-carrier/1`
  edited in place, four new invariants, their invariant tests, the coding template, changes to the
  common template, the form check's two forms, kind index, exemplar and test-case checks, one
  sentence in the task-cycle skill, the skill `maintain-coding-guidelines` with 34 regenerated
  entry points, and the installer entry.
- **Requirements:** the frozen task `docs/task-cycles/coding-guidelines/task-frozen.md` (binding:
  *To do* 1–8, the answers to questions 1–18, all 25 rows of *Settlements to record*, *Out of
  scope*), the reviewed spec `docs/task-cycles/coding-guidelines/spec.md`, the plan
  `docs/task-cycles/coding-guidelines/plan.md`, rulings C1–C21 (`reports/design-rulings.md`) and
  C22–C37 (questions table of `cycle.md`).
- **Range:** BASE `235b0b4` (`foundations`), HEAD `2eabf42`. Review package (commit list, stat,
  full diff with context): `reports/sdd/final-review-package.diff`.
- **Grade the ledger's lines:** read `reports/sdd/progress.md`; grade, in your own report, each
  `minor (deferred)` line (and any `parked` line) as a finding of this review — Critical, Important
  or Minor, or outside the task's scope — so each becomes a finding of this review.
- **Also check, across the whole change:** every *To do* item, every row of *Settlements to
  record* and every entry the spec adds is present, with source fidelity (an entry's meaning is the
  row's, its wording the cycle's); foundation entries came before the code that depends on them
  (commit order); the deliberate breaks recorded per slice (`reports/sdd/slice-*-break-*.txt`) and
  the trust-boundary crafted-input tests (`product-guidelines/form_check.py`,
  `installation/install.py`); the orchestrator's final check run is in `reports/gate-final/`
  (all suites exit 0 except `instruction-files`, 3 platform failures present at the base; Python
  3.13.16, the repository declares 3.14).
- Grade every finding Critical, Important or Minor with file:line; mark a finding outside the task's
  scope as such, or list it under "Declined to judge".

Write your full report to `reports/final-review.md` and return: verdict, counts by grade, the
blocking findings (Critical/Important not outside scope) with places.
