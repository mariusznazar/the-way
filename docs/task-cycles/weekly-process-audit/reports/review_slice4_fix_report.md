FAIL 939223030ad1a94df3b46c9acd8480bdf28bacd9

# Review of the fix of slice 4 (`269d7be..9392230`)

`git rev-parse HEAD` = `939223030ad1a94df3b46c9acd8480bdf28bacd9`, confirmed. Worktree read only (`git status --short` empty after the checks).
Read: `task-cycle/review/fix.md`, the findings file `review_slice4_findings.md`, the fix report `slice4_fix_report.md`, the whole diff of the range.
Counts: 1 blocking (finding 1 remains), 2 Minor, 0 out of scope.

## Each finding of the findings file

### Finding 1 (share of fix rounds silently wrong) — REMAINS (Important, blocking)

What the fix removed. The two silent-wrong cases I showed are gone: the resumed author/reviewer in a task named "fix" and the orchestrator's
parallel rows naming fix subagents now give `unknown` (the new tests cover both; the second also by `is_orchestrator_row`). *Review rounds* is read now
and must agree with *Events*. The share is only ever `0.0%` or `unknown`, so no count coincidence can give a wrong non-zero figure.

What remains. The `0.0%` is given when the record names no fix round, and "names" is the path rule: a file name holding the words `report` and
`fix`. Real records name their fix reports otherwise. In the archive (`git show` of `plan-project-skill-shape`, `pr-description-schema`):
Events rows `reports/fix.md` and `reports/review-fix.md` / `reports/whole-review-2.md`, and the line *Review rounds* says "one whole-change round, one fix and its review"
or names `fix` ``reports/fix.md`` — no path holds the word `report`. Both places then name nothing and agree, the share is `0.0%`, and the cycle did have a fix round.

