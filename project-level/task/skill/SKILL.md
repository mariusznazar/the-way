---
name: refine-task
description: Use to define or refine one product task before its the-way implementation cycle, whether independent, in a project plan, or based on a project's settlements without belonging to it. Not for defining a project or writing the implementation plan.
---

# Refine a task

Turn one proposed task into a document another agent can take through the task cycle. The
document's form and each section's rule stand in `project-level/task/template.md`; the way to
ask the human stands in `elements/common/way_of_working.md`. This skill holds the order of work.

This skill lives in `project-level/task/skill/` of the-way. In the-way itself, read it in the
checkout or worktree the session works in; in a product, at the pinned `.the-way` commit.
Another the-way skill named here is the project skill with the `the-way-` prefix.

## Orchestrated mode

When a project orchestrator dispatches you with a conversation-file path, read and follow
[`orchestrated_mode.md`](orchestrated_mode.md) before the common workflow below (WAY-134, WAY-154,
WAY-155). For a run of the step that settles technology (WAY-267), whether `refine-task` starts it
for a reserved choice or the human asked for it, that file points to
`project-level/technology/task_run.md`.

Manual refinement uses the direct conversation in the steps below. Both modes require final
human acceptance of the complete task, even when refinement finds no candidate settlements.
The task document carries what and why. Do not insert a separate implementation spec, test plan
or execution log; the task cycle records those in its cycle record.

## 1. Read the sources

Follow [`read_sources.md`](read_sources.md) to identify the task relationship and read its sources.
For a plan member, it points to [`project_plan_task.md`](project_plan_task.md); for a task using
project settlements without plan membership, it points to
[`source_only_task.md`](source_only_task.md). An independent task needs neither file.

## 2. Draft from what is known

Follow [`draft.md`](draft.md) when setting up or resuming the task document.

## 3. Resolve the gaps

Follow [`resolve_gaps.md`](resolve_gaps.md) for questions, choices, human actions and deployment
coverage. When the task's outcome needs a language, a framework, a library, a store of data, a way
of logging in or a place to run that no decision, approved definition or accepted answer settles,
it points to `project-level/technology/reserved_choices.md`. Resolve findings from the shared
guideline reading by kind in [`guideline_findings.md`](guideline_findings.md) (WAY-215, WAY-216).

## 4. Carry the foundation decisions

Follow [`carry_foundation.md`](carry_foundation.md) to carry and compare decisions in play.
An exclusion that survives this task and that later work builds on is a decision candidate,
worded as what the product does today, not an item under `Out of scope` (WAY-26).

## 5. Find what the refinement settles

Follow [`find_settlements.md`](find_settlements.md) to identify and route candidate settlements.

## 6. Review and hand off

Follow [`final_review.md`](final_review.md) to check the complete task, obtain its final human
acceptance and hand it off. For a newly reached part, unresolved guideline classification or
missing-discipline question, also follow `guideline_findings.md`.
