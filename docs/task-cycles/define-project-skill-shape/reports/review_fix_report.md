PASS eeca32c97a492aca5954e82914daf28d7ee59758

# Review of the fix — `define-project` in the shape of WAY-256

Range: `c0a0f52..eeca32c`, one commit, "Have step 6 of define-project name the gate's file for a
readiness-check finding, and orient the delegated mode's file". `git rev-parse HEAD` prints
`eeca32c97a492aca5954e82914daf28d7ee59758`, the head given. Method: `task-cycle/review/SKILL.md`
and `task-cycle/review/fix.md`. Bounded by `findings.md` (I-1 blocking; M-1, M-2, M-3 Minor within
the task). The fix report was read as claims, each checked below.

Counts: blocking 0; Minor 0 remaining, 0 new; out-of-scope notes 1 (the fix report's search item,
below).

## The findings of `findings.md`

**I-1 — fixed.** `project-level/skill/SKILL.md:73-75`, step 6: "Where the readiness check reports
a finding at this step, in the run `technology.md` gives or handed back by `settle-technology`,
read `gate.md` beside this skill: the finding goes where its 7.1 sends it." Step 7
(`SKILL.md:79-80`): "Read `gate.md` beside this skill unless step 6 had you read it".
- The hand-back of `project-level/technology/close.md:10` ("goes back to `define-project`, which
  names where") now lands on `SKILL.md` step 6, which names the file holding 7.1
  (`gate.md:11-16`), and so does a finding of `technology.md`'s own run of the check
  (`technology.md:7-9`). Walked by hand on routes 1, 2 and 5: `technology.md` → `settle-technology`
  → `close.md` → a non-g finding → `SKILL.md` step 6 → `gate.md` item 1 → the file of step 4, 5 or 6
  named there; without a finding, `ready for gate` → step 7 → `gate.md`, read once either way.
- WAY-256 shape: text that steps 6 and 7 consult stands in one file both steps name, and the later
  step does not have it read again; that is the form the decision's *Verification* gives as
  compliant.
- Criterion 2, the new sentence of step 6: its condition (a finding of the readiness check at step
  6, from either run) is exactly the set of findings the base answered from 7.1 in the one file the
  agent held. It adds no route — 7.1 is unchanged and only consulted — and restores the one the
  rebuild lost. It switches off guessing where the finding goes, and opening `gate.md` early with
  step 7 taken as begun: "the finding goes where its 7.1 sends it" bounds what is used. It does not
  touch the condition that sets `ready for gate` (`technology.md:7-9`). Condition-g findings
  `close.md` routes itself are not "handed back", so they stay with `settle-technology`, as in the
  base.
- Criterion 2, "unless step 6 had you read it" at step 7: switches off a second reading of the same
  file. Every route that starts at step 7 without step 6 — route 4, route 3a, a fingerprint
  mismatch from `existing_definition.md:9-12`, a resume at `ready for gate` — has the condition
  false and reads `gate.md`; a dispatched turn sent back to step 6 by 7.1 already holds it. No
  route lost; the dispatched-turn clause stands word for word as before.
- Considered and not a finding: at step 6 `gate.md` is read for 7.1 only, and its opening points to
  `delegated_mode.md`, which `SKILL.md` names at step 7 and under its own section, not at step 6.
  WAY-265's aim — every file a use may reach visible in `SKILL.md`, with its condition — is met:
  the file and its condition are named there, and a dispatched agent reads it first, before step 0.

**M-1 — fixed.** `SKILL.md:14-15` "cited below and in the files beside this skill";
`SKILL.md:20-21` "each skill named below or in the files beside this skill is the project skill of
that name with the `the-way-` prefix". No condition; the second restores the base's coverage (every
skill the skill names) and switches off the narrow reading of "below" under which `critique`,
`find-foundation-entries`, `settle-technology` or `plan-project` would be called unprefixed. It
says what the entry point already says ("Where this skill or a file it reads names another the-way
skill"); WAY-127's meaning is unchanged. The series now words this paragraph two ways, as the fix
report says; the request is to say so.

**M-2 — fixed.** `delegated_mode.md:3-4`: "The variant of the skill `define-project`, whose
`SKILL.md` lies beside this file, for a turn that `lead-project` dispatches; "this same workflow"
below is the steps that `SKILL.md` gives." It orients and instructs nothing. "for a turn that
`lead-project` dispatches" describes the file; the condition that has the file read stays in
`SKILL.md:27-29` and in the next sentence of this file, word for word the base's (base
`SKILL.md:27-28`), so no route is added. It switches off reading "this same workflow" as the text
of this file alone.

**M-3 — fixed.** `existing_definition.md:6-9` rewrapped; the token sequence of the file is
identical before and after (`diff` of whitespace-split tokens, exit 0) and it still counts 205
words. `awk 'length($0)>100'` over `project-level/skill/*.md` prints only `SKILL.md:3`, the
frontmatter `description`, as on the base.

## New in the fix diff

Nothing Critical or Important. No Minor.

## The fix report's search item, judged

