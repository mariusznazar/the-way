# Handoff to the reviewer of the whole change — own-measurement-in-decision

You are a reviewer that made none of this change. Review the whole change of one task of the-way
with `review-change`: read `task-cycle/review/SKILL.md` in the worktree whole, and a file it names
only when the step that names it comes. You are read-only; you return `PASS <sha>` or `FAIL <sha>`
as your report's first line, graded findings and the checks you ran. Select your own foundation and
guidelines by the parts of the change (`elements/common/way_of_working.md`, "Reading the
foundation"; WAY-150), and state in your report how many decisions you read whole and how many by
title only.

- Worktree (work from its root): `the root of the task's worktree`
- Range: base `3c572b95e86a1a4e6b0373b7fb11c3e7c6b00ead` to head `c76debc` (one commit, three files:
  `foundations/decisions.md`, `elements/decisions/template.md`, `elements/environment-facts/template.md`).
- Frozen task, read whole: `.runs/task-cycles/own-measurement-in-decision/task.md` (the task's
  *Settlements to record* rows 1 and 2 and *To do* items 1–3 are what the change must carry out;
  the answer to its question 3 is WAY-33).
- The author's report: `.runs/task-cycles/own-measurement-in-decision/reports/author-report.md`.
- No spec, no plan (one author without a plan). No slice. The pin is not moved.
- Trust boundary of the change: no. Irreversible operation: no.
- Foundation entries in play, by identifier: WAY-90 (edited in place), WAY-27, WAY-05, WAY-80,
  WAY-33, WAY-07, WAY-134, WAY-150, and the decisions the change gave the sentence: WAY-229, 164,
  364, 136, 371, 255, 300, 308, 309, 316, 319, 320, 323, 350, 352, 353, 362, 368, 369.

## What the orchestrator decided after the author returned (judge them, do not take them as settled)

1. WAY-312 is named by the task's item 3 but left unchanged: its *Based on* fact
   `shorter-guidelines-trial` has a source that opens (a report at a fixed commit of a public
   repository), so the sentence "its record is not open" would be false there.
2. WAY-256 (an estimate from word counts of one skill the entry does not name) is left unchanged.
3. The sentence stands in *Rejected* too where the figures stand there (WAY-136, 164, 364).
4. The author added the sentence to 14 decisions the task does not name (WAY-255 … 369), found by the
   whole-foundation search of WAY-33. Check each against WAY-90's new rule: is its figure a measurement
   of the product's own people whose record a reader of this repository cannot open? Say which are
   not (borderline per the author: WAY-362, WAY-320, WAY-323, WAY-300).
5. No wording of a decision's binding sentence, *Scope*, *Based on* or other fields except WAY-90
   may change; check that.

## Also check

- That WAY-90's change, the two templates and the rationale sentences say the same thing, and that
  the new rule does not collide with WAY-27, WAY-05, WAY-80 or another decision or invariant (the
  task exists because two rules collided).
- That no entry now points to a source a reader cannot open, and the sentences add no history of how
  a decision was reached (WAY-05).
- The checks you can run read-only: `python -B elements/common/foundation_check.py --skip-test-citations`
  and `python -B task-cycle/private_paths_check.py` on the three changed files. Do not run the full gate;
  the orchestrator runs it.

Write your full report to `.runs/task-cycles/own-measurement-in-decision/reports/reviewer-whole-report.md`
with **Unread material**, **Searches not found or unclear**, each finding with its grade as
`review-change` gives and whether it is outside the task's scope, and the checks with command and exit
code. Return the first line, the changed files with line counts and the report path.
