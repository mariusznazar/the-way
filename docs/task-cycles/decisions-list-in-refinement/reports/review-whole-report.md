FAIL 51f25908c6b1cb7bc95bc8e3fd1859d1d76acfa3

# Review of the whole change — decisions-list-in-refinement

Range `9cbc6b2..51f2590` (one commit), `git rev-parse HEAD` = `51f2590`. Task read whole:
`.runs/task-cycles/decisions-list-in-refinement/task.md`. No spec, no plan, no slice review.

Counts: blocking 1, Minor 5 (all within the task), out of scope 0.

## Findings

### Important (blocking, within the task)

**I1. The quotation check of the skill does not reach the matters the critique calls settled, though WAY-378's own example requires it.**

- Place: `project-level/task/skill/final_review.md:28-31` (step 3 "Verdicts": "For each matter you will show, open the file the critique quotes from and check the quotation word for word") against `foundations/decisions.md`, WAY-378 *Verification*, "complies" ("the refining agent opens the file the critic quotes from, sees that the quotation of one of the 6 does not say what the critic claims, and counts that guess open; it shows the human 3 matters") and *Rationale* ("A critic can call a matter settled while the first agent was right or the reverse, so the refining agent opens the file the critique quotes before it shows a matter").
- What is wrong: in the example, the guess whose quotation fails is one of the 6 the critic had judged *already settled in the repository*. Under step 3 of the skill the agent checks only "matters you will show"; a guess the critic calls settled or most likely right is not shown, so it is never opened. The example of the entry cannot happen under the skill's text. The two disagree on what the check covers.
- Why it matters: the task's own reason for the check (question 2, *Not chosen*: "krytyka mogła uznać sprawę za trafioną, choć agent się mylił, dlatego ... agent doprecyzowania sprawdza cytaty krytyki") is exactly this case: a wrong "settled" verdict hides a real open matter from the human. As the skill is worded, the check protects only against a wrong "open" verdict, which costs the human nothing but a matter shown. WAY-378's *Rationale* names the price ("a matter the critic judged settled ... and the refining agent did not re-check stays out of the human's sight"), so the entry allows the re-check, and the example shows it; the skill forbids it by omission. Graded by WAY-263 (the change's files fail to do what the entry's example shows).
- Evidence: reading of the two texts side by side; the skill's words "For each matter you will show" in step 3 and in `orchestrated_mode.md:31-32` ("check the critique's quotations as `final_review.md` gives").
- Note on the task: To do 5 says "przy każdej sprawie, którą pokaże" literally, so the skill follows the task's item; the task's own *Not chosen* of question 2 and WAY-378's example point the other way. The human's decision is which way; the change must make the skill and WAY-378 say the same. Either widen step 3 to the quotations behind every guess the critique judges settled or most likely right (cost: more files opened, bounded by the list), or change WAY-378's example to a quotation behind a matter that is shown. I recommend the first; it is what the *Not chosen* asks for.

### Minor (all within the task)

**M1. Wrong subject in the orchestrated bullet.** `project-level/task/skill/orchestrated_mode.md:30-31`: "The project orchestrator writes the *List* and the *Critique* ... and ends your turn with `questions`." Read as written, the orchestrator ends the refiner's turn; WAY-154 and the bullets around it say the refiner ends its own turn ("you end the turn"; "`questions` carries the run"). Write "you end your turn with `questions`" before the orchestrator's writing, or split the sentence.