Run (scratch `scratch4.py`, temporary repository through the tests' helpers): record with Events rows `reports/fix.md` and `reports/review-fix.md`,
*Review rounds*: "one whole-change round, one fix and its review. Closed at 4327974."; stages: an author and a reviewer with a second turn each,
named without `fix`, the second turns costing about a third of the cycle. Result: `Cost` 1.113000, `Fix rounds` `0`, `Share` `0.0%`, no unknown row.
Of the 65 archived records I could read with the new functions: 25 give `unknown` (earlier form or the two places disagree), 13 name round(s)
by the path rule and agree (share `unknown`), and 24 name no round by the path rule although they talk of fix rounds or have Events rows with `fix`
(these would give `0.0%` once their `stages.md` has the per-model section). So the silent-wrong `0.0%` is not a corner but the form of the older
records. The report's concern ("a `0.0%` relies on the record") understates it: the record does name the fix, only not in the words the rule reads.

Direction (the author's choice): give `0.0%` only where the record positively says there was no round (the item *Review rounds* reads `none`, as
`remarks_check.reads_none` reads the remarks item) and *Events* holds no row with the word `fix` or a fix/review report path; otherwise `unknown`. Or give the
share only as `unknown` until the stages carry the link (below). A test with `reports/fix.md` and prose in *Review rounds* must give `unknown`.

### Finding 2 (cost `0.000000` where no tokens) — FIXED

`priced` gives `unknown` with the reason for any `—` row; scenario A of my review (one row `—`, zero tokens) now gives `unknown` (and the test
`test_a_stage_with_no_token_usage_leaves_the_cost_unknown` fails on `269d7be`, per the report, which I believe from the diff). The reason names the stage and passes through
`cell()` at render, so a bar, control characters or escapes in the name are neutralised as before.

## New findings in the fix diff

### Minor — a tokenless orchestrator stretch now makes the cost of the whole cycle `unknown`

Place: `process-audit/audit_count.py` `priced`, the `NO_MODEL` branch. Every `—` row is refused, not only a section without tokens. In the archived `stages.md` (old form,
Total tokens column) 30 of 1,762 rows have zero tokens, all rows named `orchestrator`, in 8 of 83 files (about 10 % of cycles). If the new form writes `—` for them,
those cycles lose their cost although the missing row is an orchestrator stretch with time and no usage, not a stage with an unread transcript. The direction is safe (`unknown`, never a false figure)
and the report names the choice and its cost, so Minor. A cheaper rule keeps `unknown` for a section with no priced row at all and for subagent rows with `—`, and prices an `orchestrator` stretch with `—` as zero.

### Minor — a second line `- Review rounds:` is read as more rounds, not as a doubled line

Place: `review_rounds`. Lines starting `- Review rounds:` anywhere outside fences are unioned, while `Process pin` and the remarks item treat a doubled line as `unknown`. A doubled line can only make the two places disagree or leave them equal, so
the direction is safe; noted for consistency.

Not judged (not in the findings file, per `fix.md`): my earlier Minor findings 3-6 and the out-of-scope finding; the fix report says it neither read nor fixed them. They stay Minor and block nothing.

## Hostile input in what the fix changed

`report_paths` (a `split()` and a bounded regex over the file-name words), `review_rounds` (one pass over the lines), `is_orchestrator_row` (a prefix test) are linear; no new number conversion,
no new regular expression with nested repetition, no new subprocess or import, no new read (the record is already read under the 4 MiB cap). New reason strings carry counts and a stage name
that goes through `cell()`. A crafted record can make the share `0.0%` or `unknown` as the record says — that is the record being the source, graded in finding 1. A record that
writes `none` beside a real fix cannot be told from honest by the command.

## Whether the outcome (share `unknown` whenever the record names a round) is a defect of the fix or a limit for the human

Both, separated:

- The `unknown` for a cycle that names a round is **a limit the orchestrator must put to the human**, not a defect. I looked for a stronger tie than a word count and agree with the executor: `stages.md`
  names the subagent that worked (`… — turn 2`), not the round the turn served; the archived *Events* rows give the orchestrator's labels, not the subagent's stage name; times are in different forms. With the
  current records and `stages.md` no honest non-zero share can be computed. The only complete remedy is to make the stage report carry the link (the executor's suggestion: `cycle_stages.py` writes, per subagent turn, the report path the prompt
  names). That changes the form of the stage report and so starts a new series (WAY-336), and reads the prompt as untrusted text. WAY-334 and the task name the share of fix rounds as one of the two cost numbers; until that change the number
  is empty exactly in the cycles that matter. Cost of leaving it: the share stays `unknown` in every cycle with a fix. Cost of the change: a task of its own, new series, a new trust boundary in `cycle_stages.py`.
- The `0.0%` given where the record "names no round" is **a defect of the fix** (finding 1): it is a figure, and it is wrong for the records as they are written.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 269d7be..9392230`; `git diff 269d7be..9392230` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree) | 0 — 61 tests OK, 46 s |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| scratch `scratch3.py`, `scratch4.py`, `arch.py` in `a scratch file outside the repository` (outside the worktree; temporary repositories; archived records read through `git show`) | the `0.0%` result above; archive counts 65 / 25 / 13 / 24; zero-token rows 30 of 1,762 in 8 of 83 files |
| `git status --short` after the checks | empty |

Not run: the full suite; `foundation_check` (no foundation file in the range); a run on the real repository (the executor's: all 69 cycles `unknown`, which cannot show finding 1 since no archived `stages.md` has the per-model section).
Unverified: that the archived records that talk of a fix round would, once their `stages.md` carry the section, give `0.0%` — shown on a constructed record in the archive's form, not on an archived cycle.

## Reaches beyond the dispatch

- Archived `cycle.md` of `plan-project-skill-shape` and `pr-description-schema` (and a pass over all archived `cycle.md` and `stages.md` by `git show`) — to see how real records name fix reports (finding 1) and how many stage rows have zero tokens (new Minor).
- `task-cycle/cycle_stages.py` (read in the first review) for the `—` row and the orchestrator rows.

## Unread material

- Whole `review_slice4_report.md` was mine (written); the fix report read whole; `audit_count.py` read in the diff and the functions it touches, not again from line 1; the foundation entries were read in the first review and not reread.

## Searches not found or unclear

- Any record or `stages.md` that links a subagent stage to a fix round: none found (agrees with the fix report).
- Whether the new stage report writes `—` for an orchestrator stretch with time and no usage: the old form's zero-token rows suggest so; not verifiable without a cycle on the new form.
