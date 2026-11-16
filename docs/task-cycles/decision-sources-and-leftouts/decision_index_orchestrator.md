# decision_index.py: index of the decisions of the log

Log: foundations/decisions.md
Listed in full: 73. Listed by heading alone: 0.

## Listed in full

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/`, the copies of the cycle's agent type definitions under `.claude/agents/`, the CI configuration under `.github/workflows/` and the directory `guidelines/` with the guidelines of the-way's own code and tests, which the map gives to `agent-instructions` (WAY-44, WAY-167), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; any other directory what the sentence of its part in the part map names. The entries in `foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, foundation-review, process-audit, task-cycle

### WAY-27 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the places where the work of the-way lies — the place of its tasks and the rules of that place, the register of problems and the results of the audit — which are no source of reasoning, and a file that needs one names it by an entry of the locations file of WAY-320, never by a path.

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

### WAY-102 — What is the-way for?

The-way is a process for work on a technology product in which a change of premises or direction is an ordinary step: it passes through the product's foundation and needs no memory of what is linked to what.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, relation-model, gate, installation, agent-instructions, instruction-files, repository, project-level, product-guidelines, task-cycle

### WAY-103 — Who is the-way for?

The-way is built first for its author and aims at anyone who builds a technology product and adopts the process for their own needs; the process is written for the agents that carry out the task cycle too.

- **Scope:** decisions, elements-common, task-cycle

### WAY-01 — What state does the foundation describe?

On the main branch, the foundation describes the product as it is — its rules, with each invariant the product does not yet meet marked violated (WAY-51) — and roadmaps and plans do not change it. A task that sets out to change the foundation makes that change on its branch in the product's repository, and the change reaches the main branch in the same merge as the code it describes; no entry the task calls for is left for a later task. When a task closes, the foundation again matches the current state.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle

### WAY-02 — How does whatever depends on an entry refer to it?

Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to it by that identifier alone, with no fingerprint and no version beside it, and names an entry the foundation holds. A fingerprint, where the process records one, is the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of a text encoded in UTF-8, taken after every run of spaces and line breaks is replaced by a single space and both ends are trimmed; nothing else in the text is changed before it is digested. The one reference that carries more than the identifier is the line `decision:` of a test that holds a sentence of a decision: it gives the number and, in straight double quotation marks, the start of that sentence — from where a sentence of the entry begins, three words or more, compared after every run of spaces and line breaks is replaced by a single space — so that a test whose sentence was reworded is found, while a reference anywhere else names a decision by its number alone.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, product-guidelines

### WAY-04 — What makes up a product's foundation?

A product's foundation has five elements, and the list is closed: invariants, decisions, a glossary of product terms, a part map, and environment facts. A new pattern enters the foundation only as a field or a rule of one of the five, and only when a mechanism keeps it without human memory: a test, a lint, a check that stops a merge, a mandatory relation or configuration.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts

### WAY-07 — How is a foundation entry changed?

A foundation entry of any element carries no version: it is edited in place, on the main branch as before it, and holds only its current wording; the decision log has one entry for each number, and git keeps the earlier wordings.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

### WAY-17 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional: a decision and an invariant name the environment facts they rest on, an invariant derived from a decision names that decision, and a check names its invariant, or, where it holds a decision's sentence by a line `decision:`, that decision, with no invariant between.

- **Scope:** decisions, invariants, environment-facts

### WAY-54 — Where does the value of a field in a template come from?

The value of a field is read off the product wherever a tool can read it, and a template asks for what a value follows from rather than for the name of a value; a value that a closed list of the template does not hold is a question to the human, never the nearest value on the list.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common

### WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every entry of its kind, holding a value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there, `TODO` that something is missing. The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet: in an invariant's *Rests on*, in the form `TODO — <the fact, with its source>`; in an invariant's *Derives from*, in the form `TODO — <the decision, and where it is expected>`; and in a decision's *Based on*, in the form `TODO — <what is missing, with its source>`; where an entry stands on several things and only some are missing, the missing one is the last item of the value and reads as the form of its field, after the known items; a change that leaves one there puts it before the human. `elements/common/foundation_check.py` reports a missing field, or a word not given it, as an error.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common, task-cycle

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

