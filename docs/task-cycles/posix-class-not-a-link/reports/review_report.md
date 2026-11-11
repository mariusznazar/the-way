PASS 8fa6bac2a7af84c73f54d7c8320c9077592f955b

# Review of the whole change: posix-class-not-a-link

Range `e1726b78ad357791c5f84dd946f0edd26cdc3fe8..8fa6bac2a7af84c73f54d7c8320c9077592f955b` (one commit). `git rev-parse HEAD` in the
worktree prints `8fa6bac2a7af84c73f54d7c8320c9077592f955b`, the head given. No plan, no spec: one author's change.
Reviewed read-only; the only files I wrote are probes in the scratchpad, outside the repository.

Counts: blocking 0, Minor 2 (1 within the task, 1 outside it), out-of-scope 1 (the Minor outside the task).

## Changed files

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` (WAY-323 only) | 26 | 10 |
| `task-cycle/private_paths_check.py` | 14 | 7 |
| `task-cycle/test_private_paths_check.py` | 29 | 0 |
| `task-cycle/test_tracked_private_paths_check.py` | 9 | 0 |

## Against the task

- To do 1 (stop listing `[ [:name:] ]`, twelve names, in every check that looks for a link): met. The exception is a negative
  lookahead `(?!POSIX_CLASS)` inside the shared `NOTE_LINK` (`task-cycle/private_paths_check.py:75-82`), and `FINDING`, used by
  the cycle-record copy, the request description and `tracked_private_paths_check.py` alike, builds on it. Exactly the twelve
  names, case-sensitive, closing colon required. `[ [:other:] ]`, `[ [:alphanumeric:] ]`, `[ [:Space:] ]`, `[ [:punct:x] ]`,
  `[ [:alpha:|x] ]` stay listed (probes below and `PosixClassTest`).
- To do 2 (a real link and a path on a line with a class stay listed): met. `PosixClassTest.test_a_real_link_and_a_path_on_a_line_with_a_class_are_still_listed`
  asserts the path, `[ [Notatka] ]` and `[ [(P) Loop] ]` on one line with `[[:alpha:]]`; my probe line 5
  (`[[:space:]][ [Real] ]`) lists `[ [Real] ]`.
- Question 1 (narrow, twelve names): met as answered; the not-chosen ways are recorded in WAY-323 *Rejected* with their cost.
- Question 2 (shared list of patterns, everywhere): met as answered.
- Question 3 (does not wait for guidelines): WAY-328 covers `task-cycle`; the change waited for nothing; the-way has no
  `guidelines/` directory, so there was no guideline file to read or compare.
- Settlement row 1: the change edits WAY-323 in place. The binding part says the twelve names, the shared list is the
  mechanism (the code), and every other `[[...]]` with a letter or digit stays listed (stated in *Verification* and in the
  docstring). Sources of the settlement (pytania 1 and 2) are followed with nothing invented; the one number the author
  added to *Rationale* ("twelve such texts", 2026-11-11, "one product") matches the task's Need and Context. The entry keeps
  two binding sentences (limit three); fields *Scope*, *Based on*, *Relations*, *Origin* unchanged and still true.
  `python -B elements/common/foundation_check.py` reports 0 errors. The entry's own text, which writes `[[:space:]]` in
  backticks, is now not listed by the check (before: 3 hits, per the author; I confirmed 0 now through the invariant run).
- Nothing added that nobody asked for. `part_map.md` needs no change (`task-cycle/**` already covers the files, none is new),
  and the invariant `tracked-file-private-paths` already cites "WAY-309 and WAY-323" and is unchanged, as is its test.

## Against the foundation

- WAY-323 now says what the code does: the code lists the same twelve names the entry lists, in the same words, and the
  docstring (`private_paths_check.py:27-34`) agrees. No restatement more broadly or without a qualification found
  (WAY-263).
- WAY-308, WAY-309, WAY-324 (read whole): the change keeps the script pattern-only, standard library alone, no list of private
  words, no rewriting (WAY-38, WAY-309); the shared patterns keep WAY-324's "same patterns over tracked files" true. The
  tracked-files run on this tree lists 0 of 275 files.
- WAY-328: the departure from coding and testing guidelines is on record for `task-cycle`; nothing for me to compare against.
- No reserved choice is taken (Python standard library only, `re`).

## Tests

- `PosixClassTest` tests every one of the twelve names (a loop with the name as the failure message), shell-command lines
  (`grep -v -E "^[[:space:]]*#" "$file"`, `tr -cd '[[:alnum:]]' < x`), four wrong-name texts that must stay listed
  with their exact `(line, kind, text)` tuple, and the mixed line. They assert literals, not a value computed by the code.
  The new tracked-files test (`test_tracked_private_paths_check.py:91-98`) goes through the command and its output, with
  the class in a Markdown file next to a real link.
- Do they fail when the behaviour breaks? The author recorded them failing on the old code (3 failures, and the command
  test failing); the pattern is a single lookahead, so removing it makes the first, second and fifth tests fail
  (I read the tests against the regex; I did not mutate the file, since the worktree is read-only for me).
- `test_a_caret_before_a_class_in_one_bracket_is_no_link` passes on the old code too (no `[ [` in `[^[:space:] ]`); it
  protects against a future over-broad pattern rather than the change itself. Not a defect.
- No test at the level of the record directory or the request description file (`main` with a directory). The shared
  `find_in_text` is the only path both take, and the author ran the directory run by hand (own-work check); judged enough.
- The own-work check names the right weakest requirement (the exception in every check, and a real link and a path
  on the same line staying listed), and its check would catch it unmet.

## Findings

### Critical

none

### Important

none

### Minor

1. Within the task. `foundations/decisions.md`, WAY-323 *Rationale*, the sentence "Each of the twelve names is kept to, not matched by a
   pattern, so a text with another name between the colons stays listed": the code does match them by a pattern, an
   alternation of the twelve names (`POSIX_CLASS`). What the sentence means is that the names are listed one by one, not
   matched by a general shape such as `:[a-z]+:`. A reader could take it for a statement about the code and find it false.
   Reword to "The twelve names are listed one by one, not matched by a general shape, ...". Grade Minor: the binding
   sentence and *Verification* are right; only a clause of the rationale is loose.
2. Outside the task (out of scope). `task-cycle/private_paths_check.py:82`: `[ [[:space:] ]` (a bracket expression
   holding `[` and a class, which a shell regex can contain) is still listed as the note link `[ [[:space:] ]`: the first
   `[[` is followed by `[`, not by `:`, so the lookahead does not apply. Probe: line 1 of my probe file lists it. The task defines
   the exception as exactly `[ [:name:] ]`, and the same text is listed by the old script, so this is not a regression; it is
   a different text from the one the task names, with no sign it occurs in the 12 hits of the source product. Mention only.

### Out-of-scope findings

Finding 2 above.

## Declined to judge

- Further POSIX or GNU class names the shells accept (`word`, `ascii`): the human settled exactly the twelve names (pytanie 1).
- The loop2 side (moving the pin, removing the expected failure, `Violated: no`): listed as out of scope by the task.
- The long lines (over 100 characters) the change adds in `foundations/decisions.md` and one test: the files already hold
  hundreds of such lines and no rule checked by the form check or the gate rejects them.
- Glossary entries for "note link" or "character class": the author found none; no sentence of the change would be read wrongly for lack of it.

## Checks I ran

| Command (from the worktree root) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `8fa6bac2a7af84c73f54d7c8320c9077592f955b` |
| `git diff e1726b7 8fa6bac` and `--numstat`, `git log` | 0 | 4 files, counts as the table |
| `python -B gate/run_tests.py task-cycle` | 0 | 263 tests, OK |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | `checked: 275 files, 0 listed` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py <scratchpad probe dir>` with 11 probe lines | 1 | listed: `[ [[:space:] ]` (line 1), `[ [Real] ]` (line 5), `[ [:alpha:|x] ]` (8), `[ [:ALPHA:] ]` (9); not listed: `[[:space:][:alpha:]]`, `[[:alpha:]_]`, `[[ $x =~ [[:space:]] ]]`, `[[:space:]]]`, `![[:digit:]]`, `[[:space:]]x[[:space:]]`, `[[:space:] ]]` |
| `git status --short` after the checks | 0 | clean |

The probe file is `a probe file in the session's scratch directory`.
Not run: the full gate (the cycle's own run); the other test files of the author's list, which the `task-cycle` run covers.

## Each reach beyond the dispatch

- `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`, whole: the skill the handoff named and the file it names for this review.
- `elements/common/way_of_working.md` "Reading the foundation" (lines 59-99): to select the foundation entries (section 1).
- `foundations/decisions.md`: a search of *Scope* for `task-cycle` found 112 decisions; the entries named below were read whole by their heading.
- `foundations/invariants.md` `tracked-file-private-paths` and `foundations/part_map.md` `task-cycle` entries, whole.
- `grep` for `NOTE_LINK`, `private_paths_check`, the rule's prose (`[[ -f`, "letter, a digit, a dot") in `task-cycle/skill`, `installation`,
  `agent-instructions`, `elements`: to confirm no other text restates the rule and is now wrong. None found. `installation/README.md`
  and `task-cycle/skill/SKILL.md` were located by search only, not read.
- A line-length count with `awk` on the changed files, to judge the long lines.

## Unread material

- Decisions: 7 read whole (WAY-308, WAY-309, WAY-323, WAY-324, WAY-328, WAY-38, WAY-89) and 105 by title only, of the 112 whose *Scope* names `task-cycle`.
  I opened none of the 105 beyond the title; none of their titles points to a bearing on this change except those below.
- Decisions that bear on the change and stayed unread: WAY-320 (where a user keeps places the files of the-way name; the task's source is
  the same locations file, but the change does not touch it), WAY-263 and WAY-161 (grading rules; the skill states the grades I used),
  WAY-33 and WAY-07 (the author's search and in-place edit rules; I judged the result of the foundation step, not the step),
  WAY-71 (form of an entry; the form check reports 0 errors), WAY-164 (the author's own-work check; I judged the check from the report
  against section 2).
- Guidelines: none exist in the-way (no `guidelines/` directory); WAY-328 records the departure.
- Glossary: searched by the author, not read by me.
- `task-cycle/skill/SKILL.md`, `installation/README.md`, `agent-instructions/README.md`: located by search, not read (see above).
- The author's `private_paths_check.py` source was read in part (the docstring lines 1-60 and the pattern lines of the diff with their context from
  `git diff`); `tracked_private_paths_check.py` and the rest of both test files not read whole.

## Searches not found or unclear

- The two files in `task-cycle/skill` the author said describe the rule (`request_template.md`, `SKILL.md`): I did not confirm by reading that nothing
  there restates the exception; the `grep` for the rule's prose found no match.
- Whether the 12 hits of the source product were all `[[:space:]]`/`[[:alpha:]]` or also other of the twelve names: the task says "all that class"; unverified
  here (outside the repository).
