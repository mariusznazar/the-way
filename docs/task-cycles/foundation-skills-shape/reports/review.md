FAIL 78e47ee9350fdbfcafd014c3317b1e79cfad9ab3

# Whole-change review

Reviewed range: 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..78e47ee9350fdbfcafd014c3317b1e79cfad9ab3. HEAD matches the dispatched head. One author, no spec or plan, no prior slice review. The frozen task and both required request materials were reviewed. Guidelines selection is empty under the task's settled question 5.

## Blocking findings

### R1. Extract the missing-element-file variant from the shared reading step

**Grade:** Important. **Scope:** within the task, To do 2 and its assessment requirement. **Thread:** new. **Slice:** none; one-author change.

**Anchor:** `elements/common/way_of_working.md:47`; related assessment: `.runs/task-cycles/foundation-skills-shape/reports/assessment.md:160`.

**Do wklejenia:** The shared Read step still carries the complete procedure for a product that has no file for the element, although that procedure is needed only in that variant. The assessment combines it with ordinary reading and keeps the whole group, so To do 2's required variant split is incomplete. Move this procedure unchanged to a common companion, leave a conditional pointer at step 1, and update the assessment and route counts.

**Dlaczego to zgłaszam:** The task extends the split to fragments of `way_of_working.md` needed only in one mode or variant, naming Projected mode as the principal example rather than the entire scope. Its exception protects sections named by external readers; it does not protect every part of the ordinary shared stages. The remaining fragment is:

```text
- Where the product has no file of the element's entries, ask whether it starts that file here; if
  not, stop
  (`TODO — decision pending: which decision sets that a product starts an element's file only on
  the human's word`). If so, the same change gives the new file to a part of the map through
  `update-part-map` (WAY-44). Where the missing file is the part map itself, the current
  `update-part-map` invocation writes the first map directly, using its "The first map of a
  product" section. Where another element's file is missing and the product has no part map,
  `update-part-map` writes the map first (WAY-28, for a product the process enters;
  `TODO — decision pending: which decision sets that the part map is written before another
  element's first file`).
