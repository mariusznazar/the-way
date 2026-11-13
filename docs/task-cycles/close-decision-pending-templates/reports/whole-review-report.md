PASS 2c27260d68a571a0c0d6dafbdad645957f7388cb

# Review of the whole change — close-decision-pending-templates

Range `fca8491..2c27260` (one commit, one author, no plan). `git rev-parse HEAD` in the worktree is `2c27260d68a571a0c0d6dafbdad645957f7388cb`, the head given. Diff computed with `git diff fca8491..2c27260` and `git log fca8491..2c27260`.

Result: 0 blocking findings, 3 Minor within the task, 1 Minor out of scope.

## Against the task

- Every `TODO — decision pending` line is gone except S26 (`elements/environment-facts/template.md:130`) and S28 (`elements/invariants/template.md:82`). `git grep` on the head shows exactly those two. 30 of 32 markers removed, as the task counts (23 lines of S1-S19, plus S20-S25 and S27, one each).
- `foundations/decisions.md` and every other file of `foundations/` are unchanged (`git diff --name-only` lists only the seven `elements/` files).
- Items 2, 3, 4, 6, 7, 8, 9 of *To do* match the task's words. Item 2's text is word for word the task's. Item 3 reads as the task gives it, with the reference to step 4.1 gone. Item 4 keeps "today" and drops "in the present tense" (S21). Item 6 removes the sentence with nothing in its place (S23). Item 7 keeps the `Files: none` rule as plain text (S24). Item 8 removes the whole Draft blockquote; the file now opens with "This file defines how an invariant entry is written." (S25). Item 9's sentence rests on WAY-72 and WAY-99 and says what the task says (S27).
- S13-S19 are plain text with the rule's sense unchanged; S16 in both files, S17 (edition a citation names), S18 (descriptive source), S19 (edition a sentence names) match the line each had.
- The only change of sense among S1-S19 is the S5 ending, as the task allows. Nothing else in the diff changes the sense of a rule. Lines that were reflowed (WAY-02, WAY-17, WAY-33, WAY-80, WAY-82 mentions) keep their words.
- Settlements to record: none, no foundation entry written, none needed.
- Pins: none moved.

## Citations, one by one (task item 1)

I read each decision whole. "Confirmed" means the decision supports the sentence the citation sits on.

