PASS 3bd9e37b60cb4c91613dddfa517c445841016688

# Review of slice 5 — the installer brings `maintain-testing-guidelines` to products

Range `467a2af..3bd9e37` (one commit, `3bd9e37`), worktree
`C:/Storage/repos/the-way-wt/testing-guidelines`, `git rev-parse HEAD` = the given head.
Blocking: 0. Minor: 1. Out of scope: 1.

## What the slice does, checked against D7 and task item 2

- `installation/install.py:44` adds `"maintain-testing-guidelines": "product-guidelines/testing/SKILL.md"`
  to `SKILLS`, and nothing else in the installer changes — as D7 requires ("No new mechanism").
- `installation/test_testing_guidelines_installation.py` is a rename-only copy of
  `installation/test_coding_guidelines_installation.py` (checked with `diff`: only the docstring,
  `SKILL_SOURCE`, `NAME`, class/test names, temp prefixes, the product path `guidelines/testing.md`
  and the sibling regex differ). It covers every point D7 lists: preview lists both `CREATE` lines
  and changes nothing; `--apply` creates both entry points byte-identical with the skill's
  description and the `.the-way/product-guidelines/testing/SKILL.md` path; 40 siblings each naming
  `maintain-testing-guidelines`; the block naming `the-way-maintain-testing-guidelines`; repeat run
  changes nothing; foreign file / directory / non-UTF-8 file at the new path in `.claude` and
  `.agents`, preview and `--apply`, non-zero exit, tree unchanged, nothing staged.
- Counts 38 → 40 in `installation/test_coding_guidelines_installation.py:97` and
  `installation/test_styleguide_installation.py:91`, kept exact.
- `installation/README.md:57` (table) and `:172` (list of checks) name the skill.
- `installation/test_install.py` unchanged; its `NAMES` tuple (`:19-35`) was already a partial list
  (it lacks `maintain-styleguide` and `lead-project`), so leaving it is consistent.

## Trust boundary (WAY-48)

Checked by a scratch probe against the head's installer, each case in `.claude` and `.agents`,
preview and `--apply` (16 runs): a non-UTF-8 file, a symlinked `SKILL.md` pointing outside the
product, the skill directory itself a symlink to a directory outside the product, and a file that
imitates an installer entry point but names another skill (`the-way-critique`). Every run exited 1
with nothing written (tree equal before/after, symlink targets untouched) and `git ls-files --stage`
empty. The file cases stop with `Existing integration file differs: <path>` (`owned_entry_point`,
`installation/install.py:292-306`); the symlinked directory stops with `Parent path is not a regular
directory` (`check_parents`, `:284-289`). The refusals happen in `plan()` before any write or
staging. The slice adds a constant path and no parsing; the skill text comes from the-way's commit
(`committed`), not from the product. Nothing found that a crafted file at the new path can make the
installer do beyond refusing.

## Findings

### Critical

None.

### Important

None.

### Minor

1. **`installation/test_testing_guidelines_installation.py:149-155` — the non-UTF-8 case is exempted
   from the refusal assertions on a false premise (ruling C9).** The comment says "The non-UTF-8 case
   stops on an uncaught UnicodeDecodeError (pre-existing, C37)". That is not true at this head:
   `owned_entry_point` catches `UnicodeDecodeError` and returns False (`installation/install.py:299-302`,
   added in `24f7f44`, after the coding test the comment was copied from), so the installer refuses
   the non-UTF-8 file with the same `Existing integration file differs: …\.claude\skills\the-way-maintain-testing-guidelines\SKILL.md`
   as the other crafted files — shown by running the installer exactly as the test does (text mode,
   UTF-8), preview and `--apply`, exit 1. Consequence: the test cannot tell a clean refusal from a
   crash. Mutation evidence: removing the `try/except` in `owned_entry_point` in a scratch worktree
   (so a non-UTF-8 entry point crashes with a traceback) leaves this test passing and the whole
   `python -B gate/run_tests.py installation` passing (44 tests, exit 0). Why Minor, not Important:
   the requirement D7 states — non-zero exit, tree byte for byte, nothing staged — is met and
   asserted, and the unprotected regression would cost the user a traceback in place of a message,
   with nothing written. Fix: drop the `if kind != "non-UTF-8 file":` exemption and the comment, so
   all three crafted kinds assert the message, the directory and `NAME` (the probe shows all three
   pass at this head). The false "C37" reference also points at a question of another cycle that
   means nothing in this file.

### Out of scope

1. The same stale comment and exemption in `installation/test_coding_guidelines_installation.py:149-155`
   (pre-existing since `2eabf42`; this slice touches that file only for its count). Out of scope:
   not part of slice 5's goal; Minor; could be fixed together with finding 1.

## Declined to judge

- The wording and content of `product-guidelines/testing/SKILL.md` (slice 3), read by the installer
  here only for its `description:` line — outside this slice.
- The accuracy of spec D7's line references (`install.py:343-346` etc.) — the spec is not this
  slice's output.

## Own-work check of the executor

It named the refusal at the new path as the weakest point — that fits. Its check (the new test
passing) would catch a missing refusal for the foreign file and directory (shown: with the `SKILLS`
line removed, all foreign-file and directory subtests fail), but for the non-UTF-8 file it would
not catch a crash replacing the refusal — finding 1. Its C9 note repeats the comment's false
premise without having checked it.

## Checks run

- `python -B installation/test_testing_guidelines_installation.py -v` (reviewed worktree, writes only
  temp dirs) — 2 tests OK, exit 0.
- `python -B installation/test_coding_guidelines_installation.py` — 2 tests OK, exit 0.
- `python -B installation/test_styleguide_installation.py` — 2 tests OK, exit 0.
- `python -B elements/common/foundation_check.py` — exit 0.
- `git diff --check 467a2af..3bd9e37` — empty, exit 0. `git ls-files --eol` on the three changed
  files: `i/lf w/lf`, unchanged style.
- Failing-first, in a scratch detached worktree of `3bd9e37` with the `SKILLS` line removed:
  `python -B installation/test_testing_guidelines_installation.py` — exit 1; the crafted subtests
  fail (installer exits 0 with nothing owned at the path).
- Mutation, same scratch worktree, `try/except UnicodeDecodeError` removed from `owned_entry_point`:
  the new test's crafted case OK, exit 0; `python -B gate/run_tests.py installation` — 44 tests OK,
  exit 0 (237 s). Scratch worktree removed afterwards.
- Manual probe (scratch script, 16 runs) of crafted shapes at the new path — results under
  *Trust boundary*; plus a text-mode run of the non-UTF-8 case showing the clean refusal message.
- Not run: the full installation suite on the unmodified head (the cycle's own run; the executor
  reports exit 0, 44 tests) — only on the mutant above.

## Reach beyond the dispatch

- `installation/install.py:284-306, 337-412, 484-600` — to check the refusal path and that refusals
  precede any write or `git add` (trust-boundary check).
- `git log -S` on `installation/install.py` and the coding test — to date the `try/except` (`24f7f44`)
  against the comment (`2eabf42`) for finding 1.
- `installation/test_install.py:19-35` and a grep for non-UTF-8 cases in `installation/test_*.py` —
  to see whether any other test asserts the non-UTF-8 entry-point refusal (none does; the `\xff\xfe`
  cases there are for `AGENTS.md`/`CLAUDE.md`).
- `foundations/decisions.md` WAY-48 whole — the boundary rule the handoff names.
