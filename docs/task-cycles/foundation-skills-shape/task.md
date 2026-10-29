---
title: "the way, seria skilli 3/11: sześć małych skilli fundamentu w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-10-28
updated: 2026-10-28
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Sześć małych skilli fundamentu w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Sześć skilli fundamentu the way — `record-decision` (`elements/decisions/skill/SKILL.md`, 748 słów na `foundations` `745a6e5`), `record-invariant` (`elements/invariants/skill/SKILL.md`, 970), `record-glossary-term` (`elements/glossary/skill/SKILL.md`, 815), `record-environment-fact` (`elements/environment-facts/skill/SKILL.md`, 855), `update-part-map` (`elements/part-map/skill/SKILL.md`, 900) i `critique` (`elements/common/critique/SKILL.md`, 766) — trzyma w `SKILL.md` także fragmenty potrzebne tylko w jednym trybie albo wariancie, np. sekcję „Projected mode” w każdym z pięciu skilli wpisów (`elements/decisions/skill/SKILL.md:59–75`), „A withdrawal” (`elements/environment-facts/skill/SKILL.md:80–84`) i „The first map of a product” (`elements/part-map/skill/SKILL.md:80–86`), choć WAY-256 każe takie fragmenty trzymać w plikach obok.
- Agenci nieśli tekst tych sześciu `SKILL.md` przez ok. 14,5 mln tokenów od 2026-09-01 — trzeci wynik serii (miara serii, `ranking_2026-10-28.txt`).
- Każdy z pięciu skilli wpisów jest dopiskiem do wspólnego sposobu pracy: „Follow the steps of `elements/common/way_of_working.md` there; below is what a decision adds to each.” (`elements/decisions/skill/SKILL.md:17–18`), a krok 1 tego pliku każe przeczytać w całości szablon elementu, `elements/common/rules.md` i sam `way_of_working.md` (`elements/common/way_of_working.md:39`) — razem kilka razy więcej tekstu niż sam `SKILL.md`, którego miara serii nie liczy.

### To do

1. Sześć skilli jest ocenionych skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowanych według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym trybie lub wariancie — w pliku obok w katalogu skilla (`elements/<element>/skill/`, `elements/common/critique/`), który ten krok albo tryb wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256).
2. `elements/common/way_of_working.md` jest oceniony tak samo i przebudowany według tej oceny: fragment potrzebny tylko w jednym trybie albo wariancie — przede wszystkim sekcja „Projected mode” (`elements/common/way_of_working.md:154–185`, 416 z 2173 słów) — stoi w pliku obok w `elements/common/`, który ten tryb albo wariant wymienia; sekcje, do których odsyłają po nazwie pliki spoza części fundamentu („How a skill asks”, „Reading the foundation” i inne), zostają w `way_of_working.md` pod tą samą nazwą, a ich przeniesienie ocena może pokazać w requeście tylko jako propozycję.
3. Request zadania podaje tabelę oceny każdego skilla — fragment zacytowany dosłownie z zakresem linii na `745a6e5`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt — i liczby słów czytanych przed przebudową i po niej (słowa w plikach skilla, `way_of_working.md` i plikach obok czytanych na danej drodze, każdy plik raz), osobno dla dróg: wpis do fundamentu i wpis projektowany do definicji projektu dla każdego z pięciu skilli wpisów; wycofanie faktu w `record-environment-fact`; pierwsza mapa w `update-part-map`; w `critique` krytyk oraz autor, który zleca krytykę i rozstrzyga jej uwagi — z szablonem elementu i `elements/common/rules.md` podanymi raz, jako stały dodatek do każdej drogi; werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok, tryb albo wariant, w którym jest potrzebny.
- Żadna reguła wpisu nie trafia do pliku obok skilla elementu: reguły wpisów zostają w szablonie elementu albo w `elements/common/rules.md` (WAY-35, WAY-256).
- Każdy odsyłacz do pliku obok nazywa swój krok, tryb albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla — tak czytają skille elementów agenci kroku fundamentu i kroku powrotu cyklu.
- Każdy plik, który odsyła do przeniesionego fragmentu albo czyta `way_of_working.md` w całości — np. „Read `elements/common/way_of_working.md` in full” (`elements/common/skill/SKILL.md:41`) i „Projected mode runs as `elements/common/way_of_working.md` gives it” w pięciu skillach wpisów (`elements/decisions/skill/SKILL.md:61`) — dalej dochodzi do niego w tych samych przypadkach co przed przebudową.
- Kod w Pythonie się nie zmienia.

### Questions to settle

