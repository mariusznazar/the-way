# Decision log

The decisions of the-way, the process for building products. Entries follow
`elements/decisions/template.md` and are only ever appended.

### WAY-01 — What state does the foundation describe?

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

### WAY-02 — How do dependents learn that an entry has changed?

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

### WAY-03 — Who may change an invariant's test, and when?

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
