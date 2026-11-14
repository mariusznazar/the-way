# Author report: service-reading-and-invariant-condition

**Status:** done

**Commits** (branch `task/service-reading-and-invariant-condition`, base `0e1cd3c`):

- `19efdfd` Give the reading as a source for a setting on another's service, and name the place of an invariant's condition
- `8680824` Test that the foundation check reads a fact whose source holds a command of several lines in a code block

## Files changed (added / removed lines against the base)

| File | + / - |
|---|---|
| `foundations/decisions.md` (WAY-80, WAY-84, WAY-60, WAY-35 *Verification*) | 68 / 31 |
| `foundations/invariants.md` (new entry `elements-no-pending-marker`) | 10 / 0 |
| `elements/common/test_elements_pending_marker.py` (new test of the invariant) | 44 / 0 |
| `elements/common/test_foundation_check.py` (test for the carried question) | 16 / 0 |
| `elements/environment-facts/template.md` | 30 / 14 |
| `elements/environment-facts/skill/draft.md` | 9 / 5 |
| `elements/invariants/template.md` | 3 / 3 |
| `README.md` (list of elements and the `environment_facts.md` row) | 4 / 3 |

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check, after the entries and the test were in the index | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Invariant test, passing | `python -B -m unittest elements/common/test_elements_pending_marker.py` | 0 |
| Gate of the directory I changed | `python -B gate/run_tests.py elements/common` | 0 (201 tests, OK) |
| Private paths of tracked files | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (`checked: 298 files, 0 listed`) |
| New foundation_check test | `python -B -m unittest elements/common/test_foundation_check.py -k test_fact_source_with` | 0 |

Not run: the full gate (the orchestrator runs it); `agent-instructions/skill_entry_points.py --write` (no skill added, renamed, moved, or its description changed: only `elements/environment-facts/skill/draft.md` text changed).

### The invariant's test, failing and passing (WAY-08)

- Failing, before the markers left the templates (written first, with the real tracked files):
  `python -B -m unittest elements/common/test_elements_pending_marker.py` exit 1,
  `AssertionError: Lists differ: ['elements/environment-facts/template.md:137', 'elements/invariants/template.md:82'] != []`.
- Failing again after the change, on a seeded text (appended `decision` + line break + `pending` to the tracked `elements/common/rules.md`, restored with `git checkout -- elements/common/rules.md`, never committed):
  same command, exit 1, `['elements/common/rules.md:92']`.
- Passing, on the committed tree: same command, exit 0.

## Own-work check (WAY-164)

Requirement most likely unmet: the invariant's test must fail when a tracked file under `elements/` holds the text, and the foundation check must read a fact with a multi-line command under *Source*. The checks above show: the test fails on the two real markers and on a seeded one (also when the two words are split by a line end), and passes once the markers are removed; the foundation check passes on a fact whose *Source* has an indented code block with lines starting `#`, `##` and `- **Source:**` (see the carried question).

## Answer to the carried question

`elements/common/foundation_check.py` **does read** a fact entry whose *Source* has a code block with a multi-line command under it. Run in a scratch copy of the tree (not committed) on a temporary entry: a *Source* line `reading: the command below on ...`, a blank line, then a code block indented two spaces holding a `#` comment, a command continued with a backslash and a pipe, a line `  ## second` and a line `  - **Note:** x`: `python -B elements/common/foundation_check.py` printed `0 errors`, exit 0. Cause, verified in the code: the check reads a heading only from a line that starts with `#` in column 0 (`blocks`) and a field only from a line that starts with `- **` in column 0 (`FIELD`), so indented lines of the block are continuation or ignored text. The limit: a block **not indented** to the item breaks the check: with `## second` moved to column 0 the same run printed `the entry lacks *Source*`, exit 1 (the line was read as a new entry heading). No fix to the check was needed; the template already says the block is "indented to the item". I added `test_fact_source_with_a_command_of_several_lines_in_a_code_block` in `elements/common/test_foundation_check.py` (the break it catches: a change of `blocks` or `fields` that makes indented lines of a block read as headings or fields, a bug). The test does not cover the not-indented case, which stays an error by the template's form.

## Differences between the task's quotation of a decision and the log as it stands

