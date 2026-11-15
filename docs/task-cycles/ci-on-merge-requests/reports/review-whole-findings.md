# Findings of the review of the whole change, for the fix

Cut from `reports/review-whole-report.md` (lines 13-154, the reviewer's words): the three blocking findings (Important) and the four Minor findings within the task. The report lists no finding outside the scope for the fix.

Range reviewed: `21ecb627f885de438e2209d7ff5c137b1e1b9d83..345b6bd832326872f96e301337451762d004c60d`.

## Findings

### Important

**I-1. WAY-16 and WAY-206 now rest on settings and behaviour of the repository's host, and neither
names an environment fact or a descriptive `TODO` in *Based on*.**
Place: `foundations/decisions.md:549-553` and `:556` (WAY-16, the two new sentences and
`- **Based on:** none`); `foundations/decisions.md:4982-4984`, `:4987-4990` and `:5015-5020`
(WAY-206, the new sentence, *Based on*, *Rationale*). No slice.

- WAY-16 now declares, for the-way itself as for every product (its *Verification* names "the CI
  file of the-way"), the choice of a setting people change outside the repository: "The result of
  that run is a check the repository requires before a merge, and the owner of the repository may
  bypass it." WAY-84 says of exactly such a setting: "A choice of such a setting is a decision only
  where the product declares it, and that decision rests on the fact", and its *Verification* gives
  as complying "the protection of a branch, which no page open without the access of the product's
  people shows, is a fact whose source is a reading of it". WAY-16 reads `Based on: none`. Today the
  branch is not protected (task, *Context*: "Branch not protected", read 2026-11-14); the rule is a
  human action in the cycle that can only follow the first CI run.
- WAY-206 now rests on how GitHub's Dependabot alerts behave: "the alerts of its repository's
  service, which read the whole set of dependencies with no change needed and tell the owner of the
  repository … They are a setting of the service, no file of the repository, so a human turns them
  on." WAY-90 asks for a fact entry in *Based on* "for every citation that, once it stopped being
  true, would call the decision into question — … the behaviour of a tool the process uses"; the
  decision template (`elements/decisions/template.md:60-62`) says that where the decision's source is
  silent, *Based on* reads `TODO — <what is missing, with its source>`, "never a bare `TODO` and
  never `none`". WAY-206's *Based on* still names only the Open Mercato workflow, which says nothing
  of alerts. The foundation records GitHub's behaviour as facts elsewhere
  (`github-collapsed-section` for WAY-288, `github-closed-pull-request-branch`).
- Why it matters: the decision template's table gives *Based on* as what "the author of a change to
  a fact or a source, searching for what rests on it (WAY-33)" reads; with nothing there, a change
  of the host's alerts or of the branch rule finds neither decision. And because neither entry holds
  a descriptive `TODO`, WAY-287 does not put the gap before the human at the merge: the request will
  read as if both decisions were fully grounded. The author names the gap itself (author report,
  "Searches not found or unclear", first item) and left *Based on* as it was.
- Why Important and not Minor under WAY-364: it is no departure of form alone; WAY-16's line
  `Based on: none` is a sentence a reader reads wrongly — it states that the decision rests on no
  source outside the product, while its new sentence rests on the state of a host's branch rule.
- The answer to the handoff's question 1: yes. WAY-16 (by WAY-84) and WAY-206 (by WAY-90 and the
  template's `TODO` rule) rest on the GitHub claims in a way the foundation's own rules call a gap.
  No invariant rests on them. The `installation/README.md` sentence "on GitHub, a job that has never
  run cannot be chosen" stands in no entry and has the task's *Human actions* as its source.
- What would satisfy it, for the author to choose: an environment fact for the alerts with a source
  a reader can open, named in WAY-206's *Based on*; for the branch rule, a fact whose source is a
  reading of the rule of `foundations` once the human has set it (WAY-84), named in WAY-16's *Based
  on*; or, for either, `TODO — <what is missing, with its source>`, which WAY-287 then puts under
  *Fix or let through*.

**I-2. The correction after the human's remarks pushes new heads to the open request and never
waits for CI, which the new sentence of WAY-160 requires wherever CI runs on the open request.**
Place: `task-cycle/skill/correction.md:39-53` (unchanged by the range; it holds no word of CI), read
against `foundations/decisions.md:4064-4066` (WAY-160, the sentence the change writes) and
`task-cycle/skill/SKILL.md:580-587` (the wait, written into step 12 only). No slice.

- WAY-160 now says: "Where CI runs on the open request, the orchestrator waits for its result before
  the request is marked ready, treats a red result as a failed gate — a fix and its review — and puts
  the result into the request's description", and its *Verification* names as violations "a red CI
  result is left for the human to find; the description names no CI result where CI ran on the
  request". The change carries the wait into step 12 alone. A correction (`correction.md`) runs the
  gate, "repeat[s] the record's pair of commits from step 12", rewrites `request.md` and edits the
  description: each push starts a new CI run on a request that is usually already marked ready, and
  nothing tells the orchestrator to wait for it, to write its result into *Checks*, or to treat red
  as a failed gate. The description then carries the CI result of the previous head, or none, and a
  red run on the corrected head reaches the human unseen — the case the task's row 6 was chosen to
  stop ("błąd widoczny tylko na Linuksie trafia do Mariusza i wraca jako runda poprawek").
- `request_template.md:459-461` now asks *Checks* for "its run on the last head", so an orchestrator
  rewriting the description in a correction can infer a wait from the template; the step it follows
  does not say so, and the red path (fix, review, gate, pair again, wait again) is nowhere on the
  correction's route.
- Grade: Important by WAY-263 — the change's files fail to do what an entry the change writes
  requires. Within the task: row 6 and To do 7 settle what the cycle does with the CI result on its
  request; a correction is the cycle's own work on that request.
- Less clear, for the author to settle in the same fix: the blocked requests of
  `task-cycle/skill/blocked_finding.md:14-18` and `task-cycle/skill/reserved_return.md:53-65` are
  never marked ready, so the first clause of WAY-160 does not reach them, yet its *Verification*
  ("the description names no CI result where CI ran on the request") does. Either those routes say
  that they write the CI result too, or WAY-160 says that a request the cycle leaves blocked is out
  of the wait.

**I-3. The block the installer writes into every product restates the new rule of WAY-16 without
the owner's bypass.**
Place: `installation/install.py:204-206` (`product_guidance`: "CI runs the one command on every merge
request, with `.the-way` at the commit this repository pins, and its result is a check this
repository requires before a merge;"), against `foundations/decisions.md:552-553` (WAY-16: "The
result of that run is a check the repository requires before a merge, and the owner of the
repository may bypass it."). No slice.

- WAY-263 grades as Important a finding that "another changed file repeats the entry while
  broadening it or dropping a qualification". The block, the account of the rule that every agent in
  every product reads in each session, drops the bypass; `installation/README.md:166-170` and
  `agent-instructions/README.md:69-71` keep it. An agent of a product whose owner asks it to get a
  change past a CI run that is broken reads, in its own instructions, a check the repository requires
  and nothing more, so it has a stricter rule than the decision gives.
- The effect is small and the fix is a few words (", which the repository's owner may bypass"); the
  grade is WAY-263's, not mine to lower. Row 2 of the task names the bypass as part of the
  settlement.

### Minor

**M-1. The description of a product's CI file forbids secrets in item 1 and asks for a credential
in item 3.** Place: `installation/README.md:148-150` ("on the code of the request and with no secret
of the product, so that a request from outside cannot read one") and `:155-156` ("Where the URL in
`.gitmodules` needs a credential, the job holds one that can only read"). On GitHub a credential the
job holds is a secret, and a workflow run by `pull_request` from a fork receives none, so a product
whose `.the-way` is private either breaks item 1 or cannot check out its submodule on a request from
a fork. Neither clause comes from the task's To do 2, which lists four contents (the run on every
merge request, `.the-way` at the pinned commit, the history for `foundation_check.py`, the required
check with the bypass). Within the task (the description To do 2 asks for). One sentence that says
which of the two holds — for example that a read-only credential for the submodule is the one secret
the job may hold, and that a request from a fork then cannot be checked — removes the conflict.

**M-2. The committed copy of the record can never hold the CI row the record template now asks for,
and the text does not say where that row lives.** Place: `task-cycle/record_template.md:150-151`
("Where CI runs on the request, the run on its last head is a row of its own") and
`task-cycle/skill/SKILL.md:580-583` ("write its result … into *Verification* of the record"). The
last head is the commit that removes the record's copy; the run on it exists only after that push,
so the copy at the record's SHA, which the description links, cannot contain it, and committing a
new pair to add it moves the head and starts a new run. An orchestrator that reads the template
literally may repeat the pair to bring the row in, and wait again, without end; one that does not
publishes a record whose *Verification* lacks a row its template requires. One clause — the row
stands in the ignored original, and in the committed copy only for the runs before its own head —
settles it. Within the task (To do 7).

**M-3. Step 12 adds an edit of the description for the CI result without the checks WAY-309 asks
before every edit.** Place: `task-cycle/skill/SKILL.md:580-583`. The sentence before it ends "check
it again by the template's checks, which include the check of private paths, and edit the request
with it"; the new edit that writes the CI link and conclusions into *Checks* says nothing of the
checks, while WAY-309 asks the check of private paths "before each publication of a request's
description, the first and every later edit". A CI link holds no private path, so nothing leaks
today; an orchestrator following the step word for word publishes an edit unchecked. Within the task
(To do 7).

**M-4. The installer's block states that CI runs in every product, with no word for a product that
has not yet written its CI file.** Place: `installation/install.py:204-208`. The sentence is the one
To do 3 of the task asks for, so this is a finding about something the task mandates. In a product
that moves its pin before it writes the CI file — loop2 until its own task, which the task's *Out of
scope* names — the block tells every agent that "CI runs the one command on every merge request" and
that its result is required, both false there; for the two checks the same block gives a fallback
("While the one command does not run one of these two checks, run it on its own …"), for CI none.
The block still asks the agent to run every test before a merge, so no check goes unrun; what can go
wrong is an agent telling the human that CI checks a change that nothing checks. A clause such as
"where this repository has a CI file" would make it true in both states. Within the task (To do 3).
