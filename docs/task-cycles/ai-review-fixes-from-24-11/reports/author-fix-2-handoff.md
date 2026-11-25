# Handoff — the fix of the findings of the second review of the whole change, `make-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request.

## Where you work

- The same worktree and branch: `the task's worktree` (branch `task/ai-review-fixes-from-24-11`). The reviewed head is `2dca6873`; your fix range runs from it. Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-fix-2-report.md`, with the same sections as your earlier reports (**Unread material**, **Searches not found or unclear**, each check with command and exit code, your own-work check). The report file is the input of the cycle's scripts.

## Your stage and variant

"The fix of a review's findings", of `task-cycle/change/SKILL.md`. The findings file: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-findings.md`; read it whole. It holds two blocking findings (I-1 and I-2, both marked `Contradiction: yes`) and two Minor findings within the task (M-1, M-2), which are fixed with them. The probe the reviewer ran is beside it: `reports/review-whole-2-probe-linked.py` with its output `reports/review-whole-2-probe-linked-output.txt`; the report of the review is `reports/review-whole-2-report.md` (yours to read for this fix). Answer with evidence any finding you hold wrong; do not fix it then.

The orchestrator's rulings for the fix, binding for it:

- **I-1** (code): key the decisions' texts in the new check by the value of the number (`int`), as `base_paragraphs` and `check_held` do, not by the zero-padded label; add a test whose log writes a number otherwise than as two digits (the reviewer's `ABC-1` or `ABC-007`) and in which the decision's rationale alone changes, so that it expects the error and fails before the fix. Seen failing before the fix: run it before you change the code and report the command and exit code.
- **I-2** (entries): in WAY-12's *Rejected* keep only the option that is the way not chosen of Question 2 (the field that carries the link); drop "an error for every such invariant …" and the option of leaving the link to the skill with no check. In WAY-30's *Rejected* keep only the way of Question 1 that is a way of the product's rule ("approval before the code, as for every change to a decision"); drop "the approval left to the merge with no sentence saying so …", which WAY-134 reads as a way of how an answer is recorded. Make the edits as edits in place through `record-decision` (its `SKILL.md` is `elements/decisions/skill/SKILL.md`), change no binding sentence, and keep WAY-12's *Verification* tests clause and WAY-30's pair of examples as they are. If dropping a *Rejected* option leaves a *Rationale* sentence that now argues against the dropped option, correct that sentence so that the entry still reads true.
- **M-1** (code): skip an invariant whose heading carries a version (`/`), as `invariant_entries` does; add a test for it.
- **M-2** (entry): WAY-30's new sentence reads "asks that human no question about it", or the same meaning in words you choose with the paragraph's three-sentence limit (WAY-05) kept; the entry's English and the meaning of row 1 stay.

`foundation_check.py` stands at 1193 lines against the limit of 1200 (WAY-385); the fix stays under it (a move of code out of the file is not part of this task; if the fix cannot fit, return `returned` with where the size lies, as the method gives). Run the affected checks again: `python -B elements/common/foundation_check.py`, `python -B gate/run_tests.py elements/common`, `python -B gate/run_tests.py agent-instructions`, ruff format and lint of `elements/common` as before. Do not run the full gate. Commit by path (`git add <path> …`), message in English; return status, commits, a one-line check result and the report path.

## Working copies

Only in `.runs/author/`; remove before you return by the full path, and say so in the report.
