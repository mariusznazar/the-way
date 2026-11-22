FAIL ae37fca3310ce6efe7e7939413b8b7a1205b0ead

Review of the whole change (`review-change`), one author, no plan, no slices. Range
`2a2f4106c216c0fef4e68b7ed8bd5728ae2660ae..ae37fca3310ce6efe7e7939413b8b7a1205b0ead`, nine
commits, 26 files; `git rev-parse HEAD` in the worktree is `ae37fca3310ce6efe7e7939413b8b7a1205b0ead`.
Every blocking finding comes from no slice (the change has none): it comes from the one author's
commits named at it.

## Findings

### Critical

none

### Important

**I1. Point 3 of the task: what the quoted wording asks of the orchestrator reaches no file the
orchestrator reads.** Place: `task-cycle/plan/SKILL.md:189-195` (the new bullet) against
`task-cycle/skill/planning.md:26-37` ("A slice's handoff") and `task-cycle/skill/SKILL.md:463-469`
(step 9, sub-step 2, what a slice's handoff carries) and `:481-484` (sub-step 4, the retry);
commit `b7d99dfa`.
What is wrong: the accepted wording has three duties that are the orchestrator's — "The handoff of
each later slice lists the tests the plan leaves failing at its base, with their owners", the
executor reporting "a listed test that fails as expected" (which it can do only when its handoff
lists it), and "the orchestrator gives it an owner by editing the plan before the next slice is
dispatched". The change writes them only into `task-cycle/plan/SKILL.md`, the planner's method.
The orchestrator reads "this skill and no method you do not conduct" (`task-cycle/skill/SKILL.md:76-77`,
WAY-125), and it builds a slice's handoff by sub-step 2 and `planning.md` "A slice's handoff",
neither of which names the tests the plan leaves failing; nothing it reads tells it to edit the plan
for a failure no *Goal* names. The one half-sentence added to sub-step 3 ("and the failures its
report names against those the plan lists") makes the comparison a mechanical check whose mismatch
"goes as information to the review", and sub-step 4 still retries an executor that "reports a
failing check of its slice".
Why it matters: an executor of slice 3 that runs "the tests of the code you touched" meets a test
slice 1 left red for slice 4, finds no list of it in its handoff (its section of the plan holds only
its own *Goal*), reports a failing check and is retried a class higher — the failure AIR-708 names
and the task's *Need* gives as its first cause: "reguła stoi w pliku, którego agent nie czyta w
chwili działania". The task's *Miejsca* for point 3 name where the quoted wording stands; they do
not make the orchestrator's duties optional, and the author raises the same gap as doubt (a).
Evidence: the three passages above, read in the worktree at the head; a search of
`task-cycle/skill/` for `leaves failing|tests the plan|failing at its base` finds nothing, while the
same search of `task-cycle/plan/` finds `SKILL.md:191-192` (control).
Contradiction: no

**I2. `decision_index.py` reads the list of withdrawn identifiers with no check of its fields, and
reads a missing column as an empty list of successors.** Place:
`elements/common/decision_index.py:134-149` (`withdrawn_numbers`, `why, successors = (cells + ["",
""])[1:3]`); commit `943d4153`.
What is wrong: the change reworks the script's reading of the decision log — it now reads the table
under "## Withdrawn identifiers" and its columns *Why* and *Successors* — but takes the columns by
position, never by their names in the header, and pads a short row with empty cells. A log whose
table lacks the column *Successors* (or names it otherwise) gives, for a withdrawn number, the line
"`<ID>` is withdrawn: `<why>`; it has no successor" and exit code 0. WAY-344 asks of a script a
change changes, for "the whole reading of each file whose way of reading the change reworks", that a
missing field or one under another name ends it "with exit code 2 and a message that names the file
and the field, … never guessing and never reading the absence as an empty value", and that "each
reading of a file that the rule covers has one test that gives the file without one of the fields it
needs"; its *violates* names "a change that reworks the reading of a file checks the field it added
and leaves the other fields of that file unchecked" and "a changed script's reworked reading of a
file, has no test that gives the file without a field". Here even the fields added are unchecked
and no such test exists. The check of the foundation does not catch the shape either
(`elements/common/foundation_check.py:403` reads `cells[2] if len(cells) > 2 else ""` for the
decision log).
Why it matters: the line "it has no successor" is the answer the agent reads in place of the
decisions it should have read; a malformed table turns a withdrawn number with living successors
into a silent "nothing to read" — the quiet pass WAY-344 exists to stop. `guidelines/coding.md`
("A field missing from a file a script reads") makes this comparison a duty of the review of each
change that changes a script.
Evidence: probe `reports/review-whole-probe-withdrawn/` (input `foundations/decisions.md`, command
and output in `command.txt`): exit code 0 and "GAME-00 is withdrawn: merged into GAME-01; it has no
successor" on the head; the base ends with exit code 2.
Contradiction: yes — WAY-344

**I3. Point 5.1: text with a quotation mark is taken out of the lookup only for the ASCII double
quotation mark.** Place: `instruction-files/check_instructions.py:444` (the characters
`'*<>{}|$…"=,'`), its docstring at `:18-20` and the test
`instruction-files/test_check_instructions.py:323-333`; commit `89ae582c`.
What is wrong: point 5.1 makes "tekst z cudzysłowem" no path. The 17 warnings that the task's
*Context* (point 5) counts as "tekst, który nie jest ścieżką" on loop2 are, at the base: 7 addresses
`#/...`, 2 `.css`, 2 `restrict,command="/usr/local/bin/loop2-deploy"` and 6 `'\''` (the shell idiom
that closes a single-quoted text). The 6 `'\''` hold no `#`, `=`, `,` or bare extension, so they are
the case "tekst z cudzysłowem" stands for — the 2 `restrict,…` are taken out by `,` and `=` already.
The head still warns on all 6; typographic quotation marks, which the-way's own decision template
counts as quotation marks (`"…"`, `“…”`, `„…”`, `elements/decisions/template.md`, "Verification"),
are not taken out either. The author names the 6 as unclear in its report.
Why it matters: under WAY-418, which this change writes, each of those 6 warnings is an Important
finding of the review of loop2's change that moves its pin, and the task's *Out of scope* leaves to
that change only the real warnings — `'\''` is not among them; the noise point 5 is to cure stays in
part.
Evidence: probe `reports/review-whole-probe-quote/` (input `repo/AGENTS.md`, command and output in
`command.txt`): `'\''` and `‘docs/a.md’` warn, `"\""` does not; the base and head scripts on the
local loop2 checkout, read only: base 143 warnings, head 21, of which 6 are `'\''`.
Contradiction: no

**I4. The author's judgment that the change alters no behaviour a user sees disagrees with the
change, and no case of the walk is drawn up.** Place: `reports/author-report.md`, section
"Walkthrough (`walkthrough.md`)"; the commits `0b3a8ab1`, `4efde783`, `2a03c166`, `943d4153`,
`89ae582c`.
What is wrong: the change alters what five commands print and how they end in a terminal —
`decision_index.py --decision` for a withdrawn number exits 0 with a new line where it ended with
exit code 2; `slice_size.py` prints the verdict `fits by ranges of <file>` and exits 0 for it;
`check_instructions.py` prints `INFO` where it printed `WARN`; `gate_times.py` starts `npm` on
Windows where it failed; `run_tests.py` prints another count. WAY-406 requires the walk "for every
change of behaviour that the user sees in the running product — … a command in a terminal", and
its *violates* reads "the author of a change that alters what a command prints reports only that its
tests pass". The author judged "the-way has no running product" and did not read
`task-cycle/change/walkthrough.md`, which `task-cycle/change/SKILL.md:112-113` sends it to for such
a change. The-way's foundation settles no way to its running product, so WAY-406's third paragraph
holds: the walk is not performed "with that reason in the report and in the description of the
request", and "the author … still draws up the cases from the requirements of the task and marks
each as unchecked with that reason" (`walkthrough.md:26-28`). The report holds no such cases.
Why it matters: the request's description, built from the report, would tell the human that no
behaviour a user sees changed, and would carry no list of cases for a check by hand, which is what
WAY-406 gives the human where no way is settled. The author's own runs by hand hold: my runs of the
same commands (checks below) show the behaviour the requirements ask for; what is missing is the
judgment, the cases from the requirements and their state in the report.
Evidence: the author's report, section named above; `foundations/decisions.md`, WAY-406 (lines
7087-7108 at the head).
Contradiction: yes — WAY-406

### Minor (within the task's scope)

**M1. `task-cycle/review/whole_change.md:27-30` names `installation/README.md` with no product
form and gives the reviewer no command for its run.** The sentence added for point 5.4 says "the
check of the product's instruction files, which the product's one command runs as
`installation/README.md` gives, in a run on the head of the change". Elsewhere the file gives the
product form of each path of the-way (`:43-44`, "in a product `python -B
.the-way/task-cycle/change_file_sizes.py`"); in a product the README stands at
`.the-way/installation/README.md`. The reviewer does not run the product's one command (WAY-160), so
"a run on the head" has to be its own run of the script — `python -B
.the-way/instruction-files/check_instructions.py` from the product's root, as the README gives —
which the sentence does not say. A reviewer that reads it as the CI run finds no run before its
review. Evidence: the line itself.

### Minor (outside the task's scope)

none

### Out of scope

none beyond **Declined to judge**.

## The author's doubts (a)–(d)

- (a) `task-cycle/skill/planning.md` left unchanged: a finding, I1.
- (b) `AGENTS.md:13-15` reworded: kept. The base holds the warning `AGENTS.md:13` `SKILL.md` does
  not exist (my run of the base script on the base), and under WAY-418 the head of this change must
  hold none; the rewording keeps the line's meaning and adds no rule (WAY-128, WAY-130). No
  finding.
- (c) the *Rejected* row of WAY-255 on the silent output: kept. Row 1's last column, which the
  human accepted with the row, names "kryterium ciszy wydruku" among the rejected ways the decision
  would otherwise not get, and the task's *Context*, point 1, keeps it as rejected; it is no way the
  cycle derived (WAY-134). No finding.
- (d) the walk: a finding, I4.

## Coverage of the task

- *To do* 1–13: each quoted wording stands word for word where the task places it (checked against
  the diff: points 1, 2, 3, 4, 5.2, 5.4, 6, 7, 8, 9, 12, 13; the half-sentence of point 3 in step 9;
  the reference of point 6 at `task-cycle/skill/SKILL.md:189-191`; the path of point 8 removed with
  the words of question 2). Gaps: point 3 in effect (I1), point 5.1 in part (I3).
- Point 10: by value (`107`, `WAY-107`, `D-7`, `D-07`), withdrawn numbers with successors, `none`,
  chains with reasons, loops; help, `metavar` and `elements/common/way_of_working.md:105-110` say
  `--decision ID` with one sentence of both rules. Gap of field checks: I2.
- Point 11: `shutil.which` before `Popen`, a test with a `.cmd` file skipped off Windows; the last
  `Ran` line counts, with a test of a nested run. Both verified by runs below.
- *Settlements to record*: row 1 → WAY-255 second paragraph and three *Rejected* ways; row 2 →
  WAY-25 second paragraph and the *Rejected* check over `narrows`; row 3 → WAY-136 sentence and the
  *Rejected* ban on a red state; row 4 → WAY-418, new, at the end of "Instruction files", held by a
  pair of examples, its *Rejected* the three ways of its sources. Each meaning matches its row. The
  task carries no projected entry.
- Nothing taken from the sources is altered or invented that I found, beyond what the findings name.

## Declined to judge

- Whether 30 minutes suits a mutation run of WAY-253 or a container build, which WAY-255's first
  paragraph also names: question 1 of the task settled one limit for every command, and the
  rationale names the price ("a run that was only slow costs the check it stood for").
- `gate_times.py` reading the time of the first `Ran` line of a block while `run_tests.py` now
  counts the last: point 11 changes only the count, and the task's *Context* says the reading of a
  nested output in `gate_times.py` was fixed already.
- Arguments of a `.cmd` gate pass through `cmd.exe`'s parsing on Windows (`&`, `%`, `^`): the
  declaration is the product's own and as trusted as the command it names, so it gives the product
  no power it lacks; no product's declaration in the task holds such a character.
- The doubled word in lines such as "WAY-20 is withdrawn: withdrawn: it said …": the task gives the
  form `<ID> is withdrawn: <powód z tabeli>`, the reason word for word.

## Checks

All from the worktree of the head `.runs/review-whole/head` unless named; "exit" is the exit code.

| Check | Command or method | Result |
|---|---|---|
| sizes of the changed files | `python -B task-cycle/change_file_sizes.py 2a2f4106 ae37fca3` (reviewed worktree) | exit 0; 26 files modified, +718 lines; largest growth `instruction-files/test_check_instructions.py` +139, `elements/common/decision_index.py` 240 → 333, `instruction-files/check_instructions.py` 939 → 998 |
| rule of size, base and head | `python -B -m unittest test_size_invariant` in `agent-instructions/` of each worktree | exit 0 on both (4 tests); nothing pushed over a threshold |
| focused tests of the changed scripts | `python -B -m unittest test_slice_size test_gate_times test_tracked_files_private_paths` in `task-cycle/` | exit 0, 80 tests, 1 skipped (POSIX signal); the `.cmd` test ran (Windows) |
| | `python -B -m unittest test_decision_index` in `elements/common/` | exit 0, 25 tests |
| | `python -B -m unittest test_check_instructions` in `instruction-files/` | exit 0, 120 tests, 5 skipped |
| | `python -B gate/run_tests.py gate` | exit 0, 37 tests |
| test directories the author did not run after the last commit | `python -B gate/run_tests.py task-cycle`, `… process-audit`, `… project-level` | task-cycle exit 0, 570 tests, 2 skipped; process-audit exit 0, 344 tests; project-level exit 0, 302 tests |
| linter and formatter | `python -B -m unittest test_linter_invariant` in `agent-instructions/` | exit 0, 5 tests |
| foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| instruction check on the head (whole_change.md, WAY-418) | `python -B instruction-files/check_instructions.py .` | exit 0, `0 error, 0 warn, 5 info` |
| instruction check on the base | the same in the base worktree | `0 error, 2 warn`: `AGENTS.md:13` `SKILL.md`, `guidelines/coding.md:51` `.py` |
| point 11.1 end to end | `python -B <head or base>/task-cycle/gate_times.py --output … --registry .runs/review-whole/registry -- npm --version` | head exit 0, prints `11.13.0`, row written; base exit 2, `cannot start 'npm'` |
| point 10 on the real log | `python -B elements/common/decision_index.py --decision <ID> --output .runs/review-whole/p.md .` for `20`, `46`, `D-07`, `WAY-107`, `9999` | exit 0 with the withdrawn line and successors for 20, the chain WAY-46 → WAY-40 → no successor for 46, one decision for `D-07` and `WAY-107`; exit 2 for 9999 |
| probe I2 | `reports/review-whole-probe-withdrawn/command.txt` | head exit 0, "it has no successor"; base exit 2 |
| probe I3 | `reports/review-whole-probe-quote/command.txt` | 2 warnings: `'\''`, `‘docs/a.md’` |
| instruction check on loop2, base and head scripts (read only) | `python -B <base or head>/instruction-files/check_instructions.py <loop2 checkout>` | base `0 error, 143 warn, 7 info`; head `0 error, 21 warn, 118 info`; no warning on the head the base lacks |
| crafted input at `check_instructions.py` | reading of the code of `ignored_names`, `elsewhere`, `dead_path_note` and their tests | a `.gitignore` that is a link out is not read (test with the invariant line), a directory or no UTF-8 text names nothing; `elsewhere` asks the file system nothing and catches the drive mismatch of `commonpath` through `inside`; the network-path guard runs before it; no finding |
| crafted input at `gate_times.py` | reading of `resolve` and its tests | an empty first word or a directory ends as the script's own `Error:` with exit 2 (test); `which` runs inside the `try` that turns a start failure into that error; no finding |
| the author's own-work check | reading of its report against my runs on loop2 | it named point 5 and compared the base and head scripts on five repositories; its result (no new warning; 144 → 22 on loop2) agrees with mine (143 → 21 at loop2's present commit); it saw the 6 `'\''` and read them as outside 5.1 (I3) |

## Reaches beyond my selection

- `task-cycle/skill/planning.md` lines 1-37 and `task-cycle/skill/SKILL.md` lines 5-30, 60-80 and
  455-500: to judge where the orchestrator builds a slice's handoff and what it reads (I1).
- `elements/common/foundation_check.py:395-439`: whether the check of the foundation reads the
  columns of a withdrawn table by name (I2).
- `task-cycle/change/walkthrough.md`, whole: to judge doubt (d) (I4).
- `instruction-files/check_instructions.py:176-265` and `:336-660`: the helpers the new code calls,
  for the crafted input of the trust boundary.
- `task-cycle/gate_times.py:1-60` and `:440-460`: the docstring and the start of the command.
- `process-audit/` by search for `gate_times.py` and `run_tests.py`: whether a new series of the gate
  times needs a change of the audit (it does not: `process-audit/version_analysis.py:107-108` takes
  it from commits).
- `foundations/invariants.md`: the entries `check-instructions-refuses-outside-links`,
  `gate-times-refuses-impossible-entry`, `command-runner-passes-exit-code`, `gate-exit-code`, each
  whole.
- The local loop2 checkout, read only through the script, for I3 and the own-work check.

## Working copies

My directory was `.runs/review-whole`,
holding two git worktrees (`head` at `ae37fca3`, `base` at `2a2f4106`), the index of my selection
(`index.md`), the sections list, the extracted decisions, the outputs of my runs and a gate-times
registry. Removed: both worktrees with `git worktree remove --force` by their full paths, then
`git worktree prune` (each exit 0), then the directory itself by its full path (exit 0; it no
longer exists, and `git worktree list` names neither worktree). No remainder. Kept in `reports/` beside this report: the probes
`review-whole-probe-withdrawn/` and `review-whole-probe-quote/`.

## Unread material

16 decisions of the index of my selection read whole: WAY-25, WAY-255, WAY-136 and WAY-418, which
the change writes; WAY-12, WAY-18, WAY-225, WAY-148, WAY-160, WAY-229, WAY-339 and WAY-390, which
the task names; WAY-344, WAY-406, WAY-134 and WAY-253, which bear on findings and doubts. The other
58 listed in full were read in the index; the 104 by heading alone were run through by their
questions. Decisions that bear on the change and stayed unread whole: WAY-150 (the method of the
selection, read in `elements/common/way_of_working.md` instead), WAY-385 (the size test passed on
both worktrees), WAY-02 (the line `decision:`, read through the template's "Verification"). Guideline
files: `guidelines/coding.md`, `guidelines/testing.md`, `guidelines/coding-check.md`,
`guidelines/coding-command-runner.md` and `guidelines/coding-measuring-report.md` read whole;
`coding-generator.md`, `coding-repository-changer.md` and `coding-shared-module.md` not read, since
no changed script is of those kinds. Part map: the entries of the touched parts, read whole (the
whole file). Glossary: not read; the change coins no term and I relied on none.

## Searches not found or unclear

- Who runs the instruction check "in a run on the head of the change" that WAY-418 and
  `task-cycle/review/whole_change.md` name: the reviewer runs no gate (WAY-160), so I took it as my
  own run of the script (M1).
- A search of `task-cycle/skill/` for `leaves failing|tests the plan|failing at its base`: no hit,
  with a hit in `task-cycle/plan/SKILL.md:191-192` as control — the orchestrator's files say nothing
  of the tests a plan leaves failing (I1).
