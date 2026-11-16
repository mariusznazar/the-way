---
title: "the way: przenumerowanie decyzji przy scaleniu, gdy równoległe zadanie zajęło te same numery"
status: draft
created: 2026-11-14T08:10
updated: 2026-11-14
tags: [zadanie]
related: the project note of the process of working on a product, in the author's private notes
---

# the way: przenumerowanie decyzji przy scaleniu, gdy równoległe zadanie zajęło te same numery

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Każde zadanie nadaje nowym decyzjom „następny wolny numer” według dziennika na gałęzi, z której wystartowało (WAY-19), więc dwa zadania idące równolegle dostają te same numery.
- Zadanie scalane jako drugie musi przy uzgadnianiu z gałęzią docelową (krok 12 skilla cyklu) przenumerować swoje decyzje, a skill cyklu tego kroku nie zna — agent prowadzący cykl wymyśla przenumerowanie sam, bez reguły.
- Przenumerowanie dotąd obejmowało fundament i kod, a nie dokumenty samego cyklu: opis PR-a podaje nowe numery, a spec, plan, przekazania i raporty cyklu pod linkami w tym PR-ze — stare.
- Mariusz przy czytaniu takiego PR-a musi każdy numer decyzji z dokumentów cyklu przeliczać sam według notki z przeliczeniem.
- Zdarza się regularnie, nie raz: w the-way co najmniej cztery razy (commity `62f81a3`, `897bc0c`, `73fb11d`, `c756236`), w loop2 dwa razy (PR #25 „ognisko-i-jedzenie”, commit `1e57e30` w cyklu „mag-w-lesie”).

### To do

1. Krok 12 skilla cyklu (`task-cycle/skill/SKILL.md`, sekcja „Request and handoff”, akapit kroku 12, który zaczyna się od „Otherwise merge the remote target branch into the task branch”, ok. linii 488) mówi, co robić, gdy gałąź docelowa zajęła numery, które gałąź zadania nadała swoim nowym decyzjom: przed scaleniem, osobnym commitem, gałąź zadania przenumerowuje swoje nowe decyzje na kolejne wolne numery po numerach gałęzi docelowej, nigdy numerów gałęzi docelowej.
2. To samo przenumerowanie, jednym przebiegiem, obejmuje każde odwołanie do tych decyzji w plikach gałęzi i w oryginale zapisu cyklu w `.runs/task-cycles/<task-slug>/` w stanie sprzed wpisania zdarzenia uzgodnienia — spec, plan, przekazania, raporty i `cycle.md` razem z uwagami procesowymi; teksty zapisane później i uwagi Mariusza cytowane słowo w słowo zostają, jak są.
3. Wpis dziennika zdarzeń cyklu, który odnotowuje uzgodnienie z gałęzią docelową, podaje przeliczenie starych numerów na nowe; zapis cyklu nie dostaje osobnej notki z przeliczeniem na początku.
4. Skill korekty (`task-cycle/skill/correction.md`) przy obu swoich scaleniach gałęzi docelowej — w akapicie, który zaczyna się od „In the-way itself, before anything else”, i w akapicie, który zaczyna się od „Take a link to the request” — przenumerowuje decyzje tak, jak daje krok 12.

### Questions to settle

- 1. Co z tekstami zapisu cyklu, które powstały przed przenumerowaniem i podają stare numery?
  - Answer: Przepisać je w tym samym przebiegu, który przenumerowuje decyzje w kodzie — przed scaleniem i zanim cykl wpisze zdarzenie uzgodnienia (punkt 2).
  - Not chosen:
    - zostawić stare numery z notką z przeliczeniem na początku zapisu — zostaje dokładnie ten rozjazd, który zadanie ma usunąć, i każdy numer Mariusz przelicza sam
    - przepisać numery dopiero w kopii publikowanej w repozytorium, przy czyszczeniu ścieżek prywatnych — kopia ma też teksty sprzed scalenia i po nim, te drugie podają numery gałęzi docelowej z tego samego zakresu, a jedno przepisanie by je zepsuło; rozróżnianie tekstów po dacie to krucha mechanika
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a”; koszt wybranej drogi podany w pytaniu: raporty agentów nie są już co do znaku tym, co agent napisał (zmieniają się tylko numery), a przepisania zapisu nie sprawdza recenzent scalenia, bo zapis nie jest częścią kodu.
- 2. Gdzie zostaje przeliczenie starych numerów na nowe?
  - Answer: Tylko we wpisie dziennika zdarzeń cyklu, który odnotowuje uzgodnienie z gałęzią docelową (punkt 3).
  - Not chosen:
    - także notka na początku zapisu cyklu — druga kopia tej samej informacji, a po przepisaniu zapisu czytelnik dokumentów jej nie potrzebuje
    - nigdzie — stary commit albo wcześniejsza uwaga Mariusza ze starym numerem staje się nieczytelna
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a”
- 3. Czy reguła obejmuje też scalenie gałęzi docelowej w korekcie po uwagach do PR-a?
  - Answer: Tak — reguła stoi w kroku 12, a skill korekty odsyła do niej przy obu swoich scaleniach (punkt 4).
  - Not chosen:
    - tylko krok 12 — w korekcie agent dalej improwizuje, a to tam wypada drugie przenumerowanie, gdy PR wraca po scaleniu innego PR-a dopisującego decyzje
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 a”
- 4. Czy reguła trafia do dziennika decyzji jako nowa decyzja, z odrzuconymi wariantami?
  - Answer: Tak — nowa decyzja, której *Rejected* trzyma: przenumerowanie decyzji gałęzi docelowej; tymczasowy znacznik zamiast numeru do chwili scalenia; zostawienie starych numerów w zapisie cyklu; podglądanie numerów zajętych na cudzych gałęziach, które nie działa, bo gałąź zadania jest wypychana dopiero w kroku 12.
  - Not chosen:
    - tylko zdanie w skillu — odrzucone warianty nie stoją nigdzie, gdzie agent je przeczyta, a jeden z nich już raz wrócił w propozycji nocnego skanu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 a”; koszt wybranej drogi podany w pytaniu: jeden wpis więcej w dzienniku, który ma ok. 12 tys. linii, choć inne zadanie go odchudza.

## Context

- Notatka, z której zadanie wyszło (stan wątku, szkic zdania, odrzucone warianty): the note the task came from, in the author's private notes.
- Przypadek z the-way, 2026-11-13, cykl `review-structure-form-class`: gałąź docelowa przyniosła WAY-355–WAY-359, gałąź zadania przesunęła swoje WAY-355–WAY-360 na WAY-360–WAY-365 osobnym commitem `c756236` (12 plików, jeden przebieg skryptem) przed scaleniem `3e934b6`; recenzent scalenia dał `PASS`.
- W tym samym cyklu zapis mówi: „Every report and handoff of this record before this row names the entries by their old numbers WAY-355 to WAY-360” (`7965305:docs/task-cycles/review-structure-form-class/cycle.md:58`), a uwaga procesowa orkiestratora: „the step that gives the next free number reads the log of the base only, with no way to see the numbers a running cycle on another branch has taken” (tamże, linia 145).
- Przypadek z loop2 (PR #25): cykl przesunął D-50–D-65 na D-57–D-72, numerów z `main` nie ruszył, przenumerowanie dał osobnym commitem przed scaleniem; spec, plan i raporty zostały z D-50–D-65, a na początku zapisu cyklu stanęła notka z przeliczeniem (stary + 7).
- Spec, plan, przekazania i raporty cyklu leżą do kroku 12 tylko w `.runs/task-cycles/<task-slug>/`; do repozytorium trafia ich kopia dopiero po scaleniu gałęzi docelowej (krok 12, akapit o „The record before it is committed”), więc da się je przenumerować, zanim kopia powstanie.
- Gałąź zadania jest wypychana dopiero w kroku 12, więc numerów zajętych przez cykl na innej gałęzi nie widać przy ich nadawaniu — zapobiec zderzeniu sprawdzaniem cudzych gałęzi się nie da.
- Korekta po uwagach do PR-a też scala gałąź docelową (`task-cycle/skill/correction.md`, akapit, który zaczyna się od „Take a link to the request”, i akapit „In the-way itself, before anything else”); tak wraca do uzgodnienia PR, który Mariusz scala po innym PR-ze dopisującym decyzje.
- Inne wpisy fundamentu (niezmienniki, pojęcia słownika, fakty o otoczeniu, części mapy) mają identyfikatory-nazwy, nie kolejne numery; zderzenie nazw to zderzenie znaczeń, nie numeracji, i tego zadanie nie dotyczy.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-19 — How are decisions numbered?** „A number stands for the question a decision answers, carries the product's prefix and is given in the order entries are written; a new question gets the next free number, and a new rule next to an existing decision is a new question.” Zadanie zasady nie zmienia — numer nadawany przy scaleniu, a wcześniej tymczasowy znacznik, odpadł w notatce źródłowej.
- **WAY-02 — How does whatever depends on an entry refer to it?** „Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to it by that identifier alone (…) and names an entry the foundation holds.” Dlatego przenumerowanie przepisuje każde odwołanie do przenumerowanej decyzji.
- **WAY-306 — What does the review of the merge of the target branch ask?** „Where merging the current target branch into the task branch changes the code the cycle reviewed, the dispatch of the fresh reviewer of the merge asks whether the two sides, the task branch and what the merge brought in, still hold together (…).” Jej *Rejected* nazywa przenumerowanie decyzji zmianą, przy której węższe pytanie dałoby fałszywy alarm. Zadanie jej nie zmienia.
- **WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?** Uwagi procesowe zapisu muszą trzymać pozycje raportów „word for word”; przenumerowanie raportów musi więc objąć te same pozycje w uwagach procesowych. Zadanie jej nie zmienia.
- **WAY-357 — Where does the cycle record the cause of a correction after the request opened?** „The human's remarks of a correction are written word for word into that file (…).” Uwagi Mariusza ze starymi numerami zostają, jak je napisał. Zadanie jej nie zmienia.
- **WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?** „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217 (…).” Część `task-cycle` jest w jej zakresie, więc zadanie nie czeka na wytyczne.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy gałąź docelowa zajęła numery nowych decyzji gałęzi zadania, gałąź zadania — w kroku 12 i przy scaleniach korekty — przed scaleniem, osobnym commitem, przenumerowuje swoje decyzje na kolejne wolne numery po numerach gałęzi docelowej, nigdy numerów gałęzi docelowej, razem z każdym odwołaniem w plikach gałęzi i w zapisie cyklu w stanie sprzed wpisania uzgodnienia; odrzucone: przenumerowanie gałęzi docelowej, tymczasowy znacznik do scalenia, stare numery w zapisie cyklu, podglądanie cudzych gałęzi. | decision | pytania 1, 3 i 4 pod *Questions to settle* (wybór Mariusza) | czy reguła i jej odrzucone warianty stoją w dzienniku, czy tylko w skillu, i czy przenumerowanie obejmuje zapis cyklu oraz korektę |
| 2 | Przeliczenie starych numerów na nowe stoi tylko we wpisie dziennika zdarzeń cyklu, który odnotowuje uzgodnienie z gałęzią docelową, bez notki na początku zapisu. | decision | pytanie 2 pod *Questions to settle* (wybór Mariusza) | czy dać notkę z przeliczeniem na początku zapisu, jak w loop2, czy pominąć przeliczenie |

## Out of scope

none
