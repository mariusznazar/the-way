# Author report — the fix of the review of correction 2 (I-1, I-2)

**Status:** done

**Range:** `17065c8b9b2349b4f5953ac98a15285e3d221787..` the one commit of this fix (`5a39a328`; `git rev-parse HEAD` in the worktree gives it). No line of code changed: the syntax trees of `process-audit/record_items.py` and `process-audit/audit_count.py` with docstrings left out equal those at `17065c8b` (checked by the same comparison as in the report of correction 2).

**Files:** `foundations/decisions.md`, `process-audit/audit_count.py` (docstring), `process-audit/record_items.py` (docstrings), `process-audit/test_record_items.py`.

## I-1 — fixed (wording of five places and the test that cited a sentence it did not hold)

I took the finding's way: the rule says what `discarded_reason` does, which counts `reason: ` **followed by a backtick**, whatever word stands in the backticks.

- WAY-405, binding sentence: "gives the answer unknown unless it reads `none` or opens with `reason: ` and one marker and holds no second `reason: ` followed by a backtick (WAY-404); its later lines are details of that attempt, read for such a second `reason: ` alone, whatever word stands after the backtick, so that a second attempt written in them with no backtick after the `reason: ` or with its reason in other words is not read."
- WAY-405, *Verification*: "unknown where it holds a second `reason: ` followed by a backtick, a word that is no marker included, or opens with no marker, and gives its reason where it opens with one marker and holds no such second one, its later lines possibly a list of details, read for that second `reason: ` alone".
- `process-audit/audit_count.py` docstring (both places: the details, and the list of the reasons of unknown) and `process-audit/record_items.py` (module docstring, `discarded_reason` and `discarded_reasons`) say the same.
- The test is renamed `test_a_later_line_is_a_detail_unless_it_holds_a_second_reason_opening_in_backticks` (it held more than "no marker"); its comment now states the form that counts as a second reason; its subtests add probes B3 (`  - reason: \`budget\`; 14:05` after a plain first attempt gives `unknown` with the reason of more than one reason), the same after a `reserved choice` first attempt, and B4 (`reason: \`size\`; reason: \`budget\`` on one line gives `unknown`; `reason: \`size\`; reason: open design choice` gives `no`). The citation, "Where the lines under the item are not entries at one indent alone", now holds: that sentence says it.
- Check that shows it: the foundation check, 0 errors; `python -B -m unittest test_record_items` in `process-audit`, exit 0, 36 tests. Mutations of the code in the worktree, restored afterwards: counting only the three markers as a second reason, and counting `reason: ` with no backtick, each fail that test alone (exit 1).

## I-2 — fixed (WAY-404's *Verification* qualified, and the test)

Of the two ways, I took the qualification, in one clause: "yes where an entry carries the mark of a contradiction or the record holds the item once and it gives the marker `open design choice`, so that a yes stands over an unknown of any other part of the record, save that the marker does not stand over a doubled item, over which the mark of an entry alone stands, ... unknown where an entry carries no mark or the item is doubled and no yes stands". It says what `read_contradiction` does (probes C1 to C3 of the finding). The test is renamed `test_a_yes_stands_over_an_unknown_but_the_marker_not_over_a_doubled_item`: its records now include a doubled item with a marked-`yes` round (gives `yes`), and the doubled item with the marker `open design choice` beside rounds `none`, unmarked and marked `no` (each gives `unknown`, "the record holds the item `Discarded attempt` more than once"). A mutation that lets the marker stand over a doubled item (the item count read as "at least one") makes that test and `test_a_missing_or_doubled_item_gives_unknown_with_its_reason` fail.

## Other places that say the same wider or narrower sentence

Searched (the `.runs/` directories apart): `second marker`, `second \`reason`, `two markers`, `holds no other`, `whatever else the record holds` in `foundations/decisions.md`, `process-audit/*.py`, `process-audit/SKILL.md`, `task-cycle/*.md`, `task-cycle/skill/`, `task-cycle/review/`. The hits are the five places fixed above and `discarded_reason`/`discarded_reasons` docstrings of `record_items.py` (fixed). `process-audit/SKILL.md:226-231`, `task-cycle/record_template.md` and `task-cycle/skill/*.md` do not state which second reason is read or which yes stands over which unknown; nothing to change there.

## Not done, as the handoff says

M-1 of the review (the Minor finding) is not fixed; no code changed; nothing beyond I-1 and I-2.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B -m unittest test_record_items` in `process-audit` — exit 0, 36 tests.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 276 tests in 400.094s`, `OK`.
- `python -B gate/run_tests.py task-cycle` — exit 0, `Ran 534 tests in 101.743s`, `OK (skipped=2)`.
- Not run: the product's full gate (by the handoff); `ruff` (not installed here).

## The own-work check

- **Requirement most likely unmet:** WAY-263 — every restatement says what the code does, no wider and no narrower — now for the two places the review found wrong, and for any other place that restates the same.
- **Check:** probed the code at `17065c8b` for the shapes of the findings (B1 to B4, C1 to C3) and read each answer against the new sentences; the mutation runs above; the search above.
- **What it showed:** B1, B2 give `no` ("no backtick" is no second reason: the sentence now says so); B3, B4 give `unknown` ("a word that is no marker included"); C1, C2 give `unknown`, C3 `yes` (the clause now says it). The first draft of my edit of the test left a loop body behind; the test module failed to import (`SyntaxError`) and I fixed it before any run of the tests (no run of a failing assertion lost).

## Reaches beyond the handoff

None.

## Working copies

`.runs/author-correction-2-fix/` (`.runs/author-correction-2-fix/`) held the outputs of the two gate runs and was removed before this return. A one-file backup of `record_items.py` for the mutation runs stood for a moment directly under `.runs/` as `ri.bak`, not in my directory (a slip), and was removed in the same command that checked the file was restored.

## Unread material

none — the handoff, the findings file, `fix.md`, `SKILL.md` of the method (as read for correction 2), the passages of WAY-404 and WAY-405 and the three files changed were read.

## Searches not found or unclear

none.
