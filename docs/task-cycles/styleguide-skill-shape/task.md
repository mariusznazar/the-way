---
title: "the way, seria skilli 4/11: maintain-styleguide w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-10-30
updated: 2026-10-30
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# maintain-styleguide w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `maintain-styleguide` the way (`product-guidelines/styleguide/SKILL.md`, 2830 słów na `foundations` `525cde1`) trzyma w `SKILL.md` także fragmenty potrzebne tylko na jednym kroku albo w jednym wariancie — np. sekcję „Orchestrated mode” (`product-guidelines/styleguide/SKILL.md:76–84`), której potrzebuje tylko sesja prowadzona przez `lead-project`, badania z kroku 2 (`:128–143`), potrzebne tylko przy pierwszym styleguide bez preferencji człowieka i przy rozszerzeniu, oraz audyt z kroku 3 (`:151–168`), potrzebny tylko produktowi z ekranami — choć WAY-256 każe takie fragmenty trzymać w plikach obok.
- Agenci nieśli tekst katalogu `product-guidelines/styleguide/` przez ok. 5,4 mln tokenów od 2026-09-01 — czwarty wynik serii (miara serii, `ranking_2026-10-28.txt`).
- Krok 0 skilla każe na wejściu przeczytać ok. 6000 słów z innych plików, dwa razy tyle co sam `SKILL.md`, w tym ok. 2350 słów, które sesja wczytała już w krokach 1 i 2 `refine-task`.
- Plik, którym cykl ocenia skill, daje dla kroku, do którego dochodzi każde użycie, dwie sprzeczne odpowiedzi (`instruction-files/kind_skill.md:11` i `:13`), a WAY-256 tylko jedną.

### To do

