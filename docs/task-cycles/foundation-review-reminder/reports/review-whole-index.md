# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 58. Listed by heading alone: 79.

## Listed in full

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/` and the copies of the cycle's agent type definitions under `.claude/agents/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; any other directory what the sentence of its part in the part map names. The entries in `foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, foundation-review, process-audit, task-cycle

### WAY-27 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks and the rules of that place, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else, each by an entry of the locations file of WAY-320 and never by a path.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, installation, agent-instructions, instruction-files, product-guidelines, task-cycle

### WAY-28 — How does the process enter a product that already exists?

When the process enters a product that already exists, the existing state is its starting point and needs no justification, and the rules apply to changes from then on. The part map comes first; the invariants of the critical flows, each naming in *Part* the parts its flow runs through, are then recovered from what the product does — an agent lists what a part does, and a human chooses which of it the product must keep — and the other invariants come through the return step of tasks. Decisions are recovered only when a task touches the parts they govern.

- **Scope:** decisions, invariants, glossary, part-map, task-cycle

### WAY-34 — Which version of the process does a product use?

A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit. A newer version of the process enters a product only in one commit of the product that moves the pin, made when a task of the product needs a change of the process, as the first commit of that task's branch, under which the task's whole cycle works, or in a step of its own that takes several changes of the-way at once.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, installation, instruction-files, task-cycle

### WAY-100 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.

A decision that adopts a method or practice from outside names the practice and what it takes from it, in its binding sentences or its *Rationale*; names the source in *Based on*, or, for a source a reader of the repository cannot open, describes in *Rationale* what was seen there (WAY-27); and puts what it leaves out of the practice in *Rejected*. A list of what is taken from one source is no decision: each rule taken stands in the decision that carries it (WAY-19).

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-101 — Who chooses the backlog tool used with the-way?

The-way's task cycle requires no particular backlog application or service; each product chooses where it keeps its roadmap, projects and tasks.

- **Scope:** elements-common, project-level, task-cycle

### WAY-102 — What is the-way for?

The-way is a process for work on a technology product in which a change of premises or direction is an ordinary step: it passes through the product's foundation and needs no memory of what is linked to what.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-103 — Who is the-way for?

The-way is built first for its author and aims at anyone who builds a technology product and adopts the process for their own needs; the process is written for the agents that carry out the task cycle too.

- **Scope:** decisions, elements-common, task-cycle

### WAY-107 — Where does a product tell the project level where its backlog stands?

A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns, a place on the user's disk outside every repository standing there as an entry of the locations file of WAY-320, never as a path, and a directory of the repository or the address of a public tracker as it is. A project definition stands in the named project place; when the place is unnamed, or the file or the entry it names is missing, the agent asks the human and offers to record the answer where it fits: the entry in the file for a place on the user's disk, the section otherwise. How a task's line is handled — the status of a new line, its move to ready, the form of its dependencies and of its identifier, how a line is found and kept one to a task, which fields an agent may change, the agreement of the lines at both ends of a dependency, a clash of identifiers — is taken from the rules of the task place itself, never from text written at the product or in the-way's skills; the section names, beside the place of the tasks, the entry `task-rules` of the locations file under the product's name, whose value is the path of those rules, and where that entry or the file it names is missing, the agent asks the human once and offers to add the entry, as for a missing place.

- **Scope:** project-level, installation, foundation-review, product-guidelines

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

### WAY-14 — Who accepts a decision?

A decision, and every change to it, binds once a human accepts it, never an agent. In the-way, that human is Mariusz.

- **Scope:** decisions

### WAY-24 — How is a decision that rests on a prediction reviewed?

A decision names no date or condition for its review and the log holds no record of a review. The review of the foundation against the product is a run of the skill `review-foundation`, which a human starts in a session with an agent when the reminder of a request asks for it (WAY-300) or at any other time. A task of the product's backlog may stand for that run, and a human adds it, never a cycle.

- **Scope:** decisions, foundation-review

### WAY-25 — What settles a collision between two decisions?

Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a chain, and two decisions that narrow each other are an error. A collision between two decisions with no precedence recorded is never settled silently by the agent that meets it. Where what the human accepted gives the outcome and the change may write the decision that prevails, the change records the precedence in that decision, and its request names it with the passages of what the human accepted that give the outcome, for the human to accept at the merge (WAY-114); otherwise the agent stops and asks.

- **Scope:** decisions, task-cycle

### WAY-30 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made; that approval, including a change carried by a row of *Settlements to record*, answers the question WAY-114 requires, so the agent writing the entry asks only about a meaning beyond what the approved plan or task document carries, and in this area this decision prevails over WAY-114. When a contradiction shows only during implementation, the agent stops, quotes the decision by its number, and either brings the change into line, drops the change, or proposes on the task branch an edit of the decision, a new wording or a narrowing, and the code that needs it waits for that human. An exception written in advance into a decision's binding sentences is not a contradiction, and no exception lives only in a task document, plan or cycle record.

- **Scope:** decisions, task-cycle

### WAY-114 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a projected entry at the readiness gate, shown as one sentence in the human's language with the entry beside it; that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement; and that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier, repeated in the human's language in the description's collapsed block, while the full list of the change's entries, each by its identifier with one English sentence of its meaning, stands in the description's lower part. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, task-cycle

### WAY-313 — What is a decision of the foundation to the refinement of a project or a task?

While a project definition or a task document is refined, the technology step included, a decision of the foundation describes what the product does today and is material for revision, not a limit on the options: refinement shows an option that changes a decision as it shows any other, with the decision it changes named by its identifier, and may recommend it, asking no leave to open the decision first. This holds only before the cycle starts (WAY-315). A projected decision of an approved definition is no such material: a change of it goes through the definition and its readiness gate (WAY-118).

- **Scope:** project-level, elements-common, decisions

### WAY-314 — Which act of the human consents to a change of a decision that refinement shows?

Where refinement shows an option that changes a decision of the foundation (WAY-313), the option says in its line which decision it changes, and the human's choice of that option is the human's consent to the change (WAY-14); the acceptance of the complete task document, or the approval of the projected entries at the readiness gate of a definition, asks nothing about that change a second time. A task document carries the change and its cycle writes it with the code that needs it (WAY-30), and a definition carries it as a projected change of the decision.

- **Scope:** project-level, elements-common, decisions

### WAY-315 — From when does a decision of the foundation bind the work on a task?

A decision of the foundation binds the work on a task from the start of the task's cycle, the writing of a spec in the cycle included. In the cycle no agent departs from a decision on its own and returns with the question, as WAY-30 gives, and the looser rules that refinement follows for decisions (WAY-313, WAY-314), for the rows of its settlements (WAY-134) and for the question against an answer (WAY-113) hold only before that point.

- **Scope:** task-cycle, project-level, decisions

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.

- **Scope:** invariants, agent-instructions, task-cycle, gate

### WAY-38 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.

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

The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it.

- **Scope:** task-cycle

### WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?

The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under the shared reading of product guidelines: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither. The *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds that part to this decision's *Scope*. A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task. For the human actions placed in the cycle, the cycle does what the repository allows and opens a blocked draft request listing them, and the human performs them at the request; a human action the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle. The human places each human action the task document names while the task is refined, on the agent's proposal: before the cycle when the cycle's code needs its effect, such as an account, a key or a database, and in the cycle when it uses code the cycle writes, such as a deployment or a DNS record pointing to a new address.

- **Scope:** project-level, task-cycle

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

### WAY-227 — Where does the human meet a task cycle's work?

The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under the task owner's delegation, never recording these as human approval, and brings the request to the human, the cycle's first point of human review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request.

- **Scope:** task-cycle

### WAY-287 — What does a request put before the human for a decision?

The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks not run, the incomplete reading of the review of the whole change where its reviewer did not read the index of its whole selection or itself named a decision concerning the change as unread, and the gap was not closed on the way by that reviewer, or a fresh one, reading what stayed unread, the unfixed findings the product's user or the human working with the process will feel, the decisions of the task's own sections, in a blocked request what the cycle needs to go on, the human actions, the changed invariant tests, surfaces and *Violated* marks, the additions a change makes to a product's logging scope, a listing of the remarks check that the cycle holds wrong (WAY-295), an error of the form check that the cycle holds wrong, the pairs that give the cause of a correction after the request opened, each descriptive `TODO` in an invariant's *Rests on* or *Derives from* or in a decision's *Based on* that stands on the main branch after the change (WAY-71), and the foundation entries the human did not see at the task document — in three groups, headed *Needed from you*, *Fix or let through* and *You accept by merging*, in this order: what the request cannot go on without, an answer or an action of the human; what the cycle did not do or did not fix and can still be done in this request, which the human has done there, makes a task of or lets through; and what the cycle did within its authority, which the human accepts by merging and which waits for no separate answer. Every group stands, reading `none` where it holds no item, the items are numbered in one run through the three groups, and the section reads `none` alone where no group holds an item, which says that nothing else in the request waits for the human's yes. A blocked request keeps the same skeleton, with `blocked` in its first sentence and what the cycle needs, in plain words, and the stages it did not run because it stopped, under *Needed from you*, while each remaining finding stands with its place in the code in the lower part.

- **Scope:** task-cycle, agent-instructions

### WAY-288 — In what language is a request's description written?

A request's description is written in English, and its top part stands a second time, in the language of the task document, in a collapsed block of the description.

Where the task document of a request is in English, the collapsed block of the request's description holds `none` in place of a second English copy of the top part, and the form check, wherever it reads the task document as English, holds the block to `none`.

- **Scope:** task-cycle, agent-instructions

### WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?

Writing a request's description, the orchestrator of the cycle judges each unfixed finding — a Minor finding that no fix made, a finding outside the task's scope and the new Critical or Important finding of a fix that WAY-162 reverted — from the whole cycle record, the reports of the walk through the running product and its screenshots included, by whether the product's user or the human working with the process will feel it, and restates each that will be felt, in plain words, in the section for the human's decisions, under *Fix or let through*, as one question with the answers to fix it in this request, to make a task of it or to let it through, which one answer may settle for the whole list. The answer to fix it runs a correction with one fix and one review of that fix; the same answer is offered for a step or a check the cycle skipped, a proposal of the task's own sections not applied and an incomplete reading of the review of the whole change, and runs the step or the check, applies the proposal or has a fresh reviewer read what stayed unread, and what the correction leaves unfixed or undone, like whatever cannot be done in the request at all, is put by the request only with the question whether it becomes a task, which the human who makes none lets through by merging, or stays in the lower part, so that the loop ends after one correction. Every finding stays in its list of the lower part with the reviewer's words and its place in the code, and the judgment changes no finding's kind or grade and decides no fix and no block.

- **Scope:** task-cycle, agent-instructions

### WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?

Before every commit that adds the cycle record to the product's repository, the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports — the `.md` files of the cycle's `reports/` directory whose name holds neither `handoff` nor `findings` — that the record's process remarks do not hold word for word, appends each listed item word for word with its stage name and full report path, and runs the script again until it lists nothing. The commits that add the record are its copy for a request, the repetition of that copy in a correction after review, and the copy of a request blocked for any cause. The script only lists, and an item that two reports give is listed again until the remarks hold it twice; a report without the section gives no item and does not end the script with an error, which narrows WAY-344 for the reports this script reads.

- **Scope:** task-cycle

### WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong?

Where the orchestrator of a cycle holds a listing of the remarks check of WAY-294 to be an error of the script, with evidence it can name, the record is archived all the same and the script is not changed in that cycle: the orchestrator enters the case in the record's process remarks as a case of the script, not as an item of its stage, and names it in the request's section for the human's decisions. In that case the repeated run of WAY-294 does not hold the archive back.

- **Scope:** task-cycle

### WAY-300 — When does a request tell the human that the foundation waits for a review?

At the end of every task cycle the orchestrator counts the merges to the main branch since the last review tag, and from the threshold of the reminder script on, the description of each request the cycle writes says, in its part for the human who merges, that the foundation waits for a review. The reminder blocks nothing, the threshold is one number for every product, which no product sets for itself, and a repository with no review tag counts from the start of its history.

From the threshold on, the orchestrator reads the product's backlog for an open line of the review of this repository — a line whose name holds the name of the skill `review-foundation` and the name of the repository, open as the rules of the task place say (WAY-107). Where no such line stands, or the backlog cannot be read, the sentence asks the human to add the task of the review and gives what its name holds, the number of merges, the tag of the last review and the skill that starts the review; where the line stands, the sentence points to it and does not urge. The cycle adds and changes no line of the backlog (WAY-140).

- **Scope:** task-cycle, foundation-review

### WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?

Where a change alters what a screen shows, the screenshots that its author or reviewer shows the human are embedded as images in the description of the request, from a place that the foundation of the product settles outside the product's repository; the-way names no place. No file of a screenshot is committed to the product's repository, the copy of the task cycle's record that a commit adds to it included. A screenshot is evidence for the time of acceptance: the product may clear its place after a long time, and the images of old requests then stop showing.

Where a change alters what a screen shows and the foundation of the product settles no place for screenshots, the author inspects the screenshot as the author's check of a user-interface change gives and the request shows none: the section of its description for the human's decisions says that no screenshot is shown and why, and the cycle does not stop. A screenshot left unchecked for want of a settled way to the running product is reported as that check gives and needs no second item.

- **Scope:** task-cycle, project-level

## Listed by heading alone

- WAY-01 — What state does the foundation describe?
- WAY-02 — How does whatever depends on an entry refer to it?
- WAY-04 — What makes up a product's foundation?
- WAY-07 — How is a foundation entry changed?
- WAY-17 — Which links between foundation entries are mandatory?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-33 — What does the author of a foundation change search for?
- WAY-35 — What does an element's skill hold?
- WAY-113 — How does an agent of the-way ask a human decision?
- WAY-120 — How does the-way critique an agent's proposal?
- WAY-150 — How do the-way skills choose which product foundation material to read?
- WAY-03 — Who may change an invariant test, and when?
- WAY-51 — What does the main branch hold where the product does not meet an invariant?
- WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?
- WAY-61 — How is an invariant's method of checking written?
- WAY-62 — What does an invariant entry name in the part map?
- WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?
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
- WAY-126 — How does a projected entry enter the foundation?
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
- WAY-319 — What must an agent's way to the running product allow when two task cycles run at once?
- WAY-144 — How does a project plan show which tasks can be worked on side by side?
- WAY-147 — How is a task of a project plan named, and what does its cycle take from the name?
- WAY-124 — When is a task ready for its cycle?
- WAY-134 — How does a task carry what its refinement settles for the foundation?
- WAY-355 — Which task fixes a defect found after a merge?
- WAY-164 — What does the author of a change check of its own work before review?
- WAY-255 — How does an agent of a task's cycle wait for a command that runs long?
- WAY-260 — What does each task-cycle stage report about what it could not find or understand?
- WAY-261 — What does a task cycle report about a check that fails and passes when run again?
- WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?
- WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?
- WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?
- WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?
- WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?
- WAY-309 — How does the cycle find the private paths and notes in what it publishes?
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?
- WAY-324 — How does a product check the files it tracks for private paths and notes?
- WAY-337 — How is the cost of a cycle measured?
- WAY-339 — When do the measures of the audit stop being comparable?
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
- WAY-174 — How do the-way's skills of guidelines ask the human?
- WAY-361 — How does the review of a change get the sizes of functions and files from a product?
- WAY-238 — At which level does a test stand, and who chooses it?
- WAY-253 — Who runs a mutation tool in a task's cycle, and what does the author check in its place?
- WAY-254 — Where does the command of a mutation tool stand?
