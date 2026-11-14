# Author fix report — installer-junction-refusal

## Status

`done`

## Commits (on `task/installer-junction-refusal`, after `474df77`)

- `62ec7c1` — Test the stale-file scans against a junction at their directory and check the tool directory too (`installation/install.py`, `installation/test_install.py`, `installation/README.md`)
- `ee6126c` — Narrow the installer link invariant to its own code and record the junction fact it rests on (`foundations/invariants.md`, `foundations/environment_facts.md`)

Not pushed. Files changed in the fix: `installation/install.py` +1/-1, `installation/test_install.py` +41/-0, `installation/README.md` +2/-2, `foundations/invariants.md` +2/-2, `foundations/environment_facts.md` +6/-0.

## Findings, one by one

### 1 (blocking) — the sentence is broader than the code: fixed by narrowing the sentence

Old sentence (on `474df77`):

> The installation command neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a directory path of a product, `.the-way` included, and it refuses before it writes anything where such a link stands on the path of a file it is to write or is `.the-way`.

New sentence (on `ee6126c`):

> The installation command, with its own code, neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a path of a product, `.the-way` included, and it refuses before it writes anything where such a link stands on the path of a file it is to write or is `.the-way`.

- **Meaning, English (row 1):** the installer's own code never writes or deletes through a symbolic link or a Windows junction on a path of the product, `.the-way` included, and it refuses before writing anything where such a link stands on the path of a file it is to write or is `.the-way`.
- **Znaczenie, po polsku (row 1):** własny kod instalatora nigdy nie zapisuje ani nie usuwa niczego przez dowiązanie symboliczne ani junction Windows na ścieżce produktu, w tym przy `.the-way`, a gdy takie dowiązanie stoi na ścieżce pliku, który ma zapisać, albo jest `.the-way`, odmawia, zanim cokolwiek zapisze.
- **What the narrowing leaves outside (the human sees it at the merge):** what git itself writes when the installer starts it — in particular `git submodule add` writing the submodule's own directory under `.git/modules`. A junction at `.git/modules` is still written through with exit 0, as the review's case B showed; the entry no longer says it is not. No check of `.git` or `.git/modules` was added to `plan` (the orchestrator's decision: that would widen the task, whose item 1 asks for refusal on the path of a file the installer writes). If the human wants git's writes under `.git` held too, that is a further check in `plan` plus a test and a sentence that drops "with its own code".
- Row 1's meaning is kept: the installer neither writes nor deletes through a symbolic link or a junction, and refuses before writing. `Violated` stays `no`.
- Check that shows it: `python -B elements/common/foundation_check.py` → exit 0, `0 errors`, run after both commits.

### 2 (Minor) — three checks without a test: fixed

New test `test_the_scan_for_stale_files_does_not_enter_a_junction_at_their_directory` in `installation/test_install.py`, citing the invariant. It calls `install.stale_agent_definitions` and `install.stale_entry_points` directly (as the reviewer describes) in six cases, each a product holding the installer's own stale file (`the-way-gone`): two controls with real directories (`.claude/agents`, `.agents/skills`; the scan must return exactly that file, so an empty result below a junction is the junction's doing), and a junction at `.claude/agents`, at `.claude`, at `.agents/skills` and at `.agents` (the scan must return `[]` and the file outside stays unchanged). The junction at `.claude/agents` and at `.agents/skills` are the two the reviewer names; `.claude` and `.agents` are the ones the scans check (or should) as the parent.

Runs, command `python -B -m unittest installation.test_install -k scan_for_stale`:

- **Failing run 1, before a change of the code to the test (the test as first written, code of `62ec7c1` minus its one-line change to `install.py`):** exit 1, `FAILED (failures=1)`: the case "junction at `.agents`, scan `stale_entry_points`" returned the outside `SKILL.md` instead of `[]`. **This is a defect the test found, not only a missing test:** `stale_entry_points` checked `skills` and each entry but never `.claude` or `.agents` itself, so a junction (or a symlink, in the code before this task) at `.agents` or `.claude` let the scan list, and in `--apply` delete, a stale `SKILL.md` through it. `plan` refuses such a junction first (`check_parents`), so no run reaches it today; the same gap was in the symlink check the task replaced. Fixed in `install.py` with one condition: `is_link(target / directory) or is_link(skills) or not skills.is_dir()`. It is a few characters beyond what the finding asks and it is the same rule (the task's "wherever the installer recognises a symlink"); named here so the reviewer can contest it.
- **Passing run, after the fix:** exit 0, `Ran 1 test`, `OK`.
- **Failing run 2, on a mutation of the checks (as the handoff asks):** the three directory-level checks of `stale_agent_definitions` and `stale_entry_points` temporarily turned back into `.is_symlink()` (the `.claude`, `agents`, tool directory and `skills` ones; `is_link(entry)` left alone), same command: exit 1, `FAILED (failures=4)` — the four junction cases (`.claude/agents`, `.claude`, `.agents/skills`, `.agents`), each on its assertion that the result is `[]`. The code was restored byte for byte from a copy before the commit (`git diff` showed only the one-line fix), and the test passed again, exit 0.

### 3 (Minor) — "directory path": fixed with finding 1

The sentence says "a path of a product". Tests that cite the invariant and what its words cover:

| Test | Place of the link | Covered by |
|---|---|---|
| `test_install.py` `test_rejects_a_junction_on_the_path_of_a_file_it_writes_without_touching_the_target` | a directory on the path of a file it writes | clause 2 and "a path" |
| `test_install.py` `test_deletes_nothing_through_a_junction_at_the_folder_of_a_stale_entry_point` | the folder of a stale entry | "deletes nothing through ... a path" |
| `test_install.py` `test_the_scan_for_stale_files_does_not_enter_a_junction_at_their_directory` | a directory above a stale file | "deletes nothing through ... a path" |
| `test_install.py` `test_rejects_a_junction_at_the_submodule_directory` | `.the-way` | clause 2 ("or is `.the-way`") |
| `test_agent_types_installation.py` `test_a_symlink_in_the_way_stops_the_run_and_its_target_is_not_touched` | `.claude`, `.claude/agents`, a definition itself, a dangling one | clause 2 (the link is on the path of a file it is to write; a symlink at the definition itself is a link on that path) |
| `test_agent_types_installation.py` `test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted` | the stale definition's own path | "deletes nothing through ... a path of a product" |

Every test that cites it is covered by its words.

### 4 (Minor) — `Rests on: none`: fixed, the environment fact is written

Followed `elements/environment-facts/skill/SKILL.md` and, as it names them, `read.md`, `decide_entry.md`, `draft.md`, `write.md`, `template.md`, with `elements/common/rules.md` and `way_of_working.md` read earlier. The source is the Python 3.14 documentation page of `os.path.isjunction`. Steps:

- Opened the address with `curl` (HTTP 200, `https://docs.python.org/3.14/library/os.path.html`) and took the passage from the page's text as a reader sees it: "Return True if path refers to an existing directory entry that is a junction. Always return False if junctions are not supported on the current platform." One paragraph, so one passage. The 3.14 documentation page is a page without editions in the template's sense (its path names a version but the publisher moves it to newer text), so the form is a page with the closest archived copy that already exists, as the existing entry `python-stdlib-modules` does.
- The archived copy was found through the archive's CDX index of captures (`http://web.archive.org/cdx/search/cdx?url=docs.python.org/3.14/library/os.path.html&limit=-3&output=json`), not made for the entry: the latest capture is `20261024070950`, 2026-10-24. I fetched it and checked that both sentences of the passage stand in it word for word.
- Entry `python-junction-detection` in `foundations/environment_facts.md`, before the withdrawn identifiers: "In Python 3.14, `os.path.isjunction` returns true for an existing directory entry that is a junction, and always returns false where the current platform supports no junctions." Source: the address (archived: `http://web.archive.org/web/20261024070950/https://docs.python.org/3.14/library/os.path.html`, 2026-10-24) § os.path.isjunction — the passage; read 2026-11-14. The sentence says no more than the source (the template's rule); it does not say a junction is no symbolic link, which the page does not say (that is the task's probe, not a source).
- `installation-paths-through-links` now has `Rests on: python-junction-detection`. `foundation_check.py` → exit 0, `0 errors`.
- Meaning, English (the fact): Python 3.14's `os.path.isjunction` recognises a junction and is false where the platform has none. Po polsku: `os.path.isjunction` w Pythonie 3.14 rozpoznaje junction i zawsze zwraca fałsz tam, gdzie platforma nie ma junction. The entry is marked `the cycle's` (no row, no projected entry carries it), so the request puts it before the human.

### 5 (Minor) — README sentence: fixed

`installation/README.md` now reads "a junction at the folder of a skill the commit lacks, or at the path of an agent type's file, is not followed, so nothing is deleted through it".

### 6 (Minor) — sizes: no change asked, none made

## Checks (command, exit code)

| Check | Command | Exit | Result |
|---|---|---|---|
| New test, failing on the gap it found | `python -B -m unittest installation.test_install -k scan_for_stale` | 1 | `FAILED (failures=1)` |
| Same, after the one-line fix | same | 0 | `Ran 1 test`, `OK` |
| Same, mutation of the checks | same | 1 | `FAILED (failures=4)` |
| Same, mutation restored | same | 0 | `OK` |
| Directory of the touched tests | `python -B gate/run_tests.py installation` | 0 | `Ran 60 tests in 814.048s`, `OK` (59 before + the new one; the three junction tests of the first handoff among them, not skipped on this Windows) |
| Foundation check, after the commits | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: the whole gate (not mine now). The review's evidence runs (`crafted.py` cases) were not re-run: case B is now out of the sentence by design.

## Own-work check (WAY-164)

Requirement most likely not met by this fix: that the narrowed sentence is true to the code, and that every place the code can delete through a link has a test. Check: the new test (finding 2) calls the scans directly, and it found one real gap (`.agents`/`.claude` not checked by `stale_entry_points`), which is fixed; the mutation shows each of the four directory checks it names is protected. The sentence and the code agree on writes by the installer's own code: every `path.mkdir`, `open("x")`, `write_bytes`, `unlink`, `rmdir` of `install.py` acts on paths that went through `check_parents` or `stale_*`; the remaining writes are git's (`git submodule add`, `checkout`, `update`), which the sentence now leaves out. I did not re-run a crafted-input script for `.git/modules`.

## Reaches beyond the handoff

- `task-cycle/change/fix.md` (named by `make-change` section 1 for the fix), and the environment-facts skill's own files `read.md`, `decide_entry.md`, `draft.md`, `write.md` and `template.md` (named by the skill).
- Network: `https://docs.python.org/3.14/library/os.path.html`, the archive's CDX index and the archived copy `http://web.archive.org/web/20261024070950/...` (for finding 4, as the handoff asks).
- `elements/environment-facts` examples: `foundations/environment_facts.md` lines 1-30 and its end, read for the form and the place of the new entry.

## Unread material

- `reports/review-whole-report.md`: not read; the findings file was enough for every finding (the handoff says to read it only where a finding needs its evidence).
- Everything else the fix handoff names was read whole: the handoff, the findings file, `fix.md`, the environment-facts skill with its five files.

## Searches not found or unclear

- None that matter. The reviewer's `crafted.py` of case B is in a scratchpad I did not open.

## Questions and concerns

1. The one-line change to `stale_entry_points` (checking `.claude`/`.agents` themselves) is a code change within a fix for Minor findings, found by the test the reviewer asked for. It changes no behaviour of any run (`plan` refuses first) and is the same rule as the task's. If the cycle holds that a Minor-only fix may not change code, revert the line and drop the two `.agents` and `.claude`-for-skills cases; the invariant's test of the deletion half would then be left with a known hole. Recommendation: keep.
2. Git's writes under `.git` (the narrowing of finding 1) are a known hole in what the installer protects: a junction at `.git/modules` still sends the submodule's directory outside the product. Held out of scope by the orchestrator and the reviewer; the human sees the old and new sentence above.
