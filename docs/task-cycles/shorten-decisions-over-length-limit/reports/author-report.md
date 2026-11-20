# Author report — shorten-decisions-over-length-limit

## Status

`done with concerns` (the concerns are listed under "Problems and concerns"; none blocks the change).

## Commits

Branch `task/shorten-decisions-over-length-limit`, base `bafe3904a80f3f74e6a722dc3d8dc8be1ed882cc`.

- `2f31b30f` — Name the two reports in the guide of the agent-instructions and set the limit of 600 words apart in the entry form (To do 12 and 13).
- `ef8aa061` — Bring the twelve decisions over the length limit under it: paragraphs for ten, WAY-287 cut in two, the cases of the audit command in WAY-416 (To do 1–11; WAY-416 is `row 1`).

## Files changed (added / removed lines, `git diff --stat bafe3904..HEAD`)

| File | + / - |
|---|---|
| `agent-instructions/README.md` | 7 / 7 (one paragraph rewrapped to 100 columns) |
| `elements/decisions/template.md` | 3 / 2 |
| `foundations/decisions.md` | 179 / 133 |
| `process-audit/SKILL.md` | 2 / 2 |
| `process-audit/audit_count.py` | 4 / 4 (comments) |
| `process-audit/problem_register.py` | 2 / 2 (comments) |
| `process-audit/record_reading.py` | 8 / 8 (comments) |
| `process-audit/test_audit_count.py` | 25 / 25 (lines `decision:` and comments) |

Total 230 insertions, 183 deletions. No behaviour of any script changed.

## Number of the new decision

The log holds entries up to WAY-415 and the list of withdrawn numbers up to WAY-392, so the next free number is **WAY-416**. It stands at the end of the section "Process audit" (after WAY-405), *Scope* `process-audit, task-cycle`, *Relations* `narrows WAY-344`, *Based on* `none`, *Origin* `none`.

## Foundation step: the entries

Entry marked `row 1`: **WAY-416** — "What does the command that counts the audit do when a file it reads lacks a field it needs?"