1. `maintain-styleguide` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym wariancie — w pliku obok w `product-guidelines/styleguide/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256).
2. Krok 0 (`product-guidelines/styleguide/SKILL.md:88–91`) przestaje kazać czytać wszystko naraz: każdy plik, który wymienia, jest czytany na kroku, który go potrzebuje, a to, co sesja przeczytała już w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz.
3. `instruction-files/kind_skill.md:8–14` mówi to samo co WAY-256: w `SKILL.md` zostaje to, czego potrzebuje każdy krok, a fragment jednego kroku idzie do pliku obok także wtedy, gdy dochodzi do niego każde użycie skilla.
4. Request zadania podaje tabelę oceny skilla — fragment zacytowany dosłownie z zakresem linii na `525cde1`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt — i liczby słów czytanych przed przebudową i po niej w siedmiu drogach: pierwszy styleguide bez ekranów, człowiek bez preferencji; to samo, człowiek z preferencją; pierwszy styleguide, są ekrany; odświeżenie bez zmienionych ekranów; rozszerzenie ze zmienionymi ekranami; tryb orkiestrowany na pierwszej z tych dróg; produkt bez interfejsu, koniec na kroku 1. Na każdej drodze dwie liczby: tekst wczytany przed krokiem 4 i suma na koniec przebiegu; plik czytany dwa razy w stanie „przed” liczy się dwa razy. Werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Kod w Pythonie się nie zmienia.

### Questions to settle

- 1. Co oprócz `product-guidelines/styleguide/SKILL.md` przebudowa może ruszyć: sam ten plik, także to, kiedy każe czytać pozostałe pliki z kroku 0, czy także `product-guidelines/styleguide/template.md`?
  - Answer: `SKILL.md` i to, kiedy każe czytać pozostałe pliki z kroku 0 (To do 1 i 2); same te pliki się nie zmieniają.
  - Not chosen:
    - zostawić skill jak jest — łamie WAY-256, a seria traci ogniwo będące wzorem dla zadań 5 i 8.
    - tylko `SKILL.md`, krok 0 bez zmian — ok. 8270 słów na drodze bez badań i audytu wobec dzisiejszych ok. 8850 (−6%); większość tekstu czytanego na wejściu zostaje.
    - także podział `template.md`, z częścią dla autora w cyklu w pliku obok — dotyka pliku, z którego korzystają autor i recenzent w cyklu, nazwę sekcji „Writing the file” skill wpisuje do opisów zadań w produktach (`product-guidelines/styleguide/SKILL.md:50`), WAY-256 nie obejmuje szablonu, a zysk to najwyżej 460 słów.
  - Source: Mariusz, 2026-10-30: „B” — na drogę o szacunku ok. 5900 słów (−33%), ze słabym punktem pokazanym w pytaniu: szablon może być potrzebny już w krokach 2 i 3, więc ocena sprawdza to dla każdego pliku. Liczby to szacunek z liczenia słów na `525cde1`: `SKILL.md` 2830, pliki kroku 0 ok. 6000, z tego ok. 2350 przeczytane już przez `refine-task` (`project-level/task/skill/read_sources.md:3–4`).
- 2. Czy procedura kroku, do którego dochodzi każdy przebieg, idzie do pliku obok, skoro notatka serii i blok przekazania zadania 3 mówią o tym co innego?
  - Answer: tak — procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, kroki 0 i 1 włącznie, a fragment z jedną instrukcją zostaje w miejscu odsyłacza; WAY-256 się nie zmienia. W `SKILL.md` zostaje ok. 600 słów: obraz całości, zasady wspólne dla kroków i odsyłacze.
  - Not chosen:
    - zostawić obie wersje notatki serii bez rozstrzygnięcia — cykl sam wybierze jedno z dwóch źródeł, a recenzent może ocenić ten wybór według drugiego; zadania 5 i 8 trafią na to samo.
    - kroki każdego przebiegu zostają w `SKILL.md` — główny plik ok. 2250 słów i ok. 4 pliki obok, ale niezgodne z brzmieniem WAY-256 i z układem zadania 2, a przez kroki 0–3 agent ma w polu widzenia ok. 700 słów procedury rozmowy z człowiekiem.
    - odpowiedź z wyjątkiem „fragment potrzebny od pierwszego kroku zostaje w `SKILL.md`” bez zmiany WAY-256 — główny plik ok. 1000–1100 słów, ale stoi w sprzeczności z decyzją, którą recenzent cyklu czyta jako wiążącą, więc uwaga blokująca jest prawdopodobna.
    - ten sam wyjątek dopisany do WAY-256 — decyzja dostaje trzecią klauzulę dla oszczędności ok. 50 słów, PR wychodzi poza przebudowę, a granicę „pierwszego kroku” trzeba by dopiero nazwać, żeby nie cofnęła `slice.md` z zadania 1.
  - Source: Mariusz, 2026-10-30: „wszystko zgodnie z rekomendacjami” — na drogę „WAY-256 bez zmian, kroki 0 i 1 też idą obok”, ze słabymi punktami pokazanymi w pytaniu: ok. 50 słów więcej w sumie, 1–2 pliki więcej, a tekst czytany zaraz po `SKILL.md` nic nie zyskuje na przeniesieniu. Zastępuje wcześniejszą odpowiedź tego samego dnia, „tak jak rekomendujesz”, daną na drogę z wyjątkiem, którą rekomendacja błędnie opisała jako zgodną z WAY-256 i zadaniami 2 i 3; sprzeczność wykazał krytyk tabeli kandydatów. Oszczędność tokenów dotyczy tylko wywołań przed krokiem, który plik wymienia, i nie jest zmierzona. Źródła w sprzeczności: notatka serii „Przy ocenie skilla fragment potrzebny w każdym przebiegu danego agenta zostaje w `SKILL.md`” przeciw jej blokowi przekazania „Samo użycie fragmentu we wszystkich trybach nie oznacza, że jest potrzebny przez wszystkie kroki”; WAY-256: „that only one step or one variant of the skill needs stands in a file beside the skill”. Uwaga w notatce serii poprawiona tego samego dnia.
- 2a. Czy zadanie poprawia `instruction-files/kind_skill.md`, skoro jego linie 11 i 13 dają dla kroku, do którego dochodzi każde użycie, dwie sprzeczne odpowiedzi?
  - Answer: tak — To do 3.
  - Not chosen:
    - zostawić plik bez zmian — zadania 5–11 trafią na tę samą dwuznaczność, bo cykl ocenia skill właśnie tym plikiem.
  - Source: Mariusz, 2026-10-30: „wszystko zgodnie z rekomendacjami” — z kosztem pokazanym w pytaniu: PR dotyka jednego pliku części `instruction-files` poza samym skillem. Cytat: `instruction-files/kind_skill.md:11` „**every use needs it** — it stays in `SKILL.md`”, `:13` „**only one step or one variant needs it** — it stands in a file beside the skill”.
- 3. W jakich drogach użycia request liczy słowa czytane przed przebudową i po niej?
  - Answer: w siedmiu z To do 4, na każdej tekst wczytany przed krokiem 4 i suma na koniec przebiegu; plik czytany dwa razy w stanie „przed” liczy się dwa razy.
  - Not chosen:
    - jedna liczba na skill albo sama suma końcowa — zysk z pytania 2 byłby niewidoczny, bo leży przed krokiem 4.
    - liczenie „każdy plik raz” — zniknęłoby ok. 2350 słów z pytania 1.
  - Source: Mariusz, 2026-10-30: „przyjmuję”.
- 4. Czym mierzymy niesiony tekst po scaleniu?
  - Answer: sesja domykająca uruchamia `skille_po_kolei_dane/guidelines_carry_cost.py`, który liczy każdy plik `.md` pod `product-guidelines/` osobno, na zapisach od dnia scalenia i porównuje z `ranking_wytyczne_2026-10-30.txt`; punktem odniesienia jest też wynik skryptu serii `skill_carry_cost.py`.
  - Not chosen:
    - sam skrypt serii — liczy katalog jako całość, więc nie odróżni `SKILL.md` od szablonu.
  - Source: Mariusz, 2026-10-30: „przyjmuję” — ze słabym punktem pokazanym w pytaniu: żaden ze skryptów nie widzi powtórnych odczytów plików spoza `product-guidelines/`, a użyć było mało, więc porównanie może długo pozostać puste i główną miarą zostają słowa z requestu. Punkt odniesienia z 2026-10-30 (2083 zapisy sesji od 2026-09-01): `styleguide/SKILL.md` 3,3 mln tokenów, `styleguide/template.md` 2,9.
- 5. Czy agenci cyklu czytają metody z worktree zadania, jak w zadaniach 2 i 3?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `maintain-styleguide`, więc przebudowa skilla nie zmienia niczego, czym cykl pracuje. Wyjątkiem jest `instruction-files/kind_skill.md` z To do 3, którym cykl ocenia skill: zmiana idzie w stronę odpowiedzi na pytanie 2, więc ocena daje ten sam wynik przed nią i po niej.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: Mariusz, 2026-10-30: „przyjmuję”.
- 6. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 2 i 3 serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi.
  - Source: Mariusz, 2026-10-30: „przyjmuję”; to samo rozstrzygnięcie w zadaniu 3 (`_zadania/zadanie_skille_the_way_3_fundament.md`, *Questions to settle*, pytanie 5).

## Context

- Zadanie jest czwartym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię na następne) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Podstawą jest `foundations` po PR #58, commit `525cde1dd53c474f56ea0ece289cb60e868aa90d`; wzór oceny i tabel: zadanie 3 (PR #52, https://github.com/mariusznazar/the-way/pull/52).
- Liczba 5,4 mln z miary serii obejmuje każdy plik `.md` katalogu `product-guidelines/styleguide/`, czyli też `template.md`; kopia skryptu serii policzona 2026-10-30 po plikach daje `SKILL.md` 3,3 mln i `template.md` 2,9 mln (kopia łapie ścieżki szerzej, więc suma przewyższa 5,4).
- Tekst trybu orkiestrowanego jest prawie taki sam w `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md` i `product-guidelines/coding/SKILL.md`; każdy skill dostaje własny plik obok, a ewentualne scalenie jest sprawą zadania 8.
- `SKILL.md` przeczytało w całości 20 zapisów sesji od 2026-09-01: 7 w `loop2` (rzeczywiste użycia) i 13 w repo the way, głównie agenci zmieniający albo oceniający sam skill.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill (To do 1).
- **WAY-258** (fragment) — „No rule stands in two of its files, and no file of a kind holds a rule another kind needs […]” — nie zmienia się; To do 3 poprawia zdanie w miejscu, nie dokłada drugiego.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.
- **WAY-185** (fragment) — „Before anything else, the skill `maintain-styleguide` recognizes which user interface the styleguide is for and what the product already has for it — a file of design tokens its screens read, one nothing reads, shared components, or nothing — and whether it has screens and a styleguide, and it extends what exists rather than bringing a new system.” — nie zmienia się; wiąże kolejność kroku 1, więc przenoszone czytanie nie może jej odwrócić.
- **WAY-186** (fragment) — „It researches at every extension and never at a refresh (WAY-251), and a tool the human prefers remains the one proposed, never displaced by research.” — nie zmienia się; wyznacza warunek wariantu badań.
- **WAY-187** (fragment) — „For a product that has screens, the skill `maintain-styleguide` audits the user interface in both directions — from the source of values to the screens that read them, and from each value on a screen to the design token or component meant to cover it […]” — nie zmienia się; wyznacza warunek wariantu audytu.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; `critique/SKILL.md` przestaje być czytany na kroku 0, ale obie krytyki zostają.
- **WAY-154** (fragment) — „[…] the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`.” — nie zmienia się; opisuje tryb, którego sekcja „Orchestrated mode” idzie do pliku obok.
- **WAY-172** (fragment) — „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it […]” — nie zmienia się; sekcja „What reaches the task document” niesie ją dalej, gdziekolwiek stanie.

## Settlements to record

Candidates: 7 shown, 0 accepted — 2026-10-30

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 4/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 5 i ustawić linii „seria skilli 5/11” datę dnia domknięcia; do „Otwartych wątków” wchodzą też wynik `skille_po_kolei_dane/guidelines_carry_cost.py` na zapisach od dnia scalenia, porównany z `ranking_wytyczne_2026-10-30.txt` (pytanie 4), i sprawa ewentualnego scalenia plików trybu orkiestrowanego trzech skilli wytycznych w zadaniu 8.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Treść plików, które skill każe czytać: `product-guidelines/template.md`, `product-guidelines/styleguide/template.md`, `project-level/task/skill/SKILL.md`, `project-level/task/template.md`, `elements/common/way_of_working.md`, `elements/common/critique/SKILL.md` (pytanie 1).
- Pozostałe skille the way — zadania 5–11 serii, także `maintain-testing-guidelines` i `maintain-coding-guidelines`, które mają ten sam układ sekcji.
