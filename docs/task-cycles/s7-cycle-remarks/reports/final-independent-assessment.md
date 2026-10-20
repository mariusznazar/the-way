# Independent foundation assessment

Assessor: gpt-6.1-sol. Author model supplied by the caller: gpt-6-astra. Date: 2026-10-21.

Assessed range: `f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..9a8bc5e7ae467a1dce81b4be830130c64337db0d`.

Recommendation: **rewrite the one guide sentence identified in R1; otherwise apply**. There is one small instruction-scope concern and no objection to the proposed foundation meanings. This is an assessor's recommendation, not approval or the author's settlement.

## Boundary and complete coverage

The assessment followed this worktree's `.agents/skills/the-way-critique/SKILL.md` and `elements/common/critique/SKILL.md`. Repository identity checks found no enclosing product and no `:/.the-way` gitlink. HEAD was the assessed head. I read the complete diff of exactly the ten files below and each complete head file, including every decision and invariant. An independent byte comparison against `git cat-file blob <head>:<path>` confirmed that the working files read were those exact snapshots. Output truncations in initial combined reads were repaired with bounded chunk reads; no omitted passage was treated as read.

| Assessed file | Complete head coverage |
|---|---:|
| `agent-instructions/README.md` | 1–52 |
| `elements/common/critique/SKILL.md` | 1–75 |
| `elements/common/way_of_working.md` | 1–208 |
| `elements/part-map/skill/SKILL.md` | 1–88 |
| `elements/part-map/template.md` | 1–251 |
| `foundations/decisions.md` | 1–7706 |
| `foundations/invariants.md` | 1–2268 |
| `project-level/task/skill/SKILL.md` | 1–218 |
| `project-level/task/template.md` | 1–152 |
| `task-cycle/skill/SKILL.md` | 1–609 |

The complete part map was read, including responsibilities, assignments, dependencies, failure modes, boundaries, flows, surfaces and closing lists. Touched parts: `agent-instructions`, `elements-common`, `part-map`, `project-level`, `task-cycle`, plus the scopes of changed decision entries: `decisions`, `invariants`, `environment-facts`, `product-guidelines`. No new part is proposed.

Scope discovery examined the complete current Scope values, including wrapped lines, for all 210 current decision entries. Every entry is version 1; no repeal was encountered. Expected matches: 207. Read set: all 210 entries whole, including binding text, fields, rationale and rejected options. Expected minus read: empty. The three additional entries read are WAY-94, WAY-96 and WAY-141. The exact 207 identifiers with source locations are retained in check A's complete output below. This reconciles discovery and reading; it is not a claim that Scope matching proves every semantic collision absent.

I also read the full shared form rules, the part-map, decision and invariant templates and their example lists; the named examples are covered by the whole map/log/invariant reads. The complete glossary and violated-invariants list were read. Whole-foundation semantic inspection covered all five elements: the complete decisions, invariants, part map and glossary plus searches of environment facts for failure modes/candidates, human approval, settlements, independent assessment, chronology, recurrence, counterarguments and brief/workspace terms. No additional relevant environment-fact entry was found by those searches. This assessment is not a substitute for the author's two WAY-33 searches against the actual integration tip.

`product-guidelines/reading.md` was read. No `guidelines/` directory exists here; these ten changes are process prose rather than product code or screens. No coding/style guideline selection is applicable to this assessed diff. The guard source inspected below was read only to establish its existing mechanism, not changed.

Permitted method-source reading included installed Superpowers 6.4.1 `subagent-driven-development/SKILL.md`, its full `scripts/task-brief` and `scripts/sdd-workspace`, and this repository's `task-cycle/plan/SKILL.md`. I read no actual task document, spec, plan, operational handoff, author defense, cycle record, other report, session transcript or commit message. Hash-only history used explicit `--format=%H %aI`; file snapshots used explicit hashes and paths. Metadata naming an approver is not evidence of actual human approval. Every changed meaning remains a proposal for the human's review.

## Remarks

### R1. Keep operational failures outside the pre-main filtering exception

