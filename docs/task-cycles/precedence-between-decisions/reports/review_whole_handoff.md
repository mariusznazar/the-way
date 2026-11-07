# Handoff — review of the whole change

Stage: the review of the whole change of one task, made by an agent that did not make it.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator that
dispatches you. Ask no human. A question goes to the orchestrator in your report with the status
`questions`. You are read-only: change no file of the repository and make no commit. You alone grade
and scope your findings.

## Where you work

- Worktree and process root: `the worktree root`
  (the toplevel `git rev-parse --show-toplevel` prints there). Work from its root; read nothing in
  another checkout or worktree.
- This is the-way itself, not a product; there is no `.the-way` submodule.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it, as the reviewer of **the whole change**; read
`task-cycle/review/whole_change.md` when that skill sends you to it, and a file either names only
when the step that names it comes. You select your own foundation and guidelines by the parts the
change touches (WAY-150, WAY-213).

## What is reviewed

- Range: base `294af7fde45323ac1851c014a03071a97fc38d96`, head
  `9b44856c6b8bda6ea17f22808e3332694b026601`. Confirm that `git rev-parse HEAD` prints that head.
  Compute the diff yourself with `git diff 294af7f..9b44856` and `git log 294af7f..9b44856`.
- Frozen task, read whole: `docs/task-cycles/precedence-between-decisions/task.md`. There is no
  spec and no plan: the cycle judged that the task leaves no open design choice and that one author
  can hold the change.
- The author's report, a set of claims to verify, not evidence:
  `docs/task-cycles/precedence-between-decisions/reports/author_report.md`. It lists two changed
  foundation entries (WAY-25 and WAY-134) as `the cycle's`, its choices, and what it did not run.
- The change has no slices, no earlier review and no earlier fix. No Minor or out-of-scope finding
  comes to you from another review.

## Answers of the cycle's start (step 4)

- Trust boundary: no. Irreversible operation: no. The change touches the parts `decisions`,
  `task-cycle` and `agent-instructions`, in Markdown only, and writes no code.
- The task moves no process pin. The orchestrator ran the whole gate on the base `294af7f`: exit 0,
  804 tests in 9 directories, no check fails on the base.
- Reconciliation done by the orchestrator: the task's line numbers hold at `294af7f` except the item
  *Foundation entries the human did not see at the task document* of
  `task-cycle/skill/request_template.md`, now at lines 190-196 (the task gives 174-180).

## What the orchestrator asks you to bear in mind

- The task says its numbered *To do* and its five *Questions to settle* with their answers, sources
  and "not chosen" ways are what the human settled. Check the change against each, and check source
  fidelity: that no wording of the foundation says more or less than what the human settled.
- The task's own text on the author's choices is in the author's report under **Choices**; judge each
  as you would any addition the task did not ask for.
- The task's *Context* names entries that cite WAY-25 (WAY-32, WAY-172, WAY-268, WAY-293) and asks
  that the search of the whole foundation (WAY-33) check them; the orchestrator's own search found
  also `foundations/decisions.md:684` (WAY-26) and `elements/decisions/template.md:88`, `:198`.

## The gate

Do not run the whole gate `python -B gate/run_tests.py`; its run is the orchestrator's (WAY-160).
Run the focused checks you need, each reported with its command and exit code.

## Report

Write your full report to
`docs/task-cycles/precedence-between-decisions/reports/review_whole_report.md`, as `review-change`
gives it, with the report's first line `PASS <sha>` or `FAIL <sha>` (or `questions`), the changed
files with their added and removed line counts, the coverage of every item of the task, your reaches,
and **Searches not found or unclear** (`none` is an answer; a missing section is not). Return to the
orchestrator the first line of the report, the checks you ran with their exit codes, and the report's
path.
