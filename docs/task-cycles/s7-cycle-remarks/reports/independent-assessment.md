# Independent assessment

Status: two remarks require settlement. Required full target reads and current-Scope reconciliation are complete. This is an independent critique, not task-coverage approval or permission to merge.

Assessor: fresh delegated agent, 2026-10-21. No author reasoning, task documents, current-cycle records, reports, prompts, specs/plans or commit messages were read. No other agent was spawned. The only file written by this assessment is this report.

## Assessed material

Base: `f0b5eb131de5d681ee3fcdeb264e9f88778af2ec`
Head: `8726cc1c6b6b031ca94c6e867d0df1297c286c01`

The complete diff of exactly these files was read:

- `agent-instructions/README.md`
- `elements/common/critique/SKILL.md`
- `elements/common/way_of_working.md`
- `elements/part-map/skill/SKILL.md`
- `elements/part-map/template.md`
- `foundations/decisions.md`
- `foundations/invariants.md`
- `project-level/task/skill/SKILL.md`
- `project-level/task/template.md`
- `task-cycle/skill/SKILL.md`

All ten target files were read whole at the assessed head. The complete decisions log (lines 1–7701) and invariants file (lines 1–2268) were read, including every field, rationale, Rejected section and closing list. Truncated output passages were reread. This completes the original assessment's source coverage; it is not a second assessment of a changed revision. The full glossary and environment-facts file were also read, as was the complete part map. Current-Scope reconciliation is recorded below.

Additional material: complete part map, common rules, decisions template, task-plan skill; relevant whole decisions including WAY-01–05, WAY-07–14, WAY-16–18, WAY-24–28, WAY-33–37, WAY-113–115, WAY-120, WAY-125, WAY-134–136, WAY-148 and WAY-172; the installed Superpowers 6.4.1 `task-brief` and `sdd-workspace` scripts, and the method's workspace/brief instructions. Templates describing plans are repository rules, not a plan of the assessed task.

Touched parts from the map: agent-instructions, elements-common, part-map, project-level, task-cycle, decisions, invariants, environment-facts and product-guidelines (the last two through changed decision Scope).

## Remark A — candidate questions need recorded precedence over WAY-114

Evidence anchors at assessed head: `foundations/decisions.md:7668` (WAY-224), `foundations/decisions.md:7679` (its relations), `foundations/decisions.md:3245` (WAY-114), `foundations/decisions.md:723` (WAY-25), `elements/common/way_of_working.md:157`, `task-cycle/skill/SKILL.md:568`.

WAY-224 says:

> A candidate failure mode the cycle finds at a part goes to the human as a question in the request's *Questions*, naming the part, what fails, the damage, its severity, how it is detected, the agent's recommendation and the strongest argument against that recommendation. Such a question is not a foundation entry deferred by the return step: the cycle records the failure mode only when the task document commands it or the human supplies it or accepts the agent's proposal in answer to that question (WAY-46), and records the answer as a correction to the open request before it is merged.

WAY-114 says:

> A human accepts the meaning of a foundation entry, shown as one sentence in the human's language with the entry beside it, while its wording is the agent's: an agent writes the entry and the human accepts it at the merge of the change that holds it, or, for a projected entry, at the readiness gate. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.

Concrete overlap: the cycle discovers a new failure mode, recommends recording it, and the mode changes no approved decision. WAY-224 requires a question before writing it, while WAY-114's exhaustive pre-merge question conditions are false. Calling it a candidate rather than an entry explains the return-step exception, but does not explicitly resolve the approval-route collision. The shared step still applies WAY-114 to the part-map skill.

WAY-25 requires a direct `narrows` relation and an explicit area of precedence. WAY-224 currently only derives from WAY-46, WAY-11, WAY-113 and WAY-125. The same change correctly records explicit precedence for WAY-30 over WAY-114, making the missing equivalent here particularly visible.

Requested settlement: explicitly settle the candidate-failure-mode approval route against WAY-114, preferably with a narrow `narrows WAY-114@04b4f599` relation and matching binding wording, then update resulting fingerprints/dependents. This report does not itself approve that meaning.

Cost of leaving it: an agent must either ask a question the general rule excludes or silently choose which decision wins, which WAY-25 forbids. Cost of the narrow clarification: one explicit precedence area and its relation maintenance; no additional stage or human contact is needed. Deleting the question route would be cheaper textually but would remove the proposed benefit of keeping a found candidate available for human judgment.

