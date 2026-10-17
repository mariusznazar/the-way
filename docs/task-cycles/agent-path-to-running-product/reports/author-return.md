# Author report — return step (turn 4)

Status: **done — no foundation entry written, no commit.** One question goes to the human through
the request (part-map failure mode, WAY-46). Author: the same general-purpose subagent as turns
1–3 (claude-opus-5-5). Worktree at `0c1dfd5`; target tip `origin/foundations` refetched, still
`77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988`.

## Inputs read

- Handoff `reports/author-return-handoff.md`; `task-cycle/skill/SKILL.md` step 11 (return step);
  "Reading the foundation" in `elements/common/way_of_working.md` (read whole in turn 1, reapplied).
- `elements/part-map/skill/SKILL.md` whole and the failure-mode rules of
  `elements/part-map/template.md` (lines 40–50, 160–200) — the only element whose entry was
  considered; no other kind was written, so no other element skill was opened.
- Diff `77c8a8b..0c1dfd5` (13 files, +602/−58: my commits `596a660`, `c657b2b`, `0c1dfd5`; the
  sentence agent's `4c251dc`; the check agent's `8720107`); cycle record choices C1–C12;
  `reports/review.md` (Minor 1–3, *Declined to judge*) and `reports/review-fix.md` (verdict Yes).
- Frozen task rows 1–6; the task is independent, so its sources carry no projected entries (WAY-126
  has nothing to apply).

## Selection refresh

The real diff touches files of `project-level` (template, five skills, `readiness_check.py`, three
test files and one new test file), `decisions` (`foundations/decisions.md`) and `invariants`
(`foundations/invariants.md`). The two foundation files collect entries, so their touched parts
follow from the entries changed (WAY-44): WAY-121, WAY-122, WAY-123, WAY-165 (*Scope*
`project-level, decisions`) and `project-technology-record` (*Part* `project-level`). Touched parts:
**project-level**, **decisions** — the same as in turn 1. The complete *Scope* inspection of turn 1
(96 matches, all read whole; [foundation-selection.md](foundation-selection.md)) still holds: the
foundation changed since only by this branch's own entries (WAY-121 edited, WAY-165 added,
`project-technology-record` rewritten), and the target tip has not moved. Added to the read set:
`project-technology-record/1` as now written (`foundations/invariants.md:2021-2029`), read whole.
Invariants reached through methods naming changed files: the seven `project-level` invariants
(method `gate/run_tests.py project-level`), all passing in the fix run
([fix-tests-project-level.txt](fix-tests-project-level.txt)).

## Candidates found and how each was classified

