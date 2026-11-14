# Executor report — slice 3 (Elements: the shared rules and the way of working)

**Status:** done with concerns

Concerns: (1) the plan's text for `build_table.md` is cut off ("The rest of the… (add that first)"), so the missing sentence was chosen by me (see Choices); (2) the `elements/common` gate test `test_the_way_foundation_passes` still fails, as the plan expects, because it lists lines of files of slices not yet made; (3) two choices below change wording beyond a literal copy of the plan.

## Commits

- `21a3e94` — "Remove the withdrawn decision numbers from the shared element files and give each rule its reason" (branch `task/decision-log-second-round`, author `mariusznn@gmail.com`). Files: `elements/common/rules.md` (+18/−11), `elements/common/way_of_working.md` (+8/−4), `elements/common/projected_mode.md` (+2/−2), `elements/common/skill/SKILL.md` (+1/−1), `elements/common/skill/build_table.md` (+6/−2). Total 33 insertions, 22 deletions. Staged by path; never pushed; the product's gate was not run without a directory.

## Checks

Working tree was clean before the slice; foundation check run before the edits to get a baseline.

| # | Command | Exit | Result |
|---|---|---|---|
| 0 (baseline, before edits) | `python -B elements/common/foundation_check.py` | 1 | Lines for my five files: 22 (`rules.md` ×15, `way_of_working.md` ×4, `projected_mode.md:7`, `SKILL.md:14`, `build_table.md:20`) |
| 1 | `python -B elements/common/foundation_check.py` | 1 | Lines for my *Change* files: **0**. Exit 1 remains from lines of files of slices 1, 2, 4 and later (e.g. `elements/decisions/skill/SKILL.md:56`, `task-cycle/skill/SKILL.md`, `agent-instructions/README.md`). Expected by the plan. Output: `.runs/executor-3/executor-3-fc.txt` |
| 2 | `python -B gate/run_tests.py elements/common` | 1 | 201 tests, 1 failure: `test_the_way_foundation_passes`, which reports the same foundation lines as check 1. None of them is in my five files. Expected until the last slice. Output: `.runs/executor-3/executor-3-gate-common.txt` |
| 3 | `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests, OK. Output: `.runs/executor-3/executor-3-gate-partmap.txt` |
| 4 | `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" (no frontmatter changed). Output: `.runs/executor-3/executor-3-sep.txt` |

No test was written first: the slice is prose in element files and no test covers its wording, so no invariant test was changed or seen failing. No check reported "no test found".

## Own-work check (make-change section 3)

- **Requirement:** no number of a withdrawn entry (WAY-37, 41, 64, 72, 80, 115, 117, 226) remains in the five files, each named rule keeps one sentence of its reason, and each removed number leaves its sentence intact with its full stop; WAY-134 and WAY-315 (not withdrawn) stay.
- **Check:** `grep -n 'WAY-\(37\|41\|64\|72\|80\|115\|117\|226\)\b'` over the five files: no match (exit 1). `grep` for WAY-134 / WAY-315 in `SKILL.md` and `build_table.md`: still present. Each reason sentence was re-read against its entry's *Rationale* (below).
- **Showed:** requirement met on the grep; the reason sentences are paraphrases of the Rationale, not quotations. No run had to be repeated.

## Reasons added (file, sentence, entry read)

1. `elements/common/rules.md`, bullet under `## Language` (WAY-72 *Rationale*): "Every template's field and every word the rules of form keep out is English, so an entry in another language would pass those rules unchecked, and one language also makes the entries of the-way examples for every product."
2. `elements/common/rules.md`, first bullet of `## Identifiers` (WAY-41 and WAY-64, *Rationale*, words): "A reference rests on the identifier, and words are used because a number says nothing where it is read." One sentence serves both, as the plan allows.
3. `elements/common/rules.md`, third bullet of `## Identifiers` (WAY-64 *Rationale*, "a change of meaning is made in the entry itself (WAY-07), so only a split or merge changes an identifier"): "A change of meaning is made in the entry itself, so only a split or a merge changes an identifier." Missing rule sentence added first (see Choices 1).
4. `elements/common/way_of_working.md`, bullet ending "each such entry is fixed in the same change" in `## 2. Search the foundation` (WAY-37 *Rationale*): the bullet now ends "…each such entry is fixed in the same change, because an entry that says what holds until something exists turns false when it arrives, nothing leads from the arrival to what waits for it, and the authors of the waiting entries may be gone, so a fix left for later goes missing."
5. `elements/common/projected_mode.md`, after the opening sentence (WAY-117 *Rationale*): "Projecting keeps a future rule visible in the definition without claiming that it already holds."
6. `elements/common/skill/build_table.md`, last bullet of the last-column rule (WAY-115 *Rationale*, "the concrete guess filters noise before it becomes a rule"): "The concrete guess filters noise before it becomes a rule." Added after "shown as rejected, with its reason, and is not proposed."

