# Handoff — review of the whole change, `find-foundation-entries` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle; the orchestrator dispatches
this review. You did not make the change. You ask no human; questions go back to the orchestrator
(first line `questions`).

## Where you work

- Process root and worktree: `C:\Storage\repos\the-way\.runs\worktrees\find-foundation-entries-shape`
  (branch `task/find-foundation-entries-shape`). Read every file from it. You are read-only: write
  only your report.
- Record directory (ignored by git): `.runs/task-cycles/find-foundation-entries-shape/`.

## Stage

Your method: `task-cycle/review/SKILL.md`, read whole; its section for the review of the whole
change is `whole_change.md` beside it — read it when the step names it. Your review: **the whole
change**, one author without a plan, no spec, no slices (no slice had a review of its own).

Range: base `f447bb62ce4f8d4a4badb1b283a10f62651d65d7` to head
`a15de09` (one commit, `docs: split find-foundation-entries into SKILL.md and files beside it by
step and variant (WAY-256)`). Compute the diff yourself: `git diff f447bb6..a15de09`.

## What is reviewed against

- The frozen task: `.runs/task-cycles/find-foundation-entries-shape/task.md` — read whole; it is the
  requirement. No spec and no plan exist. The task carries no row of *Settlements to record* and no
  projected entry; the foundation step had nothing to write.
- The author's report: `.runs/task-cycles/find-foundation-entries-shape/reports/author.md` — a
  set of claims to verify, not evidence. Beside it in `reports/`: `assessment.md` (the assessment
  table and four proposals), `word-counts.md`, `verify_counts.py`, `route_check.py`.
- The base text of the skill: `git show f447bb6:elements/common/skill/SKILL.md` (identical to the
  task's base `dfd50e5`).

## Answers of the cycle's step 4

- Trust boundary: no (`elements-common`, trust boundary none). Irreversible operation: no.
- The change made no move of a pin, so no checks of one are carried.

## What the task's acceptance criteria ask of you specifically

Besides the criteria of your method:

1. Walk both routes by hand — the task variant and the project-definition variant — from
   `elements/common/skill/SKILL.md` to the file of the last step, as an agent that has the path of
   `SKILL.md` and no entry file would; list what stays and what drops on each.
2. Compare every row of `reports/assessment.md` with the place where its fragment really stands
   after the rebuild, and every nonblank line of the base with exactly one row.
3. For every rewritten conditional or pointer, compare with the base: does it add a route or lose
   one? For every new sentence: what does it switch off? A check that sentences are present is not
   enough.
4. The task variant keeps what the base reached by "show it whole as above"
   (`elements/common/skill/SKILL.md:80–81` on the base against `:72–74`).
5. Each pointer says whether the agent only reads the file or carries out its step, and names the
   step or variant in words an agent reading `SKILL.md` by path recognises; the agent sent by a
   caller recognises its variant by the caller's words (the callers: `project-level/skill/SKILL.md:129–131`,
   `project-level/task/skill/find_settlements.md:4–7`, `project-level/task/skill/orchestrated_mode.md:17`,
   `product-guidelines/{coding,styleguide,testing}/hand_back.md`).
6. Nothing changed outside `elements/common/skill/`; the skill's `description` and Python are as
   they were.
7. The word counts: recompute them yourself after the last change to a counted file and compare
   with every number the request will state (`word-counts.md` and `author.md`). The author notes
   one figure of the task that does not match the file: 424 words for the task template's section
   "Settlements to record" with its rule, against 405 counted; say which reading is right.
8. Foundation entries to check the change against are yours to select (WAY-150) by the parts the
   change touches; the task's *Decisions in play* are WAY-256, 257, 265, 35, 115, 134, 117, 127, 259.

The product's gate is not yours to run (the orchestrator runs it); run focused checks you need,
each with its command and exit code in the report.

## Report

Write the full report to `.runs/task-cycles/find-foundation-entries-shape/reports/review.md` as
your method gives it. Its first line is `PASS <sha>`, `FAIL <sha>` or `questions`. Include
**Searches not found or unclear** (each item or `none`). Return only: the first line, the report
path, a one-line check result naming what failed or did not run, and each blocking finding in one
line.
