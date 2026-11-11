PASS ff7799473843608eb11cc2f4e162920d8f7681a7

# Review of the whole change — request-decision-groups

Range `e3825a8..ff77994` (`git log`: `9876bfe`, `ff77994`); `git rev-parse HEAD` = `ff7799473843608eb11cc2f4e162920d8f7681a7`, the head given. Worktree clean before and after (`git status --short` empty). One author, no spec, no plan, no slices. No trust boundary touched (the new code reads text and imports only the standard library; no program run, no file written); no operation that cannot be undone. No reserved choice taken (no language, framework, library, store, login or place to run settled). No guidelines exist for the-way (task *Context* and *Questions to settle* 6), so none were compared.

Blocking findings: 0. Minor findings within the task: 4. Out-of-scope findings: 0.

## Findings

### Critical / Important

None.

### Minor (all within the task)

1. **"Let it through" against "only a task" after a correction.** `task-cycle/skill/request_template.md`, the paragraph of `### Fix or let through` under "For you to decide" ("Where the thing cannot be done in this request, the item offers only 'make a task of it' and 'let it through'") against kind 8 of the same file ("a finding it left unfixed carries only 'Make a task of it?'"), the *A correction* row of "The variants" ("carry only 'Make a task of it?'"), `task-cycle/skill/correction.md:50-52` and `:67`, and WAY-289 ("put by the request only with the question whether it becomes a task"). What is wrong: a thing left unfixed or undone by a correction cannot be done in this request (the loop ends after one correction), so the group paragraph (new in this change, task *To do* 5) says it offers a task and a let-through, while four other places this change keeps or edits say it offers a task only. Why it matters: the writer of a corrected request has two instructions for the same item and may write either; the human sees either "Make a task of it?" or "task or let through". Neither breaks the cycle, which is why this is Minor and not Important under WAY-263 (it is a difference in what is offered, not a rule the files break). Evidence: the five passages above, read side by side. Suggested fix: one sentence in the *A correction* row and in WAY-289 saying that the leftover carries "make a task of it" and "let it through", or one sentence in the group paragraph saying that after a correction the item carries a task only.
2. **Where the stages a blocked request did not run stand.** `task-cycle/skill/request_template.md`, "The variants", rows *A blocking finding remains* and *A slice failed twice*: "what has not run on that code — the return step, the reconciliation, the slices not made" and "the stages not run" are placed in *Needed from you*; kind 4 (skipped steps) puts a stage the cycle did not run in *Fix or let through*, and WAY-287's *Verification* repeats "the skipped step ... under *Fix or let through*". What is wrong: for a blocked request the unrun stages cannot be done in this request until the human decides, so *Needed from you* is defensible, but the template never says that kind 4 gives way to kind 1 there. Why it matters: a writer who reads kind 4 for a blocked request files the same stage in a different group than the row says. Evidence: the two rows against kind 4. Also tied to this: the state-line text "for `ready`, whether anything waits below" (the template, "The state line") is unchanged, but items of *You accept by merging* wait for nothing by the new rule; one clause there would remove the doubt.
3. **WAY-289 title narrower than its content.** `foundations/decisions.md:9167`: the title still asks "Which unfixed findings ...", while the entry now also holds the answer for a skipped step or check, a proposal not applied and an incomplete reading of the review. The author chose this on purpose (Choice 4). Why it matters: a reader or reviewer matching a change to the question by its title will not find these cases; the binding sentences carry them, so nothing is lost. Suggested fix: widen the title to "Which things the cycle left unfixed or undone does a request put before the human for a decision?" or the like, or leave it and accept the cost.
4. **Form: unwrapped and ragged lines.** `task-cycle/request_check.py:50` is 171 characters (the docstring sentence the change edited was not rewrapped; the base had no such line in this passage); `task-cycle/skill/request_template.md` lines holding "directly after *How to merge*; where the task document is in" and "space), and run both checks again, until both exit 0. Exit 2 is no listing: fix the call, or the file that could not be" (in "Write, check, publish", step 5) are ragged after the edit; `foundations/decisions.md` WAY-287 ("separate answer. Every group stands, reading `none`" followed by a short line) and WAY-327 *Rationale* ("WAY-290 has the form check judge no content, so a missing way or cost shows to nobody") break the wrap of the file. Evidence: `awk 'length>100' task-cycle/request_check.py` lists line 50 (171). No effect on behaviour; the checks pass.

