PASS 58997107c8055623854327a28a4e55f1a46553e1

Review of correction 1, made for the human's remarks on the open request (`review-change` with
`fix.md`, the remarks in place of a findings file). Range
`2cbeb15bf9eda28476630cc97e58bb3b0011e1be..58997107c8055623854327a28a4e55f1a46553e1`, one commit,
two files; `git rev-parse HEAD` in the worktree is `58997107c8055623854327a28a4e55f1a46553e1`.

## Each remark

- **Remark 1 (the walk through the five commands) — let through by the human; nothing to make.**
  The correction changes nothing for it, as the remark asks.
- **Remark 2, first item (the executor's sentence) — made.** `task-cycle/change/slice.md:14-16`, a
  new item of "Read": "The dispatch lists the tests the plan leaves failing at your slice's base,
  with their owners: report a listed test that fails as expected, not as a failing check of your
  slice, and do not make it pass outside your slice's *Change*." It holds both parts the remark asks
  for (reported as failing as expected, not as a failing check; not made to pass outside the slice's
  *Change*). The remark allows `slice.md` "and/or" `SKILL.md` §3; `slice.md` is the file the
  executor of a slice, and only it, reads (`task-cycle/change/SKILL.md:24`, the variant row), and §3
  of `SKILL.md` stands in it for a slice (`:134`). It agrees with WAY-136 ("the failure of a test so
  named is no failing check of the slice that meets it"), with step 9 sub-step 4 of
  `task-cycle/skill/SKILL.md`, which retries no listed failure, and with `task-cycle/skill/planning.md`
  ("A slice's handoff"), which makes the dispatch carry the list the sentence names.
- **Remark 2, second item (the idiom in the comment) — made.** `instruction-files/check_instructions.py:456`
  now reads `# text in quotation marks, such as '\'' of a shell, is no path`.
- **Remark 2, third item (the count of the `info` cases) — made.** The module docstring
  (`:12-20`) now says "Four cases" and lists them: a path in a sentence that says it does not load or
  exist; in a file given with `--file`, a name of one part that does not resolve; in a file of the
  repository, an absolute path outside the repository and the home directory; in a file of the
  repository, a relative path under a name of the root `.gitignore`. These are the four branches of
  `dead_path_note` that return `info` (`:604-627`); the network path, also noted as `info`, is told
  apart earlier in `check_dead_paths` and is described on its own in the docstring (`:37-46`), so it
  is no fifth case of "a path in backticks that names nothing".
- **Remark 3 (WAY-02 read whole, point 9 checked against it) — done; see the section below.** The
  correction changes no file for it, and none needs changing.

## WAY-02 and point 9

I read WAY-02 whole (`foundations/decisions.md:458-502`, heading to the next heading, with its
*Rationale* and *Rejected*).

**What WAY-02 binds.** Every entry has a permanent identifier, and whatever depends on an entry —
entries, tests, documents, code comments — refers to it by that identifier alone, with no
fingerprint and no version, naming an entry the foundation holds. The one reference that carries
more is the line `decision:` of a test that holds a sentence of a decision: the number and, in
straight double quotation marks, the start of "that sentence" — from where a sentence of the entry
begins, three words or more, compared with runs of whitespace made single — so that a test whose
sentence was reworded is found; anywhere else a decision is named by its number alone. Its
*Rejected* refuses the number alone in the line of a test, and numbered sentences as a suffix of the
number.

**Point 9's two edits against it.**
- `task-cycle/change/SKILL.md:79-81` (the new item after "Name the break each test catches"): a test
  whose break is code going against a sentence of a recorded decision holds that sentence and carries
  the line `decision:` the template gives; a test that only stands on the sentence holds nothing of
  it. It says *which* tests carry the line and sends the form to the template; it changes nothing of
  the form WAY-02 settles. It stands with WAY-02.
- `elements/decisions/template.md:282-283` (the clause after "The line stands at the test that holds
  the sentence"): "each test that holds a part of the sentences carries a line of its own, and a test
  that holds sentences of several decisions carries one line for each". The template's item keeps,
  before it, "one decision number" and "one quotation" per line, the quotation beginning at a
  sentence start and holding three words or more — WAY-02's form. The clause adds that the line is
  per test and that a test holding sentences of several decisions has one line per decision. Neither
  goes against WAY-02: no line carries two numbers, a version, a fingerprint or a suffix, and every
  line still quotes the start of a sentence the test holds. It leaves WAY-02 holding.
- One reading of the clause is loose; see the Minor finding below.

**What the whole change does against it.** The whole change (`2a2f4106..58997107`) adds two lines
`decision:`, both in `elements/common/test_decision_index.py` (fix 1): `# decision: WAY-344 "Each
reading of a file that the rule covers has one test"` and `# decision: WAY-344 "A script of the-way
that reads a file an agent or a human writes checks"`. Each gives the number alone, a quotation in
straight double quotation marks of three words or more, starting at a sentence of WAY-344's binding
sentences (the second at the start of the binding sentences, the first after a full stop and a space
in its second paragraph), and each stands at the one test that holds that sentence. No line
`decision:` is removed or changed, and the foundation check, which checks these lines against the
log, reports `0 errors` on the head. Nothing of the change goes against WAY-02.

## Findings

### Critical

none

### Important

none

### Minor (within the task's scope)

- `elements/decisions/template.md:282-283`, the clause of point 9 "and a test that holds sentences of
  several decisions carries one line for each": "each" can be read as each decision, which leaves a
  test that holds two sentences of one decision with one line and one quotation. WAY-02 and WAY-12
  give the line the start of "that sentence" — the sentence the test holds — so that a reworded
  sentence is found; a second sentence held with no line of its own is not found when it is
  reworded. The wording is the human's, accepted word for word in the task's point 9, so this is
  named, not a defect of the correction; a reader who reads "each" as each sentence held, as WAY-02
  does, reads it right. Evidence: the line itself against WAY-02 `:466-470`.

### Out of scope

none

## Declined to judge

none

## Checks

| Check | Command or method | Result |
|---|---|---|
| the correction changes only a comment and a docstring of `check_instructions.py` (trust boundary) | the file at `2cbeb15b` and at `58997107` parsed with `ast` with every docstring taken out and compared by `ast.dump` (a script of mine in `.runs/review-correction-1/`) | identical (exit 0); control: the same comparison of the file at `ae37fca3` with the head's differs (exit 1); the module docstrings differ, as the remark asks |
| tests of the instruction check | `python -B -m unittest test_check_instructions` in `instruction-files/` of a worktree of the head | exit 0, 122 tests, 5 skipped |
| linter and formatter | `python -B -m unittest test_linter_invariant` in `agent-instructions/` | exit 0 |
| instruction check on the-way (WAY-418) | `python -B instruction-files/check_instructions.py .` | exit 0, `0 error, 0 warn, 5 info` |
| foundation check, the lines `decision:` among it | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| the comment of remark 2 | line 456 of the head's file | `such as '\'' of a shell` |
| test directories the correction reaches | `python -B gate/run_tests.py task-cycle`, `… agent-instructions`, `… product-guidelines` | exit 0 each: 570, 53 and 14 tests |
| the lines `decision:` of the whole change | `git diff 2a2f4106..58997107`, the added and removed lines holding `decision: WAY` | two added, none removed or changed |
| sizes | `python -B task-cycle/change_file_sizes.py 2cbeb15b 58997107` | exit 0; `check_instructions.py` 1007 → 1009, `task-cycle/change/slice.md` 23 → 26 |

## Reaches beyond what the handoff names

- `elements/decisions/template.md:268-292` ("Verification") and `task-cycle/change/SKILL.md:72-86`,
  `:24` and `:134`: the two edits of point 9 and the place of `slice.md`, read for remark 3 and the
  first item of remark 2.
- `instruction-files/check_instructions.py:1-60` and `dead_path_note`: to count the `info` cases.

## Working copies

My directory was `.runs/review-correction-1`,
holding a git worktree `head` at `58997107`, the two copies of `check_instructions.py` and the script
that compared them, and the outputs of my runs. Removed: the worktree with `git worktree remove
--force` by its full path, then `git worktree prune` (each exit 0), then the directory by its full
path (exit 0; it no longer exists, and `git worktree list` names no copy of this review). No
remainder. No probe shows a finding, so nothing is kept in `reports/`.

## Unread material

none — the handoff, the remarks, the author's correction report, `task-cycle/review/fix.md` (read in
the review of fix 1, unchanged since), the correction diff and WAY-02 were read whole; the frozen
task was read whole in the review of the whole change and its point 9 again here.

## Searches not found or unclear

none