Missing rule sentence added first, per the plan:
- `elements/common/skill/build_table.md`, new last bullet (from WAY-115's binding text and from `definition_variant.md` step 5): "The working table stays until the step ends, each accepted row is recorded in it as it is worked through, and the step then replaces the table with its `Candidates:` line recording how many rows were shown and accepted."

Other removals (no reason sentence asked for by the plan): `rules.md` lines for WAY-41/64 (identifier bullets, withdrawn-identifier list, *Why* and *Successors* bullets), `way_of_working.md` WAY-226 (step 4 glossary bullet) and WAY-117 (`## Projected mode`), `projected_mode.md` WAY-117 (lead-in), `skill/SKILL.md` WAY-115, `build_table.md` WAY-115 (line 20).

## Entries left under the "stay" rule

None. None of the numbers this slice touches is among the ten entries that stay (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364). WAY-293 was read and not changed.

## Choices (with the way rejected and the cost if wrong)

1. **`rules.md`, third bullet of `## Identifiers`.** The plan asks for the WAY-64 binding sentence ("Splitting or merging environment fact entries, or invariant entries held there, gives each entry… a new identifier, and any other change keeps it."). The file's existing clause "Splitting or merging entries gives each entry… a new identifier" is the only statement of WAY-41's part-map split rule. Rejected: replacing it with the WAY-64 sentence alone, which would drop the part-map rule when WAY-41 is withdrawn. Chosen: "Splitting or merging part map entries, or environment fact entries, or invariant entries held there, gives each entry that comes out of it a new identifier, and any other change keeps it." Cost if wrong: the bullet is longer than the plan's literal sentence; a reviewer may ask for the literal form.
2. **`way_of_working.md`, WAY-80 replacement.** The plan says "replace … by the place: environment-facts template, section 'Source' (fact); decisions template (citation)". I wrote "(for the source of a fact, the environment-facts template, section 'Source'; for a citation, the decisions template)". The environment-facts `## Source` section exists (template.md:96). The decisions template has no section headed for citation; its citation rule sits in its *Based on* discussion (template.md ~lines 46–60), so "the decisions template" names a file, not a section. Cost if wrong: the reader must search the decisions template for the citation rule.
3. **`build_table.md`, the missing rule sentence.** The plan's text is cut off ("The rest of the… (add that first)"), so the missing part was inferred: the table's life (kept until the step ends, accepted rows recorded as worked, replaced by the `Candidates:` line). The same content already stands in `definition_variant.md` step 5 and `task_variant.md` step 5. Rejected: adding nothing, which would leave the plan's instruction unmet. Cost: three places hold the `Candidates:` line rule and may drift. The orchestrator should confirm whether this sentence belongs here or in the variants.

## Unread material

- `foundations/decisions.md` WAY-293 (current heading at line 7171): read from the heading to the Rationale's "…a choice with" (about line 7215). The rest of its *Rationale* was not read; the plan's Read range (9771–9810) is the base-line range, which ends mid-entry too.
- WAY-226 (base `ec7929d`, heading line 7002): not in the plan's *Read* list and not read whole; only its withdrawn-table row (current line 9068: "stands in `elements/glossary/template.md`") was read. Its removal from `way_of_working.md` line 95 relies on that row.
- `elements/environment-facts/template.md` `## Source` (line 96) and `elements/decisions/template.md` (citation discussion, ~lines 46–60): searched and read in part, not whole. Not files this slice changes.
- `elements/common/skill/definition_variant.md` (lines 55–70) and `task_variant.md` (lines 48–60): read in part, only for the `Candidates:` lifecycle (Choice 3).
- The other foundation entries that the withdrawn-table rows point to were not read (not in this slice's *Read*).

## Searches not found or unclear

- The plan's *Read* ranges for WAY-37, 41, 64, 72, 80, 115, 117 were read at the base `ec7929d` as instructed; all seven were found there by heading.
- WAY-293's heading is at line 7171 in the current log, not at the base-line range the plan gives.
- The plan's sentence for `build_table.md` is truncated (Choice 3).
- The plan says "replace … by the place", which leaves the replacement words open (Choice 2).

## Working copies

None made by the slice. `.runs/executor-3/` holds four text outputs of the checks listed above (`executor-3-fc.txt`, `executor-3-gate-common.txt`, `executor-3-gate-partmap.txt`, `executor-3-sep.txt`); they are check outputs, not working copies, and no worktree or clone was created, so there was nothing to remove with `git worktree remove`.

## Commands run, for the record

Full paths of the changed files:
- `elements/common/rules.md`
- `elements/common/way_of_working.md`
- `elements/common/projected_mode.md`
- `elements/common/skill/SKILL.md`
- `elements/common/skill/build_table.md`
