# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 51. Listed by heading alone: 133.

## Listed in full

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/`, the copies of the cycle's agent type definitions under `.claude/agents/` and the CI configuration under `.github/workflows/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; any other directory what the sentence of its part in the part map names. The entries in `foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, foundation-review, process-audit, task-cycle

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it. In CI that command runs on every merge request, with `.the-way` at the commit the product pins (WAY-34), from a file of CI configuration that the product writes itself by the description the-way gives, and the installer writes none. The result of that run is a check the repository requires before a merge, and the owner of the repository may bypass it.

- **Scope:** invariants, agent-instructions, task-cycle, gate, installation

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

The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it. Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the orchestrator waits for the result of the run on each head it pushes to it, a correction's included, treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review, save a check outside the task's scope that passes when run again, which WAY-261 governs — and puts the result into the request's description; a request the cycle leaves blocked for unfinished code is out of that wait, its description saying that the result of the run stands on the request's page and was not waited for.

- **Scope:** task-cycle

### WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?

The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under the shared reading of product guidelines: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither. The *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds that part to this decision's *Scope*. A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives no line `Error:`. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*. The command that counts the audit, where a table of weights or a table of the costs of an occurrence in the register of problems lacks one of its levels, writes its result, gives the values that depend on the table as unknown and ends with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither of the two columns of the cache writes in its detailed section, that command reads the report as an earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and priced as input, an approximation, and no value unknown for the missing columns, while a stage report that has one of the two columns and not the other has a missing field, with the line `Error:`. Where the locations file has no entry `repository` under `the-way`, no field is missing and that command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-363 — How does a reviewer grade a finding about the structure of code?

A reviewer grades as Minor a finding about the structure of code that lies below the threshold of the rule of size in the product's coding guidelines, and every such finding in a product that has no rule of size, whatever the reason: for example, it departed from the rule by a decision, it has no coding guidelines at all, or its guidelines were written before the rule existed. The reviewer judges its scope as for any finding (WAY-161). A finding about a function or a file over a threshold is graded as any other finding.

- **Scope:** task-cycle, product-guidelines

### WAY-167 — Where do a product's guidelines stand, and what are their files named?

A product's guidelines are written by hand and stand outside its foundation, in the directory `guidelines/` at the root of its repository: a file `guidelines/<discipline>.md` for each discipline of work on the product it keeps guidelines of, save the styleguide and coding disciplines. The guidelines of the styleguide discipline stand in a file `guidelines/styleguide-<part>.md` for each user interface of the product, `<part>` being the identifier of the part of the product's map whose files draw that user interface; those of the coding discipline stand in a file `guidelines/coding.md`, which holds the product's standing checks, the rules of the whole of its code and a table naming each other file of the discipline with when to read it, and in a file `guidelines/coding-<kind>.md` for each kind of code that has an exemplar, which holds that exemplar and its rules, `<kind>` being the identifier of the kind that the decision designating that exemplar gives. The directory `guidelines/` belongs to the part of the product's map whose files direct whoever carries out its tasks, as its instruction files and skills do.

- **Scope:** product-guidelines, installation

### WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?

A binding rule of a product's guidelines says what to do and how, and may give a use that follows it and one that breaks it, each in one line; what the guidelines hold that states no rule is an example. A rule that executes a choice of the product with a real cost names by identifier the decision of the product's log that carries the choice, while its reasons and rejected options stand in that decision alone, and a rule that only says how to write code, tests or the look of the product reads `none` in *Decision* and gives its reason in one sentence. A rule names an invariant only where a cheap test of the product's suite checks the rule on a convention of the product's code; a rule no such test can check names none, and the review of each change the rule reaches compares the change with it.

- **Scope:** product-guidelines, decisions, invariants, task-cycle

### WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?

The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason. A decision of the-way on what such a template carries or what such a skill proposes binds the template and the skill, never a product's screens or code directly.

- **Scope:** product-guidelines

### WAY-212 — How does a product's instruction file lead to its coding guidelines?

A product's root `AGENTS.md`, outside the block the-way's installer writes, points to its coding guidelines by one line naming `guidelines/coding.md` by its path in backticks with the condition of changing the product's code, written as the skill of `instruction-files` gives a pointer, and no line of it names a file `guidelines/coding-<kind>.md`. Each such file is named instead by a row of the table of `guidelines/coding.md`, by its path in backticks with the condition under which to read it, such as adding or changing a file of its kind.

- **Scope:** product-guidelines, instruction-files

### WAY-213 — How do the agents of a task's cycle read the product's guidelines?

In the task cycle the orchestrator selects by `product-guidelines/reading.md` the product's guidelines of the parts each agent's work touches — every file whose *Applies to* names such a part, a file of a kind of code only where its row's *When to read* in `guidelines/coding.md` also matches the work — and names those files in the handoff of every other agent that writes or reviews the spec, plans, makes the change or reviews a part of it, for a slice through the *Read* of its plan, which the planner proposes and the orchestrator checks; the agent reads each file named whole, never excerpts of it or a review checklist in its place, while the reviewer of the whole change selects the guidelines of its own review. The orchestrator reads the guidelines of the task's parts once, and those of a part the spec or plan adds when it adds it, and names in each handoff the files of the parts that agent's work touches, with no record of its reasons, no check of the selection by the agent that receives it and no step of its own revisiting the selection at each handoff; an agent whose work reaches a part the selection did not cover reads that part's guidelines itself and names the reach in its report. With the styleguide, the planner and the author working without a plan read the order of work the template gives, never as a rule — the environment and the library first, then the values in their source, then one screen, then its states — and follow it or explain departing from it.

- **Scope:** task-cycle, product-guidelines

### WAY-312 — Which sentences does a rule of a product's guidelines not hold?

Nothing that edits a product's guidelines, whether the template, a skill of guidelines or a product's own task, replaces a sentence that names a practice a model knows with the name of the practice, or takes out a case that follows from a rule's purpose. A product's own task cleans its existing guidelines of the sentences that the shared template of a product's guidelines rules out — a rule lists no state of the product's code or of the product and repeats neither a decision of the product's log nor a value taken from a configuration file — and the skills of guidelines carry no step that searches for them.

- **Scope:** product-guidelines

### WAY-172 — How is a new or changed meaning of a product's guidelines approved?

A new or changed meaning of a product's guidelines that carries a choice with a real cost is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as WAY-30 has a change to a decision approved, or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision. A new or changed rule that only says how to write code, tests or the look of the product, with no decision, is accepted by the human as a row of the task's table of settlements before the code that uses it, or, where the cycle found the rule itself, at the merge from the request's description, and a rule of a template of the-way binds a product only through a decision of its log that adopts it (WAY-173). Using a meaning that a decision of the product's log already carries takes no approval, and neither does changing a value that keeps its meaning; in the area of new and changed meanings of a product's guidelines that carry a choice with a real cost, this decision prevails over WAY-114, under which an agent writes such an entry on its own recommendation for the human to accept at the merge.

- **Scope:** product-guidelines, decisions, project-level, task-cycle

### WAY-174 — How do the-way's skills of guidelines ask the human?

The-way's skills `maintain-styleguide`, `maintain-coding-guidelines` and `maintain-testing-guidelines` put to the human every choice they settle for a product's guidelines, a choice they recommend included, and show each in plain words — a styleguide's by what someone using the product sees on the screen, never by the names or values of design tokens, coding guidelines' by their effect on the product, never by the names of a linter's rules or the values of a tool's configuration, and testing guidelines' by their effect on the product, never by the name of a technique or a tool — saying in plain words what a term of the field means before they first use it. The coding-guidelines skill asks for decisions, never for single rules, so that the human adopts a linter's set of rules whole. In the area of the questions these skills ask this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** product-guidelines, decisions

### WAY-215 — What happens to a task that needs missing discipline guidelines?

Unless an approved departure under the shared reading of product guidelines applies, a task changing a user interface with no styleguide, writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines, whether or not the product already has screens, code or tests, stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge of a separate guidelines task; refinement independent of that answer continues, and a task writing those guidelines does not wait for its own output. For an independent or source-only task `refine-task` adds the prerequisite to the product's backlog after human approval, while for a plan member it returns `plan change` if the plan lacks that task or `waits for task <n>` if the plan holds it, keeping the plan's ownership and states. After that task merges, refinement resumes, reads the guidelines and settles the meanings the task needs under WAY-172 before readiness; extension or correction of existing guidelines stays in the current task under WAY-172 and WAY-199, unless the human separates it.

- **Scope:** project-level, product-guidelines

### WAY-216 — What does refinement assign to a task creating an unindexed kind of code?

A task that creates the first file of a kind of code whose row the general coding index lacks gains in *To do* the designation of that kind's exemplar as the skill `maintain-coding-guidelines` gives it and its kind guidelines with their index row, without waiting for a separate exemplar task, and in a product that has coding guidelines it settles and checks, of the standing checks, only those the kind touches. Where files of the kind already exist, refinement records that discrepancy and routes exemplar selection through the comparison that skill gives existing code, rather than treating the next file as the first. Neither a kind's first file nor that comparison alone makes a task an extension under WAY-251 or takes research of the standing checks, except that a first file of a kind in a language that none of the product's standing checks reads makes the task an extension; the comparison covers that kind alone, takes no trial run of a linter's set and is no audit of a product with code.

- **Scope:** project-level, product-guidelines

### WAY-247 — May one task write a product's coding and testing guidelines together?

One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.

- **Scope:** product-guidelines, project-level

### WAY-251 — What distinguishes a refresh from an extension of guidelines?

For the skills `maintain-coding-guidelines`, `maintain-styleguide` and `maintain-testing-guidelines`, a refresh updates or corrects accepted guidelines within the scope they already cover, including adapting them to a new version of a tool the product already uses. An extension covers something new, and its research checks whether to use what the product already has or something else, with the human's preferred tool remaining the proposal.

- **Scope:** product-guidelines

### WAY-280 — On what scale does an audit of the skills of guidelines weigh what it found?

An audit of the skills `maintain-coding-guidelines`, `maintain-styleguide` and `maintain-testing-guidelines` gives each cause of what it found one weight, `grave`, `heavy`, `medium` or `light`, on one scale described once in a file the three skills share. A weight is measured by the effect on the user or the owner of the product and follows from what is at stake, never from how many places break a rule. The-way adopts weight, merging and order from a course's skill for auditing observability, for these audits, and not the audit as a skill of its own.

- **Scope:** product-guidelines

### WAY-284 — What decides which causes of an audit a task takes?

The weight proposes and the human decides: the agent proposes which causes of the top of an audit's list a task takes and which it defers, and the human settles it. On deferring a `grave` cause the agent asks whether to open a task for it in the product's backlog, and a yes takes the route WAY-215 gives a prerequisite, with nothing waiting for that task. The causes below the top are deferred together, for standing below the top, unless the human takes one.

- **Scope:** product-guidelines, project-level

### WAY-198 — How does a product's exemplar bind?

A decision of a product's log designates, for a kind of code, the one file of the product that is the exemplar of that kind, naming in backticks its path and the kind's identifier, and what of that exemplar a script can check — where a file of the kind lies, what it calls, how it validates its input — stands in the coding guidelines of that kind as rules, each naming an invariant. The rest of the exemplar stands there as an example and binds no later code.

- **Scope:** product-guidelines

### WAY-199 — What change of a product's exemplar takes approval?

Designating another file as the exemplar of a kind of code and changing a rule a script checks from that exemplar are changes of the product's decisions, approved as WAY-172 gives a changed meaning, while an edit of the exemplar that keeps those rules takes no approval. The coding guidelines of a kind give beside the path of each file of the kind they list its status, `exemplar`, `copy` or `do not copy`, and beside the exemplar's path the decision that designates it.

- **Scope:** product-guidelines

### WAY-202 — Which standing checks must a product's coding guidelines settle, and from when do they bind?

The template of the coding discipline requires three standing checks of a product's code — a linter, a formatter and an audit of dependencies — and the rule of a product's coding guidelines on each names the invariants of that check the template gives. A product departs from any of them only by a decision of its log that gives the reason. They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it with the reason.

- **Scope:** product-guidelines

### WAY-203 — Which rules of a linter's set block a change of a product's code?

A rule of a linter's set stands among the rules that block a change in the product's decision adopting the set, and so is checked by the invariant of the one rule of the product's coding guidelines on its linter, only where every report it gives on the product's code leads to a change of code worth making, a report counting by whether it leads to such a change, whether it is technically right or not. A rule of the set that gives a report leading to no such change is no rule that binds the product's code: it may stand among the examples of the coding guidelines, and no invariant checks it, so the gate does not run it. A comment in the code that turns off a rule that blocks has no effect: where the tool can be told so by a flag or its configuration, the test of the linter's invariant runs it so, and where it cannot, the review of each change finds such a comment.

- **Scope:** product-guidelines

### WAY-204 — How are the rules of a linter's set split between the rules that block and the examples?

The skill `maintain-coding-guidelines` proposes which rules of a linter's set block and which stand among the examples from a trial run of the set on the product's code, each report of which an agent that wrote none of that code judges by whether it leads to a change of code worth making, whether it is technically right or not, and a rule with one report that leads to no such change goes among the examples; for a product with no code it proposes as blocking the rules the tool's documentation marks as recommended. The human approves that split in the product's decision adopting the set, and a rule on which a later report leads to no change of code worth making goes among the examples by a change of that decision, which the human approves. The invariant of the linter rests on one environment fact, the rules the set holds at the edition the adopting decision names, and that decision gives the blocking rules as the set less the rules it keeps among the examples.

- **Scope:** product-guidelines

### WAY-205 — How do a linter and a formatter enter a product whose code already breaks their rules?

Where a product's code already breaks the rules of its linter's set that block, the skill `maintain-coding-guidelines` proposes the linter's invariant over the whole of that code, marked violated until the code is cleaned (WAY-51). A formatter enters a product by one reformatting of the whole of its code in the task that brings the formatter.

- **Scope:** product-guidelines, invariants

### WAY-206 — What does the audit of a product's dependencies check?

The skill `maintain-coding-guidelines` proposes an audit of dependencies that checks a change and fails it only where a version of a dependency that the change brings in against `{fork-point}` has a known vulnerability, as the advisory database named by the product's decision adopting the audit gives it when the check runs, of at least the severity that decision sets, every severity being among the ways the skill offers. The template of the coding discipline carries no audit of the whole tree of a product's dependencies. The signal of a vulnerability found in a dependency the product already holds is the alerts of the service its repository lies on, on GitHub the Dependabot alerts; the skill proposes that the product turn them on, and a human turns them on.

- **Scope:** product-guidelines, invariants

### WAY-360 — Does the template of the coding discipline require a rule of the size of a function and a file, and how does it reach a product?

The template of the coding discipline requires, in the general file of a product's coding guidelines, a rule of the size of a function and a file under the heading `### Size of a function and a file`, after the six rules on failures and logs, with an invariant of its own and a test of its own, outside the set of rules of the product's linter. A product sets its thresholds after a trial run on its existing code and writes its exceptions in its decision on the rule, or departs from the rule only by a decision of its log that gives the reason (WAY-173), and a product that already has coding guidelines gets the rule by an ordinary extension, as the skill `maintain-coding-guidelines` gives it for the rules on failures and logs. Where code other than the exceptions of the product's decision stands over a threshold, the rule's invariant is marked violated until that code is cleaned (WAY-51).

