# Spec — Wybór technologii, której projekt nie ustalił, wraca do Mariusza zamiast zapaść po cichu w zadaniu

- Task: `.runs/task-cycles/unsettled-technology-returns/task.md`
- Open choice: five choices the task leaves open — where the technology step's list and a settled
  choice stand in a task document; what a blocked draft request with no code holds; how the next
  cycle of the same task names its record, what happens to its branch and who moves a plan row
  back; where the stopping rule stands and how a run at a task lives beside a run at a definition;
  which foundation entries the change writes or changes.

## Intent

A technology choice that a project never settled is today made by whichever agent meets it, and
Mariusz first sees it in the request, with code already standing on it. This change gives such a
choice one way back to him: `settle-technology` can run at a task document, refinement sends a
reserved choice there, and a cycle that meets one stops without code instead of picking the smallest
reversible reading. The answers to the task's questions 1–7, its *To do* and its three rows of
*Settlements to record* are settled; this spec settles only how they take shape.

## Goals and non-goals

Goals, each tied to the task's *To do* and to the decision below that carries it:

| To do | What the change achieves | Decision |
|---|---|---|
| 1, 3 | `settle-technology` runs at a task document with a note saying what for; with no task document it starts through `refine-task` | 4 |
| 2, 4 | The list, its progress and each settled choice with everything the cycle's writer needs stand in the task document | 1 |
| 5, 9, 10 | Refinement sends a reserved choice to the step; the rule carries boundary examples; every other choice stays in the cycle | 3, 4 |
| 6 | A plan member does the same at its own document; in orchestrated refinement the refiner asks through its conversation file, the project orchestrator dispatches, the table goes in the round package | 4 |
| 7 | No stage of the cycle settles a reserved choice; the attempt is discarded and a blocked draft request names the choice | 2, 3 |
| 8 | After the human closes that draft the document returns to refinement with its accepted answers and rows, and a new cycle starts after acceptance of the whole document | 5 |

Non-goals:

- No change to `project-level/plan_state.py`, `project-level/plan_check.py`,
  `project-level/readiness_check.py` or `installation/install.py`: this change touches none of the
  part map's trust boundaries. The answer of step 4 stands for this design.
- No change to how a run at a definition behaves, to the readiness gate or to an approved
  definition.
- No change to the routes of the guideline skills (WAY-185, WAY-186, WAY-210, WAY-211, WAY-248,
  WAY-249).
- A run at a task does not take the look of `running_product.md` on its own (question 4).
- WAY-219 stays: a missing way to the running product does not by itself stop a cycle.
- The questions on how long logs live, and the observability choice of `loop2`, stay out, as the
  task's *Out of scope* gives.

## Constraints

- The task's answers, *To do* and rows bind. Row 3 names the edits of WAY-121, WAY-122, WAY-123,
  WAY-137, WAY-138 and WAY-135.
- WAY-01: no choice enters the decision log before the change that carries it reaches the main
  branch. WAY-106: a run writes no foundation entry.
- WAY-134: a decision written from a row takes as *Rejected* only the ways not chosen that the
  row's source keeps; those ways stand under the answer of the question the row's *Source* names;
  the human sees candidates in a table and cuts them.
- WAY-138: each risk taken reaches the decision's *Rationale*, marked as a hypothesis, never its
  *Based on*.
- WAY-147: a plan's task enters its cycle under its name, and the cycle names its record by it.
- WAY-153: the plan-state reader changes nothing, and the project orchestrator brings a
  closed-unmerged request or a conflicting trace to the human without correcting the plan on its
  own.
- WAY-154: only a refiner changes a task document's body; in orchestrated refinement the refiner
  starts no child agent.
- WAY-227: the cycle's only ordinary human contact is the request; a decision the foundation
  reserves opens a blocked draft request.
- WAY-256: what only one step or variant needs stands beside the skill; a single instruction stays
  where its pointer would stand. WAY-125: a file beside a method is read when its step comes.
- `.runs/technology/` is outside Git: what must survive stands in the task document.
- A skill's description stays one line that is a safe plain YAML scalar — neither `: ` nor ` #`
  in it (`agent-instructions/skill_entry_points.py`) — and a changed description is followed by
  `python -B agent-instructions/skill_entry_points.py --write`, its output committed.
