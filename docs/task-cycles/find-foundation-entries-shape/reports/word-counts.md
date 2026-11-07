# Word counts - find-foundation-entries rebuild

Made by `verify_counts.py --write` from the files at commit e9c900a of the task branch, counted as `wc -w`. Before: the base f447bb6 (the file is identical at dfd50e5). The counts hold only for those files; `verify_counts.py` without an argument checks every number the request states.

| Route and sum | Before (base) | After | Change |
|---|---|---|---|
| Task mode, sum 1: the skill's own text read on the route | 1584 | 1397 | -12% |
| Task mode, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the task template section) | 3741 | 3554 | -5% |
| Task mode, sum 3: sum 2 without what step 1 of `refine-task` read earlier (the whole task template, "How a skill asks", "Reading the foundation") | 2625 | 2438 | -7% |
| Project definition, sum 1: the skill's own text read on the route | 1584 | 1546 | -2% |
| Project definition, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the definition template section, `projected_mode.md`) | 4429 | 4391 | -1% |

Files after the rebuild: `SKILL.md` 598, `read.md` 126, `build_table.md` 198, `definition_variant.md` 624, `task_variant.md` 475; together 2021 words (base `SKILL.md`: 1584).

Files read beside the skill, unchanged: `way_of_working.md` 1752; its sections "How a skill asks" 208 and "Reading the foundation" 503; the task template section "Settlements to record" with its rule 405; the definition template section "Projected foundation changes" 674; `projected_mode.md` 419.

The task document states 424 words for the task template's section "Settlements to record" with its rule. Counted by what an agent reads - the section's own lines 80-87 (60 words) and the rule's bullet under "What each section carries" - the sum is 405. The task's figure equals lines 181-208 of `project-level/task/template.md` (424 words): the rule's bullet, the bullet "Out of scope" and the paragraph below it, without the section's own lines. This report uses 405.
