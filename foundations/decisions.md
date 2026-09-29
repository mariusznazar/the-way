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
implementation they are read-only. A mechanism outside the model enforces this: a local hook,
and in the merge request a CI check that rejects any change to an invariant test without an
accepted foundation change. A task that needs an invariant test changed goes back to the
foundation step.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** agents that a test stands in the way of cheat past it, and the Claude models
  measured do so mostly by changing the test, against which read-only tests are particularly
  effective: impossiblebench-test-modification@9cdba560.
- **Relations:** derives from WAY-01@60960941 · related to WAY-02
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-test-change-acceptance.
- **Review when:** the design of the task cycle begins, or no model in the range of fact
  impossiblebench-test-modification is Active in Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-14

*Rationale:* an agent that a test stands in the way of adjusts the test to the code: the build
turns green, and the foundation lies. Keeping invariant tests out of the implementer's reach
removes that move instead of forbidding it.
*Rejected:* a written rule "do not change the tests" — a rule written in prose stops nothing.
*Consequences:* the CI check has to tell invariant tests from other tests; it recognises them
by the invariant they cite (WAY-02). Even a change of mechanics — a selector, test data, waiting —
goes through the foundation step and its acceptance.

### WAY-04/1 — What elements make up a product's foundation?

A product's foundation has five elements, and the list is closed: invariants, decisions, a
glossary of product terms, a part map, and environment facts. A new pattern enters the
foundation only as a field or a rule of one of the five, and only when a mechanism keeps it
without human memory: a test, a lint, a check that stops a merge, a mandatory relation or
configuration.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** documentation that nobody maintains turns into "a culture of 'paper safety' at
  the expense of real safety" (Haddon-Cave, The Nimrod Review, 2009; summary:
  https://aerossurance.com/safety-management/nimrod-xv230-haddon-cave/).
- **Relations:** related to WAY-02
- **Outranks:** none
- **Verification:** level 1 — invariants: foundation-file-kinds. Level 2 for the rule on new
  patterns — an agent compares the change with the decision:
  - complies: the failure modes a part can suffer enter the foundation as fields of that part
    in the part map, and its criticality is computed from them;
  - violates: a hand-written architecture document appears next to the part map.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-14

