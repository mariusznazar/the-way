# Foundation stage — shorten the task cycle

Status: foundation stage complete and committed; foundation-only boundary, no instruction edits, tests
authored, push or later stage dispatched. Human meaning acceptance remains at request/merge.

## Inputs and authority

Worktree: C:/Storage/repos/the-way-wt/shorten-task-cycle.
Branch: task/shorten-task-cycle; clean base d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b.
Frozen task, reviewed spec, accepted plan and size report were read in full. The four accepted
rows authorize the meanings; root's provisional stage go-ahead is not human acceptance.
Used this worktree's the-way-record-decision and the-way-record-invariant entry points and
their full element skills/templates/common rules/common way of working and named examples.
Full required foundation reads completed; the initial whole-foundation search is retained in
reports/foundation-search-initial.md. No product submodule was found by either entry-point check.

## Entries and Polish meaning sentences

| Plan entry | Result | Meaning for the request |
|---|---|---|
| F1 | WAY-148/1, new decision | Pełne przekazanie pracy i raport etapu są w plikach; krótkie wiadomości prowadzą pracę, a orkiestrator czyta dowody potrzebne do rozstrzygnięcia i uzupełnia brakujący raport przed dalszą zależną pracą. |
| F2 | WAY-11/1, in-place meaning revision | Krok powrotny chroni niezmiennikiem zachowanie wymagane przez produkt, a wymienialny szczegół wykonania zostawia w zwykłych testach i opisie zmiany; wymagane niezmienniki, przyjęte ustalenia i obowiązujące wpisy projektowane nadal trzeba zapisać. |
| F3 | WAY-149/1, new decision | Pierwsze celowe złamanie testu dopisanego w kroku powrotnym następuje po niezależnej ocenie i rozstrzygnięciu uwag oraz przeglądzie ostatecznego testu; wcześniejsze testy zachowują swoje miejsce i wymagany dowód porażki. |
| F4 | WAY-136/1, in-place meaning revision | Plan rekomenduje użyteczne niezależne plasterki i pokazuje możliwość równoległej pracy, a orkiestrator osobno rozstrzyga jej wykonalność z uwzględnieniem zależności, wspólnych plików lub stanu, przeglądu i ograniczeń skilla. |
| F5 | WAY-126/1, dependency renewal only | Obowiązek zapisywania obowiązujących wpisów projektowanych pozostaje bez zmian; odwołanie wskazuje nowe brzmienie WAY-11. |
| F6 | return-step-record/1, dependency renewal only | Zmiana nadal wymaga zapisu kroku powrotnego; zdanie, wersja i niegotowa metoda pozostają bez zmian, odwołanie wskazuje nowe brzmienie WAY-11. |
| F7 | no new invariant derived; resolved below | Przegląd treści instrukcji i dowodów cyklu nie dowodzi przyszłego zachowania agentów. |

New decisions answer new questions and receive the next numbers, WAY-148 and WAY-149. Existing
pre-main entries keep /1 and Change new decision. Changed meanings carry Approved by Mariusz,
merge of <request link>; root must swap the actual request URL later. WAY-10/12/69/125 remain
byte-identical at entry level. This stage does not import the other product's game rule.

## F7 derivation and verification levels

Tried a commit-falsifiable sentence for every concrete binding clause before choosing levels:

- WAY-148: whether an agent actually supplies a complete report, reads evidence before a ruling
  or resumes without history is a fact of a run in an adopting product. Its operational
  handoff/report/record are adopter-owned outputs, not values fixed by a the-way commit. A
  commit removing a phrase or a placeholder from instructions can be identified, but a test
  matching that phrase proves neither this transfer contract nor its completeness. It would
  add an incidental format constraint that the decision does not choose. Level 2's normal,
  incomplete, failed/unchecked, disputed-evidence, resumption and assessor-boundary cases check
  the actual work and instruction meaning without claiming a commit proof of agent conduct.
- WAY-11: the existing commit-evidence obligation is already return-step-record/1, so level 1
  remains. Whether changing a discovered behavior violates the product's requirements or
  settlements needs those adopter-owned sources and a semantic judgment of that task's diff.
  No newly stated invariant of the-way follows merely from that classification. Level 2
  covers classification and discovery while explicitly preserving decision-derived
  invariants, accepted settlements and applicable projected entries.
