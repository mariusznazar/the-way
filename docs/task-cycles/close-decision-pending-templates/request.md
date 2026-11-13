**State: ready** — nothing waits for your answer; the one choice the cycle made beyond the task is only for you to accept by merging.

## What you will see

The templates that tell an agent how to write the entries of a product's foundation no longer carry the 30 notes "TODO — decision pending" that stood beside rules whose decision was once missing. Each rule now reads as a plain rule of the template, with the number of the decision behind it where one exists, so an agent writing an entry no longer takes a rule for something that does not bind, and no longer meets two sentences that contradict each other. Two notes stay on purpose: the task that deals with reading a setting in someone else's service and with where an invariant's condition is written closes them.

In the rewritten places the meaning of the rule did not change, except where you ruled otherwise. The first step of writing an entry now asks all open questions of one entry in one round, but of three kinds: a value the source does not give is asked with a pointer to where to look and never with a proposed value, a choice is asked with the ways open, their costs and a recommendation, and a question of assessment stays open; the paragraph on how a skill asks no longer sends back to that step. The sentence of an environment fact no longer says "in the present tense", the sentence about moving a product to another release of a tool is gone, the rule that a part may hold no files stays as it was, and the glossary says that a word the product shows its users in another language stays in the product's files. The heading "Draft" in the template of invariants is gone, so the template no longer says that half of its rules do not bind.

### Underneath

Only the text of seven files of the element templates and skills changed; the decision log, the invariants, the part map and every script and test are as they were, and the full set of tests passes as it did before.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. In four places the number of the decision behind a rule differs from the one in the task's table. Where a decision the table named does not say what the sentence says, the template names the decision that does, or none: the rule on when a fact may be about something outside the product cites one decision instead of two, the rule on when a product waits for the map of its parts cites none (the one decision it stood on did not say it), the rule on what a row of the external context names cites none for its first half, and the rule that a test stands in a file of code also cites the decision that excludes Markdown files. The reviewer confirmed the first two departures and asked for the other two. The price is that a reader finds fewer numbers than the task listed; the table's choice would have sent the reader to decisions that do not say the thing. (Technical changes, 2)
2. The sentence on a fact entry without a source now says in full which entries take the marker "TODO" and in which form: an invariant whose condition names a missing fact, and a decision whose basis names a missing source, each in the form the decision on the marker gives. The task asked only for a pointer to that decision; the pointer alone would have left a fact entry reading as if it stood on a fact. The price is one longer sentence. (Technical changes, 3)

## Cost

Working time of the cycle's agents across the orchestrator's session: 24 minutes 43 seconds, of which 7 minutes 50 seconds waiting for tools. Models: the orchestrator and the reviewer Claude Sonnet 5.5, the author Claude Haiku 5.5 (the cheaper class); about 24.3 million tokens (23.3 million of them cached input, 149 thousand output), 14.4 million on Sonnet and 9.9 million on Haiku. Review rounds: the review of the whole change passed with three Minor findings within the task; one fix and one review of it, passed; then the same reviewer read through the rest of the decisions it had left unread, passed. The gate ran twice, on the base and on the final tree, 15 and 12 minutes in the background. The table of stages is in the committed record, linked under Record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The foundation has waited for a review through 32 merges since its last tag; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — nic nie czeka na Twoją odpowiedź; jedyny wybór cyklu poza zadaniem służy tylko do przyjęcia przez scalenie.

## Co zobaczysz

Szablony, które mówią agentowi, jak pisać wpisy fundamentu produktu, nie niosą już 30 dopisków „TODO — decision pending” przy regułach, którym kiedyś brakowało decyzji. Każda reguła czyta się teraz jako zwykła reguła szablonu, z numerem decyzji, na której stoi, tam gdzie taka jest, więc agent piszący wpis nie bierze już reguły za niewiążącą i nie trafia na dwa zdania, które sobie przeczą. Dwa dopiski zostają celowo: zamyka je zadanie o odczycie ustawienia w cudzej usłudze i o miejscu warunku niezmiennika.

W przepisanych miejscach sens reguły się nie zmienił, poza tym, co rozstrzygnąłeś inaczej. Pierwszy krok pisania wpisu pyta teraz o wszystko, co zostało otwarte w jednym wpisie, w jednej rundzie, ale o trzy rodzaje rzeczy: brakującą wartość pyta, wskazując, gdzie jej szukać, nigdy z podaną wartością; wybór pyta z wariantami, kosztami i rekomendacją; ocena zostaje otwarta; akapit o tym, jak skill pyta, nie odsyła już do tego kroku. Zdanie faktu o otoczeniu nie mówi już „w czasie teraźniejszym”, zdanie o przejściu produktu na inne wydanie narzędzia zniknęło, reguła, że część może nie mieć plików, zostaje bez zmian, a słownik mówi, że słowo, które produkt pokazuje użytkownikom w innym języku, zostaje w plikach produktu. Nagłówek „Draft” w szablonie niezmienników zniknął, więc szablon nie mówi już, że połowa jego reguł nie wiąże.

