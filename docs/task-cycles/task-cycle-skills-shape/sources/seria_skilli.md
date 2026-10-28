---
title: "the way: przebudować skille po kolei — na górze obraz całości i zasady, wytyczne etapów w plikach obok"
status: draft
created: 2026-10-27T23:40
updated: 2026-10-28
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

## Po co to

- **Jak jest dziś:** the way ma 21 skilli, od ok. 750 do ok. 6400 słów; dziewięć ma ponad 2000 słów. Należą do czterech obszarów: cyklu zadania (prowadzenie cyklu, specyfikacja, plan, zmiana, przegląd), poziomu projektu (definicja, plan, prowadzenie, doprecyzowanie zadania, wybór technologii), wytycznych produktu (kod, testy, styleguide) i fundamentu (decyzje, niezmienniki, słownik, mapa części, fakty o otoczeniu, krytyka, wspólne zasady). Wszystko, co stoi w skillu, agent dostaje naraz — także to, co przydaje się tylko na jednym kroku albo w jednym wariancie.
- **Kto to odczuwa:** Mariusz, bo praca w the way — cykl zadania, rozmowy poziomu projektu, pisanie wytycznych i wpisów fundamentu — kosztuje go najwięcej czasu i tokenów ze wszystkiego, czego używa; i agenci, którzy płacą kontekstem za części skilla, których w danej chwili nie potrzebują.
- **Co jeśli nic:** the way dalej kosztuje tyle, ile dziś. Zadanie A ustali kryterium, ale bez tego zadania nie zostanie zastosowane do skilli, które ważą najwięcej.

## Co zmienić

Każdy skill the way dostaje ten sam kształt: w głównej części obraz całości, ogólne zasady postępowania w ramach skilla i odsyłacze do wytycznych etapów, a same wytyczne etapów leżą w plikach obok i są czytane dopiero na swoim etapie. To kształt, który Mariusz wybrał przy lekcji s01e02 kursu Mega.DEV; lekcja nazywa go „router skill”. Dotyczy wszystkich 21 skilli the way, nie tylko cyklu zadania. Wejścia `the-way-*` w produktach generuje skrypt z samych skilli, więc nie przebudowuje się ich ręcznie.

Zadanie czeka na zadanie A — przebudowę skilla do plików instrukcji, który ma dostać część o ocenie skilli i kryterium, gdzie stoi reguła. Kryterium ma dwa pytania: kiedy agent potrzebuje danej części skilla, i czy rozpozna ten moment. Część, której moment agent przeoczy, zostaje w głównej części albo dostaje warunek sformułowany tak, żeby był rozpoznawalny — inaczej przeniesienie po cichu ją wyłącza. Po A trzeba to zadanie doprecyzować: którym narzędziem oceniamy skill, w jakiej kolejności idziemy i jak wygląda jeden skill przed i po.

Kolejność: po kolei każdy skill the way, zaczynając od tych, które kosztują najwięcej. Ranking trzeba policzyć, nie zgadywać. Dla skilli cyklu zadania koszt dają zapisy cykli w `loop2` — każdy cykl zapisuje czas i tokeny każdego etapu w pliku `stages.md`. Skille spoza cyklu (poziom projektu, wytyczne, fundament) takiego zapisu nie mają; ich koszt trzeba wziąć z zapisów sesji, w których były używane — jak dokładnie, do ustalenia przy doprecyzowaniu.

Każda przebudowa to zmiana the way: idzie PR-em do repo the way według przewodnika pracy nad samym the way (`agent-instructions/README.md`), a kształt skilli ma już wpis w dzienniku decyzji the way: WAY-256, zapisany przez zadanie A. Skill oceniamy skillem `the-way-maintain-instruction-files` tego repo, w trybie oceny, z plikiem rodzaju „skill” (`instruction-files/kind_skill.md`) — tak każe WAY-256, a WAY-257 każe przy każdym fragmencie pokazać, kiedy jest potrzebny i czy agent rozpozna ten moment.

