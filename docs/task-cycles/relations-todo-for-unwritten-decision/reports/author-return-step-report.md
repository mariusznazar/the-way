# Author report — the return step, relations-todo-for-unwritten-decision

**Status:** done with concerns (one correction goes to the human: WAY-287, below)

**Commit:** `763af69` ("Hold the Relations part of WAY-71 by tests and keep its pair only for the rest"),
on top of the reviewed fix `68d8645`. Files: `foundations/decisions.md`
(WAY-71 *Verification* only), `elements/common/test_foundation_check.py` (2 comment lines). Not pushed.

## What the step compared

Read: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`, the handoff, the task,
`author-report.md`, `author-fix-report.md`, `review-fix-report.md` (first part) and the head of the code.
Compared with the code: WAY-71 and WAY-126 (the entries the change edits), WAY-287 (named by the task),
WAY-17, WAY-07, WAY-33 and WAY-114 (named by the handoff; no sentence of them touches the change), the part
map entries `decisions`, `elements-common`, and the files of the change.

## Items of the record's *Return step*

- **Foundation compared with code:** WAY-71's binding sentence (Relations in the form
  `TODO — <the decision, and where it is expected>` as the last item, a bare `TODO` an error, *Origin* never
  `TODO`) matches `foundation_check.py` at the head: bare, behind a type and comma-joined forms are errors;
  the described form passes; *Origin* is rejected. WAY-126's second paragraph (replace the `TODO` by
  `derives from <number>` / the number) is a rule for authors, no code. The decision template, `rules.md`
  and `request_template.md` item 16 say the same as WAY-71. One correction made (next item).
- **Decisions:** none new. One edit, in WAY-71's *Verification*: the Relations part of the pair that this
  change added is now held by tests (as the decisions skill's step 3 gives: a pair carried for a test the
  same change writes is removed by the return step). Two tests,
  `test_relations_a_bare_todo_names_no_decision` and `test_relations_derives_from_todo_is_an_error`, carry a
  line `decision: WAY-71 "…reports a missing field, or a word not given it, as an error."`; *Verification* now
  opens with the clause `tests:` (a bare `TODO` in *Relations*, a `TODO` behind a relation type there, a
  `TODO` joined by a comma, the described form after known relations); and I removed from the pair the
  complying example for a known plus a missing decision in *Relations*, and the violating examples for a bare
  `TODO` in *Relations*, `derives from TODO` and the comma join. The pair keeps what no test holds, including
  the parts that predate this change (it was not asked to remove those, and they stay in the pair). The
  meaning of WAY-71 is the same; WAY-126's pair stays whole: no test holds its sentence (it states how an
  author works).
  Evidence the line is read: with the quotation altered the foundation check reports
  `elements/common/test_foundation_check.py:739: the quotation stands in no binding sentence of `WAY-71``
  (1 error); restored, `0 errors`.
- **Invariants:** none written. The task, WAY-71 and the human set no rule that asks for one; the rule is held
  by decision lines and the pair (WAY-22).
- **Environment facts:** none (the change rests on no source outside the product).
- **Glossary terms:** none (no word used in a meaning WAY-95 gives an entry; "descriptive `TODO`" is plain
  language of the entries).
- **Part-map changes:** none (no file added, removed or moved; the entries `decisions` and `elements-common`
  still describe their parts).
- **Projected entries:** none; the task has no project definition source.
- **Rows of *Settlements to record*:** none (the section reads `none`).

## For the human: WAY-287 (not corrected, by design)

WAY-287's binding sentence, its *Verification* violates line and its *Rationale* list the fields whose
descriptive `TODO` the request puts before the human as "an invariant's *Rests on* or *Derives from* or a
decision's *Based on*" (`foundations/decisions.md`, around the lines "each descriptive `TODO` in an
invariant's *Rests on* or *Derives from* or in a decision's *Based on*", the violates line "the section reads
`none` while an invariant's *Rests on* or *Derives from* or a decision's *Based on* holds a descriptive
`TODO`", and the sentence in *Rationale* "A descriptive `TODO` that stands in an invariant's *Rests on* or
*Derives from* or in a decision's *Based on* once the change is merged"). Item 16 of the request template now
lists a fourth place, a decision's *Relations*. The task fixes WAY-287 as unchanged ("Bez zmiany" in *Decisions
in play*), and a correction there adds a field to an approved decision's list beyond what the task carries, so
under WAY-30 and WAY-114 it is the human's, not mine. Recommendation: add "or a decision's *Relations*" in
the three places in a later change. If left, the sentence still holds by WAY-287's own rule that another
decision may add a kind of item (WAY-71 does) and the template lists every kind. The request puts this before
the human; I wrote nothing for it.

## Not done, by design

N1 and N2 of the review of the fix (a relation type with a capital or two spaces hides a bare `TODO`; two new
tests overlap) are not fixed here; they go to the request's list.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0, `0 errors` (after the commit's edits).
- `python -B gate/run_tests.py elements/common` — 0, 257 tests OK.
- Not run: the full gate (the orchestrator's alone, WAY-160); other directories (no file of them touched).

## Own-work check

Requirement most likely not met: the entry's new *Verification* is read as the template and the foundation
check give it (a clause `tests:` with no path, lines `decision:` that quote a sentence of the entry). Check:
the foundation check on the committed tree reports `0 errors`, and with the quotation altered it reports the
quotation as standing in no binding sentence (above), so the lines are read and held.

## Unread material

`reports/review-whole-report.md` (not read; its findings file was read in the fix step), `review-fix-report.md`
read from its first lines only (the part on the four findings); WAY-17, WAY-07, WAY-33, WAY-114 and WAY-287
were read whole in the first stage of this cycle, not again; `elements/decisions/skill/SKILL.md` was read in that
stage and not again, since the entry written here is an edit of a *Verification* whose rules stand in the
template read then.

## Searches not found or unclear

None. A search of the glossary for `TODO` and `descriptive` found no entry.

## Working copies

`.runs/author/` held a backup of the test file, my edit script and the test output; it stood at
`.runs/author/` and was removed before the
report. No worktree or clone was made.
