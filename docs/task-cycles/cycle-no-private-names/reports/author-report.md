# Author report — cycle-no-private-names

**Status:** done with concerns (one concern, "Task source" and the plan-state reader; see Problems)

Branch `task/cycle-no-private-names`, base `ad44b84`. Worktree clean after the commits.

## Commits

| Commit | What |
|---|---|
| `c8fe9f6` | `task-cycle/private_paths_check.py` and `task-cycle/test_private_paths_check.py` (new) |
| `4643660` | rules of the cycle, templates and README (below) |
| `b6d93e8` | `foundations/decisions.md`: WAY-308 and WAY-309 |

## Files changed

| File | Added / removed lines |
|---|---|
| `task-cycle/private_paths_check.py` (new) | +153 / -0 |
| `task-cycle/test_private_paths_check.py` (new) | +250 / -0 |
| `task-cycle/skill/SKILL.md` (new section "The record before it is committed"; steps 9.4, 12, 13 and the remarks section reworded) | +77 / -20 |
| `task-cycle/skill/request_template.md` | +22 / -7 |
| `task-cycle/skill/correction.md` | +2 / -2 |
| `task-cycle/skill/blocked_finding.md` | +3 / -3 |
| `task-cycle/skill/reserved_return.md` | +3 / -3 |
| `task-cycle/record_template.md` | +9 / -6 |
| `agent-instructions/README.md` | +7 / -0 |
| `foundations/decisions.md` (WAY-308, WAY-309) | +94 / -0 |

Total: 620 insertions, 41 deletions in 10 files (`git diff --numstat ad44b84 HEAD`).

## What the change does

**The script** `task-cycle/private_paths_check.py TARGET`. TARGET is a directory (every file below it,
sorted by path) or a single file. It prints `<file>:<line>: <kind>: <text>` for each hit and a last
line `checked: N files, M listed`. Exit 0 nothing listed, 1 listed, 2 call error or a file that is
not UTF-8 (stderr `Error: ...`), as `remarks_check.py` and `request_check.py` do. It writes nothing,
holds no list of words, runs nothing. A file with a NUL byte near its start is binary: not read,
counted in the last line (so a screenshot in a record does not stop the check).

Forms chosen and why:

| Form | Pattern | Why |
|---|---|---|
| Windows drive path, backslash or slash | one letter not preceded by a word character, a colon, then a backslash or slash | covers the Windows home directory too; the "not preceded by a word character" rule keeps `https:` in a URL and `Note:` in prose out |
| Windows home without a drive | a backslash, `Users`, a backslash, a name, not preceded by a word character, a dot, a tilde, a slash or a hyphen | a path cut from its drive still shows the user name |
| Linux home | `/home/<name>` with the same boundary | boundary keeps `https://host/home/x`, `x/home/y`, `../home/y` out; `/home/` alone and `/home/<you>` are not listed (no name) |
| macOS home | `/Users/<name>` | same boundary |
| POSIX form of a drive | a slash, one letter, a slash and a name (the Git Bash form); also the same behind `mnt` (WSL) and behind `cygdrive` | the handoff asked for the first; the other two are the same leak in the other common layers |
| Note link | two opening square brackets, a first character that is no space, at least one letter or digit inside, no line break, two closing brackets (title, alias, heading and embed all match) | the form for writing about the link (three dots or an ellipsis inside) and the shell test with a space after the brackets are not listed, so the rules and this task's own text can name the form |

Not listed, by choice (stated in the script's docstring): a path that starts at a tilde, a relative
path, a UNC path (`\\host\share`), `/root`, and a user or machine name in plain text. A listing of text
that is none of the two kinds is possible (an array written with two brackets and a number, a code
sample with a drive-like pair); the rules tell the orchestrator to write it so the pattern passes it.
Fenced code and code spans are scanned like any other text (a copy publishes them too).

Stdout: the script's own words are ASCII; the listed text is printed as it stands (UTF-8, the way
`remarks_check.py` does it), control characters escaped.

**Rules (Q1 order).** New section "The record before it is committed" in `task-cycle/skill/SKILL.md`,
the one place that holds the sequence; every commit that adds the record points to it (step 12,
step 9.4's stop, `correction.md`, `blocked_finding.md`, `reserved_return.md`; the reference to the
process remarks check in the intro of the remarks and the section header of that check stay).
Order, with its reason in the text:
1. remarks check on the original `.runs/...` (words as the reports gave them; each item enters the
   remarks once, before any word changes);
2. copy the directory;
3. clean the copy as one rewriting applied to every text file, the same words wherever the text stands
   (so a report item and its entry in the remarks stay equal word for word); the three rules of the
   task (absolute path to repository-relative, private notes described, `Project relation:` line
   unchanged);
