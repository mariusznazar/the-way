# Foundation entries — task `testing-guidelines`

## Turn 1 — WAY-231 to WAY-243 and their facts

**Status:** `done with concerns` (concerns C-1 to C-4 below; none blocks turn 2).

### Files and commits

- `foundations/decisions.md` — +524 / −0: WAY-231 … WAY-243 appended after WAY-230, before
  `## Withdrawn identifiers`, in the plan's order.
- `foundations/environment_facts.md` — +12 / −0: `llm-test-oracle-actual-behaviour`,
  `computer-use-agent-web-testing`, after `agent-run-variance`.
- Commit `4f207dd` "Record the decisions of the testing discipline's rules (WAY-231 to WAY-243) and
  the facts they rest on", author e-mail `mariusznn@gmail.com` (checked with `git log -1`). Base
  `4302f72`. Nothing outside `foundations/` changed. No push.

### Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (at `4f207dd`) | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` (at `4f207dd`) | 0 | 109 tests, OK |
| scratch script comparing every quoted passage of the new entries with the source text fetched from its address (whitespace collapsed, markup dropped; not committed) | — | 30 of 30 passages found word for word |

No element skill names a further check. No test was written (no code; `make-change` §2 does not
apply to foundation prose).

### Entries and their meaning (Polish, for the request, WAY-114)

