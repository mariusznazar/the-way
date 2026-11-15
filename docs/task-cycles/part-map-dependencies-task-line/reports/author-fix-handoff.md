# Handoff — the fix of the whole-change review's findings

## Delegation

The person who requested this cycle delegated the intermediate choices of the cycle to the
orchestrator. Nothing here is that person's approval. Do not ask the human: return `questions`.

## What to do

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`, your head `af76148`. Commit on this branch by path.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant "the fix of a review's findings".
  Read it whole (and the file it names for a fix when that step comes).
- Findings to fix: `reports/whole-findings.md` (full path
  `docs/task-cycles/part-map-dependencies-task-line/reports/whole-findings.md`), cut word for word
  from the review of the whole change, `reports/review-whole-report.md`, whose first line was
  `FAIL af7614867a6e477088a7831fc170c4b279b6ba21`. One blocking finding (I-1) and three Minor findings
  within the task (M-1, M-2, M-3). Fix all four. M-4 and the two out-of-scope items are not fixed.
- The fix's range runs from `af76148`. Run the affected checks again (the directories your fix
  touches by `python -B gate/run_tests.py <directory>`, and
  `python -B elements/common/foundation_check.py` without `--skip-test-citations`); not the whole gate.
- Evidence of the cycle on contested points (not a grade; the reviewer alone grades): the frozen
  task `docs/task-cycles/part-map-dependencies-task-line/task.md` says, in *Decisions in play*,
  that WAY-225 stays unchanged ("Bez zmiany"), and its item 7 words the sentence of `project-level`
  as "a nie za to, jak powstaje" without an exception for the derivation, while its row 6 gives the
  derivation to the-way. For M-3, fix every place the finding names that the task does not tell you
  to keep unchanged; where a fix of it would change a binding sentence of a decision the task keeps
  unchanged (WAY-225), do not change that sentence, and say so in your report with this evidence, so
  the orchestrator can show it to the reviewer of the fix. For I-1, the clause the reviewer gives is
  the fix; keep the part-map sentence at two sentences.
- Your directory for working copies: `.runs/author-fix/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/author-fix-report.md`. Return status,
  commits, one-line check result and the report's path.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

As before: each check with its command and exit code, the own-work check, **Unread material**,
**Searches not found or unclear**, working copies. A finding you hold wrong you answer with evidence.
