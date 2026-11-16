# Handoff to the one author — correction 1 for the human's remarks

## What this is

The human answered the request (https://github.com/mariusznazar/the-way/pull/138) through the day advisor.
The remarks bind and stand word for word in
`docs/task-cycles/audit-answers-contradiction-after-code/reports/correction-1-remarks.md` — read them whole.
Method: `task-cycle/change/SKILL.md`, variant "a correction for the human's remarks". Same worktree
(`the root of the task's worktree`) and branch; the code to correct
is at `428cc4553042992c6a9813e7dd0a9ef11f0e2ea1` (the later commits only add and remove the record's
copy); the target branch has not moved. Your directory for working copies: `.runs/author-correction/`.
Your report: `docs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction-report.md`.
Delegation as before: ask the human nothing; do not run the product's full gate.

## What the remarks ask of you (items 1 and 4; items 2 and 3 are the cycle's)

- **Item 1 — the blocking finding I-2** of `reports/review-fix-report.md` (read it whole; its
  *Important* section is the finding to fix). The reviewer's fix: read the entries form only where
  every non-blank line under the item, at the entries' indent and outside fences, is a list entry;
  where a plain line stands beside entries, give `unknown` with the reason for text beside entries
  (as on the item's own line), or read the whole as the one-attempt text, which gives `unknown` for
  two markers and keeps the form "reason on the line under the item, details as a list" that
  `ab2c8c8` read as `yes`. Choose between those two by which keeps every answer that `ab2c8c8` gave
  correctly and gives no wrong `yes` or `no`; name the choice in your report. Add a test for each of
  the two records the finding gives (a plain first attempt under an empty item beside a second entry;
  the one-attempt text with its details as a list), and check crafted input as before (this is the
  trust boundary `process-audit/record_items.py`).
- **Item 4 — the Minor finding N-1** of the same report: the four places that write a second
  discarded attempt (`task-cycle/skill/SKILL.md` two paragraphs, `task-cycle/skill/reserved_return.md`,
  `task-cycle/skill/correction.md`) must say that the earlier attempt is then rewritten as an entry
  too, as `task-cycle/record_template.md` says; the reviewer's wording: "and the earlier attempt
  rewritten as an entry, as the template gives it". Keep WAY-404 in agreement with whatever you
  change; where its sentence has to change for I-2, say so in your report (WAY-404 is marked
  `the cycle's` in the request already for its entries form).

Item 5 of the request (the narrowing of WAY-344) is accepted by the human unless a later reading shows
its route does not hold; do not change it.

## Reading

The files above, whole where you change them; the foundation entries WAY-404, WAY-403, WAY-344 and
the invariants and guidelines you read in your first turn — `guidelines/coding.md`,
`guidelines/coding-measuring-report.md`, `guidelines/testing.md`.

## Checks

Run the affected focused checks (`python -B gate/run_tests.py process-audit`,
`python -B gate/run_tests.py task-cycle`, and the directory of any other file you change,
`python -B elements/common/foundation_check.py` without `--skip-test-citations`), each with its
command and exit code, a command through a pipe included. Commit by path, messages in English.

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

As `make-change` gives it for a correction, with **Unread material**, **Searches not found or
unclear**, the own-work check and the correction's range from `428cc4553042992c6a9813e7dd0a9ef11f0e2ea1`.
Return its status, commits, a one-line check result and the report's path.
