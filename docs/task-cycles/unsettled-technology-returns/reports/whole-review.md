FAIL e21d2868feeb132a4af71d108628bf52a97acd25

# Review of the whole change — `2dbf1e7..e21d286`

Three blocking findings, all Important, each a small text fix. Task, spec and plan coverage holds
apart from them. No slice had a review of its own, so every slice is judged here.

## Limit of this review, stated first

The method asks for every decision whose *Scope* names a touched part, each read whole: about 120
entries by a rough line count of `project-level` and `task-cycle` *Scope* lines. I did not read them
all. I read 18 whole, the changed and new ones in the diff, and the rest only by targeted search
(see **Reaches**). A collision with an entry I did not read could stand unseen. The foundation
agent's report claims a search of the whole foundation; I repeated part of it, not all.

## Findings

### Important

#### 1. A second run's note is lost at a document that already has a section *Technology*

- **Place:** `project-level/technology/task_run.md:24-34`, and *Close* at `:79-87`.
- **Comes from:** slice 1, `6fb58f6`. The spec's decision 1, "Resuming", is silent on it too, and
  silence is not permission.
- **Requirement:** To do 8 and To do 1. The template and spec keep "one item for each run's note",
  so several runs at one document are designed for.
- **What is wrong:** *List* is entered in two cases only: the document has no section, or the human
  adds or changes an item when shown the list. A run given a new note at a document whose section
  already holds a list is told neither to write the note nor to list its choice. Where every item
  is settled, `:34` sends it straight to *Close*.
- **Example, followed literally:**
  1. A task's refinement settles "where accounts are kept", so its section reads `— settled: ...`.
  2. The cycle meets an error tracker, stops and opens a blocked draft. The human closes it.
  3. `draft.md:15-18` makes the named choice the note, and `resolve_gaps.md:29-30` runs the step.
  4. `task_run.md` shows the list, finds no open item and goes to *Close*: no item is open, return
     to step 3.
  5. `final_review.md` finds no `— open`, so the document can be accepted with the choice that
     stopped the cycle still unsettled and its note unwritten. The next cycle stops on it again.
- **Why it matters:** this is the return path the task exists to build. It works only if the human
  happens to add the item when shown the list, and the list does not show the note. An open item
  has the same gap in a milder form: the note's choice is not added beside it.
- **Evidence:** hand trace above through `task_run.md`, `draft.md:15-18`, `resolve_gaps.md:23-31`,
  `final_review.md:7-8`. Slice 1's own trace looked for definition-only instructions, so it could
  not catch this.
- **Fix:** in *Start*, before the bullets on a list: a run given a note the section does not yet
  hold writes the note and follows *List* for it, and only then the rest applies.

#### 2. The stage agent that most often meets the choice reads the rule only once it has already decided to stop

- **Place:** `task-cycle/change/SKILL.md:102-116`.
- **Comes from:** slice 4, `dc13d6a`.
- **Requirement:** To do 7, "no stage settles it", and the spec's decision 3, "The moment an agent
  recognises": each pointer names the moment by what the agent sees, the work needing a language, a
  framework, and so on.
- **What is wrong:** the pointer opens "Before you return `returned`, check the first case". An
  executor that takes a new library, store or framework for "a choice of how to make what they
  settle", which `:104-105` calls its own to make, is not about to return `returned`, so it does
  not reach the pointer and never reads `reserved_choices.md`. That misjudgment is the very thing
  the rule exists to catch: today's silent choice in the code. The other two pointers are not gated:
  `task-cycle/plan/SKILL.md:63` and `task-cycle/spec/design.md:18` both open "Where the change/design
  needs". The agent that writes the code is the one left with the weaker form.
- **Also:** a fix's agent reaches the same gate. The spec gives "an agent that cannot remove the
  choice from the change returns `reserved`", but that sentence stands only in
  `task-cycle/skill/reserved_return.md:26-27`, which the fix's agent does not read, and `fix.md` does
  not carry it.
- **Why it matters:** the reviewer stays a second chance, but by then the code stands on the choice,
  the situation the task names. The spec accepts that an agent may miss the moment; it does not
  accept a pointer that fires only after the agent has seen it.
- **Evidence:** reading of the three pointers side by side. Slice 4's own-work check named "no
  method copies the rule", not recognition, so a grep for the path passed it.
- **Fix:** open that paragraph as the other two do, "Where the work needs a language, ...", standing
  on its own before the two cases.

#### 3. WAY-267 says more than the files do, in two clauses

- **Place:** `foundations/decisions.md:7706-7713`, and *Verification* at `:7729-7731`.
- **Comes from:** the plan's *Foundation entries*, `443442f`. The spec's table of entries has the
  same short wording as the first clause; its decision 5 has the qualification.
- **Graded by:** WAY-263: a change's files that fail to do what its entry requires, or a restatement
  more broadly or without a qualification, is Important.
