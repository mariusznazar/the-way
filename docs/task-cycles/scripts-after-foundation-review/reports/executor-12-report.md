# Executor report — slice 12, task `scripts-after-foundation-review`

**Status:** done (with one mismatch named below: the error the plan names does not exist in the code, so a new message was written)

**Commit:** `7063f94` on `task/scripts-after-foundation-review` — "Read a bare TODO after a comma or a line break in the foundation check". Not reviewed; the review of the slice is the next stage.

**Files changed**

| File | Added | Removed |
|---|---|---|
| `elements/common/foundation_check.py` | 17 | 7 |
| `elements/common/test_foundation_check.py` | 48 | 1 |

## What changed

- `todo_item` (`elements/common/foundation_check.py`, about line 301): the split now also ends a piece at a comma and at a line break (`re.split(r"[·,\n]", masked)`), so a `TODO` after either begins a TODO item. Quoted separators and quoted `TODO` still begin nothing (the `QUOTED` mask is unchanged). The match is made against the full value at the piece's first character, not against the piece alone (see the own-work check).
- `known_part` (about line 562): a TODO item that follows a comma or a line break instead of ` · ` now gives an error:
  - bare (`clock-tick, TODO`, `clock-tick\n  TODO`): the existing bare-TODO message, at the line of the `TODO`;
  - with a description (`clock-tick, TODO — a second fact`): a new message, `*<field>* joins its items by ` · `: write ` · ` before `TODO`, not a comma or a line break`.
- Module docstring (about lines 47–50): one sentence added for the new rule.
- Tests: 7 new methods in a new section `# --- a TODO after a comma or a line break, not after ` · `` placed before the section "a missing thing as the last item …" (about line 723). The decision line of `test_reworded_sentence_with_its_citing_file_changed_is_not_listed` changed (line 1500, see WAY-03 below).

## Checks run

| # | Check | Command | Exit | Result |
|---|---|---|---|---|
| 1 | Baseline before the change | `python -B gate/run_tests.py elements/common` | 0 | 235 tests, OK |
| 2 | New tests on base, before the fix | `cd elements/common && python -B -m unittest test_foundation_check -k comma -k joined` | 1 | 7 ran, FAILED (failures=11). Red for the right reasons: the bare cases passed silently (exit 0, no message); the described-after-comma cases printed "is no identifier of a fact" and lacked the new message. `test_a_described_todo_first_or_after_a_dot_joined_item_stays_as_before` passed on base, as it is a guard test. |
| 3 | New tests after the fix | same command | 0 | 7 ran, OK (before the quoted-comma test was added) |
| 4 | Focused suite after the fix, final | `python -B gate/run_tests.py elements/common` | 0 | 242 tests, OK (235 + 7) |
| 5 | Real foundation, after the fix | `python -B elements/common/foundation_check.py` | 0 | `0 errors`, one `listed:` line that is no error |
| 6 | Hostile-input probe (57 runs: 19 values × 3 fields), first version | a scratch script running the check on crafted values | 1 (traceback) | 6 runs crashed with `AttributeError` in `known_part` for `TODO,` and `TODO·TODO` in all three fields |
| 7 | Hostile-input probe, after the fix | same script | 0 | 0 crashes; every run exit 0 or 1 without a traceback |

The full gate was not run (WAY-160), as the handoff says.

