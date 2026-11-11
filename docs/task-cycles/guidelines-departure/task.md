---
title: "the way: decyzja, że samo the way odchodzi od wytycznych kodowania i testów"
status: draft
created: 2026-10-24
updated: 2026-11-11
tags: [the-way, zadanie]
related: ["the project note of the process of work on a product"]
---

## Po co to

- **Jak jest dziś:** Zadania rozwijające the way — narzędzie opisujące proces pracy nad produktami — przechodzą dalej bez własnych wytycznych kodowania i testów, choć od produktów ten proces wymaga takich wytycznych przed rozpoczęciem pracy. Instrukcja pracy nad samym the way pozwala prowadzić zmiany osobną drogą, ale nie rozstrzyga wprost, czy zwalnia to z obowiązku posiadania wytycznych.
- **Kto to odczuwa:** Agent przygotowujący zadanie the way musi ustalić, czy może przekazać je do wykonania, czy powinien poczekać na napisanie wytycznych. Mariusz ma rozstrzygnąć, czy przygotować własne wytyczne, zapisać uzasadniony wyjątek, czy ograniczyć obowiązek do produktów korzystających z the way.
- **Co jeśli nic:** Pytanie wraca przy każdym zadaniu the way, które zmienia skrypty albo testy — 11 listopada Mariusz musiał na nie odpowiadać przy przygotowaniu innego zadania. Agent, który nie zapyta, albo zatrzyma zadanie bez końca, albo przepuści je bez żadnej zapisanej podstawy.


# the way: decyzja, że samo the way odchodzi od wytycznych kodowania i testów

Status: ready for cycle
Project relation: independent

## Description

### Need

- the way jest jednocześnie procesem dla produktów i repozytorium z własnym kodem: 18 skryptów w Pythonie (np. `elements/common/foundation_check.py`, `installation/install.py`, `gate/run_tests.py`) i 29 plików testów do nich. W tym sensie samo the way jest produktem, który the way prowadzi.
- the way ma regułę dla produktów (WAY-215): zadanie, które pisze kod w produkcie bez ogólnych wytycznych kodowania albo pisze lub zmienia test w produkcie bez wytycznych testów, czeka w doprecyzowaniu, aż osobne zadanie je napisze.
- Samo the way nie ma ani `guidelines/coding.md`, ani `guidelines/testing.md`, ani decyzji, która by od nich świadomie odchodziła (WAY-217 dopuszcza takie odejście, ale tylko decyzją). Gdyby agent doprecyzowujący zadanie the way stosował regułę dosłownie, każde zadanie the way z kodem albo testami stanęłoby w miejscu.
- W praktyce dotychczasowe zadania the way — także te, które pisały wytyczne styleguide'a, kodowania i testów — szły dalej drogą opisaną w `agent-instructions/README.md`, bez czekania. Gdzie pytanie padło wprost, rozstrzygał je Mariusz dla jednego zadania, a dziennik decyzji the way tego nie zapisuje.
- Odbiorcą jest agent, który doprecyzowuje albo wykonuje zadanie the way, i Mariusz, który decyduje, czy the way ma podlegać własnym regułom wytycznych.

### To do

1. Dziennik decyzji the way (`foundations/decisions.md`) ma decyzję, która odchodzi od ogólnych wytycznych kodowania (`guidelines/coding.md`) i od wytycznych testów (`guidelines/testing.md`) dla samego the way, bez terminu ważności, a jej *Scope* wymienia wszystkie 16 części mapy części the way.

### Questions to settle

- Która droga: (a) the way pisze własne `guidelines/coding.md` i `guidelines/testing.md`, jak każdy produkt; (b) decyzja w dzienniku the way odchodzi od wytycznych kodowania i testów dla samego the way (WAY-217); (c) WAY-215 mówi wprost, że dotyczy produktów, a nie samego the way?
  - Answer: (b) — decyzja w dzienniku the way odchodzi od wytycznych kodowania i testów dla samego the way, bez terminu ważności; gdyby kiedyś własne wytyczne zaczęły się opłacać, osobne zadanie je napisze i tę decyzję wycofa.
  - Not chosen:
    - (a) własne `guidelines/coding.md` i `guidelines/testing.md` — duże zadanie: audyt ok. 20 tys. linii i 29 plików testów, dobór narzędzi z próbnym przebiegiem, zmiana WAY-09 i przypisanie `guidelines/` do części; do jego scalenia każde zadanie the way z kodem czeka; zysk dotyczy głównie kodu, który już istnieje i trzeba by go sprzątać.
    - (c) WAY-215 i odczyt wytycznych mówią wprost, że reguła nie dotyczy samego the way — wyjątek dla the way trafia do tekstu, który przypina każdy produkt, a the way, które gdzie indziej traktuje siebie jak produkt, przestaje nim być bez decyzji w swoim dzienniku; ten sam skutek co (b) w gorszym miejscu.
  - Source: Mariusz, 2026-11-11, „b” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (b) bez terminu ważności).
