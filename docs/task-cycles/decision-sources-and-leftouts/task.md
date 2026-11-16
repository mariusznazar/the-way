<!-- Frozen copy of the task document. Original: the task's note in the author's backlog ; approved: settlements accepted 2026-11-15 (Status: ready for cycle). Frozen 2026-11-16. -->

---
title: Uzupełnić w decyzjach the way źródła i to, czego nie biorą z przejętych praktyk
status: draft
created: 2026-11-14T21:31
updated: 2026-11-15
tags: [zadanie]
related: "the project note in the author's vault"
---

# Uzupełnić w decyzjach the way źródła i to, czego nie biorą z przejętych praktyk

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Siedem decyzji the way, które przejmują praktykę z zewnątrz, ma w polu *Based on* tylko `TODO — …`: wpis nazywa praktykę, ale nie jej źródło — WAY-138 (adwokat diabła, pre-mortem, szukanie nieznanych niewiadomych), WAY-142 (mapa drogowa z pionowych plasterków), WAY-143 (pionowe plasterki i praca je umożliwiająca), WAY-144, WAY-146, WAY-147 (praktyka mapy drogowej) i WAY-164 (uprząż agenta dla jego pracowników).
- Siedemnaście decyzji mówi, co bierze z zewnętrznej praktyki, ale nie mówi, czego z niej świadomie nie bierze, choć WAY-100 każe to zapisać w *Rejected*: WAY-138, 143, 146, 147, 164 (praktyki jak wyżej), WAY-268, 270, 273, 374 (lekcje kursu 10xDevs), WAY-167, 206, 212 (tabela i audyt Open Mercato), WAY-199 (statusy plików Open Mercato), WAY-233 (lista kontrolna przeglądu Open Mercato), WAY-228 (testy oparte na własnościach), WAY-236 (zalecenia Anthropic) i częściowo WAY-203 (praktyka Google).
- WAY-136 (kiedy zmiana potrzebuje planu i kto go recenzuje) cytuje w *Based on* skill Open Mercato o przeglądzie po każdym kroku, a jej zdanie wiążące daje osobną recenzję tylko kawałkowi na granicy zaufania albo z operacją nieodwracalną; wpis nie nazywa praktyki, nie mówi, czego z niej nie bierze, i nie ma relacji `derives from WAY-100`, więc nie wiadomo, czy przejmuje praktykę, czy cytat jest tylko dowodem.
- WAY-148 (jak etapy cyklu przekazują pracę orkiestratorowi) przyszła z tego samego skilla Open Mercato: cytuje w *Based on* jego szablon zlecenia dla wykonawcy kroku, a jej zdanie wiążące każe zleceniu kawałka nieść jego fragment planu skopiowany słowo w słowo; nie nazywa praktyki, nie ma relacji `derives from WAY-100` i nie stoi na żadnej liście, więc ta sama niewiadoma.
- WAY-199 ma trzy statusy pliku, a jej cytowane źródło dwa, i nie mówi dlaczego; *Rejected* WAY-203 ma limit 10 procent i regułę „tylko poprawność” jako drogi nieprzyjęte, ale nie zaznacza, że pochodzą ze źródła.
- Żaden wpis nie mówi, czy czytelnik repozytorium może otworzyć lekcje kursów, z których biorą WAY-121, 237, 256, 268, 270, 273, 280 i 374.
- Mariusz i agent, który czyta albo zmienia te decyzje, nie sprawdzą, co dokładnie przejęto z danej praktyki ani gdzie jej granica; przy zmianie reguły ktoś może uznać pominiętą część praktyki za przyjętą albo odtworzyć praktykę z pamięci, a wymyślone źródło wygląda tak samo jak prawdziwe.

### To do

