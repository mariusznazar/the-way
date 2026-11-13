# Draft from what is known

Give the task an editable title. Preserve the human's wording and the approved project's meaning;
structure them without translating them into an invented technical design.

Create or update the document in the product's task place once its goal is clear. Use `TODO` for
missing information and `Status: refining`. Give its full path to the human. For a task already in
its cycle, leave its frozen task document intact and route a scope change through the cycle's
question and record.

A task document written before and not yet in its cycle, an accepted one included, is refined from
its text: its answers and the accepted rows of *Settlements to record* stand with their sources,
and only what the human reopens, and what a reopened answer changes, is settled again. Its status
returns to `refining` and is not `ready for cycle` again until the human accepts the whole changed
document (WAY-124); steps 4 to 6 run on the whole document. A task whose blocked draft request
the human closed is such a document: the named choice is the note of the run of `settle-technology`
at it, and you keep the closed request's link under *Context*, so that the new record can be reached
from the old (WAY-269).

Fill the header line `Defect introduced by:` in every task, as `project-level/task/template.md`
gives it (WAY-354); the cycle never fills it. From the history of the lines the task changes and
from the human's report of the defect, set `none` where the task does not fix a defect found
after a merge, the addresses of the requests, or commits, that introduced the defect, or
`unknown` with the reason; apply the template's test of what such a
task is, which keeps out a new need, a change of mind, a gap of the earlier task and maintenance
(WAY-353). Where the human reopens a task document written before this line, add the line; a
document the refinement does not reopen keeps no line, and its missing line means that it was not
assessed.

Keep Description to what an implementer needs to take the task. Put likely follow-up answers in
Context. If a block's place is uncertain, move it to Context. Do not ask questions merely to fill
Context, and do not invent acceptance criteria.

Show the whole current task document when asking for a wording decision. A suggestion not
supported by the human or an approved source appears as `Proposal:` outside the document and enters
it only after acceptance.
