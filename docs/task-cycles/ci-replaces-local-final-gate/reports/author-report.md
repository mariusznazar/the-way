# Author report — ci-replaces-local-final-gate

**Status:** done with concerns (the concerns: the Windows job is unverified on GitHub, WAY-365 move not made, the foundation fact `foundations-branch-ruleset` will be stale after the human action; each below)

## Commits (base `8f0c1c3`, branch `task/ci-replaces-local-final-gate`, not pushed)

1. `b2f3f82` — audit: the final gate in CI named as a cause of a copy with no `gate_times.md` (row 6): `process-audit/audit_count.py`, `process-audit/test_audit_count.py`, `process-audit/SKILL.md`.
2. `1c65f5f` — CI file with the Windows job, `agent-instructions/README.md`, `installation/README.md` (rows 4, 5 text of the READMEs; To do 3, 4): `.github/workflows/tests.yml`, `agent-instructions/README.md`, `installation/README.md`.
3. `b646084` — WAY-160 and WAY-16 and the cycle's files (rows 1, 2, 3, 5): `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `blocked_finding.md`, `reserved_return.md`, `correction.md`, `request_template.md`, `task-cycle/record_template.md`, `task-cycle/change/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/test_request_check.py`.

Sixteen files changed in all (`git diff --stat 8f0c1c3..HEAD` gives the line counts per file).

## Checks (command, exit code)

All run from the worktree root on this Windows machine. The product's full gate was not run (WAY-160, the orchestrator's alone).

| Check | Exit code |
|---|---|
| `python -B gate/run_tests.py process-audit` (before the code: 2 failures, the two tests I changed, for the expected reason — see below; after: 235 tests OK) | before 1, after 0 |
| `python -B gate/run_tests.py task-cycle` (534 tests, 1 skipped: a Windows signal test) | 0 |
| `python -B gate/run_tests.py agent-instructions` (37 tests, 2 expected failures — the invariant test and its pair, pre-existing) | 0 |
| `python -B gate/run_tests.py installation` (62 tests) | 0 |
| `python -B gate/run_tests.py instruction-files` (105 tests, 5 skipped: POSIX-only) | 0 |
| `python -B gate/run_tests.py product-guidelines` (14 tests) | 0 |
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0 (`0 errors`) |
| `python -B -I .runs/author/check_ci_file.py` (the own-work check below, kept as `reports/author-ci-file-check.py`) | 0 |

Failing runs written first (process-audit, before the code change):
- `test_a_copy_without_the_files_gives_unknown_values_with_their_reasons_and_no_error` failed on the old reason of `Gate runs` (no "a final gate that ran in CI").
- `test_a_version_with_no_cycle_that_gave_a_value_has_one_row_and_one_line_of_reason` failed on the old *Gate times of version* reason.
- Command `python -B gate/run_tests.py process-audit`, exit 1; after the code, the same command, exit 0.

I did not run `elements`, `project-level`, `relation-model`, `gate`: no file of them changed. `agent-instructions` and `installation` tests passed with the changed READMEs.

## Own-work check (WAY-164)

Requirement most likely not met: the acceptance criterion — the CI run on Windows executes the 32 tests that Linux skips, and the Windows job works at all (venv where the gate looks for Ruff, same pinned actions, `pull_request`, read-only token, names settable as required checks).
Check written: `reports/author-ci-file-check.py` (parses the workflow with PyYAML and asserts): trigger is `pull_request` into `foundations`; `permissions: contents: read`; two jobs named `tests` (`ubuntu-latest`) and `tests-windows` (`windows-latest`); the actions of both jobs are the same and each stands at a 40-character commit; the last step of each job is exactly `python -B gate/run_tests.py` (no directory, no other checking command — invariant `ci-checking-commands`); the Windows venv step is `python -m venv .runs/quality-venv` and `.runs/quality-venv/Scripts/python.exe -m pip install --require-hashes -r requirements-quality.txt`, matching `Scripts/ruff.exe` under `.runs/quality-venv` that `agent-instructions/test_linter_invariant.py` looks for when `os.name == "nt"`. It exited 0.
What it did not show and I could not check: that the Windows runner of GitHub runs the 32 tests green. How the job is built to run them: it is the whole gate (`python -B gate/run_tests.py`) on `windows-latest`, where `os.name == "nt"`, so the tests whose skip condition is `os.name != "nt"` (`WINDOWS_ONLY` in `instruction-files/test_check_instructions.py`, the junction tests of `installation/test_install.py` that skip with "Junctions exist only on Windows", the junction test of `task-cycle/test_remove_merged_worktrees.py`) are not skipped. On this Windows machine the directories ran with only POSIX tests skipped (instruction-files: 105 tests, 5 skipped; task-cycle: 1 skipped, a signal test). The figure 32 comes from the task's context (the Linux run 43710999530); I did not recount it. Not checked, because I cannot run GitHub: that the runner lets `mklink`-style junctions and symbolic links be made (a test that cannot make one skips itself with `skipTest`, so a runner that refuses would show fewer than 32 run — the first run on the request tells); that the wheels of Ruff 0.17.1 for Windows are in `requirements-quality.txt` (the README says every wheel of the release is listed; I did not open the sums for the Windows wheel); that Git Bash is the shell `shell: bash` selects on `windows-latest` (it is on the runner image, to my knowledge, not verified here); the time of the Windows run (unknown; the job's limit is 60 minutes, Linux's 40).

