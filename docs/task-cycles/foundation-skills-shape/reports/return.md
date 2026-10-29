# Return step

Status: **done**. No foundation correction or other tracked change is needed. No new commit.

Compared head: `4d2f95ee4f9ea2aaddc3a46b64f676960c19238b`; tree: `5995f140ea34985343988002d2e27576950c3868`. Both match the reviewed and gated tree named by the dispatch. The worktree is clean. This report is the return-step record for the orchestrator's cycle archive; it is not itself tracked until that archive is committed.

## Foundation compared with the final files

The author resumed with the original selected entries and earlier full readings. At this step I reread the full task-named decisions WAY-35, WAY-117, WAY-120, WAY-125, WAY-127, WAY-150, WAY-256, WAY-257 and WAY-259, the part map, glossary and invariants, and compared their requirements with the final routing, the preserved-source assessment, the complete change inventory and the fix review. No foundation entry was written or changed by this task. No foundation-writing search had been triggered, so there are no additional entries from such a search to reconcile. This is a comparison of affected rules, not a new search of every Scope.

| Entry or rule | Actual comparison | Result |
|---|---|---|
| WAY-35; skill-rule-source | Each of the five entry skills still names its template and common rules as the entry-rule sources and the common workflow as the shared procedure. Element companions carry procedural reading, deciding, drafting, writing or projected actions. Existing entry-form prescriptions were kept unchanged rather than moved into companions; the assessment distinguishes those unchanged fragments from the unapplied template proposal. Templates and common rules have no diff. | No correction. |
| WAY-256 | Each of the 23 companions has a named step or variant pointer. Shared projected and missing-file procedures remain in elements-common. Single instructions remain inline; invariant/part-map projected routes need no element-specific projected companion. R1 moved the previously missed multi-action missing-file variant and explicitly excluded projected work. | No correction. |
| WAY-257 | Each of 126 source-fragment rows provides when the text is needed, whether that moment is recognisable and a verdict. R1 split the ordinary-reading and missing-file conditions into separate rows. | No correction. |
| WAY-150 | The full body and heading of Reading the foundation are unchanged. Shared step 1 still requires whole templates, rules and examples. Moving variant procedures does not change selective reading or the whole-foundation search at step 2. | No correction. |
| WAY-117 | Every entry skill reaches common/projected_mode.md directly. Its proposal location, no-foundation-write rule, no foundation check, no per-entry whole-foundation search, identifiers and treatment of following entries remain. The project-definition route in find-foundation-entries explicitly reads the moved mode. | No correction. |
| WAY-120 | Critique retains the optional invitation, mandatory collective-review trigger, one full set and exclusion of foundation/invariant-test diffs. prepare.md holds the fresh-agent handoff; check.md holds the full checks; settle.md leaves the explicit verdict with the author. The critic's no-write boundary stays visible in SKILL.md. | No correction. |
| WAY-125, WAY-127, WAY-259; skill-entry-points | No task-cycle method, installed entry-point mechanism or generated project entry point changed. Skill identities, locations and descriptions are unchanged. Pointers name their own step or mode and remain usable when a skill is read directly by path. No new global reading rule was added. | No correction. |
| WAY-28 and WAY-44, as carried by the original reading | The missing-file companion preserves the first-map ordering, same-invocation first map and assignment of a new foundation file to a part. first_map.md retains iteration until coverage is complete. The change adds no new cross-part dependency. | No correction. |

All other selected entry-form and procedural decisions retain the same implementation text, either in their existing file or in the reached companion. The literal-preservation and route checks recorded in fix.md and the independent fix review support this comparison; they do not establish measured agent compliance. No test, executable rule, field form or source value changes.

## Touched part map

