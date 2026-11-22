# Handoff — the review of correction 1, `review-change`

You are the reviewer of the whole change and of its fix, resumed for the review of a correction the
author made for the human's remarks on the open request. Same worktree
`the worktree root`, same bounds: you did not make the
change, you write nothing in the repository, you ask no one. Review it once, with
`task-cycle/review/SKILL.md`, reading `task-cycle/review/fix.md` for "a correction made for the
human's remarks" (the remarks take the place of a findings file).

## What is reviewed

- The range: base `2cbeb15bf9eda28476630cc97e58bb3b0011e1be`, head
  `58997107c8055623854327a28a4e55f1a46553e1` (`git diff 2cbeb15b..58997107`; one commit, two files:
  `task-cycle/change/slice.md`, `instruction-files/check_instructions.py`). Confirm that
  `git rev-parse HEAD` is that head.
- The human's remarks, word for word:
  `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/correction-1-remarks.md`. They bind the
  correction; judge whether each is carried out and whether the correction holds anything new that is
  Critical or Important.
- The author's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-correction-1-report.md`.
- The frozen task: `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`.
- Trust boundary: yes (`instruction-files/check_instructions.py`); the author says the correction
  changes a comment and a docstring only. Verify it: compare the code of the file at the base and at
  the head (the comment and the docstring are the only difference), and confirm that the module's
  tests still pass.

## One thing the remarks ask of you beyond the diff

Remark 3 of the human: read **WAY-02 whole** (find its heading in `foundations/decisions.md`; an entry
read whole is the range of lines from its heading to the next heading of any level, with its
rationale and *Rejected*), and check **point 9 of the task** (the change to the rule of the
`decision:` line in tests: the new item of `task-cycle/change/SKILL.md` after "Name the break each
test catches", and the clause added to `elements/decisions/template.md` after "The line stands at the
test that holds the sentence") against it: whether the rule that point 9 writes goes against WAY-02
or leaves it holding. Say in your report what WAY-02 binds, how point 9's two edits stand to it, and
whether anything the whole change did — the tests of this change that carry `decision:` lines
included — goes against it. This is within the correction's review; a finding that comes of it is
graded as any finding is, and a finding outside the task's scope is marked so.

## Working copies and what you do not read

Your directory for working copies is `.runs/review-correction-1/` of the worktree; the first
paragraph of "Working copies" of `task-cycle/skill/SKILL.md` binds you as in the first handoff (a
copy only in that directory, removed by its full path before you return, your report says where each
stood and that it was removed; a probe that shows a finding is kept in `reports/` beside your
report). The other files of the cycle's record directory are not yours to read.

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/review-correction-1-report.md`; first
line `PASS <sha>` or `FAIL <sha>`; the sections `review-change` gives, **Unread material**,
**Searches not found or unclear**, each reach beyond what this handoff names and the line on your
working copies. If the harness refuses the write, return the report whole as your answer. Return the
first line, the changed files with their line counts, a one-line check result and the report's path.