- 1. Gdzie kończy się zakres oceny i przebudowy: same sześć `SKILL.md`, także `elements/common/way_of_working.md`, czy także szablony elementów i `elements/common/rules.md`?
  - Answer: sześć `SKILL.md` i `elements/common/way_of_working.md` (To do 1 i 2); sekcje `way_of_working.md`, do których odsyłają pliki spoza części fundamentu, zostają na miejscu; szablony elementów i `elements/common/rules.md` są poza zakresem.
  - Source: Mariusz, 2026-10-28: „ok B” — wybór spośród: A — tylko sześć `SKILL.md`, jak zakłada seria (słaby punkt: zysk kilkuset słów na skill, a wspólna masa zostaje poza każdym zadaniem serii); B — A i fragmenty `way_of_working.md` potrzebne tylko w jednym trybie (słaby punkt: PR dotyka części wspólnej, czytanej też przez orkiestratora i recenzenta cyklu); C — B i szablony z `rules.md` (zmienia znaczenie WAY-150: „the whole reading of templates, rules and examples keep their domain”, i WAY-35). Pomiar kopią skryptu serii, liczącą także pliki wspólne, od 2026-09-01: sześć `SKILL.md` 23,6 mln tokenów, `way_of_working.md` 33,5, `rules.md` 11,0, pięć szablonów 63,5; kopia łapie ścieżki szerzej niż skrypt serii (14,5 dla sześciu skilli), a pliki wspólne czytają też inne skille.
- 2. Czy zadanie dopisuje regułę, kiedy czytać plik obok skilla elementu albo `critique`, dla agentów, którzy czytają te skille po ścieżce, a nie przez plik wejściowy?
  - Answer: nie — każdy odsyłacz do pliku obok nazywa swój krok, tryb albo wariant słowami, które agent rozpozna (kryterium akceptacji), a to, czy agenci cyklu otwierają pliki obok skilli elementów poza ich krokiem, pokazują zapisy sesji zmierzonego cyklu na `loop2`.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — bez nowej reguły (słaby punkt: agent cyklu może otworzyć na starcie plik trybu projektowanego i stracić zysk na tej drodze, nie gubiąc niczego, czego potrzebuje); B — zdanie o momencie czytania w kroku 1 `way_of_working.md` i w `critique`, z nowym wierszem decyzji (czwarta decyzja z tą samą regułą obok WAY-125, WAY-127 i WAY-259). Droga cyklu: `task-cycle/skill/SKILL.md:140` na `745a6e5` — „the agent reads each whole, and the skill of an element when it writes an entry of that element”; tryb projektowany wywołują `find-foundation-entries`, `define-project` i `settle-technology` przez skille z przedrostkiem `the-way-`.
- 3. Czy agenci cyklu czytają metody i skille fundamentu z kopii the way na commicie bazowym, jak w zadaniu 1, czy z worktree zadania, jak w zadaniu 2?
  - Answer: z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; metody cyklu się nie zmieniają, sekcje `way_of_working.md`, które czytają orkiestrator i recenzent całej zmiany, zostają na miejscu, a wynoszone fragmenty to tryby, których cykl nie używa.
  - Source: Mariusz, 2026-10-28: „jeśli uważasz, że B jest lepsze to spoko, dla mnie to żadna różnica” — na rekomendację B (worktree zadania) przeciw A (kopia na `745a6e5`, krok więcej na starcie; chroni tylko wpis fundamentu zapisany skillem przebudowanym w połowie). Orkiestrator i recenzent czytają „Reading the foundation” z `elements/common/way_of_working.md` (`task-cycle/skill/SKILL.md:56`, `task-cycle/review/SKILL.md:27` na `745a6e5`).
- 4. W jakich drogach użycia request liczy słowa czytane przed przebudową i po niej, i czym po scaleniu mierzymy niesiony tekst?
  - Answer: request liczy słowa w drogach z To do 3; po scaleniu sesja domykająca uruchamia `skille_po_kolei_dane/shared_carry_cost.py`, który liczy każdy plik `.md` pod `elements/`, pliki obok dodane w tym zadaniu też, na zapisach od dnia scalenia i porównuje z `ranking_fundament_2026-10-28.txt`; skrypt serii `skill_carry_cost.py` liczy tylko katalogi skilli i zysku z `way_of_working.md` nie widzi.
  - Source: Mariusz, 2026-10-28: „ok przyjmuję propozycje” — na propozycję dróg liczenia i zapisu kopii skryptu z punktem odniesienia, przeciw jednej liczbie na skill i porównaniu samym skryptem serii (pokazałoby tylko zysk w `SKILL.md`). Punkt odniesienia z 2026-10-28 (2170 zapisów sesji od 2026-09-01): `way_of_working.md` 33,6 mln tokenów, `rules.md` 11,0, szablony z przykładami 64,3, pięć `SKILL.md` skilli wpisów 19,9, `critique` 3,9.