### Pod spodem

Zmienił się tylko tekst siedmiu plików szablonów i skilli elementów; dziennik decyzji, niezmienniki, mapa części oraz każdy skrypt i test są takie jak były, a pełny zestaw testów przechodzi tak jak przedtem.

## Do twojej decyzji

### Wymagane od Ciebie

none

### Do poprawienia albo przepuszczenia

none

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. W czterech miejscach numer decyzji przy regule różni się od tego z tabeli zadania. Tam, gdzie decyzja z tabeli nie mówi tego, co zdanie, szablon podaje decyzję, która mówi, albo żadną: reguła o tym, kiedy fakt może dotyczyć czegoś spoza produktu, cytuje jedną decyzję zamiast dwóch, reguła o tym, kiedy produkt czeka z mapą swoich części, nie cytuje żadnej (jedyna decyzja, na której stała, tego nie mówiła), reguła o tym, co nazywa wiersz kontekstu zewnętrznego, nie cytuje żadnej przy pierwszej połowie, a reguła, że test stoi w pliku z kodem, cytuje też decyzję wyłączającą pliki Markdown. Recenzent potwierdził dwa pierwsze odstępstwa i poprosił o dwa pozostałe. Cena: czytelnik znajduje mniej numerów, niż wyliczało zadanie; wybór z tabeli odesłałby go do decyzji, które tej rzeczy nie mówią. (Technical changes, 2)
2. Zdanie o wpisie faktu bez źródła mówi teraz w całości, które wpisy dostają znacznik „TODO” i w jakiej formie: niezmiennik, którego warunek wskazuje brakujący fakt, i decyzja, której podstawa wskazuje brakujące źródło, każdy w formie, jaką podaje decyzja o znaczniku. Zadanie prosiło tylko o odesłanie do tej decyzji; samo odesłanie zostawiłoby wpis faktu czytający się tak, jakby stał na fakcie. Cena: jedno dłuższe zdanie. (Technical changes, 3)

## Koszt

Czas pracy agentów cyklu w sesji orkiestratora: 24 minuty 43 sekundy, z czego 7 minut 50 sekund to oczekiwanie na narzędzia. Modele: orkiestrator i recenzent Claude Sonnet 5.5, autor Claude Haiku 5.5 (tańsza klasa); około 24,3 mln tokenów (23,3 mln z nich to wejście z pamięci podręcznej, 149 tys. wyjście), 14,4 mln na Sonnet i 9,9 mln na Haiku. Rundy przeglądu: przegląd całej zmiany zakończył się wynikiem PASS z trzema uwagami Minor w zakresie zadania; jedna poprawka i jeden jej przegląd, PASS; potem ten sam recenzent doczytał pozostałe decyzje, których wcześniej nie przeczytał, PASS. Bramka biegła dwa razy, na bazie i na końcowym drzewie, po 15 i 12 minut w tle. Tabela etapów jest w zatwierdzonym zapisie, do którego link stoi w sekcji Record.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Fundament czeka na przegląd po 32 scaleniach od ostatniego tagu; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, a nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

1. Commit `2c27260` — the author's change in seven files: the 30 notes of "decision pending" removed: the 15 notes of cases S1–S12 closed with a decision number (S1 stood in four templates), the 8 of S13–S19 left as plain text, the 7 of items 2–9 closed as the task words them, the paragraph "How a skill asks" and step 4.1 of `elements/common/way_of_working.md` rewritten to the three kinds of question, the words "in the present tense" and the sentence on moving to another release removed from `elements/environment-facts/template.md`, the `Files: none` rule of `elements/part-map/template.md` kept, the block "Draft" removed from `elements/invariants/template.md`, and the sentence of `elements/glossary/template.md` on a word shown in another language replaced by the plain one based on two decisions. The ending of the rule at S5 ("it belongs to the foundation of the product whose commits decide it") is the only change of sense among S1–S19, as the task orders. The cleaned files are 908 lines before and 858 after.
2. Citations that differ from the task's table (item 1 of *You accept by merging*): S7 in `elements/environment-facts/template.md` cites only the decision on facts outside the product (WAY-90), not WAY-73, because WAY-90's own *Rejected* names this case; S11 in `elements/common/missing_element_file.md` cites no decision for "the part map is written before another element's first file", because WAY-44 covers the assignment of files and not the order of writing (the sentence still rests on WAY-28, cited already); S9 in `elements/part-map/template.md` cites WAY-48 only on its second sentence, the first being a reading of it that WAY-48 does not state; S3 in `elements/invariants/template.md` cites WAY-61 and WAY-321, since WAY-321 excludes Markdown files. S4, S5 and S10 were confirmed by the reviewer.
3. Commit `faee0f8` — the fix of three Minor findings of the review of the whole change: S3 and S9 as in item 2 above, and the sentence on a fact entry without a source in `elements/environment-facts/template.md` now names the invariant's *Rests on* and the decision's *Based on* with the `TODO` form WAY-71 gives each (item 2 of *You accept by merging*).
4. The return step compared the seven files, the decisions the task names, the invariants of the touched parts and the part map with the repository, found nothing that no longer matched and committed nothing.

