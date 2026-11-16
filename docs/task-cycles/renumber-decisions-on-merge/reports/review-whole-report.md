FAIL 34db2685148207b901f8a19c2629b0e14af04c91

# Review of the whole change — renumber-decisions-on-merge

Range: `1feb483cbb5a6538a475d6e42629441ba563d7f8..34db2685` (one commit, `34db2685`, one author, no
plan, no slices). `git rev-parse HEAD` in the worktree is `34db2685148207b901f8a19c2629b0e14af04c91`,
the head given. Variant: the review of the whole change of a one-author change (WAY-136): no slice,
so no blocking finding comes from a slice; each comes from the one author's commit.

Changed files (from `python -B task-cycle/change_file_sizes.py` and `git diff --numstat`):

| File | Before | After | Added / removed |
|---|---|---|---|
| `foundations/decisions.md` | 10760 | 10824 | +64 / -0 |
| `task-cycle/record_template.md` | 253 | 256 | +4 / -1 |
| `task-cycle/skill/SKILL.md` | 808 | 845 | +39 / -2 |
| `task-cycle/skill/correction.md` | 104 | 108 | +9 / -5 |

## Findings

### Critical

none

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

### Minor

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

### Out of scope

none

## Coverage of the task

- To do 1 (step 12 says what to do when the target branch took the numbers): met by
  `task-cycle/skill/SKILL.md:589-593` — the trigger, the order (renumber first, then merge), the
  pointer to "The renumbering of the task's decisions" and WAY-403 — and the section
  `SKILL.md:686-718`: a commit of its own before the merge (item 4), the next free numbers after the
  target branch's highest, entries and withdrawn numbers alike (item 1), never the target branch's
  numbers (`SKILL.md:695-696`).
