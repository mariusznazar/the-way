# Read the sources

Read the task template in full, the "How a skill asks" section of
`elements/common/way_of_working.md`, and any existing wording of this task. Select and read the
product's current foundation by "Reading the foundation" in that shared file (WAY-150). Determine
from the request whether it is independent, belongs to a project plan, or uses a project's
settlements without plan membership. Record that relationship; do not infer membership merely
because a project definition is a source.

- For a plan member, follow `project_plan_task.md` for its approved definition, plan item and
  checks.
- For a task using project settlements without plan membership, follow `source_only_task.md`.
- Whenever an approved definition is used, run
  `python -B <the-way>/project-level/readiness_check.py <definition>` before relying on its
  approval; a finding returns to `define-project`.

Read the product root `AGENTS.md` section `## Backlog` to find the task system. Check whether it
can hold the whole document. If it holds short task entries only, create a separate Markdown
document in the product's task area and link it from that entry; do not paste the document into a
checklist item. If the document's location is unclear, ask once and offer to record it in the
backlog guidance.

Check that this is one task. If it joins independent outcomes, identify the split. For a project
member, update its plan through the owning workflow before refining either new item; for another
task, ask which item to refine first. Read product files to answer factual questions before asking
the human.

Read the product's guidelines of the parts this task touches by `product-guidelines/reading.md`,
naming the parts from the task's required behaviour even before its files exist (WAY-214). Carry
its findings—guidelines missing, malformed or uncertain—to step 3. When clarification brings the
task to a part this reading did not cover, read that part's guidelines.
