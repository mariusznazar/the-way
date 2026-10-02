# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and, on the main branch, are only ever appended.

### WAY-01/1 — What state does the foundation describe?

On the main branch, the foundation describes the product as it is — its rules, together with
the listed debt wherever the product does not yet meet them — and roadmaps and plans do not change
it. A task that sets out to change the foundation makes that change in its foundation step, and the
code follows; a foundation change in progress lives on the task's branch in the product's
repository and reaches the main branch in the same merge as the code that follows it. When a task
closes, the foundation again matches the current state.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-change-merge-route. Level 2 for the rest — an
  agent compares the change with the decision:
  - complies: a task branch changes a decision and its code, and both reach the main branch in
    one merge; a task that brings the code back in line with an invariant runs without a
    foundation step;
  - violates: a planned feature is written into the foundation before it is built; the code is
    merged and the foundation change is left for a later task.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a foundation that describes intent ages with every change of direction, unseen,
because it is expected to differ from the code; one that describes the current state can be
checked against the product at any time. An abandoned task's foundation change is dropped with its
branch, leaving no false description.
*Rejected:* the foundation as a description of the target product — it ages unseen; the foundation
updated only after deployment — a step at a task's end goes missing; a "designed, not built" mark
on the main branch — an abandoned task leaves it for good.

### WAY-02/1 — How do dependents learn that an entry has changed?

Every foundation entry has a permanent identifier, and everything that depends on it — other
entries, tests, documents and code comments — refers to that identifier. A reference that relies
on the entry's current binding part carries its fingerprint (`WAY-17@<fingerprint>`), and
when the fingerprint changes, a script working on plain text files flags that reference for
review; a bare identifier and a reference to a version (`WAY-17/2`) are never flagged. The
fingerprint covers only the binding part of an entry — for a decision, its binding sentences — and
is the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that binding
part encoded in UTF-8, taken after every run of spaces and line breaks is replaced by a single
space and both ends are trimmed; nothing else in the text is changed before it is digested.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: decision-guard-stale-reference ·
  decision-fingerprint-input · log-reference-target · relation-fingerprint-value ·
  fingerprint-definition.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* only a fingerprint in each reference that relies on an entry shows which references a
change left stale; it covers only the binding part and ignores only wrapping, because flags raised
for nothing get cleared unread, and whether other changes alter the meaning is the human's call,
not a script's.
*Rejected:* impact analysis by a language model — nobody knows what it missed; a fingerprint of the
whole entry — every rationale fix flags all references; one kind of reference — a historical record
flagged like a test; a digest of the text as written — rewrapping flags everything; ignoring case
and punctuation — meaning they carry goes unflagged; the full 64-character digest — unreadable,
nothing gained; one computation per element — a reference would need its element.

### WAY-03/1 — Who may change an invariant test, and when?

Invariant tests are written and accepted together with the foundation change, and during
implementation they are read-only. A mechanism outside the model enforces this: when a change is
merged, a check whose definition is taken from the main branch rejects any change to an invariant
test not accepted by the panel or by a human. A task that needs an invariant test changed goes back
to the foundation step.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** impossiblebench-test-modification@9cdba560
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: invariant-test-change-acceptance.
- **Review when:** no model in the range of fact impossiblebench-test-modification is Active in
  Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* an agent that a test stands in the way of adjusts the test to the code: the build
turns green, and the foundation lies. Keeping invariant tests out of the implementer's reach
removes that move instead of forbidding it.
*Rejected:* a written rule "do not change the tests" — prose stops nothing; a local hook — one
switch skips it.

### WAY-04/1 — What makes up a product's foundation, and what in it is derived rather than written by hand?

A product's foundation has five elements, and the list is closed: invariants, decisions, a
glossary of product terms, a part map, and environment facts. A new pattern enters the
foundation only as a field or a rule of one of the five, and only when a mechanism keeps it
without human memory: a test, a lint, a check that stops a merge, a mandatory relation or
configuration. What can be derived from what the product executes — code, configuration,
infrastructure as code, runtime traces — is derived, never written by hand, and what is derived
describes the state; rules are written by hand: what is allowed, how bad a failure would be and
what the product promises, which the code cannot show.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-file-kinds · derived-file-content. Level 2
  for the rule on new patterns and for what is derived — an agent compares the change with the
  decision:
  - complies: a part's failure modes enter the foundation as fields of the part, and its
    criticality is computed from them; existing dependencies between parts are read from the
    product's own dependency graph and compared with the map's allowed ones;
  - violates: a hand-written architecture document appears next to the part map; a hand-written
    list of the product's endpoints kept next to the code; the allowed dependencies in the part
    map copied from the current import graph.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* each element holds what no other can, and a foundation nobody maintains gives only
paper safety; a hand-written copy of the state goes stale, and code shows only what exists: a
view derived from it shows accidents as architecture, a rule copied from it turns one into law.
*Rejected:* as elements of their own — tests (a method of an invariant), the "why" (a decision's
rationale), product identity, principles and non-goals (decisions), classes of task risk
(inherited from parts), structural code rules and quality scenarios (invariants), criticality (a
field of a part), the agent's environment and the return step (the task cycle); external
constraints as a field of the map — a fact plus the invariant it creates; a hand-written
architecture document or diagram — a second copy of the map; environment facts as backlog
hypotheses — they are true or false today; assumptions as a kind of entry — anything
inconvenient would be called one and escape checking; "do not write by hand what can be derived
from code" as the whole rule — it reads as a demand to derive the map's rules; derivation from
code alone — behaviour shows in runtime traces, deployment in infrastructure files.

### WAY-05/1 — How is a decision entry written?

A decision version opens with one to three binding sentences — in the present tense, describing
a state that is to be true, concrete enough to check — followed by fields a script or an agent
reads, then rationale and rejected options in prose, which, where the entry's author writes it
rather than quotes a source, names no file, script or count, nor what the process's own tools do or
lack today, and does not tell how the decision was reached. A field stays in the template only
while someone or something reads it, and what a decision forces on later work stands in a binding
sentence or a field, never in prose. A rule in `elements/decisions/` changes only with a decision
and cites its number, and an example there names a decision of the log by its number instead of
copying it.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: binding-sentence-count · binding-sentence-words ·
  decision-example-numbers · decision-template-change. Level 2 for the rule that every field has a
  reader — an agent compares the change with the decision:
  - complies: a new field enters the template together with the reader named in its table;
  - violates: a "notes" or "related artifacts" field that nothing reads.
  Level 2 for a rule citing the decision that sets it — an agent compares the change with the
  decision:
  - complies: a new rule of the decision template ends with the number of the decision that sets it;
  - violates: a rule added to `elements/decisions/` cites no decision.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a record written like a legal code is followed worse, and agents generalise from the
reasons they are given, so what binds stays short and checkable, reasoning below; a field
nobody reads goes empty, and long lists of fields stop people recording decisions; the template
follows the decisions (WAY-01).
*Rejected:* prose without fields — nothing a script can read reliably; many fields and relations —
fields without a reader; a hand-written status — a second copy of the versions; a one-sentence
entry — no reasoning beside the rule; "will" or "should" — an intent, not a state; capitals such as
MUST — shouting reads worse, not stronger; examples written for the template — an example with gaps
teaches gaps.

### WAY-07/1 — From when may a decision entry no longer be edited?

An entry in the decision log is edited in place until it reaches the main branch; until then
it gets no new version and no new decision about it. An edit that changes the meaning of an
accepted entry is accepted again. Once an entry is on the main branch, it is never edited, and
the log there only grows at the end.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: log-existing-lines · log-versions-added-per-number ·
  log-merge-copies. Level 2 for acceptance after a change of meaning — an agent compares the change
  with the decision:
  - complies: an accepted entry whose binding sentences changed on the task branch is shown to
    its approver again before the merge;
  - violates: an entry reaches the main branch with binding sentences its approver never saw.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* an entry binds only once it is on the main branch (WAY-01), so versions written
before would carry states that never bound anything; there the log keeps what was in force. After a
change of meaning without new acceptance, *Approved by* would name someone who did not approve it.
*Rejected:* an entry fixed from the moment it is written — every edit made during a task
becomes a version that never bound anything.

### WAY-08/1 — How is an invariant checked?

Every invariant names its method of checking, and its current result comes from running that
method, never from a status written by hand. The default method is a test in the broad sense —
a code test, an end-to-end test or an exploratory test run by an agent on the working product —
and a test counts only when a deliberately introduced break of the invariant makes it fail, in k
of n runs, which its method's command sets and records as one verdict, for a test that does not
give the same verdict every time. Human inspection is used for assessments that neither an
automated check nor a repeatable measurement can settle, and it leaves a trace of who checked and
when.

- **Change:** new decision
- **Scope:** invariants
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: invariant-method-form · invariant-test-break ·
  human-verdict-invariant-row. Level 2 for the choice of method — an agent compares the change
  with the decision:
  - complies: a person settles whether an image's text alternative describes it, after the
    accessibility check marked it incomplete;
  - violates: an invariant that a repeatable measurement can settle is left to human inspection.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* coverage is not checking: code can be covered while no test fails when it is
removed; a status written by hand goes stale with the next commit; k and n in the command let one
run's verdict cover the n runs; even accessibility tools hand uncertain cases to a person.
*Rejected:* test coverage for every invariant — untestable ones leave the foundation or get a
test that always passes.