**Category:** worth correcting; new thread. **Anchor:** C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks/agent-instructions/README.md:33.

**To paste:** The new instruction to act only on relation-fingerprint findings also excludes an operational failure that prevents those findings from being produced. Please preserve the exception for expected version-copy and request-link findings, while requiring repair of errors that leave the fingerprint checks unrun.

**Why I raise this:** The added run is intended to catch stale dependent references before the request, because the ordinary `--merge-onto none` run cannot compare them. The current sentence is: “`--merge-onto <the current foundations tip>` and act only on their relation-fingerprint findings”. This is broader than the two expected finding classes named immediately afterwards.

Existing source mechanism: `elements/decisions/format_guard.py:831` reads the target log; lines 832–834 record a general error and return `None` on failure. At lines 1195–1200, fingerprint checking runs only after successful target resolution and a non-None merged log. In `elements/invariants/format_guard.py:1412`, a failed target-log read likewise records a general error and returns `None`; lines 1634–1645 skip `check_fingerprints` unless the merged decisions, target invariants and merged facts were all obtained. Such an error is not itself a relation-fingerprint finding. For example, if Git cannot read the target snapshot, the report can contain an operational error and no stale-reference finding at all. Following 'act only' literally would leave the new safeguard unperformed. This is a source-derived failure path, not a claim that it occurred in an excluded cycle.

The surrounding guide already requires recording failed and unchecked work, but recording an operational failure as debt does not complete the new comparison. The cheaper repair is one local qualification, not another check or process layer.

**Requested full replacement for the newly added passage:**

> Before the request, also run the decisions and invariants guards with
> `--merge-onto <the current foundations tip>`. Act on their relation-fingerprint findings and
> resolve any operational error that prevents those checks from running; their findings about
> copies of a version and about a placeholder request link are expected before `main`.

**Cost both ways:** Keeping the sentence costs no edit and works on successful runs, but leaves a failed comparison without a required recovery action. The replacement adds one explicit condition and no extra normal-path execution or maintenance artifact. It keeps the intended pre-main exceptions unchanged.

## Independent checks with no other concern

### Approval already carried by a task

Checked WAY-30 (`foundations/decisions.md:869`), WAY-114 (`:3243`), WAY-124 (`:3629`), WAY-134 (`:4060`), WAY-172 (`:5734`), shared step 4.2 (`elements/common/way_of_working.md:157`) and the foundation step (`task-cycle/skill/SKILL.md:299`). **No concern found.** WAY-30 still requires the decision's approver to approve the plan/document before dependent code; an orchestrator's provisional go-ahead is not that approval. The new explicit `narrows WAY-114` relation resolves the two competing instructions without relying on a transitive precedence inference. Changed meaning beyond the approved source still returns to the human. Task readiness requires acceptance of the complete document, not merely candidate rows.

Benefit and timing: the entry writer can transcribe an already accepted meaning without another approval round. Keeping the old ambiguity risks a redundant stop; the change costs a precise comparison with the approved source, which the cycle already has to read. Treating any agent plan as human-approved would overapply the rule, but its explicit approver condition and WAY-125's distinction prevent that reading. Actual approval of this proposal was not independently verified and is not presumed.

### Human authorization of failure modes and candidate questions

Checked complete WAY-46 (`foundations/decisions.md:1310`), new WAY-224 (`:7666`), WAY-04, WAY-11, WAY-13, WAY-25, WAY-113/114 and the part-map skill/template (`elements/part-map/skill/SKILL.md:51`, `elements/part-map/template.md:182`), the foundation/return steps and request (`task-cycle/skill/SKILL.md:308`, `:417`, `:571`). **No concern found.** The human supplies or accepts the judgment; the agent may type it. A newly discovered unaccepted mode is a question rather than an entry silently written or an accepted settlement silently deferred. WAY-224 explicitly narrows WAY-114 for this case, including where there is a recommendation and no approved decision changes.

