# Slice 1 report — the line `decision:` read by the check

**Status:** done.

**Commit:** `6440ca9` Check the line decision: of a test against the decision log (`elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`; 162 insertions, 5 deletions). The worktree is clean; no commit was added after `6440ca9`.

## Files changed

- `elements/common/foundation_check.py`: 86 lines changed.
- `elements/common/test_foundation_check.py`: 81 lines added.

## What the slice does

- The script reads, in every run, each comment line `decision: <number> "<quotation>"` in a tracked file other than Markdown (the comment forms of the `invariant:` line).
- It reports, at the line, each error D3 lists: no decision number as the log writes it; a number that names no decision of the log or a withdrawn one; no quotation; text after the quotation; a quotation that stands in no binding sentence of its entry; a quotation that does not begin a sentence; a quotation of fewer than three words.
- Each number named by a line, valid or not, is kept in `self.held` for Slice 3.
- The binding sentences of an entry are read by one helper, `binding(body)`, which Slice 3 reuses. They are the paragraphs before the entry's first field, stopping at `*Rationale:*` or `*Rejected:*`.
- The docstring states the line. The surface is unchanged: path, argument and exit codes stay; no new argument, switch or exit code.
- The WAY-12 quotation `A test that holds a sentence of a decision carries beside it a line` is carried by a `decision:` line in `test_decision_line_quoting_a_sentence_passes`.

## Checks (command, exit code)

1. Red, before the code: `python -B gate/run_tests.py elements/common`, exit 1. Eight of the new tests failed on `0 errors` where an error was expected: `test_decision_line_number_with_a_suffix_fails`, `test_decision_line_quoting_fewer_than_three_words_fails`, `test_decision_line_quoting_inside_a_sentence_fails`, `test_decision_line_quoting_no_sentence_fails`, `test_decision_line_quoting_only_rationale_fails`, `test_decision_line_with_text_after_quotation_fails`, `test_decision_line_without_number_fails`, `test_decision_line_without_quotation_fails`.
2. Five new tests passed before the code, as expected, because the old script already gives their outcome: the good-line test, the wrapped-quotation test, the unknown-number test, the withdrawn-number test, the Markdown test and the untracked-file test. That is six tests; the unknown-number and withdrawn-number cases are both covered by the generic `refer_decisions` check.
3. Green, after the code: `python -B gate/run_tests.py elements/common`, exit 0, `Ran 158 tests … OK`. This run came before the two line-wrap-only edits.
4. Subset after the wrap-only edits: `python -B -m unittest` on the five decision tests that exercise the new code paths, exit 0, `Ran 5 tests … OK`.
5. `python -B gate/run_tests.py elements/part-map`, exit 0, `Ran 39 tests … OK`.
6. `python -B elements/common/foundation_check.py .` on this repository, exit 0, `0 errors`.
7. Final tree, after the wrap-only edits, and the tree clean with no new commit: `python -B gate/run_tests.py elements/common`, exit 0, `Ran 158 tests in 136.498s … OK`.

## Own-work check (WAY-164)

- Requirement: a `decision:` quotation that is reworded or moved to Rationale must be refused, not accepted.
- Check: `test_decision_line_quoting_no_sentence_fails` and `test_decision_line_quoting_only_rationale_fails`.
- Showed: both exit 1 with one error each at the test line (`tests/test_decision.py:2`), as intended. The failure is not repeated; no check failed and then passed.

## Reaches beyond the dispatch

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`, read whole. `slice.md` was read after the code, with no adaptations: no structural mismatch, and the foundation line ranges matched the handoff's current ones.
- The WAY-05 entry (`foundations/decisions.md` lines 156-205), to define "binding sentences".
- The glossary entry "binding sentence".
- `.ai/rules/git.md` and the first 40 lines of `.ai/rules/scripts.md`.
- The withdrawn-decision test fixture in `test_foundation_check.py`, to write the withdrawn-number test.

## Choices

- Binding sentences are the paragraphs before the first field, stopping at `*Rationale:*` or `*Rejected:*`. Rejected: a separate sentence splitter. Cost: a quotation that starts after "e.g. " counts as a sentence start.
- A sentence start is the start of a paragraph or the text after `. `. Quotation and entry are compared with whitespace collapsed.
- Only the unversioned entry's body is used for the quotation check. A number whose only heading is versioned has no body, so its quotation is reported as standing in no binding sentence.
- `self.held` records every `decision:` line with a well-formed number, valid or not.
- Number checks reuse `refer_decisions`, so a withdrawn or unknown number gives the same message as the generic check and is reported once. A wrong-prefix number reports `` `X` names no decision of the log ``.
- The new error messages are my wording. Slice 3 and any wording check will need to match them.

## Unread material

- WAY-61, WAY-65, WAY-321, WAY-344 and WAY-38 in `foundations/decisions.md`: not read; the change does not depend on them.
- `foundations/invariants.md` lines 116-134, 146-154, 156-164 and 328-336; `foundations/part_map.md` lines 65-75 and 215-219: not read.
- `elements/part-map/test_cross_part_imports.py`: not read; its imported names are kept, and the part-map run passes.
- The plan file: not read; the handoff copied the slice.
- `fix.md` and `ui_check.md`: not read; the slice variant does not name them.
- `test_migrate_foundation.py` line 115 has a bare `decision:` inside a string. The real-repo run passes, so it was not checked further.

## Searches not found or unclear

- No tracked non-Markdown file held a `decision:` line before this change, so no existing line needed adapting.
- Nothing else was unclear.

## Concerns

- Five of the nine D9 tests passed before the code (see check 2). The handoff's "each failing before the code" does not hold for them, because the old script already gives their outcome.
- The new error messages are my wording (see Choices).
