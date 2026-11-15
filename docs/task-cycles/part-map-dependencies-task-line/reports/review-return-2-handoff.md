# Handoff — review of the return step's commit after correction 1

## Delegation

The person who requested this cycle delegated the intermediate choices to the orchestrator.
Nothing here is the human's approval. Do not ask the human: return `questions`.

## What you review

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`. Read-only. Range: base `b8b1ce1` to head `7d9bc5a` (confirm
  `git rev-parse HEAD`): the commits of the return step. First line of your report:
  `PASS <sha>` or `FAIL <sha>`.
- Method: `task-cycle/review/SKILL.md` (`review-change`); the return step's commits are reviewed
  against the task and the foundation entries the return step writes or corrects, as its section 2
  gives. Read the `SKILL.md` whole.
- What the return step did, per its report
  (`docs/task-cycles/part-map-dependencies-task-line/reports/return-step-2-report.md`; a set of
  claims, not evidence): it reworded the invariant `audit-series-script-paths` in
  `foundations/invariants.md` so that its sentence names the measures of how a cycle's agents use the
  context and the prompt cache, as the decision on when the audit's measures stop being comparable
  (WAY-339) speaks of them, and updated the docstring of
  `process-audit/test_audit_series_scripts.py` to the same words; the test's behaviour is unchanged.
- The frozen task: `docs/task-cycles/part-map-dependencies-task-line/task.md`. The remarks of the
  human's day advisor that correction 1 carries out: `reports/correction-1-remarks.md`; the
  correction's review: `reports/review-correction-1-report.md` (`PASS b8b1ce1`, with three Minor notes,
  one of which this commit answers).
- Read whole the entries you judge it against: the invariant `audit-series-script-paths`, the decision
  WAY-339 and the glossary term `dependency of a part` if you need it; the invariants template
  `elements/invariants/template.md` for the form of the sentence. Judge: the sentence says what the
  test checks and what WAY-339 says, one rule to a sentence; the docstring agrees; nothing else
  changed; no `decision:` or `invariant:` line broke; run
  `python -B elements/common/foundation_check.py` (no `--skip-test-citations`) and
  `python -B gate/run_tests.py process-audit`.
- A Minor finding is not fixed in this review; name each reach beyond this handoff.
- Your directory for working copies: `.runs/review-return-2/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/review-return-2-report.md` with
  **Unread material** and **Searches not found or unclear**, the checks with commands and exit
  codes, working copies. You do not run the whole gate.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
