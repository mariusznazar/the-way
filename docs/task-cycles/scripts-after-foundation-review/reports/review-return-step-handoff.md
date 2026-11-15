# Handoff — reviewer of the commits of the return step, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: the commits of the return step. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2` to head `8c6d6688cc9eff8a839ee4718bad435fb5583fcc`** (`git diff c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2..8c6d6688cc9eff8a839ee4718bad435fb5583fcc` and `git log c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2..8c6d6688cc9eff8a839ee4718bad435fb5583fcc`, computed by you; confirm that `git rev-parse HEAD` is the head). One commit made by the return step (`8c6d668`): it rewrites the *Verification* of WAY-339 and WAY-344 (removing from their pairs of examples what a test now holds and naming the tests by the clause `tests:` and lines `decision:` added to three test files), splits one sentence of WAY-344 into three, and names the dead-pointer test in the part map. Review it as section 2 of the method gives for the return step: against the task and the foundation entries the return step writes or corrects; the decisions keep their meaning (the entries are edited in place, WAY-07); each line `decision:` quotes a sentence that stands in the entry; the clause `tests:` names tests that exist and hold what the entry says they hold; no sentence of an entry is left that the code contradicts. Run `python -B elements/common/foundation_check.py` (exit 0 expected, no `listed:` line for a test the change left).
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of the return step's commits (section 2 of the method). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-return-step-report.md`; its first line is `PASS 8c6d6688cc9eff8a839ee4718bad435fb5583fcc` or `FAIL 8c6d6688cc9eff8a839ee4718bad435fb5583fcc` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-return/` for working copies only.
- Directory for your working copies: `.runs/review-return/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

The return step's own instructions: `task-cycle/skill/return_step.md`; its report is below.

Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/return-step-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md`, each whole: WAY-339, WAY-344, WAY-337, WAY-03, WAY-07, WAY-97, WAY-62
- `foundations/part_map.md` entry `product-guidelines`; `foundations/glossary.md` entry `Markdown file`
- the invariants `test-method-citation`, `guidelines-file-place`, `audit-series-script-paths`

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
