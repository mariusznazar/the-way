# Independent invariant-check author: interface question

Author: /root/invariant_check, separate from invariant author and future reader author.
Source revision: 7b070c1b5697c42d416903fbfbf62f09dc8a5c62.
Authority read: invariant-check-contract.md, current project-plan-state-evidence/1, complete WAY-69/1, WAY-150/1 and WAY-153/1, complete part map, common rules, definition template and plan template. Existing test_plan_check.py was inspected for fixture form only. No spec, plan, frozen task, foundation-author report or reader implementation was read.

## Concrete question

The public output boundary says human-readable output names current states, proposed transitions and unresolved observations. It does not define how to distinguish an actual proposed transition from a mention of a rejected transition. Which stable textual record identifies a proposed transition for one task, and which record identifies an unresolved observation for that task?

For example, merely requiring the output to contain `in cycle` and `done` cannot distinguish a completion proposal from `in cycle: done is unsupported`. Prohibiting `done` rejects a legitimate explanation of why completion is unsupported. A loose substring assertion would therefore accept an unsupported-progress bug or reject a correct conservative report.

This question is about the observable boundary, not implementation. A minimal stable text prefix and task association would suffice; a JSON schema is unnecessary.

## Stage result

No test file or implementation was written. No deliberate break was written. No test command was run, no invariant verdict was recorded, and no missing-reader RED or passing check is claimed. Nothing was committed. The test-written boundary has not been reached; authoring waits for the concrete public observation convention as required by the handoff. Subsequent required work includes real temporary Git fixtures, meaningful positive/conservative assertions, byte preservation, recorded missing-reader RED, explicit test-path commit and independent reviewer deliberate break after implementation exists.

## Resumed: test-written boundary reached

The contract now defines task/propose/evidence/unchecked/conflict records, full remote-tracking integration refs, and existing origin/HEAD as the product integration declaration. I read those additions without reading the specification, implementation plan, frozen task, or foundation-author report. The source revision before test changes was 7b070c1b5697c42d416903fbfbf62f09dc8a5c62. There is still no reader implementation and I wrote no production code or deliberate break.

Foundation selection: the complete part map identifies project-level as the touched part (the only tracked changed path is project-level/test_plan_state_invariant.py). All current Scope fields, including wrapped values, were inspected by entry selection; 39 entries name project-level. Their selection is retained in invariant-check-foundation-selection.txt. Complete referenced WAY-69, WAY-150 and WAY-153 entries, current invariant, common rules, source definition/plan/task templates and the two Superpowers TDD sources were read. Selection output exceeded a tool output limit; additional chunk reads recovered the middle entries. No foundation entry was changed. The root owns the required independent assessment of this invariant-test change.

### Checks and independent expectations

The new file holds 18 citing test methods, each with its own invariant citation and a comment naming the production break it catches. Temporary bare remotes, normal repositories, real linked worktrees, real commits/pushes/fetchable remote updates and a file-transport shallow clone are used; no Git mocks or production helpers compute the evidence oracle. The definition fingerprint a3b6ab99 is an independently calculated literal. Positive fixture inputs are complete literal definition/plan/task texts. The task/plan/definition bytes are compared before and after every reader observation when the files exist.

Cases: listed live worktree; branch-only archived cycle; freshly published remote record composing both transitions; merged record after branch deletion; exact slug isolation; branch/message alone; unlisted neighbouring directory; failed fetch with cached completion; missing origin; origin default that no longer exists; another remote not obscuring valid origin; unavailable listed worktree; shallow history; done versus a live cycle conflict; draft plan; malformed plan; unapproved definition; unreadable definition. Product integration is delivery, not main/master. Original project documents are outside the explicitly supplied product repository, and paths contain spaces. Slash direction is normalized for identity-bearing evidence comparisons, preserving full paths and exact slug matching. Reasons are checked as visible unresolved records without freezing their prose. Proposal rows are asserted as exact unordered sets, so rejected-transition prose cannot masquerade as a proposal.

### Commands and actual results

1. Fixture validation used the literal test fixture through existing CLI programs (not the new reader):
   - python -B project-level/readiness_check.py <temporary definition>: exit 0, `readiness: nothing found`.
   - python -B project-level/plan_check.py <temporary plan>: exit 0, `plan: nothing found`.
2. Declared invariant method:
   `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
   Exit 1. Final run: 211 tests, 18 failures. Each new check fails on the missing reader diagnostic: `can't open file ... project-level/plan_state.py: [Errno 2] No such file or directory`. Assertions explicitly reject that diagnostic, including the unreadable-definition test, so an incidental exit 2 cannot count as a passing observation. Full captured output: invariant-check-red.txt. The JSONL contains 18 fail verdicts for project-plan-state-evidence/1 and zero failures belonging to other checks. No skips, no stub, no expected-failure decorators.
3. `python -B gate/run_tests.py gate`: exit 0, 98 tests, OK. Full output: invariant-check-critical-flows.txt.
4. `git diff --check`: exit 0 before both commits.

These failures are the expected missing-reader RED; they are not a passing evidence check. The test-written stage is complete, but the invariant has not passed and no full gate pass is claimed. After implementation, all checks must actually observe the intended behavior, and the separate code reviewer must derive and run the deliberate break from the invariant sentence.

### Files and commits

Only tracked path changed: project-level/test_plan_state_invariant.py.

- a029cbe215dc15f44f40220586a337544e24bf0e: test: define independent plan-state evidence checks
- 098d7df8550d04f0fd83343013231f568ea31ba3: test: respect declared origin integration with multiple remotes

Both commits staged only the explicit test path. Ignored report artifacts are under this reports directory; the declared JSONL remains .runs/project-plan-state-evidence.jsonl. The first ambiguous-remote expectation was corrected after the public origin-source clarification: two remotes alone cannot defeat the declared origin route. That is a contract correction to the test, with no reader implementation consulted.

### Remaining concerns and ownership

The tests intentionally stop before implementation. They cannot yet establish positive reader behavior or that the final reader's meaningful errors contain all needed evidence. A future independent review must inspect the test assertions and perform the deliberate break; passing these tests is not a substitute for that step. No PR-host outcome is invented, and no host executable is used by the fixtures. The foundation-stage independent assessment and integration acceptance belong to the parent cycle.
