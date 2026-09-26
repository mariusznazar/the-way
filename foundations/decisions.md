# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and, on the main branch, are only ever appended.

### WAY-01/1 — What state does the foundation describe?

On the main branch, the foundation describes the product as it is: its rules, together with
the listed debt wherever the product does not yet meet them. A task starts implementation by
changing the foundation, and the code follows; when the task closes, the
foundation again matches the current state. Roadmaps and plans do not change the foundation.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** specifications written separately for each change go unread: in a reported
  case of 238 such specifications over nine months, none was reopened, and the agent could not
  tell which were current (Alfredo Perez,
  https://www.alfredo-perez.dev/blog/2026-08-31-i-wrote-238-specs-and-never-read-one-again).
- **Relations:** none
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task changes the foundation entry first, the code follows, and both reach the
    main branch together;
  - violates: a planned feature is written into the foundation before it is built; the
    foundation is updated only after deployment.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-14

*Rationale:* a foundation that describes intent ages with every change of direction, and no
comparison with the code reveals it, because such a document is expected to differ from the
code. A foundation that describes the current state can be checked against the working product
at any time. The order works like test-driven development on a broader scale: the foundation
changes first, and the code follows.
*Rejected:* the foundation as a description of the target product; the foundation updated
only after deployment — a step at the end of a task is the kind of step that goes missing.
*Consequences:* every task that changes what the product does begins with a step that changes
the foundation. Plans, roadmaps and hypotheses need a home outside the foundation. Where a rule
of the foundation is not met on the main branch, what the foundation carries is the rule and a
listed violation, never a weakened rule (WAY-51).

### WAY-02/1 — How do dependents learn that an entry has changed?

Every foundation entry has a permanent identifier, and everything that depends on it — other
entries, tests, documents and code comments — refers to that identifier. A reference that relies
on the entry's current wording carries its content fingerprint (`WAY-17@<fingerprint>`), and
when the fingerprint changes, a script working on plain text files flags that reference for
review; a bare identifier and a reference to a version (`WAY-17/2`) are never flagged. The fingerprint covers
only the part of an entry that binds — for a decision, its binding sentences.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model
- **Based on:** none
- **Relations:** none
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-guard-stale-reference ·
  decision-fingerprint-input · log-reference-target · relation-fingerprint-value.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* without a mechanism, following a change through everything that depends on it
rests on a written rule and on memory. A product can hold hundreds of references to its entry
numbers, and after an entry changes nothing shows which of them went stale. A permanent identifier
with a content fingerprint lets a script find the stale ones, as Doorstop does. The fingerprint
covers only what binds, because a fix to a rationale does not change what dependents rely on,
and flags raised for nothing teach people to clear them without reading. Not every reference
relies on the wording: a passing mention follows the entry, and a record of work done under an
earlier version must not be flagged at all.
*Rejected:* propagating changes only through impact analysis by a language model — nobody
knows what it missed; a fingerprint over the whole entry — every fix to a rationale would flag
all references; a single kind of reference — a historical record would be flagged like a test.
*Consequences:* tests, documents and code comments that rely on an entry's wording cite it with
a fingerprint. Every foundation element needs a defined binding part, so that its fingerprint can
be computed.

### WAY-03/1 — Who may change an invariant's test, and when?

Invariant tests are written and accepted together with the foundation change, and during
implementation they are read-only. A mechanism outside the model enforces this: a local hook,
and in the merge request a CI check that rejects any change to an invariant test without an
accepted foundation change. A task that needs an invariant test changed goes back to the
foundation step.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** agents that a test stands in the way of change the test instead of the code,
  and Claude models do so especially readily: read-only tests are "a promising middle ground
  especially for Claude models, largely due to their preference of directly modifying test
  cases" (ImpossibleBench — Zhong, Raghunathan, Carlini, 2025,
  https://arxiv.org/abs/2510.20270; quote from the authors' summary,
  https://www.lesswrong.com/posts/qJYMbrabcQqCZ7iqm/impossiblebench-measuring-reward-hacking-in-llm-coding-1).
- **Relations:** derives from WAY-01@a291c2c0 · related to WAY-02
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-test-change-acceptance.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-14

*Rationale:* an agent that a test stands in the way of adjusts the test to the code: the build
turns green, and the foundation lies. Keeping invariant tests out of the implementer's reach
removes that move instead of forbidding it.
*Rejected:* a written rule "do not change the tests" — a gate written in prose is not a gate.
*Consequences:* the CI check has to tell invariant tests from other tests; it recognises them
by the invariant they cite (WAY-02). Even a change of form — a selector, test data, waiting —
goes through the foundation step and its acceptance.

### WAY-04/1 — What elements make up a product's foundation?

A product's foundation has five elements, and the list is closed: invariants, decisions, a
glossary of product terms, a part map, and environment facts. A new pattern enters the
foundation only as a field or a rule of one of the five, and only when a mechanism keeps it
without human memory: a test, a lint, a gate, a mandatory relation or configuration.

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

*Rationale:* each element holds what no other can. Invariants are what a task must not break.
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
environment an agent runs, and the step that carries findings out of a task's log (both belong
to the task cycle); a criticality map as a separate element (criticality is a field of a part);
external constraints as a field of the map (a constraint is an environment fact, and the
obligation it creates is an invariant); product principles and non-goals as a separate kind of
entry (they are decisions like any other); diagrams and an ARCHITECTURE.md written by hand (a
second copy of the map); environment facts as hypotheses in the backlog (they are true or false
today); assumptions as a kind of entry — anything inconvenient could be called an assumption and
escape checking, and a mandatory condition for disproving it with a review date narrows that way
round without closing it.
*Consequences:* each element is described in `elements/<element>/` of the process repository;
the description grows into the element's template as the element goes through its steps. Every
picture of the architecture — a diagram, a description — is generated from the part map and the
code, and is made for a human on request; no such picture is generated into an agent's context
(WAY-52).

### WAY-05/1 — How is a decision entry written?

A decision entry opens with one to three binding sentences — in the present tense, describing
a state that is to be true, concrete enough to check — followed by fields a script or an agent
reads, then rationale, rejected options and consequences in prose. A field stays in the template
only while someone or something reads it. A rule in `elements/decisions/` changes only with a
decision, and an example there copies a version from the log word for word.

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
  decision-example-copy · decision-template-change. Level 2 for the rule that every field has a
  reader — an agent compares the change with the decision:
  - complies: a new field enters the template together with the reader named in its table;
  - violates: a "notes" or "related artifacts" field that nothing reads.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* norms keep what binds short and checkable and put the explanation next to it; a
record written like a legal code, in a commanding voice, reads badly and is followed worse.
Agents generalise from the reasons they are given, so the reasoning stays in the entry, below
what binds. The present tense is used because a sentence with "will" or "should" describes an
intent, not a state. Fields are few because a field survives in practice only when someone reads
it in a specific activity. The template is the process's code:
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

### WAY-06/1 — Where does a foundation change in progress live?

A foundation change in progress lives on the task's branch in the product's repository and
reaches the main branch in the same merge as the code that follows it.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@a291c2c0 · related to WAY-03
- **Outranks:** none
- **Verification:** level 1 — invariants: foundation-change-merge-route. Level 2 for the rule
  that the change travels with its code — an agent compares the change with the decision:
  - complies: a task branch changes a decision entry and the code that follows it, and both
    reach the main branch in one merge;
  - violates: a task's foundation change is merged to the main branch ahead of its code; the
    code is merged and the foundation change is left for a later task.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* the main branch never describes something the product does not have (WAY-01), and
an abandoned task leaves no false description behind: its foundation change is dropped with its
branch.
*Rejected:* a foundation change kept on the main branch with a "designed, not built" marker —
the marker has to be removed when the task closes, and an abandoned task leaves a marked entry
for good.
*Consequences:* a change with no code behind it — a fix to a rationale, a decision recovered
from the existing product — also reaches the main branch through a task branch. A file conflict
catches two tasks that change the same entry in contradictory ways, but contradictory changes to
different entries merge cleanly; the search against the current main branch before the merge
(WAY-33) is what catches them. A merge into the main branch keeps a merge commit: a squash or a
rebase puts the task's commits on the main branch's first-parent history as ordinary commits,
and the level 1 invariant reads them as commits that reached it without a merge.

### WAY-07/1 — From when may a decision entry no longer be edited?

An entry in the decision log is corrected in place until it reaches the main branch; until then
it gets no new version and no new decision about it. A correction that changes the meaning of an
accepted entry is accepted again. Once an entry is on the main branch, it is never edited, and
the log there only grows at the end.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-06@fe7c4068 · related to WAY-05
- **Outranks:** none
- **Verification:** level 1 — invariants: log-existing-lines · log-versions-added-per-number. Level
  2 for acceptance after a change of meaning — an agent compares the change with the decision:
  - complies: an accepted entry whose binding sentences changed on the task branch is shown to
    its approver again before the merge;
  - violates: an entry reaches the main branch with binding sentences its approver never saw.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* an entry binds only once it describes the product on the main branch (WAY-01,
WAY-06); before that it is part of a change in progress. Versions written on a task branch would
carry into the log states that never bound anything. On the main branch the log keeps what was in
force, as it was, so there it only grows. *Approved by* is a trace of what a human accepted; after
a change of meaning without a new acceptance, it would name someone who did not approve what the
entry says.
*Rejected:* an entry fixed from the moment it is written — every correction made during a task
becomes a version that never bound anything.
*Consequences:* the format guard compares the log with the commit the task branch left the main
branch from, not with the previous commit. Until this log reaches the main branch, its entries are
corrected in place. A copy in `examples.md` follows its version when the version is corrected.

### WAY-08/1 — How is an invariant checked?

Every invariant names its method of checking, and its current result comes from running that
method, never from a status written by hand. The default method is a test in the broad sense —
a code test, an end-to-end test or an exploratory test run by an agent on the working product —
and a test counts only when a deliberately introduced break of the invariant makes it fail, in k
of n runs for a test that does not give the same result every time. Human inspection is used for
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
*Consequences:* an invariant test is accepted only after a deliberate break has made it fail, so
the quality gate needs a way to introduce such breaks. An invariant that no test or measurement
can settle stays in the foundation, checked by a person.

### WAY-09/1 — What may enter the process repository?

On the main branch, this repository holds `foundations/` with the entries of the-way itself, a
directory for each part of the process other than `repository` — `elements/<element>/` for each
foundation element, `relation-model/`, `gate/` and `task-cycle/` — the files that serve the whole
repository, which its part map gives to the `repository` part (WAY-44), and a `README.md` that
describes the repository. A directory reaches the main branch only once it holds what its part
requires: an element its template and rules, examples, a skill that writes its entries and a
script that checks them; the relation model the script that computes fingerprints; the gate the
test of every critical flow in the part map; `task-cycle/` what the design of the task cycle
sets, and until then it does not reach the main branch. The entries in `foundations/` are checked
by the scripts of their elements.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model, gate,
  repository, task-cycle
- **Based on:** none
- **Relations:** related to WAY-02 · related to WAY-04 · related to WAY-06 · related to WAY-21 ·
  related to WAY-44 · related to WAY-55
- **Outranks:** none
- **Verification:** level 1 — invariants: repository-file-location · element-directory-contents ·
  relation-model-directory-contents.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* the repository shows what the process looks like when it works, and an artefact
brought in on the side turns it into a store of material from the first day. Directories follow
the parts of the process, so that the files a change touches name the part it belongs to and the
decisions to check it against (WAY-21). What a directory must hold depends on its part, because
each tool has a reason only where it has work: a skill writes entries, so it belongs to an
element; the fingerprint script only reads, so the relation model has no skill. The skill writes
an entry in the right form when someone runs it; the script catches a form broken by hand, by
another agent or by a merge. Until a directory holds what its part requires, it is a change in
progress, and under WAY-06 such a change lives on a branch. The files that serve the whole
repository belong to no one part of the process, and WAY-44 gives them a part of their own; they
stay where the tool that reads them looks for them, and the map, not this list, names which they
are. The `README.md` binds nothing and only tells a reader what the repository is.
*Rejected:* material merged to the main branch as soon as it is written; an element whose only
tool is a skill — the form then holds only while someone remembers to run it; one `tools/`
directory for everything shared — it matches no part of the process and grows into a store; the
same set of template, skill and script required of every directory — a script that only reads has
no entries for a skill to write; the files that serve the whole repository on the map's list of
files left out on purpose, beside the `README.md` — they would lose their part and the failure
mode recorded at it, although a wrong line in `.gitattributes` turns whole files over.
*Consequences:* element descriptions in `elements/` reach the main branch as templates with their
skills and scripts, not as descriptions. The script for references and fingerprints (WAY-02,
WAY-31) lives in `relation-model/`. The quality gate is a part of the process of its own, with a
directory of its own (WAY-55), and what `task-cycle/` must hold is set when the task cycle is
designed. The map's rule for assigning files follows these directories, and a file that serves the
whole repository added later — the CI configuration, once the gate runs in CI — enters by a change
to the `repository` part of the map, not by a new version of this decision.

### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation is assessed by a panel of three agents: two
assess it independently, each from a different, named perspective and seeing only the diff and
the foundation, never the author's reasoning, and the third, on a different model where one is
available, settles between them. The panel decides changes of an invariant test's form — how the
test reaches the product: selectors, test data, waiting, never a rerun set outside the method's
command. Every other change the panel prepares with the diff, its effects and a recommendation, and
a human decides.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** a model assessing text is biased towards its own: "an LLM evaluator scores its own
  outputs higher than others' while human annotators consider them of equal quality"
  (Panickssery et al., 2024, https://arxiv.org/abs/2404.13076).
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
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* the problem is a single executor that checks itself. Agents on the same model with
the same input share its blind spots, so independence comes from a different perspective, from
not seeing the author's reasoning, and from a different model for the agent that settles. Only a
human knows what the product is meant to guard, so every change to what the foundation says goes
to a human.
*Rejected:* a panel that settles everything; a single agent without a panel.
*Consequences:* the CI check from WAY-03 accepts a change to an invariant test only with the
panel's record, and, beyond a change of form, only with a human decision. Changes waiting for a
human grow with the number of tasks, and nothing yet limits how many may wait.

### WAY-11/1 — How does a task end?

A task ends with a return step before its branch is merged: an agent lists from the diff and the
task's log what the foundation does not say — new rules and decisions, code behaviour with no
invariant over it, environment facts the change rests on — proposes it to the panel as a foundation
change, and compares the foundation with the code in the parts the task touched. A periodic review
of the foundation runs apart from tasks.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@a291c2c0 · related to WAY-06 · related to WAY-10 ·
  related to WAY-17
- **Outranks:** none
- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step finds
  — an agent compares the change with the decision:
  - complies: a rule the implementer wrote into the code for an edge case comes back as a
    proposed invariant before the merge;
  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
    invariant covers.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* part of the foundation is learned only in implementation and in use. Agreement
between the foundation and the code has to be checked, because a task that missed the foundation
will not report it by itself. A step at the end of a task is the kind of step that goes missing
(WAY-01), so the merge waits for its record. Environment facts are on the list because otherwise
they reach the foundation only when an invariant pulls them in, while the assumption that failed
Ariane 5 sat in code with no invariant over it (WAY-17).
*Rejected:* the foundation changed only at the start of a task; mechanical signals in the diff
that point to a fact — a new dependency, a new import, a browser interface, an address, a value
arriving from outside — built into the return step now, ahead of the design of the task cycle.
*Consequences:* the task's log needs a home, because the return step reads it. Comparing the
foundation with the code in the parts a task touched needs the part map's rule for assigning
files. How often the periodic review runs is set when the task cycle is designed. Until then the
return step finds facts by the agent's judgment, and an agent seldom notices one on its own; the
mechanical signals above are an input to that design.

### WAY-12/1 — How is a decision checked?

A decision is checked through the invariants derived from it, and tests live only with
invariants. Where no invariant can be derived today, an agent compares a change with the decision
using a pair of examples — one that complies and one that violates — and where an agent cannot
judge, a human assesses it and leaves a trace of who and when. A decision can combine levels,
each covering the part of its binding sentences it can check.

- **Change:** new decision
- **Scope:** decisions, invariants
- **Based on:** language models judge only part of what decisions say: "The models achieved
  substantial agreement and strong accuracy for explicit, code-inferable decisions. Accuracy falls
  short for implicit or deployment-oriented decisions that depend on deployment configuration or
  organizational knowledge" (Su, Bakhtin, Ahmad, Esposito, Lenarduzzi, Taibi, 2026,
  https://arxiv.org/abs/2602.07609).
- **Relations:** related to WAY-05 · related to WAY-08
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-verification-level ·
  level-one-decision-invariants · invariant-citation-target · verification-invariant-derivation.
  Level 2 for the choice of level — an agent compares the change with the decision:
  - complies: a decision on the product's direction is checked by an agent with a complying and a
    violating example;
  - violates: a decision whose rule a lint check could enforce is left at level 2.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* an invariant is true or false on every commit, so a test can check it; a decision
about direction, trade-offs or non-goals often cannot be checked on a commit. Agents compare a
change well with a decision that is explicit and readable from the code, and fall short on
decisions that depend on deployment or on knowledge of the organisation — those stay with a human.
A pair of examples shows the agent where the line runs, which the binding sentences alone do not.
*Rejected:* a rule in code as the only method of checking a decision — decisions that cannot be
written as a rule would stay unchecked.
*Consequences:* the section "Verification" of the decision template is the written form of this
decision. A derived invariant is named in *Verification* by the identifier of its entry in the
product's invariants file. A decision moves to level 1 once an invariant is derived from it.

### WAY-13/1 — What sets the weight of a task's process?

What a task touches, never its size, sets its process: an agent's analysis at the start of the
task settles whether it changes the foundation, which chooses its path, while three things set
how sharply it is checked — the criticality of the parts it touches, as the part map computes
it, whether it touches the files of a trust boundary, and whether the change can be undone.
Paths differ in their steps, never in the result a task has to reach; a task's size serves only
as a signal to split it, and an agent may check a change more sharply than the map computes,
never less. A human decides on every change that cannot be undone.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** formal approval does not make changes safer: "No evidence was found to support
  the hypothesis that a more formal, external review process was associated with lower change
  fail rates" (DORA, https://dora.dev/capabilities/streamlining-change-approval/). Changes that
  cannot be undone call for a different process: they are "consequential and irreversible or
  nearly irreversible – one-way doors – and these decisions must be made methodically,
  carefully, slowly, with great deliberation and consultation" (Jeff Bezos, 2015 letter to
  shareholders,
  https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm).
- **Relations:** related to WAY-01 · related to WAY-04 · related to WAY-10 ·
  related to WAY-46 · related to WAY-48
- **Outranks:** none
- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line change to a stored data format, after which users' saved data no
    longer loads, goes through the sharpest checks and waits for a human's decision;
  - violates: a task gets the heavier path because of the number of lines it changes; a change
    that cannot be undone reaches the main branch without a human's decision.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* size misleads both ways: a change across many files can be a mechanical rename
that is easy to undo, while a one-line change to a stored data format can destroy the data of
every user. How much process a task needs depends on what can go wrong: whether the task changes
what the product is meant to be, how serious a failure of the parts it touches is, and whether
the change can be taken back. Paths differ only in their steps, because a light path allowed a
weaker result becomes a way around the process. Size still matters as a signal: a large task is
split, so that each part can be checked and undone on its own. A human's attention goes where
only a human can decide, to a change that cannot be taken back.
*Rejected:* one cycle for all tasks; choosing the path by the task's size; a human approving
every diff — formal review does not lower the rate of failed changes, and it spends a human's
attention where it adds nothing.
*Consequences:* every task starts with an agent's analysis of whether it changes the
foundation. The criticality it reads is the value the part map computes (WAY-46), and the files
of a trust boundary come from that same map (WAY-48); what nothing defines yet is a way to
recognise a change that cannot be undone. The paths and their steps, and the number of degrees
the criticality scale needs, are set when the task cycle is designed.

### WAY-14/1 — Who approves a version of a decision?

