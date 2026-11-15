# Report — executor of slice 21 (the general coding guidelines `guidelines/coding.md`)

**Status:** done

**Commit:** `39aaa1ce63e4d7291b92779904031a7a62d99269` on `task/the-way-coding-and-testing-guidelines`
(base `316a6982c2d9bff99379689c441ddd5d4d1ec3c6`): "Write the general coding guidelines of the-way: the
linter, the size of a function and a file, two rules of the whole of the code and the six kinds".

**Files changed:** `guidelines/coding.md`, added, 160 lines (+160, -0).

## What the file holds

- Header: *Discipline* coding; *Applies to* the eleven parts of the Scope of WAY-379 (`elements-common`,
  `part-map`, `relation-model`, `project-level`, `task-cycle`, `gate`, `agent-instructions`,
  `instruction-files`, `installation`, `process-audit`, `product-guidelines`).
- `## When to read`: before any change of the code of the-way; names WAY-379 as the adoption.
- `## Kinds of code`: six rows (kind, `guidelines/coding-<kind>.md`, when to read), the conditions
  taken from the `## When to read` of each kind's file.
- `## Rules`, in the template's order: `### Linter` (WAY-380 · WAY-381, invariant `ruff-blocking-rules`,
  resting on the environment fact `ruff-default-rules`, named in the text); `### Formatter`
  `none — WAY-382`; `### Dependency audit` `none — WAY-383`; the six rules on failures and logs each
  `none — WAY-384`; `### Size of a function and a file` (WAY-385, invariant `function-and-file-size`);
  two further rules, each with the invariant `none`: `### How a script starts and ends` (Decision
  `none`, its reason in one sentence) and `### A field missing from a file a script reads` (Decision
  WAY-344, repeating none of it).
