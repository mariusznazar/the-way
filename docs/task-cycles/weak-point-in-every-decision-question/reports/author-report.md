# Author report — weak point in every decision question

**Status:** `done with concerns` (concerns are in "Problems and observations": the choices that go
beyond the literal *To do*, all named below; nothing blocks).

Worktree `the root of the worktree`, branch
`task/weak-point-in-every-decision-question`, base `bfb2e10`.

## Commits

- `a14b07f` — Give every decision question the weak point of its recommended way and the cost of
  undoing each way (`foundations/decisions.md` only).
- `a3c97df` — Carry the weak point and the cost of undoing into the texts that ask the human (the
  other 19 files).

## Files changed (added / removed lines, `git diff --numstat bfb2e10 HEAD`)

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 102 | 49 |
| `elements/common/way_of_working.md` | 13 | 4 |
| `elements/common/skill/build_table.md` | 1 | 1 |
| `foundation-review/with_the_human.md` | 10 | 12 |
| `process-audit/SKILL.md` | 25 | 13 |
| `product-guidelines/coding/SKILL.md` | 1 | 1 |
| `product-guidelines/coding/settle.md` | 1 | 1 |
| `product-guidelines/styleguide/SKILL.md` | 1 | 1 |
| `product-guidelines/styleguide/settle.md` | 1 | 1 |
| `product-guidelines/testing/SKILL.md` | 2 | 2 |
| `project-level/lead/answering.md` | 5 | 5 |
| `project-level/lead/conversation_template.md` | 1 | 1 |
| `project-level/lead/skill/SKILL.md` | 1 | 1 |
| `project-level/lead/skill/route_changes.md` | 4 | 4 |
| `project-level/plan/skill/delegated_mode.md` | 4 | 3 |
| `project-level/skill/existing_definition.md` | 7 | 6 |
| `project-level/skill/rounds.md` | 8 | 3 |
| `project-level/task/skill/final_review.md` | 1 | 1 |
| `project-level/task/skill/resolve_gaps.md` | 4 | 3 |
| `task-cycle/skill/request_template.md` | 21 | 13 |

Total 20 files, 213 insertions, 125 deletions. No code and no test file changed.

## What was done, by *To do* item

1. **WAY-113 edited in place** (`foundations/decisions.md`). First paragraph: a decision question
   gives the ways, the cost of each (the cost of undoing included, one word where nil), a
   recommendation and the weak point of the way recommended (strongest argument against it,
   anchored in the material where the material gives one; for a shortcut it names the right way
   and why it is not recommended); the exception of the check question stays word for word. The
   refinement sentence moved to a second paragraph (a part of another question, as the template's
   "Binding sentences" gives) and got the sentence on the rounds and the projected-changes step of
   a project definition (move of implication, reason of a costly decision; task refinement keeps
   the old rule). *Scope* gained `task-cycle`, `foundation-review`, `process-audit`,
   `product-guidelines`. *Verification* (complies and violates) holds the weak point, the cost of
   undoing, the shortcut case, the implication question in the rounds and its refusal in a task's
   refinement. *Rationale* holds the weak point and the cost of undoing, the practice taken from
   the Mega.DEV course with what was seen there (WAY-100, `Based on` stays `none` since a reader
   cannot open the recording), and the price named at question 7 (more questions after answers,
   longer rounds, no evidence the move caught anything). *Rejected* holds the ways not chosen of
   questions 2, 3, 7 (a, c) and 8 (a, c), each with the kept cost, besides the old ones.
2. **`elements/common/way_of_working.md`, "How a skill asks"**: the decision-question bullet says
   the same as WAY-113's first sentence.
3. **`task-cycle/skill/request_template.md`**: part 2 of "What an item carries" gives the cost of
   undoing each way (one word where nil); part 3 gives the weak point in one sentence, by pointer
   to "How a skill asks"; both examples show both. Kind 2 *Questions* and the row "A question from
   the foundation step" point to the item parts instead of restating options and recommendation.
4. **The search of the whole repository**: see the two lists below.
5. **`way_of_working.md`, step 4.1**: no longer restates the decision question; points to "How a
   skill asks" for the decision and the assessment question; the rule for a value the source does
   not give stays in the step.
6. **`project-level/skill/rounds.md`**: "Four moves run through the rounds" — contradiction,
   implication, the reason, and the "I do not know" rule (now a pointer for the decision case).
   `elements/common/skill/definition_variant.md` untouched, as the task says.
