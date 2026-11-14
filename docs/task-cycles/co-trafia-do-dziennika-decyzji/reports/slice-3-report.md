# Report - executor of slice 3

## Status

done

## Commits and files

- `ea2d1862a888e643eb5c598bfb9e10ab635ee73e` "Report decisions that nothing holds in the foundation check" (range `269fecc..ea2d186`).
- `elements/common/foundation_check.py`: +61 / -1 (docstring paragraph for the report, `headings` map, `base_sentences`, `held_by_pair`, `check_held`, one call in `run`).
- `elements/common/test_foundation_check.py`: +156 / -0 (section "a decision that nothing holds", 20 tests).
- Worktree clean after the commit.

## What was made

`check_held` runs in `run()` after the loop over tracked files (so `self.held`, the map of numbers named by `decision:` lines, is complete) and before the `--skip-test-citations` branch, which it does not read. A decision (unversioned entry with a *Verification*) is held when: `located(..., VERIFIED)` yields a word not in `none`/`TODO`; or a `decision:` line names its number (valid or stale, matched by integer); or its *Verification* has a line beginning `- complies:` and one beginning `- violates:`. Not held: an error at the heading line when the base is known and the entry is absent at the base or its normalised binding sentences differ (`" ".join(binding(body))`, both sides); otherwise a `listed:` line at the heading. Unknown base or base lacking `foundations/decisions.md`: `base_sentences` returns None, so only listing. Earlier-form entries (no unversioned heading, so no `bodies` entry) and entries without *Verification* are skipped. Surface unchanged: no new argument, switch or exit code.

## Checks

- Red, before the code: `python -B -m unittest elements.common.test_foundation_check` exit 1 (the command was piped through grep, so the exit code of the pipe was 0 and the failures were read from its output): 170 ran, 11 failed, each at an assertion (exit code 0 where 1 was expected, or the `listed:` line absent): `test_new_decision_that_nothing_holds_is_an_error`, `test_new_decision_naming_no_invariant_after_invariants_is_not_held`, `test_new_decision_with_only_one_half_of_a_pair_is_not_held`, `test_line_decision_in_a_markdown_file_holds_nothing`, `test_decision_whose_binding_sentence_changed_and_none_held_is_an_error`, `test_decision_with_only_its_rationale_changed_is_listed`, `test_decision_with_only_its_spacing_changed_is_listed`, `test_old_decision_that_nothing_holds_is_listed_after_the_errors`, `test_decision_that_nothing_holds_is_listed_where_the_base_is_unknown`, `test_decision_that_nothing_holds_is_listed_where_the_base_lacks_the_log`, `test_skip_switch_skips_nothing_of_the_decisions_nothing_holds`. The same run through `python -B gate/run_tests.py elements/common` (output tail cut) also showed 11 failures of 189 tests.
- Tests that pass before the code only because the old script reports nothing of this (they guard the other direction, so they matter after the code): the three "held by an invariant / pair / line" tests, `test_new_decision_held_by_a_stale_line_decision_is_reported_once`, `test_decision_whose_binding_sentence_changed_and_held_passes`, `test_entry_lacking_its_verification_is_left_to_the_check_of_fields`, `test_entry_of_the_earlier_form_is_left_to_the_check_of_fields`.
- Green: `python -B gate/run_tests.py elements/common` exit 0 (189 tests, OK).
- `python -B gate/run_tests.py elements/part-map` exit 0 (39 tests, OK).
- `python -B elements/common/foundation_check.py` on this repository: exit 0, one `listed:` line (WAY-17, `decisions.md:578`), `0 errors`. Here the base is unknown (no remote HEAD, `main` or `master` in this checkout), so no decision counts as changed.
- Extra: `installation.test_install` `test_empty_foundations_have_valid_form` run alone, exit 0 (the constraint of the spec on a repository with no commit and an empty log).

## Own-work check

Requirement most likely not met: "the foundation of the-way itself passes: every decision the task edits stays held", which the check above cannot show because the base is unknown here. Check: a clone in the scratchpad, branch `main` set to `ac75340` (the commit before the foundation step), `origin/HEAD` removed, the new script copied in, the script run: exit 0, one `listed:` line (WAY-17), `0 errors`, so the 13 edited decisions stay held with a known base. Negative control in the clone: the *Verification* of WAY-22 reduced to one sentence with no pair: `1 error`. The clone is outside the worktree (scratchpad); no ref of the real repository was touched.

## The `decision:` lines of the tests

The tests carry real comment lines, each a quotation checked against the entry as it stands: `WAY-12 "The check of the foundation reports as an error"`, `WAY-12 "A decision is held when its"`, `WAY-12 "Any other decision that nothing holds stands"`. `test_the_way_foundation_passes` (in the green run of `elements/common`) reads them and accepts them. The test products inside strings put the `decision:` text in one-line strings with `\n`, so none is read as a citation of the test file.

## Choices

- Held by an invariant means a name after `invariants:` that is not `none` or `TODO` (a value `invariants: none` holds nothing); an invalid or withdrawn name still counts as held, since the existing reference check reports it. Rejected: counting any match of the pattern, which would let `invariants: none` hold. Cost if wrong: a decision with `invariants: none` becomes an error when new.
- A `decision:` line holds by integer number, so `WAY-5` holds `WAY-05`, as the existing reference check reads numbers.
- Messages: error "`ABC-03` is added or changed by this change and nothing holds it: ..." and listed "`ABC-03` is held by nothing: ...". The tests assert the path, line and the number in backquotes, not the whole wording.

## Concerns

- A *Verification* of `TODO` (which the existing check of fields rejects) is not left out: for a new decision it gives a second report (not held), since the spec leaves out only entries of the earlier form and entries with no *Verification*. One more error line in the case; left as the spec has it.
- With a known base, the real log's ~old unheld decisions are listed; in the-way's own log that is WAY-17 only today.

## Reaches beyond the dispatch

none

## Unread material

- `.runs/.../task.md` To do 7 and Question 5 and `spec.md` Constraints, D2, D3, D8, D9: read whole in the ranges given (I read task.md 38-77 and spec.md 27-156).
- `foundations/glossary.md:13-23`, `foundations/invariants.md:156-164`, `foundations/part_map.md:65-75` and `:215-219`: not read; the slice changes no part, invariant or glossary term and the script's code carries what the check needs.
- WAY-05, WAY-19, WAY-22, WAY-321, WAY-344: read at the lines given (WAY-05 and WAY-19 and WAY-22 from their start, to about the *Rationale*; WAY-344 whole; WAY-321 whole); only the parts up to *Rationale* of WAY-05, WAY-19 and WAY-22.

## Searches not found or unclear

none
