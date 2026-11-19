**State: ready** — three items in *Fix or let through* wait for your answer; everything else you only accept by merging.

## What you will see

The Python code of the process is now kept in order by two checks that the gate enforces instead of two checks it only pretended to run.

- **One layout for all Python code.** The code is laid out by one automatic formatter at a line width of 100, in one commit that changes nothing but layout. A new list tells `git blame` to skip that one commit, so that blame still names the real author of every line. From now on a file that is out of the formatter's layout, or that switches the formatter off with a comment, turns the gate red.
- **The linter rules hold.** All 24 reports of the blocking linter rules are fixed in the files that held them, with no rule turned off. The test of the linter is no longer an "expected failure": a new violation turns the gate red.
- **The size rule holds, at new thresholds.** A function may have 110 lines and a script file 1200, counted on the formatted code (the old 80 and 1000 were counted on code with no formatter, and the formatter makes code longer). The 11 functions and 2 files over the new thresholds were divided into named parts and modules, and the test of the size rule is no longer an "expected failure" either. The big audit command was cut into five modules, and the report of the stages of a cycle into two.
- **The whole check of the foundation runs in the gate.** A broken reference in the foundation, such as a number that names no decision, now turns the gate red under a rule of its own, and the test passes whatever the main branch of a clone is called.
- **A flaky test is steadied.** The test of the removal of finished working directories failed at random on Linux; it no longer depends on Git's background maintenance.
- **One word, one meaning.** The word "entry" stays for an entry of the foundation; elsewhere the plan's change log, the registry of running gates and the items of a record's list now use their own words.

Nothing a user of the process runs behaves differently: every moved or divided script gave the same output, exit code and messages as before on crafted input, as the reviews compared.

### Underneath

The reformatting touched 78 files in one commit that a second run of the formatter reproduces byte for byte; the divisions came after it, because the thresholds count formatted code.

## For you to decide

### Needed from you

none

### Fix or let through