The question carries part, failure, damage, severity, detection, recommendation and its strongest counterargument. The part-map representation still holds severity and detection, and criticality remains computed. A task-commanded mode needs no repeated question. Acceptance is applied as a correction to the existing request before merge, so accepted criticality does not wait for a separate task. The existing correction route owns affected verification and assessment. No concern about the six unchanged invariant sentences: their checks still cover the same shape/computation properties after their WAY-46 link renewal.

Benefit: the human can judge a concrete proposal at the request without the agent making that judgment alone. The cost is one additional decision when a genuine candidate exists, and verification of the accepted correction. The cheaper alternative of a point-of-use note would leave no defined route past the prohibition on deferring entries; silently entering the mode would take the human's judgment. Applying the counterargument requirement to all questions would be unnecessary expansion; the proposed rule expressly limits it to candidate failure modes.

### Slice briefs and workspace identity

Checked `task-cycle/skill/SKILL.md:127` against `task-cycle/plan/SKILL.md:75` (actual `### Slice 1` form), the installed 6.4.1 `scripts/task-brief:34` onward (awk recognizes Task headings), and `scripts/sdd-workspace:36` onward (workspace identity is the normalized input plan path). **No concern found.** A disposable heading-adapted copy lets the existing extractor recognize slices without changing the actual plan format. The explicit third output argument puts the brief in the workspace resolved from the original plan; later review packages/ledger therefore use that same owner. Removing the temporary copy after extraction preserves one authoritative plan.

Keeping the old adapter permits a real format mismatch: the extractor does not recognize Slice headings. Letting its default output use the temporary file also changes workspace identity. The proposed adapter costs a temporary copy and heading substitution per extraction; changing all plan headings or forking the borrowed script would affect more consumers or maintain a second implementation. I did not execute the borrowed scripts because they create workspace artifacts outside the sole authorized report write. Source inspection establishes compatibility, not an observed end-to-end dispatch result.

### Implementation choices when there is no plan

Checked `project-level/task/skill/SKILL.md:120`, `project-level/task/template.md:89` and `:95` against WAY-36, WAY-124, WAY-135, WAY-136 and the no-plan route in the complete cycle. **No concern found.** The changed wording gives implementation choices an existing durable home in the cycle record. It does not turn unsettled product requirements into implementation choices or remove the requirement to settle blocking product questions before readiness.

Keeping the old wording points a no-plan task at a nonexistent plan. The replacement costs only source alignment; creating a separate plan or another choices artifact would duplicate existing cycle storage.

### Assessor inputs and assessment record

Checked `elements/common/critique/SKILL.md:19`, `agent-instructions/README.md:44` and `task-cycle/skill/SKILL.md:428` against WAY-10, WAY-120, WAY-148 and WAY-149. **No concern found.** Naming commits by hash avoids exposing commit-message author reasoning while still identifying the diff/snapshots. The guide now delegates the assessment record location to the same skill as the cycle. Outside a cycle the skill still gives the commit-message location; inside it, full report and settlement stay under reports. The exception is input filtering, not a removal of full target/source reads.

Keeping the old wording risks feeding the assessor commit messages or maintaining two conflicting record destinations. The update costs no extra review or record; expanding it to exclude product source files would impair assessment, but the current filtered input rule still permits governing repository sources.

### Form, links and internal consistency

Checked decision form (one to three binding sentences, required fields, rationale/rejected material and explicit precedence), new decision numbering, scopes, invariant sentence/version preservation and incoming dependents. **No further concern found.** Current binding fingerprints are WAY-30 `2141bece`, WAY-46 `7511b86f`, WAY-114 `04b4f599`, WAY-224 `f4441cce`. WAY-172's incoming WAY-30 relation and all six WAY-46 invariant links match the changed binding parts; WAY-224's WAY-46 relation matches too. No altered invariant sentence or test was found in the assessed range.

The guard runs below confirm no reported relation/link fingerprint mismatch at the assessed head; the decisions run's four placeholder errors are visible and are not a successful full-gate verdict. Other warnings and unchecked work remain named. Testing every unchanged part again would not improve this source assessment.