### WAY-09/1 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a
directory for each part of the process other than `repository` — `elements/<element>/` for each
foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`,
`installation/`, `agent-instructions/` and `task-cycle/` — with `probes/` as a second directory of
the environment facts part, for the checks of the-way's own facts, the files that configure the
whole repository, which its part map gives to the `repository` part (WAY-44), the root agent
instruction files, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that
describes the repository.
A directory reaches the main branch only once it holds what its part requires: an element its
template and rules, examples or a pointer to entries of the-way that serve as its examples, a
skill that writes its entries and a format guard; `elements/common/` the rules of form and the way
of working the elements' templates and skills share, the code their format guards share and the
procedure of the panel; `relation-model/` the script that computes fingerprints; `gate/` the test
of every critical flow in the part map; `installation/` the installer, its tests and a README
explaining how a product uses the pinned version; `agent-instructions/` the instructions for agents
working on this repository, led to from the root agent instruction files; `task-cycle/` what the design of
the task cycle sets, and until then it does not reach the main branch. The entries in
`foundations/` are checked by the format guards of their elements.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, repository, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: repository-file-location · element-directory-contents ·
  relation-model-directory-contents · invariant-example-target · map-example-target ·
  glossary-example-target. Level 2 for what `elements/common/`, `installation/`,
  `agent-instructions/` and `task-cycle/` hold and for the format guards checking `foundations/`
  — an agent compares the change with the decision:
  - complies: code two format guards share moves into `elements/common/`, and both load it from
    there; a new file of entries in `foundations/` comes with the format guard of its element;
    the installer, its tests and instructions stand together in `installation/`; the agent
    instructions have their own part and root entry points;
  - violates: a `tools/` directory for shared scripts reaches the main branch; `task-cycle/`
    reaches the main branch before the design of the task cycle sets what it holds.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* anything brought in on the side makes the repository a store of material; directories
follow the parts, so a change's files name its part and decisions (WAY-21); an incomplete directory
is work in progress, kept on a branch (WAY-01); probes stand apart, so an element's tests run no
fact's method; product installation and agent instructions have different failures from repository
configuration.
*Rejected:* material merged as soon as it is written — a store from the first day; an element whose
only tool is a skill — the form holds only while someone remembers to run it; one `tools/`
directory for everything shared — it matches no part and grows into a store; one set of template,
skill and script for every directory — a script that only reads has nothing for a skill to write;
the files serving the whole repository left out of the map on purpose — they lose their part and
its failure mode; installation or agent instructions folded into repository configuration — their
failures lose their own parts.

### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation is assessed by the panel, which has three
agents: two assess it independently, on different models where two are available, each from a
different, named perspective and seeing the diff and the files of the commit it assesses without
the task's chronicle, never the author's reasoning, and one of the two perspectives names what of
the change can be cut, while the third settles between them twice, reading the two assessments in
swapped order. The panel decides a change of an invariant test's mechanics — selectors, test data,
waiting — where its two settlements agree, and a rerun set outside the method's command is never
such a change. Every other change, and one on which the two settlements differ, the panel prepares
with the diff, its effects, its settlements and a recommendation, and a human decides.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  task-cycle
- **Based on:** llm-self-preference@6d9f4b97 · TODO — the finding that settling in both orders
  rests on
- **Relations:** derives from WAY-03@97d336a9
- **Verification:** level 1 — invariants: invariant-test-change-acceptance ·
  foundation-change-panel-record. Level 2 for what the panel decides — an agent compares the change
  with the decision:
  - complies: both settlements accept a new selector in an invariant test, and it merges without a
    human;
  - violates: the panel accepts a changed expected value in an invariant test; an assessing agent
    receives the author's reasoning; one order's settlement stands though the other order's differs.
- **Review when:** TODO
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* the problem is a single executor that checks itself: agents on one model with one
input share its blind spots, so independence comes from different perspectives and from not seeing
the author's reasoning; settling in both orders costs little. Only a human knows what the product is
meant to protect. The finding it cites measured models of other publishers only, and this decision
takes it across publishers (WAY-85).
*Rejected:* a panel that settles everything — it does not know what the product protects; a single
agent without a panel — it checks itself.

### WAY-11/1 — How does a task end?

A task ends with its return step before its branch is merged: an agent lists from the diff and the
task's log new rules and decisions, code behaviour with no invariant over it, environment facts the
change rests on that the foundation does not yet hold and words whose use the glossary does not yet
settle, proposes them to the panel as a foundation change, and compares the foundation with the code
in the parts the task touched. A periodic review of the foundation runs apart from tasks.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step finds
  — an agent compares the change with the decision:
  - complies: an edge-case rule the implementer wrote into the code comes back as a proposed
    invariant before the merge;
  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
    invariant covers.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* some of the foundation is learned only in implementation and in use, and a task that
missed the foundation does not report it; an end step goes missing, so the merge waits for its
record. Facts and words are listed because, like rules, they are learned in code.
*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
in the code.

### WAY-12/1 — How is a decision checked?

A decision is checked through the invariants derived from it, which its *Verification* names by
the identifiers of their entries, and tests live only with invariants. Where no invariant can be
derived today, an agent compares a change with the decision using a pair of examples — one that
complies and one that violates — and where an agent cannot judge, a human assesses it and leaves a
trace of who and when. A decision can combine levels, each covering what it can check of its
binding sentences.

- **Change:** new decision
- **Scope:** decisions, invariants
- **Based on:** llm-decision-violation-detection@92f498f3
- **Relations:** none
- **Verification:** level 1 — invariants: decision-verification-level ·
  level-one-decision-invariants · invariant-citation-target · verification-invariant-derivation.
  Level 2 for the choice of level — an agent compares the change with the decision:
  - complies: a decision on the product's direction is checked by an agent with a complying and a
    violating example;
  - violates: a decision whose rule a lint check could enforce is left at level 2.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* a test checks an invariant on every commit; a decision about direction or trade-offs
often cannot be. Agents judge explicit, code-readable decisions well and deployment- or
organisation-dependent ones poorly, a finding this decision takes across publishers (WAY-85);
those stay with a human. A pair of examples marks the line.
*Rejected:* a rule in code as the only check — decisions that cannot be written as a rule go
unchecked.

### WAY-13/1 — What sets the weight of a task's process?

What a task touches, never its size, sets its process: an agent's analysis at the start of the task
settles whether it changes the foundation, which chooses among the paths that merge a change, while
three things set how sharply it is checked — the criticality of the parts it touches, as the part
map computes it, whether it touches the files of a trust boundary, and whether the change can be
undone. Paths that merge a change differ in their steps, never in the outcome a task has to reach,
and only a human sets a task to return knowledge instead of a change, which merges nothing. A task's
size serves only as a signal to split it, an agent may check a change more sharply than the map
computes, never less, and a human decides on every change that cannot be undone.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
    a human's decision;
  - violates: a task gets the heavier path because of the number of lines it changes; a change
    that cannot be undone reaches the main branch without a human's decision; an agent turns a task
    into one that returns knowledge instead of a change without a human setting it so.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* size misleads both ways: a rename across many files is easy to undo, a one-line
change to a stored format can destroy every user's data. Paths differ only in steps, because a
weaker outcome would bypass the process; returning knowledge alters what a task delivers, so a
human sets it.
*Rejected:* one cycle for all tasks — how much process a task needs depends on what can go wrong;
the path chosen by size — size misleads; a human approving every diff (DORA) — no fewer failed
changes, and attention spent where it adds nothing.

### WAY-14/1 — Who approves a version of a decision?

A version of a decision is approved by a human, never by an agent, and records who approved it and
when; in the-way, the approver is Mariusz.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: decision-approval-record · decision-approver.
- **Review when:** the-way decides which of its elements a team may adapt, and with it who approves
  decisions for which parts · check by: 2026-12-31
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* the record of who approved and when is what a human considering a change reads, and what
WAY-07 needs when an entry has to be accepted again.
*Rejected:* a field in every entry naming who is to approve it — the same name repeated, stale once
the team changes; lists of decision-makers and of those consulted — nothing reads them.

### WAY-16/1 — How are the checks of invariants run?

The gate takes its checks from the methods of checking written in the entries, never from a list
written by hand, and one command runs the checks a change calls for together with the product's own
tests it calls for — the same command for an agent, for a human and for whatever runs it when a
change is merged.

- **Change:** new decision
- **Scope:** invariants, agent-instructions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: ci-checking-commands · gate-check-source. Level 2 for the
  same command for everyone — an agent compares the change with the decision:
  - complies: the instructions for agents name the gate's command as the way to check a change;
  - violates: the instructions for agents list test and lint commands of their own; the product's
    tests run under a command of their own beside the gate's.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* a list of checks written by hand is a second copy of the invariants that drifts: a
new invariant never runs, a removed one still does. One command for all leaves no doubt which list
ran.
*Rejected:* a gate written for each product — it drifts from that product's invariants; separate
commands for an agent, a human and whatever runs the gate when a change is merged — three lists to
keep in step; the product's tests under a command of their own — of two commands an agent runs one.

### WAY-17/1 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends
on the other, and none is optional: a decision and an invariant name the environment facts they
rest on, an invariant derived from a decision names that decision, and a check names its
invariant.

- **Change:** new decision
- **Scope:** relation-model, decisions, invariants, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: level-one-decision-invariants · invariant-citation-target
  · verification-invariant-derivation.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* the chain is the path a change travels, so a missing link breaks it without a sign,
and an assumption no entry names escapes review; the link sits in the dependent entry, because
only its writer knows what it rests on.
*Rejected:* links written by the entry depended on — it cannot know its dependents; optional
links — a missing one looks unneeded; research findings outside the environment facts —
decisions about agents would have no fact to flag them.

### WAY-18/1 — How is a product's decision log kept?

A product keeps all its decisions in one log, whatever they are about. The decision log holds every
decision version and review record in the order it was written, and what is in force today is a view
that a script generates from the log: the latest version of each number, and in place of a repealed
decision a single line pointing to the version that repealed it. A link between entries is written at
one end only, and the view shows it at the other; the one exception is a decision's level 1
invariants, which its *Verification* names while each of them names the decision in *Derives from*.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: view-versions · view-links. Level 2 for one log — an
  agent compares the change with the decision:
  - complies: a business rule and a technical constraint of one product stand in the same log
    under one numbering; a product's existing architecture records stay a source, and a decision
    recovered from them enters the one log;
  - violates: a separate log for business decisions next to the technical one.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* what is in force and the history serve different reads — checking a change, and
reaching the options rejected earlier; one log, because a collision is caught only between decisions
in the set a change is checked against; a link is written once, because nobody reopens an old entry.
*Rejected:* a single document edited in place — the history is lost; a log without a view — every
reader reconstructs the current state by hand; marks written by hand at a link's other end — they go
missing; separate logs for business and technical decisions — collisions between them go unseen; a
log per approver — each version records who approved it (WAY-14); a field for an entry's topic —
nothing reads it (WAY-05).

### WAY-19/1 — How are decisions numbered and versioned?

A number stands for the question a decision answers, carries the product's prefix and is given
in the order entries are written; a new question gets the next free number, and a new rule next
to an existing decision is a new question. On the main branch, every change to a decision is a new
version of its number, which gives the rationale for the change and restates the binding sentences
and fields in full, except that a repeal has no binding sentences. When a new decision answers a
question that an older one answered in passing, the sentence moves to the new decision, and the
older one loses it — by a new version on the main branch, by an edit before it.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: decision-heading-form · decision-version-sequence ·
  log-entry-field-presence · log-entry-field-words. Level 2 for one number per question and for
  sentences answered in passing — an agent compares the change with the decision:
  - complies: once on the main branch, a new rule for who approves a version of a decision is
    written as WAY-14/2; when a decision on a question arrives, an older decision that answered
    it in passing loses that sentence;
  - violates: the same question gets a second number; a version carries only the sentence that
    changed; the sentence stays in both decisions.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a permanent number lets references survive a change (WAY-02); a version restates the
decision whole, so no reader assembles it from pieces; a sentence answered in passing moves, because
two entries answering one question drift apart; the product's prefix keeps numbers of different
products apart in references.
*Rejected:* a new number for every change, the old entry marked as replaced — references rewired or
left on a dead entry; numbering by topic — topics move, and numbers would move with them.

### WAY-20/1 — What kinds of change can a decision undergo?

The first version of a decision names its kind of change as new decision, and every later version
names it from a closed list: editorial correction, unchanged sentences, new wording, narrowing,
challenge, repeal. A version of the kind unchanged sentences and a challenge keep the binding
sentences of the previous version word for word, and a repeal has none.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: binding-sentence-count · decision-change-kind ·
  decision-binding-across-versions · repeal-binding-sentences. Level 2 for the choice of kind — an
  agent compares the change with the decision:
  - complies: a version that answers the question anew is called a new wording; a typo fixed in
    a binding sentence is called an editorial correction;
  - violates: a version called an editorial correction turns "must" into "may".
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* whatever relies on a decision needs to know what a version did to it: a fixed
typo leaves every reliance valid, a new answer does not. A word for a change left undefined means
something different to each author, so the list is closed and defined in the template.
*Rejected:* two kinds, change and replacement — a fixed typo looks like a new answer; an open list —
each new kind carries its author's meaning.

### WAY-21/1 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never
file paths, so that the decisions governing a change are found from the files it touches through
the part map's rule for assigning files.

- **Change:** new decision
- **Scope:** decisions, part-map, task-cycle
- **Based on:** instruction-density-accuracy@f62b9a6d
- **Relations:** none
- **Verification:** level 1 — invariants: decision-scope-names · decisions-found-for-change.
- **Review when:** no model in the range of fact instruction-density-accuracy is Active in
  Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* an agent can apply only decisions it sees. The part map already assigns files to
parts, so using those parts as scope makes the governing decisions discoverable without copying
paths into each entry. Topics cannot be derived from changed files.
*Rejected:* file paths in each decision — duplicate the map; topics — cannot be derived from a
change; no scope — relevant decisions get lost among the rest.

### WAY-22/1 — Is a rule a decision or an invariant?

An invariant says nothing about why or what was rejected; a decision is a choice between
options, with its rationale, and it binds later choices, including those that cannot be checked on a
commit — direction, trade-off principles, non-goals. A rule that records a choice is a decision, and
what of it a commit can make false is written as an invariant derived from it; a rule with no choice
behind it is an invariant alone.

- **Change:** new decision
- **Scope:** decisions, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "the product has no multiplayer" is a decision, and "no screen offers a second
    player" an invariant derived from it; "a saved game is never lost on reload" is an invariant
    with a test;
  - violates: a non-goal that a commit can break is left without a derived invariant; an
    invariant carries a rationale and rejected options.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* an invariant is checked mechanically on every commit, a decision weighed when a later
choice is made; a checkable rule left only in a decision's prose escapes the gate, and a choice
written only as an invariant loses its reasons.
*Rejected:* one kind of entry for both — either the gate reads prose or the reasons are lost;
moving a checkable sentence out of its decision — the rule would be cut off from its reason.

### WAY-24/1 — How is a decision that rests on a prediction reviewed?

A decision that rests on a prediction names in *Review when* the predicted state of the world or the
product, observable when it comes, and a check-by date; the field does not lift the decision, and
whether the state has come is checked by the periodic review of the foundation. On the date, a
review record records what was observed: the state has not come, with the next date; it has come and
the decision is kept; or it has come and a named version changed the decision. Before the main
branch, an edit in place that the decision's approver accepts again answers the date as well when it
rewrites *Review when* from what was observed, and a check-by date is moved in no other way.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: review-when-form · decision-guard-overdue-review ·
  review-next-check · review-named-version. Level 2 for who looks and when — an agent compares the
  change with the decision:
  - complies: the periodic review finds a passed check-by date and records that the state has not
    come, with the next date; before the main branch, a decision whose state has come is edited in
    place from what was observed and accepted again;
  - violates: a review record says the state has not come but gives no next date; before the main
    branch, a passed check-by date is moved later with neither a review record nor an edit from
    what was observed.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a prediction is a bet; a state and a date make it checkable. An end date is more often
extended than acted on, so the date only asks for a look, and every look is recorded, so no run of
"not yet" or moved date passes in silence.
*Rejected:* a decision that expires on a date — the date gets extended; a review date without a
state — nobody knows what to check; a review as a new version — a full copy for every look; the
agent in the decision's scope checking the state — it is given the binding sentences, not this
field.

### WAY-25/1 — What settles a collision between two decisions?

Where two decisions both apply and collide, the one that prevails names the other in *Relations*
as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a
chain, and two decisions that narrow each other are an error. A collision between two decisions
with no precedence recorded is never settled by the agent that meets it; a human records the
precedence — by a new version on the main branch, by an edit before it.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: narrows-pairs. Level 2 for a collision with no precedence
  — an agent compares the change with the decision:
  - complies: an agent meets two applicable decisions that pull opposite ways, finds no
    precedence between them, stops and asks for it;
  - violates: an agent settles the collision in favour of the newer decision; an agent infers
    that A prevails over C because A narrows B and B narrows C.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* pairs record only what someone actually weighed; nothing follows along a chain, because
A over B and B over C were weighed in different situations; an agent that settles an unrecorded
collision makes a trade-off no human made, and the human who records it answers for it.
*Rejected:* one ranked list of principles (AWS tenets) — an order claimed for pairs nobody weighed;
levels of authority over whole groups of decisions — a collision inside a level stays unresolved;
the newest decision wins — the date of a decision is not its weight.

### WAY-26/1 — How are trade-off principles and non-goals written?

Each trade-off principle is a decision of its own, whose binding sentence says which of two good
things is chosen when they conflict and whose rationale names the problem it solves. Each
non-goal is a decision of its own that says what the product does not do and why.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "When speed of release conflicts with completeness, we choose speed", an entry of its
    own whose rationale names the problem; "The product has no multiplayer", with its reason, as an
    entry of its own;
  - violates: a principle naming one good thing only ("we value quality"); several principles or
    several non-goals in one entry.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a principle rules later choices only when it names what it gives up; the rationale names
the problem, so a later reader can tell when the principle stops serving it; one entry each, so each
changes on its own and precedence is recorded pair by pair (WAY-25).
*Rejected:* several principles or non-goals in one entry — a change to one flags them all, and no
precedence can be recorded between them.

### WAY-27/1 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every
entry carries its whole reasoning, and what is seen only in such a source is described in the
entry instead of being pointed to.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, agent-instructions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: outbound-link-reach. Level 2 for the reasoning in the
  entry — an agent compares the change with the decision:
  - complies: a decision quotes a public study with its address; a pattern seen in a product
    outside the repository is described in the rationale, without a pointer to it;
  - violates: *Origin* points to a private note; a rationale rests on "as in our other product"
    without saying what was seen.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a pointer to a source the reader cannot open is a dead end, leaving a claim nobody
can check; what was seen there, written down, can at least be judged, and WAY-17 still has a fact
to name.
*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader can open
them.

### WAY-28/1 — How does the process enter a product that already exists?

When the process enters a product that already exists, the existing state is its starting point
and needs no justification, and the rules apply to changes from then on. The part map with
criticality comes first; the invariants of the critical flows and the parts they run through are
then recovered from what the product does — an agent lists what a part does, and a human chooses
which of it the product must keep — and the other invariants come through the return step of
tasks. Decisions are recovered only when a task touches the parts they govern.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: on entering a product, the part map comes first; a human picks a critical payment
    flow's invariants from the agent's list of what it does; a decision is recovered when a task
    first touches the parts it governs;
  - violates: an agent turns everything the critical flows do today into invariants without a
    human's choice; an agent recovers from the code decisions for the whole product before any
    task touches them; the critical flows and the parts they run through wait for a task like any
    other.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* decisions recovered in advance tempt an agent to invent reasons that look like
decisions. What the product does today is a state, not a rule (WAY-04); only a human knows what it
must protect. An invariant needs no decision above it, so it binds before anyone knows why.
*Rejected:* recovering the whole foundation at the start — slow, with reasons invented where none
are known; everything on demand, the critical flows included — a break there shows only when a task
happens to touch them.

### WAY-29/1 — How is a decision recovered from an existing product written?

A decision recovered from an existing product records in *Origin* what was searched and what was
found, and its rationale and rejected options are quoted from that source, given by a human who
knows them, or written as `unknown`. A rationale an agent proposes goes to a human as a question,
never into the entry.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** llm-design-rationale-expert-overlap@d27dc54f
- **Relations:** derives from WAY-28@94d8ef12
- **Verification:** level 1 — invariants: inherited-origin-form · inherited-rationale-source. Level
  2 for the agent's role — an agent compares the change with the decision:
  - complies: an agent finds the reason in a merged request and quotes it; an agent finds nothing
    and asks, and the entry gives the reason under the name of the human who knew it;
  - violates: an agent writes a plausible reason inferred from the code into the entry; an agent
    lists in *Rejected* the options it infers were weighed.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* a reason an agent writes looks exactly like a recorded one, and later readers take it
for the reason the decision was made; a human who knows it is a source, a guess is not. The cited
study compared generated arguments with expert rationale after giving models the problem and
decision; it did not test recovery from code, and argument overlap is not a correctness rate. This
decision takes its warning across model publishers (WAY-85). A recorded search is not repeated,
and `unknown` shows nobody knows what the decision guards.
*Rejected:* an agent's rationale in the entry — read as the reason the decision was made; rejected
options filled in as `none considered` — nobody knows what was considered.

### WAY-30/1 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan and approved with it by
the decision's approver. When a contradiction shows only during implementation, the agent stops,
quotes the decision by its number, and either brings the change into line, drops the change, or
proposes on the task branch a new wording or a narrowing of the decision — by a new version on the
main branch, by an edit before it — and the code that needs it waits for the decision's approver. An
exception written in advance into a decision's binding sentences is not a contradiction, and no
exception lives only in a task's plan.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task branch whose code goes against a decision carries a proposed narrowing, and
    the merge waits for its approver;
  - violates: a task branch whose code contradicts a decision that stays unchanged; a task's plan
    that records a "justified violation" of a decision.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* an exception kept only in a plan leaves the foundation describing what the code no
longer does (WAY-01); stopping shows the contradiction when it is found. Aligning or dropping the
change leaves the decision intact, so the agent may do either; changing the decision is its
approver's.
*Rejected:* a justified violation recorded in the plan, the decision unchanged — the foundation
stops matching the code; a whole new answer as the only way to change a decision — a narrow
exception takes the whole decision with it.

### WAY-31/1 — Which links between entries are flagged when the named entry changes?

A relation `derives from` or `narrows` relies on the binding part of the decision it names and
carries that decision's fingerprint (`derives from WAY-01@<fingerprint>`), and an invariant entry's
*Derives from* and *Rests on* carry the fingerprint of each entry they name, while its *Part*
carries none. A change to the fingerprint of an entry so named reaches the main branch together
with every decision that relates to it with a fingerprint and every invariant carrying it, each
checked against the new binding part and carrying the new fingerprint.

- **Change:** new decision
- **Scope:** decisions, relation-model, invariants, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46 · derives from WAY-17@b1e26133
- **Verification:** level 1 — invariants: decision-guard-stale-reference ·
  relation-fingerprint-presence · relation-fingerprint-value · link-fingerprint-presence ·
  link-fingerprint-value. Level 2 for checking against the new binding part — an agent compares
  the change with the decision:
  - complies: WAY-01's new wording merges with unchanged sentences versions of its still-valid
    dependents and a new wording of one that fails; WAY-05's new wording carries its fingerprint
    into each invariant deriving from it;
  - violates: a script renews every old fingerprint in the log or `foundations/invariants.md` with
    no one reading the entries that carry them.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a relation or an invariant's link stands on what the named entry says (WAY-17), and a
plain identifier never shows the ground moved; WAY-02's fingerprint serves, so no second
mechanism; the renewal travels in the same merge, so nothing binds on the main branch unchecked.
*Rejected:* flags from the kind of change — a misnamed kind silences them; no flags, the author
reading the dependents — a step that goes missing; flags left open on the main branch — an entry in
force on unchecked ground; flags of graded strength — nothing reads the strength; a fingerprint on
*Part* — a reworded responsibility flags every invariant in the part for nothing; a renewed link
raising the invariant's version — every citing test fails with the sentence unchanged.

### WAY-32/1 — What types of relation can a decision name?

A decision names its relation to another decision with one of two types, and the list is closed:
`derives from` — a higher decision this one serves; `narrows` — a decision this one deliberately
goes against in a narrower area.

- **Change:** new decision
- **Scope:** decisions, relation-model
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: relation-type. Level 2 for the choice of type — an agent
  compares the change with the decision:
  - complies: a decision that exists to serve WAY-01 names `derives from WAY-01`; a rule for one
    part that deliberately departs from a general decision names `narrows`;
  - violates: `narrows` for a decision that only mentions another; a new answer to an old question
    given a new number and a relation instead of a new version.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a relation type each author reads differently tells a reader nothing, so each type is
defined once and the list is closed; both types rely on the other decision's binding part and carry
its fingerprint (WAY-31), and `narrows` also tells the checking agent where the other does not
apply.
*Rejected:* `related to` — it relies on nothing, so nothing reads it and it carries no fingerprint.

### WAY-33/1 — What does the author of a foundation change search for?

When a foundation entry is written, or a version changes its binding part, an agent searches the
whole foundation for entries it touches that no written link joins to it, and before the version
is accepted each finding becomes a relation, a change to one of the entries, or a question to a
human. The search runs again against the current main branch before the task branch is merged,
and a change to the foundation is merged only with the record of both searches.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-search-record. Level 2 for what the search
  covers — an agent compares the change with the decision:
  - complies: a decision to keep the game's whole state in the browser is written, and the search
    finds an unlinked requirement that players log in;
  - violates: the search reads only the decisions whose scope overlaps; the search against the
    main branch was made before another task that changed the foundation was merged.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* fingerprints flag only links someone wrote, while the costliest contradictions lie
between entries written apart, where nobody thought of a link — only a search of the whole
foundation finds them. Two tasks can contradict each other without a file conflict (WAY-01), so
the search runs again before the merge, and the merge waits for its record, because a search is a
step that goes missing.
*Rejected:* fingerprints alone — they see only written links; a search within overlapping scopes
— contradictions between parts go unseen; a search at writing only — parallel tasks collide once
merged.

### WAY-34/1 — Which version of the process does a product use?

A product uses the-way at a commit pinned in its own repository: its templates, skills and
scripts, and the decisions of the-way that bind its work, all come from that commit. A newer
version of the process enters a product only through a task in the product that moves the pin.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision; the invariants of
  this decision belong to each product's foundation, since no commit of the-way decides them:
  - complies: a product's foundation holds the invariants "this repository pins a commit of
    the-way" and "CI runs only that commit's scripts"; a task in the product moves the pin and
    carries what the newer version changes for the product;
  - violates: a product's CI fetches the latest the-way on every run; a skill in a product session
    comes from a copy of the-way other than the pinned commit.
- **Review when:** the first product has moved its pin to a newer the-way twice · check by:
  2026-11-17
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* a pinned commit turns a change of the process into a change in each product, taken
in there before it binds, so one change cannot stop every product's checks at once. The price:
products lag behind the process, and moving a pin is work, like updating a dependency.
*Rejected:* every product on the newest the-way — results change with no change in the product;
templates and scripts copied into each product — the copies drift.

### WAY-35/1 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the
element's entries stands in the element's template, or once in the part the elements share
(WAY-09) where it is common to them, each citing the decision that sets it; the way of working the
skills share stands once in that part, and a skill reads the rules and that way of working from
there instead of restating them.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: skill-rule-source · invariant-identifier-form ·
  fact-identifier-form · map-identifier-form. Level 2 for what the skill holds — an agent
  compares the change with the decision:
  - complies: a fix to a field's form in the skill's output goes into the template, not the
    skill; the skill orders its steps and says what to ask;
  - violates: the skill says a rationale has at most three sentences while the template does not;
    the skill restates the list of fields.
  Level 2 for a rule citing the decision that sets it — an agent compares the change with the
  decision:
  - complies: a new rule of an element's template or of the part the elements share ends with the
    number of the decision that sets it;
  - violates: a rule of entries added to the shared part cites no decision.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* an entry written by hand or by another agent meets only the template and the shared
part, so the rules stand where every writer and every check reaches them; a rule cites its
decision, the one place for its reason (WAY-04); steps and questions are no rule of an entry.
*Rejected:* rules restated in the skill next to the template — two copies that drift, and the
format guard and the skill hold entries to different rules.

### WAY-36/1 — Is a rule a decision or does it belong in a plan?

A rule enters the decision log only when it still binds once the change that brings it has been
merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition
between two states — stays in the plan of that work.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "the foundation reaches the main branch whole, once every element is ready" stays in
    the plan of building the foundation; "when what entries wait for arrives, they are fixed in
    the same change" enters the log;
  - violates: a decision on the order in which elements are built; a decision whose binding
    sentences say what happens until the first merge; an exclusion that ends with its task
    written into the log as a product non-goal.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a plan written in the present tense reads like a decision, and WAY-01 gives no way to
recognise one. The log binds on the main branch (WAY-07), and a rule that ends when its change is
merged binds nothing there: from its first day it records work already done.
*Rejected:* plans written into the log and repealed once done — the log fills with history of
work.

### WAY-37/1 — What happens to entries that wait for something when it arrives?

A change that brings what entries of the foundation wait for — an element's template, the part
map, a script — also fixes every entry that waits for it, in the same change: by a new version
on the main branch, by an edit before it. An agent finds those entries by searching the whole
foundation for what the change brings.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the change bringing the invariants template turns every invariant named in working
    form into a reference to its entry;
  - violates: the part map arrives, and WAY-21 still says that a scope names parts from a working
    list.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* an entry that says what holds until something exists turns false when it arrives, and
nothing leads from what arrives to what waits for it. Whoever brings it knows what it is, while the
authors of the waiting entries may be gone; a fix left for later goes missing.
*Rejected:* fixes left to the periodic review (WAY-11) — the foundation says something false until
the review comes.

### WAY-38/1 — In what are the scripts of the-way written?

Every script of the-way runs on the version of Python the repository declares, with its standard
library alone, and installs nothing. It calls git, and the commands a product declares in its own
repository — a dependency graph, a detector of breaking changes, coverage — reading their output
through an adapter for the format. Where a product declares no such command, the script reports
what it could not check, never agreement.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: script-language · script-imports · script-subprocesses ·
  map-guard-missing-command.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

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

### WAY-40/1 — What kinds of entry does the part map hold?

The part map holds three kinds of entry: a part, a critical flow and a surface. An allowed
dependency is a field of the part it starts from, and the known violations of the map's allowed
dependencies are a derived file beside the map, so neither is an entry of its own. The whole map
lives in one Markdown file of fixed shape in `foundations/`.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-04@29a75d2c
- **Verification:** level 1 — invariants: map-entry-kinds · map-section-kinds · part-map-file ·
  flow-part-names.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* each kind answers what the others cannot: a part, what it is responsible for and which
files are its; a flow, what keeps working across parts; a surface, what someone outside relies on.
A dependency has no identity beyond its pair of parts, and the map is read whole.
*Rejected:* a dependency as an entry with its own identifier — nothing refers to it alone;
criticality as a fourth kind — a field of parts and flows (WAY-04); the known violations inside the
map — computed state among hand-written rules (WAY-04); one file per part — a rename becomes a move
of files.

### WAY-41/1 — What identifies an entry of the part map?

Every entry of the part map carries a permanent identifier made of words, such as
`relation-model`, and it stays the same when the files assigned to it change. Splitting or merging
entries gives each entry that comes out of it a new identifier, and the identifier left behind
stays in the map as a withdrawn identifier giving why and naming its successors; an identifier is
never reused.

- **Change:** new decision
- **Scope:** part-map, elements-common, relation-model
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: decision-scope-names · map-identifier-form ·
  identifier-holders · map-reference-target · map-withdrawal-successors ·
  map-identifier-persistence.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* every reference to a part rests on its identifier, so it must outlive a move of the
part's files; words, because a number says nothing where it is read; a withdrawn identifier stays,
so an old reference still says where the part went.
*Rejected:* the path as identity (Packwerk) — a moved folder renames the part; a number —
unreadable where it is read; a number beside the name — a second field for a rare rename; a reused
identifier (Backstage) — an old reference silently points elsewhere.

### WAY-42/1 — What is the binding part of a part map entry?

The binding part of an entry of the part map is one sentence: a part's responsibility, a flow's
description, a surface's promise — and the entry's fingerprint covers that sentence alone. Path
patterns, allowed dependencies, failure modes and a flow's list of parts stay outside it.

- **Change:** new decision
- **Scope:** part-map, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: map-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* a reference that carries the fingerprint of a part's responsibility can be checked
when that responsibility changes (WAY-02). Files and other fields change more often without
changing what the part answers for; making them part of the fingerprint would raise flags for
changes that do not alter that promise.
*Rejected:* the whole entry — every moved file would change the fingerprint; the identifier alone
— no reference could signal a rewritten responsibility; a fingerprint per field — every reference
would need to name its field.

### WAY-43/1 — Is an entry of the part map versioned?

An entry of the part map is edited in place and carries no version, so the map shows the
product as it is today. What the entry said before an edit stays in git, and is read from
there.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: map-entry-version. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a part whose responsibility narrows has its sentence rewritten in the same change
    as the code;
  - violates: a part gains a second version of its responsibility with the earlier one kept
    above it; the map holds a section of retired entries next to the live ones.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a decision keeps earlier versions because their reasons still bind (WAY-18); a map
entry carries no reasons, so its earlier state binds nothing, and git answers whoever asks what the
product looked like. An entry read at a task's start says what is true now, without versions to
choose from.
*Rejected:* versions as in the decision log — history that binds nothing, and the reader picks the
current entry; an archive of past maps beside the map — git is one already.

### WAY-44/1 — What assigns a file to a part?

Every file git tracks belongs to exactly one part of the map, by path patterns that git itself
matches; a file that no pattern matches, and a file that two parts claim, breaks the gate, unless
the map lists that file as left out on purpose. Tests belong to the part they test and generated
files to the part of their generator; the files that serve the whole repository — the lockfile and
the build configuration — are a part of their own, and the files that only direct whoever carries
out its tasks — instructions for agents, skills, hooks and the configuration of agents' tools and of
CI — are another. For a file that collects entries about many parts, the parts a change touches
follow from the entries it adds or changes, not from the part the file itself belongs to.

- **Change:** new decision
- **Scope:** part-map, agent-instructions, task-cycle
- **Based on:** git-path-patterns@1519f3f7
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: file-part-assignment · path-pattern-reach ·
  left-out-file-assignment.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a change is checked against the decisions and the criticality of the parts it
touches, so every file yields one part. git matches, because a second dialect could resolve the
same map differently. A test changes what its part promises; files directing whoever carries out
tasks change every later task.
*Rejected:* a file in several parts — two answers, no rule to pick; patterns matched by a script
(fnmatch) — a second dialect beside git's; tests as a part of their own — a test change stops
counting against what it tests; files left unassigned in silence — the map passes while saying
less and less; a ledger file's part taken from its path — every recorded decision counts against
the decisions part alone.

### WAY-45/1 — How does the part map record a critical flow, and when does a change lie on it?

The part map's entry for a critical flow holds an identifier, a criticality and the list of parts
the flow runs through, while what has to stay true along it is an invariant whose end-to-end
test names the flow. A change lies on a flow when it touches a part from that list; a change to a
file the map leaves out, to the build configuration or to the dependencies lies on every flow. The
test of every critical flow runs on every change.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: flow-part-names · flow-invariant-link · gate-reported-set
  · flow-test-run.
- **Review when:** a product holds more critical flows than its gate can run on every change ·
  check by: 2026-12-31
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* the map computes from a flow the criticality its parts inherit and whether a change
lies on it. Files left out, the build and dependencies can alter any flow, nothing saying
which, so they lie on all; a handful of flow tests costs less to run than to choose.
*Rejected:* a critical flow as an invariant alone — its criticality reaches no part; the flow as a
mark at each part — the same list in two places; picking flow tests from the change (Azure Test
Impact Analysis) — it fails where it cannot reason.

### WAY-46/1 — How does the criticality of a part arise?

A part carries the failure modes a human records at it, each with the kind of damage it does,
its severity, and how it is detected before release — a named invariant, or an explicit "not
detected"; an obligation from a law or a contract that raises the criticality of a part enters the
part map as a failure mode of that part, whose detection names an invariant resting on the
environment fact of that obligation. The criticality of a part is computed rather than written by
hand: the highest of its own failure modes, of the critical flows it lies on, and of the parts that
depend on it, unless the dependency records that the two are separated and a failure of one does
not damage the other. A part with no failure modes recorded counts as the highest criticality;
raising a part's criticality needs no reason, and lowering it is accepted by the human deciding the
change, with the lowered criticality in front of them.

- **Change:** new decision
- **Scope:** part-map, task-cycle, environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: failure-mode-severity · failure-mode-detection ·
  part-criticality-field · map-guard-unrecorded-criticality · map-guard-dependency-report ·
  criticality-lowering-report. Level 2 for an obligation from outside — an agent compares the
  change with the decision:
  - complies: a part with personal data records "kept past the legal period", detected by an
    invariant resting on the law's fact;
  - violates: a part carries a field "minimum criticality: high" citing the law; the obligation is
    noted in a part's responsibility with no failure mode.
- **Review when:** a product that pins the-way holds data under an obligation from a law or a
  contract on one of its parts · check by: 2026-12-31
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* criticality sets how sharply a task is checked (WAY-13); hand-written, it goes stale.
Silence about a part raises checks instead of removing them; lowering, the convenient move, waits
for a human. Recorded detection shows which failures the gate misses, and lets a changed law reach
its invariant (WAY-31).
*Rejected:* criticality written by hand — a second copy of what flows and dependencies say; three
axes (confidentiality, integrity, availability) — WAY-13 reads one measure; an unassessed part
counting as the lowest — it would never raise a check; raising and lowering alike — the convenient
direction must cost something; "failure symptom" and "first step to limit the damage" as fields —
read in an incident, not when choosing checks; a floor of criticality as a field of the fact — it
changes the computation before any product needs it.

### WAY-47/1 — How is a critical flow's list of parts checked?

The list of parts of a critical flow is checked against coverage: where a flow's test leaves a
coverage file, the script reads it, finds the parts the files it names belong to and reports
every part the flow's list does not hold. A flow whose test leaves no coverage file is reported as
"list of parts unchecked", never as agreeing with the map. The coverage comes from the run the gate
already makes, and this check starts no second run of the tests.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-45@3798c435
- **Verification:** level 1 — invariants: flow-coverage-parts · map-guard-missing-coverage ·
  map-guard-test-runs.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* the hand-written list of parts decides what lies on the flow (WAY-45), so a part
missing from it sends a change down the light path; only coverage shows which files the test ran
through. Silence is "unchecked", because a check that sees nothing passes: two empty sets compare
equal.
*Rejected:* a required coverage check — a product without coverage would fail on the map instead of
using it; coverage choosing which tests run — WAY-45 runs them all; silence read as agreement — the
emptiest map would pass cleanest; a test run started by the map guard — a second, costly end-to-end
run.

### WAY-48/1 — How is a trust boundary recorded?

A trust boundary is recorded at the part that holds it, as a pattern of the code files which
accept data the product does not trust; an exchange with the external context records its
direction and marks what comes in as untrusted. A boundary can run inside the product, wherever
it reads back something it does not control — a browser's storage, a file on the user's disk.
A change that touches the files of a boundary is checked for crafted input, whatever the
criticality of the part.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: path-pattern-reach · external-exchange-row ·
  gate-boundary-change.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a part of the lowest criticality that parses what a stranger sends is the oldest way
in, so the boundary sets checks on its own. A pattern of files is matched like parts (WAY-44);
reading back a browser's storage or a user's file is the same act of trust.
*Rejected:* a trust boundary as its own kind of map entry — nothing reads it that the pattern does
not give; the boundary taken from the part's criticality — the exposed part is often the
unimportant one; the boundary as a line in a diagram (pytm) — only a human looking reads it.

### WAY-49/1 — How does a product declare a surface, and by what path may it change?

A surface is declared at the item itself, in the code or in the schema, with the level of the
promise and, once the surface is being withdrawn, the date of the withdrawal; a surface that cannot
be marked at the item is written in the map by hand and checked by a test. The map holds one entry
per surface — its identifier, the promise in words, and where the declaration sits — and holds no
list of withdrawals in progress; each level of promise carries one policy for changing a surface at
that level, written once in the map, every surface follows the policy of its level, and no surface
carries a path of its own. What a level's policy has to allow follows from whether the consumers at
that level update together with the product, and data already stored at the user is a consumer
that never updates; an exchange with the external context records whether the partner updates
together with the product.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd
- **Verification:** level 1 — invariants: surface-promise-level · surface-declaration ·
  map-withdrawal-date · external-exchange-row · promise-level-policy · surface-change-path.
  Level 2 for the test of a surface that cannot be marked — an agent compares the change with the
  decision:
  - complies: for a save-file format, the map names a test that reads a stored sample and fails
    on a renamed field;
  - violates: the map names, for a command-line interface, a test file that never runs the command.
  Level 2 for how a change follows its level's policy — an agent compares the change with the
  decision:
  - complies: a field of a format stored at the user is renamed, and the product still reads the
    old records;
  - violates: a command-line option is dropped unannounced, though its level's policy owes an
    announcement first; a level whose consumer never updates allows a break with nothing owed.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* a surface that cannot be marked and has no test disappears quietly. A consumer
shipping with the product changes in the same commit, one that does not update needs a route at
its own pace; the exchange records whether the partner updates — for what goes out, the consumer
— so whoever makes a change does not choose.
*Rejected:* surfaces computed from the code — tools see shape, never the promise; the declaration
only in the map — whoever changes the item does not read it; withdrawals in progress in the map —
a second copy, stale the day the item goes; a path per surface — copies drift apart; the path by
importance — it says how bad a break is, not who can follow; "updates together" for every internal
dependency — inside one repository it always holds.

### WAY-51/1 — What does the main branch hold where the product does not meet an invariant or the part map's allowed dependencies?

On the main branch the part map holds its allowed dependencies together with a listed debt:
every dependency the code holds that the map does not allow stands on a derived list of known
violations; an invariant the product does not meet stands, by identifier and current version, on
the derived list `foundations/violated_invariants.md`. A new violation of the map breaks the gate;
a row the code no longer contradicts breaks it too and goes in the same change; a listed `fail`
leaves the gate's command at zero, and a listed `pass` makes it fail until the same change drops
the row. A row of either list is added only by a change of the foundation that a human accepts,
never by a step of implementation, and the state a product is in when this process enters it goes
onto the list of known violations once.

- **Change:** new decision
- **Scope:** part-map, invariants, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-40@3d01f9cd · derives from WAY-53@aaeafada · derives from
  WAY-63@f16348c8 · narrows WAY-04@29a75d2c
- **Verification:** level 1 — invariants: known-violation-coverage · known-violations-growth ·
  known-violation-currency · known-violation-fields · known-violation-line-number ·
  gate-exit-code · violated-list-growth · violated-position-version.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* the process enters products that already break their rules (WAY-28); listed debt
keeps each rule whole, since a rule written to fit the code hides the intent, and makes the gap
countable. Where adding a row is the easy move, agents take it, so both lists share one ratchet.
*Rejected:* a main branch holding only what the code meets — no existing product could enter; the
rule weakened until the code fits it — the foundation describes the accident (WAY-04); one list
for both — the map's rows name parts and files, not entries; rows with line numbers — stale at the
next edit; a row without a version — a debt for an old meaning excuses a new one; a rule left out
or marked "not checked yet" until met — the gap stops being countable; debt paid by an end date —
repaid by weakening the rule; a list any step may grow (Packwerk) — it outgrows the will to empty
it; an addition check keyed to the entry's fingerprint — a second merge stop for what WAY-10
decides.

### WAY-52/1 — What is generated from the part map for an agent?

From the part map a product generates for its agents only rules pinned to path patterns: a
part's responsibility, its allowed dependencies, and the binding sentences of the decisions whose
scope names that part, written into the rule channels the tools already read. The patterns come
from the part's rule for assigning files, and a generated rule file is derived like any other. No
overview of the repository is generated for an agent.

- **Change:** new decision
- **Scope:** part-map, decisions
- **Based on:** context-file-effect@c44e5ef0 · claude-code-path-rules@ac99f128
- **Relations:** derives from WAY-40@3d01f9cd · derives from WAY-21@586e4a38 · derives from WAY-44@2f2b6227
- **Verification:** level 1 — invariants: derived-file-content · generated-pattern-source ·
  generated-overview.
- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
  of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* agents follow instructions in context files, while repository overviews have not
helped. Path rules supply the relevant instructions when an agent works with matching files.
Generating them from the map avoids a second hand-written account of part boundaries.
*Rejected:* an overview for agents — added context cost without measured benefit; rule files
written by hand — a copy of the map; the whole decision log on every path — relevant rules get
lost among the rest.

### WAY-53/1 — How is a derived file compared with what its generator produces?

A derived file is identical to what its generator produces on the same commit, except for values the
file itself declares as varying between runs. A derived file that cannot be produced from scratch is
named in the template of the element it belongs to, and is compared as a subset of its own version
on the commit the branch left the main branch from.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-04@29a75d2c
- **Verification:** level 1 — invariants: derived-file-content · derived-subset-naming.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-20

*Rationale:* equality with the generator's output catches a hand edit; a record of results the
gate keeps carries the moment of the run, so only declared values are skipped. A list of debt
regenerated from scratch would swallow new violations, so it is compared as a subset.
*Rejected:* records of results kept outside the repository — a commit's result readable only
from whatever ran it; whole files lifted out of the comparison — a hand edit in them goes
uncaught.

### WAY-54/1 — Where does the value of a field in a template come from?

The value of a field is read off the product wherever a tool can read it, and a template asks for
what a value follows from rather than for the name of a value; a value that a closed list of the
template does not hold is a question to the human, never the nearest value on the list. A template
marks where the value of each field comes from, part by part where a field's parts come from
different places: read off, where a tool gives the value; transcribed, where a human copies it
unchanged from a record outside the product; resting on a judgment, where it is neither.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a part's criticality is computed from its failure modes and the flows it lies on,
    never written at the part; a method names the command the gate runs, and its kind follows
    from that command; a field holding a link and its fingerprint is marked judgment for the
    link, read off for the fingerprint;
  - violates: a template asks the author to name a method's kind, which the command the gate
    runs already tells; a field that rests on a judgment stands beside fields that are read off,
    with nothing saying which is which; a skill writes the nearest value of a closed list, with a
    reason why it will do.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* an author naming a value picks the nearest with a plausible reason, and a wrong name
looks like a right one; a value read off cannot be talked into place. Where none fits, that pull
is strongest. A mark, part by part, keeps a judgment from passing as a reading.
*Rejected:* a definition beside each value — it says nothing about a case none of them covers; a
value meaning "none of these fits" in every closed list — it records what came cheapest; a mark
of its own for a field that carries text — the mark of a judgment already says it.

### WAY-55/1 — Which part of the process holds the gate?

In this repository, the gate is a part of the process of its own, and its directory is
`gate/`: the gate's code and the test of every critical flow are files there. No other part's
directory holds that code or such a test, and a file under `gate/` that only calls a body kept in
another part's directory leaves the gate in that part. Which checks a change calls for, when the
gate runs and what follows from what it reports belong to the task cycle, not to this part.

- **Change:** new decision
- **Scope:** gate, decisions, invariants, glossary, part-map, environment-facts, relation-model,
  repository, task-cycle
- **Based on:** none
- **Relations:** narrows WAY-44@2f2b6227
- **Verification:** level 1 — invariants: flow-test-location. Level 2 for code ownership and the
  boundary with the task cycle — an agent compares the change with the decision:
  - complies: the gate's code and a critical flow's test live under `gate/`, while the task cycle
    decides when the gate runs and how to use its result;
  - violates: a file under `gate/` only calls the gate's body kept in an element, or `gate/`
    decides which checks a change calls for.
- **Review when:** the gate runs as a program CI invokes, and the rule that picks its checks has a
  home · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* critical-flow tests span parts and need a single owner. The gate serves every
element, so an element directory is the wrong owner; the task cycle decides the work to run, not
where its runner lives. As its own part, the gate carries its failures and criticality.
*Rejected:* gate inside the invariants element — shared work owned by one element; gate inside
task-cycle — code coupled to task steps; gate among repository configuration — its failures lose
their own part; critical-flow tests in individual elements — no one element owns a cross-part flow.

### WAY-56/1 — How much does one invariant entry hold, and what is its binding part?

An invariant entry states one invariant in one sentence, which is its binding part, and the
entry's fingerprint covers that sentence alone. The method of checking and the links that WAY-08
and WAY-17 require stand beside that sentence, not inside it. Everything else the entry carries
stays outside the fingerprint — such as its method of checking, the links it names beside the
sentence, its version and a declaration of a correction.

- **Change:** new decision
- **Scope:** invariants, relation-model
- **Based on:** none
- **Relations:** derives from WAY-22@dcf291ea · derives from WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: invariant-sentence-count · invariant-fingerprint-input.
  Level 2 for one invariant per sentence — an agent compares the change with the decision:
  - complies: "every version and review record in the log has every field of the template" as one
    entry; "every human verdict names who checked and when" as one entry;
  - violates: "binding sentences number one to three and contain no *should*" as one entry; the
    sentence on fields split into one entry per field.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* one invariant per entry has a fingerprint of its own, so a fix flags only what relies
on it (WAY-02) and a break tells whether its method catches it (WAY-08); the fingerprint moves the
version and fails citing tests (WAY-57), so it covers only what the invariant demands.
*Rejected:* a property with labelled conditions — a fix to one point flags every citing test; a
split wherever a commit can break part of a sentence — one entry per version of the log; the whole
entry as the binding part — a new method or a later link fails every citing test; a fingerprint per
field — every reference would name its field.

### WAY-57/1 — Is an invariant entry versioned?

An invariant entry carries a version number, starting at 1, and holds only its current wording,
and earlier wordings are read from git. When the entry's fingerprint differs from its fingerprint
on the commit the task branch left the main branch from, its version is one higher than there,
unless the entry declares a correction naming both fingerprints and the human who decides the
change under WAY-10 confirms, with the old and the new binding part in front of them, that the
meaning is unchanged; a change after which some test citing the entry would need a different
expected value is never a correction; when the fingerprint does not differ, the entry keeps the
version it has there. A check cites its invariant by identifier and version, in the form the
template gives, and fails the gate when that version is not the current one, while elsewhere a
reference to an invariant's version is historical and never flagged, as WAY-02 has it.

- **Change:** new decision
- **Scope:** invariants, relation-model, gate, task-cycle, part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-03@97d336a9 · derives from WAY-10@9b8b1401 ·
  narrows WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: invariant-version-number · invariant-version-new ·
  invariant-version-changed · invariant-version-unchanged · invariant-earlier-wording ·
  invariant-citation-version · invariant-correction-confirmation. Level 2 for what counts as a
  correction — an agent compares the change with the decision:
  - complies: a typo fixed under a declaration the deciding human confirms, with no test citation
    changed; "at most three" becoming "at most four" raises the version, and the old citation
    fails until the test is rechecked;
  - violates: "must" becomes "may" under a confirmed correction; a heading's code literal fixed
    under a declaration, though a test asserting it would need a new expected value; a script
    moves every citation to a new version, nobody checking the tests.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a read-only test cited by fingerprint would move with every typo, and by bare
identifier never, checking a meaning gone; a version moves with meaning; the human already deciding
the change confirms a correction, so no author-named kind silences anything; a forgotten raise
drifts silently, a needless one fails loudly.
*Rejected:* no version, as in the part map — typo flags or silent drift; earlier wordings kept in
the entry — they bind nothing, and readers have to pick; a hand-written version nothing compares — a
forgotten raise goes unseen; one correction for a whole change, by its author alone — an
author-named kind silences flags across entries; a declaration naming only the old fingerprint —
after the merge it fails or, repointed, silences the next change; a test citing an earlier version
— it checks what the product no longer promises.

### WAY-58/1 — What does an invariant entry record when it was recovered from what a product does?

An invariant entry that a human chose from what the product already did before the task writing it
began, as WAY-28 describes, and that names no decision entry of the product's log it derives from,
stands in `foundations/invariants.md` on the list of recovered invariants, in a row naming its
identifier, its current version, `searched: <…>` and `found: <…>`; no other invariant entry stands
there. *found* names the place of each source the search found that gives a reason for keeping the
behaviour or calls for a different one, or reads `nothing`; a place that only cites another is
followed to the place it cites, marked when that source is superseded, and *found* never states a
reason itself, nor one an agent infers. When an entry's binding part enters the foundation, the
gate reports whether its method passes on the commit the task branch left the main branch from and
fails there on a deliberate break, and the human deciding the change sets the row with that report
in front of them.

- **Change:** new decision
- **Scope:** invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-28@94d8ef12 · derives from WAY-22@dcf291ea ·
  derives from WAY-17@b1e26133
- **Verification:** level 1 — invariants: invariant-recovered-form · invariant-recovered-derived ·
  gate-fork-point-evidence. Level 3 for the row — the human deciding the change sets it with the
  gate's report in front of them, and the record of that decision names who and when.
  Level 2 for what counts as already done and what *found* holds — an agent compares the change with
  the decision:
  - complies: from a game's save module a human chooses "a save of another version is rejected
    whole", which takes a row; *found* reads `the comment above the save format's version constant
    at <sha>, decision D23 of the concept document`; an invariant written at a task's foundation
    step for a feature being built stands on no row;
  - violates: *found* reads "old saves are dropped because the rules may have changed"; *found*
    lists a comment explaining how the loader parses a save; an invariant on a field the task adds
    is marked recovered because its check cannot fail on the older commit.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* WAY-28 lets a recovered invariant bind before anyone knows why it holds; without the
row it reads like a chosen rule, hiding that its reason was never settled. *found* points to
places, never reasons (WAY-22), and to those against the behaviour too, which a human weighing it
most needs.
*Rejected:* the mark only where no cause is known — a cause in a code comment or a concept document
gives the rule two readings; a row for every entry naming no decision — an invariant for a feature
being built would read as recovered; the mark set by the gate's run on the older commit — a rule new
to the task can pass there too; a decision kept outside the log counted as named — nothing checks
it; the reason quoted in *found* — a why inside an invariant; an origin field "derived from a
decision" — it repeats WAY-17's link; an outside catalogue's requirement as a field — it is a fact,
named under WAY-17.

### WAY-60/1 — Where may a condition that decides an invariant stand?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation
change a human decides, or where a decision in the product's log or the pinned the-way places it.
An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}`
(WAY-61), while a state it compares may be the one on `{merge-onto}`, and states what is to hold on
the main branch alone as holding where `{merge-onto}` exists. A sentence bounding or equating a
quantity measured while the product runs names its bound or tolerance, statistic and population.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate
- **Based on:** none
- **Relations:** derives from WAY-22@dcf291ea · derives from WAY-56@0d6340a8
- **Verification:** level 1 — invariants: sentence-branch-names · sentence-gate-values. Level 2 for
  the rest — an agent compares the change with the decision:
  - complies: "every version and review record in the log has every field of the template"; "the
    list of violated invariants is a subset of its version on `{fork-point}`", the commit WAY-53
    chose;
  - violates: "every request is answered within the limit set in `config.py`"; "every fingerprint
    on `main` equals the current fingerprint of the decision it names"; "a commit that changes
    `template.md` also appends a decision version to the log"; a bound written "~2 seconds"; a
    sentence measuring a change against `{merge-onto}`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a condition outside the sentence moves unseen by the fingerprint (WAY-56), so it stands