1. Dla każdej z siedmiu decyzji z `TODO` w *Based on* agent szuka źródła praktyki w dokumentach, nie w pamięci: w historii gita wpisu i w opisach commitów oraz scalonych próśb, które go wprowadziły albo zmieniły, w zapisach cykli w historii repozytorium the way, w notatkach autora w vaulcie, w którym leży ten dokument (research wzorców jakości, notatki z kursów, notatki o Open Mercato), i w źródłach publicznych, na które te notatki wskazują. Źródłem jest miejsce, z którego the way praktykę naprawdę wziął, znalezione po tym śladzie; dokument, który tylko opisuje praktykę, a do którego ślad nie prowadzi, źródłem nie jest (pytanie 1).
2. Znalezione źródło, które czytelnik repozytorium może otworzyć, stoi w *Based on* w formie WAY-90 — adres, miejsce, fragment słowo w słowo i data odczytu — w miejsce `TODO`; źródło, którego czytelnik nie otworzy, wpis opisuje w *Rationale* (WAY-27). Decyzja, której źródła agent nie znajdzie, zachowuje w *Based on* formę `TODO — <what is missing, with its source>`, a jej opis mówi, gdzie agent szukał i że nic nie znalazł (pytanie 2).
3. Dla każdej decyzji z obu list, której źródło wpis już podaje albo agent znajdzie, agent porównuje źródło z decyzją i dopisuje do *Rejected* to, czego decyzja z praktyki nie bierze, po jednej pozycji na element, w formie, którą mają już WAY-121 i WAY-142 („<element praktyki> — left out of what the step takes from <praktyka>”); powód stoi przy pozycji tylko tam, gdzie podaje go wpis albo źródło.
4. Agent ustala po śladzie, jak w punkcie 1, dla WAY-136 i WAY-148 osobno, czy przejmuje praktykę z cytowanego skilla Open Mercato — WAY-136 przegląd po kroku, WAY-148 zlecenie wykonawcy kroku — czy cytuje ją tylko jako dowód (pytanie 4). Przy przejęciu decyzja nazywa w *Rationale* praktykę i to, co z niej bierze, dopisuje do *Rejected* to, czego nie bierze, jak w punkcie 3, i dostaje w *Relations* `derives from WAY-100`; przy dowodzie wpis się nie zmienia, a prośba o scalenie mówi, na czym agent oparł ocenę.
5. WAY-199 mówi w *Rationale* albo w *Rejected*, czego nie bierze ze statusów Open Mercato (`readable`, `qa-only`) i skąd jej trzeci status, o ile mówi to dokument, który da się wskazać.
6. *Rejected* WAY-203 zaznacza przy limicie 10 procent i przy regule „tylko poprawność”, że to drogi z cytowanej praktyki Google.
7. Każda z decyzji WAY-121, 237, 256, 268, 270, 273, 280 i 374 mówi w *Rationale* jednym zdaniem, że lekcje kursu, z którego bierze, nie są otwarte dla czytelnika repozytorium; żadna nie podaje do nich adresu (pytanie 3).
8. WAY-100 zmienia się tak, jak mówi *Decisions in play*, a jej *Verification*, *Rationale* i *Rejected* zgadzają się ze zmianą; WAY-100 zmienia się w miejscu (WAY-07).
9. Prośba o scalenie wymienia dla każdej decyzji z obu list oraz dla WAY-136 i WAY-148, gdzie agent szukał, co znalazł i w którym miejscu źródła, albo że nie znalazł.

### Acceptance criteria

- Zdania wiążące żadnej z decyzji wymienionych w *Need* się nie zmieniają: zmiana dotyka ich *Based on*, *Rationale* i *Rejected*, a w WAY-136 i WAY-148 także *Relations*.
- Każde źródło dopisane do *Based on* agent cyklu otworzył i przeczytał w tym cyklu, a data odczytu jest dniem tego odczytu.

### Questions to settle

