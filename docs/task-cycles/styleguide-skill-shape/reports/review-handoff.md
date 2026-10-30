# Review of the whole change — maintain-styleguide in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator; the human
reviews the request. You made none of this change. You grade and scope alone.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape`, branch
  `task/styleguide-skill-shape`. Read only: change nothing but your report.
- Read every file of the-way from this worktree, by its path.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it, for the review of the whole change. Read a
file it names when the step or variant that names it comes. Write findings also by
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\playbook_code_review.md`, where it does
not conflict with the method.

## What you review

- Range: `525cde1dd53c474f56ea0ece289cb60e868aa90d..802b56d` (two commits: b63f7cd, 802b56d).
- Frozen task, whole: `.runs/task-cycles/styleguide-skill-shape/task.md`, accepted 2026-10-30. No
  spec, no plan; one author, so there are no slices.
- Author's report: `.runs/task-cycles/styleguide-skill-shape/reports/author.md`.
- Materials the request will carry, which are part of To do 4 and of this review:
  `.runs/task-cycles/styleguide-skill-shape/reports/assessment.md` and
  `.runs/task-cycles/styleguide-skill-shape/reports/word-counts.md`.
- The author's helpers lie in `.runs/task-cycles/styleguide-skill-shape/tools/`, with
  `reports/sentence_diff.txt`; do not rest on them where you can check for yourself.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Guidelines selection: empty (task question 6). The change writes no foundation entry
(*Settlements to record*: none). Select and read your own foundation by "Reading the foundation" in
`elements/common/way_of_working.md`, for the parts `product-guidelines` and `instruction-files`, and
the task's *Decisions in play* whole.

## Rules the orchestrator set for the materials

These are the cycle's answers to what the task leaves open; judge the materials against them:

- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. A remove or a
  reword that changes a rule's meaning stands as a proposal and is not applied (task To do 4; series
  decision, quoted in the task's *Context*).
- Word counts: every read of the route counts, refine-task's own first reading of a file the skill
  makes the session read again included, in both states; a file read twice in "before" counts twice;
  each route has one more figure without those first reads, to set beside the task's estimate of
  about 8850 and 5900 words.
- A file a counted file sends the session to on the route counts in both states.
- "pierwszy styleguide, są ekrany" is counted with a human without a preference, so research and
  audit both run; labelled beside the route.
- The product's own files and foundation entries are left out of both states; stated.
- Words are whitespace-separated, Markdown and frontmatter included; of a file read by sections, the
  sections read.

## Coverage to report

Check independently, and say what you ran with its command and exit code:

- each item of the task's *To do* and each acceptance criterion;
- every quote of `assessment.md` against the base, its line ranges, and that each nonblank line of
  the base `SKILL.md` stands in exactly one row;
- each route's file list and sum in `word-counts.md`, recomputed;
- that the rebuilt text reaches each route: walk the seven routes through the rebuilt files as an
  agent reading `SKILL.md` by its path, without the entry point, and name for each route the files
  it reaches and any rule of the base it does not reach.

Do not run the whole gate; its run is the orchestrator's.

## Report

Full report: `.runs/task-cycles/styleguide-skill-shape/reports/review.md`, its first line
`PASS <sha>` or `FAIL <sha>` or `questions`, as the method gives. Return: that first line, a
one-line check result naming what failed or did not run, and the report's path.
