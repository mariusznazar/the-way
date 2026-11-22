PASS 41921006168c95b1de449ea546fab2271ec815e9

Review of the fix of the findings of the whole-change review (`review-change` with `fix.md`), round
1. Range `ae37fca3310ce6efe7e7939413b8b7a1205b0ead..41921006168c95b1de449ea546fab2271ec815e9`,
five commits, 7 files; `git rev-parse HEAD` in the worktree is
`41921006168c95b1de449ea546fab2271ec815e9`. The findings file `reports/fix-1-findings.md` bounds
the review. No finding is contested.

## Each finding

- **I1 — fixed.** `task-cycle/skill/planning.md:39-42` now tells the orchestrator that "The handoff
  of each later slice also lists the tests the plan leaves failing at its base, with their owners,
  as the *Goal* of each earlier slice names them", and "Where a report names a failing test that no
  *Goal* names, give it an owner by editing the plan before the next slice is dispatched";
  `task-cycle/skill/SKILL.md` step 9 carries the list in sub-step 2 (`:468-470`), sends an unnamed
  failure to `planning.md` in sub-step 3 (`:479-480`) and in sub-step 4 (`:484-485`) says "a listed
  test that fails as the plan says is none (WAY-136)", so no retry follows from it. The three duties
  of the quoted wording now stand in files the orchestrator reads, the duty once (`planning.md`),
  step 9 pointing to it. Evidence: the diff; a search of `task-cycle/skill/` for
  `failing at its base` now finds `SKILL.md:469` and `planning.md:39`.
- **I2 — fixed.** `elements/common/decision_index.py:137-178` reads the list by the names
  `Identifier`, `Why`, `Successors` of its header, skips the separator row, and ends with exit code
  2 and a message naming the file and the column for a missing or renamed column, and naming the
  row and the column for a missing or empty cell; `chain` (`:181-206`) now stops on a successor that
  is neither a decision, a withdrawn identifier nor `none`, where it read it as no successor. Six
  tests, two with a line `decision:` of WAY-344, give the file without a column, under another name,
  without a cell, with an empty cell, with a successor the log lacks, and with the columns in another
  order. Evidence: my probe `reports/review-whole-probe-withdrawn/` on the new head ends with exit 2
  and "Error: foundations/decisions.md: the list of withdrawn identifiers has no column Successors"
  (it ended with exit 0 and "it has no successor" at `ae37fca3`); every one of the 179 withdrawn
  identifiers of the real log run through `--decision` ends with exit 0.
- **I3 — fixed.** `instruction-files/check_instructions.py:113-117` and `:453-454`: a token that
  holds a typographic quotation mark (`“ ” „ ‚ ‘ ’ « »`), or begins or ends with an apostrophe, is no
  path; an apostrophe inside a name leaves it a path; docstring `:19-22`. Evidence: my probe
  `reports/review-whole-probe-quote/repo` on the new head gives `0 error, 0 warn` (it warned on `'\''`
  and `‘docs/a.md’` at `ae37fca3`); the new head's script on the local loop2 checkout, read only:
  `0 error, 15 warn, 118 info` (21 at `ae37fca3`), none of the 15 holding a quotation mark — they are
  the real warnings the task's *Out of scope* leaves to loop2.
- **I4 — fixed.** `reports/author-report.md`, section "Walkthrough", now judges that the change
  alters what five commands print and how they end, states that the foundation settles no way to
  the-way as a running product so the walk is not performed, gives what the change alters in the
  user's words, what was not checked, and a plan of eight cases drawn from the task's points (10, 4,
  5, 5.2, 11.1, 11.2, and the fix of I2) plus the side-observation row, each marked unchecked with
  that reason — as WAY-406's third paragraph and `task-cycle/change/walkthrough.md:26-28` give.
- **M1 — fixed.** `task-cycle/review/whole_change.md:27-33` now tells the reviewer to run the check
  itself on the head, in the reviewed worktree, by the command `installation/README.md` gives, in a
  product `.the-way/installation/README.md` with the script's path starting with `.the-way/`. The
  author did not write the script's own path there because the part map gives `task-cycle` no
  dependency on `instruction-files` (`foundations/part_map.md:111-112`), while it does on
  `installation`; I accept that: the README gives the command whole, and the sentence names what the
  finding asked — the product form and that the reviewer runs it.

