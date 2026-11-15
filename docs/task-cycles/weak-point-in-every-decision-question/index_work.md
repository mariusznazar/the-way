# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 47. Listed by heading alone: 122.

## Listed in full

### WAY-100 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.

A decision that adopts a method or practice from outside names the practice and what it takes from it, in its binding sentences or its *Rationale*; names the source in *Based on*, or, for a source a reader of the repository cannot open, describes in *Rationale* what was seen there (WAY-27); and puts what it leaves out of the practice in *Rejected*. A list of what is taken from one source is no decision: each rule taken stands in the decision that carries it (WAY-19).

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-07 — How is a foundation entry changed?

A foundation entry of any element carries no version: it is edited in place, on the main branch as before it, and holds only its current wording; the decision log has one entry for each number, and git keeps the earlier wordings.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

### WAY-114 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a projected entry at the readiness gate, shown as one sentence in the human's language with the entry beside it; that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement; and that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier, repeated in the human's language in the description's collapsed block, while the full list of the change's entries, each by its identifier with one English sentence of its meaning, stands in the description's lower part. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, task-cycle

### WAY-315 — From when does a decision of the foundation bind the work on a task?

A decision of the foundation binds the work on a task from the start of the task's cycle, the writing of a spec in the cycle included. In the cycle no agent departs from a decision on its own and returns with the question, as WAY-30 gives, and the looser rules that refinement follows for decisions (WAY-313, WAY-314), for the rows of its settlements (WAY-134) and for the question against an answer (WAY-113) hold only before that point.

- **Scope:** task-cycle, project-level, decisions

### WAY-33 — What does the author of a foundation change search for?

When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches — those that name the entry or that it names, and those no written link joins to it — and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human. The search is not repeated before the merge and leaves no record.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle, agent-instructions

### WAY-35 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

### WAY-113 — How does an agent of the-way ask a human decision?

An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way. While a project definition or a task document is refined, the technology step included, that question is asked only where the choice contradicts a sentence the human said earlier, which the question quotes, and that holds as well for the entries written during that refinement; in a task's cycle and where an entry is written outside such a refinement it is asked as above, the looser rule holding only before the cycle starts (WAY-315).

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level

### WAY-120 — How does the-way critique an agent's proposal?

An agent may invoke critique for any proposal without waiting for the human to express doubt; a completed set for collective human review goes through it, and the diff of a change to an invariant test or to the foundation does not (WAY-10). An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict. For a collectively reviewed set the critic checks form, fidelity to source and contradictions across entries before presentation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines

### WAY-150 — How do the-way skills choose which product foundation material to read?

The-way skills read a product's foundation selectively: whoever selects names the parts the work touches from the files it changes through the part map's rules for assigning files, or, where the work names no file yet, from the responsibilities it changes; finds by a touched part's identifier the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds the invariants a test the work alters cites, the decisions whose sentence such a test holds by a line `decision:`, the decisions the task's *Decisions in play* or the work's source names, the touched parts' entries of the map and the entries these link to as far as the work needs. Of the decisions it finds by *Scope*, by a line `decision:` or as the task or the work's source names them, whoever selects reads the index and opens whole only the decisions the work changes, goes against or proposes another answer to — that one with its rejected options — those the task or the work's source names, those whose sentence a test the work alters holds by a line `decision:` and those whose binding sentences leave open what the work has to do; each other entry it selects — an invariant, an entry of the map of a touched part, or an entry, a decision included, that these or the decisions of the index link to as far as the work needs — it reads whole, and it reads more entries where relevance is uncertain and a whole file only where it is short; the reviewer of the whole change reads the index of its whole selection and states in its report how many decisions it read whole. The selection is neither recorded nor compared with every *Scope* of the log, and the search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep their domain.

The index of a selection of decisions is no file of the repository: a script of the-way writes it on demand into a file the agent names, and it gives for each selected decision its number, its question, its binding sentences and its *Scope*.

In a decision log divided into topical sections, whoever selects picks from the list of sections, by each one's heading and sentence, the sections of the work's topics, whose decisions take the place of those found by *Scope* in the selection whose index it reads, and it runs through the questions alone of the decisions outside those sections whose *Scope* names a touched part and opens whole each whose question points to a bearing on the work. In a log without topical sections the decisions are selected by the parts the work touches, and their index takes the place of reading each of them whole, the decisions the first paragraph names being opened whole as it gives.

Outside the task cycle the agent doing the work selects its own reading, while in the task cycle the orchestrator selects for its own judgments and for each handoff, which names the foundation entries by identifier; the reviewer of the whole change selects for its own review, and an agent writing a foundation entry through an element's skill for the entry it writes; and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively — a search for an identifier or a word and a read of the passage found, never of a whole file of the foundation — naming each such reach in its report.

- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts, project-level, task-cycle

### WAY-106 — What does the project level write before tasks exist?

The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries. The definition holds the project's settled scope and projected foundation entries, while the project plan holds phases, task order and which task realizes or writes each projected entry.

- **Scope:** project-level, task-cycle

### WAY-118 — What makes a project definition ready for breakdown?

The readiness gate blocks a definition with a missing section, unresolved content, an open question without its place of resolution, an unfinished candidate search, or an unsettled human-given part of a projected entry: its binding sentence or definition and a decision's rationale and rejected options; only projected fields awaiting code or the world may read `TODO`. Before approval an agent searches the whole current foundation once for what the definition and its projected entries touch, linked or not, the only search of the whole foundation on the way to the gate, and the human approves the whole projected entries with permitted `TODO`; the gate record then names the approver and the fingerprint of the definition's sections from Goal through Projected foundation changes, and no projected entry carries a field of approval. A change to those sections after approval goes through the gate again before breakdown relies on it.

- **Scope:** project-level

### WAY-126 — How does a projected entry enter the foundation?

A projected entry of an approved project definition enters the product's foundation in the change of the first task whose code makes it true — the task the plan assigns, or a task that uses the definition as a source only, even where the plan assigns the entry to another task — whole, in the wording the readiness gate approved, with the projected terms and environment facts it uses or rests on and with no record of approval copied from the gate, since the merge of the task's request brings it in; where the code makes only part of it true, the agent writes that part and the human accepts its meaning at the merge (WAY-114). The task the plan assigns writes what of the entry the foundation does not yet hold, and a projected entry no code makes true. The return step reads the projected entries of the task's sources as well as the foundation, writes one the code makes true that the foundation step missed — an invariant with its test run on that code — and writes a new entry only for a rule none of them states.

- **Scope:** project-level, task-cycle, decisions, invariants, glossary, environment-facts, part-map

### WAY-145 — Who sets where an open question of an approved project definition is resolved?

Once a project definition has passed its readiness gate, the place of resolution it gives an open question is the question's first assignment, and the plan decides from then on where the question is resolved: in a task of the plan, or by an answer the human gives or the plan quotes, with its place, from the definition or the foundation. Work on the plan may move a question to another task, with an entry in the plan's log of changes giving the reason and without taking the definition through its readiness gate again, while a move that changes which task writes a projected entry into the foundation is the human's to decide. A question that arises only in the breakdown goes to the human before the plan is handed over.

- **Scope:** project-level

### WAY-121 — Where does a project settle the technology it needs?

Before a project definition goes through its readiness gate, a step of its own lists the technology and architecture choices the project needs — such as a language, a framework, a store of data or a place to run — and, for each, either names the decision of the foundation that already holds it or settles it as a projected decision of the definition; a project whose every choice the foundation holds thus settles nothing. A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up; a choice one task can make and change alone stays with that task, while a choice under this rule that a definition missed, or that no definition holds, is settled through a run of the step at a task document (WAY-267, WAY-268). As an exception to that rule, where the project brings behaviour a user sees in the running product, the step looks at four matters of an agent's way to the running product — its logs, its interface, its development data and the place of its screenshots — and lists as a choice of its own each matter that no decision of the foundation settles for that behaviour, even where its answer adds nothing to run, pay for or back up, and even where the product has none of what the matter names, whose answer then says what an agent uses in its place; how a human learns of a failure of the running product is no such matter and has an exception of its own (WAY-270).

- **Scope:** project-level, decisions

### WAY-122 — How are the options of a technology choice found and checked before a human sees them?

The options of each technology choice a project or a task needs come from research of that choice against the project definition or, in a run at a task (WAY-267), against the task document and the run's note, rather than from a fixed list of bundled stacks, and the research of every choice that depends on no unsettled choice starts once the list of choices is confirmed, each in a report of its own. An option the product's code is written in or against — a language, a framework, a library, a store of data — is weighed by whether its documentation shows that it uses explicit types, follows conventions of layout and naming and has current, versioned documentation, and whether a public record of its use, such as a package registry or a survey, shows it widely used within its language family; for a store of data, its types are those it declares for what it stores, and its family is that of its query language. An option lacking one of these properties is offered with what each lack means for the product, which the decision records if the human chooses it; an option with no documentation or with a project no longer maintained is left out with that reason, unless the human named it or the definition or the task document holds it as a constraint, and then it is offered with that reason as such a lack; and every option is offered only after a critique that refutes every claimed difference between the options which no source supports.

- **Scope:** project-level, decisions

### WAY-123 — How does a technology choice reach a human who cannot assess the technology?

