# Independent review of assessment settlements

**Verdict: ready for the next cycle stage. Critical: 0. Important: 0. Minor: 0.**
Both assessment remarks are addressed. No fix is requested by this review.

Reviewer: `/root/reviewer`, the original whole-change reviewer, 2026-10-21.
Exact settlement range: `8726cc1c6b6b031ca94c6e867d0df1297c286c01..9a8bc5e7ae467a1dce81b4be830130c64337db0d`.
Previous reviewed range: `f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..8726cc1c6b6b031ca94c6e867d0df1297c286c01`.
Together the reviews cover the complete final product range
`f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..9a8bc5e7ae467a1dce81b4be830130c64337db0d` without a gap.

Repository-relative paths resolve from `C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks`.
Report filenames resolve from
`C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks/.runs/task-cycles/s7-cycle-remarks/reports`.
This review leaves tracked files, index and HEAD untouched and stops before the next stage.

## Strengths

- `foundations/decisions.md:7674` explicitly gives WAY-224 precedence over WAY-114 for candidate
  failure-mode questions, including the previously contradictory case of a recommended entry that
  changes no approved decision. The corresponding direct `narrows` relation at line 7682 and
  positive/negative verification examples make the boundary testable by source comparison.
- `task-cycle/skill/SKILL.md:129` keeps the original plan as the owner of the borrowed workspace.
  Passing the existing third argument fixes the path selection without changing the dependency,
  introducing another permanent plan or abandoning temporary heading conversion.
- The executable workspace evidence distinguishes extraction success from correct placement.
  It retains the failing workspace contract of the two-argument call and the passing explicit-output
  call, rather than treating both successful process exits as equivalent.

## Issues

### Critical

None found.

### Important

None found.

### Minor

None found. No new out-of-scope defect was identified.

## Settlement and task coverage

I agree with A and B after checking their source mechanisms, not merely the assessment's conclusions.
My earlier full-range review failed to identify these two omissions. Its approval/adapter conclusions
are therefore completed by this review of the corrections; the old report remains historical and
is not silently rewritten as if it had identified them.

**A — addressed, within scope.** The frozen task already requires the candidate question with a
recommendation and carries it in accepted settlement 2. The new third binding sentence records that
specific exception under WAY-25; it does not authorize other questions, change WAY-114 globally, or
permit recording an unaccepted candidate. I compared the complete current WAY-224 with WAY-25,
WAY-114 and the unchanged WAY-46, WAY-113, WAY-125 and task-cycle routes. The example where both
ordinary WAY-114 triggers are false now has an explicit answer: ask the candidate question in the
request. An ordinary entry outside that area retains WAY-114 and its already-recorded exceptions.
A task-commanded mode still does not require another question. There are three binding sentences.

**B — addressed, within scope.** I read the installed 6.4.1 `sdd-workspace` script and complete
`subagent-driven-development/SKILL.md`, using the previously read unchanged `task-brief` script,
and read the complete updated cycle skill. `task-brief` with three arguments uses the supplied
output directly. Resolving the workspace first from the original existing plan preserves its
marker/ledger identity. The normal method's report name is beside the brief, and review packages
continue to resolve from the original plan. Temporary conversion and removal remain explicit.
The instruction completes task item 6's compatibility behavior without changing its source plan.

All manual conclusions in this section have actor `/root/reviewer`, method full-diff comparison
plus source-path tracing, and evidence at the anchors above and the frozen `../task.md`;
command/exit/output fields are not applicable.

| Required meaning | Final coverage |
|---|---|
| Item 1: accepted task/plan answers WAY-114 | WAY-30 unchanged from the previous reviewed head; accepted-meaning boundary retained. |
| Item 2: both foundation-writing routes | Shared way of working and cycle foundation instructions unchanged in meaning; no renewed approval requirement added. |
| Item 3: assessment record location | README/critique routing unchanged. |
| Item 4: exclude commit messages from critic input | Critique filter unchanged. |
| Item 5: relation findings distinguished from expected pre-main errors | README rule unchanged; settlement guard evidence retains that distinction. |
| Item 6: temporary brief adapter | Corrected original-workspace identity, temporary conversion, original preservation and cleanup verified. |
| Item 7: candidate question content and before-merge answer | All fields and timing retained; explicit precedence now makes the question route consistent with WAY-114. |
| Item 8: human authorization versus typing | WAY-46, map template and map skill unchanged; no unaccepted record permitted. |
| Item 9: no-plan choices in the cycle record | Both task-template locations and refining instruction unchanged. |
| Settlement 1 | Accepted task/plan approval boundary unchanged and satisfied. |
| Settlement 2 | Candidate/authorization distinction retained; narrow precedence completes its required route. |

## Order, selection and sharpness

Independent git inspection confirms foundation commit
`6a39b73652e0cffeddd2a7454e365eae142a9e6d` changes only `foundations/decisions.md`; its child
`9a8bc5e7ae467a1dce81b4be830130c64337db0d` changes only `task-cycle/skill/SKILL.md`.
Foundation precedes operational prose. Settlement diff: two files, +15/-7.

