# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 50. Listed by heading alone: 157.

## Listed in full

### WAY-07 — How is a foundation entry changed?

A foundation entry of any element carries no version: it is edited in place, on the main branch as before it, and holds only its current wording; the decision log has one entry for each number, and git keeps the earlier wordings.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

### WAY-17 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional: a decision and an invariant name the environment facts they rest on, an invariant derived from a decision names that decision, and a check names its invariant, or, where it holds a decision's sentence by a line `decision:`, that decision, with no invariant between.

- **Scope:** decisions, invariants, environment-facts

### WAY-05 — How is a decision entry written?

A decision entry opens with one to three binding sentences that answer its question — in the present tense, describing a state that is to be true, concrete enough to check — and one paragraph of one to three binding sentences for each part of another question that it answers, followed by fields a script or an agent reads, then rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count — a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound — nor what the process's own tools do or lack today, and does not tell how the decision was reached. A field stays in the template only while someone or something reads it, and what a decision forces on later work stands in a binding sentence or a field, never in prose. An example in `elements/decisions/` names a decision of the log by its number instead of copying it.

- **Scope:** decisions

### WAY-12 — How is a decision checked?

A decision names in *Verification* the invariants derived from it, by the identifiers of their entries, where such invariants exist, and the tests that hold its sentences, by a clause that gives the parts of the sentences they hold in words and no path, no test name and no number. A test that holds a sentence of a decision carries beside it a line `decision:` that gives the number of the decision and the start of that sentence, and the decision keeps its rationale and its rejected options whole. A decision may also carry a pair of examples — a change that complies and one that violates — only for the part of its sentences that no invariant and no test checks, with which an agent compares a change with that part; the violating example is a change whose code goes against the decision while its entry stays as it is, never one that replaces the decision together with its code.

A decision is held when its *Verification* names an invariant, when a test holds a sentence of it by a line `decision:` that names its number, or when it carries a pair of examples. The check of the foundation reports as an error a decision that a change adds, or whose binding sentences the change alters, and that nothing holds. Any other decision that nothing holds stands in a list the check prints, and the list stops no change.

- **Scope:** decisions, invariants

### WAY-18 — How is a product's decision log kept?

A product keeps all its decisions in one log, whatever they are about. The log holds one entry for each decision in force and itself says what binds today, with no view generated from it kept in its place; the index of a selection of decisions that an agent writes on demand (WAY-150) is no such view. A link between entries is written at one end only; the one exception is a decision's invariants, which its *Verification* names while each of them names the decision in *Derives from*.

A log may be divided into topical sections, each a heading with one sentence of what it covers, its entries keeping their numbers; in a log so divided a new entry stands at the end of the section of its topic, or, where no section fits, in a new section at the end of the log, which the request that adds the entry names. A log without topical sections holds its entries in the order they were written, a new entry at its end.

- **Scope:** decisions

### WAY-19 — How are decisions numbered?

A number stands for the question a decision answers, carries the product's prefix and is given in the order entries are written; a new question gets the next free number, a question independent of every existing entry included, while a part of the question an existing entry answers is a sentence of that entry where it cannot change without changing that entry. A new answer to a question the log holds rewrites that question's entry. When a new decision answers a question that an older one answered in passing, the sentence moves to the new decision, and the older one loses it in the same change.

- **Scope:** decisions

### WAY-21 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never file paths, so that the decisions governing a change are found from the files it touches through the part map's rule for assigning files.

- **Scope:** decisions, part-map, task-cycle

### WAY-22 — Is a rule a decision or an invariant?

An invariant says nothing about why or what was rejected; a decision is a choice between options, with its rationale, and it binds later work until a change replaces, narrows or withdraws it, including what cannot be checked on a commit — direction, trade-off principles, non-goals. A rule that records a choice is a decision, and what of it a commit can make false is written as an invariant derived from it, unless a test holds that sentence by a line `decision:`, in which case the decision gets no derived invariant for it; an invariant stands for a rule with no choice behind it and for a rule on which several decisions stand. A single text, number, list or location is no entry of the log: it stands in the product's data or code, with the test that holds it and, where its reason is not obvious, a comment at the value.

- **Scope:** decisions, invariants

### WAY-26 — How are trade-off principles and non-goals written?

