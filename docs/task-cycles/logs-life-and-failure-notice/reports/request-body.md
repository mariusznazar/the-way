**Status: `blocked`.** Jedna uwaga blokująca została po recenzji poprawki, więc cykl stanął przed krokiem powrotnym i scaleniem z `foundations`. Czeka na Twoją decyzję (sekcja „Co blokuje”).

Krok technologii pyta o logi działającego produktu tylko o to, dokąd trafia zapis i jak agent go czyta. Log, który ginie przy każdym wdrożeniu, przechodzi to pytanie, a człowiek o awarii dowiaduje się od użytkowników. Po tej zmianie krok pyta też, jak długo zapis żyje, także między wdrożeniami, a osobną pozycją listy, skąd człowiek dowiaduje się o awarii. Lista skilla wdrożeniowego dostaje te same dwa punkty, żeby sprawa dochodziła też do produktu z już zatwierdzoną definicją.

- **Zadanie:** niezależne; opis przyjęty 2026-10-31, cytaty na `foundations` `f86fd71`, baza cyklu `foundations` `5d66387` (PR #64 nie dotknął wpisów tego zadania).
- **Przypięcie the way:** nie dotyczy, the way pracuje tu nad sobą.
- **Spec:** napisany, bo zadanie zostawiło otwartą sprawę: co krok robi z listą sprzed zmiany, gdy pozycja logów stoi już jako `held by` albo `projected`. Dwie drogi dawały człowiekowi inne zachowanie, a reguły nie niósł żaden wiersz zadania. Link poniżej, przy rejestrze.
- **Droga:** jeden autor bez planu; jedenaście plików prozy w dwóch częściach, reguły zależą od siebie nawzajem i nic nie wymagało podziału. Nie było odrzuconej próby.

## Co blokuje

### N1. `task_run.md` gains a rule by which a held decision opens at a task with no human's word

- **Place:** `project-level/technology/task_run.md:50-54`, the sentence added right after "An agent never
  opens one.": "A decision silent on part of what a matter of the logs, the interface or the development
  data asks (`running_product.md`) holds nothing, where the note touches the matter: the item stands
  `— open`, with that decision nested under it as `Changes:`."
- **What is wrong:** the condition is that the note touches the matter, not that the human gave the
  word. A note is not always the human's: `task_run.md:20`, "A run that refinement starts for a reserved
  choice takes that choice as its note". The deployment route needs no such sentence, since
  `resolve_gaps.md:65-66` already makes the human's yes "the human's word that the run asks for where a
  logs decision stands", and a note in a request is the human's word already. So what the sentence adds
  beyond the existing exception is exactly the case with no human's word: an agent's run on a reserved
  choice that touches the logs opens a decision of the foundation, and its result changes that decision.
- **Why it matters, against what:**
  - Answer 5 is the human's settlement, and it rejects this. Its question gives "każe agentowi otwierać
    decyzję" as the reason to drop the way, its *Not chosen* counts "trzeba dopisać reguły na otwieranie
    decyzji przez agenta" as a cost, and it says "WAY-267 zostaje bez zmian". The change's own *Rejected*
    in WAY-139 and WAY-270 repeat that cost ("rules are needed on an agent opening a decision").
  - WAY-267 binds "a choice a decision of the foundation holds opens only on the human's word", with the
    violating example "an agent opens a choice a decision holds on its own". The entry is unchanged, and
    the new sentence, placed as a qualification of "An agent never opens one", is an exception that
    lives only in a file beside the skill (WAY-30: "no exception lives only in a task document, plan or
    cycle record", by its reasoning; WAY-25 for a collision with no precedence written).
  - Spec D1, "Who may open what": at a task "the logs reach a run only through a note the human agreed
    to (D6), which is the human's word", and of the rule of `task_run.md` and WAY-267's sentence, "Both
    stay as they are". Spec D7: "Nothing else changes". The spec's *Files* row for `task_run.md` is D7
    alone.
  - WAY-165 does give a way to read the two as compatible, "holds" as "settles", and the human still sees
    the list and accepts the whole document, so the damage is bounded. What it costs is the rule the human
    kept: at a task, opening a decision takes the human's word. `task_run.md:78` also shows the seam:
    only "A choice the human opened says in its *Answer* which decision it changes", so an item opened
    this way has no line telling the run to say it, and the first review's concern is met only by the
    nested line.
- **How this came about:** finding 4 raised that the exception might not fire, because `list.md` says a
  silent decision holds nothing. Its fix line named `list.md` only. The right ending there is that the
  exception does fire, not that the decision stops counting.
- **Evidence:** the passages above; a read of `task_run.md` *Start* and *List* and `resolve_gaps.md:23-31`.
  No test pins the step's text.
- **Fix in one line:** make the sentence keep the human's word: for this rule a decision silent on part of
  such a matter counts as one that holds the choice, so it opens only on the human's word and then stands
  `— open` with the decision nested. The deployment route already gives that word, and a reserved choice
  whose note touches the logs then asks the human.

**Co próbowała poprawka.** Pierwsza recenzja (jej uwaga 4) wskazała, że nowa lista nad decyzją, która milczy o czasie życia zapisu, nie zagnieżdża tej decyzji pod pozycją, a przy uruchomieniu kroku na zadaniu wyjątek może nie zadziałać. Poprawka dodała do `task_run.md` zdanie, którego dotyczy uwaga wyżej.

**Czas, modele, tokeny:** @@STAGES@@ Dwie rundy przeglądu kodu (cała zmiana i poprawka) oraz dwie rundy recenzji specu.

**Czego nie uruchomiono na tym kodzie:** kroku powrotnego i scalenia z `foundations`. Test zachowania agenta idącego za tymi tekstami nie istnieje, więc też nie został uruchomiony.

## Co się zmieniło

- `project-level/definition_template.md`: pytanie o logi obejmuje czas życia zapisu; nowa pozycja o tym, skąd człowiek dowiaduje się o awarii.
- `project-level/technology/failure_notice.md` (nowy): kiedy ta pozycja trafia na listę; `SKILL.md`, `start.md` i `list.md` do niego prowadzą.
- `project-level/technology/running_product.md`: wpis, który nie odpowiada na wszystko, o co pyta sprawa, tej sprawy nie rozstrzyga; pozycja wraca jako `— open` z tym wpisem zagnieżdżonym pod nią, także przy wznowieniu listy sprzed zmiany.
- `project-level/technology/settle.md`, `research.md`, `task_run.md`: zagnieżdżony wpis dochodzi do agenta badającego, a wynik go nadpisuje; „świadomy brak” zawsze wchodzi do porównania pozycji awarii, choć nie ma strony dokumentacji.
- `project-level/task/skill/resolve_gaps.md`: gdy zadanie wdraża produkt, doprecyzowanie cytuje gotową odpowiedź albo pyta człowieka; odmowa zapisana w skillu zamyka pytanie.

Bramka gotowości i skrypty się nie zmieniły. Tekst kroku nie nazywa żadnego narzędzia.

## Sprawdzenia

- `python -B gate/run_tests.py` na `63fa039`: kod wyjścia 0, „615 tests in 8 directories; every directory passed”. Na bazie to samo. Żaden test nie zawiódł.
- `python -B elements/common/foundation_check.py .`: 0. `python -B gate/run_tests.py project-level`: 0. `python -B agent-instructions/skill_entry_points.py`: 0.
- Własne sprawdzenie autora: pozycja logów na milczącym wpisie nie wraca do `— projected` i nie korzysta ze starego raportu. To było czytanie plików, nie uruchomienie.
- Testy nie pilnują tekstu kroku, więc o jego zachowaniu mówią tylko recenzje.
- Interfejsu użytkownika zmiana nie dotyka.

## Co ten request ustala

- **WAY-270 (nowa, wiersze 2 i 3):** Gdy projekt uruchamia produkt poza maszyną, na której powstaje (chyba że definicja albo decyzja fundamentu trzyma go na tej maszynie), i żadna decyzja fundamentu tego nie rozstrzyga, krok technologii stawia na liście, jak człowiek dowiaduje się o awarii, jako osobny wybór poza drogą agenta, z odpowiedzią w postaci narzędzia zbierającego awarie, alertu albo świadomego braku (ten zawsze w porównaniu), a żadna definicja nie musi go mieć, bramka go nie sprawdza i zatwierdzona definicja nie wraca z jego powodu.
- **WAY-165 (zmiana, wiersz 1):** Pytanie o logi obejmuje też to, jak długo zapis żyje, także między wdrożeniami, a wpis (decyzja fundamentu albo decyzja projektowana), który zostawia część tego, o co pyta sprawa, bez odpowiedzi, tej sprawy nie rozstrzyga.
- **WAY-139 (zmiana, wiersz 4):** Lista skilla wdrożeniowego ma siedem punktów, w tym osobno czas życia zapisu logów i skąd człowiek dowiaduje się o awarii; dla tych dwóch doprecyzowanie cytuje odpowiedź z decyzji albo zatwierdzonej definicji, w przeciwnym razie pyta człowieka, czy uruchomić krok technologii, a zapisana odmowa pokrywa punkt.
- **WAY-121 (zmiana, ze specu):** Znaczenie bez zmian, poza wskazaniem, że sprawa awarii ma własny wyjątek (WAY-270).

Testy niezmienników: bez zmian. Powierzchnie (WAY-49): bez zmian. Znaczniki *Violated*: bez zmian.

**Dwa odczytania wierszy zadania, które przyjmujesz przy scaleniu** (rejestr, Q3 i Q4):

- Wiersz 4: gdy decyzja albo zatwierdzona definicja już odpowiada na punkt listy, doprecyzowanie ją cytuje zamiast pytać człowieka.
- Wiersz 3: definicja, która nie mówi, gdzie produkt działa, liczy się jak uruchomienie poza maszyną. Produkt tylko lokalny, którego definicja i fundament tego nie mówią, dostaje jedną pozycję, zamykaną raz świadomym brakiem.

## Pytania

Krok fundamentu nie zgłosił pytań. Jedyna sprawa dla człowieka to uwaga blokująca wyżej.

## Uwagi drobne

Z przeglądu całej zmiany (`whole-review.md`):

1. `project-level/technology/start.md:24-26`: the lookup ends the item `— projected` and does not remove
   the nested line, though spec D1 says "The nested line goes when the item ends `— projected`, here and
   in the lookup of trap 1"; `settle.md` sub-step 7 does remove it. After an interrupted write, a stale
   `Changes:` line reaches the gate. A scratch run shows the readiness check passes it, so the harm is
   a stale line in an approved definition.
2. `foundations/decisions.md:4474-4476`: WAY-165's complying example gives only `— held by`; spec D1 asks
   for both markers. The `— projected` case stands only among the violations.
3. `foundations/decisions.md:4492`: "(WAY-270)" stands on the sentence about an entry that answers part of
   a matter, and WAY-270 says nothing of that. The sentence's rule is WAY-165's own; the citation sends
   a reader to the wrong entry.
4. `project-level/technology/failure_notice.md:15`: "ending `— open`" reads against `list.md`'s step for a
   projected decision of the definition on the same matter, which gives `— projected`. A new list could
   research a choice already projected; `start.md`'s lookup corrects it only at a resume.
5. `project-level/task/skill/resolve_gaps.md:63`: "once and for each item apart" can read as two questions;
   spec D6 and WAY-139's example have one question, which the human may answer item by item.
6. Form: lines the change leaves unwrapped, `research.md:14` (153 characters), `research.md:24`,
   `settle.md:73`, and the violating examples of WAY-139 in `foundations/decisions.md`; the course is
   written `10xDEVS` at `:7955` and `10xDevs` at `:6713` and `:7809`.

Z przeglądu poprawki (`whole-review-2.md`):

1. Unwrapped lines the fix leaves in `foundations/decisions.md`: `:7904` (165 characters), `:7924` (140) and
   `:7948` (187), against the file's width of about 100.

## Uwagi poza zakresem zadania

Żaden recenzent nie oznaczył uwagi jako wykraczającej poza zadanie. To sprawy, które recenzent odłożył jako poza zadaniem (`Declined to judge`):

- A failure item the human strikes from the list comes back at the next resume, since the look adds what
  it finds missing: the three matters behave so already, and the spec's table asks for it; a change of
  that behaviour is outside the task.
- Whether "the matter" should reach a product that is no running service, such as a library: row 3 and
  D4 settle the criterion, and a deliberate absence answers it once.
- WAY-166's complying example recommends the container's output with no word on its life: its subject is
  whether an agent can use an option, and the task names no change there.

Testy poza częściami zadania: żaden nie zawiódł i nie przeszedł dopiero przy ponownym uruchomieniu.

## Rejestr

Rejestr cyklu: @@RECORD@@. Spec: @@SPEC@@. Tabela pytań i wyborów (4 pozycje, w tym Q3 i Q4 powyżej) stoi w rejestrze. Prośba o scalenie z zachowaniem commitów, bo link po SHA działa tylko wtedy.

Działania człowieka poza repozytorium: brak.
