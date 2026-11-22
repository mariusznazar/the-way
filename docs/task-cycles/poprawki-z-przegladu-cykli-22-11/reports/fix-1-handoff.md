# Handoff — the fix of the review's findings (`make-change`, "the fix of a review's findings")

You are the one author, resumed for the fix of a review's findings. Same worktree
`the worktree root`, branch
`task/poprawki-z-przegladu-cykli-22-11`, the head the review judged is
`ae37fca3310ce6efe7e7939413b8b7a1205b0ead`; your fix's range runs from it. The same delegation as in
your first handoff holds: the orchestrator answers questions from the task, the foundation and the
code; nothing it says is the human's approval.

## Method and boundary

`task-cycle/change/SKILL.md`, the variant "the fix of a review's findings" (read the variant's
rows again; the fix reads no `walkthrough.md` as such — but finding I4 asks something of your report,
below). Fix every finding of the findings file, run the affected checks again and answer, with
evidence, a finding you hold wrong. Do not run the product's gate. Commit by path, messages in
English. The return step and the other stages are not yours now.

## The findings

The findings file is `reports/fix-1-findings.md` of the cycle's record directory
(`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/fix-1-findings.md`): four blocking
findings, I1–I4, each with the reviewer's mark of contradiction with the settlements, and one Minor
finding within the task's scope, M1, which the cycle also fixes in this change (a Minor finding of
the review of the whole change within the task is fixed before the request opens). Read it whole.
The reviewer's probes that I2 and I3 name stand in
`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/review-whole-probe-withdrawn/` and
`…/review-whole-probe-quote/`; you may read those two directories (input, `command.txt`, output).
The other files of the record directory are not yours to read.

## What the orchestrator requires of the fix, by finding

- **I1** (no contradiction): write the orchestrator's duties of point 3's quoted wording into the files
  the orchestrator reads — `task-cycle/skill/planning.md` ("A slice's handoff": the tests the plan
  leaves failing at the slice's base, with their owners, are listed in the handoff of each later
  slice; the orchestrator gives an owner by editing the plan before the next slice is dispatched
  where a report names a failing test no *Goal* names) and step 9 of `task-cycle/skill/SKILL.md`
  (sub-step 2's list of what the handoff carries, and sub-step 4's retry: an executor that reports
  as failing only a test the plan lists as failing for its slice is no executor "that reports a
  failing check of its slice"). Keep the wording of the task's quoted sentences word for word where
  they stand now in `task-cycle/plan/SKILL.md`; the sentences you add in the orchestrator's files
  carry the duty in as few words as the wording allows and repeat no text beyond what is needed
  (WAY-256). The sentences you add stay within what WAY-136 and WAY-229 now say; where a decision
  needs a word for it, say so in your report rather than widening the decision.
- **I2** (contradiction, WAY-344): `withdrawn_numbers` in `elements/common/decision_index.py` reads
  the table by the names of its columns; a missing or renamed column ends the script with exit code
  2 and a message that names the file and the field, as WAY-344 gives and as the way the base's script
  ends for the table; add the test `guidelines/testing.md` and WAY-344 give — the file given without
  a field it needs. Check the neighbouring reads of the same change for the same fault.
- **I3** (no contradiction): complete point 5.1's "tekst z cudzysłowem" so that the six `'\''`
  tokens the reviewer's probe names and a text in typographic quotation marks are no path, without
  taking a real path out of the lookup (a name with a quote inside a real path stays looked up where
  a rule of the lookup says so; state your rule and its price in the report); extend the tests, the
  docstring of the script and the sentence of `instruction-files/SKILL.md` if it names the
  characters.
- **I4** (contradiction, WAY-406): in your report, the section "Walkthrough" is replaced by the
  judgment WAY-406 and `task-cycle/change/walkthrough.md` ask for — read that file whole now. The
  change alters what five commands print and how they end; the foundation settles no way to run
  the-way as a running product, so the walk is not performed, with that reason; draw up the cases
  from the requirements of the task and mark each as unchecked with that reason, in the form the file
  gives. Rewrite the report's Walkthrough section (the report file you wrote is
  `reports/author-report.md`; update it in place, and keep the rest as it stands, adding the fix's
  own section for this round).
- **M1** (Minor within the task): in `task-cycle/review/whole_change.md` give the product's form of
  the README path and say that the reviewer runs the script itself, as the finding gives.

## The other notes

- Trust boundary: yes (`task-cycle/gate_times.py`, `instruction-files/check_instructions.py`);
  think of crafted input at `check_instructions.py` again for I3.
- After `git add` of any new file, run the checks again (many list only tracked files); run the
  foundation check on the finished change without `--skip-test-citations`.
- Your directory for working copies: `.runs/author-fix-1/` of the worktree. The first paragraph of
  "Working copies" of `task-cycle/skill/SKILL.md` binds you as in your first handoff: a copy goes only
  into that directory, is removed by its full path before you return, and your report states where it
  stood and that it was removed.

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-fix-1-report.md` (its first line is
yours; it holds, for each finding, what you changed, the commits, the checks with command and exit
code, and for I4 the walk's judgment and its cases), **Unread material**, **Searches not found or
unclear**, and the line on working copies. If the harness refuses the write, return the report
whole as your answer. Return your status, your commits, a one-line check result naming what failed
or did not run, and the report's path.
