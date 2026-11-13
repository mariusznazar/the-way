FAIL 5353268

# Review of the whole change — review-structure-form-class

Range `65b6d7007ec4fffad998612e5c521eee93c7b8b5..5353268` (four commits, `c7a6733`, `093b901`, `76b038c`, `5353268`),
one author, no spec, no plan. `git rev-parse HEAD` = `5353268a83e1a168d84fc340a9b4546f638e1a0c`, the head given.
Instructions: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md` at the base (`git show 65b6d70:<path>`);
their head versions judged as part of the change.

## Findings

### Critical

none

### Important

**I1. The condition for marking the rule of size violated leaves out the exceptions, so a product whose only code over a
threshold is excepted is told to mark a met invariant violated.** Within the task (To do 3, row 3, question 4). From the
one author, commit `c7a6733`.

- Places:
  - `foundations/decisions.md:11797-11798` (WAY-355, binding): "Where the product's code is over a threshold, the rule's
    invariant is marked violated until the code is cleaned (WAY-51)."
  - `product-guidelines/coding/template.md:241-242`: "Where the product's code is over a threshold when the rule enters, the
    invariant is marked violated until the code is cleaned (WAY-51)".
  - `product-guidelines/coding/settle.md:113-114`: "where the trial run found code over a threshold, it is marked violated by a
    change of the foundation the human accepts".
  - `product-guidelines/coding/trial_run.md:30-31`: "where the code is over a threshold, step 4 proposes the rule's invariant
    marked violated (WAY-51)".
- What is wrong: the rule's own invariant (template.md, same bullet) is "that no function and no file of the parts named
  is longer than its threshold, other than those the decision's exceptions name". A function the human keeps whole as an
  exception is still code over a threshold, so all four sentences, read as written, mark the invariant violated where it
  holds. WAY-355's own *Verification* shows the intended meaning — "lists that function as an exception … and marks the
  rule's invariant violated where **other** code stands over" (`foundations/decisions.md:11808-11809`) — and question 4's
  answer says "gdy kod **już** przekracza próg" alongside "funkcje, których dzielić nie warto, dostają wyjątek"; the binding
  sentence drops both qualifications.
- Why it matters: the trial run happens before the exceptions are settled (settle.md asks thresholds, then exceptions,
  then invariants), so an agent following settle.md and trial_run.md proposes the violated mark from the trial run's count
  alone. Where every function over the threshold becomes an exception, the invariant's test is then marked as an expected
  failure and passes; under WAY-51 that test is to be unmarked when it passes, and a test runner fails on an unexpected
  success (the-way's own `gate-exit-code`: "exits non-zero when … a test marked as an expected failure passes"). The
  product's guidelines task would reach its gate with a foundation mark the human accepted and that the code
  contradicts — a blocked request for a wording slip. The binding sentence of WAY-355 is also what a later reader of the
  product's adoption checks against.
- Evidence: the four quoted sentences against the template's invariant sentence and WAY-355's *Verification*; nothing in
  the change says what happens where all over-threshold code is excepted.
- Fix in kind: "over a threshold, other than the exceptions of the decision" (or "where code other than the exceptions
  stands over a threshold") in WAY-355's binding sentence, template.md, settle.md and trial_run.md; trial_run.md and
  settle.md can say the mark is proposed once the exceptions are settled.

### Minor

Each within the task unless marked otherwise.

**M1. `foundations/decisions.md:11968-11970` (WAY-359, *Rationale*)** — "the same remark on the form of an entry was graded
blocking in 9 runs of an experiment with reviewers and Minor in 8, and 6 of its 32 runs rejected the change for its form
alone". The measurement stands with no conditions, while WAY-05 and the decisions template
(`elements/decisions/template.md:61-65`) let a measurement stand only "with what was measured and under which conditions".
The author's report says the task does not tie this experiment to WAY-229's; it does: the task's *Context* names cards D2
(the grade of the form) and D3 (the class of the reviewer) of one and the same "raport o eksperymencie z recenzentami",
and 32 runs is four variants of WAY-229's "8 runs a variant". Fix: one sentence pointing to WAY-229 for the conditions,
as WAY-164 does (`foundations/decisions.md:4918`). Minor: no sentence of the entry is read wrongly for lack of it, only
weighed without its population.

**M2. `product-guidelines/coding/template.md:75` and `:223`** — "It is no standing check, and the linter's set holds no rule
of it" / "It is no standing check and no rule of the linter's set." The glossary defines a standing check as "a check that a
tool makes of every change to a product's code for the whole of the product, rather than for one kind of code"
(`foundations/glossary.md`, `## standing check`), which is what the rule's test is: a tool run over the whole of the code on
every change. The sentence gives the term a second, narrower meaning ("one of the three checks WAY-202 requires"). Fix:
"It is none of the three standing checks the template requires (WAY-202)", or drop the clause; the next clause about the
linter's set already carries the point. Minor: the template spells out the rule's whole machinery, so no step goes wrong
by it; it is a word used against its glossary entry (WAY-99), with no behaviour that follows from it.

