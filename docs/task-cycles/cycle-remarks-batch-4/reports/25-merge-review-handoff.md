# Handoff — review of the merge with the target branch, cycle `cycle-remarks-batch-4`

You review, as an agent that did not make any of this change, the merge of the remote target branch
into the task branch (WAY-306). Read-only: change no file, make no commit. The orchestrator acts on the
user's delegation; nothing here is the human's approval.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`.
- Method: `task-cycle/review/SKILL.md`, variant **the reconciliation with the target branch**: it
  reviews the merge commit as the method gives. Read the method whole; read a file it names only when
  the step or variant that names it comes.
- The merge: commit `3c26a24` (confirm with `git rev-parse HEAD`); first parent `1b37abb` (the task
  branch as it was reviewed: its code tree is the one that passed `PASS 1c1e8c8` and the full gate,
  894 tests), second parent `5b20e75` (`origin/foundations`, which brought in the merged request #99).
  The base of the task branch was `e3825a8`. Compute the three sides yourself:
  `git diff 1b37abb..3c26a24` (what the merge brought into the task branch),
  `git diff 5b20e75..3c26a24` (what the task branch adds to the target branch), and
  `git log e3825a8..5b20e75`.
- What the question is: **do the two sides still hold together?** Two files were conflicting and were
  resolved by hand: `foundations/decisions.md` (the decision WAY-287, three places) and
  `task-cycle/skill/request_template.md` (the section for the human's decisions). The target branch
  brought in a split of that section into three groups (*Needed from you*, *Fix or let through*,
  *You accept by merging*), with numbered kinds of items; this task adds a kind 16, the descriptive
  `TODO` in *Rests on*, *Derives from* and *Based on*, to *Fix or let through*. Judge the resolution
  (placement of kind 16, the numbering, the wording of WAY-287's binding sentence, *Verification* and
  *Rationale*, its *Rejected*), and every place outside the conflict where the two sides touch: the
  cycle skill and `correction.md`, `task-cycle/request_check.py` and its tests, WAY-289, WAY-290,
  WAY-317, WAY-327, `elements/common/rules.md`, and whether the target branch's new rule about what an
  item of the first two groups carries (four parts, WAY-327) is met by the way kind 16 is worded.
- Foundation entries the merge brought in that bear on the parts this change touches (`decisions`,
  `task-cycle`, `elements-common`), whole: WAY-287 (as the target branch has it and as the merge leaves
  it), WAY-289, WAY-290, WAY-317, WAY-327; with them WAY-71 and WAY-160 as the task branch has them.
  Select the rest as the method gives and name each reach.
- Checks you may run: `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py
  elements/common`, `python -B elements/common/foundation_check.py .`. Do **not** run the other gate
  directories or the full gate: the orchestrator runs the full gate on the merge right after your
  review, and a second run beside it disturbs both.

## Report

Write it to `docs/task-cycles/cycle-remarks-batch-4/reports/26-merge-review-report.md`
(first line `PASS <sha>` or `FAIL <sha>`; findings with grade, `file:line` and scope; the checks you ran
with command and exit code; **Unread material**; **Searches not found or unclear**). Return the first
line, the findings by grade and the report path.
