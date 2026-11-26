**State: draft** — the code is finished and reviewed; the request is marked ready once the CI run on its last head has passed

## What you will see

Two things change in how a task cycle works.

First, the review of a whole change no longer depends on the cycle's leader guessing which models the session allows. Before the first piece of work for the strongest model, the leader asks a small agent to work on the model it means to use — the one named when the cycle was started, or else the strongest the tool offers — and reads from the session's own record which model that agent really worked on. If the tool quietly gave another model, the leader tries the next one down. All strongest-model work in that session then goes on the model found, and a correction after review starts its own trial. The record of the cycle lists each trial and its result, and gives for every agent the model it actually worked on, with both models where they differ. Until now a cycle started with a limited list of models could run its review on a weaker model, and the record named the model that was asked for, so you learned it only if you noticed.

Second, the list of tests that "may fail" between the pieces of a plan is gone. A piece that finds a test failing runs that test on the state before its own change: a test that fails there too is not its fault, one that passed there and fails now is its fault. The exception is a test the piece itself announced, in its own goal, that it would leave failing for a named later piece to repair. The plan has to put such a test among the checks of the piece that repairs it, and if the test still fails after that piece, the piece has failed its check although the test was red before. The leader no longer builds a list for each piece, so it cannot be wrong or stale.

### Underneath

The change is text only: two decisions rewritten, and seven files of the cycle's instructions and the record's template. No code and no test changed.

## For you to decide

### Needed from you

none

### Fix or let through

1. The new rule for choosing the strongest model also rests on what the tool's documentation says happens when a model is not allowed: the tool quietly gives the agent the session's own model. The cycle did not write that source down as a fact of the foundation, because the form for such a fact asks for the passage word for word and an archived copy of the page, and the cycle was not allowed to fetch an archive. The rule states the same thing as something seen in this product's own cycles. If the documentation changes, a reader of the rule would not learn where to look. Writing the fact in this request costs a session that fetches the archived copy and a round of review; undoing it, nothing. Making a task of it leaves the gap until someone picks it up; undoing it, nothing. Letting it through accepts the gap; undoing it later costs that task. I recommend letting it through, since the trial catches a substitution whatever the documentation says. Its weak point: the documentation is the only place that says why the tool behaves so, and no entry points to it. Write the fact in this request, make a task of it, or let it through? (Foundation entries, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The trial runs again in every new session of the leader, a correction after review included, and not once for the whole cycle. The task says "in every cycle"; the review found that a correction started with another list of models could otherwise take the model an earlier session found and run its review on a weaker one with nobody noticing. The price is one more small agent call, a few tens of thousands of tokens, per session. The cycle did not take the shorter way, a model carried over from the record, since the task rejects taking a model on faith.
3. A model of the same family as the one asked for counts as the model asked for, an older version included; only a model of another family counts as a substitution that sends the trial one model down. The tool's documentation says that a name it may not give goes to the newest allowed version of the same family, and treating that as a substitution would push reviews down a whole family for no reason. The price: an older version of the strongest family may be a little weaker than the newest, and the record shows which one worked.
4. The leader's check of a plan now also looks that a test the plan says a piece leaves failing stands among the checks of the piece that repairs it. The task puts that duty on the planner; the cycle added the look so that a forgotten entry is found before the first piece is made and not at the end. It costs one clause in the check. The cycle did not leave the duty unchecked, because the task's own answer says the missing entry would otherwise show only after all pieces.

## Cost

The cycle's working time was 46 minutes so far, 26 of them waiting for tools. One author on Claude Sonnet 5.5 made the change, one fix and the return step, which changed nothing. The review of the whole change and the review of its fix ran on Claude Opus 5.5, as asked, which the table of stages confirms. The first review failed with two blocking remarks and four Minor remarks; one fix closed all six, and the review of the fix passed. This cycle ran under the rule that stood before the change, so it made no trial of the model; it took Opus on the word of the start command and checked it in the table afterwards. The product's tests ran only in CI. Tokens in all so far: 33.0 million (24.7 million on Claude Sonnet 5.5, 8.3 million on Claude Opus 5.5). Table of stages: RECORD_LINK/stages.md.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing else waits for you.

<details>
<summary>Po polsku</summary>

**Stan: wersja robocza** — kod jest skończony i przejrzany; prośba zostanie oznaczona jako gotowa, gdy przejdzie przebieg CI na jej ostatnim stanie

## Co zobaczysz

Zmieniają się dwie rzeczy w pracy cyklu zadania.

