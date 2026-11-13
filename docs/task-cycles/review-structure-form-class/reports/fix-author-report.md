# Fix author report — review-structure-form-class

**Status:** done. Every finding of `fix-findings.md` is fixed; none is contested.

Fix range: `5353268..c6af26a`. Commits:

- `a47195b` I1, M1, M2 (`foundations/decisions.md`, `product-guidelines/coding/template.md`, `settle.md`, `trial_run.md`)
- `cd54d5a` M3, M4 (`product-guidelines/audit_end.md`, `task-cycle/review/whole_change.md`)
- `c6af26a` M5 (`task-cycle/change_file_sizes.py`, `task-cycle/test_change_file_sizes.py`)

## Findings

**I1 — fixed.** WAY-355 is edited in place (WAY-07). What each place says now:

- WAY-355, binding sentence 3 (`foundations/decisions.md`): "Where code other than the exceptions of the product's decision
  stands over a threshold, the rule's invariant is marked violated until that code is cleaned (WAY-51)."
- `template.md`, the rule's *Invariant* bullet: "Where code other than those exceptions stands over a threshold when the rule
  enters, the invariant is marked violated until that code is cleaned (WAY-51)".
- `settle.md`, two places: the meaning of a threshold ("where code other than the exceptions is already over, the invariant stands
  marked violated until that code is cleaned") and the invariants bullet ("where the trial run found code over a threshold that the
  exceptions, settled before this, do not name, it is marked violated by a change of the foundation the human accepts, until that
  code is cleaned").
- `trial_run.md`: "Once the exceptions are settled, where code they do not name stands over a threshold, step 4 proposes the rule's
  invariant marked violated (WAY-51)."

All four agree with the rule's invariant ("other than those the decision's exceptions name") and with WAY-355's *Verification*
("marks the rule's invariant violated where other code stands over"), which I left as it was. The order that settle.md asks in
(thresholds, exceptions, invariants) is what makes "settled before this" true. The finding's fix in kind, taken as given.
Check: a scripted scan of the four texts for each sentence that holds "marked violated" with a threshold printed exactly these
five sentences, each with the exceptions' qualification (own-work check below).

**M1 — fixed.** WAY-359 *Rationale* now reads "… rejected the change for its form alone (the conditions of the measurement stand in
WAY-229), so the verdict depended on the run." The reviewer is right that the task ties the form experiment to the one of WAY-229
(the same report); I had held it undecided.

**M2 — fixed.** `template.md` now says "It is none of the three standing checks (WAY-202) and no rule of the linter's set" in the
list of required forms, and "It is none of the three standing checks, and the linter's set holds no rule of it" in the section on
the rule, so the glossary's meaning of the term stays whole.

**M3 — fixed.** `product-guidelines/audit_end.md`, "Whether this audit stops": the sentence now names both checks, "the check of the
required headings of the rules on failures and logs and of the rule of size, with the questions to the human they bring at a refresh",
as `product-guidelines/coding/SKILL.md` does.

**M4 — fixed.** `task-cycle/review/whole_change.md`: "Take your numbers from two runs of your own, the first in the reviewed
worktree, which it changes in nothing, and the second in separate worktrees." The script's test
`test_the_command_changes_nothing_in_the_repository` backs the first half.

**M5 — fixed.** Three new tests: `test_a_file_that_becomes_a_symbolic_link_is_a_type_change_measured_on_both_sides` (status `T`,
note `type changed`, built in the index with `update-index --cacheinfo`, so it needs no symlink privilege on Windows),
`test_a_bar_in_a_name_is_escaped_so_that_the_row_keeps_its_cells` and
`test_a_backtick_in_a_name_gets_a_longer_delimiter_and_a_padded_edge`. The backtick was simple to fix: a new `code_span` in
`change_file_sizes.py` fences a name with a delimiter one backtick longer than the longest run in it and pads an edge that is a
backtick (`` `` `lead.md `` ``), and escapes `|`; the rename note uses it too (`Entry.renamed_from` replaces the old text note).
Each of the three behaviours was broken on purpose and the matching test failed: no `|` escape, fence not longer, no padding, the
note `type changed` dropped (4 breaks, 4 failing tests, restored and compared with `cmp`).

## Checks (command, exit code)

- `python -B -m unittest discover -s task-cycle -p "test_change_file_sizes.py"` — OK, 18 tests.
- `python -B gate/run_tests.py task-cycle` — exit 0, 383 tests.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B task-cycle/private_paths_check.py <file>` — each of the 8 changed files, exit 0.
- `python -B gate/run_tests.py instruction-files` — exit 0; `python -B gate/run_tests.py agent-instructions` — exit 0.
- `python -B agent-instructions/skill_entry_points.py` — exit 0 (no description changed).
- Not run: the whole gate, as the handoff says.

## The own-work check

- **Requirement most likely unmet:** I1 reaches four places and one more is easy to miss (settle.md has two sentences).
- **Check:** a script scanned WAY-355 (the entry only), `template.md`, `settle.md` and `trial_run.md` for each sentence with
  "marked violated" about a threshold or size.
- **Result:** five sentences found, all with the exceptions' qualification; none without. (A first idea, a grep for "marked violated"
  alone, would also have hit the linter's lines, which this fix does not touch.)

## Unread material

none (`fix.md`, the findings file and the fix handoff read whole; the reviewer's full report was not needed and not read).

## Searches not found or unclear

none.
