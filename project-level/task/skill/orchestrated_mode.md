# Orchestrated refinement

When a project orchestrator dispatches you with a conversation-file path, use the common workflow
in `SKILL.md` with the routing below (WAY-134, WAY-154, WAY-155). Read the file and
`project-level/lead/conversation_template.md` first; verify its product, plan, task identity and
process pin. Resume from its recorded next actor and all turns, checking sources again. Consume
recorded answers before proceeding; do not repeat a settled presentation/question unless its
meaning or source has changed. A missing or mismatched file/source is an `obstacle`, not permission
to guess or overwrite another task.

- Every question or presentation this skill or a borrowed skill would otherwise address to the
  human goes into your conversation turn, then you end the turn. This includes task location,
  which task to refine, goal/scope/wording, conflicting decisions, deployment-work splits,
  Human-action placement/completion, candidate acceptance/rejection, questions against choices
  and final complete-document approval. Supply complete material, available ways, costs and a
  recommendation where "How a skill asks" requires them. Never ask the human directly.
- Use `find-foundation-entries` in task mode for its source search and candidate table, but return
  its human-presentation steps and required critique/child-work requests through this file.
  Start no child agent. The project orchestrator performs dispatches and presents the round
  package, candidates and required WAY-113 questions; you approve nothing on its behalf.
- A run of the step that settles technology (WAY-265), whether `refine-task` starts it for a
  reserved choice or the human asked for it, is led through this file by
  `project-level/technology/task_run.md`.
  Write the request for it as a *Child-work request* in your turn, never as a question: it names
  the choice, the note the run is for and the path of this task document. Every question the run
  would address to the human (the list to confirm, the table of choices, the choice itself) goes
  into the turn as human material, and you end the turn. Only you write the document: the
  section *Technology*, the settled question and its three fields are written by you, from the
  research, the critique and the tests the project orchestrator brings back and from the human
  answers recorded in the file. Where the answerer marked another member's request canonical,
  wait for that run, then copy its settled question whole, with *Answer*, *Not chosen*, *Source* and
  the three fields, into your document and end your item `— settled: <question>`. The result stays
  one of the five; `questions` carries the run.
- Edit only your task document and your conversation turn. Do not write the shared plan,
  definition or foundation, nor launch implementation. Record a mismatch requiring upstream work
  as `plan change`, with evidence and the requested change. An unavailable source/capability or
  conflict preventing a valid next step is `obstacle`, with what resolves it.
- Transfer every resolved answer, including canonical answers shared across tasks, with its
  original source and the ways the human did not choose into Questions to settle before relying
  on it (WAY-134). Preserve human words separately
  from document quotations and factual code observations; code cannot prescribe required product
  behavior. A human-struck quotation returns as a human question, never a settled requirement.
- Carry human-accepted candidates whole; remove rejected rows only on the recorded human answer,
  keeping the shown/accepted counts. Pending selection or a required unanswered challenge keeps
  the task unfinished. Likewise, only the human places Human actions and confirms completion.
- `Depends on` alone does not prevent refinement. Use `waits for task <n>` only for a named question
  that needs the result of task n held by the plan; keep that question/reason in both documents.
- Finish by recording evidence and one exact result: `questions`, `waits for task <n>`,
  `ready for approval`, `plan change` or `obstacle`. The final nonempty line of the conversation
  and your entire short return are the identical phrase, with the actual number for `<n>`.
  `questions` routes remaining questions/material to the round answerer and project orchestrator;
  `ready for approval` means all checks except final whole-document acceptance pass. It is a turn
  result, never a task Status. Use `refining` or `waiting for human` as applicable; never write
  `ready for cycle`. The project orchestrator alone changes that Status after the human accepts
  the exact complete document, one at a time, and handles plan updates and safe cleanup.

## Step 6: hand off for acceptance

When the common checks pass, place the complete document and acceptance request in the conversation
and return `ready for approval`. This is a turn result, not the task Status. Leave the final Status
write to the project orchestrator, which updates it only after the human accepts the exact complete
document, one task at a time. No definition awaiting its gate permits readiness.
