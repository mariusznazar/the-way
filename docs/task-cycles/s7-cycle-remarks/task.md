---
title: "the way: poprawki z uwag cykli (ai-review S7)"
status: draft
created: 2026-10-20
updated: 2026-10-21
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: poprawki z uwag cykli (ai-review S7)

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykle zadań na the-way zgłosiły w sekcjach „Process remarks on the-way” rozjazdy między skillami a fundamentem albo procesem, a nocny skan ai-review (strumień S7) zebrał je jako sprawy AIR-476–481, które Mariusz przyjął do naniesienia.
- Odbiorcą jest orkiestrator i agenci kolejnych cykli: dziś każdy cykl obchodzi te rozjazdy własną interpretacją albo własnym skryptem, za każdym razem trochę inaczej.

### To do

1. (AIR-476) WAY-30 mówi, że zmiana decyzji zatwierdzona z planem albo dokumentem zadania jest odpowiedzią, której wymaga WAY-114: agent, który pisze wpis, nie pyta już o sens, który plan albo dokument niesie, a pyta o to, co wykracza poza niego; w tym obszarze WAY-30 ma pierwszeństwo przed WAY-114 i nazywa ją w *Relations* jako `narrows` (WAY-25).
2. (AIR-476) Krok fundamentu cyklu zadania (`task-cycle/skill/SKILL.md:297-301`) i krok 4.2 wspólnego sposobu pracy skilli wpisów (`elements/common/way_of_working.md:157-159`) pytają człowieka o zmianę sensu zatwierdzonej decyzji tylko wtedy, gdy wykracza ona poza to, co niesie zatwierdzony dokument zadania albo plan, a krok fundamentu nie traktuje jako zderzenia z obecnym wpisem wiersza *Settlements to record*, który ten wpis zmienia tak, jak zleca dokument zadania; brzmienie przyjęte w zeszycie dla `SKILL.md:299`: „…an entry would change the meaning of an approved decision beyond what the approved task document or plan carries (WAY-30)…”.
3. (AIR-477) `agent-instructions/README.md:44-45` kieruje wynik niezależnej oceny tam, gdzie każe `elements/common/critique/SKILL.md`: „Its record goes where `elements/common/critique/SKILL.md` puts it; the record of both foundation searches goes in the message of the commit that carries the change.”
4. (AIR-477) Oceniający nie dostaje wiadomości commitów: w `elements/common/critique/SKILL.md:21-22` po „never the task's chronicle or the author's reasoning” stoi „— commit messages included: name the assessed commits by hash only”.
5. (AIR-478) `agent-instructions/README.md:31-32` dostaje zdanie: „Before the request, also run the decisions and invariants guards with `--merge-onto <the current foundations tip>` and act only on their relation-fingerprint findings; their findings about copies of a version and about a placeholder request link are expected before `main`.”
6. (AIR-479) Przy kontrakcie zleceń (`task-cycle/skill/SKILL.md:126-127`) stoi zdanie: „For a plan written by `plan-task`, run the borrowed method's brief script on a temporary copy of the plan with each `### Slice N` heading written as `### Task N`, and remove the copy after extraction.” — rozwiązanie przejściowe, do czasu własnych skilli the way w miejsce Superpowers.
7. (AIR-480) Kandydat na tryb awarii, którego cykl znalazł przy części, idzie do człowieka jako pytanie w *Questions* requestu (krok 13, `task-cycle/skill/SKILL.md:553-555`), z częścią, tym, co zawodzi, szkodą, wagą, sposobem wykrycia, rekomendacją i najsilniejszym argumentem przeciw tej rekomendacji; krok fundamentu (`SKILL.md:297-301`) dopuszcza takie pytanie, a krok powrotu (`SKILL.md:401-403`) mówi, że pytanie do człowieka nie jest odłożonym wpisem. Cykl zapisuje tryb awarii przy części tylko wtedy, gdy zleca go dokument zadania albo gdy człowiek w odpowiedzi na to pytanie podaje go albo przyjmuje z propozycji agenta — wtedy jako poprawkę otwartego requestu, przed scaleniem.
8. (AIR-480) WAY-46 i szablon mapy części (`elements/part-map/template.md:184`) mówią, że tryb awarii, który zleca dokument zadania albo który człowiek w odpowiedzi na pytanie cyklu podaje albo przyjmuje z propozycji agenta, zapisuje człowiek, niezależnie od tego, kto wpisuje go do pliku.
9. (AIR-481) Szablon zadania i `refine-task` mówią, że sposób wykonania wybiera plan cyklu albo wybory zapisu cyklu, gdy planu nie ma (brzmienie z `elements/decisions/template.md:120`): `project-level/task/template.md:88` → „The cycle's plan chooses how, or the choices of its cycle record where no plan is written.”; `project-level/task/template.md:93` i `project-level/task/skill/SKILL.md:120` → „…belongs to (stays with) the cycle's plan, or to the choices of its cycle record where no plan is written.”

