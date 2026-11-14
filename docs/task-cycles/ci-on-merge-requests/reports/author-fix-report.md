# Report of the fix — ci-on-merge-requests (the one author, after the review of the whole change)

**Status:** `done with concerns` (the concerns: one `TODO` that stays in WAY-16 *Based on* by the
orchestrator's answer, the archived copy of one source that holds an older text, and two points
named under "Searches not found or unclear").

Range of the fix: `345b6bd..23f08e9`, three commits, nothing pushed. Run no whole gate.

| Commit | What |
|---|---|
| `21777bd` | `foundations/environment_facts.md` (three facts), `foundations/decisions.md` (WAY-16 and WAY-206 *Based on*, WAY-206 *Rationale*, WAY-160) |
| `827f716` | `installation/install.py`, `installation/test_install.py`, `installation/README.md` |
| `23f08e9` | `task-cycle/skill/SKILL.md`, `correction.md`, `blocked_finding.md`, `reserved_return.md`, `request_template.md`, `record_template.md`, `agent-instructions/README.md` |

`git diff --numstat 345b6bd..HEAD` (added/removed): `foundations/decisions.md` 24/12,
`foundations/environment_facts.md` 18/0, `installation/README.md` 9/9, `installation/install.py` 7/5,
`installation/test_install.py` 6/2, `task-cycle/skill/SKILL.md` 14/9, `task-cycle/skill/correction.md` 10/0,
`task-cycle/skill/blocked_finding.md` 3/1, `task-cycle/skill/reserved_return.md` 3/0,
`task-cycle/skill/request_template.md` 4/3, `task-cycle/record_template.md` 4/2,
`agent-instructions/README.md` 4/3.

## Each finding — what changed, where, and the check

**I-1 (WAY-16 and WAY-206 rest on the host).** Three environment facts, written by
`elements/environment-facts/skill/SKILL.md` and its `read.md`, `decide_entry.md`, `draft.md`,
`write.md`, each from a page of GitHub's own documentation read on 2026-11-14 with a script that
fetched the page and dropped the markup (the passages were compared with the page's text, whitespace
collapsed; the result is `reports/author-fix-sources-check.txt`):

- `github-dependabot-alerts` (page *About Dependabot alerts*): repository administrators and
  organization owners can enable the alerts, and Dependabot scans the default branch and sends alerts
  when a new vulnerability enters the GitHub Advisory Database or the dependency graph changes. Named
  in WAY-206's *Based on*, after the Open Mercato source.
- `github-required-status-checks` (page *Available rules for rulesets*): a ruleset can require status
  checks, and then they must pass before a merge into the targeted branch or tag.
- `github-ruleset-bypass` (page *Creating rulesets for a repository*): a ruleset can allow certain
  users to bypass its rules; repository admins, organization owners and enterprise owners are
  eligible. Both named in WAY-16's *Based on*.
