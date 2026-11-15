# Handoff — correction 1 for the human's remarks

## Delegation

The human's day advisor, authorised by the human to settle the items of the request in the human's
name, answered the request (pull request 130) with the remarks in
`reports/correction-1-remarks.md` (full path
`docs/task-cycles/part-map-dependencies-task-line/reports/correction-1-remarks.md`). They bind: do
what they say, word for word as written there, in this one round. Nothing here is further approval;
do not ask the human, return `questions` to the orchestrator.

## What to do

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`, head `1e45b6e` (the tree equals that of `1b5aba9`, the
  reviewed head; `origin/foundations` has not moved from `c2541ed`, so nothing was merged in). Work
  from its root; commit on this branch by path, in English.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant "a correction for the human's
  remarks". Read it whole, and the file it names for this variant when its step comes. You are the
  one author, resumed, class `same`.
- The three things the remarks ask, in this request:
  1. The rule of the decision log that says "a dependency the code holds that the part map does not
     allow … never by rewriting the allowed dependencies to fit the code" (the decision on what in
     a product's foundation is derived rather than written by hand), and the places of the log that
     carry that sentence — its pair of examples and prose, and the *Rejected* of the decision on
     what the main branch holds where the product does not meet an invariant, which the reviews
     named — say "dependency of a part" where they now say "dependency". The human's day advisor
     consents to this change of the decision the task kept unchanged: the change is the term only,
     its meaning stays as the map now defines it. Search the foundation once for each other place
     that states the same sentence and carries the bare word, and correct it by the same rule
     (WAY-33, WAY-97).
  2. The part-map template says one sentence for a part (`elements/part-map/template.md`, the
     placeholder at line 42 and the sentence at lines 191–193, and anything else the search finds):
     bring it to what the map keeps — a part is described briefly, in as few sentences as its
     responsibility needs — so the template and the map no longer disagree.
  3. Guard each of the two reads the reviews named as unguarded, the way this request guards the
     other five, by a test that fails when one side changes alone: the second copy of the pattern for
     guidelines files in `elements/common/migrate_foundation.py` (or, if simpler, remove the copy
     and read the one source in `elements/common/foundation_check.py`, which the same part may
     import), and the paths `MEASURES_SCRIPT` and `GATE_SCRIPT` that `process-audit/audit_count.py`
     reads (both files of `task-cycle`). Where a test is the guard, it comes with an invariant of
     the foundation as the five existing ones do (read `elements/invariants/template.md` and the
     skill; an existing invariant of this request may be widened if that is simpler and keeps one
     rule to a sentence), cited by `invariant: <identifier>` in the test, seen failing once with its
     command and exit code and then passing. `process-audit/audit_count.py` is a trust-boundary
     file: do not change it; the guard only reads its constants.
- Read first: the findings the two reviews gave on these points
  (`reports/review-whole-report.md`: M-3, O-1, O-2; `reports/review-whole-fix-report.md`), the
  existing tests `process-audit/test_gate_runner_path.py` and `elements/common/test_guidelines_place.py`
  and the invariants `gate-runner-path` and `guidelines-file-place`, `elements/part-map/template.md`
  whole, and the decisions you change, whole (the decision on what is derived rather than written by
  hand, and the one on what the main branch holds where an invariant is not met), with their
  *Verification* and *Rationale*.
- Do not touch anything else; the other items of the request stand as they are. A finding of your
  own that the remarks do not cover goes in your report, not into a change.
- Checks: the affected directories by `python -B gate/run_tests.py <directory>`, each failing
  once as above where a new test guards, and
  `python -B elements/common/foundation_check.py` without `--skip-test-citations`. If a skill's
  description or an agent type changes, run the generator the root `AGENTS.md` names. Not the whole
  gate: the orchestrator runs it.
- Your directory for working copies: `.runs/author-correction-1/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/author-correction-1-report.md`:
  what you changed for each of the three things, each check with command and exit code, the
  own-work check, **Unread material**, **Searches not found or unclear**, working copies. Return
  status, commits, a one-line check result and the report's path.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
