# Executor report — slice 10: a missing field of a skill ends `skill_entry_points.py` with exit 2

Status: **done**

## Commits (branch `task/the-way-coding-and-testing-guidelines`, base `6cf3fa9`)

| Commit | Subject | Files | Added | Removed |
|---|---|---|---|---|
| `c1ab102` | Test that a skill without a name or a description stops with exit code 2 | `agent-instructions/test_skill_entry_points.py` | 24 | 4 |
| `0645ec7` | Make a skill without a name or a description end the generator with exit code 2 | `agent-instructions/skill_entry_points.py` | 16 | 1 |

The test commit goes first on purpose: the two new tests were seen failing on the base before the code changed.

## Checks

Each check as command and exit code. Run from the worktree root `the root of the worktree`.

1. Failing run on the base, after the tests were written and before the code changed:
   `python -B agent-instructions/test_skill_entry_points.py` → exit **1**, `Ran 15 tests`, `FAILED (failures=2)`. The two failures are the new tests `MissingField.test_a_skill_without_name_stops_with_exit_2_naming_the_field` and `MissingField.test_a_skill_without_description_stops_with_exit_2_naming_the_field`. Both stopped at their assertion, not at an import or a missing file: the base returned `(1, '', "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n")` and `(1, '', "Error: a/SKILL.md: frontmatter has no 'description:' with a value\n")`, where the tests expect exit 2 with `the frontmatter has no line `name:`` and `…description:`.
2. Passing run after the code change: `python -B agent-instructions/test_skill_entry_points.py` → exit **0**, `Ran 15 tests … OK`.
3. `python -B agent-instructions/skill_entry_points.py` → exit **0**, output `entry points are current`. `git status` afterwards showed only the modified generator file, so the run wrote nothing.
4. `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py` → exit **0**, `All checks passed!`.
5. `python -B elements/common/foundation_check.py --skip-test-citations` → exit **0**, `0 errors`.
6. Not run: the product gate (`gate/run_tests.py` without a directory), as the handoff forbids (WAY-160). The focused run of `agent-instructions` as a directory was not run either; the test file was run directly, as the slice's *Checks* names.

## Own-work check (section 3)

- Requirement that my work most likely misses: the exit code must be 2 only where a field has no line at all, and every other error must keep exit 1. The risk was that the new check would swallow the existing `empty name` case, or the `no frontmatter` and `unclosed frontmatter` cases.
- Check: the existing `FrontmatterErrors` table still asserts exit 1 for `no frontmatter`, `unclosed frontmatter`, `byte order mark`, `empty name` and the other rows; it passed in run 2 (exit 0). The check I added runs after the frontmatter delimiters are found, so the no-frontmatter errors come first, as before.
- Mutation in my head: removing the new check, or returning 1 where it returns 2, makes the two new tests fail (the base run above is the proof for removal). Removing `re.IGNORECASE` changes behaviour only for a line such as `Name:`; **no test catches that** (see Questions, item 1).

## Choices

1. **The missing-line rule is written again inside `skill_entry_points.py`, not imported from `agent_type_copies.py`.** `agent_type_copies.py` imports `skill_entry_points`, so an import the other way would be circular. Moving the helper into a third module would widen the slice. Cost if wrong: the two copies of a four-line rule can drift apart; the slice's *Goal* asks that the two generators agree, so a later change to one should be made in both.
2. **The rule counts a line in another form (`Name:`) as present**, as `agent_type_copies.missing_field` does, with the same regex `\s*{field}\s*:` under `re.IGNORECASE`. Consequence: a skill with `Name: alpha` and no `name:` line gets exit 1 with `frontmatter has no 'name:' with a value` (the existing message), not exit 2. This matches `agent_type_copies.py`, where `Name:` gives exit 1 too. Cost if wrong: a reader of WAY-344 who reads "stands under another name" as "missing" would want exit 2 here.
3. **The two rows `no name` and `no description` were removed from the `FrontmatterErrors` table, not changed to exit 2 in it.** They now belong to the new `MissingField` class, which names the message and the exit code of each. The row `empty name` stays with exit 1, since its line exists and has no value.
4. **Two commits, test first.** The failing-test commit is kept in history so that the base failure is visible; no squash.

Rejected alternative for choice 2: exact-case match (`name:` only). It would have made `Name:` a missing field with exit 2, but it would differ from `agent_type_copies.py`, which the slice asks it to agree with.

## Adaptations of section 4

None. The plan's *Read* and *Change* matched the code: `skill_entry_points.py` had `read_skill` raising at the `frontmatter has no '{field}:' with a value` line, as the task's cause 17 says.

