# Affected-review fix handoff — same author, turn 6

Input `74cf160`. Review: `.runs/task-cycles/review-loop-end/reports/review-affected.md` (Ready to merge: Yes; 4 Minor). Under the base skill the author fixes the review's findings and the same reviewer reviews the fix range once. Rulings (cycle record C18):

- Minor 1 (two clauses beyond the rows: WAY-162's later-review lists from ruling A2, WAY-163's reconciliation clause from choice C11) — **no text change**; the orchestrator labels both in the request's *What this request settles* as settled by the cycle, not by the task's rows.
- Minor 2 (`SKILL.md:403-406`, A1 vs A11) — **apply**: the A11 sentence excepts the ledger's deferred-minor and parked lines that the final review's handoff passes on as the borrowed method wrote them; keep it to a clause.
- Minor 3 (WAY-163 *violates* example `:5243-5244`) — **apply**: the example must not count as a violation a reconciliation (and its review) that ran before a block coming from the reconciliation's own review. *Verification* only; binding sentences unchanged, so WAY-163's fingerprint stays.
- Minor 4 (WAY-161 line `:5093`, 119 characters) — **apply**: rewrap only.

Checks: `elements/decisions`, `task-cycle`, `gate` tests; decision guard `--base none --merge-onto none`; fingerprint recount; `git diff --check`; outputs `reports/affected-fix-*.txt` with command and exit code. New commit, explicit paths, line endings preserved, `.runs/` unstaged, no push, no agents. Append "Affected-review fix (turn 6)" to `reports/author-return.md` with changes (file:line), commit, `74cf160..HEAD` file list and line counts, checks. Short return.
