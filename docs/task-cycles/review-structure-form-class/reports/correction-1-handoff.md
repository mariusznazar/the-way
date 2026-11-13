# Handoff — correction 1 after review, `review-structure-form-class`

## Delegation

You are the one author of this change, resumed for a correction the human asked for on the open request (https://github.com/mariusznazar/the-way/pull/109).
The orchestrator is the one you ask; no human answers during the cycle. A fresh reviewer reviews your correction once afterwards; the human's remarks
take the place of a findings file.

## Where

- Worktree (work from its root, and nowhere else): `the worktree's root`; branch
  `task/review-structure-form-class`; head `24cbe61` (the tree is the one of `0f35395`; the record's copy was added and removed above it). The target branch
  has nothing new. Your correction's range starts at `24cbe61`.
- The human's remarks, word for word: `docs/task-cycles/review-structure-form-class/reports/correction-1-remarks.md`. They bind. Read them whole. Item 1
  asks for a fix in this request; item 2 is not fixed here (the human made a task of it elsewhere and lets it through): do nothing about item 2.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/correction-1-author-report.md`

## Method

Read `task-cycle/change/SKILL.md` in the variant "a correction for the human's remarks" (it names `task-cycle/change/fix.md`; read that file when the variant
comes). Where it names a foundation entry to change, edit it in place (WAY-07; WAY-363 is this branch's own entry, not yet merged).

## What to do

1. Item 1 of the remarks: where the product has no rule of size — one that departed from the rule by a decision with a reason, or one with no coding guidelines
   at all, such as the-way itself under WAY-328 — a finding about the structure of code is always Minor. Say so in section 3 of `task-cycle/review/SKILL.md`
   (next to the sentence on the threshold) and in the binding sentence of WAY-363 (the entry about how a reviewer grades a finding about the structure of code),
   keeping its other sentences; bring the rest of that entry in line (its *Rationale*, *Rejected*, *Verification*, and the way it names WAY-161 and WAY-328 if
   it does), and write into its *Rejected* the way not taken with its price: "graded as any other where there is no rule", with the chance of a blocking
   finding and a round of correction back that the human's request item named. Search the whole foundation and the files of `task-cycle/` and
   `product-guidelines/` once for each sentence that says "below the threshold" or describes this grade (WAY-33; for instance `task-cycle/review/whole_change.md`,
   the entry about what the review of the whole change asks, the entry about the plan, `product-guidelines/coding/template.md`, `settle.md`) and make them agree.
2. Do not widen the correction: no other grade, no other rule. Commit by path, in English, do not push.
3. Run, each with command and exit code: `python -B elements/common/foundation_check.py`, `python -B gate/run_tests.py task-cycle` (and
   `python -B gate/run_tests.py elements/part-map` and `python -B gate/run_tests.py instruction-files` if a file they read changes),
   `python -B task-cycle/private_paths_check.py <file>` on each file you change; do not run the whole gate. Give your own-work check: the requirement most
   likely unmet is that every sentence about this grade now says the same about a product with no rule; show a scan for each sentence you found.
4. Take the return step for this correction's range as well (`task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`): compare the entries the
   correction changes, those it touches and the part map with the files; correct in the same commit what no longer matches; say `none` where nothing does.
5. Report as `make-change` gives for a correction: status, commits, each remark as made or not, checks with command and exit code, the own-work check,
   **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Do not start any next stage.