## Against the task — coverage and fidelity

*To do* 1-8 and *Settlements to record* rows 1-5, each against the diff:

| Item | Result |
|---|---|
| To do 1 | Met. Template skeleton and the rule of the section: three `###` groups in the order and wording of the task, always all three, `none` per group, `none` alone for the section, one run of numbers. The Polish wording of the task ("Wymagane od Ciebie", "Do poprawienia albo przepuszczenia", "Przyjmujesz scaleniem") matches the test fixture word for word (`task-cycle/test_request_check.py`, block of `VALID`). The template says the block translates the headings, the group headings among them, and gives no Polish table; it gives none for the other headings either, so this follows the existing practice. |
| To do 2 | Met. Kinds 1-3 in *Needed from you*, 4/8/9/14 in *Fix or let through*, 5/6/7/10/11/12/13/15 in *You accept by merging*, with the criterion of each group. I compared the head's kind list with `git show e3825a8:task-cycle/skill/request_template.md` lines 170-247 and `:54`: the fifteen kinds name the same things at the same numbers. |
| To do 3 | Met. The four points for an item in which the human chooses; the action item (kind 3); the item of the accepting group; the opening sentence of that group; a bad and a good example side by side. The good example is a short rewrite of item 9 of loop2 PR #75 (I read the PR with `gh pr view 75 --repo mariusznazar/loop2`): same untried parts, same cost, same recommendation (merge / let through), a task as the third way; product names and links left out. |
| To do 4 | Met. Step 2 of "Write, check, publish", before the form check. |
| To do 5 | Met in the template (kinds 4, 9, 14) and in `correction.md:55-67`; see Minor 1 for the one place that disagrees. |
| To do 6 | Met. "item 8" (`correction.md`), "item 12" (`SKILL.md:563`) and "item 4" at kind 13 point at the same kinds as at the base. |
| To do 7 | Met. `check_decision_groups` reports: neither `none` nor groups; text before the first group; a heading that is no group; a repeat; wrong order; an empty group; a missing group; no check on the block. Docstring and tests follow. |
| To do 8 | Met. WAY-287 (three groups, criteria, `none` per group and for the section, continuous numbering, accepting group waits for no answer), WAY-289 (answer for items 4, 9 and 14), WAY-290 (group headings in what the script checks). |
| Row 1, 2 | WAY-287 edited in place, binding sentences now three (the template allows one to three, `elements/decisions/template.md:96`). |
| Row 3 | New WAY-327; scoped to the two first groups but for the action item, as To do 3 gives. |
| Row 4 | WAY-289 edited in place. |
| Row 5 | WAY-290 edited in place. |

Nothing in the diff goes beyond the task's content except the author's choices below.

### The author's choices, judged

1. Kind 15 listed as a kind in the accepting group: follows To do 2. Right.
2. Questions removed from kinds 10, 11, 12, 13, 15: follows from To do 2 ("nie wymaga odpowiedzi, scalenie jest zgodą"). Right; it is the real consequence of the group, and WAY-317's example had to follow.
3. "Let it through" for kind 8: To do 2 gives the three answers for the whole group. Right; the leftover after a correction is Minor 1.
4. WAY-289 title unchanged: Minor 3.
5. WAY-327 as a new entry, `derives from WAY-287`: row 3 asks for a decision; the relation is right. Its rule of two groups "but the action item" follows To do 3. Right.
6. WAY-114, WAY-286, WAY-288 unchanged: the task says so. Right.
7. Example without product names or links: right (the task asks for the loop2 item; leaving loop2 out avoids a link to a repository that may be private).
8. Kinds written as `- **N.**` bullets: right; a numbered list would be renumbered by a viewer (4, 8, 9, 14 would read 4, 5, 6, 7).
9. Script messages: one error at the section for a section with items and no groups, the others at the line of the fault. Right.
10. The edit outside the task, WAY-317 (*Verification* example "asks the human whether to merge without seeing the screen" became "tells the human ... which the human accepts by merging"): the old example asked a question in a section whose accepting group now waits for no answer, so the entry and the template (kind 13) would have disagreed; WAY-33 asks that the author fix such an entry in the same change. The edit touches only the example in *Verification*, not the binding sentences. Right.