only where moving it takes a decision; a branch names another commit by the hour; a change is
measured from the fork point, as a version is (WAY-57); a measured bound needs its statistic and
population.
*Rejected:* every condition in the sentence — two answers where a measure meets a definition or a
method; a closed list of places — it leaves out places a log uses; every place outside the
foundation forbidden — WAY-38 and WAY-53 place conditions in the product; an invariant kept aside
until its condition has a home — nothing counts it (WAY-51); a commit's parent as the base — a task
spreads one change over several commits.

### WAY-61/1 — How is an invariant's method of checking written, and how is its result read?

An invariant entry's method of checking is either a command the gate runs, which counts as a command
the product declares (WAY-38), begins with the name of the program it runs and is never a path alone,
or the path alone of a file a human assesses the product against; a command is the same on every run
and names no commit, branch or revision itself, and the commits its sentence names are values the gate
fills in from the template's closed list. A method checks what its sentence is about, as it stands on
the commit being checked, so a check fed input made up for it is the method of a sentence about that
check, never of one about the data the check reads. One run of a command may check many invariants,
and a method reads what another method's run left only where a decision places it, the gate then
running the first before the second; the result of an entry whose method is a command is the verdict
that run records, in a format from the template's closed list, for the entry's identifier and its
current version; a verdict recorded for another version is not its result, and a run that records
no verdict for the entry never gives it a pass.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-08@2343e09f · derives from WAY-16@5c1d60d4 ·
  derives from WAY-54@57b93cf6 · derives from WAY-57@4a838784 · derives from WAY-38@6e10c3fd ·
  derives from WAY-60@6e862c88
