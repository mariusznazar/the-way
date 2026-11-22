# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 47. Listed by heading alone: 128.

## Listed in full

### WAY-05 — How is a decision entry written?

A decision entry opens with one to three binding sentences that answer its question — in the present tense, describing a state that is to be true, concrete enough to check — and one paragraph of one to three binding sentences for each part of another question that it answers, and may carry a further such paragraph for each part of its own question that it sets apart, no paragraph of binding sentences running past 300 words and the binding sentences of one decision together not running past 600, followed by fields a script or an agent reads, then rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count — a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound — nor what the process's own tools do or lack today, and does not tell how the decision was reached. A field stays in the template only while someone or something reads it, and what a decision forces on later work stands in a binding sentence or a field, never in prose. An example in `elements/decisions/` names a decision of the log by its number instead of copying it.

The check of the foundation reports as an error a paragraph of binding sentences that runs past three sentences or past 300 words, or binding sentences that together run past 600 words, in a decision that a change adds or whose binding sentences it alters, a different division of them into paragraphs included; any other decision over a limit stands in a list the check prints, and the list stops no change.

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

A number stands for the question a decision answers, carries the product's prefix and is given in the order entries are written; a new question gets the next free number, a question independent of every existing entry included, while a part of another question that an existing entry answers, or a part of its own question that it sets apart, is a sentence of that entry where it cannot change without changing that entry. A new answer to a question the log holds rewrites that question's entry. When a new decision answers a question that an older one answered in passing, the sentence moves to the new decision, and the older one loses it in the same change.

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

### WAY-25 — What settles a collision between two decisions?

Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a chain, and two decisions that narrow each other are an error. A collision between two decisions with no precedence recorded is never settled silently by the agent that meets it. Where what the human accepted gives the outcome and the change may write the decision that prevails, the change records the precedence in that decision, and its request names it with the passages of what the human accepted that give the outcome, for the human to accept at the merge (WAY-114); otherwise the agent stops and asks.

- **Scope:** decisions, task-cycle

### WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?

An invariant's *Rests on* names every environment fact holding a condition that decides whether a commit makes its sentence true, and no other fact. A fact holds such a condition when, read otherwise, it would change whether some commit makes the sentence true, or change a value the sentence copies from it. A fact that is only a reason for a decision the invariant derives from stands in that decision's *Based on* alone; a fact stands only while an invariant's *Rests on* or a decision's *Based on* names it, and the change that removes the last such name withdraws it.

- **Scope:** invariants, decisions, environment-facts

### WAY-82 — How does an environment fact keep up with what its source says?

An environment fact names no method and no status, no test cites it, no check of it runs, on a change or by a clock, and nothing fails when the world moves. A fact changes when someone finds that its source no longer says what its sentence says, or that a newer edition the product stands on says otherwise; the change that rewrites or withdraws it corrects every entry naming it (WAY-33). An announced revision changes nothing until the new edition is out, and neither a fact nor a decision citing it names a date or condition for its review (WAY-24).

- **Scope:** environment-facts, invariants, gate, task-cycle

### WAY-84 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can open it, a host's access rule — is an environment fact, its source the place where that state is shown, or, where no page open to a reader shows it, a reading. A choice of such a setting is a decision only where the product declares it, and that decision rests on the fact. A fact about the visibility of a repository the product links to names that one repository.

- **Scope:** environment-facts, decisions

### WAY-85 — How is a finding of a study written as an environment fact?

A finding of a study stands as an environment fact saying what the study found, its source citing the version of the paper, and the models the study measured named as the study names them, in the sentence or in a passage its source quotes. That the agents of this process behave the same is no part of the fact. A decision citing a finding none of whose measured models comes from a publisher whose models the process's agents run on says in its rationale that it takes the finding across publishers.

- **Scope:** environment-facts, decisions

### WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

A decision's *Based on* quotes every source outside the product that the decision rests on with its address, the place in it, the passage word for word and the date it was read; once the environment facts element has entries, it names instead a fact entry, by its identifier alone, for every citation that, once it stopped being true, would call the decision into question — a finding about agents or models, the behaviour of a tool the process uses. A measurement that the product's own people made — its author and its agents — and whose record a reader of this repository cannot open is no such citation: its result stands in the decision's *Rationale*, or in its *Rejected* where it weighs a way not chosen, with what was measured and under which conditions; that prose says that the measurement is the product's own and that its record is not open to a reader of this repository; and no environment fact entry is written for it.

- **Scope:** decisions, environment-facts

### WAY-44 — What assigns a file to a part?

