PASS 06144e9713221bbcc680752ed0ba400e75813a34

# Review of the return step's commits: backlog-line-for-plan-tasks

Range `9d5743d7648b4a5095fba28a7d6ab100cd078c3b..06144e9713221bbcc680752ed0ba400e75813a34`, one commit
(`06144e9`), three files: `foundations/decisions.md`, `foundations/part_map.md`,
`project-level/task_line.md`. `git rev-parse HEAD` is `06144e9713221bbcc680752ed0ba400e75813a34`; the
worktree is clean. Diff and log computed by me (`git diff 9d5743d..HEAD`).

Counts: blocking 0, Minor 4 (all within the task, none blocking), out of scope 1.

## What the commit does, and my verdict on each claim to verify

- **WAY-329 (new).** The derivation it records (plan file name without extension, `-`, task name,
  lower case, each run of other characters including hyphens as one `-`, none at either end) matches
  the text of `project-level/task_line.md:35-38` word for word in meaning. I checked its three
  examples by hand: `player-game.md` + `forest-on-hex-grid` gives `player-game-forest-on-hex-grid`;
  `MVP2 plan (v2).md` + `forest-on-hex-grid` gives `mvp2-plan-v2-forest-on-hex-grid`; `a-b.md` + `c`
  and `a.md` + `b-c` both give `a-b-c`. The binding part is two sentences, present tense, no
  normative words. It stands at the end of the log after WAY-328, as the template says a new entry
  goes. Relations derive from WAY-147, WAY-107 and WAY-154, each written in the entry that depends on
  the other.
- **`Based on: none`.** Judged fair, with one remaining doubt put to the human below. The only
  source outside the product the derivation rests on is the task place's rules (the form: lower-case
  letters, digits, `-`; unique in the whole place), which lie in the author's private notes. WAY-27
  lets only the `## Backlog` section of `AGENTS.md` point there, by entry name, so an entry cannot
  quote them as a source or turn them into an environment fact; WAY-107, WAY-27 and WAY-320, which
  rest on the same place, read `none` too, and the rationale of WAY-329 describes the form the rules
  give instead of pointing to them (what WAY-27 asks). WAY-71's *violates* line (`Based on: none`
  "where its source says nothing of what it rests on") could be read against it, because the task's
  *Questions carried to cycle* does name the vault's rulebook; the way out that WAY-71 offers,
  `TODO — <what is missing, with its source>`, would put a private source on the main branch, which
  WAY-27 forbids. I leave this as a judgement the return report already flags, not a finding.
- **`the cycle's` mark.** Correct by `task-cycle/skill/foundation_step.md:19`: no row of *Settlements
  to record* and no projected entry carries the derivation; the task leaves it to the cycle (*Questions
  carried to cycle*). The task does not exclude an entry for it, so `return_step.md`'s exclusion
  clause does not apply, and the derivation binds after the merge (refiners derive it for as long as
  plans are led), so WAY-36's plan test says it belongs in the log.
- ***Rejected* and *Verification* against WAY-134 and the template.** WAY-134's limit (only the ways
  the row's source keeps, no way the writer derives) is written for a decision made from a row; WAY-329
  has no row. Its *Rejected* holds the ways the cycle record (Q1) and the author's report (choice 1)
  record as rejected, each with its reason: the bare plan name, a number counted at line creation, one
  hyphen per character. I found no rule that bars them for a `the cycle's` entry, and the template
  allows prose there. *Rationale* and *Rejected* name no file, script or count. *Verification* carries
  a complies and a violates pair in the template's form. I found no defect here.
- **No entry for choices 2-5 of the author's report.** Fair. Choice 2 is where the rule stands in the
  skills, which no rule binds the product (WAY-154, WAY-107 and WAY-329 hold the rules the file
  carries). Choice 3 (no second line, link the document) is carried by WAY-154's "where none stands".
  Choice 4 is a placement of a duty WAY-154 already holds ("brings the dependencies ... in step").
  Choice 5 (who writes the `task-rules` entry) is carried by WAY-107's "asks the human once and offers
  to add the entry". Each stays a row of the cycle record (Q5-Q8). I could not find a sentence of any
  of them that binds after the merge and is missing from an entry; the one residual gap, a line that
  already exists, is out-of-scope item 1 below.
- **The part-map clause.** A fair statement of the part's responsibility. The `project-level` entry
  stays one sentence (the template's binding part), it already answered for "evidence-backed upkeep
  of task states", and the files of the part (`task_line.md`, `backlog_place.md`, the refiner and
  lead skills) do make a line, give it its dependencies and move it to ready. It names no file, and
  adds no part, so WAY-328's *Scope* is unaffected. The `decisions` entry needs no change (the log is
  still its file).
