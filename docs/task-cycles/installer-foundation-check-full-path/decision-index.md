# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 43. Listed by heading alone: 0.

## Listed in full

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/`, the copies of the cycle's agent type definitions under `.claude/agents/`, the CI configuration under `.github/workflows/` and the directory `guidelines/` with the guidelines of the-way's own code and tests, which the map gives to `agent-instructions` (WAY-44, WAY-167), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; any other directory what the sentence of its part in the part map names. The entries in `foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, foundation-review, process-audit, task-cycle

### WAY-27 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the places where the work of the-way lies — the place of its tasks and the rules of that place, the register of problems and the results of the audit — which are no source of reasoning, and a file that needs one names it by a key of the locations file of WAY-320, never by a path.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, installation, agent-instructions, instruction-files, product-guidelines, task-cycle

### WAY-34 — Which version of the process does a product use?

A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit. A newer version of the process enters a product only in one commit of the product that moves the pin, made when a task of the product needs a change of the process, as the first commit of that task's branch, under which the task's whole cycle works, or in a step of its own that takes several changes of the-way at once.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, installation, instruction-files, task-cycle

### WAY-100 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.

A decision that adopts a method or practice from outside names the practice and what it takes from it, in its binding sentences or its *Rationale*, and puts what it leaves out of the practice in *Rejected*. Its source is the place the practice was in fact taken from, found by following the trace of that taking, never a document that only describes the practice: the decision names that source in *Based on*, or, for a source a reader of the repository cannot open, describes in *Rationale* what was seen there and says that the source is not open to that reader (WAY-27). A list of what is taken from one source is no decision: each rule taken stands in the decision that carries it (WAY-19).

A decision written from a row of a task's *Settlements to record* takes the ways in its *Rejected* from the row's source, which keeps the parts the practice leaves out where the human weighed them, as WAY-134 gives; there WAY-134 prevails over the paragraph above.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-102 — What is the-way for?

The-way is a process for work on a technology product in which a change of premises or direction is an ordinary step: it passes through the product's foundation and needs no memory of what is linked to what.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-107 — Where does a product tell the project level where its backlog stands?

A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns, a place on the user's disk outside every repository standing there as a key of the locations file of WAY-320, never as a path, and a directory of the repository or the address of a public tracker as it is. A project definition stands in the named project place; when the place is unnamed, or the file or the key it names is missing, the agent asks the human and offers to record the answer where it fits: the key in the file for a place on the user's disk, the section otherwise.

How a task's line is handled — the status of a new line, its move to ready, the form of its dependencies, the characters of its identifier and its being unambiguous in the whole place, how a line is found and kept one to a task, which fields an agent may change, the agreement of the lines at both ends of a dependency, a clash of identifiers — is taken from the rules of the task place itself, never from text written at the product or in the-way's skills; the section names, beside the place of the tasks, the key `task-rules` of the locations file under the product's name, whose value is the path of those rules, and where that key or the file it names is missing, the agent asks the human once and offers to add the key, as for a missing place. The one part of a line that the-way gives is the derivation of a task's identifier from its plan and its name in the plan, so that a dependency can name a task before that task's line exists; where the rules of the task place do not accept the derived identifier, the agent asks the human and writes no line.

- **Scope:** project-level, installation, foundation-review, product-guidelines

### WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?

`elements/common/foundation_check.py` reports an invariant whose method reads `test` and which no line `invariant: <identifier>` in a file git tracks whose name does not end in `.md` cites, in every run but the one made right after an entry is written, which passes the switch `--skip-test-citations` and so skips this report and no other. The one command that runs a product's tests runs the script without that switch (WAY-16).

- **Scope:** elements-common, invariants, gate, installation

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it. In CI that command runs on every merge request and on every system the product runs on, with `.the-way` at the commit the product pins (WAY-34), from a file of CI configuration that the product writes itself by the description the-way gives, and the installer writes none. The result of each such run is a check the repository requires before a merge, and the owner of the repository may bypass it.

- **Scope:** invariants, agent-instructions, task-cycle, gate, installation

### WAY-38 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.

A test of a standing check runs the tool that the check pins from the environment that the repository declares.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions, instruction-files, project-level, task-cycle, process-audit

### WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and the declared version moves when the version in use leaves bugfix support, never because a newer version comes out.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions, instruction-files, project-level, task-cycle, repository, process-audit

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit is bound by WAY-416 in the cases that decision gives, where it prevails over this decision.

Where a script whose purpose is to check the form of a file reads a copy of the file from the commit the branch left the main branch from, a field it needs for a comparison and finds missing from that copy is listed by a line `listed:` that names the entry and the field, with no error and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-128 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand?

A line for a file that an agent's tool loads into every session — one the skill of `instruction-files` proposes, or one a change to the-way's repository instruction files adds or rewords — is one that every session needs or that points to work an agent would not otherwise find, that an agent could not read from the repository or from general knowledge, and without which an agent would go wrong; where an agent may not recognise the moment such a pointer is for, its condition is worded as an agent meets that moment, and the rule it points to stands whole in that file only once records of agents' work show they missed the reworded pointer. Any other rule the skill proposes or such a change adds stands where what calls for it reaches the agent: a rule for some files in a file the tools load with those files, a rule for an activity in the steps of the skill that carries out that activity or in the file that leads it, and knowledge needed now and then in a file such a step or line points to. Lines that stand unchanged are not bound by it, and the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256, and to the text the installer writes in an entry point, instead.

- **Scope:** instruction-files, agent-instructions

### WAY-129 — How does an instruction file point an agent to another file?

The-way's repository instruction files hold no `@` import other than the line `@AGENTS.md` alone at the top of the root `CLAUDE.md`, and the skill of `instruction-files` proposes none other. A pointer the skill proposes, or a change to the-way's repository instruction files adds, names the file to read by its path in backticks with the condition under which to read it.

- **Scope:** instruction-files, agent-instructions

### WAY-130 — When does a rule enter an instruction file, and when does it leave?

The skill of `instruction-files` proposes a rule, and a change to the-way's repository instruction files adds one, only to remove a mistake agents made more than once, found in records of their work, and names that mistake where it proposes or adds the rule, unless the rule carries a decision the repository records or a step of an activity in the file that leads that activity. The skill proposes to take out a rule added for a mistake once that mistake can no longer be named, or once agents working without it show that it is not needed.

- **Scope:** instruction-files, agent-instructions

### WAY-131 — How is it settled whether a rule of an instruction file works?

Where the skill of `instruction-files` says whether a rule works, and where the request of a change to the-way's repository instruction files says so, it is settled as three separate questions: whether the tool loaded it, by one fresh session per variant with a file that has to load as a control; whether agents followed it, by as many fresh sessions with and without it, on one model and tool release, as its effect needs to stand out from the variation between runs; and whether it helped, by whether its mistake stops coming back in agents' work over time, never by test sessions alone.

- **Scope:** instruction-files, agent-instructions

### WAY-132 — Which file carries the instructions Claude Code, Codex and Cursor share?

The skill of `instruction-files` proposes for a repository whose agents use more than one of Claude Code, Codex and Cursor, and the-way keeps for itself, a root `AGENTS.md` that carries the instructions those tools share and a root `CLAUDE.md`, where there is one, whose first line is `@AGENTS.md` alone and which holds only what Claude Code alone needs. The skill leaves out of this proposal the files and the marked block the-way's installer writes in a product.

- **Scope:** instruction-files, agent-instructions

### WAY-133 — How is a rule of an instruction file kept when it has to hold every time?

Where a rule of an instruction file has to hold every time, the skill of `instruction-files` proposes a mechanism that keeps it without the agent choosing to — a CI check, a linter, a check of a step's output, or a local git hook where the rule guards against slips rather than against an agent that can turn the hook off — and a change to the-way's repository instruction files adds such a rule only with its mechanism. The instruction file then says what the mechanism is for, or carries what the mechanism cannot check.

- **Scope:** instruction-files, agent-instructions

### WAY-141 — How does the installer give Claude Code the guidance in a product's root AGENTS.md?

When a product has no root `CLAUDE.md`, the installer creates one whose sole line is `@AGENTS.md`, so Claude Code receives the installer's block and the product's other instructions from root `AGENTS.md`. When a root `CLAUDE.md` already exists without an effective `@AGENTS.md` import, the installation plan warns about the missing import, and the installer leaves every existing root `CLAUDE.md` untouched. The installer writes no `.claude/rules/the-way.md`.