- WAY-149: assessment/settlement/review/break order and whether evidence is for the final check
  concern the adopting cycle's execution and authors, not a property a the-way commit settles.
  Existing foundation-change-assessment-record/1 and invariant-test-break/1 remain intact;
  neither gains a new meaning or link just by this ordering choice. Semantic source/cycle
  comparison and real run evidence cover the new rule at level 2, without a phrase test or a
  new runtime scheduler or record validator.
- WAY-136: useful independence and safety of parallel work depend on the actual plan's goals,
  dependencies, files, mutable state and review ranges in the adopting product. A the-way
  commit cannot settle those facts or make the orchestrator follow its execution restriction.
  A mandatory plan heading or a redundant peer list is not the accepted meaning; no such
  structural invariant is invented. The existing level 2 remains, expanded with concrete
  opportunity, restriction, shared-state and no-useful-split examples.

This is a no-derivation finding, not an omission because Method is unknown: a derivable
sentence would require an entry even with Method TODO. Root independently confirmed this
distinction against WAY-125 and WAY-136, found no missed concrete the-way commit property and
provisionally accepted F7's resolution. No new invariant sentence, Method or check path
follows; no separate check author or deliberate break is needed for a link-only renewal.
The cost is manual semantic and cycle-evidence review; it cannot prove future agent conduct
or measured time/token savings. Existing debt is not relabeled as a pass.

## Meaning revisions for renewed human acceptance

### WAY-11/1

Old binding text:

> A task ends with its return step before its branch is merged: an agent lists from the diff and the
> task's log new rules and decisions, code behaviour with no invariant over it, environment facts the
> change rests on that the foundation does not yet hold and words whose use the glossary does not yet
> settle, writes them into the foundation in the same change, which its independent assessment covers
> (WAY-10), and compares the foundation with the code in the parts the task touched. A periodic
> review of the foundation runs apart from tasks.

New binding text:

> A task ends with its return step before its branch is merged: an agent searches the diff and the
> task's log for new rules and decisions, code behaviour with no invariant over it, environment
> facts the change rests on that the foundation does not yet hold and words whose use the glossary
> does not yet settle, writes the resulting foundation entries in the same change, which its
> independent assessment covers (WAY-10), and compares the foundation with the code in the parts
> the task touched. Uncovered code behaviour becomes an invariant when changing it in a later task
> would violate a requirement or a settled rule of the product; an implementation detail that can
> change without such a violation stays in ordinary tests and the description of the change, and
> this distinction leaves decision-derived invariants (WAY-12, WAY-22), accepted settlements
> (WAY-134) and the task's duties for projected entries (WAY-126) required. A periodic review of the
> foundation runs apart from tasks.

### WAY-136/1

Old binding text:

> Every task's cycle writes a plan with the-way's skill `plan-task`, which divides the change into
> slices and holds no code. Each slice is made by an agent of its own and then reviewed by an agent
> that did not make it, and a change of more than one slice then gets one review of the whole change,
> while the review of a plan's only slice is the review of the whole change. A slice that proves too
> large for the agent making it is discarded with its code and goes back to the planner to be split.

New binding text:

> Every task's cycle writes a plan with the-way's skill `plan-task`, which divides the change into
> slices and holds no code; the plan recommends useful slices that can be worked on and reviewed
> separately and identifies possible parallel work independently of the chosen execution skill,
> while the orchestrator records before execution whether that opportunity can be used, from
> dependencies, shared files or mutable state, separate review and the skill's restrictions. Each
> slice is made by an agent of its own and then reviewed by an agent that did not make it, and a
> change of more than one slice then gets one review of the whole change, while the review of a
> plan's only slice is the review of the whole change. A slice that proves too large for the agent
> making it is discarded with its code and goes back to the planner to be split.

## Full new and revised entries

