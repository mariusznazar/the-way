# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and are edited in place.

## The-way and how a product takes it

What the-way is for and for whom, what its repository holds and points to, and how a product takes
up its process, its version and its backlog.

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a
directory for each part of the process other than `repository`, which the part map of the-way names
with its files, the files that configure the whole repository, which its part map gives to the
`repository` part (WAY-44), the root agent instruction files, the project skill entry points under
`.claude/skills/` and `.agents/skills/`, the copies of the cycle's agent type definitions under
`.claude/agents/`, the CI configuration under `.github/workflows/` and the directory `guidelines/`
with the guidelines of the-way's own code and tests, which the map gives to `agent-instructions`
(WAY-44, WAY-167), and a `README.md` that describes the repository. A directory reaches
the main branch only once it holds what its part requires: an element its template and rules,
examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its
entries; any other directory what the sentence of its part in the part map names. The entries in
`foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, product-guidelines, foundation-review, process-audit, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: repository-file-location · element-directory-contents. For what
  `elements/common/`, `installation/`, `agent-instructions/`, `instruction-files/`,
  `project-level/`, `product-guidelines/`, `foundation-review/`, `process-audit/` and
  `task-cycle/` hold and for what
  checks `foundations/`, an agent compares the change with the decision:
  - complies: code two skills of the elements share moves into `elements/common/`, and both read it
    from there; a new rule of form for the entries in `foundations/` is checked by
    `elements/common/foundation_check.py`; the installer, its tests and instructions stand together
    in `installation/`; the templates of a definition, a plan and a task document, the skills that
    write them and the checks of a definition and a plan stand in `project-level/`; the agent
    instructions have their own part and root entry points; the project skill entry points under
    `.claude/skills/` and `.agents/skills/` stand at the root as files of `agent-instructions`, and
    the script that generates them stands with its test in `agent-instructions/`; the copies of
    the cycle's agent type definitions under `.claude/agents/` stand there too, generated from the
    definitions in `task-cycle/`; the CI configuration stands under `.github/workflows/` as files of
    `agent-instructions`, and so do the guidelines of the-way's own code and tests, which stand in
    `guidelines/`; the principles,
    the loading account, the skill and the check script of instruction files stand together in
    `instruction-files/`; the template of guidelines and the template and the skill of the
    styleguide discipline stand together in `product-guidelines/`; the skill of the review of a
    foundation and the files it reads beside it stand together in `foundation-review/`; the template
    of the register of problems, the price list of models, the command that counts the audit and the
    skill of its weekly session stand together in `process-audit/`;
  - violates: a `tools/` directory for shared scripts reaches the main branch; a new element comes
    with a script of its own that checks the form of its entries beside
    `elements/common/foundation_check.py`.
- **Origin:** none

*Rationale:* anything brought in on the side makes the repository a store of material; directories
follow the parts, so a change's files name its part and decisions (WAY-21); an incomplete directory
is work in progress, kept on a branch (WAY-01); product installation and agent instructions have
different failures from repository configuration; the project definition and task cycle answer
different questions; the principles of instruction files serve any repository, so they stand apart
from this repository's own agent instructions; a product's guidelines stand outside its foundation
and answer to no element, so their templates stand apart from the elements, and their failures — a
product's screens built on a meaning nobody approved, guidelines telling agents an old rule — are
not those of instruction files; the review of a product's foundation answers neither the question
of a task cycle nor that of an element, so its skill stands apart from both; the audit of the process
over many cycles answers neither of those questions either, so its template, command and skill stand
in a directory of their own. The guidelines of the-way's own code and tests direct whoever
carries out its tasks, as its instruction files do, so they stand in the directory where a product
keeps its guidelines (WAY-167) and belong to the part that holds those files.
*Rejected:* material merged as soon as it is written — a store from the first day; an element whose
only tool is a skill — the form holds only while someone remembers to run it; one `tools/` directory
for everything shared — it matches no part and grows into a store; one set of template, skill and
script for every directory — a script that only reads has nothing for a skill to write; the files
serving the whole repository left out of the map on purpose — they lose their part; installation or
agent instructions folded into repository configuration — their failures lose their own parts; the
principles of instruction files folded into this repository's own agent instructions — that part
answers for the-way's own instructions, and its failures differ; the templates of guidelines under
`elements/` — guidelines are no element of the foundation (WAY-04); the same folded into
`instruction-files/` — that part answers for instruction files of any repository, and its failures
differ.

### WAY-27 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every entry
carries its whole reasoning, and what is seen only in such a source is described in the entry
instead of being pointed to. The one exception is the places where the work of the-way lies — the
place of its tasks and the rules of that place, the register of problems and the results of the
audit — which are no source of reasoning, and a file that needs one names it by an entry of the
locations file of WAY-320, never by a path.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, agent-instructions, instruction-files, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: outbound-link-reach. For the reasoning in the entry, an agent
  compares the change with the decision:
  - complies: a decision quotes a public study with its address; a pattern seen in a product
    outside the repository is described in the rationale, without a pointer to it; the-way's root
    `AGENTS.md` names, in `## Backlog`, the entries of the locations file where the place of its
    tasks and the rules of that place are kept, and the instructions of the audit name the entry
    that holds the register of problems;
  - violates: *Origin* points to a private note; a rationale rests on "as in our other product"
    without saying what was seen; a file holds the path of the place of the tasks or of the
    register of problems; a decision rests its reasoning on a task document or on a result of the
    audit.
- **Origin:** none

*Rationale:* a pointer to a source the reader cannot open is a dead end, leaving a claim nobody
can check; what was seen there, written down, can at least be judged, and WAY-17 still has a fact
to name. A place where work lies — a backlog, the register of problems, the results of the audit —
is where work is kept and found, not reasoning an entry rests on, and WAY-107 sends an agent to the
backlog, to the rules by which the lines of that place are written as well; named only by an entry
of the locations file, such a place stays a place to find work and never becomes a source an entry
points to. A general sentence takes in each place the work comes to lie in, where a list would need
a change of this decision for each one. Named by an entry of the locations file, a place adds no
path to a public repository, which would tell every reader how one user's disk is laid out.
*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader can open
them; the path of the place of the tasks left in `## Backlog`, with the check for paths excepting
that section — the repository would go on saying how the user's disk is laid out, the very thing the
check is there to stop; a closed list of the places with the one file that may name each — every new
place needs a change of this decision, and a change forgotten leaves the same gap between the
decision and the files.

### WAY-28 — How does the process enter a product that already exists?

When the process enters a product that already exists, the existing state is its starting point
and needs no justification, and the rules apply to changes from then on. The part map comes
first; the invariants of the critical flows, each naming in *Part* the parts its flow runs through,
are then recovered from what the product does — an agent lists what a part does, and a human chooses
which of it the product must keep — and the other invariants come through the return step of
tasks. Decisions are recovered only when a task touches the parts they govern.

- **Scope:** decisions, invariants, glossary, part-map, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: on entering a product, the part map comes first; a human picks a critical payment
    flow's invariants from the agent's list of what it does; a decision is recovered when a task
    first touches the parts it governs;
  - violates: an agent turns everything the critical flows do today into invariants without a
    human's choice; an agent recovers from the code decisions for the whole product before any
    task touches them; the critical flows and the parts they run through wait for a task like any
    other.
- **Origin:** none

*Rationale:* decisions recovered in advance tempt an agent to invent reasons that look like
decisions. What the product does today is a state, not a rule (WAY-225); only a human knows what it
must protect. An invariant needs no decision above it, so it binds before anyone knows why.
*Rejected:* recovering the whole foundation at the start — slow, with reasons invented where none
are known; everything on demand, the critical flows included — a break there shows only when a task
happens to touch them.

### WAY-34 — Which version of the process does a product use?

A product uses the-way at a commit pinned in its own repository: its templates, skills and
scripts, and the decisions of the-way that bind its work, all come from that commit. A newer
version of the process enters a product only in one commit of the product that moves the pin,
made when a task of the product needs a change of the process, as the first commit of that task's
branch, under which the task's whole cycle works, or in a step of its own that takes several
changes of the-way at once.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, instruction-files, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision; the invariants of this decision
  belong to each product's foundation, since no commit of the-way decides them:
  - complies: a product's foundation holds the invariants "this repository pins a commit of
    the-way" and "CI runs only that commit's scripts"; a task that needs a newer skill moves the
    pin in its branch's first commit, before its route is judged, the entry points, the agent type
    definitions and the guidance the installer rewrote included, and carries what the newer version
    changes for the product;
  - violates: a product's CI fetches the latest the-way on every run; a skill in a product session
    comes from a copy of the-way other than the pinned commit; a product moves its pin after every
    change of the-way, though none of its tasks needs one; a task cycle moves the pin after its
    route is chosen, or between its slices.
- **Origin:** none

*Rationale:* a pinned commit turns a change of the process into a change in each product, taken
in there before it binds, so one change cannot stop every product's checks at once. The price:
products lag behind the process, and moving a pin is work, like updating a dependency. Moving the
pin first keeps a task's cycle under one version, so its request is read against the rules it was
made under.
*Rejected:* every product on the newest the-way — results change with no change in the product;
templates and scripts copied into each product — the copies drift; a move after every change of
the-way — it interrupts the product's own work for changes none of its tasks needs; a rule naming
which version binds a cycle after a move made partway through it — a move made first leaves no
cycle under two versions.

### WAY-100 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a
decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness
to a method or practice no decision has adopted, it asks a human before treating it as a rule.

A decision that adopts a method or practice from outside names the practice and what it takes from
it, in its binding sentences or its *Rationale*, and puts what it leaves out of the practice in
*Rejected*. Its source is the place the practice was in fact taken from, found by following the
trace of that taking, never a document that only describes the practice: the decision names that
source in *Based on*, or, for a source a reader of the repository cannot open, describes in
*Rationale* what was seen there and says that the source is not open to that reader (WAY-27). A list
of what is taken from one source is no decision: each rule taken stands in the decision that
carries it (WAY-19).

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision adopts only the risk assessment step of an outside process for task
    planning and gives its reason; an agent offers an unadopted technique as a proposal; the
    decision on that step names the step and what it takes from the process in its *Rationale*,
    quotes in *Based on* the article the step was in fact taken from, with its address, the passage
    and the date it was read, and puts the steps it does not take in *Rejected*; a decision that
    takes one practice from a course whose lessons a reader cannot open describes in its *Rationale*
    what the lesson showed and says that the lessons are not open to that reader; the rules taken
    from one outside source each stand in the decision that carries them, with no decision of its
    own for the list of what is taken;
  - violates: a skill makes an outside planning ritual mandatory because an agent recognizes it,
    without a decision adopting it; a decision adopts an outside practice and says nowhere what it
    takes from it; a decision answers the question "what do we take from this source" with a list
    of the rules taken, each of which a decision of its own would carry; a decision whose practice
    came from a course cites in *Based on* a public page found afterwards that describes the same
    practice; a decision that takes a practice from a lesson its reader cannot open describes the
    lesson and leaves the reader to guess whether its address was forgotten.
- **Origin:** none

*Rationale:* borrowing pieces without a conscious choice makes the product's boundaries hard to
explain and change. Naming the chosen piece, its scope and its reason lets later work distinguish
it from a resemblance or a habit. A decision that says what it takes from a practice and what it
leaves out keeps the likeness to the source from passing for the adoption of the whole, and a list
of what is taken from one source answers no question someone could answer otherwise, so it is no
decision (WAY-19). The source is where the practice was in fact taken from: a public page that
describes the practice, found afterwards, would look as though the practice came from there, though
it may have come from elsewhere and in another scope, what is left out would be weighed against a
text nobody read when the decision was made, and a made-up source looks the same as a true one. A
decision that says its source is not open to a reader lets a reviewer tell a closed source from a
forgotten one, and the next decision that takes from the same closed source says it as well.
*Rejected:* importing a whole outside method by default — its unrelated steps become obligations;
treating recognition by an agent as adoption — recognition does not settle fit or scope; the
sentence on the practice stated only in the skill that looks for candidates for entries — the rule
on borrowing and the rule that "what do we take from X" is no question of a decision would read as
contradicting each other, the decisions that adopt a practice would have no rule of the foundation
to follow in one form, and whoever writes a decision outside that search would not see the rule;
any public document that describes the practice as the decision takes it, as its source — the
decision would look as though it took the practice from there, though it may have taken it from
elsewhere and in another scope, and what it leaves out would be weighed against a text nobody read
when it was made; the place the practice came from and, where no trace of it is found, a public
description of the practice marked in *Rationale* as a description — a new kind of source that no
rule knows, which this decision and WAY-90 would have to admit; the sentence that a closed source
is not open to a reader written only in the decisions that already take from a course, with no rule
here — the next decision from a course would leave it out again, and a reviewer could not tell
whether its source is closed or forgotten; nothing written, the answer kept only in the document
of the task that asked — the decisions stay as unclear, and the document ends with its task.

### WAY-101 — Who chooses the backlog tool used with the-way?

The-way's task cycle requires no particular backlog application or service; each product chooses
where it keeps its roadmap, projects and tasks.

- **Scope:** elements-common, project-level, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a task-cycle step accepts task information supplied from a product's chosen files or
    tracker;
  - violates: the step can obtain tasks only from one named backlog service.
- **Origin:** none

*Rationale:* the backlog hierarchy belongs to the process, while its storage belongs to the
product. Requiring one service would force a product to move its tasks before it could use the
process.
*Rejected:* one fixed backlog service for all products — adopting the process would also require
adopting that service.

### WAY-102 — What is the-way for?

The-way is a process for work on a technology product in which a change of premises or direction is
an ordinary step: it passes through the product's foundation and needs no memory of what is linked
to what.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a change of product direction goes through the foundation, and its author searches
    the foundation for the entries the change touches and brings each finding into line in the
    same change or asks a human;
  - violates: a change of direction relies on the author remembering which decisions and documents
    to update.
- **Origin:** none

*Rationale:* a process that relies on a person to remember every affected artifact fails when work
spans tasks and sessions. Making foundation changes routine gives each change a place to start and
a route to its dependents.
*Rejected:* disconnected steps joined by hand — the person carrying the work must reconstruct
their links; treating a change of premises as an exceptional repair — the foundation falls behind
the product's direction.

### WAY-103 — Who is the-way for?

The-way is built first for its author and aims at anyone who builds a technology product and adopts
the process for their own needs; the process is written for the agents that carry out the task cycle
too.

- **Scope:** decisions, elements-common, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: an element's skill gives an agent steps it can perform, and a new task-cycle step is
    understandable to a builder using their own product;
  - violates: a task-cycle step relies on private shorthand only the author understands, or leaves
    the agent's action unstated.
- **Origin:** none

*Rationale:* starting with the author gives the process a real first user; aiming at independent
builders keeps one person's setup from defining the audience. Agents need instructions they can
execute because they perform the task cycle.
*Rejected:* an author-only procedure — another builder would have to reconstruct its unwritten
conventions; prose addressed only to humans — an agent could not take its assigned steps from it.

### WAY-107 — Where does a product tell the project level where its backlog stands?

A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`,
outside the block the-way's installer owns, a place on the user's disk outside every repository
standing there as an entry of the locations file of WAY-320, never as a path, and a directory of the
repository or the address of a public tracker as it is. A project definition stands in the named
project place; when the place is unnamed, or the file or the entry it names is missing, the agent
asks the human and offers to record the answer where it fits: the entry in the file for a place on
the user's disk, the section otherwise.

How a task's line is handled — the status of a new line, its move to ready, the form of its
dependencies, the characters of its identifier and its being unambiguous in the whole place, how a
line is found and kept one to a task, which fields an agent may change, the agreement of the lines
at both ends of a dependency, a clash of identifiers — is taken from the rules of the task place
itself, never from text written at the product or in the-way's skills; the section names, beside
the place of the tasks, the entry `task-rules` of the locations file under the product's name,
whose value is the path of those rules, and where that entry or the file it names is missing, the
agent asks the human once and offers to add the entry, as for a missing place. The one part of a
line that the-way gives is the derivation of a task's identifier from its plan and its name in the
plan, so that a dependency can name a task before that task's line exists; where the rules of the
task place do not accept the derived identifier, the agent asks the human and writes no line.

- **Scope:** project-level, installation, foundation-review, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-101 · derives from WAY-320
- **Verification:** an agent compares the change with the decision:
  - complies: a product names a directory of its repository for projects and a public tracker for
    tasks in its own backlog section, and the project definition is written in that directory; a
    product whose tasks lie in its user's private notes names, in the section, the entry of the
    locations file that holds their place and the entry `task-rules` that holds the path of the
    rules of that place, and an agent that finds either entry missing asks the human once and offers
    to add it to the file; an agent that makes a task's new line takes its status from those rules,
    and the same agent in a refinement made by hand and in one led through a plan takes the move to
    ready, the form of the dependencies and how a line already there is handled from them as well;
    an agent that writes the identifier of a task of a plan before that task's line exists derives
    it from the plan and the task's name, takes the characters it may hold and its being
    unambiguous from those rules, and, where they do not accept the derived identifier, asks the
    human and writes no line;
  - violates: the project skill assumes one backlog service for every product, or puts the product's
    paths inside the installer's marked block; the section holds the path of a place on the user's
    disk; an agent that finds the entry missing writes the path into the section; a skill of the-way
    writes a status of a task's line, the symbol of a dependency, the characters an identifier may
    hold, or a rule of how a line is found or changed, into its own text, or an agent takes the
    status of a new line from text the product keeps in its section or from the default of the tool
    that holds the tasks; an agent writes a line whose identifier the rules of the task place do
    not accept, or one it changed to fit them, instead of asking the human.
- **Origin:** none

*Rationale:* the product chooses its own backlog place, and a root instruction gives an agent one
place to find it. Keeping the place outside the generated block lets the product change it without
editing the process's installed guidance. A place on the user's disk is the user's own, so it stands
in the user's file and the section names the entry, which reads alike for every user; a place every
member of the team can reach stands in the section, where a new member finds it. The price taken: a
backlog can be named in two ways, and the agent that records a missing place judges which fits. The
rules by which a line of a task is handled belong to the place of the tasks, not to the product that
names it, so they are read from there and not copied beside the product, and the place can change
them without a change of the-way; the price is that the path to them stands in the user's file once
for each product, the same path repeated. The identifier of a task of a plan is the one part of a
line that the-way gives, since the refinement of one task writes it as a dependency before the line
of the task it waits on exists, so it must follow from the plan and the task's name alone; the
characters it may hold and its being unambiguous in the whole place stay the place's, with the rest
of a line. The price taken: the derived identifier can be one the place does not accept, as where
the place forbids hyphens, and the agent then asks the human and writes no line, since an
identifier it changed to fit would leave two lines naming one task differently.
*Rejected:* a fixed backlog location for all products — it would require moving an existing backlog;
asking for the location in every project conversation — the answer would be lost between sessions;
the file for every place, the section only naming the entry — every user of every product creates
the file, also where the backlog is public or lies in the repository, and a new member of a team
finds no tasks until writing the path everyone else knows; the place described in words in the
section, with its path in the user's global instructions — those instructions are not a place for
such things; the rules of the task place written at the product, its section giving the status of a
new line when none is given — the human's word was that the rules be taken from the task place and
not be written anywhere at the product, and no cost of this way is kept (`unknown`); a new line left
in the default state of the tool that holds the tasks — its status is wrong from the first moment
and the check of the notes against the lines reports a mismatch; a status of a line fixed in
the-way's skills — a skill of the-way would assume one tool for the backlog, against WAY-101; the
agent finding the rules through the user's global instructions — it does not work in a session that
does not load them, such as one in the cloud, and stands against the user's sentence that global
instructions are not the place for such things; a decision of its own for the derivation of the
identifier, narrowing this one — a rule that one skill of the-way holds with one sentence of its
reason is no entry of the log (WAY-293).

## The foundation and its entries

What a product's foundation is made of and what state it describes, and the rules every entry
shares: no version, references by identifier, mandatory links and the values of fields.

### WAY-01 — What state does the foundation describe?

On the main branch, the foundation describes the product as it is — its rules, with each invariant
the product does not yet meet marked violated (WAY-51) — and roadmaps and plans do not change it. A
task that sets out to change the foundation makes that change on its branch in the product's
repository, and the change reaches the main branch in the same merge as the code it describes; no
entry the task calls for is left for a later task. When a task closes, the foundation again matches
the current state.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: foundation-change-merge-route. For the rest, an agent compares the
  change with the decision:
  - complies: a task branch changes a decision and its code, and both reach the main branch in
    one merge; a task that brings the code back in line with an invariant changes no entry but
    that invariant's *Violated* mark;
  - violates: a planned feature is written into the foundation before it is built; the code is
    merged and the foundation change is left for a later task.
- **Origin:** none

*Rationale:* a foundation that describes intent ages with every change of direction, unseen,
because it is expected to differ from the code; one that describes the current state can be
checked against the product at any time. An abandoned task's foundation change is dropped with its
branch, leaving no false description. Whether an entry is written before the code that rests on it
or with it changes nothing on the main branch, which receives both in one merge.
*Rejected:* the foundation as a description of the target product — it ages unseen; the foundation
updated only after deployment — a step at a task's end goes missing; a "designed, not built" mark
on the main branch — an abandoned task leaves it for good; each entry written before the code that
depends on it, checked by the review — an order the merge erases, checked at every review.

### WAY-02 — How does whatever depends on an entry refer to it?

Every foundation entry has a permanent identifier, and everything that depends on it — other
entries, tests, documents and code comments — refers to it by that identifier alone, with no
fingerprint and no version beside it, and names an entry the foundation holds. A fingerprint, where
the process records one, is the first eight characters, in lower-case hexadecimal, of the SHA-256
digest of a text encoded in UTF-8, taken after every run of spaces and line breaks is replaced by a
single space and both ends are trimmed; nothing else in the text is changed before it is digested.
The one reference that carries more than the identifier is the line `decision:` of a test that holds
a sentence of a decision: it gives the number and, in straight double quotation marks, the start of
that sentence — from where a sentence of the entry begins, three words or more, compared after
every run of spaces and line breaks is replaced by a single space — so that a test whose sentence
was reworded is found, while a reference anywhere else names a decision by its number alone.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: fingerprint-definition · map-reference-target. For a reference by
  identifier alone, an agent compares the change with the decision:
  - complies: a test names the invariant it checks as `invariant: map-reference-target`; a
    decision relates to another as `derives from WAY-01`; a test that holds a sentence of WAY-12
    names it as `decision: WAY-12 "A decision is held when its"`, the number first and the start
    of the sentence after it;
  - violates: a new relation reads `derives from WAY-01@60960941`; a test cites
    `invariant: map-reference-target/1`; a line `decision:` gives the number with a suffix, or a
    fingerprint beside the quotation; a relation between two decisions carries a quotation.
- **Origin:** none

*Rationale:* an identifier outlives every rewording of its entry, so a reference by it stays valid,
and one naming no entry leads nowhere; what a change to an entry touches is found by the search its
author makes of the foundation (WAY-33), not by marks every reference carries and every rewording
renews. The digest is defined once, so a fingerprint recorded anywhere is computed the same way. A
number alone at a test points to the whole entry, which says nothing of the sentence the test
holds, and the quoted start lets a check find that sentence in the entry and point to the test of a
sentence that has since been reworded. The price: each rewording of a sentence a test holds needs
the quotation corrected, which the check points to.
*Rejected:* a fingerprint beside each reference that relies on the entry's binding part — every
rewording makes its author renew marks that change no meaning, and flags raised for nothing get
cleared unread; a version beside a reference — a reference relies on what the entry says today;
flags from the kind of change — a misnamed kind silences them; the full 64-character digest —
unreadable, nothing gained; the number alone in the line of a test — the entry it points to is
larger than the sentence the test holds, so the weakness of a number that stands for a part of a
question stays; numbered sentences or paragraphs, as a suffix of the number — a reordering of
sentences breaks the references, and a suffix beside a number is read as a version.

### WAY-04 — What makes up a product's foundation?

A product's foundation has five elements, and the list is closed: invariants, decisions, a
glossary of product terms, a part map, and environment facts. A new pattern enters the
foundation only as a field or a rule of one of the five, and only when a mechanism keeps it
without human memory: a test, a lint, a check that stops a merge, a mandatory relation or
configuration.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: foundation-file-kinds. For the rule on new patterns, an agent
  compares the change with the decision:
  - complies: a rule that every save of a game names its version enters the foundation as an
    invariant, with the test that keeps it;
  - violates: assumptions enter the foundation as a kind of entry of their own; a new field enters
    an element with nothing but an agent's memory to keep it.
- **Origin:** none

*Rationale:* each element holds what no other can, and a foundation nobody maintains gives only
paper safety.
*Rejected:* as elements of their own — tests (a method of an invariant), the "why" (a decision's
rationale), product identity, principles and non-goals (decisions), classes of task risk
(the two questions of WAY-13), structural code rules and quality scenarios (invariants), the agent's
environment and the return step (the task cycle); external constraints as a field of the map — a
fact plus the invariant it creates; environment facts as backlog hypotheses — they are true or false
today; assumptions as a kind of entry — anything inconvenient would be called one and escape
checking.

### WAY-07 — How is a foundation entry changed?

A foundation entry of any element carries no version: it is edited in place, on the main branch as
before it, and holds only its current wording; the decision log has one entry for each number, and
git keeps the earlier wordings.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** derives from WAY-01
- **Verification:** an agent compares the change with the decision:
  - complies: a decision whose rule changes is rewritten in its own entry, which then says only
    what binds; an invariant's sentence is reworded in place, and its heading stays
    `## <identifier>`; a part whose responsibility narrows has its sentence rewritten in the same
    change as the code;
  - violates: a change to a decision is appended as a second entry under the same number; an entry
    keeps a sentence that no longer binds beside the one that replaced it; a reworded fact's heading
    gains a version.
- **Origin:** none

*Rationale:* the log is read for what binds today (WAY-01), and an entry that holds only its current
wording is read whole, without assembling it from earlier ones; what an entry said before is
seldom needed, and git keeps it.
*Rejected:* a log that only grows on the main branch, every change a new version of its number —
a version restates the sentences the change leaves alone, and a reader assembles what binds from
many copies; an entry fixed from the moment it is written — every edit made during a task becomes a
version that never bound anything; an archive of past maps beside the map — git is one already; a
version of a fact cited by each check of the fact — it serves a check of the fact, which no fact
keeps (WAY-82).

### WAY-17 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends on
the other, and none is optional: a decision and an invariant name the environment facts they rest
on, an invariant derived from a decision names that decision, and a check names its invariant, or,
where it holds a decision's sentence by a line `decision:`, that decision, with no invariant
between.

- **Scope:** decisions, invariants, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: a test that holds a sentence of a decision carries a line `decision:` naming that
    decision, and no invariant is written between them; a test that checks an invariant carries a
    line `invariant:` naming it;
  - violates: a test that checks an invariant or holds a decision's sentence names neither.
- **Origin:** none

*Rationale:* the chain is the path a change travels, so a missing link breaks it without a sign,
and an assumption no entry names escapes review; the link sits in the dependent entry, because
only its writer knows what it rests on.
*Rejected:* links written by the entry depended on — it cannot know its dependents; optional
links — a missing one looks unneeded; research findings outside the environment facts — a search
from a changed finding would find no decision about agents that rests on it.

### WAY-54 — Where does the value of a field in a template come from?

The value of a field is read off the product wherever a tool can read it, and a template asks for
what a value follows from rather than for the name of a value; a value that a closed list of the
template does not hold is a question to the human, never the nearest value on the list.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a part's files are matched by git from its path patterns, never listed by hand
    beside them; an invariant's method reads `test` or `review`, which already tells its kind;
  - violates: a template asks the author to name a method's kind beside the method; a skill writes
    the nearest value of a closed list, with a reason why it will do.
- **Origin:** none

*Rationale:* an author naming a value picks the nearest with a plausible reason, and a wrong name
looks like a right one; a value read off cannot be talked into place. Where none fits, that pull
is strongest.
*Rejected:* a definition beside each value — it says nothing about a case none of them covers; a
value meaning "none of these fits" in every closed list — it records what came cheapest; a mark on
each field of a template saying whether its value is read off, transcribed or a judgment — a field
stays in a template only while someone reads it (WAY-05).

### WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every entry of its kind,
holding a value, or `none` or `TODO` where the template gives it that word: `none` says nothing is
there, `TODO` that something is missing. The main branch holds `TODO` only where an entry stands on
something the product's foundation does not hold yet: in an invariant's *Rests on*, in the form
`TODO — <the fact, with its source>`; in an invariant's *Derives from*, in the form
`TODO — <the decision, and where it is expected>`; in a decision's *Relations*, in the same form,
for any decision the entry derives from that the foundation does not hold yet, whether or not a
project definition projects it; and in a decision's *Based on*, in the form
`TODO — <what is missing, with its source>`; where an entry stands on several things and only some
are missing, the missing one is the last item of the value and reads as the form of its field,
after the known items; a change that leaves one there puts it before the human.
`elements/common/foundation_check.py` reports a missing field, or a word not given it, as an error.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common,
  task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** tests: that the script reports a bare `TODO` in a decision's *Relations*, a
  `TODO` behind a relation type there and a `TODO` joined to the relations by a comma as errors,
  and that it takes the descriptive form after known relations. An agent compares the change with
  the part no test holds:
  - complies: an invariant whose author searched the log and found no decision it derives from,
    and which was taken from no source outside the log, reads `Derives from: none`; a decision
    whose source is silent on what it rests on reads
    `Based on: TODO — <what is missing, with its source>`; an invariant whose decision is not
    written yet reads `Derives from: TODO — <the decision, and where it is expected>`; an
    invariant that rests on a fact the foundation holds and on one it lacks reads
    `Rests on: <the known fact> · TODO — <the missing fact, with its source>`;
  - violates: an invariant that rests on a known fact and on a missing one reads a whole-value
    `TODO — <both, the known fact in the description>`, or `<the known fact> · TODO` with nothing
    after the word; an invariant reads `Derives from: none` though nobody searched the log; a decision
    reads `Based on: none` where its source says nothing of what it rests on; an entry reads a bare
    `TODO` in *Rests on*, *Derives from* or *Based on*; a decision reads `TODO` in *Origin*.
- **Origin:** none

*Rationale:* an omitted field looks forgotten; an undefined value misleads. An invariant
with no test reads `review` as its method rather than `TODO` (WAY-61). An entry that stands on
something the foundation does not hold yet — a fact for an invariant, the decision an invariant
or a decision derives from, a source for a decision — can expose it as `TODO — <…>`
instead of falsely claiming `none`, and the description keeps the gap from standing as a silent
one: it names what is missing, and the human sees at the merge that it is left. Where only some of
the things an entry stands on are missing, the known ones stay named items, because every link of
the chain is written (WAY-17) and a named item stays checked as a reference, while a known one
moved into the description would no longer be; the missing one closes the value. *Origin* is what
an author states about the entry itself when writing it, so a gap there is a field left unfilled,
never a thing the foundation lacks; *Relations* may name a decision the foundation does not hold
yet, and the gap is then that decision, as in an invariant's *Derives from*.
*Rejected:* a decision for invariants alone — every element would need a copy; a wider scope for
WAY-05 — it answers how a decision entry is written; both words in every field — a word with no
meaning; optional fields left out when empty — intended and forgotten gaps look alike; for facts, a
state field and a ratcheted list — three mechanisms where one serves; keeping the ban on `TODO` on
the main branch and having the script enforce it — a cycle would stop to write a fact outside its
task; letting a bare `TODO` pass — the main branch would hold a gap that names no fact; `TODO` only
in *Rests on* — an author of a decision whose source is silent or whose higher decision is not
written yet, or of an invariant whose decision is not written yet, would have to stop the cycle or
write `none`, which is false; `TODO — projected: <the definition>, <the question of the entry>`
in a decision's *Relations*, which a script checks against the definition — a dead reference would
be caught, but the script that checks the form would have to read project definitions, and the
field would hold a second form beside the one an invariant's *Derives from* has; a partial entry of
a projected decision as the only way — it leaves the one case that remains, where the code makes no
part of the projected decision true; a form for the decision an approved project definition
projects alone — a narrower opening, but the rule of *Relations* would differ from that of
*Derives from*, and nothing would check the limit.

## Decision entries and the decision log

How a decision is written, numbered, scoped, checked and kept in the log, and what is a decision
rather than an invariant, a rule of a plan or a rule of a skill.

### WAY-05 — How is a decision entry written?

A decision entry opens with one to three binding sentences that answer its question — in the
present tense, describing a state that is to be true, concrete enough to check — and one paragraph
of one to three binding sentences for each part of another question that it answers, followed by
fields a script or an agent reads, then rationale and rejected options in prose, which, where the
entry's author writes it rather than quotes a source, names no file, script or count — a count
being how many files, tests or entries of its foundation the product holds; a measurement the
choice rests on may stand, with what was measured and under which conditions, never as a general
bound — nor what the process's own tools do or lack today, and does not tell how the decision was
reached. A field stays in the template only while someone or something reads it, and what a
decision forces on later work stands in a binding sentence or a field, never in prose. An example
in `elements/decisions/` names a decision of the log by its number instead of copying it.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** for the fields, an agent compares the change with the decision:
  - complies: a new field enters the template together with the reader named in its table;
  - violates: a "notes" or "related artifacts" field that nothing reads.
  For the rationale, an agent compares the change with the decision:
  - complies: a rationale gives '12 loops fit in a save with the longest program, 16 and 19 with
    shorter ones';
  - violates: a rationale gives 'at most 12 loops' with no conditions, or how many entries the log
    held when the decision was taken.
  For the binding sentences, an agent compares the change with the decision:
  - complies: an entry answers its question in a paragraph of two sentences and gives the part of
    another question that it answers its own paragraph of one sentence;
  - violates: an entry answers its question in a paragraph of five sentences; a part of another
    question is folded into the paragraph of the main question, which then runs past three
    sentences.
- **Origin:** none

*Rationale:* a record written like a legal code is followed worse, and agents generalise from the
reasons they are given, so what binds stays short and checkable, reasoning below; a field
nobody reads goes empty, and long lists of fields stop people recording decisions. The prose gives
only what a reader needs to understand the choice: the history of the product or of the decision —
what the product held, how the choice was reached — is information the reader does not need, while a
measurement the choice rests on is a reason for the choice. A part of a question that an entry
already answers is a paragraph of its own, so that what binds each part stays as short as what
binds the main question, and a reader or a test finds its sentences without sifting the rest.
*Rejected:* prose without fields — nothing a script can read reliably; many fields and relations —
fields without a reader; a hand-written status — every entry of the log binds; a one-sentence
entry — no reasoning beside the rule; "will" or "should" — an intent, not a state; capitals such as
MUST — shouting reads worse, not stronger; examples written for the template — an example with gaps
teaches gaps; a rule of the template changed only with a decision citing its number — the template
is the-way's own text, changed and reviewed like any other change to it; no number of sentences,
each binding sentence answering the question of the entry or a part of it — nothing keeps an entry
short, and the principle that what binds is short weakens; a higher fixed limit — a number with no
ground that breaks at the first topic with more parts than it allows.

### WAY-12 — How is a decision checked?

A decision names in *Verification* the invariants derived from it, by the identifiers of their
entries, where such invariants exist, and the tests that hold its sentences, by a clause that gives
the parts of the sentences they hold in words and no path, no test name and no number. A test that
holds a sentence of a decision carries beside it a line `decision:` that gives the number of the
decision and the start of that sentence, and the decision keeps its rationale and its rejected
options whole. A decision may also carry a pair of examples — a change that complies and one that
violates — only for the part of its sentences that no invariant and no test checks, with which an
agent compares a change with that part; the violating example is a change whose code goes against
the decision while its entry stays as it is, never one that replaces the decision together with its
code.

A decision is held when its *Verification* names an invariant, when a test holds a sentence of it
by a line `decision:` that names its number, or when it carries a pair of examples. The check of
the foundation reports as an error a decision that a change adds, or whose binding sentences the
change alters, and that nothing holds. Any other decision that nothing holds stands in a list the
check prints, and the list stops no change.

- **Scope:** decisions, invariants
- **Based on:** llm-decision-violation-detection
- **Relations:** none
- **Verification:** tests: that a line `decision:` of a test names a decision of the log and quotes
  the start of one of its binding sentences; which decisions the check counts as held; the error
  for a decision a change adds or alters that nothing holds, and the list of any other. An agent
  compares a change with the part no invariant and no test holds:
  - complies: a decision on the product's direction carries a complying and a violating example
    and names no invariant; a decision with a derived invariant names it after `invariants:`; a
    decision whose sentence a test holds is named at that test by a line `decision:`, names such
    tests by a clause with no path and keeps a pair of examples only for the part of its sentences
    that no test holds, its rationale and rejected options staying whole;
  - violates: a decision names an invariant whose *Derives from* names another decision; a
    decision asks for a human's assessment recorded in its entry; the violating example of a
    decision is a change that takes an option the decision did not take and rewrites the decision
    in the same request; a decision names a test that holds its sentence by the test's file or
    name; a decision whose sentence a test holds loses its rationale and its rejected options
    together with its pair of examples.
- **Origin:** none

*Rationale:* a test checks an invariant on every commit; a decision about direction or trade-offs
often cannot be. Agents judge explicit, code-readable decisions well and deployment- or
organisation-dependent ones poorly, a finding this decision takes across publishers (WAY-85), so a
pair of examples marks the line where it helps, and the human who accepts a change sees the rest. A
sentence of a decision that a test holds is checked on every commit as an invariant is, and its link
to the decision stands once, at the test, so the decision names such tests only in words and keeps
no second copy of the link that breaks when a file moves. Where a test holds a sentence the pair of
examples says nothing more, but the reasoning and the rejected options stay, since a test cannot
say why. A decision that nothing holds is a rule nobody can tell is followed, so a change that adds
or alters one holds it before it merges, while the older ones are listed and wait, because a gate
that stopped every change until each of them was held would stop all work.
*Rejected:* a rule in code as the only check — decisions that cannot be written as a rule go
unchecked; a level of verification named in every decision, a human's assessment among the levels
— the level adds nothing to the invariants named and the examples given, and every change already
reaches a human before it binds (WAY-14); the behaviour of a product left out of the log
altogether — the variants tried and rejected are lost; an error for every decision that nothing
holds — no change to a product passes until all the older ones are brought up; only a list, with
no stop — decisions that nothing holds keep arriving and the list grows.

### WAY-18 — How is a product's decision log kept?

A product keeps all its decisions in one log, whatever they are about. The log holds one entry for
each decision in force and itself says what binds today, with no view generated from it kept in
its place; the index of a selection of decisions that an agent writes on demand (WAY-150) is no
such view. A link between entries is written at one end only; the one exception is a decision's
invariants, which its *Verification* names while each of them names the decision in *Derives from*.

A log may be divided into topical sections, each a heading with one sentence of what it covers, its
entries keeping their numbers; in a log so divided a new entry stands at the end of the section of
its topic, or, where no section fits, in a new section at the end of the log, which the request that
adds the entry names. A log without topical sections holds its entries in the order they were
written, a new entry at its end.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a business rule and a technical constraint of one product stand in the same log
    under one numbering; a product's existing architecture records stay a source, and a decision
    recovered from them enters the one log; an agent writes the index of the decisions it selects
    into a file of its own working directory, and the log stays the one account of what binds;
  - violates: a separate log for business decisions next to the technical one; a decision that
    another narrows names that other in its own *Relations* as well; the index of the log's
    decisions is kept as a file of the repository beside the log.
  For where an entry stands, an agent compares the change with the decision:
  - complies: in a log divided into topical sections a new decision on how a reviewer grades a
    finding takes the next free number and stands at the end of the section on review; a decision
    that fits no section opens a new section, with its heading and sentence, at the end of the log,
    and its request names that section; a log without sections takes a new entry at its end;
  - violates: a new entry of a divided log stands at the end of the log under a section of another
    topic; the division of a log renumbers its entries to follow their sections; a new section is
    opened between two sections, or its request does not name it.
- **Origin:** none

*Rationale:* one log, because a collision is caught only between decisions in the set a change is
checked against; the log itself says what binds, so a reader reaches it without assembling versions
or generating a view; a link is written once, because two copies of it drift apart. The index of a
selection of decisions that an agent writes on demand (WAY-150) is no such view: it stands in no
file of the repository, serves the one piece of work it was written for, and leaves the log the one
account of what binds. Entries ordered by topic let an agent choose the decisions of its work's
topics by a section's heading and sentence, which the order of writing, scattering one topic across
the whole log, does not allow; the number stays the question's (WAY-19), so moving an entry into a
section breaks no reference. A new entry joins the section of its topic so that the sections keep
holding what they say, and an entry that fits none opens a section at the end, which the request
names, so the human sees a new topic of the log at the merge. A log without sections keeps the order
of writing, the one order it has.
*Rejected:* a log of every version and review, with a view of what is in force generated from it —
the view is one more thing to build and keep, and the history it leaves behind is what git keeps;
marks written by hand at a link's other end — they go missing; separate logs for business and
technical decisions — collisions between them go unseen; a log per approver — git records who
merged each change (WAY-14); a field for an entry's topic — nothing reads it (WAY-05).

### WAY-19 — How are decisions numbered?

A number stands for the question a decision answers, carries the product's prefix and is given
in the order entries are written; a new question gets the next free number, a question independent
of every existing entry included, while a part of the question an existing entry answers is a
sentence of that entry where it cannot change without changing that entry. A new answer to a
question the log holds rewrites that question's entry. When a new decision answers a question that
an older one answered in passing, the sentence moves to the new decision, and the older one loses it
in the same change.

- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: a new rule for who accepts a decision, which cannot change without changing WAY-14,
    is written into WAY-14; a rule that answers a question no entry holds gets the next free
    number; when a decision on a question arrives, an older decision that answered it in passing
    loses that sentence;
  - violates: the same question gets a second number; the sentence stays in both decisions; a part
    of a question that WAY-14 answers gets a number of its own although it cannot change without
    changing WAY-14.
- **Origin:** none

*Rationale:* a permanent number lets references survive a change (WAY-02); a new answer rewrites
the one entry, so no reader assembles the decision from pieces; a sentence answered in passing
moves, because two entries answering one question drift apart; a part of a question that cannot
change apart from its entry stands in that entry for the same reason, and a question that can
change on its own keeps a number of its own; the product's prefix keeps numbers of different
products apart in references.
*Rejected:* a new number for every change, the old entry marked as replaced — references rewired or
left on a dead entry; numbering by topic — topics move, and numbers would move with them; a new
version of the number for every change — a reader assembles what binds from many copies (WAY-07).

### WAY-21 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never
file paths, so that the decisions governing a change are found from the files it touches through
the part map's rule for assigning files.

- **Scope:** decisions, part-map, task-cycle
- **Based on:** instruction-density-accuracy
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision governing the part map names `part-map` in its *Scope*;
  - violates: a *Scope* names `foundations/part_map.md`.
- **Origin:** none

*Rationale:* an agent can apply only decisions it sees. The part map already assigns files to
parts, so using those parts as scope makes the governing decisions discoverable without copying
paths into each entry. Scope alone selects widely, since a part of a process or a product is
governed by many decisions: measured on 2026-11-15 on the-way's own log, by a search of the *Scope*
lines of all its decisions, about half of them name the part of the task cycle, so a change to that
part selects about half the log. Topics cannot be derived from changed files, so in a log divided
into topical sections an agent chooses the sections of its work's topics by their headings and
sentences, while scope still finds, from the files a change touches, each decision outside those
sections that governs a touched part, whose question the agent then runs through (WAY-150); topics
narrow the reading and scope keeps a governing decision from being lost.
*Rejected:* file paths in each decision — duplicate the map; topics in place of scope — they cannot
be derived from a change, and a decision of another topic that governs a touched part would be lost
without a trace; no scope — relevant decisions get lost among the rest.

### WAY-22 — Is a rule a decision or an invariant?

An invariant says nothing about why or what was rejected; a decision is a choice between
options, with its rationale, and it binds later work until a change replaces, narrows or withdraws
it, including what cannot be checked on a commit — direction, trade-off principles, non-goals. A
rule that records a choice is a decision, and what of it a commit can make false is written as an
invariant derived from it, unless a test holds that sentence by a line `decision:`, in which case
the decision gets no derived invariant for it; an invariant stands for a rule with no choice behind
it and for a rule on which several decisions stand. A single text, number, list or location is no
entry of the log: it stands in the product's data or code, with the test that holds it and, where
its reason is not obvious, a comment at the value.

- **Scope:** decisions, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "the product has no multiplayer" is a decision, and "no screen offers a second
    player" an invariant derived from it; "a saved game is never lost on reload" is an invariant
    with a test; a sentence of a decision on how long a transition lasts is held by a test with a
    line `decision:` and gets no invariant; the text of a button stands in the product's code with
    the test that holds it;
  - violates: a non-goal that a commit can break is left with neither a derived invariant nor a
    test holding it by a line `decision:`; an invariant carries a rationale and rejected options; a
    sentence of a decision that a test holds by a line `decision:` also gets a derived invariant; a
    single text of a screen is written as a decision.
- **Origin:** none

*Rationale:* an invariant is checked mechanically on every commit, a decision weighed when a later
choice is made; a checkable rule left only in a decision's prose escapes the gate, and a choice
written only as an invariant loses its reasons. A sentence a test holds by a line `decision:` is
already checked on every commit and tied to its decision at the test, so an invariant beside it
would be a second entry for the same test and the same rule. A single value carries no choice
that a later reader could take otherwise, so its entry would repeat what the code and its test say,
while a comment at the value keeps a reason that is not obvious where the value is changed.
*Rejected:* one kind of entry for both — either the gate reads prose or the reasons are lost;
moving a checkable sentence out of its decision — the rule would be cut off from its reason, which
holds for a sentence, while a single value, which carries no choice, goes to the product's data or
code with its test and comment; a derived invariant for each checkable part of a new decision, the
line `decision:` only marking tests that already mention a number — the change comes down to
tidying old tests, and new decisions go on producing a decision and an invariant in pairs.

### WAY-26 — How are trade-off principles and non-goals written?

Each trade-off principle is a decision of its own, whose binding sentence says which of two good
things is chosen when they conflict and whose rationale names the problem it solves. Each
non-goal is a decision of its own that says what the product does not do and why. What the product
does not do only because no work has brought it yet is no non-goal: where later work builds on it,
a decision states what the product does today.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "When speed of release conflicts with completeness, we choose speed", an entry of its
    own whose rationale names the problem; "The product has no multiplayer", with its reason, as an
    entry of its own; deleting a character, left out of a first release, written as "A character
    stays in the team once created", with the invariant derived from it, where later work builds
    on it;
  - violates: a principle naming one good thing only ("we value quality"); several principles or
    several non-goals in one entry; a feature left out of a first release written as "The product
    does not delete characters".
- **Origin:** none

*Rationale:* a principle rules later choices only when it names what it gives up; the rationale names
the problem, so a later reader can tell when the principle stops serving it; one entry each, so each
changes on its own and precedence is recorded pair by pair (WAY-25). A non-goal names a direction
the product chose, so a feature not yet built, written as one, reads as that direction and closes a
path nobody chose to close.
*Rejected:* several principles or non-goals in one entry — a change to one reopens them all, and no
precedence can be recorded between them.

### WAY-29 — How is a decision recovered from an existing product written?

A decision recovered from the code of an existing product says in *Origin*, in one sentence, that
it was recovered from the code and where in the code it shows, and its rationale and rejected
options are quoted from a source, given by a human who knows them, or written as `unknown`. A
rationale an agent proposes for a human's decision goes to the human as a question, never into the
entry; the rationale of a decision an agent takes in a task is the agent's to write. The
description of the commit, or of the merged request, that brought the shape of the code is such a
source: an agent looks there before it writes `unknown`, and quotes what it finds with the
identifier of the commit.

- **Scope:** decisions
- **Based on:** llm-design-rationale-expert-overlap
- **Relations:** derives from WAY-28
- **Verification:** for *Origin*, an agent compares the change with the decision:
  - complies: the *Origin* of a decision recovered from a product's saving reads `recovered from
    the code at src/core/save.py, save_game`;
  - violates: *Origin* lists what was searched and what was found.
  For the agent's role, an agent compares the change with the decision:
  - complies: an agent finds the reason in the description of the merged request that brought the
    shape of the code, and quotes it with the identifier of the commit; an agent finds nothing there
    and asks, and the entry gives the reason under the name of the human who knew it; the
    *Rationale* of a recovered decision whose reason nobody knows, the description of the commit and
    of the merged request having been looked at, reads `unknown`;
  - violates: an agent writes a plausible reason inferred from the code into the entry; an agent
    lists in *Rejected* the options it infers were weighed; an agent writes `unknown` without having
    looked at the description of the commit or of the merged request that brought the shape of the
    code.
- **Origin:** none

*Rationale:* a reason an agent writes looks exactly like a recorded one, and later readers take it
for the reason the decision was made; a human who knows it is a source, a guess is not. The cited
study compared generated arguments with expert rationale after giving models the problem and
decision; it did not test recovery from code, and argument overlap is not a correctness rate. The
place in the code shows a reader where the decision acts, and `unknown` shows nobody knows what the
decision guards. The description of the commit or of the merged request that brought the shape of
the code is where a reason stands, if one was written down when the code was made; `unknown` says
that nobody has a reason, so it is written once that place is looked at, and the identifier of the
commit lets a reader open the same description.
*Rejected:* an agent's rationale in the entry — read as the reason the decision was made; rejected
options filled in as `none considered` — nobody knows what was considered; *Origin* recording what
was searched and what was found — a list nothing reads once the decision is written, while the
place in the code says where to look.

### WAY-36 — Is a rule a decision or does it belong in a plan?

A rule enters the decision log only when it still binds once the change that brings it has been
merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition
between two states — stays in the plan of that work, or in the choices of its cycle record
where no plan is written.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "the foundation reaches the main branch whole, once every element is ready" stays in
    the plan of building the foundation; "when what entries wait for arrives, they are fixed in
    the same change" enters the log; an exclusion that ends with a task without a plan stays
    in the choices of its cycle record;
  - violates: a decision on the order in which elements are built; a decision whose binding
    sentences say what happens until the first merge; an exclusion that ends with its task
    written into the log as a product non-goal.
- **Origin:** none

*Rationale:* a plan written in the present tense reads like a decision, and WAY-01 gives no way to
recognise one. The log binds on the main branch (WAY-01), and a rule that ends when its change is
merged binds nothing there: from its first day it records work already done.
*Rejected:* plans written into the log and taken out once done — the log holds, while the work
lasts, a rule that binds nothing once the work is merged.

### WAY-293 — What prevails where a task or its spec excludes the entry for a choice?

Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion
prevails over the rule that a choice binding after the merge goes to the place the questions of the
decisions template give it, and the choice stays a row of the cycle record's questions table;
without such an exclusion the rule applies as before. In the area of choices that a task or its spec
explicitly excludes from the foundation, this decision prevails over WAY-22 and WAY-18. A candidate
left out of a task's *Settlements to record* is no exclusion.

In the log of the-way, a rule that stands in one skill or template of the-way stands there with one
sentence of its reason. It is an entry of the log only where it carries a choice with a real cost,
one for which someone could reasonably propose the rejected way, and the skill or template then
names that decision.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** narrows WAY-22 · narrows WAY-18
- **Verification:** an agent compares the task, its spec, the cycle and its record with the
  decision:
  - complies: a spec that says the choice of a form gets no entry in the foundation leaves that
    choice as a row of the questions table, and the cycle writes no entry for it; a task that
    excludes nothing has each choice that binds after the merge written in the place the questions
    give it; a rule of how an agent works that stands in one skill of the-way stands there with a
    sentence of its reason and no entry, while a choice of the process that someone could
    reasonably take otherwise has an entry that the skill names;
  - violates: the cycle writes an entry for a choice the task or its spec excludes; a choice that
    passes the questions is left out of the foundation because it looks small, with no exclusion in
    the task or its spec; a candidate the human did not accept into the task's *Settlements to
    record* is taken for an exclusion; a rule that only one template of the-way holds is written as
    a decision beside it, repeating its text; a skill states a choice with a real cost and names no
    decision.
- **Origin:** none

*Rationale:* without a recorded precedence, a cycle meets a task or spec that says "no entry" beside
a rule that a choice binding after the merge goes to the place the questions give, and beside WAY-22
and WAY-18, which give every choice that records a rule a place in the one log; the agent that meets
the collision may not settle it silently (WAY-25). A task or spec that excludes an entry says so in
words, so the exception is limited to what was said and the default stays: a choice that binds
after the merge goes to the place the questions give it. The choice is not lost, since its row stays
in the questions table, and the section for the human's decisions puts the cycle's choices beyond
the task before the human (WAY-287). The price is that the reasons for rejecting the other ways of
such a choice go with the spec; that a later change can rework its rule without contradicting any
entry; and that nothing in the foundation says the choice has no entry. In the log of the-way, whose
product is its skills and templates, a rule written in one of them with its reason beside it is
found where it acts, and an entry beside it would repeat that text and drift from it; a choice with
a real cost keeps its entry, since its reasons and rejected ways would otherwise be lost and a later
change could rework the rule with no entry to contradict.
*Rejected:* an exception for every choice written in the text of a skill or template, with no entry,
unless the task or spec asks for one — for a choice with a real cost, and for a product's log, the
reasons and rejected ways of such a choice are lost with the spec, a later change can rework the
rule without contradicting any entry, and the exception goes against WAY-22 and WAY-18, while for
the rest of the-way's log it is taken as the second paragraph gives it; the log of the-way with no
question that sends an instruction for how an agent works to a skill, every rule of a skill or a
template staying a decision — the log goes on growing at its pace, many of its entries only
repeating one template or skill; no change — the
return step is left without a precedence between the exclusion and the rule that a choice binding
after the merge goes to the place the questions give, and the choice is weighed again at each stage
that meets it; letting only the task exclude an entry, not its spec — where a spec excludes the
entry for each of several choices, the cycle writes a decision for every one of them and the log
grows.

## Accepting and applying decisions

Who accepts a decision and from when it binds, what a decision is to refinement, what settles a
collision or a contradiction with one, and how one that rests on a prediction is reviewed.

### WAY-14 — Who accepts a decision?

A decision, and every change to it, binds once a human accepts it, never an agent. In the-way,
that human is Mariusz.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision written on a task branch binds once Mariusz merges its request, and its
    entry holds no field naming him;
  - violates: an agent merges a request that carries a decision; an entry is edited once its
    request is open only to record who is to approve it.
- **Origin:** none

*Rationale:* a decision binds the agents that follow, so none of them accepts one. The merge is the
act by which a human accepts a change (WAY-114), and git records it with the person and the time; a
field restating it is a second copy kept in step by hand.
*Rejected:* a field in every entry recording who approved it and when, or the link of the request
whose merge accepted it — a copy of what git records, written in by hand once the request opens; a
field in every entry naming who is to approve it — the same name repeated, stale once the team
changes; lists of decision-makers and of those consulted — nothing reads them.

### WAY-24 — How is a decision that rests on a prediction reviewed?

A decision names no date or condition for its review and the log holds no record of a review. The
review of the foundation against the product is a run of the skill `review-foundation`, which a
human starts in a session with an agent when the reminder of a request asks for it (WAY-300) or at
any other time. A task of the product's backlog may stand for that run, and a human adds it, never a
cycle.

- **Scope:** decisions, foundation-review
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision's entry holds no field for its review; a request that says the
    foundation waits for a review names the skill, and the human starts it in a session; the human
    adds a line for the review to the product's backlog, and the session that runs the skill is the
    review;
  - violates: an entry carries a check-by date; a record of a review is appended to the log; a
    cycle adds the line of the review to the product's backlog; the review is run by a cycle that
    ends in a request of the changes it judged.
- **Origin:** none

*Rationale:* a date in an entry asks for a look nobody is sent to make, and passes unseen; a review
of the whole foundation, run as a skill in a session with the human, looks at all of it at once and
brings each result to the human as a proposal to decide on, where a cycle of a task would bring them
as ready changes. A line of the review in the backlog is a mark the human's own session answers to,
and the human adds it because the backlog lies outside the repository, where only a human makes an
effect (WAY-140).
*Rejected:* *Review when* in each entry, with an observable state and a check-by date, and a review
record appended on the date — the dates pass with nobody looking; a decision that expires on a date
— the date gets extended; the review set as a task of the backlog, run by a cycle that ends in a
request of corrections — the judgments of whether an assumption stands arrive whole as ready
changes with no talk, and refusing one is another round; a task of the review made ready for a cycle
and copied into the backlog — three steps where one command does; a script — it does not judge
whether the assumption of a decision stands; the cycle adding the line of the review to the backlog
itself — it would need a change to WAY-140, against the reason of WAY-161, and a product with its
backlog in an outside tracker would give the cycle the right to write outside the repository; a
sentence that asks for no line and says nothing of the backlog, the human's own setup adding the
line — another user of the-way is left with a sentence that can be scrolled past.

### WAY-25 — What settles a collision between two decisions?

Where two decisions both apply and collide, the one that prevails names the other in *Relations*
as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a
chain, and two decisions that narrow each other are an error. A collision between two decisions
with no precedence recorded is never settled silently by the agent that meets it. Where what the
human accepted gives the outcome and the change may write the decision that prevails, the change
records the precedence in that decision, and its request names it with the passages of what the
human accepted that give the outcome, for the human to accept at the merge (WAY-114); otherwise
the agent stops and asks.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: an agent meets two applicable decisions that pull opposite ways, finds no
    precedence between them, and finds that the task document the human accepted gives the
    outcome, in one passage or in two read together: it records the `narrows` and the area in the
    decision that prevails, and its request quotes those passages for the human to accept at the
    merge; an agent meets two such decisions and finds that what the human accepted does not give
    the outcome, or that the change may not write the decision that prevails, stops and asks for
    the precedence;
  - violates: an agent settles the collision in favour of the newer decision; an agent infers
    that A prevails over C because A narrows B and B narrows C; the change records a precedence
    that no passage of what the human accepted gives, or one its request does not name with those
    passages.
- **Origin:** none

*Rationale:* pairs record only what someone actually weighed; nothing follows along a chain, because
A over B and B over C were weighed in different situations; an agent that settles an unrecorded
collision silently makes a trade-off no human made. Where what the human accepted already gives the
outcome, the trade-off is the human's and the agent only writes it down; the request quotes the
passages that give it, so the human at the merge tells an entry that follows from a settlement the
human made from one the agent invented, and strikes the latter. Whether the accepted passages give
the outcome stays the agent's judgment, and the quoted passages are what that judgment is checked
by. The decision that prevails holds the record, so a collision whose prevailing decision the change
cannot write, such as one outside its own repository, still goes to a human.
*Rejected:* one ranked list of principles (AWS tenets) — an order claimed for pairs nobody weighed;
levels of authority over whole groups of decisions — a collision inside a level stays unresolved;
the newest decision wins — the date of a decision is not its weight; every precedence recorded by
a human alone, the agent stopping at each collision — a nearly finished cycle stops for an entry
whose content the human has already accepted; an exception only for a settlement that says which
decision prevails — the outcome can follow from settlements that do not say so; the wording that
the change writes the `narrows` and its request names it — it reads as the line of *Relations*
alone, and an entry named without the passages it follows from leaves the human to open the task to
judge it; the precedence recorded in the decision that prevails with no passages in the request —
the entry is stated, but not where its outcome comes from; one passage of what the human accepted
in the singular — an outcome can come from two passages read together, and an agent reading the
wording literally would stop where the outcome is given.

### WAY-30 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan, or into its task
document where no plan is written, and approved with that plan or document by the human who accepts
decisions (WAY-14) before the code that needs it is made; that approval, including a change carried
by a row of *Settlements to record*, answers the question WAY-114 requires, so the agent writing the
entry asks only about a meaning beyond what the approved plan or task document carries, and in this
area this decision prevails over WAY-114. When a contradiction shows only during implementation,
the agent stops, quotes the decision by its number, and either brings the change into line, drops
the change, or proposes on the task branch an edit of the decision, a new wording or a narrowing,
and the code that needs it waits for that human. An exception written in advance into a decision's
binding sentences is not a contradiction, and no exception lives only in a task document, plan or
cycle record.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01 · narrows WAY-114
- **Verification:** an agent compares the change with the decision:
  - complies: a task branch whose code goes against a decision carries a proposed narrowing, and
    the merge waits for the human who accepts it; a task without a plan carries the known decision
    revision in its task document, accepted by that human before dependent code, and the entry's
    author records that meaning without asking again; a further meaning goes to that human;
  - violates: a task branch whose code contradicts a decision that stays unchanged; a task's plan
    that records a "justified violation" of a decision; a task without a plan treats the
    orchestrator's go-ahead as approval of a decision revision; the entry's author asks again about
    an accepted settlement, or extends its meaning without asking.
- **Origin:** none

*Rationale:* an exception kept only with the work leaves the foundation describing what the code no
longer does (WAY-01); stopping shows the contradiction when it is found. Aligning or dropping the
change leaves the decision intact, so the agent may do either; changing the decision is the
human's. Asking again about the meaning already approved spends attention without presenting
a new choice; a meaning beyond it still needs that choice.
*Rejected:* a justified violation recorded in the plan, the decision unchanged — the foundation
stops matching the code; a whole new answer as the only way to change a decision — a narrow
exception takes the whole decision with it; repeated approval of the same meaning — the human
answers a question already settled; an implied exception to WAY-114 — competing instructions leave
the entry writer to choose which one governs.

### WAY-114 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a
projected entry at the readiness gate, shown as one sentence in the human's language with the entry
beside it; that of an entry written whole from an accepted row of a task's *Settlements to record*
with the task document, the row being the human's own settlement; and that of every other entry at
the merge of the change that holds it, where the section of the request's description for the
human's decisions gives one plain sentence of its meaning with no identifier, repeated in the
human's language in the description's collapsed block, while the full list of the change's entries,
each by its identifier with one English sentence of its meaning, stands in the description's lower
part, and an entry that is marked as the cycle's because of a pair of examples its writer added has
that pair there word for word under it. Before that, a question goes to the human only where the agent has no recommendation or the
entry would change the meaning of an approved decision; a translation never enters the foundation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: the readiness gate shows each projected entry's meaning as one sentence in Polish with
    the entry beside it; the request's section for the human's decisions gives a plain sentence of
    the meaning of each entry the cycle wrote with no row or projected entry carrying it — from the
    spec, a correction the search of the foundation made, the part of a projected entry — repeated
    in Polish in the collapsed block, while every entry, those from rows and projected ones
    included, stands by its identifier in English in the lower part, and an entry that gained a
    pair of examples the row did not give has the pair there word for word; the human reads that
    section and merges;
  - violates: an agent asks the human to confirm a choice it already recommends; a translation is
    written into the foundation; an entry changes the meaning of an approved decision without a
    question; an entry written from the spec stands only in the lower part; the section for the
    human's decisions lists the entries written from accepted rows; an entry marked as the cycle's
    for an added pair of examples reaches the merge with the pair not shown.
- **Origin:** none

*Rationale:* the human judges what an entry settles, and its wording rarely changes that. A row is
the human's own settlement, accepted with the task document, and a projected entry is wording the
gate approved; asking again at the merge buries the entries the human has not seen among those
already accepted, and a list the human does not read accepts nothing. The price is that an entry
whose wording drifts from its row reaches the merge unseen by the human, and the review of the whole
change, which reads the entry against the row, is what catches it (WAY-134, WAY-10).
*Rejected:* acceptance of the whole wording before an entry is written — attention goes to wording
while the meaning rarely moves, and each acceptance costs a round; storing a translation in the
foundation — two binding wordings could drift apart; the sentence of meaning alone for an entry
that gained a pair of examples — the examples are what agents measure every later change by, and a
sentence of meaning does not show them; every entry of the change at the top of the
request with its sentence in Polish, as before — a wall of text the human does not read; the full
list in the lower part and nothing about the entries at the top — the entries the cycle adds enter
without the human's knowledge; at the top also an entry from a row whose wording the cycle wrote,
where it differs from the human's sentence by more than words — asked again, the human chose to be
shown only the entries no row carries.

### WAY-313 — What is a decision of the foundation to the refinement of a project or a task?

While a project definition or a task document is refined, the technology step included, a decision
of the foundation describes what the product does today and is material for revision, not a limit
on the options: refinement shows an option that changes a decision as it shows any other, with the
decision it changes named by its identifier, and may recommend it, asking no leave to open the
decision first. This holds only before the cycle starts (WAY-315). A projected decision of an
approved definition is no such material: a change of it goes through the definition and its
readiness gate (WAY-118).

- **Scope:** project-level, elements-common, decisions
- **Based on:** none
- **Relations:** derives from WAY-14 · derives from WAY-30
- **Verification:** an agent compares the work with the decision:
  - complies: refining a task, an agent finds that a decision keeps the records of a service for a
    week while the task needs a month, shows the month as one option beside the week with the
    decision it changes named, recommends it and asks nothing before showing it; the technology step
    at a definition shows a way of logging in that a decision holds as an open choice, the decision's
    present answer among the options, when it sees a reason to change it; a refinement of a task
    that would change a projected decision of an approved definition sends the human to the
    definition and its readiness gate;
  - violates: a refinement leaves an option out of its comparison because a decision holds the
    choice; an agent asks the human for leave to show an option that changes a decision; a
    refinement of a task changes a projected decision of an approved definition in the task's
    document.
- **Origin:** none

*Rationale:* a decision records what the product does today. Refinement settles what a project or a
task will change, where anything may still change, so a decision that kept the agent from showing a
better option would hide from the human the very option the refinement exists to weigh; the human
still decides every change (WAY-14). A projected decision of an approved definition stays outside
because the definition and the plan of its tasks rest on it, and a change made for one task would
leave them saying the old thing with no sign (WAY-118). The price is that refinement reaches
decisions more often, and a hurried one could open decisions nobody needed to open, which the
human's choice among the options answers (WAY-314).
*Rejected:* for the sentences that open the entry, unknown; for its last sentence, a task that
changes a projected decision with one choice, as it changes a decision of the foundation — the
definition and the plan go on saying the old version, other tasks of the plan diverge with no
signal, and bringing the change into the definition and the plan is a larger task.

### WAY-314 — Which act of the human consents to a change of a decision that refinement shows?

Where refinement shows an option that changes a decision of the foundation (WAY-313), the option says
in its line which decision it changes, and the human's choice of that option is the human's consent
to the change (WAY-14); the acceptance of the complete task document, or the approval of the
projected entries at the readiness gate of a definition, asks nothing about that change a second
time. A task document carries the change and its cycle writes it with the code that needs it
(WAY-30), and a definition carries it as a projected change of the decision.

- **Scope:** project-level, elements-common, decisions
- **Based on:** none
- **Relations:** derives from WAY-14 · derives from WAY-30 · derives from WAY-313
- **Verification:** an agent compares the work with the decision:
  - complies: a comparison of two ways to keep a record shows the option that changes a decision
    with the line "changes WAY-xx: the record lives a month, not a week"; the human chooses it, the
    task document holds the choice under its question and the decision under its *Decisions in
    play*, and the acceptance of the document asks nothing about that change beyond the reading of
    the document;
  - violates: the acceptance of the document carries a separate point asking the human to approve
    the change of the decision again; an option that changes a decision does not name it in its
    line; the choice of such an option is treated as preliminary until the document is accepted.
- **Origin:** none

*Rationale:* the human sees what a change costs where they choose between the options, so the choice
is the moment of consent; a second consent to the same change asks again what was weighed and spends
the attention that the acceptance of the whole document needs for the rest of it (WAY-114). The
option names the decision it changes so that the change does not hide in an answer that reads as a
plain one. The price is that a change missed at the choice stands in the document with no separate
question, and only the reading of the document at its acceptance catches it.
*Rejected:* the acceptance of the whole document as the consent, the choice among the options
preliminary and the change a separate point at the acceptance — a second consent to the same change:
its effects are seen at the choice, and the consent is given later.

### WAY-315 — From when does a decision of the foundation bind the work on a task?

A decision of the foundation binds the work on a task from the start of the task's cycle, the
writing of a spec in the cycle included. In the cycle no agent departs from a decision on its own and
returns with the question, as WAY-30 gives, and the looser rules that refinement follows for
decisions (WAY-313, WAY-314), for the rows of its settlements (WAY-134) and for the question
against an answer (WAY-113) hold only before that point.

- **Scope:** task-cycle, project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-14 · derives from WAY-30
- **Verification:** an agent compares the work with the decision:
  - complies: the author of a spec who sees a better variant than a decision on the life of a record
    does not take it and returns with the question for the human, as WAY-30 gives, while the
    refinement of the same task showed that variant as an option beside the decision;
  - violates: the author of a spec writes a design that departs from a decision on its own; an agent
    of a cycle treats a decision as material because a spec, not code, is being written.
- **Origin:** none

*Rationale:* a spec fixes the design the code is made to, so a decision that gave way in a spec
would give way in the code, and the cycle runs from its start to its request with no human between;
the decision therefore binds from the start of the cycle. Before it, a human reads and accepts the
document that frames the work, which is the place to weigh a change. The price is that the author of
a spec who sees a better variant than a decision cannot take it alone, which costs one round through
the human.
*Rejected:* binding only from the writing of code, the spec of the cycle treating a decision as
material and the consent given at the request — a change of a decision reaches the human at the
request with code already built on it, and the cycle no longer goes from its start to its request
without a human.

## How skills write and read the foundation

How an agent selects the foundation it reads, searches the whole foundation for what an entry
touches, asks the human and has a proposal critiqued, and what an element's skill holds.

### WAY-33 — What does the author of a foundation change search for?

When a change writes a foundation entry or changes its binding part, its author, once the entry is
settled, searches the whole foundation once for the entries the change touches — those that name
the entry or that it names, and those no written link joins to it — and before the change is
accepted each finding becomes a link, a change to one of the entries in the same change, or a
question to a human. The search is not repeated before the merge and leaves no record.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle,
  agent-instructions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision to keep the game's whole state in the browser is written, and the search
    finds an unlinked requirement that players log in; a reworded decision leads its author to the
    invariants that derive from it, and each is brought in line in the same change;
  - violates: the search reads only the decisions whose scope overlaps; a reworded decision is
    merged while an invariant deriving from it still states the old rule.
- **Origin:** none

*Rationale:* a link names an entry by its identifier and no change flags it (WAY-02), and the
costliest contradictions lie between entries written apart, where nobody thought of a link, so only
a search of the whole foundation finds what a change touches, linked or not. Its author knows what
the change settles and makes it once. Two tasks can still contradict each other without a file
conflict (WAY-01); the change accepts that risk, since the review, which reads every entry the
change alters, and the human, who sees in its request each entry not accepted with the task
document (WAY-114), read it against the foundation.
*Rejected:* marks on links flagged by a change — they see only written links, and renewing a mark
does not lead to a change in the entry that carries it; a search within overlapping scopes —
contradictions between parts go unseen; a search of linked entries only — entries written apart go
unseen; a second search against the main branch before the merge, with the record of both — it
repeats the first search, and a record shows that a search ran, not what it missed.

### WAY-35 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the
element's entries stands in the element's template, or once in the part the elements share
(WAY-09) where it is common to them; the way of working the skills share stands once in that part,
and a skill reads the rules and that way of working from there instead of restating them. No
template and no skill of an element carries a note that a rule waits for a decision.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: skill-rule-source · elements-pending-marker.
  For what the skill holds, an agent compares the change with the decision:
  - complies: a fix to a field's form in the skill's output goes into the template, not the
    skill; the skill orders its steps and says what to ask;
  - violates: the skill says a rationale has at most three sentences while the template does not;
    the skill restates the list of fields.
- **Origin:** none

*Rationale:* an entry written by hand or by another agent meets only the template and the shared
part, so the rules stand where every writer and every check reaches them; steps and questions are
no rule of an entry. A note in a template or a skill that a rule waits for a decision reads as a
rule that does not bind yet, and it stays when the decision comes, since nothing leads from the
decision to the note (WAY-33); a writer who meets it takes a settled rule for an open one.
*Rejected:* rules restated in the skill next to the template — two copies that drift, and the
template and the skill hold entries to different rules; each rule citing the decision that sets
it — the rules are the-way's own text, changed and reviewed like any other change to it; the
decision left without a sentence on the note that a rule waits — the reason for the invariant that
keeps such notes out lives in the description of one request alone, and whoever goes from the
invariant to the decision finds no reason.

### WAY-113 — How does an agent of the-way ask a human decision?

An agent asks in plain conversation text, with no separate question panel: a question of
assessment stays open, and a decision question gives the available ways, the cost of each, a
recommendation and the weak point of the way recommended. The cost of a way includes the cost of
undoing it later, written as one word where it is nil; the weak point is the strongest argument
against the way recommended, anchored in the material where the material gives one, and for a
shortcut, where another way would be right were cost no matter, it names that way and says why it
is not recommended. After a human choice enters an entry's binding part, the agent asks one
question against that choice anchored in the human's words or supplied material, unless the choice
ends with the work, or the human took one of the ways offered and the decision question named,
anchored in the material, the weak point of that way.

While a project definition or a task document is refined, the technology step included, that
question is asked only where the choice contradicts a sentence the human said earlier, which the
question quotes, and that holds as well for the entries written during that refinement; in a task's
cycle and where an entry is written outside such a refinement it is asked as above, the looser rule
holding only before the cycle starts (WAY-315). In the whole refinement of a project definition, its
rounds and its step of projected foundation changes, a question may also follow an answer where it
takes the move of implication, "you wrote X; from X follows Y — does Y hold?", anchored in a
sentence of the human, or asks the reason of a decision that is costly to reverse, where neither
the human's words nor the material give it; the refinement of a task keeps the rule above.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level, task-cycle, foundation-review, process-audit, product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the exchange with the decision:
  - complies: a choice is presented in text with the cost of each way, the cost of undoing it in
    one word where it is nil, a recommendation and the weak point of the way recommended, which for
    a shortcut names the right way and why it is not recommended, followed by a source-anchored
    question against the answer when it enters a binding entry, unless the person took the way
    recommended as offered and the question named its weak point, anchored in the material; in the
    refinement of a task or a project definition, the entries written during it included, an answer
    that changes a decision, or that follows a loose remark, is written as given, while an answer
    that contradicts a sentence the person said earlier gets one question quoting that sentence; in
    the rounds of a project definition an answer from which a consequence follows draws one
    question that quotes the person's sentence and asks whether the consequence holds, and a
    decision that is costly to reverse, whose reason neither the person's words nor the material
    give, draws one question asking the reason;
  - violates: the choice appears only in a separate option panel, a decision question recommends a
    way and names no weak point of it, or names for a shortcut a weak point that leaves out the right
    way; an agent asks a generic challenge unrelated to the person's answer, or an agent asks against
    a way offered whose weak point the question already named, anchored in the material, and the
    person took as offered; in the refinement of a task or a project definition, an agent asks
    against an answer, for an entry written during it too, because it changes a decision or follows a
    loose remark, with no earlier sentence of the person that the answer contradicts; in the
    refinement of a task, an agent asks a question of implication or of the reason of a decision
    after an answer.
- **Origin:** none

*Rationale:* the person sees the trade-off where they make the choice. The weak point puts the
strongest argument against a recommendation before a person who may not be able to form that
argument as well as the agent can, so that the recommendation is weighed and not only accepted; one
anchored in the material also tells the person what was already weighed, which is why a way taken
as offered needs no question after it. The cost of undoing a way is part of its cost, and one word
where it is nil keeps the question short while naming the choice that cannot be taken back cheaply,
which would otherwise pass unnamed. The-way takes from a practice of the Mega.DEV course, whose
recording of the first episode of its third season a reader of this repository cannot open, the cost
of undoing for each way and the naming of the right way in the weak point of a shortcut; the
practice there gives the variants with their effort and whether each can be cheaply undone, then a
recommendation, then which variant would be right were cost no matter and why it is not
recommended, and it shows when an agent picks a shortcut, which is a cheap sign of debt (WAY-100).
The price is a longer question, and a weak point the agent finds weak lets a doubtful
recommendation pass. A challenge grounded in the person's own material can expose a contradiction
without inventing one. Where the question already named the weak point of a way and the person took
that way as offered, a challenge asks again what was weighed at the choice; it is kept for an
answer in the person's own words, which the question did not weigh. While a document is refined an
answer is no commitment yet, since the person reads the whole document at its acceptance and
anything in it may change, so a question after every answer, or after a loose remark, spends
attention on what that reading covers; only a contradiction with the person's own earlier sentence
is both real and quotable, and only the person can resolve it. Where an entry is written outside
such a refinement or a cycle runs, the answer is about to bind, so the question stays; the entries
written during a refinement, such as the projected entries of a definition, wait for the person's
acceptance of the whole document or at the gate, so they follow the rule of the refinement. The
price at refinement: an answer that contradicts the material, such as a product description or a
note, and no sentence of the person, passes with no question. A project definition takes more than
a task document, since it settles scope, success and risks, where a counter-argument after the
answer is worth more than the further question it costs, and the move of implication is the only
move that follows an answer; the price is more questions after answers, longer rounds, and no
evidence that the move ever caught anything.
*Rejected:* a panel of options separate from the conversation — its context is detached from the
material; a challenge to every choice, including one that ends with the work — repeated questions
would add no later protection; a challenge to every choice entering a binding entry, even a way
taken as offered whose weak point the question named — it asks again what the choice already
weighed; at refinement no question at all — a contradiction with the person's own earlier sentence
passes unnoticed too; at refinement no question only where the answer changes a decision, otherwise
as before — a loose remark still draws a question; a weak point for every way, not only the one
recommended — the questions grow clearly longer, and much of it repeats the cost of each way; the
counter-argument beside the recommendation and the question after the choice always, with no
exception — the person hears the same doubt twice, before the choice and after it; the practice of
the right fix beside the recommended one in the whole form of the course, a paragraph of its own with
the effort and the reversibility of every variant — a third thing beside the cost and the weak
point, partly repeating them, and clearly longer questions; the right fix named in the weak point
with no cost of undoing — the person may choose a way that cannot be undone cheaply without knowing
it; nothing of that practice — a plain "I recommend the patch, though a rebuild would be right"
depends on whether the agent happens to pick it as the strongest argument; for a project
definition, fitting the instructions to the rule above, so that the move of implication drops out
and the reason of a costly decision stays an ordinary question for a missing fact — a few sentences
in one file and nothing to undo, but a consequence the person did not notice shows only when the
whole definition is read, or never; leaving the instructions as they were, with the rule above for
a definition unchanged — nothing to undo today, but the contradiction stays, one place asks a
question the rule forbids and another does not; the two moves for the step of projected foundation
changes alone — nothing to undo beyond the rule itself, but the answers on scope, success and risks
fall in the rounds, where no counter-argument would follow an answer; the two moves for the whole
refinement of a definition with the rounds left as they were — nothing to undo today, but the
decision would allow what no instruction asks for, and an agent of the rounds that asked such a
question would comply with the decision though its own instructions foresee none.

### WAY-120 — How does the-way critique an agent's proposal?

An agent may invoke critique for any proposal without waiting for the human to express doubt; a
completed set for collective human review goes through it, and the diff of a change to an
invariant test or to the foundation does not (WAY-10). An independent critique gives one fresh
agent the full proposal or set, its sources and applicable rules without the author's defense; the
author checks each observation and gives one explicit verdict. For a collectively reviewed set the
critic checks form, fidelity to source and contradictions across entries before presentation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level, product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the review with the decision:
  - complies: one fresh critic receives a finished set and its sources, reports evidence for each
    concern, and the author verifies it before presenting corrected proposals and open questions;
  - violates: one critic is run per row of a set, the author silently changes a human settlement,
    two critics are run on one set, or the merge of a change to the foundation waits for a
    critique of its diff.
- **Origin:** none

*Rationale:* the author is attached to its own fluent proposal, and an independent reading can
find a mismatch with its source or another entry before the human spends attention on the set.
The author's verdict keeps the critic an aid rather than a second decision-maker.
*Rejected:* a fresh critic for every entry accepted with the human — it repeats the human's
review; letting the critic's remarks edit human settlements without asking — it would disguise a
new decision as a correction.

### WAY-150 — How do the-way skills choose which product foundation material to read?

The-way skills read a product's foundation selectively: whoever selects names the parts the work
touches from the files it changes through the part map's rules for assigning files, or, where the
work names no file yet, from the responsibilities it changes; finds by a touched part's identifier
the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds
the invariants a test the work alters cites, the decisions whose sentence such a test holds by a
line `decision:`, the decisions the task's *Decisions in play* or the work's source names, the
touched parts' entries of the map and the entries these link to as far as the work needs. Of the
decisions it finds by *Scope*, by a line `decision:` or as the task or the work's source names
them, whoever selects reads the index and opens whole only the decisions the work changes, goes
against or proposes another answer to — that one with its rejected options — those the task or the
work's source names, those whose sentence a test the work alters holds by a line `decision:` and
those whose binding sentences leave open what the work has to do; each other entry it selects — an
invariant, an entry of the map of a touched part, or an entry, a decision included, that these or
the decisions of the index link to as far as the work needs — it reads whole, and it reads more
entries where relevance is uncertain and a whole file only where it is short; the reviewer of the
whole change reads the index of its whole selection and states in its report how many decisions it
read whole. The selection is neither recorded nor compared with every *Scope* of the log, and the
search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep
their domain.

The index of a selection of decisions is no file of the repository: a script of the-way writes it
on demand into a file the agent names, and it gives for each selected decision its number, its
question, its binding sentences and its *Scope*.

In a decision log divided into topical sections, whoever selects picks from the list of sections,
by each one's heading and sentence, the sections of the work's topics, whose decisions take the
place of those found by *Scope* in the selection whose index it reads, and it runs through the
questions alone of the decisions outside those sections whose *Scope* names a touched part and opens
whole each whose question points to a bearing on the work. In a log without topical sections the
decisions are selected by the parts the work touches, and their index takes the place of reading
each of them whole, the decisions the first paragraph names being opened whole as it gives.

Outside the task cycle the agent doing the work selects its own reading, while in the task cycle
the orchestrator selects for its own judgments and for each handoff, which names the foundation
entries by identifier; the reviewer of the whole change selects for its own review, and an agent
writing a foundation entry through an element's skill for the entry it writes; and every other agent
of the cycle reads what its handoff names and reaches for what is missing selectively — a search for
an identifier or a word and a read of the passage found, never of a whole file of the foundation —
naming each such reach in its report.

- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts,
  project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-21 · derives from WAY-33 · derives from WAY-148
- **Verification:** an agent compares the reading with the work and current foundation:
  - complies: a change to a file of `gate` in a log without sections has the index written of the
    decisions whose *Scope* names `gate` and of those the task names, reads it, opens whole the
    decisions the task names, the one the change rewords, the one whose sentence a test it alters
    holds by a line `decision:` and the one whose sentence leaves open which exit code the change
    gives, and reads whole the invariants naming `gate` or `every` and the entries they link to; a
    project with no file yet names its parts from the responsibilities it changes; the search of
    the whole foundation finds a conflict outside those parts and the reading widens; in a log with
    topical sections an author picks the two sections of its work's topics from the list of
    sections, reads the index of their decisions, runs through the questions of the decisions
    outside them whose *Scope* names a touched part and opens whole the one whose question points
    to a bearing on the work; in a task cycle the executor of a slice reads the entries its handoff
    names, searches for a decision it finds missing by its identifier and names that reach in its
    report, while the reviewer of the whole change selects its own reading, reads the index of its
    whole selection, opens whole the decisions this method names and reports "151 in the index, 40
    read whole";
  - violates: only decisions already named by the task are read; a search hit replaces its whole
    entry; a template is reduced to selected excerpts; the work records its selection and compares
    it with every *Scope* of the log; the whole decision log is read to find the decisions of a few
    parts; an invariant a test the change alters cites, or a decision whose sentence such a test
    holds by a line `decision:`, is left out because its *Part* or *Scope* names another part; an
    author rewords a decision knowing it only from its line of the index, its rejected options
    unread; an index of the log's decisions is kept as a file of the repository; in a log with
    topical sections the decisions outside the work's sections whose *Scope* names a touched part
    are left unseen; an executor of a slice or a reviewer of a slice selects its own foundation
    reading, or reaches beyond its handoff without naming the reach in its report; the reviewer of
    the whole change leaves decisions of its selection out of the index it reads, or leaves out of
    its report how many decisions it read whole; an agent that reads what its handoff names knows a
    decision its handoff names only from its line of an index.
- **Origin:** none

*Rationale:* a growing foundation contains more material than each piece of work needs, while
unconditional loading spends attention on unrelated rules. The parts a change's files belong to find
the decisions that govern it (WAY-21), the task names those it settles, a test the work alters leads
to the decisions whose sentences it holds as it leads to the invariants it cites, and links lead to
the rest, so the governing material stays visible; what no link joins, the author's search of the
whole foundation finds (WAY-33). The selection by *Scope* runs to more decisions than an agent can
read whole, and of each entry only its binding sentences say what binds, while its fields, its
reasoning and its rejected options serve whoever changes the decision, goes against it or needs to
know what it leaves open. An index that gives the binding sentences of every selected decision lets
an agent know all of them, which a run through titles, giving each question alone, does not, while a
whole reading of all of them cannot be done; opening whole the decisions the work changes,
contradicts, answers otherwise or finds open puts their reasoning and rejected options before the
agent exactly where it may go against them, and a decision a test the work alters holds is one the
work may break. The index is written on demand from the log, so it holds exactly the selection,
cannot go stale, needs nothing to keep it in step or to merge between branches that add decisions,
and leaves the log the one account of what binds (WAY-18). Topical sections let an agent take the
decisions of its work's topics, where the parts of a product each name a large share of its log; the
questions of the decisions outside those sections that govern a touched part keep the safeguard of
*Scope* (WAY-21) for the cost of their headings. In a task cycle the orchestrator reads the
foundation of the task's parts to coordinate it anyway; selecting once for the handoffs spares each
agent a selection of its own, which every agent of the cycle would otherwise pay for again. An agent
writing a foundation entry searches the whole foundation for it anyway (WAY-33), so it keeps the
selection its element's skill gives. A reach named in the report shows where the selection fell
short, and the reviewer of the whole change, selecting for itself and reading the index of all it
selects, finds a governing rule the orchestrator missed before the request; its count of decisions
read whole shows the human and the orchestrator how much of the index it followed into the entries.
The price is the round of fix the reading can still need: a reviewer of the whole change may name
decisions of its index as bearing on the change and leave them unopened, and only a round of fix in
which a fresh reviewer reads them closes that gap.
*Rejected:* unconditional whole-foundation loading — its context cost grows with unrelated work;
selection only from known links or keywords — a governing decision can remain unseen; a fixed
reading limit — a difficult case loses needed context; a separate maintained index, kept as a file
of the repository and refreshed after each change of the log — a second account can drift without
resolving semantic relevance, every change of a decision has to remember to refresh it, two branches
that add decisions collide in it as well, and in a product a stale index would need a check to
report it and the file would have to be created at installation; the rule of whole reading kept,
with the reviewer of the whole change running through the rest of its selection by title — the
whole reading is broken in every cycle, the reviewer knows most of the decisions by title alone,
and the share grows with every task; the log split into two files, the binding sentences in one and
the reasoning in the other under the same numbers — set aside, to be weighed if the index does not
suffice, at the cost of changing every entry once, together with the check and the skills that read
entries; in a log with topical sections, the sections of the work's topics alone — the cheapest,
but a decision of another topic that governs a touched part is lost without a trace; the sections
of the work's topics for every agent but the reviewer of the whole change, which reads the index of
its whole selection by parts — the reviewer gains nothing from the division; a record of the
selection compared with every *Scope* of the log — it costs every piece of work and records reading,
not understanding; each agent of a task cycle selecting for itself — every agent pays for the same
reading again; the orchestrator's selection with no reach left to the agent — a missing entry is
guessed at instead of read; the reviewer of the whole change reading only the orchestrator's
selection — a gap in the selection would reach the request unchecked.

## Invariants

How an invariant is written, checked by a test or by review, given a result, marked violated and
changed together with its test.

### WAY-03 — Who may change an invariant test, and when?

Any change may alter an invariant test, in any step of its task, implementation included. A change
that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`,
names that test in its request, so that the agent reviewing the change and the human merging it see
it.

The check of the foundation lists an invariant whose method is `test`, whose sentence a change has
reworded and which a file cites by a line `invariant:`, when no file that cites it has changed
since the commit the branch left the main branch from. A change whose check lists such an invariant
names it in its request in plain words, giving what its sentence now says and that the test that
checks it was left as it was. The listing stops no change.

- **Scope:** invariants, task-cycle, agent-instructions
- **Based on:** impossiblebench-test-modification
- **Relations:** derives from WAY-01
- **Verification:** tests: which invariants the check lists for a reworded sentence, and that the
  listing stops no change. An agent compares a change with the part no test holds:
  - complies: an implementer whose code an invariant test stops fixes the code, or, where the test
    reads its sentence wrongly, fixes the test and names it in the request; a change that adds,
    drops or alters a test that holds a sentence of a decision by a line `decision:`, or alters its
    line, names that test in its request; a change that corrects the sentence of an invariant and
    leaves its test as it was names the invariant in its request, saying what the sentence now says;
  - violates: a change alters an invariant test and its request does not name it; a test that read
    its sentence rightly is weakened so that the code passes, even where the request names it; a
    task goes back to an earlier step of its cycle only because an invariant test has to change; a
    change weakens a test that holds a sentence of a decision by a line `decision:`, or drops its
    line, and its request is silent; the check lists an invariant for a corrected sentence and the
    request does not name it.
- **Origin:** none

*Rationale:* an agent that a test stands in the way of adjusts the test to the code: the build
turns green, and the foundation lies. Naming every change to an invariant test in the request puts
that move in front of the reviewer, who did not make the change, and of the human at the merge
(WAY-10), while a test that reads its sentence wrongly is fixed where it is found. Naming is
enough where a block is not, because a changed test is read against the sentence it cites by
someone who did not change it, before the change merges. A test that holds a sentence of a decision
checks that sentence as an invariant test checks its own, so it is named and read in the same way.
A sentence corrected while its test stays is the one change that leaves the test out of the
change's diff, so nothing in the diff names it and only the listing brings it before the reviewer
and the human; it is listed and not stopped, since a sentence reworded in words alone changes no
meaning and the listing can be wrong.
*Rejected:* invariant tests read-only during implementation, kept so by a check at the merge, with
a return to the foundation step for every change of one — each needed fix of a test stops the task;
a local hook — one switch skips it; a written rule "do not change the tests" — prose stops nothing.

### WAY-08 — How is an invariant checked?

Every invariant names its method of checking: a test of the product's test suite where a cheap test
can check its sentence, and review otherwise, where the review of each change by an agent that did
not make it compares the change with the sentence. The status of an invariant with a test comes
from running that test, never from a status written by hand. An invariant's test is seen failing
once, with the command that later shows it passing — run before the code that satisfies it, or,
where the code already has the behaviour, against that behaviour broken for a moment.

- **Scope:** invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the invariant on the log's fields reads `test`, and its test runs the check on the
    real log; whether an image's text alternative describes it reads `review`; a new invariant's
    test fails before the code that satisfies it is written;
  - violates: an invariant that a cheap test can check reads `review`; an entry carries a status
    `pass` written by hand; an invariant's test is taken as checking its rule without having been
    seen failing.
- **Origin:** none

*Rationale:* coverage is not checking: code can be covered while no test fails when it is removed,
so a test counts once it has been seen failing; a status written by hand goes stale with the next
commit. A check built for a rule no cheap test can decide costs more than it catches, while the
review already reads each change against the foundation (WAY-10).
*Rejected:* test coverage for every invariant — untestable ones leave the foundation or get a test
that always passes; a deliberate break of every test, written apart from it and run k of n times —
a ritual of its own for each test, where the one failure seen already shows it can fail; human
inspection with a recorded verdict — a file of verdicts beside the review that reads the change.

### WAY-51 — What does the main branch hold where the product does not meet an invariant?

On the main branch an invariant the product does not meet today stays whole and is marked violated
at its entry; an invariant is marked violated only by a change of the foundation that a human
accepts, never by a step of implementation. A change that sets or clears the mark names it in its
request; the test of a marked invariant stands in the product's suite marked as an expected failure
in the product's test tool, and the change in which it starts to pass removes that marking and the
mark of the invariant. While an invariant is marked violated, no second invariant compares the
product with its state on `{fork-point}`, and the review of each change to the files of the parts
the invariant names keeps a cleaned file or a new one from breaking it again until the mark is
cleared.

- **Scope:** invariants, gate, task-cycle, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-63 · derives from WAY-225
- **Verification:** an agent compares the change with the decision:
  - complies: an invariant on loading saves that the product breaks today reads `Violated: yes`,
    its test is marked as an expected failure, and the request that sets the mark names it;
  - violates: an implementer marks an invariant violated so that the task can end; a request sets
    or clears the mark without naming it; a marked invariant's test passes while the mark and the
    expected failure stay; an invariant the product does not meet is reworded to fit the code;
    beside a marked invariant stands a second one that no file holds more breaks than on the fork
    point; a test lists the files already cleaned and grows the list.
- **Origin:** none

*Rationale:* the process enters products that already break their rules (WAY-28); the mark keeps
each rule whole, since a rule written to fit the code hides the intent, and makes the gap countable.
Where marking a rule violated is the easy move, agents take it, so only a change a human accepts
sets the mark. The mark stands at the invariant, where every reader of it sees it. Until the last
file is clean, the marked invariant's test cannot see a break come back into a file already
cleaned; the review, which reads every change anyway, sees it there, so a cleaned file stays clean
only as surely as the reviewer reads it.
*Rejected:* a main branch holding only what the code meets — no existing product could enter; the
rule weakened until the code fits it — the foundation describes the accident (WAY-225); a derived
list of violated invariants beside the invariants file — a second file to keep in step with the
entries, which a reader of the invariant does not see; a derived list of the dependencies of a part
that the code holds against the part map — the same second file, and a dependency of a part that the
map does not allow is an invariant like any other (WAY-225); a rule left out or marked "not checked yet" until met — the gap
stops being countable; debt paid by an end date — repaid by weakening the rule; beside the marked
invariant, a second one holding from its first day that no file holds more breaks than on
`{fork-point}` and a file not there holds none — an entry kept only for the time of the cleaning,
whose withdrawal nothing checks, and a renamed file looks new to it; a test over a growing list of
cleaned files — the list decides the invariant and changes with no change of the foundation; every
file a change touches cleaned in full — a small change to a large file grows into cleaning it
whole.

### WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation
change a human decides, or where a decision in the product's log or the pinned the-way places it.
An invariant whose condition stands outside its sentence names by identifier the entry or the
decision that holds the condition, in a field where the template gives one and otherwise in its
sentence. An identifier of a decision written into the sentence because that decision holds the
condition is a part of the condition, not a link that WAY-17 requires; where such a link is due, it
stands beside the sentence, in its own field.

An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}`
(WAY-61), while a state it compares may be the one on `{merge-onto}`, and states what is to hold on
the main branch alone as holding where `{merge-onto}` exists. A sentence bounding or equating a
quantity measured while the product runs names its bound or tolerance, statistic and population.

- **Scope:** invariants, decisions, part-map, gate
- **Based on:** none
- **Relations:** derives from WAY-22
- **Verification:** an agent compares the change with the decision:
  - complies: "every entry of the log has every field of the template"; an invariant whose
    condition a decision of the pinned the-way holds names that decision's number in its sentence,
    its template giving no field for it; an invariant of the-way whose sentence reads "as WAY-309
    names them", the condition standing in that decision of its own log, has WAY-309 also in its
    *Derives from*, the link WAY-17 requires;
  - violates: "every request is answered within the limit set in `config.py`"; an invariant whose
    condition stands in a decision and which names that decision nowhere; "every fingerprint
    on `main` equals the current fingerprint of the decision it names"; "a commit that changes
    `template.md` also appends a decision version to the log"; a bound written "~2 seconds"; a
    sentence measuring a change against `{merge-onto}`; an invariant whose entry has the link WAY-17
    requires only as the identifier in its sentence, with no field of its own for it.
- **Origin:** none

*Rationale:* a condition outside the sentence moves while the sentence stays, so it stands only
where moving it takes a decision, and the invariant names that place so that whoever changes it finds
the invariant; a branch names another commit by the hour; a change is measured from the fork point,
where the work on it began; a measured bound needs its statistic and population. An identifier
in the sentence says where the condition lies, as a number in a quoted sentence does, and the links
of an entry stand beside its sentence in their own fields (WAY-17); the two are different things
even where one decision stands in both places, so a reader who finds the same number in the sentence
and in *Derives from* finds no collision.
*Rejected:* every condition in the sentence — two answers where a measure meets a definition or a
method; a closed list of places — it leaves out places a log uses; every place outside the
foundation forbidden — WAY-38 and WAY-53 place conditions in the product; an invariant kept aside
until its condition has a home — nothing counts it (WAY-51); a commit's parent as the base — a task
spreads one change over several commits; the template's own text left as it stood, without the
naming in the decision — the set of links WAY-17 gives stops being complete, and the case of a
decision of the pinned the-way stays impossible to write; the obligation to name the place removed
— invariants that go quietly stale when the decision holding their condition changes; the clause
resting on a decision outside the product's log not being an entry of it — it does not cover an
invariant of the-way whose decisions stand in its own log; the clause in the rule of the withdrawn
decision on how much an invariant entry holds — it narrows an approved decision's reach; no clause —
a reader who meets the rule of the template first may reject the correct form, and the round of
correction falls on the task of another change.

### WAY-61 — How is an invariant's method of checking written?

An invariant's method of checking reads `test` once a test of the product's test suite, written in
the product's language and run by the command that runs the product's tests, cites it, and `review`
until then, and it names no command and no script. The method is held on the finished change: an
invariant whose test a later slice of the same change writes may read `test` from its writing on. A
test checks what its invariant's sentence is about, as it stands on the commit being checked, so a
test fed input made up for it is the method of a sentence about the check it exercises, never of one
about the data that check reads.

- **Scope:** invariants, gate, decisions, part-map, elements-common, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-08 · derives from WAY-16 ·
  derives from WAY-54 · derives from WAY-07 · derives from WAY-38 ·
  derives from WAY-60
- **Verification:** invariants: test-method-citation. For the rest, an agent compares the change
  with the decision:
  - complies: a sentence about the instruction files of the repository is kept by a test running
    its check on those files; a sentence about the loader is kept by a test handing it a save of
    another version; a sentence on whether an image's text alternative describes it reads `review`;
    an invariant written by one slice of a change, whose test a later slice of the same change
    writes, reads `test` from its writing on; an invariant that no test of the finished change
    cites reads `review`;
  - violates: a sentence about the real instruction files names as its test the check's own test,
    which feeds it made-up files; an invariant's test is a script beside the product's suite, which
    the command running the product's tests does not run; an invariant reads `test` on the finished
    change while no test cites it; an entry names `python -B tools/check_saves.py` as its method.
- **Origin:** none

*Rationale:* the command that runs the product's tests already runs on every change, so an
invariant's test runs with them, in the product's language; one run serves many invariants, each
needing an outcome of its own; a check that sees nothing passes quietly (WAY-38). A change is
judged as a whole, once finished, so an invariant written before its test within one change may read
`test` from its writing, and a later slice that writes the test leaves the entry as it is. An
invariant that no test of the finished change cites has the review to keep it, and its method says
so. The price taken: between the writing of the entry and the slice that writes its test, the task's
branch, a blocked draft request included, says `test` while no test cites it; the branch reaches the
main branch only with the test, which the check in WAY-321 enforces.
*Rejected:* a command per invariant that a gate of its own runs, recording a verdict for each entry
— a second runner beside the product's tests; `TODO` as the method until the test exists — it
names nothing that keeps the rule meanwhile; a sentence in the text of the planning skill saying
that an entry reads `review` and the slice that writes its test turns it to `test` — a fourth place
for the same rule, which agents knew and passed over on purpose, and several independent slices
would change the one file of invariants, which the plan's rule that two slices change the same file
only where one depends on the other forbids; a kind named beside the method — a second value that
can disagree (WAY-54); the run's exit code as each invariant's result — one broken rule fails all, a
skipped one passes; a check's tests on made-up input as the method of a sentence about real data —
they show the check works, not that the data holds.

### WAY-62 — What does an invariant entry name in the part map?

An invariant entry names the parts of the part map where a change can make its sentence false, or
`every` where a change to any part can. A change, against the commit its branch left the main branch
from, reaches an invariant that names `every` or a part the change touches, or that a test the
change alters cites, whatever parts a file collecting entries gives that change (WAY-44), and the
agent making the change reads every invariant it reaches. The entry names no critical flow or
surface.

- **Scope:** invariants, part-map, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-16 · derives from WAY-44 ·
  derives from WAY-61
- **Verification:** an agent compares the change with the decision:
  - complies: the invariant on the log's fields names `decisions`, and a change to a test citing it
    under `gate/` reaches it too; "every file git tracks matches the patterns of exactly one part"
    names `every`;
  - violates: that sentence names `part-map`, so a file added under `gate/` never reaches it; an
    entry names the flow it protects.
- **Origin:** none

*Rationale:* invariants need what scope gives decisions (WAY-21): parts, not paths, which would
copy the map. A test may lie in another part than what it checks, so a change to it reaches the
invariant too. A missing part leaves the invariant unread by a change that can make it false,
and fails silently; an extra one costs a reading, so doubt names more.
*Rejected:* parts computed from what the test reads — a test names its own file, not what it
reaches; the invariant naming its failure mode, flow or surface — one link written at both
ends; the part holding the check — a file added elsewhere never reaches it.

### WAY-69 — Who writes an invariant's sentence, its test and the code the test covers?

An invariant's sentence, its test and the code the test covers may come from one agent; the agent
reviewing the change, which made none of it, reads the test against the sentence.

- **Scope:** invariants, gate, task-cycle
- **Based on:** visible-scoring-reward-hacking · oracle-in-loop-building
- **Relations:** derives from WAY-08
- **Verification:** an agent compares the change with the decision:
  - complies: the author of a change writes an invariant's sentence, its test and the code, sees
    the test fail first, and an agent that made none of it reviews the change;
  - violates: a cycle pauses the author while two other agents write an invariant's sentence and
    its test.
- **Origin:** none

*Rationale:* a test fitted to the code by the agent that wrote both meets the reviewer, which reads
it against the sentence without having written either (WAY-10), so the writing needs no agents of
its own.
*Rejected:* three different agents for the sentence, the test and the code, with the deliberate
break written by the reviewer — a pause and two agents for each invariant, for what the review
already reads; hiding tests from the executor — it costs honest work.

### WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?

`elements/common/foundation_check.py` reports an invariant whose method reads `test` and which no
line `invariant: <identifier>` in a file git tracks whose name does not end in `.md` cites, in every
run but the one made right after an entry is written, which passes the switch
`--skip-test-citations` and so skips this report and no other. The one command that runs a product's
tests runs the script without that switch (WAY-16).

- **Scope:** elements-common, invariants, gate, installation
- **Based on:** none
- **Relations:** derives from WAY-61 · derives from WAY-63 · derives from WAY-16
- **Verification:** invariants: test-method-citation. For the switch, an agent compares the change
  with the decision:
  - complies: the run right after an invariant that reads `test` is written, whose test a later
    slice of the same change writes, passes the switch and reports nothing; the product's one
    command of tests runs the script with no switch and reports that invariant while no test
    cites it;
  - violates: the product's one command of tests runs the script with the switch; a skill has the
    run after writing an entry leave the switch out; the report stands in a mode of the script
    that a product has to add to its own command, or in a second script.
- **Origin:** none

*Rationale:* the one command that runs a product's tests is the run every change meets before it
is merged (WAY-16), so a report that stands in it needs no line added to the command of any
product, and a test forgotten after the entry was written shows as an error, where an invariant
that no test cites would otherwise get no result and say nothing (WAY-63). The run right after an
entry is written is the one run in which the test of a later slice does not exist yet, so it alone
is the exception. The price taken: one switch to remember when an entry is written; an agent that
forgets it sees an error and may turn the method back to `review`, which is the safe direction.
*Rejected:* a separate mode of the script that a product adds to its own command of tests — the
installer and its tests change, and the command is changed by hand in each product and in every
later one; a product that does not add it has no check and nothing says so; a step of the task
cycle in which the orchestrator checks the entries before the request opens — a change made outside
a cycle stays unchecked, the cycle gets one more step, and the rule lives in the text of a skill,
which agents can knowingly pass over; no check, only the change of WAY-61 — it costs nothing today,
but a forgotten test leaves a false `test` in the foundation with no signal.

## Environment facts

Which sources and settings become environment facts, how a fact is written and named, and how it
keeps up with its source.

### WAY-73 — Which entries name an environment fact, and when does a fact leave the foundation?

An invariant's *Rests on* names every environment fact holding a condition that decides whether a
commit makes its sentence true, and no other fact. A fact holds such a condition when, read
otherwise, it would change whether some commit makes the sentence true, or change a value the
sentence copies from it. A fact that is only a reason for a decision the invariant derives
from stands in that decision's *Based on* alone; a fact stands only while an invariant's *Rests on*
or a decision's *Based on* names it, and the change that removes the last such name withdraws it.

- **Scope:** invariants, decisions, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-17 · derives from WAY-60
- **Verification:** an agent compares the change with the decision:
  - complies: `script-imports` rests on `python-stdlib-modules`, not on a finding a decision it
    derives from quotes; a change that drops the last decision citing a fact withdraws the fact;
  - violates: an invariant rests on the report of a past failure its decision quotes; an invariant
    bounding a page's load time by an outside standard's threshold reads `Rests on: none`; a fact
    that nothing names stays among the entries.
- **Origin:** none

*Rationale:* a fact holding a condition changes whether the sentence holds with no commit, so
*Rests on* is its only path to the invariant; a mere reason reaches it through its decision. A
link is written at the dependent's end (WAY-17), so a fact nothing names is seen from
nowhere; the change that drops its last name names it, so its author's search of the foundation
finds it (WAY-33).
*Rejected:* every fact in the *Based on* of the decisions it derives from — flags invariants that
still hold, and misses conditions no decision quotes; the choice left to each author — "rest on"
reads two ways; unnamed facts left in the file — facts outlive their readers; a check reporting an
unnamed fact as a warning on the task branch and an error at the merge — the author's search
already finds it, in the change that leaves it unnamed.

### WAY-82 — How does an environment fact keep up with what its source says?

An environment fact names no method and no status, no test cites it, no check of it runs, on a
change or by a clock, and nothing fails when the world moves. A fact changes when someone finds
that its source no longer says what its sentence says, or that a newer edition the product stands
on says otherwise; the change that rewrites or withdraws it corrects every entry naming it (WAY-33).
An announced revision changes nothing until the new edition is out, and neither a fact nor a
decision citing it names a date or condition for its review (WAY-24).

- **Scope:** environment-facts, invariants, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-60
- **Verification:** an agent compares the change with the decision:
  - complies: a fact's entry holds its sentence and *Source* and nothing else; NIST's notice that it
    will revise FIPS 180-4 changes nothing;
  - violates: a fact names a command that tests the behaviour its sentence states or watches its
    source; a test cites a fact on a `fact:` line; a change touching no fact fails on a fact; a
    fact's sentence is rewritten while an invariant resting on it is left as it was; a decision
    names the date of an announced revision as the day to look at a fact again.
- **Origin:** none

*Rationale:* the world changes with no commit, so a check of it in the gate of an unrelated change
would give a verdict that follows the date (WAY-60). The passage with its address and the date read
lets whoever reads the fact see at once whether the source still says so, with nothing kept
running. A moved source is found by whoever reads the fact — the author of a change resting on it,
a task's return step, or the review of the foundation against the product (WAY-24) — and that
change then reaches what rests on the fact (WAY-33).
*Rejected:* a method for each fact — a command testing the behaviour or watching the source, run
on every change that enters or rewords the fact and by a clock on the main branch, or the path of
a file a person re-reads with a dated verdict — a program, a run and a record for every fact, whose
failures reach someone only when a person reads them; an announced revision written as a condition
in *Review when* of the decision citing the fact — a date in an entry asks for a look nobody is
sent to make (WAY-24).

### WAY-84 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can
open it, a host's access rule — is an environment fact, its source the place where that state is
shown, or, where no page open to a reader shows it, a reading. A choice of such a setting
is a decision only where the product declares it, and that decision rests on the fact. A fact about
the visibility of a repository the product links to names that one repository.

- **Scope:** environment-facts, decisions
- **Based on:** github-private-repository-response
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a host's access rule is a fact whose source is the page showing it; the protection of
    a branch, which no page open without the access of the product's people shows, is a fact whose
    source is a reading of it; no decision on this repository's visibility is written, as the
    repository declares none;
  - violates: one fact lists every repository this one links to; a decision "the repository is
    private" is written where the product declares no visibility; an anonymous 404 is taken to
    show that a repository is private; the source of a setting that only a signed-in page shows is
    the address of that page.
- **Origin:** none

*Rationale:* such a setting changes with a click and no commit, so it is a fact about the world, and
each repository changes on its own. A decision needs someone who chose; otherwise no commit could
check it. Where no page open to a reader shows the setting, the one reading its setter quotes is
what a reader with access compares with it.
*Rejected:* a field naming who sets the setting — nothing reads it; a decision and a fact for every
such setting — a decision where nobody chose; a reading of the setting that is repeated, on a change
or by a clock, or a dated re-read by the person who sets it — a run and a record for every setting,
as WAY-82 rejects for every fact, which the one reading quoted is not; for a setting that only a
signed-in page shows, a page without an edition and without an archived copy, giving its address,
what it showed and the date — nobody but its author can compare the source with the quotation, and
a passage word for word from a panel clicked by hand is easy to invent; no fact written for such a
setting until the product needs it — a standing `TODO` on the main branch of a product that has the
setting, and a form agents invent meanwhile.

### WAY-85 — How is a finding of a study written as an environment fact?

A finding of a study stands as an environment fact saying what the study found, its source citing
the version of the paper, and the models the study measured named as the study names them, in the
sentence or in a passage its source quotes. That the agents of this process behave the same is no
part of the fact. A decision citing a finding none of whose measured models comes from a publisher
whose models the process's agents run on says in its rationale that it takes the finding across
publishers.

- **Scope:** environment-facts, decisions
- **Based on:** anthropic-model-states · openai-model-states
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the finding behind WAY-03 is a fact whose source is arXiv:2510.20270v1, quoting the
    passage that names the three Claude models it measured; WAY-12, citing a finding on models of
    other publishers only, says it takes the finding across publishers;
  - violates: the fact says "Claude models change tests" with no version of the paper and no
    models; the fact says the finding applies to this process's agents.
- **Origin:** none

*Rationale:* what a paper measured on given models is true for good; that this process's agents
behave the same is a bet that ages as those models leave service, so it is no fact, and the names
of the measured models let a reader of the decision weigh it.
*Rejected:* the transfer as a field of the fact — a fact no longer true or false today; the transfer
as a condition in *Review when* of each decision citing the fact, which a script checks against the
publisher's table of models — a date in an entry asks for a look nobody is sent to make (WAY-24).

### WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

A decision's *Based on* quotes every source outside the product that the decision rests on with its
address, the place in it, the passage word for word and the date it was read; once the environment
facts element has entries, it names instead a fact entry, by its identifier alone, for every
citation that, once it stopped being true, would call the decision into question — a finding about
agents or models, the behaviour of a tool the process uses. A measurement that the product's own
people made — its author and its agents — and whose record a reader of this repository cannot open
is no such citation: its result stands in the decision's *Rationale*, or in its *Rejected* where it
weighs a way not chosen, with what was measured and under which conditions; that prose says that the
measurement is the product's own and that its record is not open to a reader of this repository;
and no environment fact entry is written for it.

- **Scope:** decisions, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-17
- **Verification:** an agent compares the change with the decision:
  - complies: the ImpossibleBench finding behind WAY-03 becomes a fact entry named in its *Based
    on* as `impossiblebench-test-modification`; a past failure a decision cites stays quoted with
    its source;
  - violates: a precedent of how Packwerk handles its todo files becomes a fact entry; a finding
    about models stays quoted after the element has entries.
  For how a citation gives its source, an agent compares the change with the decision:
  - complies: a paper's finding is quoted with the edition's address, the place and passage, and
    the date read;
  - violates: a finding is quoted with its authors and year alone.
  For a measurement the product's people made, an agent compares the change with the decision:
  - complies: a decision whose rationale gives the result of a count the author ran over its own
    cycles states what was counted and over which cycles, says that the count is the product's own
    and that its record is not open to a reader of this repository, and names no fact for it in
    *Based on*;
  - violates: the same figures stand in the rationale with no word that the count is the product's
    own, so that a reader cannot tell it from a citation left without its fact; a fact entry is
    written for the count, with a private note as its source; a measurement whose report stands at
    an address any reader can open is described as the product's own and named by no fact.
- **Origin:** none

*Rationale:* only a citation whose change would call the decision into question needs an entry,
from which the search of whoever changes the fact finds the decision (WAY-33); a precedent, a past
event or a finding about people with no lapse date leads to nothing. The address, the passage and
the date let a reader find what the decision rests on and see whether it still says so. A
measurement that the product's people made is their own work, no source outside the product, and a
fact entry needs a source a reader can open while no entry may point to a source a reader
cannot open (WAY-27); the result therefore stays in the decision with its conditions, as WAY-05 lets
a measurement stand, where a reader can weigh it. The sentence that the measurement is the product's
own is what tells a reader that the figure is a measurement of the product and no citation whose
fact is missing; without it each reviewer guesses which of the two is before them. A measurement
whose report a reader can open at an address is a citation like any other, and follows the first
sentence. The price: a measurement of the product's own agents leaves no fact for the search of
WAY-33 to find, so when the model it measured is replaced nothing flags the decision that rests on
it; a finding of others about agents or models still gets its fact, as WAY-17 asks.
*Rejected:* every citation as an entry — many entries whose change would call no decision into
question, each a second copy of its quote; a fact named with its fingerprint, renewed when the fact
changes — the author's search finds the decision without it (WAY-33); the partners of the part
map's external context as linked facts — a new link with no known consumer; for a measurement the
product's people made, a summary of it with its conditions kept as a file of this repository that a
fact would name at a fixed commit — a new form of source beside those an environment fact takes, a
new kind of file with a rule on what it may not carry, and a summary to write and clean for each
experiment, with the decisions that carry such figures rewritten and a fact written for each; the
figure with a note that it comes from the author's private notes in place of a source — it points a
reader to a source the reader cannot open, which WAY-27 rejects; the rule alone, with no sentence in
the decision that the measurement is the product's own — a reviewer would still guess whether a
figure with no source is a measurement of the product or a citation left without its fact; no rule —
each decision that rests on such a measurement meets the collision of this decision with WAY-27
again, and the verdict depends on which of the two a reviewer reads as prevailing.

## Glossary

Which words take a glossary entry, what an entry holds, and how a sentence and a product's own words
rely on a term.

### WAY-93 — Where do glossary entries stand, and what identifies one?

Glossary entries stand in one file, `foundations/glossary.md`, each under its term as the foundation
writes it in running text, which no other entry there holds. The file opens with a title and a
paragraph saying what it holds, and holds no other heading than its entries.

- **Scope:** glossary
- **Based on:** none
- **Relations:** narrows WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: the entry of "part map" is headed `## part map`, as the foundation writes the term;
  - violates: an entry is headed by an identifier of the concept apart from its word; a term heads
    two entries of the file.
- **Origin:** none

*Rationale:* a sentence depends on a term by its word (WAY-97), so the word as the text writes it
heads the entry, and one entry per term gives each word one meaning to read.
*Rejected:* terms in the shared space of identifiers — a word a part takes would stay
undefined; an identifier of the concept apart from its word — names no reader uses; a warning where
a term and an identifier of the part map, the invariants or the environment facts read alike, with
one side renamed where they name different things — a term and an identifier name things in
different places of a sentence, and a word with two meanings in the foundation is renamed as WAY-99
says; a list of withdrawn terms — git keeps the earlier entries.

### WAY-94 — What does a glossary entry hold, and what is its binding part?

A glossary entry holds one definition of its term and one field, *Not*: each meaning the word
carries or carried in the files git tracks, besides its definition and a meaning a reader who knows
the product's field gives it, with what carries it. The definition is the binding part.

- **Scope:** glossary
- **Based on:** none
- **Relations:** narrows WAY-02 · derives from WAY-04
- **Verification:** an agent compares the change with the decision:
  - complies: an invariant's sentence uses "slice" with no fingerprint, and the author of a
    changed definition of "slice" finds it by searching for the word;
  - violates: a sentence cites the term as `slice@<fingerprint>`; a changed *Not* is treated as a
    change to the entry's binding part.
- **Origin:** none

*Rationale:* a fingerprint at every use would flag, at each changed definition, every sentence using
a common term — flags people clear unread (WAY-02) — so the author of a changed definition searches
for the word instead (WAY-97).
*Rejected:* *Not* in the binding part — it changes mechanically and no dependant reads it; *Avoid*,
the other words for what the term names — a field kept for words nobody lists; a reader's meaning
in *Not* — the reader brings it along; a field of neighbouring words — the definitions carry the
difference; worked examples run as tests, an area of meaning, broader and narrower terms, an allowed
synonym, a list of uses, the code's name for a term — nothing reads them, or they are computed; a
field for a definition's source or the decision that set it — no entry needs one.

### WAY-95 — Which words take a glossary entry?

A word takes a glossary entry when it means, in the product, something other than a reader who knows
the product's field takes it to mean; a word the product uses more narrowly than the field takes an
entry only where a reader who takes the field's meaning would read a sentence of the product's
English files wrongly. An agent that meets such a word in its work — writing an entry, searching the
foundation, in a task's return step — writes its entry, no sweep of every binding sentence looks for
candidates, and a human accepts the meaning (WAY-114).

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "gate", used for the one command that runs all of a product's tests, takes an entry;
    "digest", used only as SHA-256 uses it, takes none; "run", used for running a command and for
    text running across lines, takes none; a game's "secondary action", used for an action under a
    form drawn as underlined text with no border, where the field reads a second, less prominent
    button, takes an entry because "the form holds no secondary action" reads differently in the
    two meanings; a game's "map", used for the map of a level, takes none where no sentence reads
    differently for the field's meaning;
  - violates: every noun of the decision log takes an entry; an agent reads every binding sentence
    of the foundation for candidates before it writes an entry; every narrower meaning of a word
    takes an entry whether or not a sentence reads differently for it.
- **Origin:** none

*Rationale:* a glossary of every relevant word grows without bound, kept by memory, while a word
used as the field uses it needs no entry. A word whose meaning is unclear shows where an agent works
with it. A meaning narrower than the field's moves what a sentence says only where a reader who
takes the field's meaning would read that sentence otherwise, and an entry for a narrower meaning no
sentence reads differently adds a word to keep for a reader no one misleads.
*Rejected:* every term relevant to the system — no bound; a word defined where it is used, when used
in one place — nearly nothing is; a script counting places — it cannot tell a definition from
another sentence; a sweep of every binding sentence for candidates with each entry written — a
ritual every change pays for; a word's definition moved out of every sentence that says what it is,
into the glossary — a rewrite of sentences the reader already understands; every term with a use
outside the glossary checked at the merge — a check of the glossary's bookkeeping, not of what a
word means; an entry for every narrower meaning — more certain, but the glossary grows by words no
one mistakes, the direction of the first rejected way; the rule left as it stands — whether a
narrower meaning is "something other than" the field's stays open, the dispute returns with the next
change and costs a blocking remark and a round of fixes.

### WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?

A sentence relies on a glossary term by using its word. A glossary entry is edited in place, its
meaning included, and the author of a change to a definition searches, in the same change, the
English text of every file git tracks for the word and rewrites each use whose meaning the new
definition moves; a text in another language is not searched (WAY-99).

- **Scope:** glossary, decisions, invariants, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** narrows WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: the definition of "slice" is reworded, its author searches the English text of every
    file git tracks for the word and its forms, and rewrites, in the same change, the two sentences
    whose meaning moves, and leaves a Polish guideline file that holds the Polish word alone;
  - violates: a definition is reworded and no uses are looked at; a use whose meaning moved is left
    for a later change; a Polish file is searched for the Polish word that stands for the term and
    its sentences are rewritten.
- **Origin:** none

*Rationale:* a sentence relies on a term by its word, so a search for the word finds the sentences
a changed meaning reaches, and the author who changed the meaning knows what moved. The review of
the change, by an agent that did not make it (WAY-10), sees the changed definition and the rewritten
sentences in one diff, and the human sees the changed meaning in the request (WAY-114). A text in
another language is left out of the search for the reason WAY-99 gives.
*Rejected:* a version as for invariants and facts — nothing reads it; a review of every use by
another agent, putting the new definition in place of the word — a second reading of what the
author has just searched; a term used on the main branch keeping its meaning, a new meaning taking
a new word — a word stays bound to a meaning the product no longer has; a sentence barred from
spelling out a term's definition — every sentence of every entry read against every definition, by
hand; a term whose definition holds a word an invariant's sentence may not hold named in
the request — the rule on that word stays with the invariant; impact analysis by a model alone —
nobody knows what it missed (WAY-02).

### WAY-99 — How does one word keep one meaning in the foundation?

Two uses of a word in the English text of the files git tracks carry two meanings when a sentence
those files hold is true in the meaning of one use and false in the meaning of the other, whichever
of the two the sentence uses, and a sentence made up for the test does not count; where one of the
two meanings is a meaning a reader who knows the product's field would not give the word, one of the
two is renamed, and the glossary entry of the word names in *Not* each such meaning it no longer
carries, with the term, identifier, closed-list value or quoted word — holding neither the term nor
its forms — that carries it now. A meaning whose word a human has not yet chosen reads `TODO` in
*Not*, which a task branch may hold and the main branch never does. A file of a product in another
language uses its words in the meaning they have in that language, and the rules of the glossary do
not reach it.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a game's "shard" carries a currency and a level's piece, and "the shard drops from a
    chest" is true of the currency and false of the piece, so the piece becomes "fragment" and *Not*
    of "shard" names it; a game's "map" is the map of a level in every sentence that holds it, no
    sentence is true of one use and false of another, so it keeps one meaning with no rename; the
    Polish guidelines of a game use "program" in its Polish sense and no rename follows;
  - violates: "shard (currency)" and "shard (piece)" stand side by side in the foundation; *Not* of
    "shard" names "level shard", a phrase holding the word itself; two meanings are found by a
    sentence written for the purpose that the files do not hold; a word of a Polish file is replaced
    because its English counterpart is a term of the glossary of the-way.
- **Origin:** none

*Rationale:* a sentence a test cites carries its words as they stand, so a word read in two meanings
makes it true and false at once. The same sentences decide whether a word has two meanings, so the
test needs no definition of each use written first and no judgment beyond the sentences the files
hold. A carrier holding the word itself would keep the homonym under a new label. The word is the
human's choice, accepted at the merge (WAY-114). The glossary and its terms are English, so a word
of a file in another language has no entry to be held against, and which word of that language
stands for which term would be the agent's judgment at every use, with no list and with the
inflection of the language.
*Rejected:* two meanings told apart by an area — the sentence carries no area; a note beside the
word — nobody citing the sentence reads it; renaming two meanings a reader of the field tells apart —
neither is the product's own; a *Not* that always names a word — the author would choose before the
human sees the case; a test of whether a definition true of one use is false of the other — a
definition of each use must be written before it can be applied, which opens a dispute over its
wording; the criterion left open — each agent invents its own; the rules covering files in another
language, held against the English glossary — the agent decides which word corresponds to which term,
and the judgment and the disputes return; one meaning per word inside a language, with no comparison
with the English glossary — no glossary of that language exists to record the meaning, and every
rename rests on the agent's judgment; the question left open — each cycle guesses.

### WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?

A word that the glossary of the-way holds at the commit a product pins, or the last word of a term
it holds, in any of its forms, takes a qualifier — a phrase holding the word — in a sentence of the
files of the product's `foundations/` that could otherwise be read in the other meaning: a sentence
that uses the word for the product's domain and could be read as the process's, or one that uses it
for the process and could be read as the domain's, and a bare use that no sentence of those files
reads in the other meaning keeps the meaning it has there. A qualified word takes a glossary entry
only where WAY-95 gives a word one, and where the bare word itself has an entry in the glossary of
the-way, that entry records no *Not* for its domain meaning. The product's code, its interface and
talk about the product use the word of the domain unchanged.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** narrows WAY-99
- **Verification:** an agent compares the change with the decision:
  - complies: a game's invariants say "castle gate" for the way into a castle where "the gate opens"
    could be read as the command that runs the tests, and a factory's say "assembly step" for an
    operation, while their code and interfaces use `Gate` and "Step"; a game's decision says "the
    map" for the map of a level, which no sentence of its foundation reads as the part map, and
    leaves it bare; a decision of a game says "dialogue sentence" for a message shown to a player
    where the bare "sentence" could be read as a sentence of a decision;
  - violates: a game's invariant says "gate" for the way into a castle in a sentence that reads as
    the command, or a factory's says "step" for an operation where it reads as a step of a task; a
    game's glossary defines "gate" as the way into a castle; every bare "map" of a game's decisions
    is rewritten to a phrase though no sentence reads it as the part map.
- **Origin:** none

*Rationale:* a word of the process written bare in a product's foundation for something of its
domain, or a word of the domain beside it, lets a sentence be read two ways by an agent that reads
the-way's rules beside the product's, and a qualifier on the use that sentence leaves open keeps each
sentence in one reading where the rules are read; a bare use no sentence reads two ways costs the
reader nothing, and qualifying it would only add words. The people who build and use the product keep
the words of its domain, since the rule protects the reading of the foundation alone. A product
cannot edit the glossary of the-way, so the *Not* that WAY-99 asks of the word's entry has nowhere to
stand, and a phrase holding the word, which WAY-99 refuses as a carrier, here keeps the word of the
field recognizable. A term's last word can stand for the process term in short form, so the same
test applies to a domain use of that word.
*Rejected:* the bare word of the process in a product's glossary, its meaning of the domain marked
beside it and reported as a warning rather than an error — one word carrying two meanings in the
repository is a cost now accepted where no sentence reads in the other meaning, but the variant stays
refused where a sentence can be read both ways, since a mark beside the word tells the reader nothing
at the use; the words of the process written in a fixed form in the-way, such as in backticks,
leaving the plain word free for the domain — a plain word in a product's sentence may still carry
either meaning, so the form keeps nothing apart, and every entry of the-way is rewritten to it; a
word holding neither the word of the process nor its forms, as WAY-99 asks of a carrier — for words
the field uses daily, such as "part", "entry" or "element", the foundation drifts from the words the
product's people and code use; qualifying a domain word only when it is a whole process term — a
short use of a multiword term can still collide with the domain meaning; the rule kept as it was,
with the bare uses of a product tidied by a separate task of the product — a sweep of many lines and
a cost of writing that grows with each term of the glossary of the-way, and a rule applied only
selectively; the rule removed — a sentence that reads as the process's stays unprotected; the bare
last word of a term, written as plain English in a phrase that bounds it, released from the rule — a
collision stays, and such a phrase is a qualifier already; the question left unsettled — each return
step qualifies words piece by piece and the inconsistency grows with every cycle.

## The part map and derived files

How files are assigned to parts, how a trust boundary is recorded, and what is generated or derived
rather than written by hand and how it is compared with its generator.

### WAY-44 — What assigns a file to a part?

Every file git tracks belongs to exactly one part of the map, by path patterns that git itself
matches, each naming a directory or one kind of file — every invariant test, say — rather than
listing a directory's files one by one, except the files at the root of the repository, which is the
directory of no part and whose files the map names one by one; a file that no pattern matches, and a
file that two parts claim, is an error of the check of the foundation, unless the map lists that
file as left out on purpose, and so is a pattern of a part's *Files* or *Trust boundary* that
matches no file git tracks. Tests belong to the part they test and generated files to the part of
their generator; the files that serve the whole repository — the lockfile and the build
configuration — are a part of their own; the files that serve the tests of several parts are
another, which its sentence describes as such with no field of its own, and which the tests of every
part may import while code that is no test may not; and the files that only direct whoever carries
out its tasks — instructions for agents, skills, hooks and the configuration of agents' tools and of
CI — are another. For a file that collects entries about many parts, the parts a change touches
follow from the entries it adds or changes, not from the part the file itself belongs to.

- **Scope:** part-map, agent-instructions, task-cycle
- **Based on:** git-path-patterns
- **Relations:** none
- **Verification:** invariants: cross-part-imports. For the rest, an agent compares the change with
  the decision:
  - complies: a change renaming `net/` to `network/` rewrites the *Trust boundary* `net/*.py` of
    its part, and `elements/common/foundation_check.py` reports no pattern matching no file; a
    helper that the tests of two parts import stands in a part whose sentence says it serves the
    tests of several parts; the root `AGENTS.md` and `CLAUDE.md` stand in the *Files* of their part
    each by its path, since the root is the directory of no part;
  - violates: the *Trust boundary* still names `net/*.py`, which matches no file git tracks, and
    the change is merged with that error of the check; a part whose tests use a helper of another
    part names that part in its *Depends on*; code that is no test imports a part of test helpers.
- **Origin:** none

*Rationale:* a change is read against the decisions and the invariants of the parts it touches
(WAY-21, WAY-62), so every file yields one part. git matches, because a second dialect could resolve
the same map differently. A pattern for a directory or a kind of file leaves the map as it is when a
file is added or moved inside it. A test changes what its part promises; files directing whoever
carries out tasks change every later task. A helper serving the tests of several parts tests
nothing, so a part of its own takes no test away from the part it tests, and the tests importing
it need no *Depends on* that would let the code of their part import it too; its sentence says
what it is, so the form of an entry stays as it is. The root of the repository holds files of
several parts and is the directory of none, so a pattern for it would name no part's directory, and
each file there is named by its path.
*Rejected:* a file in several parts — two answers, no rule to pick; patterns matched by a script
(fnmatch) — a second dialect beside git's; a pattern for each file — the map changes with every file
added or removed; tests as a part of their own — a test change stops counting against what it tests,
while a helper serving the tests of several parts tests nothing; files left unassigned in silence —
the map passes while saying less and less; a ledger file's part taken from its path — every recorded
decision counts against the decisions part alone; a helper serving the tests of several parts left
in the part it stands in, each part whose tests use it naming that part in its *Depends on* —
nothing in the process changes, but the code of those parts may then import that part as well, the
rule loosening for a whole part to let its tests through; imports from tests left unchecked — the
simplest check of the boundaries, but a test of one part reaching into the code of another goes
unseen; a field or a mark in the entry of a part of test helpers — it changes the form of the map in
every product while nothing needs it, and would serve only a script of the process reading the map;
the sentence left without the clause on the files at the root — the gap has no effect on the map or
its check, but a reader of this decision who reads it strictly sees a map that goes against it.

### WAY-48 — How is a trust boundary recorded?

A trust boundary is recorded at the part that holds it, as a pattern of the code files which take
in what the product does not control — data from the network, keys, the deployment, files that come
from outside the product, such as one on the user's disk — and never at a script that only checks
the product's own files. An exchange with the external context records its direction and
marks what comes in as untrusted. A change that touches the files of a boundary is checked for
crafted input, and its review is aimed at that risk.

- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the file that parses requests from the network and the file that reads a user's saved
    game are the boundaries of their parts; a change to a workflow holding a deployment key gets a
    review aimed at that key;
  - violates: a script that only checks the product's own files is recorded as a trust boundary; a
    change to the parser of requests is reviewed like any other.
- **Origin:** none

*Rationale:* a part that parses what a stranger sends is the oldest way in, whatever else it does,
so the boundary sets its checks on its own. A pattern of files is matched like parts (WAY-44). A
script that checks the product's own files takes in nothing a stranger wrote, and a boundary
recorded there spends the checks for crafted input on nothing.
*Rejected:* a trust boundary as its own kind of map entry — nothing reads it that the pattern does
not give; the boundary taken from the part's criticality — the exposed part is often the
unimportant one; every script that reads a file as a boundary — the checks for crafted input
spread over files no stranger writes; the boundary as a line in a diagram (pytm) — only a human
looking reads it.

### WAY-52 — What is generated from the part map for an agent?

Nothing is generated from the part map for an agent: an agent reads the entries of the parts its
change touches, and no overview of the repository is generated for it.

- **Scope:** part-map, decisions
- **Based on:** context-file-effect · claude-code-path-rules
- **Relations:** derives from WAY-21 · derives from WAY-44
- **Verification:** invariants: generated-overview. For what an agent reads, an agent compares the
  change with the decision:
  - complies: an agent working on a change reads the map's entries of the parts it touches;
  - violates: a rule file for agents is generated from the map.
- **Origin:** none

*Rationale:* agents follow instructions in context files, while repository overviews have not
helped. An agent reading the entries of the parts its change touches has the rules a generated file
would carry, with no derived file to keep in step.
*Rejected:* rules pinned to path patterns, generated from the map into the rule channels the tools
already read — a derived file to keep in step for what an agent reads in the map anyway; an overview
for agents — added context cost without measured benefit; rule files written by hand — a copy of the
map; the whole decision log on every path — relevant rules get lost among the rest.

### WAY-53 — How is a derived file compared with what its generator produces?

A derived file is identical to what its generator produces on the same commit, except for values the
file itself declares as varying between runs.

- **Scope:** decisions, part-map, invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-225
- **Verification:** invariants: derived-file-content.
- **Origin:** none

*Rationale:* equality with the generator's output catches a hand edit; a value such as the moment
of a run changes with every run, so only declared values are skipped.
*Rejected:* records of results kept outside the repository — a commit's result readable only from
whatever ran it; whole files lifted out of the comparison — a hand edit in them goes uncaught; a
derived file compared as a subset of its version on the commit the branch left the main branch from
— debt kept as a list beside the entries, while a violated rule is marked at its invariant (WAY-51).

### WAY-225 — What in a product's foundation is derived rather than written by hand?

What can be derived from what the product executes — code, configuration, infrastructure as code,
runtime traces — is derived, never written by hand, and what is derived describes the state. Rules
are written by hand: what is allowed and what the product promises, which the code cannot show, and
a dependency of a part that the code holds and the part map does not allow is recorded as an
invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies of a part
to fit the code.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: derived-file-content. For what is derived and what is written by
  hand, an agent compares the change with the decision:
  - complies: the map's allowed dependencies of a part are written by hand, and the return step
    compares them with the dependencies of a part that the code holds; a dependency of a part that
    the code holds and a human accepts although the map does not allow it stands as the invariant
    "the part `ui` does not depend on `storage`", marked violated;
  - violates: a hand-written architecture document appears next to the part map; a hand-written
    list of the product's endpoints kept next to the code; the allowed dependencies of a part in the
    part map copied from the current import graph.
- **Origin:** none

*Rationale:* a hand-written copy of the state goes stale, and code shows only what exists: a view
derived from it shows accidents as architecture, a rule copied from it turns one into law.
*Rejected:* a hand-written architecture document or diagram — a second copy of the map; "do not
write by hand what can be derived from code" as the whole rule — it reads as a demand to derive the
map's rules; derivation from code alone — behaviour shows in runtime traces, deployment in
infrastructure files.

## Scripts and the gate

The language, the version of Python and the handling of a missing field of the-way's scripts, the
rules the-way's own code keeps, and the one command that runs every test, with how a cycle runs it.

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the
same command for an agent, for a human and for whatever runs it when a change is merged —
and no list of checks written by hand stands beside it. In CI that command runs on every merge
request and on every system the product runs on, with `.the-way` at the commit the product pins
(WAY-34), from a file of CI configuration that the product writes itself by the description the-way
gives, and the installer writes none. The result of each such run is a check the repository requires
before a merge, and the owner of the repository may bypass it.

- **Scope:** invariants, agent-instructions, task-cycle, gate, installation
- **Based on:** github-required-status-checks · github-ruleset-bypass · foundations-branch-ruleset
- **Relations:** derives from WAY-34
- **Verification:** invariants: ci-checking-commands · gate-exit-code. For the same command for
  everyone and for its run in CI, an agent compares the change with the decision:
  - complies: the instructions for agents name that one command as the way to check a change; the
    CI file of the-way runs `python -B gate/run_tests.py` on every pull request into `foundations`,
    on Linux and on Windows; the description that the installer's README gives a product says that
    its CI file runs the one command on every merge request, on every system the product runs on,
    with `.the-way` at the commit the product pins, and that the result of each run is set as a
    required check with a bypass for the owner;
  - violates: the instructions for agents list test and lint commands of their own; the tests of
    the invariants run under a command of their own beside the product's tests; the installer writes
    a CI file into a product; a CI file runs a checking command beside the one command; the result
    of the run shows on a merge request and nothing requires it before the merge; the CI file of a
    product runs on one system where the product runs on two.
- **Origin:** none

*Rationale:* a list of checks written by hand is a second copy of the tests that drifts: a new
test never runs, a removed one still does. One command for all leaves no doubt which tests ran, and
running all of them leaves nothing to choose. The run in CI is the one that does not rest on the
agent or the human who made the change having run the tests, and it is made on a system that may
differ from theirs; a result the repository requires cannot be merged red by oversight, and the
owner's bypass leaves the owner able to merge while the CI itself is broken. The run is made on each
system the product works on because its result is the final gate of the product's task cycle
(WAY-160): a system left out is checked by no one at the end of the cycle. The product writes its
own CI file because the installer knows nothing of the product's environment.
*Rejected:* a gate taking its checks from the methods written in the entries and running those a
change calls for — a second runner beside the product's tests, and a choice of tests that can
leave out the one a change breaks; separate commands for an agent, a human and whatever runs the
tests when a change is merged — three lists to keep in step; the tests of the invariants under a
command of their own — of two commands an agent runs one; the installer putting a ready CI file
into the product — the file needs correcting by hand anyway, after which the installer overwrites
the product's changes or stops managing the file, and what the installer promises products, which
names the files it touches, changes; the-way giving products nothing for CI, each product building
it alone — the rule lives in one product, the next starts from nothing, and the installer goes on
saying only to run the tests before a merge; a required check with no bypass for the owner — a
failure of the CI blocks every merge until the owner turns the rule off, which the owner can do
anyway, so the difference is only more clicking; a result that is shown and requires nothing — a
red request can be merged by oversight; CI on one system alone — the tests that need the other
system run nowhere, and an error that shows only on that system shows only in use (in the-way, an
error of the installer with junctions on Windows); CI on one system and, on the machine of the work,
only the directories of tests that need the other system — the time of that run is unmeasured and
part of the load of the machine stays.

### WAY-38 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard
library alone, and installs nothing. It calls git, the Python interpreter running it, and the
commands a product declares in its own repository, reading their output through an adapter for the
format. Where a product declares no such command, the script reports what it could not check, never
agreement.

A test of a standing check runs the tool that the check pins from the environment that the
repository declares.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions,
  instruction-files, project-level, task-cycle, process-audit
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: script-language · script-imports · script-subprocesses.
- **Origin:** none

*Rationale:* a product runs the scripts of its pinned commit (WAY-34), so every language and
package they need is something each product has to provide. The state of a language the scripts do
not parse, the product's tools already compute; a check that quietly sees nothing would pass. A test
of a standing check starts the tool that the repository pins, from an environment that the repository
declares, so the check runs the same version on every machine and no script imports a library for it.
*Rejected:* Node.js without packages — no abler than Python, and a second interpreter for every
product; shell scripts in Bash or PowerShell — they run differently on Windows and on Linux; a
compiled program in Go or Rust — every change needs a build and published files; each script in
its author's language — every product needs every interpreter chosen; the product's CI committing
that output for the scripts to read — no signal before a push, and a CI step for this process
alone; the scripts parsing other languages themselves — tools that tried gave it up
(cargo-semver-checks).

### WAY-55 — Which part of the process holds the gate?

In this repository, the gate is a part of the process of its own, and its directory is
`gate/`: the gate's code and the test of every critical flow are files there. No other part's
directory holds that code or such a test, and a file under `gate/` that only calls a body kept in
another part's directory leaves the gate in that part. Which checks a change calls for, when the
gate runs and what follows from what it reports belong to the task cycle, not to this part.

- **Scope:** gate, decisions, invariants, glossary, part-map, environment-facts, relation-model,
  repository, task-cycle
- **Based on:** none
- **Relations:** narrows WAY-44
- **Verification:** an agent compares the change with the decision:
  - complies: the gate's code and a critical flow's test live under `gate/`, while the task cycle
    decides when the gate runs and how to use its result;
  - violates: a file under `gate/` only calls the gate's body kept in an element, or `gate/`
    decides which checks a change calls for.
- **Origin:** none

*Rationale:* critical-flow tests span parts and need a single owner. The gate serves every
element, so an element directory is the wrong owner; the task cycle decides the work to run, not
where its runner lives. As its own part, the gate carries its own failures.
*Rejected:* gate inside the invariants element — shared work owned by one element; gate inside
task-cycle — code coupled to task steps; gate among repository configuration — its failures lose
their own part; critical-flow tests in individual elements — no one element owns a cross-part flow.

### WAY-63 — What is an invariant's result, and when does the command running the tests fail?

An invariant's result on the commit being checked is `pass` where every test citing it ran on that
commit and passed, and `fail` where one of them failed; a run in which no test citing it ran gives
it no result, and nothing written by hand stands in for one. An invariant whose method is review
takes no result from a run: the review of each change it reaches compares the change with its
sentence. The command running the product's tests exits non-zero when a test fails.

- **Scope:** invariants, gate, part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-61 · derives from WAY-62 ·
  derives from WAY-08
- **Verification:** invariants: gate-exit-code. For the rest, an agent compares the change with the
  decision:
  - complies: an invariant whose two tests pass in a run is `pass`; the reviewer of a change to a
    part reads the invariants of that part whose method is review and compares the change with
    them;
  - violates: an entry reads "status: pass" written by hand; an invariant whose test did not run
    counts as passing; a review passes a change without reading an invariant whose method is
    review and which the change reaches.
- **Origin:** none

*Rationale:* the outcome of a test run on the commit is the only status that does not go stale; a
test that did not run says nothing, so it is no pass; a rule no cheap test checks has the review as
its reader (WAY-08).
*Rejected:* `unchecked` for a reason on a closed list, and `error` for any other missing verdict —
a vocabulary of results kept for a gate beside the product's own runner; a status written by hand —
stale with the next commit; an invariant whose method is review left unread — a rule nothing keeps.

### WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and
the declared version moves when the version in use leaves bugfix support, never because a newer
version comes out.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions,
  instruction-files, project-level, task-cycle, repository, process-audit
- **Based on:** python-314-bugfix-status · python-release-binaries ·
  https://raw.githubusercontent.com/python/peps/b53285d29f16cc743a7a6339c947c49ccf70c525/peps/pep-0745.rst
  § Bugfix releases — "3.14.14: Tuesday, 2027-10-05 (Final regular bugfix release with binary installers)";
  read 2026-09-30
- **Relations:** none
- **Verification:** invariants: python-version-declared · script-imports.
- **Origin:** none

*Rationale:* one declared version, not a floor, because a floor gives a script's verdict per
interpreter; the end of bugfix support sets the move because the Python project publishes no new
binaries during subsequent security-only support; the price: a product pinning the-way provides
exactly this version (WAY-34, WAY-38).
*Rejected:* the newest release, unnamed — the verdict depends on the date; "3.12 or later" with an
invariant per version admitted — a fact and a verdict for each; 3.12 alone — past its bugfix
support; a move at each new release — a yearly review nothing here needs; a move at the end of
security support — years without installers.

### WAY-160 — How does the task-cycle orchestrator run the finished change's gate?

The final gate of a task cycle is the product's gate on the tree that goes into the request, and the
request gives its command and exit code, or the CI run's, and names each check that failed or did
not run; a check that did not run is unchecked, never passed. The gate's run on the cycle's own
system is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's
*Checks* nor a handoff names a run of it. Where CI runs on a request whose code is finished — one
open for review, or one that waits only for human actions in the cycle — the CI run on the head
pushed last is the final gate, and the orchestrator runs no full gate itself at the end of the cycle
or after the merge with the target branch; the run on the base of the task branch and the run after
the pin of the-way moves stay the orchestrator's own, since no request stands then, and where CI
runs on no request, or the request is left blocked for unfinished code, the orchestrator runs the
gate itself on the tree that goes into it, save where that tree is one already run.

The orchestrator waits for the result of the CI run on each head it pushes to the request, a
correction's included, treats a red result as a failed gate, handled as the cycle's gate gives — a
fix and its review and the wait for the run on the new head, save a check outside the task's scope
that passes when run again, which WAY-261 governs — and puts the result into the request's
description. Where the run gives no result within 30 minutes of the push — it does not start, it
stands in a queue or the host does not answer — the orchestrator runs the gate itself on the tree of
that head, and the description says that CI did not answer and that the gate ran on the cycle's own
system; a request the cycle leaves blocked for unfinished code is out of that wait, its description
saying that the result of the CI run stands on the request's page and was not waited for. Where CI
is the final gate, the cycle's record says so before it is copied, and names the request whose
description gives the result, so that the next cycle takes the list of failing tests from there.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-16 · derives from WAY-63 · derives from WAY-148
- **Verification:** an agent compares the gate's run and the request with the decision:
  - complies: with CI running on the request, the orchestrator runs no gate of its own after the
    return step and its review, nor after the merge with the target branch, waits for the run on the
    commit it pushed last, finds it red, has the failure fixed and the fix reviewed (a check outside
    the task's scope that passes when run again goes as WAY-261 gives), waits for the run on the
    fixed commit and writes that result into the description; after the human's remarks it
    waits again for the run on the corrected head; the run gives no result 30 minutes after the push,
    the orchestrator runs the gate on the tree of that head and the description says that CI did not
    answer and that the gate ran on the cycle's own system; with no CI on the request it runs the
    gate once on the tree the return step and its review leave, and again where the merge with the
    target branch changed it, and the request gives the command and its exit code; a request blocked
    for a remaining blocking finding says in its description that the result of the CI run was not
    waited for, and the orchestrator ran the gate on the code the request holds; the record copied
    for a request whose final gate is CI says that it is, and where the result stands;
  - violates: the focused-check reports replace the gate on the finished change; the request calls
    a check that did not run passed; the gate ran on a tree other than the one the request holds; a
    plan's *Checks* or a handoff tells an executor to run the gate after its slice; the gate fails,
    its fix changes code, and the return step does not compare the fix's range; the request is
    marked ready while the CI run on it still goes; a red CI result is left for the human to find;
    the description names no CI result where CI ran on a request whose code is finished; a
    correction pushes a corrected head and the description keeps the result of the earlier head;
    the orchestrator runs the full gate on the cycle's own system as well, where CI gives a result
    within 30 minutes; the cycle waits beyond 30 minutes for a run that gives no result, or stops
    for it, or the description keeps silent that CI did not answer.
- **Origin:** none

*Rationale:* the finished change needs verification across the work that made it, which no
author's focused checks give. The command and its exit code, or the CI result, tell the human what
passed; the checks that failed or did not run, named, keep what stayed unchecked in view. A gate run
after every slice repeats for each slice a run the finished change needs once and holds the next
slice until it ends, while the focused checks of the code a slice reaches and of the invariants its
change may make false find what it breaks there. The return step compares the foundation with the
code and corrects what no longer matches, and it needs no result of the gate, so one run on the tree
it and its review leave covers the finished change, where a run before it would be made again on the
tree it changes. The CI run on the request is the same command on the systems the product works on
(WAY-16), so it replaces the cycle's own full run: a failure that shows only on a system other than
the cycle's own is caught, and the cycle's own system is not occupied for the length of a run that CI
repeats. Every push to a request with finished code starts a new run, so the wait follows each head,
a correction's too; a request blocked for unfinished code gets no wait, since its code will change
and a run on it settles nothing the human decides, and its page still shows the run. The cycle
never stops for the host of the repository: a limit on the wait and the gate on the cycle's own
system keep the work going where the host fails. The price is that a failure of the gate comes after
the return step, that the human receives the request later, by the time CI takes, and that a product
whose CI runs on fewer systems than the product works on leaves the others unchecked at the end of
the cycle.
*Rejected:* the gate's full output kept in a file of the cycle, with its failure lines brought into
the orchestrator's context — the exit code and the failures named settle the same; executor checks
in place of the gate on the finished change — the combined result is never checked; an exit code
alone — a check that did not run would pass unseen; the gate after every slice — it multiplies the
gate's run by the number of slices and holds each slice for it; rerunning after the return step
only the checks that read the foundation — the-way does not know which checks of a product read its
foundation; a cycle that hands over the request and leaves the CI result to the human — an error
visible only on the CI's system reaches the human and returns as a round of corrections; the CI
run in place of the gate also on the base of the branch and after the pin moves — the cycle would
push the branch and open a working request at its start, a larger change for two rare cases; a
cycle that stops and leaves the request blocked until CI answers, for the human to resume — a
failure of the host of the repository stops the work.

### WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?

A script of the-way that reads a file an agent or a human writes checks that the file holds each
field the script needs — a field being any named thing the script looks for data by in the file: a
section heading, a row label, a table column or a JSON key — and where a field is missing or stands
under another name the script ends with an error that names it, never guessing and never reading the
absence as an empty value. The rule binds a script that a change adds and, in a script that a change
changes, the whole reading of each file whose way of reading the change reworks — every field of that
file, no other file and no other part of the script — and a missing field ends the script with exit
code 2 and a message that names the file and the field, except that a script whose purpose is to
check the form of a file reports a missing field whose presence it checks as a finding of its list,
with exit code 1, and except that the command that counts the audit, in a file of a cycle's record
that it reads from git history, gives the values that need a missing field as unknown, writes its
result and ends with exit code 1 and a line `Error:` that names the file and the field — a field
that an earlier form of the file never had being no missing field where the command reads the file
as that form, which it does for a stage report that has no heading of its detailed section and holds
a table of tokens by model, for one that has neither of its two time lines, and for one whose
detailed section has no column *Files named*, and which gives the values that need that field as
unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own
change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives
no line `Error:`. Where a script whose purpose is to check the form of a file reads a copy of the
file from the commit the branch left the main branch from, a field it needs for a comparison and
finds missing from that copy is listed by a line `listed:` that names the entry and the field, with
no error and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file
without one of the fields it needs and asserts the failure that names that field, the review of the
change answering for the other fields; the *Scope* names every part of the-way's part map, and a
change that adds a part to the part map adds it to this *Scope*. The command that counts the audit,
where a table of weights or a table of the costs of an occurrence in the register of problems lacks
one of its levels, writes its result, gives the values that depend on the table as unknown and ends
with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither
of the two columns of the cache writes in its detailed section, that command reads the report as an
earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and
priced as input, an approximation, and no value unknown for the missing columns, while a stage
report that has one of the two columns and not the other has a missing field, with the line
`Error:`. Where the command that counts the audit reads a cycle's record that lacks a line or an
item it reads of it — the line `Process pin` or `Target branch and base`, or the item `Process
remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or `Slices returned too large` — the
record is of an earlier form and no field is missing: the command gives the values that need it as
unknown, with a reason that names the line or the item, no line `Error:` and no change of the exit
code. Where the locations file has no entry `repository` under `the-way`, no field is missing and
that command takes the checkout in which its script lies.

- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts,
  elements-common, project-level, task-cycle, foundation-review, gate, repository,
  agent-instructions, instruction-files, installation, product-guidelines, process-audit
- **Based on:** none
- **Relations:** derives from WAY-38
- **Verification:** tests: that a field missing from a Claude Code transcript, which the script of
  the stages reads, or from the definition of an agent type, which the generator of the copies
  reads, ends the script with exit code 2 and a message that names the field, and that each such
  reading has a test that gives the file without a field; that the command that counts the audit, at
  a field missing in the file of the measures, the file of the gate times or a stage report, gives
  the values that need it as unknown, writes its result and ends with exit code 1 and a line
  `Error:` that names the file and the field; that it reads a stage report of an earlier form, one
  with no heading of its detailed section, with neither time line, with no column *Files named* or
  with neither column of the cache writes, with no line `Error:` and gives the values that need what
  that form never had as unknown, and the cost of a form with no columns of the cache writes with
  the writes priced as input; that it reads a report that has one time line or one of the two cache
  write columns and not the other as a missing field; that it reads a cycle's record that lacks the
  line `Process pin` or `Target branch and base` or an item it reads of it, with no line `Error:` and
  no change of the exit code, and gives the values that need it as unknown with a reason that names
  the line or the item; that a table of weights or of the costs of an
  occurrence which lacks a level gives the result, unknown values and the line `Error:` that names
  the level; that a locations file with no entry `repository` under `the-way` gives the checkout in
  which the script lies and no line `Error:`; that the check of the foundation lists an invariant
  whose sentence the change reworded and whose copy at the commit the branch left lacks its *Method*
  or its *Part* by one line `listed:` that names the invariant and the missing field, with no error
  and no change of the exit code; and that the file of a tool the cycle's own change changed is not
  read. An agent compares a change with the part no test holds:
  - complies: a new script reads a JSON file in which the key `due` of the issues has become
    `due_date`, and ends with exit code 2 and a message naming the file and `issues.due`, and its
    test gives the file without that key and asserts that the message names it; a change that
    reworks how a script reads the section headings of a report brings every field of that report
    under the check, adds one test that gives the report without one heading, and leaves the
    script's reading of other files as it was; a script whose purpose is to check the form of a file
    lists an absent section it checks as a problem with exit code 1; a change that adds a part to
    the part map adds its identifier to the *Scope* of this decision in the same change;
  - violates: a script reads the absent key `due` as no due date and gives its result with no
    error; a script that is neither a check of form nor the count of the audit lists an absent
    field as an item with exit code 1; a script whose purpose is to check the form of a file stops
    with exit code 2 at an absent section whose presence it checks; a change that reworks the
    reading of a file checks the field it added and leaves the other fields of that file unchecked;
    a new script's reading of a file, or a changed script's reworked reading of a file, has no test
    that gives the file without a field; a change that adds a part to the part map leaves this
    *Scope* as it was.
- **Origin:** none

*Rationale:* a script that reads a file an agent writes meets a changed format as an absent field,
and an absent field read as a value — no items, no date, no finding — lets the check the script
exists for pass with no error to show it, the same quiet pass that WAY-38 keeps out of the check of a
product's commands. The coding guidelines of the-way point to this rule for a missing field of a file
a script reads and repeat none of it (WAY-379), so the requirement stands once, in the-way's own log.
An error naming the field lets the author of the change or the cycle repair the file or the script at
once; exit code 2 says the
file was not read, apart from a listing of findings, which a caller carries out as findings, and
apart from the count of the audit, whose file in the history of git no later change can mend and
whose run, at night with no human present, would otherwise leave the session of the audit with no
result at all, the figures of the register of problems included; the count writes what it could read,
leaves unknown what the file does not give and ends with the error that names the field, so that the
error is seen and the rest of the result is not lost. A field that an earlier form of a file never
had is no loss of the file but the way that form was written, and the count of the audit reads the
files of cycles of every form; read as missing, it would end every count in exit code 1 for as long
as such files are counted, and an exit code that every run gives carries no signal. The record of a
cycle is such a file: a record lacks an item that the template gained after it was written, and it
carries no sign that names its form, so every line and item the count reads of it is read as one an
earlier form may lack. The rule covers
the whole reading of a file a change reworks, so that the old reads of that file, which a change of
format threatens most, are not left unchecked, and one test per reading, not one per field, keeps
the cost of the check in proportion. The price: a change that reworks the reading of a file
pays for the check of every field of that file; a stage report that has lost its two time lines, its
detailed section while a table of tokens by model remains, the column *Files named* of that
section, or the two columns of its cache writes, is read as the earlier form and gives unknown, or
for the cache writes the cost as the approximation, where the rule alone would give an error; an
existing script that no change touches stays as it is, so the rule protects new and changed readings
first; and the review alone answers for the fields beyond the one each test gives up. Tests of a
script's behaviour stand without an invariant, since WAY-12 concerns how a decision is checked. A
table of the register of problems that lacks one of its levels leaves the rest of the register
readable, so the count writes what it can read, gives unknown the values that depend on the table
and names the missing level, and one misspelt level costs the session of the audit those values and
not the whole result; a heading or a table that the register lacks leaves what depends on it
unreadable and stays exit code 2. The entry `repository` under `the-way` is the one entry of the
locations file that the count can do without: the checkout in which its script lies is the-way's
own, so the lack of the entry is a choice to read from it and no field lost. The exception is
written for that entry alone, since a rule that let a script read any field that has a default as
optional would let the next author call any field optional. A stage report with neither column of
the cache writes was written before the columns existed, and its cost is the approximation it has
always been, so the count reads it as that; a report with one of the two columns has lost the other,
which is the case the rule is for. A copy of a file at the commit the branch left is a file no
change can mend, and what it lacks is a gap in what the check compares with, never a fault of the
change; the check lists it, so that the reviewer learns that a reworded sentence was not compared,
and ends with no error for a gap the change did not make.
*Rejected:* the rule as a sentence of WAY-379 — WAY-379 settles whether the-way applies the template
of the coding discipline, and this rule is a requirement, not an adoption or a departure; an agent
that writes a script would look for rules in WAY-38 and the invariants `script-language`,
`script-imports` and `script-subprocesses`, not in a decision about a template; the rule as a
decision with an invariant whose *Part* is `every`, like `script-imports` — an invariant claims
something of every tracked script on every commit, so it needs an entry stating whether it holds
today; without a review of every existing script any such entry is a guess, and marking it violated
(WAY-51) would keep watch over new and changed scripts only while claiming a violation with no
evidence; the whole script as what a changed script brings under the rule — a small fix grows into
a review of every field the script reads, and the agent that reviews it has to read the whole script
instead of the diff; only the readings of fields that the change adds or reworks — an existing
script can stay checked by halves for good, and the old reads, which a change of format threatens
most, stay unprotected; review alone with the test left to the choice of the cycle — an agent that
reviews easily overlooks one unchecked field among many, and a later change that quietly removes
the check breaks nothing; review and a test for every field — as many tests as fields, and for a
file of a dozen fields the test costs more than the check, a work that falls on every change that
reworks the reading of a file; exit code 1 always, a missing field as an item of the list — the
orchestrator carries out a listing with exit code 1 as findings, and for the script that lists the
process remarks every item goes into the remarks word for word (WAY-294), so a missing section in a
report would become a process remark and the report would stay uncorrected, the same quiet pass the
rule prevents; a new exit code, such as 3 — each skill that reads exit codes would have to be
extended; exit code 2 with no result for the count of the audit — the count runs at night with no
human present, so the session of the audit has no result, the numbers of the register of problems
included, until someone mends the script; the exception for the stage report alone, the file of
measures and the file of gate times keeping exit code 2 — a file of either kind from any old cycle
that fits no form stops the whole weekly result; for a table of the register of problems that lacks
a level, exit code 2 with the level named and no result — one misspelt level leaves the session of
the audit without a result until the register is mended; for the entry `repository` under
`the-way`, exit code 2 — whoever has no entry gets no result of the audit in the morning, and the
intended return to the own checkout is gone; for the same entry, a general exception for a field
whose absence the description of a script allows with a default — a door by which the next author
can call any field optional; for a generator of copies that shares its exit codes with another
script, an exception written into this decision — the list of exceptions grows by a case with no
reason beyond convenience, and the next script can copy it; for a field missing from the copy at the
commit the branch left, an exception that leaves the invariant out with no word — a reworded
sentence whose copy has a gap passes with no one told that it was not compared; the same case left
as the cycle that wrote the check left it, with no sentence — the code departs from this decision
and the departure returns at the next review.

## Instruction files

What an instruction file that a tool loads holds, how it points to other files, when a rule enters
or leaves it, how its rules are kept and judged, and how it is shared and installed.

### WAY-128 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand?

A line for a file that an agent's tool loads into every session — one the skill of
`instruction-files` proposes, or one a change to the-way's repository instruction files adds or
rewords — is one that every session needs or that points to work an agent would not otherwise find,
that an agent could not read from the repository or from general knowledge, and without which an
agent would go wrong; where an agent may not recognise the moment such a pointer is for, its
condition is worded as an agent meets that moment, and the rule it points to stands whole in that
file only once records of agents' work show they missed the reworded pointer. Any other rule the
skill proposes or such a change adds stands where what calls for it reaches the agent: a rule for
some files in a file the tools load with those files, a rule for an activity in the steps of the
skill that carries out that activity or in the file that leads it, and knowledge needed now and
then in a file such a step or line points to. Lines that stand unchanged are not bound by it, and
the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256, and to the
text the installer writes in an entry point, instead.

- **Scope:** instruction-files, agent-instructions
- **Based on:** context-file-effect · claude-code-path-rules ·
  codex-agents-md
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a change adds to the-way's root `AGENTS.md` a line pointing, with its condition, to a
    guide no session would find otherwise; the skill proposes to move a rule for one directory's
    files into a file loaded with them; the skill, finding that agents passed by a pointer whose
    condition named the work otherwise than they meet it, proposes to reword that condition;
  - violates: the skill proposes a line describing a repository's directories and stack; a change
    adds to the-way's root `AGENTS.md` the test command its guide already gives; the skill proposes
    to keep a rule for one activity whole in the root `AGENTS.md` only because an agent might not
    recognise its moment.
- **Origin:** none

*Rationale:* a line loaded into every session costs context in each, and agents carry out what it
asks, so it earns its place only when each session needs it; descriptions of a repository have not
helped agents, while the instructions they are given are followed; a rule loaded with the files or
the activity that call for it costs nothing elsewhere; one tool reads a subdirectory's file only in
sessions started at or below it, so such a file needs a line that points to it. An agent that does
not recognise the moment a rule is for does not reach for its pointer, so moving such a rule out
switches it off without a sign; a reworded condition costs one line where the whole rule costs its
length in every session, so the rule comes back whole only on proof from records of the work, as a
new rule enters (WAY-130). A skill loads with its activity, not into every session, so where its
fragments stand follows the decisions on skills. Unchanged lines stay as they are because the
process enters an existing product (WAY-28).
*Rejected:* a fixed count of lines as the measure of a file — a count says nothing of whether a
given line is needed, even where a shorter file saves context in every session; a file of pointers
alone — it leaves reading each rule to the agent's choice; a file of its own for every area with
rules of its own — a split changes nothing unless it changes when the rule loads; a rule kept whole
in the file whenever an agent might miss its moment — any rule could be kept on that ground; rules
drawn from the repository's code — the agent reads the code itself; binding the lines that stand
today — every unchanged line would become a breach on the day of the merge.

### WAY-129 — How does an instruction file point an agent to another file?

The-way's repository instruction files hold no `@` import other than the line `@AGENTS.md` alone at
the top of the root `CLAUDE.md`, and the skill of `instruction-files` proposes none other. A pointer
the skill proposes, or a change to the-way's repository instruction files adds, names the file to
read by its path in backticks with the condition under which to read it.

- **Scope:** instruction-files, agent-instructions
- **Based on:** claude-code-imports
- **Relations:** none
- **Verification:** invariants: instruction-file-imports. For the condition beside a path, an agent
  compares the change with the decision:
  - complies: a pointer reads "Before you change the-way, read `agent-instructions/README.md`";
  - violates: a pointer reads "See @docs/style.md for the style"; a list of paths with no word on
    when to read them.
- **Origin:** none

*Rationale:* an import loads the whole file it names into every session, so a file meant for
occasional reading costs its full length in each; a path with its condition costs one line and is
read when the condition comes.
*Rejected:* `@` as a light pointer — it loads, it does not point; the text of the file pasted in — a
second copy that drifts.

### WAY-130 — When does a rule enter an instruction file, and when does it leave?

The skill of `instruction-files` proposes a rule, and a change to the-way's repository instruction
files adds one, only to remove a mistake agents made more than once, found in records of their
work, and names that mistake where it proposes or adds the rule, unless the rule carries a decision
the repository records or a step of an activity in the file that leads that activity. The skill
proposes to take out a rule added for a mistake once that mistake can no longer be named, or once
agents working without it show that it is not needed.

- **Scope:** instruction-files, agent-instructions
- **Based on:** https://arxiv.org/html/2511.12884v2 § 4.2.3 — "The evolution of Agent context files
  is driven by small, incremental additions, while deletions are minimal." · § 4.2.3 — "this
  suggests that the increase in line counts is not simply due to uneven edit sizes, but instead
  reflects a meaningful tendency to add new instructions rather than remove existing ones."; read
  2026-10-08
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a change adding a rule to the-way's root `AGENTS.md` names in its request the mistake
    it removes and the records where agents made it twice or more; a change adds to the guide that
    leads the-way's integration the step a new decision sets, with that decision as its reason; the
    skill proposes no rule for a mistake it found once or not at all;
  - violates: a rule added "just in case" after one slip recalled from memory; the skill proposes a
    rule whose mistake it did not look for; a rule against one slip is added to the guide as a step
    of the work.
- **Origin:** none

*Rationale:* files grow by small additions and are rarely cut, so a rule needs a way out from the
day it enters, and the mistake it removes is that way out. A repeated mistake is the signal; a
single one is watched, and a mistake recalled days later gives no material for a rule. A rule that
carries a decision, or a step of the work a file leads, has its reason and its way out in that
decision or that work.
*Rejected:* rules added ahead of any mistake — nobody can test them; a rule for a mistake seen once
— one slip says nothing of the next session; a register of lessons written from memory — the mistake
is lost before the rule is written; removal by the calendar — a long absence of a mistake may be the
rule working; one test for the rules against mistakes and for the steps of a guide or the rules a
decision sets — a guide could gain no step of new work until agents had gone wrong without it.

### WAY-131 — How is it settled whether a rule of an instruction file works?

Where the skill of `instruction-files` says whether a rule works, and where the request of a change
to the-way's repository instruction files says so, it is settled as three separate questions:
whether the tool loaded it, by one fresh session per variant with a file that has to load as a
control; whether agents followed it, by as many fresh sessions with and without it, on one model
and tool release, as its effect needs to stand out from the variation between runs; and whether it
helped, by whether its mistake stops coming back in agents' work over time, never by test sessions
alone.

- **Scope:** instruction-files, agent-instructions
- **Based on:** agent-run-variance
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a rule whose behaviour never happens without it is shown working by a few sessions
    with and without it; a rule meant to make a behaviour more frequent is judged over many sessions
    or by watching its mistake;
  - violates: a few sessions with and without are taken as proof that a rule raised a behaviour
    that also happens without it; a rule is called useless because one session did not load it.
- **Origin:** none

*Rationale:* loading, following and helping fail apart and are fixed apart — another carrier, other
wording or a mechanism, or nothing; runs of one agent on one task differ, so a small effect drowns
in a few sessions. The finding on that variation measured models of other publishers only, and this
decision takes it across publishers (WAY-85).
*Rejected:* the same small number of sessions with and without for every rule — it settles only a
behaviour absent without the rule; one question "does it work" — it mixes defects with different
fixes.

### WAY-132 — Which file carries the instructions Claude Code, Codex and Cursor share?

The skill of `instruction-files` proposes for a repository whose agents use more than one of Claude
Code, Codex and Cursor, and the-way keeps for itself, a root `AGENTS.md` that carries the
instructions those tools share and a root `CLAUDE.md`, where there is one, whose first line is
`@AGENTS.md` alone and which holds only what Claude Code alone needs. The skill leaves out of this
proposal the files and the marked block the-way's installer writes in a product.

- **Scope:** instruction-files, agent-instructions
- **Based on:** claude-code-agents-md · codex-agents-md · cursor-agents-md ·
  claude-code-imports
- **Relations:** none
- **Verification:** invariants: root-claude-md-import. For what `CLAUDE.md` holds and for respecting
  the installer's files, an agent compares the change with the decision:
  - complies: the-way's `CLAUDE.md` is the one line `@AGENTS.md`; the skill proposes, after the
    import, a note for Claude Code alone; in a product, the skill leaves the installer's root
    `CLAUDE.md` and marked block of `AGENTS.md` to the installer;
  - violates: the skill proposes a `CLAUDE.md` restating the rules of `AGENTS.md`; the skill
    proposes to delete the installer's root `CLAUDE.md` or edit the block between the installer's
    markers.
- **Origin:** none

*Rationale:* the tools read a shared instructions file at the root, while Claude Code reads it by
itself only where no file of its own stands; a file of its own that opens by importing the shared
one keeps one copy for them all and still lets Claude Code take additions of its own, which Cursor's
command-line agent reads too, since it reads that file as well; a rule kept in two files drifts.
What the installer writes in a product answers to the installer's own surface and stays outside
this decision.
*Rejected:* a full file for Claude Code beside the shared one — two copies that drift; relying on
Claude Code reading the shared file by itself — a file of its own, added later by hand or by a tool,
turns that reading off, and some sessions cannot read the shared file at all, for which Claude
Code's documentation advises importing it from a file of its own; a file of its own that is a link
to the shared one — Claude Code's documentation advises the import instead wherever someone who
clones the repository works on Windows.

### WAY-133 — How is a rule of an instruction file kept when it has to hold every time?

Where a rule of an instruction file has to hold every time, the skill of `instruction-files`
proposes a mechanism that keeps it without the agent choosing to — a CI check, a linter, a check of
a step's output, or a local git hook where the rule guards against slips rather than against an
agent that can turn the hook off — and a change to the-way's repository instruction files adds such
a rule only with its mechanism. The instruction file then says what the mechanism is for, or
carries what the mechanism cannot check.

- **Scope:** instruction-files, agent-instructions
- **Based on:** single-rule-compliance
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the skill proposes a CI check for a rule it found broken in commits, and an
    instruction only for what the check cannot read; a change adds to the-way's guide a rule that
    every commit names its task, together with a CI check that fails a request whose commits name
    none;
  - violates: a change adds a rule that has to hold on every commit only as a line of `AGENTS.md`;
    the skill proposes a hook of one agent tool, or a local git hook, as what keeps a rule against
    an agent that can switch it off.
- **Origin:** none

*Rationale:* a loaded rule is still not always followed, so what has to hold every time needs a
mechanism that does not depend on the agent; the instruction beside it explains, so the agent meets
the rule at the first try. A local hook — of an agent tool or of git — is skipped by one switch, as
WAY-03 weighed, so it keeps a rule against slips, never against an agent that can turn it off; a
hook of one agent tool also reaches only that tool's sessions.
*Rejected:* an instruction alone, worded more strongly — a stronger wording is still a loaded rule,
which is not followed every time; a mechanism with no word to the agent — the agent learns of it
only by failing it; a local hook as the keeper of every rule — one switch skips it.

### WAY-141 — How does the installer give Claude Code the guidance in a product's root AGENTS.md?

When a product has no root `CLAUDE.md`, the installer creates one whose sole line is `@AGENTS.md`,
so Claude Code receives the installer's block and the product's other instructions from root
`AGENTS.md`. When a root `CLAUDE.md` already exists without an effective `@AGENTS.md` import, the
installation plan warns about the missing import, and the installer leaves every existing root
`CLAUDE.md` untouched. The installer writes no `.claude/rules/the-way.md`.

- **Scope:** installation
- **Based on:** claude-code-imports · claude-code-agents-md
- **Relations:** none
- **Verification:** invariants: installation-claude-guidance.
- **Origin:** none

*Rationale:* importing the shared instructions gives Claude Code the product's backlog location
as well as the installer's guidance through one route. An existing file may hold product guidance,
so the installer reports a missing import before confirmation and leaves the file to its owner.
*Rejected:* a generated rule repeating the installer's block — it duplicates guidance without
carrying the product's other instructions; adding the import to an existing file — it changes
product-owned guidance without its owner's choice.

### WAY-258 — How are the files of the skill of `instruction-files` laid out?

The skill of `instruction-files` keeps beside its `SKILL.md` one file for each kind of text it
works on — a file a tool adds to every session, a skill, a file a tool loads with some files — and
its step that works on a kind names that kind's file. No rule stands in two of its files, and no
file of a kind holds a rule another kind needs: such a rule stands in its `SKILL.md`, or in a file
a step names as WAY-256 gives, or, once such rules are so many that the work on one kind reads
mostly the rules of others, in one shared file each such step names directly. No file of a kind
points to another file.

- **Scope:** instruction-files
- **Based on:** claude-skill-nested-references
- **Relations:** derives from WAY-256 · derives from WAY-100
- **Verification:** an agent compares the change with the decision:
  - complies: the step that judges a skill names the file of skills, and the rule on emphasis,
    which every kind needs, stands once in `SKILL.md`;
  - violates: the file of skills tells the agent to read the file of the main file for its rule on
    pointers; the rule on emphasis stands both in the file of skills and in the file of the main
    file.
- **Origin:** none

*Rationale:* the work on one kind reads the rules of that kind and those all kinds share, not the
rules of the others, which keeps fewer instructions in play at once (WAY-256); a full judgement of
a repository still reads every kind's file, so the gain lies in work on one kind. A rule kept in two
files drifts. Anthropic's guide for skill authors warns that a file reached through another
referenced file may be read only in part, and recommends references one level deep from the
skill's main file; it speaks of Claude alone, and the decision keeps the same depth for Codex and
Cursor on that word, since a route one level deep costs nothing in any tool.
*Rejected:* one `SKILL.md` with a section for each kind — every use reads the rules of every kind;
a pointer from one kind's file to another for a rule both need — a reference two levels deep; a
rule repeated in the file of each kind that needs it — the copies drift; a cap on the lines of a
skill's main file, as the same guide recommends — a count says nothing of whether a step needs a
rule (WAY-256).

## Skills and agent types in sessions

How a session reaches the-way's skills and agent types, and where the fragments and variants of a
skill stand.

### WAY-127 — How does a session working on the-way itself reach the-way's skills?

A session working on the-way itself reaches each skill of the-way as the project skill
`the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md`
and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from
the skill's `SKILL.md`. An entry point reads its skill, and each file the skill names when the step
that names that file comes rather than all of them at the start, from the checkout or worktree the
session works in — where it was started, or where it was last moved — stops itself in a product, and
hands another the-way skill on under the `the-way-` prefix. No global link reaches a skill of the-way
other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows
that repository's pinned copy instead, and the-way is not installed in itself.

- **Scope:** agent-instructions, elements-common, project-level, task-cycle, decisions, invariants,
  glossary, part-map, environment-facts, installation, instruction-files
- **Based on:** claude-code-project-skills · claude-code-nested-skills ·
  codex-repository-skills · codex-skill-paths
- **Relations:** derives from WAY-44 · derives from WAY-256
- **Verification:** invariants: skill-entry-points. For when an entry point has the files a skill
  names read, an agent compares the change with the decision:
  - complies: an entry point has the session read the skill's `SKILL.md` whole and a file the skill
    names from the same worktree when the step that names it comes;
  - violates: an entry point has the session read the skill and every file it names before the
    skill's first step.
  For the paragraphs of the skills that say where the-way lies, an agent compares the change with
  the decision:
  - complies: a skill's paragraph names, as the place of the-way, the checkout or worktree the
    session works in for the-way itself and the pinned `.the-way` for a product, and names
    another the-way skill it hands to as the project skill with the `the-way-` prefix;
  - violates: a skill tells an agent to resolve a global link to find the-way; a skill run in the-way
    hands its work to `critique` without the prefix.
  For the global link and the skill of `instruction-files/`, an agent compares the change
  with the decision:
  - complies: a global link leads to `instruction-files/` of a worktree kept at the merged tip, and
    the skill judging a product that pins the-way follows that product's
    `.the-way/instruction-files/SKILL.md`;
  - violates: a global link leads to another skill of the-way; the skill judges a product that pins
    the-way with the copy its global link reaches.
- **Origin:** none

*Rationale:* a session on the-way tries a change to a skill with the skill of its own branch, so a
skill it reads from another checkout tests nothing it changed. Entry points tracked in the
repository reach every checkout, worktree and cloud session with no step to set them up, and
generating them from the skills keeps no list of skills by hand and puts them, as generated files,
in the part of their generator (WAY-44). The checkout or worktree the session works in sets which
copy is read, because a tool may offer one checkout's entry points to a session in another
worktree, and a session moved to another directory gains that directory's entry points beside
the ones it started with; stopping in a product keeps a session there on its pinned the-way
(WAY-34); the entry point's own directory, which Codex lists with each skill, lets the first product
check find a product's submodule. The prefix keeps a personal skill of the same name from standing in
for one of the-way's. The skill of instruction files serves repositories outside the-way and its
products too, where no entry point exists and the copy a global link reads is the one wanted; in a
product the pinned copy governs (WAY-34), so the skill follows it there; a session on the-way still
reaches its branch's copy through its entry point, and the-way's repository instruction files keep
it to the prefixed skill. A fragment that only one variant of a skill needs, or only one step that
some uses pass by, stands beside the skill so that it leaves the text read at the other steps
(WAY-256); an entry point that had every file a skill names read at the start would bring each such
fragment back into play at once.
*Rejected:* a mode of the installer without a pin writing the same entry points into the-way — its
generated files would belong to `installation`, outside that part's directory, and its trust
boundary would grow; entry points written per checkout and ignored by git — a fresh worktree or
cloud session has none until someone writes them; global links, one per worktree, or links tracked
by git — a global link reads one checkout whatever branch the session works on, and tracked links
need a git setting and extra rights on Windows; names without the prefix — which skill a session
gets would rest on how Claude Code and Codex settle two skills of one name; an entry point that has
the skill and every file it names read at the start — the fragments placed beside a skill for one
step would load with the skill.

### WAY-256 — Where does a fragment of a skill stand?

A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of
the-way's process included, or one a change to a skill of the-way adds or rewords — that only one
variant of the skill needs, or only one step that some uses of the skill pass by, stands in a file
beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an
element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the
picture of the whole, the rules of working that hold across its steps, the pointers, every step
until records of sessions a person can open, those of Claude Code and Codex, show that part of the
uses since the step stood in the skill pass it by — also where no record exists — and a fragment of
one step or variant that is one instruction, which would otherwise stand in a file beside the skill,
stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond
that, a fragment's place follows from whether a use of the skill needs it at that step, never from
the count of words or lines of the file. A fragment that some steps of the skill need, not all,
stands by what it is: a rule of working that the agent has to keep during those steps stays in the
skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template,
stands in a file beside the skill that each of those steps names, a step after the first having that
file read unless an earlier step did; fragments that stand unchanged are not bound by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts,
  elements-common, project-level, product-guidelines, task-cycle
- **Based on:** single-rule-compliance · instruction-density-accuracy
- **Relations:** derives from WAY-100 · derives from WAY-128
- **Verification:** an agent compares the change with the decision:
  - complies: a change adds to a skill of the-way the form of a report only its last step writes,
    in a file beside the skill that the step names, and a line in its `SKILL.md` pointing to it;
    the skill of `instruction-files`, judging a skill with a mode only some uses take, proposes to
    move that mode's checklist into a file the mode's step names; a rule of an element's entries a
    change adds stands in the element's template; the one sentence only one variant of a skill
    needs stands in that variant's row of the skill's `SKILL.md`, where a pointer to it would stand;
    a template that three of a skill's five steps use stands in a file beside the skill, each of the
    three steps names it, and the second and third have it read unless an earlier step did, while
    the manner of asking the human, which the agent keeps at every step that asks, stands in
    `SKILL.md`; a step that the records of sessions show every use of the skill coming to stays in
    `SKILL.md` while the variant only some uses take stands in a file beside it that the step
    names, and a skill with no records yet keeps every step in `SKILL.md`;
  - violates: a change adds to a skill's `SKILL.md` a page of rules only its review step uses; a
    step that the records of sessions show every use of the skill coming to is moved to a file
    beside it; a step is moved to a file beside the skill though no record shows a use passing it
    by; the skill of `instruction-files` proposes to cut a skill to a number of lines; a change puts
    a rule of an element's entries into a file beside the element's skill; a file beside a skill
    holds one instruction and its step names it by a pointer; a step keeps several instructions only
    one variant needs in `SKILL.md` because each of them is short; a list that two steps consult is
    pasted whole into `SKILL.md` and carried through the steps that do not use it; a rule of working
    that three steps keep stands only in the file of the first, so the other two never reach it; a
    step names a file and has it read again though an earlier step read it.
- **Origin:** none

*Rationale:* a single rule is not lost in a longer file, while the more instructions an agent has
to carry out at once, the fewer it carries out; a fragment the step at hand does not need adds to
the instructions in play without being used, so it leaves the text read at that step where a use may
pass the step by, and the measure is the instructions in play over the uses of the skill, not the
words. A step that every use of the skill comes to is in play in every use wherever it stands, so a
file of its own spares no use anything and adds a pointer and an opening sentence to what each use
reads; estimated before any rebuild from the word counts of the files of one skill, that shape
reads five to fifteen percent more words in a typical session than keeping its steps in `SKILL.md`.
The estimate is this product's own, and its record is not open to a reader of this repository.
A step therefore stays in `SKILL.md` until records of sessions a person can open show that part of
the uses pass it by, while a variant, which the text of the skill shows, goes to a file beside it as
before. With no record the step stays, since a skill given a file for each step before any record
exists may be rebuilt back after its first use, one session deciding the shape. The weak point: a
step often passed by and not yet measured is carried until someone counts the records, and skills
already rebuilt with a file for a step every use reaches stop matching the rule, though they do not
breach it, since fragments standing unchanged are not bound. The finding on density measured single
prompts dense with instructions to include keywords, not an agent's work through a skill, and a file
read at an earlier step stays in context, so only the instructions of steps not yet reached leave;
no one has measured it on a skill. The shape — a main part holding the picture of the whole, the
rules of working, the pointers and the steps every use comes to, with the guidance of each variant
and of each step some uses pass by in a file beside it — is borrowed from a course on steering
models through context, whose lessons are not open to a reader of this repository, and only that
shape is adopted (WAY-100); the course's claim that a model
follows all of a long skill's instructions with a chance close to zero is not, since no measurement
stands behind it. The rules of an element's entries stay where WAY-35 places them, since every
writer and check reaches them there, and this decision orders what else a skill holds. A change to a
skill of the-way is bound because a fragment it adds would otherwise go anywhere until the skill is
judged; fragments standing unchanged are left until each skill is rebuilt, since binding them would
make every skill a breach on the day of the merge. A fragment that is one instruction, moved out,
leaves a pointer in its place, which is an instruction too: the instructions in play stay as many,
and a file is added to keep. The exception reaches no further than one instruction against the one
pointer that would replace it, so a fragment of more instructions cannot stay on the ground that
each of them is short. What an agent keeps while it works must be present at every step where it
works, so it cannot stand in the file of one step, while what it only consults is needed at the
steps that consult it and leaves the text read at the others; the rule that a later step has the
file read unless an earlier step did keeps the file from being read again where the agent already
holds it, at the price that the later step depends on what an earlier one did, and a session that
skipped the earlier step reads the file there. The boundary between a rule of working and text to
consult is a judgement, made in the row of the judgement that places the fragment.
*Rejected:* a short skill as the aim, after the course's claim — no measurement stands behind it; a
threshold of words or lines for a skill — a count says nothing of whether a step needs a fragment;
the skills of the-way's process left to WAY-35 alone — what neither a template nor the shared part
holds would follow no rule of place; binding only what the skill of `instruction-files` proposes —
a new fragment of a skill of the-way could land in its `SKILL.md` until the skill is judged;
binding the fragments that stand today — every skill would breach it on the day of the merge;
every fragment one step or variant needs moved out, one instruction included — it trades an
instruction for a pointer and adds a file; a file beside the skill for every step, one that every
use of the skill comes to included — in such a skill it adds a pointer and an opening sentence to
each use and spares none, an estimate of five to fifteen percent more words read in a typical
session, made before any rebuild from the word counts of that skill's files (the estimate is this
product's own, and its record is not open to a reader of this repository);
an exception named for one skill alone — the smallest change, but the next skill of the same profile
raises the question again, and an exception named after a skill, not after its files, leaves the
question to each skill; no change to the decision, the exception kept only in the document of the
work that rebuilds the skill — a change that breaks a binding decision is reported by a reviewer,
and the next session takes the skill as breaching it; for a skill with no records, the rule as it
stood, with the measurement deciding from the first recorded use — the smallest change, but a new
skill is given a file for each step and may be rebuilt back after its first use, one session
deciding its shape; the same with a threshold of recorded uses — one session decides nothing, but
the number is arbitrary and unmeasured, and until it the skill carries a file for each step. For a
fragment that some steps need, not all: no rule, each case settled by the table of a judgement —
every later skill settles the same question anew, and a reviewer may block each choice; everything
that more than one step needs stays in `SKILL.md` — the main file grows by text carried through
steps that do not use it, and the layout of files already made for skills with such fragments stops
matching the rule.

### WAY-265 — Where is the file of a variant named, when a step's file points to it?

In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file
points to is named in the skill's `SKILL.md` at that step as well, with the condition under which
it is read. A step's file that stands unchanged, with the variant file it points to, is not bound
by it.

- **Scope:** instruction-files, decisions, invariants, glossary, part-map, environment-facts,
  elements-common, project-level, product-guidelines, task-cycle
- **Based on:** claude-skill-nested-references
- **Relations:** derives from WAY-256
- **Verification:** an agent compares the change with the decision:
  - complies: the file of a skill's second step says research is read from a file beside the skill
    when research runs, and the skill's `SKILL.md` at that step names the same file and the same
    condition;
  - violates: the research file is named only in the second step's file, so an agent that read the
    skill's `SKILL.md` cannot see that the file exists.
- **Origin:** none

*Rationale:* an agent that reads a skill's `SKILL.md` then sees every file its use may reach and the
condition of each, and a file reached through another file, which Claude may read in part, is not
the only way to it. The cost is a file named in two places that must be kept equal, and a step's
file that stands unchanged, with the variant file it points to, differs from one rebuilt.
*Rejected:* the variant named only in the step's file, as in a layout with two levels — the layout
stays at odds with the rule of references one level deep, and the rule has to change or a reviewer
reports it in every later skill; the variant left in the step's file — every use reads variants it
does not need, against the aim of WAY-256.

### WAY-368 — Which agents run the stages of a task cycle in Claude Code?

In Claude Code, a task cycle dispatches the one author of a change without a plan as an agent of the
type `the-way-author` and every other stage agent as an agent of the type `the-way-stage`, two types
of the-way's own that give their agent every tool of the session except the skill tool. Each type
has a body of its own saying what it is, and only the type of the one author has the prompt cache
lifetime that WAY-255 gives that agent. A stage agent reaches each method, and each skill a method
names, as a file by its path, never by calling a skill; the installer writes the definitions of the
pinned commit into a product, replacing and deleting only its own files, and the copies a session on
the-way itself loads are generated from them and tracked.

The agent types of a task cycle start with the instruction files that Claude Code loads into an
agent of the session, the user's and the product's; no definition of a type sets the field that
starts an agent without them.

- **Scope:** task-cycle, installation, agent-instructions
- **Based on:** claude-code-subagent-skills-denied · claude-code-subagent-cache-ttl ·
  claude-code-subagent-agent-directories · claude-code-subagent-instruction-files
- **Relations:** derives from WAY-125 · derives from WAY-127 · derives from WAY-34
- **Verification:** an agent compares a change with the decision:
  - complies: in Claude Code the orchestrator dispatches the one author with the type
    `the-way-author` and the planner, an executor of a slice and a reviewer with `the-way-stage`;
    each handoff gives the path of the method's file; a definition names no tool of the session and
    sets no model; a definition added to the-way is written into a product by the installer and has
    its generated copy in the tracked directory of the session on the-way;
  - violates: the orchestrator dispatches a reviewer with the harness's general agent in a session
    that has the types and records no reason; a handoff tells a stage agent to call a skill; a
    definition lists tools by name or gives the skill tool back; the definition of a type other than
    the one author's sets the hour lifetime; the installer overwrites a file of a product that is
    not its own.
  For the start with the instruction files, an agent compares a change with the decision:
  - complies: a definition of a type holds the fields `name`, `description`, the denied tools and,
    for the one author, the cache lifetime;
  - violates: a definition sets the field that starts the agent without the instruction files.
- **Origin:** none

*Rationale:* a stage agent started as a general subagent carries the list of every skill of its
session before it reads its first file, and few agents of a cycle use a skill: in the session
records of the cycles of one game product 72 of 625 subagents did, and in those of the-way 4 of 252
(the count is this product's own, and the session records are not open to a reader of this
repository). A probe on a copy of that product, on Claude Code 2.1.322 and Sonnet 5.5, measured the
start of a subagent at 36,711 tokens with the skill tool and 21,759 without it: the list of skills
(29,896 characters) disappeared whole, the definitions of the tools shrank from 13 tools (31,547
characters) to 9 (22,639), and the instruction files (23,658 characters) stayed. A type with every
tool of the session but the skill tool starts about two thousand tokens larger than the probe's
agent, which had a narrow list of tools, so the start is lighter by about 37% where the probe's was
by 41%; both are estimates from the table of tool definitions, not measurements. The gain of the
lighter start was estimated, for the narrow list of tools, at about 4.5% of a cycle's cost. The
probes and the estimates are this product's own, and their record is not open to a reader of this
repository. A definition with no body gives its agent a system prompt of 1,722 characters in place
of the 3,158 of a general subagent, so each type has a body that says what it is. The tools of
connected servers, a browser's among them, stay, so an agent that has to look at an interface can,
and the-way names no tool of a plugin that a product may not have. An agent without the skill tool
reads a method as a file, which is how its handoff already gives it (WAY-125, WAY-148); and the
personal skill of the same name that the list showed beside a skill of the-way, which an agent could
take for it, is no longer shown. Two types and not one, since only the one author is resumed, after
each review and for the return step, and a cache of five minutes is written again after each such
break: in a probe of the cache, a subagent with the hour, resumed after 6.9 minutes in a live
session, read 10,470 tokens from the cache and wrote 123, where a control with five minutes wrote
its whole 4,786 anew (WAY-255 holds the account of the hour). The definitions come from the pinned
commit like the entry points of the skills (WAY-34), and a session on the-way itself has tracked
copies as it has those entry points (WAY-127), so that its cycles use the types as well. The price:
an agent of these types cannot call a skill, a personal skill for work with a browser included;
Claude Code loads the types of a directory that existed when the session started, so a session
started before the installer or a checkout created that directory has no such types, and its cycle
dispatches as before (WAY-370). The instruction files are the part of the start that the types keep.
The field that drops them drops the user's file, which holds the rules of git, of scripts and of
privacy, and the product's file together, and the product's file alone cannot be kept; starting
without them lowers the start by about eleven thousand tokens, to 10.5 thousand, a figure whose
conditions — version, model, tools — are not recorded. A later decision may reverse this where the
handoffs of the stages begin to name the product's instruction file themselves. The figure is this
product's own measurement, and its record is not open to a reader of this repository.
*Rejected:* three types, with a narrow list of tools and a third type with the browser tools named —
the-way would write into its file the names of the tools of one user's plugin, and in a product
without it the type would have nothing to check an interface with; the orchestrator would decide at
each dispatch whether a stage looks at an interface; and the one author of a change to an interface
would need a fourth type; two narrow types, with the stages that look at an interface dispatched as
a plain subagent as before — the cycle of a change to an interface would have neither the lighter
start nor the author's hour of cache, and the orchestrator chooses the type for each stage anyway;
start without the instruction files — the start falls to 10.5 thousand tokens, but the agent loses
at once the user's global instruction file (the rules of git, of scripts and of privacy) and the
product's instruction file, and the product's file alone cannot be kept.

### WAY-370 — What does a task cycle do where the session has none of the-way's agent types?

Where the session has none of the-way's agent types, because the harness is not Claude Code or the
session started before Claude Code could load them, the task cycle dispatches each stage as it would
without them and writes in its record that the stage ran without its type. The-way defines no agent
types for Codex.

- **Scope:** task-cycle, installation
- **Based on:** codex-project-agents · codex-agent-skills-config ·
  claude-code-subagent-agent-directories
- **Relations:** derives from WAY-368
- **Verification:** an agent compares a cycle and its record with the decision:
  - complies: a cycle in Codex dispatches its stages as the harness does without the types, and its
    record says in each dispatch's row that the stage ran without its type and why; a product
    installation writes no Codex agent definition;
  - violates: a cycle dispatches a stage without its type in a session that has the types and writes
    nothing of it into its record; the installer writes a definition for Codex.
- **Origin:** none

*Rationale:* the sessions from which the gain of the types was counted hold none of Codex, so no
probe showed a gain there. Codex turns off the skills of an agent one skill at a time, with a
setting for each, so the list kept in the process would grow with every skill added to the-way and
need care in each change. A stage dispatched without its type loses only the saving: its handoff
already names the method by its file, so the stage reads the same text.
*Rejected:* types for Codex too, defined in the directory Codex reads project agents from — the list
of skills they turn off grows with every skill and the process would have to keep it, and no probe
showed a gain.

## Project definition

What a project writes before tasks exist, when its definition is ready for breakdown, and how its
projected entries and open questions move on.

### WAY-106 — What does the project level write before tasks exist?

The project level reads a product's foundation and records prospective changes in the project
definition; it writes no foundation entries. The definition holds the project's settled scope and
projected foundation entries, while the project plan holds phases, task order and which task
realizes or writes each projected entry.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01
- **Verification:** an agent compares the change with the decision:
  - complies: a definition projects a new decision and the plan later assigns a task to write it;
  - violates: the definition writes the future decision into the product's foundation, or assigns
    projected entries to tasks before the breakdown has made those tasks.
- **Origin:** none

*Rationale:* the foundation describes what the product holds today; a project first settles what
the product is to become. The task assignment follows the breakdown and changes with it, while
the definition remains the source of what was settled.
*Rejected:* putting projected entries into the foundation at the readiness gate — it would describe
a future product as current; keeping the task assignment in the definition — it would duplicate
the plan and change as the plan changes.

### WAY-118 — What makes a project definition ready for breakdown?

The readiness gate blocks a definition with a missing section, unresolved content, an open
question without its place of resolution, an unfinished candidate search, or an unsettled
human-given part of a projected entry: its binding sentence or definition and a decision's
rationale and rejected options; only projected fields awaiting code or the world may read `TODO`.
Before approval an agent searches the whole current foundation once for what the definition and
its projected entries touch, linked or not, the only search of the whole foundation on the way to
the gate, and the human approves the whole projected entries with permitted `TODO`; the gate
record then names the approver and the fingerprint of the definition's sections from Goal through
Projected foundation changes, and no projected entry carries a field of approval. A change to those
sections after approval goes through the gate again before breakdown relies on it.

- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: project-readiness-gate. For the foundation search and human
  approval, an agent compares the work with the decision:
  - complies: the script stops an unfinished candidate table, the agent resolves a collision with
    an existing decision found by the one search at the gate, and the human approves the finished
    proposals;
  - violates: a warning-only review lets the breakdown begin with a missing decision reason, an
    edit to a fingerprinted section after approval keeps the old gate record, or the foundation is
    searched whole for each candidate or projected entry and again at the gate.
- **Origin:** none

*Rationale:* a warning lets a later step guess precisely what definition was meant to settle;
blocking exposes the missing answer while the person who can give it is present. The fingerprint
shows which wording was approved. Once every projected entry is written, one search sees them all
and the definition's own text; the gate record approves them together.
*Rejected:* a final checklist that only warns — it cannot prevent an unfinished search from
passing; an approval without a content fingerprint — later edits would still look approved; a
search of the whole foundation when the candidates are named and for each projected entry as well
as at the gate — it repeats the gate's search on wording not yet settled; *Approved by* in each
projected decision — it repeats the gate record.

### WAY-126 — How does a projected entry enter the foundation?

A projected entry of an approved project definition enters the product's foundation in the
change of the first task whose code makes it true — the task the plan assigns, or a task
that uses the definition as a source only, even where the plan assigns the entry to another task —
whole, in the wording the readiness gate approved, with the projected terms and environment facts
it uses or rests on and with no record of approval copied from the gate, since the merge of the
task's request brings it in; where the code makes only part of it true, the agent writes that part
and the human accepts its meaning at the merge (WAY-114). The task the plan assigns writes what of
the entry the foundation does not yet hold, and a projected entry no code makes true. The return
step reads the projected entries of the task's sources as well as the foundation, writes one the
code makes true that the foundation step missed — an invariant with its test run on that code — and
writes a new entry only for a rule none of them states.

A change that writes a projected entry into the foundation replaces each descriptive `TODO` that
points at it with a reference to it by its identifier: in a decision's *Relations* as
`derives from <number>`, and in an invariant's *Derives from* as the number.

- **Scope:** project-level, task-cycle, decisions, invariants, glossary, environment-facts,
  part-map
- **Based on:** none
- **Relations:** derives from WAY-01 · derives from WAY-11 · derives from
  WAY-114 · derives from WAY-118 · narrows WAY-106
- **Verification:** an agent compares the change with the decision:
  - complies: a source-only task whose code adds the store a projected decision chooses writes
    that decision whole in its foundation step, and the task the plan assigns later finds it and
    writes nothing; a task whose code makes one of a projected decision's two sentences true writes
    that sentence and puts its meaning before the human in the request's section for the human's
    decisions; a plan member whose code would make another item's entry true returns to the plan
    first; a task whose code makes a projected decision true writes it into the log and replaces
    the `TODO` that names it with `derives from <its number>` in the *Relations* of a decision and
    with its number in the *Derives from* of an invariant;
  - violates: the return step writes a new decision for a rule a projected entry of the
    task's source states; a task writes a projected decision into the log and leaves a decision's
    *Relations* reading `TODO — <that decision, and where it is expected>`; a shortened projected
    entry is written as the gate approved it, its
    meaning left out of the request's section for the human's decisions; the code a late-found
    projected invariant covers is set aside and rewritten.
- **Origin:** none

*Rationale:* a projected entry is wording a human already settled at the gate, and the task
whose code first makes it true is the one that can show it holds; entering with that code keeps
the foundation describing the present product and keeps one entry per rule. A part of an entry is
wording the gate did not approve in that form, so its meaning reaches the human at the merge.
*Rejected:* holding a projected entry back for the task the plan assigns — the foundation would
lag behind the code it describes; a return step that searches only the current foundation — a
rule settled in a definition comes back as a second entry under another name; carrying a
shortened entry as approved — the foundation would gain binding sentences no human approved in
that form; rewriting the code a late-found projected invariant covers — its test, seen failing
once and read by the review of the change, guards it without a second implementation.

### WAY-145 — Who sets where an open question of an approved project definition is resolved?

Once a project definition has passed its readiness gate, the place of resolution it gives an open
question is the question's first assignment, and the plan decides from then on where the question
is resolved: in a task of the plan, or by an answer the human gives or the plan quotes, with its
place, from the definition or the foundation. Work on the plan may move a question to another task,
with an entry in the plan's log of changes giving the reason and without taking the definition
through its readiness gate again, while a move that changes which task writes a projected entry
into the foundation is the human's to decide. A question that arises only in the breakdown goes to
the human before the plan is handed over.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-118 · derives from
  WAY-126 · derives from WAY-100
- **Verification:** invariants: project-plan-check. For moves, answers and new questions, an agent
  compares the plan with the decision:
  - complies: the breakdown moves the question on a session's secret from the task of the test
    server to the task of accounts, where sessions first exist, and writes why in the log of
    changes; the breakdown finds that nothing says whether the test server is public from the first
    account and asks the human before handing the plan over;
  - violates: a question lands in another task than the definition names with no entry in the log;
    the definition is edited and gated again to move a question; a move that hands the writing of a
    projected decision to another task is made without the human; the breakdown answers a question
    from its own reading of the code; a question found in the breakdown waits in a task as an
    unknown.
- **Origin:** none

*Rationale:* the place a definition gives a question is set before the tasks exist, so the
breakdown is the first to see where the question meets the work; moving it changes the way to the
approved scope, not the scope the human settled at the gate. A move left unwritten looks like the
plan's own reading of the definition, so the log makes it visible. Which task writes a projected
entry sets when the foundation comes to hold it, so a move that shifts it reaches the human. A
question the breakdown raises was settled by nobody, and the human answers it while the plan can
still change. An answer the definition or the foundation already gives needs no human to restate
it, and quoted with its place it can be checked against its source. The rule takes from the
practice of a roadmap (WAY-142) the carrying of each open question of the source into the plan
word for word, and a question that arises in the breakdown put before the human; the practice is that of the skill of a roadmap of lesson m2l1 of the
10xDevs course, whose lessons are not open to a reader of this repository, and the move of a
question written into the log of changes is the rule's own.
*Rejected:* a move taken through the gate again — the definition would be approved again for a
change of route alone; a flag marking a task blocked by its unknowns, beside a list of deferred
work, as the practice of a roadmap has them — the states of a task already hold waiting for the
human, and the list repeats the definition's exclusions; a question moved without a word — a reader
takes it for the definition's own placement; only the human answering a question the breakdown
resolves — the human would restate what the foundation already holds; the practice's blockers
outside the team, such as an approval a vendor or a stakeholder owes, kept apart from its unknowns
— left out of what the rule takes from it; the owner the practice names for each unknown — left out
of what the rule takes from it.

## Technology choices

Where and by whom a technology choice is settled, how its options are found, tested and shown to a
human, and what a reserved choice does to a task.

### WAY-121 — Where does a project settle the technology it needs?

Before a project definition goes through its readiness gate, a step of its own lists the
technology and architecture choices the project needs — such as a language, a framework, a store
of data or a place to run — and, for each, either names the decision of the foundation that
already holds it or settles it as a projected decision of the definition; a project whose every
choice the foundation holds thus settles nothing. A choice belongs on the list when settling it
later could change how the work is cut into tasks, or when it adds something the product has to
run, pay for or back up; a choice one task can make and change alone stays with that task, while a
choice under this rule that a definition missed, or that no definition holds, is settled through a
run of the step at a task document (WAY-267, WAY-268). As an exception to that rule, where the
project brings behaviour a user sees in the running product, the step looks at four matters of an
agent's way to the running product — its logs, its interface, its development data and the place of
its screenshots — and lists as a choice of its own each matter that no decision of the foundation
settles for that behaviour, even where its answer adds nothing to run, pay for or back up, and even
where the product has none of what the matter names, whose answer then says what an agent uses in
its place; how a human learns of a failure of the running product is no such matter and has an
exception of its own (WAY-270).

The answer to a matter of an agent's way to the running product — its logs, its interface, its
development data or the place of its screenshots — is a decision of the product, although it tells
an agent how to work; a skill of the product may hold the steps of operation and cites that
decision.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-100
- **Verification:** invariants: project-technology-record. For what the step lists and settles, an
  agent compares the work with the decision:
  - complies: a project that adds an account server lists its store of data and its way of logging
    in, and the definition projects a decision on each; a project that changes only how a screen
    looks, in a product whose foundation already says how an agent reaches its screens, where its
    screenshots lie and, where the product runs outside the machine it is made on, how a human
    learns of a failure, records that the foundation holds every choice it needs; a project that
    moves a product to a server lists, besides its place to run, how a human learns of a failure, as
    WAY-270 gives; the first project of a game played in a browser lists the game's logs, its
    interface, its development data and the place of its screenshots, each as a choice of its own,
    and projects a decision on each although reading the server's output and opening the game on a
    local address add nothing to run; a later project of that game, whose new screens an agent
    reaches and whose screenshots lie as those decisions say, lists none of the four; a command-line
    tool that keeps no data lists its development data, answered by sample input files kept with its
    code; a task of a plan needs a store of data its definition missed, and the human settles it in
    a run at that task's document, the approved definition untouched; a product whose skill for
    playing its game holds the steps to start the game cites the decision that settles the way to
    the game and the place of its screenshots;
  - violates: a product keeps the way to its game or the place of its screenshots only in a skill,
    with no decision of its log; the first task of the breakdown chooses the database; a definition
    reaches the gate with a store of data in its scope and no choice of it projected or found in the
    foundation; a project that brings a product's first screen leaves out how an agent operates it
    because a browser on a local address adds nothing to run; the logs, the interface, the
    development data and the place of the screenshots stand on the list as one choice; a project
    that brings a product's first screen leaves out where the screenshots lie because nothing runs
    for them; a product that keeps no data leaves its development data off the list for that
    reason.
- **Origin:** none

*Rationale:* whether a technology choice changes how the work is cut into tasks cannot be judged
by someone who does not know the technologies, so the choice is settled before the cut; a step of
its own keeps the comparison of technologies out of the talk about the project's goal and scope,
while its agent still knows the whole project. Settled before the gate, the choices are approved
with the rest of the definition, and an exit for a project whose choices the foundation already
holds keeps the step from being an empty run. A choice a definition missed, or that no definition
holds, still goes to the human through the step, and at a task document it changes no approved
section, so no gate returns. A task cycle checks behaviour a user sees in the running product as
well, and an agent with no way to the running product either leaves that check undone or improvises
its access in the middle of the cycle. The commonest answers — logs read from
the output of the product's container, the product opened in a browser on a local address — add
nothing to run, pay for or back up and change no cut of the work, so the rule of belonging alone
would never list them; the exception lists each matter as a choice of its own, weighed apart, and
only where no decision already answers it, so the first project of a product settles each in a
short decision and later projects find it in the foundation. A product with no screen or no stored
data still needs the answer that says what an agent uses instead. The place of the screenshots is
a matter of its own because the screenshot an agent takes to show the human is the evidence of its
check of the running product, and a file in the product's repository stays in its history for good
(WAY-316); left to the cycle, one request commits the files and another shows none, and a product
that settles the place with the step learns of the gap before its first request with a changed
screen, not at it. The step takes from the lesson "Towards Autonomous Product Development" the
question of how an agent sees the running product — through its logs, its interface and its
development data; the place of the screenshots is no part of the lesson. The lesson is not open to
a reader of this repository. The answer to a matter stands in the log, though it tells an agent how
to work, because the step that looks for the answer to each matter looks in the log, and a choice
with a cost — one way to the product instead of another, a place for screenshots outside the
product's repository — keeps its reasons and the ways not chosen there, where a skill gives a rule
one sentence of reason; the skill of the product keeps the steps of operation and cites the
decision.
*Rejected:* a round inside the conversation about goal and scope — no place to compare
technologies; the first tasks of the breakdown — the cut itself may depend on the choice; the step
after the readiness gate — each settled choice would change approved sections and send the
definition through the gate again (WAY-118); one step for every project with no exit — an empty
run wherever nothing changes; the agent's way to the running product as items every definition
holds, checked by the readiness gate — every project repeats what is settled once for the product;
a question about that way in the refinement of every task — every task records the same answers
with no need of its own; the rule of belonging alone for those matters — their commonest answers
would never be listed, and looking at them would settle nothing; a requirement of the step beside
the list — a new place in the form of a definition, and its answer would not reach later projects
as a decision of the foundation; the logs, the interface, the development data and the place of the
screenshots as one choice — it binds independent choices together, and a later change to one reopens
them all; one heading the step splits into as many choices as the product needs — whether a matter
is left out would rest on the agent's judgment alone; the matters on the list the deployment skill
of a product covers (WAY-139) — only a task that deploys the product checks that list, so a product
run on a local machine alone would leave an agent with no way to it; only the behaviour when no
place for screenshots is settled (WAY-316), with the step unchanged — a product learns that it has
no place only at its first request with a changed screen; the lesson's hard limit that keeps an
agent away from the production database and from root access — left out of what the step takes from
the lesson, since WAY-140 already leaves every effect outside the repository to a human, and reading
stays with the agent; the answer to a matter in a skill of the product — the step would have to
look in the skills as well, and a choice with a cost, such as one way to the product instead of
another or a public place for screenshots, would lose its reasons and the ways not chosen, since a
skill gives a rule one sentence of reason; the answer left to the product's decisions with nothing
written here — the next product applies the first question of the template of decisions as the
first did, and withdraws them again.

### WAY-122 — How are the options of a technology choice found and checked before a human sees them?

The options of each technology choice a project or a task needs come from research of that choice
against the project definition or, in a run at a task (WAY-267), against the task document and the
run's note, rather than from a fixed list of bundled stacks, and the research of every choice that
depends on no unsettled choice starts once the list of choices is confirmed, each in a report of
its own. An option the product's code is written in or against — a language, a framework, a
library, a store of data — is weighed by whether its documentation shows that it uses
explicit types, follows conventions of layout and naming and has current, versioned documentation,
and whether a public record of its use, such as a package registry or a survey, shows it widely
used within its language family; for a store of data, its types are those it declares for what it
stores, and its family is that of its query language. An option lacking one of these properties is
offered with what each lack means for the product, which the decision records if the human chooses
it; an option with no documentation or with a project no longer maintained is left out with that
reason, unless the human named it or the definition or the task document holds it as a constraint,
and then it is offered with that reason as such a lack; and every option is offered only after a
critique that refutes every claimed difference between the options which no source supports.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-120
- **Verification:** an agent compares the work with the decision:
  - complies: research for a store of data compares a file kept beside the application with a
    database server, each typed and documented, and the critique strikes a claimed difference in
    speed that no source gives; a built-in module with no record of wide use stays in the
    comparison beside a widely used library, its lack said as what it means for the product; a
    run at a task compares error trackers against the task document and the run's note, and a
    service the document names as a constraint, its project no longer maintained, is offered with
    that lack;
  - violates: the step offers a framework, a database and a host as one bundle from a fixed list;
    a comparison reaches the human with a difference no source supports; an option with
    documentation and a maintained project disappears from the comparison because it lacks one of
    the properties; an option the human names disappears from the comparison; the research of a
    choice that depends on no unsettled choice waits for another choice to be settled.
- **Origin:** none

*Rationale:* a fixed list of stacks, each bundling a framework, a store of data and a place to run,
settles several choices at once and without the project, so a bundle can run against choices the
project already holds and leave others unsettled; research for each choice starts from what the
project or the task needs. Research of independent choices run side by side and kept in reports
lets the conversation settle one choice while the next is researched, and nothing found is lost to
a long conversation. An agent can read each of the properties off an option's documentation or its public
record of use without the human knowing the technology, and each bears on how well an agent works in
the stack; a lack of one is a cost to weigh, not proof the option fails the product, while an option
with no documentation or no maintenance leaves nothing to weigh. A place to run or a way of logging
in has no types and no language family, so it is weighed by its consequences alone and checked by
the critique. An option the human brings stays the human's to choose, with what it lacks on record.
A comparison the human cannot verify needs an independent reader that refutes what no source
supports.
*Rejected:* a fixed list of bundled stacks with a default for each kind of product and language —
one pick settles several choices, unrelated to the project; options from research shown unchecked
— the human cannot tell a sound comparison from an invented one; the human checking the options —
the human this step serves cannot assess the technology; a critic for each option — one critique of
the whole comparison serves (WAY-120); never offering an option the human names that lacks a
property — a constraint from outside the project would lose to the properties; the properties as a
filter that leaves out every option lacking one — a missing version on a documentation page
excludes an option whose lack costs the product nothing, and the recommendation turns to the widely
used option with no gain for the product; research one choice at a time — the human waits for each
research in turn.

### WAY-123 — How does a technology choice reach a human who cannot assess the technology?

The step that settles technology, at a project definition or at a task (WAY-267), shows each choice
in plain text, in words a person who does not know the technology can follow: the options that
decide it, each under its own name, by their consequences for the product — what it costs, where
it runs, what keeping it running takes and what changing it later costs — the other options one
line each, and the lines of the options left out; the human chooses between those consequences. A
difference with no consequence for the product decides nothing, and where no difference with a
consequence remains, the step recommends the simplest and cheapest option. The choices whose
research started together reach the human together, in one message, one choice after another, once
every one of their comparisons has passed the critique and a fresh agent has checked, in the first
message, before it is shown, that no option stands there by figures or features instead of what it
changes for the product and that no word stays that a person who does not know the technology cannot
follow without an explanation, each choice with its recommendation and the weak point of the option
recommended; in the area of the choices this step settles, this decision prevails over WAY-114,
under which a question goes to the human only where the agent has no recommendation.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-113 · narrows WAY-114
- **Verification:** an agent compares the work with the decision:
  - complies: two stores of data are shown as "a file kept with the application and copied with
    it for a backup" against "a server to keep running in the container, with backups of its
    own", and the human picks one;
  - violates: the options are shown as lists of technical features or as columns of figures; every
    option of a choice, those that do not decide it too, is described at full length; a consequence
    is described with a word such as "bundler" that a person who does not know the technology cannot
    follow without an explanation; the first message reaches the human before a fresh agent has
    checked it; two options with no difference in consequences are offered as a matter of taste
    instead of the simpler one being recommended; two choices whose research started together reach
    the human in separate messages.
- **Origin:** none

*Rationale:* a human who cannot assess the technology can still weigh what an option costs and
where it fails, so a technical difference reaches the decision only through a consequence. Where
options differ in nothing the product feels, a choice between them is blind, and the simplest and
cheapest keeps cost and upkeep lowest. Independent choices shown together are settled in one
answer, and the weak point stated with the recommendation lets the choice stand without a question
asked after it (WAY-113). Plain text, one choice after another, is what such a human reads: a table
puts every datum of every option side by side, and a human who cannot weigh it takes the
recommendation as offered. Only the options that decide a choice are described at length, which
keeps the message short enough to read. The check by a fresh agent catches what the author no longer
sees in its own text — figures or features standing for a consequence, a word of the technology's
trade — and it is a judgement, not a mechanical rule, so it sometimes flags a word the human
knows, and the author adds an explanation nobody needed. The price of the form is a longer message,
and the loss of the comparison of the options across one page; the check covers the first message
alone, so a word of a later follow-up goes unchecked.
*Rejected:* technical differences shown as they stand — the human cannot weigh them; falling back
on a default bundle when the human cannot judge — with no fixed list (WAY-122) there is no default;
the agent choosing alone — the choice binds the product, and a human approves decisions (WAY-14);
every choice shown on its own, followed by a question against it — the human waits between choices,
and each choice costs two exchanges; each comparison shown as soon as its critique passes — the
choices reach the human one at a time; the options in one table as before — nothing breaks at
once, but a table invites taking the recommendation as offered, and a recommendation can pass that
the human would not have chosen; the table with a paragraph in plain words beneath it — the fewest
changes, but the longest message, and the table is still not read; a sentence that names a tool only
where its name carries a consequence — a bare product name stands where two forms of one tool
differ, and the human has to ask for the difference; the check for figures and features alone — it
costs nothing, but a word of the technology's trade in a consequence still reaches the human and
costs a further exchange.

### WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?

Where the options of a place to run differ in no consequence for the product and more than one of
them is the simplest and cheapest, the step that settles technology, at a project definition or at
a task (WAY-267), recommends, of those, the one an agent works with best: operated from a terminal,
deployed by a script and documented in pages an agent can read. For a place to run, how well an
agent works with an option decides nothing else: it leaves no option out of the comparison and is
weighed against no consequence for the product.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** narrows WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: two hosts that cost the same and take the same upkeep remain after the simplest and
    cheapest rule, and the one with a command-line tool and a deployment script is recommended; a
    host with no command-line tool stays in the comparison and is recommended where it costs less
    than the others;
  - violates: a host whose deployment cannot be scripted is left out of the comparison for that
    reason; a host is recommended over a cheaper one because an agent can operate it from a
    terminal; the consequences shown to the human score how well an agent works with each host
    beside its cost.
- **Origin:** none

*Rationale:* an agent writes the deployment for a place to run and reads what it reports, yet a
place to run has no types and no language family (WAY-122), so nothing in its comparison says how
well an agent works with it. Placed after every consequence for the product and after cost and
simplicity, the property chooses only between options the product does not tell apart, so it never
carries a choice against what the product needs. It seldom decides, since options rarely tie on
cost and simplicity; written down in that place, it keeps the property from entering higher, as a
filter or a weight, where an option that suits the agent would beat one that suits the product.
*Rejected:* how well an agent works with an option as a filter — a place to run the project's stack
needs could be left out for a missing command-line tool; as a weight beside the consequences — a
property the product does not feel could outweigh a cost it does; no rule for the tie — the tie
falls to the agent's taste, and the property can enter higher unseen; the same tie-break for every
choice — a language, a framework or a store of data already counts how well an agent works with it
through the properties WAY-122 weighs.

### WAY-138 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?

The step that settles technology, at a project definition or at a task (WAY-267), tests the option
it recommends for each choice it settles, one a constraint of the definition or of the task document
settles included, with a devil's advocate, a pre-mortem and a search for unknown unknowns; it tests
no choice a decision of the foundation holds, a choice the step opened being held by no decision,
and no other decision already written is tested afterwards. The risks these tests give are
hypotheses with no source, not differences claimed between options, so the critique of the
comparison does not strike them, and they stand in the message beside the option recommended before
the human chooses. The human who chooses that option takes its risks, and each risk taken reaches
the decision of that choice in its *Rationale*, beside the lacks of the option chosen, marked as a
hypothesis, through the task document where the step ran at a task.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-122 · derives from
  WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: a project settles its store of data and its place to run, the message puts beside each
    option recommended the risks the three tests gave, each marked as a hypothesis, and the human
    who takes the recommended host finds those risks in the *Rationale* of its decision beside its
    lacks; a framework the definition names as a constraint is tested; a language a decision of the
    foundation holds is not; a run at a task tests a service the task document names as a
    constraint, and a way of logging in the step opened though a decision held it, each risk taken
    standing in the task document until the cycle writes the decision;
  - violates: the critique strikes a risk from the message for want of a source; the risks are shown
    only after the human has chosen; every option of a choice is tested; an agent tests a decision
    written before the project and adds risks to it; a risk taken reaches the decision's *Based on*
    as a fact.
- **Origin:** none

*Rationale:* the critique checks that a comparison is true, not what choosing an option sets off; a
risk of the option recommended — a plan with no backup of the data, a framework whose next major
version drops the driver of the store of data chosen, a service whose free tier ends below the
traffic the project expects — comes to light only when someone asks what the choice could break.
Such a risk has no source yet, so the human weighs it as a hypothesis and takes it knowingly,
instead of the critique striking it as an unsupported claim or the agent dropping it. Shown before
the choice, a risk can still change it; carried into the decision as a hypothesis, it tells a later
reader what was accepted without passing for a sourced fact. The tests run on the option
recommended, the one the human most often takes, and only where this project or task chooses: a
choice a decision already holds has been made, and testing it again would reopen it with no reason
in the work, while a choice the step opens has that reason and is chosen anew. The step takes the
three tests from lesson m1l5 of the 10xDevs course, on deploying a product with an agent, which
runs them on the platform its research recommends against the confirmation bias of a model: a
devil's advocate looking for the flaws, hidden costs and risks of the winning option, a pre-mortem
telling how the choice failed three months later, and a search for the classes of risk the scoring
missed, each test ending in accepting the risk, recording it as a known limitation or changing the
choice. The lessons of the course are not open to a reader of this repository.
*Rejected:* tests on every option of a choice — their cost grows with options the human mostly does
not take; the risks shown after the choice — the human takes them unseen; the risks put through the
critique as claims — with no source, every one would be struck; the risks in *Based on* — it names
facts with sources, and a risk read there passes for one; an entry of its own for each risk —
assumptions as a kind of entry escape checking (WAY-04); tests on choices decisions of the
foundation hold — they reopen what was settled; a risk taken recorded as a known limitation in a
document of the product's infrastructure, left out of what the step takes from the lesson — such a
document answers no question, and the decision of the choice carries it and its reasons; the
comparison of three alternatives in a table, which the lesson adds beside the three tests, left out
of what the step takes from the lesson — the step already compares the options of each choice, and
its decision keeps those not chosen in *Rejected*; the change of roles, in which a model weighs the
choice as each of several people who will live with it, which the lesson adds beside the three
tests, left out of what the step takes from the lesson — no decision of the-way has several roles on
its other side.

### WAY-267 — How does the step that settles technology run outside a project definition?

Besides its run at a project definition, the step that settles technology runs at a task document,
with a note saying what the run is for, and a run with no task document starts by creating one
through `refine-task`. A run at a task settles what the note and the task name, looks at the matters
of an agent's way to the running product only where the note touches them, does the rest of its work
as a run at a definition does and ends back in the task's refinement, with no readiness gate; a
human may run it for any choice save one a projected decision of an approved definition settles,
which no run reopens, and the step opens a choice a decision of the foundation holds where it sees
a reason to change the decision (WAY-313), the result then being a change of that decision. The run
writes each settled choice into the task document, with the options not chosen, the source of each
difference claimed between the options, the lacks of the option chosen and the risks the human took
with it, and the task's cycle writes the decision with the code that uses it.

- **Scope:** project-level, task-cycle, decisions
- **Based on:** none
- **Relations:** derives from WAY-01 · derives from WAY-30 · derives from WAY-106 ·
  derives from WAY-121 · derives from WAY-134
- **Verification:** an agent compares the run and the task document with the decision:
  - complies: a human runs the step at a task with the note "where the product's error reports go";
    the run compares the options with their sources, tests the option it recommends and shows the
    message, the task document then holds the answer with the options not chosen, their sources, the
    lacks and the risks, and the decision enters the log in the merge of the code that uses it; a
    note that comes with no task document starts `refine-task`, which creates the document; a human
    names in the note a way of logging in that a decision holds, or the step sees a reason to change
    it and shows it open with the reason, and the result stands in the task document as a change of
    that decision; a run whose note speaks of a store of data, at a task
    that brings a first screen, lists nothing on how an agent reaches that screen; in a refinement a
    project orchestrator leads, the refiner asks for the run through its conversation file, the
    orchestrator dispatches the run's agents and the message goes in the round package;
  - violates: a run writes the option chosen into the decision log before its code exists; a run
    changes an approved definition or reopens a choice one of its projected decisions settles; a run
    leaves a choice a decision holds out of its list for want of the human's word, though it sees a
    reason to change the decision; a run adds the logs, the interface, the development data or the
    place of the screenshots to its list though the note does not touch them; the comparison stands
    only in a report the task document does not hold.
- **Origin:** none

*Rationale:* a task can need a technology choice that no definition settles, and an independent task
has no definition at all, so the step needs a place every such choice has: a task document, which
the human accepts whole and which goes with the task if the work is dropped. Written into the log
before its code, the choice would describe what the product does not hold (WAY-01); kept in the task
document, it reaches the log as every settlement does (WAY-134), and an approved definition stays
untouched, so no gate returns (WAY-118). The price is that even a small choice takes a task document,
a choice with no code takes a full cycle, and the document has to hold the comparison and its
sources, since what a run keeps elsewhere does not last with the task. Settling only what the note
and the task name keeps a task about something else from growing by choices nobody asked for, at the
price that an independent task bringing a first screen gets no answer on how an agent reaches it
unless the note asks, and its agent improvises. A decision held is material of the step before the cycle
starts (WAY-313), so the step opens it where it sees a reason; a change of a decision is the human's
(WAY-14, WAY-30), and the human's choice among the options, the present answer of the decision among
them, is the consent (WAY-314), while going through the step gives that change research and a
critique. The price is that a decision held is no longer final in refinement and a hurried run
could open further ones, which the list shown to the human, with the reason beside each item it
opens, lets the human strike.
*Rejected:* the choice written into the decision log at once, in a request of its own with no task —
it goes against WAY-01: the log would describe what the product does not yet hold, and dropped work
would leave the entry false; the choice written into the approved definition — one choice means the
readiness gate and the check of the plan again (WAY-118), and an independent task has no
definition, so a second way would be needed anyway; the note and the matters of an agent's way to
the running product together, where a task brings something a user sees — a task about something
else can gain up to four further choices, each with research and a critique, close to the question
in the refinement of every task that WAY-121 rejects; a run limited to what nothing holds — a simpler
rule, but a change of technology would go through ordinary refinement with no research or critique,
and a choice of where a product's logs go could not pass through the step.

### WAY-268 — Who settles a technology choice that no decision or definition settles?

A technology choice whose later settling could change how the work is cut into tasks, or that adds
something the product has to run, pay for or back up, and that no decision of the foundation, no
approved definition the task carries and no accepted answer of its task document settles, is a
reserved choice: the human settles it at the step that settles technology (WAY-267), so that it
rests on a source that can be checked rather than on a model's memory, and in the area of these
choices this decision prevails over WAY-114, under which an agent writes an entry on its own
recommendation for the human to accept at the merge. Refinement that sees a reserved choice runs
that step at the task, which is not ready until the human has settled it; in a task's cycle no agent
settles one, its orchestrator included: the agent that meets it returns a report with no code and
the status `reserved`, the attempt is discarded, the cycle opens a blocked draft request naming the
choice and the task returns to refinement (WAY-269). Every other choice stays in the cycle, made by
the agent that meets it and entered in the cycle record's questions table, and the tools the skills
of guidelines choose stay on those skills' routes; whether a choice falls under this rule rests on
the agent's judgment, helped by the examples of `project-level/technology/reserved_choices.md`.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-121 · derives from WAY-227 ·
  narrows WAY-114
- **Verification:** an agent compares the refinement, the cycle and its request with the decision:
  - complies: a task whose outcome needs a store of data or an error tracker nothing settles runs
    the step while it is refined and reads `waiting for human` until the human settles it; an
    executor whose slice needs a framework nothing settles returns a report with no code, the
    attempt goes with the slices already made, and a blocked draft request names the choice; a
    small library for formatting dates, a test double used only by tests and an override of one
    dependency stay with the task and enter the questions table; a source of icons that adds no fee
    and that one task can change alone stays with the task, and one that adds something to pay for
    stops it; a missing way to the running product alone stops no cycle; a new linter
    stays on the route of the coding-guidelines skill;
  - violates: an orchestrator picks a database as the smallest reversible reading and the cycle goes
    on; the human first sees a way of logging in in the request, with code standing on it; a small
    library stops a cycle; a new linter is sent to the step that settles technology; a choice an
    agent cannot place stops the cycle as a third kind, on doubt alone.
- **Origin:** none

*Rationale:* a technology choice the human first sees in the request has code standing on it, so
changing it means reworking what is written, while the choice decides what the product has to keep.
The test that puts a choice on a project's list (WAY-121) also marks what one task does not settle
alone: a choice one task can make and change alone costs little to turn back, and stopping for it
would cost a cycle, research, a critique and a message for the human. The rule takes from lesson
m2l4 of the 10xDevs course one thing, for these choices: a technical decision that rests on a source
that can be checked, not on a model's memory; the lessons of the course are not open to a reader of
this repository. A run of the step gives a choice that source, with a
critique and tests of its risks. The request is the cycle's point of human review (WAY-227), so a
choice met in the cycle leaves it through a blocked draft request and reaches the human in
refinement, where the step can run. Without the precedence, a cycle meeting such a choice would face
this decision and WAY-114 with nothing to choose between them (WAY-25). The price is that a small
library still comes from a model's memory; that the boundary rests on an agent's judgment, so a
doubtful choice judged not under the rule reaches the human in the request with code on it; that a
choice met late in a planned task costs the slices already made, and refinement can miss one; and
that the tools of guidelines keep a route with no tests of risks (WAY-138).
*Rejected:* every new element of the stack, the smallest dependency included — every small library
is a stopped cycle with research, a critique, tests of risks and a message for the human, and
WAY-121 would have to narrow, since it leaves such choices to the task; the same rule with each new
dependency also listed on a line of its own in the request — one more line in the request, an
agent's mistake seen only there with the code standing, and one more rule for a problem nobody has
recorded; the work going on in the same request, with the step's result as a remark on it — the
choice lands in a comment and not in the task document, the frozen copy of the task parts from what
the cycle does, and a new mechanism is needed; a pause in the cycle with a question to the human — it
goes against WAY-227, which would have to change, and the cycle would stop working unattended; the
tools of the skills of guidelines sent to the step as well — one way for every choice, but those
skills and the decisions on their routes
would have to change, and a task choosing several tools at once takes a longer way, with no recorded
case of the present route failing; a search engine built for agents, which the lesson reaches
through a tool server, as the way to the source, left out of what the rule takes from the lesson —
it is a choice of a provider of search, not a step of the process; the current documentation of a
library put into the agent's context before the plan, as the lesson does with a tool for it, left
out of what the rule takes from the lesson — an agent fetches the documentation when it needs it,
rather than all of it ahead.

### WAY-269 — How does a task leave a cycle that met a reserved choice, and how does it come back?

A cycle that meets a reserved choice before its request opens ends with its attempt discarded, its
task branch holding, above its base or the commit that moved the pin, only the commit that adds its
record and the commit that removes it, and a draft request marked `blocked` that names the choice,
says what did not run and why, and settles nothing; one that meets it in a correction takes back
only that correction's commits and returns the request to draft marked `blocked`. Once the human
closes the request, the task returns to refinement with its accepted answers and rows, the named
choice being the note of a run of the step that settles technology (WAY-267), and a new cycle starts
only after the human accepts the whole changed document, on a new branch and, for a task of a
project plan, under the same name. For a task of a project plan, on the human's word, the project
orchestrator removes by name that one cycle's worktree or working directory, its local branch, its
branch on the host and that branch's remote-tracking ref, and then moves the plan's row back to
`to refine`, with a line in the plan's log of changes naming the request.

- **Scope:** project-level, task-cycle
- **Based on:** github-closed-pull-request-branch
- **Relations:** derives from WAY-147 · derives from WAY-153 · derives from WAY-227 ·
  derives from WAY-268
- **Verification:** an agent compares the cycle, its request and the plan with the decision:
  - complies: the task branch goes back to its base, or to the commit that moved the pin, the commit
    that adds the record is pushed and the draft opens on it, and the commit that removes the record
    follows; the request links the record by the commit that adds it, gives the ways seen as not
    researched, and names as not run, with why, the gate and each of the spec, the plan, the
    reviews, the return step and the reconciliation with the target branch that did not run; the
    human closes it, `refine-task` runs with the named choice as its note, and the new cycle starts
    on a new branch, a task of a project plan keeping its name; the project orchestrator, told that
    the task returns to refinement, removes that one cycle's trace by name, and the plan-state
    reader reports no conflict on the row;
  - violates: a remark on the request continues the cycle; an option picked in a remark stands as
    the settled choice; the new cycle reuses the earlier branch; the new cycle of a task of a
    project plan numbers its name; a row moves back with no word from the human; `git fetch --prune`
    takes away the evidence of other tasks' closed requests.
- **Origin:** none

*Rationale:* a discarded attempt leaves no code to show, so what the human needs stands in the
request: the choice in plain words, where it showed and what was searched. The request is where the
human meets the cycle (WAY-227), and closing it hands the choice to refinement, where the step can
run and the human accepts the whole changed document, rather than to a remark that would stand
outside that document. Nothing else runs because nothing is left to check: the tree equals the base
the cycle started from or the commit that moved the pin, so the request holds no finished change for
a gate to run on (WAY-160), and after a correction it is the tree the request already holds. A
plan's task keeps its name in the new cycle because the task and its record meet through it
(WAY-147), and the earlier record never reached the target branch, so the name is free there; a new
branch keeps the discarded commits out of the new request. The earlier cycle's trace goes on the
human's word because a conflicting trace is brought to the human (WAY-153), and left in place it
would show as a conflict at every session, or as a false proposal that the new cycle has
started; it goes by name so that the evidence of other tasks' closed cycles stays. The cost is that
the removal relies on a host that keeps a closed request's commits; where one does not, the earlier
record is lost, while the task document and the request's description still carry what the next step
needs.
*Rejected:* the pair of commits pushed first and the request opened after them, as for other blocked
requests — no new order, but it rests on a host accepting a request with no changes, which no host's
documentation gives; the record left on the branch, with no removal — the request shows it on every
host, but a request merged by mistake would bring a record to the target branch; no request, the stop
reported only in the record or the conversation — the request is where the human meets the cycle's
work; the plan-state reader taught to skip a cycle whose record says it returned — the branch and
worktree could stay, but it stops bringing a conflicting trace to the human, a change to the meaning
of WAY-153; a numbered name for the new cycle of a plan's task — it breaks WAY-147, and the reader
looks for a record under the task's name, so the task could never read as done; the record of a
returned cycle kept elsewhere, out of the reader's sight — the trail to the request is lost, and a
second place for records has to be kept; the earlier branch reused — its history stays in one
place, but only a correction reuses a branch, and the discarded cycle's commits enter the new
request.

### WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?

Where a project runs the product outside the machine on which it is made, which holds unless the
definition or a decision of the foundation keeps the product on that machine, and no decision of the
foundation settles it, the step that settles technology lists how a human learns of a failure of
the running product as a choice of its own, answered by a tool that collects failures, an alert or a
deliberate absence, even where its answer adds nothing to run, pay for or back up; in a run at a task (WAY-267) it enters the list only where the note touches it. No
definition has to hold this choice, the readiness gate does not check it and an approved definition
does not come back to the step for it; it is no matter of an agent's way to the running product, so
whether an agent can read an option is a consequence like any other, and a change to it does not
open the decision on the logs. A deliberate absence always enters the comparison of this choice,
though it has no page of documentation, its consequences anchored in the document and in the pages
of the other options; in the area of this choice this decision prevails over WAY-121, which lists a
choice by its rule of belonging and the four matters of an agent's way alone, and over WAY-122,
which leaves out an option with no documentation.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100 · narrows WAY-121 · narrows WAY-122
- **Verification:** an agent compares the work with the decision:
  - complies: a project that moves a product from the developer's machine to a server, whose
    foundation holds no decision on it, lists how a human learns of a failure as a choice of its
    own beside its place to run; a definition silent on where the product runs lists it; the
    comparison holds an alert and "no tool for now" beside the tools that collect failures, the
    consequences of the absence — the failure learned of from users, and what adding a tool later
    costs — anchored in the definition and in the pages of the other options, and a deliberate
    absence shown to the human as the option recommended is tested like any other recommended option (WAY-138); a service whose panel only a
    human reads is recommended where it wins by consequences, with no lack "an agent does not
    check the running product this way"; the code a tool's hook-up takes shows as what changing the
    choice later costs (WAY-123); a product kept on the developer's machine, and a product whose
    foundation holds a decision on the matter, list nothing, and a definition without the item
    passes the readiness gate;
  - violates: the choice is folded into the logs item; the comparison leaves out the deliberate
    absence for want of a page of documentation; the step passes over an option because an agent
    cannot read its panel (WAY-166); the readiness gate rejects a definition for lacking the item,
    or an approved definition is sent back to the step for it; a product kept on the developer's
    machine gets the item; a run at a task adds the item though its note does not touch it.
- **Origin:** none

*Rationale:* a record good enough to check a change right after a deployment is not good enough to
diagnose a failure from before it, and a human who learns of a failure only from users has chosen
that without knowing it; asking puts the choice before a human who can weigh what it costs. The
criterion is that the product runs outside the machine on which it is made: a product kept on that
machine has no user who meets a failure before its maker, and a first deployment needs a place to
run, a choice that goes through the step whenever nothing settles it, so at a definition the question
comes with it; at a task the deployment skill's check carries it (WAY-139).
A definition silent on where the product runs meets the criterion, because the first project of a
product, whose place to run is not yet chosen, is the case the question exists for; a wrong yes
costs one item answered by a deliberate absence, once for the product, and a wrong no leaves the
question to the check of the deployment skill (WAY-139), which reaches only a task that deploys the
product. An alert built on the logs may come in a table of its own, after the logs are settled. The choice stands apart from the logs and from the matters of an agent's way to the running
product (WAY-165, WAY-166): a change of the tool that collects failures then does not reopen the
decision on the logs, which WAY-121 rejects, and whether an agent reads an option is an ordinary
consequence, since a panel only a human reads can be the right choice here. A deliberate absence
enters every comparison because it costs nothing to run and is a real option, though no page of
documentation describes it and WAY-122 would leave it out. The step keeps its ordinary mechanism — a
fresh agent for the choice, options from documentation with a version, consequences, the simplest
and cheapest option recommended (WAY-122, WAY-123) — with no research skill of its own, so one way
of researching a choice stays to keep current. The step adopts from lesson m3l5 of the 10xDEVS course
two questions, how long the record of the running product lives and how a human learns of a failure;
they bind by this decision, by WAY-165 and by WAY-139, and nowhere else (WAY-100); the lessons of the
course are not open to a reader of this repository. What the code
writes to the record and in what form is a question of the code, not of this step; what a tool's
hook-up takes in code shows as the cost of changing the choice later.
*Rejected:* the matter as part of the logs item — one item fewer, but a change to the tool that
collects failures reopens the whole decision on the logs, which WAY-121 already rejects ("it binds
independent choices together, and a later change to one reopens them all"), and an exception to
WAY-166 is needed; a further matter in the family of an agent's way to the running product — the
existing mechanism and criterion of entry work, but WAY-166 would pass over a panel only a human
reads, so an exception is needed anyway, and the family's definition stops fitting, since the matter
does not speak of an agent checking behaviour; the criterion of the agent's way, that the project
brings behaviour a user sees — it asks also for products kept on one machine; the first user from
outside the team as the criterion — a definition records no such moment, and a product can get
outside users with no new project, so the step does not move and the human learns of a failure from
them; no new criterion, WAY-121's ordinary rule — a deliberate absence adds nothing to run, so the
question is not asked until someone thinks of a tool; a research skill of its own for the matter — the
step already has a mechanism of research, and a second skill would repeat it and drift from it at
each change; the logs and the failure choice added to the step at a task that chooses a place to
run — the question comes in the step with no extra stop, but WAY-267 gains an exception, rules are
needed on an agent opening a decision and on waiting for the place to run, and a product still
needs the human's note; a tool that collects failures set up ahead of the choice, as the lesson sets
one up through its own path of a change, left out of what the step takes from the lesson — the step
chooses the tool, with a deliberate absence among its options; an agent reaching the failures
through the tool's server instead of being given them, left out of what the step takes from the
lesson — how an agent reads the record of the running product is a matter the step already settles
(WAY-121).

## The running product

A product's deployment skill, an agent's way to the running product, and how a product shows its
failures and what its logs hold.

### WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?

The-way holds no skill of a product, but the list of what a product's deployment skill covers: a
preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of
steps and what happens to the data; what the agent does and what the human does; how to read the
logs; how long the record lives, between deployments too; and how a human learns of a failure.
Beside the list it holds a guide to writing such a skill, with the deployment skill of loop2 as its
first example, which binds nothing and which the check of the list points to. When a task's outcome
deploys the product or changes how or where it runs, the-way's skill `refine-task` checks, while it
refines the task, that the product has a deployment skill covering every item of the list, and where
it has none or an item is missing, the task gains an item of its To do for that work or the human
splits that work into a task of its own, and that item and that task point to the guide, which an
agent reads only when it writes or completes a deployment skill; for the items on how to read the
logs, on the record's life and on a failure, the check quotes the answer a decision of the foundation or an
approved definition the task carries already gives, and the task gains the item that writes it into
the skill, a decision silent on how an agent reads the logs or on how long the record lives
answering nothing for the item on that; where nothing answers the item on how to read the logs, it
goes as the other items of the list do, and where nothing answers the item on the record's life or
on a failure, the check asks the human whether to run the step that settles technology at the task
(WAY-267), with a note on what the skill leaves unsaid, instead of filling the item in, and a skill
that records the human's refusal covers the item, so the question does not return; each item of the
To do that writes into the skill the answer to one of these three, or the record of the human's
refusal, points to the guide too.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-267 · derives from WAY-270 · derives from WAY-165 · derives from
  WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: refining a task that moves the product to another host finds that the product's
    deployment skill says nothing of rollback, and the task gains an item of its To do that adds
    it; a task that sets up the product's first deployment finds no deployment skill, and the human
    splits writing one into a task of its own; a task that moves the product to a server, whose
    deployment skill says nothing of how long the record lives, finds that a decision of the
    foundation already answers it, quotes the decision and asks nothing, and the task gains the
    item that writes the answer into the skill; a task that moves the product to a server, whose
    deployment skill says nothing of how to read the logs, finds that the decision on the product's
    logs says how an agent reads them, quotes it and asks nothing, and the task gains the item that
    writes the answer into the skill; the same task, with a logs decision silent on how an agent
    reads them, treats the item as any other of the list, so that the task gains an item of its To
    do for it or the human splits that work off; the same task, with no decision or approved
    definition answering how a human learns of a failure, asks the human once whether to run the
    step that settles technology at the task, and a refusal is recorded in the skill, which then
    covers the item at every later deployment; a task that changes the text of a page is refined
    without the check; the item that a check adds for a missing deployment skill points to the guide,
    and the agent that writes the skill reads the guide, with its parts of loop2 marked as that
    product's own, while the refinement of a task that deploys nothing does not read it; the item
    that writes into the skill the answer a decision gives for how a human learns of a failure, or
    the record of the human's refusal to settle it, points to the guide as well;
  - violates: the-way carries a deployment skill for one kind of host; the check fills in how a
    human learns of a failure with no choice of the human's and no entry that answers it; the check
    quotes a logs decision silent on how an agent reads the logs as the answer to the item on
    reading them, or asks the human whether to run the step for that item; the
    question returns at each later deployment after a refusal recorded in the skill; a task that changes where
    the product runs reaches its cycle with a deployment skill that does not say where the secrets
    lie, and with no item or task for it; the list stands only in a template, and the decision
    points to it; an item that writes into the skill the answer for how to read the logs, how long
    the record lives or how a human learns of a failure names no guide; the guide stands as a skill
    that a product applies as it is, or as a condition that a skill must meet to cover an item; the
    refinement of every task reads the guide; the guide
    carries the public address of the product it shows, or the address of its sender's mailbox in
    its maker's domain.
- **Origin:** none

*Rationale:* how a product is deployed and operated depends on where and how it runs, which differs
from product to product, so a skill of the-way would fit none of them; what such a skill has to
answer is the same for every product, and a list in a binding sentence gives the refinement a thing
to check. Knowledge of operating a product written in a document no step reads goes unread however
concrete it is, while a skill of the product reaches the agent when it prepares a deployment. The
check comes when a task first needs that knowledge, so the first task that deploys a product grows
by its deployment skill, unless the human splits that work off. The record's life and the way a
human learns of a failure are two items of the list because a skill that says only where the logs
are leaves a product whose record dies with each deployment, and whose maker learns of a failure
from its users, looking complete; the choice stays the human's, so the check asks the human before
the step runs and does not fill the item in, and where an entry already holds the answer the human
meets it as a quotation in the task document. How to read the logs is answered once for the product
by its decision on the logs (WAY-165), which says how an agent reads them, and the skill repeats
that answer, so that the two do not give an agent different instructions; where no decision answers
it, the item stays an ordinary item of the list. The price is that the skill keeps the text of the
decision, so a change of the decision is followed by a rewrite of the skill. The step's own look at the logs stays as it is
(WAY-121): this list reaches a product whose definition is already approved, when a task deploys it.
The list says what a skill covers, not what an answer to each item looks like, and the one skill
that exists describes a particular server, so whoever takes it as a pattern separates the general
from the particular alone; a guide that shows that skill part by part, with what belongs to the
product marked as its own, does it once. Only the agent that writes or completes a deployment skill
reads the guide, so the refinement of every other task reads nothing more, and since it binds
nothing, the list and the check stay what decides whether an item is covered. The price is that the
guide shows the product's skill as it stood at one commit and ages as that skill changes, and that
it shows no real address, since the repository is public; fragments of one commit with a link to it
need no change until someone chooses to show a newer one. The guide has a part for each of the three
items the check handles apart, so the item of the To do that writes into the skill the answer to one
of them points to the guide as well: an agent that is given only that item, with no pointer, reads
the one skill that exists as its pattern and separates the general from the particular alone. The
price is one more place that names the guide. The list takes from lesson m1l5 of the 10xDevs course,
on deploying a product with an agent, the parts of the document of the infrastructure the lesson
has an agent keep beside the product that say how it is operated — the preview of deployments, where
the secrets lie, how a faulty deployment is rolled back and in how many steps,
which actions take a human, and how the agent reaches the logs — and from lesson m3l5 its two items
on the record's life and on a failure (WAY-270); the lessons of the course are not open to a reader
of this repository.
*Rejected:* the pointer on the item that adds a missing deployment skill alone, the items that write
the answer to one of the three left without one — the agent that completes a skill for one of them
may not find the guide; the skill saying how a human reads the logs and the decision how an agent
reads them —
two answers that are usually the same and can drift apart; the item on how to read the logs left as
it was — the drift shows only when an agent meets two different instructions; a deployment skill
carried by the-way — what to run and where differs for every
product; a document of operations kept beside the product, as the lesson's document of the
infrastructure is — no step reads it, so it goes stale unread; the platform chosen and its reasons,
which that document holds, left out of what the list takes from the lesson — the decisions of the
foundation carry a choice and its reasons; the fit of the product's stack to the platform, which
that document holds — left out of what the list takes from the lesson; the known risks, which that
document holds — left out of what the list takes from the lesson; the region, the runtime and the
plan paid for, which that document holds — left out of what the list takes from the lesson; the
signal that would change the choice once the product grows, which that document holds — left out of
what the list takes from the lesson; the list in a template alone — nothing binds the refinement to check it; adding the logs
and the failure choice to the step at a task that chooses a place to run — the question comes in
the step with no extra stop, but WAY-267 gains an exception, rules are needed on an agent opening a
decision and on waiting for the place to run, and a product still needs the human's note; the
question at every later deployment after a refusal — one question each time, and an exception to
this decision; the text of the guide written into the step that checks the list — every
refinement of every task reads a long text, also those that deploy nothing, and the binding rule
mixes with an example; a directory of its own, a new part of the-way — it changes the decision on
what the repository holds and the map of its parts, and gains the reader nothing, since only the
check leads to the guide; no guide — the list and a reader's own reworking of the one skill that
exists, which costs nothing today and is paid by the next product deployed; the whole skill of loop2
copied with its comments — the public address of the game and the sender's mailbox address in its
author's domain would enter a public repository, and the copy would age; a frame of questions and a
link, with no fragments — the reader opens loop2 and separates the general from the particular
alone, as today.

### WAY-165 — What must an answer to each matter of an agent's way to the running product settle?

Of the matters of an agent's way to the running product, the logs ask where the record of what the
running product does goes, how long that record lives, between deployments too, and how an agent
reads it, and the interface asks how an agent operates the product as its user does — through a
screen in a browser, a call to its API or a command in a terminal — and how it sees what the
product answers. The development data asks where the data comes from on which an agent checks the
product's behaviour outside production, and how an agent brings that data to the state a check
needs, and the place of the screenshots asks where the files of the screenshots that an agent takes
to show the human lie, outside the product's repository, and how the description of a request shows
each as an image. Data set up from scratch and a dedicated test environment that persists are
examples of options of the development data, none of them ruled out, and an entry, a decision of
the foundation or a projected decision of a definition, that leaves part of what a matter asks unanswered does not settle that matter at a
project definition; in a run at a task (WAY-267) the step may open a decision of the foundation that
leaves part of it unanswered as it may open any such decision (WAY-313), the list shown to the
human saying in one sentence what that decision leaves unsaid.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-270 · derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: for a game played in a browser, the logs are answered by an agent reading the output
    of the server's container, kept in a store that outlives a redeployment, the interface by an
    agent playing the game in a browser on a local address and reading what the page shows, and the
    development data by a script that sets up test accounts with a fresh save, a save from the
    middle of a game and a password reset waiting; for a shop with a large store of data, the
    comparison of its development data weighs data a script generates, a copy of production without
    personal data that a human fetches, and a dedicated test environment that persists, each by its
    consequences; the place of the screenshots is answered by a store outside the product's
    repository to which an agent can write a file and which serves each file at an address that the
    description of a request embeds as an image; a list written before the record's life was asked,
    whose logs item stands
    `— held by` a decision silent on it, has the item end `— open` with that decision nested under
    it, and the list is shown again with one sentence on what the decision leaves unsaid; in a run
    at a task, the item over such a decision ends `— open` with that decision nested under it
    where the step opens it, and the list shown to the human says in one sentence what the decision
    leaves unsaid;
  - violates: the interface is answered by an agent reading the store of data past the
    application; the logs are answered by where the record goes and how an agent reads it, with
    nothing said of whether it outlives a redeployment, and the answer stands as settling the
    matter; a logs item of a definition's list stays `— held by` or `— projected` on a decision
    silent on the record's life; an agent waits, in a run at a task, for a word of the human before
    it opens a logs decision silent on the record's life; an approved definition is sent back to the
    step because its logs decision is silent on it; the development data names where the data comes
    from but not how an agent reaches a save from the middle of a game; the comparison of the
    development data leaves out a dedicated test environment that persists because the data has to
    be set up from scratch; the place of the screenshots is answered by a directory of the product's
    repository, or names where the files lie and says nothing of how the description of a request
    shows them as images, and the answer stands as settling the matter; in a run at a task, the list
    shown to the human has the item over such a decision with no word of what the decision leaves
    unsaid.
- **Origin:** none

*Rationale:* each answer serves an agent that checks behaviour a user sees in the running product.
The logs tell the agent what the product did, and the answer says where that record lands and how
long it lives, since an agent reads only what it can reach: a record that dies with each deployment
serves a check made right after one and no diagnosis of a failure from before it (WAY-270). An entry
that answers part of what a matter asks leaves the rest to be improvised in the cycle, so it settles
nothing at a definition, whether its answer is good or not; at a task the step may open
such a decision as it may open any decision before the cycle starts (WAY-313), the silence being
reason enough, and the human's choice among the options, the decision's present answer among them,
is the consent to the change (WAY-314). The word is "may" on purpose, as in WAY-313: the step is
not made to add an item over every silent decision, which would grow the list of every run at a
task that touches a matter, and the list still says in one sentence what the decision leaves
unsaid, so that the human can open the item. Operating the product as its user does lets
the check see what a user sees, while reading the store of data past the application shows a state
no user meets and skips the code in between. A check needs the data in a given state, so the answer
says both where the data comes from and how the agent brings it to that state; otherwise the agent of the
cycle improvises it. A dedicated test environment that persists is in many cases better than data
set up from scratch for every change, though it brings costs of its own, so neither is ruled out;
the options of a run are those its research finds (WAY-122), and the step weighs them by their
consequences (WAY-123). In a run at a task the list shown to the
human says in one sentence what a silent decision leaves unsaid, since an item that reads as
settled gives the human no sign that something is left for them to say. The screenshots an agent
takes to show the human are the evidence of its check, and the human sees them in the description
of the request, so the answer says both where the files lie, outside the product's repository where
a file would stay in its history for good (WAY-316), and how the description shows them; a place
without the second leaves each cycle to improvise how a screenshot reaches the human. The question
of how long the record lives comes from lesson m3l5 of the 10xDEVS course, on debugging with an
agent, which weighs how long a platform keeps its logs (WAY-270); the lessons of the course are not
open to a reader of this repository.
*Rejected:* the interface without "as its user does" — access to the store of data past the
application would count as an interface; the development data asked as data rebuilt from scratch —
it rules out a dedicated test environment that persists, in many cases the better option; the
development data with no word on reaching a state — a decision could leave unsaid the state a check
needs, and the agent of the cycle improvises it; what the product logs and in what form, in the
same decision, the identifiers that tie the events of one operation among the lesson's sources of a
diagnosis included — that rule acts where code is written and reviewed, in the task cycle, not where
a project settles its technology; the technical and business metrics that the lesson counts among
the sources of a diagnosis — left out of what the matter takes from the lesson; the history of
changes and deployments that the lesson counts among those sources — left out of what the matter
takes from the lesson.

### WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?

In a choice of an agent's way to the running product, whether an agent can use an option is a
consequence for the product: an option an agent cannot use stays in the comparison with that lack
said as "an agent does not check the running product this way", and the recommendation passes over
it. Where no option can be used by an agent, the recommendation goes by the other consequences and
says in one sentence that no option lets an agent check the running product this way, so the check
stays with the human.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · narrows WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: a log service cheaper than the others, whose logs only a human can read, in a panel
    behind the human's login, stays in the comparison of the logs with the lack "an agent does not
    check the running product this way", and the step recommends reading the output of the
    server's container, kept in a store that outlives a redeployment; a host whose every option for
    the logs is a panel behind the human's login has the options compared by their cost and upkeep,
    the one that wins recommended, and the message says in one sentence that no option lets an agent
    check the running product this way, so the check stays with the human;
  - violates: the step recommends the cheaper service because how well an agent works with an
    option decides only a tie; the service is left out of the comparison because an agent cannot
    read its logs; the message shows the service with no word on whether an agent can use it; on a
    host where no option can be used by an agent, the step recommends nothing, or recommends by
    cost and upkeep with no word that the check stays with the human.
- **Origin:** none

*Rationale:* a choice of an agent's way to the running product exists so that an agent can check
what a user sees in the running product; an option the agent cannot use leaves that check undone,
and the product's behaviour reaches the human unchecked, which is a consequence the product bears
rather than the agent's convenience. Kept in the comparison with its lack, the option stays open to
the human, who chooses between consequences (WAY-123). Where every option is one an agent cannot
use, passing over them all would leave the step with nothing to recommend, though the human is owed
a recommendation (WAY-113); the step recommends by the other consequences and says in one sentence
that the check stays with the human, so that the lack reaches the human at the choice. The price is
that the step does not look again for an option an agent can use: the lack comes out before the
choice, and the human answers it. For a place to run, how well an agent works
with an option still decides only a tie (WAY-137): there the agent's convenience is not what the
product needs from the choice, while here the agent's use of an option is what the choice is for.
*Rejected:* nothing added to the usual weighing of consequences — the step could recommend a
cheaper service an agent cannot use, since how well an agent works with an option decides only a
tie, and the choice would pass with an answer that gives the agent nothing; the step looking
further first for an option an agent can use, such as sending the logs to a place an agent reads,
and going the way chosen only when that yields nothing — a longer research on every such matter,
often one more service to pay for, while the options already come from research (WAY-122); the step
recommending nothing where no option can be used by an agent — an exception to WAY-113, and the
human answers with no hint; the case left unsaid — it shows at the first product with such hosting,
and each agent resolves it in its own way.

### WAY-273 — May a product hide a failure?

The template of the coding discipline holds that a failure is not hidden: code turns it neither into
an "all fine" answer nor into an empty list. A degraded mode, in which the product goes on without
one function, is allowed only where a task sets it, recording it as a decision of the product, and it
always leaves a line in the logs.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** an agent compares the template with the decision:
  - complies: the rule has a list whose source failed answer with a failure, not with no items; it
    lets a page show without its recommendations where a task set that as a decision of the product,
    with a line in the logs each time;
  - violates: the rule lets code catch an error and answer as if all went well; it lets an agent add
    a degraded mode of its own accord; it lets a degraded mode leave no line.
- **Origin:** none

*Rationale:* the-way takes this one rule from lesson m3l5 of the 10xDEVS course, because the cause of
a failure nobody sees cannot be found; the lesson says that one first stops hiding what happens in
the system and only then fixes the cause. The lessons of the course are not open to a reader of this
repository. An empty list after a failure reads as a true answer, so
neither a user nor an agent has anything to act on. A degraded mode can serve a user better than a
page that falls with one of its functions, so it is allowed; set by a task and recorded as a decision
it is known later to be deliberate, and its line keeps it from being a hidden failure. Its weak
point: it leaves a line while the user sees a working page, so nobody learns of it unless someone
reads the logs, and how a human learns of a failure stays with the step that settles technology
(WAY-270).
*Rejected:* the rule taken literally, every error written and none hidden — nothing to judge, but the
logs fill with wrong passwords and repeats, and with a degraded mode forbidden one function going down
takes a whole page with it; each product defining a failure for itself — the definition fits the
product, but it is one more item in its decision, most products write the same one, and audits stop
being comparable; the search for hidden failures as a class, by an audit of one critical flow run
before a user reports them, as the lesson sets it — left out of what the template takes from the
lesson.

### WAY-274 — Where does a product's logging scope stand, and who adds to it?

The principle of a product's logging scope stands in the product's decision on the rules on failures
and logs, and the list of today of the identifiers and business events it logs, at adoption from what
the product has in its code or in its plan, stands in a rule of its guidelines, as the product's
promise and no inventory of its code. An agent adds an item that fits the principle, any identifier
of a thing included, in the change that brings it, and the human sees it at the merge. Whatever
points to a person, an email, a name, a telephone number, a home address and an IP address among
them, takes the human's consent, and the number the product gives a user is settled by the human when
the list is accepted and takes that consent if added later.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-172 · derives from WAY-225
- **Verification:** an agent compares the change with the decision:
  - complies: a change that brings refunds adds the refund's identifier and the event of a refund to
    the list in the same change, and no cycle stops for it; a change that wants the email of a user
    in its lines stops for the human's consent; the list names a business event the product has in
    its plan and no code writes yet;
  - violates: the list stands in the product's decision, so that each item changes it; an agent adds
    an IP address as one more identifier; an agent adds the number the product gives a user with no
    consent because it means nothing outside the product; the list is regenerated from the code.
- **Origin:** none

*Rationale:* a principle with a list lets the human see what the product logs while new items keep
coming with every function and stop no cycle. The list stands in a rule, so adding an item changes no
decision (WAY-30), and the principle and the boundary, which are choices, stand in the decision. What
the product promises to log is what code cannot show (WAY-225), so the list is written by hand and a
gap between it and the code is a finding, not a reason to copy the code. The boundary is drawn at
persons, since an identifier of a thing costs nothing to add and stopping for it would hold up a cycle
for nothing. Its weak points: a list written by hand can drift from the code; an agent judges whether
an item fits the principle and whether a number points to a person, and the number of an order can be
tied to a person through the product's data; a reviewer has to watch that an added item keeps the
boundary; and the list does not stand among the entries searched when the foundation changes.
*Rejected:* the list alone — the human sees each item, but each new one changes the decision and goes
through the guidelines skill, and one that shows only in a cycle stops it for the human, while new
events come with every function; the principle alone — a new item takes no consent and stops no
cycle, but the human does not see the list, the reviewer judges everything by reading, and which
identifiers are meant keeps changing; literally no personal data — the simplest wording, but it rules
out a user's number, so one user's actions cannot be followed over time; only what the list names of
a person's data, with the agent adding to the list alone — the contradiction goes with no further
rule, but the agent could add an email too and the rule would protect nothing; the boundary taken
literally, only a number given inside the product — the sharpest, and the agent judges almost
nothing, but the number of a transaction or an order stops the cycle for the human; the list in the
decision with nothing further written — the choice of a principle with a list stays as it is, but the
dispute over changing a decision stays and two cycles can settle it differently; the list in the
decision with a new decision of the-way narrowing WAY-30 — the list stays among the decisions and the
precedence is written, but it is a standing exception to the rule that a decision does not change
without the human's approval.

### WAY-276 — What do a product's logs not hold?

The template of the coding discipline holds that the logs hold no secret, and no personal data, the
identifiers on the list of the product's logging scope being an exception to this second ban alone,
and no whole object or request body, which does not touch the error itself. Where an original error
quotes such values this rule prevails over the rule that a failure is written with its original
error, and the error is written without them, with its kind, code and place in the code; an
identifier on that list that is a secret stays out of a line, this rule prevailing over the rule
that a line of a case flow carries the identifiers the logging scope lists. The ban on personal data
is the template's choice and no
restatement of law, so a product may depart from that ban with a reason, the rest of the rule
standing and the law binding the product regardless.

- **Scope:** product-guidelines
- **Based on:** General Data Protection Regulation, https://gdpr-info.eu/art-4-gdpr/ § Article 4(1) —
  "in particular by reference to an identifier such as a name, an identification number, location
  data, an online identifier"; read 2026-11-01 · https://gdpr-info.eu/recitals/no-26/ § Recital 26 —
  "by the use of additional information should be considered to be information on an identifiable
  natural person."; read 2026-11-01 · https://gdpr-info.eu/art-5-gdpr/ § Article 5(1)(c) — "adequate,
  relevant and limited to what is necessary in relation to the purposes for which they are
  processed"; read 2026-11-01
- **Relations:** none
- **Verification:** an agent compares the template with the decision:
  - complies: the rule lets the number of a user stand in a line where the list names it, and keeps
    out an access token that stands on the list as an identifier; a database error that quotes a
    customer's email is written with its kind, code and place; a product departs from the ban on
    personal data and keeps the ban on secrets;
  - violates: the rule lets the list except a secret; it bans the error itself with the request
    bodies; it lets the original error win over the ban; it presents the ban on personal data as what
    the law requires.
- **Origin:** none

*Rationale:* a line outlives the request that wrote it and reaches whoever reads the logs, so a
secret in it is a leak, and a whole object or a request body brings in values nobody chose to write.
Without the exception a user's number would have to go, and one user's actions could not be followed
over time. The regulation counts an identification number among what identifies a person, treats
what can be tied to a person by additional information as information on that person, and limits data
to what is necessary; that it does not forbid logging personal data is an agent's reading of it and
no legal opinion, so the ban stands as a choice of the template, which a product may leave for a
reason, and what the law requires of the product stands apart from it. Where an error quotes
such values, its kind, code and place keep enough of the cause. Its weak points: a reviewer sees code
and not what an error holds at run time, so an unusual leak can pass, and whether a user's number in
the logs is lawful stays the product's to judge.
*Rejected:* literally no personal data — the simplest wording, but it rules out a user's number, so
one user's actions cannot be followed over time; only what the list names of a person's data, with
the agent adding to the list alone — the contradiction goes with no further rule, but the agent could
add an email too and the rule would protect nothing; the boundary taken literally, only a number
given inside the product — the sharpest, and the agent judges almost nothing, but the number of a
transaction or an order stops the cycle for the human.

### WAY-319 — What must an agent's way to the running product allow when two task cycles run at once?

The way to the running product that the foundation of a product settles for its interface lets two
task cycles working in separate worktrees of the product check at the same time without a browser
they share, and an agent closes the browser it opened when its check ends.

The condition reaches a product through the step that settles technology, which says for each option
of the interface whether two task cycles working in separate worktrees of the product can check at
the same time without a browser they share, and an option that cannot stays in the comparison with
that lack.

- **Scope:** task-cycle, project-level
- **Based on:** none
- **Relations:** derives from WAY-121
- **Verification:** an agent compares the foundation of a product and a cycle with the decision:
  - complies: a product settles a way in which each worktree drives a browser of its own, two
    cycles check at once, and each author closes its browser at the end of its check; the step that
    settles the interface of a product says of each option whether two cycles can check at once
    without a shared browser, and an option that cannot stays in the comparison with that lack;
  - violates: a way in which the second session started in another worktree takes over the page of
    the first; an author leaves its browser open at the end of its check; a comparison of the
    options of an interface that does not say whether two cycles can check at once.
- **Origin:** none

*Rationale:* two cycles in separate worktrees of one product both look at the running product, and a
way that gives them one browser makes the second check fail or take over the first one's page; an
author that leaves its browser open blocks the next check the same way. Between 20 and 31 October
2026, before one of two products changed its way, 13 errors of a busy browser profile stood in 9
conversation files of the sessions on those two products; the count is this product's own, and the
conversation files are not open to a reader of this repository. Stated once for every way and
carried by the step that settles technology, which keeps an option that fails it in the comparison
with that lack as WAY-166 does for an option an agent cannot use, the condition reaches a product
before it meets the conflict.
*Rejected:* the-way saying nothing, the matter staying with the product — each product finds the
conflict itself, by its errors, and a product whose main way keeps one browser profile for a
directory returns to the busy profile; the condition reaching a product only at the check of the
author — the product still learns of the conflict from the errors of its first two parallel cycles.

## Project plan

What the breakdown of a project writes, how the plan's tasks are named, ordered and run side by
side, how the plan is checked, and how a task's state in it is proven.

### WAY-142 — What does the breakdown of a project write, and in what form?

The breakdown of a project writes its plan as one document beside the approved definition, whose
header names the definition and the fingerprint the definition's gate record holds, and whose
`Status:` line says whether the plan is still a draft or has been handed to the human. Each task
stands in one row of one table of tasks, with the columns and states the plan template gives, while
the tasks that realize each projected entry and the one task that writes it into the foundation
stand in a table of their own, a row for each entry under the heading the definition gives it. The
plan also holds each open question of the definition, word for word, with where it is resolved, its
phases with what closes each where it has any, and a log of its changes, each with its reason,
written in the language of the definition under headings, states and markers kept in English.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-118 · derives from
  WAY-100
- **Verification:** invariants: project-plan-form. For what the plan holds beyond its form, an agent
  compares the plan with the decision:
  - complies: the plan of a Polish definition gives each task's goal in Polish under English
    headings, its header carries the fingerprint the gate recorded, and the projected decision
    `(new) — Who owns a document?` stands in the table of entries with tasks 3 and 5 realizing it
    and task 5 writing it;
  - violates: a task stands in the table and again under a heading of its own repeating its
    fields; the goals of a Polish definition's tasks stand in English; a phase names no condition
    that closes it.
- **Origin:** none

*Rationale:* a plan changes with every move of a task, a definition rarely and only through its
gate, so the two stand apart, and the fingerprint in the plan's header shows when the definition
beneath it has changed. One row per task keeps each fact about a task in one place, where no copy
can drift from it. A definition can project many entries, its decisions named only by their
question; listed in the row of every task that realizes them, they would fill a cell no one reads
and need short keys made up for them, while a row per entry under its own heading is matched to the
definition word for word and shows in one cell the single task that writes it. The columns and the
states stand in the template, so that a change to them needs no change of this decision. The
step takes from the practice of a roadmap of vertical slices the breaking of a project into tasks
before any task is planned. The practice is that of lesson m2l1 of the 10xDevs course, on the
roadmap of a first version of a product, and of the skill of a roadmap the lesson brings, which
opens a milestone from the product's documents, checks that they are ready, takes stock of the code
already in place, asks the human three questions that set the order of the work, and breaks the
milestone into preparatory work and vertical slices, each with a stable name for its change, the
work it needs first and the slices it can run beside. The lessons of the course are not open to a
reader of this repository.
*Rejected:* the realizing and the writing tasks as two columns of the table of tasks — a cell grows
to many long headings and needs keys made up for them; each task described again in a section of
its own beside an index table and a table for a tracker, as the practice of a roadmap holds each of
its items — three copies of one task drift apart; the
plan inside the definition — every move of a task would change approved sections and send the
definition through its gate (WAY-118); a stage of the project opened and closed inside the plan —
the project already opens with its definition and ends once each of its tasks has a final state;
the external
deadline repeated in the plan — the definition holds it; the columns named in this
decision — each change of a column would take a change of the decision; the milestones and the
interview on the order of work of the practice of a roadmap of vertical slices — left out of what
the step takes from it; the practice's scored check that the product's documents are ready before
the breakdown, left out of what the step takes from it — the definition passes its stricter
readiness gate before the breakdown (WAY-118); the practice's stock of the code already in place,
taken layer by layer by agents working side by side — left out of what the step takes from it; the
practice's fields of each item from which its acceptance criteria are drawn, among them a sentence
of why it stands where it does in the order, left out of what the step takes from it — the
refinement of each task writes its acceptance criteria from its own analysis, and the order stands
in the dependencies; the practice's list of parked items, left out of what the step takes from it —
it copies what the definition puts out of scope; the practice's state of an item blocked by an
unknown the human has to resolve, left out of what the step takes from it — the plan has a state of
waiting for the human and places each open question where it is resolved.

### WAY-143 — What does a task of a project plan end with?

A task of a project plan ends with something that can be checked in the running product, never with
a layer of the product put in place; a preparatory task stands in the plan only where a task of the
plan depends on it, the task it opens the way for. A technical element enters the plan with the
first task that uses it, or with a preparatory task that task depends on.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** invariants: project-plan-check. For what a task ends with and where a technical
  element enters, an agent compares the plan with the decision:
  - complies: a task "the player opens the forest and sees it on a grid of hexagons" also brings in
    the first data files of the game; a preparatory task puts the empty application on the test
    server, and the task of player accounts depends on it; in the-way, a task ends with
    a skill a session runs on a real definition;
  - violates: a task "the database schema" ends with tables no screen reads; a preparatory task
    sets up logging for the whole product for later use and no task depends on it; the store of data enters
    in a task before the first task that saves anything.
- **Origin:** none

*Rationale:* a task that ends with a layer in place cannot be checked by anyone using the product,
and its mistakes show only when a later task uses the layer; a task that ends in the running product
shows at its merge whether the project moves. Some work has to come first, such as a server for the
product to run on, and it earns a task of its own only by naming what it opens the way for, so a
later reader sees why it stands there; a technical element brought in early for later use is work
nobody checks until it is needed, and is often built for a need that changes. The rule takes from
the practice of vertical slices the cut by what can be checked in the running product, and from its
enabling work the rule that such work names what it opens the way for. The practice is that of the
skill of a roadmap of lesson m2l1 of the 10xDevs course (WAY-142), whose preparatory work, named
foundations, stands only with what it unlocks — a slice, a blocking unknown it reduces or a way of
verifying it enables; the lessons of the course are not open to a reader of this repository.
*Rejected:* tasks cut by layers of the product — nothing can be checked until the last layer lands;
preparatory work no task depends on — it grows into a layer of its own; a field of the preparatory
task naming the task it opens the way for, as the practice's field of what a foundation unlocks —
it repeats a dependency the plan already holds; the word slice for a task of the plan, which the
practice uses for its items — the word already names a piece of a task's change.

### WAY-144 — How does a project plan show which tasks can be worked on side by side?

The dependencies of a project plan constrain the start of a task's cycle, not its refinement: a
task starts its cycle only when the tasks it depends on are done, while refinement waits for
another task only where a question of that refinement needs its result. Two task cycles can run
side by side when neither task depends on the other, directly or through other tasks. The plan
holds no field naming the tasks a task can be worked on beside, and its order of cycle starts
follows the dependencies.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-100
- **Verification:** invariants: project-plan-form. For cycle starts and refinement waits, an agent
  compares the plan, or the work on it, with the decision:
  - complies: two cycles start together because neither task depends on the other and their
    dependencies are done; two dependent tasks are refined together, with only a question needing
    an unfinished result waiting for its named task; a task needing a saved state lists the task
    that adds saving among those it depends on;
  - violates: a task carries a field naming a dozen tasks it can be worked on beside; tasks are
    ordered by a goal picked in an interview against their dependencies; a task starts its cycle
    before a dependency is done, or refinement waits for every dependency without a question
    requiring those results.
- **Origin:** none

*Rationale:* the dependencies already say which tasks can go together; a second field derived from
them is a copy that drifts as soon as one dependency changes, and its lists grow long enough that
nobody reads them. The rule takes from the practice of a roadmap its graph of dependencies and the
order that follows from it; the practice is that of the skill of a roadmap of lesson m2l1 of the
10xDevs course (WAY-142), whose lessons are not open to a reader of this repository. The task
order WAY-106 gives the plan is this order of cycle starts. Refinement
can settle a dependent task before its prerequisites are delivered; only a question needing their
result earns a wait.
*Rejected:* a field naming the tasks a task can be worked on beside, which the practice of a roadmap
has and the rule leaves out — a copy of the dependencies that grows past reading; the order tilted
by a goal the human picks in an interview before the plan, as the practice of a roadmap tilts it —
the definition already states the goal and its risks, and the human corrects the finished plan;
the practice's slice that proves the product, placed as early as its dependencies allow — left out
of what the rule takes from it.

### WAY-146 — What checks a project plan before it is handed over?

Before a project plan is handed over, a script checks the form it reads the plan by and what the
plan's structure decides: each projected entry of the definition has tasks that realize it, exactly
one of them writing it into the foundation; each item of In scope has a task; no task depends on
itself through others; some task depends on each preparatory task; and each open question of the
definition stands in the plan word for word, with a task of the plan or an answer. The plan's
independent critique then judges, against the definition, what no script tells apart: whether each
task that is not preparatory ends with something checkable in the running product, whether each
technical element enters with the first task that uses it, whether each question stands where the
definition puts it or the log of changes gives its move, and whether a quoted answer settles its
question. A check a script can make is never left to the critique.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-120
- **Verification:** invariants: project-plan-form · project-plan-check. For the critique, an agent
  compares the work with the decision:
  - complies: the critique finds a task ending with tables no screen reads and a question placed in
    another task than the definition names with no line in the log, while the script reports a
    projected decision no task writes;
  - violates: the critique is asked whether every item of In scope has a task; the plan reaches the
    human with a question the script would have found unplaced; the agent that wrote the plan
    judges its own tasks.
- **Origin:** none

*Rationale:* a rule a script can decide holds every time the script runs, while an agent asked the
same thing answers well most of the time and costs a reading of the whole plan; what a script
cannot tell — whether an end can be checked, whether an element came early, whether a question was
moved or answered in full — needs a reader who did not write the plan, since its writer applied the
rules it would be checking. The rule takes from the practice of a roadmap its review of the plan
before it is handed on, split between a script and a reader who did not write the plan; the
practice is that of the skill of a roadmap of lesson m2l1 of the 10xDevs course (WAY-142), whose
lessons are not open to a reader of this repository.
*Rejected:* the author checking its own plan against the rules before writing it, as the practice's
review of its own roadmap does — the same agent applies and judges them; checks of a plan's form
across several copies of each task, as the practice checks that its table and its sections agree —
a plan holding each task once has no copies to compare; an agent checking what a script decides —
it costs more and sometimes misses; the practice's check that no slice stands for anything the
source does not declare — left out of what the rule takes from it; the practice's check that its
slices are of a comparable size — left out of what the rule takes from it.

### WAY-147 — How is a task of a project plan named, and what does its cycle take from the name?

A project plan gives each of its tasks a name of lower-case words joined by hyphens, which no other
task of the plan holds and which stays with the task while the plan changes. A task of the plan
enters its cycle under that name, and the cycle names its record by it.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** invariants: project-plan-form. For the cycle, an agent compares the cycle with
  the decision:
  - complies: the task `forest-on-hex-grid` of a plan names its record directory and its committed
    copy by `forest-on-hex-grid`;
  - violates: the cycle of a task of a plan names its record by a name it makes up; a task's name
    changes when its goal is reworded; a plan carries a second table of its tasks with titles for a
    tracker.
- **Origin:** none

*Rationale:* a task's cycle record and its entry in the product's backlog meet its row in the plan
through its name, so a name that changes leads a reader to the wrong work; words, because a number
that keeps the plan's own cells short says nothing in a record read apart from the plan. The rule
takes from the practice of a roadmap the stable name each of its items carries into later work; the
practice is that of the skill of a roadmap of lesson m2l1 of the 10xDevs course (WAY-142), whose
lessons are not open to a reader of this repository.
Where the product keeps its backlog is its own choice (WAY-107), and a task's entry there links its
document, so the plan needs no table of its tasks written for a tracker.
*Rejected:* the cycle naming its record when it starts — the plan and the record name one task
differently; the plan's number as the name — it says nothing where it is read; a table of the
plan's tasks with titles for a tracker, as the practice of a roadmap hands its items to a backlog —
a second copy of the tasks, which the product's backlog already holds; the practice's states of an
item that the later steps of a change move forward by its name — left out of what the rule takes
from it.

### WAY-153 — What evidence supports a task state in a project plan?

At each leading session's start a reader using git alone proposes plan state transitions only from
evidence that ties a cycle trace to the plan's task, establishes the product's integration ref
without guessing, changes no plan or task document and reports what it cannot establish. The project
orchestrator applies supported transitions with a reason and evidence in the plan's log,
resolves outcomes Git cannot establish through the product's chosen PR tool or asks the human
when that tool is absent, and brings a closed-unmerged PR or a trace conflicting with the plan
to the human without automatically correcting the plan.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-38 · derives from WAY-142 · derives from
  WAY-147
- **Verification:** invariants: project-plan-state-evidence · project-plan-state-subprocesses ·
  blocked-request-wording · blocked-request-label. For applying proposals and resolving PR outcomes,
  an agent compares the evidence and leading session with the decision:
  - complies: the project orchestrator applies supported transitions with a reason and evidence
    in the plan's log, resolves an unchecked PR outcome through the product's chosen PR tool,
    and shows a closed-unmerged PR to the human without automatic correction;
  - violates: the project orchestrator treats an unchecked observation as completion without
    resolving it, silently normalizes a conflicting trace, or guesses the PR outcome when the
    product's PR tool is absent instead of asking the human.
- **Origin:** none

*Rationale:* evidence-backed progress prevents a stale plan from hiding delivered work without letting
an uncertain observation claim delivery. Separating observation from the plan write keeps the
human-facing judgment visible; unresolved host outcomes cost a lookup or a question.
*Rejected:* a state reader that also queries the PR host — it couples observation to a host-specific
executable; inferring completion from a local trace — unfinished or abandoned work looks delivered;
automatically normalizing conflicts — a plausible state hides the discrepancy the human needs.

### WAY-230 — How does a project plan order two tasks that realize the same projected entry?

Two tasks of a project plan that realize the same projected entry go one after the other: one
depends on the other, directly or through other tasks, unless an item of the plan's change log lets
the two go side by side on that entry and gives the reason, and the breakdown shows each such item
to the human when it hands the plan over. The script that checks the plan reports each pair of
tasks realizing the same entry that neither depends on the other and no such item covers, while
neither task is done, delivered by another task or dropped.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-144 · derives from WAY-146
- **Verification:** invariants: project-plan-check. For the reasons the change log gives and what
  reaches the human, an agent compares the plan, or the work on it, with the decision:
  - complies: two tasks both realize the projected decision on what a saved game state holds, and
    the plan makes one of them depend on the other; two tasks both realize a projected invariant
    on who reads a player's saves, an item of the change log lets them go side by side because one
    makes it true for the server's requests and the other for exported files, which share no code,
    and the human sees that item when the plan is handed over;
  - violates: a plan is handed over while the script reports a pair; an item lets two tasks go
    side by side with no reason, or with "neither depends on the other" as its reason; an item
    letting two tasks go side by side reaches the human only in the plan's file.
- **Origin:** none

*Rationale:* two tasks that make the same entry true change the same rules of the product; when
their cycles run side by side and merge in the wrong order, the later merge can bring back
behaviour the earlier one replaced, and nothing shows it as a conflict. A dependency is the plan's
own way of saying "one after the other" (WAY-144), so the rule needs no new field, only fuller
dependencies. Some pairs touch different parts of one entry and would wait for nothing, so the plan
can let them go together, but only with a reason the human sees, since going together departs from
the rule. An item tied to one entry lets the pair be reported again once the two tasks share
another. A task already done, delivered or dropped leaves no cycle to collide with: the other
task's cycle starts on code that holds its result. A shared entry is the overlap a plan can see
before any task is refined; a collision in code outside the entries still meets the end of the
cycle, where the target branch is pulled in and the product's tests run.
*Rejected:* a field naming the tasks a task can go beside — WAY-144 rejects it; the plan's critique
judging which tasks collide — a script decides it (WAY-146); a dependency forced with no way out —
two tasks making different parts of one entry true would wait for nothing; an item naming the pair
alone — a second entry the two tasks come to share later would pass unreported; a pair reported as
a remark that does not fail the check — the plan would reach leading with the pair unsettled, and a
remark repeated at every run stops being read; judging collisions by the files two tasks change — a
plan names no files before its tasks are refined.

## Task refinement and readiness

When a task is ready for its cycle, split or the fix of a defect, how its refinement is exchanged
and carries what it settles, and how it places the human's actions outside the repository.

### WAY-124 — When is a task ready for its cycle?

A task document records whether the task is independent, belongs to an item of a project's plan,
or uses an approved project definition as a source without belonging to its plan; it carries the
task's scope, temporary exclusions, relevant current foundation decisions, any approved
projected wording it uses and the settlements its refinement keeps for the foundation (WAY-134).
It is ready when the human has seen and accepted its complete document, its required outcome is
stated, every known question blocking that outcome is answered, the human has accepted or
rejected every candidate settlement its refinement derived, a row that repeats a choice the human
made between ways shown standing accepted until the human strikes it (WAY-134), every human action
it places before the cycle is done (WAY-140), and implementation questions carried into the cycle
are named. A project member also matches its plan item's scope, dependencies and assigned entries;
any task using an approved definition checks that its approval still holds and names each projected
entry, or the part of it, that its code makes true, while source-only use takes no other assignment
or dependency from the plan.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-118 · derives from
  WAY-126 · derives from WAY-134 · derives from WAY-140
- **Verification:** an agent compares the task document with its stated sources:
  - complies: an independent task is ready without a project plan, a source-only task uses
    approved project wording without taking its plan's assignments yet names a projected entry its
    code makes true with the part made true, a project member matches its plan item, and a task
    whose document places opening an external account before the cycle becomes ready once the
    human has opened it and accepted the complete document; a manually refined task with no
    candidate settlements likewise waits for acceptance of its complete document; a task whose
    only candidate row repeats the human's choice between ways shown is ready once the human has
    accepted the complete document, the row standing accepted unless the human struck it;
  - violates: a source-only task is blocked for lack of a plan item, a project member is ready
    despite a mismatch with its assigned work, a task leaves out a projected entry its code
    makes true, so its cycle writes a second entry for the same rule, a task is ready while a
    candidate settlement of its refinement awaits the human, or a task is ready while a human
    action its document places before the cycle is not yet done, or an agent marks a task ready
    after the human accepted its candidate rows but never saw and accepted the complete document.
- **Origin:** none

*Rationale:* a project can inform a task without owning it; the handoff must show which relationship
applies so the next agent does not import work or dependencies the task never took on. A projected
entry is wording already settled, and the task whose code first makes it true is the one that can
show it holds; naming it before the cycle keeps one entry per rule. A human action placed before the
cycle gives the cycle's code what it needs, so a cycle started before the human action is done
cannot finish its work. Acceptance of the complete document makes the human judge the task that
enters the cycle, even when its refinement found no new foundation settlement.
*Rejected:* requiring every task to belong to a project plan — it excludes independent tasks and
gives source-only tasks assignments they do not have; carrying only the entries a plan assigns — a
source-only task's code would hold a rule the foundation lacks, and its return step would write a
second entry for it; readiness inferred from an agent's completed refinement or from acceptance of
candidate rows alone — neither accepts the complete task the cycle takes.

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task
document and the conversation that refined it, in the form of the candidate table of the skills of
the elements (`elements/common/skill/build_table.md`) with each settlement in
the human's words and, in place of its kind, the place it goes to by the questions of the decisions
template, and the task document keeps the rows the human accepts, one that goes outside the decision
log included and those that repeat a choice the human made between ways shown included unless the
human struck them, and, where the human chose among ways shown, each way not chosen, under the
answer to its question or, for a choice made outside the task's questions, in the source of the row
it settles; the agent refining the task presents the table, or, in orchestrated refinement, the
project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a
glossary term, or an environment fact a candidate decision or invariant rests on, or a settlement
that goes to another place those questions give — a skill or an instruction file, the guidelines of
a discipline, or the data or code of the product — and a settlement that a current entry the
refinement reads for the parts the task touches, or a projected entry the task carries, already
states is no candidate. The task's cycle writes each kept row whole in the place its column gives,
in the same change as the code, in its foundation step, or in its return step where the foundation
step missed it, one that no code makes true included, keeping its meaning and choosing its wording,
and gives a decision written from a row as its rejected options only the ways not chosen that the
row's source keeps, `none considered` where the human said so, or `unknown`; where that meaning
cannot hold, or the entry needs any other value neither the row nor the cycle's work gives, the
cycle asks the human through a blocked draft request rather than write another entry, and otherwise
the entry's meaning is the one the human accepted with the row in the task document (WAY-114); a
kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated
becomes no second entry, the cycle tying the row to that entry and naming both in the request.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary,
  environment-facts
- **Based on:** none
- **Relations:** derives from WAY-33 · narrows WAY-114
- **Verification:** an agent compares the task document, or the cycle, with the decision:
  - complies: a task whose human settled in refinement that an exported record keeps its owner
    carries that row, and its cycle writes a decision with that meaning in the same change as its
    code and lists it in the lower part of the request's description; a task whose refinement found
    nothing carries the counting line with none below it; in an orchestrated round the project
    orchestrator shows the candidate table and required challenge questions while the refiner
    records the human's answers; the cycle's search finds a decision of an untouched part that
    already states a kept row, and the request names the row with that decision instead of a new
    one; a decision row whose question keeps two ways the human did not choose gives its decision
    those two as rejected options, and one whose source keeps none, or keeps only ways that answer
    another part of the question, gives `unknown` with no question to the human; the row that
    repeats the choice the human made between two ways shown stands in the table accepted and
    marked, while the rows the agent derived from the material wait for the human; a rule of how an
    agent works that only one skill holds stands in the table as a row that goes to that skill, the
    human accepts it with the other rows, and the cycle writes the line in the skill in the same
    change as the code;
  - violates: the cycle writes the entry with another meaning, or leaves out a kept settlement
    because no code makes it true; a settlement that goes to a skill, to guidelines or to the
    product's code is left out of the table because it is no entry, or is written into the log as a
    decision; the refinement writes whole entries into the task document; a kept row repeats a rule
    a current decision the refinement read states; the cycle writes a second entry for a rule its
    search found already stated; an orchestrated refiner asks the human directly about candidates or
    substitutes its own acceptance; a task document keeps the human's choice among ways shown
    without the ways not chosen; the cycle fills a decision's rejected options with ways it derives
    from what the cycle would otherwise guess, or blocks the request to ask the human for them; a
    row that repeats the human's choice between ways shown waits for the human's acceptance like a
    row the agent derived.
- **Origin:** none

*Rationale:* a settlement the human makes while a task is refined binds after the merge as much as
one a project settles, yet with no place in the task document it reaches the cycle as an answer to a
question, where it reads as one more choice the cycle may make otherwise; the same holds for one
that goes to a skill, to guidelines or to the product's data or code, which the human also sees and
accepts in the table, since a settlement the cycle placed on its own would bind with a place and a
wording nobody approved. A row in the human's words carries the meaning into the cycle without a
second point of acceptance: the wording stays the agent's, as for every entry a cycle writes, the
human judged the meaning when accepting the row, and the merge does not ask again, while the review
of the whole change reads the entry against the row. A row that repeats a choice the human made
between ways shown carries that choice already, so it enters accepted and the human cuts only the
rows the agent derived; asked again, the human would answer what the choice settled, and the price
is that the row is the agent's summary of a choice the human did not read at the choice, so a wrong
summary is caught only by reading the table when the document is accepted. A table read from the
whole document finds a settlement said in passing, and its column of what the cycle would guess
drops one no reader would miss. Refinement compares the candidates with the entries it reads for the
task's parts; what no link joins, the one search of the whole foundation finds once the cycle has
settled the entry (WAY-33), and a rule already stated keeps one entry. A meaning that cannot hold
goes back to the human before the request because the human settled it, and finding the change only
at the merge would leave code already written for another meaning. In an orchestrated round a single
human-facing agent keeps these choices together without making the refiner a second channel to the
human. The ways the human saw and did not choose outlive the conversation that showed them only in
the task document. A rejected option the writer of an entry derives reads as one the human weighed,
and an agent that proposes it later has to say what has changed for a way nobody turned down, so a
way kept from the refinement is written and a missing one is `unknown`, which tells the reader
nobody knows what was weighed.
*Rejected:* whole entries written while the task is refined, as a project definition projects them —
a task has no gate to approve their wording, and refining a task would weigh as much as defining a
project; noting a settlement only when the human states one — a settlement said in passing in the
request is missed, and the agent alone decides what binds; letting the cycle change or drop a
settlement and show the difference in the request — the human's settlement could be reversed and
seen only once the code is written; decisions and invariants alone — a word whose meaning the human
settled would be defined by the cycle; a search of the whole foundation when a task's candidates are
named — it repeats the cycle's search on wording not yet settled; the ways not chosen of every
choice kept in the source of its row — they would have to be carried from the question to the
building of the table, a cell of the table takes no line break, and an orchestrated refiner
transfers answers into the task's questions, not into its table; the rule of rejected options in the
templates alone — this decision would still have the cycle ask the human where the template has it
write `unknown`, and an agent comparing a change with this decision would take `unknown` for a
breach; the rule as part of WAY-29 — its question is a decision recovered from code, and the rule
can change apart from it, so it is a question of its own (WAY-19), and with this decision still
having the cycle ask, the two would need a precedence; a decision of its own — one more entry, while
this one has to be corrected anyway; every row accepted separately, as before — a second consent to
the same choice; rows that repeat a choice kept out of the table, the cycle writing the decision
straight from the answer under the question — the sieve of choices that bind no longer after the
merge goes (the column of what the cycle would otherwise guess), the cycle itself judges which
choice to enter, and this decision needs a stronger rebuild.

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external
account — is made only by a human, through a human action the task document names and places before
the cycle or in it, while reading outside the repository stays with the agent and the cycle's record
of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect
of the task, nor is the removal of the repository's own working directories that stand outside its
directory (WAY-375). For the human actions placed in the cycle, the cycle does what the repository
allows and opens a blocked draft request listing them, and the human performs them at the request; a
human action the cycle finds that the task document does not name joins that list for the human to
place, and the request opens as a blocked draft listing it even where the document places no human
action in the cycle. The human places each human action the task document names while the task is
refined, on the agent's proposal: before the cycle when the cycle's code needs its effect, such as
an account, a key or a database, and in the cycle when it uses code the cycle writes, such as a
deployment or a DNS record pointing to a new address.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-107 · derives from WAY-227
- **Verification:** an agent compares the task document, or the cycle, with the decision:
  - complies: a task that sends mail through an outside service names opening the account and
    creating its key as human actions before the cycle; a task that moves the product to a new
    address names pointing its DNS record there as a human action in the cycle, and the cycle, its
    code done, opens a blocked draft request listing it; the agent reads a server's free disk space
    while it makes the change; the cycle itself adds the request link to the task's entry in the
    product's backlog;
  - violates: the cycle runs the deployment against the server itself; the cycle stops halfway and
    waits for the human to rotate a key; a task whose outcome needs a new key on an external account
    is ready with no human action named for it; the agent alone decides that a human action goes in
    the cycle; the cycle finds that its change needs a key the task document does not name and
    creates the key itself.
- **Origin:** none

*Rationale:* an effect outside the repository is not undone by resetting a branch and does not show
in the diff the human reviews, so the human who makes it sees what it changes; named in the task
document, each human action is known before the cycle rather than found when the work stops on it.
The request is the cycle's single point of human review (WAY-227), so a human action that uses the
cycle's code waits for the request. A human action the cycle finds goes to the human like a named
one, because the cycle may not perform it, and the request is where the human meets it. A human
action whose effect the code needs has to come first, and one that uses the code can only come after
it; the human places each, because the human performs it. A read changes nothing outside the
repository and the agent needs it to work, so it stays with the agent. The backlog record is the
cycle's own account of its request, not something the task's outcome needs, so it stays with the
cycle.
*Rejected:* the cycle making the effect itself — a reset would not undo it and the diff would not
show it; the cycle pausing midway for the human — the human would be called between stages for each
human action; every human action before the cycle — one that uses the cycle's code cannot come
first; the agent placing each human action alone — the human performs it and is the one to fit it
into the work; human actions listed only when someone asks for them — a step the human has to take
comes to light after the work that needed it.

### WAY-154 — How do agents exchange a project task refinement and keep its result?

Project refinement resumes from the plan, task documents and one ignored conversation file per task
at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the answering
agent and the project orchestrator take serialized turns on each file; the project orchestrator
hands agents only its path and routing, never relays its contents, and each refiner ends its turn as
`questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`. Only a refiner
changes the task document's body and transfers settled answers with their sources and the ways the
human did not choose (WAY-134) into Questions to settle, and it writes besides what the project
orchestrator's order asks of it: in the turn in which it first creates the task document, or in the
first later turn that can where that turn could not, the line of its task in the backlog the product
names (WAY-107), where none stands, with the dependencies the plan gives the task, and, as the rules
of the task place give, brings the lines of the tasks tied to its task into agreement with the
plan's dependencies, at the same time as the other refiners of the round and with no queue between
their writes; the plan, the definition and the foundation stay outside a refiner, and no agent other
than the project orchestrator, after the human's word, takes a step that belongs to acceptance,
which is moving the line to ready and `ready for cycle`; the project orchestrator records human
answers in conversations, owns ordinary plan updates and their log, brings the dependencies in the
task lines in step with the plan when the plan's dependencies change, and after the human has
accepted a complete task document, one document at a time, changes that document's Status line and
moves the task's line to ready, making it already ready where none stands. Agent turns, questions
and explicit waits keep the plan task to refine, a presented human package or ready for approval
makes it waiting for human, and final acceptance makes both document and plan ready for cycle and
removes only that conversation after all settled answers, their sources and the ways not chosen
survive in the task document; an explicit wait is logged and its task is proposed again when the
named prerequisite is done.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-124 · derives from WAY-142 · derives from
  WAY-144 · derives from WAY-147 · derives from WAY-107
- **Verification:** an agent compares the turns, task documents, plan and backlog with the decision:
  - complies: parallel refiners write separate documents, and each, in its first turn that creates
    its document, also writes its task's line, with the dependencies of the plan's row, while the
    others do the same; a refiner whose first turn ended on a question about the task place's rules
    writes the line in the first later turn that can; a refiner that finds the line of a task
    waiting on its own task without the dependency on it brings that line into agreement as the
    rules of the task place give, and one that finds no line for a tied task makes none; a fresh
    refiner keeps each settled answer and source; the project orchestrator, on the human's
    acceptance of a document, changes its Status line, the plan's row and the task's line together,
    making the line, already ready, where none stands; and interrupted acceptance resumes without
    guessing human agreement;
  - violates: the project orchestrator rewrites a task body or carries questions in prompts, an
    agent's readiness stands for human acceptance, a refiner moves its line to ready or writes
    `ready for cycle`, a refiner writes the plan, the definition or the foundation because a
    dispatch asked it to, a round's refiners wait for one another to write their lines, a refiner
    makes the line of a tied task that has none, or cleanup loses the only settled answer or the
    only record of the ways the human did not choose.
- **Origin:** none

*Rationale:* a file-mediated exchange keeps the project orchestrator from becoming a content relay
and lets another session resume. The retained task document carries the result that later work
needs; ownership and serialized turns cost explicit coordination but prevent competing edits. What
the rule protects is the step of acceptance and the shared plan, definition and foundation, not the
document alone: a refiner that writes only what its order asks does the work of the line in the turn
that makes the document, where the context for it is at hand, and the human's word still moves the
line to ready. The price taken: the rule is no longer checked by asking whether a refiner wrote
outside its document, but by what the orchestrator ordered, so a line is lost silently when an order
leaves it out. The refiners of a round write their lines in the same minutes, and two writes to the
one backlog file in the same instant can lose a line, or two refiners that bring the same tied line
into agreement can leave one write of it, a risk accepted because it is small and shows afterwards
as a task with no line or a line missing a field. The dependencies a line carries are a second copy
of the plan's, which WAY-144 calls a copy that drifts as soon as one dependency changes, and the
project orchestrator keeps it in step with the plan; that cost is accepted so that the view of tasks
shows what waits on what.
*Rejected:* conversation contents relayed in prompts — each transfer repeats context and can lose
answers; retaining the temporary exchange as the task result — later work reconstructs settlements
from discussion; deleting the exchange before durable transfer — provenance disappears; the project
orchestrator taking the whole backlog and the rule staying as it was — the refiner leaves undone
what it could do and the orchestrator gains one more duty to remember; refiners writing their lines
with no queue but by one append to the end of the file and a check — a technical requirement to
enforce in every order, which lowers the risk of a collision and does not remove it, since the
editor of the notes or its synchronisation can write to the file at the same moment; no change —
each following round leaves its tasks with no line to be added by hand; the first turns of the
refiners one after another to order the writes — the first turn of a round lasts as long as all of
them together; the first turns in parallel and the orchestrator then resuming each refiner for a
short request for its line — several short resumptions, a new refiner reading the whole skill when a
session breaks off on the way, and an exception to the new refiner of each turn; a new refiner for
each turn as before — the most expensive way in tokens; no dependencies in the lines — the order is
read from the plan, and the view of tasks shows none of what waits on what; the dependencies as a
separate task — one more full cycle, and until then they are added by hand.

### WAY-155 — What may the answering agent settle during a refinement round?

The answering agent answers a refinement question only with a quotation and source from the
definition, plan, foundation or other task documents, or with a factual code observation naming
file and line; a question about how the product is to be is answered only from a document, never
from code or the agent's inference. It reads the round's conversations, makes an unanswered
choice a question of decision to the human, as WAY-113 gives it, and brings the same
question to the human once while preserving its affected tasks; in the area of the choices a
refinement round leaves unanswered, this decision prevails over WAY-114, under which a question
goes to the human only where the agent has no recommendation. The project orchestrator
presents one round package of these questions, candidate settlements, placement of Human actions
and complete wording, together with every quotation answer as question, quotation and source; a
quotation answer the human strikes becomes a question to the human, whose answers return to the
conversations before fresh refiner turns.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-113 · derives from WAY-134 · derives from
  WAY-140 · narrows WAY-114
- **Verification:** an agent compares questions, answers, sources and the human package:
  - complies: a code observation settles current behavior, a documented choice settles intended
    behavior, and a rejected quotation returns once as a human question for all affected tasks;
  - violates: code or an inference supplies a requirement, a quotation answer is hidden from the
    package, or two tasks ask the human the same choice separately.
- **Origin:** none

*Rationale:* an answer grounded in a source saves the human from restating an existing settlement,
while distinguishing observation from prescription prevents accidental behavior becoming a rule.
Showing quotation answers costs attention but lets the human reject an answer that fails its
question; one shared question avoids repeated decisions.
*Rejected:* free inference by the answering agent — a plausible conclusion appears settled;
code as authority for intended behavior — an accident becomes a requirement; hiding quotation
answers until final approval — the human cannot inspect the basis of the refined tasks.

### WAY-355 — Which task fixes a defect found after a merge?

A task fixes a defect found after a merge when it removes a defect against what the task of an
earlier merged change, or the foundation, required when that change was merged, or a regression,
which is the breaking of something that worked and that the earlier change's task did not tell it
to change. A new need, a change of mind, a gap of the earlier task, a thing it did not foresee, and
maintenance such as updating a dependency are no such defect.

- **Scope:** project-level, task-cycle, process-audit
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares a change with the decision:
  - complies: a task that restores a check which a merged change broke, though the task of that
    change did not tell it to touch the check, fixes a defect found after a merge; a task that adds
    a field because the human now wants one, a task that handles a case the earlier task never
    mentioned, and a task that updates a dependency fix none;
  - violates: a task that handles a case the earlier task did not foresee is counted as fixing a
    defect of that earlier change; a task that restores what a merged change broke is left out
    because the earlier task did not mention it.
- **Origin:** none

*Rationale:* the narrow test keeps what the review of a change let through apart from what the
refinement of its task did not foresee, so the count answers whether, for example, a cheaper model
of the review lets more through. A wider test mixes the two.
*Rejected:* broadly, every task that mends something a merged change did wrong or did not foresee —
a cheap judgment, but the number mixes what the review let through with what the refinement did not
foresee, so it does not answer whether, for example, a cheaper model of the review lets more
through; broadly, with the kind of the defect in the line ("defect against the requirements" or "gap
of the task") — one more judgment for each such task, a second class in the register and a second
result to read, while nothing waits for a measure of the gaps of tasks today.

### WAY-372 — When is a task split into several tasks?

A split of a task is proposed only where it makes the work better or cheaper; time does not count,
so that a part is ready sooner is no reason. Whoever proposes a split names its reason, and the
reasons are three: a part cannot start or finish without something outside the refinement of the
task, such as access the agent lacks or another task's result; the parts change different
repositories (WAY-140); or a later step of the refinement offers a separate task. A task's size
alone is no reason: for it an agent says nothing of a split — no mention, no question, no
recommendation — and a split the human asks for, who sees the whole document, stands without one.

A project plan cuts its tasks by WAY-143 and by these reasons, never by a task's size alone.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-13 · derives from WAY-140 · derives from WAY-143
- **Verification:** an agent compares the work with the decision:
  - complies: refining a task whose parts change two repositories, the agent proposes the split and
    names that reason; refining a large task of one product, whose parts all start and finish
    without anything outside it, the agent says nothing of a split, and a split the human asks for
    is made;
  - violates: the agent proposes a split because a part would be ready sooner; the agent mentions
    that a task is large, asks whether to split it or recommends the split; a split is proposed
    with no reason named; a plan's author cuts a task for its size alone.
- **Origin:** none

*Rationale:* a split gives a part of the work a cycle of its own, with its own review, its own full
tests and its own request to merge, so it costs a whole cycle more, and it earns that cost only
where the work comes out better or cheaper; a part ready sooner is neither. The three reasons are
the cases where a split gives something one task cannot: a part that cannot start or finish alone
would wait inside one task and no cycle could end it, and parts in different repositories are not
one change. Naming the reason makes the proposal checkable, which a bare "better" is not, since an
agent readily makes one up. A word about a task's size draws a question, and the question returns at
every larger task, while the human who sees the whole document at its acceptance can ask for a split
without it.
*Rejected:* a split sensible only where the work comes out faster, cheaper and better all at once —
it passes practically only a split where one task would not go through one cycle anyway, and it
rejects even a better result paid for with a second cycle; a split sensible where any one of the
three holds — it passes "two cycles in parallel finish sooner", though dearer, the very argument the
human refuses; besides the three reasons, a risky part beside an independent one — the review aimed
at risk and the human's decision at the request already handle risk, and the split gives only that
the independent part merges without waiting, which is "sooner"; besides the three reasons, a request
to merge too large for a sensible review — at refinement the agent knows the size of the task, not
of the future change, so it is size in disguise; a general test in place of the list, the agent
proposing where it names what will be better or cheaper — the agent readily makes up a plausible
"better", which is the problem; one sentence on a task's size, with no question and no
recommendation — the mention still tempts the agent to ask, so the instruction would have to forbid
the question outright; the agent asking on a large task as before — the question returns at every
larger task; the plan's cut left as it was — the rule stays, and so does the disagreement between
the refinement and the plan's cut; a task of its own for the plan's cut — one more refinement and
one more cycle.

### WAY-374 — Does the refinement of a task ask about a word its sources leave readable in two ways?

At its step that resolves the gaps, the refinement of a task looks in the task document and in the
sentences of the sources its required result rests on — the foundation decisions the document quotes
and the sentences of the approved project definition — for a word that allows two different required
behaviours and that none of the approved project definition, an entry of the foundation, a glossary
entry included, and an answer of the human in the document settles. Where a sentence standing in the
document or in such a source allows both readings and the readings give different, observable
results inside the task's scope, the agent shows a short example from that scope and asks the human
which reading holds, as a question of decision (WAY-113); the answer stands under the task's
*Questions to settle*.

A reading no sentence allows and a case outside the task's scope raise no question, the check owes
no finding and no number of cases, and where the agent finds none it says nothing of the check. A
meaning the human settles that a reader who knows the product's field would not give the word goes
to the task's *Settlements to record* as a candidate glossary term, which WAY-95 judges there, and
an ambiguity in the approved project definition whose resolution changes the definition goes back to
the definition and its readiness gate (WAY-118).

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: a task document of a game says that the view shows the score, and the sentence of the
    approved definition it quotes uses "view" once for the drawing of the board and once for every
    screen of the browser, where the two give a different result in the task's scope; the agent
    shows the two results and asks which reading holds, and the answer goes under *Questions to
    settle*; a word whose reading an entry of the glossary settles raises no question; a task in
    which the agent finds no such word says nothing of the check;
  - violates: the agent takes one reading of the word and writes it into the task's *To do*; it asks
    about a reading that no sentence of the document or of its sources allows, or about a case
    outside the task's scope; it writes that it found no word read two ways; it sends every meaning
    the human settled to *Settlements to record* as a glossary term; the check is read as a duty to
    show some number of cases.
- **Origin:** none

*Rationale:* a word that the sentences of a task or of its sources allow two ways, with a different
result for each, reaches the code when no step asks about it: the agent that makes the change takes
one reading, and the difference shows only at the review of the request or after it, when it costs a
return to what was settled. The refinement is where the human who can say which reading holds reads
the whole document, so asking there costs one question. The-way takes this practice from lesson m2l2
of the 10xDEVS course, where an agent that plans a change first probes the terms the request leaves
undefined — "top N", "latest", "active" — with the smallest case in which two readings give a
different result; it binds the refinement of a task by this decision and nowhere else (WAY-100).
The lessons of the course are not open to a reader of this repository. What the decision adds are
its bounds. The sources are the task document and the sentences its
required result rests on, so a word that stands only in a quoted decision or in the definition is
reached and the rest of the foundation is not. A case counts only where a sentence standing in those
files allows both readings, after the model of WAY-99 for a word of the foundation, and where the
difference shows inside the task's scope, because an agent told to find cases finds plausible ones.
The check owes no finding and no number of cases, and says nothing where it finds none, for the same
reason. A word of the process is settled by the glossary of the-way and a word of the product by the
product's glossary, and only a meaning a reader of the field would not give takes an entry (WAY-95).
The price: a word whose second reading no sentence of the document or of its sources allows passes,
and so does a word that stands only in an entry of the foundation the document does not quote; a
refinement that finds no such word shows no sign that the check ran.
*Rejected:* only the words of the task document — it leaves out a word that stands in a quoted
decision or in a sentence of the definition and not in the task's own text, though the sentence
decides what the task requires; the whole definition and the whole foundation — the check becomes a
ritual and invites cases from outside the task, which the bound exists to prevent; the principle of
no duty and no number alone, the rest left to the agent's judgment — the shortest, but an agent
readily adds plausible cases at the edge, so it protects least; one sentence that it found no word
read two ways — it shows that the check ran, but it turns into a ritual and a temptation to add "but
maybe", which is inventing cases by the back door; every settled meaning as a candidate glossary
term — the glossary would grow by words nobody confuses, against WAY-95, which it would have to
change; the same probe made again by a review of the finished plan, which looks among its blind
spots for a term the plan never decides at the tie — left out of what the refinement takes from the
lesson.

### WAY-377 — Does the refinement of a task list the decisions its document leaves to the executor before the human sees the document, and who lists them?

Before the refinement of a task shows its complete document to the human, it has the decisions the
document leaves to the executor listed where the document's *Decisions in play* is not `none` or the
task changes a skill or an instruction file, and for no other task. Two fresh agents of one class of
model, cheaper than the refining agent's and named in general terms, never by the name of a model,
make the list: the first, given the complete document and the full text of the entries *Decisions in
play* names, lists each decision an executor would have to take on its own that they leave
unanswered or answer in part, and marks each answer as written, visible only in a file the document
names as a model, or guessed; the second, with read access to the repository the task changes,
settles each guess against the repository and the document. A decision counts only where it follows
from a sentence that stands in the document or in a named entry and where different answers give a
different, observable result inside the task's scope, and the list owes no decision and no number
(WAY-374).

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: a task whose *Decisions in play* names an entry of the log is refined, and before its
    document is shown the refining agent starts one fresh agent on a cheaper class, giving it the
    document and the full text of the entry and nothing of the refinement's conversation; it gets a
    list in which each decision is marked written, visible only in a model file, or guessed, and
    starts a second fresh agent on the same class that settles each guess against the repository; a
    task that renames a file and whose *Decisions in play* reads `none` gets no list and no mention
    of the step; a task with `none` there that edits a skill gets the list; a list with no decision
    is accepted as it is;
  - violates: the step runs for a task that renames a file with `none` in *Decisions in play*; the
    first agent is given the conversation of the refinement; an agent runs on a class named by the
    name of a model, or the two run on different classes; the list holds a case outside the task's
    scope, or is padded to a number of decisions; the guesses go to the human with no second agent
    having settled them.
- **Origin:** none

*Rationale:* an executor that meets a matter the document leaves open settles it on its own, and the
human learns of it at the review of the request or not at all; in the product's own tally of the
problems that cost the human's time in the work of the process, more than half were an obscurity of
a task that the agent settled, and the record of that tally is not open to a reader of this
repository. A fresh agent that reads only the document and the entries it names can list such
decisions before the cycle, and the mark of where each answer is known separates what the document
states from what the agent had to guess. A trial on two accepted task documents of this repository,
the product's own measurement whose record is not open to a reader of this repository, gave 14
decisions on each, 9 and 12 of them guesses; a critic with read access to the repository found 5 of
the 9 guesses of the first document already settled there; one run of both agents cost about 200 to
250 thousand tokens and 3 to 5 minutes. The cost fixes the condition: a task with no decision in
play that changes no skill and no instruction file is a small one, where the cost exceeds the gain.
The class is the cheaper one for both agents because in the trial the critic on it found an entry
that went against WAY-90 and a gap in the template of a request's description, and quotations it
gave, checked at random, agreed with the repository. The bound is that of WAY-374 and for the same
reason: an agent told to find decisions finds plausible ones outside the task. The price: a task
outside the condition keeps the gaps its executor settles, and a gap the two agents do not see stays
for the executor. The-way takes this practice from the course AI Tech Leaders, in whose notes of the
author it stands as the idea of listing the decisions a task document leaves to the executor with a
mark of where each answer is known, to be tried on two tasks; the notes are not open to a reader of
this repository. It takes the list and the mark, and leaves out the count of how many guesses the
human would settle otherwise and the minutes of reading the list, which the notes keep for the
trial; the second agent, the bound, the condition and the class are the-way's own (WAY-100).
*Rejected:* the step at every refinement of a task — one run cost about 200 to 250 thousand tokens
and 3 to 5 minutes in the trial, and for a small task such as a rename or a small fix the cost
exceeds the gain; the step only at the human's request — it depends on the human remembering it, and
the gaps are still closed by the executor during the work; a stronger class of model — several times
dearer with no proof that it is needed, since in the trial the critic on the cheaper class found the
gaps named above and its quotations agreed with the repository.

### WAY-378 — What does the human see after the decisions a task document leaves to the executor are listed and criticised?

The refining agent shows the human only the matters that the second agent of WAY-377 leaves truly
open and the gaps of the document itself, at most about four, the most consequential first, each in
plain language as WAY-113 asks a decision; the full list and the critique stay in a file in the
ignored `.runs/` directory of the product, whose path the agent gives the human. Before it shows a
matter, and before it keeps a guess from the human on the critique's verdict that the repository or
the task document already settles it or that it is most likely right, it checks the quotations
behind that verdict and gives the matter one explicit verdict (WAY-120), and where no matter is open
it says nothing of the step.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-377 · derives from WAY-113
- **Verification:** an agent compares the work with the decision:
  - complies: the list of a task has 11 guesses, of which the critic finds 6 already settled in the
    repository or the task document and 3 most likely right; the refining agent opens the file the
    critic quotes from, sees that the quotation of one of the 6 does not say what the critic claims,
    and counts that guess open; it shows the human 3 matters, each as a question of decision
    (WAY-113), the most consequential first, and the path of the file; a task whose list holds
    no open matter gets no mention of the step;
  - violates: the human is shown the whole list of guesses; a matter is shown, or a guess kept from
    the human, on the critic's verdict with no check of the quotation behind it; more than about
    four matters are shown at once, or a matter that is no question of decision; the path of the
    file is not given; the agent writes to the human that the step ran and found nothing open.
- **Origin:** none

*Rationale:* the raw list of guesses is too long and too thin to assess: in the product's own trial,
whose record is not open to a reader of this repository, the human looked through one in 5 minutes
and could not judge it, and only the critique of an agent with read access to the repository,
written in plain language, gave matters to settle: the human settled 7 of them, and 5 of the 7 added
a sentence to the task document. A critic can call a matter settled while the first agent was right
or the reverse, so the refining agent opens the file the critique quotes before it shows a matter and
before it keeps a guess from the human, and the full list and the critique stay in a file, where the
human who wants to check one finds it. Plain language and a limit on the number keep the human's
reading to what only the human can settle. The price: the refining agent opens one file for each
guess the critic keeps from the human, which the list bounds, a guess whose quotation holds but does
not settle the matter stays out of the human's sight, and a human who wants the whole list opens the
file.
*Rejected:* the full list of guesses shown to the human — the raw list took the human 5 minutes and
could not be assessed, and a critic could call a matter right while the agent was wrong, which is why
the full list stays in the file and the refining agent checks the critique's quotations, those of the
guesses kept from the human included.

## The course of a task cycle

The weight of a task's process, the methods of the cycle, when it writes a spec or a plan, on which
models it runs, how its stages pass their work, and how a task ends.

### WAY-11 — How does a task end?

A task ends with its return step before its branch is merged: an agent compares with the code the
foundation entries the change writes or changes, those its task names and those the search of the
foundation found, and the part map of the parts the task touched, and corrects in the same change
whatever no longer matches. In the same change it writes the sources outside the product that the
change rests on and the foundation does not yet hold, as environment facts, a word the change uses
in a meaning for which WAY-95 gives it an entry, as a glossary term, and the accepted settlements
(WAY-134), each in the place the questions of the decisions template give it and as an entry of the
decision log only where it passes all of them and where someone who does not know the decision would
do otherwise and a test that stops them would not tell them why, and projected entries (WAY-126) the
task carries that are not yet written. It writes an invariant only for a rule the task, a decision
or a human sets, never for code behaviour merely because no invariant covers it.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01
- **Verification:** invariants: return-step-record. For what the return step compares and writes,
  an agent compares the diff, the task and its sources with the decision:
  - complies: the return step finds that a part-map entry still names a file the change removed and
    corrects it; the release notes of a library the change rests on are written as an environment
    fact; a replaceable layout calculation stays in ordinary tests; an invariant the task's
    settlement sets is written; an accepted settlement that is an instruction for how an agent
    works is written into the skill that holds it, not into the log;
  - violates: a decision the change makes false is left for a later task; behaviour of the diff
    becomes an invariant only because no invariant covers it; an accepted settlement or an
    applicable projected entry is left out; an accepted settlement that the questions send to a
    skill, to guidelines or to the product's data or code is written as an entry of the log.
- **Origin:** none

*Rationale:* some of the foundation is learned only in implementation, and a change that drifted
from an entry does not report it; comparing what the change touched with the code finds that drift
where it arises, at the cost of reading only those entries. Facts and words are written because,
like rules, they are learned in code. An invariant written for behaviour no task, decision or human
sets binds a detail nobody chose, and its test fails on later changes nobody objects to. A
settlement that binds after the merge is written where its reader looks for it and where a later
change meets it, which for many settlements is a skill, guidelines or the product's data or code
and not a second copy of it in the log; the step that finds what no longer matches applies the same
questions as the step that writes the entries first, so the two do not place one settlement in two
places. An entry that nobody would act against, or whose test already tells why, only repeats what
the code says.
*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
in the code; a search of the diff and the task's log for every behaviour no invariant covers, each
turned into an invariant where a later change could break a requirement — it costs a large share of
a cycle and binds details nobody chose; ordinary tests alone for a rule the task sets — later work
can change it without meeting a foundation check.

### WAY-13 — What sets the weight of a task's process?

Every change, whatever its size, passes the product's tests and a review by an agent that did not
make it. At its start a task's cycle answers two questions — does the change touch the files of a
trust boundary (WAY-48), and does it hold an operation that cannot be undone — and a change for
which either answer is yes gets a review aimed at that risk; an operation that cannot be undone is
only prepared, and a human performs it after deciding at the request. A task's size may lighten how
its change is prepared and made — its plan and the number of agents making it — never the outcome
it has to reach or the checks run on the finished change, and outside preparing and making the
change it decides nothing; only a human sets a task to return knowledge instead of a change, which
merges nothing.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a one-line change to a stored format that cannot be undone is prepared, reviewed for
    that risk and run by a human who decided at the request; a change to the parser of network
    requests gets a review told of the boundary; a change one agent can hold, its foundation
    entries included, is made without a plan and gets the same tests and review as any change;
  - violates: a small task skips its review; the cycle runs a migration that cannot be undone; a
    change to a trust boundary's files is reviewed like any other; an agent turns a task into one
    that returns knowledge instead of a change without a human setting it so; an agent treats a
    large task as a reason to split it, or to lighten its checks, because of its size.
- **Origin:** none

*Rationale:* size misleads about what can go wrong: a rename across many files is easy to undo, a
one-line change to a stored format can destroy every user's data. What a stranger can send and what
cannot be undone are the risks a review aimed at them catches and an ordinary review may pass, and
two questions name them at the start without computing anything. Size does tell how much
preparation a change needs: a small change can be made without a plan, while the checks on the
finished change stay whole and a human still decides on what cannot be undone. Beyond preparing and
making the change size tells nothing worth deciding on, and a split for size alone has no reason of
its own (WAY-372). Returning knowledge alters what a task delivers, so a human sets it.
*Rejected:* checks as sharp as a criticality computed from the parts a change touches, with the path
that merges it chosen by whether it changes the foundation, recorded at the start and recalculated
after each diff — every cycle computes and records them, and a part with no failure modes recorded
draws the sharpest checks whatever it holds; the path chosen by size — size misleads; a human
approving every diff (DORA) — no fewer failed changes, and attention spent where it adds nothing;
keeping a change that cannot be undone, or one touching a trust boundary's files, from the lighter
preparation — it would take the lighter preparation from small tasks it suits, while a human's
decision and a review aimed at the risk already stop such a change.

### WAY-125 — Which methods does the autonomous task cycle use?

The task cycle `implement-task` uses the-way's own methods: `write-spec` for a spec and its review,
`plan-task` for a plan, `make-change` for each change an author, a slice's executor or a fix makes,
and `review-change` for each code review; the orchestrator conducts the cycle and its loop of
slices itself. Each agent reads the `SKILL.md` of its stage's method whole, and a file the method
names, one beside that `SKILL.md` included, only when the step or variant that names the file
comes, while the orchestrator reads no method it does not conduct.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-13 · derives from WAY-256
- **Verification:** an agent compares a cycle with the decision:
  - complies: the designer reads `write-spec` and each slice's executor `make-change`, while the
    orchestrator reads `implement-task` alone; a slice's executor reads the file its variant's step
    names when that step comes, and never the file only a fix's variant names;
  - violates: the orchestrator loads `review-change` because a review begins, or a reviewer works
    from its handoff without reading that method; the cycle requires a method the product's pin of
    the-way does not carry; a handoff tells a stage agent to read its method and every file the
    method names before its work begins.
- **Origin:** none

*Rationale:* the-way pinned in a product carries every method its cycle uses, so the cycle runs the
same in every harness and its methods change only with the pin. The agent doing the work needs the
picture of its whole method and the rules that hold across its steps, while loading a method again
for coordination spends attention without doing that work. A fragment that only one variant needs,
or only one step that some uses pass by, stands beside the method (WAY-256); read at the start, it
would stay in play through the other steps and in the variants the agent does not take, so its place
would spare the agent nothing. The gain is largest in the variants an agent does not take, since a
file read at an earlier step stays in context, while a step every use comes to stays in the
method's `SKILL.md`. An agent may pass by the moment its step names a file; the judgment that
moves a fragment beside a skill asks whether an agent recognises that moment.
*Rejected:* methods of an outside plugin, with or without a required version — the cycle overrides
their steps, keeps their log beside its record, and a product meets whichever version its harness
has installed; every method written into the one cycle skill — the orchestrator would read every
stage's method; reading every method in the orchestrator too — it repeats context the agent
applying it already holds; each agent reading its method and every file the method names at the
start — a fragment moved beside a stage's method would still be read at once, so the move would
change nothing for the agent.

### WAY-135 — When does a task's cycle write a spec?

A task's cycle writes a spec, reviewed by an agent other than its author, before implementation
and any plan where the task leaves an open design choice and nowhere else, and an invariant whose
sentence a row of the task's *Settlements to record* or a projected entry of its sources gives
leaves none. An agent that meets an open design choice while it makes the change returns a report
that holds no code, the attempt is discarded with the foundation entries the cycle wrote for it,
and a fresh agent given the report writes the spec, after whose review the orchestrator chooses
again whether one author can hold the change or it needs a plan, using the same judgment as before
implementation (WAY-136). Where the open design choice is a reserved choice, no spec is written: an
agent's report without code and the discard of its attempt stay the same, and the cycle stops
(WAY-268, WAY-269).

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-13 · derives from WAY-69 · derives from
  WAY-126 · derives from WAY-134 · derives from WAY-268
- **Verification:** an agent compares a cycle with the decision:
  - complies: a task whose rows of *Settlements to record* carry its two decisions and its invariant
    proceeds without a spec, and the review reads the invariant's test against its sentence; a
    task whose part-map change follows from the file it adds, with no other way
    open, proceeds without a spec; an agent that finds the task needs a decision the task does not
    carry returns a report without code, the branch goes back to its base — to the commit that
    moved the pin where the task moved it — and a fresh agent writes the spec; a reviewed spec is
    followed by one author without a plan when the change still fits one agent, or by a new plan
    when it needs division; an agent that finds the task needs a reserved choice returns a report
    without code, the branch goes back in the same way, and the cycle stops with no spec;
  - violates: a spec is written for a task whose document carries every entry it writes and that
    leaves no other way open; an agent designs a decision the task does not carry and goes on with
    the code; a spec is written around the code of an attempt that met an open design choice;
    a plan is required merely because a spec was written; a spec is written for a reserved choice.
- **Origin:** none

*Rationale:* a spec and its review earn their cost where an agent designs a foundation entry itself,
whose agreement with the current entries has to be checked before code is written on it; where the
task's document carries every entry, a spec restates what the human already settled and its review
finds nothing the reviews of the code would miss. An invariant the document carries is kept from
fitting the code by the review that reads its test against its sentence (WAY-69), not by a spec. A
choice found while the code is made cannot be weighed apart from that code, so the attempt goes,
its slices already made among them, since the spec may change what they made, and a fresh agent
designs from the task and the report. Settling the design does not itself create work to
divide; the extent of the settled change decides whether a plan earns its cost. A reserved choice
is the human's, so a designer given the report would settle what no agent may, and the cycle stops
instead.
*Rejected:* a spec for every task that changes the foundation — almost every task changes it, and
the spec would restate entries the human settled at a large share of the cycle's cost; no spec for
any task — an entry an agent designs would reach the code unchecked against the current entries;
an attempt that met an open design choice kept and completed — a spec would be written around
partial code; the agent of that attempt writing the spec — the spec would carry the shape of the
abandoned code; a spec for every task that writes an invariant — the review already reads its
test against its sentence; for a reserved choice, the work going on in the same request with the
result of the step that settles technology as a remark on it — the choice lands in a comment and not
in the task document, the frozen copy of the task parts from what the cycle does, and a new
mechanism is needed; for a reserved choice, a pause in the cycle with a question to the human — it
goes against WAY-227, which would have to change, and the cycle would stop working unattended.

### WAY-136 — When does a task's change need a plan, and who makes and reviews it?

A change that, as the orchestrator judges before implementation from the task document and,
where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made
without a plan by one author, who writes its foundation entries, its code and its return step; the
same judgment follows a reviewed spec, and an author that finds the change too large returns a
report without code, its attempt is discarded with the foundation entries it wrote, and a planner
divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which
divides it into slices and holds no code; the slices are made one after another in the plan's
order, each by an agent of its own, and a slice that proves too large for it is discarded with its
code and goes back to the planner to be split. A one-author change is reviewed by an agent that
did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation
that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every
other slice goes on after the orchestrator's mechanical check and its own checks; a change of more
than one slice then gets one review of the whole change, which judges every slice that had no
review of its own and names, for each blocking finding, the slice it comes from or that it comes
from none, while the review of a one-author change or of a plan's only slice is the review of the
whole change; and that review also checks coverage of the task, every row of its *Settlements to
record* and every projected entry it carries.

- **Scope:** task-cycle
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/step-review.md
  § "Cost" — "`per-step` multiplies review cost by the Step count — reserve it for high-risk work
  where an early defect propagating into later Steps costs more than the extra reviews."; read
  2026-10-23
- **Relations:** derives from WAY-13 · derives from WAY-69 · derives from
  WAY-126 · derives from WAY-134
- **Verification:** an agent compares the cycle and any plan with the decision:
  - complies: the orchestrator selects one author from a settled task, including its foundation
    entries, without first writing a plan; the author does its return step and another agent's
    whole-change review checks task, settlement and projected-entry coverage; a reviewed spec is
    followed by the same size judgment; an oversized author's attempt and its foundation entries are
    discarded before planning; a change of several slices has them made one after another, a slice
    the plan marks as touching a trust boundary or holding an operation that cannot be undone
    reviewed on its own and the others checked mechanically, and then one whole-change review that
    judges those others and names the slice of each blocking finding, while a plan's only slice
    needs no duplicate review; an outgrown slice is discarded and split; a task that moves the pin
    has the checks the move breaks counted in the route judgment and handed to its author or
    planner;
  - violates: a small task needs a plan merely because it writes foundation entries or follows a
    spec; the orchestrator writes a plan to decide whether to omit it; an author reviews its own
    work, or its whole-change review omits the coverage checks because there was no plan; an
    oversized author's entries survive its discarded attempt; a plan holds code; outgrown slice
    code is kept; two slices are made at once; a slice holding an operation that cannot be undone
    goes without a review of its own; a blocking finding of the whole-change review leaves open
    whether it comes from a slice; the route of a task that moves the pin is judged before the
    move, or without the checks it breaks.
- **Origin:** none

*Rationale:* a plan earns its cost by dividing a change into work an agent can hold and a reviewer
can read separately; where the change fits an author, repeated reading and handoffs add cost
without adding a check of the finished change. The risk is that the author fits its foundation to
its code; the review by an agent that made none of it keeps that choice open to challenge. An
incorrect size judgment costs an abandoned attempt, and discarding its entries as well as its code
keeps the later division from inheriting a failed shape. Slices made one after another each start
from the work before them, in one worktree, with no shared state to settle between them. A review
of every slice multiplies review by the number of slices; it pays where an early defect at a trust
boundary or in an operation that cannot be undone costs more than the review, and the review of the
whole change judges the rest. The price is that a defect of an early slice is found only after
later slices were built on it, and its fix may reach them; naming the slice of each blocking finding
shows what that price is. The checks a move of the pin breaks are work of the task that its
document cannot name in advance, so a judgment without them misjudges the change's size.
*Rejected:* a plan for every change, including a small plan used only to choose the route — it
charges for division where none is needed; lighter preparation only for changes leaving the
foundation unchanged — foundation work is common and does not itself require division; lighter
review or gate for a small change — size does not establish that its meaning stayed; small work
outside the task cycle — duplicate rules of the record, request and return step drift; a plan that
writes the code ahead — code written ahead still needs review; a whole-change review after the
review of a plan's only slice — it reads the same range again; an outgrown attempt kept and
completed — its division would be written around unfinished work; slices made side by side — each
needs a worktree of its own and a ruling on their dependencies and shared state before it runs, a
cost the change meets without gaining a check; a review of every slice — its cost grows with the
number of slices, most of which carry settled matters into code, while the review of the whole
change still reads every slice; a status by which the planner returns work it cannot divide into
slices — the pin moved before the route keeps the installer's output out of every plan; a measure of
the change's size, such as the number of files, deciding the route at the start of the cycle between
one author and a plan — on changes of one game product of 1 500 to 3 000 lines, with five cycles on
each route, a whole cycle with a plan cost 0.0182 USD per changed line (median cycle 39 USD) and a
cycle with one author 0.0157 USD (median 24 USD; the measurement is this product's own, and its
record is not open to a reader of this repository), because the plan adds the planner, the reviews
of its slices and a return step taken by an agent of its own, so the judgment from the task document
stays the choice.

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports
directory, while its messages carry routing, the stage's status, commits, a one-line check result
naming what failed or did not run, where the stage runs a test or another check, and the report's
path, while the agent's questions, concerns and each reach beyond its handoff stand
in its report. The handoff names what the agent reads, as the
orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files:
it may carry a section of the plan, spec or task copied word for word, never restated in other
words, with its file named as its address, so that a slice's executor gets its section of the plan
and works without opening the plan; and since only the orchestrator reads `cycle.md`, the
handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other
agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an
answer or choice that binds an agent goes into that agent's handoff or the message that resumes it.
The orchestrator records the event and relevant choices before dependent dispatch and reads
authoritative sources and relevant report evidence before deciding a question, settling a finding,
accepting a foundation meaning or verifying disputed or incomplete evidence, while routine
progression uses the short return, record, source paths and commits, without loading the material
the stage agent reads and checks or its full report again, and without requiring prior
conversational history; a missing or incomplete report is repaired before dependent work proceeds,
check and review duties stay with their assigned owners, and the cycle record is the cycle's only
log, with no method of the cycle keeping a log of its own beside it.

- **Scope:** task-cycle
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/executor-dispatch.md
  § "Model tier (best-effort)", the executor prompt template — "Full description: {paste the
  Step's bullets from PLAN.md Implementation Plan}"; read 2026-10-23
- **Relations:** derives from WAY-125 · derives from WAY-100
- **Verification:** an agent compares the stage handoff, return, report and orchestrator's ruling
  with the decision:
  - complies: a short return names its report, commit range and failed or unchecked checks, and
    the record permits resumption from files; a slice's handoff holds its section of the plan
    copied word for word and names the plan's path; an agent's questions stand in its report and
    its return says `questions`; the orchestrator reads the evidence of an unresolved question
    before deciding it; a missing report is repaired before the next dependent dispatch; routine
    progression does not load the stage agent's sources and full report again; a handoff tells its
    agent that `cycle.md` and the other files of the cycle's record directory are not its to read
    unless the handoff names them, and a reviewer reads the author's report because its handoff
    names it;
  - violates: a full report exists only in conversation, a short return conceals a failed check,
    dependent work proceeds on a missing report or mismatched commit range, or a question is
    settled from the short return alone; a handoff restates a requirement or value of the task,
    spec or plan in other words; an agent other than the orchestrator reads `cycle.md` or another
    file of the cycle's record directory that its handoff does not name; a handoff lacks the
    sentence that tells its agent so; a method keeps a log of the cycle's progress beside the record; the
    orchestrator reloads completed stage material for routine progression.
- **Origin:** none

*Rationale:* full material kept outside routine coordination avoids repeated context while
preserving evidence a ruling needs and a place from which work can resume. Short returns make
the next action visible, but an omitted failure can hide behind brevity, so relevant evidence
remains part of a decision and an incomplete report blocks dependent work. A check that any stage
runs can fail or go unrun, so every stage that runs one gives the line, not only a stage that checks
the product, and the orchestrator learns of a path left unchecked without reading the full report;
the price is that a stage that runs no check gives no line. Questions kept in the
report survive an interrupted session without being copied anywhere. A passage copied word for word
carries the requirement as its author wrote it, so the agent reads it without opening the whole
file, while a restatement is a second account of it that drifts from its source unseen. The decision
takes from Open Mercato's prompt for the executor of one step of a plan, which pastes the step's
bullets from the plan and names the plan's path among the step's anchors, the handoff that carries
its section of the plan word for word with the plan's file named as its address (WAY-100). The cycle
record holds every agent's events; an agent that reads it pays for all of them to learn one answer.
It also holds the orchestrator's reasoning, and so do the handoffs and reports of the other agents,
which carry the orchestrator's answers to their questions; an agent that learns that reasoning
before it gives its own assessment assesses under its influence; a reviewer of a spec in a cycle of
a game product read the log to see whether the orchestrator had already ruled on the designer's
points, and found no ruling there, and no harm to the assessment was found. The handoff says it,
because the handoff is the one text every stage agent reads in every harness, a stage dispatched
without its type included, and the sentence then stands in one place.
*Rejected:* the line of the check result dropped from the skill of the stage that plans — the
orchestrator learns of a path left unchecked only from the full report, which routine progression
does not read; the line asked only of a stage that checks the product — whether a stage gives it
then depends on whether the agent reads its skill or the decision, and a reviewer comparing with
the decision reports the gap again; full handoffs and reports repeated in messages — coordination accumulates material
it need not reread; short summaries as the only record — lost evidence cannot be recovered on
resumption; a second universal brief and report contract — duplicated obligations drift without
proving completeness; a slice method's own ledger of progress beside the record — it repeats the
record and has to be copied into it before its workspace is cleaned; rereading every stage's
evidence during ordinary coordination — it pays again for work already delegated; automatic
compaction — it does not choose the evidence a ruling needs; a handoff that restates the plan,
spec or task in its own words — the restatement drifts from its source unseen; every agent opening
the whole task, spec, plan and record — each pays to read what only a part of its work needs; the
executor's concise report of under three hundred words returned in its message, which Open
Mercato's prompt for the executor of a step asks for — left out of what the decision takes from that
prompt; the sentence that tells the agent what is not its to read placed in the definitions of the
agent types of a task cycle — in Codex and in a session without the types the stage would not have
it at all, and it would change what WAY-368 and WAY-370 say a definition and a stage without its
type hold; the same sentence in the handoff and in those definitions — it costs two places to keep
and the cost of the way through the definitions; a ban that covers only the cycle record and the
reports of other agents — the handoffs of other agents stay open, and in them the orchestrator
writes its answers to their questions, the same reasoning the ban keeps from the agent; a change
of the orchestrator's skill alone, with no change to this decision — the rule would stand in one
sentence of a skill with no reason written beside it, and a later rewrite of that skill could lose
it.

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model
set for them, named in general terms and never by the name of a model: by default a class cheaper
than the orchestrator's, for code that carries settled matters into the product, ordinary
implementation that takes decisions of its own included; the orchestrator's class, for a change
across many parts; or the strongest class available, which is the strongest of the models that the
session's settings allow, which the orchestrator takes from the list of allowed models (in Claude
Code the setting `availableModels`; where the session has no such list, every model it offers) and
never from the name of the strongest model of the family, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each
slice's class in the plan; the orchestrator sets the
one author's when it selects that route (WAY-136), by the same measure, and records it with its
reason. The one author writes its foundation entries, takes its return step and fixes its findings
on its own class.

An executor that returns `blocked` for a fact or permission no source supplies, reports a failing
check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a
repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the
slice's base, given the failed executor's report and what failed; and an executor of the strongest
class available that fails, or a retry that fails, stops the cycle.

The fix of a slice's findings runs on the class of the executor whose work stands, of findings in
several slices on the highest of their classes and of a planned change's finding of no slice on the
orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's
foundation entries, the return step of a planned change and every other reviewer work on no class
cheaper than the orchestrator's, and the review of the whole change and the review of the return
step work on the strongest class available.

- **Scope:** task-cycle
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/task-planning.md
  § "Filling `Exec` and the tier" — "Tier: `:cheap` when the Step is mechanical transcription of a
  complete spec (boilerplate, renames, applying a documented pattern, tests from an existing
  example); omit (= the configured default) for typical implementation; `:capable` for
  cross-cutting integration or design judgment inside the Step." ·
  https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/executor-dispatch.md
  § "Escalation before the stop" — "dispatch a **fresh executor for the same Step one tier above**
  the failed one (`cheap` → `standard`, `standard` → `capable`), with the failed executor's report
  and the concrete failure appended to its prompt." · § "Escalation before the stop" — "Escalation
  is bounded: one rescue per Step, never above `capable`"; read 2026-10-23
- **Relations:** derives from WAY-136 · derives from WAY-148 · derives from WAY-100
- **Verification:** an agent compares the plan, the record of slices and the dispatches with the
  decision:
  - complies: the plan sets the default class for a slice that applies a pattern the spec settles
    and for one of ordinary implementation that takes decisions of its own, the orchestrator's
    class with its reason for a slice that joins several parts, and the strongest available with its
    reason for one that needs design; the record gives the one author's class, with its reason where
    it is not the default, and the author writes its foundation entries, its return step and its fix
    on that class; an executor of the cheaper class whose check fails is replaced, from the slice's
    base, by one of the orchestrator's class given its report and the failure; the fix of a reviewed
    slice's finding runs on the class of the executor whose work stands; the review of the whole
    change and the review of the return step run on the strongest class available, whatever the
    class of the orchestrator, the orchestrator taking it from the models the session's settings
    allow;
  - violates: a plan names a model by its product name; a class other than the default stands
    without its reason; a failed executor is retried on the same class or a second time; an
    executor of the strongest class available gets a retry; a review or the spec runs on a class
    cheaper than the orchestrator's; the review of the whole change or of the return step runs on a
    class below the strongest available; a review is asked for on the strongest model of the family
    while the session's settings keep that model out; the one author works on the orchestrator's
    model with no class recorded.
- **Origin:** none

*Rationale:* a slice's handoff carries its settled requirement word for word, so much of a planned
change is the carrying of settled matters into code, which a cheaper model can do at a fraction of
the cost. Ordinary implementation within a settled task, spec and plan is within that reach too, and
the one author's change is bound by the same settled task; the reviews of the whole change and of
the return step, on the strongest class available, are what finds a cheaper model's error in code,
in a foundation entry or in the return step. The planner, who cut the slice, knows best what it
demands, and on the route without a plan the orchestrator, who judged that one agent can hold the
change, knows what that agent faces. A failure gets one retry a class higher before the cycle stops,
which costs less than running every slice on the strongest class available and less than stopping at
the first failure of a cheaper one; the slice's own review where it has one, and the review of the
whole change, find what a cheaper model got wrong. A measurement of the class of the reviewer: on
four merged changes of one product, of 959 to 1740 added lines each, two runs of each variant on
each change, which is 8 runs a variant; the reviewers read the code and ran scripts of their own but
could not run the product's tests, and worked on a reviewer's instruction newer than the changes
they reviewed. A reviewer of the cheaper class (Sonnet 5.5) passed the change in 4 of the 8 runs,
each time a change in which the original review had found a blocking flaw, repaired later, and a
reviewer of the orchestrator's class (Opus 5.5) that read the author's report passed it in 1 of the
8. The measurement is this product's own, and its record is not open to a reader of this repository.
The orchestrator's class is the class of the session that leads the cycle and may be a cheaper one,
so a review that follows it lets a flaw through in about half the runs of that measurement; the
reviews of the whole change and of the return step therefore follow no class of the session and run
on the strongest class available. That costs more, the price taken: fewer fixes after review are
counted to repay part of it, and the audit of the process shows what it costs (WAY-337, WAY-339).
What is available is the human's choice when a session starts, never a sentence of this log: a cycle
started with every model allowed takes the strongest it has, the review included, and a session that
leaves a model out takes the strongest of the rest, read from the list the settings give. A request
for a model outside that list got another model, in the one session observed the session's own, so a
review asked for on the strongest model of the family ran on a cheaper one where the session kept
that model out; the log names no model.
Classes in general terms survive the release of new models and fit any harness. The decision takes
from the skills of Open Mercato for planning and dispatching an executor a class of model for each
step of the work and one retry a class higher before the stop (WAY-100).
*Rejected:* every slice on the orchestrator's model — it pays the strongest price for transcription;
the orchestrator's class for ordinary implementation, or for the one author by inheritance — it pays
the strongest price for code whose decisions the task, the spec and the plan already bound; the
class chosen by the orchestrator at each dispatch of a slice — it judges again what the planner
judged when it cut the slice; the return step of the one author handed to a fresh agent of the
orchestrator's class — it pays a second agent to read the foundation again, while the review of the
return step judges it on the strongest class available; the orchestrator's class as the default — it
leaves the cheaper class to a judgment made slice by slice and rarely taken; retries without bound,
or on the same class — the same failure repeats at the same cost; a cheaper class for the spec, the
plan or a review — their errors reach every later step; two runs of a reviewer of a cheaper class in
place of one run of the strongest class available — both runs together caught 5 of the 14 reference
errors, as many as one run of the orchestrator's class in the measurement (5 and 6 in two such
runs), and did not improve the verdict, since a change with three blocking flaws got a PASS in both
(the same measurement, this product's own, whose record is not open to a reader of this repository);
model names in the process — they age with every release; the source's rule that typical
implementation stays on the default tier — here ordinary implementation within a settled task, spec
and plan is on the cheaper class too; the reviews of the whole change and of the return step on the
orchestrator's class, with the price in the rationale — with the orchestrator on a cheaper class a
review lets a flaw through in about half the runs of the measurement, and the protection the
rationale counts on then depends on the model of the session that leads the cycle; a bound written
in general terms with no criterion that tells the classes apart without a name — an agent reads a
general word as it pleases; the strongest class of the family the cycle runs on — a model of that
family that the human keeps out of cycles would take the reviews and the slices that need design, and
a request for it got another model; a
review one class above the session that leads the cycle, never above a model the human names — with
the session on the cheapest class the review would run on the middle class, which let a flaw through
in 4 of the 8 runs of the measurement, and a line that keeps a model out of the cycle's work has to
be drawn somewhere all the same; a restriction of models on the human's whole account — the model
leaves every session of the human, and each work on it would need a change of that restriction.

### WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?

Where the log of the target branch holds a number that a new decision of the task branch bears, the
task branch, before it merges the target branch and in a commit of its own, renumbers all its new
decisions in their order onto the next free numbers after the highest number that log holds, as an
entry or as a withdrawn number, and never changes the number of a decision of the target branch. In
that one pass it rewrites every reference to the renumbered decisions in the files of the branch and
in the original of the cycle's record as the record stands before the reconciliation is entered in
it; texts written afterwards, the rows that give the conversion of an earlier reconciliation and the
human's remarks quoted word for word stay as they are. The rule holds for the reconciliation with
the target branch before the request opens and for each merge of the target branch in a correction
after review, on either route.

The conversion of the old numbers into the new ones stands in the row of the cycle record's events
that records the reconciliation with the target branch, and in no other note of the record; a
reconciliation that renumbers again adds its own row beside the earlier ones.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-19 · derives from WAY-02
- **Verification:** an agent compares a cycle, its branch and its record with the decision:
  - complies: the new decisions of a task branch bear the numbers 500 to 502, the target branch took
    500 and 501 for its own, and the task branch gives its three the numbers 502 to 504 in a commit
    of its own before the merge, in the log, the tests, the comments, the skills and the original of
    the record, the spec, the plan, the handoffs, the reports and the process remarks among them; a
    remark of the human quoted in the record keeps the number it was written with; the row of the
    reconciliation reads 500 → 502, 501 → 503 and 502 → 504; a correction after review that
    meets decisions taken by another merged request renumbers the same way before its merge, gives
    a row of its own, 502 → 505, 503 → 506 and 504 → 507, and leaves the first row as it is;
  - violates: the task branch merges first and renumbers afterwards, or in the merge commit; the
    decisions of the target branch are renumbered; the numbers are replaced one decision at a time,
    so that 502 becomes 504 after 500 became 502; the log is renumbered and the record keeps the old
    numbers under a note of the conversion at its head; the human's quoted remark is rewritten; the
    row of the reconciliation gives no conversion; the row of an earlier reconciliation is rewritten
    with the map of a later one, so that it reads 500 → 505, 501 → 506 and 505 → 507; a correction
    merges the target branch with no renumbering where the numbers clash.
- **Origin:** none

*Rationale:* a task's new decisions take the next free numbers of the log of the branch the task
started from (WAY-19), and a task branch reaches the remote only when its request opens, so two
tasks that run side by side take the same numbers and neither can see the other's; the clash shows
at the merge, and the task that merges second gives way. The task branch renumbers rather than the
target branch because the numbers of the target branch already stand in the references of requests,
branches and commits that the task cannot reach, while its own numbers stand only in its own files
and in its own record. The record is rewritten in the same pass because a reference names an entry
the foundation holds by its number (WAY-02), and the request's description and the documents under
its links must name the same entry by the same number, so that the human who reads them converts
none by hand. The conversion of a reconciliation stands once, in the row where the cycle already says
that it reconciled, so that an old commit or an earlier remark of the human that carries an old
number can still be read; a row of an earlier reconciliation stays as it was written, since it was
true then, and the rows are read one after the other. The price: a reader of an old number follows
two rows after a second renumbering; the reports of the agents differ from what the agents wrote in
their numbers; the rewrite of the record is checked by no reviewer of the merge since the record is
no code; and a correction can renumber a second time when the request returns after another request
that adds decisions has merged.
*Rejected:* renumbering the decisions of the target branch; a temporary marker in place of a number
until the merge; the old numbers left in the cycle record, with a note of the conversion at the head
of the record — the mismatch the rule removes stays, and the reader converts each number by hand;
the numbers rewritten only in the copy of the record that is published in the repository — that copy
holds texts from before the merge and from after it, the later ones naming numbers of the target
branch from the same range, so one rewrite would corrupt them, and telling the texts apart by date
is fragile; looking at the numbers that other branches have taken while the numbers are given — the
task branch reaches the remote only when the request opens, so those numbers cannot be seen; the
rule in the reconciliation before the request opens alone — in a correction the agent goes on
improvising, and the second renumbering falls there; a note of the conversion at the head of the
record as well as in the row of events — a second copy of the same information, which a reader of
the rewritten documents does not need; no conversion kept anywhere — an old commit or an earlier
remark of the human that carries an old number becomes unreadable; the rule as a sentence of the
skill alone, with no entry — the rejected ways would stand nowhere an agent reads.

## The work of a cycle's agents

What an agent of the cycle checks of its own work and reports, how it waits for a long command, and
where its working copies and working directories go.

### WAY-164 — What does the author of a change check of its own work before review?

Before its work goes to review, the author of a one-author change names the requirement of the
task, and the executor of each slice the requirement of its slice read against the passages of the
task its handoff gives, that its work most likely does not meet, writes a check that would catch
that, and states in its report which requirement, which check and what the check showed. The
review that judges the work — a slice's own review where it has one, otherwise the review of the
whole change — reads that report, and the request lists what each such check showed among its test
evidence.

- **Scope:** task-cycle
- **Based on:**
  https://raw.githubusercontent.com/overment/limen/e746877e8ef195ab9a34a070bdd3b000d0b6cf10/templates/worker.md
  § line 25 — "Name the acceptance line most likely to be false and write the check that would catch
  it; say what that check did in the final message — a suite that only passes is not evidence.";
  read 2026-11-16
- **Relations:** derives from WAY-136 · derives from WAY-148 · derives from
  WAY-100
- **Verification:** an agent compares the author's or executor's report, the review and the request
  with the decision:
  - complies: the author of a one-author change names the requirement its work most likely misses,
    writes a test for it, and reports that the test failed and what it changed before review; the
    executor of each slice reports the same for its slice, read against the passages of the task
    its handoff gives; the review that judges each slice is given those reports, and the request
    lists each check among its test evidence;
  - violates: an author reports only that its suite passes; the executor of a slice reports no such
    check; the request leaves out what the checks showed; the author's check stands in for an
    invariant's test seen failing.
- **Origin:** none

*Rationale:* a suite its author writes passes because it tests what the author meant, so a passing
suite is no evidence that the work meets the task; turning to the requirement the work most likely
misses finds what the author can still catch before a reviewer spends a round on it. The executor
of each slice does the same against its slice, so that a larger change does not reach review with
no agent having attacked its own work. The report is the reviewer's material, and the request
shows the human what the attack found beside the other test evidence. The check does not replace
an invariant's test, which is seen failing once in its own right (WAY-08). The rule takes from the
practice that Limen, a harness of agents, sets its workers the naming of the requirement most likely
to be false, the check that would catch it and the word on what that check did, which is the whole
of that practice.
*Rejected:* the author of a one-author change alone — in a larger change made from a plan, no agent
would attack its own work before review; a review without the author's report — a reviewer of the
orchestrator's class without the report caught 4 and 3 of the 14 reference errors, with the report 5
and 6, and used more tokens, 112.47 million against 90.20 million in eight runs (the measurement is
this product's own, and its record is not open to a reader of this repository; its conditions stand
in WAY-229).

### WAY-255 — How does an agent of a task's cycle wait for a command that runs long?

An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps
its prompt cache — a container build, a mutation run, a test suite a check names — by running it in
the background and reading its output between waits each shorter than that lifetime, never in one
wait past it; in Claude Code a subagent's cache lives five minutes by default, so each wait stays
under about four. The one author's cache lives an hour, which the author's type sets (WAY-368), and
its waits stay under about four minutes as well, since Claude Code falls back to five minutes where
a subscription spends usage credits. Where the harness states no cache lifetime, the agent waits as
the harness allows.

- **Scope:** task-cycle
- **Based on:** claude-code-prompt-cache-expiry · claude-code-prompt-cache-ttls ·
  claude-code-subagent-cache-default · claude-code-subagent-cache-ttl ·
  claude-code-subagent-cache-ttl-credits
- **Relations:** none
- **Verification:** an agent compares an agent's waits in the cycle's transcripts with the
  decision:
  - complies: a reviewer in Claude Code starts the mutation run its review needs in the background
    and reads its output every four minutes until it ends; the one author, whose cache lives an
    hour, reads the output of a build it started in the background every four minutes as well;
  - violates: a subagent in Claude Code waits ten minutes in one command for a test suite to end; an
    agent's next step after a wait past its cache's lifetime writes its whole context to the cache
    again; the one author waits twenty minutes in one command on the strength of its hour; the type
    of a reviewer or of an executor sets the hour.
- **Origin:** none

*Rationale:* an agent whose cache has expired pays at its next step to write its whole context
again, while a check between waits reads that context from the cache at a fraction of that price; a
longer cache, where a harness offers one, costs more at every write, also in work that never waits.
The one author is the exception, since it alone is resumed after each review and for the return
step, and each such break outlasts five minutes. In a probe of the cache, a subagent with the hour,
resumed after 6.9 minutes in a live session, read 10,470 tokens from the cache and wrote 123, where
a control with five minutes wrote its whole 4,786 anew. Where the session was started again with its
saved conversation resumed, the hour did not help: the agent wrote its whole context anew at 2.0
times the price of input, where a write to a five-minute cache costs 1.25 times, in one try, twice;
the account in *Rejected* does not cover a restart. The probes are this product's own, and their
record is not open to a reader of this repository. The price: an hour that Claude Code ignores
while a subscription spends usage credits leaves the author at five minutes, so its waits keep to
four.
*Rejected:* one wait to the command's end — it writes the whole context again after every wait past
the lifetime; a longer cache lifetime for every agent — it raises the price of each step to spare
the few that wait: counted on the session records of past cycles of one game product and of the-way
(the count is this product's own, and the session records are not open to a reader of this
repository), an hour for every subagent raises the cost of a game cycle by 4.7% and lowers that of a
cycle of the-way itself by 1.4%, while an hour for the one author alone lowers them by 0.9% and 3.6%
and, where the author is not resumed, raises them by 0.7% and 2.2%; for the executor of a slice it
raises the cost of a game cycle by 1.6%, and for the reviewer of the whole change by 0.4% in a game
cycle and by 1.0% in a cycle of the-way itself.

### WAY-260 — What does each task-cycle stage report about what it could not find or understand?

Every task-cycle stage's report states each thing the agent looked for and did not find, or found
unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each
reach beyond the dispatch. The orchestrator copies every such item other than `none` word for word,
with the stage name and full report path, into the cycle record's *Process remarks on the-way*,
without combining repeated items.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-148
- **Verification:** an agent compares a stage report and cycle record with the decision:
  - complies: each stage reports its unsuccessful searches and unclear points, or `none`, and the
    orchestrator copies each item word for word with its stage and report path, keeping repeats;
  - violates: the report omits unsuccessful searches or unclear points, or the orchestrator omits,
    edits or combines a reported item.
- **Origin:** none

*Rationale:* a stage can resolve a gap itself without asking the orchestrator, but the next person
working on the process still needs to see where the work could not find or understand something.
Keeping this account beside the report's existing reach account preserves both kinds of evidence;
copying each item unchanged leaves the later reader able to compare the record with its source.
*Rejected:* recording only gaps in the-way's instructions — an agent must decide whose gap it is
while it is stuck, and some reports are lost; extending the reach account — routine reads would add
noise and change what that account means; collecting reports only from authors and reviewers — gaps
from designers and planners would disappear; combining repeated items — one may be hidden by an
incorrect match; adding the rule to the existing handoff decision — that decision is already long,
and a second purpose would make the reason for collecting gaps point to a decision chiefly about
something else; a condition for revisiting the scope — it needs a measure to be settled and an
obligation to check it in the decision.

### WAY-261 — What does a task cycle report about a check that fails and passes when run again?

Each failing run of a check remains in the cycle record with its command and result, even if the
check later passes. When a check has both a failing and a passing run during the cycle, the request
lists it under *Checks* as failed, with the result of its rerun and the number of cycle runs in which
it failed and passed; when preparing the request, the orchestrator recovers the task's parts from
the frozen task and its changed files using the part map, and lists the check beside findings
outside the task's scope when its file belongs to a different part. This applies in every product,
whether or not its testing guidelines name flaky tests.

The red result of the first run of the gate on the final tree stays the result of the gate, also
where the check that failed is one outside the task's scope that passes when run again; the cycle
does not stop for it, and the request names that check and the task that fixes it, or proposes that
task where none exists.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-243 · derives from WAY-160 · derives from WAY-161
- **Verification:** an agent compares a cycle record and request with the decision:
  - complies: a check that fails during the cycle and passes when run again keeps its failing run
    in the cycle record, appears in *Checks* with the rerun result and counts of its failing and
    passing cycle runs, and appears beside out-of-scope findings when its file's part, assigned
    through the part map, differs from the task's parts recovered from its frozen document and
    changed files; the first run of the gate on the final tree fails on a flaky test outside the
    task's scope, the request gives the gate as failed with the rerun's result, names that test and
    the task that fixes it or proposes one, and the cycle goes on;
  - violates: a successful rerun erases a prior failure from the record or request; a check is
    listed as outside the task's parts without the part map; a check's run counts are omitted; the
    request gives the gate as passed on the strength of a rerun of a flaky test; the cycle stops, or
    turns the test off, because a test outside the task's scope failed and passed when run again.
- **Origin:** none

*Rationale:* a later pass does not undo a failure, and reporting every failure keeps the gate's
result visible under WAY-243. The first run's red result stays the gate's, since a pass on a later
run hides the fault that made the test fail, and the cycle goes on, since a test outside its scope
is no fault of its change. The counts let the human distinguish an occasional failure from a
repeated one, while naming an outside check beside out-of-scope findings puts it before the person
who can decide whether it needs separate work. The cost is that an outside check appears twice in
the request.
*Rejected:* listing only checks outside the task's parts as failed — a check in a touched part can
still expose a defect and would have no route to the request; listing an outside check only beside
out-of-scope findings — a mistaken part assignment could remove it from *Checks*; applying the rule
only in products whose testing guidelines name flaky tests — products without that rule would keep
the gap; omitting counts — a one-off environment failure and a repeated product defect would look
the same; the cycle turning the flaky test off with a cause under WAY-233 until a task fixes it —
every cycle would change a test outside its scope, and a flaky test seldom has a cause on the side
of the data or the requirement, which WAY-243 shows by naming a flaky test skipped with "flaky" as
its only cause a violation; the rule written also in the decision on flaky tests and in the
template of testing guidelines — one more binding sentence and one more line to keep in every
product's guidelines, for a gain only in work outside the cycle.

### WAY-365 — What does a change do where it adds to a function or a file that stands over the threshold of the rule of size?

Where a slice of a plan adds to a function or a file that stands over the threshold of the product's
rule of size, the plan begins with a slice that moves a part of that function or file out without a
change of behaviour, writes the choice in its table of choices, and puts the slice that adds after
it. The author of a change without a plan makes that move the first commit that changes the code.
Such an addition is a choice of how to make the change and no open design choice, so it gets no spec
(WAY-135).

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-136 · derives from WAY-360
- **Verification:** an agent compares the plan, the author's commits and the record of choices with
  the decision:
  - complies: a task whose change adds a branch to a function that stands over its threshold gets a
    plan whose first slice moves a part of that function into a function of its own, with the tests
    that cover it as its checks, and whose second slice adds the branch, the move written in the
    table of choices; the one author of the same task makes the move its first commit of code, names
    it among its choices, and adds the branch in the commit after it;
  - violates: a plan whose slice adds to a function over its threshold with no slice that moves a
    part of it out; a spec written for such an addition; an author who adds in place and moves in the
    same commit or after it; a move that changes what the function does.
- **Origin:** none

*Rationale:* a threshold stops a change only after the code is written, and where the rule's
invariant is marked violated, an addition to a function not yet cleaned stops neither the test nor
the review, which guards only a cleaned file and a new one (WAY-51); so the room is made before the
addition. A move out with no change of behaviour is a change the tests that already cover the function
can check, and the slice that adds then lands in a place under the threshold. Moving is a choice of
how to make a change whose requirement the task and the foundation settle, so the plan's table of
choices holds it, and the open design choice that WAY-135 sends to a spec is not met.
*Rejected:* treating the addition as an open design choice, with a spec before the code — two further
stages, the designer and the reviewer of the spec, at each such addition, and a change to WAY-135,
whose reasoning ties the spec to a foundation entry that an agent designs; no change in the plan —
where the rule's invariant is not marked violated, the excess shows only in the gate after the code
is written, and where it is marked violated, an addition to a function not yet cleaned stops neither
the test nor the review (WAY-51).

### WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?

An agent of a task cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own under
the ignored `.runs/` directory of the task's worktree, never in the system's temporary directory, in
a session's scratch directory or in the main checkout of the repository. Before it returns, the
agent removes its copy, keeps in the cycle's reports what its report needs and states in the report
where the copy stood and that it was removed; where a removal fails, the agent finishes and names
the remainder with its path in the report, and the cycle carries it to its record and to the
description of the request, where the human sees it, and goes on. The same holds for the separate
checkouts that the orchestrator makes, while the files that a product's own tools and tests make by
themselves are no working copy of the agent and stand outside it.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-148
- **Verification:** an agent compares a change with the decision:
  - complies: a reviewer that needs the head commit with a file changed makes a worktree in its own
    directory under the task worktree's ignored `.runs/`, removes it before it returns and says in
    its report where it stood and that it was removed; a clone that a reviewer cannot remove is
    named in its report with its path, the cycle's record and the request's description carry it,
    and the cycle goes on;
  - violates: an agent makes a worktree in the system's temporary directory; two agents of one
    cycle write their scripts to one scratch directory; a report lists temporary files and does not
    say whether they were removed; a cycle stops because an agent could not remove a clone.
- **Origin:** none

*Rationale:* agents of the cycle left copies outside the task's directory that they could not
remove afterwards, and the human cleaned them by hand; agents of one cycle that shared the scratch
directory of the session overwrote each other's scripts, so that a run of one agent could run a
script of another. The ignored working directory of the task's worktree is inside the task's own
directory, a directory for each agent keeps the scripts of two agents apart, and what stands there
goes with the task's directory, so the human has nothing of the cycle to clean elsewhere. The price
taken: an agent that cannot remove its copy leaves a remainder that stays until the task's directory
is removed, and the human sees it in the request.
*Rejected:* a copy that stands outside the task's directory until the agent returns — it goes
against keeping the writes of an agent inside the task's directory; a failed removal that stops the
cycle — the cycle would stop for a thing the human removes with one command.

### WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?

At the start of a new cycle the cycle runs a script of the-way that removes the working directory of
an earlier task only where all of these hold at once: its tree is clean as git's own check for
removing a checkout reads it (WAY-376), every commit of it is on the remote, its branch is merged,
and it belongs to a cycle, standing on a branch whose name begins with `task/` or whose directory
holds the record of a cycle, or being a detached copy of a base made for a check. A branch is merged
where its tip is the second parent of a merge commit on the first-parent history of the remote
target branch, which git alone shows, so that a branch merged by squash or rebase, a branch that
stands at the target's tip with no commit of its own and a branch of a request closed unmerged are
not merged. A directory of a cycle that the script does not remove stays, with its reason, for the
human to decide, a copy of a base standing alone that the script does not assign to a task — one
named for no task, or for a branch it does not find — among them, and a detached checkout nested in
a directory that is removed goes with it, whatever its name, only where it is clean and on the
remote, else the directory that holds it stays.

The script touches only the checkouts that `git worktree list` names for the repository, never the
main checkout, the directory it is run in or a detached directory outside the cycle's, and it
removes directories only, never a branch, local or remote. Removing a checkout that git names, also
one that stands outside the repository's own directory, is a change to the repository's state and no
effect outside the repository in the sense of WAY-140, so the script that a cycle runs needs no act
of a human. In removing a cycle's own directories whose branches are merged this decision prevails
over WAY-13, which keeps its reach over every other operation that cannot be undone.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-140 · derives from WAY-153 · derives from WAY-373 · narrows WAY-13
- **Verification:** tests: which directories the script marks for removal and which it keeps, what
  makes a branch merged, that it touches only the checkouts git names and none of the directories
  it never removes, and that it removes no branch. An agent compares a change with the part no test
  holds:
  - complies: a new cycle runs the script before it creates its task branch and goes on without a
    word to the human where the script removed a directory that stands beside the repository's own;
    each directory of a cycle that the script kept reaches the record and the request with its name,
    branch and reason;
  - violates: the cycle asks the human before it removes a directory git names that stands outside
    the repository's own directory; the cycle removes a directory because its request was closed;
    the cycle deletes a task's branch after it removed the directory.
- **Origin:** none

*Rationale:* the directory of a task that stays after its merge fills the disk, crowds the list of
checkouts git keeps for the repository and leaves the human to find out by hand which of them is
still needed for a correction; and an agent's working copies, which go with the task's directory
(WAY-373), stay for as long as the directory does. Each condition keeps what is still needed:
a tree that is not clean and a commit that is not on the remote are work that stands nowhere else,
and a branch that is not merged is a task not yet delivered. The merge is read from the history of
git alone, so that the cycle works with any host a product may use, and its price is that a branch
merged by squash or rebase is not recognised and its directory stays for the human. The first-parent
history is read because a merge of the target branch into a task branch makes a commit of the target
the second parent of a merge that is not on the target branch, and a branch created at that commit by
another cycle would otherwise count as merged; a branch with no commit of its own, which another
cycle has just made, points at the target's tip and would pass the weaker test that the tip is an
ancestor of the target. A directory that belongs to no cycle, and a copy of a base that cannot be
assigned to a task, is not for the script to judge: a copy it removed for a name that matches no
branch could be the copy of a cycle running at the same time. The directories are removed and the
branches stay, since a branch keeps every commit and the directory can be made again from it with
one command, while deleting a branch is a decision of its own that WAY-269 gives to the human. What
the script removes stands in the state of the repository, which git lists and the cycle may change,
and not in a server, a record in DNS, a key or an account, which WAY-140 keeps for a human; asking
the human for each directory would leave the directories where they are. That is why WAY-13, which
has a human perform an operation that cannot be undone, yields here and only here. The price: a
removal cannot be undone, so the script judges by every condition at once and keeps what it cannot
place, and a directory that holds a checkout the script keeps stays with it.
*Rejected:* the script alone, with no step in the cycle, run by the human at the merge — whoever
does not run it does not clean, and the list of directories grows; a rule in the skill alone, with
no script — each cycle judges "no longer needed" in its own way and nothing gives one dry run for
clearing the directories that have gathered; the closing of a request without a merge as a reason to
remove — it needs a question to the host, and the cycle works with hosts of more than one kind; every
clean, detached copy of a base in the ignored working directory of a checkout — it may remove the
copy of a cycle running at the same time; a script that removes a clean copy of a base for which it
finds no branch — with cycles running at the same time it would remove the copy of a running cycle
whose name matches no branch, and the gate of that cycle on its base would fail midway; the tip
being an ancestor of the target branch — the branch another cycle has just made, with no commit,
would pass as merged and the cycle that has just started would lose its directory; the age of the
directory — a heuristic on time that errs on a longer task; only directories below the repository's
own directory — the directories beside it stay for hand clearing; keeping the clause on the first
clearing of the directories that gathered before the script as the human's act, for a product that
first pins this version with directories already gathered — the clause would stay for a state that
ends with that first clearing; narrowing the sentence of WAY-13 to an operation that the change
holds — WAY-13 would stop reaching the cycle's own operations that cannot be undone outside the
change, and a new such operation would meet nothing that stops it.

### WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?

A file that git ignores does not count against a clean tree, so the script of WAY-375 removes a
directory that holds ignored files, and they end with it. For each directory the script marks for
removal it lists the paths git ignores in it outside the cycle's `.runs/` directory, leaving out the
caches a command makes again, so that a human who runs the script without `--apply` sees what
would end with each directory; the cycle's own run, which removes with `--apply`, waits for no one
to read the list.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-375
- **Verification:** tests: that an ignored file does not keep a directory from being marked for
  removal, that the paths git ignores outside the cycle's `.runs/` directory are listed for a
  directory marked and the caches are left out.
- **Origin:** none

*Rationale:* the files a repository ignores are those it does not keep — build output, installed
packages, a user's local settings — so to count them as changes would keep almost every directory of
a product whose dependencies and build output are ignored, and the human would clear those by hand
all the same. The listing is the price paid for not counting them: a local setting that matters is
lost with the directory, and a human who wants to know what would go runs the script without
`--apply` and reads the list. The cycle's own run does not wait for that reading: the cycle makes
the directories of its tasks, so the ignored files in them are what agents and tools left behind,
and waiting for each would hold the cycle whenever a tool leaves a folder of its own. The caches are
left out of the list because a command makes them again and the list would be mostly them.
*Rejected:* ignored files counted as uncommitted — it would keep nearly every directory of a product
whose dependencies and build output are ignored; the list moved into the record and the description
of the request — a new line that repeats in requests, and a removed file is gone all the same; the
cycle stopping before the removal where the list is not empty — it reverses the removal without a
word to the human that WAY-375 gives, and the cycle would wait at its start each time a tool leaves
a folder of its own.

### WAY-406 — Who walks through the running product the behaviour that a change's tests do not cover, and for which changes?

The author of a change walks through the running product, after the code and before the review,
the behaviour a user sees there that the change's tests do not cover, and states the walk in the
report the review reads; in a change made from a plan, the executor of each slice that alters such
behaviour walks through its slice, read against the passages of the task its handoff gives. The walk
is required for every change of behaviour that the user sees in the running product — a screen, an
answer of an API, a command in a terminal, data the product shows — and the author or the executor
judges whether its change is one and says so in its report. The walk follows the method that the
author's skill names, which takes its steps and the rules of the walk from the practices this
decision's rationale names.

Where the audit of the process shows an error that the author or the executor let through at the
walk, the walk moves to a stage of its own with a new agent; the fix of a review's findings does not
repeat the walk.

Where the foundation of the product settles no way to the running product, the walk is not
performed, with that reason in the report and in the description of the request, and the cycle does
not stop; the author or the executor still draws up the cases from the requirements of the task and
marks each as unchecked with that reason. A screenshot left unchecked for the same reason stands in
the description with the walk as one item, not two.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-164 · derives from WAY-100
- **Verification:** an agent compares the author's or executor's report, the review and the request
  with the decision:
  - complies: the author of a change that alters what an API answers walks through the running
    product by the way its foundation settles, with cases drawn from the requirements of the task
    and a last case for what it notices on the way, and reports the verdict of each case; where the
    foundation settles no way, it reports the walk as not performed for that reason and keeps the
    cases marked unchecked, and the description holds one item for the walk and the screenshot left
    unchecked; the executor of a slice that alters a screen walks through its slice, and the
    executor of a slice that only moves code reports that its slice alters no behaviour a user sees;
  - violates: the author of a change that alters what a command prints reports only that its tests
    pass; the executor of a slice leaves the walk to the executor of the last slice; the fix of a
    review's findings walks through the product again; a cycle stops because the foundation settles
    no way to the running product; the description shows the screenshot left unchecked and the walk
    not performed as two items.
- **Origin:** none

*Rationale:* a user sees behaviour in the running product that the tests do not always cover, and an
agent that finds what the tests leave out, plans the checking of it and gives a verdict catches an
error the tests let through. The author has the code and the task fresh and writes the report the
review reads, so the walk adds a part of one stage and no agent. The executor of a slice walks
through its own slice because the executor of the last slice knows only its slice and has a limit of
reading, so it would have to read the whole task, and the report shows the state between the slices
to the review of the whole change. Where no way to the running product is settled, an agent can
still draw up the cases, so the description carries a list and the steps for a check by hand, and
stopping the cycle would punish the product for a gap the human sees in the request. The fix does
not repeat the walk because it answers findings of the review that has read the walk. The return of
the walk to a stage of its own waits for an error the audit shows, since such a stage costs one more
agent at every change a user sees.
The method takes from a practice of testing one task that a team of the human who owns this process
uses, its skill `test-run`, which is in a team repository not open to a reader of this repository
(WAY-27): the preparation (the task, the change, the way to the product and whether the product
runs), what the change alters for the user and what shared code it touches, a scope of the
requirements of the task set against what the tests cover, a plan of cases with a column of what
checks each and a last row for what is noticed on the way, a widening of the plan only on a hard
signal from the run, a verdict for each case that names the layer where it decides, a step of what
was not checked, and the check that two measurements are comparable before a difference is called a
regression. From the
lessons of two courses, also not open to a reader of this repository, it takes a block of effects
outside the product that cost or cannot be undone unless the product settles a stand-in, a sentence
in the report of where behaviour that depends on a platform was checked, a measurement in code in
place of the model's reading of a screenshot, the naming of the tool that was missing for a case
that could not be checked, the record of a limitation and the evidence from the layer actually
checked when the browser does not work, and the reading of everything the user sees on the screen —
one lesson showed an agent that confirmed a server error and missed the message that a dialog of the
browser covered. These practices bind the walk only through this decision, and only in the task
cycle.
*Rejected:* the reviewer of the whole change walking through the product as an added step of the
review — the reviewer only reads, so it would have to start the product and build a state of data,
the dearest stage grows, and each bad result is a round of fix and a new review; a stage of its own
with a new agent and a new skill from the start — one more agent at every change a user sees and a
new stage wherever the process counts and lists its stages, the largest change of the three; no
walk — behaviour outside the tests stays unchecked in the running product, and the request does not
say what was not checked; the walk only at a change of a screen — cheaper, but the gap the walk is
for stays open: an API, a terminal, a flow; the walk at every change, an internal one too — a cost
with no gain, since for a rebuild of code with no change of behaviour the walk finds nothing; only
the executor of the last slice walking through the whole change — it knows only its slice and has a
limit of reading, so it would have to read the whole task; no walk in a change made in parts — the
largest changes stay without it; the whole `test-run` with its interactive mode, for use beyond the
cycle — a skill of its own, against the author's step. Left out of the practices: the tools of that
team, which the way the product settles replaces — its tracker, its client of an API, its browser
server and its search of logs; the record of a run kept in a file in a user's directory, which the
reports of the cycle replace; the column that names who executes a case and the interactive mode;
the pause for the approval of the plan; the closers — a bug report, an update of end-to-end tests,
the documents of the repository; the question to the human whether a symptom is known; the cleanup,
which WAY-373 gives.

### WAY-407 — Who approves the cases of the walk through the running product before it is made?

No one approves the cases of the walk before it is made, and the cycle does not stop for them. The
author of a change or the executor of a slice draws the cases from the requirements of the task, not
from the code alone, puts the plan and its results into the report the review reads, and the human
sees in the request what was not checked. The refinement of a task writes no list of inputs to try
into the task document.

- **Scope:** task-cycle, project-level
- **Based on:** none
- **Relations:** derives from WAY-227 · derives from WAY-238
- **Verification:** an agent compares the report of the author or the executor, the task document
  and the request with the decision:
  - complies: the author or the executor draws the cases from the requirements of the task and
    starts the walk with no one's approval, the plan stands in its report, and the request lists
    each case left unchecked; the task document of a change a user sees holds no list of inputs to
    try;
  - violates: the cycle stops to ask the human to approve the cases; the refinement of a task writes
    into the document the inputs a human gave to try, as the plan of the walk.
- **Origin:** none

*Rationale:* the first point of the human's review of a task's cycle is the request (WAY-227), and
the plan of the walk stands in the report that the review reads, so a check of the cases before the
walk would add a stop with no point of review to gain for it. The author or the executor draws the
cases from the requirements of the task, which the review can read against the plan, and a list of
inputs given by a human is a plan of tests in the task document, which the refinement keeps out
(WAY-238).
*Rejected:* the refinement of the task writing into the document the concrete inputs to try, given
by a human — each refinement of a task a user sees would gain one question more, and WAY-238 would
have to say that such a list is no plan of tests; it makes sense only once it shows that the agent
loses variants known only to the human; the cycle stopping for the human's approval of the plan —
against WAY-227, under which the human's first point of review is the request.

### WAY-408 — What does the author or the executor do with a case of the walk that fell wrong?

The author of a change or the executor of a slice corrects each case that fell wrong before the
review, and the correction gets a test at the lowest level that catches the error (WAY-239); each
disagreement with the task is an error to correct, not a remark in the margin, and a case that fell
wrong does not break off the walk. The report says what fell wrong, what was corrected and by which
test.

An error outside the task's scope that the walk finds is reported and not corrected, and the
description of the request puts each such error before the human, under *Fix or let through*, with
the question whether to make a task of it, which merging lets through; in this area this decision
prevails over WAY-289, under which the cycle puts before the human only what it judges will be felt.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-239 · narrows WAY-289
- **Verification:** an agent compares the report of the author or the executor and the request with
  the decision:
  - complies: a case of the walk falls wrong, the author finishes the walk, corrects the error with
    a unit test that fails before the correction and passes after it, and reports the case, the
    correction and the test; an error in a part of the product that the task does not touch is
    reported, not corrected, and the description asks under *Fix or let through* whether to make a
    task of it, whether or not the cycle judges that the user or the human will feel it;
  - violates: the author notes in the report that a screen differs from the task and leaves it to
    the review; a correction of a case has no test; the author corrects an error outside the scope
    of the task in the same change; the description of the request does not mention such an error,
    or leaves it out because the cycle judges it will not be felt.
- **Origin:** none

*Rationale:* an error the walk finds is an error of the work against the task, and a note in the
margin leaves it to the review, which costs a round of fix and a new review for what the agent
could correct before. The test at the lowest level keeps the error from returning at the cost of a
walk, which is dear to repeat (WAY-239). A case that fell wrong often shares a cause with another,
so the walk goes on and the diagnosis comes at its end, with the whole picture. An error outside the
task is not the agent's to correct, since the task does not ask for it and the review would read an
addition nobody asked for; the human decides whether it is worth a task. The judgment of what is
felt that WAY-289 gives would let an error the walk found and the agent was told not to correct drop
out of the description, so no part of it would reach the human; in this area the error goes to the
human whatever that judgment says.
*Rejected:* the author only reporting an error and the review deciding on the correction — an extra
round of fix and a new review each time.

### WAY-410 — What does an agent do when a test contradicts the requirement, or when it cannot pass the test by general code?

An agent that makes a change and meets a test that expects what the requirement of the task rules
out, or that it cannot make pass by code that meets the requirement for every input, writes no code
for the input of the test and does not change the test: it commits what it has and returns to the
orchestrator of the cycle a question that names the test, quotes the requirement and says what it
tried. A test that checks behaviour the task expressly changes is no such contradiction, and the
agent changes it, with its cause on the side of the requirement.

The orchestrator answers such a question only from the task, the spec, a decision or the sentence of
an invariant, quoting the passage that settles it, and where none of them settles it opens a blocked
draft request that holds the question under *Needed from you* and picks no reading of its own.

The executor of a slice that returns such a question gets no retry on a class higher, which narrows
the retry of WAY-229; where no source settles the question, the blocked draft opens at once.

- **Scope:** task-cycle
- **Based on:** claude-test-special-casing · impossiblebench-test-modification ·
  impossiblebench-abort-option
- **Relations:** derives from WAY-227 · narrows WAY-229
- **Verification:** an agent compares the agent's report, the cycle record and the request with the
  decision:
  - complies: an author whose test expects 180 for an input of 200, where the requirement says the
    discount never exceeds 10 percent, writes no branch for 200, leaves the test as it is, commits its
    work and returns a question that names the test, quotes the requirement and says what it tried;
    the orchestrator finds in the task the sentence that settles it and resumes the author with that
    sentence quoted, or, where the task, the spec, the decisions and the invariants say nothing,
    opens a blocked draft request with the question under *Needed from you*; the executor of a
    slice that returned such a question is not replaced by one of a higher class; a test that checks
    behaviour the task expressly changes is changed by the author, who names the requirement as its
    cause;
  - violates: an author writes a branch or a returned value for the input of the test; an author
    changes the expected value of a test to the code's output to turn it green; an author continues
    after meeting a contradiction and notes it in its report; the orchestrator answers such a
    question by the smallest reversible reading of the requirement; the cycle opens a blocked draft
    request for a contradiction that a sentence of the task settles; the executor of a slice that
    returned such a question gets a retry on a class higher.
- **Origin:** none

*Rationale:* the system card places the special-casing of a test where an agent has failed several
times to find a general solution, particularly where test cases present conflicting requirements, so
an agent that has no other way out adjusts the code or the test. The rule gives it the way out: a
question to the orchestrator, with the work so far committed, and no code and no change of the test
meanwhile. A test that contradicts the requirement is a question of what the task requires, not an
open design choice, so no attempt is discarded and no spec is written (WAY-135); only the task, the
spec, a decision or the sentence of an invariant settles what a task requires. The orchestrator
answers the agents' questions under the owner's delegation (WAY-227) and answers this one from those
four alone, since the smallest reversible reading would settle the requirement itself, which no
agent of the cycle may do. Where none of the four settles it, the code cannot proceed without the
human, so the cycle ends on a blocked draft request in which the human meets the question, as WAY-227
gives for a decision reserved to the human. A slice's executor gets no retry on a class higher
because a stronger model does not remove a contradiction in the requirement, while the retry resets
the branch to the slice's base and deletes the work of the slice. An option for an agent to hand a
task to a human lowered the cheating rate of two OpenAI models in ImpossibleBench and had a much less
pronounced effect on Claude Opus 4.1 (`impossiblebench-abort-option`); the decision takes the
quantified part of the finding across publishers, as WAY-85 gives, and its size is no promise for the
process's agents, which run on Claude models. The reason for the way out stands without it: an
agent that has none can only adjust the code or the test. The price: an orchestrator may read a
source wrongly and send the author an answer that the review of the result then judges; a cycle that
ends on a blocked draft leaves the work done so far unreviewed and the task waiting for the human; an
author may ask too early, and an unneeded question costs a turn.
*Rejected:* a third reason for returning without code, the attempt discarded — the work of the author
goes, and the designer of a spec cannot settle the requirement either, since it asks the
orchestrator and never the human: the same problem at a higher cost; a blocked request at once, with
no orchestrator — every contradiction, also an obvious one that the task already settles, stops the
cycle and costs the human a turn; leaving it as it is, the agent noting the contradiction in its
report and working on — it costs nothing today, but an author with no way out adjusts the code or the
test, and an option to hand the task to a human lowered the cheating of GPT-5 in ImpossibleBench
(`impossiblebench-abort-option`); only an explicit contradiction — an author that is stuck with no
contradiction in sight, and from whom code for one input comes, has no other way out than the
workaround.

## Review of a change

Who reviews a change, which findings are fixed or block, and how a reviewer grades a finding on the
foundation, the glossary or the structure of code.

### WAY-10 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation has no assessment of its own, in a product as in
the-way itself: an agent that did not make the change reviews the whole change, its foundation
entries and invariant tests included, against its task and the foundation, and a human reads the
section of the request's description for the human's decisions and accepts the change by merging
the request.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  task-cycle, agent-instructions
- **Based on:** llm-self-preference
- **Relations:** derives from WAY-03
- **Verification:** an agent compares the change with the decision:
  - complies: a change that rewords a decision and the invariant test deriving from it is reviewed
    on its whole diff by an agent that did not make it, and the human, reading what the section for
    the human's decisions puts before the human, the reworded decision in plain words and the
    changed test among it, merges it with no other assessment;
  - violates: the author reviews its own change to the foundation; a cycle requires an assessment
    of its own of a change's foundation entries before the merge; a change merges whose foundation
    entries no reviewer read.
- **Origin:** none

*Rationale:* the problem is a single executor that checks itself: a model judging what it wrote
favours it, so an agent that did not make the change reads it. That agent usually runs on the
author's model or on a model of the author's family, and the favouring is taken to belong rather to
a family of models than to one model, so the other agent removes the author's shared context and not
the favouring itself; the process has no reviewer from another provider, and the price is taken. An
error of the product shows where the code and the foundation meet, and the review of the whole
change reads both against the task; an assessment of the foundation apart from the code sees only
entries, so what it finds beyond the review are faults of form and of checks, which the tests and
the review of the whole change also meet. The reviewer reads the whole diff, while the human reads
the section that holds what the human has not yet accepted, since a diff the human does not read
accepts nothing.
*Rejected:* one independent assessor on a model other than the author's, which sees the diff
without the author's reasoning and names what of the change can be cut — a stage of its own in
every cycle that writes entries, reading entries without the code the review reads with them; a
panel of two assessors and a settler reading both orders — its cost per change outweighs what one
reader misses, and its uncertainty becomes questions for the human; a binding sentence that the
reviewer works on a model other than the author's — with the author on the strongest model the
reviewer would be a weaker one or one of another provider; the author assessing its own change — it
checks itself.

### WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?

In the review of the whole change on either route, a finding blocks when the reviewer grades it
Critical or Important and has not itself marked it as outside the task's scope, and a Minor finding
that the review lists and the reviewer has not marked so is fixed before the request opens — in the
fix that runs for the blocking findings or, where none blocks, in one fix of its own that WAY-162
bounds. A finding the reviewer has marked as outside the task's scope — a line of its list of what
it declined to judge, or a finding it describes as going beyond the task — is not fixed, whatever
its grade, and the request lists those findings in an item of their own and, in another, the Minor
findings that no fix made — those of the code reviews after the review of the whole change, those
of a slice review that the review of the whole change does not list, those a fix left, and those of
a fix that WAY-162 reverted — each with the reviewer's words and its place in the code, while the
human decides which findings outside the scope become new tasks and creates them. The orchestrator
moves no finding from one of these kinds to another.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-136 · derives from WAY-227 · derives from
  WAY-140
- **Verification:** an agent compares the cycle and its request with the decision:
  - complies: the review of a one-author change returns only Minor findings within the task, one
    fix takes them in, one review of that fix follows, and the request lists each Minor finding
    that fix left with the reviewer's words and its place in the code; the reviewer sets aside
    under "Declined to judge" a behaviour the task does not ask for, the request lists it in an
    item of its own, and the human creates a task for it; the final review of a planned change
    returns an Important finding and a Minor finding within the task, and one fix takes in both;
  - violates: the review of the whole change lists a Minor finding within the task and the request
    opens with it unfixed and no fix having run; a fix takes in a Minor finding the reviewer marked
    as outside the task's scope, one that only a slice review gave and the review of the whole
    change does not list, or one of a code review after the review of the whole change; the
    orchestrator rules on a line the reviewer declined to judge, or moves an Important finding
    within the task to the list for new tasks; the cycle adds a task to the product's backlog
    itself; the Minor findings no fix made stand only in the cycle's reports the request links to.
- **Origin:** none

*Rationale:* the grade a reviewer gives already says how much a finding matters, so taking it as
the line between what blocks and what does not adds no second label to the review and
leaves no finding without a place; a label given against the task would let a finding tied to no
requirement of the task pass as non-blocking. A minor finding left in the request costs the human
who merges a turn of conversation and a round of correction, each with a fix and a review of its
own, or a task of its own with a session of its own, to do work the cycle has the code open for;
fixed before the request opens, it costs a fix that runs anyway where a finding blocks, or one fix
and one review of it where none does. The price of that is a round that goes to polish, and a new
serious finding in a fix made for polish alone, which would block a request that was ready
without it; WAY-162 bounds the price by giving that fix up whole, so that the request opens on
the code the review accepted. A minor finding that no fix made stays within reach of the human who
merges, with the reviewer's words, and one the product's user or the human working with the process
will feel is put before the human in plain words (WAY-289); a list the request only links to is a
list nobody reads. A finding that
widens the work is a new piece of work rather than a repair of this one, and the reviewer, who has
no stake in closing the cycle, is the one to say which findings lie outside the task, since an
orchestrator sorting them could move an inconvenient finding out of the way of the blocked request.
The human creates the new task because each product keeps its backlog where it chooses (WAY-101),
and where that is outside the repository, a cycle makes no effect there beyond its own record
(WAY-140).
*Rejected:* the cycle leaving the small findings in the request, which asks in its section for the
human's decisions whether to fix them in the request or make a task of them — every request with
such findings then costs the human a turn of conversation and a round of correction, and a small
finding that nobody will feel never reaches the question; the small findings joining a fix only
where one runs anyway for a blocking finding, and the request asking as above where none does —
the same cost in every cycle without a blocking finding, and two behaviours of the cycle that
depend on the result of the review; the rule left as it was, no fix for Minor findings — it costs
nothing today, and every later request with small findings goes through the same turn and round;
a label of its own, blocking or not, that the reviewer gives each finding against the
task — a second scale beside the grade, and a finding tied to no requirement of the task would
pass as non-blocking; the orchestrator ruling on each finding — the agent that wants the cycle
closed decides to skip a repair; the Minor findings kept only in the cycle's reports the request
links to — nobody reads them; the cycle adding the new task to the product's backlog itself — where
the backlog lies outside the repository, that is an effect only a human makes; the orchestrator
judging each finding against the frozen task — it could move an inconvenient Important finding to
the new tasks and so get round the blocked request; the orchestrator returning a line the reviewer
declined to judge to the reviewer, with the requirement of the task that covers it — the
orchestrator would choose which lines the reviewer looks at again, the lever left to the reviewer
alone, while a behaviour the task requires that the reviewer set aside still reaches the human in
the request's list, whose reading is the remedy.

### WAY-162 — How does a code review of a task's change end when its findings block?

In every code review of a task's cycle — of a slice of its plan, of the whole change, of the
return step's commits, of the reconciliation with the target branch and of a change made for the
human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and
one review of that fix, and a new Critical or Important finding in the fix itself counts as one
that remains. Where a blocking finding remains after that review of the fix, no third round runs,
the orchestrator does not rule on it, no further slice is made, and the cycle opens a draft request
marked `blocked` that lists each remaining blocking finding with its place in the code and its
reason, what the fix tried, and the time, models and tokens the cycle has used so far, from its
record of stages, with the number of review rounds.

Where the review of the whole change leaves no blocking finding and lists Minor findings that
WAY-161 has the cycle fix, one fix takes them in and one review of that fix follows, and where that
review finds a new Critical or Important finding in the fix, the cycle reverts the fix's commits
with a commit of its own, so that they stay in history, runs no third round and opens the request,
not blocked, on the code the review of the whole change accepted, the request listing the Minor
findings the fix tried and the new finding with its grade and as the review of the fix found it. In
the code reviews after the review of the whole change, and for a Minor finding that remains after a
fix, the findings that do not block go unfixed to the request's lists as WAY-161 gives them.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-161 · derives from WAY-136 · derives from
  WAY-227
- **Verification:** an agent compares the cycle and its request with the decision:
  - complies: after the review of the fix of a one-author change an Important finding stays open,
    and the cycle runs no further fix and opens a draft request marked `blocked` with that
    finding's place and reason, what the fix tried and the cycle's cost so far; a slice whose fix
    leaves a blocking finding ends the cycle the same way, and its later slices are not made; a
    Minor finding of the review of the reconciliation with the target branch is listed in the
    request; the review of a one-author change returns two Minor findings only, one fix takes them
    in, the review of that fix finds an Important finding in the fix, and the cycle reverts the fix
    with a revert commit, has the gate run on the code the revert leaves as WAY-160 gives, and
    opens a request that is
    not blocked and lists the two Minor findings and the Important finding with its grade; a fix
    that ran for an Important finding and carried a Minor one ends with a blocked request when the
    review of the fix finds a new Important finding;
  - violates: the orchestrator rules on a finding left after the review of the fix and marks the
    request ready; a third round of fixes runs, on a slice or on the whole change; a new Important
    finding in the fix is left out of the blocked request because the findings it set out to fix
    were fixed; a Minor finding of a later code review stands only in that review's report; a
    request opens blocked for a new Important finding in a fix made for Minor findings alone; the
    commits of such a fix are taken off the branch by a reset instead of a revert, or part of the
    fix is kept; the new finding of a reverted fix is left out of the request's lists.
- **Origin:** none

*Rationale:* one fix and one review of it settle an ordinary piece of work; a finding that survives
the review of its fix shows a loop that further rounds do not close, and each further round costs
as much as the one before it. The orchestrator wants the cycle closed, so a ruling of its own on
what the reviewer still blocks would let a change the reviewer did not accept reach the request as
ready; the blocked request puts that call before the human, with what the fix tried and what the
cycle has cost, so the human weighs going on against its price. A new Critical or Important finding
in the fix is one the fix made, and counting it as remaining keeps a fix from trading one blocking
finding for another. The bound holds for a slice as for the whole change: rounds cost the same
there, and a later slice built on one its review did not accept would carry the finding forward.
The findings of later reviews that do not block reach the request as WAY-161's do, because a list
the request only links to is a list nobody reads. A fix made for Minor findings alone is polish on
a change the review has already accepted, and a serious finding of its own in that fix puts at risk
what was ready without it; giving the fix up whole, by a revert that leaves it in history, returns
the request to the code that was accepted at the price of the fix's work, and the Minor findings and
the new finding reach the human in the request's lists, who can make a task of them. A Minor
finding that remains after a fix leaves the change as acceptable as it was, so it does not block.
*Rejected:* a request blocked by the new serious finding in a fix made for Minor findings alone —
polish turns a request that was ready into a blocked one, and the decision and a turn of
conversation fall on the human; the cycle keeping the part of such a fix that the review accepted
and reverting the rest — the orchestrator would decide what stays, which WAY-161 forbids it; the
orchestrator ruling on the findings left after the review of the final fix — a change the reviewer
did not accept reaches the request as ready; up to five rounds of fixes on a
slice, the orchestrator ruling on what remains after them — each round costs as much as the last,
and the orchestrator rules in the end after all; a report of the remaining findings without a
request, in conversation or in the cycle record — the request is the one place where the human
judges the cycle's work, and a report in conversation is lost with the session; no bound for the
code reviews after the review of the whole change — the orchestrator would rule on the remaining
findings after all; the findings of those later reviews that do not block kept in their reports,
which the record links — a list the request only links to is a list nobody reads; one more round
for a finding the fix introduced — a fix could trade one blocking finding for another without end.

### WAY-263 — Which foundation mismatches are Important findings?

A reviewer grades as Important a finding that a change departs from a foundation
entry it writes or changes: the change's files do what the entry forbids, fail to
do what it requires, or restate it differently, including more broadly or
without a qualification.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-161
- **Verification:** an agent compares a review finding with the entry the change writes or changes:
  - complies: the reviewer grades as Important a finding that the changed code does what the entry forbids, omits what it requires, or that another changed file repeats the entry while broadening it or dropping a qualification;
  - violates: the reviewer grades such a finding as Minor because the code or repeated account says something different from the entry.
- **Origin:** none

*Rationale:* work that contradicts its own entry, or gives agents a second
account that changes that entry, leaves the request carrying incompatible rules.
Treating the second account as Minor allows later work to follow the broader rule
and keep the conflict alive.
*Rejected:* only work that directly departs from the entry — a repeated account
that drops a qualification can still guide later work by a broader rule; only
entries the change writes, not ones it changes — a changed entry can still
contradict the part whose wording remains; add the criterion to WAY-161 — its
general rule would carry a longer, more specific grading criterion; leave the
criterion only in the skill — the foundation would not hold it and a later
change could remove it without contradicting an entry.

### WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?

A reviewer grades as Minor a finding that a word needs a glossary entry, or that a word of the
process lacks the qualifier WAY-104 gives it in a product's foundation, unless the finding cites a
sentence the files hold that a reader would read wrongly for lack of it; a finding that cites such a
sentence is graded as any other. The renaming of a word with two meanings (WAY-99) is graded as
before, and a finding that a glossary entry the change writes or changes departs from a foundation
entry stays Important (WAY-263).

- **Scope:** task-cycle, glossary
- **Based on:** none
- **Relations:** narrows WAY-161
- **Verification:** an agent compares a review finding with the decision:
  - complies: a reviewer who thinks "secondary action" needs an entry and cites no sentence grades
    the finding Minor, and the fix for Minor findings (WAY-161) or the request's list takes it; a
    reviewer who cites "the form holds no secondary action" as a sentence read wrongly by a reader
    of the field grades it as any other finding; a finding that two meanings of a word are not
    renamed is graded as it was before this decision; a finding that a new glossary entry broadens a
    rule of a decision stays Important;
  - violates: a finding that a word lacks an entry, citing no sentence, is graded Important and
    blocks the change; a finding that cites a sentence read wrongly is graded Minor for being about a
    word; a finding that a glossary entry the change writes contradicts a decision is graded Minor.
- **Origin:** none

*Rationale:* whether a word needs an entry or a qualifier depends on which reader the foundation is
read by, and a remark with no sentence behind it cannot be checked, so as a blocking finding it
sends the change through a round of fixes for a matter the reviewer cannot show; as a Minor finding
it goes to the fix for Minor findings, where the author may contest it with evidence, and to the
request's list when the author contests it or no fix repairs it. A finding that cites a sentence a
reader would read wrongly can be checked like any other, and a glossary entry the change writes is a
second account of a rule that can broaden it, which WAY-263 already grades.
*Rejected:* the grade left to the reviewer without this limit — a dispute over a word returns as a
blocking finding and a round of fixes; every narrower meaning taking an entry, so that no dispute
arises — the glossary grows by words no one mistakes, the direction WAY-95 refused; a script naming
the candidates for an entry — WAY-95 refused it, since it cannot tell a definition from another
sentence; Minor always, also with a cited sentence — a collision shown on a sentence is then
repaired only by the fix for Minor findings of the review of the whole change, which the cycle gives
up whole when the review of that fix finds a new serious finding, so that in those cases, and for a
finding of a later review, the collision reaches the merge.

### WAY-363 — How does a reviewer grade a finding about the structure of code?

A reviewer grades as Minor a finding about the structure of code that lies below the threshold of the
rule of size in the product's coding guidelines, and every such finding in a product that has no rule
of size, whatever the reason: for example, it departed from the rule by a decision, it has no
coding guidelines at all, or its guidelines were written before the rule existed. The reviewer judges
its scope as for any finding (WAY-161). A finding about a function or a file over a threshold is
graded as any other finding.

- **Scope:** task-cycle, product-guidelines
- **Based on:** none
- **Relations:** narrows WAY-161
- **Verification:** an agent compares a review finding with the decision:
  - complies: a reviewer who finds that a change added forty lines to a function that stays under the
    threshold, or left a helper with no caller, grades each finding Minor, and the fix for Minor
    findings (WAY-161) takes in what the change itself left; a reviewer who finds that a script of
    a product that has no coding guidelines grew by forty lines in one function,
    or a product that departed from the rule of size by a decision, or whose guidelines were written
    before the rule and hold none of it, grades the finding Minor; a finding that a function the
    change pushed over the threshold stands over it is graded as any other finding; a finding about
    code from before the change, which restructuring would reach, goes to the request's list as a
    finding outside the task;
  - violates: a finding that a function grew but stays under the threshold is graded Important and
    blocks the change; a finding about structure in a product with no rule of size is graded
    Important and blocks the change; a finding about a function over a threshold is graded Minor
    because it is about structure; the orchestrator regrades a finding of structure or moves it
    between the lists.
- **Origin:** none

*Rationale:* whether a structure is good is a judgment, and a grade that follows it blocks or lets
through a change by the reviewer's impression, with the same chance in the grade that a remark on the
form of an entry shows (WAY-364). A Minor finding within the task is still fixed before the request
opens (WAY-161), so what the change itself leaves, such as code with no user and a name no longer
true, is repaired in the review of the whole change, and the finding is left out of the blocking only.
Where code stands over the threshold, a number settles it and not the reviewer's impression: the test
of the rule of size stops the change, and where the rule's invariant is marked violated, the review
that keeps a cleaned file or a new one from breaking it stops it (WAY-51). Where the product has no
rule of size there is no threshold and no such test, so the same reasoning leaves a finding of
structure Minor and not blocking. The reviewer still judges the scope of each finding, so a
restructuring of code from before the change reaches the request's list and not the fix.
*Rejected:* the reviewer grading findings of structure as any other — a finding of structure can
block the change and give a round of fixes on the reviewer's impression of the structure;
findings of structure always outside the task's scope, on the request's list and for the
review of the foundation — code with no user and a name no longer true, which the change itself
left, are cleaned only by a separate task after the review of the foundation, a full cycle; the
finding graded as any other where the product has no rule of size — with no threshold a finding of
structure can block the change on the reviewer's impression and give a round of correction.

### WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?

A reviewer grades as Minor a finding that a foundation entry departs from the form of its template,
where the entry's content agrees with the code, unless the finding cites a sentence a reader would
read wrongly through the departure; a finding that cites such a sentence is graded as any other. A
finding that the content of an entry does not agree with the code stays Important (WAY-263).

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** narrows WAY-161
- **Verification:** an agent compares a review finding with the decision:
  - complies: a reviewer who finds that a decision's *Origin* names a task document, while every
    sentence of the decision agrees with the code, and cites no sentence read wrongly, grades the
    finding Minor; a reviewer who cites the sentence of a rationale that holds a rule a reader would
    take as binding, and shows how it is read, grades the finding as any other; a finding that an
    entry says what the code does not stays Important;
  - violates: a finding of a departure from the form that cites no sentence is graded Important and
    blocks the change; a finding that cites a sentence read wrongly is graded Minor because it is
    about form; a finding that the content of an entry disagrees with the code is graded Minor
    because the entry's form is also off.
- **Origin:** none

*Rationale:* the same remark on the form of an entry was graded blocking in 9 runs of an experiment
with reviewers and Minor in 8, and 6 of its 32 runs rejected the change for its form alone (the
measurement is this product's own, and its record is not open to a reader of this repository; its
conditions stand in WAY-229), so the verdict depended on the run. Graded always Important, every
departure from the form is a FAIL and a round of fixes, and a fix that fails leaves the request
blocked for form alone (WAY-162); graded always Minor, a departure that makes a reader take an entry
wrongly, such as a binding rule written in the rationale and not in a binding sentence, would not
block and would not be repaired in the reviews after the review of the whole change. A Minor finding
within the task is still fixed before the request opens (WAY-161), so the departure is repaired, and
the grade changes three things: the verdict, a pass where a fail stood; the result of a failed fix,
which reverts and leaves the request unblocked; and the lot of the finding in later reviews, where a
Minor finding goes to the request's list and is not fixed. A mismatch of content with the code stays
Important, since a request carrying it carries a rule the code does not keep (WAY-263).
*Rejected:* a departure from the form always Minor — a departure by which a reader reads an entry
wrongly, such as a binding rule in the rationale and not in the binding sentence, would not block and
in reviews after the review of the whole change is not repaired; a departure from the form always
Important, that is, blocking — every departure from the form is a FAIL and a round of fixes, and a
fix that fails leaves the request blocked for form alone (WAY-162), which in the experiment would
have reached 6 of 32 runs.

### WAY-409 — What does a reviewer do about code of the product that passes a test without meeting the requirement?

A reviewer looks, in every code review of a task's cycle — of a slice, of the whole change, of a fix,
of the commits of the return step, of the reconciliation with the target branch and of a correction
— in the code of the product that the change touches, for code that passes a test without meeting
the requirement the test stands for: a branch or a returned value made for the very input a test
uses, the expected value of a test written into the code of the product, a comment that names a
special case for a test, and a change to the outcome of a comparison that a test makes, with no
change to the test, such as an overloaded comparison operator. A reviewer grades such a finding
Important at the least, so that it blocks (WAY-161), and only code whose branch, value or comparison
exists to make a test pass is the finding; a special case that the requirement itself asks for is
none.

The rule stands in the skill of the review and in no product's guidelines, so that it holds in every
cycle, whether or not the product has adopted the template of the testing discipline.

- **Scope:** task-cycle
- **Based on:** claude-test-special-casing · impossiblebench-test-modification ·
  impossiblebench-cheating-strategies
- **Relations:** derives from WAY-13 · derives from WAY-161
- **Verification:** an agent compares a review with the decision:
  - complies: a reviewer finds that a function of the product returns 180 for the input 200 that a
    test uses, where the requirement gives a general rule that would not return it, grades the finding
    Important and the review fails; the same for a branch under a comment that says "special case for
    the test", and for a comparison operator overloaded so that the comparison a test makes comes out
    true; a product whose guidelines hold no testing discipline gets the same look; a branch on a
    value that the requirement itself names is no finding;
  - violates: a reviewer reads the files of tests and leaves the code of the product unread for this;
    a finding of such code is graded Minor and the change passes; a reviewer reports every special case
    of the product's code, the ones the requirement asks for among them; a review of a fix or of a
    correction leaves the look out.
- **Origin:** none

*Rationale:* an agent that a red test stands in the way of can turn it green in two ways, by changing
the test or by making the code give the answer the test expects. What keeps a test as it was
(WAY-233) closes the first; the second leaves the test whole and green while the requirement stays
unmet, so only a reader of the product's code who did not write it finds it (WAY-13), and the human
who merges on the green tests does not. The system card of Claude 3.7 Sonnet found that model
returning the expected test values directly and often marking such cases with a comment, and
ImpossibleBench found that making the tests read-only does not remove special-casing or operator
overloading, three of its four strategies being ones that comply with an instruction not to modify
tests, so a review that guards only the files of tests leaves most ways open. The signals are those
the card and the paper name: a comment about handling for a test, a value or a branch for the input
of a test, a comparison that returns what a test wants. Only code whose branch, value or comparison
exists to make a test pass is the finding, since a reviewer asked to judge every special case of the
product's code would report each rule the requirement asks for, and a finding that is often wrong
costs a round of fix each time. It is graded Important at the least, as a missed requirement that
the green tests hide. The rule is the reviewer's way of reading and no rule on the content of a test
file, which is why it stands in the skill of the review and not in the template of the testing
discipline (WAY-231), which binds only a product that has adopted it. The price: the reviewer judges
intent from the code, so a workaround that no signal names, such as recording extra states to answer
differently for the same input, may pass; a value that the code returns for the input of a test and
that is also right may be reported and has to be contested; and the look costs the reviewer's time in
every review.
*Rejected:* the rule in the template of the testing discipline — it works only in a product that has
adopted the template, and it is no rule on the content of a test file, since the test stays untouched
while the code cheats; leaving things as they are — it costs nothing today, since no case is known
from the 83 task cycles of the process's author counted in his register of problems of 2026-11-12
(his own record, not open to a reader of this repository), but the first case passes the review
unseen.

## The request and the human

Where the human meets a cycle's work, what a request's description puts before the human and in what
language, the screenshots it shows, and the process remarks of the cycle.

### WAY-227 — Where does the human meet a task cycle's work?

The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under
the task owner's delegation, never recording these as human approval, and brings the request to the
human, the cycle's first point of human review. Decisions reserved to a human by the foundation
remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft
request.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-13
- **Verification:** an agent compares a cycle with the decision:
  - complies: the request shows the orchestrator's provisional choices without claiming the owner's
    approval; a cycle whose code needs a decision the foundation reserves to the human opens a
    blocked draft request;
  - violates: an agent treats its own spec approval as the owner's; the cycle stops between stages
    to ask the human for an approval a stage asks for.
- **Origin:** none

*Rationale:* the request is where the human judges the cycle's work, so an approval a stage asks for
is the orchestrator's provisional one.
*Rejected:* a workflow with intermediate human gates — it would interrupt the delegated cycle.

### WAY-287 — What does a request put before the human for a decision?

The section of a request's description for the human's decisions holds everything whose merge needs
the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks
not run, the incomplete reading of the review of the whole change where its reviewer did not read
the index of its whole selection or itself named a decision concerning the change as unread, and the
gap was not closed on the way by that reviewer, or a fresh one, reading what stayed
unread, the unfixed findings the product's user or the human working with the process will feel, the
decisions of the task's own sections, in a blocked request what the cycle needs to go on, the human
actions, the changed invariant tests, surfaces and *Violated* marks, the additions a change makes to
a product's logging scope, a listing of the remarks check that the cycle holds wrong (WAY-295), an
error of the form check that the cycle holds wrong, the pairs that give the cause of a
correction after the request opened, each descriptive `TODO` in an
invariant's *Rests on* or *Derives from* or in a decision's *Based on* or *Relations* that stands on
the main branch after the change (WAY-71), and the foundation entries the human did not see at the task document — in
three groups, headed *Needed from you*, *Fix or let through* and *You accept by merging*, in this
order: what the request cannot go on without, an answer or an action of the human; what the cycle did
not do or did not fix and can still be done in this request, which the human has done there, makes a
task of or lets through; and what the cycle did within its authority, which the human accepts by
merging and which waits for no separate answer. Every group stands, reading `none` where it holds no
item, the items are numbered in one run through the three groups, and the section reads `none` alone
where no group holds an item, which says that nothing else in the request waits for the human's yes.
A blocked request keeps the same skeleton, with `blocked` in its first sentence and what the cycle
needs, in plain words, and the stages it did not run because it stopped, under *Needed from you*,
while each remaining finding stands with its place in the code in the lower part.

Another decision may add a kind of item to one of the three groups, naming the group, and the
template of a request's description lists every kind.

- **Scope:** task-cycle, agent-instructions
- **Based on:** none
- **Relations:** derives from WAY-227
- **Verification:** an agent compares the request's description with the decision:
  - complies: a request whose cycle chose the place of a new file the task left open, skipped the
    return step on the human's word and left a finding a player would feel puts all three in the
    section, the skipped step and the finding under *Fix or let through* each with its question and
    the choice under *You accept by merging* with its reason and no question, and the lower part
    keeps their evidence; a request that needs no answer and has no choice beyond the task reads
    `none` alone in the section; a request with one choice beyond the task and nothing else keeps
    all three headings, with `none` under the first two; a request whose
    cycle holds a listing of the remarks check wrong, or an error of the form check wrong, names it
    in that section; a request after a correction made for a remark of the human puts one sentence
    in *You accept by merging* that says the correction answered the remark and whether the cycle
    judged that the task required what the correction changed, so the section does not read `none`;
    a request a remaining finding blocks says in that section, in plain words,
    what the human is to decide about it, and names the return step and the reconciliation it did not
    run under *Needed from you*, while the finding's place and reason stand in the lower part; a
    request whose reviewer of the whole change read 40 of the 151 decisions of its selection whole
    and did not read the index of the other 111 puts that under *Fix or let through*, asking
    whether to have what stayed unread read in the request, make a task of it or let it through,
    and so does a request whose reviewer read the index of all 151 and named two decisions bearing
    on the change as unread, while a request whose reviewer read the index of all 151, opened 40 of
    them whole and named no decision of the change as unread has no such item; a request whose
    merged tree holds an invariant that reads
    `Rests on: TODO — the store of documents, once a task chooses it`, written by the change or
    standing from before, puts it under *Fix or let through* with the rule of that invariant and the
    missing store, and so does a request whose merged tree holds a decision that reads
    `Based on: TODO — the source of the save format` or an invariant that reads
    `Derives from: TODO — the decision on where saves live, expected in the save task`, each with
    what is missing; a value that names a fact the foundation holds and then
    `TODO — a second fact, from the vendor` is one gap, shown with the second fact alone;
  - violates: the section reads `none` while a choice beyond the task stands only among the
    foundation entries; a decision adds a kind of item to the section without naming the group that
    takes it; a group with no item is left out, or its heading stands with nothing under
    it; the numbering of the items starts again in each group; a choice the cycle made within its
    authority stands under *Needed from you*, or ends with a question that waits for an answer; a
    skipped step is named only in the last line of the checks; a blocked
    request is written in a shape of its own; the incomplete reading of the review of the whole
    change stands only in the lower part, or stands in the section in every request whatever the
    reviewer did; the section reads `none` after a correction, or the sentence of the correction's
    pairs stands only in the lower part; the section reads `none` while an invariant's *Rests on*
    or *Derives from* or a
    decision's *Based on* or *Relations* holds a descriptive `TODO` on the merged tree, or such a gap
    stands under *Needed from you* or under *You accept by merging* with no way to answer it.
- **Origin:** none

*Rationale:* the human merges once the section that asks for decisions reads `none`, so a matter that
needs a yes and stands in another section passes without the human's knowledge. One section that
holds every such matter makes its `none` a statement the human can merge on. A blocked request that
keeps the skeleton is read the way every other request is read, and what the cycle needs is the
question it asks, under *Needed from you*. Additions to a product's logging scope come here because WAY-274 counts on the
human seeing them at the merge, and this section is where the merge shows them. A review of the
whole change that did not read the index of all it selected, or that names a decision bearing on
the change as unread, passes as a full review unless the human is told, and the human is the one
who can decide to merge on a partial reading; a decision known from the index and not opened whole
is the reading WAY-150 gives, so it asks for no yes, and the section keeps its `none` for requests
that can be merged. The cause of a correction stands here
because the judgment whether the task required what the correction changed is the cycle's own, and
the merge is where the human sees it. A descriptive `TODO` that stands in
an invariant's *Rests on* or *Derives from* or in a decision's *Based on* or *Relations* once the
change is merged is a gap on the main branch that the merge leaves, so it stands under *Fix or let through* with what
it names as missing, for the human to have the missing thing written in the request, make a task of
it or let it through (WAY-71); while an old gap stands, every request carries it. In one list, what
the request cannot go on without, what the human can still have done in it and what the merge
accepts look alike and end in a similar question, so the human answers all of them in one way, or
reads none, and the matter that needs a real decision is lost among the rest; three groups put the
criterion of each before the human, and a group that always stands lets the human tell a group with
nothing in it from one that was forgotten. The list above is the base: a decision of its own, such
as WAY-308 for the relation line it cleaned and WAY-316 for the screenshot it does not show, adds a
kind of item to the section, and a sentence that lets a decision do so by naming the group spares
this entry a change for each one, while every new kind still needs a decision of its own.
*Rejected:* B. Change WAY-274 so that it does not count on the human seeing additions at the merge.
That brings back the option WAY-274 itself rejected, the principle alone, with the list unseen and
new items entering without the human, and it changes the meaning of a decision already accepted.
C. Leave the rule as it is. Additions to the logging scope keep entering without the human's
knowledge, and WAY-274 describes a mechanism the product does not have; a reviewer comparing a
change with WAY-274 would count its complies as met. A general item for everything a decision asks
the human to see at the merge. It would encourage moving everything into the section, though its
`none` is to mean the request can be merged. A search of the log by the words "at the merge",
"sees" and "merges" finds WAY-308 and WAY-316 as further cases, each with a kind of item of its own;
that is a word search, not proof. Weighed again on those cases, the general item stays rejected: it
would still move everything a decision asks the human to see into the section, whereas a kind that
a decision adds in a group it names keeps the `none` of the section a statement that the request can
be merged. Listing both kinds in this entry's sentence — two more enumerations in a long sentence,
and the next decision that adds a kind must change this entry again, a forgotten change giving the
same gap between the decision and this entry. A sentence of the top part outside this section on the
incomplete reading — an incomplete review would pass without the human's yes, with a note in a place
the template gives to something else; the lower part, in the section of the checks — the human does
not read it, so would still not know that the review was incomplete. The skipped steps and unrun
checks, the proposals not applied and the incomplete reading of the review in one group with what
the request cannot go on without — a skipped step is a matter of doing it here or letting it
through, so the group would mix two matters; only the groups that hold an item — shorter, but a
group with nothing in it cannot be told from a forgotten one, by the human or by the script; three
sections of the description in place of the groups — it changes the skeleton of the request's
description and every reference to the section, and gives the human nothing beyond headings in one
section; bold lines in place of headings — they look the same, but the script cannot tell them from
plain text and checks nothing.

### WAY-288 — In what language is a request's description written?

A request's description is written in English, and its top part stands a second time, in the
language of the task document, in a collapsed block of the description.

Where the task document of a request is in English, the collapsed block of the request's description
holds `none` in place of a second English copy of the top part, and the form check, wherever it
reads the task document as English, holds the block to `none`.

- **Scope:** task-cycle, agent-instructions
- **Based on:** github-collapsed-section
- **Relations:** narrows WAY-114
- **Verification:** an agent compares the request's description with the decision:
  - complies: a request of a task written in Polish reads in English, and its collapsed block holds
    its state, what the human will see, the human's decisions, the cost and how to merge in Polish;
  - violates: a request opens in Polish; the human's decisions stand in English alone; the block
    holds the lower part as well, or a summary of the top part instead of the top part.
  For the block where the task document is in English, an agent compares the request's description
  with the decision:
  - complies: a request of a task written in English keeps the block, its summary followed by
    `none`, and the form check passes it; wherever the form check reads the task document as
    English, it reports a block that repeats the top part;
  - violates: a request of an English task drops the block; its block repeats the top part in
    English; a request of a Polish task holds `none` in its block.
- **Origin:** none

*Rationale:* the repositories are public, so what anyone may read is in English, while the human
reads a long English text line by line and so not at all; the part the human reads stands a second
time in the language the task was written in, and stays collapsed, so the request opens in English
for every other reader. The block exists for a human who reads a long English text line by line;
where the task document is in English, that human reads the top part above it, so a second English
copy only doubles what the request shows. The block keeps its place with `none`, so the skeleton
stays the same for every request and the form check can tell a block left out from one that has
nothing to repeat.
*Rejected:* the whole description in English, as before — a long English text the human reads line
by line, so not at all; the top part in Polish and the lower part in English — a public request
opens in Polish; a report in Polish in the human's notes — the cycle writes nothing outside the
repository, and the human would look in two places; the top part repeated in English in the block —
a copy that buys the reader nothing; the block left out for an English task — the skeleton would
differ by the task's language, and a missing block could not be told from one that was forgotten.

### WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?

Writing a request's description, the orchestrator of the cycle judges each unfixed finding — a Minor
finding that no fix made, a finding outside the task's scope and the new Critical or Important
finding of a fix that WAY-162 reverted — from the whole cycle record, the reports of the walk
through the running product and its screenshots included, by whether the product's user or the human
working with the process will feel it, and restates each that will be felt, in plain words, in the
section for the human's decisions, under *Fix or let through*, as one question with the answers to
fix it in this request, to make a task of it or to let it through, which one answer may settle for
the whole list. The answer to fix it runs a correction with one fix and one review of that fix; the
same answer is offered for a step or a check the cycle skipped, a proposal of the task's own
sections not applied, an incomplete reading of the review of the whole change and something an entry
stands on that the foundation does not hold yet, and runs the step or the check, applies the
proposal, has a fresh reviewer read what stayed unread or has the missing fact, decision or source
written, and what the correction leaves unfixed or undone, like whatever cannot be done in the
request at all, is put by the request only with the question whether it becomes a task, which the
human who makes none lets through by merging, or stays in the lower part, so that the loop ends
after one correction. Every finding stays in its list of the lower part with the reviewer's words
and its place in the code, and the judgment changes no finding's kind or grade and decides no fix
and no block.

- **Scope:** task-cycle, agent-instructions
- **Based on:** none
- **Relations:** derives from WAY-161 · derives from WAY-287
- **Verification:** an agent compares the request's description with the decision:
  - complies: a Minor finding that a button stays enabled while a save runs and that no fix made is
    restated as "a player can press save twice while the game saves; fix it in this request, make a
    task of it or let it through?", and stays in the list of Minor findings with the reviewer's
    words; a finding on the name of a helper stays in its list alone; after the human answers that
    the findings are to be fixed, a correction makes one fix and has it reviewed once, and a Minor
    finding of that review is put with the question of a task alone; the return step that was
    skipped is put with the same answers, and the answer to do it in this request runs the return
    step in a correction;
  - violates: the orchestrator moves a finding it judges felt to the blocking ones, or leaves out of
    its list one it judges not felt; a finding a player would feel stands only in the lower part; a
    skipped step is offered only the answers of a task or a let-through while it can still be run in
    the request;
    the restatement names a file and a line instead of what the player meets; a finding left
    unfixed by the correction that the answer to fix it ran asks again for a fix, or the correction
    runs a second fix for it.
- **Origin:** none

*Rationale:* the reviewer's words name the code, and the human cannot tell from them what was left
unchecked and how much it matters, so a finding the user or the human will feel is lost unseen in
the lower part. The orchestrator holds the whole record, the walk through the running product
included, while the reviewer reads the code and the task, so the orchestrator sees the effect a
finding has. WAY-161 warns that an orchestrator sorting findings could move an inconvenient one out
of the way of a blocked request; this judgment only adds a line before the human, and a finding
judged not felt stays where WAY-161 puts it, so nothing WAY-161 keeps in front of the human leaves
it. The clean-ups stay in the lower part for a reading of the lower parts of many requests together.
A human who wants a finding fixed at once has an answer for it in the question, where without one he
answers against the question and the cycle has no rule for it; one answer may cover the whole list,
so that a human who wants all of it fixed answers once. A step or a check the cycle skipped, a
proposal not applied, a reading of the review left incomplete and a fact, decision or source that an
entry stands on and the foundation does not hold are things the cycle left undone and can still do
in the request, so the same answer serves them and the human has no second way to ask for them. The
correction that answer runs brings findings of its own, and a second fix for them would raise the
same question without end, so what the correction leaves goes only with the question of a task, or
stays below. The findings nobody will feel stay out of the question, since the `none` of the human's
section says that nothing waits for a yes (WAY-287), and those within the task that the review of
the whole change lists have been fixed already (WAY-161).
*Rejected:* the question as it was, only whether the finding becomes a task — a human who wants the
fix at once answers against the question, and the cycle has no rule for the answer; the same
question for the findings nobody will feel as well — the human's section swells with cosmetics,
though its `none` is to mean that nothing waits for a yes (WAY-287), and the cycle fixes the
cosmetics within the task that the review of the whole change lists anyway; every finding in the
lower part alone — the findings a player would feel are lost unseen, since neither the human nor the
nightly review reads them; the nightly review of the layer of agent instructions extended to the
review findings — that review would start carrying the product's bugs, and the clean-ups would flood
its ledger; the reviewer who reports the finding judging it — it looks with fresh eyes, but reads
the code and the task and does not run the product.

### WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?

Before every commit that adds the cycle record to the product's repository, the orchestrator runs
the-way's script that lists each item other than `none` under **Searches not found or unclear** in
the record's stage reports — the `.md` files of the cycle's `reports/` directory whose name holds
neither `handoff` nor `findings` — that the record's process remarks do not hold word for word,
appends each listed item word for word with its stage name and full report path, and runs the script again until
it lists nothing. The commits that add the record are its copy for a request, the repetition of that
copy in a correction after review, and the copy of a request blocked for any cause. The script only
lists, and an item that two reports give is listed again until the remarks hold it twice; a report
without the section gives no item and does not end the script with an error, which narrows WAY-344
for the reports this script reads.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-260 · narrows WAY-344
- **Verification:** an agent compares a cycle and its record with the decision:
  - complies: a stage report that works after the request opened gives one item beside three lines
    reading `none found`; the script lists that item with its report path, the orchestrator appends
    it and runs the script again, which lists nothing, and only then the record is committed; a
    correction runs the script over the reports of the correction too; a report named
    `review_whole.md` and one named `planner-report.md` are read, while `01-author-handoff.md`,
    `slice-1-findings.md`, `notes.txt` and `gate.log` are not; a report with no section lists
    nothing, and the script exits with 0 when no other report lists an item;
  - violates: a record is committed without the script having been run on it; the orchestrator
    stops after a run that listed items; it appends an item in other words, or leaves it out
    because it looks small; an item that two reports give stands once in the remarks; a `.md` file
    of `reports/` whose name holds neither word is left unread, or a handoff or a file of findings
    is read as a report; the script ends with exit code 2 at a report that has no section.
- **Origin:** none

*Rationale:* the orchestrator copies an item when it has a report in front of it, and in the cycles
examined when this was settled items were still missing from the remarks, from two causes: a stage
that works after the request has opened, which no step of the cycle told the orchestrator to copy,
and an item standing beside lines that read `none`, which a reading that stops at `none` passes
over. A comparison made by a script reads every report to its end every time, and a cycle with
dozens of reports is where a reader's care already failed. The nightly review of cycles makes its
cases from the record alone, so an item that is not in the record never reaches the human who
improves the process. The price is a script with tests, a longer end of every cycle, a section the
script must recognise in the two forms reports give it, and a literal reading of "other than
`none`": a line that reads `none found` enters the remarks, so the review gets more noise. A report
is told by its name lacking the two words that mark the files the cycle names otherwise, a handoff
and a file of findings, so a report under any other name is read and none is passed over unseen; the
price is that a handoff or findings file written under a name without those words is read as a
report. A report without the section is no failed reading: a stage report that returns `questions`
may lack the section, and the cycle's reports also hold files of the orchestrator, which need not
have one. A stage report that lacks it is returned to its agent for repair by the orchestrator,
which is where a missing section is caught.
*Rejected:* an exit code of 2 where no report is read — it does not catch the case where some of
the reports are read and others are not, and it goes against the rule of the cycle that exit 2
means no listing was made; a line in the listing that marks a file not read — it looks like an item
to append to the remarks; the orchestrator appends items to the remarks right after each report, a
correction included — a few sentences in the skill, but it does not close the gaps for items standing beside
`none` lines, which arose while the orchestrator had the report in front of it; a pass of the
orchestrator through all reports before every archive, skipping only a section that reads `none`
throughout — a few sentences that close both causes, but it still rests on a model reading with
care, which already failed in a cycle with dozens of reports; an exit code of 2 at a report without
the section, as WAY-344 gives — it would stop the record of every cycle whose reports hold a file
without the section, and of a cycle whose stage report returns `questions`; no exception at all,
with WAY-344 unchanged — a reviewer who compares the script with WAY-344 would take it for a breach.

### WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong?

Where the orchestrator of a cycle holds a listing of the remarks check of WAY-294 to be an error of
the script, with evidence it can name, the record is archived all the same and the script is not
changed in that cycle: the orchestrator enters the case in the record's process remarks as a case of
the script, not as an item of its stage, and names it in the request's section for the human's
decisions. In that case the repeated run of WAY-294 does not hold the archive back.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** narrows WAY-294
- **Verification:** an agent compares a cycle and its request with the decision:
  - complies: the script lists a line of a report that is no item, the orchestrator names the
    passage of the report that shows it, the record is archived, the process remarks hold the case
    as a case of the script, and the request's section for the human's decisions names it;
  - violates: the orchestrator changes the script in the same cycle; it holds the archive back until
    the script stops listing; it appends the listed line as an item of its stage to silence the
    script; it leaves the case out of the request; it holds a listing wrong with no evidence it can
    name.
- **Origin:** none

*Rationale:* a script that does not stop listing leaves the orchestrator either stuck or judging the
listing wrong itself, with a quiet return to the reading by a model that the script replaced. A case
named in the record and in the request reaches both readers: the nightly review of cycles, which
reads the record, and the human, who reads the request and decides by merging. The script is not
changed in the cycle that meets the case, so a cycle never loosens the check that judges it. The
price is that a real item the orchestrator wrongly holds wrong reaches the remarks only as a case of
the script, and the review does not see it as an item of its stage.
*Rejected:* no separate rule — the orchestrator gets stuck because the script does not stop listing,
or holds the listing wrong itself and quietly returns to reading by a model; the item the script
points at goes into the remarks as an item of its stage whatever the orchestrator judges — the
source of the decision keeps no reason beside it.

### WAY-300 — When does a request tell the human that the foundation waits for a review?

At the end of every task cycle the orchestrator counts the merges to the main branch since the last
review tag, and from the threshold of the reminder script on, the description of each request the
cycle writes says, in its part for the human who merges, that the foundation waits for a review.
The reminder blocks nothing, the threshold is one number for every product, which no product sets
for itself, and a repository with no review tag counts from the start of its history.

From the threshold on, the orchestrator reads the product's backlog for an open line of the review
of this repository — a line whose name holds the name of the skill `review-foundation` and the name
of the repository, which is the same in every cycle, open as the rules of the task place say
(WAY-107). Where no such line stands, or the backlog cannot be read, the sentence asks the human to
add the task of the review and gives what its name holds, the number of merges, the tag of the last
review and the skill that starts the review; where the line stands, the sentence points to it and
does not urge. The cycle adds and changes no line of the backlog (WAY-140).

- **Scope:** task-cycle, foundation-review
- **Based on:** none
- **Relations:** derives from WAY-24 · derives from WAY-107 · derives from WAY-140
- **Verification:** invariants: review-tag-pattern. tests: the count of merges to the main branch
  since the nearest review tag, from the start of the history where none stands, with the merges of
  the main branch into task branches left out; that the reminder line of the script turns to yes at
  the threshold and not one merge before it, and that the script gives one threshold. An agent
  compares the cycle and its request with the part no test holds:
  - complies: a cycle that ends at the threshold with no open line of the review in the backlog
    ends *How to merge* with a reminder that asks the human to add the task, names what its name
    holds, the number of merges, the tag and the skill, and the request merges like any other; the
    same cycle with an open line whose name holds `review-foundation` and the repository's name
    ends *How to merge* with a sentence that points to that line and does not ask; where the
    backlog cannot be read, the sentence says so and asks as it does for a missing line; a cycle in
    a repository with no review tag and a count below the threshold writes nothing about a review;
  - violates: the reminder stops the merge or fails a check of the gate; a product sets a number of
    its own; the count starts at the merge of the review's own change; the reminder is written
    only in the first request after the number is reached; the sentence urges while an open line
    of the review stands; the cycle adds or changes a line of the backlog.
- **Origin:** none

*Rationale:* the end of the cycle is the point every product passes, and the request is where the
human already reads before a merge, so the reminder asks the human for no habit of their own and
needs no memory or ritual that a product may lack. A reminder that stops nothing is read, where a
failing check would stop changes that have nothing to do with it. A reminder that repeats its ask
while the human has the review planned is scrolled past, so the cycle reads the backlog and stops
asking where the line stands; the human adds the line because each product keeps its backlog where
it chooses and the cycle only reads it (WAY-140, WAY-161), and a name that holds the skill and the
repository is a mark that can be written in any backlog with no identifier for the-way to issue.
Weak points taken: everyone with access to the repository sees the tag; the sentence asks until a
human adds the line; a backlog the cycle cannot read leaves it asking for a line that may stand
there; and a line that holds the mark but is no review of the foundation silences it. The number is
one for every product so that no product has a rhythm of review of its own, and it stands in the
code that counts, with its reason beside it, since a single number carries no choice that a later
reader could take otherwise (WAY-22).
*Rejected:* a check in the gate — the gate stops or lets through, a stop would block unrelated
changes, and a warning that stops nothing is not read there; a script the human runs, in a weekly
review say — it depends on a memory or a ritual that another product does not have; the merge of
the review's own change as the marker instead of a tag — a review that changes nothing leaves none,
and the count goes back to the start of the history; 10 merges, as an outside harness runs its
quality review — a review session of the human every week in the-way, running into the daily scan,
where there the ten concern a cheap review of quality and no session of a human; the cycle adding
the line of the review to the backlog itself — the backlog is the human's and lies outside the
repository, and it would need a change to WAY-140 against the reason of WAY-161; holding the request
as a draft from the threshold on — every unrelated change would wait for a click that becomes a
reflex at more than ten merges a week; the line in the backlog and the held draft together — the sum
of both costs; a sentence that asks for no line and says nothing of the backlog, the human's own
setup adding the line — another user of the-way keeps a sentence that can be scrolled past; an
identifier the-way computes for the review's line, in the field of identifier — a task that belongs
to no plan has no identifier from the-way, it works only in a task place with identifiers, and each
later review needs a new one, since the old stays on a done line; no reading of the backlog, the sentence always asking for the
task "if there is none" — the reminder never goes quiet while the review is planned; the number in
the sentence of this decision, repeated in the code — the entry keeps a single number and each
change of the threshold becomes a change of a decision, against the gain of the rhythm and the
rejected numbers standing in one place of the log.

### WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?

Where a change alters what a screen shows, the screenshots that its author or reviewer shows the
human are embedded as images in the description of the request, from a place that the foundation of
the product settles outside the product's repository; the-way names no place. No file of a
screenshot is committed to the product's repository, the copy of the task cycle's record that a
commit adds to it included. A screenshot is evidence for the time of acceptance: the product may
clear its place after a long time, and the images of old requests then stop showing.

Where a change alters what a screen shows and the foundation of the product settles no place for
screenshots, the author inspects the screenshot as the author's check of a user-interface change
gives and the request shows none: the
section of its description for the human's decisions says that no screenshot is shown and why, and
the cycle does not stop. A screenshot left unchecked for want of a settled way to the running
product is reported as that check gives and needs no second item.

A screenshot that is shown to the human lies in the place the product's foundation settles for
screenshots and not in the agent's directory of working copies, and for it this decision prevails
over WAY-373, which keeps its reach over every other screenshot and every copy made to check
something.

- **Scope:** task-cycle, project-level
- **Based on:** none
- **Relations:** derives from WAY-308 · derives from WAY-287 · narrows WAY-373
- **Verification:** invariants: record-copy-image-check · record-copy-image-files. An agent
  compares a change, its record and its request with the decision:
  - complies: the author of a change to a screen, in a product whose foundation settles a place for
    screenshots, puts the screenshot it shows there, and the request embeds it as an image under
    what the human will see; the copy of the record that a commit adds holds no image file, and the
    image check ran on it before that commit; the product clears its place a year later, the images
    of old requests stop showing and nothing in the product's repository changes;
  - violates: a request embeds an image by a link to a file of the record's copy in a commit of the
    product's repository; a screenshot file stands in a commit of the change; a copy of the record
    is committed with no run of the image check; the foundation of a product requires its place for
    screenshots never to be cleared; a template of the-way names the place where the screenshots lie.
  For a product whose foundation settles no place for screenshots, an agent compares the cycle and
  its request with the decision:
  - complies: a product whose foundation settles a way to its running screens but no place for
    screenshots: the author inspects the screenshot, commits none and embeds none, and the request
    tells the human, in plain words, that the screen was looked at and is not shown, saying that the
    product has settled no place for screenshots, which the human accepts by merging; the cycle goes
    on to its review and its request; a product whose foundation settles no way to the running
    product: the screenshot stays unchecked for that reason in the report and the request, as
    that check gives, with no item about a place;
  - violates: the cycle stops or opens blocked for the missing place; the screenshot is committed to
    the record so that the request has something to show; the request says nothing of the missing
    screenshot, or only in its checks; the missing place is reported as the reason when the way to
    the running product is what fails.
- **Origin:** none

*Rationale:* the human who accepts a request sees the screen in its description, without running
the product, and a file committed to the product's repository stays in its history for good: the
removal of the file by a later commit frees no space and does not change an image embedded by a
link to the earlier commit. In the history of one product the files of 384 screenshots held about
29 MB of about 51 MB of the whole history, measured on 2026-11-08 by listing every object of its
repository and counting their size; the measurement is this product's own, and its record is not
open to a reader of this repository. The rule is the-way's and the place is the product's, because
the places that serve a product differ in what they cost and in who can open them, and a place named
in the process would bind products it does not suit. A screenshot is looked at when the request is
accepted and rarely after, so a place that may be cleared costs a few old requests their images and
spares the product a store that only grows. The rule on working copies keeps a screenshot made to
check something in the directory of the agent, which goes with the task's directory; a screenshot
shown to the human has to outlast that directory until the request is accepted, so this decision
prevails over that rule for it and for nothing else. The price taken: an old request shows a broken
image once its place is cleared; a product with no place settled shows no screenshot, and the human
accepts without seeing the screen or settles the place first. A request that shows no screenshot and
says nothing leaves the human to guess whether the screen was looked at; naming the lack in the
section for the human's decisions lets the human weigh it and make a task of settling the place.
The author's check of a user-interface change refused to stop the cycle for an unsettled way to the
interface, and the same holds here: a stop comes after the change is made, when it can no longer be
avoided. The case differs from that of an unsettled way: there the author cannot look at the screen,
here it looks and has nowhere to put the result.
*Rejected:* the screenshots kept in the record in the product's repository and embedded by a link
to the commit — the files stay in the history for good, which is the problem the rule exists to
end; nothing kept, the agent describing the screen in words — at acceptance the screen still cannot
be seen, the problem the rule started from; the attachments of a release in the product's
repository, as the place the-way would name — in a private repository an image may not show (not
checked), and the list of releases fills with files that are no release; an external file store, as
the place the-way would name — a new tool with keys and an action of the human, a technology choice
to be settled on its own; the screenshots only on the human's
disk, in the ignored directory of the cycle — the description cannot link to a local file; a place
never cleared, the matter returning when it grows — the evidence is looked at once, when the request
is accepted; the lack of a place stopping the cycle — the stop comes after the change is made, which
the author's check of a user-interface change refused for the way to the product.

## Private paths and notes

Where a user keeps the places outside every repository that the-way's files name, and how a cycle
and a product keep private paths and notes out of what they publish.

### WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?

A task cycle commits its record and publishes the description of its request only cleaned, in every
repository, public or private: each absolute path becomes a path relative to the repository (a place
outside the repository, a description of what the place is), and the path or the title of a private
note becomes a description of what the note is. The line `Task relation:` of the record and the line
`Project relation:` of the copy of the task document stay as they are unless the check of WAY-309
lists them; a line it lists is cleaned like any other, and the request tells the human, since the
reader of a plan's state may then report a conflict. The cleaning comes before each commit
that adds the record — its copy for a request, the repetition of that copy in a correction after
review and the copy of a request blocked for any cause — and before each publication of the
description, the first and every later edit; the messages of the commits are not cleaned.

- **Scope:** task-cycle, agent-instructions, project-level
- **Based on:** none
- **Relations:** derives from WAY-27
- **Verification:** an agent compares a cycle, its record and its request with the decision:
  - complies: the copy of a record for a request names a worktree by its path from the root of the
    repository, a private note by "the task's note in the author's backlog", and keeps the
    `Task relation:` line of the record and the `Project relation:` line of the task document as
    they were when the check does not list them; a relation line the check lists is cleaned, and
    the request tells the human that the reader of a plan's state may report a conflict for the
    task; the copy of a request blocked for a reserved choice is cleaned the same way; a private
    repository gets the same cleaning as a public one;
  - violates: a copy of the record is committed with the path of the author's notes or of a
    directory on the author's disk, a relation line the check lists included; the cleaning is
    skipped because the repository is private; a relation line the check does not list is
    rewritten; a cleaned relation line is left out of what the request tells the human; a
    description is published with a link to a note in it; the record is not committed at all so
    that nothing needs cleaning.
- **Origin:** none

*Rationale:* the copy of a record stays in the history of the repository after the merge, and that
history is read by people the author never chose, so what the record says of the author's disk,
notes and private work is published with it. A search of every commit that had added a record in the
repositories where cycles had run, on 2026-11-07, found that nearly all that leaked was absolute
paths, directory names of worktrees and titles of notes in links; the search is this product's own,
and its record is not open to a reader of this repository. Cleaning keeps the record, so
three of its readers go on reading it as before: the human, who follows the link from the request;
the plan's link to the task's document; and the nightly review of process remarks. The fourth, the
reader of a project plan's state, which proves from the record that a task entered its cycle and was
finished (WAY-153), reads it with one loss. It ties the record to the plan's task by the
`Task relation:` and `Project relation:` lines, which stay as they are unless the check lists them;
but until the plan row's document link names the frozen copy of the task, it anchors the record by
the absolute path in the record's `Task source:` line, which the cleaning replaces. For a task of a
project plan the reader then reports the copy as unchecked and proposes no move to done from it
until a human links the frozen copy; it fails closed and proposes nothing it cannot prove. A task
that belongs to no plan is not read this way. A relation line the check lists is cleaned like any
other, since nothing the check lists is published, and the reader may then report a conflict for
that task; the request tells the human, who sees it. The same rule in every repository spares the
cycle a question only the hosting service can answer, the visibility of a repository. The price
taken: one more step in every cycle; the published copy of the task document differs from the
document in the author's notes; the reader's loss above; a cleaned relation line that can make the
reader report a conflict, visible in the request; the messages of commits stay unchecked; a private
name written as plain words is not seen by the check of WAY-309.
*Rejected:* committing no record, which leaves it on the disk — the reader of a project plan's state
loses its proof that a task entered a cycle and was finished (WAY-153 and the plan's template would
be rewritten), the nightly review would read directories that vanish with their worktrees, and the
request's link to the record disappears; cleaning only in public repositories — the same as the
way chosen where every repository is public, plus a second path no cycle exercises, and since only
the hosting service knows a repository's visibility and git does not, an agent would have to ask, and
one mistake publishes everything; checking the record, the description and the messages of the task
branch before its first push — a finding in a message tells an agent to rewrite the branch's history
before the first push, a risky step paid in every cycle for a problem that has not occurred;
checking the record alone — the description can leak as one request's did, and it lies in the
directory the check reads anyway.

### WAY-309 — How does the cycle find the private paths and notes in what it publishes?

Before each commit that adds the record, on its cleaned copy, and before each publication of a
request's description, the first and every later edit, the one that adds the link to the record
included, the block in the language of the task document among its text, the orchestrator runs
the-way's script that lists, with the file and the line of each, every absolute path (a drive
letter, a home directory) and every note link written `[[...]]`, and corrects what it lists until
it lists nothing. The script finds them by pattern, holds no list of private words and rewrites
nothing. The check of WAY-294 runs on the original before the copy is made, the cleaning is one
rewriting of every text file of the copy, and the check runs once more on the cleaned copy, where an
item it lists is made to read the same in the report and in the remarks, not appended again.

The script takes no `[[...]]` for a note link when its first bracket stands against a letter, a
digit, a dot or an underscore on its left, when it is a character class of the shell in double
brackets, `[[:space:]]`, with one of the twelve POSIX names between the colons (`alnum`, `alpha`,
`blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`), and no
letter for the start of a drive when a backslash stands before it. It takes no text for an absolute
path when all that follows the drive letter and its colon is escape sequences of a newline, a tab or
a carriage return (`\n`, `\t`, `\r`), so a message ending in a letter, a colon and such a sequence
is not listed; a path written with a real name, a Git Bash path, a link after a space or a mark and
a text stuck to such a sequence stay listed.

- **Scope:** task-cycle, agent-instructions, project-level
- **Based on:** none
- **Relations:** derives from WAY-308 · narrows WAY-294
- **Verification:** invariants: tracked-file-private-paths. For the cycle's use of the script, an
  agent compares a cycle, its record and its request with the decision:
  - complies: the script lists the path of a worktree in a report of the copy, the orchestrator
    replaces it by the same words in every file of the copy where it stands, the script lists
    nothing on the next run, and only then the copy is committed; the edit of a description that
    adds the link to the record is checked again before it is published, its block in Polish
    included; the check of WAY-294 lists an item of a report on the cleaned copy because the report
    and the remarks were cleaned in different words, and the orchestrator makes the two read the
    same and appends no entry;
  - violates: a copy of the record is committed with no run of the script on it; a description is
    published after a run that came before the link to the record was added; the script is given a
    list of private words, or rewrites a file; the orchestrator stops after a run that listed
    something; the orchestrator appends a second entry to the remarks for an item that the check of
    WAY-294 lists only on the cleaned copy.
  For what the script takes for an absolute path and for a note link, an agent compares the change
  with the decision:
  - complies: the script lists a path through a directory named `new`, written after a drive letter
    in a string of code, and a note link that follows a space; it lists nothing for a slot of a
    specification written with a dot before its brackets, for an array inside an array in code, for
    the end of a message in a string of code that ends in a letter, a colon and a newline sequence,
    or for the letters of a regular expression that stand after a backslash; it lists nothing for a
    character class of the shell in double brackets with one of the twelve names, such as
    `[[:space:]]` in a command, and lists a note link on the same line as one;
  - violates: the script lists the slot of a specification; the script lists the end of a message
    that ends in a newline sequence; the script lists nothing for a path through a directory named
    `new` written in a string of code; the script lists nothing for a link to a note after a space;
    the script lists `[[:space:]]`; the script lists nothing for a double-bracketed text between
    colons whose name is none of the twelve, such as the name `other`.
- **Origin:** none

*Rationale:* what a pattern sees is the form of a path or of a link, and the same search of
2026-11-07 (the search of WAY-308: this product's own, with a record not open to a reader of this
repository) showed that nearly all that leaked had such a form, while a private name written as
plain words has no mark a pattern could use. A script reads every file of the copy every time, where
a model reading a long record for what looks private misses an item without a trace, and it reads
the description, whose block in another language is the part a reader checking by eye covers least.
The check of WAY-294 runs first on the original because the original holds the words the reports
gave, so each item reaches the remarks once before any word changes; the cleaning is one rewriting
so that a report's item and its entry in the remarks keep reading alike. The price taken: a private
name in plain words passes, and a list of such names can be added by a task of its own when one
appears; the pattern lists some text that is neither a path nor a link, such as a code sample, which
the orchestrator writes so that the pattern passes it; one more check in every cycle. The patterns
were written for the prose a cycle publishes, and code holds shapes that look like their targets and
are not. A trial on every tracked file of one public product on 2026-11-09, with these rules and the
rule of WAY-320 that a note link counts only in a Markdown file, listed exactly the nine real paths
and the one example of a Git Bash path written on purpose, where the patterns without them had also
listed 78 texts that were neither: 73 of them `[[...]]`, among them an array inside an array in
code, a character class of the shell and slots of a specification quoted word for word, and 5 the
end of a message or a regular expression. Each rule is narrow, so that what a real path or link can
look like stays listed. The price taken: a directory of the root of a disk with a one-letter name,
written `n`, `t` or `r` and standing alone after the colon, is not listed; a link stuck to a word,
which Obsidian renders as a link, is not listed; and a text stuck to an escape sequence still gives
a false hit, which the product removes by rewriting the string. A character class of the shell in
double brackets is code too, though a command quoted in a Markdown file holds it: a run of the check
on 2026-11-11 over the commands in the Markdown files of one product listed twelve such texts, all
of them one of the twelve classes. Both runs are this product's own, and their record is not open to
a reader of this repository. The twelve names are listed one by one, not matched by a general shape,
so a text with another name between the colons stays listed, since it may be a note. The price
taken: a note whose title is one of these names between colons is not listed, and a name a shell
adds later needs the list changed.
*Rejected:* patterns and a list of private words in a file in the home directory — accepted first,
then given up after the search of the history: almost nothing was left to put on the list, and it
costs a file to remember, a step of the human before a cycle and code that today catches almost
nothing; patterns and a list kept in the notes, whose place the process knows only through an
environment variable — the same costs and a variable to set on every machine, and without it the
script checks the patterns alone; patterns and the orchestrator's own judgment, which replaces what
it takes to be private — one more reading of the whole record in every cycle, an omission passes
silently, and the names of a public and of a private repository look alike in text; the product
lists the Markdown file holding the quoted specification among the skipped files — every real path
later written in that file of its foundation passes; no change to the rule for a link — the check of
that product fails while the quoted fact stands in its foundation, and the quote cannot be reworded,
since an environment fact quotes its source word for word; a small letter for a drive in code starts
no path — it passes every path written with a small letter, the home directory of a user in the form
some tools print it included; recognising strings and regular expressions for each language — a
parser for each language a product adds, out of proportion to the few texts it frees; no change to
the rule for a drive — the product rewrites each such string and every later message of that form
hits again, or lists its files and a real path in them passes; no exception for every
double-bracketed text between colons — a note whose title is written between colons, in double
brackets, passes, a cost the check cannot see; no exception for every `[[` that a parenthesis or
another mark follows — it cuts real links whose titles begin with a parenthesis, as a vault holds
them; the exception only in the check of tracked files — two sets of rules to keep and to describe
apart, and a cycle copy that quotes such a command still gives the false hit, which the cycle
removes by rewriting it in words.

### WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?

A user's places on their own disk that lie outside every repository, such as the place of a
product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json`,
found at that place for every user and through no environment variable: a JSON object whose keys are
repository names, each holding entries by name, such as `tasks`, `projects` and `task-rules`, whose
values are paths on the user's disk. No file the repository tracks holds an absolute path, or a note
link in a Markdown file, other than the files that the invariant `tracked-file-private-paths` names,
which write example paths in order to find or to test them; a file that points to such a place names
its entry in the locations file. The copy of a task cycle's record and the description of a request
are checked for a note link in every file, as WAY-309 gives.

A place that a script of the-way keeps for itself under `~/.the-way/`, such as the register of the
runs of the gate, `~/.the-way/gate_runs`, needs no entry of the locations file.

- **Scope:** agent-instructions, project-level, foundation-review, product-guidelines, task-cycle,
  process-audit
- **Based on:** none
- **Relations:** derives from WAY-27
- **Verification:** invariants: tracked-file-private-paths. For the place and the form of the file,
  an agent compares the change with the decision:
  - complies: a skill that needs the place of a product's tasks reads the entry `tasks` under the
    product's name in `~/.the-way/locations.json`, and one that needs the rules of that place reads
    the entry `task-rules` under the same name; a file the repository tracks says "the entry
    `tasks` under `the-way`" where it means a place on the user's disk; the script of the gate keeps
    its register of runs under `~/.the-way/` with no entry for it in the locations file;
  - violates: a skill reads the location from an environment variable; a tracked file the
    invariant does not name holds the path of a directory on the user's disk, or a Markdown file it
    does not name holds a link to a private note; the locations file is put in a repository, or
    holds an entry of one repository under the name of another, or a single entry for the rules of
    the task place at the top level of the file, shared by every product.
- **Origin:** none

*Rationale:* the repository of the-way is public, so an absolute path written in one of its files
publishes how one user's disk is laid out and what that user's private notes are called, and the
history keeps it after the file is corrected. `~` reads the same for every user and says nothing
about any of them, so one file in a fixed place lets any file say which place it means by a name,
and each user lays the disk out as they like. With no environment variable, every tool started in
the user's home finds the file whether or not a variable was set for it. A place that a script keeps
for itself is the-way's own file, as the locations file is, and gives the user no path to choose: a
script that cannot ask the human needs a default path where no entry is, and one file for each run
needs no lock where gates run at the same time. The price taken: each user creates the file once on
each machine, and an agent that finds no file asks the human; a session that runs in the cloud has
no such file and asks too. The check for paths reads every tracked file but those that must write
example paths, and the list of those files stands in the invariant, so adding a file to it shows in
the change; a real path pasted into a file on the list passes. A note link is text of a note, so it
counts in a Markdown file; in code the same brackets are an array inside an array or a test of the
shell, and a run of the check over every tracked file of one public product on 2026-11-09 listed 71
such texts in code among 88 findings (the run is this product's own, and its record is not open to a
reader of this repository). A link in a report of the copy of a cycle's record, of any kind of file,
is still a leak, so the copy and the description keep the check of WAY-309 in every file.
*Rejected:* the register of the gate's runs as an entry of the locations file — it changes the
script of the gate, its tests and WAY-350, and a script that cannot ask the human needs a default
path where no entry is all the same; one file with the data of every run in place of a directory of
files — gates that run at the same time would write to one file and need a lock on writing, which
one file for each run avoids; the check for paths alone, with an exception for the `## Backlog`
section and the path of the tasks file left in the root `AGENTS.md` — a path in the repository is
the problem ("there should be no such paths in the repository, and that they are there is the
problem"); the place described in words in `## Backlog`, with the path in the user's global
instructions — "global instructions are probably not the place for such things"; the file found
through an environment variable, as the private layer of another project does — the file in a fixed
place plus a variable to set on every machine and in every tool, and an agent in a tool that does
not see the variable does not find the backlog; a local file in the repository that git ignores,
such as `CLAUDE.local.md` — the worktree in which a cycle runs has no such file, and Codex does not
read `AGENTS.local.md`; introducing nothing and correcting only the line that names the rulebook —
the path of the tasks file stays in the repository, and the next path written is stopped only by a
careful review; one entry for the rules of the task place shared by all products, at the top level
of the file — the keys of the file would no longer be only repository names, and a product whose
tasks lie elsewhere would silently take the rules of another place; for the files that write example
paths by their nature, a check that skips only the lines marked as examples — every example line to
mark and the code of the marks, and a real path in a marked line passes too; no exceptions, with the
examples rewritten so that the pattern does not find them — every example to rewrite, the tests and
the description of the script harder to read, and every later author of a test has to remember it; a
check that skips all test files and both scripts — a path in any test of the-way passes; a note link
counted in a Markdown file only, also in the copy of the record and in the description — a link in a
report of the copy kept as a text or a log file passes, and an agent quoting a task document carries
its links into a report, and it changes WAY-309; a note link counted in every file but the files of
code recognised by their extension — a list of extensions to extend with each new language of a
product, and a script with no extension still gives false hits; no change to the rule for a link —
false hits for every array inside an array in code and a long list of files to except.

### WAY-324 — How does a product check the files it tracks for private paths and notes?

A command of the-way checks the files git tracks in the repository where it is run and skips the
files that the sentence of the invariant named by its argument lists. A product whose
repository is public adds the check with an invariant of that kind, whose method is `test`, and a
short test that runs the command with the identifier of the invariant and cites it; the test of the
invariant `tracked-file-private-paths` in the-way runs the same command and keeps no list of its
own. Every text between backticks in the sentence names a file the command skips, and a name of a
file that git does not track is an error.

- **Scope:** task-cycle, installation
- **Based on:** none
- **Relations:** derives from WAY-320 · derives from WAY-16 · derives from WAY-34 ·
  derives from WAY-321
- **Verification:** invariants: tracked-file-private-paths. For the rest, an agent compares the
  change with the decision:
  - complies: the instruction for installing the-way in a product tells a product with a public
    repository to write the invariant and the short test that runs the command; a product moves its
    pin and its test runs the command of the new commit unchanged; the list of files that write
    example paths stands in the sentence of the invariant and nowhere else;
  - violates: the installer copies a test file into the product; the check of a foundation reads the
    tracked files of every product for paths; a product's test imports the functions of the script
    instead of running the command; the list of skipped files stands in a test of the product beside
    the sentence of its invariant.
- **Origin:** none

*Rationale:* a product reaches the check by running a command of the commit it pins (WAY-34), so the
check changes with the pin and no copy of it stands in the product; the product's test runs in its
one command of tests (WAY-16) and a test that no invariant's citation reaches is reported by the
check of the foundation (WAY-321), so the check needs no line in the product's command. The list of
files that write example paths belongs to the product, and the sentence of its invariant is where a
reader of the foundation and the command both find it. The way WAY-321 rejected for its report, a
mode that a product adds to its own command of tests, is not this one: here the product writes an
invariant and a test, and the command is one of the-way that the test runs. The price WAY-321
named stays: a public product that does not read the instruction for installing has no check, and
nothing says so. It is taken because the check does not bind each product, a private repository
publishing nothing.
*Rejected:* the installer copies the test file into the product — the copy drifts from the-way
(WAY-34), is rewritten whenever the pin moves, which widens what the installer promises, and the
list of files cannot stand in a file the installer overwrites; the check of the foundation reads the
tracked files of every product, with the list from the invariant of the product when it has one —
the check of the form of a foundation gets work that is not its own, the patterns move to the part
shared by the elements, and every product, a private one too, has failing tests after a move of the
pin until it removes or lists its paths; no change — the product writes its test on functions of the
pinned checkout that the-way does not promise to keep, and the test breaks or changes what it finds
when the pin moves; the instruction for installing saying that a product which wants the check adds
it — a public product that does not think of it stays without the check, as one did before a path
reached its repository on 2026-11-06.

## Process audit

How the cost and the measures of cycles are counted and compared across versions of the process, and
where the audit gets the cost of a problem.

### WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it?

The-way gives a template of a register of problems, which holds for each problem the cycle it comes
from, its class, its weight, the cost of its occurrence, the issue it belongs to — the one matter
that like problems of several cycles make — and that issue's fate, the fix of an implemented issue
included. A user's own tool fills the register and the user adapts the template to their own needs;
the audit reads the register that an entry of the user's locations file names and gives no problem a
class, a weight or a cost of an occurrence itself.

- **Scope:** process-audit
- **Based on:** none
- **Relations:** derives from WAY-103 · derives from WAY-320
- **Verification:** an agent compares a change with the decision:
  - complies: the command of the audit reads the register at the place that an entry of the
    locations file names, and counts each problem with the class, weight and cost of an occurrence
    the register gives it; a user whose tool records problems another way changes the template for
    themselves;
  - violates: the audit reads the stage reports of cycles and gives their remarks a class, a weight
    and a cost of an occurrence itself; the repository of the-way holds a register filled with a
    user's problems; the audit reads a register from a place written into its code.
- **Origin:** none

*Rationale:* the class, weight and cost of an occurrence of a problem are a judgment. A register
that a tool of the user fills holds that judgment once, where an audit that read the records of
cycles itself would repeat it every week, and could repeat it differently. A template lets another
user of the-way keep the same register in their own way, as WAY-103 asks of a process meant for
more than its author. The price taken: a user who has no tool that fills the register has nothing
for the audit to count, since the template of the register does not fill it itself.
*Rejected:* the audit reading the records of cycles itself and giving the class, weight and cost —
the same remarks would be judged by two agents, who may judge differently, and the tie of a problem
to its fix would have to be rebuilt each time; the-way taking over the review of the remarks of
cycles — the largest change, and the remarks would turn into issues once a week instead of every
night; the price left in its conditional form, true for every new user — a reader takes the audit
for a tool that has nothing to count today.

### WAY-337 — How is the cost of a cycle measured?

A cycle's cost is two numbers, neither divided by a measure of the size of the task: its cost at
constant prices, computed from a price list of models that carries a date, and the share of that
cost spent in fix rounds, a fix round being the fix of a review's findings and the review of that
fix. A turn of an agent serves a fix round when the message that dispatches or resumes it names the
round's findings file by its path in the cycle's `reports/`, which only the messages of that fix
and of the review of that fix do, and the cycle's record names each round by that path. The share
is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and
the stages cannot tie each round to the turns that served it.

The record's item *Review rounds* also takes an entry for a review that passed with no fix, in a form
of its own that opens with the word `review` and holds the result `PASS` and the path of the review's
report in `reports/`, with no findings file. Such an entry is no fix round for the cost of a cycle
and for its share, and the audit of the process reads it as a round with no contradiction with the
settlements (WAY-404).

- **Scope:** process-audit, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** tests: that an entry of the item *Review rounds* that opens with the word
  `review` and holds the result `PASS` is no fix round of the cost and of the share, and that a
  record whose item holds such entries alone says the cycle had no fix round. For the rest, an agent
  compares a change with the decision:
  - complies: the cost of a cycle is shown as an amount at the prices of one dated list and as the
    share of the fix rounds in it; the share counts once each turn whose message named a findings
    file of a round the record names; a record that tells its rounds in prose, without their
    findings files, leaves the share unknown;
  - violates: the cost is a sum of tokens of every kind and model; the cost is divided by the lines a
    cycle changed; a turn is put in a fix round by the words in the name of a report or of an agent;
    a record that names a fix round in any form gets a share of `0.0%`; the message that resumes the
    agent of a fix names its findings file only inside its handoff.
- **Origin:** none

*Rationale:* at constant prices a cycle's cost changes when its work changes, not when the price of a
model does, and the share of the fix rounds shows how much of the cost went to work that a review
sent back. A divisor taken from the task would turn both into a ratio whose changes could come from
the task as well as from the process, and the measure of size would have to be chosen. The message
that sets an agent working is the one text that holds, at the moment the work starts, what the
work is for; a findings file named there ties a turn to its round with no guess from names, which
differ from one cycle to the next. A share given where the tie fails is a figure that looks
measured; unknown says the measure is missing. A review that passed with no fix has no findings
file and serves no fix round, so it takes a form of its own in the record: the one form of a fix
round stays exact, and a cycle that sums up such reviews has a place for them that costs its
record no unknown. The price: the item holds two forms, and a reader of it tells the entries of
the fix rounds from the others by their first word.
*Rejected:* a cost divided by a measure of the size of the task — the human settled that cost is
measured by the two numbers alone, and the source keeps no reason beside it; a turn put in a fix
round by the words `fix` and `review` in the names of reports and of stages — records name their
fix reports in other words, and a cycle that had a fix round got a share of zero; a turn tied to a
round by its time against the times of the record — the record and the report of a cycle's stages
write times in different forms and zones; the share given only as zero or unknown until the report
of a cycle's stages carries the tie — the measure stays empty in every cycle that has a fix round;
the item *Review rounds* forbidding the entry of a review that passed with no fix, which leaves its
trace in the table of events — the cycle's leader wants those reviews summed up somewhere, so
without another place they would be written there all the same, and each such record would give
unknown; the count skipping with no word each entry not opened with `findings` — a fix round written
with a slip in its opening would vanish without a trace, giving a false `no` for Q1 and a share of the
fix rounds that is too low.

### WAY-339 — When do the measures of the audit stop being comparable?

A new series of the cost of cycles, the two numbers of WAY-337, starts only with a new price list or
with a change of the script that measures the cost, `task-cycle/cycle_stages.py`; a new series of
the count of remarks starts wherever a series of the cost starts and also with a change of the form
of a stage report, of the list of classes or of the instructions of the reviewer. The measures of
how a cycle's agents use context and the prompt cache and the times of the gate form series of
their own: a new series of those starts only with a change of the script that counts them or of the
script that records them, and, for the times of the gate, also with a change of the test runner of
the process, whose output gives the time of each directory; no change of the instructions of the
cycle, the reviewer's and the author's included, starts one. The audit compares each measure only
within a series of its own kind, and judges a version of the process by the cycles that ran on it,
never one week against another; and where a cycle's own change changes a tool that measures — the
script that measures the cost, the script that counts the measures of context and cache use, the
script that records the gate times or the test runner of the process — the audit gives the measures
of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote
them (the file of that tool is not read for that cycle, so no field of it is missing and no line
`Error:` is given for it), and its other measures as they stand under the version it ran on.

The measures of how a cycle's agents use the context and the prompt cache of the model — the number
of model calls, the size of each call's context, the tokens written to the cache and the tokens
written to it again, and, for each agent of the cycle, the bytes of the decision log and of the
index of decisions that entered its context and how many times each entered it — are counted by a
script of their own into a file of their own in the cycle's record, and are never columns of the
stage report of the cycle's stages, the table of its tokens by model. The one exception is that this
report holds, for each stage and model, the tokens written to the cache at each lifetime, as an
input of the cost (WAY-337) and not as a measure of cache use: the script that measures the cost
counts them, the script of the other measures counts the same tokens for its own file, and neither
takes its figures from the file of the other.

- **Scope:** process-audit, task-cycle, gate
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: audit-series-script-paths. tests: that the audit compares the cost
  and the count of remarks each only inside a series of its own kind, and that a series of the cost
  ends only at a new price list or a change of the script that measures the cost, and a series of
  the count of remarks also at a date of the list of classes and a change of the files that give the
  form of a stage report or of the type of agent the reviewer receives its instructions as; that
  none of these splits the series of the measures of context and cache use or of the gate times,
  and that a change of the script that counts the first, of the script that records the second or of
  the test runner of the process splits only the series of its own measures; that a cycle whose own
  change changes a tool that measures gives the measures of that tool, the times, the cost and the
  share of the cost in fix rounds for the script that measures the cost, as unknown with the reason
  that the cycle changed the tool, and its other measures as they stand under the version it ran on;
  that the stage report holds, for each stage and model, the tokens written to the cache at each
  lifetime, and that the script that measures the cost and the script of the other measures count
  the same tokens from the transcripts. For the rest, an agent compares a change with the decision:
  - complies: the cycles of one version of the process are compared with the cycles of another
    version inside a series; a later change that adds one more measure of context or cache use adds
    it to the script and the file of those measures, and the stage report keeps the columns it has;
    the file of those measures gives for the reviewer of the whole change the bytes of the decision
    log that entered its context and in how many reads, and the bytes and reads of the index of
    decisions it wrote, beside its other figures;
  - violates: the cost or the number of remarks of one week is set against that of the week before;
    a change adds to the stage report a column of a measure of context or cache use other than the
    tokens written to the cache by lifetime that the cost is priced from; the script of those
    measures writes its numbers into the stage report; the script that measures the cost takes the
    tokens written to the cache from the file of the measures, or the script of the measures takes
    them from the stage report; the bytes of the decision log are counted once for the whole cycle
    and not for each agent, or the reads of the index of decisions are left out of them.
- **Origin:** none

*Rationale:* a change of the form of a stage report changes how many remarks a cycle yields, as the
rise of remarks after WAY-260 shows, a change of the price list changes the cost of the same work,
and a change of the list of classes or of the instructions of the reviewer changes what is counted
and what is found. A number from before such a change says something about the change as well as
about the process. The cost and the count of remarks are split apart because only a new price list
and a change of the script that measures the cost change what the cost says of the same work: the
audit exists to say whether the process got dearer, and a change of the reviewer's instructions is a
change of the process, so a series of the cost that such a change ended would never hold the two
sides to compare, as WAY-339 holds for the measures of context and cache use and the gate times. The
price taken: after a change of the reviewer's instructions the audit cannot tell "the reviewer found
more" from "the process got dearer", since a rise of the cost in the series of the cost may be
either, while the count of remarks, which does change meaning with the reviewer, has the series that
ends there. The measures of context and cache use and the gate times are the numbers by which a
change to the instructions of the cycle is judged, so a series that such a change started would
never hold the two sides to compare; what changes their meaning is a change of the script that
measures them, or of the test runner whose output the times of the directories are read from, and
those are the changes that start their series. The test runner is part of the measurement of the
gate times: a change of how it runs the directories changes what the time of each one measures, and
its output is what those times are read from. A cycle that changes a tool that measures is measured
by two versions of that tool, the one it ran on and the one it left, and its figure of what the tool
measures belongs to neither alone; unknown says the measure is missing where a figure would look
measured, and the cycle's other measures stay as they are. The price: such a cycle gives no figure
of the tool it changed. A column of the stage report for the measures of context and cache use would
be a change of the script that measures the cost and would end the comparison of the cost of cycles
across it, while a file of its own changes no form of the report. The columns of the tokens written
to the cache by lifetime that the stage report does hold have this price, taken on purpose: the cost
needs them for each stage and model, and the file of the measures, whose figures are for each agent
with no model and no stage row, cannot give that. The price of the columns: the tokens written to
the cache are counted by two scripts, and the series of the cost ends at the change that brings the
columns. The bytes of the decision log and of the index of decisions in each agent's context show
what the rule of reading the foundation (WAY-150) costs each agent and whether a change of that rule
lowered the cost, so they are counted with the other measures of context use, in every cycle, where
the cycles on the two sides of such a change can be compared. The price: a second file in each
cycle's record, and a second reading of the record for the audit.
*Rejected:* the changes that start the series of the cost, with the script that counts the measures
of context and cache use added to them — the comparisons would almost never occur, since nearly
every change made to improve the process touches those instructions, and adding the script to that
list would end the series of the cost as well. For the gate times, a mark on each run of how many
directories ran at once, which would split the runs by that mark and not by a change of a script —
it changes the test runner, the script that records the times, the tables of the gate times and of
WAY-350 and the reading of the audit, it leaves the runs made between the move to parallel
directories and this decision mixed with the earlier ones, and the old records would need a reading
for the runs that carry no mark. And no split of the gate times at all, which leaves the times of
the two ways of running the gate mixed for weeks, so that whoever reads the audit must remember it
until the new runs outnumber the old. New columns of context and cache use in the stage report — a
column would change the script that measures the cost and end the series of the cost; a sentence
added to the first paragraph saying that adding columns starts no series — a file of its own avoids
the dispute with no change to that paragraph. For the series of the cost, the rule left as it was,
every change of the form of a stage report, of the list of classes and of the instructions of the
reviewer ending it, with only the file of the reviewer's type added to the changes that split — the
audit still answers unknown for most versions of the process. The rule narrowed by taking the forms
of the reports of the stages out into files of their own, so that a change of them would not touch
the files of the methods of the stages — at most 14 of the 34 splits that 134 merges of the first
parent of the main line gave would go, at the price of rebuilding four files of those methods. For a
cycle that changes a tool that measures, the measures of that tool counted in a new series and the
rest under the version the cycle ran on — one cycle stands in two versions, and the grouping and the
tests of the count grow more complicated. For the tokens written to the cache at each lifetime, the
file of the measures as their carrier into the cost — its figures are for each agent and carry no
model and no stage row, while the share of the cost spent in fix rounds needs the cost of each turn,
and a subagent that the author resumes has several turns, so the file would have to carry turns,
with the windows and the owners of the nested subagents that the script of the stages computes: a
second copy of the logic of the stages, or a file of measures that reads the stage report; it also
makes a second script that measures the cost, so that a change of the script of the measures would
end the comparison of the cost, which this decision forbids, and, were it wrong, the cost of a turn
would be wrong or unknown for the cycles that matter and the series of the cost would split at the
wrong changes. For the same tokens, a second table or section of the stage report keyed by stage and
model — the audit would join two tables by a key, a row in one and not in the other becomes a new
refusal, the heading, the table and its columns are three more fields of a reading that WAY-344
checks, and nothing is gained over columns in the table whose rows already are the stage and the
model; were it wrong, a cycle whose two tables disagree would cost unknown and the join would be a
place for a wrong figure. For the bytes of the decision log and of the index of decisions, a measure
made once by a separate agent outside the cycle, before a change of the rule of reading and again a
few cycles after it — the second half needs a task of its own with a reminder, and nothing of it
stays in the process.

### WAY-350 — Which runs of the gate does the audit compare between versions of the process?

The script that runs the gate records, at each run, how many other gate runs by the script were going
at the same time on the machine, from a registry that the script keeps in the user's own directory,
outside every repository: an empty file for each run, made when the run starts and marked as ended
when it ends, a run that has not ended counting for at most six hours, an ended one kept for a day
and an entry whose times cannot be, such as an end in the far future, deleted and counted for
nothing. The audit compares the times of the gate between versions of the process — the median of each
version and whether it falls against the previous version of the same series — only over the runs
that passed and during which no other such run was going, and shows the other runs apart.

- **Scope:** process-audit, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares a change with the decision:
  - complies: the median of a version is taken over its runs that passed with no other run
    alongside, and the runs with company, the runs that failed and the runs whose exit code is
    unknown are listed apart; a version in which every run had company or failed gets no median and
    no comparison, and its runs are listed apart;
  - violates: the median is taken over all runs; the shortest run of each version stands for it; the
    count of other runs is taken for the load of the machine as a whole; a run that failed enters
    the median.
- **Origin:** none

*Rationale:* the same run of a product's gate has lasted 15 to 16 minutes on a free machine and 23
to 40 minutes beside several sessions, so a median over all runs says mostly how loaded the machine
was; the durations are this product's own measurement, and their record is not open to a reader of
this repository. A run that failed says how soon it failed, not how long the gate takes, and one
such run alone on the machine would pull a median down and make a version look faster than it is.
The count of other runs shows only the runs by the script: a load of another kind is not seen, and a
version in which every gate had company or failed gets no comparison.
*Rejected:* the runs that failed taken into the median — a run that stops early has a short time
and makes the version look faster; the shortest run of each version — a version with more cycles has
more chances of a fast run and looks better, and one lucky run sets the result; the median of all
runs, as for the other measures — at today's spread the comparison says mostly how loaded the
machine was.

### WAY-404 — Who marks a contradiction with the settlements, and where does the audit of the process read it from?

A reviewer of a code review marks each blocking finding as a contradiction with the settlements or
as none, and the mark is the reviewer's own. A finding is a contradiction where it says that the
change does something against an entry of the foundation, one the change itself writes included, or
against a settlement of the task document — an answer under its *Questions to settle*, a row of its
*Settlements to record* or a decision of its *Decisions in play* — and a point of *To do* left undone
is none. The cycle writes the mark into the entry of the round in the record's item *Review rounds*,
and the audit of the process takes from that mark, with the marker of a discarded attempt (WAY-405),
and never from the text of a reviewer's remarks, whether a contradiction with the settlements came
out only after the code was written.

- **Scope:** process-audit, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-135 · derives from WAY-339
- **Verification:** tests: that the count answers whether a contradiction with the settlements came
  out only after the code was written from the mark of the entries of the item *Review rounds* and the
  marker of the item *Discarded attempt*: yes where an entry of the item *Review rounds* carries the
  mark of a contradiction, that item being held once and in its form (no entry in neither form, no
  findings file named twice, nothing beside its colon), or the record holds the item *Discarded
  attempt* once and it gives the marker `open design choice`, so that each yes stands over the
  unknown that the other item gives and over that of an unmarked round, while a *Review rounds*
  that is not read gives no yes, nor does a doubled *Discarded attempt*, no where every entry
  carries the mark of none and the item reads `none` or gives only the markers `reserved choice` and
  `size`, unknown where an entry carries no mark, or an item is missing, doubled or not read, and no
  yes stands, and from no text of a record.
- **Origin:** none

*Rationale:* the reviewer has read the entries of the foundation and the task document to find the
finding, so the mark costs it a line, while the leader of the cycle would have to reach the sources
to judge it at second hand, at the dearest place of the cycle. The answer to the question exists to
say whether a spec written before the code would have caught the contradiction (WAY-135): a spec
designs entries and settles what the task leaves open, so a mismatch with an entry or with a
settlement of the task is its business, and a point of *To do* that the executor left undone is
unfinished work that no spec would have caught, which would turn a yes into a measure of something
other than the spec. The price: the mark is a judgment, and the judgments of reviewers differ from one
cycle to the next; a round written before the mark gives the audit nothing to read; a change of the
instructions of the reviewer begins a new series of the count of remarks (WAY-339).
*Rejected:* the leader of the cycle marking the round when it writes the entry — it judges at second
hand, with no reading of the foundation like the reviewer's, and a remark that a task's answer is not
kept makes it reach for the sources, which adds context at the dearest place of the cycle; only an
entry of the foundation counting as a contradiction — the answer would miss the mismatches with the
settlements of the task, which a spec before the code would also have caught; every blocking finding
of an unmet requirement counting, a point of *To do* left undone included — the answer would count
the unfinished work of the executor, which no spec would have caught, and a yes would say nothing of
the spec.

### WAY-405 — How does the audit of the process read the reason of a discarded attempt?

The reason of a discarded attempt stands at the start of the record's item *Discarded attempt* as
`reason: ` and one of three markers in backticks — `open design choice`, `reserved choice` or `size`
— or, where the cycle discarded more than one attempt, at the start of each entry under the item, one
entry for each attempt; the item reads `none` where no attempt was discarded. The audit of the
process takes from this item, for its answer whether a contradiction with the settlements came out
only after the code was written, the markers alone and never the text of the item, so that an item
that reads neither `none` nor a marker, written in any earlier form, gives the answer unknown. Where
the lines under the item are not entries at one indent alone — the first line an entry at that indent
and no plain line at that indent or less — or text stands beside the colon, the whole is read as the
text of one attempt, and gives the answer unknown unless it reads `none` or opens with `reason: ` and
one marker and holds no second `reason: ` followed by a backtick (WAY-404); its later lines are
details of that attempt, read for such a second `reason: ` alone, whatever word stands after the
backtick, so that a second attempt written in them with no backtick after the `reason: ` or with its
reason in other words is not read. Where the lines are entries at one indent alone and nothing stands beside the colon, an
entry that opens with no marker gives the answer unknown unless another entry gives yes, and only the
first line of each entry is read, so that a marker in a line deeper than the entry, or in an entry
under it, is a detail and is not read. The item reads down to the next line at the left margin: a
line written there, a continuation of an entry included, is no part of the item and is not read.

- **Scope:** process-audit, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-135 · derives from WAY-404
- **Verification:** tests: that the count reads the reason of a discarded attempt from the marker at
  the start of the item, or of each entry under it, and from nothing else: a text that names an open
  design choice, a reserved choice or a size in other words, or denies one, gives unknown, and an
  item of several entries gives yes where any of them has the marker `open design choice`; and that an
  item whose lines under it are not entries at one indent alone, or with text beside its colon, is
  read as the text of one attempt, which gives no attempt where it reads `none`, unknown where it
  holds a second `reason: ` followed by a backtick, a word that is no marker included, or opens with
  no marker, and gives its reason where it opens with one marker and holds no such second one, its
  later lines possibly a list of details, read for that second `reason: ` alone; that
  in a list of entries an entry with no marker gives unknown and only the first line of each entry
  is read; and that a line at the left margin ends the item.
- **Origin:** none

*Rationale:* a reading of the words of free text can never list every way to deny or to name a
choice, so each unforeseen wording gives a yes the reading cannot tell from a true one, and the
answer to the question is the one on which the human weighs whether a cycle needed a spec; a marker
the agent that discards the attempt writes in a fixed place leaves nothing to infer. The price: the
leader of the cycle writes one more phrase, and a record written before the markers has an item the
audit reads as unknown.
*Rejected:* a wider detection of denials, with the denial after the phrase, farther than four words
or governing a list after commas giving unknown — it changes only the script, but the next
unforeseen wording gives a false yes again, and the answer stays an inference from text that the
rounds are not read by; leaving the reading as it is and adding a test that keeps the present
behaviour as a known limit — the cheapest way, but the first discarded cycle described by such a
sentence gives the false yes on which the human weighs whether the cycle needed a spec.

## Product guidelines and their rules

Where a product's guidelines stand, what a rule of them holds and does not, whether the-way's
templates bind a product, and how instruction files and the agents of a cycle reach them.

### WAY-167 — Where do a product's guidelines stand, and what are their files named?

A product's guidelines are written by hand and stand outside its foundation, in the directory
`guidelines/` at the root of its repository: a file `guidelines/<discipline>.md` for each discipline
of work on the product it keeps guidelines of, save the styleguide and coding disciplines. The
guidelines of the styleguide discipline stand in a file `guidelines/styleguide-<part>.md` for each
user interface of the product, `<part>` being the identifier of the part of the product's map whose
files draw that user interface; those of the coding discipline stand in a file
`guidelines/coding.md`, which holds the product's standing checks, the rules of the whole of its
code and a table naming each other file of the discipline with when to read it, and in a file
`guidelines/coding-<kind>.md` for each kind of code that has an exemplar, which holds that exemplar
and its rules, `<kind>` being the identifier of the kind that the decision designating that exemplar
gives. The directory `guidelines/` belongs to the part of the product's map whose files direct
whoever carries out its tasks, as its instruction files and skills do.

- **Scope:** product-guidelines, installation
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/AGENTS.md
  § line 61 — "A single task often maps to **multiple rows** — "add a new module with search" needs
  both the Module Development and Search guides. Read **all** matching guides first"; read
  2026-10-18
- **Relations:** derives from WAY-44 · derives from WAY-04 · derives from WAY-100
- **Verification:** invariants: guidelines-file-place. For the rest, an agent compares the change
  with the decision:
  - complies: a product with screens in a browser and an admin panel added to its backend keeps
    `guidelines/styleguide-web.md` and `guidelines/styleguide-admin.md`, named after the parts
    `web` and `admin` of its map, beside `guidelines/testing.md`, and the pattern `guidelines/**`
    stands among the files of the part that holds its `AGENTS.md` and its skills; a product whose
    decision designates the exemplar of the kind `endpoint` keeps `guidelines/coding-endpoint.md`
    beside `guidelines/coding.md`, whose table names it with "before adding or changing an
    endpoint", while the product's linter and formatter stand in `guidelines/coding.md` alone;
  - violates: a product's styleguide stands in `docs/` or in `foundations/`; a product with one
    user interface names its styleguide `guidelines/styleguide.md`; a styleguide is composed by a
    script from the product's decisions; a product's guidelines become entries of an element of its
    foundation; every rule of a product's code, the exemplars of its kinds included, stands in
    `guidelines/coding.md`; a product's coding guidelines stand in `guidelines/coding-backend.md`
    and `guidelines/coding-web.md`, one for each part of its map, each repeating the standing
    checks; a file `guidelines/coding-endpoint.md` stands where no decision designates an exemplar
    of that kind.
- **Origin:** none

*Rationale:* a spec lives as long as its task and holds only what entered it, while guidelines are
shared by the whole product and outlast every task that uses them. They stand outside the foundation
because the choices that bind in them are carried by the foundation's entries, which the guidelines
apply, and the rules of their own that they hold only say how to write code, tests or the look of
the product, so the five elements stay as WAY-04 closes them. They direct whoever carries out tasks,
like instruction files and skills, so they belong to that part, whose files change every later task
(WAY-44), and an instruction file leads to them as to knowledge needed now and then (WAY-128). One
directory with fixed names lets a check find them in every product; a product whose screens and
admin panel are drawn by two parts keeps a styleguide for each, and the part's identifier in the
name ties a styleguide to the files it governs, so that a renamed part shows. Coding guidelines are
cut by the kind of code rather than by part, since a kind such as an endpoint can live in more than
one part while its exemplar is one: the general file holds what binds the whole of the code once,
and an agent reads, beside it, only the files of the kinds its work touches, which the general
file's table names with when to read each. The decision takes that table from Open Mercato's table
leading from a task to the guides to read (WAY-100). The kind's identifier comes from the decision
designating its exemplar, so that a file of a kind stands only where a human has approved what it
holds.
*Rejected:* guidelines as a sixth element of the foundation — what binds in them and carries a
choice is already carried and checked by decisions and invariants, the rest only says how to write,
and the list of elements would no longer be closed; an
extract a script composes from the foundation's entries — it holds what the entries say, never how
to apply a rule or a use that follows it and one that breaks it; a styleguide in documentation
beside the code — it directs whoever carries out tasks, whose files WAY-44 gives a part of their
own, yet a change to it would count against the part whose code it describes; meanings kept in the
spec of a screen — the spec ends with its task, and the next screen gives the same colour another
meaning; guidelines in the own directory of the part that directs agents — its path differs from
product to product, and no check could find them; one styleguide for every user interface of a
product — an admin panel and the product's screens are drawn by different parts; all coding
guidelines of a product in one file — it grows beyond measure, and an agent reads rules its work
does not touch; a file of coding guidelines for each part of the map, as Open Mercato keeps a guide
in each of its packages — a kind living in two parts and the standing checks repeat in several
files and drift apart; a file for each kind with no general file — the standing checks have no
place; a row of the table naming a section to read inside a guide, as rows of Open Mercato's table
do — left out of what the decision takes from that table.

### WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?

A binding rule of a product's guidelines says what to do and how, and may give a use that follows
it and one that breaks it, each in one line; what the guidelines hold that states no rule is an
example. A rule that executes a choice of the product with a real cost names by identifier the
decision of the product's log that carries the choice, while its reasons and rejected options stand
in that decision alone, and a rule that only says how to write code, tests or the look of the
product reads `none` in *Decision* and gives its reason in one sentence. A rule names an invariant
only where a cheap test of the product's suite checks the rule on a convention of the product's
code; a rule no such test can check names none, and the review of each change the rule reaches
compares the change with it.

- **Scope:** product-guidelines, decisions, invariants, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-22 · derives from WAY-18 · derives from WAY-08
- **Verification:** an agent compares the change with the decision:
  - complies: a rule of a product's testing guidelines names the decision choosing the product's
    fixtures for test data and the invariant whose test finds a test that writes rows straight into
    the store of data, and gives in one line each a test that sets up its data through the fixtures
    and one that writes rows straight into the store; a rule that red marks only what deletes names
    its decision and no invariant, and the review of a change to the screens compares their buttons
    with it; a rule that a test is named after the behaviour it checks, which carries no choice
    with a real cost, stands in the testing guidelines with *Decision* reading `none` and its
    reason in one sentence; a sentence on how one team likes to name its branches, which states no
    rule, stands among the examples;
  - violates: a rule of a styleguide repeats its decision's rationale and rejected options; a rule
    that executes a choice with a real cost reads `none` in *Decision*; a rule that only says how to
    write carries a paragraph of reasons and rejected options; a rule whose meaning only a reading
    can judge
    names an invariant an agent checks; a rule carries whole files as cases run against the test of
    its invariant.
- **Origin:** none

*Rationale:* guidelines do not replace the foundation's elements but bring what they hold to the
work of one discipline: an agent changing a product's screens needs what to do and how, not an
account of why. A choice that binds is a decision (WAY-22), and a product keeps every decision in
one log (WAY-18), where a collision with the product's other choices can be found and the search of
the whole foundation sees it (WAY-33); named by its identifier, the decision carries its reasons
once, and a change that rewords it brings the rule in line. A rule that only says how to
write code, tests or the look of the product holds no choice that costs anything to take otherwise,
so a decision for it would repeat the rule in a second place with nothing weighed there, and one
sentence of reason beside the rule is enough to apply it; the human approves such a rule before the
code as a row of the task's table or, for one the cycle found, at the merge (WAY-172). Where a rule
gives a use that follows it and one that breaks it, they mark its line, as a pair of examples marks
a decision's, and like that pair they are optional (WAY-12). A rule of guidelines that an
instruction file leads to and that carries a choice thus carries a decision the product records,
the case in which WAY-130 lets a rule stand with no mistake behind it. A cheap test on a convention of the code catches a breach of its rule on every change for
little, while a rule whose meaning only a reading can judge is read by the review that reads every
change anyway (WAY-08); an agent run as its check would cost more than that review and could flag
sound code unseen.
*Rejected:* guidelines keeping their choices with reasons and rejected options in a log of their
own, narrowing WAY-18 and WAY-22 — a second log, whose collisions with the product's decisions no
search of the whole foundation sees, and approval and the review of changes built again for it;
guidelines with no reasons anywhere — the meanings read from the options a choice rejected are lost;
the reasons repeated in the rule beside its decision — two copies drift apart; an invariant for
every rule, checked by an agent where no test decides it — the checks cost more than the code they
guard; a rule only its decision carries, with neither a test nor the review reading the change
against it — the rule rests on the memory of the agent at work; the two uses of a rule given as
whole files and run against the test of its invariant whenever either changes — they test the test,
which is already seen failing once (WAY-08).

### WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?

The rules a template of a discipline of the-way carries and what the-way's skill of that discipline
proposes bind a product only through a decision of the product's log adopting them, and the product
departs from any of them only by a decision of its log that gives the reason. A decision of the-way
on what such a template carries or what such a skill proposes binds the template and the skill,
never a product's screens or code directly.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-168
- **Verification:** an agent compares the work with the decision:
  - complies: a product's styleguide names, at each rule the template requires, the product's
    decision adopting it; a simple admin panel's styleguide drops the page showing its components in
    every state by a decision of the product that gives its reason, the rule reading `none —` with
    that decision; a product with no dependencies of its own drops the audit of dependencies by a
    decision of its log that gives that reason; a cycle holds a product's screens and code to the
    product's decisions;
  - violates: a cycle holds a product's screens to a rule of the template the product never adopted;
    a cycle blocks a product's change on a rule of a linter's set the product never adopted; a
    product leaves out a rule the template requires with no decision of its own; the-way's template
    is edited to fit one product's departure.
- **Origin:** none

*Rationale:* a rule of a template binding every product directly would be as rigid for a simple
admin panel or a small script as for a product's main screens or code, and it would bind from
outside the product's log, where every binding choice of guidelines stands (WAY-168). Adopted by a
decision of the product, each rule meets the product's other choices where collisions are found, and
a departure, written with its reason and approved, then holds in every later task alike, so it is no
freedom to do otherwise from one task to the next. Its weak point: a product can knowingly drop a
rule that would have protected it. The-way's decisions bind a product's work through its pin
(WAY-34); these bind what the-way offers, and the product takes it as a practice from outside is
taken (WAY-100).
*Rejected:* the template's rules binding every product directly — rigid even for a simple admin
panel or a small script, and a binding choice standing outside the product's log.

### WAY-212 — How does a product's instruction file lead to its coding guidelines?

A product's root `AGENTS.md`, outside the block the-way's installer writes, points to its coding
guidelines by one line naming `guidelines/coding.md` by its path in backticks with the condition of
changing the product's code, written as the skill of `instruction-files` gives a pointer, and no
line of it names a file `guidelines/coding-<kind>.md`. Each such file is named instead by a row of
the table of `guidelines/coding.md`, by its path in backticks with the condition under which to read
it, such as adding or changing a file of its kind.

- **Scope:** product-guidelines, instruction-files
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/AGENTS.md
  § line 61 — "A single task often maps to **multiple rows** — "add a new module with search" needs
  both the Module Development and Search guides. Read **all** matching guides first"; read
  2026-10-18
- **Relations:** derives from WAY-128 · derives from WAY-129 · derives from
  WAY-167 · derives from WAY-100
- **Verification:** for the pointer of `AGENTS.md`, an agent compares the change with the
  decision:
  - complies: `AGENTS.md` reads "Before you change the product's code, read `guidelines/coding.md`"
    below the installer's block, and the table of `guidelines/coding.md` names
    `guidelines/coding-endpoint.md` with "before adding or changing an endpoint";
  - violates: `AGENTS.md` holds a line for each file of a kind; the pointer stands inside the
    installer's block; the coding guidelines are imported with `@`; the pointer names a lint command
    to run before a change.
- **Origin:** none

*Rationale:* coding guidelines no instruction leads to can be missed by a session outside the task
cycle; a path with its condition costs one line and is read when the condition comes (WAY-129), and
the pointer leads to work an agent would not otherwise find (WAY-128). A line for each file of a
kind would grow `AGENTS.md`, which the tools load into every session, with each kind the product
gains, while the general file's table leads the agent in a second step to the files of the kinds its
work touches; the decision takes that way of leading from a task to the files to read from Open
Mercato's table leading from a task to the guides to read (WAY-100). The
price: two steps instead of one, and a table that could drift from the files, which only the review
of a change that adds or removes a kind's file catches. The pointer stands outside the
installer's block, which holds no path a product chooses (WAY-107), and the gate runs the standing
checks, so the pointer names no command of its own (WAY-16). The table itself is what WAY-167 gives
the general file; this decision sets how it leads.
*Rejected:* a line of `AGENTS.md` for each file of the coding guidelines, as it has for each
styleguide — `AGENTS.md`, loaded into every session, grows with each kind; no pointer, leaving the
way in to the task cycle — a session outside that cycle can miss them; the table leading from a task
to the guides standing in the root instruction file itself, as Open Mercato keeps it — `AGENTS.md`,
loaded into every session, grows with each kind; an agent sent to explore the code for a topic no
guide covers, as Open Mercato's table allows — left out of what the decision takes from that table.

### WAY-213 — How do the agents of a task's cycle read the product's guidelines?

In the task cycle the orchestrator selects by `product-guidelines/reading.md` the product's
guidelines of the parts each agent's work touches — every file whose *Applies to* names such a part,
a file of a kind of code only where its row's *When to read* in `guidelines/coding.md` also matches
the work — and names those files in the handoff of every other agent that writes or reviews the
spec, plans, makes the change or reviews a part of it, for a slice through the *Read* of its plan,
which the planner proposes and the orchestrator checks; the agent reads each file named whole, never
excerpts of it or a review checklist in its place, while the reviewer of the whole change selects
the guidelines of its own review. The orchestrator reads the guidelines of the task's parts once,
and those of a part the spec or plan adds when it adds it, and names in each handoff the files of
the parts that agent's work touches, with no record of its reasons, no check of the selection by the
agent that receives it and no step of its own revisiting the selection at each handoff; an agent
whose work reaches a part the selection did not cover reads that part's guidelines itself and names
the reach in its report.
With the styleguide, the planner and the author working without a plan read the order of work the
template gives, never as a rule — the environment and the library first, then the values in their
source, then one screen, then its states — and follow it or explain departing from it.

- **Scope:** task-cycle, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-167 · derives from WAY-150 · derives from WAY-36
- **Verification:** an agent compares each agent's reading and work with the decision:
  - complies: the handoff of the author of a change touching screens and endpoints names the
    styleguide, the general coding guidelines and the matching kind guidelines, and the author
    reads each whole; an executor whose slice reaches a part its handoff did not cover reads that
    part's guidelines and names the reach in its report; the reviewer of the whole change selects
    the guidelines of the parts the change touches itself; an author without a plan reads the
    order as an example;
  - violates: only the reviewer reads guidelines; a handoff carries excerpts of a guideline file,
    or a checklist replaces a whole source; a kind's reading condition is ignored; the orchestrator
    records the selection with its reasons, the receiving agent checks it, or each handoff re-runs
    or re-validates it; an agent of the cycle other than the reviewer of the whole change runs the
    reading for itself in place of its handoff, or reads a further part's guidelines without naming
    the reach in its report; the order rejects a plan.
- **Origin:** none

*Rationale:* shared guidance reaches the agents designing and making a change before review can find
its absence. Reading by the parts the work touches bounds context without cutting the source into
instructions detached from their meaning; guidelines are short and hold together only as a whole, so
a file goes to an agent whole. The orchestrator reads the guidelines of the task's parts to select
them, as it selects the foundation (WAY-150), which spares each agent a selection of its own; the
price is that the orchestrator holds the guidelines of every part of the task through the cycle,
which their shortness keeps small. An agent that reaches further reads for itself, and the reviewer
of the whole change, selecting for itself, finds a file the selection missed. An order of steps ends
with the piece of work it orders, so it binds no later work and stays an example (WAY-36).
*Rejected:* guidance given only to the reviewer — mistakes are found after they are built;
a review checklist — examples can become obligations and lose their context; excerpts of a
guideline file — a rule loses the context that gives it its meaning; discovery left only to
instruction pointers — with no shared procedure, a stage can miss a file the same parts lead
another stage to; each agent of the cycle selecting for itself — every agent pays for the same
selection again; a selection the orchestrator records with its reasons, each recipient checks and
every handoff refreshes — it costs every dispatch a record and a check without widening or
correcting the selection; the order of a plan as a binding rule — a rule of a plan, which a commit
cannot make false.

### WAY-312 — Which sentences does a rule of a product's guidelines not hold?

Nothing that edits a product's guidelines, whether the template, a skill of guidelines or a
product's own task, replaces a sentence that names a practice a model knows with the name of the
practice, or takes out a case that follows from a rule's purpose. A product's own task cleans its
existing guidelines of the sentences that the shared template of a product's guidelines rules out —
a rule lists no state of the product's code or of the product and repeats neither a decision of the
product's log nor a value taken from a configuration file — and the skills of guidelines carry no
step that searches for them.

- **Scope:** product-guidelines
- **Based on:** shorter-guidelines-trial
- **Relations:** derives from WAY-168 · derives from WAY-225 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a rule on the dependency audit says that the audit runs in the product's standing
    checks and names the decision adopting its tool, and gives neither the version of the tool nor
    the number of rules its configuration enables; the list under `### Logging scope` stands in its
    rule as the product's promise; a sentence that spells out why a failure is never turned into an
    empty list stays in the rule as written; a product's task removes from the existing guidelines a
    sentence that restates a decision's *Decision* field and leaves a sentence that names a known
    practice, and a case that follows from a rule's purpose, as they were;
  - violates: a rule gives the endpoints the code has today, or the version of a linter copied from
    its configuration file; a rule repeats the sentence of the decision it names; the template, a
    skill or a product's task that cleans its guidelines replaces the sentence on an empty list with
    the words "fail loudly", or takes out a case that follows from a rule's purpose; the audit mode of
    a skill of guidelines gains a step that searches existing guidelines for such sentences.
- **Origin:** none

*Rationale:* a sentence that lists what the code or the product is today goes stale when the code
changes (WAY-225), and a sentence that repeats a decision or a value of a configuration file is a
second copy that drifts from the first (WAY-168); every agent of a cycle reads the guidelines
it is named whole (WAY-213), so each such sentence is read again at every cycle and checked against
nothing. What the author of the code is to do stays, which is what a rule of guidelines is for
(WAY-168). A trial on the guidelines of one product gave no ground for going further: on three tasks
with hidden tests, five runs each of the model Sonnet 5.5, the tests passed 45 of 45 times with the
old guidelines file, with a shorter one and with no guidelines file at all, so the measurement told
none of the three arms from another. Two inferences from that result are the author's own, not the
source's: where the arm with no file passes too, the tests cannot tell whether the file is followed;
and, by arithmetic, a pass rate near 55% gives five of five in about one set of five runs in twenty,
so five of five shows no equivalence. The trial thus settles nothing about a name of a practice or a
case that follows from the purpose, and WAY-100 lets a practice bind only through a decision that
adopts it. The template guards new text; the existing text is cleaned by the product's task, since
only that task can judge sentence by sentence whether a meaning changes (WAY-172); and the skills stay
as they are. Its weak points: the part that keeps known practices and derivable cases stands on
reasoning, not on a measurement; only the rules for which a task was written were tried, and only
today's model; the existing guidelines of a product stay as they are until its task is ordered.
*Rejected:* waiting for a stronger trial, with rules the agent breaks without the guidelines and more
than five runs — the earlier trial was a heavy one, hours of agent time and tens of millions of
tokens, and in a product such a rule may not exist, since code guards the behaviour; no decision, the shortening staying a one-off
in one product — it also turns down the part nobody disputed, and the guidelines of other products
keep only growing; the full yes, all five groups of sentences — a conclusion drawn from the lack of
a signal; besides the way chosen, a step in the audit modes of the skills of guidelines that
searches existing guidelines for such sentences — a change to several skills at once, and the
refresh mode of coding guidelines has heavy prerequisites; a separate task for the template, this
change writing only the decision — until that task, agents writing guidelines by the template keep
adding sentences the decision says to remove.

## Writing and approving guidelines

How guidelines are written, refreshed, extended and approved, what a task that needs missing
guidelines gets, and how an audit of the skills of guidelines weighs its findings and chooses its
causes.

### WAY-172 — How is a new or changed meaning of a product's guidelines approved?

A new or changed meaning of a product's guidelines that carries a choice with a real cost is a
decision of the product's log, new or changed, and the code that uses it is made only once the
human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as
WAY-30 has a change to a decision approved, or, where that document does not settle it, at a
blocked draft request on whose branch the cycle proposes the decision. A new or changed rule that
only says how to write code, tests or the look of the product, with no decision, is accepted by the
human as a row of the task's table of settlements before the code that uses it, or, where the cycle
found the rule itself, at the merge from the request's description, and a rule of a template of
the-way binds a product only through a decision of its log that adopts it (WAY-173). Using a
meaning that a decision of the product's log already carries takes no approval, and neither does
changing a value that keeps its meaning; in the area of new and changed meanings of a product's
guidelines that carry a choice with a real cost, this decision prevails over WAY-114, under which
an agent writes such an entry on its own recommendation for the human to accept at the merge.

- **Scope:** product-guidelines, decisions, project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-30 · derives from WAY-227 · narrows
  WAY-114
- **Verification:** an agent compares the work with the decision:
  - complies: a styleguide task's document carries the meaning "red marks only what deletes", the
    human accepts the document, and its cycle writes the product's decision and then the screens
    that use it; a cycle whose screen needs a role the task did not settle proposes the role's
    decision on the task branch, opens a blocked draft request, and makes the screen only once the
    human has approved it; a cycle darkens the value of the role of the button that saves to reach
    the contrast its decision asks for, its meaning kept, and asks no one; a task's table carries a
    row that goes to the testing guidelines, "a test is named after the behaviour it checks", the
    human accepts it before the code, and the cycle writes the rule with *Decision* reading `none`;
    a cycle that finds such a rule itself writes it, names it in the request among what the human
    did not see in the task, and the human accepts it at the merge;
  - violates: a cycle writes a new role's decision on its own recommendation and leaves it to the
    merge; the orchestrator's go-ahead stands for the approval of a new meaning; a screen that uses
    an existing role waits for the human; a cycle stops on a blocked draft request for a rule that
    only says how to write; a cycle writes a rule that executes a choice with a real cost with
    *Decision* reading `none`.
- **Origin:** none

*Rationale:* a meaning of guidelines binds every later screen, and code built on one the human never
saw is reworked when the human turns it down at the merge, so the approval comes before the code,
where WAY-30 already puts a change to a decision; the task's document is where the human sees what
the cycle is to build on (WAY-124), and a blocked draft request is where the human meets a decision
the cycle cannot make alone (WAY-227). A meaning a decision already carries was approved with it,
and a value changed with its meaning kept changes no rule, since the rule is the meaning and the
value stands in the code (WAY-225), so neither waits. A rule that only says how to write binds no
choice that costs anything to take otherwise, so the human sees it before the code as a row of the
task's table, and one the cycle found itself is applied by the code before the human sees it and is
accepted at the merge, a price paid so that a cycle does not stop at every small rule. Without the
precedence, a cycle meeting such a meaning would face this decision and WAY-114 with nothing to
choose between them (WAY-25).
*Rejected:* a new meaning that carries a choice with a real cost, written by the cycle and shown at
the merge, as WAY-114 gives it — code is built on a meaning the human has not seen, and turning it
down reworks the screens; approval with the plan — in a cycle the human sees the request, not the
plan (WAY-227, WAY-136); approval of every use of a meaning — every screen would wait for the
human; every rule with no decision waiting as one with a decision does, a cycle that finds a new
rule stopping on a blocked request — cycles would stop at small rules such as one that a test's name
describes behaviour; the same as chosen, and in addition the rules of the-way's template that only
say how to write entering a product's guidelines with no decision adopting them — a rule would bind
the product from outside its log, and a departure from it would have no place to stand.

### WAY-174 — How do the-way's skills of guidelines ask the human?

The-way's skills `maintain-styleguide`, `maintain-coding-guidelines` and
`maintain-testing-guidelines` put to the human every choice they settle for a product's guidelines,
a choice they recommend included, and show each in plain words — a styleguide's by what someone
using the product sees on the screen, never by the names or values of design tokens, coding
guidelines' by their effect on the product, never by the names of a linter's rules or the values of
a tool's configuration, and testing guidelines' by their effect on the product, never by the name of
a technique or a tool — saying in plain words what a term of the field means before they first use
it. The coding-guidelines skill asks for decisions, never for single rules, so that the human adopts
a linter's set of rules whole. In the area of the questions these skills ask this decision prevails
over WAY-114, under which a question goes to the human only where the agent has no recommendation.

- **Scope:** product-guidelines, decisions
- **Based on:** none
- **Relations:** derives from WAY-113 · narrows WAY-114
- **Verification:** an agent compares the conversation with the decision:
  - complies: the styleguide skill shows "the button that saves stands out, and the one that deletes
    is red with white text on it", as a question of decision (WAY-113); it asks whether to adopt
    WCAG though it recommends adopting it, after saying in plain words what contrast is; the
    coding-guidelines skill shows "a change that adds a library with a known security hole does not
    get in" as a question of decision, asks whether to adopt the formatter it recommends, and shows
    a linter's set as "this many rules will block a change, and these few flagged sound code here
    and stay as examples", and the human adopts the set with that split; the testing-guidelines
    skill shows "the tests of the account server talk to a real database, so a broken query turns
    them red, at the price of a slower run", after saying in plain words what an integration test is;
  - violates: the skill asks the human to choose between two hexadecimal values of a design token,
    or between two names of a linter's rules; it writes into the task a role or a linter it
    recommends without asking; it speaks of focus rings before saying what focus is; it asks rule by
    rule which rules of a set to take; the testing-guidelines skill asks whether to mock or to fake
    the database.
- **Origin:** none

*Rationale:* the human who approves a product's meanings and standing checks is no specialist of
user interfaces and judges neither code nor the tests below end-to-end ones, so a choice shown by the
names or values of design tokens, by the names of rules, by values of configuration or by the name of
a testing technique is one the human cannot weigh, while what a user sees or what a choice does to
the product can be weighed, as a technology choice reaches a human who cannot assess the technology
through its consequences (WAY-123). A meaning binds every later screen, a standing check or an
exemplar every later change of the code or of the tests, and no decision enters without the human's
acceptance, so a recommendation the human never heard would be a choice no human made. Asked rule by
rule, the human would judge each rule's worth in code, which the trial run already shows by its
effect. The price is a longer conversation in each task that writes guidelines.
*Rejected:* the skill writing what it recommends and asking only where it has no recommendation, as
WAY-114 gives it — screens are built on meanings the human never saw, and turning one down at the
merge reworks them, and the human meets the choice of an exemplar or a departure from a standing
check only in the finished document; questions about the names and values of design tokens, or by
the names of testing techniques and tools — the human cannot weigh them; the human deciding rule by
rule — they would judge what they cannot judge.

### WAY-215 — What happens to a task that needs missing discipline guidelines?

Unless an approved departure under the shared reading of product guidelines applies, a task changing
a user interface with no styleguide,
writing code in a product with no general coding guidelines or writing or changing a test in a
product with no testing guidelines, whether or not the product already has screens, code or tests,
stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge
of a separate guidelines task; refinement independent of that answer continues, and a task writing
those guidelines does not wait for its own output.
For an independent or source-only task `refine-task` adds the prerequisite to the product's
backlog after human approval, while for a plan member it returns `plan change` if the plan lacks
that task or `waits for task <n>` if the plan holds it, keeping the plan's ownership and states.
After that task merges, refinement resumes, reads the guidelines and settles the meanings the
task needs under WAY-172 before readiness; extension or correction of existing guidelines stays
in the current task under WAY-172 and WAY-199, unless the human separates it.

- **Scope:** project-level, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-124 · derives from WAY-144 · derives from
  WAY-154 · derives from WAY-172 · derives from WAY-199 · derives from
  WAY-244
- **Verification:** an agent compares the task, prerequisite and refinement with the decision:
  - complies: a fix in an existing product without coding guidelines waits for their task's merge,
    then reads them before the complete document is accepted; a task adding a test to a product
    whose tests have no testing guidelines waits in the same way for their task; a plan member
    returns its missing prerequisite to the plan owner; an existing styleguide is extended within
    the screen task;
  - violates: an absent styleguide is added only to the screen task's To do; readiness is granted
    merely because a dependency was named; a refiner edits the owning plan; the task writing
    guidelines waits for those guidelines; the task's wait is copied into a new plan state.
- **Origin:** none

*Rationale:* guidelines prepared within the work that first needs them shrink to that work's
needs, whereas separate preparation lets later work share meanings. Existing products accumulate
the same inconsistency, so they take the same wait; its price includes urgent fixes waiting for
that preparation. Extending guidance already present needs no such wait, and resumed refinement
can settle what could not be known without it.
*Rejected:* missing guidelines merely added to the consuming task — their scope contracts to its
needs; a wait only for new products — existing code keeps growing without shared guidance;
a wait first imposed in implementation — meanings surface after the task was accepted;
every extension separated — ordinary corrections wait for unrelated preparation; testing
guidelines with no wait — tests written meanwhile set the patterns every later test copies.

### WAY-216 — What does refinement assign to a task creating an unindexed kind of code?

A task that creates the first file of a kind of code whose row the general coding index lacks
gains in *To do* the designation of that kind's exemplar as the skill `maintain-coding-guidelines`
gives it and its kind guidelines
with their index row, without waiting for a separate exemplar task, and in a product that has
coding guidelines it settles and checks, of the standing checks, only those the kind touches.
Where files of the kind already exist, refinement records that discrepancy and routes exemplar
selection through the comparison that skill gives existing code, rather than treating the next file
as the first. Neither a kind's first file nor that comparison alone makes a task an extension under
WAY-251 or takes research of the standing checks, except that a first file of a kind in a language
that none of the product's standing checks reads makes the task an extension; the comparison covers
that kind alone, takes no trial run of a linter's set and is no audit of a product with code.

- **Scope:** project-level, product-guidelines
- **Based on:** none
- **Relations:** narrows WAY-251 · narrows WAY-202
- **Verification:** an agent compares the task and existing code with the decision:
  - complies: the task adding the first migration also designates its exemplar and writes its
    kind guidelines and index row, and in a product whose formatter reads only the application's
    language it settles the checks that read the language of migrations and leaves the formatter's
    decision as it stands; existing unindexed endpoints go through comparison, which researches no
    standing check and runs no linter's set on the product's code; the first file of a kind of
    shell scripts, in a product whose three standing checks read no shell, makes its task an
    extension, with the research of the standing checks for shell and a trial run of the set;
  - violates: the first migration waits for an exemplar that cannot exist before it; existing
    endpoints are ignored and the next endpoint is called the first; the comparison of the
    existing endpoints is run as an audit of every kind the product holds; the first file of a
    kind settles each of the three standing checks anew although the kind touches one; the first
    file of a kind of shell scripts enters a product whose standing checks read no shell, with no
    research and no tool for it.
- **Origin:** none

*Rationale:* the first instance supplies the material an exemplar needs, so separating its
designation would create a circular wait. Existing instances instead need comparison, or the next
one becomes a model without being judged against what the product already holds. Without the
limit on research every task that creates a kind's first file could pull research of all the
standing checks, and an agent on the comparison goes on improvising and may make a full audit; a
task that is an extension for another reason keeps its research. In a product that has
coding guidelines each standing check already stands decided (WAY-202), so a kind settles only
where a check reads its code. A kind in a language no standing check reads has no tool whose
decision could extend to it, and choosing a tool is a technology choice that needs the research of
an extension, so that kind makes the task one. Its weak points: whether a check reads a kind's
language is the agent's judgement from the product's decisions, and a first file in a new language
costs its task the research and the trial run of an extension.
*Rejected:* blocking every unindexed kind — a genuinely first instance could never arrive;
designating the next instance regardless of existing code — it bypasses comparison; four modes of
the coding-guidelines skill left as they were, with the gap described as a proposal — an agent on
the comparison goes on improvising and may make a full audit; the wording "Neither task is an
extension under WAY-251, and neither takes research of the standing checks" — it takes research
from a task that is an extension for another reason, against the rule that an extension researches;
only the checks the kind touches, with no exception for a new language — the tool for that language
would be chosen on a route without research of tools; no standing check for the kind, the exemption
from research read literally — a script in a new language would enter without a linter.

### WAY-247 — May one task write a product's coding and testing guidelines together?

One task of a product may write both its coding guidelines and its testing guidelines, the skill of
each discipline leading that discipline's matters in the task's refinement.

- **Scope:** product-guidelines, project-level
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-215
- **Verification:** an agent compares the task and the plan with the decision:
  - complies: a new product's first task of guidelines carries the general coding file and
    `guidelines/testing.md`, `maintain-coding-guidelines` settling the standing checks and
    `maintain-testing-guidelines` the levels and their recipes, and the first task with code depends
    on that one task;
  - violates: a new product runs two tasks of guidelines one after the other before its first code
    because each discipline is held to need a task of its own; the coding-guidelines skill settles
    the levels of the product's tests.
- **Origin:** none

*Rationale:* a new product needs both before its first code (WAY-244), and two tasks one
after the other would hold that code back for a second refinement and a second request, while one
task holds both with each discipline led by the skill that knows it. The price: a larger
refinement and a larger request.
*Rejected:* a task of its own for each discipline's guidelines — a new product waits for two tasks
before its first code.

### WAY-251 — What distinguishes a refresh from an extension of guidelines?

For the skills `maintain-coding-guidelines`, `maintain-styleguide` and
`maintain-testing-guidelines`, a refresh updates or corrects accepted guidelines within the scope
they already cover, including adapting them to a new version of a tool the product already uses.
An extension covers something new, and its research checks whether to use what the product already
has or something else, with the human's preferred tool remaining the proposal.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: adapting the accepted testing guidelines to a new major version of their test tool
    is a refresh; covering a new level of tests is an extension whose research checks whether the
    product's existing tool fits it;
  - violates: a change of a tool's version alone is treated as an extension; a new scope is called
    a refresh merely because the product already has a tool that might serve it.
- **Origin:** none

*Rationale:* an update within accepted scope corrects guidance for something the product already
does; a new scope raises whether the existing tools suit it. Telling them apart by scope gives
every discipline the same boundary and spends research where it answers a new question. A
preference still belongs to the human, so research informs its use rather than replacing it.
*Rejected:* refresh and extension treated alike — routine corrections pay for research, or new
scope receives none; a version change alone treated as an extension — new versions can leave the
covered scope unchanged.

### WAY-280 — On what scale does an audit of the skills of guidelines weigh what it found?

An audit of the skills `maintain-coding-guidelines`, `maintain-styleguide` and
`maintain-testing-guidelines` gives each cause of what it found one weight, `grave`, `heavy`,
`medium` or `light`, on one scale described once in a file the three skills share. A weight is
measured by the effect on the user or the owner of the product and follows from what is at stake,
never from how many places break a rule. The-way adopts weight, merging and order from a course's
skill for auditing observability, for these audits, and not the audit as a skill of its own.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: an endpoint that reads the request unchecked and lets a user reach someone else's
    order weighs `grave`, though it is one file; a test of a payment that passes whatever the code
    computes weighs `grave`, since the fault reaches a customer and nobody learns of it; a delete
    button that looks like any other weighs `heavy`, and forty spacings written by hand weigh
    `light`;
  - violates: each skill keeps a scale of its own; forty small breaks of a rule weigh `grave` for
    their number; a cause weighs `grave` only because it stands inside a critical flow; a weight
    blocks a change; the audit runs from time to time as a skill of its own.
- **Origin:** none

*Rationale:* the human who approves a product's guidelines judges neither its code nor its tests,
and an audit that ended with places alone would leave that human to judge what is urgent and an
agent planning the repairs with no ground for its order, and on a long list small things would come
first while a serious one drowned in the middle. A weight read off the effect says what a repair is
worth in terms anyone can judge, and one scale lets causes of different disciplines stand in one
order. Many small breaks stay small and one open way to someone else's data stays open, so
what is at stake sets the weight and the number of places does not. A weight is no grade of the
review of a change: a grade says whether a change can be trusted and blocks it, and a weight says
what is at stake and blocks nothing, so the words differ. From the skill for auditing observability
of lesson m3l5 of the 10xDEVS course the-way adopts a weight for each problem by its effect, the
merging of what comes from one source into one cause, and an order of repair, for the audits of its
skills of guidelines, for the reasons above (WAY-100); the lessons of the course are not open to a
reader of this repository. Its weak points: the text of the scale is
general, so the agent judges how serious a harm would be, and screens seldom reach `grave`, so the
top of a list comes more often from code and tests.
*Rejected:* a scale of its own for each discipline — it fits the differences between the disciplines
better, but it is one more text to keep for each, and where code and tests stand in one task their
weights cannot be compared, so a common order of repair has no ground; the scale of the review of a
change, Critical, Important and Minor, with no new words — nothing new to learn, but that scale
judges whether a change can be trusted and not the effect on the user, and such a grade in an audit
would suggest a blocking that does not stand here; the audit as a skill of its own, run from time to
time — logging is to be kept by a guideline on the code a change touches, and a look at the whole is
the audit at an extension of guidelines.

### WAY-284 — What decides which causes of an audit a task takes?

The weight proposes and the human decides: the agent proposes which causes of the top of an audit's
list a task takes and which it defers, and the human settles it. On deferring a `grave`
cause the agent asks whether to open a task for it in the product's backlog, and a yes takes the
route WAY-215 gives a prerequisite, with nothing waiting for that task. The causes below the top are
deferred together, for standing below the top, unless the human takes one.

- **Scope:** product-guidelines, project-level
- **Based on:** none
- **Relations:** derives from WAY-174 · derives from WAY-215
- **Verification:** an agent compares the work with the decision:
  - complies: the human defers a `grave` cause, the agent asks, and on a yes `refine-task` adds the
    task to the backlog of an independent task, or returns `plan change` for a plan member, and the
    refinement goes on with no wait; on a no the cause stays deferred in the document with its
    reason; the causes below the top reach the human as one choice;
  - violates: every `grave` cause enters the task with no question; the agent defers a cause of the
    top alone; a `grave` cause is deferred with no question of a backlog task; the task waits for the
    backlog task; the human is asked about each cause below the top; a skill of guidelines writes the
    backlog itself.
- **Origin:** none

*Rationale:* the repair of a `grave` cause can be large, so a weight deciding alone would swell a task
of guidelines into cleaning the product, while a `grave` cause left in a document with no further
word ends as if no audit had named it, so its deferral takes a question of its own. The human hears
the proposal with its weights in plain words (WAY-174). The route is that of a prerequisite because
who writes a backlog or a plan is settled there, and nothing waits because the task being refined does
not need the fix. Asking about each cause below the top would bring back the list the limit took
away. Its weak point: the human can answer no, the `grave` cause stays in the document, and
nothing forces a return to it.
*Rejected:* the weight deciding alone, all that is `grave` entering the task and the rest deferred —
less to settle, but the repair of a `grave` cause can be large, so a task of guidelines swells, which
WAY-205 keeps from happening; the weight only ordering the list and the human deferring alone, with
no further question — the fewest changes in the skills, but a deferred `grave` cause ends as it does
with no weight, and the problem returns later.

## Coding guidelines

A product's exemplar, its standing checks, its linters and formatters, the audit of its
dependencies, and the rule of the size of functions and files.

### WAY-198 — How does a product's exemplar bind?

A decision of a product's log designates, for a kind of code, the one file of the product that is
the exemplar of that kind, naming in backticks its path and the kind's identifier, and what of that
exemplar a script can check — where a file of the kind lies, what it calls, how it validates its
input — stands in the coding guidelines of that kind as rules, each naming an invariant. The rest of
the exemplar stands there as an example and binds no later code.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-22 · derives from WAY-173
- **Verification:** for what stands as a rule and what as an example, an agent compares the change
  with the decision:
  - complies: a product's decision designates `src/api/orders/route.ts` as the exemplar of the kind
    `endpoint`, and the coding guidelines of that kind hold, as rules naming a script's invariant
    each, that every route lies under `src/api/`, calls the shared handler and validates its input
    with the shared schema, while how the exemplar names its variables stands among the examples;
  - violates: the coding guidelines of a kind name as its exemplar a file no decision designates;
    the whole behaviour of the exemplar is one rule an agent checks by comparing new code with it;
    the exemplar's code is copied into the guidelines.
- **Origin:** none

*Rationale:* an exemplar left as an example alone lets an agent depart from it with no signal, while
a choice designated by a decision is one the human approved, and copying from existing code without
such a choice turns whichever file an agent finds into law (WAY-225). What a commit can make false
of the exemplar is written as invariants (WAY-22), which keep each later file of the kind to it; the
exemplar is ordinary code of the product, so the same invariants keep it from ageing. Its path and
kind in the decision's binding sentences let a script tie the guidelines to the approved choice.
*Rejected:* the exemplar as an example alone — an agent departs from it with no signal; an agent for
each kind judging whether new code follows the exemplar — its criterion is vague and how often it
flags sound code is unknown.

### WAY-199 — What change of a product's exemplar takes approval?

Designating another file as the exemplar of a kind of code and changing a rule a script checks from
that exemplar are changes of the product's decisions, approved as WAY-172 gives a changed meaning,
while an edit of the exemplar that keeps those rules takes no approval. The coding guidelines of a
kind give beside the path of each file of the kind they list its status, `exemplar`, `copy` or
`do not copy`, and beside the exemplar's path the decision that designates it.

- **Scope:** product-guidelines
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/apps/mercato/src/modules/example/README.md
  § line 46 — "`readable` | The file passed the reference-quality audit. Safe to read and adapt." ·
  § line 47 — "`qa-only` | The file exists and works, but fails at least one current project rule. …
  Do **not** copy it."; read 2026-10-18 ·
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/packages/core/src/modules/customers/AGENTS.md
  § line 7 — "**MUST use this module as the template** for new CRUD modules — copy file structure
  and patterns"; read 2026-11-16
- **Relations:** derives from WAY-172 · derives from WAY-198 · derives from WAY-100
- **Verification:** for what takes approval, an agent compares the change with the decision:
  - complies: a fix of a typo in the exemplar, and a change of its inner structure that keeps the
    rules a script checks from it, go with no approval; a task that would make another file the
    exemplar proposes the change of the designating decision and waits for its approval; a file that
    reads its input unchecked stands in the table as `do not copy`;
  - violates: a cycle moves the status `exemplar` to another file on its own; a rule a script checks
    from the exemplar is weakened in the same edit as the exemplar with no change of a decision; the
    status of the files stands only in the decision.
- **Origin:** none

*Rationale:* the rules a script checks from the exemplar are what binds, so they change only with a
decision, while an edit that keeps them uses a meaning a decision carries, which takes no approval
(WAY-172). An edit that changes only what of the exemplar no script checks passes with no approval,
and every later copy inherits it; that holds, because approving every change of the exemplar's
behaviour would have the human judge code they do not judge. The decision takes
from Open Mercato's statuses the status beside each path, which shows an agent reading the
guidelines what to copy and what not to (WAY-100): its `readable` and `qa-only` become `copy` and
`do not copy`. Open Mercato's statuses are two; the third, `exemplar`, marks the one file a decision
designates (WAY-198), as Open Mercato declares one module the template of its new modules of that
kind.
*Rejected:* approval of every change of the exemplar's behaviour — the human would judge code they
cannot judge; the status of the files kept in the decision alone — an agent reading the guidelines
would not see which files not to copy; the statuses given to the files of a reference module that
the product does not run, as Open Mercato gives them, rather than to files of the product's own code
— left out of what the decision takes from Open Mercato's statuses.

### WAY-202 — Which standing checks must a product's coding guidelines settle, and from when do they bind?

The template of the coding discipline requires three standing checks of a product's code — a
linter, a formatter and an audit of dependencies — and the rule of a product's coding guidelines on
each names the invariants of that check the template gives. A product departs from any of them only
by a decision of its log that gives the reason. They bind a product from the task that writes its
coding guidelines, which is complete only once it holds, for each of the three standing checks, a
decision of the product's log adopting it or departing from it with the reason.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-168
- **Verification:** for the decisions the task ends with, an agent compares the work with the
  decision:
  - complies: a product with none of the three gets, in the task that writes its coding guidelines,
    decisions adopting a linter, a formatter and an audit of dependencies, or departing from one of
    them with its reason, and its coding guidelines name each at the rule the template requires;
    the rule of the linter names the invariant whose test runs the rules that block over the parts
    named;
  - violates: the skill only proposes the standing checks a product lacks, and the task ends with no
    decision on the audit of dependencies; a product's coding guidelines leave out the formatter
    with no decision; the three stand in the template and in no decision of the-way; the rule of the
    formatter names no invariant though a test can run the formatter.
- **Origin:** none

*Rationale:* a product whose code no standing check reads changes its style and takes in a known
vulnerability with no signal, and a skill that only proposes the checks leaves it so for as long as
nobody takes the proposal up. Named in a binding sentence, the three give the refinement of the task
something to check (WAY-139), and a departure with its reason is the product's own approved choice
(WAY-173). A standing check is a run of a tool, which a test makes for little on every change, so
its rule carries an invariant (WAY-168). The price: until a product runs a task that writes its
coding guidelines, nothing of these binds it, as with the styleguide.
*Rejected:* the skill only proposing the standing checks a product lacks — a product that has none
of them would still have no signal; the three named in the template alone — nothing would bind the
refinement to check them.

### WAY-203 — Which rules of a linter's set block a change of a product's code?

A rule of a linter's set stands among the rules that block a change in the product's decision
adopting the set, and so is checked by the invariant of the one rule of the product's coding
guidelines on its linter, only where every report it gives on the product's code leads to a change of
code worth making, a report counting by whether it leads to such a change, whether it is technically
right or not. A rule of the set that gives a report leading to no such change is no rule that binds
the product's code: it may stand among the examples of the coding guidelines, and no invariant checks
it, so the gate does not run it. A comment in the code that turns off a rule that blocks has no
effect: where the tool can be told so by a flag or its configuration, the test of the linter's
invariant runs it so, and where it cannot, the review of each change finds such a comment.

- **Scope:** product-guidelines
- **Based on:** C. Sadowski, E. Aftandilian, A. Eagle, L. Miller-Cushon, C. Jaspan, "Lessons from
  Building Static Analysis Tools at Google", Communications of the ACM 61(4), April 2018,
  https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf § page 62 — "produce no
  effective false positives (the analysis should never stop the build for correct code)" · § page 59
  — "We consider an issue to be an “effective false positive” if developers did not take positive
  action after seeing the issue." · § page 59 — "If an analysis incorrectly reports an issue, but
  developers make the fix anyway to improve code readability or maintainability, that is not an
  effective false positive." · § page 62 — "analysis results shown during code review are allowed to
  include up to 10% effective false positives" · § page 62 — "report issues affecting only
  correctness rather than style or best practices"; read 2026-10-18
- **Relations:** derives from WAY-202 · derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: a rule on unused variables, every report of which led to removing dead code, stands
    among the rules that block in the decision adopting the set and blocks a change; a rule on the order of imports that flagged two files whose order a generator writes
    stands among the examples under its name in the tool, and the linter's invariant does not run
    it; a rule whose report was technically wrong, yet led to a fix that made the code clearer,
    still blocks; the linter's test runs the tool with its flag that ignores comments turning rules
    off, so such a comment leaves the report standing; the review of a change to a script whose tool
    has no such flag finds a comment that turns a rule off;
  - violates: a rule that flagged sound code once blocks because its other reports were right; a
    rule whose technically right report nobody would change the code for blocks; the gate shows the
    rules among the examples as warnings; a rule blocks because fewer than one report in ten led to
    no change; each rule of the set that blocks stands as a rule of its own under `## Rules` of the
    coding guidelines.
- **Origin:** none

*Rationale:* a change of sound code that a blocking rule stops gets through only by a change of the
decision adopting the set, put to a human who does not judge code; the decision takes from
Google's practice that a change is blocked only by a check that gives no report its developers
would not act on (WAY-100). A report that is
technically right but leads to no change worth making costs the change as much as a wrong one, while
a wrong report that leads to a better change costs nothing, so a report counts by what it leads to.
A rule that once flagged sound code leaves the agent free again in its area, as an example it reads;
that holds, because a rule that sometimes blocks sound code is worse than one an agent reads and may
pass by. The gate knows no result that only warns (WAY-63), so such a rule is an example and nothing
runs it. A rule that blocks gives no report that leads to no change worth making, so no comment that
turns it off is sound; a tool that can ignore such comments does it on every change for nothing,
while where it cannot, the review reads each change anyway. The price: some useful signals of a
linter reach the agent only as an example to read, and a comment that turns a rule off in a file
whose tool cannot ignore it is caught only as surely as the reviewer reads the change.
*Rejected:* the whole set the tool recommends blocking — the gate blocks sound code; a rule blocking
while fewer than one report in ten leads to no change, the limit Google's practice allows for checks
shown in code review, left out of what the decision takes from that practice — the gate sometimes
blocks sound code, and only a change of a decision passes it; a rule that gives such reports kept as
a check that only warns — it changes what results the gate knows (WAY-63); only rules of correctness
blocking, never rules of style, as Google's practice sets for the checks that stop a build, left out
of what the decision takes from that practice — a remark on style never blocks in the review of code
(WAY-161), and the human does not judge style; a check that is easily understood, as Google's
practice also sets for the checks that stop a build — left out of what the decision takes from that
practice; a check that is easy to act on and to fix, with a fix it suggests wherever it can, as
Google's practice also sets for those checks — left out of what the decision takes from that
practice; a script of the product's own
finding every comment that turns a rule off where the tool has no flag for it — code kept for what
the review of each change already sees.

### WAY-204 — How are the rules of a linter's set split between the rules that block and the examples?

The skill `maintain-coding-guidelines` proposes which rules of a linter's set block and which stand
among the examples from a trial run of the set on the product's code, each report of which an agent
that wrote none of that code judges by whether it leads to a change of code worth making, whether it
is technically right or not, and a rule with one report that leads to no such change goes among the
examples; for a product with no code it proposes as blocking the rules the tool's documentation
marks as recommended. The human approves that split in the product's decision adopting the set, and a
rule on which a later report leads to no change of code worth making goes among the examples by a
change of that decision, which the human approves. The invariant of the linter rests on one
environment fact, the rules the set holds at the edition the adopting decision names, and that
decision gives the blocking rules as the set less the rules it keeps among the examples.

- **Scope:** product-guidelines
- **Based on:** C. Sadowski, E. Aftandilian, A. Eagle, L. Miller-Cushon, C. Jaspan, "Lessons from
  Building Static Analysis Tools at Google", Communications of the ACM 61(4), April 2018,
  https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf § page 59 — "We consider
  an issue to be an “effective false positive” if developers did not take positive action after
  seeing the issue." · § page 59 — "If an analysis incorrectly reports an issue, but developers make
  the fix anyway to improve code readability or maintainability, that is not an effective false
  positive."; read 2026-10-18
- **Relations:** derives from WAY-203
- **Verification:** an agent compares the work with the decision:
  - complies: the skill runs a set in a scratch worktree of a product with code, a fresh agent
    judges each of its reports, the three rules with a report that led to no change worth making
    stand among the examples, and the human adopts the set with that split shown by its effect; a
    product with no code adopts the rules its linter's documentation marks as recommended, and when
    a cycle later meets a report of one of them that leads to no change worth making, a change of
    the adopting decision, approved by the human, moves it among the examples;
  - violates: the agent that wrote the code judges the reports of the trial run; the split comes
    from an agent's memory of which rules are noisy; a cycle turns a rule off in the linter's
    configuration on meeting such a report, with no change of the decision.
- **Origin:** none

*Rationale:* whether a rule's reports lead to changes worth making shows only on the product's own
code, so the split is read off a trial run, and the agent that wrote that code would judge in its
favour, so another agent judges each report, as Google weighs a report by what developers do with
it. The human does not judge code, so the human approves the split as a whole, shown by its effect
(WAY-174), never rule by rule. A product with no code has nothing to try a set on, so it takes the
rules the tool's documentation recommends; their weak point is that they block with no evidence from
the product, and the first report of one that leads to no change worth making takes it off by a
change of the decision. Which rules a set holds at one edition is one fact, which one edition of the
tool's documentation states, about one thing, with one reason to change, a new edition, as
git's rule of path patterns with its page's exceptions is one fact. A criterion of WCAG stands as a
fact of its own because each is a requirement of its own written in prose, while a rule of
a linter's set is one whose content the tool itself runs at its pinned version, so the invariant
needs the set's membership alone. The price is a trial run and a judgment of its reports each time a
set is adopted.
*Rejected:* every rule of the set blocking — the gate blocks sound code (WAY-203); the human
deciding rule by rule — the human would judge what they cannot judge (WAY-174); an environment fact
for each rule of the set — many facts with one source and one reason to change.

### WAY-205 — How do a linter and a formatter enter a product whose code already breaks their rules?

Where a product's code already breaks the rules of its linter's set that block, the skill
`maintain-coding-guidelines` proposes the linter's invariant over the whole of that code, marked
violated until the code is cleaned (WAY-51). A formatter enters a product by one reformatting of the
whole of its code in the task that brings the formatter.

- **Scope:** product-guidelines, invariants
- **Based on:** C. Sadowski, E. Aftandilian, A. Eagle, L. Miller-Cushon, C. Jaspan, "Lessons from
  Building Static Analysis Tools at Google", Communications of the ACM 61(4), April 2018,
  https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf § page 66 — "tool writers
  take on the task of first fixing all the existing issues in the codebase"; read 2026-10-18
- **Relations:** derives from WAY-51
- **Verification:** an agent compares the work with the decision:
  - complies: a product whose code breaks the blocking rules in forty files marks the linter's
    invariant violated by a change the human accepts, and its test stands as an expected failure
    until the last file is clean; the task that brings a formatter reformats every file of the
    product once, and the formatter's invariant holds from that commit;
  - violates: the blocking rules are cut down to those the code already meets; the task that brings
    the linter cleans every file of the product; the formatter's invariant is marked violated;
    beside the linter's marked invariant stands a second one comparing the reports of each file
    with `{fork-point}`.
- **Origin:** none

*Rationale:* a rule weakened until the code meets it describes the accident, not the intent
(WAY-51), and cleaning the whole of the code in the task that brings the linter grows that task into
cleaning the product. The invariant stays whole and marked, so the debt shows at its entry, and old
code is cleaned when a task has it in scope. This takes the place of Google's condition that a
check is fixed across the whole code before it is turned on. A formatter rewrites the code
itself without changing what it does, so one reformatting leaves nothing to clean. Its weak point:
until the last file is clean, no test shows a report coming back into a cleaned file or reaching a
new one.
*Rejected:* only the rules the code already meets adopted — the rule is weakened until the code fits
it (WAY-51); the whole of the code cleaned in the task that brings a linter — that task grows into
cleaning the whole product.

### WAY-206 — What does the audit of a product's dependencies check?

The skill `maintain-coding-guidelines` proposes an audit of dependencies that checks a change and
fails it only where a version of a dependency that the change brings in against `{fork-point}` has a
known vulnerability, as the advisory database named by the product's decision adopting the audit
gives it when the check runs, of at least the severity that decision sets, every severity being
among the ways the skill offers. The template of the coding discipline carries no audit of the
whole tree of a product's dependencies. The signal of a vulnerability found in a dependency the
product already holds is the alerts of the service its repository lies on, on GitHub the Dependabot
alerts; the skill proposes that the product turn them on, and a human turns them on.

- **Scope:** product-guidelines, invariants
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/.github/workflows/audit.yml
  § lines 23-24 — "The ci.yml job passes `--baseline <base yarn.lock>` so a change fails only on
  advisories it introduces."; read 2026-10-18 · github-dependabot-alerts
- **Relations:** derives from WAY-202 · derives from WAY-60 · derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: a change that adds a library at a version with a known vulnerability of high severity
    fails in a product whose decision sets high; a change to a page's text passes on the morning an
    advisory is published for a dependency the product already holds; a product whose human chose
    every severity fails a change bringing in a version with an advisory of low severity; the skill
    proposes that the product turn on the alerts of its repository's service, and says that a human
    turns them on;
  - violates: the audit reads the whole tree on every change, and a change unrelated to the
    dependencies fails on an advisory published that morning; the template sets the threshold at
    high for every product; the audit reads a copy of the database the product committed months
    before; the template carries an audit of the whole tree of dependencies run every day; the
    skill turns the alerts on itself, or leaves a vulnerability found in a held dependency with no
    word of a signal for it.
- **Origin:** none

*Rationale:* an audit of the whole tree at every change fails a change that touches no dependency on
a vulnerability published that morning, so the audit checks what the change brings, against the fork
point; the decision takes that from Open Mercato's audit, which compares with a base (WAY-100). The
severity from which a vulnerability counts and the database read are conditions of the product's
invariant, so they stand in the decision that adopts the audit (WAY-60), and the severity is the
product's choice, every severity among the ways. The tools stand at pinned versions, while the
database is read as it stands when the check runs, so that a change brings in nothing known to be
vulnerable that day. The audit sees only what a change brings in, so a vulnerability found in a
dependency the product already holds reaches the product through the alerts of its repository's
service, which scan the repository when a new vulnerability is published and not only when a change
brings in a version, and are enabled by the repository's administrators; the owner answers an alert
with a task that raises the library. They are a setting of the service, no file of the repository,
so a human turns them on. Two weak points follow. The alerts are set outside the repository, so
nothing in it shows whether they are on, and they stay off until a human turns them on. A later run
on the same commit may record `fail` where an earlier one recorded `pass`, when an advisory is
published for a version that commit brings in; such a check is answered as any check that gives
different verdicts on one commit is, by a fix of the test with no quarantine recorded, which this
decision leaves unchanged.
*Rejected:* the whole tree audited at every change — an unrelated change fails on a vulnerability
published that morning; a copy of the database the product commits — nothing moves it apart from a
change, so it ages without bound, and a change bringing in a version first flagged after it passes;
the rule on a check that gives different verdicts on one commit narrowed so that a later `fail` on
the same commit is no such check — a new meaning of that rule for a rare case; a fixed threshold of
severity for every product, as Open Mercato's audit fails from high severity — the severity is the
product's choice; a daily run in CI of the
product's audit tool over the whole set of dependencies, as Open Mercato runs its audit on a
schedule beside the audit of a change — a second CI file in every product and a
run each day, a stronger change to this decision, for the one gain that the severity threshold
agrees with the audit of a change; no signal, the limitation accepted for good — with the alerts
off, a vulnerability of high severity in a dependency on the main branch passes with no signal, as
it did in a product whose alerts were off; a list of accepted advisories that the audit lets pass,
as Open Mercato's audit keeps — left out of what the decision takes from that audit.

### WAY-360 — Does the template of the coding discipline require a rule of the size of a function and a file, and how does it reach a product?

The template of the coding discipline requires, in the general file of a product's coding
guidelines, a rule of the size of a function and a file under the heading
`### Size of a function and a file`, after the six rules on failures and logs, with an invariant of
its own and a test of its own, outside the set of rules of the product's linter. A product sets its
thresholds after a trial run on its existing code and writes its exceptions in its decision on the
rule, or departs from the rule only by a decision of its log that gives the reason (WAY-173), and a
product that already has coding guidelines gets the rule by an ordinary extension, as the skill
`maintain-coding-guidelines` gives it for the rules on failures and logs. Where code other than the
exceptions of the product's decision stands over a threshold, the rule's invariant is marked
violated until that code is cleaned (WAY-51).

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-168
- **Verification:** an agent compares the template, the skill of the coding guidelines and a
  product's work with the decision:
  - complies: the required form of the general file holds `### Size of a function and a file` after
    `### Logging scope`, and the product's further rules follow it; a product whose code holds one
    function far longer than the rest sets its thresholds after the trial run shows it, lists that
    function as an exception with its reason in its decision where the human keeps it whole, and
    marks the rule's invariant violated where other code stands over; a product of one small script
    departs from the rule by a decision with its reason, and the heading holds `none — <PREFIX-NN>`;
    a refresh of a product's coding guidelines that finds the heading missing proposes the rule, and
    the human's yes makes the task an extension;
  - violates: the template offers the rule as a further rule a product may take up; the rule's test
    stands among the rules of the linter's set; a product leaves the heading out with no decision;
    the thresholds stand in the rule's text or are taken from the template instead of standing in the
    product's decision; a refresh passes over the missing heading in silence.
- **Origin:** none

*Rationale:* a product with no rule of size has no threshold, so a change stopped for standing over
a threshold and a plan that makes room first do nothing there, and a rule a skill only proposes stays
unadopted for as long as nobody takes the proposal up (WAY-202); required, the rule is left out only
by a decision that gives the reason (WAY-173). The rule stands outside the linter's set because that
set blocks only through rules every report of which leads to a change worth making (WAY-203), and a
long function that is best left whole is a case the product knows and records as an exception, which
keeps the threshold the product's choice and still lets it block. The thresholds come from a trial run
on the product's own code, since only that shows what a threshold stops and what already stands over
it, as the split of a linter's set comes from one (WAY-204). A threshold on a number was twice refused
as a rule, for the share of copies the tests fail (WAY-252) and for the words of a skill (WAY-256),
each as a number to chase; a size is a number the code itself holds, the product sets it from its own
code, and an exception is the way out for a function worth keeping whole. A refresh stays within what
the guidelines already cover and can only notice the rule's absence and put it to the human, where a
no stays on record as a departure and the absence does not read as an oversight. The price:
a product learns of the rule only at a change of its guidelines or when it opens an extension, a
count of lines says nothing of whether a function is well made, and a function can be split only to
stand under a threshold.
*Rejected:* the rule proposed as a further rule a product may take up, with no decision on departing
from it — a product with no rule has no threshold, so blocking a change over a threshold and the
change in a task's plan do nothing there, and a skill that only proposes the checks leaves it so for
as long as nobody takes the proposal up (WAY-202); no rule in the template, only the question about
the structure of code in the review — nothing blocks, since a finding of structure in a product with
no rule of size is graded Minor (WAY-363), and the assessment of structure depends on the reviewer's
impression.

### WAY-361 — How does the review of a change get the sizes of functions and files from a product?

The test of a product's rule of size, when it fails, names every function and file over a threshold
with its size, and the reviewer of the whole change runs it as an ordinary test of the product's
suite on the state before the change and on the state after it. A product has no command of its own
that gives the sizes of functions: the one command that runs all of its tests stays the only one
(WAY-16).

- **Scope:** product-guidelines, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-360 · derives from WAY-16
- **Verification:** an agent compares the template, the reviewer's run and a product's guidelines
  with the decision:
  - complies: a test of the rule of size that finds three functions and a file over their thresholds
    fails with a message naming each of the four, with its place and its size; the reviewer of the
    whole change runs that test in a worktree of the base and in one of the head, and reports the
    functions and files named after the change that were not named before it;
  - violates: the test stops at the first function over a threshold, or names a function with no
    size; a product's guidelines or instructions name a command that prints the size of each function
    beside the command that runs all the tests; the orchestrator runs a command of the product that
    counts sizes before the review and hands the reviewer its output.
- **Origin:** none

*Rationale:* the test of the rule of size is already a test of the suite, so running it on the base
and on the head costs the reviewer two runs and no new command, and the difference between its two
failures shows what the change pushed over a threshold and what it left; a failure that names every
function and file with its size gives the reviewer the numbers without a second tool. One command
runs every test so that no list of commands written by hand drifts from the tests (WAY-16), and the
rule of size needs no exception to that. The price: the test gives sizes only of what stands over a
threshold, so the size of a function under its threshold shows only in the diff.
*Rejected:* a command of the product that writes the size of each function of the files of a change,
run by the orchestrator before the review of the whole change — a new decision with a second exception
to WAY-16, a second command in every product and a step of the orchestrator in every cycle, for a
count of functions under the threshold, which by the threshold are in order.

## Rules of a product's tests

Where the rules of a product's tests stand, where a test takes its input and expected value, what an
assertion and a change of a test may do, and how tests keep trust boundaries, take in AI and leave
things untested.

### WAY-228 — Where does a test take the input it asserts on and the value it expects?

The template of the testing discipline requires the rule that a test takes the input it asserts on
and the value it expects written out, wherever the code under test would otherwise compute either,
and only the side it compares against comes from the run; a property test takes its inputs from a
test library's generator and its expected value from a relation the code under test does not
compute — undoing the operation, an invariant's sentence, or a simpler version written from the
requirement, not copied from the code — and a counterexample the library finds is kept as an
ordinary test with its values written out. A product departs from the rule only by a decision of
its log that gives the reason, and the rule binds a product from the task that writes its testing
guidelines.

- **Scope:** product-guidelines
- **Based on:** https://www.cis.upenn.edu/~bcpierce/papers/icse24-pbt-in-practice.pdf § 4.3 Writing
  Specifications — "These properties check that a pair of functions are inverses of one
  another—for example, parsing and pretty-printing or encoding and decoding functions." · § 4.3
  Writing Specifications — "A “differential property” (in sense of differential testing [25])
  compares the system under test to a reference implementation of the same functionality that
  serves as a specification; these are often also called model-based properties (c.f. model-based
  testing [54]), especially when the reference implementation is designed to be an abstract model of
  the original code."; read 2026-10-25 ·
  https://raw.githubusercontent.com/HypothesisWorks/hypothesis/5057a16cd98bf2882848a031d3d50f1d25ba8b73/hypothesis/docs/stateful.rst
  § Invariants — "Often there are invariants that you want to ensure are met after every step in a
  process."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-231 · derives from WAY-100
- **Verification:** an agent compares the tests of a product with the decision:
  - complies: a test of a price writes out the basket it feeds in and the total it expects; a
    property test of saving and loading generates game states and expects each state loaded to equal
    the state saved; a counterexample the library found stands as an ordinary test with that state
    written out;
  - violates: a test builds the total it expects by calling the function that computes the price; a
    test reads the value it expects, at run time, from the file the code under test reads; a property
    test of a sort expects what a copy of the sort's code returns.
- **Origin:** none

*Rationale:* two sides of a test computed by one code move together, and the test stays green
unseen; the rule stands in the testing guidelines, which an agent reads before it writes or changes
a test. A property test checks a relation over many generated inputs, so its expected value
is that relation; the rule takes from the practice of property tests, as developers apply them, the
relations that lie at hand — a pair of inverse functions, a reference implementation, a condition
kept after every step (WAY-100). The relation holds only
where the code under test does not compute it: a simpler version copied from the code makes the
test a mirror of it, which only the reviewer catches. A counterexample written out stays checked on
every run, whatever the generator draws next. The price: the rule is longer.
*Rejected:* the expected value alone written out — the input still moves with the code; a line
naming each file a test's verdict leans on, in place of values written out — every tracked file
becomes the data of some test; the rule left in the coding guidelines — a test written apart from
code meets no rule; no property tests — a whole class of tests that check a relation over many
inputs is barred; the rule left silent on property tests — a generated input breaks its letter, and
nothing says what holds instead; the classical properties of mathematics and of the theory of
computing, such as an operation that gives the same result in either order or a sort that changes
nothing when repeated, which developers also apply — left out of what the rule takes from the
practice of property tests; the property that only provokes a crash, with no relation to check —
left out of what the rule takes from the practice of property tests.

### WAY-231 — Where do the rules of a product's tests stand?

Testing is a discipline of a product's guidelines of its own: the-way gives a template of the
testing discipline, from which a product writes its file `guidelines/testing.md`, and the skill
`maintain-testing-guidelines`, which leads the work that creates and keeps that file. A kind of code
of a product's coding guidelines is code of the product other than its tests, and the patterns a
product's tests follow stand in its testing guidelines at the level of test they belong to.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-167 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a product keeps the rules of its tests and the exemplar test of each level in
    `guidelines/testing.md`, written from the-way's template of the testing discipline, beside
    `guidelines/coding.md`, whose table of kinds names endpoints and migrations and no kind of
    test;
  - violates: a product's coding guidelines name a kind `unit-test` with a file
    `guidelines/coding-unit-test.md`; the rules of a product's tests stand as a section of
    `guidelines/coding.md`; the-way's coding-guidelines skill settles where a product's tests take
    their expected values.
- **Origin:** none

*Rationale:* writing tests is work of its own: an agent writes either code or tests, and tests are
written apart from code and on other assumptions than the code, so an agent writing them needs one
place that says which behaviour gets a test, at which level and how, as an agent changing screens
finds its styleguide. Rules of tests kept among the coding guidelines would reach that agent only
through guidelines it reads to change code, and a test taken as a kind of code would have its
patterns cut by kind of code while its choices — the level, the source of the expected value, what
is left untested — follow the level and the behaviour. A discipline of its own gives the template
and the skill room to say what this work needs, as the styleguide and the coding guidelines have
theirs.
*Rejected:* the rules of tests added to the coding template as a kind of code named "test" — the
choices of tests do not follow kinds of code, and an agent writing tests apart from code meets them
only by way of the coding guidelines; the rules split between a product's guidelines and the steps
of the author and the reviewer of the-way's cycle — the whole meaning of a rule stands in two places
read apart; the same rules in both places — two copies drift apart.

### WAY-232 — Where does a test's expected value come from?

The template of the testing discipline requires the rule that the expected value of every test of a
product comes from a source other than the code under test — a document of the product its testing
guidelines name as a source, such as its decision log, its glossary or its task descriptions; a
relation the code under test does not compute; a crash counted as a failure; or a human's judgement
— and never from what the code gives today, snapshots and characterization tests included. Where a
test's name does not show the source of a value, a comment in the test names it, by the line of the
document or by the human and the date, and the review of a change asks of each assertion where its
value comes from.

- **Scope:** product-guidelines
- **Based on:** llm-test-oracle-actual-behaviour
- **Relations:** derives from WAY-173 · derives from WAY-228
- **Verification:** an agent compares the tests of a product with the decision:
  - complies: a test of a discount expects 15% and its name gives the decision of the product that
    sets the discount; a property test of saving and loading expects the loaded state to equal the
    saved one; a test of how a screen lays out a long name, which no document settles, expects
    what a human judged, with the human and the date in a comment;
  - violates: an expected value copied from what the function returns today; a snapshot
    regenerated when its test fails and accepted because the new output passes; a characterization
    test kept as a check of what the code does; a reviewer passes an assertion whose value names no
    source.
- **Origin:** none

*Rationale:* a test whose expected value is what the code gives today checks only that the code
still does what it did, a bug included, and a test that mirrors the implementation fixes its error
in place while it reads as a check; a model writing a test from the code tends to put into the
assertion what the code does rather than what is required of it. The sources named let an agent find
each value somewhere other than the code, and a comment shows the source where the name does not. A
snapshot and a characterization test are what the code gives today by construction, so an
exception for them would let the whole rule through. The question at each assertion is asked by the
reviewer, who reads every test of a change anyway (WAY-13), so the rule adds no step for the author.
Writing values out (WAY-228) leaves a value copied from a run standing; this rule closes that gap.
*Rejected:* a snapshot accepted once a human has approved it, and a characterization test marked as
a description — each is the output of the code as it stands, and an exception for them carries back
the value the rule refuses; the author checking each source as a step of its own beside the
reviewer — every change pays twice in cost and time for one check; values written out with no rule
on where they come from — a value copied from today's run meets that rule.

### WAY-233 — What does a change to an existing test need?

The template of the testing discipline requires the rule that changing the expected value of an
existing test, deleting a test, weakening an assertion, and skipping or disabling a test are one
kind of change, each made with its cause on the side of the data or of the requirement and a pointer
to the evidence of that cause, and that the review reads such a change made without them as masking
a defect. The rule lists the ways a test is weakened: equality loosened to "contains", a count
removed, a tolerance raised, a skip, a deletion.

- **Scope:** product-guidelines
- **Based on:** impossiblebench-test-modification ·
  https://raw.githubusercontent.com/abseil/abseil.github.io/e9e24835cb889fe25251cb9ec6d51b79233e358d/resources/swe-book/html/ch12.html
  § Strive for Unchanging Tests, Bug fixes — "Again, bug fixes typically shouldn’t require updates
  to existing tests." · § Strive for Unchanging Tests, Behavior changes — "Changing a test in this
  case indicates that we’re breaking an explicit contract of the system, whereas changes in the
  previous cases indicate that we’re breaking an unintended contract."; read 2026-10-25 ·
  https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-code-review/references/review-checklist.md
  § 4. Tests, line 106 — "Were any assertions weakened to make the suite pass — equality loosened to
  "contains", exact counts removed, tolerances raised, assertions deleted, tests skipped or marked
  pending? (major)"; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-100
- **Verification:** an agent compares the change with the decision:
  - complies: a change raises the expected total of an order because the product's decision on its
    tax changed, and names that decision; a reviewer reads an assertion turned from equality into
    "contains", with no cause given, as masking a defect;
  - violates: a test is skipped with "flaky" as its cause and no evidence; a test that turned red is
    deleted in the change that turned it red, with no cause; a tolerance is raised so that a new
    result passes.
- **Origin:** none

*Rationale:* a good test changes only when its requirement does, so a change that moves an expected
value while neither the data nor the requirement moved says that the code moved, and the move is a
defect until shown otherwise. An agent that a failing test stands in the way of changes the test,
and a new value, a looser assertion, a skip and a deletion each turn the build green the same way,
so one rule covers them all; the rule takes from Open Mercato's review checklist its list of
weakenings (WAY-100), which lets a reviewer recognize them. A test that was wrong may rightly
change, so the rule asks for the cause and its evidence rather than forbidding the change.
*Rejected:* existing tests never changed — a wrong test could never be corrected; a cause asked only
of a changed expected value — a skip or a looser assertion masks the same defect; a test replacing
an old one required to be seen failing on the code before the fix — a ritual of its own for each
ordinary test, where only an invariant's test is seen failing once (WAY-08); the grade `major` that
Open Mercato's checklist gives a weakened assertion — left out of what the rule takes from that
checklist.

### WAY-234 — What may a test's assertion check?

The template of the testing discipline requires the rule that a test's assertions check the
behaviour its rule or its task requires, a detail of how the code carries it out that the
requirement does not ask for being no condition of the test passing, and that the review asks of
each assertion whether the code could change so that the required behaviour stays and the assertion
breaks, a yes marking a detail. A check of the case's setup is allowed where it stands before the
action, is marked as a precondition and checks a property of the case that the requirement names,
never the structure of the data that builds the case.

- **Scope:** product-guidelines
- **Based on:**
  https://raw.githubusercontent.com/abseil/abseil.github.io/e9e24835cb889fe25251cb9ec6d51b79233e358d/resources/swe-book/html/ch12.html
  § Strive for Unchanging Tests — "Therefore, the ideal test is unchanging: after it’s written, it
  never needs to change unless the requirements of the system under test change." · § Test State,
  Not Interactions — "Interaction tests tend to be more brittle than state tests for the same reason
  that it’s more brittle to test a private method than to test a public method: interaction tests
  check how a system arrived at its result, whereas usually you should care only what the result
  is."; read 2026-10-25
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the tests of a product with the decision:
  - complies: a test that a running action is not interrupted checks that the action finishes; a
    test of a refused request checks that it is refused, not the wording of the message; a test of
    a rule that applies from thirty members first checks, marked as a precondition, that its
    population has thirty members;
  - violates: a test compares word for word the record of a running action that holds a rule's
    index, so that a lasting identifier in place of the index breaks it while no action is
    interrupted; a test asserts the order of internal calls where only the result counts; a check of
    the setup reads the private list that the builder of the case filled.
- **Origin:** none

*Rationale:* a test that breaks under a change keeping the required behaviour has to be fixed by
every later change, which teaches whoever meets it to rewrite failing tests, and the test stops
telling a defect from a refactoring; the ideal test changes only with its requirement, and the
reviewer's question turns that into one asked at each assertion. A test sometimes has to know that
its case is the one the requirement names, such as that the population a measure counts exists,
before it acts; a check placed and marked as a precondition says so without making the setup a
condition of the product, while one written against the structure of the data would bring the
detail back.
*Rejected:* every check of the setup barred — a test could not show that it built the case the rule
applies to; a general exception for comparing a whole state — every detail of that state becomes a
condition of passing; the rule held for the tests of invariants alone — an ordinary test pins the
same details.

### WAY-235 — How do a product's tests keep its trust boundaries?

The template of the testing discipline requires, and the skill `maintain-testing-guidelines`
proposes, for each trust boundary of the product's part map at least one invariant that the
boundary refuses crafted input or unauthorised access, checked by a permanent test that checks the
refusal directly, takes the expected refusal from the product's decisions on permissions and is
seen failing once; a boundary that does not refuse today has that invariant marked violated as
WAY-51 gives it, and a boundary that is only the configuration of someone else's service stays with
the review of WAY-48. For authorization, the rule of the product's testing guidelines holds a table
of who, which resource and which action with the expected result, each row naming the decision on
permissions it comes from. In the area of trust boundaries this decision prevails over WAY-168: the
*Invariant* of the rule on trust boundaries names the refusal invariant of each boundary, although
its test checks the product's behaviour rather than a convention of the product's code.

- **Scope:** product-guidelines, invariants
- **Based on:**
  https://raw.githubusercontent.com/OWASP/CheatSheetSeries/cefb3e95ae33162bac8339ed15a265ed738aaf1a/cheatsheets/Authorization_Regression_Testing_Cheat_Sheet.md
  § Introduction — "Authorization implementation is rarely static." · § Define the Access Policy
  Model — "Before writing tests, explicitly define the application's access model using the
  Actor-Resource-Action pattern" · § CI/CD Gating and SDLC Integration — "Blocking PR Builds: The
  authorization test suite must be a required check in the CI/CD pipeline (e.g., GitHub Actions,
  GitLab CI)."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-48 · derives from WAY-08 · derives from
  WAY-51 · narrows WAY-168
- **Verification:** an agent compares the work with the decision:
  - complies: the server of a game, the trust boundary of its part `api`, gets the invariant that a
    player cannot read another player's saved game, whose test sends that request with another
    player's token, expects the refusal the decision on permissions gives and is seen failing once;
    the table of the rule gives, for an anonymous visitor reading saved games, a refusal and the
    decision it comes from; a product whose login is only the settings of an outside provider keeps
    that boundary with the review;
  - violates: a boundary is left to the review because its test would take long to write; the test
    of a boundary checks only that the server does not crash; a boundary that lets a crafted request
    through today gets no invariant until it is fixed; the rule on trust boundaries reads `none` in
    *Invariant* because its tests check behaviour rather than a convention of the code; the table of
    permissions stands in a decision of the product.
- **Origin:** none

*Rationale:* authorization rarely stays still: a new endpoint or a reworked query breaks a refusal
that no review of that change looks for, while a permanent test checks it on every change. A refusal
is behaviour, not a convention of the code, yet a cheap test checks it on every change, so here the
rule names an invariant where WAY-168 would leave it to the review. An invariant already has its
test seen failing once and the mark of a rule the product breaks today, so the rule needs no
mechanism of its own, and the failure seen shows that the refusal comes from the check of
permissions rather than from a fault elsewhere. The expected refusal is a value like any other, so
it comes from the product's decision on permissions (WAY-232). The table of who, what and how stands
in the guidelines, since a decision has no place for a table, and each row names its decision, so
that the meaning stands once. A boundary that is only someone else's configuration would have its
test check someone else's code. The price: a product's invariants grow by entries of security, the
benefit rests on standards rather than on a measurement, and the rule is only as good as the part
map that names the boundaries.
*Rejected:* a permanent test of refusal with no invariant — a second rule of a test seen failing
once beside WAY-08's; the review aimed at the boundary alone, as WAY-48 gives every change touching
it — a refusal broken by a change to another part passes unseen; the table of permissions held in a
decision — a decision holds one to three binding sentences and no table.

### WAY-236 — How does AI enter a product's tests?

The template of the testing discipline requires the rule that AI is no level of test: a test an AI
wrote follows every rule of the testing guidelines, an agent exploring the running product finds
cases that become ordinary tests, and a tool that heals a test by itself changes only how the test
finds what it acts on, a changed assertion or a red test turned into a skipped one being a change of
an existing test (WAY-233). An AI judge enters a permanent test only where the behaviour cannot be
checked by a plain comparison, its verdict is yes or no, it has been checked on examples a human
judged and runs on a pinned version of its model, and the testing guidelines say how they treat the
spread of its verdicts; how each AI tool the product's tests use behaves stands in an environment
fact of the product, naming the version the product uses, with the date its source was read.

- **Scope:** product-guidelines
- **Based on:** computer-use-agent-web-testing ·
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (archived:
  http://web.archive.org/web/20261017091633/https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents,
  2026-10-17) § Step 5: Design graders thoughtfully — "We recommend choosing deterministic graders
  where possible, LLM graders where necessary or for additional flexibility, and using human graders
  judiciously for additional validation." · § Step 5: Design graders thoughtfully — "LLM-as-judge
  graders should be closely calibrated with human experts to gain confidence that there is little
  divergence between the human grading and model grading."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-233 · derives from WAY-100
- **Verification:** an agent compares the tests of a product with the decision:
  - complies: a test an agent generated from a task's description takes its expected value from the
    decision that description names; an agent clicking through a new screen finds that a form takes
    an empty name, and the change adds an ordinary test of that refusal; a judge model says yes or
    no to whether a generated summary names the items of the order, checked on examples the product
    owner judged, its model version pinned, and the guidelines require every one of three runs to
    pass;
  - violates: a run of an exploring agent stands in the suite as a test; a self-healing tool
    rewrites an assertion to the new text of a screen; a judge gives a score from one to ten; a
    judgement of a screenshot by a model stands where a plain comparison of the rendered numbers
    would do.
- **Origin:** none

*Rationale:* a test an AI writes is code like any other, and the faults of tests — a value copied
from the code, an assertion on a detail — reach it the same way, so it needs no rule of its own. An
agent that tests a running web application from scratch is far from reliable at finding its defects,
so its run is no permanent test, while a case it finds, written as an ordinary test, gives the same
verdict on the same code every time. A judge's verdict varies from run to run and costs more, so the
rule takes from Anthropic's recommendation for the evaluation of agents the order of a
deterministic check first and a judge only where none exists (WAY-100); checked on examples a
human judged and pinned to one model, its verdict can be
trusted as far as those examples reach. A tool that heals a test by changing what it asserts fits
the test to a state that may be wrong, the masking WAY-233 names. AI tools change faster than the
rest of what a product runs, so the version and the date read let a reader see what a test stands
on. The price: checking a judge takes examples a human judged, repeated runs multiply the cost of a
run, and the conditions are carried over from the evaluation of agents to a product's tests as an
inference.
*Rejected:* an AI judge barred from permanent tests — a behaviour no plain comparison can check
stays untested; guidelines silent on AI — each task lets AI into tests on terms of its own; partial
credit for a task of several parts, which Anthropic's recommendation builds into a grade — left out
of what the rule takes from that recommendation; a way out for the judge, which answers "Unknown"
where it lacks the information — left out of what the rule takes from that recommendation; a rubric
with each dimension of a task graded by a judge of its own — left out of what the rule takes from
that recommendation.

### WAY-237 — What does a product deliberately not test, and where is it said?

The template of the testing discipline requires a section `## Not tested on purpose` of a product's
testing guidelines, in which each item is a category of behaviour or of code, never a single file
or test, and names the product's decision that excludes it, whose binding sentences give the
condition under which the category is tested again and whose rationale gives the reason; the
section reads `none` where nothing is excluded. A trust boundary never stands in it.

- **Scope:** product-guidelines
- **Based on:** https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
  § 1.3. Testing Principles — "Exhaustive testing is impossible. Testing everything is not feasible
  except in trivial cases (Manna 1978)." · § 5.2.4. Product Risk Control — "With respect to product
  risk control, once a risk has been analyzed, several response options to risk are possible, e.g.,
  risk mitigation by testing, risk acceptance, risk transfer, or a contingency plan (Veenendaal
  2012)."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-100
- **Verification:** an agent compares the guidelines of a product with the decision:
  - complies: a game's guidelines exclude the exact numbers of its balance, naming the decision
    whose binding sentences have its balance tests check assumptions only until the balance is
    settled; a product that excludes nothing reads `none`;
  - violates: an item names one test file skipped for a deadline; an item gives its reason in the
    guidelines and names no decision; the product's login stands in the section.
- **Origin:** none

*Rationale:* with nothing written, a missing test and a choice not to test look the same, and an
agent treats every absence as a gap to fill; an item turns that silence into a choice a human
approved. Testing everything is impossible, and accepting a risk is a legitimate answer to one, so a
product names the risks it accepts. An item by category stays short and cannot be read as leave to
skip any single test. The reason and the condition stand in a decision, where approval and the
search of the foundation reach them; the condition is part of what the decision allows, read
whenever a change reaches the category, not a date of review (WAY-24). A trust boundary is where a
missing check is the fault itself, so it is never excluded. The rule takes from the
10xDevs course on agentic development its section of what is deliberately not tested, each item
with its reason and the change that calls for its re-evaluation; the course keeps it in its plan of
tests, and here it stands in a product's guidelines (WAY-100); the lessons of the course are not
open to a reader of this repository. The kinds of tests without
value the template gives among its examples — a duplicate of another test, a test of trivial code, a
loop over nearly identical inputs — come from how Limen trimmed its own tests
(https://raw.githubusercontent.com/overment/limen/89ef3786a6c2f893b2d31cd9944ad76c483f7841/spec/features/done/2026-10/F776-trim-low-signal-tests/notes.md
§ What was cut — "Duplicates. The same rule was proven twice. The stronger, end-to-end test stays." ·
§ What was cut — "Trivia. Tests that pin constants" · § What was cut — "Variants. Loops over
near-identical inputs shrank to representative cases"; read 2026-10-25), and as examples they bind
nothing. The price: each exclusion is a decision to approve, and the section ages where nobody
checks its conditions.
*Rejected:* exclusions held only as decisions of the log, with no section in the guidelines — an
agent writing tests does not find them where it reads; items giving their reasons with no
decision — an exclusion binds with no approval; a single test as an item — the section becomes a
list of excuses; the plan of tests of the course as the place of the section — a task's refinement
holds no plan of tests (WAY-238).

## Test levels, flaky tests and mutation

The levels of a product's tests with their recipes and exemplars, when testing guidelines come into
being, what a bug caught late gets, how a flaky test is treated and how a mutation tool checks the
tests.

### WAY-238 — At which level does a test stand, and who chooses it?

The template of the testing discipline requires the rule that a test stands at the lowest level at
which the break it names turns it red, unless going lower would mean replacing with a double exactly
what can break, and a product's testing guidelines give no proportion of levels. The author of a
change chooses, in the task's cycle, which behaviour gets a permanent test and at which level,
naming the break each test catches, and the review checks the choice against the product's testing
guidelines, while a task's refinement holds no plan of tests.

- **Scope:** product-guidelines, task-cycle, project-level
- **Based on:** https://martinfowler.com/articles/practical-test-pyramid.html (archived:
  http://web.archive.org/web/20261014080941/https://martinfowler.com/articles/practical-test-pyramid.html,
  2026-10-14) § Avoid Test Duplication — "Push your tests as far down the test pyramid as you can" ·
  § Avoid Test Duplication — "If a higher-level test gives you more confidence that your
  application works correctly, you should have it."; read 2026-10-25 ·
  https://learn.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable (archived:
  http://web.archive.org/web/20260521141733/https://learn.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable,
  2026-05-21) § Write tests at the lowest possible level — "It's not feasible to test every aspect
  of a service at this level, but the principle is to use lighter unit tests if they can produce
  the same results as heavier functional tests."; read 2026-10-25
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: the rule of a price gets a unit test, since a break of its arithmetic shows there; a
    query to the product's own database is tested against a real database, since a double of the
    database would replace what can break; the author of a change names, for each new test, the
    break it catches and why no lower level shows it;
  - violates: a product's guidelines ask for seven unit tests in ten; a task's document lists the
    tests its change is to add; an end-to-end test checks every branch of a calculation that a unit
    test shows.
- **Origin:** none

*Rationale:* a break a lower test shows is found sooner, traced more exactly and run more cheaply,
and a higher test spends time on what a lower one already shows; a lighter test replaces a heavier
one only where it gives the same result, so a lower test that replaces what can break no longer
catches it, and a higher test stays where it adds confidence. A proportion reads as a target, and an
agent counting it writes tests to even out numbers, while the models of a right mix disagree and
grew from different kinds of products. Which behaviour gets a permanent test is judged best with the
change in hand, by the author who names the break, and the reviewer, who reads the change, checks
the choice against the guidelines; a plan of tests written in refinement, before the change exists,
would be a guess. The price: naming a break takes judgement that a human who does not read tests
cannot check.
*Rejected:* a pyramid or a share of each level — numbers to even out rather than breaks to catch;
the choice made in the task's refinement — before the code it is a guess, and the task's document
would carry a plan of tests; a plan of tests or a map of risks for a whole project — the scenarios
live in the tests themselves, and what gets a permanent test is agreed while the task is made.

### WAY-239 — What does a bug caught only by a high-level test or by a human get?

The template of the testing discipline requires the rule that a bug which only a high-level test or
a human caught also gets a test at the lowest level that catches it.

- **Scope:** product-guidelines
- **Based on:** https://martinfowler.com/articles/practical-test-pyramid.html (archived:
  http://web.archive.org/web/20261014080941/https://martinfowler.com/articles/practical-test-pyramid.html,
  2026-10-14) § Avoid Test Duplication — "If a higher-level test spots an error and there's no
  lower-level test failing, you need to write a lower-level test"; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-238
- **Verification:** an agent compares the change with the decision:
  - complies: an end-to-end test finds a total one cent off, and the fix adds a unit test of the
    rounding; a player reports a crash on an empty save, and the fix adds a test that loads an empty
    save;
  - violates: the fix of a bug an end-to-end test found keeps only that test; a bug a human reported
    is closed with its fix and no test.
- **Origin:** none

*Rationale:* a bug that passed every lower test shows a case the lower tests miss; a test at the
lowest level that catches it traces the next occurrence to its cause, runs fast and stays as a test
of that regression, while the high test alone says only that something broke somewhere, and a bug a
human found had no test at all.
*Rejected:* the bug left with only the high-level test that caught it — the next occurrence is found
late and traced slowly.

### WAY-240 — How do a product's testing guidelines name its test levels?

The template of the testing discipline requires that a product's testing guidelines name its test
levels, each with the product's decision that sets it, and that a level whose name means in the
product something other than in the field, "integration" above all, is a term of the product's
glossary, defined by the resources a test of that level may touch, such as files, the network or a
browser. For each part the guidelines apply to, they say in one sentence whether its complexity lies
in computation or in its connections. In the area of the names of test levels this decision
prevails over WAY-95: a level named in the product otherwise than in the field, a narrower meaning
included, takes a glossary entry whether or not a sentence would be read wrongly.

- **Scope:** product-guidelines, glossary
- **Based on:** none
- **Relations:** derives from WAY-173 · narrows WAY-95
- **Verification:** an agent compares the guidelines of a product with the decision:
  - complies: a game's guidelines name its levels unit, integration and end-to-end, its glossary
    defines "integration test" as a test that may touch files and a local server and no browser,
    and the table of levels names that term without copying it; the guidelines say that the
    simulation's complexity lies in computation and the account server's in its connections; a
    level the game names more narrowly than the field takes its glossary entry although no
    sentence of its guidelines reads differently for the field's meaning;
  - violates: the guidelines use "integration" with no glossary entry while their integration
    tests open a browser; the table of levels repeats the definition the glossary holds; a level is
    defined as "tests several parts together"; a level named more narrowly than the field takes no
    entry because no sentence would be read wrongly.
- **Origin:** none

*Rationale:* "unit" and "integration" mean different things to different teams, and much of the
dispute over the right mix of tests is a dispute over the words; a level defined by what its test
may touch can be checked without judgement. A word that means something of its own in the product is
an entry of its glossary (WAY-95), where it is defined once and keeps one meaning in the guidelines
and in the tests. For the name of a level this decision prevails over WAY-95, since under WAY-95 a
level named more narrowly than the field would take an entry only where a sentence reads wrongly,
and a level without an entry stays without any definition, the table of levels carrying none. Its
weak point: the glossary takes an entry for every such level, also where no sentence misleads a
reader. Where a part's complexity lies tells which level catches its breaks: computation shows in
tests that touch nothing outside the code, connections only in tests that reach them.
*Rejected:* each level defined in the guidelines' own table — a second definition beside the
glossary, and the two drift apart; the meaning of "integration" left to each reader — tests of one
name touch different things; this decision narrowed to WAY-95's rule, an agent judging at each
level whether a sentence misleads — a level without an entry stays without any definition, and the
dispute over "integration", for which this decision was made, returns; the two decisions left
without a precedence — the first task to write a product's testing guidelines meets two rules with
none between them (WAY-25), which costs a blocking remark and a round of fixes.

### WAY-241 — What does the recipe of a test level hold?

The template of the testing discipline gives a product's testing guidelines, for each level, a
recipe of the same fields — what the level is for and when not to use it, where its files lie and
how they are named, the name and build of a test, its doubles, its data, time and randomness, the
level's exemplar test, the command and the time limit — each field that binds naming the product's
decision that carries it, a field naming none standing as an example, and a field that repeats
another level's reading "as in <level>". The field of the command names the gate and how it narrows
to the level, a file or a test, where the gate can, and otherwise reads `none`; the field of the
time limit points to the configuration file that holds it, and reads `none` where no configuration
file holds one; and no recipe lists commands of the test tool of its own.

- **Scope:** product-guidelines
- **Based on:**
  https://raw.githubusercontent.com/abseil/abseil.github.io/e9e24835cb889fe25251cb9ec6d51b79233e358d/resources/swe-book/html/ch13.html
  § How to Decide When to Use a Real Implementation — "A real implementation is preferred if it is
  fast, deterministic, and has simple dependencies." · § TL;DRs — "A fake is often the ideal
  solution if a real implementation can’t be used in a test." · § Prefer to perform interaction
  testing only for state-changing functions — "In general, you should perform interaction testing
  only for functions that are state-changing."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-16 · derives from WAY-168
- **Verification:** an agent compares the guidelines of a product with the decision:
  - complies: the recipe of unit tests gives the gate and its narrowing to the directory of unit
    tests, and points to the configuration file of the test tool for the time limit; the field of
    doubles of integration tests names the product's decision to run them against a real database;
    the recipe of end-to-end tests reads "as in unit tests" for its data;
  - violates: a recipe lists a command of the test tool for its level beside the gate; the field of
    the time limit reads "5 s", or stays empty where no configuration file holds a limit; a field of
    doubles binds a change while it names no decision.
- **Origin:** none

*Rationale:* the same fields for every level let an agent find what binds at any level in one place,
and a small product writes a field once and points to it from the others. A field binds only where a
decision of the product carries it (WAY-173), so the template's defaults for the build of a test,
its doubles, its data and its time are proposals a product adopts or departs from. One command runs
every test (WAY-16), so the recipe gives that command and how far it narrows, and a command of the
tool beside it would be a second list that drifts; a product whose gate cannot narrow gets narrowing
only by a change of its code. A time limit copied into the guidelines goes stale beside the
configuration that holds it, and where none holds a limit the field reads `none`, as the field of
the command does, so that no product words its own way of saying so. The default order of doubles —
the real thing where it is fast, deterministic and simple, then a working simpler version, then a
stub or a mock — follows the preference for real implementations, with a check of a call kept for an
effect outside the product.
*Rejected:* commands of the test tool for each level, as an exception to WAY-16 — a list of checks
written by hand beside the gate; no field of the command — an agent looking for how to run one level
finds nothing; the value of the time limit in the recipe — a copy of the configuration that goes
stale.

### WAY-242 — How is the exemplar test of a level designated?

The exemplar test of a level of a product's tests is designated by a decision of the product, as the
exemplar of a kind of code is: where the level already has tests, the skill
`maintain-testing-guidelines` compares them and proposes the exemplar from that comparison, and
where it has none, its first test becomes the exemplar. That designation is approved in a task's
refinement only where the task's required outcome is itself a test of that level, its document
naming the level and that the task's first test of it becomes the exemplar, with no list of tests
and no path; where the author of a change chooses in the task's cycle to write a level's first
test, it is approved at a blocked draft request, as WAY-172 gives a meaning the task's document does
not settle. Until a decision designates it, the field of the exemplar in the level's recipe stands
empty, and designating another test is a change of that decision.

- **Scope:** product-guidelines, project-level
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-172
- **Verification:** an agent compares the work with the decision:
  - complies: in a product with twelve integration tests the skill compares them and proposes the
    one that sets up its data through the product's fixtures, and the human approves the decision
    naming its path; the document of a task whose outcome is the product's first end-to-end test,
    of the sign-up journey, says that this test becomes the level's exemplar, and its cycle writes
    the decision with the test's path; a cycle whose author chooses to check a query with the
    product's first integration test proposes the decision designating that test at a blocked draft
    request;
  - violates: a recipe names as its exemplar a test no decision designates; the empty field holds a
    placeholder; a cycle points the field to another test on its own; the refinement of a task that
    adds a discount rule designates the task's first unit test as that level's exemplar and gives
    its path; a cycle designates the first test of a level it chose and leaves the decision to the
    merge.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of
every later one, while a test a decision designates is one a human approved. Who designates follows
the state of the level, as for a kind of code: a comparison where tests exist, and the first test
where none does, since an exemplar's material is made by its first instance. Refinement can approve
the first test's designation only where the task's required outcome shows the level, as it assigns
a first kind's exemplar where the requirement shows the kind (WAY-216); elsewhere the level of a
test is the choice of the change's author and a task's refinement holds no plan of tests (WAY-238),
so the designation reaches the human where WAY-172 puts a meaning the task's document does not
settle. An empty field says plainly that none is designated, where an invented model would be
copied, and designating another test changes a meaning of the guidelines (WAY-172).
*Rejected:* the exemplar chosen by an agent of the cycle with no approval — a test nobody approved
becomes the model; an exemplar the template gives every product — it fits no product's tools; a
placeholder in the empty field — it reads as a designation; the designation approved in the
refinement of every task that is to write a level's first test — the refinement would choose the
level and the test, which WAY-238 leaves to the change's author; the designation always left to a
blocked draft request — a task whose outcome is itself a level's first test would stop for what its
document could carry.

### WAY-243 — How is a flaky test treated?

The template of the testing discipline requires the rule that running a flaky test again serves only
the diagnosis of what makes it flaky, never making a run of the gate pass, and that disabling or
deleting such a test is a change of an existing test under WAY-233.

- **Scope:** product-guidelines
- **Based on:**
  https://raw.githubusercontent.com/abseil/abseil.github.io/e9e24835cb889fe25251cb9ec6d51b79233e358d/resources/swe-book/html/ch11.html
  § Case Study: Flaky Tests Are Expensive — "Just keep in mind that rerunning a test is only delaying
  the need to address the root cause of flakiness."; read 2026-10-25
- **Relations:** derives from WAY-173 · derives from WAY-233
- **Verification:** an agent compares the change with the decision:
  - complies: a test that fails once in ten runs is run again to find that it waits a fixed time,
    and the change makes it wait for the event; a flaky test is deleted with the cause that the
    behaviour it checked was removed and a pointer to the decision that removed it;
  - violates: the configuration of the gate runs a failing test again until it passes; a flaky test
    is skipped with "flaky" as its only cause; a flaky test stands on a list of quarantined tests.
- **Origin:** none

*Rationale:* a test that passes on a second run hides the fault that made it fail, in the test or in
the product, and each run again trades that fault's cause for a green result; a verdict of the gate
means something only while a red run is answered. A flaky test disabled or deleted loses its check
as surely as a test skipped for a failing change, so it takes the same cause and evidence. The rule
on a check that gives different verdicts on one commit gives the test of an invariant the same
answer.
*Rejected:* a quarantine of flaky tests, with a limit for fixing them — a second state of tests to
keep, which ages, as that rule refuses it for the tests of invariants; automatic runs again in the
gate — the fault stays hidden; every flaky test fixed before the next change — unrelated work stops
for it.

### WAY-244 — When do a product's testing guidelines come into being?

The skill `maintain-testing-guidelines` proposes that a product's testing guidelines come into being
before the first task that writes the product's tests.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: a product whose plan brings its first code, and with it its first tests, gets a task
    of testing guidelines first, which settles its levels and the recipe of each before any test
    exists;
  - violates: the first tests are written and the testing guidelines are written from them
    afterwards.
- **Origin:** none

*Rationale:* the first tests written with no guidelines are the tests every later one copies — the
level they stand at, where their values come from, what they replace with doubles — as a first
screen built with no rules is the one every later screen copies, and guidelines brought to
them afterwards meet tests to rewrite. The price: a pressing fix in a product with no testing
guidelines waits for them too, and every task with code in such a product waits for the task that
writes them.
*Rejected:* the testing guidelines written from the first test — that test is written with no rules;
the testing guidelines written by the first task that needs them — they shrink to that task's needs.

### WAY-252 — How does a mutation tool check a product's tests?

The template of the testing discipline requires the rule that a mutation tool — one that makes
copies of the code, each with one small fault, and runs the product's tests on each copy — runs, at
a change, on the changed files of each part the product adopts it for, never on the whole product,
and that the reviewer of the change classifies each copy no test fails as a real gap, which gets an
assertion, an equivalent mutant, which behaves as the code does and is passed over, or a change not
worth pinning, which is passed over with its reason; the rule sets no threshold on the share of
copies the tests fail. A product adopts the rule by a decision naming the tool and the parts it runs
on, chosen among the parts whose complexity lies in computation, or departs from it by a decision
that gives the reason.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-240
- **Verification:** an agent compares the work with the decision:
  - complies: a game's testing guidelines adopt the rule for its simulation, naming its mutation
    tool, and a change to the rule of heat runs the tool on the changed file alone; the reviewer
    passes over a copy that changes only which object is returned, not its value, giving that
    reason; a product whose parts only pass requests on to other services departs from the rule by
    a decision that gives that reason;
  - violates: a product's testing guidelines require the tests to fail on nine copies in ten; a
    reviewer asks for assertions until every copy fails; the tool runs on every file of the product
    at each change; a product's testing guidelines leave the rule out with no decision.
- **Origin:** none

*Rationale:* a check of the tests made in an author's head leaves no trace and cannot be confirmed,
while a tool makes the faults and runs the tests itself, and where a tool can do a check, the tool
does it rather than an agent. What a surviving copy means still takes judgement: some copies behave
as the code does, and some change only what no requirement asks for, so the tool replaces making the
faults, not deciding about the copies that survive. A share of copies the tests fail reads as a
target, and chasing it writes tests that pin details of the code (WAY-234). The faults such copies
make — a bound, a sign, a branch — are faults of computation; in a part whose complexity lies in its
connections, they mostly break what a double replaces, so the tool runs where computation lies
(WAY-240), and narrowed to the files of a change, a run stays short. Its weak points: every product
with testing guidelines makes one decision about the rule, even one with nothing to mutate, and a
product that adopts a tool pays for its configuration.
*Rejected:* a row of the table that chooses the level of a test — the check of tests is no level of
test, and a row holds neither the classification nor the choice of a tool, while the product adopts
the table whole; a threshold on the share of copies the tests fail — a number to chase; a run over
the whole product at each change — slow, and its surviving copies lie outside the change; the rule
binding every product directly — rigid for a product with no computation (WAY-173).

### WAY-253 — Who runs a mutation tool in a task's cycle, and what does the author check in its place?

Where a product's testing guidelines adopt a mutation tool for a part (WAY-252), the agent that
reviews a change reaching that part — a slice, the whole change, a fix of findings or a correction
after the human's remarks — runs the tool on the files of that part the reviewed diff changes and
classifies itself each copy no test fails, and the author of the change does not mutate that part's
code in their head. In every other part, the author mutates the code in their head before
finishing — a wrong constant or branch, a missing side effect, an empty return, unchecked empty or
hostile input — and treats a mutation no test catches as behaviour left unprotected.

- **Scope:** task-cycle, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-252 · derives from WAY-10
- **Verification:** an agent compares the work with the decision:
  - complies: a change to a game's rule of heat reaches its simulation, for which the guidelines
    adopt a mutation tool; the author makes no mutation in their head there, and the reviewer runs
    the tool on the changed file and classifies each surviving copy; a correction after the human's
    remarks changes the same file, and its reviewer runs the tool again; a change to a part no
    adopted tool covers gets the author's check in the head;
  - violates: the author runs the tool and hands the reviewer a list of surviving copies; the author
    both mutates the code in their head and leaves the same part to the tool; the reviewer of a fix
    leaves the tool unrun on a part the guidelines adopt it for.
- **Origin:** none

*Rationale:* the reviewer did not write the tests, so its run and its classification check them as
an agent apart from the change (WAY-10), from the tool's output rather than from an author's
summary of it; an author who sees the surviving copies first is drawn to kill each with an assertion
pinned to a detail. A check in the head where a tool runs repeats the tool's work at the cost of the
author's effort. Every review whose diff reaches such a part runs the tool, so no fix or correction
escapes both the tool and the check in the head. Its weak points: a real gap the tool finds returns
to the author as a finding of the review, one round of fixes more than if the author had run the
tool, and a planned change pays for a run at a slice and again at the whole change.
*Rejected:* the author runs the tool and passes the surviving copies to the reviewer — the reviewer
judges a list the author prepared, and the author is drawn to chase the copies; the author's check
in the head beside the tool — the same check twice.

### WAY-254 — Where does the command of a mutation tool stand?

The command that runs a product's mutation tool stands in the rule of mutation testing of the
product's testing guidelines (WAY-252), and no CI configuration, recipe of a level or instruction
file names it. In the area of the command of a product's mutation tool this decision prevails over
WAY-16.

- **Scope:** product-guidelines, task-cycle, instruction-files
- **Based on:** none
- **Relations:** derives from WAY-252 · narrows WAY-16
- **Verification:** an agent compares the work with the decision:
  - complies: the rule of mutation testing in a product's testing guidelines gives the command that
    runs the tool on the files of a change, and the product's `AGENTS.md` names the gate alone;
  - violates: the product's CI runs the mutation tool on every pull request; a recipe's field of the
    command gives the mutation tool's command; the product's `AGENTS.md` names the mutation tool's
    command as a way to check a change.
- **Origin:** none

*Rationale:* one command runs every test so that no list written by hand drifts from the tests, in
which a test left out never runs and a broken change passes (WAY-16). A mutation run is a check the
reviewer makes and admits no change by itself; it asks whether the tests notice faults. A test its
command leaves out lets more copies survive, and the reviewer, classifying them, at worst asks for
an assertion another test already makes, so the drift WAY-16 guards against costs here an extra
assertion, never a broken change let through. A mode of mutation taught to each product's gate
would add code to every product that adopts a tool for that cost. The command stands beside the
rule that says when the reviewer runs it. Its weak point: a product's guidelines hold a second
command, and only the area this decision names keeps other tools from claiming the same exception.
*Rejected:* a mode of mutation in the gate — code in each product's gate to spare an extra
assertion; the run in CI — a run that admits nothing has no place where changes are admitted;
commands of the test tool for each level, which WAY-241 rejects, stay rejected, since they run the
product's tests beside the gate.

## The-way's own coding and testing guidelines

What the-way adopts of the templates of the coding and the testing discipline for its own code and
tests, where it departs from them, the kinds of its code and the levels of its tests, and the
exemplar of each.

### WAY-379 — Does the-way adopt the template of the coding discipline for its own code?

The-way adopts the template of the coding discipline for the code of each part named in *Scope*: its
coding guidelines stand in the file `guidelines/coding.md`, with a file `guidelines/coding-<kind>.md`
for each kind of code that has an exemplar, and the rules of the template bind its code through the
decisions of this log that adopt them or depart from them. The-way departs from the template only by
a decision of this log that gives the reason. The *Scope* names every part of the-way's part map that
holds Python code, and a change that gives a part Python code, or adds a part that holds it, adds that
part to this decision's *Scope*.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-202
- **Verification:** an agent compares the guidelines and a change with the decision:
  - complies: the rule of the linter in `guidelines/coding.md` names the decision that adopts the
    linter, the rule of the formatter reads `none —` with the decision that departs from it, and a
    change that gives a part its first Python file adds that part to this *Scope* in the same change;
  - violates: a rule of the-way's coding guidelines that executes a choice with a real cost names no
    decision of this log; the template of the coding discipline is edited to fit a departure of the-way
    (WAY-173); a part that holds Python code stands outside this *Scope*.
- **Origin:** none

*Rationale:* a rule of a template of the-way binds a product only through a decision of the product's
log that adopts it (WAY-173), and the-way, which treats itself as a product everywhere else, binds its
own code the same way. Without the decision each rule of its coding guidelines would cite nothing and
bind nothing, new code would copy the code already there, and a reviewer would have no threshold by
which to grade a finding of structure (WAY-363). The standing checks and the rule of size come with the
template, each adopted or departed from by a decision of its own, so that a departure has its reason on
record (WAY-202, WAY-360). Naming in *Scope* every part that holds Python code, and adding a part to it
when a part gains such code, keeps a new part from standing outside the guidelines unseen.
*Rejected:* no decision adopting the template — the rules of the coding guidelines would have no
decision to cite and would bind nothing (WAY-173).

### WAY-380 — Which linter checks the-way's code, and which of its rules block a change?

Ruff 0.17.1 checks the code of the parts that WAY-379 names, tests included, with the default set of
that version, which the environment fact `ruff-default-rules` gives, with no preview rules and for the
target version `py314`. The rules that block a change are the default set less the 18 rules `UP031`,
`ISC004`, `PLW1510`, `RUF100`, `FURB167`, `FLY002`, `I001`, `B023`, `UP017`, `SIM117`, `UP012`,
`RUF015`, `SIM102`, `C419`, `RUF012`, `SIM114`, `SIM905` and `SIM115`, which stand among the examples
of the coding guidelines. A comment in the code that turns a rule off has no effect, a fault of one
file is fixed in that file, and turning a rule off for the whole of the-way, or moving a rule between
the blocking rules and the examples, is a change of this decision.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines, repository
- **Based on:** ruff-default-rules
- **Relations:** derives from WAY-379 · derives from WAY-203 · derives from WAY-204
- **Verification:** invariants: ruff-blocking-rules. For what the invariant leaves, an agent compares
  a change with the decision:
  - complies: a report of `F841` in one file is fixed in that file and the configuration of Ruff stays
    as it is; a rule on which a later report leads to no change worth making moves among the examples
    by a change of this decision that the human approves;
  - violates: a task turns a blocking rule off in the configuration of Ruff on meeting a report, with
    no change of this decision; a rule of the examples blocks a change.
- **Origin:** none

*Rationale:* a rule blocks a change only where every report it gives leads to a change of code worth
making, and which rules do so shows only on the code itself (WAY-203, WAY-204). A trial run of the
default set on the-way's code, made by its own author and agents at the commit of the review of the
foundation, with Ruff 0.17.1, no preview rules and Python 3.14, gave 649 reports from 26 rules in 55
files; an agent that wrote none of that code judged each report by whether it led to a change worth
making. The 18 rules above gave at least one report that did not, and the other rules that reported,
among them `RUF059` and `UP022`, gave only reports that did. That run is the product's own measurement,
and its record is not open to a reader of the repository. A comment that turns a rule off has no effect
because a rule that blocks gives no report that leads to no change, so no such comment is sound
(WAY-203). The target version follows the version of Python the repository declares. The price: a
rule that gave good reports in the trial run can give a bad one later, which only a change of this
decision moves among the examples, and the 18 rules reach an agent only as examples to read.
*Rejected:* the split that another product of the same owner keeps, taken as it stands — it would block
nine rules whose reports led here to no change worth making, among them `B023`, `FLY002` and `UP017`,
and let `RUF059` pass, whose reports were worth a change; a departure from a linter with a reason —
it costs nothing today, but nothing then stops the return of the faults the trial run found or of new
ones.

### WAY-381 — How is the version of the linter pinned and installed?

The version of Ruff is pinned by `required-version = "==0.17.1"` in `ruff.toml`, which makes Ruff
refuse to run in any other version, and by the files of requirements for the tools of quality:
`requirements-quality.in`, which holds `ruff==0.17.1` and allows wheels only, and
`requirements-quality.txt`, which holds the SHA-256 sum of every wheel of that release and no source
distribution. Ruff stands in the environment `.runs/quality-venv`, which the section "Running the
tests" of `README.md` tells how to install from the requirements file, and each job of CI gains one
step that installs it there, while the one command that runs the checks stays
`python -B gate/run_tests.py` (WAY-16).

- **Scope:** repository, agent-instructions
- **Based on:** ruff-required-version
- **Relations:** derives from WAY-380 · derives from WAY-16
- **Verification:** an agent compares the change with the decision:
  - complies: the configuration of Ruff holds `required-version`, the requirements file holds a sum
    for every wheel and no source distribution, the README tells how to create `.runs/quality-venv` and
    install from the file, and each job of CI differs from before by one step that installs the
    requirements;
  - violates: the version stands in one place only; the requirements file holds a source
    distribution or a wheel with no sum; CI runs a command of Ruff beside the one command that runs the
    checks.
- **Origin:** none

*Rationale:* a linter in another version checks another set of rules, so its version has to be the same
on every machine that runs the gate. Ruff refuses to run in a version that `required-version` does
not allow, so a version that does not match shows at once and the check needs no code of its own to
find it, while the sums of the wheels let an installation be verified and are meant to let the
repository's host read the dependency. The linter is the first dependency of the-way beyond Python
itself: it has to be installed wherever the gate runs, and without it the gate is red.
*Rejected:* the version lock of the linter's configuration alone — one file fewer, but no checksums
and nothing for the alerts of the repository's host to read.

### WAY-382 — Does the-way's code get an automatic formatter?

The-way's code has no automatic formatter, so `### Formatter` of its coding guidelines reads
`none — WAY-382`. A formatter enters the-way only by a decision of this log that adopts it and by one
reformatting of the whole of its code in the task that brings it (WAY-205).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: `### Formatter` of `guidelines/coding.md` reads `none — WAY-382`, no configuration of a
    formatter stands in the repository and CI runs none;
  - violates: a task configures a formatter or reformats files of the code with no decision that
    adopts one; `### Formatter` names an invariant.
- **Origin:** none

*Rationale:* reformatting the whole of the code would move every line to which the documents of the
tasks waiting in the backlog point by its place in a file, and so give a conflict to every branch open
at the merge, while `git blame` would then name the one commit of the reformatting for each line. The
formatter is a choice that the-way and the other product of its owner can make together, in a decision
of its own, and the way back is that decision and the one reformatting that WAY-205 gives, with no
task opened for it now.
*Rejected:* a formatter with one reformatting of the whole of the code in the task that writes these
guidelines — a single commit across the code, `git blame` pointing at it and a conflict in every
branch open at the merge, for the gain of ending disputes over layout.

### WAY-383 — Does the-way's code get an audit of its dependencies?

The-way departs from the audit of dependencies, so `### Dependency audit` of its coding guidelines
reads `none — WAY-383`: its code imports nothing from outside the standard library of Python, and the
one dependency it declares is the linter, in the version WAY-381 pins. A change that brings a
dependency of its code other than the linter ends this departure and is a change of this decision.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: `### Dependency audit` reads `none — WAY-383`, and a change that adds a library to a
    script comes with a change of this decision;
  - violates: a script imports a library with no change of this decision; the reason of this decision
    still says that the-way has no dependency at all.
- **Origin:** none

*Rationale:* an audit of dependencies checks the versions of what a product depends on, and a product
that depends on nothing but the tool that checks its code has no version to check beyond the one
decision pins. The reason is worded to include that tool, since the declaration of the linter is a
dependency, and a reason that said the-way has none would stop being true at the merge.
*Rejected:* the reason as first worded, that the-way has no libraries outside its own code — it stops
being true once the linter is declared.

### WAY-384 — Does the-way adopt the six rules of the coding template on failures and logs?

The-way's scripts write no logs: they print their result to the console and report a failure by an
exit code and a line `Error:`. The-way departs from all six rules on failures and logs, so each of the
headings `### Recording a failure`, `### Hiding a failure`, `### Identifiers in log lines`,
`### Business events`, `### Secrets and personal data` and `### Logging scope` of its coding
guidelines holds only `none — WAY-384`.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: the six headings of `guidelines/coding.md` read `none — WAY-384` and nothing else, and a
    script reports a failure by an exit code and a line `Error:`;
  - violates: a heading of the six holds a rule or a list of identifiers; a script writes a log file
    and no decision adopts the rule for it.
- **Origin:** none

*Rationale:* the six rules say how code writes to a product's logs and what a product promises to log,
so a product whose programs write none has nothing for them to bind; the way of the template that
departs from all six keeps the headings and holds no principle, boundary or form of a line. How a
script ends in an error, and what it does with a missing field of a file it reads, stands in WAY-344.
Its weak point: that a failure is not turned into an answer that all went well stands in no rule of the
guidelines, and WAY-344 for a missing field and the review of each change answer for it.
*Rejected:* adopting `### Hiding a failure` in the wording of the template and departing from the other
five — that rule speaks of a line in the logs, which the-way has none of.

### WAY-385 — How large may a function and a file of a script of the-way be?

A function of a script of the-way has at most 80 lines, counted with the functions nested in it, and a
file of a script has at most 1000 lines, in each part that WAY-379 names; a test file stands outside
the rule, and no function and no file is kept whole over a threshold as an exception. A test of the
suite counts the lines with the `ast` module of the standard library, runs apart from the run of the
linter and, where it fails, names every function and file over a threshold with its size (WAY-361).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-360 · derives from WAY-361
- **Verification:** invariants: function-and-file-size. tests: that a function is counted with the
  functions nested in it and that a method is a function. For what the invariant and the test leave,
  an agent compares a change with the decision:
  - complies: a test file of two thousand lines stays outside the rule; a change that adds a branch to
    a function over its threshold begins with a move of a part of it out (WAY-365); a function that
    cannot be divided is divided or the threshold is changed in this decision, never kept as an
    exception;
  - violates: the configuration of the test lists a function or a file as an exception; the rule
    covers test files.
- **Origin:** none

*Rationale:* the thresholds come from a trial run of sizes on the-way's own code, since only that shows
what a threshold stops and what already stands over it (WAY-360); the run counted, at the commit of
the review of the foundation, how many functions and files of scripts stand over each pair of
thresholds, and 80 and 1000 leave 11 functions and 2 files over. That run is the product's own
measurement, and its record is not open to a reader of the repository. Tests stand outside the rule
because their rules stand in the testing guidelines (WAY-231). No exception stands: the invariant
of the rule is marked violated until the functions and files over a threshold are divided (WAY-51),
and until then only review keeps a cleaned or a new file from growing over it. The price: tasks that
change the largest scripts begin with a move of a part out (WAY-365), one move does not bring the
largest script under its threshold, a count of lines says nothing of whether a function is well made,
and a function can be divided only to stand under a threshold.
*Rejected:* 60 lines and 800 lines — 19 functions and 4 files over in the same run; 100 lines and 1500
lines — 7 functions and 1 file over; a departure from the rule — every remark of a reviewer on the
structure of code stays Minor (WAY-363); the rule covering test files, with a rule of the testing
guidelines — 5 test files over 1000 lines in the same run and more invariants marked violated;
exceptions pointed out one by one by the human, with a reason each.

### WAY-386 — Which file is the exemplar of the kind `check` in the-way's code?

`task-cycle/tracked_private_paths_check.py` is the exemplar of the kind `check` of the-way's code. The
coding guidelines of the kind hold no rule that a test checks, so the exemplar stands there as an
example and binds no later code.

- **Scope:** task-cycle, project-level, elements-common, instruction-files
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** an agent compares the change with the decision:
  - complies: `guidelines/coding-check.md` lists the file as `exemplar` beside this decision;
  - violates: another file takes the status `exemplar` with no change of this decision; a rule that
    no test checks is drawn from the exemplar and names an invariant.
- **Origin:** none

*Rationale:* an exemplar that a decision designates is a model the human approved, where a file
copied because an agent found it first turns whichever file that is into law (WAY-198); the kind has
no rule that a cheap test checks, so the exemplar stands as an example.
*Rejected:* another script of the kind as the exemplar — it shows the reading of arguments better and
does not show the check of a missing field.

### WAY-387 — Which file is the exemplar of the kind `measuring-report` in the-way's code?

`task-cycle/cycle_measures.py` is the exemplar of the kind `measuring-report` of the-way's code. The
coding guidelines of the kind hold no rule that a test checks, so the exemplar stands there as an
example and binds no later code.

- **Scope:** task-cycle, process-audit, project-level
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** an agent compares the change with the decision:
  - complies: `guidelines/coding-measuring-report.md` lists the file as `exemplar` beside this
    decision, and the file breaks no rule of the linter that blocks;
  - violates: another file takes the status `exemplar` with no change of this decision; the exemplar
    keeps a report of a blocking rule that the new files of the kind would copy.
- **Origin:** none

*Rationale:* the exemplar is what every later file of its kind follows, so a fault that the linter
reports in it is corrected before it is designated; otherwise each new file of the kind would take
the fault over (WAY-198).
*Rejected:* marking the invariant of the linter violated with no correction in the exemplar — the
exemplar of the kind would keep two faults that every new file of the kind copies.

### WAY-388 — Which file is the exemplar of the kind `generator` in the-way's code?

`agent-instructions/skill_entry_points.py` is the exemplar of the kind `generator` of the-way's code,
and a script of the kind changes no file of the repository it runs in without `--write`.

- **Scope:** agent-instructions
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** invariants: generator-writes-only-with-write. For the designation, an agent
  compares the change with the decision:
  - complies: `guidelines/coding-generator.md` lists the file as `exemplar` beside this decision, and
    the file ends with exit code 2 where a field it reads is missing, as WAY-344 gives;
  - violates: another file takes the status `exemplar` with no change of this decision.
- **Origin:** none

*Rationale:* the exemplar of a kind is designated by a decision so that it is a model the human
approved, and what a script can check of it stands in the guidelines of the kind as a rule that names
an invariant (WAY-198); for a generator that is the rule that without `--write` no file changes. The
exemplar is designated once its ending at a missing field of a file it reads is corrected to the exit
code 2 that WAY-344 gives, so that no later generator copies the fault.
*Rejected:* unknown.

### WAY-389 — Which file is the exemplar of the kind `repository-changer` in the-way's code?

`task-cycle/remove_merged_worktrees.py` is the exemplar of the kind `repository-changer` of the-way's
code, and a script of the kind changes neither a file that the repository tracks, other than a report
that the human names with `--report`, nor a working directory without `--apply`, or where the
confirmation is declined.

- **Scope:** task-cycle, elements-common, installation
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** invariants: repository-changer-acts-only-when-told. For the designation, an agent
  compares the change with the decision:
  - complies: `guidelines/coding-repository-changer.md` lists the file as `exemplar` beside this
    decision;
  - violates: another file takes the status `exemplar` with no change of this decision.
- **Origin:** none

*Rationale:* the exemplar of a kind is designated by a decision so that it is a model the human
approved, and what a script can check of it stands in the guidelines of the kind as a rule that names
an invariant (WAY-198); for a repository changer that is the rule that without `--apply`, or where the
confirmation is declined, nothing changes.
*Rejected:* unknown.

### WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?

`task-cycle/gate_times.py` is the exemplar of the kind `command-runner` of the-way's code, and a
script of the kind that wraps one command ends with that command's exit code unchanged.

- **Scope:** task-cycle, gate
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** invariants: command-runner-passes-exit-code. For the designation, an agent
  compares the change with the decision:
  - complies: `guidelines/coding-command-runner.md` lists the file as `exemplar` beside this decision;
  - violates: another file takes the status `exemplar` with no change of this decision.
- **Origin:** none

*Rationale:* the exemplar of a kind is designated by a decision so that it is a model the human
approved, and what a script can check of it stands in the guidelines of the kind as a rule that names
an invariant (WAY-198); for a command runner that is the rule that the exit code of the wrapped
command is passed on unchanged.
*Rejected:* unknown.

### WAY-391 — Which file is the exemplar of the kind `shared-module` in the-way's code?

`relation-model/fingerprint.py` is the exemplar of the kind `shared-module` of the-way's code, and
importing a file of the kind runs nothing.

- **Scope:** relation-model
- **Based on:** none
- **Relations:** derives from WAY-379 · derives from WAY-198
- **Verification:** invariants: shared-module-import-runs-nothing. For the designation, an agent
  compares the change with the decision:
  - complies: `guidelines/coding-shared-module.md` lists the file as `exemplar` beside this decision;
  - violates: another file takes the status `exemplar` with no change of this decision.
- **Origin:** none

*Rationale:* the exemplar of a kind is designated by a decision so that it is a model the human
approved, and what a script can check of it stands in the guidelines of the kind as a rule that names
an invariant (WAY-198); for a shared module that is the rule that importing it runs nothing.
*Rejected:* unknown.

### WAY-392 — Does the-way adopt the template of the testing discipline for its own tests?

The-way adopts the template of the testing discipline for the tests of each part named in *Scope*: its
testing guidelines stand in the file `guidelines/testing.md`, and the rules of the template bind its
tests through the decisions of this log that adopt them or depart from them. The-way departs from the
template only by a decision of this log that gives the reason, as it does from the field *Time limit*
of a recipe and from the rule of mutation testing, and the rule `### AI in tests` enters with no
decision on a tool, since no test of the-way uses an AI tool. The *Scope* names every part of the-way's
part map that holds a test, and a change that gives a part a test adds that part to this decision's
*Scope*.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-231
- **Verification:** an agent compares the guidelines and a change with the decision:
  - complies: each rule of `guidelines/testing.md` that executes a choice with a real cost names a
    decision of this log, `### Mutation testing` reads `none —` with the decision that departs from
    it, and a change that gives a part its first test adds that part to this *Scope*;
  - violates: a rule of the testing guidelines names no decision; `### AI in tests` names a tool that
    no decision of this log adopts; a part that holds a test stands outside this *Scope*.
- **Origin:** none

*Rationale:* the rules of the template of the testing discipline bind a product only through a decision
of its log (WAY-173), and the-way binds its own tests the same way, so that each rule of its testing
guidelines cites a decision and a departure has its reason on record. Naming the parts in *Scope* keeps
a new part with tests from standing outside the guidelines unseen.
*Rejected:* no decision adopting the template — the rules of the testing guidelines would have no
decision to cite and would bind nothing (WAY-173).

### WAY-393 — At which levels do the tests of the-way stand?

The tests of the-way stand at five levels: unit, files test, git test, repository test and e2e. The
files test, the git test and the repository test are terms of the glossary, which gives each by the
resources a test of that level may touch, and an e2e test runs a whole path of a session through
several scripts.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines, glossary
- **Based on:** none
- **Relations:** derives from WAY-392 · derives from WAY-240
- **Verification:** an agent compares the guidelines with the decision:
  - complies: the table of levels of `guidelines/testing.md` names the five levels, names the three
    glossary terms and copies none of their definitions, and a test of the level files test starts no
    git;
  - violates: a sixth level appears in the table with no change of this decision; the table of levels
    defines a files test in its own words; a test named a files test starts git.
- **Origin:** none

*Rationale:* a level defined by what its test may touch can be checked without judgement, while the
usual names of levels mean different things to different readers (WAY-240); three of the five levels
mean in the-way something narrower or other than in the field, so each is a term of the glossary of
the-way, which every product that pins the-way receives too. Keeping the files test and the git test
apart keeps the distinction whether a test needs git.
*Rejected:* four levels, unit, integration with files and git together, e2e and a test of the
repository — two glossary terms instead of three, and the distinction whether a test needs git
disappears.

### WAY-394 — Where does a test of the-way take its expected value from?

A test of the-way takes the value it expects from the entries of the-way's foundation, from its
glossary, from the templates and skills that the script under test carries out, or from the
description at the head of the script, which gives its exit codes and the form of its result, and
from no other document (WAY-232).

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-392 · derives from WAY-232
- **Verification:** an agent compares the tests with the decision:
  - complies: a test of an exit code names the description at the head of its script in a comment at
    the value; a test of the form of a file that a skill writes takes the form from that skill;
  - violates: a test takes its expected value from a constant or a function of the code it checks; a
    test takes it from a document outside the-way's foundation, its templates, its skills and the
    description of its scripts.
- **Origin:** none

*Rationale:* the expected value of a test comes from a document of the product that its testing
guidelines name (WAY-232); the foundation, the glossary, and the templates and skills that a script
carries out are such documents, and the description at the head of a script gives its exit codes and
the form of its result, which for most scripts stand in no other document. Its weak point: the author changes the code and its description in one
commit, and the test follows both, so the review asks of each assertion where its value comes from.
*Rejected:* the sources without the description at the head of a script — the exit codes of most
scripts stand in no other document.

### WAY-395 — Which fields of a recipe of a level of the-way's tests bind?

In the recipe of each level of the-way's tests the fields *Purpose*, *Files*, *Doubles*, *Data*, *Time
and randomness*, *Exemplar* and *Command* bind and name this decision, and *Shape* stands as an
example. *Purpose* says what the level is for and when not to use it; *Files* has the tests as files
`test_*.py` in the directory of the part, beside the script they test, under `unittest`; *Doubles*
allows a double only of the clock and of what a test cannot do on a git repository it builds in a
temporary directory, git and the file system being real and standing in a temporary directory, and at
the level of a repository test the checkout being real; *Data* has the values of a test written out in
it, each with its source in a comment; *Time and randomness* has the test give the script its time, by
replacing the clock function of the script in the process of the test or by giving a fixed time to
a script that takes one, and no fixed pause; *Command* is `python -B gate/run_tests.py
<directory>`, which the gate narrows to a directory and no further. The field
*Time limit* reads `none — WAY-395`, since the-way has no file that holds a limit and each limit
stands at the call that needs it.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-392 · derives from WAY-241
- **Verification:** an agent compares the guidelines and the tests with the decision:
  - complies: the recipe of the level git test names this decision at *Doubles*, builds the
    repository in a temporary directory and replaces nothing but the clock; a test replaces the clock
    function of the script, or gives a fixed time to a script that takes one, and does not read the
    real clock; *Time limit* reads `none — WAY-395`;
  - violates: a test replaces git with a double where a repository in a temporary directory is
    cheap; a test waits a fixed time for another process; a recipe lists a command of the test tool
    beside the gate; a recipe holds a value of a time limit.
- **Origin:** none

*Rationale:* a recipe of the same fields for every level lets an agent find what binds at any level in
one place, and a field binds only where a decision of the product carries it (WAY-241, WAY-173); the
fields above bind as rules what the-way's tests do today, and the one command that runs every test
(WAY-16) is the one the recipe gives. The field *Time limit* points to the configuration file that
holds a limit, and the-way has no such file, since each limit stands at the call that needs it.
*Rejected:* unknown.

### WAY-396 — Which test is the exemplar of the level unit of the-way's tests?

`relation-model/test_fingerprint.py::Fingerprint.test_a_tab_is_kept` is the exemplar test of the level
unit of the-way's tests.

- **Scope:** relation-model
- **Based on:** none
- **Relations:** derives from WAY-393 · derives from WAY-242
- **Verification:** an agent compares the change with the decision:
  - complies: the field *Exemplar* of the recipe of the level unit names this test beside this
    decision;
  - violates: the field names another test with no change of this decision; the field stands with a
    placeholder.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of every
later one, while a test that a decision designates is one the human approved (WAY-242).
*Rejected:* unknown.

### WAY-397 — Which test is the exemplar of the level files test of the-way's tests?

`task-cycle/test_cycle_measures.py::RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted` is
the exemplar test of the level files test of the-way's tests.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-393 · derives from WAY-242
- **Verification:** an agent compares the change with the decision:
  - complies: the field *Exemplar* of the recipe of the level files test names this test beside this
    decision;
  - violates: the field names another test with no change of this decision; the field stands with a
    placeholder.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of every
later one, while a test that a decision designates is one the human approved (WAY-242).
*Rejected:* unknown.

### WAY-398 — Which test is the exemplar of the level git test of the-way's tests?

`project-level/test_plan_state_invariant.py::PlanStateEvidence.test_fresh_remote_record_composes_both_transitions`
is the exemplar test of the level git test of the-way's tests.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-393 · derives from WAY-242
- **Verification:** an agent compares the change with the decision:
  - complies: the field *Exemplar* of the recipe of the level git test names this test beside this
    decision;
  - violates: the field names another test with no change of this decision; the field stands with a
    placeholder.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of every
later one, while a test that a decision designates is one the human approved (WAY-242).
*Rejected:* unknown.

### WAY-399 — Which test is the exemplar of the level repository test of the-way's tests?

`elements/common/test_elements_pending_marker.py::TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker`
is the exemplar test of the level repository test of the-way's tests.

- **Scope:** elements-common
- **Based on:** none
- **Relations:** derives from WAY-393 · derives from WAY-242
- **Verification:** an agent compares the change with the decision:
  - complies: the field *Exemplar* of the recipe of the level repository test names this test beside
    this decision;
  - violates: the field names another test with no change of this decision; the field stands with a
    placeholder.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of every
later one, while a test that a decision designates is one the human approved (WAY-242).
*Rejected:* unknown.

### WAY-400 — Which test is the exemplar of the level e2e of the-way's tests?

`process-audit/test_audit_count.py::Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is
the exemplar test of the level e2e of the-way's tests.

- **Scope:** process-audit
- **Based on:** none
- **Relations:** derives from WAY-393 · derives from WAY-242
- **Verification:** an agent compares the change with the decision:
  - complies: the field *Exemplar* of the recipe of the level e2e names this test beside this
    decision, and the file that holds it runs git with the configuration of the user and of the system
    shut out;
  - violates: the field names another test with no change of this decision; the file that holds the
    exemplar runs git under the user's global configuration.
- **Origin:** none

*Rationale:* a test copied from whichever test an agent finds turns an accident into the model of every
later one, while a test that a decision designates is one the human approved (WAY-242). The exemplar
is the model of every later test of its level, so the fault of the file that holds it, git run under
the user's own configuration, is corrected before the test is designated, and no copy takes it over.
*Rejected:* agreeing that the copies of the exemplar take over the fault of running git under the
user's global configuration.

### WAY-401 — What does the-way deliberately not test?

The-way does not test automatically what an agent does when it follows a skill: its tests check the
form of the texts of the skills and their consistency, and the behaviour of the agents is checked by
the human's review of a cycle at the merge and by the audit of the process, never by the gate. The
category is tested again when an error of an agent's behaviour repeats that the audit does not catch
before the merge.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-392 · derives from WAY-237
- **Verification:** an agent compares the guidelines and the tests with the decision:
  - complies: `## Not tested on purpose` of `guidelines/testing.md` names the category and this
    decision; a test of a skill checks that the files it names exist and that its text agrees with the
    template it applies;
  - violates: the gate starts a model to check what an agent does; the section lists a single test or
    file; the section names no decision.
- **Origin:** none

*Rationale:* a test of what an agent does would start a model in every run of the gate, at a cost in
tokens, and its result would not be the same on the same code; the review of a cycle by the human at
the merge and the audit of the process look at the behaviour instead. The price: an error of an agent's
behaviour that neither of them sees passes the gate.
*Rejected:* unknown.

### WAY-402 — Does the-way adopt a mutation tool?

The-way adopts no mutation tool and departs from the rule of mutation testing of the template of the
testing discipline, so `### Mutation testing` of its testing guidelines reads `none — WAY-402` and the
author of a change checks its tests in every part by mutating the code in their head (WAY-253). A
mutation tool enters the-way, for the parts whose complexity lies in computation, when an error
passes after a merge in such a part for want of an assertion.

- **Scope:** elements-common, part-map, relation-model, project-level, task-cycle, gate,
  agent-instructions, instruction-files, installation, process-audit, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-392 · derives from WAY-252
- **Verification:** an agent compares the change with the decision:
  - complies: `### Mutation testing` reads `none — WAY-402`; the author of a change to a calculation
    names a mutation of the code that no test catches and adds the assertion;
  - violates: a task adds a mutation tool to the repository with no change of this decision; the
    rule is left out with no decision.
- **Origin:** none

*Rationale:* a check in the head costs no dependency, and a tool would be one more dependency run at
every change. The return of a tool is tied to the case it is for: a part whose complexity lies in
computation, where a missing assertion lets an error through (WAY-252).
*Rejected:* a mutation tool for the parts whose complexity lies in computation — a separate choice of
technology, with the cost of its configuration.

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| WAY-06 | its rule, that a foundation change reaches the main branch with its code, stands in WAY-01 | WAY-01 |
| WAY-15 | its rule, what is derived and what is written by hand, stands in WAY-225 | WAY-225 |
| WAY-20 | withdrawn: it said only that a change names no kind of change; what a change does to an entry's meaning reaches the human as WAY-114 gives it | WAY-114 |
| WAY-23 | its rule, that a product keeps all its decisions in one log, stands in WAY-18 | WAY-18 |
| WAY-31 | withdrawn: a reference names an entry by its identifier alone, with no fingerprint (WAY-02), and the author's search finds what names a changed entry (WAY-33) | WAY-02 |
| WAY-32 | its rule, the answer to "What types of relation can a decision name?", stands in `elements/decisions/template.md` | none |
| WAY-37 | its rule, the answer to "What happens to entries that wait for something when it arrives?", stands in `elements/common/way_of_working.md` | none |
| WAY-39 | its rule, how a fingerprint is computed, stands in WAY-02 | WAY-02 |
| WAY-40 | its rule, the answer to "What kinds of entry does the part map hold?", stands in `elements/part-map/template.md` | none |
| WAY-41 | its rule, the answer to "What identifies an entry of the part map?", stands in `elements/common/rules.md` | none |
| WAY-42 | its rule, the answer to "What is the binding part of a part map entry?", stands in `elements/part-map/template.md` | none |
| WAY-43 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-45 | its rule, the answer to "How is a critical flow recorded and tested?", stands in `elements/part-map/template.md` | none |
| WAY-46 | withdrawn: it said only that a part carries no failure modes and no criticality; the part map gives a part no such field | WAY-40 |
| WAY-47 | withdrawn: it said only that no list of a critical flow's parts is checked; a critical flow has no entry in the part map (WAY-45) | WAY-45 |
| WAY-49 | its rule, the answer to "How does the part map record a surface, and how is a change to it made known?", stands in `elements/part-map/template.md` | none |
| WAY-50 | the part map keeps no levels of promise or policies of change; how a change to a surface is made known stands in WAY-49 | WAY-49 |
| WAY-56 | its rule, the answer to "How much does one invariant entry hold, and what is its binding part?", stands in `elements/invariants/template.md` | none |
| WAY-57 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-58 | its rule, the answer to "What does an invariant entry record in *Derives from* when no decision entry of the product's log carries it?", stands in `elements/invariants/template.md` | none |
| WAY-59 | the binding part of an invariant entry is given by WAY-56, which answers how much one invariant entry holds | WAY-56 |
| WAY-64 | its rule, the answer to "Where do invariant and environment fact entries stand, and what identifies one?", stands in `elements/common/rules.md` | none |
| WAY-65 | its rule, the answer to "How does a check cite its invariant, and which files are invariant tests?", stands in `elements/invariants/template.md` | none |
| WAY-66 | an invariant's links name an entry by its identifier alone, with no fingerprint (WAY-02) | WAY-02 |
| WAY-67 | a violated invariant is marked at its entry, with no list of violated invariants beside it (WAY-51) | WAY-51 |
| WAY-68 | its rule, the answer to "What happens to a check that gives different verdicts on one commit?", stands in `elements/invariants/template.md` | none |
| WAY-70 | its rule on values written out left the invariants; for a product's tests it stands in WAY-228 | WAY-228 |
| WAY-72 | its rule, the answer to "In what language is a product's foundation written?", stands in `elements/common/rules.md` | none |
| WAY-74 | withdrawn: it said only that the-way keeps no record of a run; the exit code of the command running the tests says whether a test failed (WAY-63) | WAY-63 |
| WAY-75 | its rule, where environment fact entries stand and what identifies one, stands in WAY-64 | WAY-64 |
| WAY-76 | its rule, the answer to "How much does one environment fact entry hold?", stands in `elements/environment-facts/template.md` | none |
| WAY-77 | its rule, the answer to "What shows what an environment fact is true of?", stands in `elements/environment-facts/template.md` | none |
| WAY-78 | its rule, the answer to "What is the binding part of an environment fact entry?", stands in `elements/environment-facts/template.md` | none |
| WAY-79 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-80 | its rule, the answer to "What is an environment fact's source?", stands in `elements/environment-facts/template.md` | none |
| WAY-81 | withdrawn: it said only that an environment fact names no method; how a fact keeps up with its source stands in WAY-82 | WAY-82 |
| WAY-83 | withdrawn: the foundation records no human verdict | none |
| WAY-86 | its rule, the answer to "How does a catalogue of requirements or a binding rule reach a product?", stands in `elements/environment-facts/template.md` | none |
| WAY-87 | the part map records no criticality; how an obligation from a law or a contract reaches a product stands in WAY-86 | WAY-86 |
| WAY-88 | its rule, that a fact stands only while an entry names it, stands in WAY-73 | WAY-73 |
| WAY-91 | a fact has no probe, so no release of a probe's tool counts | none |
| WAY-92 | its rule, which glossary holds a word of the process and which a word of a product's domain, stands in WAY-226 | WAY-226 |
| WAY-96 | its rule, the answer to "How is a glossary definition written?", stands in `elements/glossary/template.md` | none |
| WAY-98 | withdrawn: it said only that a glossary entry holds no *Avoid*; WAY-94 gives an entry its one field | WAY-94 |
| WAY-105 | withdrawn: when an invariant's method reads `test` and when `review` stands in WAY-61, which answers how an invariant's method of checking is written | WAY-61 |
| WAY-108 | its rule, the answer to "What form does a project definition take?", stands in `project-level/definition_template.md` | none |
| WAY-109 | its rule, the answer to "What may a project definition treat as settled without the human's answer?", stands in `project-level/definition_template.md` | none |
| WAY-110 | its rule, the answer to "When does a deadline enter a project definition?", stands in `project-level/definition_template.md` | none |
| WAY-111 | its rule, the answer to "What does the project level read in the current foundation?", stands in `project-level/skill/read_foundation.md` | none |
| WAY-112 | its rule, the answer to "How does an agent develop and resume a project definition?", stands in `project-level/skill/idea.md` | none |
| WAY-115 | its rule, the answer to "How are foundation entries found in a project's source?", stands in `elements/common/skill/build_table.md`, `elements/common/skill/definition_variant.md` and `elements/common/skill/task_variant.md` | none |
| WAY-116 | its rule, the answer to "Which foundation entries may a project definition project?", stands in `project-level/definition_template.md` | none |
| WAY-117 | its rule, the answer to "How does a foundation entry stand in a project definition before it is written?", stands in `elements/common/projected_mode.md` | none |
| WAY-119 | withdrawn: no decision carries *Review when* | none |
| WAY-149 | withdrawn: it said only that a return-step test takes no deliberate break; every invariant test is seen failing once (WAY-08) | WAY-08 |
| WAY-151 | its rule, the answer to "How much of large project definitions and existing plans does plan-project read?", stands in `project-level/plan/skill/reading_definition_and_plan.md` | none |
| WAY-152 | its rule, the answer to "What does leading a project plan leave to others?", stands in `project-level/lead/skill/SKILL.md` | none |
| WAY-156 | its rule, the answer to "How does project leading route a plan or definition change?", stands in `project-level/lead/skill/route_changes.md` and `project-level/lead/skill/definition_change.md` | none |
| WAY-157 | withdrawn: how the orchestrator waits for an agent is a step of the task-cycle skill and binds no other work | none |
| WAY-158 | its rule, the answer to "Who reads the full diff of a task-cycle change or slice?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-159 | its rule, the answer to "When does the task-cycle orchestrator rely on focused-check evidence?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-163 | its rule, the answer to "What does the cycle run before it opens a request its code review blocked?", stands in `task-cycle/skill/blocked_finding.md` | none |
| WAY-169 | its rule, the answer to "What happens to a reference of guidelines when the entry it names changes?", stands in `product-guidelines/template.md` | none |
| WAY-170 | its rule, the answer to "What checks the form of a product's guidelines?", stands in `product-guidelines/template.md` | none |
| WAY-171 | its rule, the answer to "What form does a file of a product's guidelines take?", stands in `product-guidelines/template.md` | none |
| WAY-175 | withdrawn: what the styleguide's template and skill take from outside is no question a decision answers; the sources are private, so each piece binds through the decision that carries it, on that decision's own rationale (WAY-100, WAY-27) | WAY-100 |
| WAY-176 | its rule, the answer to "How does a styleguide name its colour roles and pair them?", stands in `product-guidelines/styleguide/template.md` | none |
| WAY-177 | its rule, the answer to "What does a styleguide say of shared controls?", stands in `product-guidelines/styleguide/template.md` | none |
| WAY-178 | its rule, the answer to "Where is a fault of one screen fixed?", stands in `product-guidelines/styleguide/template.md` | none |
| WAY-179 | withdrawn: an example of a template needs no decision (WAY-168) | none |
| WAY-180 | its rule, the answer to "Does a styleguide require a page showing the product's components in every state, and where is it served?", stands in `product-guidelines/styleguide/template.md` | none |
| WAY-181 | withdrawn: the order of a plan is an example the styleguide carries, and WAY-213 says who reads it and how | WAY-213 |
| WAY-182 | its rule, the answer to "Where does a value of design tokens say it comes from, and who picks the source?", stands in `product-guidelines/styleguide/template.md` | none |
| WAY-183 | its rule, the answer to "Which user interfaces of a product get a styleguide?", stands in `product-guidelines/styleguide/recognize.md` | none |
| WAY-184 | its rule, the answer to "When does a product's styleguide come into being?", stands in `product-guidelines/styleguide/SKILL.md` and `product-guidelines/styleguide/starting_rules.md` | none |
| WAY-185 | its rule, the answer to "What does the styleguide skill look at first?", stands in `product-guidelines/styleguide/recognize.md` | none |
| WAY-186 | its rule, the answer to "Where do a styleguide's starting rules come from?", stands in `product-guidelines/styleguide/starting_rules.md` | none |
| WAY-187 | its rule, the answer to "How does the styleguide skill audit a product that has screens?", stands in `product-guidelines/styleguide/audit.md` | none |
| WAY-188 | withdrawn: what checks a rule of a styleguide is what WAY-168 gives every rule of guidelines | WAY-168 |
| WAY-189 | its rule, the answer to "Which invariants does a styleguide start with?", stands in `product-guidelines/styleguide/settle.md` | none |
| WAY-190 | withdrawn: what keeps a product cleaned gradually from breaking a marked invariant again stands in WAY-51 for every marked invariant | WAY-51 |
| WAY-191 | its rule, the answer to "Where do a styleguide's thresholds of contrast and its demand of visible focus come from?", stands in `product-guidelines/styleguide/settle.md` | none |
| WAY-192 | its rule, the answer to "How does a product's instruction file lead to its styleguide?", stands in `product-guidelines/styleguide/task_document.md` | none |
| WAY-193 | withdrawn: the same rule for every discipline stands in WAY-173 | WAY-173 |
| WAY-194 | withdrawn: how both skills of guidelines ask the human stands in WAY-174 | WAY-174 |
| WAY-195 | withdrawn: what coding guidelines take from outside is no question a decision answers; each piece binds through the decision that carries it, with its source in *Based on* (WAY-100) | WAY-100 |
| WAY-196 | withdrawn: what checks a rule of coding guidelines stands in WAY-168 and WAY-198, and the invariants of a standing check in WAY-202 | WAY-168 · WAY-198 · WAY-202 |
| WAY-197 | withdrawn: the uses of a rule are optional lines of the rule (WAY-168), and the test of its invariant is seen failing once like every other (WAY-08) | WAY-168 · WAY-08 |
| WAY-200 | its rule, the answer to "Who designates a product's exemplar for a kind of code, and when?", stands in `product-guidelines/coding/kinds.md` and `product-guidelines/coding/SKILL.md` | none |
| WAY-201 | its rule, the answer to "How does the coding-guidelines skill's audit of a product with code end?", stands in `product-guidelines/coding/kinds.md` | none |
| WAY-207 | its rule, the answer to "Where is a fault of one file of a product's code fixed?", stands in `product-guidelines/coding/template.md` | none |
| WAY-208 | its rule, the answer to "Which parts of a product get coding guidelines?", stands in `product-guidelines/coding/recognize.md` | none |
| WAY-209 | its rule, the answer to "When do a product's coding guidelines come into being?", stands in `product-guidelines/coding/recognize.md` | none |
| WAY-210 | its rule, the answer to "What does the coding-guidelines skill look at first?", stands in `product-guidelines/coding/SKILL.md` | none |
| WAY-211 | its rule, the answer to "Where do the tools of the standing checks and a linter's set of rules come from?", stands in `product-guidelines/coding/starting_set.md` | none |
| WAY-214 | its rule, the answer to "How does task refinement find missing product guidelines?", stands in `project-level/task/skill/read_sources.md` | none |
| WAY-217 | its rule, the answer to "Does an approved departure count as missing guidelines?", stands in `product-guidelines/reading.md` | none |
| WAY-218 | its rule, the answer to "Where does project breakdown place missing guidelines and first-kind work?", stands in `project-level/plan/skill/guideline_tasks.md` | none |
| WAY-219 | its rule, the answer to "What does an author check before a user-interface change reaches review?", stands in `task-cycle/change/ui_check.md` | none |
| WAY-220 | its rule, the answer to "How does a code reviewer grade a finding about appearance?", stands in `task-cycle/review/SKILL.md` | none |
| WAY-221 | its rule, the answer to "When can departure from a guideline example support a blocking finding?", stands in `task-cycle/review/SKILL.md` | none |
| WAY-222 | withdrawn: what the task cycle takes from outside is no question a decision answers; the sources are private, so each piece binds through the decision that carries it, on that decision's own rationale (WAY-100, WAY-27) | WAY-100 |
| WAY-223 | withdrawn: it said only that a test protecting a history with no elements takes no evidence of its own; every invariant test is seen failing once (WAY-08) | WAY-08 |
| WAY-224 | withdrawn: the part map records no failure modes, so no cycle asks the human about one | none |
| WAY-226 | its rule, the answer to "Which glossary holds a word of the process, and which a word of a product's domain?", stands in `elements/glossary/template.md` | none |
| WAY-245 | its rule, the answer to "How does a product's instruction file lead to its testing guidelines?", stands in `product-guidelines/testing/task_document.md` | none |
| WAY-246 | its rule, the answer to "Which parts do testing guidelines apply to, and when are they read?", stands in `product-guidelines/testing/template.md` | none |
| WAY-248 | its rule, the answer to "What does the testing-guidelines skill look at first?", stands in `product-guidelines/testing/SKILL.md` | none |
| WAY-249 | its rule, the answer to "Where does the testing-guidelines skill's starting set come from?", stands in `product-guidelines/testing/starting_set.md` | none |
| WAY-250 | its rule, the answer to "How does the testing-guidelines skill's audit of a product with tests end?", stands in `product-guidelines/testing/audit.md` | none |
| WAY-257 | its rule, the answer to "What does the skill of `instruction-files` show as the ground of each verdict?", stands in `instruction-files/judging.md` | none |
| WAY-259 | its rule, the answer to "What does an installed skill entry point tell an agent to read from the pinned the-way?", stands in `installation/install.py` | none |
| WAY-262 | its rule, the answer to "What does an author report when a check fails and passes when run again?", stands in `task-cycle/change/SKILL.md` | none |
| WAY-264 | its rule, the answer to "How does a task plan represent output written together by one command?", stands in `task-cycle/plan/SKILL.md` | none |
| WAY-266 | its rule, the answer to "What does a session do that did not read the refinement steps a skill of guidelines relies on?", stands in `product-guidelines/coding/SKILL.md` | none |
| WAY-271 | its rule, the answer to "Which rules on failures and logs does the template of the coding discipline require?", stands in `product-guidelines/coding/template.md` | none |
| WAY-272 | its rule, the answer to "What counts as a failure, and where is it written?", stands in `product-guidelines/coding/template.md` | none |
| WAY-275 | its rule, the answer to "Which lines do a product's logs hold, and what joins them?", stands in `product-guidelines/coding/template.md` | none |
| WAY-277 | its rule, the answer to "Who chooses a library that writes a product's log lines?", stands in `product-guidelines/coding/settle.md` | none |
| WAY-278 | its rule, the answer to "How do the rules on failures and logs reach a product that has coding guidelines?", stands in `product-guidelines/coding/recognize.md` | none |
| WAY-279 | its rule, the answer to "What does a product's decision on the rules on failures and logs hold?", stands in `product-guidelines/coding/settle.md` | none |
| WAY-281 | its rule, the answer to "What does an audit of the skills of guidelines merge, and what does its list hold?", stands in `product-guidelines/audit_end.md` | none |
| WAY-282 | its rule, the answer to "In what order do the causes of an audit of the skills of guidelines stand?", stands in `product-guidelines/audit_end.md` | none |
| WAY-283 | its rule, the answer to "What of an audit's list of causes does the human decide on?", stands in `product-guidelines/audit_end.md` | none |
| WAY-285 | its rule, the answer to "How is a cause of the top of an audit's list checked?", stands in `product-guidelines/audit_end.md` | none |
| WAY-286 | its rule, the answer to "What form does the description of a request a task cycle opens take?", stands in `task-cycle/skill/request_template.md` | none |
| WAY-290 | its rule, the answer to "How is the form of a request's description checked?", stands in `task-cycle/skill/request_template.md` | none |
| WAY-291 | its rule, the answer to "What does the cycle do with an error of the form check that it holds wrong?", stands in `task-cycle/skill/request_template.md` | none |
| WAY-292 | its rule, that the collapsed block of the description of a request of an English task holds `none`, is a paragraph of WAY-288 | WAY-288 |
| WAY-296 | its rule, the answer to "In what form does the cycle record hold its process remarks?", stands in `task-cycle/record_template.md` | none |
| WAY-298 | its rule, the answer to "How does a cycle on the-way itself start from the current rules?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-299 | its rule, the answer to "How does a product keep the code of its parts within the dependencies its part map allows?", stands in `elements/part-map/template.md` | none |
| WAY-301 | its rule, the answer to "What marks the last review of a repository's foundation?", stands in `foundation-review/SKILL.md` | none |
| WAY-302 | its rule, the answer to "How does a review of the foundation go, and what does it change?", stands in `foundation-review/SKILL.md` | none |
| WAY-303 | its rule, the answer to "Which unfixed remarks of merged requests does a review of the foundation check?", stands in `foundation-review/remarks.md` | none |
| WAY-304 | its rule, the answer to "Which skill reviews a repository's foundation, and whose requests does it read?", stands in `foundation-review/remarks.md` | none |
| WAY-305 | its rule, the answer to "What does a review of the foundation do with the weak points that decisions name?", stands in `foundation-review/weak_points.md` | none |
| WAY-306 | its rule, the answer to "What does the review of the merge of the target branch ask?", stands in `task-cycle/skill/correction.md` | none |
| WAY-307 | its rule, the answer to "What happens to a spec whose review fails?", stands in `task-cycle/skill/spec_review.md` | none |
| WAY-310 | its rule, the answer to "How does a product's rule on secrets and personal data show a departure from the ban on personal data alone?", stands in `product-guidelines/coding/template.md` | none |
| WAY-311 | its rule, the answer to "How do the rows of a judgement of instruction files stand for a fragment that goes to several places and for a proposal?", stands in `instruction-files/judging.md` | none |
| WAY-317 | its rule, what a cycle does where the foundation settles no place for screenshots, is a paragraph of WAY-316 | WAY-316 |
| WAY-318 | its rule, the answer to "Which artifacts of a change's check reach the description of its request?", stands in `task-cycle/skill/request_template.md` | none |
| WAY-322 | its rule, the answer to "May a human strike from the list of the technology step a matter of an agent's way to the running product or of how a human learns of a failure?", stands in `project-level/technology/list.md` | none |
| WAY-323 | its rule, what the script of WAY-309 takes for an absolute path and for a note link, is a paragraph of WAY-309 | WAY-309 |
| WAY-325 | its rule, the answer to "What does the orchestrator of a task cycle do when a stage report says material its handoff names stayed unread?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-326 | its rule, the answer to "What does a task-cycle stage report about the material its handoff names that stayed unread?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-327 | its rule, the answer to "What does an item of a request's section for the human's decisions carry where the human chooses?", stands in `task-cycle/skill/request_template.md` | none |
| WAY-328 | withdrawn: the coding guidelines and the testing guidelines of the-way's own are written, so neither is missing and the departure that this decision recorded has ended | WAY-379 · WAY-392 |
| WAY-329 | its rule, the answer to "How is the identifier of a project task's line in the backlog derived?", stands in `project-level/task_line.md` | none |
| WAY-331 | its rule, the answer to "Where in the repository does the audit of the process stand?", stands in `foundations/part_map.md` | none |
| WAY-332 | its rule, the answer to "Where do the results of the audit lie?", stands in `process-audit/SKILL.md` | none |
| WAY-333 | its rule, the answer to "How is a problem that the audit counts graded and classed?", stands in `process-audit/problem_register.md` | none |
| WAY-334 | its rule, the answer to "What does the audit count, remarks or problems?", stands in `process-audit/problem_register.md` | none |
| WAY-335 | its rule, the answer to "What decides whether a fix of the process works?", stands in `process-audit/SKILL.md` | none |
| WAY-336 | its rule, the answer to "Does how often an issue comes back set its priority?", stands in `process-audit/SKILL.md` | none |
| WAY-338 | its rule, the answer to "What is the time of a cycle?", stands in `task-cycle/cycle_stages.py` | none |
| WAY-340 | its rule, the answer to "Does the audit replay frozen earlier tasks on an old and a new version of the process?", stands in `process-audit/SKILL.md` | none |
| WAY-341 | its rule, the answer to "How often does the audit run, and what starts it?", stands in `process-audit/SKILL.md` | none |
| WAY-342 | its rule, the answer to "Which entries of the locations file does the audit of the process read?", stands in `process-audit/audit_count.py` | none |
| WAY-343 | its rule, the answer to "Which version of the-way did a cycle of the-way itself run on?", stands in `process-audit/audit_count.py` | none |
| WAY-345 | its rule, the answer to "How is the cost of one occurrence of a problem that the audit counts graded?", stands in `process-audit/problem_register.md` | none |
| WAY-346 | its rule, the answer to "Where does the result of the audit's count show the cost of an occurrence?", stands in `process-audit/audit_count.py` | none |
| WAY-347 | its rule, that the measures of context and cache use are counted by a script and into a file of their own, is a paragraph of WAY-339 | WAY-339 |
| WAY-348 | its rule, the answer to "Does the weekly count of the audit read the measures of context and cache use and the gate times, and compare them?", stands in `process-audit/audit_count.py` | none |
| WAY-349 | its rule, the answer to "How does the orchestrator of a task cycle run the product's gate so that the gate times reach the cycle's record?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-351 | its rule, the answer to "How are the tokens written again to the prompt cache counted?", stands in `task-cycle/cycle_measures.py` | none |
| WAY-352 | its rule, the answer to "From which table of the stage report is the cost of a cycle counted?", stands in `process-audit/audit_count.py` | none |
| WAY-353 | its rule, the answer to "How does a task document point at a place to change in a file?", stands in `project-level/task/template.md` | none |
| WAY-354 | its rule, the answer to "What does a review of the foundation do with a decision that describes a transitional state?", stands in `foundation-review/proposals.md` | none |
| WAY-356 | its rule, the answer to "Where is a defect found after a merge recorded, and in what form?", stands in `project-level/task/template.md` | none |
| WAY-357 | its rule, the answer to "Where does the cycle record the cause of a correction after the request opened?", stands in `task-cycle/record_template.md` | none |
| WAY-358 | its rule, what causes the line of a correction gives, is a part of the question that WAY-357 answered, and both stand in `task-cycle/record_template.md` | WAY-357 |
| WAY-359 | its rule, the answer to "How does the template of the register of problems record a defect found at the request or after the merge?", stands in `process-audit/problem_register.md` | none |
| WAY-362 | its rule, the answer to "What does the review of the whole change ask about the structure of the code a change leaves, and from which numbers?", stands in `task-cycle/review/whole_change.md` | none |
| WAY-366 | its rule, the answer to "Do the directories of a product's tests run at the same time, and how does a product keep them from it?", stands in `gate/run_tests.py` | none |
| WAY-367 | its rule, the answer to "Does a task cycle run the gate on its starting state?", stands in `task-cycle/skill/SKILL.md` | none |
| WAY-369 | its rule, that the agent types of a task cycle start with the instruction files, is a paragraph of WAY-368 | WAY-368 |
| WAY-371 | its rule, the answer to "What reading limit does a slice of a plan have?", stands in `task-cycle/slice_size.py` | none |
