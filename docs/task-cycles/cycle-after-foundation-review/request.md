**State: ready** — corrected for your answer to an item; one item of *Fix or let through* asks only whether to make a task of an old gap the correction left; what you only accept by merging waits for nothing.

## What you will see

Eleven wording gaps that the review of the foundation found in the rules of the task cycle are closed; the change is text only, in the rules of the process, and no script or test changed.

- **Removal of finished directories at the start of a cycle.** The rule that lets the cycle remove its own, already merged task directories now says so openly next to the older rule that keeps every irreversible action for you: for the cycle's own merged directories the removal wins, and every other irreversible action still waits for you. The list of ignored files that the removal script prints is now described as what you read when you run the script yourself without its apply switch; the cycle does not wait for it and its start step is unchanged. A copy of a base that the script cannot match to a task stays for you to remove by hand, and the old sentence that called the first clearing of old directories your act is gone.
- **A red gate caused by a flaky test.** When the first run of the full gate on the final tree is red because of a flaky test outside the task, that red result stays the result of the gate; the cycle does not stop and does not switch the test off, and the request names the test and the task that fixes it, or proposes such a task.
- **Your answer "fix it in this request" on a request made by hand.** It now runs one fix by the author and one review of that fix by an agent that did not make it, the same loop as for a blocking remark; what stays unfixed comes back only with the question whether to make a task of it.
- **Writing and correcting a request.** The answer "do it in this request" is now named in all three places that list what it runs, also for something an entry stands on that the foundation does not hold yet. The example of the sentence that says what started a correction no longer reads as "the task required a defect". The state line of a corrected request now says what started the correction: your remarks, your answer to an item, or only a refresh from the target branch.
- **Screenshots shown to you.** A screenshot shown to you is kept where the product's foundation settles it, and in the agent's own directory only where it settles nothing. Following your answer, the rule on where those screenshots lie now says in the foundation's own form that it prevails over the older rule on the agent's working copies, for those screenshots only; the older rule keeps every other screenshot and every copy made to check something.
- **One wording fix** in the rule on the weight of a task's process: the example of a violation now names who does it ("an agent treats a large task as a reason to split it …").

### Underneath