```markdown
### WAY-148/1 — How do task-cycle stages pass their work to the orchestrator?

Every task-cycle stage passes its full handoff and report through files in the cycle's reports
directory, while its messages carry routing, stage status, paths, commits, a concise check result
and every unresolved concern affecting the next dispatch. The orchestrator records the event and
relevant choices before dependent dispatch and reads authoritative sources and relevant report
evidence before deciding a question, settling a finding, accepting a foundation meaning or
verifying disputed or incomplete evidence; routine progression uses the short return, record,
source paths and commits without requiring prior conversational history. A missing or incomplete
report is repaired before dependent work proceeds, and this transfer contract preserves required
whole-source reads, check and review duties and the independent assessor's filtered inputs
(WAY-10), reusing a borrowed method's existing brief and report rather than duplicating them.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-125@441e3a6a · derives from WAY-10@db68de1c
- **Verification:** level 2 — an agent compares the stage handoff, return, report and
  orchestrator's ruling with the decision:
  - complies: a short return names its complete report, commit range and failed or unchecked
    checks, and the record permits resumption from files; the orchestrator reads the evidence
    of an unresolved question before deciding it; a missing report is repaired before the next
    dependent dispatch; a required whole entry is read whole;
  - violates: a full report exists only in conversation, a short return conceals a failed check,
    dependent work proceeds on a missing report or mismatched commit range, or a question is
    settled from the short return alone; a selective read replaces a mandatory whole-source
    read; the independent assessor receives the operational handoff or author's reasoning.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* full material kept outside routine coordination avoids repeated context while
preserving evidence a ruling needs and a place from which work can resume. Short returns make
the next action visible, but an omitted failure can hide behind brevity, so relevant evidence
remains part of a decision and an incomplete report blocks dependent work.
*Rejected:* full handoffs and reports repeated in messages — coordination accumulates material
it need not reread; short summaries as the only record — lost evidence cannot be recovered on
resumption; a second universal brief and report contract — duplicated obligations drift without
proving completeness; automatic compaction — it does not choose the evidence a ruling needs.
```

```markdown
### WAY-11/1 — How does a task end?

A task ends with its return step before its branch is merged: an agent searches the diff and the
task's log for new rules and decisions, code behaviour with no invariant over it, environment
facts the change rests on that the foundation does not yet hold and words whose use the glossary
does not yet settle, writes the resulting foundation entries in the same change, which its
independent assessment covers (WAY-10), and compares the foundation with the code in the parts
the task touched. Uncovered code behaviour becomes an invariant when changing it in a later task
would violate a requirement or a settled rule of the product; an implementation detail that can
change without such a violation stays in ordinary tests and the description of the change, and
this distinction leaves decision-derived invariants (WAY-12, WAY-22), accepted settlements
(WAY-134) and the task's duties for projected entries (WAY-126) required. A periodic review of the
foundation runs apart from tasks.

- **Change:** new decision
- **Scope:** decisions, invariants, glossary, part-map, environment-facts, task-cycle
- **Based on:** none
- **Relations:** derives from WAY-01@60960941
- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step
  finds and how it classifies uncovered behaviour — an agent compares the diff, the task's log
  and sources with the decision:
  - complies: a newly found rule that a later change would break becomes an invariant, with its
    requirement or settlement named; a replaceable layout calculation stays in ordinary tests
    and the change description, with the reason recorded; an invariant required by a decision
    is written even when its check costs work; accepted settlements and applicable projected
    entries are written;
  - violates: a product rule is left only in ordinary tests; every replaceable detail becomes
    a foundation invariant merely because the diff reveals it; a costly decision-derived
    invariant or an applicable accepted or projected entry is omitted under the distinction.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* some of the foundation is learned only in implementation and in use, and a task that
missed the foundation does not report it; an end step goes missing, so the merge waits for its
record. Facts and words are listed because, like rules, they are learned in code.
*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
in the code; every uncovered detail made an invariant — a replaceable implementation becomes a
product rule; ordinary tests alone for product rules — later work can change a requirement without
meeting a foundation check.
```

```markdown
### WAY-149/1 — When does the deliberate break of a return-step check take place?

For an invariant check added in a task's return step, its first acceptance deliberate break
follows the one independent assessment of the change's foundation entries and invariant tests
and the settlement of its remarks. Before that break, affected checks and code review run again
for a settlement that changes code, assessed foundation entries or invariant tests, and the code
reviewer who did not write the check reviews its final version, writes the break from the final
invariant sentence and records the required failure (WAY-08, WAY-69); later corrections to the
check or the behaviour its break covers repeat the affected verification before the final clean
run. Checks written earlier in the cycle retain their existing acceptance and deliberate-break
points, and settlement stays part of the one assessment (WAY-10), with an existing affected
review reused where it covers the final check rather than adding a whole-change review of an
unchanged range.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** derives from WAY-10@db68de1c · derives from WAY-08@2343e09f · derives from
  WAY-69@7051f884
- **Verification:** level 2 — an agent compares the cycle's check, assessment, settlement,
  review and deliberate-break evidence with the decision:
  - complies: a return-step check runs on the product, its assessment's remarks are settled,
    affected checks and review run again, and the code reviewer reviews the final check and
    records its failure on a break written from the final sentence; an earlier check keeps its
    original acceptance point; a later correction repeats the affected evidence;
  - violates: a return-step check is accepted on a break before assessment, or on a passing
    product run alone; a changed final check uses a superseded break's evidence; assessment
    replaces code review, settlement reopens assessment, or an earlier check's break is delayed
    to the return step.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* settling assessment remarks before the first acceptance break avoids repeating a
break for a check the settlement changes. A final check still needs independent review and a
real failure on the rule it protects; changing the order cannot turn a product pass or an
assessment into that evidence. Earlier checks keep the failure evidence their own stage needs.
*Rejected:* breaks both before and after assessment by default — the earlier run may check a
version that is immediately replaced; delaying every check's break — earlier stages lose their
own acceptance evidence; accepting a check after assessment alone — an approved check may still
detect no break; a second whole-change review of unchanged work — it repeats an existing review.
```

