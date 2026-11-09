PASS 2984b5f

# Review — the return step's commits (`review-change`)

Range: base `ba36539`, head `2984b5f` (`git rev-parse HEAD` = `2984b5fa762956ffbe49ee22d986ff39106b5dc4`,
matches). `git log ba36539..2984b5f`: one commit, "Name the invariant that derives from WAY-309 in its
verification". `git diff ba36539..2984b5f`: one field, `foundations/decisions.md:9810-9811`, WAY-309
*Verification*, which now begins `invariants: tracked-file-private-paths. For the cycle's use of the
script, an agent compares a cycle, its record and its request with the decision:`; the pair of
examples, binding sentences, *Rationale* and *Rejected* are unchanged.

## Findings

### Critical
none

### Important
none

### Minor
none

Blocking findings: 0. Out of scope: 0.

## What was checked and why the change holds

- **The correction itself.** `foundations/invariants.md:86-94`: `tracked-file-private-paths` reads
  *Derives from:* `WAY-320 · WAY-309`. `elements/decisions/template.md`, section "Verification":
  "*Verification* names, after `invariants:`, the invariants of the product's invariants file that
  derive from the decision ... each of them names the decision in *Derives from* (WAY-12, WAY-17)";
  and "Tests live only with invariants; a decision names in *Verification* the invariants derived
  from it (WAY-12)". Before the commit WAY-309 named no invariant while one derives from it — a real
  mismatch, and the commit closes it. Both decisions the invariant names (WAY-320 at
  `decisions.md:10219`, WAY-309 at `decisions.md:9810`) now name it back.
- **Form.** The template lets either part stand alone or both together; the combined form with a
  qualifying clause before the examples is the form WAY-27 (`decisions.md:727`) and WAY-320
  (`decisions.md:10219`) already use in this log. The qualifier "For the cycle's use of the script"
  is accurate: the invariant checks tracked files, the examples cover what no invariant checks —
  the order of runs, the description, the remarks — which the template says the pair is for
  ("for an agent comparing a change with what no invariant of the decision checks").
- **Does the field restate WAY-309 differently (WAY-263)?** No. The examples are word for word as
  before; the added clause narrows nothing in the binding sentences.
- **Positive control of the check that guards the field.** On a scratch git copy of `2984b5f`, the
  identifier in WAY-309's *Verification* was changed to `tracked-file-private-pathz`;
  `foundation_check.py` then reported `foundations/decisions.md:9810: tracked-file-private-pathz
  names no invariant`, exit 1. So the check's 0 errors on the head does read this field and is not a
  vacuous pass.

## Mismatches the return step might have missed (handoff: judge these)

Each considered against the files of the whole change (`17b83bf..2984b5f`); none found.

- **Part map, trust boundary.** `elements/part-map/template.md` "Trust boundary": a pattern of the
  *code files* of a part that take in files from outside, "such as one on the user's disk". No
  tracked `.py` reads `~/.the-way/locations.json` (search of `*.py` for `locations\.json|\.the-way/`:
  the only hit is a fixture string in `task-cycle/test_tracked_files_private_paths.py:118`); the
  locations file is read by agents following `project-level/backlog_place.md`. No trust boundary is
  missing; the return step's reason matches.
- **Part map, External context.** The locations file is a user's file an agent reads.
  `foundations/part_map.md:217` already has an untrusted row for "a repository or a user's files an
  agent's instructions are read from"; the template says a row "is read by whoever records a trust
  boundary at the part that handles the exchange", and no code handles this one. Not a mismatch.
- **Part map, files and dependencies.** `project-level/backlog_place.md` falls under
  `project-level/**`; `task-cycle/test_tracked_files_private_paths.py` under `task-cycle/**` and
  imports only `private_paths_check` of its own part. New references from `foundation-review` and
  `task-cycle` to `project-level` are allowed by their *Depends on*. `python -B gate/run_tests.py
  elements/part-map` exits 0.
