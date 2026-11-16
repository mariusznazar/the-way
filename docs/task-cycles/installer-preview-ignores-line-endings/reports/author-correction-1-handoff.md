# Handoff — correction 1 for the human's remarks

You are the one author of the change, resumed for a correction. Worktree
`the task's worktree`, branch
`task/installer-preview-ignores-line-endings`, head `81a21f51` (the last commit removes the record's
copy; your code stands at `ee4cbe35`). The request is open; its human's remarks are word for word in
`.runs/task-cycles/installer-preview-ignores-line-endings/reports/correction-1-remarks.md` — read it. It
is the only file of the record you read.

## The remark (the human's, binding)

Fix item 1 of the request: in `installation/README.md`, the table row of the agent definitions
(`.claude/agents/the-way-stage.md`, `.claude/agents/the-way-author.md`), at about lines 60-61, was
broken over two lines by the earlier fix, so on GitHub the row is cut after "as git stores them," and
the rest of the sentence shows as a separate row. Join the two lines so the row renders whole.

- Method: `task-cycle/change/SKILL.md` in this worktree (`make-change`), variant "a correction for the
  human's remarks". Read it whole, and a file it names only when the step that names it comes.
- Keep the change to that one join: the same words, one line, a single space where the line break was.
  No other edit. Check with `git diff` that the row is one line and that no other line of the file
  changed; check that the table's other rows are untouched.
- Your checks: the change is README text, so no test is needed; run `python -B gate/run_tests.py
  installation` only if you touch anything but that file (you should not). Do not run the full gate.
- Commit by path (`git add installation/README.md`), message in English, do not push.
- Trust boundary: the files are documentation only; irreversible operation: none.
- `cycle.md` and other agents' files (handoffs, reports, findings) are not yours to read unless named
  here.
- Working copies: none expected; if you make any, only under `.runs/author/`.

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

Report: `.runs/task-cycles/installer-preview-ignores-line-endings/reports/author-correction-1-report.md`,
as the method gives, with the commit, the check of the diff with its command and exit code, your own-work
check, **Unread material**, **Searches not found or unclear** (each `none` where none) and the line on
working copies. Return status, commit, one-line check result and the report path.