The step that settles technology, at a project definition or at a task (WAY-267), shows each choice in plain text, in words a person who does not know the technology can follow: the options that decide it, each under its own name, by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs — the other options one line each, and the lines of the options left out; the human chooses between those consequences. A difference with no consequence for the product decides nothing, and where no difference with a consequence remains, the step recommends the simplest and cheapest option. The choices whose research started together reach the human together, in one message, one choice after another, once every one of their comparisons has passed the critique and a fresh agent has checked, in the first message, before it is shown, that no option stands there by figures or features instead of what it changes for the product and that no word stays that a person who does not know the technology cannot follow without an explanation, each choice with its recommendation and the weak point of the option recommended; in the area of the choices this step settles, this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** project-level, decisions

### WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?

Where the options of a place to run differ in no consequence for the product and more than one of them is the simplest and cheapest, the step that settles technology, at a project definition or at a task (WAY-267), recommends, of those, the one an agent works with best: operated from a terminal, deployed by a script and documented in pages an agent can read. For a place to run, how well an agent works with an option decides nothing else: it leaves no option out of the comparison and is weighed against no consequence for the product.

- **Scope:** project-level, decisions

### WAY-138 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?

The step that settles technology, at a project definition or at a task (WAY-267), tests the option it recommends for each choice it settles, one a constraint of the definition or of the task document settles included, with a devil's advocate, a pre-mortem and a search for unknown unknowns; it tests no choice a decision of the foundation holds, a choice the step opened being held by no decision, and no other decision already written is tested afterwards. The risks these tests give are hypotheses with no source, not differences claimed between options, so the critique of the comparison does not strike them, and they stand in the message beside the option recommended before the human chooses. The human who chooses that option takes its risks, and each risk taken reaches the decision of that choice in its *Rationale*, beside the lacks of the option chosen, marked as a hypothesis, through the task document where the step ran at a task.

- **Scope:** project-level, decisions

### WAY-267 — How does the step that settles technology run outside a project definition?

Besides its run at a project definition, the step that settles technology runs at a task document, with a note saying what the run is for, and a run with no task document starts by creating one through `refine-task`. A run at a task settles what the note and the task name, looks at the matters of an agent's way to the running product only where the note touches them, does the rest of its work as a run at a definition does and ends back in the task's refinement, with no readiness gate; a human may run it for any choice save one a projected decision of an approved definition settles, which no run reopens, and the step opens a choice a decision of the foundation holds where it sees a reason to change the decision (WAY-313), the result then being a change of that decision. The run writes each settled choice into the task document, with the options not chosen, the source of each difference claimed between the options, the lacks of the option chosen and the risks the human took with it, and the task's cycle writes the decision with the code that uses it.

- **Scope:** project-level, task-cycle, decisions

### WAY-268 — Who settles a technology choice that no decision or definition settles?

A technology choice whose later settling could change how the work is cut into tasks, or that adds something the product has to run, pay for or back up, and that no decision of the foundation, no approved definition the task carries and no accepted answer of its task document settles, is a reserved choice: the human settles it at the step that settles technology (WAY-267), so that it rests on a source that can be checked rather than on a model's memory, and in the area of these choices this decision prevails over WAY-114, under which an agent writes an entry on its own recommendation for the human to accept at the merge. Refinement that sees a reserved choice runs that step at the task, which is not ready until the human has settled it; in a task's cycle no agent settles one, its orchestrator included: the agent that meets it returns a report with no code and the status `reserved`, the attempt is discarded, the cycle opens a blocked draft request naming the choice and the task returns to refinement (WAY-269). Every other choice stays in the cycle, made by the agent that meets it and entered in the cycle record's questions table, and the tools the skills of guidelines choose stay on those skills' routes; whether a choice falls under this rule rests on the agent's judgment, helped by the examples of `project-level/technology/reserved_choices.md`.

- **Scope:** project-level, task-cycle

### WAY-269 — How does a task leave a cycle that met a reserved choice, and how does it come back?

A cycle that meets a reserved choice before its request opens ends with its attempt discarded, its task branch holding, above its base or the commit that moved the pin, only the commit that adds its record and the commit that removes it, and a draft request marked `blocked` that names the choice, says what did not run and why, and settles nothing; one that meets it in a correction takes back only that correction's commits and returns the request to draft marked `blocked`. Once the human closes the request, the task returns to refinement with its accepted answers and rows, the named choice being the note of a run of the step that settles technology (WAY-267), and a new cycle starts only after the human accepts the whole changed document, on a new branch and, for a task of a project plan, under the same name. For a task of a project plan, on the human's word, the project orchestrator removes by name that one cycle's worktree or working directory, its local branch, its branch on the host and that branch's remote-tracking ref, and then moves the plan's row back to `to refine`, with a line in the plan's log of changes naming the request.

