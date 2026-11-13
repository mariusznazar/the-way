**State: ready** — corrected for your remarks; one item below asks whether to make a task of a finding the correction left, nothing blocks the merge, and what you accept by merging is listed under it.

## What you will see

Four changes to how the review of a change works and to what a product's coding rules require, and the evidence behind two rules that so far had none.

First, the review of the whole change now asks about the structure of the code the change leaves: whether a function or a file grew, whether code that nobody uses any more stays behind, whether a name stopped being true. The reviewer gets numbers for it. A new small script gives, for the commits of the change, the number of lines of each changed file before the change and after it, and the product's own size test names every function and file over its threshold, run on the state before the change and on the state after it.

Second, a product's coding guidelines now require a rule of the size of a function and a file. The rule has its own invariant and its own test, apart from the linter's rules. The product settles its thresholds after a trial run on its existing code, writes the functions it will not split as exceptions in a decision, or departs from the rule with a reason in a decision. A product that already has guidelines gets the rule by an ordinary extension of them, as it got the rules on failures and logs. Where code already stands over a threshold, the invariant is marked violated until it is cleaned, so that the review keeps cleaned code from growing again.

Third, two grades of a reviewer's remark no longer depend on chance. A remark about the structure of code below the product's threshold is Minor; the reviewer still judges whether it lies in the task's scope. A remark that a foundation entry departs from the form of its template, where the entry's content agrees with the code, is Minor, unless the reviewer names a sentence a reader would read wrongly because of the departure; a content that disagrees with the code stays Important. In a product that has no rule of size at all — one that departed from the rule with a reason, or one with no coding guidelines, such as this process repository itself — a remark about structure is always Minor, as you asked in your remark on this request. In the experiment with reviewers the same form remark was blocking in 9 runs and Minor in 8, and six runs rejected a change only for its form.

Fourth, the plan of a task: where a slice adds to a function or a file already over the threshold, the plan begins with a slice that moves a part of it out without changing behaviour, and the author of a change without a plan makes that move the first commit that changes the code. The rule that a reviewer works on no cheaper class of model than the leading agent stays as it was; its entry now holds the measurement behind it and the rejected variant of two cheaper runs, and the entry about the author's report holds the rejected variant of a review without it.

### Underneath

Six new decisions hold the rules above, one for each settlement of the task, and two existing decisions gained their measurements without a change to what binds. The script and its tests stand beside the other scripts of the task cycle.

## For you to decide

### Needed from you

none

### Fix or let through

1. After your correction, the sentence that says where a finding about structure is always Minor without a rule of size names two cases: a product that departed from the rule with a reason, and a product with no coding guidelines at all. It leaves out a third, a product whose guidelines were written before the rule existed, such as the game until its own adoption task. The review's own rules for the whole change cover that case, but the short sentence of the review skill and the decision do not. Whoever reviews a change in such a product meets two texts that do not say the same, and may grade the same finding Minor in one cycle and as any other in the next. Making it a task costs one sentence in two places and a round of review later; letting it through leaves the gap until a reviewer asks. I recommend making a task, since the clause copies your own wording and a correction has had its one round. Make a task of it? (Minor findings, 2)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The reviewer runs the script of line counts, not the orchestrator who starts the review. The task left this open; the way not taken adds a step for the orchestrator to every cycle, which the task refused for the size test. If the reviewer forgets, its report says the script did not run.
3. "The first commit" of the author without a plan, which the task names for the move that makes room, is read as the first commit that changes the code, so after the commits that only write foundation entries. The other reading puts the move before every commit, entries included, and the move would then precede the entries that describe what the code does.
4. A remark about structure that has no size — code nobody uses any more, a name that stopped being true — counts as "below the threshold", so it is Minor. The task chose "always Minor unless over the threshold"; the cycle read it to cover remarks with no size, since they cannot be over a threshold.
5. Where the rule's invariant is marked violated, its test stands marked as an expected failure and its message is hidden; the cycle added to the review's rules that the reviewer takes the mark off in its own copy of the code to read the sizes. The task did not say this. Without it the size test would show no function and no file.
6. Five more files of the coding guidelines' skill changed than the task named, so that a refresh of existing guidelines finds the missing rule and proposes it, and the hand-back of a joined task checks it. The task named only the template and the list of questions; without the others the extension route would have no trigger. The price is more places to change together later.
7. The rule of size stands under a heading of its own after the six rules on failures and logs, counts size in lines, and keeps thresholds and exceptions only in the product's decision, never in the rule's text. The way not taken is placing it among the standing checks or before the six rules, which the task and an earlier decision rule out.
8. While this cycle ran, another request merged and took the decision numbers this branch had planned. The cycle renumbered its six decisions after the new ones, and the older reports of the record name them by the old numbers. Another number order would have broken the earlier one; no content changed.
9. This correction answered your answer to an item of this request about an unfixed finding, and the cycle judged that neither the task nor the foundation required what it changed, so you see a change beyond the task that you asked for: a finding about structure is now always Minor also in a product with no rule of size.

