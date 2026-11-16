# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 21. Listed by heading alone: 95.

## Listed in full

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives no line `Error:`. Where a script whose purpose is to check the form of a file reads a copy of the file from the commit the branch left the main branch from, a field it needs for a comparison and finds missing from that copy is listed by a line `listed:` that names the entry and the field, with no error and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*. The command that counts the audit, where a table of weights or a table of the costs of an occurrence in the register of problems lacks one of its levels, writes its result, gives the values that depend on the table as unknown and ends with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither of the two columns of the cache writes in its detailed section, that command reads the report as an earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and priced as input, an approximation, and no value unknown for the missing columns, while a stage report that has one of the two columns and not the other has a missing field, with the line `Error:`. Where the locations file has no entry `repository` under `the-way`, no field is missing and that command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

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

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest of the models that the session's settings allow, which the orchestrator takes from the list of allowed models (in Claude Code the setting `availableModels`; where the session has no such list, every model it offers) and never from the name of the strongest model of the family, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class available that fails, or a retry that fails, stops the cycle.

The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every other reviewer work on no class cheaper than the orchestrator's, and the review of the whole change and the review of the return step work on the strongest class available.

- **Scope:** task-cycle

### WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?

Where a slice of a plan adds to a function or a file that stands over the threshold of the product's rule of size, the plan begins with a slice that moves a part of that function or file out without a change of behaviour, writes the choice in its table of choices, and puts the slice that adds after it. The author of a change without a plan makes that move the first commit that changes the code. Such an addition is a choice of how to make the change and no open design choice, so it gets no spec (WAY-135).

- **Scope:** task-cycle

### WAY-10 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation has no assessment of its own, in a product as in the-way itself: an agent that did not make the change reviews the whole change, its foundation entries and invariant tests included, against its task and the foundation, and a human reads the section of the request's description for the human's decisions and accepts the change by merging the request.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, task-cycle, agent-instructions

### WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?

In the review of the whole change on either route, a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope, and a Minor finding that the review lists and the reviewer has not marked so is fixed before the request opens — in the fix that runs for the blocking findings or, where none blocks, in one fix of its own that WAY-162 bounds. A finding the reviewer has marked as outside the task's scope — a line of its list of what it declined to judge, or a finding it describes as going beyond the task — is not fixed, whatever its grade, and the request lists those findings in an item of their own and, in another, the Minor findings that no fix made — those of the code reviews after the review of the whole change, those of a slice review that the review of the whole change does not list, those a fix left, and those of a fix that WAY-162 reverted — each with the reviewer's words and its place in the code, while the human decides which findings outside the scope become new tasks and creates them. The orchestrator moves no finding from one of these kinds to another.

- **Scope:** task-cycle

### WAY-162 — How does a code review of a task's change end when its findings block?

In every code review of a task's cycle — of a slice of its plan, of the whole change, of the return step's commits, of the reconciliation with the target branch and of a change made for the human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and one review of that fix, and a new Critical or Important finding in the fix itself counts as one that remains. Where a blocking finding remains after that review of the fix, no third round runs, the orchestrator does not rule on it, no further slice is made, and the cycle opens a draft request marked `blocked` that lists each remaining blocking finding with its place in the code and its reason, what the fix tried, and the time, models and tokens the cycle has used so far, from its record of stages, with the number of review rounds.

Where the review of the whole change leaves no blocking finding and lists Minor findings that WAY-161 has the cycle fix, one fix takes them in and one review of that fix follows, and where that review finds a new Critical or Important finding in the fix, the cycle reverts the fix's commits with a commit of its own, so that they stay in history, runs no third round and opens the request, not blocked, on the code the review of the whole change accepted, the request listing the Minor findings the fix tried and the new finding with its grade and as the review of the fix found it. In the code reviews after the review of the whole change, and for a Minor finding that remains after a fix, the findings that do not block go unfixed to the request's lists as WAY-161 gives them.

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

### WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it?

The-way gives a template of a register of problems, which holds for each problem the cycle it comes from, its class, its weight, the cost of its occurrence, the issue it belongs to — the one matter that like problems of several cycles make — and that issue's fate, the fix of an implemented issue included. A user's own tool fills the register and the user adapts the template to their own needs; the audit reads the register that an entry of the user's locations file names and gives no problem a class, a weight or a cost of an occurrence itself.

