PASS afa43439b39b66fc1e737897b0c6b8b0e11aa129

# Review of the whole change — unread-material

Range `02c3d47f8891b66507687b40665b323f3d20def8..afa43439b39b66fc1e737897b0c6b8b0e11aa129`
(`ca376a0` foundation entries, `afa4343` methods and template). `git rev-parse HEAD` in the worktree
printed `afa43439b39b66fc1e737897b0c6b8b0e11aa129`, the head given. Diff and log computed with
`git diff` and `git log` over that range; 10 files, 220 insertions, 49 deletions. Route: one author,
no plan, no spec. Reviewer: a fresh agent that made none of it. No tracked file was changed, no commit
made; `git status --short` was empty at the end.

Result: no Critical and no Important finding. Five Minor findings, all within the task. Nothing
blocks.

## Coverage of the task

*To do* 1 — the dopisek. Met. In `task-cycle/skill/SKILL.md:200-203`, straight after "add what it
found to the handoffs that follow." (line 199). Checked mechanically: the task's quoted sentence is a
substring of the file after whitespace is collapsed. The dropped last sentence of the older note
("A reviewer of the whole change that read only part...") is nowhere in the repository.

*To do* 2 — the fixed section. Met. **Unread material** stands before **Searches not found or
unclear** and apart from it in all five methods: `task-cycle/change/SKILL.md:137-138`,
`task-cycle/review/SKILL.md:149-154`, `task-cycle/plan/SKILL.md:198-202`,
`task-cycle/spec/design.md:71-73`, `task-cycle/spec/review.md:24-27`. In the orchestrator's skill the
paragraph of what a report holds (`SKILL.md:194-197`), the line of what is read at `done`/`PASS`
(`SKILL.md:197-199`), the repair rule (`SKILL.md:209-213`) and the executor's mechanical check
(`SKILL.md:309-314`) all carry it. `grep -rn "Searches not found" task-cycle` shows no remaining place
that lists a report's sections without the new one; the places left with only Searches are about the
process remarks (`SKILL.md:72`, `SKILL.md:483`, `record_template.md:185`, `remarks_check.py`).

*To do* 3 — the request item. Met. `task-cycle/skill/request_template.md:240-248`, item 14 of *For you
to decide*, carries the question "merge anyway?", the example shape of the task, and the condition of
the task (reviewer did not run through the rest by title, or itself named a decision of the change as
unread, and the gap was not closed on the way). The references by number I could find
(`task-cycle/skill/correction.md:48` item 8, `task-cycle/skill/SKILL.md:561` item 12) still point at the
right items. `request_check.py` names only the four top headings (`task-cycle/request_check.py:66`),
so no script change was needed.

