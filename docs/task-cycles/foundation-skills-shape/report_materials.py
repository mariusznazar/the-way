from pathlib import Path
import subprocess,re,json,html
ROOT=Path.cwd(); RUN=ROOT/'.runs/task-cycles/foundation-skills-shape'; REPORTS=RUN/'reports'
BASE='745a6e53ec5c8eab3e078a32a61aa6a583a61a93'
parts=['decisions','invariants','glossary','environment-facts','part-map']
paths=[f'elements/{p}/skill/SKILL.md' for p in parts]+['elements/common/critique/SKILL.md','elements/common/way_of_working.md']
old={p:subprocess.check_output(['git','show',f'{BASE}:{p}']).decode('utf-8') for p in paths}
relocations=json.loads((RUN/'relocations.json').read_text(encoding='utf-8'))
def norm(s): return ' '.join(s.split())
def count(p,before=False):
    s=subprocess.check_output(['git','show',f'{BASE}:{p}']).decode('utf-8') if before else Path(p).read_text(encoding='utf-8')
    return len(s.split())
def anchor(p,a,b): return f'https://github.com/mariusznazar/the-way/blob/{BASE}/{p}#L{a}-L{b}'
def when(p,section):
    if 'Projected' in section: return 'When writing an entry projected into a project definition', 'Yes: the caller names projected mode and the definition; the SKILL.md names that mode directly'
    if 'first map' in section: return 'When the product has no part map and this invocation writes its first map', 'Yes: the missing map and the section name identify the variant'
    if 'withdrawal' in section: return 'When the fact is false or has no dependants and is withdrawn', 'Yes: the fact status and its dependants identify the variant'
    if 'critique' in p:
        if 'Check independently' in section: return 'At the independent check, for both author and critic', 'Yes: the dispatched critic and the author each see their role and check step'
        if 'Settle' in section: return 'When the author settles observations after the critic returns', 'Yes: the author is named in the pointer; the critic sees its no-write boundary in SKILL.md'
        if 'material' in section or 'fresh critic' in section: return 'When invoking a fresh critic or preparing its handoff', 'Yes: the author invokes it; mandatory collective-review and optional proposal triggers remain visible'
    if re.match(r'\d\.',section): return 'At '+section, 'Yes: the numbered step is present in SKILL.md and in the shared workflow'
    return 'Throughout this skill or shared workflow', 'Yes: entry metadata, overview or a named cross-step section is read with the skill'
def keep_reason(p,section,quote):
    if p.endswith('way_of_working.md'):
        return 'Keep. These shared steps apply across entry operations, or provide their navigation and source ownership. External callers retain the named How a skill asks, Reading the foundation and Critique before collective review sections. The separately conditional missing-file and projected procedures move to companions (WAY-256).'
    if '##'==quote[:2] or quote.startswith('---') or section=='overview': return 'Keep. Navigation, metadata, source ownership and picture of the whole; WAY-35 and WAY-256.'
    if section.startswith('3.') or ('Projected' in section and ('heading reads' in quote or '*Method*' in quote or 'project only' in quote or 'a fact is projected only' in quote or 'ask for no prefix' in quote)):
        return 'Keep unchanged; proposed template move only. This paragraph includes an existing entry-form or eligibility prescription. AC2 forbids moving that rule beside an element skill; templates are outside scope. WAY-256 exempts unchanged fragments. Proposal: put the entry prescription in this element\'s template and leave the operation or its pointer here; do not apply in this change.'
    if 'withdrawal' in section: return 'Keep. One instruction to withdraw through the template with dependent updates in the same change; a pointer would replace one instruction (WAY-256).'
    if 'first map' in section: return 'Keep heading and variant pointer; WAY-256.'
    if 'critique' in p: return 'Keep. Purpose, invitation and mandatory trigger, whole-set boundary and no critique of a foundation diff describe the whole operation for both roles; WAY-120.'
    return 'Keep. Single reading, following-entry or projected handoff instruction; a pointer would be one instruction too (WAY-256).'
