PASS 23f08e917bdaa803b590135d79382da1bcdb8a43

# Review of the fix — ci-on-merge-requests

Range: `345b6bd832326872f96e301337451762d004c60d..23f08e917bdaa803b590135d79382da1bcdb8a43`
(`git rev-parse HEAD` gave `23f08e917bdaa803b590135d79382da1bcdb8a43`, the head of the handoff;
three commits, `21777bd`, `827f716`, `23f08e9`, 12 files). One author, no plan: no slice.

Result: every finding of `reports/review-whole-findings.md` is fixed; the fix brings no new
Critical or Important finding; no Minor finding remains and I found no new one in the fix diff.

## Each finding

**I-1 — fixed.** Three environment facts stand in `foundations/environment_facts.md`
(`github-dependabot-alerts`, `github-required-status-checks`, `github-ruleset-bypass`), each of one
page of GitHub's documentation, with its address, an archived copy and its date, the place, the
passages word for word and `read 2026-11-14`. WAY-206's *Based on* names `github-dependabot-alerts`
after the Open Mercato source (`foundations/decisions.md:4999-5002`); WAY-16's *Based on* names the
two ruleset facts and `TODO — a reading, as WAY-84 asks …, of the rule of the branch foundations of
the-way that requires the check tests with a bypass for the owner, once the owner has set it; no such
rule stands yet` (`:556-559`), which WAY-287 puts under *Fix or let through* (its *Verification*
accepts "a value that names a fact the foundation holds and then `TODO — …`" as one gap). Evidence:
- Each of the nine passages stands in the live page's text, markup dropped and whitespace collapsed
  (my own fetch, check 3 below).