- **WAY-308 and task-cycle cleaning vs WAY-320.** WAY-308 (`decisions.md:9731-9734`) and
  `task-cycle/skill/SKILL.md:522-526` turn a path outside the repository into "a description of what
  the place is"; WAY-320 (`decisions.md:10213-10214`) says "a file that points to such a place names
  its entry in the locations file", and `project-level/backlog_place.md:27-29` says records name the
  entry. These do not collide: WAY-27 (`decisions.md:717-719`) uses "described ... instead of being
  pointed to" as the alternative to pointing, so a description is not a pointer, and a description
  that names the entry satisfies both. Not a mismatch.
- **WAY-140 vs `backlog_place.md:24-26`** ("An agent that runs a task cycle does not create or change
  the locations file (WAY-140)"). Writing a file on the user's disk is an effect outside the
  product's repository; WAY-140 lets the cycle write only its record in the backlog entry. The
  citation holds.
- **WAY-27 vs `AGENTS.md:25`** ("as the author's rules for agent tasks in his notes give"). The line
  carries the whole command (Ready, `[/]`, remove the date), names the source in words with no
  path, and the task settles exactly this (*To do* 5, question 3). WAY-27's purpose — the content
  is carried, nothing a reader must follow — is kept; `outbound-link-reach` (links only) is met.
  Not a mismatch.
- **WAY-107 scope `installation`, `product-guidelines`.** No installer code writes or reads
  `## Backlog` (hits only in `installation/test_*_installation.py` fixtures with relative places);
  `product-guidelines/*/recognize.md:8-9` reach `## Backlog` through `refine-task`, whose
  `project-level/task/skill/read_sources.md:17-18` now routes through `backlog_place.md`.
- **Glossary.** No entry names the backlog or a location; "human action"
  (`foundations/glossary.md:79-83`) still reads correctly with the locations-file step being the
  human's. No term is missing.

## Declined to judge

- The earlier change `17b83bf..ba36539` beyond the questions above: it passed its own review; it was
  read only to judge the return step's comparison.

## Checks

| Command | Exit |
|---|---|
| `git rev-parse HEAD` | 0 (`2984b5f…`, matches) |
| `git diff ba36539..2984b5f`, `git log --oneline ba36539..2984b5f` | 0 |
| `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| `python -B gate/run_tests.py task-cycle` | 0 (209 tests, OK) |
| `python -B gate/run_tests.py elements/common` | 0 |
| `python -B gate/run_tests.py elements/part-map` | 0 |
| Positive control: `foundation_check.py .` on a scratch git copy of `2984b5f` (`git archive`) with WAY-309's identifier mistyped | 1 (reports `decisions.md:9810 ... names no invariant`), as expected |

The full gate was not run: it is the cycle's own. The reviewed worktree was not changed
(`git status --short` empty after the checks).

## Reaches beyond the dispatch

- `foundations/part_map.md` whole entries of the parts touched and its External context — to judge
  a missed part-map change (the handoff asks for it).
- `elements/part-map/template.md`, sections "Trust boundary" and "Exchanges with the external
  context" — what a trust boundary and a row are, for the same question.
- WAY-27 (`decisions.md:715-748`), WAY-107 (`decisions.md:2394-2431`) and WAY-140
  (`decisions.md:3808-3857`), each whole — the other entries naming the backlog place, which the
  handoff asks to check.
- `foundations/glossary.md`, entry "human action" — whether the locations-file step changes its
  reading.
- `task-cycle/skill/SKILL.md:510-536` (cleaning of the record) and `project-level/backlog_place.md`
  whole — to compare WAY-308 and WAY-320 with the files.
- `task-cycle/test_tracked_files_private_paths.py:1-70` — the invariant's test, to confirm its
  imports and that it is the test the invariant's `test` method names.

## Searches not found or unclear

- none
