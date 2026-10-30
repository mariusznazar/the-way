FAIL 802b56de85c63afdb8ba5a42c83bd1f5ea060260

# Review of the whole change — maintain-styleguide in the WAY-256 shape

Range `525cde1dd53c474f56ea0ece289cb60e868aa90d..802b56d`, commits b63f7cd and 802b56d. `git rev-parse HEAD` is the head given. One author, no plan, no slices, no spec: this is the only review the change gets.

Blocking: 2. Minor: 6. Out of scope: 0 findings, 2 lines of Declined to judge.

The rebuilt text itself holds: every line of the base reaches its new place, the pointers name their moments, no Python changed. The two blocking findings are narrow and cheap: one clause in `recognize.md`, and one read missing from the word counts.

## Blocking findings

### 1. The word counts leave out one file section the base has read twice (Important)

**Anchor:** `.runs/task-cycles/styleguide-skill-shape/reports/word-counts.md:7` (and every route list and the summary, `:18-24`); the read it misses is base `product-guidelines/styleguide/SKILL.md:93` and `project-level/task/skill/read_sources.md:5`.

**To paste:** The section "Reading the foundation" of `elements/common/way_of_working.md` (492 words) is read by `refine-task` and again at the base's step 0, yet it is in no route's list, so every "before" figure is 984 too low and every "after" figure 492 too low. The rule of the count says that a file read twice counts twice.

**Why I report it:** To do 4 and task question 3 make the second reading of a file the very thing the figures must show ("plik czytany dwa razy w stanie „przed” liczy się dwa razy"), and the orchestrator's rule says every read counts, refine-task's first reading of a file the skill makes the session read again included.

The mechanism: base line 93 reads "Select and read the product's foundation by "Reading the foundation" in `elements/common/way_of_working.md`", the same section `read_sources.md:5` has the session read at refine-task's step 1. That makes four things step 0 reads again, not the three `word-counts.md:7` lists (`tools/word_counts.py:66` holds only those three). The stated exclusion of "the entries of its foundation" (`word-counts.md:12`) covers the product's entries, not this section, which is the-way's own method text and has the same size in every product. No line of the file says it was left out on purpose.

The effect is on the figure the human reads as the gain: the second reading disappears in the rebuild, so the saving is understated by 492 words on all seven routes; on route 2, "without first reads" before is 9334 / 9843, not 8842 / 9351. The first reads become 2835 words, not 2343.

Figures with the section counted, recomputed by `recheck.py` from the same file sizes (the after figures without first reads do not change):

| Route | Before: to step 4 / total | After: to step 4 / total | Before without first reads | After without first reads |
|---|---|---|---|---|
| 1 | 12678 / 12678 | 7281 / 9663 | 9843 / 9843 | 4446 / 6828 |
| 2 | 12169 / 12678 | 6239 / 9452 | 9334 / 9843 | 3404 / 6617 |
| 3 | 12678 / 12678 | 7518 / 9900 | 9843 / 9843 | 4683 / 7065 |
| 4 | 12169 / 12678 | 6239 / 9452 | 9334 / 9843 | 3404 / 6617 |
| 5 | 12678 / 12678 | 7518 / 9900 | 9843 / 9843 | 4683 / 7065 |
| 6 | 12678 / 12678 | 7385 / 9767 | 9843 / 9843 | 4550 / 6932 |
| 7 | 12169 / 12169 | 4077 / 4077 | 9334 / 9334 | 1242 / 1242 |

The task's own estimate of about 8850 (2830 + about 6000) did not include this section, so `word-counts.md` should say that this is why its "before" figure now stands about 490 above the estimate.

Fix: add the section to `FIRST_READS` and `STEP0` in `tools/word_counts.py`, regenerate, and correct the sentence on "three files" and the author's figures. No file of the commits changes.

### 2. `recognize.md` has the session read again the guidelines `refine-task` already read (Important)

**Anchor:** `product-guidelines/styleguide/recognize.md:10`; against `project-level/task/skill/read_sources.md:28` and `product-guidelines/reading.md:40`; the sentence that should cover it is `product-guidelines/styleguide/SKILL.md:65-69`.