- Meaning, English: where the command that counts the audit reads a file that lacks a field, it writes its result, gives the values that need the field as unknown and ends with exit code 1 and an `Error:` line, and it reads earlier forms of the files as such, instead of ending with exit code 2 as WAY-344 gives for other scripts; WAY-416 prevails over WAY-344 for the cases it names.
- Znaczenie, po polsku: gdy komenda licząca audyt czyta plik, w którym brakuje pola, zapisuje wynik, wartości zależne od tego pola podaje jako nieznane i kończy się kodem 1 z linią `Error:`, a wcześniejsze formy plików czyta jako takie; w opisanych przypadkach ta decyzja ma pierwszeństwo przed WAY-344, która dla innych skryptów każe kończyć kodem 2.
- Structure: paragraph 1 (257 words, 3 sentences) is the sentence of precedence, the former rest of the second sentence of WAY-344 (the missing fields of the cycle's record, the earlier forms of a stage report, the file of a changed tool) and the sentence of the tables of weights and costs; paragraph 2 (195 words, 3 sentences) is the sentences of the two columns of the cache writes, of the cycle's record lacking a line or an item, and of the locations file without the key `repository`. Total 452 words.
- Writer's additions, none of them a pair of examples or a field the row left open: (a) the sentence of precedence in the binding sentences ("For the command that counts the audit this decision prevails over WAY-344 in the cases that its sentences give, and in every other case WAY-344 binds that command."), as WAY-25 and the task's *Decisions in play* require; (b) one sentence at the start of the *Rationale* ("the cases of the command that counts the audit grow with each change to that command, so they stand in a decision of their own: a change to one of them then changes this entry and leaves the general rule of WAY-344 as it is"), which is the reason the task's source gives for the split ("to ten wpis rośnie z każdą zmianą komendy audytu"), worded without a count; (c) two ways in *Rejected*, the two "Not chosen" of the question "Co zrobić z WAY-344", worded without numbers because the template bars counts in prose the writer writes.

Edits of existing entries made by the To do items (not entries written from a row; they need no row mark):

- **WAY-344**: the general rule stays; its second sentence now ends "…and except that the command that counts the audit is bound by WAY-416 in the cases that decision gives, where it prevails over this decision."; two paragraphs (210 and 131 words), 4 sentences, 341 words in all.
- **WAY-287**: first sentence cut after "…the foundation entries the human did not see at the task document." and the second begins "The section stands in three groups, headed …"; three paragraphs (218, 185 and 27 words).
- **WAY-19**: "while a part of another question that an existing entry answers, or a part of its own question that it sets apart, is a sentence of that entry where it cannot change without changing that entry."
- **WAY-391**: *Scope* `relation-model, process-audit, task-cycle, elements-common`.
- **WAY-150**: "first paragraph" is now "second paragraph".

### Map for the description of the request: where WAY-344's *Verification*, *Rationale* and *Rejected* went

Verification (the clause `tests:`), nine clauses of the base, in order:

| # | Clause (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "that a field missing from a Claude Code transcript … or from the definition of an agent type … exit code 2 … and that each such reading has a test that gives the file without a field" | WAY-344 | second sentence (the rule, exit code 2) and the sentence "Each reading of a file that the rule covers has one test" |
| 2 | "that the command that counts the audit, at a field missing in the file of the measures, the file of the gate times or a stage report, … exit code 1 and a line `Error:`" | WAY-416 | the former rest of WAY-344's second sentence |
| 3 | "that it reads a stage report of an earlier form, one with no heading … or with neither column of the cache writes …" | WAY-416 | the former rest of the second sentence (earlier forms) and the sentence "Where a stage report has neither of the two columns of the cache writes" |
| 4 | "that it reads a report that has one time line or one of the two cache write columns and not the other as a missing field" | WAY-416 | the same two sentences |
| 5 | "that it reads a cycle's record that lacks the line `Process pin` or `Target branch and base` or an item it reads of it …" | WAY-416 | "Where the command that counts the audit reads a cycle's record that lacks a line or an item" |
| 6 | "that a table of weights or of the costs of an occurrence which lacks a level gives the result, unknown values and the line `Error:`" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 7 | "that a locations file with no key `repository` under `the-way` gives the checkout in which the script lies and no line `Error:`" | WAY-416 | "Where the locations file has no key `repository` under `the-way`" |
| 8 | "that the check of the foundation lists an invariant whose sentence the change reworded and whose copy at the commit the branch left lacks its *Method* or its *Part* …" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy of the file …" |
| 9 | "that the file of a tool the cycle's own change changed is not read" | WAY-416 | the former rest of the second sentence ("a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339)") |

The pair of examples (*complies* four, *violates* six) stays whole in WAY-344, the violating example "a script that is neither a check of form nor the count of the audit lists an absent field as an item with exit code 1" included, as the settlement says; WAY-416 has no pair. The clauses 1 and 8 got "and" before the last one in WAY-344; the clauses of WAY-416 keep their words.

Rationale, thirteen sentences of the base, in order:

| # | Sentence (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "a script that reads a file an agent writes meets a changed format as an absent field …" | WAY-344 | the first sentence |
| 2 | "The coding guidelines of the-way point to this rule …" | WAY-344 | the first sentence |
| 3 | "An error naming the field lets the author … exit code 2 says the file was not read, apart from a listing of findings … and apart from the count of the audit, whose file in the history of git …" | **cut at the clause boundary before ", and apart from the count of the audit"**: first part WAY-344 (the second sentence, exit code 2 and the check-of-form exception), second part WAY-416 (the former rest of the second sentence) | both |
| 4 | "A field that an earlier form of a file never had is no loss of the file …" | WAY-416 | the former rest of the second sentence |
| 5 | "The record of a cycle is such a file …" | WAY-416 | "Where the command that counts the audit reads a cycle's record …" |
| 6 | "The rule covers the whole reading of a file a change reworks …" | WAY-344 | the second sentence and the test per reading |
| 7 | "The price: a change that reworks the reading of a file pays …; a stage report that has lost its two time lines …, where the rule alone would give an error; an existing script that no change touches stays as it is …; and the review alone answers …" | **cut at the clause boundaries**: "The price: … every field of that file; an existing script … gives up." stays in WAY-344; "a stage report that has lost … would give an error" goes to WAY-416 | the clause of the stage report concerns the former rest of the second sentence; the others concern the rule |
| 8 | "Tests of a script's behaviour stand without an invariant, since WAY-12 …" | WAY-344 | the *Verification* of the rule |
| 9 | "A table of the register of problems that lacks one of its levels …" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 10 | "The key `repository` under `the-way` is the one key …" | WAY-416 | "Where the locations file has no key `repository` under `the-way`" |
| 11 | "The exception is written for that key alone …" | WAY-416 | the same |
| 12 | "A stage report with neither column of the cache writes was written before the columns existed …" | WAY-416 | "Where a stage report has neither of the two columns of the cache writes" |
| 13 | "A copy of a file at the commit the branch left is a file no change can mend …" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy …" |

Words the two cuts add so that each part reads as a sentence: in WAY-416 the head "Exit code 2 says the file was not read, apart from the count of the audit," (the first part in WAY-344 keeps "exit code 2 says the file was not read, apart from a listing of findings, which a caller carries out as findings.") and the head "The price:" before the clause of the stage report; the full stop and the "and" at the cuts differ. A script of my own compared the multisets of words (see below): nothing of the base *Rationale* is dropped; the additions are those two heads, the full stops, and the writer's sentence (b) above.

Rejected, sixteen ways of the base, in order:

| # | Way (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "the rule as a sentence of WAY-379" | WAY-344 | the first sentence |
| 2 | "the rule as a decision with an invariant whose *Part* is `every`" | WAY-344 | the first sentence |
| 3 | "the whole script as what a changed script brings under the rule" | WAY-344 | the second sentence |
| 4 | "only the readings of fields that the change adds or reworks" | WAY-344 | the second sentence |
| 5 | "review alone with the test left to the choice of the cycle" | WAY-344 | "Each reading … has one test" |
| 6 | "review and a test for every field" | WAY-344 | "Each reading … has one test" |
| 7 | "exit code 1 always, a missing field as an item of the list" | WAY-344 | the second sentence (exit code 2, the check of form) |
| 8 | "a new exit code, such as 3" | WAY-344 | the second sentence |
| 9 | "exit code 2 with no result for the count of the audit" | WAY-416 | the former rest of the second sentence |
| 10 | "the exception for the stage report alone, the file of measures and the file of gate times keeping exit code 2" | WAY-416 | the former rest of the second sentence |
| 11 | "for a table of the register of problems that lacks a level, exit code 2 with the level named and no result" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 12 | "for the key `repository` under `the-way`, exit code 2" | WAY-416 | "Where the locations file has no key `repository` …" |
| 13 | "for the same key, a general exception for a field whose absence the description of a script allows with a default" | WAY-416 | the same |
| 14 | "for a generator of copies that shares its exit codes with another script, an exception written into this decision" | WAY-344 | the second sentence (its list of exceptions) |
| 15 | "for a field missing from the copy at the commit the branch left, an exception that leaves the invariant out with no word" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy …" |
| 16 | "the same case left as the cycle that wrote the check left it, with no sentence" | WAY-344 | the same |

WAY-416's *Rejected* adds, after the five moved ways, the two ways of the question "Co zrobić z WAY-344": the cases kept in WAY-344 and divided into paragraphs only; a decision for each case of the command that counts the audit.

## Checks

Commands run from the worktree root.

- `python -B elements/common/foundation_check.py` — after the text of the log was written and before the lines `decision:` of `process-audit/test_audit_count.py` were re-pointed: **exit 1**, 9 errors (eight lines `decision:` whose quotation stood in no binding sentence of WAY-344, and "`WAY-416` is added or changed by this change and nothing holds it"). After the lines were re-pointed: **exit 0**, output `0 errors`, no line `listed:` of any kind. Run again on the committed tree: exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` — exit 0 (277 tests, OK).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (OK).
- `python -B gate/run_tests.py task-cycle` — exit 0 (OK, 2 skipped; the skips are the suite's own).
- `python -B .runs/author/compare_binding.py` — exit 0. It reads `git show bafe3904:foundations/decisions.md` and the log at the head, takes the binding sentences of each entry (the text from the heading to the first field) and compares word for word (difflib over the words): the ten entries of the table are identical to the base, except for the single replacement `first` -> `second` in WAY-150. For WAY-287 the only difference is `document —` -> `document. The section stands`; for WAY-19 the words of To do 10; for WAY-344 and WAY-416 together against the base WAY-344 the differences are the new words named under the entries above and the changed order of the third and fourth sentences. It also prints the paragraphs: no paragraph over 300 words, no entry over 600 (WAY-150 592, WAY-134 583, WAY-339 488, WAY-416 452, WAY-287 430, WAY-344 341; the others 301–385).
- `python -B .runs/author/compare_prose.py` — exit 0. Compares the multisets of words of *Rationale*, *Rejected* and *Verification* of the base WAY-344 with those of WAY-344 and WAY-416 together: dropped none in each; added only the heads, punctuation, the two clause connectors ("tests", "and") and the writer's additions (b) and (c).
- Not run: the full gate (WAY-160, the orchestrator's); `ruff check` and `ruff format --check` (no ruff in this environment — `python -m ruff` is missing); the changed lines of the Python files are comments and a docstring, and I checked that none of my added lines is longer than 100 columns except the line `decision: WAY-416 "Where the command that counts the audit reads a cycle's record that lacks"` of `process-audit/test_audit_count.py` which is as long as the line it replaced (103, with WAY-344).
- `elements/decisions` and `elements/invariants` hold no `test_*.py`, so there is no focused run for them.

## Own-work check (WAY-164)

- Requirement most likely unmet: To do 8 (every reference to WAY-344 that concerns a moved sentence now names WAY-416) and the acceptance criterion of the word-for-word comparison. The first is a judgement over about ninety references; the foundation check proves only the lines `decision:`.
- Check: (1) `git grep -n "WAY-344"` over the whole repository outside `docs/task-cycles/` before and after, with each remaining reference read in its context; (2) `git grep` for the start of each moved sentence ("The command that counts the audit, where a table", "Where a stage report has neither", "reads a cycle's record that lacks a line", "locations file has no key", "except that the command that counts") outside the log: no hit except the re-pointed lines `decision:`; (3) the two scripts above.
- Showed: the references that now name WAY-416 are the 13 + 2 + 3 + 1 + 2 lines `decision:` and the comments listed under the files changed; no unchanged line `decision: WAY-344` quotes a moved sentence (the check would fail). Judgement calls named below.

References to WAY-344 left unchanged, and why:

- `agent-instructions/test_agent_type_copies.py` (4 lines), `agent-instructions/test_skill_entry_points.py` (6), `task-cycle/test_cycle_stages.py` (all lines `decision:` and comments), `elements/common/test_foundation_check.py` (2 lines `decision:`), `elements/common/test_compare_log_entries.py:156`, `elements/common/foundation_check.py:111,815`, `elements/invariants/template.md:176`: they concern the general rule (a transcript or a definition of an agent type ends with exit code 2), the check of a copy at the base (listed:) or the test per reading, all sentences that stay in WAY-344.
- `process-audit/test_audit_count.py:5012` and `process-audit/test_record_items.py:514,680,762`: lines `decision: WAY-344 "Each reading of a file that the rule covers has one test"`, the sentence stays in WAY-344.
- `process-audit/test_audit_count.py:3195` and `process-audit/audit_count.py:274`, `process-audit/problem_register.py:218,297`, `process-audit/problem_register.md:34`: a heading, a table or a column of the register that is missing ends the run with exit code 2 — the general rule; the sentence of WAY-416 gives only a missing level of a table of weights or costs.
- `process-audit/audit_count.py:268` (the files of the measures and gate times "are under the check of WAY-344, since their reading is new" — the general rule — "and they end the run with exit 1 …"): kept WAY-344 and added `(WAY-416)` after the exit 1, since the sentence concerns both.
- `process-audit/problem_register.py:6` (module docstring): kept WAY-344 and added WAY-416 beside it.
- `guidelines/coding.md:118,123`, `guidelines/coding-generator.md:38`, `guidelines/coding-measuring-report.md:36`: the rule of a missing field for scripts in general.
- In the log: WAY-294 (`narrows WAY-344` for the reports its script reads, and two rejected ways), WAY-339 (rejected, "a reading that WAY-344 checks"), the two lines of the section on the-way's own guidelines, WAY-388 (the generator ends with exit code 2 "as WAY-344 gives"): all the general rule.
- `docs/task-cycles/`: records, left as the handoff says.

## Walkthrough

The change alters no behaviour a user sees in the running product: it divides entries of the log, adds one entry, and changes comments, lines `decision:` and two texts of guides; no script, screen, API or command changed in what it does, and the focused suites pass.

## Reaches beyond the dispatch

- WAY-294 (`foundations/decisions.md`, the whole entry, about 70 lines): found by the search for "WAY-344"; read to decide whether it concerns a moved sentence (it does not: it narrows the general rule).
- WAY-330 and WAY-337 and the heading of the section "Process audit" (same file, lines around 8533–8635): read for the place and the form of the new entry at the end of that section.
- The passages of `process-audit/audit_count.py`, `record_reading.py`, `problem_register.py`, `test_audit_count.py` around each reference (see "Unread material").

## Choices, with the way rejected and its cost if wrong

- **Shape of WAY-416.** Paragraph 1 holds the precedence sentence, the former rest of the second sentence and the sentence of the tables; paragraph 2 the three sentences of the earlier form of the stage report, the cycle's record and the key `repository`. Rejected: putting the precedence sentence last or alone (it would sit apart from what it governs), and one paragraph of six sentences (over the limit). Cost if wrong: another division of the same words.
- **The first sentence of WAY-416 is the precedence sentence, so the start of the former rest of the second sentence is "The command that counts the audit, in a file of a cycle's record …"** (the words "and except that" dropped, "the" capitalised): lines `decision:` of the audit tests that held "The rule binds a script that a change adds and, in a script" now quote that start (13 lines). Rejected: leaving them on WAY-344 (the sentence of WAY-344 no longer says what they test), or quoting the precedence sentence at them (it holds nothing of what they assert).
- **Words added at the cut of the second sentence of WAY-344:** "is bound by WAY-416 in the cases that decision gives, where it prevails over this decision" (the number, as WAY-25 and the task require) and, in WAY-416, "For the command that counts the audit this decision prevails over WAY-344 in the cases that its sentences give, and in every other case WAY-344 binds that command." (the area where it prevails).
- **The limit of 600 words in the template** is a line in parentheses after the paragraphs, `(all the binding sentences of the entry, its paragraphs together, at most 600 words)`, not a line in angle brackets: every angle-bracketed line of the form is a paragraph, so the limit would have read as a paragraph. Rejected: angle brackets; moving the words outside the code block. Cost if wrong: a one-line change.
- **WAY-19 wording** repeats the words of WAY-05 ("a part of another question that it answers", "a part of its own question that it sets apart") and says nothing of paragraphs, so it cannot contradict WAY-05 on them. Rejected: adding "in a paragraph of its own" (WAY-05 makes it a duty for a part of another question and a may for a part of the own question; the sentence would need both).
- **The lines of the new paragraphs were not rewrapped** in the ten entries (a line broken at the start of the new paragraph, so that the diff holds only added blank lines and the split lines); the new entry and the paragraphs of WAY-344 are wrapped at 100 columns. The README paragraph was rewrapped, because a new line would have been 105 columns.
- **No move of a part of a file out first (WAY-365):** this change adds no code to a function or a file, it changes comments, a docstring and lines `decision:`, so the rule of size of the coding guidelines has nothing to apply to; I did not read that rule's text beyond the section named under "Unread material".

## Problems and concerns

- The precedence sentence of WAY-416 is held by no test (nothing in the behaviour of the count differs between "precedes" and "does not precede" in a way a test of one script can assert); the decision is held through its other five sentences by 21 lines `decision:`. If the reviewer wants it held, the smallest holder is one more line `decision:` at a test of exit 1 for a missing field of the count, quoting "For the command that counts the audit this decision prevails over WAY-344".
- The template's "Changing a decision" still reads "A part of the question an existing entry answers is a sentence of that entry, in a paragraph of its own as "Binding sentences" gives" — the wording WAY-19 had before this change. It does not contradict WAY-19 or WAY-05; it is no task item, so I left it. Observed, not verified beyond reading both.
- `process-audit/test_audit_count.py:2036` cites "the settlement 6 of the task" — a task of an earlier cycle; I changed only the number of the decision there.
- WAY-344 keeps in its second sentence the exception for the count only as a pointer; its violating example still names "the count of the audit", as the settlement orders. A reader of WAY-344 alone needs WAY-416 to know what the count does.

## Working copies

`.runs/author/compare_binding.py` and `.runs/author/compare_prose.py` (ignored, not committed, kept as the handoff asks). The other working files of the step (the splitting scripts, the texts of the two commit messages, the generated texts of the two entries and the logs of the four test runs) were removed. No worktree, clone or system temporary directory was made.

## Unread material

Read whole: `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md` (and `read.md`, `decide_entry.md` beside it), `elements/decisions/template.md`, `agent-instructions/README.md`, the frozen task document, and the decisions WAY-344, 287, 19, 391, 05, 25, 18, 12, 02, 30, 114, 33, 150, 256, 148, 339, 289, 405, 136, 154, 139, 134, 386–390.

Not read whole, or not read:

- `guidelines/coding.md` and `guidelines/testing.md`: not read. I changed comments, a docstring and lines `decision:` only, and no test or code; I read only the section of `guidelines/coding.md` that refers to WAY-344 (lines 112–128).
- `guidelines/coding-shared-module.md`: read lines 1–20 (the *Applies to* line and the table), for point 11.
- `elements/common/foundation_check.py`: not read; I used its output and the way the check reports a quotation, which the template's "Verification" gives. What it counts as a sentence I took from the template ("Binding sentences", "Verification") and confirmed by the check's result.
- The files I changed in `process-audit/` (`test_audit_count.py` about 5,700 lines, `audit_count.py`, `record_reading.py`, `problem_register.py`, `SKILL.md`): not read whole; I read the passage around each reference (about 10 lines each) and the 13+ test names and first lines of the tests whose line `decision:` I moved.
- Rationale and *Rejected* of WAY-25, 30, 114, 18, 12, 02, 33: read whole, as printed. The other entries of the table of the task's "Podział na akapity" were read whole.

## Searches not found or unclear

- `elements/decisions/SKILL.md` does not exist (the handoff says so); the skill is `elements/decisions/skill/SKILL.md`. Found.
- The task says WAY-05 "as it stands at the base, not the wording the task quotes as before #152": read at the base; it carries the paragraph of a part of the entry's own question and the limit of 600 words, so nothing is unclear.
- Whether a comment that cites WAY-344 for the count's behaviour concerns "a moved sentence" is a judgement in five places (`audit_count.py:268`, `problem_register.py:6`, `problem_register.py:218`, `test_audit_count.py:3195`, `audit_count.py:274`); named above with the decision I took in each.
- The handoff names "WAY-02 … lines `decision:`" for the form of the quotation; confirmed against WAY-02 and the template: three words or more, at the start of a sentence.
