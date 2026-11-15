# Handoff: reviewer of the whole change, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer it
gives is the human's approval. You never ask the human. The cycle has one human contact, the request.

## What you review

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`. Read-only: change no tracked file, make no commit.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole, as **the review of the whole change**; read
  `task-cycle/review/whole_change.md` too and follow it. You select your own foundation and guidelines by "Reading the
  foundation" in `elements/common/way_of_working.md` (as the change rewrote it — you are the first to use it: write the
  index of your selection of decisions with `elements/common/decision_index.py`, which the change adds, and report how
  many decisions of the index you read whole). The-way has no guideline files of a product.
- Range: base `21ecb627f885de438e2209d7ff5c137b1e1b9d83` to head `55f1a24ddcece1ba8c48a5e27595a34072939359`
  (`git diff 21ecb62..55f1a24`, `git log 21ecb62..55f1a24`; confirm `git rev-parse HEAD`).
- The frozen task (Polish): `.runs/task-cycles/decision-log-reading-index/task.md`; read it whole. The plan, whole:
  `.runs/task-cycles/decision-log-reading-index/plan.md` (five slices, F1–F10 as its foundation entries; no spec).
- Answers of step 4: trust boundary **yes** (`task-cycle/cycle_measures.py`; check crafted input at it); irreversible
  operation no. Check also that the change touches nothing it should not and that the task's *Out of scope* holds.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/review-whole-report.md`, a file at exactly that path
  (first line `PASS <sha>` or `FAIL <sha>`, the full head sha), with graded findings (name for each blocking finding the slice
  it comes from, or that it comes from none), the checks you ran with command and exit code, the count of decisions read whole,
  your **Unread material**, **Searches not found or unclear** and reaches. You alone grade and scope.

## The slices of the range, and who reviewed what

| Part of the range | Range | Agent | Review of its own |
|---|---|---|---|
| Foundation entries F1–F9, F10, WAY-21 wording | `21ecb62..0023a28` (`dae85e1`, `104e126`, `0023a28`) | foundation agent (opus) — `reports/foundation-entries-report.md` | none: you judge it |
| Slice 1: index script | `0023a28..30c5b1b` | executor (haiku) — `reports/executor-1-report.md` | none: you judge it |
| Slice 2: comparison script, check on a sectioned log | `30c5b1b..cea78e5` | executor (haiku) — `reports/executor-2-report.md` | none: you judge it |
| Slice 3: reading rule, template, two `project-level/lead/` files | `cea78e5..3cec41a` | executor (sonnet) — `reports/executor-3-report.md` | none: you judge it |
| Fix to WAY-150 and WAY-18 (a contradiction found by slice 3's executor) | `3cec41a..dbdfdad` | foundation agent resumed — "Fix 1" in its report | none: you judge it |
| Slice 4: reviewer's instruction, report, request template | `dbdfdad..4ef3fcb` | executor (haiku) — `reports/executor-4-report.md` (saved by the orchestrator from the agent's returned text; the agent would not write the file) | none: you judge it |
| Slice 5: `cycle_measures.py` and tests | `4ef3fcb..e1ab383` | executor (sonnet) — `reports/executor-5-report.md` | yes: `reports/review-5-report.md` `FAIL e1ab383` (I1), fix `e1ab383..55f1a24` (`reports/executor-5-fix-report.md`), `reports/review-5-fix-report.md` `PASS 55f1a24` |

All reports are in `.runs/task-cycles/decision-log-reading-index/`. The reports of the executors of slices 1–4 and the
foundation agent are given as claims to verify, with any mismatch the orchestrator's mechanical check passed on:

- Slice 1: a decision with no binding sentence prints nothing and is no error; the executor did not compare WAY-150 and
  WAY-18 with the plan's F-entries.
- Slice 2: only the first of 13 comparison tests was seen failing before the script; entries of a heading form other than
  `### PREFIX-NN — ` are skipped; CRLF against LF differs by design.
- Slice 3: two additions beyond the slice's text (the index as a reader in the template's table of fields; a clause in
  "Withdrawn numbers" about a sectioned log).
- Slice 4: one hit of "by title" remains in a test fixture, `task-cycle/test_remarks_check.py:204` (outside the slice's files);
  the item 14 example "40 of 151" is copied from WAY-287's rationale.
- Slice 5: `task-cycle/skill/SKILL.md` step 12 still describes `cycle_measures.py` as counting "the context and the prompt cache"
  without the log and the index (that file is slice 4's, not slice 5's).

## Minor and out-of-scope findings of the slice reviews (the only slice review: slice 5)

- M1 (review-5): a line so large that `json.loads` raises `MemoryError` gives a traceback and exit 1, not exit 2.
- M2 (review-5): a subtest at `task-cycle/test_cycle_measures.py` (`None`) skips at once and asserts nothing.
- N1 (review-5-fix): the `type` of a block or payload is not checked; the docstring says so.
- N2 (review-5-fix): one docstring line of 124 characters, `task-cycle/cycle_measures.py:83`.
Grade and scope them yourself where they bear on the whole change; your report's Minor findings within the task are fixed by the cycle.

## The foundation entries the cycle wrote, and their origin

The task's rows 1–7 of *Settlements to record* went to WAY-150 (rows 1, 2, 3, 5, 6), WAY-18 (row 4) and WAY-339 (row 7,
where WAY-347's rule stands since it was withdrawn; WAY-326 is withdrawn as well and stands in `task-cycle/skill/SKILL.md`).
Beyond rows: WAY-287 (consequence of *To do* 4), WAY-21's rationale and *Rejected* (the task's *Decisions in play*), and two
wording additions the orchestrator asked for on the message of a peer session (the price of the reading by title in WAY-150's
rationale, as the cost of a fix round, and the share of the log that selection by *Scope* returns in WAY-21's rationale, counted
by the agent); the foundation agent marked them `the cycle's`. The plan's *Choices* and the orchestrator's questions Q1–Q8 are in the
plan and the record, which you do not read. Check the entries against the task's rows and *Acceptance criteria* (the request will name the
variant each of WAY-150, WAY-18 and WAY-21 takes in), and check that no file still says the reading by title or "no topical
sections".

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/review-whole/`.

Do not run the product's full gate: the orchestrator runs it after the review and the return step. Focused checks by directory
(`python -B gate/run_tests.py <directory>`) are yours to run.
