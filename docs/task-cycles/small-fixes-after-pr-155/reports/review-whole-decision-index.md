# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 57. Listed by heading alone: 105.

## Listed in full

### WAY-03 — Who may change an invariant test, and when?

Any change may alter an invariant test, in any step of its task, implementation included. A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.

The check of the foundation lists an invariant whose method is `test`, whose sentence a change has reworded and which a file cites by a line `invariant:`, when no file that cites it has changed since the commit the branch left the main branch from. A change whose check lists such an invariant names it in its request in plain words, giving what its sentence now says and that the test that checks it was left as it was. The listing stops no change.

- **Scope:** invariants, task-cycle, agent-instructions

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

### WAY-379 — Does the-way adopt the template of the coding discipline for its own code?

The-way adopts the template of the coding discipline for the code of each part named in *Scope*: its coding guidelines stand in the file `guidelines/coding.md`, with a file `guidelines/coding-<kind>.md` for each kind of code that has an exemplar, and the rules of the template bind its code through the decisions of this log that adopt them or depart from them. The-way departs from the template only by a decision of this log that gives the reason. The *Scope* names every part of the-way's part map that holds Python code, and a change that gives a part Python code, or adds a part that holds it, adds that part to this decision's *Scope*.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-380 — Which linter checks the-way's code, and which of its rules block a change?

Ruff 0.17.1 checks the code of the parts that WAY-379 names, tests included, with the default set of that version, which the environment fact `ruff-default-rules` gives, with no preview rules and for the target version `py314`. The rules that block a change are the default set less the 18 rules `UP031`, `ISC004`, `PLW1510`, `RUF100`, `FURB167`, `FLY002`, `I001`, `B023`, `UP017`, `SIM117`, `UP012`, `RUF015`, `SIM102`, `C419`, `RUF012`, `SIM114`, `SIM905` and `SIM115`, which stand among the examples of the coding guidelines. A comment in the code that turns a rule off has no effect, a fault of one file is fixed in that file, and turning a rule off for the whole of the-way, or moving a rule between the blocking rules and the examples, is a change of this decision.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines, repository

### WAY-381 — How is the version of the linter pinned and installed?

The version of Ruff is pinned by `required-version = "==0.17.1"` in `ruff.toml`, which makes Ruff refuse to run in any other version, and by the files of requirements for the tools of quality: `requirements-quality.in`, which holds `ruff==0.17.1` and allows wheels only, and `requirements-quality.txt`, which holds the SHA-256 sum of every wheel of that release and no source distribution. Ruff stands in the environment `.runs/quality-venv`, which the section "Running the tests" of `README.md` tells how to install from the requirements file, and each job of CI gains one step that installs it there, while the one command that runs the checks stays `python -B gate/run_tests.py` (WAY-16).

- **Scope:** repository, agent-instructions

### WAY-382 — Does the-way's code get an automatic formatter?

The-way's code has an automatic formatter: the formatter of Ruff, in the version that WAY-381 pins, run with the configuration `ruff.toml` at a line width of 100 and every other setting at its default, so that `### Formatter` of its coding guidelines names this decision and the invariant `formatter-layout`. The code of the parts that WAY-379 names stands in the layout the formatter leaves, the formatter having entered the-way by one reformatting of the whole of that code (WAY-205).

The formatter and its invariant cover `.py` files only, never a Python example in a Markdown file, and a comment `fmt: off`, `fmt: on`, `fmt: skip`, `yapf: disable` or `yapf: enable` in a file that the rule covers is forbidden: the test of the formatter fails on it.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines, repository

### WAY-383 — Does the-way's code get an audit of its dependencies?

The-way departs from the audit of dependencies, so `### Dependency audit` of its coding guidelines reads `none — WAY-383`: its code imports nothing from outside the standard library of Python, and the one dependency it declares is the linter, in the version WAY-381 pins. A change that brings a dependency of its code other than the linter ends this departure and is a change of this decision.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-384 — Does the-way adopt the six rules of the coding template on failures and logs?

The-way's scripts write no logs: they print their result to the console and report a failure by an exit code and a line `Error:`. The-way departs from all six rules on failures and logs, so each of the headings `### Recording a failure`, `### Hiding a failure`, `### Identifiers in log lines`, `### Business events`, `### Secrets and personal data` and `### Logging scope` of its coding guidelines holds only `none — WAY-384`.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-385 — How large may a function and a file of a script of the-way be?

A function of a script of the-way has at most 110 lines, counted with the functions nested in it, and a file of a script has at most 1200 lines, in each part that WAY-379 names, both counted on the code as the formatter of WAY-382 leaves it; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception. A test of the suite counts the lines with the `ast` module of the standard library, runs apart from the run of the linter and, where it fails, names every function and file over a threshold with its size (WAY-361).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?

`task-cycle/tracked_private_paths_check.py` is the exemplar of the kind `check` of the-way's code. The coding guidelines of the kind hold no rule that a test checks, so the exemplar stands there as an example and binds no later code.

