# Findings to fix — Minor findings within the task of the whole-change review (PASS 4905a56544ff8d9600af406d52afdfcd588e3493)

No blocking findings. The four findings below are the reviewer's words, cut from
`review_whole_report.md`, section "Minor findings within the task". Where the reviewer's suggestion
is "no change to the entry" or "keep the sentence", the finding is carried by the request, not by
a change of the entry: make no change for it and say so in the fix report.

1. `foundations/decisions.md:10991-10992`, last sentence of *Rationale*: "Tests of a script's behaviour stand without an invariant,
   since WAY-12 concerns how a decision is checked." What is wrong: it states, in prose, how an agent is to read WAY-12 against the
   test this entry requires; WAY-05 puts what a decision forces on later work in a binding sentence or a field, never in prose, and
   WAY-12 itself still says "tests live only with invariants" with no relation to this entry. Why it matters: an agent reading WAY-12
   alone, or comparing a change with it, meets a rule it will take as forbidding the test that WAY-330 requires; the only place that
   resolves it is the rationale of another entry. Evidence: WAY-12 binding sentence; template line 130 "Tests live only with
   invariants"; WAY-25 on unrecorded collisions. Not Important: the human's task states this reading (*Context*, WAY-12 bullet) and the
   practice agrees (`test_remarks_check.py`). Suggested: keep the sentence, name it in the request's section for the human's decisions
   as the cycle's wording, and leave a narrowing of WAY-12's wording to a separate change.
2. `foundations/decisions.md:10972-10975`, *Verification* violates, "a change adds a reading of a file with no test that gives the
   file without a field": it drops the qualification of the binding sentence, which covers the readings of a new script and the
   reading of a file a changed script reworks. A change that adds a reading of a further file to an existing script is covered only if
   "reworks the way of reading" is taken to include it; the entry does not say so, and the task's Q2 answer says "gdy zmiana go
   dotyka". Effect: an agent comparing a change may judge more or less sharply than the binding part. Suggested: say in the example
   "a new script, or a changed script's reworked reading of a file, with no test ...". Minor, not Important, because the example
   reads reasonably as the stricter side of an ambiguity the task itself leaves.
3. `foundations/decisions.md:10959-10960` and the pair of examples: the writer's own additions (the relation `derives from WAY-38`,
   the pair of examples, the WAY-12 sentence) are not carried by any row. The row text and Q1 answer say "spokrewniona z WAY-38 jako
   reguła z tej samej rodziny"; WAY-32 defines `derives from` as "a higher decision this one serves", which is a stronger claim than
   "same family", though the *Rationale* does rely on WAY-38's quiet-pass sentence, so the relation is defensible. They are accepted
   by the human only at the merge (WAY-114), so the request must name them in its section for the human's decisions as the cycle's
   choices. Suggested: that naming; no change to the entry.
4. `foundations/decisions.md:11014`, *Rejected*: "the skills that read exit codes know only 0, 1 and 2" is a statement of what the
   process's tools do today, which WAY-05 and the template allow only where the entry quotes a source; here it is the writer's
   paraphrase of the task's *Not chosen*. It goes false as soon as a code is added. Suggested: end the clause at "each would have to
   be extended". Minor.
