---
title: "the way: siedem poprawek instrukcji cyklu z uwag po ostatnich cyklach"
status: draft
created: 2026-11-19T08:11
updated: 2026-11-19
tags: [zadanie]
related: "the note of the project in the author's notes"
---

# the way: siedem poprawek instrukcji cyklu z uwag po ostatnich cyklach

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Agenci, którzy prowadzą zmiany w the-way i loop2, siedem razy trafili na miejsce, w którym instrukcja cyklu milczy albo przeczy sama sobie, i za każdym razem rozstrzygnęli po swojemu.
- Wypchnęli zrzuty ekranu do publicznego repozytorium, choć zlecenie mówiło „nie wypychaj”.
- Prowadzący sam dołożył przeglądy części dużej zmiany, bo jeden recenzent nie porównałby kilkuset wpisów z ich źródłami.
- Prowadzący zapisał za agenta raport, którego agent odmówił zapisać.
- Prowadzący zignorował skrypt, który każdy kawałek pracy zmieniający jedną decyzję ogłaszał za dużym.
- Przy przenoszeniu decyzji z notatek jeden agent pominął odrzucone warianty, a inny zostawił je bez powodu.
- Agent oddał „jeszcze czekam na testy” zamiast wyniku.
- Agenci kasowali katalogi poleceniem ze zmienną w ścieżce i odbijali się od blokady, która chroni przed skasowaniem katalogu bieżącego.
- Odczuwają to agenci cyklu, którzy rozstrzygają za każdym razem od nowa, i Mariusz: w przeglądzie wraca ta sama uwaga, a raz coś trafiło do publicznego repozytorium wbrew zleceniu.
- Bez zmiany cykl działa, dopóki prowadzący trafnie zgadnie; gdy zgadnie źle, zrzuty pójdą do sieci albo nie zostaną pokazane wcale, błędne powody decyzji przejdą jednym przeglądem, naprawdę za duży kawałek zginie wśród fałszywych alarmów, a cykl ruszy dalej na niesprawdzonej pracy.

### To do

1. **Zrzuty ekranu poza repozytorium produktu (AIR-666).** W `task-cycle/skill/SKILL.md`, w akapicie, który otwiera „The cycle writes only in the task's worktree” (ok. linii 79–83), na liście wyjątków po „the account of the request named below” dopisać: „, the screenshot shown to the human, which goes to the place the product's foundation settles for screenshots ("Working copies" below)”.
2. **Przeglądy grup kawałków przy dużej zmianie (AIR-667).** W `task-cycle/skill/SKILL.md`, w podpunkcie 5 kroku przeglądu kawałka, po zdaniu kończącym się „…and the review of the whole change judges it (WAY-136).” (ok. linii 498) dopisać: „Where the slices with no review of their own are more than one reviewer of the whole change can compare with their sources — as in a change that rewrites many entries of the foundation from many notes — the lead may dispatch a fresh reviewer with `review-change` on groups of them in the plan's order, as for a slice with a review of its own, and records the grouping and its reason.”
3. **Agent odmawia zapisu raportu mimo poprawnej nazwy pliku (AIR-668).** W `task-cycle/skill/SKILL.md`, po zdaniu kończącym się „…answering that subagents should return findings as text.” (ok. linii 211) dopisać: „The handoff therefore says that the report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), the case that note leaves open. Where an agent refuses the write all the same, it returns its report whole as its answer; save it unchanged at the report path and record the refusal, with the agent's model, in the events table — never in the report, whose first line stays the agent's.”
4. **Miara kawałka liczy cały dziennik decyzji (AIR-669).**
   - (a) `task-cycle/slice_size.py`: docstring, w akapicie, który otwiera „A slice reads every file of *Read*” (ok. linii 19–20), i kod, z testem na plan, którego kawałek zmienia duży dziennik decyzji: „A file of *Change* that *Read* names by ranges counts the lines those ranges name; any other file counts whole where either field names it whole, otherwise the lines its ranges name.”
   - (b) `task-cycle/plan/SKILL.md`, koniec punktu o wpisach fundamentu w *Read*, który kończy się „…a new entry gets its identifier only when written;” (ok. linii 154): „An entry the slice changes, and the section of the log a new entry of the slice goes into, is named in *Read* by its range as well, so that its size is measured.”
   - (c) `task-cycle/change/SKILL.md`, punkt listy lektury, który brzmi „Every file you change, whole, before you change it.” (ok. linii 37), zamienić na: „Every file you change, whole, before you change it — of a file of the foundation, the entries you change and the section a new entry goes into, by the ranges your dispatch names.”
