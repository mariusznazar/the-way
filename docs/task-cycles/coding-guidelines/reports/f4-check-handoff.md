# Check-author handoff — coding guidelines, stage F4 (foundation step of the task cycle)

## Delegation

Mariusz asked for the-way's task cycle to take this task to a pull request and delegated
intermediate choices to the orchestrator. You are the **check author** of this task's invariants.
Under WAY-69 an invariant's sentence, its check and the code it covers come from three different
agents: the sentences are written (by another agent); the code that will satisfy them is not yet
written (later agents write it to meet your tests). You get each sentence and its method, never the
code's reasoning. You never ask Mariusz anything; questions go to the orchestrator in your report.

## Worktree, commit and boundaries

- Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc` at `05e44b1`.
- Change only `product-guidelines/test_form_check_invariants.py` and `installation/test_install.py`
  (its `NAMES` tuple only — C24). Commit them yourself, message in English describing what the
  commit holds and which tests are expected red until which later slice, ending after a blank line
  with:

      Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
      Claude-Session: https://claude.ai/code/session_01DYywki95VF5wQGh3SzcQZB

  Do not push.
- Report: `docs/task-cycles/coding-guidelines/reports/f4-check.md`; full
  outputs of your runs beside it (`f4-*.txt`).

## Inputs (read whole) — and what you must not read

Read:
1. The invariant entries in `foundations/invariants.md` at `05e44b1`: `guidelines-check-carrier/1`
   (edited; `git show 235b0b4:foundations/invariants.md` gives its old sentence),
   `guidelines-check-form/1`, `guidelines-check-kind-index/1`, `guidelines-check-exemplar/1`,
   `guidelines-check-example-files/1`, `gate-guidelines-example-evidence/1` (method `TODO` — no
   check from you; say so), and the other `guidelines-*` entries for context, with the decisions
   their *Derives from* names (WAY-167, WAY-168, WAY-196, WAY-198, WAY-199, WAY-202, WAY-212),
   read whole.
2. The forms the checks read: in `docs/task-cycles/coding-guidelines/spec.md`, **only §4.1, §4.2
   and §5.1** — the two fenced required forms of the coding template with their verbatim headings,
   fields, table columns and the *Status* list, and the rule on test cases (the fixtures must use
   those words exactly; the template that S2 writes will carry them). Also `product-guidelines/template.md`
   and `product-guidelines/styleguide/template.md` as they stand.
3. The existing `product-guidelines/test_form_check_invariants.py` (its harness, its fixtures, how
   it runs the form check through its command) and `installation/test_install.py`; the command
   surface of `product-guidelines/form_check.py` (its usage and exit codes, `guidelines-form-check-command`
   in `foundations/part_map.md`), and `gate/run_tests.py`'s rule on citing an invariant
   (`invariant: <identifier>` lines) and WAY-03, WAY-08, WAY-65, WAY-69.

Do not read: spec §5.2, §5.3 or any other part of the spec beyond those named; `plan.md`; the
reports of other agents; `reports/design*.md`; any reasoning about how the form check will be
changed. Do not read the body of `form_check.py` to fit your tests to its implementation; its
command surface and its existing findings' report lines are enough.

## What to write

Spec §9 lists the invariant tests the change needs; here is that list restated as your job:
coding files valid in both forms pass (general file and a kind file); a coding rule naming no
invariant fails (`guidelines-check-carrier`); a missing standing-check rule and a dropped one
(`guidelines-check-form`); kind-file names that disagree with *Discipline* `coding`
(`coding-.md`, `coding-Endpoint.md`, `coding--x.md`) (`guidelines-check-form`); the index both ways
and a kind file with no general file (`guidelines-check-kind-index`, including the clause on a row
whose *Kind* is not its file's kind or whose *When to read* is empty); the exemplar table cases —
two `exemplar` rows, none, a status off the list, a *File* git does not track, a decision whose
binding sentences do not name the path or the kind (`guidelines-check-exemplar`); a rule naming an
invariant without a good or bad block, without a pair for one of two named invariants, a block
naming an invariant the rule does not name, a refused path, a line opening a fence inside a case,
and a rule naming only `guidelines-form` that needs no blocks (`guidelines-check-example-files`);
and the existing valid styleguide fixture gains, for each rule naming an invariant other than
`guidelines-form`, a good/bad pair, so it stays valid. Every test cites its invariant as
`gate/run_tests.py` requires. Each test fails for the reason its sentence gives, never by accident.

Then run `python3 -B gate/run_tests.py product-guidelines` and `python3 -B gate/run_tests.py
installation` (Python 3.13.16; the repository declares 3.14) and record, by test name, which tests
are RED (expected: every new coding, index, exemplar and test-case test, and the `NAMES` test,
until the slices write the code) and that every test that passed at `05e44b1` still passes (or, if
an existing test now fails because the styleguide fixture changed, say why and which slice will
make it pass).

## Report contract

Each test: name, the invariant it cites, the sentence clause it checks, the fixture. Commands,
exit codes, output paths; the RED list by name; changed-file list with added/removed lines;
choices you made with the way rejected and the cost if wrong; questions. Return a short message:
status, commit, RED list summary, questions.
