# Affected review handoff

You reviewed this branch's whole change (`96623ed..9dd9880`) and the fix `896071a`. Since then the
return step and two settlements changed code, foundation entries and an invariant test. Review
that range once, by the same template you used
(`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md`,
*Declined to judge* included). You wrote none of it. Read-only on the main checkout; anything you
run goes in a detached worktree
(`git -C C:/Storage/repos/the-way-wt/product-guidelines-styleguide worktree add --detach C:/Storage/repos/the-way-wt/pg-affected-review e549363`),
removed when done. No subagents.

- Range: `896071a..e549363`, 10 commits, 9 files. Review package:
  `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.superpowers/sdd/plan-tasks/review-896071a..e549363.diff`.
- What it carries:
  - the return step `19d28f8` (WAY-167, WAY-186, `guidelines-form/1` sentence) and its settlement by
    the root's ruling C32 (`.runs/task-cycles/product-guidelines-styleguide/cycle.md`, questions
    table): WAY-167 restored to one file per discipline (`c355004`), the F4 naming cases narrowed
    by the check author (`4a4f08e`), the form check narrowed (`d1585d0`), the template's copy of
    the reworded sentence (`677ef7c`);
  - the settlement of the independent assessment, as
    `.runs/task-cycles/product-guidelines-styleguide/reports/assessment-settlement.md` gives it
    (which remarks were applied, by whom, and why the others were rejected): `04f8754`, `8ff8966`,
    `35860df`, `3550497`, `e549363`.
- Requirements: the frozen task `.runs/task-cycles/product-guidelines-styleguide/task.md` (its 27
  rows bind; check that no change here gives a row another meaning), the settlement file above,
  ruling C32, and the foundation at head.
- Evidence: `.runs/task-cycles/product-guidelines-styleguide/reports/foundation.md` (sections
  "Return step" and "Assessment settlement"), `check-author.md` (last section),
  `.superpowers/sdd/plan-tasks/task-1-report.md`, `task-2-report.md`, `task-4-report.md` (their
  settlement sections), and outputs `return-*.txt`, `return-c32-*.txt`, `settlement-*.txt` in
  `.runs/task-cycles/product-guidelines-styleguide/reports/`. Do not re-run whole suites to confirm
  them.

Also, because checks and sentences changed:

1. **Deliberate break of the naming guard (WAY-69, WAY-08).** In your worktree, remove or invert
   the guard in `product-guidelines/form_check.py` that refuses a part in the name of a
   non-styleguide discipline's file (`d1585d0`), run `python -B gate/run_tests.py product-guidelines`,
   and record whether the tests citing `guidelines-check-form/1` fail. Save command, exit code and
   output to `.runs/task-cycles/product-guidelines-styleguide/reports/affected-break-naming.txt`.
   Restore and remove the worktree.
2. **Sentences reworded over unchanged checks:** `guidelines-form/1` (`19d28f8`) and
   `guidelines-check-carrier/1` (`04f8754`). Judge whether each check still gives a verdict for
   exactly what its sentence now says, and whether a test could pass while the sentence is false.

Append your report as a new file
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/reports/affected-review.md`
in the template's format (Strengths; Issues Critical / Important / Minor with file:line, what,
why, fix; *Declined to judge*; Assessment with **Ready to merge?**), plus "Deliberate break" and
"Reworded sentences" sections. Return only: the verdict, counts by severity, blocking findings'
one-liners, the break result, the path.
