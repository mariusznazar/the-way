FAIL 5dc4b3b06a2fc809120d39a64e185be168afd5cc

# Review of the whole change — maintain-testing-guidelines in the WAY-256 shape

Range `00c0a747272a9a179b7a855f256daff985ea2ee1..5dc4b3b`, three commits, no plan, no slices. `git rev-parse HEAD` is the head given. Paths are relative to the worktree `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape`. Each blocking finding comes from no slice: one author, no plan.

Counts: 5 blocking (all Important), 5 Minor, 0 out of scope. **Declined to judge** holds 6 lines.

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

## Minor

### 6. The pointer of step 2 leaves out the first case, "before the first test"

**Anchor:** `product-guidelines/testing/SKILL.md:86`

**To paste:** The pointer names "tests with no testing guidelines yet" and "a refresh or an extension", but not a product with no tests, which is routes 1, 2 and 6. Add "before the first test" as line 133 of the base has it.

**Why:** Acceptance criterion 2 wants each pointer to name its moment. The agent still arrives, since `recognize.md:18` sends it to step 2 and the clause opens with "which step 1 gives", so the walk does not break and I do not block on it. But the base's three cases became two, and a reader of `SKILL.md` alone cannot tell that the first route takes this step. The author named this pointer as a concern for its length, not for this.

### 7. Route 5 no longer reaches the rule on choices found in tests

**Anchor:** `product-guidelines/testing/audit.md:17-20`

**To paste:** "A choice found in the product's tests is a proposal, never a rule" is not read on the new-level route with a product that has tests, where the base had it in step 3. Consider `settle.md`, which every route reads.

**Why:** Step 1 on route 5 finds the tool's configuration and habits, and the rule (WAY-29) says what becomes of them. The cost is low, because the recipe already stands on that route and little is settled from the tests. Acceptance criterion 5 keeps the agent out of `audit.md`, so the sentence would have to move, not the route.

### 8. "must" in the prose of two entries

**Anchor:** `foundations/decisions.md:7330`, `:7597`

**To paste:** The new *Rationale* of WAY-256 and that of WAY-265 use "must"; the template keeps normative words to binding sentences.

**Why:** `elements/decisions/template.md:92`. Seven other entries do the same, so this is polish.

### 9. Two meanings beyond the rows: name them in the request

**Anchor:** `foundations/decisions.md:7580-7581`, `:7608-7609`

**To paste:** "with the condition under which it is read" in WAY-265 and the last sentence of WAY-266 are not in rows 2 and 3. Name both in the request so the human reads them as additions.

**Why:** WAY-30's *Verification* counts extending a settlement's meaning without asking as a violation. Both additions have ground: WAY-129 asks a pointer for its condition, and Question 4 says task 8 repeats the sentence for the coding skill. `author.md` discloses the second (Choice 8), not the first. Neither changes what a route does, so the request naming them is enough.

### 10. Small errors in the materials

**Anchor:** `.runs/task-cycles/testing-skill-shape/reports/assessment.md:41`, `:53`, `:74`

**To paste:** Row 187-194 says the step 4 pointer names "How to show" through `settle.md`; neither does. Row 18-22 says its added sentence is listed under "Text added"; it is not, nor is the clause added to the orchestrated pointer.

**Why:** The human reads these rows as the record of what changed. `grep "How to show"` over the skill finds only `SKILL.md:52` and `starting_set.md:8`; "How to show" reaches step 4 because `SKILL.md` is read whole, so the row's conclusion stands and its reason does not. Also: the assessment's sections stand in the order check, contradictions, table, where `instruction-files/judging.md:13-26` gives check, table, contradictions, and SPLIT and CHOICE are not among its four verdicts; `author.md` says "235 nonblank lines", while the base has 227 nonblank lines and the ranges also hold 8 blank ones.

## Declined to judge

