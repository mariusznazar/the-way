**State: ready** — two items in *Fix or let through* wait for your answer; nothing else does.

## What you will see

The process now has a guide to writing a product's deployment skill, the instruction an agent reads when it prepares or checks a deployment of that product. Until now the process held only a list of what such a skill must cover and no picture of an answer; the only finished skill, the one of the game loop2, describes one small rented server, one tunnel and its own commands, so whoever took it as a model had to sort out what is general and what is loop2's.

The guide has eight parts: one for what the skill is for and how a session finds it, and one for each of the seven items of the list (the preview of deployments; where the secrets lie and how they are rotated; rollback; what the agent does and what the human does; how to read the logs; how long the record of the logs lives; how a human learns of a failure). Each part gives the questions a product answers and a short fragment showing how loop2 answered, with everything that is loop2's own marked as such. The fragments all come from one commit of loop2, which the guide links by its full SHA; the public address of the game and the sender's mail address are replaced by examples in `example.com`. For the items on the record's life and on a failure the guide also shows the human's refusal and a deliberate absence of a notice as complete answers.

The guide says outright that it binds nothing: what binds is still the list and the check of it that refinement runs. That check now names the guide in the item it adds to a task ("write or complete the deployment skill") and in the task split off for that work, and only the agent that writes such a skill reads it; refining any other task does not.

### Underneath

The rule that says what the process holds for a product's deployment skill was changed in place: beside the list it now names the guide, with loop2 as its first example, and its list of rejected ways gained the two ways the task did not choose (the guide's text written into the check itself, and the whole loop2 skill copied in).

## For you to decide

### Needed from you

none

### Fix or let through

1. Two small flaws that the last review found in the fix, and one gap it named outside the task, were left as they are. First, a paragraph in the part on what the agent does and what the human does says "A skill says what that automation does too"; read hard, that sounds like a thing every skill must do, which the guide says it never requires, and the paragraph does not say that the human's merge is what starts the automated deployment. Second, the guide marks "60 days" as loop2's own value, but it is a rule of GitHub's scheduled workflows that holds for any product, so a reader may take it for a loop2 setting. Whoever reads the guide meets them while writing a deployment skill, and neither changes a command or a number. Third, the list of what the product's directory for refinement holds and the sentence describing that part still do not name the guide; the task left that list unchanged. Fixing the first two in this request costs a correction with one fix and one more review; making a task of them leaves two wrong-sounding lines until someone writes the next skill with the guide; letting them through costs nothing today. I recommend letting the first two through, since they sit in a text that binds nothing and are short to fix whenever someone meets them, and making a task of the third, since it concerns what the list of the directory says and not this guide. Fix them in this request, make a task of them, or let them through? (Minor findings, 1 and 2; Findings outside the task's scope, 1)
2. The review of the whole change read 12 of the 79 decisions it selected for this part whole and ran through the other 67 by title only; it named as unread two decisions that lie next to the rule it checked — the one on when the step that settles technology is run, and the one on checking private paths — and did not open several groups of entries it judged not to bear on the change. If one of them says something the guide or the changed rule breaks, it would show only when someone writes the next deployment skill with the guide. A fresh reviewer reading those whole costs a short session and one more round of review; letting it through costs nothing today. I recommend letting it through, since the author read the decision on the step that settles technology whole, none of the review's findings rested on the others, and the second review of the fix found nothing new of that kind. Read them in this request, make a task of it, or let it through? (Course of the cycle, Choices)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The fragments come from the newest loop2 commit at the start of the cycle (37 commits after the one the task's note mentions), not from the commit the note names. The task asked for one commit and the skill's files are identical in both; the newer one is the state loop2 has now, and the link names it. I did not take the older one because the note named it as the state of one day, not as a requirement. (Technical changes)
4. Where the guide shows the human's refusal of an item and the deliberate absence of a failure notice, the example wording is the guide's own, labelled so, since loop2 settled both items and has no such answer. The task asked that the guide shows both as complete answers; I did not invent a loop2 fragment for them. (Technical changes)
5. In the part on what the agent does and what the human does, the guide quotes loop2's whole sentence, including its exception for deployment started by the automation the product already has, and adds one paragraph saying that such automation is a third actor next to the agent's reads and the human's changes, while what a task changes outside the repository stays the human's. The task did not ask for the paragraph; the review found the part contradicted another part of the guide without it, and I did not cut the exception from the quotation, which would have shown loop2's skill saying something it does not. (Technical changes)
6. The list does not say what "a preview of deployments" means, so the guide reads it as two things at once: seeing what runs and what a deployment did, and trying a change on the server before it reaches the main line, and says it does so. I did not read it as a separate preview environment for each branch only, since loop2 has none and the part would have no fragment. (Technical changes)

