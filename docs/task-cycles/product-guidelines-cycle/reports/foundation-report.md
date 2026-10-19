# Foundation author report

Status: foundation committed as `c0d12611ac10fed4a7fe5b904880ea803e7644bc` (`docs(foundations): define product guidelines in the task cycle`). Implementation and return have not started. Author: `/root/author`; independent assessment belongs to the orchestrator. No subagents were used.

Worktree: `C:/Storage/repos/the-way/.runs/worktrees/product-guidelines-cycle`.
Branch: `task/product-guidelines-cycle`.
Original base and pinned process: `f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624`.
Authority: frozen `task.md`, its ten accepted settlements, reviewed `spec.md` (D1–D3), `reports/spec-review-report.md`, and `reports/author-handoff.md`. Spec choices remain provisional under the invoked task cycle until the human reviews the request.

## Work and boundaries

Used the worktree's `the-way-implement-task`, `the-way-record-decision` and `the-way-update-part-map` entry points and their named source files. Read the integration route, complete common working rules, decision and map templates and examples. No skill, template, test, invariant, glossary or environment fact was changed. No private note, backlog or external application was changed; no private course passage was copied.

The ten accepted settlements become WAY-213/1 through WAY-222/1. WAY-212/1 retains its binding sentences and fingerprint `116bffdf`; its rationale and rejected alternative now explain why the instruction pointer still serves sessions outside the task cycle. Its approval points to this request because the edited entry needs acceptance. All 198 existing decision binding fingerprints match the original base.

The map adds the dependency `project-level` → `product-guidelines`, and gives `product-guidelines` responsibility for the shared selection and absence discovery procedure. Its existing `product-guidelines/**` file assignment already covers the planned reading file. The change adds no external partner, trust boundary, irreversible effect, or observed failure mode. Its criticality remains high. The complete map and incoming references were considered; no other map entry needs an edit at this stage.

## Settlement mapping and Polish meanings for the request

Each row below preserves its accepted task row; the source of each is the corresponding row in `task.md`, *Settlements to record*. The reviewed spec supplies only the stated implementation design choices, not replacement meanings.

| Task row | Entry | Znaczenie do requestu |
|---|---|---|
| 1 | WAY-213/1 | Cykl wybiera pełne wytyczne według dotkniętych części i warunków spisu rodzajów, przekazuje je wszystkim agentom projektującym, wykonującym i oceniającym zmianę, odświeża wybór wraz ze zmianą zakresu, a planiście i autorowi bez planu daje też przykład kolejności pracy. |
| 2 | WAY-214/1 | Doprecyzowanie korzysta z tego samego odczytu wytycznych co cykl, rozpoznaje rodzaj przyszłej zmiany z jej zachowania, mapy i plików, a niepewność ujawnia jako pytanie; pominięta część w istniejącym pliku ogólnym wymaga rozszerzenia tego pliku. |
| 3 | WAY-215/1 | Brak styleguide'a lub ogólnych wytycznych kodowania zatrzymuje potrzebujące ich zadanie w doprecyzowaniu do scalenia osobnego zadania, także w istniejącym produkcie, z zachowaniem właściciela planu; po scaleniu wraca ustalanie znaczeń, a rozszerzenia istniejących wytycznych i zadanie piszące same wytyczne nie dostają tej blokady. |
| 4 | WAY-216/1 | Zadanie tworzące pierwszy plik rodzaju bez wpisu w spisie obejmuje wyznaczenie wzorca i zapis wytycznych rodzaju ze spisem, bez osobnej blokady, a zastane pliki wymagają porównania przewidzianego dla istniejącego kodu. |
| 5 | WAY-217/1 | Brak pliku nie jest wykrytym brakiem dla części, dla której aktualna decyzja produktu świadomie odstępuje od tych wytycznych, i wyjątek nie wychodzi poza zakres tej decyzji. |
| 6 | WAY-218/1 | Rozbicie projektu wykrywa braki tym samym odczytem i umieszcza potrzebne wytyczne przed zależnymi zadaniami, wykorzystując już istniejące odpowiednie zadanie, a wzorzec pierwszego rodzaju pozostawia zadaniu tworzącemu jego pierwszy plik. |
| 7 | WAY-219/1 | Autor i wykonawca części zmiany interfejsu sprawdzają przed przeglądem wymagane stany i zrzut ekranu, a przy nierozstrzygniętej drodze do produktu sprawdzają kod i jawnie oznaczają zrzut jako niesprawdzony w raporcie i requeście; awaria ustalonej drogi pozostaje awarią. |
| 8 | WAY-220/1 | Recenzent ocenia uwagę o wyglądzie według konkretnego skutku dla użytkownika w dotychczasowej skali, zachowując własne prawo do nadania wagi i zakresu uwagi. |
| 9 | WAY-221/1 | Samo odejście od przykładu lub niesprawdzanej części wzorca nie uzasadnia blokady: recenzent nazywa skutek dla użytkownika albo poprawności kodu, a reguły, niezmienniki i niezależność recenzenta pozostają w mocy. |
| 10 | WAY-222/1 | Cykl jawnie przyjmuje z lekcji przykład kolejności pracy, sprawdzenie stanów i zrzutu oraz ocenę wyglądu po skutku, bez porównywania zrzutów z wzorcowymi, narzucania wytycznych produktu, wyboru technologii poza definicją projektu i cytowania prywatnej lekcji. |