## History, behavioral evidence and limits

Hash-only history and the relevant whole historical rule entries were inspected. WAY-30 first appears at `0fb5b757532b68d15639f250bf51e36fea50ba1b` (2026-09-16), requiring the decision's approver to approve the plan. WAY-46 first appears at `9d3f0ebc054a65811dd300e43dfc9c689036bc1a` (2026-09-17), already reserving failure-mode judgment to a human. WAY-114's current question boundary is present at `5f0466cceab6d5338198d6b0ea8badb5d50262f3` (2026-10-06). The filtered independent-assessment rule is present in the critique skill at `904cc45838af5171a608e31088f0bbca649241a4` (2026-10-06). The file-mediated dispatch contract appears at `19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f` (2026-10-14). Those dates establish when text entered Git, not when a human approved it or how often it worked.

The new changes appear in the assessed hash-only history at `3d0fa8480fdae3af92ca0493b4237bfa0950223d` and `8726cc1c6b6b031ca94c6e867d0df1297c286c01` on 2026-10-21. I compared their resulting text with the earlier rules rather than treating a recent rule as proof that another layer is needed.

Behavioral frequency and recurrence after those rules began to apply: **unavailable**. Records examined for that purpose: **0**, period: **none**, genuine cases/mentions/dated examples: **not measured**. I checked the permitted input boundary: the caller expressly excludes transcripts, run/cycle records and task chronology; I did not search those excluded stores or replace the missing measurement with an estimate. The source-level Task/Slice mismatch and conflicting approval instructions are concrete static mechanisms, not measured agent incidents. Claims that these changes reduce stops or save attention remain predicted benefits, not demonstrated effectiveness.

Source fidelity: the policy wording was compared with the permitted governing foundation/templates/skills, and the brief adapter with installed method source. Fidelity to the human's exact task settlements, why this particular work was requested, actual prior incidents and approval dates cannot be checked because those sources are excluded. The record's approval metadata does not fill that gap. R1 requires no change to a human meaning; the author should still verify that distinction when settling it.

## What can be cut

Cut the blanket restriction 'act only on their relation-fingerprint findings' in favor of R1's narrower successful-execution requirement. I recommend no removal of any other substantive change. The new candidate route answers a distinct question from computation of criticality, the explicit precedence prevents an actual instruction conflict, and the heading/workspace adapter uses existing tooling rather than adding a new mechanism. No new index, report system, test suite or general counterargument policy is needed.

## Executed checks

No broad test suite was rerun. Check commands below were read-only and wrote no product or other report artifact. Exit codes are actual tool results. The two guards were run against the assessed head, not the live integration tip; these establish local form/link evidence only. The caller still owns integration-tip checks and full required verification.

### A. Exact snapshot and exhaustive Scope inventory

Command: PowerShell here-string piped to `python -B -`, with the following complete stdin program. Exit: 0.