"Step 0 runs `readiness_check.py` on an approved definition and routes only a fingerprint
mismatch." The text is the base's word for word (base `SKILL.md:59-63`; now
`existing_definition.md:8-12`), and the base routed no other finding of that run either: 7.1 routes
the `--before-approval` run of step 7, and 7.5 only requires the no-option run to report nothing.
With the fingerprint matching, such a finding means the definition was approved over a gap the
script now sees (a template or checker changed since — the case the next bullet already handles
for a missing `## Technology`) or a malformed gate record (condition e not a mismatch). The rebuild
lost no route here: on route 4 the agent goes on to step 7 for the change, where 7.1 runs. I agree
with the author not to extend the pointer in this task; giving step 0 a routing for such findings
would be new content. Out of scope of the fix (outside its diff; fix.md); a note, not a finding.

## Figures recomputed

`LC_ALL=C.UTF-8 wc -w`: `SKILL.md` 570, `delegated_mode.md` 342, `existing_definition.md` 205, the
ten files 2387; the unchanged files as in the first review (82, 109, 98, 240, 108, 66, 567). Route
sums and percentages (`python -c`), with the files read beside the skill unchanged: route 1
1840/5772 (-5.0%/-1.7%), 2 1516/4945 (-21.7%/-7.8%), 3a 1684/6532 (-13.1%/-3.7%), 3b 2387/7235
(+23.2%/+6.6%), 4 1342/4771 (-30.7%/-11.1%), 5 1408/4837 (-27.3%/-9.9%); the six recorded runs, 3a
reading 9918/36671 (-14.7%/-4.4%), 3b reading 12730/39483 (+9.5%/+2.9%). All equal to
`word-counts.md` (summary and six-run table), the task-estimate lines, and the fix report's table.
`word-counts.md`'s new rule ("`gate.md` counts once on every route") matches step 7's "unless step 6
had you read it". No stale after-figure of `c0a0f52` (516, 314 after, 1786, 1602, 2305, 1288,
1354, 1462 and their totals) remains in `word-counts.md` or `assessment.md`; in `author_report.md`,
"1288" survives only in the description of a mutation test run on `c0a0f52`, which its new header
says the rest of the report describes.

## Checks run

| Check | Command or method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `eeca32c...`, the head given |
| Scope | `git diff --name-only c0a0f52..eeca32c \| grep -v "^project-level/skill/"` | exit 1 (nothing outside) |
| Pointers | `python -B <reports>/check_pointers.py` (updated by the author: `gate.md` under steps 6 and 7) | exit 0, "10 files; 0 failures" |
| Counts, author's script | `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/author_report.md <reports>/fix_report.md` | exit 0, 279 figures, 0 differ; `wc -w` cross-check on 15 files in two locales |
| Counts, mine | `wc -w` and `python -c` above | all equal |
| Clauses | `python -B <reports>/review_clauses.py` | exit 1 by design: 21 not word for word — the 18 of the first review plus the two M-1 rewordings (base lines 14, 19-20) and a heading/orientation-line splitter artefact for the delegated section; no unexplained loss |
| M-3 tokens | `diff <(git show c0a0f52:project-level/skill/existing_definition.md \| tr -s ' \n' '\n\n') <(tr -s ' \n' '\n\n' < project-level/skill/existing_definition.md)` | exit 0 |
| Wrap | `awk 'length($0)>100'` over `project-level/skill/*.md` | only `SKILL.md:3` |
| Entry points | `python -B agent-instructions/skill_entry_points.py` | exit 0, "entry points are current" |
| Foundation | `python -B elements/common/foundation_check.py .` | exit 0, "0 errors" |
| Instruction files | `python -B instruction-files/check_instructions.py . --file <each of the ten files>` | exit 0, `0 error, 1 warn, 14 info` (the base's warn) |
| Focused tests | `python -B gate/run_tests.py project-level` (background) | exit 0, 271 tests OK |
| Routes | manual walk of routes 1, 2, 3a, 4, 5 through steps 6 and 7 | as under I-1 |
| Step 0 item | `git show 2754675:project-level/skill/SKILL.md \| sed -n 59,63p` against `existing_definition.md:8-12`; `project-level/readiness_check.py:1-36`, `:276-310` | text identical; no routing for a non-mismatch finding in the base |

Not run: the whole gate (the orchestrator's); `gate/run_tests.py installation` and
`agent-instructions` (the fix touches neither; entry points checked directly); the author's
`compare_sentences.py`, `make_assessment.py` and `make_word_counts.py`, which rewrite the author's
record files.

## Declined to judge

- A routing at step 0 for a non-mismatch finding of the readiness check on an approved definition:
  outside the fix diff and absent from the base (above).

## Reaches beyond the dispatch

- `project-level/readiness_check.py:1-36`, `:276-310`: which findings the no-option run can give on
  an approved definition, to judge the fix report's search item.
- `project-level/technology/close.md` (read in the first review): the hand-back the fix answers.

## Searches not found or unclear

- A place where the base routed a non-mismatch finding of step 0's check on an approved definition:
  not found (judged above).
- Whether "a turn that `lead-project` dispatches" (`delegated_mode.md:3`) could be read as a
  condition wider than "a definition edit or step 7 through a refinement conversation path": unclear
  in principle; the next sentence gives the exact condition and `SKILL.md` has the file read only on
  it, so I raised nothing.