- `new_tools.md` left out of the routes' sums although the mutation-tool item of `settle.md:23-25` may reach it: `word-counts.md:11` discloses it, and the task gives no rule for conditional files.
- `refine-task`'s other files (`read_sources.md`, `draft.md`, its `orchestrated_mode.md` on route 6) left out of the counts although a counted file sends the session to them: the task fixes the first reading at 2835 words, and they are the same in both states.
- "unless an earlier step did" in a session resumed in a new conversation or summarised: Question 4 names that weak point and the human accepted it.
- The merits of proposals P1 and P2: they stand for the human at the request. P2's sentence does read wrongly on route 5.
- WAY-80 and WAY-229 above three binding sentences: on the base, outside the task.
- The warning on `AGENTS.md:21`: on the base, outside the task.

## Coverage the handoff asks for

### To do

| Item | Result |
|---|---|
| 1 Judged and rebuilt | Met in shape: ten files beside the skill, `SKILL.md` 1161 words. Findings 2, 3 and 7 are places where it departs. |
| 2 Step 0 reads nothing at once | Met. Each position of the task's lists checked against `read_sources.md:3-5`, `:17`, `:28` and `reading.md:40`. |
| 3 Template before the first step that uses it | Met on all routes (`SKILL.md:87`, `:96-97`, `:102-103`). |
| 4 Third answer in `kind_skill.md` | Met, word for word as Question 2, with `(WAY-256)`. The skill breaks it at finding 3. |
| 5 Variant file named in `SKILL.md` | Met: `research.md` at `:89`, `new_tools.md` at `:104-105`, each with its condition. |
| 6 The sentence ending step 0 | Met in both skills; the styleguide's only change is that sentence. |
| 7 Assessment and counts | Assessment met, with finding 10. Counts not met: finding 1. |

### Acceptance criteria

| Criterion | Result |
|---|---|
| No rule lost or changed | Not met: findings 2 and 3. Otherwise my comparison agrees with the author's: 17 base fragments not verbatim, each read against the head. |
| Each pointer recognisable | Met, with finding 6. |
| Reviewer's walk | Done below. |
| Fragment needed in several places reaches each | "How to show" and `task_document.md` reach theirs. |
| "A new level" and the audit apart | Not met as written: finding 2. |
| No Python changed | Met: the diffstat holds Markdown only. |

### Settlements to record

| Row | Result |
|---|---|
| 1 | Written into WAY-256 in place, as the orchestrator ruled; the clause on unchanged fragments holds for it. Finding 4. *Rejected* keeps both ways of Question 2 with their reasons. |
| 2 | WAY-265 written as its own entry. Findings 5 and 9. *Rejected* keeps both ways of Question 3. |
| 3 | WAY-266 written as its own entry. Finding 9. *Rejected* keeps the three ways of Question 4. |

### The walk, from `SKILL.md` without the entry point

`SKILL.md:18-23` gives the location and says files are read when their step comes, so the entry point adds nothing a session needs. All routes begin `SKILL.md`, `recognize.md`. "Not reached" lists rules of the base.