Every file git tracks belongs to exactly one part of the map, by path patterns that git itself matches, each naming a directory or one kind of file — every invariant test, say — rather than listing a directory's files one by one, except the files at the root of the repository, which is the directory of no part and whose files the map names one by one; a file that no pattern matches, and a file that two parts claim, is an error of the check of the foundation, unless the map lists that file as left out on purpose, and so is a pattern of a part's *Files* or *Trust boundary* that matches no file git tracks. Tests belong to the part they test and generated files to the part of their generator; the files that serve the whole repository — the lockfile and the build configuration — are a part of their own; the files that serve the tests of several parts are another, which its sentence describes as such with no field of its own, and which the tests of every part may import while code that is no test may not; and the files that only direct whoever carries out its tasks — instructions for agents, skills, hooks and the configuration of agents' tools and of CI — are another. For a file that collects entries about many parts, the parts a change touches follow from the entries it adds or changes, not from the part the file itself belongs to.

- **Scope:** part-map, agent-instructions, task-cycle

### WAY-48 — How is a trust boundary recorded?

A trust boundary is recorded at the part that holds it, as a pattern of the code files which take in what the product does not control — data from the network, keys, the deployment, files that come from outside the product, such as one on the user's disk — and never at a script that only checks the product's own files. An exchange with the external context records its direction and marks what comes in as untrusted. A change that touches the files of a boundary is checked for crafted input, and its review is aimed at that risk.

- **Scope:** part-map, task-cycle

### WAY-52 — What is generated from the part map for an agent?

Nothing is generated from the part map for an agent: an agent reads the entries of the parts its change touches, and no overview of the repository is generated for it.

- **Scope:** part-map, decisions

### WAY-53 — How is a derived file compared with what its generator produces?

A derived file is identical to what its generator produces on the same commit, except for values the file itself declares as varying between runs.

- **Scope:** decisions, part-map, invariants, gate

### WAY-225 — What in a product's foundation is derived rather than written by hand?

What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state. Rules are written by hand: what is allowed and what the product promises, which the code cannot show, and a dependency of a part that the code holds and the part map does not allow is recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies of a part to fit the code.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts

### WAY-160 — How does the task-cycle orchestrator run the finished change's gate?

The final gate of a task cycle is the product's gate on the tree that goes into the request, and the request gives its command and exit code, or the CI run's, and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run on the cycle's own system is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it. Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the CI run on the head pushed last is the final gate, and the orchestrator runs no full gate itself at the end of the cycle or after the merge with the target branch; the run on the base of the task branch and the run after the pin of the-way moves stay the orchestrator's own, since no request stands then, and where CI runs on no request, or the request is left blocked for unfinished code, the orchestrator runs the gate itself on the tree that goes into it, save where that tree is one already run.

The orchestrator waits for the result of the CI run on each head it pushes to the request, a correction's included, treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review and the wait for the run on the new head, save a check outside the task's scope that passes when run again, which WAY-261 governs — and puts the result into the request's description. Where the run gives no result within 30 minutes of the push — it does not start, it stands in a queue or the host does not answer — the orchestrator runs the gate itself on the tree of that head, and the description says that CI did not answer and that the gate ran on the cycle's own system; a request the cycle leaves blocked for unfinished code is out of that wait, its description saying that the result of the CI run stands on the request's page and was not waited for. Where CI is the final gate, the cycle's record says so before it is copied, and names the request whose description gives the result, so that the next cycle takes the list of failing tests from there.

- **Scope:** task-cycle

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

### WAY-136 — When does a task's change need a plan, and who makes and reviews it?

A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split.

A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own and names, for each blocking finding, the slice it comes from or that it comes from none, while the review of a one-author change or of a plan's only slice is the review of the whole change; and that review also checks coverage of the task, every row of its *Settlements to record* and every projected entry it carries; where the slices that have no review of their own are more than one reviewer of the whole change can compare with their sources, the orchestrator may, by its own judgment and not by a measure, dispatch reviews of groups of them in the plan's order, as for a slice with a review of its own, and it records the grouping and its reason.

- **Scope:** task-cycle

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads `cycle.md`, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it.

The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest of the models that the session's settings allow, which the orchestrator takes from the list of allowed models (in Claude Code the setting `availableModels`; where the session has no such list, every model it offers) and never from the name of the strongest model of the family, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class available that fails, or a retry that fails, stops the cycle.

The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every other reviewer work on no class cheaper than the orchestrator's, and the review of the whole change and the review of the return step work on the strongest class available.

- **Scope:** task-cycle

### WAY-164 — What does the author of a change check of its own work before review?

Before its work goes to review, the author of a one-author change names the requirement of the task, and the executor of each slice the requirement of its slice read against the passages of the task its handoff gives, that its work most likely does not meet, writes a check that would catch that, and states in its report which requirement, which check and what the check showed. The review that judges the work — a slice's own review where it has one, otherwise the review of the whole change — reads that report, and the request lists what each such check showed among its test evidence.

- **Scope:** task-cycle

