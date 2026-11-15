# Report of the one author — ci-on-merge-requests

**Status:** `done with concerns` (the concerns are listed under "Problems as observed" and "Searches
not found or unclear"; none blocks the request).

Worktree `the worktree of the task`, branch `task/ci-on-merge-requests`,
base `21ecb627f885de438e2209d7ff5c137b1e1b9d83`. Nothing was pushed and no `gh` call that changes
anything was made (the `gh api` calls were GET reads of release tags and `action.yml` files).

## Commits (base..head, oldest first)

| Commit | What |
|---|---|
| `7217667` | `installation/README.md`: the description of what a product's CI file holds (new section "Run the one command in CI"), the paragraph on the product's tests, the table row of `AGENTS.md` |
| `ff45403` | `installation/install.py` (`product_guidance`, the paragraph "Before a merge, ...") and `installation/test_install.py` (two tests) |
| `80e9eca` | `instruction-files/test_check_instructions.py`: two tests that failed on Linux |
| `66121c8` | `.github/workflows/tests.yml`, `foundations/part_map.md` (agent-instructions gets `.github/workflows/**`), `agent-instructions/README.md` |
| `3410e33` | `foundations/decisions.md`: WAY-16, WAY-206, WAY-160 and WAY-09 |
| `a5abe37` | `product-guidelines/coding/settle.md`, `task-cycle/skill/SKILL.md` (step 12), `task-cycle/skill/request_template.md` (*Checks*), `task-cycle/record_template.md` (*Verification*) |
| `7d027c6` | root `README.md`: the directory list of `agent-instructions` |
| `7c301ce`, `ddcbfc2` | `instruction-files/test_check_instructions.py`: the rest of the Linux fixes (the guard of the macOS shapes, one test split in two) |
| `345b6bd` | `foundations/decisions.md`: a passage of WAY-09 rewrapped, the two "price" sentences of WAY-160 merged |

Files changed (`git diff --numstat 21ecb62..HEAD`, added/removed): `.github/workflows/tests.yml` 42/0,
`README.md` 4/2, `agent-instructions/README.md` 11/0, `foundations/decisions.md` 78/27,
`foundations/part_map.md` 1/0, `installation/README.md` 43/5, `installation/install.py` 9/3,
`installation/test_install.py` 17/0, `instruction-files/test_check_instructions.py` 15/4,
`product-guidelines/coding/settle.md` 10/5, `task-cycle/record_template.md` 3/1,
`task-cycle/skill/SKILL.md` 8/1, `task-cycle/skill/request_template.md` 4/2 — 13 files, 245
insertions, 50 deletions. Head: `345b6bd`.

## What the job's name is (for the branch rule)

The workflow is named `tests` and holds one job, `jobs.tests`, with `name: tests`. The check to
select in the branch rules of `foundations` is the one the first run lists for that job: `tests`
(the pull request page may show it as `tests / tests (pull_request)`; I could not run it, so which
form the rule lists is unchecked). The name stays: the workflow's comment says so.

## The foundation entries (marked as the foundation step gives)

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-16, two new sentences (CI runs the one command on every merge request with `.the-way` at the pinned commit, from a file the product writes, the installer writes none; the result is a check the repository requires, the owner may bypass) | `row 1`, `row 2` | The one command of tests also runs in CI on every merge request, from the product's own CI file, and its result is a required check with a bypass for the owner. | Jedno polecenie testów biegnie też w CI na każdej prośbie o scalenie, z pliku CI, który pisze produkt, a jego wynik jest wymaganym sprawdzeniem z prawem obejścia dla właściciela. |
| WAY-16 *Scope* gains `installation`, *Relations* gains `derives from WAY-34`, *Verification*, *Rationale* and *Rejected* carry the two sentences | `the cycle's` | The decision now binds what the installer promises a product and rests on the pin of WAY-34. | Decyzja wiąże teraz to, co instalator obiecuje produktowi, i opiera się na przypięciu z WAY-34. |
| WAY-206, one new sentence (the signal for a vulnerability in a dependency the product already holds is the alerts of the repository's service, on GitHub Dependabot; the skill proposes them, a human turns them on); *Verification*, *Rationale* (weak points rewritten), *Rejected* brought in line | `row 4` | A vulnerability found in a library the product already uses gets its signal from the service's alerts, which the skill proposes and a human turns on. | Luka znaleziona w bibliotece, której produkt już używa, dostaje sygnał z alertów serwisu, które skill proponuje, a włącza człowiek. |
| WAY-160, one new sentence (the orchestrator waits for the CI result on the open request before the request is marked ready, treats a red result as a failed gate — a fix and its review — and puts the result into the description); *Verification*, *Rationale*, *Rejected* | `row 6` | The cycle waits for the CI run on its request, treats red as a failed final gate and writes the result into the description. | Cykl czeka na wynik CI na swojej prośbie, czerwony traktuje jak nieudaną końcową bramkę i wpisuje wynik do opisu. |
| WAY-09, the sentence names the CI configuration under `.github/workflows/` among the files the map gives to `agent-instructions`; one clause in *Verification* | `the cycle's` | The CI file is a file of the repository that the part map gives to `agent-instructions`, and WAY-09's list of what the repository holds says so. | Plik CI jest plikiem repozytorium, który mapa części daje części `agent-instructions`, i lista z WAY-09 o tym mówi. |
| part map, `agent-instructions` *Files* gains `.github/workflows/**` | `the cycle's` | The workflow has a part that answers for it. | Workflow ma część, która za niego odpowiada. |

Rows not written as an entry: row 3 stands as the comment at the head of `.github/workflows/tests.yml`
(Linux, why, Windows is checked by the cycle's gate); row 5 stands as the installer's block
(`installation/install.py`, `product_guidance`). Row 3's and row 5's meaning: *CI of the-way runs on
Linux because the POSIX tests cannot run on the author's Windows machine* / *CI the-way biegnie na
Linuksie, bo testy wymagające POSIX nie biegną na Windowsie autora*; and *the one command also runs
`check_instructions.py`, a script error stops the tests, a warning does not* / *jedno polecenie
uruchamia też `check_instructions.py`, błąd skryptu zatrzymuje testy, ostrzeżenie nie*.

The settlements stay row by row (rows 1, 2, 4, 6 as sentences of WAY-16, WAY-206, WAY-160; row 3 in
the CI file; row 5 in the block). No projected entry. No invariant written or changed (see below).
No new glossary term, no environment fact (see "Searches not found or unclear").

## Choices of how to make what the task settles (each with the way rejected and its cost if wrong)

1. **The CI file's part: `agent-instructions`.** WAY-44 says "the files that only direct whoever
   carries out its tasks — instructions for agents, skills, hooks and the configuration of agents'
   tools and of CI — are another [part]", and the part's own sentence names the configuration "of CI".
   Rejected: `repository` (files that configure the repository itself). Cost if wrong: one line of
   the part map moves; no code depends on it.
2. **The description for products stands in `installation/README.md`, a new section "Run the one
   command in CI"** (the block points to it by file and section; a test holds that the section
   exists at the pinned commit). Rejected: a file of its own in `installation/` (a second file to
   find where the README already explains how a product uses the pin), and the text inside the
   block (it would stand in every product's `AGENTS.md`, which the Codex limit and the reader both
   pay for). Cost if wrong: moving the section and the one test line.
3. **The workflow checks out the default merge ref of the pull request, whole history (`fetch-depth:
   0`), then `git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/foundations`.**
   `foundation_check.py` takes the main branch from `origin/HEAD` and finds the base by `git
   merge-base HEAD <main branch>` (docstring and `fork_point`); a checkout of a pull request sets no
   `origin/HEAD`, so without the step the script lists "the commit the branch left ... is not known"
   and compares nothing. I checked both states on a local checkout (see Checks). With the merge ref
   as `HEAD`, the merge base is the tip of `foundations`, so the script compares the merged tree with
   the tip it merges onto. Rejected: checking out the head commit of the request (`ref: ${{
   github.event.pull_request.head.sha }}`): it gives the true fork point but tests the branch and
   not the merge, and the checkout cannot fetch the head of a request from a fork; a shallow fetch
   deepened by hand: more steps, no gain. Cost if wrong: the comparison of the foundation in CI
   differs from the cycle's in a case where `foundations` moved after the task branch left it; the
   fix is one line (`ref:`).
4. **Pinned actions:** `actions/checkout` v7.0.1 at `3d3c42e5aac5ba805825da76410c181273ba90b1` and
   `actions/setup-python` v7.1.0 at `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`, both read by `gh api
   repos/<owner>/<repo>/git/ref/tags/<tag>` (the tags point to commits) and both `action.yml` files
   read at those commits (inputs `fetch-depth`, `persist-credentials`, `python-version-file` exist).
   Rejected: tags (a moved tag changes the run). Cost: the pins age; moving them is a change.
5. **`python-version-file: .python-version`** (the runner takes the version the repository declares
   — `3.14`, the latest 3.14.x — not a version written into the workflow, WAY-89).
6. **`concurrency` cancels an earlier run of the same pull request** (group `tests-${{ github.ref
   }}`) because the cycle pushes the record's commit and its removal one after the other, and only
   the run on the last head matters. Rejected: no concurrency (two full runs, ~10 minutes each, one
   of them useless). Cost: an earlier head shows `cancelled`.
7. **`timeout-minutes: 40`**, since the whole gate takes about 16 minutes one directory after
   another. Cost if wrong: a slow runner turns the check red.
8. **The block's fallback sentence now names both checks** ("While the one command does not run one
   of these two checks, run it on its own ..."). The task asked only for the new content, and a
   product that has not yet added `check_instructions.py` (loop2 will, in its own task) needs the
   same fallback as for `foundation_check.py`. Rejected: leave the fallback about the first check
   only (the second check would have no instruction until the product adds it). Cost if wrong: one
   sentence.
9. **The wait in step 12 of the cycle's skill:** after the record's commits are pushed and before the
   request is marked ready; a red result follows step 10's failure (a fix, its review by "The end of
   a code review", the gate again, the record's pair of commits repeated, the wait again); a run that
   does not report is a check that did not run. The host's tool is named as an example (`gh pr
   checks <request> --watch`). Rejected: waiting before the request opens (nothing to wait for:
   the run needs the request), and a fixed timeout in the text (the harness's own wait rules
   already cover it). Cost if wrong: the order of two paragraphs.
10. **The two Linux fixes in `instruction-files/test_check_instructions.py`** (see "Problems"):
    `CommandLine.test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup` patches the
    platform as `NetworkShapesOffWindows` does (it was the one unmarked test that judged a Windows
    network path on every platform); the guard of `NetworkShapesOffWindows` takes the platform it is
    given, so `/net/` and `/Network/` count as network shapes on macOS only; the test
    `test_net_and_network_are_mount_points_of_macos_only` became two tests, one platform each,
    because the guards of two `platform()` calls in one test nest. Rejected: marking the first test
    Windows-only (a skip added to make a check pass, and the sibling already covers Windows),
    changing `check_instructions.py` (it was right: on Linux `\\host\share\x.md` is a file name and
    `/net/` an ordinary directory). Cost: none to the script; the tests got no weaker (the Linux test
    now also asserts that `/net/host/x.md` is looked up).
11. **No invariant written, none changed; no test of the workflow's text.** `ci-checking-commands`
    still reads true (below). A test that parses the workflow would hold the trigger and the `run`
    lines by text; I rejected it because the task asks for no such test and the reviews of this
    request check the workflow's trigger, permissions and steps. Cost if wrong: a later change to
    the workflow is held by review alone.
12. **The root `README.md` and `agent-instructions/README.md` say what is now true about CI**;
    `AGENTS.md` says nothing about CI and so nothing false, and is unchanged.
13. **A row of the record's *Verification* for the CI run** (`task-cycle/record_template.md`, one
    sentence) and the CI result in the request's *Checks* (`request_template.md`): the task asks for
    the description only; the record's *Verification* lists every check the cycle reads, so the CI
    run stands there too. `task-cycle/request_check.py` needed no change: it checks the headings and
    the groups only and `Checks` already needs content or `none`.

## Checks (command and exit code)

Test first:

- `python -B -m unittest discover -s installation -p "test_install.py" -k guidance` → exit 1 before
  `installation/install.py` and the README section stood (two failures, both at their assertions:
  the fragment missing from the guidance, the section pointer missing), exit 0 after (3 tests OK).
- Linux, before the Linux fixes: `docker run --rm --memory 2g -v <copy of 21ecb62>:/repo:ro -w /repo
  python:3.14 sh -c "python -B gate/run_tests.py instruction-files"` → exit 1, 3 failures
  (`CommandLine.test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup` twice, one
  per argument form, and `NetworkShapesOffWindows.test_net_and_network_are_mount_points_of_macos_only`),
  104 tests, 10 skipped. After: exit 0, 105 tests, `OK (skipped=10)`, the 10 being the tests named
  "network paths are looked up only on Windows".

After, on Windows (focused checks of what the change touches):

- `python -B gate/run_tests.py instruction-files` → exit 0 (105 tests, `OK (skipped=5)`).
- `python -B gate/run_tests.py installation` → exit 0.
- `python -B gate/run_tests.py task-cycle` → exit 0.
- `python -B gate/run_tests.py agent-instructions` → exit 0.
- `python -B gate/run_tests.py elements/common` → exit 0 (run twice, the second after the last edit of
  `foundations/decisions.md`; 201 tests OK).
- `python -B elements/common/foundation_check.py` → exit 0 (`0 errors`), also with
  `--skip-test-citations` after the first entry was written → exit 0.
- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` → exit 0
  (`checked: 302 files, 0 listed`, run before the last README edits; the test of `task-cycle`
  that runs the same command passed after them).

After, on Linux (Docker, image `python:3.14` = Python 3.14.10, as user 1001 that is not root, a
read-only copy of the branch at `ddcbfc2`; the evidence is `reports/author-linux-evidence.txt`):

- `python -B gate/run_tests.py <directory>` for `instruction-files`, `task-cycle`, `installation`,
  `agent-instructions`, `elements/common`, `elements/part-map`, `gate`, `relation-model`,
  `process-audit`, `project-level` → each exit 0 (installation 61 tests in 314 s, `OK (skipped=21)`;
  process-audit 182 tests in 216 s). Each ran alone with `--memory 2g`.
- actionlint (`rhysd/actionlint`) on `.github/workflows/tests.yml` → exit 0, no finding.
- A simulated checkout of the pull request (a local clone fetched with `+refs/heads/*:refs/remotes/origin/*`,
  detached head): `python -B elements/common/foundation_check.py` without the `symbolic-ref` step
  lists `foundations/decisions.md: listed: the commit the branch left the main branch from is not
  known, so nothing was compared with it`, exit 0; with the step it lists nothing, exit 0.

Not run, with the reason:

- The whole gate, on Windows or in a container: the orchestrator's alone (handoff).
- The workflow itself on GitHub: nothing was pushed; the first real run is the request's.
- On Windows, the directories `gate`, `relation-model`, `process-audit`, `project-level`,
  `elements/part-map`: this change touches none of their files; they ran on Linux.
- `task-cycle` on Linux as root (the first Docker run, before I used a non-root user): 2 errors in
  `test_remove_merged_worktrees` — see "Problems as observed"; as user 1001 the directory passes.

## Own-work check (WAY-164)

- **Requirement most likely not met:** the acceptance criterion — the CI run on the request runs the
  five tests of `instruction-files/test_check_instructions.py` that Windows skips, instead of
  skipping them.
- **Check:** on Windows `python -B -m unittest discover -s instruction-files -p
  "test_check_instructions.py" -v` lists as skipped for a POSIX reason `LargeAndOddFiles.test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`
  and `LinkChains.test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`,
  `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`,
  `test_an_absolute_link_out_of_the_repository_is_not_read`, `test_every_directory_link_is_reported_wherever_it_points`
  (five); the same command in the Linux container (`-w /repo/instruction-files`, user 1001) gives
  `ok` for each of the five.
- **What it showed:** all five run and pass on Linux. What the check does not show: that the
  workflow's job does the same on a GitHub runner (the first run of the request does).
  The first Linux run also showed three tests of that file failing on Linux, which would have made
  the CI red on its first run; they are fixed (choice 10).

## Trust boundary (the handoff named it: `installation/install.py` and a workflow that takes in a pull request)

My own check of what the reviews will check:

- Trigger: `pull_request`, only into `foundations`. `pull_request_target` appears nowhere (the
  workflow's comment says why). A pull request can change the workflow and so run a changed one
  with the same read-only token and no secret; whether a pull request that edits the workflow may
  satisfy the required check is for the owner's review of that pull request.
- Token: `permissions: contents: read` at the workflow level; `persist-credentials: false` on the
  checkout.
- No secret: no `secrets.` reference. No text of the pull request in a shell command: the only
  expression is `${{ github.ref }}` in the `concurrency` group, outside any `run`; the step that
  sets `origin/HEAD` names `foundations` literally.
- Actions: two, both of `actions/`, both at full commit SHAs with the version in a comment.
- `installation/install.py`: the change is a constant string in `product_guidance`, which takes no
  input; no path, file or subprocess handling changed.
- A crafted-input test of the new reading: none, since nothing new reads input.

## The invariants after the change

- `ci-checking-commands` ("No CI configuration git tracks runs a checking command other than `python
  -B gate/run_tests.py`"): true. The workflow's only checking command is that one; the other steps
  are the checkout, the setting of `origin/HEAD` by `git symbolic-ref` and the install of Python.
- `repository-file-location`: true (`.github/workflows/tests.yml` belongs to `agent-instructions`).
- `python-version-declared`, `script-language`, `script-subprocesses`, `script-imports`,
  `tracked-file-private-paths`, `skill-entry-points`, `instruction-file-imports`: unaffected; the
  tests of those that are tests passed (above).
- WAY-254 (the mutation tool's command stands in no CI configuration) and WAY-34 (a product's CI
  runs only the pinned commit's scripts) are consistent with the new sentences; WAY-254 *narrows*
  WAY-16 and still holds.

## Search of the whole foundation (WAY-33), after the entries were settled

Searched `foundations/` for `CI`, `required check`, `merge request`, `pull request`, `Dependabot`,
`vulnerab`, `advisor`, `alerts`, `installer promise`, `gives no signal`, `run_tests.py`, `GitHub`
and read each entry found whole: WAY-09, WAY-16, WAY-34, WAY-38, WAY-44, WAY-133, WAY-160, WAY-202,
WAY-206, WAY-235, WAY-254; the invariants file whole (the entries filtered of their *Rests on*,
*Derives from* and *Violated* lines); the part map; the glossary; the environment facts by search.
Findings: WAY-09 (the list of what the repository holds) and the part map were corrected; the root
`README.md` (directory list) and `agent-instructions/README.md` were corrected; WAY-16's *Scope* and
*Relations* were corrected. No collision between two decisions. No glossary word in a meaning other
than its entry's.

## Reaches beyond the handoff (what, where, why)

- WAY-33, WAY-148, WAY-243, WAY-03, WAY-10 (`foundations/decisions.md`): the foundation step's search
  and what a changed test must name in the request; WAY-03 and WAY-10 for the invariant-test
  question (no invariant test changed).
- WAY-202, WAY-235, WAY-254 (`foundations/decisions.md`): found by the search for `CI`, `vulnerab`;
  none needed a change.
- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md`, `elements/common/way_of_working.md`, `elements/common/rules.md`
  (first 70 lines): the element's method, to edit WAY-16, WAY-206, WAY-160, WAY-09; the part map's
  `elements/part-map/skill/SKILL.md` for the edit of the map.
- `task-cycle/skill/correction.md` (first 120 lines) and `task-cycle/record_template.md` (lines
  130-200): to see whether the cycle's repeated steps and the record carry the CI result.
- `elements/common/foundation_check.py` (docstring, `fork_point`, `git`), `gate/run_tests.py`
  (docstring), `instruction-files/check_instructions.py` (docstring, `network_shaped`, `main`),
  `task-cycle/test_remove_merged_worktrees.py` (lines 555-620): to find what the CI needs and why
  two directories failed on Linux.
- `gh release list` and `gh api repos/.../git/ref/tags/...`, `.../contents/action.yml` (reads only):
  the versions and commits of the two actions. Docker: the images `python:3.14` (kept) and
  `rhysd/actionlint` (removed) were pulled.

## Working copies

- `.runs/author/clone` (a clone of the base, for the first Linux runs): stood in `.runs/author/`,
  removed (`rm -rf`) before the second Linux run.
- `.runs/author/clone2` (a clone of the branch, read-only mount of the Linux runs, updated by `git
  pull` between runs): stood in `.runs/author/`, removed at the end.
- `.runs/author/sim` (the simulated checkout of a pull request): stood in `.runs/author/`, removed
  at once.
- `.runs/author/` itself (my scripts and outputs), and `.runs/dec.py` (a script that printed a
  decision): removed. What the report needs is kept in `reports/author-linux-evidence.txt`.
- Containers: all ran with `--rm`; `docker ps -a` showed none at the end.
- Remainder: none.

## Unread material

- Decisions of the handoff's lists that I did not read whole: from `task-cycle` — all but WAY-16,
  WAY-33, WAY-34, WAY-09, WAY-148, WAY-160, WAY-243, WAY-03, WAY-10, WAY-44, WAY-55, WAY-89, WAY-100,
  WAY-102, WAY-127, WAY-324, WAY-328, WAY-344, WAY-368, WAY-370 (I did not search the "WAY-286-family"
  decisions on the request description: WAY-287, WAY-288, WAY-289, WAY-161, WAY-162, WAY-300 are
  unread; I changed only the *Checks* paragraph, the cycle's step 12 and the record's *Verification*);
  from `agent-instructions` — WAY-128 to WAY-132, WAY-287 to WAY-289, WAY-308, WAY-309, WAY-320;
  from `gate` — all but WAY-09, WAY-16, WAY-38, WAY-55, WAY-89, WAY-100, WAY-102, WAY-321, WAY-328,
  WAY-344; from `product-guidelines` — all but WAY-202, WAY-206, WAY-235, WAY-254 (`scopes.txt` lists
  58). All the `installation` and `repository` decisions of the handoff: read whole.
- `foundations/invariants.md`: read whole except the lines *Rests on*, *Derives from*, *Violated* of
  each entry (filtered out when I read lines 120-376).
- `foundations/glossary.md`: read whole (the lines "Not" were filtered).
- Files I changed that I did not read whole before changing them: `installation/install.py` (I read
  lines 1-228 and the part I changed; lines 229-685 only by search), `installation/test_install.py`
  (lines 1-60 and the passages I changed), `instruction-files/test_check_instructions.py` (the
  passages I changed and their neighbours, lines 55-125, 495-600, 785-850, 1050-1085),
  `task-cycle/record_template.md` (lines 130-200), `README.md` (lines 95-135), and
  `foundations/decisions.md` (entries only, as the method gives). `task-cycle/request_check.py` was
  searched (`Checks`) and not read; I did not change it.
- `elements/common/rules.md`: lines 1-93 read; `foundations/environment_facts.md`: searched, not
  read.

## Searches not found or unclear

- No source in the task, the foundation or the files for the two claims about the host that the new
  sentences rest on: that GitHub offers alerts of vulnerable dependencies (Dependabot) that a human
  turns on in the repository's settings, and that a branch rule can require a check once it has run
  with a bypass for the owner. The task gives them as facts of its settlements; the foundation has no
  environment fact for either (the template asks for a fact for a citation that, once false, would
  call a decision into question), and I wrote none, since a fact is taken from a source and not
  from memory. The *Based on* of WAY-16 and WAY-206 was left as it was.
- Where the name of a required check is listed in the branch rules (`tests` or `tests / tests`) could
  not be found without a run.
- The handoff names "WAY-286-family decisions about the request description and the final gate"; no
  decision numbered 286 exists in the search I made (`scopes.txt` lists WAY-287, WAY-288, WAY-289 for
  the request description); I did not read them.
- `task-cycle/request_check.py`: whether it needs a change for the CI result: not found any need
  (it checks headings and groups).

## Problems as observed

- **Three tests of `instruction-files/test_check_instructions.py` failed on Linux at the base.**
  Evidence: the Docker run above. Cause, verified by reading the tests and the script and by the
  passing run after the fixes: the tests judged a Windows network path (`\\192.0.2.1\share\x.md`)
  on every platform, and the guard of `NetworkShapesOffWindows` took `/net/` and `/Network/` for
  network shapes whatever the platform, and two `platform()` calls in one test nest their guards.
  Fixed (choice 10); the script is unchanged.
- **`task-cycle/test_remove_merged_worktrees.py`, two tests, fail where the user is root** (observed in
  the first Docker run, which ran as root): `hold_a_file` makes a directory unwritable with `chmod`,
  root ignores it, the removal succeeds, and `holder()` in the `finally` then raises
  `FileNotFoundError` on the removed path before the test can skip ("this system lets a held file be
  removed"). As user 1001 the directory passes, and a GitHub runner is not root, so the CI does not meet
  it; **I left it**: it is a fault of the test only for a root user, no part of this task. For the
  request: it may be set apart as a remark (a `holder()` that tolerates a missing path).
- **The part map's dependencies:** `.github/workflows/**` goes with `agent-instructions`, whose
  *Depends on* lists `gate`; the workflow runs `gate/run_tests.py`, which is no import, so the
  import check holds nothing against it.
- `installation` on Linux takes about 314 s alone; the whole gate on a runner is unmeasured; the
  40-minute timeout rests on the 16 minutes `agent-instructions/README.md` gives for `--jobs 1`.
- The change to `README.md` in `installation` says the CI file of a product must have Python
  `.the-way/.python-version` (WAY-89); the task's item 2 does not list Python among the contents; I
  added it because a job without Python 3.14 fails every product that pins the-way. A reader who
  wants the description to hold only what the task lists can drop item 4 of the section.

## Questions

None. (No open design choice stood; the status is `done with concerns` for the two sourceless claims
and the root-only test above.)
