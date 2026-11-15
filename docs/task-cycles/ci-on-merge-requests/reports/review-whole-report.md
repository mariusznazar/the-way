FAIL 345b6bd832326872f96e301337451762d004c60d

# Review of the whole change — ci-on-merge-requests

Range: `21ecb627f885de438e2209d7ff5c137b1e1b9d83..345b6bd832326872f96e301337451762d004c60d`
(`git rev-parse HEAD` in the worktree gave `345b6bd832326872f96e301337451762d004c60d`, the head of
the handoff). Ten commits, 13 files, 245 insertions and 50 deletions, as the handoff gives. One
author, no spec, no plan: every blocking finding below comes from no slice.

Counts: 3 blocking (Important, within the task), 4 Minor (within the task), 0 out of scope;
2 lines under *Declined to judge*.

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

## Declined to judge

- `task-cycle/test_remove_merged_worktrees.py`, two tests that fail where the user is root
  (handoff, question 4): outside the task — the fault is in the tests' handling of a held file under
  root, the CI runner is not root, and no file of this change touches them or what they test.
- What a pull request that edits `.github/workflows/tests.yml` can do to its own required check: it
  can replace the run with one that passes, and a request from a branch of the same repository can
  raise the token's `permissions` in its own copy of the workflow. Both are properties of GitHub's
  `pull_request` event for any required check, not of this workflow; the-way's answer is the review
  of every change (WAY-10) and the owner's merge, which no file of this task can add to. Outside the
  task.

## The checks against the task