1. The formatter removed the brackets around two error types in 14 `except` lines, a form that only Python 3.14 reads. Eleven files no longer load on an older Python, where they loaded before. The process declares 3.14 as its Python and CI runs it, so nothing it promises breaks; a person or a product that runs these checks on an older Python, which worked by accident, would now see a syntax error at once. Letting it through costs nothing today and undoing it later costs a round of correction. Keeping the brackets needs a formatter setting other than its default and a change to the decision on the formatter, so it costs another round with a review; undoing it costs the same. Making a task of it leaves the code as it is until someone does it, and costs nothing now. I recommend letting it through, since 3.14 is the Python the process states as required. Its weak point: the base ran on an older Python by luck, so a product that updates the pinned process on an older Python will find the break only then. Keep the brackets in this request, make a task of it, or let it through? (Minor findings, 1)
2. I could not make the random failure of the worktree-removal test happen again, so the fix, which turns off Git's background maintenance in that test, is not proven. If the cause was another one, a Linux check fails at random on some later request, as it did on an earlier one, and costs a rerun and a question to whoever is waiting for the merge. Proving it takes repeated Linux runs of the check on this request, a few rounds of waiting for CI, and undoing it costs nothing. Making a task of it leaves it unproven. Letting it through accepts that risk; undoing it later costs a correction after the next random failure. I recommend letting it through, because the failure named the very file that background maintenance creates and removes. Its weak point: no run showed the failure before the fix either, so "the cause matches" is a reading, not a measurement. Repeat the Linux runs in this request, make a task of it, or let it through? (Checks, 4)
3. Three small things stay untidy, none of them wrong in what it does. Four test names in the audit's test file still use "entry" for an item of a record's list. The size decision does not name the formatter decision in its list of relations, though its counting rests on the formatter. One function of the installer stands at 109 lines against the limit of 110, so the next line added to it turns the gate red until a part is moved out. Fixing them in this request costs a round of correction with a review and makes the change larger; undoing it costs nothing. Making a task of them costs a little queue time later; undoing it, nothing. Letting them through costs a red gate the first time someone touches the installer function. I recommend making a task of them, since each is small and independent of this change. Its weak point: three more small tasks in a long queue may stay open for weeks. Fix them in this request, make a task of them, or let them through? (Minor findings, 2 and 3; Findings outside the task's scope, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. The audit of the process loses comparability across this change. The reformatting and the divisions change the tools that measure the cost, the remarks, the context and the gate times, so the audit starts new series of those measures at the version that holds this change, and this cycle's own measures come out as unknown. I took it as a consequence of the task as you settled it, since no other way keeps the thresholds and the formatter.
5. The ban on formatter-off comments is a little wider than your answer. You named three comments; Ruff's formatter also obeys two comments of another tool's spelling, which would let a file stay out of the layout with the gate green. I forbade those two as well, in the decision, in the rule of the formatter and in the guidelines' rule, so that the ban does what you asked it to do. If you want only the three, the widening is one line to take back.
6. Two sentences of the audit's rules now name both scripts that measure the cost of a cycle, not one. The division of the stage report moved its transcript-reading code into a second script; without the change a later edit of that code would start no new series of the cost, against what the rule means. This is one decision and one invariant of the foundation, worded the same, which you did not see at the task document.
7. Three words changed in the foundation, with the same meaning: the plan's change log, the registry of running gates and an invariant about that registry now say "line" or "file" where they said "entry". You did not see these at the task document either.
8. The map of the process's parts gained the new files: the blame-skip list belongs to the part for repository files, and three new audit modules and the new transcript module are named as files that read input from outside, so that the reviews of later changes check crafted input there. The formatter's decision now also covers the part for repository files, and one decision about the foundation check names the new check rule.
9. Two rules of the foundation left the state "violated" and no longer expect their tests to fail: the one for linter rules, and the one for function and file size. The tests that check them changed accordingly: the linter's test and the size test lost their "expected failure" mark; the size thresholds moved to 110 and 1200; the new layout test and the test of the whole check of the foundation are new. Two other rules had their sentence reworded with the same meaning (the registry of running gates; the scripts whose change starts a series of the cost), and the tests that cite them were changed to match, with no assertion weakened: the audit's series test now expects both cost files, and eleven tests of the record's list were renamed.

## Cost

About 6 hours 45 minutes of working time, of which 4 hours 8 minutes waited for tools, 277 million tokens in all (172 million on Sonnet, 60 million on Opus, 45 million on Haiku; 270 million of them read from a cache). Review rounds: ten reviews of single slices, all passing at the first reading; one review of the whole change; one round of correction for its ten Minor findings, with a review of that round; and one review of the return step. No slice was made twice. The table of the stages is in [the record](https://github.com/mariusznazar/the-way/blob/0d0130f686a43e6358fb8ed445b0234ad87064f2/docs/task-cycles/code-order-formatter-linter-size/stages.md).

## How to merge

Merge with a merge commit that keeps the commits. The link to the record survives only then, and so does the one reformatting commit whose hash the blame-skip list holds: a squash or a rebase would change that hash, and the list would point at nothing.

<details>
<summary>W twoim języku</summary>

**Stan: gotowe** — trzy pozycje w *Napraw albo przepuść* czekają na twoją odpowiedź; resztę tylko akceptujesz przez scalenie.

## Co zobaczysz

Kod Pythona procesu jest teraz utrzymywany w porządku przez dwie kontrole, które bramka naprawdę egzekwuje, zamiast dwóch, które tylko udawała.

- **Jeden układ całego kodu Pythona.** Kod jest ułożony przez jeden automatyczny formater przy szerokości linii 100, w jednym commicie, który zmienia wyłącznie układ. Nowa lista każe `git blame` pominąć ten jeden commit, więc blame nadal wskazuje prawdziwego autora każdej linii. Od teraz plik, który odbiega od układu formatera albo wyłącza formater komentarzem, zaczerwienia bramkę.
- **Reguły lintera obowiązują.** Wszystkie 24 zgłoszenia blokujących reguł lintera są naprawione w plikach, w których stały, bez wyłączania żadnej reguły. Test lintera nie jest już „oczekiwaną porażką”: nowe naruszenie zaczerwieni bramkę.
- **Reguła rozmiaru obowiązuje, z nowymi progami.** Funkcja może mieć 110 linii, a plik skryptu 1200, liczone na kodzie po formatowaniu (dawne 80 i 1000 liczono na kodzie bez formatera, a formater wydłuża kod). 11 funkcji i 2 pliki powyżej nowych progów podzielono na nazwane części i moduły, a test reguły rozmiaru też nie jest już „oczekiwaną porażką”. Duże polecenie audytu pocięto na pięć modułów, a raport etapów cyklu na dwa.
- **Pełne sprawdzenie fundamentu działa w bramce.** Zepsute odwołanie w fundamencie, na przykład numer, który nie wskazuje żadnej decyzji, zaczerwieni teraz bramkę pod osobną regułą, a test przechodzi bez względu na to, jak nazywa się główna gałąź klonu.
- **Niestabilny test jest uspokojony.** Test usuwania skończonych katalogów roboczych padał losowo na Linuksie; nie zależy już od konserwacji Gita w tle.
- **Jedno słowo, jedno znaczenie.** Słowo „entry” zostaje dla wpisu fundamentu; gdzie indziej dziennik zmian planu, rejestr uruchomień bramki i pozycje listy zapisu mają własne słowa.

Nic, co uruchamia użytkownik procesu, nie zachowuje się inaczej: każdy przeniesiony albo podzielony skrypt dał na spreparowanych wejściach to samo wyjście, ten sam kod wyjścia i te same komunikaty co przedtem, jak porównały recenzje.

### Pod spodem

Przeformatowanie objęło 78 plików w jednym commicie, który drugie uruchomienie formatera odtwarza bajt w bajt; podziały przyszły po nim, bo progi liczą kod sformatowany.

## Do rozstrzygnięcia

### Potrzebne od ciebie

none

### Napraw albo przepuść

1. Formater usunął nawiasy wokół dwóch typów błędów w 14 liniach `except`, w postaci, którą czyta dopiero Python 3.14. Jedenaście plików nie ładuje się już na starszym Pythonie, na którym przedtem się ładowały. Proces deklaruje 3.14 jako swój Python i CI go uruchamia, więc nic z tego, co obiecuje, się nie psuje; osoba albo produkt, które uruchamiają te kontrole na starszym Pythonie, co działało przypadkiem, zobaczą teraz od razu błąd składni. Przepuszczenie nic dziś nie kosztuje, a cofnięcie go później kosztuje rundę poprawki. Zachowanie nawiasów wymaga ustawienia formatera innego niż domyślne i zmiany decyzji o formaterze, więc kosztuje kolejną rundę z recenzją; cofnięcie kosztuje tyle samo. Zrobienie z tego zadania zostawia kod, jak jest, dopóki ktoś tego nie zrobi, i nic nie kosztuje teraz. Rekomenduję przepuścić, bo 3.14 to Python, który proces podaje jako wymagany. Słaby punkt: baza działała na starszym Pythonie przez szczęście, więc produkt, który podnosi przypięty proces na starszym Pythonie, odkryje awarię dopiero wtedy. Zachować nawiasy w tym PR-ze, zrobić z tego zadanie czy przepuścić? (Minor findings, 1)
2. Nie udało mi się wywołać ponownie losowej porażki testu usuwania katalogów roboczych, więc poprawka, która wyłącza w tym teście konserwację Gita w tle, nie jest dowiedziona. Jeśli przyczyna była inna, kontrola na Linuksie padnie losowo przy jakimś późniejszym PR-ze, jak przy wcześniejszym, i kosztuje powtórkę oraz pytanie do tego, kto czeka na scalenie. Dowód wymaga powtórnych przebiegów kontroli na Linuksie w tym PR-ze, kilku rund czekania na CI, a cofnięcie nic nie kosztuje. Zrobienie z tego zadania zostawia sprawę nieudowodnioną. Przepuszczenie przyjmuje to ryzyko; cofnięcie go później kosztuje poprawkę po następnej losowej porażce. Rekomenduję przepuścić, bo porażka wskazała dokładnie ten plik, który konserwacja w tle tworzy i usuwa. Słaby punkt: żaden przebieg nie pokazał porażki także przed poprawką, więc „przyczyna się zgadza” to odczyt, nie pomiar. Powtórzyć przebiegi na Linuksie w tym PR-ze, zrobić z tego zadanie czy przepuścić? (Checks, 4)
3. Trzy drobne rzeczy zostają nieuporządkowane i żadna nie jest błędna w tym, co robi. Cztery nazwy testów w pliku testów audytu nadal używają słowa „entry” dla pozycji listy zapisu. Decyzja o rozmiarze nie wymienia decyzji o formaterze w liście powiązań, choć jej liczenie opiera się na formaterze. Jedna funkcja instalatora ma 109 linii przy limicie 110, więc następna dopisana do niej linia zaczerwieni bramkę, dopóki ktoś nie wyniesie jakiejś części. Poprawienie ich w tym PR-ze kosztuje rundę poprawki z recenzją i powiększa zmianę; cofnięcie nic nie kosztuje. Zrobienie z nich zadania kosztuje trochę czasu w kolejce później; cofnięcie, nic. Przepuszczenie kosztuje czerwoną bramkę przy pierwszym dotknięciu funkcji instalatora. Rekomenduję zrobić z nich zadanie, bo każda jest mała i niezależna od tej zmiany. Słaby punkt: trzy kolejne małe zadania w długiej kolejce mogą zostać otwarte tygodniami. Poprawić w tym PR-ze, zrobić z nich zadanie czy przepuścić? (Minor findings, 2 i 3; Findings outside the task's scope, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś ci nie odpowiada, powiedz która.

4. Audyt procesu traci porównywalność przez tę zmianę. Przeformatowanie i podziały zmieniają narzędzia, które mierzą koszt, uwagi, kontekst i czasy bramki, więc audyt zaczyna nowe serie tych miar w wersji zawierającej tę zmianę, a miary tego cyklu wychodzą jako nieznane. Uznałem to za skutek zadania w kształcie, w jakim je ustaliłeś, bo żadna inna droga nie utrzymuje progów i formatera.
5. Zakaz komentarzy wyłączających formater jest nieco szerszy niż twoja odpowiedź. Nazwałeś trzy komentarze; formater Ruffa respektuje też dwa komentarze w pisowni innego narzędzia, które pozwoliłyby pliku zostać poza układem przy zielonej bramce. Zakazałem także tych dwóch, w decyzji, w regule formatera i w regule wytycznych, żeby zakaz robił to, o co prosiłeś. Jeśli chcesz tylko trzy, wycofanie to jedna linia.
6. Dwa zdania reguł audytu nazywają teraz oba skrypty mierzące koszt cyklu, nie jeden. Podział raportu etapów przeniósł kod czytania transkryptów do drugiego skryptu; bez tej zmiany późniejsza edycja tego kodu nie zaczęłaby nowej serii kosztu, wbrew sensowi reguły. To jedna decyzja i jeden niezmiennik fundamentu, brzmiące tak samo, których nie widziałeś przy dokumencie zadania.
7. Trzy słowa w fundamencie zmieniły się z tym samym znaczeniem: dziennik zmian planu, rejestr uruchomień bramki i niezmiennik o tym rejestrze mówią teraz „line” albo „file” tam, gdzie mówiły „entry”. Ich też nie widziałeś przy dokumencie zadania.
8. Mapa części procesu zyskała nowe pliki: lista pomijania blame należy do części plików repozytorium, a trzy nowe moduły audytu i nowy moduł transkryptów są nazwane plikami czytającymi dane z zewnątrz, żeby recenzje późniejszych zmian sprawdzały tam spreparowane wejścia. Decyzja o formaterze obejmuje teraz także część plików repozytorium, a jedna decyzja o sprawdzaniu fundamentu nazywa nową regułę pełnego sprawdzenia.
9. Dwie reguły fundamentu wyszły ze stanu „naruszona” i nie oczekują już porażki swoich testów: ta o regułach lintera i ta o rozmiarze funkcji i plików. Testy, które je sprawdzają, zmieniły się odpowiednio: test lintera i test rozmiaru stracili znak „oczekiwana porażka”; progi rozmiaru przeszły na 110 i 1200; nowy test układu i test pełnego sprawdzenia fundamentu są nowe. Dwie inne reguły dostały przeformułowane zdanie o tym samym znaczeniu (rejestr uruchomień bramki; skrypty, których zmiana zaczyna serię kosztu), a testy, które je cytują, dopasowano bez osłabiania asercji: test serii audytu oczekuje teraz obu plików kosztu, a jedenaście testów listy zapisu przemianowano.

## Koszt

Około 6 godzin 45 minut czasu pracy, z czego 4 godziny 8 minut to czekanie na narzędzia, razem 277 milionów tokenów (172 miliony na Sonnecie, 60 milionów na Opusie, 45 milionów na Haiku; 270 milionów z nich odczytano z pamięci podręcznej). Rundy recenzji: dziesięć recenzji pojedynczych slice’ów, wszystkie zaliczone przy pierwszym czytaniu; jedna recenzja całej zmiany; jedna runda poprawek dla jej dziesięciu uwag Minor z recenzją tej rundy; oraz jedna recenzja kroku powrotu. Żaden slice nie był robiony dwa razy. Tabela etapów jest w [zapisie cyklu](https://github.com/mariusznazar/the-way/blob/0d0130f686a43e6358fb8ed445b0234ad87064f2/docs/task-cycles/code-order-formatter-linter-size/stages.md).

## Jak scalić

Scal commitem scalającym, który zachowuje commity. Link do zapisu przeżywa tylko wtedy, i tylko wtedy przeżywa jeden commit przeformatowania, którego hash trzyma lista pomijania blame: squash albo rebase zmieniłby ten hash, a lista wskazywałaby na nic.

</details>

## Technical changes

The change stands in 19 slices after one commit of foundation entries, then a fix round, then the return step's commit. By commit and group of files (the base is `d69fb20b`, the head before the record is `d41712a6`):

- **Foundation entries** (`9c093516`, `00945f93`): the formatter decision and its invariant, the new thresholds, the invariant of the whole check of the foundation, the rewording of the word "entry" in two decisions and one invariant, and the two cost scripts in the audit decision and invariant; one line of the size test that quotes the size decision.
- **Formatter** (`6c13454c` configuration; `015ce05c` the one reformatting, 78 files, +16104/-7505, nothing else; `5e8fa379`, `037f6c93` the test of the layout, the guidelines' rule, the README paragraphs, the blame-skip list and its part-map line, one name added to the list of files that hold no script).
- **Foundation check in the gate** (`2620dcc3`): a test that runs the whole check and cites its own invariant; the narrow test stays.
- **Linter reports** (`8fecce81`, `d6442f89`, `c41a772d`, `222c5a7b`): 24 reports in 20 files fixed; the one place whose usual fix would change behaviour keeps its exit code 2 and message; the linter's test unmarked and its invariant `Violated: no`.
- **The flaky test** (`0ccdc807`): Git's automatic maintenance and garbage collection turned off through the test's environment.
- **The word "entry"** (`462add5d`).
- **Divisions** (`679112e3` installer, instruction check, plan check and plan state; `d84a1fe9` the request check; `1f09e4d6` the transcript reading moved to a module of its own; `efc2f090` the test that copies the audit's modules; `95316c25`, `a30a04ff` the audit command cut into a register module, a record-reading module, a version-analysis module and a report module; `6c748289` the tests import from the new modules and the cost script spans two files; `4e5f95fb` the transitional export list removed; `d0a861d9` the size test at 110/1200, unmarked, its invariant `Violated: no`).
- **Fix of the Minor findings of the review of the whole change** (`3b3008b3` .. `2e066ab4`, nine commits; `2e066ab4` alone moves the shared base of the audit modules into a module of its own), not reverted.
- **Return step** (`d41712a6`): one sentence of the guidelines' formatter rule wrapped, no word changed.

## Checks

- **Final gate:** the CI run on this request's last head `34d9970e` (the commit that removes the record's copy), https://github.com/mariusznazar/the-way/actions/runs/44550193828, first attempt: `tests` (Linux) pass, 1m28s; `tests-windows` pass, 6m54s. Every check passed in the one run; none was rerun and no test failed. The cycle ran no full gate on its own system and has no local time of it.
- **Failing before the change:** none (taken from the merged request https://github.com/mariusznazar/the-way/pull/148, whose CI run on its last head passed in both checks; the base is a merge commit with the tree of its second parent, so no gate ran on the base).
- **Focused runs** (`python -B gate/run_tests.py <directory>`, exit 0 each, by the executors and the reviewers at the heads of their slices): installation 73 tests, instruction-files 105 (5 skipped for POSIX), process-audit 277, project-level 281, task-cycle 534 (2 skipped for Windows), elements/common 271, elements/part-map 40, agent-instructions 52, gate 36, product-guidelines 14.
- **The check of the foundation** (`python -B elements/common/foundation_check.py`, no switch): exit 0, `0 errors`, no `listed:` line, on the finished change.
- **Not proven:** the fix of the flaky test (item 2): the failure was not reproduced before or after, so only repeated CI runs on Linux can show it.
- **Own-work checks:** each slice's executor named its weakest point and checked it; the ones with the most to lose were checked by old-against-new runs on crafted input (the plan check 1795 mutated plans, the instruction check 410 trees, the plan state 73 runs, the stage report 51 inputs, the audit's record reader 6000 texts, the analysis 3000 inputs, the audit command on this repository's own history and on a crafted register), and by the reviewers again on their own inputs.
- **Reviews:** slices 2, 5, 10, 11, 13, 15, 16, 17 and 18 got a review of their own (all passed), the others were judged by the review of the whole change (Opus, `PASS`, 25 decisions read whole), then the fix round (`PASS`) and the return step (`PASS`).
- **Form check** of this description: `python -B task-cycle/request_check.py .runs/task-cycles/code-order-formatter-linter-size/request.md --task .runs/task-cycles/code-order-formatter-linter-size/task.md`: exit 0 (the last of 5 runs); **check of private paths** on the description: `python -B task-cycle/private_paths_check.py .runs/task-cycles/code-order-formatter-linter-size/request.md`, exit 0 (the last of 4 runs). On the copy of the record (`docs/task-cycles/code-order-formatter-linter-size`, commit 0d0130f6): the check of private paths, exit 0 (the last of 3 runs: exit 1 with 393 listings, exit 1 with 14, exit 0 after two rewritings of every text file); the image check, `python -B task-cycle/image_files_check.py docs/task-cycles/code-order-formatter-linter-size`, exit 0 (1 run); the remarks check, `python -B task-cycle/remarks_check.py docs/task-cycles/code-order-formatter-linter-size`, exit 0 (1 run); on the original, the remarks check ran twice: exit 1 (47 items listed and appended to the process remarks word for word), exit 0.
- **Working copies left:** none.

## Foundation entries

- The decision on the formatter (WAY-382), changed in place: the formatter of the pinned Ruff at width 100, `.py` files only, no formatter-off comments; `row 1`, `row 4`, `row 5`; its *Scope* gained the part for repository files and its binding sentence gained the two `yapf:` comments by the fix: `the cycle's`.
- The decision on size (WAY-385), changed in place: 110 lines for a function and 1200 for a file, counted on formatted code; `row 2`.
- The decision on the adoption of the coding discipline (WAY-379), its *Verification* corrected so that the formatter's rule names the decision and the invariant; `row 1`.
- The invariant `formatter-layout` (new): every `.py` file git tracks in the parts of the coding discipline stands as the pinned Ruff's formatter leaves it, and no part of it is left out by a formatter-off comment (`fmt:` or `yapf:`); `row 1`, `row 4`, `row 5`; widened to the `yapf:` comments by the fix: `the cycle's`.
- The invariant `own-foundation-check-report` (new): the check of the foundation, run with no switch on the-way's repository, reports no error; `row 3`.
- The invariants `ruff-blocking-rules` and `function-and-file-size`: `Violated: no` (WAY-51), their tests no longer expected failures.
- The decision on the plan's log of changes (WAY-145) and on the registry of running gates (WAY-350), and the invariant `gate-times-refuses-impossible-entry`: "entry" replaced by "line" and by "file"; meaning unchanged; `the cycle's`.
- The decision on the series of the cost (WAY-339) and the invariant `audit-series-script-paths`: the script that measures the cost is `task-cycle/cycle_stages.py` with `task-cycle/stage_transcripts.py`; meaning unchanged; `the cycle's`.
- The decision on the check of the foundation (WAY-09): its *Verification* names `own-foundation-check-report`; `the cycle's`.
- Part map: `repository` lists the blame-skip list; the *Trust boundary* lines of `task-cycle` and `process-audit` name `task-cycle/stage_transcripts.py`, `process-audit/record_reading.py`, `process-audit/problem_register.py` and `process-audit/audit_shared.py`.
- The coding guidelines: `### Formatter` of the-way's own guidelines now carries the decision and the invariant; the rule names the two `yapf:` comments; `guidelines/coding-shared-module.md` names `task-cycle` in *Applies to* and *Where in code*.
- Invariant tests altered (WAY-03): `agent-instructions/test_linter_invariant.py` (`ruff-blocking-rules` unmarked, `formatter-layout` new), `agent-instructions/test_size_invariant.py` (`function-and-file-size` unmarked, thresholds, its line `decision:` of the size decision), `elements/common/test_foundation_check.py` (`own-foundation-check-report` new), `process-audit/test_audit_series_scripts.py` (`audit-series-script-paths`, the expected set of cost files), `process-audit/test_audit_count.py` (imports; the expected tuple of the series paths; one expected reason naming both cost files; lines `decision:` of the cost decision), `task-cycle/test_gate_times.py` (`gate-times-refuses-impossible-entry`, two tests renamed), `process-audit/test_record_items.py` (eleven renamed tests that hold lines `decision:`), `task-cycle/test_cycle_stages.py` (imports), `task-cycle/test_remove_merged_worktrees.py` (the flaky test) and, by one-line linter fixes, `agent-instructions/test_instruction_files.py`, `gate/test_skills_reach_the_way_sessions.py`, the installation tests, `elements/common/test_migrate_foundation.py`, `task-cycle/test_cycle_measures.py`, `task-cycle/test_remarks_check.py`, `product-guidelines/test_skill_references.py`; `agent-instructions/test_script_invariants.py` got one name in its list of files that hold no script.
- The *Verification* of the foundation check lists no invariant whose sentence was corrected while its test stayed as it was.

## Minor findings

1. **Eleven files parse only on Python 3.14** (review of the whole change, finding 2): "Ruff's formatter, run at `target-version = "py314"`, removed the brackets of fourteen `except (A, B):` clauses (PEP 758), for example `elements/common/foundation_source.py:48`, `elements/common/decision_index.py:75`, `elements/common/compare_log_entries.py:61`, `elements/common/migrate_foundation.py:863`, `instruction-files/check_instructions.py:516,766`, `process-audit/audit_count.py:520`, `process-audit/version_analysis.py:111`, `task-cycle/cycle_measures.py:496` and three test files. Every file of the base compiles on Python 3.12; at the head eleven do not (`SyntaxError: multiple exception types must be parenthesized`) ... The fix is no code: a sentence in the request saying that the code now parses only on the Python it declares; a change of it (brackets kept) would take a setting of the formatter other than its default, a change of WAY-382." (Item 1.)
2. **WAY-385's list of relations does not name WAY-382** (review of the return step, `foundations/decisions.md`, the *Relations* of the size decision): "WAY-385's own rule counts lines on the code as WAY-382's formatter leaves it. This is a gap in form only, because the content agrees with the code." (Item 3.)
3. **Four tests of the audit's test file still say "entry"** for an item of a record's list (`process-audit/test_audit_count.py:545, 556, 1428, 4986`), noted by the return step; the task's list of renames names `process-audit/test_record_items.py` and not this file. (Item 3.)

## Findings outside the task's scope

1. **`installation/install.py:448` `plan` stands at 109 lines against the limit of 110** (review of the whole change, finding 11): "The change did not grow it: it was 109 lines after the reformatting (`015ce05c`) and is 109 at the head. Any later addition to it must begin with a move out (WAY-365). Outside the task: no line of this change added to it; it goes to the request's list, not to the fix." (Item 3.)

## Course of the cycle

- **Task and sources:** the task "the way: porządek kodu Pythona — automatyczne formatowanie, błędy lintera, podział za dużych funkcji i plików, ostre testy obu reguł i pełne sprawdzenie fundamentu w bramce", independent, ready for cycle, as it stood on 2026-11-19; no project plan; the foundation of the-way at `d69fb20b`.
- **Process pin:** none; the-way is the repository itself.
- **Spec:** none: the task's five settlement rows carry every entry the change writes; its five questions carried to the cycle are choices of how to make what it settles.
- **Route:** planned slices, since one agent cannot hold a change that reformats 79 files in a commit of its own, fixes 24 faults, divides 11 functions and 2 files and writes entries; one fix round for the Minor findings of the review of the whole change; no attempt discarded.
- **Plan:** 19 slices after nine foundation entries (`plan.md` in the record); the orchestrator raised the class of four slices and added one file to slice 17's change.
- **Choices:** 10 choices and rulings in the questions table (see the record).
- **Blocking findings left:** none.
- **Record:** https://github.com/mariusznazar/the-way/tree/0d0130f686a43e6358fb8ed445b0234ad87064f2/docs/task-cycles/code-order-formatter-linter-size (commit 0d0130f6; the commit after it removes the copy, so that the target branch never holds it)
