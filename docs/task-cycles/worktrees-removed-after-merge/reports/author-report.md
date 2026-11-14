# Author report — worktrees removed after merge

**Status:** done

Branch `task/worktrees-removed-after-merge`, base `835344fb183fce6dbd99be486df790f1212cacf6`.

## Commits and files

| Commit | What |
|---|---|
| `9fe7f66` | Add the script that removes the working directories of merged tasks |
| `25daf50` | Record the removal of the working directories of finished tasks |
| `a849408` | Run the removal of working directories at the start of a cycle |

Files (added / removed lines, `git diff --numstat 835344f..HEAD`):

- `task-cycle/remove_merged_worktrees.py` — new, 530 / 0.
- `task-cycle/test_remove_merged_worktrees.py` — new, 617 / 0; 42 tests.
- `foundations/decisions.md` — 106 / 10: WAY-298 edited in place; WAY-375 and WAY-376 added.
- `task-cycle/skill/SKILL.md` — 31 / 12: the three places the task names, plus step 5 and step 14.
- `task-cycle/record_template.md` — 3 / 0: the item *Directories of earlier tasks kept* in *Request handoff*.
- `task-cycle/skill/request_template.md` — 7 / 2: a sentence under *Cost* and a clause under *Checks*.

## Checks run (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest task-cycle.test_remove_merged_worktrees` | 0 | 42 tests OK, 51 s |
| `python -B gate/run_tests.py task-cycle` | 0 | 436 tests OK (the same run, before the last two tests were added: 434 tests, exit 0) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (run without `--skip-test-citations`) |
| `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` | 0 | nothing listed |

Not run: the product's full gate (`python -B gate/run_tests.py` without a directory), as the handoff says.
An earlier `foundation_check.py` run exited 1 with one error (`WAY-376` held by nothing) because the new
test file was untracked; it exited 0 after `git add` of the two new files.

### Tests written after the code, and the breaks they catch

The tests were written after a first version of the script, not before it (the task is a script over git
state, and I explored its output on the real repositories first). In place of a failing-first run I ran
20 mutations of the script against the tests (a throwaway driver, `python -I .runs/author/mutate.py`, exit 0,
removed afterwards). Each mutation was applied alone, the named tests run, the script restored:

| Mutation of the script | Result |
|---|---|
| `--first-parent` dropped from the merge listing | caught |
| second parent read as the first parent | caught |
| link check on the listed path dropped | caught |
| "git reads it as a checkout of this repository" always true | caught |
| status of the tree ignored | caught |
| "commits on the remote" always true | caught |
| ownership by the prefix `task/` alone | caught |
| protection of the directory the script runs in and holds dropped | caught |
| nested checkouts no longer block their parent | caught |
| `.runs/` not skipped in the ignored listing | caught |
| known caches not skipped | caught |
| exit code 1 on a failed removal dropped | caught |
| order of removal made parent first | **survived** — see below |
| main checkout not protected | caught |
| retry with `--force` for a populated submodule dropped | caught |
| fetch dropped | caught |
| base copy not required to stand directly under `.runs/` | caught |
| merge of the task named by a base copy not required | caught |
| the script deletes the branch after removal | caught |
| `git fetch --prune` | caught (by the test added after the first batch) |
| a failed nested removal no longer stops its parent | caught (the same) |