## Reading and search evidence

The author scanned complete Scope fields of the original 198 decisions and Part fields of 222 invariants. Starting affected parts: `task-cycle`, `project-level`, `product-guidelines`; actual consumers: `instruction-files`, `agent-instructions`. The initial selection contains 143 matching decisions, 32 additionally linked decisions, 68 matching invariants and 48 additional invariant methods touching the changed foundation files, plus `decision-guard-stale-reference/1`: 175 decisions and 117 invariants. Whole-source reads were completed, with truncated outputs reread in smaller complete-entry groups. The complete map, glossary, environment facts and violated-invariants register were read, as were the product-guidelines template and the process sources named above.

`foundation-source-inventory.json` preserves the complete original populations, IDs, source lines, complete matching field values and selection reasons. `foundation-search-inventory.json` records the 82 entry-level hits of the initial semantic search. The second, broader search expanded the decision reading to all 198 original decisions: WAY-24, 32, 42, 43, 58, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 90, 93, 94, 96, 98, 99, 105 and 141 were read whole in addition to the original 175. The final read inventory below marks these completed reads, not merely discovery. Source positions refer to the original base; new entry positions are also listed below.

Both searches used `rg` over the whole `foundations` directory, with no output limit in their saved stdout. Search terms and exact commands are in the execution ledger and command appendix. The initial terms included guidelines, styleguide, exemplar, screenshots, screens, appearance, visual, checklist, plan order, first file/code, waiting, plan changes and WAY-212. The expansion added Applies to, When to read, refinement, readiness, dependencies, preparation, review, finding, severity, states, running product and WAY-139/161/164. Whole reads supplied meaning; a match alone was not counted as an interpretation.

Manual collision assessment by `/root/author`, comparing each accepted row and spec choice with whole entries and their dependencies:

- WAY-167/171 and existing guideline form/index invariants supply the metadata; selection does not create a second metadata format. WAY-183/208 determine coverage. Existing files needing extension are distinguished from absent files.
- WAY-172/199 keep extension/correction within the task; WAY-184/209 retain their existing timing and WAY-200/201 keep comparison of existing code. WAY-139 is specifically about deployment skills, so the new separate-guidelines prerequisite does not rewrite or narrow that binding rule. Its contrasting workflow is explicitly chosen only for guidelines.
- WAY-124/144/154 and the plan ownership rules keep task `waiting for human`, result `waits for task <n>` and plan states distinct. WAY-143 still requires a consumer for preparatory work. WAY-152 does not reopen ready tasks: the waiting task has not reached readiness.
- WAY-173/193 retain product adoption and scoped departures. The task adds process obligations to the-way's skills; it does not directly bind product code or screens to this repository's template.
- WAY-164 keeps its weakest-requirement check; WAY-219 adds state/screenshot work beside it. WAY-121/165 keep access technology in the definition step. WAY-187 supplies the honest code-only/unchecked distinction. A failed settled route cannot masquerade as an unsettled route.
- WAY-161/162 preserve severity, reviewer ownership and correction rounds. WAY-195's nonblocking remark concerns coding style governed by the linter, not a visible effect on users. WAY-168/196/198 retain the rule/example boundary; no reviewer finding can be regraded by the orchestrator.
- WAY-100 and WAY-175 distinguish adoption by the task cycle from adoption by the styleguide. WAY-27 permits the described private source without quotes or private paths. No new external fact is asserted whose later change would send these choices to review under WAY-90.
- WAY-192/212 still serve sessions outside the cycle. Only WAY-212's now-stale rationale/rejected wording needed reconciliation; its binding part remains unchanged. No glossary term acquires a second meaning.

