# Author report — installer-foundation-check-full-path

**Status:** done

## Commits and files

- `1c222ce2` — Name the foundation check by its full path in the installer's block (one commit, on
  `task/installer-foundation-check-full-path`, base `fad52af3`).
- `installation/install.py` — +3 / -3: the sentence "Until the part map has its first parts, …" in
  `product_guidance` now names `{SUBMODULE}/elements/common/foundation_check.py` (an f-string, as the two
  sentences beside it).
- `installation/test_install.py` — +26 / -2: the expected `BLOCK` follows the sentence (cause on the
  requirement side: WAY-418 and the task's To do item 1); the new test
  `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`, citing
  `# invariant: installation-agents-md-warnings`.
- `foundations/invariants.md` — +10: the new entry `installation-agents-md-warnings`, put after
  `installation-paths-through-links` (the other entries of the part `installation`).

No move out of a function or file (WAY-365): `install.py` is 858 lines and `product_guidance` about 47,
under the 1200 and 110 of WAY-385, so nothing applied.

## Foundation entry (row 2) — marked `row 2`

`installation-agents-md-warnings`, Method `test`, Rests on `none`, Derives from `WAY-418`, Part
`installation · instruction-files`, Violated `no`.

- English: In a product made by a full run of the installation command, before any skill of the-way has run
  in it, the script that checks instruction files, run on the product's root, reports no warning on the root
  `AGENTS.md`.
- Po polsku: W produkcie zbudowanym pełnym przebiegiem instalatora, zanim uruchomił się w nim jakikolwiek
  skill the way, skrypt sprawdzający pliki instrukcji, puszczony na korzeniu produktu, nie zgłasza
  ostrzeżenia na głównym `AGENTS.md`.

No part was added that the row does not give: Rests on `none` (the sentence rests on no outside fact),
Derives from WAY-418 (the row's source), Part is the writer's reading of where a change can make it false
(the installer writes the block and the `.gitignore` line; the checker decides what a warning is). No
pair of examples, no `the cycle's` entry. Row 1 is not an element entry: it goes to the code and its test
(`product_guidance`, `BLOCK`), as the row says.

## Choices made (the sources settle the behaviour; these are the how)

1. **The test runs the checker on the product's root, and asserts on the lines of `AGENTS.md` only.** The
   checker is the product's own `.the-way/instruction-files/check_instructions.py` (the pinned commit, as
   a product runs it; `test_empty_foundations_have_valid_form` does the same with the foundation check).
   Rejected: `--file AGENTS.md` — the checker then reads absolute paths differently and relative ones from
   the file's directory, not the product's root, which is not how the one command runs it; asserting the
   count line `0 error, 0 warn, …` — it would couple the test to warnings of other files (entry points),
   which are not the sentence's subject, and the `info` count moves with the product. Cost if wrong: a
   warning on another file would not turn this test red; the sentence names `AGENTS.md` only.
2. **A precondition and a guard against a vacuous pass:** the test asserts the product has no `.runs`
   directory (the task's question 1), and that the last output line matches
   `^\d+ error, \d+ warn, \d+ info$`, so a checker that did not run to its end does not pass as "no warning".
3. **The product is built by `self.install("--apply")`, the existing way of `InstallTest`** (a clone of the
   source as the remote, an empty `git init` product in `tempfile`), before anything writes `.runs/`.
   The permanent test therefore stands in the system's temporary directory like every test of the file;
   the handoff's `.runs/author/` rule is for my own working copies, and I used only that for the probe.
4. **Wording of the sentence:** `{SUBMODULE}/elements/common/foundation_check.py` in backticks, line wrapped
   inside the f-string at 100 columns; no other word of the block changed (the sentence about `.runs/` is
   untouched, as question 1 binds).

## Checks

Failing runs (before the fix of the sentence), then passing:

- `python -B -m unittest installation.test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`
  before the fix: exit 1, `['WARN  dead-path AGENTS.md:10 \`foundation_check.py\` does not exist'] != []`
  (the assertion failing for the expected reason, not a stop on a missing file).
- Same command after the fix: exit 0.
- `python -B gate/run_tests.py installation`: exit 0 (74 tests, OK, 611 s — it ran in the background; the
  length is the file's own, a test that does a full installation per case).
- `python -B gate/run_tests.py instruction-files` (control; I touched nothing there): exit 0, 122 tests, OK,
  skipped 5 (POSIX-only link tests).
- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`, test exists, files added
  to git before the run and again after the commit): exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .` in the worktree: `0 error, 0 warn, 5 info`.
- Formatter and linter with the pinned Ruff of the main checkout
  (`the main checkout's .runs/quality-venv/Scripts/ruff.exe`, as `agent-instructions/test_linter_invariant.py`
  finds it): `format --check` on both files exit 0 (after one reformat of my test line, which was 1 line
  over the layout); `check` on both exit 0, `All checks passed!`.
- Not run: the full gate (`python -B gate/run_tests.py` with no argument), as the handoff says.

## Own-work check (section 3)

The requirement most likely not met: question 1 of the task — the warning on `.runs/` must go in the
product after a full installation, because the installer leaves `.runs/` in `.gitignore`; the test must
catch its loss. Check: with `ignore_change` made to create `.gitignore` with `build/` instead of `.runs/`
(a mutation, in the worktree, restored with `git checkout installation/install.py` before the commit), the
new test fails: exit 1, `['WARN  dead-path AGENTS.md:8 \`.runs/\` does not exist'] != []`. The mutation was
then removed; the committed `install.py` carries only the sentence change. The second break (the old
sentence) is the failing run above.

Mutations in the head: a sentence naming a file that is missing at the pinned commit — caught by the new
test and by `test_guidance_names_only_scripts_the_pinned_commit_holds`, whose regex now also covers this
sentence (it takes every `.the-way/<path>.py`); an empty or crashed checker output — caught by the count
line guard; a filter that matched no line — the break above shows it matches `WARN  dead-path AGENTS.md:`.

## Walkthrough

The change alters the text of a block the installer writes into a product's `AGENTS.md`, which a session
of an agent reads; it alters no screen, API or command's behaviour, and the real installation's output
was seen by the test itself (a full installation in a temporary product and the checker on its result), so
no further walk is made.

## Reaches beyond the dispatch

- `elements/invariants/skill/decide_entry.md`, `draft.md`, `write.md`, `elements/invariants/template.md`:
  named by the invariants `SKILL.md` at its steps; read whole for the entry.
- WAY-385 (`foundations/decisions.md`), read whole: to settle the rule of size for `install.py` (above).
- `installation/README.md`: read its head and the part on the block's row (up to the CI section); it
  describes the block in general terms, not this sentence, so I changed nothing there.
- Guidelines kind files: none opened. The index of `guidelines/coding.md` has the kind `repository-changer`
  for `install.py` and its row's *When to read* ("before adding or changing a repository changer: a script
  that removes, rewrites or moves files…") applies to the installer, but the change edits one literal of
  the text it writes and no behaviour of removing or moving; I judged it does not match and did not open
  `coding-repository-changer.md`. Say so if the orchestrator reads the row the other way.
- The pinned Ruff stands in the main checkout's `.runs/quality-venv`, not in the worktree; I used it by its
  path, as the linter's own test finds it.

## Unread material

- `guidelines/coding-repository-changer.md` and the other kind files: not opened (reason above).
- The glossary: no term used that needed a search; not read.
- `WAY-141`, `WAY-129`, `WAY-321`, `WAY-392`–`WAY-395`, `WAY-401`, `WAY-38`, `WAY-89`, `WAY-344`, `WAY-418`:
  each read whole from its heading to the next.
- `foundations/part_map.md`: read `instruction-files` and `installation` and the entries
  `installation-command`, `foundation-check-command` (lines 193–254); the rest not read.
- `instruction-files/check_instructions.py`: read its head description (lines 1–60) and found where
  `looks_like_path`, `check_dead_paths`, `dead_path_note` and `main` stand; the bodies of those functions I
  did not read — the behaviour was seen by running the checker on a probe product (below).
- `installation/test_install.py`, `installation/install.py`: read whole.

## Searches not found or unclear

- The index of the orchestrator's selection: not mine to read, as the handoff says.
- WAY-418's *Verification* names no invariant, though the new entry derives from it (WAY-141, for
  comparison, names `installation-claude-guidance`). Step 4.4 of the invariants skill says a decision whose
  verification "calls for" the entry gains it through `record-decision`; WAY-418's does not call for one, and
  the task's *Settlements to record* has no such row, so I left the decision as it is. Question to the
  orchestrator, my recommendation: leave it (the decision's text is unchanged in meaning, and the review's
  comparison with the decision stays an agent's).
- No `invariant:` line was needed for the text of row 1: the sentence of the block is pinned by the existing
  `BLOCK` constant and `test_guidance_*` tests, which cite no invariant.

## Working copies

- `.runs/author/probe` (a product made by a full installation, a clone of the worktree as its remote): made to
  see the checker's output on a real install, removed with `rm -rf .runs/author/probe`; `.runs/author/` is
  empty. Nothing outside `.runs/author/` and the worktree was written, apart from the temporary directories
  of the test run itself (`tempfile`, removed by the tests' cleanup).

## Problems observed

None. One note: `python -B gate/run_tests.py installation` takes about ten minutes (74 tests, most of them a
full installation or a move of the pin); this is the file's existing cost and the new test adds about eight
seconds to it.
