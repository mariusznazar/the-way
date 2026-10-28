# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and are edited in place.

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

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: fingerprint-definition. For a reference by identifier alone, an
  agent compares the change with the decision:
  - complies: a test names the invariant it checks as `invariant: map-reference-target`; a
    decision relates to another as `derives from WAY-01`;
  - violates: a new relation reads `derives from WAY-01@60960941`; a test cites
    `invariant: map-reference-target/1`.
- **Origin:** none

*Rationale:* an identifier outlives every rewording of its entry, so a reference by it stays valid,
and one naming no entry leads nowhere; what a change to an entry touches is found by the search its
author makes of the foundation (WAY-33), not by marks every reference carries and every rewording
renews. The digest is defined once, so a fingerprint recorded anywhere is computed the same way.
*Rejected:* a fingerprint beside each reference that relies on the entry's binding part — every
rewording makes its author renew marks that change no meaning, and flags raised for nothing get
cleared unread; a version beside a reference — a reference relies on what the entry says today;
flags from the kind of change — a misnamed kind silences them; the full 64-character digest —
unreadable, nothing gained.

### WAY-03 — Who may change an invariant test, and when?

Any change may alter an invariant test, in any step of its task, implementation included. A change
that alters an invariant test names that test in its request, so that the agent reviewing the
change and the human merging it see it.

- **Scope:** invariants, task-cycle, agent-instructions
- **Based on:** impossiblebench-test-modification
- **Relations:** derives from WAY-01
- **Verification:** an agent compares the change with the decision:
  - complies: an implementer whose code an invariant test stops fixes the code, or, where the test
    reads its sentence wrongly, fixes the test and names it in the request;
  - violates: a change alters an invariant test and its request does not name it; a test that read
    its sentence rightly is weakened so that the code passes, even where the request names it; a
    task goes back to an earlier step of its cycle only because an invariant test has to change.
- **Origin:** none

*Rationale:* an agent that a test stands in the way of adjusts the test to the code: the build
turns green, and the foundation lies. Naming every change to an invariant test in the request puts
that move in front of the reviewer, who did not make the change, and of the human at the merge
(WAY-10), while a test that reads its sentence wrongly is fixed where it is found. Naming is
enough where a block is not, because a changed test is read against the sentence it cites by
someone who did not change it, before the change merges.
*Rejected:* invariant tests read-only during implementation, kept so by a check at the merge, with
a return to the foundation step for every change of one — each needed fix of a test stops the task;
a local hook — one switch skips it; a written rule "do not change the tests" — prose stops nothing.

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

### WAY-05 — How is a decision entry written?

A decision entry opens with one to three binding sentences — in the present tense, describing
a state that is to be true, concrete enough to check — followed by fields a script or an agent
reads, then rationale and rejected options in prose, which, where the entry's author writes it
rather than quotes a source, names no file, script or count, nor what the process's own tools do or
lack today, and does not tell how the decision was reached. A field stays in the template only
while someone or something reads it, and what a decision forces on later work stands in a binding
sentence or a field, never in prose. An example in `elements/decisions/` names a decision of the
log by its number instead of copying it.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a new field enters the template together with the reader named in its table;
  - violates: a "notes" or "related artifacts" field that nothing reads.
- **Origin:** none

*Rationale:* a record written like a legal code is followed worse, and agents generalise from the
reasons they are given, so what binds stays short and checkable, reasoning below; a field
nobody reads goes empty, and long lists of fields stop people recording decisions.
*Rejected:* prose without fields — nothing a script can read reliably; many fields and relations —
fields without a reader; a hand-written status — every entry of the log binds; a one-sentence
entry — no reasoning beside the rule; "will" or "should" — an intent, not a state; capitals such as
MUST — shouting reads worse, not stronger; examples written for the template — an example with gaps
teaches gaps; a rule of the template changed only with a decision citing its number — the template
is the-way's own text, changed and reviewed like any other change to it.

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

### WAY-09 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a
directory for each part of the process other than `repository` — `elements/<element>/` for each
foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`,
`installation/`, `agent-instructions/`, `instruction-files/`, `project-level/`,
`product-guidelines/` and `task-cycle/` — the files that configure the whole repository, which its
part map gives to the `repository` part (WAY-44), the root agent instruction files and the project
skill entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to
`agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches
the main branch only once it holds what its part requires: an element its template and rules,
examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its
entries; `elements/common/` the rules of form and the way of working the elements' templates and
skills share, the script that checks a foundation, the script that migrates a foundation from the
earlier form, and the skills that find entries and that critique proposals; `project-level/` the
templates of a project definition, a project plan and a task document, the skills that write them
and lead a handed-over plan, the readiness check, the plan check, the reader of task-cycle evidence
for plan states and their tests; `relation-model/` the script that computes the fingerprint of a
project definition; `gate/` the command that runs every test, with its tests, and the test of every
critical flow; `installation/` the installer, its tests and a README explaining how a product uses
the pinned version; `agent-instructions/` the instructions for agents working on this repository,
led to from the root agent instruction files; `instruction-files/` the principles of instruction
files for coding agents, the account of how the tools load them, the skill that applies them, and
the script that checks instruction files with its tests; `product-guidelines/` the template that the
guidelines of every product share, for each discipline of work whose guidelines the-way gives a
template of, that template with the skill that leads the work on them; `task-cycle/` what the design
of the task cycle sets. The entries in
`foundations/` are checked by `elements/common/foundation_check.py`.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: repository-file-location · element-directory-contents. For what
  `elements/common/`, `installation/`, `agent-instructions/`, `instruction-files/`,
  `project-level/`, `product-guidelines/` and `task-cycle/` hold and for what checks `foundations/`,
  an agent compares the change with the decision:
  - complies: code two skills of the elements share moves into `elements/common/`, and both read it
    from there; a new rule of form for the entries in `foundations/` is checked by
    `elements/common/foundation_check.py`; the installer, its tests and instructions stand together
    in `installation/`; the templates of a definition, a plan and a task document, the skills that
    write them and the checks of a definition and a plan stand in `project-level/`; the agent
    instructions have their own part and root entry points; the project skill entry points under
    `.claude/skills/` and `.agents/skills/` stand at the root as files of `agent-instructions`, and
    the script that generates them stands with its test in `agent-instructions/`; the principles,
    the loading account, the skill and the check script of instruction files stand together in
    `instruction-files/`; the template of guidelines and the template and the skill of the
    styleguide discipline stand together in `product-guidelines/`;
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
not those of instruction files.
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

### WAY-10 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation has no assessment of its own, in a product as in
the-way itself: an agent that did not make the change reviews the whole change, its foundation
entries and invariant tests included, against its task and the foundation, and a human reads the
diff of the foundation and accepts the change by merging its request.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  task-cycle, agent-instructions
- **Based on:** llm-self-preference
- **Relations:** derives from WAY-03
- **Verification:** an agent compares the change with the decision:
  - complies: a change that rewords a decision and the invariant test deriving from it is reviewed
    on its whole diff by an agent that did not make it, and the human merges it with no other
    assessment;
  - violates: the author reviews its own change to the foundation; a cycle requires an assessment
    of its own of a change's foundation entries before the merge; a change merges whose foundation
    entries no reviewer read.
- **Origin:** none

*Rationale:* the problem is a single executor that checks itself: a model judging what it wrote
favours it, so an agent that did not make the change reads it. An error of the product shows where
the code and the foundation meet, and the review of the whole change reads both against the task;
an assessment of the foundation apart from the code sees only entries, so what it finds beyond the
review are faults of form and of checks, which the tests and the human reading the diff of the
foundation at the merge also meet.
*Rejected:* one independent assessor on a model other than the author's, which sees the diff
without the author's reasoning and names what of the change can be cut — a stage of its own in
every cycle that writes entries, reading entries without the code the review reads with them; a
panel of two assessors and a settler reading both orders — its cost per change outweighs what one
reader misses, and its uncertainty becomes questions for the human; the author assessing its own
change — it checks itself.

### WAY-11 — How does a task end?

A task ends with its return step before its branch is merged: an agent compares with the code the
foundation entries the change writes or changes, those its task names and those the search of the
foundation found, and the part map of the parts the task touched, and corrects in the same change
whatever no longer matches. In the same change it writes the sources outside the product that the
change rests on and the foundation does not yet hold, as environment facts, a word the change uses
in a meaning other than the usual one, as a glossary term, and the accepted settlements (WAY-134)
and projected entries (WAY-126) the task carries that are not yet written. It writes an invariant
only for a rule the task, a decision or a human sets, never for code behaviour merely because no
invariant covers it.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01
- **Verification:** invariants: return-step-record. For what the return step compares and writes,
  an agent compares the diff, the task and its sources with the decision:
  - complies: the return step finds that a part-map entry still names a file the change removed and
    corrects it; the release notes of a library the change rests on are written as an environment
    fact; a replaceable layout calculation stays in ordinary tests; an invariant the task's
    settlement sets is written;
  - violates: a decision the change makes false is left for a later task; behaviour of the diff
    becomes an invariant only because no invariant covers it; an accepted settlement or an
    applicable projected entry is left out.
- **Origin:** none

*Rationale:* some of the foundation is learned only in implementation, and a change that drifted
from an entry does not report it; comparing what the change touched with the code finds that drift
where it arises, at the cost of reading only those entries. Facts and words are written because,
like rules, they are learned in code. An invariant written for behaviour no task, decision or human
sets binds a detail nobody chose, and its test fails on later changes nobody objects to.
*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
in the code; a search of the diff and the task's log for every behaviour no invariant covers, each
turned into an invariant where a later change could break a requirement — it costs a large share of
a cycle and binds details nobody chose; ordinary tests alone for a rule the task sets — later work
can change it without meeting a foundation check.

### WAY-12 — How is a decision checked?

A decision names in *Verification* the invariants derived from it, by the identifiers of their
entries, where such invariants exist, and tests live only with invariants. A decision may also
carry a pair of examples — a change that complies and one that violates — with which an agent
compares a change with what no invariant of the decision checks; the violating example is a change
whose code goes against the decision while its entry stays as it is, never one that replaces the
decision together with its code.

- **Scope:** decisions, invariants
- **Based on:** llm-decision-violation-detection
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision on the product's direction carries a complying and a violating example
    and names no invariant; a decision with a derived invariant names it after `invariants:`;
  - violates: a decision names an invariant whose *Derives from* names another decision; a
    decision asks for a human's assessment recorded in its entry; the violating example of a
    decision is a change that takes an option the decision did not take and rewrites the decision
    in the same request.
- **Origin:** none

*Rationale:* a test checks an invariant on every commit; a decision about direction or trade-offs
often cannot be. Agents judge explicit, code-readable decisions well and deployment- or
organisation-dependent ones poorly, a finding this decision takes across publishers (WAY-85), so a
pair of examples marks the line where it helps, and the human who accepts a change sees the rest.
*Rejected:* a rule in code as the only check — decisions that cannot be written as a rule go
unchecked; a level of verification named in every decision, a human's assessment among the levels
— the level adds nothing to the invariants named and the examples given, and every change already
reaches a human before it binds (WAY-14).

### WAY-13 — What sets the weight of a task's process?

Every change, whatever its size, passes the product's tests and a review by an agent that did not
make it. At its start a task's cycle answers two questions — does the change touch the files of a
trust boundary (WAY-48), and does it hold an operation that cannot be undone — and a change for
which either answer is yes gets a review aimed at that risk; an operation that cannot be undone is
only prepared, and a human performs it after deciding at the request. A task's size may lighten how
its change is prepared and made — its plan and the number of agents making it — never the outcome
it has to reach or the checks run on the finished change, and otherwise serves only as a signal to
split it; only a human sets a task to return knowledge instead of a change, which merges nothing.

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
    that returns knowledge instead of a change without a human setting it so.
- **Origin:** none

*Rationale:* size misleads about what can go wrong: a rename across many files is easy to undo, a
one-line change to a stored format can destroy every user's data. What a stranger can send and what
cannot be undone are the risks a review aimed at them catches and an ordinary review may pass, and
two questions name them at the start without computing anything. Size does tell how much
preparation a change needs: a small change can be made without a plan, while the checks on the
finished change stay whole and a human still decides on what cannot be undone. Returning knowledge
alters what a task delivers, so a human sets it.
*Rejected:* checks as sharp as a criticality computed from the parts a change touches, with the path
that merges it chosen by whether it changes the foundation, recorded at the start and recalculated
after each diff — every cycle computes and records them, and a part with no failure modes recorded
draws the sharpest checks whatever it holds; the path chosen by size — size misleads; a human
approving every diff (DORA) — no fewer failed changes, and attention spent where it adds nothing;
keeping a change that cannot be undone, or one touching a trust boundary's files, from the lighter
preparation — it would take the lighter preparation from small tasks it suits, while a human's
decision and a review aimed at the risk already stop such a change.

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

### WAY-16 — How are the checks of invariants run?

One command runs all of a product's tests, the tests of its invariants among them — the
same command for an agent, for a human and for whatever runs it when a change is merged —
and no list of checks written by hand stands beside it.

- **Scope:** invariants, agent-instructions, task-cycle, gate
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: ci-checking-commands · gate-exit-code. For the same command for
  everyone, an agent compares the change with the decision:
  - complies: the instructions for agents name that one command as the way to check a change;
  - violates: the instructions for agents list test and lint commands of their own; the tests of
    the invariants run under a command of their own beside the product's tests.
- **Origin:** none

*Rationale:* a list of checks written by hand is a second copy of the tests that drifts: a new
test never runs, a removed one still does. One command for all leaves no doubt which tests ran, and
running all of them leaves nothing to choose.
*Rejected:* a gate taking its checks from the methods written in the entries and running those a
change calls for — a second runner beside the product's tests, and a choice of tests that can
leave out the one a change breaks; separate commands for an agent, a human and whatever runs the
tests when a change is merged — three lists to keep in step; the tests of the invariants under a
command of their own — of two commands an agent runs one.

### WAY-17 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends
on the other, and none is optional: a decision and an invariant name the environment facts they
rest on, an invariant derived from a decision names that decision, and a check names its
invariant.

- **Scope:** decisions, invariants, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02
- **Verification:** none
- **Origin:** none

*Rationale:* the chain is the path a change travels, so a missing link breaks it without a sign,
and an assumption no entry names escapes review; the link sits in the dependent entry, because
only its writer knows what it rests on.
*Rejected:* links written by the entry depended on — it cannot know its dependents; optional
links — a missing one looks unneeded; research findings outside the environment facts — a search
from a changed finding would find no decision about agents that rests on it.

### WAY-18 — How is a product's decision log kept?

A product keeps all its decisions in one log, whatever they are about. The log holds one entry for
each decision in force, in the order the entries were written, and says what binds today with no
view generated from it. A link between entries is written at one end only; the one exception is a
decision's invariants, which its *Verification* names while each of them names the decision in
*Derives from*.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a business rule and a technical constraint of one product stand in the same log
    under one numbering; a product's existing architecture records stay a source, and a decision
    recovered from them enters the one log;
  - violates: a separate log for business decisions next to the technical one; a decision that
    another narrows names that other in its own *Relations* as well.
- **Origin:** none

*Rationale:* one log, because a collision is caught only between decisions in the set a change is
checked against; the log itself says what binds, so a reader reaches it without assembling versions
or generating a view; a link is written once, because two copies of it drift apart.
*Rejected:* a log of every version and review, with a view of what is in force generated from it —
the view is one more thing to build and keep, and the history it leaves behind is what git keeps;
marks written by hand at a link's other end — they go missing; separate logs for business and
technical decisions — collisions between them go unseen; a log per approver — git records who
merged each change (WAY-14); a field for an entry's topic — nothing reads it (WAY-05).

### WAY-19 — How are decisions numbered?

A number stands for the question a decision answers, carries the product's prefix and is given
in the order entries are written; a new question gets the next free number, and a new rule next
to an existing decision is a new question. A new answer to a question the log holds rewrites that
question's entry. When a new decision answers a question that an older one answered in passing, the
sentence moves to the new decision, and the older one loses it in the same change.

- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: a new rule for who accepts a decision is written into WAY-14; when a decision on a
    question arrives, an older decision that answered it in passing loses that sentence;
  - violates: the same question gets a second number; the sentence stays in both decisions.
- **Origin:** none

*Rationale:* a permanent number lets references survive a change (WAY-02); a new answer rewrites
the one entry, so no reader assembles the decision from pieces; a sentence answered in passing
moves, because two entries answering one question drift apart; the product's prefix keeps numbers
of different products apart in references.
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
paths into each entry. Topics cannot be derived from changed files.
*Rejected:* file paths in each decision — duplicate the map; topics — cannot be derived from a
change; no scope — relevant decisions get lost among the rest.

### WAY-22 — Is a rule a decision or an invariant?

An invariant says nothing about why or what was rejected; a decision is a choice between
options, with its rationale, and it binds later work until a change replaces, narrows or withdraws
it, including what cannot be checked on a commit — direction, trade-off principles, non-goals. A
rule that records a choice is a decision, and what of it a commit can make false is written as an
invariant derived from it; a rule with no choice behind it is an invariant alone.

- **Scope:** decisions, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "the product has no multiplayer" is a decision, and "no screen offers a second
    player" an invariant derived from it; "a saved game is never lost on reload" is an invariant
    with a test;
  - violates: a non-goal that a commit can break is left without a derived invariant; an
    invariant carries a rationale and rejected options.
- **Origin:** none

*Rationale:* an invariant is checked mechanically on every commit, a decision weighed when a later
choice is made; a checkable rule left only in a decision's prose escapes the gate, and a choice
written only as an invariant loses its reasons.
*Rejected:* one kind of entry for both — either the gate reads prose or the reasons are lost;
moving a checkable sentence out of its decision — the rule would be cut off from its reason.

### WAY-24 — How is a decision that rests on a prediction reviewed?

A decision names no date or condition for its review, the log holds no record of a review, and
the review of the foundation against the product is a task of the product's backlog.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision's entry holds no field for its review; a task of the backlog reviews the
    foundation against the product;
  - violates: an entry carries a check-by date; a record of a review is appended to the log.
- **Origin:** none

*Rationale:* a date in an entry asks for a look nobody is sent to make, and passes unseen; a review
of the whole foundation, set as a task, looks at all of it at once.
*Rejected:* *Review when* in each entry, with an observable state and a check-by date, and a review
record appended on the date — the dates pass with nobody looking; a decision that expires on a date
— the date gets extended.

### WAY-25 — What settles a collision between two decisions?

Where two decisions both apply and collide, the one that prevails names the other in *Relations*
as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a
chain, and two decisions that narrow each other are an error. A collision between two decisions
with no precedence recorded is never settled by the agent that meets it; a human records the
precedence in the decision that prevails.

- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: an agent meets two applicable decisions that pull opposite ways, finds no
    precedence between them, stops and asks for it;
  - violates: an agent settles the collision in favour of the newer decision; an agent infers
    that A prevails over C because A narrows B and B narrows C.
- **Origin:** none

*Rationale:* pairs record only what someone actually weighed; nothing follows along a chain, because
A over B and B over C were weighed in different situations; an agent that settles an unrecorded
collision makes a trade-off no human made, and the human who records it answers for it.
*Rejected:* one ranked list of principles (AWS tenets) — an order claimed for pairs nobody weighed;
levels of authority over whole groups of decisions — a collision inside a level stays unresolved;
the newest decision wins — the date of a decision is not its weight.

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

### WAY-27 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every
entry carries its whole reasoning, and what is seen only in such a source is described in the
entry instead of being pointed to. The one exception is the place of its tasks, named in the
`## Backlog` section of its root `AGENTS.md` and nowhere else.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, agent-instructions, instruction-files, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: outbound-link-reach. For the reasoning in the entry, an agent
  compares the change with the decision:
  - complies: a decision quotes a public study with its address; a pattern seen in a product
    outside the repository is described in the rationale, without a pointer to it; the-way's root
    `AGENTS.md` names, in `## Backlog`, the private note where its tasks are kept;
  - violates: *Origin* points to a private note; a rationale rests on "as in our other product"
    without saying what was seen.
- **Origin:** none

*Rationale:* a pointer to a source the reader cannot open is a dead end, leaving a claim nobody
can check; what was seen there, written down, can at least be judged, and WAY-17 still has a fact
to name. A backlog place is where work is kept, not reasoning an entry rests on, and WAY-107 sends
an agent there; named in that one section, it stays a place to find work and never becomes a
source an entry points to.
*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader can open
them.

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

### WAY-29 — How is a decision recovered from an existing product written?

A decision recovered from the code of an existing product says in *Origin*, in one sentence, that
it was recovered from the code and where in the code it shows, and its rationale and rejected
options are quoted from a source, given by a human who knows them, or written as `unknown`. A
rationale an agent proposes for a human's decision goes to the human as a question, never into the
entry; the rationale of a decision an agent takes in a task is the agent's to write.

