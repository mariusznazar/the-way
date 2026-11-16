# Handoff - review of the fix of the review's findings

Same delegation, worktree, branch, rules, method (`task-cycle/review/SKILL.md`) and report form as `reports/review-whole-handoff.md`; your working-copies directory is `.runs/review-fix/` (remove it before you return). Report: `reports/review-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`.

You review the fix once. The findings file the fix was given is `reports/review-whole-findings.md` (your own words from `reports/review-whole-report.md`: blocking I-1 and I-2, Minor M-1).
- Range of the fix: from the reviewed head `34db2685148207b901f8a19c2629b0e14af04c91` to `059b891f` (one commit; files `foundations/decisions.md` and `task-cycle/skill/SKILL.md`). Read the full diff of the range.
- The fix report: `reports/author-fix-report.md`. Its choice on I-2: earlier conversion rows stay as written and a reader follows the rows one after the other (the other way out you named, rewriting the right side only, was rejected); WAY-403 was edited in the same commit to match.
- Judge: whether each finding is fixed; whether the new count check of step 3 holds when old and new ranges overlap and catches a missed reference; whether WAY-403 and the skill agree with each other and with the frozen task (`task.md`, To do 2 and 3, row 2, question 2); whether the fix introduced anything new. Only a new Critical or Important finding in the fix fails this review; a Minor finding that remains goes to the request's list.
- The author ran, all exit 0: `python -B reports/author-fix-passcheck.py`, `python -B elements/common/foundation_check.py --skip-test-citations` (0 errors), `python -B gate/run_tests.py` on `task-cycle` (534), `product-guidelines` (14), `elements/common` (257). Nobody ran the product's full gate (CI's); do not run it.
- Keep your working-copies rule: the paragraph "Working copies" of `reports/review-whole-handoff.md` holds.