## Reaches beyond the handoff

None beyond the handoff's *Read*. I read `task-cycle/change/SKILL.md` and `slice.md` whole, as the method names them. I did not read `agent-instructions/README.md` or any guideline file, as the slice does not name them.

## Working copies

None made. No `.runs/executor-10/` directory was created, so there is nothing to remove.

## Unread material

- `task.md` lines 45, 135–147 and 335–341: read in the ranges the handoff gives.
- `foundations/decisions.md` WAY-344 (2823–2968) and WAY-386 to WAY-391 (the entries of E8): read whole.
- `foundations/invariants.md` `derived-file-content` (56–65), `skill-entry-points` (271–280), `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `cross-part-imports`: read whole.
- `foundations/part_map.md` `agent-instructions` (155–173): read whole.
- `agent-instructions/agent_type_copies.py` and `test_agent_type_copies.py` 160–209 (the way the other generator does it): read whole for the script; the test file read in the ranges that show `MissingField` and the helpers (lines 1–60 and 160–209; the rest of the file not read).
- `plan.md`: the header (1–13), *Choices* (1003–1020) and *Orchestrator's additions* (1021–1041) were read whole. The section of Slice 10 was not read from the plan; I worked from the handoff's copy, as the handoff asks.
- `ruff.toml`: read only the head and the first rule set; I relied on the linter's pass rather than on the rule list.

## Searches not found or unclear

- None missing. One thing was unclear and I settled it by reading the code: whether the handoff's `E8` means the six exemplar decisions (WAY-386 to WAY-391) or the exemplar `skill_entry_points.py` decision alone. I read all six; the handoff's table says WAY-386 to WAY-391 are the E8 set, so I took that reading.

## Questions

1. **Should `Name:` (a line in another form, with no `name:` line) end with exit 2 or with exit 1?** Current code gives exit 1, matching `agent_type_copies.py`. The rule in WAY-344 says "stands under another name the script ends with an error that names it", and that could be read as exit 2. Recommended answer: keep exit 1, as `agent_type_copies.py` does, so the two generators agree; the behaviour is then not pinned by any test, and if you want it pinned, I can add a third test (about 8 lines) that gives `Name: alpha` and asserts exit 1 with the message above.
2. **Should the missing-line rule live in one shared place?** Recommended answer: no, not in this slice. The two copies are four lines each; a shared module would be a separate change that touches `agent_type_copies.py`, which is outside this slice's *Change*.

## Weakest point and the check made of it

The weakest point is the loose line match (choice 2 and Question 1). I checked it by reading the code path, and by the fact that the existing `empty name` case still gives exit 1 in the passing run. The `Name:` path itself I did not run.

## Problems observed

None in the code. The repository's commit history shows short English subjects without a type prefix; my commit subjects follow that.

## Addendum — strict field check (orchestrator's answer to Question 1)

The orchestrator ruled that `Name: alpha` with no lowercase `name:` line is a missing field: exit 2,
naming the file and `name:`. The loose match of `agent_type_copies.py` is not copied. The check now
counts a field as present only where a frontmatter line fullmatches the generator's own `FIELD`
reading (lowercase at the line start). An empty-valued line such as `name:` still ends with exit 1.

Commits added on the branch, after `0645ec7`:

- `cf302df` Test that a skill with the name in another form stops with exit code 2 (test file, one new test).
- `d84dc5b` Count a skill field as present only in its lowercase form (`skill_entry_points.py`, +4/−4).

Checks:

1. Failing run before the code change: `python -B agent-instructions/test_skill_entry_points.py` → exit **1**, `Ran 16 tests`, `FAILED (failures=1)`. The failure is the new `Name:` test: the base returned `(1, '', "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n")`, where the test expects exit 2 and `the frontmatter has no line `name:``.
2. Passing run after the change: `python -B agent-instructions/test_skill_entry_points.py` → exit **0**, `Ran 16 tests … OK`.
3. `python -B agent-instructions/skill_entry_points.py` → exit **0**, `entry points are current`; `git status` shows no write.
4. `<ruff> check --config ruff.toml --no-cache --ignore-noqa agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py` → exit **0**, `All checks passed!`.
5. `python -B elements/common/foundation_check.py --skip-test-citations` → exit **0**, `0 errors`.

The description's exit-code sentence already reads "has no line `name:` or no line `description:`",
which holds under the strict rule, so it is unchanged. The `Question 1` answer leaves
`agent_type_copies.py` alone, and no rule is shared between the generators (Question 2).
