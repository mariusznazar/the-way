# Second correction report — cycle `cycle-remarks-batch-4`, the human's remarks S1–S2

**Status:** `done`

**Commit:** `1c1e8c8` (range `98e2d86..1c1e8c8`): `elements/common/foundation_check.py`,
`elements/common/test_foundation_check.py`, `elements/common/rules.md`,
`elements/decisions/template.md`, `elements/invariants/template.md`, `foundations/decisions.md`,
`task-cycle/skill/request_template.md`.

Foundation entries edited, each `the cycle's` (WAY-114, WAY-30):

- WAY-71 — EN: Where an entry stands on several things and only some are missing, the missing one is
  the last item of the value and reads as the form of its field, after the known items. PL: Gdy wpis
  opiera się na kilku rzeczach, a brakuje tylko części, brakująca jest ostatnią pozycją wartości i ma
  postać właściwą dla pola, po pozycjach znanych.
- WAY-287 — EN: A value that names a known entry and then a descriptive `TODO` is one gap, shown with the
  missing part alone. PL: Wartość, która wymienia wpis znany, a po nim opisowe `TODO`, jest jedną luką
  pokazaną tylko z częścią brakującą.

## S1 — the mixed value, route 1

- **Script (`foundation_check.py`).** The reading of the three fields (an invariant's *Rests on* and
  *Derives from*, a decision's *Based on*) changed from "a value that begins with `TODO` is one
  description" to "the first item of the value that begins with `TODO`, and all that follows it, is one
  description". New `todo_item(value)` finds that item: the items are joined by ` · `, a ` · ` inside
  quotation marks joins nothing, and a `TODO` inside quotation marks begins no item (the same masking
  `unquoted` uses). `known_part` (was `missing_thing`) returns the entry with the value cut before the
  `TODO` item, so the items before it are read exactly as today (identifiers, fact names, quoted
  sources, decision numbers, with their reference checks) and the description is read by nothing. A
  `TODO` item with no description (bare, in backticks, or `TODO —`) is reported with the field's hint,
  on the line of that item, wherever it stands in the value. A value with no `TODO` item, and the
  fields that forbid `TODO`, are read as before. Docstring: the sentence "only a value that begins with
  `TODO` is read so" is replaced by the new rule (it also says `clock-tick · TODO` is now an error).
- **Tests (14 new methods; `test_foundation_check` 111 → 125).** For each of the three fields: a known
  entry followed by `TODO — <description>` passes, also with a comma and with ` · ` in the description,
  and with a decision number or fact-like word in a *Based on* / *Derives from* description; a known
  entry followed by a bare `TODO` fails with the hint (three bare forms, line numbers 8, 9, 21 asserted);
  a known entry that does not exist before a `TODO — …` item still fails as a reference; `TODO` first
  and then more text reads as one description; a known entry after the description is part of it;
  *Derives from* with a quoted source then a missing decision passes; *Based on* with `TODO` inside a
  quoted source, or ` · TODO` inside the quote, is no `TODO` item, and a bad fact after such a source
  is still reported. Red run before the code: 17 failing tests (rests-on and derives-from mixed cases and
  *Based on* bare cases), `python -B -m unittest test_foundation_check` exit 1; green after: OK. One new
  test (`…todo_first_reads_the_rest_as_its_description`, whole-value case) and the *Based on* described
  cases already passed before the code, as the whole-value reading was already in; they guard the
  behaviour the new rule must keep. (One of my first cases put a decision number in a *Rests on*
  description; the script checks any decision number outside *Derives from* anywhere in the invariants
  file, as before, so I removed the number from that case.)
- **Words.** WAY-71's binding sentence and `elements/common/rules.md` carry the same added clause (checked
  by a whitespace-collapsed substring comparison in both files): "where an entry stands on several
  things and only some are missing, the missing one is the last item of the value and reads as the form
  of its field, after the known items". WAY-71 *Verification*: a *complies* case (`Rests on: <the known
  fact> · TODO — <the missing fact, with its source>`) and a *violates* case (a whole-value `TODO`
  with the known fact in its description, or `<the known fact> · TODO` with nothing after). *Rationale*:
  two sentences — the known items stay named because every link is written (WAY-17) and a named item stays
  checked as a reference, which a known one moved into a description would not be; the missing one closes
  the value. (The rationale names no script, WAY-05.) Both templates say it for their fields
  (`elements/invariants/template.md` *Links*; `elements/decisions/template.md` *Based on* bullet), with the
  example form and the note that the description runs to the end so a comma or ` · ` inside joins
  nothing. WAY-287 *Verification*: the *complies* case for a mixed value; item 15 of
  `request_template.md`: "a `TODO` that closes a value after known entries is the same gap: one item,
  naming what is missing alone, not the known entries".
- **Search of the foundation (WAY-33).** grep over the repository (outside `.git` and `.runs`) for
  "begins with TODO", "read whole", "bare TODO", "descriptive TODO", "mixed list" and `python-stdlib`:
  the sentences on this rule stand in WAY-71, WAY-287, `rules.md`, both templates, the script docstring
  and item 15 only, all edited here. The projected-mode forms (`project-level/definition_template.md`,
  `elements/invariants/skill/SKILL.md`) and the glossary rule are not on the main branch and were
  unchanged in the first correction's reading; no conflict. The invariant with `python-stdlib-modules`
  in `foundations/invariants.md:121` stays a plain fact; no entry in the-way holds a `TODO` in the three
  fields.
- **`foundation_check.py` counts.** the-way (`python -B elements/common/foundation_check.py .`): exit 0,
  0 errors. loop2, read-only (`python -B elements/common/foundation_check.py <the loop2 checkout>`):
  exit 1, 1 error — `foundations/invariants.md:1244: *Rests on* reads `TODO` and names no fact`, the
  bare `TODO` the human knows; nothing about *Based on*, *Derives from*, *Relations*, *Origin*, and no
  mixed value.

## S2 — what does not change

The three fields, the whole-tree reading of item 15, `TODO` rejected in *Relations* and *Origin*, the
order of the gate and the other items are untouched; the file list above is the whole change.

## Checks (command and exit code)

- `python -B -m unittest test_foundation_check` (in `elements/common/`), before the code: FAILED
  (failures=17), exit 1; after: OK, 125 tests.
- `python -B gate/run_tests.py elements/common` exit 0 (144 tests)
- `python -B gate/run_tests.py task-cycle` exit 0 (238)
- `python -B gate/run_tests.py instruction-files` exit 0 (104, 5 skipped)
- `python -B gate/run_tests.py agent-instructions` exit 0 (18)
- `python -B gate/run_tests.py elements/part-map` exit 0 (39)
- `python -B gate/run_tests.py relation-model` exit 0 (12)
- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors")
- `python -B gate/run_tests.py installation` exit 0 (44 tests)
- Not run: the full gate.

## Own-work check

Requirement most likely unmet: "the known entry stays checked as a reference" with the description left
unchecked. Checks: the tests `…a_known_fact_before_a_todo_is_still_checked`,
`…a_decision_before_a_todo_is_still_checked` and `…a_fact_before_a_todo_is_still_checked` (a missing
`clock-tock`, `ABC-77`) fail with the reference message; and the descriptions containing `ABC-77`,
`clock-tock`, commas and ` · ` pass. Second: a `TODO` inside a quoted *Based on* source is no item
(three cases). Mutations thought through: cutting at the wrong index would read the description as
facts (caught by the described cases); not masking quotes would make `"one · TODO tick"` a `TODO` item
(caught by the quoted cases); dropping the bare check for a non-first position would let
`clock-tick · TODO` pass (caught by the three bare cases of each field).

## Reaches beyond the dispatch

none beyond the handoff; I used the search named in item 4.

## Unread material

none (the handoff and remarks whole; the files I edited were read at the places edited and, for
`foundation_check.py`, its docstring, constants and the reference functions).

## Searches not found or unclear

- Unclear: a comma or a newline as a separator before a `TODO` item. The handoff and the remarks speak
  of ` · ` only; `located` still splits *Rests on* items on commas too, so `clock-tick, TODO — x` is
  read as the item `clock-tick` and the item `TODO — x`, the latter reported as no identifier of a fact
  (as before this correction). I did not widen it; the templates state the ` · ` form.
