FAIL

# Review of the spec — unsettled-technology-returns

Spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`, against the frozen `task.md`, at
`2dbf1e7` on `task/unsettled-technology-returns`. Paths below are relative to the worktree. Nine
findings, the most consequential first. Each names the kind `task-cycle/spec/review.md` gives it.

## Findings

### 1. A run the human starts for a choice outside the rule has no way in

Kind: a requirement of the task the spec changes.

- `spec.md:283-286` routes a note with no task document to `refine-task`, "which creates the
  document and calls this step from its step 3". The only text that makes step 3 call it is the
  pointer of `spec.md:315-317`: "where the task's outcome needs such a choice and the rule of
  `reserved_choices.md` takes it, run `settle-technology` at this document". The table at
  `spec.md:226` adds nothing to it.
- The rule takes a choice only where no decision settles it (`spec.md:197-199`) and where it passes
  the test of WAY-121. So the pointer never fires for a choice a decision holds, or for a choice one
  task can make alone.
- The task requires both. To do 1 and question 4: the human can run the step for any choice, "człowiek
  może uruchomić krok dla każdego wyboru". Question 7: the note opens a choice a decision holds. The
  case the task names first, where the logs of `loop2` go, is the second of these.
- Built as written, that note starts `refine-task`, the document is created, step 3 finds that the
  rule does not take the choice, and the step never runs. The refiner either drops the note or
  invents a route.

What the builder has to know: the pointer must fire on the rule **or** on a note the refinement
started from (the run's note carried in the request, or `draft.md`'s named choice), and the spec has
to say so.

### 2. A held choice settled in a run meets three sentences that send it away

Kind: a contradiction with the task, and a place where the builder has to guess.

Question 7 and row 1 say that the result of a run on a held choice is, in the task document, a
change of that decision (WAY-30). `spec.md:117` agrees. On the way back through `refine-task`, three
sentences the spec leaves as they stand say otherwise:

- `project-level/task/skill/resolve_gaps.md:10-12`: "If the answer changes the approved project
  definition or a current foundation decision, route that change to its own process; do not silently
  settle it inside the task."
- `project-level/task/skill/find_settlements.md:21-22`: "A candidate that collides with a current
  decision or a projected entry goes back to step 4 as a conflict".
- `project-level/task/skill/carry_foundation.md:13-15`: step 4 then asks the human "whether to change
  the task or reopen the upstream settlement".

Decision 1 changes `find_settlements.md` only so that a settled technology question is always shown.
Nothing says that a choice the human opened is the exception to these sentences. A wrong guess either
moves an accepted change out of the document, against question 7, or asks the human again what the
table just settled, which WAY-30 excludes ("the agent writing the entry asks only about a meaning
beyond what the approved plan or task document carries"). The answer changes `resolve_gaps.md` and
`find_settlements.md`, or `carry_foundation.md`.

### 3. "A remark on this request is no correction" has no home in the file that decides it

Kind: a place where the builder has to guess; a wrong guess restores a way the task rejected.

`spec.md:170-172` has the blocked request say that a remark is no correction and the cycle does not
continue on it, since question 3 rejected continuing in the same request. That is text of the request
for the human. The agent that receives such a link follows `task-cycle/skill/correction.md`, whose
first lines take any link to the cycle's request as input and whose lines 15-17 hold a rule for a
blocked request: "the human's decision is the input". `spec.md:224` changes only the recovery
sentence. So a human who answers on the draft, or pastes its link into a session, sends an agent to
work on a branch with no code and in the same request: the *Not chosen* of question 3.

What the builder has to know: `correction.md` needs the case, what the agent does instead, and how
it tells this request apart from one a remaining finding blocked, whose decision is an input.

### 4. `git fetch --prune` breaks what the same decision requires

Kind: a contradiction within the spec, left to the maker.

`spec.md:438-439` leaves the command that removes the remote-tracking ref to the maker, "`git fetch
--prune` or `git branch -dr`". `spec.md:364-366` says the project orchestrator acts "on the human's
same word, naming what goes", for that one cycle's trace. `--prune` removes every remote-tracking ref
whose branch is gone from the host. `spec.md:75-76` records that the reader's fetch has no prune, so
those refs are what keeps another task's closed-unmerged trace visible as a conflict. One prune
would remove that evidence for tasks the human never named, which WAY-153 lists as a violation
("silently normalizes a conflicting trace"). Only the named deletion fits, so this is no choice for
the maker. The spec should fix it, with the order: the host's branch first, since the next fetch
otherwise brings the ref back.

### 5. "Important by WAY-263" does not hold

Kind: a contradiction with the foundation.

`spec.md:222` has `task-cycle/review/SKILL.md` grade a change that takes a reserved choice "Important
by WAY-263". WAY-263 covers a departure "from a foundation entry it writes or changes"
(`foundations/decisions.md:7493-7496`, restated at `task-cycle/review/SKILL.md:96-99`). A later task
that picks a store of data writes and changes neither of the new decisions, so WAY-263 does not reach
it. WAY-263 is not in the spec's table of changed entries. Built as written, a skill states WAY-263
more broadly than the entry does, and that sentence falls to the review of this very change. The grade
matters: `spec.md:271-272` names this check as the second chance, and a Minor finding does not block.

What the builder has to know: either the finding is Important by the general grade of section 3, a
missed requirement, or WAY-263 changes and joins the table with a row or a question that carries it.

### 6. The rule on doubt is broader than the entry that is to carry it

Kind: a contradiction within the spec.

`spec.md:208-210` treats a choice an agent cannot place, after the test and the examples, as
reserved. The meaning of the second new decision at `spec.md:406` says that a choice under the rule
is reserved and "every other choice stays in the cycle", as row 2 and To do 10 do. A doubtful choice
is, by the spec's own wording, not shown to be under the rule. So `reserved_choices.md` would say
more than the entry written with it, the case WAY-263 grades Important in the review of this change,
and the rule would bind after the merge with no entry behind it (WAY-36).

The direction of doubt is a settlement of this spec and row 2 does not carry it. The meaning at
`spec.md:406` has to carry it, or the rule has to go. Should it stay, the meaning has to say that it
is an addition to row 2, since WAY-134 lets the cycle write a row only with its own meaning.

### 7. A run the human starts at an accepted document leaves `Status: ready for cycle`

Kind: a place where the builder has to guess.

`spec.md:283-284` lets a run start where a task document is named, without `refine-task`. The return
to `refining` stands only in `draft.md:11-15`, which that route does not pass, and the *Start* of
`task_run.md` at `spec.md:289-293` does not set it. `spec.md:121-122` says that the document "keeps"
`waiting for human` while the human owes a choice, which assumes a status already moved. Until *Close*
returns to step 3, the body changes and the list may hold `— open` under `ready for cycle`, and step 1
of `implement-task` asks for nothing but that status (`task-cycle/skill/SKILL.md:27`). After an
interrupted run a cycle can take a document the human has not accepted, against WAY-124 and To do 8.

What the builder has to know: the *Start* of a run at a document not in its cycle sets `refining`, as
`draft.md` gives.

### 8. The list has no marker for a choice a projected decision settles

Kind: a place where the builder has to guess.

`spec.md:88-90` closes the list on three markers: `— open`, `— held by: <PREFIX>-<NN>` and
`— settled: <question>`. For a plan member or a source-only task, the choice may stand in a projected
decision of the approved definition the task carries, and `spec.md:197-199` counts that as settling
it. It has no number, so it cannot be `held by`, and it was not settled by the run. `list.md:18-22`
has the marker `projected` for this, tied to "this definition", and `spec.md:294-298` neither takes it
over nor excludes it. Marked `— open`, the run researches and tests what the human approved at the
gate, and its result would change the definition, which To do 6 keeps untouched and
`resolve_gaps.md:10-12` routes elsewhere. The spec also does not say what happens where the human
opens such a choice: question 7 speaks of a decision of the foundation, and a changed projected entry
means the gate again (WAY-118).

### 9. The same choice in two members of one round has no form

Kind: a place where the builder has to guess.

`spec.md:112-114` keys a report on `.runs/technology/<choice>.md` and reuses it only where its head
names "this document". In an orchestrated round refiners run side by side, and two members can name
the same choice. The second run then overwrites the first report or starts its research again, and
the choice reaches the human twice, which WAY-155 lists as a violation ("two tasks ask the human the
same choice separately"). `project-level/lead/conversation_template.md:39-42` has a canonical question
for a duplicate choice, but `spec.md:321-327` does not tie a run to it.

What the builder has to know: which document the run stands at, how its report names the affected
tasks, and how the fields of decision 1 reach the other document.

## Reaches beyond the handoff

- `foundations/decisions.md`, WAY-263: `spec.md:222` cites it. Finding 5.
- `foundations/decisions.md`, WAY-160, WAY-140, WAY-139 (read beside WAY-138): whether a request with
  no gate, and the removal of a branch on the host, collide with them. Neither does.
- `foundations/glossary.md:97-99`, *open design choice*: `spec.md:237` rests on its definition.
- `foundations/part_map.md`, the parts `project-level` and `task-cycle`: to check `spec.md:426-428`.
- `elements/decisions/template.md:40-84`: `spec.md:118-119` names lines 59-67.
- `elements/common/skill/SKILL.md:72-103`: what a task's candidates are read from (`spec.md:102-104`).
- `project-level/plan_check.py`: `spec.md:363` on a link in a `to refine` row.
- `project-level/test_plan_state.py:270-329`: `spec.md:373`.
- `product-guidelines/reading.md:85-99`: a second account of an open design choice.
- `agent-instructions/skill_entry_points.py:118-120`: the constraint at `spec.md:68-70`.
- `installation/README.md:57`: whether a description of the step stands there. It lists the skill by
  name only.

## Checks

Read-only review. `git rev-parse` gave `2dbf1e7` on `task/unsettled-technology-returns`, and `git
status --short` printed nothing. No test ran. The behaviour of `plan_state.py` that `spec.md:373-376`
claims was followed in the code, not run.

## Searches not found or unclear

- Not checked: the GitHub sentence at `spec.md:371` carries no address, and the claim at `spec.md:180`
  that no host's documentation says a request with no net diff is accepted. The review reached no host
  documentation.
- Unclear: `spec.md:139-141` says that the return step writes a choice whose row the human struck,
  while `spec.md:105-106` says that the cycle otherwise writes no decision of it. It stands under
  *Cost if wrong* and sets no behaviour, so it is no finding, but `task-cycle/skill/return_step.md:12-13`
  would have that step write what the human cut.
- Unclear: `spec.md:365` speaks of "that cycle's worktree". Where a cycle ran in the product's main
  checkout, which step 4 of `implement-task` allows, `.runs/task-cycles/<name>` stays and the reader
  still counts it as a working cycle. The spec does not say what removes it.
- Not found: `foundations/invariants.md` holds no `### ` heading for the four invariants the handoff
  names; they stand under `## `, and were read there.