## Checks

- The gate on the final tree: `python -B task-cycle/gate_times.py --output docs/task-cycles/close-decision-pending-templates/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1221 tests in 10 directories, every directory passed. On the base the same command exited 0 with 1221 tests. No check failed or did not run, and none failed and passed again in the cycle.
- Own-work check of the author: the foundation check `python -B elements/common/foundation_check.py --skip-test-citations` exit 0 (0 errors), `python -B gate/run_tests.py elements/common` exit 0 (144 tests) and `python -B gate/run_tests.py elements/part-map` exit 0 (39 tests); `grep -rn "decision pending" elements` lists exactly the two notes that stay; every decision number added was checked against its whole entry; the change is prose only and no test was added or changed, so no failing-first run applies. The reviewers repeated the foundation check on both heads, exit 0.
- The state of user-interface screens: not applicable, the change touches no screen.
- On the copy of the record: written and checked after this description was first published (see the edit that adds the record's link).
- On this description: the form check `python -B task-cycle/request_check.py docs/task-cycles/close-decision-pending-templates/request.md --task docs/task-cycles/close-decision-pending-templates/task.md` and the check of private paths on it, results below after the last edit.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the orchestrator's session: both exit 0.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 32`, `threshold: 30`, `reminder: yes`.

## Foundation entries

none. The change wrote no decision, invariant, environment fact, glossary entry or part-map entry, and changed no invariant test, no surface and no *Violated* mark.

## Minor findings

none. The three Minor findings of the review of the whole change that lay within the task were fixed (Technical changes, 3) and the review of the fix found nothing new.

## Findings outside the task's scope

1. Minor, review of the whole change. `elements/invariants/skill/decide_entry.md:12` states "one the human gives is written as a decision", a rule of entries that the decision on where rules stand puts in the template; it was there before the change and the change only closed its note. Whether to move it is a later task.
2. Minor, the review's second reading. Four templates (`elements/invariants/template.md:165`, `elements/environment-facts/template.md:170`, `elements/glossary/template.md:102`, `elements/part-map/template.md:168`) end "A field stays in this template only while someone or something reads it (WAY-05)", as the task orders. WAY-05's scope is the decision template; WAY-54 and WAY-86 already cite it for templates in general, so nothing contradicts it, but no decision states the rule for the other four elements. The reviewer: "Out of scope".
3. Minor, the review's second reading. `elements/common/way_of_working.md:138-140` (step 4.1) says "as »How a skill asks« gives it (WAY-113): a value the source does not give, …", but that section and WAY-113 give only decision and assessment questions; the kind of "a value the source does not give" is in step 3 and in WAY-54. The sentence is the task's own wording, so the change is faithful to it. The reviewer: "reword or add the kind to »How a skill asks« in a later task".

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle: close the 32 notes "decision pending" in the templates by one change (cases S1–S19 by the table, items 2–9 for S20–S25 and S27). Sources: the answers of the task's *Questions to settle* and the decision log; the-way at `fca8491` of `foundations`.
- **Process pin:** none; the-way itself, base `fca8491` of `foundations`; the gate on the base exited 0 with 1221 tests.
- **Spec:** none written; no open design choice.
- **Route:** one author without a plan, class `cheaper` (Haiku), the default for ordinary implementation; review of the whole change by a fresh reviewer on Sonnet (`PASS`, three Minor findings within the task); one fix and one review of it (`PASS`); return step with nothing to correct; a second turn of the same reviewer to read what it had named unread (`PASS`, two new Minor findings outside the task).
- **Plan:** none on this route.
- **Choices:** 3 choices of the cycle beyond the questions answered by a binding source (the record's questions table, Q1 to Q4; two of them are items 1 and 2 above).
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after the commit.
