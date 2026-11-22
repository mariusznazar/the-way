PASS 325af47326fac414cea8476c1a202124ef348df7

# Review of the return step's commits — installer-foundation-check-full-path

Range: `674c93feda110b00fab3327546a41ca26ac5e860..325af47326fac414cea8476c1a202124ef348df7`, one
commit (`325af473`, "Return step: the README of the installer lists the test of a fresh
installation's AGENTS.md"), which changes `installation/README.md` alone (+2 / -1).
`git rev-parse HEAD` = `325af47326fac414cea8476c1a202124ef348df7`, the head given.

## Findings

### Critical

none

### Important

none

### Minor

1. **`installation/README.md:287-288` — the new item says "drawing no warning", while the test it
   names also refuses an error.** The item reads "the root `AGENTS.md` of a fresh installation
   drawing no warning of `instruction-files/check_instructions.py`". The test
   `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`
   (`installation/test_install.py:456-458`) refuses every line matching
   `(?:ERROR|WARN) +\S+ AGENTS\.md:`, so it holds "no error and no warning". This is the same gap as
   the known Minor finding on the invariant `installation-agents-md-warnings`
   (`foundations/invariants.md:336`), now repeated in the README: whoever corrects the invariant's
   sentence should correct this item with it, or the two will say less than the test in two places.
   Minor: the README lists what the tests check, and a reader who learns "no warning" is not misled
   into thinking an error would pass — an error is the worse form of the same break, and line 83 of
   the same README already says an error stops the tests. Within the task (the README section that
   lists the tests of the installer).

No other finding. What I checked against the return step's report:

- **The README change is true to the test.** The test installs into an empty product with
  `--apply` (a fresh, full installation), asserts no `.runs/` exists, runs
  `.the-way/instruction-files/check_instructions.py` on the product's root and refuses a warning
  (and an error) on `AGENTS.md`; the README item says the same, with the one gap above. The path
  `instruction-files/check_instructions.py` is written relative to the-way's root, as the same
  section names `elements/common/foundation_check.py` at line 269, which fits a section about
  the-way's own tests.
- **The rest of the section stays true.** The item sits in the list of what the tests check,
  after the guidance items it belongs with; no other item of the list describes the new test, and
  "the four warnings" (line 299) are the installer's own warnings, not the instruction check's.
  The section's command `python -B gate/run_tests.py installation` runs `installation/test_install.py`,
  which holds the test.
- **The report's comparison of entries and code.** The invariant `installation-agents-md-warnings`
  (`foundations/invariants.md:334-342`) says "a full run of the installation command, before any
  skill of the-way has run in it … reports no warning on the root `AGENTS.md` that the run
  created"; the test builds that product, checks the precondition and refuses the warning. WAY-418's
  *Verification* (`foundations/decisions.md:3349`) names the invariant, and the invariant names
  WAY-418 in *Derives from*. The invariant's identifier occurs in the invariant, in WAY-418 and in
  the test's `# invariant:` line alone (my own search, below). I found no mismatch the return step
  missed beyond the known one.
- **Other text of `installation/README.md`** that touches the instruction check: lines 82-89 (the
  product adds the check to its one command; a warning is the change's to fix as an error is) stay
  true and agree with WAY-418.
- **The task's *Settlements to record*:** row 1 (the full path in the sentence) and row 2 (the
  invariant) are both in the tree at the head; the return step adds no choice beyond them.
- **Trust boundary:** the range changes no code; `installation/install.py` is unchanged in it.

## Declined to judge

- The invariant's sentence and WAY-418 themselves — reviewed at `674c93fe`, not under review again
  by the handoff; I compared them only for a mismatch the return step missed.
- The width of the README's lines (line 287 now runs past 100 characters, as the line before the
  change did and as lines 299 and 302 do): the guidelines I searched set no rule for the width of
  Markdown lines, so I found no consequence to name.

## Checks

- `git diff 674c93feda110b00fab3327546a41ca26ac5e860..325af473` and `git log --stat` of the same
  range — read; one commit, one file.
- `python -B elements/common/foundation_check.py` (worktree at head, clean) — exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .` (worktree at head) — exit 0,
  `0 error, 0 warn, 5 info`.
- `python -B -m unittest installation.test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning installation.test_install.InstallTest.test_guidance_points_to_sections_the_pinned_commit_holds`
  — exit 0, 2 tests OK (the first is the test the README names; the second reads
  `installation/README.md` at the pinned commit for the sections the block names).
- `git status --short` before and after the runs — empty both times; the reviewed worktree was not
  changed.
- Not run: `python -B gate/run_tests.py installation` and the full gate — the range changes one
  Markdown file, the handoff says no full gate, and the two tests above are the ones that read the
  changed file or that the change names.

## Reaches beyond the dispatch

- `installation/README.md:78-93` and the search for `check_instructions` in `installation/` — to
  check the rest of the README that speaks of the instruction check against the new item.
- `instruction-files/*.md`, searched for `installation|installer` — whether the instruction-files
  part describes the installer's test anywhere that would need the same item; it does not.
- `guidelines/`, searched for a rule on the width of Markdown lines — for the line-width question
  under Declined to judge; none found.
- `installation/test_install.py:380-458` — the neighbouring guidance tests, to judge where the new
  README item stands in the list.

## Working copies

None made: the checks needed no file changed, so they ran read-only in the reviewed worktree;
`.runs/review-return/` was never created, and nothing remains to remove.

## Unread material

- `.runs/task-cycles/installer-foundation-check-full-path/task.md` — read whole.
- `foundations/invariants.md` — the entry `installation-agents-md-warnings` read whole (lines
  334-342), the rest not read, as the method gives.
- `foundations/decisions.md` — WAY-418 read whole (lines 3339-3359), the rest not read.
- `installation/README.md` — read lines 78-93 and 255-314, not the whole file.
- `installation/test_install.py` — read lines 380-480, not the whole file.

## Searches not found or unclear

- A rule on the width of Markdown lines in `guidelines/` (`wrap|100 char|line length|columns|Markdown`,
  case-insensitive) — not found; the one hit on "Markdown" in `guidelines/coding.md:52` speaks of
  code examples, not line width.
