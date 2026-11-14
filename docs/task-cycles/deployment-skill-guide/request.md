**State: ready** — corrected for your remarks; one item in *Fix or let through* asks only whether to make a task of it.

## What you will see

The process now has a guide to writing a product's deployment skill, the instruction an agent reads when it prepares or checks a deployment of that product. Until now the process held only a list of what such a skill must cover and no picture of an answer; the only finished skill, the one of the game loop2, describes one small rented server, one tunnel and its own commands, so whoever took it as a model had to sort out what is general and what is loop2's.

The guide has eight parts: one for what the skill is for and how a session finds it, and one for each of the seven items of the list (the preview of deployments; where the secrets lie and how they are rotated; rollback; what the agent does and what the human does; how to read the logs; how long the record of the logs lives; how a human learns of a failure). Each part gives the questions a product answers and a short fragment showing how loop2 answered, with everything that is loop2's own marked as such. The fragments all come from one commit of loop2, which the guide links by its full SHA; the public address of the game and the sender's mail address are replaced by examples in `example.com`. For the items on the record's life and on a failure the guide also shows the human's refusal and a deliberate absence of a notice as complete answers.

The guide says outright that it binds nothing: what binds is still the list and the check of it that refinement runs. That check now names the guide in the item it adds to a task ("write or complete the deployment skill") and in the task split off for that work, and only the agent that writes such a skill reads it; refining any other task does not.

After your remarks, the paragraph on the automation a product already has now says that a person's merge is what starts the automated deployment, and "60 days", which is a rule of GitHub's scheduled workflows and not a setting of loop2, no longer carries the mark of loop2's own text.

### Underneath

The rule that says what the process holds for a product's deployment skill was changed in place: beside the list it now names the guide, with loop2 as its first example, and its list of rejected ways gained the two ways the task did not choose (the guide's text written into the check itself, and the whole loop2 skill copied in).

## For you to decide

### Needed from you

none

### Fix or let through

1. The step that checks the list adds a *To do* item for a missing deployment skill and points that item, and the task split off for it, to the guide. For the three items the step handles apart (how to read the logs, how long the record lives, how a human learns of a failure) it also adds *To do* items that write an answer into the skill, and its text does not say that those items point to the guide too, though the guide's parts 6, 7 and 8 are about exactly those cases. Someone completing the skill for one of those three items may therefore not be sent to the guide; it is reached in every flow where the skill is missing altogether, and the effect is a missed pointer, not a wrong instruction. Making a task of it costs one small edit of the step and the decision later; letting it through costs nothing today. I recommend making a task of it, since the pointer is the one thing the guide is for. Make a task of it? (Minor findings, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The fragments come from the newest loop2 commit at the start of the cycle (37 commits after the one the task's note mentions), not from the commit the note names. The task asked for one commit and the skill's files are identical in both; the newer one is the state loop2 has now, and the link names it. I did not take the older one because the note named it as the state of one day, not as a requirement. (Technical changes)
3. Where the guide shows the human's refusal of an item and the deliberate absence of a failure notice, the example wording is the guide's own, labelled so, since loop2 settled both items and has no such answer. The task asked that the guide shows both as complete answers; I did not invent a loop2 fragment for them. (Technical changes)
4. In the part on what the agent does and what the human does, the guide quotes loop2's whole sentence, including its exception for deployment started by the automation the product already has, and adds one paragraph saying that such automation is a third actor next to the agent's reads and the human's changes, and that the human's merge is what starts it, while what a task changes outside the repository stays the human's. The task did not ask for the paragraph; the review found the part contradicted another part of the guide without it, and I did not cut the exception from the quotation, which would have shown loop2's skill saying something it does not. (Technical changes)
5. The list does not say what "a preview of deployments" means, so the guide reads it as two things at once: seeing what runs and what a deployment did, and trying a change on the server before it reaches the main line, and says it does so. I did not read it as a separate preview environment for each branch only, since loop2 has none and the part would have no fragment. (Technical changes)
6. This correction answered your answer to the item on the two small flaws of the guide, and the cycle judged that neither the task nor the foundation required what it changed.

## Cost

