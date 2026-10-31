# Fix handoff — maintain-coding-guidelines in the WAY-256 shape

Same worktree, branch, cycle directory (`<cycle>`) and rules of commits and scripts as your first
handoff, `<cycle>/reports/author-handoff.md`. Questions come back to the orchestrator; never ask the
human. Do not push.

## Method and variant

In `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**. Read the file it names
for that variant.

## What you fix

- Findings file: `<cycle>/reports/findings.md`, two blocking findings of the review of `097123e`.
  Fix base: `097123e`.
- Answer with evidence a finding you hold wrong, rather than leaving it.
- The rule of WAY-29 applies to finding 2: a rationale for a decision the human took comes from the
  source, and a sentence of reason the source does not give stays out of the entry. Use only what
  rows 1 and 2 of *Settlements to record* and task question 3 keep.
- The Minor findings of the review are not yours to fix; they go to the request. Touch no other text
  of the skill or the foundation.

## After the fix

- The fix changes counted files, so regenerate `<cycle>/reports/word-counts.md` and run the helper
  that compares every figure with the files after your last change to a counted file.
- Bring `<cycle>/reports/assessment.md` in line where the fix changes what a row or its list of
  added text says.
- Run again the affected checks, each with its command and exit code:
  `python -B elements/common/foundation_check.py`,
  `python -B instruction-files/check_instructions.py .`, your `check_assessment.py` and
  `verify_counts.py`, and `python -B gate/run_tests.py installation`. Do not run the whole gate.
- Walk route 6 again from `SKILL.md` to `hand_back.md`, and write down which items of the task
  document and of step 4 it now takes and which it leaves. A walk that names the pointer without what
  the pointer leaves does not answer finding 1.

## Report

Full report: `<cycle>/reports/fix.md`, with each finding's outcome, each check's command and exit
code, the final figures of each changed file and of each route taken from `word-counts.md` as they
stand after your last change, and **Searches not found or unclear**. Return: your status, your
commits, a one-line check result naming what failed or did not run, and the report's path.
