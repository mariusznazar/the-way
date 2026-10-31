# Review of the whole change — maintain-testing-guidelines in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator; the human
reviews the request. You made none of this change. You grade and scope alone.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape`, branch
  `task/testing-skill-shape`. Read only: change nothing but your report.
- Read every file of the-way from this worktree, by its path.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it, for the review of the whole change. Read a
file it names when the step or variant that names it comes. Write findings also by
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\playbook_code_review.md`, where it does
not conflict with the method.

## What you review

- Range: `00c0a747272a9a179b7a855f256daff985ea2ee1..5dc4b3b` (three commits: 1c66173, d024d56,
  5dc4b3b). The message of 1c66173 uses identifiers renumbered by 5dc4b3b; the tree at the head
  stands.
- Frozen task, whole: `.runs/task-cycles/testing-skill-shape/task.md`, accepted 2026-10-31. No spec,
  no plan; one author, so there are no slices.
- Author's reports: `.runs/task-cycles/testing-skill-shape/reports/author.md` and
  `.runs/task-cycles/testing-skill-shape/reports/author-repair.md`.
- Materials the request will carry, which are part of To do 7 and of this review:
  `.runs/task-cycles/testing-skill-shape/reports/assessment.md` and
  `.runs/task-cycles/testing-skill-shape/reports/word-counts.md`.
- The author's helpers lie in `.runs/task-cycles/testing-skill-shape/tools/`, with
  `reports/sentence-diff.txt`; do not rest on them where you can check for yourself.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Guidelines selection: empty (task question 10). Select and read your own foundation
by "Reading the foundation" in `elements/common/way_of_working.md`, for the parts
`product-guidelines`, `instruction-files` and `decisions`, and the task's *Decisions in play* whole.
The author's report states which of the foundation it read and which it did not.

## Rules the orchestrator set

These are the cycle's answers to what the task leaves open; judge the change against them:

- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. A remove or a
  reword that changes a rule's meaning stands as a proposal and is not applied (task To do 7; series
  decision).
- Row 1 of *Settlements to record* is an edit of WAY-256 in place, by
  `elements/decisions/skill/decide_entry.md:9-10` and WAY-30; question 8 rejects a first-step
  exception and rules nothing on that row. Rows 2 and 3 are entries of their own.
- Word counts: as `wc -w` counts them; "before" at 00c0a74; a file read twice in "before" counts
  twice; a file a counted file sends the session to on the route counts in both states; the
  product's own files are left out; each route has the three figures of question 6.

## Coverage to report

Check independently, and say what you ran with its command and exit code:

- each item of the task's *To do*, each acceptance criterion and each row of *Settlements to
  record*;
- every quote of `assessment.md` against the base, its line ranges, and that each nonblank line of
  the base `SKILL.md` stands in exactly one row;
- each route's file list and sum in `word-counts.md`, recomputed;
- that no rule of the base was lost or changed meaning, by your own comparison of the base with the
  rebuilt files;
- the walk the acceptance criteria require: go through each of the six routes by hand, from
  `SKILL.md` to the file of the last step, as an agent that reached `SKILL.md` by its path without
  the entry point, and name for each route the files it reads, in order, and any rule of the base it
  does not reach. Presence of a named text is not the test; the order and the condition of each
  pointer are.

Do not run the whole gate; its run is the orchestrator's.

## Report

Full report: `.runs/task-cycles/testing-skill-shape/reports/review.md`, its first line `PASS <sha>`
or `FAIL <sha>` or `questions`, as the method gives. Return: that first line, a one-line check
result naming what failed or did not run, and the report's path.
