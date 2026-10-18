# Invariant-check handoff (F4)

The user invoked `the-way-implement-task` and delegated intermediate choices to the root
orchestrator. You are the check author of six invariants (WAY-69: the sentence, its check and the
code it covers come from three different agents). You did not write the sentences and you will not
write the code they cover; you write only their check. Send questions to the root by returning
them; never ask the human.

- Worktree: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
  `task/product-guidelines-styleguide`, head `eb9ff1e`.
- Your inputs — read these, and nothing about how the covered script is or will be built:
  - the six entries `guidelines-check-form/1`, `guidelines-check-carrier/1`,
    `guidelines-check-colour-pair/1`, `guidelines-check-reference-target/1`,
    `guidelines-check-stale-reference/1`, `guidelines-check-code-path/1` in
    `foundations/invariants.md:2153-2212` (read each whole: sentence, *Method*, *Part*,
    *Derives from*), and the entries they derive from in `foundations/decisions.md` as named there;
  - the external contract of the covered command, in `.runs/task-cycles/product-guidelines-styleguide/spec.md`:
    §3.1 and §3.2 (the form of a guidelines file and its references), §4.1 and §4.2 (the merged
    form of a styleguide), §5.1 (command, options, exit codes, report line form, record), §5.3
    (what it reports as an error). These are the observable behaviour the sentences speak of; do
    not read §5.2, §5.4, §5.5 or any later section, the plan, or reports;
  - how the-way writes invariant tests: `elements/invariants/template.md`, the test runner
    `gate/run_tests.py` (how it discovers tests and records verdicts, WAY-65 citations), and as a
    pattern `gate/test_wording_reaches_dependants.py` (temporary git repositories, literal
    fixtures, a test guarding its fixture's wording);
  - `relation-model/fingerprint.py` only to compute expected fingerprints for your literal
    fixtures once, by hand; write the expected values as literals in the test.
- Write only `product-guidelines/test_form_check_invariants.py`. Tests run the command
  `python -B product-guidelines/form_check.py` as a subprocess on temporary git repositories you
  build (a product root with `foundations/decisions.md`, `foundations/invariants.md`,
  `foundations/part_map.md` as needed, and `guidelines/<name>.md`), and assert exit codes, report
  lines and record lines. Each test cites in its body the invariant it gives a verdict for
  (`# invariant: <identifier>/1`, WAY-65). Inputs, expected fingerprints and expected message
  fragments are literals. Cover what each sentence speaks of, including: form errors; a rule
  without its carrier; a background role without a text role; references in *Decision* and
  *Invariant* fields, in `## Roles` rows, in rule prose, under `## Examples` and in a `none —`
  departure line; a reference to an absent or repealed decision and to an absent or withdrawn
  invariant; a reference whose fingerprint is stale on the same commit and, with `--merge-onto`,
  after a merge where a decision or an invariant changed only on the onto commit; versioned
  package names such as `react@18` not taken for references; a token in fenced code ignored; code
  paths `../outside.md`, `/etc/passwd`, `C:\x`, `\\host\share\x`, `:(glob)**`, `http://host/x`
  and a path git does not track rejected.
- The covered script does not exist yet: your first run fails. Record that failure with command,
  exit code and full output (never hide it with a skip). The file becomes read-only for the
  executors of the covered code (WAY-03).
- Commit only your file by explicit path, English message in the repository's style
  (`test(product-guidelines): …`).

Report to `.runs/task-cycles/product-guidelines-styleguide/reports/check-author.md`: the tests
written per invariant and what each asserts, the literal fixtures and how you computed expected
fingerprints, the run command with exit code and full output path
(`reports/check-author-run.txt`), the changed-file list with added/removed lines for your commit,
any sentence you found ambiguous (a question, not a reading you chose silently), unresolved
concerns. Return status, commit, run result and questions only.