| Route | Files after `recognize.md`, in order | Not reached |
|---|---|---|
| 1 | `testing/template.md`, `starting_set.md`, `research.md`, `critique/SKILL.md` with `prepare.md`, `check.md`, `settle.md`; no step 3; `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, section "Critique before collective review", `hand_back.md` | none needed. Audit rules need tests. |
| 2 | as route 1 without `research.md`; the critique files come at step 4 | none needed |
| 3 | as route 1, with `audit.md` after the critique of step 2 | the cycle's-choice sentence, on the narrow reading (finding 2) |
| 4 | `testing/template.md`, `starting_set.md`, `audit.md`, `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, the section, the critique files, `hand_back.md` | as route 3 |
| 5 | `testing/template.md`, `new_level.md`, `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, the section, the critique files, `hand_back.md` | `audit.md:17-20` (finding 7). `new_level.md:4` misreads here (proposal P2). |
| 6 | `orchestrated_mode.md` before `recognize.md`, then route 1; research and critiques are requested from the project orchestrator | as route 1 |

`new_tools.md` joins any route that leaves a tool as a technology question, and both `SKILL.md:104-105` and `settle.md:3-4` send the agent there. No pointer leads to a file that does not exist.

### The author's own-work check

The requirement it names, rule preservation, fits the weakest point. Its first check compares text, so it reported the mode of finding 2 and left the judgement of meaning to the author, who judged it meaning-preserving. Its walk took the narrow reading. Neither it nor the check of the reports would catch finding 1, 3 or 4.

## Foundation read

Selection by "Reading the foundation" for `product-guidelines`, `instruction-files`, `decisions`: 151 decisions by *Scope* and *Decisions in play*. I read every question heading and these 40 whole: WAY-05, 07, 14, 19, 30, 33, 35, 113, 120, 127, 128, 129, 134, 150, 154, 172, 174, 214, 215, 238, 241 to 254, 256 to 259, 265, 266. *Decisions in play* are all among them.

The other 111 I read by heading only, which is short of what the method asks. Their headings concern the styleguide, linters, technology choices and other elements' forms, and the sentences of the skill that cite them moved verbatim. A finding that rests on one of them would not have been seen.

Also read: the part map entries of the three parts; the 15 invariants whose *Part* names `every` or `decisions`; the glossary's list of terms, with `exemplar` and `binding sentence` whole; the fact `claude-skill-nested-references`. No invariant test changed.

## Checks

| Check | Result |
|---|---|
| `git rev-parse HEAD`, `git log`, `git diff --stat` on the range; `git status --short` | exit 0; head as given, 14 files, Markdown only, worktree clean before and after |
| `python -I -B elements/common/foundation_check.py` | exit 0, 0 errors; it does not count binding sentences |
| `python -I -B instruction-files/check_instructions.py .` | exit 0, 0 error, 1 warn (`AGENTS.md:21`, on the base), 3 info; it does not reach this skill |
| `python -I -B agent-instructions/skill_entry_points.py` | exit 0, entry points are current |
| `python -B -m unittest installation.test_testing_guidelines_installation gate.test_skills_reach_the_way_sessions` | exit 0, 4 tests OK. A first run with `-I` exited 1 on import only: `-I` drops the working directory from the module path |
| own script: every quote of `assessment.md` against `git show 00c0a74:...`, line ranges and links | exit 0; 44 rows, 44 literal; the 2 proposal quotes literal; the 227 nonblank lines each in exactly one row, none missing |
| own script: every route's list and sum in `word-counts.md`, with `.split()` as `wc -w` counts | exit 0; "before" all equal; `recognize.md` differs on all six routes, finding 1 |
| `wc -w` over the skill's files, the templates and the critique files; the base `SKILL.md` | 3042 at the base, 1161 at the head, `recognize.md` 422 in `d024d56` and `5dc4b3b`; the task's figures (396, 1739, 1336, 3187, 322, 509) agree |
| own script: base sentences against the eleven files, both directions | exit 0; 17 base fragments not verbatim, 35 head fragments not in the base; I read each against the other side |
| own script: binding sentences of every entry, "must" in prose | exit 0; WAY-256 at four; findings 4 and 8 |
| manual: reading every changed file against the base and the task; the walk | see above |
| `grep` for section names and pointers across the-way, for restatements of the placement rule, for the styleguide's variant pointers | no incoming reference to a moved section; `kind_skill.md` alone holds the rule; findings 5 and 10 |

**Not run:** the whole gate, by the handoff; it is the orchestrator's run, in progress when I wrote this. Behaviour of a real agent on these routes is unverified: the walk reads the text.

## Reaches beyond the dispatch

- `foundations/decisions.md`, WAY-263 binding sentence: the method cites it for grading.
- `foundations/decisions.md`, binding sentences of WAY-80 and WAY-229: a control on finding 4.
- `foundations/environment_facts.md`, `claude-skill-nested-references`: WAY-265 rests on it.
- `product-guidelines/styleguide/*.md`, the pointers only: finding 5.
- `project-level/task/skill/guideline_findings.md:39-42` and `orchestrated_mode.md`: finding 2 and the orchestrated pointer.
- `.runs/task-cycles/testing-skill-shape/cycle.md`: to see when the counts were made and what the orchestrator recorded.

## Searches not found or unclear

- Unclear: `author.md` describes choices 7 and 8 in the old form; its repair note says so, and I judged the tree.
- Unclear: whether row 2's "pliki" means a skill's every file or the step and variant files. I took the second, which the row's own example requires.
- Otherwise none.
