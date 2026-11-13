# Author report — friction-at-source (the whole change, one author)

## Status

`done with concerns` — the concerns are the handoff's non-existent `--check` flag, the tension of the steps with WAY-286 (choice 3) and the
reading of WAY-329 in WAY-354's Rationale; every check that was run passed.

## Commits (branch `task/friction-at-source`, base `6814c6f`)

- `ffeadc7` Give an item for an unrun check that a human can do by hand a fifth part of three to six steps, in WAY-327 and the template of a request's description
- `32f9904` Point at a place to change in a file by a heading or a quotation in a task document, with the line only as a hint, and record it as WAY-353
- `e51d835` Have the review of the foundation ask, for each decision that describes a transitional state, whether a task ends it, and record WAY-354 and the term

The commits carry the author address from the global git configuration of the machine (the private one, as for every repository on
this account); the base commit shows the noreply address. Nothing was pushed.

## Files changed (added / removed lines against the base)

- `foundations/decisions.md` 95 / 8 — WAY-327 edited in place; WAY-353 and WAY-354 added after WAY-352
- `foundations/glossary.md` 6 / 0 — the term `transitional state`
- `task-cycle/skill/request_template.md` 28 / 3
- `project-level/task/template.md` 7 / 0
- `project-level/task/skill/draft.md` 4 / 0
- `project-level/task/skill/final_review.md` 4 / 3
- `foundation-review/weak_points.md` 12 / 0
- `foundation-review/proposals.md` 13 / 1
- `foundation-review/with_the_human.md` 11 / 4
- `foundation-review/SKILL.md` 4 / 4 (body only; the frontmatter description is unchanged)

## Foundation entries written (meaning sentences)

- **WAY-327, edited in place — `row 3`.** English: an item of a request for a check the agent did not run that the human can do by hand has a
  fifth part, three to six steps for the human (where to go, what to do, what to see), with the same three answers as before; the writer
  checks it against that part too. Polish: pozycja opisu prośby o sprawdzeniu, którego agent nie wykonał, a które człowiek może zrobić ręcznie,
  ma piątą część — trzy do sześciu kroków dla człowieka (gdzie wejść, co zrobić, co zobaczyć), z tymi samymi trzema odpowiedziami. Its *Rejected*
  gained the two ways of question 4's *Not chosen* (the separate section of the description; no steps). WAY-286 and WAY-290 are not edited.
