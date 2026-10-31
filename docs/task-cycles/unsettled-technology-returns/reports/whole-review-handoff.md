# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. You made
none of this change.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Review is read-only: you change no file of the repository and make no commit. You run no gate;
  that run is the orchestrator's. Your report:
  `.runs/task-cycles/unsettled-technology-returns/reports/whole-review.md`

## Your method

Read `task-cycle/review/SKILL.md` whole and follow it, as the review of the whole change, and read a
file it names when the step that names it comes. Your report's first line is `PASS <sha>`, `FAIL
<sha>` or `questions`.

## The range

`2dbf1e7..e21d286` on `task/unsettled-technology-returns`, base `2dbf1e7` of `foundations`. No
slice had a review of its own, so you judge every slice, and for each blocking finding you name the
slice it comes from, or that it comes from none.

| Slice | Range | Class | Report |
|---|---|---|---|
| Foundation entries | `2dbf1e7..443442f` | same | `reports/foundation.md` |
| 1 | `443442f..6fb58f6` | same | `reports/slice-1.md` |
| 2 | `6fb58f6..c2c2479` | cheaper | `reports/slice-2.md` |
| 3 | `c2c2479..9c06170` | cheaper | `reports/slice-3.md` |
| 4 | `9c06170..dc13d6a` | cheaper | `reports/slice-4.md` |
| 5 | `dc13d6a..db126f6` | same | `reports/slice-5.md` |
| 6 | `db126f6..e21d286` | cheaper | `reports/slice-6.md` |

Each report path is relative to `.runs/task-cycles/unsettled-technology-returns/`. The foundation's
entries and slices 1 to 6 passed the orchestrator's mechanical check with no mismatch. `task-cycle/spec/SKILL.md`
stands in slice 4's *Change* and was left unchanged, as the plan allows.

## What you review against

- Frozen task, read it whole: `.runs/task-cycles/unsettled-technology-returns/task.md`. Check
  coverage of every *To do* item, every question's answer and every row of *Settlements to record*.
  It carries no projected entry. Its citations stand at `00c0a74`; the base differs only in one
  paragraph of `task-cycle/skill/SKILL.md`.
- Reviewed spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`, whose decision 4 holds the
  orchestrator's settlement of finding 10 of the spec's review.
- Plan: `.runs/task-cycles/unsettled-technology-returns/plan.md`, with its *Foundation entries* and
  *Coverage*.
- You select your own foundation and guidelines by the parts of the change. The-way has no directory
  `guidelines/`.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes; check that it stays so.
- Operation that cannot be undone: no.

## What the authors raised

These come from the authors' reports, for your reading; they name no finding and grade nothing.

- The agent of the foundation entries: WAY-266 records `narrows WAY-114`, a precedence the spec does
  not name; and it read WAY-160 as not reaching a blocked draft with no code, which one clause in
  WAY-267's *Rationale* states.
- Slice 1: `project-level/technology/settle.md` sub-step 1 gives the research agent the binding
  sentences of each decision the list names `held by`; a choice the human opened stands `— open`
  with that decision nested under it, so the sentences are not among what the leader gives.
- Slice 5: the sentence at `task-cycle/record_template.md:89-90` and step 12 keep "immediately
  after" while the request opens between the two commits for a reserved choice;
  `reserved_return.md` states the departure itself. Its report's *Choices made* gives two choices on
  what "that correction's commits" takes in and on what a stop after a reviewed spec names as not
  run.

## Reporting

Write your full report to the path above as your method gives it, with each check's command and exit
code, and **Searches not found or unclear** — each thing looked for and not found or unclear, or
`none`. Return your report's first line, a one-line check result naming what failed or did not run,
and the report's path.
