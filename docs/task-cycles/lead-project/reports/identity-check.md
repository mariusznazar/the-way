# Independent evidence-check correction

Base: 9ae98fe0b8421c5b486785a462648f51f9c50f08.
Head: a9e766d99672bf3c7693ebd4a5519e7fb8d30acf.
Commit: test: require task provenance for plan-state evidence.
Only changed tracked file: project-level/test_plan_state_invariant.py.

## Contract and independence

Authority: complete identity-check-handoff.md and identity-check-contract.md at foundation
commit 9ae98fe0b8421c5b486785a462648f51f9c50f08. Contract identifier remains
project-plan-state-evidence/1; WAY-153 fingerprint is 9874911d and the final invariant sentence
fingerprint is d7b8cc0b. The exact shared Method remains:

python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl

Read the named record template, task template, plan template, cycle start/record instructions
and this author's existing evidence check. The initial combined read exceeded a tool output
limit in the middle of the existing test; an additional read recovered the missing range.
No reader source, specification, implementation plan, production algorithm, operational author
report or next-stage input was read. No children, code repair, subprocess-check change, push,
assessment dispatch or deliberate break was performed.

## Fixture correction and independent literal oracle

Positive cycle fixtures now carry existing Task source and Task relation fields, an Artifacts
link to accepted-task.md and the frozen original task's Project relation. The source is the
original absolute task-document path with approval date. Its relative ../plan.md relation is
anchored by that original source location; an archived copy need not live beside the plan.
No UUID, new metadata field, globally unique name, compulsory record basename or current/frozen
content-equality requirement is introduced.

Both distinct project directories contain independently valid complete definitions/plans with
the same title, task number, task slug and basenames. They differ by their original source
locations. Thus a basename, title, number or slug cannot distinguish their tasks. The other
plan's frozen task correctly relates to its own plan through its own original source path.

All 18 existing methods and their assertions remain. Their positive fixture writers gained
identity-bearing records and frozen tasks; fresh remote publication commits the complete cycle
directory. Their original boundaries remain: local proof only starts, fresh reachable proof
composes or completes, and readiness/fetch/path/history/conflict constraints remain necessary.

Nine new cases use literal expected outcomes:

| Case | Exit | Proposals | Observation |
|---|---|---|---|
| Owned archived record named delivery-notes.md | 0 | ready for cycle -> in cycle; in cycle -> done | exact archive/commit/ref evidence |
| Owned frozen task after current source editorial change | 0 | both transitions | exact commit/ref evidence; content equality is unnecessary |
| Other plan's same-named integrated record, current ready row | 1 | none | conflict for current task |
| Other plan's same-named integrated record, current in-cycle row | 1 | none | conflict for current task |
| Other plan's same-named Git-listed live cycle | 1 | none | conflict for current task |
| Live same-named directory with no provenance | 0 | none | unchecked for current task |
| Archived cycle header alone | 0 | none | unchecked for current task |
| Integrated text file with no provenance, current in-cycle row | 0 | none | unchecked for current task |
| Unanchored relative task basename amid two valid plans | 0 | none | unchecked for current task |

The last case establishes insufficient/ambiguous association, without requiring one particular
human-readable wording for whether the unresolved source is called missing or ambiguous.
Every new test has its own invariant citation and a comment naming the production break it
catches. Expected proposal rows are independent literals; no production helper computes them.
The existing run_reader byte-preservation checks apply to every new case, including failures.
The ambiguity/conflict helpers require nonempty task-specific observation reasons.

## Actual verification and expected RED

Public source validation was executed for BOTH full definition/plan pairs:

- python -B project-level/readiness_check.py <definition>: exit 0, readiness: nothing found.
- python -B project-level/plan_check.py <plan>: exit 0, plan: nothing found.

Four validations passed. Full output and original temporary paths are retained in
reports/identity-check-fixture-validation.txt. The inputs were passed whole, not reduced copies.

Focused command:

python -B -m unittest discover -s project-level -p test_plan_state_invariant.py -v

Exit 1: 26 tests in 35.503s, seven failures. All original 18 cases passed with identity-bearing
positive fixtures, and the new filename-independence positive passed. The seven negative
identity cases failed as expected on the uncorrected reader: the three foreign-provenance
cases returned success instead of conflict and allowed progress; missing and unanchored
provenance cases still proposed start and/or done instead of withholding progress. Full exact
output is retained in reports/identity-check-focused-red.txt, including unsupported proposal
rows and commits. No failure was skipped or reclassified as pass.

The final added content-inequality positive ran separately:

python -B -m unittest discover -s project-level -p test_plan_state_invariant.py -k frozen_task_identity -v

Exit 0: one test in 1.638s, OK. It requires both supported transitions after an editorial source
change while keeping recorded provenance; it does not relax any state/freshness evidence.

The final file contains 27 methods: 20 observed passing across the two focused runs and seven
observed expected RED failures. The full shared Method and gate suite were intentionally not
rerun at this check-correction boundary, as the handoff assigns broad final verification to
the later implementation stage. The existing JSONL is therefore not claimed as a fresh verdict
for the corrected sentence/check. git diff --check exited 0 before the single-path commit.

## Protected subprocess check

project-level/test_plan_state_subprocesses_invariant.py stayed byte-for-byte read-only.
Its SHA-256 before and after:

01E7262B943A5055E3711E689FFFBB8037C0B3D68077CC9B49CB33DEBCB285C2

Its prior product result is neither rerun nor claimed as current verification here. Its imported
literal definition/plan/task constants are unchanged by this correction.

## Boundary and concerns

The committed independent-check boundary is reached with a meaningful expected RED, before
production repair. Source and frozen-task provenance are existing data formats, not executed
instructions. The record template's task identity fields and frozen-task relation are the
fixture authority; the tests do not prescribe a reader algorithm. The unanchored relative-source
case intentionally leaves ownership unestablished, and the future reader must expose that
without choosing one same-named project by guesswork.

No full gate, independent assessment or deliberate-break acceptance is claimed. Root owns
the code correction and final affected verification. The separate final code reviewer must
derive both affected final breaks after this assessment settlement is implemented, as the
handoff specifies. There is no unresolved question requiring a foundation or check edit before
that correction begins.
