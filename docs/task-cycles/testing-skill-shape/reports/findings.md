# Blocking findings of the review of the whole change

Copied word for word from `reports/review.md`, the review of 00c0a74..5dc4b3b, first line `FAIL 5dc4b3b06a2fc809120d39a64e185be168afd5cc`. Paths are relative to the worktree.

## Important

### 1. The word counts in the request are stale: every "after" figure is 10 words low

**Anchor:** `.runs/task-cycles/testing-skill-shape/reports/word-counts.md:62` (and the same line in every route; the Summary at `:19-24`)

**To paste:** `recognize.md` is counted as 412 words on all six routes; `wc -w` gives 422 at the head. Every "after" figure and most percentages in `word-counts.md` are wrong; regenerate the file from the head.

**Why:** To do 7 makes these figures the main measure the request carries, counted as `wc -w` counts them. `word-counts.md` was written at 01:19; `recognize.md` was last changed at 01:20:46, before commit `d024d56`, and has 422 words in both `d024d56` and `5dc4b3b`. `author.md` itself gives 422 in its table of files and 412-based sums in its table of routes. `tools/verify_reports.py` compares the sums with the file's own lines, so it passed a list that no longer matches the tree. The "before" figures, the sections (208, 492, 54) and every other file are right. Recomputed from the files of the lists:

| Route | Reported after: to step 4 / total / change | Recomputed | Without the first reading, reported / recomputed |
|---|---|---|---|
| 1 | 8801 / 11246 / -20.4% | 8811 / 11256 / -20.3% | 5966, 8411 / 5976, 8421 |
| 2 | 7738 / 11014 / -22.0% | 7748 / 11024 / -21.9% | 4903, 8179 / 4913, 8189 |
| 3 | 9031 / 11476 / -18.7% | 9041 / 11486 / -18.7% | 6196, 8641 / 6206, 8651 |
| 4 | 7968 / 11244 / -20.4% | 7978 / 11254 / -20.3% | 5133, 8409 / 5143, 8419 |
| 5 | 7693 / 10969 / -22.3% | 7703 / 10979 / -22.2% | 4858, 8134 / 4868, 8144 |
| 6 | 8899 / 11344 / -19.7% | 8909 / 11354 / -19.6% | 6064, 8509 / 6074, 8519 |

The difference is small, but the request presents these as counted numbers, and the series uses them as its measure until the first real use (Question 7). Fix: run `tools/word_counts.py` against the head, carry the figures into `author.md`, and make the helper's check compare each listed count with the file.

### 2. A mode nobody asked for: "tests at a level its cycle chooses" is true of every task, and it says "no step 2"

**Anchor:** `product-guidelines/testing/recognize.md:21-24`, `product-guidelines/testing/SKILL.md:94-97`, `.runs/task-cycles/testing-skill-shape/reports/assessment.md:60`

**To paste:** The clause "or whose tests are at a level its cycle chooses" adds a mode the base and To do 3 do not have. Taken literally it holds on every route, so an audit agent reads `new_level.md` with no new level, and "no step 2" collides with the other modes; taken narrowly, the audit routes no longer reach the rule. Keep only the mode To do 3 gives.

**Why:** The base mode (`:120`) was "a task whose required outcome is the first test of a level". To do 3 and `product-guidelines/reading.md:77-78` let the case skip step 2 only where the outcome is that test and the recipe stands with an empty *Exemplar*. The author widened the mode to reach the sentence of `new_level.md:6-8`; the assessment calls this "REWORD (meaning-preserving)". It is not:

- By WAY-238 the author of a change chooses the level of every test that is not the required outcome. Every task of testing guidelines carries "write the test of each new invariant" (`task_document.md:6`), so "its tests are at a level its cycle chooses" holds on routes 1 to 4 and 6.
- On routes 3 and 4 the condition at `SKILL.md:95` therefore sends the audit agent to `new_level.md` with no new level. Acceptance criterion 5 forbids that.
- `recognize.md:17` says modes combine. Example: an extension task with an invariant test takes "existing testing guidelines, refreshed or extended: step 2" and also "the new-level case of step 3, and no step 2". An agent that follows the second skips the research WAY-249 requires at every extension.
- The narrow reading, under which the author's walk passes, is no way out: then the sentence "the refinement designates no exemplar test" is not reached on routes 3 and 4, where the base had it inside step 3, and acceptance criterion 1 fails.
- `refine-task` sends such a task nowhere near this skill (`project-level/task/skill/guideline_findings.md:39-42`: "add no designation").

