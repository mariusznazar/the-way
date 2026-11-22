# Handoff — a correction for the human's remarks (`make-change`, "a correction for the human's remarks")

You are the one author, resumed for a correction after the human's review of the open request
https://github.com/mariusznazar/the-way/pull/157. Same worktree `the worktree root`,
branch `task/poprawki-z-przegladu-cykli-22-11`; the head is `2cbeb15bf9eda28476630cc97e58bb3b0011e1be`
(its tree equals that of `fb60dc7d`, the last commit of the return step; the two commits after it
only add and remove the record's copy). The same delegation holds: the orchestrator answers questions
from the task, the foundation and the code; nothing it says is the human's approval. The remote
target branch `foundations` has taken no commit since the base, so nothing is renumbered or merged.

## Method and variant

`task-cycle/change/SKILL.md`, the variant "a correction for the human's remarks" (read its row again
and `task-cycle/change/fix.md` where the variant names it). The remarks bind. The remarks, word for
word, are `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/correction-1-remarks.md`
(read it whole; it is the one file of the record directory besides this handoff and the frozen task,
`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`, that is yours to read; the other files
of the record are not).

## What to do

The remarks ask for three changes; items 1 and 3 of the remarks need nothing from you (the human
let the walk through the commands through, and the reading of WAY-02 whole is the reviewer's):

1. The method of the executor of a slice gets the sentence it lacks, in **one** place the executor
   reads — `task-cycle/change/slice.md` and/or `task-cycle/change/SKILL.md` §3, your choice, with
   the choice and its reason in your report: a test the plan lists as failing at the slice's base is
   reported as failing as expected, not as a failing check of its slice, and is not made to pass
   outside the slice's *Change*. Say it once, in as few words as the sentence allows (WAY-256), and
   word it so that it names the handoff as the source of the list (the executor does not read the
   plan), and so that it stays within the quoted wording of the task's point 3 and WAY-136 (a failure
   so named is no failing check of the slice) and WAY-229 (the retry is for a failing check of its
   slice). Do not copy the planner's or the orchestrator's sentences.
2. `instruction-files/check_instructions.py:454` — the comment writes the shell idiom as `'''`;
   write it as `'\''`, as the docstring and the test do. Mind the backslash in what you write (a
   backslash in a literal of a script you use to edit is a control character: write the file with
   your editing tool and search the file for the inserted idiom literally afterwards).
3. `instruction-files/check_instructions.py:12-18` — the module docstring says "Three cases are noted
   at the level `info`"; the code gives four (the bare relative name in a file given with `--file`,
   `dead_path_note`, present at the base too). Make the count right, and the list of the cases in the
   docstring.

Then, since this correction touches an instruction file of the task cycle, take the return step for
what it touches, as `task-cycle/skill/return_step.md` gives it: compare with the code the entries
that name the executor's handling of the tests a plan leaves failing and that name the info cases of
the check (the part-map entries of `task-cycle` and `instruction-files`, WAY-136 and the sentences you
and the first return step wrote), and correct in the same change whatever no longer matches; report
what you compared in the form of the record's *Return step*. Run the affected focused checks again
(the foundation check without `--skip-test-citations`, the instruction check on the-way, the tests of
`instruction-files`, ruff format and lint of the files you change, the directory run of
`agent-instructions` and `product-guidelines` where the guidelines or skills tests bear on the files
you change). Do not run the product's gate. Commit by path, messages in English.

## Notes

- Trust boundary: yes (`instruction-files/check_instructions.py`); the correction changes only a
  comment and a docstring of that file, no behaviour — say so in the report and keep it so.
- A new test file or a new file needs `git add` before the checks that list tracked files.
- Your directory for working copies: `.runs/author-correction-1/` of the worktree; the first paragraph
  of "Working copies" of `task-cycle/skill/SKILL.md` binds you as in your first handoff (a copy only
  in that directory, removed by its full path before you return, your report says where each stood
  and that it was removed).

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-correction-1-report.md`; its first
line is yours; it gives, for each of the three changes, what you changed and the commits; the choice
of place for the sentence; the checks with command and exit code; the return step's comparison;
your own-work check; **Unread material**, **Searches not found or unclear** and the line on working
copies. If the harness refuses the write, return the report whole as your answer. Return your
status, your commits, a one-line check result naming what failed or did not run, and the report's
path.