A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a projected entry at the readiness gate, shown as one sentence in the human's language with the entry beside it; that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement; and that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier, repeated in the human's language in the description's collapsed block, while the full list of the change's entries, each by its identifier with one English sentence of its meaning, stands in the description's lower part, and an entry that is marked as the cycle's because of a pair of examples its writer added has that pair there word for word under it. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.

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

### WAY-33 — What does the author of a foundation change search for?

When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches — those that name the entry or that it names, and those no written link joins to it — and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human. The search is not repeated before the merge and leaves no record.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle, agent-instructions

### WAY-35 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them. No template and no skill of an element carries a note that a rule waits for a decision.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common

### WAY-113 — How does an agent of the-way ask a human decision?

An agent asks in plain conversation text, with no separate question panel: a question of assessment stays open, and a decision question gives the available ways, the cost of each, a recommendation and the weak point of the way recommended. The cost of a way includes the cost of undoing it later, written as one word where it is nil; the weak point is the strongest argument against the way recommended, anchored in the material where the material gives one, and for a shortcut, where another way would be right were cost no matter, it names that way and says why it is not recommended. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way.

While a project definition or a task document is refined, the technology step included, that question is asked only where the choice contradicts a sentence the human said earlier, which the question quotes, and that holds as well for the entries written during that refinement; in a task's cycle and where an entry is written outside such a refinement it is asked as above, the looser rule holding only before the cycle starts (WAY-315). In the whole refinement of a project definition, its rounds and its step of projected foundation changes, a question may also follow an answer where it takes the move of implication, "you wrote X; from X follows Y — does Y hold?", anchored in a sentence of the human, or asks the reason of a decision that is costly to reverse, where neither the human's words nor the material give it; the refinement of a task keeps the rule above.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, task-cycle, foundation-review, process-audit, product-guidelines

### WAY-120 — How does the-way critique an agent's proposal?

An agent may invoke critique for any proposal without waiting for the human to express doubt; a completed set for collective human review goes through it, and the diff of a change to an invariant test or to the foundation does not (WAY-10). An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict. For a collectively reviewed set the critic checks form, fidelity to source and contradictions across entries before presentation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines

### WAY-150 — How do the-way skills choose which product foundation material to read?

The-way skills read a product's foundation selectively: whoever selects names the parts the work touches from the files it changes through the part map's rules for assigning files, or, where the work names no file yet, from the responsibilities it changes; finds by a touched part's identifier the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds the invariants a test the work alters cites, the decisions whose sentence such a test holds by a line `decision:`, the decisions the task's *Decisions in play* or the work's source names, the touched parts' entries of the map and the entries these link to as far as the work needs. Of the decisions it finds by *Scope*, by a line `decision:` or as the task or the work's source names them, whoever selects reads the index and opens whole only the decisions the work changes, goes against or proposes another answer to — that one with its rejected options — those the task or the work's source names, those whose sentence a test the work alters holds by a line `decision:` and those whose binding sentences leave open what the work has to do; each other entry it selects — an invariant, an entry of the map of a touched part, or an entry, a decision included, that these or the decisions of the index link to as far as the work needs — it reads whole, and it reads more entries where relevance is uncertain and a whole file only where it is short; the reviewer of the whole change reads the index of its whole selection and states in its report how many decisions it read whole. The selection is neither recorded nor compared with every *Scope* of the log, and the search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep their domain.

The index of a selection of decisions is no file of the repository: a script of the-way writes it on demand into a file the agent names, and it gives for each selected decision its number, its question, its binding sentences and its *Scope*.

