# Handoff 03 — review of the whole change

## Delegation

You are a reviewer dispatched by the orchestrator of `implement-task`. You did not make this
change. Ask no human; send a question to the orchestrator in your report (first line `questions`).
Read-only: change no tracked file, make no commit.

## Where you work

- Worktree, from its root: `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-2`
- Range to review: base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a`, head `3023f604d5517ca157b3cb6bb9135a360d7e29f3`
  (two commits: `b2a52f6` foundation entries, `3023f60` task-cycle instructions). Confirm that
  `git rev-parse HEAD` is the head; on a mismatch ask which range to review.

## Method and variant

- Method: `task-cycle/review/SKILL.md` in the worktree — read it whole. Your variant: **the whole
  change**; read `task-cycle/review/whole_change.md` as that skill gives.
- You select your own foundation and guidelines by "Reading the foundation" in
  `elements/common/way_of_working.md` (parts touched: `decisions`, `task-cycle`; the-way has no
  `guidelines/` directory).

## What you are given

- Frozen task, whole: `C:\Storage\repos\the-way\.runs\task-cycles\cycle-remarks-batch-2\task.md`.
  Cover every *To do* item (1–4), rows 1–3 of *Settlements to record*, and source fidelity: the
  sentences the task quotes must stand word for word where it places them; the entries must carry
  the task's meaning (WAY-134), and the changes to WAY-05 and WAY-148 were approved with the task
  document (WAY-30).
- No spec and no plan: one author without a plan; no slices, so no slice review and no Minor or
  out-of-scope findings from slice reviews.
- Answers at start: trust boundary — no; irreversible operation — no.
- The author's report, a set of claims to verify, not evidence:
  `C:\Storage\repos\the-way\.runs\task-cycles\cycle-remarks-batch-2\reports\02-author-report.md`.
  It marks WAY-293 as a new decision (row 1), WAY-05 and WAY-148 as edited in place (rows 2 and 3).
  Its choices to judge: the new WAY-05 example placed into the existing `complies:`/`violates:`
  lines instead of a second pair; WAY-293 scope `decisions, task-cycle`; no `derives from WAY-36`;
  a third binding sentence in WAY-293; and the places it names under **Searches not found or
  unclear**.
- The form of the foundation is checked by `elements/common/foundation_check.py`; the product's full
  gate is the orchestrator's and a full run is under way elsewhere — do not run
  `python -B gate/run_tests.py` without a directory argument. Focused runs of one directory are
  yours to make where you need them.

## Your report

Write it to `C:\Storage\repos\the-way\.runs\task-cycles\cycle-remarks-batch-2\reports\04-review-report.md`
as the method gives it (first line `PASS <sha>` or `FAIL <sha>`, graded findings, reaches beyond this
handoff, the checks you ran with command and exit code, the section **Searches not found or
unclear**, `none` being an answer). Return to the orchestrator only the first line, the counts of
blocking, Minor and out-of-scope findings, a one-line check result naming what failed or did not
run, and the report path.