Po przebudowie skilli cyklu zadania przychodzi jeden zmierzony cykl na `loop2` — to krok 4 lekcji s01e02 w mapie Mega.DEV. Pokaże w zapisach czasu i tokenów, czy przebudowa coś dała. Skille spoza cyklu sprawdza się przy ich następnym użyciu w `loop2`.

## Do doczytania

- Notatka zadania A: `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_instruction_files_jako_router.md` — kryterium i to, czego wymaga od części o skillach.
- `Notes/Projects/(P) Przejście Mega.DEV/mapa_pakietu_mega_dev.md`, sekcja s01e02, wiersze E16 i E17 oraz notatki „krok 3, G2” — skąd wziął się ten kształt i dlaczego zaczynamy od skilli the way, a nie od najdłuższych skilli setupu.
- Skille w repo `C:\Storage\repos\the-way`: `task-cycle\` (cykl zadania), `project-level\` (poziom projektu), `product-guidelines\` (wytyczne produktu), `elements\` (fundament); w każdym `SKILL.md` z plikami, które czyta.

## Ustalone

- **Forma: seria zadań.** Ta notatka jest nadrzędna i trzyma ustalenia wspólne dla wszystkich skilli: kolejność, sposób pomiaru, podział na PR-y, zmianę WAY-125. Każdy skill albo grupa skilli dostaje własne zadanie, doprecyzowane skillem `the-way-refine-task` tak jak zadanie A, z własnym cyklem i PR-em. Odrzucone: jedno zadanie na 20 skilli (cykl na kilkanaście godzin, jeden PR nie do przejrzenia, bez pomiaru w środku) i projekt (definicja, plan i bramka gotowości ważą więcej, niż dają, a ustalenia wspólne mieszczą się w jednej notatce). Źródło: Mariusz, 2026-10-28, „ok, tak, wariant z serią”.
- **Agent etapu czyta plik obok skilla dopiero na kroku albo w wariancie, który ten plik wymienia (zmiana WAY-125).** Dziś WAY-125 mówi „Each agent reads the method of its stage, and what it names, whole” (`foundations/decisions.md`; ten sam przepis w `task-cycle/skill/SKILL.md`, krok 3 sekcji „Inputs and authority”), a zlecenia agentom etapu każą wczytać na starcie `SKILL.md` i wszystkie wymienione w nim pliki. Bez zmiany przebudowa czterech skilli etapów (`write-spec`, `plan-task`, `make-change`, `review-change`) nic by nie dała. Zostało tylko w skillu orkiestratora, którego WAY-125 nie każe czytać w całości. Po zmianie `SKILL.md` metody czyta się w całości, a plik obok wtedy, gdy przychodzi wymieniający go krok albo wariant. Najwięcej zyskują warianty, których dany agent nie robi (np. cztery rodzaje wykonawców w `make-change`); z kroków jeszcze nieosiągniętych zysk jest mniejszy, bo plik przeczytany wcześniej zostaje w kontekście. Koszt: zmiana znaczenia przyjętej decyzji i przepisanie zleceń w skillu cyklu. Ryzyko: agent przegapi moment, w którym ma sięgnąć po plik; chroni przed tym drugie pytanie z WAY-257, a sprawdzi to zmierzony cykl na `loop2`. Zmiana wchodzi w pierwszym zadaniu serii, które dotyka skilli cyklu; po jej scaleniu numer WAY-125 trafia do nośnika wierszy E16 i E17 mapy Mega.DEV. Sprawę zgłosił recenzent całej zmiany w zadaniu A (PR #49, uwaga drobna 4). Źródło: Mariusz, 2026-10-28, „dopiszmy”.

- **Kolejność według miary „rozmiar tekstu skilla w tokenach × liczba wywołań modelu, które ten tekst niosły”.** Liczy ją skrypt z zapisów sesji Claude Code, razem z zapisami subagentów, od 2026-09-01, jedną miarą dla wszystkich 20 skilli. Ta sama miara po przebudowie jest punktem odniesienia. Powód: przebudowa zmienia tylko to, ile tekstu skilla agent nosi przy każdym wywołaniu. Samo liczenie wywołań skilla pomija agentów etapów i wpisów fundamentu, którzy czytają `SKILL.md` z dysku, a tokeny etapów z `stages.md` mierzą głównie pracę, nie skill. Ograniczenia: nie widzi sesji Codexa i nie mierzy zysku z mniejszej liczby błędów. Skala: w pilocie `loop2` wywołanie miało średnio ok. 220 tys. tokenów kontekstu, a skill orkiestratora ok. 9 tys., więc oszczędność tokenów będzie umiarkowana; główny zakład WAY-256 to mniej instrukcji naraz. Odrzucone: tokeny całych etapów i sesji przypisane skillom (przypisanie umowne, mierzy pracę) i kolejność z oceny bez pomiaru (notatka tego zakazuje; skille często czytane mogą przeważyć nad dłuższymi). Źródło: Mariusz, 2026-10-28, „wariant 1”.

- **Podział na 11 zadań, każde z jednym PR-em.** (1) Pięć skilli cyklu (`implement-task`, `write-spec`, `plan-task`, `make-change`, `review-change`) razem ze zmianą WAY-125: są splecione, bo orkiestrator w zleceniach nazywa pliki etapów, a osobne PR-y dawałyby stany pośrednie. (2) Sześć małych skilli fundamentu (`record-decision`, `record-invariant`, `record-glossary-term`, `record-environment-fact`, `update-part-map`, `critique`; 750–970 słów, wspólna część `elements/common/`). (3–11) Każdy z pozostałych osobno: trzy skille wytycznych, pięć skilli poziomu projektu i `find-foundation-entries`. Kolejność zadań wynika z miary, a grupę liczymy sumą jej skilli. Pomiar: po zadaniu cyklu jeden zmierzony cykl na `loop2`; pozostałe przy następnym użyciu w `loop2` i skryptem miary. `loop2` przesuwa przypięcie the way tylko przed zmierzonym cyklem, nie po każdym PR-ze. Odrzucone: każdy skill osobno (20 przeglądów, stany pośrednie w cyklu) i grupy według obszaru (cztery duże PR-y, kolejność według kosztu tylko między obszarami). Koszt: zadanie cyklu to największy PR serii. Źródło: Mariusz, 2026-10-28, „wariant 2”.

- **Kolejność zadań serii według miary, policzonej 2026-10-28** (2149 zapisów sesji Claude Code od 2026-09-01; tokeny ≈ znaki / 4; rozmiary plików ze stanu `foundations` na `cf11541`, nie z dnia użycia; w nawiasie część z sesji uruchomionych w repo the way):

  | # | Zadanie | Mln tokenów niesionych |
  |---|---|---|
  | 1 | cykl: `implement-task` 61,1 (29,1), `make-change` 12,0, `review-change` 5,8, `plan-task` 3,8, `write-spec` 0,8 | 83,5 |
  | 2 | `refine-task` | 19,8 (9,2) |
  | 3 | sześć małych skilli fundamentu: `record-invariant` 4,0, `record-decision` 3,4, `critique` 3,1, `record-glossary-term` 1,4, `update-part-map` 1,3, `record-environment-fact` 1,2 | 14,5 |
  | 4 | `maintain-styleguide` | 5,4 (2,3) |
  | 5 | `maintain-testing-guidelines` | 4,0 (2,6) |
  | 6 | `plan-project` | 3,7 (0,5) |
  | 7 | `find-foundation-entries` | 3,5 (2,0) |
  | 8 | `maintain-coding-guidelines` | 3,2 (2,3) |
  | 9 | `settle-technology` | 2,9 (2,3) |
  | 10 | `lead-project` | 2,4 (0,1) |
  | 11 | `define-project` | 2,2 (1,2) |

  Dla porównania `maintain-instruction-files`, przebudowany w zadaniu A: 5,4. Skrypt i wynik: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/skill_carry_cost.py` i `ranking_2026-10-28.txt` obok; uruchomienie: `python -I skill_carry_cost.py <plik wyniku>`. Po przebudowie ten sam skrypt na zapisach od dnia scalenia daje porównanie — przy tej samej liczbie wywołań różnica wynika już tylko z rozmiaru plików czytanych na danym kroku.

