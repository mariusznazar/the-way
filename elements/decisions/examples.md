# Decision entry examples

Verbatim copies of versions from this repository's decision log (`foundations/decisions.md`),
one for each kind of entry described in `template.md`. A version on the main branch never
changes, so a copy of it never goes stale; before the main branch a copy follows its version, and
the format guard checks that every example matches its version word for word.

Until a kind of entry has a real example, only its form in the template stands.

## New decision

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
