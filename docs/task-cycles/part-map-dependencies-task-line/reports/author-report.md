# Report of the one author — part-map-dependencies-task-line

**Status:** done with concerns (the concerns are the choices below marked "for the orchestrator";
none stops the change).

Worktree `the root of the task's worktree`, branch
`task/part-map-dependencies-task-line`, base `c2541ed6ef1aca0e5509cc9a929f377d97a108bc`.

## Commit

- `af76148` — "Allow the ten dependencies the code holds, define a dependency of a part, and test
  four reads of a form". One commit: the four invariants are cited by their tests and named by
  their decisions, and the part map's new dependencies are what lets the tests read the writing
  side, so no smaller split stands on its own. Added by path, never `git add -A`.

## Files changed (added / removed lines)

| File | + / − |
|---|---|
| `foundations/part_map.md` | 16 / 12 (ten dependencies of seven parts; the sentence of `project-level`) |
| `foundations/glossary.md` | 6 / 0 (term `dependency of a part`) |
| `foundations/invariants.md` | 40 / 0 (four invariants) |
| `foundations/decisions.md` | ~45 / ~25 (WAY-107 in place; *Verification* of WAY-153, WAY-300, WAY-339, WAY-167) |
| `project-level/task_line.md` | 5 / 1 |
| `project-level/backlog_place.md` | 3 / 2 |
| `elements/part-map/template.md` | 12 / 8 (see "Choices", 7) |
| `elements/invariants/examples.md` | 4 / 3 |
| `project-level/test_blocked_request_line.py` | new |
| `process-audit/test_gate_runner_path.py` | new |
| `task-cycle/test_review_tag_pattern.py` | new |
| `elements/common/test_guidelines_place.py` | new |

No file of a trust boundary of the map (`project-level/readiness_check.py`, `plan_check.py`,
`plan_state.py`, `task-cycle/cycle_stages.py`, `cycle_measures.py`, `gate_times.py`,
`process-audit/audit_count.py`, `installation/install.py`, `instruction-files/check_instructions.py`)
was changed. The two tests that import `plan_state.py` and `audit_count.py` only read a constant of
each.

## The seven items of To do and the seven rows

| To do / row | Where it stands |
|---|---|
| To do 1 | `foundations/part_map.md`, field *Depends on*, the ten dependencies exactly as the task lists them. |
| To do 2 / row 1 | `foundations/glossary.md`, term `dependency of a part`. |
| To do 3 / rows 2–5 | `foundations/invariants.md`: `blocked-request-line`, `gate-runner-path`, `review-tag-pattern`, `guidelines-file-place`, each `Method: test`, each cited by a line `invariant:` in a test. |
| To do 4 / row 6 | WAY-107 in place: sentence, *Verification*, *Rationale*, *Rejected*. |
| To do 5 / row 7 | `project-level/task_line.md`: the opening sentence no longer says "three forms"; a paragraph in "The identifier" says to ask the human and write no line where the rules do not accept the derived identifier. Row 7 goes to a file of a place, so no entry is written for it. |
| To do 6 | `project-level/backlog_place.md`, the sentence that ended "says how a line is written by them (WAY-107)". |
| To do 7 | `foundations/part_map.md`, the sentence of `project-level` is two sentences. |

## Foundation entries (one sentence in English, one in the language of the task document)

- **row 1, glossary `dependency of a part`** — EN: a dependency of a part is any reach of it to
  another part (a skill call, a file, the form of a file, a path or a git tag read, or an import),
  not only a Python import. PL: zależność części od części to każde sięgnięcie jednej części do
  drugiej — wywołanie skilla, odczyt pliku, jego formy, ścieżki albo znacznika git, albo import —
  a nie tylko import Pythona.
- **row 2, invariant `blocked-request-line`** — EN: the wording of the blocked request line that
  `plan_state.py` reads stands in backticks in the two skill files of `task-cycle` that tell the
  cycle to write it, and the record template has the field's label. PL: linia zablokowanej prośby,
  którą czyta `plan_state.py`, stoi dosłownie w dwóch plikach `task-cycle`, które każą ją pisać, a
  szablon zapisu ma etykietę pola.
- **row 3, invariant `gate-runner-path`** — EN: the path of the gate's test runner whose history the
  audit reads is a file git tracks. PL: ścieżka programu bramki, której historię czyta audyt, jest
  plikiem, który git śledzi.
- **row 4, invariant `review-tag-pattern`** — EN: every name the review skill gives the review tag,
  with `-2` and `-3` where the date repeats, is found by the pattern the reminder counts from. PL:
  każda nazwa, którą skill przeglądu daje znacznikowi (także z `-2` i `-3`), pasuje do wzorca, od
  którego przypomnienie liczy scalenia.
