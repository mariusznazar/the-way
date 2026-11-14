---
title: "the way: jak w decyzji stoi pomiar, którego źródło leży w prywatnych notatkach"
status: draft
created: 2026-11-13T20:22
updated: 2026-11-13
tags: [zadanie]
related: "the author's note of the project this task belongs to"
---

## Po co to

- **Jak jest dziś:** dwie zasady the way kłócą się ze sobą, gdy pomiar pochodzi z prywatnych notatek Mariusza. Szablon decyzji (wpisu w dzienniku decyzji the way, który mówi, co wiąże dalszą pracę i dlaczego) każe pomiar o agentach i modelach zapisać jako fakt środowiska razem ze źródłem. Druga zasada, zapisana jako decyzja WAY-27, zabrania wskazywać w repozytorium źródło, do którego czytelnik repozytorium nie sięgnie — a prywatne notatki są właśnie takim źródłem. Po scaleniu prośby o scalenie nr 109 trzy decyzje (WAY-229, WAY-164 i WAY-364) niosą liczby z eksperymentu z recenzentami bez źródła, które dałoby się otworzyć.
- **Kto to odczuwa:** agent, który pisze następną decyzję z pomiarem z prywatnych notatek, i recenzent, który ją ocenia — jeden recenzent uzna brak źródła za usterkę, inny nie, więc ta sama zmiana raz przejdzie, a raz dostanie rundę poprawek.
- **Co jeśli nic:** każda kolejna decyzja oparta na prywatnym pomiarze trafia na to samo zderzenie, a jego rozstrzygnięcie zależy od przypadku w recenzji. Nic się nie psuje od razu, ale koszt wraca przy każdym takim wpisie, a zbiór decyzji z liczbami „bez źródła” rośnie.

# the way: jak w decyzji stoi pomiar, którego źródło leży w prywatnych notatkach

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Dziennik decyzji the way ma dwie reguły, których przy pomiarze z prywatnych notatek nie da się spełnić naraz.
- Reguła pierwsza (WAY-90, powtórzona w szablonie decyzji i w szablonie faktów środowiska) każe, by *Based on* decyzji wskazywało wpis faktu środowiska dla każdego cytatu, którego zmiana podważyłaby decyzję — „a finding about agents or models”.
- Fakt środowiska musi mieć źródło w jednej z trzech form: wydanie z adresem, strona z kopią archiwalną albo odczyt z hosta (WAY-80); prywatna notatka nie jest żadną z nich.
- Reguła druga (WAY-27) zabrania wskazywać źródło, którego czytelnik repozytorium nie otworzy, i każe opisać we wpisie to, co widać tylko tam.
- WAY-05 pozwala, by uzasadnienie decyzji podało pomiar „with what was measured and under which conditions”, ale nie mówi, czy taki pomiar jest cytatem, dla którego WAY-90 wymaga faktu.
- Po prośbie o scalenie nr 109 decyzje WAY-229, WAY-164 i WAY-364 niosą w uzasadnieniu liczby z eksperymentu z recenzentami, z *Based on* bez faktu dla nich; autor zmiany i recenzent całej zmiany zgłosili to zderzenie, a recenzent odmówił oceny jako sprawy spoza zadania.
- Odbiorcy: agent piszący następną decyzję z prywatnym pomiarem i recenzent, który ją ocenia — dziś ocena zależy od tego, którą regułę recenzent przeczyta jako nadrzędną.

### To do

1. WAY-90 (zmieniona w miejscu, przez `record-decision`) mówi, że pomiar, który zrobili ludzie produktu i którego zapisu czytelnik repozytorium nie otworzy, nie jest cytatem *Based on*: stoi w *Rationale* z tym, co mierzono, i warunkami pomiaru, uzasadnienie mówi wprost, że pomiar jest własny i jego zapis jest niedostępny dla czytelnika, i nie zakłada się dla niego wpisu faktu środowiska (pytania 1 i 2).
2. Szablon decyzji `elements/decisions/template.md` — punkt, który otwiera „*Based on* names every source outside the product”, ok. linii 44 — i szablon faktów `elements/environment-facts/template.md` — sekcja „Which facts are written”, punkt, który otwiera „A decision's *Based on* names a fact entry”, ok. linii 45 — mówią to samo co WAY-90 po zmianie.
3. Każda decyzja, której uzasadnienie podaje wynik takiego pomiaru — wśród nich WAY-229, WAY-164, WAY-364 i WAY-312 — mówi w uzasadnieniu, że pomiar jest własny i jego zapisu czytelnik nie otworzy; ich zdania wiążące i pola zostają bez zmian (pytanie 3).

