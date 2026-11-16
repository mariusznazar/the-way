# Handoff — the fix of the review's findings

Stage: the fix of a review's findings, by the one author, resumed. Variant of `task-cycle/change/SKILL.md`: "the fix of a review's findings".

- Findings file: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/review-whole-findings.md` — read it whole. It holds one blocking finding (Important) and two Minor findings of the review of the whole change within the task, all three to be fixed now, in the reviewer's words. You may answer with evidence a finding you hold wrong.
- Worktree and branch as before; the reviewed head is `de24e5b8`; the fix's range runs from it. Commit by path, in English, as a new commit on the branch (no amend).
- Your directory for working copies: `.runs/author-fix/`; copies stand under the rule you already have. Your report path: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/author-fix-report.md`.
- Files of the cycle's record directory are not yours to read unless this handoff names them: this handoff and the findings file are the two it names (and your own earlier report).
- Run the affected checks again (the foundation check without `--skip-test-citations` and the directories your change touches), each with command and exit code; give your own-work check, **Unread material**, **Searches not found or unclear** and the working copies line. No full gate.
- Where you correct the *Rationale* sentence about the loop2 case, keep to what the task's sources say (`task.md`, *Context*, the evidence line): the reviewer found no ruling there and no harm was found.
- Return the status, your commits, a one-line check result and the report's path.
