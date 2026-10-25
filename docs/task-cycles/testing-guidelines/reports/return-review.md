FAIL f3c7f7e4cd6cb8ba6fcc19af87c50fe50c316697

# Review of the return step — task `testing-guidelines`

Range `a2f1165..f3c7f7e` (one commit), worktree `C:/Storage/repos/the-way-wt/testing-guidelines`,
branch `task/testing-guidelines`; `git rev-parse HEAD` = `f3c7f7e4cd6c…`, the head given. Method:
`task-cycle/review/SKILL.md`, the return step's commits reviewed against the task and the entries
the return step writes or corrects. Blocking 1, Minor 1, out of scope 0.

## Important

### 1. WAY-228's binding sentence and the template rule no longer say what Q13 settled; correction 1 rests on a false premise

- **Place:** `foundations/decisions.md:6062` (WAY-228 binding sentence, "a condition kept after
  every step" in place of "an invariant's sentence"); `product-guidelines/testing/template.md:158-159`
  (rule "Test inputs and expected values", same change).
- **What is wrong:** the task's settlement for this sentence, Q13
  (`.runs/task-cycles/testing-guidelines/task.md:97`), lists the relations a property test takes its
  expected value from as "odwrócenie operacji, **zdanie niezmiennika** albo prostsza wersja napisana
  z wymagania" — the sentence of an invariant. Row 14 (`task.md:177`) carries Q13 into the decision.
  The return step replaced that item with "a condition kept after every step", claiming that "the
  meaning intended here is the field's" and that "the meaning of WAY-228 does not change"
  (`reports/return.md`, Corrections 1).
- **Why the premise is false:** Q13 names its source as `raport_wytyczne_testow.md`, section 1. That
  section says, at line 29: "Biblioteka Hypothesis ma testy stanowe ze sprawdzeniem „prawdziwe po
  każdym kroku". To naturalna postać niezmiennika the way: losowy ciąg akcji, a po każdej
  sprawdzenie zdania niezmiennika (wniosek badacza)." and its table at line 46 files the Hypothesis
  quotation as "odpowiednik niezmiennika". The source thus uses "zdanie niezmiennika" for the
  sentence of a the-way invariant — exactly the glossary meaning ("An invariant is a sentence about
  the product that is true or false on every commit", `foundations/glossary.md:87`). The task's
  Polish uses "niezmiennik" in the same sense elsewhere (e.g. `task.md:19`, the "niezmiennika" test
  level). "An invariant's sentence" was therefore not a term used against its entry, and step 11 of
  `task-cycle/skill/SKILL.md` (lines 317–331) gives the return step no ground to rewrite it.
- **Why it matters:** the meaning does change. Before, a property test could take its expected value
  from the sentence of one of the product's invariants (the raport's own proposal: a random sequence
  of actions, the invariant's sentence checked after each); the human approved that list in Q13.
  Now the binding sentence names only "a condition kept after every step", which neither names the
  product's invariants nor covers an invariant's sentence checked over generated inputs without
  steps (e.g. a refusal invariant of a trust boundary checked over generated requests). The change
  alters a settled decision against its source — what the whole-change review's fidelity check
  forbids — and the return report's line "the meaning of WAY-228 does not change", meant "for the
  request", would tell the human the opposite of what happened.
- **Fix expected:** restore "an invariant's sentence" in the binding sentence of WAY-228 and in the
  template rule (`template.md:158`), and drop the request-facing claim. The *Rationale*'s change
  (`decisions.md:6095`, "a condition kept after every step" for developers' practice, read off
  Goldstein and Hypothesis) can stay: there the word was in the field sense, and the binding
  sentence's "invariant's sentence" is bridged to it by the raport's section 1.
- **Evidence:** `git diff a2f1165..f3c7f7e -- foundations/decisions.md product-guidelines/testing/template.md`;
  `task.md:97`, `:98` (Q13 source naming raport section 1); `raport_wytyczne_testow.md:29`, `:46`, `:53`.

## Minor

### 1. Template table and binding sentence keep two wordings for the stepwise case — by design, note only

`product-guidelines/testing/template.md:133` words the yes/no question "something kept after every
step" (from `task.md:31` and raport line 53), while the rule at `:158` after the fix of finding 1
will read "an invariant's sentence". Both follow their own lines of the task, so this is not a
defect; noted so that the fix of finding 1 does not "harmonise" them by rewriting either.

## Correction 2 — checked, matches

`project-level/task/skill/SKILL.md:148` now reads "even in a product with screens, code or tests",
as WAY-215 ("whether or not the product already has screens, code or tests",
`foundations/decisions.md:5772`), `product-guidelines/reading.md:67` and the task's *To do* item 4
(`task.md:54`) and row 16 (`task.md:179`) read. No line over the file's width; no other "screens or
code" wording left in a task-refinement context (`foundations/decisions.md:4664`, `:4683` are
WAY-173/WAY-174 text about guidelines' reach, not the wait).

## Declined to judge

- The return step's "Compared and found matching" section (WAY-231–250, part map, invariants,
  facts): claims about files this range does not change; the review is bounded by the range and the
  entries it writes or corrects.
- `project-level/task/skill/SKILL.md:160-161` wording "A missing coding and a missing testing
  guidelines": outside this range (return report lists it as a whole-change Minor).
- WAY-242's *Scope*: not changed by this range.

## Checks

| Command / method | Exit | Result |
|---|---|---|
| `git diff a2f1165..f3c7f7e`, `git log a2f1165..f3c7f7e`, `git rev-parse HEAD` | 0 | one commit, three files, head matches |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `git diff --check a2f1165..f3c7f7e` | 0 | empty |
| `python -B gate/run_tests.py project-level` | OK (run through a pipe to `tail`; unittest printed `Ran 259 tests … OK`) | task skill text changed |
| `python -B gate/run_tests.py product-guidelines` | 1 | `no test found in product-guidelines` — no tests there; template text unverified by tests |
| Manual: Q13, row 14, row 16, item 4 of `task.md` read against the diff; raport section 1 read for Q13's source; glossary `invariant`, WAY-228 and WAY-215 whole | — | finding 1; correction 2 matches |
| `git status --short` after the checks | 0 | clean; the worktree was not changed |

Not run: the full gate (the cycle's own run, step 10).

## Reaches beyond the dispatch

- `task.md:19`, `:31`, `:96-98`, `:177`, `:179`, `:54` — the task's own use of "niezmiennik" and the
  rows named, to judge the term's meaning in Q13.
- `raport_wytyczne_testow.md` lines 29, 46, 53 (section 1, named by the handoff) — the meaning of
  "zdanie niezmiennika" in Q13's source.
- `product-guidelines/reading.md:60-72` — to check correction 2's wording against the shared reading.
- `product-guidelines/testing/template.md:133` and `product-guidelines/testing/SKILL.md` (grep for
  "property") — other uses of the stepwise relation in the touched discipline.

---

## Review of the fix

PASS 8c7492538fd90a763d3ac70f0aa6ba207eda0fae

Range `f3c7f7e..8c74925` (one commit, "Restore an invariant's sentence among the relations of a
property test in WAY-228 and the testing template"); `git rev-parse HEAD` = `8c74925…`, the head
given. Bounded by the findings file: finding 1 (Important) of this report. Fixer's account:
`reports/return.md`, section "Fix after review".

### Finding 1 — fixed

- `foundations/decisions.md:6062-6064`: WAY-228's binding sentence reads again "undoing the
  operation, an invariant's sentence, or a simpler version written from the requirement, not copied
  from the code", as Q13 (`task.md:97`) settles.
- `product-guidelines/testing/template.md:158-159`: the rule reads the same; the file is
  byte-identical to `a2f1165` (`git diff a2f1165..8c74925` lists no change to it).
- Against `a2f1165`, the only change left in WAY-228 is the *Rationale*'s "a condition kept after
  every step" (`decisions.md:6095`), which this review allowed (field sense, developers' practice).
- The request-facing claim "the meaning of WAY-228 does not change" and the rendering note are
  withdrawn in the fixer's account, which now states that `f3c7f7e` did change the meaning and that
  `8c74925` restores it.

### New findings in the fix diff

None. The diff touches only the two restored passages; wrapping kept within the files' width;
correction 2 (`project-level/task/skill/SKILL.md:148`) untouched. The Minor finding stays as noted
and is not fixed, as WAY-161 gives.

### Checks

| Command | Exit | Result |
|---|---|---|
| `git diff f3c7f7e..8c74925`, `git log f3c7f7e..8c74925`, `git rev-parse HEAD` | 0 | one commit, two files, head matches |
| `git diff a2f1165..8c74925 -- foundations/decisions.md product-guidelines/testing/template.md` | 0 | only the *Rationale* line differs from `a2f1165` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `git diff --check f3c7f7e..8c74925` | 0 | empty |
| `git status --short` | 0 | clean |

Not run: the `project-level` tests (no file of that part changed in the fix range); the full gate
(the cycle's own run).
