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
WAY-155).

Manual refinement uses the direct conversation in the steps below. Both modes require final
human acceptance of the complete task, even when refinement finds no candidate settlements.

## 1. Read the sources

- Read the template in full, the "How a skill asks" section of
  `elements/common/way_of_working.md`, and any existing wording of this task. Select and read the
  product's current foundation by "Reading the foundation" in that shared file (WAY-150).
  Determine from the request whether it is independent, belongs to a project plan, or uses
  a project's settlements without plan membership. Record that relationship; do not infer
  membership merely because a project definition is a source.
- For a plan member, follow [`project_plan_task.md`](project_plan_task.md) for its approved
  definition, plan item and checks. For a task using project settlements without plan membership,
  follow [`source_only_task.md`](source_only_task.md). An independent task needs neither file.
- Read the product root `AGENTS.md` section `## Backlog` to find the task system. Check whether
  it can hold the whole document. If it holds short task entries only, create a separate Markdown
  document in the product's task area and link it from that entry; do not paste the document into
  a checklist item. If the document's location is unclear, ask once and offer to record it in
  the backlog guidance.
- Check that this is one task. If it joins independent outcomes, identify the split. For a
  project member, update its plan through the owning workflow before refining either new item;
  for another task, ask which item to refine first. Read product files to answer factual
  questions before asking the human.
- Read the product's guidelines of the parts this task touches by `product-guidelines/reading.md`,
  naming the parts from the task's required behaviour even before its files exist (WAY-214).
  Carry its findings — guidelines missing, malformed or uncertain — to step 3. When clarification
  brings the task to a part this reading did not cover, read that part's guidelines.

## 2. Draft from what is known

- Give the task an editable title. Preserve the human's wording and the approved project's
  meaning; structure them without translating them into an invented technical design.
- Create or update the document in the product's task place once its goal is clear. Use `TODO`
  for missing information and `Status: refining`. Give its full path to the human. For a task
  already in its cycle, leave its frozen task document intact and route a scope change through
  the cycle's question and record.
- A task document written before and not yet in its cycle, an accepted one included, is refined
  from its text: its answers and the accepted rows of *Settlements to record* stand with their
  sources, and only what the human reopens, and what a reopened answer changes, is settled again.
  Its status returns to `refining` and is not `ready for cycle` again until the human accepts the
  whole changed document (WAY-124); steps 4 to 6 run on the whole document.
- Keep Description to what an implementer needs to take the task. Put likely follow-up answers
  in Context. If a block's place is uncertain, move it to Context. Do not ask questions merely
  to fill Context, and do not invent acceptance criteria.
- Show the whole current task document when asking for a wording decision. A suggestion not
  supported by the human or an approved source appears as `Proposal:` outside the document and
  enters it only after acceptance.

## 3. Resolve the gaps

- Ask about the most consequential missing answer first, with one sentence explaining what it
  blocks. Put each answer under its question and update the document before asking the next.
  If the answer is in the approved project definition or foundation, quote the exact wording
  with its location instead of asking the human; an inference is not an approved answer.
- If two answers conflict, show both and ask which holds. If the answer changes the approved
  project definition or a current foundation decision, route that change to its own process;
  do not silently settle it inside the task.
- Settle known product choices needed to state the task's outcome before the cycle. A choice of
  implementation method stays with the cycle's plan, or with the choices of its cycle record where
  no plan is written. An unanswered question that blocks taking the task keeps `Status: waiting
  for human`; never turn it into an apparently executable `To do`
  item. A new choice discovered during the cycle belongs in its decision record for the PR.
- For a plan member or source-only task, reconcile the questions assigned to it as described in
  the corresponding file named in step 1. Answer a question that determines required product
  behavior in this document; reproduce an implementation question under `Questions carried to
  cycle`. Do not let a question in the task's scope disappear.
- Name under *Human actions* the human action through which a human makes each effect the task
  has outside the product's repository; a read outside the repository stays with the agent
  (WAY-140). For each human action, propose its placement by that section's rule in the template,
  and have the human place it, asked as "How a skill asks" says (WAY-140). A human action placed
  before the cycle and not yet done keeps `Status: waiting for human`; mark it `done` once the
  human has performed it (WAY-124).
