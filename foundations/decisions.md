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
test that carries no record of its independent assessment (WAY-10). A task that needs an invariant
test changed goes back to the foundation step.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** impossiblebench-test-modification@9cdba560
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: foundation-change-assessment-record.
- **Review when:** no model in the range of fact impossiblebench-test-modification is Active in
  Anthropic's table of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

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
`installation/`, `agent-instructions/`, `instruction-files/`, `project-level/` and `task-cycle/`
— with `probes/` as a second directory of the environment facts part, for the checks of
the-way's own facts, the files that configure the whole repository, which its part map gives to the
`repository` part (WAY-44), the root agent instruction files and the project skill entry points
under `.claude/skills/` and `.agents/skills/`, which the map gives to `agent-instructions`
(WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch
only once it holds what its part requires: an element its template and rules, examples or a
pointer to entries of the-way that serve as its examples, a skill that writes its entries and a
format guard; `elements/common/` the rules of form and the way of working the elements'
templates and skills share, the code their format guards share and the skills that find entries
and that critique proposals and assess changes; `project-level/` the templates of a project
definition, a project plan and a task document, the skills that write them and lead a
handed-over plan, the readiness check, the plan check, the reader of task-cycle evidence for plan
states and their tests; `relation-model/` the script that computes fingerprints; `gate/` the
test of every critical flow in the part map; `installation/` the installer, its tests and a
README explaining how a product uses the pinned version; `agent-instructions/` the instructions
for agents working on this repository, led to from the root agent instruction files;
`instruction-files/` the principles of instruction files for coding agents, the account of how
the tools load them, the skill that applies them, and the script that checks instruction files
with its tests; `task-cycle/` what the design of the task cycle sets, and until then it does not
reach the main branch. The entries in `foundations/` are checked by the format guards of their
elements.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  relation-model, gate, installation, agent-instructions, instruction-files, repository,
  project-level, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: repository-file-location · element-directory-contents ·
  relation-model-directory-contents · invariant-example-target · map-example-target ·
  glossary-example-target. Level 2 for what `elements/common/`, `installation/`,
  `agent-instructions/`, `instruction-files/`, `project-level/` and `task-cycle/` hold and for the
  format guards checking `foundations/` — an agent compares the change with the decision:
  - complies: code two format guards share moves into `elements/common/`, and both load it from
    there; a new file of entries in `foundations/` comes with the format guard of its element; the
    installer, its tests and instructions stand together in `installation/`; the templates of a
    definition, a plan and a task document, the skills that write them and the checks of a
    definition and a plan stand in `project-level/`; the agent instructions
    have their own part and root entry points; the project skill entry points under
    `.claude/skills/` and `.agents/skills/` stand at the root as files of `agent-instructions`, and
    the script that generates them stands with its test in `agent-instructions/`; the principles,
    the loading account, the skill and the check script of instruction files stand together in
    `instruction-files/`;
  - violates: a `tools/` directory for shared scripts reaches the main branch; `task-cycle/`
    reaches the main branch before the design of the task cycle sets what it holds.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* anything brought in on the side makes the repository a store of material; directories
follow the parts, so a change's files name its part and decisions (WAY-21); an incomplete directory
is work in progress, kept on a branch (WAY-01); probes stand apart, so an element's tests run no
fact's method; product installation and agent instructions have different failures from repository
configuration; the project definition and task cycle answer different questions; the principles of
instruction files serve any repository, so they stand apart from this repository's own agent
instructions.
*Rejected:* material merged as soon as it is written — a store from the first day; an element whose
only tool is a skill — the form holds only while someone remembers to run it; one `tools/`
directory for everything shared — it matches no part and grows into a store; one set of template,
skill and script for every directory — a script that only reads has nothing for a skill to write;
the files serving the whole repository left out of the map on purpose — they lose their part and
its failure mode; installation or agent instructions folded into repository configuration — their
failures lose their own parts; the principles of instruction files folded into this repository's
own agent instructions — that part answers for the-way's own instructions, and its failures differ.

### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation is assessed by one independent agent, on a model
other than its author's where one is available, which sees the diff and the files of the commit it
assesses without the task's chronicle or the author's reasoning and names what of the change can be
cut, or that nothing can. The author settles each of its remarks and records how, and a settlement
that changes the assessed foundation entries or invariant tests is part of the assessed change and
does not reopen its assessment. A human accepts the change, with the assessment and its settlement,
when merging it.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  task-cycle
- **Based on:** llm-self-preference@6d9f4b97
- **Relations:** derives from WAY-03@7c2d4ca1
- **Verification:** level 1 — invariants: foundation-change-assessment-record. Level 2 — an agent
  compares the change with the decision:
  - complies: one assessor on another model reads the diff without the author's reasoning, and the
    author records how each remark was settled before the merge; a settlement that rewrites an
    assessed invariant test is recorded beside the one assessment;
  - violates: the assessor receives the author's reasoning; the author drops a remark without
    recording why; a change merges with no assessment record; the edits of a settlement are sent
    to a second assessment.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/5

*Rationale:* the problem is a single executor that checks itself: agents on one model with one input
share its blind spots, so independence comes from another model and from not seeing the author's
reasoning; one such reader finds what a reader can, and the human who accepts at the merge reads the
change with the assessment beside it. The finding it cites measured models of other publishers only,
and this decision takes it across publishers (WAY-85).
*Rejected:* a panel of two assessors and a settler reading both orders — its cost per change
outweighs what one independent reader misses, and its uncertainty becomes questions for the human;
the author assessing its own change — it checks itself; assessing again every settlement that
changes the assessed entries or tests — each correction draws new remarks, and the change reaches
the human only after a chain of assessments.

### WAY-11/1 — How does a task end?

A task ends with its return step before its branch is merged: an agent searches the diff and the
task's log for new rules and decisions, code behaviour with no invariant over it, environment
facts the change rests on that the foundation does not yet hold and words whose use the glossary
does not yet settle, writes the resulting foundation entries in the same change, which its
independent assessment covers (WAY-10), and compares the foundation with the code in the parts
the task touched. Uncovered code behaviour becomes an invariant when changing it in a later task
would violate a requirement or a settled rule of the product; an implementation detail that can
change without such a violation stays in ordinary tests and the description of the change, and
this distinction leaves decision-derived invariants (WAY-12, WAY-22), accepted settlements
(WAY-134) and the task's duties for projected entries (WAY-126) required. A periodic review of the
foundation runs apart from tasks.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step
  finds and how it classifies uncovered behaviour — an agent compares the diff, the task's log
  and sources with the decision:
  - complies: a newly found rule that a later change would break becomes an invariant, with its
    requirement or settlement named; a replaceable layout calculation stays in ordinary tests
    and the change description, with the reason recorded; an invariant required by a decision
    is written even when its check costs work; accepted settlements and applicable projected
    entries are written;
  - violates: a product rule is left only in ordinary tests; every replaceable detail becomes
    a foundation invariant merely because the diff reveals it; a costly decision-derived
    invariant or an applicable accepted or projected entry is omitted under the distinction.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/17

*Rationale:* some of the foundation is learned only in implementation and in use, and a task that
missed the foundation does not report it; an end step goes missing, so the merge waits for its
record. Facts and words are listed because, like rules, they are learned in code.
*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
in the code; every uncovered detail made an invariant — a replaceable implementation becomes a
product rule; ordinary tests alone for product rules — later work can change a requirement without
meeting a foundation check.

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

What a task touches, never its size, sets the path that merges its change and how sharply that
change is checked: an agent's analysis at the start of the task settles whether it changes the
foundation, which chooses among the paths that merge a change, while three things set how sharply
it is checked — the criticality of the parts it touches, as the part map computes it, whether it
touches the files of a trust boundary, and whether the change can be undone. Paths that merge a
change differ in their steps, never in the outcome a task has to reach, and only a human sets a
task to return knowledge instead of a change, which merges nothing. A task's size may lighten
how its change is prepared and made — its plan and the number of agents making it — never the
outcome it has to reach or the checks run on the finished change, and otherwise serves only as a
signal to split it; an agent may check a change more sharply than the map computes, never less, and
a human decides on every change that cannot be undone.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
    a human's decision; a change one agent can hold, including its foundation entries, is made without a
    plan and runs the same checks as any change to the parts it touches;
  - violates: a task takes the path for changes that leave the foundation unchanged because it
    changes few lines; a small task skips a check that the parts it touches call for; a change that
    cannot be undone reaches the main branch without a human's decision; an agent turns a task into
    one that returns knowledge instead of a change without a human setting it so.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* size misleads both ways about what can go wrong: a rename across many files is easy to
undo, a one-line change to a stored format can destroy every user's data, so what a task touches,
never its size, sets its path and its checks. Size does tell how much preparation a change needs: a
small change can be made without a plan, while the checks on the finished change stay whole and a
human still decides on what cannot be undone.
Paths differ only in steps, because a weaker outcome would bypass the process; returning knowledge
alters what a task delivers, so a human sets it.
*Rejected:* one cycle for all tasks — how much process a task needs depends on what can go wrong;
the path chosen by size — size misleads; a human approving every diff (DORA) — no fewer failed
changes, and attention spent where it adds nothing; keeping a change that cannot be undone, or one
touching a trust boundary's files, from the lighter preparation — it would take the lighter
preparation from small tasks it suits, while a human's decision and checks kept whole already
stop such a change.

### WAY-14/1 — Who approves a version of a decision?

A version of a decision is approved by a human, never by an agent, and records who approved it and
either when, or the merge of the request by which they accepted it; in the-way, the approver is
Mariusz.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: decision-approval-record · decision-approver.
- **Review when:** the-way decides which of its elements a team may adapt, and with it who approves
  decisions for which parts · check by: 2026-12-31
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* the record of who approved, and when or by which merge, is what a human considering a
change reads, and what WAY-07 needs when an entry has to be accepted again.
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
entry instead of being pointed to. The one exception is the place of its tasks, named in the
`## Backlog` section of its root `AGENTS.md` and nowhere else.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  installation, agent-instructions, instruction-files, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: outbound-link-reach. Level 2 for the reasoning in the
  entry — an agent compares the change with the decision:
  - complies: a decision quotes a public study with its address; a pattern seen in a product
    outside the repository is described in the rationale, without a pointer to it; the-way's root
    `AGENTS.md` names, in `## Backlog`, the private note where its tasks are kept;
  - violates: *Origin* points to a private note; a rationale rests on "as in our other product"
    without saying what was seen.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/8

*Rationale:* a pointer to a source the reader cannot open is a dead end, leaving a claim nobody
can check; what was seen there, written down, can at least be judged, and WAY-17 still has a fact
to name. A backlog place is where work is kept, not reasoning an entry rests on, and WAY-107 sends
an agent there; named in that one section, it stays a place to find work and never becomes a
source an entry points to.
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
knows them, or written as `unknown`. A rationale an agent proposes for a human's decision goes to
the human as a question, never into the entry; the rationale of a decision an agent takes in a task
is the agent's to write.

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
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* a reason an agent writes looks exactly like a recorded one, and later readers take it
for the reason the decision was made; a human who knows it is a source, a guess is not. The cited
study compared generated arguments with expert rationale after giving models the problem and
decision; it did not test recovery from code, and argument overlap is not a correctness rate. This
decision takes its warning across model publishers (WAY-85). A recorded search is not repeated,
and `unknown` shows nobody knows what the decision guards.
*Rejected:* an agent's rationale in the entry — read as the reason the decision was made; rejected
options filled in as `none considered` — nobody knows what was considered.

### WAY-30/1 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan, or into its task
document where no plan is written, and approved with that plan or document by the decision's
approver before the code that needs it is made. When a contradiction shows only during
implementation, the agent stops, quotes the decision by its number, and either brings the change into line, drops the change, or
proposes on the task branch a new wording or a narrowing of the decision — by a new version on the
main branch, by an edit before it — and the code that needs it waits for the decision's approver. An
exception written in advance into a decision's binding sentences is not a contradiction, and no
exception lives only in a task document, plan or cycle record.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task branch whose code goes against a decision carries a proposed narrowing, and
    the merge waits for its approver; a task without a plan carries the known decision revision
    in its task document, accepted by the decision's approver before dependent code;
  - violates: a task branch whose code contradicts a decision that stays unchanged; a task's plan
    that records a "justified violation" of a decision; a task without a plan treats the
    orchestrator's go-ahead as approval of a decision revision.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* an exception kept only with the work leaves the foundation describing what the code no
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
  installation, instruction-files, task-cycle
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
between two states — stays in the plan of that work, or in the choices of its cycle record
where no plan is written.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "the foundation reaches the main branch whole, once every element is ready" stays in
    the plan of building the foundation; "when what entries wait for arrives, they are fixed in
    the same change" enters the log; an exclusion that ends with a task without a plan stays
    in the choices of its cycle record;
  - violates: a decision on the order in which elements are built; a decision whose binding
    sentences say what happens until the first merge; an exclusion that ends with its task
    written into the log as a product non-goal.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

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
  installation, instruction-files, task-cycle
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
raising a part's criticality needs no reason, and lowering it is accepted by the human accepting the
change at the merge, with the lowered criticality in front of them.

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
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

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
assesses.

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

An invariant entry carries a version number, starting at 1, and holds only its current wording, and
earlier wordings are read from git. When the entry's fingerprint differs from its fingerprint on the
commit the task branch left the main branch from, its version is one higher than there, unless the
entry declares a correction naming both fingerprints and the human who accepts the change at the
merge (WAY-10) confirms, with the old and the new binding part in front of them, that the meaning is
unchanged; a change after which some test citing the entry would need a different expected value is
never a correction; when the fingerprint does not differ, the entry keeps the version it has there.
A check cites its invariant by identifier and version, in the form the template gives, and fails the
gate when that version is not the current one, while elsewhere a reference to an invariant's version
is historical and never flagged, as WAY-02 has it.

- **Change:** new decision
- **Scope:** invariants, relation-model, gate, task-cycle, part-map, elements-common
- **Based on:** none
- **Relations:** derives from WAY-03@7c2d4ca1 · derives from WAY-10@db68de1c ·
  narrows WAY-02@3ffcbd46
- **Verification:** level 1 — invariants: invariant-version-number · invariant-version-new ·
  invariant-version-changed · invariant-version-unchanged · invariant-earlier-wording ·
  invariant-citation-version · invariant-correction-confirmation. Level 2 for what counts as a
  correction — an agent compares the change with the decision:
  - complies: a typo fixed under a declaration the accepting human confirms, with no test citation
    changed; "at most three" becoming "at most four" raises the version, and the old citation
    fails until the test is rechecked;
  - violates: "must" becomes "may" under a confirmed correction; a heading's code literal fixed
    under a declaration, though a test asserting it would need a new expected value; a script
    moves every citation to a new version, nobody checking the tests.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* a read-only test cited by fingerprint would move with every typo, and by bare
identifier never, checking a meaning gone; a version moves with meaning; the human who accepts the
change at the merge confirms a correction, so no author-named kind silences anything; a forgotten
raise drifts silently, a needless one fails loudly.
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
fails there on a deliberate break, and the human accepting the change at the merge sets the row with
that report in front of them.

- **Change:** new decision
- **Scope:** invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-28@94d8ef12 · derives from WAY-22@dcf291ea ·
  derives from WAY-17@b1e26133
- **Verification:** level 1 — invariants: invariant-recovered-form · invariant-recovered-derived ·
  gate-fork-point-evidence. Level 3 for the row — the human accepting the change at the merge sets
  it with the gate's report in front of them, and the record of that decision names who and when.
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
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

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
  derives from WAY-54@57b93cf6 · derives from WAY-57@89a75ebe · derives from WAY-38@6e10c3fd ·
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
  derives from WAY-57@89a75ebe
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
- **Relations:** derives from WAY-03@7c2d4ca1 · derives from WAY-17@b1e26133 ·
  derives from WAY-57@89a75ebe · derives from WAY-61@4804d070
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
  - complies: a save-load test fails, then passes, on one commit; the independent assessment accepts
    waiting for the load signal;
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

An invariant's sentence, the check that cites it and the code it covers come from three different
agents, and the deliberate break the check is accepted on is written from the sentence by the
reviewer of that code, who did not write the check. A check that cites an invariant takes the input
it asserts on and the value it expects written out, wherever the code its invariant is about would
otherwise compute either; only the side it compares against comes from the run.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate, task-cycle, relation-model
- **Based on:** visible-scoring-reward-hacking@39a85ced · oracle-in-loop-building@d13c8e26
- **Relations:** derives from WAY-08@2343e09f
- **Verification:** level 3 for who writes what — the human accepting the change at the merge
  assesses how the work was handed out, from the record that names who wrote what. Level 2 for what
  a check computes — an agent compares the change with the decision:
  - complies: a guard's test carries its expected wording and fingerprint as literals, so a longer
    fingerprint fails it;
  - violates: a test builds its reference by calling the code its invariant is about, and expects
    that call's message; a test reads the value it expects, at run time, from the file its
    invariant is about.
- **Review when:** no model in the range of fact oracle-in-loop-building is Active in Anthropic's
  table of models · check by: 2026-10-02
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* a break chosen by a check's author aims at what the check does, not what the sentence
says, a check by the sentence's author inherits its reading, and a check by the code's author is
fitted to the code; two sides computed by one code move together, and the test stays green unseen.
The reviewer already reads the check without having written it, so the break needs no agent of its
own. This takes the visible-scoring finding across publishers (WAY-85).
*Rejected:* hiding checks from the executor — it costs honest work; one agent writing all three
under a written rule — prose stops nothing; a field naming the writers — nothing reads it; the
expected value alone written out — the input still moves with the code; a `data:` line naming each
file a verdict leans on — every tracked file turns read-only; a separate agent for the deliberate
break — the code review already stands apart from the check.

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
  installation, instruction-files, repository, task-cycle
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
the rules of an element's template or of the part the elements share, and at least one of its uses
in the files of `foundations/`, the elements' templates and the part the elements share carries a
meaning a reader who knows the product's field would not give it; an agent finds the candidates and
writes the entries, and a human accepts their meaning (WAY-114). A word's definition stands in the
glossary alone, and a closed list of values a guard reads stays in its template with what each value
means. The glossary of the-way holds the words of the process, and a product's glossary holds the
words of its domain; a product takes the words of the process from the-way at the commit it pins and
defines none of them again, and in the-way, whose product is the process, the two are one file.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: glossary-term-use · glossary-process-terms. Level 2 for
  which words take an entry, where a definition stands and which glossary holds it — two uses carry
  two meanings when a definition true of one is false of the other, a noun naming one occurrence of
  what its verb does, or what does it, carries the verb's meaning, a word naming what a kind of
  entry records names the entry that records it too, and a word naming what a rule computes keeps
  the meaning a reader of the field gives it; an agent compares the change with the decision:
  - complies: "clock", used for a command and for a deadline, takes an entry with one meaning;
    "digest", used only as SHA-256 uses it, takes none; "run", used for running a command and for
    text running across lines, takes none; "critical flow" names the flow and its entry of the part
    map with one meaning; "criticality", computed for a part by a rule of the part map, takes none;
    the kinds of change of a decision stay defined in the decision template; a word used plainly and
    for a term becomes the term or has its other uses rewritten; a game's glossary
    defines "level" and uses "verdict" as the glossary of the-way defines it at the pinned commit;
  - violates: every noun of the decision log takes an entry; a decision defines a term in its
    binding sentence while the glossary holds another definition; the glossary defines "criticality"
    by the rule that computes it; a word takes an entry for its plain meaning only, to hold its
    *Not*; a game's glossary gives "verdict" a definition of its own; the glossary of the-way
    defines "level" as the game uses it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* a glossary of every relevant word grows without bound, kept by memory, while a word
used as the field uses it needs no entry. A definition stands once because copies drift, between
products too; a closed list's values mean the rule their guard applies, so they stay beside it.
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
  - complies: "The assessor is the agent that assesses a change", the rest left to WAY-10;
    the definition of result names its neighbour: "the verdict that counts for it there, or …";
  - violates: "The assessor is the agent on another model that assesses a change…", with the
    model rule WAY-10 sets;
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
not hold enters such a sentence only where the request names it for the human who accepts the change
at the merge. A glossary entry carries no version and is edited in place, and every change to a
definition goes, in the same change, through a review in which an agent puts the new definition in
place of the word in every use the guard lists and every other form it finds, and reports each use
whose meaning moves to the human accepting the change at the merge. A term used by an entry on the
main branch keeps its meaning, and a new meaning takes a new word.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts, elements-common
- **Based on:** none
- **Relations:** narrows WAY-02@3ffcbd46 · narrows WAY-60@6e862c88
- **Verification:** level 1 — invariants: glossary-entry-version · glossary-definition-uses. Level 2
  for the review, a new meaning and a paraphrase — an agent compares the change with the decision:
  - complies: the definition of "verdict" is reworded, the guard lists its uses, and the agent
    reports that none moves; after the main branch, a second sense of "gate" takes a new word; "The
    clock exits non-zero when some fact's result is `fail` or `error`";
  - violates: a definition is reworded as a mere fix and no uses are looked at; after the main
    branch "verdict" widens under an invariant's unchanged sentence and version; "The command that,
    unlike the gate, runs checks apart from any change exits non-zero when …", spelling out "clock".
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

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
new label. The word is the human's choice, accepted at the merge (WAY-10).
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

A word of a product's domain that the glossary of the-way holds at the commit the product pins, or
the last word of a term it holds, in any of its forms, is written in the files of the product's
`foundations/` with a qualifier — a phrase holding the word — and the bare word keeps there the
meaning of the process; the qualified word takes a glossary entry only where WAY-95 gives a word
one, and where the bare word itself has an entry in the glossary of the-way, that entry records no
*Not* for its domain meaning. The *Avoid*
of an entry of the product's glossary holds such a word only with a qualifier. The product's code,
its interface and talk about the product use the word of the domain unchanged.

- **Change:** new decision
- **Scope:** glossary, decisions, invariants, part-map, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-95@455377de · derives from WAY-98@94371030 ·
  narrows WAY-99@7d44dfd7
- **Verification:** level 1 — invariants: glossary-process-terms. Level 2 for how the sentences of
  a product's foundation, its code and its interface write the word — an agent compares the change
  with the decision:
  - complies: a game's invariants say "game clock" for the timer of a match, and a factory's say
    "assembly step" for an operation, while their code and interfaces use `Clock` and "Step";
    a game's glossary entry "game clock" lists "match clock" in *Avoid*;
  - violates: a game's invariant says "clock" for the timer of a match or a factory's says "step"
    for an operation; a game's glossary defines "clock" as the timer of a match, or an entry
    "lab result" lists "fact", the last word of "environment fact", in *Avoid*.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* a word of the process written bare in a product's foundation for something of its
domain carries two meanings for an agent that reads the-way's rules beside the product's, and a
qualifier keeps each word in one meaning where the rules are read; the people who build and use the
product keep the words of its domain, since the rule protects the reading of the foundation alone.
A product cannot edit the glossary of the-way, so the *Not* that WAY-99 asks of the word's entry has
nowhere to stand, and a phrase holding the word, which WAY-99 refuses as a carrier, here keeps the
word of the field recognizable. A term's last word can stand for the process term in short form, so
the qualifier also keeps a domain use of that word apart. A word of *Avoid* counts as an error at
every use WAY-98 counts, whatever meaning the use carries, so the bare word in a product's *Avoid*
would bar the meaning of
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
no count tells one meaning of a word from another; qualifying a domain word only when it is a whole
process term — a short use of a multiword term can still collide with the domain meaning.

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

### WAY-106/1 — What does the project level write before tasks exist?

The project level reads a product's foundation and records prospective changes in the project
definition; it writes no foundation entries. The definition holds the project's settled scope and
projected foundation entries, while the project plan holds phases, task order and which task
realizes or writes each projected entry.

- **Change:** new decision
- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a definition projects a new decision and the plan later assigns a task to write it;
  - violates: the definition writes the future decision into the product's foundation, or assigns
    projected entries to tasks before the breakdown has made those tasks.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* the foundation describes what the product holds today; a project first settles what
the product is to become. The task assignment follows the breakdown and changes with it, while
the definition remains the source of what was settled.
*Rejected:* putting projected entries into the foundation at the readiness gate — it would describe
a future product as current; keeping the task assignment in the definition — it would duplicate
the plan and change as the plan changes.

### WAY-107/1 — Where does a product tell the project level where its backlog stands?

A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`,
outside the block the-way's installer owns. A project definition stands in the named project
place; when the place is unnamed, the agent asks the human and offers to record the answer there.

- **Change:** new decision
- **Scope:** project-level, installation
- **Based on:** none
- **Relations:** derives from WAY-101@518c4b32
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a product names a directory for projects and a tracker for tasks in its own backlog
    section, and the project definition is written in that directory;
  - violates: the project skill assumes one backlog service for every product, or puts the
    product's paths inside the installer's marked block.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* the product chooses its own backlog place, and a root instruction gives an agent one
place to find it. Keeping the place outside the generated block lets the product change it without
editing the process's installed guidance.
*Rejected:* a fixed backlog location for all products — it would require moving an existing
backlog; asking for the location in every project conversation — the answer would be lost between
sessions.

### WAY-108/1 — What form does a project definition take?

A project definition is one document with the ordered sections of the project-level template; its
title and content use the language in which the human opened the conversation, while headings,
status values, markers read by the readiness check and projected foundation entries keep their
English forms. A `Status:` line
records whether sections are open, the definition is ready for the gate, or it is approved; every
section contains content, `none` for nothing there, or `TODO` for something missing. An unknown
stays as `TODO` in the section or projected entry that needs it, or as an open question naming
the breakdown or task that resolves it.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: project-definition-form. Level 2 for the language of
  content and the meaning of `none` — an agent compares the change with the decision:
  - complies: a Polish conversation produces Polish section content under fixed English headings,
    and a section with no risks reads `none` only after the human has said there are none;
  - violates: translated headings make the readiness check unable to read the document, or an
    unanswered section silently reads `none`.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* the person deciding the project reads its content in the language of the conversation;
fixed structural words let later work resume and check the document. A written state and
an explicit missing value show where the next conversation begins.
*Rejected:* translating structural words with the content — a checker could not read every
language; inferring progress from prose alone — a fresh agent would reconstruct the state.

### WAY-109/1 — What may a project definition treat as settled without the human's answer?

The definition's background, success and risks come from the human's answers; material supplied to
the agent anchors questions and is not silently adopted as a settlement. Every success signal
states what would falsify it.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a concept's claim of success enters the agent's question, and the definition records
    the person's answer with a condition that would show it false;
  - violates: a concept's assumption becomes a risk without asking, or a success signal names no
    circumstance that would show it false.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* a fluent draft makes an agent's inference look like the human's decision. A condition
that could disprove success gives later work a way to judge it.
*Rejected:* filling gaps from plausible material — later tasks would inherit invented choices.

### WAY-110/1 — When does a deadline enter a project definition?

A deadline enters the definition only when the human names one imposed from outside, in the
human's own words and with how firmly it binds. The agent neither asks for a deadline nor derives
one from material, and does not argue the project's scope or cost from it.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the human names an externally imposed launch date and says how firm it is, so the
    definition records that answer in their words;
  - violates: the agent asks for a deadline as a routine field, infers one from a concept's date,
    or uses a stated date to press for a smaller scope.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* a date imposed by the surroundings can constrain the work, while a date invented for
planning makes the constraint appear to come from the human.
*Rejected:* a routine deadline question — it creates pressure without an external constraint;
deriving a deadline from background material — it mistakes context for a settlement.

### WAY-111/1 — What does the project level read in the current foundation?

Before drafting, the agent selects and reads the current foundation under WAY-150, identifying
touched parts from the proposed project's responsibilities, behaviour, flows and surfaces. It
brings a touched part, a decision the project may change, an invariant it may break or a boundary
it crosses to the human as material and asks
whether the project changes an existing decision or fits it.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-150@3bd9e695
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: before any diff exists, the agent maps the idea to affected responsibilities and
    surfaces, reads every applicable Scope decision and expands to an unlinked invariant, then
    shows the touched decision and boundary and asks whether the project changes or fits it;
  - violates: the agent treats the absence of a diff as no touched parts, or reads only decisions
    already linked to the idea and misses an unlinked invariant or a boundary in the map.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/18

*Rationale:* the current foundation gives a project its starting constraints before its design
has files to point from. Reading from the proposed behaviour finds those constraints while leaving
room to follow an unexpected conflict; showing the conflict lets the human decide its meaning.
*Rejected:* reading the whole foundation for every idea — context grows with unrelated rules;
reading only entries with a matching scope or known link — an unlinked conflict stays hidden;
waiting for changed files to choose context — the project is drafted before those files exist.

### WAY-112/1 — How does an agent develop and resume a project definition?

The agent confirms its understanding of the goal with the human before the definition's first
write, then creates the initial sketch in the product's project place without a separate request
and gives its full path. It asks about the largest gaps, challenges a frame only from an anchor in
the human's words or material, reads what product files can answer, and treats "I do not know" on
assessment as an open question with its resolver but on a choice as a reason to offer a
recommendation with costs. It writes each answer and the updated `Status:` line before the next
question; work resumes from that line and, while entries are being found, from the candidate table.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: after the goal is confirmed, an agent writes a sketch, then records each answer and
    its new status before continuing; a later agent resumes from the recorded open section;
  - violates: an agent writes a complete definition from the source before checking the goal, or
    asks another question while the prior answer exists only in conversation.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* the first confirmation prevents a polished document for the wrong goal; saving each
answer makes the document a reliable place to resume. Source-anchored challenges can change an
assumption without asking the human to defend an invented objection.
*Rejected:* waiting for a second permission after confirming the goal — it adds a stop without a
new decision; writing only at the end — an interruption loses settled answers; challenging every
line by a fixed script — questions without a real anchor consume the person's attention.

### WAY-113/1 — How does an agent of the-way ask a human decision?

An agent asks in plain conversation text: a decision question gives the available ways, the cost
of each and a recommendation, while a question of assessment stays open; neither opens a separate
question panel. After a human choice enters an entry's binding part, the agent asks one question
against that choice anchored in the human's words or supplied material, unless the choice ends
with the work, or the human took one of the ways offered and the decision question named, anchored
in the material, the weak point of that way.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the exchange with the decision:
  - complies: a choice is presented in text with the costs of both ways and a recommendation,
    followed by a source-anchored question against the answer when it enters a binding entry,
    unless the person took a way offered whose weak point the question named;
  - violates: the choice appears only in a separate option panel, an agent asks a generic
    challenge unrelated to the person's answer, or an agent asks against a way offered whose weak
    point the question already named and the person took as offered.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-05

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

### WAY-114/1 — What does a human accept of an entry, and when?

A human accepts the meaning of a foundation entry, shown as one sentence in the human's language with
the entry beside it, while its wording is the agent's: an agent writes the entry and the human accepts
it at the merge of the change that holds it, or, for a projected entry, at the readiness gate. Before
that, a question goes to the human only where the agent has no recommendation or the entry would
change the meaning of an approved decision; a translation never enters the foundation.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: the request lists each entry it writes with one sentence of its meaning in Polish, and
    the human reads the entries before merging;
  - violates: an agent asks the human to confirm a choice it already recommends; a translation is
    written into the foundation; an entry changes the meaning of an approved decision without a
    question.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* the human judges what an entry settles; its wording rarely changes that, and the human
who merges reads what the change holds and answers for it.
*Rejected:* acceptance of the whole wording before an entry is written — attention goes to wording
while the meaning rarely moves, and each acceptance costs a round; storing a translation in the
foundation — two binding wordings could drift apart.

### WAY-115/1 — How are foundation entries found in a project's source?

The agent reads the project's sources in full and selects and reads the product's foundation under
WAY-150, then shows the human a complete candidate table with each proposed settlement, its kind,
its source and the concrete
choice or action the next reader would otherwise have to guess; a row without such a consequence
is shown as rejected. The human accepts or rejects rows before they are handed to the skills of
their kinds, and each accepted row is recorded as it is worked through. The definition keeps the
working table until the step ends, then replaces it with a `Candidates:` line recording how many
rows were shown and accepted.

- **Change:** new decision
- **Scope:** elements-common, project-level
- **Based on:** none
- **Relations:** derives from WAY-150@3bd9e695
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: the human sees every column of the candidate table, rejects an exclusion whose
    absence would make no task guess, and the completed definition carries the candidates line;
  - violates: the conversation hides the source and the next reader's guess while a file holds
    them, or entries are written before the human has cut the table.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/18

*Rationale:* the source distinguishes a human settlement from material offered for consideration;
the concrete guess filters noise before it becomes a rule. A table with row states lets work
resume, and a final line shows that the search occurred even when it yields no entry.
*Rejected:* turning every scope line into a foundation entry — exclusions that nobody would
misread become permanent noise; showing a shortened table — the human cannot judge provenance or
the reason a candidate matters.

### WAY-116/1 — Which foundation entries may a project definition project?

A project definition projects decisions, invariants and glossary terms that the human can settle
before the breakdown, and environment facts only where a projected decision or invariant rests on
them. Of the part map it projects a changed existing part or a critical flow through existing
parts only when every field is already known; a new part or surface remains an open question for
the breakdown.

- **Change:** new decision
- **Scope:** project-level, decisions, invariants, glossary, environment-facts, part-map
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the definition with the decision:
  - complies: the definition holds a proposed access rule, a related glossary term and a
    changed known part, while a future new part is an open question resolved in the breakdown;
  - violates: it invents files for a part that has not been designed, or records a fact with no
    projected entry depending on it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* a project can settle rules of a future product before it has tasks, but some map
fields exist only once code and files do. Restricting facts to what a proposed rule rests on
prevents a speculative inventory of the surrounding world.
*Rejected:* decisions alone at the project level — later work would still have to infer known
invariants and terms; projecting new parts with guessed files or missing fields — the map would
look complete while naming a structure that does not exist.

### WAY-117/1 — How does a foundation entry stand in a project definition before it is written?

The skill of each entry's kind writes its whole proposal under the definition's `Projected
foundation changes`, in that kind's subsection with the template's projected heading and one
sentence of its meaning, without writing the product's foundation or running the entry's format guard. A
new projected decision uses `(new)` without a number or prefix, while versions and other kinds
use the identifiers their templates give; an entry following from it remains projected or becomes
an open question when its fields await the code.

- **Change:** new decision
- **Scope:** project-level, elements-common, decisions, invariants, glossary, environment-facts,
  part-map
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: a new decision carries `(new)`, a revised decision carries its version, and an
    invariant's method remains `TODO` until a task can write its check;
  - violates: a projected proposal is written directly into the foundation, or a decision's
    revised version loses its identifier in the definition.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* the project's definition keeps a future rule visible without claiming it already
holds. Code-dependent evidence can be completed when the task writes the entry.
*Rejected:* filling every field with an invented future method or file — it makes the proposal
look checked before the product exists; leaving the human's reasoning to later tasks — they
cannot recover what was considered during definition.

### WAY-118/1 — What makes a project definition ready for breakdown?

The readiness gate blocks a definition with a missing section, unresolved content, an open
question without its place of resolution, an unfinished candidate search, or an unsettled
human-given part of a projected entry: its binding sentence or definition and a decision's
*Change*, rationale and rejected options; *Approved by* reads `on acceptance` until the gate,
and only projected fields awaiting code or the world, including an expressly deferred
*Review when* as WAY-119 permits, may read `TODO`.
Before approval an agent searches the whole current foundation for unlinked collisions, and the
human approves the whole projected entries with permitted `TODO`; the gate record then names the
approver, the foundation commit searched and the fingerprint of the definition's sections from
Goal through Projected foundation changes. A change to those sections after approval goes through
the gate again before breakdown relies on it.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: project-readiness-gate. Level 2 for the foundation
  search and human approval — an agent compares the work with the decision:
  - complies: the script stops an unfinished candidate table, the agent resolves a collision with
    an existing decision, and the human approves the finished proposals;
  - violates: a warning-only review lets the breakdown begin with a missing decision reason, or
    an edit to a fingerprinted section after approval keeps the old gate record.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* a warning lets a later step guess precisely what definition was meant to settle;
blocking exposes the missing answer while the person who can give it is present. The search and
fingerprint show which foundation and wording were approved.
*Rejected:* a final checklist that only warns — it cannot prevent an unfinished search from
passing; an approval without a content fingerprint — later edits would still look approved.

### WAY-119/1 — When may a projected decision leave Review when unresolved at the gate?

At the readiness gate, a projected decision's *Review when* holds a review condition and date, or
`none` after the human has settled that no such condition applies. It may read `TODO` only when
the timing depends on later work, the human expressly accepts deferral, and a related open
question names the breakdown or task that settles it.

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-118@5af868b3
- **Verification:** level 2 — an agent compares the definition and human approval with the
  decision:
  - complies: a prediction's review date depends on the release, so the human accepts `TODO` and
    an open question names the task that will set the date;
  - violates: the gate passes a `Review when: TODO` with no related open question, or an agent
    writes `none` simply because the source said nothing about review.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* the date for testing a prediction can depend on delivery that has not yet been
planned. An explicit deferral keeps that uncertainty visible and gives later work a place to
finish it.
*Rejected:* blocking every `TODO` — the human would have to guess a date before the plan exists;
allowing an unexplained `TODO` — no later task would own the missing answer.

### WAY-120/1 — How does the-way critique an agent's proposal?

An agent may invoke critique for any proposal without waiting for the human to express doubt; a
completed set for collective human review and every change to an invariant test or to the
foundation go through it, and for such a change the critique is its independent assessment
(WAY-10). An independent critique gives one fresh agent the full proposal or set, its sources and
applicable rules without the author's defense; the author checks each observation and gives one
explicit verdict. For a collectively reviewed set the critic checks form, fidelity to source and
contradictions across entries before presentation.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, elements-common,
  project-level, relation-model, gate, installation, agent-instructions, instruction-files,
  repository, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-10@db68de1c
- **Verification:** level 2 — an agent compares the review with the decision:
  - complies: one fresh critic receives a finished set and its sources, reports evidence for each
    concern, and the author verifies it before presenting corrected proposals and open questions;
  - violates: one critic is run per row of a set, the author silently changes a human settlement,
    or two critics are run on one change.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* the author is attached to its own fluent proposal, and an independent reading can
find a mismatch with its source or another entry before the human spends attention on the set.
The author's verdict keeps the critic an aid rather than a second decision-maker.
*Rejected:* a fresh critic for every entry accepted with the human — it repeats the human's
review; letting the critic's remarks edit human settlements without asking — it would disguise a
new decision as a correction.

### WAY-121/1 — Where does a project settle the technology it needs?

Before a project definition goes through its readiness gate, a step of its own lists the
technology and architecture choices the project needs — such as a language, a framework, a store
of data or a place to run — and settles each one the foundation does not already hold as a
projected decision of the definition. A choice belongs on the list when settling it later could
change how the work is cut into tasks, or when it adds something the product has to run, pay for
or back up; a choice one task can make and change alone stays with that task. When the foundation
already holds every such choice, the step records the decision that holds each and settles nothing.

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-116@afbcd2fa
- **Verification:** level 1 — invariants: project-technology-record. Level 2 for what the step
  lists and settles — an agent compares the work with the decision:
  - complies: a project that adds an account server lists its store of data and its way of
    logging in, and the definition projects a decision on each; a project that changes only how a
    screen looks records that the foundation holds every choice it needs;
  - violates: the first task of the breakdown chooses the database; a definition reaches the gate
    with a store of data in its scope and no choice of it projected or found in the foundation.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-04

*Rationale:* whether a technology choice changes how the work is cut into tasks cannot be judged
by someone who does not know the technologies, so the choice is settled before the cut; a step of
its own keeps the comparison of technologies out of the talk about the project's goal and scope,
while its agent still knows the whole project. Settled before the gate, the choices are approved
with the rest of the definition, and an exit for a project whose choices the foundation already
holds keeps the step from being an empty run.
*Rejected:* a round inside the conversation about goal and scope — no place to compare
technologies; the first tasks of the breakdown — the cut itself may depend on the choice; the step
after the readiness gate — each settled choice would change approved sections and send the
definition through the gate again (WAY-118); one step for every project with no exit — an empty
run wherever nothing changes.

### WAY-122/1 — How are the options of a technology choice found and checked before a human sees them?

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

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121@740c254e · derives from WAY-120@81f84997
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: research for a store of data compares a file kept beside the application with a
    database server, each typed and documented, and the critique strikes a claimed difference in
    speed that no source gives; a built-in module with no record of wide use stays in the
    comparison beside a widely used library, its lack said as what it means for the product;
  - violates: the step offers a framework, a database and a host as one bundle from a fixed list;
    a comparison reaches the human with a difference no source supports; an option with
    documentation and a maintained project disappears from the comparison because it lacks one of
    the properties; an option the human names disappears from the comparison; the research of a
    choice that depends on no unsettled choice waits for another choice to be settled.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-05

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

### WAY-123/1 — How does a technology choice reach a human who cannot assess the technology?

The step that settles a project's technology shows the options of each choice by their
consequences for the product — what it costs, where it runs, what keeping it running takes and
what changing it later costs — and the human chooses between those consequences. A difference with
no consequence for the product decides nothing, and where no difference with a consequence
remains, the step recommends the simplest and cheapest option. The choices whose research started
together reach the human together, in one table, once every one of their comparisons has passed
the critique, each with its recommendation and the weak point of the option recommended.

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-121@740c254e · derives from WAY-113@d3e5cbfa
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: two stores of data are shown as "a file kept with the application and copied with
    it for a backup" against "a server to keep running in the container, with backups of its
    own", and the human picks one;
  - violates: the options are shown as lists of technical features; two options with no
    difference in consequences are offered as a matter of taste instead of the simpler one being
    recommended; two choices whose research started together reach the human in separate
    tables.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-05

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

### WAY-124/1 — When is a task ready for its cycle?

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

- **Change:** new decision
- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-118@5af868b3 · derives from
  WAY-126@35accf8b · derives from WAY-134@2fc974a9 · derives from WAY-140@6e564611
- **Verification:** level 2 — an agent compares the task document with its stated sources:
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
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

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

### WAY-125/1 — Which Superpowers methods does the autonomous task cycle adopt?

The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec,
test-first implementation, subagent execution with independent task and final code reviews, and
preparing a pull or merge request, only for a ready task run through `implement-task`. The
orchestrator answers workflow questions and gives provisional stage go-aheads under the task
owner's delegation, never records these as human approval, controls the return between stages,
keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment
of its foundation change and its return step, and brings the request to the human for review.
Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed
without one, the cycle opens a blocked draft request; a different Superpowers version requires a
reviewed change to the-way before use.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** observation of installed Superpowers 6.4.1 on 2026-10-05 using `Get-Content -Raw
  -Encoding utf8 '<source-root>/<skill>/SKILL.md'` for each skill below; Windows PowerShell
  5.1.26100.9444 on Microsoft Windows NT 10.0.26300.0; source root
  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`:
  `brainstorming/SKILL.md` — "Help turn ideas into fully formed designs and specs through natural
  collaborative dialogue." `test-driven-development/SKILL.md` — "Write the test first. Watch it
  fail. Write minimal code to pass." `subagent-driven-development/SKILL.md` — "Fresh subagent per
  task + task review (spec + quality) + broad final review = high quality, fast iteration"
  `requesting-code-review/SKILL.md` — "The reviewer gets precisely crafted context for evaluation —
  never your session's history." `finishing-a-development-branch/SKILL.md` — "Verify tests → Detect
  environment → Present options → Execute choice → Clean up."
- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-13@e6c830b7
- **Verification:** level 2 — an agent compares a cycle with the decision:
  - complies: agents use the named methods at version 6.4.1, return between stages, and show
    provisional choices in the request without claiming human approval;
  - violates: an agent treats its own spec approval as the owner's approval, skips the request
    review, or silently runs a different Superpowers version.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/13

*Rationale:* the borrowed skills provide design, test and review methods, while the-way must keep
control of task sources, binding foundation approvals and the single human review point. Naming
the version makes the dependency visible when the process is pinned in a product. When a spec is
written and how a plan is written are the-way's own (WAY-135, WAY-136), so the methods adopted here
are those a cycle uses whenever its stage comes.
*Rejected:* adopting the complete Superpowers workflow with its intermediate human gates — it would
interrupt the delegated cycle; copying the skill bodies into the orchestrator — it would create a
second implementation of those methods.

### WAY-126/1 — How does a projected entry enter the foundation?

A projected entry of an approved project definition enters the product's foundation in the
foundation step of the first task whose code makes it true — the task the plan assigns, or a task
that uses the definition as a source only, even where the plan assigns the entry to another task —
whole, in the wording the readiness gate approved, with *Approved by* transcribed from the gate
record and with the projected terms and environment facts it uses or rests on; where the code
makes only part of it true, the agent writes that part and the human accepts its meaning at the
merge (WAY-114). The task the plan assigns writes what of the entry the foundation does not yet
hold, and a projected entry no code makes true. The return step reads the projected entries of the
task's sources as well as the foundation, writes one the code makes true that the foundation step
missed — an invariant with a check by an agent that did not write the code it covers, run on that
code — and writes a new entry only for a rule none of them states.

- **Change:** new decision
- **Scope:** project-level, task-cycle, decisions, invariants, glossary, environment-facts,
  part-map
- **Based on:** none
- **Relations:** derives from WAY-01@60960941 · derives from WAY-11@e882a9df · derives from
  WAY-114@04b4f599 · derives from WAY-118@5af868b3 · narrows WAY-106@63eddf70
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a source-only task whose code adds the store a projected decision chooses writes
    that decision whole in its foundation step, *Approved by* copied from the gate record, and
    the task the plan assigns later finds it and writes nothing; a task whose code makes one of
    a projected decision's two sentences true writes that sentence and lists its meaning in the
    request;
    a plan member whose code would make another item's entry true returns to the plan first;
  - violates: the return step writes a new decision for a rule a projected entry of the
    task's source states; a shortened projected entry is written with the gate's *Approved by*;
    the code a late-found projected invariant covers is set aside and rewritten.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* a projected entry is wording a human already settled at the gate, and the task
whose code first makes it true is the one that can show it holds; entering with that code keeps
the foundation describing the present product and keeps one entry per rule. Writing it in the
foundation step keeps the order a foundation change has: the entry, and an invariant's test, are
written before the code that follows. A part of an entry is wording the gate did not
approve in that form, so its meaning reaches the human at the merge.
*Rejected:* holding a projected entry back for the task the plan assigns — the foundation would
lag behind the code it describes; a return step that searches only the current foundation — a
rule settled in a definition comes back as a second entry under another name; carrying a
shortened entry as approved — the foundation would gain binding sentences no human approved in
that form; rewriting the code a late-found projected invariant covers — a check by an agent that
did not write the code guards it without a second implementation.

### WAY-127/1 — How does a session working on the-way itself reach the-way's skills?

A session working on the-way itself reaches each skill of the-way as the project skill
`the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md`
and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from
the skill's `SKILL.md`. An entry point reads its skill and the files it names from the checkout or
worktree the session works in — where it was started, or where it was last moved — stops itself
in a product, and hands another the-way skill on under the `the-way-` prefix. No global link
reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository
that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in
itself.

- **Change:** new decision
- **Scope:** agent-instructions, elements-common, project-level, task-cycle, decisions, invariants,
  glossary, part-map, environment-facts, installation, instruction-files
- **Based on:** claude-code-project-skills@d58fb91f · claude-code-nested-skills@4dd3d448 ·
  codex-repository-skills@7db28f98 · codex-skill-paths@5b5b6c79
- **Relations:** derives from WAY-44@2f2b6227
- **Verification:** level 1 — invariants: skill-entry-points. Level 2 for the paragraphs of the
  skills that say where the-way lies — an agent compares the change with the decision:
  - complies: a skill's paragraph names, as the place of the-way, the checkout or worktree the
    session works in for the-way itself and the pinned `.the-way` for a product, and names
    another the-way skill it hands to as the project skill with the `the-way-` prefix;
  - violates: a skill tells an agent to resolve a global link to find the-way; a skill run in the-way
    hands its work to `critique` without the prefix.
  Level 2 for the global link and the skill of `instruction-files/` — an agent compares the change
  with the decision:
  - complies: a global link leads to `instruction-files/` of a worktree kept at the merged tip, and
    the skill judging a product that pins the-way follows that product's
    `.the-way/instruction-files/SKILL.md`;
  - violates: a global link leads to another skill of the-way; the skill judges a product that pins
    the-way with the copy its global link reaches.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

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
it to the prefixed skill.
*Rejected:* a mode of the installer without a pin writing the same entry points into the-way — its
generated files would belong to `installation`, outside that part's directory, and its trust
boundary would grow; entry points written per checkout and ignored by git — a fresh worktree or
cloud session has none until someone writes them; global links, one per worktree, or links tracked
by git — a global link reads one checkout whatever branch the session works on, and tracked links
need a git setting and extra rights on Windows; names without the prefix — which skill a session
gets would rest on how Claude Code and Codex settle two skills of one name.

### WAY-128/1 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand?

A line for a file that an agent's tool loads into every session — one the skill of
`instruction-files` proposes, or one a change to the-way's repository instruction files adds or
rewords — is one that every session needs or that points to work an agent would not otherwise find,
that an agent could not read from the repository or from general knowledge, and without which an
agent would go wrong. Any other rule the skill proposes or such a change adds stands where what
calls for it reaches the agent: a rule for some files in a file the tools load with those files, a
rule for an activity in the steps of the skill that carries out that activity or in the file that
leads it, and knowledge needed now and then in a file such a step or line points to.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** context-file-effect@c44e5ef0 · claude-code-path-rules@ac99f128 ·
  codex-agents-md@6dc13475
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a change adds to the-way's root `AGENTS.md` a line pointing, with its condition, to a
    guide no session would find otherwise; the skill proposes to move a rule for one directory's
    files into a file loaded with them;
  - violates: the skill proposes a line describing a repository's directories and stack; a change
    adds to the-way's root `AGENTS.md` the test command its guide already gives.
- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
  of models · check by: 2027-01-08
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

*Rationale:* a line loaded into every session costs context in each, and agents carry out what it
asks, so it earns its place only when each session needs it; descriptions of a repository have not
helped agents, while the instructions they are given are followed; a rule loaded with the files or
the activity that call for it costs nothing elsewhere; one tool reads a subdirectory's file only in
sessions started at or below it, so such a file needs a line that points to it. The decision binds
what a change adds or rewords from then on; lines that stand unchanged are not bound by it, as the
process enters an existing product (WAY-28). Process skills and their entry points answer to their
own decisions (WAY-35, WAY-127), not to this one.
*Rejected:* a fixed count of lines as the measure of a file — a count says nothing of whether a
given line is needed, even where a shorter file saves context in every session; a file of pointers
alone — it leaves reading each rule to the agent's choice; a file of its own for every area with
rules of its own — a split changes nothing unless it changes when the rule loads; rules drawn from
the repository's code — the agent reads the code itself; binding the lines that stand today — every
unchanged line would become a breach on the day of the merge.

### WAY-129/1 — How does an instruction file point an agent to another file?

The-way's repository instruction files hold no `@` import other than the line `@AGENTS.md` alone at
the top of the root `CLAUDE.md`, and the skill of `instruction-files` proposes none other. A pointer
the skill proposes, or a change to the-way's repository instruction files adds, names the file to
read by its path in backticks with the condition under which to read it.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** claude-code-imports@5b9359fd
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 1 — invariants: instruction-file-imports. Level 2 for the condition beside
  a path — an agent compares the change with the decision:
  - complies: a pointer reads "Before you change the-way, read `agent-instructions/README.md`";
  - violates: a pointer reads "See @docs/style.md for the style"; a list of paths with no word on
    when to read them.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

*Rationale:* an import loads the whole file it names into every session, so a file meant for
occasional reading costs its full length in each; a path with its condition costs one line and is
read when the condition comes.
*Rejected:* `@` as a light pointer — it loads, it does not point; the text of the file pasted in — a
second copy that drifts.

### WAY-130/1 — When does a rule enter an instruction file, and when does it leave?

The skill of `instruction-files` proposes a rule, and a change to the-way's repository instruction
files adds one, only to remove a mistake agents made more than once, found in records of their
work, and names that mistake where it proposes or adds the rule, unless the rule carries a decision
the repository records or a step of an activity in the file that leads that activity. The skill
proposes to take out a rule added for a mistake once that mistake can no longer be named, or once
agents working without it show that it is not needed.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** https://arxiv.org/html/2511.12884v2 § 4.2.3 — "The evolution of Agent context files
  is driven by small, incremental additions, while deletions are minimal." · § 4.2.3 — "this
  suggests that the increase in line counts is not simply due to uneven edit sizes, but instead
  reflects a meaningful tendency to add new instructions rather than remove existing ones."; read
  2026-10-08
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a change adding a rule to the-way's root `AGENTS.md` names in its request the mistake
    it removes and the records where agents made it twice or more; a change adds to the guide that
    leads the-way's integration the step a new decision sets, with that decision as its reason; the
    skill proposes no rule for a mistake it found once or not at all;
  - violates: a rule added "just in case" after one slip recalled from memory; the skill proposes a
    rule whose mistake it did not look for; a rule against one slip is added to the guide as a step
    of the work.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

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

### WAY-131/1 — How is it settled whether a rule of an instruction file works?

Where the skill of `instruction-files` says whether a rule works, and where the request of a change
to the-way's repository instruction files says so, it is settled as three separate questions:
whether the tool loaded it, by one fresh session per variant with a file that has to load as a
control; whether agents followed it, by as many fresh sessions with and without it, on one model
and tool release, as its effect needs to stand out from the variation between runs; and whether it
helped, by whether its mistake stops coming back in agents' work over time, never by test sessions
alone.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** agent-run-variance@538af710
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a rule whose behaviour never happens without it is shown working by a few sessions
    with and without it; a rule meant to make a behaviour more frequent is judged over many sessions
    or by watching its mistake;
  - violates: a few sessions with and without are taken as proof that a rule raised a behaviour
    that also happens without it; a rule is called useless because one session did not load it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

*Rationale:* loading, following and helping fail apart and are fixed apart — another carrier, other
wording or a mechanism, or nothing; runs of one agent on one task differ, so a small effect drowns
in a few sessions. The finding on that variation measured models of other publishers only, and this
decision takes it across publishers (WAY-85).
*Rejected:* the same small number of sessions with and without for every rule — it settles only a
behaviour absent without the rule; one question "does it work" — it mixes defects with different
fixes.

### WAY-132/1 — Which file carries the instructions Claude Code, Codex and Cursor share?

The skill of `instruction-files` proposes for a repository whose agents use more than one of Claude
Code, Codex and Cursor, and the-way keeps for itself, a root `AGENTS.md` that carries the
instructions those tools share and a root `CLAUDE.md`, where there is one, whose first line is
`@AGENTS.md` alone and which holds only what Claude Code alone needs. The skill leaves out of this
proposal the files and the marked block the-way's installer writes in a product.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** claude-code-agents-md@e4007cb8 · codex-agents-md@6dc13475 · cursor-agents-md@aaa19b03 ·
  claude-code-imports@5b9359fd
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 1 — invariants: root-claude-md-import. Level 2 for what `CLAUDE.md` holds
  and for respecting the installer's files — an agent compares the change with the decision:
  - complies: the-way's `CLAUDE.md` is the one line `@AGENTS.md`; the skill proposes, after the
    import, a note for Claude Code alone; in a product, the skill leaves the installer's root
    `CLAUDE.md` and marked block of `AGENTS.md` to the installer;
  - violates: the skill proposes a `CLAUDE.md` restating the rules of `AGENTS.md`; the skill
    proposes to delete the installer's root `CLAUDE.md` or edit the block between the installer's
    markers.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

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

### WAY-133/1 — How is a rule of an instruction file kept when it has to hold every time?

Where a rule of an instruction file has to hold every time, the skill of `instruction-files`
proposes a mechanism that keeps it without the agent choosing to — a CI check, a linter, a check of
a step's output, or a local git hook where the rule guards against slips rather than against an
agent that can turn the hook off — and a change to the-way's repository instruction files adds such
a rule only with its mechanism. The instruction file then says what the mechanism is for, or
carries what the mechanism cannot check.

- **Change:** new decision
- **Scope:** instruction-files, agent-instructions
- **Based on:** single-rule-compliance@cf537693
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the skill proposes a CI check for a rule it found broken in commits, and an
    instruction only for what the check cannot read; a change adds to the-way's guide a rule that
    every commit names its task, together with a CI check that fails a request whose commits name
    none;
  - violates: a change adds a rule that has to hold on every commit only as a line of `AGENTS.md`;
    the skill proposes a hook of one agent tool, or a local git hook, as what keeps a rule against
    an agent that can switch it off.
- **Review when:** no model in the range of fact single-rule-compliance is Active in Anthropic's
  table of models · check by: 2027-01-08
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/11

*Rationale:* a loaded rule is still not always followed, so what has to hold every time needs a
mechanism that does not depend on the agent; the instruction beside it explains, so the agent meets
the rule at the first try. A local hook — of an agent tool or of git — is skipped by one switch, as
WAY-03 weighed, so it keeps a rule against slips, never against an agent that can turn it off; a
hook of one agent tool also reaches only that tool's sessions.
*Rejected:* an instruction alone, worded more strongly — a stronger wording is still a loaded rule,
which is not followed every time; a mechanism with no word to the agent — the agent learns of it
only by failing it; a local hook as the keeper of every rule — one switch skips it.

### WAY-134/1 — How does a task carry what its refinement settles for the foundation?

Before a task is ready for its cycle, the human sees a table of candidates found in the task
document and the conversation that refined it, in the form WAY-115 gives with each settlement in
the human's words, and the task document keeps the rows the human accepts; in manual refinement
the agent refining it presents the table, while in orchestrated refinement the project
orchestrator presents it and the questions against choices required by WAY-113 in the round
package, and the refiner returns that material through the conversation file instead of asking
the human. A candidate is a decision, an invariant, a glossary term, or an environment fact a
candidate decision or invariant rests on, and a settlement that a current entry, or a projected
entry the task carries, already states is no candidate. The task's cycle writes each kept row
whole into the foundation in its foundation step, or in its return step where the foundation
step missed it, one that no code makes true included, keeping its meaning and choosing its
wording; where that meaning cannot hold, or the entry needs a value neither the row nor the
cycle's work gives, the cycle asks the human through a blocked draft request rather than write
another entry, and otherwise the human accepts the entry's meaning at the merge (WAY-114).

- **Change:** new decision
- **Scope:** project-level, task-cycle, elements-common, decisions, invariants, glossary,
  environment-facts
- **Based on:** none
- **Relations:** derives from WAY-115@eb7ba15c · narrows WAY-114@04b4f599
- **Verification:** level 2 — an agent compares the task document, or the cycle, with the decision:
  - complies: a task whose human settled in refinement that an exported record keeps its owner
    carries that row, and its cycle writes a decision with that meaning in its foundation step,
    before the code, and names it in the request; a task whose refinement found nothing carries the
    counting line with none below it; in an orchestrated round the project orchestrator shows the
    candidate table and required challenge questions while the refiner records the human's answers;
  - violates: the cycle writes the entry with another meaning, or leaves out a kept settlement
    because no code makes it true; the refinement writes whole entries into the task document; a
    kept row repeats a rule a current decision states; an orchestrated refiner asks the human
    directly about candidates or substitutes its own acceptance.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* a settlement the human makes while a task is refined binds after the merge as much as
one a project settles, yet with no place in the task document it reaches the cycle as an answer to
a question, where it reads as one more choice the cycle may make otherwise. A row in the human's
words carries the meaning into the cycle without a second point of acceptance: the wording stays
the agent's, as for every entry a cycle writes, and the human judges the meaning at the merge. A
table read from the whole document finds a settlement said in passing, and its column of what the
cycle would guess drops one no reader would miss. A meaning that cannot hold goes back to the human
before the request because the human settled it, and finding the change only at the merge would
leave code already written for another meaning. In an orchestrated round a single human-facing
agent keeps these choices together without making the refiner a second channel to the human.
*Rejected:* whole entries written while the task is refined, as a project definition projects
them — a task has no gate to approve their wording, and refining a task would weigh as much as
defining a project; noting a settlement only when the human states one — a settlement said in
passing in the request is missed, and the agent alone decides what binds; letting the cycle change
or drop a settlement and show the difference in the request — the human's settlement could be
reversed and seen only once the code is written; decisions and invariants alone — a word whose
meaning the human settled would be defined by the cycle.

### WAY-135/1 — When does a task's cycle write a spec?

A task's cycle writes a spec, reviewed by an agent other than its author, before implementation
and any plan where the task leaves an open design choice and nowhere else, and an invariant whose
sentence a row of the task's *Settlements to record* or a projected entry of its sources gives
leaves none. An agent that
meets an open design choice while it makes the change returns a report that holds no code, the
attempt is discarded with the foundation entries the cycle wrote for it, and a fresh agent given
the report writes the spec, after whose review the orchestrator chooses again whether one author
can hold the change or it needs a plan, using the same judgment as before implementation (WAY-136).

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-13@e6c830b7 · derives from WAY-69@7051f884 · derives from
  WAY-126@35accf8b · derives from WAY-134@2fc974a9
- **Verification:** level 2 — an agent compares a cycle with the decision:
  - complies: a task whose rows of *Settlements to record* carry its two decisions and its invariant
    proceeds without a spec, and the invariant's check comes from an agent given only the sentence
    and its method; a task whose part-map change follows from the file it adds, with no other way
    open, proceeds without a spec; an agent that finds the task needs a decision the task does not
    carry returns a report without code, the branch goes back to its base, and a fresh agent writes
    the spec; a reviewed spec is followed by one author without a plan when the change still
    fits one agent, or by a new plan when it needs division;
  - violates: a spec is written for a task whose document carries every entry it writes and that
    leaves no other way open; an agent designs a decision the task does not carry and goes on with
    the code; a spec is written around the code of an attempt that met an open design choice;
    a plan is required merely because a spec was written.
- **Review when:** five cycles of `implement-task` have run under this decision, or a cycle has
  found a new foundation entry contradicting a current one only after its code was written ·
  check by: 2026-11-30
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* a spec and its review earn their cost where an agent designs a foundation entry itself,
whose agreement with the current entries has to be checked before code is written on it; where the
task's document carries every entry, a spec restates what the human already settled and its review
finds nothing the reviews of the code would miss. An invariant the document carries is kept from
fitting the code by the separate authors of its sentence, its check and the code (WAY-69), not by a
spec. A choice found while the code is made cannot be weighed apart from that code, so the attempt
goes, its slices already made among them, since the spec may change what they made, and a fresh
agent designs from the task and the report. Settling the design does not itself create work to
divide; the extent of the settled change decides whether a plan earns its cost.
*Rejected:* a spec for every task that changes the foundation — almost every task changes it, and
the spec would restate entries the human settled at a large share of the cycle's cost; no spec for
any task — an entry an agent designs would reach the code unchecked against the current entries;
an attempt that met an open design choice kept and completed — a spec would be written around
partial code; the agent of that attempt writing the spec — the spec would carry the shape of the
abandoned code; a spec for every task that writes an invariant — its separate authors already keep
its check apart from the code.

### WAY-136/1 — When does a task's change need a plan, and who makes and reviews it?

A change that, as the orchestrator judges from the task document in step 4 before implementation,
one agent can hold is made without a plan by one author, who writes its foundation entries, its
code and its return step, while an invariant's sentence and its check come from two other agents
(WAY-69); the same judgment follows a reviewed spec, and an author that finds the change too large
returns a report without code, its attempt is discarded with the foundation entries it wrote,
and a planner divides the change. Every other change gets a plan written with the-way's skill
`plan-task`, which divides it into slices and holds no code, recommends useful slices that can be
worked on and reviewed separately and identifies possible parallel work independently of the
chosen execution skill, while the orchestrator records before execution whether that opportunity
can be used, from dependencies, shared files or mutable state, separate review and the skill's
restrictions; each slice is made by an agent of its own, and a slice that proves too large for it
is discarded with its code and goes back to the planner to be split. A one-author change and
every slice are reviewed by an agent that did not make them, and a change of more than one slice
then gets one review of the whole change, while the review of a one-author change or of a plan's
only slice is the review of the whole change; the one-author review also checks coverage of the
task, every row of its *Settlements to record* and every projected entry it carries, and that
foundation entries precede the code that depends on them.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** observation of installed Superpowers 6.4.1 on 2026-10-10 using `sed -n` and
  `grep -n` in Git Bash on Microsoft Windows NT 10.0.26300.0; source root
  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`:
  `writing-plans/SKILL.md` — "Each step is one action (2-5 minutes)" and, under "No
  Placeholders", "Steps that describe what to do without showing how (code blocks required for
  code steps)"
- **Relations:** derives from WAY-13@e6c830b7 · derives from WAY-69@7051f884 · derives from
  WAY-126@35accf8b · derives from WAY-134@2fc974a9
- **Verification:** level 2 — an agent compares the cycle and any plan with the decision:
  - complies: the orchestrator selects one author from a settled task, including its foundation
    entries, without first writing a plan; the author does its return step and another agent's
    whole-change review checks task, settlement and projected-entry coverage and foundation order;
    an invariant's sentence, check and code have different authors; a reviewed spec is followed by
    the same size judgment; an oversized author's attempt and its foundation entries are discarded
    before planning; a change of several slices has each reviewed and then one whole-change review,
    while a plan's only slice needs no duplicate review; an outgrown slice is discarded and split;
    a plan identifies independent slices although the execution skill forbids parallel executors,
    and the orchestrator records sequential execution with that restriction; shared mutable state
    prevents a proposed parallel run;
  - violates: a small task needs a plan merely because it writes foundation entries or follows a
    spec; the orchestrator writes a plan to decide whether to omit it; the code author also writes
    the invariant sentence or check; an author reviews its own work, or its whole-change review
    omits the coverage and order checks because there was no plan; an oversized author's entries
    survive its discarded attempt; a plan holds code or uses Superpowers `writing-plans`; outgrown
    slice code is kept; the planner suppresses useful independent slices because of the execution
    skill or creates unnecessary slices to claim parallel work; the orchestrator treats different
    files alone as proof of independence or overrides the skill's restriction.
- **Review when:** five cycles of `implement-task` have run under this decision, or a one-author
  change has been returned as too large in two cycles out of three, or a cycle has returned more
  than one slice in three of its plan as too large · check by: 2026-11-30
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* a plan earns its cost by dividing a change into work an agent can hold and a reviewer
can read separately; where the change fits an author, repeated reading and handoffs add cost
without adding a check of the finished change. The risk is that the author fits its foundation to
its code; independent review and assessment, together with separate invariant authors, keep that
choice open to challenge. An incorrect size judgment costs an abandoned attempt, and discarding
its entries as well as its code keeps the later division from inheriting a failed shape. A useful
division outlives the restrictions of an execution method, while the execution ruling prevents
work whose dependencies or shared state make parallel execution unsafe.
*Rejected:* a plan for every change, including a small plan used only to choose the route — it
charges for division where none is needed; lighter preparation only for changes leaving the
foundation unchanged — foundation work is common and does not itself require division; lighter
review, assessment or gate for a small change — size does not establish that its meaning stayed;
small work outside the task cycle — duplicate rules of the record, request and return step drift;
Superpowers `writing-plans` — code written ahead still needs review; a whole-change review after
the review of a plan's only slice — it reads the same range again; an outgrown attempt kept and
completed — its division would be written around unfinished work; a plan shaped only by the
execution method — it hides useful independent work; parallel execution from different file names
alone — shared state and dependencies can still join the work.

### WAY-137/1 — What decides between places to run that the simplest and cheapest option leaves tied?

Where the options of a place to run differ in no consequence for the product and more than one of
them is the simplest and cheapest, the step that settles a project's technology recommends, of
those, the one an agent works with best: operated from a terminal, deployed by a script and
documented in pages an agent can read. For a place to run, how well an agent works with an option
decides nothing else: it leaves no option out of the comparison and is weighed against no
consequence for the product.

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18 · narrows WAY-123@f3b45293
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: two hosts that cost the same and take the same upkeep remain after the simplest and
    cheapest rule, and the one with a command-line tool and a deployment script is recommended; a
    host with no command-line tool stays in the comparison and is recommended where it costs less
    than the others;
  - violates: a host whose deployment cannot be scripted is left out of the comparison for that
    reason; a host is recommended over a cheaper one because an agent can operate it from a
    terminal; the table of consequences scores how well an agent works with each host beside its
    cost.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/14

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

### WAY-138/1 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?

The step that settles a project's technology tests the option it recommends for each choice it
settles, one a constraint of the definition settles included, with a devil's advocate, a pre-mortem
and a search for unknown unknowns; it tests no choice a decision of the foundation holds, and no
decision already written is tested afterwards. The risks these tests give are hypotheses with no
source, not differences claimed between options, so the critique of the comparison does not strike
them, and they stand in the table beside the option recommended before the human chooses. The human
who chooses that option takes its risks, and each risk taken reaches the decision of that choice in
its *Rationale*, beside the lacks of the option chosen, marked as a hypothesis.

- **Change:** new decision
- **Scope:** project-level, decisions
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-122@b343277a · derives from
  WAY-123@f3b45293
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: a project settles its store of data and its place to run, the table shows beside each
    option recommended the risks the three tests gave, each marked as a hypothesis, and the human
    who takes the recommended host finds those risks in the *Rationale* of its decision beside its
    lacks; a framework the definition names as a constraint is tested; a language a decision of the
    foundation holds is not;
  - violates: the critique strikes a risk from the table for want of a source; the risks are shown
    only after the human has chosen; every option of a choice is tested; an agent tests a decision
    written before the project and adds risks to it; a risk taken reaches the decision's *Based on*
    as a fact.
- **Review when:** the tests run on choices other than a place to run give no risk that the
  comparison of their choice did not already show · check by: 2026-12-31
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/14

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
project. Every choice the project settles is tested until the tests show they find nothing outside
a place to run.
*Rejected:* tests on every option of a choice — their cost grows with options the human mostly does
not take; the risks shown after the choice — the human takes them unseen; the risks put through the
critique as claims — with no source, every one would be struck; the risks in *Based on* — it names
facts with sources, and a risk read there passes for one; an entry of its own for each risk —
assumptions as a kind of entry escape checking (WAY-04); tests on choices decisions of the
foundation hold — they reopen what was settled.

### WAY-139/1 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?

The-way holds no skill of a product, only the list of what a product's deployment skill covers: a
preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of
steps and what happens to the data; what the agent does and what the human does; and how to read the
logs. When a task's outcome deploys the product or changes how or where it runs, the-way's skill
`refine-task` checks, while it refines the task, that the product has a deployment skill covering
every item of the list, and where it has none or an item is missing, the task gains an item of its
To do for that work or the human splits that work into a task of its own.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares the work with the decision:
  - complies: refining a task that moves the product to another host finds that the product's
    deployment skill says nothing of rollback, and the task gains an item of its To do that adds
    it; a task that sets up the product's first deployment finds no deployment skill, and the human
    splits writing one into a task of its own; a task that changes the text of a page is refined
    without the check;
  - violates: the-way carries a deployment skill for one kind of host; a task that changes where
    the product runs reaches its cycle with a deployment skill that does not say where the secrets
    lie, and with no item or task for it; the list stands only in a template, and the decision
    points to it.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/14

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

### WAY-140/1 — How does a task change something outside the product's repository?

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

- **Change:** new decision
- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-107@0ffcebe1 · derives from
  WAY-125@441e3a6a
- **Verification:** level 2 — an agent compares the task document, or the cycle, with the
  decision:
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
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/14

*Rationale:* an effect outside the repository is not undone by resetting a branch and does not show
in the diff the human reviews, so the human who makes it sees what it changes; named in the task
document, each human action is known before the cycle rather than found when the work stops on it.
The request is the cycle's single point of human review (WAY-125), so a human action that uses the
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

### WAY-141/1 — How does the installer give Claude Code the guidance in a product's root AGENTS.md?

When a product has no root `CLAUDE.md`, the installer creates one whose sole line is `@AGENTS.md`,
so Claude Code receives the installer's block and the product's other instructions from root
`AGENTS.md`. When a root `CLAUDE.md` already exists without an effective `@AGENTS.md` import, the
installation plan warns about the missing import, and the installer leaves every existing root
`CLAUDE.md` untouched. The installer writes no `.claude/rules/the-way.md`.

- **Change:** new decision
- **Scope:** installation
- **Based on:** claude-code-imports@5b9359fd · claude-code-agents-md@e4007cb8
- **Relations:** none
- **Verification:** level 1 — invariants: installation-claude-guidance.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/15

*Rationale:* importing the shared instructions gives Claude Code the product's backlog location
as well as the installer's guidance through one route. An existing file may hold product guidance,
so the installer reports a missing import before confirmation and leaves the file to its owner.
*Rejected:* a generated rule repeating the installer's block — it duplicates guidance without
carrying the product's other instructions; adding the import to an existing file — it changes
product-owned guidance without its owner's choice.

### WAY-142/1 — What does the breakdown of a project write, and in what form?

The breakdown of a project writes its plan as one document beside the approved definition, whose
header names the definition and the fingerprint the definition's gate record holds, and whose
`Status:` line says whether the plan is still a draft or has been handed to the human. Each task
stands in one row of one table of tasks, with the columns and states the plan template gives, while
the tasks that realize each projected entry and the one task that writes it into the foundation
stand in a table of their own, a row for each entry under the heading the definition gives it. The
plan also holds each open question of the definition, word for word, with where it is resolved, its
phases with what closes each where it has any, and a log of its changes, each with its reason,
written in the language of the definition under headings, states and markers kept in English.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-118@5af868b3 · derives from
  WAY-100@e7a74a18
- **Verification:** level 1 — invariants: project-plan-form. Level 2 for what the plan holds beyond
  its form — an agent compares the plan with the decision:
  - complies: the plan of a Polish definition gives each task's goal in Polish under English
    headings, its header carries the fingerprint the gate recorded, and the projected decision
    `(new) — Who owns a document?` stands in the table of entries with tasks 3 and 5 realizing it
    and task 5 writing it;
  - violates: a task stands in the table and again under a heading of its own repeating its
    fields; the goals of a Polish definition's tasks stand in English; a phase names no condition
    that closes it.
- **Review when:** every task of the first plan this step writes reads `done` or `dropped —
  approved by human` · check by: 2027-01-31
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/16

*Rationale:* a plan changes with every move of a task, a definition rarely and only through its
gate, so the two stand apart, and the fingerprint in the plan's header shows when the definition
beneath it has changed. One row per task keeps each fact about a task in one place, where no copy
can drift from it. A definition can project many entries, its decisions named only by their
question; listed in the row of every task that realizes them, they would fill a cell no one reads
and need short keys made up for them, while a row per entry under its own heading is matched to the
definition word for word and shows in one cell the single task that writes it. The columns and the
states stand in the template, so that a change to them needs no new version of this decision. The
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
decision — each change of a column would take a new version.

### WAY-143/1 — What does a task of a project plan end with?

A task of a project plan ends with something that can be checked in the running product, never with
a layer of the product put in place; a preparatory task stands in the plan only where a task of the
plan depends on it, the task it opens the way for. A technical element enters the plan with the
first task that uses it, or with a preparatory task that task depends on.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 1 — invariants: project-plan-check. Level 2 for what a task ends with and
  where a technical element enters — an agent compares the plan with the decision:
  - complies: a task "the player opens the forest and sees it on a grid of hexagons" also brings in
    the first data files of the game; a preparatory task puts the empty application on the test
    server, and the task of player accounts depends on it; in the-way, a task ends with
    a skill a session runs on a real definition;
  - violates: a task "the database schema" ends with tables no screen reads; a preparatory task
    sets up logging for the whole product for later use and no task depends on it; the store of data enters
    in a task before the first task that saves anything.
- **Review when:** every task of the first plan this step writes reads `done` or `dropped —
  approved by human` · check by: 2027-01-31
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/16

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

### WAY-144/1 — How does a project plan show which tasks can be worked on side by side?

The dependencies of a project plan constrain the start of a task's cycle, not its refinement: a
task starts its cycle only when the tasks it depends on are done, while refinement waits for
another task only where a question of that refinement needs its result. Two task cycles can run
side by side when neither task depends on the other, directly or through other tasks. The plan
holds no field naming the tasks a task can be worked on beside, and its order of cycle starts
follows the dependencies.

- **Change:** new decision
- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-100@e7a74a18
- **Verification:** level 1 — invariants: project-plan-form. Level 2 for cycle starts and refinement waits — an
  agent compares the plan, or the work on it, with the decision:
  - complies: two cycles start together because neither task depends on the other and their
    dependencies are done; two dependent tasks are refined together, with only a question needing
    an unfinished result waiting for its named task; a task needing a saved state lists the task
    that adds saving among those it depends on;
  - violates: a task carries a field naming a dozen tasks it can be worked on beside; tasks are
    ordered by a goal picked in an interview against their dependencies; a task starts its cycle
    before a dependency is done, or refinement waits for every dependency without a question
    requiring those results.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* the dependencies already say which tasks can go together; a second field derived from
them is a copy that drifts as soon as one dependency changes, and its lists grow long enough that
nobody reads them. The rule takes from the practice of a roadmap its graph of dependencies and the
order that follows from it, and leaves out its field of work that can run alongside. The task
order WAY-106 gives the plan is this order of cycle starts. Refinement can settle a dependent task
before its prerequisites are delivered; only a question needing their result earns a wait.
*Rejected:* a field naming the tasks a task can be worked on beside — a copy of the dependencies
that grows past reading; the order tilted by a goal the human picks in an interview before the plan
— the definition already states the goal and its risks, and the human corrects the finished plan.

### WAY-145/1 — Who sets where an open question of an approved project definition is resolved?

Once a project definition has passed its readiness gate, the place of resolution it gives an open
question is the question's first assignment, and the plan decides from then on where the question
is resolved: in a task of the plan, or by an answer the human gives or the plan quotes, with its
place, from the definition or the foundation. Work on the plan may move a question to another task,
with an entry in the plan's log of changes giving the reason and without taking the definition
through its readiness gate again, while a move that changes which task writes a projected entry
into the foundation is the human's to decide. A question that arises only in the breakdown goes to
the human before the plan is handed over.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-118@5af868b3 · derives from
  WAY-126@35accf8b
- **Verification:** level 1 — invariants: project-plan-check. Level 2 for moves, answers and new
  questions — an agent compares the plan with the decision:
  - complies: the breakdown moves the question on a session's secret from the task of the test
    server to the task of accounts, where sessions first exist, and writes why in the log of
    changes; the breakdown finds that nothing says whether the test server is public from the first
    account and asks the human before handing the plan over;
  - violates: a question lands in another task than the definition names with no entry in the log;
    the definition is edited and gated again to move a question; a move that hands the writing of a
    projected decision to another task is made without the human; the breakdown answers a question
    from its own reading of the code; a question found in the breakdown waits in a task as an
    unknown.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/16

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

### WAY-146/1 — What checks a project plan before it is handed over?

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

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-120@81f84997
- **Verification:** level 1 — invariants: project-plan-form · project-plan-check. Level 2 for the
  critique — an agent compares the work with the decision:
  - complies: the critique finds a task ending with tables no screen reads and a question placed in
    another task than the definition names with no line in the log, while the script reports a
    projected decision no task writes;
  - violates: the critique is asked whether every item of In scope has a task; the plan reaches the
    human with a question the script would have found unplaced; the agent that wrote the plan
    judges its own tasks.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/16

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

### WAY-147/1 — How is a task of a project plan named, and what does its cycle take from the name?

A project plan gives each of its tasks a name of lower-case words joined by hyphens, which no other
task of the plan holds and which stays with the task while the plan changes. A task of the plan
enters its cycle under that name, and the cycle names its record by it.

- **Change:** new decision
- **Scope:** project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 1 — invariants: project-plan-form. Level 2 for the cycle — an agent
  compares the cycle with the decision:
  - complies: the task `forest-on-hex-grid` of a plan keeps its cycle record under
    `docs/task-cycles/forest-on-hex-grid/`;
  - violates: the cycle of a task of a plan names its record by a name it makes up; a task's name
    changes when its goal is reworded; a plan carries a second table of its tasks with titles for a
    tracker.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/16

*Rationale:* a task's cycle record and its entry in the product's backlog meet its row in the plan
through its name, so a name that changes leads a reader to the wrong work; words, because a number
that keeps the plan's own cells short says nothing in a record read apart from the plan. The rule
takes from the practice of a roadmap the stable name each of its items carries into later work. Where the product keeps its backlog is its own choice (WAY-107), and a task's entry
there links its document, so the plan needs no table of its tasks written for a tracker.
*Rejected:* the cycle naming its record when it starts — the plan and the record name one task
differently; the plan's number as the name — it says nothing where it is read; a table of the
plan's tasks with titles for a tracker — a second copy of the tasks, which the product's backlog
already holds.

### WAY-148/1 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports
directory, while its messages carry routing, stage status, paths, commits, a concise check result
and every unresolved concern affecting the next dispatch. The orchestrator records the event and
relevant choices before dependent dispatch and reads authoritative sources and relevant report
evidence before deciding a question, settling a finding, accepting a foundation meaning or
verifying disputed or incomplete evidence; routine progression uses the short return, record,
source paths and commits without requiring prior conversational history. A missing or incomplete
report is repaired before dependent work proceeds, and this transfer contract preserves required
whole-source reads, check and review duties and the independent assessor's filtered inputs
(WAY-10), reusing a borrowed method's existing brief and report rather than duplicating them.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-125@441e3a6a · derives from WAY-10@db68de1c
- **Verification:** level 2 — an agent compares the stage handoff, return, report and
  orchestrator's ruling with the decision:
  - complies: a short return names its complete report, commit range and failed or unchecked
    checks, and the record permits resumption from files; the orchestrator reads the evidence
    of an unresolved question before deciding it; a missing report is repaired before the next
    dependent dispatch; a required whole entry is read whole;
  - violates: a full report exists only in conversation, a short return conceals a failed check,
    dependent work proceeds on a missing report or mismatched commit range, or a question is
    settled from the short return alone; a selective read replaces a mandatory whole-source
    read; the independent assessor receives the operational handoff or author's reasoning.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/17

*Rationale:* full material kept outside routine coordination avoids repeated context while
preserving evidence a ruling needs and a place from which work can resume. Short returns make
the next action visible, but an omitted failure can hide behind brevity, so relevant evidence
remains part of a decision and an incomplete report blocks dependent work.
*Rejected:* full handoffs and reports repeated in messages — coordination accumulates material
it need not reread; short summaries as the only record — lost evidence cannot be recovered on
resumption; a second universal brief and report contract — duplicated obligations drift without
proving completeness; automatic compaction — it does not choose the evidence a ruling needs.

### WAY-149/1 — When does the deliberate break of a return-step check take place?

For an invariant check added in a task's return step, its first acceptance deliberate break
follows the one independent assessment of the change's foundation entries and invariant tests
and the settlement of its remarks. Before that break, affected checks and code review run again
for a settlement that changes code, assessed foundation entries or invariant tests, and the code
reviewer who did not write the check reviews its final version, writes the break from the final
invariant sentence and records the required failure (WAY-08, WAY-69); later corrections to the
check or the behaviour its break covers repeat the affected verification before the final clean
run. Checks written earlier in the cycle retain their existing acceptance and deliberate-break
points, and settlement stays part of the one assessment (WAY-10), with an existing affected
review reused where it covers the final check rather than adding a whole-change review of an
unchanged range.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-10@db68de1c · derives from WAY-08@2343e09f · derives from
  WAY-69@7051f884
- **Verification:** level 2 — an agent compares the cycle's check, assessment, settlement,
  review and deliberate-break evidence with the decision:
  - complies: a return-step check runs on the product, its assessment's remarks are settled,
    affected checks and review run again, and the code reviewer reviews the final check and
    records its failure on a break written from the final sentence; an earlier check keeps its
    original acceptance point; a later correction repeats the affected evidence;
  - violates: a return-step check is accepted on a break before assessment, or on a passing
    product run alone; a changed final check uses a superseded break's evidence; assessment
    replaces code review, settlement reopens assessment, or an earlier check's break is delayed
    to the return step.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/17

*Rationale:* settling assessment remarks before the first acceptance break avoids repeating a
break for a check the settlement changes. A final check still needs independent review and a
real failure on the rule it protects; changing the order cannot turn a product pass or an
assessment into that evidence. Earlier checks keep the failure evidence their own stage needs.
*Rejected:* breaks both before and after assessment by default — the earlier run may check a
version that is immediately replaced; delaying every check's break — earlier stages lose their
own acceptance evidence; accepting a check after assessment alone — an approved check may still
detect no break; a second whole-change review of unchanged work — it repeats an existing review.

### WAY-150/1 — How do the-way skills choose which product foundation material to read?

The-way skills default to selective reading of the product's foundation: they use the complete
part map and existing entry links to choose material for the work, read selected entries whole,
and expand the reading whenever the work or an uncertain relevance needs more context.
The selection includes every current decision whose Scope names a touched part, including parts
identified from proposed work before a file diff exists, and decisions the work explicitly names.
Required whole-foundation searches and mandatory whole-source, template and example reads retain
their domain and timing; selection is checked against all current Scope fields and refreshed when
the work or foundation changes.

- **Change:** new decision
- **Scope:** elements-common, decisions, invariants, glossary, part-map, environment-facts,
  project-level, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-21@586e4a38 · derives from WAY-33@65f8dda4
- **Verification:** level 2 — an agent compares the reading and its selection record with the
  work and current foundation:
  - complies: a project with no diff uses the complete map to name affected parts, inspects all
    current Scope fields including wrapped values, reads every matched decision whole, follows
    an incoming dependent and a relevant invariant naming every part, and expands after a
    whole-foundation search finds a conflict outside those parts;
  - violates: only decisions already named by the task are read; a search hit replaces its whole
    entry; a required source is reduced to selected excerpts; selection is reused after the
    foundation changes without checking for newly applicable decisions.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/18

*Rationale:* a growing foundation contains more material than each piece of work needs, while
unconditional loading spends attention on unrelated rules. Selection from responsibilities and
links keeps the governing material visible, and expansion addresses relevance that no known link
captures; the cost is judgment about context and evidence that the selection covers its domain.
*Rejected:* unconditional whole-foundation loading — its context cost grows with unrelated work;
selection only from known links or keywords — a governing decision or an unlinked conflict can
remain unseen; a fixed reading limit — a difficult case loses needed context; a separate maintained
index — a second account can drift without resolving semantic relevance.

### WAY-151/1 — How much of large project definitions and existing plans does plan-project read?

The-way's plan-project limits reading of large project definitions and existing plans to the
material needed for the work, starting from complete inventories of scope items, projected entries,
open questions and existing tasks and their dependencies and assignments, then reading complete
source units and expanding whenever their meaning or dependencies reach further.
A new breakdown covers every scope item, projected entry and open question, and a resumed change
reads all units its dependencies or meaning reach, with the original whole documents remaining
the inputs to the existing readiness and plan checks.
The plan's one independent critique reads the complete plan and every source unit needed for its
whole semantic judgment under WAY-146, independently of the author's selection.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-146@7677c3cd
- **Verification:** level 2 — an agent compares the reading, inventories and verification record
  with the authoritative definition and plan:
  - complies: resuming an unfinished plan inventories all tasks, assignments and exact questions,
    then reads a distant dependency and projected-entry writer that affect the resumed work;
    whole-original checks run and the critic reads the whole plan with all needed sources;
  - violates: only nearby rows are inspected and a distant dependency is missed; a readiness or plan
    check receives a reduced copy; a new breakdown omits a scope item; the critic's review is
    bounded by the author's excerpts or leaves some tasks and questions unjudged.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/18

*Rationale:* large project documents hold context for many tasks, while resumed work usually
changes only some of it. Complete inventories expose distant assignments and dependencies before
context is selected, and whole verification protects the complete project; the cost is careful
expansion whenever meaning reaches beyond the initial selection.
*Rejected:* reading every large source whole at every resumption — unrelated context is loaded
repeatedly; reading only the unfinished section — distant dependencies and settlements disappear;
checking reduced copies or limiting the critic to selected material — omissions can agree with
the reduced input and pass unseen; maintaining a second plan for reading — copies drift.

### WAY-152/1 — How does the project orchestrator lead a handed-over plan?

The project orchestrator leads a handed-over project plan from tasks to refine to human-accepted
tasks ready for their cycles and keeps the plan's states consistent with evidence, proposing a
round of refinement first from tasks on which the most other tasks depend for the human to
confirm or change. The human starts task cycles separately, and when the last task is done the
project orchestrator names project closure as the next step and says that no closure skill
exists, without performing either work. After a task merges, leading the plan does not recheck
ready dependent task documents: the task cycle checks and adapts its sources at its own start.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-106@63eddf70 · derives from WAY-124@4fbad55c · derives from
  WAY-144@d5802c22
- **Verification:** level 2 — an agent compares the leading session with the decision:
  - complies: the human changes a proposed round, the project orchestrator coordinates its refinement
    and maintains evidenced states, and the human starts a ready task's cycle separately;
  - violates: leading launches a cycle, closes the project, or re-refines every ready dependent
    task after a merge instead of leaving the cycle's source check to its start.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* the human needs one conversation that keeps a plan moving and its progress visible.
Keeping task execution and closure separate bounds that conversation, while checking current
sources where implementation begins avoids repeating a check whose inputs can change again.
*Rejected:* leading that also executes cycles and closes the project — distinct work obscures the
point where the human starts implementation; automatically reopening ready dependants after each
merge — repeated refinement can be invalidated again before implementation.

### WAY-153/1 — What evidence supports a task state in a project plan?

At each leading session's start a Git-only state reader uses existing recorded task provenance
to establish that cycle traces belong to the current plan's task and proposes, with exact
evidence, ready for cycle to in cycle from such a matching working cycle directory in a
Git-listed worktree or a commit touching that task's exact archived cycle directory, and in
cycle to done from such a cycle-record commit reachable in the product's freshly fetched
integration history, composing both transitions when the plan is still ready for cycle. The
reader changes no plan or task document, establishes the product's integration ref without
guessing, and exposes absent or incomplete evidence, operational failures and conflicting traces
without unsupported progress; missing or ambiguous task provenance is unchecked and contradictory
task provenance goes to human reconciliation, with neither supplying progress. The project
orchestrator applies supported transitions with a reason and evidence in the plan's log,
resolves outcomes Git cannot establish through the product's chosen PR tool or asks the human
when that tool is absent, and brings a closed-unmerged PR or a trace conflicting with the plan
to the human without automatically correcting the plan.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-38@6e10c3fd · derives from WAY-142@e53cd0ac · derives from
  WAY-147@8cfe543f
- **Verification:** level 1 — invariants: project-plan-state-evidence ·
  project-plan-state-subprocesses. Level 2 for applying proposals and resolving PR outcomes —
  an agent compares the evidence and leading session with the decision:
  - complies: the project orchestrator applies supported transitions with a reason and evidence
    in the plan's log, resolves an unchecked PR outcome through the product's chosen PR tool,
    and shows a closed-unmerged PR to the human without automatic correction;
  - violates: the project orchestrator treats an unchecked observation as completion without
    resolving it, silently normalizes a conflicting trace, or guesses the PR outcome when the
    product's PR tool is absent instead of asking the human.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* evidence-backed progress prevents a stale plan from hiding delivered work without letting
an uncertain observation claim delivery. Separating observation from the plan write keeps the
human-facing judgment visible; unresolved host outcomes cost a lookup or a question.
*Rejected:* a state reader that also queries the PR host — it couples observation to a host-specific
executable; inferring completion from a local trace — unfinished or abandoned work looks delivered;
automatically normalizing conflicts — a plausible state hides the discrepancy the human needs.

### WAY-154/1 — How do agents exchange a project task refinement and keep its result?

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

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-124@4fbad55c · derives from WAY-142@e53cd0ac · derives from
  WAY-144@d5802c22 · derives from WAY-147@8cfe543f
- **Verification:** level 2 — an agent compares the turns, task documents and plan with the decision:
  - complies: parallel refiners write separate documents, a fresh refiner keeps each settled
    answer and source, and interrupted acceptance resumes without guessing human agreement;
  - violates: the project orchestrator rewrites a task body or carries questions in prompts,
    an agent's readiness stands for human acceptance, or cleanup loses the only settled answer.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* a file-mediated exchange keeps the project orchestrator from becoming a content relay
and lets another session resume. The retained task document carries the result that later work
needs; ownership and serialized turns cost explicit coordination but prevent competing edits.
*Rejected:* conversation contents relayed in prompts — each transfer repeats context and can lose
answers; retaining the temporary exchange as the task result — later work reconstructs settlements
from discussion; deleting the exchange before durable transfer — provenance disappears.

### WAY-155/1 — What may the answering agent settle during a refinement round?

The answering agent answers a refinement question only with a quotation and source from the
definition, plan, foundation or other task documents, or with a factual code observation naming
file and line; a question about how the product is to be is answered only from a document, never
from code or the agent's inference. It reads the round's conversations, makes an unanswered
choice a question to the human with options, costs and a recommendation, and brings the same
question to the human once while preserving its affected tasks. The project orchestrator
presents one round package of these questions, candidate settlements, placement of Human actions
and complete wording, together with every quotation answer as question, quotation and source; a
quotation answer the human strikes becomes a question to the human, whose answers return to the
conversations before fresh refiner turns.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-113@d3e5cbfa · derives from WAY-134@2fc974a9 · derives from
  WAY-140@6e564611
- **Verification:** level 2 — an agent compares questions, answers, sources and the human package:
  - complies: a code observation settles current behavior, a documented choice settles intended
    behavior, and a rejected quotation returns once as a human question for all affected tasks;
  - violates: code or an inference supplies a requirement, a quotation answer is hidden from the
    package, or two tasks ask the human the same choice separately.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* an answer grounded in a source saves the human from restating an existing settlement,
while distinguishing observation from prescription prevents accidental behavior becoming a rule.
Showing quotation answers costs attention but lets the human reject an answer that fails its
question; one shared question avoids repeated decisions.
*Rejected:* free inference by the answering agent — a plausible conclusion appears settled;
code as authority for intended behavior — an accident becomes a requirement; hiding quotation
answers until final approval — the human cannot inspect the basis of the refined tasks.

### WAY-156/1 — How does project leading route a plan or definition change?

An in-scope task split, new task, order or dependency change is delegated to a plan-project
agent and logged with its reason, while a scope change and a reassignment of the task writing a
projected entry go to the human. The project orchestrator changes definition text itself only
when that text is already before it and needs no reading of other definition sections or the
foundation; otherwise it delegates the edit, and a subagent always performs the definition's
readiness gate, with independent critique dispatched by the project orchestrator and its
findings returned to that subagent, and human approval given through the project orchestrator. A
fresh subagent then checks the plan again through plan-project step 0, and no task gains ready
for cycle while that definition gate remains open.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-118@5af868b3 · derives from WAY-120@81f84997 · derives from
  WAY-145@4312fd6b
- **Verification:** level 2 — an agent compares the edits, gate, critique and rechecked plan:
  - complies: a local text edit is made from material already read, a subagent completes the
    full gate, the human approves through the project orchestrator, and a fresh agent checks
    the plan before readiness resumes;
  - violates: a wider definition edit is made without delegation, the project orchestrator runs
    its gate itself, or a task becomes ready against a changed but unapproved definition.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/19

*Rationale:* a project can change direction while refinement proceeds, but its approved definition
is the basis of every task. Keeping the full gate and fresh plan check costs another review while
preventing readiness against an obsolete basis; a narrow edit exception avoids needless handoff
for text already available without making leading responsible for wider execution.
*Rejected:* every definition edit performed by the project orchestrator — it takes on execution and
additional context; every local edit delegated — a transfer costs more than the already bounded
edit; bypassing the gate for a small change — size does not establish that its meaning stayed.