- **WAY-154 *Verification*.** The extended "complies" example matches the binding part now in the
  log: the line in the first later turn that can, and the orchestrator making the line, already
  ready, where none stands. No contradiction with the "violates" list.
- **WAY-107 and WAY-320 rewraps.** Words unchanged (checked in the diff). See Minor 3 for the
  wrapping.
- **`project-level/task_line.md:41` `(WAY-329)`.** See Minor 2.
- **WAY-27 (unchanged).** Its exception already names the rules of the place beside the place; it
  does not conflict with WAY-329. No glossary entry is needed: "line" and "task place" are used in
  their ordinary meaning, and the word "entry" in the locations-file sense is on the request's list
  already.

## Findings

### Blocking (Critical or Important)

None.

### Minor (within the task, not blocking)

1. **WAY-329's second binding sentence says "another line" without "of another task".**
   `foundations/decisions.md:10895-10898` (binding sentence: "an agent that finds another line
   carrying the identifier it derived writes nothing and asks the human"; the *complies* example
   speaks of a first and a second plan's task). Where the line carrying the identifier is the
   task's own earlier line (a late line, a parked task), `project-level/task_line.md:23-25` says make
   no second line and link the document, with no question; only a line of a different task is the
   clash (`task_line.md:28-29`, which says "another line" right after the own-line bullet). A reader
   of the entry alone would ask the human in the own-line case too. Effect: one needless question, no
   wrong write, so Minor. Evidence: the two texts side by side.
2. **The citation `(WAY-329)` stands on a sentence the entry does not say.**
   `project-level/task_line.md:40-41`: "A task that belongs to no plan has no identifier from the-way;
   a line of it takes one only where the rules require it (WAY-329)." WAY-329 states the derivation
   for "a task of a project plan" and holds nothing about a task of no plan; the derivation sentence,
   `task_line.md:35-38`, is the one WAY-329 says, and it carries no citation. A reader who follows
   the citation finds no support for the sentence it sits on. Effect: a misdirected pointer,
   cosmetic. Put the citation after the derivation sentence.
3. **The rewrap of WAY-320 does not do what the return report says.** The report says the lines were
   "rewrapped" from over 100 columns. `foundations/decisions.md:10532` is now 160 characters (the
   old 250-character line was only split once), and `foundations/decisions.md:10482` is 106;
   `foundations/decisions.md:2491` in WAY-107 is a 62-character line followed by a 101-character one.
   I found no written width rule and `foundation_check.py` passes, so the effect is only that the
   report's claim is not accurate and the diff stays hard to read. Minor. Evidence: line lengths read
   with a short PowerShell loop over the worktree file.
4. **WAY-154 and WAY-107 now hold more than three binding sentences.** The template and WAY-05 say
   one to three (`elements/decisions/template.md:25,104`; `foundations/decisions.md:126`). WAY-154's
   first paragraph now has five sentences (`foundations/decisions.md:4436-4458`; it had three at
   `52f8164`) and WAY-107's has four (`foundations/decisions.md:2437-2448`; three at `52f8164`). The
   foundation step's commit `74fbd01` made them so, outside this range, but the return step corrected
   both entries (it extended WAY-154's *Verification* and rewrapped WAY-107) and so owned reading
   them against the template. WAY-05's reason is that what binds stays short and checkable. No check
   catches it and each sentence is itself concrete, so the effect is a heavier binding part for the
   reader, not a wrong rule: Minor. I graded it Minor within the task rather than blocking because the
   rules the sentences hold are the ones the human accepted, and only their grouping departs from
   the form.

### Out of scope (beyond this dispatch, so counted here and not re-graded)

1. **A task that already has a line gets no identifier from the refiner.** `project-level/task_line.md:23-25`
   (code of the reviewed commits, `9eb2bd6` and `9d5743d`, not this range): where a line already
   stands for the task (for example one made by `/park`), the refiner links the document and writes
   nothing else, so that line carries no `🆔` derived under WAY-329, while a dependent task's line
   names that identifier in `⛔`. If the Tasks plugin treats a `⛔` naming an absent identifier as no
   dependency (my recollection, not checked), the ordering is dropped silently, and the clash check at
   `task_line.md:28-29` cannot see it. WAY-329's text ("the identifier of the line of a task of a
   project plan is ...") reads as if every plan task's line carries it. This is a gap of the reviewed
   code against the new entry, and it lies inside the task (row 5, *Questions carried to cycle*), so
   the orchestrator should decide whether it goes to the human's list; I make no verdict on it as
   blocking because the handoff says the reviewed code is not to be reviewed again.

## Declined to judge

- The code of `9eb2bd6` and `9d5743d` (the skill files, templates, `AGENTS.md`): whole-change review
  `PASS` after one fix; outside the handoff's range. Reported only where the new entry meets it
  (out of scope 1).
- The older word "entry" in `project-level/task/skill/read_sources.md` and the Ready line a task
  returned to refinement keeps: the handoff says they stand on the request's list for the human.
- The three `product-guidelines/*/orchestrated_mode.md` files that still say "edits only the task
  document and its turn" (author concern 2, already routed to the whole-change review): reviewed code,
  not this commit.
- Whether WAY-144's accepted cost (a copy of the dependencies) is right: the human accepted it
  (question 4).

## Checks (command, exit code), all from the worktree root

- `python -B elements/common/foundation_check.py`: exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .`: exit 0, "0 error, 0 warn, 3 info".
- `python -B task-cycle/test_tracked_files_private_paths.py`: exit 0, "Ran 1 test ... OK".
- Manual: `git rev-parse HEAD` (matches the head given), `git status --short` (empty), hand
  evaluation of the derivation on the three examples of WAY-329 (all as the entry says), line lengths
  of `foundations/decisions.md` (Minor 3), sentence count of WAY-154, WAY-107 and WAY-329 against
  `52f8164` (Minor 4).
- Not run, as the handoff says: the `project-level` directory and the full suite.
- A changed invariant test: none in this range.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-05 (the one-to-three sentences rule), read whole: to judge Minor 4.
- `foundations/decisions.md` WAY-147 and WAY-101, read whole: WAY-329 derives from the first, and
  WAY-107 cites the second.
- `elements/part-map/template.md`, `elements/part-map/skill/decide_entry.md` and `write.md`: for the
  form of the `project-level` sentence (one-sentence binding part).
- `project-level/task_line.md`: whole, to compare the derivation, the clash step and the citation.
- `task-cycle/skill/foundation_step.md`: whole, for the `the cycle's` mark.
- `docs/task-cycles/backlog-line-for-plan-tasks/cycle.md`, `reports/author-report.md`,
  `reports/return-handoff.md`: for the ways Q1 and the author recorded as rejected, which WAY-329's
  *Rejected* holds; `reports/whole-review-report.md` and `fix-review-report.md` searched by word only
  (identifier, existing line, three sentences) to see whether Minor 4 and out-of-scope 1 were already
  raised: they were not.
- `git show 52f8164:foundations/decisions.md`: the base wording of WAY-154, WAY-107 and WAY-320, for
  the sentence counts and the rewrap comparison.

## Unread material

- Read whole: WAY-329, WAY-154, WAY-107, WAY-320, WAY-27, WAY-36, WAY-11, WAY-33, WAY-95, WAY-147,
  WAY-101, WAY-05, the glossary, the `project-level` and `decisions` entries of `part_map.md`, the
  return report, the frozen task, `return_step.md`, `foundation_step.md`,
  `elements/decisions/template.md` and `elements/decisions/skill/SKILL.md` with `decide_entry.md`.
- Read in part: WAY-134 (from its heading to the middle of its *Rationale*, about 70 lines; its
  *Rejected* and the end of its *Rationale* not read: I used its binding part and *Verification*, which
  carry the rule on a decision's *Rejected*); WAY-71 (to the start of its *Rejected*; the rest of
  that list not read).
- Not read: WAY-104, WAY-144 (the latter only as quoted in the task), `elements/decisions/examples.md`,
  `elements/common/rules.md`, `elements/decisions/skill/projected.md`, `elements/decisions/skill/read.md`
  (none bears on a `the cycle's` decision of this form).

## Searches not found or unclear

- A written width rule for lines of `foundations/decisions.md` (searched `*.md`, `*.py` and config
  files for column, width and wrap): not found; Minor 3 is therefore about the accuracy of the
  report's claim, not a rule broken.
- A rule for the *Rejected* of a `the cycle's` decision that is not written from a row: not found
  (WAY-134 and the template speak only of a decision written from a row); I took the template's plain
  form as the rule.
- Whether the Tasks plugin reads a `⛔` that names an absent identifier as no dependency: not
  checked (outside the repository); out-of-scope item 1 rests on my recollection.