## Cost

About 1 hour 45 minutes of working time, 45 minutes of it without waits for tools, and about 77.0 million tokens: 66.7 million on Sonnet 5.5 and 10.3 million on Opus 5.5, which the reviewer of the whole change, the review of its fix and the review of your correction used. The three runs of the whole gate, 17, 14 and 17 minutes, are not in that time. The cycle ran with one author and no plan: the author, a review of the whole change that failed on one remark, one fix of six findings, a review of that fix, the return step with a review of its one commit, a review of the merge with the target branch, a fix of one test that failed in the gate with a review of it, and then your correction with its own review. The table of stages is in the record linked under the course of the cycle.

## How to merge

Merge with a merge commit, which keeps the commits; the link to the record survives only then. The foundation has waited for a review through 31 merges since the tag of 6 November 2026, and the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — poprawiony po Twoich uwagach; jedna pozycja poniżej pyta, czy założyć zadanie z uwagi, którą poprawka zostawiła, nic nie blokuje scalenia, a to, co akceptujesz przez scalenie, jest wypisane pod nią.

## Co zobaczysz

Cztery zmiany w tym, jak działa przegląd zmiany i co wymagają od produktu jego zasady kodowania, oraz podstawa dwóch reguł, które jej dotąd nie miały.

Pierwsza: przegląd całej zmiany pyta teraz o strukturę kodu, który zmiana zostawia: czy funkcja albo plik urosły, czy zostaje kod, którego nikt już nie używa, czy nazwa przestała być prawdą. Recenzent dostaje do tego liczby. Nowy mały skrypt podaje dla commitów zmiany liczbę linii każdego zmienionego pliku przed zmianą i po niej, a test rozmiaru z produktu wymienia każdą funkcję i plik ponad progiem, uruchamiany na stanie sprzed zmiany i po niej.

Druga: wytyczne kodowania produktu wymagają teraz reguły rozmiaru funkcji i pliku. Reguła ma własny niezmiennik i własny test, osobno od reguł lintera. Produkt ustala progi po próbie na swoim kodzie, funkcje, których nie będzie dzielił, zapisuje jako wyjątki w decyzji albo odstępuje od reguły z powodem w decyzji. Produkt, który ma już wytyczne, dostaje regułę zwykłym rozszerzeniem wytycznych, tak jak dostał reguły o awariach i logach. Gdzie kod już przekracza próg, niezmiennik jest oznaczony jako naruszony do czasu sprzątania, żeby przegląd nie dopuścił do ponownego wzrostu posprzątanego kodu.

Trzecia: dwa stopnie uwag recenzenta nie zależą już od losu. Uwaga o strukturze kodu poniżej progu produktu jest drobna; recenzent nadal ocenia, czy leży w zakresie zadania. Uwaga, że wpis fundamentu odstępuje od formy swojego szablonu, gdy treść wpisu zgadza się z kodem, jest drobna, chyba że recenzent wskaże zdanie, które czytelnik przez to odstępstwo odczyta źle; rozjazd treści z kodem zostaje ważny. W produkcie, który w ogóle nie ma reguły rozmiaru — odstąpił od niej z powodem albo nie ma wytycznych kodowania, jak samo repozytorium procesu — uwaga o strukturze jest zawsze drobna, tak jak prosiłeś w swojej uwadze do tej prośby. W eksperymencie z recenzentami ta sama uwaga o formie była blokująca w 9 przebiegach i drobna w 8, a sześć przebiegów odrzuciło zmianę wyłącznie za formę.

