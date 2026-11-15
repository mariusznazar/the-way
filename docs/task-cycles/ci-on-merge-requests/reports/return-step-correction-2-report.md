# Report: the return step on the final code (correction 2)

**Status:** blocked — one question for the human that the foundation requires (below). Everything else compared matches.
**Commits:** none. I wrote nothing and rewrote no map line: where the foundation sends a mismatch to the human, the return step does not settle it (WAY-225).

## The question for the human (the reason for `blocked`)

What the code holds, in words a reader can follow:

- The CI file of the-way, `.github/workflows/tests.yml:41`, tells the step that installs Python to read the file `.python-version` (`python-version-file: .python-version`). The CI file belongs to the part `agent-instructions` (`foundations/part_map.md`, its *Files* line `.github/workflows/**`, which the task added). `.python-version` belongs to the part `repository` (`foundations/part_map.md:151`, `/.python-version`). The *Depends on* of `agent-instructions` (`foundations/part_map.md:171-173`) does not list `repository`, and no part lists it.
- The README of the installer, `installation/README.md:143` and `:158`, names `.github/workflows/tests.yml` (a file of `agent-instructions`) and `.the-way/.python-version` (a file of `repository`); the part `installation` lists neither part. The same README at `:14` named `.python-version` already on the target branch (`7f5c5a5`), so a mention of this kind existed before the task.

What the foundation says:

- The glossary entry "dependency of a part" (`foundations/glossary.md:37-39`): "any reach of that part to another part of the product: a skill of it that calls a skill or a file of the other, a script of it that reads a file of the other, … a path or a git tag of the other, or code of it that imports the other".
- The part-map template, "Allowed dependencies" (`elements/part-map/template.md:91-111`): "A dependency of a part that the code holds and *Depends on* does not allow goes to the human. Where the human accepts it as it stands, it is written as an invariant — "the part `<part>` does not depend on `<part>`" — that reads `Violated: yes` … *Depends on* is never rewritten to fit what the code reaches for today (WAY-225, WAY-51)." WAY-11 has the return step correct what no longer matches, and WAY-225 forbids the return step from rewriting *Depends on* to fit the code.

Why I hold this as required: the workflow's read of the file is a reach in the glossary's own words (a file of one part names and reads a file of another), the task's change brought it in, and the same template that required the question for `instruction-files` (correction 2, the human's answer (a)) requires it here. Why it is a question and not a settled case: the review of the merge graded the same pair Minor because the target's own tree already names `.python-version` from `installation/README.md:14` without any part listing `repository`, so whether a mention in a README counts is unsettled in the foundation itself (`reports/review-merge-report.md`, finding 3). A prose mention in a README and a CI file that reads a file are different in kind, and I do not decide it for the human.

The question, one decision to make, with the cost of each way:

1. Does the part `agent-instructions` (its CI file reads `/.python-version`) depend on the part `repository`? Recommended: yes, allow it, as with `instruction-files`. Then `repository` is added to *Depends on* of `agent-instructions` in `foundations/part_map.md`, with the citation in the commit message (the map has no field for one). Cost: one line of the map and one commit; the reach is real (the CI job installs the Python the file declares) and the part `repository` depends on nothing, so no mutual allowance arises. If instead the human does not allow it: an invariant "the part `agent-instructions` does not depend on `repository`" reading `Violated: yes` (WAY-225, WAY-51), whose reach is `.github/workflows/tests.yml:41`; cost: a debt record for a reach the task wanted (the CI job needs the file), which the human has just chosen against for `instruction-files`.
2. Do the two prose mentions of `installation/README.md` (`:143` the CI file, `:158` the file `.the-way/.python-version`) count as reaches of `installation` to `agent-instructions` and `repository`? Recommended: no; they describe, and no code of `installation` reads those files, so the map stays as it is and the foundation's own unsettled point (`README.md:14` on the target) stays on the request's list as the review put it. If the human says yes, `installation` takes the two parts into its *Depends on* the same way, or the invariants of "does not depend" are written.

Until the human answers, the map does not match the code at one reach (the CI file to `.python-version`); the cycle decides how the request carries it, as with the earlier blocked item.

## What I compared (range `7f5c5a5..2e83447`, the task's whole change on the target; and `b344595..2e83447` for what has not run)

