# Author report — defects-found-after-merge

## Status

`done with concerns` (concerns below; no question blocks the work).

## Commits (base `6814c6f`, branch `task/defects-found-after-merge`)

- `4fcec13` — templates and skills: task document line, record item, request item 17, register classes
- `aea8c2c` — foundation: WAY-353 to WAY-357 written, WAY-287 changed in place
- `15b1041` — two tests (record template item and remarks readers)
- `10c0f9e` — fix of one assertion of the audit test (see Checks)

Files, added/removed lines (`git diff --numstat 6814c6f HEAD`): `foundations/decisions.md` 190/4;
`process-audit/problem_register.md` 13/2; `process-audit/test_audit_count.py` 9/0;
`project-level/task/skill/draft.md` 10/0; `project-level/task/template.md` 14/1;
`task-cycle/record_template.md` 17/0; `task-cycle/skill/correction.md` 20/3;
`task-cycle/skill/request_template.md` 7/1; `task-cycle/test_remarks_check.py` 25/0.
No skill description changed, so `.claude/skills/` and `.agents/skills/` were not touched and
`skill_entry_points.py --write` was not run.

## What was made

1. `project-level/task/template.md`: header line `Defect introduced by:` under `Project relation:`, and
   a paragraph that gives its form, the rule of the fixing task (WAY-353), who fills it, and that a
   missing line means "not assessed". `project-level/task/skill/draft.md`: a paragraph that has the
   refining agent fill the line in every task (step 2 is common to the plan-member, source-only and
   independent routes, so one place serves all).
2. `task-cycle/record_template.md`: item `Corrections after the request opened` in *Request handoff*,
   before `Process remarks on the-way` (which stays last), with a paragraph on the pairs.
   `task-cycle/skill/correction.md`: the remarks are written word for word to
   `reports/correction-<n>-remarks.md` also when they came in conversation or concern only the refresh of
   the target branch; a paragraph tells the orchestrator to add the correction's line, with source and
   kind rules; the rewritten `request.md` carries the pairs as item 17.
3. `task-cycle/skill/request_template.md`: new kind **17** in *You accept by merging* after kind 15, and
   the correction row of the variants table names it.
4. `process-audit/problem_register.md`: classes `defect-found-at-request` and `defect-found-after-merge`
   (Added `start`), a bullet that sends `item · defect` to `known-problem-left`, and sentences for
   *Record* and *Stages* of both rows (`after the merge`, `at the request`). The counting command was
   not changed.

## Foundation step (skill `the-way-record-decision`, read through its `SKILL.md` and
`elements/decisions/`)

Search of the whole foundation (WAY-33): searched `foundations/decisions.md`, `invariants.md`,
`part_map.md`, `environment_facts.md`, `glossary.md` for `defect`, `introduced by`, `after the merge`,
`found after`, `Project relation`, `Request handoff`, `record_template`, `problem_register`,
`known-problem-left`, `correction`, `reports/`. No row was already stated by an entry, so no row is tied
to an existing entry. Entries that touch the change and needed no edit: WAY-330, WAY-333, WAY-335,
WAY-339 (a change of the list of classes already starts a new series), WAY-296 (the new item stands
before the remarks, which stay last), WAY-289, WAY-148, WAY-124, WAY-134, WAY-308 (the new line holds no
private path). No glossary term is written: *defect* and *correction* hold their ordinary meanings.
`elements/common/foundation_check.py --skip-test-citations .` exit 0 ("0 errors"). No invariant, part-map
entry or environment fact written.

Five new decisions, each answering one question; rows grouped by the one-question rule:

| Entry | Question | Rows |
|---|---|---|
| WAY-353 | Which task fixes a defect found after a merge? | 2 |
| WAY-354 | Where is a defect found after a merge recorded, and in what form? | 1, 3, 7, 8 |
| WAY-355 | Where does the cycle record the cause of a correction after the request opened? | 4, 9 |
| WAY-356 | What causes does the line of a correction give? | 5, 10 |
| WAY-357 | How does the template of the register of problems record a defect found at the request or after the merge? | 6, 11 |

Meaning sentences (English / Polish), marked by row:

- WAY-353, row 2. EN: A task fixes a defect found after a merge only when it removes a defect against what the earlier change's task or the foundation required at the merge, or a regression; a new need, a change of mind, a gap of the earlier task and maintenance do not count. PL: Zadanie naprawia błąd znaleziony po scaleniu tylko wtedy, gdy usuwa wadę wobec tego, czego w chwili scalenia wymagało zadanie tamtej zmiany albo fundament, albo regresję; nowa potrzeba, zmiana zdania, luka zadania i konserwacja się nie liczą.
- WAY-354, rows 1, 3, 7, 8. EN: A defect found after a merge is recorded in two places, the line `Defect introduced by:` in the header of every task document (the source, filled by the refining agent, reading `none`, the request addresses joined by ` · `, a commit address for a change that came without a request, or `unknown` with a reason) and a register class that counts it; a document written before the line has none, which means not assessed. PL: Błąd znaleziony po scaleniu zapisuje się w dwóch miejscach: w linii `Defect introduced by:` w nagłówku każdego dokumentu zadania (źródło, wypełnia ją agent doprecyzowujący: `none`, adresy próśb rozdzielone ` · `, adres commita dla zmiany bez prośby albo `unknown` z powodem) i w klasie rejestru, która go liczy; dokument sprzed tej linii jej nie ma i znaczy to „nie oceniano”.
- WAY-355, rows 4, 9. EN: The cycle record holds one line per correction after the request opened, before the process remarks, never a cause in a commit title, and the human's remarks go word for word into a file in the record's reports, also when they came in conversation or only concern refreshing the target branch. PL: Zapis cyklu trzyma jedną linię na każdą poprawkę po otwarciu prośby, przed uwagami procesowymi, a przyczyna nie stoi w tytule commita; uwagi człowieka trafiają słowo w słowo do pliku w `reports/`, także gdy przyszły w rozmowie albo dotyczą tylko odświeżenia gałęzi docelowej.
- WAY-356, rows 5, 10. EN: A correction's line gives each pair source · kind once: the source (`item <n>`, `remark`, `target-branch`) is read, with `<n>` the number of the item's kind in the request template, and the kind (`defect`, `not-required`, `none` only for `target-branch`) is the cycle leader's judgment by one test; the request shows the pairs in one sentence. PL: Linia poprawki wymienia raz każdą parę źródło · rodzaj: źródło (`item <n>`, `remark`, `target-branch`) jest odczytem, a `<n>` to numer rodzaju pozycji z szablonu opisu prośby; rodzaj (`defect`, `not-required`, `none` tylko przy `target-branch`) jest osądem agenta prowadzącego cykl jednym testem; opis prośby pokazuje pary jednym zdaniem.
- WAY-357, rows 6, 11. EN: The register template starts with two more classes, `defect-found-at-request` and `defect-found-after-merge`, sends `item · defect` to `known-problem-left`, and names for the two new rows the *Record* (last copy of the introducing cycle's record; copy carrying the correction's line) and *Stages* (`after the merge`; `at the request`). PL: Szablon rejestru zaczyna listę także od klas `defect-found-at-request` i `defect-found-after-merge`, para `item · defect` idzie do `known-problem-left`, a wiersz po scaleniu ma w *Record* ostatnią kopię zapisu cyklu, który błąd wprowadził, i `after the merge` w *Stages*, a wiersz przy prośbie kopię zapisu z linią poprawki i `at the request`.

Also changed: **WAY-287** (edited in place: binding sentence lists the pairs of a correction, the
complies/violates examples and the rationale say so). Mark: not a row and not `the cycle's` by my
reading — the task names this change under *Decisions in play* ("Zmiana, którą wprowadza zadanie"), so
the human accepted it with the task document. The orchestrator decides whether it goes under kind 6 of
the request. EN: The section for the human's decisions also holds the cause of a correction after the
request opened. PL: Sekcja decyzji człowieka trzyma także przyczynę poprawki po otwarciu prośby.

