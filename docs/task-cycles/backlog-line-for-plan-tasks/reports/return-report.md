# Return report: backlog-line-for-plan-tasks

**Status:** done. One commit: `06144e9` (on top of `9d5743d`; explicit paths:
`foundations/decisions.md`, `foundations/part_map.md`, `project-level/task_line.md`). Tree clean.

## Compared with the files, and corrected

| Entry or map part | What no longer matched | Correction |
|---|---|---|
| WAY-154 | The *Verification* "complies" example named only the first turn and the orchestrator's move of a line; the files (after the fix) also make a line in the first later turn that can, and make it, already ready, at acceptance where none stands (review of the fix, Minor) | example extended in `decisions.md` (WAY-154 *Verification*) |
| WAY-107 | one wrapped line over 100 columns (review of the fix, Minor) | rewrapped; no meaning changed |
| WAY-320 | one wrapped line (the `Rejected` "one entry shared by all products") and one in the binding part, both over 100 columns | rewrapped; no meaning changed |
| WAY-27 | none: its binding sentence, complies example and rationale already name the rules entry beside the place of the tasks, and `AGENTS.md` names both | none |
| WAY-144, WAY-147, WAY-328 (compare only) | none. WAY-144: the plan gains no field; the dependencies on lines are the copy the task accepted, and WAY-154's rationale says so. WAY-147: a line still links its document and its identifier is built from the plan task's name. WAY-328: no part added | none |
| Part map, `project-level` | its sentence did not say the part answers for how a task's line is made, given dependencies and moved to ready, although `project-level/task_line.md` and four skill files of the part now do | clause added in `foundations/part_map.md` |
| Part map, `decisions`, `agent-instructions`, `product-guidelines` | `decisions`: the log is its file, no change of responsibility. `agent-instructions`: `AGENTS.md` still the root file, `## Backlog` names the new entry. `product-guidelines`: three skill files changed by one sentence each, its responsibility unchanged | none |
| `project-level/task_line.md` (not an entry) | the identifier paragraph had no citation of the entry now written | `(WAY-329)` added |

