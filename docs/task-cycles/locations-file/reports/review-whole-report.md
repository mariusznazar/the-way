FAIL 973ee64

# Review of the whole change — task `locations-file`

Range: base `17b83bf145653be0beeb43f5fa8175a4197a3700`, head `973ee64` (`973ee642a2cde638dee9bc4ba8e11f1e78652e3a`,
confirmed by `git rev-parse HEAD`), one commit. One-author route: no spec, no plan, no slices.
Blocking findings: 2 (both Important, both within the task, both in foundation or instruction text,
none in the test). Minor: 2 (within the task). Out of scope: 0.

## Changed files (added / removed lines, `git diff --numstat 17b83bf..973ee64`)

| File | + | − |
|---|---|---|
| `AGENTS.md` | 6 | 5 |
| `foundation-review/SKILL.md` | 5 | 5 |
| `foundations/decisions.md` | 77 | 14 |
| `foundations/invariants.md` | 11 | 1 |
| `project-level/backlog_place.md` (new) | 38 | 0 |
| `project-level/definition_template.md` | 5 | 3 |
| `project-level/lead/skill/SKILL.md` | 2 | 1 |
| `project-level/skill/first_write.md` | 2 | 2 |
| `project-level/task/skill/final_review.md` | 1 | 1 |
| `project-level/task/skill/read_sources.md` | 5 | 5 |
| `task-cycle/skill/SKILL.md` | 2 | 1 |
| `task-cycle/test_tracked_files_private_paths.py` (new) | 128 | 0 |

12 files, 282 added, 38 removed. Matches the author's report.

## Coverage of the task

| Item | Met | Evidence |
|---|---|---|
| To do 1 — locations file `~/.the-way/locations.json`, keys are repository names, entries by name | yes | WAY-320 (`foundations/decisions.md:10204`), `project-level/backlog_place.md:14-18` |
| To do 2 — `## Backlog` names entry `tasks` under `the-way`, no absolute path; missing file or entry → ask and offer to add | yes | `AGENTS.md:20-24`; the scratch run below shows the base lines 20 and 25 were the only hits and are gone |
| To do 3 — every skill that reads `## Backlog` finds a place given as an entry; missing place → file for a place on the user's disk, section otherwise | yes, with finding I-2 | six readers point to `project-level/backlog_place.md`: `foundation-review/SKILL.md:40-41`, `project-level/skill/first_write.md:5-7`, `project-level/task/skill/read_sources.md:17-21`, `project-level/task/skill/final_review.md:27-28`, `project-level/lead/skill/SKILL.md:21-22`, `task-cycle/skill/SKILL.md:76-78`; my own `git grep -i backlog` / `task area` / `WAY-107` over tracked files found no other reader that locates the place (the plan skill places the plan beside the definition, `project-level/plan/template.md:20`; `product-guidelines/*/recognize.md:8-9` only name the section `refine-task` read; the four `installation/test_*` hits are fixtures) |
| To do 4 — test run by `gate/run_tests.py`, reads every tracked file, fails with file and line, same pattern as `private_paths_check.py`, no `## Backlog` exception, skips only a list of four files in the test | yes | `task-cycle/test_tracked_files_private_paths.py:32-37,48-58,61-65`; reuses `private_paths_check.check_file`, so the pattern is the same by construction; `gate/run_tests.py` discovers `task-cycle/` through its tracked `test_*.py` files |
| To do 5 — Ready line keeps the command, names the rulebook in words | yes | `AGENTS.md:25-26` |
| Settlement row 1 (decision; changes WAY-27, WAY-107) | yes | WAY-27 sentence, *Verification* and *Rejected* edited; WAY-107 sentence, *Verification*, *Rationale*, *Rejected* edited, with the price of question 4 and the not-chosen way of question 4 |
| Settlement row 2 (decision: fixed place, no environment variable, keys = repository names, entries `tasks`/`projects`) | yes, with finding I-1 | WAY-320 first sentence; *Rejected* carries the five not-chosen ways of question 1 |
| Settlement row 3 (invariant; changes `outbound-link-reach`) | yes in `foundations/invariants.md`, contradicted in WAY-320 (finding I-1) | new invariant `tracked-file-private-paths` (`foundations/invariants.md:86-94`), method `test`, cited by `# invariant: tracked-file-private-paths` in the test; `outbound-link-reach` loses the `## Backlog` exception (`:78`) |
| Questions carried to cycle — how the foundation records the new check | accepted | see "Autonomous choices" below |
| Human action — locations file with `tasks` under `the-way` | present | the file exists; its keys are `{'the-way': ['tasks']}` (values not read into this report) |