### Questions to settle

- 1. Jak w dzienniku decyzji stoi pomiar, który zrobili ludzie produktu (autor procesu i jego agenci) i którego zapisu czytelnik repozytorium nie otworzy?
  - Answer: wynik zostaje w uzasadnieniu decyzji, z tym, co mierzono, i warunkami pomiaru; nie zakłada się dla niego wpisu faktu środowiska. Zmienia WAY-90 i dwa szablony (jedno zdanie, że własny pomiar nie jest cytatem); WAY-27 i WAY-05 zostają bez zmian.
  - Not chosen:
    - streszczenie pomiaru z warunkami w publicznym repozytorium jako plik, a fakt środowiska wskazuje ten plik pod stałym adresem commita — zmienia WAY-80 (nowa forma źródła), dodaje nowy rodzaj pliku i regułę, czego streszczenie nie może nieść; najwyższy koszt: streszczenie i czyszczenie przy każdym eksperymencie, przepisanie trzech decyzji i nowe fakty
    - wynik bez źródła z dopiskiem „prywatne notatki autora procesu” — zmienia WAY-27, którego *Rejected* odrzuca to wprost; tanie, ale daje czytelnikowi odesłanie donikąd
    - nic nie zmieniać — każda kolejna decyzja z prywatnym pomiarem trafia na to samo zderzenie, a wynik recenzji zależy od tego, którą regułę recenzent uzna za nadrzędną
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13: „1 a, 2 a”
- 2. Czy uzasadnienie decyzji ma wprost mówić, że pomiar jest własny i jego zapis jest niedostępny dla czytelnika?
  - Answer: tak, nowa reguła tego wymaga, żeby recenzent po samym tekście odróżnił własny pomiar od cytatu, któremu zabrakło faktu; cykl dopisuje to sformułowanie w decyzjach, które już niosą taki pomiar.
  - Not chosen:
    - bez takiego zdania, sama reguła, że własny pomiar nie dostaje faktu — zero zmian w istniejących decyzjach, ale recenzent dalej zgaduje, czy liczba bez źródła to pomiar własny czy przeoczony cytat, czyli wraca niejednoznaczność, którą zadanie usuwa
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13: „1 a, 2 a”
- 3. Czy decyzje, które już niosą taki pomiar (WAY-229, WAY-164, WAY-364 i inne, np. WAY-312), poprawić według nowej zasady od razu, czy zostawić?
  - Answer: tak, w tej samej zmianie — odpowiedź daje fundament: autor zmiany wpisu fundamentu przeszukuje raz cały fundament w poszukiwaniu wpisów, których zmiana dotyczy, i każde znalezisko staje się poprawką jednego z wpisów w tej samej zmianie, linkiem albo pytaniem do człowieka.
  - Source: `foundations/decisions.md`, WAY-33, rewizja `715ae20` — "When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches […] and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human."

## Context

