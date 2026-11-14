**State: blocked** — waits for an action of yours outside the repository: the one-time clean-up of the old working directories, which only you run; the change itself is made and reviewed.

## What you will see

Until now a task cycle left the working directory of its task standing "for corrections" and nothing ever removed it, so old task directories piled up on your disk and in the list of directories git keeps for a repository. After this change a script does the sweeping, and every new cycle runs it by itself at its start, in the-way and in every product that uses it.

- The script looks at every working directory git lists for the repository and prints, for each one, "remove" or "keep" and the reason. By default it only prints. It deletes only when it is started with the switch `--apply`, and a deletion cannot be undone.
- It removes a directory only when all of this is true at once: nothing in it is uncommitted (files git ignores do not count), every commit in it is already on the remote, its branch is merged, and the directory belongs to a task cycle (it stands on a task branch, or it is a copy of the base that a reviewer made under the task's own working folder). Nested copies of the base inside a task directory go with it.
- "Merged" is judged by git alone, with no question to GitHub: the branch's last commit must be the second parent of a merge commit on the main line of the target branch. A branch merged by squash or rebase is not recognised, and neither is a request closed without merging; those directories stay and are listed with the reason.
- It never touches the main checkout, the directory it is started from, directories that are no part of a cycle (the one your skill link points to, the full-run copy, copies in a session's scratch folder), and it never deletes a branch, local or remote.
- Before it deletes a directory, the dry run shows that directory's ignored paths outside the task's own working folder (for example a local settings file), so you see what would be lost.
- The cycle puts the directories of its own kind that stayed, each as a name, a branch and a reason without a path, into its record and into the description of its request, so you see them in the request. A correction after review does not run the script. The sentence "keep the worktree for corrections" now says the directory lies there until its branch is merged, and that the script removes it.

### Underneath

The decision that said the fast-forward of the checkout is the one change a cycle makes outside its own directory is rewritten, because the removal is now a second one; two new decisions hold what the script may remove and how it reads "clean".

## For you to decide

### Needed from you

1. The one-time clean-up of the old working directories is yours to run, in two repositories: the-way and `loop2`. It uses the new script, which exists only on this branch, and it reaches directories beside the repositories, so no cycle may do it. Without it, nothing is wrong today, but the first cycle after the merge would run the script with the real switch and delete the whole backlog at once, more than a hundred directories, with no look from you and no way back. Your steps: from this task's working directory, run the script in its default mode for the-way and for `loop2` (the exact commands stand in the lower part, *Technical changes*, 1), read each list of "remove / keep" with its reasons and the ignored paths shown, and when you accept a list, run the script again with the real switch for that repository. Doing it before the merge costs a few minutes and one reading of two lists; the lists also name the directories that stay for your own decision. I recommend doing it before the merge, so that the first cycle after it finds almost nothing to delete. Will you run the clean-up in both repositories before you merge?

### Fix or let through

2. The whole test run of the-way ended red, on one test that is unrelated to this change. The test that checks the runner's option limiting how many directories run at once is a race: it passes in a second most times and sometimes waits two minutes and fails. It failed in the last run of this cycle and in two reruns of this cycle on this branch; on the unchanged base it failed in one of three runs, so the change did not cause it. Everyone who runs the whole suite will meet it now and then, and a red run costs a rerun and a doubt. Fixing it in this request costs a correction and its review, in a part this task does not own; making a task of it leaves this request as it is; letting it through leaves the test as it was. I recommend making a task of it, since it is a separate defect in a separate part. Fix it in this request, make a task of it, or let it through? (Checks, 1 and Findings outside the task's scope, 1)

3. The word "human action" is used in two senses. The glossary says a human action is an act outside the repository that a task needs and a human performs, and the new decision says that the script's removal of a directory beside the repository needs no human action, while this task itself lists the one-time clean-up as one. A reader who takes the glossary meaning may think the two contradict each other; the script and the one-time step both work as designed, and the task settled this wording itself. Tightening the other decision's phrase belongs to that decision, not to this change. I recommend making a task of it. Fix it in this request, make a task of it, or let it through? (Minor findings, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. A copy of the base nested inside a task directory goes with the directory whatever its name, as long as it is clean, on the remote and not on a branch; the task named only one name pattern for these. The agents' own copies have arbitrary names, so a name rule would keep every task directory that holds one and defeat the purpose. The price: a clean, pushed scratch copy of another name goes too.

5. A directory counts as a cycle's when its branch starts with the task prefix or when it holds the cycle's record folder, since a merged branch of an earlier task had no such prefix. The price: your own directory with a record folder in it is judged too, and removed only if it passes every other test.

6. The script has an option the task did not name, to skip the fetch and judge by the remote refs as they stand. I needed it for dry runs that must not move any ref; the cycle itself never uses it, and it can only make the script keep more.

7. Loose copies of the base in the main checkout are removed only when their name points to a task whose branch is merged. Two of the eight in the-way (their names do not give the task branch) stay and are listed for you. The price: they stay until you remove them by hand; the alternative, guessing a branch from a name, could delete a running cycle's copy.

8. A branch merged only through another branch, not directly on the target branch's main line, is not recognised as merged and stays. The task's own warning about a branch made a moment ago by a parallel cycle needed this stricter reading, since a merge of the target into a task branch would otherwise make a fresh branch look merged.

9. The new test of the script carries ten lines tying it to the two new decisions, so a later change to either decision is checked against it; no invariant, no surface and no marked violation changes, and the foundation check lists nothing.

## Cost

About 1 hour 24 minutes of working time, of which 42 minutes waiting for tools, on one model (the same as the orchestrator's) and about 60 million tokens counting repeated reads of the same context; the table of stages is in the committed record. Review rounds: the whole change was reviewed once and failed, its one fix was reviewed and passed; the return step was reviewed and passed; a failure of the whole test run after that got one more fix, reviewed and passed, and a second run of the whole suite. No directory of an earlier task was left standing by the script, since this cycle ran on the instructions as they were before this change and so did not run it.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Do not merge before you have decided item 1.

The foundation has waited for a review through 47 merges since the last review (tag `foundation-review/2026-11-06`); the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: zablokowany** — czeka na Twój ruch poza repozytorium: jednorazowe sprzątanie starych katalogów roboczych, które uruchamiasz tylko Ty; sama zmiana jest zrobiona i przejrzana.

## Co zobaczysz

Dotąd cykl zadania zostawiał katalog roboczy zadania „do poprawek” i nic go nie usuwało, więc stare katalogi zadań zalegały na Twoim dysku i na liście katalogów, którą git trzyma dla repozytorium. Po tej zmianie sprząta skrypt, a każdy nowy cykl uruchamia go sam na starcie, w the-way i w każdym produkcie, który go używa.

- Skrypt przegląda każdy katalog roboczy, który git wymienia dla repozytorium, i dla każdego wypisuje „usunę” albo „zostawiam” z powodem. Domyślnie tylko wypisuje. Usuwa dopiero z przełącznikiem `--apply`, a usunięcia nie da się cofnąć.
- Katalog usuwa tylko wtedy, gdy spełnione jest wszystko naraz: nic w nim nie jest niezacommitowane (pliki ignorowane przez git się nie liczą), każdy jego commit jest już na zdalnym repozytorium, jego gałąź jest scalona, a katalog należy do cyklu zadania (leży na gałęzi zadania albo jest kopią bazy, którą zrobił recenzent w roboczym folderze zadania). Zagnieżdżone kopie bazy wewnątrz katalogu zadania znikają razem z nim.
- „Scalona” oznacza ocenę samym gitem, bez pytania GitHuba: ostatni commit gałęzi musi być drugim rodzicem commita scalającego na głównej linii gałęzi docelowej. Gałąź scalona squashem albo rebase’em nie jest rozpoznana, tak samo PR zamknięty bez scalenia; takie katalogi zostają i trafiają na listę z powodem.
- Nigdy nie rusza kopii głównej, katalogu, z którego jest uruchomiony, katalogów spoza cyklu (tego, na który wskazuje dowiązanie Twojego skilla, kopii pełnego przebiegu, kopii w schowkach sesji) i nigdy nie usuwa gałęzi, ani lokalnej, ani zdalnej.
- Zanim usunie katalog, suchy przebieg pokazuje jego ignorowane ścieżki poza roboczym folderem zadania (na przykład lokalny plik ustawień), żebyś widział, co by przepadło.
- Cykl zapisuje katalogi swojego rodzaju, które zostały, jako nazwę, gałąź i powód, bez ścieżki, w swoim zapisie i w opisie PR-a, więc widzisz je w PR-ze. Poprawka po przeglądzie nie uruchamia skryptu. Zdanie „katalog zostaje do poprawek” mówi teraz, że katalog leży do scalenia jego gałęzi, a potem usuwa go skrypt.

### Pod spodem

Decyzja, która mówiła, że fast-forward jest jedyną zmianą cyklu poza własnym katalogiem, jest przepisana, bo usuwanie to druga taka zmiana; dwie nowe decyzje trzymają to, co skrypt może usunąć, i jak czyta „czyste”.

## Do Twojej decyzji

### Potrzebne od Ciebie

1. Jednorazowe sprzątnięcie starych katalogów roboczych jest Twoje, w dwóch repozytoriach: the-way i `loop2`. Korzysta z nowego skryptu, który istnieje tylko na tej gałęzi, i sięga katalogów obok repozytoriów, więc żaden cykl nie może tego zrobić. Bez tego dziś nic się nie psuje, ale pierwszy cykl po scaleniu uruchomiłby skrypt z prawdziwym przełącznikiem i skasował całe zaległości naraz, ponad sto katalogów, bez Twojego wglądu i bez drogi powrotnej. Twoje kroki: z katalogu roboczego tego zadania uruchom skrypt w trybie domyślnym dla the-way i dla `loop2` (dokładne polecenia są w dolnej części, *Technical changes*, 1), przeczytaj każdą listę „usunę / zostawiam” z powodami i pokazanymi ścieżkami ignorowanymi, a gdy listę zaakceptujesz, uruchom skrypt jeszcze raz z prawdziwym przełącznikiem dla tego repozytorium. Zrobienie tego przed scaleniem kosztuje kilka minut i jedno czytanie dwóch list; listy wskażą też katalogi, które zostają do Twojej decyzji. Polecam zrobić to przed scaleniem, żeby pierwszy cykl po nim zastał prawie nic do usunięcia. Czy uruchomisz sprzątanie w obu repozytoriach przed scaleniem?

### Poprawić czy przepuścić

2. Pełny przebieg testów the-way skończył się na czerwono, na jednym teście niezwiązanym z tą zmianą. Test sprawdzający opcję runnera, która ogranicza liczbę jednocześnie uruchamianych katalogów, jest wyścigiem: zwykle przechodzi w sekundę, czasem czeka dwie minuty i pada. Padł w ostatnim przebiegu tego cyklu i w dwóch ponownych uruchomieniach tego cyklu na tej gałęzi; na niezmienionej bazie padł raz na trzy próby, więc zmiana go nie spowodowała. Każdy, kto uruchamia cały zestaw, trafi na to od czasu do czasu, a czerwony przebieg kosztuje ponowne uruchomienie i wątpliwość. Naprawa w tym PR-ze kosztuje poprawkę i jej przegląd, w części, której to zadanie nie posiada; zrobienie z tego zadania zostawia ten PR bez zmian; przepuszczenie zostawia test jak był. Polecam zrobić z tego zadanie, bo to osobny błąd w osobnej części. Poprawić w tym PR-ze, zrobić zadanie czy przepuścić? (Checks, 1 oraz Findings outside the task's scope, 1)

3. Słowo „ruch ludzki” (human action) jest użyte w dwóch znaczeniach. Słownik mówi, że to czynność poza repozytorium, której zadanie potrzebuje i którą wykonuje człowiek, a nowa decyzja mówi, że usunięcie przez skrypt katalogu obok repozytorium nie wymaga takiego ruchu, podczas gdy samo zadanie wymienia jednorazowe sprzątnięcie jako taki ruch. Czytelnik, który przyjmie znaczenie ze słownika, może uznać, że te dwa zapisy się wykluczają; skrypt i jednorazowy krok działają zgodnie z założeniem, a brzmienie ustaliło samo zadanie. Doprecyzowanie frazy drugiej decyzji należy do tamtej decyzji, nie do tej zmiany. Polecam zrobić z tego zadanie. Poprawić w tym PR-ze, zrobić zadanie czy przepuścić? (Minor findings, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te punkty; jeśli któryś Ci nie odpowiada, napisz który.

4. Zagnieżdżona kopia bazy w katalogu zadania znika razem z katalogiem bez względu na nazwę, jeśli jest czysta, na zdalnym i nie na gałęzi; zadanie wymieniło tylko jeden wzorzec nazwy. Kopie robione przez agentów mają dowolne nazwy, więc reguła po nazwie zatrzymałaby każdy katalog zadania, który taką kopię ma, i zniweczyła cel. Cena: czysta, wypchnięta kopia robocza o innej nazwie też zniknie.

5. Katalog liczy się jako należący do cyklu, gdy jego gałąź zaczyna się od prefiksu zadania albo gdy ma folder zapisu cyklu, bo scalona gałąź jednego z wcześniejszych zadań nie miała tego prefiksu. Cena: Twój własny katalog z takim folderem w środku też jest oceniany, a usuwany tylko, jeśli przejdzie wszystkie pozostałe próby.

6. Skrypt ma opcję, której zadanie nie wymieniło: pominięcie pobrania zdalnych refów i ocenę po refach w stanie, w jakim są. Potrzebowałem jej do suchych przebiegów, które nie mogą ruszyć żadnego refa; sam cykl jej nie używa, a może ona tylko sprawić, że skrypt zostawi więcej.

7. Luźne kopie bazy w kopii głównej są usuwane tylko wtedy, gdy ich nazwa wskazuje zadanie ze scaloną gałęzią. Dwie z ośmiu w the-way (ich nazwy nie wskazują gałęzi zadania) zostają i są wypisane dla Ciebie. Cena: zostają, dopóki ich ręcznie nie usuniesz; alternatywa, zgadywanie gałęzi po nazwie, mogłaby skasować kopię trwającego cyklu.

8. Gałąź scalona tylko przez inną gałąź, nie wprost na głównej linii gałęzi docelowej, nie jest rozpoznana jako scalona i zostaje. Ostrzeżenie samego zadania o gałęzi założonej chwilę wcześniej przez równoległy cykl wymagało tego ostrzejszego odczytu, bo inaczej scalenie gałęzi docelowej do gałęzi zadania sprawiłoby, że świeża gałąź wyglądałaby na scaloną.

9. Nowy test skryptu niesie dziesięć linii wiążących go z dwiema nowymi decyzjami, więc późniejsza zmiana którejś z nich jest sprawdzana względem niego; żaden niezmiennik, żadna powierzchnia ani oznaczone naruszenie się nie zmienia, a kontrola fundamentu niczego nie wypisuje.

## Koszt

Około 1 godziny 24 minut czasu pracy, z czego 42 minuty czekania na narzędzia, na jednym modelu (tym samym co orkiestrator) i około 60 milionów tokenów licząc powtarzane odczyty tego samego kontekstu; tabela etapów jest w zatwierdzonym zapisie. Rundy przeglądu: całą zmianę przejrzano raz i nie przeszła, jej jedną poprawkę przejrzano i przeszła; krok powrotny przejrzano i przeszedł; po awarii pełnego przebiegu testów była jeszcze jedna poprawka, przejrzana i przeszła, oraz drugi przebieg całego zestawu. Skrypt nie zostawił żadnego katalogu wcześniejszego zadania, bo ten cykl szedł według instrukcji sprzed tej zmiany i go nie uruchamiał.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przetrwa tylko wtedy. Nie scalaj, zanim nie rozstrzygniesz punktu 1.

Fundament czeka na przegląd przez 47 scaleń od ostatniego przeglądu (znacznik `foundation-review/2026-11-06`); przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium; nic w tym PR-ze na niego nie czeka.

</details>

## Technical changes

The change adds the script that lists and removes the working directories of earlier tasks, its test, two decisions and the wiring of the script into the start of a cycle; one follow-up fixes the test after the gate. Nothing in this change was run against a real working directory with the real switch: the tests use throwaway repositories, and the dry runs on the real repositories only read.

1. `9fe7f66` — adds `task-cycle/remove_merged_worktrees.py` (530 lines) and `task-cycle/test_remove_merged_worktrees.py` (617 lines, 42 tests then). To run the one-time clean-up (item 1 of *For you to decide*), from the root of the task's working directory, `python -B task-cycle/remove_merged_worktrees.py` lists the-way's directories; `python -B task-cycle/remove_merged_worktrees.py --repository <the main checkout of loop2>` lists `loop2`'s; add `--apply` to the same command to remove the directories listed `remove` after you have read the list; `--no-fetch` skips the fetch.
2. `25daf50` — foundation entries: WAY-298 rewritten in place (the fast-forward and the removal at the start of a cycle are the two changes outside the task's directory), WAY-375 (what the script removes and what it touches) and WAY-376 (ignored files do not count against "clean", and the dry run shows them).
3. `a849408` — `task-cycle/skill/SKILL.md`: the script's run with `--apply` at step 4 on starting a new cycle (not on a correction), the exception in the paragraph "The cycle writes only in the task's worktree", the list of kept directories carried through steps 5 and 14, and "Keep the worktree for corrections." with its addition; `task-cycle/record_template.md` (the item *Directories of earlier tasks kept*) and `task-cycle/skill/request_template.md` (a sentence under *Cost*, a clause under *Checks*).
4. `1f27200` and `b8a16cc` — the fix of the review of the whole change: the status check reads a submodule's changes as git's own check does (the blocking finding), the retry with force waits for git's sentence about submodules, the fetch passes `--no-prune`, a failed state read gives a fixed reason with no path, a test for a junction and for the status; WAY-375 states the two rules the code applies (the task prefix or the record folder; nested copies by any name).
5. `eb5d28e` — the return step: one line of WAY-375's pair of examples kept to the part no test holds.
6. `9a6b6fa` — the fix of the failed gate: the helpers of the test run the script in a form the check of imports between parts can read; what the tests assert is unchanged.

## Checks

1. The gate on the final tree, `9a6b6fa` (`origin/foundations` had not moved from the base, so no merge): `python -B task-cycle/gate_times.py --output .runs/task-cycles/worktrees-removed-after-merge/gate_times.md -- python -B gate/run_tests.py`, run 2: exit 1; 1377 tests in 10 directories, 538.0 s, no other gate of the-way at the same time (the advisor of the day named one gate of another repository beside it); failed: the directory `gate`, one test, `test_run_tests.DirectoriesAtOnce.test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a race of the runner's own test: "did not meet the others" after 120 s); the other nine directories passed, `task-cycle` with 440 tests. Run 1, on `eb5d28e`: exit 1; 1374 tests, 458.7 s; failed: `elements/part-map`, `test_the_way_imports_only_from_allowed_parts`, `task-cycle/test_remove_merged_worktrees.py:111: runs a file the check cannot work out`, a fault of this change, fixed in `9a6b6fa` and reviewed (PASS); in run 1 the directory `gate` passed. The list of tests failing before the change was taken from the final gate of the earlier cycle, `docs/task-cycles/resolve-gaps-two-meanings/cycle.md` of commit `a398179`: none failing (exit 0, 1328 tests, every directory passed); the base `835344f` is a merge commit whose tree equals that of its second parent, so no gate ran on it. Diagnosis of the failed test, which serves the diagnosis only (WAY-243): the directory `gate` on `9a6b6fa` failed once in one run (139.5 s); the single test, run alternately on `9a6b6fa` and on a checkout of the base `835344f`, three times each: on the head pass, fail, pass; on the base pass, fail, pass; so the test fails by chance without this change; with the full gate runs, on the head the test passed in 3 and failed in 3 runs of the cycle (the `gate` directory of run 1 passed), on the base it passed in 3 and failed in 1 run of the diagnosis. No third whole gate was run to make a green run (WAY-243); the red run stands. The outputs of the diagnosis are in the record's `reports/`.
2. `python -B elements/common/foundation_check.py` on `9a6b6fa`, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line. Focused runs: `python -B -m unittest task-cycle.test_remove_merged_worktrees` 46 tests exit 0; `python -B gate/run_tests.py task-cycle` 440 tests exit 0; `python -B gate/run_tests.py elements/part-map` 39 tests exit 0; `python -B gate/run_tests.py agent-instructions` 25 tests exit 0.
3. Own-work checks: the author's, a read-only dry run of the script on the real repository of the-way compared with an independent recomputation by plain git for each of the 80 directories on a branch (80 of 80 agree), and a dry run on `loop2` (41 marked `remove`), nothing removed, the list of directories before and after the same 96 entries; 20 mutations of the script against the tests, 19 caught and one equivalent (the order of removal of nested directories makes no difference with this git); the fix's, five mutations each caught by the test written for it. The reviewer of the whole change reproduced the blocking finding in a throwaway repository, and ran its own dry run on the real repository (88 `remove`, 8 `keep`, nothing removed). What they cannot show: the script has never been run with `--apply` on a real working directory, by design.
4. Not run: no check of images (the record's copy holds none), no screenshots (the change has no screen), the whole gate was not green in any run on the final tree (Checks, 1).
5. The reviews: the whole change `FAIL a849408` then the fix `PASS b8a16cc`; the return step `PASS eb5d28e`; the fix of the gate `PASS 9a6b6fa`; the return step on the fix's range found nothing and made no commit.
6. Working copies: each agent reported where its copy stood and that it was removed (the reviewer's throwaway repositories and junctions, the author's trials, my checkout of the base for the diagnosis, `.runs/base/`); no remainder was named.
7. Directories of earlier tasks the script left standing: none to report; this cycle did not run the script. The dry run of the author lists, on the real repository, the directories that stay for your decision (the main checkout, the-way's own directory of this task, `the-way-global`, `the-way-fullrun`, a session's scratch copy, the directory of a task whose request was closed unmerged, and two loose base copies whose names do not give the task branch).
8. The form check and the check of private paths on this description, and the three checks on the copy of the record: written and checked after the record's commit.

## Foundation entries

1. WAY-298 (`row 1`) — the fast-forward, made only in the-way itself, and the removal of finished tasks' working directories that every new cycle runs at its start are the two changes the cycle makes to checkouts outside the task's worktree.
2. WAY-375 (`row 2`, `row 4`, `row 5`) — at its start a cycle removes an earlier task's working directory only when its tree is clean, all its commits are on the remote, its branch is merged (its tip is the second parent of a merge on the first-parent history of the remote target branch, by git alone) and it belongs to a cycle; it touches only checkouts git names, never a branch, and what it removes outside the repository's own directory is no effect outside the repository in the sense of WAY-140. Two wordings are the author's, accepted by the reviewer: "first-parent history", and the two rules the entry now states (a task's branch is told by the task prefix or by a record folder; nested copies go by any name).
3. WAY-376 (`row 6`) — a file git ignores does not count against a clean tree, and before the removal the script lists each directory's ignored paths outside `.runs/`, known caches left out.
4. `row 3` (the list of kept directories goes to the record and to the description by the route of WAY-373) is written into `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` and `task-cycle/skill/request_template.md`, with no entry of its own.

The new test holds ten lines `decision:` for WAY-375 and WAY-376; no invariant, its test or its surface changes and no *Violated* mark is set; the foundation check lists nothing.

## Minor findings

1. Review of the fix of the whole change (`PASS b8a16cc`), in the reviewer's words: the glossary defines a human action as an act outside the product's repository; WAY-375's second paragraph says that removing a checkout git names, "also one that stands outside the repository's own directory, ... needs no human action"; a reader who takes the glossary meaning reads that as a contradiction with the task's *Human actions* line, and the reviewer judged it a defect of the task's wording that the change carries, since the task's row 5 settles it; place: `foundations/decisions.md`, WAY-375, second paragraph.
2. Review of the return step (`PASS eb5d28e`), in the reviewer's words: WAY-375's body does not state the rule for loose base copies — a loose `base-check-*` copy goes only where the branch `task/<task>` its name gives is merged, and a copy named for no task goes only with its holding directory; the code and tests hold the rule and the entry does not contradict it; place: `foundations/decisions.md`, WAY-375.
3. Review of the return step (`PASS eb5d28e`), in the reviewer's words: "runs the script before it creates its task branch" now appears in both WAY-298's and WAY-375's pairs; the two agree, so it is harmless duplication; place: `foundations/decisions.md`, WAY-298 and WAY-375.

## Findings outside the task's scope

1. The check `test_a_number_of_jobs_limits_the_directories_that_run_at_once`, in `gate/test_run_tests.py` (part `gate`, outside this task's part), failed in run 2 of the whole gate and in two of the diagnosis runs on the head, and passed in run 1 and in four other runs; on the unchanged base it failed in one of four runs and passed in three; counts for the head: 3 passes, 3 failures; for the base: 3 passes, 1 failure. The failing run waits 120 seconds for a peer test directory to start and reports "did not meet the others".

## Course of the cycle

- **Task and sources:** the working directories of task cycles vanish after the merge of the request, and the old ones are swept; independent task, no project; sources: the task document (ready for cycle, answers given through the advisor of the day on 2026-11-14) and the foundation at `835344f`.
- **Process pin:** none; this checkout of the-way is the repository changed; base `835344f` of `foundations`; no pin moved; the gate on the final tree is in Checks, 1.
- **Spec:** none; no open design choice at the start (the task's questions carried to the cycle are choices of how to make what it settles).
- **Route:** one author without a plan, class `same`, a fix and its review after one `FAIL` of the whole change, a return step with one commit and its review, a failed gate with one fix, its review and the return step on its range, which found nothing.
- **Plan:** none.
- **Choices:** 9 entries in the questions table of the record (the route, the trust boundary, the unchanged skill file, the list of failing tests, three of the author's choices the review judged, the diagnosis of the unstable test and the decision to run no third whole gate), with the link to the table in the committed record.
- **Blocking findings left:** none.
- **Record:** written after the record's commit.