- **Verification:** level 1 — invariants: invariant-method-form · method-gate-values ·
  gate-verdict-per-entry · gate-pass-without-verdict · gate-method-order · test-runner-pass-line.
  Level 2 for what a method checks — an agent compares the change with the decision:
  - complies: a sentence about the log's fields names the decision guard run on
    `foundations/decisions.md`, one run giving each invariant a verdict; a sentence about the loader
    names a test handing it a save of another version; an exploratory test names the command
    starting an agent on the working product with its steps; a sentence on whether an image's text
    alternative describes it names the checklist a person assesses the page against;
  - violates: a sentence about the real log names as its method the guard's test, which feeds it
    made-up logs; a test asserting only the guard's exit code on the real log is the method of one
    of its invariants; an entry carries "runs as: script" beside its command; the gate gives every
    invariant a guard checks the guard's exit code; a command names the main branch where the
    sentence names `{fork-point}`.
  Level 2 for which run's output a method reads — an agent compares the change with the decision:
  - complies: the map guard reads a flow test's coverage file, as WAY-47 places it, after the gate
    runs that test;
  - violates: an invariant's method reads the record another invariant's guard run left, and no
    decision places that reading.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* the gate runs a method or hands it to a person (WAY-16), so prose is none; one run
serves many invariants, each needing a verdict of its own; a check that sees nothing passes quietly
(WAY-38); a branch resolved at run time answers by the hour (WAY-60).
*Rejected:* a kind named beside the method — a second value that can disagree (WAY-54); a form of
its own for an exploratory test — it looks like a human's path; the run's exit code as each
invariant's verdict — one broken rule fails all, a skipped one passes; one run per entry — a shared
check runs many times; a verdict for whichever version a check cites — a check for an old meaning
passes the raised entry; a check's tests on made-up input as the method of a sentence about real
data — they show the check works, not that the data holds; a method in prose — the gate cannot run
it.

