# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 21. Listed by heading alone: 104.

## Listed in full

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

A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split.

A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own and names, for each blocking finding, the slice it comes from or that it comes from none, while the review of a one-author change or of a plan's only slice is the review of the whole change; and that review also checks coverage of the task, every row of its *Settlements to record* and every projected entry it carries; where the slices that have no review of their own are more than one reviewer of the whole change can compare with their sources, the orchestrator may, by its own judgment and not by a measure, dispatch reviews of groups of them in the plan's order, as for a slice with a review of its own, and it records the grouping and its reason.

A slice of a plan may leave tests of the product failing that a later slice of the same plan makes pass, where its *Goal* names each such test file and the slice that makes it pass and the *Checks* of that slice hold the same test. The executor of a slice decides whether a failing test is the fault of its slice by a measure on the slice's base, running there only the tests that failed for it: a test that fails on the base too is no failing check of the slice, save a test of the slice's own *Checks*, and a test that passes on the base and fails after the slice is a failing check of the slice, save one that the slice's own *Goal* announces it leaves failing with the slice that makes it pass; its report gives the base result of each such test.

- **Scope:** task-cycle

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads `cycle.md`, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it.

The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest model the session actually gives, fixed as the next paragraph says, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

In every cycle, before its first dispatch of the strongest class, the orchestrator fixes that model by a probe: it dispatches a small agent on the candidate model and reads from the session record the model that agent worked on, the first candidate being the model the human named at the start of the cycle, which the probe checks like any other, or, where none was named, the strongest model the tool that dispatches agents offers, and the next candidate, where the agent worked on another model, the next model down. Every dispatch of the strongest class in the cycle runs on the model so fixed, the probe asks the human nothing (WAY-227), and the cycle's record gives the tries and the model each agent worked on.

An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class available that fails, or a retry that fails, stops the cycle.

The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every other reviewer work on no class cheaper than the orchestrator's, and the review of the whole change and the review of the return step work on the strongest class available.

- **Scope:** task-cycle

### WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?

Where the log of the target branch holds a number that a new decision of the task branch bears, the task branch, before it merges the target branch and in a commit of its own, renumbers all its new decisions in their order onto the next free numbers after the highest number that log holds, as an entry or as a withdrawn number, and never changes the number of a decision of the target branch. In that one pass it rewrites every reference to the renumbered decisions in the files of the branch and in the original of the cycle's record as the record stands before the reconciliation is entered in it; texts written afterwards, the rows that give the conversion of an earlier reconciliation and the human's remarks quoted word for word stay as they are. The rule holds for the reconciliation with the target branch before the request opens and for each merge of the target branch in a correction after review, on either route.

The conversion of the old numbers into the new ones stands in the row of the cycle record's events that records the reconciliation with the target branch, and in no other note of the record; a reconciliation that renumbers again adds its own row beside the earlier ones.

- **Scope:** decisions, task-cycle

### WAY-164 — What does the author of a change check of its own work before review?

Before its work goes to review, the author of a one-author change names the requirement of the task, and the executor of each slice the requirement of its slice read against the passages of the task its handoff gives, that its work most likely does not meet, writes a check that would catch that, and states in its report which requirement, which check and what the check showed. The review that judges the work — a slice's own review where it has one, otherwise the review of the whole change — reads that report, and the request lists what each such check showed among its test evidence.

- **Scope:** task-cycle

### WAY-255 — How does an agent of a task's cycle wait for a command that runs long?

An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps its prompt cache — a container build, a mutation run, a test suite a check names — by running it in the background and reading its output between waits each shorter than that lifetime, never in one wait past it, and ending its turn only after the command has ended and it has read its result; in Claude Code a subagent's cache lives five minutes by default, so each wait stays under about four. The one author's cache lives an hour, which the author's type sets (WAY-368), and its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits. Where the harness states no cache lifetime, the agent waits as the harness allows.

An agent that waits for such a command stops it where it has not ended 30 minutes after it started, the same for every product, and reports it as unfinished with the command and the last lines of its output in place of waiting on; the orchestrator enters the check that command stood for as one that did not run.

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

