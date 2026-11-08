# Fix report 1 — Minor findings of the whole-change review (PASS 038a330)

**Status:** `done`

**Commit:** `08e70be` Fix the Minor findings of the whole-change review of lead-project (branch `task/lead-project-skill-shape`, on top of `038a330`). Files: `foundations/decisions.md` (+44 / -43), `project-level/lead/skill/SKILL.md` (+4 / -4), `project-level/lead/skill/definition_change.md` (+1 / -1).

Findings read from `reports/findings-fix-1.md`. Nothing outside the six findings was changed.

## Each finding

### Minor 1 — the figure in WAY-256 (fixed, both places)

- *Rationale* now reads `estimated before any rebuild from the word counts of the files of one skill, that shape reads five to fifteen percent more words in a typical session than keeping its steps in SKILL.md`.
- *Rejected* now reads `an estimate of five to fifteen percent more words read in a typical session, made before any rebuild from the word counts of that skill's files`.
- I kept the figure in both places and stated its nature in both, as the reviewer's first option allows. The skill is not named, which WAY-05 forbids for a file or a count of the foundation; the figure counts words of a skill's files, not entries of the foundation.
- Check: `git diff -w --word-diff=porcelain 038a330 -- foundations/decisions.md` shows only the words `before any rebuild`, `word counts of the`, `estimated` → `estimate of`, `session;` → `session, made before any rebuild from the word counts of that skill's files;`. My road check asserts the phrase `before any rebuild` stands twice in the entry (result in Checks).

### Minor 2 — the pending-gate road and `route_changes.md` (fixed)

The first sentence of the step 5 pointer now reads: `On reaching this step, from a refiner's result plan change, from a changed definition in step 0 or from a gate or recheck found pending there, read route_changes.md beside this skill.` The second sentence is unchanged: `For a change of the definition, its gate or the plan recheck after it, a gate or recheck found pending in step 0 included, read definition_change.md beside this skill too.`

I chose the reviewer's first option (word the first sentence to include the pending gate), because on this road the base read all of step 5, so `route_changes.md` is read on it, with the rule on the `plan-project` agent's questions and the rerun of the whole-plan check. The exact conditions of the criterion hold: `route_changes.md` on the result `plan change` and on a changed definition in step 0 (kept, in the same words); `definition_change.md` on step 5 and on the recovery of an open gate in step 0 (kept, in the same words). What is added is the pending gate or recheck of step 0 to the first condition. What it excludes: nothing outside step 5; a pending gate that is not found in step 0 is not a road of this skill.
Check: `roads.py` assertions `M2` (first sentence names `route_changes.md`, `plan change`, `changed definition in step 0`, `found pending there`; second names `definition_change.md` and `found pending in step 0 included`).

### Minor 3 — `this route` (fixed)