**M3. `product-guidelines/audit_end.md:52-55`** (not changed by the range) — "take from it its mode alone: the check of the
required headings of the rules on failures and logs, with the question to the human it brings at a refresh, waits for the
turn of the skill whose step it is." The change adds to `recognize.md:37-41` a second refresh check, of
`### Size of a function and a file`, with its own question to the human, and the sentence that defers the first check in a
task joining coding and testing does not name it. An agent running coding's step 1 from the testing skill may ask the
human about the rule of size out of turn. Fix: name both checks, as `product-guidelines/coding/SKILL.md:105` now does.

**M4. `task-cycle/review/whole_change.md:33`** — "Take your numbers from two runs of your own, none in the reviewed
worktree". The first run is `change_file_sizes.py`, which writes nothing (its test
`test_the_command_changes_nothing_in_the_repository`, and my run on this range left `git status --porcelain` empty), and
section 2 of the skill asks for a separate worktree only "when they need files changed". In a product the instruction
also misleads: `python -B .the-way/task-cycle/change_file_sizes.py` is to be run "from the root of the repository", and a
fresh `git worktree add` leaves the `.the-way` submodule unpopulated, so in a separate worktree the path does not exist.
Fix: "the second in separate worktrees" — let the script run in the reviewed worktree.

**M5. `task-cycle/test_change_file_sizes.py`** — two behaviours of the script are untested: the status `T` and its note
`type changed` (`task-cycle/change_file_sizes.py:165-166`; `grep -c "type changed"` on the test file gives 0), and the
escaping of `|` in a file name (`change_file_sizes.py:205`; no test name holds `|`). A change that drops either passes
every test. Separately, a name holding a backtick breaks the Markdown code span of its row (scratch run: the row
`` | `back`tick.md` | 1 | 2 | +1 | modified | ``). Polish; the numbers are right in every case tried.

**M6 (outside the task's scope). `task-cycle/review/SKILL.md:126-128` and WAY-358 (`foundations/decisions.md`, binding
sentence)** — "A finding about the structure of code that lies below the threshold of the rule of size in the product's
coding guidelines is Minor". Where the product has no rule of size (a departure reading `none —`, or, as for the-way itself
under WAY-328, no coding guidelines) there is no threshold, and neither text says whether such a finding is "below" it
(always Minor) or falls back to the general grade. The task does not settle it (row 1 and question 3 speak only of a
product's threshold), and the author's report names it; settling it is the human's choice, not a fix's, so I mark it
outside the task: the request's list, for the human to decide.

## The task, item by item

| Item | Met by | Judgment |
|---|---|---|
| To do 1 | `whole_change.md:29-49` | met |
| To do 2 | `change_file_sizes.py`, its 15 tests, `whole_change.md` | met (M4, M5) |
| To do 3 | template.md, settle.md, trial_run.md, recognize.md, hand_back.md, task_document.md, coding SKILL.md | met except I1 (and M2, M3) |
| To do 4 | `review/SKILL.md:126-128`, WAY-358 narrows WAY-161 | met |
| To do 5 | `plan/SKILL.md:173-183`, `change/SKILL.md:51-57`, WAY-360 | met |
| To do 6 | `review/SKILL.md:129-133`, WAY-359 narrows WAY-161 | met (M1) |
| To do 7 | WAY-229 *Rationale* and *Rejected* | met; compared word for word, every number and condition present, binding sentences and fields unchanged (`git diff` touches only the two prose fields) |
| To do 8 | WAY-164 *Rejected* | met; 4 and 3, 5 and 6, 112.47 vs 90.20 million in eight runs, one sentence pointing to WAY-229; binding sentences unchanged |
| Row 1 | WAY-358 | meaning kept; *Rejected* = question 3's two ways not chosen |
| Row 2 | WAY-359 | meaning kept; *Rejected* = question 2's two ways; M1 |
| Row 3 | WAY-355 | meaning kept, plus the violated-mark sentence from question 4 — I1 |
| Row 4 | WAY-356 | meaning kept; *Rejected* = question 5's way |
| Row 5 | WAY-360 | meaning kept; *Rejected* = question 6's two ways |
| Row 6 | WAY-357 | meaning kept; *Rejected* `unknown` is right: row 6's source keeps no way not chosen (WAY-134) |
| Questions 1-7 | — | each answer followed; question 1 (one task) holds; question 5 keeps WAY-16 unchanged and no product command is named; question 6 sends no spec |
| Decisions in play | WAY-161, -297, -263, -51, -135, -16, -271, -278, -168, -173, -203, -05, -27, -328 | unchanged, as the task says |
| Out of scope | — | the game's adoption, the foundation review's part and WAY-229's binding sentences are untouched |

The author's concerns: (a) numbering in commit order follows WAY-19 ("in the order entries are written") — sound; (b)
"the first commit that changes the code" keeps the row's purpose (room made before the addition) — sound; (c) code with no
user and a false name are "below the threshold" and Minor, as WAY-358's *Verification* says and question 3's chosen
variant ("zawsze drobna, chyba że przekracza próg") gives; the product with no rule is M6; (d) the paragraph on taking the
expected-failure mark off in the reviewer's own worktrees is needed for To do 2 to work where the invariant is marked
violated (an expected failure hides the test's message), and changes nothing WAY-51 governs — sound; (e) the five further
coding files are needed for the extension route WAY-278 gives (a refresh that does not look for the heading cannot
propose the rule) — sound, M3 is the one place missed; (f) WAY-359 *Scope* `task-cycle` matches WAY-263's — sound;
(g) command line, git started with argument lists only, never a shell, names read null-separated and contents by blob id —
sound; tests do fail on breakage (my four mutations below, the author's six), M5 aside; (h) see To do 7 and 8.

The cycle's choices: the reviewer running the script — sound, `whole_change.md` says so (WAY-357 does not name who runs it,
which needs no entry); the rule's place after `### Logging scope` and the wording of its invariant — sound apart from I1.

## Declined to judge

- Whether the measurements in WAY-229, WAY-164 and WAY-359 should stand as an environment fact in *Based on* (the
  decisions template, line 44-47, asks one for "a finding about agents or models"): the task settles the measurement in
  *Rationale* with *Origin* `none`, and the source is in private notes, which WAY-27 forbids pointing to; the collision
  between the template's rule and WAY-27 for a private source is outside this task. Also under Searches.
- The cost for the reviewer of installing a product's toolchain in two scratch worktrees to run the size test: the task
  chooses that the reviewer runs it (question 5); its cost is not a defect of this change.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py task-cycle` | 0 | 380 tests, OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests, OK (5 skipped) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B task-cycle/change_file_sizes.py 65b6d70 5353268` | 0 | 14 files, before 13111, after 13977, +866; every row equals `git diff --numstat` added minus removed and `git show <rev>:<path> \| wc -l` on both sides; 881 - 15 = 866 as `git diff --stat` gives |
| `git status --porcelain` in the reviewed worktree after all runs | 0 | empty |

Manual checks, in a scratch repository under the session's scratchpad (outside the worktree):

- Base and head with a name with spaces, a name with Polish letters (`zażółć.md`), a name starting with `-`, a rename with
  one added line (30 → 31, `renamed from old.py`), a binary file (`binary`, not counted), a real submodule added with
  `git submodule add` (`submodule`, `.gitmodules` counted as added), a last line without a line feed: exit 0, every row
  right; summary `9 files changed (1 added, 0 deleted, 1 renamed, 5 modified, 2 not measured)`.
- The same with repository config `diff.external`, `color.diff always`, `core.abbrev 4` and `diff.renames copies`: output
  byte-identical.
- `--root` at the submodule's directory with the superproject's commits: exit 2, `Error: … names no commit`.
- `git diff --raw` gives abbreviated blob ids; `cat-file --batch` resolves them (git abbreviates to a unique prefix).
- Mutations of a copy of the script, each against the unchanged test file (`python -B -m unittest test_change_file_sizes`):
  difference sign swapped — 7 failures; `-entry.before` → `entry.before` — 1 failure; the renamed counter dropped — 1
  failure; `^{commit}` dropped from `resolve` — 1 failure; `--no-ext-diff` dropped — passes (harmless: `--raw` uses no
  external diff); the `T` status and the `|` escape are not covered (M5; my mutation of the escape did not apply because
  the shell halved its backslash, so that one is shown by reading the test file instead).

Not run: the whole gate (the orchestrator's run, as the handoff says).

## Reach beyond the dispatch

- `task-cycle/skill/foundation_step.md` whole — what `the cycle's` marks, to judge the six entries' markings.
- `product-guidelines/audit_end.md:40-70` — searched for "failures and logs" to find other places that list the required
  headings (M3).
- `product-guidelines/coding/template.md:160-180`, `recognize.md` and `trial_run.md` whole, `settle.md:1-70` — context of the
  changed lines.
- `elements/decisions/template.md` whole — the form of the six entries (M1, Declined).
- `foundations/environment_facts.md:160-209` — the entry `shorter-guidelines-trial` as the precedent for a measurement in
  *Based on*.
- `foundations/glossary.md`: the entries `open design choice`, `standing check`, `binding sentence`, and its list of
  headings — the terms the change uses (M2).
- `foundations/part_map.md`: the entries `decisions` and `task-cycle`.
- `task-cycle/plan/SKILL.md` searched for the planner's limits on running commands.

## Unread material

Decisions of my selection (*Scope* naming `task-cycle`, `product-guidelines` or `decisions`): 251. Read whole: 46 (WAY-05,
-07, -16, -17, -19, -21, -22, -27, -32, -36, -38, -51, -60, -63, -65, -71, -134, -135, -136, -150, -161, -162, -164, -168,
-171, -172, -173, -202, -203, -204, -229, -251, -263, -271, -278, -279, -297, -312, -328, -344, and WAY-355 to WAY-360).
By title only: 205; I ran through every title, none other pointed to a bearing on the change that stayed unopened.

- Invariants: those with *Part* `every`, `task-cycle` or one of the five elements read whole (`foundations/invariants.md:1-195`
  and `:260-356`); the `project-level` ones at lines 196-259 by heading and *Part* only — no touched part. Of the twelve the
  author read by heading only, none bears on the change beyond what `foundation_check.py` and the task-cycle tests cover.
- `product-guidelines/reading.md`: read whole; lines 60-103 (the gaps of missing guidelines and their hand-back) do not
  bear on the change.
- Glossary and part map: read by the entries named above, not whole.
- The decisions element's skill (`elements/decisions/skill/*.md`) and `elements/common/rules.md`: not read; the template and
  `foundation_check.py` were my measure of the entries' form.

## Searches not found or unclear

- How the measurements of WAY-229, WAY-164 and WAY-359 should stand in *Based on* where the source is private: the
  decisions template asks for an environment fact for a finding about models, WAY-27 forbids pointing to a source readers
  cannot open, and the precedent `shorter-guidelines-trial` cites a public request. Unclear; left with the task's choice.
- What the "14 reference errors" are and over which changes the counts 5 and 6, 4 and 3 were taken: not in the task, as
  the author's report says; copied faithfully.
- Whether WAY-358's "below the threshold" covers a product with no rule of size: not settled anywhere (M6).
