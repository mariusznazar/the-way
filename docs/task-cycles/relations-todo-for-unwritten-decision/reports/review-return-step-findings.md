# Findings of the review of the return step (`reports/review-return-step-report.md`, first line `FAIL 763af6951a65f6cca17b032a037c60c7b2d59e0a`)

Cut from the report in the reviewer's words: the blocking finding. The review lists no Minor finding that is fixed (its m1 is a Minor finding of a review of the return step, which is not fixed).

## Blocking

### Important

**I1 — WAY-71's clause `tests:` names two parts that no test holds by a line `decision:`, and the pair's examples for those two parts were removed (within the task; blocking).**

Place: `foundations/decisions.md:618-621` (the clause) and `foundations/decisions.md:622-633` (the pair);
`elements/common/test_foundation_check.py:731` and `:784`.

What is wrong: the clause reads "tests: that the script reports a bare `TODO` in a decision's *Relations*, a
`TODO` behind a relation type there and a `TODO` joined to the relations by a comma as errors, and that it
takes the descriptive form after known relations". Only two tests carry a line `decision: WAY-71`
(`git grep "decision: WAY-71"` finds exactly `test_foundation_check.py:739` and `:760`):

- `:739` `test_relations_a_bare_todo_names_no_decision` — the bare `TODO` in *Relations*: held.
- `:760` `test_relations_derives_from_todo_is_an_error` — the `TODO` behind a relation type: held.
- the comma join — checked by `test_relations_a_described_todo_after_a_comma_is_no_joined_list` (`:784`),
  which carries no line `decision:`: not held.
- the descriptive form after known relations — checked by
  `test_relations_a_known_decision_then_a_missing_one_described_passes` (`:731`), which carries no line
  `decision:`: not held.

The commit nonetheless removed from the pair the complying example
`Relations: derives from WAY-x · TODO — <the decision, and where it is expected>` and the violating example
of the comma join, together with the two examples that the lines do hold.

Why it matters: in the-way "a test holds a sentence" means it carries a line `decision:` (WAY-12 "A test
that holds a sentence of a decision carries beside it a line `decision:`"; template "Verification": "the
lines `decision:` find the tests, so the clause is no second copy of the link"). The return step's rule
(`task-cycle/skill/return_step.md`) removes from the pair only "that part" a test holds and "leaves a pair
only for a part no test holds". So for two of the four removed examples the meaning fell out: an agent that
compares a change with WAY-71 finds neither an example nor, following the lines `decision:`, a test for the
comma join or for the passing form after known relations; and if WAY-71 is reworded, the foundation check
flags no line at those two tests. The entry's *Verification* states a link the files do not have — the
entry's content disagrees with the files, which the review's grading keeps Important (WAY-263, WAY-364).
The author applied the same reading the other way for the older parts of the pair: the bare `TODO` in
*Rests on*, *Derives from*, *Based on* and the `TODO` in *Origin* are checked by tests without a line
(`:694`, `:710`, `:863` and others) and their examples were rightly kept — the comma and after-known parts
are in the same position and were not.

Evidence: `git grep -n "decision: WAY-71"` (2 hits, `:739`, `:760`); the test bodies at `:731-736` and
`:784-787` (no comment line); the diff of `foundations/decisions.md` (removed lines "a decision that derives
from one decision the log holds and from one it does not hold yet reads `Relations: derives from WAY-x ·
TODO — …`" and "a decision joins `TODO — …` to the relations before it with a comma instead of ` · `").

Fix (either): (a) add a line `decision:` at `:731` — for example quoting
"The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet:"
(the sentence the passing form keeps) — and at `:784` (the error sentence already quoted at `:739`); or
(b) narrow the clause to the two held parts and restore the two examples to the pair.