Po pierwsze, przegląd całej zmiany nie zależy już od tego, że prowadzący cykl zgaduje, jakie modele dopuszcza sesja. Przed pierwszą pracą dla najmocniejszego modelu prowadzący zleca małemu agentowi pracę na modelu, którego chce użyć — podanym przy starcie cyklu albo, bez niego, najmocniejszym, jaki oferuje narzędzie — i z zapisu sesji odczytuje, na którym modelu ten agent faktycznie pracował. Jeśli narzędzie po cichu dało inny model, prowadzący próbuje następnego w dół. Cała praca najmocniejszej klasy w tej sesji idzie potem na ustalony model, a poprawka po przeglądzie robi własną próbę. Zapis cyklu podaje każdą próbę i jej wynik oraz przy każdym agencie model, na którym faktycznie pracował, a gdzie się różni od zleconego — oba. Dotąd cykl uruchomiony z ograniczoną listą modeli mógł puścić przegląd na słabszym modelu, a zapis podawał model, o który prosiono, więc dowiadywałeś się o tym tylko wtedy, gdy sam zauważyłeś.

Po drugie, znika lista testów, które „mają prawo” padać między kawałkami planu. Kawałek, który zastaje padający test, uruchamia ten test na stanie sprzed własnej zmiany: test padający tam także nie jest jego błędem, test, który tam przechodził, a teraz pada, jest jego błędem. Wyjątek to test, który kawałek sam zapowiedział w swoim celu, że zostawi go padającym, dla wskazanego późniejszego kawałka, który go naprawi. Plan musi wpisać taki test do sprawdzeń kawałka naprawiającego, a jeśli test dalej pada po tym kawałku, kawałek nie przeszedł swojego sprawdzenia, choć test był czerwony już wcześniej. Prowadzący nie układa już listy dla każdego kawałka, więc lista nie może być błędna ani nieaktualna.

### Pod spodem

Zmiana to sam tekst: przepisane dwie decyzje i siedem plików z instrukcjami cyklu oraz szablon zapisu cyklu. Żaden kod ani test się nie zmienił.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawy albo przepuszczenia

1. Nowa reguła wyboru najmocniejszego modelu opiera się także na tym, co dokumentacja narzędzia mówi o modelu, który nie jest dozwolony: narzędzie po cichu daje agentowi model samej sesji. Cykl nie zapisał tego źródła jako faktu fundamentu, bo formularz takiego faktu żąda dosłownego fragmentu i archiwalnej kopii strony, a cykl nie mógł pobierać archiwum. Reguła podaje to samo jako obserwację z cykli tego produktu. Gdyby dokumentacja się zmieniła, czytelnik reguły nie dowiedziałby się, gdzie szukać. Zapisanie faktu w tej prośbie kosztuje sesję pobierającą archiwalną kopię i rundę przeglądu; cofnięcie — nic. Zrobienie z tego zadania zostawia lukę, aż ktoś je podejmie; cofnięcie — nic. Przepuszczenie przyjmuje lukę; cofnięcie później kosztuje to zadanie. Polecam przepuścić, bo próba wyłapie zastępstwo niezależnie od dokumentacji. Słaby punkt: dokumentacja jest jedynym miejscem, które mówi, dlaczego narzędzie tak się zachowuje, i żaden wpis do niej nie odsyła. Zapisać fakt w tej prośbie, zrobić z tego zadanie czy przepuścić? (Foundation entries, 1)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te punkty; jeśli któryś Ci nie odpowiada, napisz który.

2. Próba biegnie od nowa w każdej nowej sesji prowadzącego, także w poprawce po przeglądzie, a nie raz na cały cykl. Zadanie mówi „w każdym cyklu”; przegląd stwierdził, że poprawka uruchomiona z inną listą modeli mogłaby inaczej wziąć model ustalony przez wcześniejszą sesję i puścić przegląd na słabszym, a nikt by nie zauważył. Cena to jedno dodatkowe wywołanie małego agenta, kilkadziesiąt tysięcy tokenów na sesję. Cykl nie poszedł krótszą drogą, modelem przeniesionym z zapisu, bo zadanie odrzuca branie modelu na wiarę.
3. Model tej samej rodziny co ten, o który prosiono, liczy się jako model, o który prosiono, także starsza wersja; zastępstwem, które przesuwa próbę o jeden model w dół, jest dopiero model innej rodziny. Dokumentacja narzędzia mówi, że nazwa, której narzędzie nie może dać, trafia na najnowszą dozwoloną wersję tej samej rodziny, a uznanie tego za zastępstwo zepchnęłoby przeglądy o całą rodzinę bez potrzeby. Cena: starsza wersja najmocniejszej rodziny może być trochę słabsza od najnowszej, a zapis pokazuje, która pracowała.
4. Sprawdzenie planu przez prowadzącego pilnuje teraz także, żeby test, który według planu kawałek zostawia padający, stał wśród sprawdzeń kawałka, który go naprawia. Zadanie nakłada ten obowiązek na planistę; cykl dodał sprawdzenie, żeby zapomniany wpis wyszedł przed zrobieniem pierwszego kawałka, a nie na końcu. Kosztuje to jedno zdanie w sprawdzeniu. Cykl nie zostawił obowiązku bez kontroli, bo odpowiedź zadania mówi, że brak wpisu wyszedłby inaczej dopiero po wszystkich kawałkach.

