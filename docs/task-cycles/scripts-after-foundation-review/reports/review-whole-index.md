# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 58. Listed by heading alone: 139.

## Listed in full

### WAY-07 — How is a foundation entry changed?

A foundation entry of any element carries no version: it is edited in place, on the main branch as before it, and holds only its current wording; the decision log has one entry for each number, and git keeps the earlier wordings.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

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

### WAY-93 — Where do glossary entries stand, and what identifies one?

Glossary entries stand in one file, `foundations/glossary.md`, each under its term as the foundation writes it in running text, which no other entry there holds. The file opens with a title and a paragraph saying what it holds, and holds no other heading than its entries.

- **Scope:** glossary

### WAY-94 — What does a glossary entry hold, and what is its binding part?

A glossary entry holds one definition of its term and one field, *Not*: each meaning the word carries or carried in the files git tracks, besides its definition and a meaning a reader who knows the product's field gives it, with what carries it. The definition is the binding part.

- **Scope:** glossary

### WAY-95 — Which words take a glossary entry?

A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean; a word the product uses more narrowly than the field takes an entry only where a reader who takes the field's meaning would read a sentence of the product's English files wrongly. An agent that meets such a word in its work — writing an entry, searching the foundation, in a task's return step — writes its entry, no sweep of every binding sentence looks for candidates, and a human accepts the meaning (WAY-114).

- **Scope:** glossary, decisions, invariants, part-map, environment-facts

### WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?

A sentence relies on a glossary term by using its word. A glossary entry is edited in place, its meaning included, and the author of a change to a definition searches, in the same change, the English text of every file git tracks for the word and rewrites each use whose meaning the new definition moves; a text in another language is not searched (WAY-99).

- **Scope:** glossary, decisions, invariants, part-map, environment-facts, elements-common

### WAY-99 — How does one word keep one meaning in the foundation?

Two uses of a word in the English text of the files git tracks carry two meanings when a sentence those files hold is true in the meaning of one use and false in the meaning of the other, whichever of the two the sentence uses, and a sentence made up for the test does not count; where one of the two meanings is a meaning a reader who knows the product's field would not give the word, one of the two is renamed, and the glossary entry of the word names in *Not* each such meaning it no longer carries, with the term, identifier, closed-list value or quoted word — holding neither the term nor its forms — that carries it now. A meaning whose word a human has not yet chosen reads `TODO` in *Not*, which a task branch may hold and the main branch never does. A file of a product in another language uses its words in the meaning they have in that language, and the rules of the glossary do not reach it.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts

### WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?

A word that the glossary of the-way holds at the commit a product pins, or the last word of a term it holds, in any of its forms, takes a qualifier — a phrase holding the word — in a sentence of the files of the product's `foundations/` that could otherwise be read in the other meaning: a sentence that uses the word for the product's domain and could be read as the process's, or one that uses it for the process and could be read as the domain's, and a bare use that no sentence of those files reads in the other meaning keeps the meaning it has there. A qualified word takes a glossary entry only where WAY-95 gives a word one, and where the bare word itself has an entry in the glossary of the-way, that entry records no *Not* for its domain meaning. The product's code, its interface and talk about the product use the word of the domain unchanged.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts

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

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*. The same command, where a table of weights or a table of the costs of an occurrence in the register of problems lacks one of its levels, writes its result, gives the values that depend on the table as unknown and ends with exit code 1 and a line `Error:` that names the missing level; where a stage report has neither of the two columns of the cache writes in its detailed section, it reads the report as an earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and priced as input, an approximation, and no value unknown for the missing columns, while a stage report that has one of the two columns and not the other has a missing field, with the line `Error:`; and where the locations file has no entry `repository` under `the-way`, no field is missing and the command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-368 — Which agents run the stages of a task cycle in Claude Code?

In Claude Code, a task cycle dispatches the one author of a change without a plan as an agent of the type `the-way-author` and every other stage agent as an agent of the type `the-way-stage`, two types of the-way's own that give their agent every tool of the session except the skill tool. Each type has a body of its own saying what it is, and only the type of the one author has the prompt cache lifetime that WAY-255 gives that agent. A stage agent reaches each method, and each skill a method names, as a file by its path, never by calling a skill; the installer writes the definitions of the pinned commit into a product, replacing and deleting only its own files, and the copies a session on the-way itself loads are generated from them and tracked.

The agent types of a task cycle start with the instruction files that Claude Code loads into an agent of the session, the user's and the product's; no definition of a type sets the field that starts an agent without them.

- **Scope:** task-cycle, installation, agent-instructions

### WAY-164 — What does the author of a change check of its own work before review?

