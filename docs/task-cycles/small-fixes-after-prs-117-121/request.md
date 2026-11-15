**State: ready** — one item in "Fix or let through" waits for your answer; everything else is accepted by merging.

## What you will see

A set of small corrections to the-way's process, left over from five earlier merged changes (#93 and #117 to #121), made in one change. How the work with the process changes:

- The gate's test that checks directories run at the same time no longer loses lines at random on Windows. The helper that records the start and end of each test used to append to one shared file, and two processes writing at the same moment lost lines; that was the real cause of the random red in #117, which that request called "a busy machine". Now each event is a small file of its own. The test still fails when the directories run one after another, and still waits 120 seconds.
- The step that checks a deployment skill's list now sends the author to the guide for writing that skill also when a task item writes into it how to read the logs, how long the record lives, or how a human learns of a failure, or records your refusal to settle one of them.
- The three guideline templates (code, tests, screens) say that a choice the task did not settle stops the cycle only when the choice carries a real cost; a rule that only says how to write is the cycle's own, and you accept it at the merge.
- The foundation check now prints one extra line for an invariant whose sentence was reworded when its copy at the point the branch left the main branch lacks its method or its part, naming the missing field. Before, it skipped such an invariant without a word. The exit code does not change. The same check also stops reading a full stop and a space inside a quotation — straight, curly or the Polish low-high form — as the end of a sentence.
- The decision template says what the "rejected ways" of a decision the cycle wrote from its own choice holds: `unknown`, unless a statement of yours names the ways weighed. The invariant template and the rule for decisions explain that a decision number written into an invariant's sentence, because that decision holds its condition, is part of the condition and no link.
- A task document can now carry the status "dropped — approved by human", the same words as a plan's task.
- The plan skill asks a slice's checks to run the tests of the invariants its change may break, not of every invariant it reaches, and tells a slice that writes an invariant whose test a later slice writes to run the foundation check with the switch that skips the missing-test report.
- When the cycle adds to an entry written from a row of your settlements, or to an entry designed in advance, a part the row or the design does not give — a pair of examples, a field left open — the entry is marked as the cycle's and put before you at the merge. A link added to the entry does not do that.
- The strongest model for the review of the whole change and of the return step is the strongest the session's settings allow, not the strongest name of the model family.

### Underneath

The script of the foundation check was three lines over the 1000-line cap, so the code that reads files and asks git moved first, unchanged, into a new module of its own. The gate ran once on the final state and passed (1600 tests in 11 directories).

## For you to decide

### Needed from you

none

### Fix or let through

