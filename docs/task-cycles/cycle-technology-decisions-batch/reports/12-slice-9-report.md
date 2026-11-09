# Slice 9 report — README: product guidelines and the host-state source

**Status:** done

## Commits

- `da8c818` Name the reading of a host's state among the README's sources (branch `task/cycle-technology-decisions-batch`)

## Files changed

- `README.md`: 5 insertions, 3 deletions

## Change made

1. Sources list (`README.md:48-51`): added a clause that a state of a host the product's people run, which only those with access can read, is recorded as a reading: the command, the host, the tool with its version, its output and the date it was run. Wording follows WAY-80.
2. Table row for `environment_facts.md` (`README.md:77`): added the same host-state reading after the address / quoted passage / date clause.

## Left unchanged on purpose

- Product-guidelines sentence (`README.md:114-118`): it already says the template and the skill that leads the work exist for each discipline with a template (styleguide, coding, testing), as WAY-09 gives. Per the slice, nothing changed there.
- Trust boundary: none of this slice's files is one. Irreversible operation: none. No decision or guarantee changed.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Private-paths unittest | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | Ran 9 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | 0 errors |
| Whitespace check | `git diff --check` | 0 | clean |

An earlier attempt at the unittest wrote output to `/tmp/x`, which is a directory in this shell, so the redirect failed and the run printed no result. It was rerun with output to the scratchpad and passed; the exit code above is from that rerun. The full suite (`gate/run_tests.py`) was not run, per the handoff.

## Own-work check

- Requirement: the README must say the reading of a host's state is a source, in both places WAY-80 touches, and must not change the product-guidelines sentence unless it lacks what WAY-09 gives.
- Check: `grep -n host README.md` shows the host clause at lines 49-51 (sources list) and 77 (environment_facts row); the product-guidelines sentence was compared by reading it against WAY-09 (template and skill per discipline, styleguide/coding/testing listed).
- Result: both host-state places present; product-guidelines unchanged, as WAY-09 already matched.
- Prose only; no test was written, since the change is wording with no behaviour a test can check (per the method's "prose for people gets no test").

## Reaches beyond the handoff

- Read `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` and `agent-instructions/README.md` as the handoff directed.
- Read `foundations/decisions.md` WAY-09 and WAY-80, `foundations/glossary.md` environment fact and read off, and `foundations/invariants.md` tracked-file-private-paths, at the handoff's line ranges. Did not read WAY-322 (not relevant to README wording) or the plan's Foundation entries table.
- Read the whole README to find the two target sentences (it was small).

## Searches not found or unclear

- none. Drift check: the handoff's ranges matched the current text (sources at 48-49, environment_facts row at 75 before the edit, WAY-09 and WAY-80 at their current ranges).

## Choices and adaptations

- Amended my own unpushed commit once to replace a first subject line that claimed a product-guidelines change I did not make.