*To do* 4 — WAY-150 and the carriers. Met. WAY-150 (`foundations/decisions.md:4209-4290`) carries the
screening in its binding sentence, *Verification*, *Rationale* and *Rejected*;
`task-cycle/review/SKILL.md:25-33` and `elements/common/way_of_working.md:82-89` carry it ("The whole
log is not read." became "The log beyond the decisions found is not read."). The screening is for
decisions only and no other agent skims, as the task and the handoff say; WAY-213 is untouched.

*Settlements to record*, each as an entry of its kind (all four are decisions):
- Row 1 — WAY-325 (new, `foundations/decisions.md:10552`). Meaning equal to the row; *Rejected:*
  `unknown`, which `elements/decisions/template.md:61-66` gives when the row's source keeps no way not
  chosen (the source of row 1 is point 1 of *To do*, which keeps none).
- Row 2 — WAY-326 (new, `:10584`). Meaning equal to the row. *Rejected:* the two ways of question 1 and
  the record of every agent's selection from the question's control question, all in its *Source*.
- Row 3 — WAY-150 edited in place. The three ways not chosen of question 3 are added under the template
  rule that a decision written from a row keeps the ways its source keeps; the existing ways stay.
- Row 4 — WAY-287 edited in place (`:9053-9114`): the new list item, its complies/violates, rationale,
  and the two ways of question 2 in *Rejected*.

Source fidelity: the words the task quotes are not altered (dopisek exact; example "40 of 151 ... merge
anyway?" kept). Nothing in the change is invented beyond the task except the section's name **Unread
material** (the task gives none) and the item's number 14; both are among the choices judged below.

## Points the orchestrator asked to be judged

1. Row 4 as an in-place edit of WAY-287. Agreed. WAY-19 says a new answer to a question the log holds
   rewrites that entry; WAY-287's binding sentence is the list of "everything whose merge needs the
   human's yes", so a third entry would leave that list false; the task's own row says the line
   "rozszerza listę WAY-287"; WAY-134 has a row already stated by a current entry tie to that entry.
2. Item numbered 14. Agreed. It stands in the same section among the other decisions, which is what
   question 2's answer asks ("pozycja sekcji ..., obok pominiętych kroków"); inserting it beside item 4
   would renumber items 5-13 and break the references by number named above. Cost if wrong: it is read
   last. Easy to move.
3. Three ways not chosen added to WAY-150's *Rejected*. Agreed. `elements/decisions/template.md:61-66`
   makes the ways not chosen that the row's source keeps part of a decision written from a row, each with
   its reason; the three come from question 3 with their reasons, none is derived by the author. The
   orchestrator's phrase "keep *Rejected* as the task's sources describe it" (author handoff, line 95)
   is met by that. The author's alternative reading (leave *Rejected* untouched) would leave the
   task's own "Not chosen" lines unrecorded.
4. "Closed on the way" meaning the reviewer or a fresh one read what stayed unread. Reasonable and
   coherent with WAY-325 (an autonomous choice that a gap bears on nothing judged does not fit a review
   that judges the whole change). But it is defined only in the template, not in the entry — see Minor 1.
5. Section name and order; the edge of `remarks_check.py`. Name and order agreed (with Unread first the
   section is never inside Searches in the forms the methods prescribe). The edge exists as the author
   describes; I reproduced it — see Minor 4.

## Findings

### Critical

none

### Important

none

### Minor (all within the task)

1. **"Closed on the way" is defined only in the template, not in the entry that binds it.**
   Place: `task-cycle/skill/request_template.md:240-248` against `foundations/decisions.md:9053-9059`
   (WAY-287's binding sentence, "and the gap was not closed on the way") and `:10552-10580` (WAY-325).
   What is wrong: the template narrows "closed" to "the reviewer or a fresh one reading what stayed
   unread"; WAY-287 says only "closed on the way", and WAY-325 gives the orchestrator a third way, an
   autonomous choice that the gap bears on nothing. A reader of the entries alone cannot tell whether
   that choice closes the gap for the request. Why it matters: a later reviewer comparing the template
   with the entries (WAY-263) or an orchestrator reading WAY-287 may put the item in or leave it out
   either way. Evidence: the three texts above. Suggested fix: one clause in WAY-287 saying a gap is
   closed on the way when the reviewer, or a fresh one, read what stayed unread.

2. **A title-screened decision is not said to be "no gap" where the orchestrator's rule is stated.**
   Place: `task-cycle/skill/SKILL.md:200-203` and `foundations/decisions.md:10552-10557` (WAY-325),
   `:10584-10590` (WAY-326), against `task-cycle/review/SKILL.md:149-154`. What is wrong: WAY-325 fires
   on a report that says something "stayed unread or was read in part"; the whole-change reviewer's
   section always opens with counts such as "40 whole, 111 by title only". Only the review method
   says what the section lists (decisions not run through, bearing decisions unread, guideline files),
   i.e. that a decision read by title is the practice and not a gap. WAY-287's rationale says so
   (`:9092-9099`), but WAY-325/326 and the orchestrator's sentence do not. Why it matters: an
   orchestrator reading the counts as "read in part" must decide (resume, carry, or record a choice) at
   every whole-change review, which is the cost the task set out to avoid. Evidence: the quoted places.
   Suggested fix: one clause in WAY-326 (or in the `SKILL.md` sentence) that a decision read by title
   under WAY-150 is no gap.

3. **The exception for a report returning `questions` was extended to the new section without being
   in the entry.**
   Place: `task-cycle/skill/SKILL.md:209-213` ("A report that lacks its **Unread material** (WAY-326) or
   its **Searches not found or unclear** (WAY-260), save one returning `questions`...") against
   `foundations/decisions.md:10586-10592` (WAY-326: "a report without it returns to its agent for
   repair"). What is wrong: the skill states the repair rule with a qualification the entry does not
   have. The same difference already holds between this sentence and WAY-260, so the author followed
   the existing shape, and the effect is benign (a `questions` report is resumed anyway), which is why
   it is Minor and not a WAY-263 Important; but the author's report does not name it as a choice.
   Suggested fix: say in WAY-326 that a report returning `questions` is not returned for the section, or
   drop the exception for the new section.

4. **Reverse order leaks an Unread line into the process remarks; the tests cover only the prescribed
   order.**
   Place: `task-cycle/remarks_check.py:16-23` (end of a bold-label section) and
   `task-cycle/test_remarks_check.py:143-165` (the two new tests). What is wrong: when a report writes
   **Searches not found or unclear** as a bold label outside a list and then **Unread material** as a
   list item (not as bold text starting a paragraph), the Unread line is read as an item of Searches.
   Reproduced (scratch run, `remarks_check.section_items`): `**Searches...:**\n\n- item one\n\n-
   **Unread material:** the file` gives `['item one', '**Unread material:** the file']`; the same with
   a `none` bold label followed by the Unread bullet gives `['**Unread material:** the file']`. The
   forms with Unread first, with a heading, with a bold label (not a list item) after Searches, and with
   the Searches label as a list item are all read correctly. Why it matters: WAY-326's *Verification*
   calls the gap standing among WAY-260's items a violation; the leak is limited to a report that breaks
   the order the methods give, so the author's recommendation (leave it, let a real listing decide) is
   reasonable. Suggested: add a test that records the reverse-order behaviour, or end the section at a
   bold label named `Unread material` as the author proposes.

5. **Long unwrapped lines and one clumsy sentence left by the edits.**
   Place: `foundations/decisions.md:4226` (159 characters; WAY-150, the sentence that joins "of the
   cycle reads what its handoff names and reaches for what is missing selectively — a search for an
   identifier or a word and a read of the passage found,"), `foundations/decisions.md:9059` (135
   characters, WAY-287), `task-cycle/skill/SKILL.md:213` (151 characters, "section is not. An agent
   that returns `questions` gets your answers as step 6 answers the designer's — ..."), and
   `elements/common/way_of_working.md:82-83` ("Read each decision found whole, save as the reviewer of
   the whole change reads them below, as the range of lines from its heading..." reads awkwardly: two
   "as" clauses). The files are wrapped near 100 characters elsewhere. Evidence: `awk 'length>100'` on
   the added lines; no test checks line length. Suggested: re-wrap the three lines and split the
   way_of_working sentence.

## Declined to judge

- A guidelines file the whole-change reviewer read in part reaches the orchestrator through WAY-325 but
  not the request (item 14 speaks of decisions only): that is the task's own wording of point 3, so I
  set it aside.
- Unread parts of the dispatch-named material of the whole-change reviewer other than its own selection
  (the frozen task, the author's report): WAY-326 and the task restrict the section to the reviewer's
  own selection.
- The screening for the orchestrator, task refinement, project definition and plan: the task's *Out of
  scope*.
- The measure of how many selected decisions bear on a change: the task's *Out of scope*.
- The guideline gaps of the-way itself (no `guidelines/` directory): a task of its own
  (`the task about the-way's own guidelines`), per the handoff and question 4 of the task.

## Checks I ran

All from the worktree `the task's worktree`.

- `git rev-parse HEAD` — `afa43439b39b66fc1e737897b0c6b8b0e11aa129`, equal to the given head.
- `git diff --check 02c3d47f8891b66507687b40665b323f3d20def8..HEAD` — exit 0 (no whitespace errors).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
- `python -B elements/common/foundation_check.py` (without the switch) — exit 0, "0 errors".
- `python -B gate/run_tests.py task-cycle` — exit 0, 234 tests OK.
- `python -B gate/run_tests.py elements/common` — exit 0, 117 tests OK.
- `python -B gate/run_tests.py instruction-files` — exit 0, 104 tests OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK.
- `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` — exit 0, "0 listed".
- Manual: the dopisek compared with the task's text by a whitespace-collapsing substring test (Python,
  `-B`), true; the dropped last sentence searched across `task-cycle`, `elements`, `foundations`, not
  found.
- Manual: scratch run of `remarks_check.section_items` on six report forms (Python `-B -I`, run from
  `task-cycle`, no file written): results in Minor 4.
- Manual: `grep -rn "Searches not found" task-cycle` against `grep -rln "Unread material"` for the
  places that list a report's sections; `grep` of the repository for restatements of WAY-150's reading
  ("whole log", "each entry whole", "selects for its own review") — no restatement was left saying the
  reviewer reads every selected entry whole.
- Not run: the full gate (`python -B gate/run_tests.py` without a directory), which is the cycle's own
  run. The author's two added tests are characterization tests that passed first time; I judged by
  reading that they fail if the script began reading an Unread line placed before Searches as an item
  (Minor 4 covers what they leave out); I did not mutate the script.

## Reaches beyond the handoff

- `.runs/task-cycles/unread-material/reports/author_handoff.md:60-130` — to judge the orchestrator's
  point 3 ("keep *Rejected* as the task's sources describe it") and what the author was told about
  rows 1, 2 and 4.
- `elements/decisions/template.md:37-80, 210-233` — the rule on *Rejected* of a decision written from a
  row, on prose in *Rationale*, and on `unknown`; to judge the *Rejected* of the four entries.
- `task-cycle/skill/SKILL.md:160-220, 300-315` and greps for item numbers (`correction.md:48`,
  `SKILL.md:505, 561`), and `task-cycle/request_check.py:66` — to check that the new item breaks no
  reference by number.
- `product-guidelines/reading.md:1-40` — the handoff's selection of guidelines; this repository has
  no `guidelines/` directory.
- `task-cycle/remarks_check.py:1-40` and a scratch run of its `section_items` — to reproduce the edge.
- Decisions opened beyond the topic list because their title points to the change's bearing: WAY-113
  (how an agent asks a human decision), WAY-124 (when a task is ready), WAY-288, WAY-290, WAY-291,
  WAY-292 (the request description's language, form check and block), WAY-306 (the review of the merge
  of the target branch, which cites WAY-150), WAY-318 (artifacts in the request), WAY-134 (rows to
  entries), WAY-05, WAY-30, WAY-12 (how decisions are written, changed and checked).
  They are of my own selection; counted below.

## Unread material

Decisions of my selection: 162 (found by a search of `foundations/decisions.md` for the three parts the
change touches, `task-cycle`, `elements-common` and `decisions`, in *Scope*: the files changed lie in
`task-cycle/**`, `elements/common/**` and `foundations/decisions.md`; the 160 the author had plus the
two the change writes). I ran my search with a small script and did not cross-check it against a second
method.

- **Read whole: 45.** WAY-05, WAY-07, WAY-11, WAY-12, WAY-19, WAY-30, WAY-33, WAY-113, WAY-114, WAY-124,
  WAY-125, WAY-134, WAY-136, WAY-148, WAY-150, WAY-158, WAY-159, WAY-161, WAY-162, WAY-163, WAY-164,
  WAY-213, WAY-227, WAY-255, WAY-260, WAY-261, WAY-262, WAY-263, WAY-286, WAY-287, WAY-288, WAY-289,
  WAY-290, WAY-291, WAY-292, WAY-294, WAY-295, WAY-296, WAY-297, WAY-298, WAY-300, WAY-306, WAY-318,
  WAY-325, WAY-326.
- **By title only: 117** (the other decisions of the selection). I went through all 162 titles in one
  list, so no decision of the selection was left without a run through by title.
- Decisions that bear on the change and stayed unread: none that I know of. Titles that I judged not to
  bear and did not open include WAY-21 (scope), WAY-35 (what an element's skill holds), WAY-135
  (when a cycle writes a spec), WAY-256 (where a fragment of a skill stands), WAY-293 (what prevails
  where a task excludes an entry), WAY-307 (a spec whose review fails). A decision with an unremarkable
  title could have passed unopened, which is the price WAY-150 now names.
- Invariants: the invariants file was read whole (356 lines), with the 33 entries; those whose *Part*
  names `every`, `task-cycle` or `decisions` were checked against the change. The two touching the
  change are `tracked-file-private-paths` (the gate test in `task-cycle` passed) and
  `record-copy-image-files` (no image file in the range). No invariant test is changed by the range.
- Part map: the entries of `decisions`, `elements-common` and `task-cycle` read whole (lines 7-100 of
  `foundations/part_map.md`; the file read to line 135, the rest not).
- Glossary: read whole (179 lines). None of its entries is a term the change uses in a new meaning;
  "orchestrator", "handoff", "report" and "unread" are not glossary words, and I found no sentence of
  the change a reader would read wrongly for lack of an entry.
- Guideline files: none. This repository has no `guidelines/` directory (the author's report names it
  too); nothing to read whole.
- Not read whole beyond the selection: `task-cycle/skill/SKILL.md` (read lines 160-220 and the diff
  hunks, plus lines found by grep), `elements/decisions/template.md` (lines 37-80 and 210-233).

The author's own gap carried to me (65 of 160 whole, 94 by title, no glossary, WAY-82 in part) is
closed by the above as far as my selection reaches: I read the glossary and the decisions of the
report cycle (WAY-148, 150, 159, 213, 260, 286, 287 and the two new ones) and every other decision
whose title points at reports, handoffs, the request description or reading that I found in the
list. I found no contradiction between the change and those decisions beyond Minor 1-3.

## Searches not found or unclear

- The task cites `task-cycle/skill/SKILL.md:191-193`, `:193` and WAY-150 at line 4060; they have
  moved (the handoff says so). Found by content.
- The author's report quotes "keep *Rejected* as the task's sources describe it, which stands" as
  *To do* point 4 of the task; the phrase is in the orchestrator's author handoff
  (`author_handoff.md:95`), not in the task. The author's reading (add the task's "Not chosen" ways,
  keep the old ones) is the reading I accepted, but the phrase is unclear: "which stands" could also mean
  "leave *Rejected* alone".
- Where "closed on the way" is defined: not in the task, not in WAY-287, only in the template item
  (Minor 1).
- Whether a decision read by title counts as "read in part" for WAY-325: not stated where the
  orchestrator's rule stands (Minor 2).
- A test or check that the five methods hold **Unread material** before **Searches not found or
  unclear**: not found (the grep for the name in the test files returns only `test_remarks_check.py`).
  Nothing guards the sections mechanically; the orchestrator's repair rule is the only guard.
