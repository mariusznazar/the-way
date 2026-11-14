FAIL 306a122959b3d2e72d76ad3a2d01a2bd1655f9b4

# Review of the 24 decisions the review of the whole change left unopened

Range `ac753401de0bfaae0b9b8175c10c17387736f8d8..306a122959b3d2e72d76ad3a2d01a2bd1655f9b4`; `git rev-parse HEAD` is the head. Method: `task-cycle/review/SKILL.md`, as the reader of what stayed unread.

Two things about the worktree while I read. (1) It holds two uncommitted edits, by a corrector, not part of my range: `foundations/decisions.md` (WAY-241 *Rationale*, WAY-168 to WAY-173) and `product-guidelines/testing/template.md:229` (the same citation). I read every decision from `git show HEAD:foundations/decisions.md` and checked that the working file differs from it in WAY-241 only; WAY-241 at the head still cites WAY-168 (the earlier finding m1, settled, not repeated). (2) The range holds the content of three tasks merged in from the target branch (the installer junction refusal, the size of plan tasks, the own measurement in a decision: for example WAY-90, WAY-364's parenthesis, `installation/install.py`, `invariants.md`'s `installation-paths-through-links`). I judged only what this task wrote or changed; I touched nothing of the merged tasks beyond reading.

## Blocking findings (Important, within the task)

### I1. `README.md:84-88` and `agent-instructions/README.md:14-17` restate WAY-12 and WAY-03 without their qualification (WAY-263)