## New findings in the fix diff

### Critical

none

### Important

none

### Minor (within the task's scope)

- `instruction-files/check_instructions.py:454`, the comment `# text in quotation marks, such as '''
  of a shell, is no path`: the idiom it means is `'\''` (quote, backslash, two quotes), as the
  docstring (`:20`) and the test write it; `'''` in the comment is three quotes, a form the shell does
  not use. Evidence: the line itself. A reader learning the rule from the comment is misled about the
  idiom; the code is right.

### Out of scope

none

## Declined to judge

- That `--decision` of a living decision now also fails on a malformed list of withdrawn
  identifiers: WAY-344 binds the whole reading of the file, so the stricter reading is the rule's,
  not a defect.

## Checks

From a worktree of the new head `.runs/review-fix-1/head`; "exit" is the exit code.

| Check | Command or method | Result |
|---|---|---|
| sizes of the changed files | `python -B task-cycle/change_file_sizes.py ae37fca3 41921006` (reviewed worktree) | exit 0; 7 files modified, +167 lines; `check_instructions.py` 998 → 1007 |
| tests of the decision index | `python -B -m unittest test_decision_index` in `elements/common/` | exit 0, 31 tests |
| tests of the instruction check | `python -B -m unittest test_check_instructions` in `instruction-files/` | exit 0, 122 tests, 5 skipped |
| linter, formatter and rule of size | `python -B -m unittest test_linter_invariant test_size_invariant` in `agent-instructions/` | exit 0, 9 tests |
| foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` (the new lines `decision:` of WAY-344 are accepted) |
| instruction check on the-way (whole_change.md, WAY-418) | `python -B instruction-files/check_instructions.py .` | exit 0, `0 error, 0 warn, 5 info` |
| instruction check on loop2, read only | `python -B instruction-files/check_instructions.py <loop2 checkout>` | `0 error, 15 warn, 118 info`; no warning holds a quotation mark |
| every withdrawn identifier of the real log | `python -B elements/common/decision_index.py --decision <ID> --output .runs/review-fix-1/p.md .` for each of the 179 rows | 179 runs, 0 non-zero exits |
| probe of I2 | the command in `reports/review-whole-probe-withdrawn/command.txt`, on the new head | exit 2, the error naming the column `Successors` |
| probe of I3 | the command in `reports/review-whole-probe-quote/command.txt`, on the new head | exit 0, `0 error, 0 warn` |
| test directories the fix reaches | `python -B gate/run_tests.py task-cycle`, `… agent-instructions`, `… product-guidelines` | task-cycle exit 0, 570 tests; agent-instructions exit 0, 53 tests; product-guidelines exit 0, 14 tests |
| crafted input at `check_instructions.py` | reading of the changed `looks_like_path` | the fix only adds text rules that take tokens out of the lookup; no new read of a file and no new lookup; the guards of links and network paths stand before and after it unchanged |
| code made for a test (WAY-409) | reading of the fix diff for a branch or value made for a test's input | none: the column names come from the log's own header, the quotation marks are a class of characters, not the tests' tokens |

## Reaches beyond what the handoff names

- `foundations/part_map.md:105-116` (task-cycle's *Depends on*): to judge the author's reason in M1.

## Working copies

My directory was `.runs/review-fix-1`,
holding a git worktree `head` at `41921006` and the outputs of my runs. Removed: the worktree with `git worktree remove --force` by its full path,
then `git worktree prune` (each exit 0), then the directory by its full path (exit 0; it no longer
exists, and `git worktree list` names no copy of this review). No remainder.
No probe of this review needed new files in `reports/`: I reran the two probes of the whole-change
review, whose input and command stand in `reports/review-whole-probe-withdrawn/` and
`reports/review-whole-probe-quote/`.

## Unread material

none — the handoff, `task-cycle/review/fix.md`, the findings file, the author's fix report, the
section "Walkthrough" and the corrected line of "Unread material" of the author's report, and the
whole fix diff were read whole; the frozen task was read whole in the review of the whole change and
not again.

## Searches not found or unclear

none
