# Correction after review

Read when the input of `implement-task` is a link to its open request, or to a comment holding the
human's remarks.

Before anything else, read the field *Reserved choice* of the request's record, in the kept worktree
or in the commit the request links. Where it reads `none`, or the record holds no such field, go on
below. Where it names a choice, a reserved choice blocked the request, and a remark settles no such
choice:

- With no code on the branch, nothing is corrected: dispatch no one, change nothing, and tell the
  human in your report that the request is to be closed and `refine-task` run with the named choice.
  A remark that picks an option does not settle the choice, since the option would stand in a
  comment and not in the task document.
- With code on the branch, a changed remark that no longer needs the choice is an ordinary
  correction: set the field back to `none` and go on below. A remark that still needs the choice,
  or that picks an option, is answered as above.

Take a link to the request, or to a comment holding the human's remarks, as the input. Work on that
request's branch and in its worktree. First merge, never rebase, the current target branch, the
the-way pin included, and verify that the pinned checkout matches the product's gitlink. The remarks
bind; record them as new events. Keep the recorded route for the affected work: dispatch the
correction with `make-change`, resuming the author where possible, and have it reviewed with
`review-change`, the remarks in place of a findings file; the review ends as "The end of a code
review" gives. A new open design choice, a reserved choice or an oversized attempt follows the
recovery "Design and execution choice" gives, with its reset base recorded. Repeat only what the
remarks touch — the return step included — run the gate on the corrected tree as step 10 gives, and
repeat the record's pair of commits from step 12. For a request a remaining blocking finding
blocked, the human's decision is the input: make the fix it calls for, or keep the code the human
accepted despite the finding, then run what has not run on that code (WAY-163). Update the request's
description: its record link, its lists of findings and *What this request settles*.
