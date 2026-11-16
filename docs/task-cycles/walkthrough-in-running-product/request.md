**State: ready** — nothing waits for your answer; the rest you accept by merging.

## What you will see

An agent that changes something a user sees in the running product — a screen, an answer of an API, a command in a terminal, data the product shows — now has one more step in its own work. After it writes the code and before the review, it prepares and runs a walk through the running product of what the tests do not cover: it draws the cases from the requirements of the task, not from the code alone, runs them one by one, gives a verdict for each, and says what it did not check and why. A case that fell wrong is corrected before the review, with a test at the lowest level that catches the error. An error outside the task that the walk finds is reported, not corrected, and reaches you in the request. The method is a new file next to the author's skill, read only when the change alters something a user sees; the author of a change made without a plan and the agent of each part of a change made from a plan read it, the agent that fixes a review's findings does not. The review reads the author's report of the walk and checks that the judgment "this change alters / does not alter what a user sees" holds and that every case left unchecked has a reason.

What the request shows you changes in two places. A case the author did not check stands among the skipped steps with its reason and, where you can check it by hand, with the steps; where the product has settled no way for an agent to reach its running product, the walk is "not performed" for that reason, the cycle does not stop, and a screenshot left unchecked for the same reason stands in the same item, not two. An error outside the task found at the walk stands under "Fix or let through" with the one question whether to make a task of it, whatever the cycle judges about whether anyone will feel it.

The same change settles three matters for the process around it. The answer to a matter of an agent's way to the running product — its logs, its interface, its development data, the place of its screenshots — is a decision of the product, even though it tells an agent how to work; a skill of the product may hold the steps of operation and refers to that decision. The word for that way now covers also the means by which the agent shows you what it saw. And the step that settles the technology of a product now says, for each option of the interface, whether two task cycles in separate working directories can check the running product at the same time without sharing a browser; an option that cannot stays in the comparison with that lack.

### Underneath

