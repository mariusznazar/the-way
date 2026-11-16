# Author report — the audit answers whether a contradiction came out after the code

**Status:** done with concerns (one concern, about the missing items of `cycle.md` and WAY-344; see
*Questions and concerns*).

## Commits (on `task/audit-answers-contradiction-after-code`, base `aba5ee92a0734c2e775cc69662af669bf6455795`)

1. `6867078` — the move, with no change of behaviour: the reading of the items *Discarded attempt* and
   *Review rounds* leaves `process-audit/audit_count.py` for `process-audit/record_items.py`.
2. `19f7003` — the change in code and decisions: Q1 from the two marks, the tests, WAY-404, WAY-405 and
   the sentence of WAY-337.
3. `ab2c8c8` — the instructions: the review method, the cycle's skill, the reserved return, the record
   template and the skill of the audit.

Head: `ab2c8c801b2ba9170a00ed6056b8b7c56b062868`. The worktree is clean.

## Files changed (added / removed lines, `git diff --stat aba5ee9..HEAD`)

| File | + / - |
|---|---|
| `foundations/decisions.md` | 92 / 3 |
| `foundations/part_map.md` | 1 / 0 |
| `process-audit/SKILL.md` | 8 / 1 |
| `process-audit/audit_count.py` | 18 / 185 (3310 lines before, 3143 after: still over the threshold of 1000) |
| `process-audit/record_items.py` (new) | 243 / 0 |
| `process-audit/test_audit_count.py` | 134 / 69 |
| `process-audit/test_record_items.py` (new) | 246 / 0 |
| `task-cycle/record_template.md` | 23 / 13 |
| `task-cycle/review/SKILL.md` | 14 / 3 |
| `task-cycle/skill/SKILL.md` | 11 / 5 |
| `task-cycle/skill/reserved_return.md` | 3 / 2 |

## What the task required, and where it stands

- *To do* 1: `task-cycle/review/SKILL.md`, section "3. Grade" (a paragraph on the mark
  `Contradiction: yes — <entry or settlement>` / `Contradiction: no`, what counts, that a point of *To do*
  left undone is none) and section 4 (the report holds the mark of each blocking finding).
- *To do* 2: `task-cycle/skill/SKILL.md`, the paragraph "For a fix, it gives the findings file" (the
  findings file carries the mark; the entry of the round says `contradiction yes` where any blocking
  finding of the round, one the review of the fix found new included, carries `yes`); the record
  template's item *Review rounds* gives the entry `findings `reports/<file>.md`, contradiction <yes | no>: ...`.
- *To do* 3, 4, 5 and settlement row 3 (code): `process-audit/record_items.py` (`read_contradiction`,
  `read_rounds`, `round_of`, `discarded_reason`) and the docstring of `process-audit/audit_count.py`.
- *To do* 4 (the entry of a review without fixes): form `review `reports/<file>.md`, PASS: ...`, in the
  record template, in `read_rounds`, and in WAY-337.
- *To do* 6: the item *Discarded attempt* of the record template opens with `reason: ` and a marker in
  backticks; `task-cycle/skill/SKILL.md` (the two paragraphs) and `task-cycle/skill/reserved_return.md`
  ("Discard the attempt") write that marker; the detection of denials (`denied_before`, `phrase_starts`
  and their constants) is gone; the four examples of review #100 give `unknown` in
  `test_record_items.py` and in `test_audit_count.py`.

## The foundation entries written

Each marked as `foundation_step.md` gives, with its two sentences of meaning.

1. **WAY-404** (new, section "Process audit") — `row 1`.
   EN: A reviewer marks each blocking finding as a contradiction with the settlements or as none — a
   contradiction being a departure from an entry of the foundation or from a settlement of the task
   document, never an undone point of *To do* — and the audit of the process takes from that mark, never
   from the text of remarks, whether a contradiction came out only after the code was written.
   PL: Recenzent oznacza każdą blokującą uwagę jako sprzeczność z ustaleniami albo nie — sprzeczność to
   rozjazd z wpisem fundamentu albo z ustaleniem z dokumentu zadania, nigdy niedokończony punkt *To do* —
   a audyt procesu bierze z tego oznaczenia, nie z treści uwag, czy sprzeczność wyszła dopiero po
   napisaniu kodu. *Rejected* holds the three *Not chosen* of questions 1 and 2. No pair of examples.