1. When the cycle adds to a foundation entry a part you did not see at the task, such as a pair of examples, the entry is now marked and put before you at the merge, but the description of a request still gives you only one sentence of what the entry means, not the added pair. So you could merge examples by which agents will later judge changes without reading them. This request avoids it for its own entries by quoting each added pair under its entry; the next request depends on its writer doing the same. Fixing the template of the description in this request costs one more round of correction with a review, since the task did not ask for it; undoing it costs a small edit. Making a task of it costs a later session; undoing it, nothing. Letting it through costs nothing now, and the risk is a later request that hides an added pair behind a sentence until someone notices. I recommend making a task of it: the task asked only for the marking, and the reviewer judged the template outside the task. Its weak point: until that task is done, the next request that adds a pair shows it only as a sentence. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The gate's test module records each event as an empty file in a directory, named by the time in nanoseconds and the text, and reads the files back in order. The other ways were one file per process, which loses the order across processes that two tests read, and an explicit lock, which spins on Windows because a file another process is opening cannot be deleted. Before the change a trial with three processes started together lost a line in 19 of 20 runs; after it, in none of 20, and six runs of the gate's directory in a row passed. As you settled, no permanent test of the loss itself was added.
3. The extra line of the foundation check for an invariant with a missing field in the base copy appears also when a file that cites the invariant changed. The other way, listing it only when no citing file changed, would hide the very case the line is for. An invariant that lacks a field now is still an error as before, and one whose sentence did not change gets no line.
4. The code that reads files and git moved into a new module, because the check script stood at 1003 lines over a cap of 1000 and two items of the task add to it. The other way, moving the readers of text as well, is a larger move that changes what another script imports. The other task that changes the same script and the same decision sentence, which the task left without a dependency, will have to be reconciled by whichever of the two merges second.
5. In three places I went slightly beyond the words of the task so that the sentences read whole: the pointer to the guide also covers the item that records your refusal to settle; the three templates also say that a rule that only says how to write is the cycle's own, which you accept at the merge, taken from the decision on guidelines; and the rule on marking entries says in the same sentence that a link added to an entry does not change its mark, which the task said in the next sentence.
6. The decision on the model class now names the setting in Claude Code, and says that where the session has no such list the strongest of every model it offers is taken. Its rationale says that a request for a model outside the list got another model, in the one session observed the session's own; I wrote it as an observation, since the only source is that session's record and no document of the tool.
7. The task text said the code of two parts is exempt from the coding and testing guidelines; that exemption was withdrawn before this task started, so the code and the tests of this change follow the guidelines, and nothing was changed in the withdrawn decision.
8. Five entries of the foundation are marked as the cycle's, which you did not see at the task, each with one plain sentence of its meaning:
   - the decision on the guide for a deployment skill gained a pair of examples: an item that records the answer or your refusal points to the guide too, and an item that names no guide does not comply;
   - the decision on where a condition that decides an invariant may stand gained a pair: a number of a decision written into the sentence is part of the condition, and the link stands beside it in its own field;
   - the decision on how an invariant's method is written now also lists the task cycle among the parts it concerns;
   - the decision on the class of model of the one author names the strongest of the models the session's settings allow;
   - the rationale of the decision on how the gate is run says a slice's checks are the tests of the code it reaches and of the invariants its change may break.
   The added pairs stand word for word in the lower part (Foundation entries).
9. Changed tests and surfaces: a test that said a reworded invariant lacking a field in the base copy gets no line was replaced by tests that say it gets one line, and two of them hold the sentence of the decision on missing fields by a line that quotes it; one test now checks a quotation with a full stop inside. No invariant was written, changed or marked violated. The foundation check keeps its path, its argument and its exit codes; on the final tree it reports no errors and no extra lines.

## Cost

About one hour of working time across 15 stages (half an hour of it waiting for tools), 65.8 million tokens (46.1 million on Sonnet 5.5, 19.7 million on Opus 5.5), one review of the whole change that failed, one review of its fix and one review of the return step, one fix after the failed review, and one full run of the gate (513 seconds). The table of stages is in the record, whose link is added to this description once the record is committed. Three directories of earlier tasks still stand because the script that removes finished ones could not tell they were no longer needed; nothing in this request waits for them, and you may remove them by hand (names in Checks).

## How to merge

