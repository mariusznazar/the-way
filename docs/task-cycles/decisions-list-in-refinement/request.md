**State: ready** — three items of "Fix or let through" wait for your answer (one small gap in the new check and two old gaps in the foundation's reasoning); what you only accept by merging waits for nothing.

## What you will see

When the refinement of a task is finished and the complete task document is about to be shown to you, a new step now runs first. It runs only for a task that names decisions of the foundation, or that changes a skill or an instruction file; for any other task the step is skipped and the agent says nothing of it. The step works like this:

- A first fresh agent, on a cheaper class of model than the refining agent's, gets only the complete task document and the full text of the decisions the document names, and nothing of the conversation. It lists each decision an executor would have to take alone that the document leaves unanswered or answers in part, and marks where each answer is known: written (where, in which sentence), visible only in a file the document names as a model, or guessed (with the answer the agent would take). A decision counts only if it follows from a sentence that really stands in the document or in a named decision, and if different answers give a different, noticeable result inside the task; the list owes no decision and no number, and a matter already asked by the check for a word that can be read two ways, or already among the task's questions, does not come back.
- A second fresh agent, on the same class, can read the repository the task changes. For each guess it says whether the repository or the document already settles the answer (with a quotation and a path), whether the guessed answer agrees with what the repository says, what would change in the files the task changes if the answer were another, and gives a verdict: most likely right, most likely wrong, or truly open. It writes in plain language and names what it did not check.
- The refining agent then opens the file behind each quotation that would keep a matter from you, and behind each matter it will show you, and checks the quotation word for word; it gives each matter one explicit verdict, the critique's or its own. A quotation that does not hold voids the critique's verdict on that matter.
- You see only the matters that are truly open and the gaps of the document itself (a guess the critique found most likely wrong counts as such a gap), at most about four, the most consequential first, each in plain language with the ways, their costs and a recommendation, together with the path of a file in the product's ignored working directory that keeps the full list, the critique and the verdicts. When nothing is open, you hear nothing about the step.
- Your answers go under the task's questions with your words as the source and the ways you did not choose, and what they change in the task's decisions in play and settlements enters the document as in the rest of the refinement.
- In a refinement led by a project orchestrator, the refining agent starts no agent: it writes one request for the two steps in its turn; the orchestrator runs them and writes the list and the critique into the file; the refining agent, resumed, checks the quotations, writes the verdicts and puts the open matters into its turn as material for you.

### Underneath

The change is three edits of the refinement skill's texts and two new decisions in the foundation's log, one for each of your two answers about the step; the full gate passed with 1,561 tests on the final tree.

## For you to decide

### Needed from you

none

### Fix or let through

1. The widened check of quotations (see item 4 below) names only guesses "settled in the repository"; it does not name a guess the second agent judged settled by the task document itself, though the second agent may settle a guess that way. The refining agent who meets such a guess would read the text literally and not open the document's quotation. The effect is small, since the document is the text the refining agent has just written and the quotation is quick to compare by eye, but someone reading the text strictly could skip it. Fixing it costs one fix and one more review round (about the length of the first fix round of this cycle) and changes one phrase in the skill and one in the decision; letting it through leaves the gap in the text, and making a task of it leaves it until someone does that task. I recommend letting it through, because the task document is the one source the refining agent has just written and sees whole. Fix it in this request, make a task of it, or let it through? (Minor findings, 1)

2. One old decision in the foundation, about how the options of a technology choice are tested before you choose, names three testing practices (a devil's advocate, a pre-mortem and a search for unknown unknowns) but not where they come from, and the foundation marks that source as still to be found. The change did not write or touch it; it stands there on the main branch already. Whoever reads that decision cannot tell where the practices come from, which matters when someone disputes them. Writing the source in this request costs a person who knows the source and one more round of review; making a task of it leaves the mark in place; letting it through accepts the gap on the main branch. I recommend making a task of it, since the change has nothing to do with that decision and nobody has named the source. Write the source in this request, make a task of it, or let it through? (Foundation entries, 6)

3. One old decision in the foundation, about what the breakdown of a project writes into its plan, names a practice (a roadmap of vertical slices) but not its source, and the foundation marks that source as still to be found. It also stands on the main branch already and the change did not touch it. The cost of each answer is as for the previous item. I recommend making a task of it, for the same reason. Write the source in this request, make a task of it, or let it through? (Foundation entries, 7)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. The cycle widened your answer about checking the critique's quotations: the refining agent opens the file behind each quotation that keeps a matter from you (a guess judged already settled in the repository, or most likely right), not only behind the matters it shows you. Your task item says "for each matter it will show", but your own reason in the answer to the second question (the critique may judge a matter settled when the first agent was right to doubt) is the case where a wrong "settled" would hide a real open matter, and the first version of the text would not have guarded it. The review of the whole change blocked on this. The other way, to change the decision's own example to a shown matter, would have kept the task's words and left your named reason unguarded. The price is one more file opened for each guess kept from you, at most as many as the list holds.
5. A guess the critique finds most likely wrong is shown to you as a gap of the document, and not left out of your sight: the task said you see "the open matters and the gaps of the document" and did not say what happens to a wrong guess, and an executor would take the wrong answer. A guess it finds most likely right and a guess it finds settled stay in the file. The price is one more matter shown within the limit of about four.
6. The full list, the critique and the verdicts are kept in one file in the product's ignored working directory, named after the task, in three parts, and no agent of the step writes it: the refining agent writes what each agent returns (and in the orchestrated refinement the orchestrator writes the list and the critique and the refining agent the verdicts). The task fixed only "a file in the ignored directory". The other way, each agent writing its own part, would have broken the rule that only the refining agent writes the task's files and the habit that the critic writes no files. The price is that the returns are copied by hand.
7. In the refinement led by a project orchestrator, the step takes two turns of the refining agent (a request, then the turn with the checks and the verdicts), and the request itself names the method, the cheaper class and what the first agent is given, because no file of the orchestrator says anything of this kind of request. The other way, a new pointer file for the orchestrator, was outside your task. The price is that an orchestrator that does not follow the request's words could hand the first agent the conversation; the words ask for the opposite.
8. The decision about taking this practice from the course says in its reasoning, not in its list of rejected ways, what it leaves out of the practice: the count of how many guesses you would settle otherwise and the minutes spent reading the list, which your notes keep for the trial. Its rejected ways hold only the three ways your answers keep, as the rule for a decision written from your rows allows; a fourth way would have had to be invented.

## Cost

The cycle's working time counted by the script was about 31 minutes, and the cycle used about 20 million tokens, almost all of it cached input, all on the same class of model as the orchestrator's: one author, resumed twice (for the fix and for the return step), and one reviewer, resumed once. The review of the whole change blocked once; the one fix and its review passed, and the return step found nothing to change. The full gate took 14 minutes 22 seconds and passed. The table of stages stands in the record of this cycle (Course of the cycle, Record). Directories of earlier tasks still stand because the cleaning script could not tell they were no longer needed; nothing in this request waits for them, and you may remove them by hand (their names, branches and reasons stand under Checks).

## How to merge

Merge with a merge commit that keeps the commits, since the link to the cycle's record survives only then.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — na Twoją odpowiedź czekają trzy pozycje z „Popraw albo przepuść” (jedna mała luka w nowym sprawdzeniu i dwie stare luki w uzasadnieniach fundamentu); to, co tylko akceptujesz przez scalenie, na nic nie czeka.

## Co zobaczysz

Gdy doprecyzowanie zadania jest skończone i kompletny dokument zadania ma być pokazany Tobie, najpierw biegnie nowy krok. Uruchamia się tylko dla zadania, które wskazuje decyzje fundamentu albo zmienia skill lub plik instrukcji; przy każdym innym zadaniu krok jest pominięty i agent nic o nim nie mówi. Krok działa tak:

- Pierwszy świeży agent, na klasie modelu tańszej od klasy agenta doprecyzowania, dostaje tylko kompletny dokument zadania i pełne brzmienie decyzji, które dokument wskazuje, bez rozmowy. Wypisuje każdą decyzję, którą wykonawca musiałby podjąć sam, a którą dokument zostawia bez odpowiedzi albo rozstrzyga tylko w części, i zaznacza, skąd zna odpowiedź: zapisana (gdzie i jakim zdaniem), widoczna tylko w pliku, który dokument wskazuje jako wzór, albo zgadywana (z odpowiedzią, jaką agent by przyjął). Decyzja liczy się tylko wtedy, gdy wynika ze zdania, które naprawdę stoi w dokumencie albo we wskazanej decyzji, i gdy różne odpowiedzi dają różny, zauważalny wynik w zakresie zadania; lista nie ma obowiązku znaleźć decyzji ani podać liczby, a sprawa, o którą już zapytało sprawdzanie słowa o dwóch znaczeniach albo która stoi już wśród pytań zadania, nie wraca.
- Drugi świeży agent, na tej samej klasie, może czytać repozytorium, które zadanie zmienia. Przy każdym zgadnięciu mówi, czy repozytorium albo dokument już rozstrzyga odpowiedź (z cytatem i ścieżką), czy przyjęta odpowiedź zgadza się z tym, co mówi repozytorium, co by się zmieniło w plikach, które zadanie zmienia, gdyby odpowiedź była inna, i wydaje werdykt: najpewniej trafiona, najpewniej błędna albo naprawdę otwarta. Pisze prostym językiem i nazywa to, czego nie sprawdził.
- Agent doprecyzowania otwiera potem plik, na który wskazuje cytat każdej sprawy, którą by przed Tobą ukrył, i każdej, którą Ci pokaże, i sprawdza cytat słowo w słowo; każdej sprawie daje jeden jawny werdykt, krytyki albo własny. Cytat, który się nie zgadza, unieważnia werdykt krytyki w tej sprawie.
- Widzisz tylko sprawy naprawdę otwarte i luki samego dokumentu (zgadnięcie, które krytyka uznała za najpewniej błędne, jest taką luką), najwyżej około czterech, najważniejsze pierwsze, każdą prostym językiem z drogami, ich kosztem i rekomendacją, razem ze ścieżką pliku w ignorowanym katalogu roboczym produktu, w którym leżą pełna lista, krytyka i werdykty. Gdy żadna sprawa nie jest otwarta, o kroku nie słyszysz nic.
- Twoje odpowiedzi trafiają pod pytania zadania z Twoimi słowami jako źródłem i drogami, których nie wybrałeś, a to, co zmieniają w decyzjach w grze i ustaleniach do zapisania, wchodzi do dokumentu tak jak przy reszcie doprecyzowania.
- W doprecyzowaniu prowadzonym przez orkiestratora projektu agent doprecyzowania nie uruchamia żadnego agenta: zapisuje w swojej turze jedną prośbę o oba kroki; orkiestrator je uruchamia i wpisuje listę oraz krytykę do pliku; agent doprecyzowania, wznowiony, sprawdza cytaty, zapisuje werdykty i wpisuje sprawy otwarte do swojej tury jako materiał dla Ciebie.

### Pod spodem

Zmiana to trzy edycje tekstów skilla doprecyzowania i dwie nowe decyzje w dzienniku fundamentu, po jednej na każdą z Twoich dwóch odpowiedzi o tym kroku; pełna bramka testów przeszła z 1561 testami na końcowym drzewie.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Popraw albo przepuść

1. Poszerzone sprawdzanie cytatów (zob. pozycja 4 niżej) mówi tylko o zgadnięciach „rozstrzygniętych w repozytorium”, a nie o takim, które drugi agent uznał za rozstrzygnięte samym dokumentem zadania, choć drugi agent może rozstrzygać zgadnięcie także tak. Agent doprecyzowania, który trafi na takie zgadnięcie, przeczyta tekst dosłownie i nie otworzy cytatu z dokumentu. Skutek jest mały, bo dokument to tekst, który agent doprecyzowania dopiero co napisał, a cytat łatwo porównać na oko, ale ktoś czytający tekst ściśle mógłby to pominąć. Poprawka kosztuje jedną poprawkę i jeszcze jedną rundę przeglądu (mniej więcej tyle, ile pierwsza runda poprawek tego cyklu) i zmienia jedną frazę w skillu i jedną w decyzji; przepuszczenie zostawia lukę w tekście, a zrobienie z tego zadania zostawia ją do czasu, aż ktoś je wykona. Rekomenduję przepuścić, bo dokument zadania to jedyne źródło, które agent doprecyzowania właśnie napisał i widzi w całości. Poprawić w tym PR-ze, zrobić z tego zadanie, czy przepuścić? (Minor findings, 1)

2. Jedna stara decyzja w fundamencie, o tym, jak przed Twoim wyborem testuje się opcje wyboru technologii, wymienia trzy praktyki testowania (adwokata diabła, pre-mortem i szukanie nieznanych niewiadomych), ale nie mówi, skąd pochodzą, a fundament oznacza to źródło jako jeszcze do znalezienia. Zmiana tej decyzji nie napisała ani nie ruszyła; stoi już na głównej gałęzi. Kto ją czyta, nie wie, skąd te praktyki pochodzą, co ma znaczenie, gdy ktoś je podważy. Wpisanie źródła w tym PR-ze kosztuje osobę, która zna źródło, i jeszcze jedną rundę przeglądu; zrobienie zadania zostawia znacznik na miejscu; przepuszczenie akceptuje lukę na głównej gałęzi. Rekomenduję zrobić z tego zadanie, bo zmiana nie ma nic wspólnego z tą decyzją i nikt nie nazwał źródła. Wpisać źródło w tym PR-ze, zrobić z tego zadanie, czy przepuścić? (Foundation entries, 6)

3. Jedna stara decyzja w fundamencie, o tym, co rozbicie projektu zapisuje w planie, wymienia praktykę (mapę drogową pionowych kawałków), ale nie jej źródło, a fundament oznacza to źródło jako jeszcze do znalezienia. Ona też stoi już na głównej gałęzi i zmiana jej nie ruszyła. Koszt każdej odpowiedzi jest taki jak w poprzedniej pozycji. Rekomenduję zrobić z tego zadanie, z tego samego powodu. Wpisać źródło w tym PR-ze, zrobić z tego zadanie, czy przepuścić? (Foundation entries, 7)

### Akceptujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

4. Cykl poszerzył Twoją odpowiedź o sprawdzaniu cytatów krytyki: agent doprecyzowania otwiera plik, na który wskazuje cytat każdej sprawy, którą by przed Tobą ukrył (zgadnięcie uznane za już rozstrzygnięte w repozytorium albo za najpewniej trafione), a nie tylko tych, które Ci pokazuje. Punkt zadania mówi „przy każdej sprawie, którą pokaże”, ale Twój własny powód z odpowiedzi na drugie pytanie (krytyka może uznać sprawę za rozstrzygniętą, choć pierwszy agent miał rację, wątpiąc) to właśnie przypadek, w którym błędne „rozstrzygnięte” ukryłoby przed Tobą prawdziwą sprawę otwartą, a pierwsza wersja tekstu by go nie chroniła. Przegląd całej zmiany zablokował na tym punkcie. Druga droga, czyli zmiana przykładu w decyzji na sprawę pokazywaną, zachowałaby słowa zadania i zostawiła niepilnowany powód, który sam nazwałeś. Cena to jeden plik więcej do otwarcia na każde zgadnięcie ukryte przed Tobą, najwyżej tyle, ile liczy lista.
5. Zgadnięcie, które krytyka uznaje za najpewniej błędne, jest pokazywane Tobie jako luka dokumentu, a nie pomijane: zadanie mówiło, że widzisz „sprawy otwarte i luki dokumentu”, i nie mówiło, co dzieje się ze zgadnięciem błędnym, a wykonawca przyjąłby błędną odpowiedź. Zgadnięcie najpewniej trafione i zgadnięcie rozstrzygnięte zostają w pliku. Cena to jedna sprawa więcej pokazana w granicy około czterech.
6. Pełna lista, krytyka i werdykty leżą w jednym pliku w ignorowanym katalogu roboczym produktu, nazwanym od zadania, w trzech częściach, i żaden agent kroku go nie pisze: agent doprecyzowania zapisuje to, co każdy zwrócił (a w doprecyzowaniu z orkiestratorem orkiestrator pisze listę i krytykę, a agent doprecyzowania werdykty). Zadanie ustalało tylko „plik w ignorowanym katalogu”. Druga droga, w której każdy agent pisze swoją część, złamałaby zasadę, że tylko agent doprecyzowania pisze pliki zadania, i zwyczaj, że krytyk nie pisze plików. Cena to ręczne przepisanie zwrotów.
7. W doprecyzowaniu prowadzonym przez orkiestratora projektu krok zajmuje dwie tury agenta doprecyzowania (prośba, potem tura ze sprawdzeniem i werdyktami), a sama prośba nazywa metodę, tańszą klasę i to, co dostaje pierwszy agent, bo żaden plik orkiestratora nic nie mówi o tym rodzaju prośby. Druga droga, nowy plik-wskaźnik dla orkiestratora, wykraczała poza Twoje zadanie. Cena to ryzyko, że orkiestrator, który nie pójdzie za słowami prośby, mógłby dać pierwszemu agentowi rozmowę; słowa prośby każą zrobić odwrotnie.
8. Decyzja o przejęciu tej praktyki z kursu mówi w uzasadnieniu, a nie na liście odrzuconych dróg, czego z praktyki nie bierze: liczenia, ile zgadnięć rozstrzygnąłbyś inaczej, i minut spędzonych na przeglądaniu listy, które Twoje notatki zachowują na próbę. Jej odrzucone drogi zawierają tylko trzy drogi, które utrzymują Twoje odpowiedzi, jak pozwala zasada dla decyzji pisanej z Twoich wierszy; czwartą drogę trzeba by wymyślić.

## Koszt

Czas pracy policzony przez skrypt to około 31 minut, a cykl zużył około 20 milionów tokenów, prawie wszystko to wejście z pamięci podręcznej, wszystko na tej samej klasie modelu co orkiestrator: jeden autor, wznowiony dwa razy (do poprawki i do kroku zwrotnego), i jeden recenzent, wznowiony raz. Przegląd całej zmiany raz zablokował; jedna poprawka i jej przegląd przeszły, a krok zwrotny nie znalazł nic do zmiany. Pełna bramka trwała 14 minut 22 sekundy i przeszła. Tabela etapów stoi w zapisie tego cyklu (Course of the cycle, Record). Katalogi wcześniejszych zadań nadal stoją, bo skrypt czyszczący nie umiał rozpoznać, że nie są już potrzebne; nic w tym PR-ze na nie nie czeka, a Ty możesz je usunąć ręcznie (ich nazwy, gałęzie i powody stoją w Checks).

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy.

</details>

## Technical changes

- `project-level/task/skill/final_review.md`: a new opening paragraph and five numbered steps (the list, the critique, the verdicts, the matters shown to the human, the answers) before the paragraph "When the draft is complete, show it whole."; the step names the file `.runs/decisions-list/<task-name>.md` with its three parts *List*, *Critique* and *Verdicts*, and the condition under which the step runs. Commit `51f2590`, changed in `b084a4a` (the quotation check widened, "sections 4 and 5 of `SKILL.md`").
- `project-level/task/skill/orchestrated_mode.md`: one bullet after the one on `find-foundation-entries`: the refining agent starts no agent, writes one *Child-work request* in its turn that names steps 1 and 2 of `final_review.md`, the cheaper class and the first agent's input; the project orchestrator writes *List* and *Critique*; the refining agent, resumed, checks the quotations, writes *Verdicts* and puts the open matters into its turn. Commits `51f2590`, `b084a4a` (the subject of "end your turn", the content of the request).
- `project-level/task/skill/SKILL.md`: one sentence in section 6 that names the step beside the check of the complete document; rewrapped to the file's width in `b084a4a`.
- `foundations/decisions.md`: two new decisions at the end of the section "Task refinement and readiness" (see *Foundation entries*); WAY-377's *Rationale* names in `b084a4a` what the decision leaves out of the course practice.
- The fix commit `b084a4a` (range `51f2590..b084a4a`) answered the one blocking finding and five Minor findings of the review of the whole change; no commit holds a file of the cycle's working directories.

## Checks

- Final gate: `python -B task-cycle/gate_times.py --output .runs/task-cycles/decisions-list-in-refinement/gate_times.md -- python -B gate/run_tests.py`, on `b084a4a` (the final tree; `origin/foundations` fetched and still the base `9cbc6b2`, so no reconciliation), exit 0, 1561 tests in 11 directories, 861.9 s, 2 other gate runs at the same time (counted by the script); every directory passed. Run on the signal `start` of the day's advisor.
- Tests failing before the change: none. The cycle ran no gate on the base: the base is a merge commit whose tree equals that of its second parent, so the list was taken from the final gate (run 2, exit 0, 1561 tests, every directory passed) of the earlier cycle, in the *Verification* of `docs/task-cycles/scripts-after-foundation-review/cycle.md` of commit `c40ed70`.
- `python -B elements/common/foundation_check.py`, without `--skip-test-citations`, on `b084a4a`: exit 0, `0 errors`, no `listed:` line.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 5`, `threshold: 60`, `reminder: no`.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` on the one session of the cycle: both exit 0.
- Focused checks of the author, the fixer and the reviewers, their last runs: `foundation_check.py`, `check_instructions.py` exit 0; `gate/run_tests.py` for `project-level` (278 tests), `elements/common` (242), `agent-instructions` (27) and `instruction-files` (104, 5 skipped, POSIX-only) exit 0. No test of behaviour exists for the prose of skills, so none was written, and no invariant test or line `decision:` was added or changed.
- Own-work checks: the author's (reading of the new text against the task item by item, in `reports/author-report.md`), the fixer's (the skill, the orchestrated bullet and the decision read side by side, `reports/author-fix-report.md`) and the return step's (`reports/author-return-step-report.md`) were reading checks, not runs. One run of a reviewer's `decision_index.py` in the review of the fix failed with exit 2 because the reviewer had removed its own directory; it was not repeated, since `foundation_check.py` parses both entries.
- The review of the whole change read the index of its whole selection and 11 decisions whole; of the rest, 63 were listed in full and 62 by heading alone, and the reviewer named none of those it did not open whole as bearing on the change.
- Form check, check of private paths on this description, and the three checks on the copy of the record: to be filled with the record's link.
- Working copies left: none. Directories of earlier tasks kept by the cleaning script (name · branch · reason): `agent-path-to-running-product` · `task/agent-path-to-running-product` · the branch has no merge git can see on origin/foundations; `ci-on-merge-requests` · `task/ci-on-merge-requests` · uncommitted changes, and no merge git can see on origin/foundations; `base-check-stage-remarks` · detached · the branch `task/stage-remarks` its name gives is not found; `base-fix-minor-findings` · detached · the branch `task/minor-findings` its name gives is not found.

## Foundation entries

- WAY-377 (`row 1`) — "Does the refinement of a task list the decisions its document leaves to the executor before the human sees the document, and who lists them?": before the complete document is shown, two fresh agents of one cheaper class (named in general terms) list the decisions it leaves to the executor and settle the guesses against the repository, where the task has decisions in play or changes a skill or an instruction file.
- WAY-378 (`row 2`) — "What does the human see after the decisions a task document leaves to the executor are listed and criticised?": the human sees only the open matters and the gaps of the document, at most about four, each with ways, cost and a recommendation; the full list and critique stay in a file, and the refining agent checks the critique's quotations, behind the matters shown and behind the guesses kept from the human, and gives each one verdict.
- No new topical section of the decision log; no invariant, surface or *Violated* mark was changed; no kept row tied to an entry already stated; no guidelines rule with no decision.
- Gaps standing in the foundation, not written or touched by this change (the top part's items 2 and 3): WAY-138's *Based on* reads `TODO` (the source of the three testing practices) and WAY-142's *Based on* reads `TODO` (the source of the roadmap of vertical slices).

## Minor findings

1. **N1** (fix review, `reports/review-fix-1-report.md`; `project-level/task/skill/final_review.md:29-30` and the binding sentence of WAY-378): "The widened check names 'settled in the repository' only. ... though step 2 of the same file lets the critique settle by 'the repository or the document' and quote it. A guess kept from the human on a quotation of the document is checked by neither text. The effect is small ... Fix: 'settled in the repository or in the document'. Graded Minor: no entry or example is contradicted, the case is a narrowing of the check, and the original defect (an example that could not happen) is gone."

The five Minor findings of the review of the whole change (M1 to M5) were fixed in `b084a4a` and found fixed by its review.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task "the refinement of a task ends in a list of the decisions the document leaves to the executor, checked by a critique — the human sees only open matters", an independent task accepted on 2026-11-14 (the author's note, commit `1a64a1b2` of the author's vault); sources: the task's own questions and the decisions it names (WAY-374, WAY-120, WAY-113, WAY-229, WAY-100, WAY-134, WAY-124, WAY-154), the foundation at `9cbc6b2`.
- **Process pin:** not applicable; the repository is the-way itself and its checkout is the process.
- **Spec:** none; the task left no open design choice.
- **Route:** one author without a plan, on the same class of model as the orchestrator's (not the default cheaper one): the text is normative wording that later agents follow and two decisions with a rationale. The author was resumed for the fix and for the return step.
- **Plan:** none.
- **Choices:** 4 rows in the questions table of the record (the author's class; the widening of the quotation check; the reading gaps of the whole-change reviewer and of the return step judged immaterial), and 8 choices in the author's report, of which those that reach you are items 5 to 8 of "You accept by merging" above; see the questions table in the record.
- **Blocking findings left:** none.
- **Record:** to be filled with the link by the SHA of the commit that adds the record.
