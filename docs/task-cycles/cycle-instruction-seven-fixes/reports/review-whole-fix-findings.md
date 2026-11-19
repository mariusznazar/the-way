# Findings for the fix — Minor findings within the task of the review of the whole change

Cut word for word from `reports/review-whole-report.md` (`PASS bcaddc2b`). No blocking finding; no finding carries a contradiction with the settlements. Findings 5 and 6 of that report lie outside the task and are not here.

### Minor, within the task

**1. The three entries gained examples and reasons their rows do not give, and the author's report
marks them `row <n>`.** Place: the author's report, section "Foundation step" ("None is marked
`the cycle's`"); the added text at `foundations/decisions.md:5542-5544`, `:5557-5559`,
`:6285-6287`, `:6295-6296`, `:6703-6704`, `:6709-6710`.
`task-cycle/skill/foundation_step.md` says: "a part the writer adds that its row or projected
entry does not give — a pair of examples, a field the projected entry left `TODO` — makes the
entry `the cycle's`, save a pair kept only until a test of the same change holds the sentence …
and the writer keeps in its report the added pair word for word for the description to quote under
the entry". WAY-114 gives as a violation "an entry marked as the cycle's for an added pair of
examples reaches the merge with the pair not shown", and `elements/decisions/skill/SKILL.md` has
the human accept a proposed pair at the merge, "the entry marked as
`task-cycle/skill/foundation_step.md` gives". The author's reason — that it extended the clauses
the decisions had and added no pair standing apart — does not change what was added: for each new
sentence a complying and a violating example that no row gives. Why it matters: the request would
list the three entries as written from rows and show the human none of the examples by which
agents measure later changes. No file of the change is wrong; the correction is the marking and
the quotation in the author's report (and from it the record and the request). The added clauses,
word for word:

- WAY-136, complies: "a change that rewrites many entries of the foundation from many notes has
  the slices without a review of their own reviewed in groups, in the plan's order, the grouping
  and its reason recorded"; violates: "reviews of groups of slices are dispatched with no grouping
  and reason recorded, or by a measure in place of the orchestrator's judgment".
- WAY-255, complies: "and returns its report after reading the result"; violates: "an agent ends
  its turn with a note that it still waits for the tests it started in the background, in place of
  their result".
- WAY-134, complies: "a decision row whose source keeps a way with only the cost of a gate to
  reopen gives that way `no cost to the product known` in the decision's rejected options, and
  leaves out the way that only chose when the answer is recorded"; violates: "the cycle puts in
  the rejected options a way of the process, such as when an answer is recorded, or leaves a way
  whose source keeps no cost without the words `no cost to the product known`".

**2. The first paragraphs of WAY-136 and WAY-134 hold four binding sentences.** Place:
`foundations/decisions.md:6245-6264` and `:5482-5509`. The template gives "One to three sentences
answer the question of the heading, in the first paragraph under it" (WAY-05); both paragraphs had
three at the base, and the author kept WAY-255 at three by writing the rule as a clause, for this
very reason, by its report. The content agrees with the rows and the check of the foundation does
not count sentences, so this is a departure of form with no sentence read wrongly (WAY-364). A
clause joined to the third sentence, as in WAY-255, keeps the form.

**3. The reason written into the *Rationale* of WAY-134 is the author's own, not the task's.**
Place: `foundations/decisions.md:5590-5595`: "A way of the process, such as when an answer is
recorded, is no alternative the product weighed, so listed among the rejected options it would
make the proposer of a later change of the product meet a refusal that never concerned it; a way
whose source gives no cost, or only a cost of the process, stands with the words `no cost to the
product known`, so that its empty cost reads as nothing known to weigh and not as a cost nobody
weighed." The task gives one reason for point 5 and row 3: agents settled these three cases
differently from one cycle to the next (its *Need* and *Context*). The entry now gives another
reason as that of the human's settlement, and a later reader takes a written reason for the one
the decision was made for (the rationale of WAY-29 says so of a reason an agent writes). Its last
clause is also hard to read: "nothing known to weigh" and "a cost nobody weighed" are not told
apart by the words. The additions to the *Rationale* of WAY-136 and WAY-255 do follow the task's
*Need* (one reviewer cannot compare several hundred entries with their sources; a note that the
agent waits in place of the result). The correction is to state in WAY-134 the reason the task
gives, or to leave the reason out.

**4. A wrong number in the comment of a new test.** Place: `task-cycle/test_slice_size.py:64-65`:
"A decision log of 400 010 characters in its first line". The file the test writes holds 400 009
characters (`"x" * 400_000` and `"\none\ntwo\n"`, 9 characters) and its first line 400 000. The
figure of 160 004 tokens and the asserted values (8 characters, 4 tokens, `fits`) are right, so the
test stands; the comment is the source of its values (the rule on test data of
`guidelines/testing.md`) and gives one of them wrongly.
