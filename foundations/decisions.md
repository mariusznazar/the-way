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
today); assumptions as a kind of entry — anything inconvenient could be called an assumption and
escape checking, and a mandatory condition for disproving it with a review date narrows that way
round without closing it.
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
different entries merge cleanly; the search against the current main branch before the merge
(WAY-33) is what catches them.

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
- **Verification:** level 1 — invariants in working form:
  - every decision version records who approved it and when;
  - every version is approved by the approver the process rule gives for the parts in its
    scope, or by the one its *Approver override* names.
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
format guard checks only that every version records its approval, and every version in this log
is approved by Mariusz. Nothing yet settles who approves a decision whose scope spans parts with
different approvers. This decision covers decisions only; approval of other foundation entries is
set when their elements are designed.

### WAY-15/1 — What in a foundation is written by hand, and what is derived?

What can be derived from what the product executes — code, configuration, infrastructure as
code, runtime traces — is derived, never written by hand, and what is derived describes the
state. Rules are written by hand: what is allowed, what is critical and what the product
promises, which the code cannot show.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part map, environment facts
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
  is identical to what its generator produces on the same commit. Level 2 for what is derived
  and what is written by hand — an agent compares the change with the decision:
  - complies: the view of the decisions in force is generated from the log; the existing
    dependencies between parts are generated from the imports and compared with the allowed
    dependencies written in the part map;
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
edited by hand. Comparing the derived state with the rules needs the part map's rule for
assigning files (WAY-04).

### WAY-16/1 — How are the checks of invariants run?

The quality gate takes its checks from the methods of checking written in the entries, never
from a list written by hand, and runs the checks a change calls for with one command, the same
command for an agent, CI and a human.

- **Change:** new decision
- **Scope:** invariants, task cycle
- **Based on:** none
- **Relations:** related to WAY-08 · related to WAY-13 · related to WAY-15
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - CI runs no checking command other than the gate's command;
  - every check the gate runs comes from a method of checking written in an entry.
  Level 2 for the same command for everyone — an agent compares the change with the decision:
  - complies: the instructions for agents name the gate's command as the way to check a change;
  - violates: the instructions for agents list test and lint commands of their own.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
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
reports a method it cannot run, such as an inspection by a human, is not yet settled: it depends
on the template of the invariants element. Which checks a change calls for is set when the task
cycle is designed. Under WAY-09 the gate reaches the main branch of this repository only as part
of a foundation element, and no element holds it today.

### WAY-17/1 — Which links between foundation entries are mandatory?

Every link of the chain fact → decision → invariant → test is written in the entry that depends
on the other, and none is optional: a decision and an invariant name the environment facts they
rest on, an invariant derived from a decision names that decision, and an invariant test names
its invariant.

- **Change:** new decision
- **Scope:** relation model, decisions, invariants, environment facts
- **Based on:** an assumption about the world that no entry names escapes review: the inquiry
  into the failure of Ariane 5 found that "this decision was found directly in the source code.
  Given the large amount of documentation associated with any industrial application, the
  assumption, although agreed, was essentially obscured, though not deliberately, from any
  external review" (Ariane 501 Inquiry Board, ESA,
  https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report).
- **Relations:** derives from WAY-02 · related to WAY-04 · related to WAY-12
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - every invariant test names an invariant;
  - every invariant named in a decision's level 1 verification names that decision.
- **Review when:** none
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

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
with their sources in *Based on*; once it has them, every *Based on* in this log names them
instead. On the main branch, a fact learned after a decision is added to it by a field change.
Whether a decision's *Verification* keeps naming its invariants once they have entries of their
own is not yet settled: it depends on the template of the invariants element.

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
- **Verification:** level 1 — invariants in working form:
  - the view shows only the latest version of every number, and a single line for a repealed
    number;
  - every link written in the log is shown by the view at both of its ends.
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
- **Relations:** derives from WAY-02 · related to WAY-07 · related to WAY-18
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - the heading of every decision version has the form `### <prefix>-NN/V — <question>`, and the
    versions of a number are consecutive;
  - every version after the first gives a rationale for the change.
  Level 2 for one number per question and for sentences answered in passing — an agent compares
  the change with the decision:
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
- **Verification:** level 1 — invariants in working form:
  - every version after the first names a kind from the list;
  - the binding sentences are identical to the previous version for a rationale change, a field
    change and a challenge, and absent for a repeal.
  Level 2 for the choice of kind — an agent compares the change with the decision:
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
favour, or the change that settles it otherwise.

