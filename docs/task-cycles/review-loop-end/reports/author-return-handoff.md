# Return step handoff — same author, turn 4

Input: `78df576` (review of the whole change and of its fix: Ready to merge, no open findings — `reports/review.md`, `reports/review-fix.md`). Completed-change checks all exit 0 (`reports/completed-checks.json`). Target `origin/foundations` still `e7f7c3a` (orchestrator fetched at start; refetch and say if it moved).

Perform the return step of WAY-11 as step 11 of `task-cycle/skill/SKILL.md` **at the base `e7f7c3a`** gives it (this cycle runs under the base skill):

- Refresh the foundation selection by "Reading the foundation" for the real diff `e7f7c3a..78df576` and the current foundation; update `reports/foundation-selection.md` or write `reports/return-selection.md`.
- Read the cycle's choice log (cycle record questions table C1–C14) and your reports. Identify newly learned decisions, rules, uncovered behaviour, environment facts, glossary terms and part-map changes; compare the touched parts of the foundation with the code/text. For each candidate behaviour without an invariant: would changing it later violate a requirement or settled rule? Invariant if yes (report the need before writing — three authors, WAY-69); otherwise name it as a replaceable detail.
- Rows 1–7 of *Settlements to record*: confirm each is written (row → entry), write any the foundation step missed. The task carries no projected entries (independent task).
- Candidates already raised: your concern 5 (a `task-cycle` failure mode "the orchestrator rules on a blocking finding left after the review of the fix"); glossary — whether "blocking finding", "review of the fix", "review of the whole change" or "deferred minor finding" are used in a meaning a reader would not give them or in two meanings (WAY-95/97); environment fact — the Superpowers 6.4.1 observations in *Based on* of WAY-161/162 vs an environment-facts entry; the installed-version observation of choice C2 (active install 7.0.0, 6.4.1 still in the cache). Settle each: write it if it binds after the merge (WAY-36), otherwise one line in your report. Failure modes and criticality of a part belong to the human where WAY-46 says so — if the entry needs the human, report it as a question with your recommendation, not a write.
- Second whole-foundation search (WAY-33) against the current target tip, as the README asks before integration: domain, terms, findings; fingerprint recount.
- Nothing is deferred: what this request does not write is neither proposed nor listed for later.

Same boundaries as before (worktree only, explicit-path commits, line endings, no `.runs/` staged, no push, no agents). If you write anything, run the affected checks (outputs `reports/return-*.txt`, command and exit code) and give the commit and file list with added/removed lines.

Report `.runs/task-cycles/review-loop-end/reports/author-return.md` with the record template's *Return step* fields filled, the search record, every candidate with its settlement and reason, Polish meaning sentence for any new entry, checks. Short return.
