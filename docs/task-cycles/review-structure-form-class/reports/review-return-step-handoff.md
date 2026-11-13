# Handoff — the review of the return step's commit, `review-structure-form-class`

## Delegation

You review, as an agent that did not make it, the commit of the return step of one the-way task cycle. The orchestrator of the cycle is the one
you ask; no human answers during the cycle. You change nothing.

## Where

- Worktree (read-only for you): `the worktree's root`
- Range to review: `c6af26a..b596eec` (one commit on `task/review-structure-form-class`; one file, `product-guidelines/coding/template.md`).
  Confirm `git rev-parse HEAD` is `b596eec`.
- The return step's report: `docs/task-cycles/review-structure-form-class/reports/return-step-author-report.md`.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-return-step-report.md`; its first line is
  `PASS b596eec`, `FAIL b596eec` or `questions`.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it for "the return step's commits": review them as section 2 gives, against the task and the foundation
entries the return step writes or corrects.

## What is reviewed

- The frozen task: `docs/task-cycles/review-structure-form-class/task.md` (Polish). The return step changed no entry; it corrected one sentence of
  the template of coding guidelines so that the order of the required rules matches the rule of size WAY-355 puts between the six rules on failures and
  logs (WAY-271) and the product's further rules, and re-wrapped the bullet of the rule of size. Judge whether the corrected sentence is true against
  WAY-355, WAY-271 (its *Verification* says "the product's further rules follow them" and stays), the template's other bullets, and whether the re-wrap changed
  any word. Entries to read whole: WAY-355, WAY-271, WAY-278. The earlier review of the whole change and of its fix are done (`reports/review-whole-change-report.md`,
  `reports/review-fix-report.md`); do not repeat them.
- Trust boundary: no. Irreversible operation: no. Parts touched: `product-guidelines`.

## Boundaries

- Read-only. Run `python -B elements/common/foundation_check.py` and `python -B task-cycle/private_paths_check.py product-guidelines/coding/template.md`, each with
  command and exit code; do not run the whole gate. Your report holds **Unread material** and **Searches not found or unclear** (each `none` where there is
  nothing), and each finding graded as the skill gives, marked within or outside the task. A Minor finding here is not fixed in this cycle; it goes to the
  request's list. Return the first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result and the report path.