- `plan_state.py` as it stands (read at base `2dbf1e7`): `task_report` counts as a trace a working
  directory `.runs/task-cycles/<name>` in a worktree git lists, and any commit touching
  `docs/task-cycles/<name>/` in `refs/heads/` or `refs/remotes/`, tied by provenance. A trace on a
  row reading `to refine` is a conflict (`plan_state.py:416-420`); a trace on a row reading
  `ready for cycle` proposes `in cycle` (`:409-410`). The reader's fetch has no prune
  (`:106-107`), so a remote-tracking ref outlives the deletion of its branch on the host.

## Decisions

### 1. The place in the task document

**Settled.** The template gets one new section and three new fields; its existing sections stay.

- **Section *Technology*.** A third-level section of *Description*, right after *Questions to
  settle*, present only once a run of the step has begun at the task; it stays in the document
  after the run ends. It holds, as a list:
  - one item for each run's note, as it was given, with its date;
  - one item per choice, named in the document's language by what the product needs it for, ending
    with one marker in English: `— open`, `— held by: <PREFIX>-<NN>`, `— projected: <question>` for
    a choice a projected decision of the approved definition the task carries settles, the question
    reading as in that decision's heading, or `— settled: <question>`, the question reading as under
    *Questions to settle*;
  - nested items under a choice: the human's preference, the choice it waits for, and, for a choice
    the human opened though a decision holds it, the decision it changes.
- **Three fields under a settled question.** Under *Questions to settle*, a question a run settles
  holds *Answer*, *Not chosen* and *Source* as every question does, and after them, only there:
  - *Based on* — the source of each difference claimed between the options: its address, the place
    in it, the passage word for word and the date read, the form the decisions' template gives;
  - *Lacks* — each lack of the option chosen, as what it means for the product;
  - *Risks taken* — each risk the human took with it, each marked as a hypothesis.
  *Not chosen* holds every option shown and not chosen, the options left out of the comparison with
  their line included, each with its consequences as the table gave them. The template's sentence
  on a canonical answer shared by tasks extends to these three fields.
- **The row is not the step's to write.** The step ends its work at the question and the list. The
  row of *Settlements to record* comes from step 5 of `refine-task`, as every row does: an answer
  under *Questions to settle* is already what `find-foundation-entries` reads for a task, so the
  settled question becomes a candidate, the human cuts it, and its *Source* names the question.
  `find_settlements.md` says that a settled technology question is always shown as a candidate,
  since the cycle otherwise writes no decision of it. An earlier accepted row stays, as that file
  gives for a document refined again.
- **A change of a held decision comes back through refinement unsent.** Question 7 makes the result
  of a run on a choice a decision holds a change of that decision in this document (WAY-30), so three
  sentences each gain one exception, for exactly that decision: `resolve_gaps.md:10-12`, where the
  run is that change's process; `find_settlements.md:21-22`, where the candidate of such a question
  is no conflict and its row names the decision it changes; and `carry_foundation.md:13-15`, where
  *Decisions in play* quotes that decision and the human is not asked again. A collision with any
  other decision or a projected entry goes as those sentences give, and a change of an approved
  definition stays routed to its own process.
- **Resuming.** A run that finds the section reads its notes and list. An item ending `— open` is
  looked for under *Questions to settle* first; where a question written for that choice stands,
  the item ends `— settled: <question>`. Then the list is shown and asked about as `start.md` does
  for a definition, and the step goes on with the open items, their preferences and what they wait
  for. A report under `.runs/technology/` that reads `critique: passed` and names this document at
  its head is reused; any other starts its research again, so a comparison lost with a machine
  costs its research and loses no settled choice. `research.md` gains that head line, which names
  every affected task's document where one run serves several (decision 4).
- **The cycle's writer.** It reads row → the question its *Source* names → *Not chosen* for
  *Rejected*, *Based on* for *Based on*, *Lacks* and *Risks taken* for *Rationale*, each risk as a
  hypothesis. A choice that changes a decision is an edit of that decision in place (WAY-30), the
  document's acceptance being its approval. `elements/decisions/template.md` extends its two rules
  (lines 59–67) to say so; WAY-134's path from row to question is unchanged.