| # | Candidate (where) | Classification | Requirement or reason; covering test or description |
|---|---|---|---|
| 1 | The readiness check rejects a definition, approved or not, lacking a choice item beginning with `logs:`, `interface:`, `development data:` (`readiness_check.py`) | **Covered by an invariant** — `project-technology-record/1` (rewritten in `4c251dc`) | WAY-121 rows 1, 4, 5; checks `TechnologyMarks`, `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not` in `project-level/test_readiness_check.py` |
| 2 | One finding per missing mark, at the section heading line, with its message (`readiness_check.py`) | Replaceable detail | No requirement fixes how a missing mark is reported; a later change of wording or grouping breaks no rule. Ordinary test `MissingMarks.test_each_missing_mark_is_a_finding_of_its_own_naming_it` in `project-level/test_readiness_marks.py`; description of the change (commit `c657b2b`) |
| 3 | A section reading `TODO` gives one gap and no mark finding; a section reading `none` keeps its one finding (C12) | Replaceable detail | Both sections are rejected either way, so adding mark findings would violate nothing; it would only add noise. Ordinary tests `test_a_section_still_reading_todo_gives_no_mark_finding`, `test_a_section_reading_none_gives_its_one_finding`, and the uncited `Technology.test_a_section_still_reading_todo_is_one_gap_and_no_g` |
| 4 | Marks matched case-sensitively, after the `- ` marker on the item's own first line; nested items, continuation lines, prose and other sections do not count | **Covered by the invariant** (its sentence quotes the literal marks and "choice item … text begins with") | `TechnologyMarks` case, colon, position, continuation, nested, prose, other-section checks |
| 5 | Lenient forms: two spaces after the dash, no space after the colon, a mark with no name (review *Declined*) | Replaceable detail | WAY-121 asks for a name in the definition's language, but the step's agent writes the items; tightening or loosening the form breaks no rule. `test_a_definition_holding_all_three_marks_is_not_rejected_for_them` (no-space form); description of the change |
| 6 | A line inside a fenced block in `## Technology` counts as an item (review Minor 3) | Replaceable detail, pre-existing parser behaviour | Not changed by this task; listed by the review for the request |
| 7 | An approved definition written before the three were required is stopped for them alone and, once they are added, by its fingerprint (`e`) | **Covered** — the invariant (approved or not) plus WAY-118's `project-readiness-gate` route | Ordinary tests `ApprovedBefore` in `test_readiness_marks.py`; manual plan-state check [implementation-weakest-plan-state.txt](implementation-weakest-plan-state.txt) |
| 8 | Skill routes: `settle-technology` step 0 adds missing marked items as `— open`; `define-project` step 0 sends an approved definition lacking them, or lacking the section, to steps 6 and 7 and a plan recheck; `refine-task`, `plan-project`, `lead-project` name the finding and route it | **Covered by WAY-121** (level 2) — no new rule | Carried question (c) follows from rows 1 and 5 with no meaning left open (cycle record); a skill's step order is no foundation entry (WAY-35, WAY-36). Review Minor 2 (adding as open without first looking for a decision that holds them) goes to the request's list |
| 9 | Template rules: the table of marks with what each asks; "a mark in a nested item marks nothing"; WAY-165's rule beside WAY-137's | **Covered by WAY-121, WAY-165, WAY-112** — the template cites them | `project-level/definition_template.md` § Technology |
| 10 | C6 — the exact marks `logs:`, `interface:`, `development data:` | Binds after the merge, **already in the foundation**: the invariant's sentence quotes them; WAY-121 binds "marked in English", WAY-108 keeps markers English; the form lives in the template (WAY-35) | No new entry |
| 11 | C7 — a second item with the same mark is not stopped | Permissive absence of a rule; nothing to bind | Choice-table line only |
| 12 | C8, C9 — wording of row 5, place of row 6 | Already written (WAY-121, WAY-165) | — |
| 13 | C1–C5, C10–C12 | End with the work (integration route, version pin of the cycle, route, branch, order of authors, fixture handling, rulings on concerns) — WAY-36 | Choice-table lines only |
| 14 | Words: "mark"/"marked" (WAY-121, template), "marker" (template end markers), "running product", "logs", "interface", "development data" | No glossary entry (WAY-95) | Each keeps the meaning a reader of the field gives it; "mark" is used plainly across the log (e.g. WAY-46/49 "marked", WAY-54's "marks" of a value's source — a label in each use); the project-level template is outside WAY-95's set of files. "surface" not used for the interface |
| 15 | Environment facts | None | The change rests on no fact about the world |
| 16 | Part-map failure modes of `project-level` | **Question for the human** (WAY-46) — below | — |

Comparison of the touched parts with the code: `project-level`'s responsibility sentence ("the form
and writing of a project definition, its readiness gate, … the refinement of a task …") still
covers every changed file; its files pattern `project-level/**` claims the new test file; its trust
boundary `project-level/readiness_check.py` is unchanged as a pattern; *Depends on* is unchanged (no
new import). The failure-mode list is the one place the map no longer says what the gate catches.

## Rows 1–6 → entries (WAY-134)

| Row | Entry | Still holds against the final code |
|---|---|---|
| 1 | WAY-121/1, second binding sentence | yes — template, `settle-technology` step 1, readiness check |
| 2 | WAY-165/1, first binding sentence | yes — template table of marks; `settle-technology` 2.1 |
| 3 | WAY-165/1, second binding sentence | yes — template table of marks |
| 4 | WAY-121/1, third binding sentence | yes — readiness check, invariant |
| 5 | WAY-121/1, third binding sentence | yes — both modes of the check; `define-project`, `refine-task`, `plan-project`, `lead-project` routes; `ApprovedBefore` |
| 6 | WAY-165/1, third binding sentence (narrows WAY-137) | yes — template rule after WAY-137's; `settle-technology` 2.3 and 2.5 |

No row was missed; no entry written in this step.

## Entries written or changed

