# Author fix report — relations-todo-for-unwritten-decision

**Status:** done

**Commit:** `68d8645` (on `452f123`, the reviewed head). Not pushed.

Files (from `git diff --numstat 452f123 68d8645`):
`elements/common/foundation_check.py` 25 / 18, `elements/common/test_foundation_check.py` 29 / 0,
`elements/decisions/template.md` 2 / 1, `foundations/decisions.md` 7 / 6 (WAY-71 and WAY-126 only).

## Findings

**I1 — fixed.** In `foundation_check.py`, `todo_item(value, typed=False)` now also treats an item
that begins with `derives from` or `narrows` followed by the word `TODO` as a `TODO` item (new
`TYPED_TODO` pattern), and only for *Relations* (`known_part` passes `typed=name == "Relations"`).
`known_part` reports it first, with one message whatever follows the word:
`*Relations* reads `TODO` after a relation type: the `TODO` item takes no `derives from` or
`narrows`; write `TODO — <the decision, and where it is expected>``. The value is cut at that item,
so a decision number in its description is no longer reported as a reference. Docstring, the sentence
of `elements/decisions/template.md` ("The script reports a bare `TODO` in *Relations*, a `TODO`
behind a relation type (`derives from TODO`), and any `TODO` in *Origin*") and WAY-71's *violates*
line (`Relations: derives from TODO`) changed together.
Tests, written first (see below), four for the four forms of the finding:
`test_relations_a_bare_todo_behind_a_type_is_an_error` (`narrows TODO`, `` narrows `TODO` ``,
`derives from TODO —`), `test_relations_derives_from_todo_is_an_error`,
`test_relations_a_known_relation_then_derives_from_todo_is_an_error` (`derives from ABC-01 · derives
from TODO`), `test_relations_a_described_todo_behind_a_type_is_an_error_not_a_reference` (with and
without a known relation before; the description holds `ABC-77` and the report must hold only the
form error, "1 error"). Each asserts the message at line 22, which says what is wrong. The break each
catches: the item behind a type is read as a plain relation and passes (a bug). Test first: on the head
`python -B -m unittest elements/common/test_foundation_check.py -k relations` -> `FAILED (failures=7)`
(all assertion failures, 11 tests ran); after the fix the same command -> `OK` (11 tests).

**M1 — fixed.** WAY-126's new paragraph now reads "A change that writes a projected entry into the
foundation replaces each descriptive `TODO` that points at it with a reference to it by its
identifier: in a decision's *Relations* as `derives from <number>`, and in an invariant's *Derives
from* as the number." Its complying example says the same (`derives from <its number>` / its number).
The violating example was left as it was (it names the `TODO` left standing, which holds either way).

**M2 — fixed.** `test_relations_a_decision_on_a_second_line_is_still_checked`: a *Relations* value
over two lines, `derives from ABC-01 ·` and `  narrows ABC-77`, no `TODO`; expects
`foundations/decisions.md:23: `ABC-77` names no decision of the log`, 1 error. The break it catches:
the check of the known part reads only the first line (a bug). The test passes on the head (the
behaviour was right, as the finding says), so I broke the code for a moment (`zip(lines[:1], ...)` in
`check_foundation_references`), ran `-k relations` -> `FAILED (failures=1)`, this test only, and
restored the file before the commit.

**M3 — fixed.** The docstring paragraph of `foundation_check.py` around line 49 is rewrapped to 100
columns (the new sentence for *Relations* included).

## A choice

The first version of the fix put `foundation_check.py` at 1004 lines, over the 1000-line file threshold
of WAY-385 (it stood at 992 after the first commit). I did not cross it: I shortened my own additions
(docstring wording, one comment dropped, the message on fewer lines); the file now has 999 lines. Rejected:
a move of part of the file out (a larger change than three Minor findings ask). Cost if wrong: the file is
one line under the threshold, so the next addition needs a move first (WAY-365).

## Checks (command, exit code)

- `python -B gate/run_tests.py elements/common` — 0, 257 tests OK (252 before, plus the 5 new).
- `python -B elements/common/foundation_check.py` — 0, `0 errors`.
- `python -B gate/run_tests.py product-guidelines` — 0, OK (it reads skill and template texts).
- Not run: the full gate (the orchestrator's alone, WAY-160); `task-cycle` (no file of it touched);
  `ruff` (not installed here; the lines I added hold no unused name or noqa).

## Own-work check (WAY-164)

Requirement most likely not met: a bare `TODO` in *Relations* is reported as an error whatever form it
stands in. Check on the real log: WAY-71's *Relations* line set in turn (the file kept aside and
restored after each), then `python -B elements/common/foundation_check.py`:
- `derives from WAY-01 · derives from TODO` -> the type message at `foundations/decisions.md:617`, 1 error;
- `derives from TODO` -> the same, 1 error;
- `derives from WAY-01 · derives from TODO — WAY-9999, expected later` -> the same message, 1 error (not
  `WAY-9999 names no decision`);
- `derives from WAY-01 · TODO — WAY-9999, expected later` (the right form) -> `0 errors`.
The file was restored; final run `0 errors`, and `git diff` of the log shows only the WAY-71 and WAY-126
edits above.

## Reach beyond the dispatch

None beyond the findings file and the handoff; I read `task-cycle/change/fix.md` (the fix variant) and
the lines of `foundation_check.py` I changed. I did not read `reports/review-whole-report.md`: the
findings file holds each finding whole, and none points at the report for what I needed.

## Unread material

`reports/review-whole-report.md` (not read; findings file read whole). M4 and M5 are not in the findings
file and were not touched. Nothing else named in the handoff was left unread.

## Searches not found or unclear

None. (A search of the repository for other places that quote the sentence "a bare `TODO` in
*Relations*" found only the template sentence and WAY-71's *violates* line, both changed.)

## Working copies

`.runs/author/` held my fix scripts, backups of `foundation_check.py` and `decisions.md`, and the test
output; it stood at `.runs/author/`
and was removed (`rm -rf`) before this report. No worktree or clone was made.
