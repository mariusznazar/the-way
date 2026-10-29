# One-author report

Status: done with concerns

Commit: `78e47ee9350fdbfcafd014c3317b1e79cfad9ab3` — refactor: split foundation skill guidance by step and mode.
Branch: task/foundation-skills-shape. Base: 745a6e53ec5c8eab3e078a32a61aa6a583a61a93.
Worktree: C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape.

The six skills retain their overview, shared source ownership and numbered routes. Multi-instruction procedural guidance stands beside each skill, and the shared projected mode stands at elements/common/projected_mode.md. The source-finding project-definition path now reads it explicitly. The three external named sections of the common workflow remain unchanged. No tracked Python, template, common-rules or foundation-entry change was made.

## Required request materials

- Assessment: C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape/.runs/task-cycles/foundation-skills-shape/reports/assessment.md — 125 complete source-quoted rows, each with its need, recognisability, verdict, reason and ground.
- Counts: C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape/.runs/task-cycles/foundation-skills-shape/reports/word-counts.md — 14 routes, whole-file reads deduplicated, templates/rules fixed additions and conditional reads explicit.

Normal complete entry routes save 320–425 whitespace words, first map 324, fact withdrawal 320, critic 150. Complete projected routes grow 26–135 and the complete author route 65; those routes need the moved instructions as well as the new pointers/headings. The seven baseline counts exactly match the task; no discrepancy was adjusted away. This is a count of text read, not a claim of improved compliance.

## Files changed

30 Markdown files, +309/-222 lines. The following table is the commit's exact numstat.

| File | Added | Removed |
|---|---:|---:|
| `elements/common/critique/SKILL.md` | 6 | 39 |
| `elements/common/critique/check.md` | 26 | 0 |
| `elements/common/critique/prepare.md` | 12 | 0 |
| `elements/common/critique/settle.md` | 7 | 0 |
| `elements/common/projected_mode.md` | 32 | 0 |
| `elements/common/skill/SKILL.md` | 2 | 0 |
| `elements/common/way_of_working.md` | 2 | 30 |
| `elements/decisions/skill/SKILL.md` | 6 | 24 |
| `elements/decisions/skill/decide_entry.md` | 13 | 0 |
| `elements/decisions/skill/projected.md` | 10 | 0 |
| `elements/decisions/skill/read.md` | 7 | 0 |
| `elements/environment-facts/skill/SKILL.md` | 9 | 40 |
| `elements/environment-facts/skill/decide_entry.md` | 19 | 0 |
| `elements/environment-facts/skill/draft.md` | 8 | 0 |
| `elements/environment-facts/skill/projected.md` | 4 | 0 |
| `elements/environment-facts/skill/read.md` | 6 | 0 |
| `elements/environment-facts/skill/write.md` | 12 | 0 |
| `elements/glossary/skill/SKILL.md` | 8 | 33 |
| `elements/glossary/skill/decide_entry.md` | 17 | 0 |
| `elements/glossary/skill/projected.md` | 7 | 0 |
| `elements/glossary/skill/read.md` | 5 | 0 |
| `elements/glossary/skill/write.md` | 12 | 0 |
| `elements/invariants/skill/SKILL.md` | 7 | 33 |
| `elements/invariants/skill/decide_entry.md` | 21 | 0 |
| `elements/invariants/skill/draft.md` | 8 | 0 |
| `elements/invariants/skill/write.md` | 9 | 0 |
| `elements/part-map/skill/SKILL.md` | 6 | 23 |
| `elements/part-map/skill/decide_entry.md` | 14 | 0 |
| `elements/part-map/skill/first_map.md` | 7 | 0 |
| `elements/part-map/skill/write.md` | 7 | 0 |

## Checks

All commands below ran with explicit working directory C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape.

| Command | Exit | Result |
|---|---:|---|
| `python -B instruction-files/check_instructions.py .` (before and after) | 0 | 0 errors, one unchanged dead-path warning on the prose-relative private backlog `_zadania` directory; three size lines. No new warning. |
| `python -B .runs/task-cycles/foundation-skills-shape/count_probe.py` | 0 | All seven source counts match the task. |
| `python -B .runs/task-cycles/foundation-skills-shape/report_materials.py` | 0 | 125 quoted rows and 14 complete route inventories written. |
| `python -B .runs/task-cycles/foundation-skills-shape/verify_materials.py` (before and after commit) | 0 | All source quotes equal git ranges; every nonblank source line covered once; every moved and retained fragment preserved under the explicit context-pointer rewordings; all 22 companion targets exist and are pointed to; three external section bodies unchanged; route file sets exist and are deduplicated; no Python/template/common-rules changes. |
| `rg -n -F '\s+' elements/glossary/skill/decide_entry.md` | 0 | Literal regex backslash preserved in the moved glossary search instruction. |
| `git diff --check` | 0 | No whitespace error. |
| `git diff --cached --check` | 0 | No staged whitespace error. |
| `python -B elements/common/foundation_check.py` (before staging and after commit) | 0 | 0 errors; the final check includes all new tracked files. |
| `python -B agent-instructions/skill_entry_points.py` | 0 | Entry points current; skill identity/descriptions unchanged, so regeneration writes nothing. |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests passed in 40.316 seconds. |
| `git status --short` | 0 | Empty after commit. |
| `git log -1 --format='%H %ae'` | 0 | Author email is mariusznn@gmail.com. |

