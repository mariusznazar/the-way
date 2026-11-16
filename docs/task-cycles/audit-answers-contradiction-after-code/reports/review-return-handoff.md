# Handoff to the reviewer of the return step

You are a fresh reviewer: you did not make the change and wrote no earlier review of it. Ask the human nothing;
a question goes to the orchestrator in your report as `questions`.

- Worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), the review of the return step's commits, as its
  section 1 and 2 give it: against the task and the foundation entries the return step writes or corrects.
- Range: base `47a47fecbeec3957b13bf7b34eb120f5b035e0b1` to head `d3068ed` (`git rev-parse d3068ed`): one
  commit, five files — `foundations/decisions.md`, `process-audit/SKILL.md`, `process-audit/audit_count.py`,
  `process-audit/record_items.py` (docstrings only, the author states no behaviour changed: verify it) and
  `task-cycle/record_template.md`.
- The author's report of the return step (claims to verify):
  `docs/task-cycles/audit-answers-contradiction-after-code/reports/author-return-report.md`.
- The frozen task: `docs/task-cycles/audit-answers-contradiction-after-code/task.md` — read it whole; its *To do*
  3, 4, 5 and 6, *Questions to settle* 1 to 5 and the four rows of *Settlements to record* are what the corrected
  entries carry. The entries corrected: WAY-403 (row 1) and WAY-404 (row 4, marked `the cycle's` for its entries
  form). The return step changed their binding sentences and *Verification*; judge each changed sentence against
  its row, its question and the final code (`process-audit/record_items.py` at `d3068ed`), and whether a sentence
  now says more than the row and the human's accepted answers give (WAY-263 grades a departure of a change from
  an entry it writes as Important; the human accepted the behaviour of the corrections in the answer recorded in
  `docs/task-cycles/audit-answers-contradiction-after-code/reports/correction-1-remarks.md`).
- Trust boundary: yes (`process-audit/record_items.py`); the change here is docstrings, check that. Irreversible
  operation: no.
- Select the foundation entries you need for your judgment, read each whole; focused checks only
  (`python -B elements/common/foundation_check.py` without `--skip-test-citations`, `python -B gate/run_tests.py
  process-audit`); **do not run the full gate**. Your directory for working copies: `.runs/review-return/`; your
  report: `docs/task-cycles/audit-answers-contradiction-after-code/reports/review-return-report.md`.

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

First line `PASS <sha>` or `FAIL <sha>`; graded findings with places; checks with command and exit code;
**Unread material**; **Searches not found or unclear**; the line on your working copies. Return the first line,
a one-line check result and the path.