- **Scope:** project-level, task-cycle

### WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?

Where a project runs the product outside the machine on which it is made, which holds unless the definition or a decision of the foundation keeps the product on that machine, and no decision of the foundation settles it, the step that settles technology lists how a human learns of a failure of the running product as a choice of its own, answered by a tool that collects failures, an alert or a deliberate absence, even where its answer adds nothing to run, pay for or back up; in a run at a task (WAY-267) it enters the list only where the note touches it. No definition has to hold this choice, the readiness gate does not check it and an approved definition does not come back to the step for it; it is no matter of an agent's way to the running product, so whether an agent can read an option is a consequence like any other, and a change to it does not open the decision on the logs. A deliberate absence always enters the comparison of this choice, though it has no page of documentation, its consequences anchored in the document and in the pages of the other options; in the area of this choice this decision prevails over WAY-121, which lists a choice by its rule of belonging and the four matters of an agent's way alone, and over WAY-122, which leaves out an option with no documentation.

- **Scope:** project-level, decisions

### WAY-124 — When is a task ready for its cycle?

A task document records whether the task is independent, belongs to an item of a project's plan, or uses an approved project definition as a source without belonging to its plan; it carries the task's scope, temporary exclusions, relevant current foundation decisions, any approved projected wording it uses and the settlements its refinement keeps for the foundation (WAY-134). It is ready when the human has seen and accepted its complete document, its required outcome is stated, every known question blocking that outcome is answered, the human has accepted or rejected every candidate settlement its refinement derived, a row that repeats a choice the human made between ways shown standing accepted until the human strikes it (WAY-134), every human action it places before the cycle is done (WAY-140), and implementation questions carried into the cycle are named. A project member also matches its plan item's scope, dependencies and assigned entries; any task using an approved definition checks that its approval still holds and names each projected entry, or the part of it, that its code makes true, while source-only use takes no other assignment or dependency from the plan.

