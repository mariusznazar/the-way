# Handoff — the return step

## Delegation

The person who requested this cycle delegated the intermediate choices of the cycle to the
orchestrator. Nothing here is that person's approval. Do not ask the human: return `questions`.

## What to do

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`, head `1b5aba9` (the review of the whole change and of
  its fix both passed). You are the one author, resumed for the return step, class `same`.
- Stage: the return step, not a variant of `make-change`. Read
  `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` whole; the
  `SKILL.md` of an element, at the path `foundation_step.md` gives, when you write an entry of that
  element. Compare, as `return_step.md` gives, the foundation entries the change writes or changes,
  those the task names and those the search of the foundation found, and the part map of the touched
  parts, with the files of the repository, and correct in the same change whatever no longer
  matches. Write the sources outside the product and the glossary terms it asks for; write an
  invariant only for a rule the task, a decision or the human sets. A change of a decision's
  binding sentence beyond what the task carries is not allowed (WAY-30); WAY-225's sentence stays
  as the task says ("Bez zmiany").
- Frozen task, read whole: `docs/task-cycles/part-map-dependencies-task-line/task.md`. The
  remarks of the two reviews, for your use: `reports/review-whole-report.md` and
  `reports/review-whole-fix-report.md` (the latter: one new Minor, the width of line 4 of
  `foundations/part_map.md`; the cycle does not fix it).
- Commit what you correct, by path. If nothing no longer matches, commit nothing. Run the affected
  checks again and `python -B elements/common/foundation_check.py` without `--skip-test-citations`.
  Not the whole gate: the orchestrator runs it.
- Your directory for working copies: `.runs/return-step/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/return-step-report.md`, with what the
  return step compared, found and wrote, in the form `return_step.md` gives; return status, commits,
  a one-line check result and the report's path.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

Each check with its command and exit code, **Unread material**, **Searches not found or unclear**,
working copies.
