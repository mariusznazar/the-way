# Report — the one author, cycle `cycle-remarks-batch-4`

**Status:** `done with concerns` (concerns: the WAY-287 edit, the two off-list wording fixes and the
reading of "leaves" in item 7 below, all named under *Choices*).

## Commits (branch `task/cycle-remarks-batch-4`, base `e3825a8`)

1. `3effb9b` — Recognise a numbered heading of Searches not found or unclear in the remarks check
   (To do 4).
2. `77ecd4a` — Never name a task document in Origin, describe a missing fact in Rests on, run the
   gate once after the return step (To do 1, 3, 5, 6, and the part of 7 that stands in WAY-287).
3. `0d59ce9` — Start the gate after the return step and show a missing fact in Rests on to the human
   (To do 2, 7).

## Files changed (added / removed lines)

- `task-cycle/remarks_check.py` +7 / -3 (docstring sentence copied from the task; `SECTION_NUMBER`)
- `task-cycle/test_remarks_check.py` +28 / 0
- `elements/common/foundation_check.py` +20 / -3
- `elements/common/test_foundation_check.py` +37 / 0
- `elements/common/rules.md` +3 / -2
- `elements/decisions/template.md` +4 / -2
- `elements/invariants/template.md` +3 / -1
- `foundations/decisions.md` (WAY-160, WAY-71, WAY-287) +27 / -12 (approx.; `git diff --stat` has the exact count)
- `task-cycle/skill/SKILL.md` +5 / -2
- `task-cycle/skill/blocked_finding.md` +3 / -2
- `task-cycle/skill/request_template.md` +5 / 0

## What each To do item became

1. `elements/decisions/template.md`, `## Origin`: the sentence replaced word for word.
2. `task-cycle/skill/SKILL.md` step 10: the two sentences inserted after its first sentence, word for
   word. Numbering of steps 10 and 11 unchanged.
3. WAY-160 *Verification*, "complies" replaced word for word (rewrapped). Edited in place.
4. `remarks_check.py`: new `SECTION_NUMBER` (`\d+(\.\d+)*[.)]?` then blanks), applied once at the start
   of the heading text, after emphasis marks are removed; docstring sentence copied from the task;
   three new tests.
5. `foundation_check.py`: new `check_rests_on`; a `Rests on` value that begins with the word `TODO`
   (also in backticks) is read whole, never split; with no description after `TODO` and dashes it is
   an error `*Rests on* reads `TODO` and names no fact: write `TODO — <the fact, with its source>``.
   Docstring updated; five new tests.
6. WAY-71 binding sentence and `elements/common/rules.md` carry the sentence of item 6 word for word.
7. `request_template.md`: new item 15 in *For you to decide* (see *Choices*).

## Foundation entries (the foundation step)

Each entry is marked `the cycle's`: the task has no *Settlements to record* row and no projected
entry; WAY-160 and WAY-71 are edited in place as the task's To do 3 and 6 command, WAY-287 is my
addition (see *Choices*).

