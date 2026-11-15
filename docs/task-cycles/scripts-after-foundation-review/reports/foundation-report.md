# Report — foundation entries, task `scripts-after-foundation-review`

**Status:** done

## Commits (task branch `task/scripts-after-foundation-review`, base `7f5c5a5`)

- `da9d816` — `foundations/decisions.md`: WAY-339 and WAY-344 rewritten in place; one wording fix in WAY-321 (see the corrections below). Over both commits `git diff 7f5c5a5 --stat` gives 175 added and 54 removed lines in five files.
- `bfb774c` — the glossary term `Markdown file` in `foundations/glossary.md`, and the corrections of the uses that meant `.md` alone: `foundations/glossary.md`, `foundations/invariants.md`, `elements/decisions/template.md`, `elements/invariants/template.md`.

I committed the entries in two commits and not one for each entry: WAY-339, WAY-344 and the WAY-321 wording sit in one file, and `git add -p` is not available here.

## The entries

### WAY-339 — `foundations/decisions.md`, heading `### WAY-339`

- `row 3`. EN: the cost of cycles and the count of remarks are compared in two kinds of series — a series of the cost starts only with a new price list or a change of `task-cycle/cycle_stages.py`, a series of the count of remarks starts wherever one of the cost does and also with a change of the form of a stage report, of the list of classes or of the instructions of the reviewer; the *Rationale* names the price (the audit cannot tell "the reviewer found more" from "the process got dearer"). PL: koszt cykli i liczba uwag są porównywane w dwóch rodzajach serii — serię kosztu zaczyna tylko nowy cennik albo zmiana `task-cycle/cycle_stages.py`, serię liczby uwag zaczyna wszystko to, co serię kosztu, a także zmiana formy raportu etapu, listy klas i instrukcji recenzenta; *Rationale* nazywa cenę (audyt nie odróżni „recenzent znalazł więcej" od „proces zdrożał").
- `row 4`. EN: a cycle whose own change changes a tool that measures (the script that measures the cost, the one that counts the measures of context and cache use, the one that records the gate times, the test runner of the process) gets the measures of that tool as unknown with the reason that the cycle changed the tool; its other measures stand under the version it ran on. PL: cykl, którego zmiana zmienia narzędzie pomiaru (skrypt kosztu, skrypt miar kontekstu i pamięci podręcznej, skrypt czasów bramki, uruchamiacz testów), ma pomiary tego narzędzia jako `unknown` z powodem, że zmienił narzędzie, które je zapisało; pozostałe miary liczy się pod wersją, na której biegł.
- `the cycle's` (spec D3, not a row). EN: the stage report of the cycle's stages (the table of tokens by model) holds the tokens written to the cache by lifetime for each stage and model as an input of the cost only; `task-cycle/cycle_stages.py` counts them for the cost, the script of the cache-use measures counts the same tokens for its own file, neither takes figures from the other's file; the measures of context and cache use stay out of the report; *Verification* has the *violates* and *complies* lines of D3 (a column of a measure of cache use other than these is a violation; the cost series splits at the version that brings the columns and the series of the mechanism measures does not); *Rationale* names the price of the columns (two scripts count the tokens; the series of the cost ends at the change that brings them); *Rejected* holds ways A and B of D1. PL: raport etapów cyklu (tabela tokenów po modelu) zawiera tokeny zapisane do pamięci podręcznej według czasu życia dla każdego etapu i modelu tylko jako wejście kosztu; liczy je `task-cycle/cycle_stages.py` dla kosztu, skrypt miar użycia pamięci liczy te same tokeny do własnego pliku i żaden nie bierze liczb z pliku drugiego; miary kontekstu i użycia pamięci nie wchodzą do raportu; *Verification* niesie linie *violates* i *complies* z D3, *Rationale* cenę kolumn, *Rejected* drogi A i B z D1.

