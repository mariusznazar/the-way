# Handoff — review of the whole change

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator
(`implement-task`). You review as an agent that did not make the change; you are read-only. Do not ask
the human; questions go to the orchestrator in your report.

## Where and what

- Worktree (your working directory): `the root of the task's worktree (the repository root)`
- Branch `task/invariant-method-on-finished-change`; range to review: `46bba355e51bc671a4af604e11757d91574949b6..e3fcc20` (two commits, `9d499d0` and `e3fcc20`), 8 files, +178/−26.
- The repository is the-way itself; no `.the-way` submodule, the pin did not move. The route is one
  author without a plan and without a spec; so there is no slice with a review of its own — you judge
  the whole change.
- Method: read `task-cycle/review/SKILL.md` in full if it exists, otherwise the file the entry point
  `.claude/skills/the-way-review-change/SKILL.md` names, and follow it; read files it names only
  when the step or variant that names them comes. Variant: the whole change.
- Report: write it to `.runs/task-cycles/invariant-method-on-finished-change/reports/review-whole-report.md`
  as your method gives it; its first line is `PASS <sha>` or `FAIL <sha>` (or `questions`).

## What to review against

- The frozen task: `.runs/task-cycles/invariant-method-on-finished-change/task.md` (read whole; Polish).
  Check every *To do* item (1–4), the four questions as answers (the cycle must not reopen them), the
  three rows of *Settlements to record* (row 1 decision, row 2 decision, row 3 invariant — each
  written whole, its meaning the row's), and source fidelity (the entries must not add decisions the
  task does not carry; the weak points the task names must be where the task says).
- The author's report: `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`.
  It lists the author's choices (switch name `--skip-test-citations`, WAY-321 as a decision of its own,
  invariant `test-method-citation` derives from WAY-321 only, *Rejected* of WAY-61 gaining the
  planning-skill way, two one-clause edits of `README.md` and `installation/README.md` outside the
  task's list, part map unchanged). Judge each: the reviewer alone grades and scopes.
- Answers of the two questions at start: no trust boundary touched (`decisions`, `invariants`,
  `elements-common` parts have `none`); no irreversible operation.
- The orchestrator's gate run is its own (it runs after your review); the base gate was green
  (826 tests). You may run focused checks, not the full gate.
- Selection of foundation and guidelines is yours (you select by the parts of the change). The-way
  has no `guidelines/` directory; the task's question 3 settles that this does not block the change.

## Things the orchestrator asks you specifically to verify (not a limit of your review)

1. The new WAY-61 wording agrees in its sentence, complies/violates examples and rationale, and no
   other entry or template of the foundation still states the old rule (search the whole foundation
   once, WAY-33); question 4 of the task names three places that must stay unchanged — check they did.
2. The invariant `test-method-citation` is complete by the invariants template and
   `elements/common/rules.md`, its identifier is cited by a test that really exercises the check
   (`test_the_way_foundation_passes`), and the decision's *Verification* names it as the template
   requires.
3. The script change: the check really uses "tracked by git, not Markdown", reports per invariant, the
   switch skips only this report, usage errors exit 2, existing behaviour unchanged. Run
   `python -B gate/run_tests.py elements/common` and `python -B elements/common/foundation_check.py`.
4. Whether the one-clause edits of `README.md` and `installation/README.md` are required by the task's
   return-step duty (entries true to the code) or go beyond the task.
5. Language and form of the entries: English, no private paths or personal data
   (`python -B task-cycle/private_paths_check.py <file>` for the changed files).

Grade by `review-change`'s own scale and say, for each finding, whether it is within the task's
scope. This change has no plan, so no finding names a slice.