Before its work goes to review, the author of a one-author change names the requirement of the task, and the executor of each slice the requirement of its slice read against the passages of the task its handoff gives, that its work most likely does not meet, writes a check that would catch that, and states in its report which requirement, which check and what the check showed. The review that judges the work — a slice's own review where it has one, otherwise the review of the whole change — reads that report, and the request lists what each such check showed among its test evidence.

- **Scope:** task-cycle

### WAY-255 — How does an agent of a task's cycle wait for a command that runs long?

An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps its prompt cache — a container build, a mutation run, a test suite a check names — by running it in the background and reading its output between waits each shorter than that lifetime, never in one wait past it; in Claude Code a subagent's cache lives five minutes by default, so each wait stays under about four. The one author's cache lives an hour, which the author's type sets (WAY-368), and its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits. Where the harness states no cache lifetime, the agent waits as the harness allows.

- **Scope:** task-cycle

### WAY-260 — What does each task-cycle stage report about what it could not find or understand?

Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each reach beyond the dispatch. The orchestrator copies every such item other than `none` word for word, with the stage name and full report path, into the cycle record's *Process remarks on the-way*, without combining repeated items.

- **Scope:** task-cycle

### WAY-261 — What does a task cycle report about a check that fails and passes when run again?

Each failing run of a check remains in the cycle record with its command and result, even if the check later passes. When a check has both a failing and a passing run during the cycle, the request lists it under *Checks* as failed, with the result of its rerun and the number of cycle runs in which it failed and passed; when preparing the request, the orchestrator recovers the task's parts from the frozen task and its changed files using the part map, and lists the check beside findings outside the task's scope when its file belongs to a different part. This applies in every product, whether or not its testing guidelines name flaky tests.

The red result of the first run of the gate on the final tree stays the result of the gate, also where the check that failed is one outside the task's scope that passes when run again; the cycle does not stop for it, and the request names that check and the task that fixes it, or proposes that task where none exists.

- **Scope:** task-cycle

### WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?

Where a slice of a plan adds to a function or a file that stands over the threshold of the product's rule of size, the plan begins with a slice that moves a part of that function or file out without a change of behaviour, writes the choice in its table of choices, and puts the slice that adds after it. The author of a change without a plan makes that move the first commit that changes the code. Such an addition is a choice of how to make the change and no open design choice, so it gets no spec (WAY-135).

- **Scope:** task-cycle

### WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?

An agent of a task cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own under the ignored `.runs/` directory of the task's worktree, never in the system's temporary directory, in a session's scratch directory or in the main checkout of the repository. Before it returns, the agent removes its copy, keeps in the cycle's reports what its report needs and states in the report where the copy stood and that it was removed; where a removal fails, the agent finishes and names the remainder with its path in the report, and the cycle carries it to its record and to the description of the request, where the human sees it, and goes on. The same holds for the separate checkouts that the orchestrator makes, while the files that a product's own tools and tests make by themselves are no working copy of the agent and stand outside it.

- **Scope:** task-cycle

### WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?

At the start of a new cycle the cycle runs a script of the-way that removes the working directory of an earlier task only where all of these hold at once: its tree is clean as git's own check for removing a checkout reads it (WAY-376), every commit of it is on the remote, its branch is merged, and it belongs to a cycle, standing on a branch whose name begins with `task/` or whose directory holds the record of a cycle, or being a detached copy of a base made for a check. A branch is merged where its tip is the second parent of a merge commit on the first-parent history of the remote target branch, which git alone shows, so that a branch merged by squash or rebase, a branch that stands at the target's tip with no commit of its own and a branch of a request closed unmerged are not merged. A directory of a cycle that the script does not remove stays, with its reason, for the human to decide, a copy of a base standing alone that the script does not assign to a task — one named for no task, or for a branch it does not find — among them, and a detached checkout nested in a directory that is removed goes with it, whatever its name, only where it is clean and on the remote, else the directory that holds it stays.

The script touches only the checkouts that `git worktree list` names for the repository, never the main checkout, the directory it is run in or a detached directory outside the cycle's, and it removes directories only, never a branch, local or remote. Removing a checkout that git names, also one that stands outside the repository's own directory, is a change to the repository's state and no effect outside the repository in the sense of WAY-140, so the script that a cycle runs needs no act of a human. In removing a cycle's own directories whose branches are merged this decision prevails over WAY-13, which keeps its reach over every other operation that cannot be undone.

- **Scope:** task-cycle

### WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?

A file that git ignores does not count against a clean tree, so the script of WAY-375 removes a directory that holds ignored files, and they end with it. For each directory the script marks for removal it lists the paths git ignores in it outside the cycle's `.runs/` directory, leaving out the caches a command makes again, so that a human who runs the script without `--apply` sees what would end with each directory; the cycle's own run, which removes with `--apply`, waits for no one to read the list.

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

### WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?

Before every commit that adds the cycle record to the product's repository, the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports — the `.md` files of the cycle's `reports/` directory whose name holds neither `handoff` nor `findings` — that the record's process remarks do not hold word for word, appends each listed item word for word with its stage name and full report path, and runs the script again until it lists nothing. The commits that add the record are its copy for a request, the repetition of that copy in a correction after review, and the copy of a request blocked for any cause. The script only lists, and an item that two reports give is listed again until the remarks hold it twice; a report without the section gives no item and does not end the script with an error, which narrows WAY-344 for the reports this script reads.

- **Scope:** task-cycle

### WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?

A task cycle commits its record and publishes the description of its request only cleaned, in every repository, public or private: each absolute path becomes a path relative to the repository (a place outside the repository, a description of what the place is), and the path or the title of a private note becomes a description of what the note is. The line `Task relation:` of the record and the line `Project relation:` of the copy of the task document stay as they are unless the check of WAY-309 lists them; a line it lists is cleaned like any other, and the request tells the human, since the reader of a plan's state may then report a conflict. The cleaning comes before each commit that adds the record — its copy for a request, the repetition of that copy in a correction after review and the copy of a request blocked for any cause — and before each publication of the description, the first and every later edit; the messages of the commits are not cleaned.

- **Scope:** task-cycle, agent-instructions, project-level

### WAY-309 — How does the cycle find the private paths and notes in what it publishes?

Before each commit that adds the record, on its cleaned copy, and before each publication of a request's description, the first and every later edit, the one that adds the link to the record included, the block in the language of the task document among its text, the orchestrator runs the-way's script that lists, with the file and the line of each, every absolute path (a drive letter, a home directory) and every note link written `[[...]]`, and corrects what it lists until it lists nothing. The script finds them by pattern, holds no list of private words and rewrites nothing. The check of WAY-294 runs on the original before the copy is made, the cleaning is one rewriting of every text file of the copy, and the check runs once more on the cleaned copy, where an item it lists is made to read the same in the report and in the remarks, not appended again.

The script takes no `[[...]]` for a note link when its first bracket stands against a letter, a digit, a dot or an underscore on its left, when it is a character class of the shell in double brackets, `[[:space:]]`, with one of the twelve POSIX names between the colons (`alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`), and no letter for the start of a drive when a backslash stands before it. It takes no text for an absolute path when all that follows the drive letter and its colon is escape sequences of a newline, a tab or a carriage return (`\n`, `\t`, `\r`), so a message ending in a letter, a colon and such a sequence is not listed; a path written with a real name, a Git Bash path, a link after a space or a mark and a text stuck to such a sequence stay listed.

- **Scope:** task-cycle, agent-instructions, project-level

### WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?

A user's places on their own disk that lie outside every repository, such as the place of a product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json`, found at that place for every user and through no environment variable: a JSON object whose keys are repository names, each holding entries by name, such as `tasks`, `projects` and `task-rules`, whose values are paths on the user's disk. No file the repository tracks holds an absolute path, or a note link in a Markdown file, other than the files that the invariant `tracked-file-private-paths` names, which write example paths in order to find or to test them; a file that points to such a place names its entry in the locations file. The copy of a task cycle's record and the description of a request are checked for a note link in every file, as WAY-309 gives.

- **Scope:** agent-instructions, project-level, foundation-review, product-guidelines, task-cycle, process-audit

### WAY-324 — How does a product check the files it tracks for private paths and notes?

A command of the-way checks the files git tracks in the repository where it is run and skips the files that the sentence of the invariant named by its argument lists. A product whose repository is public adds the check with an invariant of that kind, whose method is `test`, and a short test that runs the command with the identifier of the invariant and cites it; the test of the invariant `tracked-file-private-paths` in the-way runs the same command and keeps no list of its own. Every text between backticks in the sentence names a file the command skips, and a name of a file that git does not track is an error.

- **Scope:** task-cycle, installation

### WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it?

The-way gives a template of a register of problems, which holds for each problem the cycle it comes from, its class, its weight, the cost of its occurrence, the issue it belongs to — the one matter that like problems of several cycles make — and that issue's fate, the fix of an implemented issue included. A user's own tool fills the register and the user adapts the template to their own needs; the audit reads the register that an entry of the user's locations file names and gives no problem a class, a weight or a cost of an occurrence itself.

- **Scope:** process-audit

### WAY-337 — How is the cost of a cycle measured?

A cycle's cost is two numbers, neither divided by a measure of the size of the task: its cost at constant prices, computed from a price list of models that carries a date, and the share of that cost spent in fix rounds, a fix round being the fix of a review's findings and the review of that fix. A turn of an agent serves a fix round when the message that dispatches or resumes it names the round's findings file by its path in the cycle's `reports/`, which only the messages of that fix and of the review of that fix do, and the cycle's record names each round by that path. The share is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and the stages cannot tie each round to the turns that served it.