### WAY-21/1 — What is a decision's scope?

A decision's scope names the parts of the product it governs, taken from the part map, and never
file paths, so that the decisions governing a change are found from the files it touches through
the part map's rule for assigning files.

- **Change:** new decision
- **Scope:** decisions, part map, task cycle
- **Based on:** an agent loses rules as their number grows: "even the best frontier models only
  achieve 68% accuracy at the max density of 500 instructions" (IFScale,
  https://arxiv.org/abs/2507.11538), and a tool vendor advises keeping an agent's instructions
  short for the same reason: "target under 200 lines per CLAUDE.md file. Longer files consume
  more context and reduce adherence" (Claude Code documentation,
  https://code.claude.com/docs/en/memory).
- **Relations:** related to WAY-04 · related to WAY-11 · related to WAY-13 · related to WAY-14
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - every part named in a decision's scope exists in the part map, or, until there is one, in the
    working list of parts;
  - no decision's scope names a file path;
  - the decisions found for a change include every decision whose scope names a part the change
    touches.
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
*Consequences:* until this process has its own part map, the scope of its decisions names parts
from a working list: decisions, invariants, glossary, part map, environment facts, relation
model, task cycle. Finding the decisions for a change needs the part map's rule for assigning
files (WAY-04). Which other decisions a change is checked against — those that govern every task,
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
last rule, which belongs to WAY-12, is the written form of this decision. Until the invariants
element has its template, an invariant derived from a decision is named in working form in the
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
product without standing in its log; how a product's checks see them is not yet settled.

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
- **Verification:** level 1 — invariants in working form:
  - every *Review when* other than `none` names both a state and a date;
  - a check-by date that has passed without a later review entry gives a warning;
  - a review whose result is that the state has not come names a date in *Next check*;
  - a review that names a version of the decision points to a version that exists.
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
which belongs to WAY-31, is the written form of this decision. Until the view and the format guard exist, pending dates are kept only by the skill and
by whoever reads the log. Before the main branch, whether a passed date is answered with a review
entry or with the date corrected in place is not yet settled (WAY-07).

### WAY-25/1 — What settles a collision between two decisions?

Precedence between decisions is recorded pair by pair in *Outranks*: a decision names the
decisions that give way to it when both apply and collide, nothing follows along a chain, and two
decisions that outrank each other are an error. A collision between two decisions with no
precedence recorded is never settled by the agent that meets it; a human records the precedence
in one of them — by a new version on the main branch, by a correction before it.

- **Change:** new decision
- **Scope:** decisions, task cycle
- **Based on:** none
- **Relations:** related to WAY-07 · related to WAY-14 · related to WAY-20
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: no two decisions outrank each other.
  Level 2 for a collision with no precedence — an agent compares the change with the decision:
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
- **Scope:** decisions, task cycle
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
- **Scope:** decisions, invariants, glossary, part map, environment facts, relation model, task
  cycle
- **Based on:** none
- **Relations:** related to WAY-09 · related to WAY-17
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: no file in the repository contains a link
  into a private note collection or into a repository its readers cannot open. Level 2 for the
  reasoning in the entry — an agent compares the change with the decision:
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
- **Scope:** decisions, invariants, part map, task cycle
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
- **Approved by:** Mariusz, 2026-09-16

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
*Consequences:* an invariant recovered from behaviour needs a method of checking and a note that
it was recovered and its cause is unknown; the invariants element has no place for that note yet.
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
- **Verification:** level 1 — invariants in working form:
  - every inherited decision has *Origin* in the form `inherited — searched: <…>; found: <…>`;
  - the *Rationale* of every inherited decision is `unknown`, a quotation with its source, or
    attributed to the human who gave it.
  Level 2 for the agent's part — an agent compares the change with the decision:
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
- **Scope:** decisions, task cycle
- **Based on:** tools that guard principles in agent work refuse a quiet way around them:
  "Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or
  tasks—not dilution, reinterpretation, or silent ignoring of the principle" (GitHub Spec Kit,
  https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md).