None. (WAY-121, WAY-165, WAY-122/123 and `project-technology-record` keep their meaning sentences
from turn 1 and the sentence agent's report.)

## Question for the human (through the request)

**Part map, `project-level`, failure modes.** Today the map says: "a technology choice the project
needs is missing from the definition's list — the first task chooses it — high — not detected".
Since this change the readiness check catches the case for three choices (logs, interface,
development data), and nothing in the map says so. Failure modes are the human's to record
(WAY-46, `update-part-map` step 3), so no entry is written.

- **A (recommended):** add a failure mode at `project-level`: "a definition reaches the breakdown,
  or a task's refinement, without one of the three choices of how an agent reaches the running
  product — the task cycle cannot check behaviour in the running product, or its agent improvises
  a way to it — high — detected by project-technology-record"; keep the existing line, which still
  holds for every other choice. Cost: one line; the part's criticality stays high (computed); the
  format guard checks that the named invariant names `project-level`.
- **B:** leave the map as it is. Cost: nothing now; the map understates what the gate catches, and
  whoever asks which failures go undetected reads the three choices as undetected.
- **C:** reword the existing line to exclude the three. Cost: the line becomes harder to read and
  the three's own damage (no way to the running product) goes unrecorded.

If the human takes A, the line is written by `update-part-map` in the same request (a part-map
change, assessed with the rest of the foundation change).

## Second whole-foundation search (WAY-33) against `77c8a8b`

- Domain: all five elements (`decisions.md`, `invariants.md`, `glossary.md`, `part_map.md`,
  `environment_facts.md`) as they stand on the branch, against the target tip `77c8a8b`
  (refetched; unchanged since the first search, so no other merged change can collide); plus the
  fingerprints of WAY-121 and WAY-165 across the repository.
- Terms: `logs:`, `interface:`, `development data:`, mark/marked/marks, marker/markers, readiness
  check, moves the pin / commit of the-way it pins, running product, can use / works with, test
  environment / production, Technology section / list of technology — output
  [return-search.txt](return-search.txt); the first search's terms (turn 1) re-read where the final
  text changed.
- Findings, each read whole:
  1. `project-readiness-gate/1` ("Before approval, … rejects a definition with a missing or
     unresolved required section …") and `project-definition-form/1` — agree with the rewritten
     `project-technology-record/1`; no overlap of conditions beyond the missing section, which
     both name for their own decision.
  2. WAY-108 ("markers read by the readiness check … keep their English forms") — the marks are
     such markers; agrees.
  3. WAY-34 ("A newer version of the process enters a product only through a task in the product
     that moves the pin") — WAY-121's "once its product moves the commit of the-way it pins"
     agrees.
  4. WAY-118, WAY-124 (a task using an approved definition checks that its approval still holds),
     WAY-142 (plan header fingerprint), WAY-145/156 (plan recheck after a definition gate) — the
     skill routes of row 5 follow them; agree.
  5. WAY-54 / WAY-46 / WAY-49 use "mark(ed)" for other labels — plain meaning, no homonym (see
     candidate 14).
  6. The part-map failure mode above — the question.
  7. No collision with WAY-137 beyond the recorded `narrows`; no environment fact concerned.
- Result: no collision; nothing to change in the foundation; one human question.

## Commands, exit codes, outputs

No foundation file changed, so no format guard or element test was required. Run for evidence:

| Command | Exit | Output | Summary |
|---|---|---|---|
| fingerprint recount (scratch script, `relation-model/fingerprint.py`) | 0 | [return-fingerprints.txt](return-fingerprints.txt) | WAY-121 `d0b060e5`, WAY-165 `a179dbe4`; 197 decision links, 0 stale; 254 invariant links to decisions, 0 stale |
| `git fetch origin`; `git rev-parse origin/foundations` | 0 | (console) | `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` |
| term search over the five element files (grep) | 0 | [return-search.txt](return-search.txt) | 103 lines, findings above |

Latest checks of the code on `0c1dfd5` (turn 3): project-level 269 OK, gate 98 OK, entry points
current, `git diff --check` clean.

## Changed files

None (`0c1dfd5..0c1dfd5`). Commit: none. `.runs/` not staged.

## Concerns

1. The part-map question above must reach the request with its options; if A is taken, the line is
   a foundation change of this request (assessed with the rest).
2. The request still owes: To do 3's line on moving the pin (part map *Change paths*); WAY-121 as a
   changed approved decision for renewed acceptance; the Minor findings and *Declined to judge*
   lines of the review in their lists (WAY-161).

## Assessment settlement (turn 5)

Applied exactly the rows marked "Apply" in [assessment-settlement.md](assessment-settlement.md):
A1, A2, A8. Commit `4239271` fix(foundations): settle the independent assessment of the
technology change (private author address checked).

**A1 — WAY-121's gate clause as a state.** The third binding sentence now reads: "The readiness
gate stops a definition whose list lacks one of the three, approved or not, and such a definition
goes back to the step and through the readiness gate again; when the foundation already holds every
choice the list needs, the step records the decision that holds each and settles nothing." The gate
clause comes first, so it no longer reads as conditional on the exit clause (also the reviewer's
Minor 1); the pin move and the refinement stay only in the *complies*/*violates* examples and the
*Rationale* (WAY-34), unchanged. Rows 1, 4 and 5 keep their meaning: row 5's "also a definition
approved before" is "approved or not". Still three binding sentences. Fingerprint WAY-121
`d0b060e5` → `068d878b`, renewed in WAY-122, WAY-123, WAY-165 (*Relations*) and in
`project-technology-record/1` *Derives from* (`foundations/invariants.md:2027`) — a link renewal
only; the invariant's sentence, its fingerprint and every `# invariant:` test are unchanged. WAY-165
`a179dbe4` unchanged. Each dependent read against the new wording: still valid.

New Polish meaning sentence of WAY-121: Lista wyborów technologicznych każdej definicji projektu
zawsze — niezależnie od reguły, co na nią trafia — ma trzy osobne pozycje drogi agenta do
działającego produktu (logi, interfejs, dane deweloperskie), każdą nazwaną w języku definicji i
oznaczoną angielskim znacznikiem tego, którą z trzech jest, rozstrzyganą jak każdy wybór własną
decyzją projektowaną albo wskazaniem decyzji, która już ją rozstrzyga, i mającą odpowiedź także
wtedy, gdy produkt danej rzeczy nie ma; bramka gotowości zatrzymuje definicję bez którejś z nich —
zatwierdzoną czy nie — a taka definicja wraca do kroku technologii i przez bramkę ponownie.

**A2 — restated routes cut.** `project-level/plan/skill/SKILL.md` and
`project-level/task/skill/SKILL.md` are back to their base text (`77c8a8b`): their existing "a
finding returns the definition to `define-project`" leads to `define-project` step 0, which
explains the finding. `project-level/lead/skill/SKILL.md` keeps one clause naming no mark string:
"…and so does one the state reader's `definition` finding reports as lacking a choice its
Technology list must hold, which `define-project` step 0 takes back (WAY-121)".

**A8 — duplicates cut.** `project-level/test_readiness_marks.py` loses
`test_the_whole_list_has_no_finding` and `test_a_section_reading_none_gives_its_one_finding`, and
the two constants only they used (`LOGS`, `DATA`). Kept: the per-mark finding naming its mark, the
`TODO` case and `ApprovedBefore`.

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [settlement-guard-decisions.txt](settlement-guard-decisions.txt) | 0 errors, 7 warnings (five pre-existing passed check-by dates WAY-03/21/52/55/69; placeholders WAY-121 :3468, WAY-165 :5388), 5 unchecked (no-main options) |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | [settlement-guard-invariants.txt](settlement-guard-invariants.txt) | 0 errors, 0 warnings, 3 unchecked (no-main options) |
| `python -B gate/run_tests.py elements/decisions` | 0 | [settlement-tests-decisions.txt](settlement-tests-decisions.txt) | 169 OK |
| `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl` | 0 | [settlement-tests-project-level.txt](settlement-tests-project-level.txt) | 267 OK (269 − the 2 cut); record: no `fail`, no `unchecked` |
| `python -B gate/run_tests.py gate` | 0 | [settlement-tests-gate.txt](settlement-tests-gate.txt) | 98 OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | [settlement-skill-entry-points.txt](settlement-skill-entry-points.txt) | entry points are current |
| `git diff --check 77c8a8b..HEAD` | 0 | [settlement-diff-check.txt](settlement-diff-check.txt) | empty |
| fingerprint recount | 0 | [settlement-fingerprints.txt](settlement-fingerprints.txt) | 197 decision links, 0 stale; 254 invariant links, 0 stale |
| weakest-point check `ApprovedBefore` (`python -B -m unittest -v project-level/test_readiness_marks.py`) | 0 | [settlement-weakest.txt](settlement-weakest.txt) | both `ApprovedBefore` tests ok (also inside the project-level run) |

Changed files `0c1dfd5..4239271`: `foundations/decisions.md` +8/−9; `foundations/invariants.md`
+1/−1; `project-level/lead/skill/SKILL.md` +3/−5; `project-level/plan/skill/SKILL.md` +1/−4;
`project-level/task/skill/SKILL.md` +1/−6; `project-level/test_readiness_marks.py` +0/−10.

Concerns: none new. The change to WAY-121's binding sentence and to the invariant's *Derives from*
link falls inside the assessed foundation change (settlement, WAY-10); the affected review reads
`0c1dfd5..4239271`.
