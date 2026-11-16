**State: draft** — the code is finished and reviewed; the CI run on the last head has not ended yet, and one question below waits for your answer.

## What you will see

From now on the process stops one more way of getting a green test without a working product. A reviewer of any change, in every review of a cycle, also reads the product's code for code that passes a test without meeting the requirement: a branch or a value made for the very input a test uses, a test's expected value written into the product's code, a comment about a special case for a test, or a comparison changed so that a test's check comes out true. Such a finding blocks the change. Only code that exists to make a test pass counts; a special case the requirement itself asks for is no finding.

The agent that makes the change has a way out as well. Where a test expects what the requirement rules out, or where the agent cannot make a test pass with code that meets the requirement for every input, it writes no code for the test's input and does not touch the test: it commits what it has and asks the orchestrator of the cycle a question that names the test, quotes the requirement and says what it tried. The orchestrator answers only from the task, its spec, a decision or the sentence of an invariant, quoting the passage. Where none of them settles it, the cycle opens a blocked draft request with the question for you, instead of choosing a reading itself; and the executor of a part of a plan that asks such a question is not retried on a stronger model, since a stronger model does not settle what the requirement is. The description of a request has a new variant for that blocked draft.

Five entries of the foundation come with it: two decisions and three facts about the outside world that the decisions rest on.

### Underneath

The change is text: four files of the cycle's skills, two files of its review of a fix and of a correction, the decision log and the file of environment facts; no script and no test changed.

## For you to decide

### Needed from you

none

### Fix or let through

1. Two rules of the process now give different answers to the same case, and none says which one wins. One rule says that a decision that borrows a practice from outside must list among its rejected ways what it leaves out of that practice. Another says that a decision written from a row of the task's settlements may list as rejected ways only those that the person who settled the row named. The two new decisions of this request fall under both. The review of the whole change read the case by the second rule, and the return step by the first and added to the rejected ways of both decisions what they leave out; the review of the return step failed that addition, because no person had weighed those ways, and it was reverted. The next task whose settlements adopt an outside practice meets the same two readings, and whichever agent meets it either leaves out what the first rule asks or adds rejected ways nobody weighed. Fixing it in this request costs a correction with one fix and a review of it, and it would change a decision this task does not carry; undoing it costs one more edit of the log. Making a task of it costs a later task and leaves the two readings in force until then; undoing it, nothing. Letting it through accepts the two readings; undoing it later costs the same task. I recommend making a task of it, with the answer the reviewer proposes (the second rule narrows the first, and refinement puts what a practice leaves out among the ways the person weighed), since it changes entries this task does not carry and needs your word on which rule wins. Its weak point: a task that adopts an outside practice may reach its cycle before this task is done, and that cycle will read the case one way or the other. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The rule for reviewers is written as a decision, and I added to it a pair of examples that the task did not give — what a review that follows the rule does, and what a review that breaks it does — which agents will compare later changes with; the pair stands word for word in the lower part. The rule lives in the reviewer's own method and in no product's testing guidelines, so it holds in every cycle, as you answered. The decision's reason for not leaving things as they are says no case is known in 83 task cycles; that count is from the task and is your own record, which the entry says is not open to a reader of the repository.
3. The rule for the agent that meets a test it cannot pass is written as a decision too, with a pair of examples of mine, word for word in the lower part. It says that the question is no third reason to return without code (the work would be thrown away), and that the orchestrator never picks "the smallest reversible reading" for it. It narrows the retry that a failed executor of a part gets, as you decided.
4. Three entries of facts about the outside world, where the task asked for one. The first is what the system card of Claude 3.7 Sonnet says about the model returning expected test values and marking it with a comment. The second is what ImpossibleBench names as four ways of cheating, three of them complying with a ban on editing tests. The third is the effect of an option to hand a task to a human. I wrote three because each says one thing and changes for one reason, and the existing fact that another rule rests on is left alone. I read each source myself, and the reviewer compared every quoted passage and both figures with the sources again; all matched.
5. The third fact says what the task's text leaves out: the paper reports that the option lowered cheating of GPT-5 from 54% to 9% and of another OpenAI model from 49% to 12%, and that the effect was much less pronounced for Claude Opus 4.1. The agents of this process run on Claude, so the decision says that it takes the figures across publishers and that their size is no promise for these agents; the way out stands on its own reason without them.
6. The task gave three reasons for not putting the review rule into the product's testing guidelines. One of them, that the process repository departs from those guidelines, no longer holds, since the repository now follows them. The decision lists the two reasons that still hold and not the third, so as not to put a false reason into the log.
7. The cycle changed two files the task did not name: the method for the review of a fix, so that a fix that adds code made for a test also fails its review, and the method for a correction after review, so that your answer to the new blocked draft has a way to go on and the draft is not waited for in CI, as for the other blocked kinds. Without them the rule would stop short of the review of a fix and of the step after your answer.