- WAY-16's *Based on* also holds `TODO — a reading, as WAY-84 asks for a setting changed outside the
  repository, of the rule of the branch foundations of the-way that requires the check tests with a
  bypass for the owner, once the owner has set it; no such rule stands yet` (the orchestrator's
  instruction: the branch is not protected today and the rule is the human's action). WAY-287 puts
  it before the human under *Fix or let through*.
- WAY-206's *Rationale* said the alerts "tell the owner of the repository" and "read the whole set of
  dependencies with no change needed"; the source says neither in those words, so I reworded it to
  what the page says (they scan when a new vulnerability is published, and are enabled by the
  repository's administrators).
- Check: `python -B elements/common/foundation_check.py` → exit 0 (`0 errors`), and with
  `--skip-test-citations` → exit 0, after the facts and *Based on* lines stood.

Choices and their prices:

1. *One page, one fact.* The branch-rule claims stand in two facts (checks, bypass), each of one page,
   since two pages of the docs are no one edition. Price: two names in WAY-16's *Based on*.
2. *The archived copies.* The CDX index lists, for the alerts page, captures up to 2026-01-07 only; I
   used the latest, `20260107142947`. **That copy holds an older text of the page: none of the four
   passages stands in it**, while the live page holds all four (`author-fix-sources-check.txt`, line
   `a_arch.txt`). The template asks for the closest archived copy that already exists, so I kept it
   and name the difference here. Price: a reader who compares the passage with the archived copy sees
   no match and must read the live page; a later capture of the page would replace the address. The
   other two copies (`20261109032616`, `20260822111548`) hold their passages.
3. *Not written:* "a check can be chosen only after it has run". I found no page of the documentation
   that says it (the ruleset pages say the check's name is entered, the classic rule searches for it).
   I did not put it in a fact, and **removed it from `installation/README.md`**, which had it as
   "(on GitHub, a job that has never run cannot be chosen, so this follows the first run)". The
   task's *Human actions* item still says it; whether it holds is the human's to see. In its place the
   README says that the rule names the check, "which on GitHub is named by the job's name" (page
   *Troubleshooting rules*, "Workflow: The name format is <job name>."; no fact for it, since no
   decision rests on it). This also answers the open point of my first report: the check to require is
   named `tests`.
4. *A `TODO` and not a reading in WAY-16.* The orchestrator's answer; price: the human sees the gap at
   the merge and the rule is not read until it is set.

**I-2 (the correction and the blocked requests).** WAY-160's sentence now reads: where CI runs on a
request whose code is finished — open for review, or waiting only for human actions in the cycle — the
orchestrator waits for the result of the run on each head it pushes, a correction's included, treats
red as a failed gate and puts the result in the description; a request left blocked for unfinished
code is out of the wait, its description saying that the result stands on the request's page and was
not waited for. WAY-160's *Verification* (complies: a correction waits again for the corrected head, a
request blocked for a finding says the result was not waited for; violates: a correction leaves the
earlier head's result in the description) and *Rationale* (every push starts a run; no wait for code
that will change) follow. In the three places and the correction:
- `task-cycle/skill/correction.md`: a new paragraph after the rewriting of the description (the wait on
  the head pushed last, the result into *Checks* in a further edit checked by the template's checks,
  into the original record's *Verification*, red as a failed gate, the blocked outcomes not waited for).
- `task-cycle/skill/SKILL.md` step 12 (the request "open for review or waits only for human actions")
  and step 9 sub-step 4 (a slice failed twice: no wait, *Checks* says so).
- `task-cycle/skill/blocked_finding.md` and `task-cycle/skill/reserved_return.md`: one sentence each.
- `task-cycle/skill/request_template.md`, *Checks*: the same statement for a request left blocked.
- Check: `python -B gate/run_tests.py task-cycle` → exit 0; `foundation_check.py` → exit 0.
- Choice: the blocked variants not named by the orchestrator (a question from the foundation step; an
  impossible task) have no sentence of their own in the skills; WAY-160 covers them by "unfinished
  code" and `request_template.md`'s *Checks* sentence. Rejected: a sentence in each variant of the
  template's table (five more places for one rule). Price: those two variants rely on the decision's
  wording.

**I-3 and M-4 (the installer's block).** One edit of the same sentence in `product_guidance`
(`installation/install.py`): "Where this repository has a CI file, CI runs the one command on every
merge request, with `.the-way` at the commit this repository pins, and its result is a check this
repository requires before a merge, which the repository's owner may bypass. While it has none,
nothing but you runs the tests before a merge, and you say so when you report. `.the-way/installation/README.md`,
section "Run the one command in CI", says what the CI file of this repository holds." The row of the
README's table for `AGENTS.md` says "where the repository has a CI file". Tests: the fragment of
`test_guidance_names_no_commit_and_covers_the_product_rules` now holds the whole conditional sentence
with the bypass and the "While it has none" sentence (the test that holds that the section exists at
the pinned commit is unchanged and still passes).
- Failing first: `python -B -m unittest discover -s installation -p "test_install.py" -k guidance`
  → exit 1 after the test change and before the installer change (1 failure: the new fragment not
  found), exit 0 after (3 tests OK).
- Break each fragment catches: dropping "which the repository's owner may bypass" or the "While it has
  none" sentence from the block (a bug: I-3, M-4); a reworded sentence that keeps the meaning breaks
  the test too — the same price the existing fragments have.
- `python -B gate/run_tests.py installation` → exit 0.

**M-1 (secret).** `installation/README.md`, item 1: "no secret of the product but the one item 3
allows"; item 3: the read-only credential for the submodule "is the one secret the job may hold, and
where the host gives a request from outside no secret, such a request cannot then be checked". I did
not state that GitHub gives a fork no secret (I did not find that sentence on the pages I read); the
clause is conditional on the host.

**M-2 (the CI row of the record).** `task-cycle/record_template.md` and step 12 of
`task-cycle/skill/SKILL.md`: the row stands in the original; the committed copy holds it only for the
runs before its own head, since the run on the head that removes the copy comes after it, and no pair
of commits is repeated to bring the row in.

**M-3 (checks before an edit).** Step 12 and the new paragraph of `correction.md`: the edit that writes
the CI result into *Checks* passes the template's checks, the check of private paths included,
before it is published (WAY-309).

## Checks (command and exit code)

- `python -B -m unittest discover -s installation -p "test_install.py" -k guidance` → 1 (before), 0
  (after).
- `python -B gate/run_tests.py installation` → 0.
- `python -B gate/run_tests.py task-cycle` → 0 (includes the check of private paths on every tracked
  file).
- `python -B gate/run_tests.py agent-instructions` → 0 (checks the instruction files, among them
  `agent-instructions/README.md`).
- `python -B gate/run_tests.py elements/common` → 0.
- `python -B elements/common/foundation_check.py` → 0 (`0 errors`), run on the committed head and
  before the commits, also with `--skip-test-citations`.
- Not run: the whole gate (the orchestrator's); the workflow on GitHub; the directories I changed
  nothing in; `instruction-files`, whose files this fix does not touch.

## Own-work check (WAY-164)

- **Requirement most likely not met:** I-2, "the wait applies to every push to a request that is open
  for review or waits only for human actions", across all routes of the cycle that push to a request.
- **Check:** searched `task-cycle/skill/` for each place that opens or pushes to a request (`grep` for
  "open the request", "as a draft", "edit the request's description", "push") and read each against
  the new sentence: step 12 (wait), correction (wait), step 9 sub-step 4, `blocked_finding.md`,
  `reserved_return.md` (no wait, stated). The correction's own reserved-choice branch (the part "After
  a correction" of `reserved_return.md`) returns the request to a blocked draft and so falls under the
  sentence of that file; it holds no sentence of its own.
- **What it showed:** the five routes the orchestrator named are covered; the two blocked variants of
  the template's table that no skill file names (a question from the foundation step, an impossible
  task) rest on the decision (choice above).

## The foundation step for the entries written or changed

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| `github-dependabot-alerts`, `github-required-status-checks`, `github-ruleset-bypass` (environment facts) | `the cycle's` | What GitHub's documentation says about the alerts, required checks and bypass, on which WAY-206 and WAY-16 rest. | Co dokumentacja GitHuba mówi o alertach, wymaganych sprawdzeniach i obejściu, na czym opierają się WAY-206 i WAY-16. |
| WAY-16 *Based on* (two facts and a `TODO`) | `the cycle's` | The decision names its sources, and the unsourced reading of the branch rule is a gap the human sees. | Decyzja wymienia swoje źródła, a brakujący odczyt reguły gałęzi jest luką, którą widzi człowiek. |
| WAY-206 *Based on*, *Rationale* | `row 4` (as before) | The signal of a vulnerability in a held library is the service's alerts, with a source. | Sygnałem o luce w używanej bibliotece są alerty serwisu, ze źródłem. |
| WAY-160 sentence, *Verification*, *Rationale* | `row 6` (as before) | The wait for CI follows every head of a request with finished code, a correction's included; a request blocked for unfinished code is not waited for. | Czekanie na CI dotyczy każdej głowy prośby z gotowym kodem, także po poprawce; prośby zablokowanej z niegotowym kodem się nie czeka. |