- To do 1 — WAY-16 carries rows 1 and 2 (`foundations/decisions.md:549-553`): met; the owner's
  bypass is in the entry (I-3 is about the block's restatement).
- To do 2 — `installation/README.md:137-170`, "Run the one command in CI": the four contents the
  task lists are there (items 1-3 and 5, and the closing paragraph for the required check with the
  bypass); see M-1. Item 4 (Python from `.the-way/.python-version`, handoff question 2) is within
  the task: WAY-89 gives as its price that "a product pinning the-way provides exactly this
  version", and without it the run To do 2 asks for cannot start; it adds no rule the foundation
  does not already hold.
- To do 3 — `installation/install.py:198-208`: `check_instructions.py` in the one command, error
  stops and warning does not, CI on every merge request, the pointer to the section; met, with I-3
  and M-4. The pointer is held by `installation/test_install.py:166-177`, which fails when the file
  or the section is missing at the pinned commit.
- To do 4 — `.github/workflows/tests.yml`: `pull_request` into `foundations`, `ubuntu-latest`,
  `python -B gate/run_tests.py`; met. Linux failures fixed within scope (handoff question 3, below).
- To do 5 — `product-guidelines/coding/settle.md:34-39` (where the audit is proposed) and `:129-133`
  (its weak point); met.
- To do 6 — WAY-206 (`foundations/decisions.md:4982-4984`); met, with I-1.
- To do 7 — `task-cycle/skill/SKILL.md:580-587`; met for step 12, not for the correction (I-2);
  M-2, M-3.
- Settlement rows: 1, 2 → WAY-16; 3 → the comment at the head of the workflow
  (`.github/workflows/tests.yml:3-6`); 4 → WAY-206; 5 → the block; 6 → WAY-160. Each is met.
- Source fidelity of the entries the change writes: WAY-16's two sentences say what rows 1 and 2
  say, and its new *Rejected* items are the four *Not chosen* of the two questions behind them;
  WAY-206's sentence and *Rationale* say what row 4 and its answer say (the owner, a task raising
  the library), and its two new *Rejected* items are that question's *Not chosen*; WAY-160's
  sentence says what row 6 says ("before the request is marked ready" renders "Mariusz dostaje
  prośbę dopiero z wynikiem CI"), and its two new *Rejected* items are that question's *Not chosen*;
  WAY-09 adds only the consequence of the part map's new pattern. Nothing added that a row does not
  settle, and nothing of a row missing, beyond what I-1 says of *Based on*.
- Acceptance criterion (handoff question 6): the workflow has no path filter, no condition on a job
  or step and no matrix, so every request into `foundations` runs the whole gate on Linux, and
  `instruction-files` with it. In a clone made as GitHub's checkout of the request makes it
  (detached merge commit of the branch into `foundations`, the whole history, no local branch,
  `origin/HEAD` set by the workflow's step) the five tests that Windows skips —
  `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`,
  `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`,
  `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`,
  `test_an_absolute_link_out_of_the_repository_is_not_read`,
  `test_every_directory_link_is_reported_wherever_it_points` — each ran and gave `ok` as a user that
  is not root. That GitHub's runner does the same shows only on the request's first run.

## The handoff's questions on the author's report

1. GitHub claims without a source: see I-1.
2. The Python line in the CI description: within the task (To do 2, above).
3. The three tests of `instruction-files/test_check_instructions.py`: they fit the task (To do 4
   asks the cycle to fix tests that fail on Linux where the fix fits its scope) and they are faults
   of the tests, not of the script. `check_instructions.py` judges `\\192.0.2.1\share\x.md` a
   network path on Windows, Cygwin and MSYS2 only, and `/net/`, `/Network/` on macOS only
   (`instruction-files/check_instructions.py:145-156`, and its docstring at `:26-29`); the tests
   assumed the Windows judgment on every system, and the old guard of `NetworkShapesOffWindows`
   flagged `/net/` whatever the platform. No test got weaker: the CommandLine test still asserts exit
   2 and no lookup, now under a patched platform, while its Windows sibling
   `NetworkPaths.test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup` keeps the
   unpatched Windows path; the split `/net/` test gained an assertion that the path is looked up on
   Linux; the guard still flags every network shape the platform under test has.
4. `task-cycle/test_remove_merged_worktrees.py` as root: outside the scope (*Declined to judge*).
5. Gate not run: I ran single directories only, listed below.
6. Acceptance criterion: above.

## Trust boundary (handoff)

- Trigger `pull_request` with `branches: [foundations]`; `pull_request_target` appears nowhere in
  the workflow (`.github/workflows/tests.yml:14-16`).
- Token: `permissions: contents: read` at the workflow's level; `persist-credentials: false` on the
  checkout, so the token is not left in `.git/config` for the request's code, which runs after it.
- No `secrets.` reference; no cache an earlier run could poison.
- No text of the request reaches a shell: the one expression, `${{ github.ref }}`, stands in
  `concurrency.group`, outside every `run`; the two `run` lines are constant.
- Actions pinned to full SHAs, each the commit its comment's tag points to (checks below).
- `installation/install.py`: the change is a constant string in `product_guidance`, which reads no
  input; nothing of the trust boundary's handling of paths, links or files changed.
- What a request that edits the workflow can do: *Declined to judge*, second line.
- Irreversible operation: the change performs nothing outside the repository. The branch rule is
  left to the human (task, *Human actions*); the change prepares it with a job whose name, `tests`,
  the workflow's comment says stays.

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 21ecb62 345b6bd`, exit 0: 13 files, +195 lines in all;
the code files grew by `installation/install.py` +6 (685 → 691, all inside the one string of
`product_guidance`), `installation/test_install.py` +17, `instruction-files/test_check_instructions.py`
+11. The-way holds no `guidelines/coding.md` (WAY-328 departs from the coding guidelines for every
part), so there is no rule of size and no test of it to run on the base and the head; no function
grew past what its job needs, no code is left without a user, no name stopped being true. No finding.

## Checks run

- `git rev-parse HEAD` → `345b6bd832326872f96e301337451762d004c60d`, exit 0.
- `git log --stat 21ecb62..345b6bd`, `git diff 21ecb62..345b6bd` → exit 0; read whole.
- `python -B task-cycle/change_file_sizes.py 21ecb62 345b6bd` (in the reviewed worktree) → exit 0.
- `gh api repos/actions/checkout/git/ref/tags/v7.0.1` → exit 0, object `commit`
  `3d3c42e5aac5ba805825da76410c181273ba90b1`, the SHA the workflow pins with `# v7.0.1`.
- `gh api repos/actions/setup-python/git/ref/tags/v7.1.0` → exit 0, object `commit`
  `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`, the SHA the workflow pins with `# v7.1.0`.
- A clone made as GitHub's checkout of a pull request makes it, in `.runs/review-whole/ci-sim`:
  `git clone --no-local -c core.autocrlf=false <worktree>`, `git checkout --detach
  origin/foundations`, `git merge --no-ff origin/task/ci-on-merge-requests` (merge commit `a9b622e`,
  parents `21ecb62` and `345b6bd`), the local branch deleted, then the workflow's own step
  `git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/foundations` → each exit 0.
- Linux, `docker run --rm --memory 2g --user 1001:1001 -e HOME=/tmp` with image `python:3.14`
  (Python 3.14.10), that clone mounted read-only, `git config --global --add safe.directory '*'`
  first:
  - `python -B gate/run_tests.py instruction-files` → exit 0, `Ran 105 tests`, `OK (skipped=10)`,
    the ten being the tests marked "network paths are looked up only on Windows";
  - `python -B -m unittest -v test_check_instructions` in `instruction-files/` → `OK (skipped=10)`,
    the five tests of the acceptance criterion each `ok`;
  - `python -B elements/common/foundation_check.py` → exit 0, `0 errors`, nothing listed (the
    comparison with the fork point ran, since `origin/HEAD` names `foundations`);
  - `python -B gate/run_tests.py elements/common` → exit 0, `Ran 201 tests`, `OK` (it holds
    `test_the_way_foundation_passes`, which runs the check of the foundation on the repository);
  - `python -B gate/run_tests.py installation` → exit 0, `Ran 61 tests`, `OK (skipped=21)`;
  - `python -B gate/run_tests.py agent-instructions` → exit 0, `Ran 25 tests`, `OK`;
  - `python -B gate/run_tests.py task-cycle` → exit 0, `Ran 440 tests`, `OK (skipped=1)`.
  A first attempt of the foundation check and `elements/common` failed (exit 2, ". lies in no git
  repository"; `FAILED (failures=1, errors=1)`) because PowerShell dropped the quotes of
  `safe.directory "*"`, so git refused the mounted clone; the runs above came from a script file and
  are the ones that count.
- Windows, in the reviewed worktree: `python -B gate/run_tests.py instruction-files` → exit 0,
  `Ran 105 tests`, `OK (skipped=5)`.
- Windows, in the reviewed worktree: `python -B gate/run_tests.py installation` → exit 0,
  `Ran 61 tests in 384.155s`, `OK` (it holds `test_guidance_points_to_sections_the_pinned_commit_holds`
  and the fragments of `test_guidance_names_no_commit_and_covers_the_product_rules`).
- `git status --short` in the reviewed worktree after all runs → empty; head unchanged.
- Not run: the whole gate, on any system (the orchestrator's alone, handoff); the directories
  `elements/part-map`, `gate`, `relation-model`, `process-audit`, `project-level` (no file of the
  change lies in them; the author reports them passing on Linux); the workflow itself on GitHub
  (nothing is pushed; the request's first run shows it).

## Reaches beyond what I selected

- `elements/decisions/template.md` (the *Based on* rules, lines 31 and 47-62, and the table of what
  reads each field, line 104): to grade I-1 against the template's `TODO` rule and WAY-364.
- `task-cycle/skill/correction.md` (lines 25-64), `task-cycle/skill/blocked_finding.md` (whole),
  `task-cycle/skill/reserved_return.md` (lines 40-84): which other routes of the cycle push to an
  open request (I-2).
- `task-cycle/skill/SKILL.md` lines 381-614 and 736-740: the steps the changed paragraph sits in.
- WAY-309 (`foundations/decisions.md:7569-7598`, read as far as its *Verification*): the rule on
  every edit of a description (M-3).
- `instruction-files/check_instructions.py` lines 1-40, 82-83, 140-218 and the lines that call
  `network_shaped`: to judge whether the Linux failures were faults of the tests.
- `elements/common/test_foundation_check.py` lines 18-19, 242-250 and 1522-1529, and
  `elements/common/foundation_check.py` lines 102-136 and 209-214 (by search): whether the
  workflow's `symbolic-ref` step changes what the gate checks.
- `installation/test_styleguide_installation.py` lines 1-40: a second test that reads the sentence
  the change rewrote.
- `product-guidelines/coding/template.md` lines 155-174 and `product-guidelines/coding/SKILL.md`
  lines 60-79: whether the coding template or skill also had to name the alerts.
- `foundations/environment_facts.md`: the headings and a search for GitHub, to see how the
  foundation records the host's behaviour (I-1).
- WAY-93, WAY-94, WAY-142, WAY-143, WAY-330: read whole because they stood beside entries I read;
  none bears on the change.

## Working copies

- `.runs/review-whole/ci-sim` (the clone above), `.runs/review-whole/scripts/run.sh` (the script
  the containers ran), `.runs/review-whole/select.py` with its output `selected.txt` (the selection
  of decisions by *Scope*), `.runs/review-whole/linux-run.txt` and `win-installation.txt` (outputs):
  all stood in `.runs/review-whole/` and were removed with that directory before I returned.
- Containers: each ran with `--rm`; `docker ps -a` showed none left.
- Remainder: none (`Test-Path .runs\review-whole` → False; no worktree was made, so none to prune).

## Unread material

Decisions of my selection (the *Scope* of each names `installation`, `agent-instructions`,
`task-cycle`, `product-guidelines`, `instruction-files`, `decisions` or `part-map`): 182. Read
whole: 40 — WAY-09, WAY-16, WAY-27, WAY-34, WAY-35, WAY-36, WAY-38, WAY-44, WAY-48, WAY-51, WAY-55,
WAY-73, WAY-82, WAY-84, WAY-85, WAY-89, WAY-90, WAY-133, WAY-140, WAY-141, WAY-160, WAY-161,
WAY-162, WAY-164, WAY-202, WAY-203, WAY-204, WAY-205, WAY-206, WAY-235, WAY-243, WAY-254, WAY-263,
WAY-287, WAY-288, WAY-289, WAY-300, WAY-321, WAY-324, WAY-328; WAY-128, WAY-129 and WAY-130 also
whole, opened by their titles, which makes 43. By title only: 139, every one run through by its
title; none whose title points to a bearing on the change stayed unread.

- Guideline files: none exist (`guidelines/` is absent; WAY-328 departs for every part), so none
  stayed unread.
- Files of the change not read whole: `installation/install.py` (lines 190-215, the function the
  change touches), `installation/test_install.py` (lines 100-180), 
  `instruction-files/test_check_instructions.py` (lines 95-130, 490-590, 1060-1090),
  `task-cycle/skill/SKILL.md` (lines 381-614, 736-740), `task-cycle/record_template.md` (lines
  138-160), `task-cycle/skill/request_template.md` (lines 445-470), `product-guidelines/coding/settle.md`
  (lines 1-145), `agent-instructions/README.md` (lines 40-113), `installation/README.md` (lines
  84-135 and the diff), `README.md` (the diff only). Each diff was read whole.
- The foundation: `foundations/part_map.md` and `foundations/invariants.md` whole;
  `foundations/glossary.md` the headings and the entries "environment fact", "foundation",
  "foundation step", "gate", "guidelines", "human action"; `foundations/environment_facts.md` the
  headings and a search.
- `task-cycle/skill/correction.md` lines 1-24 and 65 to the end: not read.

## Searches not found or unclear

- A source, in the task or the foundation, for how GitHub's Dependabot alerts behave and for the
  branch rule with a bypass for the owner: none found; `foundations/environment_facts.md` holds no
  fact on either (I-1).
- The name under which the branch rule will list the check (`tests`, or a longer form with the
  workflow's name and the event): not determinable without a run; the author reports the same.
- Whether WAY-160's wait reaches a request the cycle leaves blocked (`blocked_finding.md`,
  `reserved_return.md`): unclear from the entry (I-2, last item).
