# Respond to guideline findings

Read this file in step 3 of `SKILL.md` when the shared guideline reading reports findings
(WAY-215, WAY-216).

## Missing discipline guidelines

Missing discipline guidelines keep this task `waiting for human`, with a named question in
*Questions to settle* awaiting a separate guidelines task's merge, even in a product with screens,
code or tests. Continue refinement independent of that answer. A scoped departure applies only where
the shared reading establishes it; the task writing the missing guidelines does not wait for itself.
For an independent or source-only task, propose the prerequisite and, after human approval, add its
task to the product backlog using step 1's document conventions. For a plan member, return
`plan change` if the plan lacks it, or `waits for task <n>` for the named question if the plan holds
it; the owning project workflow writes the plan. The task document's `waiting for human` does not
set the plan row's state: preserve the question-specific waiting rules, which may leave that row
`to refine`.

After the prerequisite merges, resume here, read its guidelines and settle the meanings this task
needs under WAY-172 before step 6's complete-document acceptance. Adding the dependency alone gives
no readiness. Use `maintain-styleguide`, `maintain-coding-guidelines` or
`maintain-testing-guidelines` for their matters of refinement. A missing coding and missing testing
guidelines may be one prerequisite task (WAY-247).

## Existing guidance and first exemplars

Keep extension or correction of existing guidelines in this task, including a coding file whose
*Applies to* omits the affected part, unless the human separates the work. Settle new meanings and
exemplar changes through those discipline skills under WAY-172 and WAY-199.

For a genuinely first unindexed kind, add to *To do* designation of its first file as exemplar, its
kind guidelines and the general index row through `maintain-coding-guidelines`, without a separate
exemplar wait. Existing unindexed files instead need the comparison WAY-200 requires; record the
discrepancy and route that work within this task's scope, and for a plan member respect its plan
boundary.

For a task whose required outcome is itself the first test of a level whose recipe has an empty
*Exemplar*, add to *To do* that this test becomes the level's exemplar, naming the level and no path,
through `maintain-testing-guidelines`, without a separate exemplar wait. Where the task's tests are
its cycle's choice, add no designation: the cycle proposes one for a level's first test at a blocked
draft request (WAY-242, WAY-238).

## Step 6: readiness after a scope change

If the final scope reaches a part the step 1 reading did not cover, read that part's guidelines. A
missing-discipline question still awaiting its task's merge, or unresolved classification or
metadata, prevents readiness. A recorded dependency or an empty reading does not answer it.
