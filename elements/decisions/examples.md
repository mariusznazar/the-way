# Decision entry examples

Verbatim copies of versions from this repository's decision log (`foundations/decisions.md`),
one for each kind of change of a decision version and for a review record described in
`template.md`. A version on the main branch never changes, so a copy of it never goes stale;
before the main branch a copy follows its version, and the format guard checks that every example
matches its version word for word.

Until a kind has a real example, only its form in the template stands.

## New decision

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
- **Relations:** derives from WAY-01@4deacf15 · related to WAY-02
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