- **Scope:** task-cycle, project-level, elements-common, instruction-files

### WAY-387 — Which file is the exemplar of the kind `measuring-report` in the-way's code?

`task-cycle/cycle_measures.py` is the exemplar of the kind `measuring-report` of the-way's code. The coding guidelines of the kind hold no rule that a test checks, so the exemplar stands there as an example and binds no later code.

- **Scope:** task-cycle, process-audit, project-level

### WAY-388 — Which file is the exemplar of the kind `generator` in the-way's code?

`agent-instructions/skill_entry_points.py` is the exemplar of the kind `generator` of the-way's code, and a script of the kind changes no file of the repository it runs in without `--write`.

- **Scope:** agent-instructions

### WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?

`task-cycle/remove_merged_worktrees.py` is the exemplar of the kind `repository-changer` of the-way's code, and a script of the kind changes neither a file that the repository tracks, other than a report that the human names with `--report`, nor a working directory without `--apply`, or where the confirmation is declined.

- **Scope:** task-cycle, elements-common, installation

### WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?

`task-cycle/gate_times.py` is the exemplar of the kind `command-runner` of the-way's code, and a script of the kind that wraps one command ends with that command's exit code unchanged.

- **Scope:** task-cycle, gate

### WAY-391 — Which file is the exemplar of the kind `shared-module` in the-way's code?

`relation-model/fingerprint.py` is the exemplar of the kind `shared-module` of the-way's code, and importing a file of the kind runs nothing.

- **Scope:** relation-model, process-audit, task-cycle, elements-common

### WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?

The-way adopts the template of the testing discipline for the tests of each part named in *Scope*: its testing guidelines stand in the file `guidelines/testing.md`, and the rules of the template bind its tests through the decisions of this log that adopt them or depart from them. The-way departs from the template only by a decision of this log that gives the reason, as it does from the field *Time limit* of a recipe and from the rule of mutation testing, and the rule `### AI in tests` enters with no decision on a tool, since no test of the-way uses an AI tool. The *Scope* names every part of the-way's part map that holds a test, and a change that gives a part a test adds that part to this decision's *Scope*.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-393 — At which levels do the tests of the-way stand?

The tests of the-way stand at five levels: unit, files test, git test, repository test and e2e. The files test, the git test and the repository test are terms of the glossary, which gives each by the resources a test of that level may touch, and an e2e test runs a whole path of a session through several scripts.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines, glossary

### WAY-394 — Where does a test of the-way take its expected value from?

A test of the-way takes the value it expects from the entries of the-way's foundation, from its glossary, from the templates and skills that the script under test carries out, or from the description at the head of the script, which gives its exit codes and the form of its result, and from no other document (WAY-232).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-395 — Which fields of a recipe of a level of the-way's tests bind?

In the recipe of each level of the-way's tests the fields *Purpose*, *Files*, *Doubles*, *Data*, *Time and randomness*, *Exemplar* and *Command* bind and name this decision, and *Shape* stands as an example. *Purpose* says what the level is for and when not to use it; *Files* has the tests as files `test_*.py` in the directory of the part, beside the script they test, under `unittest`; *Doubles* allows a double only of the clock and of what a test cannot do on a git repository it builds in a temporary directory, git and the file system being real and standing in a temporary directory, and at the level of a repository test the checkout being real; *Data* has the values of a test written out in it, each with its source in a comment; *Time and randomness* has the test give the script its time, by replacing the clock function of the script in the process of the test or by giving a fixed time to a script that takes one, and no fixed pause; *Command* is `python -B gate/run_tests.py <directory>`, which the gate narrows to a directory and no further. The field *Time limit* reads `none — WAY-395`, since the-way has no file that holds a limit and each limit stands at the call that needs it.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-396 — Which test is the exemplar of the level unit of the-way's tests?

`relation-model/test_fingerprint.py::Fingerprint.test_a_tab_is_kept` is the exemplar test of the level unit of the-way's tests.

- **Scope:** relation-model

### WAY-397 — Which test is the exemplar of the level files test of the-way's tests?

`task-cycle/test_cycle_measures.py::RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted` is the exemplar test of the level files test of the-way's tests.

- **Scope:** task-cycle

### WAY-398 — Which test is the exemplar of the level git test of the-way's tests?

`project-level/test_plan_state_invariant.py::PlanStateEvidence.test_fresh_remote_record_composes_both_transitions` is the exemplar test of the level git test of the-way's tests.

- **Scope:** project-level

### WAY-399 — Which test is the exemplar of the level repository test of the-way's tests?

`elements/common/test_elements_pending_marker.py::TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker` is the exemplar test of the level repository test of the-way's tests.

- **Scope:** elements-common

### WAY-400 — Which test is the exemplar of the level e2e of the-way's tests?

