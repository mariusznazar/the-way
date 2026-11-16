# Author report — correction 2

**Status:** done. **Commit:** `763a420e` (2 files, 9 added, 7 removed). The return step is not taken.

## The remark and how it was met

The human's decision (word for word): "Add to the sentence in `project-level/task/skill/find_settlements.md:29-30` the condition its twin in `task_variant.md` has: a row adopting an outside practice enters the table as the human's choice only when it repeats a choice the human made between the ways shown; a row the agent derived itself waits for the human. Check that every other place that states this rule carries the same condition."

- `project-level/task/skill/find_settlements.md`: the sentence now reads "A row that adopts a practice from outside the product (WAY-100) and repeats a choice the human made between ways shown enters `accepted` as the human's choice, like any such row, and carries among the ways its source keeps the parts of the practice the human turned down; where its source keeps none, a question shows the parts as ways before the table closes, and the parts the human turns down go into the row's *Source* (WAY-134). A row of such a practice that you derived from the material or from the human's loose words waits for the human, as every row you derived does." The last sentence is the second half of the decision, in the words the file already uses for every derived row.
- `project-level/task/template.md` (*Settlements to record*, *Source*): "A row that adopts a practice from outside the product" now reads "… and repeats a choice the human made among ways shown", before "names among those ways each part …". The sentence named the ways of such a row without saying whose choice; the condition is the same.
- No other place needed a change (below). WAY-409, WAY-410 and the wording of Minor finding 2 are untouched.

## Places searched (the whole repository, `project-level/`, `elements/`, `task-cycle/`, `product-guidelines/`, `foundations/`) and what I did

Search: `practice from outside`, `outside practice`, `from outside the product` in every `.md` and `.py`, outside `.runs/` and `docs/`; and the words `waiting`/`waits`/`accepted`/`built` in the four files of the step.
- `elements/common/skill/task_variant.md:33` — already carries the condition ("and repeats a choice the human made between ways shown is built `accepted`"); its *State* bullet says proposed rows start `waiting`; left.
- `project-level/task/skill/find_settlements.md:29` — changed (above).
- `project-level/task/template.md:149` (*Questions to settle*: a question that settles the adoption shows the parts among its ways) — names no state, speaks of the question that settles; left. `:223` (*Source*) — changed (above).
- `elements/common/skill/build_table.md` — states "a candidate from the material is a proposal" and the accepted rule for a repeated choice, with no sentence on an outside practice; left.
- `elements/decisions/template.md:94` — "Where the row adopts a practice from outside the product, the parts … are among the ways the row's source keeps when the human weighed them": names the source's ways, no state; left.
- WAY-134 (`foundations/decisions.md:5304` binding sentence, `:5327` pair, `:5347`) and WAY-100's third paragraph: they tie the showing of the parts to "the question that settles it" / "the row's source" and name no state; the rules on state in WAY-134's first paragraph, *complies* and *violates* stand. Left.
- `elements/part-map/*`, `foundations/decisions.md:2565, 8808`: "from outside the product" in other senses (files, a practice a product takes); left.
- `foundation_step.md`, `way_of_working.md`: name no state of such a row; left.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` — exit 0.
- `python -B gate/run_tests.py project-level` — exit 0 (279 tests); the only directory with a changed file (`elements/common` was not changed this time). Not run: the full gate.

## Own-work check (WAY-164)

- Requirement most likely not met: no copy of the rule lacks the condition, in whatever words it is restated.
- Check: `reports/author-correction2-check.py FILE...`, which works by sentence, not by word list: each sentence that names a row (or candidate) adopting an outside practice together with the state it is built in (`accepted`, `waiting`, waits, built, enters) must also carry the condition (repeats a choice made between ways shown) or be about a row the agent derived.
- What it showed: on the changed files (`find_settlements.md`, `task_variant.md`, `build_table.md`, the task template, the decisions template, the decision log) 0 sentences without the condition, exit 0; on `find_settlements.md` of `637d7787` it fails (the sentence "carries among the ways its source keeps … waits" is without it) and on that of `938d6ee9` it fails (the sentence this correction fixes), exit 1 each. Limits: it reads sentences by pattern and judges nothing on meaning beyond the condition; a rule restated in other words, or across two sentences, would pass it, which is why I also searched by hand (above).

## Reaches beyond the handoff

`project-level/task/template.md` (the *Source* sentence) was changed on the decision's words "every other place that states this rule"; the handoff named `find_settlements.md` only. I read `review-correction-fix-report.md` section "What the fix itself broke" only.

## Unread material

The rest of `reports/review-correction-fix-report.md` (not mine). Nothing else of the handoff stayed unread.

## Searches not found or unclear

- None found missing. One unclear point I did not decide: whether a row a refiner derives that adopts an outside practice must also get the question that shows the left-out parts; the reviewer declined to judge it and neither the decision nor WAY-134's second paragraph reaches it, so I left it; a derived row waits for the human, who sees it in the table.

## Working copies

`.runs/author-correction2/` held two copies of `find_settlements.md` (of `637d7787` and of `938d6ee9`), the check and the output of the test run; removed. Kept in `reports/`: `author-correction2-check.py`. No worktree or clone was made.
