# Handoff — the return step (step 11)

You are the one author of the change, resumed for the return step. Worktree
`the task's worktree`, branch
`task/installer-preview-ignores-line-endings`, head now `ee4cbe35` (your change `b2c31cc2` and its
fix). The whole-change review and the review of its fix both passed (`PASS`); nothing blocks. The one
Minor finding of the review of the fix (the README's agent-definitions row at lines 60-61 broken over
two lines) is outside your fixes by the cycle's rules and goes to the request's list: do not fix it.

- Method: `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` in this worktree;
  read each whole, and the `SKILL.md` of an element (path as `foundation_step.md` gives) only if you
  write an entry of that element.
- Do: compare with the code the foundation entries your change touches, those the task names (WAY-34;
  WAY-328 is withdrawn, replaced by WAY-379 · WAY-392) and those your search of the foundation found,
  and the part map entries `installation` and `installation-command`; correct whatever no longer
  matches, in the same change. Judge, and say in the report, whether the change settles a choice that
  binds after the merge (WAY-36) — for example that a lone `\r` is text and not a line ending, or that
  mixed endings with the same text are kept — and where that choice goes by the method; write an entry
  only where the method calls for one, never an invariant for behaviour merely because none covers it.
  The task carries no *Settlements to record* and no projected entry.
- If you commit anything, commit by path with an English message, do not push; a fresh reviewer on the
  strongest class will review that range. If nothing needs writing, commit nothing and say so.
- No full gate. `cycle.md` and other agents' files are not yours to read. Working copies only under
  `.runs/author/`, removed before you return, as in your first handoff.
- Report: `.runs/task-cycles/installer-preview-ignores-line-endings/reports/author-return-report.md`,
  in the items of the record's *Return step* (foundation compared with code; decisions, invariants,
  environment facts, glossary terms, part-map changes, projected entries and rows of *Settlements to
  record* written or changed, each `none` where none), plus the checks with command and exit code,
  **Unread material**, **Searches not found or unclear**, and the line on working copies. Return
  status, commits (or none), one-line check result and the report path.