*Rationale:* each element holds what no other can. A task must not break an invariant.
Decisions are the only place for reasons and rejected options, and they constrain later changes
only when they are read as rules rather than as history. The glossary exists because terms
carry rules: without it, the same word means one thing in the concept, another in the
requirements and a third in the code. The part map lists the parts that criticality and scope
refer to; it holds rules — allowed dependencies — because code yields only the current state,
and its rule for assigning files lets a script check the map against the code and compute what
a task touches. Environment facts exist because an invariant with a green test can rest on a
fact about the world that nobody wrote down, as the assumption hidden in the code of Ariane 5
did. The list was checked for completeness against arc42, ISO/IEC/IEEE 42010 and the
documentation of several existing products. It is closed, and a new pattern needs a mechanism,
because research produced at least nine candidates for new kinds of entries and fields, and a
large foundation that nobody maintains gives only paper safety.
*Rejected:* as separate elements — tests (a method of checking an invariant), documentation of
"why" (the rationale of decisions), product identity (the foundation as a whole defines it;
"what for" and "for whom" are decisions), classes of task risk (a task inherits risk from the
parts it touches), structural code rules and quality scenarios (forms of an invariant), the
environment an agent runs, and the return step (both belong to the task cycle); a separate
element recording criticality (criticality is a field of a part);
external constraints as a field of the map (a constraint is an environment fact, and the
obligation it creates is an invariant); product principles and non-goals as a separate kind of
entry (they are decisions like any other); diagrams and an ARCHITECTURE.md written by hand (a
second copy of the map); environment facts as hypotheses in the backlog (they are true or false
today); assumptions as a kind of entry — anything inconvenient could be called an assumption and
escape checking, and a mandatory condition for disproving it with a review date narrows that way
round without closing it.
*Consequences:* each element is described in `elements/<element>/` of the process repository; the
description grows into the element's template as the element goes through its steps. Every picture
of the architecture — a diagram, a description — is generated from the part map and the code, and is
made for a human on request; no such picture is generated into an agent's context (WAY-52). Which
glossary holds a word, the-way's or a product's, is set by WAY-95.

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
- **Based on:** long lists of fields stop people from recording decisions: "Research tools
  provide interfaces to capture a long list of items which discourage designers to spend time
  to store all the items" (Capilla et al., 2016,
  https://pure.rug.nl/ws/files/65923130/1_s2.0_S0164121215002034_main.pdf). A section that only
  a template demands goes empty: "The most problematic section was Considered Options, which is
  mandatory in the MADR template … This section was absent or misplaced in most ADRs"
  (Miccio, Tommasel, Diaz-Pace, 2026, https://arxiv.org/html/2609.07375).
- **Relations:** related to WAY-01 · related to WAY-02 · related to WAY-04
- **Outranks:** none
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
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* norms keep what binds short and checkable and put the explanation next to it; a
record written like a legal code, in a commanding voice, reads badly and is followed worse.
Agents generalise from the reasons they are given, so the reasoning stays in the entry, below
the binding sentences. The present tense is used because a sentence with "will" or "should"
describes an intent, not a state. Fields are few because a field survives in practice only when
someone reads it in a specific activity. The template is the process's code:
under WAY-01 it follows the decisions, never the other way round.
*Rejected:* prose entries without fields — nothing a script or an agent can read reliably;
full templates with many fields and relations — too many fields without a reader, and the tools
built on them did not survive; a status field written by hand — a second copy of what the
sequence of versions already says; a single one-sentence statement as the whole entry — the
binding rule cannot be separated from its reasoning; normative capitals such as MUST — shouting
reads worse, not stronger; examples written for the template — an example with gaps teaches
gaps.
*Consequences:* adding or removing a field is a change of the template and therefore needs a
decision. The format guard,
`elements/decisions/format_guard.py`, checks the rules on its list in the template; the other
rules of the entry hold through review. Whether every field appears in every entry, and which
words it may hold, is set by WAY-71.

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
of n runs for a test that does not give the same verdict every time. Human inspection is used for
assessments that neither an automated check nor a repeatable measurement can settle, and it
leaves a trace of who checked and when.

- **Change:** new decision
- **Scope:** invariants
- **Based on:** a test can cover code without checking it: a pseudo-tested method is "covered by
  the test suite, yet no test case fails when the method body is removed" (Vera-Pérez, Danglot,
  Monperrus, Baudry, 2019, https://arxiv.org/abs/1807.05030). Automated tools leave cases that
  only a person can settle: "axe-core will return elements as "incomplete" where axe-core could
  not be certain, and manual review is needed" (https://github.com/dequelabs/axe-core).
- **Relations:** related to WAY-03 · related to WAY-04
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-method-form · invariant-test-break ·
  human-verdict-trace. Level 2 for the choice of method — an agent compares the change with the
  decision:
  - complies: a person settles whether an image's text alternative describes it, after the
    accessibility check marked it incomplete;
  - violates: an invariant that a repeatable measurement can settle is left to human inspection.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* coverage does not mean that a test checks anything: code can be covered while no
test fails when it is removed, so a test counts only when a break it is meant to catch makes it
fail. A result written by hand is a second copy of what running the method says, and it goes
stale with the next commit. Some assessments stay with a person, because even the tools built
for them hand the uncertain cases over for manual review.
*Rejected:* "every invariant has test coverage" — it either pushes invariants that cannot be
tested out of the foundation, or gives them a test that always passes.
*Consequences:* a check that cites an invariant is accepted only after a deliberate break has made
it fail, so the gate needs a way to introduce such breaks. An invariant that no test or
measurement can settle stays in the foundation, checked by a person.

### WAY-09/1 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a
directory for each part of the process other than `repository` — `elements/<element>/` for each
foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/` and
`task-cycle/` — the files that serve the whole repository, which its part map gives to the
`repository` part (WAY-44), and a `README.md` that describes the repository. A directory reaches
the main branch only once it holds what its part requires: an element its template and rules,
examples or a pointer to entries of the-way that serve as its examples, a skill that writes its
entries and a format guard; `elements/common/` the rules of form and the way of working the
elements' templates and skills share, the code their format guards share and the procedure of the
panel; `relation-model/` the script that computes fingerprints; `gate/` the test of every critical
flow in the part map; `task-cycle/` what the design of the task cycle sets, and until then it does
not reach the main branch. The entries in `foundations/` are checked by the format guards of their
elements.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, repository, task-cycle
- **Based on:** none
- **Relations:** related to WAY-02 · related to WAY-04 · related to WAY-21 ·
  related to WAY-44 · related to WAY-55
- **Outranks:** none
- **Verification:** level 1 — invariants: repository-file-location · element-directory-contents ·
  relation-model-directory-contents · invariant-example-target · map-example-target ·
  glossary-example-target.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* the repository shows what the process looks like when it works, and an artefact
brought in on the side turns it into a store of material from the first day. Directories follow
the parts of the process, so that the files a change touches name the part it belongs to and the
decisions to check it against (WAY-21). What a directory must hold depends on its part, because
each tool has a reason only where it has work: a skill writes entries, so it belongs to an
element; the fingerprint script only reads, so `relation-model` has no skill. The skill writes
an entry in the right form when someone runs it; the format guard catches a form broken by hand, by
another agent or by a merge. Until a directory holds what its part requires, it is a change in
progress, and under WAY-01 such a change lives on a branch. The files that serve the whole
repository belong to no one part of the process, and WAY-44 gives them a part of their own; they
stay where the tool that reads them looks for them, and the map, not this list, names which they
are. The `README.md` binds nothing.
*Rejected:* material merged to the main branch as soon as it is written; an element whose only
tool is a skill — the form then holds only while someone remembers to run it; one `tools/`
directory for everything shared — it matches no part of the process and grows into a store; the
same set of template, skill and script required of every directory — a script that only reads has
no entries for a skill to write; the files that serve the whole repository on the map's list of
files left out on purpose, beside the `README.md` — they would lose their part and the failure
mode recorded at it, although a wrong line in `.gitattributes` turns whole files over.
*Consequences:* element descriptions in `elements/` reach the main branch as templates with their
skills and scripts, not as descriptions. The script that computes fingerprints lives in
`relation-model/`, and a reference whose fingerprint is no longer current is flagged by the format
guard that checks the entry carrying it (WAY-31, WAY-90). The gate is a part of the process of its own, with a
directory of its own (WAY-55), and what `task-cycle/` must hold is set when the task cycle is
designed. The map's rule for assigning files follows these directories, and a file that serves the
whole repository added later — the CI configuration, once the gate runs in CI — enters by a change
to the `repository` part of the map, not by a new version of this decision.

### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation is assessed by the panel, which has three
agents: two assess it independently, each from a different, named perspective and seeing only the
diff and the foundation, never the author's reasoning, and one of the two perspectives names what
of the change can be cut, while the third, on a different model where one is available, settles
between them. The panel decides changes of an invariant test's mechanics — selectors, test data,
waiting — and a rerun set outside the method's command is never such a change. Every other change
the panel prepares with the diff, its effects and a recommendation, and a human decides.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  task-cycle
- **Based on:** a model assessing text favours its own: llm-self-preference@6d9f4b97.
- **Relations:** derives from WAY-03@4fa941a4 · related to WAY-07
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-test-change-acceptance ·
  foundation-change-panel-record. Level 2 for what the panel decides — an agent compares the change
  with the decision:
  - complies: the panel accepts a new selector in an invariant test, and the change is merged
    without a human;
  - violates: the panel accepts a changed expected value in an invariant test; an assessing agent
    receives the author's reasoning.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* the problem is a single executor that checks itself. Agents on the same model with
the same input share its blind spots, so independence comes from a different perspective, from
not seeing the author's reasoning, and from a different model for the agent that settles. Only a
human knows what the product is meant to protect, so every change to what the foundation says goes to a human. The finding it cites measured models of other publishers only, and this decision takes it across publishers (WAY-85).
*Rejected:* a panel that settles everything; a single agent without a panel.
*Consequences:* the CI check from WAY-03 accepts a change to an invariant test only with the
panel's record, and, beyond a change of mechanics, only with a human decision. Changes waiting for a
human grow with the number of tasks, and nothing yet limits how many may wait.

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
- **Approved by:** Mariusz, 2026-09-29

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
- **Approved by:** Mariusz, 2026-09-29

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

### WAY-15/1 — What in a foundation is written by hand, and what is derived?

What can be derived from what the product executes — code, configuration, infrastructure as
code, runtime traces — is derived, never written by hand, and what is derived describes the
state. Rules are written by hand: what is allowed, how bad a failure would be and what the
product promises, which the code cannot show.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** code shows what exists, not the rules: "Your architecture models and your source
  code will not show the same things. The difference between them is the model-code gap", and
  "intensional elements establish general rules that apply to all elements, but standard
  programming languages cannot directly express these rules" (George Fairbanks,
  https://www.georgefairbanks.com/software-architecture/model-code-gap/). A view recovered from
  the code shows accidents as decisions: "Principal architecture decisions may not have been
  implemented and are therefore out of reach of architecture recovery. Conversely, the system
  may reflect inadvertent decisions […]" (Link et al., ISEC 2019,
  https://arxiv.org/abs/1901.07700).
- **Relations:** related to WAY-04 · related to WAY-08 · related to WAY-11
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: every derived file in the repository
  is identical to what its generator produces on the same commit, except the list of known
  violations of the part map's rules, which is checked as a subset of the list on the main
  branch (WAY-51). Level 2 for what is derived and what is written by hand — an agent compares
  the change with the decision:
  - complies: the view of the decisions in force is generated from the log; the existing
    dependencies between parts are read from the dependency graph the product's own tooling
    produces and compared with the allowed dependencies written in the part map;
  - violates: a hand-written list of the product's endpoints kept next to the code; the allowed
    dependencies in the part map copied from the current import graph.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* a description written by hand of what the product simply has — a list of screens,
endpoints or configuration options — is a second copy that nobody reconciles with the code, and
it goes stale with the next change; a generator is written once and stays true on every commit.
The line runs between state and rules: code shows what exists, not what is allowed, so a view
derived from it presents an accidental state as the architecture, and a rule copied from the
current state turns an accident into law. Rules therefore stay with a human, and deriving the
state is what lets it be compared with them.
*Rejected:* "do not write by hand what can be derived from code" as the whole rule — it reads
as a demand to derive the part map, whose rules code cannot show; derivation from code alone —
the code shows structure, while behaviour shows in runtime traces and deployment in
infrastructure files.
*Consequences:* every derived view has a generator, and a derived file is regenerated, never
edited by hand. Comparing the derived state with the rules uses the part map's rule for
assigning files (WAY-44). One derived file is not regenerated from scratch — the list of known
violations, which WAY-51 keeps as a debt with a ratchet.

### WAY-16/1 — How are the checks of invariants run?

The gate takes its checks from the methods of checking written in the entries, never from a list
written by hand, and one command runs the checks a change calls for together with the product's own
tests it calls for — the same command for an agent, for a human and for whatever runs it when a
change is merged.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: ci-checking-commands · gate-check-source. Level 2 for the
  same command for everyone — an agent compares the change with the decision:
  - complies: the instructions for agents name the gate's command as the way to check a change;
  - violates: the instructions for agents list test and lint commands of their own; the product's
    tests run under a command of their own beside the gate's.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

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
- **Based on:** a relation word left without a definition drifts in use: the IETF "Updates" tag
  "is currently used for multiple different purposes, which leads to confusion …" (Kuehlewind,
  Krishnan, https://www.ietf.org/archive/id/draft-kuehlewind-update-tag-04.html). Processes that
  last give a correction of wording a path of its own: "Errata are meant to fix "bugs" in the
  specification and should not be used to change what the community meant when it approved the
  RFC" (IESG,
  https://datatracker.ietf.org/doc/statement-iesg-iesg-processing-of-rfc-errata-for-the-ietf-stream-20080730).
- **Relations:** related to WAY-02 · related to WAY-05 · related to WAY-18 · related to WAY-19
- **Outranks:** none
- **Verification:** level 1 — invariants: binding-sentence-count · decision-change-kind ·
  decision-binding-across-versions · repeal-binding-sentences. Level 2 for the choice of kind — an
  agent compares the change with the decision:
  - complies: a version that answers the question anew is called a new wording; a typo fixed in
    a binding sentence is called an editorial correction, and a human confirms that the meaning is
    unchanged;
  - violates: a version called an editorial correction turns "must" into "may".
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a version has to say what it does to the decision, because everything that relies
on the decision needs that first: a fixed typo leaves every reliance valid, and a new answer does
not. A word for a change
left without a definition ends up meaning something different to each author, so the list is
closed and each kind is defined in the template. The list was closed before the first entry, so
every version in the log uses its kind in one sense.
*Rejected:* two kinds only, change and replacement — a fixed typo would look like a new answer;
an open list extended as needed — each new kind would carry its author's meaning.
*Consequences:* the table "Kinds of change" in the decision template is the written form of this
decision, except for its column on references and the sentence below the table, which belong to
WAY-31. A challenge
ends with the next version: a rationale change when the doubt is settled in the decision's
favour, or the change that settles it otherwise. A version that changes only *Consequences* is a
rationale change, since the consequences belong to the reasoning and leave the fingerprint
unchanged.

### WAY-21/1 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never
file paths, so that the decisions governing a change are found from the files it touches through
the part map's rule for assigning files.

- **Change:** new decision
- **Scope:** decisions, part-map, task-cycle
- **Based on:** an agent loses rules as their number grows: instruction-density-accuracy@f62b9a6d;
  and a tool vendor advises keeping an agent's instructions short for the same reason: "target under
  200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence" (Claude Code
  documentation, https://code.claude.com/docs/en/memory).
- **Relations:** related to WAY-04 · related to WAY-11 · related to WAY-13 · related to WAY-14
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-scope-names · decisions-found-for-change.
- **Review when:** no model in the range of fact instruction-density-accuracy is Active in
  Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* an agent checks a change only against the decisions it reads, and among many rules
it loses some, so the decisions that govern what a change touches have to be found for it. Parts
rather than paths, because the part map already assigns files to parts: paths written into each
decision would be a second copy that drifts as soon as files move. Parts rather than topics,
because a part can be computed from a change and a topic cannot.
*Rejected:* file paths in each decision, as rule files for agents do — a second copy of the part
map; topics as scope — they cannot be computed from a change; no scope — every change checked
against every decision, and the ones that matter lost among the rest.
*Consequences:* finding the decisions for a change uses the part map's rule for assigning
files (WAY-44). Which other decisions a change is checked against — those that govern every task,
and collisions between decisions of different scopes — is set when the task cycle is designed.

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
  task-cycle
- **Based on:** none
- **Relations:** related to WAY-09 · related to WAY-17
- **Outranks:** none
- **Verification:** level 1 — invariants: outbound-link-reach. Level 2 for the reasoning in the
  entry — an agent compares the change with the decision:
  - complies: a decision quotes a public study with its address; a pattern observed in a product
    outside the repository is described in the rationale — what was seen and where it went
    wrong — without a pointer to it;
  - violates: *Origin* points to a private note; a rationale rests on "as in our other product"
    without saying what was seen.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a pointer to a source the reader cannot open is a dead end, and it leaves the reader
to trust a claim that cannot be checked. The reasoning therefore travels with the entry, and an
observation made where readers cannot look is written down as what was seen, so that it can at least be
judged, and WAY-17 still has a fact to name.
*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader of the
repository can open them.
*Consequences:* *Origin* in this log is `none` or points to a document its readers can open. The
entries written before this one already follow it. Products built with this process are not
bound by this decision; their logs may point to their own documents.

### WAY-28/1 — How does the process enter a product that already exists?

When the process enters a product that already exists, the existing state is its starting point
and needs no justification, and the rules apply to changes from then on. The part map with
criticality comes first; the invariants of the critical flows and the parts they run through are
then recovered from what the product does — an agent lists what a part does, and a human chooses
which of it the product must keep — and the other invariants come through the return step of
tasks. Decisions are recovered only when a task touches the parts they govern.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, task-cycle
- **Based on:** checking an existing product against a description written long after its code
  is slow and can fail outright: MongoDB reports "10 weeks of effort without successfully
  trace-checking one spec" (MongoDB engineering blog,
  https://www.mongodb.com/company/blog/engineering/conformance-checking-at-mongodb-testing-our-code-matches-our-tla-specs).
- **Relations:** related to WAY-01 · related to WAY-04 · related to WAY-11 · related to WAY-13 ·
  related to WAY-15
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: on entering a product, the part map comes first, and the invariants of a critical
    payment flow are chosen by a human from the agent's list of what the flow does; a decision is
    recovered when a task first touches the parts it governs;
  - violates: an agent turns everything the critical flows and the parts they run through do
    today into invariants without a human's choice; an agent recovers from the code decisions for
    the whole product before any task touches them; the critical flows and the parts they run
    through wait for a task like any other.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* matching a whole product to a description written afterwards is slow, and it
tempts an agent to write reasons that look like decisions, so decisions wait until a task needs
them. The critical flows and the parts they run through cannot wait, because a break there is
expensive (WAY-13), so their invariants come first. A human chooses among what they do, because
only a human knows what the product is meant to protect, and what it does today is a state, not
yet a rule (WAY-15). Invariants and decisions are separate lists: an invariant needs no decision
above it, so a recovered invariant can bind before anyone knows why it holds.
*Rejected:* recovering the whole foundation at the start — slow, with reasons invented where none
are known; everything on demand, the critical flows and the parts they run through included — a
break there is found only when a task happens to touch them.
*Consequences:* an invariant recovered from behaviour needs a method of checking and the note WAY-58
sets, recording what was searched and what was found for or against keeping it, which the invariants
template carries as the field *Recovered*. A decision recovered for a task is written as the section
"Inherited decisions" of the decision template says, and decision records the product already has
are read as sources when their parts are touched. No glossary is written in bulk when the
process enters a product: a word takes an entry with the entries written when the process enters it
that stand on it, the return step brings the rest, and candidates an agent finds in the product's
documents or its rule files for agents become questions to a human at once, with no list of them
kept (WAY-95).

### WAY-29/1 — How is a decision recovered from an existing product written?

A decision recovered from an existing product records in *Origin* what was searched and what was
found, and its rationale and rejected options are quoted from that source, given by a human who
knows them, or written as `unknown`. A rationale an agent proposes goes to a human as a question,
never into the entry.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** rationales written by language models match those given by experts only partly:
  "The average Precision, Recall, and F1-score of the DR generated by the five LLMs with the CoT
  method are 0.237, 0.684, and 0.351, respectively" (Zhou et al.,
  https://arxiv.org/html/2504.20781v3). A reconstructed record is easily taken for a real one: "The
  retroactive ADR has the form of the decision record but not the substance" (Catio,
  https://www.catio.tech/blog/architecture-decision-record).
- **Relations:** related to WAY-10 · related to WAY-28
- **Outranks:** none
- **Verification:** level 1 — invariants: inherited-origin-form · inherited-rationale-source. Level
  2 for the agent's role — an agent compares the change with the decision:
  - complies: an agent finds the reason in a merged request and quotes it; an agent finds
    nothing, writes `unknown` and asks the human, who remembers the reason, and the entry gives
    it under that person's name;
  - violates: an agent writes a plausible reason inferred from the code into the entry.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a reason written by an agent looks exactly like one that was recorded, and later
readers take it for the reason the decision was made. Quoting only from a source keeps the two
apart; a human who knows the reason is such a source, an agent's guess is not. Recording what was
searched spares the next agent the same search. While the reason is unknown, a change to the
decision goes to a human anyway (WAY-10), and the entry says openly that nobody can tell what the
decision guards.
*Rejected:* a rationale proposed by an agent written into the entry — it would be read as the
reason the decision was made; rejected options filled in as `none considered` — nobody knows what
was considered.
*Consequences:* the section "Inherited decisions" of the decision template is the written form of
this decision; its rule that a change to such a decision goes to a human follows from WAY-10.
`unknown` here is a value, not a `TODO`: nobody is expected to supply it. A reason found later
enters by a new version on the main branch, by an edit before it.

### WAY-30/1 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan and approved with it by
the decision's approver. When a contradiction shows only during implementation, the agent stops,
quotes the decision by its number, and either brings the change into line, drops the change, or
proposes on the task branch a new wording or a narrowing of the decision — by a new version on the
main branch, by an edit before it — and the code that needs it waits for the decision's approver. An exception written in advance into a decision's binding sentences is
not a contradiction, and no exception lives only in a task's plan.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** tools that protect principles in agent work refuse a quiet way around them:
  "Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or
  tasks—not dilution, reinterpretation, or silent ignoring of the principle" (GitHub Spec Kit,
  https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md).
- **Relations:** derives from WAY-01@60960941 · related to WAY-03 ·
  related to WAY-07 · related to WAY-14 · related to WAY-21 · related to WAY-24 · related to WAY-25
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task branch whose code goes against a decision also carries a proposed narrowing
    of that decision, and the merge waits for its approver;
  - violates: a task branch whose code contradicts a decision that stays unchanged; a task's plan
    that records a "justified violation" of a decision.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* an exception kept only in a task's plan leaves the foundation describing something
the code no longer does (WAY-01). Stopping makes the contradiction visible at the moment it is
found. The agent may bring its change into line or drop it on its own, because both leave the
decision as it is; changing the decision is for its approver, and the code waits for that, as the
foundation comes before the code (WAY-01). A narrowing keeps the decision for everything outside
the exception, and a narrowing made for a situation that may pass carries *Review when*, so that
someone looks at it again (WAY-24). An exception foreseen in the binding sentences belongs to the
decision, so acting on it contradicts nothing.
*Rejected:* a justified violation recorded in the plan without a change to the decision, as Spec
Kit's plan template allows — the foundation stops matching the code; a whole new answer as the
only way to change the decision — a narrow exception would take the whole decision with it.
*Consequences:* the rule on exceptions foreseen in advance in the section "Binding sentences" of
the decision template belongs to the written form of this decision. The task cycle needs a step
in the plan for changes to decisions, and a task's plan has no home in the process yet (WAY-01).
When the contradiction is a collision between two decisions with no precedence recorded, the
agent stops and asks for the precedence (WAY-25). Checking an implementation against decisions
needs the decisions in the scope of the change (WAY-21).

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
- **Based on:** a relation word left without a definition drifts in use: the IETF "Updates" tag
  "is currently used for multiple different purposes, which leads to confusion …" (Kuehlewind,
  Krishnan, https://www.ietf.org/archive/id/draft-kuehlewind-update-tag-04.html).
- **Relations:** related to WAY-19 · related to WAY-20 · related to WAY-25 · related to WAY-31
- **Outranks:** none
- **Verification:** level 1 — invariants: relation-type. Level 2 for the choice of type — an agent
  compares the change with the decision:
  - complies: a decision that exists to serve WAY-01 names `derives from WAY-01`; a rule for one
    part that deliberately departs from a general decision names `narrows`;
  - violates: `narrows` for a decision that only mentions another; a new answer to an existing
    question written as a new number with a relation to the old one instead of a new version.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a relation type that each author reads differently tells a reader nothing, so each
type is defined once and the list is closed. Both types rely on the binding part of the other
decision and carry its fingerprint (WAY-31), and `narrows` also tells the agent checking a change
that the other decision does not apply in that area. A link that looks like a relation has a home
of its own: a new answer to the same question is a new version (WAY-19).
*Rejected:* none considered
*Consequences:* the rule on the closed list of relations in the section "Relations and
precedence" of the decision template is the written form of this decision. A new type enters by a
new version of this decision, once something reads a distinction the three types do not make
(WAY-05). Types of links between entries of other elements are set by those elements (WAY-17).

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
  task-cycle
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-09 · related to WAY-16 · related to WAY-21
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision; the invariants of
  this decision belong to each product's foundation, since no commit of the-way decides them:
  - complies: a product's foundation holds the invariants "this repository pins a commit of
    the-way" and "the product's CI runs only the gate and the scripts of its pinned commit"; a
    task in the product moves the pin, and its merge request carries what the newer version
    changes for the product;
  - violates: a product's CI fetches the latest the-way on every run; a skill in a product session
    comes from a copy of the-way other than the pinned commit.
- **Review when:** the first product has moved its pin to a newer the-way twice · check by:
  2026-11-17
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* a product checked with whatever the-way is newest gives a different result on the
same commit from one day to the next, and a change to the process can stop the CI of every product
at once, with no change in any of them. A pinned commit makes a change of the process a visible
change in the product, as a change of the foundation comes before the code (WAY-01): a new decision
of the-way binds a product only once someone in that product has taken it in. Tools defined once
are shared by pinning, not by copying, because copies drift apart (WAY-16).
*Rejected:* every product on the newest the-way — results that change without a change in the
product, and process decisions binding a product nobody in it has seen; templates and scripts
copied into each product — the copies drift.
*Consequences:* products lag behind the process, and moving a pin is work of its own, like
updating a dependency. A product session uses the skills of its pinned commit, so the global link
to a skill described in `elements/decisions/README.md` serves only work on the-way itself. How a
product pins the commit is set by the first product that does. Which decisions of the-way an agent
checks a task against is set when the task cycle is designed (WAY-21); they come from the pinned
commit. The-way itself uses the commit it is on. How a product's invariant that pins the commit
names this decision in *Derives from*, when this decision stands in the log of the-way rather than
in the product's own, is set by the first product that writes one.

### WAY-35/1 — What does an element's skill hold?

An element's skill holds only the way of working particular to its element: every rule of the
element's entries stands in the element's template, or once in the part the elements share
(WAY-09) where it is common to them, each citing the decision that sets it; the way of working the
skills share stands once in that part, and a skill reads the rules and that way of working from
there instead of restating them.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** related to WAY-05 · related to WAY-09 · related to WAY-16
- **Outranks:** none
- **Verification:** level 1 — invariants: skill-rule-source · template-language ·
  invariant-identifier-form · fact-identifier-form. Level 2 for what the skill holds — an agent
  compares the change with the decision:
  - complies: a fix to the skill's output that concerns the form of a field goes into the
    template, and the skill is left as it is; the skill orders its steps and says what to ask;
  - violates: the skill says a rationale has at most three sentences while the template does not;
    the skill restates the list of fields.
  Level 2 for a rule citing the decision that sets it — an agent compares the change with the
  decision:
  - complies: a new rule of an element's template or of the part the elements share ends with the
    number of the decision that sets it;
  - violates: a rule of entries added to the shared part cites no decision.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* a rule written both in the skill and in the template is two copies that drift apart,
and then the format guard, which reads the template, and the skill, which writes the entries, hold
entries to different rules. An entry written by hand or by another agent meets only the template
and the part the elements share, so they are the places every writer and every check reaches. The
way of working — the order of steps, what to ask, when to stop — is not a rule of the entry, so it
stays with the skills, and what they share stands once, in the part the elements share.
*Rejected:* rules restated in the skill next to the template — two copies that drift, and the
format guard and the skill hold entries to different rules.
*Consequences:* a fix to a skill's output that concerns a rule of the entry is a
fix to the template; for decisions it comes with a decision in the log (WAY-05). The
opening paragraph of `record-decision` follows this decision, and the skills of the other elements
follow it once they are written.

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
library alone, and installs nothing. It calls git, and the commands a product declares in its own repository — a
dependency graph, a detector of breaking changes, coverage — reading their output through an
adapter for the format. Where a product declares no such command, the script reports what it
could not check, never agreement.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  task-cycle
- **Based on:** computing a language's state is work that mature tools do as separate programs —
  buf, API Extractor, japicmp, cargo-semver-checks, oasdiff — and reimplementing it was given up
  as "requires re-implementing large swaths of rust's semantics"
  (https://github.com/obi1kenobi/cargo-semver-checks).
- **Relations:** related to WAY-02 · related to WAY-09 · related to WAY-16 · related to WAY-34 ·
  related to WAY-89
- **Outranks:** none
- **Verification:** level 1 — invariants: script-language · script-imports · script-subprocesses ·
  map-guard-missing-command.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a product runs the scripts of the commit of the-way it pins (WAY-34), so every
language and every package they need becomes something each product's CI has to provide. One
language with its standard library alone leaves one interpreter to provide and nothing to
install. Which version that is, and when it moves, is set by WAY-89. What the
scripts cannot do themselves is compute the state of a language they do not parse: a dependency
graph outside Python, a breaking change in a schema, the reach of a test. Those the product
already computes with its own tools, so the script runs the command the product declares and
reads its output, rather than parsing a language it would get wrong. Silence is reported as
unchecked rather than as agreement, because a check that quietly sees nothing passes.
*Rejected:* Node.js without packages — as able as Python; a second language adds a second
interpreter to every product's CI; shell scripts in Bash or PowerShell — neither runs the same
on Windows and on Linux; a compiled program in Go or Rust — every change needs a build and
published files; each script in the language its author picks — a product's CI needs every
interpreter any script chose; the product's CI writing that output into a committed file that
the scripts then read — an agent would get no signal before pushing, and the product would carry
a CI step existing only for this process; the scripts parsing other languages themselves — the
tools that tried gave it up.
*Consequences:* a product's CI provides the Python WAY-89 declares and git, and declares in its
repository the commands whose output the scripts read. What those commands cost in time, and how
much their output depends on the environment they run in, the product pays. The format guard of
decisions, the fingerprint script of `relation-model` (WAY-09), the view of decisions in force
(WAY-18) and the gate (WAY-16) are written in Python. Skills and templates are not
scripts, and this decision does not bind them. A check runs the same way for an agent locally, in
CI and for a human (WAY-16), because all three run the same declared command.

### WAY-40/1 — What kinds of entry does the part map hold?

The part map holds three kinds of entry: a part, a critical flow and a surface. An allowed
dependency is a field of the part it starts from, and the known violations of the map's rules
are a derived file beside the map, so neither is an entry of its own. The whole map lives in one
Markdown file of fixed shape in `foundations/`.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-04@f07bb569 · related to WAY-15
- **Outranks:** none
- **Verification:** level 1 — invariants: map-entry-kinds · map-section-kinds · part-map-file ·
  flow-part-names.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* each kind answers a question the others cannot: a part says what it is responsible
for and which files belong to it, a flow says what has to keep working
across parts end to end, and a surface says what someone outside the product relies on. An
allowed dependency has no identity of its own — the pair of parts names it — and an identifier
for a relation pays off only where something points at the relation itself rather than at its
ends, as a flow that names its steps does. The known violations are what the rules do not hold
today, computed from the map and the code, so they belong with what is derived rather than among
rules written by hand (WAY-15). One file, because the map is read whole at the start of a task
and its three kinds refer to one another constantly.
*Rejected:* an allowed dependency as an entry with its own identifier — it buys a short
reference to something nothing refers to on its own, and costs a second field to check in every
reference; criticality as a fourth kind of entry — it is a field of a part and of a flow
(WAY-04); the known violations kept inside the map file — a rule written by hand and a computed
state in one file, which WAY-15 keeps apart; one file per part — a rename of a part would become
a move of files, and the map is short enough to read whole.
*Consequences:* the element's template gives the shape of each kind and the fields it carries.
The binding part of each kind, and so what its fingerprint covers, needs its own decision. The file of
known violations is derived and yet cannot be regenerated from scratch, so it needs a rule of its
own under WAY-15.

### WAY-41/1 — What identifies an entry of the part map?

Every entry of the part map carries a permanent identifier made of words, such as
`relation-model`, and it stays the same when the files assigned to it change. Splitting or merging
entries gives each entry that comes out of it a new identifier, and the identifier left behind
stays in the map as a withdrawn identifier giving why and naming its successors; an identifier is
never reused.

- **Change:** new decision
- **Scope:** part-map, elements-common, relation-model
- **Based on:** none
- **Relations:** derives from WAY-40@c3f0b830
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
description, a surface's promise — and the entry's fingerprint covers that sentence
alone. Path patterns, allowed dependencies, failure modes and a flow's list of parts stay
outside it; a change to a part's path patterns is shown instead as the list of files that
changed part.

- **Change:** new decision
- **Scope:** part-map, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46 · related to WAY-40
- **Outranks:** none
- **Verification:** level 1 — invariants: map-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* a fingerprint exists to flag the references that may have gone stale (WAY-02), so
it covers what those references rest on. What refers to a part — a decision's scope, a test, a
rule generated for an agent — rests on what the part is responsible for, not on where its files
sit today. The other fields change often and mechanically: path patterns move with the files, a
failure mode is added the day somebody learns of one, a flow's list of parts is recomputed from
coverage; flags raised by them would be raised for nothing, and flags raised for nothing teach
whoever clears them to clear them without reading. A change of path patterns still matters, but
as something else: it changes which files belong where, so the script shows it as the list of
files that changed part — a thing that can be read and checked.
*Rejected:* the whole entry as its binding part — every moved file would flag every reference to
the part; the identifier alone — a rewritten responsibility would then pass unnoticed, which is
what WAY-02 exists to prevent; a fingerprint per field — every reference would have to say which
field it relies on.
*Consequences:* the element's template marks the binding sentence of each kind of entry. The map
computes its fingerprints with the script `relation-model` already has (WAY-02). A reference
that relies on a part's path patterns has no fingerprint to carry; what catches it is the list of
files that changed part.

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
- **Scope:** part-map, task-cycle
- **Based on:** git-path-patterns@1519f3f7
- **Relations:** derives from WAY-40@c3f0b830
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
- **Relations:** derives from WAY-40@c3f0b830
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
- **Relations:** derives from WAY-40@c3f0b830
- **Verification:** level 1 — invariants: failure-mode-severity · failure-mode-detection ·
  part-criticality-field · map-guard-unrecorded-criticality · map-guard-dependency-report ·
  criticality-lowering-report. Level 2 for an obligation from outside — an agent compares the
  change with the decision:
  - complies: a part with personal data records "kept past the legal period", detected by an
    invariant resting on the law's fact;
  - violates: a part carries a field "minimum criticality: high" citing the law; the obligation is
    noted in a part's responsibility with no failure mode.
- **Review when:** TODO — the check-by date for the state: a product that pins the-way holds data
  under an obligation from a law or a contract on one of its parts
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

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
- **Relations:** derives from WAY-40@c3f0b830
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

### WAY-49/1 — How does a product declare a surface?

A surface is declared at the item itself, in the code or in the schema, with the level of the
promise and, once the surface is being withdrawn, the date of the withdrawal. The map holds one
entry per surface — its identifier, the promise in words, and where the declaration sits — and holds
no list of withdrawals in progress. A surface that cannot be marked at the item is written in the
map by hand and checked by a test.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** what counts as a surface is declared, not discovered: "Software using Semantic
  Versioning MUST declare a public API" (https://semver.org/). Tools read the promise where it is
  written at the item — API Extractor reports an exported item with no release tag
  (https://api-extractor.com/pages/messages/ae-missing-release-tag/) — and turn a withdrawal date
  written there into a check, where removing the item before the date is a breaking change
  (oasdiff, https://github.com/oasdiff/oasdiff/blob/main/docs/DEPRECATION.md).
- **Relations:** derives from WAY-40@c3f0b830 · related to WAY-15 · related to WAY-34 ·
  related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: surface-promise-level · surface-declaration ·
  map-withdrawal-date.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a surface stands on a promise, and no tool reads a promise out of code: a tool computes
the shape of what somebody declared, and the declaring falls to a human. It sits at the item,
where whoever changes it sees it and where the tools that compute shape and breaking change look
for it. The map keeps the promise in words and the place of the declaration, because that is
what a scope, a criticality and a change path are read against, and a header comment cannot
carry them. The withdrawal date stays at the item as well, because it is checked against the
item's removal; kept in the map it would be a second copy, and the entry nobody deletes. A
surface that cannot be marked at the item — the format of a saved file, a command-line
interface — exists all the same, and a hand-written entry with a test is what keeps it from
disappearing quietly.
*Rejected:* the list of surfaces computed from the code — tools compute the shape of declared
items, never which of them the product promises to keep; the declaration kept only in the map
— whoever changes the item does not read the map, and no tool would find it there; a list of
withdrawals in progress in the map — a second place to update, stale the day the item goes.
*Consequences:* the product's own tool computes the shape of declared items, a breaking change
against the main branch, and a declaration missing its level (WAY-15). A product with a format of
its own, such as a saved game, sets the shape of the mark and a parser that fails on a record it
does not recognise. The surfaces this repository promises to the products pinned to a commit
(WAY-34) — the format of entries, the way a fingerprint is computed, the commands of the scripts
— are declared when its own map is written.

### WAY-50/1 — By what path may a surface change?

Each level of promise carries one policy for changing a surface at that level, written once in
the map; every surface follows the policy of its level, and no surface carries a path of its
own. What a level's policy has to allow follows from whether the consumers at that level update
together with the product, and data already stored at the user is a consumer that never updates.
An exchange with the external context records whether its consumer updates together with the
product.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** Kubernetes ties the life of a surface to its level rather than to the surface
  itself — "Rule #4a: API lifetime is determined by the API stability level" — and treats stored
  data as a consumer that cannot be made to move: "no API versions that have been persisted to
  storage may be removed […] the API server must remain capable of decoding/converting previously
  persisted data from storage" (Kubernetes deprecation policy,
  https://kubernetes.io/docs/reference/using-api/deprecation-policy/).
- **Relations:** derives from WAY-49@1e1a52ad · related to WAY-34 · related to WAY-48
- **Outranks:** none
- **Verification:** level 1 — invariants: external-exchange-row · promise-level-policy ·
  surface-change-path.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a path written at each surface is written many times and read once, and the same
promise means the same path, so the level — which is the promise — is where the path belongs.
What the path has to allow is not a matter of taste but of who has to move: a consumer that
ships with the product can be changed in the same commit, while one that does not update needs a
route it can take at its own pace. Data already written at the user is the strictest such
consumer, because it never updates and nothing can ask it to, which is why a system that has
persisted data keeps the ability to read it back after the version that wrote it is gone.
Recording at the exchange whether the consumer updates keeps that choice out of the hands of
whoever happens to be making the change.
*Rejected:* a change path written at each surface — the same sentence copied per surface, drifting
apart as they are edited; the path chosen by how important the surface is — importance says how
bad a break would be, not who is able to follow; the trait "updates together with us" recorded
for every dependency inside the product — parts of one repository always update together, so the
trait says something only at the edge.
*Consequences:* a product sets its levels of promise and one policy for each, saying what a
change at that level may do and what it owes the consumer first — a period, an announcement, a
conversion. Those details belong to the product, not to this process. The level a product gives
a format it saves is chosen knowing that the data already stored is a consumer that will never
update.

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
- **Relations:** derives from WAY-40@c3f0b830 · derives from WAY-53@aaeafada · derives from
  WAY-63@f16348c8 · narrows WAY-15@72eb2240
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
rule weakened until the code fits it — the foundation describes the accident (WAY-15); one list
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
- **Based on:** measured on coding agents: context-file-effect@5e46b997. The tools carry channels
  for rules pinned to path patterns: Claude Code (claude-code-path-rules@ac99f128), Cursor rules —
  "Auto-attached when a matching file is in context" (https://cursor.com/docs/rules) — and Kiro
  steering — "Files are automatically included only when working with files that match the specified
  pattern" (https://kiro.dev/docs/steering/).
- **Relations:** derives from WAY-40@c3f0b830 · related to WAY-15 · related to WAY-21 ·
  related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: derived-file-content · generated-pattern-source ·
  generated-overview.
- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
  of models · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* what a context file does for an agent has been measured, and the two halves of the
answer point opposite ways: instructions pinned to files are followed, while an overview of the
repository does not help and is paid for in every call. So the map gives the agent what in
it is an instruction — what this part is responsible for, what it may depend on, what
the decisions in its scope bind — and nothing that merely says where things are. The tools' own
channels carry it, because a rule that arrives with the file the agent opens reaches it at the
moment it binds. Generated rather than written by hand, because a rule file written by hand is a
second copy of the map, which is the reason WAY-21 keeps paths out of decisions in the first
place.
*Rejected:* an overview of the code or the repository generated for an agent — measured as not
helpful, at a fixed cost in context; rule files written by hand — a second copy of the map, drifting
from it; the whole decision log pinned to every path — an agent loses rules as their number grows.
*Consequences:* a picture of the architecture for a human is made on request, outside an agent's
context, and such an overview for an agent leaves the views WAY-04 expects. The set of decisions an
agent reads at the start of a task comes from the step that goes from changed files to parts to
decisions, not from this channel alone: in Claude Code a rule pinned to paths is added only once
the agent reads a matching file. Generated rule files sit in the product's repository and are
checked as derived files (WAY-15).

### WAY-53/1 — How is a derived file compared with what its generator produces?

A derived file is identical to what its generator produces on the same commit, except for values the
file itself declares as varying between runs. A derived file that cannot be produced from scratch is
named in the template of the element it belongs to, and is compared as a subset of its own version
on the commit the branch left the main branch from.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-15@72eb2240 · related to WAY-08 · related to WAY-51
- **Outranks:** none
- **Verification:** level 1 — invariants: derived-file-content · derived-subset-naming.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-20

*Rationale:* the rule that a derived file equals its generator's output catches a file edited by
hand, and that is why it holds. A record of results, however, carries the moment of the run, so a
second run never reproduces it, and the rule would fail on the gate's own output at every pass.
Skipping declared values keeps the rule over everything the generator decides and lifts it only
where the file says the value varies — a narrower opening than taking whole files out. The second
sentence drops a count the earlier wording carried by accident: the exception was written for one
file, and a product that keeps a second such list had nowhere to put it.
*Rejected:* keeping records of results outside the repository — whether an invariant was green on a
given commit can then be read only from whatever ran it, never from the repository; lifting whole
files out of the comparison — it lifts the rule from their content too, where it still holds and
still catches a hand edit.
*Consequences:* the format guard of an element compares derived files with their generators' output
and reads the skipped values from the file itself. The record of an invariant's result carries the
moment of the run and is compared for everything else. The list of violated invariants joins the
list of known violations of the part map's rules as a file that is not produced from scratch. WAY-15
gets a version whose verification no longer spells this out. Where that commit does not exist, the
comparison finds nothing to compare against, and the guard says so, as it already does for an
invariant's version (WAY-57).

### WAY-54/1 — Where does the value of a field in a template come from?

The value of a field is read off the product wherever a tool can read it, and a template asks
for what a value follows from rather than for the name of a value. A field whose value a human
copies unchanged from a record outside the product is marked in the template as transcribed. A
field whose value neither can be read off, nor follows from what the template asks for, nor is
transcribed is marked in the template as resting on a judgment.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** related to WAY-05 · related to WAY-15 · related to WAY-44 · related to WAY-46 ·
  related to WAY-49
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the criticality of a part is computed from its failure modes and the flows it lies
    on, and no criticality is written at a part; a method of checking names the command the gate
    runs, and what kind of check it is follows from that command;
  - violates: a template asks the author to name the kind of a method, where the command the
    gate runs already tells the kinds apart; a field that rests on a judgment stands beside
    fields that are read off, with nothing saying which is which.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* an author asked to name a value picks from the names in front of them and writes a
reason why the nearest one will do; the reason reads well, and the record then says something
that was never true. The failure leaves no trace, because a wrongly named value looks exactly
like a rightly named one. A value read off the product cannot be talked into place, and a
question about the product — which command the gate runs, which files a pattern matches — has an
answer the author can check instead of argue. Where the value is a judgment after all, saying so
keeps a reader from taking it for a reading. This product already decides this way four times
over, and each time the variant in which a person names the value stands in *Rejected* with its
reason.
*Rejected:* leaving the choice to the author with a definition beside each value — a definition
tells apart values a reader already distinguishes, and says nothing about a case none of them
covers; a value meaning "none of these fits" in every closed list — it records what came cheapest
rather than what was true.
*Consequences:* a template that asks for the name of a value where a tool can read that value,
or where a question about the product settles it, is a defect of the template, fixed together
with a decision. A field that rests on a judgment says so where it stands. The skill of the
decisions element gains the sentence the map's skill already holds: a value the template's
closed list does not hold is a question to the human in the same change, and the list grows by a
new version of the decision that closed it. This decision moves to level 1 once a check can tell
apart a field that could have been read off from one that could not.

### WAY-15/2 — What in a foundation is written by hand, and what is derived?

What can be derived from what the product executes — code, configuration, infrastructure as
code, runtime traces — is derived, never written by hand, and what is derived describes the
state. Rules are written by hand: what is allowed, how bad a failure would be and what the
product promises, which the code cannot show.

- **Change:** field change · previous: WAY-15/1
- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** code shows what exists, not the rules: "Your architecture models and your source
  code will not show the same things. The difference between them is the model-code gap", and
  "intensional elements establish general rules that apply to all elements, but standard
  programming languages cannot directly express these rules" (George Fairbanks,
  https://www.georgefairbanks.com/software-architecture/model-code-gap/). A view recovered from
  the code shows accidents as decisions: "Principal architecture decisions may not have been
  implemented and are therefore out of reach of architecture recovery. Conversely, the system
  may reflect inadvertent decisions [...]" (Link et al., ISEC 2019,
  https://arxiv.org/abs/1901.07700).
- **Relations:** related to WAY-04 · related to WAY-08 · related to WAY-11 · related to WAY-53
- **Outranks:** none
- **Verification:** level 1 — invariants: derived-file-content. Level 2 for what is derived and what
  is written by hand — an agent compares the change with the decision:
  - complies: the view of the decisions in force is generated from the log; the existing
    dependencies between parts are read from the dependency graph the product's own tooling
    produces and compared with the allowed dependencies written in the part map;
  - violates: a hand-written list of the product's endpoints kept next to the code; the allowed
    dependencies in the part map copied from the current import graph.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-20

*Rationale for change:* the verification of this decision spelled out how a derived file is
compared with its generator's output, and named a single file that cannot be produced from
scratch. Both now belong to WAY-53, which answers that question on its own, and a rule said in
two places drifts apart.
*Rejected:* leaving the comparison rule here as well — two entries would then say how a derived
file is compared, and whichever is read second would win by accident.
*Consequences:* every derived view has a generator, and a derived file is regenerated, never
edited by hand. Comparing the derived state with the rules uses the part map's rule for
assigning files (WAY-44). How a derived file is compared with what its generator produces, and
which derived files cannot be produced from scratch, is set by WAY-53.

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
- **Relations:** narrows WAY-44@2f2b6227 · related to WAY-09 · related to WAY-16 ·
  related to WAY-21 · related to WAY-45 · related to WAY-47
- **Outranks:** none
- **Verification:** level 1 — invariants: flow-test-location. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: the gate's code is added under `gate/`, and what the gate does with a
    failing check is settled in the task cycle;
  - violates: the one command CI invokes to run every check (WAY-16) is added inside an element's
    directory, or under `gate/` as a call to a body kept in one; `gate/` holds the rule that picks
    which checks a change calls for, or the rule that says what a failing check stops.
- **Review when:** the gate runs as a program CI invokes, and the rule that picks its checks has a
  home · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-20

*Rationale:* the gate runs the checks written in the entries of every element (WAY-16), so a home
inside `elements/invariants/` would put the checks of the decision log and of the part map inside
the element of invariants. The task cycle answers for the steps a task runs through and for how
sharply a change is checked along them — that is when the gate runs and on what, not the code that
runs it; keeping the two apart lets the steps change without moving the gate's code. WAY-44
already gives the rule for files that serve the whole repository rather than any one part: they
are a part of their own. A test of a critical flow has no single part to belong to, because a flow
crosses parts by definition and the gate is what runs it; that is why this decision goes
against WAY-44's rule for tests in this narrow place, and nowhere else. A part of its own is also
what gives the gate its own failure modes and its own criticality.
*Rejected:* the gate in `elements/invariants/` — a program serving every element tied to one of
them; the gate in `task-cycle/` — the gate's code would move whenever the steps of a
task changed; the gate among the files that serve the whole repository, beside `.gitattributes` —
that part answers for files that configure the repository and has no tests of its own, while the
gate has failure modes, tests and dependencies on other parts; a critical flow's test kept with
the single part it tests, as WAY-44 has every other test — a flow runs through several parts and
none of them owns its test, and the cost WAY-44 named is paid by the flow carrying the gate on its
list of parts rather than left unsaid.
*Consequences:* WAY-09 gains `gate/` in its list of the directories a part of the process may
have, and the sentences in WAY-09 and WAY-16 that left the gate's home to be settled between the
invariants element and the task cycle go, both edited in place, since neither entry has reached
the main branch (WAY-07). A critical flow's test living in `gate/` puts `gate` on that flow's list
of parts, so `gate` inherits the flow's criticality (WAY-46), a change to the test lies on the
flow (WAY-45) and is checked against the decisions of every part on the list (WAY-21), and the
coverage of that test agrees with the list (WAY-47); `wording-reaches-dependants` gains `gate` on
its list with this change. The map guard gains a check that a flow's test path lies under
`gate/`, made only against this repository's own map, the way its check of `examples.md` already
is; until it does, the level 1 invariant has nothing that runs it. A file under `gate/` may use
the code of a part the map lets the gate depend on — the existing flow test reads the decision
element's test fixtures, and that is such a dependency, not the gate living in an element. When
the gate's code is built, the gate's dependencies in the map grow to the parts whose checks it
runs. The invariants element gets a format guard of its own, which is not the gate: the guard
keeps the shape of an entry, the gate runs what the entry says to check. Whether a product built
with this process keeps its own gate and flow tests in `gate/` is left to that product.

### WAY-56/1 — How much does one invariant entry hold?

An invariant entry states one invariant in one sentence. The method of
checking and the links that WAY-08 and WAY-17 require stand beside that sentence, not inside it.

- **Change:** new decision
- **Scope:** invariants
- **Based on:** none
- **Relations:** derives from WAY-22@dcf291ea · related to WAY-02 · related to WAY-08 ·
  related to WAY-12 · related to WAY-17 · related to WAY-26 · related to WAY-37
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-sentence-count. Level 2 for one invariant per
  sentence — an agent compares the change with the decision:
  - complies: "every version and review record in the log has every field of the template" is one
    entry, though a commit can break it for a single version or a single field; "every human verdict names
    who checked and when" is one entry;
  - violates: "binding sentences number one to three and contain no *should*, *will* or keyword
    of RFC 2119 in capitals" kept as one entry, though how many sentences there are and which
    words they use are two separate rules; the sentence on fields split into one entry per field.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-21

*Rationale:* an entry that states one invariant has a fingerprint of its own (WAY-02), so a fix to
it flags only what relies on it — a reason WAY-26 gives each principle and each non-goal an entry of
its own — and a deliberate break aimed at it tells whether its method catches it (WAY-08). Where one
invariant ends and the next begins is a judgment: three rules tried against the invariants
written in working form in this log — one property with labelled conditions, a split wherever a
commit can break one piece while the rest holds, one check applied across many items — each gave
two answers or a wrong one on real sentences. So the count of sentences is checked by a script,
and what one sentence may join is judged against a pair of examples, as WAY-12 does for any rule
a script cannot settle.
*Rejected:* one entry for a property, with its conditions as labelled points — no rule told one
property with several conditions from several properties, a fix to one point would flag every
test citing the entry, and a test would need a way to cite a single point; a sentence split
wherever a commit can break some of it while the rest holds — a sentence about every version in
the log would fall apart into one entry per version.
*Consequences:* the template of the invariants element gives an entry its one sentence, and the
element's format guard counts sentences as the decisions guard does, which catches length only:
two rules joined in one sentence pass it and are left to review. The binding part of an invariant
entry is set by WAY-59. What an invariant entry names in the part map, so that a change reaches the
invariants it can break, is set by WAY-62.

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
- **Relations:** derives from WAY-03@4fa941a4 · derives from WAY-10@08118926 ·
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
  derives from WAY-17@b1e26133 · related to WAY-04 · related to WAY-05 · related to WAY-07 ·
  related to WAY-08 · related to WAY-10 · related to WAY-11 · related to WAY-16 ·
  related to WAY-19 · related to WAY-29 · related to WAY-37 ·
  related to WAY-38 · related to WAY-47 · related to WAY-54 · related to WAY-55 ·
  related to WAY-56 · related to WAY-57
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-recovered-form · invariant-recovered-derived ·
  gate-fork-point-evidence. Level 3 for the row — the human deciding the change sets it with the
  gate's report in front of them, and the record of that decision names who and when.
  Level 2 for what counts as already done and what *found* holds — an agent compares the change with
  the decision:
  - complies: entering a game, an agent lists what its save module does, a human chooses "a save of
    another version is rejected whole", the gate reports that the check passes and breaks on the
    commit the branch left from, and the entry's row on the list of recovered invariants reads
    `searched: the save module and its history, the game's own documents` and `found: the comment
    above the save format's version constant at commit <sha>, decision D23 of the game's concept
    document`; an invariant written at a task's foundation step for a feature being built stands
    on no row of that list;
  - violates: *found* reads "old saves are dropped because the rules may have changed"; *found*
    lists a comment explaining how the loader parses a save; an invariant about a field the task
    itself adds is marked recovered because its check found nothing to fail on the older commit.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* WAY-28 lets an invariant recovered from an existing product bind before anyone knows
why it holds, and asks for a note that it was recovered. Without the note it reads like a rule
someone wrote, and whoever later weighs a change to it has no sign that the reason for it was never
settled in the log. Whether an entry was recovered cannot be read off the product (WAY-54): a check
run on the older commit also passes where the thing it checks does not exist yet — two empty sets
compare equal (WAY-47) — and it passes for a new rule the product happened to meet before anyone
wrote it down. A deliberate break on the older commit (WAY-08) removes the first case and not the
second, so the gate's run is evidence for the human, who already decides every change to the
foundation (WAY-10), not the ruling. The gate runs the method, never the element's format guard, which keeps only the shape of the entry
(WAY-55). The same line places both cases of the return step (WAY-11): behaviour the product had
before the task can be recovered, while a rule the implementer writes into the task's own code was
not there before the task and stays off the list. Recording the search spares the next agent the same
search, as WAY-29 does for an inherited decision. *found* points to places rather than quoting
them, because an invariant says nothing about why (WAY-22), and it lists a place calling for a
different behaviour too, since that is what a human weighing the invariant most needs to see.
*Rejected:* the mark only where no cause is known — when the process enters a product, the cause
usually sits somewhere that is not a decision entry, such as a comment in the code, a concept document or a line
of requirements, and, tried on a game this process would enter, the rule gave two answers for every
such case; a row on the list for every entry that names no decision — WAY-22 lets an invariant
stand with no choice behind it, so one written for a feature being built would stand there as
recovered; the mark set
by the gate from the check's result on the older commit, with or without a deliberate break — tried
on the same game, a rule written for a feature in progress passed there because the feature did not
yet exist, and one sentence got either mark depending on how its test was phrased; a link to a
decision kept outside the log, such as a numbered decision in a product's concept document, counted
as naming a decision — nothing checks it, and the invariant would read as chosen; the reason quoted
in *found* — it would put a why into an invariant; a field of origin with a value "derived from a
decision" — it repeats the link WAY-17 already requires; a reference to a requirement of an outside
catalogue as a field of the invariant entry — such a requirement is a fact about the world, the
reason WAY-04 turns down external constraints as a field of the map, and an invariant names the
facts it rests on under WAY-17.
*Consequences:* the template of the invariants element names the field, gives its form and marks it
as resting on a judgment; the element's format guard checks the first two invariants above, and
the gate the third, which nothing runs until the gate exists. Where the method cannot run on the older
commit — a human inspection, a test that does not build there, a repository with no main branch, as
this one until the foundation reaches it — the gate reports it as unchecked, never as passing
(WAY-38), and the human sets the field without that evidence. An entry whose binding part changes, by a
raised version (WAY-57) or by a split or a merge (WAY-64), enters again, and its field is set again. A place in *found*
that records a choice is recovered as a decision when a later task touches the part (WAY-28) — the
change that enters the invariant does not itself count as touching it; a reason given by the human
who chooses the invariant is recorded as an inherited decision given by that person (WAY-29). Once
the invariant names such a decision, its field turns to `none`, and neither the field nor the new
link raises its version (WAY-59). An invariant a human takes from a product's own requirements, which the product does
not meet yet, holds `none` and enters as an invariant the product violates, whose place is set by
WAY-51; its source is not recorded by this decision. The field's readers are the
human weighing a change to the invariant and the agent recovering a part's decisions. WAY-28's
consequence on the note is edited in place to name this decision, while the element still has no
template to carry the note (WAY-37). An invariant holding a condition taken from a requirement of an
outside catalogue names it in *Rests on* (WAY-73); how such a requirement is written as a fact is set
by WAY-86.

### WAY-59/1 — What is the binding part of an invariant entry?

The binding part of an invariant entry is its one sentence, and the entry's fingerprint covers
that sentence alone. Everything else the entry carries stays outside the fingerprint — such as its
method of checking, the links it names beside the sentence, its version and a declaration of a
correction.

- **Change:** new decision
- **Scope:** invariants, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@3ffcbd46 · derives from WAY-56@06700ffd · related to WAY-07 ·
  related to WAY-08 · related to WAY-09 · related to WAY-10 · related to WAY-17 ·
  related to WAY-19 · related to WAY-22 · related to WAY-31 · related to WAY-37 ·
  related to WAY-42 · related to WAY-55 · related to WAY-57 ·
  related to WAY-58
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* a fingerprint exists to flag what relies on an entry's binding part (WAY-02), and for an
invariant the first thing that relies on it is its version: when the fingerprint differs from the
one on the main branch, the version rises unless the human deciding the change confirms a
correction, and every test citing the entry fails the gate until the foundation step checks it
against the new binding part (WAY-57). The fingerprint moves on any change other than whitespace
(WAY-02), so it is the signal that asks whether the invariant now demands something else, and it
has to ask only where that can have happened. What an invariant demands is its sentence
(WAY-56). The rest of the entry says something else: a method says how the sentence is checked, and
a new test for the same meaning is accepted under WAY-08, with the panel and the human WAY-10
names, without touching the tests that cite the entry; a link names what the invariant rests on or
comes from, and is often written later, as a decision found behind a recovered invariant is
(WAY-58); a version and a declaration of a correction are worked out from the fingerprint and
cannot sit inside what they are worked out from. A raise caused by any of them would fail every citing test for a change that asks nothing of
the tests, and a flag raised for nothing is cleared without reading. The part map draws the same
line (WAY-42): its entry's binding part is one sentence, and the fields that change for other
reasons stay outside. This decision does not say what the sentence has to name, and that gap has a cost wherever
a condition that decides whether a commit makes the invariant true stands outside the sentence,
since a change to it raises no version, and whether it flags anything turns on whether the
invariant's link to that entry carries a fingerprint (WAY-31). Three kinds of such place can be named: a comparison with "the main branch", which gives
different answers against its tip and against the commit a branch left it from; a threshold whose
statistic or population sits in the method; and a list or a definition held elsewhere — in another
entry, in a template, in a section of the map — and reached through a word of the sentence, as the
directories of the process are held in WAY-09, whose list WAY-55 edited in place. WAY-60 settles
where each may stand; how a change to the place holding the third reaches the
invariant is set by WAY-61 and WAY-62.
*Rejected:* the whole entry as the binding part — a new method, a link written later or a fixed
field would raise the version and fail every citing test for nothing; the method of checking inside
the binding part — a new test for the same meaning would fail every test citing the entry; a
fingerprint per field — every reference would have to say which field it relies on.
*Consequences:* the template of the invariants element marks the sentence as the binding part. Where
a condition that decides an invariant may stand is set by WAY-60; which links between entries carry
a fingerprint is set by WAY-31. The sentences of WAY-57 and WAY-58 that placed the version, the
declaration of a correction and the recovered field outside the fingerprint answered this question
in passing and lose those clauses (WAY-19); with them go WAY-57's consequence saying it partly
answered the question, the half of another that waited for it, and WAY-58's level 1 invariant on the
field and the fingerprint, the reason it gave for it and its consequence leaving open whether a
decision named later raises the version — it does not. Both are edited in place and accepted
again (WAY-07). WAY-56's consequence that left this question open is edited in place, with its
fingerprint unchanged. The invariants element's format guard runs the invariants above.

### WAY-60/1 — Where may a condition that decides an invariant stand?

A condition deciding an invariant stands in its sentence, or where changing it takes a foundation
change a human decides, or where a decision in the product's log or the pinned the-way places it.
An invariant's sentence names no branch, and measures any change it speaks of against a commit on
the gate's list (WAY-61). A sentence bounding or equating a quantity measured while the product runs
names its bound or tolerance, statistic and population.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate
- **Based on:** none
- **Relations:** derives from WAY-59@2d716c3f · derives from WAY-22@dcf291ea ·
  derives from WAY-56@06700ffd · related to WAY-05 · related to WAY-07 ·
  related to WAY-10 · related to WAY-12 · related to WAY-31 ·
  related to WAY-34 · related to WAY-38 · related to WAY-51 · related to WAY-53 ·
  related to WAY-57 · related to WAY-58 · related to WAY-61
- **Outranks:** none
- **Verification:** level 1 — invariants: sentence-branch-names · sentence-gate-values. Level 2 for
  the rest — an agent compares the change with the decision:
  - complies: "every version and review record in the log has every field of the template"; "the
    list of violated invariants is a subset of its version on `{fork-point}`", the commit WAY-53
    chose;
  - violates: "every request is answered within the limit set in `config.py`"; "every fingerprint
    on `main` equals the current fingerprint of the decision it names"; "a commit that changes
    `template.md` also appends a decision version to the log"; a bound written "~2 seconds".
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* the fingerprint that moves an invariant's version covers the sentence alone (WAY-57,
WAY-59), so a condition outside it moves unseen. That is safe only where moving it takes someone
deciding: a human changing the foundation (WAY-10), or a decision placing it, as WAY-38 and WAY-53
do. A condition an ordinary step of implementation can change could be loosened by the change the
invariant exists to stop. With no such home yet, a condition stands in the sentence, and the
invariant enters unchecked (WAY-38). A branch names a different commit by the hour, so a sentence
naming one is true or false by the hour and is no invariant; what the main branch alone holds
is stated where `{merge-onto}` exists. A measured bound means nothing without its statistic and
population; a count needs neither.
*Rejected:* every condition in the sentence — on this log's invariants it gave two answers wherever
a measure met a definition or a method; a closed list of places — each try left out places the log
uses; every place outside the foundation forbidden — WAY-38 and WAY-53 place conditions in the
product; an invariant kept aside until its condition has a home — nothing counts it, the gap WAY-51
rejects; a commit's parent as the base of a change — a task spreads one change over several
commits.
*Consequences:* the invariants template states these rules, and its guard checks the level 1
invariants. A sentence measuring a change takes `{fork-point}` unless the decision it derives from
chooses `{merge-onto}` by its own edit or version (WAY-07); WAY-57 chose `{fork-point}`, and
so does an invariant deriving from no decision (WAY-58).

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
- **Relations:** derives from WAY-08@9d45e0a9 · derives from WAY-16@5c1d60d4 ·
  derives from WAY-54@f37c232a · derives from WAY-57@4a838784 · derives from WAY-38@6e10c3fd ·
  derives from WAY-60@c85d1ac0 · related to WAY-03 · related to WAY-05 · related to WAY-07 ·
  related to WAY-10 · related to WAY-12 · related to WAY-17 · related to WAY-22 · related to WAY-24 ·
  related to WAY-31 · related to WAY-34 · related to WAY-37 · related to WAY-43 · related to WAY-45 ·
  related to WAY-47 · related to WAY-48 · related to WAY-49 · related to WAY-50 · related to WAY-53 ·
  related to WAY-55 · related to WAY-56 · related to WAY-58 · related to WAY-59
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-method-form · method-gate-values ·
  gate-verdict-per-entry · gate-pass-without-verdict · gate-method-order · test-runner-pass-line.
  Level 2 for what a method checks — an agent compares the change with the decision:
  - complies: "every version and review record in the log has every field of the template" names the
    decision guard run on `foundations/decisions.md`, and one run of the guard records a verdict for
    each invariant it checks; "a save of another version is rejected whole" names a test that hands
    the loader a save written in another version, since the sentence is about the loader; an
    exploratory test names the command that starts an agent on the working product with its steps;
    whether an image's text alternative describes it, after the accessibility check marked it
    incomplete (WAY-08), names the path of the checklist a person assesses the page against;
  - violates: a sentence about the real log names, as its method, the guard's test that feeds the
    guard logs made up for it; a test that runs the guard on the real log and asserts only its exit
    code is cited for one of the invariants the guard checks; an entry carries "runs as: script"
    beside its command; the gate gives every invariant a guard checks the guard's exit code; a
    command names the main branch where the sentence names `{fork-point}`.
  Level 2 for which run's output a method reads — an agent compares the change with the decision:
  - complies: the map guard reads the coverage file a critical flow's test leaves, as WAY-47 places
    it, and the gate runs the flow's test first;
  - violates: an invariant's method reads the record another invariant's guard run left, and no
    decision places that reading.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* WAY-08 asks every invariant to name its method and to take its result from running it,
and WAY-16 has the gate read the methods from the entries, so a method is something the gate can run
or hand to a person, never prose. Two forms cover that, and they differ in form: a command, which
begins with the program it runs, and a path alone. An exploratory test run by an agent on the working
product is a test (WAY-08) and needs no form of its own, since a command can start the agent with its
steps; a path is then left to the one check only a person can make. The form is the route, and no kind
is named beside it, because a kind says nothing the method does not already say and can disagree with
it (WAY-54). A method checks what its sentence is about: a sentence about the log is checked by reading
the log, while a test that feeds a guard made-up logs shows that the guard catches a break — what
WAY-08 asks before a method counts — and is the method of a sentence about the guard. In this
repository the guards belong to the product, so both kinds of sentence exist here, and each needs its
own method. One run checks many invariants, as one pass of a format guard checks every rule on its
template's list and one run of a test suite checks every test, so an exit code tells at most that
something failed, and not even that where a check was skipped; a run once per entry would repeat an
expensive run for each invariant it serves, which WAY-47 refuses for coverage. So the run records a
verdict for each entry, and a result comes from a record of a run, never from a status written by
hand (WAY-08, WAY-53). A verdict counts only for the entry's current version, so that a raised
version fails every check still written for the old meaning, as WAY-57 has it for a test. Silence is
never a pass, because a check that quietly sees nothing passes (WAY-38). A comparison the sentence
ties to a fixed commit (WAY-60) needs that commit in the command; a command that resolved a branch
or a revision itself would answer by the hour rather than by the commit, which WAY-60 rules out, so
the gate fills the commit in from a closed list. Anything else in the command that varied between
runs would make the verdict depend on who ran it; what the runner's own environment supplies — its
network access, and for a product its interpreter — is settled neither here nor by WAY-63, while
the-way's own interpreter is set by WAY-89.
*Rejected:* a kind of method named beside it, as `script`, `declared` or `human` — nothing the gate needs
that the form does not tell, and a second value that can disagree with it (WAY-54); a form of its own for
an exploratory test run by an agent, as a path to its steps — it looks like the path a human assesses
against, and telling them apart would take a kind named by the author; the exit code of a run as the
verdict of every invariant it checks — one broken rule fails them all, and a rule the run skipped passes
with the rest; one run per entry, with a selector for the entry — a check shared by many invariants runs
as many times, and a product's own test runner cannot always run a single test; a verdict for whichever
version a check cites — a check still written for an earlier meaning would pass the raised entry; the
tests of a check, run on input made up for them, as the method of a sentence about the data that check
reads — they show the check catches a break, not that the data holds; a method in prose — the gate
cannot run it (WAY-16).
*Consequences:* the template of the invariants element gives the two forms of a method; the closed
list of values the gate fills into a command, which starts with the commit the task branch left the
main branch from (WAY-57), which is the last commit of the main branch the branch contains, and the
commit of the main branch that a merge into it is made onto, and grows by a new version of this
decision; and the closed list of formats a run's record may take, which starts with the-way's own
record of a run and grows the same way, together with the adapter that reads a product's format
(WAY-38). Where a commit on the list does not exist, as the main branch in this repository, the gate fills in `none`
in its place and the check records its verdict, as WAY-57 already says for its own checks; the
gate never turns that into a pass. A command that leaves its record in a file names that file's path
in the command itself, at a place in the working tree that does not change between runs; a method
may read what another method's run left only where a decision places it, as WAY-47 does, and the
gate then runs the first before the second. What a run leaves — its output, or the file its command
names — is what the gate reads; the record of the result it keeps in the repository is the one WAY-53 compares. The result an entry has is the
verdict of the run on the commit being checked; the run WAY-58 asks for on the commit the branch
left from is evidence for a human, not a result. The format guards of decisions, of the part map and
of invariants, once they record a verdict for each invariant they check, cite those invariants and
are invariant tests under WAY-65, read-only during implementation (WAY-03) and changing through the
panel (WAY-10). Recording a verdict for each invariant, and taking `none` in place of a commit
that does not exist, changes the commands of those three guards, which the map declares as
surfaces; the change travels on the change path of their promise level (WAY-49, WAY-50). A failure a run
records for no entry is reported by the gate as such, never dropped; how it counts is set by WAY-63.
The invariant of the critical flow `wording-reaches-dependants` was a sentence about the real log
with a test on made-up logs as its method; the same change rewrites it in the map, in place
(WAY-43), as a sentence about what the decision guard reports, and the log's own freshness stays
WAY-31's invariant, checked by the guard run on the log. The adapter through which the gate reads a
product's record of a run accepts what the map's external context marks as untrusted, so its files
become the trust boundary of the gate part (WAY-48) once they exist. A quantity measured while the
product runs is checked by a command that takes its measurements on the commit being checked, where
the population the sentence names is those measurements; a population the product meets only in use,
such as the loads real players make, fits neither form, and such an invariant still enters, as
WAY-60 has it, with its method written as `TODO — decision pending: the method of a population met
only in use`, and the gate reports it as unchecked, never as passing (WAY-38), until a new version
of this decision gives that method. Where a product's method runs the-way's own guard, the path of
the pinned the-way in the command, and the interpreter that runs it, follow from how the product
pins the-way (WAY-34), which this decision does not settle. How the result of a human assessment is
recorded, and which states a result may take and which of them make the gate's command fail, is set
by WAY-63; how a check cites its invariant, by WAY-65. When a method counts stays with WAY-08 — the
deliberate break, and k of n runs for a method that does not give the same verdict every time; k and
n stand in the method's command, so the verdict one run records for the entry already covers n runs
of the check. Who writes the break is set by WAY-69. WAY-16's consequence that left the reporting of
a method the gate cannot run to the invariants element is edited in place to point to WAY-63.

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
  derives from WAY-08@9d45e0a9 · related to WAY-16 · related to WAY-38 · related to WAY-45 ·
  related to WAY-47 · related to WAY-53 · related to WAY-55 · related to WAY-57 · related to WAY-58 ·
  related to WAY-60
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-method-form · human-verdict-trace ·
  gate-result-values · gate-unchecked-reason · gate-reported-set · gate-exit-code. Level 2 for the
  reasons — an agent compares the change with the decision:
  - complies: a flow's list of parts with no coverage file is `unchecked` (WAY-47); so is a check
    needing a commit the gate filled in as not existing;
  - violates: a guard whose call to git fails reports `unchecked`; a human's `pass` stays in force
    after a change since the assessed commit reaches the entry; a critical flow's test is left out and
    the command exits zero.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a check can always call itself unchecked, so `unchecked` holds only for listed reasons,
and an entry with no verdict for any other reason is `error`. `unchecked` leaves the command at
zero, because WAY-60 and WAY-61 let an invariant enter before its method can run, and WAY-47 makes
"unchecked" a state a human reads, not one that stops work.
*Rejected:* `unchecked` making the command fail — every invariant entering without a method would
fail every change; an open list of reasons — whatever a check says of itself would pass; a third
exit code — nothing reads it; a human's verdict valid for the entry's version — it outlives every
change to the product (WAY-08).
*Consequences:* the template lists the reasons for `unchecked`, and the list grows by a new version
of this decision: the method reads `TODO`; the method is a path and no human verdict is in force;
the method's command or file is not declared or produced, except a command declared on the commit
the branch left the main branch from, whose drop makes the result `error` (WAY-38, WAY-47, WAY-51);
the method takes a commit the gate filled in as not existing; the entry stands on the list of
quarantined invariants at its current version, and the committer date of the commit being checked
is no later than the quarantine's end date, a later one making the result `error` (WAY-68); for a fact, a probe ran on a release of its tool
outside *Holds for* (WAY-91). Where a
human verdict stands, what it names and how long it is in force is set by WAY-83. The facts whose
results the gate reports are those WAY-82 has it run. A declared command that cannot start, or a record off a closed list, is
`error`. Runs on a deliberate break, and the run WAY-58 asks for, give evidence, not results. Which
`fail` a listed violation excuses, and when a checked invariant may turn `unchecked`, is set by
WAY-51 and WAY-68.

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
- **Relations:** derives from WAY-02@3ffcbd46 · derives from WAY-56@06700ffd ·
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
on the commit being checked.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, relation-model, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-03@4fa941a4 · derives from WAY-17@b1e26133 ·
  derives from WAY-57@4a838784 · derives from WAY-61@4804d070 · related to WAY-12 ·
  related to WAY-60 · related to WAY-62 · related to WAY-63
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-citation-version · invariant-citation-target ·
  data-line-target · invariant-tests-of-change · test-runner-pass-line. Level 2 for where a
  citation stands — an agent compares the change with the decision:
  - complies: the decision guard cites `log-entry-field-presence/1` at the rule checking
    fields; a test comparing a load with a recorded save names the save on a `data:` line;
  - violates: a test file cites at its top every invariant its tests serve, though the checks
    giving the verdicts are its methods.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* WAY-61 already makes the file holding a check that records verdicts for invariants it
cites an invariant test; this decision gives that citation its written form and settles which files
carry it. One run checks many invariants (WAY-61), so a citation stands where the verdict is given:
at the smallest unit whose outcome a run records on its own — a test for a test runner, a rule's
report for a guard. A file cited on either commit counts, so a change that drops a citation or
deletes the file is still a change to an invariant test. A recorded save a test compares
a load against is named on `data:` by the test that reads it, the dependent end (WAY-17).
*Rejected:* the paths a method names as the invariant tests — a method names the data its
sentence is about, not a file that checks anything; one citation per file — one broken check
fails all it serves (WAY-61); only files citing on the commit being checked — dropping a citation
frees the file.
*Consequences:* the template gives the `invariant:` and `data:` lines, in the comment form of the
file's language. Several checks citing one invariant in one run pass only when each of them does.
A path a human assesses against is no invariant test: a change to it reaches its invariant
(WAY-62), and the human verdict lapses (WAY-63).

### WAY-68/1 — What happens to a check that gives different verdicts on one commit?

A check that cites an invariant and records both `pass` and `fail` for one commit is answered by a
foundation change, quarantine last and never for an invariant a critical flow names. A quarantine
stands in `foundations/invariants.md`, names the entry's current version and an end date, and its
result is `unchecked` until the checked commit's committer date passes that date, then `error`.
Until it is answered, a recorded `fail` stays the entry's result on that commit, whatever a later
run records.

- **Change:** new decision
- **Scope:** invariants, gate, task-cycle
- **Based on:** a quarantine works with an end date: "Fix immediately … Quarantine: If investigation
  or fix will take longer than the required response time" (GitLab, Quarantine process,
  https://handbook.gitlab.com/handbook/engineering/testing/quarantine-process/). A rerun hides what
  it absorbs: it "encourages developers to ignore flakiness in their own tests" (Micco, Google
  Testing Blog, 2016, https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html).
- **Relations:** derives from WAY-08@9d45e0a9 · derives from WAY-61@4804d070 ·
  derives from WAY-63@f16348c8 · related to WAY-03 · related to WAY-10 · related to WAY-24 ·
  related to WAY-45 · related to WAY-60 · related to WAY-64
- **Outranks:** none
- **Verification:** level 1 — invariants: quarantine-position-form · quarantine-flow-invariants ·
  gate-quarantine-result. Level 2 — an agent compares the change with the decision:
  - complies: a save-load test fails and then passes on one commit, and the panel accepts a wait
    for the load-finished signal instead of a fixed interval;
  - violates: a failing test is called flaky with no `pass` recorded on that commit; a fixed-wait
    failure is quarantined instead of fixed as a change of mechanics; a green rerun is taken as the
    commit's result while the `fail` it follows stands unanswered.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* a test that flips stops every task it reaches, and the implementer may not touch
it (WAY-03), so "it is just flaky" becomes the way around the gate unless the claim needs evidence:
a pass and a fail on one commit. A later green run
does not undo the one recorded, or rerunning until green becomes the answer. `unchecked`, and
`error` once the date passes, are set as WAY-63's other reasons are, not the hand-written verdict
WAY-08 forbids. A critical flow's test runs on every change (WAY-45), and a quarantine
would silence it. Moving the end date is a foundation change a human decides (WAY-10), not the
silent extension WAY-24 rejects.
*Rejected:* a row of the list of violated invariants — that list settles whether the product
meets an invariant, not whether a check is trusted (WAY-51); a quarantine field in every entry —
every entry pays for a rare case; a count of passes in a row to enter — k of n (WAY-08) decides
what enters; the date of the run — the result would follow the hour;
deletion once the date passes, as GitLab has it — an end date repaying by weakening the check
(WAY-51).
*Consequences:* `foundations/invariants.md` ends with a list of quarantined invariants beside its
withdrawn identifiers. A violated invariant may be quarantined, and its row of that list stays.

### WAY-69/1 — Who writes an invariant's sentence, its check and its deliberate break?

An invariant's sentence and a check that cites it come from separate acts by different agents, and
the deliberate break the check is accepted on is written from the sentence by an agent other than
the check's author, with that check and the files it reads out of its input.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate, task-cycle
- **Based on:** what a model sees of a check, it may game: visible-scoring-reward-hacking@39a85ced.
  With the check in the loop the agent builds for it: oracle-in-loop-building@d13c8e26.
- **Relations:** derives from WAY-08@9d45e0a9 · related to WAY-03 · related to WAY-05 ·
  related to WAY-10 · related to WAY-11 · related to WAY-16 · related to WAY-58 ·
  related to WAY-61 · related to WAY-65
- **Outranks:** none
- **Verification:** level 3 — the human deciding the foundation change assesses how the work was
  handed out, and the record of that decision names who and when.
- **Review when:** the design of the task cycle begins, or no model in the range of fact
  oracle-in-loop-building is Active in Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* a break chosen by the author of a check is aimed at what the check does, not at what
the sentence says, so the teeth WAY-08 asks for show only that the check catches itself. The same
holds for the check: written by whoever wrote the sentence, it inherits the reading that sentence
was written with, and a sentence two readings wide stays wide. Keeping the acts apart costs the
order of the work and nothing else, and is the move WAY-03 and WAY-10 already make: take the
oracle out of the hands of whoever is measured by it, rather than forbid its use. The finding on visible scoring measured a model of another publisher only, and this decision takes it across publishers (WAY-85).
*Rejected:* hiding checks from the executor — it costs honest work, and WAY-16 keeps one command
for an agent, CI and a human; one agent writing all three under a written rule not to aim a break
at its own check — a rule written in prose stops nothing (WAY-03); a field naming the writers —
nothing reads it (WAY-05), and the gate already reports the break WAY-58 asks for.
*Consequences:* the task cycle hands out the sentence, the check and the break as separate
instructions, and gives the record of a change its home; until then nothing in a change shows
which agent wrote what, and the human deciding the change is the only reader, so the decision
moves to level 1 by a field change once that record exists. A break written without the check may
pass for a reason the sentence does not name, and WAY-58's report is where that shows: the entry
is accepted only once the break makes the check fail (WAY-08). A check joins a file that other
checks already stand in, so this binds the act of writing a check, not the history of its file
(WAY-65).

### WAY-70/1 — What may a check compute for itself?

A check that cites an invariant takes the input it asserts on and the value it expects written out,
wherever the code its invariant is about would otherwise compute either; only the side it compares
against comes from the run.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, relation-model
- **Based on:** none
- **Relations:** derives from WAY-08@9d45e0a9 · related to WAY-03 · related to WAY-10 ·
  related to WAY-57 · related to WAY-61 · related to WAY-65 · related to WAY-69
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the flow test in `gate/` carries the wording and the fingerprint it expects as
    literals, so a change to the length of a fingerprint makes it fail;
  - violates: a test builds the reference it asserts on by calling the code its invariant is
    about, and expects the message that same call returns; a test reads the value it expects, at
    run time, from the file its invariant is about.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* where both sides of a comparison come from the same code, a change to that code moves
them together and the test stays green — it never had teeth, rather than losing them, and nothing
in its record says so. Measured here: raising the length of a fingerprint from 8 to 10 in
`relation-model/fingerprint.py` left all eight tests of the decision guard's `Relations` class
green, `test_stale_fingerprint` among them, and failed only two: the flow test in `gate/`, which
carries its fingerprint as a literal, and the test that runs the guard on the real log, where
every reference still carries the fingerprint computed at the old length. Writing the input out as
well is what the measurement asks for: four of the five calls to `fingerprint()` in that file
build the input, not the expected value.
*Rejected:* writing out the expected value alone, as the draft template has it — the same
measurement shows it misses four cases out of five; naming, on a `data:` line, each file a verdict
leans on — no cutoff was found: the map guard's own test leans on every file git tracks, so through
WAY-65 and WAY-03 the whole repository would be read-only during implementation, which is the
variant WAY-65 rejects.
*Consequences:* the tests of both guards are written under this rule; the decision guard's `Relations` class is where it bites. The draft template's sentence on
the expected value is edited in place to this wording and gains its citation (WAY-37, WAY-54).
Which files a check names, so that a fixture or a builder of its input cannot be changed
underneath it, stays open — `gate/test_wording_reaches_dependants.py` imports its fixture and
names it nowhere, and it protects it today with an assertion that the fixture still matches a
literal.

### WAY-71/1 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every entry of its kind —
in every version of a decision and every review record, the fields their forms give — holding a
value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there, `TODO` that something
is missing. The main branch holds `TODO` only in an invariant's or a fact's *Method*, and in an
invariant's *Rests on* until the facts element has entries. A guard reports a missing field, or a
word not given it, as an error.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-05 · related to WAY-09 · related to WAY-17 ·
  related to WAY-38 · related to WAY-46 · related to WAY-54 · related to WAY-57 · related to WAY-58 ·
  related to WAY-60 · related to WAY-62 · related to WAY-63
- **Outranks:** none
- **Verification:** level 1 — invariants: log-entry-field-presence · log-entry-field-words ·
  log-entry-merge-todo · map-entry-field-presence · map-entry-field-words ·
  invariant-entry-field-presence · invariant-entry-field-words · invariant-entry-merge-todo ·
  fact-entry-field-presence · fact-entry-field-words · fact-entry-merge-todo ·
  glossary-entry-field-presence · glossary-entry-field-words · glossary-entry-merge-todo ·
  decision-verification-level · decision-change-kind ·
  review-when-form · review-next-check. Level 2
  for what `none` states — an agent compares the change with the decision:
  - complies: an invariant whose author searched the log and found no decision it derives from
    reads `Derives from: none`; a decision whose source is silent on what it rests on reads
    `Based on: TODO — <what is missing>` until a human answers;
  - violates: an invariant reads `Derives from: none` though nobody searched the log; a decision
    reads `Based on: none` where its source says nothing of what it rests on.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a field left out on purpose cannot be told from one forgotten (WAY-58). `none` and
`TODO` carry that difference only where a reader acts on them — the map's guard reads `TODO` in
*Depends on* as no dependency, and `TODO` in *Part* gives the gate no part to run the invariant in
(WAY-62) — so a field takes a word only where its template says what it means there. `TODO` marks
work in progress, and the main branch describes the product as it is (WAY-01), so a `TODO` there is
a gap nothing counts, except in *Method*, which the gate reports unchecked (WAY-63), and in *Rests
on*, where the fact stands with its source until it has an entry to name (WAY-31); keeping such an
invariant out is the gap WAY-60 rejects. A fact's *Method* takes `TODO` on the same ground, and its
source never (WAY-80).
*Rejected:* a decision for the invariants element alone — every element to come would need a copy; a
wider scope for WAY-05 — its question is how a decision entry is written; `none` and `TODO` in every
field of every element — the readings above; optional fields left out when empty — an intended gap
and a forgotten one look the same; for facts, a field of state and a ratcheted list of unchecked
facts — three mechanisms where one serves.
*Consequences:* each element's template says which of the two words each field takes — the decision
template in its table of states, the others in the form of each field. A guard warns on a `TODO`
its template gives, and reports it as an error where `{merge-onto}` exists (WAY-60), which leaves
the merge creating the main branch unchecked. A ratchet for facts comes back once unchecked facts
get in the way. Each
element's guard checks the level 1 invariants above for its own entries;
`invariant-entry-merge-todo` drops *Rests on* once the environment facts element has entries.

### WAY-72/1 — In what language is a product's foundation written?

A product's foundation is written in English, whatever language the product shows the people who
use it and whatever language its team speaks.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts, elements-common
- **Based on:** none
- **Relations:** related to WAY-04 · related to WAY-05 · related to WAY-35 · related to WAY-38 ·
  related to WAY-60 · related to WAY-71
- **Outranks:** none
- **Verification:** level 1 — invariants: template-language. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: the foundation of a game whose players read Polish, built by a team that speaks
    Polish, is written in English;
  - violates: a product starts its decision log in Polish because its users and its team speak it.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* the fields, the words `none` and `TODO` and the kinds of change are English in every
template, and the format guards check words in English: the decision guard forbids *should*, *will*
and the keywords of RFC 2119 and ends a sentence only before a capital from A to Z, and the
invariants guard forbids "main branch" and "task branch" outside quoted text. An entry in another
language passes those checks without a word, so they look kept while checking nothing, and keeping
them for another language takes a list of words and a sentence counter for each language a product
speaks. One language also lets the entries of this repository serve as examples for every product.
*Rejected:* entries in the language of the product, with the words of each check listed per
language in the templates — every check grows a list for each language used, and a language with
none is checked by nothing; the language of the file, asked for when the file has no entries — the
checks of words go silent on every other language; a guard reporting an entry in another language
as unchecked — it would have to recognise the language first, which the standard library cannot do
(WAY-38).
*Consequences:* each element's template states that its entries are written in English, and the
element's skill reads the rule from there and asks for no language (WAY-35). How text the product
shows the people who use it stands in an entry — quoted in its own language or described in
English — and how a source in another language is cited are not settled here; the first product
whose users read another language settles them.

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
- **Relations:** derives from WAY-17@b1e26133 · derives from WAY-60@c85d1ac0
- **Verification:** level 1 — invariants: fact-dependants. Level 2 for which facts an invariant's
  *Rests on* names — an agent compares the change with the decision:
  - complies: `script-imports` rests on `python-stdlib-modules`, not on a finding a decision it
    derives from quotes;
  - violates: an invariant rests on the report of a past failure its decision quotes; an invariant
    bounding a page's load time by an outside standard's threshold reads `Rests on: none`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

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
- **Based on:** JSON Lines holds one JSON value on each line (json-lines@f16c5b84) and is "a
  convenient format for storing structured data that may be processed one record at a time"
  (https://jsonlines.org/); Python 3.14's `json.loads` reads each such line: "but instead of a
  file-like object, deserialize s (a str, bytes or bytearray instance containing a JSON document) to
  a Python object" (https://docs.python.org/3.14/library/json.html).
- **Relations:** derives from WAY-61@4804d070 · derives from WAY-63@f16348c8 ·
  derives from WAY-65@fbf6bef4 · related to WAY-38 · related to WAY-47 · related to WAY-48 ·
  related to WAY-49 · related to WAY-53
- **Outranks:** none
- **Verification:** level 1 — invariants: run-record-form · run-record-path · run-record-lines.
  Level 2 for the report beside the record — an agent compares the change with the decision:
  - complies: the decision guard, given a record's path, writes its verdicts there and still
    prints its report for a person;
  - violates: a guard writes its verdicts only into its report.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-29

*Rationale:* one line per verdict survives a run that stops halfway: the lines before the stop
stay readable, and an invariant without one gets no pass (WAY-61). JSON escapes whatever a
description holds, and the standard library reads it (WAY-38). A file left by an earlier run would
give verdicts for a run that did not happen, and a tracked one would change with every run. Each
key has a reader: the gate the invariant, verdict and reason (WAY-63), a person the check and
description of a failure; several checks citing one invariant each give a line (WAY-65). A check
that cannot read what the product does not produce says so, since the gate cannot tell silence
from a crash (WAY-47).
*Rejected:* plain text lines — a description with spaces needs a syntax of its own; JUnit XML — its
unit is a test case, not an invariant; a product's format, read through an adapter (WAY-61); the
run's output as the record — a person loses the guard's report, and a test runner mixes in its own;
`pass` and `fail` alone — a check that cannot read a coverage file could only stay silent, which
the gate reads as `error`; the commit, the moment and the tool versions in every line — the gate
knows them, and nothing would read them; one key `entry` for both — a rename across every guard,
test and record written; a fact's verdict under `invariant` — the key would lie about what it
names.
*Consequences:* the invariants template's closed list of formats names this form as the written
form of this decision. The gate runs no command naming a path git does not ignore, and a record
holding a line off this form gives `error` to every entry whose method wrote it (WAY-63). The
record of results the gate keeps (WAY-53) is another file, set with the gate. The form is a
surface of the-way (WAY-49), and the gate's reader of it a trust boundary (WAY-48); adding `fact`
travels on the path of that surface's promise level (WAY-50), and the runner reads the key once the
facts guard exists. WAY-61's
sentence on what the gate reads and WAY-53's rationale are edited in place (WAY-07).

### WAY-76/1 — How much does one environment fact entry hold?

An environment fact entry states in one sentence one fact that one edition of one source says, with
one reason to change, and nothing its sentence says is an invariant. Pages of one document published
together in one edition count as one source, and two facts from one edition about different things
stand as two entries.

- **Change:** new decision
- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-22@dcf291ea · related to WAY-04 · related to WAY-56 ·
  related to WAY-73 · related to WAY-91
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-sentence-count. Level 2 for what one sentence may
  hold — an agent compares the change with the decision:
  - complies: how git matches a path pattern of an attributes file, with the two exceptions its
    page gives, is one fact, and what `git check-attr` prints about a path is left out of it; the
    rules by which git ignores a path, from the page of the same edition, stand as a second entry;
  - violates: the digest SHA-256 gives and the octets UTF-8 uses stand in one entry; "the
    repository declares Python 3.14" is written as a fact.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a fact is reviewed when its source changes, so what changes together has to stand
together and what changes apart has to stand apart. Two publishers, two rhythms of change and two
methods in one entry mean that a new edition of one flags every entry resting on the other; the
facts behind this repository's own invariants glued such pairs in single lines — SHA-256 with
UTF-8, JSON with JSON Lines. An edition of one document is one source, because it changes as a
whole. The count sets how much an entry may hold, not a reason to join: two facts from one page
about different things change for different readers. An invariant written as an environment
fact would never be checked on the commit that breaks it.
*Rejected:* the pattern rule of git and what `git check-attr` reports kept in one entry — the
second is about the tool that runs a method, and changes on no commit whether the sentence holds
(WAY-73); both halves as two facts in *Rests on* — the second holds no condition of the sentence
(WAY-73).
*Consequences:* the facts guard counts sentences, as the invariants guard does, and two facts in
one sentence are left to review. What `git check-attr` reports is no fact: a probe reads the release of the tool it runs on
instead (WAY-91).

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
- **Relations:** derives from WAY-02@3ffcbd46 · related to WAY-42 ·
  related to WAY-59 · related to WAY-77
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-28

*Rationale:* the fingerprint exists to flag what relies on an entry (WAY-02), and what relies on a
fact relies on what it claims and on where the claim holds: read with another range, the same
sentence says something else about a script — `import cgi` passes under 3.12 and fails under 3.13.
The source and its date change at every re-reading and every rebuilt page, and a flag raised by them
would be raised for nothing; a source that really changes fails the watch, which leads to a review
of the fact, and only a human in that review changes the sentence or the range (WAY-82). The passage
quoted word for word is the one anchor the watch compares against at the address, so no digest is
kept beside it.
*Rejected:* the text of the source inside the fingerprint — a rebuilt page flags every dependent,
against WAY-82's rule that a change in a source is not a change of what is true; the sentence alone
— a widened range passes with no signal; a digest of the passage read, kept beside it as a lock file
keeps one — the passage quoted word for word is already the anchor.
*Consequences:* the facts guard computes the fingerprint with the script of `relation-model`. The
sentence names an edition of its source only where the product stands on that edition. A change
to the text of the source next to the quoted passage passes with no signal; that cost is accepted.
Every change of range sends everything resting on the fact to review, since its fingerprint moves
(WAY-31, WAY-90). WAY-31's consequence that left this question to the element is edited in place
to name this decision.

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
paraphrase or a text quoting the source is no source.

- **Change:** new decision
- **Scope:** environment-facts
- **Based on:** a store of sourced statements cites the edition, not the work: "When sourcing
  statements, you should only ever use the edition item of a book" (Wikidata, Help:Sources,
  https://www.wikidata.org/wiki/Help:Sources). A paraphrase drifts from its source: the fact behind
  this repository's invariant `run-record-form` said a line of JSON Lines ends in `\n`, where the
  source says a terminator after the last value is "strongly recommended but not required"
  (https://jsonlines.org/).
- **Relations:** related to WAY-17 · related to WAY-27 · related to WAY-29 · related to WAY-54 ·
  related to WAY-76 · related to WAY-78
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-source-form. Level 2 for what the sentence may say and
  what counts as a source — an agent compares the change with the decision:
  - complies: the fact about JSON Lines quotes "strongly recommended but not required" and its
    sentence says the terminator after the last value may be left out;
  - violates: the sentence says every line ends in `\n`; the source is the model's recollection of
    a page, or a blog post quoting the RFC.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* an edition with its own address does not change under the citation, a passage word
for word lets a re-reading compare two texts instead of a memory, and the date says when that was
true. Of the facts this repository's
invariants wait for, four were written wrongly — three by a paraphrase the passage would have
shown, one on a superseded edition the watch would have caught. An observation is a source when
anyone can run it again. A model's recollection is the commonest source of false facts in an
agent's work, and a text quoting the source carries the same drift.
*Rejected:* a source named by its work alone — a new edition changes what the citation says; a
summary in place of the passage — the drift this decision exists to stop; a fact resting on a whole
section of rules narrowed to the rules the product uses — a pattern outside them would rest on a
rule with no fact; such a section quoted rule by rule — a standing `TODO` in the source.
*Consequences:* a fact without a source is not written, and finding the source is a task. The
template gives the forms of a source: a fact resting on a whole section of rules quotes the
sentence that sets them and names the section by its place, where the edition has an address of
its own, so a summary of the section in the sentence is checked only by reading it in review;
examples a source publishes are a probe's test data, not its source; a further page of the same
edition names its address and place; the archived copy is the closest existing one, since making a
new one writes to someone else's service. The guard checks only the form. The skill that writes
facts checks mechanically, before a human sees one, that the address opens, the passage stands
there and a named package exists.

### WAY-81/1 — How is an environment fact's method written?

A fact's method is a command beginning with the program it runs, the path alone of a
file a human re-reads the source against, or `TODO`; a command probes the behaviour the sentence
states, watches the state its source publishes, or both. A command sets what it can of the
runner's configuration that could change its verdict, and cites each fact it gives a verdict for as
`fact: <identifier>/<version>`, and a run records no verdict for an uncited fact.

- **Change:** new decision
- **Scope:** environment-facts, gate, invariants
- **Based on:** git sets a setting of its own that changes how it matches paths: "git-clone[1] or
  git-init[1] will probe and set core.ignoreCase true if appropriate" (git-config,
  https://git-scm.com/docs/git-config); observed: `git check-attr` with and without
  `-c core.ignorecase=false`, on a pattern with a capital letter in a fresh repository, on git
  2.55.0, Windows — the path was assigned differently; run 2026-09-26.
- **Relations:** derives from WAY-61@4804d070 · related to WAY-08 · related to WAY-38 ·
  related to WAY-63 · related to WAY-65 · related to WAY-73 · related to WAY-74 ·
  related to WAY-91
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-method-form · fact-citation-target ·
  fact-verdict-citation. Level 2 for what a command asks and what it sets — an agent compares the
  change with the decision:
  - complies: the fact on path patterns runs `git -c core.ignorecase=false check-attr` on patterns
    the page's rules decide; the fact on SHA-256 probes the digests NIST publishes for it; the fact
    on JSON watches `obsoleted_by` of its RFC and that its passage still stands;
  - violates: a probe asks `git --version` and compares the number in place of the behaviour; a probe relies on the git
    configuration of the machine it runs on.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* the forms are those WAY-61 gives an invariant, so the gate and a person read both
alike. A probe asks about the behaviour, because a version number says
nothing about what the named release does. A watch reads what the source publishes as data —
`obsoleted_by` of an RFC, a model's state, a support schedule — and whether the passage still
stands. A person re-reads what no command can read. The environment that runs a method changes how faithfully it reads the world, not what
is true: git matches differently when the machine ignores case. So the command makes that
environment irrelevant, and a fact about what runs a method is no fact an invariant rests on.
*Rejected:* a kind of method named beside it — the form already says it (WAY-54, WAY-61); a probe asking for a version number in place of the behaviour — it trusts the label; the runner's configuration
recorded as a fact in *Rests on* — it changes the method's fidelity, not the sentence's truth.
*Consequences:* a command whose program is not yet declared or produced is written out in full all
the same and is unchecked for that reason, and a fact with no verdict for any other reason results
`error`, as WAY-63 has it. Where the environment cannot be made irrelevant — a model that runs a
method — it is configuration read off the product (WAY-54), while the release of a tool a probe runs is
read off the machine (WAY-91), and the deliberate break shows the
method's fidelity, which holds only where the break gives high confidence of detection. A command
records its verdicts under the key `fact` (WAY-74). WAY-73's rationale is edited in place to name
this decision. Where the checks of a product's facts stand in the part map is set when its first
fact is written; this repository's stand in `probes/`, outside every directory whose tests run as a
suite.

### WAY-82/1 — When does an environment fact's method run, and what fails its watch?

A fact's method runs on every change that enters or rewords its entry or alters a file its command
names, and by the clock, run on the main branch, which records each verdict and exits non-zero on
a `fail` or an `error`. Elsewhere a fact's `fail` stops no change; a watch fails on a published
change to its edition or when its passage no longer stands, and an announced revision fails nothing.

- **Change:** new decision
- **Scope:** environment-facts, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-60@c85d1ac0
- **Verification:** level 1 — invariants: gate-fact-run · fact-clock-exit · gate-exit-code. Level 2
  for what fails a watch — an agent compares the change with the decision:
  - complies: RFC 8259 gaining `obsoleted_by` fails the watch of the fact citing it; NIST's notice
    that it will revise FIPS 180-4 fails nothing; the passage quoted from jsonlines.org vanishing
    from the page fails its watch;
  - violates: a change touching no fact fails the gate on a fact's `fail`; the clock exits zero
    while a fact results `fail`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-29

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
- **Relations:** derives from WAY-63@f16348c8 · related to WAY-08 · related to WAY-10 ·
  related to WAY-14 · related to WAY-57 · related to WAY-61 · related to WAY-68 · related to WAY-79 ·
  related to WAY-81
- **Outranks:** none
- **Verification:** level 1 — invariants: human-verdict-invariant-row · human-verdict-fact-row ·
  gate-human-verdict.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a method that is a path gives no result until a person assesses the product or
re-reads the source (WAY-61, WAY-81), and WAY-63 says what a verdict names; it lacks a place the gate
can read. A row in the repository is visible, fixed like any other line, and read by the guards
that know the entries. One file serves both elements, because the two verdicts differ only in when
they lapse: an invariant's when the product changes under it, a fact's when the world may have
changed, which only a date can stand for. A row counts only for the current version, so a new
meaning is never excused by an old verdict. The gate compares the date with the commit it checks,
as a quarantine does (WAY-68), so that its verdict follows the commit; the clock runs against the
world, so it compares with the day. The first case waits already: who can open this repository can
be read only with the credentials of whoever sets it.
*Rejected:* the verdict in a commit message — invisible to a reader of the foundation, never
fixed, and its author is often an agent; waiting for a second case — the rule on verdicts with
a date would stay dead.
*Consequences:* both templates name the file and give its row as
`| Entry | Version | Verdict | By | On | Commit | Until |`; the invariants template's place that waits
for this decision is rewritten to follow it, and WAY-63's consequence on how long a verdict is in force
moves here. The file is written by hand and is no element's entries, so the invariant
`foundation-file-kinds` names files an element's template names. The guards check a row's form and
that the entry exists; the gate reads the row. The part that holds the file, so that a change to it
reaches both row invariants, is set with the first verdict written.

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
names the catalogue, its edition, the level or list taken and the area of the product. A binding
rule — a law, a contract, a licence — needs no adoption: whether it applies is a fact, read as
applying until a human settles otherwise. An agent that notices a likeness to a requirement nothing
has adopted or applied asks a human.

- **Change:** new decision
- **Scope:** environment-facts, decisions, invariants
- **Based on:** a binding standard starts from inclusion: "the best practice approach is to start
  with the assumption that everything is in scope until verified otherwise" (PCI Security Standards
  Council, Information Supplement: Guidance for PCI DSS Scoping and Network Segmentation, v1.1, May
  2017,
  https://listings.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1_1.pdf).
- **Relations:** related to WAY-04 · related to WAY-17 · related to WAY-58 · related to WAY-73 ·
  related to WAY-76
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a product adopts WCAG in a decision naming the edition, level AA and the screens it
    covers, and an invariant taking a criterion's condition names that requirement as a fact in
    *Rests on*; the licence of a product's icons stands as a fact that it applies;
  - violates: an agent writes an invariant from an ASVS requirement because the code looks like
    it, with no adopting decision; a licence is left out because nobody adopted it.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a voluntary catalogue binds only because someone chose it, so the choice is a
decision with its scope, and without one an agent would bind the product to whatever it recognised.
A law or a licence binds whether anyone chose it, so the only open question is whether it applies,
and reading it as applying until settled makes silence raise checks rather than remove them. A
descriptive source — an RFC, a list of modules — needs nothing beyond the fact. A likeness goes to
a human as "do we adopt this?" or "does this bind us?", because only a human knows what the product
means to take on.
*Rejected:* a field naming the kind of source, and a script checking that every requirement of an
adopted catalogue has a fact and an invariant, now — neither has a reader until a product adopts a
catalogue or takes on a binding obligation (WAY-05); a fact that nothing names is caught by WAY-73
already.
*Consequences:* a requirement of an adopted catalogue is a fact whose source is the edition, the
requirement's identifier and its text word for word, and an invariant taking a condition from it
names it in *Rests on* (WAY-73); WAY-58's consequence that left this to the element is edited in
place to name this decision. The field and the script are built on the first product that adopts a
catalogue or a binding obligation; the first in reach is the CC BY licence of the icons of the game
`loop`.

### WAY-89/1 — Which version of Python do the scripts of the-way run on, and when does it move?

The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and
the declared version moves when the version in use leaves bugfix support, never because a newer
version comes out.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, gate,
  repository, task-cycle
- **Based on:** Python 3.14 has a date for its last regular bugfix release: "3.14.14: Tuesday,
  2027-10-05 (Final regular bugfix release with binary installers)" (PEP 745,
  https://peps.python.org/pep-0745/); observed: the table of versions of the Python Developer's
  Guide (https://devguide.python.org/versions/) gives 3.14 the status "bugfix" and the end of life
  2030-10; read 2026-09-26.
- **Relations:** related to WAY-34 · related to WAY-38 · related to WAY-77 · related to WAY-81
- **Outranks:** none
- **Verification:** level 1 — invariants: python-version-declared · script-imports.
- **Review when:** the status of Python 3.14 in the table of versions of the Python Developer's
  Guide no longer reads "bugfix" · check by: 2027-10-05
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* one version, declared, rather than a floor, because a floor gives a script's verdict
per interpreter: `import cgi` passes under 3.12 and fails under 3.13, a version "3.12 or later"
promised. The version moves when the one in use leaves bugfix support, not when a newer one is
released, which changes nothing here. Past the end of bugfix support no binary installers are
released, which hurts a new machine or CI, so the move comes before the end of security support.
Versions out of support are no target, as the-way does not aim at legacy systems.
*Rejected:* the newest release, unnamed — the verdict would depend on the date; "3.12 or later"
with an invariant for every version it admits — a fact and a verdict for each version; 3.12 alone
— a version already past its bugfix support; a move whenever a newer release comes out — a yearly
review nothing here needs; a move at the end of security support, about 2030.
*Consequences:* a product's CI provides Python 3.14 to run the scripts of the-way it pins (WAY-34),
and the-way's own commands run on this interpreter. A move changes the declaration and the version
of the fact on the standard library, and sends the invariants naming the version to review; it may
cross several versions at once, and the modules removed on the way add up — for the standard
library that is one run of the fact's method and one list of imports. `.python-version` joins the files of the
`repository` part.

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

### WAY-91/1 — On which release of its tool does a probe's verdict count?

Where a fact's *Holds for* names a release of the tool its probe runs, the probe reads the release
it runs on and records it in the `description` of its line. A `fail` on any release is a `fail`; a
`pass` counts only on a release *Holds for* names, a build of it included, and on another the fact
is `unchecked`.

- **Change:** new decision
- **Scope:** environment-facts, gate
- **Based on:** none
- **Relations:** related to WAY-63 · related to WAY-73 · related to WAY-74 · related to WAY-76 ·
  related to WAY-77 · related to WAY-81 · related to WAY-82 · related to WAY-89
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the probe of the fact about git 2.55.0, run on git 2.56.0, writes `git 2.56.0` in the
    description of its line, fails the fact where the behaviour differs and leaves it `unchecked`
    where it agrees; on Git for Windows 2.55.0.windows.3, a build of git 2.55.0, its pass counts;
    the probe of the fact on SHA-256, whose *Holds for* names an edition of a standard and no
    release of a tool, reads no release;
  - violates: the probe passes the fact on git 2.56.0; it skips on another release without asking
    about the behaviour; it writes the release under a key of its own beside `description`.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a fact names a release, while the machine holds whichever release it was last updated
to, and the product runs on that one. A failure there says the tool the product depends on behaves
otherwise than the fact, which is worth a review whether the world moved or the machine left the
fact's range. A pass there says nothing about the release the fact names. The release read is no
fact an invariant rests on (WAY-73): it decides whether a verdict counts, not what is true. It goes
in `description`, where the human reviewing a `fail` or an `unchecked` reads it; WAY-74 keeps tool
versions out of the keys of a line, which nothing would read.
*Rejected:* leaving the question until the first probe is written — it would come back to a human
in another session, without the reasons; a fact about the tool's release beside the method — it
changes the method's fidelity, not the sentence's truth (WAY-73, WAY-81); a pass counted on any
release — the fact about one release would pass on another it says nothing about.
*Consequences:* WAY-63 is edited in place so that its closed list of reasons for `unchecked`
gains, for a fact, "a probe ran on a release of its tool outside *Holds for*", and the facts
template's pending question on a method resting on the tool that runs it is closed: a method rests
on no fact about that release. The clock's report names each fact left `unchecked` for this reason,
and the skill writing facts takes such a fact as a case to move to the release the machine runs.
Moving it changes *Holds for*, so the fact's version rises and every invariant naming it gets a new
fingerprint in *Rests on*: for git, eight invariants after each update of git that the fact is
moved to.

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
- **Relations:** narrows WAY-02@3ffcbd46 · derives from WAY-04@f07bb569
- **Verification:** level 1 — invariants: glossary-entry-field-presence · glossary-entry-field-words.
  Level 2 for the binding part — an agent compares the change with the decision:
  - complies: an invariant's sentence uses "verdict" with no fingerprint, and a changed definition of
    "verdict" lists it for review;
  - violates: a sentence cites the term as `verdict@<fingerprint>`; a changed *Avoid* is treated as a
    change to the entry's binding part.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-27

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
- **Based on:** a definition carries no requirement: "A definition shall not take the form of, or
  contain, a requirement" (ISO/IEC Directives, Part 2, eighth edition, 16.5.6,
  https://metanorma.github.io/mn-samples-iso/documents/directives/part2/document.html).
- **Relations:** related to WAY-05 · related to WAY-22 · related to WAY-63 · related to WAY-94 ·
  related to WAY-97
- **Outranks:** none
- **Verification:** level 1 — invariants: glossary-definition-count · glossary-definition-words.
  Level 2 for the shape, the rule and neighbouring terms — a definition carries a rule when it holds
  something the decision or invariant setting it could change while the word went on naming the same
  thing; an agent compares the change with the decision:
  - complies: "The panel is the group of agents that assesses a change", with which changes, how many
    agents and who decides left to WAY-10; "A result is the value reported for an entry on one
    commit: the verdict that counts for it there, or …";
  - violates: "The panel is the three agents that assess a change…", with the number WAY-10 sets;
    "The binding part is the part of an entry that…", its genus the word the part map uses for a
    part; the definitions of verdict and result each standing alone.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-27

*Rationale:* the foundation binds with sentences (WAY-05, WAY-56), and a definition counted as one
sentence lets the same count serve every guard. A genus places the word among things the reader
knows, and a genus that is itself a term in another meaning puts the homonym back into the
definition. A rule inside a definition changes the definition whenever the rule moves, and sends the
review of uses after what is a change of a decision; asking what the decision setting a rule could
change while the word still names the same thing tells the two apart. Neighbouring terms are kept apart only where one definition says how
they differ: a rationale calling `unchecked` a missing verdict contradicts the record of a run,
which lists it as one (WAY-74).
*Rejected:* a phrase that replaces the term, without an article or a full stop — the guard would count
something other than sentences; a test sorting by a number, a date or a list — a place or a party
passes it, as "run on the main branch" did for the clock; the definition put in place of the word in
the sentence that sets the rule — a definition says what the thing does, that sentence repeats it,
and the test failed this decision's own panel; a field naming neighbouring terms — the definitions
carry it.
*Consequences:* the shape is checked by review, the count and the words by the guard. The normative
words kept out of a definition are *must* and *must not* besides the words the decision template
keeps out of binding sentences.

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
- **Relations:** narrows WAY-02@3ffcbd46 · narrows WAY-60@c85d1ac0
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
