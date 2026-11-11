---
title: "the way: sekcja „Do rozstrzygnięcia” w opisie PR-a rozdzielić na to, co poprawić, co przyjąć scaleniem i co jest naprawdę otwarte"
status: draft
created: 2026-11-11T14:40
updated: 2026-11-11
tags: [zadanie]
related: "the project note of the work on the process, in the author's notes"
---

## Po co to

- **Jak jest dziś:** Opis PR-a z cyklu zadania ma sekcję „For you to decide”, do której szablon każe wrzucić wszystko, co przed scaleniem potrzebuje Twojego „tak”: kilkanaście rodzajów pozycji, od czynności do wykonania przez Ciebie, przez niesprawdzone polecenia i wybory agenta, po wpisy do fundamentu i niepoprawione uwagi recenzji. Wszystko stoi w jednej numerowanej liście, a każda pozycja kończy się pytaniem w rodzaju „Accept?”. Drobiazgi, które warto poprawić od ręki, wybory, które przyjmujesz samym scaleniem, i sprawy naprawdę otwarte, wymagające Twojej decyzji, wyglądają tak samo i nie mają osobnego kontekstu.
- **Kto to odczuwa:** Ty, przy każdym PR-ze z cyklu zadania, w chwili gdy masz zdecydować o scaleniu. Przy PR-ze o odtwarzaniu bazy z kopii w projekcie Loop napisałeś, że ta sekcja nie jest dla Ciebie zrozumiała „już któryś raz z rzędu”.
- **Co jeśli nic:** Każdy kolejny PR dalej kosztuje dopytywanie albo odruchowe „akceptuję”. Przy odruchowym zgadzaniu się przepuszczasz wybory, których nie przeczytałeś, więc rzecz, która miała chronić decyzję człowieka przed scaleniem, przestaje to robić. Waga średnia: nic się nie psuje od razu, ale koszt wraca przy każdym PR-ze.

# the way: sekcja „Do rozstrzygnięcia” w opisie PR-a rozdzielić na to, co poprawić, co przyjąć scaleniem i co jest naprawdę otwarte

Status: ready for cycle
Project relation: independent

## Description

### Need

- Sekcja „For you to decide” opisu PR-a z cyklu zadania zbiera w jednej numerowanej liście pozycje, które wymagają od Mariusza zupełnie różnych rzeczy, i każda kończy się podobnym pytaniem („Accept?”, „Merge without it?”).
- Mariusz, 2026-11-11, przy PR-ze #75 w loop2: „sprawy, które można i warto poprawić - są wymieszane z tym co muszę po prostu przyjąć akceptując PR i mergując go i wymieszane ze sprawami, które są zupełnie otwarte i brakuje mi dla nich jakiegokolwiek sensownego kontekstu”.
- Odbiorcą jest Mariusz przy każdym PR-ze z cyklu zadania, w chwili decyzji o scaleniu; skutkiem dzisiejszego kształtu jest dopytywanie albo odruchowa zgoda na pozycje, których nie przeczytał.

### To do

1. W `task-cycle/skill/request_template.md` sekcja *For you to decide* dzieli swoje pozycje na trzy grupy, w tej kolejności: **wymagane od Ciebie**, **do poprawienia albo przepuszczenia**, **przyjmujesz scaleniem**; każda grupa stoi pod własnym nagłówkiem `###` w sekcji `## For you to decide`, zawsze wszystkie trzy, a grupa bez pozycji ma pod nagłówkiem `none`; gdy żadna grupa nie ma pozycji, cała sekcja ma samo `none`, jak dziś; pozycje są numerowane ciągiem przez wszystkie trzy grupy. Nagłówki grup brzmią `### Needed from you`, `### Fix or let through`, `### You accept by merging`; w bloku w języku zadania stoją przetłumaczone, jak każdy nagłówek górnej części (po polsku: „Wymagane od Ciebie”, „Do poprawienia albo przepuszczenia”, „Przyjmujesz scaleniem”).
2. Szablon podaje kryterium każdej grupy i przypisuje do niej rodzaje pozycji, które dziś wylicza (numery jak w `request_template.md:170-247` @ `e3825a8`, „15” to pozycja o błędzie skryptu sprawdzającego formę z `:54`):
   - **wymagane od Ciebie** — bez odpowiedzi albo czynności człowieka PR nie może iść dalej: 1 (czego potrzebuje zablokowany PR), 2 (pytania i wybór technologii zastrzeżony dla człowieka), 3 (czynności poza repozytorium);
   - **do poprawienia albo przepuszczenia** — coś, czego cykl nie zrobił albo nie poprawił, a co da się jeszcze zrobić w tym PR-ze; odpowiedź: zrobić w tym PR-ze, zrobić z tego zadanie albo przepuścić: 4 (pominięte kroki i niepuszczone sprawdzenia), 8 (niepoprawione uwagi recenzji, które ktoś odczuje), 9 (niewprowadzone propozycje z własnych sekcji zadania), 14 (niepełna lektura recenzji całej zmiany);
   - **przyjmujesz scaleniem** — co cykl zrobił w granicach swoich uprawnień; nie wymaga odpowiedzi, scalenie jest zgodą: 5, 6, 7, 10, 11, 12, 13, 15.