**To paste:** To do 2 says what the session read at refine-task's steps 1 and 2 is not read a second time. `recognize.md:10` still reads "every file under `guidelines/`", which includes the files of the task's parts that refine-task step 1 read whole. On a refresh or an extension that is the styleguide itself.

**Why I report it:** To do 2 has two halves: each file is read at the step that needs it, and "to, co sesja przeczytała już w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz". The second half holds for the three files and the foundation and is missed here.

The mechanism: `read_sources.md:28` reads the product's guidelines of the parts the task touches, and `reading.md:40` reads whole every file whose *Applies to* names such a part. For a task about the styleguide of part `web`, that is `guidelines/styleguide-web.md` and any other file naming `web`. Then `recognize.md:10` says "Read the product's root `AGENTS.md` and every file under `guidelines/`", with no exception. The sentence right after it in the same bullet makes exactly the exception for the foundation ("besides what `refine-task` selected at its step 1"), so the file treats two reads of the same kind differently. `SKILL.md:65-69` lists what is not read again and does not list the guidelines.

The route this costs most is 4 and 5: an agent reads the accepted styleguide twice before step 2. The cost is the product's words, so it stays out of the word counts by the orchestrator's rule, and that is why nothing showed it. The author's assessment row for line 92 does not mention it; proposal P1 notes the repetition and bundles it with narrowing the reading, which is a different change.

This is not P1. The set of files the session has read after step 1 stays the same, so the rule's meaning stays the same, and the frozen task accepts it as a meaning-preserving reword.

Fix: at `recognize.md:10`, "Read the product's root `AGENTS.md` and every file under `guidelines/` that `refine-task` did not read at its step 1." Add the row's note to `assessment.md` (row `:92-92`).

## Minor findings

### 3. `kind_skill.md` now has no answer for a fragment several steps need, but not all (Minor; the wording is what To do 3 mandates)

**Anchor:** `instruction-files/kind_skill.md:8-14`; `reports/assessment.md` rows `:43-46`, `:116-118`, `:166-168`, `:170-177`; `product-guidelines/styleguide/SKILL.md:44`.

**To paste:** The two answers are now "every step needs it" and "only one step or one variant needs it", so a fragment that two or three steps need fits neither. Tasks 5 to 11 judge by this file and will meet that case. Should it be settled now?

**Why I report it:** To do 3 asks for the wording the change has, and it removes the contradiction it was asked to remove. The defect is what the narrower first answer leaves. Under the base's "every use needs it" such a fragment had an answer, a wrong one for a step's procedure; now it has none in this file, and WAY-256 says only that "only one step" goes beside and that SKILL.md keeps rules "that hold across its steps".

The rebuilt skill shows the gap in use, with three different treatments: "How to show", needed by steps 1, 2 and 4 by its own row, stays in `SKILL.md` under the heading "Rules that hold at every step", though steps 3 and 5 do not use it; the list of the task document, needed by steps 4 and 5, goes beside the skill; the definition of refresh and extension goes to the first step that needs it, under a rule stated only in that assessment row ("a rule that holds on two steps is placed in the file of the first"). Each is defensible. None follows from the file the next seven tasks judge by, and a reviewer of task 5 could block any of the three.

The gap costs nothing in this skill; it costs one more round of the same question in later tasks. A clause at line 11 ("needed across the steps") would close it, but it goes beyond the task's wording, so it is a question for the human or for task 5.

### 4. Variant files stand two levels from `SKILL.md`, and the materials do not say so (Minor)

**Anchor:** `product-guidelines/styleguide/starting_rules.md:10`, `settle.md:4`, `settle.md:38`; against `instruction-files/SKILL.md:174-179`.

**To paste:** `research.md`, `new_tools.md` and `staged_cleaning.md` are reached through a file beside the skill, while `instruction-files/SKILL.md:174` says a step points one level deep. The assessment table does not mention this; only the author's report does.

