PASS fb60dc7d8578db8372a384e7fecf711459b169c9

Review of the return step's commit (`review-change`), range
`41921006168c95b1de449ea546fab2271ec815e9..fb60dc7d8578db8372a384e7fecf711459b169c9`, one commit
`fb60dc7d` ("Return step: name the new info lines of the instruction check and a slice that fits by
ranges"), two files: `task-cycle/skill/planning.md` (+1 −1), `instruction-files/SKILL.md` (+2 −1).
`git rev-parse HEAD` = `fb60dc7d8578db8372a384e7fecf711459b169c9`, the head given.

## The two corrections

1. `task-cycle/skill/planning.md:15-16` — the orchestrator's review of the plan now asks for "a size
   report in which every slice fits, by ranges of a file or not". Right: `task-cycle/slice_size.py`
   reports `fits by ranges of <file>` (`slice_size.py:124-128`) and exits 0 for it (docstring
   `:57`, same words "every slice fits, by ranges of a file or not"); `task-cycle/plan/SKILL.md:224-225`
   (task point 4, wording accepted) says "the review of the plan accepts it as it stands". Without
   the correction the orchestrator, reading "every slice fits", could send such a slice back to the
   planner against the plan skill. Sufficient: the only other place that judges the size report is
   `planning.md:19-20` ("a slice it now reports too large returns to the planner"), which already
   fits; no other skill or record reads `plan-size.md` for a verdict (`git grep "plan-size\|slice fits"`).
2. `instruction-files/SKILL.md:56-59` — step 1's example list of `info` lines now names "an absolute
   path of another machine" and "a path under a name the root `.gitignore` gives alone". Right: the
   code gives both at level `info` (`instruction-files/check_instructions.py:615-624`, with
   `elsewhere` at `:560-568` and `ignored_names` at `:571-590`). Sufficient: the list is "for
   example", and the sentence after it ("never followed") holds for both, which the code neither
   reads nor looks up.

## The claim "no other mismatch, nothing else to write"

Checked against the entries the whole change writes:

- WAY-255 (new paragraph, examples, *Rationale*, *Rejected*): the stop at 30 minutes, report with
  command and last lines, and "the check ... as one that did not run" stand in
  `task-cycle/change/SKILL.md` (§3 last bullet), `task-cycle/review/SKILL.md:113-118` and
  `task-cycle/skill/SKILL.md:290-293`, which enters it in the record's Events (the section exists,
  `task-cycle/record_template.md:102`). Holds.
- WAY-25 (new paragraph, examples, *Rejected* row on a check over `narrows`): the same wording
  stands in `elements/decisions/template.md` "Changing a decision"; `elements/decisions/skill/SKILL.md`
  says every rule of an entry stands in the template (`:8-11`), so the skill needs no copy. Holds.
- WAY-136 (new sentence, examples, *Rationale*, *Rejected*): `task-cycle/plan/SKILL.md:189-195`,
  `task-cycle/skill/planning.md:39-42`, `task-cycle/skill/SKILL.md:468-485` ("a listed test that
  fails as the plan says is none (WAY-136)"). The binding sentence — a named failure is no failing
  check of the slice — is held where the orchestrator decides the retry. Holds; see Minor 1 for the
  executor's side.
- WAY-418 (new): `installation/README.md:88-89` and `task-cycle/review/whole_change.md:27-33` say
  the same; its complying example "a block of code or text the script takes for no path" agrees
  with the code (fenced blocks skipped, `check_instructions.py:389-395`; text that is no path,
  docstring `:18-22`). Scope `instruction-files, task-cycle, installation` names existing parts.
- Part map (`foundations/part_map.md:7-213`): no file added or moved outside its part's pattern;
  `task-cycle/review/whole_change.md` names `installation/README.md` and task-cycle depends on
  `installation` (`:112`); `elements/decisions/skill/SKILL.md:38-39` no longer names a file of
  `task-cycle`, and no other file under `elements/decisions`, `elements/part-map`,
  `elements/environment-facts` names one (`grep -rn "task-cycle/"`: nothing). Holds.
- Environment facts: WAY-73 (`foundations/decisions.md:2128-2135`) lets a fact stand only while an
  invariant's *Rests on* or a decision's *Based on* names it; no entry the change writes names the
  behaviour of `shutil.which` or the CDX index, so writing none is right.
- New series of gate times (WAY-339): the audit derives it from the history of
  `task-cycle/gate_times.py` and `gate/run_tests.py` (`process-audit/version_analysis.py:107-108`);
  no file lists series, so nothing to write. Holds.
- Pairs of examples vs tests: no test of the change carries `decision:` for WAY-25/136/255/418,
  so the pairs stay whole, as the report says.

## Findings

### Critical

none

### Important

none

### Minor

1. `task-cycle/change/slice.md` (whole file) and `task-cycle/change/SKILL.md` §3 — the executor's
   own method says nothing of the tests the plan leaves failing at its base. WAY-136's complying
   example and `task-cycle/plan/SKILL.md:191-193` have the executor of a later slice "report a listed
   test that fails as expected, not as a failing check of its slice", and `planning.md:39-41` has
   the handoff list those tests "so that its executor reports" so — but the executor reads neither
   file, and nothing tells it what the list in its handoff is for. Why it matters: an executor that
   runs "the tests of the code you touched" may report a listed test as a failing check, or try to
   make it pass in files outside its *Change*. The consequence is bounded: the orchestrator compares
   the report's failures with the plan's list and does not retry for a listed one
   (`task-cycle/skill/SKILL.md:472-485`), and a file outside *Change* is caught by the mechanical
   check, so WAY-136's binding sentence holds. A sentence in `slice.md` "Read" (the handoff lists the
   tests the plan leaves failing at the slice's base; report a listed test that fails as expected and
   leave it to its owner) would close it. Within the task (point 3); the task placed the wording in
   the plan skill and the orchestrator's skill only, so this is a gap of sufficiency, not a missed
   requirement. Evidence: `grep -n -i "as expected\|leaves failing\|failing at its base"` over
   `task-cycle/change/*.md` finds nothing.
