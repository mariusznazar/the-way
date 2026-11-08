FAIL c0a0f5271cf251055b1ec50f32087220da328698

# Review of the whole change — `define-project` in the shape of WAY-256

Range: `2754675..c0a0f52`, one commit, "Split define-project into a picture of the whole and a file
for each step and variant (WAY-256)". `git rev-parse HEAD` in the worktree prints
`c0a0f5271cf251055b1ec50f32087220da328698`, the head given. One author without a plan; no spec,
no slices, so no slice had a review of its own and every blocking finding below comes from that
one commit.

Counts: blocking 1 (Important), Minor 3 (all within the task), out of scope 0 (Declined to judge
lists 3 lines).

## Findings

### Important

**I-1. A readiness-check finding handed back to `define-project` from step 6 no longer finds where
to go — 7.1's routing now stands only in `gate.md`, which step 6 does not name.**

- Place: `project-level/skill/technology.md:7-9` (step 6) with `project-level/skill/gate.md:11-16`
  (7.1); the caller is `project-level/technology/close.md:6-11`, unchanged.
- What is wrong: step 6 runs `settle-technology`. Its last step, `close.md`, runs
  `readiness_check.py <definition> --before-approval` and says: "any other finding goes back to
  `define-project`, which names where." The only place `define-project` names where a finding of
  that check goes is 7.1 ("A finding of condition f goes back to step 5; a finding of condition g,
  or of condition a in "Technology", goes back to step 6; ... any other finding goes back to step
  4"). In the base, 7.1 stood in the one `SKILL.md` the agent had read whole, so the hand-back from
  step 6 found it. After the rebuild, 7.1 stands in `gate.md`, which `SKILL.md` names only at step
  7 and which the agent reads only "once ... reports nothing ... step 7 begins"
  (`technology.md:7-9`). `technology.md` itself names no file for a finding; `SKILL.md` step 6
  holds only "Read `technology.md` beside this skill." So on routes 1, 2 and 5, which all pass step
  6, an agent returned with a finding of condition f, or a `TODO` left in another section, holds no
  text that "names where": it can only guess, or open `gate.md` early on its own initiative. The
  same holds for a finding of `technology.md`'s own run of the check, which the base answered from
  the same 7.1.
- Why it matters: task acceptance criterion 1 ("Żadna reguła nie znika ... każdy fragment stoi po
  przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest
  potrzebny"), criterion 2 (a rewritten pointer must lose no route) and criterion 5 (a fragment
  several steps need reaches each of them). WAY-256 places text that some steps consult "in a file
  beside the skill that each of those steps names, a step after the first having that file read
  unless an earlier step did"; its *Verification* names as a violation "a rule of working that
  three steps keep stands only in the file of the first, so the other two never reach it". 7.1's
  routing is consulted at step 6 (through `close.md`'s hand-back) and at step 7; only step 7 names
  its file. The author's criterion-5 table and route walk (author report, "Walk of routes 1, 3a, 4
  and 5": route 1 "`technology.md` -> `gate.md`", route 5 "`technology.md` -> `gate.md`") pass over
  this hand-back, and the assessment's row for `L137` lists `close.md:10-11` as a caller without
  checking that "which names where" still resolves.
- Evidence: `grep -rn "define-project" project-level/technology/` gives `close.md:10` "`define-project`,
  which names where" and `close.md:11`; `grep -n "step 4\|step 5\|condition" project-level/skill/technology.md`
  finds nothing; `check_pointers.py` checks the jumps of `gate.md` and `existing_definition.md`
  only, so it passes. Manual walk of routes 1, 2 and 5 below.
- What would close it (the author's choice): have step 6 name 7.1's routing where a finding
  arises — e.g. in `technology.md`, "a finding goes where 7.1 sends it (`gate.md` beside this
  file)" — with `SKILL.md` step 6 naming `gate.md` for that case if it is read as a variant there,
  and step 7's pointer not having it read again where step 6 did (WAY-256). The new sentence would
  have to say what it switches off (criterion 2).

### Minor

**M-1. "each skill named below" and "The decisions that set its rules are cited below" now reach
into the files beside the skill.** `project-level/skill/SKILL.md:14` and `:19-20`. After the
rebuild `critique`, `find-foundation-entries`, `settle-technology` and `plan-project` are named
only in `gate.md`, `find_entries.md`, `technology.md`, and most decisions are cited there too. An
agent reading `SKILL.md` by path with no entry file (criterion 3's reader) may read "below"
narrowly and call `critique` without the `the-way-` prefix; an entry point covers it ("Where this
skill or a file it reads names another the-way skill"). The author raises the first as proposal 6
of `assessment.md` (series-wide reword); I agree it is not blocking: within the task, Minor.

**M-2. `delegated_mode.md` has no orientation line, and its "this same workflow" now points out of
its own file.** `project-level/skill/delegated_mode.md:1-5`. Every step file opens with "Step N of
the skill `define-project`, whose `SKILL.md` lies beside this file"; the variant file of the
delegated mode does not, and its moved sentence "use this same workflow with file-mediated
routing" no longer stands beside the workflow it means. A reader handed the file alone (the
orchestrators' dispatches name the section, and a critic or orchestrator may be handed the file)
must infer which workflow. The plan-project precedent (`project-level/plan/skill/delegated_mode.md`)
has the same gap. Within the task (criterion 3), Minor: the agent arriving by the pointer in
`SKILL.md` already knows.

**M-3. One line over the file's wrap width.** `project-level/skill/existing_definition.md:6` is 103
characters; every other prose line of the ten files wraps at 100 (only the frontmatter
`description` at `SKILL.md:3` is longer, as on the base). Polish, within the task.

## Declined to judge

- The glossary meaning of "gate" against "the readiness gate" (author's proposal 4): the word
  stands unchanged from the base, in WAY-118 and in `definition_template.md`, outside this
  change's files; the task leaves them unchanged.
- The proposals of `assessment.md` (remove the orchestrator's own-edit sentence, the path of
  `definition_template.md`, the repetitions with `lead-project` and the template): the task asks
  that they stand as proposals, not applied (To do 6); I judged only that they are listed, not
  their merit.
- Whether a dispatched turn editing, e.g., scope reads `rounds.md` (route 3a reading only its own
  steps): settled by the human in the task's question 2 ("bez nowego zdania"), with the weak point
  named there; not a finding of this change.

## The task's acceptance criteria, checked

1. **No rule disappears or changes meaning; every fragment stands where its step names it.** My
   clause check (`review_clauses.py`, below) finds every clause of the base in the ten files except
   the rewordings the author lists (step 0's condition, the file names added in parentheses at
   jumps, "Two moves", the rule on answers, the rule on files) and splitter artefacts (a heading
   joined to its first bullet). Fails for one fragment: 7.1's routing does not reach step 6 (I-1).
2. **Rewritten conditions compared with the base.**
   - Pointer to the delegated mode (`SKILL.md:27-29`): condition word for word the base's
     (`:27-28`); no route added or lost. The added clause "it holds what that path changes in the
     workflow below, and the file of step 7 points back to it" is description, switches nothing off.
   - Pointer of step 0 (`SKILL.md:46-47`): adds "— in a dispatched turn, the definition its
     conversation file names —". In the base the dispatched agent read the resume bullet in the
     whole file and was told to use "this same workflow with file-mediated routing", so the base
     already reached it; the clause switches off the reading that "the human" named nothing in a
     dispatched turn, and adds no route (`conversation_template.md` carries `Definition: <absolute
     path>`). Agreed.
   - Pointer of step 7 (`SKILL.md:76-77`) and opening of `gate.md:6-9`: condition "In a turn
     dispatched through a refinement conversation path", the wording `plan-project` already uses
     (`project-level/plan/skill/SKILL.md:70-80`); only `lead-project` dispatches through such a path
     (grep of "refinement conversation" across the-way). No route added or lost.
   - `gate.md:6-9` (new sentence): switches off, in a dispatched turn, speaking to the human
     directly (7.3, 7.5), running `critique` (7.3) and writing fingerprint, record and `approved`
     on unrecorded approval (7.4). Each limb restates `delegated_mode.md:9-10`, `:15-16`, `:19-21`
     without widening; it names the file, so its list is not the only source.
   - Rule "Once the definition is written (step 3), write each answer into it ..."
     (`SKILL.md:36-38`): widens the base's step-4 rule to steps 3-7, the resume and the dispatched
     turn, as criterion 5 requires; the opening clause switches it off at steps 0-2 of a new
     definition, where no file exists and WAY-112 has the goal confirmed before the first write.
     Agreed.
   - Rule "What the files can answer, read yourself instead of asking (WAY-112)" (`SKILL.md:34-35`):
     widened from "through the rounds" to every step, as criterion 5 requires; WAY-112 says it
     without a step ("reads what product files can answer"). "Three moves" → "Two moves"
     (`rounds.md:8`) follows. Agreed.
   - "Speak the language ..." and "A change of the definition after the gate ..." moved word for
     word into the rules (`SKILL.md:33`, `:39-40`). Agreed.
   - Parenthesised file names at jumps (`existing_definition.md:7-8`, `:12`, `:19`; `gate.md:12-16`):
     no condition changed.
   - Not a rewritten condition but a lost route: the hand-back of `close.md` at step 6 (I-1).
3. **Each pointer names its step or variant in words an agent reading `SKILL.md` by path
   recognises.** Every pointer stands under the base's numbered step heading (0-7) or the
   unchanged heading "Delegated definition change and gate"; step 0's and step 7's pointers give
   their conditions in words. Callers that cite numbers still land: `technology/start.md:8`
   ("`define-project` step 5") → `SKILL.md:66-68`; `lead/skill/SKILL.md:208` ("`define-project`
   step 7 in delegated mode") → `SKILL.md:74-77`, naming both `gate.md` and `delegated_mode.md`;
   `plan/skill/existing_plan.md:9` ("`define-project` step 7 again") → `SKILL.md:74-76`; the
   critic handed "SKILL.md step 7" lands on the pointer (task question 3). `gate.md:3-4` maps its
   items 1-5 to 7.1-7.5, and its internal references (7.1, 7.2, 7.3) still hold. Met, except M-1
   and M-2 (Minor).
4. **The delegated mode reaches step 7.** `SKILL.md:76-77` names `delegated_mode.md` at step 7
   with its condition (WAY-265); `gate.md:6-9` says, before item 1, never speak to the human
   directly, request the critique of 7.3 through the conversation instead of running it, and write
   fingerprint, gate record and `approved` only after the human's approval is recorded through the
   project orchestrator. The agent also read `delegated_mode.md` first, from the section's
   pointer. Met.
5. **Fragments needed at several steps reach each.** "Speak the language", "What the files can
   answer", the rule on answers and "A change ... after the gate" stand in `SKILL.md`, read whole
   on every route; 7.1's jumps name `rounds.md`, `find_entries.md`, `technology.md`
   (`gate.md:11-16`); `existing_definition.md` names `find_entries.md`, `technology.md`,
   `gate.md`. Met for the cases the criterion names; not met for 7.1's routing at step 6 (I-1).
6. **Nothing outside `project-level/skill/`; description and Python unchanged.** Met (checks
   below).
7. **Word counts.** Recomputed (below); every figure of `word-counts.md`, the author's report's
   table and the proposal's 31 words matches. The base is 1937 words under `LC_ALL=C.UTF-8 wc -w`
   and 1929 under `LC_ALL=C`; the 8 between are standalone em dashes (9 em dashes in the file, 8
   standing alone). The author's statement holds. The counts will need recomputing if I-1's fix
   changes `technology.md`, `gate.md` or `SKILL.md`.
8. **Foundation entries.** Selected below; no departure found beyond I-1's against WAY-256.

## Manual walk of routes 1, 3a, 4 and 5

As an agent holding the path of `project-level/skill/SKILL.md` and no entry file.

- **Route 1, a definition from an idea, steps 0-7.** `SKILL.md` read whole: the delegated
  section's condition is not met; the four rules are taken; step 0 reads the template and "How a
  skill asks"; no definition named → "Otherwise begin with step 1" → `idea.md` → (heading order of
  `SKILL.md`) `read_foundation.md` → `first_write.md` → `rounds.md`, which ends "step 5 begins" →
  `find_entries.md`, "step 6 begins" → `technology.md` → `settle-technology` → `close.md` → back to
  step 6 → "step 7 begins" → `gate.md`. Stays: every step's text, the four rules. Drops, as
  intended: `delegated_mode.md`, `existing_definition.md`. Drops, not intended: 7.1's routing at
  the hand-back of `close.md` (I-1).
- **Route 3a, a dispatched turn, the delegated mode, step 0 and step 7.** `SKILL.md` → the
  condition is met → `delegated_mode.md` (conversation file, `conversation_template.md`, sources
  and pin; no direct word to the human, no child agent; critique by request; approval only as
  recorded) → rules → step 0: template, "How a skill asks", the definition named by the
  conversation file → `existing_definition.md` (approved: the readiness check; fingerprint mismatch
  → step 7) → the edit → rule "A change ... goes through the gate again" → `gate.md`, whose
  opening routes 7.3-7.5 through the conversation. Stays: every limb of the base's delegated
  section, the resume, step 7. Drops: steps 1-6 unless the edit or a 7.1 finding sends the agent
  there, where the file is named (as settled in question 2).
- **Route 4, an entry of an approved definition reopened, not dispatched, steps 0 and 7.**
  `SKILL.md` → step 0 → `existing_definition.md`: approved → the check; a mismatch or the change
  itself (rule in `SKILL.md`) → step 7 → `gate.md`; a 7.1 finding → the named file of step 4, 5 or
  6. Stays: the resume, the gate, the four rules. Drops: steps 1-6 and the delegated mode. Nothing
  lost.
- **Route 5, a definition with no Technology section, reopened, steps 0, 6, 7.** `SKILL.md` → step
  0 → `existing_definition.md`: say so, ask with the costs; on reopening add `## Technology`
  `TODO`, set the status, "go on at step 6 (`technology.md` beside this file)" → `technology.md` →
  `settle-technology` → `close.md` → back to step 6 → `gate.md`. Stays: the reopening bullet word
  for word, step 6, step 7. Drops, as intended: steps 1-5, the delegated mode. Drops, not
  intended: 7.1's routing at the hand-back of `close.md` (I-1).

## The assessment table against where each fragment stands

Every nonblank line of the base (lines 1-183; blank lines 5, 15, 21, 24, 26, 35, 46, 52, 54, 72,
74, 81, 83, 91, 93, 101, 103, 126, 128, 136, 138, 144, 146, 181) falls in exactly one of the 54
rows: the ranges 1-4, 6-14, 16-20, 22-23, 25, 27-34, 36-40, 41-45, 47-51, 53, 55-56, 57-63, 64-70,
71, 73, 75, 76-77, 78-79, 80, 82, 84-86, 87-89, 90, 92, 94-96, 97-100, 102, 104-105, 106-108, 109,
110-111, 112-113, 114-116, 117, 118, 119-120, 121-122, 123, 124-125, 127, 129-131, 132-133, 134,
135, 137, 139-140, 141-143, 145, 147-151, 152-162, 163-171, 172-176, 177-180, 182-183 cover them
without gap or overlap (checked by hand against `cat -n` of the base). Each row's *New place*
compared with `cat -n` of the new files: `delegated_mode.md` 3-10, 12-16, 17-21, 23-27;
`existing_definition.md` 6-12, 13-20; `idea.md` 5, 6-7, 8-9; `read_foundation.md` 5-7, 8-10, 11;
`first_write.md` 5-7, 8-11; `rounds.md` 5-6, 7, 8-9, 10-11, 12-14, 15, 16-17, 18-19, 20, 21-22;
`find_entries.md` 5-7, 8-9, 10, 11; `technology.md` 5-6, 7-9; `gate.md` items 1-5 at 11-16, 17-27,
28-36, 37-41, 42-45 and the opening at 6-9; `SKILL.md` rules items 1-4 at 33, 34-35, 36-38, 39-40;
headings and step 0's two kept items in `SKILL.md`. All match. The row of `L137` names
`close.md:10-11` as a caller of step 6 but not its hand-back (I-1).

## Checks run

| Check | Command or method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `c0a0f52...`, the head given |
| Scope | `git diff --name-only 2754675..c0a0f52 \| grep -v "^project-level/skill/"` | exit 1 (nothing outside) |
| Description | `git diff 2754675..c0a0f52 -- project-level/skill/SKILL.md \| grep "^[-+]description"` | exit 1 (unchanged) |
| Base identity | `git diff --quiet dfd50e5 2754675 -- project-level/skill/SKILL.md` | exit 0 |
| Entry points | `python -B agent-instructions/skill_entry_points.py` | exit 0, "entry points are current" |
| Foundation | `python -B elements/common/foundation_check.py .` | exit 0, "0 errors" |
| Instruction files | `python -B instruction-files/check_instructions.py . --file <each of the ten files>` | exit 0, `0 error, 1 warn, 14 info` (the warn: root `AGENTS.md`'s private folder, as on the base) |
| Focused tests | `python -B gate/run_tests.py project-level` (background) | exit 0, 271 tests OK |
| Pointers | `python -B .runs/task-cycles/define-project-skill-shape/reports/check_pointers.py` | exit 0, "10 files; 0 failures" (it does not check step 6's hand-back) |
| Counts, author's script | `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/author_report.md` | exit 0, 263 figures, 0 differ; `wc -w` cross-check on 15 files in two locales |
| Counts, mine | `LC_ALL=C.UTF-8 wc -w` on each of the ten files, the base, `definition_template.md`, `conversation_template.md`, `way_of_working.md` lines 20-38 and 52-91, base lines 25-51, 73-125, 145-183, and the proposal's sentence; `LC_ALL=C wc -w` on the base; route sums and percentages by `python -c` | 516, 314, 205, 82, 109, 98, 240, 108, 66, 567 (2305); base 1937 / 1929; 3221; 1419; 208; 503; 314, 540, 495; 31; routes 1786/5718, 1462/4891, 1602/6450, 2305/7153, 1288/4717, 1354/4783; six runs 9482/36235 and 12294/39047 — all equal to the stated figures |
| Em dashes | `grep -o "—"` and `grep -oE "(^\| )—( \|$)"` on the base | 9 and 8 |
| Clauses | `python -B <reports>/review_clauses.py` (mine) | exit 1 by design: 138 clauses, 18 not word for word — the rewordings listed by the author and splitter artefacts (a heading joined to its first bullet); no unexplained loss |
| Callers | `grep -rn "define-project"` across the-way outside the skill and entry points; reading each passage | all step numbers still land; `technology/close.md:10` does not (I-1) |
| Route walks | manual, above | I-1 on routes 1 and 5 (and 2) |

Not run: the whole gate (the orchestrator's), the author's `compare_sentences.py` and
`make_assessment.py` (each rewrites a record file of the author: `compare_sentences.txt`,
`assessment.md`; replaced by `review_clauses.py` and the hand check of the table), and the
`installation` and `agent-instructions` test suites (the change touches neither; entry points
checked directly).

## Foundation selected (WAY-150)

Touched part: `project-level` (files `project-level/**`, `foundations/part_map.md`). Decisions whose
*Scope* names `project-level`: 66 found by a search of `- **Scope:**` lines; read whole those the
change reaches: WAY-256, WAY-265, WAY-112, WAY-118, WAY-156, and WAY-257 (task's *Decisions in
play*); WAY-106, 111, 113, 120, 127, 259 checked by their carried sentences, which stand word for
word in the rebuilt files (clause check). Invariants with *Part* `project-level` or `every`: read
`skill-entry-points`, `project-readiness-gate`, `derived-file-content`; none is changed and no test
was altered. Guidelines: the-way has no `guidelines/` (task question 7); none read.

## Reaches beyond the dispatch

- `project-level/technology/close.md`, `start.md`, `SKILL.md` (grep): to check the hand-backs into
  `define-project` — the source of I-1.
- `elements/common/skill/definition_variant.md`, `elements/common/projected_mode.md`,
  `project-level/plan/skill/read.md`, `project-level/task/skill/read_sources.md`: other callers
  that return to `define-project`, to check they still land (they do, through step 0's resume).
- `project-level/plan/skill/delegated_mode.md`, `critique_plan.md`, `SKILL.md:70-80`: the
  precedent wording of "a turn dispatched through a refinement conversation path" (M-2, criterion 2).
- `elements/common/way_of_working.md` lines 52-91 ("Reading the foundation"): the method of
  selection; and lines 20-38 to recount.
- `foundations/part_map.md` entry `project-level`; `foundations/invariants.md` entries named above.
- the author's private rules on writing scripts: the user's rule read before writing
  `review_clauses.py`.

## Searches not found or unclear

- Where `define-project` "names where" a finding of `close.md` goes, other than 7.1: not found in
  `SKILL.md`, `technology.md` or any file beside them (I-1).
- The task's Context says `SKILL.md` last changed in `4a3ee37`: `git log --follow` gives `e19ee2d`,
  and `4a3ee37` does not touch the file — the author's note holds; no figure depends on it.
- Whether route 3a's step 0 includes `existing_definition.md`: question 4 does not say; the
  author counts it, and the dispatched turn always works on a named definition, so I agree.
- Whether "Once the definition is written (step 3)" could be read by a resuming agent as "once step
  3 ran in this session": unclear in principle; the parenthesis names the step that writes the
  file, and the file exists, so I did not raise it.