- **Scope:** product-guidelines

### WAY-361 — How does the review of a change get the sizes of functions and files from a product?

The test of a product's rule of size, when it fails, names every function and file over a threshold with its size, and the reviewer of the whole change runs it as an ordinary test of the product's suite on the state before the change and on the state after it. A product has no command of its own that gives the sizes of functions: the one command that runs all of its tests stays the only one (WAY-16).

- **Scope:** product-guidelines, task-cycle

### WAY-228 — Where does a test take the input it asserts on and the value it expects?

The template of the testing discipline requires the rule that a test takes the input it asserts on and the value it expects written out, wherever the code under test would otherwise compute either, and only the side it compares against comes from the run; a property test takes its inputs from a test library's generator and its expected value from a relation the code under test does not compute — undoing the operation, an invariant's sentence, or a simpler version written from the requirement, not copied from the code — and a counterexample the library finds is kept as an ordinary test with its values written out. A product departs from the rule only by a decision of its log that gives the reason, and the rule binds a product from the task that writes its testing guidelines.

- **Scope:** product-guidelines

### WAY-231 — Where do the rules of a product's tests stand?

Testing is a discipline of a product's guidelines of its own: the-way gives a template of the testing discipline, from which a product writes its file `guidelines/testing.md`, and the skill `maintain-testing-guidelines`, which leads the work that creates and keeps that file. A kind of code of a product's coding guidelines is code of the product other than its tests, and the patterns a product's tests follow stand in its testing guidelines at the level of test they belong to.

