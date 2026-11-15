**State: ready** — corrected for your answer to an item of this request; nothing below waits for your answer now, and everything is accepted by merging.

## What you will see

A set of small corrections to the-way's process, left over from five earlier merged changes (#93 and #117 to #121), made in one change, and then corrected once for your answer on the first version. How the work with the process changes:

- The gate's test that checks directories run at the same time no longer loses lines at random on Windows. The helper that records the start and end of each test used to append to one shared file, and two processes writing at the same moment lost lines; that was the real cause of the random red in #117, which that request called "a busy machine". Now each event is a small file of its own. The test still fails when the directories run one after another, and still waits 120 seconds.
- The step that checks a deployment skill's list now sends the author to the guide for writing that skill also when a task item writes into it how to read the logs, how long the record lives, or how a human learns of a failure, or records your refusal to settle one of them.
- The three guideline templates (code, tests, screens) say that a choice the task did not settle stops the cycle only when the choice carries a real cost; a rule that only says how to write is the cycle's own, and you accept it at the merge.
- The foundation check now prints one extra line for an invariant that reads a test, whose sentence was reworded, when its copy at the point the branch left the main branch lacks its method or its part, naming the missing field. Before, it skipped such an invariant without a word. The exit code does not change. The same check also stops reading a full stop and a space inside a quotation — straight, curly or the Polish low-high form — as the end of a sentence.
- The decision template says what the "rejected ways" of a decision the cycle wrote from its own choice holds: `unknown`, unless a statement of yours names the ways weighed. The invariant template and the rule for decisions explain that a decision number written into an invariant's sentence, because that decision holds its condition, is part of the condition and no link.
- A task document can now carry the status "dropped — approved by human", the same words as a plan's task.
- The plan skill asks a slice's checks to run the tests of the invariants its change may break, not of every invariant it reaches, and tells a slice that writes an invariant whose test a later slice writes to run the foundation check with the switch that skips the missing-test report.
- When the cycle adds to an entry written from a row of your settlements, or to an entry designed in advance, a part the row or the design does not give — a pair of examples, a field left open — the entry is marked as the cycle's and put before you at the merge. A link added to the entry does not do that. After your answer, the description of the request also shows that added pair word for word under the entry, which the first version did not; this request does it for its own entries.
- The strongest model for the review of the whole change and of the return step is the strongest the session's settings allow, not the strongest name of the model family.
- Two descriptions of the foundation check's extra line now say what the code does: it concerns an invariant that reads a test, and the line names the invariant and the field only.

### Underneath

The script of the foundation check was three lines over the 1000-line cap, so the code that reads files and asks git moved first, unchanged, into a new module of its own. The gate ran on the final state after the correction and passed (1600 tests in 11 directories).

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The gate's test module records each event as an empty file in a directory, named by the time in nanoseconds and the text, and reads the files back in order. The other ways were one file per process, which loses the order across processes that two tests read, and an explicit lock, which spins on Windows because a file another process is opening cannot be deleted. Before the change a trial with three processes started together lost a line in 19 of 20 runs; after it, in none of 20, and six runs of the gate's directory in a row passed. As you settled, no permanent test of the loss itself was added.
2. The extra line of the foundation check for an invariant with a missing field in the base copy appears also when a file that cites the invariant changed. The other way, listing it only when no citing file changed, would hide the very case the line is for. An invariant that lacks a field now is still an error as before, and one whose sentence did not change gets no line.
3. The code that reads files and git moved into a new module, because the check script stood at 1003 lines over a cap of 1000 and two items of the task add to it. The other way, moving the readers of text as well, is a larger move that changes what another script imports. The other task that changes the same script and the same decision sentence, which the task left without a dependency, will have to be reconciled by whichever of the two merges second.
4. In three places I went slightly beyond the words of the task so that the sentences read whole: the pointer to the guide also covers the item that records your refusal to settle; the three templates also say that a rule that only says how to write is the cycle's own, which you accept at the merge, taken from the decision on guidelines; and the rule on marking entries says in the same sentence that a link added to an entry does not change its mark, which the task said in the next sentence.
5. The decision on the model class now names the setting in Claude Code, and says that where the session has no such list the strongest of every model it offers is taken. Its rationale says that a request for a model outside the list got another model, in the one session observed the session's own; I wrote it as an observation, since the only source is that session's record and no document of the tool.
6. The task text said the code of two parts is exempt from the coding and testing guidelines; that exemption was withdrawn before this task started, so the code and the tests of this change follow the guidelines, and nothing was changed in the withdrawn decision.
7. For your answer on the added pair of examples, the rule in the template of the description reaches only an entry that is the cycle's because of an added pair; an entry whose pair is kept only until a test of the same change holds the sentence, an entry whose only addition is a link, and an entry marked for another reason do not get it. The foundation step also tells the writer to keep the added pair word for word in its report, since the description's writer has nothing else to quote from. And the decision on what the request puts before you now says the same in its binding sentence, its check and one rejected way, so that the decision and the rule agree; I held this a clarification of what you asked, not a change of what the decision means. The other way was to leave the decision as it stood, which would have left the decision and the template disagreeing.
8. Six entries of the foundation are marked as the cycle's, which you did not see at the task, each with one plain sentence of its meaning:
   - the decision on the guide for a deployment skill gained a pair of examples: an item that records the answer or your refusal points to the guide too, and an item that names no guide does not comply;
   - the decision on where a condition that decides an invariant may stand gained a pair: a number of a decision written into the sentence is part of the condition, and the link stands beside it in its own field;
   - the decision on what the request puts before you now says that an entry marked the cycle's for an added pair of examples has that pair shown under it, and gained a pair that says so;
   - the decision on how an invariant's method is written now also lists the task cycle among the parts it concerns;
   - the decision on the class of model of the one author names the strongest of the models the session's settings allow, and gained two example clauses that say so;
   - the rationale of the decision on how the gate is run says a slice's checks are the tests of the code it reaches and of the invariants its change may break.
   The added pairs stand word for word under the entries in the lower part (Foundation entries).
