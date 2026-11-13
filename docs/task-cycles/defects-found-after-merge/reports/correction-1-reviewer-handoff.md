# Handoff — the reviewer of correction 1, `defects-found-after-merge`

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing
here is that person's approval. You did not make the change and did not write any earlier review of
it. Read-only: change nothing, commit nothing. Work from the worktree
`the task's worktree, which is the repository's root` (branch
`task/defects-found-after-merge`); start every command from its root.

## Stage and method

Stage: review a later change to an open request — a correction for the human's remarks. Method:
`task-cycle/review/SKILL.md` of this worktree. Read it whole; read a file it names only when the step
or variant that names the file comes. Dispatch information it asks for:

- Range to review: base `716b22a` (the request's head before the correction) to head `a3152c9`
  (one commit, one file: `task-cycle/skill/request_template.md`). Command: `git diff 716b22a..a3152c9`.
- The author's report: `.runs/task-cycles/defects-found-after-merge/reports/correction-1-author-report.md`.
- The human's remarks in place of a findings file (they bind), word for word in
  `.runs/task-cycles/defects-found-after-merge/reports/correction-1-remarks.md`. In short: add to the
  request template the sentence, or an example of it, that a correction which is only a refresh of the
  target branch carries with its pair `target-branch · none`, so the writer does not improvise it.
  The two items of *Needed from you* of the request are done outside the repository and the
  correction does not touch them.
- Whether the target branch was merged: no; `foundations` is still at `6814c6f`, the branch's base,
  so there was nothing to merge.
- Trust boundary: no. Irreversible operation: no.

## What to judge

That the correction does what the remark asks, and only that; that the new text agrees with the
decisions below and with `task-cycle/skill/correction.md` and `task-cycle/record_template.md`; that
the top part rules of the template (plain words, no file names, no identifiers of entries in what
the description carries) hold for the example sentences; and that nothing the correction touches
breaks a reader (`task-cycle/request_check.py` and its test). The frozen task, if you need it:
`.runs/task-cycles/defects-found-after-merge/task.md` (Polish).

## What to read (selection by the orchestrator, WAY-150, WAY-213)

Decisions, each whole: WAY-287, WAY-356, WAY-355, WAY-286, WAY-289, WAY-306, WAY-337. Files:
`task-cycle/skill/request_template.md` (whole), `task-cycle/skill/correction.md` (whole),
`task-cycle/record_template.md` (the item *Corrections after the request opened*). No product
guidelines exist in this repository.

## Report

Write the full report to `.runs/task-cycles/defects-found-after-merge/reports/correction-1-reviewer-report.md`
in the form the method gives; its first line `PASS <sha>` or `FAIL <sha>`. Include the checks you
ran with command and exit code, **Unread material** and **Searches not found or unclear** (each
`none` where none). Return only the first line, the finding counts by grade, and the report's path.