- **Scope:** product-guidelines

### WAY-232 — Where does a test's expected value come from?

The template of the testing discipline requires the rule that the expected value of every test of a product comes from a source other than the code under test — a document of the product its testing guidelines name as a source, such as its decision log, its glossary or its task descriptions; a relation the code under test does not compute; a crash counted as a failure; or a human's judgement — and never from what the code gives today, snapshots and characterization tests included. Where a test's name does not show the source of a value, a comment in the test names it, by the line of the document or by the human and the date, and the review of a change asks of each assertion where its value comes from.

- **Scope:** product-guidelines

### WAY-233 — What does a change to an existing test need?

The template of the testing discipline requires the rule that changing the expected value of an existing test, deleting a test, weakening an assertion, and skipping or disabling a test are one kind of change, each made with its cause on the side of the data or of the requirement and a pointer to the evidence of that cause, and that the review reads such a change made without them as masking a defect. The rule lists the ways a test is weakened: equality loosened to "contains", a count removed, a tolerance raised, a skip, a deletion.

- **Scope:** product-guidelines

### WAY-234 — What may a test's assertion check?

The template of the testing discipline requires the rule that a test's assertions check the behaviour its rule or its task requires, a detail of how the code carries it out that the requirement does not ask for being no condition of the test passing, and that the review asks of each assertion whether the code could change so that the required behaviour stays and the assertion breaks, a yes marking a detail. A check of the case's setup is allowed where it stands before the action, is marked as a precondition and checks a property of the case that the requirement names, never the structure of the data that builds the case.