- **row 5, invariant `guidelines-file-place`** — EN: every path of guidelines the template of
  `product-guidelines` names, and the directory it names, matches the place the foundation check
  reads. PL: każda ścieżka wytycznych z szablonu `product-guidelines` i jego katalog pasują do
  miejsca, które czyta kontrola fundamentu.
- **row 6, WAY-107** — EN: the-way gives only the derivation of a task's identifier from its plan;
  the rules of the task place give the rest of a line, the characters of the identifier and its
  uniqueness included, and where they do not accept the derived identifier the agent asks and writes
  no line. PL: the way daje wyłącznie wyprowadzenie identyfikatora z planu; resztę linii, także
  znaki identyfikatora i jego jednoznaczność, dają reguły miejsca, a gdy nie przyjmują
  wyprowadzonego identyfikatora, agent pyta i nie pisze linii.
- **row 7, `project-level/task_line.md`** — the same last clause, as an instruction of the skill
  file (no entry). EN as for row 6; PL: j.w.
- **To do 1 and To do 7 (carried by task items, no row)** — EN: the part map allows the ten
  dependencies and says that `project-level` answers for when a line is written, not for how, and
  for the deployment-skill guide. PL: mapa pozwala na dziesięć zależności, a część `project-level`
  odpowiada za to, kiedy linia jest pisana, nie jak, i za przewodnik wdrożeniowy.
- **the cycle's** (no row, no projected entry carries them): the rewording of
  `elements/part-map/template.md` and `elements/invariants/examples.md` from "allowed dependencies"
  to "allowed imports" where the sentence speaks of the test of imports (WAY-97), and one sentence
  in the template's "Allowed dependencies" that a dependency of a part is any reach, not only an
  import. EN/PL: the invariant `cross-part-imports` holds imports only; the template said
  "dependencies" for it, which the new definition makes wrong. / Niezmiennik
  `cross-part-imports` pilnuje wyłącznie importów, a szablon nazywał go „zależnościami”.
- The *Verification* of WAY-153, WAY-339, WAY-300 and WAY-167 names the new invariant derived from
  each (rows 2, 3, 4, 5; WAY-12, WAY-18).

## How each test finds the writing side, and which part it belongs to

A test belongs to the part it tests (WAY-44), which is the reader's part, so each imports only what
its own part holds, and reads the writing side as text or through git, never by import.

| Test (part) | Reader, imported | Writing side, found by |
|---|---|---|
| `project-level/test_blocked_request_line.py` (`project-level`) | `plan_state.BLOCKED_DRAFT` | a literal text: the wording, in backticks, in each of two named files of `task-cycle`; a line beginning with the label in `task-cycle/record_template.md` |
| `process-audit/test_gate_runner_path.py` (`process-audit`) | `audit_count.GATE_TEST_RUNNER` | a path git tracks: `git ls-files` on the path |
| `task-cycle/test_review_tag_pattern.py` (`task-cycle`) | `review_reminder.last_review_tag` | a pattern of a tag: the name after "Name the tag" and the suffixes after "add" in `foundation-review/SKILL.md`, then each name made as a tag on a repository built for the test and looked for by the reader on real git |
| `elements/common/test_guidelines_place.py` (`elements-common`) | `foundation_check.GUIDELINES` | a pattern in text: every backticked path of the section "Where guidelines go" of `product-guidelines/template.md`, placeholders made `x` |

The reason for the reader's part: the writing part is the one that changes without knowing the
reader exists, and the new dependency in *Depends on* is what names the reach; a test in the
writer's part would need the opposite dependency, which the map does not allow.

## Checks

Failing, then passing, of each invariant's test (the writing or reading side broken in the
worktree for a moment, then restored with `git checkout --` or `git mv` back; nothing of it is in
the commit):

