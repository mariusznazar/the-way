# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 33. Listed by heading alone: 127.

## Listed in full

### WAY-33 — What does the author of a foundation change search for?

When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches — those that name the entry or that it names, and those no written link joins to it — and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human. The search is not repeated before the merge and leaves no record.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle, agent-instructions

### WAY-150 — How do the-way skills choose which product foundation material to read?

The-way skills read a product's foundation selectively: whoever selects names the parts the work touches from the files it changes through the part map's rules for assigning files, or, where the work names no file yet, from the responsibilities it changes; finds by a touched part's identifier the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds the invariants a test the work alters cites, the decisions whose sentence such a test holds by a line `decision:`, the decisions the task's *Decisions in play* or the work's source names, the touched parts' entries of the map and the entries these link to as far as the work needs. Of the decisions it finds by *Scope*, by a line `decision:` or as the task or the work's source names them, whoever selects reads the index and opens whole only the decisions the work changes, goes against or proposes another answer to — that one with its rejected options — those the task or the work's source names, those whose sentence a test the work alters holds by a line `decision:` and those whose binding sentences leave open what the work has to do; each other entry it selects — an invariant, an entry of the map of a touched part, or an entry, a decision included, that these or the decisions of the index link to as far as the work needs — it reads whole, and it reads more entries where relevance is uncertain and a whole file only where it is short; the reviewer of the whole change reads the index of its whole selection and states in its report how many decisions it read whole. The selection is neither recorded nor compared with every *Scope* of the log, and the search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep their domain.

The index of a selection of decisions is no file of the repository: a script of the-way writes it on demand into a file the agent names, and it gives for each selected decision its number, its question, its binding sentences and its *Scope*.

In a decision log divided into topical sections, whoever selects picks from the list of sections, by each one's heading and sentence, the sections of the work's topics, whose decisions take the place of those found by *Scope* in the selection whose index it reads, and it runs through the questions alone of the decisions outside those sections whose *Scope* names a touched part and opens whole each whose question points to a bearing on the work. In a log without topical sections the decisions are selected by the parts the work touches, and their index takes the place of reading each of them whole, the decisions the first paragraph names being opened whole as it gives.

Outside the task cycle the agent doing the work selects its own reading, while in the task cycle the orchestrator selects for its own judgments and for each handoff, which names the foundation entries by identifier; the reviewer of the whole change selects for its own review, and an agent writing a foundation entry through an element's skill for the entry it writes; and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively — a search for an identifier or a word and a read of the passage found, never of a whole file of the foundation — naming each such reach in its report.

- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts, project-level, task-cycle

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form of the candidate table of the skills of the elements (`elements/common/skill/build_table.md`) with each settlement in the human's words and, in place of its kind, the place it goes to by the questions of the decisions template, and the task document keeps the rows the human accepts, one that goes outside the decision log included and those that repeat a choice the human made between ways shown included unless the human struck them, and, where the human chose among ways shown, each way not chosen, under the answer to its question or, for a choice made outside the task's questions, in the source of the row it settles; the agent refining the task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, or a settlement that goes to another place those questions give — a skill or an instruction file, the guidelines of a discipline, or the data or code of the product — and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate. The task's cycle writes each kept row whole in the place its column gives, in the same change as the code, in its foundation step, or in its return step where the foundation step missed it, one that no code makes true included, keeping its meaning and choosing its wording, and gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`; where that meaning cannot hold, or the entry needs any other value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft request rather than write another entry, and otherwise the entry's meaning is the one the human accepted with the row in the task document (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated becomes no second entry, the cycle tying the row to that entry and naming both in the request.

Where a row adopts a practice from outside the product, the refinement shows the human, among the ways of the question that settles it, the parts the practice leaves out, so that the row's source keeps them as ways not chosen and the decision's rejected options take them; where the source keeps none, the decision names what it takes from the practice in its binding sentences or its *Rationale* as WAY-100 gives and puts no left-out part in its rejected options. In this area this decision prevails over WAY-100, which asks a decision that adopts a practice to put what it leaves out in *Rejected*.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary, environment-facts

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the task's line in the backlog the product names (WAY-107) is no effect of the task, nor is the removal of the repository's own working directories that stand outside its directory (WAY-375). For the human actions placed in the cycle, the cycle does what the repository allows and opens a blocked draft request listing them, and the human performs them at the request; a human action the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle. The human places each human action the task document names while the task is refined, on the agent's proposal: before the cycle when the cycle's code needs its effect, such as an account, a key or a database, and in the cycle when it uses code the cycle writes, such as a deployment or a DNS record pointing to a new address.

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

Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads `cycle.md`, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it. The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest of the models that the session's settings allow, which the orchestrator takes from the list of allowed models (in Claude Code the setting `availableModels`; where the session has no such list, every model it offers) and never from the name of the strongest model of the family, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

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

### WAY-409 — What does a reviewer do about code of the product that passes a test without meeting the requirement?

A reviewer looks, in every code review of a task's cycle — of a slice, of the whole change, of a fix, of the commits of the return step, of the reconciliation with the target branch and of a correction — in the code of the product that the change touches, for code that passes a test without meeting the requirement the test stands for: a branch or a returned value made for the very input a test uses, the expected value of a test written into the code of the product, a comment that names a special case for a test, and a change to the outcome of a comparison that a test makes, with no change to the test, such as an overloaded comparison operator. A reviewer grades such a finding Important at the least, so that it blocks (WAY-161), and only code whose branch, value or comparison exists to make a test pass is the finding; a special case that the requirement itself asks for is none.

The rule stands in the skill of the review and in no product's guidelines, so that it holds in every cycle, whether or not the product has adopted the template of the testing discipline.

- **Scope:** task-cycle

### WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?

Where a change alters what a screen shows, the screenshots that its author or reviewer shows the human are embedded as images in the description of the request, from a place that the foundation of the product settles outside the product's repository; the-way names no place. No file of a screenshot is committed to the product's repository, the copy of the task cycle's record that a commit adds to it included. A screenshot is evidence for the time of acceptance: the product may clear its place after a long time, and the images of old requests then stop showing.

Where a change alters what a screen shows and the foundation of the product settles no place for screenshots, the author inspects the screenshot as the author's check of a user-interface change gives and the request shows none: the section of its description for the human's decisions says that no screenshot is shown and why, and the cycle does not stop. A screenshot left unchecked for want of a settled way to the running product is reported as that check gives and needs no second item.

A screenshot that is shown to the human lies in the place the product's foundation settles for screenshots and not in the agent's directory of working copies, and for it this decision prevails over WAY-373, which keeps its reach over every other screenshot and every copy made to check something.

- **Scope:** task-cycle, project-level

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
- WAY-02 — How does whatever depends on an entry refer to it?
- WAY-04 — What makes up a product's foundation?
- WAY-07 — How is a foundation entry changed?
- WAY-17 — Which links between foundation entries are mandatory?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-05 — How is a decision entry written?
- WAY-12 — How is a decision checked?
- WAY-18 — How is a product's decision log kept?
- WAY-19 — How are decisions numbered?
- WAY-21 — What is a decision's scope?
- WAY-22 — Is a rule a decision or an invariant?
- WAY-26 — How are trade-off principles and non-goals written?
- WAY-29 — How is a decision recovered from an existing product written?
- WAY-36 — Is a rule a decision or does it belong in a plan?
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice?
- WAY-14 — Who accepts a decision?
- WAY-24 — How is a decision that rests on a prediction reviewed?
- WAY-25 — What settles a collision between two decisions?
- WAY-30 — What happens when a change contradicts a decision?
- WAY-114 — What does a human accept of an entry, and when?
- WAY-313 — What is a decision of the foundation to the refinement of a project or a task?
- WAY-314 — Which act of the human consents to a change of a decision that refinement shows?
- WAY-315 — From when does a decision of the foundation bind the work on a task?
- WAY-35 — What does an element's skill hold?
- WAY-113 — How does an agent of the-way ask a human decision?
- WAY-120 — How does the-way critique an agent's proposal?
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
- WAY-16 — How are the checks of invariants run?
- WAY-38 — In what are the scripts of the-way written?
- WAY-55 — Which part of the process holds the gate?
- WAY-63 — What is an invariant's result, and when does the command running the tests fail?
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?
- WAY-160 — How does the task-cycle orchestrator run the finished change's gate?
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?
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
- WAY-355 — Which task fixes a defect found after a merge?
- WAY-227 — Where does the human meet a task cycle's work?
- WAY-287 — What does a request put before the human for a decision?
- WAY-288 — In what language is a request's description written?
- WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?
- WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?
- WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong?
- WAY-300 — When does a request tell the human that the foundation waits for a review?
- WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?
- WAY-309 — How does the cycle find the private paths and notes in what it publishes?
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?
- WAY-324 — How does a product check the files it tracks for private paths and notes?
- WAY-337 — How is the cost of a cycle measured?
- WAY-339 — When do the measures of the audit stop being comparable?
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
- WAY-404 — Who marks a contradiction with the settlements, and where does the audit of the process read it from?
- WAY-405 — How does the audit of the process read the reason of a discarded attempt?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-213 — How do the agents of a task's cycle read the product's guidelines?
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?
- WAY-174 — How do the-way's skills of guidelines ask the human?
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
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-397 — Which test is the exemplar of the level files test of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
