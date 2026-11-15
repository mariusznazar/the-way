FAIL af7614867a6e477088a7831fc170c4b279b6ba21

# Review of the whole change — part-map-dependencies-task-line

Range `c2541ed6ef1aca0e5509cc9a929f377d97a108bc..af7614867a6e477088a7831fc170c4b279b6ba21`
(`git rev-parse HEAD` is `af76148…`, one commit, one author, no plan, no slices, no spec). Worktree
`the root of the task's worktree`, read-only. Method:
`task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`. The task and the author's
report are read whole.

Counts: 1 blocking, 4 Minor within the task, 2 out of scope (listed apart).

## Changed files (added / removed lines; sizes by `task-cycle/change_file_sizes.py`)

| File | + / − | Lines before → after |
|---|---|---|
| `elements/common/test_guidelines_place.py` | 86 / 0 | new → 86 |
| `elements/invariants/examples.md` | 4 / 3 | 17 → 18 |
| `elements/part-map/template.md` | 11 / 9 | 201 → 203 |
| `foundations/decisions.md` | 44 / 23 | 9463 → 9484 |
| `foundations/glossary.md` | 6 / 0 | 191 → 197 |
| `foundations/invariants.md` | 40 / 0 | 376 → 416 |
| `foundations/part_map.md` | 18 / 13 | 274 → 279 |
| `process-audit/test_gate_runner_path.py` | 48 / 0 | new → 48 |
| `project-level/backlog_place.md` | 3 / 2 | 50 → 51 |
| `project-level/task_line.md` | 5 / 1 | 64 → 68 |
| `project-level/test_blocked_request_line.py` | 69 / 0 | new → 69 |
| `task-cycle/test_review_tag_pattern.py` | 86 / 0 | new → 86 |

12 files, +420 / −51 in total by `git diff --stat`; the per-file figures are `git diff --numstat`. The-way has no `guidelines/coding.md`, so no rule of size
and no test of it; no function or file the change reaches grew past anything (the largest addition
is 86 lines of a new test file, and `decisions.md` grew by 21 lines). A finding of structure would
be Minor (WAY-363); there is none.

## Findings

### Blocking (Important), within the task

**I-1. The sentence of `project-level` in the part map says the part is not responsible for how a
line is made, which WAY-107 as the change rewrites it, `project-level/task_line.md` and
`project-level/backlog_place.md` contradict for the derivation of the identifier.**

- Place: `foundations/part_map.md:82-91` (the sentence of `project-level`): "…and for when
  the line of a task in the product's backlog is written, given its dependencies and moved to ready,
  but not for how a line is made, which the rules of the task place say (WAY-107)."
- What is wrong: after the change, WAY-107 (`foundations/decisions.md:294-314`, the second paragraph) says "The one part
  of a line that the-way gives is the derivation of a task's identifier from its plan and its name
  in the plan", and that derivation is written in `project-level/task_line.md` ("The identifier"),
  a file of this part (`project-level/**`). `project-level/backlog_place.md:18-20` says so too:
  "gives the derivation of a task's identifier from its plan, the one part of a line the-way gives,
  but not how a line is written". The part-map sentence has no such qualification: it says the part
  does not answer for how a line is made, and that the rules of the task place say how. A reader of
  the map who asks which part answers for the identifier of a line, so that a dependency can name a
  task before its line exists, is told none does. The sentence restates WAY-107 more broadly and
  without its qualification, which WAY-263 grades Important for an entry the change writes. The
  task's own item 7 words the exclusion as "a nie za to, jak powstaje", so the defect comes from
  the task's wording; the task's item 7 does not forbid the qualification, and the settlement of
  row 6 (the-way gives the derivation) requires it.
- Why it matters: the part map is what the return step and the next author compare with the code;
  a sentence that denies a responsibility the part holds sends a later change to the wrong place or
  leads to the derivation being removed as out of the part's remit.
- Evidence: the three texts above, read side by side; `git grep -n "derivation" project-level`
  finds the derivation in `task_line.md` only, a file of `project-level`.
