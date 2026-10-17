---
title: "the way: cykl zadania — koniec pętli recenzji i najsłabszy punkt autora"
status: draft
created: 2026-10-17
updated: 2026-10-17
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]", "[[wznowienie_limen_zmiany_w_the_way]]"]
---

# Cykl zadania: koniec pętli recenzji i najsłabszy punkt autora

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl zadania pozwala recenzentowi obejrzeć poprawkę jeden raz, ale nie mówi, co się dzieje, gdy ta ponowna recenzja też wypadnie negatywnie.
- Cykl nie mówi też, co zrobić z odrzuceniem, w którym wszystkie uwagi są nieblokujące, ani z uwagą, która poszerza zakres zadania.
- Autor zmiany pisze test przed kodem, ale nic nie każe mu szukać miejsca, w którym jego wynik najpewniej nie spełnia zadania; celowe złamanie robi recenzent i tylko dla testów niezmienników.
- Odbiorcą jest Mariusz, który dostaje request z cyklu: bez tych reguł pętla recenzji kończy się tam, gdzie ją zatrzyma orkiestrator, a błąd, który autor mógł złapać sam, kosztuje rundę recenzji.

### To do

1. Gdy ponowna recenzja poprawki wypadnie negatywnie, zadanie wraca do Mariusza jako zablokowane, z listą tego, co zostało, i kosztem; trzeciej rundy nie ma.
2. Odrzucenie, w którym wszystkie uwagi są nieblokujące, oznacza przejście do requestu bez naprawy.
3. Uwaga recenzji, która poszerza zakres zadania, staje się nowym zadaniem, a nie naprawą.
4. Przed oddaniem zmiany do recenzji autor wskazuje punkt zadania, który najpewniej nie jest spełniony, pisze sprawdzenie, które by to złapało, i raportuje jego wynik.

### Questions to settle

- Pytanie 1: na której ścieżce cyklu obowiązują punkty 1–3: tylko przy zmianie jednego autora, przy recenzji całej zmiany na obu ścieżkach, czy także w pętli poprawek każdej części planu?
  - Answer: przy recenzji całej zmiany na obu ścieżkach — recenzji zmiany jednego autora i końcowej recenzji całej gałęzi zmiany z planem; pętle poprawek pojedynczych części zostają takie, jak w Superpowers `subagent-driven-development`, a na końcu ścieżki z planem blokująca uwaga po ponownej recenzji daje zablokowany request zamiast rozstrzygnięcia orkiestratora. Odrzucone: tylko ścieżka jednego autora (orkiestrator dalej sam rozstrzyga pozostałe uwagi na ścieżce z planem); także każda część planu (zastępuje pięć rund Superpowers i zatrzymuje cykl na człowieku z powodu uwag do jednej części).
  - Source: Mariusz, 2026-10-17: „idziemy ścieżką b” — na drogę b przedstawioną w rozmowie doprecyzowania.
- Pytanie 2: która uwaga jest nieblokująca?
  - Answer: uwaga oznaczona przez recenzenta jako Minor; Critical i Important blokują, a uwaga wykraczająca poza zakres zadania idzie pod punkt 3 niezależnie od stopnia. Odrzucone: osobna etykieta „blokuje / nie blokuje” nadawana przez recenzenta względem zadania (dopisek do metody Superpowers, uwagi bez przypisanego punktu zadania wypadałyby jako nieblokujące); rozstrzyganie każdej uwagi przez orkiestratora (decyzja o pominięciu naprawy u agenta, który chce domknąć cykl).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; stopnie z Superpowers 6.4.1 `requesting-code-review/code-reviewer.md:113-120`.
- Pytanie 3: w jakiej postaci zadanie „wraca jako zablokowane” i czym jest jego koszt?
  - Answer: zablokowany szkic requestu — oznaczony `blocked`, z uwagami blokującymi, które przetrwały ponowną recenzję (każda z miejscem w kodzie i powodem), tym, co próbowała poprawka, oraz kosztem: czasem, modelami i tokenami cyklu do tej chwili z `stages.md` i liczbą rund recenzji. Odrzucone: raport bez requestu, w rozmowie albo w zapisie cyklu (request jest jedynym miejscem oceny wyniku cyklu; raport w rozmowie znika z sesją).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; mechanizm z WAY-125 i `task-cycle/skill/SKILL.md:398-402`, `:429-430`, `foundations` `e7f7c3a`.