- **Readiness.** An item ending `— open` is a known blocking question (WAY-124): `final_review.md`
  checks that none stands. A run's *Start* sets `Status: refining` (decision 4), and while the human
  owes a choice the document reads `Status: waiting for human`.

**Ways rejected.**

- All of it in one new section, with the row pointing there — simpler to read in one place, but
  against question 1's answer and WAY-134, which keep the ways not chosen under the answer of a
  question; WAY-134 would need an edit no row carries.
- New columns in *Settlements to record* — a table cell takes no line break, the reason WAY-134's
  *Rejected* already gives.
- The tech step writing the row itself, as it writes a projected decision in a definition — no
  second look for the human, but the human would never see that row in the candidate table WAY-134
  describes, and the section reads `TODO` until the candidates are cut.
- The comparison kept as a committed file in the repository — it survives without the document's
  growth, but it writes the choice into the repository before any work is done, and a task document
  often stands outside it.

**Cost if wrong.** The document grows by a screen per choice; the rule of one home per fact holds
because the list only points to the question. If the human strikes a technology row at the cut, the
choice stands in the answer with no row. Rejected rows are not kept, so the return step cannot see
the cut, may still meet the choice as one that binds after the merge (WAY-36), and writes it; the
human then sees it at the merge.

### 2. The blocked draft request with no code

**Settled.**

- **What the branch holds.** The task branch is reset as for a discarded attempt: to its base, or
  to the commit that moved the pin where step 2 moved it. It then holds the pair of step 12: the
  commit that adds the record and the commit that removes it. Nothing is merged from the target
  branch.
- **How the request opens.** The order differs from the other blocked requests in one point: the
  commit that adds the record is pushed first and the draft opens on it, while its changed files
  are the record; the commit that removes the record is then pushed. The request therefore never
  depends on a host accepting a request with no changed files, and it ends as the task says, with
  only the pair. The request's description links the record by the SHA of the commit that adds it.
- **What does not run.** No spec, plan, review, return step or reconciliation runs, and the gate
  does not run: the tree equals the base, whose failing checks step 4 recorded, or the commit that
  moved the pin, whose gate step 2 ran. The request names each as not run. `cycle_stages.py` runs
  before the record is copied.
