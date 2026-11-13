**State: ready** — two items below ask whether to make a task of a finding or let it through; nothing blocks the merge, and what you accept by merging is listed under them.

## What you will see

Four changes to how the review of a change works and to what a product's coding rules require, and the evidence behind two rules that so far had none.

First, the review of the whole change now asks about the structure of the code the change leaves: whether a function or a file grew, whether code that nobody uses any more stays behind, whether a name stopped being true. The reviewer gets numbers for it. A new small script gives, for the commits of the change, the number of lines of each changed file before the change and after it, and the product's own size test names every function and file over its threshold, run on the state before the change and on the state after it.

Second, a product's coding guidelines now require a rule of the size of a function and a file. The rule has its own invariant and its own test, apart from the linter's rules. The product settles its thresholds after a trial run on its existing code, writes the functions it will not split as exceptions in a decision, or departs from the rule with a reason in a decision. A product that already has guidelines gets the rule by an ordinary extension of them, as it got the rules on failures and logs. Where code already stands over a threshold, the invariant is marked violated until it is cleaned, so that the review keeps cleaned code from growing again.

Third, two grades of a reviewer's remark no longer depend on chance. A remark about the structure of code below the product's threshold is Minor; the reviewer still judges whether it lies in the task's scope. A remark that a foundation entry departs from the form of its template, where the entry's content agrees with the code, is Minor, unless the reviewer names a sentence a reader would read wrongly because of the departure; a content that disagrees with the code stays Important. In the experiment with reviewers the same form remark was blocking in 9 runs and Minor in 8, and six runs rejected a change only for its form.

Fourth, the plan of a task: where a slice adds to a function or a file already over the threshold, the plan begins with a slice that moves a part of it out without changing behaviour, and the author of a change without a plan makes that move the first commit that changes the code. The rule that a reviewer works on no cheaper class of model than the leading agent stays as it was; its entry now holds the measurement behind it and the rejected variant of two cheaper runs, and the entry about the author's report holds the rejected variant of a review without it.

### Underneath

Six new decisions hold the rules above, one for each settlement of the task, and two existing decisions gained their measurements without a change to what binds. The script and its tests stand beside the other scripts of the task cycle.

## For you to decide

### Needed from you

none

### Fix or let through

1. In a product that has no rule of size — one that departed from the rule with a reason, or one with no coding guidelines at all, such as this process repository itself — there is no threshold, and the rules do not say how a reviewer grades a finding that a function there grew. Whoever works with the process meets this at the next review of such a change: the same finding may block it in one cycle, cost a round of correction and a second review, and pass as Minor in the next, which is the chance the task meant to remove. The ways: say that the finding is graded as any other where there is no rule — it costs one sentence in the review's rules and a decision, and such findings can then block, with the chance of a round of correction back; say that it is always Minor where there is no rule — the same edit, and real growth in such a product never blocks; or leave it as it is, which costs nothing now and leaves the choice to each reviewer. I recommend always Minor, since the task answered "Minor unless over the threshold" and a product with no rule has no threshold to cross. Fix it in this request (one of the two sentences), make a task of it, or let it through? (Findings outside the task's scope, 1)
2. Three decisions now carry numbers of the experiment with reviewers, and the numbers stand with no source a reader of the repository can open, since the report lies in private notes. The rule of the decision template asks that a measurement about models be recorded as an environment fact with its source, and another rule bars pointing to a source readers cannot reach, so the two collide for a private source. Whoever writes the next decision with a measurement will meet the same collision and a reviewer may call it a defect or not. Settling it in this request costs a new decision about how a private source stands and a round of review; making a task of it leaves the collision to that task; letting it through accepts it. I recommend making a task of it, since it changes a rule of the process and not a wording. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 2)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The reviewer runs the script of line counts, not the orchestrator who starts the review. The task left this open; the way not taken adds a step for the orchestrator to every cycle, which the task refused for the size test. If the reviewer forgets, its report says the script did not run.
4. "The first commit" of the author without a plan, which the task names for the move that makes room, is read as the first commit that changes the code, so after the commits that only write foundation entries. The other reading puts the move before every commit, entries included, and the move would then precede the entries that describe what the code does.
5. A remark about structure that has no size — code nobody uses any more, a name that stopped being true — counts as "below the threshold", so it is Minor. The task chose "always Minor unless over the threshold"; the cycle read it to cover remarks with no size, since they cannot be over a threshold.
6. Where the rule's invariant is marked violated, its test stands marked as an expected failure and its message is hidden; the cycle added to the review's rules that the reviewer takes the mark off in its own copy of the code to read the sizes. The task did not say this. Without it the size test would show no function and no file.
7. Five more files of the coding guidelines' skill changed than the task named, so that a refresh of existing guidelines finds the missing rule and proposes it, and the hand-back of a joined task checks it. The task named only the template and the list of questions; without the others the extension route would have no trigger. The price is more places to change together later.
8. The rule of size stands under a heading of its own after the six rules on failures and logs, counts size in lines, and keeps thresholds and exceptions only in the product's decision, never in the rule's text. The way not taken is placing it among the standing checks or before the six rules, which the task and an earlier decision rule out.
9. While this cycle ran, another request merged and took the decision numbers this branch had planned. The cycle renumbered its six decisions after the new ones, and the older reports of the record name them by the old numbers. Another number order would have broken the earlier one; no content changed.

