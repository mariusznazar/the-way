**State: ready** — the change is reviewed and tested; seven items below wait for your yes.

## What you will see

Four small fixes to how the process works, all taken from remarks that earlier task cycles left behind.

- A decision no longer names a task note in its *Origin* field, wherever the product keeps its tasks. Whatever such a note carried of the reasoning goes into the decision's own rationale and rejected options, and *Origin* then reads `none`. Tasks are where work is found, never a source a decision points to.
- A task cycle now runs the product's full tests once, after the return step and its review, on the tree they leave. Before, it ran them first and again after the return step changed something. A second run happens only where merging the target branch changed the tree, or where the tests fail and the fix changes code (then the return step looks at that fix as well). For a product like loop2 this saves about 35 minutes per task.
- The script that checks that the doubts stage reports end with reach the cycle's process remarks now also recognises a section heading with a number in front, such as `## 12. Searches not found or unclear`. Before, such a doubt could vanish without a trace.
- A missing fact an invariant rests on can stand on the main branch as `TODO — <the fact, with its source>`. The foundation check reads that whole, commas included, and reports a bare `TODO` as an error with a hint to name the fact. The rules, the invariants template and the request template say the same, and every request now shows you such a gap.

### Underneath

Two decisions are edited in place (how the cycle runs the gate, and what a foundation entry's fields may hold) and a third one that lists what this section holds gets one added case. The request template gains item 15 of its numbered list of what this section holds, and the cycle skill, the decision template, the rules shared by the elements, and the two scripts with their tests change as described above.

## For you to decide

1. **Which missing-fact markers a request shows you.** The task said a request shows each descriptive `TODO` in an invariant's *Rests on* "that the change leaves on the main branch", and left to the cycle in which point of this section it stands. The cycle put it here as a numbered item and read "leaves" wide: every such marker on the tree after the change, whether the change wrote it, kept it or did not remove it. The narrow reading (only in entries the change edits) was tried first and the reviewer found it contradicted the decisions the task asks for. Price: while an old gap stands, every request carries one such item; today the-way has none. Accept? (Foundation entries, 3)
2. **Two places in the cycle skill outside the task's list.** Because the full tests now wait for the return step, the cases that run them with no return step before them (a request blocked by a review finding, a slice that failed twice) now say "at once", and so does the run at a pin move. Without it, those cases would be told to wait for a step that does not run on that code. Accept? (Technical changes, 2)
3. **A rule that stands only in the cycle skill.** "Where the gate fails and its fix changes code, the return step compares that fix's range too" is written in the cycle skill, where the task puts it, and in no decision. The reviewer saw that a later edit of the skill could drop it without contradicting any entry. Putting it into the decision's example sentence would depart from the sentence the task gives word for word, so the cycle left it. Accept? (Course of the cycle, Choices)
4. **The decision on how the cycle runs the gate (the cycle's entry).** The gate runs once, on the tree the return step and its review leave, and again only where the merge with the target branch changed it. Its reasoning and the rejected way (rerunning only the checks that read the foundation, since the process does not know which checks of a product do) are added. Accept? (Foundation entries, 1)
5. **The decision on what a foundation entry's fields may hold (the cycle's entry).** The main branch may hold `TODO` only in an invariant's *Rests on*, as `TODO — <the fact, with its source>`, and a change that leaves one there puts it before you. The reasoning is rewritten, since it no longer waits for the environment facts to have entries; two rejected ways are added. Accept? (Foundation entries, 2)
6. **The decision on what this section holds (the cycle's entry).** It now also holds each descriptive `TODO` in an invariant's *Rests on* that stands on the main branch after the merge, with a compliant and a violating example; the task did not list this decision, but the new item would contradict it otherwise. Accept? (Foundation entries, 3)
7. **Two leftovers of the review that change approved decisions.** (a) One decision's example still shows a decision whose source is silent reading `Based on: TODO — <what is missing>`, although its rule now allows `TODO` only in an invariant's *Rests on*; the foundation check also still lets *Based on* read `TODO`. A decision written by that example may leave a gap in the wrong field. (b) That decision's scope does not name the cycle's part, so a cycle that selects decisions by that part to change the request template will not find it. Both were there before this change; whether *Based on* may read `TODO` is yours to decide. Fix it in this request, or make a task of it? (Findings outside the task's scope, 1 and 2)

## Cost

About 36 minutes of working time across the orchestrator and six agent turns, on one model (Sonnet 5.5), 34.1 million tokens, of which 32.9 million were cached input. One review round blocked: the review of the whole change failed on one finding, the author made one fix, and the same reviewer passed it. The reviewer was also sent back once to finish reading the decisions it had selected. The table of stages is in the committed record: RECORD_STAGES_LINK.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation is not due for a review: 19 merges since the last one, the threshold is 30.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — zmiana jest zrecenzowana i przetestowana; siedem punktów poniżej czeka na Twoje „tak”.

## Co zobaczysz

Cztery drobne poprawki w tym, jak działa proces; wszystkie wzięte z uwag, które zostawiły wcześniejsze cykle zadań.

- Decyzja nie wskazuje już w polu *Origin* notatki zadania, bez względu na to, gdzie produkt trzyma zadania. To, co taka notatka niosła z uzasadnienia, idzie do uzasadnienia decyzji i do jej odrzuconych wariantów, a *Origin* brzmi wtedy `none`. Zadania służą do znajdowania pracy, nigdy nie są źródłem, na które wskazuje decyzja.
- Cykl zadania puszcza teraz pełne testy produktu raz, po kroku powrotu i jego przeglądzie, na drzewie, które zostawiają. Wcześniej puszczał je najpierw i jeszcze raz, gdy krok powrotu coś zmienił. Drugi przebieg jest tylko wtedy, gdy scalenie gałęzi docelowej zmieniło drzewo albo gdy testy padną, a poprawka zmieni kod (wtedy krok powrotu patrzy też na tę poprawkę). W produkcie takim jak loop2 to ok. 35 minut oszczędności na zadanie.
- Skrypt, który pilnuje, żeby wątpliwości z końca raportów etapów trafiły do uwag procesowych cyklu, rozpoznaje teraz także nagłówek sekcji z numerem na początku, np. `## 12. Searches not found or unclear`. Wcześniej taka wątpliwość mogła przepaść bez śladu.
- Brakujący fakt, na którym stoi niezmiennik, może stać na gałęzi głównej jako `TODO — <fakt i jego źródło>`. Sprawdzanie fundamentu czyta to w całości, z przecinkami, a samo `TODO` zgłasza jako błąd z podpowiedzią, żeby nazwać fakt. Reguły, szablon niezmienników i szablon opisu PR-a mówią to samo, a każdy PR pokazuje Ci taką lukę.

### Pod spodem

Dwie decyzje są poprawione w miejscu (jak cykl puszcza bramkę i co mogą zawierać pola wpisu fundamentu), a trzecia, która wylicza, co zawiera ta sekcja, dostaje jeden dodany przypadek. Szablon opisu PR-a dostaje punkt 15 numerowanej listy, a skill cyklu, szablon decyzji, reguły wspólne dla elementów i dwa skrypty z testami zmieniają się jak wyżej.

## Do Twojej decyzji

1. **Które znaczniki brakującego faktu pokazuje PR.** Zadanie kazało pokazać każde opisowe `TODO` w *Rests on* niezmiennika, „które zmiana zostawia na gałęzi głównej”, i zostawiło cyklowi wybór miejsca w tej sekcji. Cykl umieścił to tu jako punkt listy i odczytał „zostawia” szeroko: każdy taki znacznik na drzewie po zmianie, niezależnie od tego, czy zmiana go napisała, zachowała, czy tylko nie usunęła. Wąskie odczytanie (tylko w wpisach, które zmiana edytuje) cykl wypróbował najpierw, ale recenzent uznał je za sprzeczne z decyzjami, o które prosi zadanie. Cena: dopóki stoi stara luka, każdy PR niesie taki punkt; dziś the-way nie ma żadnej. Akceptujesz? (Foundation entries, 3)
2. **Dwa miejsca w skillu cyklu poza listą zadania.** Skoro pełne testy czekają teraz na krok powrotu, przypadki, które puszczają je bez kroku powrotu przed nimi (PR zablokowany uwagą z przeglądu, wycinek, który zawiódł dwa razy), mówią teraz „od razu”, tak samo jak przebieg przy zmianie wersji procesu. Bez tego te przypadki miałyby czekać na krok, który na tym kodzie się nie odbywa. Akceptujesz? (Technical changes, 2)
3. **Reguła, która stoi tylko w skillu cyklu.** „Gdy bramka padnie, a jej poprawka zmieni kod, krok powrotu porównuje też zakres tej poprawki” jest zapisane w skillu cyklu, gdzie umieszcza to zadanie, a w żadnej decyzji. Recenzent zauważył, że późniejsza edycja skilla mogłaby to usunąć bez sprzeczności z jakimkolwiek wpisem. Wpisanie tego do zdania przykładu decyzji odeszłoby od zdania, które zadanie podaje słowo w słowo, więc cykl tego nie zrobił. Akceptujesz? (Course of the cycle, Choices)
4. **Decyzja o tym, jak cykl puszcza bramkę (wpis cyklu).** Bramka idzie raz, na drzewie zostawionym przez krok powrotu i jego przegląd, a drugi raz tylko tam, gdzie scalenie z gałęzią docelową zmieniło drzewo. Dodane są jej uzasadnienie i odrzucony wariant (ponawianie tylko sprawdzeń czytających fundament, bo proces nie wie, które sprawdzenia produktu to robią). Akceptujesz? (Foundation entries, 1)
5. **Decyzja o tym, co mogą zawierać pola wpisu fundamentu (wpis cyklu).** Gałąź główna może mieć `TODO` tylko w *Rests on* niezmiennika, w postaci `TODO — <fakt i jego źródło>`, a zmiana, która je zostawia, pokazuje to Tobie. Uzasadnienie jest napisane od nowa, bo nie czeka już na to, aż fakty środowiska będą miały wpisy; dodane są dwa odrzucone warianty. Akceptujesz? (Foundation entries, 2)
6. **Decyzja o tym, co zawiera ta sekcja (wpis cyklu).** Zawiera teraz także każde opisowe `TODO` w *Rests on* niezmiennika, które stoi na gałęzi głównej po scaleniu, z przykładem zgodnym i niezgodnym; zadanie nie wymieniało tej decyzji, ale nowy punkt bez tego byłby z nią sprzeczny. Akceptujesz? (Foundation entries, 3)
7. **Dwie pozostałości przeglądu, które zmieniają przyjęte decyzje.** (a) Przykład jednej decyzji nadal pokazuje decyzję, której źródło milczy, z `Based on: TODO — <czego brakuje>`, choć jej reguła dopuszcza teraz `TODO` tylko w *Rests on* niezmiennika; sprawdzanie fundamentu też nadal pozwala *Based on* brzmieć `TODO`. Decyzja pisana według tego przykładu może zostawić lukę w złym polu. (b) Zakres tej decyzji nie wymienia części cyklu, więc cykl, który dobiera decyzje po tej części przy zmianie szablonu opisu PR-a, jej nie znajdzie. Oba były przed tą zmianą; czy *Based on* może brzmieć `TODO`, rozstrzygasz Ty. Poprawić w tym PR-ze, czy zrobić z tego zadanie? (Findings outside the task's scope, 1 i 2)

## Koszt

Ok. 36 minut czasu pracy orkiestratora i sześciu tur agentów, na jednym modelu (Sonnet 5.5), 34,1 mln tokenów, w tym 32,9 mln wejścia z pamięci podręcznej. Jedna runda recenzji zablokowała: przegląd całej zmiany nie przeszedł z jednej uwagi, autor zrobił jedną poprawkę, a ten sam recenzent ją przepuścił. Recenzenta wysłano też raz z powrotem, żeby dokończył czytanie wybranych decyzji. Tabela etapów jest w zatwierdzonym zapisie: RECORD_STAGES_LINK.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Fundament nie czeka na przegląd: 19 scaleń od ostatniego, próg to 30.

</details>

## Technical changes

1. **Origin, gate order, remarks heading, missing-fact marker (the task's seven items).** `3effb9b` lets the remarks check accept a numbered heading (`task-cycle/remarks_check.py`, new case in `task-cycle/test_remarks_check.py`). `77ecd4a` rewrites the *Origin* sentence of the decision template, changes the foundation check to read a *Rests on* value that starts with `TODO` whole and to report a bare `TODO` (`elements/common/foundation_check.py`, five new tests), changes the sentence on `TODO` in `elements/common/rules.md`, and edits two decisions in place. `0d59ce9` puts the gate after the return step in step 10 of the cycle skill and adds the missing-fact item to the request template. The author's report: `reports/02-author-report.md` in the record.
2. **The words "at once" outside the task's list.** Sub-step 9.4 and the pin-move run of the cycle skill and the blocked-finding file say the gate runs at once where no return step runs on that code (`task-cycle/skill/SKILL.md`, `task-cycle/skill/blocked_finding.md`); these are needed so step 10's new order does not contradict them. The same author also reworded one bullet of `elements/invariants/template.md` so it no longer lets a missing link read a bare `TODO`.
3. **The fix of the review (`5841ed7`).** Widened the missing-fact item of the request template to the whole tree and made the decision on this section's contents say the same; added an example of it; added "at once" to the pin-move run; rewrapped two lines; added to the foundation check's docstring that only a value that begins with `TODO` is read as a missing fact; reworded one sentence of the gate decision's rationale (`reports/06-fix-report.md`). The return step compared the entries with the code and committed nothing (`reports/10-return-step-report.md`).

## Checks

- Gate before the change, on the base (`e3825a8`): `python -B gate/run_tests.py`, exit 0, 864 tests in 9 directories, no check failing.
- Gate on the change (`5841ed7`): `python -B gate/run_tests.py`, exit 0, 872 tests in 9 directories, every directory passed. It ran once, after the review of the fix and before the return step, under the cycle skill as it stands before this change (the new order binds from this merge). The return step made no commit, so the tree is the one the gate ran on. No check failed or did not run.
- Own-work checks: the author's check of the quoted sentences found all six word for word, and its mutations of the new tests failed as they should; the reviewer ran six mutations of the scripts, each caught by the new tests. The check of the fix found that item 7 no longer narrows, by a search of the repository.
- `python -B elements/common/foundation_check.py .`: exit 0, 0 errors, after the cycle's edits and after the fix.
- Form check of this description: RECORD_FORM_CHECK. Check of private paths on the description: RECORD_PRIVATE_CHECK. Checks on the copy of the record: RECORD_COPY_CHECKS.

## Foundation entries

1. WAY-160 — the cycle's: the gate runs once on the tree the return step and its review leave, and again only where the merge with the target branch changed it; its rationale and a rejected way are added.
2. WAY-71 — the cycle's: the main branch may hold `TODO` only in an invariant's *Rests on*, as `TODO — <the fact, with its source>`, and a change that leaves one puts it before the human; rationale rewritten, two rejected ways added.
3. WAY-287 — the cycle's, not listed by the task: the section for the human's decisions also holds each descriptive `TODO` in an invariant's *Rests on* that stands on the main branch after the change, with a compliant and a violating example.

No invariant test, surface or *Violated* mark changes.

## Minor findings

none

## Findings outside the task's scope

1. **M-4** (reviewer's words, partly beyond the task): "WAY-71's own *Verification* contradicts its binding sentence (`foundations/decisions.md`, entry WAY-71, *Verification*, line 1692): 'complies: ... a decision whose source is silent on what it rests on reads `Based on: TODO — <what is missing>`', while the binding sentence (rewritten by this change) lets the main branch hold `TODO` only in an invariant's *Rests on*. The contradiction was already at the base commit (the author reported it); the change rewrites the entry and does not repair it, and `DECISION_WORDS` in `foundation_check.py` still lets *Based on* read `TODO`. Partly beyond the task: the example is not in the task's list, and whether *Based on* may read `TODO` is a decision for the human. Within the entry the change rewrites, though, so it is listed."
2. **M-5, the part the fix did not take** (reviewer's words, mostly outside the task): "WAY-71 now governs what a request shows the human, but its *Scope* does not name `task-cycle` or `agent-instructions` (`foundations/decisions.md`, entry WAY-71, *Scope*), ... A cycle that selects decisions by *Scope* 'task-cycle' (the method of `way_of_working.md`, 'Reading the foundation', step 2) for a change to the request template will not find WAY-71. Adding the part, or a *Relations* link from WAY-287 to WAY-71, is a change to approved decisions; it is not in the task." The fix took only the other part, the example of the new item in WAY-287's *Verification*.

## Course of the cycle

- **Task and sources:** an independent task from the author's notes, "zadanie zbiorcze z uwag cykli — pole Origin, kolejność bramki, numerowane nagłówki w skrypcie uwag, TODO w Rests on"; its sources are the review of the AI layer of 2026-11-11 and the base `foundations` @ `e3825a8`.
- **Process pin:** none; the change is to the-way itself, and the methods were read from the task worktree.
- **Spec:** none; the task settles every choice its items open, so there was no open design choice.
- **Route:** one author without a plan, since about eleven files fit one agent; class `same` as the orchestrator, because the change rewords two approved decisions and two scripts whose parsing a slip would break silently. The author was resumed for the fix and the return step.
- **Plan:** none.
- **Choices:** seven rows in the questions table (Q1–Q7) of the record; the ones beyond the task's content stand in items 1 to 3 of *For you to decide*. Link: RECORD_CYCLE_LINK.
- **Blocking findings left:** none. The one blocking finding (the request template narrower than the decisions) was fixed once and the fix passed review.
- **Record:** RECORD_LINK
