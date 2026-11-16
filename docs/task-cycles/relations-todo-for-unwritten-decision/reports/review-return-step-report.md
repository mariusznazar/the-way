FAIL 763af6951a65f6cca17b032a037c60c7b2d59e0a

# Review of the return step — relations-todo-for-unwritten-decision

Range `68d8645c78e55bf751161fedd26dedf31cb43dbc..763af6951a65f6cca17b032a037c60c7b2d59e0a`, one commit
(`763af69` "Hold the Relations part of WAY-71 by tests and keep its pair only for the rest"); files
`foundations/decisions.md` (WAY-71 *Verification*, +6 -8) and `elements/common/test_foundation_check.py`
(+2 comment lines). `git rev-parse HEAD` = the given head.

## Findings

### Critical

none

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

### Minor

**m1 — The report's argument for why WAY-287 "still holds" misreads WAY-287 (within the task; blocks nothing).**

Place: `reports/author-return-step-report.md`, section "For the human: WAY-287", the sentence "If left, the
sentence still holds by WAY-287's own rule that another decision may add a kind of item (WAY-71 does) and
the template lists every kind."

What is wrong: WAY-287's second paragraph (`foundations/decisions.md:7020-7021`) lets another decision add a
*kind* of item "naming the group"; WAY-71 names no group, and a descriptive `TODO` in *Relations* is not a new
kind but WAY-287's own kind ("each descriptive `TODO` … (WAY-71)", `:7006-7008`) whose list of fields is now
short by one. The conclusion — leave WAY-287 to the human, as M4 already does — stands; the argument should
not be carried into the request's description as the reason the gap is harmless.

### Out of scope

M4, M5 (review of the whole change) and N1, N2 (review of the fix) are known and go to the request's list;
not re-graded.

## The five questions of the dispatch

1. **Removing examples and opening with `tests:`.** The form is right: the clause gives parts in words with no
   path, test name or number, followed by "An agent compares the change with the part no test holds:", as
   WAY-12's own *Verification* does; *Rationale* and *Rejected* stay whole (WAY-12). Removing the examples of
   the bare `TODO` in *Relations* and of `derives from TODO` is what the return step gives. Removing the
   other two is not: see I1 — those two meanings are now held by no test with a line and by no example.
2. **The two lines `decision:`.** Both quote a sentence that stands in WAY-71's binding sentences
   (`foundations/decisions.md:612`, begins after a full stop and a space, more than three words); the
   foundation check reads them (0 errors). Each test checks what its clause part says: `:739` asserts the
   error and its message for seven bare forms including after a known relation; `:760` asserts the
   typed-`TODO` error for `derives from TODO`. The quoted sentence (the script reports a word not given the
   field as an error) fits both error tests.
3. **WAY-126 left whole.** Right. Its new paragraph (`:3735-3737`) states what an author does when writing a
   projected entry; the script does not check it and no line `decision: WAY-126` exists, so its pair, which
   carries the new paragraph's complying and violating examples (`:3750-3755`), is all that holds it.
4. **Anything left out of line.** None found beyond M4 and M5. `elements/common/rules.md:22-30`,
   `elements/decisions/template.md:36`, `:64-77`, `:222-223`, the docstring of
   `elements/common/foundation_check.py:41-52` and `task-cycle/skill/request_template.md:269-274` say what
   WAY-71 says; `elements/environment-facts/template.md:101-103` speaks of facts only; `foundations/part_map.md`
   and `foundations/glossary.md` mention neither *Relations* nor `TODO`; no other entry of the log lists the
   fields that take a descriptive `TODO` except WAY-287 (M4).
5. **WAY-287.** Leaving it unchanged and naming it for the human is right: the task fixes it as "Bez zmiany",
   and adding a field to its list goes beyond what the task carries (WAY-30, as
   `task-cycle/skill/foundation_step.md` gives). The three passages the report quotes match the file
   (`:7006-7007`, `:7064-7066`, `:7082-7083`). The report states WAY-287 as not read again in this stage;
   that bears on nothing the step changed, since its quotations are accurate — only its argument is off (m1).

## Declined to judge

- Whether WAY-287 should be changed in this request — M4, the human's (task: "Bez zmiany").
- The line length of the two comment lines (128 characters) — the form of a line `decision:` requires the
  quotation to run to the end of one line.

## Against the guidelines

`guidelines/testing.md` read whole. The commit adds comment lines only: no expected value, assertion or
input changed (`### Changing an existing test` not reached).

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests OK.
- `git grep -n "decision: WAY-71"` and `git grep -n "decision: WAY-126"` — manual: 2 lines for WAY-71
  (`:739`, `:760`), none for WAY-126.
- Manual: each removed example of the diff matched to a test and to the presence of a line `decision:` at
  it (I1).
- Not run: the full gate (the dispatch forbids it).

## Reach beyond the dispatch

- `.runs/task-cycles/relations-todo-for-unwritten-decision/cycle.md` — to see the known findings M4, M5, N1,
  N2 and what the orchestrator recorded of the return step.
- `reports/review-whole-report.md`, M4 and M5 headings only (grep) — to confirm M4 is WAY-287.
- `elements/common/rules.md`, `elements/decisions/template.md` (*Relations* and "Relations and precedence"
  passages), `foundation_check.py` docstring, `request_template.md` item 16,
  `elements/environment-facts/template.md` *Source* — for question 4.

## Working copies

none — no worktree, clone or script was made; `.runs/review-return-step/` was not created.

## Unread material

`reports/author-report.md`, `reports/author-fix-report.md`, `reports/review-whole-report.md` (beyond the
M4/M5 lines) and `reports/review-fix-report.md` (beyond its headings) — named for context only, not read
whole. WAY-287 read in its binding sentences, *Verification* and the *Rationale* passage on the descriptive
`TODO` (`:6994-7086`), not its *Rejected*. WAY-71, WAY-126, WAY-12, WAY-22 read whole; `guidelines/testing.md`
whole; `return_step.md` and `foundation_step.md` whole; the template's "Verification" section and the
decisions skill's step 3 whole.

## Searches not found or unclear

- A line `decision: WAY-71` at the tests of the comma join and of the form after known relations — not found
  (I1).
- A line `decision: WAY-126` anywhere — not found (expected; question 3).
