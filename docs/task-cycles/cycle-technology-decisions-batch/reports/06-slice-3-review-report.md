PASS 8b5662de6c5eab11c590a4f99d72a73d80825ccd

# Review of slice 3 (a blocked draft request shown as blocked by the plan-state reader)

Range `7b04db09dc37fdd6abfee1330e8d19568177cd89..8b5662d`, one commit (`8b5662d`). `git rev-parse HEAD`
equals `8b5662de6c5eab11c590a4f99d72a73d80825ccd`. I computed the diff myself (`git diff 7b04db0..8b5662d`,
`git log 7b04db0..8b5662d`) and read the dispatch copy of the selection in
`.runs/task-cycles/cycle-technology-decisions-batch/reports/05-slice-3-handoff.md`.

Counts: blocking 0, Minor 2 (both inside the task), out of scope 0.

## Findings

### Critical

none

### Important

none

### Minor

1. **A lone carriage return after the wording is read as the field's line**
   (`project-level/plan_state.py:166-169`, `record_requests`). `git grep` prints the whole line;
   `result.stdout.splitlines()` on bytes also cuts at a lone `\r`, so a line
   `- Request URL and status: blocked draft, opened on this commit\r<any text>` is cut to the wording
   and recognised, although text follows on the same physical line. The skill files now say "word for
   word and alone on its line". Evidence: a scratch run (below) of that record printed
   `evidence 1 reports: blocked draft request in record docs/task-cycles/reports/record.md commit <sha>`.
   Effect: only the fixed evidence line appears; no text of the record reaches the output, so the trust
   boundary holds. The loosening is of recognition only (an author-written stray `\r` mid-line, which
   Markdown renderers treat as a line break anyway), and the PR pointer reader has the same property
   today. The new crafted-input test (`test_blocked_draft_wording_off_the_field_line_prints_nothing_of_the_record`)
   has no case with a lone `\r`. Not blocking; a case plus a split on `b"\n"` would close it.
2. **The wording inside a fenced block of the record is read as the field** (same function). The
   executor states this as a known limit ("Drift / mismatches"). My scratch run confirmed it: a record
   with the line inside a code fence is reported blocked. It is the same limit the PR pointer lines have
   (the reader does not parse Markdown), the output is again only the fixed line, and the task asks for
   recognition "in the same way and from the same Git reads" as the pointer. Minor, accepted by design;
   the limit is not written in any foundation entry, so a reader of `plan_state.py` finds it only in
   this report and in the executor's.

## Verification of the executor's claims

- **Goal (item 7), reader side.** Met. One `git grep` read with two `-e` patterns (the PR URL pattern
  as before and `re.escape(BLOCKED_DRAFT)`), one new constant, one added loop in `task_report`; the
  existing pointer lines, proposals, conflicts, exit codes are untouched in the diff. The new line sits
  after the pointer lines of the same commit, so the order of existing lines is unchanged.
- **Goal, record side.** Met. `task-cycle/skill/reserved_return.md` step 2 and
  `task-cycle/skill/blocked_finding.md` now both give the field the wording `blocked draft, opened on
  this commit`, "word for word and alone on its line", with the reader named. `record_template.md:178`
  keeps the generic `<URL and draft/ready/blocked>` for records that have a request; consistent. A grep
  for `opened on this commit` finds the wording only in these two skill files, the script and its test.
  Other paths that open a blocked draft (`foundation_step.md:31`, `SKILL.md:22`, `:115`, `:213`) do not
  mention this field; item 7 names only the two skill files, so I did not require them.
- **Trust boundary, crafted input** (the handoff's list):
  - Control characters / look-alike text / extra text on the field's line: not recognised (test cases
    "control characters after/inside the wording", "look-alike letters" (Cyrillic o), "text after the
    wording"); a form feed or no-break space after the wording is also not recognised (my scratch run:
    no blocked line). Only trailing space, tab and CR are tolerated.
  - Wording inside a fenced block: recognised (Minor 2), output unchanged in form.
  - Wording in another file of the record: not read. `record_requests` gets `records`, the paths
    `provenance()` returns, i.e. files with `Task source`/`Task relation` headers; the description
    `request.md` and other files are not passed to `git grep` (read of `plan_state.py:241-281`).
  - An instruction in the record: never printed. The new line is `"evidence %s: blocked draft request in
    record %s commit %s"` with `prefix`, `display(<path listed by Git>)` and `commit` (the id from
    `git log`); the record's text is only compared (`text.rstrip(" \t\r") == BLOCKED_DRAFT`), never
    kept. The `source.startswith(commit + ":")` guard and `len(parts) == 3` skip malformed rows.
  - Subprocesses: still only `git` (the same `git.run("grep", ...)`); no other subprocess call is added
    in the diff. The existing test `test_plan_state_subprocesses_invariant.py` passes inside the
    `project-level` run (below).
  - Existing output lines unchanged: the real-URL test keeps its `PR pointer` line byte for byte; a
    record carrying both a real URL and the wording prints both lines (scratch run), no line lost.