- **Scope:** product-guidelines

### WAY-235 — How do a product's tests keep its trust boundaries?

The template of the testing discipline requires, and the skill `maintain-testing-guidelines` proposes, for each trust boundary of the product's part map at least one invariant that the boundary refuses crafted input or unauthorised access, checked by a permanent test that checks the refusal directly, takes the expected refusal from the product's decisions on permissions and is seen failing once; a boundary that does not refuse today has that invariant marked violated as WAY-51 gives it, and a boundary that is only the configuration of someone else's service stays with the review of WAY-48. For authorization, the rule of the product's testing guidelines holds a table of who, which resource and which action with the expected result, each row naming the decision on permissions it comes from. In the area of trust boundaries this decision prevails over WAY-168: the *Invariant* of the rule on trust boundaries names the refusal invariant of each boundary, although its test checks the product's behaviour rather than a convention of the product's code.

- **Scope:** product-guidelines, invariants

### WAY-236 — How does AI enter a product's tests?

The template of the testing discipline requires the rule that AI is no level of test: a test an AI wrote follows every rule of the testing guidelines, an agent exploring the running product finds cases that become ordinary tests, and a tool that heals a test by itself changes only how the test finds what it acts on, a changed assertion or a red test turned into a skipped one being a change of an existing test (WAY-233). An AI judge enters a permanent test only where the behaviour cannot be checked by a plain comparison, its verdict is yes or no, it has been checked on examples a human judged and runs on a pinned version of its model, and the testing guidelines say how they treat the spread of its verdicts; how each AI tool the product's tests use behaves stands in an environment fact of the product, naming the version the product uses, with the date its source was read.

