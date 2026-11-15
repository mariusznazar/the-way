# Handoff — reviewer of slice 1 and the foundation entries of the plan (the range includes them), task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 1 and the foundation entries of the plan (the range includes them). Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `7f5c5a56f67d9ff40554240594ca0bde59773cb3` to head `879a14c20a4f49015bf310021f51294f78e3c1ec`** (`git diff 7f5c5a56f67d9ff40554240594ca0bde59773cb3..879a14c20a4f49015bf310021f51294f78e3c1ec` and `git log 7f5c5a56f67d9ff40554240594ca0bde59773cb3..879a14c20a4f49015bf310021f51294f78e3c1ec`, computed by you; confirm that `git rev-parse HEAD` is the head). The range holds the plan's foundation entries (commits da9d816 and bfb774c: WAY-339, WAY-344, the glossary term Markdown file and corrections of five uses of .md alone) and the slice (879a14c). Judge the entries against the task's rows 1-4 and 8 and the spec's D3 (spec.md lines 180-248), and the slice as the slice.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-1-report.md`; its first line is `PASS 879a14c20a4f49015bf310021f51294f78e3c1ec` or `FAIL 879a14c20a4f49015bf310021f51294f78e3c1ec` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-1/` for working copies only.
- Directory for your working copies: `.runs/review-1/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 1 — The table of stages on Windows when a Codex session has no turn of its own

- **Goal:** `task-cycle/cycle_stages.py` gives the table of stages, never a stack trace, on Windows when the orchestrator's Codex session holds no turn of its own. The lower bound of the search for the subagents' rollouts, set in `read_codex_session` where the orchestrator has no turn, no longer comes from a naive `datetime.fromtimestamp(0)`, which Windows does not read in every time zone; where the orchestrator has no turn, the search has no lower bound, as `codex_subagents` of `task-cycle/cycle_measures.py` does with `None`, and `codex_subagent_paths` takes that. Nothing else of how the script reads a transcript changes (Slice 2 reworks that reading). The failing test is written first and fails on the base on any machine: it does not depend on the time zone of the machine it runs on, for example by making the naive `fromtimestamp(0)` of the module raise `OSError` as Windows does, and the report says how.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:31-31` To do 4 · `foundations/decisions.md:2545-2569` WAY-38 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `task-cycle/cycle_measures.py:506-541` codex_subagents
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`
- **Checks:** start from the new test in `task-cycle/test_cycle_stages.py` (class `CodexTest`: an orchestrator rollout with no turn started, read by `read_codex_session`), red on the base; `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`
- **Depends on:** none


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-1-report.md`, `.runs/task-cycles/scripts-after-foundation-review/reports/foundation-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:2545-2570` WAY-38
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
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
