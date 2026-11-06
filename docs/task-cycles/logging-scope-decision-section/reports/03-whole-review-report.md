FAIL fa445fd10d8ddc3af9126bf2873b61c1029746c2

# Review of the whole change — logging-scope-decision-section

Range `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a..fa445fd10d8ddc3af9126bf2873b61c1029746c2` (`d6871fc`, `501a2a1`, `fa445fd`). `git rev-parse HEAD` is `fa445fd10d8ddc3af9126bf2873b61c1029746c2`, as dispatched. Route: one author, no plan, no slices, no spec. I computed the diff before reading the author's report. The worktree was not changed (scratch copies only under the session scratchpad).

Counts: blocking 1, Minor 3, out of scope 0.

## Findings

### Critical

none

### Important (blocking, within the task)

**I-1. WAY-287 *Rejected* states as fact what the task gives as an unproven search result, and rewrites one reason.**
Place: `foundations/decisions.md`, WAY-287, *Rejected*, last sentences ("A general item for everything a decision asks the human to see at the merge. No other decision asks for that, and such an item would turn this section into a list the human reads in full, so that its `none` says less.").
The task's *Questions to settle* 1, third *Not chosen*, gives: "przeszukanie dziennika nie znalazło drugiego takiego przypadku, a taka pozycja zachęcałaby do zrzucania do sekcji wszystkiego, choć jej `none` ma znaczyć 'można scalić'". The task's *Context* adds that this was a word search ("at the merge", "sees", "merges") and "to wyszukiwanie po słowach, nie dowód". The entry drops that qualification and says flatly "No other decision asks for that". Two further departures:
- the reason "encourage dumping everything into the section, though its `none` is to mean 'can merge'" becomes "a list the human reads in full, so that its `none` says less". "Reads in full" is not in the source; it is the author's own reason.
- the template's rule for *Rejected* (`elements/decisions/template.md`, "*Rationale* and *Rejected* are prose which ... names no ... count ... and does not tell how the decision was reached", and the *Settlements to record* paragraph: ways the row's source keeps, "each with the cost or the reason kept beside it") is not met by a sentence that reports the outcome of a search.
Why it matters: the entry is the log's statement of what was weighed. A reader (or a later critic) takes "No other decision asks for that" as established. It is not: the task calls it a word search and not proof. In the log itself, WAY-114 (about line 2085, "the human sees the changed meaning in the request") and WAY-172 (about line 4808, "for the human to accept at the merge") also have the human see something at the merge, so the categorical sentence is at best ambiguous. A restatement that drops a qualification is a WAY-263 departure, and the dispatch asks that nothing taken from the sources be altered or invented. The other half of the sentence (B and C) is faithful.
Evidence: the diff of `fa445fd`; the task text above; `grep -n "at the merge" foundations/decisions.md`.
Fix, small: state the third option with the source's reason ("it would encourage moving everything into the section, though its `none` is to mean the request can be merged"), and either drop "No other decision asks for that" or qualify it as the task does (a search of the log by words found no second case; not proof).

### Minor

**M-1. *Rejected* uses the task's option letters with no option A in the entry.** `foundations/decisions.md`, WAY-287, *Rejected*: "B. ... C. ..." and a third way with no letter. The log is read without the task, where the letters were defined; "B" and "C" mean nothing there, and the third item has none. Naming the ways in words, as WAY-274's *Rejected* does, reads without the task.

**M-2. The *Rationale* sentence is not in the task.** `foundations/decisions.md`, WAY-287, *Rationale*, last sentence ("Additions to a product's logging scope come here because WAY-274 counts on the human seeing them at the merge, and this section is where the merge shows them."). The author's report names it as their own choice. It is accurate and follows from the task's *Need*, so I grade it Minor; the human sees it only if they read the entry.

**M-3. Template item 10 names no place to look for the additions.** `task-cycle/skill/request_template.md:191-193`. Items 1-8 say what they are taken from ("from the record's ...", "from the changed files read against ..."). Item 10 says what to list and when to leave it out, which is all the task asks (To do 1), but an agent writing the description is not told that the additions stand in the change's diff of the product's logging-scope rule. Whether the item will be filled when it should is therefore left to the agent's attention. Not a defect against the task; mentioned because the omission of an addition is the failure the task exists to prevent.

## Against the task