7. **`process-audit/SKILL.md`**: step 3 holds the rule of the task (name from the rows what is
   broken and a step can change; put it as a question of decision by "How a skill asks"; the
   recommendation rests on what is broken, never on returns, waiting or the cost level; nothing to
   change is said in one sentence and the assessment question stays open with no recommendation);
   the two rules of working on returns and on the cost of an occurrence are unchanged. The note of
   step 4 (it has no separate template file; the note's list stands in step 4) gained *Decided*
   beside *Weighed* and *Set aside*; the introduction names the third outcome.

### To do 4 — places changed (each restated what a question of decision gives)

- `elements/common/skill/build_table.md` (the choice "between ways shown" now points to "How a skill asks").
- `foundation-review/with_the_human.md` (the opening line and the "your recommendation / what each
  costs" of items 1–4 removed, the opening line points to the section).
- `process-audit/SKILL.md` (step 1 question about a missing place; step 3 as item 7; item 4 of step 3
  "with no recommendation" now allows one where the rows show something broken).
- `product-guidelines/coding/SKILL.md`, `styleguide/SKILL.md`, `testing/SKILL.md` ("How to show").
- `product-guidelines/coding/settle.md` (thresholds with no code), `styleguide/settle.md` ("which
  criterion, which ratio") — found by the search, not on the task's list.
- `project-level/skill/rounds.md`, `existing_definition.md`.
- `project-level/lead/answering.md` (two places), `conversation_template.md`, `lead/skill/SKILL.md`
  (step 6), `lead/skill/route_changes.md`, `plan/skill/delegated_mode.md`,
  `project-level/task/skill/resolve_gaps.md` (paragraph "If two answers conflict…").
- `project-level/task/skill/final_review.md` (step 4, found by the search; the other task already
  merged into the base, so it is not a concurrent edit).
- `task-cycle/skill/request_template.md` (*Questions* kind 2 and the table row).
- Decisions reconciled through the search of the whole foundation (WAY-33): **WAY-155** (binding
  sentence: "a question of decision … as WAY-113 gives it"), **WAY-174** (the two examples of
  *Verification* "complies"), **WAY-378** (binding sentence, *Verification*, and a new relation
  `derives from WAY-113`, since the entry already named WAY-113 without a link). No test holds
  these decisions' sentences by a `decision:` line (searched), and no invariant derives from them.

### To do 4 — places looked at and left

- `project-level/task/skill/orchestrated_mode.md:17` and `project-level/skill/delegated_mode.md:11`:
  list ways, costs and recommendation, but only "where/as required by "How a skill asks"" — a
  pointer, like the one the task names as left alone.
- `project-level/technology/settle.md`, `project-level/definition_template.md`,
  `product-guidelines/*/new_tools.md`: carry the weak point of WAY-123 — the task puts them out of
  scope as the special case.
- `project-level/task/template.md:143-146` (*Not chosen* keeps ways and their cost): describes a
  field of the document, names WAY-113 and the question; it restates no rule of the question.
- `task-cycle/spec/design.md:25`, `task-cycle/plan/SKILL.md:61`, `task-cycle/change/SKILL.md:126`,
  `task-cycle/skill/SKILL.md:356,365`, `task-cycle/record_template.md:30`, `task-cycle/spec/SKILL.md:27`:
  agents' own design choices and reports ("the ways open" of a return), not a question to the human.
- `project-level/task/skill/read_sources.md:33` ("no question, no recommendation" about a split) —
  not a question of decision.
- `project-level/lead/skill/SKILL.md:127,140-143` ("offer recommendations as accepted decisions",
  refinement exception) and `elements/common/skill/task_variant.md:45`: task refinement; unchanged.
- `elements/common/skill/definition_variant.md` — unchanged by the task.
- Decisions: WAY-123 and its text ("each choice with its recommendation and the weak point") —
  out of scope; the decision on the way an agent checks the running product (a recommendation
  "owed", WAY-113 named) and its *Rejected* — state no ways/costs rule.

## Foundation entries

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-113 (decision question gives cost of undoing and weak point; check-question exception unchanged) | `row 1`, `row 2` | A decision question gives the ways, the cost of each (with the cost of undoing), a recommendation and the weak point of the recommended way, and the check question stays except where the human took the recommended way as offered with its weak point named. | Pytanie o decyzję podaje drogi, koszt każdej (z kosztem cofnięcia), rekomendację i słaby punkt rekomendowanej drogi, a pytanie kontrolne zostaje, chyba że człowiek wziął rekomendowaną drogę tak, jak ją podano, z nazwanym słabym punktem. |
| WAY-113 (the right way named in a shortcut's weak point; Mega.DEV practice named) | `row 3` | The weak point of a shortcut names the right way and why it is not recommended, which the decision takes from the Mega.DEV course by WAY-100. | Słaby punkt drogi na skróty nazywa drogę właściwą i mówi, dlaczego jej nie polecamy; decyzja przejmuje to z kursu Mega.DEV według WAY-100. |
| WAY-113 (project definition refinement: implication and reason questions) | `row 7` | In the whole refinement of a project definition, a question may follow an answer by the move of implication or ask the reason of a costly decision; a task's refinement keeps the old rule. | W całym doprecyzowaniu definicji projektu po odpowiedzi może paść pytanie z ruchu „implication” albo o powód decyzji kosztownej do cofnięcia; doprecyzowanie zadania zostaje przy dzisiejszej regule. |
| WAY-155, WAY-174, WAY-378 (reconciled, WAY-378 also linked) | `the cycle's` | Each of the three points to WAY-113 for what a decision question gives instead of listing ways, cost and recommendation. | Każda z trzech odsyła do WAY-113 po to, co daje pytanie o decyzję, zamiast wymieniać drogi, koszt i rekomendację. |

Rows 4, 5, 6 and 8 go to files (`request_template.md`, `way_of_working.md` step 4.1,
`process-audit/SKILL.md`), as their column *Goes to* gives: no entry is written for them. No
withdrawn identifier was touched; no glossary term, invariant or part-map entry was written. The
search of the foundation found no invariant or test that depends on the sentences changed (grep of
`decision:` lines and of `foundations/invariants.md`, both for WAY-113, 123, 155, 174, 378).

## Checks run (command → exit code)

- `python -B elements/common/foundation_check.py` → 0 (`0 errors`), run after the entry and again
  after the commits, no `--skip-test-citations` (no invariant test is added).
- `python -B gate/run_tests.py task-cycle` → 0 (514 tests).
- `python -B gate/run_tests.py project-level` → 0 (278 tests).
- `python -B gate/run_tests.py process-audit` → 0 (234 tests).
- `python -B gate/run_tests.py product-guidelines` → 0 (14 tests).
- `python -B gate/run_tests.py instruction-files` → 0 (105 tests, 5 skipped).
- `python -B gate/run_tests.py elements/common` → 0 (242 tests).
- `python -B gate/run_tests.py agent-instructions` → 0 (27 tests; checks the skill entry points).
- `python -B gate/run_tests.py elements` → 1 and `... foundation-review` → 1, both with
  `no test found in <directory>`: neither directory holds a `test_*.py` of its own (the tests of
  elements stand in `elements/common` and `elements/part-map`; foundation-review has none). Not a
  failure of a test. `elements/part-map` was not run: nothing under it changed and its tests do not
  read the files changed.
- Not run, by the handoff: `python -B gate/run_tests.py` with no directory.
- The test logs stand in `.runs/author/test_*.log` of the worktree (ignored).

## Own-work check (section 3)

- Requirement most likely not met: *To do* 4 — every tracked Markdown file that restates what a
  decision question gives, instead of pointing to "How a skill asks", is found, and the search of
  the foundation reconciles the decisions that restate it (WAY-33).
- Check: after the edits, `git grep -n -i -E "ways open|what each (way )?costs|their costs?|costs and a
  recommendation|ways/costs|the cost of each|options, costs|with the cost of each way|and a
  recommendation" -- '*.md'`, and the same over `foundations/*.md` for `ways, cost`, `recommendation`
  and `options`, then each remaining hit read in its context.
- Result: remaining hits are exactly the ones listed under "places looked at and left", the
  entry WAY-113 itself and `way_of_working.md` "How a skill asks" (the rule). The first run of the
  greps (before the edits) found, besides the task's list, `product-guidelines/coding/settle.md`,
  `styleguide/settle.md`, `project-level/task/skill/final_review.md`, `project-level/skill/
  delegated_mode.md` and decision WAY-378; all but `project-level/skill/delegated_mode.md` are in the
  changed list, and that one was left (see above). No failed run to report.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md`: WAY-377's neighbour WAY-378 whole (found by the search of the whole
  foundation, where its binding sentence restates the rule; WAY-378 is not in the handoff).
- `elements/decisions/template.md`, `elements/decisions/skill/read.md` and `decide_entry.md`, and
  `elements/common/rules.md` (the writer of a decision reads them as the skill gives).
- `foundations/invariants.md`: an extract of the invariants whose *Part* names `every` or a touched
  part, made by a script and read (the first 700 characters of each entry, which cuts three long
  entries; the Read tool flagged the extract file as non-UTF-8 because the script wrote it through
  the console's encoding, not because of the invariants file); no invariant bore on the change.
- Other files read to decide the To do 4 search: `project-level/skill/delegated_mode.md`,
  `project-level/task/skill/{final_review,orchestrated_mode,read_sources}.md`,
  `project-level/task/template.md` (lines 138-152), `project-level/definition_template.md`
  (lines 228-262), `product-guidelines/{coding,styleguide}/{settle,new_tools}.md` (excerpts),
  `task-cycle/{spec/design,plan/SKILL,change/SKILL}.md` (excerpts), `elements/common/skill/task_variant.md`
  (lines 38-56).

## Unread material

- `.runs/task-cycles/weak-point-in-every-decision-question/index_work.md` and `index_sections.md`:
  not read; I selected by the part named in the handoff and by search of the whole foundation.
- The part-map entries of `elements-common`, `project-level`, `task-cycle`, `foundation-review`,
  `process-audit`, `product-guidelines`, `decisions`: not read. The files changed all lie in those
  parts' directories, which the foundation check and the tests of those directories confirm.
- The decisions WAY-114, WAY-120, WAY-315, WAY-33, WAY-100, WAY-123, WAY-155, WAY-174: read whole.
  The row of WAY-327 in "Withdrawn identifiers": read as the single line (`WAY-327 | its rule … stands in
  task-cycle/skill/request_template.md | none`), the table's other rows not read.
- `elements/decisions/examples.md`: not read (the example entries for the form).
- The vault files the task quotes (the data file of the review, the notes of the Mega.DEV course):
  not read; the task's rows carry what was needed (and a private path is no source for the-way).
- `task-cycle/request_check.py`: not read; its test directory passed.

## Searches not found or unclear

- "The template of the audit's note it names" (handoff): `process-audit/SKILL.md` names no separate
  template; the note's list stands in its step 4, where *Decided* was added. Taken as that list.
- *Based on* for the Mega.DEV recording: WAY-100 gives "describe in *Rationale* what was seen there"
  for a source a reader cannot open; done, *Based on* stays `none`.

## Choices made (with the way rejected and the cost if wrong)

- WAY-113's refinement rule moved to a second paragraph (a part of another question) so the first
  paragraph keeps three sentences, as the template asks. Rejected: one paragraph of four sentences
  or a four-clause third sentence; cost if wrong — a reviewer who reads the second paragraph as a
  separate question; the fix is to merge the two paragraphs.
- `way_of_working.md` "How a skill asks": the refinement bullet gained its own bullet on the
  project definition, though *To do* 2 names only the decision-question bullet. Rejected: leaving
  the bullet that says the question after an answer is asked only on a contradiction, which would
  contradict WAY-113 after the change. Cost if wrong — one extra bullet to remove.
- WAY-378 got a relation `derives from WAY-113` besides the rewording. Rejected: rewording without
  the link (the entry then names WAY-113 in its binding sentence with no written link). Cost if
  wrong — one relation to drop.
- `final_review.md` changed although the other task changed that file: that task is merged in the
  base, and its sentence restated "the ways, the cost of each and a recommendation" next to a
  pointer. Rejected: leaving it as the pointer-with-a-list kept in `orchestrated_mode.md`. Cost if
  wrong — one sentence to restore; the list was the only difference.
- `with_the_human.md`: removed "your recommendation / what each costs" from items 1–4 so the
  opening line alone says what a question gives. Rejected: adding "and its weak point" to each item,
  which would restate the rule four more times. Cost if wrong — the items read as asking no
  recommendation; one clause to put back.
- In *Rejected* of WAY-113 the way 7 c ("leave, as the description of an earlier request advised")
  is worded "leaving the instructions as they were", since *Rejected* names no request or file
  (the template's rule on prose).

## Problems and observations

- The task says (question 1, *Context*) that the other task would change `final_review.md` and
  `SKILL.md` of the refinement; the base already holds that change (WAY-378 and its text in
  `final_review.md`). The base is therefore not the state the task describes, and the pointer-only
  rule the task assumes for that file did not hold: it restated the rule in a colon list. Handled as
  the choices above.
- "Four moves" in `rounds.md`: the fourth item ("I do not know …") is a rule rather than a move; the
  task's wording "lista … dostaje oba ruchy obok dwóch, które już ma" keeps the count as it was
  (two existing items, two added). Noted, not changed.
- `gate/run_tests.py elements` and `... foundation-review` exit 1 by the runner's rule for a
  directory with no tests; the handoff lists them as focused runs, so they stand here with the
  reason rather than as a pass.

## Working copies

- `.runs/author/` of the worktree: the edit scripts and the extract of the invariants stood there
  and were removed; the test logs `test_*.log` of the checks remain (they are the record of the
  runs above and weigh little); nothing else was made. No worktree, clone or screenshot was made.
