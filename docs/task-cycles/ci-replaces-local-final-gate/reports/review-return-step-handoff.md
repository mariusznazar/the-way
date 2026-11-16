# Handoff â€” review of the return step's commits

You are a reviewer (agent type `the-way-stage`, model `opus`) of a task cycle of the-way; you did not make this change. Nothing here is the human's approval.

- Worktree (read-only for you): `the task's worktree`, branch `task/ci-replaces-local-final-gate`.
- Method: `task-cycle/review/SKILL.md`; your variant is the review of the return step's commits, against the task and the foundation entries the return step writes or corrects (section 2 of the method). Read `task-cycle/skill/return_step.md` for what the step is to do.
- Range: `1b03ef71fb4fbd634282b6a9123913c06c0387e6..e3842146a4ed24254eb16a302284f231f0dd1801` (one commit, `e384214`, `foundations/decisions.md` only: WAY-381 and WAY-162 brought in line with two CI jobs and the CI final gate). Compute the diff yourself.
- The author's report of the step: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-return-step-report.md` (claims to verify). It also says it wrote no environment fact for three GitHub behaviours (a check can be required only after it has run once; `windows-latest` has Git Bash; a draft request still starts a `pull_request` run) and holds that none stands under a decision's sentence; judge that, and whether another entry the change touches no longer matches the code.
- Foundation entries by identifier, each whole: WAY-381, WAY-162, WAY-160, WAY-16 (`foundations/decisions.md`); the invariant `ci-checking-commands` and `function-and-file-size` if the diff bears on them. Guidelines: none bear on a change of the decision log alone.
- The task, frozen: `docs/task-cycles/ci-replaces-local-final-gate/task.md`. Passages, word for word from it (file as address):

## Decisions in play

- **WAY-160** — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. […] Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the orchestrator waits for the result of the run on each head it pushes to it, a correction's included, treats a red result as a failed gate […]” Jej *Rejected* podaje: „the CI result in place of the cycle's final gate — an error visible only on the cycle's own system is no longer caught, and the cycle stops where the host of the repository fails.” Zadanie zmienia ją punktami 1 i 2 *To do*: przebieg CI na prośbie z gotowym kodem jest końcową bramką cyklu, a lokalny przebieg końcowy biegnie tylko wtedy, gdy CI na prośbie nie biegnie albo nie da wyniku w 30 minut.
- **WAY-16** — „In CI that command runs on every merge request, with `.the-way` at the commit the product pins (WAY-34), from a file of CI configuration that the product writes itself by the description the-way gives, and the installer writes none. The result of that run is a check the repository requires before a merge, and the owner of the repository may bypass it.” Zadanie dokłada do opisu, według którego produkt pisze plik CI, systemy, na których CI biegnie (punkt 4 *To do*).
- **WAY-261** — „The red result of the first run of the gate on the final tree stays the result of the gate, also where the check that failed is one outside the task's scope that passes when run again; the cycle does not stop for it, and the request names that check and the task that fixes it, or proposes that task where none exists.” Wyjątek z punktu 1 *To do* zostaje bez zmian.
- **WAY-350** — „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.” Zdanie decyzji zostaje bez zmian: porównanie dalej obejmuje tylko przebiegi lokalne, których będzie mniej; zmienia się opis cyklu bez pliku z czasami w audycie (punkt 5 *To do*).

## Settlements to record

Candidates: 7 shown, 6 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy na prośbie o scalenie z gotowym kodem biegnie CI, jego wynik na ostatnio wypchniętym commicie jest końcową bramką cyklu: cykl nie uruchamia pełnej bramki lokalnie ani na końcu, ani po scaleniu z gałęzią docelową, a przebieg na kodzie wyjściowym i po przesunięciu przypiętej wersji the way zostaje lokalny. | sentence of WAY-160 | Questions to settle — pytania „Czy zadanie kończy się raportem…” i „Które przebiegi pełnej bramki przechodzą do CI?” (wybór Mariusza; *Not chosen* tam) | czy CI zastępuje tylko przebieg końcowy, czy też przebieg na kodzie wyjściowym i po przesunięciu wersji, i czy cykl dalej uruchamia bramkę lokalnie przed otwarciem prośby |
| 2 | Gdy na prośbie CI nie biegnie, cykl uruchamia pełną bramkę lokalnie, tak jak dziś. | sentence of WAY-160 | To do, punkt 1, ostatnie zdanie; wiersz wyprowadzony przez agenta, przyjęty przez doradcę dnia w imieniu Mariusza, 2026-11-15: „1 a” | czy produkt bez pliku CI, jak dziś loop2, zostaje bez końcowej bramki |
| 3 | Gdy CI nie da wyniku w ciągu 30 minut od wypchnięcia commita, cykl uruchamia pełną bramkę lokalnie, a opis prośby mówi, że CI nie odpowiedziało i bramka biegła lokalnie. | sentence of WAY-160 | Questions to settle — pytanie „Co cykl robi, gdy GitHub nie odpowiada…” (wybór Mariusza; *Not chosen* tam) | jak długo czekać na CI i czy cykl staje, czy idzie dalej bez CI |
| 4 | CI the way biegnie na Linuksie i na Windowsie, bo jego wynik zastępuje końcową bramkę cyklu, a 32 testy biegną tylko na Windowsie. | data or code: `.github/workflows/tests.yml`, komentarz przy wyborze systemów | Questions to settle — pytanie „Czy Windows trzeba sprawdzać…” (wybór Mariusza; *Not chosen* tam) | czy CI the way zostaje na samym Linuksie |
| 5 | CI produktu biegnie na każdym systemie, na którym produkt działa, bo jego wynik zastępuje końcową bramkę cyklu. | sentence of WAY-16 | Questions to settle — pytanie „Czy Windows trzeba sprawdzać…”, drugie zdanie odpowiedzi (wybór Mariusza; *Not chosen* tam) | na jakich systemach produkt ma uruchamiać CI według opisu w `installation/README.md` |
| 6 | Pomiar czasów bramki zostaje tylko dla przebiegów lokalnych, a audyt przy zapisie cyklu bez pliku z czasami podaje końcową bramkę w CI jako trzecią możliwą przyczynę obok cyklu wcześniejszego i zepsutego pomiaru. | skill or instruction file: `process-audit/SKILL.md` | Questions to settle — pytanie „Co audyt procesu robi z czasami bramki…” (wybór Mariusza; *Not chosen* tam) | czy pobierać czasy CI z GitHuba do `gate_times.md`, czy zostawić fałszywe „pomiar się zepsuł” |

- Do not run the product's full gate. `python -B elements/common/foundation_check.py` and single directories are yours to run, with command and exit code.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/review-return-step-report.md`, first line `PASS <sha>` or `FAIL <sha>`; with **Unread material**, **Searches not found or unclear**, the working copies line. Return the first line, the path and a one-line check result.
- Your directory for working copies: `.runs/review-return-step/`.

An agent of the cycle that makes a working copy to check something â€” a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test â€” makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy â€” a worktree with `git worktree remove --force`, then
`git worktree prune` â€” keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
