PASS 7d9bc5a1e5b8801b9e5f2fea0cde09b8c0dc7fa7

# Review of the return step's commit after correction 1

Range `b8b1ce1..7d9bc5a` (`git rev-parse HEAD` = `7d9bc5a1e5b8801b9e5f2fea0cde09b8c0dc7fa7`, confirmed).
One commit, two files, 4 lines inserted and 4 deleted: `foundations/invariants.md` and
`process-audit/test_audit_series_scripts.py`.

Counts: blocking 0, Minor 1 (out of scope), out of scope 1.

## Findings

### Critical, Important

None.

### Minor

1. **Out of scope.** The phrase "the mechanism measures" stays in other files of the part that the
   range does not touch: `process-audit/SKILL.md:57`, `:60`, `:191`, `process-audit/audit_count.py:133`,
   `:411`, `:2381`, `:2425`, `process-audit/test_audit_count.py:2783`, `:2822`, `:2830`. WAY-339 speaks
   of "the measures of how a cycle's agents use the context and the prompt cache". The commit words
   the invariant and its test as WAY-339 words them, so the invariant and the rest of the part now
   name one set of measures in two ways. `process-audit/SKILL.md:57` defines "The mechanism measures"
   by that longer phrase on its first use, so a reader is not left without an explanation, and the
   invariant's earlier wording used the same short name. No sentence is read wrongly for lack of it,
   so Minor; a reach beyond this handoff, not fixed here.

## What was judged

- **Sentence against the test and WAY-339.** The new sentence reads: each path of a script whose
  history `process-audit/audit_count.py` reads, to start a new series of the measures of how a cycle's
  agents use context and the prompt cache or of the gate times — the script that counts those
  measures, the script that records the gate times and the test runner of the gate — is a file git
  tracks. It is one rule (each path is a tracked file). Its measures phrase is the one WAY-339 uses
  ("the measures of how a cycle's agents use the context and the prompt cache"), and its three
  scripts are those WAY-339 names (the script that counts them, the script that records them, the
  test runner). The test checks the three paths `MEASURES_SCRIPT`, `GATE_SCRIPT` and
  `GATE_TEST_RUNNER` (`process-audit/audit_count.py:414-416`) with `git ls-files`, and that the gate
  scripts are the two that start the gate series (`:417`). The sentence says what the test checks.
- **Form against `elements/invariants/template.md`.** One sentence, no branch name, no `{fork-point}`,
  Method / Rests on / Derives from (WAY-339) / Part / Violated untouched; the sentence needs no
  quantity bound. The one condition that decides truth (a path tracked by git) stands in the sentence.
- **Docstring.** `process-audit/test_audit_series_scripts.py:1-4` carries the same words as the
  sentence, in the same order; the three test bodies and their "Break caught" comments are unchanged.
  The test's behaviour is unchanged (diff touches only the docstring lines).
- **Nothing else changed.** The diff has no other file; the line `- **Verification:** invariants:
  audit-series-script-paths` in WAY-339 (`foundations/decisions.md:7360`) and the identifier and
  `- **Derives from:** WAY-339` line of the invariant are intact; the heading
  `## audit-series-script-paths` is unchanged. No `decision:` or `invariant:` citation line changed.
- **The changed invariant test** is named: `process-audit/test_audit_series_scripts.py` (docstring
  only, cites `audit-series-script-paths`).
- **Note on the sentence's measure-script reading.** "The script that counts those measures" ties
  `MEASURES_SCRIPT = task-cycle/cycle_measures.py` to the measures as WAY-339 does; WAY-339's wording
  "the test runner of the process" versus the sentence's "the test runner of the gate" is a
  pre-existing difference of the earlier wording, not touched by the commit, and not a departure that
  a reader would read wrongly (`gate/run_tests.py` is both).

## Declined to judge

- The rest of the correction-1 range (`reports/review-correction-1-report.md`, `PASS b8b1ce1`): reviewed
  there; this handoff is the one commit after it.
- Use of "mechanism measures" in the other files of the part (see the Minor note above): left to a
  separate decision.

## Checks run

| Check | Command (from the worktree) | Exit |
|---|---|---|
| Foundation check, citations included | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Tests of the part | `python -B gate/run_tests.py process-audit` | 0 (`Ran 185 tests in 200.910s`, `OK`) |
| Diff of the range | `git diff b8b1ce1..HEAD`, `git log --oneline b8b1ce1..HEAD` | 0 (one commit) |
| Search of other uses of the old phrase | Grep `mechanism measures` outside `.runs/` | ten hits listed in Minor 1 |

No check could not be run. The gate as a whole was not run, as the handoff says.

## Reaches beyond the dispatch

- `foundations/decisions.md:7339-7375` (WAY-339, read whole): the handoff names it, but it is not
  listed as given text; read to compare wording.
- `process-audit/audit_count.py:414-417` and `process-audit/test_audit_series_scripts.py`, whole: to
  see what the test checks, as the handoff's "judge" asks.
- Grep of `mechanism measures` in the worktree (outside `.runs/`): to see whether the rewording leaves
  the same set of measures named two ways elsewhere; result in Minor 1.
- `foundations/invariants.md:395-412` for the entry in context.

## Working copies

None made. No directory `.runs/review-return-2/` was needed; nothing to remove.

## Unread material

None of what the dispatch names. Not read whole: the glossary term `dependency of a part` (the
handoff says "if you need it"; it bears on neither changed file), and `reports/return-step-2-report.md`,
`reports/correction-1-remarks.md`, `reports/review-correction-1-report.md` and `task.md` were not
opened — the handoff gives their claims, and the commit's two files stand on the entries judged above.

## Searches not found or unclear

None.
