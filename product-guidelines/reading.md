# Reading a product's guidelines

Use this procedure in task refinement, project breakdown, task planning and the task cycle
(WAY-213, WAY-214, WAY-218). Read it from the checkout or pinned the-way the calling workflow
uses. The inputs are the proposed change or approved project scope, the current product
foundation and files, and any earlier selection with its reasons. The result is the affected
parts with evidence, selected guideline paths with reasons, and named gaps or questions, kept
in the caller's existing document or report. It is no second catalogue of guideline contents.

## Find the affected work

Read the complete part map. Connect the required behaviour to its responsibilities, files,
critical flows and surfaces; inspect existing product files to establish what is already there.
Identify the parts the work affects, whether it changes a user interface or writes code, and
which kinds of code it creates or changes. A backend's admin panel is a user interface; helper
and build scripts are code. Names and file extensions alone do not settle the classification.
An API or terminal alone is no user interface in the styleguide's sense (WAY-183).

Before files or a diff exist, classify the announced behaviour in the same way. If the map has
no part for it, keep its identity as a question in the owning workflow until settled; additions
to the map follow that workflow's foundation rules and known files, not invented assignments.
Expand the reading where a responsibility, kind or reading condition is unclear; if it stays
unclear, record the question rather than assume there is nothing to read.

## Select and read

Inspect the header of every file of the product's guidelines and the complete kind index in
`guidelines/coding.md`, where it exists. Select every file whose *Applies to* names an affected
part. For `guidelines/coding-<kind>.md`, also require its index row's *When to read* to match
the change. Inspect the selected files' reading conditions and read each selected file whole.
The general coding file remains relevant when no kind row matches; an unindexed kind does not
remove it from the selection. Do not replace the sources with excerpts or a review checklist.

Read current product decisions for an adopted departure from a discipline's guidelines. Apply
it only to the parts and work its decision expressly covers (WAY-217); a departure for one part
does not exempt another. Record the decision and the reason the selection or missing-file
finding changes. An agent cannot infer a departure from the absence of a file.

Name missing, malformed or contradictory metadata as a finding to resolve, including an index
row whose file is absent. An uncertain condition is a question, not a nonmatching row. Never
silently turn these cases into an empty selection or call a file absent merely because its
metadata needs correction.

## Distinguish the gaps

Discovery uses the common form above; the response follows the discipline's creation timing:

- A user interface with no styleguide, or code work in a product with no `guidelines/coding.md`,
  lacks discipline guidelines, whether the product is new or already has screens or code.
  A scoped departure removes that finding only within its scope. A task writing the missing
  guidelines does not wait for its own output; still record what it is to create.
- An existing general coding file omitting an affected code part is read as the source to
  extend, not reported as an absent file. Extension or correction of existing guidelines belongs
  in the current task unless the human separates it, even when the extension is substantial
  (WAY-172, WAY-199). Changed meanings and exemplars retain their approval routes.
- A kind absent from the general index whose first file this task creates needs its exemplar,
  kind guidelines and index row in that task, without a separate exemplar prerequisite
  (WAY-216). The general file must still exist unless this task writes it or a departure applies.
- Where files of an unindexed kind already exist, record that discrepancy and route their
  comparison and exemplar selection through `maintain-coding-guidelines` under WAY-200. Do not
  call the next file the first or use the finding to authorize an unrelated audit.

Give each finding, its source and consequence to the owning workflow: `refine-task` places
questions, prerequisite work and the return after its merge; `plan-project` places preparatory
tasks and dependencies within the approved definition. A cycle finding that changes what the
task needs returns to refinement; one needing a new foundation meaning takes the cycle's
foundation route. Record the pause or question through that workflow before dependent work,
continue independent work where allowed, and invent no status or silent waiver.

## Refresh and hand back

Check an earlier selection against the scope and sources now being used. Refresh when either
changes, and on author return and reconciliation against the actual changed files and affected
parts, before dependent dispatch. Record new paths, changed reasons and unresolved findings in
the existing record. Each receiving agent verifies the selection against its own work, reads the
selected files whole and returns any expansion or discrepancy in its report. Reuse an earlier
selection only while its scope and sources still support it.
