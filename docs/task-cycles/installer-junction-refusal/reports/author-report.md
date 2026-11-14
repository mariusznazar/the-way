# Author report — installer-junction-refusal

## Status

`done`

## Commits

- `54ed53c` — Refuse and do not follow a Windows junction where the installer refuses a symlink (installer, tests, README)
- `474df77` — Record the invariant that the installer writes and deletes nothing through a link (`foundations/invariants.md`)

Base `6fa755c`, branch `task/installer-junction-refusal`, not pushed. Nothing outside the worktree touched; `.runs/` touched only for this report.

## Files changed

| File | Added / removed |
|---|---|
| `installation/install.py` | +11 / -5 |
| `installation/test_install.py` | +96 / -0 (the 3 tests, 3 helpers, 3 imports) |
| `installation/test_agent_types_installation.py` | +2 / -0 (two existing symlink tests now also cite the invariant) |
| `installation/README.md` | +9 / -2 |
| `foundations/invariants.md` | +10 / -0 |

## What the change does

- `install.py` gets one helper, `is_link(path)`: `path.is_symlink() or path.is_junction()`. It replaces `is_symlink()` at every place the installer tests a **directory** for a link: `check_parents` (parents of every written path: foundations, entry points, agent definitions), `stale_agent_definitions` (`.claude`, `.claude/agents`), `stale_entry_points` (the `skills` folder and the folder of each entry) and the `.the-way` check in `plan` (pinned case).
- Left as `is_symlink()` on purpose: `read_text_file`, `owned_entry_point`, `owned_agent_definition`, the `foundations/*` file check and `modules_file`. They test **files**; a junction is never a file (`is_file()` is false for it, so they already refuse or skip it). Changing them would be a no-op.
- Behaviour for anything that is not a junction is unchanged: the helper is `is_symlink()` plus a test that is false for a non-junction; the existing tests of `installation/` pass.
- Stale removal through a junction **skips** the entry (does not refuse the run), exactly as it already does for a symlink (existing test `test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted`). The write path **refuses** before writing (exit 1, `Parent path is not a regular directory`), as for a symlink. `.the-way` as a junction with a pin: `Existing .the-way is not a submodule directory`.

## How the tests make a junction (handoff: read `script-subprocesses` first)

`script-subprocesses`: no script git tracks starts a program other than git, the Python interpreter running it, or a product-declared command. So `cmd /c mklink /J` and PowerShell `New-Item -ItemType Junction` are not allowed in a test. The standard library has no public call that makes a junction. The way taken: the private call `_winapi.CreateJunction(target, link)` of the standard library's own `_winapi` module (`_winapi` is in `sys.stdlib_module_names`, checked, so `script-imports` holds). The same call is already used by `instruction-files/test_check_instructions.py:95` (`make_directory_link`), which is the precedent in this repository. It is imported inside the helper `InstallTest.junction`, only on `sys.platform == "win32"`; elsewhere, and where `CreateJunction` raises `OSError`, the test is skipped with a message. After creating, the helper asserts `is_junction() and not is_symlink()`, so a test never runs against something that is not a junction.

## The tests (`installation/test_install.py`, class `InstallTest`)

All three cite `# invariant: installation-paths-through-links`.

