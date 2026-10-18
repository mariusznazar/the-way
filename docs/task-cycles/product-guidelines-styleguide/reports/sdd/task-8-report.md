# Task 8 report

Status: DONE. Commits `2b5bf31` (feat(installation): give products the maintain-styleguide skill and
name the form check of guidelines before a merge) and `9dd9880` (test(installation): show the
guidance's form-check commands judge the product's own guidelines), on
`task/product-guidelines-styleguide`, committed by explicit paths.

## What was done

- `installation/install.py`: `SKILLS` gains `"maintain-styleguide": "product-guidelines/styleguide/SKILL.md"`
  (so the plan writes `.claude/skills/the-way-maintain-styleguide/SKILL.md` and its `.agents/` twin,
  `sibling_names()` names it in every wrapper, and the block's list of other skills names
  `the-way-maintain-styleguide`). `product_guidance()` gains one sentence in its last paragraph, after
  "…report what failed and what stayed unchecked." and before "A check that did not run is never a pass.":

  > Where this repository holds `guidelines/`, run `python -B .the-way/product-guidelines/form_check.py`
  > and `python -B .the-way/product-guidelines/form_check.py --merge-onto <main commit>` before a merge
  > in which a file of `guidelines/` or of `foundations/` changed.

  Built from `SUBMODULE`; the only paths in it are the-way's convention paths (`guidelines/`,
  `foundations/`, `.the-way/…`), none a product chooses (WAY-107). No other code changed: preview,
  confirmation, no-replace and the list of additions of `installation-command` are untouched.
- `installation/README.md`: the `.claude/skills` row names `maintain-styleguide`; the `AGENTS.md` row
  says the checks before a merge include "the form check of `guidelines/`"; the "Check the installer"
  list names the new tests' subject.
