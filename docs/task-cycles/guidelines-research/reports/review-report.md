PASS a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5

# Whole-change review

Reviewed range: `2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5`.

Repository: `C:/Storage/repos/the-way-wt/guidelines-research`.

The reviewer authored none of the change. HEAD matched the dispatched head before and after review. The range contains one commit, `a6453b7 Align guideline research and tool recommendations`, changing only the three guideline skills and the decision log. No spec, plan, slices, invariant changes or invariant-test changes apply.

## Findings

- Critical: 0.
- Important: 0.
- Minor: 0.
- Out of scope: 0.

No defect warrants a review finding. This verdict concerns the instructions and foundation entries on this commit; it is not evidence that agents have executed the revised skills successfully.

## Declined to judge

None.

## Requirement and scenario review

Method: read the frozen task whole, independently compute both file groups of the complete range, read all three final skills whole, and trace each route from recognition through research, audit or trial run, human settlement, task Context and handback. Compare each changed foundation entry whole, including rationale and rejected options, with the task and implementation. The author report was treated as claims to check.

| Requirement or scenario | Result and evidence |
|---|---|
| To do 1; settlement 1: first guidelines without preferences, every extension, no refresh research | Met in `product-guidelines/coding/SKILL.md:147`, `product-guidelines/styleguide/SKILL.md:128` and `product-guidelines/testing/SKILL.md:138`. Each names the first-guidelines condition separately from every extension and expressly excludes refresh research. WAY-186, WAY-211 and WAY-249 carry the same rule. |
| To do 2; settlement 2: shared refresh/extension distinction | Met by WAY-251 at `foundations/decisions.md:6995`, applied at `product-guidelines/coding/SKILL.md:134`, `product-guidelines/styleguide/SKILL.md:116` and `product-guidelines/testing/SKILL.md:125`. Updating an existing tool version within covered scope remains a refresh; new scope is an extension even where an existing tool might serve it. The extension research asks whether to reuse existing tools or use something else. |
| To do 3; settlement 3: tool consequences, recommendation, weak point and tie rule | Met at `product-guidelines/coding/SKILL.md:215`, `product-guidelines/styleguide/SKILL.md:178` and `product-guidelines/testing/SKILL.md:193`. Each includes cost, where the tool runs, upkeep and later switching cost, a recommendation and its weak point. The simplest/cheapest recommendation applies where no consequential difference remains and no human preference takes precedence. WAY-185, WAY-210 and WAY-248 carry these meanings. Coding no longer defaults to the most-used tool. |
| Settlement 4: preferred tool survives extension research | Met: each starting-set section gives researchers the preferences and the added scope, while expressly retaining the preferred tool as the proposal. Each new-tools paragraph repeats that preference at the point of recommendation. Research still runs at every extension. |
| First styleguide where screens already exist | Met at `product-guidelines/styleguide/SKILL.md:110`: starting rules and audit both run. Step 2 explicitly covers first styleguides with or without screens. The task's To do 1 applies to all three disciplines; the corresponding removal of the old WAY-186 exception therefore implements that task, rather than relying on the orchestrator's clarification as new approval. WAY-187's audit obligations remain. |
| Refresh with no preference and no research reports | All three routes can reach settlement and handback. Research-source Context is conditional at coding line 82, styleguide line 70 and testing line 73. Report critique is conditional on research having run; handback accepts any research reports at coding line 271, styleguide line 231 and testing line 248. The remaining collective critique and coding trial-run judgment are separate existing obligations, not research. |
| First guidelines with a preferred tool | No research is required by the first-guidelines condition. For coding with no code, line 162 explicitly reads the preferred tool's documented recommended rules, preserving WAY-204 rather than inventing a set in the absence of research. |
| Coding refresh or proposed version change | The trial run at `product-guidelines/coding/SKILL.md:170` uses the existing set with proposed additions or corrections, or the proposed set. Its version can be read from product files or tool documentation without a research report. Scratch execution, fresh judgment, split approval and adoption obligations remain intact. |
| Tool choice stays in the task | All three new-tools paragraphs leave the choice to the human in the task. They do not move it to the project's technology step or adopt a tool automatically. This follows the task's WAY-121 constraint. |
| All accepted settlements reach the foundation | Settlement 1 reaches WAY-186/211/249; settlement 2 reaches WAY-251; settlement 3 reaches WAY-185/210/248; settlement 4 reaches WAY-186/211/249 with preference precedence repeated beside recommendations in WAY-185/210/248. No accepted row is omitted. |

