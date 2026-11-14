# Report of the fix after the review of the whole change — decision-log-second-round

**Status:** done (finding 6 and 11 left to the orchestrator as the handoff says; two observations for the
orchestrator below, none blocks).

Worktree `the task's worktree`, branch `task/decision-log-second-round`,
reviewed head `6a984c5`, head after the fix `3849483`. Nothing pushed; the product's whole gate not run.

## Commits (9, `6a984c5..3849483`, 35 files, +170 -148)

| Commit | Finding |
|---|---|
| `26575cd` Say in the linter rule of the coding template that the exemplar is not changed for one file's sake ... | 1 |
| `27acdf2` Remove from the reading of environment facts the rule ... that slice 4 restated | 2 |
| `046d779` Give the reason of the pairs of a correction's line in the record template ... | 3 |
| `d31ae66` Name in the part map the tests and the README that WAY-09 required ... | 5 |
| `b0b7e3a` Take the dangling clause out of the identifier rule of the common rules | 7 |
| `a068f99` Remove the reason of projected mode that the four element skills repeated ... | 8 |
| `d55625e` Remove the rule sentences that stand also in the files they repeated and wrap the lines of route_changes.md | 9 (and 10 for that file) |
| `7fb0bb4` Add derives from WAY-100 to WAY-258 and wrap the added lines of the log to 100 columns | 4, 10 |
| `3849483` Wrap the added lines over 100 columns in the skill and guideline files and end the list item of audit_count.py with a semicolon | 10 |

## Findings

