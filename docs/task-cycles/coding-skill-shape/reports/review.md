FAIL 097123ec5b41e322199566462c5bfbd65e479c46

# Review of the whole change: maintain-coding-guidelines in the WAY-256 shape

Range `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a..097123e`, one commit, one author, no plan, so no
blocking finding comes from a slice. `git rev-parse HEAD` in the worktree is the head given. Worktree
left clean (`git status --short` empty before and after).

Paths below without a directory are in
`C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/product-guidelines/coding/`; `<cycle>` is
`C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/`.

Result in one paragraph: the move itself is sound. Every base sentence stands or is accounted for, every
pointer selects what the base selects, all seven routes reach what they need in the right order, and the
word counts and quotes of the materials hold. Two blocking findings remain, both in text the change
added and no source gave: one sentence that makes the document of the one-kind route lose items, and one
reason written into WAY-216.

## Blocking findings

### 1. The opening of `task_document.md` drops items of the task document on the route of one kind (Important, within To do 10; new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/product-guidelines/coding/task_document.md:3`
(with `:15`, `:34-38`; same form at `settle.md:3`)

**To paste:** On the route of one kind this sentence limits the whole task document to what "The route
of one kind" gives, and that rule gives *To do* only the kind's file with its index row. The item "write
the test of each new invariant" is then not written, though that route settles invariants; *Context*
loses the comparison's `do not copy` places too.

**Why I report it:**

- What the sentence is for: To do 10 limits what steps 4 and 5 *settle and check*, and adds what *To do*
  gains. The rule in `SKILL.md:70-74` says exactly that. The opening of `task_document.md` is text the
  author added, listed in `reports/assessment.md:109` as a pointer. It says something wider: "write into
  the task document only what ... gives, of the items below".
- The mechanism: an agent on the route reads the rule, whose only sentence about *To do* is "the task's
  *To do* gains `guidelines/coding-<kind>.md` with its row in the index". "Gains" alone excludes nothing;
  "only ... of the items below" makes it exclusive. The presence of each item in the list below is what
  the opening cancels.
- Example: a product has nine unindexed endpoints. Step 3 compares them; step 4 settles the exemplar and
  one rule a script checks, with its invariant, "each with a test of the product's suite"
  (`settle.md:25-26`, `:37`). The agent writes *To do* from `task_document.md`: the file and the row. The
  item at `task_document.md:15-16` falls out. The kind file's rule then names an invariant "whose test
  checks the rule" (`template.md:102-103`), and no item of *To do* asks for that test; under WAY-61 the
  invariant reads `review` until a test cites it, so the rule a script was to check is checked by no
  script, and the review of the task, which compares with *To do*, has nothing to hold it to. *Context*
  (`task_document.md:34-38`) goes the same way: `kinds.md:15-16` makes the agent find each `do not copy`
  file with its file and line, and the cycle's author, who "reads only the task document", gets the
  status without the place. The route has no prior use (task *Context*), so nothing but this text
  decides what an agent does.
- The same form at `settle.md:3`: "settle only ... of the items below" covers the item **Critique**
  (`settle.md:47-49`), which is no matter to settle. The author's own counting has that critique run on
  this route (`reports/word-counts.md:314`), and WAY-120 sends a completed set through it, so the text
  should not leave that open.
- What the author's check missed: its weakest point was rule preservation by sentence comparison and a
  walk. A sentence comparison cannot see a new sentence that switches old sentences off, and its walk of
  route 6 (`author.md:117-119`) records that "steps 4 and 5 open with the pointer", not what the pointer
  leaves.
- Rule of the task: "Outside To do 9-13 no rule disappears". The route lies inside To do 9-13, but To do
  10 names the invariants as within it, so losing their test is not what To do 10 settles.
- Fix, for example at `task_document.md:3`: "On the route of one kind, take from the items below what
  concerns that kind, as "The route of one kind" in `SKILL.md` gives: its file with the index row, the
  test of each new invariant, its choices, and what the comparison found." `settle.md:3` likewise names
  what it limits ("of the choices and invariants below") so that the critique stands. `hand_back.md:3`
  fits To do 10 as it is ("check only").