Each trade-off principle is a decision of its own, whose binding sentence says which of two good things is chosen when they conflict and whose rationale names the problem it solves. Each non-goal is a decision of its own that says what the product does not do and why. What the product does not do only because no work has brought it yet is no non-goal: where later work builds on it, a decision states what the product does today.

- **Scope:** decisions, task-cycle

### WAY-29 — How is a decision recovered from an existing product written?

A decision recovered from the code of an existing product says in *Origin*, in one sentence, that it was recovered from the code and where in the code it shows, and its rationale and rejected options are quoted from a source, given by a human who knows them, or written as `unknown`. A rationale an agent proposes for a human's decision goes to the human as a question, never into the entry; the rationale of a decision an agent takes in a task is the agent's to write. The description of the commit, or of the merged request, that brought the shape of the code is such a source: an agent looks there before it writes `unknown`, and quotes what it finds with the identifier of the commit.

- **Scope:** decisions

### WAY-36 — Is a rule a decision or does it belong in a plan?

A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work, or in the choices of its cycle record where no plan is written.

- **Scope:** decisions, task-cycle

### WAY-293 — What prevails where a task or its spec excludes the entry for a choice?

Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion prevails over the rule that a choice binding after the merge goes to the place the questions of the decisions template give it, and the choice stays a row of the cycle record's questions table; without such an exclusion the rule applies as before. In the area of choices that a task or its spec explicitly excludes from the foundation, this decision prevails over WAY-22 and WAY-18. A candidate left out of a task's *Settlements to record* is no exclusion.

In the log of the-way, a rule that stands in one skill or template of the-way stands there with one sentence of its reason. It is an entry of the log only where it carries a choice with a real cost, one for which someone could reasonably propose the rejected way, and the skill or template then names that decision.

- **Scope:** decisions, task-cycle

### WAY-114 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a projected entry at the readiness gate, shown as one sentence in the human's language with the entry beside it; that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement; and that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier, repeated in the human's language in the description's collapsed block, while the full list of the change's entries, each by its identifier with one English sentence of its meaning, stands in the description's lower part. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, task-cycle

### WAY-33 — What does the author of a foundation change search for?

When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches — those that name the entry or that it names, and those no written link joins to it — and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human. The search is not repeated before the merge and leaves no record.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle, agent-instructions

### WAY-03 — Who may change an invariant test, and when?

Any change may alter an invariant test, in any step of its task, implementation included. A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.

The check of the foundation lists an invariant whose method is `test`, whose sentence a change has reworded and which a file cites by a line `invariant:`, when no file that cites it has changed since the commit the branch left the main branch from. A change whose check lists such an invariant names it in its request in plain words, giving what its sentence now says and that the test that checks it was left as it was. The listing stops no change.

- **Scope:** invariants, task-cycle, agent-instructions

### WAY-08 — How is an invariant checked?

Every invariant names its method of checking: a test of the product's test suite where a cheap test can check its sentence, and review otherwise, where the review of each change by an agent that did not make it compares the change with the sentence. The status of an invariant with a test comes from running that test, never from a status written by hand. An invariant's test is seen failing once, with the command that later shows it passing — run before the code that satisfies it, or, where the code already has the behaviour, against that behaviour broken for a moment.

- **Scope:** invariants

### WAY-51 — What does the main branch hold where the product does not meet an invariant?

On the main branch an invariant the product does not meet today stays whole and is marked violated at its entry; an invariant is marked violated only by a change of the foundation that a human accepts, never by a step of implementation. A change that sets or clears the mark names it in its request; the test of a marked invariant stands in the product's suite marked as an expected failure in the product's test tool, and the change in which it starts to pass removes that marking and the mark of the invariant. While an invariant is marked violated, no second invariant compares the product with its state on `{fork-point}`, and the review of each change to the files of the parts the invariant names keeps a cleaned file or a new one from breaking it again until the mark is cleared.

- **Scope:** invariants, gate, task-cycle, product-guidelines

### WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation change a human decides, or where a decision in the product's log or the pinned the-way places it. An invariant whose condition stands outside its sentence names by identifier the entry or the decision that holds the condition, in a field where the template gives one and otherwise in its sentence.

