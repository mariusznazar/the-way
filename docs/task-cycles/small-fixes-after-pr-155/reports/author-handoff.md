# Handoff — the one author of the change

You are the one author of this change (agent type `the-way-author`). The human who asked for this
cycle has delegated intermediate choices to the orchestrator; no answer of the orchestrator is that
person's approval. You make the whole change; the orchestrator runs the product's gate, you do not.

## Where you work

- Worktree (your working directory for everything): `the root of the worktree`
  — the branch `task/small-fixes-after-pr-155`, base `80006b25feb4c5a6ffdb8f75d993051eecbc745d`. Commit
  there, naming files by path (`git add <path> …`, never `git add -A` or `git commit -a`). Never push.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant "the whole change as the one author".
  Read that `SKILL.md` whole, and a file it names only when the step or variant that names the file
  comes.
- Your directory for working copies: `.runs/author/` (under the ignored `.runs/` of the worktree).
- Your report: `.runs/task-cycles/small-fixes-after-pr-155/reports/author-report.md`. This file is the
  input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), the case the note on report
  names leaves open; write it there. Its name begins with the role, so it is not refused.
- `cycle.md` and the other files of `.runs/task-cycles/small-fixes-after-pr-155/` — other agents'
  handoffs, reports and findings — are not yours to read unless this handoff names them.

## Working copies (word for word from the cycle's rule)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

## The task

The frozen task, read whole: `.runs/task-cycles/small-fixes-after-pr-155/task.md` (the document
`Status: ready for cycle`, `Project relation: independent`). It is the requirement; its *To do*
points 1–4, *Acceptance criteria*, *Questions to settle* (answered), *Settlements to record* (rows 1
and 2) and *Out of scope* bind. Nothing in it is restated here.

No spec and no plan exist: the task leaves no open design choice, and one author holds the change.

Answers of the orchestrator at the start of the cycle (step 4):

- Trust boundary: yes. `task-cycle/gate_times.py` is a trust boundary file of the part `task-cycle`
  (it reads the output of the gate, which includes what failing tests print). Your change to it is
  small, but every review checks crafted input at that boundary; keep the reading of the output the
  way it is (the task puts a change of the rule itself out of scope).
- Irreversible operation: no.
- Open design choice: none. Reserved choice: none.

## What you write

1. The change of the task's *To do* 1–4, in `task-cycle/test_remove_merged_worktrees.py`,
   `task-cycle/test_gate_times.py` and `task-cycle/gate_times.py`.
2. The foundation step, as `task-cycle/skill/foundation_step.md` gives it — read it whole, and the
   `SKILL.md` of an element at the path it gives only when you write an entry of that element. The
   task carries one entry for it: *Settlements to record* row 1 goes to `guidelines/testing.md`
   (the rule on a git test that turns off automatic maintenance; row 2 is the code change of point 3
   and 4 and writes no entry). Write the row in the form the guidelines file and its skill
   (`product-guidelines/testing/SKILL.md`) give, in the brief form the human's answer to row 1 asks
   for: "the test repository, the bare remote one too, gets the setting in its own configuration, not
   in environment variables alone, because git passes none of them to the side that takes a `push` to
   a local repository". Do not found a shared helper for building test repositories; the task and the
   human's answer say there is none and that this task makes none.
3. The two proofs the acceptance criteria ask for, shown in your report with their commands and
   results (a one-off check made by hand, no mutation tool, WAY-402):
   - each of the four changes (i), (ii), (iii), (v) of *To do* 2, written once into a copy of
     `task-cycle/gate_times.py`, makes at least one test of `NestedRunTest` red, and the code as it
     stands in your change makes them all pass. Make each mutation in a copy under `.runs/author/`
     (never in the tracked file, never in a commit), and name for each mutant which test turned red.
   - a `GIT_TRACE` of a `push` into `origin.git` of the fixture, after your fix, shows no run of
     `git maintenance` and no run of `git gc` in `origin.git`; show the command and the lines you
     searched.
   Write the report so that the orchestrator can copy these two proofs into the record.

## What you read

Guidelines of the touched parts (`task-cycle`), each whole: `guidelines/coding.md`,
`guidelines/coding-command-runner.md` (`task-cycle/gate_times.py` is its exemplar, WAY-390),
`guidelines/testing.md`. You change `task-cycle/test_remove_merged_worktrees.py` and cite from it the
invariant `repository-changer-acts-only-when-told`; the code of `task-cycle/remove_merged_worktrees.py`
is not changed.

Foundation, from the orchestrator's selection (index: `.runs/task-cycles/small-fixes-after-pr-155/decision-index.md`,
which you may read, and each entry whole in `foundations/decisions.md` where it binds your work):
WAY-03, WAY-38, WAY-160 (the gate is not yours to run), WAY-228, WAY-232, WAY-233, WAY-234, WAY-235,
WAY-243 (flaky tests), WAY-253 (the author mutates in their head and checks), WAY-350 (what the timing
script is for), WAY-390, WAY-392, WAY-393, WAY-394, WAY-398, WAY-402. Invariants: `command-runner-passes-exit-code`,
`gate-times-refuses-impossible-entry`, `repository-changer-acts-only-when-told`, `ruff-blocking-rules`,
`formatter-layout`, `function-and-file-size`, `test-method-citation`. Glossary entries of the terms
you use. The task's evidence from the earlier review is in the history of git: `git show
399b46c7:docs/task-cycles/small-fixes-from-ai-review-and-audit/reports/<file>` for
`review-correction-1-report.md`, `review-correction-1-cases.txt`, `review-correction-1-cases.py`,
`review-correction-1-mutants.txt`, `review-correction-1-mutate.py`.

## Checks you run and report

Run, from the worktree, as the focused checks of what you change, each with its command and exit code
in your report: `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"`;
`python -B gate/run_tests.py task-cycle`; `python -B gate/run_tests.py agent-instructions` (the
formatter and linter invariants run there, and a test name has a limit of length); and, after the
foundation step, `python -B elements/common/foundation_check.py`. The test of
`ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` is flaky only
because of the background process; run it several times after your fix and say how many times and
that it held. The full gate is not yours to run.

A change to a test that holds a sentence of a decision by a line `decision:`, or that cites an
invariant (the test of point 1 cites `repository-changer-acts-only-when-told`; WAY-03), is named in
your report with the test and the invariant, so that the request can name it.

Your report holds, as `task-cycle/change/SKILL.md` gives, its **Unread material** and **Searches not
found or unclear** sections (`none` is an answer), the own-work check naming the weakest point of your
work and what it showed, and the line on working copies. Commit before you return and return only your
status, commits, a one-line check result and the report's path.
