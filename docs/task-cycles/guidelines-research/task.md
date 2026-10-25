---
title: "the way: research i rekomendacja narzędzia spójne w trzech skillach wytycznych"
status: draft
created: 2026-10-25
updated: 2026-10-25
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]", "[[wytyczne_produktu_testy]]"]
---

# the way: research i rekomendacja narzędzia spójne w trzech skillach wytycznych

Status: ready for cycle
Project relation: independent

## Description

### Need

- Trzy skille wytycznych — `maintain-coding-guidelines`, `maintain-styleguide`, `maintain-testing-guidelines` — robią research dla technologii produktu w różnych chwilach: kodowanie i styleguide przy każdym odświeżeniu i rozbudowie wytycznych (WAY-211, WAY-186), testy tylko wtedy, gdy człowiek nie ma preferencji (WAY-249).
- Research przy odświeżeniu nie ma sensu: gdy przyjęte wytyczne, np. dla pytesta, się aktualizuje albo koryguje, nic nie trzeba badać; badać warto przy rozbudowie, gdy wytyczne obejmują coś nowego — np. nową warstwę testów — i trzeba sprawdzić, czy dobrze użyć tego, co produkt już ma, czy czegoś innego.
- Nowe narzędzie, które skill wytycznych zostawia człowiekowi jako wybór technologii, dostaje rekomendację według trzech różnych reguł: kodowanie — najczęściej używane w technologii produktu (WAY-210), styleguide — bez kryterium (WAY-185), testy — bez rekomendacji (WAY-248); krok technologii projektu pokazuje opcje przez skutki dla produktu i przy remisie rekomenduje najprostszą i najtańszą (WAY-123).
- Odbiorcą jest Mariusz, który zatwierdza wybory wytycznych i nie wybierze narzędzia sam — rekomendacja musi być, a skille są uniwersalne, więc reguła ma być jedna dla wszystkich trzech.

### To do

1. Trzy skille wytycznych robią research dla technologii produktu przy pierwszych wytycznych dyscypliny (gdy człowiek nie ma preferencji, jak dziś) i przy każdej rozbudowie, a nie robią go przy odświeżeniu: WAY-186, WAY-211, WAY-249 i krok 2 trzech skilli (`product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md`).
2. Rozróżnienie odświeżenia od rozbudowy stoi w the way: odświeżenie to aktualizacja albo korekta przyjętych wytycznych w zakresie, który już obejmują; rozbudowa to objęcie wytycznymi czegoś nowego — np. nowej warstwy testów — gdzie research sprawdza, czy użyć tego, co produkt ma, czy czegoś innego.
3. Nowe narzędzie albo biblioteka, które skill wytycznych zostawia człowiekowi jako wybór technologii — linter, formater, audyt zależności, biblioteka komponentów albo nowy sposób stylowania, narzędzie testów, biblioteka testów własności — dostaje rekomendację tak, jak krok technologii projektu pokazuje opcje: przez skutki dla produktu, z rekomendacją i słabym punktem opcji rekomendowanej, przy remisie najprostsza i najtańsza (WAY-122, WAY-123): WAY-185, WAY-210, WAY-248 i odpowiednie miejsca trzech skilli.

### Questions to settle

- Czy wyrównać research i rekomendację narzędzia skilla testów z pozostałymi skillami wytycznych?
  - Answer: tak.
  - Source: Mariusz, 2026-10-25: „wyrównajmy to proszę” — na drogi: zostawić albo wyrównać, z rekomendacją wyrównania.
- Kiedy skill wytycznych robi research — przy odświeżeniu, przy rozbudowie, czy przy obu?
  - Answer: przy rozbudowie, nie przy odświeżeniu, spójnie w trzech skillach.
  - Source: Mariusz, 2026-10-25: „przy rozbudowie tak, ale przy odświezeniu to nie ma sensu”; „jeśli przyjęliśmy wytyczne np. dla pytesta i chcemy je zaktualizować czy skorygować, to po cholerę robić jakikolwiek research? jeśli byśmy chcieli wprowadzić nową warstwę testów to wtedy warto to zbadać czy dobrze uzyć tego co już mamy, czy czegoś innego - tak rozumiem rozbudowę i generalnie chciałbym, żeby to było spójne również w wytycznych kodowania i styli” — na drogi: (a) wszędzie tylko przy rozbudowie, (b) wszędzie przy obu, z uzasadnieniem WAY-211 („Tools and their recommended sets move, so refreshed coding guidelines are set against them again.”) pokazanym przed odpowiedzią.
