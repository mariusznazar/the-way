# Report: author, the fix of the review of the merge (correction 1)

**Status:** done (both findings fixed; one point for the human, below)

## Commit

- `dcb1a19` Defer the CI rule to WAY-261 and record that installation reaches instruction-files (on `7d00a48`). Files by explicit path: `foundations/decisions.md` (+7/-4), `foundations/invariants.md` (+10), `task-cycle/skill/SKILL.md` (+6/-4), `task-cycle/skill/correction.md` (+3/-2), `agent-instructions/README.md` (+2/-1).

## Finding 1 (CI red on a flaky test outside the task's scope), fixed place by place

I read WAY-160, WAY-261, WAY-243 and WAY-161 whole first. WAY-261's second paragraph governs a red first run of the gate where the failed check is outside the task's scope and passes when run again: the cycle goes on, the request names the check and the task that fixes it. WAY-243 forbids rerunning to make a run pass, WAY-161 keeps out-of-scope findings unfixed; so the four places now say "save that case, which WAY-261 governs", each in its own sentence's style and with no new rule:

- `foundations/decisions.md` WAY-160, binding sentence: "treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review, save a check outside the task's scope that passes when run again, which WAY-261 governs —". Its *Verification*, the *complies* clause that repeated "has the failure fixed and the fix reviewed", gained "(a check outside the task's scope that passes when run again goes as WAY-261 gives)". *Rationale* and *Rejected* do not say a red result is always fixed (read whole); unchanged. The *violates* item "a red CI result is left for the human to find" stays true (WAY-261 has the request name the check, so the human is told).
- `task-cycle/skill/SKILL.md` step 12: "A red result is a failed gate, handled as step 10 gives: its failures are fixed … and the wait repeated on the new head, save a check outside the task's scope that passes when run again, which step 10 leaves to WAY-261: the cycle goes on, and the description names that check and the task that fixes it, or proposes that task."
- `task-cycle/skill/correction.md`: the same exception, in the sentence about the wait after a correction.
- `agent-instructions/README.md`: "…which the change fixes before the request goes to Mariusz, save a check outside the task's scope that passes when run again, which the description names with the task that fixes it (WAY-261)."

Search that nothing else of the task's text says a red CI result is always fixed: `git grep -i -E "red (CI )?result|red run|CI result|result of the (CI )?run|failed gate"` over `task-cycle`, `agent-instructions`, `installation`, `foundations/decisions.md`, then a read of `request_template.md` (the *Checks* item, lines about CI), `record_template.md` (the CI row), `blocked_finding.md`, `reserved_return.md`, `installation/README.md:142` ("a red result shows before the merge"). None says that a red result is always fixed; they speak of the wait and of where the result is written. Unchanged.

## Finding 2 (installation reaches `instruction-files`), fixed by the route the orchestrator bound

I did not add `instruction-files` to `installation`'s *Depends on* and did not touch `foundations/part_map.md`, the installer, its README or its test. I wrote in `foundations/invariants.md`, as its last entry:

```
## installation-instruction-files-dependency

The part `installation` does not depend on `instruction-files`.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-225 · WAY-51
- **Part:** installation
- **Violated:** yes
```