Czwarta: plan zadania. Gdy kawałek dopisuje do funkcji albo pliku już ponad progiem, plan zaczyna od kawałka, który wydziela jej część bez zmiany zachowania, a autor zmiany bez planu robi to pierwszym commitem zmieniającym kod. Reguła, że recenzent pracuje na nie tańszej klasie modelu niż agent prowadzący, zostaje taka, jaka była; jej wpis ma teraz pomiar, na którym stoi, i odrzucony wariant dwóch tańszych przebiegów, a wpis o raporcie autora ma odrzucony wariant przeglądu bez niego.

### Pod spodem

Sześć nowych decyzji niesie powyższe reguły, po jednej na każde ustalenie zadania, a dwie istniejące decyzje dostały swoje pomiary bez zmiany tego, co wiąże. Skrypt i jego testy stoją obok pozostałych skryptów cyklu zadania.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Po Twojej poprawce zdanie, które mówi, gdzie uwaga o strukturze jest zawsze drobna bez reguły rozmiaru, wymienia dwa przypadki: produkt, który odstąpił od reguły z powodem, i produkt bez żadnych wytycznych kodowania. Pomija trzeci: produkt, którego wytyczne napisano, zanim reguła powstała, jak gra do czasu swojego zadania przyjęcia reguły. Własne zasady przeglądu całej zmiany ten przypadek obejmują, ale krótkie zdanie skilla przeglądu i decyzja — nie. Kto przegląda zmianę w takim produkcie, trafia na dwa teksty, które nie mówią tego samego, i tę samą uwagę może ocenić jako drobną w jednym cyklu, a jak każdą inną w następnym. Założenie zadania kosztuje jedno zdanie w dwóch miejscach i późniejszą rundę przeglądu; przepuszczenie zostawia lukę, aż zapyta o nią recenzent. Polecam założyć zadanie, bo zdanie powtarza Twoje własne brzmienie, a poprawka miała już swoją jedną rundę. Założyć zadanie? (Minor findings, 2)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz, która.

2. Skrypt liczący linie uruchamia recenzent, a nie orkiestrator, który zaczyna przegląd. Zadanie zostawiło to otwarte; droga niewybrana dodaje krok orkiestratora do każdego cyklu, czego zadanie odmówiło przy teście rozmiaru. Jeśli recenzent zapomni, jego raport mówi, że skrypt nie ruszył.
3. „Pierwszy commit” autora bez planu, który zadanie wskazuje dla wydzielenia robiącego miejsce, jest czytany jako pierwszy commit zmieniający kod, czyli po commitach, które tylko piszą wpisy fundamentu. Druga lektura stawia wydzielenie przed każdym commitem, także wpisami, a wydzielenie poprzedzałoby wtedy wpisy opisujące, co robi kod.
4. Uwaga o strukturze, która nie ma rozmiaru — kod, którego nikt już nie używa, nazwa, która przestała być prawdą — liczy się jako „poniżej progu”, więc jest drobna. Zadanie wybrało „zawsze drobna, chyba że ponad progiem”; cykl odczytał to tak, że obejmuje uwagi bez rozmiaru, bo nie mogą przekroczyć progu.
5. Gdzie niezmiennik reguły jest oznaczony jako naruszony, jego test stoi oznaczony jako oczekiwane niepowodzenie i jego komunikat jest ukryty; cykl dopisał do zasad przeglądu, że recenzent zdejmuje to oznaczenie w swojej własnej kopii kodu, żeby odczytać rozmiary. Zadanie tego nie mówiło. Bez tego test rozmiaru nie pokazałby żadnej funkcji ani pliku.
6. Zmieniono pięć plików skilla wytycznych kodowania więcej, niż zadanie wskazywało, żeby odświeżenie istniejących wytycznych znajdowało brakującą regułę i ją proponowało, a przekazanie zadania łączonego ją sprawdzało. Zadanie wskazało tylko szablon i listę pytań; bez pozostałych droga rozszerzenia nie miałaby wyzwalacza. Cena: więcej miejsc do późniejszej wspólnej zmiany.
7. Reguła rozmiaru stoi pod własnym nagłówkiem po sześciu regułach o awariach i logach, liczy rozmiar w liniach, a progi i wyjątki trzyma tylko w decyzji produktu, nigdy w tekście reguły. Droga niewybrana to umieszczenie jej wśród stałych kontroli albo przed sześcioma regułami, czego zadanie i wcześniejsza decyzja nie dopuszczają.
8. Gdy ten cykl trwał, scaliła się inna prośba i zajęła numery decyzji, które ta gałąź miała zaplanowane. Cykl przenumerował swoje sześć decyzji za nowymi, a starsze raporty rekordu wymieniają je pod dawnymi numerami. Inna kolejność numerów zepsułaby wcześniejszą; treść się nie zmieniła.
9. Ta poprawka odpowiedziała na Twoją odpowiedź na pozycję tej prośby o niepoprawioną uwagę, a cykl uznał, że ani zadanie, ani fundament nie wymagały tego, co zmieniła, więc widzisz zmianę wykraczającą poza zadanie, o którą prosiłeś: uwaga o strukturze jest teraz zawsze drobna także w produkcie bez reguły rozmiaru.

