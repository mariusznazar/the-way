# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and are only ever appended.

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
