# Handoff — review of the whole change

You are a reviewer of a the-way task cycle and made none of this change. The person who requested
the cycle has delegated intermediate choices to the orchestrator, who sends you this; its answers
below are provisional and no human's approval.

## Variant, worktree, method

- Method: `task-cycle/review/SKILL.md`, read whole, and `whole_change.md` beside it when section 1
  of it says (the review of the whole change). You select your own foundation and guidelines.
- Variant: **the whole change**, one author, no plan, no spec, no slices (so no slice had a review
  of its own: nothing to cover by slice).
- Reviewed worktree: `the task's worktree root`
  (branch `task/backlog-line-for-plan-tasks`). Never change it, its index or its branch; run any
  check that needs changed files in a separate worktree of the head commit, in your own scratch
  directory, and delete it after.
- Range: base `52f8164a354ee1a704af0d58add2f3be8e4f0247` to head
  `9eb2bd637697fd5f3cccdb891091110054f9d292` (two commits: `74fbd01`, `9eb2bd6`). Compute the diff
  yourself with `git diff <base>..<head>` and confirm `git rev-parse HEAD` is the head.
- The full test suite is the orchestrator's; do not repeat it. A project-level focused run takes
  about 12 minutes; run only what tells this change from a broken one. The orchestrator has a full
  gate run going in another checkout, so the machine is loaded.

## What is reviewed against

- The frozen task, read whole: `docs/task-cycles/backlog-line-for-plan-tasks/task.md` (in the
  worktree; the original lies in the author's private notes, never quote its path). Review coverage
  of every item of *To do* (1–6), every row of *Settlements to record* (1–5; the decisions are
  written in `foundations/decisions.md`), the decisions of *Decisions in play* (WAY-154, WAY-107,
  WAY-144, WAY-320, WAY-328), and the question the task carries to the cycle (the `🆔` identifier),
  and source fidelity: each *Rejected* the change writes holds only ways the task's *Questions to
  settle* lists under *Not chosen*, with the cost the source gives.
- The author's report, a set of claims to verify, not evidence:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/author-report.md`.
- Answers of the orchestrator: trust boundary — no (no file the part map names as one is in the
  change); irreversible operation — no; open design choice — none; reserved choice — none; the
  task does not move a pin.
- The orchestrator's autonomous choices on the author's questions, recorded as choices for you to
  judge, not as binding: (Q1) how the identifier is derived — the author's final form is in
  `project-level/task_line.md`; (Q2) the author's partial reading of
  `instruction-files/tool_loading.md` and no reading of `judging.md`, `placing.md`, `writing.md`,
  `kind_path_rule.md` (its report, *Unread material*) is accepted as bearing on nothing the author
  judged — judge whether the new file `project-level/task_line.md` and the edited skills break a
  rule of those; (Q3) the author's concerns 1 and 2 (no route where the task place has no rules;
  `product-guidelines/{coding,testing,styleguide}/orchestrated_mode.md` still say "edits only the
  task document and its turn") are passed to you for grading and scoping.
- Three files lie outside the handoff the author got (`project-level/lead/skill/route_changes.md`,
  `project-level/task/template.md`, `project-level/plan/skill/delegated_mode.md`); judge each as
  within the task or not.
- The foundation entry WAY-27 is marked `the cycle's` (the author's correction of a decision that
  the change's `AGENTS.md` wording would otherwise contradict); judge it against WAY-27's own text
  and WAY-263.

## Selection hints (yours remains your own)

Parts touched: `decisions`, `project-level`, `agent-instructions`. Product guidelines: the-way has
no guidelines directory; WAY-328 departs from the coding and testing guidelines for its own code;
no user interface is involved.

## Report

Write the full report to
`docs/task-cycles/backlog-line-for-plan-tasks/reports/whole-review-report.md`
as the method gives it, first line `PASS <head sha>` or `FAIL <head sha>`, including the counts of
decisions read whole and by title, **Declined to judge**, each check with command and exit code,
each reach beyond this dispatch, **Unread material** and **Searches not found or unclear**. Return
the first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result and
the report path.
