FAIL c2e70f9f1e01e1ebfbeed0ff69352c498b674a8a

# Review of the whole change: settle-technology in the shape of WAY-256

Range `525cde1dd53c474f56ea0ece289cb60e868aa90d..c2e70f9` (one commit, seven Markdown files). `git rev-parse HEAD` gives the head named. No plan, so a blocking finding has no slice to name: both come from the one author's commit or its reports. Every item below opens a new thread.

Counts: 2 blocking (Important), 5 Minor, 1 out of scope.

## Blocking findings

### 1. A resuming leader whose human changes the list never reaches the rules of the list

**Grade:** Important. Within the task (acceptance criteria 1 and 3).

**Anchor:** `project-level/technology/SKILL.md:33-35`, `project-level/technology/start.md:20`

**To paste:** On a resume with open choices the leader asks whether the list still holds, but it is told to read `list.md` only when the look adds an item. A human who adds or changes an item at that question leaves the leader without the rules for wording and marking it, which stand only in `list.md`.

**Why I report it:** `start.md:20` keeps the old sentence "Then show the list, ask whether it still holds", and the old `SKILL.md:74-75` shows what that answer can be: confirm, add, strike. In the old file the leader had read step 1 whatever it did, so an added item met these rules. After the change the only route to `list.md` from a resume is `SKILL.md:34-35`, "when the look it gives adds an item to the list", repeated at `start.md:15-16`. So the moment "the human adds an item" has no pointer.

What the template still carries for that leader, read whole on every route: the markers, naming by need (`definition_template.md:184-192`) and nested items (`:194`). What only `list.md` carries:

- `list.md:15-17`: a way of logging in is listed as its method, and its library is a choice of its own.
- `list.md:19-22`: a decision that settles the choice in a sentence about something else still holds it; a decision the project changes no longer holds it.
- `list.md:23-24`: writing the list and the status line before asking.
- `list.md:25-29`: why each item is needed, and the question on preferences.

Example: resuming, the human says "add logging in with Google". The leader writes a library as an item, or marks `— open` a choice a foundation decision settles in a sentence about something else, and research starts on it. Nothing reports this: the marker is valid, so `readiness_check.py` passes it.

The author saw the cost in "Choices" item 3 ("a leader that adds an item without reading `list.md` names it badly; the pointer is in `start.md` at that bullet"), but the pointer stands at the look's bullet only. Assessment row `[63-66]` says "A resumed leader that adds an item reads list.md for this rule", which is true of the look alone. `checks/reach.py` asserts only the fragments the criteria name, so it could not catch this.

Criterion 3 names two fragments after a colon. I read them as the cases it must reach, not as a limit on "a fragment needed in more than one place"; criterion 1 asks the same without a list. This is a reach gap on one sub-route, not a lost sentence: the text stands in `list.md`.

Fix, a few words: in `SKILL.md:34-35`, "when the look it gives or the human adds or changes an item", and the same in `start.md:20`, for instance "ask whether it still holds; where the human adds or changes an item, follow the step "List the choices" (`list.md` beside this file) for it". The conditional line of `word-counts.md` then covers that case too.

### 2. The count of the route "leader, resuming, open choices" leaves out `close.md`

**Grade:** Important. Within the task (To do 4). The number goes into the request.

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/word-counts.md:18`, `:66`; `.runs/task-cycles/technology-skill-shape/checks/word_counts.py:74`

**To paste:** The route "leader, resuming, open choices" is counted without `close.md`, though that leader ends in the step "Close" as the leader with a new list does, whose route counts it. The row should read 6427 and -201, not 6331 and -297.

**Why I report it:** To do 4 counts the words in the files read on a route. `SKILL.md:51` sends every leader to `close.md` once the list holds no open choice, and a resume with open choices reaches that state when its last wave is written. `settle.md` does not end the skill. Route "new list, open choices" lists `close.md` (`word_counts.py:73`), the resuming route does not (`:74`), and `word-counts.md` gives no reason for the difference.

My recount: 468 + 293 + 178 + 886 + 96 = 1921, plus 3675 fixed and 831 critique = 6427, against 6628 before = -201. All other rows recount exactly (see Checks). The conclusions in "Reading of the numbers" still hold.

The same route list sits at `checks/reach.py:20`, so the reach check never looked at `close.md` on this route. The figure "297" also stands in `author.md:101`.

Fix: add `close.md` at `word_counts.py:74` and `reach.py:20`, regenerate `word-counts.md`, and correct its file list at `:66`.

## Minor findings

### 3. Proposal 5.1: the sum of 387 is right, but "not about 800" is a judgement, and one section it drops is used

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/assessment.md:78`, `:82`

