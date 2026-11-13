# Handoff — review of the whole change

You review the whole change of a the-way task cycle (`implement-task`) as an agent that did not make it.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no answer you
get is that person's approval.

- Method: `task-cycle/review/SKILL.md`, read whole from the worktree below; it names `whole_change.md`,
  which you read and follow as it says. Read any other file it names only when the step that names it comes.
- Worktree (your working directory; read-only for you):
  `the root of the task's worktree`
- Range: base `fca8491` (`foundations`) to head `2c27260` on `task/close-decision-pending-templates`.
  One execution route: one author without a plan, one commit; no slices, no slice reviews, no plan, no spec.
- Frozen task, read it whole:
  `docs/task-cycles/close-decision-pending-templates/task.md`
- The author's report, to read:
  `docs/task-cycles/close-decision-pending-templates/reports/author-report.md`
- Your report, written to:
  `docs/task-cycles/close-decision-pending-templates/reports/whole-review-report.md`
  Its first line is `PASS <sha>`, `FAIL <sha>` or `questions`, as the method gives.

## Answers of the start

- Trust boundary: no. Irreversible operation: no. No open design choice, no reserved choice, no settlement to
  record, no foundation entry written; `foundations/decisions.md` must be unchanged.
- The task moved no pin.

## What the task gives the review to judge

- The task's *To do* item 1 says: "Każdy cytat jest sprawdzony w `foundations/decisions.md` przed wpisaniem; przy
  S4, S5, S7, S10 i S11 raport ma średnią pewność, więc przegląd zmiany potwierdza cytat albo zamienia go na
  zwykły tekst." So for each citation the change writes, and in particular S4, S5, S7, S10 and S11, check the
  quoted decision entry whole and judge whether it supports the sentence it is attached to.
- The author's report names places where it departed from the task's table (S11 without WAY-44, S7 without
  WAY-73) and a place it flagged as its own inference (S3, S4, S9, item 5). Judge each against the task and
  the decision text; the author's recommendation binds you to nothing.
- Every `TODO — decision pending` line except S26 and S28 is gone, and the sense of a rule changes only where
  the task says so (S5's ending; items 2–9 of *To do*; S20–S25, S27 of *Questions to settle*).

## Gaps the author's report states and the orchestrator carries to you

The author left unread, as its report says: `elements/common/rules.md` (it defines the bare `TODO` and `none`
rules), the glossary entries (headings only), `elements/common/projected_mode.md`, the templates' `examples.md`
files, and the entries WAY-02, WAY-17, WAY-65, WAY-80 and WAY-82, which it cites on reflowed lines. Read those
that bear on your judgment of the changed sentences.

## The checks

The orchestrator runs the product's gate on the reviewed change; you do not run `gate/run_tests.py` whole. You may
run the foundation check and focused checks.