No invariant test changed, no new test was written and no invariant-first failing run applies. The full gate was not run by the author, as the handoff and make-change require; it belongs to the orchestrator. No fresh-agent behaviour experiment was run; the task assigns the measured loop2 cycle and post-merge carry-cost measurement outside this change.

An inspection command using Get-Content with several positional file arguments exited 1 (PowerShell parameter binding); the same intended files were then read successfully with `Get-Content -Raw -Encoding UTF8 -Path` and a comma-separated path list. This was an inspection syntax error, not a failed repository check. The first exploratory critique split had incorrect line boundaries; inspection exposed sentence fragments, the boundaries were corrected before any commit, and the exact-source preservation check now passes.

## Own-work check

Weakest requirement: no original rule becomes unreachable or changes meaning, and the request's literal quotes and route totals honestly describe the result. The ignored verification helper compares each report quote with its full original git range and checks exhaustive source coverage, preserves every source fragment either in its original file or in its named destination (with only explicit contextual reference substitutions), verifies direct companion pointers and unchanged external anchors, and validates the route inventories. It passed before and after commit. In addition, I read every companion file and the changed route text, checked the read/decide/draft/write order and reviewed the projected overrides, first-map path and critic/author boundary. Mechanical equality supports preservation, but the independent reviewer still judges semantic routing and the entry-rule distinction.

## Choices and concerns

1. Existing paragraphs prescribing entry form or eligibility stay unchanged in SKILL.md, with proposed template moves in the assessment only. This follows task AC2 and its explicit exclusion of templates, using WAY-256's unchanged-fragment exception. The orchestrator agreed this is the scope-preserving implementation choice, subject to independent review. Moving those rules into companions would violate AC2; editing their templates now would widen the task. Cost: those paragraphs still load for every invocation, and the assessment cannot complete that future cleanup. No human settlement was changed.
2. The projected invariant and part-map routes have no element-specific companion because their form/eligibility paragraphs remain and the remaining procedural handoff/exclusion is one instruction. They both explicitly read the common projected mode. The withdrawal paragraph also stays as one instruction; a pointer would add a file without reducing instructions in play. The alternative is a pointless file, or a template change outside scope.
3. Common normal steps and externally named sections stay in way_of_working.md; only its projected-mode procedure moves. Splitting ordinary shared stages too was rejected because To do 2 targets modes/variants and the protected shared-reader routes must remain stable. Cost: normal complete entry routes still read the 1782-word shared file.
4. Critic no-write guidance is visible in SKILL.md, while author-only preparation and settlement move separately and the independent checks are shared. Moving the boundary only with settlement would hide it from the critic.
5. The source-finding skill gains only the project-definition pointer to the extracted common mode. Its task-refinement route does not project entries and does not need that mode; its existing common read stays. No new blanket reading rule is introduced.
6. Counts report full completion, not only smaller SKILL.md files. The projected and full-author routes grow slightly; a smaller headline number would conceal that cost. Source examples and product-specific foundation/source documents remain required but are outside the task's specified file count and are not estimated.

## Foundation step and reaches

The frozen task has zero accepted settlements, no projected entry to write and no foundation revision. The foundation step therefore writes none. The changed files remain within existing parts' directory patterns; no new part, dependency, trust boundary or surface is introduced. The author compared the change with the selected entries and found no entry requiring correction. The orchestrator still owns the cycle's return step.

Additional selective reach: WAY-128, WAY-129, WAY-130, WAY-131, WAY-132 and WAY-133 in foundations/decisions.md, read whole because maintain-instruction-files requires the instruction-file decisions and cites their pointer, evidence and rule-entry criteria. Linked facts instruction-density-accuracy, single-rule-compliance and claude-skill-nested-references were read to understand the adopted structure and its evidential limits. The seven targets, all five element templates, common/rules.md, common/skill/SKILL.md and incoming named-section references were read to preserve existing access and distinguish entry rules from procedure. Global/repository skill and script conventions were read as required. User loading settings were searched only for the named loading keys, not printed whole. No secret was copied.

No question for the human, no missing permission and no further implementation work is outstanding. Remaining concerns are the unchanged entry-form paragraphs and the absence of behavioural measurement, both explicit above. No push or request creation was performed.