- **Scope:** product-guidelines

### WAY-237 — What does a product deliberately not test, and where is it said?

The template of the testing discipline requires a section `## Not tested on purpose` of a product's testing guidelines, in which each item is a category of behaviour or of code, never a single file or test, and names the product's decision that excludes it, whose binding sentences give the condition under which the category is tested again and whose rationale gives the reason; the section reads `none` where nothing is excluded. A trust boundary never stands in it.

- **Scope:** product-guidelines

### WAY-238 — At which level does a test stand, and who chooses it?

The template of the testing discipline requires the rule that a test stands at the lowest level at which the break it names turns it red, unless going lower would mean replacing with a double exactly what can break, and a product's testing guidelines give no proportion of levels. The author of a change chooses, in the task's cycle, which behaviour gets a permanent test and at which level, naming the break each test catches, and the review checks the choice against the product's testing guidelines, while a task's refinement holds no plan of tests.

- **Scope:** product-guidelines, task-cycle, project-level

### WAY-239 — What does a bug caught only by a high-level test or by a human get?

The template of the testing discipline requires the rule that a bug which only a high-level test or a human caught also gets a test at the lowest level that catches it.

- **Scope:** product-guidelines

### WAY-240 — How do a product's testing guidelines name its test levels?

The template of the testing discipline requires that a product's testing guidelines name its test levels, each with the product's decision that sets it, and that a level whose name means in the product something other than in the field, "integration" above all, is a term of the product's glossary, defined by the resources a test of that level may touch, such as files, the network or a browser. For each part the guidelines apply to, they say in one sentence whether its complexity lies in computation or in its connections. In the area of the names of test levels this decision prevails over WAY-95: a level named in the product otherwise than in the field, a narrower meaning included, takes a glossary entry whether or not a sentence would be read wrongly.