The older word "entry" one paragraph above the "line" in `project-level/task/skill/read_sources.md`
(a review Minor of the fix, on the request's list) I left: a review finding is no foundation entry
(`return_step.md`), and the sentence is older text of a reviewed file.

## Entries written or changed

- **Decisions:** one written, **WAY-329** — "How is the identifier of a project task's line in the
  backlog derived?". Marked `the cycle's` (no row carries it): the task leaves the derivation to the
  cycle (*Questions carried to cycle*). WAY-154, WAY-107, WAY-320 changed by the foundation step
  (rows 1, 2, 5; rows 3, 4; row 4), WAY-27 (the cycle's), all in place and corrected above.
  - EN: A refiner computes the identifier of a plan task's line from the plan's file name and the
    task's plan name, in lower case, runs of other characters (hyphens included) as one `-`, so that
    it can write it in another task's dependency before that line exists; it is unambiguous only
    while plan file names differ and no two pairs join alike, and an agent that finds the identifier
    already carried writes nothing and asks the human.
  - PL: Refiner liczy identyfikator linii zadania z planu z nazwy pliku planu i nazwy zadania w
    planie, małymi literami, ciągi innych znaków (także `-`) jako jedno `-`, żeby móc wpisać go w
    zależność innego zadania, zanim jego linia powstanie; jest jednoznaczny tylko, gdy nazwy plików
    planów różnią się i żadne dwie pary nie sklejają się tak samo, a agent, który znajdzie
    identyfikator już zajęty, nic nie pisze i pyta człowieka.
  - WAY-329 *Rejected* holds the ways recorded in the cycle record (Q1: the bare plan name, a number
    counted at line creation) and the one-hyphen-per-character form from the author's own check; its
    *Based on* is `none` (the form the task place's rules give is theirs, WAY-107; the entry does not
    quote them).
- **Invariants, environment facts, glossary terms, projected entries:** none each. No invariant:
  the derivation is a rule of a decision, no test reaches it, and "behaviour merely because no
  invariant covers it" is not written. No environment fact: the rules of the task place lie in the
  author's private notes, which no file here may quote (WAY-27, WAY-320). No glossary term: "line"
  and "task place" are used in the field's meaning (WAY-95); the review's Minor 6 on "entry" is the
  request's list, not an entry.
- **Part-map changes:** one, the `project-level` sentence above. No part added, so WAY-328's *Scope*
  is unchanged.
- **Settlement rows (foundation step):**
  - row 1 → WAY-154 (refiner writes what the order asks; nobody but the orchestrator, on the human's
    word, takes the step of acceptance; plan, definition, foundation stay outside);
  - row 2 → WAY-154 (line made in the first turn that creates the document, in parallel, no queue;
    the orchestrator moves it to ready with the Status and the plan's row);
  - row 3 → WAY-107 (forms from the rules of the task place, never from the product or the-way's
    skills);
  - row 4 → WAY-107 (the entry `task-rules`, the section names it, ask once and offer the entry) and
    WAY-320 (the entry name beside `tasks` and `projects`; the shared entry as a rejected way);
  - row 5 → WAY-154 (dependencies from the plan's *Depends on* on the line; refiner writes, the
    orchestrator keeps them in step; the copy's cost accepted).

## Choices of the cycle that may bind after the merge (WAY-36)

- **Q1, the derivation of the identifier** (with my choice 1 and the fix's assumptions): an entry,
  WAY-329. It binds after the merge (refiners derive it for as long as plans are led; written lines
  carry it) and the task does not exclude an entry for it.
- **Choice 2, the new file `project-level/task_line.md`:** stays a row of the questions table.
  It is where a rule stands in the skills, not a rule that binds the product, and WAY-154, WAY-107
  and WAY-329 hold the rules the file carries.
- **Choice 3, a task with an existing line** (make no second, link the document, leave the status as
  the rules give): stays a row. WAY-154's "where none stands" already carries "no second line", and
  "the status as the rules give" adds nothing the rules do not hold.
- **Choice 4, the orchestrator's correction of dependencies in `route_changes.md`:** stays a row.
  WAY-154 holds the duty ("when the plan's dependencies change"); the file it stands in is a layout
  choice.
- **Choice 5, a refiner writing the `task-rules` entry after the human's agreement:** stays a row.
  WAY-107 already says the agent asks and offers to record the entry, and `backlog_place.md` gives
  the rule that it writes it only on agreement; the refiner as the writer is a routing detail.
- **The fallback of B1 (a line made late; made ready by the orchestrator where none stands):** an
  entry, already in WAY-154's binding sentence and, now, its example. No second entry.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors" (after the last edit).
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 3 info".
- `python -B task-cycle/test_tracked_files_private_paths.py` — exit 0, OK.
- Not run, as the handoff says: the `project-level` directory and the full gate.
- No failing run of a test written first exists: I wrote no test and no invariant.

## Own-work check

- Requirement most likely not met: that rows 1 to 5 are each made true by an entry and by skill text.
  Check: `grep -c "task-rules"` over `decisions.md` (4), `AGENTS.md` (1), `backlog_place.md` (2), each
  exit 0; the rows' meanings stand in WAY-154, WAY-107 and WAY-320 as listed above, read after the
  edits. It showed no row missing. The check is reading, not a test.
- Second check: `grep -n "WAY-329"` finds the decision (`decisions.md:10891`) and the one citation in
  `project-level/task_line.md:41`; no other file names an identifier that WAY-329 would have to be
  tied to.

## Unread material

- `foundations/decisions.md`: WAY-11, WAY-36, WAY-95 read whole; WAY-33 (the search rule) not
  re-read for this step. `elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md` and the
  head of `template.md` read; the rest of the template, its "Assigning files", not read.
- `reports/whole-review-report.md`, `fix-review-report.md`: not read; the handoff's own text, the
  fix report and `cycle.md` gave what the step needed.
- All else the handoff names, whole.

## Searches not found or unclear

- Where "the choices of its cycle record" for a choice that stays a row are written: the cycle record's
  questions table (`cycle.md`) is the orchestrator's, so I name the rows (choices 2 to 5) here and
  leave their entry in that table to the orchestrator.
- Whether `Based on: none` is right for WAY-329, since the form the task place requires is a source
  outside the product that I cannot quote: unclear; I chose `none` and a rationale that points to
  WAY-107 and does not repeat the rules. The human may prefer `TODO — ...` (WAY-71) at the request.

## Reach beyond the handoff

- `project-level/task_line.md`: the one citation `(WAY-329)`; a reviewed file, so noted.
- `foundations/part_map.md`: `project-level` sentence (above).
