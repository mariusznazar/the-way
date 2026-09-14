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
