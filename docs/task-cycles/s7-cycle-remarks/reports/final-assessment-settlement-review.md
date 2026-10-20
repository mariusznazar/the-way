# Final affected review — assessment settlement R1

**Verdict: ready for the next cycle stage. Critical: 0. Important: 0. Minor: 0.**
R1 is addressed. No fix is requested.

Reviewer: `/root/reviewer`, 2026-10-21. Exact reviewed range:
`9a8bc5e7ae467a1dce81b4be830130c64337db0d..9c2a87c28ff0359bb0a48425fa23c5d8119a63a0`.
The complete diff and final `agent-instructions/README.md` were read. Product files, index and HEAD
remain untouched; only ignored reviewer evidence/report files were written. No agents were spawned.

Repository-relative anchors resolve from `C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks`.
Report filenames resolve from
`C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks/.runs/task-cycles/s7-cycle-remarks/reports`.

## Strengths

- `agent-instructions/README.md:32` now requires completion of the requested comparison when an
  operational error prevents it from running. It no longer treats the absence of a fingerprint
  finding after such an error as sufficient.
- The two expected pre-main finding classes remain explicit: changed copies of a decision version
  and placeholder request links. The change does not require treating those as an operational
  failure or adding a new normal-path command.
- The surrounding instruction still retains errors, warnings and unchecked work and prohibits a
  full-gate claim from partial checks. No test, guard flag, foundation meaning or artifact is added.

## Issues

### Critical

None found.

### Important

None found.

### Minor

None found. No out-of-scope defect was identified in this affected review.

## Coverage, scope and order

R1 is within frozen task item 5: the added target-aware runs must actually compare fingerprints.
Repair of an error preventing that comparison is a prerequisite of the requested operation. It
does not expand the task into correcting expected pre-main copy/placeholder findings. WAY-63's
complete entry expressly distinguishes a failing Git call from a valid unchecked result, and
WAY-160 retains actionable errors for the orchestrator. Both entries were reread in full.

All other eight task items and both accepted settlements are unchanged from the two prior reviewed
ranges. The candidate-question precedence and original-plan workspace correction remain intact.
No foundation entry changes here, so no new foundation-before-dependent-implementation order is
required; the earlier verified ordering remains valid.

This review completes the contiguous coverage:

| Report | Exact range |
|---|---|
| `code-review.md` | `f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..8726cc1c6b6b031ca94c6e867d0df1297c286c01` |
| `assessment-settlement-review.md` | `8726cc1c6b6b031ca94c6e867d0df1297c286c01..9a8bc5e7ae467a1dce81b4be830130c64337db0d` |
| This report | `9a8bc5e7ae467a1dce81b4be830130c64337db0d..9c2a87c28ff0359bb0a48425fa23c5d8119a63a0` |

Settlement diff: one file, +3/-3. Final product range:
`f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..9c2a87c28ff0359bb0a48425fa23c5d8119a63a0`.

| Final changed file | Added | Removed |
|---|---:|---:|
| `agent-instructions/README.md` | 7 | 4 |
| `elements/common/critique/SKILL.md` | 3 | 2 |
| `elements/common/way_of_working.md` | 3 | 2 |
| `elements/part-map/skill/SKILL.md` | 5 | 3 |
| `elements/part-map/template.md` | 5 | 3 |
| `foundations/decisions.md` | 75 | 19 |
| `foundations/invariants.md` | 6 | 6 |
| `project-level/task/skill/SKILL.md` | 3 | 2 |
| `project-level/task/template.md` | 5 | 3 |
| `task-cycle/skill/SKILL.md` | 24 | 10 |
| **Total** | **136** | **54** |

## Sources, guidelines and sharpness

The settlement changes the integration instructions owned by agent-instructions, affecting existing
verification behavior rather than adding a responsibility. The broad nine-part foundation selection
from the complete task remains a safe superset. No foundation file differs from the previous
reviewed head; all 207 expected Scope matches and prior complete reads of all 210 decisions and
the other four foundation files remain applicable. `reviewer-final-selection.json` records the
new revision and reuse rationale. I refreshed the particular execution-error context through
WAY-63, WAY-160 and both actual guard callers/helpers. No new linked entry or fingerprint is needed.

The previously read `product-guidelines/reading.md` and complete unchanged part map still apply.
Guideline selection remains empty: this is process prose, without production code or UI changes,
and there is no guidelines directory. Read-only guard inspection does not turn this into a code
change. Criticality remains high, the edit is reversible, and no declared boundary file changes.
There is no invariant sentence/check/method/version change and no deliberate-break requirement.

## Weakest-point and failure-path verification

Actor: `/root/reviewer`. Method: manual tracing of the real guard helpers and their conditional
callers, then applying three cases to the complete revised guide. Command/exit/output fields for
these manual judgments: not applicable.

