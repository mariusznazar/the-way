# Report of the fix of the whole-change review's findings

**Status:** `done`

Findings: `findings.md` beside this file (review of `2754675..c0a0f52`, FAIL: I-1 blocking; M-1,
M-2, M-3 Minor within the task). All four fixed; none contested.

## Commit and files

Commit `eeca32c` on `task/define-project-skill-shape`, from the reviewed head `c0a0f52`: "Have step 6
of define-project name the gate's file for a readiness-check finding, and orient the delegated
mode's file". Only `project-level/skill/` changed.

| File | Added | Removed |
|---|---|---|
| `project-level/skill/SKILL.md` | 9 | 6 |
| `project-level/skill/delegated_mode.md` | 3 | 0 |
| `project-level/skill/existing_definition.md` | 4 | 4 |

Reports regenerated after the last change to a counted file: `word-counts.md`
(`make_word_counts.py`) and `assessment.md` (`make_assessment.py`, with `proposals.md`). The
figures of `author_report.md` are updated to the tree after the fix, with a pointer to this
report at its top. The scripts `compare_sentences.py` and `check_pointers.py` are updated, as
listed under the findings.

## The findings

### I-1 - a readiness-check finding at step 6 had no text that named where it goes - fixed

The finding holds. In the base, 7.1 stood in the one `SKILL.md` read whole, so a finding that
`project-level/technology/close.md:6-10` hands back "to `define-project`, which names where", or that
the check of step 6 reports, found its routing. After `c0a0f52`, 7.1 stood only in `gate.md`,
which only step 7 named.

The fix, in `SKILL.md`:

- Step 6, `SKILL.md:73-75`: "Read `technology.md` beside this skill. Where the readiness check
  reports a finding at this step, in the run `technology.md` gives or handed back by
  `settle-technology`, read `gate.md` beside this skill: the finding goes where its 7.1 sends it."
- Step 7, `SKILL.md:79-80`: "Read `gate.md` beside this skill unless step 6 had you read it; in a
  turn dispatched through a refinement conversation path it points to `delegated_mode.md` for what
  changes."

This is text that two steps consult, so it stands in a file that each step names, and a later step
does not have it read again (WAY-256). I put the pointer in `SKILL.md` at step 6, not in
`technology.md`. Then one sentence covers both ways a finding comes: the check that `technology.md`
runs, and the hand-back of `close.md`, which returns the agent to `define-project`, that is, to
`SKILL.md`.

Each new or rewritten sentence, compared with the base (criterion 2):

- **The sentence of step 6.** Condition: a finding of the readiness check at step 6, from either
  source. In the base, a finding at step 6 went where 7.1 sends it, with 7.1 already before the
  agent. After the fix it goes the same way, now by naming the file.
  - It adds no route: 7.1 is unchanged, and the base already applied it to such a finding, since
    `close.md` hands the finding back for `define-project` to name where.
  - It restores the route that `c0a0f52` lost.
  - It switches off the agent at step 6 guessing where a finding goes, or opening `gate.md` early
    on its own and reading step 7 as begun.
  - It does not set `ready for gate`. `technology.md`'s "Once ... reports nothing ... set the
    status line to `ready for gate`" still governs that.
- **"unless step 6 had you read it" at step 7.** It switches off a second reading of `gate.md`
  when step 6 already had it read. The base had one file read once, so no route is added or lost.
  - The price, as WAY-256 states it: a session that skipped step 6 reads the file at step 7. Every
    route that starts at step 7 (route 4, the dispatched turn, a resume whose status reads
    `ready for gate`) did not pass step 6, so the condition does not hold and it reads `gate.md`.
  - The dispatched-turn clause is unchanged.

Check: `check_pointers.py` now expects `gate.md` to be named under step 6 and step 7 of `SKILL.md`,
and both sentences to be present. Shown failing: with step 6's pointer made to name `rounds.md`, it
exited 1 with three failures. Restored, byte-identical by `cmp`, it exited 0.

Walk of the reviewer's routes 1, 2 and 5:
- Each reaches step 6, reads `technology.md`, and runs `settle-technology`.
- On a finding, either handed back or from the check of `technology.md`: `SKILL.md` step 6 sends
  the agent to `gate.md`'s 7.1, which names the file of step 4, 5 or 6.
- Without a finding: `ready for gate`, and step 7 reads `gate.md`.

### M-1 - "below" no longer covers the files beside the skill - fixed

- `SKILL.md:14-15`: "The decisions that set its rules are cited below and in the files beside
  this skill."
- `SKILL.md:20-21`: "each skill named below or in the files beside this skill is the project skill
  of that name with the `the-way-` prefix".

Neither sentence has a condition. The second widens the prefix rule back to every skill the skill
names, which it covered in the base, when all of them stood below it. It switches off a narrow
reading of "below", under which an agent that reads `SKILL.md` by its path could call `critique`,
`find-foundation-entries`, `settle-technology` or `plan-project` without the prefix. The meaning of
WAY-127's paragraph is unchanged.

