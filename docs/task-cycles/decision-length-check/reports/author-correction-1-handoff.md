# Handoff — correction 1, for the human's remarks

You are the one author, resumed for a correction after the human's remarks on the open request.
The remarks bind. The person who requested this cycle delegated intermediate choices to the
orchestrator; no answer here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`; the head you start from is
  `2ffff547` (the commit that removes the record's copy; the change's code is as `9c7f9b71` left it).
  Work from the worktree's root. The target branch has no new commit, so nothing was merged or
  renumbered.
- Your method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; read
  `task-cycle/change/fix.md` or the file the variant's row names, as the variant gives.
- The remarks, word for word: `.runs/task-cycles/decision-length-check/reports/correction-1-remarks.md`.
  Read it whole. It has two answers; **only the first asks for a change of files by you**:
  1. Fix the gap of `guidelines/coding-shared-module.md`: add `elements-common` to its *Applies to*,
     and `elements/common/` to its *Where in code*, so an agent that changes a shared module in that
     directory is handed that guidance. No other change to that file; make no change to its *Files of
     this kind* table, rules or examples. Check the file's form against the-way's guidelines
     (`guidelines/coding.md` names how a coding guidelines file is written; `product-guidelines/reading.md`
     explains how *Applies to* is read) and against the tests that read guidelines files, and say in
     the report what they accept.
  2. The reading of six decisions whole is the work of a fresh reviewer, not yours: do not read or judge
     them for that purpose.
- The commit goes on the task branch, by path, in English; leave the worktree clean. Do not touch the
  record's copy in `docs/task-cycles/` (it is not in the tree) or the files of `.runs/task-cycles/`.
- Checks to run again, each with command and exit code: `python -B gate/run_tests.py product-guidelines`,
  `python -B gate/run_tests.py agent-instructions`, `python -B elements/common/foundation_check.py`
  (exit 0, `0 errors`), the linter if any Python file changed (none is expected). Do not run the
  product's full gate: CI is its final gate and a local run is the orchestrator's.
- Your directory for working copies: `.runs/author-correction-1/`; remove it before you return.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-correction-1-report.md`, with its
  status, commits, checks, own-work check, **Unread material**, **Searches not found or unclear** and
  working copies, as before.