- Jaki zasięg ma odejście — które części mapy części the way wymienia decyzja?
  - Answer: wszystkie 16 części mapy: decisions, part-map, relation-model, invariants, glossary, environment-facts, elements-common, project-level, task-cycle, foundation-review, gate, repository, agent-instructions, instruction-files, installation, product-guidelines; powód odejścia dotyczy całego the way, nie katalogów, w których dziś jest kod. Odejście obejmuje wytyczne kodowania i testów, nie styleguide.
  - Not chosen:
    - tylko 9 części z dzisiejszym kodem w Pythonie (agent-instructions, elements-common, part-map, gate, installation, instruction-files, project-level, relation-model, task-cycle) — pierwszy skrypt albo test w innej części znów stawia pytanie i wymusza rozszerzenie decyzji.
  - Source: Mariusz, 2026-11-11, „2” (odpowiedź na pytanie z zasięgami (1) i (2) i rekomendacją (2)).

## Context

- Skąd ten temat: znalezisko z doprecyzowania zadania the way: testy jako osobna dyscyplina wytycznych produktu (2026-10-24) — odczyt wytycznych (`product-guidelines/reading.md`) przy zadaniu the way pokazał brak wytycznych samego the way; tamto zadanie poszło dalej drogą z `agent-instructions/README.md`, jak wcześniejsze zadania the way.
- Pytanie padło też przy doprecyzowaniu zadania zbiorczego z uwag cykli (Origin, kolejność bramki, uwagi, Rests on): „Czy brak własnych wytycznych kodowania i testów the way wstrzymuje to zadanie (WAY-215), skoro zmienia skrypty i testy?” — odpowiedź Mariusza 2026-11-11: „a”, czyli „nie wstrzymuje — zadanie idzie jak dotychczasowe zadania the way” (`_zadania/zadanie_the_way_zbiorcze_origin_bramka_uwagi_rests_on.md`, *Questions to settle*).
- Kod the way na `foundations` `e3825a8`: ok. 20 tys. linii Pythona, wyłącznie biblioteka standardowa, testy na `unittest`, uruchamiane jednym poleceniem `python -B gate/run_tests.py`; repozytorium nie śledzi konfiguracji lintera ani formattera (brak `pyproject.toml`, `ruff.toml`, `setup.cfg`). Pliki `.py` leżą w częściach: agent-instructions, elements-common, part-map, gate, installation, instruction-files, project-level, relation-model, task-cycle.
- WAY-09 wylicza katalogi, które mogą stać na gałęzi głównej the way, i nie ma wśród nich `guidelines/`; niezmiennik `repository-file-location` (`foundations/invariants.md`) trzyma każdy śledzony plik w `foundations/` albo w katalogu, który WAY-09 nazywa. Droga (a) musi więc zmienić WAY-09 i przypisać `guidelines/` do części w mapie części.
- Sprawdzone: w repozytorium the way nie ma katalogu `guidelines/`, a w dzienniku decyzji nie ma decyzji, która odchodzi od wytycznych dla samego the way (przeszukanie `foundations/decisions.md` pod kątem „the-way itself”, „this repository”, „departs from”, `foundations` `e3825a8`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-215 — What happens to a task that needs missing discipline guidelines?: „Unless a departure under WAY-217 applies, a task changing a user interface with no styleguide, writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines, whether or not the product already has screens, code or tests, stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge of a separate guidelines task; refinement independent of that answer continues, and a task writing those guidelines does not wait for its own output.”
- WAY-217 — Does an approved departure count as missing guidelines?: „The shared reading of product guidelines treats no absent discipline file as missing for the affected part where a current decision of the product's log departs from those guidelines for that part, and applies that departure only within the scope the decision gives it.” *Rejected:* „a departure inferred by the agent — absence would authorize itself.”
- WAY-209 — When do a product's coding guidelines come into being?: „The skill `maintain-coding-guidelines` proposes that, in a product with no code, the general file of its coding guidelines, with its standing checks, comes into being before the first task that writes the product's code […]”
- WAY-244 — When do a product's testing guidelines come into being?: „The skill `maintain-testing-guidelines` proposes that a product's testing guidelines come into being before the first task that writes the product's tests.”

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | the way odchodzi od ogólnych wytycznych kodowania i od wytycznych testów dla samego the way, bez terminu ważności, we wszystkich 16 częściach swojej mapy części; gdyby własne wytyczne zaczęły się opłacać, osobne zadanie je napisze i tę decyzję wycofa. | decision | *Questions to settle*: „Która droga…” (b) i „Jaki zasięg ma odejście…” (2); drogi niewybrane w ich *Not chosen* | czy odejście jest czasowe (np. do utworzenia `main`), które części obejmuje i czy obejmuje też testy |
| 2 | Zmiana, która dodaje część do mapy części the way, dopisuje ją do *Scope* decyzji odejścia z wiersza 1. | decision | wyprowadzone z odpowiedzi „2” i z WAY-217 („applies that departure only within the scope the decision gives it”); przyjęte przez Mariusza 2026-11-11: „przyjmuję”; niewybrana droga: bez tego zdania pierwszy skrypt w nowej części znów stawia pytanie o brak wytycznych | czy nowa część mapy jest objęta odejściem, czy pytanie o brak wytycznych wraca przy pierwszym jej skrypcie |

## Out of scope

- odejście od styleguide'a — the way nie ma ekranów.