- **Scope:** project-level, task-cycle

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form of the candidate table of the skills of the elements (`elements/common/skill/build_table.md`) with each settlement in the human's words and, in place of its kind, the place it goes to by the questions of the decisions template, and the task document keeps the rows the human accepts, one that goes outside the decision log included and those that repeat a choice the human made between ways shown included unless the human struck them, and, where the human chose among ways shown, each way not chosen, under the answer to its question or, for a choice made outside the task's questions, in the source of the row it settles; the agent refining the task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, or a settlement that goes to another place those questions give — a skill or an instruction file, the guidelines of a discipline, or the data or code of the product — and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate. The task's cycle writes each kept row whole in the place its column gives, in the same change as the code, in its foundation step, or in its return step where the foundation step missed it, one that no code makes true included, keeping its meaning and choosing its wording, and gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`; where that meaning cannot hold, or the entry needs any other value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft request rather than write another entry, and otherwise the entry's meaning is the one the human accepted with the row in the task document (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated becomes no second entry, the cycle tying the row to that entry and naming both in the request.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary, environment-facts

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task. For the human actions placed in the cycle, the cycle does what the repository allows and opens a blocked draft request listing them, and the human performs them at the request; a human action the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle. The human places each human action the task document names while the task is refined, on the agent's proposal: before the cycle when the cycle's code needs its effect, such as an account, a key or a database, and in the cycle when it uses code the cycle writes, such as a deployment or a DNS record pointing to a new address.

- **Scope:** project-level, task-cycle

### WAY-154 — How do agents exchange a project task refinement and keep its result?

Project refinement resumes from the plan, task documents and one ignored conversation file per task at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the answering agent and the project orchestrator take serialized turns on each file; the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`. Only a refiner changes the task document's body and transfers settled answers with their sources and the ways the human did not choose (WAY-134) into Questions to settle, and it writes besides what the project orchestrator's order asks of it: in the turn in which it first creates the task document, or in the first later turn that can where that turn could not, the line of its task in the backlog the product names (WAY-107), where none stands, with the dependencies the plan gives the task, and, as the rules of the task place give, brings the lines of the tasks tied to its task into agreement with the plan's dependencies, at the same time as the other refiners of the round and with no queue between their writes; the plan, the definition and the foundation stay outside a refiner, and no agent other than the project orchestrator, after the human's word, takes a step that belongs to acceptance, which is moving the line to ready and `ready for cycle`; the project orchestrator records human answers in conversations, owns ordinary plan updates and their log, brings the dependencies in the task lines in step with the plan when the plan's dependencies change, and after the human has accepted a complete task document, one document at a time, changes that document's Status line and moves the task's line to ready, making it already ready where none stands. Agent turns, questions and explicit waits keep the plan task to refine, a presented human package or ready for approval makes it waiting for human, and final acceptance makes both document and plan ready for cycle and removes only that conversation after all settled answers, their sources and the ways not chosen survive in the task document; an explicit wait is logged and its task is proposed again when the named prerequisite is done.

- **Scope:** project-level

### WAY-155 — What may the answering agent settle during a refinement round?

The answering agent answers a refinement question only with a quotation and source from the definition, plan, foundation or other task documents, or with a factual code observation naming file and line; a question about how the product is to be is answered only from a document, never from code or the agent's inference. It reads the round's conversations, makes an unanswered choice a question to the human with options, costs and a recommendation, and brings the same question to the human once while preserving its affected tasks; in the area of the choices a refinement round leaves unanswered, this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation. The project orchestrator presents one round package of these questions, candidate settlements, placement of Human actions and complete wording, together with every quotation answer as question, quotation and source; a quotation answer the human strikes becomes a question to the human, whose answers return to the conversations before fresh refiner turns.

- **Scope:** project-level

### WAY-355 — Which task fixes a defect found after a merge?

A task fixes a defect found after a merge when it removes a defect against what the task of an earlier merged change, or the foundation, required when that change was merged, or a regression, which is the breaking of something that worked and that the earlier change's task did not tell it to change. A new need, a change of mind, a gap of the earlier task, a thing it did not foresee, and maintenance such as updating a dependency are no such defect.

- **Scope:** project-level, task-cycle, process-audit

### WAY-372 — When is a task split into several tasks?

A split of a task is proposed only where it makes the work better or cheaper; time does not count, so that a part is ready sooner is no reason. Whoever proposes a split names its reason, and the reasons are three: a part cannot start or finish without something outside the refinement of the task, such as access the agent lacks or another task's result; the parts change different repositories (WAY-140); or a later step of the refinement offers a separate task. A task's size alone is no reason: for it an agent says nothing of a split — no mention, no question, no recommendation — and a split the human asks for, who sees the whole document, stands without one.

A project plan cuts its tasks by WAY-143 and by these reasons, never by a task's size alone.

- **Scope:** project-level

### WAY-374 — Does the refinement of a task ask about a word its sources leave readable in two ways?

At its step that resolves the gaps, the refinement of a task looks in the task document and in the sentences of the sources its required result rests on — the foundation decisions the document quotes and the sentences of the approved project definition — for a word that allows two different required behaviours and that none of the approved project definition, an entry of the foundation, a glossary entry included, and an answer of the human in the document settles. Where a sentence standing in the document or in such a source allows both readings and the readings give different, observable results inside the task's scope, the agent shows a short example from that scope and asks the human which reading holds, as a question of decision (WAY-113); the answer stands under the task's *Questions to settle*.

A reading no sentence allows and a case outside the task's scope raise no question, the check owes no finding and no number of cases, and where the agent finds none it says nothing of the check. A meaning the human settles that a reader who knows the product's field would not give the word goes to the task's *Settlements to record* as a candidate glossary term, which WAY-95 judges there, and an ambiguity in the approved project definition whose resolution changes the definition goes back to the definition and its readiness gate (WAY-118).

- **Scope:** project-level

### WAY-377 — Does the refinement of a task list the decisions its document leaves to the executor before the human sees the document, and who lists them?

Before the refinement of a task shows its complete document to the human, it has the decisions the document leaves to the executor listed where the document's *Decisions in play* is not `none` or the task changes a skill or an instruction file, and for no other task. Two fresh agents of one class of model, cheaper than the refining agent's and named in general terms, never by the name of a model, make the list: the first, given the complete document and the full text of the entries *Decisions in play* names, lists each decision an executor would have to take on its own that they leave unanswered or answer in part, and marks each answer as written, visible only in a file the document names as a model, or guessed; the second, with read access to the repository the task changes, settles each guess against the repository and the document. A decision counts only where it follows from a sentence that stands in the document or in a named entry and where different answers give a different, observable result inside the task's scope, and the list owes no decision and no number (WAY-374).

- **Scope:** project-level

### WAY-378 — What does the human see after the decisions a task document leaves to the executor are listed and criticised?

The refining agent shows the human only the matters that the second agent of WAY-377 leaves truly open and the gaps of the document itself, at most about four, the most consequential first, each in plain language as WAY-113 asks a decision, with the ways, the cost of each and a recommendation; the full list and the critique stay in a file in the ignored `.runs/` directory of the product, whose path the agent gives the human. Before it shows a matter, and before it keeps a guess from the human on the critique's verdict that the repository or the task document already settles it or that it is most likely right, it checks the quotations behind that verdict and gives the matter one explicit verdict (WAY-120), and where no matter is open it says nothing of the step.

- **Scope:** project-level

### WAY-11 — How does a task end?

A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches. In the same change it writes the sources outside the product that the change rests on and the foundation does not yet hold, as environment facts, a word the change uses in a meaning for which WAY-95 gives it an entry, as a glossary term, and the accepted settlements (WAY-134), each in the place the questions of the decisions template give it and as an entry of the decision log only where it passes all of them and where someone who does not know the decision would do otherwise and a test that stops them would not tell them why, and projected entries (WAY-126) the task carries that are not yet written. It writes an invariant only for a rule the task, a decision or a human sets, never for code behaviour merely because no invariant covers it.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle

### WAY-13 — What sets the weight of a task's process?

Every change, whatever its size, passes the product's tests and a review by an agent that did not make it. At its start a task's cycle answers two questions — does the change touch the files of a trust boundary (WAY-48), and does it hold an operation that cannot be undone — and a change for which either answer is yes gets a review aimed at that risk; an operation that cannot be undone is only prepared, and a human performs it after deciding at the request. A task's size may lighten how its change is prepared and made — its plan and the number of agents making it — never the outcome it has to reach or the checks run on the finished change, and outside preparing and making the change it decides nothing; only a human sets a task to return knowledge instead of a change, which merges nothing.

- **Scope:** task-cycle

### WAY-125 — Which methods does the autonomous task cycle use?

The task cycle `implement-task` uses the-way's own methods: `write-spec` for a spec and its review, `plan-task` for a plan, `make-change` for each change an author, a slice's executor or a fix makes, and `review-change` for each code review; the orchestrator conducts the cycle and its loop of slices itself. Each agent reads the `SKILL.md` of its stage's method whole, and a file the method names, one beside that `SKILL.md` included, only when the step or variant that names the file comes, while the orchestrator reads no method it does not conduct.

- **Scope:** task-cycle

### WAY-135 — When does a task's cycle write a spec?

A task's cycle writes a spec, reviewed by an agent other than its author, before implementation and any plan where the task leaves an open design choice and nowhere else, and an invariant whose sentence a row of the task's *Settlements to record* or a projected entry of its sources gives leaves none. An agent that meets an open design choice while it makes the change returns a report that holds no code, the attempt is discarded with the foundation entries the cycle wrote for it, and a fresh agent given the report writes the spec, after whose review the orchestrator chooses again whether one author can hold the change or it needs a plan, using the same judgment as before implementation (WAY-136). Where the open design choice is a reserved choice, no spec is written: an agent's report without code and the discard of its attempt stay the same, and the cycle stops (WAY-268, WAY-269).

- **Scope:** task-cycle

### WAY-136 — When does a task's change need a plan, and who makes and reviews it?

A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split. A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own and names, for each blocking finding, the slice it comes from or that it comes from none, while the review of a one-author change or of a plan's only slice is the review of the whole change; and that review also checks coverage of the task, every row of its *Settlements to record* and every projected entry it carries.

- **Scope:** task-cycle

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads the cycle record, an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it. The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class. An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class that fails, or a retry that fails, stops the cycle. The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every reviewer — the review of the whole change and the review of the return step included — work on no class cheaper than the orchestrator's.

- **Scope:** task-cycle

### WAY-10 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation has no assessment of its own, in a product as in the-way itself: an agent that did not make the change reviews the whole change, its foundation entries and invariant tests included, against its task and the foundation, and a human reads the section of the request's description for the human's decisions and accepts the change by merging the request.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, task-cycle, agent-instructions

### WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?

In the review of the whole change on either route, a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope, and a Minor finding that the review lists and the reviewer has not marked so is fixed before the request opens — in the fix that runs for the blocking findings or, where none blocks, in one fix of its own that WAY-162 bounds. A finding the reviewer has marked as outside the task's scope — a line of its list of what it declined to judge, or a finding it describes as going beyond the task — is not fixed, whatever its grade, and the request lists those findings in an item of their own and, in another, the Minor findings that no fix made — those of the code reviews after the review of the whole change, those of a slice review that the review of the whole change does not list, those a fix left, and those of a fix that WAY-162 reverted — each with the reviewer's words and its place in the code, while the human decides which findings outside the scope become new tasks and creates them. The orchestrator moves no finding from one of these kinds to another.

- **Scope:** task-cycle

### WAY-162 — How does a code review of a task's change end when its findings block?

In every code review of a task's cycle — of a slice of its plan, of the whole change, of the return step's commits, of the reconciliation with the target branch and of a change made for the human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and one review of that fix, and a new Critical or Important finding in the fix itself counts as one that remains. Where a blocking finding remains after that review of the fix, no third round runs, the orchestrator does not rule on it, no further slice is made, and the cycle opens a draft request marked `blocked` that lists each remaining blocking finding with its place in the code and its reason, what the fix tried, and the time, models and tokens the cycle has used so far, from its record of stages, with the number of review rounds. Where the review of the whole change leaves no blocking finding and lists Minor findings that WAY-161 has the cycle fix, one fix takes them in and one review of that fix follows, and where that review finds a new Critical or Important finding in the fix, the cycle reverts the fix's commits with a commit of its own, so that they stay in history, runs no third round and opens the request, not blocked, on the code the review of the whole change accepted, the request listing the Minor findings the fix tried and the new finding with its grade and as the review of the fix found it. In the code reviews after the review of the whole change, and for a Minor finding that remains after a fix, the findings that do not block go unfixed to the request's lists as WAY-161 gives them.

- **Scope:** task-cycle

### WAY-263 — Which foundation mismatches are Important findings?

A reviewer grades as Important a finding that a change departs from a foundation entry it writes or changes: the change's files do what the entry forbids, fail to do what it requires, or restate it differently, including more broadly or without a qualification.

- **Scope:** task-cycle

### WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?

A reviewer grades as Minor a finding that a word needs a glossary entry, or that a word of the process lacks the qualifier WAY-104 gives it in a product's foundation, unless the finding cites a sentence the files hold that a reader would read wrongly for lack of it; a finding that cites such a sentence is graded as any other. The renaming of a word with two meanings (WAY-99) is graded as before, and a finding that a glossary entry the change writes or changes departs from a foundation entry stays Important (WAY-263).

- **Scope:** task-cycle, glossary

### WAY-363 — How does a reviewer grade a finding about the structure of code?

A reviewer grades as Minor a finding about the structure of code that lies below the threshold of the rule of size in the product's coding guidelines, and every such finding in a product that has no rule of size, whatever the reason: for example, it departed from the rule by a decision, it has no coding guidelines at all, or its guidelines were written before the rule existed. The reviewer judges its scope as for any finding (WAY-161). A finding about a function or a file over a threshold is graded as any other finding.

- **Scope:** task-cycle, product-guidelines

### WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?

A reviewer grades as Minor a finding that a foundation entry departs from the form of its template, where the entry's content agrees with the code, unless the finding cites a sentence a reader would read wrongly through the departure; a finding that cites such a sentence is graded as any other. A finding that the content of an entry does not agree with the code stays Important (WAY-263).

- **Scope:** task-cycle

### WAY-174 — How do the-way's skills of guidelines ask the human?

The-way's skills `maintain-styleguide`, `maintain-coding-guidelines` and `maintain-testing-guidelines` put to the human every choice they settle for a product's guidelines, a choice they recommend included, and show each in plain words — a styleguide's by what someone using the product sees on the screen, never by the names or values of design tokens, coding guidelines' by their effect on the product, never by the names of a linter's rules or the values of a tool's configuration, and testing guidelines' by their effect on the product, never by the name of a technique or a tool — saying in plain words what a term of the field means before they first use it. The coding-guidelines skill asks for decisions, never for single rules, so that the human adopts a linter's set of rules whole. In the area of the questions these skills ask this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** product-guidelines, decisions

## Listed by heading alone

- WAY-09 — What may enter the process repository?
- WAY-27 — Where may this repository point for its reasoning?
- WAY-28 — How does the process enter a product that already exists?
- WAY-34 — Which version of the process does a product use?
- WAY-101 — Who chooses the backlog tool used with the-way?
- WAY-102 — What is the-way for?
- WAY-103 — Who is the-way for?
- WAY-107 — Where does a product tell the project level where its backlog stands?
- WAY-01 — What state does the foundation describe?
- WAY-02 — How does whatever depends on an entry refer to it?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-21 — What is a decision's scope?
- WAY-26 — How are trade-off principles and non-goals written?
- WAY-36 — Is a rule a decision or does it belong in a plan?
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice?
- WAY-24 — How is a decision that rests on a prediction reviewed?
- WAY-25 — What settles a collision between two decisions?
- WAY-30 — What happens when a change contradicts a decision?
- WAY-313 — What is a decision of the foundation to the refinement of a project or a task?
- WAY-314 — Which act of the human consents to a change of a decision that refinement shows?
- WAY-03 — Who may change an invariant test, and when?
- WAY-51 — What does the main branch hold where the product does not meet an invariant?
- WAY-61 — How is an invariant's method of checking written?
- WAY-62 — What does an invariant entry name in the part map?
- WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?
- WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?
- WAY-82 — How does an environment fact keep up with what its source says?
- WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?
- WAY-44 — What assigns a file to a part?
- WAY-48 — How is a trust boundary recorded?
- WAY-16 — How are the checks of invariants run?
- WAY-38 — In what are the scripts of the-way written?
- WAY-55 — Which part of the process holds the gate?
- WAY-63 — What is an invariant's result, and when does the command running the tests fail?
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?
- WAY-160 — How does the task-cycle orchestrator run the finished change's gate?
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?
- WAY-127 — How does a session working on the-way itself reach the-way's skills?
- WAY-256 — Where does a fragment of a skill stand?
- WAY-265 — Where is the file of a variant named, when a step's file points to it?
- WAY-368 — Which agents run the stages of a task cycle in Claude Code?
- WAY-370 — What does a task cycle do where the session has none of the-way's agent types?
- WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?
- WAY-165 — What must an answer to each matter of an agent's way to the running product settle?
- WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?
- WAY-273 — May a product hide a failure?
- WAY-274 — Where does a product's logging scope stand, and who adds to it?
- WAY-276 — What do a product's logs not hold?
- WAY-319 — What must an agent's way to the running product allow when two task cycles run at once?
- WAY-142 — What does the breakdown of a project write, and in what form?
- WAY-143 — What does a task of a project plan end with?
- WAY-144 — How does a project plan show which tasks can be worked on side by side?
- WAY-146 — What checks a project plan before it is handed over?
- WAY-147 — How is a task of a project plan named, and what does its cycle take from the name?
- WAY-153 — What evidence supports a task state in a project plan?
- WAY-230 — How does a project plan order two tasks that realize the same projected entry?
- WAY-164 — What does the author of a change check of its own work before review?
- WAY-255 — How does an agent of a task's cycle wait for a command that runs long?
- WAY-260 — What does each task-cycle stage report about what it could not find or understand?
- WAY-261 — What does a task cycle report about a check that fails and passes when run again?
- WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?
- WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?
- WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?
- WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?
- WAY-227 — Where does the human meet a task cycle's work?
- WAY-287 — What does a request put before the human for a decision?
- WAY-288 — In what language is a request's description written?
- WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?
- WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?
- WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong?
- WAY-300 — When does a request tell the human that the foundation waits for a review?
- WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?
- WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?
- WAY-309 — How does the cycle find the private paths and notes in what it publishes?
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?
- WAY-324 — How does a product check the files it tracks for private paths and notes?
- WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it?
- WAY-337 — How is the cost of a cycle measured?
- WAY-339 — When do the measures of the audit stop being comparable?
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
- WAY-167 — Where do a product's guidelines stand, and what are their files named?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?
- WAY-212 — How does a product's instruction file lead to its coding guidelines?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-312 — Which sentences does a rule of a product's guidelines not hold?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
- WAY-215 — What happens to a task that needs missing discipline guidelines?
- WAY-216 — What does refinement assign to a task creating an unindexed kind of code?
- WAY-247 — May one task write a product's coding and testing guidelines together?
- WAY-251 — What distinguishes a refresh from an extension of guidelines?
- WAY-280 — On what scale does an audit of the skills of guidelines weigh what it found?
- WAY-284 — What decides which causes of an audit a task takes?
- WAY-198 — How does a product's exemplar bind?
- WAY-199 — What change of a product's exemplar takes approval?
- WAY-202 — Which standing checks must a product's coding guidelines settle, and from when do they bind?
- WAY-203 — Which rules of a linter's set block a change of a product's code?
- WAY-204 — How are the rules of a linter's set split between the rules that block and the examples?
- WAY-205 — How do a linter and a formatter enter a product whose code already breaks their rules?
- WAY-206 — What does the audit of a product's dependencies check?
- WAY-360 — Does the template of the coding discipline require a rule of the size of a function and a file, and how does it reach a product?
- WAY-361 — How does the review of a change get the sizes of functions and files from a product?
- WAY-228 — Where does a test take the input it asserts on and the value it expects?
- WAY-231 — Where do the rules of a product's tests stand?
- WAY-232 — Where does a test's expected value come from?
- WAY-233 — What does a change to an existing test need?
- WAY-234 — What may a test's assertion check?
- WAY-235 — How do a product's tests keep its trust boundaries?
- WAY-236 — How does AI enter a product's tests?
- WAY-237 — What does a product deliberately not test, and where is it said?
- WAY-238 — At which level does a test stand, and who chooses it?
- WAY-239 — What does a bug caught only by a high-level test or by a human get?
- WAY-240 — How do a product's testing guidelines name its test levels?
- WAY-241 — What does the recipe of a test level hold?
- WAY-242 — How is the exemplar test of a level designated?
- WAY-243 — How is a flaky test treated?
- WAY-244 — When do a product's testing guidelines come into being?
- WAY-252 — How does a mutation tool check a product's tests?
- WAY-253 — Who runs a mutation tool in a task's cycle, and what does the author check in its place?
- WAY-254 — Where does the command of a mutation tool stand?