1. `test_rejects_a_junction_on_the_path_of_a_file_it_writes_without_touching_the_target` — a junction to a folder outside the product at each of `.claude`, `.claude/agents`, `.claude/skills`, `.claude/skills/the-way-make-change` (a current entry's folder), `.agents`, `.agents/skills`, `foundations`; preview and `--apply` each (14 subtests). Asserts: exit not 0, `Parent path is not a regular directory`, no `Installed.`, the product tree (listed through the junction) and the outside folder unchanged, outside folder still holds only its canary file, no `.gitmodules`.
2. `test_deletes_nothing_through_a_junction_at_the_folder_of_a_stale_entry_point` — junction at `.claude/skills/the-way-gone` and at `.agents/skills/the-way-gone`, each to an outside folder holding the installer's own `SKILL.md` for `the-way-gone`; preview and `--apply`: exit 0, no `DELETE`, outside `SKILL.md` byte-equal, junction still there.
3. `test_rejects_a_junction_at_the_submodule_directory` — real install, then `.the-way` is replaced by a junction to a checkout of the pinned commit (the clone `self.source`, whose `git rev-parse HEAD` is asserted equal to the pin, so the installer would accept it if it went through); preview and `--apply`: exit not 0, `Existing .the-way is not a submodule directory`, the target unchanged.

The two existing symlink tests of `test_agent_types_installation.py` (`test_a_symlink_in_the_way_stops_the_run_and_its_target_is_not_touched`, `test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted`) now also carry `# invariant: installation-paths-through-links`, since the sentence covers symbolic links too. This is a change to an invariant test of an existing file; the request names it.

Break each test catches (WAY: name the break): test 1 — `check_parents` going back to `is_symlink()` (a bug: write through a junction); test 2 — `stale_entry_points` going back to `entry.is_symlink()` (a bug: deletes a file outside the product); test 3 — the `.the-way` check going back to `is_symlink()`. Each test depends on one site, as the failing run below shows.

## Checks (command, exit code)

All run from the worktree root, Windows, Python 3.14.3.

| Check | Command | Exit | Result |
|---|---|---|---|
| **Failing run, before the fix** (tests written, `install.py` unchanged) | `python -B -m unittest installation.test_install -k junction -k stale_entry` | 1 | `Ran 3 tests in 118.010s`, `FAILED (failures=18)`: 14 subtests of test 1 (every junction folder, preview and apply: `AssertionError: 0 == 0` — the installer exited 0 and wrote through the junction), 2 of test 2 (`'DELETE' unexpectedly found` — the installer planned and in apply would have deleted the outside file), 2 of test 3 (`0 == 0` — exit 0). Each failed at its first assertion, for the expected reason, not on a missing module or helper. |
| **Passing run, after the fix** | `python -B -m unittest installation.test_install -k junction -k stale_entry -v` | 0 | `Ran 3 tests in 79.227s`, `OK`, all three `... ok`, none skipped. |
| Directory | `python -B gate/run_tests.py installation` | 0 | `Ran 59 tests in 899.434s`, `OK` (the existing tests of `installation/` and the 3 new ones). |
| Foundation check, before the tests were committed | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| Foundation check without the switch, after both commits | `python -B elements/common/foundation_check.py` | 0 | `0 errors` (the invariant reads `test` and is cited) |
| Ad hoc crafted input, no pin | `python -I <scratchpad>/nopin.py installation/install.py` (a product with a junction at `.the-way` and no gitlink, `--apply`) | prints `1` | `Error: ...\.the-way already exists; refusing to replace it`, nothing created outside — an existing refusal, `os.path.lexists` already covers a junction. |

Not run, by the handoff: the product's whole gate (`python -B gate/run_tests.py` with no argument). The passing run took 79 s and the directory 899 s because every test of this directory clones the-way in `setUp`; nothing in my change adds to that cost per test beyond three tests (the 14 subtests of test 1 reuse the one clone).

## Acceptance criterion

"On Windows the tests of item 3 are not skipped": ran here (Windows 11), the three tests ran and passed (`-v` shows `ok`, no `skipped`); the directory run reports `OK` with no skip count. On a platform without junctions they are skipped by `junction()` with the message `Junctions exist only on Windows`.

## Own-work check (WAY-164)

Requirement most likely not met: "wherever the installer recognises a symlink today ... the removal of stale entries and `.the-way` included" — that a junction is recognised at every directory-level site, not only at the one the tests reach first. Check: I listed every `is_symlink` in `install.py` (`grep -n is_symlink`) before and after; the remaining ones (lines 206, 324, 340, 439, 460) test files, where a junction cannot occur; the five directory-level sites are replaced. Then crafted input as the handoff asks, one case per place: `.claude`, `.claude/agents`, `.claude/skills`, a current entry folder, `.agents`, `.agents/skills`, `foundations` (test 1), a stale entry folder under `.claude` and `.agents` (test 2), `.the-way` with a pin (test 3) and `.the-way` without a pin (ad hoc run above). Result: all refuse or skip as set out, and the failing run before the fix shows every one of them going wrong first.

Mutation in the head: the two `is_link` calls in `stale_agent_definitions` (`.claude`, `.claude/agents`) and the one on the `skills` folder in `stale_entry_points` are **not protected by any test**: they are unreachable behind `check_parents`, which refuses a junction at `.claude`, `.claude/agents` or `.claude/skills` before the stale scan runs (the folders hold files the installer writes). I made them consistent with the helper rather than leave `is_symlink()` there, as a guard against a later reordering of `plan`; a mutation of them is caught by no test. Naming it rather than faking a test: any test would have to call the function directly, which asserts on the replacement of the flow, not on behaviour.

## The entry (row 1)

`installation-paths-through-links`, in `foundations/invariants.md` after `installation-claude-guidance`. Written by following `elements/invariants/skill/SKILL.md` (and `decide_entry.md`, `draft.md`, `write.md` beside it, which the skill names), `template.md`, `rules.md`, `way_of_working.md`, `examples.md`. The search of the whole foundation for `junction`, `symlink`, `symbolic link` found no entry stating this (WAY-33): the only hit is an environment fact about Claude Code reading `AGENTS.md`, unrelated.

Sentence: "The installation command neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a directory path of a product, `.the-way` included, and it refuses before it writes anything where such a link stands on the path of a file it is to write or is `.the-way`."

Fields: Method `test`; Rests on `none`; Derives from WAY-48 · WAY-235 · WAY-368; Part `installation`; Violated `no`.

- **Meaning, English (row 1):** the installer never writes or deletes through a symbolic link or a Windows junction on a path of the product, `.the-way` included; where such a link stands on the path of a file it must write, it refuses before it writes anything.
- **Znaczenie, po polsku (row 1):** instalator nigdy nie zapisuje ani nie usuwa niczego przez dowiązanie symboliczne ani junction Windows na ścieżce produktu, w tym przy `.the-way`; gdy takie dowiązanie stoi na ścieżce pliku, który ma zapisać, odmawia, zanim cokolwiek zapisze.

Choices made in the entry (the row leaves them to the writer; no one can answer):

- **Removal skips, writing refuses.** The row says "odmawia, zanim cokolwiek zapisze" and the task's item 2 says removal "nie usuwa niczego, do czego prowadzi junction"; the installer's existing behaviour for a symlink at a stale entry is to skip it and carry on (an existing test holds that). So the sentence says "neither writes nor deletes" through a link, and "refuses" only for the write path and `.the-way`. Rejected: "refuses" for removal as well — it would change what the installer does for a stale symlink, which item 5 forbids.
- **Part `installation`, not `every`:** only a change to `installation/**` can make this false.
- **Derives from WAY-368, as well as WAY-48 and WAY-235:** WAY-368 (verification) binds the installer to replace and delete only its own files, which is the deletion half. WAY-235 is exempted from the-way by WAY-328, but the entry has its shape (a refusal on a trust boundary, checked by a permanent test seen failing once); WAY-328 stays out of the links as it only exempts.
- **Rests on `none` — see concerns.**
- Identifier names what the sentence constrains (paths and links), not what it demands.
- Part map: the surface `installation-command` was not edited (see concerns).

## Reaches beyond the handoff

- `instruction-files/test_check_instructions.py:80-120` and a `grep` of the whole worktree for `_winapi|CreateJunction|mklink|isjunction|is_junction`: to find how this repository already creates a junction in a test (handoff told me to find the allowed way); found the precedent at `:92-100`.
- `foundations/environment_facts.md` entry `python-stdlib-modules` (lines 24-28) and `sys.stdlib_module_names` in the interpreter: to confirm `_winapi` counts as a standard-library module for `script-imports`.
- `elements/invariants/skill/decide_entry.md`, `draft.md`, `write.md`: named by the element's skill, not by the handoff.
- A grep of `foundations/` for `junction|symlink|symbolic link`: the search of the foundation of WAY-33.
- The vault's `rules/git.md` and `rules/scripts.md` (the user's global rules for commits and scripts).