| Invariant | Break | Failing run | Passing run |
|---|---|---|---|
| `blocked-request-line` | "opened on this commit" → "opened on that commit" in `task-cycle/skill/blocked_finding.md` | `python -B -m unittest project-level/test_blocked_request_line.py`, exit 1 | `python -B gate/run_tests.py project-level`, exit 0 (278 tests) |
| `blocked-request-line` | field label of the record template shortened | same command, exit 1 | same |
| `gate-runner-path` | `GATE_TEST_RUNNER = "gate/run_test.py"` in `audit_count.py`; also `git mv gate/run_tests.py gate/runner.py` | `python -B -m unittest process-audit/test_gate_runner_path.py`, exit 1 both | `python -B gate/run_tests.py process-audit`, exit 0 (184 tests) |
| `review-tag-pattern` | `TAG_PATTERN = "foundation-reviews/*"` in `review_reminder.py`; also the skill's tag name changed to `review/YYYY-MM-DD` | `python -B -m unittest task-cycle/test_review_tag_pattern.py`, exit 1 both | `python -B gate/run_tests.py task-cycle`, exit 0 (483 tests) |
| `guidelines-file-place` | regex of `foundation_check.GUIDELINES` read `^guideline/…`; template: `docs/<discipline>.md`; template: first directory `docs/`; template: `guidelines/coding/<kind>.md` | `python -B -m unittest elements/common/test_guidelines_place.py`, exit 1 each (after the change below) | `python -B gate/run_tests.py elements/common`, exit 0 |

Other checks, each with exit code:

- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`): exit 0, `0 errors`,
  run on the final text.
- `python -B gate/run_tests.py elements/part-map` (the test `cross-part-imports` among them): exit 0,
  39 tests, run after the part map's change.
- `python -B gate/run_tests.py elements/common`: exit 0 (235 tests), again after the last edit of
  a test of that directory; `task-cycle`: exit 0 (483 tests), again after the last edit.
  `project-level` and `process-audit` ran once, after the foundation edits and before the rewrap of
  one line of WAY-107's *Rationale*, which no test of those directories reads.
- Not run: `python -B gate/run_tests.py` with no directory (the orchestrator runs it); the
  `gate` directory's tests (no file of `gate/` changed); `skill_entry_points.py --write` and
  `agent_type_copies.py --write` (no skill, no description, no agent type changed).
- The flaky timing test of the `gate` directory was not run, so it did not show.

## Own-work check (WAY-164)

- Requirement most likely not met: "each of the four tests fails when the reading side **or** the
  writing side changes alone". I broke each side of each test, as the table above gives.
- It showed a gap. The first version of `test_guidelines_place.py` read only backticked paths that
  began with `guidelines/`, so a template naming `docs/<discipline>.md`, or the directory `docs/`,
  still passed (exit 0 on both breaks). I changed it to read every backticked path of the section;
  the two breaks, and a nested `guidelines/coding/<kind>.md`, now fail (exit 1) and the unbroken
  run passes. The command of the failing and passing runs is the one in the table.
- A second test of each file checks the test's own oracle (a pattern that finds everything, a
  listing that names everything), so that the first test cannot pass for any input.

## Choices (with the way rejected and the cost if wrong)

1. **Term `dependency of a part`**, not `dependency` or `part dependency`. The bare word also carries
   the meanings of a task's dependency and a package's, which a reader gives it, so a bare entry
   would claim them (WAY-99). Cost if wrong: a later rename of the term and of the sentences that
   use it (the part-map template, WAY-225 and WAY-44 write "a dependency", which reads in the
   context of the map).
2. **The sentence of `project-level` is two sentences**, as the task says. For the orchestrator:
   `elements/part-map/template.md` says "one sentence" for a part and "The binding part of an entry
   is one sentence"; the map already holds parts of several sentences (`process-audit`,
   `installation-command`), so I did not edit the template. A follow-up could reword the template.
3. **WAY-107's binding text is two paragraphs**, not one: the first holds the two sentences about
   the place, the second the rules of a line and the identifier. One paragraph would hold four
   sentences, and WAY-05 gives one to three. Rejected: a fourth sentence in the one paragraph.
   Cost if wrong: the index of decisions shows the same sentences; nothing reads the paragraph
   count.
4. ***Derives from* of the four invariants.** The task names WAY-300 (row 4) and WAY-339 (row 3)
   but no decision for rows 2 and 5; I chose WAY-153 (the reader of the plan state) and WAY-167
   (the place of guidelines). Rejected for row 2: WAY-269 (reserved choice: it holds no sentence
   about the wording of the record). Cost if wrong: the *Derives from* and the *Verification* name
   another decision.
5. **WAY-107's *Rejected*** gets the way not chosen that the task's question keeps (a decision of
   its own, narrowing WAY-107), worded without the history of how it came.
6. **New test files**, one for each invariant, not additions to the files of 2 000 and 3 000
   lines. Rejected: adding classes to `test_plan_state.py` and `test_audit_count.py`.
7. **Reworded "allowed dependencies" to "allowed imports"** in `elements/part-map/template.md`
   (four places) and `elements/invariants/examples.md` (WAY-97): the invariant and its test hold
   imports only, and under the new definition "dependencies" would promise more than it checks. Cost
   if wrong: the template says "imports" where the task wanted the old word kept; revert is four
   words.
8. **One commit**, not two (see the commit's paragraph above).
9. **The label of the field is checked in `record_template.md`**, not in the two skill files: the
   skill files print the label in italics (`*Request URL and status*`), while the template has the
   line the reader's constant begins with.

## Context of the task, checked against the files (it was checked on `21ecb62`)

- The reader and writer sides of the four reads stand as the task gives: `BLOCKED_DRAFT` in
  `plan_state.py`, `GATE_TEST_RUNNER` in `audit_count.py`, `TAG_PATTERN` in `review_reminder.py`,
  `GUIDELINES` in `foundation_check.py`; the skill names `foundation-review/YYYY-MM-DD`; the
  template names `guidelines/`. `test_plan_state.py` still keeps its own `BLOCKED_FIELD`.
- One difference: `elements/common/migrate_foundation.py` holds a second copy of the same
  `GUIDELINES` regex, and `audit_count.py` reads two scripts of the gate (`GATE_SCRIPTS`, the
  runner and `task-cycle/gate_times.py`). The invariants hold the runner and the one regex of
  `foundation_check.py`, as the rows say; the copy in `migrate_foundation.py` is held by no test
  (the same part, so no *Depends on* is involved).
- The reaches of the seven parts into other parts (the skills of `decisions` and `part-map`, the
  entry points of `agent-instructions`) I did not open; the change does not depend on them.

## Reach beyond the dispatch (name, where, why)

- WAY-153 and WAY-167 whole, WAY-44 and WAY-51 (sections of the *Rationale* and *Rejected*), by the
  line numbers of a search: to choose *Derives from* and to see the ten dependencies against
  WAY-225 and WAY-44.
- `project-level/test_plan_state_invariant.py`, the opening of `test_plan_state.py`,
  `test_review_reminder.py` and the opening of `test_audit_count.py`: to see how a test of each
  reader starts and what it already holds.
- `product-guidelines/template.md` lines 15–44, `foundation-review/SKILL.md` lines 28–106,
  `task-cycle/skill/reserved_return.md` lines 45–69: the writing sides.
- The skills of the glossary, invariants and part-map elements and the files they name, as
  `task-cycle/skill/foundation_step.md` says; and the user's global rule on commits
  (`git.md`), before the commit.

## Unread material

- `foundations/decisions.md` whole: not read; WAY-107, WAY-153, WAY-225 whole; WAY-300, WAY-339 and
  WAY-167 read from their heading to the end of their *Verification* or *Rationale* (WAY-339 only
  its first 45 lines; its *Rationale* and *Rejected* unread); WAY-44 read in its *Verification*,
  *Rationale* and *Rejected*, its binding sentence by the index; WAY-51 read by its binding
  sentence in the index and its *Rationale* and *Rejected*.
- WAY-11, WAY-95 (the binding sentences by the index and the glossary template), WAY-07, WAY-12,
  WAY-22, WAY-97, WAY-99, WAY-314, WAY-293: by their binding sentences in
  `.runs/orchestrator/index.md` only. WAY-02 and WAY-150: not opened (no test I altered holds a
  decision by a line `decision:`).
- `elements/decisions/skill/read.md`, `decide_entry.md`, `projected.md`, `elements/decisions/examples.md`,
  `elements/part-map/examples.md`, `first_map.md`: not opened. The skills of the three other
  elements I read; the *Examples* files of the glossary and invariants I read.
- `elements/part-map/test_cross_part_imports.py`: read whole; `elements/common/foundation_check.py`
  lines 1–150 and the line of `GUIDELINES` only; `process-audit/audit_count.py` lines 120–150 and
  400–425; `plan_state.py` lines 1–200; `review_reminder.py` lines 1–110.
- `task-cycle/skill/reserved_return.md` read lines 45–69 only.

## Searches not found or unclear

- The glossary uses of the word `dependency`: I searched the English text of the tracked files for
  its forms (274 lines outside Python); I judged each by its context and read the lines on parts
  and the part map; the lines of tasks and of products' packages carry the reader's meaning and I
  left them. I did not read each of the 274 lines in its full paragraph.
- No convention found for naming a test of an invariant; I used `test_<subject>.py`.
- The task gives no decision for rows 2 and 5 (see Choices, 4).
- The template says "one sentence" for a part while the task asks for two (Choices, 2).

## Working copies

- `.runs/author/` of the worktree: outputs of the runs and the commit message file; no worktree, no
  clone. Removed before this report was returned.