### WAY-62/1 — What does an invariant entry name in the part map?

An invariant entry names the parts of the part map where a change can make its sentence false,
or `every` where a change to any part can. A change, against the commit its branch left the main
branch from, reaches an invariant that names `every` or a part the change touches, or whose method
names a file the change alters, whatever parts a file collecting entries gives that change
(WAY-44). The entry names no failure mode, critical flow or surface.

- **Change:** new decision
- **Scope:** invariants, part-map, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-16@5c1d60d4 · derives from WAY-44@2f2b6227 ·
  derives from WAY-61@4804d070
- **Verification:** level 1 — invariants: invariant-part-names · invariant-part-form · change-reach.
  Level 2 for which parts — an agent compares the change with the decision:
  - complies: the invariant on the log's fields names `decisions`, and a decision scoped to `gate`
    reaches it through its method's file; "every file git tracks matches the patterns of exactly
    one part" names `every`;
  - violates: that sentence names `part-map`, so a file added under `gate/` never reaches it; an
    entry names the flow it protects.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* invariants need what scope gives decisions (WAY-21): parts, not paths, which would
copy the map. A decision scoped to `gate` touches `gate`, not the log, so a method's files reach
the invariant too. A missing part fails silently, an extra one costs a run, so doubt names more.
*Rejected:* parts computed from what the method reads — a test's command names its test file, not
what it reaches; the invariant naming its failure mode, flow or surface — one link written at both
ends; the part holding the check — a file added elsewhere never reaches it.

### WAY-63/1 — What results does the gate report for invariants, and which make its command fail?

An invariant's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the
template's closed list, or `error` otherwise. The gate reports a result for at least every invariant
the change reaches and every invariant a critical flow names, and its command exits non-zero when
a result it reports is `error`, a listed invariant's is `pass`, an unlisted invariant's or a fact's
is `fail`, or a run records a failure for no entry, and zero otherwise.

- **Change:** new decision
- **Scope:** invariants, gate, part-map, task-cycle, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-61@4804d070 · derives from WAY-62@d9c21624 ·
  derives from WAY-08@2343e09f
- **Verification:** level 1 — invariants: invariant-method-form · gate-result-values ·
  gate-unchecked-reason · gate-reported-set · gate-exit-code. Level 2 for the reasons — an agent
  compares the change with the decision:
  - complies: a flow's list of parts with no coverage file is `unchecked` (WAY-47), as are a check
    needing a commit the gate filled in as not existing and the comparison of a product's glossary
    with the glossary of the-way in a repository that pins no the-way;
  - violates: a guard whose call to git fails reports `unchecked`; a human's `pass` stays in force
    after a change since the assessed commit reaches the entry; a critical flow's test is left out and
    the command exits zero.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-02

*Rationale:* a check can always call itself unchecked, so only listed reasons count; `unchecked`
leaves the command at zero, because an invariant may enter before its method can run (WAY-60,
WAY-61), and a human reads it (WAY-47). A product that pins no the-way, or pins a commit of it
holding no glossary, has no words of the process to compare its own with (WAY-34), so that
comparison is undecided, not failed.
*Rejected:* `unchecked` failing the command — every invariant without a method would fail every
change; an open list of reasons — any excuse passes; a third exit code — nothing reads it; a
human's verdict valid for the entry's version — it outlives changes to the product; no reason for
a product that pins no the-way — its comparison with the glossary of the-way records nothing, and
the gate reads `error` there.

### WAY-64/1 — Where do invariant and environment fact entries stand, and what identifies one?

Invariant entries stand in one file, `foundations/invariants.md`, and environment fact entries in
one file, `foundations/environment_facts.md`, each under an identifier made of words that no other
entry or withdrawn identifier of those two files or of the part map holds. An identifier either
file held on the commit the branch left the main branch from stays in it, as an entry or as a
withdrawn identifier giving why and naming its successors or `none`, and one it held as a withdrawn
identifier there never names an entry again. Splitting or merging environment fact entries, or
invariant entries held there, gives each entry that comes out of it a new identifier, and any other
change keeps it.

- **Change:** new decision
- **Scope:** environment-facts, invariants, part-map, elements-common, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46 · derives from WAY-56@0d6340a8 ·
  derives from WAY-57@4a838784
- **Verification:** level 1 — invariants: identifier-holders · map-invariant-names ·
  invariant-identifier-form · invariants-file · invariant-identifier-persistence ·
  invariant-withdrawal-persistence · withdrawal-successors · environment-facts-file ·
  fact-identifier-form · fact-identifier-persistence · fact-withdrawal-persistence ·
  fact-withdrawal-successors. Level 2 for what counts as a split — an agent compares the change
  with the decision:
  - complies: an invariant drops a clause and keeps its identifier at a raised version (WAY-57);
    an entry taking in a clause of another keeps its identifier, and the other is split; a fact
    joining JSON and JSON Lines splits into two new identifiers, the old withdrawn naming both;
  - violates: an entry drops a clause that reappears as a new entry and keeps its identifier; a
    changed meaning is withdrawn naming `none` and restated under a new identifier.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* words, so a citation says what it leans on; a version carries a change of meaning
(WAY-57, WAY-79), so only a split or merge changes an identifier, and a withdrawn one shows a
citation where the meaning went.
*Rejected:* a number with a prefix — a mistyped number names another entry; a file per part — an
entry naming several parts or `every` has none; identifiers unique within a file — a reference
would need its element; one half of a split keeping the identifier — nothing sends its reader to
the other half; a fact shown false deleted — an older citation leads nowhere, and the fact can come
back; every identifier ever written kept — one dropped before the main branch was never cited.

### WAY-65/1 — How does a check cite its invariant, and which files are invariant tests?

A check cites, at the smallest unit whose outcome a run records on its own, each invariant it gives
a verdict for as `invariant: <identifier>/<version>`, and a run records no verdict for an invariant
its check does not cite. A file is named as a check's data by a line `data: <path>`, and a file is
an invariant test of a change when it is one on the commit the branch left the main branch from or
on the commit being checked. Where several checks cite one invariant in a run, the run gives it
`pass` only when each of them records `pass`.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, relation-model, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-03@97d336a9 · derives from WAY-17@b1e26133 ·
  derives from WAY-57@4a838784 · derives from WAY-61@4804d070
- **Verification:** level 1 — invariants: invariant-citation-version · invariant-citation-target ·
  data-line-target · invariant-tests-of-change · test-runner-pass-line · gate-verdict-per-entry.
  Level 2 for where a citation stands — an agent compares the change with the decision:
  - complies: the decision guard cites `log-entry-field-presence/1` at the rule checking
    fields; a test comparing a load with a recorded save names the save on a `data:` line;
  - violates: a test file cites at its top every invariant its tests serve.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a citation stands where the verdict is given (WAY-61); a pass from one check would
hide another's fail; counting either commit keeps a dropped citation or deleted file protected
(WAY-03); a test names its data as the dependent end (WAY-17).
*Rejected:* the paths a method names as the invariant tests — a method names data, not checks; one
citation per file — one broken check fails all it serves (WAY-61); only files citing on the commit
checked — dropping a citation frees the file.

### WAY-68/1 — What happens to a check that gives different verdicts on one commit?

A check that cites an invariant and records both `pass` and `fail` for one commit is answered by a
foundation change, quarantine last and never for an invariant a critical flow names. A quarantine
stands in `foundations/invariants.md`, names the entry's current version and an end date, and its
result is `unchecked` until the checked commit's committer date passes that date, then `error`.
Until it is answered, a recorded `fail` stays the entry's result on that commit, whatever a later
run records.

- **Change:** new decision
- **Scope:** invariants, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-08@2343e09f · derives from WAY-61@4804d070 ·
  derives from WAY-63@f16348c8
- **Verification:** level 1 — invariants: quarantine-position-form · quarantine-flow-invariants ·
  gate-quarantine-result. Level 2 — an agent compares the change with the decision:
  - complies: a save-load test fails, then passes, on one commit; the panel accepts waiting for the
    load signal;
  - violates: a failing test is called flaky with no `pass` recorded on that commit; a fixed-wait
    failure is quarantined instead of fixed as a change of mechanics; a green rerun is taken as the
    commit's result while the `fail` it follows stands unanswered.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* a flipping test stops every task it reaches and the implementer may not touch it
(WAY-03), so "just flaky" needs evidence; a green rerun undoing a fail makes rerunning the answer;
a critical flow's test runs on every change (WAY-45); moving the end date is a human's foundation
change (WAY-10).
*Rejected:* a row of the list of violated invariants — it judges the product, not the check
(WAY-51); a quarantine field in every entry — every entry pays for a rare case; a count of passes
in a row to enter — k of n decides that (WAY-08); the date of the run — the result would follow
the hour; deletion once the date passes (GitLab) — the check is weakened.

### WAY-69/1 — Who writes an invariant's sentence, its check and its deliberate break, and what may the check compute for itself?