No existing invariant test changed, and no sentence of an invariant was reworded.

## Cost

About 39 minutes of active stages and about 52 million tokens: the author on Sonnet (four turns: the change, the fix of the review of the whole change, the return step, the fix of the review of the return step), four reviewer turns on Opus (the whole change and its fix, the return step and its fix), and the orchestrator on Sonnet. Two reviews failed — the whole change and the return step — each with one fix and a passing review of the fix. The table of stages is in the committed record, linked below.

## How to merge

Merge with a merge commit, not squash or rebase, so that the link to the cycle's record, which names a commit, stays reachable. Nothing in this request waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: szkic** — kod jest gotowy i sprawdzony; przebieg CI na ostatnim commicie jeszcze się nie skończył, a jedno pytanie poniżej czeka na Twoją odpowiedź.

## Co zobaczysz

Od teraz proces zamyka jeszcze jedną drogę do zielonego testu bez działającego produktu. Recenzent każdej zmiany, w każdym przeglądzie cyklu, czyta też kod produktu pod kątem kodu, który przechodzi test bez spełnienia wymagania: rozgałęzienia albo wartości zrobionej pod to jedno wejście, którego używa test, oczekiwanej wartości testu wpisanej w kod produktu, komentarza o specjalnym przypadku dla testu albo porównania zmienionego tak, żeby sprawdzenie testu wychodziło prawdziwe. Takie znalezisko blokuje zmianę. Liczy się tylko kod, który istnieje po to, żeby test przeszedł; specjalny przypadek, o który prosi samo wymaganie, nie jest znaleziskiem.

Autor zmiany też ma wyjście. Gdy test oczekuje tego, co wymaganie wyklucza, albo gdy autor nie umie przejść testu kodem, który spełnia wymaganie dla każdego wejścia, nie pisze kodu pod wejście testu i nie rusza testu: commituje to, co ma, i zadaje orkiestratorowi cyklu pytanie, które nazywa test, cytuje wymaganie i mówi, co autor próbował. Orkiestrator odpowiada wyłącznie z zadania, jego specyfikacji, decyzji albo zdania niezmiennika, cytując fragment. Gdy żadne z nich nie rozstrzyga, cykl otwiera zablokowany szkic PR-a z pytaniem do Ciebie, zamiast samemu wybierać odczytanie; a wykonawca części planu, który zadaje takie pytanie, nie dostaje ponowienia na silniejszym modelu, bo silniejszy model nie rozstrzygnie, czym jest wymaganie. Opis PR-a ma nowy wariant na taki zablokowany szkic.

Razem z tym wchodzi pięć wpisów fundamentu: dwie decyzje i trzy fakty o świecie zewnętrznym, na których decyzje stoją.

### Pod spodem

Zmiana to tekst: cztery pliki skilli cyklu, dwa pliki przeglądu poprawki i korekty, dziennik decyzji i plik faktów środowiska; żaden skrypt ani test się nie zmienił.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Popraw albo przepuść