intro='''# Assessment of the foundation skills\n\nMode: judge; kind: skill. Source: `745a6e53ec5c8eab3e078a32a61aa6a583a61a93`. The frozen task authorises the structural changes; the orchestrator accepts routine implementation choices and the human reviews the request. No rule is removed or changed in meaning. Proposed template moves remain proposals only.\n\n## Mechanical check and context\n\n`python -B instruction-files/check_instructions.py .` exited 0 before and after the change. It reported `WARN dead-path AGENTS.md:21 _zadania\\ does not exist`, and size lines for AGENTS.md (22 lines, 195 words), CLAUDE.md (1 line, 1 word), agent-instructions/README.md (78 lines, 721 words). The warning comes from treating the prose-relative private backlog directory as a repository path. The unchanged backlog pointer is reachable by the authorised orchestrator; this task changes none of these files. Claude Code, Codex and Cursor all follow the explicit step pointers; no loading mechanism changes. No check info says a file was skipped.\n\nThe active session starts in the the-way checkout, and this stage in its task worktree. Project entry points support Claude Code and Codex; Cursor compatibility is considered through the shared explicit-read layout. Codex config names CLAUDE.md as fallback and sets project_doc_max_bytes to 65536. The only Claude loading exclusion found is C:/Storage/AGENTS.md; project instruction behaviour is read from the existing AGENTS.md/CLAUDE.md pair. No new dependence on discovery or automatic imports is introduced.\n\nEvidence searched: current frozen task and git history of the seven files. In particular c005a49 supplies the shared selective-reading procedure; b066454 keeps critique for sets and sources rather than foundation diffs. Grounds below are carried decisions/steps and the whole-file costs measured in word-counts.md, not a claim of measured agent compliance. No additional behavioural claim or new rule is proposed; session-record measurement belongs to the task's post-merge follow-up.\n\n## Tables\n\nQuotes reproduce the complete stated source ranges. HTML line breaks preserve their line boundaries in table cells; entities only escape Markdown/HTML syntax. Blank separators are not separate instructions. Every nonblank source line belongs to a table row.\n\n'''
out=[intro]; records=[]
for p in paths:
    lines=old[p].splitlines(); moved=[r for r in relocations if r['path']==p]
    lookup={r['start']:r for r in moved}; covered=set(); section='overview'; entries=[]; i=1
    while i<=len(lines):
        if not lines[i-1].strip(): i+=1;continue
        if lines[i-1].startswith('## '): section=lines[i-1][3:]
        if i in lookup:
            r=lookup[i]; end=r['end']; quote='\n'.join(lines[i-1:end]); verdict='Move to `'+r['target']+'`. '+r['reason']
            if p.endswith('critique/SKILL.md') and section=='Settle the review': verdict+=' The critic no-write sentence stays visible in SKILL.md for both roles.'
        else:
            end=i
            while end<len(lines) and lines[end].strip() and end+1 not in lookup and not lines[end].startswith('## '): end+=1
            quote='\n'.join(lines[i-1:end]); verdict=keep_reason(p,section,quote)
            if 'Projected mode runs as' in quote: verdict='Reword without meaning change: point directly to elements/common/projected_mode.md, the shared mode instructions moved from way_of_working.md. The same mode remains the trigger.'
        need,recognise=when(p,section)
        if i in lookup:
            need=lookup[i].get('need',need)
            recognise=lookup[i].get('recognise',recognise)
        records.append(dict(path=p,start=i,end=end,quote=quote,need=need,recognise=recognise,verdict=verdict))
        i=end+1
    out += ['## '+p+'\n\n','| Full literal source fragment | Needed when | Will the agent recognise it? | Verdict, reason and ground |\n|---|---|---|---|\n']
    for r in [r for r in records if r['path']==p]:
        escaped=html.escape(r['quote'],quote=False).replace('|','&#124;').replace('\n','<br>')
        out.append(f'| [{p}:{r["start"]}-{r["end"]}]({anchor(p,r["start"],r["end"])}): <code>{escaped}</code> | {r["need"]} | {r["recognise"]} | {r["verdict"]} |\n')
    out.append('\n')