An invariant's sentence and a check that cites it come from separate acts by different agents, and
the deliberate break the check is accepted on is written from the sentence by an agent other than
the check's author, with that check and the files it reads out of its input. A check that cites an
invariant takes the input it asserts on and the value it expects written out, wherever the code its
invariant is about would otherwise compute either; only the side it compares against comes from the
run.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate, task-cycle, relation-model
- **Based on:** visible-scoring-reward-hacking@39a85ced · oracle-in-loop-building@d13c8e26
- **Relations:** derives from WAY-08@2343e09f
- **Verification:** level 3 for who writes what — the human deciding the foundation change assesses
  how the work was handed out, and the record of that decision names who and when. Level 2 for what
  a check computes — an agent compares the change with the decision:
  - complies: a guard's test carries its expected wording and fingerprint as literals, so a longer
    fingerprint fails it;
  - violates: a test builds its reference by calling the code its invariant is about, and expects
    that call's message; a test reads the value it expects, at run time, from the file its
    invariant is about.
- **Review when:** no model in the range of fact oracle-in-loop-building is Active in Anthropic's
  table of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a break chosen by a check's author aims at what the check does, not what the sentence
says, and a check by the sentence's author inherits its reading; two sides computed by one code move
together, and the test stays green unseen. This takes the visible-scoring finding across publishers
(WAY-85).
*Rejected:* hiding checks from the executor — it costs honest work; one agent writing all three under
a written rule — prose stops nothing; a field naming the writers — nothing reads it; the expected
value alone written out — the input still moves with the code; a `data:` line naming each file a
verdict leans on — every tracked file turns read-only.

### WAY-71/1 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every entry of its kind —
in every version of a decision and every review record, the fields their forms give — holding a
value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there,
`TODO` that something is missing. The main branch holds `TODO` only in an invariant's or a fact's
*Method*, and in an invariant's *Rests on* until the facts element has entries. A guard reports a
missing field, or a word not given it, as an error.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: log-entry-field-presence · log-entry-field-words ·
  log-entry-merge-todo · map-entry-field-presence · map-entry-field-words ·
  invariant-entry-field-presence · invariant-entry-field-words · invariant-entry-merge-todo ·
  fact-entry-field-presence · fact-entry-field-words · glossary-entry-field-presence ·
  glossary-entry-field-words · glossary-entry-merge-todo · decision-verification-level ·
  decision-change-kind · review-when-form · review-next-check. Level 2
  for what `none` states — an agent compares the change with the decision:
  - complies: an invariant whose author searched the log and found no decision it derives from
    reads `Derives from: none`; a decision whose source is silent on what it rests on reads
    `Based on: TODO — <what is missing>`;
  - violates: an invariant reads `Derives from: none` though nobody searched the log; a decision
    reads `Based on: none` where its source says nothing of what it rests on.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* an omitted field looks forgotten (WAY-58); an undefined value misleads. A missing
*Method* yields `unchecked`, not a false pass (WAY-63). Before facts have entries, an invariant can
expose a needed fact as `TODO` instead of falsely claiming `none`; once they do, the gap must be
resolved.
*Rejected:* a decision for invariants alone — every element would need a copy; a wider scope for
WAY-05 — it answers how a decision entry is written; both words in every field — a word with no
meaning; optional fields left out when empty — intended and forgotten gaps look alike; for facts, a
state field and a ratcheted list — three mechanisms where one serves.

### WAY-72/1 — In what language is a product's foundation written?

A product's foundation is written in English, whatever language the product shows the people who
use it and whatever language its team speaks.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the foundation of a game whose players read Polish, built by a team that speaks
    Polish, is written in English;
  - violates: a product starts its decision log in Polish because its users and its team speak it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* every template's fields are English, and the words the rules of form keep out (WAY-05,
WAY-60) are English words: an entry in another language passes those rules without a word, so they
look kept while checking nothing. One language also makes the entries of the-way examples for every
product.
*Rejected:* entries in the product's language, each check's words listed per language — a list for
every language, and one without a list checked by nothing; the file's language, asked while it has
no entries — word checks go silent on other languages; a guard reporting other languages unchecked
— recognising a language needs more than the standard library (WAY-38).

### WAY-73/1 — Which entries name an environment fact?

An invariant's *Rests on* names every environment fact holding a condition that decides whether a
commit makes its sentence true, and no other fact. A fact holds such a condition when, read
otherwise, it would change whether some commit makes the sentence true, or change a value the
sentence copies from it. A fact that is only a reason for a decision the invariant derives
from stands in that decision's *Based on* alone; every environment fact on the main branch is named
by an invariant's *Rests on* or by a decision's *Based on*, and on a task branch, a fact that nothing
names is a warning.

- **Change:** new decision
- **Scope:** invariants, decisions, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-17@b1e26133 · derives from WAY-60@6e862c88
- **Verification:** level 1 — invariants: fact-dependants. Level 2 for which facts an invariant's
  *Rests on* names — an agent compares the change with the decision:
  - complies: `script-imports` rests on `python-stdlib-modules`, not on a finding a decision it
    derives from quotes;
  - violates: an invariant rests on the report of a past failure its decision quotes; an invariant
    bounding a page's load time by an outside standard's threshold reads `Rests on: none`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* a fact holding a condition changes whether the sentence holds with no commit, so
*Rests on* is its only path to the invariant; a mere reason reaches it through its decision
(WAY-31). A link is written at the dependent's end (WAY-17), so a fact nothing names is seen from
nowhere.
*Rejected:* every fact in the *Based on* of the decisions it derives from — flags invariants that
still hold, and misses conditions no decision quotes; the choice left to each author — "rest on"
reads two ways; no check on unnamed facts — facts outlive their readers; an error on the task branch
too — a fact written before its dependent would break the branch midway.

### WAY-74/1 — What form does the-way's own record of a run take?

The-way's own record of a run is a JSON Lines file at the one `.jsonl` path the command names,
which git ignores and the gate clears before the run. It holds a line per verdict a check gives an
invariant or a fact, and per failure recorded for no entry. A line holds `check`, `verdict` as
`pass`, `fail` or `unchecked` beside a `reason` the template of the invariants element lists,
`invariant` or `fact` as `<identifier>/<version>` or `invariant` as `null`, and at most
`description`.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, repository, environment-facts,
  elements-common
- **Based on:** JSON Lines holds one JSON value on each line: json-lines@f16c5b84.
- **Relations:** derives from WAY-61@4804d070 · derives from WAY-63@f16348c8 ·
  derives from WAY-65@581724fc
- **Verification:** level 1 — invariants: run-record-form · run-record-path · run-record-lines.
  Level 2 for the report beside the record — an agent compares the change with the decision:
  - complies: the decision guard, given a record's path, writes its verdicts there and still
    prints its report for a person;
  - violates: a guard writes its verdicts only into its report.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* lines survive a run stopping halfway, and an invariant without one gets no pass
(WAY-61); the standard library reads JSON, which escapes any description (WAY-38); a stale file
gives verdicts of a run that never happened, a tracked one changes every run; each key has a
reader.
*Rejected:* plain text lines — spaces in a description need their own syntax; JUnit XML — its unit
is a test case, not an invariant; a product's format — the gate reads it through an adapter
(WAY-61); the run's output as the record — a person loses the guard's report; `pass` and `fail`
alone — a check unable to read a coverage file could only stay silent; the commit, moment and tool
versions in every line — nothing reads them; one key `entry` for both — a rename across every guard
and test; a fact's verdict under `invariant` — the key would lie.

### WAY-76/1 — How much does one environment fact entry hold?

An environment fact entry states in one sentence one fact that one edition of one source says, with
one reason to change, and nothing its sentence says is an invariant. Pages of one document published
together in one edition count as one source, and two facts from one edition about different things
stand as two entries.

- **Change:** new decision
- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-22@dcf291ea
- **Verification:** level 1 — invariants: fact-sentence-count. Level 2 for what one sentence may
  hold — an agent compares the change with the decision:
  - complies: git's path-pattern rule for attributes files, with its page's two exceptions, is one
    fact, without what `git check-attr` prints; git's ignore rules, from a page of the same edition,
    stand as a second entry;
  - violates: the digest SHA-256 gives and the octets UTF-8 uses stand in one entry; "the
    repository declares Python 3.14" is written as a fact.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a fact is reviewed when its source changes, so what changes together stands together:
two sources in one entry let a new edition of one flag every entry resting on the other. An
invariant written as a fact would never be checked on the commit that breaks it.
*Rejected:* git's pattern rule and what `git check-attr` reports in one entry — the second is about
a method's tool, and no commit changes it (WAY-73); both as facts in *Rests on* — the second holds
no condition of the sentence (WAY-73).

### WAY-77/1 — What does an environment fact's *Holds for* name?

An environment fact names in *Holds for* what its sentence is true of — a tool and its version, a
platform, an edition, or the models a study measured — and never a word whose meaning moves with
the date, such as "latest"; where the source publishes no editions, *Holds for* says so. A range
the product declares for itself stands in the sentence of an invariant, never in a fact.

- **Change:** new decision
- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: fact-scope-word. Level 2 for what a range names — an agent
  compares the change with the decision:
  - complies: the standard library's modules are a fact for CPython 3.14, while "the repository
    declares Python 3.14" is an invariant; the fact about JSON Lines reads "JSON Lines, which
    jsonlines.org publishes without versions";
  - violates: a fact's method reads the product's `.python-version` to choose which interpreter to
    probe; *Holds for* reads "jsonlines.org as read on 2026-09-26".
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a fact is true in the range it names, and a newer range does not refute it; "latest"
would make its verdict change with the date, not the world. The product's range changes with a
commit, so it belongs to an invariant, meeting the fact through *Rests on* (WAY-73).
*Rejected:* a fact's method reading the product's declared version — a sentence about the product in
a fact; a script comparing the product's range with the fact's — *Holds for* is prose, and the
invariant's writer sees both; the date read in *Holds for* of a source without editions — every
re-reading would flag its dependants for nothing.

### WAY-78/1 — What is the binding part of an environment fact entry?

The binding part of an environment fact entry is its sentence together with its *Holds for*, and
the entry's fingerprint covers the sentence followed by the value of *Holds for*, computed as
WAY-02 says. The source, its passage and the date read, and the method stay outside it, and no
digest of the source's text is kept.

- **Change:** new decision
- **Scope:** environment-facts, relation-model, invariants
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: fact-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* what relies on a fact relies on its claim and the range it holds for; the source and
its date change at every re-reading, so flags from them would mean nothing; a source that changes
fails the watch (WAY-82). Text changed beside the quoted passage passes unseen, an accepted cost.
*Rejected:* the source's text in the fingerprint — a rebuilt page flags every dependent (WAY-82);
the sentence alone — a widened range passes unseen; a digest of the passage (as a lock file keeps
one) — the quoted passage is already the anchor.

### WAY-79/1 — Is an environment fact entry versioned?

An environment fact entry carries a version number, starting at 1, and holds only its current
wording. When its fingerprint differs from its fingerprint on the commit the task branch left the
main branch from, its version is one higher than there, and otherwise it keeps the version it has
there. A check citing a fact at a version other than the current one fails the gate.

- **Change:** new decision
- **Scope:** environment-facts, relation-model, gate, elements-common
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: fact-version-new · fact-version-changed ·
  fact-version-unchanged · fact-citation-version. Level 2 for a raise — an agent compares the
  change with the decision:
  - complies: a typo fixed in a fact's sentence raises the version; a range widened from CPython
    3.14 to 3.14 and 3.15 raises the version; the probe citing the old version fails until
    rechecked;
  - violates: a typo fixed in a fact's sentence keeps the version; every citation moved to the new
    version by a script, with no one checking the probe.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a version pins a method's result to the binding part it checked: a probe cites the
fact by identifier and version and fails once the meaning moves, as for invariants (WAY-57); a
fact's history binds nothing, so earlier wordings are read from git.
*Rejected:* no version, as in the part map (WAY-43) — results keyed by fingerprint, a second
mechanism beside WAY-57's; a correction keeping the version, as for invariants — it saves only
editing the `fact:` lines, whose failure shows the raise anyway.

### WAY-80/1 — What is an environment fact's source?

Every environment fact entry names its source: an edition with its publisher's own address, or a
page without editions with its closest archived copy, giving the place, the passage word for word
and the date read; or an observation naming the command, the tool and its version, the platform
and the date it ran. The sentence says no more than its source, and a model's memory, an agent's
paraphrase or a text quoting the source is no source. A fact resting on a whole section of rules
quotes the sentence of its source that sets those rules and names the section by its place alone,
where the edition has an address of its own.

- **Change:** new decision
- **Scope:** environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: fact-source-form. Level 2 for what the sentence may say,
  what counts as a source and how a whole section of rules is cited — an agent compares the change
  with the decision:
  - complies: the JSON Lines fact quotes "strongly recommended but not required" and says the final
    terminator may be left out; the git path patterns fact quotes the sentence handing matching to
    `.gitignore` rules and names that section by place;
  - violates: the sentence says every line ends in `\n`; the source is the model's recollection of
    a page, or a blog post quoting the RFC; a fact on a pattern syntax quotes its rules one by one,
    or only the rules the product uses.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* an edition with its own address does not change under the citation, a passage word
for word lets a re-reading compare two texts, and the date says when that held. An observation is a
source when anyone can rerun it; a recollection or a quoting text carries a paraphrase's drift.
*Rejected:* a source named by its work alone — a new edition changes what the citation says; a
summary in place of the passage — the drift this decision exists to stop; a whole section of rules
narrowed to those the product uses — a pattern outside them rests on no fact; such a section quoted
rule by rule — a standing `TODO` in the source.

### WAY-81/1 — How is an environment fact's method written, and on which release of its tool does a probe's verdict count?

A fact's method is a command beginning with the program it runs, the path alone of a
file a human re-reads the source against, or `TODO`; a command probes the behaviour the sentence
states, watches the state its source publishes, or both. A command sets what it can of the
runner's configuration that could change its verdict, and cites each fact it gives a verdict for as
`fact: <identifier>/<version>`, and a run records no verdict for an uncited fact. Where a fact's
*Holds for* names a release of the tool its probe runs, the probe reads the release it runs on and
records it in the `description` of its line; a `fail` on any release is a `fail`; a `pass` counts
only on a release *Holds for* names, a build of it included, and on another the fact is
`unchecked`.

- **Change:** new decision
- **Scope:** environment-facts, gate, invariants
- **Based on:** none
- **Relations:** derives from WAY-61@4804d070
- **Verification:** level 1 — invariants: fact-method-form · fact-citation-target ·
  fact-verdict-citation. Level 2 for what a command asks and what it sets — an agent compares the
  change with the decision:
  - complies: the fact on path patterns runs `git -c core.ignorecase=false check-attr` on patterns
    the page's rules decide; the fact on SHA-256 probes the digests NIST publishes for it; the fact
    on JSON watches `obsoleted_by` of its RFC and that its passage still stands;
  - violates: a probe asks `git --version` and compares the number in place of the behaviour; a
    probe relies on the git configuration of the machine it runs on.
  Level 2 for the release a probe's verdict counts on — an agent compares the change with the
  decision:
  - complies: run on git 2.56.0, the probe of a git 2.55.0 fact writes `git 2.56.0` in
    `description`; it fails the fact where the behaviour differs and leaves it `unchecked` where it
    agrees; on Git for Windows 2.55.0.windows.3, a build of git 2.55.0, its pass counts; the probe
    of the SHA-256 fact, whose *Holds for* names no tool release, reads none;
  - violates: the probe passes the fact on git 2.56.0; it skips on another release without asking
    about the behaviour; it writes the release under a key of its own beside `description`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* the forms are WAY-61's, so both elements read alike; a version number says nothing
of what a release does; the machine running a method changes its fidelity, not the truth; a pass on
another release says nothing of the named one, while a fail there still calls for review.
*Rejected:* a kind of method named beside it — the form says it (WAY-54); a version number in
place of the behaviour — it trusts the label; the runner's configuration or the tool's release as
a fact in *Rests on* — it changes fidelity, not truth (WAY-73); a pass counted on any release — it
passes a fact about another release; the release under a key of its own — nothing reads it
(WAY-74).

