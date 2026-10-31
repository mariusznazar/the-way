FAIL

# Review of the spec — logs-life-and-failure-notice

Spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`
Task: `.runs/task-cycles/logs-life-and-failure-notice/task.md`
Base read: worktree at `5d66387`, clean.

Three findings. The main choice of D1 and the place of the look in D2 hold; each finding asks for a
narrow change to the spec, none reopens a decision of it.

## Findings

### 1. D6 step 2 changes To do 4 and row 4 without saying so, and contradicts the spec's own entry for WAY-139

Kind: a requirement of the task changed; a contradiction of the spec with itself.

- To do 4 and row 4 have one rule, with no exception: where the task deploys the product or changes
  how or where it runs and the skill does not say the item, refinement asks the human whether to run
  the step with a note, and the skill gets the answer. Row 4's last column names what this settles:
  "czy dopisać brakujący punkt skilla samemu, bez wyboru człowieka".
- D6 step 2 adds a second way: where a decision of the foundation or an approved definition answers
  the item, "quote it, ask nothing, and the *To do* gains the item that writes it into the skill". The
  agent then fills the skill's item in with no question to the human.
- D6's closing lists "Two readings picked". This one is not among them, so the spec presents a third
  reading as settled mechanics. The handoff makes a change to a To do or a row a finding.
- *Foundation entries*, WAY-139, says the check "asks the human about them instead of filling them
  in", with no exception. A builder working from that sentence writes a WAY-139 that
  `project-level/task/skill/resolve_gaps.md` then contradicts in the same change; a builder working
  from D6 writes one that does not say what its check does.

The way may well be right. `resolve_gaps.md:6-8` already tells refinement to quote an answer the
foundation holds rather than ask, and running the step on a matter a decision answers would open that
decision for nothing. But it is a decision over a settled answer, and it has to be taken as one. The
orchestrator rules which holds:

- keep step 2: name it as a third reading with its reason, and carry the exception into the meaning
  of WAY-139, so the entry, row 4 and D6 say one thing;
- or drop step 2: the question is asked in that case too, and the spec says what a yes then does to
  the decision that already answers the item.

### 2. D2's condition for step 1 is narrower than D4's criterion, in the case that matters most

Kind: a contradiction of the spec with itself; the builder has to guess.

- D4: where the place to run stands `— open` and the definition does not keep the product on the
  machine it is made on, "the criterion counts as met". Silence about where the product runs is a yes.
- D2, `SKILL.md` step 1: read `failure_notice.md` "where the project runs the product outside the
  machine on which it is made". That is the plain criterion without the case above, and silence reads
  as a no. The `list.md` bullet in D2 gives no condition of its own, so the builder will take this one.
- `failure_notice.md` is the file that holds the rule "counts as met" (D2, "It says: the criterion of
  D4"). An agent writing a new list for a first project, the place to run not yet chosen, tests the
  narrow condition, does not read the file and never meets the wider rule. That first project is the
  case To do 3 exists for. A list that is resumed is safe, since step 0 reads the file unconditionally.
- Ordering makes this worse: in `list.md` the look stands before the bullet that gives each item its
  marker, so at that moment no item of the place to run "holds `— open`" yet. D4's wording cannot be
  applied at that point as it reads.

What would settle it: the spec states one condition for `SKILL.md` step 1 and the `list.md` bullet
that is true for a definition silent on where the product runs, for example "unless the definition
keeps the product on that machine", or has step 1 read the file wherever `list.md` is read, and it
words D4's case against what the definition says rather than against the marker.

Why the answer changes the build: with the narrow reading, a project that has not chosen where to run
gets no item. Its failure question then waits for the check of D6, and D6 reaches only a task that
deploys the product, which is the "wrong no" D4 prices as avoidable.

### 3. The rewrite that D1 relies on has no place in the files, and the Files table rules out the place it would go

Kind: the builder has to guess; a wrong guess matters.

- D1's table: for a logs item `— projected: Q` with Q silent, "settling it rewrites that projected
  decision in projected mode". For `— held by: X`, the decision "changes only through a projected
  edit".
- *Files*: `settle.md` — "sub-step 1 only". Sub-step 7 is where a choice is handed to `record-decision`
  (`project-level/technology/settle.md:61-70`), and it stays as it is: it hands the choice with its
  consequences and options, and nothing says which entry the result replaces.
- `record-decision` does not find that entry alone in the case of a projected decision.
  `elements/decisions/skill/decide_entry.md:9` searches the log, and `elements/common/projected_mode.md`
  step 2 limits the search to the element's own file. A projected `(new)` entry stands in the
  definition, not in the log, so nothing finds it. Step 4.3 writes the entry under a heading, and no
  file says to replace one.
- For held X the search of the log usually finds the question, but that rests on the agent recognising
  it. The run at a task has this rule written (`project-level/technology/task_run.md:72-74`, "A choice
  the human opened says in its *Answer* which decision it changes"); the run at a definition, which
  D1 sends down the same road, has none.

Why the answer changes the build: the wrong guess leaves two projected entries on one question, the
silent one still standing. The readiness check passes it, since `readiness_check.py:231` keeps
questions as a set. The spec's own reason for rejecting "leave the items alone" then comes true: "a
silent projected decision enters the foundation already failing the next project's look".

What would settle it: the spec says where the rule stands, and the Files row changes to match. The
natural place is `settle.md` sub-step 7: a nested entry goes to `record-decision` as the entry the
result rewrites, a projected one replaced under its heading and a decision of the foundation projected
as its change, `#### <PREFIX>-<NN> — <question>`. A rule placed in `running_product.md` would do if the
spec says so.

