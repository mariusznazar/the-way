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

Read the product root `AGENTS.md` section `## Backlog` to find the task system, as
`project-level/backlog_place.md` gives. Check whether it can hold the whole document. If it holds
short task lines only, create a separate Markdown document in the product's task area and link it
from that line; do not paste the document into a checklist item. If the document's location is
unclear, ask once and offer to record it as that file gives.

Where the task has no line there yet, make it as `project-level/task_line.md` gives, which also
says when. The rules of the task place come from the `## Backlog` section too, as
`project-level/backlog_place.md` gives; a missing entry of them is asked about once, like a
missing place.

Check that this is one task. Keep one task by default: each split adds a full cycle. Identify a
split only where a part cannot start or finish without something outside this refinement — access
the agent lacks, another task's result — or where the parts change different repositories, since
the cycle writes only in the product's repository, or where a later step of this skill offers one,
and name that reason (WAY-372). For a task's size alone say nothing of a split: no mention, no
question, no recommendation; the human sees the whole document and may ask for a split. For a
project member, update its plan through the owning workflow before refining either new item; for
another task, ask which item to refine first. Read product files to answer factual questions before asking
the human.

Read the product's guidelines of the parts this task touches by `product-guidelines/reading.md`,
naming the parts from the task's required behaviour even before its files exist (WAY-214). Carry
its findings—guidelines missing, malformed or uncertain—to step 3. When clarification brings the
task to a part this reading did not cover, read that part's guidelines.