```

This contains several actions: obtain the start-file choice, stop on refusal, assign a new file to the map, avoid a recursive first-map invocation, and create the missing map before another element's first file. It therefore does not qualify for the one-instruction exception. For example, updating an existing decision log with an existing part map reads this entire procedure through the mandatory whole reading of the shared file, though none of these actions can apply. The projected route also carries it despite its explicit override not to start foundation files or write a map first. This is exactly the unnecessary variant reading To do 2 asks this change to remove; no numerical size threshold or claim about measured compliance is needed to establish the missed requirement.

The assessment's row for baseline lines 39–56 calls the whole group needed "At 1. Read" and keeps it because "Scope permits mode/variant extraction, not a new split of the common stages." That reasoning overlooks the distinct missing-file condition inside the group. The full caller search finds external references to the three named shared sections, and the source-finding skill's whole-file read; no external named-section reference protects this paragraph. A conditional pointer preserves those routes without splitting ordinary shared steps. Keep all existing TODOs and choices unchanged in the companion, and preserve the projected override. Recalculate the required counts; routes entering the missing-file variant should name its additional read explicitly. This correction needs neither a template change nor a new foundation decision.

The author's own-work verification checks that retained text is still present, not whether the assessment correctly identifies its trigger; therefore its successful run cannot catch this gap.

## Minor findings

None.

## Out-of-scope findings

None.

## Declined to judge

- Post-merge carry-cost measurement and the measured loop2 cycle: the frozen task explicitly places them outside this implementation.
- Removing or relocating unchanged entry-form duplication through template changes: templates and common rules are excluded by the task. The assessment exposes this as an unapplied proposal; this review does not require that broader cleanup.

## Other conclusions

The moved text is preserved with contextual path substitutions. Every added companion is reached by a step or mode named in its owner; the five entry skills remain usable when read directly by path. The first-map heading remains reachable from the common missing-map branch. Projected work explicitly reaches the common mode from each entry skill and from the source-finding project-definition route. The protected How a skill asks, Reading the foundation and Critique before collective review sections retain their exact bodies and headings. Critic and author reading are separated while the critic's no-write boundary remains visible.

I find no additional AC2 violation in the moved material: the drafting/search actions direct the agent to existing template rules rather than establish new field forms in the companions. Keeping the unchanged field prescriptions in SKILL.md, with the template cleanup only proposed, is a reasonable scope-preserving choice given the explicit template exclusion. This does not exempt the separately identifiable procedural variant in R1. The new companion files contain multiple actions; the retained withdrawal and following-entry instructions fit the one-instruction exception.

All 125 quoted fragments and their baseline line anchors were independently compared against the literal git blobs, covering every nonblank line of all seven evaluated files once. All 14 reported route totals were independently recomputed from their full file inventories, each file once, with the five unchanged template/common-rule additions checked separately. Counts match the current implementation; they will need updating for R1. No Python, template, common-rule or foundation entry changes occur, and no invariant test is altered. The existing part-map directory patterns own the added files without a new dependency, surface or trust boundary.

## Checks

Commands ran in `C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape`.

| Check | Exit | Result |
|---|---:|---|
| `git rev-parse HEAD` | 0 | Dispatched head confirmed. |
| `git log --oneline 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..78e47ee9350fdbfcafd014c3317b1e79cfad9ab3` | 0 | One implementation commit. |
| `git diff 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..78e47ee9350fdbfcafd014c3317b1e79cfad9ab3` | 0 | Whole range inspected, with truncated sections reopened separately. |
| `python -B .runs/task-cycles/foundation-skills-shape/reviewer_verify.py` | 0 | Independent parsing of final assessment Markdown and final counts: 125 literal quotes/anchors, seven-file nonblank coverage, 14 deduplicated route totals, five fixed additions, three unchanged external sections, permitted changed-file set. |
| `python -B .runs/task-cycles/foundation-skills-shape/verify_materials.py` | 0 | Author's helper inspected, then rerun: moved/retained text preservation and 22 companion pointers pass, with its explicit contextual substitutions. |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 errors; one unchanged `_zadania` dead-path warning from the private backlog pointer; three size info lines. |
| `python -B agent-instructions/skill_entry_points.py` | 0 | Entry points current. |
| `git diff --check 745a6e53ec5c8eab3e078a32a61aa6a583a61a93..78e47ee9350fdbfcafd014c3317b1e79cfad9ab3` | 0 | No whitespace error. |
| `git status --short` | 0 | Tracked worktree clean. |

Manual route check: searched incoming references with `rg -n 'way_of_working\.md|common/critique/SKILL\.md' elements project-level product-guidelines task-cycle installation`, exit 0, then read the relevant calls and followed each new pointer. Manual classification of the seven assessed files and companions against the whole task and WAY-35/WAY-256 identifies R1. No executable focused test can decide whether this procedural fragment has the correct trigger; the manual comparison is the discriminating check.

Not run: full `python -B gate/run_tests.py`, assigned to the orchestrator by the handoff and review method; fresh-agent behavioral measurements, assigned outside this change. No claim of improved compliance is made. Initial inspection encountered a wrong guessed path `instruction-files/skill/SKILL.md` (exit 1); file inventory located and the review read `instruction-files/SKILL.md`. An initial scratch selector split the log at the wrong heading level; its one-entry result failed the positive control and was discarded before relying on the selection. Neither was a product-check failure.

## Selective reaches

- `instruction-files/SKILL.md`, `instruction-files/judging.md`, `instruction-files/kind_skill.md`: criteria for the required assessment, particularly variant triggers and the single-instruction exception.
- WAY-128–WAY-133, WAY-257 and WAY-259 in `foundations/decisions.md`, each whole: instruction-placement and assessment rules beyond the touched-part selection and details named by the task/author report.
- `instruction-density-accuracy`, `single-rule-compliance` and `claude-skill-nested-references` in `foundations/environment_facts.md`, each whole: evidential limits of the split and direct reading pointers.
- All five element templates and `elements/common/rules.md`, whole: distinguish entry rules from procedural instructions and validate fixed count supplements.
- Incoming shared-workflow and critique calls in `project-level/`, `product-guidelines/`, `task-cycle/` and `elements/common/skill/SKILL.md`: check the preserved direct-path and whole-shared-file reading routes.
- The author's ignored verification helper and the final request materials: compare its own-work-check claims with what the code actually asserts, then independently verify the final rendered table inputs.