- Fix, a clause: say that the part gives the derivation of the identifier of a task of a plan and
  that the rest of how a line is made is the rules of the task place's.
- Slice: not applicable (one commit, no plan).

### Minor, within the task

**M-1. The new sentence in `elements/part-map/template.md` restates the glossary entry in other
words and leaves part of it out.**
`elements/part-map/template.md:91-94` says "A dependency of a part is any reach of it to another
part, not only an import, so *Depends on* names also a part whose skill the part calls or whose
file, form of a file or tag of git its script reads". The entry `dependency of a part`
(`foundations/glossary.md:37-41`) lists a skill that calls "a skill or a file" of the other part,
a script that reads a file, "the form that file is written in, a path or a git tag". The template
omits the path of a file and the file a skill calls. The first clause, "any reach", carries the
meaning, so this is not graded as WAY-263 does for a restatement that changes it; but two lists of
one definition drift. A reference to the term instead of a second list would keep one definition.

**M-2. `blocked-request-line` joins two rules in one sentence.**
`foundations/invariants.md:378-386`: the wording stands in backticks in two files of `task-cycle`,
"and" `task-cycle/record_template.md` has a line beginning with the label. The invariants template
("The sentence") gives one rule to an entry and judges a joined pair as two (WAY-12). A reword of
the label and a reword of the wording are separate breaks. The content agrees with the code and the
test checks both, so Minor (WAY-364). The task's row 2 asks for the first rule only; the label rule
is the author's addition (author's report, Choice 9), for which a reason stands.

**M-3. Bare `dependency` / `allowed dependencies` in running text of the part map's decisions and
skills does not use the glossary term as it is written.**
The term is `dependency of a part` (`foundations/glossary.md:37`); WAY-93 heads an entry with the
term "as the foundation writes it in running text" and WAY-97 says a sentence relies on a term by
using its word. The text writes "a dependency the code holds that the part map does not allow"
(WAY-225, `foundations/decisions.md:2488-2491`, whose binding sentence the task keeps unchanged),
"the allowed dependencies" (`foundations/part_map.md:4`, `elements/part-map/skill/SKILL.md:3,40`)
and the like; only `elements/part-map/template.md:91` writes the term in full. A reader who takes
the field's meaning of the bare word, imports or packages, reads WAY-225 as about imports only, the
very reading the task's Need names. The author's reason for the longer term (Choice 1) is sound
(the bare word also means a task's and a package's dependency); the gap is that no sentence outside
the template uses it. Not graded higher because the sentences are in the context of the part map,
which narrows the reading, and the glossary-entry rule of section 3 gives Minor where no sentence
is cited that a reader reads wrongly in its context.

**M-4. The task's second sentence of `project-level` departs from the part-map template, which says
one sentence for a part.**
`elements/part-map/template.md:42` ("<one sentence: what this part is responsible for>") and
`:191-193` ("The binding part of an entry is one sentence"); the entry of `project-level` now has two
sentences, as the task's item 7 asks. The map already holds longer parts (`process-audit`,
`installation-command`), so the departure is older than the change. The author raised it and did not
edit the template. This lies outside the task (the task asks for two sentences, and a reword of the
template is a new matter); it is listed here and under **Out of scope**, and the cycle does not fix
it (WAY-161).

### Out of scope (counted apart; none blocks)

- **O-1.** M-4 above: the template's "one sentence" against the map's multi-sentence parts.
- **O-2.** `elements/common/migrate_foundation.py` holds a second copy of the regex of
  `foundation_check.GUIDELINES`, and `process-audit/audit_count.py` reads two more paths
  (`MEASURES_SCRIPT`, `GATE_SCRIPT`, both of `task-cycle`) that no invariant of this change holds;
  the rows of the task name only the runner and the one regex. A task of its own.

## Items of the task, row by row (judged, not taken from the author's table)