## Against the foundation

- WAY-287, 289, 290 and 327 say what the code and the template do: the groups, their criteria, always three, `none` alone, continuous numbers, accepting group without a question, the answer for items 4/9/14, the script's checks, no judgment of content (the script test `test_a_section_with_no_content...` and the docstring say the same). WAY-290 *violates* adds "or whether an item stands in the group it belongs to"; the docstring says the same. No restatement broader than its entry found beyond Minor 1.
- WAY-05 (binding sentences carry what binds): the groups and the answers stand in binding sentences; the added *Rationale* and *Rejected* only explain. WAY-07 (edit in place): done; no appended second entry.
- WAY-286 (top part in plain words, no file names or identifiers) holds for the template's example and the item text it prescribes; WAY-114 (one plain sentence for entries the human did not see) is kept in kind 6; WAY-300 (reminder is no item) is kept in "How to merge".
- No invariant written or changed, no invariant test changed (`task-cycle/test_request_check.py` cites no `invariant:` line; the new code imports only the standard library, runs nothing, writes nothing).
- `foundation_check.py`: exit 0, `0 errors`.

## Tests — do they fail when the behaviour breaks

I copied `task-cycle/` to a scratch directory outside the worktree and broke `check_decision_groups` five ways; the tests fail on each: order check removed (1 failure), repeat check removed (1), text-before-first-group check removed (1), missing-group check removed (6), "no group" check removed (1 failure, 2 errors). A sixth mutation (empty-group check) did not match my pattern and did not run. `test_the_templates_example_of_the_decision_section_passes_the_check` reads the template's own example and runs the check on it; I ran it. The skeleton test ties the group names to the template.

## Own-work check of the author

The author names "numbers of kinds stay" and "the example passes the check". Both are where the change is weakest, and its check (list the kinds, compare with the base; run the example through the check) would catch each unmet. I repeated both and they hold.

## Declined to judge