- **Wzór: przykład `make-change`, z wyjątkiem dla fragmentu z jedną instrukcją.** Tabela ocen i układ po przebudowie: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/przyklad_make_change.md` — w `SKILL.md` obraz całości, tabela wariantów na początku kroku 1, część wspólna; obok `slice.md`, `fix.md`, `ui_check.md`. Fragment wariantu albo kroku, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, gdzie stałby odsyłacz do niego: odsyłacz też jest instrukcją, więc plik obok nie zmniejszyłby liczby instrukcji naraz, a dołożyłby plik do utrzymania. Wyjątek dochodzi do WAY-256 i do `instruction-files/kind_skill.md` w zadaniu 1, razem ze zmianą WAY-125. Ryzyko: „to tylko jedna instrukcja” jako furtka do zostawiania wszystkiego; granica jest policzalna — jedna instrukcja przeciw jednemu odsyłaczowi. Przykład pokazał też, że w `make-change` zysk jest mały (ok. 15%, z 12 do ok. 10 mln tokenów w mierze serii), bo warianty różnią się kilkoma liniami; duży zysk leży w `implement-task`. Źródło: Mariusz, 2026-10-28, „dopiszmy ten wyjątek”.

- **Przebudowa zmienia miejsce reguł, nie ich treść.** Cykl każdego zadania serii wykonuje sam tylko werdykty „keep” i „move” oraz przeredagowania, które nie zmieniają znaczenia — zdanie odsyłacza, wiersz tabeli wariantów, fragment z jedną instrukcją w miejscu odsyłacza; werdykty „remove” i „reword” zmieniające treść reguły idą do requestu jako propozycje. Powód: PR serii ma być do przejrzenia jako przebudowa („nic nie zginęło, nic nie zmieniło sensu”), a pomiar ma pokazać skutek samego kształtu, nie usuniętej treści. Koszt: znalezione zbędne reguły czekają na osobną zmianę. Odrzucone: cykl wykonuje wszystkie werdykty. Źródło: Mariusz, 2026-10-28, „A” w doprecyzowaniu zadania 1 (`_zadania/zadanie_skille_the_way_1_cykl_zadania.md`) i „tak, przyjmuję” na dopisanie tego do serii.

## Otwarte wątki / decyzje

- Brak otwartych na poziomie serii. Zadanie 1 (cykl) gotowe do cyklu: `_zadania/zadanie_skille_the_way_1_cykl_zadania.md` (`Status: ready for cycle`, 2026-10-28); następne do doprecyzowania: zadanie 2 (`refine-task`). Handoff niżej dotyczy zadania 1 i jest już wykorzystany.

## Handoff dla AI

Blok do wklejenia świeżej sesji. Nie powtarza stanu wątku — odsyła po niego
do treści wyżej.

```text
Kontynuujemy pracę nad serią przebudowy skilli the way. Twoje zadanie w tej sesji: doprecyzować z Mariuszem zadanie 1 serii — przebudowę pięciu skilli cyklu zadania (implement-task, write-spec, plan-task, make-change, review-change) razem ze zmianą decyzji WAY-125 i wyjątkiem w WAY-256 — aż jego opis dojdzie do linii „Status: ready for cycle”. Samej przebudowy w tej sesji nie robisz.

