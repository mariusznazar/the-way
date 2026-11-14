**State: ready** — nothing waits for your answer; the two items in the last group you only accept by merging.

## What you will see

A reviewer of a change now grades a remark about the structure of the code — for example that a function grew — as a minor remark in every product that has no rule on the size of functions and files, whatever the reason it has none. Until now the reviewer's instructions and the decision behind them named only two such products: one that gave up the rule by a written decision, and one that has no coding guidelines at all, like the-way itself. They left out a third: a product whose coding guidelines were written before the size rule existed, which is how the game stands until it adopts the rule. The instructions and the decision now give the three as examples of every product without the rule, not as a closed list, and say the same as the longer text that tells the reviewer of the whole change how to read structure.

For you this means that when the first change in such a product is reviewed, a remark that a function grew can no longer be graded minor by one reviewer and important by another; it stays minor, does not block the change, and so costs no round of fixes and a second review. Nothing breaks today, since nobody reviews changes in the game by this rule yet.

The final gate of this change passed: 1267 tests in 10 directories, 12 minutes 43 seconds on this machine, with one other gate running at the same time.

### Underneath

One sentence of the review instructions and the binding sentence of the decision on grading structure now name the three cases as examples of "every such finding", and the decision's checks and reasoning no longer speak of the older two-case scope; a line of the decision that was far wider than the rest is wrapped like the others.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The longer text that tells the reviewer of the whole change how to read structure was left as it is. Its last point already says that where the product's guidelines hold no such rule a structure remark is minor, and a product with guidelines from before the rule falls under that wording; the task did not list that text for an edit. The price: that point does not name the third case in words, so a reader who takes "hold no such rule" very narrowly could still miss it; naming it would have added a third place that repeats the examples and can drift from the other two.
2. The newest changes of the target branch (the limit on what a slice of a plan reads) were merged into this branch while the cycle ran and were not reviewed by a separate reviewer: the merge was clean, it touches neither the review instructions nor the decision this change edits, a search of what it brought in finds none of the words of this change, and the foundation check and the whole gate passed on the merged tree. The price: if the new decision on the reading limit collides in meaning with the edited decision in a way the search did not find, it shows only when someone next works on either.

## Cost

Working time of the orchestrator's turns and the agents' turns: 14 minutes 17 seconds, of which 9 minutes 33 seconds was not waiting for tools; the two gate runs (15 minutes 55 seconds, then 12 minutes 43 seconds) ran beside, in the background. Models: the orchestrator and the review on Claude Sonnet 5.5, the author on Claude Haiku 5.5 (the cheaper class, since the change is ordinary editing of text); about 11.7 million tokens, of which 11.2 million are cached input and 82 thousand output. The review passed at once, so no fix and no second review ran; the reviewer was resumed once to read what it had left unread. The table of stages stands in the record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The foundation has waited for a review through 37 merges since its last tag; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — nic nie czeka na Twoją odpowiedź; dwie pozycje w ostatniej grupie tylko przyjmujesz przez scalenie.

## Co zobaczysz

Recenzent zmiany ocenia teraz uwagę o strukturze kodu — na przykład że funkcja urosła — jako drobną w każdym produkcie, który nie ma reguły o rozmiarze funkcji i plików, niezależnie od powodu. Dotąd instrukcja recenzenta i decyzja za nią wymieniały tylko dwa takie produkty: ten, który zrezygnował z reguły zapisaną decyzją, i ten, który nie ma wytycznych kodowania wcale, jak samo the way. Pomijały trzeci: produkt, którego wytyczne kodowania powstały, zanim reguła rozmiaru istniała — tak stoi gra, dopóki jej nie przyjmie. Instrukcja i decyzja podają teraz te trzy jako przykłady każdego produktu bez reguły, a nie jako zamkniętą listę, i mówią to samo co dłuższy tekst, który uczy recenzenta całej zmiany czytać strukturę.