By the orchestrator's rule, a reword that changes a rule's meaning stands as a proposal and is not applied. Fix: `recognize.md` keeps only the case with the recipe standing and the extension clause; `SKILL.md:95` loses "or its tests are at a level its cycle chooses"; the sentence on the cycle's choice moves, unchanged, to where every route settles exemplars, the exemplar item of `settle.md:15-16`, which is a move the task accepts. Row 120 of the assessment and its "Text added" row change with it.

### 3. "Extend what exists" stands in the file of the first step, which is the violating example the change itself wrote

**Anchor:** `product-guidelines/testing/recognize.md:27-29`, `.runs/task-cycles/testing-skill-shape/reports/assessment.md:62`, `foundations/decisions.md:7280-7284`

**To paste:** The assessment's own row says this rule holds at steps 1, 2 and 4 and then places it in the file of step 1. WAY-256 now keeps such a rule of working in `SKILL.md`, and names this very layout as violating. Move the three lines to "Rules that hold across the steps".

**Why:** The row reads: "A rule that holds on three steps, placed in the file of the first". The new sentence of WAY-256 says "a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`", the third answer of `kind_skill.md:15-16` says the same, and the entry's *Verification* lists as violating "a rule of working that three steps keep stands only in the file of the first". WAY-263 makes this Important: the change's files do what an entry it writes forbids.

The rule binds at step 2, where a human's preference and the research could propose a second tool, and at step 4, where recipes are settled (WAY-248: "it extends what exists rather than setting a second tool beside it"). The row's defence does not hold: `starting_set.md` says only that a preferred tool is the one proposed, and `settle.md` says nothing of recipes staying with the tool the product runs. Its other defence, that a file read earlier stays in context, would equally have let "How to show" stand in `starting_set.md`; the author moved "How to show" to `SKILL.md` on exactly this ground (Choice 2). WAY-256's *Rationale* leaves the boundary between a rule and text to consult to the row, but this row calls it a rule.

Fix: the bullet moves to "Rules that hold across the steps" in `SKILL.md`, verdict KEEP. It costs about 52 words in `SKILL.md`, so the counts of finding 1 change with it.

### 4. WAY-256 now has four binding sentences; WAY-05 allows three

**Anchor:** `foundations/decisions.md:7271-7284`

**To paste:** The binding paragraph of WAY-256 has four sentences, against "one to three binding sentences" of WAY-05 and the template. Merge the new sentence or the closing one so the paragraph has three.

**Why:** WAY-05 (Scope `decisions`, a part this change touches) and `elements/decisions/template.md:25` and `:90` limit binding sentences to three. The base had three. The change adds "A fragment that some steps of the skill need..." and keeps "Fragments that stand unchanged are not bound by it." as a fourth. `author-repair.md` (Choices, 1) cites the limit and calls the new sentence "the third", which miscounts. `foundation_check.py` does not count sentences, so its exit 0 says nothing here. My count over the log finds 221 of 224 entries within the limit at the head; the other two above it, WAY-80 and WAY-229, stand on the base and are outside this task. Fix: join the last two sentences with a semicolon, as "...unless an earlier step did; fragments that stand unchanged are not bound by it." WAY-134 leaves the wording to the cycle, so the row's meaning stays.

### 5. WAY-265's exemption does not cover the skill it was written for

**Anchor:** `foundations/decisions.md:7579-7581`, `product-guidelines/styleguide/SKILL.md:69-70`, `:78-79`, `:89-90`

**To paste:** Row 2 exempts unchanged files "as in the styleguide skill"; the entry exempts only "Skills whose files stand unchanged". This same request changes `styleguide/SKILL.md`, so the styleguide skill breaches WAY-265 on the day of the merge. Word the exemption by file, as the row does.

**Why:** Row 2 of *Settlements to record* reads "pliki stojące bez zmian, jak w skillu styleguide'u, reguła omija", and Question 3 keeps that skill in two levels "until someone takes up that remark". The styleguide skill was rebuilt according to WAY-256 (commit `802b56d`), so the entry's first clause reaches it. Its step files point to variant files its `SKILL.md` does not name: `starting_rules.md:10` to `research.md`, `settle.md:4` to `new_tools.md`, `settle.md:38` to `staged_cleaning.md`. To do 6 changes `styleguide/SKILL.md` in this request, so "Skills whose files stand unchanged" no longer describes it. A reviewer of a later change, or of task 8, who reads the entry as written finds a breach the human ruled out. WAY-263 grades a restatement without its qualification Important. Fix: something like "A step's file that stands unchanged, with the variant file it points to, is not bound by it", and the last clause of *Rationale* at `:7597-7598` to match.
