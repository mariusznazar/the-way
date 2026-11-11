**State: ready** — corrected for your remarks; the change is reviewed and tested again; six items below wait for your yes.

## What you will see

Four small fixes to how the process works, all taken from remarks that earlier task cycles left behind, and — from your remarks on the first version of this request — one rule made complete.

- A decision no longer names a task note in its *Origin* field, wherever the product keeps its tasks. Whatever such a note carried of the reasoning goes into the decision's own rationale and rejected options, and *Origin* then reads `none`. Tasks are where work is found, never a source a decision points to.
- A task cycle now runs the product's full tests once, after the return step and its review, on the tree they leave. Before, it ran them first and again after the return step changed something. A second run happens only where merging the target branch changed the tree, or where the tests fail and the fix changes code (then the return step looks at that fix as well, and the decision on the gate now says what breaks it if the return step does not). For a product like loop2 this saves about 35 minutes per task.
- The script that checks that the doubts stage reports end with reach the cycle's process remarks now also recognises a section heading with a number in front, such as `## 12. Searches not found or unclear`. Before, such a doubt could vanish without a trace.
- Something an entry stands on that the foundation does not hold yet can stand on the main branch as `TODO — <what is missing, with its source>`, in three places: an invariant's *Rests on* (a fact), an invariant's *Derives from* (a decision not written yet) and a decision's *Based on* (what it rests on). The foundation check reads that whole, commas included, reports a bare `TODO` in any of the three as an error with a hint to name what is missing, and now also reports `TODO` in a decision's *Relations* or *Origin*, where the rule never allowed it. The rules, both templates and the request template say the same, and every request shows you each such gap.

### Underneath