**Why I report it:** The skill the task judges by says "A step of a route points directly and one level deep (step → file)", resting on the fact `claude-skill-nested-references`: Claude may read only part of a file referenced from a referenced file, for instance with `head -100`. That principle names no decision, so by `instruction-files/SKILL.md:17-18` it is a proposal, not a binding rule, and WAY-258 binds this depth only for the files of `instruction-files`.

The concrete failure cannot happen at these sizes: the three files are 5 to 16 lines. `refine-task` has the same shape (`read_sources.md:10-12`). The author's reason, that the moment arises inside the step, is sound. The remaining fault is that the human reading the table does not see the choice, and task 5 will copy it as the pattern. Fix: one sentence in the new-place cell of rows `:128-137`, `:178-183` and `:216-219`.

### 5. `staged_cleaning.md` is one sentence behind a pointer (Minor)

**Anchor:** `product-guidelines/styleguide/staged_cleaning.md:3-5`, `settle.md:37-38`; assessment row `:216-219`.

**To paste:** The file holds one sentence, and the pointer to it takes 21 of those 54 words. Is that two instructions, as the row says, or the one instruction WAY-256 keeps where its pointer would stand?

**Why I report it:** WAY-256 gives as a breach "a file beside a skill holds one instruction and its step names it by a pointer", and as compliance "the one sentence only one variant of a skill needs stands in that variant's row". The base has this as one list item of "Propose:". The author counts two instructions (propose the invariant marked violated; say that only the review keeps it), and "say when proposing it" can be read that way, so the verdict is defensible and stands in the table where the human can dispute it. On the other reading the item goes back into `settle.md:37-38`, and the change has one file less to keep. No agent goes wrong either way; hence not blocking. `new_tools.md` is several instructions and is rightly beside the skill.

### 6. Step 0 assumes `refine-task` ran (Minor)

**Anchor:** `product-guidelines/styleguide/SKILL.md:65-69`, `recognize.md:11`.

**To paste:** A session that opens this skill directly, as its description allows, is told that the task template, "How a skill asks" and the foundation are "not read again" although it never read them. Nothing sends it to `refine-task` first.

**Why I report it:** The walk through the routes reaches every rule when the session comes through refine-task. The base protected the other way in: step 0 read refine-task's `SKILL.md`, the template and the foundation whatever came before. Now the only guard is `SKILL.md:27-29` ("`refine-task` opens or resumes the task through its steps 1 and 2; this skill takes over at its step 3"), a description rather than an instruction. The skill's description ("Use when a product's user interface … needs a styleguide …") invites direct entry.

The author's concern 1, a resumed session, is not this gap: a resumed task goes through refine-task's steps 1 and 2 again, so it reads them. Direct entry is the gap. I found no record of how often it happens, so I cannot say it is common. I keep it Minor because the text does name refine-task as the way in, and a careful agent goes there. Fix: end step 0 with a clause such as "a session that did not come through them starts at `refine-task`'s step 1". That is a new rule, so it is the human's call, not the fixer's, unless the orchestrator takes it as following from `SKILL.md:27-29`.

### 7. `assessment.md` departs from the form `judging.md` gives (Minor)

**Anchor:** `reports/assessment.md:53`, `:61`, `:84` (rows `:69-71`, `:110-112`, `:220-220`); `reports/assessment.md:31` against `instruction-files/judging.md:11-26`.

**To paste:** Three rows name no ground, and contradictions stand before the table rather than after it.

**Why I report it:** `judging.md:21-25` asks for a ground in every row: a mistake, a cost, or a carried decision or step. Rows `:69-71` and `:220-220` give a reason and no ground; row `:110-112` says "as the row before" and stops. Grounds are one clause each (WAY-134, WAY-168 and WAY-256 are the candidates). The order is `judging.md:11-26`: check, table, contradictions. WAY-257's own demand, both answers in every row, is met in all 50 rows. The human can still read the table; the task's To do 4 lists no ground column, hence Minor.

### 8. The rule on refine-task's other files, and the author's account of the 5900 estimate (Minor)