`assessment.md` proposal 6 now says the reword is applied here, and proposes it for the four other
skills of the series that keep "each skill named below". The series now words this paragraph two
ways, and the request should say so.

Check: `compare_sentences.py` lists the reworded unit by name in its expected rewordings, and
exits 0.

### M-2 - `delegated_mode.md` had no orientation line - fixed

`delegated_mode.md:3-4`: "The variant of the skill `define-project`, whose `SKILL.md` lies beside
this file, for a turn that `lead-project` dispatches; "this same workflow" below is the steps that
`SKILL.md` gives."

It orients the reader and gives no instruction. Its "for a turn that `lead-project` dispatches"
describes the file and is no condition for reading it. The condition that has the file read stays
in `SKILL.md`, word for word the base's. The line switches off reading "this same workflow" as
anything other than the skill's steps. The base sentence under it is unchanged.

### M-3 - one line over the wrap width - fixed

`existing_definition.md:6-9` rewrapped. The words are unchanged, and the file still has 205 words.
The longest line of the ten files, frontmatter aside, is now within 100 characters, checked by
`awk 'length>100'` over `project-level/skill/*.md`, which prints only `SKILL.md:3`, the
frontmatter `description`.

## Checks

| Command | Exit code |
|---|---|
| `python -B gate/run_tests.py project-level` (on `eeca32c`) | 0, 271 tests OK |
| `python -B elements/common/foundation_check.py .` | 0, "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | 0, "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file project-level/skill/SKILL.md --file project-level/skill/delegated_mode.md --file project-level/skill/existing_definition.md` | 0, `0 error, 1 warn, 7 info` (the root `AGENTS.md`'s `_zadania\` warning of the base; INFO `definition_template.md` relative at `SKILL.md:13`, `:45`, as on the base) |
| the same with `--file` for each of the ten files | 0, `0 error, 1 warn, 14 info`, as `assessment.md` states |
| `python -B <reports>/make_word_counts.py` then `make_assessment.py` | 0; 54 rows, 0 errors |
| `python -B <reports>/compare_sentences.py` | 0: 121 units of the base, 8 not word for word, all named |
| `python -B <reports>/check_pointers.py` | 0 |
| `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/author_report.md` | 0, 263 figures compared, 0 differ; `wc -w` cross-check on 15 files in two locales |

Not run:
- `gate/run_tests.py installation` and `agent-instructions`: the fix touches no file they read
  beyond what `skill_entry_points.py` checks, and the description is unchanged.
- The whole gate, which is the orchestrator's.

## Figures after the fix

| Route | Skill text before | Total before | Skill text after | Total after |
|---|---|---|---|---|
| 1 | 1937 | 5869 | 1840 (-5.0%) | 5772 (-1.7%) |
| 2 | 1937 | 5366 | 1516 (-21.7%) | 4945 (-7.8%) |
| 3a | 1937 | 6785 | 1684 (-13.1%) | 6532 (-3.7%) |
| 3b | 1937 | 6785 | 2387 (+23.2%) | 7235 (+6.6%) |
| 4 | 1937 | 5366 | 1342 (-30.7%) | 4771 (-11.1%) |
| 5 | 1937 | 5366 | 1408 (-27.3%) | 4837 (-9.9%) |

- `SKILL.md` alone: 570 words.
- `delegated_mode.md`: 342 words.
- All ten files: 2387 words.

`word-counts.md` gained one rule: `gate.md` counts once on every route, whether it is read at
step 6 for a finding or at step 7.

## Own-work check

- **The requirement the fix most likely misses:** a route that starts at step 7 without passing
  step 6 losing `gate.md` through "unless step 6 had you read it".
- **The check:** I walked every route that reaches step 7: routes 1, 2, 3a, 3b, 4 and 5, the
  fingerprint mismatch of `existing_definition.md`, and the resume of a definition whose status
  reads `ready for gate`. For each I asked whether step 6 could have had `gate.md` read in the
  same session.
- **What it showed:**
  - Only routes 1, 2 and 5 pass step 6, and on them the file is read at step 6 or at step 7, once.
  - Routes 3a and 4, the mismatch and the `ready for gate` resume never run step 6 before step 7,
    so the condition is false and step 7 reads the file.
  - A dispatched turn whose 7.1 finding sends it back to step 6 has already read `gate.md` at
    step 7, so it holds the file when it returns.

## Reaches beyond the dispatch

- `project-level/technology/close.md`, whole, to confirm the hand-back's wording ("any other
  finding goes back to `define-project`, which names where").

## Searches not found or unclear

- Step 0 runs `readiness_check.py` on an approved definition (`existing_definition.md:9-12`) and
  routes only a fingerprint mismatch (to step 7). It does not say where another finding of that
  run goes. In the base, 7.1 stood in the same file. It is unclear whether the base meant 7.1 to
  route such a finding at step 0. The review did not raise it, and I did not extend the pointer to
  step 0, since that could add a route. Route 4 goes on to step 7, which runs 7.1 anyway.
