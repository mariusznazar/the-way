# Handoff — the return step

## Delegation

As in `reports/author-handoff.md`: the delegation is the orchestrator's; your go-aheads are never the human's approval; you ask no human anything.

## What you do

- You are resumed as the one author, for the return step (step 11 of the cycle). Read `task-cycle/skill/return_step.md` and
  `task-cycle/skill/foundation_step.md`, each whole; the `SKILL.md` of an element (path in `foundation_step.md`) when you write an entry of it.
- The change you compare: base `604907c88d9973ccf2dbf697e3ce7e1f358fa81c` to head `540aed04` (your first commit `4bc1667c` and the fix
  `540aed04`, which moved `test_script_invariants.py` to `agent-instructions/`). The review of the whole change passed
  (`PASS 4bc1667c`, Minor findings fixed) and so did the review of the fix (`PASS 540aed04`); you read neither report.
- Compare with the files of the repository, as `return_step.md` gives: the foundation entries the change writes or changes (the four
  invariants), those the task names (WAY-38, WAY-89, WAY-09, WAY-08, WAY-61), those your search of the foundation found, and the part map of
  the parts the change touched (now `agent-instructions`, `elements-common` and `invariants`, besides `part-map` whose test file left).
  Correct in the same change whatever no longer matches. Commit what you change by explicit path; where you change nothing, commit nothing.
- Write no entry for behaviour merely because no invariant covers it; write an invariant only for a rule the task, a decision or the human sets.
  A choice of the change that binds after the merge goes to the place the questions of the decisions template give it, or stays a row of the
  questions table; the choices of your first report (1–6) and of the fix are for you to judge by that rule.
- Your directory for working copies: `.runs/author/` (the same). Your report:
  `docs/task-cycles/script-invariants-by-test/reports/author-return-report.md`, with the items of the record's *Return step* — foundation
  compared with code; decisions, invariants, environment facts and glossary terms written or changed; part-map changes; projected entries
  written; rows of *Settlements to record* written, with the place each went to (rows 1–3: the test code) — with **Unread material** and
  **Searches not found or unclear**, and the line on working copies.
- You run no full gate (WAY-160): run the focused directories you change and `python -B elements/common/foundation_check.py`
  (without `--skip-test-citations`).

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