```python
import pathlib,re,subprocess
head='9a8bc5e7ae467a1dce81b4be830130c64337db0d'
base='f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
files=['agent-instructions/README.md','elements/common/critique/SKILL.md','elements/common/way_of_working.md','elements/part-map/skill/SKILL.md','elements/part-map/template.md','foundations/decisions.md','foundations/invariants.md','project-level/task/skill/SKILL.md','project-level/task/template.md','task-cycle/skill/SKILL.md']
for p in files:
 b=subprocess.run(['git','cat-file','blob',head+':'+p],capture_output=True,check=True).stdout
 print('SNAPSHOT',len(b.splitlines()),p,'MATCH' if pathlib.Path(p).read_bytes()==b else 'DIFF')
s=subprocess.run(['git','cat-file','blob',head+':foundations/decisions.md'],capture_output=True,check=True).stdout.decode('utf-8')
parts={'agent-instructions','elements-common','part-map','decisions','invariants','environment-facts','project-level','task-cycle','product-guidelines'}
entries=list(re.finditer(r'^### (WAY-\d+)/(\d+).*$',s,re.M)); current={}; malformed=[]
for i,m in enumerate(entries):
 body=s[m.start():entries[i+1].start() if i+1<len(entries) else len(s)]
 scope=re.search(r'^- \*\*Scope:\*\* (.*(?:\n  .*)*)',body,re.M)
 if not scope: malformed.append(m[1]); continue
 scopes=set(re.split(r',\s*',scope[1].replace('\n','').strip()))
 current[m[1]]=(int(m[2]),s[:m.start()].count('\n')+1,scopes)
expected=[(k,v[1]) for k,v in current.items() if parts&v[2]]
print('TOUCHED',','.join(sorted(parts)))
print('CURRENT',len(current),'SCOPE_MALFORMED',','.join(malformed) or 'none','EXPECTED',len(expected))
print('EXPECTED_IDS_LOCATIONS',' '.join(k+':'+str(n) for k,n in expected))
print('READ_SET all',len(current),'current entries; missing expected: none')
print('GUIDELINES_DIRECTORY_EXISTS',pathlib.Path('guidelines').exists())
for p,pat in [('foundations/decisions.md','WAY-30/1'),('foundations/decisions.md','WAY-46/1'),('foundations/decisions.md','WAY-114/1'),('elements/common/critique/SKILL.md','For a change to an invariant test'),('task-cycle/skill/SKILL.md','For each operational dispatch')]:
 result=subprocess.run(['git','log','--format=%H %aI','--reverse','-G',pat,base,'--',p],capture_output=True,text=True,check=True)
 print('HISTORY',p,pat); print(result.stdout.strip())
```

The READ_SET line declares the manual whole-file read coverage; the script computes the expected set, not whether a reader understood the text. Complete stdout/stderr:

```text
SNAPSHOT 52 agent-instructions/README.md MATCH
SNAPSHOT 75 elements/common/critique/SKILL.md MATCH
SNAPSHOT 208 elements/common/way_of_working.md MATCH
SNAPSHOT 88 elements/part-map/skill/SKILL.md MATCH
SNAPSHOT 251 elements/part-map/template.md MATCH
SNAPSHOT 7706 foundations/decisions.md MATCH
SNAPSHOT 2268 foundations/invariants.md MATCH
SNAPSHOT 218 project-level/task/skill/SKILL.md MATCH
SNAPSHOT 152 project-level/task/template.md MATCH
SNAPSHOT 609 task-cycle/skill/SKILL.md MATCH
TOUCHED agent-instructions,decisions,elements-common,environment-facts,invariants,part-map,product-guidelines,project-level,task-cycle
CURRENT 210 SCOPE_MALFORMED none EXPECTED 207
EXPECTED_IDS_LOCATIONS WAY-01:6 WAY-02:38 WAY-03:71 WAY-04:95 WAY-05:137 WAY-07:176 WAY-08:203 WAY-09:234 WAY-10:317 WAY-11:355 WAY-12:396 WAY-13:426 WAY-14:471 WAY-16:492 WAY-17:519 WAY-18:543 WAY-19:575 WAY-20:608 WAY-21:635 WAY-22:657 WAY-24:685 WAY-25:720 WAY-26:749 WAY-27:775 WAY-28:806 WAY-29:838 WAY-30:869 WAY-31:911 WAY-32:946 WAY-33:972 WAY-34:1003 WAY-35:1032 WAY-36:1066 WAY-37:1095 WAY-38:1122 WAY-40:1152 WAY-41:1177 WAY-42:1203 WAY-43:1226 WAY-44:1253 WAY-45:1284 WAY-46:1310 WAY-47:1357 WAY-48:1384 WAY-49:1410 WAY-51:1454 WAY-52:1490 WAY-53:1516 WAY-54:1539 WAY-55:1572 WAY-56:1603 WAY-57:1633 WAY-58:1676 WAY-60:1723 WAY-61:1759 WAY-62:1813 WAY-63:1844 WAY-64:1881 WAY-65:1921 WAY-68:1952 WAY-69:1986 WAY-71:2022 WAY-72:2060 WAY-73:2086 WAY-74:2119 WAY-76:2154 WAY-77:2183 WAY-78:2213 WAY-79:2236 WAY-80:2266 WAY-81:2301 WAY-82:2346 WAY-83:2375 WAY-84:2403 WAY-85:2436 WAY-86:2468 WAY-89:2502 WAY-90:2531 WAY-93:2564 WAY-95:2632 WAY-97:2712 WAY-98:2748 WAY-99:2782 WAY-100:2814 WAY-101:2840 WAY-102:2863 WAY-103:2890 WAY-104:2915 WAY-105:2969 WAY-106:3018 WAY-107:3044 WAY-108:3070 WAY-109:3101 WAY-110:3124 WAY-111:3148 WAY-112:3177 WAY-113:3207 WAY-114:3243 WAY-115:3272 WAY-116:3303 WAY-117:3331 WAY-118:3360 WAY-119:3394 WAY-120:3421 WAY-121:3453 WAY-122:3531 WAY-123:3590 WAY-124:3629 WAY-125:3679 WAY-126:3741 WAY-127:3788 WAY-128:3847 WAY-129:3889 WAY-130:3915 WAY-131:3955 WAY-132:3987 WAY-133:4025 WAY-134:4060 WAY-135:4114 WAY-136:4165 WAY-137:4239 WAY-138:4279 WAY-139:4329 WAY-140:4368 WAY-142:4447 WAY-143:4499 WAY-144:4537 WAY-145:4574 WAY-146:4620 WAY-147:4660 WAY-148:4691 WAY-149:4737 WAY-150:4779 WAY-151:4817 WAY-152:4854 WAY-153:4885 WAY-154:4927 WAY-155:4965 WAY-156:5000 WAY-157:5035 WAY-158:5064 WAY-159:5091 WAY-160:5121 WAY-161:5151 WAY-162:5217 WAY-163:5289 WAY-164:5332 WAY-165:5371 WAY-166:5418 WAY-167:5453 WAY-168:5524 WAY-169:5597 WAY-170:5639 WAY-171:5682 WAY-172:5734 WAY-173:5777 WAY-174:5812 WAY-175:5847 WAY-176:5940 WAY-177:5980 WAY-178:6008 WAY-179:6034 WAY-180:6061 WAY-181:6087 WAY-182:6113 WAY-183:6140 WAY-184:6164 WAY-185:6193 WAY-186:6223 WAY-187:6264 WAY-188:6303 WAY-189:6334 WAY-190:6369 WAY-191:6405 WAY-192:6441 WAY-193:6477 WAY-194:6513 WAY-195:6552 WAY-196:6650 WAY-197:6691 WAY-198:6736 WAY-199:6771 WAY-200:6806 WAY-201:6838 WAY-202:6867 WAY-203:6901 WAY-204:6945 WAY-205:6997 WAY-206:7040 WAY-207:7085 WAY-208:7117 WAY-209:7145 WAY-210:7177 WAY-211:7214 WAY-212:7246 WAY-213:7287 WAY-214:7323 WAY-215:7360 WAY-216:7402 WAY-217:7431 WAY-218:7457 WAY-219:7489 WAY-220:7525 WAY-221:7551 WAY-222:7581 WAY-223:7615 WAY-224:7666
READ_SET all 210 current entries; missing expected: none
GUIDELINES_DIRECTORY_EXISTS False
HISTORY foundations/decisions.md WAY-30/1
0fb5b757532b68d15639f250bf51e36fea50ba1b 2026-09-16T00:45:10+02:00
HISTORY foundations/decisions.md WAY-46/1
9d3f0ebc054a65811dd300e43dfc9c689036bc1a 2026-09-17T23:28:05+02:00
HISTORY foundations/decisions.md WAY-114/1
56a88e54566294ea47959400bc37c5c0519c616f 2026-10-04T00:26:14+02:00
5f0466cceab6d5338198d6b0ea8badb5d50262f3 2026-10-06T00:32:00+02:00
HISTORY elements/common/critique/SKILL.md For a change to an invariant test
904cc45838af5171a608e31088f0bbca649241a4 2026-10-06T00:18:17+02:00
HISTORY task-cycle/skill/SKILL.md For each operational dispatch
19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f 2026-10-14T00:53:05+02:00
```

