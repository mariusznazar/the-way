# Handoff — reviewer of slice 5, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 5. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `aaed860` to head `61894c282d8e92625ba1730ee967975d9d32c4d9`** (`git diff aaed860..61894c282d8e92625ba1730ee967975d9d32c4d9` and `git log aaed860..61894c282d8e92625ba1730ee967975d9d32c4d9`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 5 alone. Information from the orchestrator's mechanical check (not a finding): the full test_audit_count.py has one failing test, Cost.test_the_stage_report_cycle_stages_writes_gives_the_share, expected red until Slice 7 (the audit refuses the eleven-column header of the stage report; the plan and the orchestrator's choice Q3 name it). Judge whether any other test fails.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-5-report.md`; its first line is `PASS 61894c282d8e92625ba1730ee967975d9d32c4d9` or `FAIL 61894c282d8e92625ba1730ee967975d9d32c4d9` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-5/` for working copies only.
- Directory for your working copies: `.runs/review-5/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 5 — A register table without a level names the level; a missing `repository` entry under `the-way` is no missing field

- **Goal:** in `process-audit/audit_count.py`, a table *Weights* that lacks one of its four levels or a table *Costs of an occurrence* that lacks one of its five makes the count write its result as today, give the values that depend on the table as `unknown`, end with exit code 1 and an `Error:` line that **names the missing level** (and, where a level is written twice, the level written twice), no longer only the table (the two sentences "must name the four levels, each once" and "must name the five levels, each once"); the run is not ended with exit code 2 and nothing is written. The module description says so beside its exit codes, and the existing test `test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` is changed first, with a like test for *Weights*, each giving the table without one level and asserting the line that names it (WAY-344: the one test per reading). The missing entry `repository` under `the-way` is no missing field: `the_way_checkout` takes the checkout the script lies in, as it does today, the description of the module keeps the sentence, and a test pins it (a locations file with no entry `repository` under `the-way`, a pin of a commit of the checkout the script lies in, exit code 0, no `Error:`). WAY-344, as the foundation step wrote it, holds both exceptions; no other reading of a file changes.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:28-30` To do 1 to 3 · `.runs/task-cycles/scripts-after-foundation-review/task.md:51-58` Questions to settle 1 · `.runs/task-cycles/scripts-after-foundation-review/task.md:134-134` Decisions in play, WAY-344 · `.runs/task-cycles/scripts-after-foundation-review/task.md:143-144` Settlements to record, rows 1 and 2 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/decisions.md:7309-7341` WAY-330 · `foundations/glossary.md:187-191` cost of an occurrence · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the changed test in class `RegisterCount` (a level missing in *Costs of an occurrence*, the line names it) and its like for *Weights*, red on the base, and the test for the entry `repository` (class `Locations`); `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k RegisterCount -k Locations`; then `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`
- **Depends on:** none


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-5-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/decisions.md:7357-7390` WAY-330
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:124-135` process-audit
- `foundations/glossary.md:187-192` cost of an occurrence

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