Merge so that the commits are kept (the repository's own pull requests are merged as "Merge pull request"), since the link to the record survives only then. After the merge, the check of task notes in your notes vault has to start recognising the new status word of a dropped task; the task left that to the day advisor or to you, and nothing in this request waits for it.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — jedna pozycja w „Do poprawy albo przepuszczenia” czeka na Twoją odpowiedź; reszta jest przyjmowana przez scalenie.

## Co zobaczysz

Zestaw drobnych poprawek procesu the-way, które zostały po pięciu wcześniej scalonych zmianach (#93 oraz #117–#121), zrobiony jedną zmianą. Jak zmienia się praca z procesem:

- Test bramki sprawdzający, że katalogi biegną naraz, przestaje losowo gubić linie na Windows. Pomocnik zapisujący start i koniec każdego testu dopisywał do jednego wspólnego pliku, a dwa procesy piszące w tej samej chwili gubiły linie; to była prawdziwa przyczyna losowej porażki w #117, którą tamta prośba nazwała „zajętą maszyną”. Teraz każde zdarzenie to osobny mały plik. Test dalej pada, gdy katalogi biegną jeden po drugim, i dalej czeka 120 sekund.
- Krok sprawdzający listę skilla wdrożeniowego kieruje autora do przewodnika po pisaniu tego skilla także wtedy, gdy punkt zadania wpisuje do niego, jak czytać logi, jak długo żyje zapis albo skąd człowiek dowiaduje się o awarii, albo zapisuje Twoją odmowę rozstrzygnięcia którejś z tych spraw.
- Trzy szablony wytycznych (kod, testy, ekrany) mówią, że wybór nierozstrzygnięty przez zadanie zatrzymuje cykl tylko wtedy, gdy niesie realny koszt; reguła, która tylko mówi, jak pisać, jest własna dla cyklu i przyjmujesz ją przy scaleniu.
- Kontrola fundamentu wypisuje jedną dodatkową linię dla niezmiennika, którego zdanie przeredagowano, a którego kopia z miejsca, w którym gałąź odeszła od głównej, nie ma metody albo części — z nazwą brakującego pola. Wcześniej taki niezmiennik pomijała bez słowa. Kod wyjścia się nie zmienia. Ta sama kontrola przestaje też czytać kropkę ze spacją wewnątrz cytatu — prostego, kręconego albo polskiego dolno-górnego — jako koniec zdania.
- Szablon decyzji mówi, co wpisać w „odrzucone drogi” decyzji, którą cykl zapisał z własnego wyboru: `unknown`, chyba że Twoja wypowiedź nazywa rozważone drogi. Szablon niezmienników i reguła dla decyzji wyjaśniają, że numer decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem.
- Dokument zadania może mieć status „dropped — approved by human”, te same słowa co zadanie planu.
- Skill planu każe w sprawdzeniach kawałka uruchamiać testy niezmienników, które zmiana kawałka może zepsuć, a nie każdego, do którego kawałek sięga, i każe kawałkowi, który zapisuje niezmiennik z testem pisanym przez późniejszy kawałek, uruchomić kontrolę fundamentu z przełącznikiem pomijającym zgłoszenie braku testu.
- Gdy cykl dopisze do wpisu z wiersza Twoich ustaleń albo do wpisu zaprojektowanego z góry część, której wiersz ani projekt nie dają — parę przykładów, pole zostawione otwarte — wpis dostaje oznaczenie „cyklu” i trafia przed Ciebie przy scaleniu. Powiązanie dopisane do wpisu tego nie robi.
- Najmocniejszy model do przeglądu całej zmiany i kroku powrotu to najmocniejszy z dozwolonych w ustawieniach sesji, a nie najmocniejsza nazwa rodziny modeli.

### Pod spodem

Skrypt kontroli fundamentu miał o trzy linie za dużo ponad limit 1000 linii, więc kod czytający pliki i pytający gita przeniesiono najpierw, bez zmian, do osobnego nowego modułu. Bramka przeszła raz na stanie końcowym (1600 testów w 11 katalogach).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawy albo przepuszczenia

1. Gdy cykl dopisze do wpisu fundamentu część, której nie widziałeś przy zadaniu, taką jak para przykładów, wpis jest teraz oznaczany i trafia przed Ciebie przy scaleniu, ale opis prośby daje Ci nadal tylko jedno zdanie o znaczeniu wpisu, a nie dopisaną parę. Możesz więc scalić przykłady, według których agenci będą później sądzić zmiany, nie przeczytawszy ich. Ta prośba tego unika dla własnych wpisów, cytując każdą dopisaną parę pod wpisem; następna prośba zależy od tego, czy jej autor zrobi to samo. Poprawa szablonu opisu w tej prośbie kosztuje jeszcze jedną rundę poprawki z przeglądem, bo zadanie o to nie prosiło; cofnięcie to mała zmiana. Zrobienie z tego zadania kosztuje późniejszą sesję; cofnięcie — nic. Przepuszczenie nic dziś nie kosztuje, a ryzyko to późniejsza prośba, która ukryje dopisaną parę za zdaniem, aż ktoś to zauważy. Rekomenduję zrobić z tego zadanie: zadanie prosiło tylko o oznaczanie, a recenzent uznał szablon za leżący poza zadaniem. Słaby punkt: dopóki to zadanie nie powstanie, następna prośba, która dopisze parę, pokaże ją tylko jako zdanie. Poprawić w tej prośbie, zrobić z tego zadanie czy przepuścić? (Findings outside the task's scope, 1)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; powiedz, która Ci nie odpowiada.

2. Moduł próbny testów bramki zapisuje każde zdarzenie jako pusty plik w katalogu, nazwany czasem w nanosekundach i tekstem, i odczytuje pliki z powrotem po kolei. Inne drogi to jeden plik na proces, który gubi kolejność między procesami, a ją czytają dwa testy, i jawna blokada, która kręci się w pętli na Windows, bo pliku otwieranego przez inny proces nie da się skasować. Przed zmianą próba z trzema procesami startującymi razem gubiła linię w 19 z 20 przebiegów, po niej w żadnym z 20, a sześć kolejnych przebiegów katalogu bramki przeszło. Jak ustaliłeś, nie dodano stałego testu samej utraty linii.
3. Dodatkowa linia kontroli fundamentu dla niezmiennika z brakującym polem w kopii bazowej pojawia się także wtedy, gdy plik cytujący niezmiennik się zmienił. Druga droga, wypisanie tylko gdy żaden plik cytujący się nie zmienił, ukryłaby właśnie ten przypadek, dla którego linia istnieje. Niezmiennik, któremu pola brakuje teraz, nadal jest błędem jak dotąd, a taki, którego zdanie się nie zmieniło, nie dostaje linii.
4. Kod czytający pliki i git przeniesiono do nowego modułu, bo skrypt kontroli miał 1003 linie przy limicie 1000, a dwa punkty zadania mu dokładają. Druga droga, przeniesienie także czytników tekstu, to większe przeniesienie, które zmienia to, co importuje inny skrypt. Drugie zadanie, które zmienia ten sam skrypt i to samo zdanie decyzji, a które zadanie zostawiło bez zależności, będzie musiało zostać pogodzone przez to z dwóch, które scali się później.
5. W trzech miejscach poszedłem odrobinę dalej niż słowa zadania, żeby zdania czytały się całe: wskazanie przewodnika obejmuje też punkt, który zapisuje Twoją odmowę rozstrzygnięcia; trzy szablony mówią też, że reguła, która tylko mówi, jak pisać, jest własna dla cyklu i przyjmujesz ją przy scaleniu, co wzięto z decyzji o wytycznych; a reguła oznaczania wpisów mówi w tym samym zdaniu, że powiązanie dopisane do wpisu nie zmienia jego oznaczenia, co zadanie mówiło w następnym zdaniu.
6. Decyzja o klasie modelu nazywa teraz ustawienie w Claude Code i mówi, że gdy sesja nie ma takiej listy, bierze się najmocniejszy z każdego modelu, jaki oferuje. Jej uzasadnienie mówi, że prośba o model spoza listy dostała inny model, w jednej obserwowanej sesji model sesji; zapisałem to jako obserwację, bo jedynym źródłem jest zapis tej sesji, a nie dokument narzędzia.
7. Tekst zadania mówił, że kod dwóch części jest wyłączony spod wytycznych kodowania i testowania; to wyłączenie wycofano przed rozpoczęciem tego zadania, więc kod i testy tej zmiany idą za wytycznymi, a w wycofanej decyzji niczego nie zmieniono.
8. Pięć wpisów fundamentu ma oznaczenie „cyklu”, czyli nie widziałeś ich przy zadaniu, każdy z jednym prostym zdaniem znaczenia:
   - decyzja o przewodniku po skillu wdrożeniowym dostała parę przykładów: punkt zapisujący odpowiedź albo Twoją odmowę wskazuje też przewodnik, a punkt, który nie wskazuje żadnego, nie jest zgodny;
   - decyzja o tym, gdzie może stać warunek rozstrzygający niezmiennik, dostała parę: numer decyzji wpisany w zdanie jest częścią warunku, a powiązanie stoi obok w swoim polu;
   - decyzja o zapisie metody niezmiennika wymienia teraz także część „cykl zadania”;
   - decyzja o klasie modelu jednego autora nazywa najmocniejszy z modeli dozwolonych w ustawieniach sesji;
   - uzasadnienie decyzji o uruchamianiu bramki mówi, że sprawdzenia kawałka to testy kodu, do którego sięga, i niezmienników, które jego zmiana może zepsuć.
   Dopisane pary stoją słowo w słowo w dolnej części (Foundation entries).
9. Zmienione testy i powierzchnie: test mówiący, że przeredagowany niezmiennik z brakującym polem w kopii bazowej nie dostaje linii, zastąpiono testami mówiącymi, że dostaje jedną linię, a dwa z nich trzymają zdanie decyzji o brakującym polu linią, która je cytuje; jeden test sprawdza teraz cytat z kropką w środku. Żaden niezmiennik nie został napisany, zmieniony ani oznaczony jako naruszony. Kontrola fundamentu zachowuje swoją ścieżkę, argument i kody wyjścia; na stanie końcowym nie zgłasza błędów ani dodatkowych linii.

## Koszt

Około godziny pracy w 15 etapach (pół godziny z tego to czekanie na narzędzia), 65,8 miliona tokenów (46,1 miliona na Sonnecie 5.5, 19,7 miliona na Opusie 5.5), jeden przegląd całej zmiany, który nie przeszedł, jeden przegląd jego poprawki i jeden przegląd kroku powrotu, jedna poprawka po nieudanym przeglądzie i jedno pełne uruchomienie bramki (513 sekund). Tabela etapów jest w zapisie; link do niego zostanie dopisany do tego opisu po zatwierdzeniu zapisu. Trzy katalogi wcześniejszych zadań nadal stoją, bo skrypt usuwający zakończone nie umiał stwierdzić, że już nie są potrzebne; nic w tej prośbie na nie nie czeka, możesz je usunąć ręcznie (nazwy w Checks).

## Jak scalić

Scal tak, żeby commity zostały (własne prośby repozytorium scala się jako „Merge pull request”), bo link do zapisu przeżywa tylko wtedy. Po scaleniu sprawdzanie notatek zadań w Twoim vaulcie musi zacząć rozpoznawać nowe słowo statusu zadania, z którego zrezygnowano; zadanie zostawiło to doradcy dnia albo Tobie, a nic w tej prośbie na to nie czeka.

</details>

## Technical changes

The change is eight commits on the base `b6b3416`, in five groups. The corrections of items 3 and 4 of the task were withdrawn or moved before the cycle and were not made.

- **Gate test (To do 1 and 2):** `677ad78` — `gate/test_run_tests.py`: `log_event` and `logged_events` write and read one empty file per event in a directory `timeline`; `timed_module` embeds their source; the wait of 120 seconds and the test that fails when directories run one after another are unchanged. No test of the loss was added, as settled.
- **Move before the code that adds (To do 8 and 19):** `ac3c96f` — `git`, `fork_point`, `at_commit`, `read` and `MAIN_BRANCHES` moved as they stood from `elements/common/foundation_check.py` into the new `elements/common/foundation_source.py`; no change of behaviour.
- **Foundation check (To do 8 and 19):** `76c2bd2`, `b23275b` — one line for a reworded invariant that reads `test` whose base copy lacks *Method* or *Part*, naming the field, listed whether or not a citing file changed; a full stop inside `"…"`, `“…”` or `„…”` no longer begins a sentence; tests for each; the two descriptions of the listing.
- **Decisions, templates and skills (To do 5–7, 9–18, 20):** `52b122b`, `e9aea95`, `eaf815c` — the decisions WAY-139, WAY-344, WAY-60, WAY-61 and WAY-229 in place and the rationale of WAY-160; the templates of decisions, invariants, tasks and the three guidelines; the skills of plan, cycle, foundation step and decisions, and the step that checks a deployment skill's list; the fixes of the review's findings (wording, the third quotation form, a test that holds the listing when a citing file changed).
- **Return step:** `4066ae5` — WAY-344's sentence narrowed to "a field it needs for a comparison", its two added clauses of examples removed because its tests hold them, the two descriptions of the listing and the part map's line for `elements-common` made to match the code.

## Checks

- **Gate:** `python -B task-cycle/gate_times.py --output .runs/task-cycles/small-fixes-after-prs-117-121/gate_times.md -- python -B gate/run_tests.py` on head `4066ae5`, Windows, after the day advisor's start signal: exit 0, 1600 tests in 11 directories, every directory passed, 513.087 s. The random test of directories at the same time did not fail in this run.
- **Failing on the base:** none. The base `b6b3416` is a merge commit whose tree equals the tree of its second parent, so the gate was not run on it; the list is taken from the final gate of the merged cycle (`docs/task-cycles/the-way-coding-and-testing-guidelines/cycle.md`, added by commit `a0ffa80`): exit 0, 1596 tests, every directory passed.
- **Foundation check:** `python -B elements/common/foundation_check.py` without `--skip-test-citations` on head `4066ae5`: exit 0, `0 errors`, no `listed:` line.
- **Own-work checks:** the author's check of its two most doubtful requirements (the loss of lines gone; the listing line with no change of exit code) showed what the report states; the author's fix and return-step checks show the same for the quotation form and the narrowed sentence. Focused runs of the directories of the touched parts passed in each report.
- **Reviews:** whole change `FAIL e9aea95` (two Important, eight Minor, one outside scope), review of its fix `PASS eaf815c`, review of the return step `PASS 4066ae5` (three Minor); all by agents on Opus 5.5, as asked.
- **Form check:** `python -B task-cycle/request_check.py` — pending until the record is committed. **Private paths on the description:** pending until the record is committed. **Copy of the record:** pending until the record is committed. **Process remarks check:** pending until the record is committed. **CI on the request:** pending until the record is committed.
- **Working copies:** none stand. One agent ran a throwaway script from the system's temporary directory against the working-copies rule and deleted it at once.
- **Directories of earlier tasks kept:** `agent-path-to-running-product` (branch `task/agent-path-to-running-product`: not merged as far as git can see on the target branch, or merged by squash, or its request open or closed); `base-check-stage-remarks` (detached: the branch `task/stage-remarks` its name gives is not found); `base-fix-minor-findings` (detached: the branch `task/minor-findings` its name gives is not found).

## Foundation entries

The part map's `elements-common` gained the line for the module that reads the files and git for the check (`4066ae5`). No topical section of the decision log was opened, no kept row tied to an entry stated earlier was written, no invariant was written, changed or marked violated, and no glossary term, environment fact or projected entry was written.

- **WAY-139** — marked `the cycle's` (row 1 settles the sentence; the pair is not the row's). Each item of a task's *To do* that writes into the skill the answer to how to read the logs, how long the record lives or how a human learns of a failure, or the record of the human's refusal, points to the guide too. Added pair: *complies* — "the item that writes into the skill the answer a decision gives for how a human learns of a failure, or the record of the human's refusal to settle it, points to the guide as well"; *violates* — "an item that writes into the skill the answer for how to read the logs, how long the record lives or how a human learns of a failure names no guide".
- **WAY-344** — marked `row 3`. Where a script that checks the form of a file reads that file's copy at the commit the branch left, a field it needs for a comparison and finds missing there is listed by a `listed:` line naming the entry and the field, with no error and no change of the exit code. Its two tests hold the sentence by a line `decision:`; no pair was added.
- **WAY-60** — marked `the cycle's` (row 5 settles the sentence; the pair is not the row's). A decision identifier written into an invariant's sentence because the decision holds the condition is part of the condition, not a link WAY-17 requires; the link stands beside the sentence in its own field. Added pair: *complies* — "an invariant of the-way whose sentence reads "as WAY-309 names them", the condition standing in that decision of its own log, has WAY-309 also in its *Derives from*, the link WAY-17 requires"; *violates* — "an invariant whose entry has the link WAY-17 requires only as the identifier in its sentence, with no field of its own for it".
- **WAY-61** (*Scope* only) — marked `the cycle's` (To do 15, no row). The scope of the decision on an invariant's method of checking names `task-cycle` as well.
- **WAY-229** — marked `the cycle's` (To do 20, no row). The strongest class available is the strongest of the models the session's settings allow, taken from `availableModels`, never from the name of the strongest model of the family; its *Verification* gained the example "a review is asked for on the strongest model of the family while the session's settings keep that model out" as a violation, and the complies example now reads "…the orchestrator taking it from the models the session's settings allow".
- **WAY-160** (*Rationale* only) — marked `the cycle's` (To do 14, no row). The focused checks of a slice are those of the code it reaches and of the invariants its change may make false.
- **Rows without an entry:** rows 2 (the three guidelines templates), 4 (`elements/decisions/template.md`, `task-cycle/skill/foundation_step.md`), 6 and 8 (`task-cycle/plan/SKILL.md`), 7 (`project-level/task/template.md`) and 9 (`task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`) are written in those files by their own rules.
- **Tests holding a decision's sentence by a line `decision:`:** two tests of `elements/common/test_foundation_check.py` now hold WAY-344 by a line `decision:`; a line `decision: WAY-03 "The listing stops no change"` of the test they replace is dropped with that test.

## Minor findings

- **r1 (return step review, within the task):** "The README's sentence on the base-copy listing drops 'that reads `test`'. `agent-instructions/README.md:17-18`: 'an invariant whose sentence a change rewords and whose copy at that commit lacks *Method* or *Part* it lists too, naming the field, whether or not a file citing it changes.' The code lists only an invariant whose *Method* reads `test` now (`elements/common/foundation_check.py:737-739`) … A reader of the README would expect a line for a `review` invariant and take its absence for a fault. … Blocks nothing."
- **r2 (return step review, within the task):** "The template row reads as if the listed line says whether a citing file changed. `elements/invariants/template.md:176`: 'and, naming the field and whether or not a file citing it changed, one that reads `test` whose reworded sentence's copy at the base lacks *Method* or *Part* (WAY-344)'. … the line names the invariant and the field only (`foundation_check.py:742-745`). … Form only; the content agrees with the code."
- **r3 (return step review, within the task):** the meaning sentence of WAY-344 that the earlier reports held was broader than the corrected entry; the reviewer gave a sentence to carry, and this description carries it (Foundation entries). Nothing in a commit is left to fix.

## Findings outside the task's scope

1. **o1 (review of the whole change):** "The request's section 6 gives one sentence of an entry's meaning, not the pair of examples that made it `the cycle's`. `task-cycle/skill/request_template.md:295-297`. Row 9's aim is that the human sees an added pair before merging; section 6 asks only for 'one plain sentence of its meaning', so an entry that is `the cycle's` only by its pair can still reach the human without the pair. The task carries only items 17 and 18 for this, so the template's section is outside it. Minor."

## Course of the cycle

- **Task and sources:** the task "the way: drobne poprawki po PR-ach #93 i #117–#121", independent, items 1, 2 and 5–20 of its *To do* and rows 1–9 of its *Settlements to record*; its frozen copy is in the record. Sources: the base `b6b3416` of `foundations`.
- **Process pin:** none; the-way is the process.
- **Spec:** none — no open design choice; the technique of the gate test's fix and the wording of the clauses were choices of how to make what the task settles.
- **Route:** one author without a plan (Sonnet 5.5, the orchestrator's class), because one agent could hold the change; reviews on Opus 5.5.
- **Plan:** none.
- **Choices:** 6 choices of the cycle beyond the task's content (items 2–7 above), in the questions table of the record (link added after the record is committed).
- **Blocking findings left:** none; the two Important findings of the review of the whole change were fixed and the fix passed its review.
- **Record:** written and checked after this description; its link is added once the record is committed.

