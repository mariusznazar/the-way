---
title: "the way: dwie zmiany dziennika decyzji — odczyt jako źródło faktu o ustawieniu w cudzej usłudze, niezmiennik wskazuje miejsce swojego warunku — i test, że dopiski „decision pending” nie wracają"
status: draft
created: 2026-11-13T10:30
updated: 2026-11-13
tags: [zadanie]
related: the process-work project note in the author's backlog
---

## Po co to

- **Jak jest dziś:** Dwie reguły szablonów the way czekają na zmianę dziennika decyzji. Po pierwsze, fakt o ustawieniu, które widać tylko po zalogowaniu w cudzej usłudze (ochrona gałęzi w GitHubie, reguła w panelu Cloudflare), nie ma dozwolonej formy źródła: odczyt — polecenie, narzędzie, wynik słowo w słowo, data — przysługuje dziś tylko serwerom, które prowadzimy sami. To zawężenie wyszło przypadkiem z zakresu małego zadania 27.10.2026; szerszy wariant recenzent zostawił mnie do decyzji, a nikt mi go nie pokazał. Po drugie, szablon niezmienników każe niezmiennikowi wskazać wpis albo decyzję, w której leży jego warunek, ale żadna decyzja tego nie mówi, a dla decyzji samego the way nie ma pola, w którym dałoby się ją wskazać.
- **Kto to odczuwa:** Agent cyklu w loop2, gdy pierwszy raz oprze coś na ustawieniu w GitHubie albo Cloudflare — będzie wymyślał formę źródła sam, jak już raz było. Autor zmiany decyzji, który nie znajdzie niezmiennika trzymającego warunek w tej decyzji, bo niezmiennik jej nie wymienia.
- **Co jeśli nic:** Dziś nic się nie psuje: loop2 nie ma jeszcze faktu o ustawieniu w cudzej usłudze, a wszystkie 127 jego niezmienników wskazuje swoją decyzję w polu „Derives from”. Koszt przychodzi przy pierwszym takim przypadku — rozmowa o formie w środku cyklu i trwałe `TODO` na gałęzi głównej — oraz po cichu, gdy zmieni się decyzja trzymająca warunek niezmiennika, który jej nie wymienia.