### 2. The *Rationale* of WAY-216 holds a reason nobody gave, and it is false of a trial run (Important, within To do 13; new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/foundations/decisions.md:5969`
(lines 5969-5972)

**To paste:** "Research and a trial run answer a new scope" is the author's own reason for a decision the
human settled, and no source of the task gives it. It is also untrue of the trial run: a refresh covers
no new scope and still runs one (`recognize.md:25-26`). The reason should come from the row's source or
go.

**Why I report it:**

- What the sentence is for: the template has a changed decision's *Rationale* describe the decision as it
  then stands, and an agent reads it in a borderline case.
- The rule: WAY-29, binding sentence: "A rationale an agent proposes for a human's decision goes to the
  human as a question, never into the entry; the rationale of a decision an agent takes in a task is the
  agent's to write." Rows 1 and 2 are the human's ("Zostaję przy B", "Tak, przyjmuję"). The review of the
  whole change also checks "nothing the change takes from them altered or invented". The author says so
  itself: "The *Rationale* sentence is my wording (no source gives one)" (`author.md:174`, `:211`).
- Mechanism and values: the sentence pairs research and a trial run as both answering a new scope. For
  research that holds, and the foundation says so (WAY-211, WAY-251 rationales). For a trial run it does
  not. `recognize.md:25-26` gives "existing coding guidelines, refreshed or extended: step 2, and step 3,
  which tries the set", WAY-251 has a refresh stay "within the scope they already cover", and WAY-204
  prices the trial run as "each time a set is adopted". So the entry the change writes and the file the
  change writes disagree on when a trial run happens; an agent reasoning from the rationale in a
  borderline case would drop the trial run at a refresh. WAY-29 gives the danger itself: "a reason an
  agent writes looks exactly like a recorded one".
- Its last clause is sourced and can stay: "a task that is an extension for another reason keeps its
  research (WAY-211)" is row 1's own reason for rejecting the other wording.
- Fix: replace the first clause by what the rows keep: row 2's cost (without it every task creating a
  first file of a kind could pull research of all the standing checks) and question 3's (an agent on
  the comparison improvises and may make a full audit); say nothing of why a trial run exists.

## Minor findings

### 3. The assessment's order and verdicts are outside `judging.md`, and the author's report says otherwise (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/assessment.md:31`
(headings `:9`, `:31`, `:35`; rows `:61`, `:71`, `:73`; claim `author.md:22`)

**To paste:** `judging.md` gives check script, table, contradictions; the assessment has contradictions
before the table and numbers them so. Three rows read `SPLIT`, which is not one of its four verdicts.

**Why I report it:** `instruction-files/judging.md:11-26` gives the order and the closed list keep, move,
remove, reword. The handoff asked for both because a remark on the earlier skill's assessment found the
same two faults. `author.md:22` claims "sections in the order of `judging.md`", which is false. The
preface says a split "is written as the verdicts of its parts", and the rows do give those, but each
opens with `SPLIT`. Graded Minor because nothing is missing and a reader loses nothing but the promised
order. It would be the same remark a second time, so I recommend fixing it in the same round as findings
1 and 2: move "Contradictions" after the table and begin those rows with `MOVE` and `REWORD`.

### 4. The assessment says no mistake was found, yet the history it searched records one on the sentence To do 12 touches (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/assessment.md:81`
(and `:7`)

**To paste:** The row of `:187-196` says "Mistake: not found in the records searched", but commits
5a00041 and f34e477 record the correction that made "the audit covers every one of them" read as it does.

**Why I report it:** `:7` lists both commits as searched "by their messages". f34e477: "Revise C38: the
audit of step 3 covers every kind ... as WAY-201 (row 22) gives it with no exception. Remove the human's
option to defer a kind". `judging.md:22` names a commit as a place a mistake is seen, and the ground of a
row is what a human disputes. This sentence is the one the fifth mode has to pass by without weakening;
the row is the place to say what it was kept for. The change itself respects it: `kinds.md:5-9` keeps the
sentence and adds the one-kind case beside it. Fix: name the commits in the row and adjust `:7`.

