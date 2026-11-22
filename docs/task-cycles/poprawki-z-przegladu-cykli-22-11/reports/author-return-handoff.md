# Handoff — the return step (the one author, resumed)

You are the one author, resumed for the return step. Same worktree
`the worktree root`, branch
`task/poprawki-z-przegladu-cykli-22-11`; the head after the review of your fix is
`41921006168c95b1de449ea546fab2271ec815e9` (the review of the whole change failed on `ae37fca3`;
your fix of its findings was reviewed and passed). The same delegation holds: the orchestrator answers
questions from the task, the foundation and the code; nothing it says is the human's approval.

## Method

Read `task-cycle/skill/return_step.md` whole and follow it, with `make-change`
(`task-cycle/change/SKILL.md`) as the method of your work: it is the return step, step 11 of
`implement-task`, as that file gives it. It compares with the code the entries the change writes or
changes (WAY-255, WAY-25, WAY-136, the new WAY-418, the edited templates and skills), those the
task names (its *Decisions in play*), those your search of the foundation found, and those your
own search by the names and words the change's code adds finds (`--decision` by value, `fits by
ranges of`, `shutil.which`, `Ran <n> tests`, the levels `info` and `warn` of the instruction check,
the part-map entries of the parts touched), and corrects in the same change whatever no longer
matches; it writes what that file lists (environment facts, glossary terms by WAY-95, a row or
projected entry the foundation step missed, a choice that binds after the merge), and nothing
beyond. The frozen task is
`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`; no spec, no plan.

Do not fix the Minor finding the review of the fix found new (the comment at
`instruction-files/check_instructions.py:454` writes the idiom as `'''`): a Minor finding of the
review of a fix does not block and goes to the request's list, and the cycle runs no third round.
Do not run the product's gate. Commit by path, messages in English; where you change nothing, commit
nothing and say so. Where you change anything, name every commit.

## Working copies

Your directory is `.runs/author-return/` of the worktree; the first paragraph of "Working copies" of
`task-cycle/skill/SKILL.md` binds you as in your first handoff (a copy only in that directory,
removed by its full path before you return, the report states where each stood and that it was
removed). The files of the cycle's record directory other than the frozen task, this handoff and
your own reports are not yours to read.

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-return-report.md`; its first line is
yours; it gives, in the form of the record's *Return step*: Foundation compared with code,
Decisions written or changed, Invariants written or changed, Environment facts, Glossary terms,
Part-map changes, Projected entries written whole or in part, Rows of *Settlements to record*
written (the place each went to); then **Unread material**, **Searches not found or unclear** and the
line on working copies. If the harness refuses the write, return the report whole as your answer.
Return your status, any commits, a one-line check result naming what failed or did not run, and the
report's path.