## Names of the checks (for the human action)

- Linux check name unchanged: `tests`. New Windows check: `tests-windows` (job `name:`). Two separate jobs, no matrix, because a matrix would name the checks `tests (ubuntu-latest)` and break the name `tests` the ruleset requires (`foundations-branch-ruleset`).
- Request-ready text for the Human action (the task's *Human actions*): "In the ruleset `foundations_tests` of the repository the-way add the required status check `tests-windows` (integration: GitHub Actions) beside `tests`, keeping the bypass for the owner. GitHub offers `tests-windows` for selection only after it has run once, so do it after the first CI run on this request. The name of the Linux check stays `tests`; nothing to correct there." Polish: "W regule gałęzi `foundations_tests` repozytorium the-way dodaj wymagane sprawdzenie `tests-windows` (GitHub Actions) obok `tests`, z prawem obejścia dla właściciela. GitHub pokaże `tests-windows` do wyboru dopiero po pierwszym przebiegu, więc zrób to po pierwszym przebiegu CI na tej prośbie. Nazwa sprawdzenia na Linuksie zostaje `tests`."

## Foundation entries (the foundation step)

Each row of *Settlements to record*, where it went, with the sentence in English and in the document's language.

- **Rows 1, 2, 3 → `WAY-160`** (`foundations/decisions.md`, edited in place; marked `row 1`, `row 2`, `row 3`).
  - EN: Where CI runs on a request with finished code, its run on the head pushed last is the cycle's final gate and the orchestrator runs no full gate itself at the end or after the merge with the target branch; the run on the base and after the pin moves stay local; where CI runs on no request the orchestrator runs the gate itself; where the CI run gives no result within 30 minutes of the push the orchestrator runs the gate itself and the description says CI did not answer.
  - PL: Gdy na prośbie z gotowym kodem biegnie CI, jego przebieg na ostatnio wypchniętej głowie jest końcową bramką cyklu, a cykl nie uruchamia pełnej bramki lokalnie ani na końcu, ani po scaleniu z gałęzią docelową; przebiegi na kodzie wyjściowym i po przesunięciu wersji zostają lokalne; gdy CI nie biegnie, bramka biegnie lokalnie; gdy CI nie da wyniku w 30 minut od wypchnięcia, cykl uruchamia bramkę lokalnie, a opis mówi, że CI nie odpowiedziało.
  - Also rewritten with it: the *Verification* pair, *Rationale*, and *Rejected* (the old item "the CI result in place of the cycle's final gate" is removed, since it is now the decision; two ways kept by the row's sources added: CI also for the base and the pin move; a cycle that stops until CI answers).
  - Wording choices: the entry has two binding paragraphs (the second is the wait, the 30 minutes and the blocked request), not one; the first sentence was reworded so that it does not say that the orchestrator itself runs the gate where CI does (the old first sentence stood in the fixture of `task-cycle/test_request_check.py`, which I changed to the new sentence).
- **Row 4 → code: `.github/workflows/tests.yml`**, the comment at the choice of the systems (no entry). EN: the CI of the-way runs on Linux and on Windows because its result replaces the cycle's final gate and the tests of each system run only there. PL: CI the way biegnie na Linuksie i na Windowsie, bo jego wynik zastępuje końcową bramkę cyklu, a testy każdego systemu biegną tylko na nim.
- **Row 5 → `WAY-16`** (edited in place; marked `row 5`). EN: In CI the product's one command runs on every merge request and on every system the product runs on, and the result of each run is a required check. PL: CI produktu biegnie na każdym systemie, na którym produkt działa, a wynik każdego przebiegu jest wymaganym sprawdzeniem. Its description for products: `installation/README.md`, "Run the one command in CI", new item 6 and the paragraph on the result. Its *Verification*, *Rationale* and *Rejected* were edited (two ways kept by the row's source added: CI on one system alone; CI on Linux and on the author's machine only the Windows directories).
- **Row 6 → skill file `process-audit/SKILL.md`** (no entry), with the message in `process-audit/audit_count.py` (`read_optional`, the *Gate times of version* line, the module description) and the tests. EN: the measuring of gate times stays for the local runs only, and a copy with no `gate_times.md` is named as an earlier cycle, a final gate that ran in CI, or a failed measuring script, with the record's *Verification* saying which. PL: pomiar czasów bramki zostaje tylko dla przebiegów lokalnych, a brak `gate_times.md` w kopii zapisu tłumaczy cykl wcześniejszy, końcowa bramka w CI albo zepsuty pomiar, o czym mówi *Verification* zapisu.
- Row 6, the part about *Verification* of the cycle's record saying the final gate ran in CI: `task-cycle/record_template.md` (the *Verification* paragraph and the line on `gate_times.md`), `task-cycle/skill/SKILL.md` step 10 and 12.
- No entry marked `projected` or `the cycle's`; no pair of examples added beyond the ones the two decisions already carried (I changed their wording).
- The search of the whole foundation (WAY-33): WAY-162 says the cycle "runs the gate on the code the revert leaves"; I left it, since "the gate" there is the gate WAY-160 defines (CI's run or the local one). WAY-367 (the gate on the starting state), WAY-350, WAY-261, WAY-243 need no change. The environment fact `foundations-branch-ruleset` states what the ruleset is today (one required check `tests`); it stays true until the human sets the second check, and needs a new reading (the `gh api` command in it) after that — I cannot do the reading (WAY-82); the request should say so.
- `foundation_check.py` ran with exit 0 and `0 errors` and no `listed:` lines.

## What the other files changed

- `task-cycle/skill/SKILL.md`: step 10 now says which run is the final gate (the CI run where a file of CI configuration starts one on a request into the target branch; local otherwise, and local for the runs of steps 2, 4, for a request blocked for unfinished code, and where CI gives no result in 30 minutes); step 12 waits for the CI run for at most 30 minutes, falls back to the local run, runs no gate after the merge where CI is the final gate; steps 2, 4, 9.4 point at the local run; step 4 reads a CI run's result from the merged branch's *Verification*.
- `blocked_finding.md`, `reserved_return.md`, `correction.md`, `request_template.md` (*Checks*), `record_template.md`, `change/SKILL.md`, `plan/SKILL.md`: wording that cited the local final gate or the wait. `planning.md` was read and left (its line says a slice's *Checks* hold no run of the gate, still true).
- `.github/workflows/tests.yml`: second job, own comment; the Linux job's steps unchanged.

## Trust boundary (`process-audit/audit_count.py`)

What the script reads from a record copy and what I checked: a missing `gate_times.md` gives `unknown` with a reason, no `Error:`, exit 0 (test `test_a_copy_without_the_files_gives_unknown_values_with_their_reasons_and_no_error`, now with the new cause); an empty `gate_times.md` is a missing field `table of the runs`, `Error:` line, exit 1, never an empty list of runs (new test `test_an_empty_gate_file_is_a_missing_field_and_not_an_empty_list_of_runs`; it passed at once, since the reading already did it — I added it because a cycle with its final gate in CI is where a missing or odd file becomes ordinary); a table without a column, a row of the wrong width, crafted values, more than 500 runs, a git failure on the file are covered by existing tests that passed. The new message is built from constants of the script (`ABSENCE_CAUSES`), no text of the copy enters it. The audit's own change does not start a new series of gate times (WAY-339 names `gate_times.py` and `gate/run_tests.py` for that).

## Choices (with the way rejected and its cost if wrong)

1. **No WAY-365 move.** `process-audit/audit_count.py` stands at 3317 lines, over the 1000-line threshold of WAY-385, and my change adds about 6 net lines to it (a constant, a longer message, a docstring line). I made no move of a part out as the method asks for the first commit. Reason: the part next to my change, `read_gate` (108 lines, itself over the 80-line threshold), is entangled with `Cycle`, `missing_reason`, `table_cells` and the trust boundary; moving it is a refactor larger than the change, and another branch (`task/audit-answers-contradiction-after-code`, commit `6867078`) already moves other parts of the same file and adds a module to the part map's trust boundary and to the test's copy list, so a second move here would conflict in the same lines. Rejected: a move of the reading of `gate_times.md` into its own module. Cost if wrong: the reviewer may grade it as a finding on WAY-365 (a file over the threshold; WAY-363 does not soften it); the fix is one move commit before this one.
2. **Two jobs, not a matrix**, to keep the name `tests`. Rejected: a matrix `os: [ubuntu-latest, windows-latest]` (checks `tests (ubuntu-latest)`, `tests (windows-latest)`; the ruleset's `tests` would never report and no PR could merge without the bypass). Cost if wrong: duplicated steps in the file.
3. **`shell: bash` for the Windows job**, so the README's commands (`.runs/quality-venv/Scripts/python.exe …`) run as written. Rejected: PowerShell with the same path. Cost if wrong: the job fails at the venv step on the first run, visible at once.
4. **Windows `timeout-minutes: 60`** (Linux 40), since the Windows time is unknown; the cycle's 30-minute wait then falls back to the local run if the Windows job is slower. Rejected: 40. Cost if wrong: a slow Windows run makes every cycle run the gate locally too until the time is known.
5. **How "CI runs on the request" is told** (step 10): by a file of CI configuration that starts a run on a request into the target branch (on GitHub a workflow on `pull_request` for it), confirmed on the request's page; the task gives no rule, so this is my reading. Rejected: asking the host for the checks before the request exists (it cannot answer). Cost if wrong: for a product whose workflow does not start for some request, the cycle skips the local gate and then finds no run in 30 minutes, and falls back to local — a wait, no wrong pass.
6. **The *Rejected* of WAY-160** takes two ways from the sources of rows 1 and 3. The not-chosen way of the question "Does the task end with a report or change the process at once" (a report only, the change in another task) is left out: it is a way of ending the task, not a way of running the gate; a reviewer who finds it missing from row 1's source has a Minor finding at most (WAY-364). Cost if wrong: one added clause.
7. **No change to `README.md` at the root**: its line about "the one command of tests run in CI on every pull request" stays true.
8. `process-audit/audit_count.py`: the reasons of the two optional files now come from `ABSENCE_CAUSES`; the text of the old reason for `mechanism_measures.md` is unchanged.

## Reaches beyond the handoff

- Read whole the files the handoff named plus: `elements/decisions/skill/read.md`, `decide_entry.md` (named by the decisions `SKILL.md` for its steps 1 and 2), `task-cycle/record_template.md` (the *Verification* paragraph — task row 6 needs it; the handoff named `task-cycle/skill` files but not this one), `README.md` section "Installing the linter" (named by the handoff), `foundations/environment_facts.md` lines of `github-required-status-checks`, `github-ruleset-bypass`, `foundations-branch-ruleset`, `foundations/invariants.md` entry `ci-checking-commands` (found by search; to check that a second job breaks no invariant), WAY-385 and WAY-365 (found because `audit_count.py` is over the size threshold), `git show 6867078` (the other branch's move out of `audit_count.py`; to learn the form of a move). Gap in the selection: the handoff did not name `task-cycle/record_template.md` or WAY-365/WAY-385.
- Did not read the full `installation/README.md` or the full `agent-instructions` directory beyond the two sections and the files the tests run.

## Unread material

- `.runs/orchestrator/index.md`: read whole. Decision entries WAY-16, WAY-160, WAY-261, WAY-350, WAY-243 read whole (WAY-243's and WAY-350's only for their binding sentences, rationale and *Rejected*; all read to their end). The decisions skill's `read.md`/`decide_entry.md` read whole.
- Entries "of the parts task-cycle, process-audit, agent-instructions and installation that the foundation step's search finds": I searched the log for "gate", "final gate", "Windows", "own system" and read the hits in context (WAY-55, WAY-162, WAY-367 table row, WAY-344 for the field rule). I did not read whole every decision whose *Scope* names those parts (the index lists them by heading; none of the headings pointed to a bearing on the change beyond the ones above). `foundations/part_map.md`: I did not open it; no file was added or moved.
- `guidelines/coding-check.md`: not read; no script of the kind `check` changed.
- No test, skill or README other than the ones named in the commits was opened whole.

## Searches not found or unclear

- The task gives no rule for telling that CI runs on a request before the request exists; I wrote one (choice 5).
- `foundations/part_map.md` and the invariant list were not searched for an entry naming the second CI job; `ci-checking-commands` (review method) is the only one found and the second job runs the same one command.
- The count "32 tests" could not be reproduced here (no Linux run); I found the skip conditions in `test_check_instructions.py`, `test_install.py`, `test_remove_merged_worktrees.py` but did not sum them.

## Working copies

`.runs/author/` held the logs of the focused runs and `check_ci_file.py`; the script was copied to `reports/author-ci-file-check.py` and `.runs/author/` removed. No worktree or clone made. Nothing remains.

## Problems observed

- Two `Edit` calls on `foundations/decisions.md` first failed with "string not found" where the old text I quoted differed from the file in the wrapping of one line; the file was unchanged by the failed call and I repeated with the exact text. No consequence.
- The pre-tool hook of the session asked for reading `scripts.md` and `git.md` once each; read, no consequence.
