---
title: "the way: cykl zadania po przeglądzie fundamentu — usuwanie katalogów, losowo padający test, opis prośby i korekta"
status: draft
created: 2026-11-15
updated: 2026-11-15
tags: [zadanie]
related: "the project note on the process of work on a product"
---

# the way: cykl zadania po przeglądzie fundamentu — usuwanie katalogów, losowo padający test, opis prośby i korekta

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/125

## Description

### Need

- Przegląd fundamentu the way z 2026-11-14 (sprawdzony commit `21ecb62`) znalazł w regułach cyklu zadania miejsca, w których decyzje sobie przeczą albo instrukcja nie mówi agentowi, co robić; Mariusz zdecydował, że idą jednym zadaniem.
- Usuwanie katalogów roboczych przez cykl (WAY-375, WAY-376) stoi wbrew innym regułom:
  - P18: WAY-13 każe trzymać w zmianie każdą operację, której nie da się cofnąć, a WAY-375 każe cyklowi samemu usuwać katalogi; przy okazji przykład naruszenia w *Verification* WAY-13 nie mówi, kto „traktuje duże zadanie jako powód do podziału” (uwaga #122-2).
  - P19: lista plików ignorowanych, które giną z usuwanym katalogiem, nie trafia do Mariusza przed usunięciem, choć WAY-376 tak mówi; a kopie bazowe, których gałęzie nie istnieją, zostają do ręcznego sprzątania i Mariusz widzi je w każdej prośbie, choć WAY-375 raz mówi, że ich ocena nie należy do skryptu, a raz odrzuca zostawienie ich do ręcznego sprzątania (uwaga #126-3, = #125-5).
  - P20: WAY-375 nazywa pierwsze sprzątanie „human action”, a słownik definiuje tak czynność poza repozytorium (uwaga #125-7); słownika nie zmieniamy.
  - Stan przejściowy WAY-375: klauzula o pierwszym sprzątaniu opisuje stan, który się skończył (w the way i loop2 nie ma dziś zaległych katalogów); Mariusz zdecydował ją usunąć.
- P10: krok bramki w skillu cyklu nie mówi, co znaczy czerwona bramka, gdy padł losowo padający test spoza zakresu zmiany (taki test padał w dziewięciu prośbach, które podały wynik bramki na cztery różne sposoby, a każda powtórka kosztowała ok. 15 minut).
- G2 (5 uwag z próśb: #79-5, #97-2, #107-3, #107-5, #123-4): instrukcje, które piszą opis prośby i prowadzą korektę po uwagach Mariusza, mają luki i przykłady, które mylą — odpowiedź Mariusza nie ma reguły, która ją wykona, linia stanu mówi o uwagach, których nie było, a akapit kopiowany do zlecenia każe przenieść zrzut ekranu przeznaczony dla Mariusza.

### To do

1. Usunąć z WAY-375 klauzulę o pierwszym sprzątaniu katalogów, które zebrały się przed skryptem („the first clearing of the directories that gathered before the script, which a task document places as a human action, is the human's act”).
2. Przeredagować WAY-376 (zdanie wiążące i *Rationale*, akapit, który zaczyna się od „the files a repository ignores”) tak, by lista ścieżek ignorowanych służyła przebiegowi na sucho (skrypt `task-cycle/remove_merged_worktrees.py` bez `--apply`), który człowiek uruchamia sam, a nie obiecywała, że człowiek widzi ją przed usunięciem dokonanym przez cykl; krok startu cyklu się nie zmienia.
3. Zapisać w WAY-375, że kopia bazowa, której skrypt nie przypisze do zadania, zostaje człowiekowi, i usunąć z jej *Rejected* sprzeczną z tym pozycję („a script that leaves the copies of a base alone — the loose copies stay for hand clearing”).
4. Zapisać w WAY-375 `narrows WAY-13` w *Relations* i w zdaniu wiążącym obszar, w którym WAY-375 przeważa: usuwanie własnych, scalonych katalogów cyklu.
5. W *Verification* WAY-13 nadać przykładowi naruszenia podmiot: „an agent treats a large task as a reason to split it …” w miejsce „a large task is treated as a reason to split it …” (uwaga #122-2).
6. Dopisać w kroku bramki skilla cyklu (`task-cycle/skill/SKILL.md`, akapit, który zaczyna się od „A check that fails in a cycle run and passes when run again”, ok. linii 484) i w zdaniu wiążącym WAY-261, że czerwony wynik pierwszego przebiegu bramki na końcowym drzewie zostaje wynikiem bramki, także gdy padł losowo padający test spoza zakresu zmiany; cykl z tego powodu się nie zatrzymuje, a prośba nazywa ten test i zadanie, które go naprawi, albo je proponuje, gdy go nie ma.
7. Dopisać w `agent-instructions/README.md` (sekcja „Check the change” albo „Integrate into `foundations`”), że odpowiedź „fix it in this request” na pozycję *Fix or let through* w prośbie zrobionej ręcznie uruchamia jedną poprawkę autora i jedną recenzję tej poprawki przez agenta, który jej nie robił — tę samą pętlę, którą README daje dla blokujących uwag recenzji — a to, co po niej zostaje niepoprawione, wraca tylko z pytaniem, czy zrobić z tego zadanie (uwaga #79-5).
8. Dopisać rodzaj 16 szablonu prośby („Something an entry stands on that the foundation does not hold yet”) do trzech list, które mówią, co uruchamia odpowiedź „zrób to w tej prośbie”: listy w `task-cycle/skill/correction.md` (ta, która zaczyna się od „for a skipped step or an unrun check (item 4)”), wiersza „A correction” tabeli wariantów w `task-cycle/skill/request_template.md` („whether it ran on an answer to item 8, 4, 9 or 14”) i listy w WAY-289 (akapit, który zaczyna się od „An answer to do it in this request, to an item of *Fix or let through* other than item 8”); korekta dla rodzaju 16 dopisuje brakujący fakt, decyzję albo źródło, jak mówi akapit samego rodzaju 16 (uwaga #97-2).
9. W przykładzie pozycji 17 szablonu prośby (`task-cycle/skill/request_template.md`, zdanie „This correction answered your remark about a defect the task required, …”) zastąpić to brzmienie takim, którego nie da się odczytać jako „zadanie wymagało defektu”, np. „your remark, and the cycle judged that the task required what it asked to change” (uwaga #107-3).
10. W wierszu „A correction” tabeli wariantów `task-cycle/skill/request_template.md` sprawić, by linia stanu mówiła „corrected for your remarks” tylko wtedy, gdy korektę uruchomiły uwagi człowieka, a korekta, która tylko odświeżyła gałąź z gałęzi docelowej, mówiła w linii stanu to, co ją uruchomiło, z tych samych par źródeł, które wypisuje pozycja 17 (uwaga #107-5).
11. W pierwszym akapicie sekcji „Working copies” skilla cyklu (`task-cycle/skill/SKILL.md`, zdanie „The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed.”) dopisać wyjątek dla zrzutu ekranu pokazywanego człowiekowi: ten trafia tam, gdzie każe `task-cycle/change/ui_check.md` (miejsce, które fundament produktu ustala dla zrzutów), a do katalogu agenta tylko wtedy, gdy takiego miejsca nie ma (uwaga #123-4).

### Questions to settle

- Stan przejściowy WAY-375: zostawić klauzulę o pierwszym sprzątaniu (dla produktu, który pierwszy raz przypina tę wersję z zaległymi katalogami) czy ją usunąć?
  - Answer: usunąć.
  - Not chosen:
    - zostawić — klauzula dotyczy jeszcze produktu, który przypina tę wersję z zaległymi katalogami (ocena czytelnika paczki 7, #125-8)
  - Source: Mariusz, 2026-11-14, przegląd fundamentu, decyzja przy stanie przejściowym WAY-375 w pliku danych
- P20. Poszerzyć w słowniku definicję „human action” czy zmienić WAY-375?
  - Answer: słownika nie zmieniamy; usunięcie klauzuli (pytanie wyżej) usuwa zdanie, które nazywa sprzątanie czynnością człowieka.
  - Not chosen:
    - (a) poszerzyć definicję „human action” o czynność człowieka w repozytorium — przeczy odpowiedzi „Słownika nie zmieniamy.” pod #125, którą Mariusz uznał za swoją
  - Source: komentarz pod the-way#125 („Słownika nie zmieniamy.”), uznany przez Mariusza 2026-11-14 za jego odpowiedź (pytanie wstępne przeglądu, „a”)
- P18. Zawęzić zdanie WAY-13 do operacji, którą zmiana trzyma, czy zapisać w WAY-375 `narrows WAY-13` z obszarem?
  - Answer: (b) — WAY-375 zapisuje w *Relations* `narrows WAY-13`, a jej zdanie wiążące nazywa obszar: usuwanie własnych, scalonych katalogów cyklu; WAY-13 zachowuje zasięg wobec każdej innej nieodwracalnej czynności.
  - Not chosen:
    - (a) zawęzić zdanie WAY-13 do „an operation that cannot be undone which the change holds” — WAY-13 przestaje obejmować nieodwracalne czynności samego cyklu poza zmianą, a nową taką czynność nic by nie zatrzymało
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „b — narrows WAY-13 w WAY-375, obszar: usuwanie własnych, scalonych katalogów cyklu; WAY-13 zachowuje zasięg”
- P19, lista plików ignorowanych: (a) przenieść listę usuniętych katalogów do zapisu i opisu prośby, a WAY-376 mówi, że człowiek widzi po usunięciu, co odeszło, (b) zatrzymać cykl przed usunięciem, gdy lista nie jest pusta, czy (c) zapisać w WAY-376, że lista służy przebiegowi na sucho, który człowiek uruchamia sam?
  - Answer: (c) — WAY-376 mówi, że lista służy przebiegowi na sucho (skrypt bez `--apply`), który człowiek uruchamia sam; krok cyklu się nie zmienia. Katalogi zadań zakłada cykl, więc pliki ignorowane w nich to resztki agentów i narzędzi; uczciwy wpis bez nowego szumu w prośbach i bez zatrzymywania cyklu.
  - Not chosen:
    - (a) lista do zapisu i opisu prośby — nowa, powtarzająca się linia w prośbach (dziś `.superpowers/`), a usunięty plik i tak przepada
    - (b) zatrzymać cykl, gdy lista nie jest pusta — odwraca „without a word to the human” z WAY-375; cykl czeka na starcie, ilekroć narzędzie zostawi swój folder (dziś zatrzymałby go katalog `coding-guidelines` w loop2)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „1 c”, z uzasadnieniem: „katalogi zadań zakłada cykl, więc pliki ignorowane w nich to resztki agentów i narzędzi; uczciwy wpis bez nowego szumu w prośbach i bez zatrzymywania cyklu”
- P19, luźne kopie bazowe (#126-3): (a) skrypt usuwa czystą kopię bazową, gdy nie znajduje gałęzi z jej nazwy, czy (b) WAY-375 mówi wprost, że takie kopie zostają człowiekowi?
  - Answer: (b) — WAY-375 mówi wprost, że kopia bazowa, której skrypt nie przypisze do zadania, zostaje człowiekowi, a pozycja *Rejected* „a script that leaves the copies of a base alone — the loose copies stay for hand clearing” przestaje temu przeczyć; dwie obecne kopie Mariusz usuwa ręcznie.
  - Not chosen:
    - (a) skrypt usuwa kopię bez znalezionej gałęzi — przy równoległych cyklach usunąłby kopię trwającego cyklu, której nazwa nie pasuje do gałęzi, i bramka tamtego cyklu na bazie padłaby w trakcie
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „2 b”, „zgodnie z rekomendacją”
- P10. Czerwony wynik zostaje werdyktem, a prośba nazywa test i zadanie, które go naprawi, czy test wyłącza się z przyczyną według WAY-233?
  - Answer: (a) — czerwony wynik pierwszego przebiegu bramki na końcowym drzewie zostaje wynikiem bramki; cykl nie zatrzymuje się z tego powodu, a prośba nazywa losowo padający test i zadanie, które go naprawi, albo je proponuje, gdy go nie ma.
  - Not chosen:
    - (b) cykl wyłącza test z przyczyną według WAY-233 do czasu zadania, które go naprawi — każdy cykl zmienia test spoza swojego zakresu, a losowy test zwykle nie ma przyczyny po stronie danych albo wymagania (WAY-243 wymienia „a flaky test is skipped with "flaky" as its only cause” jako naruszenie)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „1 a … spójne z WAY-261, bez ruszania cudzego testu”
- P10. Gdzie stoi ta reguła: w kroku bramki skilla cyklu i w WAY-261, czy też w WAY-243 i szablonie wytycznych testów produktu?
  - Answer: (a) — zdanie w kroku bramki skilla cyklu (`task-cycle/skill/SKILL.md`) i zdanie w WAY-261; skill cyklu obejmuje cykle każdego produktu, więc WAY-243 i szablon wytycznych testów zostają bez zmian.
  - Not chosen:
    - (b) dodatkowo WAY-243 i sekcja *Flaky tests* szablonu `product-guidelines/testing/template.md` — zdanie wiążące i linia szablonu więcej, odświeżenie `guidelines/testing.md` w loop2, a zysk tylko przy pracy poza cyklem
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „2 a … reguła wiążąca bez zmiany szablonu produktów”
- #79-5. Odpowiedź „fix it in this request” przy prośbie zrobionej ręcznie według `agent-instructions/README.md`: (a) README daje jej pętlę jednej poprawki i jednej recenzji, czy (b) szablon prośby mówi, że ręczna prośba pyta tylko, czy zrobić zadanie albo przepuścić?
  - Answer: (a) — README daje odpowiedzi „fix it” jedną poprawkę autora i jedną recenzję tej poprawki przez agenta, który jej nie robił, tę samą pętlę co dla blokujących uwag recenzji.
  - Not chosen:
    - (b) ręczna prośba pyta tylko o zadanie albo przepuszczenie — Mariusz traci możliwość poprawki od razu w prośbie zrobionej ręcznie
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, „2 a … ta sama pętla co dla uwag blokujących”

## Context

- Plik danych przeglądu: `the data file of the review of the foundation, in the author's notes` — sekcja „Fundament” → „Propozycje” (P10, P18, P19, P20), „Decyzje opisujące stan przejściowy”, punkt 6 (WAY-375), i „Grupy uwag”, G2; każda pozycja ma tam słowa wpisu, dowody, drogi, koszt i decyzję Mariusza pod swoim numerem.
- Sprawdzony commit przeglądu: `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (gałąź `foundations`); numery linii w pliku danych odnoszą się do niego.
- `Defect introduced by:` — prośba #125 dodała jednocześnie WAY-376, która mówi, że człowiek widzi listę plików ignorowanych przed usunięciem, i krok startu cyklu, który usuwa katalogi z `--apply` bez pokazania jej nikomu; dodała też WAY-375 bez relacji do WAY-13, choć WAY-25 nie pozwala zostawić kolizji bez zapisanego pierwszeństwa. Pozostałe pozycje (P10, G2) to luki wcześniejszych zadań, nie defekty.
- Co pokazały katalogi zadań w loop2 (2026-11-15, `git ls-files --others --ignored --exclude-standard` poza `.runs/` i cache'ami): `.superpowers/` (notatki narzędzia agenta) w `coding-guidelines` i `.ruff_cache/` w `naprawa-startu-dockera-w-bramce`; żadnego pliku ustawień.
- Dwie luźne kopie bazowe w the way to `.runs/base-check-stage-remarks` i `.runs/base-fix-minor-findings` (gałęzie `task/stage-remarks-check` i `task/fix-minor-findings` scalone, nazwy kopii do nich nie pasują); skill cyklu każe robić kopię bazową w `.runs/base/` wewnątrz katalogu zadania, więc nowa luźna kopia powstaje tylko wtedy, gdy agent od skilla odejdzie. Trzeci katalog z #126-3, `agent-path-to-running-product`, nie jest scalony. Mariusz może je usunąć ręcznie niezależnie od tego zadania.
- WAY-261 już każe wpisać test, który padł i przeszedł po powtórce, pod *Checks* jako padający, z wynikiem powtórki i liczbą przebiegów; pozycja 4 szablonu prośby już pyta, czy padający test naprawić, czy przepuścić. *To do* 6 dopisuje tylko, który wynik jest wynikiem bramki.
- Sam losowo padający test bramki (`DirectoriesAtOnce`) naprawia zadanie „the way: drobne poprawki po PR-ach #117–#121” (*To do* 1–2); P10 dotyczy reguły kroku bramki na następny taki przypadek.
- Pozycja 16 listy drobnych poprawek brzmienia z przeglądu (przykład *Verification* WAY-13) idzie tu razem z P18 jako *To do* 5.
- Kolejność cykli: `task-cycle/skill/request_template.md` zmienia też zadanie „the way: dziennik decyzji po przeglądzie fundamentu” (Z1, P11); cykle Z1 i Z2 nie biegną równocześnie, a cykl, który startuje drugi, startuje z `foundations` po scaleniu pierwszego; pierwszy idzie ten, który wcześniej będzie `ready for cycle` (doradca dnia w imieniu Mariusza, 2026-11-15: „cykle Z1 i Z2 po kolei — taśmę the way i tak prowadzę po jednym cyklu naraz”).
- Rodzaj 16 szablonu prośby zmienia też zadanie „the way: zadanie oparte na zaplanowanej, jeszcze niezapisanej decyzji …” (`ready for cycle`); *To do* 8 dotyka tylko list, które rodzaj 16 pomijają, nie jego akapitu.
- Hasło słownika „human action” zostaje bez zmian; po *To do* 1 WAY-375 nie nazywa już żadnej czynności tym terminem.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-13 — What sets the weight of a task's process?** (`foundations/decisions.md`), zdanie wiążące w części: „At its start a task's cycle answers two questions — does the change touch the files of a trust boundary (WAY-48), and does it hold an operation that cannot be undone — and a change for which either answer is yes gets a review aimed at that risk; an operation that cannot be undone is only prepared, and a human performs it after deciding at the request.” *Verification*, violates: „… a large task is treated as a reason to split it, or to lighten its checks, because of its size.” Zmiana, którą zadanie robi: zdanie wiążące bez zmian, WAY-375 przeważa nad nim w obszarze usuwania własnych, scalonych katalogów cyklu (`narrows WAY-13`); przykład *Verification* dostaje podmiot „an agent treats a large task …” (*To do* 4–5).
- **WAY-25 — What settles a collision between two decisions?**: „Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a chain, and two decisions that narrow each other are an error. A collision between two decisions with no precedence recorded is never settled silently by the agent that meets it.” Bez zmian; daje formę *To do* 4.
- **WAY-375 — Which working directories of earlier tasks does a cycle remove at its start, and which does it leave to the human?**, zdanie wiążące w części: „… A directory of a cycle that the script does not remove stays, with its reason, for the human to decide, … The script touches only the checkouts that `git worktree list` names for the repository, never the main checkout, the directory it is run in or a detached directory outside the cycle's, and it removes directories only, never a branch, local or remote. Removing a checkout that git names, also one that stands outside the repository's own directory, is a change to the repository's state and no effect outside the repository in the sense of WAY-140, so the script that a cycle runs needs no act of a human; the first clearing of the directories that gathered before the script, which a task document places as a human action, is the human's act.” *Relations*: „derives from WAY-140 · derives from WAY-153 · derives from WAY-373”. *Rationale*: „A directory that belongs to no cycle, and a base copy named for no task, is not for the script to judge.” *Rejected*: „a script that leaves the copies of a base alone — the loose copies stay for hand clearing”. Zmiany, które zadanie robi: usuwa klauzulę o pierwszym sprzątaniu (*To do* 1); mówi, że kopia bazowa, której skrypt nie przypisze do zadania, zostaje człowiekowi, i usuwa sprzeczną pozycję *Rejected* (*To do* 3); dopisuje `narrows WAY-13` z obszarem (*To do* 4).
- **WAY-376 — Does a file that git ignores keep a working directory of a task from being removed?**: „A file that git ignores does not count against a clean tree, so the script of WAY-375 removes a directory that holds ignored files, and they end with it. For each directory the script marks for removal it lists the paths git ignores in it outside the cycle's `.runs/` directory, leaving out the caches a command makes again, so that the human sees before the removal what ends with it.” *Rationale*: „The listing is the price paid for not counting them: a local setting that matters is lost with the directory, and the human sees it in the list before the removal is made.” Zmiana, którą zadanie robi: lista służy przebiegowi na sucho, który człowiek uruchamia sam; zdanie i *Rationale* przestają obiecywać, że człowiek widzi ją przed usunięciem dokonanym przez cykl (*To do* 2).
- **WAY-261 — What does a task cycle report about a check that fails and passes when run again?**: „Each failing run of a check remains in the cycle record with its command and result, even if the check later passes. When a check has both a failing and a passing run during the cycle, the request lists it under *Checks* as failed, with the result of its rerun and the number of cycle runs in which it failed and passed; … This applies in every product, whether or not its testing guidelines name flaky tests.” Zmiana, którą zadanie robi: dopisuje, że czerwony wynik pierwszego przebiegu bramki na końcowym drzewie zostaje wynikiem bramki, także przy losowo padającym teście spoza zakresu zmiany, a prośba nazywa ten test i zadanie, które go naprawi, albo je proponuje (*To do* 6).
- **WAY-243 — How is a flaky test treated?**: „The template of the testing discipline requires the rule that running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of the gate pass, and that disabling or deleting such a test is a change of an existing test under WAY-233.” Bez zmian (pytanie P10 o miejsce reguły).
- **WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision?**, akapit: „An answer to do it in this request, to an item of *Fix or let through* other than item 8, runs the correction the same way, the item it names being the remark the correction binds (WAY-289): — for a skipped step or an unrun check (item 4): … — for a proposal of the task's own sections that was not applied (item 9): … — for an incomplete reading by the review of the whole change (item 14): …”. Zmiana, którą zadanie robi: lista dostaje rodzaj 16, dla którego korekta dopisuje brakujący fakt, decyzję albo źródło (*To do* 8).

## Settlements to record

Candidates: 7 shown, 7 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Klauzulę WAY-375 o pierwszym sprzątaniu katalogów usunąć. | sentence of WAY-375 | *Questions to settle*, stan przejściowy WAY-375 | czy zostawić klauzulę dla produktu, który pierwszy raz przypina tę wersję |
| 2 | WAY-375 `narrows WAY-13`, w obszarze usuwania własnych, scalonych katalogów cyklu; WAY-13 zachowuje zasięg. | sentence of WAY-375 | *Questions to settle*, P18 | czy zawęzić samo zdanie WAY-13 |
| 3 | Lista ścieżek ignorowanych służy przebiegowi na sucho, który człowiek uruchamia sam; cykl usuwa bez pokazywania jej. | sentence of WAY-376 | *Questions to settle*, P19, lista plików ignorowanych | czy przenieść listę do zapisu i prośby albo zatrzymywać cykl |
| 4 | Kopia bazowa, której skrypt nie przypisze do zadania, zostaje człowiekowi. | sentence of WAY-375 | *Questions to settle*, P19, luźne kopie bazowe | czy nauczyć skrypt usuwać kopię bez znalezionej gałęzi |
| 5 | Czerwony wynik pierwszego przebiegu bramki na końcowym drzewie zostaje wynikiem bramki, także przy losowo padającym teście spoza zakresu; prośba nazywa test i zadanie, które go naprawi. | sentence of WAY-261 | *Questions to settle*, P10, oba pytania | czy podać zielony wynik powtórki, czy wyłączyć test |
| 6 | Reguła z wiersza 5 stoi w skillu cyklu i w WAY-261; WAY-243 i szablon wytycznych testów produktu zostają bez zmian. | skill or instruction file: `task-cycle/skill/SKILL.md` | *Questions to settle*, P10, gdzie stoi reguła | czy zmienić WAY-243 i szablon wytycznych testów |
| 7 | Odpowiedź „fix it” przy prośbie zrobionej ręcznie uruchamia jedną poprawkę i jedną recenzję tej poprawki. | skill or instruction file: `agent-instructions/README.md` | *Questions to settle*, #79-5 | czy ręczna prośba ma w ogóle pytać o poprawkę w prośbie |

## Out of scope

- Naprawa samego losowo padającego testu bramki — niesie ją zadanie „the way: drobne poprawki po PR-ach #117–#121”.
- Usunięcie dwóch luźnych kopii bazowych i katalogu `agent-path-to-running-product` — Mariusz robi to ręcznie, niezależnie od zadania.
