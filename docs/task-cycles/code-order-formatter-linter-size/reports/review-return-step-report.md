PASS d41712a6d24656410a5e303ec3e45e54ae0bde7f

# Review of the return step's commits - code-order-formatter-linter-size

Range `2e066ab4..d41712a6`, one commit: `d41712a6` "Wrap the last sentence of the formatter rule in the
coding guidelines at the width of the rest". `git rev-parse HEAD` gives `d41712a6d24656410a5e303ec3e45e54ae0bde7f`,
the head given. Changed file: `guidelines/coding.md`, 2 insertions, 2 deletions.

## Findings

### Critical

none

### Important

none

### Minor

1. `foundations/decisions.md:10796` (WAY-385, *Relations*). The binding sentence (line 10786-10788) counts the
   thresholds "on the code as the formatter of WAY-382 leaves it", while *Relations* names WAY-379, WAY-360 and
   WAY-361 only. The content agrees with the code (`agent-instructions/test_size_invariant.py` counts the formatted
   files, and the formatter invariant holds them formatted), so this is a departure of form, Minor (WAY-364); no
   sentence is read wrongly through it, since WAY-382's own *Rationale* (line 10720-10721) says that the thresholds
   of WAY-385 count the code after the formatter. Written by the change's foundation step, not by `d41712a6`; the
   return step's report names it as its concern 3. Within the task (point 4 changes WAY-385); not blocking.

## Declined to judge

- The four test names of `process-audit/test_audit_count.py` with `entry` in the sense of a sub-item (return step
  report, concern 1): a rename of tests is a change of code, outside the return step's commits, and whether they are
  among the uses point 8 of the task leaves is a choice for the orchestrator; the whole change passed its review.
- The ban on `yapf: disable` / `yapf: enable` beside the `fmt:` comments (concern 2): written by the change before
  this commit and reviewed whole (`PASS 2e066ab4`); WAY-382, `formatter-layout`, `guidelines/coding.md` and the test
  agree with each other, so it is no departure of an entry from the code, which is what this review judges.
- The phrase "Standard library only" in the docstrings of `process-audit/version_analysis.py` and
  `process-audit/audit_report.py`, which import sibling modules of the-way: a docstring of code outside this
  commit, read as "nothing outside the-way and the standard library"; not a foundation entry or guideline.

## What the review checked

- **No word of `### Formatter` changed.** `git diff 2e066ab4..d41712a6` moves "the one command of the gate" from the
  end of line 54 to the start of line 55 and nothing else; `git diff --word-diff` shows no added or removed word;
  `guidelines/coding.md` at both commits, with runs of spaces and line ends collapsed, gives the same MD5
  (`ad188c21ebcaa40c3c3c78ea3aefaa5a`). Lines 50-55 now all stand within 100 characters, like the rest of the
  paragraph. No test reads the real `guidelines/coding.md` text of this paragraph (the test files that name
  `guidelines/coding.md` use fixtures); `foundation_check.py`, which reads it, exits 0.
- **Old phrases** ("80 lines", "1000 lines", "known violation", "expected failure", `expectedFailure`,
  "none - WAY-382", "none — WAY-382", "settings of the linter", "no formatter", "no automatic formatter", "80/1000"),
  over the worktree outside `.runs/`: the hits are the general text of WAY-51 (`decisions.md:1841-1856`) and of
  `decisions.md:9619`, the templates (`elements/invariants/template.md:166`, `elements/part-map/template.md:115,119`),
  `foundation-review/weak_points.md:82`, `task-cycle/review/whole_change.md:48`, `README.md:82` (all about the
  mechanism of a violated invariant), fixtures of tests (`gate/test_run_tests.py:213`,
  `elements/common/migrate_foundation.py:937`), and the measurements before the formatter in the *Rationale* and
  *Rejected* of WAY-382 (`decisions.md:10712,10722`) and WAY-385 (`decisions.md:10824-10828`). `README.md:106`
  ("the settings of the linter") now reads "the settings of the linter and the formatter", which matches
  `ruff.toml`. No `expectedFailure` stands in `agent-instructions/test_linter_invariant.py` or
  `agent-instructions/test_size_invariant.py`. The return step's claim holds, with `README.md:106` an extra hit it
  did not list but which is correct.
- **WAY-382, WAY-385 against the code.** WAY-382 (line 10691-10699): Ruff of WAY-381, `ruff.toml`, width 100
  (`ruff.toml:6` `line-length = 100`), `.py` only (`ruff.toml` `[format] exclude = ["*.md"]`), the five forbidden
  comments (test class `Formatter` in `agent-instructions/test_linter_invariant.py`). WAY-385: 110/1200 on the
  formatted code (`test_size_invariant.py:5`, its `decision:` line 71 quotes the new opening). Both match.
