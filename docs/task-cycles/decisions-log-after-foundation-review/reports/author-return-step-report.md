# Report — the return step — decisions-log-after-foundation-review

**Status:** `done` — the comparison found nothing that no longer matches; no new commit (head stays `cecc49e`, working tree clean).

## The comparison, in the fields of the record's *Return step*

- **Foundation compared with code:** none that no longer matched. Compared, `0dae56b..cecc49e`:
  - every entry of the task's *Decisions in play*, *Invariants* and *Fakty o otoczeniu* lists, against the files they bind: WAY-229 and `task-cycle/skill/SKILL.md` (the review of the whole change at the step "Then the review of the whole change" and step 11 read "the strongest class available"; step 11's return step of a planned change, step 9's executor class and the plan/skill measure of `task-cycle/plan/SKILL.md:161` and `task-cycle/skill/SKILL.md:116-122, 405-411` already say "`strongest` available" in the same meaning); WAY-27 and root `AGENTS.md` (`## Backlog` names entries of the locations file, no path); WAY-320 and `task-cycle/gate_times.py` (default registry `~/.the-way/gate_runs`, no entry of the locations file) and WAY-350 ("outside every repository", unchanged); WAY-287 and `task-cycle/skill/request_template.md` (the template lists every kind, items 12 and 13 among them); WAY-241 and `product-guidelines/testing/template.md` (the *Time limit* line reads `none`); WAY-35 and the invariant `elements-pending-marker` with its test; WAY-44 and `foundations/part_map.md` (root files are named one by one: `/AGENTS.md`, `/CLAUDE.md`, `/.gitignore`, `/.python-version`); WAY-255 and the three new facts; the facts `openai-model-states`, `anthropic-model-states`, `claude-code-imports`, `claude-code-project-skills` and their dependants WAY-85, 127, 129, 132, 141 and `installation-claude-guidance`; `instruction-files/tool_loading.md`; `cut_tasks.md` against WAY-372; `starting_rules.md` against WAY-173; `guideline_findings.md` against `audit_end.md` and both `hand_back.md`.
  - searches of the whole foundation for the changed meanings, by `git grep` and `grep`: `elements-no-pending-marker` → no hit; `and nowhere else` → four hits, none about WAY-27 (WAY-100 ×2, a task-cycle sentence and an invariant-sentence example); `gate_runs` → the decision, the script and its test, all agreeing; `at launch` → the fact `claude-code-imports` (meant) and `tool_loading.md:21` (rules without `paths`, another fact); `orchestrator's class` → only WAY-229 and the measurement in WAY-164's *Rejected* ("a reviewer of the orchestrator's class without the report…", which reports what was measured and points to WAY-229); `no class cheaper` → only `task-cycle/skill/SKILL.md:497`, the return step of a planned change, which WAY-229 still binds so; `Rejected: unknown` → no entry left; the places that state the class of a review (`task-cycle/review/`, `request_template.md`, `agent-instructions/README.md`, `task-cycle/agent-types/`, the entry points) → none states a class.
  - the part map of the touched parts (`decisions`, `invariants`, `environment-facts`, `task-cycle`, `agent-instructions`, `instruction-files`, `product-guidelines`, `project-level`, `elements-common`, and `installation`, which `generated-overview` now names): the sentences and *Files* match; "External context" names the script that runs the gate for the task cycle, and `task-cycle/gate_times.py` stands in the part `task-cycle`.
  - the glossary: no term of it is used against its entry; no word of the change takes a new entry.
- **Decisions written or changed:** WAY-229, WAY-10, WAY-27, WAY-320, WAY-287, WAY-35, WAY-241, WAY-44, WAY-330, WAY-313, WAY-162, WAY-255, WAY-360, WAY-363, and reworded or reflowed WAY-90, 121, 124, 126, 140, 147, 161, 206, 216, 237, 243, 328, 339, 365, 372.
- **Invariants written or changed:** `elements-pending-marker` (renamed from `elements-no-pending-marker`; the rule is set by WAY-35, row 7); `generated-overview` (*Part* names `installation`; set by WAY-52, row 8); `repository-file-location` (points to the part map; set by WAY-09, *To do* 8).
- **Environment facts:** new `claude-code-prompt-cache-expiry`, `claude-code-prompt-cache-ttls`, `claude-code-subagent-cache-default` (the sources of WAY-255, *To do* 15); changed `openai-model-states`, `anthropic-model-states`, `claude-code-imports`, `claude-code-project-skills`. No further source outside the product that the change rests on and the foundation lacks.
- **Glossary terms:** none.
- **Part-map changes:** "External context" (the sentence on the script that runs the gate; *To do* 19.20). No part added, split or removed.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written** (each whole, in the place the column *Goes to* names):
  - row 1 → WAY-229 (sentence), with `task-cycle/skill/SKILL.md` following it;
  - row 2 → WAY-10 (sentence of the *Rationale*, the price);
  - row 3 → WAY-27 (sentence);
  - row 4 → WAY-320 (sentence, its own paragraph);
  - row 5 → WAY-287 (sentence, its own paragraph);
  - row 6 → WAY-35 (sentence);
  - row 7 → invariant `elements-pending-marker`;
  - row 8 → invariant `generated-overview`;
  - row 9 → WAY-44 (clause);
  - row 10 → WAY-330 (the price; its *Rejected* carries the way the source keeps);
  - row 11 → WAY-241 (sentence), with the line of `product-guidelines/testing/template.md`.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` → exit 0, `0 errors` (on `cecc49e`).
- No file changed in this step, so no focused test run; the tests of `elements/common` and `task-cycle` passed on the same tree in the fix (`reports/fix-report.md`).

## Findings that stay as they are

- The review's Minor N-1 (`task-cycle/skill/SKILL.md:457`, a word alone on a line): not touched, goes to the request's list.
- Seen in the comparison, left as it stands because `fix.md` and the handoff bound this step to the findings file and the task: the *Rationale* of WAY-363 still says "the same chance in the grade that a remark on the form of an entry shows (WAY-364)" (named already in the report of the first change, "Searches"); and WAY-10's *Rejected* says "the strongest model" for the author's model, in a way taken from the row's source — it is no second meaning of "strongest class available", which only WAY-229 defines.

## Unread material

- Read whole this step: `task-cycle/skill/return_step.md`; the handoff; `task-cycle/record_template.md` (*Return step*).
- Read in part: the entries and files of the comparison, by the searches above and the places they returned (the whole entries were read in the change itself: see `reports/author-report.md`, **Unread material**); the part map entries of the touched parts, by the lines the greps returned and the first 60 lines; the glossary by its headings.
- Not read: `reports/review-whole-report.md` and the fix review's report.

## Searches not found or unclear

none.

## Reaches beyond this handoff

- `task-cycle/plan/SKILL.md:159-166` and `task-cycle/skill/SKILL.md:116-122, 405-411` (the measure of the class of a slice and of the one author), to check that "strongest available" there matches WAY-229; `foundations/glossary.md` headings.

## Working copies

None made: no `.runs/author/` directory stands (the one of the first change was removed at its return).