- **Scope:** installation

### WAY-258 — How are the files of the skill of `instruction-files` laid out?

The skill of `instruction-files` keeps beside its `SKILL.md` one file for each kind of text it works on — a file a tool adds to every session, a skill, a file a tool loads with some files — and its step that works on a kind names that kind's file. No rule stands in two of its files, and no file of a kind holds a rule another kind needs: such a rule stands in its `SKILL.md`, or in a file a step names as WAY-256 gives, or, once such rules are so many that the work on one kind reads mostly the rules of others, in one shared file each such step names directly. No file of a kind points to another file.

- **Scope:** instruction-files

### WAY-418 — What does a change do with a warning of the script that checks the instruction files?

The product keeps the script that checks its instruction files at no warning: a change that adds a warning corrects the path or names it where the script does not read it, as it corrects an error. A warning of the script in a run on the head of the change is a finding of the review of the whole change, Important and within the task's scope, with no comparison with the base.

- **Scope:** instruction-files, task-cycle, installation

### WAY-127 — How does a session working on the-way itself reach the-way's skills?

A session working on the-way itself reaches each skill of the-way, which a human starts, as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on as the next paragraph gives. No global link reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in itself.

The header of each entry point holds `disable-model-invocation: true`, so that Claude Code offers the model no skill of the-way, in the-way itself or in a product that carries it as `.the-way`, and a human starts a skill with the command `/the-way-<name>`. In the-way itself a skill hands another the-way skill on by reading that skill's `SKILL.md` from the checkout or worktree the session works in, never by calling it, each entry point giving the path of every skill; in a product a skill hands another on as the project skill with the `the-way-` prefix, through the product's own entry point that the installer writes.

- **Scope:** agent-instructions, elements-common, project-level, task-cycle, decisions, invariants, glossary, part-map, environment-facts, installation, instruction-files, foundation-review, product-guidelines

### WAY-256 — Where does a fragment of a skill stand?

A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one variant of the skill needs, or only one step that some uses of the skill pass by, stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps, the pointers, every step until records of sessions a person can open, those of Claude Code and Codex, show that part of the uses since the step stood in the skill pass it by — also where no record exists — and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file.

A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines, task-cycle

### WAY-265 — Where is the file of a variant named, when a step's file points to it?

In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines, task-cycle

### WAY-368 — Which agents run the stages of a task cycle in Claude Code?

In Claude Code, a task cycle dispatches the one author of a change without a plan as an agent of the type `the-way-author` and every other stage agent as an agent of the type `the-way-stage`, two types of the-way's own that give their agent every tool of the session except the skill tool. Each type has a body of its own saying what it is, and only the type of the one author has the prompt cache lifetime that WAY-255 gives that agent. A stage agent reaches each method, and each skill a method names, as a file by its path, never by calling a skill; the installer writes the definitions of the pinned commit into a product, replacing and deleting only its own files, and the copies a session on the-way itself loads are generated from them and tracked.

The agent types of a task cycle start with the instruction files that Claude Code loads into an agent of the session, the user's and the product's; no definition of a type sets the field that starts an agent without them.

- **Scope:** task-cycle, installation, agent-instructions

### WAY-370 — What does a task cycle do where the session has none of the-way's agent types?

Where the session has none of the-way's agent types, because the harness is not Claude Code or the session started before Claude Code could load them, the task cycle dispatches each stage as it would without them and writes in its record that the stage ran without its type. The-way defines no agent types for Codex.

- **Scope:** task-cycle, installation

### WAY-324 — How does a product check the files it tracks for private paths and notes?

A command of the-way checks the files git tracks in the repository where it is run and skips the files that the sentence of the invariant named by its argument lists. A product whose repository is public adds the check with an invariant of that kind, whose method is `test`, and a short test that runs the command with the identifier of the invariant and cites it; the test of the invariant `tracked-file-private-paths` in the-way runs the same command and keeps no list of its own. Every text between backticks in the sentence names a file the command skips, and a name of a file that git does not track is an error.

- **Scope:** task-cycle, installation

### WAY-167 — Where do a product's guidelines stand, and what are their files named?