- **WAY-353, new — `row 1`.** English: a task document points at a place to change in a file by a heading or a quotation, the line number is only
  a hint, and the *Source* under a question stays as it is, with the line and the revision. Polish: dokument zadania wskazuje miejsce do zmiany
  w pliku nagłówkiem albo cytatem, numer linii jest tylko podpowiedzią, a źródło odpowiedzi pod pytaniem zostaje z linią i rewizją. *Rejected*:
  the script that checks references before the cycle, and no rule (question 2's two ways, with their costs).
- **WAY-354, new — `row 2`.** English: a review of the foundation lists, by reading, the decisions that describe a transitional state, asks the
  human at each whether a task ends it and where none does proposes creating one (WAY-302); an entry carries no field for the task. Polish:
  przegląd fundamentu wypisuje, czytając, decyzje opisujące stan przejściowy, przy każdej pyta człowieka, czy jest zadanie, które ten stan
  kończy, a gdy nie ma, proponuje jego założenie; wpis decyzji nie ma pola na zadanie. *Rejected*: the field in the entry, the question at
  refinement, no rule (question 3's three ways). Scope `decisions, foundation-review` (mirrors WAY-24, which also says the entry holds no field);
  relations `derives from WAY-24 · derives from WAY-302`.
- **Glossary `transitional state` — `row 4`.** English: a state of a product that a decision describes until work later than the change that
  brings the decision ends it. Polish: stan produktu, który decyzja opisuje do czasu, aż skończy go praca późniejsza niż zmiana wnosząca tę decyzję.
  *Not* reads `none`.

### What the glossary skill gave about row 4 (WAY-95)

I put the term through `elements/glossary/template.md` ("Which words take an entry") and `decide_entry.md`. A search of the English text of the
tracked files for `transitional` and `transition` found no use of the term; `transition` appears in WAY-36 ("a transition between two states", a
piece of work that stays in a plan) and in two lead-skill files in another sense. The term is narrower than its field's meaning: a reader taking
"transitional" as any temporary state would read the review sentence of WAY-354 as covering ordinary rules with "until" and states that end with
their own change, which WAY-36 keeps out of the log. That is the case the template admits for a word used more narrowly (a sentence read wrongly
under the field's meaning), so the entry stands. The row's own wording and the skill agree; the row's example (a shared control with two forms
until the last screen moves to React) is not in the entry, because the template's entry holds one definition sentence and `Not`; the example
stands in WAY-354's verification, made generic ("a new library"). No conflict to settle.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` (after the entries, before commit) | 0, `0 errors` |
| `python -B elements/common/foundation_check.py` (on the committed tree) | 0, `0 errors` |
| `python -B agent-instructions/skill_entry_points.py --check` | 2 — the script has no `--check` (only `--write`); a mismatch of the handoff, see below |
| `python -B agent-instructions/skill_entry_points.py` (no argument) | 0, `entry points are current`; no skill description changed, so `--write` was not needed |
| `python -B gate/run_tests.py task-cycle` | 0, 365 tests OK (includes `TemplateTest` of the template's skeleton and example, and `test_tracked_files_private_paths`) |
| `python -B task-cycle/private_paths_check.py <file>` on each of the 10 changed files | 0 for each |
| `python -B gate/run_tests.py project-level` | 0, 275 tests OK |
| own-work check (below) | 0, `problems: []` |

Not run: the whole gate (`python -B gate/run_tests.py` without a directory), as the handoff says. `foundation-review/` has no tests. The tests of
`elements/common`, `agent-instructions` and the other directories were not run: no file of theirs changed.

### Project-level run

`python -B gate/run_tests.py project-level`: exit 0, 275 tests OK (run on the working tree that the three commits then recorded unchanged).

## Own-work check (WAY-164)

- Requirement most likely missed: the form check (WAY-290) and the skeleton (WAY-286) stay as they are, and a description that carries the new
  fifth part — numbered steps nested under an item of *Fix or let through* — must still pass the form check.
- Check: `a throwaway script in the session's scratchpad`, run as
  `python -B <that script> .` from the worktree root. It takes the new example item of the template, puts it in the three groups of the
  `VALID` description of `task-cycle/test_request_check.py` and runs `Checked(description, POLISH_TASK)`. Result: `problems: []`, exit 0.
- A second check of the same requirement: `TemplateTest` in the `task-cycle` run (the skeleton's headings and the one example of the decision
  section) passes; the new example block starts with `1. The new page...`, so it is not counted as a second example of the section.

## Choices made, with the way rejected and its cost if wrong

1. **Where the steps' rule stands in the request template:** a bullet in "What an item carries" plus a sentence in kind 4 and in step 2 of
   "Write, check, publish". Rejected: a new section of the template (the task's *Not chosen*). Cost if wrong: none beyond wording.
2. **An added second example in the request template** (an item with three steps, after the existing "good item"). Rejected: leaving the form
   without an example. Cost if wrong: one more example to keep in step; it is outside the fenced skeleton and cannot break the form test.
3. **The tension of the steps with WAY-286** (the top part holds no file names): I wrote that the steps carry no file name and no identifier
   of an entry, and that where the way to a place is a file, the step describes the place and the item ends with its pointer to the lower part,
   as other items do. This is my wording of how the two rules meet, not a text of the row. Cost if wrong: the writer of a description may meet a
   check that can only be done by running a file's command; the orchestrator should say if steps may name a command.
4. **The task-document rule stands in three places:** the last paragraph of `project-level/task/template.md` (the rule), `draft.md` (writing),
   `final_review.md` (the readiness check list gained one clause). The task names "the file or files where the rule belongs"; the clause in
   `final_review.md` is my addition. Rejected: the rule in `resolve_gaps.md`. Cost if wrong: one clause to remove.
5. **WAY-354 sits in `weak_points.md` / `proposals.md` / `with_the_human.md` and the body of `SKILL.md`** (steps 2 and 6), as items 2 of the
   order of going through the list (the existing items 2 and 3 became 3 and 4). The glossary entry is appended at the end of the file, like the
   latest entries. Rejected: a new file in `foundation-review/` (it would need a part-map check; none needed now).
6. **WAY-354 Rationale carries no counts** of decisions with "until" (the template allows a measurement only with its conditions and bars
   counts of the foundation's entries); it says "mostly in ordinary rules" and dates the search. WAY-353 Rationale does carry the register
   numbers of 2026-11-12 (80 rows, 45 of 83 cycles, costs), since the choice rests on that measurement. Cost if wrong: a reviewer may want the
   numbers of the search in WAY-354 too.
7. **Three commits instead of one**, one for each of rows 3, 1 and 2 plus 4; `foundations/decisions.md` was staged from prepared intermediate
   states so that each commit holds only its own decision. The foundation check passes on the last commit only (an earlier commit holds files
   that name WAY-354 only after the third); the base-to-tip tree is what the gate reads.

## Search of the whole foundation (WAY-33)

Searched `foundations/*.md` for: `four parts`, `these four`, `WAY-327`, `line number`, `file:line`, `transitional`, `transition`, `until` in the
decisions that speak about the review, `review of the foundation`, `review-foundation`, `foundation review`, `Questions to settle`,
`quotation`. Found and judged:

- Other users of "the four parts": only `task-cycle/skill/request_template.md` (corrected); no other file names them.
- WAY-24, WAY-302, WAY-305, WAY-303, WAY-301, WAY-304: none says the review does only what it lists; no correction needed (WAY-354 derives
  from WAY-24 and WAY-302 and adds a kind of proposal).
- WAY-36 ("a transition between two states"): a different word and a different thing (a piece of work); no correction; WAY-354 refers to it.
- No existing decision answered how a task document points at a file (WAY-353 is a new question); `Source: file:line and revision` stays in
  the template as it was.
- Part map: `foundation-review` and `task-cycle`/`project-level` descriptions stay true; no file was added or moved, so the part map needs no
  assignment (the return step has nothing to assign from this change).
- Invariants read by *Part* (`every`, `project-level`, `task-cycle`, `decisions`, `glossary`): none is altered. `skill-entry-points` holds
  (no description changed); `tracked-file-private-paths` passes in the `task-cycle` run.

## Reach beyond the dispatch

- `foundations/invariants.md`: ran a search by *Part* and read the invariants the handoff selected by name only in part (the entries of
  `foundation-file-kinds`, `foundation-change-merge-route`, `repository-file-location`, `return-step-record`, `derived-file-content`,
  `tracked-file-private-paths`, `skill-rule-source`, `skill-entry-points`); the rest of the list was found by title only. See Unread material.
- `elements/common/foundation_check.py` and `task-cycle/test_request_check.py` (lines 160-264, 541-560, 898-960) read in part, to design the
  own-work check and to see that the template's skeleton and example are tested.
- `foundation-review/remarks.md` lines 8-20 read, to see how the review treats the remarks, before placing the new order item.
- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/glossary/template.md` and both
  element skills with their `read.md`/`decide_entry.md`/`write.md`: read whole, as the skills of the elements give.
- `agent-instructions/README.md` lines 1-80 read (the route for the-way itself).

## Unread material

- WAY-282, WAY-310, WAY-311, WAY-312: read whole (they bear little on the files changed; no finding from them).
- Decisions named in the handoff: all of WAY-327, WAY-286, WAY-287, WAY-289, WAY-290, WAY-24, WAY-302, WAY-305, WAY-36, WAY-37, WAY-01,
  WAY-301, WAY-303, WAY-113, WAY-114, WAY-124, WAY-134, WAY-308, WAY-309, WAY-320 read whole; WAY-282, WAY-310, WAY-311, WAY-312 also.
- Invariants: the whole `foundations/invariants.md` was not read; read whole the eight entries listed above; the others whose *Part* names a
  touched part were listed by title (`project-definition-form`, `project-readiness-gate`, `project-technology-record`, `project-plan-form`,
  `project-plan-check`, `project-plan-state-evidence`, `project-plan-state-subprocesses`, `record-copy-image-check`, `record-copy-image-files`
  and the script and test-method ones). The change touches none of their subjects.
- `project-level/task/skill/`: read whole `SKILL.md`, `draft.md`, `read_sources.md`, `resolve_gaps.md`, `final_review.md`; not read:
  `carry_foundation.md`, `find_settlements.md`, `guideline_findings.md`, `orchestrated_mode.md`, `project_plan_task.md`,
  `source_only_task.md` (searched only, for `line number`, `file:line`, `revision`).
- `foundation-review/remarks.md`: lines 8-20 only; `foundations/environment_facts.md`: not read (no entry of it is touched).
- The part map and the glossary: read whole.
- `task-cycle/skill/request_template.md`, `project-level/task/template.md`, `foundation-review/{SKILL,weak_points,proposals,with_the_human}.md`,
  `draft.md`, `final_review.md`: each read whole before the change.

## Searches not found or unclear

- `python -B agent-instructions/skill_entry_points.py --check`, named in the handoff, does not exist (error exit 2); the script takes `--write`
  or no argument (no argument checks). I used the no-argument form.
- The handoff names the next free number WAY-353; the log's last entry before the change was WAY-352 and no withdrawn number is 353 or 354 —
  confirmed.
- The task document's *Context* names WAY-329 as the reason a task outside a plan has no identifier an entry could name; WAY-329 derives only
  the identifier of a plan task's line, so WAY-354's Rationale says "an identifier that an entry could name exists only for a task of a project
  plan (WAY-329)" — a reading, not a quotation. A reviewer may want that sentence tightened.
- The task's row 1 says the rule covers "the template and the skill"; no single file of the skill is named, so I chose `draft.md` and
  `final_review.md` (choice 4).

## Problems and mismatches observed

- Handoff mismatch: `skill_entry_points.py --check` (above).
- `foundations/part_map.md`: no assignment needed; no file added or moved.
- Not mine, for the orchestrator: the note that the-way tells the author to name "the steps for the human" without a file name (WAY-286) while
  a check by hand often starts from a file or a command — see choice 3.