- WAY-160 — `the cycle's`. EN: The gate runs once on the tree the return step and its review leave,
  and again only where the merge with the target branch changed it. PL: Bramka idzie raz, na drzewie
  zostawionym przez krok powrotu i jego przegląd, a drugi raz tylko tam, gdzie scalenie gałęzi
  docelowej zmieniło drzewo. Also added to *Rationale* (why, and the price: a failing gate sends its
  fix back through the return step) and to *Rejected* ("rerunning after the return step only the
  checks that read the foundation — the-way does not know which checks of a product read its
  foundation", the wording the task's *Decisions in play* quotes).
- WAY-71 — `the cycle's`. EN: The main branch may hold `TODO` only in an invariant's *Rests on*, as
  `TODO — <the fact, with its source>` naming a missing fact, and a change that leaves one puts it
  before the human. PL: Gałąź główna może mieć `TODO` tylko w polu *Rests on* niezmiennika, w postaci
  `TODO — <fakt i jego źródło>`, a zmiana, która je zostawia, pokazuje to człowiekowi. *Rationale*
  rewritten (the "until facts have entries" reasoning is gone); *Rejected* gained the two ways quoted
  in the task's *Decisions in play*.
- WAY-287 — `the cycle's`. EN: The section for the human's decisions also holds each descriptive
  `TODO` in an invariant's *Rests on* that the change leaves. PL: Sekcja decyzji człowieka obejmuje
  też każde opisowe `TODO` w *Rests on* niezmiennika, które zmiana zostawia. One clause added to the
  binding sentence, one sentence to *Rationale*.
- No glossary term, invariant, environment fact or part-map entry written; none called for.

## Checks (command and exit code)

- `python -B -m unittest test_remarks_check` (from `task-cycle/`), before the code: FAILED (failures=2),
  exit 1 — the two new tests of the numbered heading fail on `[] != ['one item']` etc.; the third
  new test (a negative one) passes already, by design. After the code: OK, 53 tests.
- `python -B -m unittest test_foundation_check` (from `elements/common/`), before the code: 9
  failures in the new tests (descriptive `TODO` rejected as "is no identifier of a fact"; bare `TODO`
  passing with "0 errors"). After the code: OK, 103 tests.
- `python -B gate/run_tests.py task-cycle` exit 0 (238 tests)
- `python -B gate/run_tests.py elements/common` exit 0 (122 tests)
- `python -B gate/run_tests.py agent-instructions` exit 0 (18)
- `python -B gate/run_tests.py instruction-files` exit 0 (104, 5 skipped)
- `python -B gate/run_tests.py relation-model` exit 0 (12)
- `python -B gate/run_tests.py elements/part-map` exit 0 (39)
- `python -B gate/run_tests.py installation` exit 0 (44; it runs `foundation_check.py`)
- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors"); also with
  `--skip-test-citations` after the decisions were edited, exit 0.
- Not run: the full gate `python -B gate/run_tests.py` (the orchestrator's alone); no change touches
  a skill's name or description, so `agent-instructions/skill_entry_points.py --write` was not run.

## Own-work check (section 3)

- Requirement most likely unmet: "copy a quoted sentence exactly" (items 1, 2, 3, 4, 6). Check: a
  script reads the four target files with whitespace collapsed and tests that each quoted sentence
  is a substring. Result: all six sentences found (template Origin, SKILL.md step 10, WAY-160
  complies clause, remarks_check docstring, WAY-71, `rules.md`). The only difference from the task is
  line wrapping.
- Requirement second most likely unmet: item 5's "whole, without splitting". Test
  `test_rests_on_a_missing_fact_described_passes_whole` includes a description with a comma, with
  identifier-looking words (`clock-tock`) and with ` · ` inside; all pass because the value is read
  whole.
- Mutations thought through: dropping the `—–-` characters from the strip in `check_rests_on` makes
  the `TODO —` case pass: the test `bare_todo` catches it. Dropping the word boundary
  `(?![^\s`])` reads `TODOs` as `TODO`: `a_word_that_only_starts_with_todo` catches it. Dropping
  `SECTION_NUMBER` fails the two positive heading tests (seen failing). An over-broad number
  pattern (anything before the name) is caught by the negative heading test (`Section 12. ...`,
  `12.Searches`, `12. Other searches ...`).

## A bare `TODO` in the foundation of the-way itself

None. `grep` of `foundations/invariants.md` finds no `Rests on` with `TODO` at all, and
`foundation_check.py .` reports 0 errors on the tree. Out of the task's scope, and for the other
side of the pin: loop2's bare `TODO` in its `invariants.md`, as the task's *Out of scope* says.

## Choices (how to make what the task settles)

1. **Item 7 — where the descriptive `TODO` shows: *For you to decide*, as new item 15.** Chosen from
   `request_template.md` itself: that section "holds everything whose merge needs the human's yes,
   and nothing else", and WAY-71 says the change "puts it before the human"; a left `TODO` is a gap
   the merge puts on the main branch, which needs a yes. Rejected: *Foundation entries* (lower part)
   — it lists entries and asks for nothing, so the human would not be asked; item 6 ("entries the
   human did not see at the task document") — a row's entry is seen at the task document yet may
   still carry a `TODO`, so item 6 would not catch it. Cost if wrong: one numbered item to move.
   Reading of "leaves": the item is for a `TODO` the change writes or keeps in an entry it edits,
   found in the change's diff of the invariants file; a `TODO` in an entry the change does not touch
   is not the change's and gives no item (otherwise each request would repeat the same old gap).
   Cost if wrong: a gap left in an untouched entry never reaches a request; the foundation review is
   the place for it.
2. **WAY-287 edited (one clause in the binding sentence, one in *Rationale*), though the task does not
   list it among the decisions it edits.** WAY-287 lists exhaustively what *For you to decide*
   holds and says its `none` means nothing else waits for a yes; item 15 would otherwise contradict
   it (WAY-33, WAY-37: fix the entries that wait for what the change brings). Rejected: leaving
   WAY-287 as it is and reporting the mismatch — the foundation would say two things at once the
   moment this merges. Cost if wrong: one clause to take out; the orchestrator should check this edit,
   since it is marked `the cycle's` and goes before the human at the merge.