| Task item | Result |
|---|---|
| To do 1: new item at the end of the *For you to decide* list, in plain words (what it is, which log line carries it), "Accept it?", absent when nothing is added, existing numbers unchanged | Met. `request_template.md:191-193` is item 10; items 1-9 unchanged (diff shows only the addition). Wording follows the task, nothing more. |
| To do 2: WAY-274 unchanged; WAY-287 list gains the kind | Met. WAY-274 is not in the diff; the binding sentence gains "the additions a change makes to a product's logging scope" (rewrapped; the rest of the sentence is unchanged word for word). |
| To do 3: BOM at the start of a file passes as without | Met. `read()` uses `utf-8-sig` for both the description and the task. Test `test_files_saved_with_a_byte_order_mark_exit_as_without_it` passes; on the base script (scratch copy) it fails. |
| To do 4: `## <…>` fails the check, message says omit or write the heading of the task's own section | Met. `request_check.py:353-358`, the heading fails wherever it stands, with its content or `none`. Test `test_the_placeholder_heading_is_reported_even_with_none_under_it` passes; on the base script it fails. The message names both ways out, as the task says. |
| To do 5: the template's sentence under the placeholder says the heading is omitted when the task has no sections of its own | Met. `request_template.md:103-104`. The skeleton keeps the `## <…>` line, which `TemplateTest.test_the_templates_skeleton_has_the_scripts_headings` pins. |
| Settlement row 1: the addition stands in the PR decision section, WAY-274 unchanged; *Rejected* of WAY-287 was `unknown` | Written in place in WAY-287 (the log edits an entry in place, WAY-07; a new number would duplicate the question WAY-287 answers). *Rejected* is filled from *Questions to settle* 1, but not faithfully: see I-1. |

Departures the author named, judged:
- Edit in place of WAY-287 against a new number: right, the row says "dopisek w WAY-287".
- *Rationale* sentence: M-2.
- *Rejected* filled from *Questions to settle* 1: right in principle, wrong in wording: I-1, M-1.
- BOM stripped by `utf-8-sig`: sound. `check()` called directly with a string that carries a BOM still reports line 1; no caller does that (`main` reads through `read`).
- Removed in-memory BOM test: acceptable, since the design strips the BOM at file read, and the file-level test fails without the fix.

## Against the foundation and the guidelines

Foundation read by the parts the change touches (`task-cycle`, `decisions`): the entries WAY-274, WAY-287, the template `elements/decisions/template.md` (whole) and the rules for a decision written from a row of *Settlements to record*. The-way has no guidelines of its own for code or tests. The change adds no invariant, changes no invariant test and no surface, and marks nothing *Violated*. WAY-287's binding sentence and the template's list now agree (the kind is in both). WAY-290 (script judges no content): the placeholder check judges a heading's form only, in line with it. The decision's *Relations* line does not name WAY-274, and need not: WAY-274 is not a higher decision WAY-287 serves.

Reserved choice: none taken. Trust boundary and irreversible operation (answers of the start: no): the change prepares nothing of the kind; `request_check.py` only reads two files.

Own-work check of the author: the requirement named (the placeholder rule rejects a real own section; the BOM change breaks a file without BOM) fits where the change is weakest, and `test_the_tasks_own_sections_in_their_slot_pass` and the BOM test would catch it. Tests are not self-confirming: the two new tests fail on the base script and pass on the head.

## Declined to judge

- Whether WAY-287's *Verification* should gain a complies/violates example for the logging-scope item: the task asks only for the kind in the list.
- Whether WAY-114 and WAY-172 are "second cases" of a decision counting on the human at the merge: a search of the foundation beyond the task, not the change.
- The separate variant of the PR template for consent to data that points to a person: the task puts it out of scope.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Tests of the part | `python -B gate/run_tests.py task-cycle` (in the worktree) | 0 (`Ran 94 tests`, `OK`) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| New tests against the base script (scratch copy of `request_check.py` at `61c72fb` with the head's test file and template) | `python -B -m unittest test_request_check` in the scratchpad copy | 1, exactly the two new tests fail |
| Search of the log for decisions that count on the human seeing something at the merge | `grep -n "at the merge\|sees it\|sees them\|human sees\|human merges" foundations/decisions.md` | 0 (manual reading of the hits) |

Not run: the whole gate (`python -B gate/run_tests.py`), which the orchestrator runs.

## Reaches beyond the dispatch

- `elements/decisions/template.md` (whole, in effect): to judge the *Rejected* and *Relations* fields of WAY-287; the selection of the foundation by the parts of the change.
- `foundations/decisions.md` WAY-274 whole and the lines found by the grep above (WAY-114, WAY-172): to test the claim "No other decision asks for that".
- `task-cycle/request_check.py` around lines 300-420 and 460-480, and `task-cycle/test_request_check.py:660-700`: the callers and the neighbouring test of the changed code.

## Searches not found or unclear

- Unclear: whether "No other decision asks for that" in WAY-287 means "no other decision asks for a general item" or "no other decision counts on the human's seeing at the merge"; the second is not shown by the task (word search, "nie dowód") and the log has hits (WAY-114, WAY-172) that make it doubtful. Raised as I-1.
- Not found: a place in the cycle's files that tells the agent writing the description how to find additions to the logging scope in the diff (M-3).
- Not found: any other file that lists the kinds of WAY-287 or counts the items of the template's list (searched `For you to decide`, `logging scope` in `*.md` and `*.py`): the only copies are WAY-287 and the template, both updated.