## Remark B — the temporary plan must not become the borrowed method's workspace identity

Evidence: `task-cycle/skill/SKILL.md:127`; installed Superpowers 6.4.1 `skills/subagent-driven-development/scripts/task-brief:21`–27, `scripts/sdd-workspace:41`–77; the borrowed method's `SKILL.md:136`–149 and `SKILL.md:251`–266.

The new instruction says:

> For a plan written by `plan-task`, run the borrowed method's brief script on a temporary copy of the plan with each `### Slice N` heading written as `### Task N`, and remove the copy after extraction.

The heading adaptation matches the actual extractor: it recognizes Task-number headings outside fenced blocks. However, the borrowed method's documented invocation uses two arguments, `task-brief PLAN_FILE N`. With those arguments the script derives the output workspace from PLAN_FILE through `sdd-workspace`. That helper records the plan's normalized path as its ownership marker and disambiguates a different path even when its basename is the same.

Thus following the new instruction with the documented two-argument invocation makes the temporary copy own a DIFFERENT workspace from the original plan's ledger. The borrowed method names the implementer's report beside its brief, so reports move there as well. This defeats the method's stated single workspace for ledger, briefs, reports and review packages. The temporary path is then removed. This mechanism was established from source, not inferred from an author's account and not demonstrated by executing a new cycle.

Requested settlement: retain the temporary heading conversion but explicitly resolve the workspace using the original plan, and pass `<original-plan-workspace>/task-N-brief.md` as the script's supported third argument. Keep reports/ledger tied to that original identity. There is no need to patch the dependency or create a second persistent plan.

Cost of leaving it: split artifacts, additional workspace directories and a fragile recovery/cleanup path. Cost of clarification: one explicit output argument and a few words of adapter instruction. Removing the adapter entirely would restore the existing extractor failure for Slice headings.

## Critique questions

1. **Who benefits and when?** The approval clarification serves a human who has already accepted a decision revision and the agent recording it. The failure-mode route serves the human judging damage and the cycle preserving a newly found candidate at request review. The brief adapter serves dispatch from a plan using Slice headings. The no-plan wording serves refinement and execution choice. The merge-onto check serves the pre-request author who otherwise does not validate relation fingerprints. Excluding commit messages serves assessor independence. These intended moments follow directly from the text. Whether they match the historical prompting case is unverified because task chronology is excluded.
2. **Frequency?** Unavailable. Session/run records examined: zero; empirical observation period: none; dated agent-behavior cases: none verified. No transcript search was attempted because the explicit filtered-input boundary excludes those records. Repository occurrences are rule mentions, not behavioral cases. No rate, recurrence count or claim of demonstrated agent improvement is made.
3. **Overapplication and displacement?** WAY-30 preserves approval by the decision's approver and retains the stop for a meaning beyond accepted scope; it does not authorize an orchestrator to approve changes. WAY-46 preserves human judgment while allowing agent transcription; no criticality calculation changes. WAY-224 is specifically about candidate failure modes, not every request question. Remarks A and B identify where the new rules can move uncertainty into precedence selection and artifact recovery respectively.
4. **Cheaper route and cuts?** No whole behavioral addition can be cut on the inspected evidence without losing its stated function. Prefer the existing third argument of task-brief over a new script or permanent converted plan. Keep the existing no-plan record rather than introducing another document. The README's reference to the critique report-location rule removes a duplicate policy. The local repeated operational reminders point readers to WAY-224 at distinct entry points; cutting all but the decision would make the skill harder to execute. Empirical proportionality remains unmeasured, so this is a structural cost judgment, not measured savings.

## History checked without commit messages

Hash-only `git log --format=%H -S ...` searches and file snapshots establish that:

- WAY-30's plan approval rule exists at `0fb5b757532b68d15639f250bf51e36fea50ba1b`; its initial binding wording already puts decision-approver acceptance before dependent work.
- WAY-46's human-recorded failure modes exist at `9d3f0ebc054a65811dd300e43dfc9c689036bc1a`.
- Reusing the borrowed method's brief exists at `19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f`.
- The cycle-report location rule exists at `904cc45838af5171a608e31088f0bbca649241a4`; its whole critique skill snapshot was read.

These are source-history observations. They do not establish when an agent began complying or whether a problem recurred afterward. No historical commit message was opened.

## Explicit no-concern checks

