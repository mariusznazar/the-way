# Handoff — the return step after correction 1

You are the one author, resumed for the return step after correction 1. The person who requested this
cycle delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`, head `35796540` (the correction's
  one commit, reviewed `PASS 35796540`).
- Method: `task-cycle/skill/return_step.md` whole (and `task-cycle/skill/foundation_step.md` where you would
  write an entry). Compare with the code what correction 1 changed — the file
  `guidelines/coding-shared-module.md` (*Applies to* and *Where in code* now name `elements-common` and
  `elements/common/`) — with the foundation entries that bear on it: WAY-391 and the invariant
  `shared-module-import-runs-nothing`, the entries WAY-386 to WAY-390 for how a decision's *Scope* matches a
  guidance's *Applies to*, and the part map entry of `elements-common`. Correct in the same change whatever
  no longer matches, within what the correction's remarks and the task settle; a finding of the review of
  correction 1 that is marked outside the task's scope (WAY-391's *Scope*, the wording of WAY-19 and WAY-150)
  is **not** yours to fix here: say so in your report, naming each.
- Commit nothing unless something no longer matches. Do not run the full gate. Where you change a file, run
  the focused checks it affects and `python -B elements/common/foundation_check.py`, with command and exit
  code each.
- Your directory for working copies: `.runs/author-correction-1-return/` (remove it before you return). Make no
  file outside the worktree.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-correction-1-return-report.md`, in the
  form of the record's *Return step*, with **Unread material**, **Searches not found or unclear** and working
  copies.