- `installation/test_styleguide_installation.py` (new, ordinary test file, no invariant citation):
  1. `test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product` — crafted CRLF
     product files (`foundations/decisions.md`, `guidelines/styleguide-web.md`, an `AGENTS.md` with a
     `## Backlog` naming `docs/backlog/`, `CLAUDE.md` with import, `.gitignore`): preview lists
     `CREATE` for both wrappers and shows the sentence, writes nothing; apply gives byte-identical
     wrappers named `the-way-maintain-styleguide`, pinned commit, `.the-way/product-guidelines/styleguide/SKILL.md`
     as source, all 30 wrappers' sibling sentence naming `maintain-styleguide`; the appended block
     names `the-way-maintain-styleguide` and the sentence and holds none of the product's paths;
     product files preserved byte for byte (or as prefix for the appended two); only `.gitmodules`
     and `.the-way` staged; repeat says "Already installed; no changes" and changes nothing.
  2. `test_guidance_names_both_form_check_commands_and_they_run_in_the_product` — the installed
     `AGENTS.md` names exactly the two commands; after commit, each (with `<main commit>` = the
     product's HEAD) exits 0 with a `note:` when the product has no guidelines, and exits 1 naming
     `guidelines/styleguide-web.md:0: error: the header line *Discipline* is missing` once the product
     holds a broken file (strengthened in `9dd9880`, see weakest point).
  3. `test_block_of_an_earlier_pin_without_the_sentence_is_refused_before_writing` — an `AGENTS.md`
     holding the block without the sentence (the earlier pin's guidance) is refused in preview and
     `--apply` with "differs from this commit's guidance", nothing written (the pin-move path of §8).
- `installation/test_install.py`, `installation/test_installed_guidance.py`,
  `installation/test_lead_installation.py` unchanged (`git diff --stat 96623ed..HEAD` on them: empty).

## TDD evidence

- Pre-change: `python -B gate/run_tests.py installation` exit 0, 30 tests OK —
  `reports/slice-8-pre-installation.txt`.
- RED (test file written, install.py untouched): `python -B -m unittest -v installation/test_styleguide_installation.py`
  exit 1, 3 failures, each for the missing feature — `reports/slice-8-red.txt`:
  test 1 `'CREATE .claude/skills/the-way-maintain-styleguide/SKILL.md\n' not found in` the preview;
  test 2 the sentence not found in `AGENTS.md`; test 3 `assertNotEqual` — the "earlier" block equals
  the current one, since the current guidance lacks the sentence.
- GREEN after the change: same command exit 0, 3 OK — `reports/slice-8-green.txt`.
- After strengthening test 2: exit 0, 3 OK — `reports/slice-8-green-2.txt`. The strengthened
  assertion's failing side is shown by the control in `slice-8-weakest-point.txt` (the same command
  on a root without guidelines exits 0, so a command that checked the-way's own root would fail it).

## Checks (all under `.runs/task-cycles/product-guidelines-styleguide/reports/`, on HEAD `9dd9880`)

Run by `slice8_final.py` in the session scratchpad (the thirteen directories named explicitly, not
`run_checks.py all`); summary in `slice-8-final-checks.json`.

| Command | Exit | Output |
|---|---|---|
| `python -B gate/run_tests.py gate` | 0 | `slice-8-final-tests-gate.txt` — 98 tests OK |
| `python -B gate/run_tests.py elements/decisions` | 0 | `slice-8-final-tests-elements-decisions.txt` — 169 OK |
| `python -B gate/run_tests.py elements/invariants` | 0 | `slice-8-final-tests-elements-invariants.txt` — 233 OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | `slice-8-final-tests-elements-glossary.txt` — 204 OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | `slice-8-final-tests-elements-part-map.txt` — 162 OK |
| `python -B gate/run_tests.py elements/environment-facts` | 0 | `slice-8-final-tests-elements-environment-facts.txt` — 165 OK |
| `python -B gate/run_tests.py relation-model` | 0 | `slice-8-final-tests-relation-model.txt` — 19 OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | `slice-8-final-tests-agent-instructions.txt` — 18 OK |
| `python -B gate/run_tests.py installation` | 0 | `slice-8-final-tests-installation.txt` — 33 OK (30 + 3 new) |
| `python -B gate/run_tests.py instruction-files` | 0 | `slice-8-final-tests-instruction-files.txt` — 104 OK, skipped=5 |
| `python -B gate/run_tests.py task-cycle` | 0 | `slice-8-final-tests-task-cycle.txt` — 41 OK |
| `python -B gate/run_tests.py project-level` | 0 | `slice-8-final-tests-project-level.txt` — 250 OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | `slice-8-final-tests-product-guidelines.txt` — 60 OK |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `slice-8-final-decision-guard.txt` — 0 error(s), 32 warning(s), 5 unchecked |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `slice-8-final-invariant-guard.txt` — 0 error(s), 0 warning(s), 3 unchecked |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | `slice-8-final-glossary-guard.txt` — 0 error(s), 0 warning(s), 5 unchecked |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | `slice-8-final-part-map-guard.txt` — 0 error(s), 0 warning(s), 7 unchecked |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 | `slice-8-final-environment-facts-guard.txt` — 0 error(s), 0 warning(s), 3 unchecked |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `slice-8-final-skill-entry-points.txt` — "entry points are current" |
| `git diff --check 96623ed..HEAD` | 0 | `slice-8-final-diff-check.txt` — empty |

The brief's own checks `gate/run_tests.py installation` and `gate` are the two rows above (run once,
on the committed HEAD).

### Every warning and unchecked line of the final set

- instruction-files, 5 skips (same count as `baseline-tests-instruction-files.txt`): one "no FIFO on
  this platform", four "needs the real path of a link, as on P…" (link-chain tests) — platform skips.
- decision guard, 32 warnings: five check-by dates passed without a review record (WAY-03 line 71,
  WAY-21 line 635, WAY-52 line 1476, WAY-55 line 1558, WAY-69 line 1972, each "check-by date
  2026-10-02 has passed without a review record"); 27 "*Approved by* is the placeholder `merge of
  <request link>`" at lines 293, 5464, 5510, 5555, 5593, 5635, 5686, 5723, 5758, 5815, 5861, 5894,
  5922, 5947, 5973, 5999, 6025, 6051, 6077, 6109, 6143, 6183, 6217, 6251, 6285, 6322, 6356 (the
  WAY-167–192 entries awaiting the request link, plus line 293). 5 unchecked: the lines the log holds
  on the main branch and the versions it gains per number (`--base none`); a change to the template
  without a new version in the log (`--base none`); `TODO` in the log; the copies of a version both
  logs hold; the fingerprints relations carry (each `--merge-onto none`).
- invariant guard, 3 unchecked: identifiers, versions, corrections and the list of violated
  invariants (`--base none`); `TODO` in the entries; the fingerprints the links of the entries carry
  (`--merge-onto none`).
- glossary guard, 5 unchecked: the count of the words of *Avoid*; terms and identifiers that came to
  read alike; the uses of every term whose definition changed (each `--base none`); `TODO` in the
  entries; the terms with no use after the merge (`--merge-onto none`).
- part-map guard, 7 unchecked: the list of parts of `wording-reaches-dependants` and of
  `skills-reach-the-way-sessions` (their tests leave no coverage file); the change path of every
  promise level in use (no command reports them); the dependencies between parts and new or stale
  violations (no dependency-graph command); the list of known violations; the identifiers of the map;
  the lowering of a part's computed criticality (each `--base none`).
- environment-facts guard, 3 unchecked: identifiers and versions (`--base none`); the fingerprints
  decisions carry for facts; the facts nothing names after the merge (`--merge-onto none`).

None of these is new to slice 8 (slice 8 touches no foundation file); all are the no-main state or
the placeholder links the request fills.

## Files changed (`04920a1..9dd9880`)

| File | Added | Removed |
|---|---|---|
| `installation/install.py` | 6 | 1 |
| `installation/README.md` | 4 | 3 |
| `installation/test_styleguide_installation.py` (new) | 169 | 0 |

## Sharpness inputs

- Parts touched: `installation` only (its `Depends on` already names `product-guidelines`).
- Trust-boundary files: `installation/install.py` (WAY-48). The change adds one dict entry and one
  constant sentence; no new read of product input, no new write path, no new subprocess. Crafted
  inputs exercised by the new tests: a CRLF `AGENTS.md` without a block (appended, prefix preserved),
  an `AGENTS.md` holding a block of an earlier pin (refused before writing), CRLF `CLAUDE.md`,
  `.gitignore`, foundation file and a product guidelines file (preserved); the block contains no
  product-chosen path (`docs/backlog/`, `styleguide-web`, `local-data/` asserted absent; WAY-107).
  The existing installer tests (30) still pass unchanged.
- Surface `installation-command`: wording kept; the promised additions are the same three (the
  block's text grows, as it does whenever `SKILLS` grows).
- Irreversible: nothing. Pin level `pinned`: a product moving its pin past this commit gets
  "differs from this commit's guidance" on its old block and removes it, as the README's pin-move
  paragraph already says — the request should carry that line (spec §8).

## Weakest-point check (WAY-164)

- Requirement most likely not met: spec §8 / brief — the guidance's form-check commands, run as named
  from the product root, check the product's `guidelines/`. My first test 2 showed only that both
  commands exit 0 with a `note:` in a product with no guidelines; the-way itself also holds no
  guidelines, so a command that checked the-way's own root (the README warns a guard run inside
  `.the-way` checks the-way's files) would have passed it too.
- Check (manual, then made a test): actor — this executor; method — `slice8_weakest.py` (session
  scratchpad) installs into a fresh temporary product, extracts both commands from the installed
  `AGENTS.md` by regex, commits, adds a malformed `guidelines/styleguide-web.md`, runs both commands
  from the product root; control — `python -B product-guidelines/form_check.py` on the-way's root.
- Observed: both commands exit 1 with six `guidelines/styleguide-web.md:0: error: …` lines
  ("the header line *Discipline* is missing" first) and `6 error(s), 0 warning(s), 0 unchecked`;
  the control exits 0 with "the repository holds no guidelines/". Evidence:
  `reports/slice-8-weakest-point.txt`. The broken-file assertion was then added to test 2
  (`9dd9880`), green in `slice-8-green-2.txt` and in the final installation run.

## Concerns

- Spec §8 and §10 say `installation/test_install.py` `NAMES` gains the skill; per the brief and the
  orchestrator (WAY-03: that file holds tests citing `installation-claude-guidance/1`) it stays
  unchanged and the new ordinary test file carries the coverage. So `test_install.py`'s loops over
  `NAMES` do not cover `maintain-styleguide`; `test_styleguide_installation.py` asserts the same
  things (both wrappers, sibling sentence, block naming) for it. The whole-change reviewer should
  see this reading.
- The sentence's `<main commit>` placeholder follows spec §8 verbatim; the earlier paragraph of the
  block tells how to find the commit and when `none` applies, so no new wording was added for it.

## Final-review fix

Finding (final-review.md, Important 1): "The product guidance runs the form check only for some of
the changes that can break the styleguide" — `installation/install.py:176-179`. Held right: the
template gives `guidelines-form` the *Part* `every` and `guidelines-reference-current` the part
holding `.the-way` (`product-guidelines/template.md:171-175`), so a rename of a file `## Where in code`
names, or a moved pin, can break guidelines in a change that touches neither `guidelines/` nor
`foundations/`, and nothing else in a product runs the check.

- **Change** (commit `896071a`, fix(installation): name the form check of guidelines before every
  merge, since a rename or a moved pin breaks guidelines whatever files a change touches): the
  sentence now reads "Where this repository holds `guidelines/`, run
  `python -B .the-way/product-guidelines/form_check.py` and
  `python -B .the-way/product-guidelines/form_check.py --merge-onto <main commit>` before every
  merge." `SENTENCE` in `installation/test_styleguide_installation.py` updated to it, with a comment
  naming why. Files: `installation/install.py` +1 −1, `installation/test_styleguide_installation.py`
  +4 −2. `installation/README.md` unchanged (its row "running the checks before a merge, the form
  check of `guidelines/` included" stays true).
- **RED** (test expectation changed first, install.py untouched):
  `python -B -m unittest -v installation/test_styleguide_installation.py` exit 1, 3 failures, each
  the new sentence not found / the earlier block equal to the current one —
  `reports/slice-8-fix-red.txt`.
- **GREEN:** same command exit 0, 3 OK — `reports/slice-8-fix-green.txt`.
- `python -B gate/run_tests.py installation` exit 0, 33 tests OK — `reports/slice-8-fix-tests-installation.txt`.
- `python -B gate/run_tests.py gate` exit 0, 98 tests OK — `reports/slice-8-fix-tests-gate.txt`.
- `git diff --check 96623ed..HEAD` exit 0, no output.
- Out of this fix: spec §8 (`.runs/task-cycles/product-guidelines-styleguide/spec.md:628-631`) still
  gives the old trigger word for word; the root decides whether the spec or the request records the
  revision. The review's Minor findings (incl. Task 8 M1, M2) are not addressed here.