### 5. The assessment refers to a check of paths the author's report does not hold (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/assessment.md:29`

**To paste:** "The paths named by the rebuilt files were checked by hand, see the author's report": the
report holds no such check.

**Why I report it:** `author.md` has no line on it (`grep -n "by hand\|paths"` finds only the part map at
`:146`). The claim happens to hold: I checked every path the eleven files name and each exists (checks
below). The request should say what was run, so drop the pointer or state the check.

### 6. Proposal P1 quotes one of the three places To do 8 names (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/assessment.md:115`

**To paste:** P1 quotes `:223-224` and only lists `:269` and `:63-69`, while saying "the lines are quoted
whole"; and it is marked RECOMMENDED without saying what lets it in.

**Why I report it:** the human decides P1 at the request and has only this row in front of them, and
line 269 is the sentence an agent actually meets at step 5. `judging.md:30-31` recommends a proposal
only where "When to add a rule" lets it in; the ground here is "a cost of misreading", with no mistake
found. The exception for a step of the activity probably applies (`instruction-files/SKILL.md:249-252`),
but the row should say so. P1's substance is right and stays a proposal, as the orchestrator's rule
gives.

### 7. The author's report carries figures from before its last edit (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/author.md:51`
(with `:10`, `:22`, `:59`, `:63-66`)

**To paste:** The report's table is 7 words low on every "after" figure; `word-counts.md` is right. Take
the request's figures from `word-counts.md`.

**Why I report it:** `author.md:10` gives `SKILL.md` 1499 words; `wc -w` at the head gives 1506, as
`word-counts.md` does. So route 1 reads 8613/11234 there and 8620/11241 in `word-counts.md`, and every
route alike; the change of the total is -25.1% at most, not -25.2%; the text grew by 747 words (4143
against 3396), not 740; and `:22` says 249 nonblank lines where the base has 247. `word-counts.md` was
regenerated after the last edit and the report's prose was not. Nothing tracked is affected; the risk is
only that a figure is copied from the report into the request.

### 8. The *Rejected* of WAY-216 is written about the change, not the decision (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/foundations/decisions.md:5974`
(lines 5974-5976)

**To paste:** "four modes of the coding-guidelines skill left as they were" holds a count and a state of
the process's own skill, which author-written prose of an entry leaves out.

**Why I report it:** the way itself is the source's (question 3, *Not chosen*), so it belongs in
*Rejected* (WAY-134). Its wording is the author's translation, so `elements/decisions/template.md:53-55`
applies: no count, nothing of what the process's own tools do or lack today, nothing of how the decision
was reached. Suggested wording: "no mode for the comparison in the coding-guidelines skill, the gap
described as a proposal — an agent on the comparison improvises and may make a full audit". Minor: it
binds nothing.

## Good, for keeping

- `recognize.md:21-24` turns To do 9 into a condition that selects exactly the task's case, and the choice
  at `SKILL.md:111-113` keeps `kinds.md` on a task that also creates a new kind.
- "A choice found in the product's files" and "Extend what exists" moved to the rules across steps, so
  they reach every route, "A new kind" included, which reads no file of step 3.
- The fragment `:197-199` no longer depends on "Where the product has code:".

## Declined to judge

- That the third sentence of WAY-216 answers a question of its own under WAY-19: rows 1-2 and To do 13
  order an edit in place, and the human settled the wording.
- The contradiction on "A new kind" with "each standing check": it stays a proposal by the task and the
  orchestrator's rule; only its row was judged (finding 6).
- Whether P2 should be taken: not recommended by the author and outside the task's outcome.
- The task's estimates against the counted figures (upper bounds of routes 3 and 4; "ca. 400 words"
  against 747): the author reports the differences and bent nothing; the human's choice was made on an
  estimate, which is for the human to weigh at the request.
- Whether counting route 6 "before" as an ordinary run of the base is the fairest reading: the task
  leaves it open, and the report states the reading beside the route.
