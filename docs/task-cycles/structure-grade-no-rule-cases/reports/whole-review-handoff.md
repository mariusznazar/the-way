# Handoff — review of the whole change

You review the whole change of a task cycle of the-way as an agent that did not make it. The person
who requested the cycle has delegated intermediate choices to the orchestrator; no answer you get is
that person's approval. You are read-only: change no file of the worktree.

- Worktree: `the root of the task's worktree`, branch
  `task/structure-grade-no-rule-cases`. The repository is the-way itself: no pin, no `.the-way`.
- Method of your stage: `task-cycle/review/SKILL.md` (`review-change`). Read it whole, then the
  files it names as the step that names them comes (`whole_change.md` for this review).
- What is reviewed: the whole change, range `1be90579bf3daa618dd87c06bd56042eabb642c1..5554f5d`
  (one commit, `5554f5d`; confirm `git rev-parse HEAD` is the head you were given and the range
  is computed by you).
- Frozen task, read it whole: `docs/task-cycles/structure-grade-no-rule-cases/task.md`. No spec, no
  plan: one author without a plan; no slices, so there are no slice reviews, and no Minor or
  out-of-scope findings of slice reviews to grade.
- The author's report (claims to verify, not evidence):
  `docs/task-cycles/structure-grade-no-rule-cases/reports/author-report.md`.
- Answers of step 4: trust boundary — no; irreversible operation — no; open design choice — none.
  The task carries no row of *Settlements to record* and no projected entry; the change edits the
  decision WAY-363 in place (WAY-07). The task moved no pin.
- Checks the base already fails: none (list taken from the final gate of the cycle of the merged
  branch: exit 0, 1267 tests, every directory passed).
- The-way has no coding guidelines (WAY-328), so none are read. You select your own foundation
  entries by "Reading the foundation" in `elements/common/way_of_working.md`, and state how many
  decisions you read whole and how many by title only.
- Where the task's acceptance criterion is concerned, judge it by reading, per `whole_change.md`:
  the three cases must give the reviewer the same grade in section 3 of `SKILL.md`, in the binding
  sentence of WAY-363 and in the last bullet of "The structure of the code the change leaves" in
  `task-cycle/review/whole_change.md`. The author did not edit `whole_change.md`; judge whether that
  meets the criterion and the task's *To do*.
- For the structure of the code the change leaves, `whole_change.md` asks for the numbers of
  `python -B task-cycle/change_file_sizes.py <base> <head>`; the-way has no rule of size, so no
  test of the rule exists to run and the diff is your material.
- Run `python -B elements/common/foundation_check.py` in the worktree and report its command and
  exit code. Do not run the whole gate: the orchestrator runs it.

## Report

Write the full report to
`docs/task-cycles/structure-grade-no-rule-cases/reports/whole-review-report.md`;
its first line is `PASS <head sha>` or `FAIL <head sha>` and nothing else (or `questions`). Return
the first line, the changed files with their line counts, a one-line check result, and the report's
path. The report holds **Unread material** and **Searches not found or unclear** sections
(`none` where there is nothing), and lists each Minor finding with its place in the code, in its own
words, and says in them where a Minor finding lies outside the task.