- WAY-80, WAY-84, WAY-60, WAY-82, WAY-35, WAY-328: the task's quoted wording equals the log at `0e1cd3c`. PR #120 did not change those entries (checked with `git diff f749cfc 0e1cd3c` over `foundations/decisions.md`, the two templates and `README.md`).
- The task quotes WAY-84's binding sentence as ending "...where that state is shown."; the log continues with two more sentences (a choice of such a setting; visibility of a linked repository). Unchanged by me beyond the first sentence.
- WAY-58 is quoted by the task from the invariants template, not from the log; the template's quoted point stands unchanged.
- PR #120 form: the `decision:` lines of a test (and the clause `tests:` of *Verification*). None of my entries needs such a line: WAY-80, WAY-84 and WAY-60 keep their `complies` / `violates` pairs (I extended each pair for the change); WAY-35 names the new invariant in *Verification*. The foundation check reports `0 errors` and lists nothing.
- Invariants template: PR #120 changed the *Fields and their readers* row of *sentence*; my change touches no sentence of an existing invariant.
- Task text says "Szablon faktów ... punkt o odczycie w „A source takes one of three forms" ...": the template as it stands is as the task describes; the dangling bullet quoted in the task is replaced as item 4 says.

## Foundation entries written (WAY-134; meaning in English and in the task's language, mark)

1. **WAY-80, changed in place — mark `row 1`, `row 3`, `row 4`.**
   - EN: A state of a host the product's people run, or of a setting they set on another's service, which no page open without their access shows, has for its source a reading: one invocation quoted word for word however many commands and lines it holds (a command of several lines in a code block), naming the command or the API call, the host or the service, each tool its result depends on with its version, the output (or the lines the sentence rests on) and the date; the quoted output holds no secret because the command reads only the fields the sentence rests on.
   - PL: Odczyt jest źródłem także dla ustawienia w cudzej usłudze; to jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało (wielowierszowe w bloku kodu), z wersją każdego narzędzia; cytowany wynik nie zawiera sekretu, bo polecenie czyta tylko pola, na których stoi zdanie.
   - *Rejected* gets the ways not chosen that the task keeps for rows 3 and 4 (marker over a secret; rule only in template and skill; one command per fact; one backticked fragment), each with its cost; its old "a reading of a host that a check reruns" reads "of a host or a service" (my choice, see below). *Rationale* and the *Verification* pair extended.
2. **WAY-84, changed in place — mark `row 1`, `row 2`.**
   - EN: A setting people of the product change outside the repository is a fact whose source is the place showing its state, or, where no page open to a reader shows it, a reading (WAY-80); what *Rejected* turns down is a repeated reading (on a change or by a clock), not the one reading quoted.
   - PL: Ustawienie zmieniane poza repozytorium ma za źródło stronę, która je pokazuje, a gdy żadna strona otwarta dla czytelnika go nie pokazuje — odczyt (WAY-80); odrzucony jest odczyt powtarzany, nie jeden zacytowany.
   - *Rejected* also gets the two ways the task keeps under row 1's question (page without edition and archive copy; no fact until the product needs it).
3. **WAY-60, changed in place — mark `row 5`.**
   - EN: An invariant whose condition stands outside its sentence names, by identifier, the entry or decision that holds the condition: in a field where the template gives one, otherwise in its sentence.
   - PL: Niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje identyfikatorem wpis albo decyzję, która go trzyma — w polu, jeśli szablon takie daje, a inaczej w zdaniu.
   - *Rationale* gets the reason (whoever changes the holder finds the invariant); *Rejected* gets the two not-chosen ways of the task's question; the pair gets one example each.
4. **Invariant `elements-no-pending-marker` (`foundations/invariants.md`) — mark `row 6`.**
   - EN: No file git tracks under `elements/` holds the text "decision pending". Method `test`; Rests on `none`; Derives from WAY-35; Part: decisions · part-map · invariants · glossary · environment-facts · elements-common (every part whose files stand under `elements/`); Violated `no`.
   - PL: Żaden plik, który git śledzi pod `elements/`, nie zawiera tekstu „decision pending".
   - WAY-35's *Verification* now names it (`invariants: skill-rule-source · elements-no-pending-marker`), as WAY-61/others name theirs.