## Reaches beyond the dispatch

- `elements/decisions/template.md`: to check the spec's claims on the form of an entry, on stages in a
  binding sentence, on `narrows` and on *Rejected*. The claims hold.
- `foundations/decisions.md`, whole entries WAY-05, WAY-07, WAY-19, WAY-25, WAY-118 and WAY-134 (the
  last read up to its *Origin* field): the spec cites each.
- `elements/decisions/skill/SKILL.md`, `decide_entry.md`, `projected.md` and
  `elements/common/projected_mode.md`: what a hand-over in projected mode does with an entry that
  stands. Finding 3.
- `project-level/readiness_check.py`, lines 1-300: the spec's claim that nested items pass the check.
  The claim holds (`items()`, lines 192-209).
- `project-level/test_readiness_check.py`, lines 98-125, and a search of the tests for
  `project-level/technology` and the template: the claim that no test pins the step's text. It holds;
  the tests read only the form blocks of the template, which the spec does not touch.
- `project-level/task/template.md` (*Questions to settle*, *Technology*),
  `project-level/task/skill/orchestrated_mode.md`, `project_plan_task.md`, `carry_foundation.md` and
  `project-level/skill/SKILL.md` (steps 0 and 7): whether D6 and D1 need a change in files the spec
  leaves out. They do not: the rule on questions in `orchestrated_mode.md` covers D6's question, and
  a yes is a run the human asked for.
- `agent-instructions/README.md`: as `AGENTS.md` requires for work on the-way.
- A search of the tracked files for `logs`, `rollback` and the phrases of the logs question: whether
  another text restates what the spec changes. Only the files of its table do.

## Searches not found or unclear

- D8's phrase on the boundary: searched in Polish and English, "bez dotykania", "without touching",
  "application code" and neighbours, over the repository. Not found, which agrees with D8.
- The whole foundation search of WAY-33 was not made here: the spec leaves it to the maker, and only
  the entries named above were read.
- WAY-139's *Relations* in the spec gain WAY-267 with no type named, while D3 names `derives from` for
  the new decision. Read as `derives from`; unclear only in wording, so no finding.
- `foundations/decisions.md` line numbers in the task from WAY-219 on moved as the handoff says; the
  quoted passages were found at their entries.
