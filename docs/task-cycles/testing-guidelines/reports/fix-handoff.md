# Handoff — fix of the whole-change review's blocking finding (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You fix the blocking finding of the review of the whole change. Follow the project
skill `the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as the agent fixing a review's findings. The finding concerns the foundation entries and
slices 3 and 4, so you are a fresh agent on the same branch. Fix only this finding; Minor findings
are not fixed. Where you hold the finding wrong, answer with evidence in your report instead.
A decision you change goes through `the-way-record-decision` (its step 1 selection and its search
of the whole foundation once the change is settled). Questions go to the orchestrator; never ask
the human.

## Worktree, range and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`.
- Reviewed head: `3bd9e37b60cb4c91613dddfa517c445841016688`; your fix range starts there.
- Commit with explicit paths, English messages in the style of `git log`, author
  `mariusznn@gmail.com`; no push; leave the worktree clean.
- Findings file (the finding in the reviewer's words): `.runs/task-cycles/testing-guidelines/reports/fix-findings.md`.
- Full review for context: `.runs/task-cycles/testing-guidelines/reports/whole-review.md`.
- Report: `.runs/task-cycles/testing-guidelines/reports/fix.md`.

## The orchestrator's choice of the way out (C13)

Way (a) of the finding, which stays within rows 8 and 12 and mirrors WAY-216 (refinement assigns
the designation only where refinement knows the task creates the first instance):
- WAY-242's "where it has none" clause: the designation of a level's first exemplar test is approved
  in refinement only where the task's required behaviour itself is a test of that level (e.g. a
  task whose outcome is the product's first end-to-end test); refinement then names the level and
  that the task's first test of it becomes the exemplar — never a list of tests or their paths
  (WAY-238).
- Otherwise, where the cycle's author chooses a level whose recipe has an empty *Exemplar*, the
  designation goes to the human at a blocked draft request, as WAY-172 already provides.
- Adjust in the same way what follows from it: WAY-242's *Verification* examples; the WAY-218 edit
  where it places the designation in the breakdown; the skill's "A new level"
  (`product-guidelines/testing/SKILL.md`, around 162-164 — no path settled in refinement); the
  reading bullet (`product-guidelines/reading.md`, around 77-79); `project-level/task/skill/SKILL.md`
  (around 170-172) and `project-level/plan/skill/SKILL.md` (around 121-123); and the template's
  *Exemplar* recipe field text if it says otherwise. WAY-238 stays as it is.
- No new mechanism: the blocked draft request route exists in `task-cycle/skill/SKILL.md`; you
  change nothing under `task-cycle/`. The change must not widen beyond the finding.

## Answers of step 4

- Trust boundary: yes (`installation/install.py`) — your fix does not touch it.
- Irreversible operation: no.

## What to read

- The whole frozen task `.runs/task-cycles/testing-guidelines/task.md` (rows 8 and 12, Q7, To do
  item 1's exemplar bullet) and the spec's D3/D5/D6 and *Foundation entries*
  (`.runs/task-cycles/testing-guidelines/spec.md`).
- Foundation, each whole: WAY-25, WAY-172, WAY-198, WAY-199, WAY-200, WAY-216, WAY-218, WAY-238,
  WAY-242 (find each by `### WAY-<n> —` in `foundations/decisions.md`); glossary `exemplar`.
- The files the finding names, whole: `product-guidelines/testing/SKILL.md`,
  `product-guidelines/testing/template.md` (recipe *Exemplar* field), `product-guidelines/reading.md`,
  `project-level/task/skill/SKILL.md` step 3, `project-level/plan/skill/SKILL.md` step 2.

## Checks

Run and report with command and exit code: `python -B elements/common/foundation_check.py`,
`python -B agent-instructions/skill_entry_points.py` (entry points current),
`python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py elements/common`,
`git diff --check 3bd9e37`. Return: status, commits, a one-line check result, the report's path.
