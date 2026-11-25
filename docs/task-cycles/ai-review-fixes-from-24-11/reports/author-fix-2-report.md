# Author fix 2 report — ai-review-fixes-from-24-11

**Status:** done

**Commit:** `b87125b6` on `task/ai-review-fixes-from-24-11` (range from the reviewed head `2dca6873`): `elements/common/foundation_check.py` (+8 −6 approx.), `elements/common/test_foundation_check.py` (+19), `foundations/decisions.md` (+4 −10 approx.). No finding held wrong.

## Fixes

- **I-1 (code).** `check_linked` keys the decisions' texts by `int` of the number in the heading (`entry_texts` takes a `key` function, `int` for the decisions, `str` for the invariants) and looks the decision up by the same integer as `base_paragraphs` and `check_held` do; the message still names the decision by the two-digit label. File stands at 1193 lines (unchanged, under 1200).
  - Test `test_decision_whose_number_is_written_without_a_leading_zero_is_compared_as_changed`: the log writes `### ABC-1 —`, an old gap, and only the decision's rationale changes; expects the error line and `1 error`.
  - Seen failing before the code fix: `python -B -m unittest -k "leading_zero_is_compared" -k "earlier_form_with_a_version" elements.common.test_foundation_check` → exit 1, `FF`; the first test failed with `0 != 1 : foundations/decisions.md:10: listed: \`save-keeps-name\` derives from \`ABC-01\` … 0 errors`, as the reviewer's probe showed. After the fix the same selection (with the other new tests) passes: `Ran 20 tests … OK`, exit 0.
- **M-1 (code).** `check_linked` skips an invariant that is not in the texts keyed by unversioned heading (`name not in now[INVARIANTS]`), so `## x/2` is left to the earlier-form error, as `invariant_entries` does. Test `test_invariant_of_the_earlier_form_with_a_version_is_left_to_the_check_of_fields`: expects exit 1, the earlier-form error for `save-keeps-name/2`, `1 error`, no "derives from"; seen failing before the fix in the same run (the extra `listed:` line was there).
- **I-2 (entries).** Edited in place with the method of `record-decision`; no binding sentence changed; WAY-12's *Verification* and WAY-30's pair untouched.
  - WAY-12 *Rejected*: only "an error only where the *Derives from* of the invariant or the *Verification* of the decision changes — it leaves the gap where someone changes the decision and should see what stands on it" (Question 2's way not chosen) remains of what the cycle added; the options "the link left to the skill with no check" and "an error for every such invariant" are dropped. WAY-12's *Rationale* addition (the link written at both ends; the error stands where a change touches either entry; older gaps wait in the list) argues for the chosen rule, not against a dropped option, and reads true as it stands, so it is unchanged.
  - WAY-30 *Rejected*: kept "approval before the code for each line that names a derived invariant in a decision's *Verification* — a cycle without a plan stops at every new rule derived from an existing decision, for one mechanical line" (Question 1's way a); dropped "the approval left to the merge with no sentence saying so …". The *Rationale* sentence added on the same point argues for the line needing no approval before the code, the kept option's reverse, and stays true.
- **M-2 (entry).** WAY-30's new sentence now ends "and the agent making it asks that human no question about it."; the paragraph is still two sentences, far under the limits of WAY-05.

## Own-work check

Requirement most likely unmet: the error where the change alters a decision whose heading writes the number other than as two digits, and no double report for a versioned invariant. Checks: the two new tests above (failing, then passing) and `python -B elements/common/foundation_check.py` on the finished change.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0, no `listed:` line.
- `python -B gate/run_tests.py elements/common` → 316 tests OK, exit 0.
- `python -B gate/run_tests.py agent-instructions` → 53 tests OK, exit 0 (size and formatter invariants; `foundation_check.py` 1193 lines).
- `ruff format --config ruff.toml elements/common` → 13 files left unchanged; `ruff check --config ruff.toml --ignore-noqa elements/common` → all checks passed, exit 0 (Ruff of the main checkout's `.runs/quality-venv`).
- The full gate was not run.

## Reach beyond the handoff

none. The probe files `review-whole-2-probe-linked*` were not opened: the findings file describes the cases, and the two new tests reproduce them.

## Unread material

The review report `reports/review-whole-2-report.md` and the probe files named by the handoff: not read; the findings file was read whole and its two cases were reproduced by the new tests.

## Searches not found or unclear

none.

## Working copies

`.runs/author/` held the output files of the test runs; removed by its full path.