### WAY-255 — How does an agent of a task's cycle wait for a command that runs long?

An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps its prompt cache — a container build, a mutation run, a test suite a check names — by running it in the background and reading its output between waits each shorter than that lifetime, never in one wait past it, and ending its turn only after the command has ended and it has read its result; in Claude Code a subagent's cache lives five minutes by default, so each wait stays under about four. The one author's cache lives an hour, which the author's type sets (WAY-368), and its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits. Where the harness states no cache lifetime, the agent waits as the harness allows.

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

### WAY-339 — When do the measures of the audit stop being comparable?

A new series of the cost of cycles, the two numbers of WAY-337, starts only with a new price list or with a change of the script that measures the cost, `task-cycle/cycle_stages.py` with the module `task-cycle/stage_transcripts.py` that it imports; a new series of the count of remarks starts wherever a series of the cost starts and also with a change of the form of a stage report, of the list of classes or of the instructions of the reviewer. The measures of how a cycle's agents use context and the prompt cache and the times of the gate form series of their own: a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process, whose output gives the time of each directory; no change of the instructions of the cycle, the reviewer's and the author's included, starts one.

The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; and where a cycle's own change changes a tool that measures — the script that measures the cost, the script that counts the measures of context and cache use, the script that records the gate times or the test runner of the process — the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them (the file of that tool is not read for that cycle, so no field of it is missing and no line `Error:` is given for it), and its other measures as they stand under the version it ran on. The audit shows each series as an image of all its cycles — what its kind carries, the answer Q3 and the fall standing only where two groups meet (WAY-417) — and, inside it, as a comparison before and after a change: the cycles on the versions that hold the change against those on the versions that lack it, both groups of that series, the version a cycle ran on, never its date, deciding its group; for the times of the gate both take only the runs that WAY-350 compares. That comparison is made for each fixed issue of the register of problems with a fix commit, and for no other change.

The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again, and, for each agent of the cycle, the bytes of the decision log and of the index of decisions that entered its context and how many times each entered it — are counted by a script of their own into a file of their own in the cycle's record, and are never columns of the stage report of the cycle's stages, the table of its tokens by model. The one exception is that this report holds, for each stage and model, the tokens written to the cache at each lifetime, as an input of the cost (WAY-337) and not as a measure of cache use: the script that measures the cost counts them, the script of the other measures counts the same tokens for its own file, and neither takes its figures from the file of the other.

- **Scope:** process-audit, task-cycle, gate

### WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?

`task-cycle/gate_times.py` is the exemplar of the kind `command-runner` of the-way's code, and a script of the kind that wraps one command ends with that command's exit code unchanged.

- **Scope:** task-cycle, gate

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
- WAY-07 — How is a foundation entry changed?
- WAY-17 — Which links between foundation entries are mandatory?
- WAY-54 — Where does the value of a field in a template come from?
- WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?
- WAY-14 — Who accepts a decision?
- WAY-24 — How is a decision that rests on a prediction reviewed?
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
- WAY-95 — Which words take a glossary entry?
- WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?
- WAY-99 — How does one word keep one meaning in the foundation?
- WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?
- WAY-16 — How are the checks of invariants run?
- WAY-38 — In what are the scripts of the-way written?
- WAY-55 — Which part of the process holds the gate?
- WAY-63 — What is an invariant's result, and when does the command running the tests fail?
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?
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
- WAY-134 — How does a task carry what its refinement settles for the foundation?
- WAY-140 — How does a task change something outside the product's repository?
- WAY-355 — Which task fixes a defect found after a merge?
- WAY-11 — How does a task end?
- WAY-13 — What sets the weight of a task's process?
- WAY-125 — Which methods does the autonomous task cycle use?
- WAY-135 — When does a task's cycle write a spec?
- WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?
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
- WAY-350 — Which runs of the gate does the audit compare between versions of the process?
- WAY-404 — Who marks a contradiction with the settlements, and where does the audit of the process read it from?
- WAY-405 — How does the audit of the process read the reason of a discarded attempt?
- WAY-416 — What does the command that counts the audit do when a file it reads lacks a field it needs?
- WAY-167 — Where do a product's guidelines stand, and what are their files named?
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?
- WAY-212 — How does a product's instruction file lead to its coding guidelines?
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
- WAY-391 — Which file is the exemplar of the kind `shared-module` in the-way's code?
- WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?
- WAY-393 — At which levels do the tests of the-way stand?
- WAY-394 — Where does a test of the-way take its expected value from?
- WAY-395 — Which fields of a recipe of a level of the-way's tests bind?
- WAY-397 — Which test is the exemplar of the level files test of the-way's tests?
- WAY-399 — Which test is the exemplar of the level repository test of the-way's tests?
- WAY-401 — What does the-way deliberately not test?
- WAY-402 — Does the-way adopt a mutation tool?