- **To do 1, ten dependencies.** `git diff` of `foundations/part_map.md` shows exactly these
  changes to *Depends on*: `decisions` + `invariants`, `product-guidelines`, `project-level`;
  `part-map` + `decisions`; `elements-common` + `product-guidelines`; `project-level` +
  `task-cycle`; `task-cycle` + `foundation-review`; `process-audit` + `gate`; `agent-instructions`
  + `foundation-review`, `process-audit`. That is ten, nothing else moved there but the sentence of
  `project-level` and the wrapping of three lines. No *Trust boundary*, no *Files*, no surface
  changed; no file the map names as a trust boundary changed (`git diff --stat`). Each of the ten
  has the ground the task's *Questions to settle* gives (WAY-225), none from "the code already
  reaches". `foundation_check.py` finds all parts named.
- **To do 2, glossary.** `foundations/glossary.md:37-41`, term `dependency of a part`, alphabetically
  placed, one definition, `Not: none`. It names the five kinds of reach that row 1 names (skill
  call, file, form of a file, path, git tag, import). `Not: none` agrees with WAY-94: the other
  meanings of the bare word (a task's, a package's) are the field's. See M-1 and M-3.
- **To do 3, four invariants.** `blocked-request-line`, `gate-runner-path`, `review-tag-pattern`,
  `guidelines-file-place`, each `Method: test`, `Rests on: none`, `Part` the parts a change can
  break it in, each cited by a line `invariant:`. See "Tests" below. *Derives from*: WAY-300 and
  WAY-339 as the task names; WAY-153 and WAY-167, which the task does not name, hold: WAY-153's
  reader reports "blocked draft request in record" as evidence of a cycle trace
  (`project-level/plan_state.py:407-409`), and WAY-167's sentence puts guidelines in
  `guidelines/<discipline>.md`, which is what the template and the check agree on. The two names a
  *Verification* of WAY-153 and WAY-167 each (WAY-12, WAY-17).
- **To do 4, WAY-107.** In place (WAY-07). The binding text is two paragraphs: place (two
  sentences), line handling and the derivation (two sentences); `elements/decisions/template.md`
  "Binding sentences" gives one paragraph for the question and one for each part of another
  question, each of one to three sentences — met. *Verification* complies and violates both name
  the derivation, the characters and the asking; *Rationale* gives the reason and the price;
  *Rejected* gives the way the task keeps (b) with its reason, without the history, as WAY-134
  and the template require. The binding text, *Verification* and *Rationale* agree (compared
  line by line); WAY-293 is cited by number. No normative word, no `should`/`will`.
- **To do 5, `task_line.md`.** "Where the rules are silent on a matter of that list, ask the human
  once" names what it concerns; the paragraph in "The identifier" says to ask the human and write
  no line where the rules do not accept the derived identifier, and not to change it, with the
  reason. Met.
- **To do 6, `backlog_place.md`.** Says when and by which agent a line is written by the rules, and
  that the-way gives the derivation, not how a line is written. Met.
- **To do 7, sentence of `project-level`.** Two sentences, the deployment guide named, `when` /
  `not how`. Met in the words of the task; see I-1 for what the wording leaves false, M-4 for the
  count of sentences.
- **Settlements, rows 1–7.** Row 1 glossary, rows 2–5 invariants, row 6 sentence of WAY-107, row 7
  the instruction file; each lies in the place its column gives. The rewording of "allowed
  dependencies" to "allowed imports" in `elements/part-map/template.md` (four places) and
  `elements/invariants/examples.md` (one place) names no row, but WAY-97 requires it: the
  invariant `cross-part-imports` checks imports only, and under the new definition of a dependency
  the old words would promise a check of every reach. Judged within the task. The
  sentence "where the dependency is an import" at `template.md:117` is accurate.
- **Fidelity to sources.** The change takes nothing from outside the task: the ten dependencies,
  the definition of row 1, the rows' meanings and the answer to the P6 question are as the task
  gives them. Nothing invented. No file of a trust boundary changed; no operation that cannot be
  undone.
