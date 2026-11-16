# Handoff to the one author — the fix of the review of correction 1

The review of your correction returned `FAIL b3bd8f4e1b401ab38ccf6e22f2fa96847c508490`
(`reports/review-correction-report.md`). The one blocking finding, R-1, stands in
`reports/review-correction-findings.md`, in the reviewer's words; fix it with `make-change`, variant
"the fix of a review's findings", on the same branch from head `b3bd8f4`. Your directory for working
copies: `.runs/author-correction-fix/`. Your report:
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction-fix-report.md`.
Delegation as before: ask the human nothing, do not run the product's full gate.

- Fix R-1 as the finding gives, or by a way you hold better with its reason: the new predicate in
  `process-audit/record_items.py` must require that the first line under the item be an entry at the
  entries' indent (`base`), so that an entry indented deeper than the next one is no longer dropped; the
  reviewer checked `lines[0][0] == base and` added to the predicate. The reason the reading then gives for
  a first entry at another indent must fit that case — not "a plain line stands beside the entries" where
  the line is an entry; a reason naming lines at another indent than the entries fits both. Add a test with
  the record of the finding and the one with a third entry (`- reason: `reserved choice``), through
  `read_contradiction`, and check that the test `deeper` (a sub-entry under an entry at `base` gives `no`) and the
  earlier tests still stand.
- The Minor findings M-1, M-2, M-3 and the out-of-scope O-1 of that report are **not** to be fixed: the
  cycle carries them to the request's lists. Do not touch the entries of the foundation.
- Run the affected focused checks (`python -B gate/run_tests.py process-audit`, `... task-cycle`,
  `python -B elements/common/foundation_check.py` without `--skip-test-citations`), each with command and
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

As `make-change` gives it for a fix: **Unread material**, **Searches not found or unclear**, the own-work
check, the fix's range from `b3bd8f4`. Return status, commits, a one-line check result and the report's path.
