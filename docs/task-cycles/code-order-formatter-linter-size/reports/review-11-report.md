PASS 679112e3bf1225559d129d949473e12ed6520546

# Review of slice 11 (four over-long functions at three parts' trust boundaries divided)

Range `462add5d..679112e3` (three commits: `612146a2`, `72150951`, `679112e3`), `git rev-parse HEAD` in the
worktree is `679112e3bf1225559d129d949473e12ed6520546`. Changed files (`git diff --stat`):
`installation/install.py` 147 lines changed, `instruction-files/check_instructions.py` 39,
`project-level/plan_check.py` 90, `project-level/plan_state.py` 487; 456 insertions, 307 deletions.

## Findings

### Critical

none

### Important (blocking)

none

### Minor

none

### Out of scope

none

## What I verified

- **Each function stands at most 110 lines.** `function_sizes` of `agent-instructions/test_size_invariant.py`
  on the four files at the head: no function over 110. Largest per file: `install.py` `plan` 109 (outside the
  slice, unchanged) then `run` 58; `check_instructions.py` `check_layout` 88, `check_file` 23;
  `plan_check.py` `read_tasks` 89, `check_header` 69; `plan_state.py` `observe` 63, `task_report` 60,
  `provenance` 23. The parts moved out each have a name of their own and a docstring (`print_submodule_actions`,
  `print_file_actions`, `print_stale_deletions`, `print_shared_actions`, `apply_submodule`, `write_files`;
  `check_dead_paths`, `check_at_imports`, `check_emphasis`; `check_status`, `check_fingerprints`;
  `record_provenance`, `anchored_parents`, `relation_problem`, `frozen_artifact_problem`, `archived_cycles`,
  `report_verdict`, `TaskEvidence`). None is a cut at an arbitrary line: the "Good" of the rule of size
  (`guidelines/coding.md`, *Size of a function and a file*) is met.
- **Reading of the diff against the old code, function by function.**
  - `install.run`: the preview prints in the old order (submodule, files, stale, shared, warnings); the
    credential refusal, the `Not a directory` refusal, the confirmation, the "already installed" exit and
    `Cancelled` stay in `run` in the old order; the print functions write nothing, so the invariant
    `repository-changer-acts-only-when-told` (WAY-389) and `installation-paths-through-links` are not reached;
    `plan()` is untouched.
  - `check_file`: the old single loop did the `@` import check and the emphasis count; every `continue` of that
    loop is in the inner `for match` loop, so no line skipped the emphasis count. The new `check_emphasis`
    counts the same `prose_lines`; findings keep their order (dead paths, `@` imports, emphasis, size).
  - `check_header`: `check_status` and `check_fingerprints` return finding lists that `check_header` appends
    to the same list in the old position; every `return findings, None` stays in `check_header`.
  - `provenance`: each `continue` of the old loop is mapped to a `(kind, reason)` pair; the order of the
    conditions (copy absent, anchoring, relation, frozen artifact) is the old order; the inversion
    `if not names_plan(...) or name != ...` to `if names_plan(...) and name == ...: return None` is exact;
    `related_plan`/`member_plan` are still computed before the test as before.
  - `task_report`: the seven lists live in one `TaskEvidence`; the helpers mutate the same lists in the same
    order, so on a `GitError` or `UnicodeError` the partial lines, `active`, `archived`, `unchecked`,
    `contradictions` stand as in the old code and `merged` is reset after it, as before. `report_verdict` is
    the old tail, line for line.
- **Same verdict, exit code and message at the boundary files** (my own comparison, base `462add5d` against
  head, both as worktrees in my directory, crafted input):
  - `instruction-files/check_instructions.py`: a tree with a missing path, `//host` and `\\host` network paths,
    a sentence saying a file does not load (English and Polish), `@AGENTS.md`, `@` imports with a trailing
    comma, a missing and a network `@` import, emphasis in and out of a fence in a root file and in a skill,
    `--file` with a readable and a missing file, and a network root: stdout, stderr and exit code are byte for
    byte equal in all five runs (exit 1, 0, 0, 2).
  - `project-level/plan_check.py`: `check()` of base and head on 784 inputs built from the suite's valid plan
    and definition (each line deleted and doubled, five `Status:` variants including an impossible date, a
    swapped fingerprint, a missing and a changed approval fingerprint, each definition line deleted, a missing
    definition and an unreadable one, an empty plan, 600 random one-to-three-character mutations): 493
    distinct finding lists, equal in all 784 (`cmp` of the two result files).
  - `installation/install.py`: on two fresh product repositories (CRLF `AGENTS.md`, plain `CLAUDE.md`), preview,
    `--apply` answered `n`, `--apply` answered `y`, and `--apply` again: output (commit hash and product path
    normalised) and exit code (0, 0, 0, 0) equal, and the product files (less `.git` and `.the-way`) equal;
    a URL with credentials and a missing directory: same message, exit 1.
  - `project-level/plan_state.py`: no crafted-input comparison of my own beyond the suite; the 73 process runs
    of `test_plan_state.py` pass, and the executor's normalised outputs of the same 73 runs, which I did not
    re-run, were compared by the executor with base. My reading of `provenance` and `task_report` above is the
    check of its trust boundary.