## Gdzie jesteśmy

Przebudowa wszystkich skilli the way została rozpisana na serię jedenastu zadań, po jednym PR-ze każde. Kolejność wynika z pomiaru: ile tekstu skilla agenci nieśli w kontekście, licząc każde wywołanie modelu po przeczytaniu skilla. Pięć skilli cyklu zadania wyszło najwyżej, ok. 83 mln tokenów od 1 września, z czego sam skill orkiestratora implement-task to ok. 61 mln. Dlatego zadanie 1 to cykl.

Kształt skilla jest już decyzją the way (WAY-256): w SKILL.md zostaje obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym wariancie stoi w pliku obok, który ten krok wymienia. Zadanie 1 dokłada do tego dwie zmiany przyjęte przez Mariusza. Pierwsza: WAY-125 dziś każe agentowi etapu czytać na starcie swoją metodę i wszystko, co ona wymienia; po zmianie agent czyta SKILL.md w całości, a plik obok dopiero wtedy, gdy przychodzi wymieniający go krok albo wariant — bez tego przenoszenie treści do plików obok w skillach etapów nic nie daje. Druga: fragment, który jest jedną instrukcją, zostaje w SKILL.md w miejscu, gdzie stałby odsyłacz do niego, bo odsyłacz też jest instrukcją; ten wyjątek trafia do WAY-256 i do instruction-files/kind_skill.md.

