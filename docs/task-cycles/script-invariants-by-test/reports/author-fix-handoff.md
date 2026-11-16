# Handoff — the fix of the Minor findings of the review of the whole change

## Delegation

As in `reports/author-handoff.md`, which you already know: the delegation is the orchestrator's, your go-aheads are
never the human's approval, and you ask no human anything.

## What you do

- You are resumed as the one author. Variant of `task-cycle/change/SKILL.md`, in the words of its row: "the fix of a review's
  findings" — read `task-cycle/change/fix.md`, which that row names, whole.
- The review of the whole change returned `PASS 4bc1667c` with no blocking finding and four Minor findings within the task.
  The findings are in `docs/task-cycles/script-invariants-by-test/reports/fix-findings.md`, in the reviewer's words
  (`reports/fix-findings.md`). Fix each of the four, run the affected checks again, and answer with evidence a finding you hold wrong.
- The reviewer's report, for the evidence behind a finding: `docs/task-cycles/script-invariants-by-test/reports/review-whole-report.md`.
  Read only what a finding needs.
- M3 names two ways: widen the sentence of `part-map` in `foundations/part_map.md` (the return step's way, with the skill
  `elements/part-map/skill/SKILL.md`), or move the file, or the two tests of it that import nothing, to `agent-instructions/`. The
  choice is yours: take the one that keeps the part map and the tests agreeing with the fewest changes and say which and why, with
  the way rejected and its cost. Whichever you take, a test that cites an invariant keeps its line `invariant: <identifier>`.
- The range of the fix runs from the reviewed head `4bc1667c`. Commit on the branch `task/script-invariants-by-test` in the
  worktree `the root of the task's worktree`, by explicit path, messages in English.
- Your directory for working copies: `.runs/author/` (the same as before). Your report:
  `docs/task-cycles/script-invariants-by-test/reports/author-fix-report.md`, in the form `task-cycle/change/fix.md` gives, with
  **Unread material** and **Searches not found or unclear**.
- You run no full gate (WAY-160). Run the focused directories you change as `python -B gate/run_tests.py <directory>` and
  `python -B elements/common/foundation_check.py` (without `--skip-test-citations`).
- Names of the tests you change or add are in your report (WAY-03); a change of the expected value of an existing test goes with its
  cause and evidence (`guidelines/testing.md`, "Changing an existing test").
- The orchestrator's choice Q3: the reviewer read WAY-344 and WAY-395 whole; read WAY-344 and WAY-395 whole yourself for M2 and M4, as
  your first reading was in part.

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
