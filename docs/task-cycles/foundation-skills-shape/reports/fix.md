# Fix of the whole-change review

Status: **done**.

Commit: `4d2f95ee4f9ea2aaddc3a46b64f676960c19238b` (`fix: extract the missing foundation file workflow`), following reviewed head `78e47ee9350fdbfcafd014c3317b1e79cfad9ab3` in the dispatched worktree. Tracked worktree is clean.

## Blocking finding

**R1 — fixed.** The missing-element-file procedure moves verbatim from shared step 1 to `elements/common/missing_element_file.md`. Step 1 now points to it only when the element file is missing and the operation is outside projected mode. The source's start-file question, refusal stop, assignment to a part, direct first-map invocation, map-first ordering and both TODOs remain unchanged. `elements/common/projected_mode.md` is byte-identical to the reviewed head, including its override to ask about no file to start and write no part map first. The three externally referenced common sections are unchanged.

The assessment now separates baseline lines 39–46 (ordinary reading) from lines 47–56 (missing-file procedure), reproduces both complete literal fragments and gives the latter its actual conditional trigger, projected exclusion and move verdict. There are 126 rows covering every nonblank source line. The route report now has 18 routes: four explicit first-element-file routes and the existing first-map route name the additional common read; ordinary and projected routes exclude it. The shared file is now 1675 words; the missing-file companion is 133. Each ordinary/projected entry route drops 107 words relative to the reviewed version; the first-map route adds 26, reflecting its pointer and companion heading. All reported full-file totals were recomputed.

## Files

| Tracked file | Added | Removed |
|---|---:|---:|
| `elements/common/way_of_working.md` | 2 | 10 |
| `elements/common/missing_element_file.md` | 12 | 0 |

Ignored request materials updated under `.runs/task-cycles/foundation-skills-shape/`: `reports/assessment.md`, `reports/word-counts.md`, `assessment_rows.json`, `routes.json`, `relocations.json`, `report_materials.py`, `verify_materials.py`; `fix_r1_materials.py` records the helper update. The original author report and review are historical evidence and remain unchanged. The reviewer's `reviewer_verify.py` remains reviewer-owned; its hardcoded 125-row/14-route/30-file expectations describe the reviewed head and need updating by the reviewer for this fix (current totals: 126 rows, 18 routes, 31 files across the whole change).

## Checks

All commands ran from `C:/Storage/repos/the-way/.runs/worktrees/foundation-skills-shape`.

| Command | Exit | Result |
|---|---:|---|
| `python -B .runs/task-cycles/foundation-skills-shape/fix_r1_materials.py` | 0 | Added missing-file relocation metadata and report explanations. |
| `python -B .runs/task-cycles/foundation-skills-shape/report_materials.py` | 0 | Regenerated 126 assessment rows and 18 route totals. |
| `python -B .runs/task-cycles/foundation-skills-shape/verify_materials.py` | 0 | Literal quotes, complete source coverage, moved/retained text, 23 reachable companions, three unchanged external sections, missing-file trigger, unchanged projected override, 18 inventories and rendered totals pass. |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 errors; unchanged private-backlog `_zadania` path warning and three size information lines. |
| `python -B agent-instructions/skill_entry_points.py` | 0 | Entry points current. |
| `git diff --check` | 0 | No whitespace error. |
| `git diff --cached --check` | 0 | No staged whitespace error. |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors, including the staged new companion's part ownership. |
| `git diff --cached --stat` | 0 | Only the two intended Markdown files, 14 added / 10 removed lines. |
| `git rev-parse HEAD` | 0 | Fix commit confirmed. |
| `git status --short` | 0 | Clean after commit. |

No full gate run: it belongs to the orchestrator. No new invariant or behavioral test: this fix relocates prose without changing its procedure, and measured agent behavior remains outside this task. No test failed. No tracked executable, template, rule or invariant test changed.

## Own-work check and choices

The likely missed requirement was the variant boundary itself: an absent file in projected mode must not cause a new foundation file or part map. I manually followed the ordinary existing-file, missing-file, missing-map and projected paths. The condition in shared step 1 reaches the companion only for the missing-file foundation route; that companion retains the direct first-map branch. A missing map in projected work still follows the unchanged override. The helper additionally checks the literal trigger, absence of the extracted procedure in the common file, exact projected-file bytes and the companion's inclusion only in first-file/first-map count inventories. These checks establish textual preservation and reachability, not measured agent compliance.

I chose to say "Outside projected mode" in the pointer, instead of relying only on the later projected override. Both preserve the current procedure; an implicit exclusion would leave an avoidable premature read on the precise route the finding identifies. I added separate first-file count rows instead of hiding their read cost in a footnote. Counts of a first-file route whose map is also missing explicitly add the first-map invocation with shared files deduplicated; one entry's table is not a count of an unbounded chain of following entries.

The prior blanket assessment of common stages was too broad: it grouped a conditional multi-action procedure with ordinary reading. R1 identifies that boundary correctly. No finding is contested, no scope choice or human settlement is changed, and there are no new selective foundation reaches beyond the dispatch and the author's earlier report. No unresolved problem was observed in this fix.