- **What the request states.** It is marked `blocked` and, beyond what step 13 gives for any
  request (goal, relation, sources, pin, the discarded attempt and the agent's report):
  - under *Questions*, the choice in plain words, by what the product needs it for; where it showed
    (the stage and the item of the task); which limb of the rule takes it; what was searched and
    found not to settle it;
  - the ways the agent saw, marked as not researched and carrying no recommendation, since the
    technology step does that research;
  - *Checks*: the checks failing on the base, and that nothing else ran and why;
  - the time, models and tokens so far, from `stages.md`;
  - *What this request settles*: none;
  - what happens next: the human closes the request, and `refine-task` takes the named choice as
    the note. A remark on this request is no correction and the cycle does not continue on it,
    since question 3 rejected continuing in the same request.
- **After a correction.** Where the agent of a correction returns a reserved choice, only that
  correction's commits go, the request returns to draft marked `blocked`, and it names the choice as
  above; its code stands until the human closes it or changes the remark.
- **What `correction.md` does with such a request.** That file takes any link to a cycle's request
  as its input, so it gains the case. The agent tells the case from a request a remaining finding
  blocked by the record's field *Reserved choice* (decision 3), read from the kept worktree or the
  commit the request links; a request a remaining finding blocked has that field at `none`, or no
  such field where its record is older than this change, and the rule at lines 15-17 stands for it.
  - With no code on the branch, nothing is corrected: the agent dispatches no one, changes nothing,
    and tells the human in its report that the request is to be closed and `refine-task` run with
    the named choice. A remark that picks an option does not settle the choice, since the option
    would stand in a comment and not in the task document.
  - With code on the branch, the blocked state of "After a correction": a changed remark that no
    longer needs the choice is an ordinary correction; a remark that still needs it, or that picks
    an option, is answered as above.

**Ways rejected.**

- The pair first, then the request, as the other blocked requests do — no new order, but it rests
  on the host accepting a request whose net diff is empty. The evidence found is a third-party
  remark only; no host's documentation says so.
- The record left on the branch, no removal — the request shows its record as changed files on
  every host, but it breaks step 12's rule that the target branch never holds a record should the
  request be merged by mistake.
- No request, the stop reported only in the record or the conversation — WAY-227 and the same
  reason WAY-162 rejects it: the request is where the human meets the cycle's work.

**Cost if wrong.** Where a host closes a request whose diff later empties, the human still has the
closed request with its description and link; the only loss is one word of state. A later pushed
removal costs one more push than the other blocked requests.

### 3. The rule in the skills and the status of the return

**Settled.**

- **One home of the rule.** A new file `project-level/technology/reserved_choices.md` holds the
  rule: the test of WAY-121 in one sentence; that the choice is reserved when no decision of the
  foundation, no approved definition the task carries and no accepted answer of the task document
  settles it; the boundary examples; what stays where it is. It says that a human may run the step
  for any choice, and that the rule says only what stops a task on its own.
- **Examples it carries.** Stops: a store of data, an error tracker, a framework the product's code
  is written against, a way of logging in, a place to run. Stays with the task: a small library for
  formatting dates, a test double used only by tests, an override of one dependency. At the
  boundary: a source of icons stays with the task while it adds no fee and one task
  can change it alone, and stops where it adds something to pay for. The tools of the guideline
  skills stay on those skills' routes. A missing way to the running product alone does not stop a
  cycle (WAY-219).
- **The boundary.** A choice is under the rule or it is not; one an agent cannot place is no third
  kind. The boundary rests on the agent's judgment, helped by the examples, as question 2 accepted,
  and a choice judged not under the rule stays in the cycle and enters the questions table (To do
  10).
- **The moment an agent recognises.** Each pointer names the moment by what the agent sees: the work
  needs a language, a framework, a library, a store of data, a way of logging in or a place to run
  that the task, the spec and the foundation do not settle. Then the agent reads the rule. Only then
  does it hold its text, so the methods carry a pointer each and no copy.
- **Where the pointers stand.**
  | File | What changes |
  |---|---|
  | `task-cycle/change/SKILL.md` | section 5 gains the case; section 6 lists the status `reserved`; the report holds the choice, where it shows, the limb of the rule, what was searched and the ways seen, and no code |
  | `task-cycle/plan/SKILL.md` | section 2 gains the case; section 5 lists the status |
  | `task-cycle/spec/design.md` | the sentence at lines 15–16 excepts a reserved choice; the designer returns `reserved` with the same report |
  | `task-cycle/spec/SKILL.md` | section 4 names the status where it says what the designer returns, if the wording needs it |
  | `task-cycle/review/SKILL.md` | section 2 gains the check: a change that takes a reserved choice is a finding, graded Important by the general grade of section 3, a missed requirement, with no citation of WAY-263, which reaches only an entry the change writes or changes |
  | `task-cycle/skill/SKILL.md` | the status list; the two sentences at lines 186–188 and 213–214 except a reserved choice; step 4 judges it beside the open design choice; a paragraph under "Design and execution choice" points to the new file; step 13 points to it |
  | `task-cycle/skill/correction.md` | its recovery sentence names the case, and it gains the case of a request a reserved choice blocked (decision 2) |
  | `task-cycle/record_template.md` | *Discarded attempt* names the reason; a field *Reserved choice* in *Spec and execution route*, reading `none` or the choice |
  | `project-level/task/skill/resolve_gaps.md` | the pointer and its route (decision 4); the exception of decision 1 at lines 10–12; the sentence at lines 17–18 excepts a reserved choice |
  | `project-level/task/skill/find_settlements.md` | the sentence on a settled technology question and the exception of decision 1 |
  | `project-level/task/skill/carry_foundation.md` | the exception of decision 1 |
  | `project-level/task/skill/final_review.md` | the check of decision 1 |
- **The status `reserved`.** A new status under `make-change`, `plan-task` and, for the designer,
  `write-spec`. It is what separates the route from `returned`:

  | | `returned` for an open design choice | `reserved` |
  |---|---|---|
  | Who settles it | a fresh designer, then the orchestrator | the human, in `settle-technology` at the task document |
  | The attempt | discarded with its entries | discarded with its entries, slices already made included |
  | What follows | spec, its review, the route judged again | no spec; the blocked draft request of decision 2; the cycle ends |

  A reserved choice is also an open design choice by the glossary's definition, so the check for a
  reserved choice comes first; that is the exception row 3 gives WAY-135.
- **What the orchestrator does.** A new file `task-cycle/skill/reserved_return.md`, read when it
  applies, as `blocked_finding.md` is:
  1. It checks the report against the rule, because the agent's claim is not evidence. Where a
     source settles the choice, it answers and resumes the agent. Where the rule does not take the
     choice, it goes on by the route that fits, as a choice of how to make the change or an open
     design choice. Otherwise it stops.
  2. The same check runs on every question and every `returned` report, and on the task at step 4,
     before any answer: no answer and no smallest reversible reading settles a reserved choice. A
     choice the orchestrator finds at step 4 has no agent report; the record holds it, and nothing
     is discarded.
  3. It discards the attempt as WAY-135 gives, to the task's base or to the commit that moved the
     pin, and records the discard with the reason.
  4. It takes the steps of decision 2 and ends the cycle with status `blocked`.
- **A finding of a review.** A reviewer's finding of this kind gets its one fix as any other. An
  agent that cannot remove the choice from the change returns `reserved`.

**Ways rejected.**

- `returned` with a field in the report — one status fewer, but the orchestrator's route would
  depend on reading a field, and the planner's `returned` already leads to step 6, while the
  designer has no such status at all.
- `blocked` — it already leads to a blocked draft, but it means a missing fact or permission, keeps
  the committed work, and gives a slice's executor a retry one class higher, all wrong here.
- The rule copied into each method — every copy has to be kept in step, and an agent reads rules
  its work does not need.
- The rule in the decision alone — stage agents read the entries their handoff names, so an agent
  whose handoff does not name it would not meet it.
- A rule that doubt leans to reserved — a doubtful choice would never reach the request with code
  on it, but the rule would say more than row 2, which reserves a choice under the rule and leaves
  every other in the cycle, and it would bind after the merge with no entry behind it (WAY-36).

**Cost if wrong.** A choice stopped wrongly costs one cycle and one refinement; the task's measure
(three agent choices in 25 cycles of `loop2`, none clearly under the rule) suggests this is rare. A
doubtful choice judged not under the rule reaches the human in the request with code on it, the
weak point question 2 accepted. An agent that does not recognise the moment repeats today's
behaviour, and the reviewer's check is the second chance.

### 4. A run at a task beside a run at a definition

**Settled.** One skill, the same name, and one new file holding only what differs.

- **`project-level/technology/SKILL.md`.** Its description says that the step also runs at a task
  document, with a note saying what for, for a choice no definition settles or one the human
  opens, and that it resumes from the document's Technology section. Its title and opening speak of
  technology, not only a project's. It names "the document": the definition, or in a run at a task
  the task document with its note. The sentence on where the step writes names both documents and
  keeps "never into the product's foundation" (WAY-106). Step 0 routes: where a task document is
  named, read `task_run.md` beside this skill first; where a note comes with no task document,
  start `refine-task` with the note as the request, which creates the document and calls this step
  from its step 3, the note passing to the run whatever the rule says of the choice.
- **`project-level/technology/task_run.md`, new.** Read at step 0 of a run at a task; it holds, step
  by step, only what differs:
  - *Start* — in place of `start.md`'s first two bullets: read the task document whole, the
    template's section on *Technology*, the definition template's Technology section for the rules
    of weighing, and "How a skill asks". Foundation reading as in `start.md`. A document in a
    running cycle is left alone (`draft.md`); any other, an accepted one included, is set to
    `Status: refining` before anything else changes, as `draft.md` gives, so that an interrupted run
    never leaves a changed body under `ready for cycle`. A run refinement starts for a reserved
    choice takes that choice as its note; a run with no note and no such choice asks for it once.
    The look of `running_product.md` is not taken.
  - *List* — `list.md` applies, except that the items come from the note and the task, the rule of
    belonging selects nothing for a choice the human names, and a choice a decision of the foundation
    holds opens only on the human's word, in the note or a change to the list: it then stands
    `— open` with the decision it changes nested under it, and an agent never opens one (question
    7). A choice a projected decision of the approved definition the task carries settles stands
    `— projected: <question>`, as `list.md` gives, and no run reopens it, since question 7 speaks of
    a decision of the foundation and To do 6 keeps the definition untouched: a human who wants it
    changed goes the way `resolve_gaps.md:10-12` and WAY-118 give. The status line of a definition
    does not apply.
  - *Settle* — sub-steps 1 to 6 of `settle.md` as they stand, with the document in place of the
    definition. WAY-165 and WAY-166 apply where the note touches the logs, the interface or the
    development data. A choice the human opened is no longer held, so it is tested. A constraint the
    task document states counts as a definition's constraint does.
  - *Write* — in place of sub-step 7: decision 1's question and fields, the item ended `— settled:
    <question>`, the next wave started; no `record-decision`.
  - *Close* — in place of `close.md`: no item ends `— open`; no readiness check; return to the step
    of `refine-task` that called the run, or to step 3 for a run the human started, so that steps 4
    to 6 run on the whole document and the human accepts all of it (To do 8).
  - *Orchestrated* — a refiner leads the run through its conversation: `orchestrated_mode.md` gives
    the routing below.
- **Neutral wording, not a copy.** `research.md`, read by a fresh agent that never sees `task_run.md`,
  and `settle.md` say "the document" where both runs share the sentence, and `research.md` adds the
  report's head line and the note among what the leader gives. `settle.md`'s sub-step 7 gains the
  one-line pointer. `start.md`, `list.md`, `close.md` and `running_product.md` keep their text, each
  still true of a run at a definition; the definition template gains nothing.
- **Refinement.** `resolve_gaps.md` runs `settle-technology` at this document in three cases, the
  rule deciding only the first: the task's outcome needs a choice the rule of `reserved_choices.md`
  takes; the refinement started from a note, carried in the request or given by a closed draft's
  named choice (`draft.md`), whether the choice is under the rule or a decision holds it; or the
  human asks for a run while the task is refined. The document reads `waiting for human` until the
  human settles what the run lists. `find_settlements.md` as in decision 1.
- **Plan members.** `project_plan_task.md` says that the run stands at the member's own document
  and the approved definition stays untouched, so no gate returns; a choice that changes the cut of
  the work returns to the plan as its step 4 gives; a human who wants a projected decision changed
  goes as *List* above gives.
- **Orchestrated refinement.** `orchestrated_mode.md`: the refiner writes the request for a run as a
  *Child-work request* in its conversation turn, and every question the run would address to the
  human goes into the turn; only the refiner writes the document. `conversation_template.md`:
  *Human material* gains a line for the list to confirm and the table of choices. `lead/skill/SKILL.md`
  step 3: the project orchestrator dispatches the research agents, the critiques and the tests the
  refiner requests, and the table goes in the round package, with its choices recorded as human
  answers. The refiner's results stay the five it has: `questions` carries this.
- **One choice in two members of a round.** The request for a run stays a *Child-work request*,
  never a question of the turn: a question would reach `project-level/lead/answering.md`, whose
  agent answers each question from a quotation or prepares it for the human with costs and a
  recommendation, with no research, critique or test of risks, and for a choice the human opened
  would quote the very decision reopened. `answering.md` and `conversation_template.md` gain what
  this needs: a request for a run names the choice and its note; before choosing canonical IDs the
  answering agent, which reads every conversation of the round, also reads these requests, and where
  two members name one choice with the same scope it marks one canonical request and its affected
  tasks, as `conversation_template.md:39-42` and WAY-155 give for a question. It answers no such
  request and prepares no human question for it, since the run does that. The project orchestrator
  then dispatches one run for that canonical request. It stands at the document of the affected task
  with the lowest number; its report's head names every affected task's document, and its list and
  table reach the human once. The refiner of the other member copies the settled question whole,
  with *Answer*, *Not chosen*, *Source* and the three fields of decision 1, into its own document,
  and ends its own item `— settled: <question>`, as the template gives a canonical answer. Each
  member then keeps its own row, and the second cycle ties its row to the entry the first wrote, as
  WAY-134 gives. This paragraph is the orchestrator's settlement of finding 10 of the spec's review,
  left after the one revision (`task-cycle/skill/spec_review.md`).

**Ways rejected.**

- A second skill for tasks — clean to read, but a second copy of the steps, and a run at a task
  is the same step (To do 3).
- The differences written inline in each step file — no new file, but the definition's run reads
  branches it never takes, against WAY-256.
- A blanket "read definition as task document" in `task_run.md`, with no rewording — the smallest
  edit, but `research.md`'s reader never sees that sentence.
- A request for a run written as a question, with `answering.md` told to leave such a question
  unanswered — it reuses the canonical fields as they stand, but it makes a new kind of question the
  agent has to tell apart, and a miss reaches the human as an ordinary question with no research.

**Cost if wrong.** A difference missed in `task_run.md` makes a run at a task apply a definition's
rule, which the human would see in the conversation. The file adds one more place to keep when a
step changes.

### 5. The next cycle of the same task

**Settled.** Nothing in WAY-147, step 5 or step 12 changes.

- **The record's name.** The new cycle uses the same name. The earlier record stands only on the
  branch of the closed request; it never reached the target branch, so `docs/task-cycles/<name>/`
  is free there. A plan member keeps its plan name, and the provenance the reader checks still
  holds, the source document being the same. An independent task's cycle names its record as step 5
  gives; nothing ties it to the earlier name.
- **The branch.** The new cycle creates a new branch from the current target, since step 4 lets
  only a correction reuse one. The earlier branch is never reused; its name binds nothing, so where
  it stands the new branch takes another.
- **The document.** `draft.md` already gives what To do 8 asks: a document not in its cycle, an
  accepted one included, keeps its answers and rows, returns to `refining`, and is `ready for cycle`
  again only on acceptance of the whole changed document. It gains that a task whose blocked request
  the human closed is such a document, and that the named choice is the run's note. The refiner
  keeps the closed request's link under *Context*, so the new record can be reached from the old.
- **The plan row, and who moves it.** The project orchestrator, on the human's word (WAY-153). In
  `lead/skill/SKILL.md` step 1 a closed-unmerged request already goes to the human. A new supported
  transition is added: where the human says that the task returns to refinement, a row reading
  `in cycle`, or still `ready for cycle`, goes to `to refine`, with a change-log line naming the
  request. The document cell stays; `plan_check.py` does not object to a link on `to refine`.
- **The earlier cycle's trace.** Before moving the row, the project orchestrator removes that one
  cycle's trace, on the human's same word and naming what goes, in this order:
  1. its worktree, where it ran in one of its own; where it ran in a checkout that stays, only its
     ignored `.runs/task-cycles/<name>` directory there, the record standing in the commit it adds;
  2. its local branch, by name, which git refuses while a worktree holds it;
  3. its branch on the host, by name, where the human has not deleted it;
  4. the remote-tracking ref of that branch alone, by name, with `git branch -dr`, after step 3,
     since a fetch would otherwise bring it back.
  `git fetch --prune` is not used: it removes every remote-tracking ref whose branch is gone, so it
  would remove the evidence of other tasks' closed-unmerged cycles, a conflict the human never named
  (WAY-153). Only then does the reader see no trace. Left in place, the trace would show as a
  conflict at every session on a `to refine` row, and on a `ready for cycle` row as a false proposal
  that the new cycle has started. Should a removal fail, the reader reports the conflict, the
  existing route to the human.
- **The record after removal.** The commit stays reachable through the closed request, and GitHub's
  documentation gives "You can restore the head branch of a closed pull request."
  (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request,
  read 2026-10-31). The request's description, which decision 2 makes self-standing, is what the
  next refinement needs.
- **A test.** `project-level/test_plan_state.py:297` already pins that a trace on a `to refine` row
  is a conflict. It gains the other half this design rests on: with the branch deleted on the host
  the conflict stays while the remote-tracking ref stands, and with that ref and the local branch
  gone the row reports none. No invariant test changes.
- `project-level/plan/template.md` says, beside the states, that a row goes back only as
  `lead-project` gives.

**Ways rejected.**

- The reader taught to skip a cycle whose record says it returned — the branch and worktree could
  stay and nothing need be deleted, but it changes a trust-boundary file and
  `project-plan-state-evidence`, and it stops bringing a conflicting trace to the human, a change
  to the meaning of WAY-153 beyond what the task carries (WAY-30). This design avoids that.
- A numbered name, `<name>-2` — no collision to reason about, but it breaks WAY-147, and the reader
  looks for `docs/task-cycles/<name>/`, so the task could never read as done.
- The record of a returned cycle under another directory, out of the reader's sight — nothing to
  delete, but the reader would lose the trail to the request, and a second place for records has to
  be kept.
- Reusing the earlier branch — its history survives in one place, but step 4 forbids it, and
  it brings the discarded cycle's commits into the new request.

**Cost if wrong.** The removal relies on the human's word and on a host that keeps a closed
request's commits; where it does not, the earlier record is lost, and the task document and request
description still carry all the next step needs. An independent task leaves its branch to the
human: it harms nothing, since no reader looks for it.

## Foundation entries

New:

| Entry | Kind | From | Meaning |
|---|---|---|---|
| (new) — How does the step that settles technology run outside a project definition? | decision | row 1 | The step also runs at a task document with a note saying what for, starting through `refine-task` where no document exists; it settles what the note and the task name, does not look at the three matters on its own, may open a choice a decision of the foundation holds only on the human's word as a change of that decision, reopens no choice a projected decision of an approved definition settles (To do 6), and writes the choice into that document with its ways not chosen, sources, lacks and risks, for the cycle to write the decision with the code. |
| (new) — Who settles a technology choice that no decision or definition settles? | decision | row 2 | Such a choice under the rule of WAY-121 is reserved to the human: refinement sends it to the step, and a cycle that meets it stops with a report and no code; every other choice stays in the cycle and the guideline skills' tools on their routes; it names what is adopted from lesson m2l4 of 10xDEVS (WAY-100). It derives from WAY-227 and WAY-121. |
| (new) — How does a task leave a cycle that met a reserved choice, and how does it come back? | decision | this spec | The branch holds only the record's pair, the blocked draft states the named choice and that nothing ran beyond it; the human closes it; the next cycle keeps the name on a new branch; the project orchestrator, on the human's word, removes that one cycle's trace by name and moves the row back. It derives from WAY-227, WAY-147, WAY-153. |
| reserved choice | glossary term | this spec | A technology choice the rule of the second new decision keeps for the human; unlike the other decisions WAY-227 reserves, a cycle ends on it, and unlike any other open design choice, no spec is written. |

Changed, each in place:

| Entry | Kind | From | Change in meaning |
|---|---|---|---|
| WAY-121 | decision | row 3 | The choice a definition missed, or that no definition holds, is settled through the run at a task; its rule of belonging and its order before the gate stay. |
| WAY-122 | decision | row 3 | The research goes against the definition or, at a task, against its document and note; a constraint can be the task's. |
| WAY-123 | decision | row 3 | Holds for the step wherever it runs. |
| WAY-137 | decision | row 3 | Holds for the step wherever it runs. |
| WAY-138 | decision | row 3 | Holds wherever the step runs, a constraint of the task included; risks reach the decision through the task document; a choice the human opened is held by no decision and is tested. |
| WAY-135 | decision | row 3 | For a reserved choice the report without code is the same, but no spec follows and the cycle stops. |

Searched and left unchanged: WAY-106 (the task document already takes what refinement settles under
WAY-134, and the run writes no entry); WAY-124 (an open item is a known blocking question); WAY-134
(the path from row to question stands); WAY-147; WAY-153; WAY-165 and WAY-166 (general already);
WAY-172 and WAY-242 (their blocked draft proposes a decision on the branch, in another area);
WAY-219; WAY-227 (the second new decision is the reservation it speaks of); WAY-263 (it reaches only
an entry a change writes or changes, and the reviewer's check uses the general grade); the invariants
`project-technology-record`, `project-plan-state-evidence`, `project-plan-form`; the part map
(`project-level/**` and `task-cycle/**` cover the new files, and `task-cycle` may depend on
`project-level`). `elements/decisions/template.md` changes as a template, not an entry. The search of
the whole foundation is the writer's, as WAY-33 gives, once the entries are settled.

## Left to the maker

- The wording of every text, the description of `settle-technology` included, within the constraint
  on its form.
- The foundation step's wording of each entry, its *Scope*, its number and, for the entries this
  spec names, its *Rejected* from the ways above.
- Whether `task-cycle/spec/SKILL.md` needs its own sentence or `design.md` carries the status alone.
- The exact place of each pointer inside the sections named, and where in the record template the
  new field stands.
- Whether one author can hold this change or it needs a plan: the orchestrator's judgment after the
  spec's review.
