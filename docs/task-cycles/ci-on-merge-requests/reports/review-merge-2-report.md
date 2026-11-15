PASS cde07ddcb21527561cb313ff10a4c3e7aa944cc4

# Review of the second merge of the target branch (correction 2)

Reviewed: merge commit `cde07dd` (first parent `2e83447`, the task branch after correction 2;
second parent `9cbc6b2`, `foundations`). Merge base `7f5c5a5`, confirmed with
`git merge-base 2e83447 9cbc6b2`. `git rev-parse HEAD` in my worktree gave
`cde07ddcb21527561cb313ff10a4c3e7aa944cc4`, the head I was given. Method:
`task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` at `cde07dd`. The question the handoff
asks bounds this review: do the two sides still hold together?

## Findings

None: no Critical, no Important, no Minor finding.

## Question 1: the four files that both sides changed

The merge kept both sides whole, and I checked that mechanically for every file, not only the four
that both sides changed. I stripped two diffs down to their changed lines (`+`/`-`, without the
`+++`/`---` file lines) and compared them:

- The task's side: `git diff 7f5c5a5 2e83447` against `git diff 9cbc6b2 cde07dd`. `diff` exit
  0: the merge adds to the target exactly the lines the task added to the base.
- The target's side: `git diff 7f5c5a5 9cbc6b2` against `git diff 2e83447 cde07dd`. `diff` exit
  0: nothing of the target's was lost or changed.
- The lists of changed files match on both sides (`diff` of the `--name-only` lists, exit 0 twice).

How each shared file reads in the merged tree:

- `task-cycle/skill/SKILL.md`: both changes are in step 12. The target's change (lines 572–577)
  adds `task-cycle/cycle_stages.py` to the scripts whose exit code 2 is recorded as a check that did
  not run. The task's paragraph (lines 589–602) adds the wait for CI on the last pushed head, the
  red result handled as a failed gate, and the exception for a flaky check outside the task's scope
  (WAY-261). The two read consistently: both record a check that did not run under *Checks* and never
  read it as passed. The task's other change, in step 9 (the request left blocked, with no wait for
  CI), stands unchanged at line 438. The target changed no step number and no heading, so the
  references "step 12 of `task-cycle/skill/SKILL.md`" in `record_template.md`,
  `request_template.md`, `correction.md` and `agent-instructions/README.md` still point at the
  right step.
- `foundations/part_map.md`: in *agent-instructions* the task added `.github/workflows/**`, and in
  the *Depends on* of *installation* it added `instruction-files`; both are present. The target's
  change is a sentence in the description of *product-guidelines* (the test of dead pointers in
  skills). It touches neither of the task's lines, and the *Depends on* of *product-guidelines*
  already names `project-level`, whose skills that test reads.
- `installation/README.md`: the task added the `AGENTS.md` row of the table, the paragraph on
  `check_instructions.py`, the section "Run the one command in CI" and a line of the test
  description. The target's change is the paragraph on the check of tracked private paths: the four
  Markdown endings and the UTF-16 byte order mark. They sit in different paragraphs, and the task's
  section follows the target's paragraph with no overlap.
- `foundations/decisions.md`: I compared the decision log's entries with
  `elements/common/compare_log_entries.py` across the four commits:
  - base against task: WAY-09, WAY-16, WAY-160 and WAY-206 differ (exit 1), the task's four entries;
  - base against target: WAY-321, WAY-344 and WAY-339 differ (exit 1);
  - target against merge: only the task's four differ (exit 1), so the target's entries come into
    the merge byte for byte;
  - task against merge: only WAY-321, WAY-344 and WAY-339 differ (exit 1), so the task's four
    entries come into the merge byte for byte.

  No entry is reported as standing in only one copy: the merge brought in no new decision.

## Question 2: the target's new rules and checks against the task's change

- WAY-321, read whole. Its only change is in the binding sentence: "other than Markdown" becomes
  "whose name does not end in `.md`". The task's README sentence that cites WAY-321 (the product's
  command runs `foundation_check.py` without `--skip-test-citations`, "so that the command reports an
  invariant that reads `test` and which no test cites") still says what the entry says. The task
  changes no `invariant:` citation.