Observed result: no unresolved collision and no unapproved existing binding change. The new relations' fingerprints were independently recomputed locally; they match current targets. A later full return/reconciliation search and independent assessment remain required after implementation; this is the initial search, not a substitute for them.

## Invariant derivation assessment

WAY-12 requires executable invariants where a decision can yield them and permits level 2 only where no invariant can currently be derived; WAY-22 requires a derived invariant for what a commit can make false. This is not a waiver because a method is unavailable. Each new entry therefore carries concrete complying and violating examples under Verification level 2. The candidate considered for each group is recorded here:

| Entries | Candidate and why no new executable invariant follows |
|---|---|
| WAY-213/214/217 | Completeness and correctness of selection, classification of prospective work, whole reading and interpretation of a scoped departure depend on agent judgment against each product and task; the-way has no committed selection model whose presence proves those acts. Metadata syntax, real part names, index coverage and existing references already have `guidelines-form`, `guidelines-check-form`, `guidelines-check-kind-index` and reference invariants. Their sentences and checks remain unchanged. |
| WAY-215/216/218 | Whether a task needs a missing discipline, a question needs another task's merged answer, an existing prerequisite is adequate, or an instance is genuinely first is a semantic refinement/planning judgment. Existing task and project-plan form/state/dependency checks still cover the committed structures they own. A string check for prescribed skill wording would accept an instruction with an omitted or contrary condition and would not verify this judgment. |
| WAY-219 | Whether the author inspected applicable states and a rendered screenshot, whether evidence supports the observed result, and whether the route is settled are actions and evidence interpretation in a particular product; a committed phrase or path does not establish that inspection. Existing invariant checks and WAY-164 checks still run. The new policy does not prescribe a universal visual rule or new executable browser route. |
| WAY-220/221 | Whether a visual or example-related finding has a concrete user/correctness consequence and warrants a severity is the independent reviewer's judgment. Counting severity words or enforcing a keyword would replace that judgment with a different rule, and cannot establish the consequence. Binding product rules continue to be checked through their own invariants. |
| WAY-222 | The explicit adoption and its non-goals concern the practice the cycle follows, not a new executable interface feature. Agent review can compare the skills and reports against the named adoption and exclusions. No reference-image subsystem, product-specific prescription, or technology-selection mechanism is added. |

These choices match the existing level-2 treatment of comparable cycle/refinement judgments in WAY-139, 144, 148, 161, 164, 173, 193 and 200; they do not demote any existing level-1 obligation. Existing decision/map shape, relation, source, approval and sentence-count invariants apply to the new foundation text and were checked by the guards. No new/changed invariant sentence or method is required; therefore the WAY-69 separate sentence/check authors were not invoked. If implementation reveals a new commit-checkable contract, work must return to that boundary before its test is written.

## Choices, costs and outstanding work

The ten entries keep the accepted settlements separately reviewable, at the cost of a longer decision log. Merging them would hide distinct future reasons to change. The shared lookup adds a procedure used at three points; independent lookup would reduce initial wiring but permit selection and absence discovery to drift. Separate preparation of absent discipline guidelines costs a wait even for an urgent existing-product fix; writing them inside its consumer would shrink their coverage to that fix. The first-kind exception avoids a circular wait and keeps existing-code comparison explicit. Scope-limited departures honor the product's human choice at the cost of losing that guidance for later work in the same scope. Screenshot fallback keeps work moving while retaining visible uncertainty. Example freedom can accumulate inconsistency, but existing binding rules and a later deliberate promotion of a recurring issue to a rule remain available.