- Place: `README.md:84-88`: "It reports as an error each decision that a change adds or rewords and that nothing holds, and it lists, without failing, the other decisions that nothing holds and each invariant whose sentence a change rewords while no file citing it changes." `agent-instructions/README.md:14-17` says the same of "the decisions that nothing holds" and "the invariants whose sentence a change rewords while no file citing them changes".
- What is wrong: WAY-12 (written by the change) says the error stands for "a decision that a change adds, or whose binding sentences the change alters"; a change that rewords only *Rationale* or *Rejected* is *listed*, not an error (the script's `check_held`, test `test_decision_with_only_its_rationale_changed_is_listed`). "Rewords" of a decision, with no "binding sentences", reads as any reword, so the README says an error where the script and the entry say a listing. WAY-03 (written by the change) lists an invariant "whose method is `test`"; the README leaves that out. The script's own docstring (`elements/common/foundation_check.py:11-55`) and `elements/invariants/template.md:170` carry both qualifications; only the two READMEs drop them.
- Why it matters: WAY-263 and `task-cycle/review/SKILL.md` section 3 grade as Important a file that restates an entry the change writes or changes "more broadly or without a qualification". A reader of the README learns that rewording a rationale stops the gate.
- Settle: in both files write "each decision that a change adds or whose binding sentences it alters" and "each invariant that reads `test` whose sentence a change rewords while no file citing it changes". Two small edits, no entry changes.

### I2. WAY-03's binding sentence names a test that holds a decision's sentence; the request template and WAY-03's own *Verification* name only a changed line `decision:`

- Place: `foundations/decisions.md:83` (WAY-03), first paragraph: "A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request". Against it: `task-cycle/skill/request_template.md:303-305` and `:455-457` ("each test whose line `decision:` the change adds, drops or alters"), and WAY-03's *Verification* ("a change that adds, drops or alters the line `decision:` of a test names that test").
- What is wrong: the binding sentence makes the altered test the subject, as it does for an invariant test. The template and the *Verification* make the changed line the subject. A change that weakens the body of a test that holds a sentence of a decision, and leaves its line `decision:` as it was, is named by the sentence and by no other place; that is the weakening WAY-03 exists to show (its own source, `impossiblebench-test-modification`). The template and the *Verification* restate the entry differently in the sense of WAY-263 (narrower here).
- Why it matters: the request omits the altered test that the human merging is meant to see.
- Settle (a question for the orchestrator, below): widen the two lines of the request template and the *Verification* clause to "each test that holds a sentence of a decision by a line `decision:` that the change alters, adds or drops" (the entry's sentence stays, no human acceptance needed); or, if the human meant the line only, narrow the binding sentence (a change of a binding sentence: it goes to the human through WAY-30). I recommend the first.

## Minor findings (within the task)

### m1. `elements/common/test_foundation_check.py:1436` holds a sentence of WAY-03 that the test does not check

`# decision: WAY-03 "A change whose check lists such an invariant"` stands over `test_reworded_sentence_with_its_citing_file_changed_is_not_listed`. The sentence is "A change whose check lists such an invariant names it in its request in plain words, …", which is about the request; the test shows only that a changed citing file is not listed. WAY-03's *Verification* says the same: `tests:` "which invariants the check lists for a reworded sentence, and that the listing stops no change", and leaves the naming in the request "to the part no test holds". The line makes the script's check read the quotation as held. The previous review judged the test to hold "the case of the changed citing file"; that case is the sentence "The check of the foundation lists an invariant whose method…", already quoted at the other tests. Settle: change the quotation at line 1436 to that sentence (it is still a sentence start) or drop the line; the decision stays held by the others.

### m2. `elements/decisions/template.md:151`, question 5 says "in whole or in part … it becomes a sentence of that entry" without the qualification of WAY-19

WAY-19 (changed by the change) says a part of the question an existing entry answers is a sentence of that entry "where it cannot change without changing that entry"; "a part that can change on its own is a question of its own with its own number" (the same template, section "Changing a decision", gives it). Question 5 drops that, and so does the row value `sentence of <PREFIX-NN>` in `project-level/task/template.md`. The question ends with a pointer to "Changing a decision", which carries the qualification, so a reader who follows it reads it right; I grade Minor for that reason (the same drop in a README with no pointer is I1). Settle: add "where it cannot change without changing that entry" after "in part" in the question.

### m3. Three discipline templates tell the author to stop at a blocked draft request for a choice the task did not settle, citing WAY-172, which now sends a rule with no decision to the merge

- Place: `product-guidelines/coding/template.md:348-349`, `product-guidelines/styleguide/template.md:182-183`, `product-guidelines/testing/template.md:273-274` ("A choice the task did not settle is a question that stops the cycle at a blocked draft request, never a rule, a row or a field (WAY-172)").
- What: WAY-172 (changed by the change) now says that a rule that only says how to write, found by the cycle, is written by it and accepted at the merge, and lists as violating "a cycle stops on a blocked draft request for a rule that only says how to write". The three lines say "a choice … never a rule" without the limit "that carries a choice with a real cost". A reader of one template meets the old rule. The spec's non-goals leave the discipline templates unchanged, so this is a gap the spec made, not one the maker made. WAY-173 says a decision of the-way on what a template carries binds that template.
- Settle (question for the orchestrator): add the limit to the three lines ("a choice with a real cost the task did not settle"), or leave them and put the overlap before the human at the request, as the human decides on edits outside the spec.

### m4. `elements/common/foundation_check.py:751` (`list_invariants`): an invariant that lacked *Method* or *Part* at the base is dropped with no word (WAY-344)

WAY-344: a script that reads a file checks each field it needs and does not read an absence as an empty value; a script whose purpose is to check form lists a missing field. For the working tree the missing field is reported by the existing check of fields (tested). For the copy at the base, a missing *Method* or *Part* makes the invariant a non-candidate and nothing is written (`test_reworded_invariant_lacking_method_or_part_at_base_adds_no_listing` asserts only `["0 errors"]`). The spec (D9) chose it, and a file at a base cannot be mended, so the cost is small, but WAY-344 gives that exception only to the count of the audit. Settle: write one `listed:` line naming the invariant and the missing field, as the line for an unknown base, or record the choice in the request among those the cycle made.

### m5. WAY-287's enumerated list and the heading of kind 7 do not name what the change adds to the section

WAY-287 lists "the changed invariant tests, surfaces and *Violated* marks" and "the foundation entries the human did not see at the task document". The change puts into kind 7 of `task-cycle/skill/request_template.md` (headed *Changed invariant tests, surfaces and Violated marks*) an invariant listed for a corrected sentence and tests with a changed line `decision:`, and into kind 6 a guidelines rule with no decision, which is no foundation entry. WAY-287's first words ("everything whose merge needs the human's yes") and its group *You accept by merging* cover them, so nothing contradicts; but the list and the heading read narrower than the section. Settle: the heading of kind 7 may name the new items; WAY-287's list stays (changing it is a change of a binding sentence, for the human).

## Outside the task (not blocking, one finding)

### o1. WAY-150's selection does not take in the decision a test holds by a line `decision:`

WAY-150 adds to the selection "the invariants a test the work alters cites". The change introduces the line `decision:` and WAY-03 asks a request to name an altered test that holds a decision's sentence, but WAY-150 does not add "the decisions a test the work alters holds". A reviewer or author altering such a test is not led to the decision whose sentence it holds, except through the line itself. The task changes neither WAY-150 nor the way an agent reads the log (the human names it as the next task, `reports/correction-1-remarks.md` item 2). Out of scope; for that task.

## Declined to judge

- The switch `--skip-test-citations` (WAY-321): the cycle's ruling stands; I only checked that no sentence of WAY-321 or WAY-61 contradicts it (it does not: `check_held` and `list_invariants` stand outside the `if not skip_test_citations`, `foundation_check.py` docstring and `way_of_working.md:147-150` agree with WAY-321).
- The unknown base written only where the log holds a decision (WAY-38 "never agreement"): the cycle's ruling stands; WAY-38's sentence is about the commands a product declares, which git is not.
- The wording of the five questions and the choice of "Goes to" in place of "Kind": rulings of the task and spec.
- The content of the three merged-in tasks.

## The 24 decisions, each read whole (rationale and *Rejected* included) at `HEAD`

WAY-344 read whole as well (handoff). Bearing on the change, one line each:

- WAY-25: whole. None. The change records no new precedence (WAY-172 and WAY-293 narrow what they narrowed before); its two attached paragraphs add no `narrows`.
- WAY-30: whole. None to the code. The thirteen edits and the fix's edits to WAY-17 and WAY-115 stand in the request's items 7 and 8, as the entry asks.
- WAY-38: whole. None. Script on the standard library; git only (`git show`, `merge-base`, `rev-parse`, `diff`); unknown base reported, never agreement, where the log holds a decision. See Declined.
- WAY-61: whole. None. No invariant is written by the change; the method of `test-method-citation` is held (the script reports it, the run on the repository gives `0 errors`). The tests of the new sentences are about the check they exercise, as the entry allows.
- WAY-113: whole. None. The questions asked against a choice at refinement are not touched by `task_variant.md`'s edit.
- WAY-124: whole. None. A row that goes outside the log stays a settlement the human accepts before the task is ready.
- WAY-126: whole. None. The five questions are not applied to projected entries (`foundation_step.md`, `return_step.md` route "a row and a choice", not a projected entry).
- WAY-150: whole. Finding o1 (outside the task); otherwise none: the unread-material counts and the selection rules are not touched.
- WAY-161: whole. None. The request template keeps the lists the entry gives.
- WAY-169: whole. Bearing: m3 (the guidelines templates that name WAY-172); the rules of guidelines that name the changed entries WAY-168, WAY-171, WAY-172 in `product-guidelines/template.md` are in line. No product guideline file exists in the-way.
- WAY-170: whole. None. `check_guidelines` reads *Applies to* and *Invariant* only, never *Decision*, so `Decision: none` raises nothing; the template says so.
- WAY-173: whole. None. The edited template keeps "a rule of a template of the-way binds a product only through a decision of the product's log that adopts it (WAY-173)"; `Decision: none` stays for a rule of the product's own.
- WAY-174: whole. None. The skills of guidelines are unchanged; a rule with no decision comes through a row.
- WAY-213: whole. None.
- WAY-235: whole. None. It narrows WAY-168 in the area of trust boundaries; WAY-168 still holds the sentence on an invariant only where a cheap test checks a convention, so the precedence stays meaningful.
- WAY-241: whole. Stale citation of WAY-168 (m1 of the earlier review, settled, uncommitted fix in the worktree); otherwise none.
- WAY-263: whole. Findings I1, I2 and m2 are graded by it.
- WAY-268: whole. None. The choices of the cycle stay in the questions table; `return_step.md` keeps that sentence.
- WAY-286: whole. None. Skeleton unchanged; kinds 6 and 7 only gain sentences.
- WAY-287: whole. m5.
- WAY-290: whole. None. `request_check.py` is unchanged and reads headings and groups only, which the change does not alter.
- WAY-315: whole. None. The decisions the spec departed from in a first reading (WAY-115) were brought to the human through the fix and the request (item 8), not decided in the spec.
- WAY-321: whole. None to the contrary; see Declined. The skill sentence in `elements/decisions/skill/SKILL.md:34-43` names the switch, and the request template tells the description writer to run the script without it.
- WAY-364: whole. None. The finding grades above follow it: m1 to m5 are form or wording departures where the content agrees with the code; I1 and I2 cite a sentence a reader reads wrongly.
- WAY-344: whole (read for WAY-38). m4. The tests give an entry without *Verification* (`test_entry_lacking_its_verification_is_left_to_the_check_of_fields`) and an invariant without *Method* or *Part* now; the script is a check of form, so a finding with exit code 1 is the form the entry asks.

## Checks run

- `python -B elements/common/foundation_check.py` in the worktree: exit 0, output `0 errors`, no `listed:` line.
- `python -B -m unittest elements.common.test_foundation_check`: exit 0, 180 tests OK (180 s, run in the background and finished before I returned).
- Manual: `git show HEAD:foundations/decisions.md` compared by heading with the working file: differs in WAY-241 only. Entries changed in the range, found by comparing normalised text at the base and the head: 38 headings, 16 with a changed binding part (WAY-02, 03, 05, 11, 12, 17, 19, 22, 90, 115, 134, 146, 168, 171, 172, 293); WAY-90, 146 and the others outside the task's list came from the merged tasks.
- Not run: the gate and the full suite (not mine); `installation` tests (not touched by this task's own change).

## Reaches beyond the dispatch

- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` whole and `reports/correction-1-remarks.md`, `reports/return-review-report.md` (parts): to know the rulings and what was settled.
- `foundations/decisions.md`, WAY-12, WAY-03, WAY-168, WAY-02, WAY-17, WAY-115, WAY-19, WAY-22, WAY-293, WAY-171, WAY-172, WAY-134, WAY-11 and WAY-05 by comparison of the base and the head, for the entries the change wrote; for the bearing of the 24 on them.
- `product-guidelines/{coding,styleguide,testing}/template.md` and `settle.md` (searched for WAY-168, 171, 172 and "no decision", the passages read): for WAY-169, WAY-172, WAY-173, m3.
- `elements/common/way_of_working.md:135-160`, `elements/common/foundation_check.py` (the diff and `check_guidelines`), `elements/common/test_foundation_check.py` (test list and the lines `decision:`), `README.md`, `agent-instructions/README.md`, `elements/decisions/template.md` and `skill/*.md`, `task-cycle/skill/{request_template,return_step,foundation_step}.md`, `task-cycle/record_template.md`, `project-level/task/template.md`, `product-guidelines/template.md`: the diff of the range.

## Questions for the orchestrator

1. I2: widen the request template and WAY-03's *Verification* to the altered test (my recommendation), or narrow WAY-03's binding sentence to the line (a binding-sentence change, for the human)?
2. m3: the three discipline templates are outside the spec (non-goal). Bring them in line in this request, or put the overlap before the human?
3. m4: write a `listed:` line for a base copy that lacks *Method* or *Part*, or record the choice in the request?

## Unread material

- Of the 24 decisions of the handoff: none; each read whole at the head. Counts: 24 read whole (WAY-344 as well), 0 by title only.
- The earlier reports (`whole-review-report.md`, `fix-review-report.md`, `return-review-report.md`, `merge-review-report.md`): read by search and in the parts that name the 24 decisions, README, WAY-172 and WAY-344, not whole (the handoff says I need not).
- The thirteen decisions edited in place: read by comparison of the base and the head (each paragraph compared), not each as a whole entry; the entries WAY-02, 05, 11, 12, 19, 22, 03, 134, 168, 171, 172, 293, 17 and 115 were read in full where the 24 refer to them.
- `elements/common/foundation_check.py` read as the diff of the range (437 lines) plus `check_guidelines` and the lines around line 751; the unchanged body of the script was not read.
- `elements/common/test_foundation_check.py` read by test names and the tests I cite; 180 tests were run, not each read.
- `product-guidelines/{coding,styleguide,testing}` files: the passages that name the changed decisions, not each file.
- The merged-in tasks' files: not read.

## Searches not found or unclear

- A statement in the-way's foundation that a test holding a decision's sentence by a line `decision:` reaches the selection of a review (WAY-150): not found (o1).
- The reason the spec's non-goal says the discipline templates stay unchanged while WAY-172 changes the meaning of "a choice the task did not settle" there: not found in the spec or the reports (m3).
- Whether the base of the cycle (`ac75340`) is the commit the branch left the target from, or an earlier one: unclear; the range includes three merged tasks, which I took as given.