2. **WAY-405** (new, section "Process audit") — `row 4`.
   EN: The reason of a discarded attempt stands at the start of the item *Discarded attempt* as
   `reason: ` and one of three markers in backticks, and the audit takes its answer from the marker
   alone, never from the text of the item, so that an item with no marker gives unknown.
   PL: Powód porzuconej próby stoi na początku pozycji *Discarded attempt* jako `reason: ` i jeden z
   trzech znaczników w odwrotnych apostrofach, a audyt bierze odpowiedź tylko ze znacznika, nigdy z
   tekstu pozycji, więc pozycja bez znacznika daje `unknown`. *Rejected* holds the two *Not chosen* of
   question 5. No pair of examples.
3. **WAY-337**, a new second paragraph — `row 2`.
   EN: The item *Review rounds* also takes an entry for a review that passed with no fix, opened with
   `review`, holding `PASS` and the report's path; it is no fix round for the cost and the share, and the
   audit reads it as a round with no contradiction.
   PL: Pozycja *Review rounds* przyjmuje też wpis przeglądu bez poprawek, otwierany słowem `review`, z
   wynikiem `PASS` i ścieżką raportu; nie jest rundą poprawek dla kosztu i udziału, a audyt czyta go jako
   rundę bez sprzeczności. *Rejected* gained the two *Not chosen* of question 3; the *Rationale* gained
   two sentences; *Verification* gained a `tests:` clause, its pair of examples is as it was.
4. **Part map, `process-audit`, field *Trust boundary*** gains `process-audit/record_items.py` — `the
   cycle's`.
   EN: The module that now reads the items of the records taken from git history stands beside
   `audit_count.py` as a trust boundary of the part, so a change to it is checked for crafted input.
   PL: Moduł, który teraz czyta pozycje zapisów z historii gita, stoi obok `audit_count.py` jako granica
   zaufania części, więc zmiana w nim jest sprawdzana pod kątem spreparowanego wejścia.
   It follows from the move (WAY-11) and no row carries it; no pair of examples was added.

Settlement row 3 is code only (`record_items.py`, `read_contradiction`), no entry. No pair of examples
was added to any entry, so there is nothing to quote under an entry in the description.

## Choices I made, with the way rejected and the cost if wrong

1. **The part moved out first (WAY-365, WAY-385):** the reading of the two items, with the helpers it
   uses (`header_field`, `is_report_file`, `REPORT_FILE`, `item_texts`, `item_count_reason`,
   `item_words`, `reads_none_first`, `review_rounds`, `read_contradiction`, `phrase_starts`,
   `denied_before` and their constants), 180 lines, into `process-audit/record_items.py`. Reason: the
   change touches exactly this reading, so the addition lands in a module of 243 lines under the
   threshold, while `audit_count.py` stays at 3143 lines (it was 3310; the invariant
   `function-and-file-size` stays violated, which one move cannot cure). Tests that cover the move:
   `python -B gate/run_tests.py process-audit`, 234 tests, exit 0 on the move commit's tree (run before
   the commit; the instruction texts were the only other change in the tree). `audit_count.py` imports
   the nine names it uses, so every name the tests and other scripts use (`audit_count.read_contradiction`,
   `audit_count.remarks_check`) still works; the one test that builds a copy of the script now copies the
   module with it. Way rejected: moving the whole reading of `cycle.md` (`process_pin`, `remarks_count`,
   `read_plan`, `read_too_large`) — more lines moved and more names for the importers, with no line of
   it touched by this change.