## Cost

About 38 minutes of working time and 28.8 million tokens in all, all on the sonnet model (the author on the same class as the orchestrator, since the guide's value lies in telling the general from loop2's own and a leaked address would land in a public repository). One round of review with a fix: the review of the whole change failed with two Important and four Minor findings, their one fix passed its review with two new Minor findings, and the return step changed nothing. The full gate passed on its one run (Checks). The table of stages lies in the committed record, linked under *Course of the cycle*.

## How to merge

Merge it with a merge commit that keeps the commits, since the link to the record in this description survives only then. The foundation has waited for a review through 41 merges since the tag of its last review, which stands at `foundation-review/2026-11-06`; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — dwie pozycje w sekcji „Napraw albo przepuść” czekają na Twoją odpowiedź; nic innego nie czeka.

## Co zobaczysz

Proces ma teraz przewodnik po pisaniu skilla wdrożeniowego produktu, czyli instrukcji, którą agent czyta, gdy przygotowuje albo sprawdza wdrożenie tego produktu. Dotąd proces trzymał tylko listę tego, co taki skill musi obejmować, i żadnego obrazu odpowiedzi; jedyny gotowy skill, skill gry loop2, opisuje jeden mały wynajęty serwer, jeden tunel i własne polecenia, więc kto brał go za wzór, sam musiał oddzielać to, co ogólne, od tego, co właściwe loop2.

Przewodnik ma osiem części: jedną o tym, do czego skill służy i jak sesja go znajduje, i po jednej na każdą z siedmiu pozycji listy (podgląd wdrożeń; gdzie leżą sekrety i jak się je wymienia; cofnięcie wdrożenia; co robi agent, a co człowiek; jak czytać logi; jak długo żyje zapis logów; skąd człowiek dowiaduje się o awarii). Każda część podaje pytania, na które produkt odpowiada, i krótki fragment pokazujący, jak odpowiedział loop2, z wyraźnym oznaczeniem tego, co właściwe loop2. Wszystkie fragmenty pochodzą z jednego commitu loop2, który przewodnik linkuje pełnym SHA; publiczny adres gry i adres pocztowy nadawcy są zastąpione przykładami w domenie `example.com`. Dla pozycji o życiu zapisu i o awarii przewodnik pokazuje też odmowę człowieka i świadomy brak powiadomienia jako pełne odpowiedzi.

Przewodnik mówi wprost, że niczego nie wiąże: wiąże nadal lista i sprawdzenie jej w doprecyzowaniu zadania. To sprawdzenie wskazuje teraz przewodnik w punkcie, który dodaje zadaniu („napisać albo uzupełnić skill wdrożeniowy”), i w zadaniu wydzielonym na tę pracę; czyta go tylko agent piszący taki skill, a doprecyzowanie innych zadań nie.

### Pod spodem