- Pytanie 4: kto zakłada nowe zadanie z uwagi poszerzającej zakres?
  - Answer: Mariusz; request wymienia takie uwagi w osobnej pozycji, każdą ze słowami recenzenta i miejscem w kodzie. Odrzucone: cykl sam dopisuje zadanie do backlogu produktu (przy backlogu poza repozytorium to skutek poza repozytorium, którego WAY-140 agentowi zabrania).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-101 i WAY-140.
- Pytanie 5: czy punkt 4 dotyczy także wykonawcy każdej części planu, i gdzie trafia raport z jego sprawdzenia?
  - Answer: tak — autor zmiany jednego autora wskazuje najsłabszy punkt zadania, a wykonawca każdej części najsłabszy punkt swojej części względem zadania; wynik (który punkt, jakie sprawdzenie, co wyszło) trafia do raportu autora albo wykonawcy, który czyta recenzent, a request wymienia go w dowodach testów. Odrzucone: tylko autor zmiany jednego autora (przy większych zmianach z planem nikt nie atakuje własnego wyniku przed recenzją).
  - Source: Mariusz, 2026-10-17: „b” — na drogę b przedstawioną w rozmowie doprecyzowania, razem z zaproponowanym przy obu drogach miejscem raportu.
- Pytanie 6: czy uwaga blokująca, która zostaje po ponownej recenzji, może przejść do rozstrzygnięć niezależnej oceny w kroku 11; czy recenzja kodu uruchomiona później (rozstrzygnięcie oceny w kroku 11, uzgodnienie z gałęzią docelową w kroku 12, poprawka po recenzji człowieka) ma własną parę recenzja–ponowna recenzja; czy nowa uwaga Critical albo Important w samej poprawce liczy się jako uwaga, która została?
  - Answer: granica szczelna — uwaga blokująca po ponownej recenzji idzie tylko do zablokowanego requestu, nie do rozstrzygnięć kroku 11; każda późniejsza recenzja kodu (krok 11, krok 12, poprawka po recenzji człowieka) ma tę samą regułę: jedna poprawka, jedna ponowna recenzja, potem blokada; nowa uwaga Critical albo Important w poprawce liczy się jak ta, która została. Odrzucone: krok 11 jako wyjście dla pozostałej uwagi i brak limitu dla późniejszych recenzji (rozstrzygnięcie orkiestratora, odrzucone w odpowiedzi na pytanie 1).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; przypadek Q31 w Context.
- Pytanie 7: które z kroków 10–12 (pełna bramka, krok zwrotny, niezależna ocena wpisów fundamentu już na gałęzi, zapis cyklu) cykl wykonuje, zanim otworzy zablokowany szkic z wiersza 1?
  - Answer: pełną bramkę i zapis cyklu ze `stages.md`; krok zwrotny i niezależna ocena wpisów fundamentu zostają pominięte i nazwane w requeście, a poprawka po decyzji człowieka uruchamia je na kodzie, który przeszedł recenzję. Odrzucone: wszystkie kroki do końca (praca agentów nad kodem, którego recenzja nie przyjęła, powtarzana po poprawce); sam zapis cyklu i koszt (bez stanu kodu wobec reszty testów produktu).
  - Source: Mariusz, 2026-10-17: „c” — na drogę c przedstawioną w rozmowie doprecyzowania; kroki 10–12 w `task-cycle/skill/SKILL.md`, `foundations` `e7f7c3a`.
- Pytanie 8: czy request przy przejściu bez naprawy wymienia uwagi Minor, czy zostają tylko w raportach cyklu?
  - Answer: request wymienia je w osobnej pozycji, każdą ze słowami recenzenta i miejscem w kodzie, bez naprawy. Odrzucone: tylko w raportach cyklu, do których request linkuje („a roll-up nobody reads is a silent discard”).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; Limen `templates/agents.md:151`, Superpowers 6.4.1 `subagent-driven-development/SKILL.md:364`.
