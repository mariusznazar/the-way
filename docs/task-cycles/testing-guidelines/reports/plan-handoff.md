# Handoff — planner (plan-task), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the planner. Follow the project skill `the-way-plan-task` (read
`task-cycle/plan/SKILL.md` in this worktree whole, and what it names). Write no code and nothing
into `foundations/` or any tracked file; write only `plan.md`, `plan-size.md` and your report.
Questions go to the orchestrator in your report (status `questions`), never to the human. Where you
meet an open design choice the spec leaves, return it instead of a plan.

## Worktree and paths

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  base `4302f72ba638fb222fc3d9de73decacdf7ca6682` (`foundations`), HEAD equal to the base. The-way is
  the top-level repository; integration route and test command in `agent-instructions/README.md`
  ("Check the change": `python -B gate/run_tests.py` and `python -B gate/run_tests.py <directory>`).
- Frozen task (read whole): `.runs/task-cycles/testing-guidelines/task.md`.
- Reviewed spec (read whole): `.runs/task-cycles/testing-guidelines/spec.md` — reviewed by a fresh
  agent: first review FAIL, revised once, re-review PASS (`reports/spec-review.md`, section
  "Re-review of the revision"). Its *Decisions* and *Foundation entries* bind the plan.
- Write: `.runs/task-cycles/testing-guidelines/plan.md`, the size report
  `.runs/task-cycles/testing-guidelines/plan-size.md` (from `task-cycle/slice_size.py` as the method
  gives), and your full report `.runs/task-cycles/testing-guidelines/reports/plan.md`.

## Answers of step 4 and the cycle's rulings

- Trust boundary: yes — `installation/install.py` (part `installation`). Mark the slice that
  changes it with that *Risk*.
- Irreversible operation: no.
- C3: row 25 is carried by *Based on* / *Rejected* of other decisions, no decision of its own.
- C4: WAY-242 carries WAY-200's split; one bullet in `product-guidelines/reading.md` like WAY-216's;
  the testing skill mirrors only the coding skill's "A new kind" mode.

## What to read

- The whole frozen task and the whole spec; the designer's report `reports/design.md` and the spec
  review `reports/spec-review.md` for evidence where needed.
- The files the spec names as changing, enough to size the slices: `product-guidelines/**`,
  `installation/install.py`, `installation/README.md`, `installation/test_install.py`,
  `installation/test_coding_guidelines_installation.py`, `agent-instructions/skill_entry_points.py`,
  `project-level/task/skill/SKILL.md`, `project-level/plan/skill/SKILL.md`, the-way's `README.md`,
  `foundations/decisions.md` (the entries edited in place: WAY-174, WAY-214, WAY-215, WAY-218,
  WAY-228), `foundations/glossary.md` (`exemplar`), `foundations/environment_facts.md`.
- The foundation entries each slice's *Read* should name: the decisions of the task's *Decisions in
  play* (WAY-08, WAY-13, WAY-16, WAY-48, WAY-51, WAY-121, WAY-167, WAY-168, WAY-171, WAY-172,
  WAY-173, WAY-174, WAY-198, WAY-199, WAY-200, WAY-209, WAY-212, WAY-213, WAY-214, WAY-215, WAY-218,
  WAY-228), and, by part, decisions whose *Scope* names `product-guidelines` (WAY-02, WAY-09, WAY-27,
  WAY-51, WAY-100, WAY-102, WAY-120, WAY-167–WAY-174, WAY-176–WAY-178, WAY-180, WAY-182–WAY-187,
  WAY-189, WAY-191, WAY-192, WAY-198–WAY-219, WAY-221, WAY-228) and `installation` (WAY-09, WAY-27,
  WAY-34, WAY-38, WAY-89, WAY-100, WAY-102, WAY-107, WAY-127, WAY-141, WAY-167); invariants
  `skill-entry-points`, `skill-rule-source`, `installation-claude-guidance`, `generated-overview`
  and those of `every` a slice's files reach. The-way has no `guidelines/` of its own.

## What the plan must hold

As the method gives: *Foundation entries* (the twenty new decisions WAY-231–WAY-250, the five edits
in place, the glossary edit, the environment facts) written before slice 1 by one agent through the
element skills, unless you show why another order is needed; then slices in order, each with
*Change*, *Read*, *Model*, *Risk*, checks that can actually run and their commands, and *Choices*.
Cover every *To do* item, every row of *Settlements to record* (row 25 as tied per C3), and every
entry of the spec's *Foundation entries*. Include the entry-point generator run
(`python -B agent-instructions/skill_entry_points.py --write`) and its committed output.

## Report

Return a short message: status, the paths of `plan.md`, `plan-size.md` and your report, and a
one-line check result naming what failed or did not run.