- The accepted-meaning clarification is reflected in the shared foundation-writing step and task-cycle foundation step. WAY-30 names the approver; the provisional cycle go-ahead still does not replace that approval.
- WAY-30 explicitly narrows WAY-114 and names its area. WAY-172's binding text remains unchanged; its changed relation is propagated.
- Six changed invariants retain their sentences, methods, versions and parts. Their updated WAY-46 references remain consistent with that decision's unchanged criticality/detection computation.
- The part-map template and skill both preserve required failure-mode damage, severity and detection information. They permit transcription only from the named sources of human authorization.
- The task template and refinement skill now account for the existing no-plan route, consistent with WAY-36 and WAY-136. They create no new implementation artifact.
- The report-location change in the repository README agrees with the critique skill's inside/outside-cycle distinction.
- Explicitly excluding commit messages reinforces WAY-10's already-existing reasoning filter.
- The two guard runs below report no relation-fingerprint failure. This establishes only those mechanical checks, not the fidelity of proposed meanings.
- No executable production code or invariant test changes occur in the assessed ten-file diff. No deliberate-break exercise was needed for a changed test.

## Validation and limitations

Manual checks: performed by this assessor through diff/source comparison and source tracing as described above. Command/exit/output for the manual conclusions: not applicable; file anchors are their evidence.

Automated checks: only the following two guards were run. Full combined tool stdout/stderr and actual exit codes are retained below. The merge comparison uses the assessed base, not a claim about the latest integration tip. Decisions exit 1 is not a pass: its version-copy and placeholder errors are the pre-main conditions the changed README explicitly expects. Five overdue-review warnings remain visible. Invariants exit 0 still includes one unchecked category and absence of human verdicts. No full gate, test suite, live cycle, temp-plan extraction experiment or semantic completeness proof was run.

The complete foundation reads and current-Scope reconciliation establish no additional remark requiring settlement. They confirm the existing approval-route collision against the broader governing rules, including WAY-150's source-selection requirements. All current invariant Part fields, methods and critical-flow references were inspected through the complete invariant/map reads; reading the superset leaves no reached invariant unread. The glossary's complete terms and Avoid spellings reveal no additional wording concern in this diff. Environment facts were read as the repository's recorded premises, not independently reverified against external publishers. The source task's fidelity and the human's actual settlements were intentionally not evaluated; the author must settle remarks without silently changing them. Different-model independence cannot be established from the filtered materials.


### Command

```text
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto f0b5eb131de5d681ee3fcdeb264e9f88778af2ec --today 2026-10-21
```

Exit code: 1

Full output:

```text
foundations/decisions.md:869: error: WAY-30/1 differs from its copy on f0b5eb131de5d681ee3fcdeb264e9f88778af2ec; the log after the merge holds this copy
foundations/decisions.md:898: error: WAY-30/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:1310: error: WAY-46/1 differs from its copy on f0b5eb131de5d681ee3fcdeb264e9f88778af2ec; the log after the merge holds this copy
foundations/decisions.md:1342: error: WAY-46/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:5734: error: WAY-172/1 differs from its copy on f0b5eb131de5d681ee3fcdeb264e9f88778af2ec; the log after the merge holds this copy
foundations/decisions.md:5762: error: WAY-172/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:7691: error: WAY-224/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:71: warning: WAY-03: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:635: warning: WAY-21: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:898: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:1342: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:1490: warning: WAY-52: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1572: warning: WAY-55: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1986: warning: WAY-69: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:5762: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:7691: warning: *Approved by* is the placeholder `merge of <request link>`
unchecked: the lines the log holds on the main branch, and the versions it gains per number — --base none: there is no commit the branch left the main branch from
unchecked: a change to the template without a new version in the log — --base none: there is no commit the branch left the main branch from
7 error(s), 9 warning(s), 2 unchecked
```

### Command

```text
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto f0b5eb131de5d681ee3fcdeb264e9f88778af2ec
```

Exit code: 0

Full output:

```text
unchecked: identifiers, versions, corrections and the list of violated invariants — --base none: there is no commit the branch left the main branch from
note: there is no human_verdicts.md; no human verdict is given
0 error(s), 0 warning(s), 1 unchecked
```

## Completed foundation selection and read reconciliation

Foundation revision: `8726cc1c6b6b031ca94c6e867d0df1297c286c01`. Touched parts remain those listed above; collective foundation files were mapped by their changed entries, not assigned wholesale to their container. The complete current Scope inspection includes wrapped values and latest versions. There are 210 current decisions, all version 1, with no repeals or missing Scope fields. The nine-part selection matches 207 decisions. The three outside that selection are WAY-94/1 (glossary, relation-model), WAY-96/1 (glossary), and WAY-141/1 (installation). They were also read whole, so explicitly named decisions and governing relations cannot leave a missing read merely because they fall outside Scope.