Search of the whole foundation (WAY-33) for the entries written: searched `foundations/` for
`Dependabot`, `alerts`, `required check`, `bypass`, `status check`, `CI`, `waits for`, `blocked`
against WAY-160, WAY-16, WAY-206, WAY-84, WAY-90, WAY-287, WAY-263, WAY-309, WAY-254, WAY-235 and the
facts file; findings: `installation/README.md` (the claim "a job that has never run cannot be chosen"
removed, row of the table), `agent-instructions/README.md` (the wait after a correction and the
blocked exception), the cycle's skill files above. No collision between decisions.

## Reaches beyond the handoff (what, where and why)

- `foundations/decisions.md`: WAY-84, WAY-90, WAY-287, WAY-263, WAY-309 (read whole) for the rules of
  *Based on*, `TODO` and the checks before a description is published.
- `elements/environment-facts/template.md` and `skill/read.md`, `decide_entry.md`, `draft.md`,
  `write.md`: the element's method.
- `task-cycle/skill/correction.md` (read whole), `blocked_finding.md`, `reserved_return.md`.
- The pages of GitHub's documentation named above and `web.archive.org` CDX index and captures, read
  with `curl` and a script of my own (`urllib`); pages on secrets of forked requests and on
  troubleshooting rulesets (read for `README.md`; not written as a fact).
- `git stash` and `git stash pop` once in a slip of a command: the stash list was empty after it and
  the tree was as before (verified with `git status`); no work was lost.

## Working copies

- `.runs/author-fix/` (pages as text, scripts `txt.py`, `chk.py`, the edit scripts, test outputs):
  stood there, removed with `rm -rf`. What the report needs is kept in
  `reports/author-fix-sources-check.txt`. No worktree, no container, no clone. Remainder: none.

## Unread material

- Files I changed that I did not read whole before changing them: `installation/test_install.py` and
  `installation/install.py` beyond the passages I changed (both read in part in the first turn),
  `foundations/decisions.md` (entries only), `foundations/environment_facts.md` (the part I added to
  and its end; earlier facts only as examples).
- Decisions of the handoff's lists beyond WAY-84, WAY-90, WAY-287, WAY-263, WAY-309 and those of the
  first turn: unread.
- `task-cycle/skill/request_check.py`, `elements/environment-facts/skill/projected.md`: not read.

## Searches not found or unclear

- A passage of GitHub's documentation that says a check can be chosen for a required rule only after
  it has run: not found on *Available rules for rulesets*, *Creating rulesets for a repository*,
  *Troubleshooting rules* and *Managing a branch protection rule*; removed from the README (above).
- A later archived copy of *About Dependabot alerts* whose text holds the passages: the CDX index lists
  none after 2026-01-07; the archived address names an older text.
- Whether the "Dependabot alerts" page and the "ruleset" pages are each "one edition" for the template:
  the template says a page without editions takes the closest archived copy; I wrote each fact from
  one page.

## Problems as observed

- The Wayback Machine answered `429 Too Many Requests` to many requests in a row; the captures were
  fetched after waits. The passages of both rulesets copies were then compared.
- A command of mine that mixed a heredoc with an interactive `python` call opened a REPL and ran
  into its timeout; I stopped it. It had written no file of the repository.

## Questions

None.