- **Scope:** product-guidelines, glossary

### WAY-241 — What does the recipe of a test level hold?

The template of the testing discipline gives a product's testing guidelines, for each level, a recipe of the same fields — what the level is for and when not to use it, where its files lie and how they are named, the name and build of a test, its doubles, its data, time and randomness, the level's exemplar test, the command and the time limit — each field that binds naming the product's decision that carries it, a field naming none standing as an example, and a field that repeats another level's reading "as in <level>". The field of the command names the gate and how it narrows to the level, a file or a test, where the gate can, and otherwise reads `none`; the field of the time limit points to the configuration file that holds it, and reads `none` where no configuration file holds one; and no recipe lists commands of the test tool of its own.

- **Scope:** product-guidelines

### WAY-242 — How is the exemplar test of a level designated?

The exemplar test of a level of a product's tests is designated by a decision of the product, as the exemplar of a kind of code is: where the level already has tests, the skill `maintain-testing-guidelines` compares them and proposes the exemplar from that comparison, and where it has none, its first test becomes the exemplar. That designation is approved in a task's refinement only where the task's required outcome is itself a test of that level, its document naming the level and that the task's first test of it becomes the exemplar, with no list of tests and no path; where the author of a change chooses in the task's cycle to write a level's first test, it is approved at a blocked draft request, as WAY-172 gives a meaning the task's document does not settle. Until a decision designates it, the field of the exemplar in the level's recipe stands empty, and designating another test is a change of that decision.

