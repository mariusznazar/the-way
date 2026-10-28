# Handoff — review of the whole change, task `task-cycle-skills-shape`

You review a change you did not make, as an agent of a the-way task cycle. The person who requested
this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human. You alone grade and scope your findings.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`. Read-only: change no file and commit nothing outside your report.
- **Method:** `review-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/review/SKILL.md`, with every file of the process it names read
  from `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the
  methods of its stage from that copy at the base commit (its To do 7), because this change rebuilds
  those methods — including the one you apply. The foundation, the code and the tests you judge are
  the worktree's.
- **What you review:** the whole change, range `cf11541f039649db3a76aa5aaa2d7cce2cc48f34..7369993885567d683ef7b7a8b08933318c21ed4d`
  (13 commits, 67 files, +523 −329; 42 of the files are generated entry points of one changed line
  each).
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/review-report.md`; its first line
  is `PASS <sha>`, `FAIL <sha>` or `questions`, as your method gives.

## What you read

- The frozen task, whole: `.runs/task-cycles/task-cycle-skills-shape/task.md` (in Polish), with its
  two frozen sources: `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md`
  (the judgment and layout `make-change` follows, To do 5) and
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md`, section „Ustalone”.
- The plan: `.runs/task-cycles/task-cycle-skills-shape/plan.md` (no spec was written). Its section
  "Common to the rebuild slices" binds Slices 7–11.
- You select your own foundation entries and guidelines, by the parts of the change (`task-cycle`,
  `instruction-files`, `agent-instructions`, `decisions`). the-way has no `guidelines/`; the task's
  second question under *Questions to settle* settles the selection as empty.

## Slices, their ranges and their reviews

No slice had a review of its own: no slice was marked with a risk. You judge every slice, and the
plan's *Foundation entries*, and name for each blocking finding the slice it comes from, or none.

| Slice | Range | Class and model | Agent's report |
|---|---|---|---|
| Foundation entries (rows 1–3: WAY-125, WAY-127, WAY-256) | `cf11541..40f0fd3` | same, Opus | `reports/foundation-report.md` |
| 1 — exception in `instruction-files/kind_skill.md` | `40f0fd3..746da1b` | cheaper, Sonnet | `reports/slice1-report.md` |
| 2 — generator's sentence, its test, `AGENTS.md`, 6 entry points | `746da1b..61cc5ab` | cheaper, Sonnet | `reports/slice2-report.md` |
| 3–6 — the other 36 entry points | `61cc5ab..b898353` | cheaper, Sonnet | `reports/slice3-report.md` … `slice6-report.md` |
| 7 — `make-change` | `b898353..9b776fe` | cheaper, Sonnet | `reports/slice7-report.md` |
| 8 — `write-spec` | `9b776fe..bf75d1c` | strongest (= Opus here) | `reports/slice8-report.md` |
| 9 — `plan-task` | `bf75d1c..00d000e` | strongest (= Opus here) | `reports/slice9-report.md` |
| 10 — `review-change` | `00d000e..a2456e5` | strongest (= Opus here) | `reports/slice10-report.md` |
| 11 — `implement-task` | `a2456e5..7369993` | strongest (= Opus here) | `reports/slice11-report.md` |

Report paths are under `.runs/task-cycles/task-cycle-skills-shape/`. The sentence comparisons of
Slices 7–11 lie beside them (`slice<N>-before.txt`, `-after.txt`, `-comm.txt`).

## What the orchestrator's mechanical checks passed on, as information

Each slice passed the mechanical check (clean tree, non-empty range, files within *Change*, each
check with its command and exit code). Mismatches and concerns passed on, with no judgment of them:

- Foundation entries: WAY-125 was written for every file a method names, "one beside that
  `SKILL.md` included", where settlement row 1 speaks of a file beside the skill; the orchestrator
  accepted it from To do 1 ("wszystko, co metoda wymienia") as choice C19. WAY-256's exception is
  bounded to a fragment "which would otherwise stand in a file beside the skill". WAY-125 and
  WAY-127 gained `derives from WAY-256`.
- Slice 2: `AGENTS.md:11–12` leaves a short line in the paragraph's wrapping.
- Slices 2–6: the tracked-entry-points test failed by plan between Slices 2 and 6; after Slice 6
  every entry point is current.
- Slice 7: rows 15 and 19 of the example (the slice insets of sections 3 and 5) kept in `SKILL.md`
  as one-instruction fragments, against the example's layout line; the slice variant reads 1 820
  words against 1 777 before; the dispatches of the plan's foundation entries and of the return step
  fit no row of the variants table (the base had the same gap).
- Slice 8: step 2's pointer adds "or revising it"; "the code the choice depends on" kept in the
  common Read.
- Slice 9: the after-spec sentence kept in `SKILL.md` step 1 under the one-instruction exception;
  two "reword" proposals on `task-cycle/plan/SKILL.md` "*Read* is the whole reading", no edit.
- Slice 10: sections of `review-change` renumbered (old 6 "Report" is 4; the orchestrator's
  `git grep` found no outside citation of the old numbers); report items kept in `SKILL.md`, unlike
  Slice 7; one proposal (the reviewer's return lacks the one-line check result of
  `implement-task`'s handoff paragraph and WAY-148), no edit.
- Slice 11: the pin move and step 9's planned sub-steps stay in `SKILL.md` though one route needs
  them (reasons in its report); a new sentence says a handoff for a dispatch with no row in
  `make-change`'s table names the stage instead; the foundation-step agent now reads an element's
  skill "when it writes an entry of that element", where the base said it reads "the element skills
  it names" with the paragraph, which the executor took as part of the WAY-125 change; pointers use
  full paths `task-cycle/skill/<file>.md`.

## Answers of the orchestrator's start

- Trust boundary: no — no file the part map names as one is changed.
- Irreversible operation: no.
- No spec (no open design choice); planned route.

## What the task asks a reviewer to weigh

Every To do 1–7 and both acceptance criteria, rows 1–3 of *Settlements to record*, and the answers
under *Questions to settle*: in particular that the cycle carried out only "keep" and "move" verdicts
and rewordings that change no meaning, with "remove" and "reword" as proposals (acceptance
criterion 2: no rule disappears or changes meaning beyond To do 1–3), that each fragment moved
beside a skill is named at the step or variant that needs it, and that no Python changed beyond the
generator's sentence and its test's assertion (acceptance criterion 1).

Do not run `gate/run_tests.py` as a whole; the orchestrator runs it. Focused checks are yours to run.
Return your report's first line, the counts of blocking, Minor and out-of-scope findings, a one-line
result of the checks you ran naming what failed or did not run, and the report's path.