## Cost

About 1 hour 16 minutes of working time, 36 minutes of it without waits for tools, and about 57.7 million tokens: 49.0 million on Sonnet 5.5 and 8.7 million on Opus 5.5, which the reviewer of the whole change and the review of its fix used. The two runs of the whole gate, 16 and 14 minutes, are not in that time. The cycle ran with one author and no plan: the author, a review of the whole change that failed on one remark, one fix of six findings, a review of that fix, the return step with a review of its one commit, a review of the merge with the target branch, and a fix of one test that failed in the gate with a review of it. The table of stages is in the record linked under the course of the cycle.

## How to merge

Merge with a merge commit, which keeps the commits; the link to the record survives only then. The foundation has waited for a review through 31 merges since the tag of 6 November 2026, and the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — dwie pozycje poniżej pytają, czy założyć zadanie z uwagi albo ją przepuścić; nic nie blokuje scalenia, a to, co akceptujesz przez scalenie, jest wypisane pod nimi.

## Co zobaczysz

Cztery zmiany w tym, jak działa przegląd zmiany i co wymagają od produktu jego zasady kodowania, oraz podstawa dwóch reguł, które jej dotąd nie miały.

Pierwsza: przegląd całej zmiany pyta teraz o strukturę kodu, który zmiana zostawia: czy funkcja albo plik urosły, czy zostaje kod, którego nikt już nie używa, czy nazwa przestała być prawdą. Recenzent dostaje do tego liczby. Nowy mały skrypt podaje dla commitów zmiany liczbę linii każdego zmienionego pliku przed zmianą i po niej, a test rozmiaru z produktu wymienia każdą funkcję i plik ponad progiem, uruchamiany na stanie sprzed zmiany i po niej.

Druga: wytyczne kodowania produktu wymagają teraz reguły rozmiaru funkcji i pliku. Reguła ma własny niezmiennik i własny test, osobno od reguł lintera. Produkt ustala progi po próbie na swoim kodzie, funkcje, których nie będzie dzielił, zapisuje jako wyjątki w decyzji albo odstępuje od reguły z powodem w decyzji. Produkt, który ma już wytyczne, dostaje regułę zwykłym rozszerzeniem wytycznych, tak jak dostał reguły o awariach i logach. Gdzie kod już przekracza próg, niezmiennik jest oznaczony jako naruszony do czasu sprzątania, żeby przegląd nie dopuścił do ponownego wzrostu posprzątanego kodu.

Trzecia: dwa stopnie uwag recenzenta nie zależą już od losu. Uwaga o strukturze kodu poniżej progu produktu jest drobna; recenzent nadal ocenia, czy leży w zakresie zadania. Uwaga, że wpis fundamentu odstępuje od formy swojego szablonu, gdy treść wpisu zgadza się z kodem, jest drobna, chyba że recenzent wskaże zdanie, które czytelnik przez to odstępstwo odczyta źle; rozjazd treści z kodem zostaje ważny. W eksperymencie z recenzentami ta sama uwaga o formie była blokująca w 9 przebiegach i drobna w 8, a sześć przebiegów odrzuciło zmianę wyłącznie za formę.

Czwarta: plan zadania. Gdy kawałek dopisuje do funkcji albo pliku już ponad progiem, plan zaczyna od kawałka, który wydziela jej część bez zmiany zachowania, a autor zmiany bez planu robi to pierwszym commitem zmieniającym kod. Reguła, że recenzent pracuje na nie tańszej klasie modelu niż agent prowadzący, zostaje taka, jaka była; jej wpis ma teraz pomiar, na którym stoi, i odrzucony wariant dwóch tańszych przebiegów, a wpis o raporcie autora ma odrzucony wariant przeglądu bez niego.