*Rejected* of each entry takes the *Not chosen* of the question named by the rows' *Source*; rows 7, 8,
9, 10 and 11 name *To do* items, which keep no ways, so they add nothing to *Rejected*. The *Verification*
example pairs and the *Rationale* sentences are my wording from the rows and their questions; none
adds a rule.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0, "0 errors".
- First runs on the tree before the commits (all with `python -B gate/run_tests.py <directory>`):
  `task-cycle` exit 0 (367 tests); `process-audit` exit **1** (180 tests, 1 failure: my new test
  `Remarks.test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries` asserted
  an empty *Unknown values* table, which holds other fields in that fixture; the remarks count itself
  was `1` as expected); `project-level` exit 0 (275 tests); `elements/common` exit 0 (144 tests);
  `agent-instructions` exit 0 (18 tests).
- After the fix of that assertion (commit `10c0f9e`, now `assertNotIn("Remarks", ...)`), runs on the
  final tree: `python -B -m unittest -k corrections_item test_audit_count` (in `process-audit/`) exit 0;
  `python -B gate/run_tests.py process-audit` exit 0 (180 tests OK); `python -B gate/run_tests.py
  task-cycle` exit 0 (367 tests OK, after the last re-wrap of `correction.md`). The other three
  directories were run before the test fix and the re-wrap only, with nothing in them touched since.