| Case | Place (head) | Decision text | Verdict |
|---|---|---|---|
| S1 (WAY-05) x4 | env-facts :170, glossary :102, invariants :165, part-map :168 | WAY-05 holds the sentence word for word, though its scope is the decision template (*Scope: decisions*). WAY-54 already cites WAY-05 for the same rule about templates generally. | Confirmed (the task's choice; see Declined to judge) |
| S2 (WAY-64) | invariants :22-23 | WAY-64's *complies* example: "an entry taking in a clause of another keeps its identifier, and the other is split". | Confirmed |
| S3 (WAY-61) | invariants :59-60 | WAY-61 supports "a test is written in the product's language, of the product's suite". "A Markdown file holds no citing test" is not in WAY-61; it is in WAY-321 and in the invariant `test-method-citation`. | Confirmed for the first clause; see Minor 1 |
| S4 (WAY-44) | invariants :94 (`whether a check belongs to the product is settled by the part map (WAY-44)`) | WAY-44: every file git tracks belongs to exactly one part, or the map lists it as left out on purpose. So the map is the authority on where a tracked check stands. It does not say "belongs to the product" in those words. | Confirmed on a reading; the weakest of the confirmed citations. Left as written. |
| S5 (WAY-62, WAY-22) | invariants :144-145 | WAY-62: an entry names the parts where a change can make its sentence false, or `every`; WAY-22: an invariant is a rule a commit can make false. Together they support "a sentence no commit of this product can make false is not an invariant of this product". | Confirmed. The ending's removal is the task's. |
| S6 (WAY-73) | env-facts :57 | WAY-73 "and no other fact"; WAY-76 *Rejected* uses the same case, a fact about a test's tool that "no commit changes". | Confirmed |
| S7 (WAY-90; WAY-73 not added) | env-facts :64 | WAY-90 *Rejected*: "the partners of the part map's external context as linked facts — a new link with no known consumer", and its text: a fact only for a citation that would call a decision into question. This is the sentence it sits on. WAY-73 would add only "a fact stands only while a decision's *Based on* names it", which the sentence already carries in its wording. | Confirmed; leaving WAY-73 out is acceptable, nothing is misstated |
| S8 (WAY-48, WAY-44, WAY-41) | part-map :19-20 | WAY-48 speaks of "the external context"; WAY-44 of "the map lists that file as left out on purpose"; WAY-41 of withdrawn identifiers. Each stands at its own list. | Confirmed |
| S9 (WAY-48) | part-map :148-149 | WAY-48: a boundary is recorded at the part; an exchange with the external context records direction and untrusted input. It does not say a row names no part and no file. | See Minor 2 |
| S10 (WAY-22, WAY-29) | decide_entry.md :12 | WAY-29: rationale of a recovered decision is "given by a human who knows them"; WAY-22: a rule that records a choice is a decision. | Confirmed |
| S11 (WAY-28 only, WAY-44 not added) | missing_element_file.md :8 | WAY-28: "The part map comes first". WAY-44 says every tracked file has a part; it does not set an order of writing. WAY-44 is already cited one line above. | Confirmed with plain text; the task allows the review to replace a doubtful citation, and the sentence is carried by WAY-28 |
| S12 (WAY-71) | way_of_working.md :129-131 | `rules.md:19` says a silent source reads `TODO`, "not a blank" (WAY-71); WAY-71's violation list holds `Based on: none` where the source is silent. "Asked about before anything is written" stays plain text, as the task says. | Confirmed |
| Item 5 (WAY-71) | env-facts :91-93 | WAY-71 gives the forms `TODO — <the fact, with its source>` for *Rests on* and `TODO — <what is missing, with its source>` for *Based on*, and "a change that leaves one there puts it before the human". | See Minor 3 |

## Findings

### Critical, Important
none.

### Minor, within the task

1. `elements/invariants/template.md:59-60` — S3. The citation `(WAY-61)` follows "A test stands in a file of code; a Markdown file holds no citing test". WAY-61 says a test is of the product's suite in the product's language; it does not exclude Markdown. WAY-321 does ("a file git tracks other than Markdown") and is already cited at `:52` of this file. A reader who opens WAY-61 for the second clause does not find it. Citing `(WAY-61, WAY-321)` would carry both clauses. The sentence is not wrong, and the task chose WAY-61; this is the author's concern C3.
2. `elements/part-map/template.md:148-149` — S9. "A row names no part and no file (WAY-48)" is followed in the next sentence by "... at the part that handles the exchange (WAY-48)". The second cite is exact. The first attributes to WAY-48 something it does not say (that a row names neither part nor file); it is a reading of "a boundary is recorded at the part" and of the row's three columns. The task asked for WAY-48 here and gave no medium-confidence flag, so the author followed it; the effect is a citation a reader cannot confirm. Either leave only the second cite or keep both and accept the inference. Two `(WAY-48)` in two adjacent sentences also reads as repetition.
3. `elements/environment-facts/template.md:91-93` — item 5. "An entry that would stand on a missing fact takes `TODO — <the fact, with its source>` in its field" sits in the *Source* section of a template for fact entries, where "an entry" otherwise means a fact entry (line 38: *Source* "takes neither `none` nor `TODO`"). A fact entry never stands on a fact; the entry meant is an invariant (*Rests on*) or a decision (*Based on*), and WAY-71 gives the decision a different form (`TODO — <what is missing, with its source>`). A reader of this template may look for the field in a fact entry and not find it. The task's own wording ("wpis, który stałby na brakującym fakcie") has the same shape, so this is a polish: name "an invariant's *Rests on*" and keep the form as WAY-71 gives it. This is the author's concern C6.

### Minor, outside the task

4. `elements/invariants/skill/decide_entry.md:12` — the sentence "one the human gives is written as a decision" is a rule of entries stated in a skill; WAY-35 puts rules of entries in the template or `rules.md`. It was there before the change, and the change only closes its marker. Author's concern C7; named here as outside the task.

## Declined to judge

- The removal of the S5 ending ("it belongs to the foundation of the product whose commits decide it") — the task orders it. Noted only that WAY-34's verification still speaks of invariants that "belong to each product's foundation, since no commit of the-way decides them"; the statement stays true in the decision log and no file the change leaves says otherwise.
- WAY-05's scope is the decision template (WAY-71's *Rejected* says WAY-05 "answers how a decision entry is written"). The task chose WAY-05 for the four "fields and their readers" sentences, and an earlier decision (WAY-54, *Rejected*) already cites WAY-05 for the same rule about templates in general; set aside.
- The author's note about `return-step-record`: its method is `review` and its sentence opens "Where {merge-onto} exists"; the-way has no main branch today, and the record is the cycle's return step, not the author's task. Set aside.
- Structure of code: no code file is changed, so no growth, no unused code, no name that stopped being true (WAY-362). The product has no coding guidelines for the-way's own files in this checkout, so any structure finding would be Minor in any case (WAY-363).

