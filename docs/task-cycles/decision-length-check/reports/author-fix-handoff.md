# Handoff — the fix of a review's findings

You are the one author, resumed for the fix of the findings of the review of the whole change. The
person who requested this cycle delegated intermediate choices to the orchestrator; no answer here
is that person's approval.

- Worktree and branch as before: the task's worktree,
  `task/decision-length-check`. The reviewed head is `e8b76178`; the fix's range runs from it.
- Your method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read
  `task-cycle/change/fix.md` for it, as the variant's row gives.
- The findings file: `.runs/task-cycles/decision-length-check/reports/review-whole-fix-findings.md`
  (the reviewer's words: one blocking finding, marked `Contradiction: yes`, and four Minor findings
  within the task, all of which are fixed in this one fix). Read it whole. You may read the reviewer's
  report `.runs/task-cycles/decision-length-check/reports/review-whole-report.md` for the evidence
  behind a finding, and for nothing else of the record.
- Not yours to fix: finding 6 of that report (outside the task's scope), and anything else the
  findings file does not name.
- Finding 5 changes an entry of the part map (`foundations/part_map.md`, part `elements-common`):
  write it as the skill of that element gives, read from `elements/part-map/skill/SKILL.md`, adding
  the second module to the sentence the way the earlier module stands in it; make no other change
  to the part map.
- Finding 1 repeats an entry the change writes: bring `README.md` and `agent-instructions/README.md`
  in line with the second paragraph of WAY-05 as it stands (`foundations/decisions.md`), so that the
  qualification "that nothing holds" does not attach to the length error, and the different division
  into paragraphs counts, as WAY-05 says. If you hold a finding wrong, answer with evidence in your
  report instead of changing the file.
- Finding 4: either restore the escapes in `QUOTED` as the base had them (and say the move is then
  unchanged), or keep the characters and say so in the report; the choice is yours, with the reason.
- Your directory for working copies: `.runs/author-fix/`; remove it before you return. Do not run
  the product's full gate. Run again the checks the fix affects (`elements/common`,
  `elements/part-map`, `agent-instructions`, `product-guidelines`, the check of the foundation, the
  linter and the formatter) with command and exit code each.
- Commit by path, in English, on the task branch; leave the worktree clean.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-fix-report.md`, with its
  status, commits, checks, own-work check, **Unread material**, **Searches not found or unclear**
  and working copies, as before.