Fidelity to the sources: the quotations of the human in WAY-320 *Rejected* are faithful English
renderings of the Polish quotes in question 1; WAY-107's *Rejected* additions match the not-chosen
ways of questions 1 and 4. Nothing in the change invents a way not in the task, apart from the two
behaviours the author declared (Minor M-1 and finding I-2).

### Autonomous choices of the author, judged

1. New invariant `tracked-file-private-paths` with method `test`, `outbound-link-reach` staying
   `review` without its exception — accepted. WAY-61 gives `test` only where the test checks what
   the sentence is about; the test checks paths and note links, not links into repositories a reader
   cannot open, so turning `outbound-link-reach` to `test` would break WAY-61. Row 3 says the change
   touches `outbound-link-reach`, and it does (the exception is dropped). The four exempt files stand
   in the sentence, as WAY-60 requires of a deciding condition.
2. Test in `task-cycle/`, not `gate/` — accepted. `gate` depends on none (`foundations/part_map.md:119`),
   so a test there importing `task-cycle/private_paths_check.py` would break `cross-part-imports`;
   the test and the module are both in `task-cycle`. Reading `foundations/invariants.md` as text is
   no import.

## Findings

### Important (blocking)

**I-1 — WAY-320 states the rule of settlement row 3 without its qualification, and the repository's
files do what it forbids.** `foundations/decisions.md:10210-10211` (WAY-320):
"No file the repository tracks holds an absolute path or a note link; a file that points to such a
place names its entry in the locations file." Row 3 of *Settlements to record*, and the invariant
`tracked-file-private-paths` the change writes from it (`foundations/invariants.md:88`), both carry
the exception for the four files that write example paths. WAY-320 drops it, so on the head commit
four tracked files (`task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`,
`instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py`) do what
the decision forbids — the task's *Context* counts 98 such hits in them. WAY-263 grades as Important
a change whose files do what an entry it writes forbids, or that restates an entry more broadly or
without a qualification; both hold here. Why it matters: a later agent reading WAY-320 alone, as a
decision a *Scope* search selects, would take the exemption list as a violation and "fix" the
examples or the test, the very way question 2 rejected. Related gap in the same entry: the reasoning
of question 2 — the price taken (a real path pasted into a listed file passes; adding a file to the
list shows in the diff) and its three not-chosen ways — stands in no entry; the invariant has no
rationale field and WAY-320, from which it derives, carries only question 1. Fix: qualify the
sentence (for example, "…other than the files the invariant `tracked-file-private-paths` names,
which write example paths in order to find or test them"), or narrow it to what the *violates* bullet
already says (the path of a place on the user's disk, a link to a private note), and add the price
and the not-chosen ways of question 2 to WAY-320's rationale and *Rejected*.
Evidence: the sentences quoted; `python -B gate/run_tests.py task-cycle` exit 0 only because the
test skips the four files.

**I-2 — `project-level/backlog_place.md` cites WAY-140 for a rule WAY-140 contradicts, and contradicts
the task-cycle skill that sends the orchestrator to it.** `project-level/backlog_place.md:23-25`:
"An agent that runs a task cycle writes nothing outside the repository (WAY-140): it names the
missing entry in its report and goes on only with what it can do without the place." WAY-140 says the
opposite for the backlog: "the cycle's record of the request and of the task's state in the backlog
entry the product names (WAY-107) is no effect of the task", and its *complies* example is "the cycle
itself adds the request link to the task's entry in the product's backlog". The change itself makes
`task-cycle/skill/SKILL.md:76-78` read "in the task's entry in the backlog the product names
(WAY-107), found as `project-level/backlog_place.md` gives, the cycle may add the request link and set
the task's state" — so the orchestrator follows a pointer into a file whose sentence, taken as
written, forbids that very write. This is a sentence the author added beyond the task (declared in
the report as a "weakest point"); the intended rule — a cycle does not create or change the user's
locations file — is right, but the wording is broader than the rule and misattributes it. Graded
Important: two instructions the same agent reads together disagree on whether it may write the
backlog entry, which is fragile behaviour of the cycle's last step. Fix: narrow the sentence to the
locations file, for example "An agent that runs a task cycle does not create or change the locations
file (WAY-140): …".

### Minor (within the task)

**M-1 — `project-level/backlog_place.md:20-21` widens the trigger of "missing" beyond WAY-107.**
"…or the path it holds does not exist, the place is missing." WAY-107 (as changed) names the place
unnamed, or the file or entry missing. Treating a dangling path as missing is a reasonable user's
expectation and contradicts nothing, so it is Minor; either add "or the path it holds does not exist"
to WAY-107 or leave it as the operational reading. The author declared it.

**M-2 — `project-level/backlog_place.md:10` and `:28` write the example as "the entry `tasks` under
`the-way`".** The file is read by skills working in any product; at `:28` the sentence reads as a
fixed phrase ("those say … and nothing more"), so an agent in a product may copy the-way's name.
Write it as "the entry `tasks` under the product's name, as …" or mark it as the-way's own example.

## Declined to judge

- Sessions in the cloud without the locations file — the task leaves this aside (question 1).
- The `## Backlog` section of `loop2` — *Out of scope* of the task.
- Paths already in the public history of the-way — *Out of scope* of the task.
- Whether "entry" (glossary: a foundation entry) gains a second meaning in "an entry of the locations
  file" — I found no sentence of the tracked files true in one meaning and false in the other (WAY-99),
  every use is qualified "of the locations file", and "the task's entry in the backlog" used the word
  outside the glossary meaning before this change; not a finding.
- Line length of the changed prose lines (`foundation-review/SKILL.md:44`, `project-level/task/skill/final_review.md:28`) — the-way has no guidelines, and the line at `final_review.md:28` was already long.

## Checks run

- `git rev-parse HEAD` → `973ee642…`, matches the head given.
- `python -B gate/run_tests.py task-cycle` in the reviewed worktree — exit 0, 209 tests, OK.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B gate/run_tests.py elements/common` — exit 0.
- `python -B gate/run_tests.py agent-instructions` — exit 0.
- `python -B gate/run_tests.py project-level` — exit 0.
- Failing run, in a separate detached worktree of `973ee64` in the scratchpad: `git checkout 17b83bf -- AGENTS.md`,
  then `python -B -m unittest task-cycle.test_tracked_files_private_paths` — exit 1, one failure,
  listing exactly `AGENTS.md:20` and `AGENTS.md:25` (absolute paths; values masked here). Shows the
  test fails when the behaviour it protects breaks.
- Drift run, same scratch worktree: added a fifth file name to the sentence of the invariant in
  `foundations/invariants.md`, then the same unittest command — exit 1,
  `test_the_exempt_files_are_the_ones_the_invariant_names` fails. Shows the list in the test and the
  sentence cannot drift apart silently.
- The scratch worktree was removed (`git worktree remove --force`, `git worktree prune`); the reviewed
  worktree's `git status --short` is empty before and after.
- Manual: the locations file exists, and its keys are `the-way` → `tasks` (values not printed).
- Manual: read the made-up-file tests (`task-cycle/test_tracked_files_private_paths.py:79-123`); each
  asserts an exact list with file and line written out, not a value the code computes.
- Not run: the full gate (`python -B gate/run_tests.py`), which is the orchestrator's run.

## Own-work check of the author

The author named *To do* 3 as weakest and checked it by grepping for "Backlog", "backlog" and
"WAY-107". My wider search (`task area`, `project place`, `keeps its projects/tasks`) found no reader
it missed, so its check would have caught an unmet *To do* 3. It did not reach the two places this
review blocks on: the qualification in WAY-320 and the WAY-140 sentence it added to
`backlog_place.md`.

## Reaches beyond the handoff

- `task-cycle/private_paths_check.py` whole — to confirm the test reuses its pattern and how
  `check_file` treats binary and non-UTF-8 files.
- `gate/run_tests.py` whole — to confirm the test is run by the gate's discovery.
- `foundations/part_map.md` whole (short) — to assign the changed files to parts and judge the test's
  placement against `gate`'s *Depends on*.
- `foundations/invariants.md` whole — every invariant whose *Part* is `every` or a touched part.
- Decisions WAY-27, WAY-61, WAY-60, WAY-140, WAY-263, WAY-309, WAY-320, WAY-99, WAY-107, each whole —
  named by the task, written by the change, or needed for a grade.
- Glossary entry `entry` — for the possible second meaning (declined).
- `project-level/plan/template.md:15-25`, `product-guidelines/coding/recognize.md:1-14`,
  `product-guidelines/testing/recognize.md:1-14`, `foundation-review/SKILL.md:1-30` — to check
  *To do* 3 coverage and how skills name the-way's files in a product.
- The keys of the locations file — to confirm the human action, values not read into this report.

## Searches not found or unclear

- I did not read every decision whose *Scope* names `project-level`, `task-cycle` or
  `agent-instructions` (step 2 of "Reading the foundation" selects several hundred); I read the
  decisions the task's *Decisions in play* names, those the change writes or changes, and those they
  link to or a grade needed.
- The task does not say which repository name a product uses as its key in the locations file; the
  change leaves it to the `## Backlog` line, which names it — no finding.
- `the-way` has no `guidelines/`, as the handoff says, so no guideline rule was compared.