- Pytanie 9: kto rozstrzyga, że uwaga wykracza poza zakres zadania — sam recenzent czy orkiestrator?
  - Answer: recenzent — poza zakresem jest to, co recenzent sam tak oznaczył: pozycje jego listy „Declined to judge” i uwagi, które opisał jako wykraczające poza zadanie; orkiestrator nie przenosi uwag między kategoriami. Odrzucone: orkiestrator rozstrzyga każdą uwagę względem zamrożonego zadania (mógłby przesunąć niewygodną uwagę Important do nowych zadań i obejść blokadę z wiersza 1).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; Superpowers 6.4.1 `requesting-code-review/code-reviewer.md:43-48`; przypadek w `docs/task-cycles/instruction-files-part/cycle.md:107` z commita `58ee76e`.

## Context

- Źródło: lekcja „Towards Autonomous Product Development” (Adam Gospodarczyk, harness Limen w wersji `e746877`), wiersze L1 część 2 i L2 w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Learning\mapa_artykulow.md`; stan wątku w `wznowienie_limen_zmiany_w_the_way.md` obok tego dokumentu.
- Limen, `templates/agents.md:151`, krok 6: „A rejection whose findings are all non-blocking — lint reach, style, hardening past the ticket's scope — is a merge […]. A finding that widens the slice becomes a ticket line, not a repair. […] one repair and one re-review settle an ordinary ticket. A second FAIL on the same slice ends the loop even when every finding is labelled proven; the reply names what remains and what it cost. Do not buy a third round.”
- Limen, `templates/worker.md:25`: „Name the acceptance line most likely to be false and write the check that would catch it; say what that check did in the final message — a suite that only passes is not evidence.”
- Dziś na ścieżce jednego autora: „The author or executor fixes findings, affected checks run again, and the same reviewer reviews the fix range once.” — `task-cycle/skill/SKILL.md:308-309`, `foundations` `e7f7c3a`.
- Dziś na ścieżce z planem części idą przez Superpowers `subagent-driven-development` 6.4.1: do pięciu rund poprawek na część, potem orkiestrator sam rozstrzyga otwarte uwagi; po recenzji całej gałęzi jedna fala poprawek, jedna ponowna recenzja i rozstrzygnięcie reszty przez orkiestratora (`subagent-driven-development/SKILL.md:372-373`, `:411-427`, `:458-469`).
- Recenzent Superpowers (`requesting-code-review/code-reviewer.md:113-119`) dzieli uwagi na Critical, Important i Minor.
- Przypadek z zapisu cyklu `instruction-files-part` (2026-10-08, commit `58ee76e`, `docs/task-cycles/instruction-files-part/cycle.md`, Q31): po ponownej recenzji końcowej fali poprawek została uwaga Important; orkiestrator przeniósł ją do rozstrzygnięć niezależnej oceny w kroku 11, a uwaga 6 tego zapisu nazywa brak kolejności między „There is no second fix wave” Superpowers a krokiem 11.
- Słownik the way nadaje węższe znaczenie słowom „verdict” i „correction” (`foundations/glossary.md`), więc angielskie brzmienie wpisów z wierszy 1–5 ich nie używa dla werdyktu recenzenta i poprawki; wiersze 1–4 korzystają z „uwagi blokującej” określonej w wierszu 5.

## Questions carried to cycle

- Czy reguły z wierszy *Settlements to record* stają się nowymi decyzjami, czy dopiskiem do istniejącej (WAY-136 opisuje recenzję i jej zakres) — rozstrzyga przeszukanie fundamentu w kroku fundamentu.
- Jak rozgraniczyć pozycję requestu z uwagami poszerzającymi zakres od zdania kroku zwrotnego „what this request does not write is neither proposed nor listed for later” (`task-cycle/skill/SKILL.md:348-349`), które dotyczy wpisów fundamentu.
- Czy sprawdzenie najsłabszego punktu zostaje w repozytorium jako zwykły test, czy jest jednorazowym pomiarem opisanym w raporcie.
- Które kroki cykl uznaje za wykonane, a które za pominięte, gdy blokada przychodzi z recenzji późniejszej niż recenzja całej zmiany (rozstrzygnięcie oceny w kroku 11, uzgodnienie w kroku 12, poprawka po recenzji człowieka) — z zasadą odpowiedzi na pytanie 7: tania bramka i zapis cyklu tak, praca agentów nad kodem nieprzyjętym przez recenzję nie.

## Human actions

none

## Decisions in play

Przeszukanie: decyzje z *Scope* `task-cycle` w `foundations/decisions.md` na `foundations` `e7f7c3a` oraz wyszukanie słów „re-review”, „fix range”, „blocked”, „Minor”, „non-blocking”, „weakest”, „widens” we wszystkich plikach fundamentu. Żadna decyzja nie ustala liczby rund recenzji ani tego, co po negatywnej ponownej recenzji; z żadną decyzją zadanie nie koliduje. Koliduje z tekstem skilla cyklu: „Stop early only when the required outcome cannot be implemented under the available evidence, capabilities and binding rules. A slow step, a failed test, a reviewer finding or an ambiguous implementation method is work to resolve, not a reason to ask the human.” (`task-cycle/skill/SKILL.md:16-19`) — wiersz 1 dodaje nowy powód zatrzymania, więc cykl zmienia także ten wstęp.

- WAY-125/1 — przyjęcie metod Superpowers 6.4.1, w tym `subagent-driven-development` „with independent task and final code reviews”; „Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request”. Zadanie odchodzi od czterech kroków przyjętych metod: w końcowej recenzji całej gałęzi `subagent-driven-development` — rozstrzygania pozostałych uwag przez orkiestratora (wiersze 1–2), przeglądu i naprawy uwag Minor w końcowej fali poprawek (wiersz 5) i odkładania uwag spoza zakresu do zapisu metody (wiersz 6); w `requesting-code-review` — rozstrzygania listy „Declined to judge” przez wykonawcę („The executor rules on each line”, `code-reviewer.md:46-48`; wiersz 6).
- WAY-136/1 — „A one-author change and every slice are reviewed by an agent that did not make them, and a change of more than one slice then gets one review of the whole change, while the review of a one-author change or of a plan's only slice is the review of the whole change”. Zadanie dokłada regułę końca pętli tej recenzji całej zmiany.
- WAY-11/1 — „A task ends with its return step before its branch is merged”; WAY-10/1 — niezależna ocena zmiany fundamentu. Krok zwrotny i ocena pominięte przed zablokowanym szkicem (wiersz 4) odbywają się więc przed każdym scaleniem, także gdy decyzja człowieka nie zmienia kodu.
- WAY-148/1 — „Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory”. Raport najsłabszego punktu idzie tą drogą.
- WAY-13/1 — „an agent may check a change more sharply than the map computes, never less”. Przejście do requestu bez uwag blokujących nie zmniejsza zestawu sprawdzeń.
- WAY-69/1 — „the deliberate break the check is accepted on is written from the sentence by the reviewer of that code, who did not write the check”. Najsłabszy punkt autora nie zastępuje celowego złamania przez recenzenta, a sprawdzenie najsłabszego punktu nigdy nie jest sprawdzeniem, które cytuje niezmiennik — to pisze inny agent niż autor kodu.
- WAY-101/1 — „each product chooses where it keeps its roadmap, projects and tasks”; WAY-140/1 — „A task's effect outside the product's repository … is made only by a human”. Stąd nowe zadanie z uwagi poszerzającej zakres zakłada człowiek.

## Settlements to record

Candidates: 8 shown, 7 accepted — 2026-10-17

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy po ponownej recenzji poprawki w recenzji całej zmiany — zmiany jednego autora albo końcowej recenzji całej gałęzi zmiany z planem — zostają uwagi blokujące, trzeciej rundy nie ma, a orkiestrator tych uwag nie rozstrzyga sam, tylko otwiera zablokowany szkic requestu z uwagami, które zostały (każda z miejscem w kodzie i powodem), tym, co próbowała poprawka, i kosztem cyklu do tej chwili z `stages.md` z liczbą rund recenzji, a pętle poprawek pojedynczych części zostają takie, jak przyjmują WAY-125 i WAY-136 (granica zakresu, nie nowa reguła). | decision | To do 1; odpowiedzi na pytania 1 i 3 | czy po końcowej recenzji gałęzi orkiestrator sam odkłada pozostałe blokujące uwagi i oznacza request jako gotowy, jak każe Superpowers, albo zleca kolejną rundę |
| 2 | Uwaga blokująca, która została po ponownej recenzji, nie przechodzi do rozstrzygnięć niezależnej oceny w kroku 11, a nowa uwaga Critical albo Important w samej poprawce liczy się jak ta, która została. | decision | odpowiedź na pytanie 6; przypadek Q31 w Context | czy przenieść pozostałą uwagę do rozstrzygnięć kroku 11, jak w cyklu `instruction-files-part` |
| 3 | Każda recenzja kodu uruchomiona po recenzji całej zmiany — przy rozstrzygnięciu oceny w kroku 11, przy uzgodnieniu z gałęzią docelową w kroku 12 i w poprawce po recenzji człowieka — ma tę samą regułę: jedna poprawka, jedna ponowna recenzja, potem zablokowany szkic. | decision | odpowiedź na pytanie 6 | ile rund poprawki dopuścić w recenzjach późniejszych niż recenzja całej zmiany |
| 4 | Przed otwarciem zablokowanego szkicu cykl uruchamia pełną bramkę i zapis cyklu, a krok zwrotny i niezależną ocenę wpisów fundamentu pomija, nazywa w requeście i uruchamia w poprawce po decyzji człowieka, na kodzie, który przeszedł recenzję albo który człowiek przyjął mimo uwagi. | decision | odpowiedź na pytanie 7; WAY-11 i WAY-10 dla kodu przyjętego przez człowieka | czy przed blokadą wykonać krok zwrotny i niezależną ocenę na kodzie, którego recenzja nie przyjęła |
| 5 | W recenzji całej zmiany na obu ścieżkach recenzja bez uwag blokujących — gdzie blokują Critical i Important recenzenta, poza uwagami wykraczającymi poza zakres zadania (wiersz 6) — oznacza przejście do requestu bez naprawy, a request wymienia nienaprawione uwagi Minor w osobnej pozycji, każdą ze słowami recenzenta i miejscem w kodzie. | decision | To do 2; odpowiedzi na pytania 1, 2 i 8 | czy uwagi Minor uruchamiają rundę poprawki na ścieżce jednego autora i czy końcowa fala poprawek na ścieżce z planem naprawia uwagi Minor, jak dziś każe Superpowers |
| 6 | W recenzji całej zmiany na obu ścieżkach uwaga, którą recenzent sam oznaczył jako wykraczającą poza zakres zadania — pozycja jego listy „Declined to judge” albo uwaga tak opisana — bez względu na stopień nie jest naprawiana, tylko request wymienia ją w osobnej pozycji ze słowami recenzenta i miejscem w kodzie, a człowiek decyduje, które z nich stają się nowym zadaniem, i je zakłada; orkiestrator nie przenosi uwag między kategoriami. | decision | To do 3; odpowiedzi na pytania 1, 4 i 9 | czy naprawić taką uwagę w cyklu albo dopisać zadanie do backlogu produktu samemu, i czy orkiestrator może sam uznać uwagę za wykraczającą poza zakres |
| 7 | Przed oddaniem do recenzji autor zmiany jednego autora wskazuje punkt zadania, a wykonawca każdej części punkt swojej części względem zadania, który najpewniej nie jest spełniony, pisze sprawdzenie, które by to złapało, i podaje w swoim raporcie, który to punkt, jakie sprawdzenie i co wyszło, a raport czyta recenzent i request wymienia wynik w dowodach testów. | decision | To do 4; odpowiedź na pytanie 5 | czy autor poza testem pisanym przed kodem ma szukać miejsca, w którym jego wynik nie spełnia zadania, i czy dotyczy to wykonawców części |

## Out of scope

- Pomijanie recenzji przy drobnych zmianach (L1 część 1) — świadomie nieprzejęte; code review zostaje zawsze.
- Przegląd fundamentu liczony scaleniami (L7) i pytanie kroku technologii o dostęp agenta do produktu (A1) — osobne zadania w backlogu.
- Przestawienie kolumny „nośnik” w wierszach L1 i L2 mapy artykułów na numery WAY — krok po scaleniu, w vaulcie, poza cyklem.
