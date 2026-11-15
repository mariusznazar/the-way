# Handoff — review of correction 1 for the human's remarks

## Delegation

The human's day advisor, authorised by the human to settle the items of the request in the human's
name, answered request 130 with the remarks in `reports/correction-1-remarks.md`
(`docs/task-cycles/part-map-dependencies-task-line/reports/correction-1-remarks.md`). They bind
the correction; you review whether the correction does what they say and breaks nothing else.
Nothing here is the human's approval. Do not ask the human: return `questions`.

## What you review

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`. Read-only. Range of the correction: base `1e45b6e` (its
  tree equals that of the head you reviewed, `1b5aba9`) to head `b8b1ce1` (confirm
  `git rev-parse HEAD`). One commit, six files.
- Method: `task-cycle/review/SKILL.md` (`review-change`), a correction made for the human's
  remarks; read `fix.md` beside it and follow it: the remarks in place of a findings file. Your first
  line is `PASS <sha>` or `FAIL <sha>`.
- The correction's report (claims, not evidence):
  `docs/task-cycles/part-map-dependencies-task-line/reports/author-correction-1-report.md`. The
  frozen task is `docs/task-cycles/part-map-dependencies-task-line/task.md`; your earlier selection
  stands, reach for more selectively and name each reach.
- Points to judge:
  1. The change of the decision on what is derived rather than written by hand, and of the
     *Rejected* of the decision on what the main branch holds where an invariant is not met, is the
     term only ("dependency of a part"), as the remarks say, with the advisor's consent, which is
     the human's consent to change a decision the task kept unchanged. A change of meaning, or of a
     binding sentence beyond the term, is a finding; check also that no `decision:` line of a test
     now quotes a changed sentence wrongly.
  2. The part-map template now says a part, and a surface, is described briefly in as few sentences
     as needed. The correction also changed the surface placeholder and the section "Surfaces",
     which the remarks name only for a part; judge whether that is within the remarks.
  3. The two guards: the copy of the guidelines pattern in `elements/common/migrate_foundation.py`
     is removed and the script imports `GUIDELINES` from `foundation_check.py` (check that the import
     resolves where the script runs, from a pinned checkout included, and that `cross-part-imports`
     allows it); the invariant `gate-runner-path` is widened and renamed `audit-series-script-paths`
     and its test renamed `process-audit/test_audit_series_scripts.py`: one rule to a sentence, the
     test fails when the reading side or the writing side of each path changes alone (break each in
     a working copy of yours under your directory, never in the worktree, and name the command and
     exit code), the invariant cited by `invariant:`, `Derives from` and the decision's
     *Verification* agree, no reference to the old identifier is left (`git grep` for it).
  4. Nothing outside the remarks changed, and `process-audit/audit_count.py` (a trust-boundary file)
     is untouched.
- A new Critical or Important finding counts as one that remains; a Minor finding of a correction
  is not fixed and goes to the request's list.
- Your directory for working copies: `.runs/review-correction-1/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/review-correction-1-report.md`. You do
  not run the whole gate.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

First line, the checks you ran with commands and exit codes, **Unread material**, **Searches not
found or unclear**, working copies.