### Questions to settle

- Pytanie 0: czy sprawy AIR-476–481 idą jednym zadaniem, choć każda jest osobną poprawką?
  - Answer: tak — jedna linia zadania na sprawy S7 z jednej sesji ai-review.
  - Source: Mariusz, 2026-10-20, sesja ai-review: „Mariusz: rób — pozycja wspólnej linii zadania S7 (jedna linia na sprawy AIR-476–482)” (`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md:221`); AIR-482 odrzucona tamże (`:1603`).
- Pytanie 1 (AIR-476): czy zawężenie „beyond what the approved task document or plan carries (WAY-30)” stoi tylko w kroku fundamentu cyklu, czy także w kroku 4.2 wspólnego sposobu pracy skilli wpisów, które krok fundamentu wywołuje?
  - Answer: w obu miejscach, a do tego zmiana fundamentu: WAY-30 zapisuje pierwszeństwo przed WAY-114 dla zmiany zatwierdzonej z dokumentem zadania albo planem (droga c). Odrzucone: zawężenie tylko w `SKILL.md:299` (agent piszący wpis skillem elementu dalej czyta w `way_of_working.md:158` „zapytaj”); zawężenie w obu plikach bez zmiany fundamentu (opiera się na odczytaniu WAY-114, którego ta decyzja sama nie zapisuje).
  - Source: Mariusz, 2026-10-20: „myślę, że chyba jednak poszedłbym w wariant c” — na drogi a/b/c przedstawione w rozmowie doprecyzowania.
  - Pytanie kontrolne: czy droga c trzyma się wobec oceny krytyki z zeszytu, że „WAY-30/1 (`decisions.md:870-872`) już uznaje zatwierdzone zadanie za zgodę, więc skill jest ostrzejszy od fundamentu” (`ai_review_ledger.md:221`)? Trzyma się — WAY-30 mówi, kiedy zapada zgoda, ale nie, że po niej agent nie pyta, a WAY-114 wymaga pytania przy każdej zmianie sensu; WAY-172/1, odchodząc od WAY-114 przez zgodę z WAY-30, zapisała pierwszeństwo wprost, więc odczytanie krytyki nie wystarcza. Mariusz, 2026-10-20: „tak, zostajemy przy c”.
