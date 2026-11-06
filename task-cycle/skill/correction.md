# Correction after review

Read when the input of `implement-task` is a link to its open request, or to a comment holding the
human's remarks.

In the-way itself, before anything else, fetch, and bring what the session works in up to the remote
target branch. Where the session works in a copy of the target branch, fast-forward it as step 4 of
`implement-task` gives, or stop and say so; where it works in the request's worktree, merge the
remote target branch into it. In both cases, where something came in, start again from the entry
point that started the cycle.

Then read the field *Reserved choice* of the request's record, in the kept worktree or in the
commit the request links. Where it reads `none`, or the record holds no such field, go on below.
Where it names a choice, a reserved choice blocked the request, and a remark settles no such
choice:

- With no code on the branch, nothing is corrected: dispatch no one, change nothing, and tell the
  human in your report that the request is to be closed and `refine-task` run with the named choice.
  A remark that picks an option does not settle the choice, since the option would stand in a
  comment and not in the task document.
- With code on the branch, a changed remark that no longer needs the choice is an ordinary
  correction: set the field back to `none` and go on below. A remark that still needs the choice,
  or that picks an option, is answered as above.

Take a link to the request, or to a comment holding the human's remarks, as the input. Work on that
request's branch and in its worktree. First merge, never rebase, the remote target branch, the
the-way pin included, and verify that the pinned checkout matches the product's gitlink. The remarks
bind; record them as new events. Keep the recorded route for the affected work: dispatch the
correction with `make-change`, resuming the author where possible, and have it reviewed with
`review-change`, the remarks in place of a findings file; the review ends as "The end of a code
review" gives. A new open design choice, a reserved choice or an oversized attempt follows the
recovery "Design and execution choice" gives, with its reset base recorded. Repeat only what the
remarks touch — the return step included — run the gate on the corrected tree as step 10 gives, and
repeat the record's pair of commits from step 12, running before it the process remarks check of
`implement-task` ("The process remarks check") on the record with every report of the cycle, the
correction's own among them. For a request a remaining blocking finding
blocked, the human's decision is the input: make the fix it calls for, or keep the code the human
accepted despite the finding, then run what has not run on that code (WAY-163). Rewrite
`request.md` by `task-cycle/skill/request_template.md`, in its variant for a correction, for the
state after the correction and with the link to the record's new commit, check it as the template
gives, and edit the request's description from it.
