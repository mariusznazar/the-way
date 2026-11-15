# Handoff — reviewer of slice 6, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 6. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `61894c282d8e92625ba1730ee967975d9d32c4d9` to head `4c03086723435b286e1a94c92c5b12e3028be12d`** (`git diff 61894c282d8e92625ba1730ee967975d9d32c4d9..4c03086723435b286e1a94c92c5b12e3028be12d` and `git log 61894c282d8e92625ba1730ee967975d9d32c4d9..4c03086723435b286e1a94c92c5b12e3028be12d`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 6 alone. Information from the orchestrator's mechanical check (not a finding): the full test_audit_count.py has the one expected red test, Cost.test_the_stage_report_cycle_stages_writes_gives_the_share (until Slice 7; choice Q3); the executor did not run the whole file after its last docstring-only edit: run it yourself and judge whether any other test fails. The change of a series of the cost is told to start with cycle_stages.py (spec D5, plan Slice 6).
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-6-report.md`; its first line is `PASS 4c03086723435b286e1a94c92c5b12e3028be12d` or `FAIL 4c03086723435b286e1a94c92c5b12e3028be12d` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-6/` for working copies only.
- Directory for your working copies: `.runs/review-6/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 6 — Two kinds of series: the cost and the count of remarks

- **Goal:** in `process-audit/audit_count.py`, the grouping of the versions of the process into series gives two kinds, and each comparison stays inside its own kind. A series of the cost ends at a change of the price list or of the script that measures the cost, `task-cycle/cycle_stages.py` (and of no other script: the spec's D5), between two versions, and nowhere else; the median cost and the answer Q3 are compared inside it. A series of the count of remarks ends wherever a series of the cost ends, and also at a date of *Added* or *Withdrawn* of the register's list of classes, at a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, that is, of the files of the-way under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and of `task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its instruction (the list of the module description, the paragraph "the tree of the-way under `task-cycle/change`, …"); the answers Q1 and Q2 are compared inside it. `git diff --quiet` as now, a failure counting as changed. The section *Process versions* and its description say, per series, why it begins where it does, and no cell sets a number of one kind of series beside a number of the other; the description of the module, the sentences that call the test "deliberately conservative", the text of the section and the reasons of a series are rewritten to this rule. The module description and the result keep `Q1`, `Q2` and `Q3` and the section *Measure versions* as they are. The new tests start from: a change of `task-cycle/agent-types/the-way-stage.md` starts a series of the count and none of the cost; a change of a file under `task-cycle/review` starts a series of the count and none of the cost; a change of `task-cycle/cycle_stages.py` starts both; a new price list starts both.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:32-33` To do 5 and 6 · `.runs/task-cycles/scripts-after-foundation-review/task.md:59-64` Questions to settle 2 · `.runs/task-cycles/scripts-after-foundation-review/task.md:133-133` Decisions in play, WAY-339 · `.runs/task-cycles/scripts-after-foundation-review/task.md:145-145` Settlements to record, row 3 · `.runs/task-cycles/scripts-after-foundation-review/spec.md:341-346` D5, the split of the series · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/invariants.md:398-407` audit-series-script-paths · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** same — the grouping, its description and its tests change together, and the rule must hold for every comparison of the section
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the tests of class `ProcessVersions` and of class `PriceBoundary` named above, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k ProcessVersions -k PriceBoundary -k MeasureVersions`; then `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` (the invariant `audit-series-script-paths` holds)
- **Depends on:** Slice 5


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-6-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/invariants.md:398-407` audit-series-script-paths
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:124-135` process-audit

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
