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

## 1. Read the sources

- Read the template in full, the "How a skill asks" section of
  `elements/common/way_of_working.md`, and any existing wording of this task. Select and read the
  product's current foundation by "Reading the foundation" in that shared file (WAY-150).
  Determine from the request whether it is independent, belongs to a project plan, or uses
  a project's settlements without plan membership. Record that relationship; do not infer
  membership merely because a project definition is a source.
- If the task belongs to a project, read its approved definition and its plan, whose form
  `project-level/plan/template.md` gives, and run
  `python -B <the-way>/project-level/plan_check.py <plan>`; a finding returns to `plan-project`.
  Identify the plan item by its name, its dependencies, the projected entries it realizes or
  writes and the open questions the plan places in it (WAY-142, WAY-145, WAY-147). A proposed
  split or scope change goes back to the project plan before either resulting task can be ready.
- If the task uses a project's settlements without belonging to its plan, read that definition
  in full but take no plan assignment or dependency from it. Select the goal, scope, technology,
  projected entries and open questions relevant to the stated task. An independent task requires
  neither definition nor plan. Whenever an approved definition is used, run
  `python -B <the-way>/project-level/readiness_check.py <definition>` before relying on its
  approval; a finding returns to `define-project`.
- Read the product root `AGENTS.md` section `## Backlog` to find the task system. Check whether
  it can hold the whole document. If it holds short task entries only, create a separate Markdown
  document in the product's task area and link it from that entry; do not paste the document into
  a checklist item. If the document's location is unclear, ask once and offer to record it in
  the backlog guidance.
- Check that this is one task. If it joins independent outcomes, identify the split. For a
  project member, update its plan through the owning workflow before refining either new item;
  for another task, ask which item to refine first. Read product files to answer factual
  questions before asking the human.

## 2. Draft from what is known

- Give the task an editable title. Preserve the human's wording and the approved project's
  meaning; structure them without translating them into an invented technical design.
- Create or update the document in the product's task place once its goal is clear. Use `TODO`
  for missing information and `Status: refining`. Give its full path to the human. For a task
  already in its cycle, leave its frozen task document intact and route a scope change through
  the cycle's question and record.
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
  implementation method stays with the cycle's plan. An unanswered question that blocks taking
  the task keeps `Status: waiting for human`; never turn it into an apparently executable `To do`
  item. A new choice discovered during the cycle belongs in its decision record for the PR.
- For a project member, reconcile every open question the plan places in its item. For a
  source-only task, reconcile the project questions explicitly brought into this task, without
  absorbing the project's other work. Answer a question that determines required product
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

## 4. Carry the foundation decisions

- Search the current foundation for decisions the task touches, including an unlinked
  collision; quote their current wording and version. If a project definition is a source,
  bring in its relevant approved projected wording. For a project member, use the plan to
  identify which entries it is assigned to realize or write. A source-only task takes no plan
  assignment, but its cycle writes a projected entry its code will make true: mark that entry
  under *Decisions in play* with the part made true now, also when the plan assigns it to another
  task (WAY-124, WAY-126).
- For a project member, compare the numbered work, dependencies and projected entries with its
  plan item. A mismatch returns to the plan, not an unrecorded change in this document.
- If the task would contradict a current decision or a projected entry, show the conflict and
  its consequences. The human chooses whether to change the task or reopen the upstream
  settlement. Do not replace approved wording with the agent's paraphrase.
- An exclusion that survives this task is a decision candidate, not an item under `Out of scope`.

## 5. Find what the refinement settles

- Once the gaps are resolved and the decisions in play carried, find what the refinement settled
  that binds after the task's merge, through `find-foundation-entries` with the task as its caller:
  the source is the task document, the conversation that refined it and the material the task
  started from; the next reader is the task's cycle; the mode is rows of the document's section
  *Settlements to record* (WAY-134). This runs for every task, whatever its project relation: a
  project member and a source-only task add their own settlements beside the projected entries
  they carry.
- A candidate that collides with a current decision or a projected entry goes back to step 4 as a
  conflict; one that changes the task's scope goes back to step 3.

## 6. Review and hand off

- When the draft is complete, show it whole. Propose any block to move from Description to
  Context or remove, with a short reason for each; apply the moves the human accepts. If there
  is nothing worth moving, say so and continue.
- Check that every blocking question has an answer, the numbered work is executable, the
  questions brought into this task are accounted for, the decisions in play are present or
  explicitly `none` after a search, and *Settlements to record* opens with its `Candidates:` line,
  no row awaiting the human, and *Human actions* reads `none` or has every human action placed
  and every human action before the cycle done (WAY-124, WAY-140). For a project member, also
  check its plan item and assignments; for any task using approved project settlements, check
  the definition's approval and that every projected entry its code makes true is marked with the
  part made true. Mark `Status: ready for cycle` only when its applicable checks pass; report an
  obstacle instead of declaring readiness.
- The task document carries what and why. Do not insert a separate implementation spec, test
  plan, or execution log here. The task cycle records those in its cycle record.