- Co liczy się jako źródło praktyki, które decyzja podaje według WAY-100 („names the source in *Based on*”)?
  - Answer: miejsce, z którego the way naprawdę wziął praktykę, znalezione po śladzie — historia gita, notatka albo research w vaulcie, publiczny oryginał, który ta notatka cytuje; publiczny oryginał stoi w *Based on* z cytatem, a prywatna notatka, którą ślad przeszedł, jest opisana w *Rationale*. Gdzie śladu nie ma, decyzja zostaje bez źródła i bez listy tego, czego nie bierze.
  - Not chosen:
    - dowolny publiczny dokument, który opisuje praktykę tak, jak decyzja ją bierze — wpis wygląda, jakby the way wziął praktykę stamtąd, choć mógł skądinąd i w innym zakresie, a „czego nie bierze” powstaje wobec tekstu, którego nikt nie czytał przy decyzji; to ryzyko z notatki zadania („wymyślone źródło wygląda tak samo jak prawdziwe”)
    - pochodzenie, a gdzie śladu brak, publiczny opis praktyki oznaczony w *Rationale* jako opis — nowy rodzaj źródła, którego żadna reguła nie zna; zadanie rośnie o zmianę WAY-100 i WAY-90
  - Source: Mariusz, 2026-11-14, odpowiedź przekazana przez sesję „doradca-dnia”, którą upoważnił do odpowiadania w swoim imieniu: „pytanie 1 — a. Źródło to miejsce, z którego the way naprawdę wziął praktykę, po śladzie (git, notatka/research w vaulcie, publiczny oryginał, który ta notatka cytuje); gdzie śladu nie ma, decyzja zostaje bez źródła i bez listy „czego nie bierze”. Podstawa: zgodne z „bez zgadywania” Mariusza, nie zmienia żadnej reguły; b to dokładnie ryzyko z notatki, c powiększa zadanie o zmianę WAY-100 i WAY-90.”
- Co stoi w *Based on* decyzji, której źródła agent nie znajdzie?
  - Answer: zostaje `TODO — …` w formie, którą daje WAY-71, a opis przy nim mówi, gdzie agent szukał i że nic nie znalazł; `unknown` z notatki zadania było skrótem piszącego notatkę, nie wymogiem Mariusza, i WAY-71 ma pierwszeństwo.
  - Not chosen:
    - `unknown` jako nowa dozwolona wartość *Based on* — zmiana reguły w czterech–pięciu miejscach (WAY-71, szablon decyzji, wspólne reguły formy, skrypt sprawdzający formę z testem) dla garści wpisów
    - `none` i zdanie w *Rationale*, że źródło jest nieznane — `none` mówi, że decyzja na niczym z zewnątrz nie stoi, a wspólne reguły każą wtedy pisać `TODO` („where a source is silent, the field reads `TODO`”)
  - Source: Mariusz, 2026-11-14, odpowiedź przekazana przez sesję „doradca-dnia”: „pytanie 2 — a. Zostaje „TODO — …” z opisem, gdzie szukano i że nic nie znaleziono; „unknown” w mojej notatce było moim skrótem, nie wymogiem Mariusza — reguła WAY-71 ma pierwszeństwo. Podstawa: ta sama informacja bez zmiany reguły w pięciu miejscach dla garści wpisów.”
- Czy czytelnik repozytorium może otworzyć lekcje kursów, z których biorą WAY-121, 237, 256, 268, 270, 273, 280 i 374, i co wpis mówi o tym?
  - Answer: lekcje nie są publiczne i decyzje nie podają do nich adresu. Każda z tych decyzji mówi w *Rationale*, że kurs nie jest otwarty dla czytelnika repozytorium, a WAY-100 dostaje ten sam wymóg dla każdej decyzji, która bierze praktykę ze źródła, którego czytelnik repozytorium nie otworzy.
  - Not chosen:
    - zdanie tylko w ośmiu wpisach, bez zmiany WAY-100 — następna decyzja z kursu znów tego nie powie, a recenzent znów nie rozstrzygnie, czy źródło jest zamknięte, czy zapomniane
    - nic nie dopisywać, odpowiedź tylko w dokumencie zadania — wpisy zostają tak samo niejasne, a dokument znika po zadaniu
  - Source: Mariusz, 2026-11-14, w rozmowie: „3.1 - lekcje nie są publiczne i nie będziemy do nich linkować 3.2 - a”
- Czy zadanie sprawdza też WAY-148, która przyszła tym samym commitem 8ccbd6e z tego samego skilla Open Mercato co WAY-136, a nie stoi na żadnej liście?
  - Answer: tak — WAY-148 przechodzi to samo sprawdzenie co WAY-136 (*To do* 4).
  - Not chosen:
    - WAY-148 poza zadaniem, odnotowana w *Out of scope* — jeśli przejmuje praktykę, następny recenzent porównujący ją z WAY-100 znajdzie ten sam brak co przegląd fundamentu przy WAY-136 i zadanie trzeba otwierać znowu
    - sprawdzenie wszystkich decyzji, które cytują źródło z internetu bez relacji do WAY-100 i bez przejścia przez prośbę nr 126 (poza WAY-136 i 148: WAY-89, 205, 234, 235, 238, 239, 241) — osiem wpisów więcej do przeczytania, choć przegląd fundamentu czytał je wszystkie i żadnego nie zgłosił
  - Source: Mariusz, 2026-11-15, odpowiedź przekazana przez sesję „doradca-dnia”, którą upoważnił do odpowiadania w swoim imieniu: „1 a — dopisz WAY-148 do tego samego sprawdzenia co WAY-136 (to samo pochodzenie z commita 8ccbd6e, koszt jednego przeczytania).”