## Koszt

Około 1 godziny 45 minut czasu pracy, w tym 45 minut bez oczekiwania na narzędzia, i około 77,0 mln tokenów: 66,7 mln na Sonnecie 5.5 i 10,3 mln na Opusie 5.5, którego użył recenzent całej zmiany, przegląd jej poprawki i przegląd Twojej poprawki. Trzy przebiegi całej bramki, 17, 14 i 17 minut, nie wchodzą do tego czasu. Cykl szedł z jednym autorem i bez planu: autor, przegląd całej zmiany, który odrzucił zmianę przez jedną uwagę, jedna poprawka sześciu uwag, przegląd tej poprawki, krok zwrotny z przeglądem jego jednego commitu, przegląd scalenia z gałęzią docelową, poprawka jednego testu, który padł w bramce, z jej przeglądem, a potem Twoja poprawka z własnym przeglądem. Tabela etapów jest w rekordzie, do którego link stoi w przebiegu cyklu.

## Jak scalić

Scal commitem scalającym, który zachowuje commity; link do rekordu przeżywa tylko wtedy. Fundament czeka na przegląd po 31 scaleniach od tagu z 6 listopada 2026, a przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

Text of the foundation, of the skills and of the template of coding guidelines, and one script with its tests. Twelve commits on top of `65b6d70`, in this order:

1. `c7a6733` — the rule of size in `product-guidelines/coding/`: the required rule `### Size of a function and a file` in `template.md`, the question about thresholds and exceptions in `settle.md`, the trial of sizes in `trial_run.md`, the refresh check in `recognize.md`, and the lines in `task_document.md`, `hand_back.md` and the coding `SKILL.md`; the two entries written then as WAY-355 and WAY-356 (now WAY-360 and WAY-361).
2. `093b901` — `task-cycle/change_file_sizes.py` with `task-cycle/test_change_file_sizes.py` (15 tests then), the section on structure in `task-cycle/review/whole_change.md`, the two grades in section 3 of `task-cycle/review/SKILL.md`; the entries then WAY-357 to WAY-359 (now WAY-362 to WAY-364).
3. `76b038c` — the move-out slice in `task-cycle/plan/SKILL.md` and the first commit in `task-cycle/change/SKILL.md`; the entry then WAY-360 (now WAY-365).
4. `5353268` — WAY-229 (*Rationale*, *Rejected*) and WAY-164 (*Rejected*) edited in place; binding sentences and fields untouched, checked by a scripted comparison of base and head.
5. `a47195b`, `cd54d5a`, `c6af26a` — the fix of the review's findings: the condition for marking the rule's invariant violated now names only code the exceptions do not cover (WAY-360's binding sentence, `template.md`, `settle.md`, `trial_run.md`); WAY-364 points to WAY-229 for the conditions of its measurement; `template.md` keeps "standing check" to the three the template requires; `product-guidelines/audit_end.md` names both refresh checks; `whole_change.md` lets the script run in the reviewed worktree; the script fences a name with a backtick and escapes a bar, with three more tests.
6. `b596eec` — the return step: the bullet on the order of the required rules in `template.md` says the rule of size comes between the six rules and the product's further rules.
7. `c756236` and `3e934b6` — the renumbering of this branch's decisions WAY-355 to WAY-360 as WAY-360 to WAY-365 and the merge of `origin/foundations` (`8079485`, which holds WAY-355 to WAY-359 of another request); the one conflict, in `foundations/decisions.md`, kept both sides.
8. `0f35395` — the path of the script in `task-cycle/test_change_file_sizes.py` as a constant made from the test's directory, because the test of the imports of the-way's code could not work out the file the test ran.
9. `c04d9cc` — correction 1, for your remark: a finding about the structure of code is Minor also where the product has no rule of size, in section 3 of `task-cycle/review/SKILL.md` and in the binding sentence of WAY-363 (edited in place, with its *Verification*, *Rationale* and *Rejected*), and in `task-cycle/review/whole_change.md`, `product-guidelines/coding/settle.md` and `product-guidelines/coding/template.md`, which agreed only after the change.

## Checks

- Gate on the base `65b6d70`, in a separate checkout: `python -B task-cycle/gate_times.py --output ../task-cycles/review-structure-form-class/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1200 tests in 10 directories, 729.9 s. No check failed on the base.
- Gate on the merged tree `3e934b6`: the same command, exit 1, 1221 tests in 10 directories, 1000.6 s; `elements/part-map` failed, `test_cross_part_imports.TheWay.test_the_way_imports_only_from_allowed_parts`, reporting two lines of `task-cycle/test_change_file_sizes.py` as running a file the check cannot work out. After the fix `0f35395` the same command on `0f35395`: exit 0, 1221 tests, every directory passed, 831.1 s. The check failed in 1 of 4 cycle runs of the gate and passed in 3 (the base and the last two); its rerun passed, and the failure was a defect of this change, not flakiness (the test file reached by the failing check belongs to the part `part-map`, outside the task's parts, so it also stands under *Findings outside the task's scope*).
- Focused checks, each with its true exit code: `python -B elements/common/foundation_check.py`, exit 0, `0 errors` (on the head and on each commit by the author); `python -B gate/run_tests.py task-cycle`, exit 0, 385 tests; `process-audit` 180 and `project-level` 275 tests, exit 0 after the merge; `python -B gate/run_tests.py elements/part-map`, exit 0, 39 tests after the fix; `python -B task-cycle/private_paths_check.py <file>` on each changed file, exit 0; `python -B agent-instructions/skill_entry_points.py`, exit 0 (no skill description changed).
- The new script on the range of the change, by the reviewer: `python -B task-cycle/change_file_sizes.py 65b6d70 5353268`, exit 0; every row equals the added minus the removed lines of `git diff --numstat`; tried by the reviewer on names with a space, with non-ASCII letters, with a leading dash, a rename, a binary file and a submodule, in a scratch repository. The tests of the script were broken on purpose six ways by the author and four by the reviewer; each break was caught except a harmless one.
- Own-work checks: the author's check that WAY-229 and WAY-164 changed only in *Rationale* and *Rejected*, with every number of the task present, exit 0, repeated word for word by the reviewer; the fix author's scan of every sentence that holds "marked violated" with a threshold, exit 0, five sentences, all with the exceptions' qualification.
- Correction 1, the gate on `c04d9cc`: the same command, exit 0, 1221 tests in 10 directories, every directory passed, 1036.8 s; `python -B elements/common/foundation_check.py`, exit 0; `python -B gate/run_tests.py task-cycle` exit 0, 385 tests; `elements/part-map`, `instruction-files` and `python -B agent-instructions/skill_entry_points.py`, exit 0; `python -B task-cycle/private_paths_check.py <file>` on each of the five changed files, exit 0. The author's own-work check: a scan of each sentence about this grade, all saying the same; the reviewer searched the whole branch once (21 hits, each read) and found none missed.
- Reviews: whole change `FAIL 5353268` (1 blocking, 5 Minor within the task, 1 Minor outside; 46 of 251 selected decisions read whole, 205 by title); the fix `PASS c6af26a`; the return step's commit `PASS b596eec`; the reconciliation with the target branch `PASS 3e934b6`; the fix of the failing gate test `PASS 0f35395`; your correction `PASS c04d9cc` (0 blocking, 2 Minor within the task, 1 outside).
- The description: `python -B task-cycle/request_check.py docs/task-cycles/review-structure-form-class/request.md --task docs/task-cycles/review-structure-form-class/task.md`, exit 0, `form holds`; `python -B task-cycle/private_paths_check.py docs/task-cycles/review-structure-form-class/request.md`, exit 0, 0 listed.
- The copy of the record, `585fb1b`, each check run once after the copy was cleaned (the process remarks check three times on the original before it, the last exit 0): `python -B task-cycle/private_paths_check.py docs/task-cycles/review-structure-form-class`, exit 0, 25 files, 0 listed (19 listed before the cleaning); `python -B task-cycle/image_files_check.py docs/task-cycles/review-structure-form-class`, exit 0, 25 files, 0 listed; `python -B task-cycle/remarks_check.py docs/task-cycles/review-structure-form-class`, exit 0, 9 reports, 11 items, 0 missing from the remarks.
- Not run: nothing the change called for.

## Foundation entries

- WAY-360 (row 3): the template of coding guidelines requires a rule of the size of a function and a file with its own invariant and test outside the linter's set; a product settles thresholds after a trial run and exceptions in its decision, or departs by a decision with a reason; a product with guidelines gets it by an extension; the invariant is marked violated while code other than the exceptions stands over a threshold.
- WAY-361 (row 4): the test of the rule names every function and file over a threshold with its size, the reviewer of the whole change runs it on the state before the change and after it, and a product has no command of its own for sizes.
- WAY-362 (row 6): the reviewer of the whole change judges what the change leaves in the structure of the code, with the lines of each changed file before and after (a script of the-way) and the test of the rule of size on both states; no *Rejected* way, since the task keeps none for the row.
- WAY-363 (row 1, changed in place by correction 1): a finding about the structure of code below the product's threshold, or in a product with no rule of size, is Minor and its scope is judged as for any finding; a finding about a function or a file over a threshold is graded as any other; narrows WAY-161.
- WAY-364 (row 2): a finding that an entry departs from the form of its template, where its content agrees with the code, is Minor unless it cites a sentence a reader would read wrongly through the departure; a mismatch of content with the code stays Important; narrows WAY-161.
- WAY-365 (row 5): where a slice adds to a function or a file over the threshold, the plan begins with a slice that moves a part out without a change of behaviour, written in the table of choices, and the author without a plan makes that move the first commit that changes the code; no spec.
- WAY-229 (task item 7, changed in place): binding sentences unchanged; *Rationale* holds the measurement of the reviewer's class with its conditions, *Rejected* the variant of two cheaper runs with its result.
- WAY-164 (task item 8, changed in place): binding sentences unchanged; *Rejected* holds the variant of a review without the author's report with its result and a pointer to WAY-229 for the conditions.
- No invariant, environment fact, glossary term or part-map change; the return step wrote no entry. The new script is not added to the *Trust boundary* of `task-cycle`: it reads git and counts lines and runs nothing it reads.

## Minor findings

1. Review of the fix of the whole change, `foundations/decisions.md:11969-11970`, `product-guidelines/coding/template.md:75`, `:223`, `:243`, `product-guidelines/audit_end.md:55`, `task-cycle/review/whole_change.md:33`: "Rewrapped lines left over-long — the fix inserted words without rewrapping the paragraph, as the files around them wrap near 100 characters. Polish only; nothing reads differently."
2. Review of correction 1, WAY-363 and `task-cycle/review/SKILL.md` section 3 (C1): "the cases set off by dashes after 'no rule of size' name only two: a product that departed from the rule, and one with no coding guidelines. They leave out a third: a product whose guidelines were written before the rule existed, such as the game until its own adoption task. `whole_change.md` does cover that case. The clause copies the human's own wording, so whether to widen it is the human's call." (item 1 of *For you to decide*)
3. Review of correction 1, WAY-363 *Rationale* (C2): "one line runs to 163 characters because the inserted sentence was not rewrapped."

## Findings outside the task's scope

1. Declined to judge, review of the whole change, line 1: "Whether the measurements in WAY-229, WAY-164 and WAY-359 should stand as an environment fact in *Based on* (the decisions template, line 44-47, asks one for 'a finding about agents or models'): the task settles the measurement in *Rationale* with *Origin* `none`, and the source is in private notes, which WAY-27 forbids pointing to; the collision between the template's rule and WAY-27 for a private source is outside this task. Also under Searches." The entry the reviewer named WAY-359 is WAY-364 now. You answered the item that asked about it: not fixed here, a task made in your notes, let through in this request.
2. Declined to judge, review of the whole change, line 2: "The cost for the reviewer of installing a product's toolchain in two scratch worktrees to run the size test: the task chooses that the reviewer runs it (question 5); its cost is not a defect of this change."
3. Review of correction 1, under Declined to judge: WAY-360's *Rejected* still says "the same chance in the grade" for the case of a product with no rule, which correction 1 now settles as Minor; the text is your own wording of a rejected option (the task's question 4), so the reviewer left it.
4. The check of the imports of the-way's code, `elements/part-map/test_cross_part_imports.py`, of the part `part-map` outside the task's parts: it failed in 1 of 4 cycle runs of the gate and passed in the other 3, with the rerun passing; the cause was the test this change wrote, fixed in `0f35395`.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes, `Status: ready for cycle`, six of eight candidate settlements accepted on 2026-11-12; goal: the review of the whole change asks about the structure of code with numbers, the grades of remarks about structure and about the form of an entry are fixed, the reviewer's class rule gets its measurement; no human action placed in the cycle. The foundation changed between the state the task was refined on (`2292f33`) and the base (`65b6d70`) in entries about the audit and the request; none of the sixteen entries the task names changed.
- **Process pin:** not applicable; the cycle ran on the-way's own checkout at `65b6d70`, equal to `origin/foundations` after a fetch at the start, and the task moves no pin. `origin/foundations` moved to `8079485` during the cycle and was merged (`3e934b6`), the merge reviewed `PASS 3e934b6`; a second fetch at the end found nothing new.
- **Spec:** none; no open design choice at the start: the task's answers 1 to 7 settle the rules and what is rejected; the shape of the script's command line and output, the place and wording of the rule and its invariant in the template, and the wording of the entries were choices of how to make what is settled.
- **Route:** one author without a plan, on the orchestrator's own class (not the cheaper one), because the change spans three parts, writes entries that bind later work and a script; the author's one retry was never needed.
- **Plan:** none.
- **Choices:** 8 rows in the record's questions table (the route, the author's class, the reviewer running the script, the position of the rule in the template, the reviewer's class, the author's unread material carried to the review, the reading of "the first commit", and the way a failing gate check is reviewed); those that bind after the merge stand under *You accept by merging*; the table is in the record.
- **Blocking findings left:** none; the one blocking finding of the review of the whole change was fixed and its fix passed; correction 1 was reviewed `PASS c04d9cc`.
- **Corrections:** correction 1, for your comment on this request (item 1: fix it here; item 2: let it through, a task made in your notes); the remarks word for word are `reports/correction-1-remarks.md` in the record; the base the correction started from is `24cbe61` (the tree of `0f35395`, nothing reset); the cycle changed nothing else for it.
- **Record:** https://github.com/mariusznazar/the-way/tree/585fb1b1ee1e75489458136fa127318f44b215e0/docs/task-cycles/review-structure-form-class (committed in `585fb1b`, removed from the final tree in the next commit; the table of stages is `stages.md` in it, the questions table is in `cycle.md`).
