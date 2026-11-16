# Handoff to the one author — the return step

You are the one author of this change, resumed for the return step (step 11 of `implement-task`).
This is no variant row of `task-cycle/change/SKILL.md`: your stage is **the return step**. Read
`task-cycle/skill/return_step.md` whole and `task-cycle/skill/foundation_step.md` whole (the return
step writes as the foundation step writes), each from this worktree, and the `SKILL.md` of an element,
at the path `foundation_step.md` gives, when you write an entry of that element.

- Worktree `the task's worktree`, branch
  `task/walkthrough-in-running-product`; head now `cdbde3d2` (the whole-change review passed after one
  fix: `PASS cdbde3d2`). The frozen task `.runs/task-cycles/walkthrough-in-running-product/task.md`
  is the authority.
- Compare with the code the entries your change writes or changes (WAY-406, WAY-407, WAY-408, WAY-121,
  WAY-319, the glossary entry, the template of decisions), those the task names (its *Decisions in
  play*) and those your search of the foundation found, and the part map of the touched parts
  (`task-cycle`, `decisions`, `glossary`, `project-level`); correct what no longer matches in the same
  change. Take particularly into account the review's remarks that the last fix left as Minor findings
  (they go to the request's list and are NOT yours to fix unless they are a mismatch the return step
  finds by itself): kind 8 of `request_template.md` still titled "the user or the human will feel";
  `request_template.md` saying "its author reported" for an error the walk found; the heading of
  WAY-408 naming "the author" only; four re-flowed lines of the log past its usual width.
- Write, where the return step gives it: environment facts (a source outside the product the change
  rests on that the foundation does not hold), glossary terms, part-map changes, rows of *Settlements to
  record* the foundation step missed, a choice that binds after the merge. Write no invariant unless
  the task, a decision or the human sets the rule. The task's rows 1-5, 9-11 are in the log already;
  rows 6-8 stand in `task-cycle/change/walkthrough.md`; say in the report where each row went.
- Run the affected focused checks (`python -B elements/common/foundation_check.py`, and the directory
  tests of what you change). No full gate (CI is the final gate).
- Commit only if you change something, by path, in English; nothing under `.runs/`.
- Working copies: directory `.runs/author-return/`, removed before you return; the paragraph "Working
  copies" of your first handoff stands.
- Report: `.runs/task-cycles/walkthrough-in-running-product/reports/author-return-report.md`, with, as
  the record's *Return step* gives it: Foundation compared with code; Decisions written or changed;
  Invariants written or changed; Environment facts; Glossary terms; Part-map changes; Projected entries
  written whole or in part; Rows of *Settlements to record* written (row number and where it went).
  Plus **Unread material**, **Searches not found or unclear**, working copies, and any open question
  for the orchestrator. Return status, commits (or "none"), a one-line check result and the path.
