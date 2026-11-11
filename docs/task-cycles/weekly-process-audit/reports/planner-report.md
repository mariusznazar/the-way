# Planner report — weekly-process-audit

- Status: done with concerns
- Plan: `.runs/task-cycles/weekly-process-audit/plan.md`
- Size report: `.runs/task-cycles/weekly-process-audit/plan-size.md` — the last run of
  `python -B task-cycle/slice_size.py .runs/task-cycles/weekly-process-audit/plan.md` from the
  worktree's root, exit 0: all 7 slices `fits` (largest: Slice 3, 3 files, about 48,000 estimated
  tokens).
- Check result: slice_size.py exit 0, no slice too large or unchecked; no other check run (the plan
  holds no code).

## The plan in short

*Foundation entries* (written first, before Slice 1): the 12 rows of *Settlements to record*, all
decisions; WAY-09 changed (To do 1); the *Scope* of WAY-38, WAY-89 and WAY-320 extended with the new
part (through WAY-21).

Slices, made in this order:

1. The part `process-audit` and its directory: the template of the register of problems and the
   part-map entry — strongest, no risk.
2. `task-cycle/cycle_stages.py`: the wait for tools per stage and in the summary, a subagent call
   not counted; each stage's start time and tokens by model and kind — cheaper, no risk.
3. The counting command `process-audit/audit_count.py`: locations entries, unattended run, cycle
   records found in the named repositories' history, per cycle the pin, the number of remarks, the
   working time and the wait for tools; the part's *Trust boundary* — strongest, trust boundary.
4. The dated price list and the cost at constant prices with the share of fix rounds — cheaper,
   trust boundary.
5. The register read: problems per cycle by class and weight, the issues in place with and without
   their fix, the open issues — cheaper, trust boundary.
6. Each process version's median cost and three answers, and the series kept apart — cheaper,
   trust boundary.
7. The skill `audit-process`, its generated entry points and the README — same, no risk.

## Open design choice and reserved choice

None found. Every decision the change needs stands in a row of *Settlements to record* or in the
change of WAY-09 that *To do* item 1 names; the extensions of the *Scope* of WAY-38, WAY-89 and
WAY-320 follow from WAY-21 and change no meaning. No language, framework, library, store of data,
way of logging in or place to run outside what the foundation settles (Python with the standard
library, WAY-38; git as the only program started). The shapes the handoff leaves to the slices —
the register template, the command's result, the keys of the locations file — are left to Slices 1,
3 and 4 to 6, each asked to name its choice in its report.

## Guidelines

The-way has no product guidelines: no coding, testing or styleguide file to read. The task's answer
under *Questions to settle* says their absence does not hold this task (WAY-215); I name it here as
the method asks. The change touches no user interface, so there is no styleguide example of the
order of work to follow or depart from.

## Concerns

1. **The foundation check reports between the entries and Slice 1.** The *Foundation entries* name
   the part `process-audit` in their *Scope*, and its part-map entry comes only with Slice 1, which
   adds the directory's first file (`task-cycle/plan/SKILL.md` puts a part-map change for a new file
   in the slice that adds the file; a *Files* pattern that matches no tracked file is an error too,
   WAY-44). So `python -B elements/common/foundation_check.py --skip-test-citations` on the entries'
   commit reports the references to `process-audit`, and only those; after Slice 1 it reports
   nothing. The plan says so under its *Foundation entries* table, so the agent writing the entries
   is not stopped by it.
2. **Four slices with a review of their own.** Slices 3 to 6 all change
   `process-audit/audit_count.py`, which the start's answer names as the trust boundary, so each gets
   a review aimed at crafted input, plus the review of the whole change. Splitting reading from
   computing into two files would shorten that, but the computing still takes untrusted text from
   records (see *Choices*).
3. **Prices are data taken from outside sources.** Slice 4 has to take each model's prices from the
   provider's published price page, with its address and the date read, never from memory. Where the
   executor cannot reach those pages, every cost comes out `unknown`; the slice says so rather than
   guessing.
4. **Old records give `unknown`.** Records written before Slice 2 lack the wait for tools and the
   per-stage tokens by model, and older ones may lack the WAY-296 form of remarks. The early weeks of
   the audit will show many `unknown` values; the plan has the command give `unknown` with a reason,
   never zero.
5. **The size report counts no file an earlier slice creates.** `process-audit/problem_register.md`
   and `process-audit/audit_count.py` do not exist at the base, so the *Read* fields of Slices 3, 5
   and 7 name them without backticks and the script does not count them. What those agents read is
   larger than the report shows, though still far under the limit.
6. **`task-cycle/cycle_stages.py` reads files from the user's disk, but no trust boundary covers
   it.** It reads session transcripts on the user's disk, which WAY-48 counts as "files that come
   from outside the product, such as one on the user's disk", while the part map gives `task-cycle`
   *Trust boundary* none. Slice 2 is marked `Risk: none`, following the part map as the method
   requires. Proposed answer: leave this to the return step or to a review of the foundation; it is
   not this task's to settle.
7. **Is the counting command a surface?** A user's system scheduler will call it by its path and
   arguments (WAY-49: a command someone outside relies on). The task does not ask the-way to promise
   to keep it, so the plan adds no surface entry. Proposed answer: no surface in this task; the
   return step or the human may weigh it at the request.

## Questions