Expected matches are exactly the 207 identifiers with heading-line anchors in the output below, all in `foundations/decisions.md`. Declared selected/read set: all 210 current entries, comprising those 207 matches and the three explicitly listed outside them. Expected minus read: empty. Merely discovered but unread decisions: empty. The complete invariants read similarly includes all `every` entries, touched Part matches, methods naming a changed file and invariants of both map critical flows. This is a reading reconciliation, not proof of semantic completeness or a pass of `decisions-found-for-change` (whose method remains TODO).

The following read-only inventory command supplemented the full reads. Working directory: `C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks`. It wrote no script or repository file. Actual exit code: 0. Full output follows the exact command.

```powershell
@'
import re
from pathlib import Path
s=Path('foundations/decisions.md').read_text(encoding='utf-8')
parts=set('agent-instructions elements-common part-map project-level task-cycle decisions invariants environment-facts product-guidelines'.split())
heads=list(re.finditer(r'^### (WAY-\d+)/(\d+).*$',s,re.M))
latest={}
for i,m in enumerate(heads):
    block=s[m.start():heads[i+1].start() if i+1<len(heads) else len(s)]
    scope=re.search(r'^- \*\*Scope:\*\* (.*?)(?=\n- \*\*|\Z)',block,re.M|re.S)
    value=(int(m[2]),s[:m.start()].count('\n')+1,block,scope[1].strip() if scope else 'MISSING')
    if m[1] not in latest or value[0]>latest[m[1]][0]: latest[m[1]]=value
assert 'WAY-01' in latest and 'WAY-224' in latest
selected=[];excluded=[];repealed=[];missing=[]
for key,(version,line,block,scope) in latest.items():
    if scope=='MISSING': missing.append(key)
    if re.search(r'^- \*\*Change:\*\* repeal',block,re.M):
        repealed.append(key); continue
    matches=parts.intersection(re.findall(r'[a-z]+(?:-[a-z]+)*',scope))
    if matches: selected.append(f'{key}/{version}:{line}')
    else: excluded.append(f'{key}/{version}:{line} Scope={scope}')
print('latest entries:',len(latest))
print('selected:',len(selected))
print(', '.join(selected))
print('excluded:')
print('\n'.join(excluded))
print('repealed:',repealed)
print('missing Scope:',missing)
'@ | python -B -
```

