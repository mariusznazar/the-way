# Handoff to the reviewer of the merge of the target branch (correction 2)

You are a fresh reviewer: you did not make the change and did not write any earlier review of it.
Ask the human nothing; a question goes to the orchestrator in your report as `questions`.

## What you review

- The worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole; a file it names only when the step
  or variant that names it comes.
- The range: the merge commit `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6`, which merged the remote target
  branch `foundations` (`30c947f686b3d304f5a952cb6efe547762cfa247`, the merge of PR #140) into the task
  branch (`7ef5b13d3dff99dc16bf17dd253e74d2f0efa455`, the head the earlier reviews judged, whose code is
  `1d7d105`; the later commits only add and remove the record's copy under `docs/task-cycles/`, ignore it).
  The diff to review is `git diff 7ef5b13 2e31b74b`. What each side brought: the target branch
  `git diff 7ef5b13...30c947f`, the task branch `git diff 30c947f...7ef5b13`.
- The question to answer: **do the two sides still hold together?** PR #140 ("CI replaces the local final
  gate") changed `process-audit/audit_count.py` (it moved the pricing of stage rows into the new
  `process-audit/stage_pricing.py`) and the cycle's skill texts; the task branch moved the reading of the
  items *Discarded attempt* and *Review rounds* into the new `process-audit/record_items.py` and added a
  reading of the entries of both items. Three files conflicted and were resolved by hand in the merge
  commit:
  - `process-audit/audit_count.py`: two constant blocks, one from each side, both gone from the file
    (`NO_MODEL` and `ORCHESTRATOR` moved to `stage_pricing.py` by the target branch; `REPORT_FILE`,
    `ROUNDS_LABEL` and `ROUND_ENTRY` moved to `record_items.py` by the task branch). Check that no name
    is used and undefined, imported and unused, or defined twice.
  - `process-audit/test_audit_count.py`: a tuple of file names copied into a built checkout, now holding
    both new modules.
  - `task-cycle/skill/correction.md`: one paragraph holds both sides' edits, the discard wording of the
    task branch and the "on your own system ... local run" wording of the target branch.

  Check the auto-merged files too (`foundations/decisions.md`, `process-audit/SKILL.md`,
  `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/reserved_return.md`):
  that no sentence of one side now contradicts the other (for example a sentence of the task branch that
  says the gate runs on the orchestrator's own system, where the target branch now makes CI the final
  gate), and that the foundation entries the target branch changed that bear on the parts this change
  touches (`process-audit`, `task-cycle`, the decision log) — WAY-160, WAY-16, WAY-261, WAY-161, and the
  others that `git diff 7ef5b13...30c947f -- foundations/decisions.md` shows — still hold with the task
  branch's entries WAY-337, WAY-344, WAY-404 and WAY-405.
- The task the change carries out: `.runs/task-cycles/audit-answers-contradiction-after-code/task.md` (frozen).
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-merge-report.md`.
  Your directory for working copies: `.runs/review-merge/`.

Another agent, the author of a correction, edits this worktree meanwhile: judge the commits above, not
the files you find in the worktree later; do the checks in a worktree of `2e31b74b` in your directory.

## Checks

Focused checks only, in a worktree of `2e31b74b` in your directory: `python -B gate/run_tests.py process-audit`,
`python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py`, and the
directory of any other file the merge changed that holds tests. **Do not run the product's full gate.**
Report each check with its command and exit code.

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

First line `PASS <sha>` or `FAIL <sha>` (or `questions`); graded findings with places in the code and
whether a finding is a contradiction with an entry of the foundation; checks with commands and exit
codes; **Unread material**; **Searches not found or unclear**; the line on your working copies.
Return the first line, a one-line check result and the report's path.