- Pozycja pochodzi z komentarza „Uwagi doradcy dnia w imieniu Mariusza” pod prośbą o scalenie https://github.com/mariusznazar/the-way/pull/109, pozycja 2 (pierwotna notatka zadania podawała część opisu „Fix or let through”, gdzie tej pozycji nie ma): „Three decisions carry numbers of the experiment with reviewers with no source a reader can open (the template's rule on measurements collides with WAY-27 for a private source). Not fixed here: the doradca makes a task of it in the author's notes; let it through in this request.”
- Rekomendację, by zrobić z tego zadanie, przyjął 13.11 wieczorem doradca dnia w imieniu Mariusza, gdy Mariusz był poza komputerem; doprecyzowanie miało ją przejrzeć i ją utrzymało (w pytaniu 1 droga „nic nie zmieniać” nie została wybrana).
- Zadanie, które dało decyzje z pomiarem, ustaliło już w swoim doprecyzowaniu: „Uzasadnienie decyzji może podać pomiar z tym, co mierzono i w jakich warunkach (WAY-05), ale nie wskazuje źródła, którego czytelnik repozytorium nie otworzy (WAY-27); raport z eksperymentu leży w prywatnych notatkach, więc wynik opisuje się we wpisie, a *Origin* zostaje `none`.” — the author's earlier task note on the review of the whole change. Nie rozstrzygnęło, co z regułą WAY-90.
- Repozytorium the way jest publiczne (`gh repo view`, 2026-11-13: `PUBLIC`), więc wszystko, co trafi do repozytorium, czyta każdy.
- `Defect introduced by: none`: zderzenie stoi w samym fundamencie (WAY-90 wobec WAY-27 i WAY-05), a prośba nr 109 zrobiła to, co jej zadanie kazało; to luka reguł, nie wada wobec tego, czego fundament wymagał przy scaleniu.
## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?** Zmieniana przez to zadanie (wiersze 1 i 2 *Settlements to record*): własny pomiar, którego zapisu czytelnik nie otworzy, nie jest cytatem i nie dostaje faktu. Brzmienie dziś: „A decision's *Based on* quotes every source outside the product that the decision rests on with its address, the place in it, the passage word for word and the date it was read; once the environment facts element has entries, it names instead a fact entry, by its identifier alone, for every citation that, once it stopped being true, would call the decision into question — a finding about agents or models, the behaviour of a tool the process uses.”
- **WAY-27 — Where may this repository point for its reasoning?** Bez zmiany; z niej wynika, że wynik opisuje się we wpisie, a źródła się nie wskazuje: „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks and the rules of that place, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else, each by an entry of the locations file of WAY-320 and never by a path.”
- **WAY-05 — How is a decision entry written?** Bez zmiany; pozwala na pomiar w uzasadnieniu: „[…] rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count — a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound — nor what the process's own tools do or lack today, and does not tell how the decision was reached.”
- **WAY-80 — What is an environment fact's source?** Bez zmiany; prywatna notatka nie jest żadną z jej form: „Every environment fact entry names its source: an edition with its publisher's own address, or a page without editions with its closest archived copy, giving the place, the passage word for word and the date read. A state of a host the product's people run, which no page shows and only those with access to the host can read, has for its source a reading […]”.
- **WAY-33 — What does the author of a foundation change search for?** Bez zmiany; daje odpowiedź na pytanie 3: „When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches […] and before the change is accepted each finding becomes a link, a change to one of the entries in the same change, or a question to a human.”
- **WAY-229 — On which class of model do the executor of a slice and the one author work?** Uzasadnienie dostaje zdanie, że pomiar klasy recenzenta jest własny i jego zapis niedostępny (punkt 3 *To do*); zdania wiążące bez zmiany. Uzasadnienie dziś: „A measurement of the class of the reviewer: on four merged changes of one product, of 959 to 1740 added lines each, two runs of each variant on each change, which is 8 runs a variant; […]”.
- **WAY-164 — What does the author of a change check of its own work before review?** Jak WAY-229 (punkt 3 *To do*); *Rejected* dziś: „a review without the author's report — a reviewer of the orchestrator's class without the report caught 4 and 3 of the 14 reference errors, with the report 5 and 6, […]; the conditions of the measurement stand in WAY-229.”
- **WAY-364 — How does a reviewer grade a finding that a foundation entry departs from the form of its template?** Jak WAY-229 (punkt 3 *To do*); uzasadnienie dziś: „the same remark on the form of an entry was graded blocking in 9 runs of an experiment with reviewers and Minor in 8, and 6 of its 32 runs rejected the change for its form alone (the conditions of the measurement stand in WAY-229) […]”.
- **WAY-312 — Which sentences does a rule of a product's guidelines not hold?** Jak WAY-229 (punkt 3 *To do*); uzasadnienie dziś: „A trial on the guidelines of one product gave no ground for going further: on three tasks with hidden tests, five runs each of the model Sonnet 5.5, the tests passed 45 of 45 times […]”.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Pomiar, który zrobili ludzie produktu i którego zapisu czytelnik repozytorium nie otworzy, nie jest cytatem *Based on*: stoi w uzasadnieniu decyzji z tym, co mierzono, i warunkami pomiaru, bez wpisu faktu środowiska. | decision | pytanie 1 (wybór spośród pokazanych dróg) | czy dla liczb eksperymentu z recenzentami założyć fakt środowiska, opublikować streszczenie, czy dopisać odesłanie do prywatnych notatek |
| 2 | Uzasadnienie z takim pomiarem mówi wprost, że pomiar jest własny i jego zapisu czytelnik nie otworzy. | decision | pytanie 2 (wybór spośród pokazanych dróg) | czy dopisywać to zdanie w WAY-229, WAY-164, WAY-364 i WAY-312, czy zostawić je bez niego |

## Out of scope

none