1. **Target cannot be read.** `elements/decisions/format_guard.py:1016` distinguishes a genuinely
   absent path from a Git failure. `:831` reports that failure and returns no merged log;
   `:1195`–`:1200` calls the fingerprint check only with a valid target and merged log. The invariant
   guard uses the same distinction through `elements/common/guard_shared.py:304`; its
   `elements/invariants/format_guard.py:1412` failure returns no merged decisions, and `:1634`–`:1645`
   requires merged decisions, target entries and facts before fingerprint comparison. Therefore
   an operational error can prevent the comparison while producing no fingerprint finding.
   The new README explicitly requires resolving that error. Invalid-target resolution is also
   covered by the inspected `find_commit` branches.
2. **Comparison runs and reports a stale reference.** The README still requires acting on the
   relation-fingerprint finding; the added qualification does not exclude it.
3. **Comparison runs with only pre-main copy/placeholder findings.** Those remain expressly
   expected. Their nonzero guard exit is retained as evidence, not mislabeled a successful full
   gate, and the instruction does not require changing the approved pre-main version policy.

The narrowest risk was that recovery wording would either leave an unperformed comparison
acceptable or inadvertently remove the intended pre-main exceptions. The three cases above show
neither outcome in the final text. I agree with the source-derived failure mechanism after reading
it directly. No live recovery was simulated and no guard was modified. This is sufficient for the
one-sentence instruction fix; it is not empirical evidence that an agent will always recover.
My earlier review did not flag the overly broad “act only” wording; this report completes that
conclusion after the final assessment found it, without rewriting the historical report.

## Check evidence and limits

Reviewer metadata checks ran from the worktree, all exit 0. Exact argv, exit and full stdout/stderr
are retained in `reviewer-final-checks.json`: `git rev-parse HEAD`; `git status --short`;
`git log --reverse --format=%H %P --name-only` for the exact settlement range;
`git diff --numstat` for that range and the final product range; and `git diff --name-only` for the
settlement range restricted to foundations. They confirm the exact head, clean tracked state,
one README-only commit, final counts and unchanged foundation. No test suite was rerun by me.

The author evidence is in `final-settlement-before.json` and `final-settlement-checks.json` with
their complete-output paths. I read the actual post-change instruction-check and test output:
18 agent-instructions tests pass; the mechanical check exits 0 with the unchanged private
`AGENTS.md:20` path warning, zero errors and three size information lines. The author's whitespace
check exits 0. These are focused evidence, not a substitute for the root's final required checks.
The root is running those separately; this report does not relabel earlier test results as run
on this head. Existing approval placeholders, overdue-review warnings and unchecked categories
remain unaffected.

The previous assessment-model concern now has a replacement `final-independent-assessment.md`,
which identifies assessor gpt-6.1-sol and author gpt-6-astra and assesses the complete previous
product range. This review reads that report and settles its only requested code change; it does
not independently audit harness model/session metadata or reopen the assessment.

## Recommendations

Proceed with this reviewed head and preserve all three review ranges. Retain the existing
warnings/unchecked evidence, complete the root-owned final verification, and swap approval-link
placeholders through the established request step. No additional implementation edit or review
round is requested here. This verdict is not authorization to merge.

## Declined to judge

The initial review's complete list is retained verbatim below as historical boundaries. Its
model-compliance limitation remains; the previous settlement review's model-independence concern
is now accompanied by the replacement assessment identified above. I did not independently audit
its harness identity (no product-file anchor). Final required-check execution and human merge
acceptance remain outside this review boundary. No live operational failure/recovery was exercised.

- **General counterarguments for every question / a new relation-only guard flag:** explicitly
  excluded by the frozen task. The diff does not implement either; I did not demand them.
- **Future model compliance or measured effectiveness of these prompts:** the supplied traces and
  adapter run establish instruction behavior and extraction mechanics, not repeated agent-run
  outcomes. No measurement was supplied or fabricated.
- **Completing existing foundation debt:** overdue reviews, missing methods, absent coverage and
  pre-existing instruction warnings are visible limitations, not regressions created by this
  change. They do not justify rewriting unrelated foundation entries in this task.
- **Calling expected pre-main errors a new guard defect:** rejected after reading the actual
  diagnostic output and the existing integration route. The ordinary form checks and the extra
  fingerprint inspection serve different purposes. Placeholder replacement still belongs to the
  later request-creation step; this review does not approve leaving it unresolved at integration.
- **Independent foundation assessment or human merge acceptance:** outside this review boundary.
  The correct report location/input restriction is reviewed, but its later execution is not
  claimed complete here.
- **External-source freshness of unchanged environment facts:** their recorded content and
  relevance were read; their external publications were not reverified. This task changes no
  fact or underlying empirical claim.
- **Ordinary “correction to the open request” versus the glossary's invariant-entry correction:**
  considered and set aside. The new rule explicitly names the open request, adds an authorized
  entry through the normal correction stages, and neither declares an invariant Correction nor
  permits keeping its version after a changed meaning. No concrete versioning ambiguity or
  bypass follows from this use; existing process decisions also use the ordinary sense.
- **Final-slice extraction retaining the plan's trailing shared sections:** the installed script
  runs until the next Task heading, so the final slice may include those sections. This does not
  alter the source plan or add another slice, and it does not defeat the requested compatibility
  fix. The supplied executable scenario proves first-slice separation; it is not a claim that
  every possible plan shape was executed.