**To paste:** Proposal 5.1 adds up to 387 for its own list of sections, but the assessment never says why this differs from the "about 800" the human saw in question 2. It also leaves out "Gate record", which defines the fingerprint `SKILL.md:53` relies on.

**Why I report it:** My recount gives 63 + 81 + 98 + 65 + 80 = 387, so the arithmetic holds. The author's further claim (`author.md:102`) that 800 "does not match the sections" depends on what counts as a section the skill uses:

- "Every section, and the words `none` and `TODO`" is 478 words, and the skill uses only its opening sentences and two table rows. Dropping it too gives 865, close to the task's figure.
- "Gate record" (80 words) says which sections the fingerprint covers (`definition_template.md:344`), which is what `SKILL.md:53` means by "the sections its fingerprint covers". Keeping it gives 307.

So the honest result is a range of 307 to 865, depending on how whole a section must be unused. "800" does not appear in `assessment.md` at all, and only that file goes into the request. "No step of the skill uses them" (`:82`) is also the reason given for not searching the omitted sections, which makes the search circular. The proposal's verdict, not recommended, may well stand; the human should see what the figure rests on.

### 4. `research.md`: a new clause is undisclosed, and its word does not match the file

**Anchor:** `project-level/technology/research.md:12-13`

**To paste:** "your own output is the one report below" is a new statement the assessment does not list, and below it the file says only "the comparison", never "report". The opening "The step" also has no antecedent in this file.

**Why I report it:** The clause changes no rule: the old text already ended the agent at "writes the comparison ... and ends", and the agent needs it, since "The step writes into the definition" could otherwise read as permission. But `author.md` choice 8 calls its list "the only new statements" and omits this clause, and assessment row `[24-25]` says the sentence was copied word for word. The handoff counts every gloss as a rewording, so the request should name it. An agent will map "report" to the one file it writes, so nothing goes wrong; for criterion 4 the fix is one word: "the one comparison below". The gloss "A reference such as (WAY-122) ..." is also missing from `assessment.md`, though `author.md` lists it.

### 5. Two files named `settle.md` are in play at the same moment

**Anchor:** `project-level/technology/settle.md`; `elements/common/critique/SKILL.md:37`

**To paste:** While following the technology `settle.md`, the leader reads the critique's instruction "the author reads `settle.md` beside this skill". The same name for two files can make it skip the critique's own closing rules or reopen the wrong file.

**Why I report it:** The critique's file holds how the author settles the review (70 words). The risk grows after a compaction, and the one real run was compacted six times. This is reasoning from the names; no record shows it happening. Cost of leaving it: an occasional wrong read. Cost of a rename such as `settle_choices.md`: the pointers in `SKILL.md`, `start.md`, `close.md` and the reports.

### 6. Eight rows of the assessment name no ground

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/assessment.md`, rows `[27-27]`, `[36-36]`, `[46-46]`, `[48-48]`, `[79-79]`, `[81-81]`, `[160-160]`, `[166-166]`

**To paste:** These rows give a verdict with no ground, which the judging method asks of every row. Four are headings; the others are moved bullets whose only change is a reference.

**Why I report it:** `instruction-files/judging.md:15-25` asks for a ground in each row: a mistake, a cost, or a carried decision or step. To do 4 lists four columns and WAY-257 two answers, and all 37 rows have those, so this is a gap against the method only. "Carried step of the skill" would close each row.

### 7. Stale figures in the author's report

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/author.md:20`, `:21`, `:101`

**To paste:** `author.md` gives `research.md` as 446 words, `close.md` as 102 and the research route's saving as 1676; the files and `word-counts.md` give 467, 96 and -1655.

**Why I report it:** The orchestrator's mechanical check found this, and my count confirms it. `author.md` does not go into the request, so only a figure copied from it could do harm. Finding 2 changes the 297 at `:101` too.

## Out of scope

### 8. "read off" in a meaning the glossary does not give

**Anchor:** `project-level/technology/research.md:22`; `foundations/glossary.md:121-123`

Beyond the task: the phrase stands in the old `SKILL.md:97` too, and only its person changed. The glossary defines "read off" as what a tool gives from the product or the machine as they stand, while here an agent reads a property from documentation. This is the one effect I found of the author not reading the glossary. It does not mislead the research agent, which gets no glossary, but the word holds two meanings (WAY-95, reached through `elements/common/way_of_working.md:97-99`).

