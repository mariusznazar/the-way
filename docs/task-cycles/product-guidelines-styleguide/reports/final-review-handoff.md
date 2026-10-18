# Whole-branch review handoff

The final whole-branch review of a the-way task cycle, by Superpowers 6.4.1
`requesting-code-review` with its template
`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md`
(read it whole and follow its output format, including *Declined to judge*). You made none of this
change. Read-only on the checkout; for anything you run, use a detached worktree
(`git -C C:/Storage/repos/the-way-wt/product-guidelines-styleguide worktree add --detach C:/Storage/repos/the-way-wt/pg-final-review 9dd9880`),
removed when done. No subagents. Return questions to the root orchestrator; never ask the human.

## What was implemented

Product guidelines for the-way, with the styleguide as the first guidelines: 26 decisions
(WAY-167–WAY-192) and an in-place edit of WAY-09; the glossary term "guidelines"; the part
`product-guidelines` with a surface; eight invariants (`foundations/invariants.md:2133-2212`) and
the renewal of six; the invariant checks `product-guidelines/test_form_check_invariants.py`; the
templates `product-guidelines/template.md` and `product-guidelines/styleguide/template.md`; the form
check `product-guidelines/form_check.py` with `test_form_check.py` (a trust boundary); the skill
`product-guidelines/styleguide/SKILL.md` (`maintain-styleguide`) and all regenerated entry points;
the installer's skill list, guidance sentence, README and tests.

## Requirements

- The frozen task `.runs/task-cycles/product-guidelines-styleguide/task.md` — binds; its 27 rows of
  *Settlements to record* carry meanings the human accepted (each must be written as an entry of its
  kind, its meaning unchanged), its *To do* 1–11, *Out of scope*.
- The reviewed spec `.runs/task-cycles/product-guidelines-styleguide/spec.md` and the plan
  `.runs/task-cycles/product-guidelines-styleguide/plan.md` (with *Coverage*); the root's rulings
  C5–C30 in the questions table of `.runs/task-cycles/product-guidelines-styleguide/cycle.md`.
- The repository's foundation as it stands at the head, and `agent-instructions/README.md`.

## Range

Base `96623ed` (the `foundations` commit the branch left), head `9dd9880`. Review package (commit
list, stat, full diff with context, 390 KB):
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.superpowers/sdd/plan-tasks/review-96623ed..9dd9880.diff`.
If it does not fit one read, review it in passes and say so.

## Ledger lines to grade

The method's ledger holds deferred minor findings, rulings and notes from the slice reviews:
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.superpowers/sdd/plan-tasks/final-review-ledger-lines.md`
(as the method wrote them). In your own report, grade each `minor (deferred)` line and each `note`
line as a finding of this review — Critical, Important or Minor, or outside the task's scope — with
its place in the code, after checking it against the head.

## Evidence available

Slice reports and reviews in `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.superpowers/sdd/plan-tasks/`
(`task-N-report.md`, `task-N-review.md`, re-reviews); deliberate-break outputs
`.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-*.txt`, `slice-3-break-*.txt`;
the root's full run of the available checks at head in
`.runs/task-cycles/product-guidelines-styleguide/reports/completed-*.txt` and `completed-checks.json`.
Do not re-run whole suites to confirm them; run a focused check only for a specific doubt.

## Report

Write the full report to
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/reports/final-review.md`
in the template's format (Strengths; Issues Critical / Important / Minor with file:line, what, why,
fix; *Declined to judge*; Recommendations; Assessment with **Ready to merge?**), plus a section
"Ledger lines graded". Return only: the verdict, counts by severity, the blocking findings'
one-liners, the report path.
