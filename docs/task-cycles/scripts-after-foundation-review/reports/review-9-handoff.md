# Handoff — reviewer of slice 9, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 9. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `6e3ab99a5d540d97fe1755e617a9c66893e960ee` to head `b6f800c19d85ab449527b49b1e2f255f3b25d85f`** (`git diff 6e3ab99a5d540d97fe1755e617a9c66893e960ee..b6f800c19d85ab449527b49b1e2f255f3b25d85f` and `git log 6e3ab99a5d540d97fe1755e617a9c66893e960ee..b6f800c19d85ab449527b49b1e2f255f3b25d85f`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 9 alone.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-9-report.md`; its first line is `PASS b6f800c19d85ab449527b49b1e2f255f3b25d85f` or `FAIL b6f800c19d85ab449527b49b1e2f255f3b25d85f` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-9/` for working copies only.
- Directory for your working copies: `.runs/review-9/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 9 — *Unknown values* gives one line for each field and reason

- **Goal:** the section *Unknown values* of the result in `process-audit/audit_count.py` gives the values the count did not establish as one line for each pair of a field and a reason, with the number of values of that pair and its first few examples; the full list stays in the register, and the limit `MAX_LISTED` and the line "more values the register leaves unknown are not listed here" are gone or have the new meaning the description of the result gives. The description of the module (the sentences about *Unknown values* and the register's unknown values) and the headings of the result say what the lines are. The result stays deterministic: the same input, the same bytes, and a value that is crafted text reaches the result only as the module already lets it (cut, one line, no bar). The test starts from the register template, which gave about 830 lines, now one line per pair, and from the example lines of one pair.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:37-37` To do 10 · `.runs/task-cycles/scripts-after-foundation-review/task.md:75-79` Questions to settle 5 · `.runs/task-cycles/scripts-after-foundation-review/task.md:114-114` Context, the limit · `.runs/task-cycles/scripts-after-foundation-review/task.md:148-148` Settlements to record, row 6 · `foundations/decisions.md:7309-7341` WAY-330 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the new tests of classes `Run` and `RegisterCount` (the template register gives a bounded number of lines, a line for each pair with its count and examples), red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Run -k RegisterCount -k CraftedInput`; then the whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`
- **Depends on:** Slice 8


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-9-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7357-7390` WAY-330
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