## Koszt

Czas pracy cyklu to dotąd 46 minut, z czego 26 czekania na narzędzia. Jeden autor na Claude Sonnet 5.5 zrobił zmianę, jedną poprawkę i krok powrotu, który niczego nie zmienił. Przegląd całej zmiany i przegląd jego poprawki poszły na Claude Opus 5.5, jak zlecono, co potwierdza tabela etapów. Pierwszy przegląd odrzucił zmianę z dwiema uwagami blokującymi i czterema drobnymi; jedna poprawka zamknęła wszystkie sześć, a przegląd poprawki przeszedł. Ten cykl szedł według reguły sprzed zmiany, więc nie zrobił próby modelu; wziął Opusa na słowo z polecenia startowego i sprawdził go potem w tabeli. Testy produktu poszły tylko w CI. Tokeny dotąd: 33,0 mln (24,7 mln na Claude Sonnet 5.5, 8,3 mln na Claude Opus 5.5). Tabela etapów: RECORD_LINK/stages.md.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo tylko wtedy zostaje działający link do zapisu cyklu. Nic więcej nie czeka na Ciebie.

</details>

## Technical changes

The request changes nine files, in three groups, in one commit of the author and one fix commit.

1. Two decisions in place. The decision on the class of model of the author and the executor now fixes the strongest class by a trial in every cycle and again in every later session of the orchestrator (`foundations/decisions.md`, WAY-229: binding sentences, *Verification*, *Rationale*, *Rejected*, and a new relation to WAY-227). The decision on when a task needs a plan now carries the base measure of a slice's failing test, its two exceptions and the announced test in the repairing slice's *Checks*, in a new third paragraph moved out of the first, which was near the word limit (WAY-136: binding sentences, *Verification*, *Rationale*, *Rejected*). `git diff` of the file: +102 −33.
2. The cycle's skill and its files. `task-cycle/skill/SKILL.md` gets a paragraph before step 9 with the procedure of the trial (small agent with the description `model probe <n>`, the row of its table in `task-cycle/cycle_stages.py` output, the family rule, the next model down, the tries written under *Strongest class* of the record), the three places of the rule now say "the model the probe fixed", step 9 sub-steps 2 to 4 no longer carry a list of failing tests and use the base measure, and step 12 sets the models in the record from `stages.md`, here and in each stop that runs the script (`task-cycle/skill/blocked_finding.md`, `task-cycle/skill/reserved_return.md`). `task-cycle/change/slice.md` gets the section "A failing test"; `task-cycle/change/SKILL.md` names it in its table; `task-cycle/plan/SKILL.md` and `task-cycle/skill/planning.md` carry the planner's rule and the orchestrator's check.
3. The record template (`task-cycle/record_template.md`): the model the agent worked on in *Author*, in the *Slices* column and in the *Events* actor, and a new item *Strongest class*.

