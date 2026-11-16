# Return step report — renumber-decisions-on-merge

**Status:** done — nothing no longer matched; no commit.

**Commits:** none. Head stays `059b891f`; `git status --short` shows a clean tree.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`
  (`reports/author-return-step-foundation-check.txt`).
- `python -B gate/run_tests.py product-guidelines` — exit 0 (14 tests, OK), run for the one test that
  reads the skills' references. No other directory was run: nothing changed in this step.
- Not run: the product's full gate.

One-line result: all run checks pass; no change made.

## Entries compared, and what no longer matched

Compared with the final text of the change (`task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`,
`task-cycle/record_template.md`, `foundations/decisions.md` at `059b891f`):

- **WAY-403** (written): its binding sentences match the final text of "The renumbering of the task's
  decisions" — the next free numbers after the highest of entries and withdrawn numbers (item 1); the
  commit of its own before the merge (item 4); the one pass over the files and the original of the
  record, with the texts written afterwards, the rows of an earlier reconciliation's conversion and
  the human's remarks left as they are (item 2); the conversion only in the *Events* row, earlier rows
  beside it (item 5); both merges of the correction (`correction.md`). The count check of items 1 and 3
  is a detail of how the skill makes the pass verifiable and is no binding sentence of the entry; the
  pair of examples (500..502 -> 502..504, the second row 502 -> 505 ..., the corrupted row in the
  violating example) agrees with the skill. Nothing to correct. It names no withdrawn number; its
  *Relations* link live entries only.
- **WAY-19** (numbering): consistent; the new entry derives from it, takes the next free number
  (403), and the "no entry and no withdrawn number holds the next free number" rule is the one item 1
  follows.
- **WAY-02** (references by identifier): consistent; the pass rewrites every reference, the lines
  `decision:` of tests included ("every file of the branch that refers to a renumbered decision").
- **WAY-294** (process remarks hold the reports' items word for word): consistent; the same map is
  applied to the reports and to the remarks in one pass, so the check still finds them equal.
- **WAY-293** (a rule in a skill with one sentence of its reason; the skill names the decision where
  the choice has a real cost): consistent; the section names WAY-403 with one sentence of the
  reason, and step 12 and both paragraphs of `correction.md` name it.
- **WAY-162 and the review wording** (the reconciliation with the target branch is a code review):
  consistent; the renumbering commit stands in the merge review's range.
- Withdrawn entries named by the task (WAY-306, WAY-357, WAY-328): not linked anywhere in the change.
- Also searched (WAY-33), no entry disagrees: the log's lines that mention the merge of the target
  branch (the gate after the merge, the plan's collision text, the blocked request's list of what did
  not run) say nothing of numbers of decisions; `elements/decisions/template.md` repeats WAY-19.
- **Part map**, parts `task-cycle` (files `task-cycle/**`) and `decisions` (`elements/decisions/**`,
  `foundations/decisions.md`): the change adds no file and moves none; each touched file is in the
  part the map assigns it to, and the parts' descriptions ("the steps a task runs through"; "the log
  of the-way itself") stay true. No change.
- **Invariants** with `Part` `every`, `task-cycle` or `decisions`: compared with the change by their
  binding sentences; none is touched (`return-step-record` is satisfied by this record;
  `blocked-request-label` and `skill-entry-points` are unaffected — no label of
  `record_template.md` and no skill description changed; the entry-point and reference tests
  passed in the focused runs of the earlier stages).

## Record's *Return step* items

- Foundation compared with code: the entries and the part map above, each compared with the final
  text of the change at `059b891f`; what no longer matched: none.
- Decisions written or changed: WAY-403 (written).
- Invariants written or changed: none.
- Environment facts: none (no source outside the product).
- Glossary terms: none. `renumbering`, `conversion row` and `reconciliation` have no entry in
  `foundations/glossary.md`, and under WAY-95 take none: each is used as the field uses it ("the
  reconciliation with the target branch" is the cycle's existing phrase, and no sentence of the
  change reads differently for a reader who takes the ordinary meaning). "New decision" is defined
  at its use in the skill's section (a decision the task branch's log holds and its log at the merge
  base does not).
- Part-map changes: none.
- Projected entries written whole or in part: none.
- Rows of *Settlements to record* written: row 1 — WAY-403, first paragraph (the rule), with its
  place in the skill: step 12 and "The renumbering of the task's decisions" of
  `task-cycle/skill/SKILL.md`, and both merge paragraphs of `task-cycle/skill/correction.md`; row 2 —
  WAY-403, second paragraph (the conversion stands only in the *Events* row), with its place in
  `task-cycle/skill/SKILL.md` (item 5) and the sentence in `task-cycle/record_template.md` (*Events*).
  Marks: row 1 `row 1`, row 2 `row 2`, the pair of examples `the cycle's` (as in `author-report.md`).

## Choices of the fix and the questions of the decisions template

The choices of the fix report — the second row left as written (the conversion read as a chain), the
count check of items 1 and 3 — are instructions for how an agent works that stand in one skill of the-way
(WAY-293, the second paragraph; question 1 of the decisions template in the-way's log), and carry no
choice with a real cost that someone could reasonably take the other way beyond what WAY-403's
*Rationale* already carries (the second way out is named there as the price, "a reader follows two
rows"). They stay rows of the cycle's questions table; no entry is written. WAY-403's pair of
examples stays: no test holds its sentences (the change writes no test), and `foundation_check.py`
counts a pair as holding the entry.

The reviewer's Minor point N-1 of the review of the fix (the same number can stand in both rows with
two meanings after two renumberings) is not fixed, as the handoff says; it goes to the request's list.

## Unread material

- `foundations/glossary.md`: read by its headings only (to see whether the three words have an
  entry); no entry was opened.
- `foundations/invariants.md`: the entries whose *Part* is `every`, `task-cycle` or `decisions` were
  read by their heading and first sentence only, not whole.
- `foundations/part_map.md`: only the entries of `decisions` and `task-cycle` and the file's opening.
- Read whole: the handoff, `return_step.md`, `foundation_step.md`, WAY-95, and WAY-403 in its final
  form.

## Searches not found or unclear

none

## Working copies

`.runs/author-return/` (a helper script and the outputs): removed before the return. Kept in
`reports/`: `author-return-step-foundation-check.txt`. Nothing remains.
