PASS 4066ae5d8f585a5af1568cc444751f1a7038d23b

# Review of the return step's commits — task `small-fixes-after-prs-117-121`

Range `eaf815c..4066ae5`, one commit `4066ae5`; `git rev-parse HEAD` = `4066ae5d8f585a5af1568cc444751f1a7038d23b`,
confirmed. Files: `agent-instructions/README.md`, `elements/invariants/template.md`, `foundations/decisions.md`
(WAY-344), `foundations/part_map.md` (part `elements-common`). Judged against `task-cycle/skill/return_step.md`,
the task's items 8 and 9, its *Context* line on the README, rows 1–9 of *Settlements to record* (row 3 above all),
WAY-344, WAY-114 and WAY-134 read whole, and `elements/common/foundation_check.py` with its tests at `4066ae5`.

## What holds

- **WAY-344, corrected sentence** (`foundations/decisions.md:2858-2861`): "a field it needs for a comparison and
  finds missing from that copy is listed by a line `listed:` that names the entry and the field, with no error and
  no change of the exit code". True of `list_invariants` (`elements/common/foundation_check.py:723-747`): the base
  copy's *Method* and *Part* are read only for an invariant that is in the base, has both fields now, reads `test`
  now and whose sentence is reworded — exactly the case where the comparison is attempted; the line names the
  invariant and the field (`:742-745`); it is a `note`, not an error. The narrowing fixes the breadth of the
  earlier "a field missing from that copy". The test lines `decision:` (`test_foundation_check.py:1586`, `:1607`)
  still quote the sentence's unchanged start, and the check gives `0 errors`. Within the-way, no other script
  that checks form reads a copy at the base (`git grep` for `fork_point|merge-base|at_commit` in `*.py`:
  `foundation_check.py`, `foundation_source.py`, `installation/install.py`, `process-audit/audit_count.py`; the
  last two are no check of form), so the sentence binds no other code today.
- **Removal of the two pair clauses and the mark `row 3`.** The removed clauses (complies "the same script,
  reading a copy … on a line `listed:` and keeps its exit code"; violates "… ends with an error at a field missing
  from the copy … or passes over it without a word") state what the tests at `test_foundation_check.py:1585-1614`
  hold: listed with exit code 0 and `0 errors`, one line naming the field. The *Verification* clause `tests:`
  already names that test (`foundations/decisions.md:2894-2897`). This is the return step's own rule
  (`return_step.md:16-18`: remove the part a test holds, name the test in `tests:`, keep a pair only for a part no
  test holds). After the removal WAY-344's pair is word for word the pair at `b6b3416` (checked by
  `git diff b6b3416..4066ae5 -- foundations/decisions.md`). What the cycle wrote beyond row 3 is the *Rationale*
  sentence and the *Rejected* clause; *Rejected* gives the two ways not chosen that the question of row 3 keeps
  (`task.md:80-82`), as WAY-134 requires, and neither a rationale nor a link makes an entry `the cycle's` by
  `task-cycle/skill/foundation_step.md:30-33`. So the mark goes back to `row 3` rightly, and I2 of the whole
  review no longer applies to WAY-344.
- **Minor n1 of the fix review — fixed.** Both descriptions now say the base-copy listing is made whether or not a
  file citing the invariant changes, as the code does (`foundation_check.py:740-745` lists before the citing-file
  test at `:767-769`) and as the test at `test_foundation_check.py:1606-1614` holds.