## Each acceptance criterion by name

| Criterion | Result | Reader by reader |
|---|---|---|
| 1. No rule lost or changed in meaning, apart from To do 2 and 3 | **Text met; reach not met on one sub-route (finding 1)** | Word diff of all old text against all new text read hunk by hunk: every hunk is a move, a listed rewording, or text added by To do 2 or 3. All 20 rewordings keep their meaning. The rules of steps 2.2 and 2.3 the leader no longer reads remain in the template's Technology section (`definition_template.md:203-228`), read whole. |
| 2. Every pointer names its step in words an agent recognises, also read by path | **Met, apart from the condition of finding 1** | All pointers checked: `SKILL.md:33-35,39-40,44-47,51`, `start.md:12,14,16,21,24`, `list.md:12,30`, `settle.md:15,17,18,21,42`, `close.md:8,9`. Each gives the step's name or the state of the Technology section. `research.md` stands alone; each other file names its skill and that its `SKILL.md` lies beside it, and `SKILL.md` names all six directly. |
| 3. A fragment needed in several places reaches each | **The two named cases met; the criterion not met in general (finding 1)** | The look reaches both resumes through `SKILL.md:33-34` and `start.md:13-14`. The report name reaches the leader through `SKILL.md:28-29` and the agent through `research.md:35-37`. |
| 4. The research agent knows every term and rule from its file and what it is given | **Met (wording note in finding 4)** | The location of the-way, the template, `held by`, the three matters (true against `definition_template.md:167-183`), the WAY references, the report name and the foundation rule are all there. No wave, critique or step number. No rule of the leader's concerns it. |
| 5. Python unchanged | **Met** | The diff holds only seven `.md` files. |

To do: 1 met (judge mode in the order `judging.md` gives; finding 6). 2 met (`settle.md:12-16`, `research.md`). 3 met, including a resume where sub-step 4 falls away (`SKILL.md:46-47`, "or of a table", and `settle.md:41-42`); the template stays read in full (`start.md:5`). 4 met apart from finding 2. 5 followed. 6 met: the proposals stand as proposals and are unapplied (`start.md:5`, `research.md:22-34` and `list.md:26-28` are unchanged in substance), with finding 3 on 5.1. The sentences "the request names" belong to the request, which does not exist yet. *Settlements to record* reads `none`, so nothing is owed there.

WAY-256 as worded:

- Each of the six files holds more than one instruction. `close.md` is the shortest: run, route the findings, return. `running_product.md` is several instructions, and it serves a variant, a project with behaviour a user sees, reached from two steps, so it is neither every-use text nor one instruction.
- No file is one instruction behind a pointer.
- Rules across the steps stay: the foundation rule, the report name, the re-gate rule, the location paragraph.
- Reading instructions of step 0 moved because question 7 sends the whole step beside the skill.

Foundation: the change writes no entry. Nothing restates WAY-121, 122, 123, 137, 138, 165 or 166 differently. WAY-127's paragraph test holds for `SKILL.md` and `research.md`, and the prefix sentence now covers the files beside the skill. The search for references found nothing that names a step number of this skill from outside, and `define-project step 5` and `its step 4.1` are correct.

The author's own-work check named the right weak point, reach, but both its checks test presence of named text, and the reach check took the route lists from the author, so it could not catch either blocking finding.

`assessment.md`: the 37 quotations match `525cde1` character for character, the ranges and links agree, each non-blank line of 156 belongs to a row, line 91 alone is split and at the stated place, each row has both WAY-257 answers, and each word count in the last column is right.

The environment facts the author did not read as files have no effect: `claude-skill-nested-references` asks for references one level deep from `SKILL.md`, and `SKILL.md` names all six files and the critique directly. The template and `way_of_working.md` are read from `start.md`, a second level, because question 7 moves step 0; `start.md:5` says "in full" and `SKILL.md` also names both.

## Declined to judge

- How agents really follow the new pointers: the task accepts that the counts are of files, not behaviour (question 4), and no run exists.
- The growth of the longest route (+172) and of the seven files together (2122 to 2761, against "about 50" in question 7): the author reports it, WAY-256 sets place by need and never by count, and no requirement caps it.
- The request's own text, which To do 2, 3, 4 and 6 bind: it does not exist yet.
- Whether proposals 5.1 to 5.3 should be taken: that is the human's decision.
- The stub items 2 and 3 of `settle.md`: a choice of form with no effect on a rule.

## Checks

