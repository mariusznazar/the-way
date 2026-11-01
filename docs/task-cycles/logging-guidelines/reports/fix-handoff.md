# Handoff — fix of the review's findings

You are the one author, resumed. Your stage is **the fix of a review's findings**, under
`task-cycle/change/SKILL.md`: read the row of that variant and what it names.

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/logging-guidelines`, branch
  `task/logging-guidelines`, reviewed head `1740c02`. No upstream is set; do not push.
- Findings file, one blocking finding: `.runs/task-cycles/logging-guidelines/reports/whole-review-findings.md`.
- Your report: `.runs/task-cycles/logging-guidelines/reports/fix.md`, ignored by Git.

The review's Minor findings are not fixed in this cycle: they go to the request for the human, so
touch what the finding needs and nothing else. Where the fix reaches the spec's reading, the change
is what binds: the spec stays as it passed its review.

Run the affected checks again, each with its command and exit code, taken not through a pipe: at
least `python -B elements/common/foundation_check.py .`. Do not run the full gate. Commit by path,
message in English in the form the repository's recent commits use, and leave a clean tree.

The restriction stands in the task's wording: apart from that document, read no note and no
repository of any product.

Where the fix changes the meaning of WAY-275, update its sentence for the request in your report.
Return only your status, your commits, a one-line check result naming what failed or did not run,
and the report's path.