An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}` (WAY-61), while a state it compares may be the one on `{merge-onto}`, and states what is to hold on the main branch alone as holding where `{merge-onto}` exists. A sentence bounding or equating a quantity measured while the product runs names its bound or tolerance, statistic and population.

- **Scope:** invariants, decisions, part-map, gate

### WAY-61 — How is an invariant's method of checking written?

An invariant's method of checking reads `test` once a test of the product's test suite, written in the product's language and run by the command that runs the product's tests, cites it, and `review` until then, and it names no command and no script. The method is held on the finished change: an invariant whose test a later slice of the same change writes may read `test` from its writing on. A test checks what its invariant's sentence is about, as it stands on the commit being checked, so a test fed input made up for it is the method of a sentence about the check it exercises, never of one about the data that check reads.

- **Scope:** invariants, gate, decisions, part-map, elements-common

### WAY-62 — What does an invariant entry name in the part map?

An invariant entry names the parts of the part map where a change can make its sentence false, or `every` where a change to any part can. A change, against the commit its branch left the main branch from, reaches an invariant that names `every` or a part the change touches, or that a test the change alters cites, whatever parts a file collecting entries gives that change (WAY-44), and the agent making the change reads every invariant it reaches. The entry names no critical flow or surface.

- **Scope:** invariants, part-map, gate, task-cycle

### WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?

An invariant's sentence, its test and the code the test covers may come from one agent; the agent reviewing the change, which made none of it, reads the test against the sentence.

- **Scope:** invariants, gate, task-cycle

### WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?

`elements/common/foundation_check.py` reports an invariant whose method reads `test` and which no line `invariant: <identifier>` in a file git tracks whose name does not end in `.md` cites, in every run but the one made right after an entry is written, which passes the switch `--skip-test-citations` and so skips this report and no other. The one command that runs a product's tests runs the script without that switch (WAY-16).

- **Scope:** elements-common, invariants, gate, installation

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it. In CI that command runs on every merge request, with `.the-way` at the commit the product pins (WAY-34), from a file of CI configuration that the product writes itself by the description the-way gives, and the installer writes none. The result of that run is a check the repository requires before a merge, and the owner of the repository may bypass it.

- **Scope:** invariants, agent-instructions, task-cycle, gate, installation

### WAY-38 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.

A test of a standing check runs the tool that the check pins from the environment that the repository declares.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions, instruction-files, project-level, task-cycle, process-audit

### WAY-55 — Which part of the process holds the gate?

In this repository, the gate is a part of the process of its own, and its directory is `gate/`: the gate's code and the test of every critical flow are files there. No other part's directory holds that code or such a test, and a file under `gate/` that only calls a body kept in another part's directory leaves the gate in that part. Which checks a change calls for, when the gate runs and what follows from what it reports belong to the task cycle, not to this part.

- **Scope:** gate, decisions, invariants, glossary, part-map, environment-facts, relation-model, repository, task-cycle

### WAY-63 — What is an invariant's result, and when does the command running the tests fail?

An invariant's result on the commit being checked is `pass` where every test citing it ran on that commit and passed, and `fail` where one of them failed; a run in which no test citing it ran gives it no result, and nothing written by hand stands in for one. An invariant whose method is review takes no result from a run: the review of each change it reaches compares the change with its sentence. The command running the product's tests exits non-zero when a test fails.

- **Scope:** invariants, gate, part-map, task-cycle

### WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and the declared version moves when the version in use leaves bugfix support, never because a newer version comes out.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions, instruction-files, project-level, task-cycle, repository, process-audit

### WAY-160 — How does the task-cycle orchestrator run the finished change's gate?

The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it. Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the orchestrator waits for the result of the run on each head it pushes to it, a correction's included, treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review, save a check outside the task's scope that passes when run again, which WAY-261 governs — and puts the result into the request's description; a request the cycle leaves blocked for unfinished code is out of that wait, its description saying that the result of the run stands on the request's page and was not waited for.

- **Scope:** task-cycle

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives no line `Error:`. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*. The command that counts the audit, where a table of weights or a table of the costs of an occurrence in the register of problems lacks one of its levels, writes its result, gives the values that depend on the table as unknown and ends with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither of the two columns of the cache writes in its detailed section, that command reads the report as an earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and priced as input, an approximation, and no value unknown for the missing columns, while a stage report that has one of the two columns and not the other has a missing field, with the line `Error:`. Where the locations file has no entry `repository` under `the-way`, no field is missing and that command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?

The-way holds no skill of a product, but the list of what a product's deployment skill covers: a preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of steps and what happens to the data; what the agent does and what the human does; how to read the logs; how long the record lives, between deployments too; and how a human learns of a failure. Beside the list it holds a guide to writing such a skill, with the deployment skill of loop2 as its first example, which binds nothing and which the check of the list points to. When a task's outcome deploys the product or changes how or where it runs, the-way's skill `refine-task` checks, while it refines the task, that the product has a deployment skill covering every item of the list, and where it has none or an item is missing, the task gains an item of its To do for that work or the human splits that work into a task of its own, and that item and that task point to the guide, which an agent reads only when it writes or completes a deployment skill; for the items on how to read the logs, on the record's life and on a failure, the check quotes the answer a decision of the foundation or an approved definition the task carries already gives, and the task gains the item that writes it into the skill, a decision silent on how an agent reads the logs or on how long the record lives answering nothing for the item on that; where nothing answers the item on how to read the logs, it goes as the other items of the list do, and where nothing answers the item on the record's life or on a failure, the check asks the human whether to run the step that settles technology at the task (WAY-267), with a note on what the skill leaves unsaid, instead of filling the item in, and a skill that records the human's refusal covers the item, so the question does not return.

- **Scope:** project-level

### WAY-142 — What does the breakdown of a project write, and in what form?

The breakdown of a project writes its plan as one document beside the approved definition, whose header names the definition and the fingerprint the definition's gate record holds, and whose `Status:` line says whether the plan is still a draft or has been handed to the human. Each task stands in one row of one table of tasks, with the columns and states the plan template gives, while the tasks that realize each projected entry and the one task that writes it into the foundation stand in a table of their own, a row for each entry under the heading the definition gives it. The plan also holds each open question of the definition, word for word, with where it is resolved, its phases with what closes each where it has any, and a log of its changes, each with its reason, written in the language of the definition under headings, states and markers kept in English.

- **Scope:** project-level

### WAY-124 — When is a task ready for its cycle?

A task document records whether the task is independent, belongs to an item of a project's plan, or uses an approved project definition as a source without belonging to its plan; it carries the task's scope, temporary exclusions, relevant current foundation decisions, any approved projected wording it uses and the settlements its refinement keeps for the foundation (WAY-134). It is ready when the human has seen and accepted its complete document, its required outcome is stated, every known question blocking that outcome is answered, the human has accepted or rejected every candidate settlement its refinement derived, a row that repeats a choice the human made between ways shown standing accepted until the human strikes it (WAY-134), every human action it places before the cycle is done (WAY-140), and implementation questions carried into the cycle are named. A project member also matches its plan item's scope, dependencies and assigned entries; any task using an approved definition checks that its approval still holds and names each projected entry, or the part of it, that its code makes true, while source-only use takes no other assignment or dependency from the plan.

- **Scope:** project-level, task-cycle

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form of the candidate table of the skills of the elements (`elements/common/skill/build_table.md`) with each settlement in the human's words and, in place of its kind, the place it goes to by the questions of the decisions template, and the task document keeps the rows the human accepts, one that goes outside the decision log included and those that repeat a choice the human made between ways shown included unless the human struck them, and, where the human chose among ways shown, each way not chosen, under the answer to its question or, for a choice made outside the task's questions, in the source of the row it settles; the agent refining the task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, or a settlement that goes to another place those questions give — a skill or an instruction file, the guidelines of a discipline, or the data or code of the product — and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate. The task's cycle writes each kept row whole in the place its column gives, in the same change as the code, in its foundation step, or in its return step where the foundation step missed it, one that no code makes true included, keeping its meaning and choosing its wording, and gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`; where that meaning cannot hold, or the entry needs any other value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft request rather than write another entry, and otherwise the entry's meaning is the one the human accepted with the row in the task document (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated becomes no second entry, the cycle tying the row to that entry and naming both in the request.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary, environment-facts

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task, nor is the removal of the repository's own working directories that stand outside its directory (WAY-375). For the human actions placed in the cycle, the cycle does what the repository allows and opens a blocked draft request listing them, and the human performs them at the request; a human action the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle. The human places each human action the task document names while the task is refined, on the agent's proposal: before the cycle when the cycle's code needs its effect, such as an account, a key or a database, and in the cycle when it uses code the cycle writes, such as a deployment or a DNS record pointing to a new address.