`definition_change.md` now ends `A check passing the old fingerprint or approval alone does not complete the definition change.` (reviewer's option: a noun with an antecedent). Check: `roads.py` assertion `M3` (`this route` absent from the file, the new ending present).

### Minor 4 — long lines of WAY-256 (fixed)

Re-wrapped to 100 columns, line breaks only: in the Rationale and in the Rejected paragraph, from the first long line to the end of the paragraph (in the Rationale the new-line break between its two halves now also runs together, which is a line break too). Counted in characters, not bytes, the entry has no line over 100 (`roads.py` assertion `M4`). The `awk length` count the reviewer used counts bytes (`—` is three bytes in the C locale), so it still lists lines 7601, 7677 and 7688 at 103, 101 and 102 bytes; in characters they are 99, 99 and 100. The word-level diff above shows no word moved.

### Minor 5 — the word-count columns mix two bases (contested as code; no code changes)

It is a matter of how the request states the table; no file changes. Where I hold otherwise: my report (section 5) already says the `after` side files are counted at `57795e4` (7255) and the `before` at `a3206c1` (7253), and that the skill-text columns are exact. The orchestrator can either give the side files at one commit in both columns (the skill-text change is the same: see the table below) or say so beside the table. The skill-text change (column 3 of my table) is unaffected by the 2 words.

### Minor 6 — opening lines `technology_run.md:3` and `task_return.md:3–4` (contested as code; no code changes)

No code changes. The reviewer is right that these two lines restate the pointer's condition. The honest entry for the request, in the form it can copy: `technology_run.md` opening line: *restates the pointer's condition (a run of the step that settles technology, reached from 3.1 or 3.3); excludes nothing the pointer did not*; `task_return.md` opening line: *restates the pointer's condition (the human has said a blocked request is closed); adds no road; the transitions made from evidence are excluded by that condition, not by this line*.

## Numbers of my first report that this fix changes

Recomputed with `counts.py` (Python `wc`-equivalent through the real `wc -w` of Git Bash, `LC_ALL=C`) and confirmed by the independent `verify_numbers.py`. The fix changes two counted files: `SKILL.md` 2036 → 2044 (+8, the longer first sentence of the pointer of step 5) and `definition_change.md` 270 → 271 (+1). Unchanged: `route_changes.md` 176, `task_return.md` 246, `technology_run.md` 129, the old `SKILL.md` 2580, the side files 7253 / 7255, and every number outside section 5 of the first report.

| Number | Before the fix | After the fix |
|---|---|---|
| `SKILL.md` words | 2036 | 2044 |
| `definition_change.md` words | 270 | 271 |
| the five files together (against 2580 before the rebuild) | 2857 (+277) | 2866 (+286) |
| pointer of step 5 in `SKILL.md` | 53 | 61 |
| all pointers in `SKILL.md` | 166 | 174 |
| road 1 skill text / with step-0 files | 2482 (-98, -3.8%) / 9737 (-96, -1.0%) | 2491 (-89, -3.4%) / 9746 (-87, -0.9%) |
| road 2 | 2212 (-368, -14.3%) / 9467 (-366, -3.7%) | 2220 (-360, -14.0%) / 9475 (-358, -3.6%) |
| road 3 | 2036 (-544, -21.1%) / 9291 (-542, -5.5%) | 2044 (-536, -20.8%) / 9299 (-534, -5.4%) |
| road 4 | 2458 (-122, -4.7%) / 9713 (-120, -1.2%) | 2466 (-114, -4.4%) / 9721 (-112, -1.1%) |
| road 5 | 2341 (-239, -9.3%) / 9596 (-237, -2.4%) | 2349 (-231, -9.0%) / 9604 (-229, -2.3%) |
| road 6 | 2482 (-98, -3.8%) / 9737 (-96, -1.0%) | 2491 (-89, -3.4%) / 9746 (-87, -0.9%) |

"Before the rebuild" is 2580 on every road and 9833 with the side files (unchanged). The task's estimates for the skill text (1: 2400–2550, 2: 2050–2250, 3: 1950–2100, 4: 2300–2500, 5: 2150–2350, 6: 2400–2550) still contain every measured number (road 5, 2349, only just). The estimate for the five files together (+170 to +370) contains +286. The first report was regenerated with these numbers and with the new commit; it also gained one table row (`:219 this route`) and its row for the step 5 pointer carries the new text.

## Checks

| Command (from the worktree root) | Exit code | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn, 3 info |
| `python -B gate/run_tests.py instruction-files` | 0 | ----------------------------------------------------------------------; Ran 104 tests in 2.278s; OK (skipped=5) |
| `python -B gate/run_tests.py agent-instructions` | 0 | ----------------------------------------------------------------------; Ran 18 tests in 3.459s; OK |
| `python -B gate/run_tests.py elements/common` | 0 | ----------------------------------------------------------------------; Ran 109 tests in 23.049s; OK |
| `python -B gate/run_tests.py project-level` | 0 | ----------------------------------------------------------------------; Ran 271 tests in 104.428s; OK |
| `python -B gate/run_tests.py installation` | 0 | ----------------------------------------------------------------------; Ran 44 tests in 204.307s; OK |
| `python -B roads.py` (my road and sentence checks, M1–M4 included; scratchpad) | 0 | 33 assertions pass, 0 fail |
| `python -B fid.py` (word comparison, old SKILL.md against the new files) | 0 | only the differences of the first report plus `this route` → `the definition change` |
| `python -B verify_numbers.py` on the regenerated `author-report.md` | 0 | all numbers agree with the files |
| `awk 'length($0)>100'` on the WAY-256 entry | 0 | three lines at 101–103 bytes, 99–100 characters (see Minor 4) |

Not run: `python -B gate/run_tests.py` without a directory (the orchestrator runs it).

## Own-work check

- **Requirement most likely missed in the fix:** the criterion that the condition of each pointer covers every road and is worded as reaching the step, which Minor 2 touches; and that a fix of Minor 4 changes no word. The check: `roads.py` (33 assertions, now with `M1`–`M4`) reads the files and asserts the pointer conditions of every road of the criterion, the absence of `this route`, the 100-character limit and the two `before any rebuild` phrases; a word-level diff (`git diff -w --word-diff=porcelain 038a330 -- foundations/decisions.md`) lists only the intended words of Minor 1. Result: 33 pass, 0 fail; the word diff shows only those words.
- **Long-line check, two runs:** `awk 'length($0)>100'` lists three lines (103, 101, 102 bytes); read with Python they are 99, 99 and 100 characters, so the check in characters (`roads.py` M4) passes.
- The fix touched no moved sentence except the last of `definition_change.md`; the word comparison of the old `SKILL.md` with the new files (`fid.py`) lists only the differences named in the first report plus `this route` → `the definition change`.

## Searches not found or unclear

- The reviewer's long-line list (`7601, 7659, 7662, 7688, 7691, 7692, 7696`) is in bytes and its line numbers shifted when I edited the entry for Minor 1; I took the intent (no line of the entry over 100 columns) and checked it in characters. In bytes three lines still exceed 100; they are 99 to 100 characters.
- Whether the orchestrator wants the figure of WAY-256 dropped from one place instead of qualified in both: I kept it in both (reviewer's alternative); the other choice is a one-line edit.
- Minor 5 and 6 concern the request's text; I did not see the request's draft.