### WAY-82/1 — When does an environment fact's method run, and what fails its watch?

A fact's method runs on every change that enters or rewords its entry or alters a file its command
names, and by the clock, run on the main branch, which records each verdict and exits non-zero on
a `fail` or an `error`. Elsewhere a fact's `fail` stops no change; a watch fails on a published
change to its edition or when its passage no longer stands, and an announced revision fails nothing.

- **Change:** new decision
- **Scope:** environment-facts, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-60@6e862c88
- **Verification:** level 1 — invariants: gate-fact-run · fact-clock-exit · gate-exit-code. Level 2
  for what fails a watch — an agent compares the change with the decision:
  - complies: RFC 8259 gaining `obsoleted_by` fails the watch of the fact citing it; NIST's notice
    that it will revise FIPS 180-4 fails nothing; the passage quoted from jsonlines.org vanishing
    from the page fails its watch;
  - violates: a change touching no fact fails the gate on a fact's `fail`; the clock exits zero
    while a fact results `fail`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* the world changes with no commit, so in the gate of an unrelated change a fact's
verdict would follow the date (WAY-60); the clock gives the world its own rhythm. An announced
revision is a prediction, which belongs in *Review when* (WAY-24).
*Rejected:* facts checked in every change's gate — the verdict follows the date; one review date
for every fact — sources change at different paces; an announced revision failing the watch, once
or as a standing flag — a review with no possible outcome.

### WAY-83/1 — Where does a human verdict stand, and how long is it in force?

A human verdict on an invariant or an environment fact stands in a row of
`foundations/human_verdicts.md` naming the entry, its version, the verdict, who, when, the commit
assessed and *Until*, and counts only for the entry's current version. An invariant's verdict, with
`none` in *Until*, lapses when a change since that commit reaches the entry; a fact's lapses after
the date in *Until*, which the gate compares with the checked commit's committer date and the clock
with the day it runs.

- **Change:** new decision
- **Scope:** invariants, environment-facts, gate, elements-common
- **Based on:** none
- **Relations:** derives from WAY-63@f16348c8
- **Verification:** level 1 — invariants: human-verdict-invariant-row · human-verdict-fact-row ·
  gate-human-verdict. Level 2 for the clock — an agent compares the change with the decision:
  - complies: the clock, run on a day after a fact's *Until*, counts no human verdict for that fact;
  - violates: the clock compares *Until* with the committer date of the commit it runs on.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a path method gives no result until a person assesses (WAY-61, WAY-81), and WAY-08
asks for a trace; a row is visible, fixable and checkable; one file serves both, as only the lapse
differs; the gate's date follows the commit, the clock's the world.
*Rejected:* the verdict in a commit message — invisible to a reader of the foundation, never
fixed, often written by an agent; waiting until a first verdict is needed — the rule on dated
verdicts would stay dead.

### WAY-84/1 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can
open it, a host's access rule — is an environment fact whose method reads that state where it
lives, or is re-read by the person who sets it where reading it takes their credentials. A choice
of such a setting is a decision only where the product declares it, and that decision rests on the
fact. A fact about the visibility of a repository the product links to names that one repository,
and its method reads it anonymously.

- **Change:** new decision
- **Scope:** environment-facts, decisions
- **Based on:** github-private-repository-response@e0f7ced2
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: each repository this one links to has its own fact on whether an anonymous reader can
    open it; a condition on who can open this repository rests on a fact its owner re-reads, with a
    dated verdict; no decision on this repository's visibility is written, as the repository
    declares none;
  - violates: a probe decides the repository is private from an anonymous 404; one fact lists
    every repository this one links to; a decision "the repository is private" is written where
    the product declares no visibility.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* such a setting changes with a click and no commit, so a method run against the world
alone sees it move, as for a fact; where only the setter can read it, a change between re-readings
goes unseen. A decision needs someone who chose; otherwise no commit could check it.
*Rejected:* a field naming who sets the setting — a failed run shows without it; a decision and a
fact for every such setting — a decision where nobody chose; a token on the clock's machine — a
secret, and a new reason to be unchecked; a verdict from an anonymous 404 and the repository's
`origin` — its fidelity depends on who runs it.

### WAY-85/1 — How is a finding of a study written as an environment fact?

A finding of a study stands as an environment fact recording what the study measured, in the
version of the paper its source names, with *Holds for* naming the measured models by the dated
identifiers the study gives, or by its own names where it gives none. That the agents of this
process behave the same is a prediction, written in *Review when* of each decision citing the fact
as a state a script can check, never in the fact. A decision citing a finding none of whose
measured models the publisher of this process's models lists says in its rationale that it takes
the finding across publishers, and carries no such state.

- **Change:** new decision
- **Scope:** environment-facts, decisions
- **Based on:** anthropic-model-states@640ad66c
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the finding behind WAY-03 is a fact holding for arXiv:2510.20270v1 and the three
    Claude models it measured; WAY-03's *Review when* waits for no model in that fact's range being
    Active in Anthropic's table; WAY-69, citing a finding on another publisher's model only, says it
    takes the finding across publishers;
  - violates: the fact says "Claude models change tests" with no version and no models; the fact
    carries a field saying the finding still applies to this process's agents; a decision citing a
    finding on other publishers' models only carries a state met the day it is written.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* what a paper measured on given models is true for good; that this process's agents
behave the same is a bet that ages as those models leave service, and bets already have *Review
when* (WAY-24). Named models let a script check it against the publisher's table.
*Rejected:* the transfer as a field of the fact — a second mechanism for predictions beside WAY-24,
and a fact no longer true or false today.

### WAY-86/1 — How does a catalogue of requirements or a binding rule reach a product?

A voluntary catalogue of requirements binds a product only through a decision adopting it that
names the catalogue, its edition, the level or list taken and the area of the product, and a
requirement an invariant takes a condition from is an environment fact. A binding rule — a law,
a contract, a licence — needs no adoption: what it requires is an environment fact, and the
product is held to it until a human settles, in a decision, that the rule does not apply. An agent
that notices a likeness to a requirement nothing has adopted or applied asks a human.

- **Change:** new decision
- **Scope:** environment-facts, decisions, invariants
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a decision adopts WCAG, naming its edition, level AA and the screens covered; an
    invariant taking a criterion's condition rests on that requirement's environment fact; the
    attribution an icon licence requires is an environment fact, and the invariant crediting the
    icons' author rests on it;
  - violates: an agent writes an invariant from an ASVS requirement because the code looks like
    it, with no adopting decision; a licence is left out because nobody adopted it; "the licence
    applies to the product's icons" is written as an environment fact.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a voluntary catalogue binds only because someone chose it; without that choice an
agent would bind the product to whatever it recognised. A law binds whether chosen or not, and
holding the product to it until a human settles otherwise makes silence raise checks rather than
remove them.
*Rejected:* a field naming the kind of source — no reader until a product adopts a catalogue or
takes on a binding rule (WAY-05); a script matching adopted requirements to facts and invariants —
the same, and WAY-73 already catches an unnamed fact; "the rule applies" as an environment fact — a
commit removing what the rule covers would make it false (WAY-76).

### WAY-89/1 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and
the declared version moves when the version in use leaves bugfix support, never because a newer
version comes out.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, gate,
  installation, repository, task-cycle
- **Based on:** python-314-bugfix-status@cb6aa573 · python-release-binaries@6d2c12f8 ·
  https://raw.githubusercontent.com/python/peps/b53285d29f16cc743a7a6339c947c49ccf70c525/peps/pep-0745.rst
  § Bugfix releases — "3.14.14: Tuesday, 2027-10-05 (Final regular bugfix release with binary installers)";
  read 2026-09-30
- **Relations:** none
- **Verification:** level 1 — invariants: python-version-declared · script-imports.
- **Review when:** the status of Python 3.14 in the table of versions of the Python Developer's
  Guide no longer reads "bugfix" · check by: 2027-10-05
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* one declared version, not a floor, because a floor gives a script's verdict per
interpreter; the end of bugfix support sets the move because the Python project publishes no new
binaries during subsequent security-only support; the price: a product pinning the-way provides
exactly this version (WAY-34, WAY-38).
*Rejected:* the newest release, unnamed — the verdict depends on the date; "3.12 or later" with an
invariant per version admitted — a fact and a verdict for each; 3.12 alone — past its bugfix
support; a move at each new release — a yearly review nothing here needs; a move at the end of
security support — years without installers.

### WAY-90/1 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

A decision's *Based on* quotes every citation with its source, given as WAY-80 gives a fact's
source; once the environment facts element has entries, it names a fact entry instead for every
citation that, stopping being true today, would send the decision to review — a finding about agents
or models, the behaviour of a tool the process uses. A fact named there carries its fingerprint, as
`<identifier>@<fingerprint>`, renewed as WAY-31 renews a relation's.

- **Change:** new decision
- **Scope:** decisions, environment-facts, relation-model
- **Based on:** none
- **Relations:** derives from WAY-17@b1e26133
- **Verification:** level 1 — invariants: based-on-fact-fingerprint · based-on-fact-fingerprint-value.
  Level 2 for which citations become entries — an agent compares the change with the decision:
  - complies: the ImpossibleBench finding behind WAY-03 becomes a fact entry named in its *Based
    on*; a past failure a decision cites stays quoted with its source;
  - violates: a precedent of how Packwerk handles its todo files becomes a fact entry with a probe;
    a finding about models stays quoted after the element has entries.
  Level 2 for how a citation gives its source — an agent compares the change with the decision:
  - complies: a paper's finding is quoted with the edition's address, the place and passage, and
    the date read;
  - violates: a finding is quoted with its authors and year alone.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* only a citation whose change would send the decision to review needs an entry to be
flagged by; a precedent, a past event or a finding about people with no lapse date sends nothing.
The fingerprint carries the fact's change to the decision, as to an invariant (WAY-31).
*Rejected:* every citation as an entry — many entries with methods nobody runs; a fact named by its
identifier alone — a changed fact would flag no decision; the partners of the part map's external
context as linked facts — a new link with no known consumer.

### WAY-93/1 — Where do glossary entries stand, and what identifies one?

Glossary entries stand in one file, `foundations/glossary.md`, each under its term as the foundation
writes it in running text, which no other entry there holds. Terms are a space of their own, and a
change that makes a term read like an identifier of the part map, the invariants or the environment
facts is a warning, after which one side is renamed where the two name different things; in the-way,
a term that names an element raises none against the part whose files include
`elements/<identifier>/`. The file opens with a title and a paragraph saying what it holds, and holds
no other heading than its entries.

- **Change:** new decision
- **Scope:** glossary, part-map, invariants, environment-facts
- **Based on:** none
- **Relations:** narrows WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: glossary-file · glossary-file-sections · glossary-term-holder
  · glossary-term-collision. Level 2 for what follows the warning — an agent compares the change with
  the decision:
  - complies: a new term "repository" raises the warning against a part `repository` meaning
    something else, and one is renamed; the term "part map" raises none against the part `part-map`;
  - violates: the warning on "repository" is cleared as the same thing because the names are spelt
    alike; a renamed term keeps its entry under the new word while the old word stays usable.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a sentence depends on a term by its word (WAY-94), so the word as the text writes it
heads the entry. A term and an identifier that read alike still meet in the text, so the change
bringing them together is shown once, when the name is chosen.
*Rejected:* terms in the shared space of identifiers (WAY-64) — a word a part takes would stay
undefined; an identifier of the concept apart from its word — names no reader uses; the warning for
every part named after its element — every *Scope* and *Part* value naming one renamed; a warning at
every run of the guard — people learn to ignore it; a list of withdrawn terms — *Avoid* already holds
the old word.

### WAY-94/1 — What does a glossary entry hold, and what is its binding part?

A glossary entry holds one definition of its term and two fields: *Avoid*, each other word for what
the term names with what it is confused with — the term's last word standing for the whole term is
no other word — and *Not*, each meaning the word carries or carried in the files of `foundations/`,
the elements' templates and the part the elements share, besides its definition and a meaning a
reader who knows the product's field gives it, with what carries it. The definition is the binding
part, and a sentence depends on a term by using its word, carrying no fingerprint.

- **Change:** new decision
- **Scope:** glossary, relation-model
- **Based on:** none
- **Relations:** narrows WAY-02@3ffcbd46 · derives from WAY-04@29a75d2c
- **Verification:** level 1 — invariants: glossary-entry-field-presence · glossary-entry-field-words.
  Level 2 for the binding part — an agent compares the change with the decision:
  - complies: an invariant's sentence uses "verdict" with no fingerprint, and a changed definition of
    "verdict" lists it for review;
  - violates: a sentence cites the term as `verdict@<fingerprint>`; a changed *Avoid* is treated as a
    change to the entry's binding part.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-01

*Rationale:* a fingerprint at every use would flag, at each changed definition, every sentence using
a common term — flags people clear unread (WAY-02) — so a changed definition's uses are reviewed
instead (WAY-97). A term's last word is the term shortened, and banning it would ban the term's own
uses.
*Rejected:* *Avoid* and *Not* in the binding part — they change mechanically and no dependant reads
them; a reader's meaning in *Not* — the reader brings it along; a field of neighbouring words — the
definitions carry the difference (WAY-96); a field of forms the endings miss — it makes a second word
legal and empties *Avoid*; worked examples run as tests, an area of meaning, broader and narrower
terms, an allowed synonym, a list of uses, the code's name for a term — nothing reads them, or they
are computed; a field for a definition's source or the decision that set it — no entry needs one.

### WAY-95/1 — Which words take a glossary entry, and in which glossary?

A word takes a glossary entry when it stands in the binding part of an entry of the foundation or in
the rules of an element's template or of the part the elements share, and at least one of its uses in
the files of `foundations/`, the elements' templates and the part the elements share carries a
meaning a reader who knows the product's field would not give it; an agent finds the candidates and
a human chooses. A word's definition stands in the glossary alone, and a closed list of values a
guard reads stays in its template with what each value means. The glossary of the-way holds the
words of the process, and a product's glossary holds the words of its domain; a product takes the
words of the process from the-way at the commit it pins and defines none of them again, and in the-way,
whose product is the process, the two are one file.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: glossary-term-use · glossary-process-terms. Level 2 for
  which words take an entry, where a definition stands and which glossary holds it — two uses carry
  two meanings when a definition true of one is false of the other, a noun naming one occurrence of
  what its verb does, or what does it, carries the verb's meaning, a word naming what a kind of entry
  records names the entry that records it too, and a word naming what a rule computes keeps the
  meaning a reader of the field gives it; an agent compares the change with the decision:
  - complies: "clock", used for a command and for a deadline, takes an entry with one meaning;
    "digest", used only as SHA-256 uses it, takes none; "run", used for running a command and for
    text running across lines, takes none; "critical flow" names the flow and its entry of the part
    map with one meaning; "criticality", computed for a part by a rule of the part map, takes none;
    the kinds of change of a decision stay defined in the decision template; a word used plainly and
    for a term becomes the term or has its other uses rewritten; a game's glossary
    defines "level" and uses "verdict" as the glossary of the-way defines it at the pinned commit;
  - violates: every noun of the decision log takes an entry; a decision defines a term in its binding
    sentence while the glossary holds another definition; the glossary defines "criticality" by the
    rule that computes it; a word takes an entry for its plain meaning only, to hold its *Not*; a
    game's glossary gives "verdict" a definition of its own; the glossary of the-way defines "level"
    as the game uses it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a glossary of every relevant word grows without bound, kept by memory, while a word used
