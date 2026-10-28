# Handoff — return step, task `task-cycle-skills-shape`

You take the return step of a planned change in a the-way task cycle, as a fresh agent. The person
who requested this cycle has delegated intermediate choices to the orchestrator; send questions to
the orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`, head `7369993885567d683ef7b7a8b08933318c21ed4d`; the task's base
  `cf11541f039649db3a76aa5aaa2d7cce2cc48f34`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`. Read also, whole, the step of the cycle that holds
  this stage: step 11 of `.runs/the-way-base/task-cycle/skill/SKILL.md` (lines 349–364), and the
  element skills it names where you write or correct an entry, each from `.runs/the-way-base/`.
  The task requires every agent of this cycle to read the methods of its stage from that copy at the
  base commit (its To do 7), because this change rebuilds them.
- The foundation, the files and the tests you compare and correct are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/return-report.md`.

## What you compare

- The entries the change writes or changes (commit `40f0fd3`): WAY-125, WAY-127, WAY-256.
- The entries the task names under *Decisions in play*: WAY-125, WAY-256, WAY-127, WAY-257, WAY-35,
  WAY-148, WAY-150; and those the foundation step's search touched: WAY-258, WAY-128, WAY-129, the
  invariant `skill-entry-points` (`.runs/task-cycles/task-cycle-skills-shape/reports/foundation-report.md`).
- The part map's entries of the touched parts: `task-cycle`, `instruction-files`,
  `agent-instructions`, `decisions` (`foundations/part_map.md`).
- Against the code at the head: `task-cycle/**` (the five rebuilt skills and the files beside them),
  `instruction-files/kind_skill.md`, `AGENTS.md`, `agent-instructions/skill_entry_points.py` and its
  test, the entry points.

Correct in the same change whatever no longer matches, as step 11 gives. Write a new entry only as
step 11 allows; the review findings are no foundation entries.

## What you read

- The frozen task, whole: `.runs/task-cycles/task-cycle-skills-shape/task.md` (in Polish).
- The plan: `.runs/task-cycles/task-cycle-skills-shape/plan.md`.
- The review of the whole change, `PASS 7369993`, 0 blocking, 5 Minor, 4 out of scope:
  `.runs/task-cycles/task-cycle-skills-shape/reports/review-report.md`. A Minor finding is not
  fixed as a finding; but where your own comparison finds the code no longer matching an entry, you
  correct it as the return step, whether or not a finding also names it.

## Boundaries the task sets

- No Python changes beyond the generator's sentence and its test's assertion (acceptance criterion
  1). `installation/install.py:136` ("Read the files it references inside `.the-way`") is outside
  that: if you find it no longer matching an entry, report it with your reading — no edit.
- The rebuild changes where text stands, not what it says: "remove" and "reword" that change a
  rule's content are proposals in your report, with no edit (task, *Questions to settle* 5).
- Process prose of the five skills is not to be re-judged here; the return step compares entries
  with the code.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec; planned route; guidelines none.

## Your boundary

Commit any correction on the task branch, keep the worktree clean, and return. Run
`python -B elements/common/foundation_check.py`, `python -B agent-instructions/skill_entry_points.py`
and the focused `python -B gate/run_tests.py <directory>` for each directory your corrections touch,
and `git diff --check`; report each with its command and exit code. Do not run `gate/run_tests.py`
as a whole; that run is the orchestrator's. Your report fills, for the record, *Foundation compared
with code* (each entry compared: what no longer matched and its correction, or none), and the
entries written or changed by kind. Return your status, your commits (or none), a one-line check
result naming what failed or did not run, and your report's path.