- **Scope:** process-audit

### WAY-337 — How is the cost of a cycle measured?

A cycle's cost is two numbers, neither divided by a measure of the size of the task: its cost at constant prices, computed from a price list of models that carries a date, and the share of that cost spent in fix rounds, a fix round being the fix of a review's findings and the review of that fix. A turn of an agent serves a fix round when the message that dispatches or resumes it names the round's findings file by its path in the cycle's `reports/`, which only the messages of that fix and of the review of that fix do, and the cycle's record names each round by that path. The share is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and the stages cannot tie each round to the turns that served it.

- **Scope:** process-audit, task-cycle

### WAY-339 — When do the measures of the audit stop being comparable?

A new series of the cost of cycles, the two numbers of WAY-337, starts only with a new price list or with a change of the script that measures the cost, `task-cycle/cycle_stages.py`; a new series of the count of remarks starts wherever a series of the cost starts and also with a change of the form of a stage report, of the list of classes or of the instructions of the reviewer. The measures of how a cycle's agents use context and the prompt cache and the times of the gate form series of their own: a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process, whose output gives the time of each directory; no change of the instructions of the cycle, the reviewer's and the author's included, starts one. The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; and where a cycle's own change changes a tool that measures — the script that measures the cost, the script that counts the measures of context and cache use, the script that records the gate times or the test runner of the process — the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them (the file of that tool is not read for that cycle, so no field of it is missing and no line `Error:` is given for it), and its other measures as they stand under the version it ran on.

The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again, and, for each agent of the cycle, the bytes of the decision log and of the index of decisions that entered its context and how many times each entered it — are counted by a script of their own into a file of their own in the cycle's record, and are never columns of the stage report of the cycle's stages, the table of its tokens by model. The one exception is that this report holds, for each stage and model, the tokens written to the cache at each lifetime, as an input of the cost (WAY-337) and not as a measure of cache use: the script that measures the cost counts them, the script of the other measures counts the same tokens for its own file, and neither takes its figures from the file of the other.

- **Scope:** process-audit, task-cycle, gate

### WAY-350 — Which runs of the gate does the audit compare between versions of the process?

The script that runs the gate records, at each run, how many other gate runs by the script were going at the same time on the machine, from a registry that the script keeps in the user's own directory, outside every repository: an empty file for each run, made when the run starts and marked as ended when it ends, a run that has not ended counting for at most six hours, an ended one kept for a day and an entry whose times cannot be, such as an end in the far future, deleted and counted for nothing. The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.

- **Scope:** process-audit, task-cycle

### WAY-385 — How large may a function and a file of a script of the-way be?

A function of a script of the-way has at most 80 lines, counted with the functions nested in it, and a file of a script has at most 1000 lines, in each part that WAY-379 names; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception. A test of the suite counts the lines with the `ast` module of the standard library, runs apart from the run of the linter and, where it fails, names every function and file over a threshold with its size (WAY-361).

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
- WAY-03 — Who may change an invariant test, and when?
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
- WAY-164 — What does the author of a change check of its own work before review?
- WAY-255 — How does an agent of a task's cycle wait for a command that runs long?
- WAY-260 — What does each task-cycle stage report about what it could not find or understand?
- WAY-261 — What does a task cycle report about a check that fails and passes when run again?
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
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
- WAY-361 — How does the review of a change get the sizes of functions and files from a product?
- WAY-238 — At which level does a test stand, and who chooses it?
- WAY-253 — Who runs a mutation tool in a task's cycle, and what does the author check in its place?
- WAY-254 — Where does the command of a mutation tool stand?
- WAY-379 — Does the-way adopt the template of the coding discipline for its own code?
- WAY-380 — Which linter checks the-way's code, and which of its rules block a change?
- WAY-382 — Does the-way's code get an automatic formatter?
- WAY-383 — Does the-way's code get an audit of its dependencies?
- WAY-384 — Does the-way adopt the six rules of the coding template on failures and logs?
- WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?
- WAY-387 — Which file is the exemplar of the kind `measuring-report` in the-way's code?
- WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?
- WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-397 — Which test is the exemplar of the level files test of the-way's tests?
- WAY-400 — Which test is the exemplar of the level e2e of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
