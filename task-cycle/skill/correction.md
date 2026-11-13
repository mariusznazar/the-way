# Correction after review

Read when the input of `implement-task` is a link to its open request, or to a comment holding the
human's remarks.

In the-way itself, before anything else, fetch, and bring what the session works in up to the remote
target branch. Where the session works in a copy of the target branch, fast-forward it as step 4 of
`implement-task` gives, or stop and say so; where it works in the request's worktree, merge the
remote target branch into it and, where that merge changes code the cycle reviewed, have it reviewed
and its affected checks run as the merge in the paragraph below is (WAY-306). In both cases, where
something came in, start again from the entry point that started the cycle.

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
the-way pin included, and verify that the pinned checkout matches the product's gitlink. Where that
merge changes code the cycle reviewed, a fresh reviewer reviews the merge with `review-change`, with
a dispatch that asks whether the two sides still hold together and names the foundation entries the
merge brought in that bear on the parts the change touches, as step 12 of `implement-task` gives
(WAY-306, WAY-150), and the agents that own the checks the merge touches run them again. The remarks
bind; record them as new events, and write them word for word, as the human gave them, into
`reports/correction-<n>-remarks.md` of the record, `<n>` counting the corrections from 1, also
where they came in conversation or concern only the refreshing of the target branch (WAY-357).
Keep the recorded route for the affected work: dispatch the
correction with `make-change`, resuming the author where possible, and have it reviewed with
`review-change`, the remarks in place of a findings file; the review ends as "The end of a code
review" gives. A new open design choice, a reserved choice or an oversized attempt follows the
recovery "Design and execution choice" gives, with its reset base recorded. Repeat only what the
remarks touch — the return step included — run the gate on the corrected tree as step 10 gives, and
repeat the record's pair of commits from step 12, preparing the copy before it as `implement-task`
("The record before it is committed") gives, with every report of the cycle in the record, the
correction's own among them. For a request a remaining blocking finding
blocked, the human's decision is the input: make the fix it calls for, or keep the code the human
accepted despite the finding, then run what has not run on that code (WAY-163). Rewrite
`request.md` by `task-cycle/skill/request_template.md`, in its variant for a correction, for the
state after the correction, with the link to the record's new commit and with the pairs of the
correction in one sentence as the item of kind 17 in *You accept by merging* (WAY-287), check it
as the template gives, and edit the request's description from it.

Before the record's copy is prepared, add the correction's line to the record's item *Corrections
after the request opened*, as `task-cycle/record_template.md` gives it: the file of the remarks and
each pair `<source> · <kind>` of the correction once (WAY-357, WAY-358). Take the source from what
started the correction: `item <n>` for the human's answer to an item of the request's *For you to
decide*, `<n>` being the number of that item's kind in `request_template.md`, as in item 8
below, never the number the item had in the description; `remark` for a remark of the human
outside any item; `target-branch` for a correction that exists only to refresh the target branch
at the human's request. Judge each kind by one test against the documents: `defect` where what the
correction changes was required by the approved task document or by the foundation, or is a
regression, which is the test of `project-level/task/template.md` for a task that fixes a defect;
`not-required` where it was not required; `none` only with `target-branch`. A correction that has
several sources gives each pair once.

An answer to the item of the request's *For you to decide* on unfixed findings (item 8 of
`request_template.md`) that asks for the fix makes the findings it names the remarks the correction
binds; an answer that names none makes of them the findings the item listed (WAY-289). The
correction's review ends as every review does. The findings that remain unfixed after it are put by
the request only with the question of a task, or stay in the lower part, and no second correction
is asked for them. An answer to make a task, or to let the item through, needs no correction.

An answer to do it in this request, to an item of *Fix or let through* other than item 8, runs the
correction the same way, the item it names being the remark the correction binds (WAY-289):

- for a skipped step or an unrun check (item 4): the correction runs the step or the check that
  was left out, on the corrected tree, and records its result;
- for a proposal of the task's own sections that was not applied (item 9): the correction applies
  the proposal;
- for an incomplete reading by the review of the whole change (item 14): a fresh reviewer, who
  did not make the change and did not write that review, reads what stayed unread, and its report
  holds its **Unread material**, and its findings are handled as those of every review are.

What such a correction leaves undone, or finds anew, is put by the request only with the question
of a task, as for item 8, and so is an item that cannot be done in this request at all. The human
who makes no task lets such an item through by merging.
