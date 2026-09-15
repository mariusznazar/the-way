# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and, on the main branch, are only ever appended.

### WAY-01/1 — What state does the foundation describe?

On the main branch, the foundation describes the product as it is. A task starts
implementation by changing the foundation, and the code follows; when the task closes, the
foundation again matches the current state. Roadmaps and plans do not change the foundation.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, task cycle
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
the foundation. Plans, roadmaps and hypotheses need a home outside the foundation.

### WAY-02/1 — How do dependents learn that an entry has changed?

Every foundation entry has a permanent number, and everything that depends on it — other
entries, tests, documents and code comments — refers to that number. A reference that relies
on the entry's current wording carries its content fingerprint (`WAY-17@<fingerprint>`), and
when the fingerprint changes, a script working on plain text files flags that reference for
review; plain numbers and version numbers (`WAY-17/2`) are never flagged. The fingerprint covers
only the part of an entry that binds — for a decision, its binding sentences.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, relation model
- **Based on:** none
- **Relations:** none
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - a reference whose fingerprint differs from its entry's current fingerprint is flagged;
  - a change to a decision's rationale alone leaves its fingerprint unchanged;
  - every referenced number exists.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-14

*Rationale:* without a mechanism, following a change through everything that depends on it
rests on a written rule and on memory. A product can hold hundreds of references to its entry
numbers, and after an entry changes nothing shows which of them went stale. A permanent number
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
- **Scope:** invariants, task cycle
- **Based on:** agents that a test stands in the way of change the test instead of the code,
  and Claude models do so especially readily: read-only tests are "a promising middle ground
  especially for Claude models, largely due to their preference of directly modifying test
  cases" (ImpossibleBench — Zhong, Raghunathan, Carlini, 2025,
  https://arxiv.org/abs/2510.20270; quote from the authors' summary,
  https://www.lesswrong.com/posts/qJYMbrabcQqCZ7iqm/impossiblebench-measuring-reward-hacking-in-llm-coding-1).
- **Relations:** derives from WAY-01 · related to WAY-02
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a merge request that changes an
  invariant test without an accepted foundation change fails the CI check.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
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
- **Scope:** decisions, invariants, glossary, part map, environment facts
- **Based on:** documentation that nobody maintains turns into "a culture of 'paper safety' at
  the expense of real safety" (Haddon-Cave, The Nimrod Review, 2009; summary:
  https://aerossurance.com/safety-management/nimrod-xv230-haddon-cave/).
- **Relations:** related to WAY-02
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: the foundation holds entries of the
  five elements only. Level 2 for the rule on new patterns — an agent compares the change with
  the decision:
  - complies: criticality enters the foundation as a field of a part in the part map;
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
today).
*Consequences:* each element is described in `elements/<element>/` of the process repository;
the description grows into the element's template as the element goes through its steps. Every
picture of the architecture — a diagram, a code map for an agent, a description — is generated
from the part map and the code.

### WAY-05/1 — How is a decision entry written?

A decision entry opens with one to three binding sentences — in the present tense, describing
a state that is to be true, concrete enough to check — followed by fixed fields that a script or
an agent reads, and by rationale, rejected options and consequences in prose. Every field
appears in every entry, holding a value, `none` or `TODO`, and a field stays in the template
only while someone or something reads it. The rules and examples in `elements/decisions/` are
the written form of this decision: a rule changes only together with a decision, and an example
is a verbatim copy of a version from the log.

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
- **Verification:** level 1 — invariants in working form:
  - every entry in the log has every field of the template;
  - binding sentences number one to three and contain no *should*, *will* or all-caps;
  - every example in `examples.md` matches its version in the log word for word;
  - a commit that changes `template.md` also appends a decision version to the log.
  Level 2 for the rule that every field has a reader — an agent compares the change with the
  decision:
  - complies: a new field enters the template together with the reader named in its table;
  - violates: a "notes" or "related artifacts" field that nothing reads.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* norms keep what binds short and checkable and put the explanation next to it; a