- 5. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1 i 2 serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Source: Mariusz, 2026-10-28: „tak” — na tę samą odpowiedź co w zadaniu 2 (`_zadania/zadanie_skille_the_way_2_refine_task.md`, *Questions to settle*, pytanie o wytyczne kodowania: Mariusz, 2026-10-28, „przyjmuję” (punkt a)), przeciw czekaniu na wytyczne samego the way (seria stoi).

## Context

- Zadanie jest trzecim z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię na następne) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Podstawą jest `foundations` po PR #51, commit `745a6e53ec5c8eab3e078a32a61aa6a583a61a93`; wzór oceny i tabel: zadanie 1 (PR #50, https://github.com/mariusznazar/the-way/pull/50) i zadanie 2 (PR #51, https://github.com/mariusznazar/the-way/pull/51).
- Cykl dochodzi do skilli elementów po ścieżce w przypiętym the way, nie przez plik wejściowy: „the agent reads each whole, and the skill of an element when it writes an entry of that element” (`task-cycle/skill/SKILL.md:140–141`) i „an agent writing a foundation entry reads as the element's skill gives” (`task-cycle/skill/SKILL.md:157–158`); WAY-125 obejmuje metody etapów, WAY-127 i WAY-259 — pliki wejściowe, więc żadna z nich nie mówi, kiedy taki agent czyta plik obok skilla elementu.
- `critique` nie jest wywoływany w cyklu (`task-cycle/` na `745a6e5` go nie wymienia); wywołują go `define-project`, `plan-project`, `lead-project`, `settle-technology`, trzy skille wytycznych i `way_of_working.md` („Critique before collective review”), każdy przez świeżego agenta ze ścieżką `elements/common/critique/SKILL.md`.
- WAY-150 kończy się zdaniem „the search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep their domain” — szablony, `rules.md` i przykłady czyta się w całości z decyzji; `way_of_working.md` czyta się w całości tylko z jego własnego kroku 1.
- Przebudowa trzyma się dwóch niezmienników the way: `skill-rule-source` — „Every element's skill names its element's template and `elements/common/` as the source of the rules of its entries, and `elements/common/` as the source of the way of working the skills share.” — i `skill-entry-points`, który każdemu plikowi `SKILL.md` daje parę plików wejściowych (`foundations/invariants.md` na `745a6e5`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — według niej przebudowuje się sześć skilli (To do 1).
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.”
- **WAY-35** — „An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them.” — nie zmienia się; wyznacza, co nie może trafić do pliku obok skilla elementu.
- **WAY-150** (fragment) — „The selection is neither recorded nor compared with every *Scope* of the log, and the search of the whole foundation (WAY-33) and the whole reading of templates, rules and examples keep their domain.” — nie zmienia się.
- **WAY-117** — „The skill of each entry's kind writes its whole proposal under the definition's `Projected foundation changes`, in that kind's subsection with the template's projected heading and one sentence of its meaning, without writing the product's foundation or running the foundation check, and without searching the whole foundation for the entry: the readiness gate searches it once for the whole definition (WAY-118). […]” — nie zmienia się; jej tryb opisują sekcje „Projected mode”, które przebudowa może przenieść.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; `critique` czytają dwie role: autor, który zleca i rozstrzyga, i krytyk.
- **WAY-125** (fragment) — „Each agent reads the `SKILL.md` of its stage's method whole, and a file the method names, one beside that `SKILL.md` included, only when the step or variant that names the file comes, while the orchestrator reads no method it does not conduct.” — nie zmienia się; nie obejmuje skilli elementów.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in […]” — nie zmienia się.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się.

## Settlements to record

Candidates: 7 shown, 0 accepted — 2026-10-28

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 3/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 4 i ustawić linii „seria skilli 4/11” datę dnia domknięcia; do „Otwartych wątków” wchodzi też wynik `skille_po_kolei_dane/shared_carry_cost.py` na zapisach od dnia scalenia, porównany z `ranking_fundament_2026-10-28.txt` (pytanie 4).
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- `find-foundation-entries` (`elements/common/skill/SKILL.md`) — zadanie 7 serii; to zadanie zmienia w nim tylko odsyłacz do fragmentu przeniesionego z `way_of_working.md`, jeśli przeniesienie tego wymaga.
- Szablony elementów (`elements/<element>/template.md`), ich przykłady i `elements/common/rules.md` — ich podział zmieniłby znaczenie WAY-150 i WAY-35 (pytanie 1).
- Uwagi z PR-ów #50 i #51 — nie przechodzą do tego zadania.
- Pozostałe skille the way — zadania 4–11 serii.
