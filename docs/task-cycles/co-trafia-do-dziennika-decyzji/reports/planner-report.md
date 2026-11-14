# Planner report — co trafia do dziennika decyzji

Status: done with concerns

Plan: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`
Final size report: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan-size.md` (every slice fits; the largest reads about 75 000 estimated tokens and changes at most 4 files).

## Result

Nine slices after the foundation step. Slices 1 to 4 change `elements/common/foundation_check.py` and its tests one after another: the line `decision:` (D3), the base and the `listed:` lines (D1), decisions nothing holds (D2), the invariant whose sentence changed (D4, with the README lines). Slice 5 is the decisions template. Slice 6 holds the skill, `decide_entry.md` and the return step. Slice 7 holds the column *Goes to* (four files). Slice 8 is the guidelines template. Slice 9 is the request template. The *Foundation entries* table lists the thirteen decisions and the two attached paragraphs (WAY-12 for D2, WAY-03 for D4). The coverage table maps every point of *To do*, all 12 rows, the three questions carried to the cycle and D1–D9. No open design choice and no reserved choice was found.

## Concerns

1. **The spec's note on order against the cycle's method.** The spec says the decisions' texts "must be written last, after the files they describe". The handoff and the plan method write the foundation entries before slice 1. I followed the method and put it in *Choices*; the return step compares the entries with the code and trims the pairs. The tests of Slices 3 and 4 quote the new attached paragraphs of WAY-12 and WAY-03, so those entries have to exist first anyway.
2. **Line ranges of edited entries are stale after the foundation step.** The foundation step edits 13 entries in place and the log grows, so ranges such as `foundations/decisions.md:383-411` WAY-12 are the entries' size at the base. The identifier is the address. The orchestrator should refresh the ranges for WAY-12, WAY-03 and the other edited entries when it writes each handoff (the plan's Slices 3, 4, 5, 6, 7, 8, 9 read them).
3. **Where the check meets the-way's own gate.** `origin/HEAD` of this repository names `foundations`, so in the-way's own gate the base is known and each of the 13 edited decisions must be held (invariant, `decision:` line or pair). Slices 3 and 4 run `python -B elements/common/foundation_check.py` on the repository; a failure there means the foundation step left an edited decision with no pair, which is the foundation step's to correct, not a slice's (no slice changes the log). The report of that run will also print one `listed:` line for every old unheld decision (spec: about 300 entries of the-way's log have only a pair; the count of lines that print is not known to me).
4. **Further places that may say the old rule, not named by the spec.** `task-cycle/record_template.md:184` ("Rows of *Settlements to record* written: <row number and identifier for each row, or none>") has no place for a row that goes to a skill, guidelines or code. It is not in any slice's *Change*, because `process-audit/audit_count.py` and `task-cycle/test_remarks_check.py` read that file and I did not read how. The orchestrator can add it to Slice 6 or leave it to the return step. `elements/common/skill/read.md:9` names "the plan test" only and needs no change; `elements/decisions/skill/projected.md` is excluded by the spec.
5. **Spec's open item the human did not see (kind 5, D2).** The pair-then-trim rule costs a pair written and trimmed in every cycle that has a decision pinned only by a later slice's test; the alternative is a switch that also skips this error, which changes WAY-321. This is the orchestrator's ruling, as the handoff says; the plan follows the spec.
6. **`foundation-check-command` is a surface, not a trust boundary.** Slices 1–4 still change a script every product runs as its gate. I marked their *Risk* `none` as the handoff directs; Slices 2 and 3 are on the `same` model class for that reason. The review of the whole change reads the surface promise (path, one argument, exit codes 0, 1, 2).
7. **File of tests grows.** `elements/common/test_foundation_check.py` is 1052 lines and gains about forty tests (D9). The-way has no `guidelines/` directory, so no rule of size applies and no move-out slice was written (method: the bullet asks nothing).

## Guidelines found missing or uncertain

The-way has no `guidelines/` directory; none was read. Nothing else is missing.

## Relation of the order to the styleguide example

No styleguide exists for the-way; no example to follow or depart from.

## Reaches beyond the dispatch

- `foundations/part_map.md` whole, to check the trust boundaries (none among the changed files) and to name part entries.
- `foundations/invariants.md:96-165` and `326-337` (skill-rule-source, script-language, script-imports, script-subprocesses, fingerprint-definition, map-reference-target, test-method-citation, cross-part-imports): the script is `every`-part code, so these bear on slices 1–4.
- `foundations/glossary.md` and `foundations/environment_facts.md`: heads and the entries named in the plan (binding part, binding sentence, invariant test, guidelines, foundation step, return step; git-path-patterns, python-stdlib-modules), to set ranges.
- `elements/common/way_of_working.md:50-119` and `140-150` ("Reading the foundation" and the steps of writing an entry), for the selection of reads and for the run right after an entry is written.
- `task-cycle/slice_size.py` (docstring and constants), `gate/run_tests.py` (docstring: it takes a directory only, so the checks name directories), `agent-instructions/skill_entry_points.py` (docstring and generated entry points: they hold the skill's `name` and `description`, so a body-only change needs no `--write`).
- `README.md:78-90`, `installation/README.md:58-120` (it does not need a change), `agent-instructions/README.md:10-20`, `task-cycle/skill/request_template.md:270-309` and `436-453`, `project-level/task/template.md:78-107` and `190-236`, `task-cycle/skill/foundation_step.md`, `elements/common/skill/task_variant.md`, `build_table.md`, `product-guidelines/template.md`, `elements/decisions/template.md`, `skill/SKILL.md`, `decide_entry.md`, `task-cycle/skill/return_step.md`: read whole or in the part shown, to cut slices and name what each reads.
- `elements/common/foundation_check.py` whole; `elements/common/test_foundation_check.py:1-245` and `990-1052`; `installation/test_install.py` (heading of the empty-foundation test only; the plan names `665-700`, which exists).
- Searches of all Markdown and Python files for "Kind"/"its kind", "plan test", "Settlements to record", "tests live only", "names no decision is an example" and `record_template`, to find the files that carry the old rule (result in concern 4 and in the slices' *Change*).

## Unread material

- The decision entries themselves (WAY-36, 293, 11, 134, 19, 05, 12, 22, 03, 02, 65, 168, 167, 171, 172, 173, 26 and the others the slices' *Read* names): I read the task's quotations and the spec's account of them, and located each by heading and range with a script; I did not read the entries whole. The plan names them by identifier and range for the slices' agents to read.
- `elements/common/rules.md`: read the `{fork-point}` passage only (lines 76-89).
- `project-level/task/template.md`: lines 78-107 and 190-236 only. `task-cycle/skill/request_template.md`: the parts named above. `README.md` and `agent-instructions/README.md`: the lines named above. `elements/common/test_foundation_check.py`: lines named above.
- `elements/common/way_of_working.md`: lines 50-119 and 140-150.
- `task-cycle/too_large.md`, `project-level/technology/reserved_choices.md` and `agent-instructions/README.md` as a whole: not read, because their steps did not come (no oversized attempt, no choice of technology, handoff did not name it).
- The invariants not listed in this report, `foundations/environment_facts.md` and the glossary beyond the entries named: not read.

## Searches not found or unclear

- None of the items named in the handoff was missing.
- Unclear: whether `task-cycle/record_template.md:184` is to change (concern 4).
- Unclear: whether `python -B agent-instructions/skill_entry_points.py` with no `--write` exits non-zero when an entry point is out of date; its docstring says it reports and `--write` writes. Slice 6 uses it as "nothing to write"; the maker will see.

## Questions

None that block the plan. For the orchestrator to settle: concern 4 (add `task-cycle/record_template.md` to Slice 6 or not).
