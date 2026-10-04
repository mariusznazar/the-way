---
name: refine-task
description: Use to define or refine one task of an approved the-way project before its implementation cycle. Produces a task document with scope, answered questions and the foundation decisions it carries; not for defining a project or writing the implementation plan.
---

# Refine a task

Turn one proposed task into a document another agent can take through the task cycle. The
document's form and each section's rule stand in `project-level/task/template.md`; the way to
ask the human stands in `elements/common/way_of_working.md`. This skill holds the order of work.

This skill lives in `project-level/task/skill/` of the-way. When installed globally, resolve the
link to find the process root. In a product, read the pinned `.the-way` commit; another the-way
skill named here is the product skill with the `the-way-` prefix.

## 1. Read the sources

- Read the template in full, the "How a skill asks" section of
  `elements/common/way_of_working.md`, the project definition, the project's task plan, the
  product foundation, and any existing wording of this task. Run
  `python -B <the-way>/project-level/readiness_check.py <definition>` before treating the
  definition or its projected entries as approved. A finding returns to `define-project`.
  If a task plan or approved definition is absent, report the gap; a draft may be refined,
  but it cannot be marked ready.
- Identify the exact plan item, its dependencies, and the projected entries assigned to it.
  Copy its identifier or link into `Plan item:`. A proposed split or scope change goes back to
  the project plan before either resulting task can be ready.
- Read the product root `AGENTS.md` section `## Backlog` to find the task system. Check whether
  it can hold the whole document. If it holds short task entries only, create a separate Markdown
  document in the product's task area and link it from that entry; do not paste the document into
  a checklist item. If the document's location is unclear, ask once and offer to record it in
  the backlog guidance.
- Check that this is one task. If the request joins independent outcomes, identify the split
  and update the plan through its owning workflow before refining either new item. Read product
  files to answer factual questions before asking the human.

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
- A product choice must be settled before the cycle. A choice of implementation method stays
  with the cycle's plan. An unanswered question that blocks the task keeps `Status: waiting for
  human`; never turn it into an apparently executable `To do` item.
- Reconcile every open question whose resolver in the project definition names this plan item.
  Answer a question that determines product behavior in this document; reproduce an
  implementation question under `Questions carried to cycle`. Do not let either disappear.

## 4. Carry the foundation decisions

- From the project's assignments and the approved definition, bring in the exact approved
  projected entries this task realizes or writes. Search the current foundation for decisions
  the task touches, including an unlinked collision; quote their current wording and version.
- Compare the task's numbered work, dependencies and projected entries against the identified
  plan item. A mismatch returns to the plan, not an unrecorded change in this document.
- If the task would contradict a current decision or a projected entry, show the conflict and
  its consequences. The human chooses whether to change the task or reopen the upstream
  settlement. Do not replace approved wording with the agent's paraphrase.
- An exclusion that survives this task is a decision candidate, not an item under `Out of scope`.

## 5. Review and hand off

- When the draft is complete, show it whole. Propose any block to move from Description to
  Context or remove, with a short reason for each; apply the moves the human accepts. If there
  is nothing worth moving, say so and continue.
- Check that every blocking question has an answer, the numbered work is executable, the
  assigned project questions are accounted for, the plan item and its assignments match,
  the decisions in play are present or explicitly `none` after a search, and the project
  definition still passes its approval check. Mark `Status: ready for cycle` only then;
  report any remaining obstacle instead of declaring readiness.
- The task document carries what and why. Do not insert a separate implementation spec, test
  plan, or execution log here. The task cycle records those on the task branch.

Use the language the human opened in for conversation and document content.
