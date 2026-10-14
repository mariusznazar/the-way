# Slice 2 implementer report

Status: DONE. Boundary: committed Slice 2, before independent review. No subagents, reviewers,
push, foundation writes, task-backlog writes, or next-stage invocation by this executor.

## Authority, inputs and reading evidence

Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
Branch: `task/selective-document-reading`.
Input BASE: `3056064eedf9cc49404e74be7294f4078799cbc1` (confirmed HEAD before editing).
The root supplied Slice 1's independent approval; the consumed interface was the actual final
`Reading the foundation` section at this BASE, read in full, not the dispatch's summary.
The exact SDD `task-2-brief.md` was read first, then the Superpowers 6.4.1 implementer template,
frozen task and reviewed spec in full. The whole implementation plan was not loaded.

Input content fingerprints (SHA-256, identifying actual file bytes, not foundation fingerprints):

- `.superpowers/sdd/plan/task-2-brief.md`: SHA-256 `d1e89641188cb50c3ee8b49ff4f37057ca77274a33212267d898c01a3a64185b`.
- `.runs/task-cycles/selective-document-reading/task.md`: SHA-256 `dff4652dc2aa1b9a2b6dae1293f4cc5a8a3013983200da4c48e02ea1f2b852d6`.
- `.runs/task-cycles/selective-document-reading/spec.md`: SHA-256 `e606c789df997efa69d22eb3b845a526d8a7ca66cfe34ea1e10610339dc0f0dc`.
- `elements/common/way_of_working.md`: SHA-256 `9829af10836ea54dbcb9d1d449ae8960e3f5e81086b35d5525e620634c8b975b`.

Other reads: all six Change paths in full; `agent-instructions/README.md`;
`elements/common/critique/SKILL.md`; complete `foundations/part_map.md` and glossary;
`project-level/definition_template.md`, `project-level/plan/template.md`,
`project-level/task/template.md`, `task-cycle/record_template.md`; actual implementations
`project-level/plan_check.py` and `project-level/readiness_check.py` and their two named test files.
The skill conventions and code-review playbook named by user instructions were read, read-only.
Large command output was split into further reads when truncated, including spec, skill tail,
conventions opening, template table and foundation ranges.

Foundation source locations are the exact ranges in the brief. The temporary range extracts
`decisions-slice2-read.txt` and `invariants-slice2-read.txt` beside this report retain original
line numbers for working evidence; they are not new process artifacts or supported interfaces.
All selected decision entries were read with their fields, rationale and rejected alternatives.
The complete current Scope-field inspection includes wrapped fields; this log has only version 1
entries and no repeals. Touched parts from actual file assignments: `project-level`, `task-cycle`.
Expected versus selected comparison is in `task-2-scope-evidence.json`; no expected match missing.
The comparison verifies the declared selection, not automated proof of actual comprehension.

Actual loaded decision identifiers:

WAY-01/1, WAY-03/1, WAY-09/1, WAY-10/1, WAY-11/1, WAY-12/1, WAY-13/1, WAY-16/1, WAY-17/1, WAY-21/1, WAY-25/1, WAY-26/1, WAY-27/1, WAY-28/1, WAY-30/1, WAY-31/1, WAY-33/1, WAY-34/1, WAY-36/1, WAY-37/1, WAY-38/1, WAY-44/1, WAY-45/1, WAY-46/1, WAY-47/1, WAY-48/1, WAY-51/1, WAY-55/1, WAY-57/1, WAY-62/1, WAY-63/1, WAY-65/1, WAY-68/1, WAY-69/1, WAY-82/1, WAY-89/1, WAY-100/1, WAY-101/1, WAY-102/1, WAY-103/1, WAY-106/1, WAY-107/1, WAY-108/1, WAY-109/1, WAY-110/1, WAY-111/1, WAY-112/1, WAY-113/1, WAY-114/1, WAY-115/1, WAY-116/1, WAY-117/1, WAY-118/1, WAY-119/1, WAY-120/1, WAY-121/1, WAY-122/1, WAY-123/1, WAY-124/1, WAY-125/1, WAY-126/1, WAY-127/1, WAY-134/1, WAY-135/1, WAY-136/1, WAY-137/1, WAY-138/1, WAY-139/1, WAY-140/1, WAY-142/1, WAY-143/1, WAY-144/1, WAY-145/1, WAY-146/1, WAY-147/1, WAY-148/1, WAY-149/1, WAY-150/1, WAY-151/1.

Actual loaded invariant identifiers:

foundation-file-kinds/1, foundation-change-merge-route/1, invariant-method-form/1, invariant-test-break/1, repository-file-location/1, foundation-change-assessment-record/1, return-step-record/1, level-one-decision-invariants/1, verification-invariant-derivation/1, foundation-change-path/1, derived-file-content/1, ci-checking-commands/1, gate-check-source/1, view-versions/1, view-links/1, decision-scope-names/1, decisions-found-for-change/1, outbound-link-reach/1, foundation-search-record/1, script-language/1, script-imports/1, script-subprocesses/1, part-map-file/1, map-reference-target/1, file-part-assignment/1, path-pattern-reach/1, map-invariant-names/1, flow-coverage-parts/1, surface-promise-level/1, surface-declaration/1, promise-level-policy/1, known-violation-coverage/1, known-violation-currency/1, flow-test-location/1, invariant-citation-version/1, invariants-file/1, invariant-citation-target/1, data-line-target/1, link-fingerprint-value/1, environment-facts-file/1, fact-citation-version/1, fact-method-form/1, fact-citation-target/1, glossary-file/1, glossary-avoid-growth/1, project-definition-form/1, project-readiness-gate/1, project-technology-record/1, project-plan-form/1, project-plan-check/1, skill-entry-points/1, instruction-file-imports/1.

Expected Scope matches are all loaded IDs above except the additionally loaded WAY-12, WAY-17 and
WAY-31, which the brief supplies for linked verification/source semantics. No foundation entry
was edited, so this slice introduces no new WAY-33 writing/integration search record; existing
search domain and timings remain mandatory in the consumers.

## Implementation and files

- `project-level/skill/SKILL.md`
- `project-level/technology/SKILL.md`
- `project-level/task/skill/SKILL.md`
- `task-cycle/skill/SKILL.md`
- `task-cycle/plan/SKILL.md`
- `project-level/plan/skill/SKILL.md`

Five consumers now refer to the reviewed shared foundation method instead of their obsolete
local loading clauses. The project planner also uses that method, including decisions not already
listed by the definition. Define-project maps an idea before a diff; technology includes decisions
holding or constraining its choices; task relations and source reads remain unchanged.
The task cycle refreshes selection before its foundation step, return step and reconciliation.
Plan-task makes complete foundation entries the smallest entry range in a slice Read list.

Plan-project starts/resumes from complete heading/status/header/gate/version inspection and
inventories of all scope items, projected headings, exact questions and places, and all existing
tasks/dependencies/assignments/questions/phases/change-log locations. Complete source units are
read when needed and expanded by dependency or meaning before editing. New breakdowns cover all
scope, entries and exact questions. Sources remain original whole check inputs. One independent
critic reads the complete authoritative plan and every needed source unit without an author-set
inspection boundary. Existing post-critique checks, findings handling and human handover stay.
No names, descriptions, locations, parser, interface, test body or template changed.

## Choices, evidence, alternatives and costs

| Choice | Evidence and reason | Rejected alternative | Cost if wrong |
|---|---|---|---|
| Referral to one shared foundation method in each reader | Spec Applying the contract and Slice 1's actual shared section | Copying Scope/link/search algorithm into six skills | A future shared change requires checking its callers; copies would drift and cost repeated maintenance |
| One plan-project reading section called from start/resume and Read | Spec Selective definition and existing-plan reading; WAY-151 | Separate start and resume methods or a new selector/index | One section still requires agent judgment; duplicate methods could diverge and a new interface needs design/tests |
| Complete temporary inventories before choosing resumed work | WAY-151, exact task brief | Reading only nearby unfinished rows or retaining a second product plan | Inventory costs an initial global scan and may still be misread; local-only reading loses distant assignments |
| Explicit complete-plan critic input, independently expandable sources | WAY-146 and WAY-151; existing critique contract | Passing only author excerpts or letting author self-review replace critique | Critic can load substantial source material; limited inputs would let source omissions survive |
| Refresh at foundation, return and reconciliation points | Shared method requires refresh on revision/scope change; task-cycle stages already exist | Restructuring stages or trusting initial selection forever | Extra selection work at changed boundaries; stale selection would miss new governing decisions |
| Preserve whole-source reads outside plan-project and all ownership/approval rules | Frozen task out-of-scope and spec boundary | Extending document selection to technology/refine-task or changing stage organization | Larger source reads remain in those workflows; changing them here would exceed authorized scope |
| Existing suites and inspection walkthroughs, no literal instruction tests | Exact brief Checks; prose-only implementation | New parser/selector or tests mirroring text | Semantic behavior remains partly unchecked; string tests cannot prove agent understanding |

No unsettled design choice or source contradiction was found. Instructions remain English.
Scripted replacements read/write existing bytes or use newline='' and retain original endings.
Control-character scan found no non-tab/newline/carriage-return ASCII control characters.

## Verification

Commands run from the stated worktree on the final semantic content (later changes only wrapped
lines and restored the existing phrase 'newly learned', with no reader contract change):