Five files of rules and instructions changed (the decision log, three files of the cycle's instructions and the guide for work on this repository); the full gate passed with 1457 tests on the final tree.

## For you to decide

### Needed from you

none

### Fix or let through

1. One old gap that this change did not make and did not touch: the rule that says how a technology choice is tested for what choosing it could break (a devil's advocate, a pre-mortem and a search for unknown unknowns) names the three tests but no source they were taken from, and the foundation marks the source as missing. You answered that it belongs to a separate task already waiting in your queue, which fills in the sources of the practices the process took over, so the correction left it as it was; the request carries the item only because the gap still stands. Make a task of it, or let it through by merging? (Foundation entries, 7)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The cycle chose the words of the state line of a corrected request: "corrected for your remarks" only where your remarks started the correction, "corrected for your answer to an item" where your answer to an item did, and "refreshed from the target branch at your request" where only that did, each in its words when there are two sources. The task fixed only the first phrase and asked that the line say what started the correction; I did not fix one phrase for each source inside a script, since the task did not touch the script and nothing reads these phrases.
3. The cycle added to the part of the request for findings outside the task's scope one clause: for a check outside the task's parts that failed and passed again, the request also gives the task that fixes it, or the proposal of one. The task asked that the request name that task but left the template of the request unchanged, and the reviewer found that the form had no place for it; I did not leave the wording to each cycle, since then different requests would word it or leave it out in different ways.
4. The decision about removing finished directories now outranks, for the cycle's own merged directories only, the rule that has you perform every irreversible action; the rule keeps its reach over every other irreversible action. The passages you accepted that give this outcome are quoted in the lower part. I did not narrow the sentence of the older rule itself, since it would then stop reaching irreversible actions of the cycle outside a change, and a new one would meet nothing that stops it. (Foundation entries, 1)
5. Following your answer, the decision that says where a screenshot shown to you lies now outranks, for such a screenshot only, the rule that keeps an agent's working copies in its own directory; that rule keeps its reach over every other screenshot and every copy made to check something. I wrote it as the foundation asks for one rule that outranks another, on the rule that outranks, and not as an exception inside the older rule, which your answer left to the form the foundation asks for. Your own words that give this outcome are quoted in the lower part. (Foundation entries, 6)
6. The example of a violation in the rule on the weight of a task's process now names who does it ("an agent treats a large task as a reason to split it …"); its meaning is unchanged, and the rule itself did not change. (Foundation entries, 4)
7. The answer "do it in this request" is now named, also for something an entry stands on that the foundation does not hold yet, in the rule about which unfinished things a request puts before you and in the correction instructions. The task placed the list of such answers in the rule; it stands in the correction instructions, so I changed both places. (Foundation entries, 5)
8. This correction answered your answer to an item of this request, and the cycle judged that the foundation required what the answer asked to change: the foundation requires that where two rules collide the one that prevails records it, and the screenshot exception that the first change wrote into the cycle's instructions had no such record; the reviewer had seen it and marked it outside the task, so the cycle saw it and left it. Your answer on the missing source of the testing rule asked for no change, so the cycle judged nothing about it.

## Cost

About 36 minutes of working time of the cycle across the first run and the correction, with 14 minutes of waiting for tools and about 39.7 million tokens, all on one model (Claude Sonnet 5.5); two review rounds of the whole change and its parts: the review of the whole change passed with two small notes within the task, which one fix and one review of that fix closed, and the review of the correction passed. The table of stages is in the cycle's record (its link is written after the record's commit). Directories of earlier tasks still stand because the script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand; their names, branches and reasons stand in *Checks*.

## How to merge

Merge it so that the commits are kept (a merge commit), since the link to the record of the cycle survives only then.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — poprawiona dla Twojej odpowiedzi na pozycję; jedna pozycja z części „Popraw albo przepuść” pyta tylko, czy zrobić zadanie ze starej luki, którą korekta zostawiła; to, co tylko akceptujesz przez scalenie, na nic nie czeka.

## Co zobaczysz

Zamknięte jest jedenaście luk w sformułowaniach reguł cyklu zadania, które znalazł przegląd fundamentu; zmiana to sam tekst reguł procesu, żaden skrypt ani test się nie zmienił.

- **Usuwanie zakończonych katalogów na starcie cyklu.** Reguła pozwalająca cyklowi usuwać własne, już scalone katalogi zadań mówi teraz o tym wprost obok starszej reguły, która zostawia Tobie każdą czynność nieodwracalną: dla własnych, scalonych katalogów cyklu przeważa usuwanie, a każda inna czynność nieodwracalna dalej czeka na Ciebie. Lista plików ignorowanych, którą drukuje skrypt usuwający, jest opisana jako to, co czytasz, gdy sam uruchamiasz skrypt bez przełącznika zastosowania; cykl na nią nie czeka, a jego krok startu się nie zmienia. Kopia bazowa, której skrypt nie przypisze do zadania, zostaje Tobie do ręcznego usunięcia, a stare zdanie nazywające pierwsze sprzątanie starych katalogów Twoją czynnością zniknęło.
- **Czerwona bramka od losowo padającego testu.** Gdy pierwszy przebieg pełnej bramki na końcowym drzewie jest czerwony przez losowo padający test spoza zadania, ten czerwony wynik zostaje wynikiem bramki; cykl się nie zatrzymuje i nie wyłącza testu, a prośba nazywa test i zadanie, które go naprawi, albo je proponuje.
- **Twoja odpowiedź „napraw to w tej prośbie” przy prośbie zrobionej ręcznie.** Uruchamia teraz jedną poprawkę autora i jedną recenzję tej poprawki przez agenta, który jej nie robił — tę samą pętlę co dla uwagi blokującej; to, co zostaje niepoprawione, wraca tylko z pytaniem, czy zrobić z tego zadanie.
- **Pisanie i korekta prośby.** Odpowiedź „zrób to w tej prośbie” jest teraz wymieniona we wszystkich trzech miejscach, które mówią, co ona uruchamia, także dla rzeczy, na której stoi wpis, a której fundament jeszcze nie zawiera. Przykład zdania mówiącego, co uruchomiło korektę, nie brzmi już jak „zadanie wymagało defektu”. Linia stanu skorygowanej prośby mówi teraz, co uruchomiło korektę: Twoje uwagi, Twoja odpowiedź na pozycję albo samo odświeżenie z gałęzi docelowej.
- **Zrzuty ekranu pokazywane Tobie.** Zrzut pokazywany Tobie trafia tam, gdzie ustala go fundament produktu, a do katalogu agenta tylko tam, gdzie fundament nic nie ustala. Zgodnie z Twoją odpowiedzią reguła o tym, gdzie leżą takie zrzuty, mówi teraz w formie, jakiej wymaga fundament, że przeważa nad starszą regułą o kopiach roboczych agenta, tylko dla tych zrzutów; starsza reguła zachowuje każdy inny zrzut i każdą kopię robioną do sprawdzenia czegokolwiek.
- **Jedna poprawka brzmienia** w regule o ciężarze procesu zadania: przykład naruszenia ma teraz podmiot („an agent treats a large task as a reason to split it …”).

### Pod spodem

Zmieniło się pięć plików reguł i instrukcji (dziennik decyzji, trzy pliki instrukcji cyklu i przewodnik pracy nad tym repozytorium); pełna bramka na końcowym drzewie przeszła z 1457 testami.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Popraw albo przepuść

1. Jedna stara luka, której ta zmiana nie zrobiła i której nie ruszyła: reguła mówiąca, jak wybór technologii jest sprawdzany pod kątem tego, co jego wybór mógłby zepsuć (adwokat diabła, pre-mortem i szukanie nieznanych niewiadomych), nazywa trzy sprawdziany, ale nie podaje źródła, z którego je wzięto, a fundament oznacza to źródło jako brakujące. Odpowiedziałeś, że należy do osobnego zadania, które już czeka w Twojej kolejce i uzupełnia źródła praktyk przejętych przez proces, więc korekta zostawiła ją bez zmian; prośba niesie tę pozycję tylko dlatego, że luka nadal stoi. Zrobić z tego zadanie, czy przepuścić przez scalenie? (Foundation entries, 7)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

2. Cykl dobrał słowa linii stanu skorygowanej prośby: „poprawiona dla Twoich uwag” tylko tam, gdzie korektę uruchomiły Twoje uwagi, „poprawiona dla Twojej odpowiedzi na pozycję” tam, gdzie uruchomiła ją Twoja odpowiedź na pozycję, a „odświeżona z gałęzi docelowej na Twoją prośbę” tam, gdzie tylko to; przy dwóch źródłach każde własnymi słowami. Zadanie ustaliło tylko pierwsze sformułowanie i poprosiło, by linia mówiła, co uruchomiło korektę; nie ustaliłem jednego sformułowania dla każdego źródła w skrypcie, bo zadanie skryptu nie dotyka i nic tych sformułowań nie czyta.
3. Cykl dopisał w części prośby o ustaleniach spoza zakresu zadania jedną klauzulę: dla sprawdzenia spoza części zadania, które padło i przeszło po powtórce, prośba podaje też zadanie, które je naprawi, albo propozycję takiego zadania. Zadanie prosiło, by prośba nazywała to zadanie, ale zostawiało szablon prośby bez zmian, a recenzent stwierdził, że formularz nie ma na to miejsca; nie zostawiłem sformułowania każdemu cyklowi, bo wtedy różne prośby sformułowałyby to albo pominęły na różne sposoby.
4. Decyzja o usuwaniu zakończonych katalogów przeważa teraz, tylko dla własnych, scalonych katalogów cyklu, nad regułą, która każe Tobie wykonywać każdą czynność nieodwracalną; reguła zachowuje zasięg wobec każdej innej czynności nieodwracalnej. Fragmenty, które zaakceptowałeś, a które dają ten wynik, są zacytowane w dolnej części. Nie zawężałem samego zdania starszej reguły, bo przestałaby wtedy obejmować nieodwracalne czynności cyklu poza zmianą, a nowa taka czynność nie napotkałaby niczego, co ją zatrzymuje. (Foundation entries, 1)
5. Zgodnie z Twoją odpowiedzią decyzja mówiąca, gdzie leży zrzut ekranu pokazywany Tobie, przeważa teraz, tylko dla takiego zrzutu, nad regułą trzymającą kopie robocze agenta w jego katalogu; ta reguła zachowuje zasięg wobec każdego innego zrzutu i każdej kopii robionej do sprawdzenia czegokolwiek. Zapisałem to tak, jak fundament każe zapisywać jedną regułę przeważającą nad drugą — przy regule przeważającej, a nie jako wyjątek wewnątrz starszej, co Twoja odpowiedź zostawiła formie, jakiej wymaga fundament. Twoje słowa, które dają ten wynik, są zacytowane w dolnej części. (Foundation entries, 6)
6. Przykład naruszenia w regule o ciężarze procesu zadania ma teraz podmiot („an agent treats a large task as a reason to split it …”); jego znaczenie jest bez zmian, a sama reguła się nie zmieniła. (Foundation entries, 4)
7. Odpowiedź „zrób to w tej prośbie” jest teraz wymieniona, także dla rzeczy, na której stoi wpis, a której fundament jeszcze nie zawiera, w regule o tym, które niedokończone sprawy prośba stawia przed Tobą, i w instrukcjach korekty. Zadanie umieściło listę takich odpowiedzi w regule; stoi ona w instrukcjach korekty, więc zmieniłem oba miejsca. (Foundation entries, 5)
8. Ta korekta odpowiedziała na Twoją odpowiedź na pozycję tej prośby, a cykl uznał, że fundament wymagał tego, o co ta odpowiedź prosiła: fundament wymaga, by tam, gdzie dwie reguły kolidują, ta, która przeważa, to zapisała, a wyjątek dla zrzutu ekranu, który pierwsza zmiana wpisała do instrukcji cyklu, takiego zapisu nie miał; recenzent to widział i uznał za sprawę poza zadaniem, więc cykl to zauważył i zostawił. Twoja odpowiedź w sprawie brakującego źródła reguły o testowaniu nie prosiła o zmianę, więc cykl niczego o niej nie oceniał.

## Koszt

Około 36 minut czasu pracy cyklu w pierwszym przebiegu i w korekcie, w tym 14 minut czekania na narzędzia, i około 39,7 miliona tokenów, wszystkie na jednym modelu (Claude Sonnet 5.5); dwie rundy recenzji całości i jej części: recenzja całości przeszła z dwiema drobnymi uwagami w zakresie zadania, które zamknęła jedna poprawka i jedna recenzja tej poprawki, a recenzja korekty przeszła. Tabela etapów jest w zapisie cyklu (jego link dochodzi po commicie zapisu). Katalogi wcześniejszych zadań nadal stoją, bo skrypt nie mógł rozpoznać, że nie są już potrzebne; nic w tej prośbie na nie nie czeka i możesz je usunąć ręcznie; ich nazwy, gałęzie i powody są w *Checks*.

## Jak scalić

Scal tak, by zachować commity (merge commit), bo link do zapisu cyklu przetrwa tylko wtedy.

</details>

## Technical changes

The change is three commits of work on `task/cycle-after-foundation-review`, from the base `739c813` (the head of `foundations`), made by one author without a plan and without a spec (no open design choice); the record's copy was added and removed in further pairs of commits.

- `6727b67`, the change: `foundations/decisions.md` (WAY-13 *Verification*; WAY-375 binding sentences, *Relations*, *Rationale*, *Rejected*; WAY-376 binding sentence, *Rationale*, *Rejected*; WAY-261 a second paragraph, *Verification*, *Rationale*, *Rejected*; WAY-289 binding sentences and *Rationale*), `task-cycle/skill/SKILL.md` (step 10 paragraph; first paragraph of "Working copies"), `task-cycle/skill/correction.md` (list of kinds that "do it in this request" runs), `task-cycle/skill/request_template.md` (kind 17's example sentence; the row "A correction" of the variants table) and `agent-instructions/README.md` ("Integrate into `foundations`"). 5 files, 111 added and 57 removed lines.
- `cfda61e`, the fix of the two Minor findings of the review of the whole change: `task-cycle/skill/request_template.md` (the clause on the task that fixes a flaky check, in *Findings outside the task's scope*) and `foundations/decisions.md` (WAY-375: "a copy of a base standing alone"). 2 files, 5 changed lines.
- `f92d9dd`, correction 1, for your answer to the item on the screenshot exception: `foundations/decisions.md`, WAY-316 only (a third paragraph of binding sentences, `narrows WAY-373` in *Relations*, one sentence of *Rationale*). 1 file, 9 added lines. It carries out the finding that the review of the whole change had marked outside the task's scope (Minor 3 there), which is therefore no longer unfixed. No reset: the correction was made on top of the branch, after the target branch was fetched and found unmoved.
- The return steps of the first run and of the correction committed nothing: the entries and the part map still matched the files.
- Not changed: WAY-243, WAY-138, the testing template, the glossary entry *human action*, `task-cycle/remove_merged_worktrees.py`, the invariants and the part map.

## Checks

- Gate: `python -B task-cycle/gate_times.py --output .runs/task-cycles/cycle-after-foundation-review/gate_times.md -- python -B gate/run_tests.py`, run twice and exit 0 each time: run 1 on `cfda61e` (before the correction), 1457 tests in 10 directories, 345.8 s; run 2 on `f92d9dd` (the final tree), 1457 tests in 10 directories, 356.9 s; no other gate run at the same time, every directory passed, no check failed or did not run. Run 2 started before the return step of the correction was repeated; that step then committed nothing, so the tree it checked is the final tree.
- Failing before the change: none; no gate run on the base. The base `739c813` is a merge whose tree equals that of its second parent, so the list was taken from the final gate of the earlier cycle, `docs/task-cycles/part-map-dependencies-task-line/cycle.md` of commit `8200eb3` (run 2, exit 0, 1457 tests, every directory passed).
- `python -B elements/common/foundation_check.py` without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line, on `cfda61e` and on `f92d9dd`.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 3`, `threshold: 60`, `reminder: no`.
- Focused checks by the author, the fix author, the correction's author and the reviewers: `python -B gate/run_tests.py elements/common` (235 tests), `task-cycle` (483), `agent-instructions` (25), `process-audit`: exit 0 each; the check of private paths on each changed file: 0 listed; `git grep` for `narrows WAY-316` and `narrows WAY-373`: only WAY-316's line.
- Own-work checks: the author searched the tracked files for the statements the change removes ("first clearing", "hand clearing", "sees before", "loose copies") and found them only in the *Rejected* of WAY-375 and WAY-376 where the ways not chosen are named; the fix author checked that the fix grows nothing beyond its two findings (5 changed lines); the correction's author checked that no two decisions narrow each other and that no test holds a sentence of WAY-316. The reviewer of the whole change compared the new sentences of WAY-375 and WAY-376 with the docstring and `inspect_state` of `task-cycle/remove_merged_worktrees.py`; they agree.
- No test or invariant was written or changed: the change is prose, and the tests that cite sentences of WAY-375 and WAY-376 (`task-cycle/test_remove_merged_worktrees.py`) keep their quoted sentence starts, which `foundation_check.py` compares.
- Reading by the reviews: the review of the whole change read the index of its whole selection (32 decisions in full, 111 by heading), opened 10 decisions whole and read 23 by their binding sentences; it did not open the invariants file, the glossary or the environment facts whole, nor WAY-140 and WAY-153. The cycle judged that this bears on nothing the reviewer judged (the author read the invariants and the glossary whole; the change writes no invariant, glossary entry or test; the foundation check lists none), and no item 14 follows. The return step did not open `task-cycle/request_check.py`; a search of the `*.py` files for the changed state-line phrases found no match. The review of the correction read the entries it needed whole and left the rest of the decisions template unread.
- Form check of this description and check of private paths on it: written and checked after this commit; the three checks on the copy of the record: written after the record's copy is made.
- Working copies left: none.
- Directories of earlier tasks the removal script kept (name | branch | reason): agent-path-to-running-product | task/agent-path-to-running-product | the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed; ci-on-merge-requests | task/ci-on-merge-requests | the same reason; cycle-after-foundation-review | task/cycle-after-foundation-review | the same reason (this cycle's own directory); base-check-stage-remarks | detached | the branch task/stage-remarks its name gives is not found; base-fix-minor-findings | detached | the branch task/minor-findings its name gives is not found.

## Foundation entries

1. **WAY-375**, marked `row 1`, `row 2`, `row 4`: the first clearing of directories that gathered before the script is no longer named as the human's act; a copy of a base standing alone that the script does not assign to a task stays for the human; WAY-375 narrows WAY-13 in removing a cycle's own, merged directories, and WAY-13 keeps its reach over every other operation that cannot be undone. The passages of what the human accepted that give the precedence outcome (WAY-25), quoted from the frozen task: *Questions to settle*, P18, Answer: "(b) — WAY-375 zapisuje w *Relations* `narrows WAY-13`, a jej zdanie wiążące nazywa obszar: usuwanie własnych, scalonych katalogów cyklu; WAY-13 zachowuje zasięg wobec każdej innej nieodwracalnej czynności."; *To do* 4: "Zapisać w WAY-375 `narrows WAY-13` w *Relations* i w zdaniu wiążącym obszar, w którym WAY-375 przeważa: usuwanie własnych, scalonych katalogów cyklu."; and row 2 of *Settlements to record*.
2. **WAY-376**, marked `row 3`: the list of ignored paths serves a dry run that a human starts alone (the script without `--apply`); the cycle's own run with `--apply` waits for no one to read it, and the cycle's start step is unchanged.
3. **WAY-261**, marked `row 5` and `row 6`: the red result of the first run of the gate on the final tree stays the gate's result, also where the failing check is one outside the task's scope that passes when run again; the cycle does not stop, and the request names that check and the task that fixes it, or proposes it; the rule stands in this decision and in step 10 of the cycle's skill, and WAY-243 and the testing template stay unchanged.
4. **WAY-13**, *Verification* only, marked `the cycle's`: the example of a violation names its subject ("an agent treats a large task as a reason to split it …"); the binding sentence is unchanged.
5. **WAY-289**, binding sentences and *Rationale*, marked `the cycle's`: the answer "do it in this request" is offered also for something an entry stands on that the foundation does not hold yet, and runs the writing of the missing fact, decision or source.
6. **WAY-316**, a third paragraph of binding sentences, *Relations* and *Rationale*, marked `the cycle's` (written by correction 1 from your answer, no row of *Settlements to record* carries it): for a screenshot shown to the human, WAY-316 prevails over WAY-373, which keeps its reach over every other screenshot and every copy made to check something; `narrows WAY-373` stands in its *Relations*. The passage of what the human accepted that gives the outcome (WAY-25), quoted from your answer on the request: "for a screenshot shown to the human, the rule that keeps it where the product's foundation settles it prevails over WAY-373; WAY-373 keeps its reach over every other screenshot and copy made to check something." The form comes from WAY-25 and the decisions template ("Relations and precedence"), which put `narrows` on the decision that prevails and the area in its binding sentences; WAY-373 is unchanged, narrows nothing and nothing but WAY-316 narrows it.
7. The gap marked `TODO` in the *Based on* of WAY-138 (the source of the devil's advocate, the pre-mortem and the search for unknown unknowns) stands in the tree after the change; the change did not write, keep or remove it, and kind 16 of the template puts it before the human in item 1.
- Rows of the task's *Settlements to record* placed outside an entry: row 6 in step 10 of `task-cycle/skill/SKILL.md` and row 7 in `agent-instructions/README.md`.
- Invariants: none written or changed; no invariant is listed by the foundation check for a corrected sentence; no test that holds a sentence of a decision by a line `decision:` was added, dropped or altered.

## Minor findings

1. Found by the review of correction 1, in its words: "`foundations/decisions.md` WAY-316 *Verification* (lines ~6942-6968) was not extended for the new paragraph: no `complies`/`violates` line says what a conforming or violating change looks like for a shown screenshot against WAY-373 (for example, a shown screenshot left only in the agent's directory). The existing lines cover the place and the committed file, not this precedence; an agent comparing a change with the decision has no example for it. The remark did not ask for it; the correction's own-work check names no such line. Evidence: reading the *Verification* of WAY-316 whole after the change. Within the correction's reach, low consequence." A correction does not fix its own Minor findings, and the cycle judged that neither the product's user nor the person working with the process will feel it, so it carries no item above.

## Findings outside the task's scope

1. Named by the author and not graded by the reviewer, who left it outside the change: `task-cycle/change/ui_check.md` says both "keep none" and, for a place that is not settled, "move it … into your directory" for a screenshot. It lies in a file the change did not touch.
- The finding that this list carried before correction 1 (the screenshot exception in the skill against WAY-373 and WAY-316) was fixed by the correction.
- Checks outside the task's parts that failed and passed again: none.

## Course of the cycle

- **Task and sources:** the task "the way: cykl zadania po przeglądzie fundamentu — usuwanie katalogów, losowo padający test, opis prośby i korekta", an independent task, `ready for cycle`, its seven settlements accepted on 2026-11-15; its sources are the review of the foundation of 2026-11-14 (reviewed commit `21ecb62`) and the answers of the day's advisor on the human's behalf recorded in the task.
- **Process pin:** none; the-way is the repository the change is made in, and the cycle read its skill from the task's worktree.
- **Spec:** none; the task leaves no open design choice, every choice being a row of its *Settlements to record* or an answer in its *Questions to settle*.
- **Route:** one author without a plan, class `same` as the orchestrator's (the change binds across seven linked decisions); reviewed once as a whole by an agent that did not make it, with one fix for its Minor findings and one review of that fix; correction 1 (remarks: the record's file `reports/correction-1-remarks.md`; no reset, since it was made on top of the branch) was made by the resumed author and reviewed once by the same reviewer; the return steps committed nothing.
- **Plan:** none.
- **Choices:** 5 rows in the questions table of the record (no spec; the order to wait for the day's advisor's signal before each full gate; two gaps in what the reviews read, judged to bear on nothing; the kind `defect` of correction 1), besides the author's choices in its report; those whose result you see are items 2, 3, 5 and 7.
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after that commit.
