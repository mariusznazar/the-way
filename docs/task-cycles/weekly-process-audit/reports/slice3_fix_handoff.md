# Handoff — fix of the findings of the review of slice 3 (`make-change`: "the fix of a review's findings")

You are the executor of slice 3, resumed. The review of your slice (range `876710c..9285a74`) returned FAIL with three blocking
findings. Read `task-cycle/change/fix.md` whole (the method's variant for a fix), then the findings file:
`docs/task-cycles/weekly-process-audit/reports\review_slice3_findings.md` — the reviewer's words; the full review is `docs/task-cycles/weekly-process-audit/reports\review_slice3_report.md`.

- Fix the three blocking findings (the crafted header line / continuation, the backslash before a bar in a table cell, the
  out-of-range committer date). Add a test for each that fails on the head `9285a74` for the reason the finding names, then passes.
  The three Minor findings and the lines under Declined to judge are not yours to fix (they go to the request's list), except
  where fixing a blocking finding touches the same line.
- Where you hold a finding wrong, answer with evidence in your report; the reviewer judges it.
- Run the affected checks again: `python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py elements/part-map`,
  `python -B elements/common/foundation_check.py`, `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`;
  give each as command and exit code.
- Commit with `git add <paths>`, messages in English. The fix's range starts at `9285a74`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice3_fix_report.md`; return status, commits, check line, questions, concerns, reaches, **Unread
  material** and **Searches not found or unclear**, and the own-work check, as `make-change` requires.
