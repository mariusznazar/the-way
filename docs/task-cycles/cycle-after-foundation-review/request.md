**State: ready** — two items of *Fix or let through* wait for your answer; what you only accept by merging waits for nothing.

## What you will see

Eleven wording gaps that the review of the foundation found in the rules of the task cycle are closed; the change is text only, in the rules of the process, and no script or test changed.

- **Removal of finished directories at the start of a cycle.** The rule that lets the cycle remove its own, already merged task directories now says so openly next to the older rule that keeps every irreversible action for you: for the cycle's own merged directories the removal wins, and every other irreversible action still waits for you. The list of ignored files that the removal script prints is now described as what you read when you run the script yourself without its apply switch; the cycle does not wait for it and its start step is unchanged. A copy of a base that the script cannot match to a task stays for you to remove by hand, and the old sentence that called the first clearing of old directories your act is gone.
- **A red gate caused by a flaky test.** When the first run of the full gate on the final tree is red because of a flaky test outside the task, that red result stays the result of the gate; the cycle does not stop and does not switch the test off, and the request names the test and the task that fixes it, or proposes such a task.
- **Your answer "fix it in this request" on a request made by hand.** It now runs one fix by the author and one review of that fix by an agent that did not make it, the same loop as for a blocking remark; what stays unfixed comes back only with the question whether to make a task of it.
- **Writing and correcting a request.** The answer "do it in this request" is now named in all three places that list what it runs, also for something an entry stands on that the foundation does not hold yet. The example of the sentence that says what started a correction no longer reads as "the task required a defect". The state line of a corrected request now says what started the correction: your remarks, your answer to an item, or only a refresh from the target branch. A screenshot shown to you is kept where the product's foundation settles it, and in the agent's own directory only where it settles nothing.
- **One wording fix** in the rule on the weight of a task's process: the example of a violation now names who does it ("an agent treats a large task as a reason to split it …").

### Underneath