- **Relations:** derives from WAY-01 · related to WAY-03 · related to WAY-06 · related to WAY-07 ·
  related to WAY-14 · related to WAY-21 · related to WAY-24 · related to WAY-25
- **Outranks:** none
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: a task branch whose code goes against a decision also carries a proposed narrowing
    of that decision, and the merge waits for its approver;
  - violates: a task branch whose code contradicts a decision that stays unchanged; a task's plan
    that records a "justified violation" of a decision.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
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
plain number. A change to a decision's fingerprint reaches the main branch together with every
decision that relates to it with a fingerprint, each checked against the new wording and carrying
the new fingerprint.

- **Change:** new decision
- **Scope:** decisions, relation model
- **Based on:** requirement tools that keep traceability between items store the state of the
  parent in each link: "Each link consists of the parent item UID and the fingerprint of the
  parent item. When the fingerprint of a parent item changes, the link is reported as suspect
  during validation" (Doorstop documentation,
  https://github.com/doorstop-dev/doorstop/blob/develop/docs/cli/validation.md).
- **Relations:** derives from WAY-02 · related to WAY-17 · related to WAY-18 · related to WAY-20 ·
  related to WAY-24
- **Outranks:** none
- **Verification:** level 1 — invariants in working form:
  - every `derives from` and `narrows` relation carries a fingerprint, and no `related to`
    relation does;
  - on the main branch, every fingerprint in a relation equals the current fingerprint of the
    decision it names.
  Level 2 for checking against the new wording — an agent compares the change with the decision:
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
wording of WAY-01 can take that reason away. A plain number points to whatever the other decision
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
drops the relation or changes with it. Until the format guard defines how the fingerprint is
computed, relations in this log carry plain numbers, and fingerprints are added in place once it
does. Which links between entries of other elements carry a fingerprint is set by those elements
(WAY-17).

### WAY-32/1 — What types of relation can a decision name?

A decision names its relation to another decision with one of three types, and the list is
closed: `derives from` — a higher decision this one serves; `narrows` — a decision this one
deliberately goes against in a narrower area; `related to` — any other link.

- **Change:** new decision
- **Scope:** decisions, relation model
- **Based on:** a relation word left without a definition drifts in use: the IETF "Updates" tag
  "is currently used for multiple different purposes, which leads to confusion …" (Kuehlewind,
  Krishnan, https://www.ietf.org/archive/id/draft-kuehlewind-update-tag-04.html).
- **Relations:** related to WAY-19 · related to WAY-20 · related to WAY-25 · related to WAY-31
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: every relation in a decision entry has
  one of the three types. Level 2 for the choice of type — an agent compares the change with the
  decision:
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
- **Scope:** decisions, invariants, glossary, part map, environment facts, task cycle
- **Based on:** in a product built before this process, a requirement that players log in and a
  decision to keep the game's whole state in the browser, with no server, were written in separate
  documents with no link between them; they contradicted each other, and nothing a change could
  flag connected them.
- **Relations:** related to WAY-02 · related to WAY-06 · related to WAY-10 · related to WAY-11 ·
  related to WAY-21 · related to WAY-25 · related to WAY-31
- **Outranks:** none
- **Verification:** level 1 — invariant in working form: a merge request that changes a foundation
  entry without the record of the search made when it was written and of the search against the
  current main branch fails the CI check. Level 2 for what the search covers — an agent compares
  the change with the decision:
  - complies: a new decision to keep the state in the browser is written, the search finds a
    requirement for player accounts in another part that nothing links to it, and the
    contradiction goes to a human before the decision is accepted;
  - violates: the search reads only the decisions whose scope overlaps; the search against the
    main branch was made before another task that changed the foundation was merged.
- **Review when:** the design of the task cycle begins · check by: 2026-09-23
- **Origin:** none
- **Approver override:** none
- **Approved by:** Mariusz, 2026-09-16

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
an overlapping scope. Until the other elements have entries, the foundation searched is the
decision log.