`process-audit/test_audit_count.py::Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is the exemplar test of the level e2e of the-way's tests.

- **Scope:** process-audit

### WAY-401 — What does the-way deliberately not test?

The-way does not test automatically what an agent does when it follows a skill: its tests check the form of the texts of the skills and their consistency, and the behaviour of the agents is checked by the human's review of a cycle at the merge and by the audit of the process, never by the gate. The category is tested again when an error of an agent's behaviour repeats that the audit does not catch before the merge.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-402 — Does the-way adopt a mutation tool?

The-way adopts no mutation tool and departs from the rule of mutation testing of the template of the testing discipline, so `### Mutation testing` of its testing guidelines reads `none — WAY-402` and the author of a change checks its tests in every part by mutating the code in their head (WAY-253). A mutation tool enters the-way, for the parts whose complexity lies in computation, when an error passes after a merge in such a part for want of an assertion.

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
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-21 — What is a decision's scope?
- WAY-26 — How are trade-off principles and non-goals written?
- WAY-36 — Is a rule a decision or does it belong in a plan?
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice?
- WAY-25 — What settles a collision between two decisions?
- WAY-30 — What happens when a change contradicts a decision?
- WAY-114 — What does a human accept of an entry, and when?
- WAY-315 — From when does a decision of the foundation bind the work on a task?
- WAY-33 — What does the author of a foundation change search for?
- WAY-113 — How does an agent of the-way ask a human decision?
- WAY-150 — How do the-way skills choose which product foundation material to read?
- WAY-51 — What does the main branch hold where the product does not meet an invariant?
- WAY-61 — How is an invariant's method of checking written?
- WAY-62 — What does an invariant entry name in the part map?
- WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?
- WAY-82 — How does an environment fact keep up with what its source says?
- WAY-44 — What assigns a file to a part?
- WAY-48 — How is a trust boundary recorded?
- WAY-16 — How are the checks of invariants run?
- WAY-38 — In what are the scripts of the-way written?
- WAY-55 — Which part of the process holds the gate?
- WAY-63 — What is an invariant's result, and when does the command running the tests fail?
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?
- WAY-160 — How does the task-cycle orchestrator run the finished change's gate?
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
- WAY-370 — What does a task cycle do where the session has none of the-way's agent types?
- WAY-106 — What does the project level write before tasks exist?
- WAY-126 — How does a projected entry enter the foundation?
- WAY-267 — How does the step that settles technology run outside a project definition?
- WAY-268 — Who settles a technology choice that no decision or definition settles?
- WAY-269 — How does a task leave a cycle that met a reserved choice, and how does it come back?
- WAY-319 — What must an agent's way to the running product allow when two task cycles run at once?
- WAY-144 — How does a project plan show which tasks can be worked on side by side?
- WAY-147 — How is a task of a project plan named, and what does its cycle take from the name?
- WAY-124 — When is a task ready for its cycle?
- WAY-134 — How does a task carry what its refinement settles for the foundation?
- WAY-140 — How does a task change something outside the product's repository?
- WAY-355 — Which task fixes a defect found after a merge?
- WAY-11 — How does a task end?
- WAY-13 — What sets the weight of a task's process?
- WAY-125 — Which methods does the autonomous task cycle use?
- WAY-135 — When does a task's cycle write a spec?
- WAY-136 — When does a task's change need a plan, and who makes and reviews it?
- WAY-148 — How do task-cycle stages pass their work to the orchestrator?
- WAY-229 — On which class of model do the executor of a slice and the one author work?
- WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?
- WAY-164 — What does the author of a change check of its own work before review?
- WAY-255 — How does an agent of a task's cycle wait for a command that runs long?
- WAY-260 — What does each task-cycle stage report about what it could not find or understand?
- WAY-261 — What does a task cycle report about a check that fails and passes when run again?
- WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?
- WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?
- WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?
- WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?
- WAY-406 — Who walks through the running product the behaviour that a change's tests do not cover, and for which changes?
- WAY-407 — Who approves the cases of the walk through the running product before it is made?
- WAY-408 — What does the author or the executor do with a case of the walk that fell wrong?
- WAY-410 — What does an agent do when a test contradicts the requirement, or when it cannot pass the test by general code?
- WAY-10 — Who assesses a change to an invariant test or to the foundation?
- WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?
- WAY-162 — How does a code review of a task's change end when its findings block?
- WAY-263 — Which foundation mismatches are Important findings?
- WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?
- WAY-363 — How does a reviewer grade a finding about the structure of code?
- WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?
- WAY-409 — What does a reviewer do about code of the product that passes a test without meeting the requirement?
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
- WAY-404 — Who marks a contradiction with the settlements, and where does the audit of the process read it from?
- WAY-405 — How does the audit of the process read the reason of a discarded attempt?
- WAY-416 — What does the command that counts the audit do when a file it reads lacks a field it needs?
- WAY-361 — How does the review of a change get the sizes of functions and files from a product?
