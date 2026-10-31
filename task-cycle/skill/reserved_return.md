# A reserved choice

Read under "Design and execution choice" of `implement-task`, where an agent returned `reserved`,
or where the task at step 4, an agent's question or a report of `returned` needs a language, a
framework, a library, a store of data, a way of logging in or a place to run that the task, the
spec and the foundation do not settle.

No stage of the cycle settles a reserved choice, you included (WAY-268): the human settles it at
`settle-technology`, so the cycle ends in a blocked draft request and the task returns to refinement
(WAY-269).

## Check the choice

Read `project-level/technology/reserved_choices.md` of the pinned the-way and check the choice
against its rule before any answer: an agent's claim is no evidence, and no answer and no smallest
reversible reading settles a reserved choice.

- Where a source the rule names settles the choice, answer from it and resume the agent.
- Where the rule does not take the choice, go on by the route that fits: a choice of how to make the
  change is the agent's to make and yours to enter in the questions table, and an open design choice
  takes the recovery "Design and execution choice" gives.
- Otherwise stop, by the rest of this file: no spec is written (WAY-135), and a slice's executor
  gets no retry.

This check rules on no finding of a review. A finding that the change takes a reserved choice gets
its one fix as any other (WAY-162), and the agent of that fix returns `reserved` where it cannot
remove the choice from the change. Where you then find no reserved choice, answer the agent; the
finding stands, and the review of the fix judges it.

## Discard the attempt

Discard the attempt as "Design and execution choice" gives for an open design choice (WAY-135), its
foundation entries and the slices already made with it: the report kept, its last commit and files
recorded, the task branch reset to the recorded base — to the commit that moved the pin where step 2
moved it. Record the discard with its reason under *Discarded attempt* and the choice under
*Reserved choice*, and do not continue at step 6.

A choice you find at step 4 has no agent report and leaves nothing to discard: the record holds it
under *Reserved choice*, and the rest of steps 4 and 5 sets up the branch, its base, the checks
failing on it and the record.

## Open the request

From here nothing else of the cycle runs: no spec, plan, review, return step or reconciliation with
the target branch, and nothing is merged from the target branch. The gate does not run either: the
tree equals the base, whose failing checks step 4 recorded, or the commit that moved the pin, whose
gate step 2 ran.

The order differs from step 12's in one point: the request opens on the commit that adds the record,
before the commit that removes it. It therefore never rests on a host accepting a request with no
changed files, and the branch still ends with only the pair of step 12.

1. Set the record's status to `blocked` and run `task-cycle/cycle_stages.py` as step 12 gives.
2. Copy the record directory, commit it as step 12 gives and push that commit. The request does not
   exist yet, so *Request URL and status* in the copy reads `blocked draft, opened on this commit`.
3. Open the request as a draft on that commit, marked `blocked`, while the record is its changed
   files, and link the record in its description by the SHA of that commit.
4. Commit the removal of the copy and push it. A host that closes the request when its diff empties
   changes nothing: the closed request keeps its description and its link.

Keep the worktree, take step 14 and end the cycle with the status `blocked`.

## What the request states

Beyond what step 13 gives any request — the goal, the relation, the sources, the pin, the discarded
attempt and the agent's report — the request states:

- under *Questions*, the choice in plain words, by what the product needs it for; where it showed,
  by the stage and the item of the task; which limb of the rule takes it; and what was searched and
  found not to settle it;
- the ways the agent saw, marked as not researched and carrying no recommendation, since
  `settle-technology` does that research;
- *Checks*: the checks failing on the base and, as not run, each of the stages above that did not
  run, the gate among them, and why;
- the time, models and tokens so far, from `stages.md`;
- *What this request settles*: none;
- what happens next: the human closes the request, and `refine-task` takes the named choice as the
  note. A remark on this request is no correction, and the cycle does not continue on it.

## After a correction

Where the agent of a correction returns `reserved` and the check above stops the work, the request's
code stands and only that correction's commits go: reset the branch to the head the request held
when the correction began, the correction's merge of the target branch included, none of them being
pushed yet, and record that reset base. The tree is then the one the request already holds, so
neither the gate nor a review runs on it.

Set *Reserved choice* in the record, repeat the record's pair of commits as `correction.md` gives
and update the request's link to the record. Return the request to draft marked `blocked`, with the
choice, the ways seen and what happens next as above, its *What this request settles* unchanged. Its
code stands until the human closes the request or changes the remark, and `correction.md` takes a
remark on it.
