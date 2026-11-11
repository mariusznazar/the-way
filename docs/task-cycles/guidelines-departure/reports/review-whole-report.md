PASS 7442841890655820eaeb6862519430b87c20d648

# Review of the whole change — guidelines-departure

Range `e3825a8..7442841` (`git rev-parse HEAD` = `7442841890655820eaeb6862519430b87c20d648`, matches the handoff; `git log` shows one commit; worktree clean). One file changed: `foundations/decisions.md`, +47 lines, entry WAY-327 at lines 10628-10673, between WAY-326 and *Withdrawn identifiers*. No code, test, user interface or skill is touched, so there is no guideline of the product to compare (the-way has none, which is what WAY-327 records).

Counts: blocking 0 · Minor within the task 4 · out of scope 1.

## Task coverage

*To do* item 1 — "the decision log has a decision that departs from the general coding guidelines and the testing guidelines for the-way itself, with no time limit, whose *Scope* names all 16 parts": met.

- Departure from both disciplines: binding sentence 1, "departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217". The styleguide is excluded in the *Rationale* and in a *violates* example, as the task's *Out of scope* asks.
- No time limit: no binding sentence names a stage (the template forbids one, so the decision holds until a change withdraws it), and the *Rationale* says it outright.
- *Scope*: I compared it myself with `foundations/part_map.md` lines 7-175 (the 16 `##` sections with a **Files:** line; the sections from line 177 on are surfaces and not parts). The same 16 identifiers, same order as the task's list: decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines.

*Settlements to record*, row 1 (departure, no time limit, 16 parts, tests included, withdrawn by a separate task if own guidelines come to pay): held, with one part placed in prose (Minor 3).

Row 2 (a change that adds a part to the map adds it to the *Scope*): held by binding sentence 2 and by both *Verification* examples. One entry for both rows is sound: row 2 only keeps the *Scope* of row 1 true and answers no independent question (`elements/decisions/skill/decide_entry.md`: "keep the question the rest serves"). The decision's *Scope* names `part-map`, so a later change to the map selects it by the reading of the foundation, which is what makes the sentence reachable. Its not-chosen way is missing from *Rejected* (Minor 1).

Source fidelity: the three *Rejected* ways follow the task's *Not chosen* (own guidelines; the rule saying it excludes the-way; nine parts only), with the counts and file names the template forbids removed and the costs kept. Nothing was added that the task does not give; I found no invented value. *Based on: none* and *Origin: none* are right (a human's answer is the decider's motive, not an outside source; the task document is private).

## Against the foundation and the template