Reguła mówiąca, co proces trzyma dla skilla wdrożeniowego produktu, została zmieniona w miejscu: obok listy wskazuje teraz przewodnik, z loop2 jako pierwszym przykładem, a jej lista odrzuconych dróg dostała dwie drogi, których zadanie nie wybrało (treść przewodnika wpisana do samego sprawdzenia i skopiowanie całego skilla loop2).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Dwie drobne wady, które ostatnia recenzja znalazła w poprawce, i jedną lukę poza zadaniem zostawiono bez zmian. Po pierwsze, akapit w części o tym, co robi agent, a co człowiek, mówi „skill mówi też, co robi ta automatyka”; czytane na ostro brzmi to jak rzecz, którą musi robić każdy skill, a przewodnik mówi, że niczego nie wymaga, i akapit nie mówi, że to scalenie człowieka uruchamia automatyczne wdrożenie. Po drugie, przewodnik oznacza „60 dni” jako wartość właściwą loop2, a to reguła GitHuba dla zaplanowanych przepływów, która obowiązuje każdy produkt, więc czytelnik może wziąć ją za ustawienie loop2. Kto czyta przewodnik, trafi na nie przy pisaniu skilla wdrożeniowego, a żadna nie zmienia polecenia ani liczby. Po trzecie, lista tego, co trzyma katalog doprecyzowania, i zdanie opisujące tę część nadal nie wymieniają przewodnika; zadanie zostawiło tę listę bez zmian. Naprawa pierwszych dwóch w tej prośbie kosztuje poprawkę z jedną naprawą i jedną recenzją więcej; zrobienie z nich zadania zostawia dwie źle brzmiące linie, aż ktoś napisze kolejny skill z przewodnikiem; przepuszczenie nic dziś nie kosztuje. Polecam przepuścić dwie pierwsze, bo leżą w tekście, który niczego nie wiąże, i łatwo je poprawić, gdy ktoś na nie trafi, a z trzeciej zrobić zadanie, bo dotyczy tego, co mówi lista katalogu, nie tego przewodnika. Naprawić w tej prośbie, zrobić z nich zadanie, czy przepuścić? (Drobne uwagi, 1 i 2; Uwagi poza zakresem zadania, 1)
2. Recenzja całej zmiany przeczytała w całości 12 z 79 decyzji, które wybrała dla tej części, a pozostałe 67 przejrzała po samych tytułach; jako nieprzeczytane wskazała dwie decyzje leżące obok sprawdzanej reguły — o tym, kiedy uruchamia się krok rozstrzygający technologię, i o sprawdzaniu ścieżek prywatnych — i nie otwierała kilku grup wpisów, które uznała za niedotyczące zmiany. Jeśli któraś mówi coś, co przewodnik albo zmieniona reguła łamie, wyszłoby to dopiero, gdy ktoś napisze kolejny skill wdrożeniowy z przewodnikiem. Świeży recenzent czytający je w całości kosztuje krótką sesję i jeszcze jedną rundę recenzji; przepuszczenie nic dziś nie kosztuje. Polecam przepuścić, bo autor przeczytał w całości decyzję o kroku rozstrzygającym technologię, żadna uwaga recenzji nie oparła się na pozostałych, a druga recenzja poprawki nie znalazła nic nowego tego rodzaju. Przeczytać je w tej prośbie, zrobić z tego zadanie, czy przepuścić? (Przebieg cyklu, Wybory)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

3. Fragmenty pochodzą z najnowszego commitu loop2 z chwili startu cyklu (37 commitów po tym, który wymienia notatka zadania), nie z commitu z notatki. Zadanie chciało jednego commitu, a pliki skilla są w obu identyczne; nowszy to stan, jaki loop2 ma teraz, a link go nazywa. Nie wziąłem starszego, bo notatka podała go jako stan jednego dnia, nie jako wymaganie. (Zmiany techniczne)
4. Tam, gdzie przewodnik pokazuje odmowę człowieka co do pozycji i świadomy brak powiadomienia o awarii, przykładowe brzmienie jest własne przewodnika i tak oznaczone, bo loop2 rozstrzygnęło obie pozycje i nie ma takiej odpowiedzi. Zadanie chciało, żeby przewodnik pokazał obie jako pełne odpowiedzi; nie wymyślałem fragmentu loop2. (Zmiany techniczne)
5. W części o tym, co robi agent, a co człowiek, przewodnik cytuje całe zdanie loop2 razem z wyjątkiem dla wdrożenia uruchamianego przez automatykę, którą produkt już ma, i dodaje jeden akapit mówiący, że taka automatyka jest trzecim wykonawcą obok odczytów agenta i zmian człowieka, a to, co zadanie zmienia poza repozytorium, zostaje człowieka. Zadanie nie prosiło o ten akapit; recenzja stwierdziła, że bez niego część przeczyła innej części przewodnika, a wyjątku z cytatu nie wyciąłem, bo pokazałby skill loop2 mówiący to, czego nie mówi. (Zmiany techniczne)
6. Lista nie mówi, co znaczy „podgląd wdrożeń”, więc przewodnik czyta to jako dwie rzeczy naraz: zobaczenie, co działa i co zrobiło wdrożenie, oraz wypróbowanie zmiany na serwerze, zanim trafi do głównej gałęzi, i mówi, że tak robi. Nie czytałem tego jako osobnego środowiska podglądu dla każdej gałęzi, bo loop2 go nie ma i część nie miałaby fragmentu. (Zmiany techniczne)

