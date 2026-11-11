# Handoff — fix of the findings of the review of slice 4 (`make-change`: "the fix of a review's findings")

You are the executor of slice 4, resumed. The review of your slice (range `116f319..269d7be`) returned FAIL with two blocking
findings (Important). Read `task-cycle/change/fix.md` whole, then the findings file `docs/task-cycles/weekly-process-audit/reports\review_slice4_findings.md` (the
reviewer's words; the full review is `docs/task-cycles/weekly-process-audit/reports\review_slice4_report.md`).

- Fix the two blocking findings (the share of fix rounds silently wrong; a cost of 0.000000 where tokens are absent). Add a test for each
  that fails on `269d7be` for the reason the finding names, then passes.
- For finding 1: the rule that the share is given only when it can be told with certainty is the plan's; where the stages of a cycle cannot
  be tied to its fix rounds *reliably*, the share is `unknown` with the reason — never a figure from a coincidence of counts. A wrong
  figure is worse than `unknown`. Choose the narrowest reliable tie you can defend with evidence from the records (the *Events* rows and the
  *Review rounds* line of a record, the stage names of `stages.md`), and say in your report what you chose and why.
- The Minor findings (3–6) and the out-of-scope finding are not yours to fix, except where fixing a blocking finding touches the same line.
- Where you hold a finding wrong, answer with evidence in your report; the reviewer judges it.
- Run the affected checks again, each as command and exit code: `python -B gate/run_tests.py process-audit`,
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`, and the run on this repository with stdin closed (a
  temporary locations file and results directory).
- Commit with `git add <paths>`, messages in English. The fix's range starts at `269d7be`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice4_fix_report.md`; return status, commits, check line, questions, concerns, reaches, **Unread material**
  and **Searches not found or unclear**, and the own-work check.