- To do 2 (one pass over the branch's files and the original of the record before the
  reconciliation is entered; later texts and the human's quoted remarks stay): met by `SKILL.md:702-
  709`, save the two defects I-1 (its check) and I-2 (the earlier conversion row).
- To do 3 (the conversion only in the row of the events that records the reconciliation, no note at
  the head): met by `SKILL.md:717-718` and `task-cycle/record_template.md:98-101`.
- To do 4 (the correction renumbers at both its merges): met by `task-cycle/skill/correction.md:8-12`
  ("In the-way itself, before anything else") and `correction.md:29-31,37` ("Take a link to the
  request").
- Row 1 of *Settlements to record*: WAY-403's first paragraph (`foundations/decisions.md:6234-6242`)
  says each part of the row: before the merge, a commit of its own, the next free numbers, never the
  target branch's numbers, one pass over the branch's files and the record as it stands before the
  reconciliation, later texts and quoted remarks unchanged, in step 12 and in the correction's merges
  ("before the request opens and ... in a correction after review, on either route"). Its *Rejected*
  holds the four ways of question 4 and the *Not chosen* of questions 1, 3 and 4, each with the
  reason its source keeps beside it and none beside the two ways for which the task keeps none, as
  `elements/decisions/template.md` gives for a decision written from a row (no derived way entered).
- Row 2: WAY-403's second paragraph (`foundations/decisions.md:6244-6245`), with the two *Not chosen*
  of question 2 in *Rejected*.
- *Decisions in play*: WAY-19 and WAY-02 are linked as live (`derives from`); WAY-306, WAY-357 and
  WAY-328, withdrawn in the log (`foundations/decisions.md:10783,10794,10817`), are named nowhere in
  the diff (`git diff ... | grep "WAY-306\|WAY-357\|WAY-328"`, exit 1). WAY-294's process remarks
  are covered by the one pass ("`cycle.md` with its process remarks", `SKILL.md:704`), so reports
  and remarks are rewritten by the same map and keep agreeing.
- Fidelity to the task's sources: nothing the change takes from the task is altered or invented,
  save the author's additions below (choices 3 and 5), which are judged there.

## The author's four choices, judged

1. Row 2 as a second paragraph of WAY-403, not an entry of its own — accepted, no finding. WAY-05
   gives a part of another question a paragraph of its own in an entry; WAY-19 keeps a question that
   can change on its own under a number of its own. Where the conversion stands could move on its
   own, so the call is close, as the author says; but the conversion has no meaning without the
   renumbering, and the entry's question ("How does a task's branch give new numbers ...") reaches
   the record of the numbers it gives. Cost if wrong: one entry split out later, with no reference to
   repair beyond this skill.
2. The procedure in a new section of `task-cycle/skill/SKILL.md` that step 12 points to — accepted,
   no finding. Step 12 itself says when the renumbering runs and that it comes before the merge, and
   names WAY-403; the section sits among the other reference sections after step 14 ("The process
   remarks check", "The record before it is committed"), and both paragraphs of `correction.md` need
   one place to name. WAY-293's second paragraph is kept: the skill names WAY-403 and gives one
   sentence of its reason (`SKILL.md:690-692`).
3. The renumbering commit in the range of the merge's review — accepted, no finding: the renumbering
   changes the reviewed code (the log, references in skills and tests), and the merge's reviewer, who
   asks whether the two sides still hold together (the rule of withdrawn WAY-306, now in
   `correction.md:33-39`), is where a wrong number in the branch's files would be caught; WAY-403's
   stated price, that no reviewer of the merge checks the rewrite of the record, stays true. The
   companion rewrite of an earlier reconciliation's conversion row is finding I-2.
4. The examples of WAY-403 with bare numbers — accepted, no finding: the foundation check reports a
   prefixed invented number as naming no entry, and bare numbers read unambiguously in the examples.
   The skill does not follow the same choice (M-1).

## WAY-135, read whole (the gap carried from the author)

WAY-135 asks for a spec where the task leaves an open design choice, which the glossary defines as a
choice that neither the task nor a spec settles and that "either sets a foundation entry or takes a
way that is costly to turn back once code is written on it". The task's two rows carry the one entry
the change writes, whole; the choices the author added (the section's place, the merge review's
range, the rewrite of an earlier conversion row, the form of the examples) set no foundation entry
and are each a sentence of a skill, cheap to turn back. So WAY-135 called for no spec here and the
cycle broke none of it. It bears on the change only in that the defect of I-2 sits in one of those
added choices, which no spec review saw; the review of the whole change is where it is caught.

## The structure of the code the change leaves

`task-cycle/change_file_sizes.py` gives the sizes above. The rule `### Size of a function and a file`
of `guidelines/coding.md` covers scripts and the change touches no script, so no worktree of the base
or the head was made for the test of the invariant `function-and-file-size`; the four files are
Markdown text, and no function grew. `SKILL.md` grows by 37 lines to 845, `foundations/decisions.md`
by one entry (task, question 4, names the cost: "jeden wpis więcej w dzienniku"). No finding of
structure.

## Declined to judge

- That another unmerged branch, `origin/task/audit-answers-contradiction-after-code` (commit
  `19f70031`), also writes a `WAY-403` (and `WAY-404`): a live case of the clash this change
  handles, to be met at step 12 by whichever request merges second; it is no defect of this change.
- How a correction's agent reads a remark of the human that names a number renumbered in the same
  correction (the remarks are recorded after the pass, word for word, so they keep the old number):
  the task settles that the remarks stay as written and the conversion row serves to read them; how
  the orchestrator hands such a remark to the correction's author is outside the task.

## Checks

- `git rev-parse HEAD` — `34db2685148207b901f8a19c2629b0e14af04c91`, the head given.
- `git log --oneline 1feb483c..34db2685` and `git diff 1feb483c..34db2685` — one commit, four
  files, read whole.
- `python -B task-cycle/change_file_sizes.py 1feb483cbb5a6538a475d6e42629441ba563d7f8 34db2685`
  — exit 0, table above.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`.
- `python -B elements/common/decision_index.py --output .runs/review-whole/sections.md --sections`
  — exit 0.
- `python -B elements/common/decision_index.py --output .runs/review-whole/index.md --section "Decision
  entries and the decision log" --section "The course of a task cycle" --section "The request and
  the human" --section "Review of a change" --part decisions --part task-cycle --decision WAY-19
  --decision WAY-02 --decision WAY-294 --decision WAY-135 --decision WAY-293 --decision WAY-403` —
  exit 0 (34 listed in full, 119 by heading). A first run that also named `--decision WAY-306`,
  `WAY-357` and `WAY-328` ended with exit 2, `Error: foundations/decisions.md: no decision WAY-306`:
  they are withdrawn, as the handoff says.
- `python -B -I .runs/review-whole/scratch_renumber.py` (scratch run of steps 2 and 3 of the new
  section) — exit 0; output quoted in I-1 and I-2.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, OK (skipped=2).
- Manual: `git diff ... | grep "WAY-306\|WAY-357\|WAY-328"` — exit 1, none named.
- Manual: `git log --all -S"WAY-403" -- foundations/decisions.md` — WAY-403 is free at the base; the
  other branch's use of it is under *Declined to judge*.
- Not run: the product's full gate, as the handoff gives (the cycle's own run and CI's).

## Reaches beyond the dispatch

- `elements/common/way_of_working.md` lines 54-194 (section "Reading the foundation" and step 4.3),
  for the selection and to check the reference of `SKILL.md:711`.
- `product-guidelines/reading.md`, whole, for the selection of guidelines.
- `foundations/part_map.md`, entries `decisions` and `task-cycle`, whole.
- `foundations/invariants.md`: the entries whose *Part* names `decisions`, `task-cycle` or `every`,
  by heading; read whole `foundation-change-merge-route`, `return-step-record`, `skill-rule-source`
  and `tracked-file-private-paths`, the ones the change could reach. None is changed and no invariant
  test is changed.
- `foundations/glossary.md`: the entries `entry` and `open design choice`, whole (for WAY-135).
- `elements/decisions/template.md` lines 75-105 and 295-315 (the rules of *Rationale* and
  *Rejected*, and of recovered decisions), to judge WAY-403's *Rationale* and *Rejected*.
- `elements/common/foundation_check.py`, its docstring lines 17-28, for M-1.
- `task-cycle/skill/correction.md`, whole; `task-cycle/skill/SKILL.md` lines 586-725 and its
  mentions of the return step, for the order of steps 11 and 12.
- `foundations/decisions.md` lines 10783-10818 (the withdrawn rows of WAY-306, WAY-328, WAY-357).
- Commit `19f70031` on `origin/task/audit-answers-contradiction-after-code`, its stat and headings
  only, to see what else holds WAY-403.

## Guidelines

The change writes no code, no test and no user interface: its four files are Markdown text of the
foundation and of skills, and the-way's guidelines (`guidelines/coding*.md`, `guidelines/testing.md`)
reach scripts and tests (`product-guidelines/reading.md`, "Name the affected work"). No guideline
file was selected, so none was read, and no rule of a guideline is reached.

## Working copies

All in `.runs/review-whole/` of the worktree: `sections.md` and `index.md` (the index of my
selection), `fc.txt` (the foundation check's output), `scratch_renumber.py` (the scratch run of
I-1 and I-2), `t_pg.txt` and `t_tc.txt` (the outputs of the two focused test runs). No worktree,
clone or screenshot was made. The directory `.runs/review-whole/` was removed whole before the
return; nothing is kept in `reports/`, since the report quotes what it needs. Remainder: none.

## Unread material

22 decisions of the index of my selection read whole: WAY-02, WAY-05, WAY-11, WAY-12, WAY-13,
WAY-18, WAY-19, WAY-21, WAY-22, WAY-26, WAY-29, WAY-36, WAY-125, WAY-135, WAY-136, WAY-293, WAY-294
and WAY-403 of those listed in full, and WAY-04, WAY-07, WAY-17 and WAY-54 of those listed by heading.
WAY-403's *Rejected* and *Rationale* were read whole as the diff holds them.

none — no decision bearing on the change stayed unread. Read by their binding sentences in the index
alone, which leave nothing open for this change: WAY-10, WAY-148, WAY-161, WAY-162, WAY-227,
WAY-229, WAY-263, WAY-287, WAY-288, WAY-289, WAY-295, WAY-297, WAY-300, WAY-316, WAY-363, WAY-364.
Opened in part only: WAY-71 (its first paragraph) and WAY-144 (its binding paragraph and the start
of *Verification*), whose questions I ran through and found not bearing. No guideline file was
selected (see *Guidelines*).

## Searches not found or unclear

- `decision_index.py --decision WAY-306` (and WAY-357, WAY-328, named in the task's *Decisions in
  play*) — not found as entries: withdrawn, as the handoff says; their rules stand in
  `task-cycle/skill/correction.md` and `task-cycle/record_template.md`.
- Unclear: whether the merge's review in step 12 runs whenever a renumbering ran, since step 12 asks
  for it only "where that changes the reviewed code" (`SKILL.md:592`). Read as: a renumbering runs
  only where the target branch added decisions to the log the change also changed, so the merge
  always changes a reviewed file then; no finding.