1. **Fixed** (`26575cd`, `product-guidelines/coding/template.md`, rule **Linter**). The clause of WAY-207
   is back: "a fault of one file is fixed in that file, and the exemplar of its kind is not changed for that
   file's sake", and the reason of the entry's *Rationale* ("the exemplar is what every later file of its kind
   follows, so changing it for one file's sake changes what binds all the later ones"), placed beside the
   reason the rule already gave for the configuration. Wording from WAY-207 at the base (lines 6428-6462 of
   the base log), the reason in the pattern of the existing sentence.
2. **Fixed** (`27acdf2`): the bullet is removed from `elements/environment-facts/skill/read.md`; the file is
   back to the plan's text (WAY-37 taken out of line 6, nothing else). The rule stands in
   `elements/common/way_of_working.md:114-118` ("whether the change brings what entries of the foundation wait
   for ...; each such entry is fixed in the same change, because an entry that says what holds until something
   exists turns false when it arrives, nothing leads from the arrival to what waits for it ... so a fix left
   for later goes missing"). Checked: it stands there with the rule and the reason; the first bullet of the
   file sends the reader to that section ("Reading the foundation" of the same file). Nothing else needed.
3. **Fixed** (`046d779`, `task-cycle/record_template.md`): one sentence after the definition of the kind,
   word for word the first sentence of WAY-358's *Rationale* ("A pair keeps apart who raised a correction,
   which is read, and what was wrong, which is judged, so that two numbers come out of the pairs: a defect that
   the review of the change let through, `remark · defect`, and a defect that the cycle saw and left,
   `item · defect`"). The second sentence of the *Rationale* (the human sees the kind at the merge) and the
   *Rejected* were not added: the finding asks one sentence.
4. **Fixed** (`7fb0bb4`): WAY-258 *Relations* now `derives from WAY-256 · derives from WAY-100`, the pattern
   of the other adopters (e.g. WAY-167). Nothing else of the entry changed.
5. **Fixed, by the part map** (`d31ae66`, `foundations/part_map.md`), the first of the two ways the finding
   gives; the words come from WAY-09 at the base:
   - `installation`: "preparing a product repository to use one pinned commit of the-way: the installer, its
     tests and a README explaining how a product uses the pinned version" (`installation/README.md` and its
     tests exist);
   - `gate`: "the command that runs every test of the-way, with its tests, and for the tests of critical flows";
   - `instruction-files`: "the script that checks instruction files mechanically and its tests";
   - `project-level`: "and for the tests of its readiness check, its plan check and its reader of
     task-cycle evidence for plan states".
   Partly contested: the finding lists `elements/common` and the script that migrates a foundation as
   missing; the `elements-common` sentence already holds it ("the script that migrates a foundation from the
   earlier form of the-way", `foundations/part_map.md:69-70`), so I changed nothing there. The readiness
   check, plan check and reader of plan states were already named by the `project-level` sentence as
   "readiness gate", "check of that plan" and "evidence-backed upkeep of task states"; only their tests were
   missing. `foundations/decisions.md` WAY-09 untouched (the handoff names WAY-258 alone).
6. **Not touched** (the orchestrator's; no WAY-202 or keep/withdraw decision touched).
7. **Fixed** (`b0b7e3a`, `elements/common/rules.md`): the sentence now reads "Splitting or merging entries
   gives each entry that comes out of it a new identifier. A change of meaning is made in the entry itself, so
   only a split or a merge changes an identifier." — the sentence of the base (before this change) plus the
   reason from WAY-64's *Rationale*; "held there" and the repeated clause are gone.
8. **Fixed** (`a068f99`): the sentence "Projecting keeps a future ... visible in the definition without
   claiming that it already holds" (and, in the decisions skill, "so a new decision carries no number yet")
   is removed from the four skills; it stands at `elements/common/projected_mode.md:4`. The sentence added to
   `elements/invariants/skill/SKILL.md` about code-dependent evidence ("Code-dependent evidence can be
   completed when the task writes the entry, so the method reads `review` until then") is not the one the
   finding names; I left it.
9. **Fixed** (`d55625e`), one sentence each, each against the place the finding gives:
   - `project-level/lead/skill/route_changes.md`: "You change definition text yourself only when ... otherwise
     you delegate the edit" removed; it stands in `project-level/lead/skill/definition_change.md:10`, which
     the same paragraph already names.
   - `product-guidelines/coding/kinds.md`: "Where the product holds no file of a kind, the exemplar of that
     kind is designated by the task that creates its first file" removed; it stands in
     `product-guidelines/coding/SKILL.md`, "A new kind". The sentence after it ("Who designates the exemplar
     follows from the state of the product: ...") stays, as the reason; it still reads on its own.
   - `elements/common/skill/build_table.md`: the bullet on the working table and the `Candidates:` line
     removed; it stands in step 5 of `definition_variant.md:63-67` and `task_variant.md:54-58`. (The clause
     "each accepted row is recorded in it as it is worked through" of WAY-115 stands in those files only as
     the row states of step 4, "set the row to `written`".)
   - `product-guidelines/styleguide/starting_rules.md`: the sentence on the timing removed ("The styleguide
     of a user interface comes into being before ... first screen"; the description of
     `product-guidelines/styleguide/SKILL.md` gives it); the reason sentence "A first screen built with no
     rules is the screen every later one copies" stays, since the plan asked each file for its reason.
10. **Fixed** (`d55625e`, `7fb0bb4`, `3849483`). Method: a script (`.runs/fix-whole/reflow.py`, since removed)
    took from `git diff -U0 ec7929d` every line the change added with more than 100 characters, outside table
    rows, and re-wrapped it at 100 columns outside backtick spans. A line that follows is joined only where it
    is itself a line the change added; otherwise the overflow stands as a short line of its own, so no line
    the change did not touch is rewrapped (hence some short lines mid-paragraph, e.g.
    `gate/run_tests.py:17-18`, `process-audit/audit_count.py:134-135`). Covered:
    - the files the finding names: `product-guidelines/template.md` (13, and also 94), `gate/run_tests.py:17`,
      `foundation-review/weak_points.md:28`, `instruction-files/judging.md:16`,
      `project-level/skill/read_foundation.md:7`, `task-cycle/review/whole_change.md:34`,
      `elements/glossary/template.md:86`, `task-cycle/skill/SKILL.md` (steps 4, 9, 10 and the stage reports:
      lines 159, 274, 286, 457);
    - the same fault in lines the finding did not list: `elements/invariants/template.md:60`,
      `product-guidelines/audit_end.md:91`, `product-guidelines/coding/hand_back.md:11`,
      `product-guidelines/coding/recognize.md:5`, `product-guidelines/reading.md:89`,
      `project-level/plan/skill/guideline_tasks.md:7`, `project-level/technology/list.md:45`,
      `task-cycle/change_file_sizes.py:2`, `task-cycle/gate_times.py:2`, `task-cycle/review/SKILL.md:77,120`,
      `task-cycle/skill/spec_review.md:9`, `task-cycle/spec/design.md:27-28`,
      `process-audit/audit_count.py:134`;
    - the log: 21 lines in WAY-90, 134, 206, 215, 216, 243, 276, 287, 309, 316, 328, 339, 360, 368. WAY-288,
      named by the finding, holds no added line over 100 characters at the head (checked), so nothing to change.
    - `process-audit/audit_count.py:54`: "cycle started under." now ends with a semicolon, like the other items
      of that list.
    Not wrapped, by design: table rows of *Withdrawn identifiers* (a table row cannot wrap),
    `foundations/part_map.md:270` (a table row) and `foundations/invariants.md:88` (a line of 289 characters of
    the invariant `tracked-file-private-paths` that the change modified; a binding list the invariant's test
    reads, not touched). After the fix the same script finds no added prose line over 100 characters.
11. **Taken as the rule of my own check**; see the own-work check.

## Own-work check (WAY-164): each touched rule read against its entry at the base

The base log was read from `git show ec7929d:foundations/decisions.md`.

- Finding 1 against WAY-207: both halves of the rule (no rule of the linter off for the product; no exemplar
  change for one file's sake) and both halves of the reason now stand in the template; the approval clause stood
  already. Matches *Verification*'s violation "the exemplar is changed so that a new file departing from it
  passes".
- Finding 3 against WAY-358: the sentence is the entry's own; the pairs, the source and the kind were there.
- Finding 5 against WAY-09: each part sentence read against the sentence of its directory in the base entry;
  only the contents that were missing were added; `elements-common`, `relation-model`,
  `agent-instructions`, `product-guidelines`, `foundation-review`, `process-audit` and `task-cycle` already say
  what the base said (read, not grepped).
- Finding 7 against WAY-41, WAY-64: the identifier rule says what the base `rules.md` said, plus the reason of
  WAY-64.
- Findings 8 and 9 (removals): for each removed sentence I read the place that keeps it
  (`projected_mode.md:4`, `definition_change.md:10`, `SKILL.md` "A new kind", step 5 of the two variants,
  the skill description) and the withdrawn entry whose rule it was (WAY-117, WAY-156, WAY-200/201, WAY-115,
  WAY-184). Two consequences for the withdrawn list, below.
- Finding 2 against WAY-37: the rule and the reason stand once, in `way_of_working.md`.
- The expectation that most likely failed was a rule left incomplete by a removal; the check that could find it
  was this reading, and it showed the two points below.

## For the orchestrator (not changed, outside the files I may change)

- *Withdrawn identifiers* rows whose *Why* now names a place that no longer holds the whole rule:
  WAY-184 ("stands in `product-guidelines/styleguide/starting_rules.md`": the timing now stands in the
  description of `product-guidelines/styleguide/SKILL.md` and the reason in `starting_rules.md`); WAY-156
  ("stands in `project-level/lead/skill/route_changes.md`": the edit-yourself clause stands in
  `project-level/lead/skill/definition_change.md`, which `route_changes.md` names); WAY-115 ("stands in
  `elements/common/skill/build_table.md`": the closing of the working table stands in the two variants).
  Each is a one-place edit of the *Why* if the orchestrator wants the rows to point to the exact place; this is
  a result of findings 9, taken as the review asked.
- The one `listed:` line of `foundation_check.py` for `tracked-file-private-paths` stands as expected.

## Checks (focused; each after the last change, run on the tree that `3849483` holds)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`, the one expected `listed:` line for `tracked-file-private-paths`); run twice, again at the head |
| `python -B agent-instructions/skill_entry_points.py` (skill files touched; descriptions unchanged) | 0 (`entry points are current`) |
| `python -B gate/run_tests.py elements/common` | 0, 201 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0, 39 tests OK |
| `python -B gate/run_tests.py gate` | 0, 36 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0, 104 tests OK (5 skipped) |
| `python -B gate/run_tests.py process-audit` | 0, 182 tests OK |
| `python -B gate/run_tests.py project-level` | 0, 275 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0, 440 tests OK |
| `git diff HEAD --check` before the commits | 0, nothing reported |
| script: added prose lines over 100 characters in `git diff -U0 ec7929d` (outside table rows and the two files named above) | none left |

Directories I changed that hold no tests: `foundation-review/`, `foundations/` (checked by
`foundation_check.py`), `product-guidelines/`, `elements/decisions/`, `elements/environment-facts/`,
`elements/glossary/`, `elements/invariants/` (the elements' skills; `elements/part-map` and `elements/common`
hold the element tests, run above). The gate test that failed once for the reviewer
(`test_by_default_every_directory_runs_at_the_same_time`) passed in this run.

## Reaches beyond the dispatch

- The base log `git show ec7929d:foundations/decisions.md`: WAY-207, WAY-358, WAY-09, WAY-64 (whole) and
  WAY-115, WAY-156, WAY-184 (head of each, for the observation above): the handoff named the base log for the
  own-work check.
- `elements/common/skill/definition_variant.md` (steps 4-5), `task_variant.md` (step 5), `SKILL.md` of
  `elements/common/skill/`, `product-guidelines/coding/SKILL.md` ("A new kind"), `product-guidelines/styleguide/SKILL.md`
  (head): to confirm where each removed sentence stands (finding 9).
- `installation/`, `gate/`, `project-level/`, `instruction-files/` directory listings: to name only contents that exist (finding 5).

## Unread material

- `product-guidelines/coding/template.md` and `elements/common/rules.md`: read in the region I changed (the
  rule **Linter** and lines 40-70) and in the diff of the change, not whole; the other files I changed I read in
  the diff and the region, not whole (Edit accepted them without a read of the whole file).
- `.runs/task-cycles/decision-log-second-round/task.md` and `plan.md`: not read; I relied on the findings file
  and the review's report, which quote them.
- `task-cycle/change/slice.md`, `project-level/technology/reserved_choices.md`: not read (not needed here).
- The review report: read whole.

## Searches not found or unclear

- None unclear in the instructions. For finding 10 the finding names "WAY-288" among the log's rewritten lines
  over 100 columns; at the head no added line of WAY-288 exceeds 100 characters (a count in characters; if the
  reviewer counted bytes, the lines with a dash would differ by two columns).

## Working copies

`.runs/fix-whole/` of the worktree held: `base.md` (the base log), `w09_base.md`, `w09_head.md`, `long.txt`,
`ctx.txt`, `d2.txt`, `d_log.txt`, `diff_nolog.txt`, `stat_before.txt`, `reflow.py` and `t_*.txt` (the output of
the seven test runs). No worktree or clone was made. Removed file by file before returning, then the
directory itself (see the end of this section for any remainder).

Choices: finding 5 by the part map and not by the request (the reviewer's other way) — cost if wrong: the
part-map sentences are a little longer and the human may wish the rule narrower; the other way would leave a
rule that requires less than the base. Finding 10 by short lines and not by rewrapping whole paragraphs — cost
if wrong: a few ragged lines; the other way touches lines the change did not.

Remainder: none.

## Addition: the *Why* of three withdrawn rows (allowed by the orchestrator after the fix)

Commit `0364c08`: only the *Why* of three rows of *Withdrawn identifiers* in `foundations/decisions.md`
(+3 -3, nothing else in the log):

- WAY-115: now `elements/common/skill/build_table.md`, `elements/common/skill/definition_variant.md` and
  `elements/common/skill/task_variant.md` (the closing of the working table with the `Candidates:` line stands in
  step 5 of the two variants).
- WAY-156: now `project-level/lead/skill/route_changes.md` and `project-level/lead/skill/definition_change.md`
  (the clause on who edits definition text stands in the second).
- WAY-184: now `product-guidelines/styleguide/SKILL.md` (the timing, in its description) and
  `product-guidelines/styleguide/starting_rules.md` (the starting rules wider than the first task).

Checks after the change:

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`, the one expected `listed:` line for `tracked-file-private-paths`) |
| `python -B gate/run_tests.py elements/common` | 0, 201 tests OK |

I made no new working copy and removed no file outside `.runs/fix-whole/` (already removed).
