# Findings of the review of the whole change (reviewer's words, from review-whole-report.md)

Reviewed head: 34db2685148207b901f8a19c2629b0e14af04c91. First line of the review: FAIL.

## Blocking

### Important

**I-1. The check of step 3 fails on a correct pass whenever the old and the new numbers overlap,
which is the usual case.** Within the task (To do 2). From the one author's commit `34db2685`.

- Place: `task-cycle/skill/SKILL.md:710-711` — "3. Search the files of the branch and the original
  of the record for each old number: it stands nowhere but in what stays as it is."
- What is wrong: the map gives the new decisions the numbers right after the target branch's
  highest, so the new range starts inside the old one whenever the target branch took fewer numbers
  than the task has new decisions. Then an old number is also a new number, and after a correct pass
  it stands everywhere the renumbered decision is named. The entry's own complying example is such a
  map (500..502 -> 502..504, `foundations/decisions.md:6251-6255`: old 502 is the new number of the
  decision first numbered 500), and so are both cases the task names (the-way 355..360 -> 360..365,
  where 360 is in both ranges; loop2 D-50..D-65 -> D-57..D-72, where 57..65 are in both).
- Why it matters: the step is the one check the procedure gives that the pass reached every
  reference (To do 2: "jednym przebiegiem, obejmuje każde odwołanie"). Read as written, it reports
  a failure for every correct pass with an overlap, and the orchestrator either learns to discount
  it — then it no longer catches a missed reference — or "fixes" what it found by replacing the old
  number again, which is the chain the step before it forbids (`SKILL.md:705-706`, "never decision by
  decision") and the violating example of WAY-403 names ("so that 502 becomes 504 after 500 became
  502", `foundations/decisions.md:6259-6260`). Only the old numbers that are not themselves new
  numbers of the map (old minus new) can be searched for this way; for the rest the check has to be
  of another kind, for example a count of each reference before the pass under its old number
  against the count after it under its new one.
- Evidence: a scratch run of the pass as step 2 gives it, on the entry's complying map
  (`.runs/review-whole/scratch_renumber.py`, removed; its output is quoted here): after the pass the
  text `The spec names WAY-502, WAY-503 and WAY-504.` holds no old 500 or 501, and the step-3 search
  for old `WAY-502` finds it (`True`). The author's own-work check (`reports/author-passcheck.py`)
  tested the pass and not this search, so it could not catch this.

**I-2. The rewrite of an earlier reconciliation's conversion row "with the rest" corrupts that row
whenever the numbers first borne overlap the second map.** Within the task (To do 2 and 3, row 2 of
*Settlements to record*); the rule of rewriting the earlier row is the author's choice 5, beyond the
task's text. From the one author's commit `34db2685`.

- Place: `task-cycle/skill/SKILL.md:708-709` — "A row of an earlier reconciliation's conversion is
  rewritten with the rest, so that it reads from the numbers the decisions first bore to the present
  ones." together with `SKILL.md:702-707` ("Apply the map once to ... `cycle.md` ... in one pass").
- What is wrong: the sentence states the goal (first numbers -> present numbers) and prescribes a
  mechanism ("with the rest", that is the same one-pass application of the map) that does not reach
  it. The pass rewrites every whole number of the map's domain in the row, on the left side as well
  as on the right, and the left side holds the numbers first borne, which overlap the domain of the
  second map whenever the first renumbering moved the decisions by fewer places than their count —
  the usual case, as in I-1. The earlier row then names, on its left side, a number that is now the
  present number of another decision.
- Why it matters: the conversion is kept, by the human's choice (task, question 2, *Not chosen*:
  "nigdzie — stary commit albo wcześniejsza uwaga Mariusza ze starym numerem staje się
  nieczytelna"), so that an old commit or an earlier remark of the human that carries an old number
  can still be read. A corrupted row makes it read wrongly: a reader holding the first number 502
  finds no row for it in the first reconciliation's row, and the row instead maps 505, a number that
  now names another decision. The second renumbering is exactly the case WAY-403's rationale names as
  a price ("a correction can renumber a second time"), so the sentence is written for a case that
  will come. The step-3 search of I-1 meets the same row from the other side: the left side of an
  earlier row still holds old numbers of this map, so the row is neither "what stays as it is" nor
  free of old numbers.
- Evidence: the same scratch run: a first row `WAY-500 -> WAY-502, WAY-501 -> WAY-503, WAY-502 ->
  WAY-504` under a second map `502 -> 505, 503 -> 506, 504 -> 507`, applied as step 2 gives,
  becomes `WAY-500 -> WAY-505, WAY-501 -> WAY-506, WAY-505 -> WAY-507`; the goal the sentence
  names is `WAY-500 -> WAY-505, WAY-501 -> WAY-506, WAY-502 -> WAY-507` (`False`). Two ways out,
  each one sentence: rewrite only the right side of an earlier row, or leave earlier rows as they are
  and read the conversion as a chain of rows (the way the author rejected, at the cost of a reader
  following two rows); either way step 3 then has to name the earlier rows among what keeps old
  numbers.

## Minor findings within the task (fixed in the same round, WAY-161)

**M-1. The skill's example of whole-number matching names two live decisions of the-way's log.**
Within the task.

- Place: `task-cycle/skill/SKILL.md:706-707` — "match a whole number, so that `WAY-35` is not found in
  `WAY-355`."
- What is wrong: `WAY-35` ("What does an element's skill hold?") and `WAY-355` ("Which task fixes a
  defect found after a merge?") are entries of the log, and a decision number with the log's prefix
  in a tracked file is a reference by WAY-02 and by `elements/common/foundation_check.py`. The line
  is no reference to either decision; the change's own entry avoids exactly this by writing its
  examples as bare numbers (author's choice 4).
- Why it matters: small but concrete — a search of the foundation for what names WAY-35 or WAY-355
  (WAY-33) finds this line, and a withdrawal of either would make the foundation check report it as
  a reference to a withdrawn number, an edit to this skill for a change that has nothing to do with
  it. Bare numbers (`35` in `355`), as in WAY-403, avoid both.
- Evidence: `foundations/decisions.md` index lines `WAY-35 — What does an element's skill hold?`
  and `WAY-355 — Which task fixes a defect found after a merge?`
  (`.runs/review-whole/index.md`, removed); `foundation_check.py` docstring, line 27-28: "a
  reference that names no entry, or a withdrawn one: a decision number with the log's prefix
  anywhere in a file git tracks".