5. **Odrzucone warianty, których jedynym kosztem jest proces (AIR-670).** W `elements/decisions/template.md`, w punkcie, który otwiera „The *Rejected* of a decision written from a row” (ok. linii 90), „…each with the cost or the reason kept beside it;” zamienić na „…each with the cost or the reason kept beside it — or, where the source keeps none or keeps only a cost of the process (a gate to reopen, a step to repeat), with `no cost to the product known`; a way that is itself a way of the process rather than of the product, such as how or when an answer is recorded, is the one way kept by the source that stays out;”. To samo zdanie wiążące wchodzi do WAY-134 przez skill zapisu decyzji (zob. *Decisions in play*).
6. **Odpowiedź „czekam na własne testy” zamiast wyniku (AIR-671).** W `task-cycle/change/SKILL.md` (ok. linii 119–121) i w `task-cycle/review/SKILL.md` (ok. linii 113–115), w punkcie, który otwiera „A command that may run longer than your harness keeps its prompt cache”, „…reading its output between them (WAY-255).” zamienić na „…reading its output between them, and you end your turn only after it has ended and you have read its result (WAY-255).”
7. **Kasowanie kopii poleceniem ze zmienną w ścieżce (AIR-673).**
   - (a) `task-cycle/skill/SKILL.md`, sekcja „Working copies”, na końcu akapitu, w którym stoi „…it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` —” (ok. linii 357–361), nowe zdanie: „It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.”
   - (b) Ten sam plik, krok kopii zapisu cyklu (ok. linii 823–824): „2. Copy the whole record directory to `docs/task-cycles/<task-slug>/` on the task branch…” zamienić na „2. Remove an earlier copy, by its path written out in full, then copy the whole record directory to `docs/task-cycles/<task-slug>/` on the task branch…”.

### Questions to settle

- Czy punkty 1–7 wchodzą w brzmieniu z „To do”?
  - Answer: tak, w tym brzmieniu; wariantów odrzuconych nie przywracać.
  - Not chosen:
    - punkt 1: zdanie wiążące w WAY-316 i zdanie o zleceniach zabraniających pushu — oba przypadki są sprzed commitu 6727b67a z 15.11, a w loop2 decyzja D-419 rozstrzyga, kto wypycha zrzuty; waga obniżona z wysokiej do średniej
    - punkt 2: miara oparta na `slice_size.py` (wariant ze sprawy) — przyjęto osąd prowadzącego z zapisanym powodem
    - punkt 4: gałąź „plik fundamentu bez zakresu liczy zero linii” ze sprawy — odrzucona przy przyjęciu sprawy
    - punkt 6: zdanie po stronie prowadzącego, o odpowiedzi bez statusu — poprawka idzie u źródła, w instrukcji agenta
    - punkt 7: skrypt `task-cycle/record_copy.py` robiący kopię zapisu (propozycja nocnego skanu) — usuwa tylko blokady kroku kopii, a większość bierze się ze sprzątania kopii roboczych; kosztowałby osobny cykl
  - Source: Mariusz, 2026-11-19, przyjęcie spraw AIR-666…AIR-671 i AIR-673 w dziennym przeglądzie ai-review (zeszyt `Notes/Areas/(A) Claude code/ai_review_ledger.md`)
- Punkt 2 a WAY-136: czy decyzja dostaje zdanie o przeglądach grup kawałków?
  - Answer: tak — WAY-136 dostaje zdanie, że gdy kawałków bez własnego przeglądu jest więcej, niż jeden recenzent całości porówna ze źródłami, prowadzący może zlecić przeglądy ich grup i zapisuje podział z powodem; kryterium zostaje osądem prowadzącego, nie miarą.
  - Not chosen:
    - tylko skill, decyzja bez zmian — skill przeczy zdaniu WAY-136 „only one that touches a trust boundary or holds an operation that cannot be undone … gets a review of its own”; pierwszy cykl z przeglądami grup dostanie uwagę recenzenta albo pytanie
    - kryterium na mierze `slice_size.py` (suma szacowanych tokenów kawałków grupy w progu jednego kawałka) — Mariusz odrzucił ten wariant przy przyjęciu sprawy; miara jest przybliżona w dwie strony: pliki czytane przez kilka kawałków liczą się kilka razy, diff, który czyta recenzent, nie liczy się wcale, a kawałek „unchecked” nie ma rozmiaru
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19: „1 b — osąd prowadzącego z zapisanym powodem, WAY-136 dostaje zdanie z tym osądem. Twój rachunek przybliżeń miary (podwójne liczenie wspólnych plików, brak diffu, „unchecked” bez rozmiaru) to dobry powód do zapisania obok.”
- Punkt 1 a WAY-140: czy decyzja dostaje wyjątek na zrzut ekranu pokazany człowiekowi?
  - Answer: nie — zmienia się tylko lista wyjątków w skillu, jak przyjął Mariusz; WAY-140 zostaje bez zmian.
  - Not chosen:
    - wąski wyjątek w WAY-140 (tylko zrzut, tylko pokazany człowiekowi, tylko w miejscu, które wskazuje fundament produktu) — przywraca w innej decyzji znaczenie zdania w WAY-316, które Mariusz odrzucił przy przyjęciu sprawy
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19: „2 b — tylko skill, jak przyjął Mariusz. Zderzenie WAY-140 z WAY-316, które zostaje, pokaż Mariuszowi jednym zdaniem przy akceptacji dokumentu”
- Punkt 6 a WAY-255: czy decyzja dostaje zdanie o końcu tury dopiero po wyniku?
  - Answer: tak — reguła końca tury wchodzi do WAY-255, a oba skille (wykonawcy i recenzenta) cytują decyzję.
  - Not chosen:
    - tylko oba skille, odwołanie „(WAY-255)” zostaje — odwołanie twierdzi, że decyzja mówi coś, czego nie mówi, a recenzent może to zgłosić
    - tylko oba skille, odwołanie przesunięte na samą część o czekaniu — reguła żyje w dwóch skillach bez wspólnej decyzji i może się rozjechać
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19: „3 a — reguła końca tury w WAY-255, oba skille cytują decyzję.”
- Punkt 4: czy domknąć lukę kawałka, który tylko dopisuje nową decyzję?
  - Answer: tak, zdaniem w skillu planisty (punkt 4(b)): kawałek podaje w *Read* zakres sekcji dziennika, do której dopisuje wpis; skrypt po zmianie 4(a) liczy wtedy tę sekcję, nie cały dziennik.
  - Not chosen:
    - zostawić lukę świadomie, w „Out of scope” — kawałki dopisujące decyzje dalej wychodzą „za duże”, więc prowadzący dalej ignoruje miarę przy części kawałków
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19: „4 a — brzmienie (b) jak proponujesz; 5% dziennika przy dopisaniu decyzji to akceptowalny zapas.”
- Punkt 4: czy wykonawca kawałka czyta zmieniany plik fundamentu w całości, skoro miara po 4(a) liczy tylko zakresy?
  - Answer: nie — skill wykonawcy dostaje punkt 4(c): z pliku fundamentu wykonawca czyta zmieniane wpisy i sekcję, do której idzie nowy wpis, po zakresach ze zlecenia; miara i lektura liczą to samo, a skill przestaje przeczyć swojemu „never a whole file of the foundation”.
  - Not chosen:
    - zostawić „Every file you change, whole” — miara po poprawce zaniża to, co instrukcja każe czytać (dziennik decyzji 892 KB, ok. 357 tys. tokenów przy progu 150 tys.), a sprzeczność w skillu zostaje
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19: „a — dopisz ósmy punkt w tym brzmieniu. (…) domyka 4(a) (bez niego miara i lektura liczą co innego) i usuwa sprzeczność skilla z jego własnym „never a whole file of the foundation”.”

## Context

- Źródłem punktów są sprawy AIR-666…AIR-671 i AIR-673 z dziennego przeglądu ai-review; zeszyt `Notes/Areas/(A) Claude code/ai_review_ledger.md`, po 14 dniach archiwum `ai_review_ledger_archive.md`.
- Miejsca zmian sprawdzone 2026-11-19 na `foundations` @ d69fb20b; numery linii są tylko podpowiedzią obok cytatu.
- Punkt 2: przy zadaniu loop2 przepisującym ok. 300 decyzji z ok. 60 notatek prowadzący dołożył sześć przeglądów grup; każdy dał `FAIL`, razem 21 ważnych uwag.
- Punkt 3: wbudowana notka subagenta Claude Code zakazuje plików raportów, z wyjątkiem plików będących wejściem innego narzędzia — sprawdzone w zapisie podagenta the-way; po zmianie nazw raportów na `<etap>-report.md` wykonawca na Haiku i tak odmówił zapisu.
- Punkt 4: dziennik decyzji loop2 i the-way ma ok. 0,8 MB, więc każdy kawałek zmieniający jedną decyzję wychodzi „za duży” (w loop2 31 kawałków).
- Punkt 5: agenci rozstrzygają raz tak, raz inaczej, gdy jedynym kosztem wariantu jest koszt procesu, gdy wariant jest sposobem zapisania odpowiedzi albo gdy źródło nie podaje kosztu wcale (3 uwagi z 2 cykli loop2).
- Punkt 6: w jednym cyklu the-way trzy razy (Haiku i Sonnet).
- Punkt 7: ok. 170 blokad w 102 sesjach od 14.10, zmierzone 2026-11-19 w rozmowach the-way i loop2; krok kopii zapisu to 10–25% z nich, reszta to sprzątanie kopii roboczych przez podagentów; szkody nie zaobserwowano, koszt to powtórzone wywołania, ryzyko — kopia zapisu wrzucona jako podkatalog starej.
- Po punkcie 1 WAY-140 i WAY-316 dalej się zderzają: WAY-140 mówi, że efekt poza repozytorium robi tylko człowiek, a WAY-316 każe położyć zrzut w miejscu poza repozytorium i o WAY-140 milczy; skill dostaje wyjątek, decyzje nie, zgodnie z odrzuceniem zdania w WAY-316 przy przyjęciu sprawy.
- `Defect introduced by: none`: sprzeczność punktu 1 powstała, gdy request #91 (WAY-316) przeniósł do skilli miejsce na zrzuty poza repozytorium, a lista wyjątków skilla szła za WAY-140; to zderzenie dwóch decyzji, którego tamto zadanie nie przewidziało, nie defekt wobec tego, czego wymagało; pozostałe punkty to luki i nowe potrzeby.
- Pełny zapis sesji, w której powstała notatka (wygasa ~2027-02-17, 2 MB): `a file outside the repository (the record of the session in which the note arose)`; czytać przez `python "the author's script that reads a session record (outside the repository)" --session d7ff6502-c09e-4188-9abe-628947361c48 --format text --out <katalog roboczy>/zapis_sesji.txt`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-136 — When does a task's change need a plan, and who makes and reviews it?** — zmieniana (punkt 2): „of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own”. Zmiana: zdanie, że gdy kawałków bez własnego przeglądu jest więcej, niż jeden recenzent całości porówna ze źródłami, prowadzący może z własnego osądu zlecić przeglądy ich grup w kolejności planu i zapisuje podział z powodem; *Rejected* tej decyzji („a review of every slice — … while the review of the whole change still reads every slice”) cykl uzgadnia z tym zdaniem.
- **WAY-255 — How does an agent of a task's cycle wait for a command that runs long?** — zmieniana (punkt 6): „An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps its prompt cache … by running it in the background and reading its output between waits each shorter than that lifetime, never in one wait past it”. Zmiana: zdanie, że agent kończy turę dopiero, gdy polecenie się skończyło i przeczytał jego wynik.
- **WAY-134 — How does a task carry what its refinement settles for the foundation?** — zmieniana (punkt 5): „gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`”. Zmiana: to samo zdanie wiążące co w `elements/decisions/template.md` z punktu 5 — wariant bez kosztu albo tylko z kosztem procesu dostaje `no cost to the product known`, a wariant będący sposobem procesu (jak albo kiedy zapisać odpowiedź) do *Rejected* nie wchodzi.
- **WAY-140 — How does a task change something outside the product's repository?** — bez zmian: „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human”, z wyjątkami: zapis requestu i stanu zadania w backlogu oraz usuwanie katalogów roboczych (WAY-375). Lista wyjątków w skillu, do której punkt 1 dopisuje zrzut, idzie za tą decyzją.
- **WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?** — bez zmian: „the screenshots that its author or reviewer shows the human are embedded as images in the description of the request, from a place that the foundation of the product settles outside the product's repository; the-way names no place.” Pierwszeństwo ustala tylko nad WAY-373; o WAY-140 milczy.
- **WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?** — bez zmian (punkt 7): „Before it returns, the agent removes its copy, keeps in the cycle's reports what its report needs and states in the report where the copy stood and that it was removed”.
- **WAY-148 — How do task-cycle stages pass their work to the orchestrator?** — bez zmian (punkt 3): „Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory” oraz „a missing or incomplete report is repaired before dependent work proceeds”.