**Anchor:** `reports/word-counts.md:8`; `reports/author.md:110`, `:76`.

**To paste:** Two matters of the counts' account, neither changing a difference between before and after: `word-counts.md:8` departs from the rule as written and needs the orchestrator's confirmation, and the reason `author.md:110` gives for missing 5900 is wrong and should not go into the request.

**Why I report it:**

- `word-counts.md:8` leaves out the files refine-task sends the session to, on the ground that they are equal in both states. The orchestrator's rule reads "A file a counted file sends the session to on the route counts in both states", and refine-task's `SKILL.md` is a counted file. Read literally, that adds `read_sources.md` 298, `draft.md` 240, `resolve_gaps.md` 411 and `product-guidelines/reading.md` 1141 words on every route; `guideline_findings.md` 453 where a finding sends the session there; and on route 6 refine-task's `orchestrated_mode.md` 579 and `project_plan_task.md` 205. The exclusion is stated, the difference stays the same and only the percentages move, so this is for the orchestrator to confirm or to order counted. I recommend confirming and keeping the stated exclusion: counting them would blur the comparison with the task's estimate, which is what the rule's extra figure is for.
- `author.md:110` says 5900 was missed because `SKILL.md` is 906 words rather than about 600, and that at 600 the figure would be about 5800. That does not follow: on route 2 every step's file is read, so a word moved from `SKILL.md` into them leaves the sum unchanged. The task's estimate comes from about 8270 less about 2350. The real gap of about 700 words is the 509 words of the files beside the critique, plus about 190 words of what the rebuild adds on that route (pointers, the step 0 paragraph, the files' headings). `word-counts.md` itself does not repeat the wrong reason.
- `author.md:76` says "216 lines". The base has 205 nonblank lines; 216 is the sum of the rows' ranges, blank lines inside them included. The coverage claim itself holds.

## Declined to judge

- P1 and P2, the two proposals not applied: whether to narrow the reading of `guidelines/` or the WCAG proposal is outside the task, which leaves them as proposals. I checked only that their quotes are exact and that they stand as proposals.
- Whether the orchestrated-mode files of the three guideline skills should merge: the task's *Context* leaves this to task 8.

## Coverage

### To do and acceptance

| Item | Result | How |
|---|---|---|
| To do 1, judged and rebuilt in the shape of WAY-256 | met, save finding 2's clause; form of the table: finding 7 | read each of the 11 files against the base; `SKILL.md` holds the picture, rules across steps and pointers; the one-instruction exception judged per file: `hand_back.md` is two instructions, `new_tools.md` several, `staged_cleaning.md` finding 5 |
| To do 2, step 0 stops reading everything | **not fully met**: finding 2 | each file of step 0 followed to its step; `product-guidelines/template.md` is first needed at step 4 and the styleguide template at step 2 (I checked both against steps 1 to 3); refine-task's reads confirmed in `read_sources.md:3-5` |
| To do 3, `kind_skill.md:8-14` | met; a gap remains: finding 3 | diff read; `grep` of the repository shows no other copy of "every use needs" |
| To do 4, assessment table | met; form: finding 7 | recheck below |
| To do 4, word counts in seven routes | **not met**: finding 1 | recheck below |
| Acceptance 1, no rule lost or changed | met | own clause comparison (155 clauses, 18 not verbatim, each accounted for below) and the walk |
| Acceptance 2, each pointer names its step or variant in words an agent recognises | met | every pointer read: `SKILL.md:59-61`, `:73`, `:77`, `:82-84`, `:88`, `:93`; `starting_rules.md:9-10`; `settle.md:3-4`, `:37-38`, `:40-42`; `research.md:13`; `hand_back.md:3`. None rests on the entry point or the `the-way-` prefix for its condition |
| Acceptance 3, no Python changed | met | `git diff --name-only` over the range: 12 paths, all `.md` |
| *Settlements to record* | none in the task, none written | none of the 12 paths lies under `foundations/` |

Moving "How to show" and "Write each answer" from step 4 to every step: I checked this as the likeliest change of meaning. WAY-174 binds "every choice they settle" and every term of the field, so the text now says what the decision says. `resolve_gaps.md:4-6` already binds the second one at refine-task's step 3. Step 2's preference question is a question of assessment, not a choice, so "the ways open, their cost and a recommendation" does not clash with `way_of_working.md:34-35`. No finding, beyond the heading's "every step" in finding 3.

The 18 clauses not verbatim in my comparison: 2 are table rows my splitter joined, 2 are headings it joined to a sentence that stands verbatim, and 14 are the author's list in `author.md:59-72`. I read each of the 14 against its new text. The one with most weight, base line 93, split well: WAY-165 is about the agent's way, and the citation stands with that clause in `audit.md:6`.

### The seven routes, walked as an agent reading `SKILL.md` by its path

Every route is entered through refine-task's steps 1 and 2; direct entry is finding 6. "Not reached" names what a run of that route does not read, and whether that is right.

| Route | Files reached, in order | Rule of the base not reached |
|---|---|---|
| 1 first, no screens, no preference | `SKILL.md`, `recognize.md`, styleguide `template.md`, `starting_rules.md`, `research.md`, critique `SKILL.md`, `prepare.md`, `check.md`, `settle.md` (critique); `product-guidelines/template.md`, `settle.md`, `task_document.md`, section "Critique before collective review", `hand_back.md` | `audit.md` and the decisions on the agent's way: right, no audit runs. `new_tools.md` on its condition |
| 2 first, no screens, preference | as route 1 without `research.md`; the critique files at step 4 | as route 1 |
| 3 first, screens | as route 1, with `audit.md` before step 4 | none. `staged_cleaning.md` and `new_tools.md` on their conditions |
| 4 refresh, screens unchanged | as route 2 | `audit.md`, so also "A palette read off the code is a proposal" and "An existing choice the human keeps becomes a decision…" (base `:166-168`). On the base those stand in step 3, which this route skips by step 1's mode, so nothing is lost; the assessment row says the same |
| 5 extension, screens changed | as route 3 | none |
| 6 orchestrated, on route 1 | `orchestrated_mode.md` first, then route 1 | as route 1. `research.md:13` still has the session read the critique skill though the orchestrator starts the critic; that matches the base, where step 0 read it |
| 7 no interface | `SKILL.md`, `recognize.md`; ends at `recognize.md:4` | everything after step 1: right. `AGENTS.md` and `guidelines/` go unread on this route, by the order `recognize.md:3-10` gives; WAY-185 puts recognizing first |

### Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation | `python -B elements/common/foundation_check.py` | 0, 0 errors |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0; 0 errors, 1 warning, 3 info, the same as `assessment.md:21-27` |
| Tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0, 18 tests |
| Tests of `instruction-files`, which the author did not run | `python -B gate/run_tests.py instruction-files` | 0, 104 tests, 5 skipped |
| Tests of `installation` | `python -B gate/run_tests.py installation` | 0, 44 tests |
| Whitespace | `git diff --check 525cde1..802b56d` | 0 |
| Line endings | `git ls-files --eol product-guidelines/styleguide instruction-files/kind_skill.md` | all `i/lf w/lf` |
| Worktree untouched | `git status --short` | clean, before and after |
| Recheck of the materials, my own script, not the author's | `python -B <scratchpad>/recheck.py <out>` | 0; script and output below |

What the recheck showed:

- 50 main rows and 2 proposal rows: every quote equals the base, every line range and link agrees. All 205 nonblank lines of the base stand in exactly one row.
- Every route figure of the summary and all 22 file lists reproduce, as the files the lists name. All file sizes reproduce: `SKILL.md` 2830 on the base and 906 now. Finding 1 is what the lists leave out, not an error of addition.
- `product-guidelines/template.md`, styleguide `template.md`, the task template, refine-task's `SKILL.md`, critique `SKILL.md` and `way_of_working.md` are byte-equal to the base, as question 1 requires.
- Every `.md` path in backticks in the eleven files resolves, apart from the product paths and `<part>` patterns.
- Files beside the critique: I grepped them for further files; they send the session nowhere else.

Script: `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\da5f3fbe-3569-48c8-a993-d28779b79354\scratchpad\recheck.py`, output `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\da5f3fbe-3569-48c8-a993-d28779b79354\scratchpad\recheck.txt`.

### Not run

- The whole gate: by the handoff, it is the orchestrator's run.
- A session of an agent on the rebuilt skill: not run, by the method's bound on a review; the walk above is a reading, so whether agents take each pointer is unverified. The author says the same.
- Comparison of the materials' form with PR #52, the task's pattern: not made. I judged the table against `judging.md` and the task.

### Author's own-work check

It names rule preservation and checks it sentence by sentence. That is the right requirement, and the check would catch text lost. It would not catch a rule that stands but no longer reaches its route; the walk above does that and finds none. The author's report that 23 decisions went unread (`author.md:117`) was a real hole; I read 21 of them whole, WAY-155 and the tail of WAY-134 excepted, and none is broken by the change.

## Foundation read

Selected by "Reading the foundation" for `product-guidelines` and `instruction-files`, 92 entries with the task's *Decisions in play*.

- Read whole: WAY-02, 09, 27, 34, 38, 51, 89, 100, 102, 107, 120, 127 to 133, 154, 165, 167 to 174, 176 to 178, 180, 182 to 187, 189, 191, 192, 198 to 210, 213 to 215, 251, 256 to 259, 263. Every entry of the task's *Decisions in play* is among them.
- Read by heading only, for bearing on the change: WAY-211, 212, 216 to 219, 221, 228 to 250, 252 to 254. These bind the coding and testing disciplines, a user-interface change's evidence and tools of a product; this change moves no text of theirs.
- Part map: entries of the two parts read; `product-guidelines/**` and `instruction-files/**` claim every new file.
- Invariants: none names either part in *Part*; `skill-rule-source` read, and it does not reach this skill. `skill-entry-points` is covered by the tests of `agent-instructions`; the entry points are unchanged because the description is.
- Glossary: searched for the terms the change turns on (route, step, variant, skill, entry point, fragment); no entry of those names.
- Guidelines: the selection is empty (task question 6).
- No invariant test changes. No trust boundary is touched, and no irreversible operation.

## Reaches beyond the dispatch

- `instruction-files/SKILL.md` and `instruction-files/judging.md`, whole: the method of To do 1, for findings 3, 4 and 7.
- `project-level/task/skill/SKILL.md`, `read_sources.md`, `draft.md`, `resolve_gaps.md`, `guideline_findings.md`, `orchestrated_mode.md` and `product-guidelines/reading.md`, whole: what refine-task truly reads, for findings 1, 2, 6 and the walk.
- `product-guidelines/template.md`, `product-guidelines/styleguide/template.md`, `elements/common/critique/SKILL.md`, `elements/common/way_of_working.md:1-88`: to judge when each file is first needed.
- `foundations/environment_facts.md` entry `claude-skill-nested-references`: finding 4.
- `.claude/skills/the-way-maintain-styleguide/SKILL.md`: the entry point's reading rule, for acceptance 2.
- `.runs/task-cycles/styleguide-skill-shape/tools/word_counts.py`: to find what the count leaves out; I did not rest on its figures.
- `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md`: before writing my scripts.

## Searches not found or unclear

- A statement anywhere in `word-counts.md` that "Reading the foundation" was left out on purpose: not found (finding 1).
- How often sessions open `maintain-styleguide` directly rather than through refine-task: not found; the records are outside this worktree (finding 6).
- Whether WAY-256 sends a fragment of two steps beside the skill or keeps it in `SKILL.md`: unclear from its text (finding 3).
- Whether "one instruction" in WAY-256 covers a sentence with a rider: unclear (finding 5).
- For the orchestrator, unverified and from memory: GitHub limits a request's body to 65536 characters, as far as I recall. `assessment.md` is 50209 characters and `word-counts.md` 18081, 68290 together, so the two may not fit in one body.