The method is taken from the testing practice of a team's skill and from two courses, which a reader of this repository cannot open, so a decision of the log names what is taken, where it applies and why, and the method file holds the steps. The change is Markdown only: one new method file, pointers in the skills of the author and the reviewer, the request template, the template and the log of decisions, the glossary and the technology step.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The cycle made three choices that the task and the foundation leave open. First, the five settled answers about the walk stand as three decisions in the log — who walks and for which changes; who approves the cases; what happens to a case that fell wrong and to an error outside the task — not as one, since each can change alone; the adoption of the practices from the team's skill and the courses stands in the first of them. Second, the new method file is named by the cycle, as the task left the name open. Third, where the task's references did not match the files, the cycle followed the files: the task cites a decision about effects outside the repository for "no pause in the middle of the cycle", and the new decision cites the one that makes the request your first point of review instead; the paragraph of the request template that the task names for the rule on textual traces does not exist, so that rule stayed where it is, in the top part, with one added clause. Another answer would change what the foundation binds, and so how the next change reads these rules.
2. Three decisions of the log are new, written by the cycle from the task's settlements, each with a pair of examples (a "complies" and a "violates") that the task does not give, which agents will compare later changes with; the pairs stand word for word in the lower part. In plain words, each says: (a) the author of a change, or the agent of a part of a planned change, walks through the running product what the tests do not cover, after the code and before the review, for every change of what a user sees; where no way to the product is settled, the walk is "not performed" with that reason and the cycle goes on; after a later audit finds an error the author let through, the walk moves to a stage of its own; (b) no one approves the cases of the walk before it is made and the cycle does not stop for them; the task's refinement writes no list of inputs to try; (c) a case that fell wrong is corrected before the review with a test, and an error outside the task is reported and goes to you under "Fix or let through" with the question whether to make a task of it. Two older decisions gained one added example each in their pairs: the one on where the technology a project needs is settled (a product's skill holds the steps and refers to the decision; a product that keeps the way only in a skill breaks the rule) and the one on two cycles checking at once (the technology step says it for each option). Their meaning is the task's.
3. A new decision overrides an older one in one area, and the cycle recorded it. The older decision says that the cycle puts before you only the unfixed findings it judges you or a user will feel. The new decision on a case that fell wrong says that each error outside the task that the walk finds goes to you, whatever that judgment says, so that none can drop out of the description; the new one is recorded as narrowing the older one. The passages of what you accepted that give the outcome: the task's To do 5 says that an error outside the task found at the walk reaches the section for your decisions "as a matter to decide (make a task of it or let it through)", and the settlement row 5 says that the author reports an error outside the task "to the request as a matter for the human".

## Cost

About 52 minutes of working time, 19.5 of them waiting for tools, and 64.9 million tokens in all, most of them reading from the cache: 48.1 million on the model of the author and the orchestrator (sonnet) and 16.8 million on the reviewers' model (opus, the strongest the session allows). The review of the whole change failed once (six blocking and six Minor findings), was fixed once and passed; the review of the return step failed once (one blocking finding), was fixed once and passed; no round was left over. The final gate is the CI run on the last head, below. The table of stages is in the committed record: `docs/task-cycles/walkthrough-in-running-product/stages.md` at commit `RECORD_SHA`.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing in this request waits for a review of the foundation.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowy** — nic nie czeka na Twoją odpowiedź, resztę akceptujesz przez scalenie.

## Co zobaczysz

Agent, który zmienia coś, co użytkownik widzi w działającym produkcie — ekran, odpowiedź API, polecenie w terminalu, dane, które produkt pokazuje — ma teraz jeden krok więcej w swojej pracy. Po napisaniu kodu, a przed recenzją, przygotowuje i przeprowadza przejście przez działający produkt po tym, czego nie obejmują testy: układa przypadki z wymagań zadania, nie tylko z kodu, wykonuje je po kolei, wydaje werdykt dla każdego i mówi, czego nie sprawdził i dlaczego. Przypadek, który wypadł źle, poprawia przed recenzją, z testem na najniższym poziomie, który ten błąd łapie. Błąd poza zadaniem, który znajdzie przy przejściu, zgłasza zamiast poprawiać, i trafia on do Ciebie w PR-ze. Metoda to nowy plik obok skilla autora, czytany tylko wtedy, gdy zmiana zmienia coś, co widzi użytkownik; czytają go autor zmiany robionej bez planu i agent każdej części zmiany robionej według planu, a agent poprawiający uwagi recenzji go nie czyta. Recenzja czyta raport autora z przejścia i sprawdza, czy ocena „ta zmiana zmienia / nie zmienia tego, co widzi użytkownik” się zgadza i czy każdy przypadek niesprawdzony ma powód.

W tym, co pokazuje PR, zmieniają się dwa miejsca. Przypadek, którego autor nie sprawdził, stoi wśród pominiętych kroków z powodem, a gdy da się go sprawdzić ręcznie — z krokami; gdy produkt nie ustalił drogi, którą agent dociera do jego działającej wersji, przejście jest „niewykonane” z tego powodu, cykl się nie zatrzymuje, a zrzut ekranu niesprawdzony z tej samej przyczyny stoi w tej samej pozycji, nie w drugiej. Błąd poza zadaniem, znaleziony przy przejściu, stoi w „Do poprawy albo przepuszczenia” z jednym pytaniem, czy zrobić z niego zadanie, bez względu na to, co cykl sądzi o tym, czy ktoś go odczuje.

Ta sama zmiana rozstrzyga jeszcze trzy sprawy dla procesu wokół niej. Odpowiedź na sprawę drogi agenta do działającego produktu — logi, interfejs, dane deweloperskie, miejsce zrzutów — jest decyzją produktu, choć mówi agentowi, jak pracować; skill produktu może trzymać kroki obsługi i powołuje się na tę decyzję. Słowo na tę drogę obejmuje teraz także środek, którym agent pokazuje Ci, co zobaczył. A krok, który rozstrzyga technologię produktu, mówi teraz przy każdej opcji interfejsu, czy dwa cykle zadania w osobnych katalogach roboczych mogą sprawdzać działający produkt naraz bez wspólnej przeglądarki; opcja, która nie może, zostaje w porównaniu z tym brakiem.

### Pod spodem

Metoda pochodzi z praktyki testowania ze skilla zespołu i z dwóch kursów, których czytelnik tego repozytorium nie może otworzyć, więc decyzja w dzienniku nazywa, co przejęto, gdzie obowiązuje i dlaczego, a plik metody trzyma kroki. Zmiana to sam Markdown: jeden nowy plik metody, odnośniki w skillach autora i recenzenta, szablon opisu PR-a, szablon i dziennik decyzji, słownik i krok technologii.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Do poprawy albo przepuszczenia

brak

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

1. Cykl dokonał trzech wyborów, które zadanie i fundament zostawiają otwarte. Po pierwsze, pięć rozstrzygniętych odpowiedzi o przejściu stoi w dzienniku jako trzy decyzje — kto przechodzi i przy jakich zmianach; kto zatwierdza przypadki; co z przypadkiem, który wypadł źle, i z błędem poza zadaniem — a nie jako jedna, bo każdą z nich można zmienić osobno; przejęcie praktyk ze skilla zespołu i kursów stoi w pierwszej z nich. Po drugie, nazwę nowego pliku metody nadał cykl, bo zadanie zostawiło ją otwartą. Po trzecie, gdzie odwołania w zadaniu nie zgadzały się z plikami, cykl poszedł za plikami: zadanie powołuje się na decyzję o skutkach poza repozytorium przy „braku pauz w środku cyklu”, a nowa decyzja powołuje się na tę, która robi z PR-a Twój pierwszy punkt przeglądu; akapit szablonu PR-a, który zadanie wskazuje jako miejsce reguły o śladach tekstowych, nie istnieje, więc ta reguła została tam, gdzie jest, w górnej części, z jedną dopisaną klauzulą. Inna odpowiedź zmieniłaby, co wiąże fundament, a więc jak następna zmiana czyta te reguły.
2. Trzy decyzje w dzienniku są nowe, napisane przez cykl z rozstrzygnięć zadania, każda z parą przykładów („zgodne” i „naruszające”), której zadanie nie podaje i z którą agenci będą porównywać późniejsze zmiany; pary stoją słowo w słowo w dolnej części. Prostymi słowami każda mówi: (a) autor zmiany, albo agent części zmiany robionej według planu, sprawdza w działającym produkcie to, czego nie obejmują testy, po kodzie i przed recenzją, przy każdej zmianie tego, co widzi użytkownik; gdy nie ustalono drogi do produktu, przejście jest „niewykonane” z tym powodem i cykl idzie dalej; gdy późniejszy audyt pokaże błąd, który autor przepuścił, przejście przechodzi do osobnego etapu; (b) nikt nie zatwierdza przypadków przejścia, zanim je wykonano, i cykl się dla nich nie zatrzymuje; doprecyzowanie zadania nie zapisuje listy wejść do wypróbowania; (c) przypadek, który wypadł źle, jest poprawiany przed recenzją z testem, a błąd poza zadaniem jest zgłaszany i trafia do Ciebie w „Do poprawy albo przepuszczenia” z pytaniem, czy zrobić z niego zadanie. Dwie starsze decyzje dostały po jednym dopisanym przykładzie w swoich parach: ta o tym, gdzie rozstrzyga się technologię potrzebną projektowi (skill produktu trzyma kroki i powołuje się na decyzję; produkt, który trzyma drogę tylko w skillu, łamie regułę), i ta o dwóch cyklach sprawdzających naraz (krok technologii mówi to przy każdej opcji). Ich znaczenie pochodzi z zadania.
3. Nowa decyzja w jednym obszarze przeważa nad starszą, i cykl to zapisał. Starsza decyzja mówi, że cykl stawia przed Tobą tylko niepoprawione uwagi, które uzna, że Ty albo użytkownik odczujecie. Nowa decyzja o przypadku, który wypadł źle, mówi, że każdy błąd poza zadaniem znaleziony przy przejściu idzie do Ciebie niezależnie od tej oceny, żeby żaden nie wypadł z opisu; nowa jest zapisana jako zawężająca starszą. Fragmenty tego, co zaakceptowałeś, które dają wynik: pozycja 5 w „Do zrobienia” zadania mówi, że błąd spoza zakresu zadania znaleziony przy przejściu „trafia do sekcji dla decyzji człowieka jako sprawa do rozstrzygnięcia (zrobić z niego zadanie czy puścić)”, a wiersz 5 rozstrzygnięć mówi, że autor błąd poza zakresem zadania „zgłasza do PR-a jako sprawę dla człowieka”.

## Koszt

Około 52 minut pracy, z czego 19,5 to czekanie na narzędzia, i 64,9 mln tokenów razem, w większości odczyt z pamięci podręcznej: 48,1 mln na modelu autora i orkiestratora (sonnet) i 16,8 mln na modelu recenzentów (opus, najmocniejszy dozwolony w tej sesji). Przegląd całej zmiany raz wypadł źle (sześć uwag blokujących i sześć drobnych), został raz poprawiony i przeszedł; przegląd kroku zwrotnego raz wypadł źle (jedna uwaga blokująca), został raz poprawiony i przeszedł; żadna runda nie została nierozstrzygnięta. Bramką końcową jest przebieg CI na ostatnim commicie, niżej. Tabela etapów jest w zatwierdzonym rekordzie: `docs/task-cycles/walkthrough-in-running-product/stages.md` w commicie `RECORD_SHA`.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do rekordu przetrwa tylko tak. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

- `940893de` — the foundation step and the code, by the one author: the new method file `task-cycle/change/walkthrough.md` (sections: preparation; what the change alters for the user and the shared code it touches; scope of the task's requirements against what the tests cover; the plan of cases with the column of the way of the product that checks each, in the order of conditions and building of state, and a last row for what is noticed on the way; the rules of the walk; the verdict of each case with its layer, and "what I did not check"; the comparison of two measurements); a pointer in `task-cycle/change/SKILL.md` section 3 (the readers: the one author and the executor of a slice; not the fix) and a bullet of the report in section 6; a bullet in `task-cycle/review/SKILL.md` ("The author's own-work check"); in `task-cycle/skill/request_template.md` kinds 4 and 8, the pointer in kind 13 and the sentence on the artifacts of the check; question 1 of `elements/decisions/template.md`; the glossary entry; point 3 of `project-level/technology/research.md`; in `foundations/decisions.md` WAY-406, WAY-407, WAY-408 and the added paragraphs of WAY-121 and WAY-319. `task-cycle/change/ui_check.md` is unchanged.
- `cdbde3d2` — the fix of the six blocking and six Minor findings of the review of the whole change: the column "by what" of the plan names only ways of the running product and a reading of the code fills no row; the cases and verdicts of the walk stay in the reports and are not listed in *Checks*; WAY-408 names its group and records that it narrows WAY-289; the method looks for the product's skill by the decision's identifier, the direction WAY-121 gives; the two course items the task puts out of scope removed from the *Rejected* of WAY-406; WAY-407's *Scope* gains `project-level`; the form of the binding sentences, the *Rationale* wording and the readers named in the report bullet.
- `83aa64db` — the return step: kind 8 of the request template titled for the walk's errors too and saying "its author or executor"; the question of WAY-408 names the executor; log lines re-flowed to the log's width with no change of words.
- `f9054319` — the fix of the one blocking finding of the review of the return step: the lower part's paragraph *Findings outside the task's scope*, the top part's sentence on artifacts and the bullet of the review skill say "an author or the executor of a slice".

## Checks

- Final gate: the CI run on the request's last head, `CI_PENDING`.
- The list of failing checks before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/144, since the base is a merge commit with the tree of its second parent and no gate ran on it: one flaky test, `test_remove_merged_worktrees.ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` (`FileNotFoundError` on `maintenance.lock`, a race with Git's background maintenance), which failed on Linux in that request's first CI run and passed on the second attempt.
- Focused checks by the agents (all exit 0): `python -B gate/run_tests.py task-cycle` (534 tests, 2 skipped) at `940893de`, `cdbde3d2`, `83aa64db` and `f9054319`; `project-level` (279), `elements/common` (257) and `agent-instructions` (37, 2 expected failures) at `940893de`; `elements/common` again at `cdbde3d2`. The tests of `project-level` and `agent-instructions` were not rerun at the later heads: no file of those directories changed after `940893de`, and the later commits change Markdown only.
- `python -B elements/common/foundation_check.py` without `--skip-test-citations` on the finished change: exit 0, `0 errors`, no `listed:` line.
- `python -B agent-instructions/skill_entry_points.py`: exit 0, entry points current (no skill description changed).
- `python -B task-cycle/private_paths_check.py` on each changed file: exit 0, with a positive control (exit 1 on a file holding a user path). `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, 18 merges, `reminder: no`.
- Own-work checks (WAY-164): the author named the requirement most likely missed — no private path or note title in a committed file and the entries in the template's form — checked by the three commands above and a search for the names of the private sources: nothing found. After the fix, the author checked the path of an out-of-scope error from the walk to the human by reading WAY-408, kind 8 and the lower part against each other; the review of the return step then found one place of the template still reading "the author" and it was corrected.
- No walk through a running product ran: this change alters no behaviour a user sees in a running product (it changes the process's own texts); the new rules apply from the next change.
- `python -B task-cycle/request_check.py` on this description and `python -B task-cycle/private_paths_check.py` on it: `DESC_CHECKS_PENDING`.
- On the copy of the record: `COPY_CHECKS_PENDING`.
- The remarks check on the original record: run 1 exit 1 (13 items listed, appended word for word), run 2 exit 0.
- No working copy of an agent stays. No directory of an earlier task stays.

## Foundation entries

- **WAY-406** — marked `row 1`, `row 2`, `row 3`, and `the cycle's` for its pair of examples. The author of a change, and the executor of each slice that alters behaviour a user sees, walks through the running product what the tests do not cover, after the code and before the review; the walk is required for every such change, is "not performed" with its reason where the foundation settles no way to the product without stopping the cycle, the fix of a review's findings does not repeat it, and a stage of its own comes only if the audit shows an error the author let through; the practices of `test-run` and the courses bind only through this decision. Its pair, word for word:
  - complies: the author of a change that alters what an API answers walks through the running product by the way its foundation settles, with cases drawn from the requirements of the task and a last case for what it notices on the way, and reports the verdict of each case; where the foundation settles no way, it reports the walk as not performed for that reason and keeps the cases marked unchecked, and the description holds one item for the walk and the screenshot left unchecked; the executor of a slice that alters a screen walks through its slice, and the executor of a slice that only moves code reports that its slice alters no behaviour a user sees;
  - violates: the author of a change that alters what a command prints reports only that its tests pass; the executor of a slice leaves the walk to the executor of the last slice; the fix of a review's findings walks through the product again; a cycle stops because the foundation settles no way to the running product; the description shows the screenshot left unchecked and the walk not performed as two items.
- **WAY-407** — marked `row 4`, and `the cycle's` for its pair. No one approves the cases of the walk before it is made and the cycle does not stop for them; the author or the executor draws them from the requirements of the task and the human sees in the request what was not checked; the refinement of a task writes no list of inputs to try. Its pair, word for word:
  - complies: the author or the executor draws the cases from the requirements of the task and starts the walk with no one's approval, the plan stands in its report, and the request lists each case left unchecked; the task document of a change a user sees holds no list of inputs to try;
  - violates: the cycle stops to ask the human to approve the cases; the refinement of a task writes into the document the inputs a human gave to try, as the plan of the walk.
- **WAY-408** — marked `row 5`, and `the cycle's` for its pair and for the precedence it records over WAY-289 (item 3 of *You accept by merging* carries the passages of what the human accepted that give the outcome). The author or the executor corrects a case that fell wrong before the review, with a test at the lowest level that catches the error, and reports an error outside the task's scope, which the request puts before the human under *Fix or let through* to make a task of or let through. Its pair, word for word:
  - complies: a case of the walk falls wrong, the author finishes the walk, corrects the error with a unit test that fails before the correction and passes after it, and reports the case, the correction and the test; an error in a part of the product that the task does not touch is reported, not corrected, and the description asks under *Fix or let through* whether to make a task of it, whether or not the cycle judges that the user or the human will feel it;
  - violates: the author notes in the report that a screen differs from the task and leaves it to the review; a correction of a case has no test; the author corrects an error outside the scope of the task in the same change; the description of the request does not mention such an error, or leaves it out because the cycle judges it will not be felt.
- **WAY-121** — changed, marked `row 9`, and `the cycle's` for the two added items of its pair. The answer to a matter of an agent's way to the running product is a decision of the product though it tells an agent how to work, and a skill of the product may hold the steps of operation and cites that decision. The added items, word for word: complies — "a product whose skill for playing its game holds the steps to start the game cites the decision that settles the way to the game and the place of its screenshots"; violates — "a product keeps the way to its game or the place of its screenshots only in a skill, with no decision of its log".
- **WAY-319** — changed, marked `row 11`, and `the cycle's` for the two added items of its pair. The condition reaches a product through the step that settles technology, which says for each option of the interface whether two cycles can check at once without a shared browser, and an option that cannot stays in the comparison with that lack. The added items, word for word: complies — "the step that settles the interface of a product says of each option whether two cycles can check at once without a shared browser, and an option that cannot stays in the comparison with that lack"; violates — "a comparison of the options of an interface that does not say whether two cycles can check at once".
- **Template of decisions, question 1 of "Where it goes"** — `row 9`: the answer on a matter of an agent's way to the running product goes to the log, not to a skill, and a skill of the product may hold the steps and cites the decision.
- **Glossary, "agent's way to the running product"** — `row 10`: the way is also the means by which the agent shows the human what it saw.
- Rows 6, 7 and 8 of *Settlements to record* are in `task-cycle/change/walkthrough.md`, and row 11 also in point 3 of `project-level/technology/research.md`; they write no entry. No topical section of the log is opened (the three decisions stand in the section "The work of a cycle's agents"). No invariant, surface or *Violated* mark is changed.

## Minor findings

The Minor findings of the reviews that no fix made. Those of the review of the whole change and of its fix were all fixed by the fix or by the return step. What stays, all cosmetic:

- Review of the return step, finding 3, `task-cycle/skill/request_template.md:251` and `:264`: "Two lines over the template's width introduced by the commit. `request_template.md:251` (160 characters) and `request_template.md:264` (113 characters). Before the commit no prose line of kind 8 passed the width ... The same commit re-flowed the log for its width, so the template's kind 8 is left in the shape the commit corrected elsewhere. Polish; no reader is misled."
- Review of the fix of the return step, `task-cycle/skill/request_template.md:187`: "runs to 118 characters, past the width of the template's prose (the line was re-flowed only on line 186, and line 187 kept its old tail). Polish; no reader is misled."

## Findings outside the task's scope

- Review of the whole change, O1, `project-level/definition_template.md:241`: "the Technology section of the definition template carries WAY-166's rule for an option an agent cannot use but not WAY-319's condition that `research.md` now carries. The task names only `research.md`; whether the template should carry it too goes beyond the task."
- Review of the whole change, O2, `task-cycle/skill/SKILL.md` (the orchestrator's check of a `make-change` report, which looks for the own-work check): "does not look for the walk's part of the report. The task asks for no such check; outside its scope."
- No error found by a walk (none ran). No check outside the task's parts failed and passed again in this cycle's runs.

## Course of the cycle

- **Task and sources:** the task "give the agents of the-way a method of testing in the running product what automatic tests do not catch", independent, in the author's backlog (note updated 2026-11-15, accepted by the day advisor on the owner's behalf); sources: the testing skill of a team repository, two courses (not open to a reader of this repository) and the foundation at base `9cffc9ba`.
- **Process pin:** not applicable — this is the-way itself, the checkout the session works in.
- **Spec:** none; the task settles every question it names, and the one detail it leaves, the name of the method file, is a choice of how to make what it settles.
- **Route:** one author without a plan (the-way-author, class `same`, sonnet) — one new file, pointers in four files and a foundation step of a few entries and three sentences; no part needed a division.
- **Plan:** none.
- **Choices:** 7 choices of the cycle, in the questions table of the record (the author's class, the reviewers' model, the file's name, the split into three decisions, the pairs of examples, the wording of the lack in the technology step and of kind 8, the references of the task that did not match the files).
- **Blocking findings left:** none.
- **Record:** `docs/task-cycles/walkthrough-in-running-product/cycle.md` at commit `RECORD_SHA`.
