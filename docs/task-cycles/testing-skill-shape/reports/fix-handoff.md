# Fix of the review's findings — maintain-testing-guidelines in the WAY-256 shape

Same worktree, branch and rules as `reports/author-handoff.md`. Method: `task-cycle/change/SKILL.md`,
variant **"the fix of a review's findings"**; read the file it names for that variant.

- Fix base: `5dc4b3b`. The fix's range runs from it.
- Findings: `.runs/task-cycles/testing-skill-shape/reports/findings.md`, five blocking findings in
  the reviewer's words. Fix each, or answer with evidence a finding you hold wrong; the review of the
  fix reads that answer. This is the one fix the review allows.
- The reviewer's whole report, for its context and its walk: `reports/review.md`. Its Minor findings
  are not part of this fix and go to the request as they stand; leave them, unless a line you change
  for a blocking finding is the same line.

Where a fix moves a sentence, it moves it unchanged. A reword that changes a rule's meaning is not
applied; it stands as a proposal (task To do 7).

The findings reach the materials, which are part of the change's evidence:

- `reports/word-counts.md`: regenerate it from the head after the last change of a counted file, and
  have the helper compare each listed count with the file at the head.
- `reports/assessment.md`: the rows the fixes change, with their new places, regenerated, and every
  quote still literal against 00c0a74.
- Your own account of the figures goes into `reports/fix.md`; `author.md` stays as written, except
  where the handoff of finding 1 asks a figure of it be carried, which `fix.md` does by naming the
  counted file.

After the fixes, walk again by hand each of the six routes the fix reaches, as an agent would, from
`SKILL.md` to the file of the last step, and write what each reads.

## Checks

Run again what the fix affects: `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`, your `verify_reports.py`, and
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing). Do not run
the whole gate.

## Commits and report

New commits on the branch, `git add <paths>`, no history rewritten, no push. Full report:
`.runs/task-cycles/testing-skill-shape/reports/fix.md`, with each check's command and exit code, what
each finding became, every choice with the way not taken, reaches, concerns and **Searches not found
or unclear**. Return: your status, your commits, a one-line check result naming what failed or did
not run, and the report's path.
