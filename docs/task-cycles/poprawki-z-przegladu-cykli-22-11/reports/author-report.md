Author report — the whole change, one author without a plan (`make-change`).

**Status:** done with concerns (concerns: see "Concerns" below; no check of the changed code failed at the end; checks I did not run are listed).

Worktree `the worktree root`, branch `task/poprawki-z-przegladu-cykli-22-11`, base `2a2f4106c216c0fef4e68b7ed8bd5728ae2660ae`.

## Commits (range `2a2f4106..HEAD`)

| Commit | What |
|---|---|
| `0b3a8ab1` | point 4: `task-cycle/slice_size.py` verdict `fits by ranges of <file>`, with tests |
| `4efde783` | point 11.1: `task-cycle/gate_times.py` starts the first word as `shutil.which` resolves it, with tests |
| `ae37fca3` | fix of my own test of 11.1 (a path of the mocked `which` was absolute, the repository's private-paths test refused it) |
| `2a03c166` | point 11.2: `gate/run_tests.py` counts the last `Ran <n> tests` line of a directory, with a test |
| `943d4153` | point 10: `elements/common/decision_index.py`, tests, `elements/common/way_of_working.md` |
| `89ae582c` | point 5.1, 5.2, 5.3, 5.5: `instruction-files/check_instructions.py`, tests, `instruction-files/SKILL.md`, `AGENTS.md` (one reworded line, see Choices) |
| `b7d99dfa` | prose of points 1, 3, 4, 6, 9, 12, 13 in `task-cycle/change|review|plan|skill/SKILL.md` |
| `9a4d108d` | prose of points 2, 7, 8, 9 in the templates and skills of `decisions`, `part-map`, `environment-facts` |
| `9a948c7e` | foundation: WAY-255, WAY-25, WAY-136 edited, WAY-418 new; `installation/README.md` (5.4); `task-cycle/review/whole_change.md` (5.4) |

Files changed, with added and removed lines (`git diff --stat 2a2f4106..HEAD`, 26 files, 847 insertions, 129 deletions; the fix commit `ae37fca3` adds 3 and 3 more to the 61-line growth of `task-cycle/test_gate_times.py`):

```
AGENTS.md                                    |   6 +-
elements/common/decision_index.py            | 121 +++++++++++++++++++---
elements/common/test_decision_index.py       | 113 ++++++++++++++++++++
elements/common/way_of_working.md            |   7 +-
elements/decisions/skill/SKILL.md            |   4 +-
elements/decisions/template.md               |   8 +-
elements/environment-facts/skill/draft.md    |   3 +-
elements/environment-facts/template.md       |  13 ++-
elements/part-map/skill/SKILL.md             |   5 +-
elements/part-map/template.md                |   5 +
foundations/decisions.md                     | 102 ++++++++++++++++---
gate/run_tests.py                            |  15 +--
gate/test_run_tests.py                       |  13 +++
installation/README.md                       |   3 +
instruction-files/SKILL.md                   |   4 +-
instruction-files/check_instructions.py      | 147 +++++++++++++++++++--------
instruction-files/test_check_instructions.py | 145 +++++++++++++++++++++++++-
task-cycle/change/SKILL.md                   |  13 ++-
task-cycle/gate_times.py                     |  18 +++-
task-cycle/plan/SKILL.md                     |  20 +++-
task-cycle/review/SKILL.md                   |   7 +-
task-cycle/review/whole_change.md            |   5 +-
task-cycle/skill/SKILL.md                    |  22 ++--
task-cycle/slice_size.py                     |  54 ++++++++--
task-cycle/test_gate_times.py                |  61 +++++++++++
task-cycle/test_slice_size.py                |  62 +++++++++++
```

## Foundation entries (foundation step)

Each entry written by following `elements/decisions/skill/SKILL.md` (with `read.md`, `decide_entry.md`, the template, `rules.md`, `way_of_working.md`), on the task branch. The index of my selection is kept as `reports/author-decision-index.md` (written with `decision_index.py`; 47 decisions listed in full, 128 by heading; I read in full the ones the handoff and the work name: WAY-25, 255, 136, 12, 18, 225, 148, 160, 229, 339, 390, 385, plus 365, 344 by the index).

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-255 (a paragraph, *Rationale* and *Rejected* rows added, pair extended) | row 1 | An agent that waits for a long command stops it if it has not ended 30 minutes after it started, the same for every product, reports it as unfinished with the command and the last lines of its output, and the orchestrator enters its check as one that did not run. | Agent, który czeka na długie polecenie, zatrzymuje je, gdy nie skończyło się po 30 minutach (tyle samo w każdym produkcie), zgłasza je jako niezakończone z poleceniem i ostatnimi liniami wydruku, a prowadzący wpisuje jego sprawdzenie jako niewykonane. |
| WAY-25 (a paragraph, *Rationale* and *Rejected* rows added, pair extended) | row 2 | A decision that narrows another leaves the log only with the area where it prevails carried into that other decision or into the skill or template that takes the rule, or it stays; a decision whose *Rejected* refuses its withdrawal stays. | Decyzja, która zawęża inną, opuszcza dziennik tylko z obszarem swojej przewagi przeniesionym do tamtej decyzji albo do skillu lub szablonu, który przejmuje regułę; inaczej zostaje, a decyzja, której *Rejected* odrzuca jej wycofanie, zostaje zawsze. |
| WAY-136 (a sentence in the first paragraph, *Rationale* and *Rejected* rows added, pair extended) | row 3 | A slice of a plan may leave tests failing that a later slice of the same plan makes pass, if its *Goal* names each such test file and that slice, and the failure of a test so named is no failing check of the slice that meets it. | Kawałek planu może zostawić czerwone testy, które naprawia późniejszy kawałek tego samego planu, jeśli jego *Goal* nazywa każdy taki plik testów i ten kawałek; oczekiwana porażka takiego testu nie jest czerwonym sprawdzeniem kawałka. |
| WAY-418 (new, end of the section "Instruction files") | row 4 | The product keeps the script that checks its instruction files at no warning, a change corrects a warning it adds as an error, and a warning in a run on the head of the change is an Important finding of the review of the whole change within the task's scope, with no comparison with the base. | Produkt trzyma sprawdzarkę instrukcji na zerze ostrzeżeń, zmiana poprawia ostrzeżenie, które wnosi, jak błąd, a ostrzeżenie w przebiegu na głowie zmiany to uwaga recenzenta całej zmiany — Important, w zakresie zadania — bez porównywania z bazą. |
| pairs added to WAY-255, WAY-25, WAY-136 | the cycle's | Each of the three decisions already carried a pair of examples; I extended each pair with one clause in *complies* and one in *violates* for the sentence added, so that the sentence is held (WAY-12). | Każda z trzech decyzji miała już parę przykładów; rozszerzyłem każdą o po jednym członie w *complies* i *violates* dla dopisanego zdania, żeby zdanie było trzymane (WAY-12). |

Nothing is `projected`; the task carries no projected entries. No question was left to the human.

Pairs of examples added, word for word (the lines that are new; the rest of each pair is unchanged):

WAY-255, *complies* (appended): "an executor whose test file has not ended 30 minutes after it started stops it and reports it unfinished with the command and the last lines of its output, and the orchestrator enters the check it stood for as one that did not run;" — *violates* (appended): "an executor waits two hours in four-minute stretches for a test file that never ends; the orchestrator reads the check of a run that was stopped as unfinished as passed."

WAY-25, *complies* (appended): "a change withdraws a decision that narrows another in the same change that carries the area where it prevailed into that other decision or into the template that takes the rule; a decision whose *Rejected* refuses its own withdrawal stays in the log;" — *violates* (appended): "a change withdraws a decision that narrows another, or goes against one it derives from in a narrower area, and carries the area where it prevailed nowhere."

WAY-136, *complies* (appended): "a slice leaves a test file failing that a later slice makes pass, and its *Goal* names the file and that slice, and the executor of a later slice reports the test as failing as expected, not as a failing check of its slice;" — *violates* (appended): "a slice leaves a test failing that no *Goal* of the plan names; the executor of a slice takes a test that the plan lists as failing for a failing check of its slice and is retried for it."

WAY-418 (the whole pair, written whole for the new decision; the row asks for a pair as the cheapest holding, so I mark the entry `row 4`):
- complies: "a change that names a path in an instruction file makes the path exist, or names it where the script does not read it, such as a block of code or text the script takes for no path; the review of the whole change reads one warning of the script in its run on the head of the change, grades it Important within the task's scope and does not look at the run on the base;"
- violates: "a change leaves a warning of the script in an instruction file, and the review passes it because the base held the same warning; the review compares the warnings of the base with those of the head and keeps only the new ones; the review grades such a warning Minor, or lists it among the findings outside the task's scope."

*Rejected* of the four entries (WAY-134): WAY-255 takes the two ways of question 1's *Not chosen* (a multiple of the time of the product's full tests; 30 minutes that a dispatch may lengthen) and, as the row's last column names it, the criterion of silent output, which stands in the task's *Context* point 1, not in the row's *Source* — see Concerns 1. WAY-25 takes the rejected check over `narrows` (*Context*, point 2). WAY-136 takes the rejected ban on a red state (*Context*, point 3). WAY-418 takes the three ways of the row's source (comparison of base and head; paths of a server into blocks of code; a warning that blocks nothing, the *Not chosen* of question 3).