- The duplicate maintenance of three `orchestrated_mode.md` files: settled by task question 2.

## Coverage

### To do

| # | Result | How checked |
|---|---|---|
| 1 | met, but see finding 1 for one added sentence | rows against files; shape against `testing/`, WAY-256 |
| 2 | met | each item of step 0 against `read_sources.md:3-5,17,28`, `reading.md:39-43`, `recognize.md:7-11`, `research.md:12`, `settle.md:47-49`; the critique files count 145+294+70=509 |
| 3 | met | `SKILL.md:101`, `:110`, `:112`, `:121-122` |
| 4 | met | `research.md` at `SKILL.md:103-104`, `new_tools.md` at `:123-124`, each with `starting_set.md`/`settle.md`'s condition. The critique skill is another skill, named in the introduction and at the two steps' files, as in the testing and styleguide skills |
| 5 | met | `SKILL.md:89-91` equals `testing/SKILL.md:79-81` word for word |
| 6 | met; findings 3, 4, 5 | see "Assessment" below |
| 7 | met in `word-counts.md`; finding 7 for `author.md` | see "Word counts" below |
| 8 | met; finding 6 | P1 and P2 at `assessment.md:115-118` |
| 9 | met | `recognize.md:21-24` against the wording of To do 9 |
| 10 | rule met at `SKILL.md:70-74`; finding 1 for the opening of `task_document.md` | |
| 11 | met | in "Rules that hold across the steps" |
| 12 | met | `trial_run.md`, `kinds.md`; the sentence at `kinds.md:6-9` beside "the audit covers every one of them" |
| 13 | met in the binding part; finding 2 and 8 in the prose | diff of `foundations/decisions.md`; no new entry |

### Acceptance criteria

| Criterion | Result |
|---|---|
| No rule lost or changed outside To do 9-13 | met: see "Rule preservation" |
| One kind reads `kinds.md`, not `starting_set.md`, `research.md`, `trial_run.md`; first guidelines, extension and refresh read `trial_run.md` and `kinds.md` as step 3 today | met: walk below |
| Reworded conditions add and lose no route; step 2 pointer names all conditions of `:141`, with "before the first code", and does not read as a kind without a file | met: `SKILL.md:99-102` |
| Each pointer recognisable by an agent reaching `SKILL.md` by its path | met: "beside this skill", step names, conditions in the agent's terms. No pointer rests on the entry point |
| Reviewer walks each route and compares each row with its place | done, below |
| "How to show" reaches step 2; "What reaches the task document" reaches steps 4 and 5; "Extend what exists" and `:200-202` reach every route | met: `SKILL.md:52-67`, `:122`, `:129`. Of "steps 1 and 3 say themselves what they add": step 1 does (`recognize.md:5-6`); step 3 writes nothing itself in the base either, see "Searches" |
| Linter documentation rule reaches the preference route | met: `starting_set.md:14-16` |
| Refresh sentence in `starting_set.md` | met: `:11-13` |
| "A new kind" reads neither `trial_run.md` nor `kinds.md` | met: the two conditions of `SKILL.md:108-113` do not hold on it |
| `:197-199` stays at step 3, its condition free of `:169` | met: `SKILL.md:115-117` |
| "Where the skill works" stays | met: `diff` of the lines is empty |
| `description` and Python unchanged, so the entry points too | met: `diff` of the frontmatter empty; no `.py`, `.claude` or `.agents` file in the range |
| Counts made after the last change; helper compares each figure | met: 346 figures at the head, summary table included (I read `tools/verify_counts.py`), and my own count agrees |

### Settlements to record

| Row | Result |
|---|---|
| 1 | written in WAY-216 in the wording of the task's *Context*, word for word; `narrows WAY-251` on WAY-216 only (WAY-18); WAY-251 untouched; three binding sentences (WAY-05). The binding sentence states the area where it prevails (WAY-25) |
| 2 | same sentence of WAY-216 |
| 3 | last sentence of WAY-266 removed. `git grep "not bound by it until"` finds it nowhere else. The *Verification* of WAY-266 needed no change |