Template and skill text (no decision): item 4 (facts template opening paragraph, the *Source* form line, the three-forms bullet, the setting bullet in *Which facts are written*, the replaced `TODO` bullet citing WAY-80 and WAY-84, the skill's *Source* step, the two `README.md` places), item 5 in the facts template (reading is one invocation; code block indented to the item; versions; no secret), item 6 (code under a fixed commit: symbol, one statement or line, whitespace collapsed, ` · `, “…”), item 7 in the invariants template (the marker gone, the rule cites WAY-60).

## Choices, with the way rejected and the cost if wrong

- **Test place:** `elements/common/test_elements_pending_marker.py` (part `elements-common`), not `gate/` or a new directory: the gate already runs every directory with a `test_*.py`, and the file's neighbours are the foundation tests. Rejected: `gate/` (that part answers for the runner). Cost if wrong: moving a file and its citation.
- **The test matches `decision\s+pending`** (two words split by a line end or several spaces count) and is written as a pattern so the file, itself under `elements/`, does not hold the text. Rejected: a literal single-space match (a wrapped marker would pass). Cost if wrong: a legitimate wrapped use of the two words fails the test; none exists today. It is case-sensitive, matching the sentence.
- **Invariant sentence uses straight quotation marks** around "decision pending" (quoted text per the template), not backticks, as the task wrote it in backticks only in its own prose.
- **Q1's not-chosen (b), (c) went to WAY-84's *Rejected*; Q3's and Q5's not-chosen went to WAY-80's;** Q2's to WAY-60's. Rejected: all in one decision. Cost if wrong: the reader looks in the neighbour decision.
- **WAY-80's *Rejected* "a reading of a host that a check reruns" now reads "of a host or a service"** and **WAY-80/WAY-84's *Verification* pairs got examples for the changed sentences**, beyond the task's letter, because the unchanged wording would contradict (a reading now also of a service) or leave the new sentences unchecked. Cost if wrong: a deleted clause.
- **WAY-80's binding paragraph now has five sentences** (it had four, already past the template's one to three); I did not restructure it. The foundation check does not count sentences. A restructure is a separate decision for the human.
- The new `WAY-84` binding sentence refers to WAY-80 in the binding part, as the task's wording (B2 (a)) asks.
- Added a test for the carried question although the check did not fail, since the template now promises the form; it pins the answer.

## Reaches beyond the dispatch (section 1)

- `elements/invariants/skill/decide_entry.md`, `draft.md`, `write.md`, `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/environment-facts/skill/write.md`: read whole, because `SKILL.md` of the invariants and decisions elements names them for the foundation step (step 1 of each skill).
- `elements/common/foundation_check.py` (parts: `blocks`, `fields`, `FIELD`, the check of fields) and `elements/common/test_foundation_check.py` (the `Product` helper and neighbouring tests): read to answer the carried question and write its test.
- `task-cycle/test_tracked_files_private_paths.py` (the form of the example the handoff names), `gate/run_tests.py` head (to know how the directory is run).
- Search of the foundation after the entries (WAY-33): terms "people run", "a reading", "reading:", WAY-80, WAY-84, WAY-60, "access to the host", "own server" across all Markdown and Python files; entries found and read: `product-guidelines/styleguide/settle.md` and WAY-191 (cite WAY-80 for a fact's source, unaffected), WAY-92's text on a source form (unaffected), `elements/environment-facts/skill/write.md` (a reading's output is the output of the run: still true), glossary (no entry for "reading"). No invariant of the-way derives from WAY-60, WAY-80 or WAY-84, so none needed correction. Nothing further was found to change.

## Unread material

- WAY-07 (edit a decision in place), WAY-33 (the search after a settled entry) and WAY-328: not read as entries; I know them from their uses in the templates, `way_of_working.md` step 2 (WAY-33) and the task's quotation (WAY-328). The change does not touch them.
- The glossary entries of the terms used: not opened.
- The examples of the invariants and facts elements (`examples.md`, which the step 1 of `way_of_working.md` names): not read; I took the form from the templates and from the entries of `foundations/invariants.md` printed above.
- `README.md`: read lines 1-80 and the two places I changed; the rest only through the diff against the earlier base.
- Read whole: WAY-80, WAY-84, WAY-60, WAY-35, WAY-82, WAY-58, WAY-61; the invariants `tracked-file-private-paths`, `skill-rule-source`, `test-method-citation`, `element-directory-contents`; both templates and the draft of the facts skill; `foundations/part_map.md`; the task and the method.

## Searches not found or unclear

- The handoff names `elements/environment-facts/skill/draft.md` for the skill's *Source* point; the point is in that file, found at once.
- Unclear: the template's rule that a decision's binding paragraph holds one to three sentences, against WAY-80's existing four; the foundation check does not enforce it (see the choice above).
- Not found: a glossary entry for "reading" (the term is used in the decision's sense, as it already was).