- Each fact's sentence says what its passages say and no more: the alerts can be enabled by
  repository administrators and organization owners, and Dependabot scans the default branch and
  sends alerts on a new advisory or a changed dependency graph; required status checks must pass
  before collaborators can merge into the targeted branch; a ruleset can let certain users bypass it,
  repository admins, organization owners and enterprise owners being eligible ("among those
  eligible" keeps the list open, as the page's list is longer).
- WAY-206's *Rationale* was brought down to what the fact gives (`:5028-5030`: the alerts "scan the
  repository when a new vulnerability is published and not only when a change brings in a version,
  and are enabled by the repository's administrators"); "the owner answers an alert with a task that
  raises the library" keeps the task's answer to its fourth question ("Sygnał trafia do właściciela
  repozytorium, a reakcją jest zadanie podbicia biblioteki").
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors` (every fact named is held,
  every fact held is named — WAY-73).

**I-2 — fixed.** WAY-160's sentence now names the requests the wait covers — "a request whose code
is finished — one open for review, or one that waits only for human actions in the cycle" — "on each
head it pushes to it, a correction's included", and puts a request "the cycle leaves blocked for
unfinished code" out of the wait, its description saying so (`foundations/decisions.md:4067-4072`);
*Verification* (`:4082-4084`, `:4090-4091`) and *Rationale* (`:4106-4109`) follow. The routes do what
it says:
- `task-cycle/skill/correction.md:55-63`: a new paragraph — the wait on the head pushed last once the
  pair of commits is pushed, the result into *Checks* in a further, checked edit and into the
  original record, red as a failed gate with fix, review, gate, pair and wait again; a request the
  correction leaves blocked is not waited for.
- `task-cycle/skill/SKILL.md` step 12 (`:581-592`) limits the wait to a request "open for review or
  waits only for human actions in the cycle"; step 9 sub-step 4 (`:436-437`), `blocked_finding.md`
  (`:18-20`) and `reserved_return.md` (`:67-68`) say that their blocked requests are not waited for and
  what *Checks* says instead; `request_template.md` *Checks* (`:462-463`) gives the same sentence for
  every request left blocked for unfinished code.
- The orchestrator's answer bounds the way (handoff); the way holds together. A request waiting only
  for human actions — this task's own — is still waited for, which keeps row 6 for every request whose
  code the human will merge.

**I-3 — fixed.** The block (`installation/install.py:204-210`) now reads "… and its result is a check
this repository requires before a merge, which the repository's owner may bypass." The test fragment
in `installation/test_install.py:147-150` holds the whole sentence, the bypass included, so dropping
the bypass fails `test_guidance_names_no_commit_and_covers_the_product_rules`. Nothing else in
`installation/install.py` changed (the diff of the range touches only that string).

**M-1 — fixed.** `installation/README.md:148-157`: item 1 allows "no secret of the product but the
one item 3 allows"; item 3 says the read-only credential "is the one secret the job may hold, and
where the host gives a request from outside no secret, such a request cannot then be checked". The
two items now agree, and the second clause is conditional on the host, so it states nothing about
GitHub that no source gives.

**M-2 — fixed.** `task-cycle/record_template.md:150-153` and step 12 (`task-cycle/skill/SKILL.md:586-588`)
say the row stands in the original record, that the committed copy holds it only for the runs before
its own head, and that no pair of commits is repeated to bring it in. `correction.md` writes the
result "into *Verification* of the original record", in step with them.

**M-3 — fixed.** Step 12 (`SKILL.md:584-585`) and `correction.md:57-59` make the edit that writes the
CI result pass "the template's checks, the check of private paths included" before it is published
(WAY-309).

**M-4 — fixed.** The same sentence of the block opens "Where this repository has a CI file" and is
followed by "While it has none, nothing but you runs the tests before a merge, and you say so when you
report." (`installation/install.py:204-209`), held by the second new fragment of the test
(`installation/test_install.py:151-152`); the table row of `installation/README.md:61` says "where the
repository has a CI file". The sentence To do 3 asks for still stands, now true in both states.

## What the fix itself brings

- Trust boundary: `installation/install.py` changes a constant string only; `product_guidance` still
  takes no input. No finding.
- The facts: each value is taken from its page (check 3); each source has address, archived copy
  with date, place, passages and date read, in the template's form. No finding.
- WAY-16, WAY-206, WAY-160: sentence, *Verification*, *Rationale* and *Rejected* agree with each other
  and with rows 1, 2, 4 and 6. WAY-160's exemption of a blocked request is the orchestrator's bounded
  answer, carried as a choice of the cycle; it narrows no row, since a request blocked for unfinished
  code is no request the human merges as it stands. No finding.
- `agent-instructions/README.md:106-109` restates WAY-160 with "after each correction" and the blocked
  exemption, in step with the entry. No finding.

## The author's open points

1. "A check can be chosen only after it has run", removed from `installation/README.md`, while the
   task's *Human actions* still carries it: the removal is sound — the claim had no source, and
   WAY-16 and the facts no longer lean on it. The task document is the cycle's frozen input, not a
   file of this change; the human meets the sentence there when setting the rule, and it costs
   nothing if it is wrong (the rule is set after the request's first run either way). The README's
   new clause "which on GitHub is named by the job's name" rests on a page the author read and no
   entry rests on it; I did not fetch that page (see *Searches not found or unclear*). No finding.
2. The archived copy of the Dependabot page holds an older text: the environment-facts template asks
   for "the closest archived copy that already exists … never one made for the entry"
   (`elements/environment-facts/template.md:109-111`), and the author took the latest capture the
   index lists and names the gap. The live page holds the four passages (check 3). It complies with
   the template; a reader who compares with the archive sees the older text, which a later capture
   cures. No finding.
3. The two blocked variants of the request template that no skill file names (a question from the
   foundation step, an impossible task): WAY-160's "a request the cycle leaves blocked for unfinished
   code" and the *Checks* sentence of `request_template.md:462-463` reach them, and the template is
   what writes their description. No finding.

## Declined to judge

none

## Checks run

1. `git rev-parse HEAD` → `23f08e917bdaa803b590135d79382da1bcdb8a43`, exit 0; `git log --stat
   345b6bd..23f08e9` and `git diff 345b6bd..23f08e9` → exit 0, read whole.
2. Line lengths of the fix diff, by a one-line PowerShell filter: the long lines are the one-line fact
   entries and a table row, as the files already hold; no finding.
3. `python -I -B scripts/passages.py passages.txt` (a script of mine in `.runs/review-fix/scripts/`
   that fetched each of the three live pages of GitHub's documentation the new facts cite, dropped the
   markup, collapsed whitespace and looked for each quoted passage) → exit 0;
   `about-dependabot-alerts [True, True, True, True]`, `available-rules-for-rulesets [True, True]`,
   `creating-rulesets-for-a-repository [True, True, True]`. The archived copies I did not fetch; the
   author's `reports/author-fix-sources-check.txt` reports the Dependabot copy as holding an older text
   (open point 2).
4. Windows, in the reviewed worktree, one at a time:
   - `python -B elements/common/foundation_check.py` → exit 0, `0 errors`;
   - `python -B gate/run_tests.py elements/common` → exit 0, `Ran 201 tests`, `OK`;
   - `python -B gate/run_tests.py task-cycle` → exit 0, `Ran 440 tests`, `OK`;
   - `python -B gate/run_tests.py agent-instructions` → exit 0, `Ran 25 tests`, `OK`;
   - `python -B gate/run_tests.py installation` → exit 0, `Ran 61 tests in 397.140s`, `OK`.
5. `git status --short` after the runs → empty; head unchanged.
- Not run: the whole gate (the orchestrator's alone); Linux runs (the fix touches no test that needs
  POSIX, and no code path that differs between the systems); the workflow on GitHub.

## Reaches beyond the dispatch

- `elements/environment-facts/template.md` lines 95-154 (the *Source* rules): to judge the form of the
  three facts and the archived copy (open point 2).
- The three pages of GitHub's documentation the facts cite, fetched once each by my script: to check
  each passage.
- WAY-287 (read whole in the review of the whole change): whether a *Based on* with facts and a `TODO`
  is one gap put before the human.

## Working copies

- `.runs/review-fix/scripts/passages.py` (the script of check 3), `.runs/review-fix/passages.txt`,
  `win-runs.txt` and `one.txt` (outputs): all stood in `.runs/review-fix/`, removed with that
  directory before I returned (`Test-Path .runs\review-fix` → False).
- No worktree, clone or container. Remainder: none.

## Unread material

- Read whole: the findings file, the author's fix report and its sources check, the handoff, `fix.md`,
  the diff of the range, WAY-16, WAY-160 and WAY-206 at the head, the three new facts.
- Not read whole: `task-cycle/skill/correction.md` beyond lines 25-75; `task-cycle/skill/SKILL.md`
  beyond the passages the diff touches (read in the review of the whole change, lines 381-614);
  `installation/README.md` beyond the diff and lines 137-173; `foundations/environment_facts.md`
  beyond the new entries and the headings. Decisions: none beyond those of the review of the whole
  change, whose counts stand in `reports/review-whole-report.md`.

## Searches not found or unclear

- The page of GitHub's documentation behind "the rule names the check, which on GitHub is named by
  the job's name" (`installation/README.md:170`): not fetched by me; the author names *Troubleshooting
  rules*. No entry rests on it.