The one survivor, the order of removal, is an equivalent mutation with this git (2.55.0): git also
removes the registration of a nested checkout whose directory a parent's removal already took, so the
outcome is the same in either order. The order stays as a precaution against a git that differs; no
test can tell it apart here.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** item 3 of *To do* and the settlement of row 2 — a branch is merged
  only where its tip is the second parent of a merge commit on the target branch, and no directory is
  removed that is not a clean, pushed, merged cycle directory; with the real repository of the-way (94
  entries in the task's reading) as the place where a wrong reading would show.
- **Check:** a read-only dry run on the real repository, `python -B task-cycle/remove_merged_worktrees.py
  --repository <the main checkout of the-way> --no-fetch` (exit 0), then an independent recomputation
  with a separate throwaway script that shares no code with the script: for every worktree standing on a branch,
  `git log --first-parent --merges --format=%P origin/foundations` for the second parents, `git status
  --porcelain`, `git for-each-ref --contains` and the record directory, compared with the script's
  `remove` or `keep`.
- **Showed:** 80 of 80 worktrees on a branch agree (the worktree of this task and the main checkout left
  out); no mismatch; 79 of them are marked `remove`. The script marked 88 directories `remove` in all
  (the 79 on a branch and 9 detached: 6 loose base copies and 3 nested ones) and kept, among others, `the-way-global` and `the-way-fullrun` (detached,
  outside a cycle), the directory of a session's scratchpad (changes, outside a cycle), the closed
  unmerged task directory (`task/agent-path-to-running-product`: no merge git can see) and two loose base
  copies whose names give no branch (see the questions table). A dry run on the second repository (`loop2`,
  a product, `--no-fetch`, exit 0) marked 41 for removal and kept the directories with changes, unpushed commits, a nested scratch
  checkout with changes, and the branches `10x/…`, `trial/…` and `chore/…` that are outside a cycle. The dry
  runs removed nothing and changed no ref (`--no-fetch`); the list of worktrees of the-way before and after
  holds the same 96 entries.
- Never run: `--apply` against a worktree of this machine. Every `--apply` of the tests and of my hand
  trials was in a throwaway repository, in the system's temporary directory (the tests) or under
  `.runs/author/` (hand trials of git's behaviour with a junction and a submodule).

## Foundation entries (foundation step)

Searched the whole foundation (WAY-33) for `worktree`, `fast-forward`, `working copy` and `outside the
task's worktree`, and read WAY-298, 373, 140, 153, 269, 314, 148, 48, 328 whole, and also WAY-38, 89, 127,
227, 308, 344 and 296 whole. Found: WAY-298 carries the sentence the task changes (only place that says
"the one change"); `.claude/…` entry points and the part map need no change (the script is in
`task-cycle/**`, not a trust boundary by the orchestrator's answer); WAY-373, WAY-140, WAY-153 and WAY-269
stand unchanged and WAY-375 derives from them.

| Entry | Row | Meaning in English | Meaning in Polish |
|---|---|---|---|
| WAY-298 (sentence edited, one clause added to its pair of examples, *Rationale* price) | row 1 | The fast-forward, made only in the-way itself, and the removal of finished tasks' working directories that every new cycle runs at its start are the two changes the cycle makes to checkouts outside the task's worktree. | Fast-forward, robiony tylko w samym the-way, i usuwanie katalogów roboczych zakończonych zadań, które każdy nowy cykl robi na starcie, to dwie zmiany, jakie cykl robi w checkoutach poza katalogiem zadania. |
| WAY-375 | rows 2, 4 and 5 | At its start a cycle removes an earlier task's working directory only when its tree is clean, all its commits are on the remote, its branch is merged (tip is the second parent of a merge on the first-parent history of the remote target branch, by git alone) and it belongs to a cycle; it touches only checkouts git names, never a branch, and what it removes outside the repository's own directory is no effect outside the repository in the sense of WAY-140. | Na starcie cykl usuwa katalog roboczy wcześniejszego zadania tylko, gdy drzewo jest czyste, wszystkie commity są na zdalnym, gałąź jest scalona (czubek jest drugim rodzicem scalenia na pierwszorodzicielskiej historii zdalnej gałęzi docelowej, samym gitem) i katalog należy do cyklu; rusza tylko checkouty wymieniane przez git, nigdy gałęzi, a usunięcie poza katalogiem repozytorium nie jest skutkiem poza repozytorium w rozumieniu WAY-140. |
| WAY-376 | row 6 | A file git ignores does not count against a clean tree, and before the removal the script lists each directory's ignored paths outside `.runs/`, known caches left out. | Plik ignorowany przez git nie liczy się do czystego drzewa, a przed usunięciem skrypt wypisuje przy każdym katalogu jego ignorowane ścieżki poza `.runs/`, pomijając znane cache. |

Row 3 (the list of kept directories goes to the record and to the description by the route of WAY-373) went
to its place: `task-cycle/skill/SKILL.md` step 4, the item *Directories of earlier tasks kept* of
`task-cycle/record_template.md`, and `*Cost*` and `*Checks*` of `task-cycle/skill/request_template.md`; no
entry was written for it. No entry is marked `the cycle's`, but see the questions table for two wordings
that are mine: the words "first-parent history" in WAY-375 (the row says "on the target branch") and the
`.runs/`-directory part of WAY-376.

Glossary: I judged that "merged branch", "base copy" and "belongs to a cycle" need no glossary entry
(WAY-95): WAY-375's own sentence defines "merged" where it is used, and no sentence reads differently for a
reader who knows git's field.

## Questions table — choices of how to make what the task settles

| # | Choice | Way rejected | Cost if wrong |
|---|---|---|---|
| 1 | Name and place: `task-cycle/remove_merged_worktrees.py`, test `task-cycle/test_remove_merged_worktrees.py`; run from the root of the repository (in a product, `.the-way/task-cycle/…`) with `--repository` defaulting to `.`. | A name that says "cleanup" for any directory, or a place outside `task-cycle/` (the part map's `task-cycle/**` already covers the file). | A rename: one path in step 4, the test, two decisions' tests lines. Small. |
| 2 | How a task branch is told from another: a worktree on a branch is a cycle's where the branch begins `task/` **or** its directory holds `.runs/task-cycles/`, the record directory of a cycle. The real `s7-cycle-remarks` is found by the record directory. | The prefix alone (misses `s7-cycle-remarks`); the record alone (misses a directory made at step 4, before the record exists at step 5); reading the branch name out of the merge commit's subject (it is a host's wording). | A directory of a cycle on an unprefixed branch with no record stays for the human (wrongly kept, never wrongly removed). A human's own directory with a `.runs/task-cycles/` in it is judged too, and only a clean, pushed, merged one is removed. |
| 3 | Merged = tip is the second parent of a merge on the **first-parent** history of the target (`git rev-list --first-parent --merges --parents`). | All merges of the target's history: the merge of the target into a task branch makes a target commit a second parent, so a fresh branch at that commit would count as merged (test `…merge_of_the_target_into_a_task_branch…`). | A branch merged into the target by a side route that is not a first-parent merge (a fast-forward, a merge made on another branch) is not recognised and stays: kept, never wrongly removed. |
| 4 | Order of removal of nested directories: the deepest first; a directory is removed only when every checkout inside it is detached, clean, on the remote, and each nested one is removed with it, **whatever its name**; otherwise the directory stays, naming what it holds. A nested checkout on a branch always keeps the parent. | The name rule for nested ones too (`base-check*`): it would keep a task directory for a clean, pushed scratch checkout, which loses nothing when removed; letting git remove the parent and its nested directories as plain files (leaves registrations and could delete uncommitted work in the nested checkout). | The stricter reading is item 4 of the task read to the letter ("`base-check-*` nested in the task directory vanish with it"); mine removes also other clean, pushed, detached nested checkouts. Nothing uncommitted or unpushed is lost either way. If the orchestrator wants the stricter rule, it is one line in `Cleanup.judge`. |
| 5 | A directory locked by another process (Windows): no retry, no force, no kill; `git worktree remove` fails, the script prints a `failed` line with git's message, exits 1, goes on to the other directories, and lists the directory for the human with the fixed reason "removal failed; see the output of the script" (no git message, which carries a path). A parent of a nested checkout that failed is skipped. A removal that exits 0 but leaves the directory standing counts as failed. | A retry loop with a wait; `--force` or `-f -f`; a removal by the script's own `rmtree`. | Git may leave a directory partly deleted after a failure; a later run then reads it as unclean and keeps it, for the human. A directory held by an editor stays one more cycle. |
| 6 | Broken registration: a directory that is missing (git's `prunable`) is kept with "`git worktree prune` removes the registration"; a directory whose `.git` is gone or points into another repository is kept ("git does not read it as a checkout of this repository": its toplevel and `--git-common-dir` must equal the directory and the repository's); the listed path being a symbolic link or a junction is kept. | `git worktree prune` by the script (it also forgets a directory on a drive that is not connected); judging the directory by the repository above it. | A stale registration stays until the human prunes. |
| 7 | The exact rule of the name of a loose base copy: a detached checkout standing directly under a directory named `.runs` and named `base`, `base-check`, `base-fix`, `base-check-<task>` or `base-fix-<task>` (`<task>` is `[A-Za-z0-9][A-Za-z0-9._-]*`). A copy named for a task is removed only where the branch `task/<task>`, each of the local and the remote-tracking one that exists, is merged; a copy named for no task (`base`, `base-check`, `base-fix`) and a copy whose branch is not found never stand alone. | Any detached copy under `.runs/` (may be a copy of a cycle running now); a fuzzy match of the name to a branch (a wrong match removes a running cycle's copy). | Two of the eight loose copies in the real main checkout stay for the human: `base-check-stage-remarks` (its task branch is `task/stage-remarks-check`) and `base-fix-minor-findings` (its branch is `task/fix-minor-findings`). The dry run lists both under the cycle's list with the reason "the branch … its name gives is not found". |
| 8 | Known caches left out of the ignored listing: `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.cache`, `.tox`, `.nox`, `.venv`, `venv`, `node_modules`, `dist`, `build`, `.next`, `.nuxt`, `.turbo`, `.parcel-cache`, `coverage`, `.gradle`, `target`, `.DS_Store`, `Thumbs.db`, and `*.pyc`; the listing shows 12 paths a directory and counts the rest. `.superpowers`, `.claude/settings.local.json`, `.stryker-tmp` and `.playwright-cli` are shown. | Skipping every ignored directory at the top level; skipping nothing (52 `node_modules` in `loop2`). | A directory named like a cache that holds something made by hand (`build`, `target`, `dist`) is removed without being shown. |
| 9 | An option `--no-fetch` (not in the task): the script judges by the remote-tracking refs as they stand. | No such option: the dry run on the real repositories would have moved their remote-tracking refs, which the orchestrator forbade. | The option can only make the script keep more (a merge not yet fetched is not seen; a push not yet fetched looks unpushed); never remove more. |
| 10 | The target branch: `--target BRANCH` on the remote, else the branch the remote's `HEAD` names, else `main`, else `master`; the remote is `--remote`, default `origin`. Step 4 passes `--target <target branch>`. | A target taken from the checked-out branch of the main checkout. | None while the remote's `HEAD` is right; a wrong `--target` makes the script find no merge and keep everything. |
| 11 | Exit codes: 0; 1 with `--apply` when a removal failed or left the directory standing; 2 for the script's own failure (no repository, no target branch, a failed fetch) with nothing judged and nothing removed. | Exit 1 for any directory that stays. | The orchestrator reads exit 1 as a failed removal only. |
| 12 | Output: one line per directory `remove|keep <path> [<branch or detached>] <reasons>`; under a `remove` its ignored paths; a closing list `- <name> | <branch> | <reason>` of the cycle's directories that stay, with no absolute path, which the cycle copies. A directory the script runs in is left out of that list (it is not a decision for the human). Output is UTF-8. | A JSON output. | The orchestrator copies lines by hand from text. |
| 13 | The foundation entries: rows 2, 4 and 5 as one decision (WAY-375, one question: which directories, and what the script touches), row 6 as a second (WAY-376, one question: do ignored files keep a directory), row 1 as the edit of the sentence of WAY-298. | Four decisions, one per row. | A reviewer may want row 5 (WAY-140's boundary) as its own entry; moving the second paragraph of WAY-375 into a new decision is a small edit. |
| 14 | Where the script runs in step 4: after the fast-forward (in the-way itself) and before the task branch is created, also where step 2 moves the pin (that path creates the branch by step 4's rules). The skill says an exit code other than 0 stops nothing. | Running it at the start of step 4's first question; running it in step 5 with the record. | If the script's exit is 2 offline, the cycle's own fetch will have failed already. |
| 15 | The record and the description: a new record item *Directories of earlier tasks kept*, a sentence under *Cost* and the lines under *Checks*; *For you to decide* has no item for it. | A section of its own in the record; an item of *Fix or let through* (nothing in the request waits for the human's yes). | A request carries the lines again each time something stays; the human may find them noise. |

## Reaches beyond the dispatch

- WAY-38, WAY-89, WAY-127, WAY-227, WAY-296, WAY-308, WAY-344 and WAY-95, each whole, in
  `foundations/decisions.md`: WAY-38 and WAY-89 because the change is a script of the-way, WAY-127 for how a
  session reads a skill from its worktree, WAY-227 for where the human meets the cycle's work, WAY-296 for
  the form of the process remarks next to the record item I added, WAY-308 for the list that goes to a
  published description, WAY-344 for the rule on a file a script reads (the script reads no file an agent
  writes, only git's output and whether a directory exists, so no field check applies), WAY-95 for the
  glossary judgment. Found by the list of decisions whose *Scope* names `task-cycle` (137 entries, printed by
  a throwaway script), selected by title.
- The part map's `task-cycle`, `repository` and *External context* entries, and, each whole, for writing
  WAY-375 and WAY-376 (the foundation step names the element's `SKILL.md`):
  `elements/decisions/skill/SKILL.md`, `elements/decisions/skill/read.md`,
  `elements/decisions/skill/decide_entry.md`, `elements/decisions/template.md`,
  `elements/common/rules.md` and `elements/common/way_of_working.md`.
- `task-cycle/private_paths_check.py` (docstring and patterns) to keep the new files free of what it lists;
  `elements/common/foundation_check.py` (its docstring) for the form of a line `decision:`.
- `agent-instructions/README.md` and `AGENTS.md`: read for the integration route.

## Unread material

- WAY-286, WAY-287, WAY-289, WAY-290 and WAY-309: not read as entries; their content reached me only through
  `task-cycle/skill/request_template.md` (read whole) and, for WAY-309, the docstring of
  `private_paths_check.py`.
- The decisions whose *Scope* names `task-cycle` beyond the ones I name above and in the handoff (about 120
  of 137): by title only; none of them names the cycle's start, working directories or the record's request
  handoff by its title.
- `elements/decisions/examples.md`: not read (the template's examples are the entries I read, WAY-373 and
  WAY-298 among them).
- `task-cycle/request_check.py` and `task-cycle/test_request_check.py`: not read; the template says the check
  judges only headings and "content or `none`", so I did not open them.
- `task-cycle/test_tracked_files_private_paths.py`: read whole.

## Searches not found or unclear

- none

(Items that stand out but are not "not found": the task's item 8 names "the way WAY-373 leads a remainder of an
agent", which sets the record's *Working copies left* and the description's *Cost* and *Checks*; I read it
as a route and made a new record item beside the old one rather than widening *Working copies left*, which
names the agent and the repository-root path of a working copy.)

## Concerns and values that do not pass my reckoning

- The task's context counts 94 entries on the author's disk "that the cycle counts again"; `git worktree
  list` now gives 96, the main checkout and this task's own worktree among them, and the script marks 88
  `remove`. The counts differ because the disk changed since (the task itself says so); the task's own
  split (78 task directories, 11 base copies) I did not reproduce exactly.
- Two of the 8 loose base copies are kept for a name that gives no branch (choice 7). The human clean-up
  at the request will see them in the dry-run list.
- A directory that git has removed from its list but leaves standing (seen once, with a junction in a
  checkout in a hand trial: git exited 0 and left an empty `.runs/`) is reported by the script as a
  failed removal; I did not find the reason inside git and do not claim one.

## Working copies

- `.runs/author/` of the task's worktree: hand trials of git's behaviour (a junction inside a checkout, a
  populated submodule, the format of `git worktree list --porcelain -z`), the mutation driver, the outputs
  of the dry runs and of the focused checks. Removed with `rm -rf` before this report; the directory is
  gone (`ls .runs` shows only `task-cycles/`), `git worktree list` holds the same 96 entries as before,
  and no worktree was registered by me in the real repository.
- The tests' own temporary repositories (`tempfile`, system temporary directory) are the files that a
  product's tests make by themselves and are removed by the tests.
- Remainder: none.