1. Dwie reguły procesu dają teraz różne odpowiedzi w tym samym przypadku i żadna nie mówi, która wygrywa. Jedna mówi, że decyzja, która pożycza praktykę z zewnątrz, ma wypisać w odrzuconych drogach to, czego z tej praktyki nie wzięła. Druga mówi, że decyzja napisana z wiersza ustaleń zadania może wypisać jako odrzucone tylko te drogi, które nazwała osoba rozstrzygająca wiersz. Dwie nowe decyzje z tego PR-a podpadają pod obie. Przegląd całej zmiany odczytał ten przypadek wedle drugiej reguły, a krok zwrotny wedle pierwszej i dopisał do odrzuconych dróg obu decyzji to, czego nie wzięły; przegląd kroku zwrotnego odrzucił ten dopisek, bo żaden człowiek tych dróg nie ważył, i został cofnięty. Następne zadanie, którego ustalenia przyjmują praktykę z zewnątrz, trafi na te same dwa odczytania, a agent, który na nie trafi, albo pominie to, czego chce pierwsza reguła, albo doda odrzucone drogi, których nikt nie ważył. Poprawa w tym PR-ze kosztuje korektę z jedną poprawką i jej przeglądem, a zmieniłaby decyzję, której to zadanie nie niesie; cofnięcie kosztuje jeszcze jedną edycję dziennika. Zrobienie z tego zadania kosztuje późniejsze zadanie i zostawia obie reguły w mocy do tego czasu; cofnięcie — nic. Przepuszczenie przyjmuje dwa odczytania; cofnięcie później kosztuje to samo zadanie. Polecam zrobić z tego zadanie, z odpowiedzią, którą proponuje recenzent (druga reguła zawęża pierwszą, a doprecyzowanie zadania wpisuje to, czego praktyka nie wzięła, wśród dróg, które człowiek ważył), bo to zmienia wpisy, których to zadanie nie niesie, i potrzebuje Twojego słowa, która reguła wygrywa. Słaby punkt: zadanie przyjmujące praktykę z zewnątrz może dojść do swojego cyklu, zanim to zadanie powstanie, i ten cykl odczyta przypadek tak albo inaczej. Poprawić w tym PR-ze, zrobić z tego zadanie czy przepuścić? (Findings outside the task's scope, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

2. Reguła dla recenzentów jest zapisana jako decyzja i dodałem do niej parę przykładów, której zadanie nie dawało — co robi przegląd, który trzyma się reguły, a co przegląd, który ją łamie — z którą agenci będą porównywać późniejsze zmiany; para stoi słowo w słowo w dolnej części. Reguła mieszka w metodzie samego recenzenta, a w niczyich wytycznych testów produktu, więc działa w każdym cyklu, tak jak odpowiedziałeś. Powód decyzji, by nie zostawiać jak jest, mówi, że nie znany jest żaden przypadek w 83 cyklach zadań; ta liczba pochodzi z zadania i jest Twoim własnym zapisem, którego, jak mówi wpis, czytelnik repozytorium nie może otworzyć.
3. Reguła dla agenta, który trafia na test nie do przejścia, jest też zapisana jako decyzja, z moją parą przykładów, słowo w słowo w dolnej części. Mówi, że pytanie nie jest trzecim powodem zwrotu bez kodu (praca poszłaby do kosza) i że orkiestrator nigdy nie wybiera dla niego „najmniejszego odwracalnego odczytania”. Zawęża ponowienie, które dostaje wykonawca części, który zawiódł, tak jak zdecydowałeś.
4. Trzy wpisy faktów o świecie zewnętrznym, tam gdzie zadanie prosiło o jeden. Pierwszy to to, co karta systemowa Claude 3.7 Sonnet mówi o tym, że model zwraca oczekiwane wartości testów i znaczy to komentarzem. Drugi to cztery sposoby oszukiwania, które nazywa ImpossibleBench, z czego trzy zgadzają się z zakazem edycji testów. Trzeci to skutek opcji oddania zadania człowiekowi. Napisałem trzy, bo każdy mówi jedną rzecz i zmienia się z jednego powodu, a istniejący fakt, na którym stoi inna reguła, zostaje nietknięty. Każde źródło przeczytałem sam, a recenzent porównał jeszcze raz z źródłami każdy cytowany fragment i obie liczby; wszystko się zgadza.
5. Trzeci fakt mówi to, co tekst zadania pomija: artykuł podaje, że opcja obniżyła oszukiwanie GPT-5 z 54% do 9%, a innego modelu OpenAI z 49% do 12%, i że dla Claude Opus 4.1 efekt był znacznie słabszy. Agenci tego procesu działają na Claude, więc decyzja mówi, że przenosi te liczby ponad wydawców i że ich wielkość nie jest obietnicą dla tych agentów; wyjście stoi na własnym powodzie bez nich.
6. Zadanie podało trzy powody, by nie wpisywać reguły recenzenta do wytycznych testów produktu. Jeden z nich, że repozytorium procesu od tych wytycznych odstępuje, już nie obowiązuje, bo repozytorium teraz za nimi idzie. Decyzja wymienia dwa powody, które dalej obowiązują, a nie trzeci, żeby nie wpisać do dziennika fałszywego powodu.
7. Cykl zmienił dwa pliki, których zadanie nie nazwało: metodę przeglądu poprawki, żeby poprawka dodająca kod zrobiony pod test też nie przeszła swojego przeglądu, oraz metodę korekty po przeglądzie, żeby Twoja odpowiedź na nowy zablokowany szkic miała którędy iść dalej, a szkicu nie czekało się w CI, jak przy pozostałych rodzajach zablokowanych. Bez nich reguła urywałaby się przed przeglądem poprawki i przed krokiem po Twojej odpowiedzi.

Żaden istniejący test niezmiennika się nie zmienił i żadne zdanie niezmiennika nie zostało przeformułowane.

## Koszt

Około 39 minut aktywnych etapów i około 52 mln tokenów: autor na Sonnecie (cztery tury: zmiana, poprawka po przeglądzie całej zmiany, krok zwrotny, poprawka po przeglądzie kroku zwrotnego), cztery tury recenzentów na Opusie (cała zmiana i jej poprawka, krok zwrotny i jego poprawka) oraz orkiestrator na Sonnecie. Dwa przeglądy nie przeszły — całej zmiany i kroku zwrotnego — każdy z jedną poprawką i przechodzącym przeglądem poprawki. Tabela etapów jest w zatwierdzonym zapisie, podlinkowanym niżej.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase, żeby link do zapisu cyklu, który wskazuje commit, pozostał osiągalny. Nic w tym żądaniu nie czeka na przegląd fundamentu.

</details>

## Technical changes

- `477ea5ad` — three environment facts in `foundations/environment_facts.md`, after `impossiblebench-test-modification`: `claude-test-special-casing` (the system card of Claude 3.7 Sonnet, chapters 6 and 6.2), `impossiblebench-cheating-strategies` (the four strategies, § 4.1) and `impossiblebench-abort-option` (the option to abort with a flag for a human, § 5.3). The author read the card and the paper and matched each quoted passage; the reviewer matched all of them again.
- `c8eef488` — the two decisions and the skill edits. WAY-409 closes the section "Review of a change" and WAY-410 closes "The work of a cycle's agents" in `foundations/decisions.md`. `task-cycle/review/SKILL.md`: a new item of section 2 (the four signals, the narrow qualifier) and the grade in section 3 (Important at the least, in every review). `task-cycle/change/SKILL.md`: a new item of section 2 and pointers in sections 1, 5 and 6 (the author commits, returns the status `questions` and writes nothing for the test's input). `task-cycle/skill/SKILL.md`: a paragraph on a question about a test after the paragraph on an agent that returns `questions`, the early-stop list at the head, step 9 sub-step 4 (no retry on a higher class) and the list of copies of the record. `task-cycle/skill/request_template.md`: kind 2 of *Needed from you* admits the question, and a new row of the table of variants. `task-cycle/review/fix.md` and `task-cycle/skill/correction.md`: see item 7 of *You accept by merging*. No script and no test changed; `task-cycle/request_check.py` reads no row of the table of variants and needed no change.
- `1a17406a` — the fix of the review of the whole change: the head of the skill and the first line and ways open of the new template row now carry both cases of WAY-410 and its four sources; the stages named as not run follow the code the question met, and a correction returns the open request to a draft; the zero count in WAY-409 no longer names a register and a date the task does not give for it; the three pointers name the paragraph that holds the rule.
- `91f6c884` and `b91fe896` — the return step's addition to the rejected ways of WAY-409 and WAY-410, and its revert after its review failed it; the final tree is the one of `1a17406a`.

## Checks

- Final gate: the CI run on this request's last head — pending; its link, each check by name and its conclusion, and for a red run the tests that failed, are added when the run ends. The cycle ran no full gate on its own system, since CI runs on the request (step 10 of the cycle's skill).
- The list of checks failing before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/146, since the base `4758840f` is a merge commit with the tree of its second parent and no gate ran on it: none (every check of that request's one CI run passed).
- Focused checks by the author and the reviewers, each with exit 0: `python -B gate/run_tests.py task-cycle` (534 tests, 2 skipped, at `c8eef488` and `1a17406a`) and `python -B -m unittest discover -s task-cycle -p test_request_check.py` (74 tests, at `1a17406a`); `python -B elements/common/foundation_check.py` on the finished change, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
- Own-work checks (WAY-164): the author named as the requirement most likely not met that the skills restate the two decisions without widening them or dropping a qualification, and checked it with a script of 18 assertions on the changed files (18 of 18 on the head, 18 of 18 failing on the base); that check could not see a narrower restatement elsewhere in the same files, which the review of the whole change found twice (the head of the skill and the first line of the template row). After the fix the author wrote a second check that fails on a restatement that names one case or fewer than four sources: exit 1 with four failures on `c8eef488`, exit 0 on `1a17406a`; the reviewer of the fix searched the files on its own and found none left.
- Walk through the running product: not applicable, since the change alters no behaviour a user sees in a running product; it changes the text of the process and the foundation of the-way.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, 20 merges, `reminder: no`.
- Description: `python -B task-cycle/request_check.py <description> --task <frozen task>` and `python -B task-cycle/private_paths_check.py <description>` — to be run before publishing; their last runs are added with the link to the record.
- Copy of the record: the three checks on it are added with the link to the record.
- No working copy of an agent stays. No directory of an earlier task stays.

## Foundation entries

- WAY-409 — marked `the cycle's` (row 1, whole; a pair of examples added): every code review of a cycle looks in the product's code for code that passes a test without meeting the requirement, grades such a finding Important at the least so that it blocks, and judges only code that exists to make a test pass; the rule stands in the review's skill, in every cycle. The pair of examples, as the entry holds it:
  - complies: a reviewer finds that a function of the product returns 180 for the input 200 that a test uses, where the requirement gives a general rule that would not return it, grades the finding Important and the review fails; the same for a branch under a comment that says "special case for the test", and for a comparison operator overloaded so that the comparison a test makes comes out true; a product whose guidelines hold no testing discipline gets the same look; a branch on a value that the requirement itself names is no finding;
  - violates: a reviewer reads the files of tests and leaves the code of the product unread for this; a finding of such code is graded Minor and the change passes; a reviewer reports every special case of the product's code, the ones the requirement asks for among them; a review of a fix or of a correction leaves the look out.
- WAY-410 — marked `the cycle's` (row 2, whole; a pair of examples added; it narrows WAY-229): an agent that meets a test the requirement contradicts, or that it cannot pass by general code, writes no code for the test's input and does not change the test but commits and asks the orchestrator, which answers only from the task, the spec, a decision or an invariant and otherwise opens a blocked draft request with the question; a slice's executor gets no retry on a higher class. The pair of examples, as the entry holds it:
  - complies: an author whose test expects 180 for an input of 200, where the requirement says the discount never exceeds 10 percent, writes no branch for 200, leaves the test as it is, commits its work and returns a question that names the test, quotes the requirement and says what it tried; the orchestrator finds in the task the sentence that settles it and resumes the author with that sentence quoted, or, where the task, the spec, the decisions and the invariants say nothing, opens a blocked draft request with the question under *Needed from you*; the executor of a slice that returned such a question is not replaced by one of a higher class; a test that checks behaviour the task expressly changes is changed by the author, who names the requirement as its cause;
  - violates: an author writes a branch or a returned value for the input of the test; an author changes the expected value of a test to the code's output to turn it green; an author continues after meeting a contradiction and notes it in its report; the orchestrator answers such a question by the smallest reversible reading of the requirement; the cycle opens a blocked draft request for a contradiction that a sentence of the task settles; the executor of a slice that returned such a question gets a retry on a class higher.
- `claude-test-special-casing` — marked `the cycle's` (no row; *To do* 5): the system card of Claude 3.7 Sonnet reports that the model occasionally special-cases tests (returning expected values, modifying tests), often marking it with a comment, and names monitoring for such comments and for test modifications among its mitigations.
- `impossiblebench-cheating-strategies` — marked `the cycle's` (no row): ImpossibleBench names four cheating strategies and reports that the latter three work around instructions not to modify tests while technically complying.
- `impossiblebench-abort-option` — marked `the cycle's` (no row): in ImpossibleBench, an option to abort with a flag for a human lowered the cheating rate of GPT-5 from 54% to 9% and of o3 from 49% to 12%, with a much less pronounced effect on Claude Opus 4.1.
- No topical section of the decision log is opened, no kept row tied to an entry already stated, no invariant test altered, no surface altered and no *Violated* mark set or cleared; the foundation check lists no invariant for a corrected sentence and no test that holds a sentence of a decision by a line `decision:` is added, dropped or altered.

## Minor findings

- N1, found by the review of the fix of the whole change (Minor, within the task, outside the fix's diff, so it did not reopen that review), `foundations/decisions.md`, WAY-410, *Rationale*: "The *Rationale* reads "A slice's executor gets no retry on a class higher because a stronger model does not remove a contradiction in the requirement". The fix widened the same reason in the skill to both cases ("a stronger class does not settle what the requirement is", `SKILL.md:475-476`), so the skill now gives a reason the decision does not. For the second case — no general code passes the test, no contradiction seen — the decision's prose gives no reason why a stronger model would not help. Prose, not a binding sentence, and the binding sentence covers both cases, so no reader is led to a wrong act; Minor. Suggested wording: "because a stronger model does not settle what the requirement is"."

## Findings outside the task's scope

- Finding 2 of the review of the return step, marked outside the task's scope by the reviewer (Important by its effect; not blocking), WAY-100 and WAY-134 in `foundations/decisions.md`: "The foundation records no precedence between WAY-100 and WAY-134 for a decision written from a row that adopts a practice from outside. Where a row's source keeps no left-out parts of the practice, the two entries cannot both hold, and neither names the other in *Relations*. This cycle read the collision both ways — the review of the whole change by the template, the return step by WAY-100 — and each reading is defensible from one entry. Every later cycle whose row adopts an outside practice meets it again. The task does not ask for it to be settled, and recording a precedence changes a decision this task does not carry, so it is outside the task. Recommended for the request's list, with the answer I recommend: WAY-134 narrows WAY-100 for a decision written from a row, and the refinement of a task whose row adopts a practice carries the parts left out among the *Not chosen* of the row's answer, so that they reach *Rejected* as ways the human weighed. Leaving it unrecorded costs nothing today but gives the next cycle the same choice between two readings."

## Course of the cycle

- **Task and sources:** the task "the review catches code that bypasses a test, and the author stops when a test contradicts the requirement" (independent; the task's note in the author's backlog, approved 2026-11-14); sources: the system card of Claude 3.7 Sonnet, ImpossibleBench (arXiv 2510.20270), and the foundation of the-way at `4758840f`.
- **Process pin:** not applicable — the-way itself.
- **Spec:** none; the task leaves no open design choice (its four questions carry their answers and sources, and its two settlements settle their decisions).
- **Route:** one author without a plan, on the class of the orchestrator's model, since one agent can hold the change. The whole change failed its review once (one blocking finding, three Minor taken into the same fix) and the fix passed; the return step failed its review once (one blocking finding) and the fix, a revert, passed. No attempt was discarded.
- **Plan:** none.
- **Choices:** 10 — the 7 choices of the author named in its report (the layout of the template row, the status `questions` of the author's return, the blocked draft by pointer in the skill and no new file, three facts and not one, the two extra files, the pairs of examples, no change to the record template), the revert of the return step's addition after its review, and the 2 instructions of the human for this cycle (the strongest allowed model is `opus`; a local full run waits for the day advisor's start signal, and none was needed since CI is the final gate); see the questions table of the record.
- **Blocking findings left:** none.
- **Record:** the link is added when the record is committed.
