# Report of the return step — ci-on-merge-requests

**Status:** `done`. One commit after `23f08e9`; its hash is in the return line below and
`git log --format=%h 23f08e9..HEAD` gives it. A fresh reviewer reviews that range.

Read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`. The glossary
skill was not followed, since no term is written. Method for the commit: `task-cycle/change/SKILL.md`.

## Foundation compared with code

Compared, each against the files of the head `23f08e9`:

- **WAY-16** (two sentences, *Scope*, *Relations*, *Based on*, *Verification*): the CI file runs
  `python -B gate/run_tests.py` and no other checking command on every pull request into
  `foundations`; the installer writes no CI file; the README of the installer gives the description
  with the pinned `.the-way`, the history, the required check and the bypass; the block names the
  bypass. Matches.
- **WAY-206**: `product-guidelines/coding/settle.md` proposes the alerts beside the audit and names
  them among the weak points; the skill turns nothing on. Matches. The *Rationale* rests on
  `github-dependabot-alerts`, named in *Based on*.
- **WAY-160**: step 12, step 9 sub-step 4, `correction.md`, `blocked_finding.md`,
  `reserved_return.md`, `request_template.md` and `record_template.md` say what the sentence says
  (wait on each head of a request with finished code, a correction's included; red is a failed gate;
  a request blocked for unfinished code is not waited for; the CI row stands in the original record).
  Matches. The two blocked variants of the template's table named in the fix report rest on the
  sentence's "unfinished code".
- **WAY-09** and the part map: `.github/workflows/**` is a pattern of `agent-instructions`, which WAY-44
  gives CI configuration to; `foundation_check.py` assigns the file and reports no pattern that
  matches nothing. Matches. The sentences of the `installation`, `task-cycle`, `product-guidelines`
  and `agent-instructions` parts and the surfaces `installation-command` and `test-runner-command`
  stay true: the installer's promise (which files it touches) did not change.
- **The decisions the task names:** WAY-34 (the pinned commit; the description and the block say it;
  no CI of the-way fetches a later the-way) and WAY-133 (the change adds no rule of an instruction
  file without a mechanism: the sentences added to `agent-instructions/README.md` state what is, and
  the mechanism of the wait stands in the cycle's skill). Match, no change.
- **Invariants:** `ci-checking-commands`, `repository-file-location`, `python-version-declared`,
  `script-language`, `script-subprocesses` still read true of the head.
- **The three environment facts** (`github-dependabot-alerts`, `github-required-status-checks`,
  `github-ruleset-bypass`): each is named by WAY-206 or WAY-16, so none stands unnamed.

One mismatch found and corrected in this step: `installation/README.md` said that the required check
"on GitHub is named by the job's name", a claim about the host that no decision rests on (the page
that says it was read in the fix and no fact was written for it, since a fact stands only while a
decision or an invariant names it). The clause is removed; the sentence now reads "Give the job a
name that stays: the rule names the check." The workflow's comment (`.github/workflows/tests.yml`)
says only that the branch rule names the job's check, and asserts nothing of the host.

## What the step writes

- **Decisions written or changed:** none in this step (WAY-16, WAY-206, WAY-160 and WAY-09 were
  written by the foundation step and its fix; compared above).
- **Invariants written or changed:** none. The task and the decisions set no rule beyond what
  `ci-checking-commands` holds; a test of the workflow's text was weighed in the first report and
  not written, since no decision and no human asks for it.
- **Environment facts:** none new. Sources outside the product that the change rests on and the
  foundation does not hold: none remain. `actions/checkout` and `actions/setup-python` inputs (read at
  the pinned commits in the first turn) and the `pull_request` / `pull_request_target` advice and
  `submodules: true` / `fetch-depth: 0` in the README's description are examples in the workflow and
  in a description for people; no decision or invariant rests on them, so no fact stands for them
  (WAY-73, WAY-90: a fact stands only where something names it).
- **Glossary terms:** none. "CI", "merge request", "required check" and "bypass" are used as a reader who
  knows the field takes them (WAY-95); no sentence of the change reads otherwise for that reader.
- **Part-map changes:** none in this step (`agent-instructions` gained `.github/workflows/**` in the
  foundation step; compared above).
- **Projected entries written whole or in part:** none; the task projects none.
- **Rows of *Settlements to record* written:** row 1 and row 2 as sentences of WAY-16; row 3 as the
  comment of `.github/workflows/tests.yml` (Linux, why, and that Windows is checked by the cycle's
  gate); row 4 as the sentence of WAY-206; row 5 as the paragraph of `product_guidance` in
  `installation/install.py` (with its tests); row 6 as the sentence of WAY-160. Each stands where its
  *Goes to* column names it. The code makes true no row and no projected entry that the foundation step
  missed.

## Choices that bind after the merge (WAY-36, WAY-11, WAY-134)

Each is placed by the questions of the decisions template ("Where it goes"); a choice gets an entry
only where the template says the log:

| Choice | Place | Entry written |
|---|---|---|
| The CI file belongs to `agent-instructions` | the part map (WAY-44 already gives CI configuration to that part) | the part-map pattern, written by the foundation step; no decision |
| The description for products stands in `installation/README.md`, section "Run the one command in CI" | the part `installation`'s own README, which holds how a product uses the pin; the block points to it and a test holds that the section exists | none; a row of the questions table |
| Actions at commit SHAs, `persist-credentials: false`, `concurrency` cancelling an earlier run, `timeout-minutes: 40`, `python-version-file` | one text or number of the code, with its comment (template question 3) | none; the comment of the workflow says why for the pins; a row of the questions table |
| A request blocked for unfinished code is not waited for | already a sentence of WAY-160 and the cycle's skill files | none further |
| The block's fallback sentence names both checks and the missing CI file | the instruction text of the installer (template question 1: it stands in one skill or instruction file) | none; row 5 of the task covers it |

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` → exit 0 (`0 errors`), before and after the commit.
- `python -B gate/run_tests.py installation` → exit 0 (61 tests, OK; run after the README edit).
- Not run: the whole gate; other directories (the commit touches `installation/README.md` only).

## Commit

- One commit after `23f08e9`: `installation/README.md`, one clause removed (1 line changed). No other
  file changed.

## Working copies

- `.runs/return-step/` (one edit script): stood there, removed. Remainder: none.

## Unread material

- Decisions of the scopes beyond those named in this and the earlier reports: unread (WAY-128 to WAY-132,
  WAY-287 to WAY-289 were read only as far as the first turn's search; WAY-84, WAY-90, WAY-287, WAY-263,
  WAY-309, WAY-95 were read whole in the fix and here).
- `elements/glossary/skill/SKILL.md`: not read (no term written).

## Searches not found or unclear

- none
