# Report of correction 1 — part-map-dependencies-task-line

**Status:** done. **Commit:** `b8b1ce1` on `task/part-map-dependencies-task-line`, from `1e45b6e`
(six files: `foundations/decisions.md`, `foundations/invariants.md`,
`elements/part-map/template.md`, `elements/common/migrate_foundation.py`, the test of the audit's
scripts renamed from `process-audit/test_gate_runner_path.py` to
`process-audit/test_audit_series_scripts.py`). No file of a trust boundary was changed:
`process-audit/audit_count.py` is untouched; the test only reads its constants.

## The remarks, each as made, and how

**Remark 1, first — the term in the rule on a dependency the map does not allow.** Done, with the
consent the remarks give (the change is the term only):
- WAY-225 (`foundations/decisions.md`), binding sentence: "a dependency of a part that the code
  holds and the part map does not allow is recorded as an invariant the product does not meet
  (WAY-51), never by rewriting the allowed dependencies of a part to fit the code." Its pair of
  examples says "allowed dependencies of a part", "dependencies of a part that the code holds" and
  "a dependency of a part that the code holds and a human accepts"; the *violates* example says
  "the allowed dependencies of a part in the part map".
- WAY-51, *Rejected*: "a derived list of the dependencies of a part that the code holds against the
  part map … a dependency of a part that the map does not allow is an invariant like any other".
- *Searched once for each other place that states the same sentence with the bare word*
  (`git grep` for "not allow", "allowed dependenc*", "dependency the code/map", "dependencies it/its",
  "rewrit* the allowed"): the other hits are the part-map template and skill (already corrected in the
  fix), the title of the withdrawn row WAY-299 (history; left), a docstring of a test (imports),
  and a line of the decision log about moving an entry ("does not allow" in another sense), unrelated. No further place found.

**Remark 1, second — the part-map template says one sentence for a part.** Done in
`elements/part-map/template.md`: the part placeholder reads "what this part is responsible for,
briefly, in as few sentences as that needs"; the surface placeholder the same for the promise; the
section "Surfaces" says the entry states the promise briefly in as few sentences as it needs; the
section "The binding part" reads "a part's responsibility or a surface's promise, each described
briefly, in as few sentences as it needs". I took the surface along because the map's own surfaces
(`installation-command` and others) hold several sentences, which is the same disagreement the
remark names.

**Remark 1, third — guard the two reads the reviews named.**
- *The copy of the guidelines pattern* in `elements/common/migrate_foundation.py`: removed, the
  script imports `GUIDELINES` from `foundation_check.py` (same part, so `cross-part-imports` stays
  green). No test and no invariant needed: with no second copy there is one source.
- *`MEASURES_SCRIPT` and `GATE_SCRIPT`* of `process-audit/audit_count.py`: I widened the invariant
  `gate-runner-path` to `audit-series-script-paths` (a new identifier; the old one never reached the
  main branch): "Each path of a script whose history `process-audit/audit_count.py` reads, to start
  a new series of the mechanism measures or of the gate times — the script that counts the measures
  of a cycle, the script that records the gate times and the test runner of the gate — is a file
  git tracks." *Part:* `process-audit · task-cycle · gate`; still one rule (the same check over a
  set), `Derives from: WAY-339`, whose *Verification* names the new identifier. The test
  `process-audit/test_audit_series_scripts.py` cites it by `invariant:` and also checks that the
  audit's list of scripts for the gate series is the two it names, so a path added to the audit is
  not left unguarded.

**Remark 2 (let through):** nothing to do.

## Checks (command, exit code)

Failing once, then passing, of the widened invariant's test (the writing side moved with
`git mv`, then moved back; nothing of it is in the commit):
- `task-cycle/cycle_measures.py` moved: `python -B -m unittest process-audit/test_audit_series_scripts.py`,
  exit 1.
- `task-cycle/gate_times.py` moved: same command, exit 1.
- `gate/run_tests.py` moved: same command, exit 1.
- Unbroken: same command, exit 0; then `python -B gate/run_tests.py process-audit`, exit 0.

Other checks:
- `python -B elements/common/foundation_check.py` (no skip switch): exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common`: exit 0 (the migration script's tests included).
- `python -B gate/run_tests.py elements/part-map`: exit 0 (`cross-part-imports`).
- `python -B gate/run_tests.py installation`: exit 0 (it runs the migration script from a pinned
  `.the-way`, where the new import must resolve beside it).
- No skill description and no agent type changed, so no generator was run. The whole gate not run.

## Own-work check

Requirement most likely missed: the meaning of WAY-225 must not change, and the script must behave
as before. A change in meaning would show in the foundation check (a `decision:` quotation of
WAY-225 would fail) and none does, exit 0; the behaviour of the migration is covered by its own
tests and the installation test that runs it from `.the-way`, exit 0 for both.

## Findings of my own, not changed

- `foundations/part_map.md:20` (the `part-map` sentence, "the dependencies it allows") and
  `foundation-review/weak_points.md:84` ("a part whose files or dependencies the code no longer
  follows") still say the bare word in the map's meaning; they do not state the sentence of WAY-225,
  so the remarks do not cover them.
- A run of `git grep` on the decision log found the title of the withdrawn row WAY-299 with the
  bare word; a withdrawn row records history and is left.

## Reach beyond the dispatch

None.

## Unread material

none (the remarks, the handoff, `change/SKILL.md` whole; the files edited read before editing;
`reports/review-whole-report.md` read at M-3, M-4, O-1, O-2 and `review-whole-fix-report.md` whole).
The skill of the invariants element and its template I had read earlier in this cycle and did not
reread.

## Searches not found or unclear

none.

## Working copies

`.runs/author-correction-1/` held run outputs and the commit message; removed before return. No
worktree or clone made.
