# Report of the correction for the human's remarks (correction 1)

**Status:** done

Base: `34d9970e0a7a130e6e0488c553170fbe7a6ca8a9`. Evidence in `reports/fixer-correction-checks/`
(`gate-process-audit.txt`, `gate-part-map.txt`, `foundation-check.txt`).

## Commits

| Commit | Remark | Files |
|---|---|---|
| `65ef8dd5` | 1: four test names | `process-audit/test_audit_count.py` |
| `ff70e690` | 2: relation of WAY-385 | `foundations/decisions.md` |

## The remarks as made, and how

Remarks word for word are in `reports/correction-1-remarks.md`. The two that bind (items 4-9 accepted: the two fixes);
the others (the brackets of the `except` lines, the unproven fix of the flaky test, `plan` at 109 lines) were let
through and are untouched.

### 1. Four test names that said "entry" (fixed, `65ef8dd5`)

Found by the word (`grep -n "def test.*entr"`), at lines 545, 556, 1428 and 4986. The words are those of commit
`462add5d` (an item of a list under the record's items is a "sub-item"):

| Old | New |
|---|---|
| `test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries` | `test_the_corrections_item_before_the_remarks_item_is_not_among_its_sub_items` |
| `test_items_after_the_remarks_item_are_not_its_entries` | `test_items_after_the_remarks_item_are_not_its_sub_items` |
| `test_an_entry_of_review_rounds_without_its_findings_file_leaves_the_share_unknown` | `test_a_sub_item_of_review_rounds_without_its_findings_file_leaves_the_share_unknown` |
| `test_crafted_entries_of_review_rounds_break_no_cell_and_give_no_answer_they_do_not_state` | `test_crafted_sub_items_of_review_rounds_break_no_cell_and_give_no_answer_they_do_not_state` |

- Four lines changed, names only: no assertion, no expected value, no body; the lines `decision:` and `invariant:` of
  the tests stand as they were (the fourth carries `decision: WAY-404` and is untouched; the first three carry none).
  The diff of the commit shows exactly the four `def` lines.
- `git grep -n` of the four old names over the repository (`.runs` excluded) found no other reference. The words that
  remain in the file with the other meanings (`entry` as a key of the locations file, a line of a JSON transcript, and
  "foundation entries" in a plan text) are not items of a record's list and stay.
- `ruff format --config ruff.toml` left the file unchanged; `ruff check --config ruff.toml --ignore-noqa` exit 0.
  The new fourth name makes the `def` line 99 characters, within 100.
- `python -B gate/run_tests.py process-audit` exit 0, 277 tests (`gate-process-audit.txt`).

### 2. WAY-385 names WAY-382 (fixed, `ff70e690`)

*Relations* of WAY-385 now reads `derives from WAY-379 · derives from WAY-360 · derives from WAY-361 · derives from
WAY-382`. No other field and no binding sentence changed; edited in place (WAY-07).

- **Choice: `derives from`.** The template defines `derives from` as a higher decision this one serves and `narrows` as a
  decision this one deliberately goes against in a narrower area, where the two collide. WAY-385 does not go against
  WAY-382: its first sentence counts the lines "on the code as the formatter of WAY-382 leaves it", so it rests on that
  decision and its rationale takes WAY-382's effect into the thresholds, the same stand as its other relations
  (WAY-379, WAY-360, WAY-361) take. 
- **Rejected: `narrows WAY-382`.** It would record a collision that does not exist, and the template then asks the
  narrowed decision to be named from the other side and the precedence to be stated in the binding sentences of the one
  that prevails; WAY-385 states no such area. Cost if wrong: a reader of the log, or the index of a selection, takes
  WAY-385 for a departure from WAY-382's formatter and looks for an area of precedence that is not there.
- `python -B elements/common/foundation_check.py` exit 0, "0 errors" (`foundation-check.txt`); the entry
  `elements/decisions/skill/SKILL.md` and the template's *Relations* and *Relations and precedence* rules were read as the
  step gives. `python -B gate/run_tests.py elements/part-map` exit 0, 40 tests (`gate-part-map.txt`).

## Tests altered that hold a decision or an invariant (WAY-03)

The four tests of finding 1: one of them cites WAY-404 by a line `decision:` (the line stands unchanged); the name only
changed. None cites an invariant. No decision's binding sentence and no invariant changed, so no test holds a reworded
sentence.

## Own-work check (WAY-164)

Requirement most likely not met: "only the names ... no assertion, no expected value changes" and "do not change the
binding sentence of WAY-385 or any other field". Check: `git diff 34d9970e..HEAD --stat` shows two files; the diff of
`test_audit_count.py` is the four `def` lines, and the diff of `foundations/decisions.md` is the one *Relations* line.
Both runs above passed at the first attempt.

## Runs (command, exit code)

| Command | Exit |
|---|---|
| `ruff format` / `ruff check --ignore-noqa` on `process-audit/test_audit_count.py` | 0 / 0 |
| `python -B elements/common/foundation_check.py` | 0 |
| `python -B gate/run_tests.py elements/part-map` | 0 |
| `python -B gate/run_tests.py process-audit` | 0 |

The full gate was not run (handoff).

## Reaches beyond the handoff

None.

## Unread material

none.

## Searches not found or unclear

none.

## Working copies

`.runs/fixer-correction/` (the two gate outputs while they ran): the outputs were copied to
`reports/fixer-correction-checks/` and the directory removed with `rm -rf .runs/fixer-correction`. No worktree or clone
was made. Remainder: none.