### WAY-406 — Who walks through the running product the behaviour that a change's tests do not cover, and for which changes?

The author of a change walks through the running product, after the code and before the review, the behaviour a user sees there that the change's tests do not cover, and states the walk in the report the review reads; in a change made from a plan, the executor of each slice that alters such behaviour walks through its slice, read against the passages of the task its handoff gives. The walk is required for every change of behaviour that the user sees in the running product — a screen, an answer of an API, a command in a terminal, data the product shows — and the author or the executor judges whether its change is one and says so in its report. The walk follows the method that the author's skill names, which takes its steps and the rules of the walk from the practices this decision's rationale names.

Where the audit of the process shows an error that the author or the executor let through at the walk, the walk moves to a stage of its own with a new agent; the fix of a review's findings does not repeat the walk.

Where the foundation of the product settles no way to the running product, the walk is not performed, with that reason in the report and in the description of the request, and the cycle does not stop; the author or the executor still draws up the cases from the requirements of the task and marks each as unchecked with that reason. A screenshot left unchecked for the same reason stands in the description with the walk as one item, not two.

- **Scope:** task-cycle

### WAY-407 — Who approves the cases of the walk through the running product before it is made?

No one approves the cases of the walk before it is made, and the cycle does not stop for them. The author of a change or the executor of a slice draws the cases from the requirements of the task, not from the code alone, puts the plan and its results into the report the review reads, and the human sees in the request what was not checked. The refinement of a task writes no list of inputs to try into the task document.

- **Scope:** task-cycle, project-level

### WAY-408 — What does the author or the executor do with a case of the walk that fell wrong?

The author of a change or the executor of a slice corrects each case that fell wrong before the review, and the correction gets a test at the lowest level that catches the error (WAY-239); each disagreement with the task is an error to correct, not a remark in the margin, and a case that fell wrong does not break off the walk. The report says what fell wrong, what was corrected and by which test.

An error outside the task's scope that the walk finds is reported and not corrected, and the description of the request puts each such error before the human, under *Fix or let through*, with the question whether to make a task of it, which merging lets through; in this area this decision prevails over WAY-289, under which the cycle puts before the human only what it judges will be felt.

- **Scope:** task-cycle

### WAY-410 — What does an agent do when a test contradicts the requirement, or when it cannot pass the test by general code?

An agent that makes a change and meets a test that expects what the requirement of the task rules out, or that it cannot make pass by code that meets the requirement for every input, writes no code for the input of the test and does not change the test: it commits what it has and returns to the orchestrator of the cycle a question that names the test, quotes the requirement and says what it tried. A test that checks behaviour the task expressly changes is no such contradiction, and the agent changes it, with its cause on the side of the requirement.

The orchestrator answers such a question only from the task, the spec, a decision or the sentence of an invariant, quoting the passage that settles it, and where none of them settles it opens a blocked draft request that holds the question under *Needed from you* and picks no reading of its own.

The executor of a slice that returns such a question gets no retry on a class higher, which narrows the retry of WAY-229; where no source settles the question, the blocked draft opens at once.

- **Scope:** task-cycle

### WAY-227 — Where does the human meet a task cycle's work?

The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under the task owner's delegation, never recording these as human approval, and brings the request to the human, the cycle's first point of human review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request.

- **Scope:** task-cycle

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
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?
- WAY-418 — What does a change do with a warning of the script that checks the instruction files?
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
- WAY-10 — Who assesses a change to an invariant test or to the foundation?
- WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?
- WAY-162 — How does a code review of a task's change end when its findings block?
- WAY-263 — Which foundation mismatches are Important findings?
- WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?
- WAY-363 — How does a reviewer grade a finding about the structure of code?
- WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?
- WAY-409 — What does a reviewer do about code of the product that passes a test without meeting the requirement?
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
- WAY-385 — How large may a function and a file of a script of the-way be?
- WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?
- WAY-387 — Which file is the exemplar of the kind `measuring-report` in the-way's code?
- WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?
- WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?
- WAY-391 — Which file is the exemplar of the kind `shared-module` in the-way's code?
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-397 — Which test is the exemplar of the level files test of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