- Pytanie 2 (AIR-480): przy jakim warunku cykl zapisuje kandydata na tryb awarii, skoro wiersz *Settlements to record* nie może nieść zmiany mapy części, i jak krok fundamentu i krok powrotu dopuszczają takie pytanie?
  - Answer: cykl zapisuje tryb awarii, gdy zleca go dokument zadania albo gdy człowiek podaje go w odpowiedzi na pytanie w requeście (poprawka otwartego requestu przed scaleniem), a WAY-46 i szablon mapy części mówią wprost, że taki tryb zapisuje człowiek, niezależnie od tego, kto wpisuje go do pliku (droga a+); krok fundamentu dopuszcza pytanie o kandydata, a krok powrotu nie traktuje go jako odłożonego wpisu. Odrzucone: zdanie z zeszytu „unless a row of *Settlements to record* carries it” (wiersz nie może nieść zmiany mapy części — `project-level/task/template.md:131-132`, WAY-134, więc warunek nigdy nie zachodzi); droga a bez zmiany WAY-46 (opiera się na odczytaniu „a human records/writes”); droga b — cykl nigdy nie zapisuje, przyjęty tryb idzie osobnym zadaniem (krytyczność części zaniżona do jego cyklu, kandydat ginie między scaleniem a nowym zadaniem).
  - Source: Mariusz, 2026-10-20: „a+ jak proponujesz” — na drogi a/a+/b przedstawione w rozmowie doprecyzowania.
  - Pytanie kontrolne: czy a+ trzyma się wobec WAY-46/1 „A part carries the failure modes a human records at it, each with the kind of damage it does, its severity, and how it is detected before release”, skoro samo „tak” w requeście wprowadza wagę i sposób wykrycia ocenione przez agenta jako zapis człowieka? Trzyma się, z dodanym warunkiem — propozycja agenta przychodzi z kontrargumentem (pytanie 3). Mariusz, 2026-10-21: „myślę, że tak; gdybym sam miał opisać ten tryb nie wiedziałbym jak to sensownie zrobić; przy takich przypadkach lepiej, żeby to zaproponował agent, a ja jeśli będę miał wątpliwości, to skoryguję; żeby było jeszcze bezpieczniej można by zawsze przy propozycji agenta dodawać kontrargument do tej propozycji - coś jak ten komentarz tutaj, żeby skłonić czytającego do głebszego zastanowienia się nad słusznością rozwiązania”.
- Pytanie 3 (AIR-480): czy kontrargument dołączany do propozycji agenta obejmuje tylko kandydata na tryb awarii, czy każde pytanie w *Questions* requestu?
  - Answer: w tym zadaniu tylko kandydat na tryb awarii — rekomendacja agenta przychodzi z najsilniejszym argumentem przeciw niej; kontrargument przy każdej propozycji agenta, wspólny dla wszystkich skilli the way (WAY-113, „How a skill asks”), idzie osobnym zadaniem w backlogu (droga c). Odrzucone: każde pytanie w *Questions* requestu w tym zadaniu (wychodzi poza poprawki S7, a ogólna reguła należy do sposobu pytania wspólnego dla skilli, nie do samego cyklu); sam tryb awarii bez osobnego zadania na uogólnienie.
  - Source: Mariusz, 2026-10-21: „niech będzie na ten moment c” — na drogi a/b/c przedstawione w rozmowie doprecyzowania.

## Context