Reading, by "Reading the foundation" of `elements/common/way_of_working.md`: parts touched: `agent-instructions`, `installation`, `task-cycle`, `instruction-files`, `product-guidelines`, `decisions`, `environment-facts`, `invariants`, `repository` (for the read of `.python-version`). `decision_index.py --sections` then `--section "Scripts and the gate" --section "Environment facts" --section "The part map and derived files"` with `--part` for each touched part: exit 0, 263 lines of index read. `compare_log_entries.py` of the target's log against the final log lists four changed entries: WAY-09, WAY-16, WAY-160, WAY-206. I read whole: WAY-11 (the gap of my earlier report, now read whole), WAY-16, WAY-160, WAY-206, WAY-09 (the changed lines), WAY-225, WAY-51 and the glossary entry.

Compared with the code, each matches:

- WAY-16 (CI runs the one command on every merge request, the product writes its own CI file, the installer writes none, the result is required with a bypass for the owner): `.github/workflows/tests.yml` runs `python -B gate/run_tests.py` on `pull_request` into `foundations` with a job named `tests`; the installer writes no CI file; `installation/README.md` "Run the one command in CI" says the file is the product's and the result a required check with a bypass; the rule exists as read in `foundations-branch-ruleset`. Its *Based on* names three facts, no `TODO`.
- WAY-160 (wait for CI, red result handled as the cycle's gate gives, with WAY-261's exception): `task-cycle/skill/SKILL.md` step 12, `correction.md`, `agent-instructions/README.md`, `request_template.md`, `record_template.md` say the same, as the fix `dcb1a19` made them.
- WAY-206 and the coding settle skill: `product-guidelines/coding/settle.md` carries the proposal of Dependabot alerts and its limit, as WAY-206 says; the fact `github-dependabot-alerts` is named in its *Based on*.
- WAY-09: `.github/workflows/` among the places `agent-instructions` owns: the map's *Files* line and `README.md` (`agent-instructions/` bullet) say so.
- The four GitHub facts (`github-dependabot-alerts`, `github-required-status-checks`, `github-ruleset-bypass`, `foundations-branch-ruleset`) each stand named by WAY-206 or WAY-16 (WAY-73); `foundation_check.py` reports no unnamed or missing fact.
- The part map of the touched parts: `installation` lists `instruction-files` (correction 2) for the guidance, the README and the test that name `check_instructions.py` (settlement 5); `agent-instructions` lists `gate`, `instruction-files`, `task-cycle` and the others its workflow and README reach; `instruction-files` (test change) imports nothing outside its part (`elements/part-map` tests pass); `task-cycle`, `product-guidelines`, `decisions`, `environment-facts`, `invariants` reach only parts they list. The one reach no *Depends on* allows is the one in the question above.
- The invariant `installation-instruction-files-dependency` and its sentence stand nowhere (correction 2).

## Places the settlements went to

- Foundation compared with code: done as above; one question is open (above), nothing else differs.
- Decisions: none written. Invariants: none. Environment facts: none (`foundations-branch-ruleset` was written by correction 1). Glossary terms: none. Part-map changes: none (blocked on the question). Projected entries: none. Rows of *Settlements to record*: none new (the first cycle's return step stands; row 5 went to the installer's block and its part-map allowance by correction 2).
- The Minor findings of the reviews: not fixed (as bound).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) at `2e83447`: `0 errors`, exit 0.
- No file changed, so no directory tests run by this step; the earlier runs on the same tree (`elements/part-map` 39 OK, `elements/common` 235 OK, both exit 0) stand from correction 2. The full gate was not run.

## Unread material

- `reports/review-merge-report.md` was read only at finding 3 and its two nearby passages ("Searches not found or unclear", "Declined to judge"), not whole. WAY-09 was read at the changed lines only, not whole. `elements/part-map/skill/SKILL.md` was not read again (read at line 41 earlier). The `--part`/`--section` index of 263 lines was read by headings and the entries named above; the other decisions in it were not opened.

## Searches not found or unclear

- Whether a prose mention of another part's file in a README counts as a dependency of the part: unclear in the foundation (the glossary's words cover "a path", the target's own `installation/README.md:14` leaves it unlisted); put to the human as question 2.
- Any other tracked file reading `.python-version` or naming `.github/workflows/`: searched with `git grep -n "python-version"` and `git grep -n "workflows"` (`.runs/` and `decisions.md` excluded): only the workflow, `installation/README.md`, `foundations/part_map.md` and `foundations/invariants.md` (the invariant `python-version-declared`, a sentence about the file, not a reach).

## Working copies

`.runs/return-step-correction-2/` held the section list, the decision index and the target's copy of the log (for `compare_log_entries.py`). Removed before return; no remainder.
