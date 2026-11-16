# Handoff — review of the whole change

## Delegation

The person who requested this cycle delegated the intermediate choices to the orchestrator of the
cycle. You review as an agent that made none of the change. Grade and scope of every finding are
yours: nothing in this handoff calls a finding wrong, Minor or outside the scope. Ask no human anything;
a question goes to the orchestrator in your report as your method gives it.

## Where and what

- Worktree: `the root of the task's worktree`, branch `task/script-invariants-by-test`. This is
  the-way itself; the process root is the worktree. You change nothing in it.
- Method of your stage: `task-cycle/review/SKILL.md`, read whole; for the review of the whole change it
  names `whole_change.md` beside it, which you read and follow. Your variant: "the whole change".
- Range: base `604907c88d9973ccf2dbf697e3ce7e1f358fa81c` to head `4bc1667c` (the one commit of the author;
  confirm `git rev-parse HEAD` is the head it gives, and compute the diff yourself with `git diff <base>..<head>`).
- The frozen task, read whole: `docs/task-cycles/script-invariants-by-test/task.md`. There is no spec and no plan; the
  route is one author without a plan, so no slice had a review of its own — you judge the whole change.
- The author's report: `docs/task-cycles/script-invariants-by-test/reports/author-report.md`. It is a set of claims
  to verify, not evidence.
- Your directory for working copies: `.runs/review-whole/` of the worktree.
- Your report: `docs/task-cycles/script-invariants-by-test/reports/review-whole-report.md`; its first line is
  `PASS <sha>`, `FAIL <sha>` or `questions`.
- `cycle.md` and the other files of `docs/task-cycles/script-invariants-by-test/`, other than the two named above,
  are not yours to read.
- You do not run the product's full gate (WAY-160). You may run the focused directories
  (`python -B gate/run_tests.py elements/part-map`, `... elements/common`) and `python -B elements/common/foundation_check.py`.
  A test is seen red by breaking the behaviour in a working copy under `.runs/review-whole/`, never in the worktree itself.

## What the orchestrator tells you

- Trust boundary of the change: no. Irreversible operation: no. The task moved no pin.
- Autonomous choices of the orchestrator you should know of (Q1, Q2): the task's *Decisions in play* names WAY-328, withdrawn
  on this base (the guidelines of the-way's own code and tests exist: WAY-379, WAY-392), so the author followed
  `guidelines/coding.md` and `guidelines/testing.md`; and the task's *Context* lists five tracked kinds while the base also tracks
  `.github/workflows/tests.yml`, `requirements-quality.in`, `requirements-quality.txt` and `ruff.toml`, which row 1 of *Settlements to
  record* has the author add to the list of `script-language` with a reason; judge each reason.
- Unread material the author names: it read WAY-344 only to its *Scope* and WAY-395 in part (it states this in its report).
  You read both whole as part of your own selection and judge the author's reading of files against WAY-344.
- Coverage you check, by the task, not by the author's list: each item 1–5 of the task's *To do*, each row 1–3 of *Settlements to record*
  against the code (the list of kinds; the failure on another interpreter naming both versions; the reach of `script-imports` equal to that of
  `cross-part-imports`, including a name that cannot be worked out), the four invariant entries (`Method: test` and nothing else changed),
  each invariant's test seen failing once (WAY-08) — repeat at least the failing run of each invariant's test yourself in a working copy.
  The tests are new invariant tests; the request names them (WAY-03).
- The change adds only tests and four words of the foundation; judge from the guidelines, `guidelines/testing.md` (levels, expected values,
  behaviour not implementation, trust boundaries) and `guidelines/coding.md`, the guideline files of the parts you find the change touches,
  each whole. You select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` and
  `product-guidelines/reading.md`; the task's *Decisions in play* are WAY-38, WAY-89, WAY-09, WAY-08, WAY-61 (WAY-328 withdrawn).

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

## What the report holds

As `task-cycle/review/SKILL.md` gives it, with the first line, the graded findings (each with its place `file:line`, its grade, whether
within the task's scope and whether it contradicts the settlements), the checks you ran with command and exit code, how many decisions of the
index you read whole, your **Unread material**, **Searches not found or unclear**, and your working copies line.