- **Scope:** process-audit, task-cycle

### WAY-339 — When do the measures of the audit stop being comparable?

A new series of the cost of cycles, the two numbers of WAY-337, starts only with a new price list or with a change of the script that measures the cost, `task-cycle/cycle_stages.py`; a new series of the count of remarks starts wherever a series of the cost starts and also with a change of the form of a stage report, of the list of classes or of the instructions of the reviewer. The measures of how a cycle's agents use context and the prompt cache and the times of the gate form series of their own: a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process, whose output gives the time of each directory; no change of the instructions of the cycle, the reviewer's and the author's included, starts one. The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; and where a cycle's own change changes a tool that measures — the script that measures the cost, the script that counts the measures of context and cache use, the script that records the gate times or the test runner of the process — the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them, and its other measures as they stand under the version it ran on.

The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again, and, for each agent of the cycle, the bytes of the decision log and of the index of decisions that entered its context and how many times each entered it — are counted by a script of their own into a file of their own in the cycle's record, and are never columns of the stage report of the cycle's stages, the table of its tokens by model. The one exception is that this report holds, for each stage and model, the tokens written to the cache at each lifetime, as an input of the cost (WAY-337) and not as a measure of cache use: the script that measures the cost counts them, the script of the other measures counts the same tokens for its own file, and neither takes its figures from the file of the other.

- **Scope:** process-audit, task-cycle, gate

### WAY-350 — Which runs of the gate does the audit compare between versions of the process?

The script that runs the gate records, at each run, how many other gate runs by the script were going at the same time on the machine, from a registry that the script keeps in the user's own directory, outside every repository: an empty file for each run, made when the run starts and marked as ended when it ends, a run that has not ended counting for at most six hours, an ended one kept for a day and an entry whose times cannot be, such as an end in the far future, deleted and counted for nothing. The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.

- **Scope:** process-audit, task-cycle

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
- WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?
- WAY-82 — How does an environment fact keep up with what its source says?
- WAY-84 — How is a setting that people of the product change outside its repository written?
- WAY-85 — How is a finding of a study written as an environment fact?
- WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?
- WAY-44 — What assigns a file to a part?
- WAY-48 — How is a trust boundary recorded?
- WAY-52 — What is generated from the part map for an agent?
- WAY-53 — How is a derived file compared with what its generator produces?
- WAY-225 — What in a product's foundation is derived rather than written by hand?
- WAY-128 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand?
- WAY-129 — How does an instruction file point an agent to another file?
- WAY-130 — When does a rule enter an instruction file, and when does it leave?
- WAY-131 — How is it settled whether a rule of an instruction file works?
- WAY-132 — Which file carries the instructions Claude Code, Codex and Cursor share?
- WAY-133 — How is a rule of an instruction file kept when it has to hold every time?
- WAY-141 — How does the installer give Claude Code the guidance in a product's root AGENTS.md?
- WAY-127 — How does a session working on the-way itself reach the-way's skills?
- WAY-256 — Where does a fragment of a skill stand?
- WAY-265 — Where is the file of a variant named, when a step's file points to it?
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
- WAY-124 — When is a task ready for its cycle?
- WAY-134 — How does a task carry what its refinement settles for the foundation?
- WAY-140 — How does a task change something outside the product's repository?
- WAY-154 — How do agents exchange a project task refinement and keep its result?
- WAY-155 — What may the answering agent settle during a refinement round?
- WAY-355 — Which task fixes a defect found after a merge?
- WAY-372 — When is a task split into several tasks?
- WAY-374 — Does the refinement of a task ask about a word its sources leave readable in two ways?
- WAY-11 — How does a task end?
- WAY-13 — What sets the weight of a task's process?
- WAY-125 — Which methods does the autonomous task cycle use?
- WAY-135 — When does a task's cycle write a spec?
- WAY-136 — When does a task's change need a plan, and who makes and reviews it?
- WAY-148 — How do task-cycle stages pass their work to the orchestrator?
- WAY-229 — On which class of model do the executor of a slice and the one author work?
- WAY-227 — Where does the human meet a task cycle's work?
- WAY-287 — What does a request put before the human for a decision?
- WAY-288 — In what language is a request's description written?
- WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?
- WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong?
- WAY-300 — When does a request tell the human that the foundation waits for a review?
- WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?
- WAY-167 — Where do a product's guidelines stand, and what are their files named?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?
- WAY-212 — How does a product's instruction file lead to its coding guidelines?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-312 — Which sentences does a rule of a product's guidelines not hold?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
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