### Pod spodem

Sześć nowych decyzji niesie powyższe reguły, po jednej na każde ustalenie zadania, a dwie istniejące decyzje dostały swoje pomiary bez zmiany tego, co wiąże. Skrypt i jego testy stoją obok pozostałych skryptów cyklu zadania.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

1. W produkcie, który nie ma reguły rozmiaru — takim, który od niej odstąpił z powodem, albo takim bez wytycznych kodowania, jak samo repozytorium procesu — nie ma progu, a zasady nie mówią, jak recenzent ma ocenić uwagę, że funkcja tam urosła. Spotkasz to przy najbliższym przeglądzie takiej zmiany: ta sama uwaga może ją zablokować w jednym cyklu, kosztować rundę poprawek i drugi przegląd, a w następnym przejść jako drobna, czyli właśnie ten los, który zadanie miało usunąć. Drogi: napisać, że uwaga jest tam oceniana jak każda inna — to jedno zdanie w zasadach przeglądu i decyzja, a takie uwagi mogą wtedy blokować, z losem rundy poprawek z powrotem; napisać, że tam jest zawsze drobna — ta sama zmiana, a realny wzrost w takim produkcie nigdy nie blokuje; albo zostawić tak, jak jest, co nic dziś nie kosztuje i zostawia wybór każdemu recenzentowi. Polecam „zawsze drobna”, bo zadanie odpowiedziało „drobna, chyba że ponad progiem”, a produkt bez reguły nie ma progu do przekroczenia. Poprawić w tej prośbie (jednym z dwóch zdań), założyć zadanie czy przepuścić? (Findings outside the task's scope, 1)
2. Trzy decyzje niosą teraz liczby z eksperymentu z recenzentami, a liczby stoją bez źródła, które czytelnik repozytorium może otworzyć, bo raport leży w prywatnych notatkach. Reguła szablonu decyzji każe zapisać pomiar o modelach jako fakt środowiska ze źródłem, a inna reguła zakazuje wskazywania źródła, do którego czytelnik nie sięgnie, więc dla źródła prywatnego te dwie reguły się zderzają. Kto napisze następną decyzję z pomiarem, trafi na to samo, a recenzent może to uznać za usterkę albo nie. Rozstrzygnięcie w tej prośbie kosztuje nową decyzję o tym, jak stoi źródło prywatne, i rundę przeglądu; założenie zadania zostawia zderzenie temu zadaniu; przepuszczenie je akceptuje. Polecam założyć zadanie, bo to zmienia regułę procesu, a nie sformułowanie. Poprawić w tej prośbie, założyć zadanie czy przepuścić? (Findings outside the task's scope, 2)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz, która.

3. Skrypt liczący linie uruchamia recenzent, a nie orkiestrator, który zaczyna przegląd. Zadanie zostawiło to otwarte; droga niewybrana dodaje krok orkiestratora do każdego cyklu, czego zadanie odmówiło przy teście rozmiaru. Jeśli recenzent zapomni, jego raport mówi, że skrypt nie ruszył.
4. „Pierwszy commit” autora bez planu, który zadanie wskazuje dla wydzielenia robiącego miejsce, jest czytany jako pierwszy commit zmieniający kod, czyli po commitach, które tylko piszą wpisy fundamentu. Druga lektura stawia wydzielenie przed każdym commitem, także wpisami, a wydzielenie poprzedzałoby wtedy wpisy opisujące, co robi kod.
5. Uwaga o strukturze, która nie ma rozmiaru — kod, którego nikt już nie używa, nazwa, która przestała być prawdą — liczy się jako „poniżej progu”, więc jest drobna. Zadanie wybrało „zawsze drobna, chyba że ponad progiem”; cykl odczytał to tak, że obejmuje uwagi bez rozmiaru, bo nie mogą przekroczyć progu.
6. Gdzie niezmiennik reguły jest oznaczony jako naruszony, jego test stoi oznaczony jako oczekiwane niepowodzenie i jego komunikat jest ukryty; cykl dopisał do zasad przeglądu, że recenzent zdejmuje to oznaczenie w swojej własnej kopii kodu, żeby odczytać rozmiary. Zadanie tego nie mówiło. Bez tego test rozmiaru nie pokazałby żadnej funkcji ani pliku.
7. Zmieniono pięć plików skilla wytycznych kodowania więcej, niż zadanie wskazywało, żeby odświeżenie istniejących wytycznych znajdowało brakującą regułę i ją proponowało, a przekazanie zadania łączonego ją sprawdzało. Zadanie wskazało tylko szablon i listę pytań; bez pozostałych droga rozszerzenia nie miałaby wyzwalacza. Cena: więcej miejsc do późniejszej wspólnej zmiany.
8. Reguła rozmiaru stoi pod własnym nagłówkiem po sześciu regułach o awariach i logach, liczy rozmiar w liniach, a progi i wyjątki trzyma tylko w decyzji produktu, nigdy w tekście reguły. Droga niewybrana to umieszczenie jej wśród stałych kontroli albo przed sześcioma regułami, czego zadanie i wcześniejsza decyzja nie dopuszczają.
9. Gdy ten cykl trwał, scaliła się inna prośba i zajęła numery decyzji, które ta gałąź miała zaplanowane. Cykl przenumerował swoje sześć decyzji za nowymi, a starsze raporty rekordu wymieniają je pod dawnymi numerami. Inna kolejność numerów zepsułaby wcześniejszą; treść się nie zmieniła.

## Koszt

Około 1 godziny 16 minut czasu pracy, w tym 36 minut bez oczekiwania na narzędzia, i około 57,7 mln tokenów: 49,0 mln na Sonnecie 5.5 i 8,7 mln na Opusie 5.5, którego użył recenzent całej zmiany i przegląd jej poprawki. Dwa przebiegi całej bramki, 16 i 14 minut, nie wchodzą do tego czasu. Cykl szedł z jednym autorem i bez planu: autor, przegląd całej zmiany, który odrzucił zmianę przez jedną uwagę, jedna poprawka sześciu uwag, przegląd tej poprawki, krok zwrotny z przeglądem jego jednego commitu, przegląd scalenia z gałęzią docelową oraz poprawka jednego testu, który padł w bramce, z jej przeglądem. Tabela etapów jest w rekordzie, do którego link stoi w przebiegu cyklu.

## Jak scalić

Scal commitem scalającym, który zachowuje commity; link do rekordu przeżywa tylko wtedy. Fundament czeka na przegląd po 31 scaleniach od tagu z 6 listopada 2026, a przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

Text of the foundation, of the skills and of the template of coding guidelines, and one script with its tests. Eleven commits on top of `65b6d70`, in this order:

1. `c7a6733` — the rule of size in `product-guidelines/coding/`: the required rule `### Size of a function and a file` in `template.md`, the question about thresholds and exceptions in `settle.md`, the trial of sizes in `trial_run.md`, the refresh check in `recognize.md`, and the lines in `task_document.md`, `hand_back.md` and the coding `SKILL.md`; the two entries written then as WAY-355 and WAY-356 (now WAY-360 and WAY-361).
2. `093b901` — `task-cycle/change_file_sizes.py` with `task-cycle/test_change_file_sizes.py` (15 tests then), the section on structure in `task-cycle/review/whole_change.md`, the two grades in section 3 of `task-cycle/review/SKILL.md`; the entries then WAY-357 to WAY-359 (now WAY-362 to WAY-364).
3. `76b038c` — the move-out slice in `task-cycle/plan/SKILL.md` and the first commit in `task-cycle/change/SKILL.md`; the entry then WAY-360 (now WAY-365).
4. `5353268` — WAY-229 (*Rationale*, *Rejected*) and WAY-164 (*Rejected*) edited in place; binding sentences and fields untouched, checked by a scripted comparison of base and head.
5. `a47195b`, `cd54d5a`, `c6af26a` — the fix of the review's findings: the condition for marking the rule's invariant violated now names only code the exceptions do not cover (WAY-360's binding sentence, `template.md`, `settle.md`, `trial_run.md`); WAY-364 points to WAY-229 for the conditions of its measurement; `template.md` keeps "standing check" to the three the template requires; `product-guidelines/audit_end.md` names both refresh checks; `whole_change.md` lets the script run in the reviewed worktree; the script fences a name with a backtick and escapes a bar, with three more tests.
6. `b596eec` — the return step: the bullet on the order of the required rules in `template.md` says the rule of size comes between the six rules and the product's further rules.
7. `c756236` and `3e934b6` — the renumbering of this branch's decisions WAY-355 to WAY-360 as WAY-360 to WAY-365 and the merge of `origin/foundations` (`8079485`, which holds WAY-355 to WAY-359 of another request); the one conflict, in `foundations/decisions.md`, kept both sides.
8. `0f35395` — the path of the script in `task-cycle/test_change_file_sizes.py` as a constant made from the test's directory, because the test of the imports of the-way's code could not work out the file the test ran.

## Checks

- Gate on the base `65b6d70`, in a separate checkout: `python -B task-cycle/gate_times.py --output ../task-cycles/review-structure-form-class/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1200 tests in 10 directories, 729.9 s. No check failed on the base.
- Gate on the merged tree `3e934b6`: the same command, exit 1, 1221 tests in 10 directories, 1000.6 s; `elements/part-map` failed, `test_cross_part_imports.TheWay.test_the_way_imports_only_from_allowed_parts`, reporting two lines of `task-cycle/test_change_file_sizes.py` as running a file the check cannot work out. After the fix `0f35395` the same command on `0f35395`: exit 0, 1221 tests, every directory passed, 831.1 s. The check failed in 1 of 3 cycle runs of the gate and passed in 2 (the base and the last); its rerun passed, and the failure was a defect of this change, not flakiness (the test file reached by the failing check belongs to the part `part-map`, outside the task's parts, so it also stands under *Findings outside the task's scope*).
- Focused checks, each with its true exit code: `python -B elements/common/foundation_check.py`, exit 0, `0 errors` (on the head and on each commit by the author); `python -B gate/run_tests.py task-cycle`, exit 0, 385 tests; `process-audit` 180 and `project-level` 275 tests, exit 0 after the merge; `python -B gate/run_tests.py elements/part-map`, exit 0, 39 tests after the fix; `python -B task-cycle/private_paths_check.py <file>` on each changed file, exit 0; `python -B agent-instructions/skill_entry_points.py`, exit 0 (no skill description changed).
- The new script on the range of the change, by the reviewer: `python -B task-cycle/change_file_sizes.py 65b6d70 5353268`, exit 0; every row equals the added minus the removed lines of `git diff --numstat`; tried by the reviewer on names with a space, with non-ASCII letters, with a leading dash, a rename, a binary file and a submodule, in a scratch repository. The tests of the script were broken on purpose six ways by the author and four by the reviewer; each break was caught except a harmless one.
- Own-work checks: the author's check that WAY-229 and WAY-164 changed only in *Rationale* and *Rejected*, with every number of the task present, exit 0, repeated word for word by the reviewer; the fix author's scan of every sentence that holds "marked violated" with a threshold, exit 0, five sentences, all with the exceptions' qualification.
- Reviews: whole change `FAIL 5353268` (1 blocking, 5 Minor within the task, 1 Minor outside; 46 of 251 selected decisions read whole, 205 by title); the fix `PASS c6af26a`; the return step's commit `PASS b596eec`; the reconciliation with the target branch `PASS 3e934b6`; the fix of the failing gate test `PASS 0f35395`.
- The form check, the check of private paths and the process remarks check: last runs are added with the record's link.
- Not run: nothing the change called for.

## Foundation entries

- WAY-360 (row 3): the template of coding guidelines requires a rule of the size of a function and a file with its own invariant and test outside the linter's set; a product settles thresholds after a trial run and exceptions in its decision, or departs by a decision with a reason; a product with guidelines gets it by an extension; the invariant is marked violated while code other than the exceptions stands over a threshold.
- WAY-361 (row 4): the test of the rule names every function and file over a threshold with its size, the reviewer of the whole change runs it on the state before the change and after it, and a product has no command of its own for sizes.
- WAY-362 (row 6): the reviewer of the whole change judges what the change leaves in the structure of the code, with the lines of each changed file before and after (a script of the-way) and the test of the rule of size on both states; no *Rejected* way, since the task keeps none for the row.
- WAY-363 (row 1): a finding about the structure of code below the product's threshold is Minor and its scope is judged as for any finding; narrows WAY-161.
- WAY-364 (row 2): a finding that an entry departs from the form of its template, where its content agrees with the code, is Minor unless it cites a sentence a reader would read wrongly through the departure; a mismatch of content with the code stays Important; narrows WAY-161.
- WAY-365 (row 5): where a slice adds to a function or a file over the threshold, the plan begins with a slice that moves a part out without a change of behaviour, written in the table of choices, and the author without a plan makes that move the first commit that changes the code; no spec.
- WAY-229 (task item 7, changed in place): binding sentences unchanged; *Rationale* holds the measurement of the reviewer's class with its conditions, *Rejected* the variant of two cheaper runs with its result.
- WAY-164 (task item 8, changed in place): binding sentences unchanged; *Rejected* holds the variant of a review without the author's report with its result and a pointer to WAY-229 for the conditions.
- No invariant, environment fact, glossary term or part-map change; the return step wrote no entry. The new script is not added to the *Trust boundary* of `task-cycle`: it reads git and counts lines and runs nothing it reads.

## Minor findings

1. Review of the fix of the whole change, `foundations/decisions.md:11969-11970`, `product-guidelines/coding/template.md:75`, `:223`, `:243`, `product-guidelines/audit_end.md:55`, `task-cycle/review/whole_change.md:33`: "Rewrapped lines left over-long — the fix inserted words without rewrapping the paragraph, as the files around them wrap near 100 characters. Polish only; nothing reads differently."

## Findings outside the task's scope

1. `task-cycle/review/SKILL.md:126-128` and the binding sentence of WAY-363 (Minor, review of the whole change, M6): "A finding about the structure of code that lies below the threshold of the rule of size in the product's coding guidelines is Minor. Where the product has no rule of size (a departure reading `none —`, or, as for the-way itself under WAY-328, no coding guidelines) there is no threshold, and neither text says whether such a finding is 'below' it (always Minor) or falls back to the general grade. The task does not settle it (row 1 and question 3 speak only of a product's threshold), and the author's report names it; settling it is the human's choice, not a fix's, so I mark it outside the task: the request's list, for the human to decide." The reviewer's name for the entry was WAY-358 at that time.
2. Declined to judge, review of the whole change, line 1: "Whether the measurements in WAY-229, WAY-164 and WAY-359 should stand as an environment fact in *Based on* (the decisions template, line 44-47, asks one for 'a finding about agents or models'): the task settles the measurement in *Rationale* with *Origin* `none`, and the source is in private notes, which WAY-27 forbids pointing to; the collision between the template's rule and WAY-27 for a private source is outside this task. Also under Searches." The entry the reviewer named WAY-359 is WAY-364 now.
3. Declined to judge, review of the whole change, line 2: "The cost for the reviewer of installing a product's toolchain in two scratch worktrees to run the size test: the task chooses that the reviewer runs it (question 5); its cost is not a defect of this change."
4. The check of the imports of the-way's code, `elements/part-map/test_cross_part_imports.py`, of the part `part-map` outside the task's parts: it failed in 1 of 3 cycle runs of the gate and passed in the other 2, with the rerun passing; the cause was the test this change wrote, fixed in `0f35395`.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes, `Status: ready for cycle`, six of eight candidate settlements accepted on 2026-11-12; goal: the review of the whole change asks about the structure of code with numbers, the grades of remarks about structure and about the form of an entry are fixed, the reviewer's class rule gets its measurement; no human action placed in the cycle. The foundation changed between the state the task was refined on (`2292f33`) and the base (`65b6d70`) in entries about the audit and the request; none of the sixteen entries the task names changed.
- **Process pin:** not applicable; the cycle ran on the-way's own checkout at `65b6d70`, equal to `origin/foundations` after a fetch at the start, and the task moves no pin. `origin/foundations` moved to `8079485` during the cycle and was merged (`3e934b6`), the merge reviewed `PASS 3e934b6`; a second fetch at the end found nothing new.
- **Spec:** none; no open design choice at the start: the task's answers 1 to 7 settle the rules and what is rejected; the shape of the script's command line and output, the place and wording of the rule and its invariant in the template, and the wording of the entries were choices of how to make what is settled.
- **Route:** one author without a plan, on the orchestrator's own class (not the cheaper one), because the change spans three parts, writes entries that bind later work and a script; the author's one retry was never needed.
- **Plan:** none.
- **Choices:** 8 rows in the record's questions table (the route, the author's class, the reviewer running the script, the position of the rule in the template, the reviewer's class, the author's unread material carried to the review, the reading of "the first commit", and the way a failing gate check is reviewed); those that bind after the merge stand under *You accept by merging*; the table is in the record.
- **Blocking findings left:** none; the one blocking finding of the review of the whole change was fixed and its fix passed.
- **Record:** the link is added in the next edit of this description, after the record is committed.
