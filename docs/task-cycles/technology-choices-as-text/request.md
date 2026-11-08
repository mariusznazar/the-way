**State: ready** — the change is complete and checked; one thing waits for your yes, listed under "For you to decide".

## What you will see

When the process settles which technology a product uses, it used to show you the choices researched together as one dense table: several choices at once, with counts of packages and kilobytes in the cells. From now on it shows them in one message of plain text, one choice after another:

- Each choice says what it decides, in words that a person who does not know the technology can follow.
- The options that decide it are described under their own names, each by what it changes for the product.
- The other options get one line each, and the lines of the options that were left out stay.
- Then come the recommendation, the weak point of the option recommended, and beside it the risks the tests found, each marked as a hypothesis.

Before the message reaches you, a fresh agent now also checks it for two things: that no option is shown by figures or features instead of by what it changes for the product, and that no word stands there which a person who does not know the technology could not follow without an explanation. The word "table" is replaced by "message" everywhere it named what you receive: in the technology step, in the templates for a project definition and for a task, in the skill that leads a project, and in the decision log.

Two small related fixes ride along. When a task meets a choice that an existing rule already holds, the list shown to you keeps that item as held and now adds one sentence saying what that rule leaves unsaid, so you can see that there is something left for you to say. And one sentence in the same paragraph, which said the opposite of the list rule, is corrected.

What it costs: the message is longer than the table was, and you lose the comparison of options side by side. The check by the agent is a judgment, not a mechanical rule, so it may flag a word you know, and it reads only the first message, so a jargon word in a later follow-up goes unchecked.

### Underneath

The wording lives in the text of the technology step, in three templates and one skill of the project part, and in seven entries of the decision log; one of them, the rule on how a technology choice reaches you, changes its meaning from "one table" to "one message of plain text".

## For you to decide

1. This request changes the meaning of a rule you accepted earlier: the rule on how technology choices reach you said "in one table", and now says "in one message of plain text, one choice after another", with the check by a fresh agent added. You accepted this at the task; the merge makes it binding. Accept? (Foundation entries, 1 and 2)
2. Three choices the cycle made where the task left room, and another answer would change what the foundation binds: (a) the check by the fresh agent is written into the same rule as the form of the message, not into the general rule on checking proposals that are shown together; (b) the sentence about the held item is written into the rule on tasks that already says such an item stays held, not into the rule on how the step runs at a task; (c) the rule on choosing a place to run and the rule on logs, the interface and the development data were reworded in the same way, and the second was not on the task's list. Accept? (Course of the cycle, Choices)

## Cost

About 30 minutes of working time across 15 stages and 23.2 million tokens in all, every stage on Sonnet 5.5; almost all of the tokens are cached input (22.3 million), and the output is 0.14 million. Two code reviews: the whole change passed with four small remarks, and the fix for them passed. One fix, and a return step that changed nothing. The table of stages is in the committed record: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/technology-choices-as-text/stages.md

## How to merge

Merge with a merge commit, not squash or rebase, so that the commits stay and the link to the record keeps working. Nothing in this request waits for a review of the foundation.

<details>
<summary>W Twoim języku</summary>

**Stan: ready** — zmiana jest gotowa i sprawdzona; jedna rzecz czeka na Twoje tak, wypisana w „Do rozstrzygnięcia”.

### Co zobaczysz

Gdy proces ustala, jakiej technologii użyje produkt, pokazywał Ci wybory zbadane równolegle jako jedną gęstą tabelę: kilka wyborów naraz, z liczbami pakietów i kilobajtów w komórkach. Od teraz pokazuje je jedną wiadomością zwykłego tekstu, wybór po wyborze:

- Każdy wybór mówi, co rozstrzyga, słowami, które odczyta osoba nieznająca technologii.
- Opcje, które rozstrzygają, są opisane pod własnymi nazwami, każda tym, co zmienia w produkcie.
- Pozostałe opcje dostają po jednej linii, a linie opcji, które odpadły, zostają.
- Potem idą rekomendacja, słaby punkt rekomendowanej opcji i obok niego ryzyka, które wyszły z testów, każde oznaczone jako hipoteza.

Zanim wiadomość do Ciebie dotrze, świeży agent sprawdza ją teraz także pod dwoma kątami: czy żadna opcja nie stoi liczbami albo cechami zamiast tym, co zmienia w produkcie, i czy nie pada słowo, którego osoba nieznająca technologii nie odczyta bez wyjaśnienia. Słowo „tabela” zastąpiło „wiadomość” wszędzie tam, gdzie nazywało to, co dostajesz: w kroku technologii, w szablonach definicji projektu i zadania, w skillu prowadzącym projekt i w dzienniku decyzji.

Przy okazji dwie drobne poprawki. Gdy zadanie trafia na wybór, który już trzyma istniejąca reguła, lista pokazana Tobie zostawia tę pozycję jako trzymaną i dopisuje jedno zdanie o tym, czego ta reguła nie mówi, żebyś widział, że jest coś do dopowiedzenia. A jedno zdanie w tym samym akapicie, które mówiło odwrotnie niż reguła listy, jest poprawione.