The decision-skill step 4.4 ("what follows"): no decision derives from or narrows the three edited decisions in a way their new sentences change; no invariant derives from them; no invariant of WAY-418 is needed (held by the pair, as the row asks). The search of the foundation (WAY-33) for `WAY-255`, `narrows` and `30 minutes` found no second statement of any row; the 30 minutes of WAY-160 concern the wait for CI and are another matter.

## Checks run

All paths from the worktree root; "exit" is the exit code. The gate (`python -B gate/run_tests.py` with no argument) was not run.

| Check | Command | Exit |
|---|---|---|
| point 4, failing before the code (`test_a_slice_too_large_only_for_one_changed_file_fits_by_its_ranges`, `1 != 0`) | `cd task-cycle && python -B -m unittest test_slice_size` | 1 |
| point 4, passing | the same | 0 |
| point 11.1, failing before the code (the `.cmd` test: `cannot start 'gatecmd'`; the `which` test: `['npm', ...]` != the path) | `cd task-cycle && python -B -m unittest test_gate_times.PassThroughTest` | 1 |
| point 11.1, passing (54 tests, 1 skipped: the signal test of POSIX) | `cd task-cycle && python -B -m unittest test_gate_times` | 0 |
| point 11.2, failing before the code (`7 tests ...` instead of `2 tests`) | `python -B gate/run_tests.py gate` | 1 |
| point 11.2, passing (37 tests) | `python -B gate/run_tests.py gate` | 0 |
| point 10, failing before the code (13 failures) | `cd elements/common && python -B -m unittest test_decision_index` | 1 |
| point 10, passing (25 tests) | the same | 0 |
| point 5, failing before the code (4 failures) | `cd instruction-files && python -B -m unittest test_check_instructions` | 1 |
| point 5, passing (120 tests, 5 skipped: POSIX-only link and FIFO cases) | the same | 0 |
| mutation of the invariant `check-instructions-refuses-outside-links` for the new `.gitignore` read (the `leads_out` guard removed for a moment): `test_an_ignore_file_that_is_a_link_out_of_the_repository_is_not_read` failed; the guard restored before the commit | `cd instruction-files && python -B -m unittest test_check_instructions.NamesInTheIgnoreFile` | 1, then 0 after restoring |
| the check of instruction files on the-way itself, at the base: 2 warnings; at the head: none | `python -B instruction-files/check_instructions.py .` | 0 (head) |
| ruff format and lint (ruff 0.17.1 installed in `.runs/author/venv`, since the sandbox has none) on the changed folders | `.runs/author/venv/Scripts/ruff format --check <folder>` and `.runs/author/venv/Scripts/ruff check <folder>` | 0 |
| the foundation check with the switch, during the change | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |
| the foundation check on the finished change, without the switch | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| directory `task-cycle`, all my commits except the last fix | `python -B gate/run_tests.py task-cycle` | 1: one failure, `test_no_tracked_file_holds_an_absolute_path_or_a_note_link` (my test of 11.1 held `a path of a drive's tools directory ending in npm.CMD`); fixed in `ae37fca3`; see next row |
| the failing test and the tests of the file I fixed, after the fix | `cd task-cycle && python -B -m unittest test_gate_times test_tracked_files_private_paths` | 0 |
| directory `gate`, after all commits | `python -B gate/run_tests.py gate` | 0 |

