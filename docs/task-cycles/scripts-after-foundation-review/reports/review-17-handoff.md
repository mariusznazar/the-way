# Handoff — reviewer of slice 17, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 17. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `c01fe56763983c7a366ecda82067c06e4dd50582` to head `e8bef720a34924cb4b32bd0f136f51c006e2b504`** (`git diff c01fe56763983c7a366ecda82067c06e4dd50582..e8bef720a34924cb4b32bd0f136f51c006e2b504` and `git log c01fe56763983c7a366ecda82067c06e4dd50582..e8bef720a34924cb4b32bd0f136f51c006e2b504`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 17 alone. The executor ran the script on the user's real session records (read only); judge the code change and its test, and the report's counts. You may re-run the script on a real Codex cycle yourself in your own directory, read only, writing only under .runs/review-17/ and putting no path of the disk, user name or content of a session into your report.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-17-report.md`; its first line is `PASS e8bef720a34924cb4b32bd0f136f51c006e2b504` or `FAIL e8bef720a34924cb4b32bd0f136f51c006e2b504` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-17/` for working copies only.
- Directory for your working copies: `.runs/review-17/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 17 — The measures of a real Codex cycle, run and corrected

- **Goal:** `task-cycle/cycle_measures.py` is run on the session records of a real cycle led in Codex that lie under the user's `~/.codex/sessions` (the 78 records there name the-way and `implement-task`; pick one whole cycle, with its subagents, and the session of a nested Claude Code helper where the cycle has one, read from the Claude Code home), with `--output` naming a file in the executor's own directory under `.runs/` of this worktree; the run reads and writes nothing else outside `.runs/`. The executor reports **counts and facts only**: the number of agents of each tool, whether each cycle-level measure of the file has a value or `unknown` and why, whether the cache figures of the Codex agents are `unknown` as the script's description says, and whether the nested helper's measures are full; **no absolute path of the user's disk, no user name and no content of a session**. A measure that comes out wrong or empty where the script should give it is a defect of this cycle: the executor fixes it in `task-cycle/cycle_measures.py` with the test first in `task-cycle/test_cycle_measures.py` (a fixture of the form the real record had, made by hand and with no real content) and reports what it fixed; where nothing is wrong, it changes nothing. The spec leaves this script as it is for the route of the cache writes, so a change here is a change for this item only. Where the user's Codex home, Claude Code home or the records cannot be opened, the executor reports it and does not guess. The output of the run and the executor's directory are removed before it returns (only the counts stay in its report).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:38-38` To do 11 · `.runs/task-cycles/scripts-after-foundation-review/task.md:80-84` Questions to settle 6 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/decisions.md:7007-7072` WAY-308 · `foundations/part_map.md:101-111` task-cycle
- **Model:** same — it judges real data and may change a trust-boundary script on what it sees
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`
- **Checks:** the run above, with its counts in the report; where a defect is fixed, the new test red on the base and `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`
- **Depends on:** none


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-17-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/decisions.md:7055-7121` WAY-308
- `foundations/part_map.md:101-112` task-cycle

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