Five files of rules and instructions changed (the decision log, three files of the cycle's instructions and the guide for work on this repository); the full gate passed with 1457 tests.

## For you to decide

### Needed from you

none

### Fix or let through

1. The cycle's instructions now say that a screenshot meant for you is kept where the product's foundation settles it, and only otherwise in the agent's own directory. An older rule of the foundation, about where an agent keeps its working copies, still lists "a screenshot" among the copies kept in the agent's directory, with no exception, and the rule that says where your screenshots go does not say that it overrides the older one. The reviewer thought the two can be read together, since a screenshot shown to you is no copy made "to check something", but nobody has written that down. Whoever feels it is an agent of a later cycle that reads the foundation and not the cycle's instructions when it has a screenshot to show you: it would put it in its own directory, and you would not see it. Fixing it in this request costs one more correction with a review, and it edits a rule the task did not name; making a task keeps this request to its own task, leaves the gap until that task is done, and costs nothing else today; letting it through accepts the gap for good. I recommend making a task, since which of the two rules prevails is a decision of its own that the task did not ask for. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)
2. One old gap that this change did not make and did not touch: the rule that says how a technology choice is tested for what choosing it could break (a devil's advocate, a pre-mortem and a search for unknown unknowns) names the three tests but no source they were taken from, and the foundation marks the source as missing. A person who wants to check where the rule comes from finds nothing to check against. Writing the source in this request costs finding the document it comes from and a round of review; making a task leaves the gap standing until then; letting it through accepts it on the main branch. I recommend making a task, since finding the source needs a decision on which document to cite and has nothing to do with this change. Write it in this request, make a task of it, or let it through? (Foundation entries, 6)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The cycle chose the words of the state line of a corrected request: "corrected for your remarks" only where your remarks started the correction, "corrected for your answer to an item" where your answer to an item did, and "refreshed from the target branch at your request" where only that did, each in its words when there are two sources. The task fixed only the first phrase and asked that the line say what started the correction; I did not fix one phrase for each source inside a script, since the task did not touch the script and nothing reads these phrases.
4. The cycle added to the part of the request for findings outside the task's scope one clause: for a check outside the task's parts that failed and passed again, the request also gives the task that fixes it, or the proposal of one. The task asked that the request name that task but left the template of the request unchanged, and the reviewer found that the form had no place for it; I did not leave the wording to each cycle, since then different requests would word it or leave it out in different ways.
5. The decision about removing finished directories now outranks, for the cycle's own merged directories only, the rule that has you perform every irreversible action; the rule keeps its reach over every other irreversible action. The passages you accepted that give this outcome are quoted in the lower part. I did not narrow the sentence of the older rule itself, since it would then stop reaching irreversible actions of the cycle outside a change, and a new one would meet nothing that stops it. (Foundation entries, 1)
6. The example of a violation in the rule on the weight of a task's process now names who does it ("an agent treats a large task as a reason to split it …"); its meaning is unchanged, and the rule itself did not change. (Foundation entries, 4)
7. The answer "do it in this request" is now named, also for something an entry stands on that the foundation does not hold yet, in the rule about which unfinished things a request puts before you and in the correction instructions. The task placed the list of such answers in the rule; it stands in the correction instructions, so I changed both places. (Foundation entries, 5)

## Cost

About 26 minutes of working time of the cycle, with 11 minutes of waiting for tools and about 25.5 million tokens, all on one model (Claude Sonnet 5.5); one review round of the whole change that passed with two small notes within the task, one fix for them and one review of that fix, which passed. The table of stages is in the cycle's record; its link is added with the record. Directories of earlier tasks still stand because the script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand; their names, branches and reasons stand in *Checks*.

## How to merge

Merge it so that the commits are kept (a merge commit), since the link to the record of the cycle survives only then.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — dwie pozycje z części „Popraw albo przepuść” czekają na Twoją odpowiedź; to, co tylko akceptujesz przez scalenie, na nic nie czeka.

## Co zobaczysz

Zamknięte jest jedenaście luk w sformułowaniach reguł cyklu zadania, które znalazł przegląd fundamentu; zmiana to sam tekst reguł procesu, żaden skrypt ani test się nie zmienił.

- **Usuwanie zakończonych katalogów na starcie cyklu.** Reguła pozwalająca cyklowi usuwać własne, już scalone katalogi zadań mówi teraz o tym wprost obok starszej reguły, która zostawia Tobie każdą czynność nieodwracalną: dla własnych, scalonych katalogów cyklu przeważa usuwanie, a każda inna czynność nieodwracalna dalej czeka na Ciebie. Lista plików ignorowanych, którą drukuje skrypt usuwający, jest opisana jako to, co czytasz, gdy sam uruchamiasz skrypt bez przełącznika zastosowania; cykl na nią nie czeka, a jego krok startu się nie zmienia. Kopia bazowa, której skrypt nie przypisze do zadania, zostaje Tobie do ręcznego usunięcia, a stare zdanie nazywające pierwsze sprzątanie starych katalogów Twoją czynnością zniknęło.
- **Czerwona bramka od losowo padającego testu.** Gdy pierwszy przebieg pełnej bramki na końcowym drzewie jest czerwony przez losowo padający test spoza zadania, ten czerwony wynik zostaje wynikiem bramki; cykl się nie zatrzymuje i nie wyłącza testu, a prośba nazywa test i zadanie, które go naprawi, albo je proponuje.
- **Twoja odpowiedź „napraw to w tej prośbie” przy prośbie zrobionej ręcznie.** Uruchamia teraz jedną poprawkę autora i jedną recenzję tej poprawki przez agenta, który jej nie robił — tę samą pętlę co dla uwagi blokującej; to, co zostaje niepoprawione, wraca tylko z pytaniem, czy zrobić z tego zadanie.
- **Pisanie i korekta prośby.** Odpowiedź „zrób to w tej prośbie” jest teraz wymieniona we wszystkich trzech miejscach, które mówią, co ona uruchamia, także dla rzeczy, na której stoi wpis, a której fundament jeszcze nie zawiera. Przykład zdania mówiącego, co uruchomiło korektę, nie brzmi już jak „zadanie wymagało defektu”. Linia stanu skorygowanej prośby mówi teraz, co uruchomiło korektę: Twoje uwagi, Twoja odpowiedź na pozycję albo samo odświeżenie z gałęzi docelowej. Zrzut ekranu pokazywany Tobie trafia tam, gdzie ustala go fundament produktu, a do katalogu agenta tylko tam, gdzie fundament nic nie ustala.
- **Jedna poprawka brzmienia** w regule o ciężarze procesu zadania: przykład naruszenia ma teraz podmiot („an agent treats a large task as a reason to split it …”).

### Pod spodem

Zmieniło się pięć plików reguł i instrukcji (dziennik decyzji, trzy pliki instrukcji cyklu i przewodnik pracy nad tym repozytorium); pełna bramka przeszła z 1457 testami.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Popraw albo przepuść

1. Instrukcje cyklu mówią teraz, że zrzut ekranu przeznaczony dla Ciebie trafia tam, gdzie ustala go fundament produktu, a tylko w innym razie do katalogu agenta. Starsza reguła fundamentu, o tym, gdzie agent trzyma kopie robocze, nadal wymienia „zrzut ekranu” wśród kopii trzymanych w katalogu agenta, bez wyjątku, a reguła mówiąca, gdzie idą Twoje zrzuty, nie mówi, że przeważa nad starszą. Recenzent uznał, że da się je czytać razem, bo zrzut pokazywany Tobie nie jest kopią robioną „żeby coś sprawdzić”, ale nikt tego nie zapisał. Odczuje to agent późniejszego cyklu, który czyta fundament, a nie instrukcje cyklu, gdy będzie miał zrzut do pokazania Tobie: położyłby go w swoim katalogu i nie zobaczyłbyś go. Poprawienie w tej prośbie kosztuje jeszcze jedną korektę z recenzją i zmienia regułę, której zadanie nie wskazało; zrobienie zadania zostawia tę prośbę przy jej zadaniu, zostawia lukę do czasu tamtego zadania i dziś nic więcej nie kosztuje; przepuszczenie przyjmuje lukę na stałe. Rekomenduję zrobić zadanie, bo to, która z dwóch reguł przeważa, jest osobną decyzją, o którą zadanie nie prosiło. Poprawić w tej prośbie, zrobić z tego zadanie, czy przepuścić? (Findings outside the task's scope, 1)
2. Jedna stara luka, której ta zmiana nie zrobiła i której nie ruszyła: reguła mówiąca, jak wybór technologii jest sprawdzany pod kątem tego, co jego wybór mógłby zepsuć (adwokat diabła, pre-mortem i szukanie nieznanych niewiadomych), nazywa trzy sprawdziany, ale nie podaje źródła, z którego je wzięto, a fundament oznacza to źródło jako brakujące. Kto chce sprawdzić, skąd reguła pochodzi, nie ma z czym sprawdzić. Dopisanie źródła w tej prośbie kosztuje znalezienie dokumentu, z którego pochodzi, i rundę recenzji; zrobienie zadania zostawia lukę do czasu tamtego zadania; przepuszczenie przyjmuje ją na głównej gałęzi. Rekomenduję zrobić zadanie, bo znalezienie źródła wymaga decyzji, który dokument zacytować, i nie ma nic wspólnego z tą zmianą. Dopisać w tej prośbie, zrobić z tego zadanie, czy przepuścić? (Foundation entries, 6)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

3. Cykl dobrał słowa linii stanu skorygowanej prośby: „poprawiona dla Twoich uwag” tylko tam, gdzie korektę uruchomiły Twoje uwagi, „poprawiona dla Twojej odpowiedzi na pozycję” tam, gdzie uruchomiła ją Twoja odpowiedź na pozycję, a „odświeżona z gałęzi docelowej na Twoją prośbę” tam, gdzie tylko to; przy dwóch źródłach każde własnymi słowami. Zadanie ustaliło tylko pierwsze sformułowanie i poprosiło, by linia mówiła, co uruchomiło korektę; nie ustaliłem jednego sformułowania dla każdego źródła w skrypcie, bo zadanie skryptu nie dotyka i nic tych sformułowań nie czyta.
4. Cykl dopisał w części prośby o ustaleniach spoza zakresu zadania jedną klauzulę: dla sprawdzenia spoza części zadania, które padło i przeszło po powtórce, prośba podaje też zadanie, które je naprawi, albo propozycję takiego zadania. Zadanie prosiło, by prośba nazywała to zadanie, ale zostawiało szablon prośby bez zmian, a recenzent stwierdził, że formularz nie ma na to miejsca; nie zostawiłem sformułowania każdemu cyklowi, bo wtedy różne prośby sformułowałyby to albo pominęły na różne sposoby.
5. Decyzja o usuwaniu zakończonych katalogów przeważa teraz, tylko dla własnych, scalonych katalogów cyklu, nad regułą, która każe Tobie wykonywać każdą czynność nieodwracalną; reguła zachowuje zasięg wobec każdej innej czynności nieodwracalnej. Fragmenty, które zaakceptowałeś, a które dają ten wynik, są zacytowane w dolnej części. Nie zawężałem samego zdania starszej reguły, bo przestałaby wtedy obejmować nieodwracalne czynności cyklu poza zmianą, a nowa taka czynność nie napotkałaby niczego, co ją zatrzymuje. (Foundation entries, 1)
6. Przykład naruszenia w regule o ciężarze procesu zadania ma teraz podmiot („an agent treats a large task as a reason to split it …”); jego znaczenie jest bez zmian, a sama reguła się nie zmieniła. (Foundation entries, 4)
7. Odpowiedź „zrób to w tej prośbie” jest teraz wymieniona, także dla rzeczy, na której stoi wpis, a której fundament jeszcze nie zawiera, w regule o tym, które niedokończone sprawy prośba stawia przed Tobą, i w instrukcjach korekty. Zadanie umieściło listę takich odpowiedzi w regule; stoi ona w instrukcjach korekty, więc zmieniłem oba miejsca. (Foundation entries, 5)

## Koszt

Około 26 minut czasu pracy cyklu, w tym 11 minut czekania na narzędzia, i około 25,5 miliona tokenów, wszystkie na jednym modelu (Claude Sonnet 5.5); jedna runda recenzji całości, która przeszła z dwiema drobnymi uwagami w zakresie zadania, jedna poprawka dla nich i jedna recenzja tej poprawki, która przeszła. Tabela etapów jest w zapisie cyklu; jej link dochodzi razem z zapisem. Katalogi wcześniejszych zadań nadal stoją, bo skrypt nie mógł rozpoznać, że nie są już potrzebne; nic w tej prośbie na nie nie czeka i możesz je usunąć ręcznie; ich nazwy, gałęzie i powody są w *Checks*.

## Jak scalić

Scal tak, by zachować commity (merge commit), bo link do zapisu cyklu przetrwa tylko wtedy.

</details>

## Technical changes

The change is two commits on `task/cycle-after-foundation-review`, from the base `739c813` (the head of `foundations`), made by one author without a plan and without a spec (no open design choice).

- `6727b67`, the change: `foundations/decisions.md` (WAY-13 *Verification*; WAY-375 binding sentences, *Relations*, *Rationale*, *Rejected*; WAY-376 binding sentence, *Rationale*, *Rejected*; WAY-261 a second paragraph, *Verification*, *Rationale*, *Rejected*; WAY-289 binding sentences and *Rationale*), `task-cycle/skill/SKILL.md` (step 10 paragraph; first paragraph of "Working copies"), `task-cycle/skill/correction.md` (list of kinds that "do it in this request" runs), `task-cycle/skill/request_template.md` (kind 17's example sentence; the row "A correction" of the variants table) and `agent-instructions/README.md` ("Integrate into `foundations`"). 5 files, 111 added and 57 removed lines.
- `cfda61e`, the fix of the two Minor findings of the review of the whole change: `task-cycle/skill/request_template.md` (the clause on the task that fixes a flaky check, in *Findings outside the task's scope*) and `foundations/decisions.md` (WAY-375: "a copy of a base standing alone"). 2 files, 5 changed lines.
- The return step committed nothing: the entries and the part map still matched the files.
- Not changed: WAY-243, the testing template, the glossary entry *human action*, `task-cycle/remove_merged_worktrees.py`, the invariants and the part map.

## Checks

- Gate: `python -B task-cycle/gate_times.py --output .runs/task-cycles/cycle-after-foundation-review/gate_times.md -- python -B gate/run_tests.py`, exit 0 on `cfda61e` (the final tree): 1457 tests in 10 directories, 345.8 s, no other gate run at the same time, every directory passed; run once, no check failed or did not run.
- Failing before the change: none; no gate run on the base. The base `739c813` is a merge whose tree equals that of its second parent, so the list was taken from the final gate of the earlier cycle, `docs/task-cycles/part-map-dependencies-task-line/cycle.md` of commit `8200eb3` (run 2, exit 0, 1457 tests, every directory passed).
- `python -B elements/common/foundation_check.py` without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 3`, `threshold: 60`, `reminder: no`.
- Focused checks by the author, the fix author and the reviewers: `python -B gate/run_tests.py elements/common` (235 tests), `task-cycle` (483), `agent-instructions` (25), `process-audit`: exit 0 each; the check of private paths on each changed file: 0 listed.
- Own-work checks: the author searched the tracked files for the statements the change removes ("first clearing", "hand clearing", "sees before", "loose copies") and found them only in the *Rejected* of WAY-375 and WAY-376 where the ways not chosen are named; the fix author checked that the fix grows nothing beyond its two findings (5 changed lines). The reviewer of the whole change compared the new sentences of WAY-375 and WAY-376 with the docstring and `inspect_state` of `task-cycle/remove_merged_worktrees.py`; they agree.
- No test or invariant was written or changed: the change is prose, and the tests that cite sentences of WAY-375 and WAY-376 (`task-cycle/test_remove_merged_worktrees.py`) keep their quoted sentence starts, which `foundation_check.py` compares.
- Reading by the reviews: the review of the whole change read the index of its whole selection (32 decisions in full, 111 by heading), opened 10 decisions whole and read 23 by their binding sentences; it did not open the invariants file, the glossary or the environment facts whole, nor WAY-140 and WAY-153. The cycle judged that this bears on nothing the reviewer judged (the author read the invariants and the glossary whole; the change writes no invariant, glossary entry or test; the foundation check lists none), and no item 14 follows. The return step did not open `task-cycle/request_check.py`; a search of the `*.py` files for the changed state-line phrases found no match.
- Form check of this description: written and checked after this commit; the check of private paths on it and on the copy of the record, the image check and the remarks check on the copy: written after the record's copy is made.
- Working copies left: none.
- Directories of earlier tasks the removal script kept (name | branch | reason): agent-path-to-running-product | task/agent-path-to-running-product | the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed; ci-on-merge-requests | task/ci-on-merge-requests | the same reason; cycle-after-foundation-review | task/cycle-after-foundation-review | the same reason (this cycle's own directory); base-check-stage-remarks | detached | the branch task/stage-remarks its name gives is not found; base-fix-minor-findings | detached | the branch task/minor-findings its name gives is not found.

## Foundation entries

1. **WAY-375**, marked `row 1`, `row 2`, `row 4`: the first clearing of directories that gathered before the script is no longer named as the human's act; a copy of a base standing alone that the script does not assign to a task stays for the human; WAY-375 narrows WAY-13 in removing a cycle's own, merged directories, and WAY-13 keeps its reach over every other operation that cannot be undone. The passages of what the human accepted that give the precedence outcome (WAY-25), quoted from the frozen task: *Questions to settle*, P18, Answer: "(b) — WAY-375 zapisuje w *Relations* `narrows WAY-13`, a jej zdanie wiążące nazywa obszar: usuwanie własnych, scalonych katalogów cyklu; WAY-13 zachowuje zasięg wobec każdej innej nieodwracalnej czynności."; *To do* 4: "Zapisać w WAY-375 `narrows WAY-13` w *Relations* i w zdaniu wiążącym obszar, w którym WAY-375 przeważa: usuwanie własnych, scalonych katalogów cyklu."; and row 2 of *Settlements to record*.
2. **WAY-376**, marked `row 3`: the list of ignored paths serves a dry run that a human starts alone (the script without `--apply`); the cycle's own run with `--apply` waits for no one to read it, and the cycle's start step is unchanged.
3. **WAY-261**, marked `row 5` and `row 6`: the red result of the first run of the gate on the final tree stays the gate's result, also where the failing check is one outside the task's scope that passes when run again; the cycle does not stop, and the request names that check and the task that fixes it, or proposes it; the rule stands in this decision and in step 10 of the cycle's skill, and WAY-243 and the testing template stay unchanged.
4. **WAY-13**, *Verification* only, marked `the cycle's`: the example of a violation names its subject ("an agent treats a large task as a reason to split it …"); the binding sentence is unchanged.
5. **WAY-289**, binding sentences and *Rationale*, marked `the cycle's`: the answer "do it in this request" is offered also for something an entry stands on that the foundation does not hold yet, and runs the writing of the missing fact, decision or source.
6. The gap marked `TODO` in the *Based on* of WAY-138 (the source of the devil's advocate, the pre-mortem and the search for unknown unknowns) stands in the tree after the change; the change did not write, keep or remove it, and kind 16 of the template puts it before the human in item 2.
- Rows of the task's *Settlements to record* placed outside an entry: row 6 in step 10 of `task-cycle/skill/SKILL.md` and row 7 in `agent-instructions/README.md`.
- Invariants: none written or changed; no invariant is listed by the foundation check for a corrected sentence; no test that holds a sentence of a decision by a line `decision:` was added, dropped or altered.

## Minor findings

none

## Findings outside the task's scope

1. Marked Minor and outside the task by the reviewer of the whole change, in its words: "`task-cycle/skill/SKILL.md` "Working copies" first paragraph (new exception for a screenshot shown to the human) against WAY-373, whose binding sentence lists "a screenshot" among the working copies that stand in the agent's directory under `.runs/` with no exception, and against WAY-316, which says where a screenshot shown to the human lies but has no `narrows WAY-373`. The skill now carries a precedence that no decision records; WAY-25 requires the precedence to stand in the decision that prevails. The author read the two as compatible (a screenshot shown to the human is no copy made "to check something"), and that reading is reasonable; the task's item 11 names the skill only. A later reader who reads WAY-373 alone gets the old rule. Proposed fix, for a later task: in WAY-373 say that a screenshot shown to the human is outside the sentence (or record `narrows WAY-373` in WAY-316). This lies outside the task." Its place: the first paragraph of "Working copies" in `task-cycle/skill/SKILL.md`, and WAY-373 and WAY-316 in `foundations/decisions.md`.
2. Named by the author and not graded by the reviewer, who left it outside the change: `task-cycle/change/ui_check.md` says both "keep none" and, for a place that is not settled, "move it … into your directory" for a screenshot. It lies in a file the change did not touch.
- Checks outside the task's parts that failed and passed again: none.

## Course of the cycle

- **Task and sources:** the task "the way: cykl zadania po przeglądzie fundamentu — usuwanie katalogów, losowo padający test, opis prośby i korekta", an independent task, `ready for cycle`, its seven settlements accepted on 2026-11-15; its sources are the review of the foundation of 2026-11-14 (reviewed commit `21ecb62`) and the answers of the day's advisor on the human's behalf recorded in the task.
- **Process pin:** none; the-way is the repository the change is made in, and the cycle read its skill from the task's worktree.
- **Spec:** none; the task leaves no open design choice, every choice being a row of its *Settlements to record* or an answer in its *Questions to settle*.
- **Route:** one author without a plan, class `same` as the orchestrator's (the change binds across seven linked decisions); reviewed once as a whole by an agent that did not make it, with one fix for its Minor findings and one review of that fix; the return step committed nothing.
- **Plan:** none.
- **Choices:** 4 rows in the questions table of the record (no spec; the order to wait for the day's advisor's signal before each full gate; two gaps in what the reviews read, judged to bear on nothing), besides the author's choices in its report; those whose result you see are items 3, 4 and 7.
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written with the next edit of this description.
