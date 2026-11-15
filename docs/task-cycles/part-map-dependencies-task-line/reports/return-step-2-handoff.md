# Handoff — the return step again, after correction 1

## Delegation

The human's day advisor, authorised by the human to settle the items of the request in the human's
name, answered it with the remarks in `reports/correction-1-remarks.md`; correction 1 (`b8b1ce1`)
carries them out and passed its review (`PASS b8b1ce1`, `reports/review-correction-1-report.md`).
Nothing here is further approval. Do not ask the human: return `questions`.

## What to do

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`, head `b8b1ce1`. You are the one author, resumed for the
  return step, class `same`.
- Stage: the return step, repeated for what the correction touched. Read
  `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` whole. Compare, as
  they give, with the files of the repository: the entries the correction wrote or changed (the
  decision on what is derived rather than written by hand and the *Rejected* of the decision on
  what the main branch holds where an invariant is not met, the invariant `audit-series-script-paths`
  that replaced `gate-runner-path` and the *Verification* that names it, the part-map template, the
  migration script that now imports the guidelines pattern), those the task names and those the
  search of the foundation finds, and the part map of the touched parts; correct in the same change
  whatever no longer matches, and write what the step asks (sources, glossary terms, invariants only
  for a rule the task, a decision or the human sets). A change of a decision's binding sentence
  beyond the term the remarks allow is not allowed (WAY-30).
- Notes of the review of the correction for your use: two lines of `foundations/decisions.md`
  (`:1740`, `:7360`) pass 100 columns; the path `task-cycle/cycle_stages.py` in `TREE_PATHS` of
  `process-audit/audit_count.py` is unguarded; the invariant's wording "the script that counts the
  measures of a cycle" is looser than WAY-339. The cycle does not fix a Minor finding of a
  correction; correct them only if the return step's own comparison finds them to be a mismatch
  with an entry the correction changed, and say which in the report.
- Commit what you correct, by path; commit nothing where nothing no longer matches. Run the affected
  checks and `python -B elements/common/foundation_check.py` without `--skip-test-citations`. Not
  the whole gate.
- Your directory for working copies: `.runs/return-step-2/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/return-step-2-report.md`: what the
  step compared, found and wrote in the form `return_step.md` gives; each check with command and exit
  code, **Unread material**, **Searches not found or unclear**, working copies. Return status,
  commits, a one-line check result and the report's path.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