- When the task's outcome deploys the product or changes how or where it runs, check that the
  product has a deployment skill covering every item of the list WAY-139 holds, in
  `<the-way>/foundations/decisions.md`. Where it has none or an item is missing, add an item to
  *To do* for that work and offer the human to split it into a task of its own, which step 1
  then handles (WAY-139). A task with no such outcome takes no check.
- Resolve the shared guideline reading's findings by their kind in
  [`guideline_findings.md`](guideline_findings.md) (WAY-215, WAY-216).

## 4. Carry the foundation decisions

- Carry under *Decisions in play* the current decisions the task touches, as "Reading the
  foundation" of step 1 selects them for the task's scope, each by its identifier with its current
  wording quoted. If a project definition is a source, bring in its relevant approved projected
  wording. For plan assignment or source-only handling of projected entries, follow the file named
  in step 1 for that task relation (WAY-124, WAY-126).
- For a plan member, follow `project_plan_task.md` to compare numbered work, dependencies and
  projected entries with its plan item. A mismatch returns to the plan, not an unrecorded change
  in this document.
- If the task would contradict a current decision or a projected entry, show the conflict and
  its consequences. The human chooses whether to change the task or reopen the upstream
  settlement. Do not replace approved wording with the agent's paraphrase.
- An exclusion that survives this task and that later work builds on is a decision candidate,
  worded as what the product does today, not an item under `Out of scope` (WAY-26).

## 5. Find what the refinement settles

- Once the gaps are resolved and the decisions in play carried, find what the refinement settled
  that binds after the task's merge, through `find-foundation-entries` with the task as its caller:
  the source is the task document, the conversation that refined it and the material the task
  started from; the next reader is the task's cycle; the mode is rows of the document's section
  *Settlements to record* (WAY-134). This runs for every task, whatever its project relation: a
  project member and a source-only task add their own settlements beside the projected entries
  they carry.
- Refinement searches no more of the foundation than step 1 reads and *Decisions in play*
  carries. The one search of the whole foundation is the cycle's, when it writes each kept row
  (WAY-33); a kept row that search finds already stated becomes no second entry, and one whose
  meaning cannot hold against what it finds goes back to the human, as WAY-134 gives both.
- Where the document already holds accepted rows from an earlier refinement, a row the human
  reopens, or whose source this refinement changed or removed, is a candidate again; every other
  accepted row enters the working table `accepted` and is not cut again. The counts of the
  `Candidates:` line cover this refinement's working table.
- A candidate that collides with a current decision or a projected entry goes back to step 4 as a
  conflict; one that changes the task's scope goes back to step 3.

## 6. Review and hand off

- When the draft is complete, show it whole. Propose any block to move from Description to
  Context or remove, with a short reason for each; apply the moves the human accepts. If there
  is nothing worth moving, say so and continue.
- Check that every blocking question has an answer, the numbered work is executable, the
  questions brought into this task are accounted for, the decisions in play are present or
  `none` where the reading of the foundation found none, *Settlements to record* opens with its
  `Candidates:` line and holds no row awaiting the human, and *Human actions* reads `none` or has
  every human action placed and every human action before the cycle done (WAY-124, WAY-140). For a
  plan member, check the assignment by `project_plan_task.md`; for any task using approved project
  settlements, check the definition's approval and that every projected entry its code makes true
  is marked with the part made true. Report an obstacle instead of declaring readiness when a
  check fails.
- Follow `guideline_findings.md` for a newly reached part, an unresolved classification or
  metadata, or a missing-discipline question still awaiting its task's merge; a recorded dependency
  or an empty reading does not answer it.
- Once these checks pass, show the complete final document and explicitly ask the human to accept
  that document, then wait. Acceptance of candidates, Human-action placement or an earlier draft
  is not this acceptance. Keep `Status: waiting for human` until it is given, including a task
  with no candidates. Apply requested changes and show the complete revised document again. In
  manual mode mark `Status: ready for cycle` only after this acceptance and all applicable checks
  pass (WAY-124). For the orchestrated handoff and status, follow `orchestrated_mode.md`. No
  definition awaiting its gate permits readiness.
- The task document carries what and why. Do not insert a separate implementation spec, test
  plan, or execution log here. The task cycle records those in its cycle record.