- Entry kind and mark: `the cycle's` (no row of *Settlements to record* carries it, as `foundation_step.md` marks an entry for the human to see). The sentence has the exact form "The part `X` does not depend on `Y`." that the check of allowed imports (`cross-part-imports`, and its test `elements/part-map/test_cross_part_imports.py`, `MARKED`) reads; the entry is a whole entry that a human accepts at the request, as the template's "Allowed dependencies" says, so the request must name that it sets `Violated: yes` (WAY-51; item 7 of the request template).
- English: the part that installs the-way into a product must not depend on the part that checks instruction files, and today it does, so the entry stands as an unmet invariant.
- The reach it records, as the review gave it (the template gives an entry no field for it, so it stands here and must stand in the request's item on the Violated mark):
  - the guidance the installer writes into every product names `python -B .the-way/instruction-files/check_instructions.py` and states the script's exit-code contract: `installation/install.py:200-202`;
  - `installation/README.md:61` and `:82-84` say the same;
  - `installation/test_install.py:145-146` and `:161-168` check that the path exists at the pinned commit.
- *Method* is `review`, not `test`: the sentence is about any reach (the glossary: a skill that calls a file, a script that reads a file, a path or a git tag, an import), which no cheap test can check; a test that searched the files of `installation/` for the text `instruction-files` would see one kind of reach only, and the test file would have to stand in or beside the part it checks. Rejected: such a test marked `expectedFailure` — it would hold one reach and say it holds the sentence (`elements/invariants/template.md`, "A test checks what its sentence is about"). Cost if the human prefers a test: one more test file with the expected-failure mark, and `Method` turns to `test`.
- *Derives from* WAY-225 (the route) and WAY-51 (the mark). *Rests on* none: no outside fact. *Part*: `installation`, the part whose change can make the sentence false.
- The same entry and the part map: the import check lets only an import of `installation` to `instruction-files` pass with this entry; the reach here is a path in text, not an import, so the check is neither relaxed nor changed (`elements/part-map` tests passed).
- **For the human (the Violated mark):** the human sees the mark at the request and may instead allow the dependency. In that case this entry is removed, and these files change: `foundations/part_map.md` (add `instruction-files` to the *Depends on* of the part `installation`, lines 192-193) and `foundations/invariants.md` (the entry's removal, with its identifier moving to the list of withdrawn identifiers only if the file keeps such a list; it holds none today). The installer, its README and its test stay as they are.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0.
- `python -B gate/run_tests.py elements/part-map`: 39 tests OK, exit 0.
- `python -B gate/run_tests.py agent-instructions`: 25 tests OK, exit 0.
- `python -B gate/run_tests.py task-cycle`: 483 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common`: 235 tests OK, exit 0.
- Not run: the full gate (the orchestrator's); `foundations` holds no tests; `installation` unchanged, so not run.
- Own-work check: the requirement most likely unmet is "no step now contradicts another". Check: the five places read side by side after the change, each saying the red-CI-on-an-outside-flaky-check case goes by WAY-261 (decisions:2682-2686 and 2696-2698, SKILL.md step 12, correction.md, README), and a search for any text saying "a fix" for a red result without the exception (above) found none. The second requirement, "the merged map does not contradict the merged code unrecorded": the entry records the reach and the checker accepts it (exit 0).

## Reach beyond the handoff

- `elements/part-map/test_cross_part_imports.py` lines 36-75 and 138-160 (the form of the marked sentence the check reads), and `elements/part-map/template.md` "Allowed dependencies" and `elements/part-map/skill/SKILL.md` line 41: to match the exact form of the sentence. `elements/invariants/skill/{decide_entry,draft,write}.md` and `template.md` were read for the entry.
- `elements/invariants/examples.md` (opened, first lines) for examples of form.
- The text of `installation/install.py:198-204`, `README.md:80-85`, `test_install.py:158-170` to confirm the reach's line numbers (the review gave 200-202; the line with the path is 201).

## Unread material

- `elements/common/way_of_working.md` "Reading the foundation" and the decision index script were not used for selection; I read the decisions and files the handoff named instead. WAY-11 (named in the handoff) was not read whole this run (I took its content as the review quotes it through the template); the glossary entry "dependency of a part" and WAY-225, WAY-51, WAY-263 were read whole. `reports/review-merge-report.md` was not read (the findings file was enough for what the findings cite).

## Searches not found or unclear

- A field of the invariant entry for the reach it records: the template has none and says an entry holds nothing about why; the reach stands in this report and must go to the request's item on the Violated mark. Unclear whether the orchestrator wants it also in a test (see *Method* above).
- Another flagged mismatch I did not fix because it is not named in the findings: none seen.

## Working copies

`.runs/author-fix-merge/` held only the logs of the four test runs; removed before return, no remainder.
