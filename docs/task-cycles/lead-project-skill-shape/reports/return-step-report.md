# Return step report — task cycle `lead-project-skill-shape`

**Status:** `done`. **Commits:** none (the step found nothing to correct). Head stays `08e70be`.

Method read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`. No entry was written, so no element skill was needed.

## Answers to the questions of the record's *Return step* section

- **Foundation compared with code:** yes. Compared with the files of the repository: WAY-256 (as edited), WAY-125 and WAY-127 (rationales as edited), `instruction-files/kind_skill.md` (as edited); the decisions the task names (WAY-257, WAY-265, WAY-311, WAY-30, WAY-05, WAY-152, WAY-154, WAY-156, WAY-269, WAY-127, WAY-259); the entries the search of the foundation found (WAY-128, WAY-258); the part map entries of `decisions`, `project-level`, `instruction-files`. Nothing no longer matches. Details below.
- **Decisions written or changed in this step:** none. (Changed earlier in the change, by the foundation step: WAY-256 in place by row 1; the rationales of WAY-125 and WAY-127.)
- **Invariants written:** none. No decision or human sets a rule of the kind that an invariant would check; no invariant derives from WAY-256, and `skill-entry-points` is unaffected (its test passes).
- **Environment facts written:** none. The change rests on no source outside the product: the "five to fifteen percent" estimate is an estimate of the task's own, made from the word counts of a skill's files, and WAY-256 keeps its existing *Based on* facts (`single-rule-compliance`, `instruction-density-accuracy`).
- **Glossary terms written:** none. The words the change uses (use of a skill, step, variant, record of sessions, pointer) have no meaning for which WAY-95 gives an entry, and none of them is used against an entry of the glossary (the glossary holds no entry for them).
- **Part-map changes:** none. `project-level/**` covers the four new files; `instruction-files/**` and `foundations/decisions.md` (part `decisions`) are unchanged in responsibility, files and dependencies; the part map says nothing of where a fragment of a skill stands.
- **Projected entries:** none (the task carries none).
- **Rows of *Settlements to record* written:** row 1, by the foundation step (WAY-256 edited in place); its meaning sentences are in `author-report.md` section 1 marked `row 1`. No other row exists, and the step missed none.

## What was compared, and the result

| Entry or file | Compared with | Result |
|---|---|---|
| WAY-256 binding sentences (three, WAY-05) | `instruction-files/kind_skill.md` | The same rule in both: a step stays while records show every use comes to it, also with no record; a variant or a step some uses pass by goes beside; the third sentence is unchanged and its bullet in `kind_skill.md` is unchanged. Match |
| WAY-256 *Rationale* and *Rejected* (WAY-05: no file, script or count of the foundation) | the entry's own earlier text | The entry already named `SKILL.md` as the main file of a skill in *Rejected* before this change (`could land in its SKILL.md`), as WAY-265's rationale does; the added mentions are of the same kind; the figure is a count of words of a skill's files with its conditions, not a count of files, tests or entries of a foundation. `foundation_check.py` passes. No correction |
| WAY-125, WAY-127 rationales | WAY-256 | Both name the step every use comes to as staying in the main file; the verification examples of both still hold (the executor reads the file of its variant's step when that step comes; an entry point reads a named file when its step comes). Match |
| WAY-257, WAY-311 (rows of a judgement) | the table of `author-report.md` | Every row has the two answers beside the verdict; a fragment that goes to several places has a row for each part; each proposal has its own row. The table lives in the request, as the decisions put it. Match |
| WAY-265 | `project-level/lead/skill/SKILL.md` | The four files are named in `SKILL.md` at the step that leads to each, with the condition of reading; `route_changes.md` names `definition_change.md`, and `SKILL.md` names it too. Match |
| WAY-259, WAY-127 | entry points (`.claude/skills/the-way-lead-project/SKILL.md`, `.agents/...`) | They read `SKILL.md` whole and a named file when its step comes; no change needed; `installation` and `agent-instructions` tests pass |
| WAY-269 | `task_return.md`, `SKILL.md` step 1 | The worktree, local branch, host branch and remote-tracking ref are removed by name in that order, only on the human's word; `git fetch --prune` stays forbidden in `SKILL.md`. Match |
| WAY-152, WAY-154, WAY-156 | `SKILL.md` steps 0–4, `route_changes.md`, `definition_change.md` | The leading, the file exchange, the delegation of plan changes and of the definition gate stand as before, word for word apart from the connectors listed in `author-report.md`. Match |
| WAY-30 | WAY-256 | The exception is written into the binding sentences, not into the task document alone. Match |
| WAY-128, WAY-258 | `kind_skill.md`, `instruction-files/SKILL.md` | WAY-128 says the lines of process skills answer to WAY-256; WAY-258 asks that no file of a kind point to another file: `kind_skill.md` points to none. `instruction-files/SKILL.md:143–151` (`what a step does not need leaves the text read at that step`) states the principle and does not contradict the placement rule. Match |
| Part map entries (`decisions`, `project-level`, `instruction-files`) | files of the repository | Match, nothing to change |
| Other skills rebuilt earlier with a file for a step every use reaches (and `product-guidelines/{coding,styleguide,testing}/SKILL.md`, `project-level/technology/SKILL.md`) | WAY-256 | Not bound: fragments standing unchanged are not bound by it; the follow-up task named in the task document reviews them. No correction |

Choices that bind after the merge (WAY-36): none found. The layout choices of the rebuild (the boundary of the definition file, the `fetch --prune` rule staying in `SKILL.md`, the closure bullet staying) are visible in the files and recorded in the table and choices of `author-report.md`; the task excludes no entry for them but no rule outside WAY-256 binds beyond the code. They stay in the request's list of choices, not as entries.

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `git status --short` | 0 | clean (no file changed by this step) |
| `git log --oneline 57795e4..HEAD` | 0 | `e98f46b`, `b9e19f7`, `038a330`, `08e70be` |
| grep of `SKILL.md` and `task_return.md` for the WAY-269 rules (`fetch --prune`, `git branch -dr`, the four removals) | 0 | all present |

The tests (`instruction-files`, `agent-instructions`, `elements/common`, `project-level`, `installation`) passed on `08e70be` in the fix; this step changed no file, so I did not run them again. Not run: the whole gate.

## Own-work check

- **Requirement most likely missed:** that a statement of the old rule remains somewhere in the foundation, which the one search of the foundation (done when the entry was written) and this comparison should have caught. Check: a fresh search of the repository (excluding `.runs/` and `docs/`) for the old rule's wording — `one step or variant`, `only one step`, `every use of the skill comes`, `also where every use` — and for every `WAY-256` citation. Result: the only remaining hits are the new wording of WAY-256 itself, the unchanged one-instruction exception in `kind_skill.md` and in WAY-256 (both unchanged by design), the description of layout in the earlier-rebuilt skills (not bound), and citations in WAY-125, WAY-127, WAY-258, WAY-259, WAY-265 which I read in the foundation step and re-read here. Nothing states the old rule.
- **Second check:** that the rationale/rejected prose breaches WAY-05's ban on naming a file. Compared with the entry's own pre-change text and WAY-265's rationale; both name `SKILL.md` as a skill's main file. Left as is; the reviewer passed it.

## Searches not found or unclear

none