*Rejected* also takes, from the task's *Not chosen* of question 2 (a and b, with the reason kept: "the audit still answers unknown for most versions"; "at most 14 of 34 splits in 134 merges, for rebuilding four files of methods") and of question 4 (a, with the reason kept). The existing items of *Rejected* stay, one reworded: the item about new columns of context and cache use in the stage report now gives the reason that a column would change the script that measures the cost.

### WAY-344 — heading `### WAY-344`

- `row 1`. EN: a table *Weights* or *Costs of an occurrence* of the register of problems that lacks a level gives a written result, the values that depend on the table unknown, exit code 1 and an `Error:` line that names the missing level. PL: tabela *Weights* albo *Costs of an occurrence* rejestru problemów, której brakuje poziomu, daje zapisany wynik, wartości zależne od tabeli jako `unknown`, kod 1 i linię `Error:` z nazwą brakującego poziomu.
- `row 2`. EN: a missing entry `repository` under `the-way` in the locations file is no missing field; the count takes the checkout in which its script lies; the exception is for that entry alone. PL: brak wpisu `repository` pod `the-way` w pliku lokalizacji nie jest brakującym polem; liczenie bierze checkout, w którym leży jego skrypt; wyjątek dotyczy tylko tego wpisu.
- `the cycle's` (spec D3, not a row). EN: a stage report whose detailed section has neither of the two cache-write columns is an earlier form, read with no `Error:`, its cost given with the writes priced as input (the approximation), no value made unknown by the missing columns; a report with one of the two columns and not the other has a missing field and ends with the `Error:` line. PL: raport etapów, w którego szczegółowej sekcji nie ma żadnej z dwóch kolumn zapisów do pamięci podręcznej, to wcześniejsza forma: czytana bez `Error:`, z kosztem podanym jako przybliżenie (zapisy wyceniane jak wejście), bez wartości `unknown` z powodu brakujących kolumn; raport z jedną z dwóch kolumn ma brakujące pole i kończy się linią `Error:`.

*Verification* gains the *complies* and *violates* cases of the three; *Rationale* the reasons (a table missing a level leaves the register readable, so the result is written; the exception for `repository` is written for that entry alone; the earlier form of the cache-write columns) and the earlier-form sentence of the price now lists the two columns; *Rejected* gains 1.1 a, 1.2 b, 1.3 a and 1.3 c of the task's question 1 with their reasons. The three exceptions stand in one new sentence at the end of the binding paragraph, so that they stay apart from the sentences the sibling task ("the way: small fixes after the requests #117 to #121") changes; the *Rationale* line that lists the earlier forms of the stage report also gained the two columns (one line, in the middle of the *Rationale*, which the sibling may also touch).

### WAY-337 — read only, no change

Spec D3: none of its sentences is made untrue. I read it whole and changed nothing. Row 5 (pricing of the writes) goes to code and data.

### Glossary `Markdown file` — `foundations/glossary.md`, heading `## Markdown file`

- `row 8`. EN: a Markdown file is a file whose name ends in `.md`, `.markdown`, `.mdx` or `.mdc`, in any letter case; *Not* is `none`. PL: plik Markdown to plik, którego nazwa kończy się na `.md`, `.markdown`, `.mdx` albo `.mdc`, bez względu na wielkość liter.

The words "in any letter case" are not in row 8; they are in the description of `task-cycle/tracked_private_paths_check.py` ("a file whose name ends in `.md` in any letter case") and in the plan's slice 16, and I took them from there. If the human wants the case to count, this clause is the one to change.

### Corrections of the uses that meant `.md` alone — `the cycle's` (wording only, no approved meaning changed)

Search of the whole foundation for "Markdown" (WAY-33, WAY-97). The sentences of WAY-320, of the invariant `tracked-file-private-paths`, of the part map (`tracked-private-paths-command`), WAY-309's *Rationale*, and the single files named "Markdown file" (the part-map template, the instruction file in WAY-309's *Rejected*) are true as the new term reads them: left. Corrected, each to say what the code behind it does, so the meaning of every one is the same as before:

| Where | Before | After | What the code does |
|---|---|---|---|
| `foundations/invariants.md`, `test-method-citation` | "other than a Markdown file" | "whose name does not end in `.md`" | `elements/common/foundation_check.py` tests `endswith(".md")` |
| `foundations/invariants.md`, `guidelines-file-place` | "a Markdown file directly in `guidelines/`" | "a file whose name ends in `.md` directly in `guidelines/`" | `GUIDELINES` pattern ends in `\.md$` |
| `foundations/glossary.md`, `repository instruction file` | "as a Markdown file its root … names" | "as a file whose name ends in `.md` or `.mdc` that its root … names" | `instruction-files/check_instructions.py` `POINTED_SUFFIXES = (".md", ".mdc")` |
| `foundations/decisions.md`, WAY-321 | "other than Markdown" | "whose name does not end in `.md`" | as the first row |
| `elements/decisions/template.md` | "a tracked file other than Markdown" | "a tracked file whose name does not end in `.md`" | as the first row (line `decision:`) |
| `elements/invariants/template.md` | "a Markdown file holds no citing test" | "a file whose name ends in `.md` holds no citing test" | as the first row |

None of these changes the meaning of an approved decision; I report no correction that would. The alternative to each — leaving the sentence and letting the new term read it as true of `.mdc` — would make it false of the code.

## For the request (WAY-03)

The check lists two invariants whose sentence this change rewords while no file citing it changed: `test-method-citation` (test: `elements/common/test_foundation_check.py`) and `guidelines-file-place` (test: `elements/common/test_guidelines_place.py`). The request names both in plain words, saying what the sentence now says (the suffix `.md` is named in place of "a Markdown file") and that the test was left as it was. The listing stops nothing.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — after WAY-339, WAY-344 and the glossary entry and its corrections, and again after the commits: exit 0, `0 errors`, two `listed:` lines (the two invariants above). I ran the check once after all the edits and once after the commits, not after each entry separately: all the entries were written in one pass before the first run.
- No other check; the gate not run (WAY-160).

## Own-work check (`make-change` section 3)

Requirement most likely unmet: the spec's D3 says the earlier forms of the stage report are listed "in the entry and in its *complies* line" and that `Error:` for a report with neither column is a *violates*. Check: I read the new WAY-344 text against D3's sentences one by one. The list of earlier forms in the first sentence is not edited (kept apart from the sibling task); the third sentence names the form with neither cache-write column as "an earlier form too", and the *complies* and *violates* lines carry the wording: no `Error:`, the cost given as the approximation, no value made unknown by the missing columns; one column alone is a missing field. Found: D3 is met, except that the list is in a sentence beside the first one and not inside it — a choice, named below. A second check: no `should`, `will` or capitalised keyword in the binding sentences of the two decisions (searched; none).

## Choices

- WAY-344: the three exceptions stand in one new third sentence at the end of the binding paragraph, not inside the first sentence's list. Way rejected: adding each to the first sentence — the sibling task changes it and the merge conflicts at a line both change. Cost if wrong: a reader finds the earlier forms in two places.
- WAY-339 is split into the first paragraph (three sentences: two kinds of series; series of the measures of context and cache use and gate times; the comparison and the unknown of a changed tool) and the second paragraph (where the measures are counted and the cache-write columns). The tool a cycle changes is a sentence of the first paragraph, not a paragraph of its own: it answers the same question.
- *Rejected* of WAY-339 holds ways A and B of D1 only, as the plan says; ways D and E of D1 (*Input* made to exclude the writes; a third script) are not in it, since D3 asks for A and B.
- *Rejected* of WAY-344 holds 1.2 b as well, though row 1 and 2 do not name it: it is a way not chosen for the content of WAY-344 that the task's question 1 keeps.
- The WAY-321 wording and the four other corrections of "Markdown" were made in this step and not left to the slices: the search of the foundation is this step's (WAY-33), the slices change code and tests only.

## Observations and uses I did not change (outside my limits: code and docstrings)

These tracked English files still use "Markdown" or "Markdown file" in the `.md`-alone meaning or in the `.md`/`.mdc` one; they are code, a skill or a docstring, and my limits are entries only. For the slices and the review to decide:

- `elements/common/foundation_check.py` lines 35, 68, 70, 77, 90, 740 and 846 ("other than Markdown", "a Markdown file"): the check reads `.md` alone. The sibling task changes this file.
- `instruction-files/check_instructions.py` lines 8 and 569, `instruction-files/SKILL.md` line 277, `agent-instructions/test_instruction_files.py` lines 4 and 84: "the Markdown files the root names", read as `.md` and `.mdc`.
- `project-level/plan_check.py` line 703 and `project-level/readiness_check.py` line 326 (`help=` of an argument, "a Markdown file"): the argument is a document, any suffix.
- `task-cycle/tracked_private_paths_check.py` line 15 and `installation/README.md` lines 86, 91 and 124: slice 16 corrects them.
- `task-cycle/private_paths_check.py` line 39 ("a link only in a Markdown file"): the script reads a note link in every file it is given; the word describes WAY-320's rule.

One observation about the foundation, not changed: "stage report" means two things. WAY-260 and WAY-294 use it for the report an agent of a stage writes (`reports/*.md`); WAY-339's first paragraph ("the form of a stage report") means that, while WAY-339's second paragraph, WAY-344 and the spec mean the table of stages `stages.md`. In WAY-339's second paragraph I wrote "the stage report of the cycle's stages, the table of its tokens by model" to tell them apart. A rename is a decision for the human (WAY-99); I did not make it.

## Reaches beyond the handoff

- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/glossary/skill/read.md`, `decide_entry.md`, `write.md`, `elements/decisions/template.md`, `elements/glossary/template.md`, `elements/glossary/examples.md`, `elements/decisions/examples.md`, WAY-03: the element skills name them as the reading of an entry; read whole (WAY-03 only for the form and for the listing of a changed invariant sentence).
- `elements/invariants/template.md` line 60, `elements/decisions/template.md` line 233, `instruction-files/check_instructions.py` lines 53 and 569-590, `elements/common/foundation_check.py` suffix tests (lines 760-770, 958): read only for the corrections of "Markdown" above.
- `process-audit/problem_register.md` lines 76-110 (the two tables and their levels): to word the plain-language level case of WAY-344.

## Unread material

- `process-audit/audit_count.py`: read lines 1-235 (the module description to the register paragraph); lines 236-330 not read.
- The spec: read lines 50-254 (Constraints from line 50, D1, D2, D3 and the first lines of D4); lines 1-49 and 255 to the end (D4 and D5) not read, not named by the handoff.
- `task-cycle/tracked_private_paths_check.py`: the module description (lines 1-40) only.
- The invariants file and the other foundation files: the sentences of `tracked-file-private-paths` and `test-method-citation` whole, the rest by search.
- WAY-324, WAY-320, WAY-07, WAY-33, WAY-95, WAY-97, WAY-99, WAY-35, WAY-150, WAY-30, WAY-337, WAY-339, WAY-344, `foundations/glossary.md` and `foundations/part_map.md`: read whole.

## Searches not found or unclear

- The task's row 8 gives the suffixes but not whether the letter case counts; I took "in any letter case" from the description of `task-cycle/tracked_private_paths_check.py` and the plan (see the glossary entry above).
- "Stage report" has two meanings in the foundation (see above); the reading of WAY-339's first paragraph ("the form of a stage report") as the agent's report is mine, from the plan's slice 6 (the files under `task-cycle/change`, `plan`, `review`, `spec`).
- WAY-339's *Rejected* item for question 2 b carries a measurement of the task's source ("14 of 34 splits in 134 merges"); I kept it with the conditions the source gives; its record is the git history of the branch, which a reader can open.
- The three exceptions of WAY-344 and the cache-write columns have no tests yet; *Verification* carries the pair of examples for them, to be replaced by the clause `tests:` and the lines `decision:` by the return step where a slice's test holds them (the template's rule on a later slice's test).

## Working copies

None made. `.runs/foundation/` was not created; nothing to remove.