- `## Examples`: one example, a table of the 18 rules (code, name as `ruff rule <code>` gives it,
  what it checks for, the last taken from the tool's own text for the rule).
- `## Where in code`: `ruff.toml`, the two requirement files, the two tests of the standing checks
  and the nine directories of the code of the kinds.

No value is copied: no version of the tool, no threshold, no count of rules, no `target-version`
(grep for `0.17`, `py314`, `80`, `1000`, `18`, `389`, `407`, `WAY-328`, an absolute path: no hit).

## Checks run (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` (prints `0 errors`) | 0 |
| The 18 names | `python -B .runs/executor-21/check_names.py` — for each of the 18 rows runs `ruff rule <code>` of the main checkout's ruff 0.17.1 and compares its heading with the code and the name written in the file; also that none of the 18 is in the `select` of `ruff.toml` (18 rows found, 0 mismatches) | 0 |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (`checked: 322 files, 0 listed`) | 0 |
| Instruction check | `python -B instruction-files/check_instructions.py . --file guidelines/coding.md` (`0 error, 0 warn, 4 info`; the one info line about the file is its size) | 0 |
| Every WAY-NN in the file is an entry | grep of the identifiers (WAY-16, 203, 344, 361, 365, 379, 380, 381, 382, 383, 384, 385) against `^### WAY-NN ` of `foundations/decisions.md` | no missing |

No test was written and no invariant's test is changed by this slice, so there is no failing run to
record. The full gate was not run (WAY-160); the handoff's *Checks* does not name it.

**Mismatch with the handoff's check:** the *Checks* line `python -B instruction-files/check_instructions.py
guidelines/coding.md` gives exit code 2 (`Error: ROOT is not a directory: guidelines/coding.md`), since the
script's first argument is the root. I ran it as `check_instructions.py . --file guidelines/coding.md`,
exit 0. The root `AGENTS.md` does not name the file, so a plain run on the root does not follow it.

## Own-work check (section 3)

- **Requirement most likely not met:** "No value is copied from a configuration file or a decision, and
  every reference names an entry the foundation holds", with no text naming WAY-328 (the rules of
  WAY-312 and of the template of guidelines). The sentence of the Linter rule saying how the rules that
  block are taken ("from `ruff-default-rules`, less the rules under `## Examples`") and the sentence of
  the size rule on what is counted come nearest to repeating a decision.
- **Check:** a grep for every value of WAY-380, 381, 385 and the configuration (versions, `py314`, 80,
  1000, 18, 389, 407) and for WAY-328 — no hit; `foundation_check.py` exit 0 for the references; the
  names of the 18 against the tool, exit 0. What it showed: no value is copied. Whether the two
  sentences above are "repetition" is a judgement only a reading gives; I kept them as instructions for
  the author (what the invariant reads, what is counted) and left the thresholds, the exceptions, the
  set's membership and the way of the split to the decisions.

## Choices (with the way rejected and the cost if wrong)

1. **The `Name` and `What it checks for` columns of the 18 rules** come from the output of
   `ruff rule <code>`, not from memory. Rejected: a bare list of codes, which gives the reader no hint of
   what the rule is. If wrong: a summary a reviewer finds too long for an example "nothing here binds".
2. **`### How a script starts and ends` names a function `main`** that returns the exit code, called as
   `sys.exit(main())`. The settlement (answer 12) says "one fixed place of start that returns the exit
   code" and names `main` only in "install.py without `main`". Rejected: leaving the shape of the place
   open. If wrong: the human meant another form and the rule's text and Good line are corrected.
   Note: `relation-model/fingerprint.py`, the exemplar of the shared module, has no `main`, so the rule
   as written reaches it; no invariant checks it and the settlement lists 8 files that break it.
3. **`## Where in code` lists nine directories** (the union of the directories the six kind files list),
   reading the plan's "the directories of the kinds" so. Rejected: `guidelines/` alone, which holds
   the kind files but not the code. If wrong: a reviewer wants only the guidelines directory, and nine
   lines go.
4. **The Linter rule's text carries one conditional sentence** about the invariant reading `Violated: yes`
   (the test is then an expected failure and shows no report returning), taken from the weak point of
   WAY-205. Rejected: leaving it out, which hides from the author why the review has to look. It states
   no state, only a condition. The same for the rule of size.
5. **The size rule holds Good and Bad lines** (the template proposes none); they come from the price
   named in WAY-385 (a function divided only to stand under a threshold). Rejected: `none`. If wrong:
   a reviewer finds them a guess, and they become `none`.
6. **The rule on a field missing from a file has Good and Bad `none`**, since a use that follows it would
   repeat WAY-344. The *Invariant* `none` for both further rules as the plan gives.
7. **WAY-365 and WAY-361 are named in the rule of size** (a change that adds to code over a threshold
   begins with a move out; no command of its own that counts sizes). Both are cited in WAY-385 and the
   template's text of the rule; rejected: no reference to them, which leaves the author of a change
   without the step WAY-365 gives.

## Reach beyond the handoff

- `foundations/decisions.md` WAY-365 (whole, lines 6197 to 6232) and WAY-379 to WAY-391 (whole): WAY-365
  because the size rule's text cites it, WAY-379 to WAY-391 because E1 to E8 are those entries.
- The four kind guidelines files written by earlier slices (`guidelines/coding-generator.md`,
  `-repository-changer.md`, `-command-runner.md`, `-shared-module.md`, `-measuring-report.md`,
  `-check.md`) and `agent-instructions/test_linter_invariant.py`, `test_size_invariant.py` (headers and
  the lines that cite the invariants), `requirements-quality.in`, `relation-model/fingerprint.py`,
  `task-cycle/tracked_private_paths_check.py` (head), and `elements/common/foundation_check.py`
  (`check_guidelines`): for the kinds table's conditions, the names of the two tests, the form of `main`
  and what the check reads of a guidelines file.
- `plan.md` from line 1003 to the end (the *Choices* and the orchestrator's additions), which the
  handoff says binds.

## Working copies

`.runs/executor-21/` held `check_names.py` and the output of the instruction check. It was removed
before the return (`rm -rf`); nothing remains.

## Unread material

- E37 (`ruff-default-rules`): read only the first line of its sentence and the start of its source; the
  list of 407 codes was not read through (its use here is the name of the fact; the 18 names were checked
  against the tool, not against the fact).
- E17 (the withdrawal of WAY-328): seen as the row of the table of withdrawn identifiers in
  `foundations/decisions.md` (line 10477), not read as an entry; the file names WAY-328 nowhere.
- E16 (WAY-09) and E20 (WAY-38), named by the handoff's table of identifiers but not in the *Read* of the
  slice: not read beyond the first lines of WAY-09.
- WAY-16, cited in the Linter and size rules from WAY-361 and WAY-381: not read; its title and content
  were taken from those two decisions' own use of it.
- Invariants read whole: `ruff-blocking-rules`, `function-and-file-size`, `tracked-file-private-paths`,
  `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`,
  `repository-file-location`, `ci-checking-commands`, `guidelines-file-place`, `map-reference-target`,
  `derived-file-content`, `generator-writes-only-with-write` (and the next three of its block, the first
  lines). The task's passages were read at the ranges named (27, 59–61, 66–70, 72–147, 203–207, 514–532).
  `product-guidelines/reading.md`, `product-guidelines/template.md` and
  `product-guidelines/coding/template.md` were read whole. The other files named in the handoff were read.

## Searches not found or unclear

- The handoff's check `check_instructions.py guidelines/coding.md` is not a valid form of the script's
  arguments (see above); the form I ran is named there.
- The plan's "the directories of the kinds" in `## Where in code` is ambiguous (the directories of the
  code of the kinds, or the directory of the kind files); I took the first (choice 3).
- The settlement of answer 12 does not say that the place of start is named `main`; I wrote it so on the
  ground of the one mention in the same answer (choice 2).

## Addendum — correction of the orchestrator on the rule of the place of start

The orchestrator's choice, not the human's approval. In `guidelines/coding.md`, the rule
`### How a script starts and ends` now reads "Each script that is started from the command line opens
with ..." and holds one added sentence: "A file of the kind `shared-module`, which is only imported, has
no place of start, and this rule does not reach it." No invariant is added; the rest of the file is as
it was. This settles choice 2 above for `relation-model/fingerprint.py`: the rule no longer reaches it.

**Commit:** `6fd60efda6773fb942509ebd4243ce2e76470e51` ("Limit the rule on the place of start of a
script to a script started from the command line"); `guidelines/coding.md` only, 7 lines added and 5
removed (the paragraph reflowed).

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` (`0 errors`) | 0 |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (`checked: 323 files, 0 listed`) | 0 |
| Instruction check | `python -B instruction-files/check_instructions.py . --file guidelines/coding.md` (`0 error, 0 warn, 4 info`) | 0 |

The three ran twice, before and after the reflow of the paragraph, all with exit 0. The names check of
the 18 rules was not rerun: the table is unchanged. No working copy was made.