## Koszt

Około 38 minut czasu pracy i 28,8 mln tokenów w sumie, wszystko na modelu sonnet (autor na tej samej klasie co orkiestrator, bo wartość przewodnika leży w odróżnieniu tego, co ogólne, od tego, co właściwe loop2, a wyciek adresu trafiłby do publicznego repozytorium). Jedna runda recenzji z poprawką: recenzja całej zmiany nie przeszła z dwiema uwagami ważnymi i czterema drobnymi, ich jedna poprawka przeszła recenzję z dwiema nowymi drobnymi uwagami, a krok powrotny niczego nie zmienił. Pełna bramka przeszła w jednym uruchomieniu (Sprawdzenia). Tabela etapów leży w zatwierdzonym zapisie, podlinkowana w sekcji „Przebieg cyklu”.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu w tym opisie przetrwa tylko wtedy. Fundament czeka na przegląd od 41 scaleń od tagu ostatniego przeglądu, `foundation-review/2026-11-06`; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, i nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

Two commits on top of the base `d40d1cb`: the change (`a900916`) and the fix of the review's findings (`4e60278`); the return step committed nothing.

- `project-level/task/deployment_skill_guide.md` (new, 336 lines at its first commit): parts 1 to 8 as above. Each part has the questions and a fragment; loop2's own text stands in `[loop2: …]`; the two links name `e54f23c0ea3bd1db13d2635333417eb50412d6a0`, the tip of loop2's `main` at the cycle's start, where the task's note named an earlier state (item 3). Parts 7 and 8 carry the guide's own wording for the refusal and the absent notice (item 4); part 5 quotes the whole sentence on who changes the server and adds the paragraph on the third actor (item 5); part 2 reads "a preview of deployments" as two things and says so (item 6).
- `project-level/task/skill/resolve_gaps.md`: the paragraph of the deployment check says the *To do* item it adds, and the task split off for that work, name the guide as what to read when writing the skill; the agent writing or completing a deployment skill reads it, refinement of other tasks does not; the guide binds nothing.
- `foundations/decisions.md`, the entry WAY-139 edited in place (WAY-07): the binding sentences name the guide beside the list; *Verification* gets one example of compliance and one of violation; *Rationale* says why and at what price; *Rejected* gets the ways not chosen under the task's questions 1 and 2. *Scope*, *Based on*, *Relations* and *Origin* are as they were.
- The fix `4e60278`, for the review's findings: the guide no longer says that an answer to its questions "covers the item", and part 7's two kinds of answer are examples; part 5 quotes the whole sentence; loop2's numbers and intervals are marked as loop2's; fragments keep the source order, with the section named where a sentence comes from elsewhere; the binding sentence of WAY-139 is split so the guide does not read as an eighth item of the list; the preview wording (item 6). The fix also marked "60 days" as loop2's and restored two small cuts, neither on the review's list.
- Not changed, as the task says: WAY-09 and the part map; the loop2 skill.

## Checks

