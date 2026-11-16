# Handoff to the reviewer of the renumbering and of the second merge of the target branch (correction 2)

You are a fresh reviewer: you did not make the change and did not write any earlier review of it. Ask the human nothing; a question goes to the orchestrator in your report as `questions`.

## What you review

- The worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole; a file it names only when the step or variant that names it comes.
- The range, two commits, judged with the earlier head `f5100d78` (the code the earlier reviews of correction 2 accepted) as the base:
  1. the renumbering commit `7957e5d0f68404095ea763e079dc6826c477c46d`: `git diff f5100d78 7957e5d0`;
  2. the merge commit `702525993aa85c5baa4cd239c64e0296e8d12948`, which merged the remote target branch `foundations` at `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898` (the merges of PR #141 and PR #142) into the renumbering commit: `git diff 7957e5d0 70252599` and what the target brought, `git diff 30c947f...3cbaeb9f`.
- The renumbering: the target branch took WAY-403 for its own decision (PR #142, "How does a task's branch give new numbers to its decisions that the target branch has taken?"). The task's two new decisions bore WAY-403 and WAY-404; before the merge they were renumbered in one pass as WAY-403 → WAY-404 and WAY-404 → WAY-405, as WAY-403 of the target (`foundations/decisions.md`, the decision of that title) gives. **The map to compare the pass with: 403 → 404, 404 → 405.** Before the pass the tracked files held 15 references to WAY-403 and 27 to WAY-404 (`foundations/decisions.md` 4 and 2; `process-audit/audit_count.py` 1 and 1; `process-audit/record_items.py` 1 and 1; `process-audit/test_audit_count.py` 2 and 5; `process-audit/test_record_items.py` 5 and 14; `task-cycle/review/SKILL.md` 1 and 0; `task-cycle/skill/SKILL.md` 1 and 2; `task-cycle/skill/correction.md` 0 and 1; `task-cycle/skill/reserved_return.md` 0 and 1). Judge: that the pass applied the map once and to whole numbers (a reference `WAY-404` after the pass stands where `WAY-403` stood, and `WAY-405` where `WAY-404` stood, no more, no fewer: count them in `git diff f5100d78 7957e5d0`); that no number of a decision of the target branch was changed; that no file of the range other than the renumbering changed in that commit; that the numbers in the headings, the *Relations* and *Based on* fields, the `decision:` lines of the tests, the `tests:` clauses and the prose of the two renumbered decisions all agree; and that `python -B elements/common/foundation_check.py` finds the two numbers and the target's WAY-403 each once.
- The question for the merge: **do the two sides still hold together?** PR #141 added a decision's *Relations* to the descriptive places of WAY-287 and a second required check to the ruleset fact; PR #142 added WAY-403 and its rule in `task-cycle/skill/SKILL.md` ("The renumbering of the task's decisions"), `task-cycle/skill/correction.md`, `task-cycle/record_template.md`, `elements/common/foundation_check.py` and its tests, `elements/decisions/template.md`. Name the foundation entries the merge brought in that bear on the parts the change touches (`process-audit`, `task-cycle`, the decision log): the target's WAY-403, WAY-287, WAY-160, WAY-19, WAY-02, and the others that `git diff 30c947f 3cbaeb9f -- foundations/decisions.md` shows; check that the renumbered decisions of the task now carry what the target's checks and template ask of a decision (`elements/decisions/template.md`, `elements/common/foundation_check.py`, which the focused check below runs), and that the task's sentences in `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md` and `task-cycle/record_template.md` and those the target added no longer contradict each other.
- The task the change carries out: `.runs/task-cycles/audit-answers-contradiction-after-code/task.md` (frozen). Note that the frozen task and the record refer to the decisions by the numbers of the pass.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-merge2-report.md`. Your directory for working copies: `.runs/review-merge-2/` (keep every probe and backup inside it).

## Checks

Focused checks only, in a worktree of `70252599` in your directory: `python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py elements`, `python -B elements/common/foundation_check.py` without `--skip-test-citations`, and the directory of any other file the merge changed that holds tests. **Do not run the product's full gate.** Report each check with command and exit code.

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

## The report

First line `PASS <sha>` or `FAIL <sha>` (or `questions`); graded findings with places in the code and whether a finding is a contradiction with an entry of the foundation; checks with commands and exit codes; **Unread material**; **Searches not found or unclear**; the line on your working copies. Return the first line, a one-line check result and the report's path.