Who approves a version of a decision is set by a process rule for the parts in its scope; the
entry names an approver, in *Approver override*, only when that rule does not apply to it. Every
version records who approved it and when.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** the UK government's decision record framework sets the level at which a decision
  is made from the reach of its impact — a team's decision is "Local to a single team or working
  group", with "No impact on other teams or shared platforms" — and its record has no field for
  an owner (Architectural Decision Record Framework, GOV.UK,
  https://www.gov.uk/government/publications/architectural-decision-record-framework/architectural-decision-record-framework).
- **Relations:** related to WAY-05 · related to WAY-07 · related to WAY-10 · related to WAY-13
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-approval-record · decision-approver.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* an approver written into every entry repeats the same name across the log and goes
stale when people change roles, while a rule for each part changes in one place. An entry names
someone only as an exception, so an exception stands out instead of drowning among repeated
names. The record of who approved and when is what a human considering a change reads, and what
WAY-07 needs when an entry has to be accepted again.
*Rejected:* an approver named in every entry — the same name repeated, stale once the team
changes; lists of decision-makers and of those consulted — nothing reads them.
*Consequences:* the section "Approval" of the decision template is the written form of this
decision. The rule that names the approver for each part has no home yet; until it has one, the
format guard checks only that every version records who approved it and when, as
`<who>, YYYY-MM-DD` — `TODO` there is an error — and every version in this log is approved by
Mariusz. Nothing yet settles who approves a decision whose scope spans parts with
different approvers. This decision covers decisions only; approval of other foundation entries is
set when their elements are designed.

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

The quality gate takes its checks from the methods of checking written in the entries, never
from a list written by hand, and runs the checks a change calls for with one command, the same
command for an agent, CI and a human.

- **Change:** new decision
- **Scope:** invariants, task-cycle
- **Based on:** none
- **Relations:** related to WAY-08 · related to WAY-13 · related to WAY-15
- **Outranks:** none
- **Verification:** level 1 — invariants: ci-checking-commands · gate-check-source. Level 2 for the
  same command for everyone — an agent compares the change with the decision:
  - complies: the instructions for agents name the gate's command as the way to check a change;
  - violates: the instructions for agents list test and lint commands of their own.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* a list of checks written by hand — in the CI configuration, in the instructions for
an agent, in a person's habits — is a second copy of the list of invariants, and each copy
drifts on its own: a new invariant is never run, a removed one still is. A gate that reads the
methods from the entries runs exactly what the foundation says, and one command for everyone
removes the question of which list someone ran. Under WAY-08 the current result of an invariant
comes from running its method; the gate is what runs it.
*Rejected:* a gate written for each product — it drifts from that product's invariants;
separate commands for an agent, CI and a human — three lists to keep in step; running every
check on every change — it leaves no room for checking a change as sharply as what it touches
calls for (WAY-13).
*Consequences:* every method of checking is written in a form the gate can read. How the gate
reports a method it cannot run, such as an inspection by a human, is set by WAY-63. Which checks a change calls for is set when the task
cycle is designed. Under WAY-55 the gate is a part of the process of its own and reaches
the main branch in `gate/`.

### WAY-17/1 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends
on the other, and none is optional: a decision and an invariant name the environment facts they
rest on, an invariant derived from a decision names that decision, and an invariant test names
its invariant.

- **Change:** new decision
- **Scope:** relation-model, decisions, invariants, environment-facts
- **Based on:** an assumption about the world that no entry names escapes review: the inquiry
  into the failure of Ariane 5 found that "this decision was found directly in the source code.
  Given the large amount of documentation associated with any industrial application, the
  assumption, although agreed, was essentially obscured, though not deliberately, from any
  external review" (Ariane 501 Inquiry Board, ESA,
  https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report).
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-04 · related to WAY-12
- **Outranks:** none
- **Verification:** level 1 — invariants: level-one-decision-invariants · invariant-citation-target
  · verification-invariant-derivation.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* the chain is the path a change travels: when a fact about the world changes, the
decisions and invariants resting on it come up for review, and through them their tests. A link
missing anywhere breaks the path without a sign, because nothing shows which dependent should
have been reached. The link is written in the dependent entry, as every reference is (WAY-02):
whoever writes an entry knows what it rests on, while the entry it rests on cannot know what will
be built on it. Research findings about agents and models are environment facts of this process
like any other — the world around the product, true today and liable to change.
*Rejected:* links written by the entry that others depend on — it cannot know what will be built
on it; optional links — a link never written cannot be told from one that is not needed;
research findings kept as evidence outside the environment facts — the decisions of this process
about agents would have no fact to be flagged by.
*Consequences:* until the environment facts element has entries, a decision quotes its facts
with their sources in *Based on*; once it has them, which citations become fact entries, and how
*Based on* names one, is set by WAY-90. On the main branch, a fact learned after a decision is added to it by a field change.
A decision's *Verification* names its level 1 invariants by the identifiers of their entries
(WAY-12), and each of those entries names the decision in *Derives from*.

### WAY-18/1 — How are the history of decisions and what is in force kept apart?

