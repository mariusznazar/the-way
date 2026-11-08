# Handoff — review of correction 1, `define-project` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle; after his remarks on the open
request the orchestrator dispatches this review. You did not make the change. You ask no human;
questions go back to the orchestrator (first line `questions`).

## Where you work

- Process root and worktree: `.`
  (branch `task/define-project-skill-shape`). Read every file from it. Read-only: write only your
  report (and scratch scripts named `review_correction_*.py` under the record's `reports/`).
- Record directory (ignored by git): `.runs/task-cycles/define-project-skill-shape/`.

## Stage

Your method: `task-cycle/review/SKILL.md`, read whole, and a file it names when its step comes.
Your review: **a later change to an open request** — a correction for the human's remarks.

Range: `a0c56bb..3f25d61` (one commit, "Apply the request's proposals 1, 4, 5 and 6 at the human's
request"; `a0c56bb` is the commit that removed the record's copy, so the code before the
correction is that of `09b0dd0`). Compute the diff yourself.

## What is reviewed against

- The human's remarks, which bind, in place of a findings file:
  `.runs/task-cycles/define-project-skill-shape/reports/remarks.md`. They widen the task's To do 3
  for proposal 6 alone.
- The proposals they apply: `.runs/task-cycles/define-project-skill-shape/reports/assessment.md`,
  section 4 (proposals 1, 4, 5, 6), as they stood before the correction:
  `git show` is not available for it (it is not tracked); the copy committed in `4f508f8`
  (`docs/task-cycles/define-project-skill-shape/reports/assessment.md`) holds that state.
- The frozen task: `.runs/task-cycles/define-project-skill-shape/task.md` (in Polish), whose
  acceptance criteria still bind every file of `project-level/skill/`: no rule disappears or
  changes meaning beyond what the remarks ask, every rewritten condition is compared with the base
  and adds or loses no route.
- The correction's report: `.runs/task-cycles/define-project-skill-shape/reports/correction_report.md`
  — claims to verify, not evidence; with the regenerated `assessment.md`, `word-counts.md` and the
  author's scripts (`check_correction.py`, `verify_counts.py`, `compare_sentences.py`,
  `make_assessment.py`, `check_pointers.py`).

Specifically:

1. Each of the four remarks made as `remarks.md` says, and nothing else: proposal 1 removes one
   sentence and the paragraph reads on; proposal 5 only the template's path; proposal 6 only the
   one phrase, in the skills whose `SKILL.md` has files beside it naming a skill, the author's
   reason for leaving `task-cycle/plan/SKILL.md` checked; proposal 4 only where "gate" means the
   readiness gate, fixed names kept, nothing in WAY-118, the template or the glossary.
2. No `description` of a skill, no Python and no `the-way-*` entry point changed.
3. The regenerated figures: recompute the ones the correction moved.

Answers of step 4: no trust boundary (the changed files are Markdown, none of them a file the
part map names as a trust boundary), no irreversible
operation.

The product's gate is the orchestrator's; run focused checks you need, each with command and exit
code.

## Report

Write the full report to `.runs/task-cycles/define-project-skill-shape/reports/correction_review_report.md`
as your method gives it; first line `PASS <sha>`, `FAIL <sha>` or `questions`; include
**Searches not found or unclear** as bullets, with nothing after that section. Return only: the
first line, the report path, a one-line check result, and each blocking finding in one line.
