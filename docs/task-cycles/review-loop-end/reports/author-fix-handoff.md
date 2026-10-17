# Review fix handoff — same author, turn 3

Input: `ac65ac3`. Review: `.runs/task-cycles/review-loop-end/reports/review.md` (range `e7f7c3a..ac65ac3`, With fixes: 0 Critical, 2 Important, 4 Minor) — read it whole. This cycle runs under the skill at its base `e7f7c3a`, where the author fixes the review's findings and the same reviewer reviews the fix range once; so all six findings are fixed here (the new rule of WAY-161 binds only after the merge). Orchestrator rulings (cycle record C12–C14):

## Important 1 — Superpowers' "out-of-scope observations" (C12)

The reviewer is right on the source: in 6.4.1 they are issues outside the **fix diff** (`subagent-driven-development/re-review-prompt.md:57-61`, `:92-95`; `SKILL.md:402-403`), ungraded and non-blocking, sent to the ledger as deferred minors. They are not findings outside the task.

Ruling — route (ii) in its method-faithful form, no new rule:
- That borrowed step is **not** replaced. An observation outside the fix diff stays what the method makes it, a deferred minor finding; and by WAY-161 the request lists unfixed Minor findings with the reviewer's words and place. So it reaches the request in the Minor list; it does not block and starts no round.
- Correct WAY-125's binding description of the replaced steps to what the methods actually do: (a) the orchestrator adjudicates and parks residual findings after the review of the final fix; (b) the final fix wave takes in deferred minor findings; (c) the executor rules on each "Declined to judge" line. Drop "findings outside the task wait in the method's ledger". Adjust WAY-125's *violates* and rationale only as far as this correction needs. Correct the skill's `:433` list the same way, and say in "The end of a code review" (briefly) that observations the review of a planned change's final fix reports outside the fix diff are deferred minor findings, listed with the Minor findings.
- WAY-161's *Based on*: remove the "Out-of-scope observations go to the ledger …" quotation unless a sentence of WAY-161/162 relies on it.
- Renew every fingerprint your WAY-125 change affects (WAY-31), and rerun the whole-foundation fingerprint recount.
- Rejected: route (i), counting Critical/Important observations outside the fix diff as remaining — it adds a grading and a blocking rule to the borrowed re-review that no row of the task carries. Cost if wrong: a serious issue seen only by the final fix's re-reviewer reaches the human listed in the request rather than blocking it; the human still sees it at the request.

## Important 2 — order before a blocked request (C13)

Move the skill to match WAY-163 and row 4 ("przed otwarciem"): before opening a blocked draft, run the gate, run `task-cycle/cycle_stages.py` for `stages.md`, write the cycle record and commit its pair (copy, then removal); then open the draft and link the record by the SHA of the commit that adds it. Do not reword WAY-163.

## Minor 1–4 (C14)

Apply the reviewer's fixes: (1) the review of the fix for a plan of one slice is by the same reviewer, as for a one-author change; (2) step 9's planned boundary includes the review of that fix; (3) for a finding the author/executor contests with evidence, the fix handoff asks the reviewer of the fix to state whether it keeps the finding — on the planned route the scoped re-review's "NOT ADDRESSED" alone does not settle a contested finding; keep it to one sentence; (4) reflow the paragraphs with ragged short lines that you touched (keep lines ≤ 100 characters).

## Checks, boundary, output

Same as turn 2: focused tests (`task-cycle`, `elements/decisions`), `gate`, decision guard with `--base none --merge-onto none`, `git diff --check`, skill entry points; complete outputs under `reports/fix-*.txt`, command and exit code each. A new commit (do not amend reviewed commits). Explicit paths, English message, line endings preserved, no `.runs/` staged, no push.

Append "Fix (turn 3)" to `author-implementation.md`: per finding — what changed, file:line, or why not; commit and `ac65ac3..HEAD` file list with added/removed lines; checks; whether the change of WAY-125 changes any Polish meaning sentence from your foundation report (give the new one if so). Short return; stop before the review of the fix.