### Assessment

Own script, independent of the author's: 56 rows; 247 nonblank lines of the base, each in exactly one
row, none missing, none twice; every quote equal to its lines; every permalink range equal to its stated
range. Each row's stated new place compared by hand with the files: all hold, ordinal places included
("first bullet", "second bullet", "last paragraph"). Row costs of 113, 69, 197, 249, 195 and 489 words
equal the files. The claim of `assessment.md:7` on the remarks: 0 mentions of the skill in PRs 50, 52, 59,
60 and 62, and PR 51 has no comments, as it says. The output of `check_instructions.py` it quotes equals
mine.

### Word counts

Own script over `reports/word-counts.md`: each file figure against `wc -w`-equal counts at the head (and
at f86fd71 for the base `SKILL.md`), the three sections by their headings, every sum, every figure without
the first reading and the summary table with its percentages: 371 figures, 0 differ. Each route's file
list matches the walk below. Before: 3391+3396+1336+2112+3391+54+322=14002, +509=14511.

### Rule preservation

Own comparison, sentence by sentence, whitespace normalised, list markers and headings dropped: of the
base's 157 sentence pieces 13 are not verbatim in the rebuilt files, the same places the author names.
By what each says:

| Base | Now | Same meaning? |
|---|---|---|
| `:49` "reads only the document" | `SKILL.md:50` "the task document" | yes |
| `:103-107` (four pieces) | pointers at steps 2-4, `research.md:12`, `settle.md:48-49`, step 0 | yes; the second reading goes as To do 2 accepts |
| `:108` | `recognize.md:7-8` | yes: `AGENTS.md` whole; the rest of `guidelines/` |
| `:109-112` | `recognize.md:8-11` | yes: only the added entries, as To do 2 lists them; the method of selecting was read at `refine-task` step 1 |
| `:148-150` (two pieces) | `starting_set.md:10-13` | yes |
| `:157-159` | `research.md:10-12` | yes: the file is read only where research ran |
| `:216-218` | `settle.md:6-7`, `new_tools.md:3` | yes |
| `:261-262` | `settle.md:47-49` | yes |
| `:268` | `hand_back.md:6` | yes |

Every other base sentence is verbatim. Every new sentence is in the assessment's list of added text. Of
these only the opening of `task_document.md` and `settle.md` changes what is selected (finding 1).

Reworded conditions, by what they select:

| Condition | Selects as the base? |
|---|---|
| Orchestrated mode, `SKILL.md:78-81` | yes; the added words are the first line of `project-level/task/skill/orchestrated_mode.md` |
| Step 2, `SKILL.md:99-102` | yes: no code, code without `guidelines/coding.md`, refresh, extension |
| Research, `SKILL.md:103-104` | yes, as `:148-149` |
| Step 3, both files, `SKILL.md:108-111` | yes: modes 2 and 4 of the base, where the product has code |
| Step 3, `kinds.md` alone, `SKILL.md:111-113` | the new route of To do 9, and nothing else |
| "A new kind", `SKILL.md:115-117` | yes, and now free of `:169` as the task asks |
| New tools, `SKILL.md:123-124`, `settle.md:6-7` | yes |
| Template at steps 3 and 4 | every route reads it before the first step that uses it, once |

### The walk

As an agent that reached `SKILL.md` by its path, having read `refine-task` steps 1 and 2. Each route
reads `SKILL.md` whole first. `new_tools.md` joins step 4 of any route where a new tool is left as a
question. "Not reached" names the base rules a route does not read; on all routes it is text of another
route's condition.

