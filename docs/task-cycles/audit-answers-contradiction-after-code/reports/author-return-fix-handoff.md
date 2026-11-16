# Handoff to the one author — the fix of the review of the return step

The review of your return step returned `FAIL d3068ed09017a0d0807c9e51d580ec3ba8b64589`
(`reports/review-return-report.md`). Its one blocking finding, I-1, stands in
`reports/review-return-findings.md`, in the reviewer's words; fix it with `make-change`, variant "the fix of a
review's findings", on the same branch from head `d3068ed`. Your directory for working copies:
`.runs/author-return-fix/`. Your report:
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-return-fix-report.md`.
Delegation as before: ask the human nothing; do not run the product's full gate.

- Fix I-1 as the reviewer's direction gives, or by a better way with its reason: WAY-405's binding sentence and
  *Verification* (and the docstring of `process-audit/audit_count.py` at the lines the finding names) must
  say what the code does — where the lines under the item are not entries at one indent alone, the whole is read
  as the text of one attempt and gives unknown unless it opens with `reason: ` and one marker and holds no other —
  so that the sentence is no wider than the code (WAY-263). Keep what the other review passed: the sentence's
  start that a test cites by a line `decision:`, the narrowing of WAY-344, the rest of the return step. Change no
  behaviour of the code; check the sentence against `process-audit/record_items.py` and the tests that cite
  WAY-405 (`process-audit/test_record_items.py:142-151`, `:191-195`, `:210-212`).
- The Minor finding M-1 of that report (WAY-404's *Verification* does not say that yes wins over unknown) is **not**
  to be fixed here: the cycle carries it to the request.
- Run `python -B elements/common/foundation_check.py` without `--skip-test-citations`,
  `python -B gate/run_tests.py process-audit` and `python -B gate/run_tests.py task-cycle`, each with command and
  exit code, a command through a pipe included. Commit by path, messages in English.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The report

As `make-change` gives it for a fix: **Unread material**, **Searches not found or unclear**, the own-work check,
the fix's range from `d3068ed`. Return status, commits, a one-line check result and the report's path.