Not run: the whole suite of the-way beyond `elements/common` (outside the slice's Checks).

## Own-work check (section 3)

- **Requirement:** a crafted field value cannot make the script crash with a stack trace, write outside its places, run a command, or put input text unescaped into a result; a bare `TODO` after a comma or a line break is reported, not passed; a described `TODO` after a comma gets the joined-by error, not "is no identifier".
- **Check:** check 6 (hostile values, all three fields, including the line-break forms, quoted `TODO` and `·`), plus tests 1–5 of the table.
- **Showed:** check 6 first run crashed on `TODO,` and `TODO·TODO`. Cause (verified by the traceback): `TODO_VALUE` requires the word to end at whitespace, a backtick or the end of the value, so `todo_item` matched the piece `TODO` but `known_part`, matching the full value, got `None`. Fix: `todo_item` now matches `TODO_VALUE` against the full value at the piece's first character. Check 7 after the fix: no crashes. The script's own output is UTF-8 text from the foundation; no subprocess or write was added.
- Mutations thought through (not run as separate edits): dropping the comma from the split fails the comma tests; dropping `\n` fails the line-break tests; removing the joined branch fails the described tests; removing the bare branch fails the bare tests; always erroring on a non-empty prefix fails the existing `clock-tick · TODO …` tests (they still pass).

## Choices made

1. **New message for the joined-by case.** The plan says the described-after-comma case should get "the error that says the items of the field are joined by ` · `". Searching the code, the tests and the spec for such a message found nothing (`grep` for "joined by" hits docstrings only). I wrote one. Rejected: accepting the described-after-comma case silently, which would drop the error the goal requires. Cost if wrong: a product value of the form `clock-tick, TODO — …` now fails with the new message; before it failed with "is no identifier", so no new kind of failure.
2. **A line break is treated like a comma for the described case.** The goal names only the comma. Reason: the field parser already splits items on a line break (`ITEM` in the module). Rejected: keeping the line break as before. Cost if wrong: a wrapped value (`clock-tick`, then a line break, then `  TODO — x`) errors now with the new message; it errored before with "is no identifier", so the fail/pass result is unchanged.
3. **The decision line in the test.** The line at test file line 1500 cited `A change whose check lists such an invariant`, which the test does not check (the test checks that a citing file that changed stops the listing, i.e. the "when no file that cites it has changed" condition of the sentence). It now cites `The check of the foundation lists an invariant whose method`, the same sentence its neighbours cite, and whose wording appears in WAY-03 (`decisions.md` line 1635). Rejected: removing the line, which loses the traceability. The test itself is unchanged.
4. **Matching `TODO_VALUE` against the full value in `todo_item`** (the crash fix above). Rejected: changing the word rule `TODO_VALUE` so that `TODO,` counts as the word — that changes how the rest of a field is read, outside the slice.
5. **Module docstring sentence added** (about lines 47–50), so the documented rule matches the code.

## WAY-03 — the changed test (named for the request)

- Test: `test_reworded_sentence_with_its_citing_file_changed_is_not_listed` in `elements/common/test_foundation_check.py`, decision line at line 1500.
- Before: `# decision: WAY-03 "A change whose check lists such an invariant"`.
- After: `# decision: WAY-03 "The check of the foundation lists an invariant whose method"`.
- The test body is unchanged. The sentence it now cites is the one the test checks; the old one is not checked by it.
- The other decision-line tests (lines 1493–1534, 1541–1561) are unchanged.

## Foundation entries and files read beyond the handoff

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`, whole (the method).
- `.ai/rules/scripts.md` and `.ai/rules/git.md` (the user's rules, read as the hooks required before a script and a commit).
- `foundations/decisions.md` lines 1628–1673 (WAY-03), 2545–2570 (WAY-38) and `foundations/invariants.md` 116–145, as the handoff names them; a grep found the WAY-03 sentence at line 1635.
- The plan text of slice 12 was not read beyond the handoff's copy.

## Unread material

- `.runs/task-cycles/scripts-after-foundation-review/task.md` lines 39–40, 96–100, 106, 127: read as the handoff gives them (ranges printed). Not read: the rest of the task.
- `plan.md` and `spec.md`: not opened; the handoff's copy of slice 12 was used.
- `foundations/decisions.md` WAY-03 and WAY-38 were read as the handoff ranges; no other part of them.
- `foundations/invariants.md` 116–145: read as named.

## Searches not found or unclear

- "the error that says the items of the field are joined by ` · `" (plan, slice 12 Goal, and the finding G3 #97-1 in `task.md`): not found in `elements/common/foundation_check.py`, `test_foundation_check.py`, or the spec and plan; the finding's sentence reads as if that error were the current one, while the code gives "is no identifier of a fact". Resolved by choice 1; the plan's wording is ambiguous and should be checked by the reviewer.
- A `TODO,` with a trailing comma (`clock-tick, TODO,`, `clock-tick · TODO,`) is not read as the `TODO` word by the rule of `TODO_VALUE` and passes silently in `Rests on`, `Derives from` and `Based on`. Confirmed by probe 6/7 (`TODO,` exit 0 in all three fields, after the fix). By reading the code, not by running base, the same happens before the change. Not fixed: it is outside the slice (changing the word rule changes how the rest of a field is read). Reported for the orchestrator's decision.
- The quoted-comma test (`test_a_comma_or_a_todo_inside_quotation_marks_joins_and_begins_nothing`) was added after the red run and was not run on base.

## Own work for the reviewer

- The line-break split was checked only on indented continuation lines (`\n  TODO`), which is how the parser reads a continuation. An unindented `\n` ends the field, so it is not a case here.

## Working copies

- `.runs/executor-12` — my scratch directory: `probe.py`, `probe-out.txt` (red and fixed probe of 12 values in three fields), `probe2.py`, `probe2-out.txt` (hostile-input probe, 57 runs), `baseline-elements-common.txt`, `after-elements-common.txt`, `real-foundation-after.txt`. Removed after this report was written; the outputs that the report needs are in the table above. No worktree or clone was made.
