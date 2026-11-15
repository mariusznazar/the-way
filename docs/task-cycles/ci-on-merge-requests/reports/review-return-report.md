PASS b3445959f103234a8a56347e8ff2190948a3156b

# Review of the return step's commits — ci-on-merge-requests

Range `23f08e9..b344595`; `git rev-parse HEAD` is `b3445959f103234a8a56347e8ff2190948a3156b`. One commit
(`b344595`), one file, `installation/README.md`, one line: the clause ", which on GitHub is named by the
job's name" removed from "Give the job a name that stays: the rule names the check." Nothing else
changed (`git log --stat`, `git diff`; the worktree's `git status` is clean).

## Findings

None (Critical: 0, Important: 0, Minor: 0). Blocking: 0. Out of scope: 0.

## What I checked and what it showed

1. **Does the commit do what the return step requires** (`task-cycle/skill/return_step.md`)? The step
   compares the entries the change writes or touches with the code and corrects what no longer matches;
   writes an environment fact only for a source outside the product that the change rests on and the
   foundation does not hold; and writes no entry that is not needed. The commit corrects a claim about
   the host in the installer's README. WAY-73 says a fact stands only while an invariant's *Rests on* or a
   decision's *Based on* names it, so a clause that no entry rests on needs no fact; removing the
   clause is the form that rule gives, and the alternative (writing a fact no one names, which WAY-73
   forbids) is the wrong one. The sentence that stays still gives the instruction a product's author needs
   (keep the job's name stable because the rule names the check) and is true of the file
   `.github/workflows/tests.yml` (job `tests`, comment lines 5-6).
2. **Does anything rest on the removed sentence?** I searched the tracked files (not `.runs/`) for
   `job's name`, `job name`, `named by the job`, `check name`, `name that stays`, case-insensitive: hits are
   only the workflow comment (`tests.yml:5-6`, which says the rule names the job's check and asserts nothing
   of the host), the README line itself, and three unrelated "names" in `decisions.md` and
   `product-guidelines/coding/template.md`. I read whole: WAY-16 (it names the check `tests` in its
   *Based on* TODO, and its *Verification* names the README description as saying "required check with a
   bypass for the owner" — neither mentions how GitHub names a check), invariant `ci-checking-commands`
   (rests on none), the three facts `github-dependabot-alerts`, `github-required-status-checks`,
   `github-ruleset-bypass` (none says anything about the name of a check; each is named by WAY-206 or WAY-16
   — `grep` of the identifiers). The tests of `installation` hold only the heading "Run the one command in
   CI" (`installation/test_install.py:175`), which is unchanged. The report's claim holds: no decision,
   invariant, fact or test rests on the sentence.
3. **Other claims of the report.**
   - Entries compared: I read WAY-16, WAY-160 and WAY-206 whole and compared them with the code. WAY-16 is
     matched by `tests.yml` (one command, on `pull_request` into `foundations`), the installer (no CI file
     written; `installation/install.py:198-210` says the command runs in CI at the pinned commit, is a
     required check, owner may bypass, and points to the README section) and the README section. WAY-160
     is matched by `task-cycle/skill/SKILL.md:581-592` (wait on the head last pushed, red result is a
     failed gate, a blocked request is not waited for, `tests` result in the description and the record).
     WAY-206 is matched by `product-guidelines/coding/settle.md:34-39` and `:129-131` (the alerts are
     proposed and the skill turns nothing on; the weak point is named).
   - No new environment fact: the README's other host statements (`pull_request` never
     `pull_request_target`, `submodules: true`, `fetch-depth: 0`) are examples that no decision or
     invariant names; by WAY-73 no fact stands for them. I judge the report right and the commit
     consistent: it removes the one clause whose truth a reader could take for the foundation's, and leaves
     the examples, which are labelled "on GitHub" and bind nobody.
   - No new glossary term: the README sentence after the edit uses no word that needs an entry that the
     earlier text did not.
   - Rows of *Settlements to record*, each where its *Goes to* column names it: 1 and 2 in the sentences of
     WAY-16 (read); 3 in the comment of `tests.yml:3-6` (Linux, why, Windows by the cycle's gate); 4 in the
     sentence of WAY-206 (lines 4994-4996); 5 in `product_guidance` of `installation/install.py:198-210`
     (the script runs too, error stops, warning does not); 6 in the sentence of WAY-160 (read). All present.
   - Choices that bind after the merge: the table's placing agrees with the questions of the decisions
     template as the report applies them; none of the five rows needs a log entry on the grounds the report
     gives (one text or number of code with its comment; the README is where the description for products
     lives). I did not open the template to re-derive each row beyond this; see *Unread material*.
4. **Does the commit add anything nobody asked for?** No. It removes a clause; it adds no text.

## Declined to judge

- Whether the README should state how GitHub names a required check, as help for a product's author:
  a matter of taste about the description, outside the return step's rule and the task; the removed clause
  was not required by any row of the task.
- The `TODO` in the *Based on* of WAY-16 (the reading of the branch rule once the owner sets it) and the
  human action that sets the rule: written by the earlier steps and reviewed in `PASS 23f08e9`; not part of
  this range.

## Checks I ran

- `python -B elements/common/foundation_check.py` in the worktree root → exit 0 (`0 errors`).
- `python -B gate/run_tests.py installation` → exit 0 (61 tests, OK, 295 s).
- Not run: the whole gate (not allowed), other directories (the commit touches only
  `installation/README.md`).
- Manual: `git rev-parse HEAD`, `git log --stat 23f08e9..b344595`, `git diff 23f08e9..b344595`,
  `git status --short` (clean); searches named above.

## Reaches beyond the dispatch

- `foundations/environment_facts.md` (the three GitHub facts, lines 258-274), `foundations/invariants.md`
  (`ci-checking-commands`), WAY-73 and WAY-90 in `foundations/decisions.md` (lines 1584, 1737): to judge
  whether a fact is owed for the removed clause.
- `.github/workflows/tests.yml`, `installation/install.py:198-210`, `task-cycle/skill/SKILL.md:570-596`,
  `product-guidelines/coding/settle.md:34-39,127-131`, `installation/test_install.py` (grep): to verify the
  rows of *Settlements to record* and that no test holds the clause.

## Working copies

None made; `.runs/review-return/` was not needed and does not exist.

## Unread material

- Read whole: the handoff, `task-cycle/review/SKILL.md`, `task.md`, `return-step-report.md`,
  `task-cycle/skill/return_step.md`, WAY-16, WAY-73, WAY-160, WAY-206 (WAY-90 read from its first
  paragraph through the *Rationale*; its *Rejected* tail read only in part), the three environment facts.
- Not read: `return-step-handoff.md`; the decisions template (`foundation` questions "Where it goes") and
  `foundation_step.md`, so the report's table of choices that bind after the merge is judged by the
  entries it names, not re-derived by the template; `product-guidelines` guideline files (no code or
  guideline rule is reached by a one-clause README edit); WAY-34, WAY-133, WAY-09, WAY-44 (the report says
  they match "no change"; I did not reread them, as the commit changes none of what they say).

## Searches not found or unclear

none