## Checks run

| Command (from the worktree root) | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `2c27260d68a5...` |
| `git diff fca8491..2c27260 --stat`, `--name-only`, `git log fca8491..2c27260 --oneline` | 0 |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0, "0 errors" |
| `python -B task-cycle/change_file_sizes.py fca8491 2c27260` | 0; 7 files, lines 908 -> 858, every file shorter |
| `python -B gate/run_tests.py elements/common` | 0, "Ran 144 tests ... OK" |
| `python -B gate/run_tests.py elements/invariants`, `elements/glossary`, `elements/environment-facts` | 1 each, "no test found in ..."; the three directories hold no test, so nothing ran |
| `git grep "decision pending"` on the head | 2 lines, S26 and S28 |
| `git grep -i "draft template\|does not reach the main\|ahead of the decisions\|finding it is a task\|in the present tense\|a decision's to make"` on the head, excluding `.runs` | no hit in a file the change should have updated (two hits in `foundations/decisions.md` are other uses of "present tense") |
| a script of my own printing whole decision entries by number (`WAY-44, 28, 90, 73, 22, 29, 61, 62, 48, 41, 71, 64, 72, 99, 05, 113, 76, 82, 02, 17, 40, 34, 321`) from `foundations/decisions.md` | 0 |

Not run: `gate/run_tests.py` whole (the orchestrator's). The structure test of the invariant of size (WAY-361) was not run: the change touches Markdown only and the checkout holds no rule `### Size of a function and a file` that I looked for beyond `product-guidelines/` pointers; the numbers above and the diff are my material.

The `ls guidelines` / `grep` run for the coding guidelines exited 2 (no `guidelines/` directory in the the-way checkout).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-34 (verification passage about invariants belonging to a product's foundation), WAY-40, WAY-321, WAY-54 and the WAY-05 mentions by `grep -n WAY-05` — to judge S3, S5, S9 and S1.
- `foundations/invariants.md` entries `element-directory-contents`, `skill-rule-source`, `map-reference-target`, `test-method-citation`, `derived-file-content`, `outbound-link-reach`, `tracked-file-private-paths`, `return-step-record` — the invariants of the touched parts and the ones that bear on a change of templates.
- `foundations/part_map.md` entries `decisions`, `part-map`, `environment-facts`, `elements-common` — the parts the change touches.
- `elements/common/rules.md` lines 13-23 through `grep` — what the bare `TODO` and `none` rule says (the handoff named the file as unread by the author).
- `elements/part-map/template.md:118-170`, `elements/common/way_of_working.md:1-60`, `elements/environment-facts/template.md:84-126` — read to see the sentences in their place.

## Unread material

- Decisions of the selection: 23 read whole (WAY-02, 05, 17, 22, 28, 29, 34 in its verification passage only, 40, 41, 44, 48, 61, 62, 64, 71, 72, 73, 76, 82, 90, 99, 113, 321, and WAY-54's *Rejected* line); 0 skimmed by title as a screening pass. I did not run through the other decisions by title; the selection was by citation and by `git grep` for the changed phrases, which found no decision those phrases contradict. Of 323 decisions, I did not read WAY-33, WAY-35, WAY-36, WAY-76-related WAY-77/78/80, WAY-114 and WAY-150 whole, though some bear on sentences reflowed in this change (WAY-80, WAY-33); I judged the reflowed lines by their words, which the diff shows unchanged.
- Invariants read whole: the eight named above. The other entries of `foundations/invariants.md` of the touched parts were not read.
- Part map: the four entries above read whole; the entries `invariants` and `glossary` were not read.
- `foundations/glossary.md` entries: not read.
- Guidelines: the-way's own checkout holds none for these files that I found; `product-guidelines/*` were not read.
- `elements/common/rules.md` was read by `grep` lines only, not whole. `elements/common/projected_mode.md` and the templates' `examples.md` files: not read; the changed sentences are not about projected mode or examples.
- `elements/decisions/template.md`: read only through `grep` lines (its `WAY-05` sentence and `TODO` rules).

## Searches not found or unclear

- A guideline of the-way that sets a rule of size for these files: not found (`grep` of `product-guidelines/` finds only the instructions for writing one).
- Whether the cycle expects the return step's record from the author's commit: not stated in the handoff; the invariant `return-step-record` does not apply while the-way has no main branch. Unclear, not blocking.
- Whether WAY-05, scoped to decisions, is meant to bear on the "Fields and their readers" line of the other four templates: the task says so and WAY-54 does the same in a *Rejected* line; no entry says so as a rule. Unclear, not blocking.