| Part | Final files and responsibility compared | Result |
|---|---|---|
| decisions | elements/decisions/** continues to own the skill and its read, decide_entry and projected companions; dependency on elements-common unchanged. | Existing entry matches. |
| invariants | elements/invariants/** owns the skill and decide_entry, draft and write companions; decisions, part-map, environment-facts and elements-common dependencies unchanged. | Existing entry matches. |
| glossary | elements/glossary/** owns the skill and read, decide_entry, write and projected companions; listed foundation dependencies unchanged. | Existing entry matches. |
| environment-facts | elements/environment-facts/** owns the skill and read, decide_entry, draft, write and projected companions; listed foundation dependencies unchanged. | Existing entry matches. |
| part-map | elements/part-map/** owns the skill and decide_entry, write and first_map companions; elements-common/invariants dependencies unchanged. | Existing entry matches. |
| elements-common | elements/common/** owns the shared workflow, projected_mode.md, missing_element_file.md, source-finding pointer and critique files. Shared workflow, source finding and critique remain its declared responsibilities. | Existing entry matches. |

All six entries still correctly declare no trust boundary. No surface or external-context relationship is added, removed or changed. The previously run foundation check includes the new files and reports 0 errors.

## Other invariant and entry obligations

- foundation-file-kinds, repository-file-location and element-directory-contents: no foundation file is added; all new tracked files are Markdown companions within the existing process directories. Templates, examples and SKILL.md remain in place.
- derived-file-content and generated-overview: no generator or derived content changed; existing entry-point verification and the supplied gate pass. No directory overview was added.
- ci-checking-commands, script-language, script-imports and script-subprocesses: no tracked script or CI configuration changes.
- outbound-link-reach and instruction-file-imports: the tracked additions use existing repository paths or skill names, with no new private/external link or tool import. Private task provenance and reports remain in the ignored run until the orchestrator's archive procedure.
- map-reference-target: no foundation reference is added or changed; the foundation check and supplied gate pass.
- foundation-change-merge-route: no foundation entry changed; integration still belongs to the human through the request into foundations.
- return-step-record: this completed comparison is available for the cycle's required archive commit before publication. That archive is the orchestrator's next operation, not a missing foundation entry.

The task has zero accepted Settlements to record, no projected foundation entry assigned to it, and no spec or plan carrying entries. The work adds no external factual dependency: the existing instruction-density and single-rule evidence continues to support WAY-256 with its stated limits, and no compliance improvement is claimed. It introduces no product term or changed glossary meaning. No new invariant is warranted: the split implements WAY-256 and the task's structural requirements; it does not establish an independent product rule or justify recording behavior merely because it exists. Reversible filenames and grouping choices are implementation choices, not new decisions that bind later work. No entry is deferred or proposed for later by this return step.

## Checks and evidence

All commands below ran in `C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape`.

| Command | Exit | Result |
|---|---:|---|
| `git diff --name-status 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..HEAD` | 0 | 31 Markdown files, all within the six mapped element directories. |
| Decision locator, exact command below | 0 | Located all nine task-named decisions; each full entry then reread, not substituted by its search hit. |
| Source/pointer locator, exact command below | 0 | Confirmed source ownership and the final explicit reading routes. |
| `git rev-parse HEAD 'HEAD^{tree}'` | 0 | Head and tree match dispatch. |
| `git diff --exit-code 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..HEAD -- foundations elements/common/rules.md elements/decisions/template.md elements/invariants/template.md elements/glossary/template.md elements/environment-facts/template.md elements/part-map/template.md .agents .claude installation task-cycle` | 0 | No changes to foundation entries, excluded templates/rules, entry points, installation or task-cycle methods. |
| `git status --short` | 0 | Clean tracked worktree. |

Locator commands:

```powershell
rg -n '^#+ .*WAY-(35|117|120|125|127|150|256|257|259)\b' foundations/decisions.md
rg -n 'template.md|common/|projected_mode.md|missing_element_file.md|prepare.md|check.md|settle.md' elements/decisions/skill/SKILL.md elements/invariants/skill/SKILL.md elements/glossary/skill/SKILL.md elements/environment-facts/skill/SKILL.md elements/part-map/skill/SKILL.md elements/common/critique/SKILL.md elements/common/skill/SKILL.md elements/common/way_of_working.md
```

The dispatch supplies `python -B gate/run_tests.py`: exit 0, 613 tests in eight directories, five Windows skips, on the same tree. This return step did not rerun the gate or focused tests because it makes no tracked change; their author/reviewer command evidence remains in the existing reports. No check in this step failed. No invariant test changed.

No new reach beyond the dispatch. No question, correction or unresolved finding remains from the comparison. The earlier review's sole blocker was fixed and independently reviewed PASS on the compared head.