No open question or additional design choice requires a human answer at this stage. Implementation is not authorized to start until the orchestrator resumes this author. The request URL remains a placeholder until a real request exists; the orchestrator must replace it in WAY-212..222 before completion. Five pre-existing overdue-review warnings remain outside this task. Guard unchecked results remain unchecked; this report does not claim a full gate pass.

## Checks and manual evidence

All commands in the appendix were actually executed by this author; no orchestrator baseline is claimed as this run. `foundation-checks.jsonl` records exact argument vectors, actual exit codes and paths to complete stdout/stderr. Guard `.jsonl` files preserve every verdict. The failed first inventory run is retained: exit 1 on the non-entry heading `Withdrawn identifiers`; fixing the inventory to exclude headings without entry versions yielded the expected population and selected counts. This was a reporting utility failure, not a product check failure.

The decision guard returned 0 errors, 16 warnings, 5 unchecked: five overdue reviews (WAY-03/21/52/55/69), eleven merge-link placeholders (WAY-212..222); base-line/version/template comparisons, merge TODO, duplicate versions and relation-fingerprint comparison are unchecked for `none`. The manual fingerprint check supplies evidence for the new links but does not relabel the guard's unchecked verdict.

The part-map guard returned 0 errors, 0 warnings, 7 unchecked: two missing flow-coverage files, no promise-level change-path command, no dependency graph command, and three absent-base checks (known violations, identifiers, lowered criticality). The invariant guard returned 0 errors, 0 warnings, 3 unchecked (base identifiers/versions/corrections/violations, merge TODO and fingerprints), with no human verdict file. The glossary guard returned 0 errors, 0 warnings, 5 unchecked (base Avoid counts, collisions, changed-definition uses; merge TODO and unused terms). The environment-facts guard returned 0 errors, 0 warnings, 3 unchecked (base identifiers/versions; merge fingerprints and unused facts), with no human verdict file.

The author's critical-flow run `python -B gate/run_tests.py gate` completed 98 tests, OK, exit 0. It is a test suite, not the full foundation gate. No screenshots apply to this prose-only foundation stage.

Manual check actor `/root/author`: read all new entries beside the exact accepted settlement table and reviewed spec; observed ten mapped meanings, unchanged exclusions, no invented course quote, scoped exceptions, no new review severity scale, no missing author/slice role. Evidence: mapping above, tracked foundation diff, and `foundation-binding-check.stdout.txt`. Compared the changed map entry with the full map and planned file ownership; observed the needed dependency and shared responsibility with no new file ownership boundary. Actual commit, diff counts, completed inventory and exact execution ledger follow.


## Completed inventory and execution appendix

Complete IDs, original source locations, full Scope/Part values and completed-read flags: `foundation-completed-read-inventory.json`. Original discovery snapshots remain unchanged. Whole reads total 198 original decisions and 117 invariants; every row of both populations remains available, including unselected invariants.

Changed file line counts before commit (`git diff --numstat`):

```text
333	5	foundations/decisions.md
3	2	foundations/part_map.md
```

Current entry positions:

- WAY-212/1: `foundations/decisions.md:7225`.
- WAY-213/1: `foundations/decisions.md:7266`.
- WAY-214/1: `foundations/decisions.md:7302`.
- WAY-215/1: `foundations/decisions.md:7339`.
- WAY-216/1: `foundations/decisions.md:7381`.
- WAY-217/1: `foundations/decisions.md:7410`.
- WAY-218/1: `foundations/decisions.md:7436`.
- WAY-219/1: `foundations/decisions.md:7468`.
- WAY-220/1: `foundations/decisions.md:7504`.
- WAY-221/1: `foundations/decisions.md:7530`.
- WAY-222/1: `foundations/decisions.md:7560`.

Exact command argument vectors, exit codes and complete output paths (relative to cycle `reports/`); vectors preserve shell-independent arguments:

- Command: `["rg", "-n", "-i", "guideline|styleguide|exemplar|screenshot|screen|appearance|visual|checklist|plan order|first file|first code|waiting for human|waits for task|plan change|WAY-212", "foundations"]`; exit `0`; stdout: `foundation-search.stdout.txt`; stderr: `foundation-search.stderr.txt`.
- Command: `["python", "-B", ".runs/task-cycles/product-guidelines-cycle/reports/foundation_inventory.py"]`; exit `1`; stdout: `foundation-inventory.stdout.txt`; stderr: `foundation-inventory.stderr.txt`.
- Command: `["python", "-B", ".runs/task-cycles/product-guidelines-cycle/reports/foundation_inventory.py"]`; exit `0`; stdout: `foundation-inventory-fixed.stdout.txt`; stderr: `foundation-inventory-fixed.stderr.txt`.
- Command: `["rg", "-n", "-i", "Applies to|When to read|refin|readiness|waiting|blocked|depends|preparatory|review|finding|Minor|Important|states|running product|WAY-212|WAY-139|WAY-164|WAY-161", "foundations"]`; exit `0`; stdout: `foundation-search-broad.stdout.txt`; stderr: `foundation-search-broad.stderr.txt`.
- Command: `["python", "-B", "elements/decisions/format_guard.py", "--base", "none", "--merge-onto", "none", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-decisions.jsonl"]`; exit `0`; stdout: `foundation-decisions.stdout.txt`; stderr: `foundation-decisions.stderr.txt`.
- Command: `["python", "-B", "elements/part-map/format_guard.py", "--base", "none", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-part-map.jsonl"]`; exit `0`; stdout: `foundation-part-map.stdout.txt`; stderr: `foundation-part-map.stderr.txt`.
- Command: `["python", "-B", "elements/environment-facts/format_guard.py", "--base", "none", "--merge-onto", "none", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-environment.jsonl"]`; exit `0`; stdout: `foundation-environment.stdout.txt`; stderr: `foundation-environment.stderr.txt`.
- Command: `["python", "-B", "elements/invariants/format_guard.py", "--base", "none", "--merge-onto", "none", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-invariants.jsonl"]`; exit `0`; stdout: `foundation-invariants.stdout.txt`; stderr: `foundation-invariants.stderr.txt`.
- Command: `["python", "-B", "elements/glossary/format_guard.py", "--base", "none", "--merge-onto", "none", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-glossary.jsonl"]`; exit `0`; stdout: `foundation-glossary.stdout.txt`; stderr: `foundation-glossary.stderr.txt`.
- Command: `["python", "-B", "gate/run_tests.py", "gate", "--record", ".runs/task-cycles/product-guidelines-cycle/reports/foundation-gate-tests.jsonl"]`; exit `0`; stdout: `foundation-gate-tests.stdout.txt`; stderr: `foundation-gate-tests.stderr.txt`.
- Command: `["python", "-B", ".runs/task-cycles/product-guidelines-cycle/reports/foundation_verify.py"]`; exit `0`; stdout: `foundation-binding-check.stdout.txt`; stderr: `foundation-binding-check.stderr.txt`.
- Command: `["rg", "-n", "product-guidelines@", "foundations"]`; exit `1`; stdout: `foundation-map-incoming.stdout.txt`; stderr: `foundation-map-incoming.stderr.txt`.
- Command: `["git", "diff", "--check"]`; exit `0`; stdout: `foundation-diff-check.stdout.txt`; stderr: `foundation-diff-check.stderr.txt`.
- Command: `["git", "diff", "--numstat"]`; exit `0`; stdout: `foundation-diff-counts.stdout.txt`; stderr: `foundation-diff-counts.stderr.txt`.

The incoming map-fingerprint search exits 1 because there are no `product-guidelines@` matches; its command executed normally, and the broad search has positive matches for the part identifier. The diff whitespace check exits 0. No warning or unchecked result requires a new ruling before implementation: merge placeholders require the later request URL, old review dates retain their existing warning, and absent-main/undeclared-reporting limits are the established pre-main route. Full final gate and independent foundation assessment remain with the orchestrator.

Commit verification: `git commit -F .runs/task-cycles/product-guidelines-cycle/reports/foundation-commit-message.txt` exited 0 after explicit staging of `foundations/decisions.md` and `foundations/part_map.md`; git reported 336 insertions and 7 deletions across those two files. `git log -1 --format='%H %ae'` returned the commit above and the configured private-repository email; `git status --short` returned no changes. The branch has no upstream, so no mismatched-upstream warning applies. The report and evidence remain in the ignored cycle directory for the orchestrator's eventual carrying commit; they are not claimed as tracked in the foundation commit. The temporary source-excerpt read buffer was removed so it cannot be archived as a copy of git-held source.