as the field uses it needs no entry. A definition stands once because copies drift,
between products too; a closed list's values mean the rule their guard applies, so they stay beside
it.
*Rejected:* every term relevant to the system — no bound; a word defined where it is used, when used
in one place — nearly nothing is; a script counting places — it cannot tell a definition from
another sentence; a meaning new to the product as the test — the reader's meaning already catches a
coined word.

### WAY-96/1 — How is a glossary definition written?

A glossary definition is one sentence in the present tense with no normative word, shaped for a noun
as "<term> is <genus> that <difference>" and for a verb or an adjective as "<subject> is <term> when
<condition>", and its genus is no term of the glossary in another meaning. It says what the word
means and holds no rule about what the word names, and where two terms name neighbouring things, the
definition of one uses the other.

- **Change:** new decision
- **Scope:** glossary
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: glossary-definition-count · glossary-definition-words.
  Level 2 for the shape, the rule and neighbouring terms — a definition carries a rule when it holds
  something the decision or invariant setting it could change while the word went on naming the same
  thing; an agent compares the change with the decision:
  - complies: "The panel is the group of agents that assesses a change", the rest left to WAY-10;
    the definition of result names its neighbour: "the verdict that counts for it there, or …";
  - violates: "The panel is the three agents that assess a change…", with the number WAY-10 sets;
    "The binding part is the part of an entry that…", its genus a term of the part map; the
    definitions of verdict and result each standing alone.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* a genus that is a term in another meaning brings the homonym back; a rule inside a
definition changes it whenever the rule moves and sends the review of uses after what is a
decision's change; neighbouring terms stay apart only where one definition says how they differ.
*Rejected:* a phrase replacing the term, with no article or full stop — the count would count
something other than sentences; a rule told by a number, a date or a list — a place or a party
passes it; a rule told by putting the definition into the sentence setting the rule — that sentence
repeats what the thing does; a field naming neighbouring terms — the definitions carry it.

### WAY-97/1 — How does a sentence rely on a glossary term, and what does a change to a definition go through?

A sentence of a foundation entry that speaks of what a glossary term defines uses the term, never a
paraphrase of its definition, and a term whose definition holds a word an invariant's sentence may
not hold enters such a sentence only where the human deciding the change accepts it. A glossary
entry carries no version and is edited in place, and every change to a definition goes, in the same
change, through a review in which an agent puts the new definition in place of the word in every use
the guard lists and every other form it finds, and reports each use whose meaning moves to the human
deciding the change. A term used by an entry on the main branch keeps its meaning, and a new meaning
takes a new word.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** narrows WAY-02@3ffcbd46 · narrows WAY-60@6e862c88
- **Verification:** level 1 — invariants: glossary-entry-version · glossary-definition-uses. Level 2
  for the review, a new meaning and a paraphrase — an agent compares the change with the decision:
  - complies: the definition of "verdict" is reworded, the guard lists its uses, and the agent
    reports that none moves; after the main branch, a second sense of "gate" takes a new word; "The
    clock exits non-zero when some fact's result is `fail` or `error`";
  - violates: a definition is reworded as a mere fix and no uses are looked at; after the main branch
    "verdict" widens under an invariant's unchanged sentence and version; "The command that, unlike the
    gate, runs checks apart from any change exits non-zero when …", spelling out "clock".
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a sentence relies on a term by its word, which the review searches for, so a paraphrase
hides a dependant, and a term can hide from an invariant's guard a word its sentence may not hold.
On the main branch, a moved definition would silently change what tests check.
*Rejected:* a version as for invariants and facts — nothing reads it; a review only of a declared
new meaning — the line is a judgment every time; impact analysis by a model alone — nobody knows
what it missed (WAY-02); a record of the review checked by the guard — it sees only that a record
exists; after the main branch, the old entry withdrawn for a new one — old entries read in the new
meaning; a fingerprinted link from such an invariant to the entry — the word already reaches it.

### WAY-98/1 — Where is a word of a glossary entry's *Avoid* an error?

A word stands in a glossary entry's *Avoid* only where every use of it in the files of `foundations/`,
the elements' templates and the part the elements share carries the term's meaning, and it is an error where a change makes it
stand more times in such a file than on the commit the task branch left the main branch from. What a use
of a term leaves out (WAY-97), text in quotation marks, an identifier of the part map, the invariants
or the environment facts standing in a field's value, the glossary's entries and text a new decision
version restates word for word are not counted.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: glossary-avoid-growth · glossary-avoid-single ·
  glossary-avoid-term · glossary-avoid-carrier · glossary-not-quoted-word. Level 2 for what may stand
  in *Avoid* — an agent compares the change with the decision:
  - complies: "checker", whose every use names the format guard, stands in that term's *Avoid*; a
    paragraph holding it is rewrapped and the guard stays quiet;
  - violates: "run" stands in an *Avoid* though the foundation also runs commands; "main branch", kept
    out of an invariant's sentence only, is put into an *Avoid*.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a synonym comes back in whatever the next author writes, so every file is counted; a
word with another correct meaning cannot be banned without that meaning. Counts per file survive
rewrapping. Quotes, names and restated sentences are not uses, and the count skips what the list of
uses skips.
*Rejected:* the binding parts alone — a synonym in a rationale teaches the next author; added lines —
every rewrap errs; a word banned from one kind of sentence moved into *Avoid* — "main branch" is
right outside an invariant's sentence; a word in two *Avoid* lists, or one that is also a term — the
guard would give two answers; a ratcheted list of old occurrences — the counts per file stand in for
it.

### WAY-99/1 — How does one word keep one meaning in the foundation?

Where a word carries two meanings in the files of `foundations/`, the elements' templates and the
part the elements share and one of them is a meaning a reader who knows the product's field would not give it, one of the two is
renamed wherever those files may still be edited, and the glossary entry of the word names in *Not*
each such meaning it no longer carries, with the term, identifier, closed-list value or quoted word —
holding neither the term nor its forms — that carries it now. A meaning whose word a human has not yet chosen reads `TODO` in *Not*, which a task
branch may hold and the main branch never does.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: glossary-not-target · glossary-not-quoted-word ·
  glossary-entry-merge-todo. Level 2 for how a second meaning goes — an agent compares the change with
  the decision:
  - complies: a game's "shard" carries a currency and a level's piece, the piece becomes "fragment",
    and *Not* of "shard" names it;
  - violates: "shard (currency)" and "shard (piece)" stand side by side in the foundation; *Not* of
    "shard" names "level shard", a phrase holding the word itself.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a sentence a test cites carries its words as they stand, so a word read in two meanings
makes it true and false at once. A carrier holding the word itself would keep the homonym under a
new label. The word is the human's choice (WAY-10).
*Rejected:* two meanings told apart by an area — the sentence carries no area; a note beside the
word — nobody citing the sentence reads it; renaming two meanings a reader of the field tells apart —
neither is the product's own; a *Not* that always names a word — the author would choose before the
human sees the case.

### WAY-100/1 — When does a method or practice borrowed from elsewhere bind a product?

A method or practice borrowed from outside a product binds its way of working only through a
decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness
to a method or practice no decision has adopted, it asks a human before treating it as a rule.

- **Change:** new decision
- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts,
  elements-common, task-cycle, gate, repository
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a decision adopts only the risk assessment step of an outside process for task
    planning and gives its reason; an agent offers an unadopted technique as a proposal;
  - violates: a skill makes an outside planning ritual mandatory because an agent recognizes it,
    without a decision adopting it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* borrowing pieces without a conscious choice makes the product's boundaries hard to
explain and change. Naming the chosen piece, its scope and its reason lets later work distinguish
it from a resemblance or a habit.
*Rejected:* importing a whole outside method by default — its unrelated steps become obligations;
treating recognition by an agent as adoption — recognition does not settle fit or scope.

### WAY-101/1 — Who chooses the backlog tool used with the-way?

The-way's task cycle requires no particular backlog application or service; each product chooses
where it keeps its roadmap, projects and tasks.

- **Change:** new decision
- **Scope:** decisions, elements-common, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task-cycle step accepts task information supplied from a product's chosen files or
    tracker;
  - violates: the step can obtain tasks only from one named backlog service.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* the backlog hierarchy belongs to the process, while its storage belongs to the
product. Requiring one service would force a product to move its tasks before it could use the
process.
*Rejected:* one fixed backlog service for all products — adopting the process would also require
adopting that service.

### WAY-102/1 — What is the-way for?

The-way is a process for work on a technology product in which a change of premises or direction is
an ordinary step: it passes through the product's foundation and needs no memory of what is linked
to what.

- **Change:** new decision
- **Scope:** decisions, part-map, relation-model, invariants, glossary, environment-facts,
  elements-common, task-cycle, gate, repository
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a change of product direction goes through the foundation, and references to affected
    entries are checked before the change is merged;
  - violates: a change of direction relies on the author remembering which decisions and documents
    to update.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* a process that relies on a person to remember every affected artifact fails when work
spans tasks and sessions. Making foundation changes routine gives each change a place to start and
a route to its dependents.
*Rejected:* disconnected steps joined by hand — the person carrying the work must reconstruct
their links; treating a change of premises as an exceptional repair — the foundation falls behind
the product's direction.

### WAY-103/1 — Who is the-way for?

The-way is built first for its author and aims at anyone who builds a technology product and adopts
the process for their own needs; the process is written for the agents that carry out the task cycle
too.

- **Change:** new decision
- **Scope:** decisions, elements-common, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: an element's skill gives an agent steps it can perform, and a new task-cycle step is
    understandable to a builder using their own product;
  - violates: a task-cycle step relies on private shorthand only the author understands, or leaves
    the agent's action unstated.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* starting with the author gives the process a real first user; aiming at independent
builders keeps one person's setup from defining the audience. Agents need instructions they can
execute because they perform the task cycle.
*Rejected:* an author-only procedure — another builder would have to reconstruct its unwritten
conventions; prose addressed only to humans — an agent could not take its assigned steps from it.

### WAY-104/1 — How does a product write a word of its domain that the glossary of the-way holds?

A word of a product's domain that the glossary of the-way holds at the commit the product pins, in
any of its forms, is written in the files of the product's `foundations/` with a qualifier — a
phrase holding the word — and the bare word keeps there the meaning of the process; the qualified
word takes a glossary entry only where WAY-95 gives a word one, and the entry of the bare word in
the glossary of the-way records no *Not* for it. The *Avoid* of an entry of the product's glossary
holds a word the glossary of the-way holds, or the last word of a term it holds, in any of its
forms, only with a qualifier. The product's code, its interface and talk about the product use the
word of the domain unchanged.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-95@1cc58b42 · derives from WAY-98@94371030 ·
  narrows WAY-99@7d44dfd7
- **Verification:** level 1 — invariants: glossary-process-terms. Level 2 for how the sentences of
  a product's foundation, its code and its interface write the word — an agent compares the change
  with the decision:
  - complies: a game's invariants say "game clock" for the timer of a match, and its glossary,
    holding no entry for it, defines no "clock", while its code names a class `Clock` and its
    screen shows "Clock"; a game's glossary entry "game clock" lists "match clock" in *Avoid*;
  - violates: a game's glossary defines "clock" as the timer of a match; a game's invariant says
    "clock" for the timer of a match; a game's glossary entry "match timer" lists "clock" in
    *Avoid*, or its entry "lab result" lists "fact", the last word of "environment fact".
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-02

*Rationale:* a word of the process written bare in a product's foundation for something of its
domain carries two meanings for an agent that reads the-way's rules beside the product's, and a
qualifier keeps each word in one meaning where the rules are read; the people who build and use the
product keep the words of its domain, since the rule protects the reading of the foundation alone.
A product cannot edit the glossary of the-way, so the *Not* that WAY-99 asks of the word's entry has
nowhere to stand, and a phrase holding the word, which WAY-99 refuses as a carrier, here keeps the
word of the field recognizable. A word of *Avoid* counts as an error at every use WAY-98 counts,
whatever meaning the use carries, so the bare word in a product's *Avoid* would bar the meaning of
the process that the bare word keeps; the last word of a term of the-way, such as "fact" for
"environment fact", stands for the whole term (WAY-94), so in a product's *Avoid* it would bar that
term's short form in the same way.
*Rejected:* the bare word of the process in a product's glossary, its meaning of the domain marked
beside it and reported as a warning rather than an error — one word carries two meanings in the
repository, and whoever reads the foundation tells at every use which one it carries; the words of
the process written in a fixed form in the-way, such as in backticks, leaving the plain word free
for the domain — a plain word in a product's sentence may still carry either meaning, so the form
keeps nothing apart, and every entry of the-way is rewritten to it; a word holding neither the word
of the process nor its forms, as WAY-99 asks of a carrier — for words the field uses daily, such as
"part", "entry" or "result", the foundation drifts from the words the product's people and code use;
the bare word in a product's *Avoid*, its uses in the meaning of the process left out of the count —
no count tells one meaning of a word from another.

### WAY-105/1 — Which check reports an invariant whose command runs a script that does not exist, and how is that script read?

The gate, when it runs an invariant's method whose program is a Python interpreter — `python`,
`python3`, `python3.<minor>` or `py`, with or without `.exe` — reports the entry `unchecked` for
want of a declared or produced command where the script the command runs does not exist on the
commit being checked, or `error` where that script exists on the commit the branch left the main
branch from; no format guard judges whether a command's script exists. The gate reads such a
command as a POSIX shell splits it into words, quotes, backslashes and operators included, and its
script is the first word after the interpreter's own options and the values they take, never a
value the gate fills in. A method whose program is declared or produced by the product but is no
Python interpreter, and whose script does not exist yet, reads `TODO`.

- **Change:** new decision
- **Scope:** gate, invariants
- **Based on:** none
- **Relations:** derives from WAY-63@f16348c8 · derives from WAY-61@4804d070 ·
  derives from WAY-38@6e10c3fd
- **Verification:** level 1 — invariants: gate-missing-script. Level 2 for what the format guard
  leaves alone, which word of a command is its script, and the method of another program — an
  agent compares the change with the decision:
  - complies: an entry whose method is `python -B tools/check_saves.py --record .runs/saves.jsonl`,
    written before `tools/check_saves.py` exists, passes the format guard with no warning; the gate
    takes `my tools/check.py` as the script of `python -B "my tools/check.py" --base {fork-point}`,
    and `tools/check.py` as that of `py -3 -W error tools/check.py`; in a product that declares
    `node`, an entry whose check will be `node tools/check_saves.js`, not written yet, reads `TODO`;
  - violates: the format guard warns on that entry; the gate takes `error` as the script of
    `python -W error tools/check.py`, `"my` as that of the quoted path, or `{fork-point}` as a
    script; in a product that declares `node`, an entry names `node tools/check_saves.js` before
    that script exists.
- **Review when:** none
- **Origin:** the panel's record of the change that counts the checks a `none` option leaves
  unchecked in every guard's summary, in the message of commit d389623 of the-way
- **Approved by:** Mariusz, 2026-10-02

*Rationale:* an invariant may be written before the code that checks it, so when the entry is
written a wrong path and a script not yet written look alike, and a warning there falls on the case
the template allows, each one reaching a human. The gate runs the method, so it meets a missing
script where the result is read, and the closed list of reasons already holds this one; a script
the branch removed is a check the change dropped, which the list already makes an error. The cost
is that a wrong path shows at the first run of the gate, not when the entry is written. A command
is read as a POSIX shell reads it: a path in quotes is one word, and a word an option takes, or a
word after the script, belongs to the option or the script. Which word is the script follows from
the interpreter's own options, known for Python alone, so the method of another program waits as
`TODO` until its script exists.
*Rejected:* a warning of the format guard when the entry is written — it falls on the case the
template allows, and every one reaches a human; nobody reporting it — a method with a wrong path
looks checked until its first run; a command split on spaces — a quoted path breaks in two, and a
word an option takes is read as the script.
