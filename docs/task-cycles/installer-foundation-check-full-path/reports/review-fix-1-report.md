PASS 674c93feda110b00fab3327546a41ca26ac5e860

# Review of fix 1 — installer-foundation-check-full-path

- Range: `1c222ce238c2194900ec246de5f8cc6cfa7faa5b..674c93feda110b00fab3327546a41ca26ac5e860`, one
  commit `674c93fe`. `git rev-parse HEAD` in the reviewed worktree gave
  `674c93feda110b00fab3327546a41ca26ac5e860`, the head the handoff gives.
- Changed files (`git diff --numstat`):
  - `foundations/decisions.md`: +2 / -1
  - `foundations/invariants.md`: +1 / -1
  - `installation/test_install.py`: +6 / -2
  These match the author's report.
- Counts: 0 blocking findings; 1 new Minor finding, within the task; 0 outside the task's scope.

## The findings of `reports/review-whole-findings.md`

**1. WAY-418's *Verification* does not name the invariant the change derives from it — fixed.**
- `foundations/decisions.md:3349-3350` now reads "invariants: installation-agents-md-warnings. An
  agent compares a change with the part no invariant and no test holds:". The pair of examples
  stays word for word. This is the form of `elements/decisions/template.md:42-44`, with no `tests:`
  clause, which is right: no test carries a line `decision:` for WAY-418.
- The binding sentences, *Scope*, *Based on*, *Relations*, *Origin*, *Rationale* and *Rejected* are
  unchanged (the diff touches only the *Verification* line).
- Evidence: the probe of the first review, run on the new head, gives "15 of 75 links not named",
  and `installation-agents-md-warnings <- WAY-418` is no longer among them. The remaining 15 are the
  older ones set aside in the first review.
- `python -B elements/common/foundation_check.py` on the head: exit 0, `0 errors`.

**2. The new test lets an error on the root `AGENTS.md` pass — fixed.**
- The filter at `installation/test_install.py:456-458` is now `(?:ERROR|WARN) +\S+ AGENTS\.md:`.
- Evidence: the mutation of the first review (`error-line`, "See @docs/rules.md." added to the
  sentence about the part map) now turns the test red, exit 1: `['ERROR at-import AGENTS.md:10
  @docs/rules.md. — a punctuation mark right after the path stops Claude Code from loading it,
  without a warning'] != []` (`reports/review-fix-1-probe-error-line.txt`).
- The two earlier mutations, `old-sentence` and `no-ignore-line`, still turn it red (exit 1 each).

**3. The invariant's sentence can be read to cover the product's own lines of `AGENTS.md` — fixed.**
- `foundations/invariants.md:336` now ends "…reports no warning on the root `AGENTS.md` that the
  run created." A product whose `AGENTS.md` existed before the run is no longer covered.
- The test builds an empty product, in which the run creates `AGENTS.md`, so the test checks what
  the sentence says.
- The sentence was reworded, and the file that cites it, `installation/test_install.py`, changed in
  the same branch, so `foundation_check.py` does not list it under WAY-03. The request still names
  this invariant test, as the first review listed.

## Findings in the fix diff

### Minor

**4. The invariant's test refuses an error that its sentence does not name**
(`installation/test_install.py:453-458` against `foundations/invariants.md:336`; new in this fix,
within the task).

The sentence of `installation-agents-md-warnings` says the checker "reports no warning". The test
that cites it now also fails on a line `ERROR … AGENTS.md:`. So a block that draws an error and no
warning makes the test, and through it the invariant's result, read `fail` (WAY-08: "The status of
an invariant with a test comes from running that test"), although its sentence holds. The template
asks that "A test checks what its sentence is about" (`elements/invariants/template.md:55`).

The consequence is small, and I do not grade it higher. The extra assertion fails only on a real
defect: an error stops every product's one command, and the guidance block itself says so at
`installation/install.py:213`. The failure message shows the level `ERROR`, so whoever reads it is
not misled about what broke. The comment at the assertion gives the reason.

Two ways to close the gap; the choice is the cycle's:
- (a) The sentence says "reports no warning and no error". This changes the invariant beyond the
  words of row 2 of *Settlements to record*, so it may need the human under WAY-30.
- (b) Leave it as it stands and accept a test stricter than its sentence.

## Declined to judge

none. Outside the fix diff I considered nothing new.

## Checks run

| Command | Where | Exit | Result |
|---|---|---|---|
| `git rev-parse HEAD`; `git log` / `git diff` / `git diff --numstat 1c222ce2..HEAD` | reviewed worktree | 0 | head matches; 1 commit; counts above |
| `python -B instruction-files/check_instructions.py` (the instruction check, as `installation/README.md:82` gives it, in the-way without `.the-way/`) | reviewed worktree, head | 0 | `0 error, 0 warn, 5 info` |
| `python -B elements/common/foundation_check.py` | worktree of the head | 0 | `0 errors` |
| `python -B derived_links.py .` (the probe of the first review) | worktree of the head | 0 | `15 of 75 links not named`; WAY-418 not among them |
| `python -B -m unittest test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation` | worktree of the head, `installation/` | 0 | 2 tests OK |
| `PYTHONIOENCODING=utf-8 python -B probe.py error-line` | review directory, head worktree restored after | 1 | test red on the `ERROR` line (finding 2 fixed) |
| `python -B probe.py old-sentence` | same | 1 | test red on the bare `foundation_check.py` |
| `python -B probe.py no-ignore-line` | same | 1 | test red on `.runs/` |
| `python -B -m unittest test_linter_invariant` (Ruff linter and formatter invariants) | worktree of the head, `agent-instructions/` | 0 | OK |

- The first run of the `error-line` probe broke in the probe itself, not in the test. The test's
  failure message holds an em dash, which the console's code page could not decode into the probe's
  captured output. The run was repeated with `PYTHONIOENCODING=utf-8` and is the row above.
- The worktree had `git status --short` empty after each probe.
- Not run: the full gate (as the handoff says), and the whole `installation` directory. The author
  reports exit 0 (74 tests); I ran the two tests the fix reaches.

## Reaches beyond the dispatch

- `elements/decisions/template.md:42-44` and `:270-310`, and `elements/invariants/template.md:55`,
  re-read from the first review: the form of the *Verification* and the rule of finding 4.
- `foundations/decisions.md` WAY-08 (binding sentence, from the index of the first review): the
  result of an invariant, for finding 4.

## Working copies

All stood in `.runs/review-fix-1/`:
- a worktree of the head (`head`), removed with `git worktree remove --force`, then
  `git worktree prune`;
- copies of the two probe scripts of the first review, and their outputs.

The directory was removed (`rm -rf` by its full path). The output that finding 2 needs is kept as
`reports/review-fix-1-probe-error-line.txt`. The reviewed worktree, its index and its branch were
not changed.

## Unread material

none. The findings file, the author's report of the fix, the handoff, `task-cycle/review/fix.md`
and the fix diff were read whole.

## Searches not found or unclear

- Whether naming errors in the sentence of `installation-agents-md-warnings` (option a of finding 4)
  needs the human under WAY-30. It is unclear: it widens the rule that row 2 settles, so I leave
  that choice to the cycle.
