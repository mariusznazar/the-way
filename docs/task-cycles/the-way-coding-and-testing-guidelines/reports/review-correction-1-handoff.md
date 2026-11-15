# Handoff — reviewer of correction 1

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here is that person's approval. You review a correction as an agent that did not make it.

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. You change nothing in it.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant **a later change to an open request (a correction)**: the human's remarks stand in place of a findings file. Read it whole and files it names where the step names them.
- Range: `db0c5f8..3b29618` (one commit). The remarks the correction answers: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/correction-1-remarks.md` (word for word; only the two items marked **Fix** bind: Minor finding 4 — the wording of WAY-395 about `--today`; Minor finding 3 — remove from WAY-380 and WAY-388–WAY-391 the examples that repeat what an invariant holds). The correction's handoff and report: `reports/correction-1-handoff.md`, `reports/correction-1-report.md`. The reviews that gave the two Minor findings: `reports/review-return-report.md` (its Minor finding 1) and the review of the fix of the whole change; the template of decisions: `elements/decisions/template.md` ("Verification"); the foundation step: `task-cycle/skill/foundation_step.md`.
- Judge the change against the remarks, the template (a pair of examples only for a part no invariant or test checks), the invariants each decision names, and that nothing the remarks did not ask for changed. Trust boundary: yes for the whole change, none in this range. Irreversible operation: no.
- Your directory for working copies: `.runs/review-correction-1/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-correction-1-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Do not run the full gate; `python -B elements/common/foundation_check.py` and focused runs of `elements/common` and `agent-instructions` are yours.
- Working copies: you make any in your directory under `.runs/` of the worktree, never in the system's temporary directory; before you return remove each (`git worktree remove --force`, then `git worktree prune`) and say so in the report; where a removal fails, name the remainder with its path and reason.

## What you return

First line, graded findings as the method gives, checks with command and exit code, **Unread material**, **Searches not found or unclear**, the working-copies line, and a short return: status, report path, changed files with line counts, one-line check result.