The fix (`15bf941a`) closed the two blocking remarks and the four Minor remarks of the review of the whole change: the trial in every session (a correction's included), the exception narrowed to the announced test the slice's own *Checks* hold, the row of the probe's agent where the tool does not name it, the family rule, one word of the planner's sentence and one of the decision's *Verification*, and the models of the stops that run the script. Nothing was reverted.

## Checks

1. Final gate: the CI run on this request's last head, which is the final gate; the cycle ran no full gate on its own system. Its result: pending, to be written here when the run ends.
2. Failing before the change: none. The base `b502011f` is a merge commit with the tree of its second parent (`dca0a541a53148179c33920e268c3e0b339af185` both), so no gate ran on the base; the list was taken from the *Checks* of the merged request https://github.com/mariusznazar/the-way/pull/160 (the CI run https://github.com/mariusznazar/the-way/actions/runs/45691891142 on `7af4c81b`, first attempt: `tests` and `tests-windows` passed; its item 2 names none failing before) and from `docs/task-cycles/recommendation-not-below-goal/cycle.md` at `9b94b3f4`.
3. The author's focused checks on each head it made (`60561fba`, `15bf941a`): `python -B elements/common/foundation_check.py` exit 0, `0 errors`; `python -B instruction-files/check_instructions.py .` exit 0, 0 error, 0 warn; `python -B gate/run_tests.py task-cycle` exit 0 (570 tests, 2 skipped on Windows), `project-level` exit 0 (302 tests), `elements/common` exit 0 (316 tests), `process-audit` exit 0 on the first head. The orchestrator ran `python -B elements/common/foundation_check.py` without `--skip-test-citations` on `15bf941a`: exit 0, `0 errors`, no `listed:` line.
4. The reviewers' own runs: the review of the whole change (Claude Opus 5.5, `FAIL 60561fba`) ran the foundation check (exit 0), the instruction check (exit 0), `python -B task-cycle/change_file_sizes.py` (exit 0), `python -B -m unittest agent-instructions/test_size_invariant.py` (exit 0, 4 tests), `python -B gate/run_tests.py task-cycle` (exit 0, 570 tests) and a search of tracked files for the old wording (only the new text); it read 4 decisions whole and the index of its whole selection (21 in full, 104 by heading). The review of the fix (same reviewer, `PASS 15bf941a`) ran the foundation check, the instruction check, the `task-cycle` tests and the same search, all exit 0, and read the two changed decisions again.
5. Own-work checks: the author named the requirement likeliest not met (that the orchestrator can read the model a probe agent worked on from the session record, so that the rule does not rest on a tool behaviour that does not exist) and checked it by running `python -B task-cycle/cycle_stages.py` on its own live session, whose table gave `claude-sonnet-5-5` in the column *Subagent model* for its row; for the fix, that the narrower exception stands in every place, checked by a search of all tracked files for the old wording (none left).
6. Walk through the running product (WAY-406): the change alters no behaviour a user sees in a running product — it is prose of the process, two decisions and a record template — so no walk and no case marked unchecked stand for it.
7. Not run: the trial of the model itself has never run, since this cycle ran under the rule before the change; the first cycle after the merge is its first run, and its record will show the tries. The return step ran and changed nothing (no review of it). The reconciliation with the target branch found nothing to merge, since `origin/foundations` stayed at the base `b502011f`. `skill_entry_points.py --write` was not needed: no skill's description or name changed.
8. The form check of this description: pending.
9. The remarks check on the original: `python -B task-cycle/remarks_check.py .runs/task-cycles/strongest-model-probe-and-slice-base-measure` run 1 exit 1 (2 items listed, appended word for word), run 2 exit 0. The three checks on the copy of the record: pending.
10. The count of merges since the last review of the foundation: `python -B task-cycle/review_reminder.py origin/foundations` exit 0, `merges: 34`, `threshold: 60`, `reminder: no`.
11. Working copies left: none; directories of earlier tasks kept: none.

## Foundation entries

- WAY-229 — `row 1`: the strongest class of model is not read from a list of allowed models but fixed in every cycle, and again in every later session of its orchestrator, by a trial: a small agent is asked for the candidate model (the one named at the start, else the strongest the tool offers), the model it really worked on is read from the session record, the next model down is tried on a substitution, a model of the candidate's family counts as the candidate, and every dispatch of the class then runs on the model fixed; the record gives the tries and the human is asked nothing. The entry also gains the relation `derives from` WAY-227, a link that does not make it `the cycle's`.
- WAY-136 — `row 2` and `row 3`: a slice's executor decides whether a failing test is its slice's fault by running the tests that failed for it on the slice's base: a test failing there too is no fault of the slice, one that passes there and fails after is, except a test the slice's own *Goal* announces it leaves failing for a named later slice; an announced test also stands in the *Checks* of the slice that repairs it, and its failure after that slice is that slice's failed check though it failed on its base too; the report gives the base result of each such test.
- No invariant was added, changed or marked violated; no invariant test and no line `decision:` of a test changed (no test cites either decision); no glossary term, no environment fact and no part-map entry; no projected entry.

## Minor findings

none

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task; its need is that the review of a whole change and of the return step runs on the strongest model the session allows, also when the cycle starts on a weaker one, and that a slice's executor decides a failing test by a measure on its base instead of a list from the plan; sources: the task document with its three answered questions (accepted 2026-11-26), `foundations/decisions.md` at `b502011f`.
- **Process pin:** none, the-way is the repository itself.
- **Spec:** none: the task's answers settle the design; what was left was how to make what they settle.
- **Route:** one author without a plan, since the five points of the task depend on each other and one agent can hold them; the author on class `same` as the orchestrator, Claude Sonnet 5.5.
- **Plan:** none.
- **Choices:** 3 other choices of the cycle, the items 2 to 4 of *You accept by merging* (rows Q3 to Q5 of the questions table of the record: RECORD_LINK/cycle.md); besides them two rulings that bind nobody after the merge, Q1 (Opus taken on the word of the start command) and Q2 (the author's unread reading carried to the reviewer).
- **Blocking findings left:** none.
- **Record:** RECORD_LINK/cycle.md