- Gate on the base `d40d1cb`: not run. The base is a merge commit whose tree is identical to the tree of the head of the branch it merged (`git rev-parse` of both print `7c4593e79bded6ddc86328661a2fff920f37fb5f`); the list of tests failing before the change is taken from the final gate of that branch's cycle, `docs/task-cycles/oversized-plan-tasks/cycle.md` in the commit `0f66409`: exit 0 on its run 2 with 1271 tests in 10 directories; its run 1 failed once on `test_a_number_of_jobs_limits_the_directories_that_run_at_once` of the directory `gate` and passed on its diagnosis, so no test was failing before the change and that one is known flaky.
- Gate on the final change, head `4e60278`: `python -B task-cycle/gate_times.py --output .runs/task-cycles/deployment-skill-guide/gate_times.md -- python -B gate/run_tests.py`: exit 0, 1271 tests in 10 directories, every directory passed; one run, no failure. The remote target branch had not moved (`d40d1cb`), so no merge was made.
- Own-work checks: the author ran `python -B elements/common/foundation_check.py` (exit 0, 0 errors), `python -B -m unittest discover -s project-level -p "test_*.py"` (exit 0, 275 tests, on each of its two heads), `python -B task-cycle/private_paths_check.py` on the guide and the step (exit 0, 0 listed), `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (exit 0, 298 files, 0 listed) and a search of the committed text for the real game address and the sender's mailbox domain (none found); the author's script comparing each quotation with the loop2 files at the commit left differences it explained (the guide's own wording, a table kept in part, one command cut by the script's own limit, the adaptation of the copy of a secret); the review found the cut clause the script did not (fixed). The reviewers repeated the foundation check, the private-path checks and the part's tests (exit 0, 275 tests) and the search for the two strings (none), and read both links (HTTP 200; the repository is public). The return step changed no file and ran no test.
- User-interface states and screenshots: not applicable, no screen changed.
- The form check, the check of private paths on this description and on the copy of the record, the image check and the remarks check on the original and on the copy: last runs filled in after the record's commit.

## Foundation entries

1. WAY-139 (`row 1` and `row 2`): beside the list of what a product's deployment skill covers, the-way holds a guide to writing such a skill with loop2's as its first example, which binds nothing and which the check of the list points to from the item it adds; the guide shows loop2 by fragments of one commit, with a link to it and what is loop2's own marked, and shows no real address of the game and no sender mailbox address, only addresses in `example.com`.

No other decision, invariant, environment fact, glossary term or part-map entry is written or changed; no kept row tied to an entry already stated.

## Minor findings

1. From the review of the fix, new, not fixed (`project-level/task/deployment_skill_guide.md:226-229`): "The paragraph on the third actor puts two statements side by side without saying how they fit. … "A skill says… too" can be read as a thing a skill must do, which WAY-139's *Verification* lists as a violation when the guide stands as a condition (`decisions.md:3918-3919`); in context (the paragraph describes what loop2's sentence names) the reading is possible but not the natural one, hence Minor. (b) The deployment of a merged commit is an effect outside the repository and the paragraph does not say that it is the human's merge that sets it off, so a reader still has to reconcile it with WAY-140 alone. Fix direction: "A skill names that automation too" and one clause on the human's merge starting it."
2. From the review of the fix, new, not fixed (`project-level/task/deployment_skill_guide.md:343`): ""60 days" is marked as loop2's, but it is GitHub's rule. … ("GitHub disables a scheduled workflow after [loop2: 60 days]"). The source sentence states a rule of GitHub's scheduled workflows; it holds for any product that uses them, which is what a reader of the guide would want to know. The marker tells the reader it is loop2's own value. The author reports this as a mark beyond my list. Fix: take the marker off."

## Findings outside the task's scope

1. `foundations/decisions.md:238-240` (WAY-09's list for `project-level/`) and `foundations/part_map.md:77-83`, from the review of the whole change: "WAY-09 and the part-map sentence of `project-level` do not name a guide. … The file lies in `project-level/`, which the invariant `repository-file-location` allows, and WAY-139 itself has Scope `project-level`; but the part-map sentence gives refinement of a task as the part's reach, while the guide is read by the agent that writes the skill in the cycle. The task says WAY-09 stays unchanged, so this is outside the task; whether a word is worth adding is for the human."

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes (frozen copy `task.md` in the record), settlements accepted on 2026-11-14; sources: the check of the deployment list in `resolve_gaps.md`, the decision log at `d40d1cb`, and the public loop2 skill at `e54f23c0ea3bd1db13d2635333417eb50412d6a0`.
- **Process pin:** none, this is the-way itself; the gate on the base is in *Checks*.
- **Spec:** none, both rows of the task's settlements settle where the guide lies, how it is reached and how loop2 is shown; the file name and wording are the writer's.
- **Route:** one author without a plan, on the same class as the orchestrator (sonnet), since the guide is judgment prose and a leaked real address would enter a public repository.
- **Plan:** none.
- **Choices:** 6 rows in the questions table of the record: the loop2 commit (item 3), the author's class, the reading gap of the first report, the guide's own wording for refusal and absent notice (item 4), the paragraph on the third actor (item 5), the reading of "a preview of deployments" (item 6); the review's reading gap is item 2.
- **Blocking findings left:** none.
- **Record:** pending, the link is added after the record's commit.