- Form (`elements/decisions/template.md`): two binding sentences, present tense, no *should*, *will*, capitals or RFC words; all fields present; entry at the end of the log; the question names a choice. `foundation_check.py` reports 0 errors.
- Against WAY-215 and WAY-217: WAY-215 begins "Unless a departure under WAY-217 applies", and `product-guidelines/reading.md` applies a departure "only to the parts and work it expressly covers", so no `narrows` is needed and none collides. `derives from WAY-217 · derives from WAY-173` is right (WAY-173: a departure is a decision of the product's log that gives the reason).
- WAY-208/WAY-209/WAY-244/WAY-246 are proposals of the guidelines skills for a product; WAY-327 collides with none of them.
- Nothing else in the foundation answers the question in passing (searched `depart`, `own guidelines`, `no guidelines`, `the-way's own` in `foundations/` and `guidelines` in `agent-instructions/` and `foundations/invariants.md`; positive control: `agent-instructions/README.md` exists and the same search finds the known departures in WAY-173, WAY-217 and WAY-310).

## Findings

### Blocking

None.

### Minor (within the task)

1. `foundations/decisions.md:10663-10673` (*Rejected*). Row 2's *Source* keeps a way not chosen — a decision with no sentence that adds a new part to the *Scope* ("bez tego zdania pierwszy skrypt w nowej części znów stawia pytanie o brak wytycznych"). The template says *Rejected* of a decision written from a row holds the ways not chosen that the row's source keeps, each with its cost. The author's report says it entered "only the three ways the task keeps in its *Not chosen*" and so took the way from question 2 (nine parts only) but not the one in row 2's *Source*. The third *Rejected* way has a nearly equal cost, but a reader who later wants to drop binding sentence 2 finds no record that it was weighed. Fix: one more clause in *Rejected*.
2. `foundations/decisions.md:10653-10664` (*Rationale*). WAY-173 says a product departs only by a decision "that gives the reason". The *Rationale* opens with "the reason for the departure lies in the-way as a whole" and never says what the reason is. The only trace of it is the cost of the way not chosen in *Rejected* (a large task of its own, with the gain lying mostly in code that already exists). A reader of the *Rationale* cannot tell why the-way departs. I considered Important, since WAY-173 asks for it; Minor because the content is in the entry, only in the wrong place and unlabelled. Fix: one sentence in the *Rationale* saying why own guidelines do not pay now, taken from the task's *Not chosen* (a).
3. `foundations/decisions.md:10663-10664` (*Rationale*, last sentence: "If guidelines of the-way's own come to pay, a separate task writes them and withdraws or narrows this decision"). It is row 1's own clause (the task: a separate task writes them and withdraws the decision). WAY-05 puts "what a decision forces on later work" in a binding sentence or a field, never in prose. As written, nothing binding says what happens to the departure once a part gets guidelines of its own. Fix: move it to a binding sentence, or drop it as a prediction (the template already makes every decision hold until a change withdraws it).
4. `foundations/decisions.md:10658` — the *Rationale* wraps on a one-line stub ("on record. Recorded once in the log, the") and the next lines are re-flowed at a different width from the rest of the paragraph. Cosmetic; re-wrap the paragraph.

### Out of scope

5. WAY-216 gives a task that creates the first file of a kind of code absent from the general coding index the duty to designate an exemplar and write kind guidelines "with their index row". Binding sentence 1 releases only "the general coding guidelines and the testing guidelines", and the-way has no `guidelines/coding.md` to hold an index. Whether a first file of a new kind in the-way is released from that duty is not answered by WAY-327 or by `product-guidelines/reading.md` (which says "the general file must still exist unless ... a departure applies" and nothing about kinds). The task does not ask for it, so it is not a defect of this change; it is a question the next task that adds a kind of code in the-way will meet. Cost if left: the question returns once, at that task.

## Declined to judge

- Whether to add an invariant plus test that every part of the map is in the *Scope* of WAY-327 (the author's concern): the task asks for none, and it would need code. Left as the author's follow-up suggestion.
- The gate (`gate/run_tests.py`): the orchestrator runs it, per the handoff.
- Whether the decision is the right one (the human chose it); I judged only fidelity and form.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` (from the worktree root) | 0 ("0 errors") |
| Range and head | `git rev-parse HEAD`; `git log --oneline e3825a8..7442841`; `git status --short` | 0 each; head matches, one commit, worktree clean |
| Diff | `git diff e3825a8..7442841` | 0; only `foundations/decisions.md`, +47 |
| Selection of decisions (scratch script in the session scratchpad, read-only) | `python -I .../scratchpad/sel.py` | 0; 285 entries, 79 name `decisions` |
| Scope against part map | manual: `foundations/part_map.md` lines 7-175 against the *Scope* line | 16 = 16, same identifiers |
| Binding-sentence words | manual reading: no should, will, capitals, exclamation marks | none found |

Not run: the product's gate (orchestrator's), any test (the change holds no code).

## Reaches beyond the dispatch

- `elements/common/way_of_working.md`, `elements/decisions/template.md`, `elements/common/rules.md`, `elements/decisions/skill/decide_entry.md`, `elements/decisions/examples.md` — read whole (the template and WAY-134 decide the form of an entry written from a row).
- `product-guidelines/reading.md` — read whole, to judge how a departure is applied.
- `foundations/part_map.md` lines 1-180 — to check the 16 parts.
- Search of `foundations/` and `agent-instructions/` for existing answers or collisions (above).
- `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md` — the method.
- `.runs/task-cycles/guidelines-departure/task.md` and `reports/author-report.md` — read whole.

## Unread material

Selection. The handoff names part `decisions`. But WAY-44 and step 1 of "Reading the foundation" say that for a file collecting entries about many parts the parts touched follow from the entries written, and WAY-327 names all 16 parts. By that rule the selection is almost the whole log, which I did not read. I selected by topic instead: the decisions on the form of a decision, the numbering and scope of decisions, the departure from guidelines, the discipline guidelines and their timing, and the reading of guidelines.

Counts of decisions of my selection: **21 read whole, 7 read in part, about 257 by title only** (of the 285 entries of the log, which I screened by title and by a keyword filter on each entry's binding paragraph: 165 lines in the filter output, among them every decision of `decisions` or about guidelines).

- Read whole: WAY-03, 05, 07, 08, 19, 21, 44, 173, 208, 209, 213, 214, 215, 216, 217, 218, 244, 245, 246, 326, 327.
- Read in part: WAY-25 (to the *Rationale*), WAY-134 (binding sentences and the start of *Verification*), WAY-174 (binding sentences and the start of *Verification*), WAY-210 (binding sentences and the start of *Verification*), WAY-219 and WAY-247 (binding sentences and the start of *Verification*).
- Decisions that bear on the change and stayed unread (title only): WAY-30, 33 (the author's search of the foundation), 114, 150, 202, 263, 310, 315. I judged from titles and from what the template cites of them that none changes the verdict.
- Part-map entries: read lines 1-180 whole (all 16 parts).
- Invariants: not read; searched `foundations/invariants.md` for `guidelines`, no match (positive control above applies to the method, not this file; the file exists, 356 lines).
- Glossary entries: not read; the entry uses `departure` in the plain sense of WAY-217 and WAY-173.
- Guideline files: none exist in the-way (no `guidelines/` directory); nothing to read.
- `foundations/environment_facts.md`: not read; WAY-327 has *Based on: none*.

## Searches not found or unclear

- Not found: a `guidelines/` directory; any decision before WAY-327 that departs from guidelines for the-way itself (matches the task's *Context*).
- Not found: any statement in `agent-instructions/` about guidelines (no match; the README defines the integration route only).
- Unclear: whether the handoff's "part `decisions`" or the WAY-44 rule (all 16 parts) is the intended selection; I took the second and report the cost above.
- Unclear: out-of-scope finding 5 (kinds of code under WAY-216).
