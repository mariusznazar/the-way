# Review of the whole change — maintain-coding-guidelines in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator; the human
reviews the request. You made none of this change. You grade and scope alone.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape`, branch
  `task/coding-skill-shape`. Read only: change nothing but your report. The orchestrator runs the
  gate in this worktree beside you; it writes no tracked file.
- Read every file of the-way from this worktree, by its path.
- The cycle's directory is `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/`, called
  `<cycle>` below.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it, for the review of the whole change. Read a
file it names when the step or variant that names it comes. Write findings also by
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\playbook_code_review.md`, where it does
not conflict with the method.

## What you review

- Range: `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a..097123e` (one commit).
- Frozen task, whole: `<cycle>/task.md`, accepted 2026-10-31. No spec, no plan; one author, so there
  are no slices.
- Author's report: `<cycle>/reports/author.md`. Its *Reaches beyond this handoff* says which of the
  foundation it read whole and which it did not, and its *Searches not found or unclear* names what
  it found unclear; its handoff is `<cycle>/reports/author-handoff.md`.
- Materials the request will carry, which are part of To do 6, To do 7 and of this review:
  `<cycle>/reports/assessment.md` and `<cycle>/reports/word-counts.md`.
- The author's helpers lie in `<cycle>/tools/`, with `<cycle>/reports/sentences.txt`; do not rest on
  them where you can check for yourself.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Guidelines selection: empty (task question 8). Select and read your own foundation by
"Reading the foundation" in `elements/common/way_of_working.md`, for the parts `product-guidelines`
and `decisions`. The task's *Decisions in play* quote some decisions in part: read each of those
decisions whole in the log, and each decision the moved text cites. State which you read whole and
which you did not.

## Rules the orchestrator set

These are the cycle's answers to what the task leaves open; judge the change against them:

- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. Outside To do
  9–13, a remove or a reword that changes a rule's meaning stands as a proposal and is not applied.
- Rows 1 and 2 of *Settlements to record* are one edit of WAY-216 in place, and row 3 an edit of
  WAY-266 in place; no new entry. The link `narrows WAY-251` stands on WAY-216 only.
- The rule of To do 10 holds on the fifth mode only; the contradiction To do 8 names stays a
  proposal.
- Word counts: as `wc -w` counts them; "before" at f86fd71; a file read twice in "before" counts
  twice; the files beside the critique count where the route reaches them; the product's own files
  are left out; each of the seven routes has the three figures of task question 4.

## Coverage to report

Check independently, and say what you ran with its command and exit code:

- each item of the task's *To do*, each acceptance criterion and each row of *Settlements to
  record*;
- every quote of `assessment.md` against the base, its line ranges, that each nonblank line of the
  base `SKILL.md` stands in exactly one row, and each row's stated new place against the place the
  fragment really stands (the task's acceptance criterion on the walk);
- each route's file list and sum in `word-counts.md`, recomputed;
- that no rule of the base was lost or changed meaning, by your own comparison of the base with the
  rebuilt files, the reworded conditions of modes and pointers compared by what they select;
- the walk the acceptance criteria require: go through each of the seven routes by hand, from
  `SKILL.md` to the file of the last step, as an agent that reached `SKILL.md` by its path without
  the entry point, and name for each route the files it reads, in order, and any rule of the base it
  does not reach. Presence of a named text is not the test; the order and the condition of each
  pointer are.

Do not run the whole gate; its run is the orchestrator's.

## Report

Full report: `<cycle>/reports/review.md`, its first line `PASS <sha>` or `FAIL <sha>` or
`questions`, as the method gives. Return: that first line, a one-line check result naming what
failed or did not run, and the report's path.