In a decision log divided into topical sections, whoever selects picks from the list of sections, by each one's heading and sentence, the sections of the work's topics, whose decisions take the place of those found by *Scope* in the selection whose index it reads, and it runs through the questions alone of the decisions outside those sections whose *Scope* names a touched part and opens whole each whose question points to a bearing on the work. In a log without topical sections the decisions are selected by the parts the work touches, and their index takes the place of reading each of them whole, the decisions the first paragraph names being opened whole as it gives.

Outside the task cycle the agent doing the work selects its own reading, while in the task cycle the orchestrator selects for its own judgments and for each handoff, which names the foundation entries by identifier; the reviewer of the whole change selects for its own review, and an agent writing a foundation entry through an element's skill for the entry it writes; and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively — a search for an identifier or a word and a read of the passage found, never of a whole file of the foundation — naming each such reach in its report.

- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts, project-level, task-cycle

### WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation change a human decides, or where a decision in the product's log or the pinned the-way places it. An invariant whose condition stands outside its sentence names by identifier the entry or the decision that holds the condition, in a field where the template gives one and otherwise in its sentence. An identifier of a decision written into the sentence because that decision holds the condition is a part of the condition, not a link that WAY-17 requires; where such a link is due, it stands beside the sentence, in its own field.

An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}` (WAY-61), while a state it compares may be the one on `{merge-onto}`, and states what is to hold on the main branch alone as holding where `{merge-onto}` exists. A sentence bounding or equating a quantity measured while the product runs names its bound or tolerance, statistic and population.

- **Scope:** invariants, decisions, part-map, gate

### WAY-61 — How is an invariant's method of checking written?

An invariant's method of checking reads `test` once a test of the product's test suite, written in the product's language and run by the command that runs the product's tests, cites it, and `review` until then, and it names no command and no script. The method is held on the finished change: an invariant whose test a later slice of the same change writes may read `test` from its writing on. A test checks what its invariant's sentence is about, as it stands on the commit being checked, so a test fed input made up for it is the method of a sentence about the check it exercises, never of one about the data that check reads.

- **Scope:** invariants, gate, decisions, part-map, elements-common, task-cycle

### WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?

An invariant's *Rests on* names every environment fact holding a condition that decides whether a commit makes its sentence true, and no other fact. A fact holds such a condition when, read otherwise, it would change whether some commit makes the sentence true, or change a value the sentence copies from it. A fact that is only a reason for a decision the invariant derives from stands in that decision's *Based on* alone; a fact stands only while an invariant's *Rests on* or a decision's *Based on* names it, and the change that removes the last such name withdraws it.

- **Scope:** invariants, decisions, environment-facts

### WAY-84 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can open it, a host's access rule — is an environment fact, its source the place where that state is shown, or, where no page open to a reader shows it, a reading. A choice of such a setting is a decision only where the product declares it, and that decision rests on the fact. A fact about the visibility of a repository the product links to names that one repository.

- **Scope:** environment-facts, decisions

### WAY-85 — How is a finding of a study written as an environment fact?

A finding of a study stands as an environment fact saying what the study found, its source citing the version of the paper, and the models the study measured named as the study names them, in the sentence or in a passage its source quotes. That the agents of this process behave the same is no part of the fact. A decision citing a finding none of whose measured models comes from a publisher whose models the process's agents run on says in its rationale that it takes the finding across publishers.

- **Scope:** environment-facts, decisions

### WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

A decision's *Based on* quotes every source outside the product that the decision rests on with its address, the place in it, the passage word for word and the date it was read; once the environment facts element has entries, it names instead a fact entry, by its identifier alone, for every citation that, once it stopped being true, would call the decision into question — a finding about agents or models, the behaviour of a tool the process uses. A measurement that the product's own people made — its author and its agents — and whose record a reader of this repository cannot open is no such citation: its result stands in the decision's *Rationale*, or in its *Rejected* where it weighs a way not chosen, with what was measured and under which conditions; that prose says that the measurement is the product's own and that its record is not open to a reader of this repository; and no environment fact entry is written for it.

- **Scope:** decisions, environment-facts

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

### WAY-52 — What is generated from the part map for an agent?

Nothing is generated from the part map for an agent: an agent reads the entries of the parts its change touches, and no overview of the repository is generated for it.

- **Scope:** part-map, decisions

### WAY-53 — How is a derived file compared with what its generator produces?

A derived file is identical to what its generator produces on the same commit, except for values the file itself declares as varying between runs.

- **Scope:** decisions, part-map, invariants, gate

### WAY-225 — What in a product's foundation is derived rather than written by hand?

What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state. Rules are written by hand: what is allowed and what the product promises, which the code cannot show, and a dependency of a part that the code holds and the part map does not allow is recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies of a part to fit the code.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts

### WAY-55 — Which part of the process holds the gate?

In this repository, the gate is a part of the process of its own, and its directory is `gate/`: the gate's code and the test of every critical flow are files there. No other part's directory holds that code or such a test, and a file under `gate/` that only calls a body kept in another part's directory leaves the gate in that part. Which checks a change calls for, when the gate runs and what follows from what it reports belong to the task cycle, not to this part.

- **Scope:** gate, decisions, invariants, glossary, part-map, environment-facts, relation-model, repository, task-cycle

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field — a field that an earlier form of the file never had being no missing field where the command reads the file as that form, which it does for a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*, and which gives the values that need that field as unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives no line `Error:`. Where a script whose purpose is to check the form of a file reads a copy of the file from the commit the branch left the main branch from, a field it needs for a comparison and finds missing from that copy is listed by a line `listed:` that names the entry and the field, with no error and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field, the review of the change answering for the other fields; the *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds it to this *Scope*. The command that counts the audit, where a table of weights or a table of the costs of an occurrence in the register of problems lacks one of its levels, writes its result, gives the values that depend on the table as unknown and ends with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither of the two columns of the cache writes in its detailed section, that command reads the report as an earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and priced as input, an approximation, and no value unknown for the missing columns, while a stage report that has one of the two columns and not the other has a missing field, with the line `Error:`. Where the locations file has no entry `repository` under `the-way`, no field is missing and that command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines, process-audit

### WAY-127 — How does a session working on the-way itself reach the-way's skills?

A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix. No global link reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in itself.

- **Scope:** agent-instructions, elements-common, project-level, task-cycle, decisions, invariants, glossary, part-map, environment-facts, installation, instruction-files

### WAY-256 — Where does a fragment of a skill stand?

A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one variant of the skill needs, or only one step that some uses of the skill pass by, stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps, the pointers, every step until records of sessions a person can open, those of Claude Code and Codex, show that part of the uses since the step stood in the skill pass it by — also where no record exists — and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines, task-cycle

### WAY-265 — Where is the file of a variant named, when a step's file points to it?

In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level, product-guidelines, task-cycle

### WAY-126 — How does a projected entry enter the foundation?

A projected entry of an approved project definition enters the product's foundation in the change of the first task whose code makes it true — the task the plan assigns, or a task that uses the definition as a source only, even where the plan assigns the entry to another task — whole, in the wording the readiness gate approved, with the projected terms and environment facts it uses or rests on and with no record of approval copied from the gate, since the merge of the task's request brings it in; where the code makes only part of it true, the agent writes that part and the human accepts its meaning at the merge (WAY-114). The task the plan assigns writes what of the entry the foundation does not yet hold, and a projected entry no code makes true. The return step reads the projected entries of the task's sources as well as the foundation, writes one the code makes true that the foundation step missed — an invariant with its test run on that code — and writes a new entry only for a rule none of them states.

- **Scope:** project-level, task-cycle, decisions, invariants, glossary, environment-facts, part-map

### WAY-121 — Where does a project settle the technology it needs?

Before a project definition goes through its readiness gate, a step of its own lists the technology and architecture choices the project needs — such as a language, a framework, a store of data or a place to run — and, for each, either names the decision of the foundation that already holds it or settles it as a projected decision of the definition; a project whose every choice the foundation holds thus settles nothing. A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up; a choice one task can make and change alone stays with that task, while a choice under this rule that a definition missed, or that no definition holds, is settled through a run of the step at a task document (WAY-267, WAY-268). As an exception to that rule, where the project brings behaviour a user sees in the running product, the step looks at four matters of an agent's way to the running product — its logs, its interface, its development data and the place of its screenshots — and lists as a choice of its own each matter that no decision of the foundation settles for that behaviour, even where its answer adds nothing to run, pay for or back up, and even where the product has none of what the matter names, whose answer then says what an agent uses in its place; how a human learns of a failure of the running product is no such matter and has an exception of its own (WAY-270).

- **Scope:** project-level, decisions

### WAY-122 — How are the options of a technology choice found and checked before a human sees them?

The options of each technology choice a project or a task needs come from research of that choice against the project definition or, in a run at a task (WAY-267), against the task document and the run's note, rather than from a fixed list of bundled stacks, and the research of every choice that depends on no unsettled choice starts once the list of choices is confirmed, each in a report of its own. An option the product's code is written in or against — a language, a framework, a library, a store of data — is weighed by whether its documentation shows that it uses explicit types, follows conventions of layout and naming and has current, versioned documentation, and whether a public record of its use, such as a package registry or a survey, shows it widely used within its language family; for a store of data, its types are those it declares for what it stores, and its family is that of its query language. An option lacking one of these properties is offered with what each lack means for the product, which the decision records if the human chooses it; an option with no documentation or with a project no longer maintained is left out with that reason, unless the human named it or the definition or the task document holds it as a constraint, and then it is offered with that reason as such a lack; and every option is offered only after a critique that refutes every claimed difference between the options which no source supports.

- **Scope:** project-level, decisions

### WAY-123 — How does a technology choice reach a human who cannot assess the technology?

The step that settles technology, at a project definition or at a task (WAY-267), shows each choice in plain text, in words a person who does not know the technology can follow: the options that decide it, each under its own name, by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs — the other options one line each, and the lines of the options left out; the human chooses between those consequences. A difference with no consequence for the product decides nothing, and where no difference with a consequence remains, the step recommends the simplest and cheapest option. The choices whose research started together reach the human together, in one message, one choice after another, once every one of their comparisons has passed the critique and a fresh agent has checked, in the first message, before it is shown, that no option stands there by figures or features instead of what it changes for the product and that no word stays that a person who does not know the technology cannot follow without an explanation, each choice with its recommendation and the weak point of the option recommended; in the area of the choices this step settles, this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** project-level, decisions

### WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?

Where the options of a place to run differ in no consequence for the product and more than one of them is the simplest and cheapest, the step that settles technology, at a project definition or at a task (WAY-267), recommends, of those, the one an agent works with best: operated from a terminal, deployed by a script and documented in pages an agent can read. For a place to run, how well an agent works with an option decides nothing else: it leaves no option out of the comparison and is weighed against no consequence for the product.

- **Scope:** project-level, decisions

### WAY-138 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?

The step that settles technology, at a project definition or at a task (WAY-267), tests the option it recommends for each choice it settles, one a constraint of the definition or of the task document settles included, with a devil's advocate, a pre-mortem and a search for unknown unknowns; it tests no choice a decision of the foundation holds, a choice the step opened being held by no decision, and no other decision already written is tested afterwards. The risks these tests give are hypotheses with no source, not differences claimed between options, so the critique of the comparison does not strike them, and they stand in the message beside the option recommended before the human chooses. The human who chooses that option takes its risks, and each risk taken reaches the decision of that choice in its *Rationale*, beside the lacks of the option chosen, marked as a hypothesis, through the task document where the step ran at a task.

- **Scope:** project-level, decisions

### WAY-267 — How does the step that settles technology run outside a project definition?

Besides its run at a project definition, the step that settles technology runs at a task document, with a note saying what the run is for, and a run with no task document starts by creating one through `refine-task`. A run at a task settles what the note and the task name, looks at the matters of an agent's way to the running product only where the note touches them, does the rest of its work as a run at a definition does and ends back in the task's refinement, with no readiness gate; a human may run it for any choice save one a projected decision of an approved definition settles, which no run reopens, and the step opens a choice a decision of the foundation holds where it sees a reason to change the decision (WAY-313), the result then being a change of that decision. The run writes each settled choice into the task document, with the options not chosen, the source of each difference claimed between the options, the lacks of the option chosen and the risks the human took with it, and the task's cycle writes the decision with the code that uses it.

- **Scope:** project-level, task-cycle, decisions

### WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?

Where a project runs the product outside the machine on which it is made, which holds unless the definition or a decision of the foundation keeps the product on that machine, and no decision of the foundation settles it, the step that settles technology lists how a human learns of a failure of the running product as a choice of its own, answered by a tool that collects failures, an alert or a deliberate absence, even where its answer adds nothing to run, pay for or back up; in a run at a task (WAY-267) it enters the list only where the note touches it. No definition has to hold this choice, the readiness gate does not check it and an approved definition does not come back to the step for it; it is no matter of an agent's way to the running product, so whether an agent can read an option is a consequence like any other, and a change to it does not open the decision on the logs. A deliberate absence always enters the comparison of this choice, though it has no page of documentation, its consequences anchored in the document and in the pages of the other options; in the area of this choice this decision prevails over WAY-121, which lists a choice by its rule of belonging and the four matters of an agent's way alone, and over WAY-122, which leaves out an option with no documentation.

- **Scope:** project-level, decisions

### WAY-165 — What must an answer to each matter of an agent's way to the running product settle?

Of the matters of an agent's way to the running product, the logs ask where the record of what the running product does goes, how long that record lives, between deployments too, and how an agent reads it, and the interface asks how an agent operates the product as its user does — through a screen in a browser, a call to its API or a command in a terminal — and how it sees what the product answers. The development data asks where the data comes from on which an agent checks the product's behaviour outside production, and how an agent brings that data to the state a check needs, and the place of the screenshots asks where the files of the screenshots that an agent takes to show the human lie, outside the product's repository, and how the description of a request shows each as an image. Data set up from scratch and a dedicated test environment that persists are examples of options of the development data, none of them ruled out, and an entry, a decision of the foundation or a projected decision of a definition, that leaves part of what a matter asks unanswered does not settle that matter at a project definition; in a run at a task (WAY-267) the step may open a decision of the foundation that leaves part of it unanswered as it may open any such decision (WAY-313), the list shown to the human saying in one sentence what that decision leaves unsaid.

- **Scope:** project-level, decisions

### WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?

In a choice of an agent's way to the running product, whether an agent can use an option is a consequence for the product: an option an agent cannot use stays in the comparison with that lack said as "an agent does not check the running product this way", and the recommendation passes over it. Where no option can be used by an agent, the recommendation goes by the other consequences and says in one sentence that no option lets an agent check the running product this way, so the check stays with the human.

- **Scope:** project-level, decisions

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form of the candidate table of the skills of the elements (`elements/common/skill/build_table.md`) with each settlement in the human's words and, in place of its kind, the place it goes to by the questions of the decisions template, and the task document keeps the rows the human accepts, one that goes outside the decision log included and those that repeat a choice the human made between ways shown included unless the human struck them, and, where the human chose among ways shown, each way not chosen, under the answer to its question or, for a choice made outside the task's questions, in the source of the row it settles; the agent refining the task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, or a settlement that goes to another place those questions give — a skill or an instruction file, the guidelines of a discipline, or the data or code of the product — and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate. The task's cycle writes each kept row whole in the place its column gives, in the same change as the code, in its foundation step, or in its return step where the foundation step missed it, one that no code makes true included, keeping its meaning and choosing its wording, and gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`; where that meaning cannot hold, or the entry needs any other value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft request rather than write another entry, and otherwise the entry's meaning is the one the human accepted with the row in the task document (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated becomes no second entry, the cycle tying the row to that entry and naming both in the request.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary, environment-facts