```text
latest entries: 210
selected: 207
WAY-01/1:6, WAY-02/1:38, WAY-03/1:71, WAY-04/1:95, WAY-05/1:137, WAY-07/1:176, WAY-08/1:203, WAY-09/1:234, WAY-10/1:317, WAY-11/1:355, WAY-12/1:396, WAY-13/1:426, WAY-14/1:471, WAY-16/1:492, WAY-17/1:519, WAY-18/1:543, WAY-19/1:575, WAY-20/1:608, WAY-21/1:635, WAY-22/1:657, WAY-24/1:685, WAY-25/1:720, WAY-26/1:749, WAY-27/1:775, WAY-28/1:806, WAY-29/1:838, WAY-30/1:869, WAY-31/1:911, WAY-32/1:946, WAY-33/1:972, WAY-34/1:1003, WAY-35/1:1032, WAY-36/1:1066, WAY-37/1:1095, WAY-38/1:1122, WAY-40/1:1152, WAY-41/1:1177, WAY-42/1:1203, WAY-43/1:1226, WAY-44/1:1253, WAY-45/1:1284, WAY-46/1:1310, WAY-47/1:1357, WAY-48/1:1384, WAY-49/1:1410, WAY-51/1:1454, WAY-52/1:1490, WAY-53/1:1516, WAY-54/1:1539, WAY-55/1:1572, WAY-56/1:1603, WAY-57/1:1633, WAY-58/1:1676, WAY-60/1:1723, WAY-61/1:1759, WAY-62/1:1813, WAY-63/1:1844, WAY-64/1:1881, WAY-65/1:1921, WAY-68/1:1952, WAY-69/1:1986, WAY-71/1:2022, WAY-72/1:2060, WAY-73/1:2086, WAY-74/1:2119, WAY-76/1:2154, WAY-77/1:2183, WAY-78/1:2213, WAY-79/1:2236, WAY-80/1:2266, WAY-81/1:2301, WAY-82/1:2346, WAY-83/1:2375, WAY-84/1:2403, WAY-85/1:2436, WAY-86/1:2468, WAY-89/1:2502, WAY-90/1:2531, WAY-93/1:2564, WAY-95/1:2632, WAY-97/1:2712, WAY-98/1:2748, WAY-99/1:2782, WAY-100/1:2814, WAY-101/1:2840, WAY-102/1:2863, WAY-103/1:2890, WAY-104/1:2915, WAY-105/1:2969, WAY-106/1:3018, WAY-107/1:3044, WAY-108/1:3070, WAY-109/1:3101, WAY-110/1:3124, WAY-111/1:3148, WAY-112/1:3177, WAY-113/1:3207, WAY-114/1:3243, WAY-115/1:3272, WAY-116/1:3303, WAY-117/1:3331, WAY-118/1:3360, WAY-119/1:3394, WAY-120/1:3421, WAY-121/1:3453, WAY-122/1:3531, WAY-123/1:3590, WAY-124/1:3629, WAY-125/1:3679, WAY-126/1:3741, WAY-127/1:3788, WAY-128/1:3847, WAY-129/1:3889, WAY-130/1:3915, WAY-131/1:3955, WAY-132/1:3987, WAY-133/1:4025, WAY-134/1:4060, WAY-135/1:4114, WAY-136/1:4165, WAY-137/1:4239, WAY-138/1:4279, WAY-139/1:4329, WAY-140/1:4368, WAY-142/1:4447, WAY-143/1:4499, WAY-144/1:4537, WAY-145/1:4574, WAY-146/1:4620, WAY-147/1:4660, WAY-148/1:4691, WAY-149/1:4737, WAY-150/1:4779, WAY-151/1:4817, WAY-152/1:4854, WAY-153/1:4885, WAY-154/1:4927, WAY-155/1:4965, WAY-156/1:5000, WAY-157/1:5035, WAY-158/1:5064, WAY-159/1:5091, WAY-160/1:5121, WAY-161/1:5151, WAY-162/1:5217, WAY-163/1:5289, WAY-164/1:5332, WAY-165/1:5371, WAY-166/1:5418, WAY-167/1:5453, WAY-168/1:5524, WAY-169/1:5597, WAY-170/1:5639, WAY-171/1:5682, WAY-172/1:5734, WAY-173/1:5777, WAY-174/1:5812, WAY-175/1:5847, WAY-176/1:5940, WAY-177/1:5980, WAY-178/1:6008, WAY-179/1:6034, WAY-180/1:6061, WAY-181/1:6087, WAY-182/1:6113, WAY-183/1:6140, WAY-184/1:6164, WAY-185/1:6193, WAY-186/1:6223, WAY-187/1:6264, WAY-188/1:6303, WAY-189/1:6334, WAY-190/1:6369, WAY-191/1:6405, WAY-192/1:6441, WAY-193/1:6477, WAY-194/1:6513, WAY-195/1:6552, WAY-196/1:6650, WAY-197/1:6691, WAY-198/1:6736, WAY-199/1:6771, WAY-200/1:6806, WAY-201/1:6838, WAY-202/1:6867, WAY-203/1:6901, WAY-204/1:6945, WAY-205/1:6997, WAY-206/1:7040, WAY-207/1:7085, WAY-208/1:7117, WAY-209/1:7145, WAY-210/1:7177, WAY-211/1:7214, WAY-212/1:7246, WAY-213/1:7287, WAY-214/1:7323, WAY-215/1:7360, WAY-216/1:7402, WAY-217/1:7431, WAY-218/1:7457, WAY-219/1:7489, WAY-220/1:7525, WAY-221/1:7551, WAY-222/1:7581, WAY-223/1:7615, WAY-224/1:7666
excluded:
WAY-94/1:2598 Scope=glossary, relation-model
WAY-96/1:2678 Scope=glossary
WAY-141/1:4423 Scope=installation
repealed: []
missing Scope: []
```

An initial exploratory inventory used `^##` for decision headings and returned zero. A positive-control read of the first entry and final Scope lines exposed that decisions use `###`; that result was discarded, not treated as an empty foundation. The corrected command above asserts the first and last current decision IDs before reporting. These inventory counts describe repository entries, never empirical agent-behavior cases. No guards were rerun while completing source coverage.