- **Invariants** `formatter-layout`, `function-and-file-size`, `ruff-blocking-rules`, `own-foundation-check-report`,
  `audit-series-script-paths`, `cycle-stages-refuses-crafted-names`, `shared-module-import-runs-nothing`,
  `gate-times-refuses-impossible-entry` read whole: each reads `Violated: no` where it should; the parts of the Scope
  of WAY-379 match the ten directories of `PARTS` in both invariant tests (each also fails on a tracked `.py` file
  outside them); `audit-series-script-paths` names `version_analysis.py` and `stage_transcripts.py`, which
  `version_analysis.py:56-57,82-84` holds as `COST_SCRIPT`, `COST_MODULE` and the three other paths;
  `cycle-stages-refuses-crafted-names` points at the description of `cycle_stages.py`, which still holds the form of
  *Files named* (`task-cycle/cycle_stages.py:69`); `shared-module-import-runs-nothing` names only
  `relation-model/fingerprint.py`, unchanged.
- **Part map.** *Files*: `task-cycle/**` and `process-audit/**` cover the six new modules; `/.git-blame-ignore-revs`
  stands under `repository` and holds `015ce05c2a7209af7db05873775f561acdae408f`, an ancestor of the head whose
  78 changed files are all `.py`. *Depends on*: the imports of `audit_shared.py`, `record_reading.py`,
  `problem_register.py`, `version_analysis.py`, `audit_report.py` are the standard library, each other,
  `stage_pricing` and `record_items` of `process-audit`, and `remarks_check` of `task-cycle`, which `process-audit`
  may depend on (`part_map.md:135`); `task-cycle/stage_transcripts.py` imports the standard library only.
  *Trust boundary*: `stage_transcripts.py`, `problem_register.py`, `record_reading.py`, `audit_shared.py` are listed;
  `version_analysis.py` is not, though it hands a commit name from a record to `git rev-parse` — it checks it with
  `SHORT_HASH.fullmatch` first (`version_analysis.py:139`) and takes it from `record_reading.py`, which is listed and
  reads the files from outside; I judge the entry consistent with the template's definition ("files that take in
  what the product does not control", `elements/part-map/template.md:124-127`) and with the plan's choice the return
  step cites.
- **Guidelines.** `guidelines/coding.md` read whole: `### Formatter` and `### Size of a function and a file` agree
  with WAY-382, WAY-385 and the invariants. `guidelines/coding-shared-module.md` and
  `guidelines/coding-measuring-report.md` list none of the new modules; the coding template says a file added after
  the audit that wrote the table takes no row until the guidelines are refreshed
  (`product-guidelines/coding/template.md:268-269`), so the tables do not contradict the code.
- Reviewed the return step's environment-fact reasoning: no sentence of WAY-382 or `formatter-layout` depends on how
  Ruff treats the comments, since the test finds them by `tokenize`; agreed.

## Checks

| Command | Exit |
|---|---|
| `git diff 2e066ab4..d41712a6`, `git diff --word-diff 2e066ab4..d41712a6` | 0 (no word changed) |
| `git show <commit>:guidelines/coding.md \| tr -s ' \n' ' ' \| md5sum` at both commits | 0 (same sum) |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B gate/run_tests.py elements/part-map` | 0 (OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (OK) |
| `git merge-base --is-ancestor 015ce05c d41712a6`; `git show --name-only 015ce05c` | 0; only `.py` files |

The full gate was not run (the handoff forbids it).

## Reaches beyond the dispatch

- `elements/part-map/template.md` (passages on *Trust boundary*, lines 46-47 and 122-130): to judge the trust-boundary
  lines of the part map against the new modules.
- `product-guidelines/coding/template.md` lines 89-113 and 256-269: to judge whether the tables of files of a kind
  must list the new modules.
- `guidelines/coding-shared-module.md` and `guidelines/coding-measuring-report.md`, read whole: guidelines of the
  kinds the new modules belong to.
- `README.md` lines 60-129 and the change's diff of `README.md` and `ruff.toml` from `d69fb20b`: the hit of
  "settings of the linter".

## Working copies

`.runs/review-return-step/` of the worktree held the output of the two focused test runs (`partmap.txt`, `ai.txt`).
No worktree, clone or screenshot was made. The directory was removed before return; nothing remains.

## Unread material

- `foundations/decisions.md`: WAY-382 and WAY-385 read whole; WAY-51 and the other decisions only at the lines the
  searches found.
- The six new modules: read at their docstrings, imports and the lines named above, not whole.
- `.runs/task-cycles/code-order-formatter-linter-size/reports/return-step-handoff.md`,
  `task-cycle/skill/return_step.md` and `reports/review-whole-fix-report.md`: not read; the claims were checked
  against the files themselves.

## Searches not found or unclear

- "none - WAY-382", "none — WAY-382", "no automatic formatter", "80/1000", "known violation": not found outside
  `.runs/` beyond the hits named above.
