# Reading a product's guidelines

Use this procedure whenever an agent's work touches a product's user interface or code: in task
refinement (WAY-214), in project breakdown (WAY-218) and in the task cycle (WAY-213). Read it from
the checkout or pinned the-way the calling workflow uses.

Who selects: outside the task cycle, the agent doing the work selects the guidelines of the parts
its work touches. In the task cycle, the orchestrator of `implement-task` reads by this procedure
the guidelines of the task's parts once, and names in each other agent's handoff the files of the
parts that agent's work touches — for a slice, through the *Read* of its plan, which the planner
proposes and the orchestrator checks; the reviewer of the whole change selects for its own review.
Every other agent of the cycle reads the files its handoff names (WAY-213). A guideline file goes
to an agent whole: guidelines are short and hold together only as a whole. The selection is not
recorded with its reasons, the receiving agent does not check it, and no step of its own revisits
it at each handoff. The only result the reading leaves is its findings — guidelines missing,
malformed or uncertain — which go to the workflow that owns the work, as "Hand the findings back"
says.

## Name the affected work

Name the parts the work touches as step 1 of "Reading the foundation" in
`elements/common/way_of_working.md` names them: from the files the work changes or is to change,
or, where the work names no file yet, from the responsibilities it changes. Inspect the
product's files to establish what is already there. For each part, settle whether the work changes
a user interface or writes code, and which kinds of code it creates or changes. A backend's admin
panel is a user interface; helper and build scripts are code. Names and file extensions alone do
not settle the classification. An API or terminal alone is no user interface in the styleguide's
sense (WAY-183).

If the map has no part for the work, keep its identity as a question in the owning workflow until
settled; additions to the map follow that workflow's foundation rules and known files, not
invented assignments. Where a part, a classification or a kind is unclear, read further; if it
stays unclear, name the question rather than assume there is nothing to read.

## Select and read

Inspect the header of every file of the product's guidelines and the complete kind index in
`guidelines/coding.md`, where it exists. Read whole every file whose *Applies to* names an
affected part; a file `guidelines/coding-<kind>.md` only where its index row's *When to read* also
matches the work. The general coding file stays in the reading when no kind row matches; an
unindexed kind does not remove it. Never replace a file with excerpts or a review checklist.

A current decision of the product's log that departs from a discipline's guidelines applies only
to the parts and work it expressly covers (WAY-217): for them, an absent file of that discipline
is not missing; a departure for one part does not exempt another. An agent cannot infer a
departure from the absence of a file.

Name missing, malformed or contradictory metadata as a finding to resolve, including an index row
whose file is absent. An uncertain condition is a question, not a nonmatching row. Never silently
turn these cases into an empty reading or call a file absent merely because its metadata needs
correction.

When the work reaches a part the selection did not cover — a file the change did not expect to
touch, a scope grown in clarification — the agent doing the work reads that part's guidelines
itself before relying on them, and an agent of the task cycle names that reach in its report. A
reach does not update a list of selected files; the report names it.

## Distinguish the gaps

Discovery uses the common form above; the response follows when the discipline's guidelines come
into being:

- A user interface with no styleguide, or code work in a product with no `guidelines/coding.md`,
  lacks discipline guidelines, whether the product is new or already has screens or code.
  A scoped departure removes that finding only within its scope. A task writing the missing
  guidelines does not wait for its own output; still name what it is to create.
- An existing general coding file omitting an affected code part is read as the source to
  extend, not reported as an absent file. Extension or correction of existing guidelines belongs
  in the current task unless the human separates it, even when the extension is substantial
  (WAY-172, WAY-199). Changed meanings and exemplars retain their approval routes.
- A kind absent from the general index whose first file this task creates needs its exemplar,
  kind guidelines and index row in that task, without a separate exemplar prerequisite
  (WAY-216). The general file must still exist unless this task writes it or a departure applies.
- Where files of an unindexed kind already exist, name that discrepancy and route their
  comparison and exemplar selection through `maintain-coding-guidelines` under WAY-200. Do not
  call the next file the first or use the finding to authorize an unrelated audit.

## Hand the findings back

Give each finding, its source and consequence to the owning workflow: `refine-task` places
questions, prerequisite work and the return after its merge (WAY-215); `plan-project` places
preparatory tasks and dependencies within the approved definition (WAY-218). An agent of the task
cycle names its finding in its report, and the orchestrator in the cycle record: one that changes
what the task needs stops the cycle, which opens a blocked draft request showing it, as
`implement-task` gives where the required outcome cannot be made; one needing a foundation entry the
task, any spec and the foundation leave open is an open design choice, returned without code for a
spec (WAY-135); one that would change an approved decision beyond what the task document or plan
carries is a question the cycle's foundation step allows (WAY-30). Record the pause or question
through that workflow before dependent work, continue independent work where allowed, and invent no
status or silent waiver.