9. Changed tests and surfaces: a test that said a reworded invariant lacking a field in the base copy gets no line was replaced by tests that say it gets one line, and two of them hold the sentence of the decision on missing fields by a line that quotes it; one test now checks a quotation with a full stop inside. No invariant was written, changed or marked violated. The foundation check keeps its path, its argument and its exit codes; on the final tree it reports no errors and no extra lines.
10. This correction answered your answer to the item on unfixed findings. The cycle judged that the task did not require the rule on the added pair, which you asked for, and that the foundation did require the two descriptions of the listing to match the code.

## Cost

About one hour and twenty minutes of working time across 51 stages (about forty minutes of it waiting for tools), 94.1 million tokens (70.1 million on Sonnet 5.5, 23.9 million on Opus 5.5), five reviews — the whole change, which failed; its fix; the return step; the correction, which failed on one point; and its fix — one fix after the first failed review, one correction and one corrected account after the second, and two full runs of the gate (513 and 427 seconds). The table of stages is in the record, whose link is added to this description once the record is committed. Three directories of earlier tasks still stand because the script that removes finished ones could not tell they were no longer needed; nothing in this request waits for them, and you may remove them by hand (names in Checks).

## How to merge

Merge so that the commits are kept (the repository's own pull requests are merged as "Merge pull request"), since the link to the record survives only then. After the merge, the check of task notes in your notes vault has to start recognising the new status word of a dropped task; the task left that to the day advisor or to you, and nothing in this request waits for it.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — poprawione pod Twoją odpowiedź na pozycję tej prośby; nic poniżej nie czeka na Twoją odpowiedź, a wszystko jest przyjmowane przez scalenie.

## Co zobaczysz

Zestaw drobnych poprawek procesu the-way, które zostały po pięciu wcześniej scalonych zmianach (#93 oraz #117–#121), zrobiony jedną zmianą, a potem raz poprawiony pod Twoją odpowiedź na pierwszą wersję. Jak zmienia się praca z procesem:

- Test bramki sprawdzający, że katalogi biegną naraz, przestaje losowo gubić linie na Windows. Pomocnik zapisujący start i koniec każdego testu dopisywał do jednego wspólnego pliku, a dwa procesy piszące w tej samej chwili gubiły linie; to była prawdziwa przyczyna losowej porażki w #117, którą tamta prośba nazwała „zajętą maszyną”. Teraz każde zdarzenie to osobny mały plik. Test dalej pada, gdy katalogi biegną jeden po drugim, i dalej czeka 120 sekund.
- Krok sprawdzający listę skilla wdrożeniowego kieruje autora do przewodnika po pisaniu tego skilla także wtedy, gdy punkt zadania wpisuje do niego, jak czytać logi, jak długo żyje zapis albo skąd człowiek dowiaduje się o awarii, albo zapisuje Twoją odmowę rozstrzygnięcia którejś z tych spraw.
- Trzy szablony wytycznych (kod, testy, ekrany) mówią, że wybór nierozstrzygnięty przez zadanie zatrzymuje cykl tylko wtedy, gdy niesie realny koszt; reguła, która tylko mówi, jak pisać, jest własna dla cyklu i przyjmujesz ją przy scaleniu.
- Kontrola fundamentu wypisuje jedną dodatkową linię dla niezmiennika z metodą `test`, którego zdanie przeredagowano, a którego kopia z miejsca, w którym gałąź odeszła od głównej, nie ma metody albo części — z nazwą brakującego pola. Wcześniej taki niezmiennik pomijała bez słowa. Kod wyjścia się nie zmienia. Ta sama kontrola przestaje też czytać kropkę ze spacją wewnątrz cytatu — prostego, kręconego albo polskiego dolno-górnego — jako koniec zdania.
- Szablon decyzji mówi, co wpisać w „odrzucone drogi” decyzji, którą cykl zapisał z własnego wyboru: `unknown`, chyba że Twoja wypowiedź nazywa rozważone drogi. Szablon niezmienników i reguła dla decyzji wyjaśniają, że numer decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem.
- Dokument zadania może mieć status „dropped — approved by human”, te same słowa co zadanie planu.
- Skill planu każe w sprawdzeniach kawałka uruchamiać testy niezmienników, które zmiana kawałka może zepsuć, a nie każdego, do którego kawałek sięga, i każe kawałkowi, który zapisuje niezmiennik z testem pisanym przez późniejszy kawałek, uruchomić kontrolę fundamentu z przełącznikiem pomijającym zgłoszenie braku testu.
- Gdy cykl dopisze do wpisu z wiersza Twoich ustaleń albo do wpisu zaprojektowanego z góry część, której wiersz ani projekt nie dają — parę przykładów, pole zostawione otwarte — wpis dostaje oznaczenie „cyklu” i trafia przed Ciebie przy scaleniu. Powiązanie dopisane do wpisu tego nie robi. Po Twojej odpowiedzi opis prośby pokazuje też tę dopisaną parę słowo w słowo pod wpisem, czego pierwsza wersja nie robiła; ta prośba robi to dla własnych wpisów.
- Najmocniejszy model do przeglądu całej zmiany i kroku powrotu to najmocniejszy z dozwolonych w ustawieniach sesji, a nie najmocniejsza nazwa rodziny modeli.
- Dwa opisy dodatkowej linii kontroli fundamentu mówią teraz to, co robi kod: dotyczy niezmiennika z metodą `test`, a linia nazywa tylko niezmiennik i pole.

### Pod spodem

Skrypt kontroli fundamentu miał o trzy linie za dużo ponad limit 1000 linii, więc kod czytający pliki i pytający gita przeniesiono najpierw, bez zmian, do osobnego nowego modułu. Bramka przeszła na stanie końcowym po poprawce (1600 testów w 11 katalogach).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawy albo przepuszczenia

none

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; powiedz, która Ci nie odpowiada.

1. Moduł próbny testów bramki zapisuje każde zdarzenie jako pusty plik w katalogu, nazwany czasem w nanosekundach i tekstem, i odczytuje pliki z powrotem po kolei. Inne drogi to jeden plik na proces, który gubi kolejność między procesami, a ją czytają dwa testy, i jawna blokada, która kręci się w pętli na Windows, bo pliku otwieranego przez inny proces nie da się skasować. Przed zmianą próba z trzema procesami startującymi razem gubiła linię w 19 z 20 przebiegów, po niej w żadnym z 20, a sześć kolejnych przebiegów katalogu bramki przeszło. Jak ustaliłeś, nie dodano stałego testu samej utraty linii.
2. Dodatkowa linia kontroli fundamentu dla niezmiennika z brakującym polem w kopii bazowej pojawia się także wtedy, gdy plik cytujący niezmiennik się zmienił. Druga droga, wypisanie tylko gdy żaden plik cytujący się nie zmienił, ukryłaby właśnie ten przypadek, dla którego linia istnieje. Niezmiennik, któremu pola brakuje teraz, nadal jest błędem jak dotąd, a taki, którego zdanie się nie zmieniło, nie dostaje linii.
3. Kod czytający pliki i git przeniesiono do nowego modułu, bo skrypt kontroli miał 1003 linie przy limicie 1000, a dwa punkty zadania mu dokładają. Druga droga, przeniesienie także czytników tekstu, to większe przeniesienie, które zmienia to, co importuje inny skrypt. Drugie zadanie, które zmienia ten sam skrypt i to samo zdanie decyzji, a które zadanie zostawiło bez zależności, będzie musiało zostać pogodzone przez to z dwóch, które scali się później.
4. W trzech miejscach poszedłem odrobinę dalej niż słowa zadania, żeby zdania czytały się całe: wskazanie przewodnika obejmuje też punkt, który zapisuje Twoją odmowę rozstrzygnięcia; trzy szablony mówią też, że reguła, która tylko mówi, jak pisać, jest własna dla cyklu i przyjmujesz ją przy scaleniu, co wzięto z decyzji o wytycznych; a reguła oznaczania wpisów mówi w tym samym zdaniu, że powiązanie dopisane do wpisu nie zmienia jego oznaczenia, co zadanie mówiło w następnym zdaniu.
5. Decyzja o klasie modelu nazywa teraz ustawienie w Claude Code i mówi, że gdy sesja nie ma takiej listy, bierze się najmocniejszy z każdego modelu, jaki oferuje. Jej uzasadnienie mówi, że prośba o model spoza listy dostała inny model, w jednej obserwowanej sesji model sesji; zapisałem to jako obserwację, bo jedynym źródłem jest zapis tej sesji, a nie dokument narzędzia.
6. Tekst zadania mówił, że kod dwóch części jest wyłączony spod wytycznych kodowania i testowania; to wyłączenie wycofano przed rozpoczęciem tego zadania, więc kod i testy tej zmiany idą za wytycznymi, a w wycofanej decyzji niczego nie zmieniono.
7. Pod Twoją odpowiedź o dopisanej parze przykładów reguła w szablonie opisu obejmuje tylko wpis, który jest „cyklu” z powodu dopisanej pary; nie obejmuje wpisu, którego para jest trzymana tylko do czasu, aż test tej samej zmiany utrzyma zdanie, wpisu, do którego dopisano tylko powiązanie, ani wpisu oznaczonego z innego powodu. Krok fundamentu mówi też autorowi, żeby zachował dopisaną parę słowo w słowo w swoim raporcie, bo piszący opis nie ma skąd jej wziąć. A decyzja o tym, co prośba stawia przed Tobą, mówi teraz to samo w zdaniu wiążącym, sprawdzeniu i jednej odrzuconej drodze, żeby decyzja i reguła się zgadzały; uznałem to za doprecyzowanie tego, o co prosiłeś, a nie zmianę znaczenia decyzji. Druga droga to zostawić decyzję bez zmian, co zostawiłoby decyzję i szablon w rozjeździe.
8. Sześć wpisów fundamentu ma oznaczenie „cyklu”, czyli nie widziałeś ich przy zadaniu, każdy z jednym prostym zdaniem znaczenia:
   - decyzja o przewodniku po skillu wdrożeniowym dostała parę przykładów: punkt zapisujący odpowiedź albo Twoją odmowę wskazuje też przewodnik, a punkt, który nie wskazuje żadnego, nie jest zgodny;
   - decyzja o tym, gdzie może stać warunek rozstrzygający niezmiennik, dostała parę: numer decyzji wpisany w zdanie jest częścią warunku, a powiązanie stoi obok w swoim polu;
   - decyzja o tym, co prośba stawia przed Tobą, mówi teraz, że wpis oznaczony „cyklu” z powodu dopisanej pary przykładów ma tę parę pokazaną pod sobą, i dostała parę, która to mówi;
   - decyzja o zapisie metody niezmiennika wymienia teraz także część „cykl zadania”;
   - decyzja o klasie modelu jednego autora nazywa najmocniejszy z modeli dozwolonych w ustawieniach sesji i dostała dwa zdania przykładów, które to mówią;
   - uzasadnienie decyzji o uruchamianiu bramki mówi, że sprawdzenia kawałka to testy kodu, do którego sięga, i niezmienników, które jego zmiana może zepsuć.
   Dopisane pary stoją słowo w słowo pod wpisami w dolnej części (Foundation entries).
9. Zmienione testy i powierzchnie: test mówiący, że przeredagowany niezmiennik z brakującym polem w kopii bazowej nie dostaje linii, zastąpiono testami mówiącymi, że dostaje jedną linię, a dwa z nich trzymają zdanie decyzji o brakującym polu linią, która je cytuje; jeden test sprawdza teraz cytat z kropką w środku. Żaden niezmiennik nie został napisany, zmieniony ani oznaczony jako naruszony. Kontrola fundamentu zachowuje swoją ścieżkę, argument i kody wyjścia; na stanie końcowym nie zgłasza błędów ani dodatkowych linii.
10. Ta poprawka odpowiedziała na Twoją odpowiedź na pozycję o nienaprawionych ustaleniach. Cykl uznał, że zadanie nie wymagało reguły o dopisanej parze, o którą prosiłeś, a fundament wymagał, żeby dwa opisy wypisywanej linii zgadzały się z kodem.

## Koszt

Około godziny i dwudziestu minut pracy w 51 etapach (około czterdziestu minut z tego to czekanie na narzędzia), 94,1 miliona tokenów (70,1 miliona na Sonnecie 5.5, 23,9 miliona na Opusie 5.5), pięć przeglądów — całej zmiany, który nie przeszedł; jego poprawki; kroku powrotu; poprawki, która nie przeszła w jednym punkcie; i jej naprawy — jedna poprawka po pierwszym nieudanym przeglądzie, jedna korekta i jeden poprawiony zapis po drugim oraz dwa pełne uruchomienia bramki (513 i 427 sekund). Tabela etapów jest w zapisie; link do niego zostanie dopisany do tego opisu po zatwierdzeniu zapisu. Trzy katalogi wcześniejszych zadań nadal stoją, bo skrypt usuwający zakończone nie umiał stwierdzić, że już nie są potrzebne; nic w tej prośbie na nie nie czeka, możesz je usunąć ręcznie (nazwy w Checks).

## Jak scalić

Scal tak, żeby commity zostały (własne prośby repozytorium scala się jako „Merge pull request”), bo link do zapisu przeżywa tylko wtedy. Po scaleniu sprawdzanie notatek zadań w Twoim vaulcie musi zacząć rozpoznawać nowe słowo statusu zadania, z którego zrezygnowano; zadanie zostawiło to doradcy dnia albo Tobie, a nic w tej prośbie na to nie czeka.

</details>

## Technical changes

The change is ten commits on the base `b6b3416`, in six groups. The corrections of items 3 and 4 of the task were withdrawn or moved before the cycle and were not made.

- **Gate test (To do 1 and 2):** `677ad78` — `gate/test_run_tests.py`: `log_event` and `logged_events` write and read one empty file per event in a directory `timeline`; `timed_module` embeds their source; the wait of 120 seconds and the test that fails when directories run one after another are unchanged. No test of the loss was added, as settled.
- **Move before the code that adds (To do 8 and 19):** `ac3c96f` — `git`, `fork_point`, `at_commit`, `read` and `MAIN_BRANCHES` moved as they stood from `elements/common/foundation_check.py` into the new `elements/common/foundation_source.py`; no change of behaviour.
- **Foundation check (To do 8 and 19):** `76c2bd2`, `b23275b` — one line for a reworded invariant that reads `test` whose base copy lacks *Method* or *Part*, naming the field, listed whether or not a citing file changed; a full stop inside `"…"`, `“…”` or `„…”` no longer begins a sentence; tests for each; the two descriptions of the listing.
- **Decisions, templates and skills (To do 5–7, 9–18, 20):** `52b122b`, `e9aea95`, `eaf815c` — the decisions WAY-139, WAY-344, WAY-60, WAY-61 and WAY-229 in place and the rationale of WAY-160; the templates of decisions, invariants, tasks and the three guidelines; the skills of plan, cycle, foundation step and decisions, and the step that checks a deployment skill's list; the fixes of the first review's findings.
- **Return step:** `4066ae5` — WAY-344's sentence narrowed to "a field it needs for a comparison", its two added clauses of examples removed because its tests hold them, the two descriptions of the listing and the part map's line for `elements-common` made to match the code.
- **Correction 1 (your answer on the added pair):** `5cb2e1f` — `task-cycle/skill/request_template.md` (the rule on the added pair, in the item of the top part and in *Foundation entries*), one clause in `task-cycle/skill/foundation_step.md`, WAY-114 changed in place (binding sentence, *Verification*, *Rejected*), the README sentence and the invariants-template row made to match the code.

## Checks

- **Gate:** `python -B task-cycle/gate_times.py --output docs/task-cycles/small-fixes-after-prs-117-121/gate_times.md -- python -B gate/run_tests.py` on head `5cb2e1f` (the code after correction 1), Windows, after the day advisor's start signal: exit 0, 1600 tests in 11 directories, every directory passed, 426.665 s. The first run, on `4066ae5`, before the correction: exit 0, 1600 tests, 513.087 s. The random test of directories at the same time did not fail in either run.
- **Failing on the base:** none. The base `b6b3416` is a merge commit whose tree equals the tree of its second parent, so the gate was not run on it; the list is taken from the final gate of the merged cycle (`docs/task-cycles/the-way-coding-and-testing-guidelines/cycle.md`, added by commit `a0ffa80`): exit 0, 1596 tests, every directory passed.
- **Foundation check:** `python -B elements/common/foundation_check.py` without `--skip-test-citations` on head `5cb2e1f`: exit 0, `0 errors`, no `listed:` line.
- **Own-work checks:** the author's checks of its most doubtful requirement in each report (the loss of lines gone; the quotation form; the narrowed sentence; the three remarks of the correction) show what each report states; focused runs of the directories of the touched parts passed in each report, the correction's included (`task-cycle` 534, `agent-instructions` 37, `product-guidelines` 14, `elements/common` 246). No test reads the wording of the request template, so its review is what reads the new rule.
- **Reviews:** whole change `FAIL e9aea95` (two Important, eight Minor, one outside scope), review of its fix `PASS eaf815c`, review of the return step `PASS 4066ae5` (three Minor), review of the correction `FAIL 5cb2e1f` (one Important, two Minor) and review of its fix `PASS 5cb2e1f` (one Minor); all by agents on Opus 5.5, as asked.
- **Form check:** `python -B task-cycle/request_check.py <description> --task <frozen task>` — last run exit 0. **Private paths on the description:** `python -B task-cycle/private_paths_check.py <description>` — last run exit 0, 0 listed. **Copy of the record** (`docs/task-cycles/small-fixes-after-prs-117-121`, committed and removed by the next commit): pending until the record is committed. **CI on the request:** pending until the record is committed.
- **Working copies:** none stand. One agent ran a throwaway script from the system's temporary directory against the working-copies rule and deleted it at once.
- **Directories of earlier tasks kept:** `agent-path-to-running-product` (branch `task/agent-path-to-running-product`: not merged as far as git can see on the target branch, or merged by squash, or its request open or closed); `base-check-stage-remarks` (detached: the branch `task/stage-remarks` its name gives is not found); `base-fix-minor-findings` (detached: the branch `task/minor-findings` its name gives is not found).

## Foundation entries

The part map's `elements-common` gained the line for the module that reads the files and git for the check (`4066ae5`). No topical section of the decision log was opened, no kept row tied to an entry stated earlier was written, no invariant was written, changed or marked violated, and no glossary term, environment fact or projected entry was written.

- **WAY-139** — marked `the cycle's` (row 1 settles the sentence; the pair is not the row's). Each item of a task's *To do* that writes into the skill the answer to how to read the logs, how long the record lives or how a human learns of a failure, or the record of the human's refusal, points to the guide too. Added pair: *complies* — "the item that writes into the skill the answer a decision gives for how a human learns of a failure, or the record of the human's refusal to settle it, points to the guide as well"; *violates* — "an item that writes into the skill the answer for how to read the logs, how long the record lives or how a human learns of a failure names no guide".
- **WAY-344** — marked `row 3`. Where a script that checks the form of a file reads that file's copy at the commit the branch left, a field it needs for a comparison and finds missing there is listed by a `listed:` line naming the entry and the field, with no error and no change of the exit code. Its two tests hold the sentence by a line `decision:`; no pair was added.
- **WAY-60** — marked `the cycle's` (row 5 settles the sentence; the pair is not the row's). A decision identifier written into an invariant's sentence because the decision holds the condition is part of the condition, not a link WAY-17 requires; the link stands beside the sentence in its own field. Added pair: *complies* — "an invariant of the-way whose sentence reads "as WAY-309 names them", the condition standing in that decision of its own log, has WAY-309 also in its *Derives from*, the link WAY-17 requires"; *violates* — "an invariant whose entry has the link WAY-17 requires only as the identifier in its sentence, with no field of its own for it".
- **WAY-114** (binding sentence, *Verification*, *Rejected*; changed by correction 1) — marked `the cycle's` (no row carries it; your answer settles the rule of the request template, not this entry's wording or its examples). The lower part of the request's description shows, under an entry marked as the cycle's because of a pair of examples its writer added, that pair word for word, so that the human merges the examples that agents will measure later changes by having seen them. Added pair: *complies* — "and an entry that gained a pair of examples the row did not give has the pair there word for word"; *violates* — "an entry marked as the cycle's for an added pair of examples reaches the merge with the pair not shown". Also changed, not a pair: the end of the binding sentence ("and an entry that is marked as the cycle's because of a pair of examples its writer added has that pair there word for word under it") and one way of *Rejected* ("the sentence of meaning alone for an entry that gained a pair of examples — the examples are what agents measure every later change by, and a sentence of meaning does not show them").
- **WAY-61** (*Scope* only) — marked `the cycle's` (To do 15, no row). The scope of the decision on an invariant's method of checking names `task-cycle` as well.
- **WAY-229** — marked `the cycle's` (To do 20, no row). The strongest class available is the strongest of the models the session's settings allow, taken from `availableModels`, never from the name of the strongest model of the family. Its two added clauses of its pair, word for word: *complies* — "the orchestrator taking it from the models the session's settings allow"; *violates* — "a review is asked for on the strongest model of the family while the session's settings keep that model out".
- **WAY-160** (*Rationale* only) — marked `the cycle's` (To do 14, no row). The focused checks of a slice are those of the code it reaches and of the invariants its change may make false.
- **Rows without an entry:** rows 2 (the three guidelines templates), 4 (`elements/decisions/template.md`, `task-cycle/skill/foundation_step.md`), 6 and 8 (`task-cycle/plan/SKILL.md`), 7 (`project-level/task/template.md`) and 9 (`task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`) are written in those files by their own rules.
- **Tests holding a decision's sentence by a line `decision:`:** two tests of `elements/common/test_foundation_check.py` now hold WAY-344 by a line `decision:`; a line `decision: WAY-03 "The listing stops no change"` of the test they replace is dropped with that test.

## Minor findings

- **m1 (review of correction 1, within the task):** "'each as the entry holds it' can be read as quoting the whole *complies*/*violates* field, not the added clause." The place is the *Foundation entries* paragraph of `task-cycle/skill/request_template.md`; the foundation step says only the added pair.
- **m2 (review of correction 1, within the task):** "One line of WAY-114's binding sentence is not rewrapped." The line stands in `foundations/decisions.md` in the binding sentence of WAY-114 and is 131 characters where its neighbours wrap at about 100.
- **m1 (review of the fix of correction 1, within the task):** WAY-229's added *complies* clause should be quoted under it too, as for WAY-114; this description quotes both clauses (Foundation entries), so the finding stands only as a record.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task "the way: drobne poprawki po PR-ach #93 i #117–#121", independent, items 1, 2 and 5–20 of its *To do* and rows 1–9 of its *Settlements to record*; its frozen copy is in the record. Sources: the base `b6b3416` of `foundations`.
- **Process pin:** none; the-way is the process.
- **Spec:** none — no open design choice; the technique of the gate test's fix and the wording of the clauses were choices of how to make what the task settles.
- **Route:** one author without a plan (Sonnet 5.5, the orchestrator's class), because one agent could hold the change; reviews on Opus 5.5. Correction 1 by the same author, resumed; no reset.
- **Plan:** none.
- **Choices:** 7 choices of the cycle beyond the task's content (items 1–7 above), in the questions table of the record (link added after the record is committed).
- **Corrections after the request opened:** correction 1, your remarks https://github.com/mariusznazar/the-way/pull/137#issuecomment-6902888817, copied word for word in the record (`reports/correction-1-remarks.md`); no reset, the branch continued from `aefe984`.
- **Blocking findings left:** none; the Important finding of the review of the whole change and the Important finding of the review of correction 1 were fixed and their fixes passed review.
- **Record:** written and checked after this description; its link is added once the record is committed.
