# Independent subprocess-check repair

Base: 114c68960670e31a878ff00fbdf9ed5c00689089.
Only authorized changed product file: project-level/test_plan_state_subprocesses_invariant.py.
Author: invariant_check, separate from sentence author and reader author.

## Sources and boundary

Read the complete repair handoff and isolated repair contract, the complete current entries
project-plan-state-evidence/1 and project-plan-state-subprocesses/1, WAY-69/1, WAY-149/1 and
WAY-153/1, complete public record/task/plan templates, this author's existing subprocess check
and its independently authored literal CYCLE_RECORD fixture. The existing selective foundation
reading identifies project-level as the only touched part; the directly applicable testing and
provenance entries were refreshed against this base. WAY-153's current fingerprint is 9874911d.
The installed Superpowers 6.4.1 TDD and writing-good-tests instructions were read at the initial
independent test-authoring stage and applied here as assertion-first RED then fixture repair.

No plan_state.py content, production reasoning, reviewer report/mutation, identity implementation
report, operational cycle ledger, task specification or implementation plan was read. Hashing
the protected production file verifies preservation and does not disclose its source. No child,
foundation change, production change, evidence-check edit, deliberate break, second assessment,
push or next-stage dispatch was performed.

## Change and independent positive control

The successful scenario now requires these literal proposal rows, exactly and without extras:

- propose 1 report-download: ready for cycle -> in cycle
- propose 1 report-download: in cycle -> done

It also requires the retained literal PR pointer https://example.invalid/pull/41, exact archive
directory and integration header refs/remotes/origin/delivery with the independently published
commit. This establishes complete identity-bearing evidence reading before accepting the
Git-only observation verdict. Merely returning 0 or moving a fetched ref cannot pass it.

The positive input now uses existing record fields: original absolute Task source with approval
date, Task relation: plan item, an Artifacts link to the retained accepted-task.md, that task's
literal Project relation pointing to the original plan, and Request URL and status containing
the PR pointer. Both record and frozen task are committed and published before the observation.
The plan and original task remain outside the product repository. The PR URL is fixture data;
no host lookup is performed by the check.

The audit observer is unchanged. Its nonempty trace assertion, executable identity assertions,
old exit-code checks, successful real-ref movement and failed-remote unchanged-ref assertions
are preserved. The failed-fetch/operational failure scenario remains a separate citing test.
No expected answer is derived from production helpers or output; commit IDs are values created
and read from the controlled publisher fixture, independent of the reader.

## Choices and costs

Leaving the old header-only archive would keep a passing program-start check while the reader
reports missing provenance, so the successful evidence-reading route could remain unexercised.
Repairing the existing fixture and asserting composed transitions plus retained pointer adds
small fixture maintenance but makes that missing route visible. This is the chosen repair.

Reusing the independently authored literal CYCLE_RECORD input avoids a duplicate record format;
it creates a dependency on that shared test input, while no expected observations or test methods
are shared. Writing another equivalent record literal would duplicate maintenance without
improving the independent output oracle. No production algorithm or required record basename
is introduced by either choice.

## Assertion-first RED and focused GREEN

Focused command, after adding output assertions but before changing the incomplete input:

python -B -m unittest discover -s project-level -p test_plan_state_subprocesses_invariant.py -v

Exit 1: two tests in 3.711s, one failure. The failed-remote check passed. The successful check
failed because neither required proposal was present. Actual output explicitly reported
missing recorded task provenance in cycle snapshot and no sufficient cycle trace. Full UTF-8
output: reports/subprocess-check-repair-red.txt. This is a real exposed incomplete positive
control, not a production defect or the reviewer's deliberate break.

After repairing only the fixture, the same focused command returned exit 0: two tests in
3.312s, OK. Full UTF-8 output: reports/subprocess-check-repair-focused-green.txt.

## Protected source preservation

Before and after hashes are identical:

- project-level/test_plan_state_invariant.py SHA-256:
  1BB9A2A2BAD076EC4A424278E3AE2958458C17B7B344209726A081791F50B206
- project-level/plan_state.py SHA-256:
  027A95F1F60C2E185555146015D168F26B39B574A3FE1CEE5FE680A39D554970

## Remaining limits

The unchanged audit observer covers standard Python process-start APIs in the reader interpreter,
not native API evasion or an impostor executable named git, and intentionally excludes programs
Git itself starts. Its Windows command-line branch is exercised on this host; POSIX execution
remains untested here. The two scenarios establish successful complete observation and an
operational failure path, not exhaustive input/path coverage.

This repair returns at the independent check-author boundary. A passing product run does not
accept the invariant or substitute for the final reviewer's independently derived acceptance
break under WAY-69/149. No full gate or new independent assessment is claimed.

## Final verification and committed boundary

Final head: f1f878ee5c847f6407bdb55823adca09244022be.
Commit: test: require complete evidence reading in subprocess check.
Only project-level/test_plan_state_subprocesses_invariant.py was explicitly staged and committed.
The final diff is 19 added and 3 removed lines; no observer code or prior assertion was removed.

Exact Method on final bytes:

python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl

Exit 0: 250 tests in 101.408s, OK. Full UTF-8 output is retained in
reports/subprocess-check-repair-method.txt. The JSONL was inspected by exact identifier:
project-plan-state-subprocesses/1 has 2 pass rows, project-plan-state-evidence/1 has 27 pass
rows, and the whole record has zero fail rows. These are actual product-run verdicts.

python -B gate/run_tests.py gate

Exit 0: 98 tests in 22.894s, OK. Full UTF-8 output is retained in
reports/subprocess-check-repair-gate.txt. Both suites ran against the same final test bytes;
no test edits occurred while they ran. git diff --check exited 0 before commit.

The isolated check repair is complete. Final reviewer acceptance break and any required
review/settlement remain the root's separately dispatched work. The protected hashes above
remain unchanged, and no source outside the authorized test was committed.