- **Decisions in play.** WAY-225, WAY-51 (no invariant marked violated: `git grep "Violated: yes"`
  has no new hit), WAY-11, WAY-44, WAY-95, WAY-107, WAY-293, WAY-300, WAY-339: each kept as the
  task says.

## Tests — correctness and the break checks

I ran the checks in a worktree of the head under `.runs/review-whole/wt` (removed; see Working
copies). Each break is a change of one side only, then a reset of the worktree.

Passing runs on the head, all exit 0: `python -B -m unittest project-level/test_blocked_request_line.py`
(3 tests), `process-audit/test_gate_runner_path.py` (2), `task-cycle/test_review_tag_pattern.py` (3),
`elements/common/test_guidelines_place.py` (3); `python -B elements/common/foundation_check.py`
(no skip flag): `0 errors`, exit 0.

Breaks, each run as `python -B -m unittest <test file>`, the exit code shown:

| Invariant | Side | Break | Exit |
|---|---|---|---|
| `blocked-request-line` | writing | wording in `task-cycle/skill/blocked_finding.md` reworded | 1 |
| | writing | wording in `task-cycle/skill/reserved_return.md` reworded | 1 |
| | writing | label in `task-cycle/record_template.md` renamed | 1 |
| | reading | `BLOCKED_DRAFT` wording changed in `plan_state.py` | 1 |
| | reading | `BLOCKED_DRAFT` label changed | 1 |
| `gate-runner-path` | writing | `git mv gate/run_tests.py gate/runner.py` | 1 |
| | reading | `GATE_TEST_RUNNER = "gate/run_test.py"` | 1 |
| `review-tag-pattern` | writing | skill's `Name the tag` form changed to `review/YYYY-MM-DD` | 1 |
| | writing | skill's suffixes changed (`-b`, `-c`) | 1 |
| | writing | skill's suffixes dropped | 1 |
| | reading | `TAG_PATTERN = "foundation-reviews/*"` | 1 |
| | reading | `TAG_PATTERN = "foundation-review/????-??-??"` (misses the suffixes) | 1 |
| `guidelines-file-place` | reading | `GUIDELINES` regex `^guideline/` | 1 |
| | reading | regex loosened to `^guidelines/.+\.md$` (nested files) | 1 (caught by the uncited oracle test, `guidelines/x/y.md`) |
| | reading | regex loosened to any directory | 1 (oracle test, `docs/x.md`) |
| | writing | template's `guidelines/coding.md` moved to `docs/coding.md` | 1 |
| | writing | template's directory sentence moved to `docs/` | 1 |
| | writing | template's `guidelines/coding-<kind>.md` nested | 1 |

The failing tests named the breaks, not an import error (read from the `FAIL:` lines). Each test
reads the real reader's constant or function and the real writing file; none computes its expected
value from the code under test (the oracle tests check that the reader's constant splits, that the
git listing says "no file" for a path that is none, that the pattern does not find a tag of another
name, and that the check reads no file outside `guidelines/`). The test of `review-tag-pattern`
builds a repository of one tag whose name is the skill's, so git matches the pattern; the invariants
template's rule on input made up for a test (WAY-61) holds, because the sentence is about the
match, and the names come from the real skill.

Weak points found, not graded: the tests of `blocked-request-line` find the wording by text in
backticks, so a skill that moved it into a fenced block fails the test while still telling the
cycle the same; that is a stricter check than the sentence's "in backticks" and the sentence says
it.

The suites of the directories the change touches, run in the same worktree with
`python -B gate/run_tests.py <directory>`: `elements/part-map` (39 tests) exit 0, `project-level`
(278) exit 0, `process-audit` (184) exit 0, `elements/common` (235) exit 0, `task-cycle` (483)
exit 0. The whole `python -B gate/run_tests.py` I did not run (the orchestrator runs it).

## Selection, structure and reaches

