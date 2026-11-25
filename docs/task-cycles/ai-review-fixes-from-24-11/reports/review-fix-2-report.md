PASS b87125b6ae03b2a36fc66f80927758dac876f45e

# Review of fix 2 — ai-review-fixes-from-24-11

Range: `2dca687367fb016839219488d08511ddf83e8e11..b87125b6ae03b2a36fc66f80927758dac876f45e`, one
commit (`b87125b6`) by the one author. `git rev-parse HEAD` in the reviewed worktree is `b87125b6…`,
the head given. Bounded by `reports/review-whole-2-findings.md` (I-1, I-2 blocking; M-1, M-2 Minor
within the task). No plan, no slice.

Counts: blocking 0; Minor 0 remaining, 0 new; out of scope 0.

## The findings

**I-1 — fixed.** `elements/common/foundation_check.py:813-814` now keys the decisions' texts by
`int` of the number in the heading (`entry_texts(..., key=int)`), and the comparison at `:844-846`
looks the decision up by the loop's integer `key`, the value `self.bodies`, `base_paragraphs` and
`check_held` use; the message keeps the two-digit label, as `check_held` does. Evidence: the new
test `test_decision_whose_number_is_written_without_a_leading_zero_is_compared_as_changed`
(`elements/common/test_foundation_check.py:2498-2504`) reproduces my probe's case (heading
`### ABC-1 —`, old gap, only the decision's rationale changed) and expects the error line and
`1 error`; it passes on `b87125b6` and fails with the script of `2dca6873` put back in a worktree of
the fix (below). A heading padded otherwise (`ABC-007`) is covered by the same `int` key.

**I-2 — fixed.** WAY-12's *Rejected* (`foundations/decisions.md:828-836`) keeps, of what the cycle
added, only Question 2's way not chosen ("an error only where the *Derives from* of the invariant or
the *Verification* of the decision changes — …"); "the link … left to the skill … with no check" and
"an error for every such invariant" are gone. WAY-30's *Rejected* (`:1335-1341`) keeps only
"approval before the code for each line …" (Question 1's way that differs in the rule itself);
"the approval left to the merge with no sentence saying so …" is gone. The orchestrator's ruling
agrees with the finding and I hold it right. The *Rationale* additions of both decisions stay: they
argue for the chosen rule, not for a dropped option, and still read true; WAY-134 bounds *Rejected*,
not *Rationale*.

**M-1 — fixed.** `check_linked` skips an invariant whose identifier has no unversioned heading
(`name not in now[INVARIANTS]`, `foundation_check.py:824`), so `## save-keeps-name/2` is left to the
earlier-form error, as the docstring says. Evidence: the new test
`test_invariant_of_the_earlier_form_with_a_version_is_left_to_the_check_of_fields`
(`test_foundation_check.py:2506-2513`) expects exit 1, the earlier-form error, `1 error` and no
"derives from"; it passes on the fix and fails on the script of `2dca6873`.

**M-2 — fixed.** WAY-30's second paragraph now ends "and the agent making it asks that human no
question about it." (`foundations/decisions.md:1304`).

## What the dispatch asked besides

- No binding sentence of a decision changed beyond M-2's two words: the diff of
  `foundations/decisions.md` touches WAY-12's *Rejected*, WAY-30's second paragraph (M-2) and
  WAY-30's *Rejected*, nothing else.
- WAY-12's *Verification* `tests:` clause and WAY-30's pair of examples are outside the diff and
  stand as they were.
- New Critical or Important finding in the fix diff: none. I read the changed code for what it might
  break: `entry_texts` keeps its old behaviour by default (`key=str`) and has no other caller; the
  versioned decision heading `### ABC-01/2 — …` still matches neither pattern; a log with both
  `## x/1` and `## x` still reads the fields `read_named` kept first, as before the fix (not raised:
  outside the fix's reach and unchanged by it). The script stays at 1193 lines.
- New Minor finding: none.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD`, `git log --oneline 2dca6873..b87125b6`, `git diff 2dca6873..b87125b6` —
  exit 0; head matches.
- `python -B elements/common/foundation_check.py` in the reviewed worktree — `0 errors`, no
  `listed:` line, exit 0.
- In a worktree of `b87125b6`: `python -B -m unittest -k leading_zero_is_compared -k
  earlier_form_with_a_version elements.common.test_foundation_check` — `Ran 2 tests … OK`, exit 0;
  the same command with `elements/common/foundation_check.py` replaced by `git show
  2dca6873:elements/common/foundation_check.py` — `FAILED (failures=2)`, both new tests, exit 1;
  the file restored with `git checkout --` afterwards.
- In the same worktree: `python -B gate/run_tests.py elements/common` — `Ran 316 tests … OK`, exit 0;
  `python -B gate/run_tests.py agent-instructions` (size, formatter and linter invariants) —
  `Ran 53 tests … OK`, exit 0.
- `the pinned Ruff of the main checkout's quality virtual environment format --check --config ruff.toml
  elements/common` — `13 files already formatted`, exit 0; `… ruff.exe check --config ruff.toml --ignore-noqa
  elements/common` — `All checks passed!`, exit 0.
- `wc -l elements/common/foundation_check.py` — 1193 (threshold 1200).
- The full gate was not run (the cycle's own run).

Changed invariant tests: none; the fix adds two tests carrying lines `decision: WAY-12`.

## Reach beyond the dispatch

none

## Working copies

- `.runs/review-fix-2/head` (worktree of
  `b87125b6`) and `.runs/review-fix-2/`
  (test outputs): the worktree removed with `git worktree remove --force` (exit 0), then `git worktree prune` (exit 0), and the directory removed (exit 0). No remainder.

## Unread material

none — the findings file, the fix report, the handoff and the whole fix diff were read whole;
WAY-12, WAY-30 and WAY-134 were read whole in the review of the whole change and their changed parts
again here.

## Searches not found or unclear

none