- **What is wrong:**
  - "under the same name" binds every task. Spec decision 5 gives the name only to a plan member:
    "An independent task's cycle names its record as step 5 gives; nothing ties it to the earlier
    name", and step 5 (`task-cycle/skill/SKILL.md:121-122`) is unchanged. WAY-267's own *Rationale*
    argues from a plan's task alone. Its *Verification* lists a numbered name as a breach with no
    such limit, so an independent task's new cycle breaches the entry by following step 5.
  - "says that nothing else ran and why" is false of a stop after a reviewed spec or a slice. The
    file gives "each of the stages above that did not run" (`reserved_return.md:73-74`), and slice 5
    says so in its choice 2 and its searches. The *Verification* list has the same fixed form.
  - Lesser, same sentence: "holding only the commit that adds its record and the commit that removes
    it" omits the commit that moved the pin, which `reserved_return.md:34` keeps. *Verification*
    states it, so this alone would not block.
- **Fix:** "under the same name" limited to a task of a project plan; "says what did not run and
  why"; *Verification* to match. No change to any file but the entry.

### Minor

1. **WAY-160 has no written exception for the draft with no gate run.** `reserved_return.md:45-47`,
   WAY-267 *Rationale*. WAY-160 binds "the tree that goes into the request". The reading that it does
   not reach this draft is sound: the tree equals the base, whose checks step 4 ran, and the request
   names the gate as not run. WAY-163 binds only a request a blocking finding blocks. But WAY-25 keeps
   a collision from being settled by the agent that meets it, so this reading has to be named to the
   human in the request, as the foundation agent asks.
2. **`narrows WAY-114` is a precedence neither the task nor the spec names.** `decisions.md:7657-7658`.
   Its form follows WAY-25 and WAY-123, and row 2 carries its substance. WAY-25 has a human record a
   precedence, so name it in the request. WAY-30 and WAY-155 give the same pattern.
3. **The research agent does not get the sentences of a decision the human opened.**
   `project-level/technology/settle.md:14`, `research.md:11-13`, as slice 1 raised. It gets only the
   number under `Changes:`, so a comparison can miss what the reopened decision was protecting. One
   clause in `task_run.md` *Settle* closes it.
4. **The canonical request has no field, no ID and no stated order.** `project-level/lead/skill/SKILL.md:113-118`
   stands in sub-step 1 though the mark comes from sub-step 2; `answering.md:44-45` asks for "request
   IDs" that `conversation_template.md:103-105` does not give; `answering.md:11-12` limits edits to
   answers under question IDs; a lone request is never marked canonical. Not blocking: the routing of
   `questions` sends the answerer first (`conversation_template.md:127`), and an agent can name an ID.
   Left as it is, two runs for one choice stay possible, which WAY-155 forbids in spirit.
5. **Nobody is named to correct a report in an orchestrated run.** `settle.md:23-24,39` has the leader
   correct the comparison, end it `critique: passed` and write the risks into it, while
   `orchestrated_mode.md:34` limits the refiner, who leads the run, to its document and its turn.
6. **"Immediately after" stands unqualified** in `task-cycle/record_template.md:89-91` and step 12,
   while the request opens between the two commits. `reserved_return.md:49-51` states the departure,
   so no agent is misled that follows that file.
7. **Authors' reports fall short of their method.** Slices 2, 3, 4 and 6 name their commit as "see
   `git log -1`", not by SHA, and slices 3 and 4 give no per-file line counts. The own-work checks of
   slices 2, 3 and 4 are greps and rereads that could not catch an unmet requirement (WAY-164), which
   is how finding 2 passed.
8. **Unwrapped lines:** `project-level/lead/answering.md:48`, `project-level/technology/research.md:15`,
   `task-cycle/review/SKILL.md:70`. No check binds the width.

## Declined to judge

- A human's run at an accepted plan member leaves its row `ready for cycle` while the document reads
  `refining`, with no supported move: `draft.md` had this before the change, and the task does not
  name it.
- An agent that takes a reserved choice and reports `done`: the spec accepts it, with the reviewer as
  second chance. Finding 2 concerns only the pointer's form.
- The human striking a technology row at the cut: the spec's decision 1 accepts this cost.
- An independent task's earlier branch and worktree left in place: the spec's decision 5 accepts this.

## Coverage

| Requirement | Result |
|---|---|
| To do 1 | met, except a second run's note (finding 1) |
| To do 2 | met: `task_run.md`, `task/template.md` |
| To do 3 | met: `task_run.md` *List*, *Settle* |
| To do 4 | met: template fields, `elements/decisions/template.md` |
| To do 5 | met: `resolve_gaps.md`, `final_review.md` |
| To do 6 | met; canonical mechanics thin (Minor 4, 5) |
| To do 7 | met, except the pointer in `make-change` (finding 2) |
| To do 8 | met for a document with no section; not with one (finding 1) |
| To do 9 | met: `reserved_choices.md` table |
| To do 10 | met: `reserved_choices.md`, `resolve_gaps.md` |
| Questions 1-7 | answers carried; ways not chosen counted: WAY-265 holds 4, WAY-266 holds 5, as the task's |
| Row 1 | WAY-265; "any choice" narrowed for projected decisions, as spec and To do 6 give |
| Row 2 | WAY-266; lesson m2l4 named in its *Rationale* (WAY-100) |
| Row 3 | WAY-121, 122, 123, 137, 138, 135 all changed |
| Questions carried | both answered: `reserved_return.md`, lead-project step 1, WAY-267 (finding 3) |