record written like a legal code, in a commanding voice, reads badly and is followed worse.
Agents generalise from the reasons they are given, so the reasoning stays in the entry, below
what binds. The present tense is used because a sentence with "will" or "should" describes an
intent, not a state. Fields are few because a field survives in practice only when someone reads
it in a specific activity. Every field appears in every entry because a field that is simply
missing cannot be told apart from one that was forgotten. The template is the process's code:
under WAY-01 it follows the decisions, never the other way round.
*Rejected:* prose entries without fields — nothing a script or an agent can read reliably;
full templates with many fields and relations — too many fields without a reader, and the tools
built on them did not survive; optional fields left out when empty — an intended gap and a
forgotten one look the same; a status field written by hand — a second copy of what the
sequence of versions already says; a single one-sentence statement as the whole entry — the
binding rule cannot be separated from its reasoning; normative capitals such as MUST — shouting
reads worse, not stronger; examples written for the template — an example with gaps teaches
gaps.
*Consequences:* adding or removing a field is a change of the template and therefore needs a
decision. Until the format guard exists, the rules of the entry hold only through review.

### WAY-06/1 — Where does a foundation change in progress live?

A foundation change in progress lives on the task's branch in the product's repository and
reaches the main branch in the same merge as the code that follows it.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, task cycle
- **Based on:** none
- **Relations:** derives from WAY-01 · related to WAY-03
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a commit that changes the foundation
  reaches the main branch only by merging a task branch. Level 2 for the rule that the change
  travels with its code — an agent compares the change with the decision:
  - complies: a task branch changes a decision entry and the code that follows it, and both
    reach the main branch in one merge;
  - violates: a task's foundation change is merged to the main branch ahead of its code; the
    code is merged and the foundation change is left for a later task.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* the main branch never describes something the product does not have (WAY-01), and
an abandoned task leaves no false description behind: its foundation change is dropped with its
branch.
*Rejected:* a foundation change kept on the main branch with a "designed, not built" marker —
the marker has to be removed when the task closes, and an abandoned task leaves a marked entry
for good.
*Consequences:* a change with no code behind it — a fix to a rationale, a decision recovered
from the existing product — also reaches the main branch through a task branch. A file conflict
catches two tasks that change the same entry in contradictory ways, but contradictory changes to
different entries merge cleanly; checking the merged foundation for consistency needs a
mechanism of its own.

### WAY-07/1 — From when may a decision entry no longer be edited?

An entry in the decision log is corrected in place until it reaches the main branch; until then
it gets no new version and no new decision about it. A correction that changes the meaning of an
accepted entry is accepted again. Once an entry is on the main branch, it is never edited, and
the log there only grows at the end.

- **Change:** new decision
- **Scope:** decisions
- **Based on:** none
- **Relations:** derives from WAY-06 · related to WAY-05
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - a merge to the main branch that changes or removes a line of the log already on the main
    branch fails the format guard;
  - a merge to the main branch adds at most one version of each number.
  Level 2 for acceptance after a change of meaning — an agent compares the change with the
  decision:
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
*Consequences:* the format guard compares the log with the main branch, not with the previous
commit. Until this log reaches the main branch, its entries are corrected in place. A copy in
`examples.md` follows its version when the version is corrected.

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
- **Verification:** level 1 — invariants in working form:
  - every invariant names a method of checking;
  - every invariant test fails on a deliberately introduced break of its invariant;
  - every result of a human inspection names who checked and when.
  Level 2 for the choice of method — an agent compares the change with the decision:
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

Only foundation elements reach the main branch of this repository, each with its template and
rules, a skill that writes its entries and a script that checks them.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, relation model
- **Based on:** none
- **Relations:** related to WAY-04 · related to WAY-06
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: every file on the main branch belongs to
  a foundation element that has a template, a skill and a script.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* the repository shows what the process looks like when it works, and an artefact
brought in on the side turns it into a store of material from the first day. The skill writes an
entry in the right form when someone runs it; the script catches a form broken by hand, by
another agent or by a merge. Until an element has all of them, it is a change in progress, and
under WAY-06 such a change lives on a branch.
*Rejected:* material merged to the main branch as soon as it is written; an element whose only
tool is a skill — the form then holds only while someone remembers to run it.
*Consequences:* element descriptions in `elements/` reach the main branch as templates with their
skills and scripts, not as descriptions.

### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?