### WAY-11 — How does a task end?

A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches. In the same change it writes the sources outside the product that the change rests on and the foundation does not yet hold, as environment facts, a word the change uses in a meaning for which WAY-95 gives it an entry, as a glossary term, and the accepted settlements (WAY-134), each in the place the questions of the decisions template give it and as an entry of the decision log only where it passes all of them and where someone who does not know the decision would do otherwise and a test that stops them would not tell them why, and projected entries (WAY-126) the task carries that are not yet written. It writes an invariant only for a rule the task, a decision or a human sets, never for code behaviour merely because no invariant covers it.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle

### WAY-136 — When does a task's change need a plan, and who makes and reviews it?

A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split. A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own and names, for each blocking finding, the slice it comes from or that it comes from none, while the review of a one-author change or of a plan's only slice is the review of the whole change; and that review also checks coverage of the task, every row of its *Settlements to record* and every projected entry it carries.

- **Scope:** task-cycle

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads the cycle record, an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it. The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle

### WAY-10 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation has no assessment of its own, in a product as in the-way itself: an agent that did not make the change reviews the whole change, its foundation entries and invariant tests included, against its task and the foundation, and a human reads the section of the request's description for the human's decisions and accepts the change by merging the request.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common, task-cycle, agent-instructions

### WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?

