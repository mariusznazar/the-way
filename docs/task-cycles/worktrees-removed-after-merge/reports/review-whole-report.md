FAIL a849408fade7f5454a2a1535fc14ee364a0fa7bf

# Review of the whole change — worktrees removed after merge

Range `835344fb183fce6dbd99be486df790f1212cacf6..a849408fade7f5454a2a1535fc14ee364a0fa7bf` (`git rev-parse HEAD`
confirmed `a849408…`), three commits of one author, no spec, no plan, no slices. Judged against
`.runs/task-cycles/worktrees-removed-after-merge/task.md`.

Counts: blocking 1 (Important), Minor within the task 5, out of scope 0 (and 4 lines under Declined to judge).

## Findings

### Important (blocking, within the task)

**I1. The script's "clean tree" is weaker than git's own check, and its `--force` retry then removes uncommitted work of a populated submodule.**

- Place: `task-cycle/remove_merged_worktrees.py:328` (`git status --porcelain -z --untracked-files=normal`) and `:421-427` (`remove_entry`, the retry with `--force`).
- What is wrong: git's own check in `git worktree remove` is `git status --porcelain --ignore-submodules=none`. The script's status honours the repository's configuration, so a submodule declared `ignore = all` (or `dirty`, `untracked`) in `.gitmodules` or `.git/config` shows no change in it. For any checkout holding a populated submodule git refuses first with its submodule message (before its own dirt check), the script then retries with `--force`, and `--force` skips git's dirt check altogether. In a product every task directory holds a populated `.the-way`, so in a product the removal runs forced as the normal path, and the only guard against loss is the script's weaker status.
- Evidence (my own run, a throwaway repository under `.runs/review-whole/`, now removed; the driver is kept as `reports/review-whole-submodule-check.py`): a merged, pushed task directory with a populated submodule whose `.gitmodules` entry has `ignore = all`, with `UNCOMMITTED WORK` written into a tracked file of the submodule and a new untracked file in it. `git status --porcelain` printed nothing; `git status --porcelain --ignore-submodules=none` printed ` M .the-way`. The script with `--apply` printed `remove … clean, on origin, branch merged` and `removed`, and the directory was gone: the uncommitted work went with it. The test `test_a_populated_submodule_does_not_keep_a_clean_directory` (`test_remove_merged_worktrees.py:494`) covers only a submodule with no configuration, where both statuses agree, so it cannot show this.
- Why it matters: the task item 2 and the rule of row 2 make "tree clean" a condition of an irreversible removal, and the orchestrator's answer asks me to check that the script removes only what the rule allows. WAY-375 says a tree "is clean (WAY-376)" and that the script "keeps what it cannot place". A repository that hides submodule changes in its status (a common setting to quiet a pinned submodule) loses work silently. The loss needs that setting, but the fix is one flag and the operation cannot be undone.
- Fix: pass `--ignore-submodules=none` in `inspect_state`'s status (and so also for nested checkouts); add a test with `ignore = all` and a changed file in a populated submodule that expects `keep`. Keep the `--force` retry only after that.

### Minor (within the task)

**M1. The `--force` retry is triggered by the word "submodule" anywhere in git's message, which includes the directory's path.** `remove_merged_worktrees.py:424` (`b"submodule" in done.stderr.lower()`). Git's refusal for a changed tree reads `fatal: '<path>' contains modified or untracked files, use --force to delete it` (I reproduced it: the message carries the path). A task directory named for a task such as `fix-submodule-handling`, or any ancestor directory with that word, makes every refusal git gives — a file created between judging and removing, a state git sees and the script's status does not — retry with `--force`. Match git's own submodule sentence ("working trees containing submodules cannot be moved or removed") or look for submodules before the first call, not the whole message. Related to I1 and cheap to fix with it.

**M2. The script's fetch prunes remote-tracking refs where the user's configuration says `fetch.prune`; the docstring, the test and WAY-269 say it must not.** `remove_merged_worktrees.py:220` (`git fetch --no-tags <remote>`), docstring `:16` ("never `--prune`"), test `test_the_fetch_does_not_prune_the_remote_tracking_branches` (`test_remove_merged_worktrees.py:543`, which sets `GIT_CONFIG_GLOBAL` to the null device, so it cannot see the configuration). Evidence: in a throwaway repository with `git config fetch.prune true`, a branch deleted on the remote was gone from `refs/remotes/origin/` after one dry run of the script (my run, removed). WAY-269's *violates* line names `git fetch --prune` taking away the evidence of other tasks' closed requests, and WAY-153's reader reads that evidence. The cycle's own step-4 fetch has the same exposure, so this does not make the cycle worse than it is, but the claim of the script and the test is not true. Add `--no-prune` to the fetch, and make the test set `fetch.prune` in the repository's configuration.