- Źródło: rekordy AIR-476–481 w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md` (sekcje „Historia”, wpisy „sesja: krytyka … Przeredagowane … Mariusz: rób” z 2026-10-20); każda sprawa ma tam cytat z zapisu cyklu, diagnozę i rachunek.
- Zeszyt cytuje linie na `foundations` @ `d829e3a`; na obecnym czubku `f0b5eb1` wszystkie cytowane zdania stoją pod tymi samymi numerami linii (sprawdzone 2026-10-20).
- AIR-478: na czystym czubku `f0b5eb1` strażnik decyzji i strażnik niezmienników z `--base none --merge-onto origin/foundations` dają 0 błędów; błędy kopii wersji i zastępczego linku requestu pojawiają się dopiero na gałęzi zadania (pomiar krytyka z zeszytu, niepowtórzony).
- AIR-479: `task-cycle/skill/SKILL.md:55` przypina Superpowers 6.4.1 (WAY-125); nagłówek planu `### Slice 1 — <goal in a few words>` stoi w `task-cycle/plan/SKILL.md:75`; wzorzec `^#+ Task <n>` skryptu `task-brief` jest ten sam w 6.4.1 i 7.0.0 (krytyka w zeszycie).
- Części dotknięte zmianą: `decisions` (pkt 1, 8), `part-map` (pkt 8), `task-cycle` (pkt 2, 6, 7), `agent-instructions` (pkt 3, 5), `elements-common` (pkt 2, 4), `project-level` (pkt 9) — według przypisań plików w `foundations/part_map.md`.
- Wytyczne produktu: zmiana dotyka wyłącznie instrukcji w Markdownie — ani interfejsu, ani kodu w rozumieniu `product-guidelines/reading.md`; the-way nie ma katalogu `guidelines/`, więc wybór wytycznych jest pusty i nie ma braku do zgłoszenia.
- Opis żadnego skilla się nie zmienia, więc punktów wejścia (`agent-instructions/skill_entry_points.py`) nie trzeba generować na nowo.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-30/1 (`foundations/decisions.md:869`): „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the decision's approver before the code that needs it is made.” — pkt 1 i 2.
- WAY-114/1 (`foundations/decisions.md`, nagłówek „What does a human accept of an entry, and when?”): „Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision” — pkt 1 i 2, pytanie 1.
- WAY-25/1 (`foundations/decisions.md`, nagłówek „What settles a collision between two decisions?”): „the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails” — pkt 1.
- WAY-172/1 (`foundations/decisions.md:5725`): „derives from WAY-30@6924312f” i w swoim obszarze „prevails over WAY-114”: nowy sens wytycznych produktu wymaga zgody w dokumencie zadania, jak WAY-30, zanim powstanie kod, zamiast akceptacji przy scaleniu; zmiana WAY-30 zmienia odcisk, który WAY-172 niesie (WAY-31).
- WAY-10/1 (`foundations/decisions.md:317`): niezależny oceniający „sees the diff and the files of the commit it assesses without the task's chronicle or the author's reasoning” — pkt 3 i 4.
- WAY-46/1 (`foundations/decisions.md:1302`): „A part carries the failure modes a human records at it” — pkt 7 i 8; sześć niezmienników niesie jej odcisk `WAY-46@a5f43e40` (`foundations/invariants.md:763-813`), więc zmiana zdania wiążącego WAY-46 przechodzi przez nie (WAY-31).
- WAY-134/1 (`foundations/decisions.md:4046`): „A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on” — pkt 7, pytanie 2.
- WAY-31/1 i WAY-07/1: odciski relacji wobec zdania wiążącego oraz edycja wpisów w miejscu przed `main` — pkt 1 i 5.
- WAY-125/1 i WAY-148/1: Superpowers 6.4.1 w cyklu oraz „reusing a borrowed method's existing brief and report rather than duplicating them” — pkt 6.
- WAY-36/1: „…stays in the plan of that work, or in the choices of its cycle record where no plan is written” — pkt 9.

## Settlements to record

Candidates: 7 shown, 2 accepted — 2026-10-21

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zmiana decyzji zatwierdzona z dokumentem zadania albo planem — także jako wiersz *Settlements to record* — jest odpowiedzią, o którą WAY-114 każe pytać: agent piszący wpis nie pyta o sens, który dokument albo plan niesie, a pyta o to, co wykracza poza niego; w tym obszarze WAY-30 ma pierwszeństwo przed WAY-114. | decision | odpowiedź na pytanie 1 z pytaniem kontrolnym; To do 1 i 2 | czy zatrzymać cykl zablokowanym szkicem requestu, żeby zapytać o zmianę decyzji, którą zatwierdzone zadanie samo zleca, albo o wiersz, który zderza się z obecnym wpisem, bo ma go zmienić |
| 2 | Kandydat na tryb awarii, którego cykl znalazł przy części, idzie do człowieka jako pytanie w *Questions* requestu — z częścią, tym, co zawodzi, szkodą, wagą, sposobem wykrycia, rekomendacją i najsilniejszym argumentem przeciw niej — a tryb awarii, który zleca dokument zadania albo który człowiek w odpowiedzi podaje albo przyjmuje z propozycji agenta, zapisuje człowiek, niezależnie od tego, kto wpisuje go do pliku, i cykl wpisuje go poprawką otwartego requestu przed scaleniem. | decision | odpowiedzi na pytania 2 i 3 z pytaniem kontrolnym do pytania 2; To do 7 i 8 | czy kandydata pominąć jako „a human records failure modes”, odłożyć do osobnego zadania, czy wpisać samemu, i czy samo „tak” na propozycję agenta wystarcza, skoro szablon mapy części mówi „A human writes the failure modes” |

## Out of scope

- Najsilniejszy argument przeciw rekomendacji przy innych pytaniach niż kandydat na tryb awarii — osobne zadanie w backlogu, reguła wspólna dla skilli, które pytają człowieka (pytanie 3).
- Wariant 2 AIR-478 — flaga strażnika, która porównuje same odciski relacji bez drugiego commita; wraca dopiero, gdy czytanie czerwonego wyniku okaże się zawodne.