# the way: dwie zmiany dziennika decyzji — odczyt jako źródło faktu o ustawieniu w cudzej usłudze, niezmiennik wskazuje miejsce swojego warunku — i test, że dopiski „decision pending” nie wracają

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- W szablonach the way zostały dwa ostatnie dopiski `TODO — decision pending` (stan na `f749cfc`, gałąź `foundations`, po scaleniu PR #110): w `elements/environment-facts/template.md` w sekcji „Source”, w punkcie, który otwiera „A setting on a host the product's people run that only its setter can read”, i w `elements/invariants/template.md` w sekcji „The sentence”, w punkcie, który otwiera „A condition that decides whether a commit makes the sentence true”.
- Fakt o ustawieniu, które ludzie produktu ustawili w cudzej usłudze i które widać tylko po zalogowaniu (ochrona gałęzi w GitHubie, reguła w panelu Cloudflare), nie ma dziś dozwolonej formy źródła: WAY-80 daje odczyt tylko dla hosta, który ludzie produktu prowadzą sami, a strona za logowaniem nie jest ani edycją, ani stroną z kopią archiwalną.
- Szablon niezmienników każe niezmiennikowi wskazać wpis albo decyzję trzymającą jego warunek, ale WAY-60 tego nie mówi, a dla decyzji the way z przypiętego commita szablon nie daje pola (ten sam szablon mówi, że taka decyzja „is no decision entry of it”, WAY-58).
- Agenci loop2 dwa razy wymyślali sami zapis źródła, którego szablon faktów nie opisuje: cytat z kodu narzędzia pod stałym commitem oraz odczyt złożony z kilku poleceń albo z polecenia wielowierszowego; recenzent przepuścił oba za precedensem (AIR-642).
- Nic nie pilnuje, żeby dopiski `decision pending` nie wróciły do `elements/` po zamknięciu ostatniego.
- Odbiorcą są agenci piszący fakty i niezmienniki w produktach i w samym the way oraz autor zmiany decyzji, który szuka wpisów od niej zależnych.

### To do

1. WAY-80 daje odczyt jako źródło także dla ustawienia, które ludzie produktu ustawili w cudzej usłudze i którego nie pokazuje żadna strona otwarta bez ich dostępu; forma jak dla hosta: polecenie albo wywołanie API, usługa, narzędzie z wersją, wynik słowo w słowo (albo linie, na których stoi zdanie), data. Brzmienie zmiany stoi w *Decisions in play*.
2. WAY-84 mówi, że takie ustawienie ma odczyt za źródło (WAY-80), a jego *Rejected* odrzuca odczyt powtarzany — na zmianę albo według zegara — a nie jeden odczyt zacytowany.
3. WAY-80 mówi, że cytowany wynik odczytu nie zawiera sekretu, a polecenie czyta tylko pola, na których stoi zdanie faktu.
4. Szablon faktów: punkt z dopiskiem w sekcji „Source” zastąpiony regułą cytującą WAY-80 i WAY-84; forma odczytu w punkcie „A source takes one of three forms”, w akapicie otwierającym szablon i we wzorze pola *Source* obejmuje usługę i regułę o sekrecie; skill faktów (`elements/environment-facts/skill/draft.md`, punkt „*Source*”) mówi, jak zrobić odczyt w usłudze i jak zawęzić polecenie do pól, na których stoi zdanie, tak żeby wynik nie niósł sekretu; opis faktów w `README.md` (lista elementów fundamentu i wiersz `environment_facts.md` tabeli plików) obejmuje odczyt w usłudze.
5. WAY-80 mówi, że odczyt to jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało; polecenie wielowierszowe stoi w bloku kodu pod *Source*, a każde narzędzie, od którego zależy wynik, ma podaną wersję. Zmiana idzie razem z punktem 1 (WAY-80 mówi dziś „the command” w liczbie pojedynczej); szablon faktów — punkt o odczycie w „A source takes one of three forms” i wzór pola *Source* — mówi to samo.
6. Szablon faktów, w sekcji „Source”, mówi, jak cytować kod pod stałym commitem: miejsce to symbol — funkcja, klasa albo stała — w którym stoi fragment; cytat to jedna instrukcja albo linia kodu słowo w słowo, z białymi znakami ściśniętymi do jednej spacji, a kilka cytatów łączy ` · `; fragment zawierający `"` stoi w “…”. To tekst szablonu, bez zmiany dziennika.
7. WAY-60 dostaje zdanie: niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje identyfikatorem wpis albo decyzję, która ten warunek trzyma — w polu, jeśli szablon takie daje, a inaczej w samym zdaniu. Szablon niezmienników: dopisek znika, a reguła cytuje WAY-60.
8. Nowy niezmiennik the way w `foundations/invariants.md`: żaden plik, który git śledzi pod `elements/`, nie zawiera tekstu „decision pending”; metoda `test`, wyprowadzony z WAY-35. Test uruchamiany przez `python -B gate/run_tests.py` cytuje go linią `invariant: <identyfikator>` i nie przechodzi, gdy taki plik się pojawi.

### Questions to settle

- Który wariant zamyka sprawę źródła ustawienia czytanego po zalogowaniu w cudzej usłudze?
  - Answer: (a) — odczyt jest źródłem także dla ustawienia w cudzej usłudze (zmiana WAY-80 i WAY-84), z regułą o wycinaniu sekretów z cytowanego wyniku.
  - Not chosen:
    - (b) strona bez edycji, bez kopii archiwalnej: adres strony ustawień, co pokazywała, data — nikt poza autorem nie porówna źródła z cytatem, a „passage word for word” z panelu klikanego ręcznie łatwo zmyślić.
    - (c) takiego faktu się nie pisze, dopóki produkt go nie potrzebuje — trwałe `TODO` na gałęzi głównej produktu, który ma takie ustawienie, i forma wymyślana przez agentów w międzyczasie.
  - Source: Mariusz, 2026-11-13, notatka „rozstrzygniecia_mariusza.md”, sekcja „Sprawa 3” — „S26: wariant (a) — odczyt jako źródło także dla ustawienia w cudzej usłudze (WAY-80, WAY-84), z regułą o wycinaniu sekretów z cytowanego wyniku.”; warianty i ich koszty: raport „otwarte_decyzje_the_way.md”, blok S26.
- Który wariant zamyka sprawę wskazania wpisu albo decyzji trzymającej warunek niezmiennika?
  - Answer: (a) — jedno zdanie w WAY-60.
  - Not chosen:
    - (b) tekst własny szablonu w obecnym brzmieniu — zestaw powiązań z WAY-17 przestaje być kompletny, a przypadek decyzji z przypiętego the way zostaje niewykonalny.
    - (c) usunąć obowiązek — cicho nieaktualne niezmienniki po zmianie decyzji.
  - Source: Mariusz, 2026-11-13, notatka „rozstrzygniecia_mariusza.md”, sekcja „Sprawa 3” — „S28: wariant (a) — zdanie w WAY-60.”; warianty i ich koszty: raport „otwarte_decyzje_the_way.md”, blok S28.
- Czy test, że dopiski nie wracają, wchodzi do tego zadania?
  - Answer: tak, po scaleniu zadania o dopiskach w szablonach (scalone jako PR #110, `f749cfc`).
  - Source: Mariusz, 2026-11-13, notatka „rozstrzygniecia_mariusza.md”, tabela „Partia działań sprawy 3” — „W4 (S26, S28), W7 | zadanie, `⛔` na zadanie powyżej (test W7 działa dopiero po zamknięciu ostatniego dopisku)”.
- Gdzie i jak stoi reguła, że zacytowany wynik odczytu nie zawiera sekretu?
  - Answer: (a) — zdanie w WAY-80: cytowany wynik nie zawiera sekretu, a polecenie czyta tylko pola, na których stoi zdanie faktu; skill faktów uczy, jak polecenie zawęzić.
  - Not chosen:
    - (b) zdanie w WAY-80, że sekret w cytowanym wyniku zastępuje znacznik, np. `<secret removed>` — pierwszy wyjątek od „słowo w słowo”; ktoś musi rozpoznać sekret, przeoczony token trafia do repozytorium, a znacznik daje fałszywe poczucie, że wynik sprawdzono.
    - (c) reguła tylko w szablonie i skillu faktów, bez zmiany dziennika — szablon dopowiada do „word for word” z WAY-80 coś, czego decyzja nie mówi; ten sam rodzaj rozjazdu, który sprzątał PR #110.
  - Source: Mariusz przez doradcę dnia, 2026-11-13 — „a (zdanie w WAY-80: cytowany wynik bez sekretu, polecenie czyta tylko pola, na których stoi zdanie faktu; skill faktów uczy zawężania).”
- Czy test z punktu 8 trzyma niezmiennik the way, czy stoi bez niego?
  - Answer: (a) — z niezmiennikiem: „No file git tracks under `elements/` holds the text `decision pending`”, metoda `test`, wyprowadzony z WAY-35.
  - Not chosen:
    - (b) sam test, bez wpisu — o jeden wpis mniej, ale pierwszy w the way test prawdziwych plików, którego fundament nie tłumaczy; kto go usunie albo osłabi, nie znajdzie śladu, po co był.
  - Source: Mariusz przez doradcę dnia, 2026-11-13 — „1 a, 2 a, 3 a.”
- Jak zapisać odczyt złożony z kilku poleceń w jednym wywołaniu i odczyt z poleceniem wielowierszowym?
  - Answer: (a) — odczyt to jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało; polecenie wielowierszowe stoi w bloku kodu pod *Source*; każde narzędzie, od którego zależy wynik, ma podaną wersję; WAY-80 dostaje to w zdaniu o odczycie.
  - Not chosen:
    - (b) odczyt to zawsze jedno polecenie w jednej linii, a każde kolejne to osobny fakt — 25-wierszowy skrypt nie ma formy, a odczyt wersji narzędzia staje się osobnym faktem, na którym nic nie stoi.
    - (c) wszystko w jednym fragmencie w backtickach, WAY-80 dostaje tylko liczbę mnogą — zero pracy, ale pokazany tekst dalej nie jest tym, co się wykonało.
  - Source: Mariusz przez doradcę dnia, 2026-11-13 — „1 a, 2 a, 3 a.”
- Jak cytować kod pod stałym commitem — czym jest „place”, czym „passage” i jak cytować fragment z `"`?
  - Answer: (a) — miejsce to symbol (funkcja, klasa albo stała), cytat to jedna instrukcja albo linia kodu słowo w słowo z białymi znakami ściśniętymi do jednej spacji, kilka cytatów łączy ` · `, fragment z `"` stoi w “…”; tylko tekst szablonu, bez zmiany WAY-80.
  - Not chosen:
    - (b) kod zawsze w backtickach — pęka na kodzie z backtickami (szablony tekstu w JS, Markdown) i różni się od formy cytatu ze strony `"…"`.
    - (c) `\"` wewnątrz zwykłych cudzysłowów — cytat przestaje być słowo w słowo, bo dochodzą ukośniki.
  - Source: Mariusz przez doradcę dnia, 2026-11-13 — „1 a, 2 a, 3 a.”

## Context

- Dopiski przy obu regułach to ostatnie dwa w `elements/` po PR #110; `git grep "decision pending" -- elements` na `f749cfc` daje dokładnie te dwa trafienia.
- Zawężenie odczytu do własnych hostów nie było zastrzeżeniem wobec usług: zadanie z 27.10.2026 dotyczyło tylko własnego serwera, recenzent zablokował szersze zamknięcie dopisku (uwaga B2) i dał dwa wyjścia do wyboru Mariusza, a autor wziął węższe bez pytania; raport „otwarte_decyzje_the_way.md”, blok S26.
- Brzmienie zmiany WAY-80 i WAY-84 pochodzi z raportu recenzenta z 27.10.2026, uwaga B2, wariant (a): „WAY-80 says "a state of a host the product's people run, or of a setting they set on another's service, which no page open without their access shows"; WAY-84 adds in its body that such a setting with no page open to a reader has a reading for its source (WAY-80), and its Rejected says the rejected re-read is a repeated one, not the one reading quoted”.
- Obawa o sekrety w dawnych kartach dotyczyła maszyny czytającej ustawienie cyklicznie cudzymi danymi logowania; cykliczne sprawdzanie faktów wycięło WAY-82, a jednorazowy odczyt właściciela konta tej obawy nie budzi — zostaje sam cytowany wynik, bo wyjście API potrafi nieść tokeny.
- loop2 cytuje już kod pod stałym commitem jako stronę edycji: miejsce to symbol (`§ makeResponse`, `§ DEFAULT_SELECTORS, complete list`), a fragment z `"` stoi w cudzysłowach typograficznych “…” albo z `\"` (`loop2` `origin/main` `fc00c406`, `foundations/environment_facts.md`, wpisy ze źródłami z `raw.githubusercontent.com` i `unpkg.com`).
- Uwagi z loop2 do punktu 4 zadania: `loop2@80d6bad:docs/task-cycles/repo-na-zrzuty/cycle.md:129` (kod jako źródło), `loop2@c2a9c61:docs/task-cycles/odtwarzanie-bazy-z-kopii/cycle.md:153` (trzy polecenia w jednym wywołaniu) i `:156` (polecenie 25-wierszowe w jednym fragmencie w backtickach, który skleja linie).
- Recenzent z 27.10.2026 proponował w uwadze M3: „Several lines of one output are quoted as several passages, joined by ` · `; an entry holds one reading, and a second command is a second fact.” — pierwsza połowa weszła do szablonu, druga nie.
- Poza szablonem formy źródła opisują `README.md` (lista elementów fundamentu, punkt o faktach, i wiersz `environment_facts.md` tabeli plików) — oba mówią o odczycie tylko dla hosta.
- the way odstępuje dla własnego kodu i testów od wytycznych kodu i testów produktu (WAY-328), więc test z punktu 8 nie czeka na wytyczne.
- Ani `foundation_check.py`, ani `migrate_foundation.py` nie rozpoznają formy `reading:` w *Source* (`git grep reading elements/common/*.py` na `f749cfc`).
- Raport, z którego zadanie wyszło: „otwarte_decyzje_the_way.md” (bloki S26 i S28, sprzeczności K8 i K9b, karty D4 i D7) w notatkach projektu; decyzje Mariusza z 13.11.2026: „rozstrzygniecia_mariusza.md”, sekcja „Sprawa 3”.

## Questions carried to cycle

- Czy `elements/common/foundation_check.py` czyta wpis faktu, którego pole *Source* ma pod sobą blok kodu z poleceniem wielowierszowym, czy wymaga poprawki (punkt 5).

## Human actions

none

## Decisions in play

- WAY-80 — „What is an environment fact's source?” — dziś: „A state of a host the product's people run, which no page shows and only those with access to the host can read, has for its source a reading: the command, the host it ran on and the tool with its version, its output word for word or the lines of it the sentence rests on, and the date run.” Zmiana, którą robi zadanie (pytania o wariant odczytu, o sekret i o odczyt z kilku poleceń): odczyt obejmuje też „a setting they set on another's service, which no page open without their access shows”, z poleceniem albo wywołaniem API i usługą; cytowany wynik nie zawiera sekretu, a polecenie czyta tylko pola, na których stoi zdanie faktu; odczyt to jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało, polecenie wielowierszowe w bloku kodu, z wersją każdego narzędzia, od którego zależy wynik.
- WAY-84 — „How is a setting that people of the product change outside its repository written?” — dziś: „The current state of a setting that people of the product change outside its repository — who can open it, a host's access rule — is an environment fact, its source the place where that state is shown.”; *Rejected*: „a method reading the setting where it lives, or a dated re-read by the person who sets it — a run and a record for every setting, as WAY-82 rejects for every fact.” Zmiana, którą robi zadanie (pytanie o wariant odczytu): takie ustawienie, którego nie pokazuje żadna strona otwarta bez dostępu ludzi produktu, ma odczyt za źródło (WAY-80); *Rejected* odrzuca odczyt powtarzany, a nie jeden odczyt zacytowany.
- WAY-60 — „Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?” — dziś: „A condition deciding an invariant stands in its sentence, or where changing it takes a foundation change a human decides, or where a decision in the product's log or the pinned the-way places it.” Zmiana, którą robi zadanie (pytanie o wskazanie warunku): niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje identyfikatorem wpis albo decyzję, która ten warunek trzyma — w polu, jeśli szablon takie daje, a inaczej w samym zdaniu.
- WAY-82 — „How does an environment fact keep up with what its source says?” — „An environment fact names no method and no status, no test cites it, no check of it runs, on a change or by a clock, and nothing fails when the world moves.” Zadanie go nie zmienia; odróżnienie w WAY-84 odczytu powtarzanego od jednego zacytowanego stoi na nim.
- WAY-35 — „What does an element's skill hold?” — „every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them”; jego *Rejected* odrzuca „each rule citing the decision that sets it — the rules are the-way's own text”. Z niego wyprowadza się niezmiennik z punktu 8.
- WAY-58 — szablon niezmienników, sekcja „Derives from”, punkt otwierający „Neither a source nor the place in the code”: „A decision named anywhere but the product's own log — a numbered decision in a concept document, a decision of the-way at the commit the product pins — is no decision entry of it (WAY-58).” Dlatego dla decyzji z przypiętego the way nie ma pola; zmiana WAY-60 każe ją wtedy wskazać w samym zdaniu.
- WAY-328 — „Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?” — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217”. Test z punktu 8 nie czeka więc na wytyczne.

## Settlements to record

Candidates: 7 shown, 6 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Odczyt — polecenie albo wywołanie API, usługa, narzędzie z wersją, wynik słowo w słowo, data — jest źródłem także dla ustawienia, które ludzie produktu ustawili w cudzej usłudze i którego nie pokazuje żadna strona otwarta bez ich dostępu. | decision (zmiana WAY-80, WAY-84) | *Questions to settle*, pytanie o wariant odczytu | czy zamknąć dopisek odczytem, stroną bez kopii archiwalnej, czy zostawić `TODO` |
| 2 | Odrzucony jest odczyt powtarzany, na zmianę albo według zegara, a nie jeden odczyt zacytowany. | decision (zmiana WAY-84) | *Questions to settle*, pytanie o wariant odczytu | czy zostawić *Rejected* WAY-84 w brzmieniu, które przeczy nowej formie źródła |
| 3 | Cytowany wynik odczytu nie zawiera sekretu, a polecenie czyta tylko pola, na których stoi zdanie faktu. | decision (zmiana WAY-80) | *Questions to settle*, pytanie o sekret | czy wycinać sekret znacznikiem, zawężać polecenie, czy opisać to tylko w szablonie |
| 4 | Odczyt to jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało; polecenie wielowierszowe stoi w bloku kodu, a każde narzędzie, od którego zależy wynik, ma podaną wersję. | decision (zmiana WAY-80) | *Questions to settle*, pytanie o odczyt z kilku poleceń | czy kolejne polecenie to osobny fakt, czy część jednego odczytu, i jak zapisać polecenie wielowierszowe |
| 5 | Niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje identyfikatorem wpis albo decyzję, która ten warunek trzyma — w polu, jeśli szablon takie daje, a inaczej w samym zdaniu. | decision (zmiana WAY-60) | *Questions to settle*, pytanie o wskazanie warunku | gdzie niezmiennik produktu wskazuje decyzję z przypiętego the way |
| 6 | Żaden plik, który git śledzi pod `elements/`, nie zawiera tekstu „decision pending”. | invariant | *Questions to settle*, pytanie o test | czy test stoi sam, czy cytuje niezmiennik, i z czego ten się wyprowadza |
## Out of scope

- Zmiana WAY-99 o słowie pokazywanym w innym języku — sprawa S27 zamknięta bez zmiany dziennika w PR #110.
- Wpis loop2 ze starszą formą źródła `observed:` (`mikrus-tunnel-outbound-tcp`) — należy do loop2.
