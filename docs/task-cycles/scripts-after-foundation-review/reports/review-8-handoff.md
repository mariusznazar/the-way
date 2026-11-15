# Handoff — reviewer of slice 8, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 8. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `f1d632396d25f47cddf7efee7d4659a2e7e47e7c` to head `6e3ab99a5d540d97fe1755e617a9c66893e960ee`** (`git diff f1d632396d25f47cddf7efee7d4659a2e7e47e7c..6e3ab99a5d540d97fe1755e617a9c66893e960ee` and `git log f1d632396d25f47cddf7efee7d4659a2e7e47e7c..6e3ab99a5d540d97fe1755e617a9c66893e960ee`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 8 alone. Information from the orchestrator (not a finding): the executor ran the whole test_audit_count.py before six test methods were renamed and one comment re-wrapped, so run the whole file yourself on the head. The executor's own reading, for you to judge against WAY-339 and WAY-344 as the foundation entries now say it: for a cycle that changed a tool, the file that tool wrote is not read for that cycle, so a missing field in it ends no run with exit 1; its values are unknown with the reason; one test in MechanismMeasures pins this.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-8-report.md`; its first line is `PASS 6e3ab99a5d540d97fe1755e617a9c66893e960ee` or `FAIL 6e3ab99a5d540d97fe1755e617a9c66893e960ee` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-8/` for working copies only.
- Directory for your working copies: `.runs/review-8/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 8 — A cycle that changed the tool that measures gives that tool's measures as unknown

- **Goal:** in `process-audit/audit_count.py`, a cycle of the-way whose own change changes the tool that wrote a file of its copy gives the measures that tool wrote as `unknown`, with the reason that the cycle changed the tool that wrote them, and the other measures of the cycle as it does today, under the version it ran on (WAY-339, row 4). The tools and what each wrote: `task-cycle/cycle_stages.py` — the times, the cost and the share of fix rounds from `stages.md`; `task-cycle/cycle_measures.py` — `mechanism_measures.md`; `task-cycle/gate_times.py` or `gate/run_tests.py` — `gate_times.md`. The tools are taken from what Slice 6 settled about series (the same paths, not a second list that can drift). The cycle changed the tool where the files of the tool differ between the version it ran on and the commit of its last copy of the record in the-way's own history (`git diff --quiet`, a failure counting as changed, as `differs` does); the executor names in its report how it finds that commit and why a cycle of another repository is left as it is (item 8 holds for cycles of `the-way` only), and a copy of an earlier cycle is not put in doubt by it. The comment at `MEASURES_FILE` ("A copy holding neither is an earlier form.") says what the module description says ("A copy that holds neither is of an earlier cycle or of one whose script failed"), in the same words (To do 9). The tests: for each of the three groups of tools, a cycle whose copy changes it gives that group's values `unknown` with the reason and the other values as before, and a cycle that changes none gives all as before.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:35-36` To do 8 and 9 · `.runs/task-cycles/scripts-after-foundation-review/task.md:70-74` Questions to settle 4 · `.runs/task-cycles/scripts-after-foundation-review/task.md:133-133` Decisions in play, WAY-339 · `.runs/task-cycles/scripts-after-foundation-review/task.md:146-146` Settlements to record, row 4 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:7471-7506` WAY-350 · `foundations/invariants.md:398-407` audit-series-script-paths · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `foundations/part_map.md:124-134` process-audit
- **Model:** same — a new reading of git history that must not put the cycles of earlier forms in doubt
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the new tests of classes `MechanismMeasures`, `GateRunsMeasures` and `Times` (one per group of tools) and of class `ProcessVersions`, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MechanismMeasures -k GateRunsMeasures -k Times -k ProcessVersions -k MeasureVersions`; then the whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`
- **Depends on:** Slice 7 · Slice 6


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-8-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:7586-7622` WAY-350
- `foundations/invariants.md:398-407` audit-series-script-paths
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:101-112` task-cycle
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
