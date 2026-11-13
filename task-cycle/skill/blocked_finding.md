# A blocking finding that remains

Read under "The end of a code review" of `implement-task`, when a blocking finding remains after the
review of its fix.

When a blocking finding remains after the review of its fix — in any of the cycle's code reviews, a
slice's included — the change is blocked: run no third round and do not rule on the finding. Run
the gate on the change as step 10 gives, at once, since no return step runs on this code, and make
no further slice, no return step and no reconciliation with the target branch on code its review
has not accepted (WAY-163). Run
`task-cycle/cycle_stages.py`, and beside it `task-cycle/cycle_measures.py`, as step 12 gives, write the record, prepare its copy as "The record
before it is committed" of `implement-task` gives and commit the copy and its removal as step 12
gives them, then write the description by `task-cycle/skill/request_template.md` as
step 13 gives, in its variant for a remaining blocking finding, linking the record by the SHA of the
commit that adds it, and open the request from it as a draft marked `blocked`. The request does not
exist when the copy is committed, so *Request URL and status* in the copy reads, word for word and
alone on its line, `blocked draft, opened on this commit`, the wording `project-level/plan_state.py`
recognises to report the task as blocked. After the human's decision, the correction after review
runs what has not run on the code that passed review or that the human accepted despite the finding.