- **Scope:** decisions
- **Based on:** llm-design-rationale-expert-overlap
- **Relations:** derives from WAY-28
- **Verification:** for *Origin*, an agent compares the change with the decision:
  - complies: the *Origin* of a decision recovered from a product's saving reads `recovered from
    the code at src/core/save.py, save_game`;
  - violates: *Origin* lists what was searched and what was found.
  For the agent's role, an agent compares the change with the decision:
  - complies: an agent finds the reason in a merged request and quotes it; an agent finds nothing
    and asks, and the entry gives the reason under the name of the human who knew it; the
    *Rationale* of a recovered decision whose reason nobody knows reads `unknown`;
  - violates: an agent writes a plausible reason inferred from the code into the entry; an agent
    lists in *Rejected* the options it infers were weighed.
- **Origin:** none

*Rationale:* a reason an agent writes looks exactly like a recorded one, and later readers take it
for the reason the decision was made; a human who knows it is a source, a guess is not. The cited
study compared generated arguments with expert rationale after giving models the problem and
decision; it did not test recovery from code, and argument overlap is not a correctness rate. The
place in the code shows a reader where the decision acts, and `unknown` shows nobody knows what the
decision guards.
*Rejected:* an agent's rationale in the entry — read as the reason the decision was made; rejected
options filled in as `none considered` — nobody knows what was considered; *Origin* recording what
was searched and what was found — a list nothing reads once the decision is written, while the
place in the code says where to look.

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

### WAY-32 — What types of relation can a decision name?

A decision names its relation to another decision with one of two types, and the list is closed:
`derives from` — a higher decision this one serves; `narrows` — a decision this one deliberately
goes against in a narrower area.

- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision that exists to serve WAY-01 names `derives from WAY-01`; a rule for one
    part that deliberately departs from a general decision names `narrows`;
  - violates: `narrows` for a decision that only mentions another; a new answer to an old question
    given a new number and a relation instead of an edit of the old decision.
- **Origin:** none

*Rationale:* a relation type each author reads differently tells a reader nothing, so each type is
defined once and the list is closed; both types rely on what the other decision says, and `narrows`
also records precedence (WAY-25), telling the checking agent where the other does not apply.
*Rejected:* `related to` — it relies on nothing, so nothing reads it.

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
conflict (WAY-01); the change accepts that risk, since the review and the human who sees every
entry it alters in its request read it against the foundation.
*Rejected:* marks on links flagged by a change — they see only written links, and renewing a mark
does not lead to a change in the entry that carries it; a search within overlapping scopes —
contradictions between parts go unseen; a search of linked entries only — entries written apart go
unseen; a second search against the main branch before the merge, with the record of both — it
repeats the first search, and a record shows that a search ran, not what it missed.

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
    pin in its branch's first commit, before its route is judged, the entry points and guidance the
    installer rewrote included, and carries what the newer version changes for the product;
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

### WAY-35 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the
element's entries stands in the element's template, or once in the part the elements share
(WAY-09) where it is common to them; the way of working the skills share stands once in that part,
and a skill reads the rules and that way of working from there instead of restating them.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: skill-rule-source. For what the skill holds, an agent compares the
  change with the decision:
  - complies: a fix to a field's form in the skill's output goes into the template, not the
    skill; the skill orders its steps and says what to ask;
  - violates: the skill says a rationale has at most three sentences while the template does not;
    the skill restates the list of fields.
- **Origin:** none

*Rationale:* an entry written by hand or by another agent meets only the template and the shared
part, so the rules stand where every writer and every check reaches them; steps and questions are
no rule of an entry.
*Rejected:* rules restated in the skill next to the template — two copies that drift, and the
template and the skill hold entries to different rules; each rule citing the decision that sets
it — the rules are the-way's own text, changed and reviewed like any other change to it.

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

### WAY-37 — What happens to entries that wait for something when it arrives?

A change that brings what entries of the foundation wait for — an element's template, the part
map, a script — also fixes every entry that waits for it, in the same change. The author of the
change finds those entries in its one search of the whole foundation (WAY-33).

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the change bringing the invariants template turns every invariant named in working
    form into a reference to its entry;
  - violates: the part map arrives, and WAY-21 still says that a scope names parts from a working
    list.
- **Origin:** none

*Rationale:* an entry that says what holds until something exists turns false when it arrives, and
nothing leads from what arrives to what waits for it. Whoever brings it knows what it is, while the
authors of the waiting entries may be gone; a fix left for later goes missing.
*Rejected:* fixes left to the periodic review (WAY-24) — the foundation says something false until
the review comes.

### WAY-38 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard
library alone, and installs nothing. It calls git, the Python interpreter running it, and the
commands a product declares in its own repository, reading their output through an adapter for the
format. Where a product declares no such command, the script reports what it could not check, never
agreement.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions,
  instruction-files, project-level, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: script-language · script-imports · script-subprocesses.
- **Origin:** none

*Rationale:* a product runs the scripts of its pinned commit (WAY-34), so every language and
package they need is something each product has to provide. The state of a language the scripts do
not parse, the product's tools already compute; a check that quietly sees nothing would pass.
*Rejected:* Node.js without packages — no abler than Python, and a second interpreter for every
product; shell scripts in Bash or PowerShell — they run differently on Windows and on Linux; a
compiled program in Go or Rust — every change needs a build and published files; each script in
its author's language — every product needs every interpreter chosen; the product's CI committing
that output for the scripts to read — no signal before a push, and a CI step for this process
alone; the scripts parsing other languages themselves — tools that tried gave it up
(cargo-semver-checks).

### WAY-40 — What kinds of entry does the part map hold?

The part map holds two kinds of entry: a part and a surface. An allowed dependency and a trust
boundary are fields of the part they belong to, so neither is an entry of its own, and a critical
flow has no entry (WAY-45). The whole map lives in one Markdown file of fixed shape in
`foundations/`.

- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-04
- **Verification:** an agent compares the change with the decision:
  - complies: a payment service is a part, and the file format its clients read is a surface;
  - violates: the map holds an entry for a critical flow, a list of known violations of its
    allowed dependencies, or a criticality scale.
- **Origin:** none

*Rationale:* each kind answers what the other cannot: a part, what it is responsible for and which
files are its; a surface, what someone outside relies on. A dependency has no identity beyond its
pair of parts, and the map is read whole.
*Rejected:* a dependency as an entry with its own identifier — nothing refers to it alone; a
critical flow as a kind of entry, with its criticality, its parts and its coverage — an invariant
and its test already say what has to keep working along it and where a change can break it (WAY-45);
the dependencies the code holds against the map as a derived list beside it — a list compared with
nothing goes stale, while a violated invariant stands where its reader sees it (WAY-51); one file
per part — a rename becomes a move of files.

### WAY-41 — What identifies an entry of the part map?

Every entry of the part map carries a permanent identifier made of words, such as
`relation-model`, and it stays the same when the files assigned to it change. Splitting or merging
entries gives each entry that comes out of it a new identifier; the identifier left behind, and the
identifier of an entry removed with nothing in its place, stays in the map as a withdrawn identifier
giving why and naming its successors, or `none` for an entry removed; an identifier is never
reused.

- **Scope:** part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-40
- **Verification:** invariants: map-reference-target.
- **Origin:** none

*Rationale:* every reference to a part rests on its identifier, so it must outlive a move of the
part's files; words, because a number says nothing where it is read; a withdrawn identifier stays,
so an old reference still says where the part went.
*Rejected:* the path as identity (Packwerk) — a moved folder renames the part; a number —
unreadable where it is read; a number beside the name — a second field for a rare rename; a reused
identifier (Backstage) — an old reference silently points elsewhere.

### WAY-42 — What is the binding part of a part map entry?

The binding part of an entry of the part map is one sentence: a part's responsibility or a
surface's promise. Path patterns, allowed dependencies, a trust boundary and who relies on a
surface stay outside it.

- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: a part's sentence says what it answers for, and a directory moved to another place
    changes only its *Files*;
  - violates: a part's sentence lists the directories its files sit in, so that a move rewrites
    it.
- **Origin:** none

*Rationale:* whatever names an entry relies on what the entry answers for, and a change of that
sentence sends the author to the entries naming it (WAY-02, WAY-33). Files and the other fields
change more often without changing what the part answers for; making them binding would send the
author there for changes that do not alter that promise.
*Rejected:* the whole entry — every moved file would count as a change of meaning; a fingerprint
beside each reference — renewed on every reworded sentence, while a reference by identifier and the
search on each change of a sentence find the same entries (WAY-02).

### WAY-44 — What assigns a file to a part?

Every file git tracks belongs to exactly one part of the map, by path patterns that git itself
matches, each naming a directory or one kind of file — every invariant test, say — rather than
listing a directory's files one by one; a file that no pattern matches, and a file that two parts
claim, is an error of the check of the foundation, unless the map lists that file as left out on
purpose, and so is a pattern of a part's *Files* or *Trust boundary* that matches no file git
tracks. Tests belong to the part they test and generated files to the part of their generator; the
files that serve the whole repository — the lockfile and the build configuration — are a part of
their own, and the files that only direct whoever carries out its tasks — instructions for agents,
skills, hooks and the configuration of agents' tools and of CI — are another. For a file that
collects entries about many parts, the parts a change touches follow from the entries it adds or
changes, not from the part the file itself belongs to.

- **Scope:** part-map, agent-instructions, task-cycle
- **Based on:** git-path-patterns
- **Relations:** derives from WAY-40
- **Verification:** an agent compares the change with the decision:
  - complies: a change renaming `net/` to `network/` rewrites the *Trust boundary* `net/*.py` of
    its part, and `elements/common/foundation_check.py` reports no pattern matching no file;
  - violates: the *Trust boundary* still names `net/*.py`, which matches no file git tracks, and
    the change is merged with that error of the check.
- **Origin:** none

*Rationale:* a change is read against the decisions and the invariants of the parts it touches
(WAY-21, WAY-62), so every file yields one part. git matches, because a second dialect could resolve
the same map differently. A pattern for a directory or a kind of file leaves the map as it is when a
file is added or moved inside it. A test changes what its part promises; files directing whoever
carries out tasks change every later task.
*Rejected:* a file in several parts — two answers, no rule to pick; patterns matched by a script
(fnmatch) — a second dialect beside git's; a pattern for each file — the map changes with every file
added or removed; tests as a part of their own — a test change stops counting against what it tests;
files left unassigned in silence — the map passes while saying less and less; a ledger file's part
taken from its path — every recorded decision counts against the decisions part alone.

### WAY-45 — How is a critical flow recorded and tested?

A critical flow has no entry in the part map. What has to stay true along it is an invariant whose
*Part* names the parts the flow runs through, and its test is a test of the product's suite like any
other, run with the rest of the suite.

- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-40
- **Verification:** an agent compares the change with the decision:
  - complies: what has to keep working along a payment flow is an invariant whose *Part* names the
    parts the flow runs through, and its test runs whenever the product's tests run;
  - violates: the map holds an entry for the flow; the flow's test runs only when a change touches
    one of its parts.
- **Origin:** none

*Rationale:* the product's tests run whole on every change, so a flow's test needs no list of parts
to be chosen by, and the invariant's *Part* already names where a change can break the flow
(WAY-62).
*Rejected:* the flow as an entry of the map with its criticality, its list of parts and a coverage
file — a second record of what the invariant's *Part* says, choosing tests that run anyway; a
comment line naming the flow in its test — a link nothing reads; the flow as a mark at each part —
the same list in two places; picking flow tests from the change (Azure Test Impact Analysis) — it
fails where it cannot reason.

### WAY-48 — How is a trust boundary recorded?

A trust boundary is recorded at the part that holds it, as a pattern of the code files which take
in what the product does not control — data from the network, keys, the deployment, files that come
from outside the product, such as one on the user's disk — and never at a script that only checks
the product's own files. An exchange with the external context records its direction and
marks what comes in as untrusted. A change that touches the files of a boundary is checked for
crafted input, and its review is aimed at that risk.

- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-40
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

### WAY-49 — How does the part map record a surface, and how is a change to it made known?

A surface is what someone outside the product relies on — an API, a file format, a command — and
its entry in the part map states the promise in one sentence and names who relies on it. A change
that alters a surface names the surface in its request.

- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-40
- **Verification:** an agent compares the change with the decision:
  - complies: the entry of a save-file format names the players whose saved games the product must
    keep reading, and the request that renames one of its fields names the surface;
  - violates: a surface carries a level of promise or a path of change of its own; a change drops a
    command-line option, and its request does not name the surface.
- **Origin:** none

*Rationale:* a broken promise falls on someone who took no part in the change, so the map names who
that is, and the request names the change for the agent reviewing it and the human merging it.
*Rejected:* a declaration at the item with the level of the promise and a date of withdrawal, one
change path for each level and a record of whether a partner updates together with the product —
machinery to keep for each surface, while the one who relies on it and a change named in the request
reach the reviewer and the human; surfaces computed from the code — tools see shape, never the
promise.

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
entries, which a reader of the invariant does not see; a derived list of the dependencies the code
holds against the part map — the same second file, and a dependency the map does not allow is an
invariant like any other (WAY-225); a rule left out or marked "not checked yet" until met — the gap
stops being countable; debt paid by an end date — repaid by weakening the rule; beside the marked
invariant, a second one holding from its first day that no file holds more breaks than on
`{fork-point}` and a file not there holds none — an entry kept only for the time of the cleaning,
whose withdrawal nothing checks, and a renamed file looks new to it; a test over a growing list of
cleaned files — the list decides the invariant and changes with no change of the foundation; every
file a change touches cleaned in full — a small change to a large file grows into cleaning it
whole.

### WAY-52 — What is generated from the part map for an agent?

Nothing is generated from the part map for an agent: an agent reads the entries of the parts its
change touches, and no overview of the repository is generated for it.

- **Scope:** part-map, decisions
- **Based on:** context-file-effect · claude-code-path-rules
- **Relations:** derives from WAY-40 · derives from WAY-21 · derives from WAY-44
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

### WAY-56 — How much does one invariant entry hold, and what is its binding part?

An invariant entry states one invariant in one sentence, which is its binding part. The method of
checking and the links that WAY-08 and WAY-17 require stand beside that sentence, not inside it.

- **Scope:** invariants
- **Based on:** none
- **Relations:** derives from WAY-22
- **Verification:** an agent compares the change with the decision:
  - complies: "every entry of the log has every field of the template" as one entry;
  - violates: "binding sentences number one to three and contain no *should*" as one entry; the
    sentence on fields split into one entry per field.
- **Origin:** none

*Rationale:* one invariant per entry lets the failure of its test, seen once, show that the test
catches that rule (WAY-08).
*Rejected:* a split wherever a commit can break part of a sentence — one entry per version of the
log.

### WAY-58 — What does an invariant entry record in *Derives from* when no decision entry of the product's log carries it?

An invariant entry that no decision entry of the product's log carries, taken from a source outside
the log — a ticket, a requirement of the product — names that source in *Derives from* with its
address, the place in it, the passage stating the rule quoted word for word between quotation
marks and the date it was read. One that a human chose from what the product already did before the task writing it began,
as WAY-28 describes, and that no such source carries either, reads in *Derives from* that it was
recovered from code, with the place in the code that shows the behaviour. Neither states a reason
for the behaviour, nor one an agent infers.

- **Scope:** invariants
- **Based on:** none
- **Relations:** derives from WAY-28 · derives from WAY-22 ·
  derives from WAY-17
- **Verification:** an agent compares the change with the decision:
  - complies: from a game's save module a human chooses "a save of another version is rejected
    whole", whose *Derives from* reads `recovered from code — the version check of the save loader
    in src/save.ts`; an invariant written for a feature being built names its decision; an invariant
    taken from a ticket the product does not meet yet reads in *Derives from*
    `https://tracker.example.org/browse/GAME-12 § Acceptance criteria — "a save of another version
    is rejected whole"; read 2026-10-21`;
  - violates: a recovered invariant's *Derives from* reads "old saves are dropped because the rules
    may have changed"; an invariant on a field the task adds reads recovered from code; a recovered
    invariant names no place in the code; an invariant taken from a ticket names the ticket by its
    key alone, or reads recovered from code.
- **Origin:** none

*Rationale:* WAY-28 lets a recovered invariant bind before anyone knows why it holds; without the
mark it reads like a chosen rule, hiding that its reason was never settled, and the place in the
code leads whoever weighs a change to the behaviour. A rule taken from a ticket or a requirement
keeps in the foundation where it came from, and the address, the passage and the date let a reader
find that source and see whether it still says so, as in a decision's *Based on* (WAY-90). The
reason stays out, since an invariant says nothing about why (WAY-22).
*Rejected:* a list of recovered invariants with what was searched and found, set by the human at the
merge from the gate's run on the older commit — a second record beside the entry, and a rule new to
the task can pass that run too; the mark only where no cause is known — a cause in a code comment or
a concept document gives the rule two readings; a decision kept outside the log counted as named —
nothing checks it; the reason quoted beside the mark — a why inside an invariant.

### WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation
change a human decides, or where a decision in the product's log or the pinned the-way places it.
An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}`
(WAY-61), while a state it compares may be the one on `{merge-onto}`, and states what is to hold on
the main branch alone as holding where `{merge-onto}` exists. A sentence bounding or equating a
quantity measured while the product runs names its bound or tolerance, statistic and population.

- **Scope:** invariants, decisions, part-map, gate
- **Based on:** none
- **Relations:** derives from WAY-22 · derives from WAY-56
- **Verification:** an agent compares the change with the decision:
  - complies: "every entry of the log has every field of the template";
  - violates: "every request is answered within the limit set in `config.py`"; "every fingerprint
    on `main` equals the current fingerprint of the decision it names"; "a commit that changes
    `template.md` also appends a decision version to the log"; a bound written "~2 seconds"; a
    sentence measuring a change against `{merge-onto}`.
- **Origin:** none

*Rationale:* a condition outside the sentence moves while the sentence stays, so it stands only
where moving it takes a decision; a branch names another commit by the hour; a change is measured
from the fork point, where the work on it began; a measured bound needs its statistic and
population.
*Rejected:* every condition in the sentence — two answers where a measure meets a definition or a
method; a closed list of places — it leaves out places a log uses; every place outside the
foundation forbidden — WAY-38 and WAY-53 place conditions in the product; an invariant kept aside
until its condition has a home — nothing counts it (WAY-51); a commit's parent as the base — a task
spreads one change over several commits.

### WAY-61 — How is an invariant's method of checking written?

An invariant's method of checking reads `test` once a test of the product's test suite, written in
the product's language and run by the command that runs the product's tests, cites it, and `review`
until then, and it names no command and no script. A test checks what its invariant's sentence is
about, as it stands on the commit being checked, so a test fed input made up for it is the method of
a sentence about the check it exercises, never of one about the data that check reads.

- **Scope:** invariants, gate, decisions, part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-08 · derives from WAY-16 ·
  derives from WAY-54 · derives from WAY-07 · derives from WAY-38 ·
  derives from WAY-60
- **Verification:** an agent compares the change with the decision:
  - complies: a sentence about the instruction files of the repository is kept by a test running
    its check on those files; a sentence about the loader is kept by a test handing it a save of
    another version; a sentence on whether an image's text alternative describes it reads `review`;
    an invariant written before its test reads `review`, and the change that adds a test citing it
    turns its method to `test`;
  - violates: a sentence about the real instruction files names as its test the check's own test,
    which feeds it made-up files; an invariant's test is a script beside the product's suite, which
    the command running the product's tests does not run; an invariant reads `test` while no test
    cites it; an entry names `python -B tools/check_saves.py` as its method.
- **Origin:** none

*Rationale:* the command that runs the product's tests already runs on every change, so an
invariant's test runs with them, in the product's language; one run serves many invariants, each
needing an outcome of its own; a check that sees nothing passes quietly (WAY-38). An invariant may
be written before its test, and its method then says what keeps it meanwhile: the review.
*Rejected:* a command per invariant that a gate of its own runs, recording a verdict for each entry
— a second runner beside the product's tests; `TODO` as the method until the test exists — it
names nothing that keeps the rule meanwhile; a kind named beside the method — a second value that
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

### WAY-64 — Where do invariant and environment fact entries stand, and what identifies one?

Invariant entries stand in one file, `foundations/invariants.md`, and environment fact entries in
one file, `foundations/environment_facts.md`, each under an identifier made of words that no other
entry or withdrawn identifier of those two files or of the part map holds. An identifier either
file held on the commit the branch left the main branch from stays in it, as an entry or as a
withdrawn identifier giving why and naming its successors or `none`, and one it held as a withdrawn
identifier there never names an entry again. Splitting or merging environment fact entries, or
invariant entries held there, gives each entry that comes out of it a new identifier, and any other
change keeps it.

- **Scope:** environment-facts, invariants, part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-02 · derives from WAY-56 ·
  derives from WAY-07
- **Verification:** an agent compares the change with the decision:
  - complies: an invariant drops a clause in place and keeps its identifier (WAY-07); an entry
    taking in a clause of another keeps its identifier, and the other is split; a fact joining
    JSON and JSON Lines splits into two new identifiers, the old withdrawn naming both;
  - violates: an entry drops a clause that reappears as a new entry and keeps its identifier; a
    changed meaning is withdrawn naming `none` and restated under a new identifier.
- **Origin:** none

*Rationale:* words, so a citation says what it leans on; a change of meaning is made in the entry
itself (WAY-07), so only a split or merge changes an identifier, and a withdrawn one shows a
citation where the meaning went.
*Rejected:* a number with a prefix — a mistyped number names another entry; a file per part — an
entry naming several parts or `every` has none; identifiers unique within a file — a reference
would need its element; one half of a split keeping the identifier — nothing sends its reader to
the other half; a fact shown false deleted — an older citation leads nowhere, and the fact can come
back; every identifier ever written kept — one dropped before the main branch was never cited.

### WAY-65 — How does a check cite its invariant, and which files are invariant tests?

A test cites, at the test that checks it, each invariant it checks as `invariant: <identifier>`. A
file is an invariant test of a change when it cites an invariant on the commit the branch left the
main branch from or on the commit being checked.

- **Scope:** invariants, gate, decisions, part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-03 · derives from WAY-17 ·
  derives from WAY-07 · derives from WAY-61
- **Verification:** for where a citation stands, an agent compares the change with the decision:
  - complies: a test running the check of instruction files on the repository cites
    `instruction-file-imports` at its assertion on imports;
  - violates: a test file cites at its top every invariant its tests serve; a test cites an
    invariant with a version beside its identifier.
- **Origin:** none

*Rationale:* a citation stands where the outcome is given (WAY-61); counting either commit keeps a
dropped citation or a deleted test among the invariant tests a request names (WAY-03); an invariant
carries no version for a citation to name (WAY-07).
*Rejected:* one citation per file — one broken test fails all it serves (WAY-61); only files citing
on the commit checked — dropping a citation hides the change from the request.

### WAY-68 — What happens to a check that gives different verdicts on one commit?

A test that cites an invariant and gives both `pass` and `fail` on one commit is fixed as any test
of the product is, and the foundation records no quarantine for it.

- **Scope:** invariants, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-08 · derives from WAY-61 ·
  derives from WAY-63
- **Verification:** an agent compares the change with the decision:
  - complies: a save-load test fails, then passes, on one commit, and a change makes it wait for
    the load signal instead of a fixed pause;
  - violates: a flipping test stands quarantined in the invariants file; a failing test is called
    flaky and run again until it passes, with nothing fixed.
- **Origin:** none

*Rationale:* a test that flips on one commit is a fault of the test, which a change fixes like any
other fault; a green run again hides the fault instead of answering it.
*Rejected:* a quarantine with an end date in the invariants file, set by a change of the foundation
— a mechanism and a date a human moves, kept for a rare case; a count of passes in a row — it hides
the fault.

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

### WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every entry of its kind,
holding a value, or `none` or `TODO` where the template gives it that word: `none` says nothing is
there, `TODO` that something is missing. The main branch holds `TODO` only in an invariant's
*Rests on*, until the facts element has entries. `elements/common/foundation_check.py` reports a
missing field, or a word not given it, as an error.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: an invariant whose author searched the log and found no decision it derives from,
    and which was taken from no source outside the log, reads `Derives from: none`; a decision
    whose source is silent on what it rests on reads
    `Based on: TODO — <what is missing>`;
  - violates: an invariant reads `Derives from: none` though nobody searched the log; a decision
    reads `Based on: none` where its source says nothing of what it rests on.
- **Origin:** none

*Rationale:* an omitted field looks forgotten (WAY-58); an undefined value misleads. An invariant
with no test reads `review` as its method rather than `TODO` (WAY-61). Before facts have entries,
an invariant can expose a needed fact as `TODO` instead of falsely claiming `none`; once they do,
the gap must be resolved.
*Rejected:* a decision for invariants alone — every element would need a copy; a wider scope for
WAY-05 — it answers how a decision entry is written; both words in every field — a word with no
meaning; optional fields left out when empty — intended and forgotten gaps look alike; for facts, a
state field and a ratcheted list — three mechanisms where one serves.

### WAY-72 — In what language is a product's foundation written?

A product's foundation is written in English, whatever language the product shows the people who
use it and whatever language its team speaks.

- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the foundation of a game whose players read Polish, built by a team that speaks
    Polish, is written in English;
  - violates: a product starts its decision log in Polish because its users and its team speak it.
- **Origin:** none

*Rationale:* every template's fields are English, and the words the rules of form keep out (WAY-05,
WAY-60) are English words: an entry in another language passes those rules without a word, so they
look kept while checking nothing. One language also makes the entries of the-way examples for every
product.
*Rejected:* entries in the product's language, each check's words listed per language — a list for
every language, and one without a list checked by nothing; the file's language, asked while it has
no entries — word checks go silent on other languages; a guard reporting other languages unchecked
— recognising a language needs more than the standard library (WAY-38).

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

### WAY-76 — How much does one environment fact entry hold?

An environment fact entry states in one sentence one fact that one edition of one source says, with
one reason to change, and nothing its sentence says is an invariant. Pages of one document published
together in one edition count as one source, and two facts from one edition about different things
stand as two entries.

- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-22
- **Verification:** an agent compares the change with the decision:
  - complies: git's path-pattern rule for attributes files, with its page's two exceptions, is one
    fact, without what `git check-attr` prints; git's ignore rules, from a page of the same edition,
    stand as a second entry;
  - violates: the digest SHA-256 gives and the octets UTF-8 uses stand in one entry; "the
    repository declares Python 3.14" is written as a fact.
- **Origin:** none

*Rationale:* a fact is changed when its source changes, so what changes together stands together:
two sources in one entry would send a new edition of one to every entry resting on the other. An
invariant written as a fact would never be checked on the commit that breaks it.
*Rejected:* git's pattern rule and what `git check-attr` reports in one entry — the second is about
a test's tool, and no commit changes it (WAY-73); both as facts in *Rests on* — the second holds
no condition of the sentence (WAY-73).

### WAY-77 — What shows what an environment fact is true of?

What an environment fact's sentence is true of is shown by the edition its source cites, or, where
the source publishes no editions, by the date it was read, and no field of the entry names it
again. Its sentence holds no word whose meaning moves with the date, such as "latest". A range the
product declares for itself stands in the sentence of an invariant, never in a fact.

- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the standard library's modules are a fact cited from the documentation of CPython
    3.14, while "the repository declares Python 3.14" is an invariant; the fact about JSON Lines
    quotes jsonlines.org, which publishes no versions, with the date it was read;
  - violates: a fact's sentence says what "the latest release" of a tool does; an entry carries a
    field repeating the edition its source cites.
- **Origin:** none

*Rationale:* the address of an edition already names what the fact is true of, and the date read
does so for a source without editions, so a field naming it again is a copy that drifts. "Latest"
would make the sentence change with the date, not the world. The product's range changes with a
commit, so it belongs to an invariant, meeting the fact through *Rests on* (WAY-73).
*Rejected:* a field naming the tools, platforms, editions or measured models the sentence is true
of — it repeats what the source names, for the sake of a check comparing the release it ran on and
of a fingerprint, neither of which a fact keeps (WAY-82, WAY-02); a fact reading the product's
declared version — a sentence about the product in a fact.

### WAY-78 — What is the binding part of an environment fact entry?

The binding part of an environment fact entry is its sentence. The source, its passage and the date
read stay outside it, and no digest of the source's text is kept.

- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a sentence reworded for a new edition changes the binding part; a source re-read on a
    new date that still says the same does not, and the entries naming the fact are left alone;
  - violates: the date read is counted as part of what dependants rely on.
- **Origin:** none

*Rationale:* what relies on a fact relies on its claim, while the source and its date change at
every re-reading; a source that no longer says the same changes the sentence (WAY-82). Text changed
beside the quoted passage passes unseen, an accepted cost.
*Rejected:* the source's text in the binding part — a rebuilt page would change it for every
dependant; a digest of the passage (as a lock file keeps one) — the quoted passage is already the
anchor.

### WAY-80 — What is an environment fact's source?

Every environment fact entry names its source: an edition with its publisher's own address, or a
page without editions with its closest archived copy, giving the place, the passage word for word
and the date read. A state of a host the product's people run, which no page shows and only those
with access to the host can read, has for its source a reading: the command, the host it ran on and
the tool with its version, its output word for word or the lines of it the sentence rests on, and
the date run. The sentence says no more than its source,
and a model's memory, an agent's paraphrase or a text quoting the source is no source. A fact
resting on a whole section of rules quotes the sentence of its source that sets those rules and
names the section by its place alone, where the edition has an address of its own.

- **Scope:** environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the git path patterns fact quotes the sentence handing matching to `.gitignore` rules
    and names that section by place; the mode of a script installed on the product's test server
    cites the `stat` command run there, the host, the tool and its version, its output
    `755 root:root` and the date;
  - violates: the sentence says every line ends in `\n`; the source is the model's recollection of
    a page, a blog post quoting the RFC, or the output of a command the author ran about a tool or a
    format some page documents; a reading names the command and the date but not its output; a fact
    on a pattern syntax quotes its rules one by one, or only the rules the product uses.
- **Origin:** none

*Rationale:* an edition with its own address does not change under the citation, a passage word
for word lets a reader compare it with what the source says now, and the date says when that held;
a recollection or a quoting text carries a paraphrase's drift. A host the product's people run
shows its state on no page, so the output of the command that reads it stands where the passage
stands: one reading, quoted, which a reader with access compares with the host as another compares
a passage with its page; no check reruns it, on a change or by a clock (WAY-82).
*Rejected:* a source named by its work alone — a new edition changes what the citation says; a
summary in place of the passage — the drift this decision exists to stop; an observation naming a
command, its tool and the date it ran without its output — a reader has nothing to compare the host
with; a reading of a host that a check reruns — a check of the fact, which no fact keeps (WAY-82);
a reading where a page documents the same — the page is the source; a whole section of rules
narrowed to those the product uses — a pattern outside them rests on no fact; such a section quoted
rule by rule — a standing `TODO` in the source.

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
a task's return step, or the review of the foundation against the product, a task of the product's
backlog (WAY-24) — and that change then reaches what rests on the fact (WAY-33).
*Rejected:* a method for each fact — a command testing the behaviour or watching the source, run
on every change that enters or rewords the fact and by a clock on the main branch, or the path of
a file a person re-reads with a dated verdict — a program, a run and a record for every fact, whose
failures reach someone only when a person reads them; an announced revision written as a condition
in *Review when* of the decision citing the fact — a date in an entry asks for a look nobody is
sent to make (WAY-24).

### WAY-84 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can
open it, a host's access rule — is an environment fact, its source the place where that state is
shown. A choice of such a setting is a decision only where the product declares it, and that
decision rests on the fact. A fact about the visibility of a repository the product links to names
that one repository.

- **Scope:** environment-facts, decisions
- **Based on:** github-private-repository-response
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a host's access rule is a fact whose source is the page showing it; no decision on
    this repository's visibility is written, as the repository declares none;
  - violates: one fact lists every repository this one links to; a decision "the repository is
    private" is written where the product declares no visibility; an anonymous 404 is taken to
    show that a repository is private.
- **Origin:** none

*Rationale:* such a setting changes with a click and no commit, so it is a fact about the world, and
each repository changes on its own. A decision needs someone who chose; otherwise no commit could
check it.
*Rejected:* a field naming who sets the setting — nothing reads it; a decision and a fact for every
such setting — a decision where nobody chose; a method reading the setting where it lives, or a
dated re-read by the person who sets it — a run and a record for every setting, as WAY-82 rejects
for every fact.

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

### WAY-86 — How does a catalogue of requirements or a binding rule reach a product?

A voluntary catalogue of requirements binds a product only through a decision adopting it that
names the catalogue, its edition, the level or list taken and the area of the product, and a
requirement an invariant takes a condition from is an environment fact. A binding rule — a law,
a contract, a licence — needs no adoption: what it requires is an environment fact, and the
product is held to it until a human settles, in a decision, that the rule does not apply. An agent
that notices a likeness to a requirement nothing has adopted or applied asks a human.

- **Scope:** environment-facts, decisions, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision adopts WCAG, naming its edition, level AA and the screens covered; an
    invariant taking a criterion's condition rests on that requirement's environment fact; the
    attribution an icon licence requires is an environment fact, and the invariant crediting the
    icons' author rests on it;
  - violates: an agent writes an invariant from an ASVS requirement because the code looks like
    it, with no adopting decision; a licence is left out because nobody adopted it; "the licence
    applies to the product's icons" is written as an environment fact.
- **Origin:** none

*Rationale:* a voluntary catalogue binds only because someone chose it; without that choice an
agent would bind the product to whatever it recognised. A law binds whether chosen or not, and
holding the product to it until a human settles otherwise makes silence raise checks rather than
remove them.
*Rejected:* a field naming the kind of source — no reader until a product adopts a catalogue or
takes on a binding rule (WAY-05); a script matching adopted requirements to facts and invariants —
the same, and WAY-73 already withdraws a fact nothing names; "the rule applies" as an environment
fact — a commit removing what the rule covers would make it false (WAY-76).

### WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and
the declared version moves when the version in use leaves bugfix support, never because a newer
version comes out.

- **Scope:** elements-common, relation-model, gate, installation, agent-instructions,
  instruction-files, project-level, task-cycle, repository
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

### WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

A decision's *Based on* quotes every source outside the product that the decision rests on with its
address, the place in it, the passage word for word and the date it was read; once the environment
facts element has entries, it names instead a fact entry, by its identifier alone, for every
citation that, once it stopped being true, would call the decision into question — a finding about
agents or models, the behaviour of a tool the process uses.

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
- **Origin:** none

*Rationale:* only a citation whose change would call the decision into question needs an entry,
from which the search of whoever changes the fact finds the decision (WAY-33); a precedent, a past
event or a finding about people with no lapse date leads to nothing. The address, the passage and
the date let a reader find what the decision rests on and see whether it still says so.
*Rejected:* every citation as an entry — many entries whose change would call no decision into
question, each a second copy of its quote; a fact named with its fingerprint, renewed when the fact
changes — the author's search finds the decision without it (WAY-33); the partners of the part
map's external context as linked facts — a new link with no known consumer.

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
*Rejected:* terms in the shared space of identifiers (WAY-64) — a word a part takes would stay
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
the product's field takes it to mean; an agent that meets such a word in its work — writing an
entry, searching the foundation, in a task's return step — writes its entry, no sweep of every
binding sentence looks for candidates, and a human accepts the meaning (WAY-114).

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "gate", used for the one command that runs all of a product's tests, takes an entry;
    "digest", used only as SHA-256 uses it, takes none; "run", used for running a command and for
    text running across lines, takes none;
  - violates: every noun of the decision log takes an entry; an agent reads every binding sentence
    of the foundation for candidates before it writes an entry.
- **Origin:** none

*Rationale:* a glossary of every relevant word grows without bound, kept by memory, while a word
used as the field uses it needs no entry. A word whose meaning is unclear shows where an agent works
with it.
*Rejected:* every term relevant to the system — no bound; a word defined where it is used, when used
in one place — nearly nothing is; a script counting places — it cannot tell a definition from
another sentence; a sweep of every binding sentence for candidates with each entry written — a
ritual every change pays for; a word's definition moved out of every sentence that says what it is,
into the glossary — a rewrite of sentences the reader already understands; every term with a use
outside the glossary checked at the merge — a check of the glossary's bookkeeping, not of what a
word means.

### WAY-96 — How is a glossary definition written?

A glossary definition is one sentence.

- **Scope:** glossary
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: "The gate is the one command that runs all of a product's tests, the tests of its
    invariants among them.";
  - violates: a definition of two sentences, the second telling what the gate runs.
- **Origin:** none

*Rationale:* a definition of one sentence is read whole beside every use of its word.
*Rejected:* a fixed shape — the present tense with no normative word, "<term> is <genus> that
<difference>" for a noun, no rule about what the word names, a neighbouring term named in the
definition — a test every definition goes through, while the human accepting the entry reads its
meaning; a phrase replacing the term, with no article or full stop — the count would count
something other than sentences; a field naming neighbouring terms — nothing reads it.

### WAY-97 — How does a sentence rely on a glossary term, and what does a change to a definition go through?

A sentence relies on a glossary term by using its word. A glossary entry is edited in place, its
meaning included, and the author of a change to a definition searches, in the same change, the
texts that use the word and rewrites each use whose meaning the new definition moves.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** narrows WAY-02
- **Verification:** an agent compares the change with the decision:
  - complies: the definition of "slice" is reworded, its author searches every file git tracks
    for the word and its forms, and rewrites, in the same change, the two sentences whose meaning
    moves;
  - violates: a definition is reworded and no uses are looked at; a use whose meaning moved is left
    for a later change.
- **Origin:** none

*Rationale:* a sentence relies on a term by its word, so a search for the word finds the sentences
a changed meaning reaches, and the author who changed the meaning knows what moved. The review of
the change, by an agent that did not make it (WAY-10), and the human at the merge see the changed
definition and the rewritten sentences in one diff.
*Rejected:* a version as for invariants and facts — nothing reads it; a review of every use by
another agent, putting the new definition in place of the word — a second reading of what the
author has just searched; a term used on the main branch keeping its meaning, a new meaning taking
a new word — a word stays bound to a meaning the product no longer has; a sentence barred from
spelling out a term's definition — every sentence of every entry read against every definition, by
hand; a term whose definition holds a word an invariant's sentence may not hold named in
the request — the rule on that word stays with the invariant; impact analysis by a model alone —
nobody knows what it missed (WAY-02).

### WAY-99 — How does one word keep one meaning in the foundation?

Where a word carries two meanings in the files git tracks and one of them is a meaning a reader who
knows the product's field would not give it, one of the two is renamed, and the glossary entry of
the word names in *Not* each such meaning it no longer carries, with the term, identifier,
closed-list value or quoted word — holding neither the term nor its forms — that carries it now. A
meaning whose word a human has not yet chosen reads `TODO` in *Not*, which a task branch may hold
and the main branch never does.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a game's "shard" carries a currency and a level's piece, the piece becomes "fragment",
    and *Not* of "shard" names it;
  - violates: "shard (currency)" and "shard (piece)" stand side by side in the foundation; *Not* of
    "shard" names "level shard", a phrase holding the word itself.
- **Origin:** none

*Rationale:* a sentence a test cites carries its words as they stand, so a word read in two meanings
makes it true and false at once. A carrier holding the word itself would keep the homonym under a
new label. The word is the human's choice, accepted at the merge (WAY-114).
*Rejected:* two meanings told apart by an area — the sentence carries no area; a note beside the
word — nobody citing the sentence reads it; renaming two meanings a reader of the field tells apart —
neither is the product's own; a *Not* that always names a word — the author would choose before the
human sees the case.

### WAY-100 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a
decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness
to a method or practice no decision has adopted, it asks a human before treating it as a rule.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a decision adopts only the risk assessment step of an outside process for task
    planning and gives its reason; an agent offers an unadopted technique as a proposal;
  - violates: a skill makes an outside planning ritual mandatory because an agent recognizes it,
    without a decision adopting it.
- **Origin:** none

*Rationale:* borrowing pieces without a conscious choice makes the product's boundaries hard to
explain and change. Naming the chosen piece, its scope and its reason lets later work distinguish
it from a resemblance or a habit.
*Rejected:* importing a whole outside method by default — its unrelated steps become obligations;
treating recognition by an agent as adoption — recognition does not settle fit or scope.

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

### WAY-104 — How does a product write a word of its domain that the glossary of the-way holds?

A word of a product's domain that the glossary of the-way holds at the commit the product pins, or
the last word of a term it holds, in any of its forms, is written in the files of the product's
`foundations/` with a qualifier — a phrase holding the word — and the bare word keeps there the
meaning of the process; the qualified word takes a glossary entry only where WAY-95 gives a word
one, and where the bare word itself has an entry in the glossary of the-way, that entry records no
*Not* for its domain meaning. The product's code, its interface and talk about the product use the
word of the domain unchanged.

- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-226 · narrows WAY-99
- **Verification:** an agent compares the change with the decision:
  - complies: a game's invariants say "castle gate" for the way into a castle, and a factory's say
    "assembly step" for an operation, while their code and interfaces use `Gate` and "Step";
  - violates: a game's invariant says "gate" for the way into a castle or a factory's says "step"
    for an operation; a game's glossary defines "gate" as the way into a castle.
- **Origin:** none

*Rationale:* a word of the process written bare in a product's foundation for something of its
domain carries two meanings for an agent that reads the-way's rules beside the product's, and a
qualifier keeps each word in one meaning where the rules are read; the people who build and use the
product keep the words of its domain, since the rule protects the reading of the foundation alone.
A product cannot edit the glossary of the-way, so the *Not* that WAY-99 asks of the word's entry has
nowhere to stand, and a phrase holding the word, which WAY-99 refuses as a carrier, here keeps the
word of the field recognizable. A term's last word can stand for the process term in short form, so
the qualifier also keeps a domain use of that word apart.
*Rejected:* the bare word of the process in a product's glossary, its meaning of the domain marked
beside it and reported as a warning rather than an error — one word carries two meanings in the
repository, and whoever reads the foundation tells at every use which one it carries; the words of
the process written in a fixed form in the-way, such as in backticks, leaving the plain word free
for the domain — a plain word in a product's sentence may still carry either meaning, so the form
keeps nothing apart, and every entry of the-way is rewritten to it; a word holding neither the word
of the process nor its forms, as WAY-99 asks of a carrier — for words the field uses daily, such as
"part", "entry" or "element", the foundation drifts from the words the product's people and code
use; qualifying a domain word only when it is a whole process term — a short use of a multiword term
can still collide with the domain meaning.

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

### WAY-107 — Where does a product tell the project level where its backlog stands?

A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`,
outside the block the-way's installer owns. A project definition stands in the named project
place; when the place is unnamed, the agent asks the human and offers to record the answer there.

- **Scope:** project-level, installation
- **Based on:** none
- **Relations:** derives from WAY-101
- **Verification:** an agent compares the change with the decision:
  - complies: a product names a directory for projects and a tracker for tasks in its own backlog
    section, and the project definition is written in that directory;
  - violates: the project skill assumes one backlog service for every product, or puts the
    product's paths inside the installer's marked block.
- **Origin:** none

*Rationale:* the product chooses its own backlog place, and a root instruction gives an agent one
place to find it. Keeping the place outside the generated block lets the product change it without
editing the process's installed guidance.
*Rejected:* a fixed backlog location for all products — it would require moving an existing
backlog; asking for the location in every project conversation — the answer would be lost between
sessions.

### WAY-108 — What form does a project definition take?

A project definition is one document with the ordered sections of the project-level template; its
title and content use the language in which the human opened the conversation, while headings,
status values, markers read by the readiness check and projected foundation entries keep their
English forms. A `Status:` line
records whether sections are open, the definition is ready for the gate, or it is approved; every
section contains content, `none` for nothing there, or `TODO` for something missing. An unknown
stays as `TODO` in the section or projected entry that needs it, or as an open question naming
the breakdown or task that resolves it.

- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: project-definition-form. For the language of content and the meaning
  of `none`, an agent compares the change with the decision:
  - complies: a Polish conversation produces Polish section content under fixed English headings,
    and a section with no risks reads `none` only after the human has said there are none;
  - violates: translated headings make the readiness check unable to read the document, or an
    unanswered section silently reads `none`.
- **Origin:** none

*Rationale:* the person deciding the project reads its content in the language of the conversation;
fixed structural words let later work resume and check the document. A written state and
an explicit missing value show where the next conversation begins.
*Rejected:* translating structural words with the content — a checker could not read every
language; inferring progress from prose alone — a fresh agent would reconstruct the state.

### WAY-109 — What may a project definition treat as settled without the human's answer?

The definition's background, success and risks come from the human's answers; material supplied to
the agent anchors questions and is not silently adopted as a settlement. Every success signal
states what would falsify it.

- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a concept's claim of success enters the agent's question, and the definition records
    the person's answer with a condition that would show it false;
  - violates: a concept's assumption becomes a risk without asking, or a success signal names no
    circumstance that would show it false.
- **Origin:** none

*Rationale:* a fluent draft makes an agent's inference look like the human's decision. A condition
that could disprove success gives later work a way to judge it.
*Rejected:* filling gaps from plausible material — later tasks would inherit invented choices.

### WAY-110 — When does a deadline enter a project definition?

A deadline enters the definition only when the human names one imposed from outside, in the
human's own words and with how firmly it binds. The agent neither asks for a deadline nor derives
one from material, and does not argue the project's scope or cost from it.

- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: the human names an externally imposed launch date and says how firm it is, so the
    definition records that answer in their words;
  - violates: the agent asks for a deadline as a routine field, infers one from a concept's date,
    or uses a stated date to press for a smaller scope.
- **Origin:** none

*Rationale:* a date imposed by the surroundings can constrain the work, while a date invented for
planning makes the constraint appear to come from the human.
*Rejected:* a routine deadline question — it creates pressure without an external constraint;
deriving a deadline from background material — it mistakes context for a settlement.

### WAY-111 — What does the project level read in the current foundation?

Before drafting, the agent selects and reads the current foundation under WAY-150, identifying
touched parts from the proposed project's responsibilities, behaviour, flows and surfaces. It
brings a touched part, a decision the project may change, an invariant it may break or a boundary
it crosses to the human as material and asks
whether the project changes an existing decision or fits it.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-150
- **Verification:** an agent compares the work with the decision:
  - complies: before any diff exists, the agent maps the idea to affected responsibilities and
    surfaces, reads every applicable Scope decision and expands to an unlinked invariant, then
    shows the touched decision and boundary and asks whether the project changes or fits it;
  - violates: the agent treats the absence of a diff as no touched parts, or reads only decisions
    already linked to the idea and misses an unlinked invariant or a boundary in the map.
- **Origin:** none

*Rationale:* the current foundation gives a project its starting constraints before its design
has files to point from. Reading from the proposed behaviour finds those constraints while leaving
room to follow an unexpected conflict; showing the conflict lets the human decide its meaning.
*Rejected:* reading the whole foundation for every idea — context grows with unrelated rules;
reading only entries with a matching scope or known link — an unlinked conflict stays hidden;
waiting for changed files to choose context — the project is drafted before those files exist.

### WAY-112 — How does an agent develop and resume a project definition?

The agent confirms its understanding of the goal with the human before the definition's first
write, then creates the initial sketch in the product's project place without a separate request
and gives its full path. It asks about the largest gaps, challenges a frame only from an anchor in
the human's words or material, reads what product files can answer, and treats "I do not know" on
assessment as an open question with its resolver but on a choice as a reason to offer a
recommendation with costs. It writes each answer and the updated `Status:` line before the next
question; work resumes from that line and, while entries are being found, from the candidate table.

- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: after the goal is confirmed, an agent writes a sketch, then records each answer and
    its new status before continuing; a later agent resumes from the recorded open section;
  - violates: an agent writes a complete definition from the source before checking the goal, or
    asks another question while the prior answer exists only in conversation.
- **Origin:** none

*Rationale:* the first confirmation prevents a polished document for the wrong goal; saving each
answer makes the document a reliable place to resume. Source-anchored challenges can change an
assumption without asking the human to defend an invented objection.
*Rejected:* waiting for a second permission after confirming the goal — it adds a stop without a
new decision; writing only at the end — an interruption loses settled answers; challenging every
line by a fixed script — questions without a real anchor consume the person's attention.

### WAY-113 — How does an agent of the-way ask a human decision?

An agent asks in plain conversation text: a decision question gives the available ways, the cost
of each and a recommendation, while a question of assessment stays open; neither opens a separate
question panel. After a human choice enters an entry's binding part, the agent asks one question
against that choice anchored in the human's words or supplied material, unless the choice ends
with the work, or the human took one of the ways offered and the decision question named, anchored
in the material, the weak point of that way.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the exchange with the decision:
  - complies: a choice is presented in text with the costs of both ways and a recommendation,
    followed by a source-anchored question against the answer when it enters a binding entry,
    unless the person took a way offered whose weak point the question named;
  - violates: the choice appears only in a separate option panel, an agent asks a generic
    challenge unrelated to the person's answer, or an agent asks against a way offered whose weak
    point the question already named and the person took as offered.
- **Origin:** none

*Rationale:* the person sees the trade-off where they make the choice. A challenge grounded in
their own material can expose a contradiction without inventing one. Where the question already
named the weak point of a way and the person took that way as offered, a challenge asks again what
was weighed at the choice; it is kept for an answer in the person's own words, which the question
did not weigh.
*Rejected:* a panel of options separate from the conversation — its context is detached from the
material; a challenge to every choice, including one that ends with the work — repeated questions
would add no later protection; a challenge to every choice entering a binding entry, even a way
taken as offered whose weak point the question named — it asks again what the choice already
weighed.

### WAY-114 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry, shown as one sentence in the human's language with
the entry beside it, while its wording is the agent's: an agent writes the entry and the human accepts
it at the merge of the change that holds it, or, for a projected entry, at the readiness gate. Before
that, a question goes to the human only where the agent has no recommendation or the entry would
change the meaning of an approved decision; a translation never enters the foundation.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: the request lists each entry it writes with one sentence of its meaning in Polish, and
    the human reads the entries before merging;
  - violates: an agent asks the human to confirm a choice it already recommends; a translation is
    written into the foundation; an entry changes the meaning of an approved decision without a
    question.
- **Origin:** none

*Rationale:* the human judges what an entry settles; its wording rarely changes that, and the human
who merges reads what the change holds and answers for it.
*Rejected:* acceptance of the whole wording before an entry is written — attention goes to wording
while the meaning rarely moves, and each acceptance costs a round; storing a translation in the
foundation — two binding wordings could drift apart.

### WAY-115 — How are foundation entries found in a project's source?

The agent reads the project's sources in full and selects and reads the product's foundation under
WAY-150, then shows the human a complete candidate table with each proposed settlement, its kind,
its source and the concrete
choice or action the next reader would otherwise have to guess; a row without such a consequence
is shown as rejected. The human accepts or rejects rows before they are handed to the skills of
their kinds, and each accepted row is recorded as it is worked through. The definition keeps the
working table until the step ends, then replaces it with a `Candidates:` line recording how many
rows were shown and accepted.

- **Scope:** elements-common, project-level
- **Based on:** none
- **Relations:** derives from WAY-150
- **Verification:** an agent compares the work with the decision:
  - complies: the human sees every column of the candidate table, rejects an exclusion whose
    absence would make no task guess, and the completed definition carries the candidates line;
  - violates: the conversation hides the source and the next reader's guess while a file holds
    them, or entries are written before the human has cut the table.
- **Origin:** none

*Rationale:* the source distinguishes a human settlement from material offered for consideration;
the concrete guess filters noise before it becomes a rule. A table with row states lets work
resume, and a final line shows that the search occurred even when it yields no entry.
*Rejected:* turning every scope line into a foundation entry — exclusions that nobody would
misread become permanent noise; showing a shortened table — the human cannot judge provenance or
the reason a candidate matters.

### WAY-116 — Which foundation entries may a project definition project?

A project definition projects decisions, invariants and glossary terms that the human can settle
before the breakdown, and environment facts only where a projected decision or invariant rests on
them. Of the part map it projects a changed existing part only when every field is already known;
a new part or surface remains an open question for the breakdown.

- **Scope:** project-level, decisions, invariants, glossary, environment-facts, part-map
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the definition with the decision:
  - complies: the definition holds a proposed access rule, a related glossary term and a
    changed known part, while a future new part is an open question resolved in the breakdown;
  - violates: it invents files for a part that has not been designed, or records a fact with no
    projected entry depending on it.
- **Origin:** none

*Rationale:* a project can settle rules of a future product before it has tasks, but some map
fields exist only once code and files do. Restricting facts to what a proposed rule rests on
prevents a speculative inventory of the surrounding world.
*Rejected:* decisions alone at the project level — later work would still have to infer known
invariants and terms; projecting new parts with guessed files or missing fields — the map would
look complete while naming a structure that does not exist.

### WAY-117 — How does a foundation entry stand in a project definition before it is written?

The skill of each entry's kind writes its whole proposal under the definition's `Projected
foundation changes`, in that kind's subsection with the template's projected heading and one
sentence of its meaning, without writing the product's foundation or running the foundation check,
and without searching the whole foundation for the entry: the readiness gate searches it once for
the whole definition (WAY-118). A new projected decision uses `(new)` without a number or prefix,
while a change of a current decision and other kinds use the identifiers their templates give;
an entry following from it remains projected or becomes an open question when its
fields await the code.

- **Scope:** project-level, elements-common, decisions, invariants, glossary, environment-facts,
  part-map
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: a new decision carries `(new)`, a changed decision carries its number, and an
    invariant's method reads `review` until a task writes its test;
  - violates: a projected proposal is written directly into the foundation, a changed decision
    loses its identifier in the definition, or the skill searches the whole foundation for one
    projected entry.
- **Origin:** none

*Rationale:* the project's definition keeps a future rule visible without claiming it already
holds. Code-dependent evidence can be completed when the task writes the entry. One search at the
gate reads every projected entry once its wording is settled.
*Rejected:* filling every field with an invented future method or file — it makes the proposal
look checked before the product exists; leaving the human's reasoning to later tasks — they
cannot recover what was considered during definition; a search of the whole foundation for each
projected entry as it is written — the gate repeats it for the whole definition.

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

### WAY-121 — Where does a project settle the technology it needs?

Before a project definition goes through its readiness gate, a step of its own lists the
technology and architecture choices the project needs — such as a language, a framework, a store
of data or a place to run — and, for each, either names the decision of the foundation that
already holds it or settles it as a projected decision of the definition; a project whose every
choice the foundation holds thus settles nothing. A choice belongs on the list when settling it
later could change how the work is cut into tasks, or when it adds something the product has to
run, pay for or back up; a choice one task can make and change alone stays with that task. As an
exception to that rule, where the project brings behaviour a user sees in the running product, the
step looks at three matters of an agent's way to the running product — its logs, its interface and
its development data — and lists as a choice of its own each matter that no decision of the
foundation settles for that behaviour, even where its answer adds nothing to run, pay for or back
up, and even where the product has none of what the matter names, whose answer then says what an
agent uses in its place.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-116 · derives from
  WAY-100
- **Verification:** invariants: project-technology-record. For what the step lists and settles, an
  agent compares the work with the decision:
  - complies: a project that adds an account server lists its store of data and its way of
    logging in, and the definition projects a decision on each; a project that changes only how a
    screen looks, in a product whose foundation already says how an agent reaches its screens,
    records that the foundation holds every choice it needs; the first project of a game played in
    a browser lists the game's logs, its interface and its development data, each as a choice of
    its own, and projects a decision on each although reading the server's output and opening the
    game on a local address add nothing to run; a later project of that game, whose new screens
    an agent reaches as those decisions say, lists none of the three; a command-line tool that
    keeps no data lists its development data, answered by sample input files kept with its code;
  - violates: the first task of the breakdown chooses the database; a definition reaches the gate
    with a store of data in its scope and no choice of it projected or found in the foundation; a
    project that brings a product's first screen leaves out how an agent operates it because a
    browser on a local address adds nothing to run; the logs, the interface and the development
    data stand on the list as one choice; a product that keeps no data leaves its development data
    off the list for that reason.
- **Origin:** none

*Rationale:* whether a technology choice changes how the work is cut into tasks cannot be judged
by someone who does not know the technologies, so the choice is settled before the cut; a step of
its own keeps the comparison of technologies out of the talk about the project's goal and scope,
while its agent still knows the whole project. Settled before the gate, the choices are approved
with the rest of the definition, and an exit for a project whose choices the foundation already
holds keeps the step from being an empty run. A task cycle checks behaviour a user sees in the
running product as well, and an agent with no way to the running product either leaves that check
undone or improvises its access in the middle of the cycle. The commonest answers — logs read from
the output of the product's container, the product opened in a browser on a local address — add
nothing to run, pay for or back up and change no cut of the work, so the rule of belonging alone
would never list them; the exception lists each matter as a choice of its own, weighed apart, and
only where no decision already answers it, so the first project of a product settles each in a
short decision and later projects find it in the foundation. A product with no screen or no stored
data still needs the answer that says what an agent uses instead. The step takes from the lesson
"Towards Autonomous Product Development" the question of how an agent sees the running product —
through its logs, its interface and its development data — and leaves out the lesson's hard limit
that keeps an agent away from the production database and from root access.
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
as a decision of the foundation; the logs, the interface and the development data as one choice —
it binds independent choices together, and a later change to one reopens them all; one heading the
step splits into as many choices as the product needs — whether a matter is left out would rest on
the agent's judgment alone; the matters on the list the deployment skill of a product covers
(WAY-139) — only a task that deploys the product checks that list, so a product run on a local
machine alone would leave an agent with no way to it.

### WAY-122 — How are the options of a technology choice found and checked before a human sees them?

The options of each technology choice a project needs come from research of that choice against
the project definition, rather than from a fixed list of bundled stacks, and the research of every
choice that depends on no unsettled choice starts once the list of choices is confirmed, each in a
report of its own. An option the project's code is written in or against — a language, a
framework, a library, a store of data — is weighed by whether its documentation shows that it uses
explicit types, follows conventions of layout and naming and has current, versioned documentation,
and whether a public record of its use, such as a package registry or a survey, shows it widely
used within its language family; for a store of data, its types are those it declares for what it
stores, and its family is that of its query language. An option lacking one of these properties is
offered with what each lack means for the product, which the decision records if the human chooses
it; an option with no documentation or with a project no longer maintained is left out with that
reason, unless the human named it or the definition holds it as a constraint, and then it is offered
with that reason as such a lack; and every option is offered only after a critique that refutes
every claimed difference between the options which no source supports.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-120
- **Verification:** an agent compares the work with the decision:
  - complies: research for a store of data compares a file kept beside the application with a
    database server, each typed and documented, and the critique strikes a claimed difference in
    speed that no source gives; a built-in module with no record of wide use stays in the
    comparison beside a widely used library, its lack said as what it means for the product;
  - violates: the step offers a framework, a database and a host as one bundle from a fixed list;
    a comparison reaches the human with a difference no source supports; an option with
    documentation and a maintained project disappears from the comparison because it lacks one of
    the properties; an option the human names disappears from the comparison; the research of a
    choice that depends on no unsettled choice waits for another choice to be settled.
- **Origin:** none

*Rationale:* a fixed list of stacks, each bundling a framework, a store of data and a place to run,
settles several choices at once and without the project, so a bundle can run against choices the
project already holds and leave others unsettled; research for each choice starts from what the
project needs. Research of independent choices run side by side and kept in reports lets the
conversation settle one choice while the next is researched, and nothing found is lost to a long
conversation. An agent can read each of the properties off an option's documentation or its public
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

The step that settles a project's technology shows the options of each choice by their
consequences for the product — what it costs, where it runs, what keeping it running takes and
what changing it later costs — and the human chooses between those consequences. A difference with
no consequence for the product decides nothing, and where no difference with a consequence
remains, the step recommends the simplest and cheapest option. The choices whose research started
together reach the human together, in one table, once every one of their comparisons has passed
the critique, each with its recommendation and the weak point of the option recommended; in the
area of the choices this step settles, this decision prevails over WAY-114, under which a question
goes to the human only where the agent has no recommendation.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-113 · narrows WAY-114
- **Verification:** an agent compares the work with the decision:
  - complies: two stores of data are shown as "a file kept with the application and copied with
    it for a backup" against "a server to keep running in the container, with backups of its
    own", and the human picks one;
  - violates: the options are shown as lists of technical features; two options with no
    difference in consequences are offered as a matter of taste instead of the simpler one being
    recommended; two choices whose research started together reach the human in separate
    tables.
- **Origin:** none

*Rationale:* a human who cannot assess the technology can still weigh what an option costs and
where it fails, so a technical difference reaches the decision only through a consequence. Where
options differ in nothing the product feels, a choice between them is blind, and the simplest and
cheapest keeps cost and upkeep lowest. Independent choices shown together are settled in one
answer, and the weak point stated with the recommendation lets the choice stand without a question
asked after it (WAY-113).
*Rejected:* technical differences shown as they stand — the human cannot weigh them; falling back
on a default bundle when the human cannot judge — with no fixed list (WAY-122) there is no default;
the agent choosing alone — the choice binds the product, and a human approves decisions (WAY-14);
every choice shown on its own, followed by a question against it — the human waits between choices,
and each choice costs two exchanges; each comparison shown as soon as its critique passes — the
tables come one choice at a time.

### WAY-124 — When is a task ready for its cycle?

A task document records whether the task is independent, belongs to an item of a project's plan,
or uses an approved project definition as a source without belonging to its plan; it carries the
task's scope, temporary exclusions, relevant current foundation decisions, any approved
projected wording it uses and the settlements its refinement keeps for the foundation (WAY-134).
It is ready when the human has seen and accepted its complete document, its required outcome is
stated, every known question blocking that outcome is answered, the human has accepted or
rejected every candidate settlement its refinement found, every human action it places before
the cycle is done (WAY-140), and implementation questions carried into the cycle are named. A
project member also matches its plan item's scope, dependencies and assigned entries; any task
using an approved definition checks that its approval still holds and names each projected
entry, or the part of it, that its code makes true, while source-only use takes no other
assignment or dependency from the plan.

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
    candidate settlements likewise waits for acceptance of its complete document;
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
for coordination spends attention without doing that work. A fragment that only one step or variant
needs stands beside the method (WAY-256); read at the start, it would stay in play through the
other steps and in the variants the agent does not take, so its place would spare the agent
nothing. The gain is largest in the variants an agent does not take, since a file read at an earlier
step stays in context. An agent may pass by the moment its step names a file; the judgment that
moves a fragment beside a skill asks whether an agent recognises that moment (WAY-257).
*Rejected:* methods of an outside plugin, with or without a required version — the cycle overrides
their steps, keeps their log beside its record, and a product meets whichever version its harness
has installed; every method written into the one cycle skill — the orchestrator would read every
stage's method; reading every method in the orchestrator too — it repeats context the agent
applying it already holds; each agent reading its method and every file the method names at the
start — a fragment moved beside a stage's method would still be read at once, so the move would
change nothing for the agent.

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

- **Scope:** project-level, task-cycle, decisions, invariants, glossary, environment-facts,
  part-map
- **Based on:** none
- **Relations:** derives from WAY-01 · derives from WAY-11 · derives from
  WAY-114 · derives from WAY-118 · narrows WAY-106
- **Verification:** an agent compares the change with the decision:
  - complies: a source-only task whose code adds the store a projected decision chooses writes
    that decision whole in its foundation step, and the task the plan assigns later finds it and
    writes nothing; a task whose code makes one of a projected decision's two sentences true writes
    that sentence and lists its meaning in the request;
    a plan member whose code would make another item's entry true returns to the plan first;
  - violates: the return step writes a new decision for a rule a projected entry of the
    task's source states; a shortened projected entry is written as the gate approved it, its
    meaning left out of the request;
    the code a late-found projected invariant covers is set aside and rewritten.
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
it to the prefixed skill. A fragment that only one step or variant of a skill needs stands beside
the skill so that it leaves the text read at the other steps (WAY-256); an entry point that had
every file a skill names read at the start would bring each such fragment back into play at once.
*Rejected:* a mode of the installer without a pin writing the same entry points into the-way — its
generated files would belong to `installation`, outside that part's directory, and its trust
boundary would grow; entry points written per checkout and ignored by git — a fresh worktree or
cloud session has none until someone writes them; global links, one per worktree, or links tracked
by git — a global link reads one checkout whatever branch the session works on, and tracked links
need a git setting and extra rights on Windows; names without the prefix — which skill a session
gets would rest on how Claude Code and Codex settle two skills of one name; an entry point that has
the skill and every file it names read at the start — the fragments placed beside a skill for one
step would load with the skill.

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
the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256 instead.

- **Scope:** instruction-files, agent-instructions
- **Based on:** context-file-effect · claude-code-path-rules ·
  codex-agents-md
- **Relations:** derives from WAY-100
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
- **Relations:** derives from WAY-100
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
- **Relations:** derives from WAY-100
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
- **Relations:** derives from WAY-100
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
- **Relations:** derives from WAY-100
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
- **Relations:** derives from WAY-100
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

### WAY-134 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task
document and the conversation that refined it, in the form WAY-115 gives with each settlement in
the human's words, and the task document keeps the rows the human accepts; the agent refining the
task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and
WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a
candidate decision or invariant rests on, and a settlement that a current entry the refinement
reads for the parts the task touches, or a projected entry the task carries, already states is no
candidate. The task's cycle writes each kept row whole into the foundation in its foundation step,
or in its return step where the foundation step missed it, one that no code makes true included,
keeping its meaning and choosing its wording; where that meaning cannot hold, or the entry needs a
value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft
request rather than write another entry, and otherwise the human accepts the entry's meaning at the
merge (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33)
finds already stated becomes no second entry, the cycle tying the row to that entry and naming
both in the request.

- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary,
  environment-facts
- **Based on:** none
- **Relations:** derives from WAY-115 · derives from WAY-33 · narrows WAY-114
- **Verification:** an agent compares the task document, or the cycle, with the decision:
  - complies: a task whose human settled in refinement that an exported record keeps its owner
    carries that row, and its cycle writes a decision with that meaning in the same change as its
    code and names it in the request; a task whose refinement found nothing carries the counting
    line with none below it; in an orchestrated round the project orchestrator shows the candidate
    table and required challenge questions while the refiner records the human's answers; the
    cycle's search finds a decision of an untouched part that already states a kept row, and the
    request names the row with that decision instead of a new one;
  - violates: the cycle writes the entry with another meaning, or leaves out a kept settlement
    because no code makes it true; the refinement writes whole entries into the task document; a
    kept row repeats a rule a current decision the refinement read states; the cycle writes a
    second entry for a rule its search found already stated; an orchestrated refiner asks the human
    directly about candidates or substitutes its own acceptance.
- **Origin:** none

*Rationale:* a settlement the human makes while a task is refined binds after the merge as much as
one a project settles, yet with no place in the task document it reaches the cycle as an answer to
a question, where it reads as one more choice the cycle may make otherwise. A row in the human's
words carries the meaning into the cycle without a second point of acceptance: the wording stays
the agent's, as for every entry a cycle writes, and the human judges the meaning at the merge. A
table read from the whole document finds a settlement said in passing, and its column of what the
cycle would guess drops one no reader would miss. Refinement compares the candidates with the
entries it reads for the task's parts; what no link joins, the one search of the whole foundation
finds once the cycle has settled the entry (WAY-33), and a rule already stated keeps one entry. A
meaning that cannot hold goes back to the human before the request because the human settled it,
and finding the change only at the merge would leave code already written for another meaning. In
an orchestrated round a single human-facing agent keeps these choices together without making the
refiner a second channel to the human.
*Rejected:* whole entries written while the task is refined, as a project definition projects
them — a task has no gate to approve their wording, and refining a task would weigh as much as
defining a project; noting a settlement only when the human states one — a settlement said in
passing in the request is missed, and the agent alone decides what binds; letting the cycle change
or drop a settlement and show the difference in the request — the human's settlement could be
reversed and seen only once the code is written; decisions and invariants alone — a word whose
meaning the human settled would be defined by the cycle; a search of the whole foundation when a
task's candidates are named — it repeats the cycle's search on wording not yet settled.

### WAY-135 — When does a task's cycle write a spec?

A task's cycle writes a spec, reviewed by an agent other than its author, before implementation
and any plan where the task leaves an open design choice and nowhere else, and an invariant whose
sentence a row of the task's *Settlements to record* or a projected entry of its sources gives
leaves none. An agent that meets an open design choice while it makes the change returns a report
that holds no code, the attempt is discarded with the foundation entries the cycle wrote for it,
and a fresh agent given the report writes the spec, after whose review the orchestrator chooses
again whether one author can hold the change or it needs a plan, using the same judgment as before
implementation (WAY-136).

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-13 · derives from WAY-69 · derives from
  WAY-126 · derives from WAY-134
- **Verification:** an agent compares a cycle with the decision:
  - complies: a task whose rows of *Settlements to record* carry its two decisions and its invariant
    proceeds without a spec, and the review reads the invariant's test against its sentence; a
    task whose part-map change follows from the file it adds, with no other way
    open, proceeds without a spec; an agent that finds the task needs a decision the task does not
    carry returns a report without code, the branch goes back to its base — to the commit that
    moved the pin where the task moved it — and a fresh agent writes the spec; a reviewed spec is
    followed by one author without a plan when the change still fits one agent, or by a new plan
    when it needs division;
  - violates: a spec is written for a task whose document carries every entry it writes and that
    leaves no other way open; an agent designs a decision the task does not carry and goes on with
    the code; a spec is written around the code of an attempt that met an open design choice;
    a plan is required merely because a spec was written.
- **Origin:** none

*Rationale:* a spec and its review earn their cost where an agent designs a foundation entry itself,
whose agreement with the current entries has to be checked before code is written on it; where the
task's document carries every entry, a spec restates what the human already settled and its review
finds nothing the reviews of the code would miss. An invariant the document carries is kept from
fitting the code by the review that reads its test against its sentence (WAY-69), not by a spec. A
choice found while the code is made cannot be weighed apart from that code, so the attempt goes,
its slices already made among them, since the spec may change what they made, and a fresh agent
designs from the task and the report. Settling the design does not itself create work to
divide; the extent of the settled change decides whether a plan earns its cost.
*Rejected:* a spec for every task that changes the foundation — almost every task changes it, and
the spec would restate entries the human settled at a large share of the cycle's cost; no spec for
any task — an entry an agent designs would reach the code unchecked against the current entries;
an attempt that met an open design choice kept and completed — a spec would be written around
partial code; the agent of that attempt writing the spec — the spec would carry the shape of the
abandoned code; a spec for every task that writes an invariant — the review already reads its
test against its sentence.

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
slices — the pin moved before the route keeps the installer's output out of every plan.

### WAY-137 — What decides between places to run that the simplest and cheapest option leaves tied?

Where the options of a place to run differ in no consequence for the product and more than one of
them is the simplest and cheapest, the step that settles a project's technology recommends, of
those, the one an agent works with best: operated from a terminal, deployed by a script and
documented in pages an agent can read. For a place to run, how well an agent works with an option
decides nothing else: it leaves no option out of the comparison and is weighed against no
consequence for the product.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100 · narrows WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: two hosts that cost the same and take the same upkeep remain after the simplest and
    cheapest rule, and the one with a command-line tool and a deployment script is recommended; a
    host with no command-line tool stays in the comparison and is recommended where it costs less
    than the others;
  - violates: a host whose deployment cannot be scripted is left out of the comparison for that
    reason; a host is recommended over a cheaper one because an agent can operate it from a
    terminal; the table of consequences scores how well an agent works with each host beside its
    cost.
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

The step that settles a project's technology tests the option it recommends for each choice it
settles, one a constraint of the definition settles included, with a devil's advocate, a pre-mortem
and a search for unknown unknowns; it tests no choice a decision of the foundation holds, and no
decision already written is tested afterwards. The risks these tests give are hypotheses with no
source, not differences claimed between options, so the critique of the comparison does not strike
them, and they stand in the table beside the option recommended before the human chooses. The human
who chooses that option takes its risks, and each risk taken reaches the decision of that choice in
its *Rationale*, beside the lacks of the option chosen, marked as a hypothesis.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-122 · derives from
  WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: a project settles its store of data and its place to run, the table shows beside each
    option recommended the risks the three tests gave, each marked as a hypothesis, and the human
    who takes the recommended host finds those risks in the *Rationale* of its decision beside its
    lacks; a framework the definition names as a constraint is tested; a language a decision of the
    foundation holds is not;
  - violates: the critique strikes a risk from the table for want of a source; the risks are shown
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
recommended, the one the human most often takes, and only where this project chooses: a choice a
decision already holds has been made, and testing it again would reopen it with no reason in the
project.
*Rejected:* tests on every option of a choice — their cost grows with options the human mostly does
not take; the risks shown after the choice — the human takes them unseen; the risks put through the
critique as claims — with no source, every one would be struck; the risks in *Based on* — it names
facts with sources, and a risk read there passes for one; an entry of its own for each risk —
assumptions as a kind of entry escape checking (WAY-04); tests on choices decisions of the
foundation hold — they reopen what was settled.

### WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?

The-way holds no skill of a product, only the list of what a product's deployment skill covers: a
preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of
steps and what happens to the data; what the agent does and what the human does; and how to read the
logs. When a task's outcome deploys the product or changes how or where it runs, the-way's skill
`refine-task` checks, while it refines the task, that the product has a deployment skill covering
every item of the list, and where it has none or an item is missing, the task gains an item of its
To do for that work or the human splits that work into a task of its own.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** an agent compares the work with the decision:
  - complies: refining a task that moves the product to another host finds that the product's
    deployment skill says nothing of rollback, and the task gains an item of its To do that adds
    it; a task that sets up the product's first deployment finds no deployment skill, and the human
    splits writing one into a task of its own; a task that changes the text of a page is refined
    without the check;
  - violates: the-way carries a deployment skill for one kind of host; a task that changes where
    the product runs reaches its cycle with a deployment skill that does not say where the secrets
    lie, and with no item or task for it; the list stands only in a template, and the decision
    points to it.
- **Origin:** none

*Rationale:* how a product is deployed and operated depends on where and how it runs, which differs
from product to product, so a skill of the-way would fit none of them; what such a skill has to
answer is the same for every product, and a list in a binding sentence gives the refinement a thing
to check. Knowledge of operating a product written in a document no step reads goes unread however
concrete it is, while a skill of the product reaches the agent when it prepares a deployment. The
check comes when a task first needs that knowledge, so the first task that deploys a product grows
by its deployment skill, unless the human splits that work off.
*Rejected:* a deployment skill carried by the-way — what to run and where differs for every
product; a document of operations kept beside the product — no step reads it, so it goes stale
unread; the list in a template alone — nothing binds the refinement to check it.

### WAY-140 — How does a task change something outside the product's repository?

A task's effect outside the product's repository — on a server, in DNS, on keys or on an external
account — is made only by a human, through a human action the task document names and places before
the cycle or in it, while reading outside the repository stays with the agent and the cycle's record
of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect
of the task. For the human actions placed in the cycle, the cycle does what the repository allows
and opens a blocked draft request listing them, and the human performs them at the request; a human
action the cycle finds that the task document does not name joins that list for the human to place,
and the request opens as a blocked draft listing it even where the document places no human action
in the cycle. The human places each human action the task document names while the task is refined,
on the agent's proposal: before the cycle when the cycle's code needs its effect, such as an
account, a key or a database, and in the cycle when it uses code the cycle writes, such as a
deployment or a DNS record pointing to a new address.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100 · derives from WAY-107 · derives from
  WAY-227
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
before any task is planned, and leaves out its milestones, its estimates and its interview on the
order of work.
*Rejected:* the realizing and the writing tasks as two columns of the table of tasks — a cell grows
to many long headings and needs keys made up for them; each task described again in a section of
its own beside an index table and a table for a tracker — three copies of one task drift apart; the
plan inside the definition — every move of a task would change approved sections and send the
definition through its gate (WAY-118); a stage of the project opened and closed inside the plan —
the project already opens with its definition and ends once each of its tasks has a final state;
the external
deadline repeated in the plan — the definition holds it (WAY-110); the columns named in this
decision — each change of a column would take a change of the decision.

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
enabling work the rule that such work names what it opens the way for.
*Rejected:* tasks cut by layers of the product — nothing can be checked until the last layer lands;
preparatory work no task depends on — it grows into a layer of its own; a field of the preparatory
task naming the task it opens the way for — it repeats a dependency the plan already holds; the word
slice for a task of the plan — the word already names a piece of a task's change.

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
order that follows from it, and leaves out its field of work that can run alongside. The task
order WAY-106 gives the plan is this order of cycle starts. Refinement
can settle a dependent task before its prerequisites are delivered; only a question needing their
result earns a wait.
*Rejected:* a field naming the tasks a task can be worked on beside — a copy of the dependencies
that grows past reading; the order tilted by a goal the human picks in an interview before the plan
— the definition already states the goal and its risks, and the human corrects the finished plan.

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
  WAY-126
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
it, and quoted with its place it can be checked against its source.
*Rejected:* a move taken through the gate again — the definition would be approved again for a
change of route alone; a flag marking a task blocked by its unknowns, beside a list of deferred
work — the states of a task already hold waiting for the human, and the list repeats the
definition's exclusions; a question moved without a word — a reader takes it for the definition's
own placement; only the human answering a question the breakdown resolves — the human would restate
what the foundation already holds.

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
before it is handed on, split between a script and a reader who did not write the plan.
*Rejected:* the author checking its own plan against the rules before writing it — the same agent
applies and judges them; checks of a plan's form across several copies of each task — a plan holding
each task once has no copies to compare; an agent checking what a script decides — it costs more
and sometimes misses.

### WAY-147 — How is a task of a project plan named, and what does its cycle take from the name?

A project plan gives each of its tasks a name of lower-case words joined by hyphens, which no other
task of the plan holds and which stays with the task while the plan changes. A task of the plan
enters its cycle under that name, and the cycle names its record by it.

- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100
- **Verification:** invariants: project-plan-form. For the cycle, an agent compares the cycle with
  the decision:
  - complies: the task `forest-on-hex-grid` of a plan keeps its cycle record under
    `docs/task-cycles/forest-on-hex-grid/`;
  - violates: the cycle of a task of a plan names its record by a name it makes up; a task's name
    changes when its goal is reworded; a plan carries a second table of its tasks with titles for a
    tracker.
- **Origin:** none

*Rationale:* a task's cycle record and its entry in the product's backlog meet its row in the plan
through its name, so a name that changes leads a reader to the wrong work; words, because a number
that keeps the plan's own cells short says nothing in a record read apart from the plan. The rule
takes from the practice of a roadmap the stable name each of its items carries into later work.
Where the product keeps its backlog is its own choice (WAY-107), and a task's entry there links its
document, so the plan needs no table of its tasks written for a tracker.
*Rejected:* the cycle naming its record when it starts — the plan and the record name one task
differently; the plan's number as the name — it says nothing where it is read; a table of the
plan's tasks with titles for a tracker — a second copy of the tasks, which the product's backlog
already holds.

### WAY-148 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports
directory, while its messages carry routing, the stage's status, commits, a one-line check result
naming what failed or did not run, and the report's path, while the agent's questions, concerns and
each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the
orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files:
it may carry a section of the plan, spec or task copied word for word, never restated in other
words, with its file named as its address, so that a slice's executor gets its section of the plan
and works without opening the plan; and since only the orchestrator reads the cycle record, an
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
- **Relations:** derives from WAY-125
- **Verification:** an agent compares the stage handoff, return, report and orchestrator's ruling
  with the decision:
  - complies: a short return names its report, commit range and failed or unchecked checks, and
    the record permits resumption from files; a slice's handoff holds its section of the plan
    copied word for word and names the plan's path; an agent's questions stand in its report and
    its return says `questions`; the orchestrator reads the evidence of an unresolved question
    before deciding it; a missing report is repaired before the next dependent dispatch; routine
    progression does not load the stage agent's sources and full report again;
  - violates: a full report exists only in conversation, a short return conceals a failed check,
    dependent work proceeds on a missing report or mismatched commit range, or a question is
    settled from the short return alone; a handoff restates a requirement or value of the task,
    spec or plan in other words; an agent other than the orchestrator reads the cycle record to
    learn an answer; a method keeps a log of the cycle's progress beside the record; the
    orchestrator reloads completed stage material for routine progression.
- **Origin:** none

*Rationale:* full material kept outside routine coordination avoids repeated context while
preserving evidence a ruling needs and a place from which work can resume. Short returns make
the next action visible, but an omitted failure can hide behind brevity, so relevant evidence
remains part of a decision and an incomplete report blocks dependent work. Questions kept in the
report survive an interrupted session without being copied anywhere. A passage copied word for word
carries the requirement as its author wrote it, so the agent reads it without opening the whole
file, while a restatement is a second account of it that drifts from its source unseen. The cycle
record holds every agent's events; an agent that reads it pays for all of them to learn one answer.
*Rejected:* full handoffs and reports repeated in messages — coordination accumulates material
it need not reread; short summaries as the only record — lost evidence cannot be recovered on
resumption; a second universal brief and report contract — duplicated obligations drift without
proving completeness; a slice method's own ledger of progress beside the record — it repeats the
record and has to be copied into it before its workspace is cleaned; rereading every stage's
evidence during ordinary coordination — it pays again for work already delegated; automatic
compaction — it does not choose the evidence a ruling needs; a handoff that restates the plan,
spec or task in its own words — the restatement drifts from its source unseen; every agent opening
the whole task, spec, plan and record — each pays to read what only a part of its work needs.

### WAY-150 — How do the-way skills choose which product foundation material to read?

The-way skills read a product's foundation selectively: whoever selects names the parts the work
touches from the files it changes through the part map's rules for assigning files, or, where the
work names no file yet, from the responsibilities it changes; finds by a touched part's identifier
the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds
the invariants a test the work alters cites, the decisions the task's *Decisions in play* or the
work's source names, the touched parts' entries of the map and the entries these link to as far as
the work needs; and reads each selected entry whole, reading more entries where relevance is
uncertain and a whole file only where it is short. Outside the task cycle the agent doing the work
selects its own reading, while in the task cycle the orchestrator selects for its own judgments and
for each handoff, which names the foundation entries by identifier; the reviewer of the whole change
selects for its own review, and an agent writing a foundation entry through an element's skill for
the entry it writes; and every other agent of the cycle reads what its handoff names and reaches for
what is missing selectively — a search for an identifier or a word and a read of the passage found,
never of a whole file of the foundation — naming each such reach in its report. The selection is
neither recorded nor compared with every *Scope* of the log, and the search of the whole foundation
(WAY-33) and the whole reading of templates, rules and examples keep their domain.

- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts,
  project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-21 · derives from WAY-33 · derives from WAY-148
- **Verification:** an agent compares the reading with the work and current foundation:
  - complies: a change to a file of `gate` reads the decisions whose *Scope* names `gate`, found by
    searching for `gate`, those the task names, the invariants naming `gate` or `every` and the
    entries they link to; a project with no file yet names its parts from the responsibilities it
    changes; the search of the whole foundation finds a conflict outside those parts and the
    reading widens; in a task cycle the executor of a slice reads the entries its handoff names,
    searches for a decision it finds missing by its identifier and names that reach in its report,
    while the reviewer of the whole change selects its own reading;
  - violates: only decisions already named by the task are read; a search hit replaces its whole
    entry; a template is reduced to selected excerpts; the work records its selection and compares
    it with every *Scope* of the log; the whole decision log is read to find the decisions of a few
    parts; an invariant a test the change alters cites is left out because its *Part* names another
    part; an executor of a slice or a reviewer of a slice selects its own foundation reading, or
    reaches beyond its handoff without naming the reach in its report.
- **Origin:** none

*Rationale:* a growing foundation contains more material than each piece of work needs, while
unconditional loading spends attention on unrelated rules. The parts a change's files belong to find
the decisions that govern it (WAY-21), the task names those it settles, and links lead to the rest,
so the governing material stays visible; what no link joins, the author's search of the whole
foundation finds (WAY-33). In a task cycle the orchestrator reads the foundation of the task's parts
to coordinate it anyway; selecting once for the handoffs spares each agent a selection of its own,
which every agent of the cycle would otherwise pay for again. An agent writing a foundation entry
searches the whole foundation for it anyway (WAY-33), so it keeps the selection its element's skill
gives. A reach named in the report shows where the selection fell short, and the reviewer of the
whole change, selecting for itself, finds a governing rule the orchestrator missed before the
request.
*Rejected:* unconditional whole-foundation loading — its context cost grows with unrelated work;
selection only from known links or keywords — a governing decision can remain unseen; a fixed
reading limit — a difficult case loses needed context; a separate maintained index — a second
account can drift without resolving semantic relevance; a record of the selection compared with
every *Scope* of the log — it costs every piece of work and records reading, not understanding;
each agent of a task cycle selecting for itself — every agent pays for the same reading again;
the orchestrator's selection with no reach left to the agent — a missing entry is guessed at
instead of read; the reviewer of the whole change reading only the orchestrator's selection — a
gap in the selection would reach the request unchecked.

### WAY-151 — How much of large project definitions and existing plans does plan-project read?

The-way's plan-project limits reading of large project definitions and existing plans to the
material needed for the work, starting from complete inventories of scope items, projected entries,
open questions and existing tasks and their dependencies and assignments, then reading complete
source units and expanding whenever their meaning or dependencies reach further.
A new breakdown covers every scope item, projected entry and open question, and a resumed change
reads all units its dependencies or meaning reach, with the original whole documents remaining
the inputs to the existing readiness and plan checks.
The plan's one independent critique reads the complete plan and every source unit needed for its
whole semantic judgment under WAY-146, independently of the author's selection.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-146
- **Verification:** an agent compares the reading, inventories and verification record with the
  authoritative definition and plan:
  - complies: resuming an unfinished plan inventories all tasks, assignments and exact questions,
    then reads a distant dependency and projected-entry writer that affect the resumed work;
    whole-original checks run and the critic reads the whole plan with all needed sources;
  - violates: only nearby rows are inspected and a distant dependency is missed; a readiness or plan
    check receives a reduced copy; a new breakdown omits a scope item; the critic's review is
    bounded by the author's excerpts or leaves some tasks and questions unjudged.
- **Origin:** none

*Rationale:* large project documents hold context for many tasks, while resumed work usually
changes only some of it. Complete inventories expose distant assignments and dependencies before
context is selected, and whole verification protects the complete project; the cost is careful
expansion whenever meaning reaches beyond the initial selection.
*Rejected:* reading every large source whole at every resumption — unrelated context is loaded
repeatedly; reading only the unfinished section — distant dependencies and settlements disappear;
checking reduced copies or limiting the critic to selected material — omissions can agree with
the reduced input and pass unseen; maintaining a second plan for reading — copies drift.

### WAY-152 — What does leading a project plan leave to others?

The project orchestrator leads a handed-over project plan from tasks to refine to human-accepted
tasks ready for their cycles and keeps the plan's states consistent with evidence, proposing a
round of refinement first from tasks on which the most other tasks depend for the human to
confirm or change. The human starts task cycles separately, and when the last task is done the
project orchestrator names project closure as the next step, performing neither closure nor a task
cycle. After a task merges, leading the plan does not recheck ready dependent task documents: the
task cycle checks and adapts its sources at its own start.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106 · derives from WAY-124 · derives from
  WAY-144
- **Verification:** an agent compares the leading session with the decision:
  - complies: the human changes a proposed round, the project orchestrator coordinates its refinement
    and maintains evidenced states, and the human starts a ready task's cycle separately;
  - violates: leading launches a cycle, closes the project, or re-refines every ready dependent
    task after a merge instead of leaving the cycle's source check to its start.
- **Origin:** none

*Rationale:* the human needs one conversation that keeps a plan moving and its progress visible.
Keeping task execution and closure separate bounds that conversation, while checking current
sources where implementation begins avoids repeating a check whose inputs can change again.
*Rejected:* leading that also executes cycles and closes the project — distinct work obscures the
point where the human starts implementation; automatically reopening ready dependants after each
merge — repeated refinement can be invalidated again before implementation.

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
- **Verification:** invariants: project-plan-state-evidence · project-plan-state-subprocesses. For
  applying proposals and resolving PR outcomes, an agent compares the evidence and leading session
  with the decision:
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

### WAY-154 — How do agents exchange a project task refinement and keep its result?

Project refinement resumes from the plan, task documents and one ignored conversation file per
task at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the
answering agent and the project orchestrator take serialized turns on each file; the project
orchestrator hands agents only its path and routing, never relays its contents, and each refiner
ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or
`obstacle`. Only a refiner changes the task document's body and transfers settled answers with
their sources into Questions to settle; the project orchestrator records human answers in
conversations, owns ordinary plan updates and their log, and changes only the task document's
Status line after the human has accepted that complete document, one document at a time. Agent
turns, questions and explicit waits keep the plan task to refine, a presented human package or
ready for approval makes it waiting for human, and final acceptance makes both document and plan
ready for cycle and removes only that conversation after all settled answers and their sources
survive in the task document; an explicit wait is logged and its task is proposed again when the
named prerequisite is done.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-124 · derives from WAY-142 · derives from
  WAY-144 · derives from WAY-147
- **Verification:** an agent compares the turns, task documents and plan with the decision:
  - complies: parallel refiners write separate documents, a fresh refiner keeps each settled
    answer and source, and interrupted acceptance resumes without guessing human agreement;
  - violates: the project orchestrator rewrites a task body or carries questions in prompts,
    an agent's readiness stands for human acceptance, or cleanup loses the only settled answer.
- **Origin:** none

*Rationale:* a file-mediated exchange keeps the project orchestrator from becoming a content relay
and lets another session resume. The retained task document carries the result that later work
needs; ownership and serialized turns cost explicit coordination but prevent competing edits.
*Rejected:* conversation contents relayed in prompts — each transfer repeats context and can lose
answers; retaining the temporary exchange as the task result — later work reconstructs settlements
from discussion; deleting the exchange before durable transfer — provenance disappears.

### WAY-155 — What may the answering agent settle during a refinement round?

The answering agent answers a refinement question only with a quotation and source from the
definition, plan, foundation or other task documents, or with a factual code observation naming
file and line; a question about how the product is to be is answered only from a document, never
from code or the agent's inference. It reads the round's conversations, makes an unanswered
choice a question to the human with options, costs and a recommendation, and brings the same
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

### WAY-156 — How does project leading route a plan or definition change?

An in-scope task split, new task, order or dependency change is delegated to a plan-project agent
and logged with its reason, while a scope change goes to the human, as does a reassignment of the
task writing a projected entry (WAY-145). The project orchestrator changes definition text itself
only when that text is already before it and needs no reading of other definition sections or the
foundation; otherwise it delegates the edit, and a subagent always performs the definition's
readiness gate, with independent critique dispatched by the project orchestrator and its findings
returned to that subagent, and human approval given through the project orchestrator. A fresh
subagent then checks the plan again through plan-project step 0, and no task gains ready for cycle
while that definition gate remains open.

- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-118 · derives from WAY-120 · derives from
  WAY-145
- **Verification:** an agent compares the edits, gate, critique and rechecked plan:
  - complies: a local text edit is made from material already read, a subagent completes the
    full gate, the human approves through the project orchestrator, and a fresh agent checks
    the plan before readiness resumes;
  - violates: a wider definition edit is made without delegation, the project orchestrator runs
    its gate itself, or a task becomes ready against a changed but unapproved definition.
- **Origin:** none

*Rationale:* a project can change direction while refinement proceeds, but its approved definition
is the basis of every task. Keeping the full gate and fresh plan check costs another review while
preventing readiness against an obsolete basis; a narrow edit exception avoids needless handoff
for text already available without making leading responsible for wider execution.
*Rejected:* every definition edit performed by the project orchestrator — it takes on execution and
additional context; every local edit delegated — a transfer costs more than the already bounded
edit; bypassing the gate for a small change — size does not establish that its meaning stayed.

### WAY-158 — Who reads the full diff of a task-cycle change or slice?

The independent code reviewer reads the full diff of the range it reviews — a one-author change, a
slice with a review of its own, or the whole change, every slice of a plan included, judging each
slice that had no review of its own as its only review — while the task-cycle orchestrator uses its
changed-file list with added and removed line counts and the first line of the reviewer's report,
`PASS` or `FAIL` with the head commit, for routine progression. A question, finding or disputed or
incomplete evidence still calls for the orchestrator's relevant source and report reading under
WAY-148.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-136 · derives from WAY-148
- **Verification:** an agent compares the review range and coordination record with the change:
  - complies: the independent reviewer reads the entire committed range and returns `PASS` or
    `FAIL`, while the orchestrator uses that line and the range's file and line-count summary; the
    reviewer of the whole change of a plan reads the diff of every slice and judges each that had
    no review of its own;
  - violates: the reviewer sees only a summary, or the orchestrator reads the full diff again
    for routine progression; an unresolved finding is settled without reading its evidence; a
    slice without a review of its own is passed over by the review of the whole change.
- **Origin:** none

*Rationale:* the independent reviewer already reads the change for correctness, so repeating that
read in coordination costs attention. The trade-off is that coordination does not catch what the
reviewer misses; the human's review of the request remains.
*Rejected:* the orchestrator routinely reading the full diff beside the reviewer — duplicated
reading dominates coordination; giving the reviewer only a summary — the actual change escapes review.

### WAY-159 — When does the task-cycle orchestrator rely on focused-check evidence?

The author or executor runs the focused checks of its change or slice and reports each as its
command and exit code; the orchestrator relies on that evidence instead of rerunning those checks
for routine progression. A report missing the command or the exit code of a check it ran is
incomplete, and a claim that tests passed does not repair it; a change or a failure calls for its
affected checks to run again.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-148 · derives from WAY-13
- **Verification:** an agent compares the executor's check evidence and subsequent coordination with
  the committed range:
  - complies: the executor reports the command and exit code of each check, and the orchestrator
    proceeds without another run; a missing exit code returns for repair; a correction runs its
    affected checks again;
  - violates: a bare claim that tests passed substitutes for an unreported check, the orchestrator
    reruns a check solely because the executor returned, or a changed range uses stale evidence.
- **Origin:** none

*Rationale:* repeating a completed check for coordination spends time without checking another
state. A command and its exit code say what ran and whether it passed, and the check can be run
again when a result is uncertain; a changed state or an unresolved failure needs new evidence
rather than reuse by habit.
*Rejected:* rerunning focused checks after every return — repeated work delays the cycle; trusting
a claim without execution evidence — a check that never ran can appear complete; never rerunning
after a correction — the evidence would describe an earlier change; the full output of every check
kept in a file of the cycle — the command and exit code already settle whether it passed, and a
report naming a failure says what failed.

### WAY-160 — How does the task-cycle orchestrator run the finished change's gate?

The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request,
and the request gives its command and exit code and names each check that failed or did not run; a
check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no
author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of
it.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-16 · derives from WAY-63 · derives from WAY-148
- **Verification:** an agent compares the gate's run and the request with the decision:
  - complies: the orchestrator runs the gate after the review of the whole change and again after
    the return step changed the tree, and the request gives the command and its exit code;
  - violates: the focused-check reports replace the gate on the finished change; the request calls
    a check that did not run passed; the gate ran on a tree other than the one the request holds; a
    plan's *Checks* or a handoff tells an executor to run the gate after its slice.
- **Origin:** none

*Rationale:* the finished change needs verification across the work that made it, which no
author's focused checks give, and the orchestrator owns that run. The command and its exit code
tell the human what passed; the checks that failed or did not run, named, keep what stayed
unchecked in view. A gate run after every slice repeats for each slice a run the finished change
needs once and holds the next slice until it ends, while the focused checks of the code and
invariants a slice reaches find what it breaks there.
*Rejected:* the gate's full output kept in a file of the cycle, with its failure lines brought into
the orchestrator's context — the exit code and the failures named settle the same; executor checks
in place of the gate on the finished change — the combined result is never checked; an exit code
alone — a check that did not run would pass unseen; the gate after every slice — it multiplies the
gate's run by the number of slices and holds each slice for it.

### WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?

In the review of the whole change on either route, a finding blocks when the reviewer grades it
Critical or Important and has not itself marked it as outside the task's scope, and a review that
leaves no blocking finding sends the change to its request without a fix. A finding the reviewer
has marked as outside the task's scope — a line of its list of what it declined to judge, or a
finding it describes as going beyond the task — is not fixed, whatever its grade, nor is a Minor
finding, and the request lists those findings in an item of their own and the Minor findings in
another, each with the reviewer's words and its place in the code, while the human decides which
findings outside the scope become new tasks and creates them. The orchestrator moves no finding
from one of these kinds to another.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-136 · derives from WAY-227 · derives from
  WAY-140
- **Verification:** an agent compares the cycle and its request with the decision:
  - complies: the review of a one-author change returns only Minor findings, and the change goes
    to its request without a fix, the request listing each of them with the reviewer's words and
    its place in the code; the reviewer sets aside under "Declined to judge" a behaviour the task
    does not ask for, the request lists it in an item of its own, and the human creates a task for
    it; the final review of a planned change returns an Important finding within the task, and a
    fix follows;
  - violates: a fix runs for Minor findings alone; the fix after the whole-change review of a
    planned change takes in the Minor findings of its slice reviews; the orchestrator rules on a
    line the reviewer
    declined to judge, or moves an Important finding within the task to the list for new tasks;
    the cycle adds a task to the product's backlog itself; the Minor findings stand only in the
    cycle's reports the request links to.
- **Origin:** none

*Rationale:* the grade a reviewer gives already says how much a finding matters, so taking it as
the line between what blocks and what does not adds no second label to the review and
leaves no finding without a place; a label given against the task would let a finding tied to no
requirement of the task pass as non-blocking. A minor finding fixed in a round of its own spends
that round on polish, while one listed in the request with the reviewer's words stays in front of
the human who merges; a list the request only links to is a list nobody reads. A finding that
widens the work is a new piece of work rather than a repair of this one, and the reviewer, who has
no stake in closing the cycle, is the one to say which findings lie outside the task, since an
orchestrator sorting them could move an inconvenient finding out of the way of the blocked request.
The human creates the new task because each product keeps its backlog where it chooses (WAY-101),
and where that is outside the repository, only a human makes an effect there (WAY-140).
*Rejected:* a label of its own, blocking or not, that the reviewer gives each finding against the
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
record of stages, with the number of review rounds. In the code reviews after the review of the
whole change, the findings that do not block go unfixed to the request's lists as WAY-161 gives
them.

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
    request;
  - violates: the orchestrator rules on a finding left after the review of the fix and marks the
    request ready; a third round of fixes runs, on a slice or on the whole change; a new Important
    finding in the fix is left out of the blocked request because the findings it set out to fix
    were fixed; a Minor finding of a later code review stands only in that review's report.
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
the request only links to is a list nobody reads.
*Rejected:* the orchestrator ruling on the findings left after the review of the final fix — a
change the reviewer did not accept reaches the request as ready; up to five rounds of fixes on a
slice, the orchestrator ruling on what remains after them — each round costs as much as the last,
and the orchestrator rules in the end after all; a report of the remaining findings without a
request, in conversation or in the cycle record — the request is the one place where the human
judges the cycle's work, and a report in conversation is lost with the session; no bound for the
code reviews after the review of the whole change — the orchestrator would rule on the remaining
findings after all; the findings of those later reviews that do not block kept in their reports,
which the record links — a list the request only links to is a list nobody reads; one more round
for a finding the fix introduced — a fix could trade one blocking finding for another without end.

### WAY-163 — What does the cycle run before it opens a request its code review blocked?

Before the cycle opens a request that a remaining blocking finding blocks (WAY-162), it runs the
product's gate on the change and writes its cycle record with its record of stages, while it makes
no further slice and runs neither the reconciliation with the target branch nor the return step on
code its review has not accepted, and the request names each of these that has not run on that
code. After the human's decision on the request, the work on its branch starts with that
reconciliation and runs the others on code that has passed review or that the human accepted
despite the finding.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-162 · derives from WAY-11
- **Verification:** an agent compares the cycle and its request with the decision:
  - complies: a cycle blocked after the review of the final fix runs the gate, writes its record,
    opens the blocked request naming the reconciliation with the target branch and the return step
    as not run, and runs them once the human accepts the code despite the finding; a cycle blocked
    by the review of a slice names the slices not made as well;
  - violates: the return step runs on code its reviewer blocked; the target branch is merged and
    its affected code review run before a request blocked by an earlier review; the blocked request
    opens without a run of the gate on the change; a request whose code the human accepted despite
    the finding is merged without its return step.
- **Origin:** none

*Rationale:* work an agent does on code its review has not accepted is done again once the fix the
human's decision calls for is made, while a run of the gate costs little and shows the human where
the code stands against the rest of the product's checks, and the cycle record holds the cost the
request names. The return step still comes before any merge (WAY-11), so leaving it out before a
blocked request moves it rather than drops it, even where the human's decision changes no code. The
reconciliation with the target branch waits with it, because it would draw a code review of its own
on that code, and the work after the human's decision begins by merging the target branch in any
case.
*Rejected:* every step up to the request run before the blocked request — agents work on code the
review did not accept and repeat that work after the fix; the cycle record and the cost alone — the
human would not see where the code stands against the rest of the product's checks; the
reconciliation with the target branch before the blocked request — its review would run on code the
review did not accept, and the merge is made again after the fix.

### WAY-164 — What does the author of a change check of its own work before review?

Before its work goes to review, the author of a one-author change names the requirement of the
task, and the executor of each slice the requirement of its slice read against the passages of the
task its handoff gives, that its work most likely does not meet, writes a check that would catch
that, and states in its report which requirement, which check and what the check showed. The
review that judges the work — a slice's own review where it has one, otherwise the review of the
whole change — reads that report, and the request lists what each such check showed among its test
evidence.

- **Scope:** task-cycle
- **Based on:** none
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
an invariant's test, which is seen failing once in its own right (WAY-08). The rule takes from an
agent harness's practice for its workers the naming of the requirement most likely to be false and
the check that would catch it.
*Rejected:* the author of a one-author change alone — in a larger change made from a plan, no agent
would attack its own work before review.

### WAY-165 — What must an answer to each matter of an agent's way to the running product settle?

Of the matters of an agent's way to the running product, the logs ask where the record of what the
running product does goes and how an agent reads it, and the interface asks how an agent operates
the product as its user does — through a screen in a browser, a call to its API or a command in a
terminal — and how it sees what the product answers. The development data asks where the data
comes from on which an agent checks the product's behaviour outside production, and how an agent
brings that data to the state a check needs. Data set up from scratch and a dedicated test
environment that persists are both options of that choice.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121
- **Verification:** an agent compares the work with the decision:
  - complies: for a game played in a browser, the logs are answered by an agent reading the output
    of the server's container, the interface by an agent playing the game in a browser on a local
    address and reading what the page shows, and the development data by a script that sets up
    test accounts with a fresh save, a save from the middle of a game and a password reset waiting;
    for a shop with a large store of data, the comparison of its development data weighs data a
    script generates, a copy of production without personal data that a human fetches, and a
    dedicated test environment that persists, each by its consequences;
  - violates: the interface is answered by an agent reading the store of data past the
    application; the development data names where the data comes from but not how an agent reaches
    a save from the middle of a game; the comparison of the development data leaves out a dedicated
    test environment that persists because the data has to be set up from scratch.
- **Origin:** none

*Rationale:* each answer serves an agent that checks behaviour a user sees in the running product.
The logs tell the agent what the product did, and the answer says where that record lands, since
an agent reads only what it can reach. Operating the product as its user does lets the check see
what a user sees, while reading the store of data past the application shows a state no user meets
and skips the code in between. A check needs the data in a given state, so the answer says both
where the data comes from and how the agent brings it to that state; otherwise the agent of the
cycle improvises it. A dedicated test environment that persists is in many cases better than data
set up from scratch for every change, though it brings costs of its own, so neither is ruled out
and the step weighs them by their consequences (WAY-123).
*Rejected:* the interface without "as its user does" — access to the store of data past the
application would count as an interface; the development data asked as data rebuilt from scratch —
it rules out a dedicated test environment that persists, in many cases the better option; the
development data with no word on reaching a state — a decision could leave unsaid the state a check
needs, and the agent of the cycle improvises it; what the product logs and in what form, in the
same decision — that rule acts where code is written and reviewed, in the task cycle, not where a
project settles its technology.

### WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product?

In a choice of an agent's way to the running product, whether an agent can use an option is a
consequence for the product: an option an agent cannot use stays in the comparison with that lack
said as "an agent does not check the running product this way", and the recommendation passes over
it.

- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121 · narrows WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: a log service cheaper than the others, whose logs only a human can read, in a panel
    behind the human's login, stays in the comparison of the logs with the lack "an agent does not
    check the running product this way", and the step recommends reading the output of the
    server's container;
  - violates: the step recommends the cheaper service because how well an agent works with an
    option decides only a tie; the service is left out of the comparison because an agent cannot
    read its logs; the table shows the service with no word on whether an agent can use it.
- **Origin:** none

*Rationale:* a choice of an agent's way to the running product exists so that an agent can check
what a user sees in the running product; an option the agent cannot use leaves that check undone,
and the product's behaviour reaches the human unchecked, which is a consequence the product bears
rather than the agent's convenience. Kept in the comparison with its lack, the option stays open to
the human, who chooses between consequences (WAY-123). For a place to run, how well an agent works
with an option still decides only a tie (WAY-137): there the agent's convenience is not what the
product needs from the choice, while here the agent's use of an option is what the choice is for.
*Rejected:* nothing added to the usual weighing of consequences — the step could recommend a
cheaper service an agent cannot use, since how well an agent works with an option decides only a
tie, and the choice would pass with an answer that gives the agent nothing.

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
- **Relations:** derives from WAY-44 · derives from WAY-04
- **Verification:** an agent compares the change with the decision:
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
because they hold no rule of their own, only how to apply rules the foundation's entries carry, so
the five elements stay as WAY-04 closes them. They direct whoever carries out tasks, like instruction
files and skills, so they belong to that part, whose files change every later task (WAY-44), and an
instruction file leads to them as to knowledge needed now and then (WAY-128). One directory with
fixed names lets a check find them in every product; a product whose screens and admin panel are
drawn by two parts keeps a styleguide for each, and the part's identifier in the name ties a
styleguide to the files it governs, so that a renamed part shows. Coding guidelines are cut by the
kind of code rather than by part, since a kind such as an endpoint can live in more than one part
while its exemplar is one: the general file holds what binds the whole of the code once, and an
agent reads, beside it, only the files of the kinds its work touches, which the general file's
table names with when to read each, as Open Mercato's table leading from a task to the guides to
read does. The kind's identifier comes from the decision designating
its exemplar, so that a file of a kind stands only where a human has approved what it holds.
*Rejected:* guidelines as a sixth element of the foundation — what binds in them is already carried
and checked by decisions and invariants, and the list of elements would no longer be closed; an
extract a script composes from the foundation's entries — it holds what the entries say, never how
to apply a rule or a use that follows it and one that breaks it; a styleguide in documentation
beside the code — it directs whoever carries out tasks, whose files WAY-44 gives a part of their
own, yet a change to it would count against the part whose code it describes; meanings kept in the
spec of a screen — the spec ends with its task, and the next screen gives the same colour another
meaning; guidelines in the own directory of the part that directs agents — its path differs from
product to product, and no check could find them; one styleguide for every user interface of a
product — an admin panel and the product's screens are drawn by different parts; all coding
guidelines of a product in one file — it grows beyond measure, and an agent reads rules its work
does not touch; a file of coding guidelines for each part of the map — a kind living in two parts
and the standing checks repeat in several files and drift apart; a file for each kind with no
general file — the standing checks have no place.

### WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?

A binding rule of a product's guidelines names by identifier the decision of the product's log that
carries its choice and says what to do and how, and may give a use that follows it and one that
breaks it, each in one line, while its reasons and rejected options stand in that decision alone;
what a product's guidelines hold that names no such decision is an example, not a rule. A rule
names an invariant only where a cheap test of the product's suite checks the rule on a convention of
the product's code; a rule no such test can check names none, and the review of each change the rule
reaches compares the change with it.

- **Scope:** product-guidelines, decisions, invariants
- **Based on:** none
- **Relations:** derives from WAY-22 · derives from WAY-18 · derives from WAY-08
- **Verification:** an agent compares the change with the decision:
  - complies: a rule of a product's testing guidelines names the decision choosing the product's
    fixtures for test data and the invariant whose test finds a test that writes rows straight into
    the store of data, and gives in one line each a test that sets up its data through the fixtures
    and one that writes rows straight into the store; a rule that red marks only what deletes names
    its decision and no invariant, and the review of a change to the screens compares their buttons
    with it; a sentence on how one team likes to name its branches, which no decision carries,
    stands among the examples;
  - violates: a rule of a styleguide repeats its decision's rationale and rejected options; an agent
    holds a change to a rule that names no decision; a rule whose meaning only a reading can judge
    names an invariant an agent checks; a rule carries whole files as cases run against the test of
    its invariant.
- **Origin:** none

*Rationale:* guidelines do not replace the foundation's elements but bring what they hold to the
work of one discipline: an agent changing a product's screens needs what to do and how, not an
account of why. A choice that binds is a decision (WAY-22), and a product keeps every decision in
one log (WAY-18), where a collision with the product's other choices can be found and the search of
the whole foundation sees it (WAY-33); named by its identifier, the decision carries its reasons
once, and a change that rewords it brings the rule in line (WAY-169). A rule naming no decision
would bind with a choice nobody approved, so it is an example; where a rule gives a use that follows
it and one that breaks it, they mark its line, as a pair of examples marks a decision's, and like
that pair they are optional (WAY-12). A rule of guidelines that an instruction file leads to thus
carries a decision the product records, the case in which WAY-130 lets a rule stand with no mistake
behind it. A cheap test on a convention of the code catches a breach of its rule on every change for
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

### WAY-169 — What happens to a reference of guidelines when the entry it names changes?

A change that changes the binding part of a decision or an invariant brings every
rule of the guidelines naming it in line in the same change, its author finding those rules by the
entry's identifier.

- **Scope:** product-guidelines, elements-common
- **Based on:** none
- **Relations:** derives from WAY-02 · derives from WAY-33
- **Verification:** an agent compares the change with the decision:
  - complies: a rule of a styleguide names `GAME-07` in *Decision*; a product rewords the decision
    that gives its `destructive` role its meaning, and the same change rewrites that role's meaning
    in its styleguide;
  - violates: a rule reads `GAME-07@60960941`; a change rewording a decision merges, and the
    styleguide that restates it is left for a later task.
- **Origin:** none

*Rationale:* an identifier outlives every rewording of its entry, so a reference by it stays valid,
and one naming no entry, or a withdrawn one, leads nowhere and is found by the check of references
(WAY-02, WAY-170). Guidelines that say in silence other than their decision are worse than weak
ones, since agents go on following the old rule, and the author of the change that moved the entry
knows what moved, so that change brings them in line, as it brings the entries it touches (WAY-33).
Every reference counts, in a rule's prose, an example or a table as much as in a field, since an
agent reads them all alike.
*Rejected:* a fingerprint on every reference, stopping the merge until it is renewed — renewing a
mark does not lead to reading the rule that carries it, and every rewording that changes no meaning
makes work; the guidelines left for a later task — agents read the old rule meanwhile; only the
fields of a rule brought in line — a reference in a rule's prose or in an example drifts unseen.

### WAY-170 — What checks the form of a product's guidelines?

No script of the-way checks the form of a product's guidelines: the review of a change that writes
or changes them compares them with the template every product's guidelines share and, where the-way
gives one, the template of their discipline, at the commit of the-way the product pins.
`elements/common/foundation_check.py` reports every decision number in a file of a product's
guidelines, every invariant a rule's *Invariant* names and every part *Applies to* names that the
product's foundation does not hold, or holds as withdrawn.

- **Scope:** product-guidelines, elements-common
- **Based on:** none
- **Relations:** derives from WAY-10 · derives from WAY-34
- **Verification:** an agent compares the change with the decision:
  - complies: the review of a task that writes a product's first styleguide finds a rule that
    repeats its decision's rationale and asks for it to go; a styleguide names `GAME-40`, which the
    log does not hold, and the check of references reports it;
  - violates: a change to a product's styleguide merges without its review reading the template of
    the styleguide; the-way's template of guidelines gives every product an invariant whose test
    checks the headings of its guidelines; a rule names a withdrawn decision, and nothing reports
    it.
- **Origin:** none

*Rationale:* the form of a file of guidelines misleads no agent that reads it, while what a rule
says can, and only a reading judges that; the review reads the guidelines a change touches anyway
(WAY-10). A reference naming no entry does mislead, and a check of references finds it in every
file at once (WAY-02). The templates come from the commit the product pins, so a product's
guidelines change their form only when it moves its pin (WAY-34).
*Rejected:* a script of the-way checking every file of guidelines against the templates before each
merge — it reports headings and fields, never a wrong meaning, and every change to a template is a
change to the script; invariants of guidelines that every product holds, whose tests run that script
— each product carries entries for a check of the-way's; the form left to readers with no check of
references — a rule naming a withdrawn decision would go on binding.

### WAY-171 — What form does a file of a product's guidelines take?

Every file of a product's guidelines holds, in this order, the header lines *Discipline* and
*Applies to*, the latter naming parts of the product's map, and the sections `## When to read`,
`## Rules`, `## Examples` and `## Where in code`, with what the template of its discipline adds at
the places that template names, and each rule of `## Rules` stands under a heading of its own with
the fields *Decision*, *Invariant*, *Good* and *Bad*, the last two reading `none` where the rule
gives no such use. `## Where in code` names by their paths the files and directories of the
product the guidelines point to and copies no value from them, and a section or a rule that a
template of the-way requires and the product drops holds only `none —` followed by the product's
decision that departs from it. The headings, header lines, field names, values of closed lists and
the marker `none —` stay in English while the rest of the text is in the language the product
writes its guidelines in.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-168
- **Verification:** an agent compares the change with the decision:
  - complies: a product whose team writes in Polish writes the rules and examples of its styleguide
    in Polish under the English headings and fields;
  - violates: a product translates the headings of its guidelines, and the-way's templates and
    skills no longer find them; a styleguide copies the values of its colours under
    `## Where in code`.
- **Origin:** none

*Rationale:* one form lets an agent and a reviewer find the same sections in the guidelines of every
discipline, and a discipline's template only adds to it, so guidelines of a discipline the-way gives
no template of still have one; the fields carry what a rule holds beside its entries (WAY-168). A
copy of a value the code holds goes stale, so the guidelines point to it (WAY-225). A part a
template requires is dropped only by a decision, so a departure is the product's own approved
choice, visible where the part would stand. The structural words stay in English because the-way's
templates and skills name them and the check of references reads fields by their names, as a project
definition keeps its headings in English while its content follows the human's language (WAY-108);
the rest follows the product, whose agents and people read it, and binding it to English would bind
every product's text for no reader of the-way's. The price: where that text is in another language
than the decisions, a meaning it restates is a translation, and a translation that drifts while its
decision stands is caught only by a reader; the guidelines stand outside the foundation, so this is
not the translation WAY-114 keeps out of it, and the decision stays the one binding wording.
*Rejected:* every file of guidelines wholly in English — it binds the text every product's own agents
and people read; the language of the conversation that wrote each part — a document that lives
across tasks would change language from one session to the next; guidelines only of the disciplines
the-way gives templates of — a product could not write guidelines of a discipline of its own; a
required part left out with no word — a departure would look like an omission.

### WAY-172 — How is a new or changed meaning of a product's guidelines approved?

A new or changed meaning of a product's guidelines is a decision of the product's log, new or
changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has
approved it, in the document of the task that needs it, as WAY-30 has a change to a decision
approved, or, where that document does not settle it, at a blocked draft request on whose branch
the cycle proposes the decision. Using a meaning that a decision of the product's log already
carries takes no approval, and neither does changing a value that keeps its meaning. In the area of
new and changed meanings of a product's guidelines this decision prevails over WAY-114, under which
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
    the contrast its decision asks for, its meaning kept, and asks no one;
  - violates: a cycle writes a new role's decision on its own recommendation and leaves it to the
    merge; the orchestrator's go-ahead stands for the approval of a new meaning; a screen that uses
    an existing role waits for the human.
- **Origin:** none

*Rationale:* a meaning of guidelines binds every later screen, and code built on one the human never
saw is reworked when the human turns it down at the merge, so the approval comes before the code,
where WAY-30 already puts a change to a decision; the task's document is where the human sees what
the cycle is to build on (WAY-124), and a blocked draft request is where the human meets a decision
the cycle cannot make alone (WAY-227). A meaning a decision already carries was approved with it,
and a value changed with its meaning kept changes no rule, since the rule is the meaning and the
value stands in the code (WAY-225), so neither waits. Without the precedence, a cycle meeting such a
meaning would face this decision and WAY-114 with nothing to choose between them (WAY-25).
*Rejected:* a new meaning written by the cycle and shown at the merge, as WAY-114 gives it — code is
built on a meaning the human has not seen, and turning it down reworks the screens; approval with
the plan — in a cycle the human sees the request, not the plan (WAY-227, WAY-136); approval of every
use of a meaning — every screen would wait for the human.

### WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?

The rules a template of a discipline of the-way carries and what the-way's skill of that discipline
proposes bind a product only through a decision of the product's log adopting them, and the product
departs from any of them only by a decision of its log that gives the reason. A decision of the-way
on what such a template carries or what such a skill proposes binds the template and the skill,
never a product's screens or code directly.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-168 · derives from WAY-100
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
    is red with white text on it", with the ways open, their cost and its recommendation; it asks
    whether to adopt WCAG though it recommends adopting it, after saying in plain words what
    contrast is; the coding-guidelines skill shows "a change that adds a library with a known
    security hole does not get in" with the ways open, their cost and its recommendation, asks
    whether to adopt the formatter it recommends, and shows a linter's set as "this many rules will
    block a change, and these few flagged sound code here and stay as examples", and the human
    adopts the set with that split; the testing-guidelines skill shows "the tests of the account
    server talk to a real database, so a broken query turns them red, at the price of a slower run",
    after saying in plain words what an integration test is;
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

### WAY-176 — How does a styleguide name its colour roles and pair them?

The template of the styleguide discipline gives a styleguide a table of roles, each named by what it
is for and never by a colour, such as `primary` or `muted`, of the kind `background`, `text` or
`other`, with one sentence of what someone using the product understands on seeing it and the
decision that carries that meaning, each pointing to the role's value in the product's file of design
tokens without copying it. Each role of the kind `background` stands in that table with the role of
the kind `text` that stands on it.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** for names, meanings and values, an agent compares the change with the
  decision:
  - complies: the role `destructive`, of the kind `background`, means "this action deletes something
    for good", carries `destructive-foreground` as the text on it, and names the decision that gives
    that meaning, while its value stands only in the file of design tokens; a product whose library
    names a role `surface` keeps that name in its code and its styleguide;
  - violates: a role is named `red-600`; one role named `green` stands for both "this rule can act"
    and "the game is won"; the table copies the colours' values.
- **Origin:** none

*Rationale:* a name after a shade cannot catch one colour carrying two meanings, while a name after
a role makes a second meaning visible as a role that does not fit; the sentence of what the user
understands is what an agent at work needs, and the decision it names is where that meaning is
approved and checked against the product's other choices (WAY-168). A background never stands alone:
its text decides whether anything on it can be read, so the two are written together. Values are
held by the code, so the table points to them (WAY-171).
*Rejected:* variables named by shade, as one product's design system has them — they do not catch
one colour in two meanings; a background role defined with no text role on it — its pair goes
unchecked; the values written into the table — a copy of the code goes stale; role names kept clear
of every word the glossary of the-way holds — a role's name lives in the product's code, which uses
the words of its own field unchanged (WAY-104), and the-way's words stay on the-way's side.

### WAY-177 — What does a styleguide say of shared controls?

The template of the styleguide discipline has a styleguide point by its path to the directory of the
product's shared components and name the states each shared control has — default, hover, visible
focus, disabled, error, empty and loading — each shown on the page of every state or marked as not
applying with its reason. It names a component by its path only where that component departs from
the list of states, and never copies the list of components the code holds.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a styleguide points to `src/components/` and gives the seven states, and names
    `src/components/Toggle.tsx` alone, as a control with no empty state, with that reason;
  - violates: a styleguide describes a button in its default state only; a styleguide lists every
    component of the product with its file.
- **Origin:** none

*Rationale:* the states other than the default are the ones that drift first and that a screenshot
of a screen with data never shows, so the styleguide names them for every shared control; a state a
control cannot have is marked with its reason, so an omission and a choice are told apart. The code
already says which components exist, and a copy of that list would go stale (WAY-225).
*Rejected:* controls described in their default state alone — the other states drift unseen; a list
of components copied from the code — it goes stale at the next component.

### WAY-178 — Where is a fault of one screen fixed?

The template of the styleguide discipline has a styleguide hold that a global design token carries a
meaning for the whole product, and that a fault of one screen is fixed in that screen's component,
never by changing a global design token's value for that screen's sake. A change of a global design
token takes what WAY-172 gives a change of a meaning and a change of a value.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-172
- **Verification:** an agent compares the change with the decision:
  - complies: a list whose rows lose their spacing on one screen is fixed in that list's component;
    a change that darkens `primary` for every screen to reach the contrast its decision asks for
    goes without approval;
  - violates: the value of `muted` is changed so that one screen's text reads better, and every other
    screen changes with it; a change of what `primary` means is made as a fix of one screen.
- **Origin:** none

*Rationale:* a global design token is read by every screen, so changing it for one screen changes
what all the others show, unseen by the task that made the change; a fix in the component stays where
the fault is. What such a change takes is set once, by WAY-172, so this decision only points to it.
*Rejected:* a global value adjusted to fix one screen — every other screen moves with it.

### WAY-180 — Does a styleguide require a page showing the product's components in every state, and where is it served?

The template of the styleguide discipline has a styleguide name by its path a page of the product
that shows its shared components and samples in every state, a page the product serves in development
alone and never in production. The page is code of the product, not part of the styleguide's text.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a styleguide names the page at `/states`, which answers "not found" in a production
    build, and each shared control appears there in its seven states;
  - violates: the page is served in production; the styleguide holds drawings of the states in
    place of a page of the product.
- **Origin:** none

*Rationale:* the page is the visual half of the styleguide: it shows in one place what the text says
of every state, for an agent checking its work and for a reviewer, while a screen with data shows
only one state. Served in production it would show users samples meant for the team; as code of the
product it changes with the components it draws, which a picture in a document would not.
*Rejected:* no such page — the states other than the default are seen nowhere at once; the page
served in production — users meet samples; pictures of the states in the document — they go stale.

### WAY-182 — Where does a value of design tokens say it comes from, and who picks the source?

The template of the styleguide discipline has each value of the product's file of design tokens carry
beside it where it comes from. The skill `maintain-styleguide` chooses that source for each product,
and the-way holds no list of tools values are taken from.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a line beside the block of colours in the file of design tokens names the theme of the
    product's library and its version they come from;
  - violates: values stand in the file with no word of their source; the template names a theme
    generator every product takes its values from.
- **Origin:** none

*Rationale:* values that live only in a conversation are values the next session invents again, so
each keeps its source where it stands. Which source fits depends on the product's technology and on
what it already has, so the skill chooses it with the human, and a list of tools in the-way would fit
only the products that use them.
*Rejected:* values with no source — the next change cannot tell a choice from an accident; the
lists of theme generators and presets as sources every product takes — they fit only some
technologies.

### WAY-183 — Which user interfaces of a product get a styleguide?

The skill `maintain-styleguide` proposes a styleguide for every user interface of a product, an admin
panel added to its backend included, however simple it is. A product whose users reach it only
through an API or a terminal has no user interface and gets no styleguide.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: a backend that gains an admin panel of three screens gets a short styleguide of its
    own; a command-line tool gets none;
  - violates: the skill passes over an admin panel because it is small or used by the team alone.
- **Origin:** none

*Rationale:* an agent left free does something different in every task, and that is what guidelines
are for; even guidelines of modest quality are consistent, and a product with them does not grow
into chaos, so a weak styleguide is better than none. A screen nobody outside the team sees still
needs one meaning for each colour.
*Rejected:* no styleguide for a small or helper user interface — each task styles it its own way.

### WAY-184 — When does a product's styleguide come into being?

The skill `maintain-styleguide` proposes that the styleguide of a user interface comes into being
before that user interface's first screen, with a set of starting rules wider than what the first
task that uses it needs.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: a product whose plan brings its first screen gets a styleguide task first, whose
    rules cover the roles, states and focus the product's announced screens need;
  - violates: the first screen is built and the styleguide is written from it afterwards; the
    styleguide holds only the roles of the first screen.
- **Origin:** none

*Rationale:* a first screen built with no rules is the screen every later one copies, and a rule that
blocks a change to a screen until a styleguide exists would need an exception for it. Rules wider
than the first task mean the next screens find their meanings already there. A styleguide written
before any screen has no audit to start from.
*Rejected:* the styleguide written on the first screen — that screen is built with no rules; a
minimal styleguide before the first screen, with only that screen's roles — every next screen adds
meanings in a hurry.

### WAY-185 — What does the styleguide skill look at first?

Before anything else, the skill `maintain-styleguide` recognizes which user interface the
styleguide is for and what the product already has for it — a file of design tokens its screens
read, one nothing reads, shared components, or nothing — and whether it has screens and a
styleguide, and it extends what exists rather than bringing a new system. A new library of
components or a new way of styling is a choice the skill leaves to the human as a question of the
task, never one it settles, showing the options by their consequences for the product — cost,
where they run, upkeep and the cost of changing later — with a recommendation and the weak point
of the option recommended, keeping the human's preferred tool as the recommendation (WAY-186) and
otherwise recommending the simplest and cheapest where no difference with a consequence remains
(WAY-123). A palette read from the code is a proposal, never a rule, until the product declares it
in a decision.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-121 · derives from WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: in a product whose file of design tokens holds two colours nothing reads, the skill
    proposes making the screens read that file and adding roles to it; a product with no shared
    components gets them in its existing styling, and the question of a library of components goes
    to the human with consequences, a recommendation and its weak point;
  - violates: the skill sets up a new library of components in a product that has its own design tokens;
    the skill chooses a styling technology itself or offers options without a recommendation;
    the colours the code uses become a rule of the
    styleguide with no decision of the product.
- **Origin:** none

*Rationale:* an existing system, even a worse one, beats a better one brought in, since the
screens already read it and a second one splits them in two. What the product has decides how the
skill works — before the first screen, an audit, or a refresh — so it is read first. A new library
is something the product has to keep, a technology choice, and the human makes it. A human who
cannot judge the library can weigh what it costs and where it fails; the recommendation gives a
way to take without deciding by technical names alone.
*Rejected:* a new system set up on a
product whose file of design tokens nothing reads — two systems side by side; the skill choosing a
new library itself — a dependency the human never chose; the palette the code uses taken as the
product's rule — an accident of the code becomes law (WAY-225); options with no recommendation —
the human is left to judge technology they cannot assess.

### WAY-186 — Where do a styleguide's starting rules come from?

The skill `maintain-styleguide` takes the starting rules of a user interface's first styleguide
from the human's preferences for its technology that the product's foundation settles, and, where
the human has none, from research of the basic rules for that technology, each source named with
its page and version and every difference no source supports refuted by a critique before the
human sees the rules, as the options of a technology choice are checked (WAY-122). It researches
at every extension and never at a refresh (WAY-251), and a tool the human prefers remains the one
proposed, never displaced by research. It adds the meanings of the screens the product announces —
in its definition, plan, specs and mockups — and proposes what the research finds without imposing
it.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-122 · derives from WAY-120 · derives from WAY-251
- **Verification:** an agent compares the work with the decision:
  - complies: the human has no preferences for a browser game's styling, research names the pages
    and versions of its library's documentation, a fresh critic strikes a claimed difference no page
    gives, and the starting set adds roles for the states the game's plan announces; a product
    with screens and no styleguide takes that same starting-set path alongside its audit; an
    extension runs research with the human's preferred tool kept as the proposal; a correction of
    existing roles refreshes the styleguide without research;
  - violates: the starting rules come from the agent's memory; a fixed list of roles from one course
    is used for every product; research reaches the human uncritiqued; an extension reuses the
    first research; a refresh runs research; research offers another tool in place of the human's
    preferred one.
- **Origin:** none

*Rationale:* the value of a styleguide has two layers, consistency and the quality of its rules,
and research with sources and a critique keeps the second, while preferences of the human come
first because the product is theirs. A fixed list in the-way would need keeping and would fit no
technology well, as the roles of one library and the palette of another differ; without the
product's own meanings one colour comes back in several meanings. New scope needs a check of
whether the existing tools fit it, while correcting accepted rules within their scope needs no new
comparison. Existing screens supply audit evidence, not preferences or a reason to skip research
where the human has none.
*Rejected:* a fixed starting list in the-way's template — a list to
keep, unfitted to the technology; preferences and research without the product's meanings — one
colour in several meanings again; research once for each product — later extensions miss current
recommendations; a source named with no critique, or rules from the agent's memory — the human
cannot tell a sound rule from an invented one; research at every refresh — an update within
accepted scope pays for a comparison it does not need.

### WAY-187 — How does the styleguide skill audit a product that has screens?

For a product that has screens, the skill `maintain-styleguide` audits the user interface in both
directions — from the source of values to the screens that read them, and from each value on a
screen to the design token or component meant to cover it — and ends with three to five charges, each
with its file and line and one sentence of its effect on the user, in four categories: a missing
design token, a missing shared component, accidental architecture, and a meaning, one colour
carrying several. The audit always asks what someone sees without data, straight from a link, after a
refresh, and it uses the agent's way to the running product where the product's foundation settles
one, otherwise auditing from the code and marking as unchecked what cannot be seen without the
running product.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: an audit charges that one green means both "can act" and "won", with the lines where
    each is drawn and what the player cannot learn from it, and that a screen opened from a link
    shows a blank page before it fills; with no decision on how an agent opens the screens, it marks
    the focus outline as not seen;
  - violates: the styleguide is written from the idea of the product with no audit of its code; the
    audit checks only screens with data; an audit with no way to the running product says focus is
    visible.
- **Origin:** none

*Rationale:* without an audit a styleguide writes down an idea of the product, not its code; each
direction finds what the other misses — a file of design tokens nothing reads, and a value no token
covers. A few charges with a place and an effect can be weighed by a human who is no specialist,
and the category of meaning holds the charge the other three miss, one colour in several meanings.
The standing question catches what a screenshot with data never shows. Logging in is a matter of the
product's behaviour, not of its styleguide, so the question leaves it out; a product with no decided
way to the running product is audited from its code rather than waiting for a task that settles it.
*Rejected:* a styleguide written with no audit — it describes the idea, not the code; the skill
stopped until the product decides the agent's way to the running product — the product waits for a
task that does not exist yet; "logged out" in the standing question — not a matter of the styleguide.

### WAY-189 — Which invariants does a styleguide start with?

The skill `maintain-styleguide` proposes, and the rules the template of the styleguide discipline
requires call for, a styleguide's first invariants, each checked by a cheap test of the product's
suite on a convention of its code: no file of the user interface's part holds a value written in
place of a design token; every control those files draw shows a visible focus; and every pair of a
background and its text reaches, with the values of the file of design tokens, the contrast that the
product's decision adopting WCAG takes (WAY-191). It proposes no invariant over the meanings of the
roles, which the review of each change compares with their decisions (WAY-168).

- **Scope:** product-guidelines, invariants
- **Based on:** none
- **Relations:** derives from WAY-168 · derives from WAY-191
- **Verification:** for what the skill proposes, an agent compares the work with the decision:
  - complies: a styleguide task proposes three invariants — the scan for values written in place of
    design tokens, focus on every control and contrast computed from the file of design tokens —
    each with its test in the product's suite, and leaves each role's meaning to the review;
  - violates: the contrast is judged by an agent looking at screenshots; the focus invariant is left
    out because the browser draws a default outline; an agent checks with k of n that each role
    keeps its meaning.
- **Origin:** none

*Rationale:* values written in place of design tokens, controls with no visible focus and text that
cannot be read on its background are the faults a styleguide meets first, and each can be decided by
a test reading the files and the file of design tokens, so none is left to the review. A meaning
cannot be read by a test, and the review that reads every change already reads it (WAY-168).
*Rejected:* focus and contrast left to the review or to an agent — a test decides them every time
for little; no invariants of focus and contrast at the start — the faults the styleguide is for go
unchecked; an invariant an agent checks with k of n, that no file of the part uses a role in a
meaning other than its decision gives — it costs more than the review that reads each change anyway
(WAY-168).

### WAY-191 — Where do a styleguide's thresholds of contrast and its demand of visible focus come from?

The skill `maintain-styleguide` takes the thresholds of contrast and the demand of visible focus from
WCAG through a decision of the product adopting it, which it asks the human for with the
recommendation to adopt the newest edition that is a W3C Recommendation when the decision is
written, named by its number as the W3C's page gives it at that time, at level AA, for every screen
of the user interface the styleguide covers, proposing another way only where the human chooses it
and writing nothing the human has not accepted. Each success criterion an invariant of the
styleguide takes a condition from stands as an environment fact the invariant rests on, with its
source as WAY-80 gives it.

- **Scope:** product-guidelines, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-86
- **Verification:** an agent compares the work with the decision:
  - complies: the skill says in plain words what contrast and focus are, recommends adopting the
    newest edition of WCAG the W3C's page names as a Recommendation that day, at level AA for every
    screen, and on the human's acceptance the task carries the decision and the facts of the
    contrast and focus criteria, each quoting the passage of that edition;
  - violates: a contrast invariant writes a ratio with no decision adopting WCAG; the edition is
    named from memory; the skill writes the adopting decision without asking because it recommends
    adopting.
- **Origin:** none

*Rationale:* a threshold written into an invariant with no adopted catalogue is a number from WCAG
without its source, and no reader can tell which edition it follows; adopted by a decision naming
edition, level and screens, the catalogue binds the product as WAY-86 gives it, and the facts carry
the criteria to the invariants (WAY-73). WCAG is a good standard and the human takes it unless
meaning to do otherwise, so the skill recommends adopting it, yet no decision enters without the
human. A law or a contract binds without adoption (WAY-86), so it is asked about before.
*Rejected:* thresholds of the product's own in an invariant's sentence with no adoption — a number
from WCAG with no named source or edition; no invariants of contrast and focus at the start — the
faults of focus seen in the first trial stay unchecked.

### WAY-192 — How does a product's instruction file lead to its styleguide?

A product's root `AGENTS.md`, outside the block the-way's installer writes, points to each styleguide
by its path in backticks with the condition of changing a file of the part it covers, and the rule
forbidding values written in place of design tokens in that part's files stands where the skill of
`instruction-files` places a rule for some files, saying what keeps it: the product's invariant,
or, while that invariant is marked violated, the review of each change to the part's files
(WAY-51); both are written as that skill gives them.

- **Scope:** product-guidelines, instruction-files
- **Based on:** none
- **Relations:** derives from WAY-128 · derives from WAY-129 · derives from
  WAY-133
- **Verification:** an agent compares the change with the decision:
  - complies: `AGENTS.md` reads "Before you change a file of `web`, read
    `guidelines/styleguide-web.md`" below the installer's block, and a rules file loaded with the
    files of `web` forbids values written in place of design tokens and names the invariant that
    checks it; in a product cleaning its screens gradually, whose invariant is marked violated, the
    same rule says that until the mark is cleared the review of each change to the files of `web`
    keeps it;
  - violates: the pointer stands inside the installer's block; the styleguide is imported with `@`;
    the rule names a lint command of its own; the rule stands in `AGENTS.md` for every session.
- **Origin:** none

*Rationale:* a styleguide no instruction leads to is not found by an agent in a new session; a path
with its condition costs one line and is read when the condition comes (WAY-129), and the pointer
leads to work an agent would not otherwise find (WAY-128). The rule concerns some files, so it
stands where the tools load it with them (WAY-128); it carries a decision the product records
(WAY-168), so it needs no recorded mistake (WAY-130), and it holds every time only through its
invariant, which the instruction says it is for (WAY-133); the gate runs that invariant, so the
instruction names no command of its own (WAY-16). While the invariant is marked violated, its test
stands as an expected failure and keeps nothing, so the instruction names the review of each change
as what keeps the rule until the mark is cleared (WAY-51). The pointer stands outside the
installer's block, which holds no path a product chooses (WAY-107).
*Rejected:* a styleguide with no way in from the instructions — an agent in a new session does not
find it; the rule as a line of every session — it costs context in each and is not followed every
time without its check.

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
  Do **not** copy it."; read 2026-10-18
- **Relations:** derives from WAY-172 · derives from WAY-198
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
behaviour would have the human judge code they do not judge. The status beside each path shows an
agent reading the guidelines what to copy and what not to, as Open Mercato's statuses do.
*Rejected:* approval of every change of the exemplar's behaviour — the human would judge code they
cannot judge; the status of the files kept in the decision alone — an agent reading the guidelines
would not see which files not to copy.

### WAY-200 — Who designates a product's exemplar for a kind of code, and when?

Where a product holds no file of a kind of code, the exemplar of that kind is designated by the task
that creates its first file. Where it already holds files of that kind, the skill
`maintain-coding-guidelines` judges every one of them, compares them and proposes the exemplar from
that comparison, with the status `copy` or `do not copy` of every other file, and the human approves
the decision that designates it.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-198
- **Verification:** an agent compares the work with the decision:
  - complies: in a product with nine endpoints the skill judges all nine, proposes the one that
    follows the product's rules best as the exemplar and marks two `do not copy`; a task that creates
    a product's first migration designates that migration as the exemplar of its kind;
  - violates: the oldest endpoint becomes the exemplar with no comparison; the exemplar waits until
    someone asks for it while agents copy what they find; the skill writes the designating decision
    with no approval of the human.
- **Origin:** none

*Rationale:* who designates the exemplar follows from the state of the product, as the styleguide
comes before the first screen (WAY-184) and the audit reads a product that has screens (WAY-187): a
first file built with no exemplar is the file every later one copies, and with several files a
choice made without comparing them makes whichever file an agent finds into law (WAY-225). The price
is one more way of working for the skill.
*Rejected:* the exemplar designated only by the task that creates the first file — it says nothing of
a product that already has several; the exemplar designated after the fact by a separate decision
once several files exist — until then every agent copies what it finds.

### WAY-201 — How does the coding-guidelines skill's audit of a product with code end?

The audit the skill `maintain-coding-guidelines` makes of a product that has code ends with a
proposed exemplar for each kind of code the product holds files of, each with one sentence of what
the product gains by it, and with the files of that kind marked `do not copy`, each with the file and
line of the place that breaks a rule.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-200
- **Verification:** an agent compares the work with the decision:
  - complies: the audit proposes for the kind `endpoint` the file `src/api/orders/route.ts`, "every
    new endpoint checks its input as this one does", and marks `src/api/legacy/users.ts` `do not
    copy` at its line 42, where it reads the request's body unchecked;
  - violates: the audit ends with the linter's reports listed by the names of their rules; a file
    stands as `do not copy` with no line; an exemplar is proposed with no word of what the product
    gains.
- **Origin:** none

*Rationale:* the human who approves the exemplar does not judge code, and a proposal with what the
product gains, and a fault with its place, can be weighed by someone who is no developer, as the
styleguide's audit ends with charges of a place and an effect (WAY-187); the place also shows the
next agent where not to copy from.
*Rejected:* what the audit found shown as a comparison of the files' code — the human cannot weigh
it.

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
- **Relations:** derives from WAY-202
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
decision adopting the set (WAY-207), put to a human who does not judge code; Google blocks a change
only by a check that gives no report its developers would not act on. A report that is
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
while fewer than one report in ten leads to no change, as Google allows for checks shown in code
review — the gate sometimes blocks sound code, and only a change of a decision passes it; a rule
that gives such reports kept as a check that only warns — it changes what results the gate knows
(WAY-63); only rules of correctness blocking, never rules of style — a remark on style never blocks
in the review of code (WAY-161), and the human does not judge style; a script of the product's own
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
tool's documentation states, about one thing, with one reason to change, a new edition (WAY-76), as
git's rule of path patterns with its page's exceptions is one fact. A criterion of WCAG stands as a
fact of its own (WAY-191) because each is a requirement of its own written in prose, while a rule of
a linter's set is one whose content the tool itself runs at its pinned version, so the invariant
needs the set's membership alone. The price is a trial run and a judgment of its reports each time a
set is adopted.
*Rejected:* every rule of the set blocking — the gate blocks sound code (WAY-203); the human
deciding rule by rule — the human would judge what they cannot judge (WAY-174); an environment fact
for each rule of the set — many facts with one source and one reason to change (WAY-76).

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
whole tree of a product's dependencies.

- **Scope:** product-guidelines, invariants
- **Based on:**
  https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/.github/workflows/audit.yml
  § lines 23-24 — "The ci.yml job passes `--baseline <base yarn.lock>` so a change fails only on
  advisories it introduces."; read 2026-10-18
- **Relations:** derives from WAY-202 · derives from WAY-60
- **Verification:** an agent compares the work with the decision:
  - complies: a change that adds a library at a version with a known vulnerability of high severity
    fails in a product whose decision sets high; a change to a page's text passes on the morning an
    advisory is published for a dependency the product already holds; a product whose human chose
    every severity fails a change bringing in a version with an advisory of low severity;
  - violates: the audit reads the whole tree on every change, and a change unrelated to the
    dependencies fails on an advisory published that morning; the template sets the threshold at
    high for every product; the audit reads a copy of the database the product committed months
    before; the template carries an audit of the whole tree of dependencies run every day.
- **Origin:** none

*Rationale:* an audit of the whole tree at every change fails a change that touches no dependency on
a vulnerability published that morning, so the audit checks what the change brings, against the fork
point, as Open Mercato's audit compares with a base. The severity from which a
vulnerability counts and the database read are conditions of the product's invariant, so they stand
in the decision that adopts the audit (WAY-60), and the severity is the product's choice, every
severity among the ways. The tools stand at pinned versions, while the database is read as it stands
when the check runs, so that a change brings in nothing known to be vulnerable that day. Two weak
points follow. A vulnerability found in a dependency the product already holds gives no signal while
no change brings in a version of it. A later run on the same commit may record `fail` where an
earlier one recorded `pass`, when an advisory is published for a version that commit brings in; such
a check is answered as WAY-68 gives it, which this decision leaves unchanged.
*Rejected:* the whole tree audited at every change — an unrelated change fails on a vulnerability
published that morning; a copy of the database the product commits — nothing moves it apart from a
change, so it ages without bound, and a change bringing in a version first flagged after it passes;
WAY-68 narrowed so that a later `fail` on the same commit is no check giving different verdicts — a
new meaning of WAY-68 for a rare case; a fixed threshold of severity for every product — the
severity is the product's choice.

### WAY-207 — Where is a fault of one file of a product's code fixed?

The template of the coding discipline has a product's coding guidelines hold that a fault of one
file is fixed in that file, never by turning a rule of the linter off for the whole product nor by
changing the exemplar for that file's sake, and that turning a rule of the linter off for the whole
product is a change of the product's decision adopting the linter's set, which the human approves as
WAY-172 gives a changed meaning.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-172 · derives from WAY-173
- **Verification:** an agent compares the change with the decision:
  - complies: a new endpoint that the linter flags for an unused import loses that import; a team
    that finds a blocking rule wrong for the product changes its decision adopting the set with the
    human's approval, and only then the rule is turned off in the linter's configuration; the review
    of a change that turns a rule off in the configuration with no change of the decision asks for
    the decision;
  - violates: a rule is turned off in the linter's configuration so that one change gets through;
    the exemplar is changed so that a new file departing from it passes the rules a script checks
    from it.
- **Origin:** none

*Rationale:* a rule of the linter reads every file of the parts it covers, so turning it off for one
file's sake changes what binds all the others, unseen by the task that made the change, and the
exemplar is what every later file of its kind follows; a fix in the file stays where the fault is. A
blocking rule gives no report that leads to no change worth making (WAY-203), so a report of it is a
fault to fix, and a rule wrong for the product is a matter of the decision that adopted it, as a
global design token is for a styleguide (WAY-178). The configuration changes in a few files a review
reads with every change to them, and the tool, pinned with its set unchanged, already runs the rules
the decision names. The price: a rule turned off in the configuration with no change of the decision
is caught only as surely as the reviewer reads that change.
*Rejected:* a rule turned off in the linter's configuration so that one change gets through — every
other file loses the rule unseen; a second invariant keeping the linter's configuration to the
decision's rules that block — a check of a list the review of each change to the configuration
already reads.

### WAY-208 — Which parts of a product get coding guidelines?

The skill `maintain-coding-guidelines` proposes coding guidelines for every part of a product's map
that holds code, the scripts of its build included, however small that part is, and the general file
of its coding guidelines names each such part in *Applies to*.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: a product with a backend, a client in the browser and a part holding its build scripts
    names all three in *Applies to* of `guidelines/coding.md`, and its standing checks read the code
    of all three;
  - violates: the skill passes over the part of build scripts because it is small; the general file
    names only the backend because its kinds of code live there.
- **Origin:** none

*Rationale:* an agent left free does something different in every task, and that is what guidelines
are for; even guidelines of modest quality are consistent, as for the styleguide of every user
interface (WAY-183), and a small part of code drifts as surely as a large one. The general file
holds what binds the whole of the code once (WAY-167), so the parts it covers are the parts its
standing checks read.
*Rejected:* no coding guidelines for a small or helper part, such as the scripts of the build — each
task writes it its own way.

### WAY-209 — When do a product's coding guidelines come into being?

The skill `maintain-coding-guidelines` proposes that, in a product with no code, the general file of
its coding guidelines, with its standing checks, comes into being before the first task that writes
the product's code, and that the file of a kind of code comes into being with the task that creates
the first file of that kind.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the work with the decision:
  - complies: a product whose plan brings its first code gets a task of coding guidelines first,
    which adopts a linter, a formatter and an audit of dependencies before any code exists; the task
    that writes the product's first migration writes `guidelines/coding-migration.md` with that
    migration as its exemplar;
  - violates: the linter and the formatter are brought in once the first code is written; a file of
    the kind `endpoint` is written while the product holds no endpoint.
- **Origin:** none

*Rationale:* the first code written with no standing check is the code every later change copies,
and checks brought to it afterwards find code to clean (WAY-205), as a first screen built with no
rules is the one every later screen copies (WAY-184). A file of a kind holds its exemplar, which
exists only once the task that creates the first file of the kind has designated it (WAY-200).
Coding guidelines written before any code have no trial run to start from (WAY-204).
*Rejected:* the linter and the formatter brought in only after the first code is written — that code
is written with no standing check, and they meet it as code to clean.

### WAY-210 — What does the coding-guidelines skill look at first?

Before anything else, the skill `maintain-coding-guidelines` recognizes which parts of a product
hold code and what the product already has for them — a linter, a formatter, an audit of
dependencies, kinds of code that already have files, or nothing — and whether it has coding
guidelines, and it extends what exists rather than setting a second tool beside it. A new linter,
formatter or audit of dependencies is a choice the skill leaves to the human as a question of the
task, never one it settles, showing the options by their consequences for the product — cost,
where they run, upkeep and the cost of changing later — with a recommendation and the weak point
of the option recommended, keeping the human's preferred tool as the recommendation (WAY-211) and
otherwise recommending the simplest and cheapest where no difference with a consequence remains
(WAY-123).

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-121 · derives from WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: in a product whose linter runs with a few rules, the skill proposes adding rules to
    that linter's configuration; a product with no standing check gets three questions, each
    showing the consequences with a recommendation and its weak point, and recommending the
    simplest and cheapest where no difference with a consequence remains;
  - violates: the skill sets a second linter beside the one the product runs because it judges it
    better; the skill chooses a formatter itself; a tool is recommended only because it is the
    most used, although another has better consequences for the product.
- **Origin:** none

*Rationale:* an existing tool, even a worse one, beats a better one brought in, since the code and
the people working on it already follow it, and two linters over one code disagree, as for a
styleguide's system (WAY-185). What the product has decides how the skill works — before the first
code, an audit, or a refresh — so it is read first. A new tool is something the product has to
keep, a technology choice, and the human makes it. The human is no developer, so a recommendation
through consequences gives a way they can weigh and take as offered, with its weakness visible.
Wide use can bear on those consequences (WAY-122), but cannot replace them.
*Rejected:* a second
linter set beside a product's working one because the skill judges it better — two tools over one
code disagree; the skill choosing a new tool itself — a dependency the human never chose; the
most-used tool as the default recommendation — popularity alone says nothing of whether the
product benefits; options with no recommendation — the human is left to judge technology they
cannot assess.

### WAY-211 — Where do the tools of the standing checks and a linter's set of rules come from?

The skill `maintain-coding-guidelines` takes the tools of the standing checks and a linter's set
of rules from the human's preferences for the product's technology that the product's foundation
settles, and, for the first coding guidelines where the human has none, from research of each
standing check for that technology, each source named with its page and version and every claim no
source supports refuted by a critique before the human sees the options, as the options of a
technology choice are checked (WAY-122). A tool the human prefers remains the one proposed, never
displaced by research. The skill researches at every extension and never at a refresh (WAY-251).

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-122 · derives from WAY-120 · derives from WAY-251
- **Verification:** an agent compares the work with the decision:
  - complies: the human has no preference for the linter of a product written in TypeScript;
    research names the pages and versions of the tools' documentation and of a record of their use,
    a fresh critic strikes a claimed difference no page gives, and only then the human sees the
    options; an extension runs research with the human's preferred tool kept as the proposal;
    adapting the existing guidelines to a new tool version refreshes them without research;
  - violates: the tools come from the agent's memory; research reaches the human uncritiqued; an
    extension reuses the first research; a refresh runs research; the skill offers another tool
    in place of one the human named as preferred.
- **Origin:** none

*Rationale:* the product is the human's, so their preferences come first; where they have none,
research with sources and a critique lets a human who cannot judge the tools tell a sound
comparison from an invented one (WAY-122, WAY-120), as for a styleguide's starting rules
(WAY-186). New scope needs a check of whether the existing tools fit it, while updating or
correcting accepted rules within their scope needs no new comparison.
*Rejected:* tools and sets
proposed from the agent's memory — the human cannot tell a sound proposal from an invented one;
research once for each product — later extensions miss what has moved; research at every refresh —
an update within accepted scope pays for a comparison it does not need.

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
  WAY-167
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
gains, while the general file's table, as Open Mercato's table leading from a task to the guides to
read leads the agent in a second step to the files of the kinds its work touches. The
price: two steps instead of one, and a table that could drift from the files, which only the review
of a change that adds or removes a kind's file catches (WAY-170). The pointer stands outside the
installer's block, which holds no path a product chooses (WAY-107), and the gate runs the standing
checks, so the pointer names no command of its own (WAY-16). The table itself is what WAY-167 gives
the general file; this decision sets how it leads.
*Rejected:* a line of `AGENTS.md` for each file of the coding guidelines, as WAY-192 has for each
styleguide — `AGENTS.md`, loaded into every session, grows with each kind; no pointer, leaving the
way in to the task cycle — a session outside that cycle can miss them.


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
- **Relations:** derives from WAY-167 · derives from WAY-171 · derives from
  WAY-150 · derives from WAY-36
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


### WAY-214 — How does task refinement find missing product guidelines?

The skill `refine-task` uses the reading the agents of the task cycle use,
`product-guidelines/reading.md`, to find guidelines by the affected parts' *Applies to* and a kind
of code by its row in the general coding index, the table of `guidelines/coding.md`, with the
consequence of an absence following when the discipline's guidelines come into being (WAY-184,
WAY-209, WAY-244).
Before a diff exists, it identifies affected parts, user interfaces, code, kinds of code and whether
the work writes or changes tests from the required behaviour, the responsibilities of the part map
and existing product files, expanding its reading and exposing unresolved classification or
malformed metadata as a question rather than an empty match.
An existing general coding file whose *Applies to* omits an affected code part is read for
extension in the current task, not treated as an absent file.

- **Scope:** project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-150 · derives from WAY-167 · derives from
  WAY-171 · derives from WAY-183 · derives from WAY-208 · derives from
  WAY-213
- **Verification:** an agent compares refinement and its reading with the decision:
  - complies: an announced admin panel is recognized before its files exist; the same lookup
    finds the missing styleguide and an unindexed kind; an omitted part extends existing coding
    guidelines; an absent indexed file is named as a discrepancy; a fix whose required behaviour
    needs a new test is recognized as writing tests in a product with no testing guidelines;
  - violates: each discipline uses an unrelated lookup; helper code is passed over because it is
    small; an uncertain kind is silently considered covered; an omitted part creates a false wait
    for a new general coding file; a task that changes a test is classified only by the code it
    touches.
- **Origin:** none

*Rationale:* discovery repeated per discipline drifts from what the later cycle reads. Recognizing
the work before implementation lets refinement find its missing ground, at the cost of judgment
about prospective responsibilities; visible uncertainty leaves that judgment open to correction.
*Rejected:* separate discovery for each discipline — later additions bring another place to keep
consistent; classification from names alone — a helper can contain code and a backend can draw
screens without its name saying so.


### WAY-215 — What happens to a task that needs missing discipline guidelines?

Unless a departure under WAY-217 applies, a task changing a user interface with no styleguide,
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
  WAY-184 · derives from WAY-209 · derives from WAY-217 · derives from
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
gains in *To do* the designation of that kind's exemplar under WAY-200 and its kind guidelines
with their index row, without waiting for a separate exemplar task.
Where files of the kind already exist, refinement records that discrepancy and routes exemplar
selection through the comparison WAY-200 gives existing code, rather than treating the next file
as the first.

- **Scope:** project-level, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-200 · derives from WAY-209
- **Verification:** an agent compares the task and existing code with the decision:
  - complies: the task adding the first migration also designates its exemplar and writes its
    kind guidelines and index row; existing unindexed endpoints go through comparison;
  - violates: the first migration waits for an exemplar that cannot exist before it; existing
    endpoints are ignored and the next endpoint is called the first.
- **Origin:** none

*Rationale:* the first instance supplies the material an exemplar needs, so separating its
designation would create a circular wait. Existing instances instead need comparison, or the next
one becomes a model without being judged against what the product already holds.
*Rejected:* blocking every unindexed kind — a genuinely first instance could never arrive;
designating the next instance regardless of existing code — it bypasses comparison.


### WAY-217 — Does an approved departure count as missing guidelines?

The shared reading of product guidelines treats no absent discipline file as missing for the
affected part where a current decision of the product's log departs from those guidelines for
that part, and applies that departure only within the scope the decision gives it.

- **Scope:** project-level, product-guidelines, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the reading and departure with the product's decisions:
  - complies: an approved departure for helper scripts removes their missing-guidelines finding
    while an affected browser interface still needs its own styleguide;
  - violates: a deliberate departure still blocks every task until the rejected guidelines are
    written; a departure for one part silently exempts another.
- **Origin:** none

*Rationale:* a product can knowingly decline guidance through its own decision, and forcing its
creation afterwards would cancel that choice. The price is that the departure removes the
protection for later work too, which is why its stated scope matters.
*Rejected:* no departure respected by discovery — an accepted product choice could never be used;
a departure inferred by the agent — absence would authorize itself.


### WAY-218 — Where does project breakdown place missing guidelines and first-kind work?

The skill `plan-project` uses the same reading of product guidelines as refinement and the task
cycle, and places a task for a missing styleguide, general coding guidelines or testing guidelines
before the tasks that need it, with those tasks depending on it, reusing an adequate task the plan
already holds, and one guidelines task may carry both missing coding and testing guidelines
(WAY-247).
It places the designation of the exemplar and kind guidelines with the task creating that kind's
first file, under WAY-216, and the designation of a level's exemplar test with a task whose required
outcome is itself that level's first test (WAY-242), while changes beyond the approved definition
follow the existing definition and plan approval route.

- **Scope:** project-level, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-143 · derives from WAY-144 · derives from
  WAY-184 · derives from WAY-209 · derives from WAY-214 · derives from
  WAY-216 · derives from WAY-244 · derives from WAY-242
- **Verification:** an agent compares the breakdown with the definition and product:
  - complies: the screen tasks depend on the missing styleguide task, while the first migration
    task carries its exemplar work; a new product's first code task depends on one task writing
    both its coding and its testing guidelines; the task whose outcome is the product's first
    end-to-end test carries the designation of that level's exemplar test; a suitable existing
    prerequisite is reused;
  - violates: guidance is discovered only when the first screen task is refined; a preparatory
    task has no consumer; the plan silently enlarges the approved scope; a separate task waits to
    designate a level's exemplar test before any test of that level exists; the plan assigns a
    level's exemplar test to a task whose tests its cycle chooses.
- **Origin:** none

*Rationale:* discovering the prerequisite during breakdown makes the dependencies visible before
work is handed out; refinement remains useful for work outside a project and for later omissions.
The cost is applying the shared reading at another point, rather than revising the plan when its
first consumer reaches refinement.
*Rejected:* discovery left to refinement alone — the initial breakdown lacks a prerequisite its
own consumers already need; separate exemplar preparation — the material is made by its consumer.


### WAY-219 — What does an author check before a user-interface change reaches review?

Before review, the author of a one-author change and the executor of a slice changing a user
interface check the affected components' states required by the product's applicable styleguide,
beside the check of WAY-164, and inspect a screenshot through the agent's way to the running
product that its foundation settles.
Where the foundation settles no such way, they inspect the states in code and mark the screenshot
unchecked for that reason in their report and the request; a settled way that fails keeps its
actual failed or unperformed check rather than that reason.
The report records what was checked, how, what was observed and the screenshot evidence where
obtained, without treating a code inspection as evidence of rendered appearance.

- **Scope:** task-cycle, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-164 · derives from WAY-177 · derives from
  WAY-187 · derives from WAY-165 · derives from WAY-173
- **Verification:** an agent compares the author's evidence, review and request with the decision:
  - complies: an author checks the states the adopted styleguide requires and inspects a
    screenshot; with no settled way it inspects code and names the unchecked screenshot in both
    places; a failed settled way is reported as that failure;
  - violates: a passing suite replaces the state check; a default-state screenshot stands for all
    required states; code inspection is called proof of visible focus; absent access is hidden.
- **Origin:** none

*Rationale:* states beyond the default are easy to omit, and rendered appearance can differ from
what source inspection suggests. Looking at both catches different faults before review; where
the running product cannot be reached, exposing the remaining gap lets the human weigh it without
inventing a new technology choice inside the task.
*Rejected:* state and screenshot checks left to the reviewer — faults reach review that the author
can catch; stopping the cycle for an unsettled way to the interface — it creates another blocker
after the change is made; code inspection described as rendered evidence — the gap disappears; a
comparison with reference screenshots — every intended change of how a screen looks would also
take new reference shots, a cost the check of states and a screenshot does not bring.


### WAY-220 — How does a code reviewer grade a finding about appearance?

A code reviewer grades a finding about appearance by its concrete effect on the user, within the
review's existing severity scale, rather than treating it as Minor merely because it concerns
appearance; the reviewer retains the grade and scope decisions WAY-161 assigns it.

- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-161
- **Verification:** an agent compares the finding and its grade with the visible consequence:
  - complies: a colour that makes a destructive action look harmless is judged by that consequence;
    a visual difference with no blocking consequence can remain Minor;
  - violates: an appearance defect is called Minor solely because it is visual; every visual
    difference is automatically blocking; the orchestrator changes the reviewer's grade.
- **Origin:** none

*Rationale:* appearance can carry the meaning by which a person chooses an action, so a visual
fault can change behaviour as seriously as incorrect code. Its consequence supplies the
distinction without introducing another severity scale or moving judgment to the author.
*Rejected:* appearance always minor — a misleading action survives review as polish;
appearance always blocking — harmless differences cost a repair round.


### WAY-221 — When can departure from a guideline example support a blocking finding?

Departure from an example in product guidelines or from the part of an exemplar no script checks
is not by itself grounds for a blocking review finding: the reviewer names the consequence for
the user or for code correctness that warrants the blocking grade under WAY-161.
Binding rules and their invariants retain their force, and this criterion gives the orchestrator
no authority to regrade or discard a reviewer's finding.

- **Scope:** task-cycle, product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-168 · derives from WAY-198 · derives from
  WAY-161
- **Verification:** an agent compares a finding with the guideline and named consequence:
  - complies: a different internal arrangement is not blocking merely because the exemplar uses
    another; a departure causing incorrect input handling is graded by that effect;
  - violates: the reviewer blocks only because the example was not copied; the orchestrator
    discards an Important finding by calling the cited material an example.
- **Origin:** none

*Rationale:* examples teach useful ways without acquiring the force of approved rules, and
comparison without a concrete consequence turns taste into a blocker. The price is that some
consistency can drift until a recurring problem warrants a rule with its own invariant.
*Rejected:* leaving the distinction unstated in review — examples acquire binding force in use;
letting the orchestrator decide which findings count — the agent closing the work judges its own
obstacle.


### WAY-225 — What in a product's foundation is derived rather than written by hand?

What can be derived from what the product executes — code, configuration, infrastructure as code,
runtime traces — is derived, never written by hand, and what is derived describes the state. Rules
are written by hand: what is allowed and what the product promises, which the code cannot show, and
a dependency the code holds that the part map does not allow is recorded as an invariant the
product does not meet (WAY-51), never by rewriting the allowed dependencies to fit the code.

- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** invariants: derived-file-content. For what is derived and what is written by
  hand, an agent compares the change with the decision:
  - complies: the map's allowed dependencies are written by hand, and the return step compares
    them with the dependencies the code holds; a dependency of the code that a human accepts
    although the map does not allow it stands as the invariant "the part `ui` does not depend on
    `storage`", marked violated;
  - violates: a hand-written architecture document appears next to the part map; a hand-written
    list of the product's endpoints kept next to the code; the allowed dependencies in the part
    map copied from the current import graph.
- **Origin:** none

*Rationale:* a hand-written copy of the state goes stale, and code shows only what exists: a view
derived from it shows accidents as architecture, a rule copied from it turns one into law.
*Rejected:* a hand-written architecture document or diagram — a second copy of the map; "do not
write by hand what can be derived from code" as the whole rule — it reads as a demand to derive the
map's rules; derivation from code alone — behaviour shows in runtime traces, deployment in
infrastructure files.

### WAY-226 — Which glossary holds a word of the process, and which a word of a product's domain?

The glossary of the-way holds the words of the process, and a product's glossary holds the words of
its domain; a product takes the words of the process from the-way at the commit it pins and defines
none of them again, and in the-way, whose product is the process, the two are one file.

- **Scope:** glossary, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a game's glossary defines "level" and uses "return step" as the glossary of the-way
    defines it at the pinned commit;
  - violates: a game's glossary gives "return step" a definition of its own; the glossary of the-way
    defines "level" as the game uses it.
- **Origin:** none

*Rationale:* a definition of a word of the process stands once, in the-way, because copies drift
between products.
*Rejected:* each product defining the words of the process in its own glossary — the copies drift
between products.

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
- **Relations:** derives from WAY-173 · derives from WAY-231
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
a test (WAY-246). A property test checks a relation over many generated inputs, so its expected value
is that relation, and developers apply such tests where a relation lies at hand — a pair of inverse
functions, a reference implementation, a condition kept after every step. The relation holds only
where the code under test does not compute it: a simpler version copied from the code makes the
test a mirror of it, which only the reviewer catches. A counterexample written out stays checked on
every run, whatever the generator draws next. The price: the rule is longer.
*Rejected:* the expected value alone written out — the input still moves with the code; a line
naming each file a test's verdict leans on, in place of values written out — every tracked file
becomes the data of some test; the rule left in the coding guidelines — a test written apart from
code meets no rule; no property tests — a whole class of tests that check a relation over many
inputs is barred; the rule left silent on property tests — a generated input breaks its letter, and
nothing says what holds instead.

### WAY-229 — On which class of model do the executor of a slice and the one author work?

The executor of a slice, and the one author of a change without a plan, work on the class of model
set for them, named in general terms and never by the name of a model: by default a class cheaper
than the orchestrator's, for code that carries settled matters into the product, ordinary
implementation that takes decisions of its own included; the orchestrator's class, for a change
across many parts; or the strongest class available, for one that needs design — each class other
than the default with one sentence of its reason. The planner sets each slice's class in the plan;
the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure,
and records it with its reason. The one author writes its foundation entries, takes its return step
and fixes its findings on its own class. An executor that returns `blocked` for a fact or permission
no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical
check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh
executor one class higher, from the slice's base, given the failed executor's report and what
failed; and an executor of the strongest class that fails, or a retry that fails, stops the cycle.
The fix of a slice's findings runs on the class of the executor whose work stands, of findings in
several slices on the highest of their classes and of a planned change's finding of no slice on the
orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's
foundation entries, the return step of a planned change and every reviewer — the review of the whole
change and the review of the return step included — work on no class cheaper than the
orchestrator's.

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
- **Relations:** derives from WAY-136 · derives from WAY-148
- **Verification:** an agent compares the plan, the record of slices and the dispatches with the
  decision:
  - complies: the plan sets the default class for a slice that applies a pattern the spec settles
    and for one of ordinary implementation that takes decisions of its own, the orchestrator's
    class with its reason for a slice that joins several parts, and the strongest with its reason
    for one that needs design; the record gives the one author's class, with its reason where it is not
    the default, and the
    author writes its foundation entries, its return step and its fix on that class; an executor of
    the cheaper class whose check fails is replaced, from the slice's base, by one of the
    orchestrator's class given its report and the failure; the fix of a reviewed slice's finding
    runs on the class of the executor whose work stands; the review of the whole change runs on the
    orchestrator's class or a stronger one;
  - violates: a plan names a model by its product name; a class other than the default stands
    without its reason; a failed executor is retried on the same class or a second time; an
    executor of the strongest class gets a retry; a review or the spec runs on a class cheaper than
    the orchestrator's; the one author works on the orchestrator's model with no class recorded.
- **Origin:** none

*Rationale:* a slice's handoff carries its settled requirement word for word, so much of a planned
change is the carrying of settled matters into code, which a cheaper model can do at a fraction of
the cost. Ordinary implementation within a settled task, spec and plan is within that reach too —
unlike the source, which keeps typical implementation on the default tier — and
the one author's change is bound by the same settled task; the reviews of the whole change and of
the return step, on the orchestrator's class, are what finds a cheaper model's error in code, in a
foundation entry or in the return step. The planner, who cut the slice, knows best what it demands,
and on the route without a plan the orchestrator, who judged that one agent can hold the change,
knows what that agent faces. A failure gets one retry a class higher before the cycle stops, which
costs less than running every slice on the strongest class and less than stopping at the first
failure of a cheaper one; the slice's own review where it has one, and the review of the whole
change, find what a cheaper model got wrong. Classes in general terms survive the release of new
models and fit any harness.
*Rejected:* every slice on the orchestrator's model — it pays the strongest price for transcription;
the orchestrator's class for ordinary implementation, or for the one author by inheritance — it pays
the strongest price for code whose decisions the task, the spec and the plan already bound; the
class chosen by the orchestrator at each dispatch of a slice — it judges again what the planner
judged when it cut the slice; the return step of the one author handed to a fresh agent of the
orchestrator's class — it pays a second agent to read the foundation again, while the review of the
return step judges it on that class; the orchestrator's class as the default — it leaves the cheaper
class to a judgment made slice by slice and rarely taken; retries without bound, or on the same
class — the same failure repeats at the same cost; a cheaper class for the spec, the plan or a
review — their errors reach every later step; model names in the process — they age with every
release.

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
- **Relations:** derives from WAY-173
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
so one rule covers them all, and the list of weakenings, as Open Mercato's review checklist gives
it, lets a reviewer recognize them. A test that was wrong may rightly change, so the rule asks for
the cause and its evidence rather than forbidding the change.
*Rejected:* existing tests never changed — a wrong test could never be corrected; a cause asked only
of a changed expected value — a skip or a looser assertion masks the same defect; a test replacing
an old one required to be seen failing on the code before the fix — a ritual of its own for each
ordinary test, where only an invariant's test is seen failing once (WAY-08).

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
- **Relations:** derives from WAY-173 · derives from WAY-233
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
verdict on the same code every time. A judge's verdict varies from run to run and costs more, so a
deterministic check comes first and a judge only where none exists, as Anthropic recommends for the
evaluation of agents; checked on examples a human judged and pinned to one model, its verdict can be
trusted as far as those examples reach. A tool that heals a test by changing what it asserts fits
the test to a state that may be wrong, the masking WAY-233 names. AI tools change faster than the
rest of what a product runs, so the version and the date read let a reader see what a test stands
on. The price: checking a judge takes examples a human judged, repeated runs multiply the cost of a
run, and the conditions are carried over from the evaluation of agents to a product's tests as an
inference.
*Rejected:* an AI judge barred from permanent tests — a behaviour no plain comparison can check
stays untested; guidelines silent on AI — each task lets AI into tests on terms of its own.

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
- **Relations:** derives from WAY-173
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
missing check is the fault itself, so it is never excluded. The 10xDevs course on agentic
development keeps such a section, what is deliberately not tested, in its plan of tests, each item
with its reason and the change that calls for its re-evaluation; here it stands in a product's
guidelines, since a task's refinement holds no plan of tests (WAY-238). The kinds of tests without
value the template gives among its examples — a duplicate of a stronger test, a test that pins
trivial constants, a loop over nearly identical inputs — come from how Limen trimmed its own tests
(https://raw.githubusercontent.com/overment/limen/89ef3786a6c2f893b2d31cd9944ad76c483f7841/spec/features/done/2026-10/F776-trim-low-signal-tests/notes.md
§ What was cut — "Duplicates. The same rule was proven twice. The stronger, end-to-end test stays." ·
§ What was cut — "Trivia. Tests that pin constants" · § What was cut — "Variants. Loops over
near-identical inputs shrank to representative cases"; read 2026-10-25), and as examples they bind
nothing. The price: each exclusion is a decision to approve, and the section ages where nobody
checks its conditions.
*Rejected:* exclusions held only as decisions of the log, with no section in the guidelines — an
agent writing tests does not find them where it reads; items giving their reasons with no
decision — an exclusion binds with no approval; a single test as an item — the section becomes a
list of excuses.

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
in computation or in its connections.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-226
- **Verification:** an agent compares the guidelines of a product with the decision:
  - complies: a game's guidelines name its levels unit, integration and end-to-end, its glossary
    defines "integration test" as a test that may touch files and a local server and no browser,
    and the table of levels names that term without copying it; the guidelines say that the
    simulation's complexity lies in computation and the account server's in its connections;
  - violates: the guidelines use "integration" with no glossary entry while their integration
    tests open a browser; the table of levels repeats the definition the glossary holds; a level is
    defined as "tests several parts together".
- **Origin:** none

*Rationale:* "unit" and "integration" mean different things to different teams, and much of the
dispute over the right mix of tests is a dispute over the words; a level defined by what its test
may touch can be checked without judgement. A word that means something of its own in the product is
an entry of its glossary (WAY-95), where it is defined once and keeps one meaning in the guidelines
and in the tests. Where a part's complexity lies tells which level catches its breaks: computation
shows in tests that touch nothing outside the code, connections only in tests that reach them.
*Rejected:* each level defined in the guidelines' own table — a second definition beside the
glossary, and the two drift apart; the meaning of "integration" left to each reader — tests of one
name touch different things.

### WAY-241 — What does the recipe of a test level hold?

The template of the testing discipline gives a product's testing guidelines, for each level, a
recipe of the same fields — what the level is for and when not to use it, where its files lie and
how they are named, the name and build of a test, its doubles, its data, time and randomness, the
level's exemplar test, the command and the time limit — each field that binds naming the product's
decision that carries it, a field naming none standing as an example, and a field that repeats
another level's reading "as in <level>". The field of the command names the gate and how it narrows
to the level, a file or a test, where the gate can, and otherwise reads `none`; the field of the
time limit points to the configuration file that holds it; and no recipe lists commands of the test
tool of its own.

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
    the time limit reads "5 s"; a field of doubles binds a change while it names no decision.
- **Origin:** none

*Rationale:* the same fields for every level let an agent find what binds at any level in one place,
and a small product writes a field once and points to it from the others. A field binds only where a
decision of the product carries it (WAY-168), so the template's defaults for the build of a test,
its doubles, its data and its time are proposals a product adopts or departs from. One command runs
every test (WAY-16), so the recipe gives that command and how far it narrows, and a command of the
tool beside it would be a second list that drifts; a product whose gate cannot narrow gets narrowing
only by a change of its code. A time limit copied into the guidelines goes stale beside the
configuration that holds it. The default order of doubles — the real thing where it is fast,
deterministic and simple, then a working simpler version, then a stub or a mock — follows the
preference for real implementations, with a check of a call kept for an effect outside the product.
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
- **Relations:** derives from WAY-173 · derives from WAY-200 · derives from WAY-172
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
- **Relations:** derives from WAY-173 · derives from WAY-68 · derives from WAY-233
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
as surely as a test skipped for a failing change, so it takes the same cause and evidence. WAY-68
gives the test of an invariant the same answer.
*Rejected:* a quarantine of flaky tests, with a limit for fixing them — a second state of tests to
keep, which ages, as WAY-68 refuses it for the tests of invariants; automatic runs again in the gate
— the fault stays hidden; every flaky test fixed before the next change — unrelated work stops for
it.

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
screen built with no rules is the one every later screen copies (WAY-184), and guidelines brought to
them afterwards meet tests to rewrite. The price: a pressing fix in a product with no testing
guidelines waits for them too, and every task with code in such a product waits for the task that
writes them.
*Rejected:* the testing guidelines written from the first test — that test is written with no rules;
the testing guidelines written by the first task that needs them — they shrink to that task's needs.

### WAY-245 — How does a product's instruction file lead to its testing guidelines?

A product's root `AGENTS.md`, outside the block the-way's installer writes, points to its testing
guidelines by one line naming `guidelines/testing.md` by its path in backticks with the condition of
writing or changing a test, written as the skill of `instruction-files` gives a pointer, and the
line names no command.

- **Scope:** product-guidelines, instruction-files
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-128 · derives from WAY-129 · derives from
  WAY-167 · derives from WAY-16
- **Verification:** an agent compares the change with the decision:
  - complies: `AGENTS.md` reads "Before you write or change a test, read `guidelines/testing.md`"
    below the installer's block;
  - violates: the pointer stands inside the installer's block; the testing guidelines are imported
    with `@`; the line names the command that runs the tests; the testing guidelines are reached
    only through the line that points to the coding guidelines.
- **Origin:** none

*Rationale:* testing guidelines no instruction leads to can be missed by a session outside the task
cycle; a path with its condition costs one line and is read when the condition comes (WAY-129), and
the pointer leads to work an agent would not otherwise find (WAY-128). Its condition is writing or
changing a test, since an agent that writes a test apart from the code would not meet a condition of
changing the product's code. The pointer stands outside the installer's block, which holds no path
a product chooses (WAY-107), and the gate runs the tests, so the line names no command of its own
(WAY-16).
*Rejected:* the testing guidelines reached only through the coding guidelines — an agent writing
tests apart from code does not open them; no pointer, leaving the way in to the task cycle — a
session outside that cycle can miss them.

### WAY-246 — Which parts do testing guidelines apply to, and when are they read?

The template of the testing discipline has a product's testing guidelines name in *Applies to*
every part of the product's map whose code the product's tests check and every part that holds test
files, and, before the product's first test, the parts the product's plan gives tests. Their
`## When to read` reads: before writing or changing a test.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173
- **Verification:** an agent compares the guidelines of a product with the decision:
  - complies: a product whose tests under `tests/` check the code of its parts `server` and
    `client` names `server`, `client` and the part that holds `tests/` in *Applies to*; a product
    with no tests whose plan gives tests to its part `sim` names `sim`;
  - violates: *Applies to* names only the part that holds the test files, so a change to the code
    of `server` does not select the testing guidelines; a product with no tests leaves *Applies to*
    empty.
- **Origin:** none

*Rationale:* the shared reading selects a file of guidelines by the parts its *Applies to* names
(WAY-213), so naming both the parts whose code the tests check and the parts that hold the tests
selects the testing guidelines for a change of either — code whose tests lie in another part, and
test files alone. Before the first test, the plan is what says which parts will have tests. The
condition of reading serves the pointer of the instruction file (WAY-245) and an agent outside the
cycle; the cycle's selection by parts does not turn on it, since a condition judged before a diff
exists could drop the file from an agent that then writes a test. The price: an agent whose work
touches a part with tests but writes none reads one more short file.
*Rejected:* only the parts that hold test files — a change to code whose tests lie in another part
misses the file; only the parts whose code the tests check — a change to test files alone misses
it; the selection of the cycle also turning on the condition of reading — a wrong "no" before the
diff exists drops the file from an agent that writes a test.

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

*Rationale:* a new product needs both before its first code (WAY-209, WAY-244), and two tasks one
after the other would hold that code back for a second refinement and a second request, while one
task holds both with each discipline led by the skill that knows it. The price: a larger
refinement and a larger request.
*Rejected:* a task of its own for each discipline's guidelines — a new product waits for two tasks
before its first code.

### WAY-248 — What does the testing-guidelines skill look at first?

Before anything else, the skill `maintain-testing-guidelines` recognizes which parts of a product
have tests or, before the first test, which parts the product's plan gives tests, and what the
product already has for them — a test tool, levels, directories of tests, doubles, tests of
invariants, or nothing — and it extends what exists rather than setting a second tool beside it. A
new test tool or a library of property tests is a technology choice the skill leaves to the human
as a question of the task, never one it settles, showing the options by their consequences for the
product — cost, where they run, upkeep and the cost of changing later — with a recommendation and
the weak point of the option recommended, keeping the human's preferred tool as the recommendation
(WAY-249) and otherwise recommending the simplest and cheapest where no difference with a
consequence remains (WAY-123).

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-121 · derives from WAY-123
- **Verification:** an agent compares the work with the decision:
  - complies: in a product whose tests run under one test runner, the skill proposes recipes for
    that runner's levels; a product that is to have property tests and holds no library for them
    gets the choice of that library as a question of the task, with consequences, a
    recommendation and its weak point;
  - violates: the skill sets a second test runner beside the product's own because it judges it
    better; the skill adds a library of property tests itself or leaves its choice to the human
    with no recommendation.
- **Origin:** none

*Rationale:* an existing tool, even a worse one, beats a better one brought in, since the tests
and the people working on them already follow it, and two runners over one suite split its
conventions, as for coding guidelines (WAY-210). What the product has decides how the skill works
— before the first test, an audit, or a refresh — so it is read first. A new tool is something the
product has to keep, a technology choice, and the human makes it (WAY-121). A human who cannot
judge test tools can weigh consequences and take a recommendation with its weakness visible.
*Rejected:* a second test tool set beside the product's own — two tools over one suite disagree;
the skill choosing a new tool itself — a dependency the human never chose; options with no
recommendation — the human is left to judge technology they cannot assess.

### WAY-249 — Where does the testing-guidelines skill's starting set come from?

The skill `maintain-testing-guidelines` takes the starting set of a product's testing guidelines
from the human's preferences, and, for its first testing guidelines where the human has none, from
research for the product's technology, each question of it given to a fresh agent, each source
named with its page and version and every claim no source supports refuted by a critique before
the human sees the set, as the options of a technology choice are checked (WAY-122). It researches
at every extension and never at a refresh (WAY-251), and a tool the human prefers remains the one
proposed, never displaced by research. It proposes what the research finds without imposing it.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-122 · derives from WAY-120 ·
  derives from WAY-251
- **Verification:** an agent compares the work with the decision:
  - complies: the human answers "I do not know" on how the product's tests are laid out; research
    of the product's test runner names the pages and versions of its documentation, one fresh agent
    for each question; a fresh critic strikes a claimed difference no page gives; only then the
    human sees the set; an extension to a new test level runs research, keeping the human's
    preferred tool as the proposal; correcting the existing recipes refreshes them without research;
  - violates: the starting set comes from the agent's memory; one agent researches every question;
    research reaches the human uncritiqued; a convention the research found is written into the
    task as settled; an extension reuses the first research; a refresh runs research; research
    offers another tool in place of the human's preferred one.
- **Origin:** none

*Rationale:* the product is the human's, so their preferences come first; where they have none,
research with sources and a critique lets a human who cannot judge tests tell a sound proposal
from an invented one (WAY-122, WAY-120), as for coding guidelines (WAY-211). A fresh agent for
each question keeps each research to its question and its report. New scope needs a check of
whether the existing tools fit it, while updating or correcting accepted recipes within their
scope needs no new comparison.
*Rejected:* conventions of tests proposed from the agent's memory —
the human cannot tell a sound proposal from an invented one; a fixed starting set in the-way's
template — it fits no product's technology; research once for each product — later extensions miss
what has moved; research at every refresh — an update within accepted scope pays for a comparison
it does not need.

### WAY-250 — How does the testing-guidelines skill's audit of a product with tests end?

The audit the skill `maintain-testing-guidelines` makes of a product that has tests ends, for each
level, with a proposed exemplar test, with one sentence of what the product gains by it, and three to
five charges, each with its file and line and one sentence of its effect, and, for each trust
boundary of the product's map, with whether a test of its refusal exists.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** derives from WAY-173 · derives from WAY-242
- **Verification:** an agent compares the work with the decision:
  - complies: the audit proposes for integration tests `tests/integration/test_orders.py`, "every
    new integration test sets up its data through the fixtures as this one does", charges that
    `tests/unit/test_price.py:42` builds the total it expects by calling the function under test, so
    the test passes whatever the price is, and says that no test of the boundary `api` sends a
    request with another player's token;
  - violates: the audit ends with the test tool's warnings listed by name; a charge stands with no
    line; the audit says nothing of the trust boundaries.
- **Origin:** none

*Rationale:* the human who approves the exemplar tests does not judge tests below end-to-end ones,
and a proposal with what the product gains, and a fault with its place and effect, can be weighed by
someone who is no developer, as the coding-guidelines skill's audit ends (WAY-201) and the
styleguide's audit ends with charges of a place and an effect (WAY-187); a few charges keep the
whole weighable. Whether each boundary has a test of refusal shows where the invariant of WAY-235 is
missing.
*Rejected:* what the audit found shown as a comparison of the tests' code — the human cannot weigh
it; every fault the audit found listed — a list too long to weigh.

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

### WAY-255 — How does an agent of a task's cycle wait for a command that runs long?

An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps
its prompt cache — a container build, a mutation run, a test suite a check names — by running it in
the background and reading its output between waits each shorter than that lifetime, never in one
wait past it; in Claude Code a subagent's cache lives five minutes by default, so each wait stays
under about four. Where the harness states no cache lifetime, the agent waits as the harness allows.

- **Scope:** task-cycle
- **Based on:** https://code.claude.com/docs/en/prompt-caching.md § "Cache lifetime" — "Cached
  prefixes expire after a period of inactivity. Each request that hits the cache resets the timer,
  so the cache stays warm as long as you keep working." · § "Cache lifetime" — "a one-hour TTL
  that keeps the cache warm through longer breaks but charges a higher rate for cache writes" ·
  § "Subagents and the cache" — "Subagents fall outside the main-conversation TTL bucket, so they
  get five minutes even on a subscription until you choose a longer one."; read 2026-10-27
- **Relations:** none
- **Verification:** an agent compares an agent's waits in the cycle's transcripts with the
  decision:
  - complies: a reviewer in Claude Code starts the mutation run its review needs in the background
    and reads its output every four minutes until it ends;
  - violates: a subagent in Claude Code waits ten minutes in one command for a test suite to end; an
    agent's next step after a wait past its cache's lifetime writes its whole context to the cache
    again.
- **Origin:** none

*Rationale:* an agent whose cache has expired pays at its next step to write its whole context
again, while a check between waits reads that context from the cache at a fraction of that price;
a longer cache, where a harness offers one, costs more at every write, also in work that never
waits.
*Rejected:* one wait to the command's end — it writes the whole context again after every wait past
the lifetime; a longer cache lifetime for every agent — it raises the price of each step to spare
the few that wait.

### WAY-256 — Where does a fragment of a skill stand?

A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of
the-way's process included, or one a change to a skill of the-way adds or rewords — that only one
step or one variant of the skill needs stands in a file beside the skill that the step names, or,
where it is a rule or a way of working WAY-35 places in an element's template or in the part the
elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working
that hold across its steps and the pointers, and a fragment of one step or variant that is one
instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its
pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place
follows from whether a use of the skill needs it at that step, never from the count of words or
lines of the file. Fragments that stand unchanged are not bound by it.

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
  - violates: a change adds to a skill's `SKILL.md` a page of rules only its review step uses; the
    skill of `instruction-files` proposes to cut a skill to a number of lines; a change puts a rule
    of an element's entries into a file beside the element's skill; a file beside a skill holds one
    instruction and its step names it by a pointer; a step keeps several instructions only one
    variant needs in `SKILL.md` because each of them is short.
- **Origin:** none

*Rationale:* a single rule is not lost in a longer file, while the more instructions an agent has
to carry out at once, the fewer it carries out; a fragment the step at hand does not need adds to
the instructions in play without being used, so it leaves the text read at that step, and the
measure is the instructions in play, not the words. The finding on density measured single prompts
dense with instructions to include keywords, not an agent's work through a skill, and a file read
at an earlier step stays in context, so only the instructions of steps not yet reached leave; no
one has measured it on a skill. The shape — a main part holding the picture of the whole, the rules
of working and the pointers, with each step's guidance in a file beside it — is borrowed from a
course on steering models through context, and only that shape is adopted (WAY-100); the course's
claim that a model follows all of a long skill's instructions with a chance close to zero is not,
since no measurement stands behind it. The rules of an element's entries stay where WAY-35 places
them, since every writer and check reaches them there, and this decision orders what else a skill
holds. A change to a skill of the-way is bound because a fragment it adds would otherwise go
anywhere until the skill is judged; fragments standing unchanged are left until each skill is
rebuilt, since binding them would make every skill a breach on the day of the merge. A fragment
that is one instruction, moved out, leaves a pointer in its place, which is an instruction too: the
instructions in play stay as many, and a file is added to keep. The exception reaches no further
than one instruction against the one pointer that would replace it, so a fragment of more
instructions cannot stay on the ground that each of them is short.
*Rejected:* a short skill as the aim, after the course's claim — no measurement stands behind it; a
threshold of words or lines for a skill — a count says nothing of whether a step needs a fragment;
the skills of the-way's process left to WAY-35 alone — what neither a template nor the shared part
holds would follow no rule of place; binding only what the skill of `instruction-files` proposes —
a new fragment of a skill of the-way could land in its `SKILL.md` until the skill is judged;
binding the fragments that stand today — every skill would breach it on the day of the merge;
every fragment one step or variant needs moved out, one instruction included — it trades an
instruction for a pointer and adds a file.

### WAY-257 — What does the skill of `instruction-files` show as the ground of each verdict?

For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it
and whether an agent recognises that moment when it comes, and every row of its judgement,
whatever its verdict, shows both answers beside the verdict.

- **Scope:** instruction-files
- **Based on:** none
- **Relations:** derives from WAY-128
- **Verification:** an agent compares the skill, or a judgement it gave, with the decision:
  - complies: a row keeping a line of a root `AGENTS.md` says the line is needed in every session
    and that no moment has to be recognised for it; a row moving a rule into a skill's step says
    the rule is needed at that step and whether the agent at that step recognises it;
  - violates: a row reads "keep — meets the three conditions" and nothing more; only the rows that
    move a rule say when it is needed.
- **Origin:** none

*Rationale:* a human disputes what a row shows: a verdict shown with its criterion can be disputed
on the criterion, a verdict alone only as a whole. The second question finds the rule whose pointer
an agent would pass by, which the first question alone would move out of the agent's reach and
switch off without a sign (WAY-128).
*Rejected:* the reason particular to each verdict alone — for keep and remove it names conditions
and defects, never when the rule is needed; the criterion stated once above the table — a row could
not be disputed on its own.

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
- **Relations:** derives from WAY-256
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

### WAY-259 — What does an installed skill entry point tell an agent to read from the pinned the-way?

An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full.
It tells the agent to read a file the skill names inside `.the-way` when the step or variant that
names the file comes, not all named files at the start.

- **Scope:** installation
- **Based on:** none
- **Relations:** derives from WAY-256
- **Verification:** an agent compares a product's entry point with the decision:
  - complies: the entry point tells the agent to read the full skill first and a named file when
    the step or variant that names it comes;
  - violates: the entry point tells the agent to read every named file before starting the skill.
- **Origin:** none

*Rationale:* reading the full skill gives the agent the picture of the work, its shared rules and
its pointers. Reading each named file when its step or variant comes keeps rules for other work out
of the instructions in play, at the cost of recognizing the named moment and opening the file then.
*Rejected:* reading every named file at the start — the agent carries instructions for steps or
variants it may not take; reading only the skill — an agent at a named step lacks its detailed rules.

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| WAY-06 | its rule, that a foundation change reaches the main branch with its code, stands in WAY-01 | WAY-01 |
| WAY-15 | its rule, what is derived and what is written by hand, stands in WAY-225 | WAY-225 |
| WAY-20 | withdrawn: it said only that a change names no kind of change; what a change does to an entry's meaning reaches the human as WAY-114 gives it | WAY-114 |
| WAY-23 | its rule, that a product keeps all its decisions in one log, stands in WAY-18 | WAY-18 |
| WAY-31 | withdrawn: a reference names an entry by its identifier alone, with no fingerprint (WAY-02), and the author's search finds what names a changed entry (WAY-33) | WAY-02 |
| WAY-39 | its rule, how a fingerprint is computed, stands in WAY-02 | WAY-02 |
| WAY-43 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-46 | withdrawn: it said only that a part carries no failure modes and no criticality; the part map gives a part no such field | WAY-40 |
| WAY-47 | withdrawn: it said only that no list of a critical flow's parts is checked; a critical flow has no entry in the part map (WAY-45) | WAY-45 |
| WAY-50 | the part map keeps no levels of promise or policies of change; how a change to a surface is made known stands in WAY-49 | WAY-49 |
| WAY-57 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-59 | the binding part of an invariant entry is given by WAY-56, which answers how much one invariant entry holds | WAY-56 |
| WAY-66 | an invariant's links name an entry by its identifier alone, with no fingerprint (WAY-02) | WAY-02 |
| WAY-67 | a violated invariant is marked at its entry, with no list of violated invariants beside it (WAY-51) | WAY-51 |
| WAY-70 | its rule on values written out left the invariants; for a product's tests it stands in WAY-228 | WAY-228 |
| WAY-74 | withdrawn: it said only that the-way keeps no record of a run; the exit code of the command running the tests says whether a test failed (WAY-63) | WAY-63 |
| WAY-75 | its rule, where environment fact entries stand and what identifies one, stands in WAY-64 | WAY-64 |
| WAY-79 | withdrawn: that an entry of any element carries no version and is edited in place stands in WAY-07 | WAY-07 |
| WAY-81 | withdrawn: it said only that an environment fact names no method; how a fact keeps up with its source stands in WAY-82 | WAY-82 |
| WAY-83 | withdrawn: the foundation records no human verdict | none |
| WAY-87 | the part map records no criticality; how an obligation from a law or a contract reaches a product stands in WAY-86 | WAY-86 |
| WAY-88 | its rule, that a fact stands only while an entry names it, stands in WAY-73 | WAY-73 |
| WAY-91 | a fact has no probe, so no release of a probe's tool counts | none |
| WAY-92 | its rule, which glossary holds a word of the process and which a word of a product's domain, stands in WAY-226 | WAY-226 |
| WAY-98 | withdrawn: it said only that a glossary entry holds no *Avoid*; WAY-94 gives an entry its one field | WAY-94 |
| WAY-105 | withdrawn: when an invariant's method reads `test` and when `review` stands in WAY-61, which answers how an invariant's method of checking is written | WAY-61 |
| WAY-119 | withdrawn: no decision carries *Review when* | none |
| WAY-149 | withdrawn: it said only that a return-step test takes no deliberate break; every invariant test is seen failing once (WAY-08) | WAY-08 |
| WAY-157 | withdrawn: how the orchestrator waits for an agent is a step of the task-cycle skill and binds no other work | none |
| WAY-175 | withdrawn: what the styleguide's template and skill take from outside is no question a decision answers; the sources are private, so each piece binds through the decision that carries it, on that decision's own rationale (WAY-100, WAY-27) | WAY-100 |
| WAY-179 | withdrawn: an example of a template needs no decision (WAY-168) | none |
| WAY-181 | withdrawn: the order of a plan is an example the styleguide carries, and WAY-213 says who reads it and how | WAY-213 |
| WAY-188 | withdrawn: what checks a rule of a styleguide is what WAY-168 gives every rule of guidelines | WAY-168 |
| WAY-190 | withdrawn: what keeps a product cleaned gradually from breaking a marked invariant again stands in WAY-51 for every marked invariant | WAY-51 |
| WAY-193 | withdrawn: the same rule for every discipline stands in WAY-173 | WAY-173 |
| WAY-194 | withdrawn: how both skills of guidelines ask the human stands in WAY-174 | WAY-174 |
| WAY-195 | withdrawn: what coding guidelines take from outside is no question a decision answers; each piece binds through the decision that carries it, with its source in *Based on* (WAY-100) | WAY-100 |
| WAY-196 | withdrawn: what checks a rule of coding guidelines stands in WAY-168 and WAY-198, and the invariants of a standing check in WAY-202 | WAY-168 · WAY-198 · WAY-202 |
| WAY-197 | withdrawn: the uses of a rule are optional lines of the rule (WAY-168), and the test of its invariant is seen failing once like every other (WAY-08) | WAY-168 · WAY-08 |
| WAY-222 | withdrawn: what the task cycle takes from outside is no question a decision answers; the sources are private, so each piece binds through the decision that carries it, on that decision's own rationale (WAY-100, WAY-27) | WAY-100 |
| WAY-223 | withdrawn: it said only that a test protecting a history with no elements takes no evidence of its own; every invariant test is seen failing once (WAY-08) | WAY-08 |
| WAY-224 | withdrawn: the part map records no failure modes, so no cycle asks the human about one | none |