None that hold the plan. The proposed answers to concerns 6 and 7 stand above; the readings of
unclear points stand under *Choices* in the plan and under *Searches not found or unclear* below.

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md:290-314` (step 9, Plan): how the row `Foundation entries` is
  dispatched before Slice 1 and checked with it, so I could place the part-map entry against the
  transient foundation-check finding.
- `task-cycle/skill/SKILL.md:425-444` (step 12) and a search for `stages.md|cycle_stages` across the
  tracked files: who runs `cycle_stages.py` and which texts describe `stages.md`, to decide what
  Slice 2 changes.
- `task-cycle/change/SKILL.md:20-59`: how an executor reads its foundation entries and writes an
  entry through an element's skill, for Slice 1's part-map entry.
- `README.md:95-144`: the list of directories and of the directories that hold a skill, which
  Slice 7 extends.
- `installation/install.py:25-59` and a search for `SKILLS` in `installation/`: whether a new skill
  has to reach products, for the choice not to install the audit skill.
- `project-level/backlog_place.md` whole: how a locations entry is read and what happens when it is
  missing, which Slices 3 and 7 follow.
- `elements/common/foundation_check.py:1-60` and `task-cycle/tracked_private_paths_check.py:1-30`
  (docstrings): to name the slices' checks with their arguments.
- `task-cycle/slice_size.py:1-80` (docstring): how *Read* and *Change* are measured, for the paths
  of files that earlier slices create.
- A search for `foundation-review` across the tracked files outside `foundations/decisions.md`: where
  the directories of the parts are listed, to find every file a new part touches (README, installer,
  part map).
- A search for `locations.json` across the tracked files: existing readers of the locations file
  (only `project-level/backlog_place.md` and the root `AGENTS.md`).
- A search for test files citing `cross-part-imports`, `map-reference-target`, `skill-entry-points`
  and `tracked-file-private-paths`, and a listing of `elements/part-map/`: which test directories
  the slices' checks run.
- Listings of `foundation-review/`, `task-cycle/` and the method directories `task-cycle/change/`,
  `plan/`, `review/`, `spec/`, `skill/`, with a search for `Searches not found or unclear` in
  `task-cycle/`: where the forms of the stage reports and the reviewer's instructions stand, for
  Slice 6's series.
- `git log` of `docs/task-cycles/**/plan.md`: to look for an earlier plan that added a part; none
  was inspected further.

## Unread material

- `task-cycle/remarks_check.py`: read lines 1-120 of 361 (the docstring, constants and the first
  helpers); the rest was not needed to cut slices, and Slice 3 reads it whole.
- `agent-instructions/skill_entry_points.py`: read lines 1-70 of 247 (the docstring, constants and
  the git helper); Slice 7 only runs it.

Everything else the handoff names was read whole: the frozen task; the decisions WAY-09, WAY-103,
WAY-140, WAY-260, WAY-296, WAY-320, WAY-40, WAY-41, WAY-42, WAY-44, WAY-48, WAY-49, WAY-21, WAY-38,
WAY-89, WAY-127, WAY-125, WAY-148, WAY-150, WAY-229, WAY-255, WAY-256, WAY-265, WAY-101, WAY-107,
WAY-13, WAY-134, WAY-135 and WAY-136 (WAY-45, WAY-102 and WAY-126 were read too, as they stood inside
the ranges read); the invariants named; `foundations/part_map.md` and `foundations/glossary.md`;
`task-cycle/cycle_stages.py`, `task-cycle/test_cycle_stages.py`, `task-cycle/record_template.md`,
`project-level/plan_state.py`, `foundation-review/SKILL.md` and `gate/run_tests.py`.

## Searches not found or unclear

- Not found: a decision that governs `task-cycle/cycle_stages.py` or `stages.md`. I searched
  `foundations/decisions.md` for `cycle_stages`, `stages.md`, `transcript` and "how long each stage";
  the only hits were unrelated (WAY-229, WAY-255).
- Unclear: whether "czas pracy agentów" (To do 3, row 9) includes the wait for tools or excludes it.
  The task's *Context* names their joining as the problem, and row 9 asks for them as a pair; the
  plan takes the working time without the wait, the two adding up to today's working time (*Choices*).
- Unclear: what a "wersja procesu" (To do 3, row 10) groups — each *Process pin*, or the pins
  between two changes of the process. In the-way's own cycles nearly every cycle has a pin of its own,
  so a median per pin is often a median of one cycle. Slice 6 groups by pin and names its grouping.
- Unclear: from what date the "dni czekania" of an open issue (To do 3) count — the first cycle of
  its problem, or the day the issue entered the register. Left to Slice 5 to name.
- Unclear: what a "runda poprawek po recenzji" (To do 3, row 8) spans — the fix alone, or the fix and
  the review of that fix. The plan takes both (*Choices*).
- Unclear: how the command can tell "zmiana formatu raportu etapu" or of the reviewer's instructions
  (To do 4, row 10) from any other change to the same method files; left to Slice 6 to name.
- Unclear: whether `task-cycle/cycle_stages.py` is a trust boundary under WAY-48, since it reads
  session transcripts from the user's disk, while the part map gives `task-cycle` none (concern 6).
- Unclear: whether the counting command is a surface under WAY-49 (concern 7).
- Not found: a list, in the-way, of the tool calls by which Codex and Claude Code start, message or
  wait for a subagent. `task-cycle/cycle_stages.py` finds subagents by their files and by
  `parent_thread_id`, not by tool call, so Slice 2 has to find those names in transcripts.