| Check | Exit | Result |
|---|---:|---|
| `git rev-parse HEAD c2e70f9` | 0 | both the given head |
| `git diff --stat 525cde1dd53c474f56ea0ece289cb60e868aa90d..c2e70f9` | 0 | 7 Markdown files, +203 -132 |
| `git ls-files --eol project-level/technology/` | 0 | all `i/lf w/lf` |
| `git diff --no-index --word-diff=plain --word-diff-regex='[^[:space:]]+' -U0` of old `SKILL.md` against the seven new files joined; read by hand | 1, as `--no-index` gives on a difference | 178 lines; every change accounted for |
| My own script: quotations, ranges, links, coverage, word numbers of `assessment.md` | 0 | 37 rows, 0 bad, 0 uncovered lines |
| My own script: all word counts and proposal 5.1 from `git show` | 0 | every figure of `word-counts.md` right; route list wrong (finding 2) |
| Manual: walk of the five routes through the pointers, file by file | n/a | findings 1 and 2 |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (`dead-path AGENTS.md:21`, unchanged), 3 info, as the assessment says |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B elements/common/foundation_check.py .` | 0 by a run behind a pipe, so the exit shown was `tail`'s; the output read `0 errors` | no foundation file changed |
| `python -B .runs/task-cycles/technology-skill-shape/checks/reach.py <scratch file>` | 0 | 77 assertions, 0 failed; passes with finding 2's route list |
| `python -B .runs/task-cycles/technology-skill-shape/checks/preservation.py <scratch file>` | 0 | exact=51, listed=20, problems=0 |
| `python -B .runs/task-cycles/technology-skill-shape/checks/word_counts.py <scratch file>` | 0 | reproduces the reported rows |
| `python -B gate/run_tests.py project-level` | 0 | 267 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `git status --short` after the tests | 0 | 0 lines, worktree clean before this report |
| `git log --follow --oneline -- project-level/technology/SKILL.md`, counted | 0 | 13 with this commit, so 12 as the assessment says |
| `git show 2a8954e:project-level/technology/SKILL.md` | 0 | 1335 words, no `runs/technology` |
| `zstd -dc` of the Codex record, then counted | 0 | 15,914,081 bytes, 5280 lines, the quoted reply at line 160, as stated; the decompressed copy was deleted from the scratchpad |

Not run: the full gate (the orchestrator's, as the handoff says); the author's negative controls (they change files, and my own checks do not rest on those scripts); `instruction-files` tests (no file they read changed). Not verified in the Codex record: the six compaction lines, the 17 reads and the 241 human messages.

## Reaches beyond the dispatch

- `C:\Storage\repos\loop2\.runs\technology-research\brief.md:13`, and the Codex record the assessment cites: to test claims of a required report.
- `foundations/glossary.md` whole (short), and `foundations/environment_facts.md` by search for the three facts the handoff's note concerns: to judge the effect of the author's not reading them.
- `elements/common/critique/SKILL.md` and `prepare.md`, `instruction-files/SKILL.md`, `kind_skill.md`, `judging.md`, `project-level/skill/SKILL.md:125-164`, `checks/reach.py`, `checks/word_counts.py`, `checks/changes.json`.

Foundation selection, under "Reading the foundation": the part `project-level` of the part map; the invariants `project-definition-form`, `project-readiness-gate`, `project-technology-record`; 68 decisions, those whose *Scope* names `project-level` and those the task names. Read whole: WAY-09, 10, 35, 38, 89, 100 to 102, 106 to 118, 120 to 124, 126 to 130, 133, 134, 137, 138, 150, 165, 166, 256 to 259, 263.

**Not read whole, a departure from the method:** WAY-139 onward in the plan, lead and guidelines range (140, 142 to 147, 151 to 156, 161, 172, 214 to 218, 230, 238, 242, 247). A case-insensitive search of all 68 for `technology`, `SKILL.md` and "beside a skill" hit only the entries I read whole, with hits there as the positive control, so I judged these by that search and their headings.

## Searches not found or unclear

- `author.md` choice 7 and the handoff say 9 changes of person in `research.md`. I find 7 verbs changed in 5 sentences: finds, gives, reads off, says, also says, writes, ends. Listing is not at issue, and no meaning changes on either count.
- `author.md:102` sets 387 against the task's 800 and points to the assessment for the section list and bounds; `assessment.md` gives those but never mentions 800 (finding 3).
- `.claude/skills/` entry points state that they serve a session on the-way; a product's entry point was not read, since `installation/` did not change.
- `cycle.md` not read, as the handoff requires.
