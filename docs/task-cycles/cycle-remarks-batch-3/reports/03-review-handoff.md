# Handoff 03 — review of the whole change

## Delegation

You are a reviewer dispatched by the orchestrator of `implement-task`. You did not make this
change. Ask no human; send a question to the orchestrator in your report (first line `questions`).
Read-only: change no tracked file, make no commit.

## Where you work

- Worktree, from its root (do not work from any other directory): `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3`
- Range to review: base `3177e1090f6000ed97fbbbab70ec7c7e622aa2c9`, head `7841f00` (confirm with `git rev-parse HEAD` the full SHA; three commits: `0b81978` To do 1 and the decision WAY-298 and the WAY-291 example, `f13c800` To do 2 and 3, `7841f00` To do 4). On a mismatch ask which range to review.

## Method and variant

- Method: `task-cycle/review/SKILL.md` in the worktree — read it whole. Your variant: **the whole change**; read `task-cycle/review/whole_change.md` as that skill gives.
- You select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` (parts touched: `task-cycle`, `elements-common`, and the file `foundations/decisions.md`; the-way has no `guidelines/` directory, and the task says it does not wait for them).

## What you are given

- Frozen task, whole: `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3\.runs\task-cycles\cycle-remarks-batch-3\task.md`. Cover every *To do* item (1–4), row 1 of *Settlements to record*, and source fidelity: the sentences the task quotes must stand word for word where it places them; the new decision must carry the row's meaning (WAY-134) and its *Rejected* the ways the task's *Not chosen* lists; the changes to the WAY-291 example and to `way_of_working.md` were approved with the task document (WAY-30).
- No spec and no plan: one author without a plan; no slices, so no slice review and no Minor or out-of-scope findings from slice reviews.
- Answers at start: trust boundary — no; irreversible operation — no. The change touches `task-cycle/request_check.py` and `task-cycle/remarks_check.py`, neither a trust boundary of the part map.
- The author's report, a set of claims to verify, not evidence: `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3\.runs\task-cycles\cycle-remarks-batch-3\reports\02-author-report.md`. It marks WAY-298 as the new decision (row 1). Its choices and concerns to judge on their merits, as you would any: the correction's restart condition ("where something came in"), the new first paragraph of `correction.md` against the retained "First merge, never rebase" sentence, what `SKILL.md:68` and step 12 now say against the new sentences, the *Rejected* of WAY-298 against the task's *Not chosen*, and the places it names under **Searches not found or unclear**.
- The form of the foundation is checked by `elements/common/foundation_check.py`; the product's full gate is the orchestrator's and a full run follows elsewhere — do not run `python -B gate/run_tests.py` without a directory argument. Focused runs of one directory are yours to make where you need them.

## Your report

Write it to `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3\.runs\task-cycles\cycle-remarks-batch-3\reports\04-review-report.md` as the method gives it (first line `PASS <sha>` or `FAIL <sha>`, graded findings, reaches beyond this handoff, the checks you ran with command and exit code, the section **Searches not found or unclear**, `none` being an answer). Return to the orchestrator only the first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result naming what failed or did not run, and the report path.
