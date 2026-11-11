# Handoff — the fix of a review's findings (`make-change`, variant "the fix of a review's findings")

Same worktree and branch (`task/posix-class-not-a-link`), the reviewed head is `8fa6bac`. Read the
findings in `.runs/task-cycles/posix-class-not-a-link/reports/fix_findings.md` and fix them in one
commit (explicit paths, English message). Read `task-cycle/change/fix.md` as the method names it.
Run the affected checks again (`python -B elements/common/foundation_check.py`,
`python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`) and answer with
evidence a finding you hold wrong. Report path: `reports/fix_report.md`, with **Unread material** and
**Searches not found or unclear**, commands and exit codes. No full gate.
