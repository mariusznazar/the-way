# Author return report — installer-foundation-check-full-path

**Status:** done

**Commit:** `325af473` (on `task/installer-foundation-check-full-path`, after `674c93fe`):
`installation/README.md` +2 / -1. Nothing else needed a correction.

## What I compared with the code

- **The entries the change wrote or changed:** the invariant `installation-agents-md-warnings`
  (`foundations/invariants.md:334`) against the test that cites it
  (`installation/test_install.py:435`) and the block (`installation/install.py:207`); WAY-418's
  *Verification* (`foundations/decisions.md:3349`) against the invariant (the identifier matches, the
  invariant names WAY-418 in *Derives from*, the pair of examples stays for the part no invariant holds).
  They match, apart from the one point below.
- **Entries the task names and the search of the foundation found** (the handoff's list: WAY-141, WAY-129,
  WAY-321, WAY-392–395, WAY-401, WAY-38, WAY-89, WAY-344, `installation-claude-guidance`,
  `installation-paths-through-links`): no sentence of them is made false by the block's new wording; the
  invariants about the block's other claims are held by tests that did not change.
- **My own search by the names and words the code adds:**
  - `Until the part map has|first parts|claimed by no part` outside the log: only `install.py`,
    `test_install.py` and `installation/README.md:270`, which describes the same report in prose and names
    the script by its path `elements/common/foundation_check.py` already.
  - `installation-agents-md-warnings`: the invariant, WAY-418's *Verification*, and the one test; no other
    file carries it.
  - `foundation_check.py` as a bare name in `.md` files: 19 hits in the element templates, the README and
    `product-guidelines/template.md`; each speaks of the script itself in the-way's own text and none is a
    path the instruction check reads in a root instruction file, and none copies the block's sentence.
  - `ERROR`/`WARN` and `looks_like_path` in the Markdown of `installation`, `instruction-files` and the part
    map: no hit; the instruction check's own description (head of `check_instructions.py`) already says a
    warning is the change's to fix as an error is.
- **The part map** (`installation`, `instruction-files`, the entries `installation-command` and
  `foundation-check-command`, `foundations/part_map.md:193–254`): the part descriptions and the
  `installation` -> `instruction-files` dependency the test relies on stand as they are; the interface entries
  say nothing the change moved.
- **`installation/README.md`:** the row `AGENTS.md` of "Files in the product" describes the block in general
  terms and stays true; the paragraph "A warning is the change's to fix as an error is" stays true. The
  section "Check the installer" lists what the tests of the installer hold and did not list the new test;
  that was the one mismatch. Corrected: it now reads "…guidance naming only scripts and README sections the
  pinned commit holds, the root `AGENTS.md` of a fresh installation drawing no warning of
  `instruction-files/check_instructions.py`, a moved pin…".

## Sentence and test (the fix's Minor finding)

The invariant says "no warning"; its test also refuses an `ERROR` line on `AGENTS.md`, as the handoff names.
My search finds no further disagreement: the test's other assertions (the precondition that no `.runs/`
directory exists, the count line of the checker) are guards, not claims the sentence lacks, and the sentence's
"that the run created" matches the test, which builds an empty product. I changed neither, as the handoff says.

## Return step items

- Decisions written or changed in the return step: none. (WAY-418's *Verification* was edited in the fix, not
  here.)
- Invariants written or changed: none in this step (`installation-agents-md-warnings` came with row 2 in the
  first stage).
- Environment facts: none — the change rests on no source outside the product.
- Glossary terms: none — no word is used in a meaning WAY-95 gives an entry.
- Part-map changes: none.
- Projected entries: none.
- Rows of *Settlements to record*: row 1 (the block's sentence with the full path) went to the code and its test
  in the first stage, `installation/install.py` `product_guidance` and `BLOCK` in
  `installation/test_install.py`; row 2 went to the invariant `installation-agents-md-warnings` in
  `foundations/invariants.md`. Neither was missed, and no choice binds after the merge that is not already one
  of the two rows.

## Checks

- `python -B elements/common/foundation_check.py`: exit 0, `0 errors` (README added to git before the run).
- `python -B instruction-files/check_instructions.py .`: `0 error, 0 warn, 5 info`.
- `python -B -m unittest installation.test_install.InstallTest.test_guidance_points_to_sections_the_pinned_commit_holds installation.test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`:
  exit 0 (the README is read by the first, as the section holder of the block; the second is the invariant's
  test).
- Not run: `python -B gate/run_tests.py installation` — this step changes one Markdown file the installation
  tests read only for the sections the block names (unchanged); the tests of the code were run in full at
  `674c93fe` (exit 0, 74 tests) and no code changed since. Not run: the full gate, as the handoff says.

## Unread material

- `elements/glossary/skill/SKILL.md` and the glossary: not read; no term of the change needed an entry.
- `foundations/part_map.md`: read lines 193–254 only, as in the first stage.
- `reports/review-whole-report.md`, the review's reports: not mine.

## Searches not found or unclear

none

## Working copies

None made in this step; `.runs/author/` is empty.