**M2. The request does not carry the method to the project orchestrator.** `orchestrated_mode.md:25-34` is addressed to the refiner. The *Child-work request* it tells the refiner to write names "the list and then the critique", the task document and the file, but not that the orchestrator takes the method from `final_review.md` steps 1 and 2, nor the inputs and class that WAY-377 binds (the first agent gets the document and the full entries and nothing of the conversation; both agents on a class cheaper than the refiner's). No file of `project-level/lead/` says anything of this request type (the author's report says so); `lead/skill/SKILL.md` 3.1 only says "You perform all child dispatches their borrowed workflows request". An orchestrator that hands the list agent the conversation path (WAY-154's habit) or runs it on its own class breaks WAY-377. Cheapest fix within the task: the bullet tells the refiner to name `final_review.md` steps 1 and 2 and the class in the request. A pointer file in `project-level/lead/` like `technology_run.md` would be outside the task's *To do* and is not required by me.

**M3. WAY-100's "what it leaves out of the practice" has no line in WAY-377.** `foundations/decisions.md`, WAY-377 *Rejected* holds only the three ways of the task, as WAY-134 allows for a decision written from a row; WAY-100 asks a decision that adopts an outside practice to put what it leaves out in *Rejected*. The *Rationale* says what is taken (the list and the mark) and that the rest is the-way's own, which covers "what is taken", not "what is left out" (the card D8 in the author's notes also names a count of how many guesses the human would settle otherwise, which the entry does not take). Not blocking: the row's source keeps no such way and WAY-134 forbids inventing one; `unknown`/a sentence in *Rationale* of what is left out would close it. Judged as the author asked (point 4): the pair of two decisions is right (the two questions change independently); the *Rejected* matches the task's *Not chosen* word for word in meaning (checked item by item).

**M4. "steps 4 and 5 of the skill" inside a numbered list of five steps.** `final_review.md:38-40` (step 5 "Answers") ends "enters the document as steps 4 and 5 of the skill give", copied from To do 6. Inside a list whose own steps 4 and 5 are "Show" and "Answers" it can be read as the list's own steps. Write "sections 4 and 5 of `SKILL.md`".

**M5. The new sentence of `SKILL.md` is not wrapped like its neighbours.** `project-level/task/skill/SKILL.md:64` is 107 characters, the rest of the file wraps at 100. The sentence itself is one sentence next to the check of the complete document, as To do 8 asks. No check reports it.

(Also seen, not a finding: the condition of the step stands in four places — `SKILL.md`, `final_review.md`, WAY-377 and the task row; today they say the same, "`Decisions in play` is not `none` or the task changes a skill or an instruction file", so no drift now.)

## The points the orchestrator put to me

1. **A guess the critique finds most likely wrong is a gap of the document and is shown.** Defensible and within the task's words ("luki samego dokumentu"): an executor would take the wrong answer. WAY-378's binding sentence and example have no "most likely wrong" case; the rule lives only in `final_review.md` step 4. Not a finding; if I1 is fixed, a sentence in WAY-378 *Rationale* would keep entry and skill together.
2. **A quotation that does not hold voids the critique's verdict on that matter.** Consistent with WAY-378's example ("counts that guess open"). Sound. See I1 for what the check reaches.
3. **File name and writers.** `.runs/decisions-list/<task-name>.md`, one file, three parts; manual mode: the refining agent writes; orchestrated: orchestrator writes *List* and *Critique*, refiner *Verdicts*. Consistent between `final_review.md:7-9` and `orchestrated_mode.md:29-33`; matches the `.runs/project-refinement/<task-name>.md` naming of WAY-154 and the conversation file's `<task-name>`. The task fixes only "a file in the ignored `.runs/`". Fine; the sentence with the wrong subject is M1.
4. **Two decisions and WAY-377's *Rejected*.** See M3. WAY-377 / WAY-378 are two answers (when and by whom; what the human sees), the second `derives from` the first, the first `derives from WAY-100` like WAY-374. Numbers 377 and 378 free on every local ref (checked with `git grep` on all refs). Meaning sentences of the author's table match the rows.
5. **Condition and contradictions outside.** The three skill files and WAY-377 say the same condition. `project-level/lead/skill/SKILL.md` 3.1 ("refiners ... launch no children"), `lead/answering.md`, `lead/conversation_template.md` ("Child-work requests: ... delegated work") and `project-level/task/template.md` (`none` marks an empty *Decisions in play*) do not contradict the new text; the lead has no pointer to the method (M2). `resolve_gaps.md:64` ("start no agent") remains true for the orchestrated step that resolves the gaps.

Also checked: *Out of scope* kept (`resolve_gaps.md`, WAY-374 and WAY-113 untouched; no "strongest argument" rule); no use of "gate" in the added text (grep of the added lines: none) and none of the glossary's other terms in another meaning; no absolute path, `[[` link in the added lines (grep: none). Every To do 1-8 has its sentence; both rows of *Settlements to record* are written as WAY-377 (row 1) and WAY-378 (row 2); *Verification* by a pair of examples holds both, as WAY-12 gives; no invariant test was changed.

## Declined to judge

- The pointer file for the lead (`project-level/lead/`) — outside the task's *To do*; mentioned only as the alternative in M2.
- Whether the first agent's list of "visible only in a model file" decisions needs a place in what the human sees — the task does not give them one; no finding.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 9cbc6b2c46837c956f863843de0dd0bc3d32d8f1 51f2590`, exit 0: `foundations/decisions.md` 9616 -> 9719 (+103), `project-level/task/skill/SKILL.md` 63 -> 65, `final_review.md` 31 -> 70, `orchestrated_mode.md` 75 -> 85. Only Markdown; the-way holds no `guidelines/coding.md` and so no test of the size rule. No code, no function, no name that stopped being true. `final_review.md` now opens with two paragraphs that both begin "When the draft is complete" (the author's choice 3); no finding.

## Checks I ran

- `python -B elements/common/foundation_check.py` — "0 errors", exit 0.
- `python -B instruction-files/check_instructions.py .` — 0 error, 0 warn, 3 info, exit 0.
- `python -B task-cycle/change_file_sizes.py <base> 51f2590` — exit 0.
- `python -B elements/common/decision_index.py --output .runs/review-whole/index.md ...` (sections, parts `project-level` and `decisions`, decisions WAY-377, 378, 374, 120, 113, 100, 229, 134, 124, 154) — exit 0 (and `--sections`, exit 0).
- `python -B gate/run_tests.py project-level` — 278 tests OK, exit 0 (about 207 s).
- `git grep` of `### WAY-377` to `### WAY-379` over every local ref — only this branch holds them.
- Grep of the added lines for absolute paths, `[[`, "gate" — no hit.
- Not run: the whole gate (forbidden); no test of behaviour exists for prose, and none could fail on these texts.

## Reaches beyond the dispatch

- `project-level/lead/skill/SKILL.md` (sections 2-3), `project-level/lead/answering.md` (lines 28-60), `project-level/lead/conversation_template.md` (lines 95-125), `project-level/lead/skill/technology_run.md` — to see whether the orchestrator is told how to run the new request (M2).
- `project-level/task/template.md` (*Decisions in play* lines 74-100, 186-200) — the empty marker `none` of the condition.
- `foundations/glossary.md` headings — "gate" and the other terms.
- `foundations/invariants.md` entries `tracked-file-private-paths`, `skill-rule-source` (whole), and the *Part* lines of the others.
- WAY-17, WAY-02 (the links an entry needs), by their own entries.
- the author's notes on the AI Tech Leaders course, card D8 (lines 684-705) — what the practice holds, for M3.

## Working copies

`.runs/review-whole/` (the index of my selection `index.md` and the list `sections.md`): inside the reviewed worktree, ignored by git; removed before return (see the last line of this report). No worktree made.

## Unread material

Decisions of the index of my selection read whole: 11 (WAY-377, WAY-378, WAY-374, WAY-100, WAY-120, WAY-113, WAY-124, WAY-134, WAY-154, WAY-229, WAY-99). The others of the index (63 listed in full, 62 by heading alone) I read by their binding sentences and, for the headings, by their questions; none bears on the change beyond those named, but I did not open whole: WAY-95 (glossary words: judged by the glossary headings instead), WAY-114, WAY-313/314/315, WAY-155, WAY-267 (technology run, the model the bullet follows, read by its sentence), WAY-35, WAY-256 (the layout of a skill, read by its sentence), WAY-12 and WAY-05 (the form of an entry: read by their sentences and against the entries' form). No guidelines file (the-way holds none). Invariants: of the entries whose *Part* is `every`, `project-level` or `decisions` I read two whole and the *Part* lines of the rest, not each; the part-map entries of `project-level` and `decisions` read whole. `instruction-files/changing.md`, `writing.md`, `judging.md`, `tool_loading.md`, `kind_skill.md`, `placing.md`: not read; the change touches skills of the process, not files a tool loads, and `check_instructions.py` passed.

## Searches not found or unclear

- A pointer in `project-level/lead/` to this request type: not found (M2).
- A test that holds a sentence of WAY-374, WAY-377 or WAY-378 by `decision:`: none; not needed (pair of examples).
- Whether WAY-100's "what it leaves out" can be written from a row's source that keeps no such way: unclear (M3).
Removed: .runs/review-whole/ (index.md, sections.md) at the end of the review.
