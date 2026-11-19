# Return step for correction 1 - code-order-formatter-linter-size

**Status:** done. **Commits:** none (nothing needed correcting). **Head compared:** `ff70e690`, base `34d9970e`.

## Return step

- **Foundation compared with code:** the correction changes two things, compared as follows; nothing no longer matched.
  - WAY-385 (`foundations/decisions.md:10784`): the diff of `34d9970e..ff70e690` in that file is the one *Relations* line,
    now `derives from WAY-379 · derives from WAY-360 · derives from WAY-361 · derives from WAY-382`; no other field, no
    binding sentence and no *Verification* changed. Its sentence ("both counted on the code as the formatter of WAY-382
    leaves it") is the dependence the relation records. `agent-instructions/test_size_invariant.py` still holds
    `FUNCTION_LIMIT = 110`, `FILE_LIMIT = 1200` and its `decision: WAY-385 "A function of a script of the-way has at most
    110 lines, counted with the functions nested in it"` line, which matches the unchanged opening of the sentence; that
    file is outside the correction's diff.
  - The *Relations* rules (`elements/decisions/template.md`, "Relations and precedence"): two types, `derives from` ("a
    higher decision this one serves") and `narrows` ("a decision this one deliberately goes against in a narrower area");
    a relation is written in the entry that depends on the other (WAY-18) and names the other by its number alone
    (WAY-02). The new item is written in WAY-385, which depends on WAY-382, and names it by `WAY-382`. `narrows` would
    record a collision the sentences do not have (WAY-385 states no area where it prevails over WAY-382), so `derives from`
    is the type the closed list gives; the fixer's choice stands. No chain or mutual `narrows` arises (WAY-382 names WAY-379
    and WAY-173 only). WAY-385's *Scope* lies inside WAY-382's.
  - `elements/common/foundation_check.py` reads a decision's *Relations* for shape (items joined by ` · `, no `TODO` after
    a type, references that name a decision): `python -B elements/common/foundation_check.py` exits 0, "0 errors".
  - Search of the foundation for what the relation changes: the decisions, invariants, part map and glossary that name
    WAY-385 or WAY-382 are WAY-382 itself, WAY-385 itself and the invariants `formatter-layout` (derives from WAY-382) and
    `function-and-file-size` (derives from WAY-385); none states a relation between the two decisions or depends on the
    list. No file holds a copy of the *Relations* line (`git grep "derives from WAY-360"` finds only the log).
  - The part map is not touched by the correction and no part gained a file; not compared again.
  - The four renamed tests (`process-audit/test_audit_count.py` lines 545, 556, 1428, 4986): the diff is the four `def`
    lines and nothing else (no assertion, expected value, `decision:` or `invariant:` line); the old names occur nowhere
    else in the repository (`git grep` outside `.runs`); the new names read as the glossary gives. The glossary's `entry`
    is "the text, under one or more headings of its own, that a file of the foundation holds about one thing it
    records", and each renamed test speaks of an item of a record's list, which the record template calls a sub-item, as
    the eleven tests of `process-audit/test_record_items.py` do. The fourth test cites WAY-404 by a `decision:` line that
    quotes "the sub-item of the round", which now agrees with its name.
- **Decisions written or changed:** none by this step (WAY-385's *Relations* was changed by the fixer, `ff70e690`).
- **Invariants written or changed:** none.
- **Environment facts:** none (the correction rests on no source outside the product).
- **Glossary terms:** none (WAY-95: `entry` keeps its one meaning in the glossary; the renamed tests no longer use it
  against that entry).
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** none (no row falls to the correction).

## Checks run

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` at `ff70e690` | 0 ("0 errors") |
| `git diff 34d9970e ff70e690 --stat` | two files, 5 insertions, 5 deletions |

No test was touched by this step, so no focused run was made; the fixer's runs (`process-audit` exit 0 with 277 tests,
`elements/part-map` exit 0) stand in its report and were not repeated. The full gate was not run.

## Own-work check (WAY-164)

Requirement most likely not met: the correction touches only the four names and the one *Relations* line, so a leftover
`entry` in the sense of a record's sub-item, or a stale reference to an old name, could remain. Check: `git grep` for the
four old names over the repository (none), `git grep -nE '\b(entry|entries)\b'` on `test_audit_count.py` (the remaining
uses are a key of the locations file at lines 982-994, a line of a JSON transcript at 1274-1276 and "foundation entries"
in plan texts at 4730, 4772, 4861), and the diff of the range. Showed: no leftover in the sense of a record's sub-item.

## Observation, not corrected

`process-audit/test_audit_count.py` lines 982-994 name the key of the locations file `entry` (a loop variable) and lines
1274-1276 name a line of a transcript `entry`. Neither is an item of a record's list, neither is in the remarks (they name
the four test names and the relation), and the task's point 8 leaves uses with a meaning from the domain. Left.

## Unread material

- `elements/decisions/skill/SKILL.md` was not read: the step wrote no decision. The *Relations* passage of
  `elements/decisions/template.md` was read; its other sections were not.
- `foundation_check.py` was read by search for its *Relations* handling (lines 41-60, 173-183, 592-640), not whole.
- The fixer's `reports/fixer-correction-checks/` outputs were not read beyond the first line of `foundation-check.txt`.

## Searches not found or unclear

- A place that states a relation between WAY-382 and WAY-385 other than the log: not found.
- A copy of WAY-385's *Relations* outside `foundations/decisions.md`: not found.
- Nothing was unclear.

## Working copies

None made.
