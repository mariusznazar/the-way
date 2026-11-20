# Handoff — the fix of the findings of the review of correction 2

You are the one author, resumed for the fix of the blocking finding of the review of correction 2. The
person who requested this cycle delegated intermediate choices to the orchestrator; no answer here is that
person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`; the reviewed head, from which the
  fix's range runs, is `fa5d349e`.
- Method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read
  `task-cycle/change/fix.md`. Because the fix changes the words of WAY-05, do it through the foundation step as
  you did for correction 2 (`task-cycle/skill/foundation_step.md` and the `SKILL.md` of the decisions element).
- The findings: `.runs/task-cycles/decision-length-check/reports/review-correction-2-fix-findings.md` (one
  blocking finding, marked `Contradiction: yes`). Read it whole. You may read the reviewer's report
  `.runs/task-cycles/decision-length-check/reports/review-correction-2-report.md` for the evidence behind it,
  and for nothing else. The two Minor findings of that report (the name of a part in WAY-19 against WAY-05, and
  "for this report alone" in `agent-instructions/README.md`) are **not** yours to fix: they are Minor findings of
  a correction and go to the request's list. Do not change WAY-19.
- What to make: the one statement of item 2 of the remarks
  (`.runs/task-cycles/decision-length-check/reports/correction-2-remarks.md`) in the three places the finding
  names — WAY-05, the template's "Binding sentences", and the template's entry form (the block of the form of
  an entry) — so that they say the same: a further paragraph may also carry a part of the entry's own question,
  each such paragraph standing within the limits of a paragraph, and the number of such paragraphs is not
  limited by any of the three (the human chose no limit on the number of paragraphs; the 600 words of the whole
  entry keep the length). Keep WAY-05 within all three limits (count it with the script) and restore none of the
  ways not chosen. If you hold the finding wrong, answer with evidence in your report instead of changing the
  files.
- Checks to run again, each with command and exit code, as the fix affects them: `python -B gate/run_tests.py
  elements/common`, `agent-instructions`, `product-guidelines`; `python -B elements/common/foundation_check.py`
  (exit 0, `0 errors`); the linter only if a Python file changes. Do not run the product's full gate. If a test
  that holds a sentence of WAY-05 by a line `decision:` quotes text you reword, keep its quotation true.
- Commit by path, in English; leave the worktree clean; touch no file of `.runs/task-cycles/` and make none
  outside the worktree. Your directory for working copies: `.runs/author-correction-2-fix/`; remove it before
  you return.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-correction-2-fix-report.md`, with its
  status, commits, checks, own-work check, the entries you changed with their marks, **Unread material**,
  **Searches not found or unclear** and working copies.