```markdown
### WAY-136/1 — What plan does a task's cycle write, and who makes and reviews its slices?

Every task's cycle writes a plan with the-way's skill `plan-task`, which divides the change into
slices and holds no code; the plan recommends useful slices that can be worked on and reviewed
separately and identifies possible parallel work independently of the chosen execution skill,
while the orchestrator records before execution whether that opportunity can be used, from
dependencies, shared files or mutable state, separate review and the skill's restrictions. Each
slice is made by an agent of its own and then reviewed by an agent that did not make it, and a
change of more than one slice then gets one review of the whole change, while the review of a
plan's only slice is the review of the whole change. A slice that proves too large for the agent
making it is discarded with its code and goes back to the planner to be split.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** observation of installed Superpowers 6.4.1 on 2026-10-10 using `sed -n` and
  `grep -n` in Git Bash on Microsoft Windows NT 10.0.26300.0; source root
  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`:
  `writing-plans/SKILL.md` — "Each step is one action (2-5 minutes)" and, under "No
  Placeholders", "Steps that describe what to do without showing how (code blocks required for
  code steps)"
- **Relations:** derives from WAY-13@e6c830b7
- **Verification:** level 2 — an agent compares the plan and cycle with the decision:
  - complies: a one-line fix has one useful slice and its review is the only whole-change code
    review; a change of several slices has each slice reviewed and then one whole-change review;
    an outgrown slice is discarded and split; a plan identifies independent slices although
    the execution skill forbids parallel executors, and the orchestrator records sequential
    execution with that restriction; shared mutable state prevents a proposed parallel run;
  - violates: a task has no plan, or a plan holds code or uses Superpowers `writing-plans`; an
    author reviews its own slice, a one-slice change gets a duplicate whole-change review, or
    outgrown code is kept; the planner suppresses useful independent slices because of the
    execution skill, or creates unnecessary slices to claim parallel work; the orchestrator
    treats different files alone as proof of independence or overrides the skill's restriction.