About 59 minutes of working time and 46.8 million tokens in all, all on the sonnet model (the author on the same class as the orchestrator, since the guide's value lies in telling the general from loop2's own and a leaked address would land in a public repository). Four rounds of review: the review of the whole change failed with two Important and four Minor findings, their one fix passed its review, the correction for your remarks passed its review, and the merge with the target branch, which moved twice during the correction, was reviewed once (passed); the return step changed nothing. The full gate passed on two runs and failed once on a timing test of its own directory (Checks). The table of stages lies in the committed record, linked under *Course of the cycle*.

## How to merge

Merge it with a merge commit that keeps the commits, since the link to the record in this description survives only then. The foundation has waited for a review through 43 merges since the tag of its last review, which stands at `foundation-review/2026-11-06`; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — poprawione po Twoich uwagach; jedna pozycja w sekcji „Napraw albo przepuść” pyta tylko, czy zrobić z niej zadanie.

## Co zobaczysz

Proces ma teraz przewodnik po pisaniu skilla wdrożeniowego produktu, czyli instrukcji, którą agent czyta, gdy przygotowuje albo sprawdza wdrożenie tego produktu. Dotąd proces trzymał tylko listę tego, co taki skill musi obejmować, i żadnego obrazu odpowiedzi; jedyny gotowy skill, skill gry loop2, opisuje jeden mały wynajęty serwer, jeden tunel i własne polecenia, więc kto brał go za wzór, sam musiał oddzielać to, co ogólne, od tego, co właściwe loop2.

Przewodnik ma osiem części: jedną o tym, do czego skill służy i jak sesja go znajduje, i po jednej na każdą z siedmiu pozycji listy (podgląd wdrożeń; gdzie leżą sekrety i jak się je wymienia; cofnięcie wdrożenia; co robi agent, a co człowiek; jak czytać logi; jak długo żyje zapis logów; skąd człowiek dowiaduje się o awarii). Każda część podaje pytania, na które produkt odpowiada, i krótki fragment pokazujący, jak odpowiedział loop2, z wyraźnym oznaczeniem tego, co właściwe loop2. Wszystkie fragmenty pochodzą z jednego commitu loop2, który przewodnik linkuje pełnym SHA; publiczny adres gry i adres pocztowy nadawcy są zastąpione przykładami w domenie `example.com`. Dla pozycji o życiu zapisu i o awarii przewodnik pokazuje też odmowę człowieka i świadomy brak powiadomienia jako pełne odpowiedzi.

Przewodnik mówi wprost, że niczego nie wiąże: wiąże nadal lista i sprawdzenie jej w doprecyzowaniu zadania. To sprawdzenie wskazuje teraz przewodnik w punkcie, który dodaje zadaniu („napisać albo uzupełnić skill wdrożeniowy”), i w zadaniu wydzielonym na tę pracę; czyta go tylko agent piszący taki skill, a doprecyzowanie innych zadań nie.

Po Twoich uwagach akapit o automatyce, którą produkt już ma, mówi teraz, że to scalenie człowieka uruchamia automatyczne wdrożenie, a „60 dni”, które jest regułą zaplanowanych przepływów GitHuba, a nie ustawieniem loop2, nie nosi już oznaczenia tekstu właściwego loop2.

### Pod spodem