4. `private_paths_check.py` on the copy until exit 0;
5. remarks check on the cleaned copy until exit 0; a listing there means the cleaning differed
   between report and remarks: make them equal in the copy, append nothing;
6. record both runs; then commit. Commit messages are not checked.
`remarks_check.py` is not changed. I ran the sequence on a small made-up record (scratch, outside the
repository): remarks check on the original exit 0; after one rewriting of the copy, the new script on
the copy exit 0, the remarks check on the copy exit 0, the new script on the original exit 1 with five
hits. So `remarks_check.py` reads a copy (its docstring already says so) and Q1 works as written.

The description: `request_template.md` "Write, check, publish" gets the step 4 (the command, what it
lists, exit codes, "the block in the task document's language included", "commit messages are not
checked"), the publish step requires both checks on each edit (the record-link edit included), and the
*Checks* rule names the private-path check's last run on the description and on the copy, with command
and exit code, and the remarks check's runs on the original and the copy. `SKILL.md` step 13 names both
scripts. `agent-instructions/README.md` gets the command for a change made without a cycle.

**Templates.** `record_template.md`: `Product repository:` no longer asks for a path (the repository's
name or remote address); the remarks entry reads "full report path from the repository's root"; the
closing paragraph points to the new section; `Task source:` is the concern below.

**Foundation (rows 1 and 2).** Two decisions, because the rows answer two questions (what is
published and how it is found), as WAY-286 and WAY-290 are two:
- WAY-308: cleaning in every repository, record copy (all three commits) and description, `Project
  relation:` line unchanged, commit messages not cleaned. Derives from WAY-27. Rejected: the four ways
  not chosen of questions 1 and 3, each with the cost kept beside it.
- WAY-309: the pattern script before each commit of the copy and each publication of the description,
  no list of private words, rewrites nothing. Derives from WAY-308. Rejected: the three ways not chosen
  of question 2.
Both: Scope `task-cycle, agent-instructions` (as WAY-290, since the README gains the command), Based on
`none`, Verification without invariants (no new invariant, as the task says), Origin `none`.
Meaning in English: WAY-308 — the cycle publishes its record and request description only with
absolute paths made relative and private notes described; WAY-309 — a pattern script lists such paths
and note links before each commit and publication, and the cycle corrects what it lists.
Meaning in Polish (task language): WAY-308 — cykl publikuje zapis i opis requestu tylko po
oczyszczeniu: ścieżki bezwzględne zamienione na względne, prywatne notatki opisane zamiast wskazane.
WAY-309 — skrypt wypisuje po wzorcu ścieżki bezwzględne i linki do notatek przed każdym commitem
zapisu i każdą publikacją opisu, a cykl poprawia to, co wypisze. Both rows are `row 1` and `row 2`
entries written whole.

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest test_private_paths_check` (run in `task-cycle/`, after the code and test were written) | 0 | 35 tests OK; a later `python -B -m unittest task-cycle/test_private_paths_check.py` after I removed one weak test (byte-order mark: no pattern depends on it): exit 0, 34 tests OK |
| `python -B gate/run_tests.py task-cycle` (baseline on the base commit, before any edit) | 0 | 151 tests OK |
| `python -B gate/run_tests.py task-cycle` (after the change) | 0 | 185 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` (check mode; no skill description changed, so no `--write`) | 0 | `entry points are current` |

Not run: the full gate (the orchestrator's). `skill_entry_points.py --write` not needed (no skill
added, renamed, moved, nor its description changed).

Test-first: not strictly. I wrote the script and the tests together; no test was first seen failing
against an empty function. In its place I mutated the script (scratch script, file restored after
each run and checked identical to a backup) and every mutation below was caught:

| Mutation | Result of the test file |
|---|---|
| no "not preceded by a word character" on the drive pattern | 3 failures |
| no letter-or-digit rule on the note link | 1 failure |
| no first-character-is-no-space rule on the note link | 1 failure |
| binary files read instead of skipped | 1 failure |
| line end `\n` only | 1 failure |
| no boundary on the Linux/macOS home pattern | 1 failure |
| no boundary on the POSIX drive pattern | 3 failures |
| backslash form of `Users` removed | 1 failure |
| name after the home directory not required | 5 failures |
| drive pattern accepts a slash only | 3 failures |
| macOS or Linux home removed | 2 and 4 failures |
| files not sorted by path | 1 failure |
| directory not read recursively | 2 failures |
| exit code 0 when listed | 3 failures |
| trailing punctuation not stripped from a path | 3 failures |
| `/mnt` and `/cygdrive` removed | 1 failure |

One mutation run at first left the script file with Windows line ends (my scratch script re-wrote it
through `write_text`); I restored it from a byte copy and checked `git ls-files --eol`-style that no
CR is in the three files (`grep -c` of the carriage return: 0 for the script, its test and
`remarks_check.py`). Two earlier mutation attempts did not apply (a literal with doubled backslashes
reached the tool with one) and are redone above.

## Own-work check (WAY-164)

Requirement of the task that the work most likely does not meet: the script "does not list a URL or
ordinary prose" while it lists the drive, home and POSIX-drive forms, and the first *To do* step
("clean the copy, then check it") works with the real `remarks_check.py` (Q1). Checks:
- Ran the script over the tracked text of the repository, directory by directory
  (`elements`, `task-cycle`, `project-level`, `foundations`, `product-guidelines`,
  `foundation-review`, `installation`, `instruction-files`, `agent-instructions`, `gate`,
  `relation-model`): the only hits outside the new script and its test are in
  `instruction-files/check_instructions.py` (a drive root inside a regular expression, 2 hits) and
  `instruction-files/test_check_instructions.py` (a made-up drive path, 1 hit) — code, not prose; no
  URL and no sentence is listed. Command per directory: `python -B task-cycle/private_paths_check.py <dir>`,
  exit 0 for all other directories, 1 for `task-cycle` (own script and test) and `instruction-files`.
- Ran it on the frozen task of this cycle: one hit, the link in its front matter (line 7); the task's
  prose that names the forms (a drive letter, double square brackets) is not listed. Exit 1.
- Ran the Q1 sequence on a made-up record (above): exit codes 0, 0, 0 on the cleaned copy and 1 on
  the uncleaned original.
What the check showed: no false positive on prose in the repository; the order works with the two real
scripts. What it did not show: behaviour on a real archived record of a long cycle (none is in the
tree; the orchestrator's own record is the first real run).

Weakest point: the interaction with the plan-state reader (see Problems 1), and, within my own
scope, the heuristic edges of the patterns (an array index written with two brackets and numbers is listed as a note link; a drive-like
pair in an escape such as an upper-case letter followed by a colon and a backslash-n in a string is
listed). Check made on the second: tests for the cases that must not be listed (URLs, prose with
colons, the shell test, paths relative or starting at a tilde); the two known false positives are
left listed on purpose (a missed leak costs more than one reworded sentence) and the rules say what to
do with a listing of other text.

Each *To do* and settlement: *To do* 1 — SKILL section, steps 12, 9.4, the three side files, the
record template; *To do* 2 — script, tests, template step 4, README; acceptance criterion — the
script exists on this branch and the orchestrator's record and description can be checked by it (not
run on them: the orchestrator's); row 1 — WAY-308; row 2 — WAY-309; Q1 — as ruled; "Out of scope" —
no rewriting mode, no word list, no message check, nothing in the published history touched. Q4/Q5
carried: no guidelines of the product (followed `remarks_check.py` conventions); Q5 is the
orchestrator's act.

## Choices I made (with the way rejected and cost if wrong)

1. **Name `private_paths_check.py`** (the task leaves it to me). Rejected: `private_names_check.py`
   (the script finds no names, only paths and links; the name would promise more). Cost if wrong:
   rename in four files.
2. **One call for a directory or a file** (`TARGET`), not two flags. Rejected: `--record` and
   `--description`. Cost: none known.
3. **Two decisions, not one.** Rejected: one decision with both rows (two questions in one entry,
   against `decide_entry.md`). Cost if wrong: merge them; the identifiers WAY-308 and WAY-309 would
   then be one withdrawn.
4. **`Based on: none`** for both decisions, although the task's *Need* cites the visibility of both
   repositories read on 2026-11-07. Rejected: an environment fact "the repositories are public".
   Reason: the decision cleans in every repository, so it stands whatever the visibility; the
   visibility is the motive, and a motive is no source (the template says so). Cost if wrong: add an
   environment fact through its skill and a `Based on` line.
5. **No change to the invariant `outbound-link-reach`** (its *Derives from* stays WAY-27). Rejected:
   adding WAY-308 to its *Derives from* and naming it in WAY-308's *Verification*. Reason: the task
   asks for no invariant and an invariant edit is more than the task carries. Cost if wrong: the
   decisions' *Verification* names no invariant, as the task allows.
6. **A path outside the repository** becomes "a description of what the place is" (the task says only
   "relative to the repository", which no path outside it can be). Written in WAY-308 and the SKILL.
   Rejected: a relative path that climbs out (`../..`), which still shows the layout. Cost if wrong:
   one clause in both places.
7. **The order of the remarks check and the cleaning** as Q1 ruled; plus the rule that a listing of
   the remarks check on the cleaned copy is solved by making report and remarks equal, appending no
   second entry. Rejected: appending (it would hold the item twice). Cost if wrong: one extra entry
   in the remarks.
8. **Text not a path or link but listed** (a code sample): "write it so the pattern does not list it;
   no listing is left in place". Rejected: a "listing held wrong" variant like WAY-295 (not asked for;
   the text can always be reworded). Cost if wrong: an orchestrator stuck on a sample it cannot reword
   (none seen).
9. **README gets the second command** though the task lists only the cycle's places: the README is the
   route of a the-way change without a cycle, and the same description is published there.

## Reach beyond the handoff

| What | Where | Why |
|---|---|---|
| `project-level/plan_state.py` lines 161-330 | read | to see what the reader needs from the copy (`Task source:`, `Task relation:`, `Project relation:` of the frozen task) before I changed the template line |
| `project-level/task/template.md` (the `Project relation:` form), `project-level/plan/template.md` (the *Document* column) | read | the form of that line and the plan's link to the frozen copy |
| `elements/decisions/template.md`, `elements/decisions/examples.md`, `elements/decisions/skill/{read,decide_entry}.md`, `elements/common/{rules,way_of_working}.md` | read whole | to write the decisions (the skill file is `elements/decisions/skill/SKILL.md`; the handoff's `elements/decisions/SKILL.md` does not exist) |
| `foundations/environment_facts.md` (headings, two entries) | read | to decide `Based on` |
| `foundations/glossary.md` (headings), grep of the foundation for `remarks`, `private`, `task-cycles/` | read | the search of the whole foundation (WAY-33) |
| `task-cycle/request_check.py` (head) | read | conventions of the checks |
| The vault rules `scripts.md` and `git.md` | read | the user's global instructions |
| `agent-instructions/README.md` | changed | see choice 9 |

## Searches not found or unclear

- `elements/decisions/SKILL.md`, named by the handoff as the record-decision skill: not found; the
  skill is `elements/decisions/skill/SKILL.md` (with `read.md`, `decide_entry.md`, `projected.md`).
- Unclear: what the record template's `Task source:` line should ask for. The handoff says it must stop
  asking for an absolute path. But `project-level/plan_state.py` (lines 253-258) anchors the record of
  a plan item to its task by that line's absolute path when it reads a working cycle directory, and a
  line that is no absolute path gives "original Task source or Document cannot be anchored", i.e.
  unchecked, for the invariant `project-plan-state-evidence`. I kept the absolute path in the working
  record and made the committed copy cleaned (see Problems 1).
- Unclear: what to do if the new check lists the `Project relation:` line itself (the line must stay
  unchanged). Its template form is the plan's file name and the task's name, so it should never hold
  an absolute path; I wrote no rule for the case.
- Unclear: how the record of an old cycle already in the history relates to the new rules: out of
  scope by the task; nothing written.
- A decision, invariant or glossary entry that already states the rows: none found (search of the
  foundation for `private`, `remarks`, `task-cycles/`, `absolute path`); WAY-27 and the invariant
  `outbound-link-reach` are the nearest and are not changed.
- A guideline file of the product (coding or testing): none (the task, question 4).

## Problems as observed

1. **`Task source:` and the plan-state reader (concern).** Evidence: `project-level/plan_state.py`
   lines 253-258 (`candidates` come from the record's `Task source:`; with no absolute candidate and
   no linked frozen copy the reader reports "original Task source or Document cannot be anchored").
   Effect on my change: I kept the absolute path in the working record (the reader reads the working
   cycle directory in the worktree, which is never cleaned), and the committed copy, cleaned, names the
   document by what it is. Then, for a plan item whose *Document* cell still holds the original path
   (not yet done), the archived commit gives "unchecked" instead of "owned"; once the task is done and
   the *Document* links the frozen copy, the reader does not need that line (verified in the code:
   `parents` come from the candidates only for resolving a relative plan path; a bare file name works).
   This deviates from the handoff's wording ("the template must stop asking for an absolute path") on
   purpose; the other reading breaks the working-directory proof. I did not run the reader on a cleaned
   copy (no fixture of one; I did not change `plan_state.py` or its tests). The choice is a one-line
   template edit either way. Cause verified by reading the code only; the effect is not run.
2. The first mutation run of a scratch script re-wrote the script with Windows line ends; found when a
   diff showed every line changed; fixed from a byte copy and checked (`grep -c` carriage returns: 0).
   Guess for cause: Python's `write_text` on this machine translates the line end.
3. One of my tool calls printed an incomplete result because a heredoc literal with doubled backslashes
   reached the interpreter with one; the check was redone through a file written by the file tool.