- **Review when:** five cycles of `implement-task` have run under this decision, or a cycle has
  returned more than one slice in three of its plan as too large, or has used, as
  `task-cycle/cycle_stages.py` counts them, no clearly fewer tokens than the 363.7 million that
  the cycle of https://github.com/mariusznazar/the-way/pull/11 used, for a task of like size ·
  check by: 2026-11-30
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* a plan earns its cost by dividing the change, so that a narrow agent makes each slice
and a narrow reviewer reads it, which is where reviews catch the errors that matter; code written
out ahead in the plan is most of a plan's cost and catches nothing a review of the code does not. A
plan without code costs little, so every task gets one, and its form can change in its own skill
apart from the cycle. A small change is a plan of one slice, so one path holds every task, and its
one review reads the whole change. A useful division of work outlives the restrictions of one
execution method, while the execution ruling keeps the recommendation from becoming permission
for work whose dependencies or shared state make it unsafe.
*Rejected:* Superpowers `writing-plans` — each step carries its code, so the plan costs a large
share of the change and still needs the review of that code; a separate path for small tasks
without a plan — two paths would hold the same rules of the record, the request and the return
step, while size only lightens one process (WAY-13); a review of the whole change after the review
of a plan's only slice — it reads the same range twice; an outgrown slice's code kept and completed
— its split would be written around partial code; a plan shaped only by the restrictions of
one execution method — it hides useful independent work; parallel execution from different file
names alone — shared state and dependencies can still join the work.
```

## Choices and costs

- Use the accepted requirement/settlement boundary. Keeping the broad uncovered-behavior
  wording would preserve avoidable foundation work and fail row 2; narrowing it risks a wrong
  classification, so the evidence must name the requirement/settlement or replacement reason.
- Preserve required invariants and all existing authorship, assessment and check duties.
  Dropping an expensive invariant would reduce work but contradict the accepted meaning and
  WAY-12; the cost of the chosen boundary is that required checks remain required.
- Put the first acceptance break of return-step checks after assessment settlements. Keeping
  its earlier point repeats obsolete checks after corrections; moving all breaks would remove
  earlier acceptance evidence. Final-version review and reruns after later corrections remain.
- Recommend independent work separately from execution permission. Suppressing it loses useful
  planning information; automatic parallel execution risks conflicts or violates the chosen
  skill. The orchestrator must judge the actual plan and record the execution ruling.
- Reuse the existing record and briefs/reports. A universal schema/validator adds a maintained
  interface and proves presence only; the selected contract costs manual evidence review.

## Search, fingerprints and checks

Initial search: reports/foundation-search-initial.md, with populations, queries, full results
and every finding's disposition. Search against the current integration tip and the one
independent foundation assessment remain root-owned later obligations; this author did not
dispatch another assessor or treat the initial search as the pre-integration search.

Final binding fingerprints, computed with relation-model/fingerprint.py:

- WAY-11: e882a9df
- WAY-136: e9ca5dac
- WAY-148: 2a5f9057
- WAY-149: 6c02ef48

Changed files: foundations/decisions.md and foundations/invariants.md only.

## Executed checks and limitations

Full command output and exits are in reports/foundation-checks.md; machine-readable guard/test
records are alongside it as foundation-decisions.jsonl, foundation-invariants.jsonl,
foundation-decisions-tests.jsonl, foundation-invariants-tests.jsonl and foundation-gate-tests.jsonl.
Every executed check below exited 0. Interpreter: Python 3.14.3.

| Check | Result |
|---|---|
| decision element tests | 169 pass |
| invariant element tests | 233 pass |
| gate tests, including current critical-flow tests | 98 pass |
| decision format guard, --base none --merge-onto none | 0 errors; 9 warnings; 5 unchecked from none options (2 base, 3 merge) |
| invariant format guard, --base none --merge-onto none | 0 errors; 0 warnings; 3 unchecked from none options (1 base, 2 merge) |
| direct final fingerprints through relation-model/fingerprint.py | every affected reference matches; final values and relation targets in reports/foundation-fingerprints.md |
| git diff --check | no whitespace errors |
| newline/control-character inspection in foundation_write.py | original CRLF retained in both existing files; no control characters except tab/CR/LF |

The five existing overdue-review warnings individually concern WAY-03, WAY-21, WAY-52, WAY-55 and
WAY-69, each with check-by date 2026-10-02 and no review record. No unrelated review was reopened or
silently postponed. The four new placeholder warnings individually concern WAY-11, WAY-136,
WAY-148 and WAY-149; root must replace their request-link placeholders once the request exists.
No other guard unchecked line exists. The invariant guard's note that human_verdicts.md is absent
means no human verdict was given; this stage invents none.

return-step-record/1 retains Method TODO and therefore has no runnable pass in this stage.
The none-mode guards leave 8 checks unchecked in total; their exit 0 does not establish the
omitted comparisons. The separately run fingerprint helper verifies the actual final binding
text and every affected dependency, including WAY-126 and return-step-record, and all relation
targets retained or introduced by the changed decisions. No invariant check or product test was
written; the existing invariant's sentence/version/method are unchanged.

## Boundary and remaining work

No unresolved foundation authoring question remains. Root read the actual two-file diff and
confirmed it preserves the four accepted meanings without a further conflict. This is not the
independent foundation assessment or human acceptance. Before dependent dispatch root refreshes
plan identifiers/ranges and size, then owns the later instruction slice, source/case review,
single independent assessment, integration-tip foundation search and reviewable request. The
current cycle keeps its base process's acceptance order.

Changed foundation entries are WAY-148/1, WAY-11/1, WAY-149/1, WAY-136/1, WAY-126/1 and
return-step-record/1. Only foundations/decisions.md and foundations/invariants.md belong in this
stage's commit. Reports stay ignored for the root's later archive; transient editing/fingerprint
.py helpers are not product implementation and root omits them from that archive.

Commit: dba4cf81769446484d68b6260424260f7f1da85e — feat(task-cycle): Record the shorter cycle contracts.
The commit stages exactly foundations/decisions.md and foundations/invariants.md, includes the
initial foundation-search record in its message, and was not pushed. Working tree is clean
after it. The one later assessment and integration-tip search remain root-owned requirements.