The changed entries keep current-state wording, retain their identifiers, and add WAY-251 for the separate shared boundary question. Their examples, rationale and rejected alternatives match their binding parts. No new external fact is asserted that requires an environment-fact entry. The part map still assigns every changed file and permits the dependencies used. No change reaches a trust boundary, an irreversible operation, executable product code or a product user interface.

The author's own-work check targets the weakest routes of this change: refreshes depending on research artifacts and extension research displacing a preference. Its manual walkthrough is appropriate to these prose changes and would reveal those omissions. This review repeated the routes independently; neither walkthrough is described as a fresh-agent behavioral trial.

## Executed checks

Commands ran from the repository root above. Source reads are accounted for by the manual methods rather than treated as tests.

| Command | Exit code | Result |
|---|---:|---|
| `git -C .agents/skills/the-way-review-change rev-parse --show-superproject-working-tree` | 0 | Empty: this is not a product submodule. |
| `git ls-files --stage -- :/.the-way` | 0 | Empty: no product pin in this repository. |
| `git rev-parse HEAD` | 0 | Dispatched head, before and after review. |
| `git status --short` | 0 | Clean reviewed working tree, before and after review. |
| `git log --oneline 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5` | 0 | One commit. |
| `git diff --stat 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5` | 0 | Four expected prose files. |
| `git diff 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5 -- product-guidelines` | 0 | Read every hunk of all three skills. |
| `git diff 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5 -- foundations/decisions.md` | 0 | Read every hunk of all seven entries. These two diff commands partition the complete changed-file set. |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors`. |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current`. No description, name or path changed. |
| `git diff --check 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5` | 0 | No whitespace errors. |

The following searches also exited 0. The first checked references and possible stale research/recommendation instructions; the second located report anchors after whole-file reading. They were discovery checks, not substitutes for that reading.

```powershell
rg -n 'WAY-(185|186|210|211|248|249|251)|research.*refresh|refresh.*research|most.used.*recommend' --glob '*.md' --glob '!.runs/**' product-guidelines foundations project-level task-cycle
rg -n '^### WAY-(185|186|210|211|248|249|251)|^## [1-5]\.|research.s sources|any$|any research|New tools|A refresh|documentation' foundations/decisions.md product-guidelines/coding/SKILL.md product-guidelines/styleguide/SKILL.md product-guidelines/testing/SKILL.md
```

Guideline discovery used `product-guidelines/reading.md`: `Test-Path guidelines` returned `False` (PowerShell exit 0). No product UI, code or test is being written by this change, so no missing-discipline prerequisite arises from that absence.

Not run:

- `python -B gate/run_tests.py`: the cycle owns the complete-suite run; the review method expressly says not to repeat it.
- Fresh-agent executions of the revised skills: the review method forbids reviewer delegation. The scenario evidence above is a manual instruction walkthrough.
- Runtime/UI checks and screenshot inspection: no executable product or UI changed.
- First-failing invariant tests: no invariant or invariant test changed.

## Reaches beyond the handoff

The mandatory independent foundation and guideline selection followed `elements/common/way_of_working.md` and `product-guidelines/reading.md`. Each selected decision was read whole, including its rationale and rejected alternatives; relevant invariant entries and glossary terms were also read. The selection itself is not recorded here, as that procedure directs.

Additional sources read whole for the review:

- `product-guidelines/template.md` and the coding, styleguide and testing `template.md` files: check that changed handbacks and sourcing still supply the downstream guideline writers and preserve existing adoption obligations.
- `elements/decisions/template.md` and `elements/common/rules.md`: assess the form and meaning of the six revised decisions and new WAY-251, not merely the structural validator's result.

The reference search also covered `project-level` and `task-cycle` to find downstream consumers of the changed rules; it found no additional stale instruction requiring a finding. No external web source was needed: this review checks the supplied task and repository rules, not current properties of any tool. The cycle record was not read. No reviewed file, index, branch or commit was changed; only ignored review scratch artifacts were written.