- **Foundation.** The slice writes no foundation entry and changes no invariant test. WAY-365 (move out with
  no change of behaviour) and WAY-48 (a trust boundary is checked for crafted input) are met as above;
  F2 (WAY-385, 110 lines) is met for the four files. `check_instructions.py` and `plan_check.py` are `copy`
  and `install.py`, `plan_state.py` `do not copy` in the guideline tables; nothing was added to the `do not
  copy` files that a new file would copy except a small dataclass.
- **Tests that guard the behaviour.** The existing suites are the guard (a move out with no change of
  behaviour needs no new test, WAY-365); they exercise the CLI of each boundary (73 process runs of
  `plan_state.py`, install runs on disposable repositories, `check_instructions` on trees with links and
  oversize files). No test was changed in the range, none asserts nothing, and no code in the range is made for
  a test.
- **Reserved choice:** none taken. **Code made to pass a test:** none found.
- **Executor's claims:** the three claims I could check cheaply held (sizes, ruff, three gates); its
  differential counts I did not repeat beyond the comparisons above. One path it names as unchecked (a
  `GitError` in `archived_cycles` after a first commit was accepted) I read in the code and found the same as
  the old one, but did not run.

## Declined to judge

none

## Checks run (command, exit code)

All in worktrees of mine under `.runs/review-11/` (head and base), `<ruff>` is
`the Ruff of the quality environment of the main checkout`.

- `git rev-parse HEAD` in the reviewed worktree: `679112e3bf1225559d129d949473e12ed6520546`, as given.
- `<ruff> format --check --config ruff.toml <four files>` — exit 0 ("4 files already formatted").
- `<ruff> check --config ruff.toml --ignore-noqa <four files>` — exit 0 ("All checks passed!").
- `function_sizes` of `agent-instructions/test_size_invariant.py` on the four files (python -B script) —
  exit 0, no function over 110 (numbers above).
- `python -B gate/run_tests.py installation` — exit 0, 73 tests OK (432 s).
- `python -B gate/run_tests.py instruction-files` — exit 0, 105 tests OK, 5 skipped (platform skips: no FIFO,
  needs the real path of a link as on POSIX).
- `python -B gate/run_tests.py project-level` — exit 0, 281 tests OK (145 s).
- The three differential comparisons of the trust-boundary files (method and results above) — each exit 0,
  `cmp` equal. Test outputs and the plan-check comparison script are kept in
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-11-checks/`.
- Not run, on purpose: the full gate (`python -B gate/run_tests.py` without a directory), as the handoff says.

## Reaches beyond the handoff

- A search of the repository's `.md` and `.py` files for `check_file`, `check_header`, `task_report`,
  `install.run` and `plan_state.provenance`, to see whether a document or test names a function this slice
  moved: only unrelated functions of other files matched; nothing cites the moved ones. Why: a rename-free
  move should leave no reference, and this confirmed it.
- The test file `project-level/test_plan_check.py` of the head, loaded as a module to take its valid plan and
  definition as seeds for my comparison. Why: seeds for crafted input that fit the plan's form.

## Working copies and their removal

- `.runs/review-11/wt` (worktree of `679112e3`) and `.runs/review-11/base` (worktree of `462add5d`): removed
  with `git worktree remove --force`, then `git worktree prune`; `git worktree list` no longer names them.
- `.runs/review-11/` held my crafted-input trees (`cases/`), two product repositories (`prod_base`,
  `prod_wt`) with their outputs and result files: removed, the directory is empty.
- Kept in `reports/review-11-checks/`: `t_installation.txt`, `t_instruction-files.txt`, `t_project-level.txt`
  (test outputs) and `pc_diff.py` (the plan-check comparison script).
- No remainder.

## Unread material

none read in part among what the handoff names, with these exceptions: `foundations/part_map.md:81-100` and
`:183-203`, `task.md` outside the lines the slice's *Read* names, and `guidelines/coding-command-runner.md`,
`-generator.md`, `-shared-module.md` (not named by the handoff) stayed unread; the part map was not needed
because the handoff names the trust-boundary files. Read whole: the review method, `guidelines/coding.md`,
`coding-check.md`, `coding-measuring-report.md`, `coding-repository-changer.md`, the executor's report, WAY-365,
WAY-48 and the invariant entries by the line ranges the handoff gives (the *Read* ranges by address are
shifted by a few lines against the current file, as the handoff's own list of current ranges says; I read the
ranges at the current addresses), `task.md:32` and `:62-68`, and `agent-instructions/test_size_invariant.py`
(to line 80, the counting functions, which is all the check uses). F2 (WAY-385) I read through the answer of
`task.md:62-68` and the text of the thresholds, not as its whole entry.

## Searches not found or unclear

- The *Read* of the slice gives addresses (for example `foundations/decisions.md:6615-6651`) that stand a line
  or two off the "current ranges" the handoff lists (`6616-6653`); not a finding, the listed current ranges
  were used.
- The emphasis finding did not appear in my first crafted tree (no word of the `EMPHASIS` pattern in it); I
  added one with words of the pattern and it came out equal on base and head.