## Context

- Sprawa wyszła z prośby o scalenie nr 126 w repozytorium the way (https://github.com/mariusznazar/the-way/pull/126), porządków dziennika decyzji: przepisała decyzje według wzoru z WAY-100 i zostawiła te luki jawne, bo źródła ani brakującej połowy nie wolno dopisywać z pamięci; sekcja „Foundation entries”, punkty 3 i 4, wymienia decyzje.
- Zapis cyklu tej prośby, wersja po poprawce: `git show cfd275c:docs/task-cycles/decision-log-second-round/reports/foundation-report.md`, sekcja „For the human”, punkty 2–4, wymienia braki decyzja po decyzji.
- Ustalenie z 2026-11-14, zapisane w tej notatce przed doprecyzowaniem przez sesję „doradca-dnia” (słowo `unknown` w nim to skrót tej sesji, który pytanie 2 zastępuje): „Mariusz większości źródeł nie pamięta albo nie zna. Źródła szuka agent — w dokumentach, nie w pamięci […]. Każde znalezione źródło podaje z cytatem i miejscem; „czego decyzja nie bierze” wyprowadza z porównania źródła z decyzją. Gdzie źródła nie znajdzie, wpisuje `unknown` zamiast `TODO` — bez zgadywania. Mariusz tylko przegląda wynik w PR-ze.”
- Agent tamtego cyklu szukał słów „roadmap”, „vertical slice”, „devil's advocate” i „harness” tylko w plikach repozytorium the way i nic nie znalazł; vaultu ani historii gita nie przeszukiwał.
- Przy doprecyzowaniu widać kandydatów, nie sprawdzonych jako źródło: katalog wzorców jakości z researchu w vaulcie ma wzorzec „W53. Pre-mortem” z adresem artykułu HBR z 2007 roku; testy WAY-138 weszły do dziennika commitem 53b3827.
- Numery decyzji się nie zmieniają: inne pliki powołują się na nie.
- WAY-136 doszła do zadania z przeglądu fundamentu 2026-11-14 (propozycja P7, bez uwag z próśb): decyzja Mariusza z tego przeglądu każe dopisać ją do zadania i sprawdzić, czy przejmuje praktykę, czy cytat jest tylko dowodem; prośba nr 126 jej nie sprawdzała, bo nie miała relacji do WAY-100.
- Ślad WAY-136 i WAY-148: commit 8ccbd6e (2026-10-23) przepisał WAY-136 i WAY-148 i dopisał WAY-229, „each citing Open Mercato's om-auto-create-pr-loop in Based on”; notatka the author's research note on Limen and Open Mercato opisuje przegląd po kroku w Open Mercato (punkt, który otwiera „Przegląd per krok jest **domyślnie wyłączony**”) i jego bramki zależne od ryzyka (punkt „OM: bramki zależne od ryzyka”, który dwa pytania o granicę zaufania i operację nieodwracalną nazywa własnymi the way, z Open Mercato „częściowo zbieżnymi”).
- Pozycja 3 listy drobnych poprawek brzmienia z tego przeglądu (WAY-121, *Rationale*) idzie zadaniem „the way: dziennik decyzji po przeglądzie fundamentu …” i dotyka tego samego *Rationale* co to zadanie.
- Plik danych przeglądu fundamentu 2026-11-14: the data file of the foundation review of 2026-11-14 in the author's notes, sekcja „Fundament” → „Propozycje”, P7.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-100 — When does a method or practice borrowed from elsewhere bind a product?** (`foundations/decisions.md`), drugi akapit zdań wiążących:
  > A decision that adopts a method or practice from outside names the practice and what it takes from it, in its binding sentences or its *Rationale*; names the source in *Based on*, or, for a source a reader of the repository cannot open, describes in *Rationale* what was seen there (WAY-27); and puts what it leaves out of the practice in *Rejected*. A list of what is taken from one source is no decision: each rule taken stands in the decision that carries it (WAY-19).
  - Zmiana, którą robi zadanie (WAY-30, WAY-314): źródłem, które decyzja podaje, jest miejsce, z którego praktykę wzięto, a nie dokument, który ją tylko opisuje (pytanie 1); decyzja, która bierze ze źródła, którego czytelnik repozytorium nie otworzy, mówi w *Rationale*, że to źródło nie jest dla niego otwarte (pytanie 3). Akapit ma dziś dwa zdania, a limit to trzy.
- **WAY-27 — Where may this repository point for its reasoning?**:
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.
- **WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?**, pierwsze zdanie:
  > A decision's *Based on* quotes every source outside the product that the decision rests on with its address, the place in it, the passage word for word and the date it was read; once the environment facts element has entries, it names instead a fact entry, by its identifier alone, for every citation that, once it stopped being true, would call the decision into question — a finding about agents or models, the behaviour of a tool the process uses.
  - Zadanie stosuje to zdanie tak, jak stoi: źródło, którego zmiana podważyłaby decyzję, staje się faktem środowiska według WAY-90.
- **WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?**, fragment:
  > The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet: […] and in a decision's *Based on*, in the form `TODO — <what is missing, with its source>`; […] a change that leaves one there puts it before the human.
  - Zadanie stosuje ten fragment tak, jak stoi (pytanie 2).
- **WAY-136 — When does a task's change need a plan, and who makes and reviews it?**, fragment zdania wiążącego i *Based on*:
  > of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks;

  > https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/step-review.md § "Cost" — "`per-step` multiplies review cost by the Step count — reserve it for high-risk work where an early defect propagating into later Steps costs more than the extra reviews."; read 2026-10-23
  - Zadanie zmienia ją tylko przy przejęciu praktyki (*To do* 4): *Rationale*, *Rejected* i *Relations*, bez zdań wiążących.
- **WAY-148 — How do task-cycle stages pass their work to the orchestrator?**, fragment zdania wiążącego i *Based on*:
  > it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan;

  > https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-auto-create-pr-loop/references/executor-dispatch.md § "Model tier (best-effort)", the executor prompt template — "Full description: {paste the Step's bullets from PLAN.md Implementation Plan}"; read 2026-10-23
  - Zadanie zmienia ją tylko przy przejęciu praktyki (*To do* 4), tak samo jak WAY-136.
- Decyzje, w których zadanie zmienia *Based on*, *Rationale* albo *Rejected*, bez zmiany ich zdań wiążących: WAY-121, 138, 142, 143, 144, 146, 147, 164, 167, 199, 203, 206, 212, 228, 233, 236, 237, 256, 268, 270, 273, 280 i 374; każdą cykl czyta w całości w `foundations/decisions.md` pod nagłówkiem `### WAY-NN`.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Źródłem, które decyzja przejmująca praktykę podaje, jest miejsce, z którego the way praktykę naprawdę wziął, znalezione po śladzie; dokument, który tylko opisuje praktykę, źródłem nie jest. | sentence of WAY-100 | odpowiedź na pytanie „Co liczy się jako źródło praktyki…” w *Questions to settle*, która trzyma drogi niewybrane | czy WAY-100 zostaje bez zmiany, a następna decyzja przejmująca praktykę podaje publiczny opis praktyki znaleziony po fakcie |
| 2 | Decyzja, która bierze praktykę ze źródła, którego czytelnik repozytorium nie otworzy, mówi w *Rationale*, że to źródło nie jest dla niego otwarte. | sentence of WAY-100 | odpowiedź na pytanie „Czy czytelnik repozytorium może otworzyć lekcje kursów…” w *Questions to settle*, która trzyma drogi niewybrane | czy zdanie o zamkniętym źródle staje tylko w ośmiu wpisach, a następna decyzja z kursu go nie ma |

## Out of scope

- Źródło nowego zdania WAY-29 (karta prywatnej analizy), które raport cyklu prośby nr 126 też wymienia: WAY-29 nie przejmuje praktyki z zewnątrz.
- Decyzje WAY-128–133, 137, 139, 140 i 173: używają źródła jako dowodu, nie przejmują z niego praktyki.
