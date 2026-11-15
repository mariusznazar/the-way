# Handoff — reviewer of slice 2, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 2. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `879a14c20a4f49015bf310021f51294f78e3c1ec` to head `bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b`** (`git diff 879a14c20a4f49015bf310021f51294f78e3c1ec..bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b` and `git log 879a14c20a4f49015bf310021f51294f78e3c1ec..bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 2 alone; the earlier slice and the foundation entries were reviewed (review-1). The entries as they stand are your reference for WAY-344.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-2-report.md`; its first line is `PASS bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b` or `FAIL bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-2/` for working copies only.
- Directory for your working copies: `.runs/review-2/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 2 — The reading of a Claude Code transcript by the stage script is under WAY-344

- **Goal:** `task-cycle/cycle_stages.py` reads a Claude Code transcript under WAY-344, the whole reading of that file and no other: a needed field that is absent (a `null` is absent), or a count that is no non-negative whole number, ends the script with exit code 2 and a message that names the transcript, the line and the field; the exit-code paragraph of the module description says exit 2 for a missing field and exit 1 for the rest. The fields are the closed list of the spec's D4, which governs where it differs from `task-cycle/cycle_measures.py`: *Needed* — of every `user` or `assistant` line that has a `timestamp`, `message` and `message.content`; of every `assistant` line whose model is not `<synthetic>`, `message.usage` with `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` and `output_tokens`; a `timestamp` that is no time ends the script with exit 2 naming the field, as an uncaught error today. *Stay as they are* — a line with no `timestamp` skipped before its type is looked at, `type`, `isMeta`, `message.model` absent or `null` (the model `unknown` and the existing warning), `message.id` (the line's `uuid` stands for it), `message.stop_reason` absent or `null`, and the lenient reading of content blocks (a `tool_use` with no `id`, a `name`, a `tool_result` with no `tool_use_id`, a `text` that is no string). The fields `message.usage.cache_creation` and its two lifetimes are not read here: they join the list in Slice 3. The reading of a Codex rollout and of `agent-<id>.meta.json` does not change. One test gives a transcript without a needed field and asserts exit code 2 and the field named; the tests that pin the list that stays — a response that names no model (the warning, the model `unknown`), early lines of a response with `stop_reason` `null`, a line with no `timestamp`, a response with a `uuid` and no `id` — read as today and end with exit 0; the existing fixtures of the Claude Code tests that lack a needed field gain it. The sentence of step 12 of `task-cycle/skill/SKILL.md` (about line 571: where `task-cycle/cycle_measures.py` or `task-cycle/gate_times.py` ends with exit code 2 and an `Error:` line, record the command, the exit code and the line…) names `task-cycle/cycle_stages.py` too; the file is never written by hand.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py` · `task-cycle/skill/SKILL.md`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/spec.md:57-61` Constraints, WAY-344 for each reading · `.runs/task-cycles/scripts-after-foundation-review/spec.md:265-327` D4, WAY-344 for the transcript, the test, the orchestrator step · `.runs/task-cycles/scripts-after-foundation-review/task.md:134-134` Decisions in play, WAY-344 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/decisions.md:2545-2569` WAY-38 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `task-cycle/cycle_measures.py:1-110` the model for the form of the check, as its module description gives it
- **Model:** same — a whole reading with a closed list of fields, what stays lenient pinned, and the fixtures of a large test file change together
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`
- **Checks:** start from the new test (a transcript without a needed field, exit 2 and the field named) and the pin tests, the first red on the base; `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`; `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` (the script this one is modelled on is untouched)
- **Depends on:** Slice 1


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-2-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:2741-2901` WAY-344
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
