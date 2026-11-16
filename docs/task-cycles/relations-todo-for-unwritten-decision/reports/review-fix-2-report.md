PASS 07a23b3a1ee8680697d3ad0aeb26e9803a693fb5

# Review of the fix of the return step's findings — relations-todo-for-unwritten-decision

Range `763af6951a65f6cca17b032a037c60c7b2d59e0a..07a23b3a1ee8680697d3ad0aeb26e9803a693fb5`, one commit
("Hold the comma join and the passing form of WAY-71 by a decision line at their tests"); one file,
`elements/common/test_foundation_check.py`, +2 comment lines, none removed. `git rev-parse HEAD` = the given
head; the tree is clean.

## The findings, one by one

**I1 — fixed.** `git grep -n "decision: WAY-71"` now finds four lines, one at each part WAY-71's clause
`tests:` (`foundations/decisions.md:618-621`) names:

| Part of the clause | Test | Line | Quotation |
|---|---|---|---|
| the descriptive form after known relations is taken | `test_relations_a_known_decision_then_a_missing_one_described_passes` | `:732` | "The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet:" |
| a bare `TODO` in *Relations* is an error | `test_relations_a_bare_todo_names_no_decision` | `:740` | "`elements/common/foundation_check.py` reports a missing field, or a word not given it, as an error." |
| a `TODO` behind a relation type is an error | `test_relations_derives_from_todo_is_an_error` | `:761` | same |
| a `TODO` joined by a comma is an error | `test_relations_a_described_todo_after_a_comma_is_no_joined_list` | `:786` | same |

Each line sits directly under the `def` of the test it marks, and each test asserts what its part says: `:732`
asserts that three after-known values pass; `:786` asserts the error "*Relations* joins its items by ` · `"
and one error. The new quotation begins at the start of WAY-71's second sentence (after "`TODO` that
something is missing. ", `foundations/decisions.md:602-604`), holds more than three words and stands in the
binding sentences; it is the sentence that gives the passing form, so it fits a passing test, and the error
sentence fits the comma test. The foundation check reads both (0 errors on the head; the author's report
shows an altered quotation at `:732` rejected, then restored). With the four lines in place, the two
examples the return step removed from the pair are held by tests, so no meaning is left without a test or
an example.

## New findings in the fix diff

### Critical

none

### Important

none

### Minor

none

m1, M4, M5, N1 and N2 are known and go to the request's list; not re-graded.

## Declined to judge

- That the quotation at `:732` is a prefix of a long sentence and does not word out the *Relations* form
  itself — the form of a line `decision:` asks only for the start of a sentence, and the author names this
  cost in the report; nothing to judge beyond that.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests OK.
- `git grep -n "decision: WAY-71"` — manual: four lines, `:732`, `:740`, `:761`, `:786`, mapped to the four
  parts of the clause (table above).
- Not run by me: the altered-quotation run (it needs a changed file, so a working copy; the author's report
  gives it, and the 0-error run on the head with the same mechanism reading the two older lines suffices).
  Not run: the full gate (the dispatch forbids it).

## Reach beyond the dispatch

`foundations/decisions.md:600-606` — to confirm where WAY-71's second sentence begins.

## Working copies

none — `.runs/review-return-step/` was not created.

## Unread material

none — the handoff, the findings file, the fix report, my earlier report and the fix diff were read whole.

## Searches not found or unclear

none
