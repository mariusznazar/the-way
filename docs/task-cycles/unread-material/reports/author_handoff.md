# Handoff — the one author of the change

## Delegation

The person who requested this cycle (the-way's author) delegated intermediate choices to the
orchestrator. Nothing here is that person's approval. Your go-ahead is provisional; the human
reviews the pull request.

## Where you work

Worktree (work from its root, edit nowhere else): `the task's worktree`
Branch: `task/unread-material`. Base commit: `02c3d47f8891b66507687b40665b323f3d20def8` (target branch `foundations`).
This is the-way itself, with no `main`: read `agent-instructions/README.md` first for the route.
No other agent writes in this worktree. Commit your work on this branch; commit by path
(`git add <path> ...`), never `git add -A`. Commit messages in English.
Never edit anything outside this worktree. Never touch `.runs/`.

## Your stage and its variant

Method: `task-cycle/change/SKILL.md` (project skill `the-way-make-change`). Your variant, in the
words of its row: **the whole change as the one author**. Read that `SKILL.md` whole, and a file it
names (e.g. `task-cycle/change/slice.md`, `fix.md`, `ui_check.md`) only when the step or variant
that names it comes.

You do the foundation step with your code: read `task-cycle/skill/foundation_step.md` whole and write
the four rows of *Settlements to record* as decisions through the pinned element skill
(`elements/decisions/` — find its `SKILL.md` and follow it), each whole, meaning the row's, wording
yours. You return before the return step and before review; the orchestrator resumes you for the
return step afterwards.

You run focused checks only (the touched directories: `python -B gate/run_tests.py task-cycle`,
`python -B gate/run_tests.py elements/common`, and any other directory your change touches, e.g. a
test of `foundations`). You do **not** run the full gate (`python -B gate/run_tests.py` without
argument); the orchestrator does.

## The task

Frozen task (read whole): `docs/task-cycles/unread-material/task.md`
Source: the author's private task note `the task's note in the author's backlog`, `Status: ready for
cycle`, settlements accepted 2026-11-08. Task language is Polish; write the-way's files in English
as the repository does.

Answers of the orchestrator's step 4:
- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. The task settles where each piece goes. The wording of the new report
  section's heading and sentences is yours to make — name it once and use the same heading in all
  five methods, in the orchestrator's skill and in the request template.
- Reserved choice: none. Route: one author without a plan.
- Lines the task cites for `foundations` @ a3206c1 have moved. Find places by content:
  - the anchor sentence of point 1 stands in `task-cycle/skill/SKILL.md` after "add what it found
    to the handoffs that follow." (also read how that paragraph treats the reports' **Searches not
    found or unclear** and its repair rule, and make the new section follow the same repair rule);
  - WAY-150 is a decision in `foundations/decisions.md` (`### WAY-150 — …`), at about line 4209;
  - the sentence "The whole log is not read." is in "Reading the foundation" in
    `elements/common/way_of_working.md` (step 2), and WAY-150's wording carries the same selection
    to `task-cycle/review/SKILL.md` section "Read" and to `task-cycle/review/whole_change.md` if it
    states how the reviewer reads;
  - the five stage reports: `task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`,
    `task-cycle/plan/SKILL.md`, `task-cycle/spec/design.md`, `task-cycle/spec/review.md`;
  - the request description template is `task-cycle/skill/request_template.md` (its section for the
    human's decisions, the *For you to decide* list; WAY-287). `task-cycle/request_check.py` and
    its test check the description form: if the form check or a test enumerates the items of
    that section, the new item must fit what the check allows, and the change must keep
    `python -B gate/run_tests.py task-cycle` green. If making the item pass the check requires
    changing the script, say so in the report as a question rather than guessing; changing the
    script is in scope only as far as the new item needs.

## What the change must deliver (all four points of *To do*)

1. Dopisek in `task-cycle/skill/SKILL.md`: the exact English text quoted in *To do* point 1,
   placed as the task says. Do not add the dropped last sentence of the older note.
2. A fixed section in the report of each of the five stage methods: what of the handoff — for the
   reviewer of the whole change: of its own selection — stayed unread or was read in part, or
   `none`. Separate from **Searches not found or unclear** (not folded into it: WAY-260 sends that
   section word for word into the process remarks). The orchestrator reads this section in every
   report, and a report without it returns to its agent for repair as a report without
   **Searches not found or unclear** does. Update every place in the orchestrator's skill that
   lists what a report holds or what the orchestrator reads/checks in it (including the line that
   says what is read at status `done`/`PASS`), and the record template if it lists report sections.
   Check `task-cycle/remarks_check.py` still does what it should with the new section next to
   **Searches not found or unclear** (the section must not be read as, or inside, that section).
3. `task-cycle/skill/request_template.md`: one item in the section for the human's decisions,
   beside skipped steps and unrun checks, about the incomplete reading of the reviewer of the whole
   change, with the question whether to merge anyway — present only when the reviewer did not skim
   the rest of its selection by titles, or itself admitted that a decision concerning the change
   stayed unread, and the gap was not closed on the way. Example shape from the task: „The review of
   the whole change read 40 of 151 selected decisions whole; merge anyway?” (write it in the
   template's own language and form: it says the top part is plain words with no file names and no
   identifiers). Keep the template's other statements about that section true (the numbering of
   items, any place that counts or lists the items, `none` semantics under WAY-287).
4. WAY-150 and its carriers: the reviewer of the whole change reads whole the decisions of its
   selection that concern the change's topic, skims the rest of its selection by titles and opens
   every one whose title points to a bearing on the change, and states in its report how many it
   read whole and how many only by title. Change WAY-150 in place (its rule text, *Verification*
   complies/violates, *Rationale*; keep *Rejected* as the task's sources describe it, which stands),
   change `task-cycle/review/SKILL.md` ("Read") and "Reading the foundation" in
   `elements/common/way_of_working.md` so that "The whole log is not read." no longer contradicts
   the reviewer's practice. The title screening applies to decisions only; a guidelines file the
   agent did not read whole goes to the section of point 2 (WAY-213 stays as it is). Screening
   applies to the reviewer of the whole change only; other agents keep reading what their handoff
   names whole.

Settlements to record (decisions): rows 1–4 of *Settlements to record* in the frozen task, each
whole. Row 3 changes WAY-150 (edit in place, WAY-07). Rows 1, 2 and 4 are new decisions — find, by
searching the whole foundation (WAY-33), whether each is already stated by an existing entry
(for example WAY-148, WAY-260, WAY-287); if so, tie the row to it per `foundation_step.md` rather
than writing a second entry. Mark each entry `row <n>` in your report.

## Out of scope

Screening by title for the orchestrator, task refinement, project definition or plan; measuring how
many selected decisions really concerned a change. Do not fix the guideline gaps of the-way
(task `the task about the-way's own guidelines`).

## What you read (the orchestrator's selection)

Whole, by identifier, from `foundations/decisions.md` (each entry from its `###` heading to the
next): WAY-148, WAY-150, WAY-213, WAY-159, WAY-260, WAY-286, WAY-287 (the task's *Decisions in
play*). Also read whole `foundations/part_map.md` entries for `task-cycle`, `elements-common`,
`decisions`. For the rest of the selection — the decisions whose *Scope* names those three parts
and the invariants whose *Part* names them or `every` — select and read as "Reading the foundation"
in `elements/common/way_of_working.md` and the decisions element's skill give; you write
foundation entries, so you select as that skill's step 1 gives. Also read whole each file you edit.
Reach for anything else selectively (a search for an identifier or a word, and the passage found)
and name each reach in your report.

## Your report

Write it to
`docs/task-cycles/unread-material/reports/author_report.md`
as `task-cycle/change/SKILL.md` gives it (checks with command and exit code, reaches beyond the
handoff, **Searches not found or unclear**, the own-work check, one English sentence and one
Polish sentence of the meaning of each foundation entry with its mark). Return: status, commits,
a one-line check result, and the report path.

(There is no "unread" section in the report format yet — it is what you are adding. In your own
report, add a short line stating anything in this handoff you did not read whole.)
