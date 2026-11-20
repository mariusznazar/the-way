# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 12. Listed by heading alone: 97.

## Listed in full

### WAY-02 — How does whatever depends on an entry refer to it?

Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to it by that identifier alone, with no fingerprint and no version beside it, and names an entry the foundation holds. A fingerprint, where the process records one, is the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of a text encoded in UTF-8, taken after every run of spaces and line breaks is replaced by a single space and both ends are trimmed; nothing else in the text is changed before it is digested. The one reference that carries more than the identifier is the line `decision:` of a test that holds a sentence of a decision: it gives the number and, in straight double quotation marks, the start of that sentence — from where a sentence of the entry begins, three words or more, compared after every run of spaces and line breaks is replaced by a single space — so that a test whose sentence was reworded is found, while a reference anywhere else names a decision by its number alone.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, product-guidelines

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

### WAY-385 — How large may a function and a file of a script of the-way be?

A function of a script of the-way has at most 110 lines, counted with the functions nested in it, and a file of a script has at most 1200 lines, in each part that WAY-379 names, both counted on the code as the formatter of WAY-382 leaves it; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception. A test of the suite counts the lines with the `ast` module of the standard library, runs apart from the run of the linter and, where it fails, names every function and file over a threshold with its size (WAY-361).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

## Listed by heading alone

- WAY-09 — What may enter the process repository?
- WAY-27 — Where may this repository point for its reasoning?
- WAY-28 — How does the process enter a product that already exists?
- WAY-34 — Which version of the process does a product use?
- WAY-100 — When does a method or practice borrowed from elsewhere bind a product?
- WAY-101 — Who chooses the backlog tool used with the-way?
- WAY-102 — What is the-way for?
- WAY-103 — Who is the-way for?
- WAY-01 — What state does the foundation describe?
- WAY-04 — What makes up a product's foundation?
- WAY-07 — How is a foundation entry changed?
- WAY-17 — Which links between foundation entries are mandatory?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-14 — Who accepts a decision?
- WAY-24 — How is a decision that rests on a prediction reviewed?
- WAY-25 — What settles a collision between two decisions?
- WAY-30 — What happens when a change contradicts a decision?
- WAY-114 — What does a human accept of an entry, and when?
- WAY-313 — What is a decision of the foundation to the refinement of a project or a task?
- WAY-314 — Which act of the human consents to a change of a decision that refinement shows?
- WAY-315 — From when does a decision of the foundation bind the work on a task?
- WAY-33 — What does the author of a foundation change search for?
- WAY-35 — What does an element's skill hold?
- WAY-113 — How does an agent of the-way ask a human decision?
- WAY-120 — How does the-way critique an agent's proposal?
- WAY-150 — How do the-way skills choose which product foundation material to read?
- WAY-03 — Who may change an invariant test, and when?
- WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?
- WAY-61 — How is an invariant's method of checking written?
- WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?
- WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?
- WAY-84 — How is a setting that people of the product change outside its repository written?
- WAY-85 — How is a finding of a study written as an environment fact?
- WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?
- WAY-95 — Which words take a glossary entry?
- WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?
- WAY-99 — How does one word keep one meaning in the foundation?
- WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?
- WAY-44 — What assigns a file to a part?
- WAY-52 — What is generated from the part map for an agent?
- WAY-53 — How is a derived file compared with what its generator produces?
- WAY-225 — What in a product's foundation is derived rather than written by hand?
- WAY-16 — How are the checks of invariants run?
- WAY-38 — In what are the scripts of the-way written?
- WAY-55 — Which part of the process holds the gate?
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?
- WAY-128 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand?
- WAY-129 — How does an instruction file point an agent to another file?
- WAY-130 — When does a rule enter an instruction file, and when does it leave?
- WAY-131 — How is it settled whether a rule of an instruction file works?
- WAY-132 — Which file carries the instructions Claude Code, Codex and Cursor share?
- WAY-133 — How is a rule of an instruction file kept when it has to hold every time?
- WAY-127 — How does a session working on the-way itself reach the-way's skills?
- WAY-256 — Where does a fragment of a skill stand?
- WAY-265 — Where is the file of a variant named, when a step's file points to it?
- WAY-368 — Which agents run the stages of a task cycle in Claude Code?
- WAY-126 — How does a projected entry enter the foundation?
- WAY-121 — Where does a project settle the technology it needs?
- WAY-122 — How are the options of a technology choice found and checked before a human sees them?
- WAY-123 — How does a technology choice reach a human who cannot assess the technology?
- WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?
- WAY-138 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?
- WAY-267 — How does the step that settles technology run outside a project definition?
- WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?
- WAY-165 — What must an answer to each matter of an agent's way to the running product settle?
- WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?
- WAY-134 — How does a task carry what its refinement settles for the foundation?
- WAY-11 — How does a task end?
- WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?
- WAY-10 — Who assesses a change to an invariant test or to the foundation?
- WAY-287 — What does a request put before the human for a decision?
- WAY-288 — In what language is a request's description written?
- WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?
- WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?
- WAY-309 — How does the cycle find the private paths and notes in what it publishes?
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
- WAY-174 — How do the-way's skills of guidelines ask the human?
- WAY-379 — Does the-way adopt the template of the coding discipline for its own code?
- WAY-380 — Which linter checks the-way's code, and which of its rules block a change?
- WAY-381 — How is the version of the linter pinned and installed?
- WAY-382 — Does the-way's code get an automatic formatter?
- WAY-383 — Does the-way's code get an audit of its dependencies?
- WAY-384 — Does the-way adopt the six rules of the coding template on failures and logs?
- WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?
- WAY-388 — Which file is the exemplar of the kind `generator` in the-way's code?
- WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-399 — Which test is the exemplar of the level repository test of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