Wzorem jest przykład przebudowy make-change: tabela ocen każdego fragmentu i szkic układu po przebudowie. Przykład pokazał, że w make-change zysk jest mały (ok. 15%), bo jego warianty różnią się kilkoma liniami; duży zysk leży w implement-task. Szczegóły, uzasadnienia i odrzucone warianty są w notatce serii i w plikach wymienionych niżej.

## Do doczytania

C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_skille_the_way_po_kolei_wedlug_kryterium.md — notatka serii; przeczytaj ją w całości, zwłaszcza sekcję „Ustalone”. Jest pisana do Mariusza: przejmij treść, nie ton.
C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\skille_po_kolei_dane\przyklad_make_change.md — tabela ocen make-change i układ po przebudowie; wzór dla pozostałych skilli cyklu.
C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\skille_po_kolei_dane\ranking_2026-10-28.txt — wynik pomiaru, i skill_carry_cost.py obok — skrypt, który go liczy i który po scaleniu da porównanie.
C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_instruction_files_jako_router.md — zadanie A, które dało WAY-256, WAY-257 i WAY-258; wzór formy opisu zadania gotowego do cyklu.
C:\Storage\repos\the-way\agent-instructions\README.md — jak zmienia się sam the way.
Zapis sesji, w której powstała seria (wygasa ok. 2026-11-27; grepuj po konkretach, nie czytaj w całości): C:\Users\Mariusz\.claude\projects\C--Storage-repos-the-way\8a2c81e2-d801-49a8-be6d-3d33d73f20a3.jsonl

## Ograniczenia / czego nie robić

Pracuj w C:\Storage\repos\the-way, nie w kopiach the way w produktach (.the-way w loop2) ani w C:\Storage\repos\the-way-global. Wejść .claude/skills/the-way-* i .agents/skills/the-way-* nie edytuj ręcznie — generuje je python -B agent-instructions/skill_entry_points.py --write. Używaj skilli the way z przedrostkiem the-way-; osobisty skill refine-task Mariusza to nie ten sam skill. Ustalenia serii są materiałem, nie ścianą: jeśli rozmowa pokaże lepszy wariant, wyłóż go z rachunkiem obu stron, zamiast go przemilczeć. Po scaleniu PR-a zadania 1 numer WAY-125 dochodzi do nośnika wierszy E16 i E17 w C:\Storage\The Brain\The Brain\Notes\Projects\(P) Przejście Mega.DEV\mapa_pakietu_mega_dev.md — to krok po scaleniu, nie w tej sesji.

## Pierwszy ruch

Przeczytaj notatkę serii w całości, potem wywołaj skill the-way-refine-task — prowadzi doprecyzowanie jednego zadania przed cyklem the way i zapisuje jego opis jako dokument w _zadania/. Gdy dokument powstanie, przepnij linię „the way, seria skilli 1/11” w C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_tasks_active.md z notatki serii na ten dokument.
```