| Command | Exit | Result |
|---|---:|---|
| `python -B gate/run_tests.py project-level` | 0 | 193 tests, OK, 0.323 seconds |
| `python -B gate/run_tests.py task-cycle` | 0 | 41 tests, OK, 0.491 seconds |
| `python -B gate/run_tests.py gate` | 0 | 98 tests, OK, 14.684 seconds |
| `git diff --check` | 0 | No whitespace errors, including after formatting cleanup |
| Read-only current Scope comparison | 0 | All project-level/task-cycle matches present; missing [] |
| ASCII control scan of six changed files | 0 | Clean |

No failed suite, warning, skip or erroneous output appeared. The original check implementations
were inspected: plan_check reads the entire plan and definition named relative to it; readiness
reads the entire supplied definition, and fingerprint processing remains unchanged. The existing
tests exercise missing coverage, exact questions, assignment/writer errors, cycles, preparatory
requirements, stale fingerprints, original relative paths and CRLF inputs. No production-code
RED/GREEN TDD steps apply to these Markdown-only instruction changes, as the brief explicitly
rules; no new tests were authored.

## Final-instruction audit and inspection walkthroughs

These are instruction inspections, not executed agent workflows or real large-project runs.

1. **Resumed distant effects.** Suppose an unfinished plan edit starts near task 40, but task 3
   is its prerequisite, task 7 writes its projected entry, and a distant question is assigned to
   task 40. Plan-project's complete inventory exposes all task dependencies, writers and exact
   questions before choosing resumed work. The third/fourth bullets of Reading the definition and
   plan require complete affected rows/entries/questions and all dependency/meaning-reached units
   before editing. Thus nearby-row selection alone violates the final instructions; a writer
   change still returns to the human under step 4/5. Whole checks run on originals.
2. **New complete breakdown.** Scope, projected headings and every exact question are inventoried
   in original order, with wrapped question items intact. Each scope item is processed at step 2,
   every complete projected entry before step 3 assignment, and every exact question in step 4.
   Batches can load context progressively, but the explicit all-project requirement excludes a
   partial breakdown. Unchanged steps 5-7 retain script coverage, one critique and handover.
3. **Structurally valid semantic failures.** A plan containing a layer-only goal, a moved question
   with no reason, or an inadequate but nonempty quoted answer may pass plan_check: the actual
   implementation documents this boundary and existing test permits moved questions structurally.
   Step 6 requires the independent critic to judge every non-preparatory goal, first use of every
   technical element, every move and quoted answer against needed original source context. Neither
   the author inventory nor a clean script result limits that judgment. Critique completion waits
   for the complete semantic judgment, not the first batch.
4. **Six-reader preservation audit.** Define-project still reads existing definition and supplied
   idea whole, shows changed decisions/invariants/boundaries and searches the whole foundation at
   readiness step 7.2. Technology still reads definition whole. Refine-task preserves independent,
   plan-member and source-only duties and approved-source checks. Implement-task preserves the full
   frozen task, stage order, provisional/human approval distinction, whole projected entry and
   settlement duties, and exactly the original filtered independent assessment package at step 11.
   Plan-task retains full frozen task/spec/source inputs and only changes foundation routing and
   complete-entry range semantics. Plan-project preserves original whole check commands and
   fingerprint/findings routing while applying its new document method.
5. **Complete Read ranges.** Plan-task's Change/Read field rule now requires a range identifying
   an entry to contain all its fields, rationale and rejected options. The existing shared
   receiving-stage check/expansion rule is invoked, so handing a paragraph alone is insufficient.

## Self-review and remaining limitations

Read the real six-file git diff against BASE, checked replacement in place, and compared all
reader clauses to the reviewed spec. No scope expansion, stale opposing whole-read clause in
plan-project, lost source/approval duty or assessment-input leak found. Formatting-only corrections
were made before commit. Names/descriptions/locations remain byte-identical in frontmatter, so no
entry-point regeneration is required. The working tree contained no unrelated tracked changes.
Tracked diff stays in git; no duplicate diff is archived in this report.

The full gate remains unimplemented; passing partial suites is not a full-gate pass. Automatic
actual-read completeness, semantic collision completeness, decisions-found-for-change/1 Method
TODO, and measured real large-project token savings remain unchecked. Common's absent tests and
no-main foundation guard omissions remain the task's previously recorded limitations; this slice
runs no foundation guard because it changes no foundation file. Root owns final required checks,
independent review, return step and integration. No unresolved implementation concern.

Commit: `0c266f3da8cb92204d7788c4bce9065bc2e8b92e` - Apply selective reading to project and task workflows.

Post-commit boundary check: tracked working tree clean; six explicitly staged paths only.
Final control-character and frontmatter byte-comparison checks exit 0. No push performed.
