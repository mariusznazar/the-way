**State: ready** — three things wait for your yes, listed under "For you to decide".

## What you will see

The agent that leads the writing of a product's coding, testing or styleguide guidelines now gets texts that agree with each other and with the decisions behind them. Until now it met rules that contradicted one another, pointers to the wrong step and questions put at the wrong moment. Concretely, it now does the following:

- It checks for itself what a screen shows without data, from a link and after a refresh, instead of asking you about every screen.
- It settles with you the version of the tool for each standing check, not only the tool.
- When you pick a different tool or rule set than the one that was tried, the split into blocking rules and examples rests on a trial of the one you picked.
- For a new kind of code it settles only the standing checks that kind touches, and a kind in a language no check reads makes the task an extension of the guidelines.
- It no longer asks you again about the rules on failures and logs when the product's guidelines already hold them with an explicit "none".
- A test of a level that the testing guidelines do not name yet sends the task to the testing skill as an extension, and the exemplar test of that level is settled there.
- When one task carries both coding and testing guidelines and the work is split, the skill that stopped closes the list of causes, and a skill hands back to the next step of the task only after the other skill has led its matters.
- The judging of instruction files gives a fragment that goes to several places a row per part, and each proposed rule change a row of its own.
- A level of tests named in the product more narrowly than in the field always gets a glossary entry.

### Underneath

Twenty remarks left open by the review of the foundation are fixed in the skills and templates of the three guideline disciplines, in the shared reading and audit text, in the judging text of instruction files and in the decision log, where five settlements you already accepted are written down.

## For you to decide

