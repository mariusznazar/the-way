# Affected code review — coding guidelines, range `5a00041..a839ea7` (task cycle step 11)

Reviewer: a fresh agent (claude-opus-5-5) that wrote none of the range, no check and no invariant
sentence of this task. Method: Superpowers 6.4.1 `skills/requesting-code-review/code-reviewer.md`,
read whole from the scratchpad clone the handoff names, its "Declined to judge" list included.
Read-only on `/home/user/the-way` apart from this report and `reports/affected-break-*.txt`; every
run was made in a scratch worktree at `a839ea7` under the scratchpad, removed afterwards. Reviewed in
one pass: the range is 7 files, +98 −27.

## What was implemented

Six commits: the return step `355a240` (`guidelines-check-kind-index/1` edited in place, "git
lists" → "git tracks"; part `task-cycle` *Depends on* gains `product-guidelines`); C39 `f34e477`
(the coding skill's audit covers every kind, the deferral of a kind dropped); C40 `28b42a2` (control
test: an untracked kind file is no error; rename "git lists" → "git tracks"); the assessment's
settlement — `a677bc4` (I1: WAY-203 reworded, WAY-204's relation renewed), `8242720` (I2: the
styleguide template and skill point to "Test cases of a rule"), `a839ea7` (I3: two invariant tests).

## Requirements read

`task-frozen.md` rows 3, 7, 11, 22; `cycle.md` C19, C32, C38–C40; `reports/assessment.md` whole
(I1–I3, M1–M6); `reports/assessment-settlement.md`; the package `reports/affected-review-package.diff`
(identical to `git diff 5a00041..a839ea7`, with log, stat and wider context). Code read against
them: `product-guidelines/form_check.py` (`fenced_blocks`, `check_cases`, `check_rule_cases`,
`kind_of`, `row_path`, `check_kind_index`, `list_guidelines`, `tracked_paths`, `run`), the fixtures
and helpers of `product-guidelines/test_form_check_invariants.py` (`check`, `assert_reported_anew`,
`baseline_errors`, `assert_clean`, `FOUNDATION`, `CODING`, `CODING_ENDPOINT`, `STYLEGUIDE`),
`product-guidelines/template.md` "Test cases of a rule", `product-guidelines/styleguide/template.md`
(required rules), `product-guidelines/coding/template.md` (`### Linter`, "The tools of the standing
checks"), `product-guidelines/coding/SKILL.md` steps 3–4 and *To do*, WAY-190, WAY-201, WAY-204,
`task-cycle/skill/SKILL.md` steps 10–11.

## Evidence

- `python3 -B gate/run_tests.py product-guidelines` at `a839ea7`: `Ran 140 tests … OK`.
- Critical flows and the foundation parts the range touches, at `a839ea7`: `gate` 18 OK,
  `agent-instructions` 169 OK, `elements/decisions` 233 OK, `elements/invariants` 162 OK,
  `elements/part-map` 98 OK.
- Format guards as `agent-instructions/README.md` prescribes before `main`: decisions
  (`--base none --merge-onto none`) 0 errors, 27 warnings (check-by dates and the `<request link>`
  placeholder), 5 unchecked; invariants 0 errors, 3 unchecked; part map (`--base none`) 0 errors,
  7 unchecked. With `--merge-onto none` the guard does not check relation fingerprints, so
  WAY-203's was recomputed with `relation-model/fingerprint.py` from its binding sentences at
  `a839ea7`: `45e40683`, the value WAY-204 now carries; no file outside `.runs/` still holds
  `WAY-203@96f71a98`, and none carries a fingerprint of `guidelines-check-kind-index`.

## Deliberate breaks (WAY-69, WAY-08)

Each in its own scratch worktree at `a839ea7`, `form_check.py` edited, then
`python3 -B gate/run_tests.py product-guidelines` and the same with `--record`. Outputs, each with
its diff: `reports/affected-break-1.txt`, `-2.txt`, `-2b.txt`, `-3.txt`.

| # | Break | Result |
|---|---|---|
| 1 | `guidelines-check-kind-index/1` as edited ("git tracks"): `check_kind_index` counts every file of guidelines read — untracked ones included — as a file of a kind, and an untracked `guidelines/coding.md` as present | **detected** — 6 subtests fail, all in tests citing `guidelines-check-kind-index/1`: `test_a_kind_file_git_does_not_track_is_no_error` (4: both cases × both option sets), `test_a_kind_file_with_no_general_file_is_reported` [the general file untracked], `test_a_row_naming_no_file_git_tracks_is_reported` (untracked=True); the record gives that invariant `fail` |
| 2 | `guidelines-check-example-files/1`, "a block left open to the end of the file": `check_rule_cases` no longer reports an open block, so the end of the file closes it | **detected** — `test_a_case_left_open_to_the_end_of_the_file_is_reported` fails in both subtests (file of a kind, styleguide), citing `guidelines-check-example-files/1`, record `fail`; the ordinary `test_form_check.TestCases.test_a_case_left_open_…` fails too |
| 2b | the same clause, broken where blocks are read: `fenced_blocks` gives an open block the file's last line as its closing line | **detected** — the same three failures |
| 3 | `guidelines-check-kind-index/1`, a row whose *File* names a tracked file not of the form `guidelines/coding-<kind>.md`: the report dropped, the row still skipped (`continue` kept, so no other report takes its place) | **detected** — `test_a_row_naming_a_tracked_file_of_no_kind_is_reported` fails in all four subtests (`guidelines/testing.md`, `guidelines/styleguide-web.md`, `guidelines/coding.md`, `src/api/orders/route.ts`, the last tracked through `FOUNDATION`), citing `guidelines-check-kind-index/1`, record `fail`; three ordinary tests fail too |

On break 3: deleting the whole `if kind is None:` block instead would let the *Kind* comparison
(against `None`) and the "names no file git tracks" report fire at the row, so the check would still
report it and the invariant would still hold; the break that removes the report is the one above.
No break went undetected.

## Strengths

- The two I3 tests isolate exactly the clause each covers: the open-block test asserts its own
  preconditions (`last.endswith("\n```\n\n")`, no fence after it) and the error at the case's
  opening line with the fragment "end of the file", so the swallowed sections' other errors cannot
  satisfy it (`test_form_check_invariants.py:1417-1438`); the tracked-file test covers four shapes
  of *File*, one of them a tracked file of the code, at the row's own line (`:1202-1220`).
- The C40 control (`:1222-1236`) pins the edited sentence's "git tracks" from the other side, in
  both option sets, and break 1 shows it is what catches an untracked file counted as present.
- WAY-203's rewording (`decisions.md:6882-6888`) says where a blocking rule stands — in the
  adopting decision, checked through the one `### Linter` rule — and adds the matching *violates*
  case ("each rule of the set that blocks stands as a rule of its own under `## Rules`"), which is
  I1's point; row 7's meaning is kept. WAY-204's relation was renewed and is current.
- C39 is applied cleanly: no trace of a deferred kind remains in `coding/SKILL.md` (step 3, step 4,
  *Context*); the skill now matches WAY-201 and rows 3 and 22.
- The styleguide template states which required rule carries no cases and which take the
  violated-list reading, conditioned on gradual cleaning as WAY-190 is, without restating the
  common template's rule (`styleguide/template.md:190-196`), as the settlement asked.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

None.

### Minor (Nice to Have)

1. **One line of WAY-203's verification left unwrapped.** `foundations/decisions.md:6896`
   (169 characters): "among the rules that block in the decision adopting the set and blocks a
   change; a rule on the order of imports …" — the rest of the entry wraps at 100. No guard
   reports it and no fingerprint depends on it (verification is not a binding sentence). Fix:
   rewrap the *complies* item.
2. **The styleguide skill's *To do* drops WAY-190's condition.** `product-guidelines/styleguide/SKILL.md:52-54`
   tells the cycle's author to read the cases of `### No value in place of a design token` "as that
   section gives for an invariant on the list of violated invariants and for the invariant beside
   it", unconditionally; the template (`styleguide/template.md:193-196`) and WAY-190 put that
   invariant on the list, with a companion, only where the product cleans its screens as tasks
   touch them. For a single clean-up there is no companion, and the relative reading on a commit
   where the invariant passes gives the same verdicts as the strict one, so no wrong result follows;
   the cycle's author, who reads only the task document, meets a reference to an invariant that may
   not exist. Fix: prefix "where the product cleans its screens as tasks touch their styles,".
3. **"the invariant" of a rule that names up to three.** `foundations/decisions.md:6883-6884`:
   "checked by the invariant of the one rule of the product's coding guidelines on its linter";
   `### Linter` names up to three invariants (`coding/template.md:134-148`), and the one that checks
   a blocking rule is the first (the second keeps the list, the third is the ratchet). The template
   itself says "the invariant of the rules that block" (`:229-230`), so a reader maps it; "the first
   invariant of …" would be exact. Optional — the wording moves the fingerprint again and WAY-204's
   relation with it.

## Recommendations

- Rewrap `decisions.md:6896` and, if the author agrees, add the condition of Minor 2 in the same
  touch; neither changes a fingerprint (Minor 3 would).

## Declined to judge

- `form_check.py:1362-1368`, `check_kind_index`'s docstring, still says "git lists" (explaining it
  as what git tracks): outside the range; the code agrees with the edited sentence, as break 1 and
  the control show.
- M1–M6 of the assessment, settled as kept in `assessment-settlement.md`: the executor's ruling,
  not re-judged.
- The in-place edits of WAY-203 and of `guidelines-check-kind-index/1` without new versions, and
  WAY-203's changed meaning awaiting Mariusz's acceptance at the merge (*Approved by* is the
  placeholder): what `agent-instructions/README.md` allows before `main`.
- The part map's new edge `task-cycle` → `product-guidelines` closing a cycle: the assessment
  found 236 cycles already on the map; the edge is justified by `task-cycle/skill/SKILL.md:339-347,
  392-394`.
- Clauses of the touched invariants other than the two the breaks name (paths, other fences, the
  exemplar): not changed in this range and broken in earlier reviews.
- Python 3.13 in this environment against the declared 3.14 (return step O3).

## Assessment

**Ready to merge? Yes** (the three Minors may be taken or left).

**Reasoning:** Every settlement asked of this range is implemented as ruled — the edited
kind-index sentence matches the code, the skill no longer defers a kind, WAY-203 says where a
blocking rule stands and its fingerprint is carried correctly, the styleguide files point to the
test cases — and each of the three deliberate breaks (four, with a second variant of break 2) is
caught by a test citing the broken invariant; all tests and guards pass at `a839ea7`.

Counts: Critical 0, Important 0, Minor 3; findings outside the task's scope: 0 (one note on an
out-of-range docstring set aside under "Declined to judge").