## Unread material

- `foundations/invariants.md`: read lines 1-16 and 100-199, 255-357 (the eight invariants the handoff names, the part `installation` and `every` ones around them, and the entries `elements/invariants/examples.md` names, except below); not read: lines 16-100 and 199-255, which include the example entry `return-step-record`. The handoff names it only through `examples.md`; its form was taken from the entries read.
- Everything else the handoff names was read whole: the eight decisions (WAY-13, WAY-34, WAY-38, WAY-48, WAY-141, WAY-235, WAY-328, WAY-368, each to the next `###`, the longer ones in two reads), the part map, the glossary, the element's template, rules, way of working, examples and `SKILL.md`, the foundation step, `make-change`, the task, `install.py`, both test files and the README.

## Searches not found or unclear

- No environment fact for what a Windows junction is, and no instruction that says whether `Rests on` of this invariant must name one (see concerns). Searched `foundations/environment_facts.md` for `junction`: no hit.
- The handoff says "`test_agent_types_installation.py:263`" shows an existing symlink test form; at this base commit the test is at line 255-264 (the `link` helper at 247). No effect.

## Questions and concerns

1. **`Rests on: none` for a Windows junction.** `draft.md` says to put through the template's test every fact that "neither the product nor the-way writes, such as a standard, a library or a law, found behind what the sentence names". "Windows junction" is such a platform fact, and `installation-claude-guidance` rests on one (`claude-code-imports`). I wrote `none` and no environment fact because the rule for a fact is to take it from a source, never from memory (WAY-80), I had no source in the handoff, and `TODO` would put an unanswerable question before the human on the main branch. The sentence also stays true if the platform fact were different, since the code uses the Python 3.14 standard library's `is_junction` and does not parse the file system itself. Recommendation: accept `none`; if the reviewer wants the fact, it is a small environment-fact entry from the Python 3.14 documentation of `os.path.isjunction` ("Return True if path refers to an existing directory entry that is a junction") — I did not fetch it.
2. **Part map surface `installation-command`** says the installer "rewrites only its own ... and deletes only its own". The refusal through links is not in its text and I did not add it: the task's *Settlements to record* names an invariant only, and a promise to products is the human's to widen. Recommendation: leave; a product already relies only on the preview and confirmation, and the refusal narrows what the installer does.
3. **Time of the directory run (899 s) is the installer tests' own cost** (each test clones the-way); noticed because the harness cut the first waits. Not caused by this change.
4. The three new tests make an `outside` folder inside the temporary directory; if the installer ever misbehaves again, it writes inside that temporary directory and nowhere else, and `TemporaryDirectory.cleanup` removes the tree (the runs ended without a cleanup error; I did not inspect the temporary directory afterwards, so "no stray files" is not verified).

## Problems as observed

None beyond the defect the task names: before the fix the 18 subtests above failed as listed, which reproduces the defect (exit 0, writes through the junction, plan to delete the outside `SKILL.md`). Cause verified by the passing run after replacing only the five directory-level tests of `is_symlink()` with `is_link()` — no other change to the code.