- **Part map** (`foundations/part_map.md:67-73`): "with the module that reads the files and git for it" is true of
  `elements/common/foundation_source.py` (its docstring: "The ways `foundation_check.py` reads a repository … It
  reads files and asks git, and writes nothing"); its only importer is `foundation_check.py:130`; it imports only
  `os`, `subprocess`, `sys`, so *Depends on* needs nothing new; `elements/common/**` already holds the file;
  *Trust boundary* `none` stands as for the script that already ran git. The responsibility sentence keeps every
  item it had.

## Findings

### Critical / Important

none

### Minor, within the task

**r1 — The README's sentence on the base-copy listing drops "that reads `test`".**
`agent-instructions/README.md:17-18`: "an invariant whose sentence a change rewords and whose copy at that commit
lacks *Method* or *Part* it lists too, naming the field, whether or not a file citing it changes." The code lists
only an invariant whose *Method* reads `test` now (`elements/common/foundation_check.py:737-739`: `continue` when
`found["Method"][0] != "test"`, before `lacking` is computed); an invariant reading `review` whose base copy lacks
*Method* and whose sentence is reworded gives no line. The template row the same commit writes keeps the
qualifier ("one that reads `test`"), so the two descriptions now differ. A reader of the README would expect a
line for a `review` invariant and take its absence for a fault. The same omission stands, unchanged by this range,
in WAY-344's *Verification* clause `tests:` (`foundations/decisions.md:2894-2895`, "lists an invariant whose
sentence the change reworded and whose copy … lacks"); that clause describes what the tests hold, and they hold
a `test` invariant, so it misleads less. Suggested: "an invariant that reads `test` whose sentence a change
rewords and whose copy at that commit lacks *Method* or *Part* it lists too, …". Blocks nothing: the binding
sentence of WAY-344 ("a field it needs for a comparison") is right, and no comparison is made for `review`.

**r2 — The template row reads as if the listed line says whether a citing file changed.**
`elements/invariants/template.md:176`: "and, naming the field and whether or not a file citing it changed, one
that reads `test` whose reworded sentence's copy at the base lacks *Method* or *Part* (WAY-344)". "naming the
field and whether or not a file citing it changed" parses as two things the line names; the line names the
invariant and the field only (`foundation_check.py:742-745`). "whose reworded sentence's copy at the base lacks
*Method*" also gives the fields to the sentence's copy, not the invariant's. Suggested: "and, whether or not a
file citing it changed, one that reads `test` whose sentence a change reworded and whose copy at the base lacks
*Method* or *Part*, naming the field (WAY-344)". Form only; the content agrees with the code.

**r3 — No meaning sentence of WAY-344 matches the corrected entry; the one the request would carry is broader.**
The return step's report (`reports/return-step-report.md:15-22`) gives marks and notes but no meaning sentences,
so for WAY-344 the orchestrator has only the sentence of `reports/author-fix-report.md:41` (and
`author-report.md:48`): "A field missing from the copy of a file at the commit the branch left is listed by a
`listed:` line naming the entry and the field, with no error and no change of the exit code." That is the
breadth the return step just corrected out of the entry: it drops "a script whose purpose is to check the form
of a file" and "a field it needs for a comparison". WAY-114 puts every entry in the request's lower part by its
identifier with one English sentence of its meaning, so the request would state WAY-344 more broadly than the
foundation does. Suggested sentences for the orchestrator to carry:
English — "Where a script that checks the form of a file reads that file's copy at the commit the branch left,
a field it needs for a comparison and finds missing there is listed by a `listed:` line naming the entry and the
field, with no error and no change of the exit code."
Polish — "Gdy skrypt sprawdzający formę pliku czyta kopię tego pliku z commita bazowego, brak pola potrzebnego
mu do porównania wypisuje linią `listed:` z nazwą wpisu i pola, bez błędu i bez zmiany kodu wyjścia."
Minor: the foundation is right; the fix is in the request's text, which the orchestrator writes.

### Outside the task's scope

none

## Declined to judge

- The subject of WAY-344's new sentence, "a script whose purpose is to check the form of a file", is wider than
  row 3's "the check of the foundation"; it was written by the foundation step, unchanged by this range, and read
  against the row by the review of the whole change, which owns that comparison (WAY-114's rationale). Today it
  binds only `foundation_check.py` (see above).
- `foundations/decisions.md:2861` now runs to 117 characters, made long by this range's rewrap; no formatter rule
  (WAY-382), no effect on a reader — as the fix review declined the same for two other lines.
- The other entries the cycle wrote (WAY-139, WAY-60, WAY-61, WAY-229, WAY-160's rationale), which the return
  step compared and left unchanged; this range does not touch them and the earlier reviews judged them.

## Checks run

In a worktree of `4066ae5` at `.runs/review-return/head`:

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B -m unittest discover -s elements/common -p test_foundation_check.py -k reworded` | 0 | 9 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 tests OK (expected failures=2) |
| `git diff b6b3416..4066ae5 -- foundations/decisions.md` (manual) | 0 | WAY-344's pair equals the base's; only sentence, `tests:`, rationale and *Rejected* differ |
| `git grep -n` for `fork_point\|merge-base\|at_commit` in `*.py` (manual) | 0 | only `foundation_check.py` among checks of form reads a base copy |
| `awk` line lengths over 100 in the changed passages (manual) | 0 | `decisions.md:2861` 117, new in range |

Not run: the full gate (the orchestrator's). No mutation run: the range changes no code or test.

## Reaches beyond the dispatch

- `task-cycle/skill/foundation_step.md:17-47` — the rule that makes an entry `the cycle's`, to judge the mark.
- `foundations/decisions.md`, WAY-03 whole (by search for its heading) — to check that the listing's other
  description is not contradicted by the base-copy listing; it says "lists … when", not "only when".
- `reports/author-report.md:48` and `reports/author-fix-report.md:34-44` — the meaning sentences the return step
  carries for WAY-344.
- `elements/common/foundation_source.py:1-40` and `elements/common/compare_log_entries.py:1-40` — the module the
  part map names, and whether another script of form reads a base copy.

## Working copies

`.runs/review-return/head` (detached worktree of
`4066ae5`): removed with `git worktree remove --force`, then `git worktree prune`; `.runs/review-return/` stands
empty. Remainder: none.

## Unread material

none — the handoff, the method, `return_step.md`, the return step's report and the fix review's report whole; the
task's passages the handoff names; WAY-344, WAY-114, WAY-134 whole; the whole review's report at lines 40-80 and
its WAY-344 mentions (it was read for what was judged, not as material of this range).

## Searches not found or unclear

none