3. **Two phrases outside the task's list**, so that step 10's new ordering does not contradict the
   places that run the gate with no return step before it: `task-cycle/skill/blocked_finding.md`
   ("as step 10 gives, at once, since no return step runs on this code", WAY-163) and
   `task-cycle/skill/SKILL.md` sub-step 9.4 ("as step 10 gives, at once, since no return step
   runs"). The pin-move run at SKILL.md line 48 I left: it is a run on a commit, not on the finished
   change. Cost if wrong: two small phrases to remove.
4. **`invariants/template.md` line 122–124** (the *Links* bullet) now says a missing *Rests on* reads
   `TODO — <the fact, with its source>`, never the bare word, which `foundation_check.py` reports
   (WAY-17, WAY-71). The handoff pointed to this template for statements that must follow; the old
   sentence ("reads `TODO` rather than `none`") would have licensed the bare word.
5. **Bare-`TODO` rule details**: the value is recognised by the word `TODO` at its start (with an
   optional backtick); the description is whatever remains after blanks, backticks and dashes
   (`—`, `–`, `-`), so `TODO`, `` `TODO` ``, `TODO —` fail and `TODO the store` (no dash) passes. A
   value like `TODO · clock-tick` also passes, since the part after the dash-less `TODO` is non-empty;
   the template form is the dash form, and I did not police the dash itself. Cost if wrong: a
   stricter regex.
6. **Number pattern in `remarks_check.py`**: `\d+(\.\d+)*[.)]?` followed by at least one blank, so
   `12.`, `12)`, `3.1`, `3.1.` all work and `12.Searches ...` does not. Applies to headings only (as
   the task says); the bold-label form `**12. Searches ...**` is not accepted.
7. **Three commits**, by area, with `foundations/decisions.md` in the second although WAY-160's
   text goes with the third commit's gate order: the decisions file has three entries edited and
   cannot be split without interactive `git add -p`.

## Reaches beyond the dispatch

- Read `agent-instructions/README.md` (named by `AGENTS.md`) and `the user's global rule on writing scripts`
  (a rule of the global instructions before writing scripts). The latter proved needed: a
  Python heredoc and a `sed` command under Bash had stripped backslashes from a regex; I found it by
  reading the diff and corrected it with the Edit tool before committing.
- Read WAY-286, WAY-287, WAY-289 whole (they were in the "also" list) and searched the repository for
  `TODO` statements, `Origin` rules, uses of `remarks_check`, `step 10` and `after the return step`
  (the WAY-33 search). Read `task-cycle/record_template.md` lines 120–145 and `correction.md` 30–45
  (to see they stay true; they do).
- `elements/common/migrate_foundation.py` and `elements/part-map/` tests were not otherwise read; the
  part-map tests were run only.

## Unread material

- WAY-295, WAY-296, WAY-298, WAY-300, WAY-290 (named in the handoff list): not read whole; I read
  none of them. WAY-17, 163, 294, 07, 11, 37, 148, 260, 05, 29, 33, 35, 286, 287, 289 and 27 I read
  whole; WAY-159 whole; WAY-160, WAY-71 whole. WAY-295/296/298/300 concern the remarks check's
  listing, the record's remarks form, the pin at the start and the review reminder, which none of
  the changes alters in meaning.
- WAY-24, WAY-25, WAY-113 and the other decisions that `way_of_working.md` names in passing: not read.
- The invariants of the 20 whose *Part* names `every`, `decisions`, `task-cycle` or `elements-common`:
  not read one by one. I searched `foundations/invariants.md` for WAY-71, WAY-160 and for `TODO`
  and found no entry that names them or holds a `TODO`; I did not read the invariants' sentences.
  `skill-rule-source`, `element-directory-contents`, `record-copy-image-check` and
  `test-method-citation` were not read; the gate directories I ran (task-cycle, elements/common,
  installation, instruction-files, agent-instructions, relation-model, elements/part-map) pass.
- The part map entries `decisions`, `task-cycle`, `elements-common`: not read; no file was added,
  removed or moved, so no entry's *Files* changes.
- The glossary: not read; no term is used in a new meaning.
- `elements/decisions/examples.md`, `elements/common/projected_mode.md`, `elements/decisions/skill/projected.md`:
  not read (not projected mode; examples are decisions in the log).

## Searches not found or unclear

- A bare `TODO` in the foundation of the-way: not found (no `Rests on` with `TODO` in
  `foundations/invariants.md`).
- An invariant or a test that cites WAY-71 or WAY-160 or checks the `TODO` rule on the main branch:
  not found in `foundations/invariants.md`; the rule is checked by `foundation_check.py` and its tests.
- Unclear: which `TODO`s of a changed invariants file count as "left" by the change (item 7 of the
  task, WAY-71's "a change that leaves one there"); I read it as written or kept in an entry the
  change edits (*Choices* 1).
- Unclear: WAY-71's *Verification* "complies" example still says a decision whose source is silent
  reads `Based on: TODO — <what is missing>`, while its binding sentence allows `TODO` on the main
  branch only in *Rests on*. The two disagree already at the base commit; I did not change the
  example (not in the task) and report the mismatch.
- Unclear: whether step 10's added sentence should also govern the three runs "as step 10 gives" of
  blocked or failed cycles (I added "at once" to two of them; see *Choices* 3).

## Problems as observed

- A Bash heredoc with Python and a `sed -i` containing backslashes produced `\d`/`\t` mangled into
  `d`/a tab in `remarks_check.py`. Evidence: `cat -A` of the line and the diff. Cause: the shell
  or tool layer drops/reads backslashes (a guess; not isolated). Fixed with the Edit tool; the diff
  and tests confirm the final file.

## Weakest point of my own work

Choice 1 and 2 together: the placement of the item 15 in *For you to decide* and the matching edit of
WAY-287, a decision outside the task's list of edits. They are the only places where the text is mine
and not the task's. The reviewer should compare item 15 and the WAY-287 clause with the sentence
"a change that leaves one there puts it before the human" (WAY-71) and say whether "leaves" reaches
the `TODO`s of untouched entries; if so, the item and the clause widen from "writes or keeps in an
entry it edits" to every `TODO` on the tree.