**M3. WAY-375 leaves out two rules the code applies, so the entry and the files differ (WAY-263, graded Minor because the entry is silent, not contradicted).** `foundations/decisions.md:12950-13016` against `remove_merged_worktrees.py:349-364` and `:371-386`. (a) A nested detached checkout in a removed task directory goes with it whatever its name; the entry's ownership condition ("standing on a task's branch or being a detached copy of a base") does not mention nested checkouts, and the task's item 4 names only `base-check-*`. I judge the code right (choice 4 below), the entry must say it. (b) "A task's branch" is told by the `task/` prefix or by a record directory `.runs/task-cycles/` in the checkout; the entry says only "a task's branch", which a reader reads as the prefix, and the task itself says the prefix is not enough (*Questions carried to cycle*). One sentence for each in the first paragraph of WAY-375, or the request's *Foundation entries* marks them as the cycle's own.

**M4. A reason in the list "for the human" can carry an absolute path.** `remove_merged_worktrees.py:330` puts `first_line(status.stderr)` after `git cannot read its state:`; git's messages for a broken checkout normally name the path. That reason reaches the line `- <name> | <branch> | <reason>` that the cycle copies into the record and the description, whose item 8 and WAY-375 say "no absolute path" (and `private_paths_check.py` would then list it). Not reproduced (I could not make `status` fail after `reads_as_checkout` passed); found by reading. Replace the message with a fixed text, as the author did for a failed removal.

**M5. Two behaviours the task names have no test.** No test makes the listed path a Windows junction (the one test of a link, `test_a_listed_path_that_is_a_link_is_kept`, uses a symbolic link; `is_link` also calls `os.path.isjunction`). I ran it by hand in a throwaway repository: a merged directory replaced by a junction to a moved copy was kept with "its path is a symbolic link or a junction" and the copy was intact. And there is no test for I1. Add both.

### Out of scope

none.

## Declined to judge