## Settlements to record

Candidates: 3 shown, 3 accepted — 2026-11-19

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy kawałków bez własnego przeglądu jest więcej, niż jeden recenzent całości porówna ze źródłami, prowadzący może z własnego osądu, nie z miary, zlecić przeglądy ich grup i zapisuje podział z powodem. | sentence of WAY-136 | pytanie „Punkt 2 a WAY-136” (wybór doradcy dnia w imieniu Mariusza; odrzucone warianty pod pytaniem) | zmieni tylko skill i zostawi WAY-136 w sprzeczności z nim albo wpisze do decyzji miarę z `slice_size.py` |
| 2 | Agent, który puścił długie polecenie w tle, kończy turę dopiero, gdy polecenie się skończyło i przeczytał jego wynik. | sentence of WAY-255 | pytanie „Punkt 6 a WAY-255” (wybór doradcy dnia w imieniu Mariusza; odrzucone warianty pod pytaniem) | zostawi w obu skillach odwołanie do WAY-255, które twierdzi więcej, niż decyzja mówi |
| 3 | Decyzja pisana z wiersza dostaje przy wariancie, dla którego źródło nie podaje kosztu albo podaje tylko koszt procesu, `no cost to the product known`, a wariant będący sposobem procesu, np. jak albo kiedy zapisać odpowiedź, do *Rejected* nie wchodzi. | sentence of WAY-134 | punkt 5 „To do” i pytanie „Czy punkty 1–7 wchodzą w brzmieniu z „To do”?” (przyjęte przez Mariusza) | zmieni tylko szablon decyzji, a WAY-134 dalej każe dawać tylko `none considered` albo `unknown` |

## Out of scope

none
