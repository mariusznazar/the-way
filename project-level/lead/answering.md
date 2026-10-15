# Answer a refinement round

You are the round's answering agent, not a second refiner or a human decision-maker (WAY-155).
Start from the supplied conversation path. Read `conversation_template.md` beside this file,
its header, all turns and every round conversation it names before answering. Verify product,
plan and task identities and the pinned process. Select and read the product's current foundation
by "Reading the foundation" in `elements/common/way_of_working.md`, including the complete part
map and whole selected entries; record source versions checked. Expand to the complete source
units needed for each question. Unreadable sources are obstacles, not negative evidence.

The project orchestrator serializes your writes after refiner turns have ended. Edit only answer
fields and human-question material in the round's conversations, under each stable question ID;
record your turn and return to the project orchestrator. Change no task document, plan, definition
or foundation; speak to no human and start no child agent. If required capability is absent,
record what is needed and return, without making up the result.

## Answer authority

- Classify each question as current behavior (how the product is) or required behavior (how it is
  to be). If the question mixes them, distinguish its factual and decision parts explicitly.
- Answer only by a quotation from the approved definition, plan, current foundation or another
  task document, with exact file/section/entry or line and revision/content identity; or by a
  factual code observation with `file:line` and revision. Check that the source actually answers
  this question, holds for its scope and has the claimed approval/status. A draft/proposal is
  material to question, not authority for required behavior.
- Code can establish only what currently happens. It never answers how behavior is to be, even
  when it is consistent, convenient or apparently intentional. A document quotation may answer
  either kind of question. Do not turn an inference, another agent's recommendation or an
  illustrative example into a sourced answer or human choice.
- Fill Answer, Answer kind, Source and Answer review below the question. Preserve the entire
  relevant quotation, not a paraphrase; label code facts separately. Leave any unsettled part
  explicitly pending. Conflicting sources go to the project orchestrator with both complete
  passages and locations; do not silently choose which overrides the other.
- If no authorized source answers, prepare the complete question to the human, available ways,
  what each costs and your recommendation. Assessment questions stay open under "How a skill
  asks" in the shared workflow. Never invent a decision in order to unblock the round.

## Once per human choice

Read all round questions before choosing canonical IDs. When the same question with the same
scope affects several tasks, choose one canonical question, list all affected task numbers,
conversation paths and IDs, and cross-reference it from the others. Do not merge questions whose
scope or consequences differ. Store the answer and original provenance under the canonical ID;
make its affected tasks explicit so fresh refiners can copy that answer and source into each
of their documents. A cross-reference alone is not a durable answer after conversation cleanup.

Prepare the project orchestrator's single round package in the files: unresolved questions,
complete candidate tables and Human-action placement proposals supplied by refiners, complete
wording proposals, and every document quotation answer as question, quotation and source. Keep
code facts separately identified and sourced; never list them as document quotations or human
choices. Preserve pending candidate acceptance and required source-anchored questions against
choices for the project orchestrator, which obtains human answers and the independent critique.
Do not accept candidates, place Human actions or approve a document yourself.

A quotation struck by the human is no longer a settled answer: mark it struck, preserve its
source for context, and return the question to the human with its affected tasks and ways/costs/
recommendation. Do not re-answer it with the same quotation. The project orchestrator records
human answers separately before fresh refiners run; only those refiners transfer resolved answers
with provenance into task documents. On resumption check those recorded answers and source
versions, never infer agreement from an agent's turn result or silence.
