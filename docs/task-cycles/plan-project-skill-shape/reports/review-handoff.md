# Review of the whole change — plan-project in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator; the human
reviews the request. You made none of this change. You grade and scope alone.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape`, branch
  `task/plan-project-skill-shape`. Read only: change nothing but your report. The orchestrator runs
  the gate in this worktree beside you; it writes no tracked file.
- Read every file of the-way from this worktree, by its path.
- The cycle's directory is
  `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/.runs/task-cycles/plan-project-skill-shape/`,
  called `<cycle>` below.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it, for the review of the whole change. Read a
file it names when the step or variant that names it comes. Write findings also by
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\playbook_code_review.md`, where it does
not conflict with the method.

## What you review

- Range: `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092..db3845c` (one commit).
- Frozen task, whole: `<cycle>/task.md`, created 2026-11-01. No spec, no plan; one author, so there
  are no slices.
- Author's report: `<cycle>/reports/author.md`, its handoff `<cycle>/reports/author-handoff.md`. The
  report says which of the foundation it read whole and which it did not.
- Materials the request will carry, which are part of To do 7, To do 8, To do 9 and of this review:
  `<cycle>/reports/assessment.md` and `<cycle>/reports/word-counts.md`.
- The author's helpers lie in `<cycle>/tools/`, with `<cycle>/reports/sentence_diff.txt`; do not
  rest on them where you can check for yourself.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Guidelines selection: empty (task question 7). Select and read your own foundation by
"Reading the foundation" in `elements/common/way_of_working.md`, for the part `project-level`. The
task's *Decisions in play* quote some decisions in part: read each of those decisions whole in the
log, and each decision the moved text cites. State which you read whole and which you did not.

## Rules the orchestrator set

These are the cycle's answers to what the task leaves open; judge the change against them:

- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings, the pointer of
  To do 5 and the sentence of To do 4. A remove, or a reword that changes a rule's meaning, stands
  as a proposal and is not applied.
- The task carries no row of *Settlements to record*; the change writes no foundation entry.
- Word counts: as `wc -w` counts them; "before" at 2f51e6c; of a file read by sections, the sections
  read; the definition, the plan and the product's files are left out; each route has the two
  figures of task question 4, route 5 in its two versions.

## Coverage to report

Check independently, and say what you ran with its command and exit code:

- each item of the task's *To do* and each acceptance criterion;
- every quote of `assessment.md` against the base, its line ranges, that each nonblank line of the
  base `SKILL.md` stands in exactly one row, and each row's stated new place against the place the
  fragment really stands;
- each route's file list and sum in `word-counts.md`, recomputed from the files;
- that no rule of the base was lost or changed meaning, by your own comparison of the base with the
  rebuilt files, each reworded condition of a mode, variant or pointer compared with the base by
  what it selects, and for each new sentence what it switches off;
- the walk the acceptance criteria require: go by hand through the files of routes 2, 3, 4, 5 and 7
  of task question 4, from `SKILL.md` to the file of the last step, as an agent that reached
  `SKILL.md` by its path without the entry point, and write for each route what stays and what falls
  away, and any rule of the base it does not reach. Presence of a named text is not the test; the
  order and the condition of each pointer are.

Do not run the whole gate; its run is the orchestrator's.

## Report

Full report: `<cycle>/reports/review.md`, its first line `PASS <sha>` or `FAIL <sha>` or
`questions`, as the method gives. Return: that first line, a one-line check result naming what
failed or did not run, and the report's path.