- **Pattern in `git grep -E`.** `re.escape` puts `\-` and `\ ` in an ERE; Git's matcher read it as a
  literal in this environment (tests pass on Windows, the author's platform). Portability of `\ ` to
  other regex engines was not checked (not run elsewhere); a record not recognised would show as before
  the change, so the failure is silent but safe.
- **Tests.** They fail when the behaviour breaks: the first two assert the exact blocked line (the
  executor's failing-first run is in its report; I did not re-create the pre-change state, since that
  needs a changed tree; unverified by me, plausible from the diff: without `record_requests` no line is
  printed). The crafted-input test checks the absence of the line, of a new proposal, of ESC/BEL and of
  the injected `in cycle -> done`. The expected values are literals, not computed by the code. The
  executor's mutation (`BLOCKED_DRAFT in text`) is credible: the crafted cases "wording in prose",
  "quoted", "indented", "text after the wording" would all match it.
- **Foundation.** No entry is written or changed by this slice. The change agrees with
  `project-plan-state-command` (evidence-bearing proposals, no new proposal/conflict/exit code),
  `project-plan-state-evidence` (no proposal made from the blocked line) and
  `project-plan-state-subprocesses`; WAY-153 does not enumerate evidence line kinds. No invariant test
  was changed.
- **Reserved choice:** none taken (no language, library, store, login or place to run).
- **Guidelines:** the handoff selected none; no guideline file reached by the change was named, and I
  made no reach for one.
- **Own-work check:** the executor named the right weakest requirement (nothing else of the record
  reaches the output) and its check (ten crafted cases plus a mutation) would catch it unmet, except for
  the lone-`\r` case of Minor 1.

## Declined to judge

- Whether the other paths that end in a blocked draft request (`task-cycle/skill/foundation_step.md`,
  `SKILL.md` steps for a human action and for a remaining blocking finding other than the two named
  files) write a record copy that should carry the same wording: item 7 names only `blocked_finding.md`
  and `reserved_return.md`.
- Whether a record whose request later gets a real URL should stop showing the blocked line: the
  task and slice fix no such rule, and the line is tied to the commit it was found in.

## Checks run

- `git rev-parse HEAD` -> `8b5662de6c5eab11c590a4f99d72a73d80825ccd`, equal to the head given.
- `python -B -m unittest discover -s project-level -p "test_plan_state.py"` -> exit 0 (`Ran 44 tests`, OK).
- `python -B gate/run_tests.py project-level` -> exit 0 (`Ran 275 tests`, OK).
- `python -B elements/common/foundation_check.py --skip-test-citations` -> exit 0 (`0 errors`).
- `git diff --check 7b04db0..8b5662d` -> exit 0.
- Scratch probes, a script outside the reviewed worktree
  (`a scratch file outside the repository`),
  subclassing the fixture of `test_plan_state.py` in a temporary directory; the reviewed worktree, index
  and branch were not changed (`git status --short` empty). Cases: lone CR then extra text -> recognised
  (Minor 1); fenced block -> recognised (Minor 2); wording plus a real PR URL -> both lines; form feed
  after the wording -> not recognised; no-break space after the wording -> not recognised. Exit 0.
- Not run: the full `python -B gate/run_tests.py` (the cycle's own run); the failing-first state of the
  new tests (needs a changed tree).

## Reaches beyond the dispatch

- `task-cycle/record_template.md:170-200` (already in the selection at 176-195, read slightly beyond);
  `project-level/plan_state.py:120-150, 241-281, 370-420` (the callers and `provenance`, to learn which
  files `git grep` reads); `project-level/test_plan_state.py:140-166` (fixture helpers);
  `project-level/test_plan_state_subprocesses_invariant.py:95-160` (what the subprocess invariant test
  observes); a grep for `opened on this commit|blocked draft|Request URL and status` across
  `*.md`/`*.py` outside `.runs/` (to find other writers of the field).
- `a document in the author's private notes`, read before the scratch script (the author's
  own rule for scripts).

## Searches not found or unclear

none