| Final product file | Added | Removed |
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

I refreshed the foundation selection at the exact final head. All Scope fields were inspected by
the reviewer helper; the expected 207 IDs and heading lines equal the previous selection. The
nine candidate parts remain decisions, invariants, part-map, task-cycle, elements-common,
project-level, agent-instructions, environment-facts and product-guidelines. The previous complete
five-file foundation reads remain applicable: the 209 decision entries preceding WAY-224 are
byte-equivalent after newline normalization, and the settlement diff changes none of the other
foundation files. WAY-224 was reread whole, including rationale and rejected options. All reached
invariant entries are covered by the unchanged complete invariant read.
`reviewer-settlement-selection.json` records the refreshed revision, expected/read sets and no
missing match. No selection expansion was needed.

An independent whole-foundation incoming-reference search found no `WAY-224@` reference (rg exit 1,
empty stdout/stderr). A positive-control search found the real WAY-46 relation lines. The new
outgoing WAY-114 fingerprint was independently computed from its binding text and equals
`04b4f599`. Thus there is no incoming fingerprint requiring propagation, and the new outgoing link
is current. This search is not a claim that no operational WAY-224 references exist.

I reapplied `product-guidelines/reading.md` to the actual settlement and reused the complete,
unchanged part map. Coding/styleguide selection remains empty: product changes are process prose,
there is no UI or production-code change, and no guidelines directory exists. The ignored scenario
is evidence, not new product functionality. High criticality, reversibility and no changed
trust-boundary file are confirmed; no value of criticality or failure-mode entry changes. No
invariant sentence, method, check or version changes, so no new deliberate-break exercise applies.

## Weakest point and checks

The weakest point of this settlement is artifact ownership. I read the complete scenario helper,
its exact installed-script calls and full stdout/stderr, both initial and corrected results, and
the retained scratch artifacts. The same-basename plans make the control meaningful: the original
plan owns `.../.superpowers/sdd/plan`, while the temporary one causes `plan-temporary`. The old
two-argument extractor exits 0 but leaves the original workspace without its brief. The corrected
call supplies `.../plan/task-1-brief.md` and writes there. A later original-plan resolution returns
that same workspace. The assertions check unchanged marker and ledger bytes, the original plan's
bytes, required slice content including a fenced example, exclusion of the second slice, and
temporary-plan removal. The final retained plan hash and artifact locations were also checked
independently by my helper.

Evidence: `check-settlement-workspace.py`, `settlement-workspace-commands.json`,
`settlement-workspace-result.json`, `settlement-workspace-scenario-initial.txt`,
`settlement-workspace-scenario-corrected.txt` and `settlement-workspace-rerun.json`.
The author executed this scenario; I inspected its implementation, outputs and artifacts without
rerunning it. The first run's exit 1 was an overly strict relative-marker assertion on Windows;
the corrected fixture validates file identity and byte preservation. The failure remains recorded.
The report is a fixture placed by the helper, not evidence of an actual implementer dispatch or
full-cycle execution. That limit is appropriate for this focused compatibility check.

Reviewer-executed verification command:
`python -B .runs/task-cycles/s7-cycle-remarks/reports/reviewer-settlement-check.py`, exit 0.
Full combined stdout/stderr and exit: `reviewer-settlement-check.txt`. Exact subprocess argv,
working directory, exits and complete stdout/stderr for the metadata/search checks:
`reviewer-settlement-checks.json`. They include HEAD/status, ordered commit paths, settlement and
combined numstats, incoming-reference search and positive control. The source read used for byte
comparison is identified by git revision rather than archived as another copy of the decision log.
The helper's assertions additionally check unchanged entries, the fingerprint, refreshed selection,
guideline absence and retained scenario artifacts. No test suite or full gate was rerun by me.

Author evidence records 228 focused passing tests (169 decisions, 41 task-cycle, 18 instruction),
plus form/relations/whitespace checks in `settlement-checks-foundation.json` and
`settlement-checks-operational.json` with full output paths. I read the complete target-aware
decision output: exit 1, exactly three changed pre-main copies and four approval placeholders,
no fingerprint error, five overdue-review warnings plus placeholder warnings and two unchecked
history categories. The invariant relation output is reported as exit 0 with one unchecked
history category. These are not a full-gate pass. The root's required final checks remain its
responsibility; earlier 971-test evidence is not relabeled as run on this new head.

## Recommendations

Proceed with the completed settlement review. Preserve the prior review plus this report and their
exact ranges. Keep failed/unchecked evidence and replace approval-link placeholders at the existing
request step. The author report says the author/assessor different-model prerequisite still needs
repair by the orchestrator; this review does not certify that repair. Do not present this code
review as a replacement for the required independent assessment or human merge acceptance.

## Declined to judge

The previous review's complete list is preserved verbatim below. These are retained limitations
and considered boundaries, not newly graded defects or silently approved omissions. In addition,
the author/assessor model-independence repair is owned by the orchestrator and not verified by this
source review; no code anchor applies. The assessment-settlement author report identifies that
outstanding prerequisite, so the next-stage handoff must retain it.

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