- WAY-344, read whole. The changes concern the command that counts the audit: a file of a tool the
  cycle itself changed is not read, a table of the register of problems may lack a level, the cache
  write columns, and the entry `repository`. The *Verification* now names the generator of agent-type
  copies, whose definitions the task does not change. The task adds no script and does not rework
  how any script reads a file: the change to `install.py` only adds text to a string. It adds no part
  to the part map, so the *Scope* clause does not apply.
- WAY-339, read whole. A new series of measures now starts with a change of
  `task-cycle/cycle_stages.py`, and a cycle that changes a tool that measures gives that tool's
  measures as unknown. The task changes none of the measuring tools (`cycle_stages.py`,
  `cycle_measures.py`, `gate_times.py`, `gate/run_tests.py`). Its CI file runs `gate/run_tests.py`
  but does not change it. `process-audit/audit_count.py` reads no table of *Verification* in a
  record (grep: it names *Verification* only in messages and docstrings), so the CI row the task adds
  to the record template meets no reading by the audit count.
- The checks of private paths (`private_paths_check.py`, `tracked_private_paths_check.py`). They
  now list a drive written as part of an address (a slash, then a drive letter and a colon, then a directory) and read note links in files ending in
  `.markdown`, `.mdx` and `.mdc`. `task-cycle/test_tracked_files_private_paths.py`, which runs that
  check over every tracked file, passed on the merged tree within `gate/run_tests.py task-cycle`. So
  no file of the task, `tests.yml` and the new README section included, gives a hit under the widened
  patterns. The links the task's step 12 asks to write into *Checks* are `https://` URLs, which the
  new pattern excludes: there is a word character, or a slash or colon, before any slash followed by a drive letter and a colon.
- The process remarks check (`remarks_check.py`). It now opens a section on the line under a list
  item. The task changes no report form that this check reads (the record template and request
  template changes are prose about the CI row), and the task-cycle tests passed.
- The new test of dead pointers in skills (`product-guidelines/test_skill_references.py`). It reads
  only the skills of `product-guidelines/` and `project-level/`. The task's one change there,
  `product-guidelines/coding/settle.md`, adds no pointer to a file, step or heading. The test treats
  `.github/` paths as a product's. No pointer of those skills into `task-cycle/skill/SKILL.md`
  breaks: the task removed no heading and no step. The test passed.
- How Markdown endings are tracked, and the glossary terms "Markdown file" (new) and "repository
  instruction file" (now `.md` or `.mdc`). The task's added text uses the word "Markdown" nowhere.
  Its README and installer block name `installation/README.md` (`.md`) in backticks, the same at the
  base and on both sides. `instruction-files/check_instructions.py` now follows `.mdc` files as well
  as `.md`; that does not change what it follows from the task's block. Its tests and those of
  `agent-instructions` passed.
- The changed invariants (`test-method-citation`, `audit-series-script-paths`,
  `guidelines-file-place`). None is cited by a test the task changed, and the foundation check
  reports 0 errors.
- Trust boundary. `git diff 2e83447 cde07dd -- installation/install.py .github/workflows/tests.yml`
  printed nothing (exit 0): the merge changes neither file the change's trust boundary lies in.

## Fix and correction status

This is a review of the reconciliation with the target branch, not of a fix's findings file or of
the human's remarks. Correction 2 was reviewed and passed earlier (`PASS 2e83447`). Its result comes
into the merge unchanged: every changed line of `7f5c5a5..2e83447` stands in `9cbc6b2..cde07dd`.

## Declined to judge

- The Minor findings of earlier reviews that stand in the request's list. The handoff names them as
  not mine to re-judge.
- The target branch's own changes on their merits (audit count, stage script, the new test). They
  came in through the merged request 132 and its own review; I judged them only where they meet the
  task's change.

## Checks run

On the merged tree at `cde07dd`, in my worktree, one at a time:

| Command | Exit code | Result |
|---|---|---|
| `git merge-base 2e83447 9cbc6b2` | 0 | `7f5c5a5…` |
| `git diff 2e83447 cde07dd -- installation/install.py .github/workflows/tests.yml` | 0 | empty |
| changed-line comparison, task side (`diff` of stripped `git diff 7f5c5a5 2e83447` and `git diff 9cbc6b2 cde07dd`) | 0 | identical |
| changed-line comparison, target side (`diff` of stripped `git diff 7f5c5a5 9cbc6b2` and `git diff 2e83447 cde07dd`) | 0 | identical |
| `python -B elements/common/compare_log_entries.py` base→task, base→target, target→merge, task→merge | 1, 1, 1, 1 | differences as listed under question 1, all expected |
| `python -B elements/common/decision_index.py --output … --sections .` | 0 | 28 sections |
| `python -B elements/common/decision_index.py --output … --section "Scripts and the gate" --section "Instruction files" --section "The-way and how a product takes it" --part` for each of the 10 parts `--decision WAY-321 --decision WAY-339 --decision WAY-344 .` | 0 | index of 333 lines |
| `python -B elements/common/foundation_check.py` (no `--skip-test-citations`) | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` | 0 | 242 tests OK |
| `python -B gate/run_tests.py installation` | 0 | 61 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 27 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 105 tests OK, 5 skipped |
| `python -B gate/run_tests.py task-cycle` | 0 | 514 tests OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests OK |

Checks I could not run:

- The task's own CI run on Linux of the merged tree, which would include the target's new tests:
  `cde07dd` is not pushed (the branch is 41 commits ahead of `origin`, and the open request #127
  stands at `9a00830`). The 5 tests skipped in `instruction-files` need POSIX, and they and the
  target's new tests get their Linux run only when the cycle waits for CI after the push (step 12).
- The full gate: the orchestrator runs it, as the handoff gives.

## Reaches beyond the dispatch

- `process-audit/audit_count.py`, a grep for `Verification|Checks`: to see whether the audit reads
  the *Verification* table where the task adds the CI row (it does not).
- The docstring and first 60 lines of `product-guidelines/test_skill_references.py`: to see which
  skills it reads and how it treats `.github/` paths.
- The target's diffs of `agent-instructions/test_instruction_files.py`,
  `elements/part-map/test_cross_part_imports.py`, `foundations/glossary.md` and
  `foundations/invariants.md`: to judge where they meet the task.

## Working copies

- A detached worktree of `cde07dd` at
  `.runs/review-merge-2/wt`. Removed with
  `git worktree remove --force` (exit 0), then `git worktree prune` (exit 0).
- Logs, the four copies of the decision log and the indexes, in
  `.runs/review-merge-2/logs` and `…\cmp`. Removed
  with the whole directory `.runs/review-merge-2` (`rm -rf`, exit 0). Nothing is kept in `reports/`
  beyond this report; the results it needs are quoted above.

## Unread material

- `elements/common/way_of_working.md`: I read only the section "Reading the foundation", the one
  the handoff names.
- The decision index of my selection (333 lines): of its decisions I read whole only the three the
  merge changed (WAY-321, WAY-339, WAY-344). The other decisions are the same at `2e83447` and at
  `cde07dd` (the comparison of entries shows no other difference), so the merge brought in nothing
  new there for this review. The earlier reviews of the change judged them.
- The task's four entries (WAY-09, WAY-16, WAY-160, WAY-206): their bytes are compared, not re-read
  whole, since they come into the merge byte for byte and were judged in the earlier reviews.
- `product-guidelines/test_skill_references.py` beyond its first 60 lines, and
  `process-audit/audit_count.py` beyond the grep.

## Searches not found or unclear

- `decision_index.py --decision 321` ended with exit 2 (`no decision 321`). The switch takes the
  full identifier (`--decision WAY-321`), which the method's wording `--decision NUMBER` in
  `elements/common/way_of_working.md` does not show.