| Entry | Row | Meaning |
|---|---|---|
| WAY-231 | 1, 15 | Testy są osobną dyscypliną wytycznych produktu: the way daje szablon dyscypliny testów, z którego produkt pisze `guidelines/testing.md`, i skill `maintain-testing-guidelines`, który ten plik tworzy i utrzymuje; rodzaj kodu w wytycznych kodowania to kod produktu poza testami, a wzorce testów stoją w przewodniku testów przy swoim poziomie. |
| WAY-232 | 2 | Szablon testów wymaga, żeby oczekiwana wartość każdego testu pochodziła z niezależnego źródła — dokumentu produktu wskazanego w przewodniku, relacji, której nie liczy kod pod testem, awarii liczonej jako błąd albo oceny człowieka — nigdy z dzisiejszego wyniku kodu, także dla snapshotów i testów charakteryzujących; gdy źródła nie widać z nazwy testu, wskazuje je komentarz, a recenzent pyta przy każdej asercji „skąd ta wartość”. |
| WAY-233 | 3 | Szablon testów wymaga, żeby zmiana oczekiwanej wartości, usunięcie, osłabienie asercji, pominięcie i wyłączenie istniejącego testu były jedną kategorią zmian, każda z przyczyną po stronie danych albo wymagania i odnośnikiem do dowodu, inaczej recenzent czyta ją jak maskowanie defektu; reguła wymienia sposoby osłabiania testu. |
| WAY-234 | 4 | Szablon testów wymaga, żeby asercje sprawdzały zachowanie wymagane przez regułę albo zadanie, a szczegół wykonania nie był warunkiem zaliczenia; recenzent pyta, czy kod da się zmienić tak, że zachowanie zostaje, a asercja pęka; sprawdzenie przygotowania przypadku wolno, gdy stoi przed działaniem, jest oznaczone jako warunek wstępny i sprawdza cechę przypadku nazwaną w wymaganiu. |
| WAY-235 | 5 | Szablon testów wymaga, a skill testów proponuje, dla każdej granicy zaufania z mapy części co najmniej jeden niezmiennik odmowy ze stałym testem, który sprawdza odmowę wprost, bierze ją z decyzji o uprawnieniach i jest widziany raz czerwony; granica, która dziś nie odmawia, ma niezmiennik oznaczony jako naruszony, granica będąca wyłącznie konfiguracją cudzej usługi zostaje przy przeglądzie, a dla autoryzacji reguła przewodnika trzyma tabelę kto × zasób × akcja → wynik z decyzją przy każdym wierszu. |
| WAY-236 | 6 | Szablon testów wymaga, żeby AI nie było poziomem testu: test napisany przez AI podlega wszystkim regułom, agent eksplorujący znajduje przypadki, które stają się zwykłymi testami, narzędzie samonaprawiające zmienia tylko sposób znajdowania elementu, sędzia AI wchodzi do stałych testów tylko pod czterema warunkami, a zachowanie każdego narzędzia AI produktu stoi w fakcie środowiska z wersją i datą odczytu. |
| WAY-237 | 7 | Szablon testów wymaga sekcji `## Not tested on purpose`, w której każda pozycja to kategoria zachowania albo kodu z decyzją produktu niosącą warunek powrotu w zdaniach wiążących i powód w uzasadnieniu; `none`, gdy nic nie wyłączono; granica zaufania nigdy. |
| WAY-238 | 8 | Szablon testów wymaga, żeby test stał na najniższym poziomie, na którym nazwane zepsucie da czerwony wynik, chyba że zejście niżej wymagałoby zaślepienia dokładnie tego, co może się zepsuć, bez proporcji poziomów; wybór robi autor zmiany w cyklu, nazywając zepsucie, recenzent sprawdza go wobec przewodnika, a doprecyzowanie zadania nie trzyma planu testów. |
| WAY-239 | 9 | Szablon testów wymaga, żeby błąd złapany dopiero przez test wysokiego poziomu albo przez człowieka dostał też test na najniższym poziomie, który go łapie. |
| WAY-240 | 10 | Szablon testów wymaga, żeby przewodnik nazywał poziomy testów produktu, każdy z decyzją, żeby nazwa poziomu znacząca w produkcie co innego niż w branży była wpisem słownika produktu zdefiniowanym po zasobach, których test wolno dotknąć, i żeby przy każdej części stało zdanie, czy jej złożoność mieszka w obliczeniach, czy w połączeniach. |
| WAY-241 | 11 | Szablon testów daje każdemu poziomowi przepis o tych samych polach; pole wiążące wskazuje decyzję produktu, pole bez decyzji jest przykładem, pole może brzmieć „as in <level>”; pole polecenia podaje bramkę i jej zawężenie albo `none`, limit czasu odsyła do pliku konfiguracji, a przepis nie wypisuje osobnych poleceń narzędzia testów. |
| WAY-242 | 12, C4 | Test wzorcowy poziomu wyznacza decyzja produktu, jak wzorzec rodzaju kodu: gdzie poziom ma testy, skill testów porównuje je i proponuje wzorzec; gdzie nie ma żadnego, wyznacza go zadanie, które pisze pierwszy test poziomu, zatwierdzone w doprecyzowaniu; do wyznaczenia pole stoi puste, a wskazanie innego testu to zmiana tej decyzji. |
| WAY-243 | 13 | Szablon testów wymaga, żeby ponowne uruchomienie testu niestabilnego służyło tylko diagnozie, nigdy zazielenieniu bramki, a wyłączenie albo usunięcie takiego testu było zmianą istniejącego testu z WAY-233. |
| `llm-test-oracle-actual-behaviour` (fact) | for WAY-232 | W kontrolowanym eksperymencie Konstantinou i in. z GPT-3.5 Turbo na wyroczniach testów 24 otwartych repozytoriów Javy generowanie testów przez LLM ma skłonność do wyroczni oddających faktyczne zachowanie programu zamiast oczekiwanego. |
| `computer-use-agent-web-testing` (fact) | for WAY-236 | W WebTestBench żaden z modeli ocenianych przez autorów w ramie WebTester nie przekracza F1 30% w automatycznym testowaniu aplikacji webowych od końca do końca. |

Row 25 (ruling C3), carried in turn 1 as the spec's D9 gives it:

- OWASP (refusal tests as a required check) → *Based on* of WAY-235.
- Google, ch. 12 (a test changes only with its requirement) → *Based on* of WAY-233 (and WAY-234).
- Google, ch. 13 (a real dependency before a double) → *Based on* of WAY-241.
- Google, ch. 11 (re-running only delays the fix) → *Based on* of WAY-243.
- Open Mercato (the list of weakenings) → *Based on* of WAY-233.
- Anthropic (deterministic graders before an AI judge) → *Based on* of WAY-236.
- Limen (tests without value) → named with address and passages in WAY-237's *Rationale*.
- 10xDevs (a section of what is deliberately not tested) → described in WAY-237's *Rationale*,
  no pointer (WAY-27).
- Left out: plan of tests, map of risks and proportions → *Rejected* of WAY-238; the red replacement
  of an old test → *Rejected* of WAY-233; quarantine (and automatic re-runs) → *Rejected* of WAY-243.

### Quotations — address and date read (all read 2026-10-25)

Every passage was fetched from the address below and compared word for word by script (30/30).
Pages without editions cite their closest existing archived copy, found through the CDX index of
captures (none made for the entry).