1. Choices the cycle made where the task left room, which another answer would change for the person leading these guidelines or for the foundation: (a) which standing checks a new kind of code "touches" is left to the agent's judgement, with no written criterion; (b) the personal-data line of the coding template and the rows of the judging table became new decisions, not edits of older ones; (c) who starts the return of a stopped audit after you split the work is not named; (d) the judging table says nothing about the verdict of a proposal row beyond "a row of its own"; (e) a rule that stays after a departure keeps the meaning of a failure in its own text. Accept them? (Course of the cycle, Choices)
2. Three entries of the foundation that you did not see at the task: one sentence in the glossary template about test-level names, found by the search of the whole foundation, and two precedences the cycle recorded — the test-level naming decision now wins over the older glossary-words decision, and the new-kind decision narrows the older decision on standing checks. Accept them? (Foundation entries, 6-8)
3. Two findings you or an agent leading the work will feel: the coding and testing skills still say that a new meaning reaches the code only through the task document, while the styleguide skill now also names the second way, approval at a blocked draft request; and the testing skill still points to some variant files through another file, where the styleguide and coding skills now point directly. Fix them in this request, or make a task of them? (Findings outside the task's scope, 1-2)

## Cost

About 36 minutes of working time across 13 stages, 37.5 million tokens in all, of which 32.0 million on Sonnet 5.5 and 5.5 million on Opus 5.5; cached input is nearly all of it. Three code reviews (the whole change, its fix, the return step), one fix. The table of stages is in the committed record: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/guidelines-skills-batch/stages.md

## How to merge

Merge with a merge commit, not squash or rebase, so that the commits stay and the link to the record keeps working. Nothing in this request waits for a review of the foundation.

<details>
<summary>W Twoim języku</summary>

**Stan: ready** — trzy rzeczy czekają na Twoje tak, wypisane w „Do rozstrzygnięcia”.

### Co zobaczysz

Agent, który prowadzi pisanie wytycznych kodu, testów albo styleguide'u produktu, dostaje teraz teksty zgodne ze sobą i z decyzjami, na których stoją. Dotąd trafiał na reguły sprzeczne między sobą, odesłania do złego kroku i pytania zadawane w złym momencie. Konkretnie:

- Sam sprawdza, co ekran pokazuje bez danych, prosto z linku i po odświeżeniu, zamiast pytać Cię o każdy ekran.
- Ustala z Tobą wersję narzędzia każdego stałego sprawdzenia, nie tylko samo narzędzie.
- Gdy wybierzesz inne narzędzie albo inny zestaw reguł niż ten, który przeszedł próbę, podział na reguły blokujące i przykłady opiera się na próbie wybranego zestawu.
- Przy nowym rodzaju kodu rozstrzyga tylko te stałe sprawdzenia, których ten rodzaj dotyka, a rodzaj w języku, którego żadne sprawdzenie nie czyta, robi z zadania rozszerzenie wytycznych.
- Nie pyta Cię od nowa o reguły awarii i logów, gdy wytyczne produktu już je mają z wyraźnym „none”.
- Pierwszy test poziomu, którego wytyczne testów jeszcze nie nazywają, kieruje zadanie do skilla testów jako rozszerzenie, i tam ustala się wzorcowy test tego poziomu.
- Gdy jedno zadanie niesie wytyczne kodu i testów razem, a Ty rozdzielisz pracę, skill, który się zatrzymał, domyka listę przyczyn, a skill oddaje pracę do następnego kroku zadania dopiero wtedy, gdy drugi skill poprowadził swoje sprawy.
- Ocena plików instrukcji daje fragmentowi idącemu w kilka miejsc wiersz na każdą część, a każdej proponowanej zmianie reguły własny wiersz.
- Poziom testów nazwany w produkcie węziej niż w branży zawsze dostaje hasło słownika.

### W środku

Dwadzieścia uwag z przeglądu fundamentu, które dalej stały, poprawiono w skillach i szablonach trzech dyscyplin wytycznych, we wspólnym tekście czytania i audytu, w tekście oceny plików instrukcji oraz w dzienniku decyzji, gdzie zapisano pięć przyjętych już przez Ciebie ustaleń.

### Do rozstrzygnięcia

1. Wybory, które cykl zrobił tam, gdzie zadanie zostawiało miejsce, a inna odpowiedź zmieniłaby coś dla osoby prowadzącej te wytyczne albo dla fundamentu: (a) które stałe sprawdzenia nowy rodzaj kodu „dotyka”, zostaje ocenie agenta, bez zapisanego kryterium; (b) linia danych osobowych szablonu kodu i wiersze tabeli oceny stały się nowymi decyzjami, a nie poprawkami starszych; (c) nie wskazano, kto uruchamia powrót zatrzymanego audytu po rozdzieleniu pracy; (d) tabela oceny nie mówi nic o werdykcie wiersza propozycji poza „własnym wierszem”; (e) reguła, która zostaje po odstępstwie, trzyma znaczenie awarii we własnym tekście. Przyjmujesz? (Przebieg cyklu, Wybory)
2. Trzy wpisy fundamentu, których nie widziałeś przy zadaniu: jedno zdanie w szablonie słownika o nazwach poziomów testów, znalezione wyszukiwaniem po całym fundamencie, oraz dwa pierwszeństwa zapisane przez cykl — decyzja o nazwach poziomów testów wygrywa teraz ze starszą decyzją o hasłach słownika, a decyzja o nowym rodzaju kodu zawęża starszą decyzję o stałych sprawdzeniach. Przyjmujesz? (Wpisy fundamentu, 6-8)
3. Dwie uwagi, które odczujesz Ty albo agent prowadzący pracę: skille kodu i testów dalej mówią, że nowe znaczenie dociera do kodu tylko przez dokument zadania, a skill styleguide'u wymienia już drugą drogę, zatwierdzenie przy zablokowanym szkicu requestu; skill testów wskazuje część plików wariantów dalej przez inny plik, gdzie skille styleguide'u i kodu wskazują je wprost. Poprawić w tym requeście, czy zrobić z nich zadanie? (Uwagi poza zakresem zadania, 1-2)

### Koszt

Około 36 minut pracy w 13 etapach, łącznie 37,5 mln tokenów, z czego 32,0 mln na Sonnet 5.5 i 5,5 mln na Opus 5.5; prawie wszystko to wejście z pamięci podręcznej. Trzy przeglądy kodu (całej zmiany, jej poprawki, kroku powrotnego), jedna poprawka. Tabela etapów jest w zatwierdzonym rekordzie: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/guidelines-skills-batch/stages.md

### Jak scalić

Scal commitem scalającym, nie przez squash ani rebase, żeby commity zostały, a link do rekordu działał. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

The change fixes the open remarks of the first review of the foundation in the guideline skills, then writes the settlements into the decision log. Four commits:

- `e6d0f9e` — the twenty items of the task, in the skills and templates of the coding, testing and styleguide guidelines (`product-guidelines/coding/`, `product-guidelines/testing/`, `product-guidelines/styleguide/`), the shared files `product-guidelines/audit_end.md` and `product-guidelines/reading.md`, `project-level/task/skill/guideline_findings.md` and `instruction-files/judging.md`.
- `e66e8e7` — the five settlements as entries of `foundations/decisions.md`, and one sentence in `elements/glossary/template.md`.
- `2c46cb7` — the fix for the review of the whole change: one blocking finding (the testing skill no longer settled the exemplar test of a level that has no recipe yet) and eight Minor findings within the task (a table cell, the weak point of one decision, a bare file name, a criterion the sources did not give, the scope of one decision, a missing citation, a table row against its paragraph, the second trial run).
- `f5ae96f` — the return step: two summary sentences in `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md` that still described the old hand-back rule.

Nothing is a script, a surface or an invariant test; no skill was added, renamed or moved, so the entry points are unchanged.

## Checks

- The gate, `python -B gate/run_tests.py`, on the final tree `f5ae96f`: exit 0, 804 tests in 9 directories, every directory passed. On the reviewed change `2c46cb7`: exit 0, the same count. On the base `05534d3`: exit 0, the same count; no check failed on the base or in either run.
- Not covered by any test: the texts in `product-guidelines/` have no test directory and `instruction-files/check_instructions.py` does not read them, so the skill files were checked by reading (by the author and by three reviewers). A wording error there would show only when an agent follows the skill.
- Own-work checks of the author, item by item, in the author's report; `python -B elements/common/foundation_check.py` exit 0 (0 errors); `python -B instruction-files/check_instructions.py .` exit 0; the focused tests of `instruction-files`, `project-level`, `elements/common`, `agent-instructions` and the two installation unittest modules, all exit 0.
- The form check of this description, `python -B task-cycle/request_check.py .runs/task-cycles/guidelines-skills-batch/request.md --task .runs/task-cycles/guidelines-skills-batch/task.md`: FORM_RUNS. The check of private paths on the description: PATHS_RUNS. On the copy of the record, `python -B task-cycle/private_paths_check.py docs/task-cycles/guidelines-skills-batch`: COPY_PATHS_RUNS. The process remarks check, `python -B task-cycle/remarks_check.py`: REMARKS_RUNS.

## Foundation entries

1. The decision on how a product's testing guidelines name test levels, edited, marked `row 1`: for the names of test levels it prevails over the decision on which words take a glossary entry, so a level named otherwise than in the field, a narrower meaning included, always takes a glossary entry.
2. A new decision, marked `row 2`: the line `Personal data: none — <PREFIX-NN>` is a field of the rule `### Secrets and personal data` that the coding template adds, and its name stays in English.
3. A new decision, marked `row 3`: the judging table gives a fragment going to several places a row for each part with one of four verdicts, and each proposal to add or change a rule a row of its own.
4. The decision on the order of the causes of an audit of the guidelines skills, edited, marked `row 4`: when the human separates the work after one audit stopped, so that the other will not run, the skill of the stopped audit closes the list as the audit that runs last does.
5. The decision on what refinement assigns to a task creating an unindexed kind of code, edited, marked `row 5`: a new kind in a product with coding guidelines settles and checks only the standing checks it touches, and a kind in a language no standing check reads makes the task an extension.
6. A sentence in `elements/glossary/template.md`, marked `the cycle's`: the name of a level of a product's tests is an exception to the rule for narrower meanings, and always takes an entry. It restated the older rule without the exception, so the search of the whole foundation corrected it.
7. The test-level naming decision (entry 1), marked `the cycle's` for its precedence: it now `narrows` the glossary-words decision and states its area in its own binding sentence. The passage of what you accepted that gives the outcome: „WAY-240 wygrywa przy nazwach poziomów testów, a WAY-240 dostaje zdanie o pierwszeństwie przed WAY-95.” The older decision is not edited, since the rule on precedence puts the record in the decision that prevails.
8. The new-kind decision (entry 5), marked `the cycle's` for its precedence: it now `narrows` the decision on the three standing checks. The passage that gives the outcome: „tak — na wariant c agenta, zmieniający obie strony” with the anchor „They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it”. The scope of the test-level decision also now names the glossary part, so an agent working on the glossary finds it.

No invariant test, surface or *Violated* mark is changed.

## Minor findings

1. From the review of the fix, `product-guidelines/coding/template.md`, the column "Goes with it" of the row for `### Recording a failure`: "It now restates the departed rule's own content ("the way a failure is written, with its cause, once, where code handles it, and the last-resort handler"). The other rows use this column for what goes *besides* the departed heading ("the form of a line", "the events of the list…"), and the row for `### Hiding a failure` still reads "nothing else". The row is correct but reads in a different way from its neighbours. Nothing a reader does changes; polish only." It does not change what a reader does.

## Findings outside the task's scope

1. `product-guidelines/coding/SKILL.md:46` and `product-guidelines/testing/SKILL.md:45` still say "A meaning reaches the code only through the task document". "Item 1 changed only the styleguide skill. The three sibling skills now say different things about the same WAY-172 route, and the coding and testing ones omit the blocked-draft way, which their own templates give ("Writing the files", `coding/template.md:316-317`). This goes beyond the task (item 1 names the styleguide skill alone). Suggested as a backlog item." The next agent leading coding or testing guidelines may read the one-way text and not propose a meaning at a blocked draft request.
2. `product-guidelines/testing/SKILL.md:98` and `:117-118` still point indirectly ("`starting_set.md` sends you to `research.md`", "`settle.md` sends you to `new_tools.md`"). "Item 3 names only the styleguide and coding skills. The same principle (`instruction-files/SKILL.md`, "points directly and one level deep") applies. This goes beyond the task." The agent still reaches the files, one level deeper than the rule asks.

No check whose file belongs to a part outside the task's parts failed in a cycle run.

## Course of the cycle

- **Task and sources:** one task, independent of any project, to fix the twenty open remarks of the first review of the foundation in the guideline skills and to write five settlements into the decision log; sources: the task document accepted on 2026-11-07, the foundation at `f447bb6` when it was refined and at `05534d3` when the cycle started (only one reworded paragraph in each of three skills differed, touching no item).
- **Process pin:** none; the repository is the process itself, and the gate on the base and on the final tree passed.
- **Spec:** none; the task settles every choice its items need, so there was no open design choice.
- **Route:** one author without a plan, class same as the orchestrator (Sonnet 5.5), because the change is text across a few files of one family; the author was resumed for the fix and the return step. No discarded attempt.
- **Plan:** none.
- **Choices:** 16 choices and rulings besides the task's content, in the questions table of the record, five of them in item 1 of "For you to decide": https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/guidelines-skills-batch/cycle.md
- **Blocking findings left:** none; the one blocking finding of the review of the whole change was fixed and the fix passed its review.
- **Record:** https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/guidelines-skills-batch
