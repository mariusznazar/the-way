PASS e3842146a4ed24254eb16a302284f231f0dd1801

# Review of the return step's commits — ci-replaces-local-final-gate

Range `1b03ef71fb4fbd634282b6a9123913c06c0387e6..e3842146a4ed24254eb16a302284f231f0dd1801`, one commit
`e384214` ("Return step: bring WAY-381 and WAY-162 in line with two CI jobs and the CI final gate"),
`foundations/decisions.md` only, 5 insertions, 4 deletions. `git rev-parse HEAD` in the worktree is
`e3842146a4ed24254eb16a302284f231f0dd1801`, the head given.

Counts: 0 blocking, 1 Minor, 0 out of scope.

## Findings

### Critical

none

### Important

none

### Minor

1. **`foundations/decisions.md:10022-10023` (WAY-381, *Verification*, complies)** — the corrected
   clause reads "each job of CI differs from before by one step that installs the requirements".
   For `tests` (Linux) that is true: it is the job WAY-381 first changed. For `tests-windows`
   (`.github/workflows/tests.yml:53-78`) there is no "before": the job is new in this change and
   holds six steps, a `defaults` block and its own timeout, of which one installs the requirements.
   What the code does agrees with the entry's meaning — each job has exactly one install step
   (`tests.yml:48-50`, `tests.yml:75-77`) and runs only `python -B gate/run_tests.py` beside it — so
   this is wording, not content (WAY-364). The risk is small: a reviewer of a later change that adds
   a job, reading the complies clause literally, compares the new job with a "before" that does not
   exist. A wording that holds for every job: "each job of CI holds one step that installs the
   requirements, beside the one command". The body sentence ("each job of CI gains one step that
   installs it there", `decisions.md:10012-10013`) reads well enough as "has one more step" and needs
   nothing. Within the task (an entry the return step writes); Minor, so it does not block.

## Verification of the author's claims

- **WAY-381 now matches two jobs.** Confirmed against `.github/workflows/tests.yml`: both jobs make
  `.runs/quality-venv` and install from `requirements-quality.txt` with `--require-hashes`, the
  Windows one through `Scripts/python.exe`; the README sections the entry and the CI comment name
  exist (`README.md:167` "Running the tests", `README.md:185` "Installing the linter"). The
  *Rationale* ("installed wherever the gate runs") still holds. Marking it `the cycle's` is right:
  no row of *Settlements to record* carries it.
- **WAY-162 now defers to WAY-160.** "has the gate run on the code the revert leaves as WAY-160
  gives" (`decisions.md:6743`) agrees with WAY-160 (`decisions.md:2814-2820`, the CI run on the head
  pushed last is the final gate, the orchestrator's own run where CI runs on no request or gives no
  result in 30 minutes) and with `task-cycle/skill/SKILL.md:574-580` (revert, then the request opens
  on the accepted code) and `:622-643` (step 12, the wait for CI). The old wording "runs the gate"
  would have named a local run that WAY-160 now forbids where CI answers, so the correction was
  needed. The meaning of the example is unchanged; `the cycle's` is right.
- **WAY-160, WAY-16 left as they stand.** Read whole; both agree with the CI file, step 12 of the
  cycle and each other: WAY-16 asks CI on every system the product runs on (row 5) and the-way's file
  runs on Linux and Windows; WAY-160 holds rows 1, 2 and 3 (CI final gate, local run where CI does
  not run, 30-minute limit with the description saying so). No row was missed by the foundation step.
- **WAY-261, WAY-350.** WAY-261's "first run of the gate on the final tree" reads as well for a CI run
  as for a local one; WAY-350 compares only runs of the script that records gate times, which are
  local, as the task requires. No change needed.
- **No test holds a sentence of WAY-381, WAY-162, WAY-160 or WAY-16.** No line `decision: WAY-381`,
  `WAY-162`, `WAY-160` or `WAY-16` in any file (Grep, positive control: `# decision: WAY-339` found in
  `process-audit/test_audit_count.py`). `task-cycle/test_request_check.py:58-65` quotes WAY-160 and
  WAY-162 only inside a fixture task text; that is no test of the decision, so no pair moves to a
  `tests:` clause.
- **Part map, invariant `ci-checking-commands`, glossary.** `.github/workflows/**` stays in
  `agent-instructions` (`part_map.md:173`); `process-audit/**` covers `stage_pricing.py`, which reads
  no file, so the trust boundary `process-audit/audit_count.py` (`part_map.md:134`) stands. Neither
  CI job runs a checking command beside `python -B gate/run_tests.py` (`git symbolic-ref` and the
  install step check nothing), so `ci-checking-commands` holds. The glossary's *gate* ("the one
  command that runs all of a product's tests") is not used against its meaning by "the CI run ... is
  the final gate": the CI run runs that command.

## The three behaviours of GitHub with no environment fact

The handoff asks whether any of them stands under a decision's sentence. The rule: a task's return
step writes a source the change rests on "as a fact where this section asks for one"
(`elements/environment-facts/template.md:71-72`), the section asks for one where a decision's *Based
on* needs a citation that, once untrue, would call the decision into question (`template.md:45-48`),
and a fact stands only while a decision or an invariant names it (`template.md:73`). Judged one by
one:

1. **A check can be chosen as required only after it has run once.** It decides only when the human
   action of the task can be taken (the task's question "Kiedy w regule gałęzi `foundations`
   przybywa wymagane sprawdzenie na Windowsie?"), not the truth of WAY-16 or WAY-160: were it false,
   the human could set the rule earlier, and no decision would change. No fact needed. Agreed.
2. **`windows-latest` has Git Bash.** Only the CI file rests on it (`tests.yml:59-63`,
   `shell: bash`). No decision names a shell or a runner image; WAY-16 asks only that CI run on each
   system. Were it false, the Windows job would fail at its first step and the CI file would change,
   not a decision. No fact needed. Agreed; the first CI run on the request shows it.
3. **A request opened as a draft still starts a `pull_request` run.** The strongest candidate:
   step 12 opens the request as a draft and waits for CI on it (`SKILL.md:613`, `:622-628`), and a
   request waiting for human actions stays a draft (`SKILL.md:644-645`), which WAY-160 names among
   the requests whose CI run is the final gate. Still, WAY-160 states a condition ("Where CI runs on a
   request whose code is finished"), names no host and no behaviour of one, and holds where CI does
   not run on a draft: the 30-minute limit sends the cycle to its own run, and the decision's sentence
   stays true. Were the behaviour to change, the cost of the cycle on GitHub would grow by the wait,
   which the step's order in `SKILL.md`, an instruction file, would have to answer; that is no
   citation that calls the decision into question. No fact needed. Agreed, with this as the reason
   rather than "no decision's sentence names it" alone.

None of the three is a finding.

## Declined to judge

- `foundations/environment_facts.md:294-303` (`foundations-branch-ruleset`) reads that the rule
  requires only `tests`, while WAY-16 (which is *Based on* it) and the CI comment
  (`tests.yml:8-9`, "the branch rule that requires them names each") speak of both checks required.
  Set aside: the task gives the change of the rule as a human action in the cycle, a reading of a
  state that does not yet exist cannot be written, and the CI comment is outside this range (the
  review of the whole change covered it). Whoever takes the human action's result into the request
  should note that the fact then needs a new reading.
- The move of the stage pricing from `process-audit/audit_count.py` to
  `process-audit/stage_pricing.py`, against the withdrawn rows of WAY-342, WAY-343, WAY-346, WAY-348
  and WAY-352 (`decisions.md:10720-10728`, "stands in `process-audit/audit_count.py`"): outside this
  range and outside the return step's commit; looked at only far enough to see that the rules those
  rows name (which entries are read, which version, where the cost shows, which table is read) are
  not the pricing arithmetic that moved, and that `audit_count.py` still reads `stages.md`
  (`audit_count.py:995`).

## Checks

| Check | Command or method | Exit code / result |
|---|---|---|
| Range and head | `git log --oneline <base>..<head>`, `git diff --stat`, `git diff --word-diff`, `git rev-parse HEAD` | 0; one commit, one file, head matches |
| Foundation check on the head | `python -B elements/common/foundation_check.py` (in the worktree, nothing changed) | 0, `0 errors` |
| No test holds the touched decisions | Grep `decision: WAY-(381\|162\|160\|16)\b` over the worktree; positive control `decision: WAY-339` | none found; control found |
| Other entries on CI jobs, systems, the final gate | Grep in `foundations/` for `job of CI`, `Windows`, `on Linux`, `final gate`, `own system`, `runs the gate`, `gate_times`, `CI result`, `wait for CI`, `audit_count`, `stage_pricing`, `.github/workflows` | only WAY-16, WAY-160, WAY-261, WAY-350, WAY-381, WAY-162 and withdrawn rows bear on it; each read and agrees, save the Minor finding |
| CI file against WAY-381 and `ci-checking-commands` | manual reading of `.github/workflows/tests.yml` whole | each job one install step, one checking command |
| Product's full gate | not run, as the handoff says; the change is one file of the foundation | not run |

## Reaches beyond the dispatch

- `task-cycle/skill/foundation_step.md` (whole): the return step writes "as the foundation step
  writes"; needed for the marks `the cycle's` and the rule on facts.
- `elements/environment-facts/skill/SKILL.md`, `decide_entry.md` (whole), `template.md:30-79`: to
  judge the three GitHub behaviours.
- `foundations/environment_facts.md:294-303` (`foundations-branch-ruleset`): WAY-16's *Based on*.
- WAY-261 (`decisions.md:6354-6382`) and WAY-350 (`decisions.md:7994-8029`), whole as decisions of
  the task: to check they still match the code. WAY-337 (`decisions.md:7816-7855`) whole and WAY-339
  in part (`:7857-7895`): to see whether the moved pricing code changes what they say.
- The withdrawn rows `decisions.md:10690-10734`: found by the search for `audit_count`.
- `foundations/part_map.md:120-185`, `foundations/glossary.md` entry *gate*, invariant
  `ci-checking-commands` (`invariants.md:66-74`).
- `task-cycle/skill/SKILL.md:560-655` (the revert of a fix, step 12): what WAY-162 and WAY-160 now
  point to.
- `README.md` headings at 167 and 185; `task-cycle/test_request_check.py:40-84`; the head of
  `process-audit/stage_pricing.py` and the moved definitions of `audit_count.py`.

## Working copies

None made; `.runs/review-return-step/` was not created. Nothing remains.

## Unread material

- The invariant `function-and-file-size`: not read; the range changes no code, so it does not bear.
- WAY-339: read through the start of its *Verification* (`decisions.md:7857-7895`), not its
  *Rationale* and *Rejected*; it is no entry of the dispatch and bears only on the moved code outside
  this range.
- `reports/review-whole-report.md`, `reports/review-fix-report.md`: not read; not named by the
  dispatch.

Otherwise none: the handoff, the method, `return_step.md`, the author's report, the frozen task and
WAY-381, WAY-162, WAY-160, WAY-16 were read whole.

## Searches not found or unclear

- Unclear: the handoff file is not valid UTF-8 (its Polish passages show replacement characters);
  the same passages were read in the frozen task, which reads correctly.
- Unclear: whether a fact that a decision rests on through the order of a step of the cycle (the
  draft request and its `pull_request` run) counts as a citation of that decision; judged above that
  it does not, since WAY-160's sentence holds without it.
