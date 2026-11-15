# Report — executor of slice 16, task `scripts-after-foundation-review`

**Status:** done

- Worktree: `the root of the task's worktree`, branch `task/scripts-after-foundation-review`.
- Slice: 16 — The check of tracked files reads all the Markdown suffixes; the README says what is read; two installation tests install from a clone.
- Method: `task-cycle/change/SKILL.md` (variant: a slice), with `task-cycle/change/slice.md`.

## Commits

- `c01fe56763983c7a366ecda82067c06e4dd50582` — Read note links in every Markdown suffix and install the styleguide and testing tests from a clone.

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/tracked_private_paths_check.py` | 4 | 4 |
| `task-cycle/test_tracked_private_paths_check.py` | 12 | 0 |
| `installation/README.md` | 7 | 5 |
| `installation/test_styleguide_installation.py` | 15 | 4 |
| `installation/test_testing_guidelines_installation.py` | 16 | 5 |

Total: 5 files, 54 insertions, 18 deletions (`git show --numstat` of the commit).

Absolute paths of the files:
- `task-cycle/tracked_private_paths_check.py`
- `task-cycle/test_tracked_private_paths_check.py`
- `installation/README.md`
- `installation/test_styleguide_installation.py`
- `installation/test_testing_guidelines_installation.py`

## What was done

(a) `tracked_private_paths_check.py`: `MARKDOWN_SUFFIX = ".md"` became `MARKDOWN_SUFFIXES = (".md", ".markdown", ".mdx", ".mdc")`, used as `name.lower().endswith(MARKDOWN_SUFFIXES)`. The module description says the same, with the glossary term "Markdown file" (`foundations/glossary.md:199-201`). The README's command description (installation/README.md, the paragraph on the command's output and exit codes) says the same. WAY-320's sentence and the invariant `tracked-file-private-paths` are unchanged.

(b) `installation/README.md`: the exit-2 clause now says a file that starts with a UTF-16 byte order mark is read as UTF-16, as `private_paths_check.py` reads it, and a file with a NUL byte near its start is counted as binary and not read.

(c) Both installation tests (`test_styleguide_installation.py`, `test_testing_guidelines_installation.py`) now run `setUp` as the coding guidelines test does: `git clone` of the checkout into `<tempdir>/source`; `self.commit` and the `cat-file` check run in the clone; `shutil.copyfile(INSTALL, <clone>/installation/install.py)` so the installer under test is the working-tree one; `install()` uses that copy with `--url <clone>`. The line that compares the pin (`self.git("-C", ".the-way", "rev-parse", "HEAD")`) compares with the clone's commit, as the handoff requires. In the testing test, `git show` of the skill now runs in the clone.

## Tests written first

New test: `test_a_note_link_is_listed_in_every_markdown_suffix_in_any_letter_case` in `task-cycle/test_tracked_private_paths_check.py`. Fixtures: `rules.mdc`, `page.mdx`, `guide.markdown`, `UPPER.MDC` each with a note link; `src/a.py` with the same link (not listed).

- Failing run (base, before the script change): `python -B -m unittest discover -s task-cycle -p "test_tracked_private_paths_check.py"` exit 1 — `AssertionError: Lists differ: [] != ['UPPER.MDC:1: note link: a double-bracket note link']`; the four `.mdc`, `.mdx`, `.markdown`, `.MDC` hits were missing, so the failure is an assertion on the listing, not a missing module.
- Passing run (after the script change, same command): exit 0, `Ran 21 tests ... OK`.

The existing test `test_a_note_link_is_listed_in_a_markdown_file_only` already covers `.md`, `.MD` and a `.py`/`.js`/`.txt` file not listed; it is unchanged and still passes.

No invariant's test was changed. `test_tracked_files_private_paths.py` (the invariant's test) is untouched. No test holds a `decision:` line that was changed.

## Checks run

| Check | Command | Exit code | Result |
|---|---|---|---|
| New and existing tests of the tracked check | `python -B -m unittest discover -s task-cycle -p "test_tracked_private_paths_check.py"` | 0 | Ran 21 tests, OK |
| The invariant on the tracked files | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | `checked: 310 files, 0 listed` |
| The invariant's test | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | Ran 1 test, OK |
| Styleguide installation | `python -B -m unittest discover -s installation -p "test_styleguide_installation.py"` | 0 | Ran 2 tests, OK |
| Testing guidelines installation | `python -B -m unittest discover -s installation -p "test_testing_guidelines_installation.py"` | 0 | Ran 2 tests, OK |

Not run: the full gate (WAY-160, not run by the executor). The commit-in-checkout failure the slice guards against was not reproduced by a simulated commit during a run; the clone isolation is verified by the passing runs and by reading the code, not by such a simulation.

One-line check result for the orchestrator: all five focused checks exit 0; none failed; the whole gate was not run.

## Own-work check (section 3)

- Requirement: the new suffix reading does not make `tracked-file-private-paths` fail on the files git tracks now. Check: run the invariant's command on the worktree. Shown: exit 0, `checked: 310 files, 0 listed`. `git ls-files` shows no tracked `.mdc`, `.mdx` or `.markdown` file, so the new suffixes add no file to the check today.
- Requirement: the README and the script's description say the same as the code. Check: read both against the code after the change. The suffix list and the UTF-16 sentence match `private_paths_check.py` lines 52-54 and `tracked_private_paths_check.py` line 15-16.
- Mutation in the head: restoring `.md` alone makes the new test fail (the base run above is this mutation).

## Choices made

- The glossary term "Markdown file" is taken from `foundations/glossary.md:199-201` (the entry's sentence: "a file whose name ends in `.md`, `.markdown`, `.mdx` or `.mdc`, in any letter case"). The slice's text and the glossary agree; no other word was used.
- Test fixture names use upper case `UPPER.MDC` to cover letter case; the expected listing is written in sorted order, as the command lists files sorted by path.
- The `installation/README.md` change to the command description was placed in the paragraph that already says what the command lists and what exit 2 means, so no new paragraph was added.
- For (c), `shutil.copyfile` copies the working-tree installer into the clone; the clone's own `installation/install.py` is overwritten in the temp directory only, never in the repository.
- The `git` helper's `cwd=` argument is used with the clone (`self.source`) where the commit is read, so the product's own commands keep the product as their working directory.

## Reaches beyond the slice's named ranges (section 1)

- `foundations/glossary.md:195-205` — read the whole "Markdown file" entry to take the term; the glossary's other entries not read. Why: the slice says the term is the one the foundation step wrote, and the entry is the only place it lives.
- `foundations/decisions.md:7183-7253` — read as the start of WAY-320 (heading and body to *violates*). Why: the search by "Markdown file" pointed there. The rest of WAY-320 (`7254-7302`, the end of the entry and the start of WAY-324) was not read; see Unread material.
- `foundations/decisions.md` line 7191-7200 and 7215 and 7254 are the text of WAY-294/WAY-320 rationale, which mentions the Markdown rule; read as part of 7183-7253.

## Unread material

- `foundations/decisions.md:7254-7302` (rest of WAY-320, after *violates*) and `7303-7351` (WAY-324): not read. WAY-320's sentence, which the slice keeps unchanged, lies within 7183-7253 and was read there.
- `task.md:45-47`, `91-95`, `130`, `150`: read in part via `sed` on those line numbers, which is the named range.
- `task-cycle/private_paths_check.py:110-194` (the named range): read as lines 100-200 and 1-60 (the module description, lines 46-55, and `check_file` lines 140-158). Read in full for the named range.
- `installation/test_coding_guidelines_installation.py:28-60`: read as lines 1-70.

## Searches not found or unclear

- Searched `foundations/` for "Markdown file" to locate the glossary term: found the glossary entry (`glossary.md:199`), WAY-320 (`decisions.md:7191-7270`), and the invariant (`invariants.md:88`). No conflict with the slice.
- Searched for `.mdc`, `.mdx`, `.markdown` in `git ls-files`: none tracked, so no file of the repository is newly listed.
- Searched the installation tests for `SOURCE` uses: `SOURCE` is still used for the clone source and for `INSTALL`, and `SKILL_SOURCE` is unchanged. Nothing unclear.

## Working copies

No working copy was made: no worktree, clone or prepared input is left by the executor. The clone the installation tests make is inside a `tempfile` directory created and removed by each test (not the executor's). `.runs/executor-16/` does not exist.

## Problems observed

- None that block the slice. The line numbers the task gives for `self.commit = ...` (styleguide l. 37, testing l. 32) match the base.
- The git hook (`rules-on-demand`) asked for the git rules to be read before the first commit attempt; the attempt was repeated after reading `a rule or note file of the author's, outside the repository`. The commit message is English and the files are added by path; nothing under `.runs/` was added. No other effect.
