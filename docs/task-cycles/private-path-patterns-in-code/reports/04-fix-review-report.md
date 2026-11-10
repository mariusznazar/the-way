PASS 578a8bd7bb5026e374386ff750287da24849dad5

# Review 04 — the fix of the Minor findings of review 02

Range `287a027..578a8bd` (one commit, `578a8bd`; files `foundations/decisions.md`,
`installation/README.md`, +13/-5). `git rev-parse HEAD` = `578a8bd7bb5026e374386ff750287da24849dad5`,
the head given. Bounded by `03-fix-findings.md` (three Minor findings, none contested).

## Findings of the findings file

1. **WAY-320 rationale count — fixed.** `foundations/decisions.md:10318` now reads "listed 71 such
   texts in code among 88 findings", which matches `task.md:27` (70 arrays in arrays + 1 shell class)
   and no longer credits the Markdown-only rule with the two specification slots. Nothing else in the
   entry changed (diff is one line).
2. **README exit codes and backticked texts — fixed.** `installation/README.md:117-120` now names
   every exit-2 case of `task-cycle/tracked_private_paths_check.py` (identifier not given once, no git
   repository, invariants file or invariant missing, untracked named file, file not UTF-8) and says
   a file with a NUL byte near its start is counted as binary. `:86-87` now says every backticked
   text of the sentence is read as a file path. Checked against the command's raises
   (`tracked_private_paths_check.py:47-52, 70-88, 92-98, 117-118`) and `private_paths_check.py:130-142`.
   The empty-sentence case and `git` not startable are covered by "when it cannot check".
3. **README *Derives from* — fixed.** `installation/README.md:88-92` says *Derives from* names a
   decision of the product's own log, or the source of the rule as the invariant template's "Links"
   gives, and that a decision of the-way is no decision entry of the product. This agrees with
   `elements/invariants/template.md:122-142`.

## New findings in the fix diff

### Critical / Important

none

### Minor (non-blocking)

1. `installation/README.md:119` — "or a tracked file is not UTF-8 text" is slightly broader than the
   code: a file starting with a UTF-16 byte-order mark is not UTF-8 but is decoded and read
   (`task-cycle/private_paths_check.py:134-139`), not exit 2. The error lies in the harmless
   direction (the README promises an error the command does not give); fix if wanted: "is neither
   UTF-8 nor UTF-16 with a byte-order mark".

## Declined to judge

- Two added lines exceed the usual wrap of about 100 characters (`foundations/decisions.md:10318`,
  105; `installation/README.md:121`, 109). The files already hold such lines (533 and 14 lines over
  100), and no check reads line length; not a finding.

## Checks run

| Check | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `578a8bd7bb5026e374386ff750287da24849dad5` |
| `python -B gate/run_tests.py installation` | 0, 44 tests OK |
| `python -B elements/common/foundation_check.py` | 0, "0 errors" |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0, "checked: 275 files, 0 listed" |
| Manual: fix diff read whole; README text compared case by case with the command's error raises; line lengths of added lines measured (`awk`) | as above |

Not run: the whole gate (the orchestrator runs it). `git status --short` was empty; no tracked file
changed. Scratch output: `.runs/review04_inst.txt` (ignored).

## Reaches beyond the dispatch

- `elements/invariants/template.md:120-142`, read in review 02 and used again for finding 3.
- `task-cycle/private_paths_check.py:126-145`, to check the README's UTF-8 and binary wording.

## Searches not found or unclear

none
