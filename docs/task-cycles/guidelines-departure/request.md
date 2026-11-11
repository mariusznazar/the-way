**State: ready** — the change is complete and checked; two questions wait in *For you to decide*, and neither blocks the merge.

## What you will see

The-way now has, in its own decision log, a written decision that it does not hold its own code and tests to the general coding guidelines and the testing guidelines that a product must have. The decision has no end date and names all 16 parts of the-way's map of parts. A task of the-way that writes a script or a test therefore no longer stops and asks whether it must wait for such guidelines: the answer is on record. A change that adds a part to the map of parts also adds it to this decision, so a new part is covered from its first script. The decision does not cover the style guide, because the-way has no screens. If guidelines of the-way's own ever pay off, a separate task writes them and withdraws the decision.

### Underneath

One new entry in the decision log, written from the two settled rows of the task as one decision, with the reasons and the three ways not chosen. No code, test or skill changed.

## For you to decide

1. The decision says a separate task that writes "guidelines of the-way's own" withdraws it. The decision covers coding and testing guidelines only, so read literally, a task that wrote only one of them, or only a style guide, would withdraw the whole decision. The task does not say whether one of the two is enough. A second, smaller matter: the decision does not say whether the departure also releases a first file of a new kind of code from the duty to write guidelines for that kind; that question returns once, at the next task that adds a new kind of code to the-way. Fix the first in this request, or make a task of it? (Minor findings, 1; Findings outside the task's scope, 1)
2. The review of the whole change read 21 of about 285 decisions whole and 7 in part, and went through the rest by title, naming eight decisions that bear on the change and that it read by title only. It chose its reading by topic, because the part-based selection would have taken nearly the whole log. Merge anyway?

## Cost

15 minutes of working time, one model (the same as the orchestrator's) and about 10.4 million tokens counted with cache, across one author, one review of the whole change, one fix of Minor findings and its review, and the return step. Review rounds: none blocked; one fix round for Minor findings. The table of stages is in the committed record, linked at the end of this description.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing in this request waits for a review of the foundation.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — zmiana jest kompletna i sprawdzona; w sekcji „Do rozstrzygnięcia" czekają dwa pytania, żadne nie blokuje scalenia.

## Co zobaczysz

The way ma teraz w swoim dzienniku decyzji zapisaną decyzję, że nie podlega własnym ogólnym wytycznym kodowania ani wytycznym testów, które musi mieć każdy produkt. Decyzja nie ma terminu ważności i wymienia wszystkie 16 części mapy części the way. Zadanie the way, które pisze skrypt albo test, nie zatrzymuje się więc już z pytaniem, czy musi czekać na takie wytyczne: odpowiedź jest zapisana. Zmiana, która dodaje część do mapy części, dopisuje ją też do tej decyzji, więc nowa część jest objęta od pierwszego skryptu. Decyzja nie obejmuje styleguide'a, bo the way nie ma ekranów. Gdyby własne wytyczne the way zaczęły się opłacać, osobne zadanie je napisze i wycofa tę decyzję.

### Pod spodem

Jeden nowy wpis w dzienniku decyzji, napisany z dwóch przyjętych wierszy zadania jako jedna decyzja, z uzasadnieniem i trzema drogami niewybranymi. Żaden kod, test ani skill nie zmienił się.

## Do rozstrzygnięcia

1. Decyzja mówi, że osobne zadanie, które napisze „własne wytyczne" the way, ją wycofuje. Decyzja obejmuje tylko wytyczne kodowania i testów, więc czytana dosłownie: zadanie, które napisze tylko jedne z nich albo sam styleguide, wycofałoby całą decyzję. Zadanie nie rozstrzyga, czy wystarczą jedne z dwóch. Druga, mniejsza sprawa: decyzja nie mówi, czy odejście zwalnia też pierwszy plik nowego rodzaju kodu z obowiązku napisania wytycznych dla tego rodzaju; to pytanie wróci raz, przy następnym zadaniu, które doda nowy rodzaj kodu do the way. Poprawić pierwszą sprawę w tym requeście, czy zrobić z niej zadanie? (Minor findings, 1; Findings outside the task's scope, 1)
2. Przegląd całej zmiany przeczytał w całości 21 z około 285 decyzji i 7 w części, a resztę przejrzał po tytułach; wskazał osiem decyzji związanych ze zmianą, które przeczytał tylko po tytule. Dobrał lekturę według tematu, bo wybór według części objąłby niemal cały dziennik. Scalić mimo to?

## Koszt

15 minut czasu pracy, jeden model (ten sam co orkiestratora) i około 10,4 mln tokenów razem z pamięcią podręczną, w jednym autorze, jednym przeglądzie całej zmiany, jednej poprawce uwag Minor z jej przeglądem i kroku powrotnym. Rundy przeglądu: żadna nie blokowała; jedna runda poprawki uwag Minor. Tabela etapów jest w zatwierdzonym rekordzie, do którego link stoi na końcu tego opisu.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do rekordu przetrwa tylko wtedy. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

Two commits change `foundations/decisions.md` only. The first adds the decision WAY-327 after WAY-326 (+47 lines): the binding sentences, *Scope* naming the 16 parts of the part map, the *Verification* examples, the *Rationale* and the three ways not chosen. The second (+15/-13) fixes the four Minor findings of the review of the whole change: it adds the reason for the departure to the *Rationale*, adds the way not chosen from row 2 to *Rejected*, moves the withdrawal clause of row 1 into a third binding sentence and re-wraps the *Rationale*. Nothing outside the decision log changed.

## Checks

- Gate: `python -B gate/run_tests.py` in the task worktree at the final head, exit code 0, "864 tests in 9 directories; every directory passed". The same command on the base commit before the change: exit code 0, 864 tests. No check failed or did not run.
- Foundation check: `python -B elements/common/foundation_check.py --skip-test-citations`, exit code 0, "0 errors", run by the author, the return step and both reviews.
- Own-work check (author): the *Scope* of the decision read against the parts of the part map as two sets, equal, 16 identifiers; no *should*, *will* or capital requirement words in the binding sentences.
- Form check of this description, private-paths check of it, and the three checks on the copy of the record: filled in with the record link below.
- Process remarks check: run on the original record until it listed nothing (exit code 0 after one appending round, nine items).

## Foundation entries

- WAY-327 — row 1 and row 2: the-way does not hold its own code and tests to the general coding guidelines or the testing guidelines of a product, with no time limit and in all 16 parts of its part map, so no task of the-way waits for such guidelines; a change that adds a part to the map adds it to the decision's *Scope*; a separate task that writes guidelines of the-way's own withdraws it. Rows 1 and 2 are written as one entry, because row 2 only keeps the *Scope* of row 1 true. No invariant test, surface or *Violated* mark is changed.

## Minor findings

1. `foundations/decisions.md:10634-10635`, the third binding sentence of WAY-327 — found by the review of the fix, grade Minor, within the task. Reviewer's words: "'Guidelines of the-way's own' is wider than what the decision covers. The decision departs only from the general coding guidelines and the testing guidelines, and its *Rationale* excludes the styleguide. Read literally, a task that writes only a styleguide of the-way (not a thing the-way needs, as it has no screens), or only coding guidelines (leaving testing departed), 'withdraws this decision.' Row 1 says 'własne wytyczne' in the context of the two disciplines, so the wider wording is the row's own, and a task that writes any of them can state in its change which part of the decision it withdraws. It blocks nothing; a reader who meets it can resolve it from the *Rationale*. Fix, if the human wants it: 'A separate task that writes the coding guidelines and the testing guidelines of the-way's own withdraws this decision' (a choice of meaning for the human, since row 1 does not say whether one of the two is enough, so I did not grade it higher)."

## Findings outside the task's scope

1. Place: binding sentence 1 of WAY-327 and `product-guidelines/reading.md`. Reviewer's words: "WAY-216 gives a task that creates the first file of a kind of code absent from the general coding index the duty to designate an exemplar and write kind guidelines 'with their index row'. Binding sentence 1 releases only 'the general coding guidelines and the testing guidelines', and the-way has no `guidelines/coding.md` to hold an index. Whether a first file of a new kind in the-way is released from that duty is not answered by WAY-327 or by `product-guidelines/reading.md` (which says 'the general file must still exist unless ... a departure applies' and nothing about kinds). The task does not ask for it, so it is not a defect of this change; it is a question the next task that adds a kind of code in the-way will meet. Cost if left: the question returns once, at that task."

## Course of the cycle

- **Task and sources:** an independent task of the-way: record the decision that the-way departs from the general coding guidelines and the testing guidelines, in all 16 parts, with no end date; base commit e3825a8 of the integration branch; sources: the task document with its two settlement rows, the decisions on missing guidelines and on a departure, the part map.
- **Process pin:** not applicable; this is the-way itself.
- **Spec:** none — both rows settle the entry, so no open design choice.
- **Route:** one author without a plan, on the same model class as the orchestrator, because the entry binds 16 parts and needs a search of the whole foundation.
- **Plan:** none.
- **Choices:** 4 other choices, in the questions table of the record: the author's class of model, the reading of two reports' unread material as no gap (twice), and the two rows as one entry.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds the record.