Cena: wiadomość jest dłuższa niż tabela i tracisz porównanie opcji obok siebie. Sprawdzenie przez agenta to ocena, nie reguła mechaniczna, więc może zgłosić słowo, które znasz, i czyta tylko pierwszą wiadomość, więc żargon w późniejszym dopytaniu przechodzi niesprawdzony.

### W środku

Brzmienie siedzi w tekście kroku technologii, w trzech szablonach i jednym skillu części projektowej oraz w siedmiu wpisach dziennika decyzji; jeden z nich, reguła o tym, jak wybór technologii do Ciebie dociera, zmienia sens z „jedna tabela” na „jedna wiadomość zwykłego tekstu”.

### Do rozstrzygnięcia

1. Ten request zmienia sens reguły, którą wcześniej przyjąłeś: reguła o tym, jak wybory technologii do Ciebie docierają, mówiła „jedną tabelą”, a teraz mówi „jedną wiadomością zwykłego tekstu, wybór po wyborze”, z dopisanym sprawdzeniem przez świeżego agenta. Przyjąłeś to przy zadaniu; scalenie robi to wiążącym. Przyjmujesz? (Foundation entries, 1 i 2)
2. Trzy wybory, które cykl zrobił tam, gdzie zadanie zostawiało miejsce, a inna odpowiedź zmieniłaby to, co wiąże fundament: (a) sprawdzenie przez świeżego agenta jest zapisane w tej samej regule co forma wiadomości, a nie w ogólnej regule o sprawdzaniu propozycji pokazywanych razem; (b) zdanie o trzymanej pozycji jest zapisane w regule o zadaniach, która już mówi, że taka pozycja zostaje trzymana, a nie w regule o tym, jak krok biegnie przy zadaniu; (c) reguła o wyborze miejsca uruchomienia i reguła o logach, interfejsie i danych rozwojowych zostały przeredagowane tak samo, przy czym druga nie była na liście zadania. Przyjmujesz? (Course of the cycle, Choices)

### Koszt

Około 30 minut pracy w 15 etapach i łącznie 23,2 mln tokenów, wszystkie etapy na Sonnet 5.5; prawie wszystko to wejście z pamięci podręcznej (22,3 mln), a wyjście to 0,14 mln. Dwa przeglądy kodu: przegląd całej zmiany przeszedł z czterema drobnymi uwagami, a poprawka na nie też przeszła. Jedna poprawka i krok powrotny, który niczego nie zmienił. Tabela etapów jest w zatwierdzonym rekordzie: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/technology-choices-as-text/stages.md

### Jak scalić

Scal commitem scalającym, nie przez squash ani rebase, żeby commity zostały, a link do rekordu działał. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

This is a change of wording in the process's own texts and of one accepted rule; no script runs differently. No test reads these sentences, so their wording was checked by reading (by the author and by the two reviewers), not by a test. Two commits besides the record's:

- `78c32c7` — the texts and the entries. `project-level/technology/settle.md` carries the message in place of the table and the added check; `project-level/technology/task_run.md` carries the held-item sentence and the corrected interjection; one word changed in `project-level/technology/SKILL.md`, `project-level/definition_template.md`, `project-level/task/template.md`, `project-level/task/skill/orchestrated_mode.md`, `project-level/lead/conversation_template.md` and `project-level/lead/skill/SKILL.md`; and in `foundations/decisions.md`, WAY-123 and WAY-165 changed in meaning and WAY-137, WAY-138, WAY-166, WAY-267 and WAY-268 changed by one word or one rephrased example.
- `f809953` — the fix for the four Minor findings of the review of the whole change: one phrase of WAY-123 made unambiguous ("in the first message, before it is shown"), one reason removed from its rationale because the task did not give it, the sentence on how far the check reaches reworded as what the check covers, and the added lines rewrapped so that the diff holds only the change.

Nothing is a script, a surface or an invariant test; no skill was added, renamed, moved or given another description, so the entry points are unchanged. One wording difference is left on purpose: the project definition template says a fresh agent "has checked that message", where WAY-123 says "in the first message, before it is shown"; the meaning is the same.

## Checks