- **Scope:** product-guidelines, project-level

### WAY-243 — How is a flaky test treated?

The template of the testing discipline requires the rule that running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of the gate pass, and that disabling or deleting such a test is a change of an existing test under WAY-233.

- **Scope:** product-guidelines

### WAY-244 — When do a product's testing guidelines come into being?

The skill `maintain-testing-guidelines` proposes that a product's testing guidelines come into being before the first task that writes the product's tests.

- **Scope:** product-guidelines

### WAY-252 — How does a mutation tool check a product's tests?

The template of the testing discipline requires the rule that a mutation tool — one that makes copies of the code, each with one small fault, and runs the product's tests on each copy — runs, at a change, on the changed files of each part the product adopts it for, never on the whole product, and that the reviewer of the change classifies each copy no test fails as a real gap, which gets an assertion, an equivalent mutant, which behaves as the code does and is passed over, or a change not worth pinning, which is passed over with its reason; the rule sets no threshold on the share of copies the tests fail. A product adopts the rule by a decision naming the tool and the parts it runs on, chosen among the parts whose complexity lies in computation, or departs from it by a decision that gives the reason.

- **Scope:** product-guidelines

### WAY-253 — Who runs a mutation tool in a task's cycle, and what does the author check in its place?

Where a product's testing guidelines adopt a mutation tool for a part (WAY-252), the agent that reviews a change reaching that part — a slice, the whole change, a fix of findings or a correction after the human's remarks — runs the tool on the files of that part the reviewed diff changes and classifies itself each copy no test fails, and the author of the change does not mutate that part's code in their head. In every other part, the author mutates the code in their head before finishing — a wrong constant or branch, a missing side effect, an empty return, unchecked empty or hostile input — and treats a mutation no test catches as behaviour left unprotected.

- **Scope:** task-cycle, product-guidelines

### WAY-254 — Where does the command of a mutation tool stand?

The command that runs a product's mutation tool stands in the rule of mutation testing of the product's testing guidelines (WAY-252), and no CI configuration, recipe of a level or instruction file names it. In the area of the command of a product's mutation tool this decision prevails over WAY-16.

- **Scope:** product-guidelines, task-cycle, instruction-files

## Listed by heading alone

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
- WAY-07 — How is a foundation entry changed?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-21 — What is a decision's scope?
- WAY-26 — How are trade-off principles and non-goals written?
- WAY-36 — Is a rule a decision or does it belong in a plan?
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice?
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
- WAY-51 — What does the main branch hold where the product does not meet an invariant?
- WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?
- WAY-61 — How is an invariant's method of checking written?
- WAY-62 — What does an invariant entry name in the part map?
- WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?
- WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?
- WAY-82 — How does an environment fact keep up with what its source says?
- WAY-95 — Which words take a glossary entry?
- WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?
- WAY-99 — How does one word keep one meaning in the foundation?
- WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?
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
- WAY-258 — How are the files of the skill of `instruction-files` laid out?
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
- WAY-377 — Does the refinement of a task list the decisions its document leaves to the executor before the human sees the document, and who lists them?
- WAY-378 — What does the human see after the decisions a task document leaves to the executor are listed and criticised?
- WAY-11 — How does a task end?
- WAY-13 — What sets the weight of a task's process?
- WAY-125 — Which methods does the autonomous task cycle use?
- WAY-135 — When does a task's cycle write a spec?
- WAY-136 — When does a task's change need a plan, and who makes and reviews it?
- WAY-148 — How do task-cycle stages pass their work to the orchestrator?
- WAY-229 — On which class of model do the executor of a slice and the one author work?
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
- WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it?
- WAY-337 — How is the cost of a cycle measured?
- WAY-339 — When do the measures of the audit stop being comparable?
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