A binding rule of a product's guidelines says what to do and how, and may give a use that follows it and one that breaks it, each in one line; what the guidelines hold that states no rule is an example. A rule that executes a choice of the product with a real cost names by identifier the decision of the product's log that carries the choice, while its reasons and rejected options stand in that decision alone, and a rule that only says how to write code, tests or the look of the product reads `none` in *Decision* and gives its reason in one sentence. A rule names an invariant only where a cheap test of the product's suite checks the rule on a convention of the product's code; a rule no such test can check names none, and the review of each change the rule reaches compares the change with it.

- **Scope:** product-guidelines, decisions, invariants, task-cycle

### WAY-172 — How is a new or changed meaning of a product's guidelines approved?

A new or changed meaning of a product's guidelines that carries a choice with a real cost is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as WAY-30 has a change to a decision approved, or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision. A new or changed rule that only says how to write code, tests or the look of the product, with no decision, is accepted by the human as a row of the task's table of settlements before the code that uses it, or, where the cycle found the rule itself, at the merge from the request's description, and a rule of a template of the-way binds a product only through a decision of its log that adopts it (WAY-173). Using a meaning that a decision of the product's log already carries takes no approval, and neither does changing a value that keeps its meaning; in the area of new and changed meanings of a product's guidelines that carry a choice with a real cost, this decision prevails over WAY-114, under which an agent writes such an entry on its own recommendation for the human to accept at the merge.

- **Scope:** product-guidelines, decisions, project-level, task-cycle

### WAY-174 — How do the-way's skills of guidelines ask the human?

The-way's skills `maintain-styleguide`, `maintain-coding-guidelines` and `maintain-testing-guidelines` put to the human every choice they settle for a product's guidelines, a choice they recommend included, and show each in plain words — a styleguide's by what someone using the product sees on the screen, never by the names or values of design tokens, coding guidelines' by their effect on the product, never by the names of a linter's rules or the values of a tool's configuration, and testing guidelines' by their effect on the product, never by the name of a technique or a tool — saying in plain words what a term of the field means before they first use it. The coding-guidelines skill asks for decisions, never for single rules, so that the human adopts a linter's set of rules whole. In the area of the questions these skills ask this decision prevails over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** product-guidelines, decisions

## Listed by heading alone