- Parts the change touches, by WAY-44 and the rules for a file collecting entries: `decisions`
  (`foundations/decisions.md`, entries scoped `project-level`, `task-cycle`, `process-audit`,
  `product-guidelines`), `part-map`, `glossary`, `invariants` (the four parts the new invariants
  name), `project-level`, `process-audit`, `task-cycle`, `elements-common`, `product-guidelines`
  and `foundation-review` (through the new invariants' *Part*).
- Index written with `python -B elements/common/decision_index.py --output
  .runs/review-whole/index.md` (the log has topical sections; I chose the sections "The foundation
  and its entries", "Decision entries and the decision log", "Invariants", "Glossary", "The part
  map and derived files", "Process audit", "Project plan", "Review of a change", "Product
  guidelines and their rules", with `--part` for the eight touched parts and `--decision` for
  WAY-107, 153, 225, 51, 11, 44, 95, 293, 300, 339, 167): 63 decisions in full, 104 by heading. The
  index is a file no commit takes. I ran through the 104 headings: those bearing on the work
  (WAY-134, WAY-33, WAY-114) are named under Unread material with what I read of each; none of the
  others points to a bearing on this change.
- Invariants read whole: `cross-part-imports`, `project-plan-state-evidence`,
  `project-plan-state-subprocesses`, and the four new ones; `return-step-record` I did not open (the change does not reach it). Part-map entries: the whole map read. Glossary: the new entry, plus the glossary
  template. Templates read whole: `elements/decisions/template.md`, `elements/invariants/template.md`,
  `elements/part-map/template.md`, `elements/glossary/template.md` (first 80 lines, the form of an
  entry).
- Word `dependency` in the English text of tracked files: I read each of the 78 lines outside
  `foundations/decisions.md` and Python (`git grep -n -i dependenc`), and the lines of
  `foundations/decisions.md` that are not about a task's or a package's dependency (about 60
  lines, among them WAY-44, WAY-51, WAY-225, WAY-299's withdrawn row), and the Python uses in
  `elements/part-map/test_cross_part_imports.py` ("no dependency" for the standard library and for
  a path outside the root stays true under the new definition). No use of the glossary term in
  another meaning than its entry gives remains; the uses of the bare word for a task or a package
  carry the field's meaning. The finding M-3 is about the term's spelling, not its meaning.
- Files outside the touched parts reached beyond the selection (what, where, why):
  `task-cycle/skill/reserved_return.md`, `task-cycle/skill/blocked_finding.md`,
  `task-cycle/record_template.md`, `foundation-review/SKILL.md` lines 28-110,
  `product-guidelines/template.md` lines 15-45, `process-audit/audit_count.py` 405-420 and
  `project-level/plan_state.py` 20-40, 140-200, 396-415, `task-cycle/review_reminder.py` 45-90,
  `elements/common/foundation_check.py` line 131, to read the writing and the reading sides of
  the four invariants; `elements/part-map/skill/*.md` (the three files the author left unread:
  `first_map.md`, `decide_entry.md`, `write.md` through a search for `import`, `reach` and
  `Depends on`) and `elements/part-map/examples.md`, to check that no use of "dependency" there is
  moved by the definition; `elements/decisions/skill/decide_entry.md`, `read.md` and
  `elements/decisions/examples.md` whole, for the form of WAY-107.
- The gap list of the handoff, answered:
  - WAY-107's form: kept (two paragraphs of two sentences; *Verification*, *Rationale*, *Rejected*
    as the template gives); the author's unread files `decide_entry.md`, `read.md`, `examples.md`
    give nothing that the change misses (`examples.md` names WAY-03 only; `projected.md` I did not
    read: it is the projected-mode skill, which this change does not touch).
  - WAY-339 *Rationale* and *Rejected*: read whole; the *Verification* edit names the invariant as
    the entry's runner-change sentence requires, and nothing in *Rationale* or *Rejected* is made
    false. WAY-153, WAY-300, WAY-167: read whole; the same.
  - "allowed dependencies" → "allowed imports": required by WAY-97, within the task.
  - Two sentences in the sentence of `project-level`: the task asks for it; M-4 and I-1.
  - *Derives from* of `blocked-request-line` (WAY-153) and `guidelines-file-place` (WAY-167): hold.
  - The 274 lines: see above.

## Declined to judge

- The second copy of the guidelines regex in `elements/common/migrate_foundation.py`, held by no
  test: outside the task's row 5 (O-2).
- `MEASURES_SCRIPT` and `GATE_SCRIPT` paths of `process-audit/audit_count.py`, held by no
  invariant: outside the task's row 3 (O-2); they stand in a part `process-audit` already depends
  on.
- The template's "one sentence" per part against the parts that hold more (M-4, O-1).
- The decision in `elements/part-map/test_cross_part_imports.py`'s reading of `Violated: yes`
  invariants for imports only: no behaviour changes; the template sentence qualifies it.

## Checks I ran (command, exit code)

- `git rev-parse HEAD` → `af7614867a6e477088a7831fc170c4b279b6ba21`; `git log c2541ed..HEAD` one
  commit.
- `python -B task-cycle/change_file_sizes.py c2541ed… af76148…` → exit 0.
- `python -B elements/common/decision_index.py --sections --output .runs/review-whole/sections.md`
  → exit 0; the index command above → exit 0 (the first attempt with the numbers written `107` etc.
  gave exit 2, `no decision 107`; the form is `WAY-107`).
- In the worktree of the head: `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- The four test files, each unbroken → exit 0; each broken as the table gives → exit 1 (one
  loosening of `GUIDELINES` first gave exit 0 because my edit did not apply; repeated with an edit
  that applied and then exit 1).
- `python -B gate/run_tests.py elements/part-map`, `project-level`, `process-audit`,
  `elements/common`, `task-cycle` → exit 0 each (39, 278, 184, 235, 483 tests).
- Not run: the whole `python -B gate/run_tests.py`; the directories `gate`, `product-guidelines`,
  `foundation-review`, `installation`, `instruction-files` (no file of them changed).

## Unread material

Decisions of the index I read whole: 13 of the 63 listed in full — WAY-107, WAY-153, WAY-225,
WAY-44, WAY-51, WAY-95, WAY-97, WAY-99, WAY-11, WAY-134, WAY-300, WAY-339, WAY-167. The rest of the
63 I read by their binding sentences in the index: WAY-05, WAY-12 and WAY-293 bear on the
change and stayed read by binding sentences and, for WAY-05 and WAY-12, by the decisions template
that carries them; their *Rationale* and *Rejected* are unread. WAY-33 and WAY-114 I read by
heading only. The 104 decisions by heading I ran
through by headings only. No guideline files exist in this repository (`guidelines/` is absent), so
none is unread. `elements/decisions/skill/projected.md` unread (projected mode; not touched).
`elements/glossary/template.md` read to line 80 only; the remainder (form of an entry, examples)
unread. The whole of `project-level/plan_state.py`, `process-audit/audit_count.py`,
`task-cycle/review_reminder.py` and `elements/common/foundation_check.py` unread beyond the passages
named.

## Searches not found or unclear

- WAY-33's cycle-side "search of the whole foundation" is not recorded in the commit; I cannot tell
  from the files what the author's search covered beyond the author's report, and I searched the
  word `dependency`, `three forms` and the identifier derivation myself.
- No convention for naming the test files of an invariant was found (author's report says the same);
  `test_<subject>.py` fits the neighbours.
- The task's item 7 says "a nie za to, jak powstaje" with no exception for the derivation, while its
  row 6 gives the derivation to the-way: unclear how the task meant both to hold (I-1).

## Working copies

- `.runs/review-whole/wt` of the worktree: a detached worktree of `af76148`, made for the checks
  and breaks above. Removed with `git worktree remove --force` and `git worktree prune` (the list
  no longer shows it). The test outputs I kept there I deleted; nothing of it is needed.
- `.runs/review-whole/index.md` remains (the index the handoff asks for; no commit takes it);
  `sections.md`, the list of sections I wrote first, I deleted.
