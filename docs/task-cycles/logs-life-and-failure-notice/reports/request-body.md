Krok technologii pyta o logi działającego produktu tylko o to, dokąd trafia zapis i jak agent go czyta. Log, który ginie przy każdym wdrożeniu, przechodzi to pytanie, a człowiek o awarii dowiaduje się od użytkowników. Po tej zmianie krok pyta też, jak długo zapis żyje, także między wdrożeniami, a osobną pozycją listy, skąd człowiek dowiaduje się o awarii. Lista skilla wdrożeniowego dostaje te same dwa punkty, żeby sprawa dochodziła też do produktu z już zatwierdzoną definicją.

- **Zadanie:** niezależne; opis przyjęty 2026-10-31, cytaty na `foundations` `f86fd71`, baza cyklu `foundations` `5d66387` (PR #64 nie dotknął wpisów tego zadania); `foundations` od tamtej pory się nie zmieniło, więc scalenie nic nie wniosło.
- **Przypięcie the way:** nie dotyczy, the way pracuje tu nad sobą.
- **Spec:** napisany, bo zadanie zostawiło otwartą sprawę: co krok robi z listą sprzed zmiany, gdy pozycja logów stoi już jako `held by` albo `projected`. Dwie drogi dawały człowiekowi inne zachowanie, a reguły nie niósł żaden wiersz zadania. Link poniżej, przy rejestrze.
- **Droga:** jeden autor bez planu; jedenaście plików prozy w dwóch częściach, reguły zależą od siebie nawzajem i nic nie wymagało podziału. Nie było odrzuconej próby.

## Przebieg

Request stał chwilę jako `blocked`: po recenzji poprawki została uwaga, że `task_run.md` pozwala agentowi otworzyć decyzję fundamentu bez słowa człowieka. Twoja decyzja: „poprawmy to”. Milcząca decyzja otwiera się przy zadaniu tylko na słowo człowieka, a WAY-267 zostaje bez zmian. Korekta `94d20f3` to wprowadziła. Jej recenzja zwróciła jedną uwagę blokującą: WAY-165 nazywała naruszeniem to, co plik teraz robi. Poprawka `7f69096` ograniczyła to zdanie do definicji projektu i recenzja przeszła: `PASS 7f69096`.

**Skutek dla zadania, do przyjęcia przy scaleniu.** Context zadania mówi bez ograniczenia, że decyzja o logach milcząca o czasie życia zapisu nie rozstrzyga sprawy logów. Teraz obowiązuje to przy definicji projektu; przy zadaniu taka decyzja trzyma wybór, dopóki człowiek jej nie otworzy.

Krok powrotny niczego nie zmienił. Czas, modele, tokeny: @@STAGES@@

## Co się zmieniło

- `project-level/definition_template.md`: pytanie o logi obejmuje czas życia zapisu; nowa pozycja o tym, skąd człowiek dowiaduje się o awarii.
- `project-level/technology/failure_notice.md` (nowy): kiedy ta pozycja trafia na listę; `SKILL.md`, `start.md` i `list.md` do niego prowadzą.
- `project-level/technology/running_product.md`: przy definicji wpis, który nie odpowiada na wszystko, o co pyta sprawa, tej sprawy nie rozstrzyga; pozycja wraca jako `— open` z tym wpisem zagnieżdżonym pod nią, także przy wznowieniu listy sprzed zmiany.
- `project-level/technology/settle.md`, `research.md`: zagnieżdżony wpis dochodzi do agenta badającego, a wynik go nadpisuje; „świadomy brak” zawsze wchodzi do porównania pozycji awarii, choć nie ma strony dokumentacji.
- `project-level/technology/task_run.md`: przy zadaniu pozycja awarii wchodzi na listę tylko przez dopisek, a milcząca decyzja otwiera się tylko na słowo człowieka. Dopisek wyprowadzony przez doprecyzowanie z wyboru zastrzeżonego nie jest tym słowem.
- `project-level/task/skill/resolve_gaps.md`: gdy zadanie wdraża produkt, doprecyzowanie cytuje gotową odpowiedź albo pyta człowieka; odmowa zapisana w skillu zamyka pytanie.

Bramka gotowości i skrypty się nie zmieniły. Tekst kroku nie nazywa żadnego narzędzia.

## Sprawdzenia

- `python -B gate/run_tests.py` na `7f69096`: kod wyjścia 0, „615 tests in 8 directories; every directory passed”. Na bazie to samo. Żaden test nie zawiódł.
- `python -B elements/common/foundation_check.py .`: 0. `python -B gate/run_tests.py project-level`: 0. `python -B agent-instructions/skill_entry_points.py`: 0.
- Własne sprawdzenie autora: pozycja logów na milczącym wpisie nie wraca do `— projected` i nie korzysta ze starego raportu, a przy zadaniu działa w trzech przypadkach (dopisek człowieka, dopisek z doprecyzowania, zgoda przy zadaniu wdrożeniowym). To było czytanie plików, nie uruchomienie.
- Testy nie pilnują tekstu kroku, więc o jego zachowaniu mówią tylko recenzje. Zachowania agenta idącego za tymi tekstami nic nie sprawdza.
- Interfejsu użytkownika zmiana nie dotyka.

## Co ten request ustala

- **WAY-270 (nowa, wiersze 2 i 3):** Gdy projekt uruchamia produkt poza maszyną, na której powstaje (chyba że definicja albo decyzja fundamentu trzyma go na tej maszynie), i żadna decyzja fundamentu tego nie rozstrzyga, krok technologii stawia na liście, jak człowiek dowiaduje się o awarii, jako osobny wybór poza drogą agenta, z odpowiedzią w postaci narzędzia zbierającego awarie, alertu albo świadomego braku (ten zawsze w porównaniu), a żadna definicja nie musi go mieć, bramka go nie sprawdza i zatwierdzona definicja nie wraca z jego powodu.
- **WAY-165 (zmiana, wiersz 1):** Pytanie o logi obejmuje też to, jak długo zapis żyje, także między wdrożeniami; wpis, który zostawia część tego, o co pyta sprawa, bez odpowiedzi, nie rozstrzyga jej przy definicji projektu, a w przebiegu przy zadaniu (WAY-267) trzyma wybór jak każda decyzja, więc otwiera się tylko na słowo człowieka.
- **WAY-139 (zmiana, wiersz 4):** Lista skilla wdrożeniowego ma siedem punktów, w tym osobno czas życia zapisu logów i skąd człowiek dowiaduje się o awarii; dla tych dwóch doprecyzowanie cytuje odpowiedź z decyzji albo zatwierdzonej definicji, w przeciwnym razie pyta człowieka, czy uruchomić krok technologii, a zapisana odmowa pokrywa punkt.
- **WAY-121 (zmiana, ze specu):** Znaczenie bez zmian, poza wskazaniem, że sprawa awarii ma własny wyjątek (WAY-270).

Testy niezmienników: bez zmian. Powierzchnie (WAY-49): bez zmian. Znaczniki *Violated*: bez zmian.

**Dwa odczytania wierszy zadania, które przyjmujesz przy scaleniu** (rejestr, Q3 i Q4):

- Wiersz 4: gdy decyzja albo zatwierdzona definicja już odpowiada na punkt listy, doprecyzowanie ją cytuje zamiast pytać człowieka.
- Wiersz 3: definicja, która nie mówi, gdzie produkt działa, liczy się jak uruchomienie poza maszyną. Produkt tylko lokalny, którego definicja i fundament tego nie mówią, dostaje jedną pozycję, zamykaną raz świadomym brakiem.

## Pytania

Brak.

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

Z przeglądu korekty (`correction-review.md`):

1. `project-level/technology/task_run.md:55-57` and `list.md:31`: a human who is to give the word is not told
   there is anything to give it on. For a note refinement derived, the list shows `— held by: <X>`, and
   `list.md` asks for one sentence on why the project needs the item; nothing has the run say what `<X>` leaves
   unsaid, as `start.md` has a definition say. The handoff's "the list shows the human the silent decision" and
   the correction report's "the human sees the decision silent" hold only of the marker, which reads as settled.
   The default is the safe one, nothing opens and the deployment check still asks at a task that deploys, so I
   grade it Minor. The same case meets `reserved_choices.md`, where a choice no decision settles is reserved: with
   a silent decision, the run can close with the item held while WAY-165 says the choice is unsettled, and C1's
   fix does not remove that. One clause, saying what the decision leaves unsaid when the list is shown, closes both.
2. `project-level/technology/task_run.md:53-54`: "whatever `list.md` says of the matter it settles" calls the
   matter one the silent decision settles, the reverse of `list.md`'s sentence. "whatever `list.md` says" reads
   clean.

Z przeglądu poprawki korekty (`correction-review-2.md`):

1. `foundations/decisions.md:4458-4462`: the entry of the clause includes "a projected decision of a definition", so
   "it holds the choice like any decision, which opens only on the human's word" also reads on a projected decision,
   which WAY-267 (`:7718`) and `task_run.md:59` say no run reopens at all, whatever the human's word. The two do not
   collide: "opens only on" states a condition and grants nothing, and WAY-267 is the stricter and explicit one, so an
   agent following either reaches spec D6's second reading. "Like any decision" is the loose part. Writing "a decision
   of the foundation" in the second half of the sentence would end it.
2. Form: lines the fix leaves unwrapped, `foundations/decisions.md:4484` (131 characters) and `:4499` (105).

## Uwagi poza zakresem zadania

Żaden recenzent nie oznaczył uwagi jako wykraczającej poza zadanie. To sprawy, które recenzenci odłożyli jako poza zadaniem (`Declined to judge`):

- A failure item the human strikes from the list comes back at the next resume, since the look adds what
  it finds missing: the three matters behave so already, and the spec's table asks for it; a change of
  that behaviour is outside the task.
- Whether "the matter" should reach a product that is no running service, such as a library: row 3 and
  D4 settle the criterion, and a deliberate absence answers it once.
- WAY-166's complying example recommends the container's output with no word on its life: its subject is
  whether an agent can use an option, and the task names no change there.

- `list.md`'s line break after "A decision of the foundation" keeps a short line the change left: form, already
  named in the first review's Minor 6.

Testy poza częściami zadania: żaden nie zawiódł i nie przeszedł dopiero przy ponownym uruchomieniu.

## Rejestr

Rejestr cyklu: @@RECORD@@. Spec: @@SPEC@@. Tabela pytań i wyborów (4 pozycje, w tym Q3 i Q4 powyżej) stoi w rejestrze. Prośba o scalenie z zachowaniem commitów, bo link po SHA działa tylko wtedy.

Działania człowieka poza repozytorium: brak.