Reguła mówiąca, co proces trzyma dla skilla wdrożeniowego produktu, została zmieniona w miejscu: obok listy wskazuje teraz przewodnik, z loop2 jako pierwszym przykładem, a jej lista odrzuconych dróg dostała dwie drogi, których zadanie nie wybrało (treść przewodnika wpisana do samego sprawdzenia i skopiowanie całego skilla loop2).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Krok, który sprawdza listę, dodaje punkt *Do zrobienia* dla brakującego skilla wdrożeniowego i kieruje ten punkt oraz zadanie z niego wydzielone do przewodnika. Dla trzech pozycji, które krok obsługuje osobno (jak czytać logi, jak długo żyje zapis, skąd człowiek dowiaduje się o awarii), dodaje też punkty, które wpisują odpowiedź do skilla, a jego tekst nie mówi, że te punkty też kierują do przewodnika, choć części 6, 7 i 8 przewodnika dotyczą dokładnie tych przypadków. Kto uzupełnia skill dla jednej z tych trzech pozycji, może więc nie zostać skierowany do przewodnika; trafia do niego w każdym przepływie, gdzie skilla brakuje w ogóle, a skutkiem jest pominięte wskazanie, nie błędna instrukcja. Zrobienie z tego zadania kosztuje jedną małą zmianę kroku i decyzji później; przepuszczenie nic dziś nie kosztuje. Polecam zrobić z tego zadanie, bo wskazanie to jedyna rzecz, do czego przewodnik służy. Zrobić z tego zadanie? (Drobne uwagi, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Fragmenty pochodzą z najnowszego commitu loop2 z chwili startu cyklu (37 commitów po tym, który wymienia notatka zadania), nie z commitu z notatki. Zadanie chciało jednego commitu, a pliki skilla są w obu identyczne; nowszy to stan, jaki loop2 ma teraz, a link go nazywa. Nie wziąłem starszego, bo notatka podała go jako stan jednego dnia, nie jako wymaganie. (Zmiany techniczne)
3. Tam, gdzie przewodnik pokazuje odmowę człowieka co do pozycji i świadomy brak powiadomienia o awarii, przykładowe brzmienie jest własne przewodnika i tak oznaczone, bo loop2 rozstrzygnęło obie pozycje i nie ma takiej odpowiedzi. Zadanie chciało, żeby przewodnik pokazał obie jako pełne odpowiedzi; nie wymyślałem fragmentu loop2. (Zmiany techniczne)
4. W części o tym, co robi agent, a co człowiek, przewodnik cytuje całe zdanie loop2 razem z wyjątkiem dla wdrożenia uruchamianego przez automatykę, którą produkt już ma, i dodaje jeden akapit mówiący, że taka automatyka jest trzecim wykonawcą obok odczytów agenta i zmian człowieka, a uruchamia ją scalenie człowieka, podczas gdy to, co zadanie zmienia poza repozytorium, zostaje człowieka. Zadanie nie prosiło o ten akapit; recenzja stwierdziła, że bez niego część przeczyła innej części przewodnika, a wyjątku z cytatu nie wyciąłem, bo pokazałby skill loop2 mówiący to, czego nie mówi. (Zmiany techniczne)
5. Lista nie mówi, co znaczy „podgląd wdrożeń”, więc przewodnik czyta to jako dwie rzeczy naraz: zobaczenie, co działa i co zrobiło wdrożenie, oraz wypróbowanie zmiany na serwerze, zanim trafi do głównej gałęzi, i mówi, że tak robi. Nie czytałem tego jako osobnego środowiska podglądu dla każdej gałęzi, bo loop2 go nie ma i część nie miałaby fragmentu. (Zmiany techniczne)
6. Ta korekta odpowiedziała na Twoją odpowiedź do pozycji o dwóch drobnych wadach przewodnika, a cykl uznał, że ani zadanie, ani fundament nie wymagały tego, co zmieniła.

## Koszt

Około 59 minut czasu pracy i 46,8 mln tokenów w sumie, wszystko na modelu sonnet (autor na tej samej klasie co orkiestrator, bo wartość przewodnika leży w odróżnieniu tego, co ogólne, od tego, co właściwe loop2, a wyciek adresu trafiłby do publicznego repozytorium). Cztery rundy recenzji: recenzja całej zmiany nie przeszła z dwiema uwagami ważnymi i czterema drobnymi, ich jedna poprawka przeszła recenzję, korekta po Twoich uwagach przeszła recenzję, a scalenie z gałęzią docelową, która w czasie korekty ruszyła dwa razy, zrecenzowano raz (przeszło); krok powrotny niczego nie zmienił. Pełna bramka przeszła w dwóch uruchomieniach i raz padła na teście czasowym własnego katalogu (Sprawdzenia). Tabela etapów leży w zatwierdzonym zapisie, podlinkowana w sekcji „Przebieg cyklu”.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu w tym opisie przetrwa tylko wtedy. Fundament czeka na przegląd od 43 scaleń od tagu ostatniego przeglądu, `foundation-review/2026-11-06`; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, i nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

Base `d40d1cb`; the target branch `foundations` moved to `0e1cd3c` and then to `0b77f5a` during the correction, and both were merged into the task branch (`dc18abf`, `dd91dd2`, no conflict). Commits of the change: the change (`a900916`), the fix of the review's findings (`4e60278`) and the correction for your remarks (`aa21be7`); the record's two pairs of commits only add and remove the record.

- `project-level/task/deployment_skill_guide.md` (new, 352 lines): parts 1 to 8 as above. Each part has the questions and a fragment; loop2's own text stands in `[loop2: …]`; the two links name `e54f23c0ea3bd1db13d2635333417eb50412d6a0`, the tip of loop2's `main` at the cycle's start, where the task's note named an earlier state (item 2). Parts 7 and 8 carry the guide's own wording for the refusal and the absent notice (item 3); part 5 quotes the whole sentence on who changes the server and adds the paragraph on the third actor (item 4); part 2 reads "a preview of deployments" as two things and says so (item 5).
- `project-level/task/skill/resolve_gaps.md`: the paragraph of the deployment check says the *To do* item it adds, and the task split off for that work, name the guide as what to read when writing the skill; the agent writing or completing a deployment skill reads it, refinement of other tasks does not; the guide binds nothing.
- `foundations/decisions.md`, the entry WAY-139 edited in place (WAY-07): the binding sentences name the guide beside the list; *Verification* gets one example of compliance and one of violation; *Rationale* says why and at what price; *Rejected* gets the ways not chosen under the task's questions 1 and 2. *Scope*, *Based on*, *Relations* and *Origin* are as they were.
- The fix `4e60278`: the guide no longer says that an answer to its questions "covers the item", and part 7's two kinds of answer are examples; part 5 quotes the whole sentence; loop2's numbers and intervals are marked as loop2's; fragments keep the source order, with the section named where a sentence comes from elsewhere; the binding sentence of WAY-139 is split so the guide does not read as an eighth item of the list; the preview wording.
- The correction `aa21be7`, for your remarks, in the guide only: part 5 now reads "A skill names that automation too, and the human's merge is what starts the automated deployment", and "60 days" no longer carries the loop2 mark.
- Not changed, as the task and your remarks say: WAY-09 and the part map (a task is made of it apart from this request); the loop2 skill.

## Checks

- Gate on the base `d40d1cb`: not run. The base is a merge commit whose tree is identical to the tree of the head of the branch it merged (`git rev-parse` of both print `7c4593e79bded6ddc86328661a2fff920f37fb5f`); the list of tests failing before the change is taken from the final gate of that branch's cycle, `docs/task-cycles/oversized-plan-tasks/cycle.md` in the commit `0f66409`: exit 0 on its run 2 with 1271 tests in 10 directories; its run 1 failed once on `test_a_number_of_jobs_limits_the_directories_that_run_at_once` of the directory `gate` and passed on its diagnosis, so no test was failing before the change and that one is known flaky.
- Gate on the final tree, head `dd91dd2`: `python -B task-cycle/gate_times.py --output .runs/task-cycles/deployment-skill-guide/gate_times.md -- python -B gate/run_tests.py --jobs 4`: exit 1, 1331 tests in 10 directories; the directory `gate` failed on `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a trial directory did not meet the others within 120 seconds). `python -B gate/run_tests.py gate` alone on the same tree: exit 0, 36 tests in 18 seconds (diagnosis only, WAY-243). The same test failed in run 1 of the gate of the cycle that gave the list above. Across this correction's three gate runs, on `aa21be7` (exit 0, 1271 tests), on the first merged tree `dc18abf` (exit 0, 1326 tests) and on `dd91dd2`, it failed in 1 and passed in 2; the first gate before the correction, on `4e60278`, also passed (exit 0, 1271 tests). The second merge changed no file of this change, so the last green run on the change's own files is the one on `dc18abf`; no further gate run was made to make the last one pass.
- Own-work checks: the author ran `python -B elements/common/foundation_check.py` (exit 0, 0 errors), `python -B -m unittest discover -s project-level -p "test_*.py"` (exit 0, 275 tests, on each of its heads), `python -B task-cycle/private_paths_check.py` on the guide and the step (exit 0, 0 listed), `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (exit 0, 298 files, 0 listed) and a search of the committed text for the real game address and the sender's mailbox domain (none found); the review of the whole change found a cut clause that the author's script comparing quotations with loop2 had explained away (fixed). The reviewers repeated the foundation check and the private-path checks (exit 0) and the search for the two strings (none) and read both links (HTTP 200; the repository is public). The part's tests ran exit 0, 275 tests, run by the orchestrator alone on the correction head, since the reviewer's own run of them was lost without a result. After the merges the orchestrator ran `python -B elements/common/foundation_check.py` without `--skip-test-citations` on the final tree: exit 0, 0 errors, no listed invariant.
- User-interface states and screenshots: not applicable, no screen changed.
- The form check, the check of private paths on this description and on the copy of the record, the image check and the remarks check on the original and on the copy: last runs filled in after the record's commit.

## Foundation entries

1. WAY-139 (`row 1` and `row 2`): beside the list of what a product's deployment skill covers, the-way holds a guide to writing such a skill with loop2's as its first example, which binds nothing and which the check of the list points to from the item it adds; the guide shows loop2 by fragments of one commit, with a link to it and what is loop2's own marked, and shows no real address of the game and no sender mailbox address, only addresses in `example.com`.

No other decision, invariant, environment fact, glossary term or part-map entry is written or changed; no kept row tied to an entry already stated. No test holds a sentence of WAY-139 by a line `decision:`, and the foundation check lists no invariant for a corrected sentence.

## Minor findings

1. From the review of the merge with the target branch, not fixed (`project-level/task/skill/resolve_gaps.md:64-67` against the binding sentences of WAY-139): "The three items the check handles apart (logs reading, record's life, failure notice; `resolve_gaps.md:71-96`) also add *To do* items that write or record an answer in the skill, and the bullets do not say that those items name the guide too; WAY-139's text ("that item and that task point to the guide") reads the same way, so the two files agree with each other. A reader could take an agent that completes the skill for one of those three items as not pointed to the guide, though the guide's parts 6, 7 and 8 show exactly those cases. Not caused by the merge (it stood at `aa21be7` and passed two reviews); task *To do* 2 says the point item and the split task name the guide, which both files do. Kept Minor: no sentence a reader would read wrongly was found, the guide is reachable from the first item or the split task in every flow where the skill is missing, and the item for a single missing list entry is covered by "an item is missing"." (item 1 of *Fix or let through*)
2. From the review of the merge with the target branch, not fixed (`foundations/decisions.md:4001` and `:4030`): "the lines the change reflowed in WAY-139 are left over the width of the lines around them: line 4001 ("logs, on the record's life and on a failure, the check quotes the answer a decision of the foundation or an", 107 chars) in the binding sentences, and line 4030 ("without the check; the item that a check adds for a missing deployment skill points to the guide,", 101 chars) in *Verification*. Cosmetic only: no rule of the template or of `foundation_check.py` sets a width (the check reports 0 errors), and the entry's meaning is unaffected."

The two Minor findings of the fix's review (the third-actor paragraph's wording and the "60 days" mark) were fixed by the correction and are no longer unfixed.