Source fidelity: nothing invented against the task found. The GitHub passage in WAY-267 *Based on*
reads as quoted, under the heading given.

Slices judged: foundation entries, finding 3. Slice 1, finding 1. Slice 2, no blocking finding.
Slice 3, Minor 4, 5. Slice 4, finding 2. Slice 5, no blocking finding; its own-work check was the
strongest of the set. Slice 6, no blocking finding; its test is real.

Section 2 checks: the change settles no reserved choice, being text and one test. Trust boundary: no
file the part map names changes (`plan_state.py`, `plan_check.py`, `readiness_check.py`,
`check_instructions.py`, `install.py`). The cycle holds no operation that cannot be undone; the
removal of a host branch is an instruction to a later session on the human's word, and GitHub keeps
the head branch restorable. No invariant test changes: `test_plan_state_invariant.py` is untouched,
and the new test stands in `test_plan_state.py`.

## Checks

| Check | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `e21d286`, the head given |
| `python -B -m unittest discover -s project-level -p "test_plan_state.py"` | 0 | 37 tests OK |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current |
| `python -B instruction-files/check_instructions.py . --file <f>` for `task_run.md`, `reserved_choices.md`, `reserved_return.md` | 0 each | 0 errors, 1 warn each; I did not read the warn line, which the slices' reports name as `AGENTS.md:21` |
| new test on a whole-tree scratch copy, unmutated (control) | 0 | passes |
| same, `plan_state.py:116` reading `refs/heads/` alone | 1 | fails at the first read: reports no conflict |
| same, `--prune` added to the reader's fetch | 1 | fails: the row reports no trace, so the test catches a reader that forgets early |
| `rg -U "smallest\s+reversible"` over `foundations`, `task-cycle`, `project-level`, `elements` | 0 | every line excepts a reserved choice or says none settles one |
| `git diff --stat 2dbf1e7..e21d286` on the trust-boundary files and the invariant test | 0 | empty |
| manual: fetched the GitHub page | not applicable | heading and first sentence as WAY-267 quotes them |

Void runs: three earlier mutation runs on a copy of `project-level/` alone failed in the control too,
since that copy lacks the rest of the tree. They show nothing and are not counted.

Not run: the gate, which is the orchestrator's. `task-cycle` and `agent-instructions` tests: taken
from the slices' reports. No agent was run on the instruction texts, so findings 1 and 2 and every
"met" above rest on reading and hand trace, not on observed agent behaviour.

## Reaches beyond the dispatch

- `foundations/decisions.md`, whole: WAY-25, 30, 100, 114, 134, 136, 140, 142, 147, 153, 154, 155,
  160, 162, 163, 164, 227, 229, selected as the entries the change most bears on. WAY-121, 122, 123,
  135, 137, 138 in the diff with its context; WAY-265, 266, 267 whole in the diff.
- `foundations/invariants.md`: `project-technology-record`, `project-plan-form`,
  `project-plan-state-evidence`, `skill-rule-source`, `return-step-record`.
- `foundations/part_map.md:86-90` only, for the trust boundaries. `foundations/glossary.md`: *reserved
  choice*, *open design choice*.
- `elements/decisions/template.md:1-75`, `elements/common/way_of_working.md` "Reading the foundation",
  `elements/common/skill/SKILL.md:60-85`, for how a settled question reaches a row.
- Files beside the change: `task-cycle/skill/foundation_step.md`, `blocked_finding.md`,
  `spec_review.md`, `plan_member.md`, `task-cycle/change/fix.md`, `task-cycle/spec/review.md`,
  `project-level/plan_state.py:100-124,376-392,410-425`.
- The session's global rules on code review, scripts and search, as the user's instructions ask.
  The handoff's report path and form replace the scratchpad and form that playbook gives.
- The GitHub page WAY-267 quotes, to check the passage.

## Searches not found or unclear

- Whether WAY-160 reaches a request with no code: unclear, read as not reaching it (Minor 1).
- No place found that tells a fix's agent to return `reserved`, other than through section 5's gate
  (finding 2).
- No instruction found for a run given a new note at a document with a list (finding 1).
- Where a canonical request's mark and ID stand: not found (Minor 4).
- Who corrects a technology report in an orchestrated run: not found (Minor 5).
- Whether "a choice of how to make what they settle" takes in a new library in the agent's reading is
  a judgment about agents, unverified: no agent was run.