The decision log holds every entry in the order it was written, and what is in force today is a
view that a script generates from the log: the latest version of each number, and in place of a
repealed decision a single line pointing to the version that repealed it. A link between entries
is written at one end only, and the view shows it at the other.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** Python's decision process keeps the settled record apart from the current
  description: "a PEP is considered a historical document rather than a living specification",
  and "Formal documentation of the expected behavior should be maintained elsewhere, such as the
  Language Reference" (PEP 1, https://peps.python.org/pep-0001/). Polish rules for consolidated
  legal texts keep the place of a repealed provision with a pointer: its designation and the word
  "repealed" are entered, with a note giving the title of the repealing act (Zasady techniki
  prawodawczej, § 106, own translation,
  https://www.senat.gov.pl/gfx/senat/userfiles/_public/k10/kancelaria/wydawnictwa/pdf/zasady_techniki.pdf).
- **Relations:** related to WAY-05 · related to WAY-07 · related to WAY-15 · related to WAY-17
- **Outranks:** none
- **Verification:** level 1 — invariants: view-versions · view-links.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* the history of a decision and the statement of what holds today serve different
reads: whoever wants to change a decision needs its versions and reasons, while an agent checking
a change works from what is in force and reaches the options rejected earlier through the
history. One document edited in place loses the history; one document that only grows buries the
current state. A mark written by hand at the other end of a link is the kind of step that goes
missing, because nobody reopens an old entry when a new one refers to it, so each link is written
once and the generated view shows both ends.
*Rejected:* a single document edited in place — the history is lost and nothing shows what
changed when; a log without a view — every reader reconstructs the current state by hand; marks
written by hand at the other end of a link — they go missing.
*Consequences:* the opening paragraph of the decision template, its rule that entries are
appended in the order they are written and its rule on who writes a relation are the written
form of this decision. The view script does not exist yet; until it does, what is in force is read from the log as the
latest version of each number. The end that writes a link is the entry that depends on the other
(WAY-17), for relations between decisions as for links between elements.

### WAY-19/1 — How are decisions numbered and versioned?

A number stands for the question a decision answers, carries the product's prefix and is given
in the order entries are written; a new question gets the next free number, and a new rule next
to an existing decision is a new question, related to its neighbour. On the main branch, every
change to a decision is a new version of its number, which points to the version before it,
gives the rationale for the change and restates the binding sentences, fields and consequences
in full, except that a repeal has no binding sentences. When a new decision answers a question
that an older one answered in passing, the sentence moves to the new decision, and the older one
loses it — by a new version on the main branch, by a correction before it.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** legislative drafting restates a changed provision whole and forbids a change
  hidden in a new provision: under the Polish rules of legislative drafting, an amended provision
  is cited "in its full new wording", and an amendment may not replace an old provision with a
  new one "without indicating at the same time that this change is being made" (Zasady techniki
  prawodawczej, §§ 87(1) and 86, own translation,
  https://www.senat.gov.pl/gfx/senat/userfiles/_public/k10/kancelaria/wydawnictwa/pdf/zasady_techniki.pdf).
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-07 · related to WAY-18
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-heading-form · decision-version-sequence ·
  decision-change-rationale. Level 2 for one number per question and for sentences answered in
  passing — an agent compares the change with the decision:
  - complies: once on the main branch, a new rule for who approves a version of a decision is
    written as WAY-14/2; when a decision on a question arrives, an older decision that answered
    it in passing loses that sentence;
  - violates: the same question gets a second number; a version carries only the sentence that
    changed; the sentence stays in both decisions.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a permanent number lets references survive a change (WAY-02): a reference that
relies on the wording is flagged by its fingerprint, and the rest follow the decision. A new
number for every change would force every reference to be rewired, or leave it pointing at a dead
entry, and the current answer would be reached through a chain of replacements. Each version
restates the decision whole, so no reader assembles it from pieces. A sentence answered in
passing moves to the decision that now answers its question, because two entries answering one
question drift apart, and a change to one of them hides a change to the other. The prefix keeps
numbers of different products apart in references, and numbers carry no topic, so nothing is
renumbered when topics shift.
*Rejected:* a new number for every change, with the old entry marked as replaced — references
must be rewired or stay with a dead entry; numbering by topic — topics move, and numbers would
have to move with them.
*Consequences:* the section "Numbers and versions" of the decision template and its rule on the
prefix are the written form of this decision. The reasoning behind a decision is spread over its
versions, so the view has to reach a decision's earlier versions through a history line.

### WAY-20/1 — What kinds of change can a decision undergo?

Every version after the first names its kind of change from a closed list: editorial correction,
rationale change, field change, new wording, narrowing, challenge, replacement, repeal. A
rationale change, a field change and a challenge keep the binding sentences of the previous
version word for word, and a repeal has none.

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
  - complies: a version that answers the question anew is called a replacement; a typo fixed in
    a binding sentence is called an editorial correction, and a human confirms that the meaning is
    unchanged;
  - violates: a version called an editorial correction turns "must" into "may"; a whole new
    answer is called a new wording.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a version has to say what it does to the decision, because everything that relies
on the decision needs that first: a fixed typo leaves every reliance valid, a new answer does
not, and a replacement leaves work built on the old answer to be dealt with. A word for a change
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
rationale change, since the consequences are part of the reasoning and leave the fingerprint
unchanged.

### WAY-21/1 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never
file paths, so that the decisions governing a change are found from the files it touches through
the part map's rule for assigning files.

- **Change:** new decision
- **Scope:** decisions, part-map, task-cycle
- **Based on:** an agent loses rules as their number grows: "even the best frontier models only
  achieve 68% accuracy at the max density of 500 instructions" (IFScale,
  https://arxiv.org/abs/2507.11538), and a tool vendor advises keeping an agent's instructions
  short for the same reason: "target under 200 lines per CLAUDE.md file. Longer files consume
  more context and reduce adherence" (Claude Code documentation,
  https://code.claude.com/docs/en/memory).
- **Relations:** related to WAY-04 · related to WAY-11 · related to WAY-13 · related to WAY-14
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-scope-names · decisions-found-for-change.
- **Review when:** none
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

An invariant is a sentence about the product that is true or false on every commit and says
nothing about why or what was rejected; a decision is a choice between options, with its
rationale, and it binds later choices, including those that cannot be checked on a commit —
direction, trade-off principles, non-goals. A rule that records a choice is a decision, and what
of it a commit can make false is written as an invariant derived from it; a rule with no choice
behind it is an invariant alone.

- **Change:** new decision
- **Scope:** decisions, invariants
- **Based on:** none
- **Relations:** related to WAY-04 · related to WAY-08 · related to WAY-12 · related to WAY-17
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "the product has no multiplayer" is a decision with its reason, and "no screen
    offers a second player" is an invariant derived from it; "a saved game is never lost on
    reload" is an invariant with a test;
  - violates: a non-goal that a commit can break is left without a derived invariant; an
    invariant carries a rationale and rejected options.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* the two are read differently: an invariant is checked mechanically on every commit,
while a decision is weighed when a later choice is made. A checkable rule left only in a
decision's prose escapes the gate, and a choice written only as an invariant loses its reasons.
When a rule is both, each part goes where it is read: the choice and its reasons stay in the
decision, and the checkable sentence becomes an invariant that names it.
*Rejected:* one kind of entry for both — either the gate reads prose or the reasons are lost;
moving a checkable sentence out of its decision — the rule would be cut off from its reason.
*Consequences:* the section "Decision or invariant" of the decision template, apart from its
plan test, which belongs to WAY-36, and its last rule, which belongs to WAY-12, is the written form
of this decision. An invariant derived from a decision is named by its identifier in the
decision's *Verification* (WAY-12).

### WAY-23/1 — How many decision logs does a product have?

A product keeps all its decisions in one log, whatever they are about.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** long-lived document series keep different kinds of decisions, approved in
  different ways, in one series: "Various contributors provide input to the RFC Series. These
  contributors come from several different communities, each with its own defined process for
  approving documents that will be published by the RFC Editor" (RFC 8729,
  https://www.rfc-editor.org/rfc/rfc8729.html), and Python's series holds process documents next
  to technical ones — "A Process PEP describes a process surrounding Python, or proposes a change
  to (or an event in) a process" (PEP 1, https://peps.python.org/pep-0001/).
- **Relations:** related to WAY-14 · related to WAY-18 · related to WAY-21
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a business rule and a technical constraint of one product stand in the same log
    under one numbering; a product that arrives with a folder of architecture records keeps it as
    a source and writes a decision recovered from it into its log when a task first touches the
    parts that decision governs;
  - violates: a separate log for business decisions next to the technical one.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a collision between a product decision and a technical one is caught only when both
are in the set a change is checked against; two logs each look consistent while contradicting
each other. A topic needs no log of its own: the scope selects which decisions to check (WAY-21),
and who approves follows from the parts in scope (WAY-14), so the reason other processes split
their logs — different approvers — needs no second log. The log of this process is separate from
the logs of the products built with it, because they are separate products.
*Rejected:* separate logs for business and technical decisions — collisions between them go
unseen; a field for the topic of an entry — nothing reads it (WAY-05).
*Consequences:* the rule in the decision template that the log has no topical sections is the
written form of this decision. Decision records a product already has when the process enters it
are a source for inherited decisions, not a second log. The decisions of this process bind every
product without standing in its log: a product reads them from the commit of the-way it pins
(WAY-34), and which of them a task is checked against is set when the task cycle is designed
(WAY-21).

### WAY-24/1 — How is a decision that rests on a prediction reviewed?

A decision that rests on a prediction names in *Review when* the predicted state of the world or
the product, observable when it comes, and a check-by date; the field does not lift the decision,
and the agent working in its scope checks whether the state has come. On the date, a review entry
records the result: the state has not come, with the next date; it has come and the decision is
kept; or it has come and a named version changed the decision.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** a criterion for revisiting a bet works when it is concrete and timed: "The best
  quitting criteria combine two things: a state and a date" (Annie Duke,
  https://behavioralscientist.org/annie-duke-quit-mental-models-to-help-you-cut-your-losses/).
  An end date written into a rule does not by itself bring the rule to an end: "More often than
  not, despite the inclusion of a sunset clause, legislation has been renewed for a longer period
  of time than the original sunset clause or even made permanent" (Westminster Foundation for
  Democracy, 2022,
  https://www.wfd.org/sites/default/files/2022-01/2022-01-18%20PLS%20sunset%20clauses%20-%20final.pdf).
- **Relations:** related to WAY-07 · related to WAY-17 · related to WAY-18 · related to WAY-19 ·
  related to WAY-20
- **Outranks:** none
- **Verification:** level 1 — invariants: review-when-form · decision-guard-overdue-review ·
  review-next-check · review-named-version.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a decision that rests on a prediction is a bet, and a state with a date turns "we
will see" into something someone checks. The field never ends the decision by itself: an end
date written into a rule is more often extended than acted on, so here the date only asks for a
look, and the look is recorded. Each review names what was observed, so a run of "not yet" shows
as such instead of being renewed in silence. A review is an entry of its own and not a version,
because a version restates the whole decision (WAY-19), and a look that changed nothing would add
a full copy of it.
*Rejected:* a decision that expires on a date — the date is extended rather than acted on; a
review date without a state — nobody knows what to check; a review written as a new version — a
full copy of the decision for every look that changed nothing.
*Consequences:* the section "Review" of the decision template, apart from its last sentence,
which belongs to WAY-31, is the written form of this decision. A passed check-by date without a review is a
warning of the format guard; until the view exists, dates still to come are kept only by the skill
and by whoever reads the log. Before the main branch, whether a passed date is answered with a review
entry or with the date corrected in place is not yet settled (WAY-07).

### WAY-25/1 — What settles a collision between two decisions?

Precedence between decisions is recorded pair by pair in *Outranks*: a decision names the
decisions that give way to it when both apply and collide, nothing follows along a chain, and two
decisions that outrank each other are an error. A collision between two decisions with no
precedence recorded is never settled by the agent that meets it; a human records the precedence
in one of them — by a new version on the main branch, by a correction before it.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** related to WAY-07 · related to WAY-14 · related to WAY-20
- **Outranks:** none
- **Verification:** level 1 — invariants: outranks-pairs. Level 2 for a collision with no precedence
  — an agent compares the change with the decision:
  - complies: an agent meets two applicable decisions that pull opposite ways, finds no
    precedence between them, stops and asks for it;
  - violates: an agent settles the collision in favour of the newer decision; an agent infers
    that A outranks C because A outranks B and B outranks C.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a ranked list of principles claims an order between pairs that never meet, and
every new principle has to be placed against all the others; pairs record only what someone
actually weighed. Nothing follows along a chain, because A over B and B over C were weighed in
different situations and say nothing about A and C. An agent that settles an unrecorded
collision itself makes a trade-off no human made. One person records the precedence, so that one
person answers for the trade-off when it is questioned.
*Rejected:* one ranked list of principles, as in organisations that keep no more than seven
tenets "in descending order of priority" (AWS,
https://aws.amazon.com/blogs/enterprise-strategy/tenets-supercharging-decision-making/) — an
order claimed for pairs nobody weighed; levels of authority over whole groups of decisions — a
collision inside a level stays unresolved; the newest decision wins — the date of a decision is
not its weight.
*Consequences:* the field *Outranks* and the rules on precedence in the decision template — in
"Relations and precedence" and in the sentence on precedence between principles — are the
written form of this decision. When a new decision is less important than an existing one, the
existing one gets the new number in its *Outranks*: by a field change on the main branch, by a
correction before it. `narrows` stays for a decision that deliberately goes against another in a
narrower area; *Outranks* is for two decisions that both apply. What the agent does once it has
stopped is set by the rules for a change that contradicts a decision.

### WAY-26/1 — How are trade-off principles and non-goals written?

Each trade-off principle is a decision of its own, whose binding sentence says which of two good
things is chosen when they conflict and whose rationale names the problem it solves. Each
non-goal is a decision of its own that says what the product does not do and why; non-goals
exist only at product level, and a task's exclusions stay in the task's plan unless they outlive
the task.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** a principle guides only when both sides are worth having: principles of this kind
  weigh "two things that could be entirely good choices" (The Uncertainty Project,
  https://www.theuncertaintyproject.org/tools/even-over-statements), and "A tenet takes a stand by
  declaring that a team cares more about one thing than another" (Kindel,
  https://blog.kindel.com/2020/02/10/tenets/). Exclusions made for one piece of work carry that
  work's reason: "No-gos — Anything specifically excluded from the concept: functionality or use
  cases we intentionally aren't covering to fit the appetite or make the problem tractable"
  (Shape Up, https://basecamp.com/shapeup/1.5-chapter-06).
- **Relations:** related to WAY-04 · related to WAY-11 · related to WAY-22 · related to WAY-25
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "When speed of release conflicts with completeness of a feature, we choose speed",
    as an entry of its own, with a rationale naming the problem it solves; "The product has no
    multiplayer", with its reason, as an entry of its own;
  - violates: a principle naming one good thing only ("we value quality"); several principles or
    several non-goals in one entry; an exclusion that ends with its task written into the log as
    a product non-goal.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a principle rules later choices only when it names what it gives up; a sentence in
favour of one good thing decides nothing. The rationale names the problem, so that a later reader
can tell when the principle has stopped serving it. Each principle and each non-goal is an entry
of its own, so that each one changes on its own, with its own reason, and so that precedence can
be recorded between principles pair by pair (WAY-25). A task's exclusions end with the task,
while a product's non-goals hold until they are changed, so only the latter belong in the log.
*Rejected:* several principles or non-goals in one entry — a change to one flags them all, and no
precedence can be recorded between them; every task exclusion in the log — most expire with their
task and bury the product's non-goals.
*Consequences:* the section "Trade-off principles and non-goals" of the decision template, apart
from its sentence on precedence between principles, which belongs to WAY-25, is the written form
of this decision. A non-goal that a commit can break gets an invariant derived from it (WAY-22).
A task's exclusion that turns out to outlive the task comes back through the return step (WAY-11)
as a non-goal. A task's plan has no home in the process yet (WAY-01).

### WAY-27/1 — Where may this repository point for its reasoning?

Nothing in this repository points to a source outside it that its readers cannot reach: every
entry carries its whole reasoning, and a fact seen only in such a source is described in the
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
to trust a claim that cannot be checked. The reasoning therefore travels with the entry, and a
fact seen where readers cannot look is written down as what was seen, so that it can at least be
judged, and WAY-17 still has a fact to name.
*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader of the
repository can open them.
*Consequences:* *Origin* in this log is `none` or points to a document its readers can open. The
entries written before this one already follow it. Products built with this process are not
bound by this decision; their logs may point to their own documents.

### WAY-28/1 — How does the process enter a product that already exists?

When the process enters a product that already exists, the existing state is its starting point
and needs no justification, and the rules apply to changes from then on. The part map with
criticality comes first; the invariants of critical parts are then recovered from what the
product does — an agent lists what a part does, and a human chooses which of it the product must
keep — and the other invariants come through the return step of tasks. Decisions are recovered
only when a task touches the parts they govern.

- **Change:** new decision
- **Scope:** decisions, invariants, part-map, task-cycle
- **Based on:** checking an existing product against a description written long after its code
  is slow and can fail outright: MongoDB reports "10 weeks of effort without successfully
  trace-checking one spec" (MongoDB engineering blog,
  https://www.mongodb.com/company/blog/engineering/conformance-checking-at-mongodb-testing-our-code-matches-our-tla-specs).
- **Relations:** related to WAY-01 · related to WAY-04 · related to WAY-11 · related to WAY-13 ·
  related to WAY-15 · related to WAY-23
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: on entering a product, the part map comes first, and the invariants of a critical
    payment flow are chosen by a human from the agent's list of what the flow does; a decision is
    recovered when a task first touches the parts it governs;
  - violates: an agent turns everything a critical part does today into invariants without a
    human's choice; an agent recovers from the code decisions for the whole product before any
    task touches them; the critical parts wait for a task like any other.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* matching a whole product to a description written after the fact is slow, and it
tempts an agent to write reasons that look like decisions, so decisions wait until a task needs
them. Critical parts cannot wait, because a break there is expensive (WAY-13), so their
invariants come first. A human chooses among what they do, because only a human knows what the
product is meant to guard, and what it does today is a state, not yet a rule (WAY-15). Invariants
and decisions are separate lists: an invariant needs no decision above it, so a recovered
invariant can bind before anyone knows why it holds.
*Rejected:* recovering the whole foundation at the start — slow, with reasons invented where none
are known; everything on demand, the critical parts included — a break there is found only when
a task happens to touch them.
*Consequences:* an invariant recovered from behaviour needs a method of checking and the note
WAY-58 sets, recording what was searched and what was found for or against keeping it, which
the invariants template carries as the field *Recovered*.
A decision recovered for a task is written as the section "Inherited decisions" of the decision
template says, and decision records the product already has are read as sources when their parts
are touched (WAY-23).

### WAY-29/1 — How is a decision recovered from an existing product written?

A decision recovered from an existing product records in *Origin* what was searched and what was
found, and its rationale and rejected options are quoted from that source, given by a human who
knows them, or written as `unknown`. A rationale an agent proposes goes to a human as a question,
never into the entry.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** rationales written by language models match those given by experts only in part:
  "the Precision of LLM-generated DR with the three prompting strategies ranges from 0.267 to
  0.278" (Zhou et al., https://arxiv.org/abs/2504.20781). A reconstructed record is easily taken
  for a real one: "The retroactive ADR has the form of the decision record but not the
  substance" (Catio, https://www.catio.tech/blog/architecture-decision-record).
- **Relations:** related to WAY-06 · related to WAY-10 · related to WAY-23 · related to WAY-28
- **Outranks:** none
- **Verification:** level 1 — invariants: inherited-origin-form · inherited-rationale-source. Level
  2 for the agent's part — an agent compares the change with the decision:
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
enters by a new version on the main branch, by a correction before it.

### WAY-30/1 — What happens when a change contradicts a decision?

A change to a decision that a task needs is written into the task's plan and approved with it by
the decision's approver. When a contradiction shows only during implementation, the agent stops,
quotes the decision by its number, and either brings the change into line, drops the change, or
proposes on the task branch a new wording, a narrowing or a replacement of the decision — by a
new version on the main branch, by a correction before it — and the code that needs it waits for
the decision's approver. An exception written in advance into a decision's binding sentences is
not a contradiction, and no exception lives only in a task's plan.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** tools that guard principles in agent work refuse a quiet way around them:
  "Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or
  tasks—not dilution, reinterpretation, or silent ignoring of the principle" (GitHub Spec Kit,
  https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md).
- **Relations:** derives from WAY-01@a291c2c0 · related to WAY-03 · related to WAY-06 ·
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
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* an exception kept only in a task's plan leaves the foundation describing something
the code no longer does (WAY-01). Stopping makes the contradiction visible at the moment it is
found. The agent may bring its change into line or drop it on its own, because both leave the
decision as it is; changing the decision is for its approver, and the code waits for that, as the
foundation comes before the code (WAY-01). A narrowing keeps the decision for everything outside
the exception, and a narrowing made for a situation that may pass carries *Review when*, so that
someone looks at it again (WAY-24). An exception foreseen in the binding sentences is part of the
decision, so acting on it contradicts nothing.
*Rejected:* a justified violation recorded in the plan without a change to the decision, as Spec
Kit's plan template allows — the foundation stops matching the code; a replacement as the only
way to change the decision — a narrow exception would take the whole decision with it.
*Consequences:* the rule on exceptions foreseen in advance in the section "Binding sentences" of
the decision template is part of the written form of this decision. The task cycle needs a step
in the plan for changes to decisions, and a task's plan has no home in the process yet (WAY-01).
When the contradiction is a collision between two decisions with no precedence recorded, the
agent stops and asks for the precedence (WAY-25). Checking an implementation against decisions
needs the decisions in the scope of the change (WAY-21).

### WAY-31/1 — Which relations between decisions are flagged when the named decision changes?

A relation `derives from` or `narrows` relies on the wording of the decision it names and carries
that decision's content fingerprint (`derives from WAY-01@<fingerprint>`), while `related to` is a
plain identifier. A change to a decision's fingerprint reaches the main branch together with
every decision that relates to it with a fingerprint, each checked against the new wording and
carrying the new fingerprint.

- **Change:** new decision
- **Scope:** decisions, relation-model
- **Based on:** requirement tools that keep traceability between items store the state of the
  parent in each link: "Each link consists of the parent item UID and the fingerprint of the
  parent item. When the fingerprint of a parent item changes, the link is reported as suspect
  during validation" (Doorstop documentation,
  https://github.com/doorstop-dev/doorstop/blob/develop/docs/cli/validation.md).
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-17 · related to WAY-18 ·
  related to WAY-20 · related to WAY-24
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-guard-stale-reference ·
  relation-fingerprint-presence · relation-fingerprint-value. Level 2 for checking against the new
  wording — an agent compares the change with the decision:
  - complies: WAY-01 gets a new wording, and the same merge brings field change versions of the
    decisions deriving from it that still stand, and a new wording of one that no longer does;
  - violates: a script renews every old fingerprint in the log without anyone reading the
    decisions that carry them.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a decision that derives from another, or narrows it, stands on what the other says:
tests are read-only (WAY-03) because the foundation comes before the code (WAY-01), and a new
wording of WAY-01 can take that reason away. A plain identifier points to whatever the other
says today, so nothing shows that the ground has moved. `related to` is a passing mention, and a
flag raised on it would be raised for nothing, which teaches people to clear flags without reading
(WAY-02). The fingerprint is the mechanism WAY-02 already sets for references that rely on
wording, so the log needs no second one. The renewal travels in the same merge, because on the
main branch a decision resting on a wording no longer in force would bind without anyone having
checked it, and a renewal written as a version records who checked (WAY-14).
*Rejected:* flags from the kind of change and the order of the log — a second mechanism next to
the fingerprint, and a kind misnamed by its author silences the flag; no flags in the log, with
the author of a change reading the decisions that depend on it — a step that goes missing, and
nothing catches it; a fingerprint on every relation — flags raised for nothing on passing
mentions; flags left open on the main branch until a later task — a decision in force on ground
nobody checked; flags of different strength for different kinds of change — nothing reads the
strength, since the flag names the kind that raised it.
*Consequences:* the rule on relations with fingerprints in the section "Relations and precedence"
of the decision template, the column on references in its table "Kinds of change" and its
sentence on how a change in another decision reaches this one, in the section "Review", are the
written form of this decision. On the main branch, a change to a decision's binding sentences
brings at least a field change version of every decision that derives from it or narrows it. A
repealed decision has no fingerprint to renew: each decision that derives from it or narrows it
drops the relation or changes with it. The fingerprint is computed as WAY-39 says. Which links
between entries of other elements carry a fingerprint is set by those elements (WAY-17).

### WAY-32/1 — What types of relation can a decision name?

A decision names its relation to another decision with one of three types, and the list is
closed: `derives from` — a higher decision this one serves; `narrows` — a decision this one
deliberately goes against in a narrower area; `related to` — any other link.

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
- **Approved by:** Mariusz, 2026-09-16

*Rationale:* a relation type that each author reads differently tells a reader nothing, so each
type is defined once and the list is closed. The three types keep apart what a reader acts on:
`derives from` and `narrows` rely on the wording of the other decision and carry its fingerprint
(WAY-31), `narrows` also tells the agent checking a change that the other decision does not apply
in that area, and every other link is a mention that asks for nothing. Two links that look like
relations have homes of their own: a new answer to the same question is a new version (WAY-19),
and precedence between decisions that both apply is recorded in *Outranks* (WAY-25).
*Rejected:* none considered
*Consequences:* the rule on the closed list of relations in the section "Relations and
precedence" of the decision template is the written form of this decision. A new type enters by a
new version of this decision, once something reads a distinction the three types do not make
(WAY-05). Types of links between entries of other elements are set by those elements (WAY-17).

### WAY-33/1 — What does the author of a foundation change search for?

When a foundation entry is written, or a version changes what it binds, an agent searches the
whole foundation for entries it touches that no written link joins to it, and before the version
is accepted each finding becomes a relation, a change to one of the entries, or a question to a
human. The search runs again against the current main branch before the task branch is merged,
and a merge request that changes the foundation without the record of both searches fails the CI
check.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** in a product built before this process, a requirement that players log in and a
  decision to keep the game's whole state in the browser, with no server, were written in separate
  documents with no link between them; they contradicted each other, and nothing a change could
  flag connected them.
- **Relations:** related to WAY-02 · related to WAY-06 · related to WAY-10 · related to WAY-11 ·
  related to WAY-21 · related to WAY-25 · related to WAY-31
- **Outranks:** none
- **Verification:** level 1 — invariants: foundation-search-record. Level 2 for what the search
  covers — an agent compares the change with the decision:
  - complies: a new decision to keep the state in the browser is written, the search finds a
    requirement for player accounts in another part that nothing links to it, and the
    contradiction goes to a human before the decision is accepted;
  - violates: the search reads only the decisions whose scope overlaps; the search against the
    main branch was made before another task that changed the foundation was merged.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* fingerprints (WAY-02, WAY-31) flag only links someone wrote, and the contradictions
that cost most lie between entries written apart — in different parts, at different times — where
nobody thought to write a link. Only a search at the moment of writing looks for what is not
linked. It covers the whole foundation, because a search within overlapping scopes would never
set a decision about storage against a requirement about accounts. It runs for every version that
changes what an entry binds, because a new wording touches other entries as a new entry does,
while a change to the rationale or the fields touches nothing new. The search at writing sees the
foundation as it was when the branch was made, and two tasks that change different entries in
contradictory ways merge without a file conflict (WAY-06), so the search runs again against the
main branch before the merge. A search is a step that goes missing, so the merge waits for its
record, and a finding becomes a link, a change or a question, because a finding left in a report
is forgotten.
*Rejected:* the layer of numbers and fingerprints alone — it sees only links someone wrote; a
search among the decisions with overlapping scope — contradictions between parts go unseen; a
search at writing only — tasks running in parallel collide unseen once merged; a field in the entry
recording the search — nothing reads it once the entry is accepted.
*Consequences:* the search does not guarantee that nothing was missed: it is a layer above the
fingerprints, not a replacement for them. Where the record of the searches lives and what it holds
are set when the task cycle is designed, together with the records of the panel (WAY-10) and of
the return step (WAY-11). A finding that is a collision with no precedence recorded stops the work
(WAY-25). The skill that writes decisions searches the whole foundation, not only the decisions in
an overlapping scope, and the foundation searched holds the entries of every element it has.

### WAY-34/1 — Which version of the process does a product use?

A product uses the-way at a commit pinned in its own repository: its templates, skills and
scripts, and the decisions of the-way that bind its work, all come from that commit. A newer
version of the process enters a product only through a task in the product that moves the pin.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  task-cycle
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-09 · related to WAY-16 · related to WAY-21 ·
  related to WAY-23
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

An element's skill holds only the way of working: every rule of the element's entries stands in
the element's template, and the skill reads the rules from there instead of restating them.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** related to WAY-05 · related to WAY-09 · related to WAY-16
- **Outranks:** none
- **Verification:** level 1 — invariants: skill-rule-source. Level 2 for what the skill holds — an
  agent compares the change with the decision:
  - complies: a correction of the skill's output that concerns the form of a field goes into the
    template, and the skill is left as it is; the skill orders its steps and says what to ask;
  - violates: the skill says a rationale has at most three sentences while the template does not;
    the skill restates the list of fields.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a rule written both in the skill and in the template is two copies that drift apart,
and then the script that checks the format, which reads the template, and the skill, which writes
the entries, hold entries to different rules. An entry written by hand or by another agent meets
only the template, so the template is the one place every writer and every check reaches. The way
of working — the order of steps, what to ask, when to stop — is not a rule of the entry, so it
stays with the skill.
*Rejected:* rules restated in the skill next to the template — two copies that drift, and the
script and the skill hold entries to different rules.
*Consequences:* a correction of a skill's output that concerns a rule of the entry is a
correction of the template; for decisions it comes with a decision in the log (WAY-05). The
opening paragraph of `record-decision` follows this decision, and the skills of the other elements
follow it once they are written.

### WAY-36/1 — Is a rule a decision or part of a plan?

A rule enters the decision log only when it still binds once the change that brings it has been
merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition
between two states — stays in the plan of that work.

- **Change:** new decision
- **Scope:** decisions, task-cycle
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-07 · related to WAY-22 · related to WAY-26
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: "the foundation reaches the main branch whole, once every element is ready" stays in
    the plan of building the foundation; "when what entries wait for arrives, they are corrected in
    the same change" enters the log;
  - violates: a decision on the order in which elements are built; a decision whose binding
    sentences say what happens until the first merge.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* WAY-01 keeps plans out of the foundation but gives no way to recognise one, and a
plan written in the present tense reads like a decision. The log binds on the main branch
(WAY-07), and a rule that ends when its change is merged binds nothing there: from its first day on
the main branch it is a record of something already done, which would need a repeal at once. The
test asks the same kind of question as the one between a decision and an invariant — whether the
sentence can be pointed at a moment where it still binds.
*Rejected:* plans written into the log and repealed once done — the log fills with the history of
work instead of what binds.
*Consequences:* the plan test in the section "Decision or invariant" of the decision template is
the written form of this decision, and the skill applies it before drafting an entry. A plan of
work has no home in the process yet (WAY-26).

### WAY-37/1 — What happens to entries that wait for something when it arrives?

A change that brings what entries of the foundation wait for — an element's template, the part
map, a script — also corrects every entry that waits for it, in the same change: by a new version
on the main branch, by a correction before it. An agent finds those entries by searching the whole
foundation for what the change brings.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, relation-model,
  task-cycle
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-07 · related to WAY-19 · related to WAY-33
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the change that brings the template of invariants also turns every invariant named
    in working form in the log into a reference to an entry, and corrects the consequences that
    waited for that template;
  - violates: the part map arrives, and WAY-21 still says that a scope names parts from a working
    list.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* an entry that says what holds until something exists becomes false the moment it
arrives, and nothing flags it: no link and no fingerprint (WAY-31) leads from what arrives to the
entries that wait for it, so the foundation stops describing the product as it is (WAY-01) without
a sign. Whoever brings the awaited thing knows what it is, while the authors of the waiting
sentences may be long gone, so the search belongs to the change that brings it. The correction
travels in the same change, because a correction left for later is a step that goes missing.
*Rejected:* corrections left to the periodic review (WAY-11) — the foundation says something false
until the review comes.
*Consequences:* bringing an element, the part map or a shared script includes reading the whole
foundation for sentences that wait for it — "until", "not yet", "in working form".

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
reads the result, rather than parsing a language it would get wrong. Silence is reported as
unchecked rather than as agreement, because a check that quietly sees nothing passes.
*Rejected:* Node.js without packages — as able as Python; a second language adds a second
interpreter to every product's CI; shell scripts in Bash or PowerShell — neither runs the same
on Windows and on Linux; a compiled program in Go or Rust — every change needs a build and
published files; each script in the language its author picks — a product's CI needs every
interpreter any script chose; the product's CI writing those results into a committed file that
the scripts then read — an agent would get no signal before pushing, and the product would carry
a CI step existing only for this process; the scripts parsing other languages themselves — the
tools that tried gave it up.
*Consequences:* a product's CI provides the Python WAY-89 declares and git, and declares in its
repository the commands whose output the scripts read. What those commands cost in time, and how
much their result depends on the environment they run in, the product pays. The format guard of
decisions, the fingerprint script of the relation model (WAY-09), the view of decisions in force
(WAY-18) and the quality gate (WAY-16) are written in Python. Skills and templates are not
scripts, and this decision does not bind them. A check runs the same way for an agent locally, in
CI and for a human (WAY-16), because all three run the same declared command.

### WAY-39/1 — How is the content fingerprint of an entry computed?

The content fingerprint of a foundation entry is the first eight characters, in lower-case
hexadecimal, of the SHA-256 digest of the entry's binding part encoded in UTF-8, taken after
every run of spaces and line breaks is replaced by a single space and both ends are trimmed.
Nothing else in the text is changed before it is digested.

- **Change:** new decision
- **Scope:** relation-model, decisions, invariants, glossary, part-map, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-05 · related to WAY-09 ·
  related to WAY-31 · related to WAY-38
- **Outranks:** none
- **Verification:** level 1 — invariants: fingerprint-definition.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* entries are wrapped by hand at a line length, and wrapping them again says nothing
new, so a flag raised by it would be raised for nothing (WAY-02). Every other change counts,
because whether a change of a letter, a comma or a quotation alters the meaning is what the
human clearing the flag decides; a script that ignored some of them would decide it silently.
Eight characters keep a relation short enough to read in a list, with a chance of about one in
four billion that a changed wording keeps its fingerprint. SHA-256 is in Python's standard
library (WAY-38). One way of computing for every element keeps WAY-02 a single mechanism, while
each element's template still says which part of its entry binds.
*Rejected:* a digest of the text exactly as written — rewrapping a paragraph flags every
reference; ignoring case and punctuation as well — a change of meaning carried by them goes
unflagged; the full digest of 64 characters — relations become hard to read with nothing gained;
a way of computing for each element — a reference to an entry would need to know its element to
be checked.
*Consequences:* the script that computes fingerprints lives in `relation-model/` (WAY-09), and the
format guard of decisions uses it. A fixed typo in binding sentences changes the fingerprint and
is cleared as an editorial correction. A repeal has no binding sentences, so it has no
fingerprint (WAY-31). Changing this way of computing changes every fingerprint at once, and every
relation that carries one is renewed in the same change.

### WAY-40/1 — What kinds of entry does the part map hold?

The part map holds three kinds of entry: a part, a critical flow and a surface the product
promises to keep. An allowed dependency is a field of the part it starts from, and the known
violations of the map's rules are a derived file beside the map, so neither is an entry of its
own. The whole map lives in one Markdown file of fixed shape in `foundations/`.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-04@f7328944 · related to WAY-15 · related to WAY-23
- **Outranks:** none
- **Verification:** level 1 — invariants: map-entry-kinds · map-section-kinds · part-map-file.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* each kind answers a question the others cannot: a part says what a piece of the
product is responsible for and which files belong to it, a flow says what has to keep working
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
What binds in each kind, and so what its fingerprint covers, needs its own decision. The file of
known violations is derived and yet cannot be regenerated from scratch, so it needs a rule of its
own under WAY-15.

### WAY-41/1 — What identifies an entry of the part map?

Every entry of the part map carries a permanent identifier made of words, such as
`relation-model`, and it stays the same when the entry's title changes or the files assigned to
it change. Splitting or merging entries gives every result a new identifier, and the identifier
left behind stays in the map as a withdrawal line naming its successors; an identifier is never
reused.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** Packwerk ties a package's identity to its location — "The package name is the
  path to the folder from the project root" (Packwerk USAGE,
  https://github.com/Shopify/packwerk/blob/main/USAGE.md). Backstage makes the name the thing
  others refer to — "This name is both meant for human eyes to recognize the entity, and for
  machines and other components to reference the entity" — and lets it be reused: "Names may be
  reused at a later time, after an entity is deleted from the registry" (Backstage, Descriptor
  Format of Catalog Entities,
  https://github.com/backstage/backstage/blob/master/docs/features/software-catalog/descriptor-format.md).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-02 · related to WAY-19
- **Outranks:** none
- **Verification:** level 1 — invariants: decision-scope-names · map-identifier-form ·
  identifier-holders · map-reference-target.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* every reference to a part rests on its identifier — a decision's scope (WAY-21), a
criticality inherited along a dependency, a rule file generated for an agent — so the identifier
has to survive the two things that change most often about a part: its title and the files that
belong to it. Identity taken from the path turns every move of a folder into a change of
identity, and the paths already live in the part's assignment rule. Words rather than a number,
because the identifier is read in a scope field and in a dependency list, where a number says
nothing about what it names. A withdrawn identifier stays visible, so that a reference left in a
test or a document resolves to something that says where the part went, rather than to nothing
or, after reuse, to a different part.
*Rejected:* the path as identity — a folder moved renames the part; a number alone —
unreadable where it is used; a number beside the name — it buys a cheap rename of a part whose
responsibility has not changed, and costs a second field and a check of the pair in every
reference, and it can be added later without rewriting the map if renames become frequent; an
identifier reused once a part is gone — an old reference then points at a different part with
no sign.
*Consequences:* splitting or merging a part is a change that renames everything referring to
it: the scopes of decisions, generated rule files and tests. The map keeps withdrawal lines for
good, and grows slowly with them. A script reports a reference to an identifier that does not
exist or that a withdrawal line holds.

### WAY-42/1 — What part of a part map entry binds?

What binds in an entry of the part map is one sentence: a part's responsibility, a flow's
description, a surface's promise — and the entry's content fingerprint covers that sentence
alone. Path patterns, allowed dependencies, failure modes and a flow's list of parts stay
outside it; a change to a part's path patterns is shown instead as the list of files that
changed part.

- **Change:** new decision
- **Scope:** part-map, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-39 · related to WAY-40
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
computes its fingerprints with the script the relation model already has (WAY-39). A reference
that relies on a part's path patterns has no fingerprint to carry; what catches it is the list of
files that changed part.

### WAY-43/1 — Is an entry of the part map versioned?

An entry of the part map is corrected in place and carries no version, so the map shows the
product as it is today. What the entry said before a correction stays in git, and is read from
there.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** none
- **Relations:** derives from WAY-01@a291c2c0 · related to WAY-07 · related to WAY-19 ·
  related to WAY-40
- **Outranks:** none
- **Verification:** level 1 — invariants: map-entry-version. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a part whose responsibility narrows has its sentence rewritten in the same change
    as the code;
  - violates: a part gains a second version of its responsibility with the earlier one kept
    above it; the map holds a section of retired entries next to the live ones.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a decision keeps its earlier versions because they still bind: their reasons and
rejected options stop a later change from walking back into what was already weighed (WAY-18).
An entry of the part map carries no reasons — what put a part where it is lives in a decision —
so its earlier state binds nothing, and the only reader it has is someone asking what the
product looked like then, which git answers. Versions would also cost the map its one job: an
entry read at the start of a task has to say what is true now, and a file of versions makes the
reader choose.
*Rejected:* versions as in the decision log — the map would carry history that binds nothing,
and every reader would have to pick the current entry; an archive of past maps beside the
current one — git is that archive already.
*Consequences:* a correction to a binding sentence changes the entry's fingerprint (WAY-42), and
whoever makes the correction clears the references it flags (WAY-02). The map is not
append-only, so what guards it is the review of the change, not the format guard. A part that
disappears leaves a withdrawal line, which is the map's only trace of what is gone (WAY-41).

### WAY-44/1 — What assigns a file to a part?

Every file git tracks belongs to exactly one part of the map, by path patterns that git itself
matches; a file that no pattern matches, and a file that two parts claim, breaks the gate,
unless the map lists that file as left out on purpose. Tests belong to the part they test,
generated files to the part of their generator, and the files that serve the whole repository —
the lockfile, the build and the CI configuration — are a part of their own. For a file that
collects entries about many parts, the parts a change touches follow from the entries it adds or
changes, not from the part the file itself belongs to.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** Python's standard library does not match paths the way git does: `fnmatch`
  states that "the filename separator ('/' on Unix) is *not* special"
  (https://docs.python.org/3.10/library/fnmatch.html), and `PurePath.full_match`, which handles
  `**`, arrives only in Python 3.13 (https://docs.python.org/3.13/library/pathlib.html). git
  matches such patterns itself, through `.gitattributes`, where "a later line overrides an
  earlier line" (https://git-scm.com/docs/gitattributes), and reports the result with
  `git check-attr` (https://git-scm.com/docs/git-check-attr). import-linter treats a rule that
  matches nothing as an error by default (https://import-linter.readthedocs.io/).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-04 · related to WAY-15 ·
  related to WAY-21 · related to WAY-38
- **Outranks:** none
- **Verification:** level 1 — invariants: file-part-assignment · path-pattern-reach ·
  left-out-file-assignment.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a change is checked against the decisions whose scope names the parts it touches
(WAY-21), and how sharply it is checked follows from the criticality of those parts, so every
file a change can carry has to yield one part — not none, and not two with no rule to choose.
git matches the patterns rather than a script of the-way, because the repository already speaks
that dialect everywhere, and the standard library does not speak it: `fnmatch` treats the path
separator as an ordinary character, and a matcher of the scripts' own would be a second dialect
beside git's, so the same map could resolve one way in a script and another in git. Tests go
with the part they test, because changing a test changes what that part promises, not some part
called "tests"; generated files go with their generator, because that is where a change to them
comes from. The files that serve the whole repository have no natural part, and giving them one
would tie the lockfile to whichever part happened to claim it. A file that no pattern matches is
an error rather than a quiet no-man's-land, and where leaving a file out is deliberate the map
says so by name, so that the error keeps its meaning. A file collecting entries about many parts
would otherwise pull every change of any part into the single part that owns the file.
*Rejected:* a file in several parts — the decisions to check and the criticality of the task
would have two answers and no rule to pick; patterns matched by a script of the-way — two
dialects of pattern in one repository, resolving differently across systems; tests as a part of
their own — a change to a test would stop counting as a change to what it tests; files left
unassigned in silence — the map would keep passing while saying less and less about the
repository; the part of a ledger file taken from its path — every decision recorded would count
as a change to the decisions part alone.
*Consequences:* the map writes its patterns in git's dialect, and the script asks git to match
them (WAY-38). The element's template gives a part its field of patterns and a mark for
generated files, and gives the map its list of files left out on purpose. Binding the map's
script to the format of an element's entries, so that a ledger file yields the parts of a change,
is part of designing that script.

### WAY-45/1 — What is a critical flow, and when does a change lie on it?

A critical flow is an entry of the part map: an identifier, a criticality and the list of parts
it runs through, while what has to stay true along it is an invariant whose end-to-end test names
the flow. A change lies on a flow when it touches a part from that list; a change to a file the
map leaves out, to the build configuration or to the dependencies lies on every flow. The test of
every critical flow runs on every change.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** a tool that picks tests from a change falls back where it cannot reason: "For
  commits and scenarios that TIA can't understand, it falls back to running all tests […] if the
  code commit contains changes to HTML or CSS files, it can't reason about them and falls back to
  running all tests" (Azure DevOps Test Impact Analysis,
  https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-08 · related to WAY-13 ·
  related to WAY-16 · related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: flow-part-names · flow-invariant-link · gate-reported-set
  · flow-test-run.
- **Review when:** a product holds more critical flows than its gate can run on every change ·
  check by: 2026-12-31
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* a flow needs a place in the map, not only an invariant, because two things have to
be computed from it: the criticality it passes to the parts it runs through, and the fact that a
given change lies on it. An invariant alone sits outside the map, where neither computation can
reach it. The list of parts lives at the flow rather than as a mark at each part, so that there
is one list to read and one place to correct. Files that belong to no part, the build
configuration and the dependencies lie on every flow, because a change to them can alter any
flow and nothing in the map says which — the same fallback a test-selection tool makes where it
cannot reason. Every flow's test runs on every change, because a product holds a handful of
critical flows, and choosing among a handful costs more than running them.
*Rejected:* a critical flow as an invariant alone, outside the map — its criticality would reach
no part, and nothing could tell that a change lies on it; the flow recorded as a mark at each
part it runs through — the same list in two places, with no place to read the flow whole;
picking which flow tests to run from the change — with a handful of flows the choice costs more
than the run, and it fails exactly where it cannot reason.
*Consequences:* a flow that spans two versions of the product — save, upgrade, load — keeps the
recorded earlier states its test replays in a part on its list, so that changing them counts as a
change on the flow (WAY-44). Checking a flow's list of parts against what its test really touches
needs a rule of its own. A part on a critical flow inherits that flow's criticality.

### WAY-46/1 — How does the criticality of a part arise?

A part carries the failure modes a human records at it, each with the kind of damage it does,
its severity, and how it is detected before release — a named invariant, or an explicit "not
detected". The criticality of a part is computed rather than written by hand: the highest of its
own failure modes, of the critical flows it lies on, and of the parts that depend on it, unless
the dependency records that the two are separated and a failure of one does not damage the
other. A part with no failure modes recorded counts as the highest criticality; raising a part's
criticality needs no reason, and lowering it needs one, written at the part.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** safety standards make a part inherit the class of what it belongs to unless a
  documented separation says otherwise — IEC 62304 4.3 d), quoted on the Elsmar Cove forum
  (https://elsmar.com/elsmarqualityforum/threads/different-62304-safety-classes-for-modules-in-software-system.90429/):
  "such SOFTWARE ITEMS shall inherit the software safety classification of the original SOFTWARE
  ITEM (or SOFTWARE SYSTEM) unless the MANUFACTURER documents a rationale for classification into
  a different software safety class […]. Such a rationale shall explain how the new SOFTWARE
  ITEMS are segregated so that they may be classified separately" — and treat what nobody
  classified as the highest class (Johner Institute, "Safety classes according to IEC 62304",
  https://blog.johner-institute.com/iec-62304-medical-software/safety-class-iec-62304/): "If the
  manufacturer does not carry out this safety classification, the software and all software
  components fall into the highest safety class C." Changing an assessment is asymmetric: "Proprietors
  may raise Protection Levels for a specific use case. An exception is required to lower a published
  Protection Level" (UC Berkeley, Data and IT Resource Classification Standard,
  https://security.berkeley.edu/data-classification-standard).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-04 · related to WAY-13 ·
  related to WAY-15 · related to WAY-45
- **Outranks:** none
- **Verification:** level 1 — invariants: failure-mode-severity · failure-mode-detection ·
  part-criticality-field · map-guard-unrecorded-criticality · map-guard-dependency-report.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* criticality is the number that sets how sharply a task is checked (WAY-13), and it
arises outside the part: from the damage its own failure does, from the flows it serves, and
from who leans on it. Written by hand at the part, it would be a copy that goes stale the day a
new flow crosses the part or a new dependency appears; computed, it follows both. The
computation takes the highest rather than an average, because the worst failure is the one the
process exists for, and it stops at a recorded separation, because a part whose failure cannot
damage the important one is the only part that has earned a lower number. A part nobody has
assessed counts as the highest, so that silence raises checks instead of removing them. Raising
is free and lowering costs a written reason, because lowering is the move made for convenience.
Detection before release sits at the failure mode, and names the invariant that detects it, so
that the map says which failures the gate would catch and which it would not.
*Rejected:* criticality written by hand at the part — a second copy of what the flows and
dependencies already say; three separate axes of criticality — confidentiality, integrity and
availability — as fields of a part, since WAY-13 reads one measure of sharpness and nothing
would read the other two; an unassessed part counting as the lowest — a part nobody looked at
would never raise a check; raising and lowering treated alike — the direction made for
convenience has to cost something; "failure symptom" and "first step to limit the damage" as
fields — they are read by an operator during an incident, and this process has no incident path.
*Consequences:* WAY-13 reads the computed value, not what a human wrote. The kind of damage
chooses which checks a task runs, not how sharply it is checked. The number of degrees of the
scale is `TODO`: it follows from the number of distinct sets of steps the task cycle has, and is
set when the task cycle is designed. A part whose criticality is raised from outside — by a law
or a contract — gets it through a failure mode whose detection names an invariant resting on the
fact of the obligation (WAY-87).

### WAY-47/1 — How is a critical flow's list of parts checked?

The list of parts of a critical flow is checked against coverage: where a flow's test leaves a
coverage file, the script reads it, maps the files it names to parts and reports every part the
flow's list does not hold. A flow whose test leaves no coverage file is reported as "list of
parts unchecked", never as agreeing with the map. The coverage comes from the run the gate
already makes, and this check starts no second run of the tests.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** a checking script fails rather than guessing where it cannot read what it needs:
  "If value could not be extracted then script should fail" (Kubernetes KEP-1209, Metrics
  Validation and Verification,
  https://github.com/kubernetes/enhancements/blob/master/keps/sig-instrumentation/1209-metrics-stability/README.md).
- **Relations:** derives from WAY-45@3991b544 · related to WAY-16 · related to WAY-38 ·
  related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: flow-coverage-parts · map-guard-missing-coverage ·
  map-guard-test-runs.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a flow's list of parts is written by a human and decides what lies on the flow
(WAY-45), so a part quietly missing from it sends a change down the light path. Coverage is the
only thing that says which files the test really ran through. The check is conditional rather
than required, because a product with no coverage for a flow still gets the rest of the map,
while a check that demands what a product does not produce gets turned off whole. Silence is
reported as "unchecked" rather than as agreement, because a check that has stopped seeing
anything passes — two empty sets compare equal, which is how a route-guarding test in a product
built with agents needed a second test to guard against a vacuous pass. The coverage comes from
the run the gate already makes, because an end-to-end run is expensive, and a map that costs a
second one is a map nobody keeps.
*Rejected:* a required coverage check — a product without coverage would fail on the map instead
of using it; coverage used to choose which tests run — a different job, and WAY-45 runs them all;
silence read as agreement — the emptiest map would be the cleanest; a test run started by the
map's script — a second end-to-end run for the sake of a check.
*Consequences:* a product that wants the lists of its flows checked makes its gate leave a
coverage file for each flow's test, in a format the script reads (WAY-38). "Unchecked" is a state
of the map that a human reads, not an error that stops the work.

### WAY-48/1 — How is a trust boundary recorded?

A trust boundary is recorded at the part that holds it, as a pattern of the code files which
accept data the product does not trust; an exchange with the external context records its
direction and marks what comes in as untrusted. A boundary can run inside the product, wherever
it reads back something it does not control — a browser's storage, a file on the player's disk.
A change that touches the files of a boundary is checked for crafted input, whatever the
criticality of the part.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** Chromium picks the review a change needs from the files it touches rather than
  from their importance, by pinning owners to a file pattern —
  `per-file *.mojom=file://ipc/SECURITY_OWNERS` (Chromium, IPC security reviews,
  https://chromium.googlesource.com/chromium/src/+/main/docs/security/ipc-reviews.md). A trust
  boundary kept as an object of a diagram has no reader: in pytm, none of the threat rules reads
  the boundaries the model records (https://github.com/OWASP/pytm).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-11 · related to WAY-13 ·
  related to WAY-44 · related to WAY-46
- **Outranks:** none
- **Verification:** level 1 — invariants: trust-boundary-pattern · external-exchange-row ·
  gate-boundary-change.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* what makes a change dangerous is not only how much the part matters but where the
data comes from: a part of the lowest criticality that parses what a stranger sends is the
oldest way in. The boundary therefore feeds the choice of checks on its own, read from the files
a change touches — the signal Chromium already routes its security review by. It is a pattern of
files rather than a line in a picture, because a pattern is matched by the same machinery that
assigns files to parts (WAY-44), while a boundary kept as an object has no reader at all. The
boundary runs inside the product as well as at its edge, because the product controls neither
the browser's storage nor the file on the player's disk, and reading either back is the same act
of trust.
*Rejected:* a trust boundary as its own kind of entry in the map — nothing would read it that
the pattern at the part does not already give; the boundary taken from the criticality of the
part — the two are independent, and the exposed part is often the unimportant one; the boundary
drawn as a line in a diagram — read by a human looking at the picture, and by nothing else.
*Consequences:* a part that accepts untrusted data carries the pattern, and every exchange with
the external context carries a direction. Places that start accepting data outside the pattern
are caught by the step that carries findings out of a task (WAY-11). What the check for crafted
input consists of is set when the task cycle is designed.

### WAY-49/1 — How does a product declare a surface it promises to keep?

A surface the product promises to keep is declared at the element itself, in the code or in the
schema, with the level of the promise and, once the surface is being withdrawn, the date of the
withdrawal. The map holds one entry per surface — its identifier, the promise in words, and
where the declaration sits — and holds no list of withdrawals in progress. A surface that cannot
be marked at the element is written in the map by hand and checked by a test.

- **Change:** new decision
- **Scope:** part-map
- **Based on:** what counts as a surface is declared, not discovered: "Software using Semantic
  Versioning MUST declare a public API" (https://semver.org/). Tools read the promise where it is
  written at the element — API Extractor reports an exported item with no release tag
  (https://api-extractor.com/pages/messages/ae-missing-release-tag/) — and turn a withdrawal date
  written there into a check, where removing the element before the date is a breaking change
  (oasdiff, https://github.com/oasdiff/oasdiff/blob/main/docs/DEPRECATION.md).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-15 · related to WAY-34 ·
  related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: surface-promise-level · surface-declaration ·
  map-withdrawal-date.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* a surface is a promise, and no tool reads a promise out of code: a tool computes the
shape of what somebody declared, and the declaring is the human part. It sits at the element,
where whoever changes it sees it and where the tools that compute shape and breaking change look
for it. The map keeps the promise in words and the place of the declaration, because that is
what a scope, a criticality and a change path are read against, and a header comment cannot
carry them. The withdrawal date stays at the element as well, because it is checked against the
element's removal; kept in the map it would be a second copy, and the entry nobody deletes. A
surface that cannot be marked at the element — the format of a saved file, a command-line
interface — exists all the same, and a hand-written entry with a test is what keeps it from
disappearing quietly.
*Rejected:* the list of surfaces computed from the code — tools compute the shape of declared
elements, never which of them the product promises to keep; the declaration kept only in the map
— whoever changes the element does not read the map, and no tool would find it there; a list of
withdrawals in progress in the map — a second place to update, stale the day the element goes.
*Consequences:* the product's own tool computes the shape of declared elements, a breaking change
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
- **Relations:** derives from WAY-49@631b41c6 · related to WAY-34 · related to WAY-48
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

### WAY-51/1 — What does the main branch hold where the map's rules are not met?

On the main branch the part map holds its rules together with a listed debt: every place where
the code does not meet a rule stands on a derived list of known violations. A new violation
breaks the gate; a position the code no longer contradicts breaks it too and goes in the same
change; a position is added only by a change of the foundation that a human accepts, never by a
step of implementation. The state a product is in when this process enters it goes onto that
list once.

- **Change:** new decision
- **Scope:** part-map, task-cycle
- **Based on:** a list of known violations grows without limit where adding to it is the cheap
  move: Packwerk answers most situations with "Simply run `bin/packwerk update-todo`" and holds
  that "New dependency violations are never hard-blocked"
  (https://github.com/Shopify/packwerk/blob/main/RESOLVING_VIOLATIONS.md), and its authors record
  what followed — "the rate at which Packwerk was identifying problems to its users vastly
  outpaced their capacity to actually fix them (or interest in doing so)" and, for domain
  components, "monstrously large todo files for every component. With every new feature added,
  these todo files grew larger" (A Packwerk Retrospective,
  https://railsatscale.com/2024-01-26-a-packwerk-retrospective/).
- **Relations:** derives from WAY-40@aeabb301 · narrows WAY-15@72eb2240 · related to WAY-01 ·
  related to WAY-28
- **Outranks:** none
- **Verification:** level 1 — invariants: known-violation-coverage · known-violations-growth ·
  known-violation-currency · known-violation-fields · known-violation-line-number.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* this process enters products that already exist (WAY-28), where a rule the code
breaks in fifty places either stops all work or is quietly dropped. The listed debt keeps the
rule a rule while making the gap visible and countable. What the list needs is a ratchet, because
its own failure mode is well recorded: where adding to the list is the easiest move, it grows
faster than anyone's will to empty it, and an agent takes that move more readily than a person.
Hence the three mechanisms together — a new violation is an error, a stale position is an error,
and growing the list is a foundation change a human accepts — since any one of them alone leaves
the cheap move open. Positions carry no line numbers, because a line number goes stale at the
next edit while the violation it stands for does not.
*Rejected:* a main branch holding only what the code already meets — the process could never
enter an existing product; the rule weakened until the code fits it — the map would then describe
the accident rather than the intent (WAY-15); positions with line numbers — stale at the next
edit; a part marked "not checked yet" instead of a list of violations — the gap stops being
countable, and nothing shows whether it grows.
*Consequences:* a list growing at one part is a signal to review where that part's boundary runs,
rather than an order to pay the debt: it is easier to bend a mental model to what the code
actually does than the other way round. The list is derived and yet cannot be regenerated from
scratch — regenerating would swallow the new violations — so it is checked as a subset of the
list on the main branch. What the main branch of a foundation carries (WAY-01) therefore includes
this debt.

### WAY-52/1 — What is generated from the part map for an agent?

From the part map a product generates for its agents only rules pinned to path patterns: a
part's responsibility, its allowed dependencies, and the binding sentences of the decisions whose
scope names that part, written into the rule channels the tools already read. The patterns come
from the part's rule for assigning files, and a generated rule file is derived like any other. No
overview of the repository is generated for an agent.

- **Change:** new decision
- **Scope:** part-map, decisions
- **Based on:** measured on coding agents, "providing context files does not generally improve
  task success rates, while increasing inference cost by over 20% on average", and "while
  instructions in the context files are well followed by coding agents, repository overviews,
  although popular and recommended by model providers, are not helpful" (Gloaguen, Mündler,
  Müller, Raychev, Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for
  Coding Agents?", ETH Zurich / LogicStar.ai, https://arxiv.org/abs/2602.11988). The tools carry
  channels for rules pinned to path patterns: Cursor rules
  (https://cursor.com/docs/context/rules), Claude Code memory
  (https://code.claude.com/docs/en/memory) and Kiro steering (https://kiro.dev/docs/steering/).
- **Relations:** derives from WAY-40@aeabb301 · related to WAY-15 · related to WAY-21 ·
  related to WAY-44
- **Outranks:** none
- **Verification:** level 1 — invariants: derived-file-content · generated-pattern-source ·
  generated-overview.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-17

*Rationale:* what a context file does for an agent has been measured, and the two halves of the
answer point opposite ways: instructions pinned to files are followed, while an overview of the
repository does not help and is paid for in every call. So the map gives the agent the part of
itself that is an instruction — what this part is responsible for, what it may depend on, what
the decisions in its scope bind — and nothing that merely says where things are. The tools' own
channels carry it, because a rule that arrives with the file the agent opens reaches it at the
moment it binds. Generated rather than written by hand, because a rule file written by hand is a
second copy of the map, which is the reason WAY-21 keeps paths out of decisions in the first
place.
*Rejected:* a code map or repository overview generated for an agent — measured as not helpful,
at a fixed cost in context; rule files written by hand — a second copy of the map, drifting from
it; the whole decision log pinned to every path — an agent loses rules as their number grows.
*Consequences:* a picture of the architecture for a human is made on request, outside an agent's
context, and the code map for an agent leaves the views WAY-04 expects. The set of decisions an
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
for the fact a value follows from rather than for the name of a value. A field whose value
neither can be read off nor follows from a fact is marked in the template as resting on a
judgment.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts
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
- **Approved by:** Mariusz, 2026-09-20

*Rationale:* an author asked to name a value picks from the names in front of them and writes a
reason why the nearest one will do; the reason reads well, and the record then says something
that was never true. The failure leaves no trace, because a wrongly named value looks exactly
like a rightly named one. A value read off the product cannot be talked into place, and a
question about a fact — which command the gate runs, which files a pattern matches — has an
answer the author can check instead of argue. Where the value is a judgment after all, saying so
keeps a reader from taking it for a reading. This product already decides this way four times
over, and each time the variant in which a person names the value stands in *Rejected* with its
reason.
*Rejected:* leaving the choice to the author with a definition beside each value — a definition
tells apart values a reader already distinguishes, and says nothing about a case none of them
covers; a value meaning "none of these fits" in every closed list — the list of relation types
already carries one, and it is chosen 166 times out of 191, so it records what came cheapest
rather than what was true.
*Consequences:* a template that asks for the name of a value where a tool can read that value,
or where a question about a fact settles it, is a defect of the template, corrected together
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

### WAY-55/1 — Which part of the process holds the quality gate?

In this repository, the quality gate is a part of the process of its own, and its directory is
`gate/`: the code that runs the checks a change calls for, and the test of every critical flow,
are files there. No other part's directory holds that code or such a test, and a file under
`gate/` that only calls a body kept in another part's directory leaves the gate in that part.
Which checks a change calls for, when the gate runs and what follows from its result belong to
the task cycle, not to this part.

- **Change:** new decision
- **Scope:** gate, decisions, invariants, glossary, part-map, environment-facts, relation-model,
  repository, task-cycle
- **Based on:** none
- **Relations:** narrows WAY-44@220f5b85 · related to WAY-09 · related to WAY-16 ·
  related to WAY-21 · related to WAY-45 · related to WAY-47
- **Outranks:** none
- **Verification:** level 1 — invariants: flow-test-location. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: the code that runs the checks is added under `gate/`, and what the gate does with a
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
crosses parts by definition (WAY-45) and the gate is what runs it; that is why this decision goes
against WAY-44's rule for tests in this narrow place, and nowhere else. A part of its own is also
what gives the gate its own failure modes and its own criticality.
*Rejected:* the gate in `elements/invariants/` — a program serving every element tied to one of
them; the gate in `task-cycle/` — the code that runs the checks would move whenever the steps of a
task changed; the gate among the files that serve the whole repository, beside `.gitattributes` —
that part answers for files that configure the repository and has no tests of its own, while the
gate has failure modes, tests and dependencies on other parts; a critical flow's test kept with
the single part it tests, as WAY-44 has every other test — a flow runs through several parts and
none of them owns its test, and the cost WAY-44 named is paid by the flow carrying the gate on its
list of parts rather than left unsaid.
*Consequences:* WAY-09 gains `gate/` in its list of the directories a part of the process may
have, and the sentences in WAY-09 and WAY-16 that left the gate's home to be settled between the
invariants element and the task cycle go, both corrected in place, since neither entry has reached
the main branch (WAY-07). A critical flow's test living in `gate/` puts `gate` on that flow's list
of parts, so `gate` inherits the flow's criticality (WAY-46), a change to the test lies on the
flow (WAY-45) and is checked against the decisions of every part on the list (WAY-21), and the
coverage of that test agrees with the list (WAY-47); `wording-reaches-dependants` gains `gate` on
its list with this change. The map's script gains a check that a flow's test path lies under
`gate/`, made only against this repository's own map, the way its check of `examples.md` already
is; until it does, the level 1 invariant has nothing that runs it. A file under `gate/` may use
the code of a part the map lets the gate depend on — the existing flow test reads the decision
element's test fixtures, and that is such a dependency, not the gate living in an element. When
the gate's code is built, the gate's dependencies in the map grow to the parts whose checks it
runs. The invariants element gets a format guard of its own, which is not the gate: the guard
keeps the shape of an entry, the gate runs what the entry says to check. Whether a product built
with this process keeps its own gate and flow tests in `gate/` is left to that product.

### WAY-56/1 — How much does one invariant entry hold?

An invariant entry states one invariant, as WAY-22 defines it, in one sentence. The method of
checking and the links that WAY-08 and WAY-17 require stand beside that sentence, not inside it.

- **Change:** new decision
- **Scope:** invariants
- **Based on:** none
- **Relations:** derives from WAY-22@52c514ca · related to WAY-02 · related to WAY-08 ·
  related to WAY-12 · related to WAY-17 · related to WAY-26 · related to WAY-37
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-sentence-count. Level 2 for one invariant per
  sentence — an agent compares the change with the decision:
  - complies: "every entry in the log has every field of the template" is one entry, though a
    commit can break it for a single entry or a single field; "every result of a human inspection
    names who checked and when" is one entry;
  - violates: "binding sentences number one to three and contain no *should*, *will* or keyword
    of RFC 2119 in capitals" kept as one entry, though how many sentences there are and which
    words they use are two separate rules; the sentence on fields split into one entry per field.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-21

*Rationale:* WAY-22 says what an invariant is: a sentence a commit makes true or false. An entry
that states one such sentence has a fingerprint of its own (WAY-02), so a fix to it flags only
what relies on it — a reason WAY-26 gives each principle and each non-goal an entry of its own —
and a deliberate break aimed at it tells whether its method catches it (WAY-08). Where one
invariant ends and the next begins is a judgment: three rules tried against the invariants
written in working form in this log — one property with labelled conditions, a split wherever a
commit can break one part while the rest holds, one check applied across many items — each gave
two answers or a wrong one on real sentences. So the count of sentences is checked by a script,
and what one sentence may join is judged against a pair of examples, as WAY-12 does for any rule
a script cannot settle.
*Rejected:* one entry for a property, with its conditions as labelled points — no rule told one
property with several conditions from several properties, a fix to one point would flag every
test citing the entry, and a test would need a way to cite a single point; a sentence split
wherever a commit can break one part of it while the rest holds — a sentence about every entry of
the log would fall apart into one entry per entry.
*Consequences:* the template of the invariants element gives an entry its one sentence, and the
element's format guard counts sentences as the decisions guard does, which catches length only:
two rules joined in one sentence pass it and are left to review. What in an invariant entry
binds is set by WAY-59. What an invariant entry names in the part map, so that a change reaches the
invariants it can break, is set by WAY-62.

### WAY-57/1 — Is an invariant entry versioned?

An invariant entry carries a version number, starting at 1, and holds only its current wording,
and earlier wordings are read from git. When the entry's content fingerprint differs from its
fingerprint on the main branch, its version is one higher than there, unless the entry declares a
correction naming both fingerprints and the human who decides the change under WAY-10 confirms,
with both wordings in front of them, that the meaning is unchanged; when the fingerprint does not
differ, the entry keeps the version it has there. An invariant test cites its invariant by
identifier and version, in the form the template gives, and fails the gate when that version is
not the current one, while elsewhere a reference to an invariant's version is historical and never
flagged, as WAY-02 has it.

- **Change:** new decision
- **Scope:** invariants, relation-model, gate, task-cycle, part-map
- **Based on:** none
- **Relations:** derives from WAY-03@4fa941a4 · derives from WAY-10@a5941d52 ·
  narrows WAY-02@af08ee5d · related to WAY-07 · related to WAY-08 · related to WAY-14 ·
  related to WAY-17 · related to WAY-19 · related to WAY-20 · related to WAY-22 ·
  related to WAY-31 · related to WAY-39 · related to WAY-43 · related to WAY-45 ·
  related to WAY-54 · related to WAY-56
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-version-number · invariant-version-new ·
  invariant-version-changed · invariant-version-unchanged · invariant-earlier-wording ·
  invariant-citation-version · invariant-correction-confirmation. Level 2 for what counts as a
  correction — a change after which some test citing the entry would need a different expected
  value is a raise, never a correction, because WAY-10 treats a changed expected value as more than
  a test's form; an agent compares the change with the decision:
  - complies: a typo in an invariant's sentence is fixed under a declaration naming both
    fingerprints, the human deciding the change confirms it seeing both wordings, and no test's
    citation changes; "at most three" rewritten as "at most four" raises the version, and the test
    citing the old version fails until the foundation step checks the test against the new wording;
  - violates: "must" becomes "may" under a confirmed correction; a wrong dash in a heading's code
    literal is fixed under a declaration, though a test asserting that literal would need a
    different expected value; every citation moved to a new version by a script, with no one
    checking the tests against the new wording.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* an invariant test is read-only during implementation (WAY-03), and a change to it goes
to the panel and, beyond a change of form, to a human (WAY-10). Cited with a content fingerprint,
as WAY-02 has every reference that relies on wording, the test would be flagged by every change
other than whitespace (WAY-39), and a fixed typo would bring a change to a read-only test, with a
panel and a human for it. Cited by a bare identifier, it would never be flagged, and would go on
checking a meaning the entry no longer states. A version sits between the two: it moves when the
meaning moves. It is a second mechanism next to the fingerprint, which WAY-31 turns down for
references between decisions; there a flagged reference is cleared by whoever reads it, while here
the reference is a read-only test that nobody may touch without a human, so the question of
meaning is asked once, at the entry, of the human who already decides the change. That keeps the
ground WAY-31 stands on — a kind of change named by its author never silences anything by itself:
the declaration covers only the entry it stands in, names the wording it corrects and the wording
that replaces it, and counts only once a human has confirmed it. The default is a raise, because a
forgotten raise drifts silently while a needless one fails loudly. After the merge a declaration
names the fingerprint the entry now has on the main branch, so it states something true about the
entry's history and needs no step to remove it; the next change to the entry replaces it or
removes it, since a declaration whose second fingerprint no longer matches is an error. The version
is written in the entry rather than computed on demand, because a test cites a value that has to
stand where the test's reader can see it; the guard computes what it must be and compares. Unlike
a decision (WAY-19), an invariant carries no reasons and no rejected options (WAY-22), so its
earlier wordings bind nothing — the ground on which WAY-43 keeps no versions in the part map;
unlike a part of the map, an invariant has read-only tests pinned to what it means, and they need a
marker that changes with the meaning alone.
*Rejected:* no version, as in the part map (WAY-43) — a test would carry a fingerprint and be
flagged by every fixed typo, or a bare identifier and never be flagged; earlier versions kept in
the entry, as in the decision log — an invariant carries no reasons, so its history binds nothing,
and every reader would have to pick the current wording; a version written by hand with nothing
comparing it — a forgotten raise leaves tests checking an old meaning with no sign; a correction
declared once for a whole change, by its author alone — a kind named by its author silencing the
flag, which WAY-31 rejects, and a correction in one entry would cover a change of meaning in
another; a declaration naming only the fingerprint it corrects — after the merge it names a
fingerprint the main branch no longer has, and either fails the gate until a second change removes
it, or, repointed, silences the next change of meaning; the declaration kept in the commit message
of the change — it would rest on a record of the change that this process has no home for yet
(WAY-10, WAY-33); a test allowed to cite an earlier version, as a reference to a decision version
may — a test never deliberately checks what the product no longer promises.
*Consequences:* the template of the invariants element gives an entry its version, the form of a
citation with a version and the form of a declaration of a correction. What in an invariant entry
binds, and so what the fingerprint covers, is set by WAY-59. A correction keeps every test's citation, and does not stop a test's form from changing in the same
change, as WAY-10 allows; a change to the way fingerprints are computed (WAY-39) removes every
declaration of a correction in the same change. Who counts as the human deciding the change for an
invariant entry, and where the confirmation is recorded, is not settled here: it follows the rule
WAY-14 leaves to each element and the records WAY-10 and WAY-33 already owe the task cycle; until
then the guard reports a declaration as "correction declared, confirmation not checked", never as
agreeing. The invariants element's format guard runs the invariants above; the entry on the main
branch they compare with is the one holding the same identifier there (WAY-64). The map gives
`invariants` a dependency on `decisions`, `part-map` and `relation-model`, and none runs the other
way. The guard compares an entry with its
state at the point where the task branch left the main branch, not with the main branch's tip, so
an entry the branch never touched is never asked to change. Where there is no main branch — as in
this repository until the foundation reaches it — the guard compares nothing and says so, and
every entry stays at version 1, as entries of the decision log are corrected in place before the
main branch (WAY-07); afterwards a merge raises an entry's version by at most one. A version
citation is not a reference that leans on wording (WAY-02), so the promise of the critical flow
`wording-reaches-dependants` does not cover it; a stale one is caught by the last two invariants
above. The test of that flow, `gate/test_wording_reaches_dependants.py`, names its flow but no
invariant with a version, and is brought into line by the change that brings the invariants
element (WAY-37). After a raise, a citing test's changed citation is accepted like a new test under
WAY-08. A human inspection carries no version under this decision; an exploratory test run by an
agent is a test (WAY-08) and cites one like any other. A split, a merge or a withdrawal leaves a
test citing the old identifier with no current version to match, so it fails the gate as above
(WAY-64).

### WAY-58/1 — What does an invariant entry record when it was recovered from what a product does?

An invariant entry that a human chose from what the product already did before the task writing it
began, as WAY-28 describes, and that names no decision entry of the product's log it derives from,
carries a field reading `recovered — searched: <…>; found: <…>`; every other invariant entry holds
`none` there. *found* names the place of
each source the search found that gives a reason for keeping the behaviour or calls for a different
one, or reads `nothing`; a place that only cites another is followed to the place it cites, marked
when that source is superseded, and *found* never states a reason itself, nor one an agent infers.
When an entry's wording enters the foundation, the gate reports whether its method passes on the
commit the task branch left the main branch from and fails there on a deliberate break, and the
human deciding the change sets the field with that report in front of them.

- **Change:** new decision
- **Scope:** invariants, gate
- **Based on:** none
- **Relations:** derives from WAY-28@036a9301 · derives from WAY-22@52c514ca ·
  derives from WAY-17@ab01c0e5 · related to WAY-04 · related to WAY-05 · related to WAY-07 ·
  related to WAY-08 · related to WAY-10 · related to WAY-11 · related to WAY-16 ·
  related to WAY-19 · related to WAY-23 · related to WAY-29 · related to WAY-37 ·
  related to WAY-38 · related to WAY-47 · related to WAY-54 · related to WAY-55 ·
  related to WAY-56 · related to WAY-57
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-recovered-form · invariant-recovered-derived ·
  gate-fork-point-evidence. Level 3 for the value of the field — the human deciding the change sets
  it with the gate's report in front of them, and the record of that decision names who and when.
  Level 2 for what counts as already done and what *found* holds — an agent compares the change with
  the decision:
  - complies: entering a game, an agent lists what its save module does, a human chooses "a save of
    another version is rejected whole", the gate reports that the check passes and breaks on the
    commit the branch left from, and the entry reads `recovered — searched: the save module and its
    history, the game's own documents; found: the comment above the save format's version constant
    at commit <sha>, decision D23 of the game's concept document`; an invariant written at a task's
    foundation step for a feature being built holds `none`;
  - violates: *found* reads "old saves are dropped because the rules may have changed"; *found*
    lists a comment explaining how the loader parses a save; an invariant about a field the task
    itself adds is marked recovered because its check found nothing to fail on the older commit.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* WAY-28 lets an invariant recovered from an existing product bind before anyone knows
why it holds, and asks for a note that it was recovered. Without the note it reads like a rule
someone wrote, and whoever later weighs a change to it has no sign that the reason for it was never
settled in the log. Whether an entry was recovered cannot be read off the product (WAY-54): a check
run on the older commit also passes where the thing it checks does not exist yet — two empty sets
compare equal (WAY-47) — and it passes for a new rule the product happened to meet before anyone
wrote it down. A deliberate break on the older commit (WAY-08) removes the first case and not the
second, so the gate's run is evidence for the human, who already decides every change to the
foundation (WAY-10), not the verdict; the field is marked in the template as resting on a judgment.
The gate runs the method, never the element's format guard, which keeps only the shape of the entry
(WAY-55). The same line places both cases of the return step (WAY-11): behaviour the product had
before the task can be recovered, while a rule the implementer writes into the task's own code was
not there before the task and holds `none`. Recording the search spares the next agent the same
search, as WAY-29 does for an inherited decision. *found* points to places rather than quoting
them, because an invariant says nothing about why (WAY-22), and it lists a place calling for a
different behaviour too, since that is what a human weighing the invariant most needs to see. The
field is present in every entry, with `none` as a statement, because a missing value cannot be told
from a forgotten one (WAY-71).
*Rejected:* the mark only where no cause is known — at entry into a product the cause usually sits
somewhere that is not a decision entry, such as a comment in the code, a concept document or a line
of requirements, and, tried on a game this process would enter, the rule gave two answers for every
such case; the mark on every entry that names no decision — WAY-22 lets an invariant stand with no
choice behind it, so one written for a feature being built would be marked recovered; the mark set
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
(WAY-38), and the human sets the field without that evidence. An entry whose wording changes, by a
raised version (WAY-57) or by a split or a merge (WAY-64), enters again, and its field is set again. A place in *found*
that records a choice is recovered as a decision when a later task touches the part (WAY-28) — the
change that enters the invariant does not itself count as touching it; a reason given by the human
who chooses the invariant is recorded as an inherited decision given by that person (WAY-29). Once
the invariant names such a decision, its field turns to `none`, and neither the field nor the new
link raises its version (WAY-59). An invariant a human takes from a product's own requirements, which the product does
not meet yet, holds `none` and enters as an invariant the product violates, whose place is set by
WAY-67; its source is not recorded by this decision. The field's readers are the
human weighing a change to the invariant and the agent recovering a part's decisions. WAY-28's
consequence on the note is corrected in place to name this decision, while the element still has no
template to carry the note (WAY-37). An invariant holding a condition taken from a requirement of an
outside catalogue names it in *Rests on* (WAY-73); how such a requirement is written as a fact is set
by WAY-86.

### WAY-59/1 — What part of an invariant entry binds?

What binds in an invariant entry — its wording, as WAY-57 and WAY-58 use the word — is its one
sentence, and the entry's content fingerprint covers that sentence alone. Everything else the
entry carries stays outside the fingerprint — such as its method of checking, the links it names
beside the sentence, its version, a declaration of a correction and the recovered field.

- **Change:** new decision
- **Scope:** invariants, relation-model
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · derives from WAY-56@3213162c · related to WAY-07 ·
  related to WAY-08 · related to WAY-09 · related to WAY-10 · related to WAY-17 ·
  related to WAY-19 · related to WAY-22 · related to WAY-31 · related to WAY-37 ·
  related to WAY-39 · related to WAY-42 · related to WAY-55 · related to WAY-57 ·
  related to WAY-58
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* a fingerprint exists to flag what relies on an entry's wording (WAY-02), and for an
invariant the first thing that relies on it is its version: when the fingerprint differs from the
one on the main branch, the version rises unless the human deciding the change confirms a
correction, and every test citing the entry fails the gate until the foundation step checks it
against the new wording (WAY-57). The fingerprint moves on any change other than whitespace
(WAY-39), so it is the signal that asks whether the invariant now demands something else, and it
has to ask only where that can have happened. What an invariant demands is its sentence (WAY-22,
WAY-56). The rest of the entry says something else: a method says how the sentence is checked, and
a new test for the same meaning is accepted under WAY-08, with the panel and the human WAY-10
names, without touching the tests that cite the entry; a link names what the invariant rests on or
comes from, and is often written later, as a decision found behind a recovered invariant is
(WAY-58); a version and a declaration of a correction are worked out from the fingerprint and
cannot sit inside what they are worked out from; the recovered field records how the entry was
found. A raise caused by any of them would fail every citing test for a change that asks nothing of
the tests, and a flag raised for nothing is cleared without reading. The part map draws the same
line (WAY-42): its entry binds by one sentence, and the fields that change for other reasons stay
outside. This decision does not say what the sentence has to name, and that gap has a cost wherever
a condition that decides whether a commit makes the invariant true stands outside the sentence,
since a change to it raises no version, and whether it flags anything turns on whether the
invariant's link to that entry carries a fingerprint (WAY-66). Three kinds of such place can be named: a comparison with "the main branch", which gives
different answers against its tip and against the commit a branch left it from; a threshold whose
statistic or population sits in the method; and a list or a definition held elsewhere — in another
entry, in a template, in a section of the map — and reached through a word of the sentence, as the
directories of the process are held in WAY-09, whose list WAY-55 corrected in place. WAY-60 settles
where each may stand; how a change to the place holding the third reaches the
invariant is set by WAY-61 and WAY-62.
*Rejected:* the whole entry as the binding part — a new method, a link written later or a corrected
field would raise the version and fail every citing test for nothing; the method of checking inside
the binding part — a new test for the same meaning would fail every test citing the entry; a
fingerprint per field — every reference would have to say which field it relies on.
*Consequences:* the template of the invariants element marks the sentence as the binding part. Where
a condition that decides an invariant may stand is set by WAY-60; which links between entries carry
a fingerprint is set by WAY-66. The sentences of WAY-57 and WAY-58 that placed the version, the
declaration of a correction and the recovered field outside the fingerprint answered this question
in passing and lose those clauses (WAY-19); with them go WAY-57's consequence saying it answered
part of the question, the half of another that waited for it, and WAY-58's level 1 invariant on the
field and the fingerprint, the reason it gave for it and its consequence leaving open whether a
decision named later raises the version — it does not. Both are corrected in place and accepted
again (WAY-07). WAY-56's consequence that left this question open is corrected in place, with its
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
- **Relations:** derives from WAY-59@6ceadf4e · derives from WAY-22@52c514ca ·
  derives from WAY-56@3213162c · related to WAY-05 · related to WAY-06 · related to WAY-07 ·
  related to WAY-10 · related to WAY-12 · related to WAY-23 · related to WAY-31 ·
  related to WAY-34 · related to WAY-38 · related to WAY-51 · related to WAY-53 ·
  related to WAY-57 · related to WAY-58 · related to WAY-61
- **Outranks:** none
- **Verification:** level 1 — invariants: sentence-branch-names · sentence-gate-values. Level 2 for
  the rest — an agent compares the change with the decision:
  - complies: "every entry in the log has every field of the template"; "the list of violated
    invariants is a subset of its version on `{fork-point}`", the commit WAY-53 chose;
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
naming one is true or false by the hour, which WAY-22 rules out; what the main branch alone holds
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
chooses `{merge-onto}` by its own correction or version (WAY-07); WAY-57 chose `{fork-point}`, and
so does an invariant deriving from no decision (WAY-58).

### WAY-61/1 — How is an invariant's method of checking written, and how is its result read?

An invariant entry's method of checking is either a command the gate runs, which counts as a command
the product declares (WAY-38), begins with the name of the program it runs and is never a path alone,
or the path alone of a file a human assesses the product against; a command is the same on every run
and names no commit, branch or revision itself, and the commits its sentence names are values the gate
fills in from the template's closed list. A method checks what its sentence is about, as it stands on
the commit being checked, so a check fed input made up for it is the method of a sentence about that
check, never of one about the data the check reads. One run of a command may check many invariants,
and the result of an entry whose method is a command is the verdict that run records, in a format from
the template's closed list, for the entry's identifier and its current version; a verdict recorded for
another version is not its result, and a run that records no verdict for the entry never gives it a
pass.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map
- **Based on:** none
- **Relations:** derives from WAY-08@a0bbac21 · derives from WAY-16@dd3e3cc1 ·
  derives from WAY-54@39382a33 · derives from WAY-57@29edb491 · derives from WAY-38@6e10c3fd ·
  derives from WAY-60@c85d1ac0 · related to WAY-03 · related to WAY-05 · related to WAY-07 ·
  related to WAY-10 · related to WAY-12 · related to WAY-17 · related to WAY-22 · related to WAY-24 ·
  related to WAY-31 · related to WAY-34 · related to WAY-37 · related to WAY-43 · related to WAY-45 ·
  related to WAY-47 · related to WAY-48 · related to WAY-49 · related to WAY-50 · related to WAY-53 ·
  related to WAY-55 · related to WAY-56 · related to WAY-58 · related to WAY-59
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-method-form · method-gate-values ·
  gate-verdict-per-entry · gate-pass-without-verdict. Level 2 for what a method checks — an agent
  compares the change with the decision:
  - complies: "every entry in the log has every field of the template" names the decision guard
    run on `foundations/decisions.md`, and one run of the guard records a verdict for each
    invariant it checks; "a save of another version is rejected whole" names a test that hands the
    loader a save written in another version, since the sentence is about the loader; an exploratory
    test names the command that starts an agent on the working product with its steps; whether an
    image's text alternative describes it, after the accessibility check marked it incomplete
    (WAY-08), names the path of the checklist a person assesses the page against;
  - violates: a sentence about the real log names, as its method, the guard's test that feeds the
    guard logs made up for it; a test that runs the guard on the real log and asserts only its exit
    code is cited for one of the invariants the guard checks; an entry carries "runs as: script"
    beside its command; the gate gives every invariant a guard checks the guard's exit code; a
    command names the main branch where the sentence names `{fork-point}`.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

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
repository the guards are part of the product, so both kinds of sentence exist here, and each needs its
own method. One run checks many invariants, as one pass of a format guard checks every rule on its
template's list and one run of a test suite checks every test, so an exit code tells at most that
something failed, and not even that where a check was skipped; a run once per entry would repeat an
expensive run for each invariant it serves, which WAY-47 refuses for coverage. So the run records a
verdict for each entry, and a result is a record of a run, never a status written by hand (WAY-08,
WAY-53). A verdict counts only for the entry's current version, so that a raised version fails every
check still written for the old meaning, as WAY-57 has it for a test. Silence is never a pass, because
a check that quietly sees nothing passes (WAY-38). A comparison the sentence ties to a fixed commit
(WAY-60) needs that commit in the command; a command that resolved a branch or a revision itself would
answer by the hour rather than by the commit, which WAY-60 rules out, so the gate fills the commit in
from a closed list. Anything else in the command that varied between runs would make the verdict depend
on who ran it; what the runner's own environment supplies — its network access, and for a product
its interpreter — is settled neither here nor by WAY-63, while the-way's own interpreter is set by
WAY-89.
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
a method the gate cannot run to the invariants element is corrected in place to point to WAY-63.

### WAY-62/1 — What does an invariant entry name in the part map?

An invariant entry names the parts of the part map where a change can make its sentence false,
or `every` where a change to any part can. A change, against the commit its branch left the main
branch from, reaches an invariant that names `every` or a part the change touches, or whose method
names a file the change alters, whatever parts a file collecting entries gives that change
(WAY-44). The entry names no failure mode, critical flow or surface.

- **Change:** new decision
- **Scope:** invariants, part-map, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-16@dd3e3cc1 · derives from WAY-44@220f5b85 ·
  derives from WAY-61@c6bdfd7c · related to WAY-13 · related to WAY-18 · related to WAY-21 ·
  related to WAY-45 · related to WAY-46 · related to WAY-47 · related to WAY-54 ·
  related to WAY-55 · related to WAY-56 · related to WAY-60
- **Outranks:** none
- **Verification:** level 1 — invariants: invariant-part-names · invariant-part-form · change-reach.
  Level 2 for which parts — an agent compares the change with the decision:
  - complies: "every entry in the log has every field of the template" names `decisions`, and a
    new decision scoped to `gate` reaches it because the guard's method names the log; "every
    file git tracks matches the patterns of exactly one part" names `every`;
  - violates: that sentence on tracked files names `part-map`, so a file added under `gate/`
    never reaches it; an entry names the flow it guards.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* the gate runs the checks a change calls for (WAY-16), so invariants need what scope
gives decisions (WAY-21): parts, not paths, which would copy the map. Parts alone miss what WAY-44
does on purpose: a new decision scoped to `gate` touches `gate`, not `decisions`, and would never
reach the invariants on the log's form. The files a method names are read off the entry (WAY-54);
a change to them reaches it. A part missing from the list fails silently,
an extra one costs a run, so doubt names more (WAY-13). Failure modes and flows already name their
invariant (WAY-45, WAY-46), and a link is written at one end only (WAY-18).
*Rejected:* parts computed from what the method reads — a test's command names its test file, not
the product it reaches, and coverage exists only where a product produces it (WAY-47); every
invariant run on every change — WAY-16 turns that down; the invariant naming its failure mode, flow
or surface — one link written at both ends; the part holding the check — the sentence on tracked
files would never run when a file is added elsewhere.
*Consequences:* the template of the invariants element gives the field, marked as a judgment, and
its format guard checks the first two invariants above; what a change reaches is computed from the
map and the entries (WAY-44), and which checks it calls for beyond that stays with the task cycle
(WAY-16, WAY-55). In the file holding invariant entries, a change of an entry touches the
parts it names (WAY-44), and `every` all. WAY-56's consequence that left this question open is
corrected in place.

### WAY-63/1 — What results does the gate report for invariants, and which make its command fail?

An invariant's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the
template's closed list, or `error` otherwise. The gate reports a result for at least every invariant
the change reaches and every invariant a critical flow names, and its command exits non-zero when
a result it reports is `error`, a listed invariant's is `pass`, an unlisted invariant's or a fact's
is `fail`, or a run records a failure for no entry, and zero otherwise.

- **Change:** new decision
- **Scope:** invariants, gate, part-map, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-61@c6bdfd7c · derives from WAY-62@d9c21624 ·
  derives from WAY-08@a0bbac21 · related to WAY-16 · related to WAY-38 · related to WAY-45 ·
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
and every other missing verdict is `error`. `unchecked` leaves the command at zero, because WAY-60
and WAY-61 let an invariant enter before its method can run, and WAY-47 makes "unchecked" a state a
human reads, not one that stops work.
*Rejected:* `unchecked` making the command fail — every invariant entering without a method would
fail every change; an open list of reasons — whatever a check says of itself would pass; a third
exit code — nothing reads it; a human's verdict valid for the entry's version — it outlives every
change to the product (WAY-08).
*Consequences:* the template lists the reasons for `unchecked`, and the list grows by a new version
of this decision: the method reads `TODO`; the method is a path and no human verdict is in force;
the method's command or file is not declared or produced, except a command declared on the commit
the branch left the main branch from, whose drop makes the result `error` (WAY-38, WAY-47, WAY-67);
the method takes a commit the gate filled in as not existing; the entry stands on the list of
quarantined invariants at its current version, and the committer date of the commit being checked
is no later than the quarantine's end date, a later one making the result `error` (WAY-68). Where a
human verdict stands, what it names and how long it is in force is set by WAY-83. The facts whose
results the gate reports are those WAY-82 has it run. A declared command that cannot start, or a record off a closed list, is
`error`. Runs on a deliberate break, and the run WAY-58 asks for, give evidence, not results. Which
`fail` a listed violation excuses, and when a checked invariant may turn `unchecked`, is set by
WAY-67 and WAY-68.

### WAY-64/1 — Where do invariant entries stand, and what identifies one?

Invariant entries stand in one file, `foundations/invariants.md`, each under an identifier made of
words that no other entry or withdrawal line of that file, of the part map or of
`foundations/environment_facts.md` holds. An identifier the
file held on the commit the branch left the main branch from stays, as an entry or as a withdrawal
line naming its successors or `none`. Splitting or merging entries held there gives every result a
new identifier, and any other change keeps it.

- **Change:** new decision
- **Scope:** invariants, part-map
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · derives from WAY-56@3213162c ·
  derives from WAY-57@29edb491 · related to WAY-07 · related to WAY-35 · related to WAY-39 ·
  related to WAY-41 · related to WAY-45 · related to WAY-46 · related to WAY-62
- **Outranks:** none
- **Verification:** level 1 — invariants: identifier-holders · map-invariant-names ·
  invariant-identifier-form · invariants-file · invariant-identifier-persistence ·
  invariant-withdrawal-persistence · withdrawal-successors. Level 2 for what counts as a split — an
  agent compares the change with the decision:
  - complies: an entry drops a clause and keeps its identifier at a raised version
    (WAY-57); an entry that takes in a clause of another keeps its identifier, and the other is
    split;
  - violates: an entry drops a clause that reappears as a new entry and keeps its identifier; a
    changed meaning is withdrawn naming `none` and restated under a new identifier.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* words, as in the map (WAY-41): a citation says what it guards, and a mistyped word
seldom names another entry, as a number does. Unique across invariants and the map, so
a reference resolves without naming its element (WAY-39). One file: an entry naming several
parts or `every` (WAY-62) has no part's file. A version carries a change of meaning (WAY-57), so
the identifier changes only where one sentence becomes several or several one, and the withdrawal
line shows a citing test, or a decision that is never edited (WAY-07), where the meaning went. Only
identifiers that reached the main branch stay; a name dropped before was never cited there.
*Rejected:* a number with a prefix; one result of a split keeping the identifier — its citing test
is rechecked against that half, and nothing sends its reader to the other; a file per part;
identifiers unique only within the file; every identifier ever written kept.
*Consequences:* the template gives the file, the identifier's form and withdrawal list as the
map's, and the naming rule: what the sentence constrains, with an aspect where another entry
constrains the same, never what it demands (WAY-35). The entry on the main branch WAY-57 compares
with is the one holding the identifier there. The guard reads the identifiers of the map and of the
facts file, and the map's guard the invariants file; the facts file joins the space by WAY-75. A flow and a failure mode name an invariant by its identifier, and a
flow keeps its test.

### WAY-65/1 — How does a check cite its invariant, and which files are invariant tests?

A check cites each invariant it gives a verdict for as `invariant: <identifier>/<version>`, and a
run records no verdict for an invariant its check does not cite. The file holding such a check,
and each file it reads and names there as `data: <path>`, are invariant tests on the commit the
branch left the main branch from or on the commit being checked.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, relation-model, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-03@4fa941a4 · derives from WAY-17@ab01c0e5 ·
  derives from WAY-57@29edb491 · derives from WAY-61@c6bdfd7c · related to WAY-12 ·
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
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* WAY-61 already makes a check that records verdicts for invariants it cites an
invariant test; this decision gives that citation its written form and settles which files carry
it. One run checks many invariants (WAY-61), so a citation stands at the check that gives the
verdict, and a check is the smallest unit whose outcome a run records on its own — a test for a
test runner, a rule's report for a guard. A file cited on either commit counts, so a change that
drops a citation or deletes the file is still a change to a test. A recorded save a test compares
a load against is named on `data:` by the test that reads it, the dependent end (WAY-17).
*Rejected:* the paths a method names as the invariant tests — a method names the data its
sentence is about, not a file that checks anything; one citation per file — one broken check
fails all it serves (WAY-61); only files citing on the commit being checked — dropping a citation
frees the file.
*Consequences:* the template gives the `invariant:` and `data:` lines, in the comment form of the
file's language. Several checks citing one invariant in one run pass only when each of them does.
A path a human assesses against is no invariant test: a change to it reaches its invariant
(WAY-62), and the human verdict lapses (WAY-63).

### WAY-66/1 — Which links beside an invariant's sentence carry a content fingerprint?

An invariant entry's *Derives from* and *Rests on* carry the content fingerprint of each entry they
name, and its *Part* carries none. A change to that fingerprint reaches the main branch with every
invariant carrying it, each checked against the new wording and carrying the new fingerprint.

- **Change:** new decision
- **Scope:** invariants, decisions, relation-model, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · derives from WAY-17@ab01c0e5 · related to WAY-12 ·
  related to WAY-21 · related to WAY-31 · related to WAY-39 · related to WAY-57 ·
  related to WAY-59 · related to WAY-60 · related to WAY-61 · related to WAY-62
- **Outranks:** none
- **Verification:** level 1 — invariants: link-fingerprint-presence · link-fingerprint-value. Level
  2 for checking against the new wording — an agent compares the change with the decision:
  - complies: WAY-05 gets a new wording; the same change carries its new fingerprint into every
    invariant naming it in *Derives from*, and rewords with a raised version any invariant whose
    sentence no longer holds;
  - violates: a script renews every stale fingerprint in `foundations/invariants.md` with no one
    reading the invariants that carry them.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* an invariant derived from a decision, or resting on a fact, stands on what that entry
says (WAY-17), and a decision is verified through its invariants (WAY-12), so a link left on ground
that has moved verifies nothing and nothing shows it. The fingerprint is the mechanism WAY-02 already
sets for a reference that relies on wording, applied here as WAY-31 already applies it between
decisions, and one mechanism serves every element (WAY-39). *Part* names where a change can break the
sentence, not what it means, as a decision's *Scope* names parts bare too (WAY-21); fingerprinting it
would flag every invariant in a reworded part for nothing. How a place holding a condition without a
fingerprint is read, and how a change to it reaches the invariant, are not this question: a method
already reads what its sentence is about (WAY-61), and a change already reaches an invariant through
*Part* or through a file its method names (WAY-62).
*Rejected:* plain identifiers — a reworded decision would leave its invariants unflagged, what WAY-02
already forbids; a fingerprint on *Part* — a part names where a change can break the sentence, not
what it means, and a reworded responsibility would flag every invariant in the part, as a decision's
*Scope* names parts bare too (WAY-21); a renewed link raising the invariant's version — every citing
test would fail the gate with the sentence unchanged.
*Consequences:* the template of the invariants element gives both links with `@<fingerprint>`, and
its format guard checks the level 1 invariants above through the relation model's script (WAY-39).
What a fact's fingerprint covers is set by WAY-78; until the element has entries, an
invariant writes a fact it rests on as `TODO — <the fact, with its source>`, as a decision quotes one
in *Based on* (WAY-17). WAY-59's and WAY-60's passages that left this question open are corrected in
place.

### WAY-67/1 — What does the main branch hold where an invariant is not met?

An invariant the product does not meet stands, by identifier and current version, on the derived
list `foundations/violated_invariants.md`. A listed `fail` leaves the gate's command at zero, and a
listed `pass` makes it fail until the same change drops the position. A position is added only by a
change of the foundation that a human accepts, never by a step of implementation.

- **Change:** new decision
- **Scope:** invariants, gate, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-53@aaeafada · derives from WAY-63@f16348c8 · related to WAY-08 ·
  related to WAY-10 · related to WAY-15 · related to WAY-28 · related to WAY-51 · related to WAY-57 ·
  related to WAY-58 · related to WAY-60 · related to WAY-61
- **Outranks:** none
- **Verification:** level 1 — invariants: gate-exit-code · violated-list-growth ·
  violated-position-version.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* a product the process enters already breaks some of what it should hold (WAY-28), and a
rule written to fit the code hides the intent (WAY-15); so the invariant stays whole, and its breach
is a counted debt, like the map's (WAY-51). Like the map's, the list grows wherever growing it is
cheap, so it takes the same ratchet. A position carries the entry's current version, so a new meaning
is not excused by a debt accepted for the old one. Whether a change may turn a checked invariant
`unchecked`, and when a dropped command is `error` instead, is a question about which result an entry
has, corrected into WAY-63 directly, not answered here.
*Rejected:* one list shared with the map's — its positions name parts and files, not entries (WAY-51,
WAY-53); an invariant left out until it holds — the gap WAY-60 rejects for a part left "not checked
yet" (WAY-51); a position without a version; a debt paid on a clock — WAY-51 sets no clock for the
map's debt, and a clock repays debt by weakening the rule; a mechanical addition-check keyed to a
changed fingerprint of the entry — a second gate for what WAY-10 already decides for any change to
this list.
*Consequences:* the template names the list as not produced from scratch (WAY-53) and gives its form.
A change to this list is a foundation change, so WAY-10's panel and a human decide it before it
merges (WAY-01, WAY-51). Invariants a product fails at entry go onto the list with the entering
change. An invariant that enters without a method is `unchecked` from its first commit, not debt
(WAY-60, WAY-63). WAY-63's closed list and exit rule, WAY-53's comparison commit, and the pointers in
WAY-58 and WAY-61 that left this to a decision on debt are corrected in place.

### WAY-68/1 — What happens to an invariant test that gives different verdicts on one commit?

An invariant test that records both `pass` and `fail` for one commit is answered by a foundation
change, quarantine last and never for an invariant a critical flow names. A quarantine stands in
`foundations/invariants.md`, names the entry's current version and an end date, and its
result is `unchecked` until the checked commit's committer date passes that date, then `error`.
Until it is answered, a recorded `fail` stays the entry's result on that commit, whatever a later
run records.

- **Change:** new decision
- **Scope:** invariants, gate, task-cycle
- **Based on:** a quarantine works with a clock: "Fix immediately … Quarantine: If investigation or
  fix will take longer than the required response time" (GitLab, Quarantine process,
  https://handbook.gitlab.com/handbook/engineering/testing/quarantine-process/). A rerun hides what
  it absorbs: it "encourages developers to ignore flakiness in their own tests" (Micco, Google
  Testing Blog, 2016, https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html).
- **Relations:** derives from WAY-08@a0bbac21 · derives from WAY-61@c6bdfd7c ·
  derives from WAY-63@f16348c8 · related to WAY-03 · related to WAY-10 · related to WAY-24 ·
  related to WAY-45 · related to WAY-60 · related to WAY-64 · related to WAY-67
- **Outranks:** none
- **Verification:** level 1 — invariants: quarantine-position-form · quarantine-flow-invariants ·
  gate-quarantine-result. Level 2 — an agent compares the change with the decision:
  - complies: a save-load test fails and then passes on one commit, and the panel accepts a wait
    for the load-finished signal instead of a fixed interval;
  - violates: a failing test is called flaky with no `pass` recorded on that commit; a fixed-wait
    failure is quarantined instead of fixed as a change of form; a green rerun is taken as the
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
*Rejected:* a position on the list of violated invariants — that list settles whether the product
meets an invariant, not whether a check is trusted (WAY-67); a quarantine field in every entry —
every entry pays for a rare case; a count of passes in a row to enter — k of n (WAY-08) decides
entry; the date of the run — the result would follow the hour;
deletion once the date passes, as GitLab has it — a clock repaying by weakening the check (WAY-67).
*Consequences:* `foundations/invariants.md` ends with a list of quarantined invariants beside its
withdrawn identifiers. A violated invariant may be quarantined, and its position on that list stays.

### WAY-69/1 — Who writes an invariant's sentence, its check and its deliberate break?

An invariant's sentence and a check that cites it come from separate acts by different agents, and
the deliberate break the check is accepted on is written from the sentence by an agent other than
the check's author, with that check and the files it reads out of its input.

- **Change:** new decision
- **Scope:** invariants, decisions, part-map, gate, task-cycle
- **Based on:** what a model sees of a check, it games: reward hacking "was more than 43× more
  common on RE-Bench tasks than HCAST tasks, perhaps because on RE-Bench tasks the model was able
  to see the entire scoring function" (METR, 2025,
  https://metr.org/blog/2025-06-05-recent-reward-hacking/). With the check in the loop the agent
  builds for it: "With the oracle in the loop, the score reaches near-perfect, but from a demo
  holding the tested behavior directly, the library left dead or absent" (Building to the Test,
  2026, https://arxiv.org/abs/2606.28430).
- **Relations:** derives from WAY-08@a0bbac21 · related to WAY-03 · related to WAY-05 ·
  related to WAY-10 · related to WAY-11 · related to WAY-16 · related to WAY-58 ·
  related to WAY-61 · related to WAY-65
- **Outranks:** none
- **Verification:** level 3 — the human deciding the foundation change assesses how the work was
  handed out, and the record of that decision names who and when.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-22

*Rationale:* a break chosen by the author of a check is aimed at what the check does, not at what
the sentence says, so the teeth WAY-08 asks for show only that the check catches itself. The same
holds for the check: written by whoever wrote the sentence, it inherits the reading that sentence
was written with, and a sentence two readings wide stays wide. Keeping the acts apart costs the
order of the work and nothing else, and is the move WAY-03 and WAY-10 already make: take the
oracle out of the hands of whoever is measured by it, rather than forbid its use.
*Rejected:* hiding checks from the executor — it costs honest work, and WAY-16 keeps one command
for an agent, CI and a human; one agent writing all three under a written rule not to aim a break
at its own check — a gate written in prose is not a gate (WAY-03); a field naming the writers —
nothing reads it (WAY-05), and the gate already reports the break WAY-58 asks for.
*Consequences:* the task cycle hands out the sentence, the check and the break as separate
instructions, and gives the record of a change its home; until then nothing in a change shows
which agent wrote what, and the human deciding the change is the only reader, so the decision
moves to level 1 by a field change once that record exists. A break written without the check may
pass for a reason the sentence does not name, and WAY-58's report is where that shows: the entry
is accepted only once the break makes the check fail (WAY-08). A check joins a file that other
checks already stand in, so this binds the act of writing a check, not the history of its file
(WAY-65).

### WAY-70/1 — What may an invariant test compute for itself?

An invariant test takes the input it asserts on and the value it expects written out, wherever the
code its invariant is about would otherwise compute either; only the side it compares against
comes from the run.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, relation-model
- **Based on:** none
- **Relations:** derives from WAY-08@a0bbac21 · related to WAY-03 · related to WAY-10 ·
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
the expected value is corrected in place to this wording and gains its citation (WAY-37, WAY-54).
Which files an invariant test names, so that a fixture or a builder of its input cannot be changed
underneath it, stays open — `gate/test_wording_reaches_dependants.py` imports its fixture and
names it nowhere, and it guards it today with an assertion that the fixture still matches a
literal.

### WAY-71/1 — Does every field of a foundation entry appear in every entry, and what may it hold?

Every field an element's template gives an entry of its kind appears in every such entry, holding a
value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there,
`TODO` that something is missing. The main branch holds `TODO` only in an invariant's or a fact's
*Method*, and in an invariant's *Rests on* until the facts element has entries. A guard reports a
missing field, or a word not given it, as an error.

- **Change:** new decision
- **Scope:** decisions, part-map, invariants, glossary, environment-facts
- **Based on:** none
- **Relations:** related to WAY-01 · related to WAY-05 · related to WAY-09 · related to WAY-17 ·
  related to WAY-38 · related to WAY-46 · related to WAY-54 · related to WAY-57 · related to WAY-58 ·
  related to WAY-60 · related to WAY-62 · related to WAY-63 · related to WAY-66
- **Outranks:** none
- **Verification:** level 1 — invariants: log-entry-field-presence · log-entry-field-words ·
  log-entry-merge-todo · map-entry-field-presence · map-entry-field-words ·
  invariant-entry-field-presence · invariant-entry-field-words · invariant-entry-merge-todo ·
  fact-entry-field-presence · fact-entry-field-words · fact-entry-merge-todo. Level 2
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
on*, where the fact stands with its source until it has an entry to name (WAY-66); keeping such an
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
- **Scope:** decisions, part-map, invariants, glossary, environment-facts
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

### WAY-73/1 — Which environment facts does an invariant's *Rests on* name?

An invariant's *Rests on* names every environment fact holding a condition that decides whether a
commit makes its sentence true, and no other fact. A fact holds such a condition when, read
otherwise, it would give some commit another verdict under the same sentence, or change a value
the sentence copies from it. A fact that is only a reason for a decision the invariant derives
from stands in that decision's *Based on* alone.

- **Change:** new decision
- **Scope:** invariants, decisions, environment-facts
- **Based on:** none
- **Relations:** derives from WAY-17@ab01c0e5 · derives from WAY-60@c85d1ac0 · related to WAY-04 ·
  related to WAY-12 · related to WAY-22 · related to WAY-38 · related to WAY-58 · related to
  WAY-61 · related to WAY-62 · related to WAY-66 · related to WAY-71
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the invariant "no script imports a module outside the standard library of Python
    3.14" rests on the list of that library's modules, and not on the finding about
    cargo-semver-checks that WAY-38 quotes in *Based on*;
  - violates: the invariant "every invariant test names an invariant" rests on the Ariane 501
    finding that WAY-17 quotes; an invariant bounding a page's load time by a threshold an
    outside standard sets reads `Rests on: none`, whether its sentence names the standard or
    copies the number.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-23

*Rationale:* WAY-17 makes the link mandatory, and "rest on" reads two ways: on invariants written
from this log, it gave both answers. *Rests on* is read by whoever reviews an invariant when a
fact changes. A fact that is only a reason moves no verdict: its change sends the decision to
review, and a new wording reaches every invariant naming it through the fingerprint in *Derives
from* (WAY-66). A fact holding a condition moves the verdict, or a value the sentence copies, with
nothing in the foundation changed: a fact of the world changes with no commit of the product, so
no change reaches the invariant through its parts (WAY-62), and *Rests on* is its only path there.
A fact about what runs the method — a tool, an interpreter, a model — holds no such condition: it
changes how faithfully the method reads the verdict, not the verdict. A fact's method is written so
that it does not matter where a command can do so (WAY-81), and the-way's own commands run on the
interpreter WAY-89 declares; whether an invariant's command must set the runner's configuration as
a fact's does is not settled.
*Rejected:* every fact in the *Based on* of each decision the invariant derives from — a change of
it flags invariants whose verdict does not move, and it still misses a condition no decision
quotes, as the list of the standard library above; the choice left to each author — the two
answers above.
*Consequences:* the invariants template states the rule and its test beside the links. An
invariant with no such fact reads `Rests on: none`, whatever its decisions quote.

### WAY-74/1 — What form does the-way's own record of a run take?

The-way's own record of a run is a JSON Lines file at the one `.jsonl` path the command names,
which git ignores and the gate clears before the run. It holds a line per verdict a check gives an
invariant or a fact, and per failure recorded for no entry. A line holds `check`, `verdict` as
`pass`, `fail` or `unchecked` beside a `reason` its element's template lists, `invariant` or `fact`
as `<identifier>/<version>` or `invariant` as `null`, and at most `description`.

- **Change:** new decision
- **Scope:** invariants, gate, decisions, part-map, repository, environment-facts
- **Based on:** JSON Lines is "a convenient format for storing structured data that may be
  processed one record at a time" (https://jsonlines.org/); Python 3.14's `json` module reads it
  (https://docs.python.org/3.14/library/json.html).
- **Relations:** derives from WAY-61@c6bdfd7c · derives from WAY-63@f16348c8 ·
  derives from WAY-65@58d1f2c3 · related to WAY-38 · related to WAY-47 · related to WAY-48 ·
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
- **Approved by:** Mariusz, 2026-09-26

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
sentence on what the gate reads and WAY-53's rationale are corrected in place (WAY-07).

### WAY-75/1 — Where do environment fact entries stand, and what identifies one?

Environment fact entries stand in one file, `foundations/environment_facts.md`, each under an
identifier of words that no other entry or withdrawn identifier of that file, of
`foundations/invariants.md` or of the part map holds. An identifier the file held on the commit the
branch left the main branch from stays, as an entry or as a withdrawn identifier giving why and
naming its successors or `none`. Splitting or merging entries gives every result a new identifier,
and any other change keeps it.

- **Change:** new decision
- **Scope:** environment-facts, invariants, part-map
- **Based on:** a store of facts keeps a value it has shown wrong so that nobody enters it again:
  the deprecated rank "allows other users to know not to re-add the value to the item" (Wikidata,
  Help:Ranking, https://www.wikidata.org/wiki/Help:Ranking).
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-04 · related to WAY-17 ·
  related to WAY-41 · related to WAY-64 · related to WAY-73
- **Outranks:** none
- **Verification:** level 1 — invariants: environment-facts-file · fact-identifier-form ·
  identifier-holders · fact-identifier-persistence · fact-withdrawal-persistence ·
  fact-withdrawal-successors. Level 2 for what counts as a split — an agent compares the change with
  the decision:
  - complies: a fact's scope widened from one release to two keeps its identifier at a raised
    version; a fact joining JSON and JSON Lines is split into two entries with new identifiers, and
    the old one is withdrawn naming both;
  - violates: of that split, one half keeps the old identifier; a reworded fact takes a new
    identifier and the old one is withdrawn naming it.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* an invariant's *Rests on* and a decision's *Based on* reach a fact by its identifier
(WAY-17, WAY-90), so the identifier outlives a new edition, a new scope and a reworded sentence.
Words, as for parts and invariants (WAY-41, WAY-64), because a reference then says what it leans
on. One space of identifiers across the three files lets a reference resolve without naming its
element, the reason WAY-64 gives for invariants and the map. A fact shown false stays as a
withdrawn identifier with why, so that nobody writes it again and an older decision citing it still
finds where it went.
*Rejected:* a fact shown false deleted from the file — an older citation leads nowhere, and the
fact can come back.
*Consequences:* the template gives the file, the identifier's form, the naming rule — what the fact
is about, never its value or the edition it cites, as `json-text` rather than `json-rfc-8259` — and
the list of withdrawn identifiers with *Why* and *Successors*. Each of the three guards reads the
identifiers of the other two files (WAY-64). `foundations/environment_facts.md` joins the files of
the `environment-facts` part when its first entry is written.

### WAY-76/1 — How much does one environment fact entry hold?

An environment fact entry states in one sentence one fact that one edition of one source says, with
one reason to change, and its sentence says nothing that a commit of the product can make true or
false. Pages of one document published together in one edition count as one source, and two facts
from one edition about different things stand as two entries.

- **Change:** new decision
- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-22@52c514ca · related to WAY-04 · related to WAY-56 ·
  related to WAY-73 · related to WAY-75
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
about different things change for different readers. A sentence a commit can make false is an
invariant (WAY-22), and written as a fact it would never be checked on the commit that breaks it.
*Rejected:* the pattern rule of git and what `git check-attr` reports kept in one entry — the
second is about the tool that runs a method, and moves no verdict of the sentence (WAY-73); both
halves as two facts in *Rests on* — the second holds no condition of the sentence (WAY-73).
*Consequences:* the facts guard counts sentences, as the invariants guard does, and two facts in
one sentence are left to review. What `git check-attr` reports waits for the question whether a
method may rest on a fact, beside *Rests on*, which this decision does not settle.

### WAY-77/1 — What does an environment fact's *Holds for* name?

An environment fact names in *Holds for* what its sentence is true of — a tool and its version, a
platform, an edition, or the models a study measured — and never a word whose meaning moves with
the date, such as "latest"; where the source publishes no editions, *Holds for* says so. A scope
the product declares for itself stands in the sentence of an invariant, never in a fact.

- **Change:** new decision
- **Scope:** environment-facts, invariants
- **Based on:** none
- **Relations:** related to WAY-60 · related to WAY-66 · related to WAY-73 · related to WAY-76 ·
  related to WAY-78 · related to WAY-85 · related to WAY-89
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-scope-word. Level 2 for what a scope names — an agent
  compares the change with the decision:
  - complies: the modules of the standard library are a fact holding for CPython 3.14, while "the
    repository declares Python 3.14 in `.python-version`" is an invariant; the fact about JSON
    Lines reads "JSON Lines, which jsonlines.org publishes without versions";
  - violates: a fact's method reads the product's `.python-version` to choose which interpreter to
    probe; *Holds for* reads "jsonlines.org as read on 2026-09-26".
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a fact is true in the scope it names, and a claim true in a past scope is not refuted
when the scope moves on; what refutes it is a different claim for the same scope. "Latest" names
one release today and another tomorrow, so a verdict read against it would change with the date,
not with the world. The product's own scope is something a commit changes, so it belongs to an
invariant, and the two meet through links that already exist: an invariant depending on that scope
names it in its sentence and the fact in *Rests on* (WAY-73), and a change of the fact's scope
reaches it through the fingerprint (WAY-66). A source with no editions has no scope beyond its
subject, and a date read in *Holds for* would move the fingerprint at every re-reading.
*Rejected:* a fact whose method reads the product's declared version — its verdict would depend on
a commit of the product, which puts a sentence about the product into a fact; a script comparing
the product's scope with the fact's — *Holds for* is prose, and the writer of the invariant sees
both; the date read standing in *Holds for* for a source without editions — every re-reading
would raise the version and flag every entry resting on the fact for nothing.
*Consequences:* whether the version an invariant names lies within the fact's scope is seen by its
author, not by a script. A newer release of a named tool fails nothing: the fact about the named
release stays true, and what calls for moving the product to another release is a condition in
the *Review when* of the decision that chose it, as WAY-89 has it for Python. How a study's models
are named is set by WAY-85.

### WAY-78/1 — What part of an environment fact entry binds?

What binds in an environment fact entry is its sentence together with its *Holds for*, and the
entry's content fingerprint covers the sentence followed by the value of *Holds for*, computed as
WAY-39 says. The source, its passage and the date read, *Set by*, the method and a declaration of a
correction stay outside it, and no digest of the source's text is kept.

- **Change:** new decision
- **Scope:** environment-facts, relation-model, invariants
- **Based on:** none
- **Relations:** derives from WAY-02@af08ee5d · related to WAY-39 · related to WAY-42 ·
  related to WAY-59 · related to WAY-66 · related to WAY-77
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-fingerprint-input.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* the fingerprint exists to flag what relies on an entry (WAY-02), and what relies on a
fact relies on what it claims and on where the claim holds: read with another scope, the same
sentence gives a script another verdict — `import cgi` passes under 3.12 and fails under 3.13. The
source and its date change at every re-reading and every rebuilt page, and a flag raised by them
would be raised for nothing; a source that really changes fails the watch, which leads to a review
of the fact, and only a human in that review changes the sentence or the scope (WAY-82). The passage
quoted word for word is the one anchor the watch compares against at the address, so no digest is
kept beside it.
*Rejected:* the text of the source inside the fingerprint — a rebuilt page flags every dependent,
against WAY-82's rule that a change in a source is not a change of what is true; the sentence alone
— a widened scope passes with no signal; a digest of the passage read, kept beside it as a lock file
keeps one — the passage quoted word for word is already the anchor.
*Consequences:* the facts guard computes the fingerprint with the relation model's script. The
sentence names an edition of its source only where the product stands on that edition. A change
to the text of the source next to the quoted passage passes with no signal; that cost is accepted.
Every change of scope sends everything resting on the fact to review, since its fingerprint moves
(WAY-66, WAY-90). WAY-66's consequence that left this question to the element is corrected in place
to name this decision.

### WAY-79/1 — Is an environment fact entry versioned?

An environment fact entry carries a version number, starting at 1, and holds only its current
wording. When its fingerprint differs from its fingerprint on the main branch, its version is one
higher than there, unless the entry declares a correction naming both fingerprints and the human
deciding the change confirms, seeing both wordings, that the meaning is unchanged. A check citing a
fact at a version other than the current one fails the gate.

- **Change:** new decision
- **Scope:** environment-facts, relation-model, gate
- **Based on:** none
- **Relations:** related to WAY-10 · related to WAY-14 · related to WAY-43 · related to WAY-57 ·
  related to WAY-61 · related to WAY-75 · related to WAY-78
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-version-new · fact-version-changed ·
  fact-version-unchanged · fact-citation-version. Level 2 for what counts as a correction — a
  change after which some check citing the fact would need a different expected value is a raise;
  an agent compares the change with the decision:
  - complies: a typo in a fact's sentence is fixed under a declaration naming both fingerprints,
    and the human confirms it; a scope widened from CPython 3.14 to CPython 3.14 and 3.15 raises the
    version, and the probe citing the old version fails until it is checked against the new scope;
  - violates: "strongly recommended" becomes "required" under a confirmed correction; every
    citation moved to the new version by a script, with no one checking the probe.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a version pins the result of a method to the wording it checked: a probe cites the
fact by identifier and version, and fails once the meaning has moved under it, as an invariant test
does (WAY-57). Without a version, a probe's result would have to be keyed by the fingerprint — a
new mechanism in the guards and the runner, and harder for a person to read than a number. The
fact's history binds nothing, so only the current wording stays in the file, and earlier ones are
read from git.
*Rejected:* no version, corrected in place as the part map is (WAY-43) — a result of a method would
need the fingerprint as its key, a second mechanism beside WAY-57's.
*Consequences:* the template gives an entry its version and the form of a declaration of a
correction; the facts guard computes what the version must be. The guard compares an entry with
its state where the task branch left the main branch; where there is no main branch it compares
nothing, says so, and every entry stays at version 1. Who counts as the human deciding the change
for a fact follows the rule WAY-14 leaves to each element, and where the confirmation is recorded
is not settled here, as WAY-57 leaves it for invariants; until then the guard reports a declared
correction as unconfirmed, never as agreeing.

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
- **Relations:** derives from WAY-61@c6bdfd7c · related to WAY-08 · related to WAY-38 ·
  related to WAY-63 · related to WAY-65 · related to WAY-73 · related to WAY-74
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-method-form · fact-citation-target ·
  fact-verdict-citation. Level 2 for what a command asks and what it sets — an agent compares the
  change with the decision:
  - complies: the fact on path patterns runs `git -c core.ignorecase=false check-attr` on patterns
    the page's rules decide; the fact on SHA-256 probes the digests NIST publishes for it; the fact
    on JSON watches `obsoleted_by` of its RFC and that its passage still stands;
  - violates: a probe asks `git --version` and compares the number; a probe relies on the git
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
*Rejected:* a kind of method named beside it — the form already says it (WAY-54, WAY-61); a probe
asking for a version number — it trusts the label over the behaviour; the runner's configuration
recorded as a fact in *Rests on* — it changes the method's fidelity, not the sentence's truth.
*Consequences:* a command whose program is not yet declared or produced is written out in full all
the same and is unchecked for that reason, and a fact with no verdict for any other reason results
`error`, as WAY-63 has it. Where the environment cannot be made irrelevant — a model that runs a
method — it is configuration read off the product (WAY-54), and the deliberate break shows the
method's fidelity, which holds only where the break gives high confidence of detection. A command
records its verdicts under the key `fact` (WAY-74). WAY-73's rationale is corrected in place to name
this decision. Where the probes of this repository's own facts live in the part map is set when its
first fact is written.

### WAY-82/1 — When does an environment fact's method run, and what fails its watch?

A fact's method runs on every change that enters or rewords its entry or alters a file its command
names, and by a clock: one command, run on the main branch, that runs the method of every fact,
records each verdict and exits non-zero on a `fail` or an `error`. Elsewhere a fact's `fail` stops
no change; a watch fails on a published change to its edition or when its passage no longer stands,
and an announced revision fails nothing.

- **Change:** new decision
- **Scope:** environment-facts, gate, task-cycle
- **Based on:** a test of an external service runs to the service's rhythm, not the code's: "these
  tests need to be based on the rhythm of changes to the external service", and its failure starts
  work rather than stopping it: "A failure in a contract test shouldn't necessarily break the build
  in the same way that a normal test failure would. It should, however, trigger a task to get things
  consistent again" (Martin Fowler, ContractTest, 2011, https://martinfowler.com/bliki/ContractTest.html).
- **Relations:** derives from WAY-60@c85d1ac0 · related to WAY-24 · related to WAY-61 ·
  related to WAY-62 · related to WAY-63 · related to WAY-74 · related to WAY-81 · related to WAY-83
- **Outranks:** none
- **Verification:** level 1 — invariants: gate-fact-run · fact-clock-exit · gate-exit-code. Level 2
  for what fails a watch — an agent compares the change with the decision:
  - complies: RFC 8259 gaining `obsoleted_by` fails the watch of the fact citing it; NIST's notice
    that it will revise FIPS 180-4 fails nothing; the passage quoted from jsonlines.org vanishing
    from the page fails its watch;
  - violates: a change touching no fact fails the gate on a fact's `fail`; the clock's command
    exits zero while a fact results `fail`.
- **Review when:** the design of the task cycle begins · check by: 2026-10-02
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* the world changes with no commit, so a fact's verdict inside the gate of an unrelated
change would depend on the date, which WAY-60 and WAY-61 rule out for a verdict. The clock gives
the world a rhythm of its own. On a change that enters a fact, rewords it or alters the file that
pins its tool, the repository does change the fact, so the gate runs it there, and its `fail` fails
the gate as WAY-63 has it. A human re-reading carries its own date (WAY-83), so no entry needs a
rhythm of its own. A superseded, withdrawn or amended edition, or a vanished passage, leads to a
review of the fact but does not make its sentence false; only the human in that review changes the
sentence or its scope. An announced revision is a prediction: whoever wants to look ahead writes it
in *Review when* of the decision citing the fact (WAY-24).
*Rejected:* facts checked in every change's gate — the verdict follows the date; one review date
for every fact — the pace of change differs between sources; an announced revision failing the
watch once, with the review accepting it — a review with no possible outcome, beside the version; an
announced revision as a standing flag; what a failure opens settled now.
*Consequences:* for now the clock only reports: its command records the verdicts and exits
non-zero. This repository has no scheduler, so the clock runs by hand, and while nobody runs it no
change of the world is seen; a change is learned of on the day its edition is published. What a
failure becomes — a task, a branch, a message — is set when the task cycle is designed.

### WAY-83/1 — Where does a human verdict stand, and how long is it in force?

A human verdict on an invariant or an environment fact is a row of `foundations/human_verdicts.md`
naming the entry, its version, the verdict, who, when, the commit assessed and *Until*, and counts
only for the entry's current version. An invariant's verdict, with `none` in *Until*, lapses when a
change since that commit reaches the entry; a fact's lapses after the date in *Until*, which the
gate compares with the checked commit's committer date and the clock with the day it runs.

- **Change:** new decision
- **Scope:** invariants, environment-facts, gate
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
can read. A row in the repository is visible, corrected like any other line, and read by the guards
that know the entries. One file serves both elements, because the two verdicts differ only in when
they lapse: an invariant's when the product changes under it, a fact's when the world may have
changed, which only a date can stand for. A row counts only for the current version, so a new
meaning is never excused by an old verdict. The gate compares the date with the commit it checks,
as a quarantine does (WAY-68), so that its verdict follows the commit; the clock runs against the
world, so it compares with the day. The first case waits already: who can open this repository can
be read only with the credentials of whoever sets it.
*Rejected:* the verdict in a commit message — invisible to a reader of the foundation, never
corrected, and its author is often an agent; waiting for a second case — the rule on verdicts with
a date would stay dead.
*Consequences:* both templates name the file and give its row as
`| Entry | Version | Verdict | By | On | Commit | Until |`; the invariants template's place that waits
for this decision is corrected to it, and WAY-63's consequence on how long a verdict is in force
moves here. The file is written by hand and is no element's entries, so the invariant
`foundation-file-kinds` names files an element's template names. The guards check a row's form and
that the entry exists; the gate reads the row. The part that holds the file, so that a change to it
reaches both row invariants, is set with the first verdict written.

### WAY-84/1 — How is a setting that people of the product change outside its repository written?

The current state of a setting that people of the product change outside its repository — who can
open it, a host's access rule — is an environment fact whose *Set by* names who sets it, and whose
method reads that state where it lives, or is re-read by that person where reading it takes their
credentials. A choice of such a setting is a decision only where the product declares it, and that
decision rests on the fact.

- **Change:** new decision
- **Scope:** environment-facts, decisions
- **Based on:** a host can hide the state it keeps from an anonymous reader: "GitHub uses a `404 Not
  Found` response instead of a `403 Forbidden` response to avoid confirming the existence of private
  repositories" (GitHub REST API documentation,
  https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api).
- **Relations:** related to WAY-17 · related to WAY-22 · related to WAY-27 · related to WAY-81 ·
  related to WAY-83
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: who can open this repository is a fact set by the repository owner and re-read by
    the owner, with a verdict dated until the end of the quarter, and no decision on its
    visibility is written, since nothing in the repository declares one;
  - violates: the same fact reads `Set by: none`; a probe decides the repository is private from
    an anonymous 404; a decision "the repository is private" is written where the product
    declares no visibility.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* such a setting changes with a click and no commit, so no change of the product reaches
what rests on it, and only a method run against the world sees it move — the path a fact has.
Written without who sets it, it reads like a law of nature; *Set by* tells the person reviewing a
failed run whom to ask. Where the state can be read only with the setter's credentials, a secret on
the clock's machine would be a new failure of its own, so the setter re-reads it and the verdict
carries its date (WAY-83); an anonymous 404 cannot tell a private repository from a missing one. A
decision exists where someone chose and the product says so; elsewhere nothing was chosen, and a
decision would be one no commit could check.
*Rejected:* a bare fact without who sets it — it reads like a law of nature; a decision and a fact
for every such setting — a decision where nobody chose anything; a command holding a token on the
clock's machine — a secret, and a new reason to be unchecked; a verdict put together from an
anonymous 404 and the repository's own `origin` — its fidelity depends on who runs it.
*Consequences:* the template gives the field *Set by*, `none` for what nobody in the product sets.
A change between two re-readings goes unseen, which costs little while nothing this repository
links to is private. A fact about a setting set outside the product, such as the visibility of the
repositories this one links to, reads `Set by: none` and is probed anonymously; its list grows with
every link, and the invariant copies the list from the fact.

### WAY-85/1 — How is a finding of a study written as an environment fact?

A finding of a study stands as an environment fact recording what the study measured, in the
version of the paper its source names, with *Holds for* naming the measured models by the dated
identifiers the study gives, or by its own names where it gives none. That the agents of this
process behave the same is a prediction, written in *Review when* of each decision citing the fact
as a state a script can check, never in the fact.

- **Change:** new decision
- **Scope:** environment-facts, decisions
- **Based on:** a study names the models it measured: "GPT-5, o3, o4-mini, GPT-4.1, Claude Opus
  4.1, Claude Sonnet 4, Claude Sonnet 3.7, and Qwen3-Coder" (ImpossibleBench v1, § 3.1,
  https://arxiv.org/abs/2510.20270v1). A model's publisher keeps a state for each model, among them
  "Retired: The model is no longer available for use" (Anthropic, Model deprecations,
  https://platform.claude.com/docs/en/about-claude/model-deprecations).
- **Relations:** related to WAY-03 · related to WAY-17 · related to WAY-24 · related to WAY-77 ·
  related to WAY-80 · related to WAY-90
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the finding behind WAY-03 is a fact holding for arXiv:2510.20270v1 and the eight
    models it names, and WAY-03's *Review when* reads "no model in the scope of fact
    `impossiblebench-test-modification` is Active, or a study of an Active model is found";
  - violates: the fact says "Claude models change tests" with no version and no models; the fact
    carries a field saying the finding still applies to the agents of this process.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a finding has two layers. What a paper in a given version measured on given models is
true for good and checked by re-reading the paper. That the agents of this process behave the same
is a bet that ages as the measured models leave service, and a bet already has its mechanism in the
log: *Review when* with a state and a date (WAY-24). Kept in the fact, it would be a second
mechanism for predictions, and the fact would stop being true or false today (WAY-04). A script can
check the transfer when the fact names the measured models and a publisher's table gives their
states.
*Rejected:* the transfer as a field of the fact — a second mechanism for predictions beside WAY-24,
and a fact that is no longer true or false today.
*Consequences:* the same condition is repeated in every decision citing one finding, about eight
in this log. Where a study gives no dated identifiers, the script checking *Review when* resolves
the names it gives through the publisher's table of models; that script does not exist yet. A
decision that already waits for another state, as WAY-03 waits for the design of the task cycle,
needs *Review when* to hold more than one state, which takes a change of the decision template.
WAY-03 is rewritten on this pattern when the citations of *Based on* become fact entries, and its
condition is met the day it is written.

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
  related to WAY-76 · related to WAY-88
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
catalogue or takes on a binding obligation (WAY-05); a fact that nothing names is caught by WAY-88
already.
*Consequences:* a requirement of an adopted catalogue is a fact whose source is the edition, the
requirement's identifier and its text word for word, and an invariant taking a condition from it
names it in *Rests on* (WAY-73); WAY-58's consequence that left this to the element is corrected in
place to name this decision. The field and the script are built on the first product that adopts a
catalogue or a binding obligation; the first in reach is the CC BY licence of the icons of the game
`loop`.

### WAY-87/1 — How does an obligation from outside raise the criticality of a part?

An obligation from a law or a contract that raises the criticality of a part enters the part map as
a failure mode of that part, whose detection names an invariant resting on the environment fact of
that obligation.

- **Change:** new decision
- **Scope:** part-map, environment-facts, invariants
- **Based on:** none
- **Relations:** derives from WAY-46@b0cef8dd · related to WAY-04 · related to WAY-13 ·
  related to WAY-73 · related to WAY-86
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a part storing players' personal data records the failure mode "personal data is
    kept past the period the law allows", detected by an invariant that rests on the fact that the
    law applies;
  - violates: a part carries a field "minimum criticality: high" citing the law; the obligation is
    noted in a part's responsibility with no failure mode.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* WAY-46 left an obligation from outside with no path into the map. The path exists
without a new field: a failure mode raises a part's criticality, raising needs no reason (WAY-46),
and the chain fact → invariant → failure mode carries the obligation to the part, so that a change
of the law reaches the invariant through its fingerprint (WAY-66). A floor field would change
WAY-46 and the map's script, and none of the three products in reach holds data under such an
obligation.
*Rejected:* a floor of criticality as a field of the fact, read by the map's script beside failure
modes, flows and dependants — a change of WAY-46 and of the script with no reader today.
*Consequences:* criticality raised this way does not fall by itself when the obligation lapses —
the safe direction. A floor field comes back for consideration with the first product that holds
data under a legal obligation on its parts. Two ways a scoping standard differs from WAY-46 — what
can reach a system, not only what it depends on, and a separation confirmed by a test — are not
settled here. WAY-46's consequence on a part whose criticality is raised from outside is corrected
in place to name this decision.

### WAY-88/1 — May an environment fact stand that nothing rests on?

Every environment fact on the main branch is named by an invariant's *Rests on* or by a decision's
*Based on*; on a task branch, a fact that nothing names is a warning.

- **Change:** new decision
- **Scope:** environment-facts, invariants, decisions
- **Based on:** none
- **Relations:** related to WAY-05 · related to WAY-17 · related to WAY-73 · related to WAY-90
- **Outranks:** none
- **Verification:** level 1 — invariants: fact-dependants.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* a link is written at the dependent's end (WAY-17), so a fact that nothing names is
invisible from anywhere else, and its method goes on running for no reader. A task may write a fact
before the invariant or decision that needs it, so the branch only warns, and the merge demands the
link.
*Rejected:* no check — facts outlive their readers and are checked for nobody; an error on the task
branch as well — a fact written first, in the same task as what rests on it, would break the branch
midway.
*Consequences:* the facts guard builds the reverse index from the invariants file and the decision
log. A true fact whose last dependant goes is withdrawn in the same change, with why, or the merge
fails.

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
library that is one probe and one list of imports. `.python-version` joins the files of the
`repository` part.

### WAY-90/1 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?

Once the environment facts element has entries, a decision's *Based on* names a fact entry for
every citation that, stopping being true today, would send the decision to review — a finding about
agents or models, the behaviour of a tool the process uses — and quotes every other citation with
its source. A fact named there carries its content fingerprint, as `<identifier>@<fingerprint>`,
renewed as WAY-31 renews a relation's.

- **Change:** new decision
- **Scope:** decisions, environment-facts, relation-model
- **Based on:** none
- **Relations:** derives from WAY-17@ab01c0e5 · related to WAY-02 · related to WAY-31 ·
  related to WAY-66 · related to WAY-85 · related to WAY-88
- **Outranks:** none
- **Verification:** level 1 — invariants: based-on-fact-fingerprint · based-on-fact-fingerprint-value.
  Level 2 for which citations become entries — an agent compares the change with the decision:
  - complies: the finding of ImpossibleBench behind WAY-03 becomes a fact entry named in its *Based
    on*; the Ariane 501 finding behind WAY-17 stays quoted with its source;
  - violates: a precedent of how Packwerk handles its todo files becomes a fact entry with a probe;
    a finding about models stays quoted after the element has entries.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-26

*Rationale:* WAY-17 has decisions name the facts they rest on, and read literally it would turn
every citation into an entry — dozens, most with a method nobody needs to run. The test that keeps
what matters is the reader's: a citation whose change would send the decision to review is a fact
the decision rests on, and it needs an entry to be flagged by; a precedent, a past event or a
finding about people with no date on which it lapses sends nothing to review. The fingerprint is how
a change of the fact reaches the decision, as it reaches an invariant (WAY-66); a bare identifier
would leave the decision on ground that has moved with nothing to show it. A product outside that
pins this one and reads a surface of it is such a fact only when a decision about that surface
passes the same test.
*Rejected:* every citation as an entry, as WAY-17's consequence first read — dozens of entries with
methods nobody needs to run; a fact named in *Based on* by its identifier alone — a changed fact
would flag no decision; the partners of the part map's external context kept as facts linked from
the map — a new link with a fingerprint and changes to a template, a guard and two decisions, with
no known consumer.
*Consequences:* WAY-17's consequence is corrected in place to name this decision. The borderline
cases met when this log's citations are rewritten are settled by a human. About eight decisions
cite findings about models and two to four the behaviour of tools. Partners stay in the map's
external context, written by hand, so a consumer nobody recorded goes unseen. The first fact entry
also ends the `TODO` in every invariant's *Rests on* at the merge (WAY-71), so the change that writes
it writes the facts all of them wait for.