2. `instruction-files/check_instructions.py:12-18` — the module docstring says "Three cases are noted
   at the level `info`", but `dead_path_note` gives a fourth: a bare relative name in a file given with
   `--file` (`:610-614`, present at the base too). Return step's correction 2 lists the `info` lines
   "for example", so the skill is not wrong; the docstring is the script's own description and
   undercounts. Within the task (point 5) but outside this range — a sentence of the whole change's
   code, not of the return step's commit; offered for the request's list.

## Declined to judge

- The rest of the whole change's code (`decision_index.py`, `gate_times.py`, `run_tests.py`,
  `check_instructions.py` logic, the tests): reviewed to PASS before the return step; the handoff
  bounds this review to the return step's corrections and mismatches with the foundation.
- The withdrawn-identifier output printing "WAY-46 is withdrawn: withdrawn: it said only…": the
  doubled word comes from the table row itself (`foundations/decisions.md:11685`), not from the
  script; data of the log outside this task.
- The Minor at `instruction-files/check_instructions.py:454` (`'''`): left unfixed by design, not
  touched by this range.

## Checks run

- `git rev-parse HEAD` → `fb60dc7d8578db8372a384e7fecf711459b169c9`, exit 0.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .` → exit 0, `0 error, 0 warn, 5 info` (all
  five are `size` lines).
- `python -B -m unittest task-cycle/test_slice_size.py` → exit 0, 25 tests OK.
- `python -B gate/run_tests.py instruction-files` → exit 0, 122 tests OK (5 skipped).
- `python -B elements/common/decision_index.py --output <copy>/idx.md --decision D-0255 --decision WAY-46 --decision 418`
  → exit 0; WAY-255 and WAY-418 listed in full, the line "WAY-46 is withdrawn: …; its successor
  WAY-40 is withdrawn: …; it has no successor" — agrees with `elements/common/way_of_working.md:105-110`.
- Manual: `git status --porcelain` empty before and after the checks.
- Not run: the gate (the cycle's own run, WAY-160).

## Reaches beyond the handoff

- `task-cycle/slice_size.py:1-135` and `task-cycle/plan/SKILL.md:170-239` — to judge correction 1.
- `instruction-files/check_instructions.py:1-40`, `:555-634`, and the base version's
  `dead_path_note` area (`git show 2a2f4106:…`, `:565-592`) — to judge correction 2 and the
  docstring.
- `instruction-files/check_instructions.py` search for fences (`:69`, `:389-395`) — WAY-418's example.
- `installation/README.md:68-92`, `:250-263` — warnings wording beside WAY-418.
- `foundations/decisions.md:2128-2157` (WAY-73 whole) and the headings of
  `foundations/environment_facts.md` — the claim of no environment fact.
- `elements/decisions/skill/SKILL.md` whole — where WAY-25's new rule should reach.
- `task-cycle/change/slice.md` whole and searches of `task-cycle/change/*.md` — the executor's side
  of WAY-136 (Minor 1).
- `task-cycle/record_template.md` headings — the Events section WAY-255's skill text names.
- `process-audit/*.py` search for `gate_times.py`/`run_tests.py` — the claim on WAY-339's series.
- `foundations/decisions.md:11670-11685` (two rows of the withdrawn table) — the probe's output.

## Working copies

- `.runs/review-return` held
  `idx.md`, the output of the `decision_index.py` probe; removed with `rm -rf` by its full path
  before returning. No probe shows a finding, so nothing was kept in `reports/`.

## Unread material

- WAY-25, WAY-136, WAY-255 not opened whole: read their changed hunks in
  `git diff 2a2f4106..fb60dc7d -- foundations/decisions.md` and their earlier binding text as the
  task quotes it. WAY-418 read whole (all of it is in the diff).
- `elements/decisions/template.md`, `elements/part-map/template.md`, `elements/part-map/skill/SKILL.md`,
  `elements/environment-facts/template.md`, `elements/environment-facts/skill/draft.md`: read the
  hunks the whole change makes, not each file whole.
- `instruction-files/SKILL.md`: read `:40-79` and the hunks of the whole change, not whole.
- `installation/README.md`: read `:68-92` and `:250-263`, not whole.

## Searches not found or unclear

- A sentence in the executor's method (`task-cycle/change/`) on the tests the plan leaves failing at
  a slice's base: not found (Minor 1).
