# Author fix 2 report — relations-todo-for-unwritten-decision

**Status:** done

**Commit:** the commit "Hold the comma join and the passing form of WAY-71 by a decision line at their tests",
on top of the reviewed head `763af69` (hash in `git log -1` of the branch; not pushed). One file:
`elements/common/test_foundation_check.py`, 2 lines added, none removed.

## I1 — fixed, by way (a)

The finding is right: of the four parts WAY-71's clause `tests:` names, only two tests carried a line
`decision: WAY-71`; the comma join and the passing form after known relations had none, while their
examples had left the pair.

I added a line `decision:` at the two tests the finding names:
- `test_relations_a_known_decision_then_a_missing_one_described_passes` (the passing form after known
  relations), quoting the start of WAY-71's second sentence: "The main branch holds `TODO` only where an
  entry stands on something the product's foundation does not hold yet:" — the sentence that allows the
  form;
- `test_relations_a_described_todo_after_a_comma_is_no_joined_list` (the comma join), quoting the sentence
  already quoted at the two other tests: "`elements/common/foundation_check.py` reports a missing field, or
  a word not given it, as an error."

Now `git grep -n "decision: WAY-71"` finds four lines (`:732`, `:740`, `:761`, `:786` of the test file),
one for each part the clause names: the passing form, the bare `TODO`, the `TODO` behind a relation type
and the comma join.

**Why (a) and not (b).** The clause and the pair were written as the return step gives (a pair kept for a
test of the same change is removed once the test holds the sentence); the tests exist and check these
parts directly, so a line at each makes the entry's *Verification* true as it stands, with two lines and
no change of the entry. (b) would restore two examples to the pair for parts that tests already hold,
leaving a duplicate source for the same behaviour and a clause narrower than the tests. Rejected: (b).
Cost if wrong: the quotation of the first line is a prefix of a long sentence, so the line says "this test
holds that sentence" for a part (the form) the quoted prefix does not word out; if WAY-71's second
sentence is reworded, the foundation check flags the line and its author reads the test again, which is
what the line is for.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0, `0 errors`.
- With the first quotation altered ("holds" -> "keeps"): `elements/common/test_foundation_check.py:732: the
  quotation stands in no binding sentence of `WAY-71``, 1 error, so the new line is read; restored,
  `0 errors` (the test file was restored from a copy; `git diff` shows only the two added lines).
- `python -B gate/run_tests.py elements/common` — 0, 257 tests OK.
- Not run: the full gate (the orchestrator's alone, WAY-160).

## Own-work check

Requirement most likely not met: every part the clause `tests:` names has a test with a line `decision:`.
Check: `git grep -n "decision: WAY-71"` gives four lines at four tests, mapped one to one to the four parts
of the clause (above); the foundation check reads them (altered quotation rejected once, then restored).

## Not touched

WAY-287, M4, M5, N1, N2 and m1, as the handoff says.

## Reach beyond the dispatch

None. I did not read `reports/review-return-step-report.md`: the finding file holds the finding whole and
names its places, which I read in the code.

## Unread material

`reports/review-return-step-report.md` (not read, as above). Nothing else named in the handoff was left
unread.

## Searches not found or unclear

None.

## Working copies

`.runs/author/` held my edit script and a backup of the test file; it stood at
`.runs/author/` and was removed before the
report. No worktree or clone was made.