Dla Ciebie znaczy to, że przy pierwszym przeglądzie zmiany w takim produkcie uwaga o rozroście funkcji nie dostanie już drobnego stopnia od jednego recenzenta i ważnego od innego; zostaje drobna, nie blokuje zmiany, więc nie kosztuje rundy poprawek ani drugiego przeglądu. Dziś nic się nie psuje, bo zmian w grze według tej reguły nikt jeszcze nie przegląda.

Końcowa bramka tej zmiany przeszła: 1267 testów w 10 katalogach, 12 minut 43 sekundy na tej maszynie, przy jednej innej bramce działającej w tym samym czasie.

### Pod spodem

Jedno zdanie instrukcji przeglądu i zdanie wiążące decyzji o ocenie struktury podają teraz trzy przypadki jako przykłady „każdej takiej uwagi”, a sprawdzenia i uzasadnienie decyzji nie mówią już o dawnym zakresie dwóch przypadków; linia decyzji, która była znacznie szersza od reszty, jest zawinięta jak pozostałe.

## Do twojej decyzji

### Wymagane od Ciebie

none

### Do poprawienia albo przepuszczenia

none

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. Dłuższy tekst, który uczy recenzenta całej zmiany czytać strukturę, został bez zmian. Jego ostatni punkt już mówi, że tam, gdzie wytyczne produktu nie mają takiej reguły, uwaga o strukturze jest drobna, a produkt z wytycznymi sprzed reguły podpada pod to sformułowanie; zadanie nie wymieniało tego tekstu do edycji. Cena: ten punkt nie nazywa trzeciego przypadku wprost, więc czytelnik, który weźmie „nie mają takiej reguły” bardzo wąsko, mógłby go jeszcze przeoczyć; nazwanie go dodałoby trzecie miejsce powtarzające przykłady, które może rozjechać się z dwoma pozostałymi.
2. Najnowsze zmiany gałęzi docelowej (limit tego, co czyta slice planu) weszły do tej gałęzi w trakcie cyklu i nie miały osobnej recenzji: scalenie było czyste, nie dotyka ani instrukcji przeglądu, ani decyzji, które ta zmiana edytuje, wyszukanie słów tej zmiany w tym, co weszło, niczego nie znajduje, a kontrola fundamentu i cała bramka przeszły na scalonym drzewie. Cena: jeśli nowa decyzja o limicie czytania koliduje znaczeniem z edytowaną decyzją w sposób, którego wyszukanie nie znalazło, wyjdzie to dopiero przy następnej pracy nad jedną z nich.

## Koszt

Czas pracy tur orkiestratora i agentów: 14 minut 17 sekund, z czego 9 minut 33 sekundy to czas bez oczekiwania na narzędzia; dwa przebiegi bramki (15 minut 55 sekund, potem 12 minut 43 sekundy) biegły obok, w tle. Modele: orkiestrator i recenzja Claude Sonnet 5.5, autor Claude Haiku 5.5 (klasa tańsza, bo zmiana to zwykła edycja tekstu); około 11,7 mln tokenów, z czego 11,2 mln to wejście z pamięci podręcznej, a 82 tys. wyjście. Recenzja przeszła od razu, więc nie było poprawki ani drugiego przeglądu; recenzent został wznowiony raz, żeby doczytać to, czego nie przeczytał. Tabela etapów leży w zapisie.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Fundament czeka na przegląd po 37 scaleniach od ostatniego tagu; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, a nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

1. Commit `5554f5d` — `task-cycle/review/SKILL.md`, section 3 (lines 126–131): the sentence on a finding about the structure of code is Minor "where the product has no rule of size, whatever the reason", with "for example, the product departed from the rule by a decision, it has no coding guidelines at all, or its guidelines were written before the rule existed" as examples and the clause on judging the scope as a sentence of its own. `foundations/decisions.md`, entry WAY-363, edited in place (WAY-07): the binding sentence says the same; the *Verification* bullet that complies now also names "a product whose guidelines were written before the rule and hold none of it"; the *Rationale* sentence "The reviewer still judges the scope of each finding…", which stood in one line of 163 characters, is wrapped like the rest of the entry. *Scope*, *Relations*, *Rejected* and the *violates* bullet were left as they were: they already speak of "a product with no rule of size" in general terms.
2. Merge `6914b90` — the target branch at `3c572b9` (the reading limit of a slice, WAY-371, `task-cycle/slice_size.py` and its test) merged in, no conflict.

