# Part map entry examples

Verbatim copies of entries from this repository's own part map (`foundations/part_map.md`), one
for each kind of entry described in `template.md`. An entry of a map carries no version and is
edited in place, so a copy follows the entry it comes from, and the guard checks that every
example matches its entry word for word.

Until a kind of entry has a real example, only its form in the template stands.

*A part, with every field filled:*

## part-map — The part map

The part answers for the part map: the form of an entry, the tools that write and check one, and
the map of the-way itself.

- **Files:** elements/part-map/**
  foundations/part_map.md
- **Depends on:** relation-model · elements-common
- **Failure modes:**
  - the guard assigns a file to the wrong part, or to none — a change is checked against the
    wrong decisions and at the wrong sharpness — high — not detected
- **Trust boundary:** elements/part-map/format_guard.py

*A part whose tool does not exist yet, so it holds no files:*

## task-cycle — The task cycle

The part answers for the steps a task runs through and for how sharply a change is checked along
them.

- **Files:** none
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

*A critical flow:*

## wording-reaches-dependants — A change of a binding part reaches what leans on it

Someone changes the binding sentences of a foundation entry, and every reference that leans on
the old binding part is reported before the change reaches the main branch.

- **Criticality:** high
- **Parts:** relation-model · decisions · gate
- **Invariant:** decision-guard-stale-reference — test: gate/test_wording_reaches_dependants.py
- **Coverage:** none

*A surface declared at the item itself:*

## content-fingerprint — The fingerprint

The same wording gives the same fingerprint.

- **Declared at:** relation-model/fingerprint.py · fingerprint

*A surface that cannot be marked at the item, and leans on a test instead:*

## entry-format — The form of an entry

The form of an entry changes for a product only when that product moves the commit it pins.

- **Declared at:** not markable — test: elements/decisions/test_format_guard.py
