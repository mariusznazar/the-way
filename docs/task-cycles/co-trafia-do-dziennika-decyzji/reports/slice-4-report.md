# Slice 4 report — An invariant whose sentence changed while its test did not

## Status

`done`

## Commits

- `12286a5` List an invariant whose sentence changed while its test did not (on `task/co-trafia-do-dziennika-decyzji`, base `ea2d186`)

Worktree left clean. Nothing pushed.

## Files changed

| File | Diff |
|---|---|
| `elements/common/foundation_check.py` | +78 lines (docstring bullet, two module helpers, one method, one call in `run`) |
| `elements/common/test_foundation_check.py` | +90 lines (nine tests, one fixture method, two constants) |
| `README.md` | 6 lines changed |
| `agent-instructions/README.md` | 8 lines changed |

Total: 177 insertions, 5 deletions (`git diff --stat ea2d186..HEAD`).

## Checks

Commands run from the worktree root, with exit codes.

1. Baseline before any edit: `python -B gate/run_tests.py elements/common`, exit 0, 189 tests OK.
2. Red, before the code: `python -B elements/common/test_foundation_check.py -v -k reworded -k citing_file_deleted -k invariant_added`, exit 1, 1 failure: `test_reworded_sentence_with_its_citing_file_unchanged_is_listed` (`'foundations/invariants.md:3: listed: \`save-round-trip\`' not found in '0 errors'`). This is the failure the slice asks for.
   - The other eight tests in that run passed before the code. They check that no listing appears, which the old script never wrote, so they pass for a reason that predates the change. Named as such: `test_reworded_sentence_with_its_citing_file_changed_is_not_listed`, `test_citing_file_deleted_is_a_change_and_not_listed`, `test_reworded_sentence_in_spacing_only_is_not_listed`, `test_reworded_sentence_whose_method_reads_review_is_not_listed`, `test_invariant_added_with_its_citing_file_is_not_listed`, `test_reworded_invariant_with_no_citing_file_is_not_listed`, `test_reworded_invariant_lacking_method_or_part_now_adds_no_listing`, `test_reworded_invariant_lacking_method_or_part_at_base_adds_no_listing`.
3. Green, after the code: the same command, exit 0, 9 tests OK.
4. `python -B gate/run_tests.py elements/common`, exit 0, 198 tests OK (includes `test_the_way_foundation_passes`, which reads the WAY-03 quotations of the new `decision:` lines against the real entry).
5. `python -B gate/run_tests.py elements/part-map`, exit 0, 39 tests OK.
6. `python -B elements/common/foundation_check.py` on this repository, exit 0, `0 errors`. One listed line, `foundations/decisions.md:578: listed: WAY-17 is held by nothing`, comes from the slices 1 to 3 behaviour, not from this change. The-way has no `main` or `master` branch, so the base is unknown here and no invariant can be listed on this repository.

Line lengths: the three edited Python passages I wrote are within 100 characters. Other over-100 lines already existed before this slice and are left as they were.

## Own-work check (section 3)

- Requirement: the listing lists an invariant only when its sentence changed, its method reads `test`, a citing file exists at base or now, and no citing file differs from the base. A listing must never change the exit code.
- Check: the nine tests above, plus the exit-code assertion in the listed case.
- Result: all nine pass. The changed-citing-file case and the deleted-citing-file case each show the change rule working in both directions.
- Mutation thought: dropping the `changed` set makes `test_reworded_sentence_with_its_citing_file_changed_is_not_listed` fail. Dropping the base-side citing set is caught by no test. A file that cites at base and is unchanged also cites now, so the base-side set matters only for a file that changed or was deleted, and both are already excluded. The behaviour is correct but not protected by a test that would fail on its removal. This is a note, not a bug.

## Choices

1. **Changed files come from `git diff --name-only --no-renames -z <base>`** rather than comparing file bytes read from the base and from disk. Rejected: a byte comparison, which counts a line-ending difference as a change. Cost of the choice: a change git sees as no change (for example, a line-ending change that git normalises away) is not treated as a change, so a citing file that differs only that way can still let the listing fire. This is the safe direction for the listing.
2. **Base citing files are found with `git ls-tree -r` and `at_commit` only when a candidate invariant exists**, to avoid reading every file at the base on each run. Cost: none beyond the candidate check.
3. **Reworded README sentence split.** In `agent-instructions/README.md`, the sentence that also named `migrate_foundation.py` was split into two sentences so that the new script description fits. The words about `migrate_foundation.py` are unchanged in meaning.
4. No change to any slice 1 to 3 code except the added call in `run`, the docstring bullet, and the new helpers and method. No invariant was written or edited. No invariant test changed.
5. Test quotations: the `decision:` lines of the new tests quote the starts of WAY-03's sentences "The check of the foundation lists an invariant whose method", "A change whose check lists such an invariant" and "The listing stops no change". The gate's `test_the_way_foundation_passes` ran against the real repository and passed, so the quotations are accepted by the script.

## Reaches beyond the dispatch

- Read spec `D2` and `D3` (referenced by the slice's notes, not named by its *Read*). Reason: the normalisation and quotation rules were needed to write the tests.
- Read the module-level helpers `blocks`, `fields`, `binding`, `at_commit`, `read` and the citation regex in `foundation_check.py`, which the slice notes said to use. Read them as they stand.

## Unread material

- Spec lines outside the slice's *Read* ranges, including D1 and D5 to D7: not read.
- `foundations/decisions.md` WAY-12 (referenced in code comments): not read whole.
- `task-cycle/change/fix.md` and `ui_check.md`: not needed for this slice; not read.
- Everything the handoff's *Read* names is read whole, or read by its line ranges as the handoff gives them: the spec and task passages, WAY-03, WAY-65, WAY-61, WAY-321, WAY-344, the glossary entry, the invariant `test-method-citation`, the part-map passages, and both READMEs around the changed lines.

## Searches not found or unclear

- Whether the-way's real repository has a base branch for `foundation_check.py`: unclear, and the answer is no in this worktree (no `main` or `master`, and `origin/HEAD` not set), so the listing is never exercised on the real repository. The tests cover it on temporary repositories instead.
- The `.ai/rules/git.md` rule was read after a hook blocked the first commit attempt. The commit then went through unchanged in message and path form.

## Concerns and questions

- None that block the slice. The base-side citing set is redundant in practice (see the own-work check); if the orchestrator wants it removed, that would simplify the code without changing behaviour. I kept it because the spec says "at the base or now".

## Background processes

- Started: a backgrounded `gate/run_tests.py elements/common` for the baseline (`bnib67xe6`, completed), a monitor on it (`b500vllu1`, ended), a backgrounded chain of the two gate runs (`b4gczfcn7`, completed) and a monitor on it (`bcobnmp1v`, ended).
- At return: no background process or monitor of this session is still running.
