# Handoff 02 — review of the whole change

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You
did not make this change. You are read-only: you write only your report. Questions go to the
orchestrator as a report with first line `questions`. Never present a go-ahead as the human's
approval.

## Where you work

- Worktree (your working directory, the process root): `the task's worktree root`
- Branch `task/private-path-patterns-in-code`; target branch `foundations`.
- The method of your stage is `task-cycle/review/SKILL.md` in this worktree: read it whole and
  follow it, and `whole_change.md` beside it when the step that names it comes. Your variant is
  "the whole change".

## What you review

- Range: base `73b51db53716f5a7656ae73f327c18e30e9fd5c5`, head `287a027` (one commit by the one
  author, no plan, no spec). Compute the diff yourself.
- The frozen task: `.runs/task-cycles/private-path-patterns-in-code/task.md`. Read it whole. Check
  coverage of every item of *To do* (1–6), both *Acceptance criteria*, each answered question
  (1–5) and each of the three rows of *Settlements to record*, and fidelity to the task's wording.
- The author's report: `.runs/task-cycles/private-path-patterns-in-code/reports/01-author-report.md`.
  It is a set of claims to verify, not evidence.
- Answers of the cycle's step 4: trust boundary — no; irreversible operation — no (the files the
  task changes are not named as a trust boundary by the part map); open design choice — none, the
  new command's name and argument form, the reading of the file names out of the sentence of the
  invariant and the exact patterns are how-to-make choices the author named in its report;
  reserved choice — none.
- Choices of the orchestrator you should know of, which you may find wrong:
  - the words "przepuszczony/przepuszczone zostaje" in the answers of questions 2 and 3 are read
    as "slips through, is not listed" (`zob.[[Notatka]]` and a lone `C<colon>\n`, `C<colon>\t`, `C<colon>\r` are
    accepted misses); the reasons stand in the author's report (concern 2) and in the cycle's
    record: the same task text uses "przepuszcza" for a miss, and a `[[` stuck to a dot is no link
    by question 2's own rule;
  - the part-map entry for the new command as a surface is not in the range: the cycle's return
    step, which comes after this review, writes it through `the-way-update-part-map`.
- The task's *Out of scope*: any change in loop2. The count of 10 places on the tracked files of
  loop2 in the first acceptance criterion could not be run (no access to that repository); judge
  whether the made-up files of the author's tests show the same shapes and whether the rules, as
  written, give 10 on the shapes the task names.

## What you select and read

You select your own foundation by "Reading the foundation" in `elements/common/way_of_working.md`,
by the parts the change touches (`task-cycle`, `installation`, and the foundation files as a file
that collects entries). The task's *Decisions in play* are WAY-309, WAY-320, WAY-16, WAY-321,
WAY-34 and the invariant `tracked-file-private-paths`; the change also writes WAY-323 and WAY-324.
There are no product guidelines in this repository (the task's question 5 settles that the cycle
does not wait for them).

## Checks you may run

Focused ones: `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py installation`,
`python -B elements/common/foundation_check.py`, and the new command on this repository. Do not run
the whole gate (`python -B gate/run_tests.py`): the orchestrator runs it. Do not change a tracked
file; a scratch repository for a crafted input belongs in a new empty directory under
`.runs/` of this worktree.

## Report

Write the full report to `.runs/task-cycles/private-path-patterns-in-code/reports/02-whole-change-review-report.md`
as the method gives it, with the first line `PASS <sha>` or `FAIL <sha>`, graded findings (each
with `file:line`), the checks you ran with command and exit code, and **Searches not found or
unclear** (`none` is an answer). Return your first line, your checks in one line and the report's
path.