- Według jakiego kryterium skill wytycznych rekomenduje nowe narzędzie?
  - Answer: tak jak krok technologii projektu (WAY-122, WAY-123), we wszystkich trzech skillach, z WAY-210 włącznie; rekomendacja musi być.
  - Source: Mariusz, 2026-10-25: „musi być rekomendacja, bo i tak nie będę w stanie wybrać, ale czekaj - robimy to w uniwersalnym skillu, więc powinno być uniwersalnie”; „opcja b będzie lepsza” — na drogi: (a) testy jak kodowanie, „najczęściej używane w technologii”, (b) narzędzia w skillach wytycznych przez kryterium kroku technologii, z rekomendacją (b).
- Czy rozróżnienie odświeżenia od rozbudowy i rekomendacja przez skutki trzymają się wobec przypadków granicznych?
  - Answer: ustalenia przyjęte bez zmian; dostosowanie wytycznych do nowej wersji narzędzia, które produkt już ma, jest aktualizacją w zakresie, który wytyczne obejmują — odświeżeniem bez researchu; przy pierwszych wytycznych kodowania trzy wybory narzędzi (linter, formater, audyt zależności) idą każdy przez skutki dla produktu z rekomendacją.
  - Source: pytania kontrolne agenta, 2026-10-25 — (1) nowa główna wersja pytesta zmienia zalecany sposób pisania testów: odświeżenie czy rozbudowa?; (2) WAY-210 *Rationale* „a product with no standing check meets three such choices at once, so the skill recommends the tool most used in the technology, which the human can take as offered” wobec drogi (b); Mariusz, 2026-10-25: „przyjmuję ustalenia” — bez zmiany ustaleń.

## Context

- Dziś: krok 2 `product-guidelines/coding/SKILL.md:136-155` i `product-guidelines/styleguide/SKILL.md:117-132` robią research „where the human has none, and at every refresh or extension”; `product-guidelines/testing/SKILL.md:125-143` — przy odświeżeniu pyta o preferencje i bada tylko „where the human has none” (`foundations` `2895e0e`).
- „Odświeżenie” i „rozbudowa” stoją w the way zawsze razem („refreshed or extended”) — w decyzjach WAY-185, WAY-186, WAY-210, WAY-211, WAY-247–WAY-249 i w opisach trzech skilli; żaden wpis ich nie rozróżnia.
- Uzasadnienie researchu przy odświeżeniu, które zadanie znosi: WAY-211 *Rationale* „Tools and their recommended sets move, so refreshed coding guidelines are set against them again.”; *Verification* WAY-211 liczy jako naruszenie „an extension reuses the first research”.
- Uzasadnienie kryterium „najczęściej używane”, które zadanie zastępuje: WAY-210 *Rationale* „The human is no developer, and a product with no standing check meets three such choices at once, so the skill recommends the tool most used in the technology, which the human can take as offered […] and how widely an option is used within its family bears on how well an agent works with it (WAY-122).” Szerokie użycie zostaje jedną z cech, po których WAY-122 waży opcję.
- W skillu kodowania narzędzie, które człowiek woli, jest proponowane, a żadne inne nie stoi w jego miejscu (krok 2: „A tool the human prefers is the one proposed, and no other is offered in its place”).
- Skąd rozjazd testów: recenzja specu cyklu `testing-guidelines` (uwaga F5) uznała powtórny research za nieniesiony przez wiersz 23 zadania `wytyczne_produktu_testy`; zapis cyklu w `docs/task-cycles/testing-guidelines/` przy commicie `4b2cdb4`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Wybór: część `product-guidelines` (i `decisions`, `glossary` przez zmieniane wpisy); decyzje researchu i nowego narzędzia trzech skilli wytycznych oraz kroku technologii projektu (`foundations` `2895e0e`).

Zmieniane przez zadanie:

- WAY-185 — „[…] A new library of components or a new way of styling is a choice the skill leaves to the human as a question of the task, never one it settles. […]” Dostaje rekomendację jak w kroku technologii (punkt 3 *To do*).
- WAY-186 — „The skill `maintain-styleguide` takes the starting rules of a styleguide written before the first screen of its user interface from the human's preferences for the technology of that user interface that the product's foundation settles, and, where the human has none, from research of the basic rules of a styleguide for that technology, […] proposes what the research finds without imposing it, and researches again whenever a styleguide is refreshed or extended.” Research przy rozbudowie, nie przy odświeżeniu (punkt 1).
- WAY-210 — „[…] A new linter, formatter or audit of dependencies is a choice the skill leaves to the human as a question of the task, never one it settles, recommending by default the tool most used in the product's technology, as research with sources shows it.” Kryterium kroku technologii zamiast „najczęściej używane” (punkt 3).
- WAY-211 — „The skill `maintain-coding-guidelines` takes the tools of the standing checks and a linter's set of rules from the human's preferences for the product's technology that the product's foundation settles, and, where the human has none, from research of each standing check for that technology, […]. It researches again whenever a product's coding guidelines are refreshed or extended.” Research przy rozbudowie, nie przy odświeżeniu (punkt 1).
- WAY-248 — „[…] A new test tool or a library of property tests is a technology choice the skill leaves to the human as a question of the task, never one it settles.” Dostaje rekomendację jak w kroku technologii (punkt 3).
- WAY-249 — „The skill `maintain-testing-guidelines` takes the starting set of a product's testing guidelines from the human's preferences, and, where the human has none, from research for the product's technology, […]. It proposes what the research finds without imposing it.” Research przy rozbudowie (punkt 1).

Wzór:

- WAY-122 — „The options of each technology choice a project needs come from research of that choice against the project definition, rather than from a fixed list of bundled stacks, […] An option the project's code is written in or against — a language, a framework, a library, a store of data — is weighed by whether its documentation shows that it uses explicit types, follows conventions of layout and naming and has current, versioned documentation, and whether a public record of its use, such as a package registry or a survey, shows it widely used within its language family; […] and every option is offered only after a critique that refutes every claimed difference between the options which no source supports.”
- WAY-123 — „The step that settles a project's technology shows the options of each choice by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs — and the human chooses between those consequences. A difference with no consequence for the product decides nothing, and where no difference with a consequence remains, the step recommends the simplest and cheapest option. […]”

Ograniczają zadanie:

- WAY-121 — „[…] a choice one task can make and change alone stays with that task.” Nowe narzędzie wytycznych zostaje wyborem zadania, nie kroku technologii projektu; zadanie bierze z kroku technologii tylko sposób pokazania i rekomendowania opcji.
- WAY-174 — skille wytycznych pokazują każdy wybór przez skutek dla produktu, prostym językiem.

## Settlements to record

Candidates: 5 shown, 4 accepted — 2026-10-25

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skille wytycznych kodowania, styleguide'a i testów robią research przy rozbudowie wytycznych, a przy odświeżeniu — aktualizacji albo korekcie przyjętych wytycznych — nie robią go. | decision | Questions to settle, odpowiedź 2 (Mariusz, 2026-10-25) | czy przy aktualizacji przewodnika dla pytesta znów uruchamiać agentów researchu |
| 2 | Rozbudowa to objęcie wytycznymi czegoś nowego — np. nowej warstwy testów — gdzie research sprawdza, czy użyć tego, co produkt ma, czy czegoś innego; odświeżenie to aktualizacja albo korekta w zakresie, który wytyczne już obejmują. | decision | Questions to settle, odpowiedź 2 (Mariusz, 2026-10-25: „tak rozumiem rozbudowę”) | czy zmiana wersji narzędzia albo dopisanie reguły to rozbudowa, czy odświeżenie |
| 3 | Nowe narzędzie albo biblioteka, które skill wytycznych zostawia człowiekowi jako wybór technologii, dostaje rekomendację tak, jak krok technologii projektu pokazuje opcje: przez skutki dla produktu, z rekomendacją i słabym punktem, przy remisie najprostsza i najtańsza — we wszystkich trzech skillach. | decision | Questions to settle, odpowiedź 3 (Mariusz, 2026-10-25: „opcja b będzie lepsza”) | czy linter i narzędzie testów rekomendować jako „najczęściej używane”, czy przez skutki dla produktu |
| 4 | Narzędzie, które człowiek woli, jest tym proponowanym, a research go nie wypiera — we wszystkich trzech skillach (propozycja z materiału). | decision | Context, krok 2 `product-guidelines/coding/SKILL.md` („A tool the human prefers is the one proposed, and no other is offered in its place”); przyjęte — Mariusz, 2026-10-25: „przyjmuję ustalenia” | czy przy rozbudowie research może zaproponować inne narzędzie zamiast preferowanego |

## Out of scope

- Wyrównanie innych różnic między trzema skillami wytycznych niż research i rekomendacja narzędzia — gdy się znajdą, osobne zadanie.
