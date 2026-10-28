---
title: "the way, seria skilli 2/11: refine-task w kształcie WAY-256, z plikami wejściowymi w produktach czytającymi pliki obok na ich kroku"
status: draft
created: 2026-10-28
updated: 2026-10-28
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# refine-task w kształcie WAY-256, z plikami wejściowymi w produktach czytającymi pliki obok na ich kroku

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `refine-task` the way (`project-level/task/skill/SKILL.md`, 2933 słowa na `foundations` `3aee7d9`) trzyma w `SKILL.md` także fragmenty potrzebne tylko w jednym trybie albo wariancie — np. sekcję „Orchestrated mode” (`project-level/task/skill/SKILL.md:16–59`), której potrzebuje tylko agent wysłany przez `lead-project` — choć WAY-256 każe takie fragmenty trzymać w plikach obok.
- Agenci nieśli tekst `refine-task` przez ok. 19,8 mln tokenów od 2026-09-01, z czego 9,2 mln w sesjach w repo the way — drugi wynik wśród skilli the way (miara serii, `ranking_2026-10-28.txt`).
- `refine-task` nie jest etapem cyklu, więc WAY-125 go nie obejmuje: sesja dochodzi do niego przez plik wejściowy skilla. W produkcie ten plik pisze instalator i mówi „Read the files it references inside `.the-way`.” bez słowa o tym, kiedy (`installation/install.py:136` na `3aee7d9`), więc sesja może wczytać na starcie wszystkie pliki obok skilla i przeniesienie fragmentów nic by nie dało. Tak samo dochodzi do `implement-task` orkiestrator cyklu w produkcie (uwaga O1 recenzenta PR #50).

### To do

1. Pliki wejściowe skilli the way, które instalator zapisuje w produkcie, każą czytać plik wymieniony przez skill z `.the-way` dopiero wtedy, gdy przychodzi krok albo wariant, który go wymienia — nie wszystkie na starcie:
   - zdanie w `installation/install.py:135–136` brzmi: „Read `.the-way/<path>` in full and follow it, and read a file it names inside `.the-way` when the step or variant that names it comes, not all of them at the start.”;
   - opis pliku wejściowego w `installation/README.md:57` mówi, że czyta on „its source skill from `.the-way`, and each file the skill names there when the step that names it comes”;
   - test `installation/test_install.py:123`, który przechodzi po plikach wejściowych wszystkich skilli, sprawdza w każdym, że nowe zdanie w nim stoi, a „Read the files it references” nie;
   - dziennik decyzji the way dostaje decyzję z wiersza 1 *Settlements to record*.
2. `refine-task` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym wariancie — w pliku obok w `project-level/task/skill/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256).
3. Request zadania podaje tabelę oceny `refine-task` — fragment, kiedy jest potrzebny i czy agent rozpozna ten moment, werdykt — i to, ile słów czyta sesja `refine-task` przed przebudową i po niej w trzech wariantach: ręczne doprecyzowanie zadania niezależnego, ręczne doprecyzowanie zadania z planu projektu i tryb orkiestrowany (agent wysłany przez `lead-project`); werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.

### Acceptance criteria

- Żadna reguła `refine-task` nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Kod w Pythonie zmienia się tylko w zdaniu pliku wejściowego w `installation/install.py` i w teście tego zdania (To do 1).

### Questions to settle

- Czy zmiana zdania w plikach wejściowych w produktach zmienia też decyzję the way, a jeśli tak — którą?
  - Answer: tak — nowa, wąska decyzja w zakresie `installation`: plik wejściowy, który instalator zapisuje w produkcie, każe czytać skill w całości, a plik, który skill wymienia w `.the-way`, dopiero na kroku albo w wariancie, który go wymienia; wynika z WAY-256, ze sprawdzeniem w kształcie WAY-127; WAY-127 zostaje bez zmian.
  - Source: Mariusz, 2026-10-28: „ok, niech będzie C” — wybór spośród: A — tylko kod, zdanie, opis i test, bez decyzji (słaby punkt: reguła w produktach żyje tylko w kodzie, kolejna zmiana instalatora może ją po cichu cofnąć, a recenzent nie ma decyzji do porównania); B — rozszerzyć WAY-127 o produkty (zmienia pytanie i znaczenie decyzji zmienionej w zadaniu 1, miesza dwie drogi, które jej *Rejected* rozdziela); C — nowa wąska decyzja (słaby punkt: ta sama reguła w trzech decyzjach — WAY-125, WAY-127 i nowej). Żadna decyzja z *Scope* obejmującym `installation` (WAY-09, 27, 34, 38, 89, 100, 102, 107, 127, 141, 167 na `3aee7d9`) nie mówi o treści pliku wejściowego w produkcie; WAY-127, `foundations/decisions.md:2918` na `3aee7d9`: „How does a session working on the-way itself reach the-way's skills?”.
- Jakie słowa ma nowe zdanie pliku wejściowego w produkcie i jak sprawdza je test?
  - Answer: brzmienie generatora wejść the way z „inside `.the-way`” zamiast „under the same root”, opis w README w tym samym sensie, a test plików wejściowych wszystkich skilli sprawdza obecność nowego zdania i brak starego (To do 1).
  - Source: Mariusz, 2026-10-28: „przyjmuję” — na propozycję trzech punktów To do 1, przeciw drodze „znaczenie w opisie, słowa wybiera cykl” (słaby punkt: dwa sformułowania tej samej reguły w the way i w produktach). Wzór: `agent-instructions/skill_entry_points.py:175` na `3aee7d9`: „read a file it names under the same root when the step or variant that names it comes, not all of them at the start”; dziś drugiego zdania nie sprawdza żaden test, pierwsze — trzy testy wytycznych (np. `installation/test_coding_guidelines_installation.py:93`).
- Czy zadanie, które przez To do 1 zmienia kod w Pythonie, czeka na wytyczne kodowania samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadanie 1 serii; wybór wytycznych jest pusty, a kod w Pythonie zmienia się tylko w zdaniu pliku wejściowego i jego teście.
  - Source: Mariusz, 2026-10-28: „przyjmuję” (punkt a) — przeciw drodze „czekać na rozstrzygnięcie wytycznych samego the way” (seria stoi). To samo rozstrzygnięcie w zadaniu 1: `_zadania/zadanie_skille_the_way_1_cykl_zadania.md`, *Questions to settle*, pytanie o wytyczne kodowania (Mariusz, 2026-10-28, „A”).
- Czy agenci cyklu czytają metody etapów z kopii the way na commicie bazowym, jak w zadaniu 1?
  - Answer: nie — z worktree zadania, zwykłą drogą cyklu; cykl nie używa `refine-task` ani pliku wejściowego instalatora, więc przebudowa nie zmienia niczego, czym cykl pracuje.
  - Source: Mariusz, 2026-10-28: „przyjmuję” (punkt b) — przeciw kopii na commicie bazowym (krok więcej bez ochrony w zamian). `task-cycle/` na `3aee7d9` nie wymienia `refine-task` ani `project-level/task/skill`; instalator wymienia tylko przy przesuwaniu przypięcia w produkcie (`task-cycle/skill/SKILL.md:41–43`).
- Kto projektuje układ `refine-task` po przebudowie i gdzie Mariusz widzi tabelę oceny?
  - Answer: cykl — ocenia skill skillem `the-way-maintain-instruction-files` i rozkłada fragmenty sam, z układami zadania 1 jako wzorem; pliki obok kładzie w `project-level/task/skill/`; Mariusz widzi tabelę oceny i liczby czytanych słów w requeście.
  - Source: Mariusz, 2026-10-28: „przyjmuję” (punkt c) — przeciw tabeli w doprecyzowaniu (kilka godzin sesji, opis zadania staje się projektem wykonania wbrew `project-level/task/skill/SKILL.md:239` na `3aee7d9`).
- W jakich wariantach request liczy słowa czytane przed przebudową i po niej?
  - Answer: w trzech — ręczne doprecyzowanie zadania niezależnego, ręczne doprecyzowanie zadania z planu projektu, tryb orkiestrowany (To do 3).
  - Source: Mariusz, 2026-10-28: „przyjmuję” (punkt d) — przeciw jednej liczbie dla całego skilla, która nie pokaże, w którym wariancie przebudowa daje zysk.

## Context

- Zadanie jest drugim z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię na następne) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Poprawka instalatora idzie z tym zadaniem z decyzji Mariusza, 2026-10-28: „poprawka instalatora idzie razem z zadaniem 2” (notatka serii, „Otwarte wątki / decyzje”).
- Wzór oceny i tabel: zadanie 1 serii, PR #50 (https://github.com/mariusznazar/the-way/pull/50) — tabele ocen pięciu skilli w komentarzach PR-a, liczby słów przed i po w opisie.
- Miara serii (`Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/skill_carry_cost.py`) liczy każdy plik `.md` w katalogu `project-level/task/skill/`, więc plik obok położony w tym katalogu wchodzi do porównania po scaleniu, a plik położony gdzie indziej — nie.
- Plik wejściowy w produkcie zmienia się dopiero, gdy produkt przesunie przypięcie the way i uruchomi instalator z nowej wersji — instalator przepisuje wtedy swoje pliki wejściowe (kontrakt `installation-command` w `foundations/part_map.md`).
- Szablon rozmowy `project-level/lead/conversation_template.md:66` wskazuje agentowi trybu orkiestrowanego `project-level/task/skill/SKILL.md - orchestrated mode`; agent ten nie dochodzi do skilla przez plik wejściowy.
- WAY-128 kończy się zdaniem „the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256 instead” (`foundations/decisions.md:2997` na `3aee7d9`) — nowa decyzja z wiersza 1 *Settlements to record* jest kolejną, której pliki wejściowe podlegają.

## Questions carried to cycle

- Czy `project-level/task/template.md` (1580 słów na `3aee7d9`), który `refine-task` każe czytać w całości na kroku 1 (`project-level/task/skill/SKILL.md:63`), jest oceniany razem z `SKILL.md`; miara serii go nie liczy, bo leży poza `project-level/task/skill/`.

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — według niej przebudowuje się `refine-task` (To do 2); nowa decyzja z To do 1 z niej wynika.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.”
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — nie zmienia się; ta sama reguła dla repo the way, wzór nowej decyzji i jej sprawdzenia.
- **WAY-34** (fragment) — „A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit.” — nie zmienia się; dlatego nowe zdanie dociera do produktu dopiero z przesunięciem przypięcia.

## Settlements to record

Candidates: 7 shown, 1 accepted — 2026-10-28

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Plik wejściowy, który instalator zapisuje w produkcie, każe czytać skill w całości, a plik, który skill wymienia w `.the-way`, dopiero na kroku albo w wariancie, który go wymienia — nie wszystkie na starcie; to nowa decyzja w zakresie `installation`, wynikająca z WAY-256, sprawdzana parą przykładów „complies / violates” jak WAY-127, a WAY-127 zostaje bez zmian. | decision | Questions to settle — pytanie o decyzję (Mariusz, 2026-10-28, „ok, niech będzie C”, z odrzuconymi A i B); przyjęte przez Mariusza 2026-10-28: „tak, zostawiamy 1” | czy dopisać regułę do WAY-127, zmieniając jej pytanie, czy pisać osobną decyzję, i czy sprawdzać ją niezmiennikiem, czy parą przykładów |

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 2/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 3 i ustawić linii „seria skilli 3/11” datę dnia domknięcia.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- `elements/common/way_of_working.md` i pozostałe pliki, które `refine-task` wymienia, a które czytają też inne skille — `product-guidelines/reading.md`, `project-level/lead/conversation_template.md`, `project-level/plan/template.md`.
- Pozostałe skille the way — zadania 3–11 serii.
