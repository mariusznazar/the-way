# Handoff to the reviewer — the review of correction 1 (once)

You are the reviewer of the whole change, resumed (Opus). Same worktree
`the task's worktree (the repository's root)`, same rules (read-only on the branch, no full gate,
delegation as before). Method: `task-cycle/review/SKILL.md`, the review of a correction; the remarks
stand in place of a findings file.

**Range:** `4d7ad7960b10399ff64d67ca1b98b15e97dac375` to `d7323f17` — one commit by the author (10 files,
+219 −176): `foundations/decisions.md`, `process-audit/SKILL.md`, `process-audit/audit_count.py`,
`process-audit/record_items.py`, `process-audit/test_audit_count.py`, `process-audit/test_record_items.py`,
`task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`,
`task-cycle/skill/reserved_return.md`.

**The remarks that bind (word for word):** `.runs/task-cycles/readiness-approval-rename/reports/correction-1-remarks.md`.
Item 1 (let through) needs no work. Item 2: fix in this request the use of "entry" for an item of a list in
the description of a cycle's record, with the word the change already gives a line of a table where it
fits ("row"), consistent with the glossary, the word added to the glossary if new there, and if a place
means something no plain word covers, say so. The author's report:
`.runs/task-cycles/readiness-approval-rename/reports/author-correction-report.md` (the word it chose is
"sub-item" for an item of a nested list under an item of the record, and why; kinds of "entry" it left,
numbered 1–8, with reasons; no glossary entry added, with the reason by WAY-95). The frozen task:
`.runs/task-cycles/readiness-approval-rename/task.md`. The report of your earlier reviews: you know them.

**What to judge.**
- Does the correction do what item 2 asks, within what it binds: every use of "entry"/"entries" for an
  item of a list under an item of a cycle's record, in the English text of tracked files, is renamed, and
  nothing else is touched? Search by WAY-97 yourself; judge the author's choice of "sub-item" over "row"
  or "item" and its reason, and its decision not to add a glossary entry (WAY-95), against the remark's
  "add the word to the glossary if it is new there".
- The kinds of "entry" the author left (its report's kinds 2, 3, 6 especially: the plan's log of changes in
  `foundations/decisions.md` WAY-145 and `project-level/lead/skill/SKILL.md`, the gate-run registry,
  "file/entry/section" in two lead files): is leaving each within the remark's scope? A left use is a
  finding only if the remark covers it; say which are outside it.
- Every word-only change to a decision (WAY-309, WAY-337, WAY-404, WAY-405) keeps its meaning; read each
  whole. The `# decision:` quotes of the tests equal the sentences as changed (`foundation_check.py`).
- The scripts `process-audit/audit_count.py` and `process-audit/record_items.py` (the part map names
  `audit_count.py` as a trust boundary): only messages, docstrings and comments changed; what they accept and
  refuse is the same (crafted input: a record whose *Process remarks* or *Review rounds* has no sub-items, a
  text beside its items, a wrong indent — same verdict as at `4d7ad796`; compare with a worktree of the old
  head). The changed expected values in the tests (rule "Changing an existing test" of
  `guidelines/testing.md`): cause and evidence stated, no assertion weakened.
- Lines the rename lengthened re-broken with no word changed.
- Run the affected focused checks yourself once, with command and exit code (`process-audit`, `task-cycle`,
  `elements/common`, `product-guidelines`, `gate`, `foundation_check.py`). Do not run the full gate.

**Report** to `.runs/task-cycles/readiness-approval-rename/reports/review-correction-report.md`, first line
`PASS <sha>` or `FAIL <sha>`; grades as before (a new Critical or Important finding fails the review; Minor and
outside-the-scope findings go to the request's list); **Unread material**; **Searches not found or
unclear** (`none` if nothing); checks with command and exit code; working copies (directory
`.runs/review-correction/`, removed before return, say so). Return only the first line, a one-line check
result and the report path.