- **Scope:** project-level, task-cycle

### WAY-154 — How do agents exchange a project task refinement and keep its result?

Project refinement resumes from the plan, task documents and one ignored conversation file per task at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the answering agent and the project orchestrator take serialized turns on each file; the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`. Only a refiner changes the task document's body and transfers settled answers with their sources and the ways the human did not choose (WAY-134) into Questions to settle, and it writes besides what the project orchestrator's order asks of it: in the turn in which it first creates the task document, or in the first later turn that can where that turn could not, the line of its task in the backlog the product names (WAY-107), where none stands, with the dependencies the plan gives the task, and, as the rules of the task place give, brings the lines of the tasks tied to its task into agreement with the plan's dependencies, at the same time as the other refiners of the round and with no queue between their writes; the plan, the definition and the foundation stay outside a refiner, and no agent other than the project orchestrator, after the human's word, takes a step that belongs to acceptance, which is moving the line to ready and `ready for cycle`; the project orchestrator records human answers in conversations, owns ordinary plan updates and their log, brings the dependencies in the task lines in step with the plan when the plan's dependencies change, and after the human has accepted a complete task document, one document at a time, changes that document's Status line and moves the task's line to ready, making it already ready where none stands. Agent turns, questions and explicit waits keep the plan task to refine, a presented human package or ready for approval makes it waiting for human, and final acceptance makes both document and plan ready for cycle and removes only that conversation after all settled answers, their sources and the ways not chosen survive in the task document; an explicit wait is logged and its task is proposed again when the named prerequisite is done.

- **Scope:** project-level

### WAY-155 — What may the answering agent settle during a refinement round?

The answering agent answers a refinement question only with a quotation and source from the definition, plan, foundation or other task documents, or with a factual code observation naming file and line; a question about how the product is to be is answered only from a document, never from code or the agent's inference. It reads the round's conversations, makes an unanswered choice a question of decision to the human, as WAY-113 gives it, and brings the same question to the human once while preserving its affected tasks; in the area of the choices a refinement round leaves unanswered, this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation. The project orchestrator presents one round package of these questions, candidate settlements, placement of Human actions and complete wording, together with every quotation answer as question, quotation and source; a quotation answer the human strikes becomes a question to the human, whose answers return to the conversations before fresh refiner turns.

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

The refining agent shows the human only the matters that the second agent of WAY-377 leaves truly open and the gaps of the document itself, at most about four, the most consequential first, each in plain language as WAY-113 asks a decision; the full list and the critique stay in a file in the ignored `.runs/` directory of the product, whose path the agent gives the human. Before it shows a matter, and before it keeps a guess from the human on the critique's verdict that the repository or the task document already settles it or that it is most likely right, it checks the quotations behind that verdict and gives the matter one explicit verdict (WAY-120), and where no matter is open it says nothing of the step.

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

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest that the cycle's session lets its agents use, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class available that fails, or a retry that fails, stops the cycle.

The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every other reviewer work on no class cheaper than the orchestrator's, and the review of the whole change and the review of the return step work on the strongest class available.

- **Scope:** task-cycle

### WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?

The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason. A decision of the-way on what such a template carries or what such a skill proposes binds the template and the skill, never a product's screens or code directly.

- **Scope:** product-guidelines

### WAY-172 — How is a new or changed meaning of a product's guidelines approved?

A new or changed meaning of a product's guidelines that carries a choice with a real cost is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as WAY-30 has a change to a decision approved, or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision. A new or changed rule that only says how to write code, tests or the look of the product, with no decision, is accepted by the human as a row of the task's table of settlements before the code that uses it, or, where the cycle found the rule itself, at the merge from the request's description, and a rule of a template of the-way binds a product only through a decision of its log that adopts it (WAY-173). Using a meaning that a decision of the product's log already carries takes no approval, and neither does changing a value that keeps its meaning; in the area of new and changed meanings of a product's guidelines that carry a choice with a real cost, this decision prevails over WAY-114, under which an agent writes such an entry on its own recommendation for the human to accept at the merge.

- **Scope:** product-guidelines, decisions, project-level, task-cycle

## Listed by heading alone

- WAY-09 — What may enter the process repository?
- WAY-27 — Where may this repository point for its reasoning?
- WAY-28 — How does the process enter a product that already exists?
- WAY-34 — Which version of the process does a product use?
- WAY-100 — When does a method or practice borrowed from elsewhere bind a product?
- WAY-101 — Who chooses the backlog tool used with the-way?
- WAY-102 — What is the-way for?
- WAY-103 — Who is the-way for?
- WAY-107 — Where does a product tell the project level where its backlog stands?
- WAY-01 — What state does the foundation describe?
- WAY-02 — How does whatever depends on an entry refer to it?
- WAY-04 — What makes up a product's foundation?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-14 — Who accepts a decision?
- WAY-24 — How is a decision that rests on a prediction reviewed?
- WAY-25 — What settles a collision between two decisions?
- WAY-30 — What happens when a change contradicts a decision?
- WAY-313 — What is a decision of the foundation to the refinement of a project or a task?
- WAY-314 — Which act of the human consents to a change of a decision that refinement shows?
- WAY-315 — From when does a decision of the foundation bind the work on a task?
- WAY-35 — What does an element's skill hold?
- WAY-113 — How does an agent of the-way ask a human decision?
- WAY-120 — How does the-way critique an agent's proposal?
- WAY-150 — How do the-way skills choose which product foundation material to read?
- WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?
- WAY-82 — How does an environment fact keep up with what its source says?
- WAY-84 — How is a setting that people of the product change outside its repository written?
- WAY-85 — How is a finding of a study written as an environment fact?
- WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?
- WAY-95 — Which words take a glossary entry?
- WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?
- WAY-99 — How does one word keep one meaning in the foundation?
- WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?
- WAY-44 — What assigns a file to a part?
- WAY-48 — How is a trust boundary recorded?
- WAY-52 — What is generated from the part map for an agent?
- WAY-53 — How is a derived file compared with what its generator produces?
- WAY-225 — What in a product's foundation is derived rather than written by hand?
- WAY-127 — How does a session working on the-way itself reach the-way's skills?
- WAY-256 — Where does a fragment of a skill stand?
- WAY-265 — Where is the file of a variant named, when a step's file points to it?
- WAY-368 — Which agents run the stages of a task cycle in Claude Code?
- WAY-370 — What does a task cycle do where the session has none of the-way's agent types?
- WAY-106 — What does the project level write before tasks exist?
- WAY-118 — What makes a project definition ready for breakdown?
- WAY-126 — How does a projected entry enter the foundation?
- WAY-145 — Who sets where an open question of an approved project definition is resolved?
- WAY-121 — Where does a project settle the technology it needs?
- WAY-122 — How are the options of a technology choice found and checked before a human sees them?
- WAY-123 — How does a technology choice reach a human who cannot assess the technology?
- WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?
- WAY-138 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?
- WAY-267 — How does the step that settles technology run outside a project definition?
- WAY-268 — Who settles a technology choice that no decision or definition settles?
- WAY-269 — How does a task leave a cycle that met a reserved choice, and how does it come back?
- WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?
- WAY-165 — What must an answer to each matter of an agent's way to the running product settle?
- WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?
- WAY-273 — May a product hide a failure?
- WAY-274 — Where does a product's logging scope stand, and who adds to it?
- WAY-276 — What do a product's logs not hold?
- WAY-319 — What must an agent's way to the running product allow when two task cycles run at once?
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
- WAY-10 — Who assesses a change to an invariant test or to the foundation?
- WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?
- WAY-162 — How does a code review of a task's change end when its findings block?
- WAY-263 — Which foundation mismatches are Important findings?
- WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?
- WAY-363 — How does a reviewer grade a finding about the structure of code?
- WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?
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
- WAY-337 — How is the cost of a cycle measured?
- WAY-339 — When do the measures of the audit stop being comparable?
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
- WAY-167 — Where do a product's guidelines stand, and what are their files named?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-212 — How does a product's instruction file lead to its coding guidelines?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-312 — Which sentences does a rule of a product's guidelines not hold?
- WAY-174 — How do the-way's skills of guidelines ask the human?
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
- WAY-379 — Does the-way adopt the template of the coding discipline for its own code?
- WAY-380 — Which linter checks the-way's code, and which of its rules block a change?
- WAY-382 — Does the-way's code get an automatic formatter?
- WAY-383 — Does the-way's code get an audit of its dependencies?
- WAY-384 — Does the-way adopt the six rules of the coding template on failures and logs?
- WAY-385 — How large may a function and a file of a script of the-way be?
- WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?
- WAY-387 — Which file is the exemplar of the kind `measuring-report` in the-way's code?
- WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?
- WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-397 — Which test is the exemplar of the level files test of the-way's tests?
- WAY-398 — Which test is the exemplar of the level git test of the-way's tests?
- WAY-399 — Which test is the exemplar of the level repository test of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