A product's guidelines are written by hand and stand outside its foundation, in the directory `guidelines/` at the root of its repository: a file `guidelines/<discipline>.md` for each discipline of work on the product it keeps guidelines of, save the styleguide and coding disciplines. The guidelines of the styleguide discipline stand in a file `guidelines/styleguide-<part>.md` for each user interface of the product, `<part>` being the identifier of the part of the product's map whose files draw that user interface; those of the coding discipline stand in a file `guidelines/coding.md`, which holds the product's standing checks, the rules of the whole of its code and a table naming each other file of the discipline with when to read it, and in a file `guidelines/coding-<kind>.md` for each kind of code that has an exemplar, which holds that exemplar and its rules, `<kind>` being the identifier of the kind that the decision designating that exemplar gives. The directory `guidelines/` belongs to the part of the product's map whose files direct whoever carries out its tasks, as its instruction files and skills do.

- **Scope:** product-guidelines, installation

### WAY-212 — How does a product's instruction file lead to its coding guidelines?

A product's root `AGENTS.md`, outside the block the-way's installer writes, points to its coding guidelines by one line naming `guidelines/coding.md` by its path in backticks with the condition of changing the product's code, written as the skill of `instruction-files` gives a pointer, and no line of it names a file `guidelines/coding-<kind>.md`. Each such file is named instead by a row of the table of `guidelines/coding.md`, by its path in backticks with the condition under which to read it, such as adding or changing a file of its kind.

- **Scope:** product-guidelines, instruction-files

### WAY-254 — Where does the command of a mutation tool stand?

The command that runs a product's mutation tool stands in the rule of mutation testing of the product's testing guidelines (WAY-252), and no CI configuration, recipe of a level or instruction file names it. In the area of the command of a product's mutation tool this decision prevails over WAY-16.

- **Scope:** product-guidelines, task-cycle, instruction-files

### WAY-379 — Does the-way adopt the template of the coding discipline for its own code?

The-way adopts the template of the coding discipline for the code of each part named in *Scope*: its coding guidelines stand in the file `guidelines/coding.md`, with a file `guidelines/coding-<kind>.md` for each kind of code that has an exemplar, and the rules of the template bind its code through the decisions of this log that adopt them or depart from them. The-way departs from the template only by a decision of this log that gives the reason. The *Scope* names every part of the-way's part map that holds Python code, and a change that gives a part Python code, or adds a part that holds it, adds that part to this decision's *Scope*.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-380 — Which linter checks the-way's code, and which of its rules block a change?

Ruff 0.17.1 checks the code of the parts that WAY-379 names, tests included, with the default set of that version, which the environment fact `ruff-default-rules` gives, with no preview rules and for the target version `py314`. The rules that block a change are the default set less the 18 rules `UP031`, `ISC004`, `PLW1510`, `RUF100`, `FURB167`, `FLY002`, `I001`, `B023`, `UP017`, `SIM117`, `UP012`, `RUF015`, `SIM102`, `C419`, `RUF012`, `SIM114`, `SIM905` and `SIM115`, which stand among the examples of the coding guidelines. A comment in the code that turns a rule off has no effect, a fault of one file is fixed in that file, and turning a rule off for the whole of the-way, or moving a rule between the blocking rules and the examples, is a change of this decision.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines, repository

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

### WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?

`task-cycle/remove_merged_worktrees.py` is the exemplar of the kind `repository-changer` of the-way's code, and a script of the kind changes neither a file that the repository tracks, other than a report that the human names with `--report`, nor a working directory without `--apply`, or where the confirmation is declined.

- **Scope:** task-cycle, elements-common, installation

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

### WAY-401 — What does the-way deliberately not test?

The-way does not test automatically what an agent does when it follows a skill: its tests check the form of the texts of the skills and their consistency, and the behaviour of the agents is checked by the human's review of a cycle at the merge and by the audit of the process, never by the gate. The category is tested again when an error of an agent's behaviour repeats that the audit does not catch before the merge.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

### WAY-402 — Does the-way adopt a mutation tool?

The-way adopts no mutation tool and departs from the rule of mutation testing of the template of the testing discipline, so `### Mutation testing` of its testing guidelines reads `none — WAY-402` and the author of a change checks its tests in every part by mutating the code in their head (WAY-253). A mutation tool enters the-way, for the parts whose complexity lies in computation, when an error passes after a merge in such a part for want of an assertion.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, product-guidelines

## Listed by heading alone