| Route | Files in order | Base rule not reached |
|---|---|---|
| 1 no code, no preference | `recognize.md`; `coding/template.md`, `starting_set.md`, `research.md`, critique `SKILL.md` with `prepare.md`, `check.md`, `settle.md`; step 3 conditions fail; `product-guidelines/template.md`, `settle.md`, `task_document.md`, way-of-working section "Critique before collective review"; `hand_back.md` | trial run and kinds (no code), as in the base |
| 2 no code, preference | as 1 without `research.md`; critique skill first at step 4 through `settle.md:49`. The documentation rule reaches it at `starting_set.md:14-16` | research, as the base by its condition |
| 3 code, no guidelines, no preference; extension | as 1, then `trial_run.md`, `kinds.md` at step 3, template not read again | none |
| 4 refresh | as 2, then `trial_run.md`, `kinds.md`; `starting_set.md:11-13` keeps research away | research, as the base |
| 5 "A new kind", guidelines stand | `recognize.md`; the paragraph at `SKILL.md:115-117`; `product-guidelines/template.md`, `coding/template.md`, `settle.md`, `task_document.md`, critique section and skill; `hand_back.md`. What a script can check of an exemplar comes from `template.md:170-171`, so `kinds.md` is not needed | steps 2 and 3's files, as the base by mode. Steps 4 and 5 still say "each standing check": P1, not a new gap |
| 6 one kind | `recognize.md`; `coding/template.md`, `kinds.md`; `product-guidelines/template.md`, `settle.md`, `task_document.md`, critique section and skill; `hand_back.md` | **the item of the invariant's test and *Context*, switched off by the opening of `task_document.md`: finding 1** |
| 7 orchestrated, route 1 | `orchestrated_mode.md` before step 1, then as 1 | as 1 |

WAY-210: step 1 names the parts first and finds what the product has after the reading, and the base read
everything before step 1, so the order is not turned around.

### Own-work check of the author

It named rule preservation, which fits where the change is weakest, and ran a real comparison and walk.
It would catch a lost sentence, not an added sentence that switches old ones off: finding 1 passed
through it.

### Other points of section 2

No reserved choice is settled. No test or invariant test changed, none was due: only Markdown. No trust
boundary and no operation that cannot be undone. No user interface.

## Checks

Scripts are mine, in `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/41f2056f-3658-4eef-997b-34fd0fc1aa7a/scratchpad/`.

| Command | Exit | Showed |
|---|---|---|
| `git rev-parse HEAD`, `git status --short` | 0 | head as given; empty |
| `git diff --stat f86fd71..097123e`; same for `project-level elements product-guidelines/template.md product-guidelines/coding/template.md` | 0 | 12 files; none of those outside |
| `git diff --check f86fd71..097123e` | 0 | clean |
| `python -B chk_assess.py <base SKILL.md> <cycle>/reports/assessment.md` | 0 | see "Assessment" |
| `wc -w` on each counted file; sections by heading; `git show f86fd71:` for the templates | 0 | 1506, 113, 403, 180, 197, 249, 195, 69, 629, 489, 113; 1336; 2112; 463; 2228; 322+145+294+70; 208, 492, 54 |
| `python -B chk_counts.py <cycle>/reports/word-counts.md` | 0 | 371 compared, 0 differ |
| `python -B <cycle>/tools/verify_counts.py <cycle>/reports/word-counts.md` | 0 | 346 figures, 0 differ |
| `python -B chk_sent.py` | 0 | 157 pieces, 13 not verbatim, 49 new pieces |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn, 3 info, equal to the base's saved output (`diff`, exit 0) |
| `diff` of base `:24-45` with `SKILL.md:25-46`; of the frontmatter | 0 | empty |
| shell loop over every path named by the eleven files | 0 | all exist; product paths left out |
| `git grep` for references to moved sections, WAY-216, "not bound by it until", "unindexed" | 0 | no broken reference; `reading.md:83-85`, `guideline_findings.md:33-35`, `plan/skill/SKILL.md:120-121` agree with the edit |
| `gh pr view <n> --comments` for 50, 51, 52, 59, 60, 62, with a count of mentions | 0 | 0 mentions; 51 empty |
| `git show -s f34e477 5a00041` | 0 | finding 4 |
| Manual: the walk, each row's place, each condition | | above |