A change to an invariant test or to the foundation is assessed by a panel of three agents: two
assess it independently, each from a different, named perspective and seeing only the diff and
the foundation, never the author's reasoning, and the third, on a different model where one is
available, settles between them. The panel decides changes of an invariant test's form — how the
test reaches the product: selectors, test data, waiting. Every other change the panel prepares
with the diff, its effects and a recommendation, and a human decides.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, task cycle
- **Based on:** a model assessing text is biased towards its own: "an LLM evaluator scores its own
  outputs higher than others' while human annotators consider them of equal quality"
  (Panickssery et al., 2024, https://arxiv.org/abs/2404.13076).
- **Relations:** derives from WAY-03 · related to WAY-07
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a merge request that changes an invariant
  test or a foundation entry without the panel's record — two assessments and a settlement —
  fails the CI check. Level 2 for what the panel decides — an agent compares the change with the
  decision:
  - complies: the panel accepts a new selector in an invariant test, and the change is merged
    without a human;
  - violates: the panel accepts a changed expected value in an invariant test; an assessing agent
    receives the author's reasoning.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

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
task's log what the foundation does not say — new rules, decisions made along the way, code
behaviour with no invariant over it — and proposes it as a foundation change for the panel. In
the same step it compares the foundation with the code in the parts the task touched. A periodic
review of the whole foundation runs alongside, independent of tasks.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts, task cycle
- **Based on:** none
- **Relations:** derives from WAY-01 · related to WAY-06 · related to WAY-10
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a merge request without the record of
  its return step fails the CI check. Level 2 for what the return step finds — an agent compares
  the change with the decision:
  - complies: a rule the implementer wrote into the code for an edge case comes back as a
    proposed invariant before the merge;
  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
    invariant covers.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* part of the foundation is learned only in implementation and in use. Agreement
between the foundation and the code has to be checked, because a task that missed the foundation
will not report it by itself. A step at the end of a task is the kind of step that goes missing
(WAY-01), so the merge waits for its record.
*Rejected:* the foundation changed only at the start of a task.
*Consequences:* the task's log needs a home, because the return step reads it. Comparing the
foundation with the code in the parts a task touched needs the part map's rule for assigning
files. How often the periodic review runs is set when the task cycle is designed.

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
- **Verification:** level 1 — invariants in working form:
  - every decision entry names its verification level, and a level 1 entry names at least one
    invariant;
  - a test that cites a foundation entry cites an invariant, never a decision.
  Level 2 for the choice of level — an agent compares the change with the decision:
  - complies: a decision on the product's direction is checked by an agent with a complying and a
    violating example;
  - violates: a decision whose rule a lint check could enforce is left at level 2.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-15

*Rationale:* an invariant is true or false on every commit, so a test can check it; a decision
about direction, trade-offs or non-goals often cannot be checked on a commit. Agents compare a
change well with a decision that is explicit and readable from the code, and fall short on
decisions that depend on deployment or on knowledge of the organisation — those stay with a human.
A pair of examples shows the agent where the line runs, which the binding sentences alone do not.
*Rejected:* a rule in code as the only method of checking a decision — decisions that cannot be
written as a rule would stay unchecked.
*Consequences:* the section "Verification" of the decision template is the written form of this
decision. Until the invariants element has its template, a derived invariant is named in working
form. A decision moves to level 1 once an invariant is derived from it.

### WAY-13/1 — What sets the weight of a task's process?

What a task touches, never its size, sets its process: an agent's analysis at the start of the
task settles whether it changes the foundation, which chooses its path, and the criticality of
the parts it touches, as the part map records it, together with whether the change can be
undone, set how sharply it is checked. Paths differ in their steps, never in the result a task
has to reach, and a task's size serves only as a signal to split it. A human decides on every
change that cannot be undone.

- **Change:** new decision
- **Scope:** task cycle
- **Based on:** formal approval does not make changes safer: "No evidence was found to support
  the hypothesis that a more formal, external review process was associated with lower change
  fail rates" (DORA, https://dora.dev/capabilities/streamlining-change-approval/). Changes that
  cannot be undone call for a different process: they are "consequential and irreversible or
  nearly irreversible – one-way doors – and these decisions must be made methodically,
  carefully, slowly, with great deliberation and consultation" (Jeff Bezos, 2015 letter to
  shareholders,
  https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm).
- **Relations:** related to WAY-01 · related to WAY-04 · related to WAY-10
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a merge request that changes a
  foundation entry, run on the path for tasks that do not change the foundation, fails the CI
  check. Level 2 for the rest — an agent compares the change with the decision:
  - complies: a one-line change to a stored data format, after which users' saved data no
    longer loads, goes through the sharpest checks and waits for a human's decision;
  - violates: a task gets the heavier path because of the number of lines it changes; a change
    that cannot be undone reaches the main branch without a human's decision.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
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
foundation. Setting how sharply a task is checked needs the criticality of parts from the part
map (WAY-04) and a way to recognise a change that cannot be undone, which nothing defines yet.
The paths and their steps are set when the task cycle is designed.