- The gate, `python -B gate/run_tests.py`, on the final tree `f809953`: exit 0, 804 tests in 9 directories, every directory passed. On the base `a3206c1`: exit 0, the same count. No check failed or did not run in either gate run.
- Two directory checks failed once in a cycle run and passed again; both files are of parts outside the task's parts, so the details stand under "Findings outside the task's scope": `python -B gate/run_tests.py elements/common` failed in 1 cycle run and passed in 4 others; `python -B gate/run_tests.py installation` failed in 1 cycle run and passed in 3 others.
- `python -B elements/common/foundation_check.py`: exit 0 ("0 errors"), run by the author, by both reviewers and again by the author at the fix and at the return step. `python -B gate/run_tests.py project-level`: exit 0, 271 tests.
- Own-work check of the author: the requirement most likely not met was that every site where "table" names what you receive is changed and no ordinary table is. The check was a search of "table" and "tables" in `project-level/` and `foundations/` with every remaining hit read; every remaining hit is an ordinary table. It also found a draft error before the commit: the first draft of WAY-123 said the checking agent "sees only the message", whereas the step also gives it the document.
- The author checked that the sentences of points 1, 2 and 5 of the task stand word for word: exit 0, found 4 of 4. Own-work check of the fix: it found five added lines over the width of their neighbours and fixed them; the width scan then gave exit 0, 97 added lines, none over 100 characters. Own-work check of the return step: a `git grep` of the old wording over the whole repository found two hits, both correct (a rejected way in WAY-123 and the plan's "one row of one table of tasks").
- The form check of this description, `python -B task-cycle/request_check.py .runs/task-cycles/technology-choices-as-text/request.md --task .runs/task-cycles/technology-choices-as-text/task_frozen.md`, and the check of private paths on the description, `python -B task-cycle/private_paths_check.py .runs/task-cycles/technology-choices-as-text/request.md`: run on this text, results filled in when the record is committed.

## Foundation entries

1. WAY-123, changed, marked `row 1`: a wave of technology choices reaches the human in one message of plain text, choice after choice; only the options that decide a choice are described at length, under their own names, the others get one line and the lines of the options left out stay; the table, the table with a plain paragraph beneath and the rule "tool name only where it carries a consequence" are rejected. This changes the meaning of an accepted decision.
2. WAY-123, changed, marked `row 2`: before the wave reaches the human, a fresh agent checks the first message for an option shown by figures or features instead of what it changes for the product and for a word a person who does not know the technology cannot follow without an explanation; the check stays an agent's judgment and covers the first message alone; the variant that checks figures and features only is rejected.
3. WAY-165, changed, marked `row 3`: in a run at a task, the list shown to the human keeps an item held by a decision that is silent on part of its matter as held, with one sentence saying what that decision leaves unsaid.

Rows 1 and 2 are tied to the existing WAY-123, and row 3 to the existing WAY-165, since each already answers the question the row settles. WAY-137, WAY-138, WAY-166, WAY-267 and WAY-268 changed by one word or one rephrased example, with no change of meaning. No entry is marked `projected` or `the cycle's`. No invariant test, surface or *Violated* mark is changed.

## Minor findings

1. From the review of the fix, the fix report (in the record, `reports/fix_report.md`; the reviewer names it `reports/fix.md`): "`reports/fix.md` says the added lines are "within 100 characters and within 100 bytes" and that the scan printed "0 over-long, longest 100 bytes". Counted by bytes, 11 added lines are 102 to 105 bytes (see above). The claim of bytes is wrong, the claim of characters is right, and finding 4 asked for characters. It affects no file of the change. Blocks nothing."

## Findings outside the task's scope

The reviewers marked no finding outside the task's scope. Two checks whose files belong to parts outside the task's parts failed once in a cycle run and passed again:

- `elements/common/test_foundation_check.py`: two tests (`test_based_on_names_by_identifier_alone_no_fact`, `test_file_left_out_on_purpose_needs_no_part`) failed in the author's run when three test directories were run at once; the same directory passed alone (109 tests) and in 3 later runs (the whole-change reviewer's, the fix author's, the gate on the final tree). The cause was not verified; the author's guess is contention on temporary git repositories.
- `installation/test_styleguide_installation.py`: one test (`test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product`) failed in a run that spanned the author's commit, because it compares the pinned commit with the HEAD it found at the start; the file passed alone (2 tests), the directory passed in the fix author's run (44 tests) and in the gate on the final tree.

## Course of the cycle

- **Task and sources:** one task, independent of any project, to show the choices of a technology wave as text instead of a table and to correct the held-item sentence; sources: the task document accepted on 2026-11-07 with its three settlements, and the foundation at `a3206c1`. The task cited line numbers at `52889bc`; the files of `project-level/` had not changed since, and `foundations/decisions.md` had moved, so its sites were found by heading and quoted words.
- **Process pin:** none; the repository is the process itself, and the gate on the base and on the final tree passed.
- **Spec:** none; the task settles every choice its items need, so there was no open design choice.
- **Route:** one author without a plan, class same as the orchestrator (Sonnet 5.5), because the change touches an accepted decision and asks a judgment at each site where "table" appears. No discarded attempt.
- **Plan:** none.
- **Choices:** 7 rows in the questions table of the record, three of them (C5 to C7) in item 2 of "For you to decide": https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/technology-choices-as-text/cycle.md
- **Blocking findings left:** none; the review of the whole change found no blocking finding, and the fix for its four Minor findings passed its review.
- **Record:** https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/technology-choices-as-text