The change touches no code, test or interface; the whole-change review's selection and the author's search of the foundation found no other place that states the two-case scope.

## Checks

- The gate on the merged final tree (`6914b90`): `python -B task-cycle/gate_times.py --output docs/task-cycles/structure-grade-no-rule-cases/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1267 tests in 10 directories, every directory passed, 763 seconds, with one other gate running at the same time. The same command on the reviewed tree before the merge (`5554f5d`): exit 0, 1267 tests, every directory passed, 955 seconds, with one other gate running at the same time.
- Base: the starting state `1be9057` is a merge commit with the same tree as its second parent, so no gate ran on it; the list of tests failing before the change, none, was taken from the final gate of the cycle `gate-series-on-test-runner` (exit 0, 1267 tests), from its record at commit `97ac793`, file `docs/task-cycles/gate-series-on-test-runner/cycle.md`.
- Own-work check of the author: the requirement most likely unmet was one grade for the three cases in the three places; a search of the repository for the old two-case wording with each hit read showed only the two edited places name the cases and the review text covers the third through "hold no such rule"; `python -B elements/common/foundation_check.py` exit 0, 0 errors; `python -B gate/run_tests.py task-cycle` exit 0, 394 tests. `python -B gate/run_tests.py foundations` exit 1, "no test found in foundations": the directory holds no tests, so it is no check of the change.
- Review of the whole change: `PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8`, no finding of any grade; it ran `python -B elements/common/foundation_check.py` (exit 0) and `python -B task-cycle/change_file_sizes.py 1be9057 5554f5d` (exit 0); the-way has no rule of size, so no test of it exists. In a second turn it read the invariants, the part map, the glossary and the two guideline files of the part whole, and counted 14 of 260 selected decisions read whole and the rest by title.
- The state of user-interface screens: not applicable, the change touches no screen.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 37`, `threshold: 30`, `reminder: yes`.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the orchestrator's session: both exit 0.
- On the copy of the record and on this description: written and checked after this description was first published (see the edit that adds the record's link).

## Foundation entries

- WAY-363, edited in place by *To do* 2 of the task: a reviewer grades as Minor a finding about the structure of code below the threshold of the rule of size, and every such finding in a product that has no rule of size, whatever the reason — a decision departing from the rule, no coding guidelines, or guidelines written before the rule; no row of *Settlements to record* and no projected entry carries it; *To do* 2 of the task does, and you accepted that with the task document, so it is no item of *You accept by merging*.

No invariant, environment fact, glossary entry or part-map entry is written, and no invariant test, surface or *Violated* mark is changed.

## Minor findings

none

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle: close the sentence of the review skill and the decision on grading structure so that a product with guidelines from before the size rule is covered as the other two cases are. Sources: the task's *To do*, *Acceptance criteria*, *Context* and *Decisions in play*; the-way at `1be9057` of `foundations`.
- **Process pin:** none; the-way itself, base `1be9057` of `foundations`; no gate ran on the base (the list of failing tests, none, taken from the earlier cycle's final gate, see *Checks*).
- **Spec:** none written; no open design choice.
- **Route:** one author without a plan, class `cheaper` (Claude Haiku 5.5), because the change is ordinary editing of text; review of the whole change by a fresh reviewer on Sonnet (`PASS`, no finding); the reviewer was resumed once to read its unread material (invariants, part map, glossary, one decision, two guideline files) and found nothing; the return step found nothing to change and committed nothing.
- **Plan:** none on this route.
- **Choices:** 3 choices of the cycle beyond the questions answered by a binding source (the record's questions table holds them as Q1, Q3 and Q4; Q2 was superseded by the reviewer's second turn; items 1 and 2 of *You accept by merging* are Q4 and Q3).
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after the commit.