2. **The forms of the marks.** Discarded attempt: `reason: ` + marker in backticks, at the very start of
   the item's text (the first line, or the first line under an empty first line); a text that holds
   `reason: `` more than once gives unknown (two reasons say nothing); `none` as before. Round entry:
   `findings `<path>`, contradiction yes|no` followed by `:` or the end of the text; `review `<path>`,
   PASS` followed by `:` or the end. Rejected: the marker as a word (`size`) with no `reason: ` and no
   backticks — the first of the four examples of review #100 (`open design choice not found`) begins with
   a marker word. Cost if wrong: the template and the code change together in one place each.
3. **`yes` is read before the shape of *Discarded attempt* is judged**: a round marked `contradiction yes`
   gives `yes` also where *Discarded attempt* is missing, doubled or prose; and an entry in neither form,
   or a malformed item *Review rounds*, gives `unknown` except where *Discarded attempt* has the marker
   `open design choice` (as the old code read an open design choice with no look at the rounds). Rejected:
   `unknown` for any malformed item first — it hides a stated yes. Cost if wrong: one `yes` where the
   other item is broken.
4. **A set in place of a list for the names already seen** in `read_rounds`: the old `entry.group(1) in
   found` compared each entry with all before it, so a record of some 100,000 distinct entries (the file
   cap of 4 MiB allows about 160,000) made the reading quadratic. A test with 100,000 entries fixes it.
5. **A review entry's mark is `no` by its form** (a review that passed has no blocking finding), and the
   review entry is not tied to turns: a review path with the word `findings` in its name is not matched
   against turns by the share (only findings entries are).
6. **The field of the *Unknown values* row of a Q1 reason stays `Discarded attempt`**, as before, also
   for the reason that concerns a round; changing it would change a field the tests and the session read.
7. **`review/SKILL.md` marks only blocking findings** (what the task and WAY-404 say); the mark of a
   round is written by the leader from the findings file and from the fix review's report.

## Checks run (command, exit code)

- `python -B gate/run_tests.py process-audit` — exit 0, 257 tests (also 234 tests, exit 0, on the move
  commit's tree).
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, 1 skipped (Windows, a signal test).
- `python -B gate/run_tests.py elements/common` — exit 0, 246 tests (started a moment before the last edit of
  `foundations/decisions.md`; `foundation_check.py` below ran after it).
- `python -B gate/run_tests.py elements/part-map` — exit 0, 40 tests (and again at the end, exit 0).
- `python -B gate/run_tests.py agent-instructions` — exit 0, 37 tests, 2 expected failures (the two
  invariants marked violated, `ruff-blocking-rules` and `function-and-file-size`).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (run with `--skip-test-citations`
  before the commits and without it after them).
- Ruff, the pinned executable of the main checkout's `quality-venv`, `check --config ruff.toml --no-cache
  --ignore-noqa` on `process-audit`: 4 reports, all on code this change did not touch (`UP037` at
  `audit_count.py` 2126, 2339, 2413 and `F541` at `test_audit_count.py` 2424, the last blamed to
  `b6f800c`); no report on `record_items.py`, `test_record_items.py` or a line I wrote. (The exit code was
  not kept: the command went through `tail`.)
- Not run: the product's full gate (`python -B gate/run_tests.py` with no directory), by the handoff;
  the other directories' tests that no change of mine reaches.
- The first failing runs: the new tests were written after the code, in the same sitting, not first
  (the code and the form of the marks were settled together); I then checked each with a mutation. The
  tests are named by the break they catch below. `test_record_items.py` failed once on a test of mine
  (a duplicated findings name in the test's own data), fixed in the test; no other check failed and passed
  on a rerun.

## The own-work check (WAY-164)

- **The requirement most likely not met:** *To do* 5 and settlement row 3 — a round entry without a mark gives
  Q1 `unknown` with the one reason, "in a record from before the change and after it", in place of the
  old reason, and the real archive of records still reads without a crash.
- **The check:** `python -B .runs/author/real_records.py` (a script of mine, since removed), which reads the last
  copy of each of the 103 records of `docs/task-cycles/*/cycle.md` in this repository's history with
  `record_items.read_contradiction` and `review_rounds`.
- **What it showed (exit 0):** 103 records: Q1 `no` for 4, `unknown` for 99. The reasons: 62 times `the item
  `Review rounds` does not give its entries...` (older records with no item or an item in prose); 26 times
  the one reason `the entry of a round does not say whether there was a contradiction` (older entries
  opened with `findings`, no mark); 10 times `the record holds no item `Discarded attempt``; 1 time
  `holds no marker of its reason` (a record with prose in *Discarded attempt*). No `yes`, no crash, as the
  task's *Context* says of such records. `test_audit_count.ProcessVersions
  .test_a_round_marked_as_a_contradiction_gives_yes_and_an_unmarked_round_unknown` holds the same on a built
  history: the form of an entry before the mark and an entry with the mark `maybe` give one pair of
  *Unknown values* with count 2 and that one reason.

## Tests, and the break each catches (in the head and by mutation)

I mutated `record_items.py` eight times and ran `test_record_items`: the check of two markers removed,
the lookahead after the mark removed, a review entry counted as a fix round, a `yes` of an entry ignored,
the review entry's mark made `None`, the marker searched anywhere in the text, an unmarked entry read as
`no`, and the marker `size` read as a yes — every one caught (script output, since removed). Not
caught by a test: a mutation that replaces the set of names with a list is caught only by time (the
100,000-entry test would not finish); the test has no time limit by the testing guidelines.

New tests: `process-audit/test_record_items.py` (20 tests: the marker at the start; the four examples of
review #100; text not in the form; two markers; a missing or doubled item; a fenced item; each form of an
entry; a mark that runs on; entries deeper, fenced or in another item are not read; a malformed item
*Review rounds*; 100,000 entries; `review_rounds` gives findings files only); in `test_audit_count.py`: the
markers through the command (`test_the_marker_of_a_discarded_attempt_gives_q1`), the four examples through
the command, a marker not at the start, crafted discarded attempts and crafted round entries (no cell of
the result holds a control character), the marked and the unmarked round, the share with entries of reviews
that passed (three forms), reviews alone give a share of `0.0%`, and a record with no item *Discarded
attempt* or no item *Review rounds*.

Changed or deleted existing tests (cause: the requirement, *To do* 6 and question 5; evidence: the task
document): `test_a_discarded_attempt_that_denies_a_design_choice_is_not_read_as_one`,
`test_the_templates_own_form_of_a_discarded_open_design_choice_reads_yes`,
`test_a_denial_stands_only_where_it_comes_just_before_the_phrase`,
`test_crafted_discarded_attempts_break_no_cell_and_no_pattern`,
`test_a_discarded_attempt_opening_with_none_is_not_read_as_a_design_choice` and
`test_a_review_round_with_discarded_none_leaves_the_question_unknown` are replaced by the tests above (the
denial detection is gone, so the cases of the first three have no behaviour left to test); the reading-a
cycle of `test_the_questions_read_the_record_items_and_say_unknown_otherwise` now writes the marker. No
invariant's test changed.

## Questions and concerns (for the orchestrator)

1. **Concern — the missing items of `cycle.md` and WAY-344.** The handoff says that where a reading of a
   file is reworked, WAY-344 binds the whole reading and each reading has one test with a missing field
   that asserts the failure naming it. For `cycle.md`, the code reads each item missing from a record as
   `unknown` with a reason naming the item and exit code 0, never as `Error:` with exit 1 (the old reading
   did the same for `Discarded attempt`, `Review rounds`, `Plan`, `Slices returned too large` and the
   remarks, and every test that builds a record without items depends on it). I kept that: a record of an
   earlier form lacks items, the records the command reads from history are of many forms, and the record
   has no sign that names its form. The tests that give the file without `Discarded attempt` and without
   `Review rounds` assert the reason that names the item and the exit code 0
   (`test_a_record_without_the_item_discarded_attempt_or_review_rounds_gives_q1_unknown`,
   `test_a_missing_or_doubled_item_gives_unknown_with_its_reason`). Recommendation: keep; a hard error for a
   missing `Discarded attempt` would make most records of the archive end the run with exit 1, and WAY-344
   names no form of `cycle.md` as one that has the field. Cost if wrong: a reviewer asks for `Error:` lines
   for the record, a change of the reading of every item at once.
2. **A value that did not pass my reckoning:** the task's *Context* says 252 commits changed
   `docs/task-cycles/*/cycle.md` and the record of the the-way holds forms of both items; I found 103 records
   (last copy of each folder) in this repository's reachable history. It changes nothing in the code.
3. The words of *Questions to settle* 1 say "przerwanie serii kosztu" (the count's series) is accepted: the
   change to `task-cycle/review/SKILL.md` starts a new series of the count of remarks (WAY-339) and does not
   start a series of the cost; `COUNT_PATHS` and `TREE_PATHS` stand as they were, no change was needed.
4. The glossary holds no entry for "settlement" or "marker"; I used `contradiction with the settlements`
   with its three sources spelled out in WAY-404 and in the review method. `foundation_check.py` reports
   nothing; I added no glossary entry (the words are the task's own, *Settlements to record*).

## Reaches beyond the handoff

- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md`, `elements/decisions/template.md`,
  `elements/common/rules.md` — read for writing the decisions (the foundation step names the skill of the
  element; its files were not in the handoff's list).
- `foundations/part_map.md` (the `process-audit` entry), `elements/part-map/template.md` (the section "Trust
  boundary") and `elements/part-map/skill/SKILL.md` — for the one-line change of the trust boundary.
- `foundations/decisions.md` WAY-135 (whole), read to write the new entries' *Relations* and rationale — it
  was in *Decisions in play*, not in the handoff's list of selected decisions.
- `agent-instructions/test_linter_invariant.py` and `ruff.toml`, to find how the linter is run; the
  pinned `ruff.exe` of the main checkout's `.runs/quality-venv` was run as a program (the test itself reads it
  there).
- `foundations/glossary.md` (the entries `foundation step`, `open design choice`, `reserved choice`).

## Working copies

My directory `.runs/author/` of the worktree held the scripts of the move, scratch outputs of the test runs
and `real_records.py`. It stood at `.runs/author/`
and was removed before this return. No worktree or clone was made.

## Unread material

- `foundations/decisions.md`: WAY-162 I read in part (up to its first *Verification* lines), WAY-294 in part (up to its
  *Rationale*), WAY-229 and WAY-260 not at all. The handoff names them; none bears
  on a line of the change as far as I saw.
- The invariants of the parts `task-cycle` and `process-audit` I read are the ones listed by a search of
  the *Part* line (`record-copy-*`, `blocked-request-*`, `audit-series-script-paths`, `review-tag-pattern`,
  `ruff-blocking-rules`, `function-and-file-size`, `cycle-*`, `gate-times-*`, `audit-count-refuses-record-links`);
  those whose *Part* is `every` I read only where named (`script-imports`, `cross-part-imports`).
- `guidelines/coding.md`, `coding-measuring-report.md`, `testing.md`: read whole.
- `task-cycle/skill/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/record_template.md`,
  `task-cycle/skill/reserved_return.md`, `process-audit/SKILL.md` (lines 25 to end), `process-audit/audit_count.py`
  (the docstring, the constants, the reading of the items and its callers, and the whole of what I
  moved; the rest of its 3300 lines I did not read), `process-audit/test_audit_count.py` (the helpers, the
  classes `Cost` and `ProcessVersions` in the parts that bear on this change; the other classes I did not read).
- The private note of the audit named by the task (`audit-2026-11-14.md`, "Sprawa 4") and the vault's other
  notes: not read, as the handoff places the task's text before them.

## Searches not found or unclear

- The sentence of WAY-344 about "the whole reading of a file" does not say whether a record's missing item is
  a missing field or an earlier form of the record: I could not tell from the sentence or from the
  `Verification` of WAY-344 how the command reads `cycle.md` (see concern 1).
- The glossary holds no entry for the words "settlement" and "mark"; I found none (`grep` of the glossary's
  headings).
- I could not find a place in the instructions that tells the cycle's leader to write the round's entry
  when a round ends: `task-cycle/record_template.md` gives its form, and the paragraph of `task-cycle/skill/SKILL.md`
  on the findings file now says how the mark is set, but no step names the moment the entry is written; I
  left that as the template and the existing paragraph give it.