3. Szablon mówi, co niesie pozycja każdej grupy:
   - pozycja, w której człowiek wybiera, w grupach **wymagane od Ciebie** i **do poprawienia albo przepuszczenia**: (1) co się dzieje, konkretnie — kto to odczuje (użytkownik produktu albo człowiek pracujący z procesem), kiedy i w jakiej sytuacji, bez nazw kroków procesu i numerów wpisów, a nazwa nieunikniona dostaje przy pierwszym wystąpieniu jedno zdanie, czym jest; (2) każda droga osobno — co się stanie po jej wybraniu, ile kosztuje (czas, runda poprawki z recenzją, ryzyko, które zostaje) i gdzie może to wyjść później; (3) rekomendacja z powodem w jednym zdaniu; (4) pytanie z odpowiedziami do wyboru;
   - czynność poza repozytorium (pozycja 3): co zrobić, po co PR tego potrzebuje i co się stanie, gdy jej nie będzie;
   - **przyjmujesz scaleniem** — co cykl wybrał albo zapisał i dlaczego, prostymi słowami, a gdzie miał inną drogę, jednym zdaniem, czemu jej nie wziął; grupa zaczyna się zdaniem, że scalenie oznacza zgodę, a gdy któraś pozycja nie pasuje, Mariusz mówi która.
   
   Szablon pokazuje obok siebie wzór dobry (pozycja 9 opisu PR-a #75 w loop2, o nieprzećwiczonych częściach procedury) i zły (dzisiejszy przykład szablonu „the return step was skipped on your instruction; merge without it?”).
4. W „Write, check, publish” szablonu, przed sprawdzeniem formy, agent piszący opis sprawdza każdą pozycję dwóch pierwszych grup według czterech punktów z *To do* 3 i uzupełnia braki.
5. Szablon mówi, co uruchamia odpowiedź „zrobić w tym PR-ze” dla każdego rodzaju pozycji drugiej grupy, tak jak dziś dla uwag recenzji (`task-cycle/skill/correction.md:48`): dla pominiętego kroku albo sprawdzenia — jego wykonanie; dla niewprowadzonej propozycji — jej wprowadzenie; dla niepełnej lektury recenzji — przeczytanie przez świeżego recenzenta tego, co zostało nieprzeczytane. Gdy czegoś nie da się zrobić w tym PR-ze, pozycja daje tylko odpowiedzi „zadanie” albo „przepuścić”.
6. Odwołania do pozycji sekcji po numerze — `task-cycle/skill/correction.md` („item 8”), `task-cycle/skill/SKILL.md` („item 12”), sam szablon („item 4” przy pozycji 13) — wskazują po zmianie te same rodzaje pozycji co dziś.
7. `task-cycle/request_check.py` zgłasza błąd formy, gdy sekcja `## For you to decide` w angielskiej części opisu nie ma ani samego `none`, ani trzech nagłówków grup z *To do* 1 w tej kolejności, każdego z treścią albo `none`, bez treści przed pierwszym z nich; nie ocenia treści pozycji i nie sprawdza nagłówków grup w bloku w języku zadania. Opis skryptu i jego testy idą za tą zmianą.
8. Decyzja WAY-290 wymienia wśród tego, co skrypt sprawdza, nagłówki grup. Decyzja WAY-287 opisuje sekcję podzieloną na trzy grupy pod własnymi nagłówkami, z kryterium każdej; pozycje grupy „przyjmujesz scaleniem” nie czekają na osobną odpowiedź, a `none` całej sekcji znaczy to co dziś. Decyzja WAY-289 opisuje odpowiedź „zrobić w tym PR-ze” także dla pozycji 4, 9 i 14, nie tylko dla uwag recenzji.

### Questions to settle

- Według czego pozycja trafia do grupy i do której grupy idzie każdy z rodzajów pozycji, które szablon dziś wylicza?
  - Answer: trzy grupy według tego, czego pozycja wymaga od Mariusza — wymagane od Ciebie (1, 2, 3), do poprawienia albo przepuszczenia (4, 8, 9, 14), przyjmujesz scaleniem (5, 6, 7, 10, 11, 12, 13, 15) — z kryteriami i odpowiedziami jak w *To do* 2 i 5.
  - Not chosen:
    - pominięte kroki i niepuszczone sprawdzenia (4), niewprowadzone propozycje (9) i niepełna lektura recenzji (14) w grupie „otwarte” razem z 1–3 — Mariusz: „1, 2, 3 - to jest wymagane na pewno, ale już np. 4 - to jest już kwestia do przepuszczenia i temat typu - do poprawienia lub do przepuszczenia, więc trochę miesza dwie sprawy”.
  - Source: Mariusz, 2026-11-11, „ok, przyjmuję” (odpowiedź na poprawiony podział z tabelą grup i wierszy, po pierwszej odpowiedzi „przyjmuję, ale...”).
- Co musi zawierać pozycja, przy której Mariusz wybiera, żeby nie była ogólnikowa, i kto tego pilnuje przed publikacją opisu?
  - Answer: cztery punkty z *To do* 3 — co się dzieje konkretnie, każda droga z ceną, rekomendacja z powodem, pytanie z odpowiedziami — pilnowane przez agenta piszącego opis, który przed publikacją sprawdza według nich każdą pozycję dwóch pierwszych grup (*To do* 4).
  - Not chosen:
    - sama reguła w szablonie ze wzorem dobrym i złym — agent dalej może pisać ogólnie i nikt tego nie łapie przed Mariuszem;
    - osobny, świeży agent czytający górną część opisu przed publikacją — jedno wywołanie agenta więcej w każdym cyklu i zmiana WAY-290, która takiego drugiego odczytu nie przyjęła; zostaje na później, gdyby samosprawdzenie nie wystarczyło.
  - Source: Mariusz, 2026-11-11, „generalnie zwięzła wersja tego co mamy zapisane w globalnej instrukcji, czyli chyba tak, te 4 punkty pilnowane drogą b” (uwaga wyjściowa: „obecnie sprawy prezentowane w sekcji do rozstrzygnięcia są bardzo ogólnikowe i brakuje mi tam rachunku zysków i strat w miejscach gdzie faktycznie podejmuję decyzję”).
- W jakiej formie sekcja dzieli pozycje: trzy nagłówki w jednej sekcji, osobne sekcje opisu, czy wyróżnione wiersze jak w PR-ze #75; i czy grupa bez pozycji stoi z `none`, czy znika?
  - Answer: trzy nagłówki `###` w sekcji „For you to decide”, zawsze wszystkie trzy, grupa bez pozycji z `none`, cała sekcja z samym `none`, gdy żadna grupa nic nie ma; numeracja ciągła przez grupy (*To do* 1).
  - Not chosen:
    - tylko grupy, które coś mają — krócej, ale grupy pustej nie da się odróżnić od zapomnianej, ani przez człowieka, ani przez skrypt;
    - trzy osobne sekcje opisu zamiast „For you to decide” — zmienia szkielet opisu, WAY-286, WAY-287 i każde odesłanie do tej sekcji w skillach, a człowiekowi na GitHubie nie daje nic ponad nagłówki w jednej sekcji;
    - pogrubione wiersze jak w PR-ze #75 — wyglądają tak samo, ale skrypt nie odróżni ich od zwykłego tekstu i niczego nie przypilnuje.
  - Source: Mariusz, 2026-11-11, „A” (wybór wariantu „trzy podnagłówki w sekcji, zawsze wszystkie trzy”).
- Czy skrypt sprawdzający formę opisu (`task-cycle/request_check.py`) ma pilnować podziału na grupy, i jak po angielsku brzmią nagłówki grup?
  - Answer: skrypt pilnuje nagłówków grup w angielskiej części opisu (*To do* 7), a nagłówki brzmią `Needed from you`, `Fix or let through`, `You accept by merging` (*To do* 1).
  - Not chosen:
    - tylko szablon, bez skryptu — zero kodu, ale opis w starym kształcie albo z pogrubionymi wierszami wychodzi z cyklu i Mariusz widzi go dopiero przy scaleniu; skrypt formy powstał właśnie dlatego, że agent piszący z szablonu gubi albo przestawia sekcje (WAY-290).
  - Source: Mariusz, 2026-11-11, „a” (wybór wariantu „skrypt pilnuje nagłówków grup”, przedstawionego z tymi trzema nagłówkami jako rekomendacją).
- Czy zmiana obejmuje też to, jak inne sekcje górnej części opisu (np. „What you will see”) mówią o rzeczach, które człowiek przyjmuje, czy tylko sekcję „For you to decide”?
  - Answer: tylko sekcję „For you to decide”.
  - Not chosen:
    - także pierwszy wiersz opisu, liczący pozycje grup „wymagane od Ciebie” i „do poprawienia albo przepuszczenia” — od razu widać, czy coś blokuje scalenie, ale licznik może rozjechać się z grupami, a skrypt tego nie sprawdzi.
  - Source: Mariusz, 2026-11-11, „ok” (odpowiedź na rekomendację, by zostać przy samej sekcji).
- Czy brak własnych wytycznych kodowania i testów the way wstrzymuje to zadanie (WAY-215), skoro zmienia skrypt i jego testy?
  - Answer: nie wstrzymuje — zadanie idzie jak dotychczasowe zadania the way; sprawa wytycznych zostaje przy zadaniu „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów”.
  - Not chosen:
    - wstrzymać zadanie w `waiting for human` do scalenia zadania o wytycznych — tamto zadanie nie ma wybranego kierunku, więc czekanie nie ma końca, a każdy kolejny PR przychodzi z sekcją w starym kształcie.
  - Source: Mariusz, 2026-11-11, „nie wstrzymujemy”.

## Context

- Wzorem jest opis PR-a #75 w repozytorium loop2 (https://github.com/mariusznazar/loop2/pull/75, scalony): sekcja „For you to decide” ma trzy pogrubione wiersze — „To fix: one small thing, with my recommendation”, „You accept these by merging; if one does not suit you, say which”, „Open: your decision needed” — i jedną ciągłą numerację pozycji 1–9 przez wszystkie trzy grupy; blok po polsku powtarza to jako „Do poprawienia…”, „Przyjmujesz scaleniem; jeśli któryś punkt Ci nie pasuje, napisz który”, „Otwarte: potrzebna Twoja decyzja”.
- W PR-ze #75 do grupy „do poprawienia” trafiła niepoprawiona drobna uwaga recenzji, do „przyjmujesz scaleniem” wybory cyklu wykraczające poza zadanie i wpisy fundamentu, których Mariusz nie widział w zadaniu, a do „otwarte” nieprzećwiczone części procedury (pytanie „scalić mimo to?”).
- Podział powstał w rozmowie przy PR-ze #75 2026-11-11 jako odpowiedź na uwagę z *Need*; Mariusz odpowiedział „robimy poprawki teraz, a jak zlecisz to zaparkuj mi proszę zadanie na poprawienie szablonu PR z moją uwagą”, a opis PR-a przepisano w trzech grupach przed scaleniem.
- Miejsca w `foundations` @ `e3825a8`: szkielet sekcji `task-cycle/skill/request_template.md:78`, reguła sekcji i lista rodzajów pozycji `:163-247`, zasada bloku w języku zadania („the headings translated”) `:139-141`, pozycja o błędzie skryptu formy `:54`; nagłówki sprawdzane przez skrypt `task-cycle/request_check.py:66`, a jego test `task-cycle/test_request_check.py:172`.
- Skrypt sprawdzający formę dziś sprawdza tylko nagłówki `##`, ich kolejność, treść albo `none` w każdej sekcji i język bloku; nie ocenia treści (WAY-290, docstring `task-cycle/request_check.py:1-52`).
- the way nie ma katalogu `guidelines/`; sprawą własnych wytycznych the way zajmuje się osobne zadanie „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów” (stan `[?]`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-287 — What does a request put before the human for a decision?** Zmiana: sekcja w trzech grupach, z kryterium każdej (*To do* 8; pytanie 1).
  > The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — […] — and its `none` says that nothing else in the request waits for the human's yes.
- **WAY-289 — Which unfixed findings does a request put before the human for a decision?** Zmiana: odpowiedź „zrobić w tym PR-ze” także dla pozycji 4, 9 i 14 (*To do* 5 i 8; pytanie 1).
  > […] restates each that will be felt, in plain words, in the section for the human's decisions as one question with two answers, to fix it in this request or to make a task of it, which one answer may settle for the whole list.
- **WAY-286 — What form does the description of a request a task cycle opens take?** Bez zmiany; trzy nagłówki grup stoją w jego sekcji dla decyzji człowieka i trzymają jego zasadę, że sekcja bez treści ma `none`.
  > The description of a request a task cycle opens follows one template whose headings stand in a fixed order and at a fixed level: first a top part written for the human in plain words, with no file names and no identifiers of entries […]
- **WAY-290 — How is the form of a request's description checked?** Zmiana: lista tego, co skrypt sprawdza, obejmuje nagłówki trzech grup w sekcji dla decyzji człowieka (*To do* 7); zakaz oceniania kompletności tej sekcji zostaje.
  > Before a request opens, the cycle runs the-way's script that checks the form of the request's description — the order and level of its headings, content or `none` in each section, and the collapsed block in the task document's language — […] The script judges no content.
- **WAY-114 — What does a human accept of an entry, and when?** Bez zmiany; mówi już dziś, że scalenie przyjmuje znaczenie wpisów, których człowiek nie widział w zadaniu.
  > […] that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier […]
- **WAY-288 — In what language is a request's description written?** Bez zmiany.
  > A request's description is written in English, and its top part stands a second time, in the language of the task document, in a collapsed block of the description.

## Settlements to record

Candidates: 6 shown, 5 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Sekcja dla decyzji człowieka dzieli pozycje na trzy grupy według tego, czego wymagają: wymagane od Ciebie (bez odpowiedzi albo czynności PR nie idzie dalej), do poprawienia albo przepuszczenia (cykl czegoś nie zrobił albo nie poprawił, a da się to zrobić w tym PR-ze), przyjmujesz scaleniem (cykl zrobił to w granicach uprawnień, scalenie jest zgodą). | decision (zmiana WAY-287) | *Questions to settle*, pytanie o grupy i przypisanie | czy grupy wpisać do WAY-287, czy zostawić je w samym szablonie, i jakim kryterium je opisać |
| 2 | Grupy stoją pod trzema nagłówkami w tej sekcji, zawsze wszystkie, grupa bez pozycji z `none`, cała sekcja z samym `none`, gdy nic nie ma; numeracja ciągła. | decision (zmiana WAY-287) | *Questions to settle*, pytanie o formę | czy pusta grupa znika, czy stoi z `none`, i czy numeracja zaczyna się od nowa w każdej grupie |
| 3 | Pozycja, w której człowiek wybiera, mówi konkretnie, co się dzieje i kto to odczuje, daje każdą drogę z jej ceną, rekomendację z powodem i pytanie z odpowiedziami; agent piszący opis sprawdza to przed publikacją. | decision | *Questions to settle*, pytanie o treść pozycji | czy ta wymagana treść wiąże tylko jako zdanie szablonu, czy jako decyzja, którą recenzja zmiany szablonu może przywołać |
| 4 | Odpowiedź „zrobić w tym PR-ze” dotyczy także pominiętego kroku albo sprawdzenia, niewprowadzonej propozycji i niepełnej lektury recenzji, nie tylko uwag recenzji. | decision (zmiana WAY-289) | *Questions to settle*, pytanie o grupy i przypisanie | czy rozszerzyć WAY-289, czy opisać to tylko w szablonie i w `correction.md` |
| 5 | Skrypt sprawdzający formę opisu pilnuje nagłówków trzech grup w angielskiej części opisu, bez oceniania treści pozycji. | decision (zmiana WAY-290) | *Questions to settle*, pytanie o skrypt | czy dopisać nagłówki grup do listy tego, co skrypt sprawdza, w WAY-290 |

## Out of scope

- Pierwszy wiersz opisu (stan PR-a) i sekcja „What you will see” — zostają, jak są.
- Opisy już otwartych albo scalonych PR-ów — nie są przepisywane.
