# A blocking finding that remains

Read under "The end of a code review" of `implement-task`, when a blocking finding remains after the
review of its fix.

When a blocking finding remains after the review of its fix — in any of the cycle's code reviews, a
slice's included — the change is blocked: run no third round and do not rule on the finding. Run
the gate on the change as step 10 gives, and make no further slice, no return step and no
reconciliation with the target branch on code its review has not accepted (WAY-163). Run
`task-cycle/cycle_stages.py` as step 12 gives, write the record and commit its copy and its removal
as step 12 gives them, then open the request as a draft marked `blocked`, link the record by the
SHA of the commit that adds it, and give what step 13 names for it. After the human's decision, the
correction after review runs what has not run on the code that passed review or that the human
accepted despite the finding.
