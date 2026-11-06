# Findings 2 — blocking findings of the review of correction 1

Source: `reports/14-review-correction-1-report.md`, `FAIL 8cbcac0b8dab89fcd56257955bd6f5c62c1194ff`, range `79bd480..8cbcac0`. The reviewer's words, copied:

### Important

**I1 — a command line of `sys.executable` whose script is joined on after the list is read as
running no file, and passes in silence.**

- Place: `elements/part-map/test_cross_part_imports.py:298-322` (`command_line`): when the
  elements after the interpreter are only options, or none, the loop ends without a target and
  without a problem; `command` (:279-282) reads only the list literal, so a script added by `+` or
  `.append` is never seen. The fixture `subprocess.run([sys.executable])` (:783) pins "no target,
  no problem" as intended.
- What is wrong: the remark asks that a new process of the running interpreter given a path counts
  as an import "and its test reads such runs"; the docstring (:19) promises "A use of
  `sys.executable` the check cannot read as a command line fails it" and (:26-27) "a check that
  quietly sees less would pass". Both are false for these forms, which are ordinary ways to build
  a command line (the tree already has `[sys.executable, "-B", RUNNER] + list(arguments)`,
  `gate/test_run_tests.py:55`, one argument away from it).
- Evidence: scratch probe
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\gaps.py`,
  each line placed in `core/engine.py` of the test's own fixture repository, where `core` may not
  depend on `shell`:
  - `subprocess.run([sys.executable, '-B'] + [os.path.join(HERE, '..', 'shell', 'screen.py')])`
    → `([], [])`;
  - `subprocess.run([sys.executable] + [<same path>])` → `([], [])`;
  - `cmd = [sys.executable]` / `cmd.append(<same path>)` / `subprocess.run(cmd)` → `([], [])`.
  The same run written as one list is reported as forbidden (`test_each_form_of_a_run_is_seen`).
- Why Important: this is the requirement the remark adds, and the gap is of the kind remark 1
  (M1) asked to remove: the invariant's only test passes while seeing less. No instance on
  today's tree.
- Possible fix: a command line that ends with no target, no `-c`, no `-` and no `-m` fails as "runs
  a command line the check cannot read" (and the fixture at :783 moves to the failing cases), or a
  list of `sys.executable` that is an operand of `+` or a name later mutated fails the same way.