- The Polish translation of the group headings in a real request (the template names none; the task's wording is the reference). Set aside because no real description is in the range.
- Whether a fresh review of the top part (the task's rejected way) would serve better than the writer's self-check: the task settled it.
- The wording of the opening sentence of *You accept by merging* in a real request: it is content for each request, not for this change.

## Checks I ran

| Check | Command | Exit |
|---|---|---|
| The range's tests of the script | `python -B task-cycle/test_request_check.py` | 0 (74 tests, OK) |
| Focused: task-cycle | `python -B gate/run_tests.py task-cycle` | 0 (254 tests) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0, `0 error, 0 warn, 3 info` |
| Private paths, on each of the six changed files | `python -B task-cycle/private_paths_check.py <file>` | 0 for each |
| Mutation of the script in a scratch copy | five edits of `request_check.py` in `...\scratchpad\mut2\task-cycle`, then `python -B test_request_check.py` | 1 each (tests failed as they should) |
| Kinds against the base | manual: `git show e3825a8:task-cycle/skill/request_template.md` lines 170-247, against `grep` of the head's `- **N.**` kinds | identical fifteen |
| Source of the good example | manual: `gh pr view 75 --repo mariusznazar/loop2 --json body` | read; item 9 matches the template's example in substance |

Could not run or not run: the whole gate (the orchestrator's); the author's "tests written first" claim (the failing-first re-creation) was not repeated, it is a claim I leave unverified; the focused directories other than `task-cycle` (the change touches no other).

## Reach beyond the dispatch

- `foundations/decisions.md` WAY-05, WAY-07, WAY-227, WAY-263, WAY-300: read whole, because the change writes or edits entries (WAY-05, WAY-07), grades (WAY-263), the reminder in the section it changes (WAY-300) and the request's role (WAY-227).
- `elements/decisions/template.md` line 96 ("one to three sentences"): to check the sentence count of WAY-287.
- `agent-instructions/README.md` (lines 60-76, 90-96), `task-cycle/skill/blocked_finding.md` (lines 8-18), `task-cycle/skill/foundation_step.md` (lines 10-34), `task-cycle/skill/SKILL.md` (lines 205-232, 436-466, 555-570): to find other statements about the section; none disagrees except as Minor 2.
- `gh pr view 75 --repo mariusznazar/loop2`: the source of the example (read only).

## Unread material

Counts of the review of the whole change: my selection (parts `task-cycle` and `decisions`, by *Scope*) holds 157 decisions (110 with `task-cycle`, 78 with `decisions`, 31 in both). **14 read whole** (WAY-05, 07, 114, 161, 162, 227, 263, 286, 287, 291, 292, 300, 326, 327) and **143 by title only** (the rest of the 157; I read all 157 titles). The six read in part below (WAY-289, 290, 295, 317, 288, 10) are counted among the 143.

Read in part, not whole:
- WAY-289, WAY-290: the changed hunks of the diff with their surrounding paragraphs (statement, *Verification*, *Rationale*, *Rejected* as the diff shows them); the unchanged remainder of each entry not read.
- WAY-295: statement, *Verification* and the start of *Rationale* (`foundations/decisions.md:9421-9445`); *Rejected* not read.
- WAY-317: the statement and the edited *Verification* hunk (`:10275-10310`); *Rationale* and *Rejected* not read.
- WAY-288: its statement as quoted in the task and at `:9143`; the entry not read whole.
- WAY-10: the *Verification* lines 305-318 only.

Decisions whose title points to a bearing on the change and that I did not read whole: WAY-33 (the author's search of the foundation; I rely on its restatement in `way_of_working.md`), WAY-150 (restated in `way_of_working.md` and in the skill; not opened as an entry), WAY-316 and WAY-318 (screenshots and artifacts in the description; the changed template passages that cite them are unchanged in meaning), WAY-308 and WAY-309 (private paths; run, not read), WAY-134 and WAY-126 (kept rows and projected entries; kind 6 text is unchanged), WAY-164, WAY-168, WAY-213 (read by title; the change is no code with guideline rules).

Guideline files: none exist for the-way (no `guidelines/` directory), so none to read. Invariants and part map: the `task-cycle` and `decisions` part-map entries and the invariants naming them were read as the author's report names them and as the orchestrator's answers at start give (boundary `none`); I did not re-read `foundations/invariants.md` whole. `task-cycle/skill/SKILL.md`: read in passages only (lines 205-232, 436-466, 500-512, 555-570). `foundations/glossary.md`: not read (no term of the glossary is used by the changed wording).

## Searches not found or unclear

- The kinds of the template have no mention of where a blocked request files kind 4 (Minor 2): searched `blocked`, `kind 4`, `item 4` in the template, `blocked_finding.md` and `SKILL.md`; no passage settles it.
- Whether the Polish headings of the groups should stand in the template: searched the template, `SKILL.md`, `correction.md` for any table of translated headings; none exists for any heading, so unclear whether the task's "po polsku:" is for the block's writer or only for the test fixture. Not graded.
- The author's "tests written first, failing" run: its scratch directory is not in the range and I did not repeat it; unverified.
- The count line of the handoff ("six files, 605 insertions"): `git diff e3825a8..ff77994 --stat` shows the same six files; no gap.
