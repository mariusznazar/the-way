# Handoff — return step (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You take the cycle's return step on the planned route, as a fresh agent. Follow
the project skill `the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole)
and read whole step 11 of `task-cycle/skill/SKILL.md` ("Take the return step: …", lines 317–331),
which holds this stage, with the element skills it names (`the-way-record-decision`,
`the-way-record-glossary-term`, `the-way-record-environment-fact`, `the-way-update-part-map`,
`the-way-record-invariant`). `agent-instructions/README.md` ("Make the change") gives the-way's own
form of the return step: it does not hunt for behaviour no invariant covers. Correct in the same
change whatever no longer matches; defer no entry; write an invariant only for a rule the task, a
decision or the human sets. Review findings are no foundation entries. Questions go to the
orchestrator; never ask the human.

## Worktree, range and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  reviewed head `a2f11659043955f741c5c51a88d36f9f981572b2` (whole change `4302f72..a2f1165`,
  review of the whole change FAIL → fix `a2f1165` → PASS).
- Commit with explicit paths, English messages, author `mariusznn@gmail.com`; no push; clean tree.
  Commit nothing if nothing needs correcting, and say so.
- Report: `.runs/task-cycles/testing-guidelines/reports/return.md`.

## Answers of step 4 and rulings

- Trust boundary: yes (`installation/install.py`, slice 5, reviewed). Irreversible operation: no.
- C3 (row 25 tied to WAY-233, 235, 236, 237, 238, 241, 243), C4 and C13 (WAY-242's split: refinement
  approves a level's first exemplar only where the task's required behaviour is a test of that level;
  otherwise a blocked draft request), C10 (WAY-235 narrows WAY-168), C11, C12 — see the reports.

## What to compare

- The entries the change writes or changes: decisions WAY-231–WAY-250 (new), WAY-174, WAY-214,
  WAY-215, WAY-218, WAY-228 (edited), glossary `exemplar` (edited), environment facts
  `llm-test-oracle-actual-behaviour`, `computer-use-agent-web-testing` (new) — against the code as it
  now stands: `product-guidelines/testing/template.md`, `product-guidelines/testing/SKILL.md`,
  `product-guidelines/coding/template.md`, `product-guidelines/coding/SKILL.md`,
  `product-guidelines/reading.md`, `project-level/task/skill/SKILL.md`,
  `project-level/plan/skill/SKILL.md`, `installation/install.py`, `installation/README.md`,
  `README.md`.
- The entries the task names (*Decisions in play*: WAY-08, WAY-13, WAY-16, WAY-48, WAY-51,
  WAY-121, WAY-167, WAY-168, WAY-171, WAY-172, WAY-173, WAY-198, WAY-199, WAY-200, WAY-209, WAY-212,
  WAY-213) and those the foundation agent's searches found (`reports/foundation.md`).
- The part map of the touched parts: `product-guidelines`, `installation`, `agent-instructions`,
  `project-level`, `decisions`, `glossary`, `environment-facts` (does each part's responsibility,
  files and *Depends on* still match?).
- Rows of *Settlements to record* (frozen task `.runs/task-cycles/testing-guidelines/task.md`) the
  code makes true that the foundation step missed; sources outside the product the change rests on
  that the foundation does not hold; words used in a meaning other than the usual one or against
  their entry; choices that bind after the merge (WAY-36).
- For orientation: the spec `.runs/task-cycles/testing-guidelines/spec.md` and the review
  `reports/whole-review.md` (its Minor findings are not yours to fix).

## Checks

Run and report with command and exit code: `python -B elements/common/foundation_check.py`,
`python -B agent-instructions/skill_entry_points.py`, `python -B gate/run_tests.py elements/common`,
and `git diff --check a2f1165` if you commit. Return: status, commits (or none), a one-line check
result, the report's path.