Rows of the table that did not fit above:

| directories after all commits | `python -B gate/run_tests.py elements/common` · `... elements/part-map` · `... instruction-files` · `... installation` · `... agent-instructions` · `... product-guidelines` | 0 each (six runs, started at the same time as the `task-cycle` run) |
| directory `task-cycle` once more as a whole after `ae37fca3` | not run: the one failing test and the file I fixed were rerun (row above); the directory takes several minutes | not run |

## Own-work check (WAY-164)

- Requirement most likely not met: point 5, that the noise of the instruction check falls while no real warning is lost, and that the three new levels do not let a missing path hide (a check of a trust boundary file).
- Check: ran the script of the base (`git show 2a2f4106:instruction-files/check_instructions.py`) and the script of the head on the-way and on four other repositories of this disk (read only; the script writes nothing), and compared the sets of `WARN` lines (`reports/author-compare-warnings.py`).
- Result: no repository got a warning the base did not have (0 new `WARN` on each of five). On the repository the task names as the example (loop2), warnings fell from 144 to 22: 89 absolute paths outside the repository and the home directory and 22 relative paths under a name of the root `.gitignore` became `info`; the examples of 5.1 (`#/konta`, `#/mapy`, `#/wiedza`, `.css`, a `restrict,command=...` text) are no longer looked up. The 22 that remain contain the real ones the task lists as out of scope and 7 that 5.1 does not name (see Concerns 3). On the-way the check now stands at no warning (base: 2).
- Crafted input at the two trust-boundary files (the handoff's answer: yes): for `gate_times.py` an empty first word and a first word that names a directory end as the script's own `Error:` with exit 2, no traceback (test `test_a_first_word_that_names_no_file_to_start_is_an_error_not_a_traceback`); a NUL cannot come through a command line. For `check_instructions.py` the new reads are a `.gitignore` that is a link out of the repository (not read, reported as a link not read, test with the invariant line), a directory, a non-UTF-8 file (no crash, the file names nothing); `elsewhere` compares text only and asks the file system nothing; the existing guard of network paths is untouched (the three tests that expected `warn` for an absolute outside path still look the path up, and now expect `info`).

## Walkthrough (`walkthrough.md`; rewritten in the fix of round 1, finding I4)

**Judgment.** The change alters behaviour a user sees in a terminal: what five commands print and how they end — `decision_index.py --decision` for a withdrawn number (a line, exit code 0, where it ended with exit code 2), `slice_size.py` (the verdict `fits by ranges of <file>`, exit code 0), `check_instructions.py` (`INFO` where it printed `WARN`, fewer lines), `gate_times.py` (starts `npm` on Windows, where it failed to start) and `run_tests.py` (another count on its last line). The earlier version of this section judged that it alters none; that was wrong (WAY-406).

**The walk is not performed.** The foundation of the-way settles no way to the-way as a running product: no decision gives its logs, its interface, its development data or a place for its screenshots, and no skill of it cites one. By `walkthrough.md` section 1 I make sections 2 to 4, run no section 5 and mark every case unchecked with that reason; the cycle does not stop. (The commands were run by hand during the work, and the reviewer ran them too; that is no walk, since it is no way the foundation settles, and no case below rests on it.)

**What the change alters, in the user's words.** A person who asks the index of decisions for a withdrawn number gets the decisions that took its place and a line saying so, in place of an error. A person who plans a task gets `fits by ranges of <file>` for a slice that only one big changed file made too large. A person who checks instruction files gets fewer warnings: text that is no path and paths on other machines or in the ignore file are no longer reported as missing. The cycle's orchestrator can time a gate declared as `npm test` on Windows. The runner's last line counts a directory's tests once. Code shared with other paths that the change touches: `check_dead_paths` serves every instruction file the script reads, the one the user gives with `--file` included; `decision_index.py` serves every skill that reads the foundation.

**Scope.** Each requirement the tests already cover is left to them; the walk would take what no test reads: the whole text a command prints, and its use on a real log and a real repository.

**What I did not check, and why.** Every case below: the foundation settles no way to run the-way as a running product. Also outside the plan: other platforms than Windows for `gate_times.py` and the `.cmd` case (the test is skipped there); loop2's own `.gitignore` as input beyond the counts of my own-work check.

**Plan of cases (all unchecked, reason: the foundation settles no way to the running product):**

| Case | By what | Verdict |
|---|---|---|
| `--decision 7`, `WAY-7`, `D-07` of a real log print the same decision (task point 10) | a command in a terminal on the real log | unchecked: no way to the running product settled |
| `--decision` of a withdrawn number with living successors lists them in full under a line with the reason; of one with no successor prints the line `it has no successor` and exits 0; of one whose successor is withdrawn names the chain (point 10, question 4) | a command in a terminal on the real log | unchecked: same reason |
| `--decision` on a log whose withdrawn table lacks a column ends with exit code 2 naming the file and the field (WAY-344, fix of I2) | a command in a terminal on a made-up log | unchecked: same reason |
| `slice_size.py` on a plan whose one changed code file is too big whole prints `fits by ranges of <file>` and exits 0; on a plan over the limit of files prints `too large` and exits 1 (point 4) | a command in a terminal on a made-up plan | unchecked: same reason |
| `check_instructions.py` on a repository with `#/konta`, `.css`, a server path outside the repository and the home directory, a name of the root `.gitignore` and the shell idiom for a quote prints `INFO`, never `WARN`, for each, and still `WARN` for a path inside the repository that names nothing (point 5) | a command in a terminal on a made-up repository | unchecked: same reason |
| `check_instructions.py --file` on a global instruction file with an absolute path that names nothing prints `WARN` as before (point 5.2) | a command in a terminal | unchecked: same reason |
| `gate_times.py -- npm test` on Windows runs `npm.cmd` and ends with its exit code (point 11.1) | a command in a terminal on Windows with Node installed | unchecked: same reason (and no `npm` is declared by the-way) |
| `run_tests.py` with no argument on a repository whose tests print the report of a nested run ends with the count of each directory's own tests (point 11.2) | a command in a terminal | unchecked: same reason, and the full run is the cycle's own (WAY-160) |
| side observation | whatever shows on the way | unchecked: nothing walked |

The tests of the change, which the plan above leaves to their own level, are in "Checks run"; each case above has a test that gives its input and asserts its output (the `npm` case on Windows only).

**Fell wrong, corrected, errors outside the task's scope:** none found, since nothing was walked.

## Choices, with the way rejected and the cost if wrong

1. `fits by ranges of <file>` takes the first file of *Change*, in the order written, whose ranges bring the slice under the limit of reading; rejected: the file whose counting saves the most — it needs a second comparison and names a file a reader may not expect; cost if wrong: the row names one of two files that both would do. Exit code stays 0 for it (rejected: 1 — the plan skill says no slice to split). A slice over the limit of files stays `too large` whatever the ranges.
2. `shutil.which` is applied on every platform, not only on Windows; rejected: only where `os.name == "nt"` — a second path to test and no gain, `which` returns the same executable on POSIX. Cost if wrong: a POSIX `PATH` entry that `which` and `exec` read differently (none known). `which` on Windows also searches the current directory first, as `CreateProcess` does for `.exe` already; the declared command comes from the product, so no new exposure.
3. `decision_index.py` finds the number by value and ignores the prefix, and keeps the identifier of the withdrawn list in the line (`WAY-46 is withdrawn: ...`) with the *Why* verbatim — several *Why* cells begin with the word `withdrawn:`, so the line reads `is withdrawn: withdrawn: it said ...`; rejected: stripping it — it would edit the table's words. A chain with several successors is walked depth first and flattened: `its successor <ID> is withdrawn: <why>` for each withdrawn one met, then `its successors are listed in full` if any decision lives at an end, else `it has no successor`. A loop of withdrawn numbers ends the walk.
4. In `check_instructions.py` an absolute path outside the repository and the home directory is still looked up, and noted as `info` only where it is not found; rejected: noting every such path as not checked without a lookup — it would add an `info` line for every `/usr/bin/...` that exists. The `.gitignore` name rule takes a line that is one name, with a slash before or after it taken off; a line with a slash inside, a pattern, a comment and a negation name no part.
5. `AGENTS.md` line 13 reworded (`that skill's \`SKILL.md\`` to `the \`<skill>/SKILL.md\` of that skill`): the base had one real warning there and the new rule makes a warning on the head a blocking finding of this very change; rejected: leaving it and reporting it — an Important finding on my own change; cost if wrong: a one-line rewording of an instruction file the task does not name. It adds no rule (WAY-128).
6. The three tests of `NetworkShapesOffWindows` that expected `warn` for `///host/x.md`, `/host/x.md`, `/net/host/x.md` on Linux and `a path of a drive's share directory ending in x.md` now expect `info`, with a comment naming point 5.2 as the cause; they still check that the path is looked up. The cause lies in the requirement (an absolute path outside the repository and the home directory is `info`), not in the data.
7. The new decision stands at the end of "Instruction files" with number WAY-418 (the next free: entries to 417, withdrawn to 371). Scope: instruction-files, task-cycle, installation.
8. Where a function or a file stands over the threshold (WAY-385, WAY-365): none did; the largest function I touched is `check_layout` at 88 lines (not changed by me); `check_instructions.py` is 1020 lines, under 1200. No move-out commit was needed.

## Reaches beyond the dispatch

- `foundations/decisions.md`: reading by search the sections around WAY-258 (the end of "Instruction files") and the `## Withdrawn identifiers` table, to place WAY-418 and to learn the shapes of withdrawn chains (179 rows, 136 with `none`, 8 pointing to a withdrawn number, 3 with several successors) — to test chains against real data.
- `elements/common/foundation_check.py` and `foundation_text.py`: `table`, `items`, `blocks` (read their code to reuse `items` and `blocks` in `decision_index.py`).
- `guidelines/coding-shared-module.md`, `coding-generator.md`, `coding-measuring-report.md`, `coding-repository-changer.md`: read to see which kind `decision_index.py` is; it matches none of the six kinds' *When to read* (it is no shared module, generator, measuring report or changer), so I took only the general `coding.md`.
- `foundations/invariants.md`: the invariants `function-and-file-size` and `check-instructions-refuses-outside-links` (read by search).
- Other repositories on this disk, read only, through the script, for the own-work check (counts only in this report).
- `installation/README.md` lines 55-110 and `AGENTS.md`, to place point 5.4 and the one rewording.

## Unread material

- (round 1: `task-cycle/change/walkthrough.md` was unread when this report was first written; the fix read it whole.)
- `foundations/invariants.md`, `foundations/part_map.md`, `foundations/glossary.md`: read by search or by the entries of the touched parts (part map lines 1-30, 56-82, 105-118, 145-154, 193-215 read); the glossary entries of the terms I use were not read whole (I coined no term).
- Decisions read only by the index, not whole: WAY-229, 160, 148, 339, 390, 18, 225 (quoted whole in the task; I read their binding sentences there and in the index, and not their *Rationale* and *Rejected* in the log, since the change leaves them as they are).
- `task-cycle/skill/foundation_step.md` and `elements/common/way_of_working.md` read whole; `elements/decisions/skill/read.md` and `decide_entry.md` read whole; `elements/decisions/skill/projected.md` not read (projected mode does not apply).
- Skill and template files I did not change but the handoff names as read: `task-cycle/slice_size.py` etc. were read whole. `task-cycle/skill/SKILL.md` read whole.

## Searches not found or unclear

- Where the handoff of a later slice lists the tests a plan leaves failing (point 3, second sentence of the quoted wording): the file that lists what each slice's handoff carries is `task-cycle/skill/planning.md`; the task names `task-cycle/plan/SKILL.md` and step 9 of `task-cycle/skill/SKILL.md` only, so `planning.md` was not changed, and its list of what a slice's handoff carries does not yet name the failing tests of the plan. Unclear whether the task meant it to.
- The row 1 *Rejected* variant "the criterion of silent output" is in the task's *Context* point 1 and in the last column of the row, not in the row's *Source* (question 1's *Not chosen*): unclear whether WAY-134 lets it in; I wrote it.
- The check of instruction files still warns on loop2 on the token `'\''` (6 times, a shell quote idiom) and on `src/browser/sim/hex.ts:10-30` (a range of lines after a path): point 5.1 names neither (a quotation mark there is read as `"`), so they are not excluded. `.env` as a bare token is now no path, since `env` is in the list of extensions.
- `ruff` is not installed in this sandbox; I installed 0.17.1 into `.runs/author/venv` to check format and lint.

## Concerns

1. The *Rejected* of WAY-255 holds a way (silent output) that comes from the task's *Context* and the row's last column, not from the row's *Source* proper; see Searches.
2. Where a quoted wording met current text: point 3's first sentence says a slice's *Checks* hold no test an earlier slice leaves failing, while `task-cycle/change/SKILL.md` also has the executor run "the tests of the code you touched"; the quoted sentence covers it ("reports a listed test that fails as expected"). Point 4's wording in `task-cycle/slice_size.py`'s old docstring ("counts whole ... whatever ranges") contradicted the new verdict; I rewrote that paragraph of the docstring. Point 8 and the quoted sentence of `elements/part-map/skill/SKILL.md` stand between "never rewrite it to fit the code" and "Where the two differ": no contradiction found.
3. Point 11 changes the measuring script and the test runner: a new series of gate times starts (WAY-339); nothing else for the author.
4. The `AGENTS.md` rewording (Choice 5) is outside the points of the task; it is there so that the head has no warning.
5. The directory runs of `task-cycle`, `elements/common` and the others ran at the same time on a loaded machine and took several minutes; the one failure of `task-cycle` was mine and is fixed.

## Working copies

`.runs/author/` of the worktree stood with: a virtual environment `venv/` (ruff 0.17.1), my scripts (`sizes.py`, `compare.py`, a copy of the base's `check_instructions.py` and of the head's before a mutation), the index `index.md`, `sections.md`, and the outputs of the directory runs. Kept in `reports/` beside this report: `author-decision-index.md` (the index) and `author-compare-warnings.py` (the comparison of the base and the head script). The rest was removed with the directory itself by its full path (see the line below).

Removed: `.runs/author` with all it held (removal by its full path, command exit 0); no remainder, no git worktree or clone was made.