- The part map's trust-boundary list (`foundations/part_map.md:101`) does not name the script: that is the orchestrator's answer of step 4 (WAY-48: the script takes in names from the product's own git state), not an item of the task; I applied the irreversible-operation check to the script all the same.
- The two loose base copies kept because their names give no branch (`base-check-stage-remarks`, `base-fix-minor-findings`): a copy whose branch is deleted or named differently can never be matched, so it stays and is listed at every cycle; the task's rule ("name points to a task with a merged branch") gives that, and the one-time cleanup by the human covers the existing ones.
- `task-cycle/skill/correction.md:7` says a correction fast-forwards "as step 4 gives", and step 4 now also holds the removal: SKILL step 4 and WAY-298 both say a correction does not run it, so I leave the sentence as consistent.
- Size and structure (WAY-362, WAY-363): the-way has no `guidelines/coding.md` rule of size (WAY-328), so any such finding would be Minor; the numbers are below and I name none.

## Choices of the author that the orchestrator asked me to judge

1. **Choice 4 — a nested detached, clean, pushed checkout goes with its task directory whatever its name.** Accepted. The task's *Need* 4 is that the agents' copies of WAY-373 "vanish with the task directory", and those are nested detached checkouts of arbitrary names (a reviewer's worktree under `.runs/<role>/`), so a `base-check-*` name rule would keep every task directory that holds one and defeat the task. Item 5's "never detached directories outside the cycle" is about detached directories that stand on their own; a checkout inside a cycle's directory is inside the cycle. Nothing uncommitted or unpushed goes (the parent stays where a nested checkout has changes, unpushed commits, a branch or a lock; the tests `test_a_nested_checkout_*` hold that). It departs from the letter of item 4, so the entry must say it (M3).
2. **Choice 7 — loose base copies whose names give no task branch stay.** Accepted: it is the task's rule applied exactly (`base-check-<task>` / `base-fix-<task>` to `task/<task>`, merged on each of the local and remote-tracking refs that exist). It errs only toward keeping. The real run keeps `base-check-stage-remarks` and `base-fix-minor-findings` and lists them.
3. **Choice 9 — the option `--no-fetch`, not in the task.** Accepted. It is needed for the read-only dry runs the cycle's own reviewers are told to make, is documented, tested (`test_the_merge_pushed_by_another_clone_is_seen_after_the_fetch_only`), and step 4 never passes it. Judging by stale remote-tracking refs can only keep more in every case I could build (an unseen merge keeps; an unseen push keeps), and removal never deletes commits (git keeps the objects). The docstring's "can only make it keep" is true enough.
4. **Choice 13 — rows 2, 4 and 5 as one decision (WAY-375).** Accepted, with no finding. `elements/decisions/skill/decide_entry.md` allows two entries "or keep the question the rest serves", and "never a branch" and "git-named checkouts only" serve the one question "which directories does the cycle remove". The WAY-140 sentence is the row 5 boundary and is findable only through WAY-375's second paragraph; a later reader looking for "may automation remove directories beside the repository" would not guess that title, but the entry cites WAY-140 in *Relations*, in *Verification* and in the *Rationale*.
5. **"first-parent history" in WAY-375.** Accepted and needed. The task's own *Not chosen* for the weaker test ("a branch just made by a parallel cycle would pass as merged") applies equally to a merge of the target into a task branch, which makes a target commit the second parent of a merge that is not on the target's first-parent history; `test_the_merge_of_the_target_into_a_task_branch_makes_no_branch_merged` fails when the first-parent flag is dropped. It errs only toward keeping. The entry states it with its reason in the *Rationale*.
6. **The `.runs/` part of WAY-376.** Accepted. Item 2 and the *Answer* say ignored files do not count and item 6 says the listing leaves out `.runs/`; WAY-376 says exactly that (`list_ignored` skips a top-level `.runs/` only). Row 6's text "Pliki ignorowane poza `.runs/` nie liczą się do 'czyste'" read to the letter would count an ignored file inside `.runs/` — which holds the cycle's own record; the answer is the intended reading and the code and the entry follow it.

## Coverage of the task

**To do**

| # | Verdict |
|---|---|
| 1 dry run by default, `--apply` removes | Met (`remove`/`keep` with reasons; exit 0; `--apply` only runs `git worktree remove`). |
| 2 all conditions at once | Met as far as I1 allows: clean, on the remote, merged, belongs to a cycle; ignored files do not count. I1 is the gap in "clean". |
| 3 merged = second parent of a merge on the target, git alone, fetch first | Met (`merged`, `fetch`); `--no-fetch` added (choice 3); fetch prunes under configuration (M2). |
| 4 `base-check-*` nested vanish, loose by name | Met and broadened for nested ones (choice 1, M3); loose rule exact (choice 2). |
| 5 only what git lists; never main, the directory it runs in, outsiders, branches | Met: main, bare, cwd/top/script directory, link or junction, missing, unreadable, locked, foreign detached all kept; no branch command anywhere. I checked on the real repository: `the-way-global`, `the-way-fullrun`, the session's scratchpad copy kept. |
| 6 reasons for everything kept; ignored paths outside `.runs/` minus caches | Met. One combined reason covers "not merged / open / closed / squash" (git cannot tell them apart; the *Answer* names the reason "scalenie niewykrywalne gitem"). |
| 7 step 4 runs `--apply`; exception in the paragraph; correction does not run it | Met (`SKILL.md:75-81`, `:129-148`). |
| 8 list to the record and the request by the route of WAY-373, name/branch/reason, no path | Met (`SKILL.md` steps 4, 5, 14, `record_template.md:202-204`, `request_template.md` *Cost* and *Checks*), except M4. |
| 9 "Keep the worktree for corrections." kept with the addition | Met (`SKILL.md:568-569`). |

**Settlement rows** — 1: WAY-298 edited in place and consistent with its *Verification* and *Rationale*. 2, 4, 5: WAY-375. 3: `SKILL.md` and the two templates. 6: WAY-376. All six met; the wording differences are in M3.

**Answers under *Questions to settle*** — 1 (who and when; any product; `the-way-global` skipped): met. 2 (which directory): met (closed-PR directory kept: `task/agent-path-to-running-product` on the real run). 3 (merged): met. 4 (one-time cleanup by the human at the request): the script supports it (`--repository`, dry run by default, usable from the task's worktree on the other repository); the human action belongs to the orchestrator's request, not to the commits. 5 (where the list lands): met. 6 (directories beside the repository): met, with WAY-375's second paragraph. 7 (ignored files): met.

**Places of `SKILL.md` that *Context* names** — the paragraph "The cycle writes only in the task's worktree", step 4 and the end of step 12: all three changed as the task says; steps 5 and 14 added (inside the task's purpose, the list needs a place to land).

**Request template, record template and the three checks (the orchestrator's gap).** I read `request_check.py` whole. It judges headings in order, the state line, content-or-`none` per section, the decision groups and the collapsed block's language; it reads no sentence of *Cost* or *Checks*, so the template's new sentence and clause pass it. I made a description from the template (with the new *Cost* sentence and a *Checks* line holding the kept-list format) and a task document: `request_check.py` exit 0 (`form holds`), `private_paths_check.py` exit 0 (`0 listed`). I made a record directory whose *Request handoff* holds the new item and ran `remarks_check.py` on it: exit 0 (the item starts no block the nightly cut reads, and sits before *Process remarks on the-way*). The new item, its line under *Cost* and under *Checks* follow the route of the neighbouring *Working copies left* line (WAY-373) and WAY-296's form is untouched. The record item names "the script of step 4"; the template carries no stale reference.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 835344f… HEAD` (exit 0): `foundations/decisions.md` 12991 → 13087 (+96); `task-cycle/record_template.md` 231 → 234 (+3); `task-cycle/remove_merged_worktrees.py` added, 530; `task-cycle/skill/SKILL.md` 698 → 717 (+19); `task-cycle/skill/request_template.md` 513 → 518 (+5); `task-cycle/test_remove_merged_worktrees.py` added, 617. The-way holds no `guidelines/coding.md` with a rule of size (WAY-328), so there is no threshold test to run; I read the new functions: the longest is `Cleanup.judge` (about 25 lines) and `run` (about 23); no code without a user (every name is read); no name that stopped being true (`SKILL.md`'s "Keep the worktree" sentence was updated). No finding of structure.

## Checks I ran (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` (reviewed worktree) | 0 | 436 tests OK, 77 s |
| `python -B -m unittest task-cycle.test_remove_merged_worktrees -v` | 0 | 42 tests OK, 46 s, none skipped (symbolic links work here) |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` and `.../record_template.md` | 0 | `0 listed` each |
| `python -B task-cycle/change_file_sizes.py 835344f… HEAD` | 0 | table above |
| `python -B task-cycle/remove_merged_worktrees.py --no-fetch` from the reviewed worktree, against its own repository (dry run) | 0 | 96 entries before and after (`git worktree list`), nothing removed: 88 `remove`, 8 `keep`; it kept the main checkout, this worktree, `the-way-global`, `the-way-fullrun`, the scratchpad copy, the closed-unmerged task directory and the two unmatched loose base copies; the 79 task directories and 9 detached copies marked `remove` are the author's count; output kept in `reports/review-whole-dry-run-output.txt` |
| `python -B task-cycle/request_check.py <made description> --task <made task>` | 0 | `form holds` |
| `python -B task-cycle/private_paths_check.py <made description>` | 0 | `0 listed` |
| `python -B task-cycle/remarks_check.py <made record directory>` | 0 | `0 not in the process remarks` |
| `python -B .runs/review-whole/drv_submodule.py` (throwaway repository; kept as `reports/review-whole-submodule-check.py`) | 0 | shows I1: the directory with uncommitted submodule work was removed |
| by hand, throwaway repositories under `.runs/review-whole/` (PowerShell): a junction inside a worktree pointing to a directory outside; a listed path replaced by a junction; `git worktree remove` of a directory named `fix-submodule-handling` with an untracked file; `fetch.prune true` with a branch deleted on the remote | — | git removed the junction and left the target intact (and left the emptied directory standing, which the script reports as failed); the junction path was kept by the script; git's refusal message carries the path; the fetch pruned the ref (M2) |

Not run: the product's full gate (the orchestrator's); the script with `--apply` against any real worktree (it was never run; every `--apply` of mine was in a throwaway repository); a dry run on `loop2` (not needed to judge the change).

**The change only prepares the removal.** No test runs the script against a real repository: every test builds a repository in a temporary directory and passes `--repository` to it, with the working directory a temporary one too. Nothing in the commits runs `--apply`; the step in `SKILL.md` runs it only at the start of a later cycle. The script removes through one call, `git worktree remove <path>` for a path git lists (absolute, so never an option; a name such as `-odd name ü` is tested), and calls no branch command, no `rmdir`, no `rmtree`. Names from git as crafted input: a branch name only reaches output and the `startswith("task/")` test; a directory name reaches only the regular expression for base copies (the task name class excludes `{`, `~`, `^`, a leading dash; `..` inside a name makes an invalid ref that does not resolve, so the copy stays); a link or junction at the listed path is kept; a junction inside a checkout is not followed by git (shown); a registration git holds broken, a missing directory and a directory whose `.git` points elsewhere are kept; a locked directory is kept and a directory another process holds fails and is reported, its parent kept. The one way to a removal beyond the rule is I1 (and M1).

## Foundation entries the change writes or changes

WAY-298 (sentence, the pair of examples and the price edited in place), WAY-375 and WAY-376 (new): `foundation_check.py` reports `0 errors`; no invariant test is changed. WAY-298 now says what the code does (two changes outside the task's worktree, the fast-forward only in the-way itself, the removal in every product); WAY-375's and WAY-376's statements agree with the code except M3. The text of WAY-373, WAY-140, WAY-153 and WAY-269 stands; WAY-269's *violates* line about `git fetch --prune` is the reason for M2.

## Reaches beyond the dispatch (section 1)

- `task-cycle/skill/correction.md:1-12` (whether a correction reads "step 4" as including the removal), `task-cycle/skill/SKILL.md:299-324` ("Working copies", the model of the route the new list copies), `task-cycle/skill/request_template.md:405-462`, `task-cycle/record_template.md:180-215`, `agent-instructions/README.md` (the integration route), `foundations/part_map.md:93-105` (the part and its trust boundary list), `elements/decisions/skill/decide_entry.md:12-13` (the one-question rule, for choice 13), `elements/common/way_of_working.md:58-110` ("Reading the foundation"); `grep` for `base-check`/`base-fix`, `Working copies left`, "outside the task's worktree" across the repository (no other file names the two base-copy names or the sentence the task changes).
- `foundations/decisions.md`: WAY-48, WAY-140, WAY-153, WAY-269, WAY-298, WAY-373, WAY-375, WAY-376, each read whole, for the trust boundary, the human-action boundary, the evidence of the plan-state reader, the removal by the orchestrator, the sentence the task changes and the entries the change writes.

## Unread material

- Decisions of my selection: **8 read whole** (WAY-48, 140, 153, 269, 298, 373, 375, 376), **132 by title only** (the other decisions whose *Scope* names `task-cycle`, 139 in all, listed by a throwaway script that I removed; I opened none of them beyond the eight). No title of those 132 points to a bearing on the removal of working directories at the cycle's start; the nearest are WAY-127, WAY-227, WAY-286/287/289, WAY-308/309/323/324, WAY-294/296, WAY-38/89 and WAY-344, which I did not open (the templates' behaviour that they govern I checked by running the three checks; the script's language and Python version I checked by the repository's `.python-version` use of `os.path.isjunction` elsewhere and `python --version`, 3.14.3).
- Invariants whose *Part* is `every` or `task-cycle`: not read (I read only their part list; the one `task-cycle` invariant, `record-copy-image-check`, concerns image files). No test of an invariant is changed by the change.
- Glossary: grepped for `worktree`, `merge`, `record`, `cycle`, `remove` among its headings (no entry); not read whole.
- Guideline files: the-way has no `guidelines/coding.md` to read for a rule of size; `product-guidelines/reading.md` not applied (the change touches no product's guidelines).
- `elements/decisions/examples.md`, `elements/decisions/template.md`: not read (WAY-375 and WAY-376 were compared with `foundation_check.py` and the one-question rule only).
- `task-cycle/request_check.py` and `remarks_check.py`: read (the first whole; the second its docstring and patterns only), `private_paths_check.py`: docstring only.

## Searches not found or unclear

- none

## Working copies

- `.runs/review-whole/` of the worktree: the dry-run output, the focused-test and gate output, the made description, task and record, the driver of the submodule check, three throwaway repositories (`jt`, `jt2`, `sm`) with junctions and a populated submodule. All removed (junctions with `rmdir` first, so no target was followed; `.runs/` holds `task-cycles/` alone). `git worktree list` holds the same 96 entries as before; no worktree was registered in the real repository.
- Kept in `reports/` beside this report: `review-whole-dry-run-output.txt` (the dry-run listing, with absolute paths, in the ignored directory) and `review-whole-submodule-check.py` (the driver of I1, which rebuilds its throwaway repository under `.runs/review-whole/sm` and leaves it there).
- Remainder: none.