Not run: the whole gate (the orchestrator's, by the handoff; I relied on nothing from its log), and
`skill_entry_points.py --write` and the gate's `agent-instructions` and `installation` directories
(writes or belongs to the gate; the frontmatter and the entry points are unchanged in the range).

## Foundation read

Selected by "Reading the foundation" for the parts `product-guidelines` and `decisions`: 140 decisions by
*Scope*, plus those the task names and the moved text cites.

Read whole (87): WAY-01, 05, 07, 08, 10, 11, 12, 14, 16, 17, 18, 19, 21, 22, 25, 28, 29, 30, 32, 33, 34,
35, 36, 37, 44, 51, 61, 100, 107, 113, 114, 120, 121, 122, 123, 124, 127, 128, 134, 150, 154, 155, 167,
168, 169, 170, 171, 172, 173, 174, 198-212, 213, 214, 215, 216, 217, 218, 219, 221, 225, 228, 231, 247,
248, 251, 256, 257, 259, 263, 265, 266, 267, 268. This holds every decision of *Decisions in play* and
every decision the moved text cites.

Selected and **not** read whole (65), which departs from the method's "each found whole"; I read their
headings and set them aside as about what the change does not touch — styleguide, testing, technology
places, other elements and the repository: WAY-02, 04, 09, 24, 26, 27, 52, 53, 54, 55, 60, 65, 71, 72, 73,
84, 85, 86, 90, 95, 97, 99, 102, 103, 104, 116, 117, 126, 137, 138, 165, 166, 176, 177, 178, 180, 182,
183, 184, 185, 186, 187, 189, 191, 192, 232-246, 249, 250, 252, 253, 254.

Part map: `decisions`, `product-guidelines`, whole. Invariants: the entries at `foundations/invariants.md:1-130`
whole; of the rest, `map-reference-target`, `skill-entry-points` and `instruction-file-imports` (*Part*
`every`) by name only. Glossary: `exemplar`, `standing check`; the headings of the rest. Guidelines
selection: empty (task question 8).

## Reaches beyond the dispatch

- `instruction-files/judging.md`, `instruction-files/kind_skill.md`, `instruction-files/SKILL.md` ("When
  to add a rule"): to judge the assessment.
- `elements/decisions/template.md:45-74`, `:95-204`, `:210-218`: to judge the entry.
- `task-cycle/skill/foundation_step.md`, `task-cycle/change/SKILL.md` (lines on invariants): what the
  cycle's author does with an entry and a test (findings 1, 2).
- `project-level/task/skill/read_sources.md`, `guideline_findings.md`, `orchestrated_mode.md` (first 40
  lines), `product-guidelines/reading.md`, `project-level/plan/skill/SKILL.md:115-125`: To do 2,
  callers, the wording of the orchestrated pointer.
- `product-guidelines/testing/SKILL.md`, `recognize.md`, `research.md`, `settle.md:49-51`,
  `styleguide/research.md`: the shape, and the wording of To do 5.
- `git show -s f34e477 5a00041`, `gh pr view` of six requests: to test the assessment's statement of the
  records.

## Searches not found or unclear

- **"Steps 1 and 3 say themselves what they add to the document" (acceptance criterion).** Step 3 adds
  nothing itself: neither base nor rebuilt step 3 writes into the document; it hands to step 4 ("The split
  goes to step 4 with its evidence"), and *Context* is written from `task_document.md` at step 4. The
  author read it this way (`author.md:202-204`). I take the criterion as describing the base, loosely,
  and find no gap: the evidence reaches the document on every route that makes it.
- **"The wider mode governs" (To do 9).** The fifth mode's own conditions exclude the modes it could lose
  to (it needs `guidelines/coding.md`, and neither a refresh nor an extension), so the clause bites only
  on a task that also creates a new kind, where neither mode is wider. The author ran both side by side,
  which I think right: `SKILL.md:111` reads `kinds.md` there and the paragraph of "A new kind" still holds.
  But `SKILL.md:71` then says "only what concerns that kind" with two kinds in play. No real case stands
  behind it; the task's wording is kept as ordered. Recommended answer if asked: both kinds are settled,
  the standing checks are not.
- **`author.md` on the WAY-216 *Rationale*:** flagged by the author as its own wording, which is what led
  to finding 2.
- No other instruction, handoff or task passage was unclear.