### B. Focused renewal audit

Command: PowerShell here-string piped to `python -B -`, with the following complete stdin program. Exit: 0.

```python
import pathlib,re,hashlib,subprocess
head='9a8bc5e7ae467a1dce81b4be830130c64337db0d'
s=subprocess.run(['git','cat-file','blob',head+':foundations/decisions.md'],capture_output=True,check=True).stdout.decode('utf-8')
fps={}
for m in re.finditer(r'^### (WAY-\d+)/\d+[^\n]*\n\n(.*?)(?=\n\n)',s,re.M|re.S): fps[m[1]]=hashlib.sha256(re.sub(r'\s+',' ',m[2]).strip().encode()).hexdigest()[:8]
errors=[]
for p in ['foundations/decisions.md','foundations/invariants.md']:
 data=subprocess.run(['git','cat-file','blob',head+':'+p],capture_output=True,check=True).stdout.decode('utf-8')
 refs=[]
 for i,line in enumerate(data.splitlines(),1):
  if re.search(r'(derives from|narrows|Derives from)',line) or (line.startswith('  ') and 'WAY-' in line):
   for n,fp in re.findall(r'(WAY-\d+)@([a-f0-9]{8})',line):
    if n in {'WAY-30','WAY-46'}:
     refs.append((i,n,fp))
     if fps[n]!=fp: errors.append((p,i,n,fp,fps[n]))
 print(p,'changed-decision dependents:',','.join(str(i)+':'+n+'@'+fp for i,n,fp in refs))
print('FINGERPRINT_MISMATCHES',len(errors))
for err in errors: print(err)
print('VERDICT', 'PASS' if not errors else 'FAIL')
raise SystemExit(bool(errors))
```

Complete stdout/stderr:

```text
foundations/decisions.md changed-decision dependents: 5748:WAY-30@2141bece,7681:WAY-46@7511b86f
foundations/invariants.md changed-decision dependents: 763:WAY-46@7511b86f,773:WAY-46@7511b86f,783:WAY-46@7511b86f,793:WAY-46@7511b86f,803:WAY-46@7511b86f,813:WAY-46@7511b86f
FINGERPRINT_MISMATCHES 0
VERDICT PASS
```

### C. Decision guard

Command:

```powershell
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto 9a8bc5e7ae467a1dce81b4be830130c64337db0d
```

Actual exit: 1. Complete stdout/stderr:

```text
foundations/decisions.md:898: error: WAY-30/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:1342: error: WAY-46/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:5762: error: WAY-172/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:7696: error: WAY-224/1: *Approved by* is the placeholder `merge of <request link>`, which a merge onto the main branch does not take
foundations/decisions.md:71: warning: WAY-03: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:635: warning: WAY-21: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:898: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:1342: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:1490: warning: WAY-52: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1572: warning: WAY-55: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1986: warning: WAY-69: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:5762: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:7696: warning: *Approved by* is the placeholder `merge of <request link>`
unchecked: the lines the log holds on the main branch, and the versions it gains per number — --base none: there is no commit the branch left the main branch from
unchecked: a change to the template without a new version in the log — --base none: there is no commit the branch left the main branch from
4 error(s), 9 warning(s), 2 unchecked
```


### D. Invariants guard

Command:

```powershell
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto 9a8bc5e7ae467a1dce81b4be830130c64337db0d
```

Actual exit: 0. Complete stdout/stderr:

```text
unchecked: identifiers, versions, corrections and the list of violated invariants — --base none: there is no commit the branch left the main branch from
note: there is no human_verdicts.md; no human verdict is given
0 error(s), 0 warning(s), 1 unchecked
```


Assessment boundary reached. No fixes, source edits, commits, pushes or next workflow were performed. Only this report was written.