Not run: `python -B gate/run_tests.py` with no argument (the orchestrator's), the return step, any review.

## Tests written

- `task-cycle/test_remarks_check.py`: `CommandTest.test_a_corrections_item_and_a_file_of_the_humans_remarks_change_nothing`
  (a record in the template's request-handoff form with the corrections item and a
  `correction-1-remarks.md` file beside a stage report: exit 0, nothing listed, 2 reports read) and
  `TemplateTest.test_the_corrections_item_before_the_remarks_is_no_part_of_their_block`. Break they
  catch: the corrections item put after the process remarks, or into their block, and a file of the
  human's remarks that the check cannot read as a report. Mutation run: the item moved after the
  remarks item in the template, `python -B -m unittest -k corrections test_remarks_check` (in
  `task-cycle/`): exit 1, the template test errors with `ValueError: substring not found` (an error
  at the order assertion's index call, not an assertion; the reason is the intended one — the order);
  restored, exit 0. These two passed on first run because they test a form the readers already
  accept (the audit test below failed once for a wrong assertion of mine, see Checks); the first-failing-test rule does not fit (prose and template change, no new code).
- `process-audit/test_audit_count.py`: `Remarks.test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries`
  (count of remarks 1 beside a corrections item with two lines, no *Unknown values*). Break it
  catches: the remarks count reading the lines of the item before it.

## Own-work check (section 3 of the method)

Requirement most likely not met: "the readers still read the forms" — Q2 of the orchestrator (the
record's new item must not disturb `remarks_check.py`, the nightly cut and `audit_count.py`) and the
description of a corrected request with item 17 in *You accept by merging* must pass the form check.
Checks: the two new tests above and the existing ones of `task-cycle` and `process-audit`; a scratch
script (`.../scratchpad/own_check.py`, outside the repository) that builds a description from the
form check's own fixture with item 17 alone in the third group and runs `request_check` on it
(0 problems), and runs `plan_state.header_fields` on the new template header (1 `Project relation`
field, 1 `Defect introduced by` field): `python -B -X utf8 own_check.py` exit 0. Showed: no reader
breaks. The nightly review itself (the user's tool) is not in the repository and was not run.

## Choices and rejected ways

- Name of the file of the remarks: `reports/correction-<n>-remarks.md`, `<n>` from 1 (the pattern the
  game's cycles use, per the task's *Context*). It holds neither `handoff` nor `findings`, so
  `remarks_check.py` reads it as a report and, having no section, it gives no item; the name with
  `findings` would be taken as a findings file. Rejected: any other name; cost if wrong: a rename in
  `correction.md` and the template.
- Pair separator in the line: `, ` (a pair holds ` · `). Rejected: ` · ` between pairs (ambiguous).
- Kind 17's sentence is written from the pairs "in plain words" with no item numbers (the top part of
  a description holds no identifiers); the template says so.
- WAY-354 binds the line's form, who fills it and the two places; the definition of a fixing task
  stands once, in WAY-353 (one home for a fact); WAY-356 refers to WAY-353 for the kind test.
- `Based on: none` and `Origin: none` in all five: the sources are the human's answers and a task
  document, which are no source outside the product and, by the template, no *Origin*.
- Relations: WAY-353 `none`; WAY-354 derives from WAY-330; WAY-355 derives from WAY-148; WAY-356 derives
  from WAY-355; WAY-357 derives from WAY-330 and WAY-333. Rejected: deriving WAY-354 from WAY-353
  (the second only defines a term the first uses).

## Concerns

1. "Pary tej poprawki": the description after correction n shows the pairs of that correction only
   (row 5 and *To do* 3 say so), so a description after a second correction no longer shows the first
   one's pairs, though the record keeps both lines. If the human wants every correction shown, kind 17
   would say "of each correction"; I followed the words.
2. Item 17 now makes *You accept by merging* non-empty after any correction, including one for the
   refresh of the target branch alone (`target-branch · none`); WAY-287's complies example speaks of a
   correction made for a remark only as an example, not a limit.
3. The kind test (`defect` / `not-required`) is the orchestrator's judgment from the documents; the
   record template and `correction.md` repeat WAY-353's criterion by reference instead of copying it.
4. WAY-287 is edited, as the task's *Decisions in play* says; its *Rejected* is untouched.
5. WAY-354's rationale and WAY-357's rejected way name "the nightly review", which is the user's own
   tool (WAY-330 says a user's tool fills the register); taken from the source's *Not chosen* wording.
6. Human actions of the task (the user's register classes, the nightly review reading the new line)
   are not made by me and not by the cycle; they stay for the request's kind 3 items.

## Reaches beyond the handoff

- Read `elements/decisions/template.md`, `elements/decisions/skill/*.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md` (the method of the skill named in the handoff).
- Read `task-cycle/skill/SKILL.md` passages on the record, the remarks and the cleaning of the copy
  (lines 60-100, 140-170, 440-634), `task-cycle/remarks_check.py` lines 270-340,
  `process-audit/audit_count.py` lines 288-360 and 690-722, `project-level/plan_state.py` `header_fields`,
  `project-level/task/skill/SKILL.md`, `foundation-review/with_the_human.md` (the passage that makes
  tasks with `Project relation:`; unchanged, as the new line is left to refinement), and
  decisions WAY-334, 342, 343, 345, 346 (read whole, as process-audit decisions) — to check that the
  readers and the audit's decisions still hold.
- Read the user's `the user's global rule on writing scripts` (global instructions); no
  private path enters any committed file.

## Unread material

- Decisions named by the handoff and read whole: WAY-330, 333, 339, 287, 296, 289, 335, 286, 288, 290,
  292, 148, 294, 295, 306, 337, 124, 134. Not read: the handoff names "every decision whose *Scope* names
  `process-audit`"; I read whole WAY-330, 333, 334, 335, 337, 339, 342, 343, 345, 346 and 352. Not
  read at all: the remaining decisions of that scope (WAY-331, 332, 336, 338, 340, 341, 344, 347 to
  351; WAY-344 only through its mention in WAY-294), chosen by title as concerning the price list, the
  schedule, the results' place and the measures of context, which the new classes and columns do not
  touch.
- Invariants: read whole `return-step-record`, `derived-file-content`, `tracked-file-private-paths`,
  `script-language`, `foundation-file-kinds`. Glossary read whole. Part map: read `project-level`,
  `task-cycle`, `process-audit` entries (lines 77-125).
- `agent-instructions/README.md` and `task-cycle/skill/foundation_step.md` read whole;
  `task-cycle/change/SKILL.md` read whole.
- Task document read whole.

## Searches not found or unclear

- The handoff says to check "that the nightly cut of the remarks ... still read the template's form";
  the nightly review is the user's tool outside the repository, so I could check only
  `remarks_check.py` (whose cut the nightly review is said to follow) and `audit_count.py`, not the
  tool itself. Unclear whether the nightly cut reads exactly as `remarks_check.remark_blocks` does.
- The handoff names `project-level/task/skill/` "the file that fits — `draft.md` is the likely place";
  no file of the skill lists the header lines of the task document, so `draft.md` is a judgment, not a
  found place.
- No decision or glossary entry states the term "fixing task" or "correction"; I used them in their
  ordinary meaning.

## Problems observed

- `python -B -I` ignores `PYTHONIOENCODING`, so a helper that printed decision text came out with
  replacement characters (my helper's problem; the files are UTF-8, `foundation_check` exit 0).