out.append('''## Entry-rule boundary and unapplied proposals\n\nExisting form-bearing paragraphs remain byte-for-byte in SKILL.md: decisions step 3 and projected prefix/heading; invariants Method, Derives from and Violated, plus projected fields/heading; glossary definition/Not and projected heading; environment-facts projected eligibility/heading; part-map drafting prescriptions and projected eligibility/heading. Their fields are already prescribed by the corresponding template (decision Decision entry and Verification; invariant Method and test, Links and Violated; glossary Form of an entry; environment facts Which facts are written; part map The binding part, Assigning files, Allowed dependencies, Trust boundary and Surfaces). Projected heading forms also have their shared source in project-level/definition_template.md. The proposed future template move would remove this duplication and allow the remaining drafting workflow to be split without moving entry rules into companions. Leaving them here costs context but preserves both the task scope and the current rule; doing the template work now would broaden this task beyond its accepted boundary. No remove verdict and no meaning-changing reword is applied.\n\nThe projected invariant and projected part-map routes have no element-specific companion: their entry prescriptions stay unchanged, and their remaining projected handoff/first-map exclusion is one instruction. They still read the common projected_mode.md. The withdrawal instruction remains inline for the same one-instruction exception.\n\n## Contradictions and reachability\n\nNo new contradiction was found between files read together. Existing form duplication is the unapplied proposal above. All source-owned rules remain referred to their template/common source. Numbered steps still occur in the original order; the common normal steps are modified by projected_mode.md before a projected operation is performed. The dependency chain for projected work is explicit both in each entry skill and in the retained Projected mode heading of way_of_working.md. find-foundation-entries reads the new common file for a project definition. The source-finding task variant does not project entries and retains its existing path.\n\nThe external anchors How a skill asks, Reading the foundation and Critique before collective review retain both their headings and bodies. The missing-element-file procedure is read at step 1 only outside projected mode and only when that file is absent. It keeps the start-file choice, stop, map assignment and ordering unchanged. The first-map heading stays in update-part-map, so the extracted common missing-map instruction still reaches the variant. The critic reads SKILL.md and check.md and sees its no-write boundary; the author additionally reads prepare.md and settle.md. No new global rule for when agents load files is added.\n''')
(REPORTS/'assessment.md').write_text(''.join(out),encoding='utf-8',newline='\n')
(RUN/'assessment_rows.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
# Routes count each whole source file once. Step companions are always read when that step is reached.
common='elements/common/way_of_working.md'; projected='elements/common/projected_mode.md'
missing='elements/common/missing_element_file.md'
normal={p:[f'elements/{p}/skill/SKILL.md',common]+[f'elements/{p}/skill/{f}.md' for f in ['read','decide_entry','draft','write'] if Path(f'elements/{p}/skill/{f}.md').exists()] for p in parts}
routes=[]
for p in parts:
    before=[f'elements/{p}/skill/SKILL.md',common]
    routes.append((p+' / foundation entry',before,normal[p]))
    after=normal[p]+[projected]
    if Path(f'elements/{p}/skill/projected.md').exists(): after += [f'elements/{p}/skill/projected.md']
    routes.append((p+' / projected entry',before,after))
    if p!='part-map':
        routes.append((p+' / first element file',before,normal[p]+[missing]))
routes.append(('environment-facts / withdrawal',['elements/environment-facts/skill/SKILL.md',common],normal['environment-facts']))
routes.append(('part-map / first map',['elements/part-map/skill/SKILL.md',common],normal['part-map']+[missing,'elements/part-map/skill/first_map.md']))
critic='elements/common/critique/'
routes.append(('critique / critic',[critic+'SKILL.md'],[critic+'SKILL.md',critic+'check.md']))
routes.append(('critique / author invoking and settling',[critic+'SKILL.md'],[critic+'SKILL.md',critic+'prepare.md',critic+'check.md',critic+'settle.md']))
wc=['# Whole-route word counts\n\nWords are whitespace-separated tokens (`len(text.split())`), including Markdown syntax and frontmatter. Before is 745a6e53ec5c8eab3e078a32a61aa6a583a61aa6a583a61a93 (short name 745a6e5); after is the task worktree. Each listed file counts once per complete invocation, even if more than one step points to it. Numbers cover the six skills, the shared workflow and their companions. Templates/rules are shown once in the fixed-addition table below. Product foundation entries, the input proposal, source documents and examples are outside this task\'s specified count and vary by invocation; their required reading has not changed.\n\n']
wc[0]=wc[0].replace('745a6e53ec5c8eab3e078a32a61aa6a583a61aa6a583a61a93',BASE)
wc+=['| Complete route | Before | After | After minus before |\n|---|---:|---:|---:|\n']
for name,before,after in routes:
    b=sum(count(p,True) for p in set(before));a=sum(count(p) for p in set(after));wc.append(f'| {name} | {b} | {a} | {a-b:+} |\n')
wc+=['\n## Files read on each route\n\nBefore: each entry route reads its SKILL.md and elements/common/way_of_working.md. Each critique role reads elements/common/critique/SKILL.md. After:\n\n']
for name,before,after in routes: wc.append('- **'+name+'**: '+', '.join('`'+p+'`' for p in after)+'.\n')
wc+=['\n## Fixed addition, counted once per invocation\n\n| Entry kind | Element template | Common rules | Sum to add before and after |\n|---|---:|---:|---:|\n']
rules=count('elements/common/rules.md')
for p in parts:
    t=count(f'elements/{p}/template.md');wc.append(f'| {p}: `elements/{p}/template.md` | {t} | {rules} | {t+rules} |\n')
wc.append('| critique | 0 | 0 | 0; this skill mandates neither an element template nor common rules |\n')
wc.append(f'''\n## Conditional reading\n\n- The projected common file is read only in projected mode. The three projected element companions are read only for that mode; invariant and part-map projected instructions remain inline as the assessment explains.\n- Foundation-entry rows assume the element file already exists. first element file rows add common/missing_element_file.md; projected routes never read it. Its before cost was already included in the whole shared file. A first-file route that also needs a part map dispatches update-part-map first; add the first-map route with shared files counted once, as for other following entries.\n- first_map.md is read only when writing a product's first map. Each iteration in that map counts each file once; no multiplier is charged for rereading.\n- The fact withdrawal instruction does not waive the shared steps; it is still inline. The complete withdrawal route therefore has the same file set as a complete fact-entry route. A route that stops before drafting or writing does not read those step files; the table deliberately reports completion, not an early return.\n- The author and critic both perform check.md. Only the author preparing/settling the independent critique needs prepare.md and settle.md. With no fresh critic, the author does interim checks and the collective review waits; this is not counted as a completed independent critic route.\n- A caller that has independently required the whole common workflow adds 2173 words before or {count(common)} after to a critique-only invocation, once. These are caller costs, not a requirement of critique. A projected caller additionally reads common/projected_mode.md after the change; if it has already read it, it is not counted twice. Likewise, following entries dispatched to another element add that element's files with shared files deduplicated; the table describes one entry invocation, not an unbounded chain of consequences.\n- find-foundation-entries keeps its whole common read and, for a project definition, now explicitly reads projected_mode.md. Readers of named external sections keep their section and incur no additional mode read unless their work projects an entry.\n\n## Baseline reconciliation\n\nThe seven baseline counts exactly reproduce the task: decisions 748, invariants 970, glossary 815, environment-facts 855, part-map 900, critique 766, shared workflow 2173. No discrepancy was adjusted away. The structural split reduces the normal complete routes; projected complete routes and the full author route can grow because they still need all applicable instructions plus pointers/headings. This measures file-reading cost, not a measured improvement in compliance or token carry over a session.\n''')
(REPORTS/'word-counts.md').write_text(''.join(wc),encoding='utf-8',newline='\n')
(RUN/'routes.json').write_text(json.dumps(routes,indent=2),encoding='utf-8')
print('assessment rows',len(records),'routes',len(routes))