Three decisions are edited in place (how the cycle runs the gate, what a foundation entry's fields may hold, and what this section holds); the decision on the entry's fields now also names the cycle's part in its scope. The cycle skill, the decision and invariant templates, the rules shared by the elements, the request template and the two scripts with their tests change as described above.

## For you to decide

1. **Which gaps a request shows you.** The task said a request shows each descriptive `TODO` "that the change leaves on the main branch", and left to the cycle in which point of this section it stands. The cycle put it here as a numbered item and read "leaves" wide: every such gap on the tree after the change, whether the change wrote it, kept it or did not remove it. The three places it covers (a fact, a decision, a basis) are your decision from the correction. Price: while an old gap stands, every request carries one item for it; today the-way has none and loop2 has one bare `TODO` that its own update will describe. Accept? (Foundation entries, 2 and 3)
2. **Two places in the cycle skill outside the task's list.** Because the full tests now wait for the return step, the cases that run them with no return step before them (a request blocked by a review finding, a slice that failed twice) now say "at once", and so does the run at a pin move. Without it, those cases would be told to wait for a step that does not run on that code. Accept? (Technical changes, 2)
3. **The decision on how the cycle runs the gate (the cycle's entry).** The gate runs once, on the tree the return step and its review leave, and again only where the merge with the target branch changed it. Its reasoning and the rejected way (rerunning only the checks that read the foundation, since the process does not know which checks of a product do) are added, and the "violates" example now names a gate failure whose fix the return step does not compare. Accept? (Foundation entries, 1)
4. **The decision on what a foundation entry's fields may hold (the cycle's entry).** The main branch may hold `TODO` only where an entry stands on something the foundation does not hold yet, in the three places above and in the form of each, and a change that leaves one there puts it before you. The reasoning is rewritten, and one rejected way is added: `TODO` only in *Rests on* would make an author of a decision whose source is silent, or of an invariant whose decision is not written yet, stop the cycle or write a false `none`. One sentence of the reasoning is the cycle's own, not your remark's: why *Relations* and *Origin* never read `TODO` (the reviewer found it true enough and not needed for the rule to stand). Accept? (Foundation entries, 2)
5. **The decision on what this section holds (the cycle's entry).** It now also holds each descriptive `TODO` in those three places that stands on the main branch after the merge, with a compliant and a violating example; the task did not list this decision, but the new item would contradict it otherwise. Accept? (Foundation entries, 3)
6. **A mixed value is read the wrong way round.** An invariant that rests on one fact the foundation holds and one it lacks has no way to be written: `Rests on: python-stdlib-modules · TODO` passes although the rule forbids a bare `TODO`, while the described `python-stdlib-modules · TODO — a second fact, from the vendor` is rejected with two confusing errors. The rule says only the form where the whole value is `TODO — …`, and nothing in your remarks settled the mixed case, so the cycle left it. Someone writing such an invariant will meet it. Fix it in this request, or make a task of it? (Findings outside the task's scope, 1)

## Cost

About 1 hour 3 minutes of working time across the orchestrator and the agents' turns, on one model (Sonnet 5.5), 70.0 million tokens, of which 67.7 million were cached input. Two review rounds: the first review of the whole change failed on one finding, the author made one fix and the same reviewer passed it; your remarks were then made as a correction, and the same reviewer passed that too. The reviewer was also sent back once to finish reading the decisions it had selected. The table of stages is in the committed record: RECORD_STAGES_LINK.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation is not due for a review: 19 merges since the last one, the threshold is 30.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — poprawione według Twoich uwag; zmiana jest znów zrecenzowana i przetestowana; sześć punktów poniżej czeka na Twoje „tak”.

## Co zobaczysz

Cztery drobne poprawki w tym, jak działa proces; wszystkie wzięte z uwag, które zostawiły wcześniejsze cykle zadań, a z Twoich uwag do pierwszej wersji tego PR-a — jedna reguła dokończona.

- Decyzja nie wskazuje już w polu *Origin* notatki zadania, bez względu na to, gdzie produkt trzyma zadania. To, co taka notatka niosła z uzasadnienia, idzie do uzasadnienia decyzji i do jej odrzuconych wariantów, a *Origin* brzmi wtedy `none`. Zadania służą do znajdowania pracy, nigdy nie są źródłem, na które wskazuje decyzja.
- Cykl zadania puszcza teraz pełne testy produktu raz, po kroku powrotu i jego przeglądzie, na drzewie, które zostawiają. Wcześniej puszczał je najpierw i jeszcze raz, gdy krok powrotu coś zmienił. Drugi przebieg jest tylko wtedy, gdy scalenie gałęzi docelowej zmieniło drzewo albo gdy testy padną, a poprawka zmieni kod (wtedy krok powrotu patrzy też na tę poprawkę, a decyzja o bramce mówi teraz, co jest pogwałceniem, gdy tego nie robi). W produkcie takim jak loop2 to ok. 35 minut oszczędności na zadanie.
- Skrypt, który pilnuje, żeby wątpliwości z końca raportów etapów trafiły do uwag procesowych cyklu, rozpoznaje teraz także nagłówek sekcji z numerem na początku, np. `## 12. Searches not found or unclear`. Wcześniej taka wątpliwość mogła przepaść bez śladu.
- To, na czym wpis stoi, a czego fundament jeszcze nie ma, może stać na gałęzi głównej jako `TODO — <czego brakuje, ze źródłem>`, w trzech miejscach: w *Rests on* niezmiennika (fakt), w *Derives from* niezmiennika (decyzja jeszcze nienapisana) i w *Based on* decyzji (na czym stoi). Sprawdzanie fundamentu czyta to w całości, z przecinkami, samo `TODO` w którymkolwiek z trzech zgłasza jako błąd z podpowiedzią, żeby nazwać, czego brakuje, i zgłasza teraz także `TODO` w *Relations* i *Origin* decyzji, gdzie reguła nigdy go nie dopuszczała. Reguły, oba szablony i szablon opisu PR-a mówią to samo, a każdy PR pokazuje Ci każdą taką lukę.

### Pod spodem

Trzy decyzje są poprawione w miejscu (jak cykl puszcza bramkę, co mogą zawierać pola wpisu fundamentu i co zawiera ta sekcja), a decyzja o polach wpisu wymienia teraz w zakresie także część cyklu. Skill cyklu, szablony decyzji i niezmienników, reguły wspólne dla elementów, szablon opisu PR-a i dwa skrypty z testami zmieniają się jak wyżej.

## Do Twojej decyzji

1. **Które luki pokazuje PR.** Zadanie kazało pokazać każde opisowe `TODO`, „które zmiana zostawia na gałęzi głównej”, i zostawiło cyklowi wybór miejsca w tej sekcji. Cykl umieścił to tu jako punkt listy i odczytał „zostawia” szeroko: każda taka luka na drzewie po zmianie, niezależnie od tego, czy zmiana ją napisała, zachowała, czy tylko nie usunęła. Trzy miejsca, które to obejmuje (fakt, decyzja, podstawa), to Twoja decyzja z korekty. Cena: dopóki stoi stara luka, każdy PR niesie dla niej jeden punkt; dziś the-way żadnej nie ma, a loop2 ma jedno gołe `TODO`, które opisze jego własna aktualizacja. Akceptujesz? (Foundation entries, 2 i 3)
2. **Dwa miejsca w skillu cyklu poza listą zadania.** Skoro pełne testy czekają teraz na krok powrotu, przypadki, które puszczają je bez kroku powrotu przed nimi (PR zablokowany uwagą z przeglądu, wycinek, który zawiódł dwa razy), mówią teraz „od razu”, tak samo jak przebieg przy zmianie wersji procesu. Bez tego te przypadki miałyby czekać na krok, który na tym kodzie się nie odbywa. Akceptujesz? (Technical changes, 2)
3. **Decyzja o tym, jak cykl puszcza bramkę (wpis cyklu).** Bramka idzie raz, na drzewie zostawionym przez krok powrotu i jego przegląd, a drugi raz tylko tam, gdzie scalenie z gałęzią docelową zmieniło drzewo. Dodane są jej uzasadnienie i odrzucony wariant (ponawianie tylko sprawdzeń czytających fundament, bo proces nie wie, które sprawdzenia produktu to robią), a przykład „niezgodnie” nazywa teraz awarię bramki, której poprawki krok powrotu nie porównuje. Akceptujesz? (Foundation entries, 1)
4. **Decyzja o tym, co mogą zawierać pola wpisu fundamentu (wpis cyklu).** Gałąź główna może mieć `TODO` tylko tam, gdzie wpis stoi na czymś, czego fundament jeszcze nie ma: w trzech miejscach wyżej i w postaci każdego z nich, a zmiana, która je zostawia, pokazuje to Tobie. Uzasadnienie jest napisane od nowa, dodany jest jeden odrzucony wariant: `TODO` tylko w *Rests on* zmusiłoby autora decyzji, której źródło milczy, albo niezmiennika, którego decyzja nie jest jeszcze napisana, do zatrzymania cyklu albo do wpisania fałszywego `none`. Jedno zdanie uzasadnienia jest własne cyklu, nie Twoją uwagą: dlaczego *Relations* i *Origin* nigdy nie przyjmują `TODO` (recenzent uznał je za wystarczająco prawdziwe i niepotrzebne, by reguła stała). Akceptujesz? (Foundation entries, 2)
5. **Decyzja o tym, co zawiera ta sekcja (wpis cyklu).** Zawiera teraz także każde opisowe `TODO` w tych trzech miejscach, które stoi na gałęzi głównej po scaleniu, z przykładem zgodnym i niezgodnym; zadanie nie wymieniało tej decyzji, ale nowy punkt bez tego byłby z nią sprzeczny. Akceptujesz? (Foundation entries, 3)
6. **Wartość mieszana jest czytana na opak.** Niezmiennik, który stoi na jednym fakcie, który fundament ma, i jednym, którego nie ma, nie ma jak być zapisany: `Rests on: python-stdlib-modules · TODO` przechodzi, choć reguła zabrania gołego `TODO`, a opisane `python-stdlib-modules · TODO — a second fact, from the vendor` jest odrzucane dwoma mylącymi błędami. Reguła mówi tylko o postaci, w której cała wartość to `TODO — …`, a Twoje uwagi nie rozstrzygały przypadku mieszanego, więc cykl go zostawił. Ktoś, kto napisze taki niezmiennik, na to trafi. Poprawić w tym PR-ze, czy zrobić z tego zadanie? (Findings outside the task's scope, 1)

## Koszt

Ok. 1 godzina 3 minuty czasu pracy orkiestratora i tur agentów, na jednym modelu (Sonnet 5.5), 70,0 mln tokenów, w tym 67,7 mln wejścia z pamięci podręcznej. Dwie rundy recenzji: pierwszy przegląd całej zmiany nie przeszedł z jednej uwagi, autor zrobił jedną poprawkę, a ten sam recenzent ją przepuścił; Twoje uwagi poszły potem jako korekta, którą ten sam recenzent też przepuścił. Recenzenta wysłano też raz z powrotem, żeby dokończył czytanie wybranych decyzji. Tabela etapów jest w zatwierdzonym zapisie: RECORD_STAGES_LINK.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Fundament nie czeka na przegląd: 19 scaleń od ostatniego, próg to 30.

</details>

## Technical changes

1. **Origin, gate order, remarks heading, missing-fact marker (the task's seven items).** `3effb9b` lets the remarks check accept a numbered heading (`task-cycle/remarks_check.py`, new case in `task-cycle/test_remarks_check.py`). `77ecd4a` rewrites the *Origin* sentence of the decision template, changes the foundation check to read a *Rests on* value that starts with `TODO` whole and to report a bare `TODO` (`elements/common/foundation_check.py`, five new tests), changes the sentence on `TODO` in `elements/common/rules.md`, and edits two decisions in place. `0d59ce9` puts the gate after the return step in step 10 of the cycle skill and adds the missing-fact item to the request template. The author's report: `reports/02-author-report.md` in the record.
2. **The words "at once" outside the task's list.** Sub-step 9.4 and the pin-move run of the cycle skill and the blocked-finding file say the gate runs at once where no return step runs on that code (`task-cycle/skill/SKILL.md`, `task-cycle/skill/blocked_finding.md`); these are needed so step 10's new order does not contradict them. The same author also reworded one bullet of `elements/invariants/template.md` so it no longer lets a missing link read a bare `TODO`.
3. **The fix of the first review (`5841ed7`).** Widened the missing-fact item of the request template to the whole tree and made the decision on this section's contents say the same; added an example of it; added "at once" to the pin-move run; rewrapped two lines; added to the foundation check's docstring that only a value that begins with `TODO` is read as a missing fact; reworded one sentence of the gate decision's rationale (`reports/06-fix-report.md`).
4. **The correction for your remarks (`10d443f`).** Adds `task-cycle` to the scope of the decision on the entry's fields and the "violates" case to the gate decision; extends the descriptive `TODO` to an invariant's *Derives from* and a decision's *Based on* in that decision, in the rules, in both templates, in the decision on this section's contents and in item 15 of the request template; makes the foundation check read both fields whole, report a bare `TODO` in each, and report `TODO` in *Relations* and *Origin*, with 14 new test cases (`elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`, `reports/13-correction-report.md`). Run read-only on loop2 the check reports one error, the bare `TODO` in *Rests on* that the task already names.
5. **The return step ran twice and committed nothing** (`reports/10-return-step-report.md`, `reports/17-correction-return-step-report.md`): the entries, the part map and the glossary terms agree with the code.

## Checks

- Gate before the change, on the base (`e3825a8`): `python -B gate/run_tests.py`, exit 0, 864 tests in 9 directories, no check failing.
- Gate on the change after the first fix (`5841ed7`): exit 0, 872 tests. Gate on the corrected tree (`10d443f`): `python -B gate/run_tests.py`, exit 0, 880 tests in 9 directories, every directory passed. Each ran once, after the review of the change before it, under the cycle skill as it stood before this change merged; neither return step committed, so the final tree is the one the last gate ran on. No check failed or did not run.
- Own-work checks: the author's check of the quoted sentences found all six word for word, and its mutations of the new tests failed as they should; the reviewer ran six mutations of the scripts, each caught; the new tests of the correction fail without the code (15 failures counted by the reviewer, 14 by the author).
- `python -B elements/common/foundation_check.py .`: exit 0, 0 errors, after the cycle's edits, after the fix and after the correction.
- Form check of this description: RECORD_FORM_CHECK. Check of private paths on the description: RECORD_PRIVATE_CHECK. Checks on the copy of the record: RECORD_COPY_CHECKS.

## Foundation entries

1. WAY-160 — the cycle's: the gate runs once on the tree the return step and its review leave, and again only where the merge with the target branch changed it; its rationale and a rejected way are added, and its "violates" example names a gate failure whose fix the return step does not compare.
2. WAY-71 — the cycle's: the main branch may hold `TODO` only where an entry stands on something the foundation does not hold yet — an invariant's *Rests on*, an invariant's *Derives from* and a decision's *Based on*, each in its form — and a change that leaves one puts it before the human; `task-cycle` joins its scope; rationale rewritten, three rejected ways added, and a new case of what violates it (a bare `TODO` in any of the three, `TODO` in *Relations* or *Origin*).
3. WAY-287 — the cycle's, not listed by the task: the section for the human's decisions also holds each descriptive `TODO` in those three places that stands on the main branch after the change, with a compliant and a violating example.

No invariant test, surface or *Violated* mark changes.

## Minor findings

none. (The author notes one line of the decision on this section's contents now passes 100 columns after a rewrap; cosmetic, left so that a commit does not start another review.)

## Findings outside the task's scope

1. **N-1** (reviewer's words of the review of the correction, marked outside the task's scope): "A list in *Rests on* or *Derives from* that holds an existing entry and a `TODO` is read the other way round from the rule: the bare `TODO` item passes, the described one fails for *Rests on* (`elements/common/foundation_check.py`, the checks of the three fields). I ran `foundation_check.py` on a scratch copy of `foundations/` with `script-imports` edited: `Rests on: python-stdlib-modules · TODO` gives no error; `Rests on: python-stdlib-modules · TODO — a second fact, from the vendor` gives two errors; `Derives from: WAY-38 · TODO — a second decision, expected in the next task` and `WAY-38 · TODO` give none; `Derives from: TODO` gives the bare-`TODO` error. The rule gives only the form where the whole value is `TODO — ...`, which leaves unsaid how an invariant that rests on one fact the foundation holds and one it lacks is to be written; WAY-17 says every link is written, so dropping the existing fact is not an answer. [...] It is an issue of the rule more than of this diff, and the remarks did not settle it, so it lies outside the correction and outside the task; it blocks nothing. Suggested: a decision of the human on mixed values (either read the part after `·` that begins with `TODO` as a description, or say in the rule that the field holds the whole `TODO — ...` and the existing fact stands in the description)."
2. Left unchanged and not asked for: a *Relations* link from WAY-287 to WAY-71, the remaining part of an earlier remark of the first review (its other part, the scope of WAY-71, was made in the correction).

## Course of the cycle

- **Task and sources:** an independent task from the author's notes, "zadanie zbiorcze z uwag cykli — pole Origin, kolejność bramki, numerowane nagłówki w skrypcie uwag, TODO w Rests on"; its sources are the review of the AI layer of 2026-11-11 and the base `foundations` @ `e3825a8`.
- **Process pin:** none; the change is to the-way itself, and the methods were read from the task worktree.
- **Spec:** none; the task settles every choice its items open, so there was no open design choice.
- **Route:** one author without a plan, since about eleven files fit one agent; class `same` as the orchestrator, because the change rewords approved decisions and two scripts whose parsing a slip would break silently. The author was resumed for the fix, the return steps and the correction. Correction 1 (your remarks of the session, [the remarks](RECORD_REMARKS_LINK)): reset base `14b7680`, the removal commit of the first copy of the record, whose tree is the reviewed and tested one.
- **Plan:** none.
- **Choices:** ten rows in the questions table of the record (Q1–Q10); the ones beyond the task's content stand in items 1 to 6 of *For you to decide*. Link: RECORD_CYCLE_LINK.
- **Blocking findings left:** none. The one blocking finding (the request template narrower than the decisions) was fixed once and the fix passed review; the correction passed its review with one Minor finding, left to you (item 6).
- **Record:** RECORD_LINK