| Entry | Source and address | Place |
|---|---|---|
| WAY-233, WAY-234 | SWE@Google ch. 12, `https://raw.githubusercontent.com/abseil/abseil.github.io/e9e24835cb889fe25251cb9ec6d51b79233e358d/resources/swe-book/html/ch12.html` (the site's repository at its last commit touching the book) | Strive for Unchanging Tests (Bug fixes; Behavior changes); Test State, Not Interactions |
| WAY-241 | SWE@Google ch. 13, same commit, `…/ch13.html` | How to Decide When to Use a Real Implementation; TL;DRs; Prefer to perform interaction testing only for state-changing functions |
| WAY-243 | SWE@Google ch. 11, same commit, `…/ch11.html` | Case Study: Flaky Tests Are Expensive |
| WAY-233 | Open Mercato skills, `https://raw.githubusercontent.com/open-mercato/skills/e320bd5e3f0761a6d7249085c42c77a4b37d480d/skills/om-code-review/references/review-checklist.md` | § 4. Tests, line 106 |
| WAY-233 | ImpossibleBench — existing fact `impossiblebench-test-modification`, by identifier | — |
| WAY-235 | OWASP Authorization Regression Testing Cheat Sheet, `https://raw.githubusercontent.com/OWASP/CheatSheetSeries/cefb3e95ae33162bac8339ed15a265ed738aaf1a/cheatsheets/Authorization_Regression_Testing_Cheat_Sheet.md` (the repository's last commit of that file, 2026-10-04) | Introduction; Define the Access Policy Model; CI/CD Gating and SDLC Integration |
| WAY-236 | Anthropic, *Demystifying evals for AI agents*, `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents`, archived `http://web.archive.org/web/20261017091633/…` (2026-10-17) | Step 5: Design graders thoughtfully |
| WAY-237 | ISTQB CTFL v4.0.1, `https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf` | 1.3. Testing Principles; 5.2.4. Product Risk Control |
| WAY-237 (*Rationale*) | Limen, `https://raw.githubusercontent.com/overment/limen/89ef3786a6c2f893b2d31cd9944ad76c483f7841/spec/features/done/2026-10/F776-trim-low-signal-tests/notes.md` (repository public: `github.com/overment/limen` answers 200 unauthenticated) | What was cut |
| WAY-238, WAY-239 | Vocke, *The Practical Test Pyramid*, `https://martinfowler.com/articles/practical-test-pyramid.html`, archived `http://web.archive.org/web/20261014080941/…` (2026-10-14) | Avoid Test Duplication |
| WAY-238 | Microsoft Learn, *Shift testing left with unit tests*, `https://learn.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable`, archived `http://web.archive.org/web/20260521141733/…` (2026-05-21) | Write tests at the lowest possible level |
| fact `llm-test-oracle-actual-behaviour` | Konstantinou et al., `https://arxiv.org/abs/2410.21136v1` and `https://arxiv.org/html/2410.21136v1` | Abstract; III-A Research Questions (the model measured: GPT 3.5-turbo) |
| fact `computer-use-agent-web-testing` | WebTestBench, `https://arxiv.org/abs/2603.25226v1` and `https://arxiv.org/html/2603.25226v1` | Abstract; 4.1 Settings (models measured); 4.2 Main Results |

Of the spec's "Quotations" table, only Hypothesis and Goldstein et al. are not read here: they
belong to WAY-228, turn 2.

### Search of the whole foundation (WAY-33) — findings and what I corrected

Searched the decision log, invariants, facts, glossary and part map for the questions of the new
entries and for: flaky/quarantine, snapshot, expected value, refusal, test level, exemplar, test
plan, trust boundary, `WAY-228`, `WAY-212`, `WAY-167`, and each glossary term the new text uses.

- **Glossary term used in another meaning, corrected in the entries:** "standing check" (a check a
  tool makes of every change, such as a linter) — my draft of WAY-236 said an exploring agent's run
  "is no standing check", and several entries said "standing test"; all now say "permanent test".
  "entry" (text of a foundation file) — WAY-237 used it for the items of the guidelines' section;
  now "item". "element" (division of a foundation) — WAY-236 said a healing tool fixes "how the test
  finds an element"; now "how the test finds what it acts on".
- **`exemplar`:** WAY-231 and WAY-242 use "exemplar test" of a level, which the glossary's current
  definition ("later code of its kind") does not cover once WAY-231 takes tests out of the kinds of
  code. Not corrected here: the plan gives the widening of `exemplar` to turn 2 (spec D1).
- **WAY-228:** its *Rationale* says the rule stands in the coding guidelines, read before changing
  "the product's code, tests included (WAY-212)", which WAY-231 no longer bears out. Not corrected
  here: WAY-228 is edited in place in turn 2 (row 14, D4).
- **No question found already answered:** no decision holds the question of any of WAY-231–243.
  Neighbours read whole and found consistent: WAY-03 (an invariant test may change; WAY-233 adds a
  cause and evidence for any test), WAY-08 and WAY-51 (taken over by WAY-235), WAY-48, WAY-68 (same
  answer for an invariant's flaky test; WAY-243 derives from it), WAY-16 (WAY-241), WAY-24
  (WAY-237, see C-2), WAY-77 (WAY-236, see C-3), WAY-168 (WAY-235, see C-1), WAY-198–200 (WAY-242),
  WAY-226 (WAY-240).
- **Waiting entries:** nothing in the foundation waits for this change.
- Invariants and part map: no entry touched (spec *Part map and invariants*).

### Own-work check (make-change §3)

- Requirement most likely unmet: "every quotation an entry carries is copied from the source at a
  fixed address, never from the research notes" (spec *Constraints*, "Quotations"). Check: a script
  extracts each `§ <place> — "<passage>"` of the new decisions and facts, maps it to the source
  fetched from that address (HTML reduced to reader text, Markdown with markup dropped, the PDF
  through `pdftotext`) and tests word-for-word containment. Result: 30 of 30 found. One passage of
  the research differed from the page and was not used as given there: the OWASP "200 OK is never
  acceptable" line, which the research marks as a paraphrase.
- Second check: each binding sentence holds one to three sentences, no "should"/"will" outside
  quotations, *Rationale* names no file path or count of my own (the Limen address is a quoted
  source). Checked by reading and by grep; two "should"/"will" in my prose rewritten.

### Reaches beyond the handoff

- `foundations/decisions.md` WAY-03, WAY-12, WAY-24, WAY-25, WAY-26, WAY-68, WAY-77/WAY-80/WAY-85,
  WAY-90, WAY-95–WAY-100, WAY-120, WAY-122, WAY-176–WAY-192, WAY-201–WAY-202, WAY-208–WAY-212,
  WAY-216, WAY-217, WAY-219–WAY-230 — read whole for the search of WAY-33 and as models of form
  (decision examples name WAY-03).
- `foundations/invariants.md` `outbound-link-reach` — the Limen and Open Mercato addresses must be
  reachable without signing in (both answer 200).
- `elements/common/foundation_check.py` — how *Based on* splits items and recognizes quotations, so
  that inner quotation marks and ` · ` inside passages are safe.
- Research notes `watek_6_limen.md` (for the Limen file and commit) and `propozycja_szablonu_i_skilla.md`
  (rows A1–A16) — orientation only; no passage copied from them.

### Choices made (wording is mine within the rows; rejected way and cost if wrong)

1. Anthropic's recommendation quoted in WAY-236's *Based on*, not made a fact — it is a
   recommendation of practice, not a finding about models (WAY-90). Cost if wrong: one fact entry
   and one *Based on* item.
2. WebTestBench relied on (fact written): WAY-236's clause that an exploring agent's run is no
   permanent test rests on agents testing web applications poorly today; were that untrue, the
   clause would be questioned (WAY-90). Rejected: no fact, the clause unsupported. Cost if wrong: a
   fact withdrawn with its *Based on* item.
3. No cross-publisher sentence (WAY-85): Konstantinou measured GPT-3.5 Turbo (OpenAI), WebTestBench
   Claude and GPT models — publishers whose models the process's agents run on (WAY-85's own
   *Based on* names `anthropic-model-states` and `openai-model-states`).
4. Pages without editions cite archived copies (Anthropic, Vocke, Microsoft), as facts do; the
   Google book and OWASP cite the publishers' repositories at a commit instead of the live pages.
5. WAY-238 and WAY-239 keep apart (D9); WAY-239 cites only Vocke's rule, WAY-238 Vocke and Microsoft.
6. The 10xDevs piece is described by the course's name without a pointer (WAY-27, ruling C3).
7. "permanent test" for the task's "stały test", since "standing" would collide with the glossary's
   "standing check" (see search findings). Cost if wrong: a word replaced in six entries.

### Concerns

- **C-1 — WAY-235 against WAY-168's "on a convention of the product's code".** WAY-168 lets a rule
  of guidelines name an invariant "only where a cheap test of the product's suite checks the rule on
  a convention of the product's code". A refusal test checks the boundary's behaviour, which is not
  plainly "a convention of the code". The task (Q2, item 1) and the reviewed spec read WAY-168 as
  "a cheap test — invariant; otherwise review", and WAY-235's *Rationale* says so ("a refusal is
  behaviour a cheap test checks, so the rule names an invariant (WAY-168)"). If the orchestrator
  reads WAY-168 strictly, this is a collision with no precedence recorded (WAY-25): WAY-235 would
  need `narrows WAY-168` with its area in a binding sentence, which is a human's to record.
  Recommendation: keep as written — the meaning is the human's (Q2) and WAY-168's purpose is the
  cheap-test-versus-review split — and name the reading in the request.
- **C-2 — WAY-237 against WAY-24.** WAY-24: "A decision names no date or condition for its review."
  Row 7 puts the exclusion's "warunek powrotu" in the product decision's binding sentences (spec F3).
  I read the return condition as the scope of what the exclusion allows (WAY-30's foreseen
  exception), not a review trigger, and the *Rationale* says so. If read otherwise, the human
  settles it.
- **C-3 — WAY-236's environment fact of an AI tool.** Row 6: "narzędzie AI produktu ma fakt
  środowiska z wersją i datą odczytu". WAY-77 makes a version the product declares a sentence about
  the product (an invariant), never a fact; so WAY-236 words the fact as how the tool behaves, naming
  the version the product uses, with the date its source was read — a fact about the world, as
  WAY-90 allows ("the behaviour of a tool"). Same meaning as the row in my reading; flagged in case
  the orchestrator reads the row as a fact of the version alone.
- **C-4 — turn 2 dependencies.** The glossary `exemplar` widening and the WAY-228 edit settle the two
  findings above; until then, the branch holds WAY-231/WAY-242 using "exemplar" beyond its
  definition and WAY-228's rationale leaning on WAY-212 for tests. No entry of turn 1 refers to
  WAY-244–WAY-250 (the check would fail on a number the log does not hold).
  *Settled in turn 2.*

## Turn 2 — WAY-244 to WAY-250, the five edits in place, `exemplar`, ruling C10

**Status:** `done`.

### Files and commits

- `foundations/decisions.md` — +311 / −64: WAY-244 … WAY-250 appended after WAY-243; WAY-174,
  WAY-214, WAY-215, WAY-218 and WAY-228 edited in place; WAY-235 edited for ruling C10.
- `foundations/glossary.md` — +1 / −1: `exemplar` widened.
- Commit `57917c3` "Record the testing skill's decisions (WAY-244 to WAY-250), give the testing
  discipline its place in WAY-228, WAY-174, WAY-214, WAY-215 and WAY-218, widen exemplar to tests,
  and let WAY-235 narrow WAY-168", author e-mail `mariusznn@gmail.com`. Explicit paths. No push.

### Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (at `57917c3`) | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` (worktree equal to `57917c3`) | 0 | 109 tests, OK |
| scratch script comparing every quoted passage of WAY-228, WAY-231–WAY-250 and the two facts with the source fetched from its address | — | 33 of 33 found word for word (turn 1's 30 again, and 3 new) |

### Entries and their meaning (Polish, for the request, WAY-114)

| Entry | Row | Meaning |
|---|---|---|
| WAY-244 (new) | 17 | Skill testów proponuje, żeby przewodnik testów produktu powstawał przed pierwszym zadaniem, które pisze testy produktu. |
| WAY-245 (new) | 19 | Główny `AGENTS.md` produktu, poza blokiem instalatora, wskazuje przewodnik testów jedną linią ze ścieżką `guidelines/testing.md` w backtickach i warunkiem pisania albo zmiany testu, bez polecenia. |
| WAY-246 (new) | 20 | Przewodnik testów wymienia w *Applies to* każdą część mapy, której kod sprawdzają testy, i każdą część z plikami testów, a przed pierwszym testem — części, którym plan produktu daje testy; czyta się go przed napisaniem albo zmianą testu. |
| WAY-247 (new) | 21 | Jedno zadanie produktu może napisać naraz wytyczne kodowania i przewodnik testów, a sprawy każdej dyscypliny prowadzi w jego doprecyzowaniu jej własny skill. |
| WAY-248 (new) | 22 | Skill testów najpierw rozpoznaje, które części mają testy (albo dostaną je według planu) i co produkt już ma — narzędzie testów, poziomy, katalogi, zaślepki, testy niezmienników albo nic — i rozbudowuje to; nowe narzędzie testów albo biblioteka testów własności to wybór technologii, który zostaje pytaniem zadania. |
| WAY-249 (new) | 23 | Skill testów bierze zestaw startowy z preferencji człowieka, a bez nich z researchu dla technologii produktu — świeży agent na każde pytanie, źródła ze stroną i wersją, krytyka przed pokazaniem człowiekowi — i proponuje, nie narzuca. |
| WAY-250 (new) | 24 | Audyt produktu z testami kończy się, dla każdego poziomu, propozycją testu wzorcowego ze zdaniem o korzyści i 3–5 zarzutami z `plik:linia` i zdaniem skutku, a dla każdej granicy zaufania — informacją, czy ma test odmowy. |
| WAY-228 (edited) | 14 | Regułę wypisanych wartości wymaga teraz szablon testów, nie kodowania, i wiąże ona produkt od zadania, które pisze jego przewodnik testów; test własności bierze wejścia z generatora biblioteki, a oczekiwaną wartość z relacji, której nie liczy kod pod testem (odwrócenie operacji, zdanie niezmiennika, prostsza wersja napisana z wymagania), a znaleziony kontrprzykład zostaje zwykłym testem z wypisanymi wartościami. |
| WAY-174 (edited) | 18 | Zasada pytania człowieka o każdy wybór prostym językiem obejmuje też skill testów, który pokazuje wybory przewodnika testów przez skutek dla produktu, nigdy nazwą techniki ani narzędzia. |
| WAY-215 (edited) | 16 | Zadanie, które pisze albo zmienia testy w produkcie bez przewodnika testów, czeka w doprecyzowaniu na scalenie osobnego zadania przewodnika, tak jak zadanie bez styleguide'a albo wytycznych kodowania. |
| WAY-218 (edited) | 16 | Podział projektu stawia zadanie brakującego przewodnika testów przed zadaniami, które go potrzebują, jedno zadanie wytycznych może nieść naraz wytyczne kodowania i testów, a wyznaczenie testu wzorcowego poziomu idzie z zadaniem, które pisze pierwszy test tego poziomu. |
| WAY-214 (edited) | item 4 | Doprecyzowanie rozpoznaje, obok części, interfejsów, kodu i rodzajów kodu, także to, czy praca pisze albo zmienia testy, a skutek braku przewodnika testów obowiązuje od chwili, gdy przewodnik powstaje według WAY-244. |
| WAY-235 (edited, C10) | 5 | Dodatkowo: w obszarze granic zaufania decyzja ma pierwszeństwo przed WAY-168 — *Invariant* reguły granic zaufania wymienia niezmiennik odmowy każdej granicy, choć jego test sprawdza zachowanie produktu, a nie konwencję kodu (`narrows WAY-168`). |
| `exemplar` (glossary, edited) | D1 | Wzorzec to plik produktu, który decyzja produktu wyznacza jako model, według którego pisze się późniejsze pliki tego samego rodzaju: kod danego rodzaju kodu albo testy danego poziomu testów. |

`exemplar`, old and new definition: "…the model after which later code of its kind is written" →
"…the model after which later files of its sort are written: code of a kind of code, or tests of a
level of tests".

### Rulings applied

- **C10:** WAY-235 gains `narrows WAY-168` in *Relations* and a third binding sentence stating the
  area where it prevails; its *Rationale* now says a refusal is behaviour, not a convention of the
  code, so here the rule names an invariant where WAY-168 would leave it to review; its
  *Verification* gains the violating case of the rule reading `none` for that reason. Per WAY-18 and
  the template's "Relations and precedence", the relation stands only in the entry that prevails;
  WAY-168 stays unchanged, since nothing in its fields names what narrows it. The two do not narrow
  each other.
- **C11:** WAY-236 and WAY-237 kept as written in turn 1.

### Quotations (read 2026-10-25, compared by script)

| Entry | Source and address | Place |
|---|---|---|
| WAY-228 | Goldstein et al., *Property-Based Testing in Practice*, ICSE 2024, `https://www.cis.upenn.edu/~bcpierce/papers/icse24-pbt-in-practice.pdf` (the authors' PDF; the CDX index holds no archived copy, and none was made) | 4.3 Writing Specifications (round-trip and differential properties) |
| WAY-228 | Hypothesis, `https://raw.githubusercontent.com/HypothesisWorks/hypothesis/5057a16cd98bf2882848a031d3d50f1d25ba8b73/hypothesis/docs/stateful.rst` (the repository's head commit, 2026-10-23) | Invariants |

All turn 1 quotations re-checked in the same run (30/30). No new environment fact: WAY-228's sources
describe what developers do and what a library offers, not a finding about agents or models (WAY-90).

### Search of the whole foundation (WAY-33) — findings and corrections

- **C-4 settled:** `exemplar` now covers a level's exemplar test (WAY-231, WAY-242, WAY-250); WAY-228's
  *Rationale* no longer leans on WAY-212 and names WAY-246 as where the rule is read.
- **Uses of `exemplar`** (`git grep -i -w exemplars?` over every tracked file): every existing use is
  of a kind of code (WAY-167, WAY-198–WAY-201, WAY-207, WAY-209, WAY-216, WAY-218, the coding template
  and skill, `product-guidelines/reading.md`, `product-guidelines/template.md`, the two project-level
  skills); the widened definition keeps that meaning, so no use moves.
- **Neighbours read whole, consistent:** WAY-184 and WAY-209 (WAY-244); WAY-192 and WAY-212
  (WAY-245; WAY-212's condition "changing the product's code" stays the coding pointer's); WAY-213
  (WAY-246; not edited, as D6 gives); WAY-210 and WAY-211 (WAY-248, WAY-249; WAY-249 holds no
  research at every refresh, as the spec gives); WAY-201 and WAY-187 (WAY-250); WAY-216 and WAY-217
  (a departure under WAY-217 covers testing guidelines unchanged); WAY-114 (WAY-174 still narrows
  it); withdrawn WAY-70's row ("for a product's tests it stands in WAY-228") stays true.
- **References in other files** to the edited decisions (WAY-228 in `product-guidelines/coding/*`;
  WAY-214, WAY-215, WAY-218 in `product-guidelines/reading.md` and the two project-level skills) are
  the slices' work (WAY-169), not foundation entries; noted for slices 2–4.
- Glossary terms in the new text: "standing check" only in its glossary sense (WAY-174, WAY-247); no
  "element", "entry" or "slice" in another meaning.
- Invariants and part map: untouched.

### Own-work check

- Requirement most likely unmet: each edit in place keeps every sentence the task does not change and
  adds only what its row carries. Check: `git diff --word-diff` of WAY-174, WAY-214, WAY-215, WAY-218
  and WAY-228 read against the spec's *Decisions edited in place* and D4: only the testing
  discipline's words, the relations the spec names (WAY-215: WAY-244; WAY-218: WAY-244, WAY-242;
  WAY-228: WAY-231) and matching examples and *Rejected* items changed. One addition beyond the
  spec's list, by choice: WAY-218's binding sentence names WAY-247 with no relation (the spec gives
  it none).
- Binding sentences counted: none above three (WAY-235 now three).

### Reaches beyond the handoff (turn 2)

- `foundations/decisions.md` WAY-128, WAY-129 (relations of WAY-245) and WAY-107 (cited in its
  rationale), read whole.
- Goldstein PDF and Hypothesis docs fetched for WAY-228's *Based on* (spec "Quotations" table).

### Choices made

1. WAY-228's sources go to *Based on*, not *Rationale*: the property-test clause rests on them. Cost
   if wrong: moving them to prose.
2. WAY-245 to WAY-250 derive from WAY-173 besides the relations the spec names, following the spec's
   "each derives from WAY-173 unless noted". Cost if wrong: one relation removed each.
3. WAY-215's *Rejected* gains "testing guidelines with no wait" (Q8, way b), WAY-174's gains
   questions by the names of testing techniques, so the edited entries keep describing the decision
   as it stands (WAY-07).

### Concerns

- None open. The request should name WAY-235 `narrows WAY-168` (C10), the widened `exemplar` with
  both definitions, and WAY-228's new place and the task from which it binds.