## Findings outside the task's scope

1. `foundations/decisions.md` (the list WAY-09 gives for `project-level/`) and `foundations/part_map.md` (the sentence of the part `project-level`), from the review of the whole change: "WAY-09 and the part-map sentence of `project-level` do not name a guide. … The file lies in `project-level/`, which the invariant `repository-file-location` allows, and WAY-139 itself has Scope `project-level`; but the part-map sentence gives refinement of a task as the part's reach, while the guide is read by the agent that writes the skill in the cycle. The task says WAY-09 stays unchanged, so this is outside the task; whether a word is worth adding is for the human." You answered to make a task of it, saved through the park skill after this correction, not in this request.
2. `gate/test_run_tests.py`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a check of the part `gate`, outside the task's parts): failed in 1 of this correction's 3 full gate runs and in the earlier cycle's run 1, and passed in the others and in the run of its directory alone (36 tests, exit 0); the cause is unproven, a trial directory did not meet the others within 120 seconds while the directories ran at once.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes (frozen copy `task.md` in the record), settlements accepted on 2026-11-14; sources: the check of the deployment list in `resolve_gaps.md`, the decision log at `d40d1cb`, and the public loop2 skill at `e54f23c0ea3bd1db13d2635333417eb50412d6a0`.
- **Process pin:** none, this is the-way itself; the gate on the base is in *Checks*.
- **Spec:** none, both rows of the task's settlements settle where the guide lies, how it is reached and how loop2 is shown; the file name and wording are the writer's.
- **Route:** one author without a plan, on the same class as the orchestrator (sonnet), since the guide is judgment prose and a leaked real address would enter a public repository. Correction 1 ran on the same route; its remarks are in the record.
- **Plan:** none.
- **Choices:** 9 rows in the questions table of the record: the loop2 commit (item 2), the author's class, the reading gap of the first report, the guide's own wording for refusal and absent notice (item 3), the paragraph on the third actor (item 4), the reading of "a preview of deployments" (item 5), and, for the correction, the return step not repeated, the second merge not reviewed separately and the gate run with `--jobs 4`.
- **Blocking findings left:** none.
- **Record:** pending, the link is added after the record's commit.
