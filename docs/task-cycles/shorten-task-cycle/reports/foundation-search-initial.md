# Initial whole-foundation search — shorten the task cycle

Worktree: C:/Storage/repos/the-way-wt/shorten-task-cycle.
Input foundation: d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b, clean before drafting.
Population: all six files returned by `rg --files foundations`: decisions.md, invariants.md,
part_map.md, glossary.md, environment_facts.md and violated_invariants.md.
Full reads: decision log, invariants, part map and glossary; every relevant decision's full
entry including Rejected, and both elements' full templates, common rules, common way of
working, skills and named examples. Environment facts were searched across their full file;
the changes adopt no new outside fact and no invariant condition from one.

## Findings and disposition

- Written WAY-11 dependency: WAY-126 derives from it; its projected-entry duties remain
  applicable under the requirement/settlement criterion. Renew its fingerprint only.
- Written WAY-11 dependency: return-step-record/1 still requires the return record before
  integration; retain sentence, Method TODO and version 1, renewing Derives from only.
- No entry carries WAY-136's fingerprint. Its existing author/reviewer, final-review and
  outgrown-slice duties stay intact in the in-place edit.
- WAY-01/03/07/14/30/31/33/114/134 govern route, authoring, renewed meaning acceptance and
  dependencies; apply the accepted rows without claiming human acceptance or inventing a
  pre-main version. New numbers follow WAY-147: WAY-148 and WAY-149.
- WAY-08/10/12/22/57/61/63/69 retain real failure evidence, independent filtered assessment,
  derivation, separate authors, final-version evidence and disclosure of unchecked work.
  No further meaning revision or narrowing is needed.
- WAY-125 retains adopted Superpowers 6.4.1 and report preservation; the new transfer decision
  derives from it and WAY-10. WAY-135 retains spec/plan and discard boundaries; no whole-source
  read is weakened. WAY-136's execution ruling respects the skill's restrictions.
- WAY-126/134 still require applicable projected entries and accepted settlements; WAY-28's
  human choice of recovered existing behavior is untouched. The task's adjacent-tile example
  is not a the-way product rule.
- WAY-36 keeps this work's temporary choices out of the log; all four rows bind future cycles.
  WAY-144 applies to project tasks, not slices; no duplicate parallel-peer list is introduced.
- WAY-27 keeps private task sources out of foundation Origin; full reasoning is in the
  entries, with Origin none. Rationale/motive is not an environment fact or measured saving.
- WAY-95/97/99: return step, foundation step, invariant test, slice, result and verdict retain
  their glossary meanings. Handoff and report use ordinary field meanings; no new glossary
  meaning or duplicated definition follows. No words from Avoid are introduced.
- WAY-37: the change brings no missing guard, full gate, run-evidence method or other mechanism
  a waiting foundation entry needs. In particular return-step-record's TODO is not resolved by
  editing prose, and no full gate is claimed.
- Part map: existing task-cycle/** and foundation paths cover the work. No responsibility,
  critical flow, surface, trust boundary or detection entry changes. The listed
  surface-promise-level/1 debt remains unrelated.

## Search commands and full results

Case-insensitive whole-foundation searches below support the full reads rather than replacing
them. Positive controls include the actual WAY-11 relation in WAY-126 and return-step-record's
Derives from; each is an actual dependent entry, not a source quotation. Results were captured
without a result limit; rg exit 1 would mean no matches, not a tool failure.

### written dependencies

`rg -n -i 'WAY-(11|136)@|return-step-record' foundations`

Exit: 0; matching lines: 4.

```text
foundations\invariants.md:216:## return-step-record/1
foundations\invariants.md:222:- **Derives from:** WAY-11@16d55adb
foundations\decisions.md:356:- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step finds
foundations\decisions.md:3649:- **Relations:** derives from WAY-01@60960941 · derives from WAY-11@16d55adb · derives from
```

### handoff and evidence

`rg -n -i 'handoff|report|resum|context|chronicle|reasoning|dispatch' foundations`

Exit: 0; matching lines: 110.

```text
foundations\part_map.md:6:reports that graph, the comparison is unchecked.
foundations\part_map.md:155:  - the gate reports a check as passed although it never ran — a change that breaks an invariant
foundations\part_map.md:218:  - the check script reports a sound instruction file as broken, or a defect at a level above or
foundations\part_map.md:227:    directories it was given, hang or stop without a report — a user's credentials can leave the
foundations\part_map.md:259:carrying its old fingerprint is reported before the change reaches the main branch.
foundations\part_map.md:269:session on the-way would not find under its `the-way-` name is reported before the change reaches
foundations\part_map.md:354:## External context
foundations\glossary.md:177:A result is the value reported for an entry on one commit: the verdict that counts for it there, or a value of its template's closed list standing in place of one.
foundations\environment_facts.md:102:## context-file-effect/1
foundations\environment_facts.md:104:Providing context files to coding agents does not generally improve their task success rates while increasing inference cost by over 20% on average, and the agents follow the instructions in those files well while repository overviews in them do not help.
foundations\environment_facts.md:107:- **Source:** https://arxiv.org/abs/2602.11988v3 § Abstract — "Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average." · § Abstract — "Specifically, we find that while instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful."; read 2026-09-30 · https://arxiv.org/html/2602.11988v3 § 4.1 — "We consider four coding agents, paired with suitable models: Claude Code [3] with Sonnet-4.5 [5], Codex [26] with GPT-5.2 and GPT-5.1 mini [32], and Qwen Code [28] with Qwen3-30b-coder [34]."; read 2026-09-30
foundations\environment_facts.md:108:- **Method:** `python -B gate/run_tests.py probes/context-file-effect --record .runs/fact-context-file-effect.jsonl`
foundations\environment_facts.md:200:Claude Code expands a file that a `CLAUDE.md` imports with `@path/to/import` syntax and loads it into context at launch alongside that `CLAUDE.md`, and skips Markdown code spans and fenced code blocks when it parses imports.
foundations\environment_facts.md:203:- **Source:** https://code.claude.com/docs/en/memory (archived: http://web.archive.org/web/20261007150822/https://code.claude.com/docs/en/memory, 2026-10-07) § Import additional files — "CLAUDE.md files can import additional files using @path/to/import syntax." · § Import additional files — "Imported files are expanded and loaded into context at launch alongside the CLAUDE.md that references them." · § Import additional files — "Import parsing skips Markdown code spans and fenced code blocks."; read 2026-10-08
foundations\environment_facts.md:235:- **Source:** https://arxiv.org/abs/2605.10039v1 § Abstract — "Practitioners assume that structural choices (file size, instruction position, file architecture, contradictions in adjacent files) measurably affect adherence." · § Abstract — "We report a systematic factorial study of these choices using four manipulated variables, measuring compliance with a trivial target annotation across 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported descriptively under a CLI-version confound), and five coding tasks." · § Abstract — "None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction." · § Abstract — "The largest effect we measured is within-session: each additional function the agent generates is associated with approximately 5.6% lower odds of compliance per step (OR = 0.944) within the session-length range we tested, though the relationship is non-monotonic rather than a constant per-step effect."; read 2026-10-08
foundations\invariants.md:8:The decision guard, given "{merge-onto}", reports every `derives from` or `narrows` relation, in the latest version of a decision in the log a merge onto that commit leaves, whose fingerprint differs from the current fingerprint there of the decision it names.
foundations\invariants.md:579:The map guard reports a check whose declared command the product lacks as unchecked, never as agreement.
foundations\invariants.md:797:## map-guard-dependency-report/1
foundations\invariants.md:807:## criticality-lowering-report/1
foundations\invariants.md:809:The map guard, given "{fork-point}", reports every part whose computed criticality is lower than on that commit.
foundations\invariants.md:829:The map guard reports a critical flow whose test leaves no coverage file as "list of parts unchecked", never as agreeing with the map.
foundations\invariants.md:849:Every exchange with the external context in the part map records its direction, whether what comes in is trusted, and whether the partner updates together with the product.
foundations\invariants.md:1109:For every invariant entry whose sentence a change adds or alters against "{fork-point}", the gate's report states whether the entry's method passes on "{fork-point}" and fails there on a deliberate break, or that this could not be checked.
foundations\invariants.md:1159:For every invariant whose command a run of the gate carried out, the gate's report shows the verdict that run recorded for the entry's identifier and current version, and `pass` only where every check of that run citing the entry recorded `pass`.
foundations\invariants.md:1169:The gate reports no pass for an invariant for which neither a run of its command recorded a verdict nor a human verdict for it is in force.
foundations\invariants.md:1219:Every result the gate reports for an invariant is `pass`, `fail`, `unchecked` or `error`.
foundations\invariants.md:1229:Every `unchecked` the gate reports names a reason on the list in the invariants template.
foundations\invariants.md:1239:The gate reports an invariant whose command runs, under a Python interpreter, a script that does not exist on the commit being checked `unchecked` for want of a declared or produced command where that script does not exist on "{fork-point}" either, and `error` where it exists there.
foundations\invariants.md:1247:## gate-reported-set/1
foundations\invariants.md:1249:The gate reports a result for every invariant a change against "{fork-point}" reaches, and for every invariant a critical flow names.
foundations\invariants.md:1269:The gate's command exits non-zero when some result it reports is `error`, an invariant on the list of violated invariants results `pass`, an invariant off that list or an environment fact results `fail`, or a run records a failure for no entry, and zero otherwise.
foundations\invariants.md:1409:The gate reports a quarantined entry `unchecked` while the checked commit's committer date is no later than its end date, and `error` after.
foundations\invariants.md:1849:The glossary guard, given a product's glossary, reports as an error every entry there whose term,
foundations\invariants.md:1921:For every entry of `foundations/glossary.md` whose definition differs from its definition on "{fork-point}", the glossary guard's report lists the uses of its term.
foundations\decisions.md:167:reasons they are given, so what binds stays short and checkable, reasoning below; a field
foundations\decisions.md:172:entry — no reasoning beside the rule; "will" or "should" — an intent, not a state; capitals such as
foundations\decisions.md:309:assesses without the task's chronicle or the author's reasoning and names what of the change can be
foundations\decisions.md:322:  - complies: one assessor on another model reads the diff without the author's reasoning, and the
foundations\decisions.md:325:  - violates: the assessor receives the author's reasoning; the author drops a remark without
foundations\decisions.md:334:reasoning; one such reader finds what a reader can, and the human who accepts at the merge reads the
foundations\decisions.md:360:  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
foundations\decisions.md:367:missed the foundation does not report it; an end step goes missing, so the merge waits for its
foundations\decisions.md:751:### WAY-27/1 — Where may this repository point for its reasoning?
foundations\decisions.md:754:entry carries its whole reasoning, and what is seen only in such a source is described in the
foundations\decisions.md:763:- **Verification:** level 1 — invariants: outbound-link-reach. Level 2 for the reasoning in the
foundations\decisions.md:776:to name. A backlog place is where work is kept, not reasoning an entry rests on, and WAY-107 sends
foundations\decisions.md:779:*Rejected:* *Origin* pointing to the notes where the reasoning was worked out — no reader can open
foundations\decisions.md:1090:through an adapter for the format. Where a product declares no such command, the script reports
foundations\decisions.md:1259:- **Verification:** level 1 — invariants: flow-part-names · flow-invariant-link · gate-reported-set
foundations\decisions.md:1291:  part-criticality-field · map-guard-unrecorded-criticality · map-guard-dependency-report ·
foundations\decisions.md:1292:  criticality-lowering-report. Level 2 for an obligation from outside — an agent compares the
foundations\decisions.md:1317:coverage file, the script reads it, finds the parts the files it names belong to and reports
foundations\decisions.md:1318:every part the flow's list does not hold. A flow whose test leaves no coverage file is reported as
foundations\decisions.md:1344:accept data the product does not trust; an exchange with the external context records its
foundations\decisions.md:1377:that never updates; an exchange with the external context records whether the partner updates
foundations\decisions.md:1457:- **Based on:** context-file-effect@c44e5ef0 · claude-code-path-rules@ac99f128
foundations\decisions.md:1461:- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
foundations\decisions.md:1466:*Rationale:* agents follow instructions in context files, while repository overviews have not
foundations\decisions.md:1469:*Rejected:* an overview for agents — added context cost without measured benefit; rule files
foundations\decisions.md:1535:gate runs and what follows from what it reports belong to the task cycle, not to this part.
foundations\decisions.md:1643:gate reports whether its method passes on the commit the task branch left the main branch from and
foundations\decisions.md:1645:that report in front of them.
foundations\decisions.md:1654:  it with the gate's report in front of them, and the record of that decision names who and when.
foundations\decisions.md:1801:### WAY-63/1 — What results does the gate report for invariants, and which make its command fail?
foundations\decisions.md:1804:template's closed list, or `error` otherwise. The gate reports a result for at least every invariant
foundations\decisions.md:1806:a result it reports is `error`, a listed invariant's is `pass`, an unlisted invariant's or a fact's
foundations\decisions.md:1815:  gate-unchecked-reason · gate-reported-set · gate-exit-code. Level 2 for the reasons — an agent
foundations\decisions.md:1820:  - violates: a guard whose call to git fails reports `unchecked`; a human's `pass` stays in force
foundations\decisions.md:1985:*Method*, and in an invariant's *Rests on* until the facts element has entries. A guard reports a
foundations\decisions.md:2040:no entries — word checks go silent on other languages; a guard reporting other languages unchecked
foundations\decisions.md:2061:  - violates: an invariant rests on the report of a past failure its decision quotes; an invariant
foundations\decisions.md:2092:  Level 2 for the report beside the record — an agent compares the change with the decision:
foundations\decisions.md:2094:    prints its report for a person;
foundations\decisions.md:2095:  - violates: a guard writes its verdicts only into its report.
foundations\decisions.md:2106:(WAY-61); the run's output as the record — a person loses the guard's report; `pass` and `fail`
foundations\decisions.md:2136:*Rejected:* git's pattern rule and what `git check-attr` reports in one entry — the second is about
foundations\decisions.md:2519:context as linked facts — a new link with no known consumer.
foundations\decisions.md:2676:place of the word in every use the guard lists and every other form it finds, and reports each use
foundations\decisions.md:2687:    reports that none moves; after the main branch, a second sense of "gate" takes a new word; "The
foundations\decisions.md:2915:beside it and reported as a warning rather than an error — one word carries two meanings in the
foundations\decisions.md:2926:### WAY-105/1 — Which check reports an invariant whose command runs a script that does not exist, and how is that script read?
foundations\decisions.md:2929:`python3`, `python3.<minor>` or `py`, with or without `.exe` — reports the entry `unchecked` for
foundations\decisions.md:2971:template allows, and every one reaches a human; nobody reporting it — a method with a wrong path
foundations\decisions.md:3053:fixed structural words let later work resume and check the document. A written state and
foundations\decisions.md:3103:deriving a deadline from background material — it mistakes context for a settlement.
foundations\decisions.md:3130:### WAY-112/1 — How does an agent develop and resume a project definition?
foundations\decisions.md:3138:question; work resumes from that line and, while entries are being found, from the candidate table.
foundations\decisions.md:3146:    its new status before continuing; a later agent resumes from the recorded open section;
foundations\decisions.md:3154:answer makes the document a reliable place to resume. Source-anchored challenges can change an
foundations\decisions.md:3190:*Rejected:* a panel of options separate from the conversation — its context is detached from the
foundations\decisions.md:3250:resume, and a final line shows that the search occurred even when it yields no entry.
foundations\decisions.md:3309:look checked before the product exists; leaving the human's reasoning to later tasks — they
foundations\decisions.md:3390:  - complies: one fresh critic receives a finished set and its sources, reports evidence for each
foundations\decisions.md:3447:report of its own. An option the project's code is written in or against — a language, a
foundations\decisions.md:3480:project needs. Research of independent choices run side by side and kept in reports lets the
foundations\decisions.md:3575:*Rationale:* a project can inform a task without owning it; the handoff must show which relationship
foundations\decisions.md:3593:keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment
foundations\decisions.md:3609:  `requesting-code-review/SKILL.md` — "The reviewer gets precisely crafted context for evaluation —
foundations\decisions.md:3750:- **Based on:** context-file-effect@c44e5ef0 · claude-code-path-rules@ac99f128 ·
foundations\decisions.md:3759:- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
foundations\decisions.md:3764:*Rationale:* a line loaded into every session costs context in each, and agents carry out what it
foundations\decisions.md:3773:given line is needed, even where a shorter file saves context in every session; a file of pointers
foundations\decisions.md:3816:- **Based on:** https://arxiv.org/html/2511.12884v2 § 4.2.3 — "The evolution of Agent context files
foundations\decisions.md:4003:meets an open design choice while it makes the change returns a report that holds no code, the
foundations\decisions.md:4005:the report writes the spec, from which the plan is written again.
foundations\decisions.md:4017:    carry returns a report without code, the branch goes back to its base, and a fresh agent writes
foundations\decisions.md:4037:agent designs from the task and the report.
foundations\decisions.md:4118:*Rationale:* an agent writes the deployment for a place to run and reads what it reports, yet a
foundations\decisions.md:4295:so the installer reports a missing import before confirmation and leaves the file to its owner.
foundations\decisions.md:4486:    another task than the definition names with no line in the log, while the script reports a
```

### return classification and preserved duties

`rg -n -i 'return step|behaviour|behavior|requirement|settlement|projected|uncovered' foundations`

Exit: 0; matching lines: 119.

```text
foundations\glossary.md:86:The foundation step is the step of a task in which the task writes the change of the foundation it sets out to make, as against what its return step carries back.
foundations\glossary.md:156:A probe is a check of an environment fact that tries out the behaviour the fact states.
foundations\glossary.md:182:## return step
foundations\glossary.md:184:The return step is the step of a task that carries back to the foundation what the task's change holds and the foundation does not yet say.
foundations\part_map.md:90:  - the entry finder omits a settlement that a later task must guess — a project can pass its gate
foundations\part_map.md:91:    with an incomplete projected foundation — high — not detected
foundations\part_map.md:101:uses its settlements as a source, or stands on its own.
foundations\part_map.md:109:  - an agent fills a missing human answer with a plausible settlement — tasks inherit an invented
foundations\part_map.md:121:  - the plan check accepts a plan in which a projected entry has no task writing it, or two — the
foundations\part_map.md:221:  - the account of how the tools load instruction files states a behaviour a tool no longer has —
foundations\environment_facts.md:128:With the hidden test oracle in their loop, the two Copilot CLI agents the study ran reach a near-perfect score from a demo holding the tested behaviour directly, leaving the requested library dead or absent.
foundations\environment_facts.md:131:- **Source:** https://arxiv.org/abs/2606.28430v1 § Abstract — "In a controlled code-as-spec setup, two production Copilot CLI agents (claude-opus-4.7, gpt-5.5) re-implement a React Fluent-UI data table in Angular as a reusable library under a hidden 222-test Playwright oracle across 18 runs and three oracle-availability conditions." · § Abstract — "With the oracle in the loop, the score reaches near-perfect, but from a demo holding the tested behavior directly, the library left dead or absent."; read 2026-09-26 · https://arxiv.org/html/2606.28430v1 § 2 — "We study GitHub Copilot CLI (version 1.0.56) under two model configurations"; read 2026-09-26
foundations\invariants.md:218:Where {merge-onto} exists, every change against {fork-point} holds, in one of its commits, the record of its task's return step.
foundations\invariants.md:2023:Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds.
foundations\invariants.md:2050:The project plan check rejects a plan in which a projected entry of its definition has no task
foundations\invariants.md:2056:names a task, a projected entry, an In scope item or an open question that the plan or its
foundations\invariants.md:2110:| foundation-change-panel-record | replaced: the record of a panel of two assessors and two settlements became the record of one independent assessment and of how each remark was settled | foundation-change-assessment-record |
foundations\decisions.md:129:field of a part), the agent's environment and the return step (the task cycle); external
foundations\decisions.md:135:code alone — behaviour shows in runtime traces, deployment in infrastructure files.
foundations\decisions.md:310:cut, or that nothing can. The author settles each of its remarks and records how, and a settlement
foundations\decisions.md:312:does not reopen its assessment. A human accepts the change, with the assessment and its settlement,
foundations\decisions.md:323:    author records how each remark was settled before the merge; a settlement that rewrites an
foundations\decisions.md:326:    recording why; a change merges with no assessment record; the edits of a settlement are sent
foundations\decisions.md:339:the author assessing its own change — it checks itself; assessing again every settlement that
foundations\decisions.md:345:A task ends with its return step before its branch is merged: an agent lists from the diff and the
foundations\decisions.md:346:task's log new rules and decisions, code behaviour with no invariant over it, environment facts the
foundations\decisions.md:356:- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step finds
foundations\decisions.md:360:  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
foundations\decisions.md:788:which of it the product must keep — and the other invariants come through the return step of
foundations\decisions.md:952:    finds an unlinked requirement that players log in;
foundations\decisions.md:1640:behaviour or calls for a different one, or reads `nothing`; a place that only cites another is
foundations\decisions.md:1670:places, never reasons (WAY-22), and to those against the behaviour too, which a human weighing it
foundations\decisions.md:1677:decision" — it repeats WAY-17's link; an outside catalogue's requirement as a field — it is a fact,
foundations\decisions.md:2261:file a human re-reads the source against, or `TODO`; a command probes the behaviour the sentence
foundations\decisions.md:2280:  - violates: a probe asks `git --version` and compares the number in place of the behaviour; a
foundations\decisions.md:2285:    `description`; it fails the fact where the behaviour differs and leaves it `unchecked` where it
foundations\decisions.md:2289:    about the behaviour; it writes the release under a key of its own beside `description`.
foundations\decisions.md:2298:place of the behaviour — it trusts the label; the runner's configuration or the tool's release as
foundations\decisions.md:2425:### WAY-86/1 — How does a catalogue of requirements or a binding rule reach a product?
foundations\decisions.md:2427:A voluntary catalogue of requirements binds a product only through a decision adopting it that
foundations\decisions.md:2429:requirement an invariant takes a condition from is an environment fact. A binding rule — a law,
foundations\decisions.md:2432:that notices a likeness to a requirement nothing has adopted or applied asks a human.
foundations\decisions.md:2440:    invariant taking a criterion's condition rests on that requirement's environment fact; the
foundations\decisions.md:2443:  - violates: an agent writes an invariant from an ASVS requirement because the code looks like
foundations\decisions.md:2455:takes on a binding rule (WAY-05); a script matching adopted requirements to facts and invariants —
foundations\decisions.md:2493:or models, the behaviour of a tool the process uses. A fact named there carries its fingerprint, as
foundations\decisions.md:2979:projected foundation entries, while the project plan holds phases, task order and which task
foundations\decisions.md:2980:realizes or writes each projected entry.
foundations\decisions.md:2989:    projected entries to tasks before the breakdown has made those tasks.
foundations\decisions.md:2997:*Rejected:* putting projected entries into the foundation at the readiness gate — it would describe
foundations\decisions.md:3031:status values, markers read by the readiness check and projected foundation entries keep their
foundations\decisions.md:3035:stays as `TODO` in the section or projected entry that needs it, or as an open question naming
foundations\decisions.md:3061:the agent anchors questions and is not silently adopted as a settlement. Every success signal
foundations\decisions.md:3103:deriving a deadline from background material — it mistakes context for a settlement.
foundations\decisions.md:3200:it at the merge of the change that holds it, or, for a projected entry, at the readiness gate. Before
foundations\decisions.md:3228:complete candidate table with each proposed settlement, its kind, its source and the concrete
foundations\decisions.md:3248:*Rationale:* the source distinguishes a human settlement from material offered for consideration;
foundations\decisions.md:3258:before the breakdown, and environment facts only where a projected decision or invariant rests on
foundations\decisions.md:3271:    projected entry depending on it.
foundations\decisions.md:3285:The skill of each entry's kind writes its whole proposal under the definition's `Projected
foundations\decisions.md:3286:foundation changes`, in that kind's subsection with the template's projected heading and one
foundations\decisions.md:3288:new projected decision uses `(new)` without a number or prefix, while versions and other kinds
foundations\decisions.md:3289:use the identifiers their templates give; an entry following from it remains projected or becomes
foundations\decisions.md:3300:  - violates: a projected proposal is written directly into the foundation, or a decision's
foundations\decisions.md:3316:human-given part of a projected entry: its binding sentence or definition and a decision's
foundations\decisions.md:3318:and only projected fields awaiting code or the world, including an expressly deferred
foundations\decisions.md:3321:human approves the whole projected entries with permitted `TODO`; the gate record then names the
foundations\decisions.md:3323:Goal through Projected foundation changes. A change to those sections after approval goes through
foundations\decisions.md:3346:### WAY-119/1 — When may a projected decision leave Review when unresolved at the gate?
foundations\decisions.md:3348:At the readiness gate, a projected decision's *Review when* holds a review condition and date, or
foundations\decisions.md:3392:  - violates: one critic is run per row of a set, the author silently changes a human settlement,
foundations\decisions.md:3402:review; letting the critic's remarks edit human settlements without asking — it would disguise a
foundations\decisions.md:3410:projected decision of the definition. A choice belongs on the list when settling it later could
foundations\decisions.md:3425:    with a store of data in its scope and no choice of it projected or found in the foundation.
foundations\decisions.md:3544:task's scope, temporary exclusions, relevant current foundation decisions, any approved projected
foundations\decisions.md:3545:wording it uses and the settlements its refinement keeps for the foundation (WAY-134). It is ready
foundations\decisions.md:3547:human has accepted or rejected every candidate settlement its refinement found, every human action
foundations\decisions.md:3551:using an approved definition checks that its approval still holds and names each projected entry,
foundations\decisions.md:3562:    approved project wording without taking its plan's assignments yet names a projected entry its
foundations\decisions.md:3567:    despite a mismatch with its assigned work, a task leaves out a projected entry its code
foundations\decisions.md:3569:    candidate settlement of its refinement awaits the human, or a task is ready while a human
foundations\decisions.md:3576:applies so the next agent does not import work or dependencies the task never took on. A projected
foundations\decisions.md:3583:source-only task's code would hold a rule the foundation lacks, and its return step would write a
foundations\decisions.md:3594:of its foundation change and its return step, and brings the request to the human for review.
foundations\decisions.md:3631:### WAY-126/1 — How does a projected entry enter the foundation?
foundations\decisions.md:3633:A projected entry of an approved project definition enters the product's foundation in the
foundations\decisions.md:3637:record and with the projected terms and environment facts it uses or rests on; where the code
foundations\decisions.md:3640:hold, and a projected entry no code makes true. The return step reads the projected entries of the
foundations\decisions.md:3652:  - complies: a source-only task whose code adds the store a projected decision chooses writes
foundations\decisions.md:3655:    a projected decision's two sentences true writes that sentence and lists its meaning in the
foundations\decisions.md:3658:  - violates: the return step writes a new decision for a rule a projected entry of the
foundations\decisions.md:3659:    task's source states; a shortened projected entry is written with the gate's *Approved by*;
foundations\decisions.md:3660:    the code a late-found projected invariant covers is set aside and rewritten.
foundations\decisions.md:3665:*Rationale:* a projected entry is wording a human already settled at the gate, and the task
foundations\decisions.md:3671:*Rejected:* holding a projected entry back for the task the plan assigns — the foundation would
foundations\decisions.md:3672:lag behind the code it describes; a return step that searches only the current foundation — a
foundations\decisions.md:3675:that form; rewriting the code a late-found projected invariant covers — a check by an agent that
foundations\decisions.md:3860:  - complies: a rule whose behaviour never happens without it is shown working by a few sessions
foundations\decisions.md:3861:    with and without it; a rule meant to make a behaviour more frequent is judged over many sessions
foundations\decisions.md:3863:  - violates: a few sessions with and without are taken as proof that a rule raised a behaviour
foundations\decisions.md:3874:behaviour absent without the rule; one question "does it work" — it mixes defects with different
foundations\decisions.md:3954:each settlement in the human's words, and the task document keeps the rows the human accepts. A
foundations\decisions.md:3956:or invariant rests on, and a settlement that a current entry, or a projected entry the task
foundations\decisions.md:3958:foundation in its foundation step, or in its return step where the foundation step missed it, one
foundations\decisions.md:3974:  - violates: the cycle writes the entry with another meaning, or leaves out a kept settlement
foundations\decisions.md:3981:*Rationale:* a settlement the human makes while a task is refined binds after the merge as much as
foundations\decisions.md:3986:table read from the whole document finds a settlement said in passing, and its column of what the
foundations\decisions.md:3992:defining a project; noting a settlement only when the human states one — a settlement said in
foundations\decisions.md:3994:or drop a settlement and show the difference in the request — the human's settlement could be
foundations\decisions.md:4002:task's *Settlements to record* or a projected entry of its sources gives leaves none. An agent that
foundations\decisions.md:4013:  - complies: a task whose rows of *Settlements to record* carry its two decisions and its invariant
foundations\decisions.md:4065:    slice, given the task as its requirements, is the change's only code review; a change of four
foundations\decisions.md:4306:the tasks that realize each projected entry and the one task that writes it into the foundation
foundations\decisions.md:4320:    headings, its header carries the fingerprint the gate recorded, and the projected decision
foundations\decisions.md:4427:through its readiness gate again, while a move that changes which task writes a projected entry
foundations\decisions.md:4444:    projected decision to another task is made without the human; the breakdown answers a question
foundations\decisions.md:4454:plan's own reading of the definition, so the log makes it visible. Which task writes a projected
foundations\decisions.md:4469:plan's structure decides: each projected entry of the definition has tasks that realize it, exactly
foundations\decisions.md:4487:    projected decision no task writes;
```

### assessment and check acceptance

`rg -n -i 'assess|deliberate|accept|review|break' foundations`

Exit: 0; matching lines: 400.

```text
foundations\part_map.md:17:  - the format guard accepts an entry the template forbids — a wrong entry reaches the main
foundations\part_map.md:84:skill, which is also the independent assessor of a change to an invariant test or to the
foundations\part_map.md:92:  - a critique presents a source mismatch as an accepted correction — the human approves a meaning
foundations\part_map.md:99:breakdown of an approved definition into a project plan and the check of that plan, and the
foundations\part_map.md:107:  - the gate accepts an unresolved placeholder in a required section — tasks inherit an explicit
foundations\part_map.md:113:  - a definition reaches the breakdown with a listed technology choice still open or naming no
foundations\part_map.md:121:  - the plan check accepts a plan in which a projected entry has no task writing it, or two — the
foundations\part_map.md:124:  - the breakdown places an open question in another task than the definition names with no line
foundations\part_map.md:143:    human cannot assess what the agents chose — high — not detected
foundations\part_map.md:155:  - the gate reports a check as passed although it never ran — a change that breaks an invariant
foundations\part_map.md:158:    ran to its end, or failed — a change that breaks an invariant reaches the main branch — high —
foundations\part_map.md:161:    pass, its own tests included — a change that breaks an invariant reaches the main branch —
foundations\part_map.md:195:    without the required checks or acceptance — high — not detected
foundations\part_map.md:219:    below what it is — a reviewer cuts a rule that worked, or passes over a real defect — high —
foundations\part_map.md:228:    machine, or a review rests on a check that never ran — high — not detected
foundations\part_map.md:230:    an instruction written in a file under review — a secret enters the conversation, or a proposal
foundations\part_map.md:341:guidance for Claude Code and Codex and a `.runs/` ignore line in a product keeps its preview and
foundations\part_map.md:367:| pinned | anything, a break included, since a product takes the change only by moving the commit it pins | a line in the merge request saying what moving the pin changes for a product |
foundations\invariants.md:136:## invariant-test-break/1
foundations\invariants.md:138:Every check that cites an invariant fails, in k of n runs where its command sets them, on the deliberate break it was accepted on.
foundations\invariants.md:206:## foundation-change-assessment-record/1
foundations\invariants.md:208:Where {merge-onto} exists, no change alters, against {fork-point}, an invariant test or a foundation entry without a record of its independent assessment, naming what of the change can be cut or that nothing can, and of how each remark was settled.
foundations\invariants.md:417:## review-when-form/1
foundations\invariants.md:419:Every *Review when* in the decision log other than `none` or `TODO` names both a state and a date.
foundations\invariants.md:427:## decision-guard-overdue-review/1
foundations\invariants.md:429:The decision guard, given a date, warns of every check-by date earlier than it that no later review record answers.
foundations\invariants.md:437:## review-next-check/1
foundations\invariants.md:439:Every review record in the decision log that records that the state has not come names a date, or holds `TODO`, in *Next check*, and every other one holds nothing there but a date, `none` or `TODO`.
foundations\invariants.md:447:## review-named-version/1
foundations\invariants.md:449:Every version of a decision that a review record names exists in the decision log.
foundations\invariants.md:589:The script of `relation-model` gives a text the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that text encoded in UTF-8, after every run of spaces and line breaks is replaced by a single space and both ends are trimmed.
foundations\invariants.md:1079:Every correction an entry of `foundations/invariants.md` declares is confirmed by the human who accepts the change at the merge, with the old and the new binding part in front of them.
foundations\invariants.md:1109:For every invariant entry whose sentence a change adds or alters against "{fork-point}", the gate's report states whether the entry's method passes on "{fork-point}" and fails there on a deliberate break, or that this could not be checked.
foundations\invariants.md:1419:Every decision version and review record of the decision log carries every field the decision template gives one of its kind.
foundations\invariants.md:1429:No field of a decision version or review record of the decision log holds `none` or `TODO` where the decision template does not give it that word.
foundations\invariants.md:1439:Where {merge-onto} exists, no field of a decision version or review record of the decision log holds `TODO`.
foundations\invariants.md:1619:The fingerprint the environment facts guard gives an entry is the fingerprint of its sentence and its *Holds for* joined by a line break.
foundations\invariants.md:1749:Every row of `foundations/human_verdicts.md` naming an invariant names an entry of `foundations/invariants.md` whose method is a path, gives `pass` or `fail`, names who gave it, when and the commit assessed, and reads `none` in *Until*.
foundations\invariants.md:1759:Every row of `foundations/human_verdicts.md` naming an environment fact names an entry of `foundations/environment_facts.md` whose method is a path, gives `pass` or `fail`, names who gave it, when and the commit assessed, and carries a date in *Until*.
foundations\invariants.md:2087:Where git tracks a `CLAUDE.md` at the repository's root, its text begins with `@AGENTS.md` followed directly by a line break, `\n` or `\r\n`, or by the end of the text.
foundations\invariants.md:2109:| invariant-test-change-acceptance | replaced: a change to an invariant test is covered by the one independent assessment of any change to an invariant test or to the foundation | foundation-change-assessment-record |
foundations\invariants.md:2110:| foundation-change-panel-record | replaced: the record of a panel of two assessors and two settlements became the record of one independent assessment and of how each remark was settled | foundation-change-assessment-record |
foundations\glossary.md:79:A product's foundation is the written record of the rules the product holds itself to, of what those rules stand on and of where the product breaks them.
foundations\environment_facts.md:98:- **Holds for:** arXiv:2507.11538v1, measuring claude-3.5-haiku, claude-3.7-sonnet, claude-opus-4, claude-sonnet-4, deepseek-r1-0528, gemini-2.5-flash-preview, gemini-2.5-pro-preview, llama-4-maverick, llama-4-scout, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview, o3, o4-mini, qwen3-235b-a22b, grok-3-beta and grok-3-mini-beta
foundations\environment_facts.md:163:- **Source:** https://raw.githubusercontent.com/python/devguide/999633216399256b6ce5376c9287f07efd6c9a65/versions.rst § Status key, bugfix — "New binaries are built and released roughly every two months." · § Status key, security — "After two years (18 months for versions before 3.13), only security fixes are accepted and no more binaries are released."; read 2026-09-30
foundations\environment_facts.md:242:- **Holds for:** arXiv:2602.07150v3, measuring Qwen/Qwen3-32B, agentica-org/DeepSWE-preview and mistralai/Devstral-2-123B-Instruct-2512, each with the nano-agent and R2E-Gym scaffolds
foundations\environment_facts.md:243:- **Source:** https://arxiv.org/html/2602.07150v3 § Abstract — "We test this assumption by collecting 60,000 agentic trajectories on SWE-Bench-Verified, spanning three models and two scaffolds." · § Abstract — "We find substantial variance: single-run pass@1 estimates vary by 2.2 to 6.0 percentage points depending on which run is selected, with standard deviations exceeding 1.5 percentage points even at temperature 0." · § 2.1 — "We exhaustively evaluate six different agents, where an agent is defined as a model-scaffold pairs." · § 2.1 — "Qwen/Qwen3-32B" · § 2.1 — "agentica-org/DeepSWE-preview" · § 2.1 — "mistralai/Devstral-2-123B-Instruct-2512" · § 2.1 — "nano-agent is our own minimal scaffold for agentic coding experiments" · § 2.1 — "R2E-Gym is a code agent scaffold"; read 2026-10-08
foundations\decisions.md:26:- **Review when:** none
foundations\decisions.md:44:review; a bare identifier and a reference to a version (`WAY-17/2`) are never flagged. The
foundations\decisions.md:47:part encoded in UTF-8, taken after every run of spaces and line breaks is replaced by a single
foundations\decisions.md:57:- **Review when:** none
foundations\decisions.md:73:Invariant tests are written and accepted together with the foundation change, and during
foundations\decisions.md:76:test that carries no record of its independent assessment (WAY-10). A task that needs an invariant
foundations\decisions.md:83:- **Verification:** level 1 — invariants: foundation-change-assessment-record.
foundations\decisions.md:84:- **Review when:** no model in the range of fact impossiblebench-test-modification is Active in
foundations\decisions.md:119:- **Review when:** none
foundations\decisions.md:162:- **Review when:** none
foundations\decisions.md:180:accepted entry is accepted again. Once an entry is on the main branch, it is never edited, and
foundations\decisions.md:188:  log-merge-copies. Level 2 for acceptance after a change of meaning — an agent compares the change
foundations\decisions.md:190:  - complies: an accepted entry whose binding sentences changed on the task branch is shown to
foundations\decisions.md:193:- **Review when:** none
foundations\decisions.md:199:change of meaning without new acceptance, *Approved by* would name someone who did not approve it.
foundations\decisions.md:208:and a test counts only when a deliberately introduced break of the invariant makes it fail, in k
foundations\decisions.md:210:give the same verdict every time. Human inspection is used for assessments that neither an
foundations\decisions.md:218:- **Verification:** level 1 — invariants: invariant-method-form · invariant-test-break ·
foundations\decisions.md:224:- **Review when:** none
foundations\decisions.md:250:proposals and assess changes; `project-level/` the templates of a project definition, a project
foundations\decisions.md:285:- **Review when:** none
foundations\decisions.md:305:### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?
foundations\decisions.md:307:A change to an invariant test or to the foundation is assessed by one independent agent, on a model
foundations\decisions.md:309:assesses without the task's chronicle or the author's reasoning and names what of the change can be
foundations\decisions.md:311:that changes the assessed foundation entries or invariant tests is part of the assessed change and
foundations\decisions.md:312:does not reopen its assessment. A human accepts the change, with the assessment and its settlement,
foundations\decisions.md:320:- **Verification:** level 1 — invariants: foundation-change-assessment-record. Level 2 — an agent
foundations\decisions.md:322:  - complies: one assessor on another model reads the diff without the author's reasoning, and the
foundations\decisions.md:324:    assessed invariant test is recorded beside the one assessment;
foundations\decisions.md:325:  - violates: the assessor receives the author's reasoning; the author drops a remark without
foundations\decisions.md:326:    recording why; a change merges with no assessment record; the edits of a settlement are sent
foundations\decisions.md:327:    to a second assessment.
foundations\decisions.md:328:- **Review when:** none
foundations\decisions.md:334:reasoning; one such reader finds what a reader can, and the human who accepts at the merge reads the
foundations\decisions.md:335:change with the assessment beside it. The finding it cites measured models of other publishers only,
foundations\decisions.md:337:*Rejected:* a panel of two assessors and a settler reading both orders — its cost per change
foundations\decisions.md:339:the author assessing its own change — it checks itself; assessing again every settlement that
foundations\decisions.md:340:changes the assessed entries or tests — each correction draws new remarks, and the change reaches
foundations\decisions.md:341:the human only after a chain of assessments.
foundations\decisions.md:348:settle, writes them into the foundation in the same change, which its independent assessment covers
foundations\decisions.md:350:review of the foundation runs apart from tasks.
foundations\decisions.md:362:- **Review when:** none
foundations\decisions.md:377:complies and one that violates — and where an agent cannot judge, a human assesses it and leaves a
foundations\decisions.md:391:- **Review when:** none
foundations\decisions.md:422:  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
foundations\decisions.md:429:- **Review when:** none
foundations\decisions.md:450:either when, or the merge of the request by which they accepted it; in the-way, the approver is
foundations\decisions.md:458:- **Review when:** the-way decides which of its elements a team may adapt, and with it who approves
foundations\decisions.md:464:change reads, and what WAY-07 needs when an entry has to be accepted again.
foundations\decisions.md:484:- **Review when:** none
foundations\decisions.md:508:- **Review when:** none
foundations\decisions.md:512:*Rationale:* the chain is the path a change travels, so a missing link breaks it without a sign,
foundations\decisions.md:513:and an assumption no entry names escapes review; the link sits in the dependent entry, because
foundations\decisions.md:522:decision version and review record in the order it was written, and what is in force today is a view
foundations\decisions.md:538:- **Review when:** none
foundations\decisions.md:573:- **Review when:** none
foundations\decisions.md:601:- **Review when:** none
foundations\decisions.md:622:- **Review when:** no model in the range of fact instruction-density-accuracy is Active in
foundations\decisions.md:649:  - violates: a non-goal that a commit can break is left without a derived invariant; an
foundations\decisions.md:651:- **Review when:** none
foundations\decisions.md:661:### WAY-24/1 — How is a decision that rests on a prediction reviewed?
foundations\decisions.md:663:A decision that rests on a prediction names in *Review when* the predicted state of the world or the
foundations\decisions.md:665:whether the state has come is checked by the periodic review of the foundation. On the date, a
foundations\decisions.md:666:review record records what was observed: the state has not come, with the next date; it has come and
foundations\decisions.md:668:branch, an edit in place that the decision's approver accepts again answers the date as well when it
foundations\decisions.md:669:rewrites *Review when* from what was observed, and a check-by date is moved in no other way.
foundations\decisions.md:675:- **Verification:** level 1 — invariants: review-when-form · decision-guard-overdue-review ·
foundations\decisions.md:676:  review-next-check · review-named-version. Level 2 for who looks and when — an agent compares the
foundations\decisions.md:678:  - complies: the periodic review finds a passed check-by date and records that the state has not
foundations\decisions.md:680:    place from what was observed and accepted again;
foundations\decisions.md:681:  - violates: a review record says the state has not come but gives no next date; before the main
foundations\decisions.md:682:    branch, a passed check-by date is moved later with neither a review record nor an edit from
foundations\decisions.md:684:- **Review when:** none
foundations\decisions.md:691:*Rejected:* a decision that expires on a date — the date gets extended; a review date without a
foundations\decisions.md:692:state — nobody knows what to check; a review as a new version — a full copy for every look; the
foundations\decisions.md:714:- **Review when:** none
foundations\decisions.md:741:- **Review when:** none
foundations\decisions.md:770:- **Review when:** none
foundations\decisions.md:803:- **Review when:** none
foundations\decisions.md:811:are known; everything on demand, the critical flows included — a break there shows only when a task
foundations\decisions.md:832:- **Review when:** none
foundations\decisions.md:864:- **Review when:** none
foundations\decisions.md:898:- **Review when:** none
foundations\decisions.md:914:`derives from` — a higher decision this one serves; `narrows` — a decision this one deliberately
foundations\decisions.md:924:    part that deliberately departs from a general decision names `narrows`;
foundations\decisions.md:927:- **Review when:** none
foundations\decisions.md:941:is accepted each finding becomes a relation, a change to one of the entries, or a question to a
foundations\decisions.md:955:- **Review when:** none
foundations\decisions.md:986:- **Review when:** the first product has moved its pin to a newer the-way twice · check by:
foundations\decisions.md:1021:- **Review when:** none
foundations\decisions.md:1048:- **Review when:** none
foundations\decisions.md:1075:- **Review when:** none
foundations\decisions.md:1082:*Rejected:* fixes left to the periodic review (WAY-11) — the foundation says something false until
foundations\decisions.md:1083:the review comes.
foundations\decisions.md:1089:repository — a dependency graph, a detector of breaking changes, coverage — reading their output
foundations\decisions.md:1100:- **Review when:** none
foundations\decisions.md:1128:- **Review when:** none
foundations\decisions.md:1155:- **Review when:** none
foundations\decisions.md:1177:- **Review when:** none
foundations\decisions.md:1205:- **Review when:** none
foundations\decisions.md:1219:matches; a file that no pattern matches, and a file that two parts claim, breaks the gate, unless
foundations\decisions.md:1233:- **Review when:** none
foundations\decisions.md:1261:- **Review when:** a product holds more critical flows than its gate can run on every change ·
foundations\decisions.md:1283:raising a part's criticality needs no reason, and lowering it is accepted by the human accepting the
foundations\decisions.md:1298:- **Review when:** a product that pins the-way holds data under an obligation from a law or a
foundations\decisions.md:1308:axes (confidentiality, integrity, availability) — WAY-13 reads one measure; an unassessed part
foundations\decisions.md:1328:- **Review when:** none
foundations\decisions.md:1344:accept data the product does not trust; an exchange with the external context records its
foundations\decisions.md:1356:- **Review when:** none
foundations\decisions.md:1396:    announcement first; a level whose consumer never updates allows a break with nothing owed.
foundations\decisions.md:1397:- **Review when:** none
foundations\decisions.md:1408:importance — it says how bad a break is, not who can follow; "updates together" for every internal
foundations\decisions.md:1416:the derived list `foundations/violated_invariants.md`. A new violation of the map breaks the gate;
foundations\decisions.md:1417:a row the code no longer contradicts breaks it too and goes in the same change; a listed `fail`
foundations\decisions.md:1419:the row. A row of either list is added only by a change of the foundation that a human accepts,
foundations\decisions.md:1431:- **Review when:** none
foundations\decisions.md:1435:*Rationale:* the process enters products that already break their rules (WAY-28); listed debt
foundations\decisions.md:1445:assesses.
foundations\decisions.md:1461:- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
foundations\decisions.md:1485:- **Review when:** none
foundations\decisions.md:1518:- **Review when:** none
foundations\decisions.md:1548:- **Review when:** the gate runs as a program CI invokes, and the rule that picks its checks has a
foundations\decisions.md:1574:  - complies: "every version and review record in the log has every field of the template" as one
foundations\decisions.md:1578:- **Review when:** none
foundations\decisions.md:1583:on it (WAY-02) and a break tells whether its method catches it (WAY-08); the fingerprint moves the
foundations\decisions.md:1586:split wherever a commit can break part of a sentence — one entry per version of the log; the whole
foundations\decisions.md:1595:entry declares a correction naming both fingerprints and the human who accepts the change at the
foundations\decisions.md:1612:  - complies: a typo fixed under a declaration the accepting human confirms, with no test citation
foundations\decisions.md:1618:- **Review when:** none
foundations\decisions.md:1623:identifier never, checking a meaning gone; a version moves with meaning; the human who accepts the
foundations\decisions.md:1644:fails there on a deliberate break, and the human accepting the change at the merge sets the row with
foundations\decisions.md:1653:  gate-fork-point-evidence. Level 3 for the row — the human accepting the change at the merge sets
foundations\decisions.md:1664:- **Review when:** none
foundations\decisions.md:1695:  - complies: "every version and review record in the log has every field of the template"; "the
foundations\decisions.md:1702:- **Review when:** none
foundations\decisions.md:1720:or the path alone of a file a human assesses the product against; a command is the same on every run
foundations\decisions.md:1744:    alternative describes it names the checklist a person assesses the page against;
foundations\decisions.md:1755:- **Review when:** none
foundations\decisions.md:1790:- **Review when:** none
foundations\decisions.md:1821:    after a change since the assessed commit reaches the entry; a critical flow's test is left out and
foundations\decisions.md:1823:- **Review when:** none
foundations\decisions.md:1865:- **Review when:** none
foundations\decisions.md:1898:- **Review when:** none
foundations\decisions.md:1925:  - complies: a save-load test fails, then passes, on one commit; the independent assessment accepts
foundations\decisions.md:1930:- **Review when:** none
foundations\decisions.md:1943:### WAY-69/1 — Who writes an invariant's sentence, its check and its deliberate break, and what may the check compute for itself?
foundations\decisions.md:1946:agents, and the deliberate break the check is accepted on is written from the sentence by the
foundations\decisions.md:1947:reviewer of that code, who did not write the check. A check that cites an invariant takes the input
foundations\decisions.md:1955:- **Verification:** level 3 for who writes what — the human accepting the change at the merge
foundations\decisions.md:1956:  assesses how the work was handed out, from the record that names who wrote what. Level 2 for what
foundations\decisions.md:1963:- **Review when:** no model in the range of fact oracle-in-loop-building is Active in Anthropic's
foundations\decisions.md:1968:*Rationale:* a break chosen by a check's author aims at what the check does, not what the sentence
foundations\decisions.md:1971:The reviewer already reads the check without having written it, so the break needs no agent of its
foundations\decisions.md:1976:file a verdict leans on — every tracked file turns read-only; a separate agent for the deliberate
foundations\decisions.md:1977:break — the code review already stands apart from the check.
foundations\decisions.md:1982:in every version of a decision and every review record, the fields their forms give — holding a
foundations\decisions.md:1997:  decision-change-kind · review-when-form · review-next-check. Level 2
foundations\decisions.md:2004:- **Review when:** none
foundations\decisions.md:2030:- **Review when:** none
foundations\decisions.md:2063:- **Review when:** none
foundations\decisions.md:2074:too — a fact written before its dependent would break the branch midway.
foundations\decisions.md:2096:- **Review when:** none
foundations\decisions.md:2129:- **Review when:** none
foundations\decisions.md:2133:*Rationale:* a fact is reviewed when its source changes, so what changes together stands together:
foundations\decisions.md:2135:invariant written as a fact would never be checked on the commit that breaks it.
foundations\decisions.md:2158:- **Review when:** none
foundations\decisions.md:2182:- **Review when:** none
foundations\decisions.md:2188:fails the watch (WAY-82). Text changed beside the quoted passage passes unseen, an accepted cost.
foundations\decisions.md:2212:- **Review when:** none
foundations\decisions.md:2246:- **Review when:** none
foundations\decisions.md:2290:- **Review when:** none
foundations\decisions.md:2296:another release says nothing of the named one, while a fail there still calls for review.
foundations\decisions.md:2321:- **Review when:** none
foundations\decisions.md:2327:revision is a prediction, which belongs in *Review when* (WAY-24).
foundations\decisions.md:2328:*Rejected:* facts checked in every change's gate — the verdict follows the date; one review date
foundations\decisions.md:2330:or as a standing flag — a review with no possible outcome.
foundations\decisions.md:2336:assessed and *Until*, and counts only for the entry's current version. An invariant's verdict, with
foundations\decisions.md:2349:- **Review when:** none
foundations\decisions.md:2353:*Rationale:* a path method gives no result until a person assesses (WAY-61, WAY-81), and WAY-08
foundations\decisions.md:2381:- **Review when:** none
foundations\decisions.md:2398:process behave the same is a prediction, written in *Review when* of each decision citing the fact
foundations\decisions.md:2409:    Claude models it measured; WAY-03's *Review when* waits for no model in that fact's range being
foundations\decisions.md:2415:- **Review when:** none
foundations\decisions.md:2420:behave the same is a bet that ages as those models leave service, and bets already have *Review
foundations\decisions.md:2446:- **Review when:** none
foundations\decisions.md:2474:- **Review when:** the status of Python 3.14 in the table of versions of the Python Developer's
foundations\decisions.md:2485:support; a move at each new release — a yearly review nothing here needs; a move at the end of
foundations\decisions.md:2492:citation that, stopping being true today, would send the decision to review — a finding about agents
foundations\decisions.md:2510:- **Review when:** none
foundations\decisions.md:2514:*Rationale:* only a citation whose change would send the decision to review needs an entry to be
foundations\decisions.md:2542:- **Review when:** none
foundations\decisions.md:2571:    "verdict" lists it for review;
foundations\decisions.md:2574:- **Review when:** none
foundations\decisions.md:2579:a common term — flags people clear unread (WAY-02) — so a changed definition's uses are reviewed
foundations\decisions.md:2595:writes the entries, and a human accepts their meaning (WAY-114). A word's definition stands in the
foundations\decisions.md:2623:- **Review when:** none
foundations\decisions.md:2651:  - complies: "The assessor is the agent that assesses a change", the rest left to WAY-10;
foundations\decisions.md:2653:  - violates: "The assessor is the agent on another model that assesses a change…", with the
foundations\decisions.md:2657:- **Review when:** none
foundations\decisions.md:2662:definition changes it whenever the rule moves and sends the review of uses after what is a
foundations\decisions.md:2673:not hold enters such a sentence only where the request names it for the human who accepts the change
foundations\decisions.md:2675:definition goes, in the same change, through a review in which an agent puts the new definition in
foundations\decisions.md:2677:whose meaning moves to the human accepting the change at the merge. A term used by an entry on the
foundations\decisions.md:2685:  for the review, a new meaning and a paraphrase — an agent compares the change with the decision:
foundations\decisions.md:2692:- **Review when:** none
foundations\decisions.md:2696:*Rationale:* a sentence relies on a term by its word, which the review searches for, so a paraphrase
foundations\decisions.md:2699:*Rejected:* a version as for invariants and facts — nothing reads it; a review only of a declared
foundations\decisions.md:2701:what it missed (WAY-02); a record of the review checked by the guard — it sees only that a record
foundations\decisions.md:2725:- **Review when:** none
foundations\decisions.md:2759:- **Review when:** none
foundations\decisions.md:2765:new label. The word is the human's choice, accepted at the merge (WAY-10).
foundations\decisions.md:2783:  - complies: a decision adopts only the risk assessment step of an outside process for task
foundations\decisions.md:2787:- **Review when:** none
foundations\decisions.md:2807:  - complies: a task-cycle step accepts task information supplied from a product's chosen files or
foundations\decisions.md:2810:- **Review when:** none
foundations\decisions.md:2836:- **Review when:** none
foundations\decisions.md:2862:- **Review when:** none
foundations\decisions.md:2897:- **Review when:** none
foundations\decisions.md:2955:- **Review when:** none
foundations\decisions.md:2972:looks checked until its first run; a command split on spaces — a quoted path breaks in two, and a
foundations\decisions.md:2989:    projected entries to tasks before the breakdown has made those tasks.
foundations\decisions.md:2990:- **Review when:** none
foundations\decisions.md:2995:the product is to become. The task assignment follows the breakdown and changes with it, while
foundations\decisions.md:3016:- **Review when:** none
foundations\decisions.md:3036:the breakdown or task that resolves it.
foundations\decisions.md:3048:- **Review when:** none
foundations\decisions.md:3073:- **Review when:** none
foundations\decisions.md:3096:- **Review when:** none
foundations\decisions.md:3110:may change, an invariant it may break or a boundary it crosses to the human as material and asks
foundations\decisions.md:3122:- **Review when:** none
foundations\decisions.md:3136:assessment as an open question with its resolver but on a choice as a reason to offer a
foundations\decisions.md:3149:- **Review when:** none
foundations\decisions.md:3163:of each and a recommendation, while a question of assessment stays open; neither opens a separate
foundations\decisions.md:3181:- **Review when:** none
foundations\decisions.md:3196:### WAY-114/1 — What does a human accept of an entry, and when?
foundations\decisions.md:3198:A human accepts the meaning of a foundation entry, shown as one sentence in the human's language with
foundations\decisions.md:3199:the entry beside it, while its wording is the agent's: an agent writes the entry and the human accepts
foundations\decisions.md:3215:- **Review when:** none
foundations\decisions.md:3221:*Rejected:* acceptance of the whole wording before an entry is written — attention goes to wording
foundations\decisions.md:3222:while the meaning rarely moves, and each acceptance costs a round; storing a translation in the
foundations\decisions.md:3230:is shown as rejected. The human accepts or rejects rows before they are handed to the skills of
foundations\decisions.md:3231:their kinds, and each accepted row is recorded as it is worked through. The definition keeps the
foundations\decisions.md:3233:rows were shown and accepted.
foundations\decisions.md:3244:- **Review when:** none
foundations\decisions.md:3258:before the breakdown, and environment facts only where a projected decision or invariant rests on
foundations\decisions.md:3261:the breakdown.
foundations\decisions.md:3269:    changed known part, while a future new part is an open question resolved in the breakdown;
foundations\decisions.md:3272:- **Review when:** none
foundations\decisions.md:3302:- **Review when:** none
foundations\decisions.md:3312:### WAY-118/1 — What makes a project definition ready for breakdown?
foundations\decisions.md:3317:*Change*, rationale and rejected options; *Approved by* reads `on acceptance` until the gate,
foundations\decisions.md:3319:*Review when* as WAY-119 permits, may read `TODO`.
foundations\decisions.md:3324:the gate again before breakdown relies on it.
foundations\decisions.md:3334:  - violates: a warning-only review lets the breakdown begin with a missing decision reason, or
foundations\decisions.md:3336:- **Review when:** none
foundations\decisions.md:3346:### WAY-119/1 — When may a projected decision leave Review when unresolved at the gate?
foundations\decisions.md:3348:At the readiness gate, a projected decision's *Review when* holds a review condition and date, or
foundations\decisions.md:3350:the timing depends on later work, the human expressly accepts deferral, and a related open
foundations\decisions.md:3351:question names the breakdown or task that settles it.
foundations\decisions.md:3359:  - complies: a prediction's review date depends on the release, so the human accepts `TODO` and
foundations\decisions.md:3361:  - violates: the gate passes a `Review when: TODO` with no related open question, or an agent
foundations\decisions.md:3362:    writes `none` simply because the source said nothing about review.
foundations\decisions.md:3363:- **Review when:** none
foundations\decisions.md:3376:completed set for collective human review and every change to an invariant test or to the
foundations\decisions.md:3377:foundation go through it, and for such a change the critique is its independent assessment
foundations\decisions.md:3380:explicit verdict. For a collectively reviewed set the critic checks form, fidelity to source and
foundations\decisions.md:3389:- **Verification:** level 2 — an agent compares the review with the decision:
foundations\decisions.md:3394:- **Review when:** none
foundations\decisions.md:3401:*Rejected:* a fresh critic for every entry accepted with the human — it repeats the human's
foundations\decisions.md:3402:review; letting the critic's remarks edit human settlements without asking — it would disguise a
foundations\decisions.md:3424:  - violates: the first task of the breakdown chooses the database; a definition reaches the gate
foundations\decisions.md:3426:- **Review when:** none
foundations\decisions.md:3437:technologies; the first tasks of the breakdown — the cut itself may depend on the choice; the step
foundations\decisions.md:3473:- **Review when:** none
foundations\decisions.md:3493:the human this step serves cannot assess the technology; a critic for each option — one critique of
foundations\decisions.md:3501:### WAY-123/1 — How does a technology choice reach a human who cannot assess the technology?
foundations\decisions.md:3523:- **Review when:** none
foundations\decisions.md:3527:*Rationale:* a human who cannot assess the technology can still weigh what an option costs and
foundations\decisions.md:3547:human has accepted or rejected every candidate settlement its refinement found, every human action
foundations\decisions.md:3571:- **Review when:** none
foundations\decisions.md:3589:test-first implementation, subagent execution with independent task and final code reviews, and
foundations\decisions.md:3593:keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment
foundations\decisions.md:3594:of its foundation change and its return step, and brings the request to the human for review.
foundations\decisions.md:3597:reviewed change to the-way before use.
foundations\decisions.md:3608:  task + task review (spec + quality) + broad final review = high quality, fast iteration"
foundations\decisions.md:3609:  `requesting-code-review/SKILL.md` — "The reviewer gets precisely crafted context for evaluation —
foundations\decisions.md:3617:    review, or silently runs a different Superpowers version.
foundations\decisions.md:3618:- **Review when:** none
foundations\decisions.md:3622:*Rationale:* the borrowed skills provide design, test and review methods, while the-way must keep
foundations\decisions.md:3623:control of task sources, binding foundation approvals and the single human review point. Naming
foundations\decisions.md:3638:makes only part of it true, the agent writes that part and the human accepts its meaning at the
foundations\decisions.md:3661:- **Review when:** none
foundations\decisions.md:3710:- **Review when:** none
foundations\decisions.md:3759:- **Review when:** no model in the range of fact context-file-effect is Active in Anthropic's table
foundations\decisions.md:3795:- **Review when:** none
foundations\decisions.md:3830:- **Review when:** none
foundations\decisions.md:3865:- **Review when:** none
foundations\decisions.md:3898:- **Review when:** none
foundations\decisions.md:3936:- **Review when:** no model in the range of fact single-rule-compliance is Active in Anthropic's
foundations\decisions.md:3954:each settlement in the human's words, and the task document keeps the rows the human accepts. A
foundations\decisions.md:3962:accepts the entry's meaning at the merge (WAY-114).
foundations\decisions.md:3977:- **Review when:** none
foundations\decisions.md:3984:words carries the meaning into the cycle without a second point of acceptance: the wording stays
foundations\decisions.md:4000:A task's cycle writes a spec, reviewed by an agent other than its author, before its plan where the
foundations\decisions.md:4022:- **Review when:** five cycles of `implement-task` have run under this decision, or a cycle has
foundations\decisions.md:4030:*Rationale:* a spec and its review earn their cost where an agent designs a foundation entry itself,
foundations\decisions.md:4032:task's document carries every entry, a spec restates what the human already settled and its review
foundations\decisions.md:4033:finds nothing the reviews of the code would miss. An invariant the document carries is kept from
foundations\decisions.md:4046:### WAY-136/1 — What plan does a task's cycle write, and who makes and reviews its slices?
foundations\decisions.md:4049:slices and holds no code. Each slice is made by an agent of its own and then reviewed by an agent
foundations\decisions.md:4050:that did not make it, and a change of more than one slice then gets one review of the whole change,
foundations\decisions.md:4051:while the review of a plan's only slice is the review of the whole change. A slice that proves too
foundations\decisions.md:4064:  - complies: a one-line fix is made from a plan of one slice by one agent, and the review of that
foundations\decisions.md:4065:    slice, given the task as its requirements, is the change's only code review; a change of four
foundations\decisions.md:4066:    slices gets four slice reviews and one review of the whole change; a slice that outgrows its
foundations\decisions.md:4069:    Superpowers `writing-plans`; the agent that made a slice reviews it; a change of one slice gets
foundations\decisions.md:4070:    a second review of the same range; the code of an outgrown slice is kept and completed.
foundations\decisions.md:4071:- **Review when:** five cycles of `implement-task` have run under this decision, or a cycle has
foundations\decisions.md:4080:and a narrow reviewer reads it, which is where reviews catch the errors that matter; code written
foundations\decisions.md:4081:out ahead in the plan is most of a plan's cost and catches nothing a review of the code does not. A
foundations\decisions.md:4084:one review reads the whole change.
foundations\decisions.md:4086:share of the change and still needs the review of that code; a separate path for small tasks
foundations\decisions.md:4088:step, while size only lightens one process (WAY-13); a review of the whole change after the review
foundations\decisions.md:4114:- **Review when:** none
foundations\decisions.md:4128:falls to the agent's taste, and the property can enter higher unseen; the same tie-break for every
foundations\decisions.md:4132:### WAY-138/1 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go?
foundations\decisions.md:4158:- **Review when:** the tests run on choices other than a place to run give no risk that the
foundations\decisions.md:4166:traffic the project expects — comes to light only when someone asks what the choice could break.
foundations\decisions.md:4170:reader what was accepted without passing for a sourced fact. The tests run on the option
foundations\decisions.md:4185:preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of
foundations\decisions.md:4206:- **Review when:** none
foundations\decisions.md:4254:- **Review when:** none
foundations\decisions.md:4259:in the diff the human reviews, so the human who makes it sees what it changes; named in the task
foundations\decisions.md:4261:The request is the cycle's single point of human review (WAY-125), so a human action that uses the
foundations\decisions.md:4289:- **Review when:** none
foundations\decisions.md:4300:### WAY-142/1 — What does the breakdown of a project write, and in what form?
foundations\decisions.md:4302:The breakdown of a project writes its plan as one document beside the approved definition, whose
foundations\decisions.md:4326:- **Review when:** every task of the first plan this step writes reads `done` or `dropped —
foundations\decisions.md:4339:step takes from the practice of a roadmap of vertical slices the breaking of a project into tasks
foundations\decisions.md:4372:- **Review when:** every task of the first plan this step writes reads `done` or `dropped —
foundations\decisions.md:4407:- **Review when:** none
foundations\decisions.md:4428:into the foundation is the human's to decide. A question that arises only in the breakdown goes to
foundations\decisions.md:4438:  - complies: the breakdown moves the question on a session's secret from the task of the test
foundations\decisions.md:4440:    changes; the breakdown finds that nothing says whether the test server is public from the first
foundations\decisions.md:4444:    projected decision to another task is made without the human; the breakdown answers a question
foundations\decisions.md:4445:    from its own reading of the code; a question found in the breakdown waits in a task as an
foundations\decisions.md:4447:- **Review when:** none
foundations\decisions.md:4452:breakdown is the first to see where the question meets the work; moving it changes the way to the
foundations\decisions.md:4456:question the breakdown raises was settled by nobody, and the human answers it while the plan can
foundations\decisions.md:4463:own placement; only the human answering a question the breakdown resolves — the human would restate
foundations\decisions.md:4491:- **Review when:** none
foundations\decisions.md:4499:rules it would be checking. The rule takes from the practice of a roadmap its review of the plan
foundations\decisions.md:4523:- **Review when:** none
```

### independence and execution

`rg -n -i 'slice|parallel|independen|dependenc|Superpowers' foundations`

Exit: 0; matching lines: 93.

```text
foundations\part_map.md:4:promises to the products pinned to its commits. The map says which dependencies are allowed; the
foundations\part_map.md:5:product's dependency graph shows which dependencies the code actually holds. When no command
foundations\part_map.md:84:skill, which is also the independent assessor of a change to an invariant test or to the
foundations\part_map.md:119:  - a task using a project definition only as a source inherits work or dependencies from that
foundations\part_map.md:360:| a command a product declares — a dependency graph, coverage | them → us | untrusted | no |
foundations\glossary.md:189:## slice
foundations\glossary.md:191:A slice is a piece of a task's change that the task's plan sets apart with its own files, goal, material to read and checks.
foundations\invariants.md:208:Where {merge-onto} exists, no change alters, against {fork-point}, an invariant test or a foundation entry without a record of its independent assessment, naming what of the change can be cut or that nothing can, and of how each remark was settled.
foundations\invariants.md:797:## map-guard-dependency-report/1
foundations\invariants.md:799:The map guard computes the criticality of a part that has failure modes recorded as the highest of the severities of its own failure modes, of the criticalities of the critical flows it lies on, and of the computed criticalities of the parts that depend on it by a dependency recording no separation.
foundations\invariants.md:919:Every dependency the code holds that the part map does not allow stands on the list of known violations.
foundations\invariants.md:939:Every row of the list of known violations names a dependency the code holds that the part map does not allow.
foundations\invariants.md:2109:| invariant-test-change-acceptance | replaced: a change to an invariant test is covered by the one independent assessment of any change to an invariant test or to the foundation | foundation-change-assessment-record |
foundations\invariants.md:2110:| foundation-change-panel-record | replaced: the record of a panel of two assessors and two settlements became the record of one independent assessment and of how each remark was settled | foundation-change-assessment-record |
foundations\decisions.md:76:test that carries no record of its independent assessment (WAY-10). A task that needs an invariant
foundations\decisions.md:114:    criticality is computed from them; existing dependencies between parts are read from the
foundations\decisions.md:115:    product's own dependency graph and compared with the map's allowed ones;
foundations\decisions.md:117:    list of the product's endpoints kept next to the code; the allowed dependencies in the part
foundations\decisions.md:307:A change to an invariant test or to the foundation is assessed by one independent agent, on a model
foundations\decisions.md:333:share its blind spots, so independence comes from another model and from not seeing the author's
foundations\decisions.md:338:outweighs what one independent reader misses, and its uncertainty becomes questions for the human;
foundations\decisions.md:348:settle, writes them into the foundation in the same change, which its independent assessment covers
foundations\decisions.md:424:    plan of one slice and runs the same checks as any change to the parts it touches;
foundations\decisions.md:965:— contradictions between parts go unseen; a search at writing only — parallel tasks collide once
foundations\decisions.md:993:products lag behind the process, and moving a pin is work, like updating a dependency.
foundations\decisions.md:1089:repository — a dependency graph, a detector of breaking changes, coverage — reading their output
foundations\decisions.md:1118:dependency is a field of the part it starts from, and the known violations of the map's allowed
foundations\decisions.md:1119:dependencies are a derived file beside the map, so neither is an entry of its own. The whole map
foundations\decisions.md:1134:A dependency has no identity beyond its pair of parts, and the map is read whole.
foundations\decisions.md:1135:*Rejected:* a dependency as an entry with its own identifier — nothing refers to it alone;
foundations\decisions.md:1170:patterns, allowed dependencies, failure modes and a flow's list of parts stay outside it.
foundations\decisions.md:1252:file the map leaves out, to the build configuration or to the dependencies lies on every flow. The
foundations\decisions.md:1267:lies on it. Files left out, the build and dependencies can alter any flow, nothing saying
foundations\decisions.md:1281:depend on it, unless the dependency records that the two are separated and a failure of one does
foundations\decisions.md:1291:  part-criticality-field · map-guard-unrecorded-criticality · map-guard-dependency-report ·
foundations\decisions.md:1307:*Rejected:* criticality written by hand — a second copy of what flows and dependencies say; three
foundations\decisions.md:1409:dependency — inside one repository it always holds.
foundations\decisions.md:1411:### WAY-51/1 — What does the main branch hold where the product does not meet an invariant or the part map's allowed dependencies?
foundations\decisions.md:1413:On the main branch the part map holds its allowed dependencies together with a listed debt:
foundations\decisions.md:1414:every dependency the code holds that the map does not allow stands on a derived list of known
foundations\decisions.md:1450:part's responsibility, its allowed dependencies, and the binding sentences of the decisions whose
foundations\decisions.md:1925:  - complies: a save-load test fails, then passes, on one commit; the independent assessment accepts
foundations\decisions.md:2866:*Rationale:* starting with the author gives the process a real first user; aiming at independent
foundations\decisions.md:3377:foundation go through it, and for such a change the critique is its independent assessment
foundations\decisions.md:3378:(WAY-10). An independent critique gives one fresh agent the full proposal or set, its sources and
foundations\decisions.md:3398:*Rationale:* the author is attached to its own fluent proposal, and an independent reading can
foundations\decisions.md:3480:project needs. Research of independent choices run side by side and kept in reports lets the
foundations\decisions.md:3488:A comparison the human cannot verify needs an independent reader that refutes what no source
foundations\decisions.md:3530:cheapest keeps cost and upkeep lowest. Independent choices shown together are settled in one
foundations\decisions.md:3542:A task document records whether the task is independent, belongs to an item of a project's plan,
foundations\decisions.md:3550:A project member also matches its plan item's scope, dependencies and assigned entries; any task
foundations\decisions.md:3553:dependency from the plan.
foundations\decisions.md:3561:  - complies: an independent task is ready without a project plan, a source-only task uses
foundations\decisions.md:3576:applies so the next agent does not import work or dependencies the task never took on. A projected
foundations\decisions.md:3581:*Rejected:* requiring every task to belong to a project plan — it excludes independent tasks and
foundations\decisions.md:3586:### WAY-125/1 — Which Superpowers methods does the autonomous task cycle adopt?
foundations\decisions.md:3588:The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec,
foundations\decisions.md:3589:test-first implementation, subagent execution with independent task and final code reviews, and
foundations\decisions.md:3593:keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment
foundations\decisions.md:3596:without one, the cycle opens a blocked draft request; a different Superpowers version requires a
foundations\decisions.md:3601:- **Based on:** observation of installed Superpowers 6.4.1 on 2026-10-05 using `Get-Content -Raw
foundations\decisions.md:3604:  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`:
foundations\decisions.md:3617:    review, or silently runs a different Superpowers version.
foundations\decisions.md:3624:the version makes the dependency visible when the process is pinned in a product. When a spec is
foundations\decisions.md:3627:*Rejected:* adopting the complete Superpowers workflow with its intermediate human gates — it would
foundations\decisions.md:4036:goes, its slices already made among them, since the spec may change what they made, and a fresh
foundations\decisions.md:4046:### WAY-136/1 — What plan does a task's cycle write, and who makes and reviews its slices?
foundations\decisions.md:4049:slices and holds no code. Each slice is made by an agent of its own and then reviewed by an agent
foundations\decisions.md:4050:that did not make it, and a change of more than one slice then gets one review of the whole change,
foundations\decisions.md:4051:while the review of a plan's only slice is the review of the whole change. A slice that proves too
foundations\decisions.md:4056:- **Based on:** observation of installed Superpowers 6.4.1 on 2026-10-10 using `sed -n` and
foundations\decisions.md:4058:  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`:
foundations\decisions.md:4064:  - complies: a one-line fix is made from a plan of one slice by one agent, and the review of that
foundations\decisions.md:4065:    slice, given the task as its requirements, is the change's only code review; a change of four
foundations\decisions.md:4066:    slices gets four slice reviews and one review of the whole change; a slice that outgrows its
foundations\decisions.md:4069:    Superpowers `writing-plans`; the agent that made a slice reviews it; a change of one slice gets
foundations\decisions.md:4070:    a second review of the same range; the code of an outgrown slice is kept and completed.
foundations\decisions.md:4072:  returned more than one slice in three of its plan as too large, or has used, as
foundations\decisions.md:4079:*Rationale:* a plan earns its cost by dividing the change, so that a narrow agent makes each slice
foundations\decisions.md:4083:apart from the cycle. A small change is a plan of one slice, so one path holds every task, and its
foundations\decisions.md:4085:*Rejected:* Superpowers `writing-plans` — each step carries its code, so the plan costs a large
foundations\decisions.md:4089:of a plan's only slice — it reads the same range twice; an outgrown slice's code kept and completed
foundations\decisions.md:4339:step takes from the practice of a roadmap of vertical slices the breaking of a project into tasks
foundations\decisions.md:4383:the practice of vertical slices the cut by what can be checked in the running product, and from its
foundations\decisions.md:4387:task naming the task it opens the way for — it repeats a dependency the plan already holds; the word
foundations\decisions.md:4388:slice for a task of the plan — the word already names a piece of a task's change.
foundations\decisions.md:4395:the dependencies.
foundations\decisions.md:4406:    ordered by a goal picked in an interview against their dependencies.
foundations\decisions.md:4411:*Rationale:* the dependencies already say which tasks can go together; a second field derived from
foundations\decisions.md:4412:them is a copy that drifts as soon as one dependency changes, and its lists grow long enough that
foundations\decisions.md:4413:nobody reads them. The rule takes from the practice of a roadmap its graph of dependencies and the
foundations\decisions.md:4416:*Rejected:* a field naming the tasks a task can be worked on beside — a copy of the dependencies
foundations\decisions.md:4473:independent critique then judges, against the definition, what no script tells apart: whether each
```

### waiting entries and vocabulary

`rg -n -i 'TODO.*(cycle|plan|return|assess)|foundation step|return step|invariant test' foundations`

Exit: 0; matching lines: 44.

```text
foundations\part_map.md:84:skill, which is also the independent assessor of a change to an invariant test or to the
foundations\invariants.md:208:Where {merge-onto} exists, no change alters, against {fork-point}, an invariant test or a foundation entry without a record of its independent assessment, naming what of the change can be cut or that nothing can, and of how each remark was settled.
foundations\invariants.md:218:Where {merge-onto} exists, every change against {fork-point} holds, in one of its commits, the record of its task's return step.
foundations\invariants.md:1329:Every `data:` line in an invariant test names a file that exists.
foundations\invariants.md:1339:The invariant tests of a change include every file that is an invariant test on "{fork-point}" or on the commit being checked.
foundations\invariants.md:2109:| invariant-test-change-acceptance | replaced: a change to an invariant test is covered by the one independent assessment of any change to an invariant test or to the foundation | foundation-change-assessment-record |
foundations\glossary.md:84:## foundation step
foundations\glossary.md:86:The foundation step is the step of a task in which the task writes the change of the foundation it sets out to make, as against what its return step carries back.
foundations\glossary.md:112:## invariant test
foundations\glossary.md:114:An invariant test is a file that holds a check citing an invariant, or a file such a check reads and names as its data.
foundations\glossary.md:182:## return step
foundations\glossary.md:184:The return step is the step of a task that carries back to the foundation what the task's change holds and the foundation does not yet say.
foundations\decisions.md:10:it. A task that sets out to change the foundation makes that change in its foundation step, and the
foundations\decisions.md:23:    foundation step;
foundations\decisions.md:71:### WAY-03/1 — Who may change an invariant test, and when?
foundations\decisions.md:73:Invariant tests are written and accepted together with the foundation change, and during
foundations\decisions.md:77:test changed goes back to the foundation step.
foundations\decisions.md:90:turns green, and the foundation lies. Keeping invariant tests out of the implementer's reach
foundations\decisions.md:129:field of a part), the agent's environment and the return step (the task cycle); external
foundations\decisions.md:305:### WAY-10/1 — Who assesses a change to an invariant test or to the foundation?
foundations\decisions.md:307:A change to an invariant test or to the foundation is assessed by one independent agent, on a model
foundations\decisions.md:311:that changes the assessed foundation entries or invariant tests is part of the assessed change and
foundations\decisions.md:324:    assessed invariant test is recorded beside the one assessment;
foundations\decisions.md:345:A task ends with its return step before its branch is merged: an agent lists from the diff and the
foundations\decisions.md:356:- **Verification:** level 1 — invariants: return-step-record. Level 2 for what the return step finds
foundations\decisions.md:360:  - violates: the return step reports nothing to add, while the diff brings in behaviour that no
foundations\decisions.md:369:*Rejected:* the foundation changed only at the foundation step — what implementation teaches stays
foundations\decisions.md:788:which of it the product must keep — and the other invariants come through the return step of
foundations\decisions.md:1878:### WAY-65/1 — How does a check cite its invariant, and which files are invariant tests?
foundations\decisions.md:1883:an invariant test of a change when it is one on the commit the branch left the main branch from or
foundations\decisions.md:1905:*Rejected:* the paths a method names as the invariant tests — a method names data, not checks; one
foundations\decisions.md:3370:*Rejected:* blocking every `TODO` — the human would have to guess a date before the plan exists;
foundations\decisions.md:3376:completed set for collective human review and every change to an invariant test or to the
foundations\decisions.md:3583:source-only task's code would hold a rule the foundation lacks, and its return step would write a
foundations\decisions.md:3594:of its foundation change and its return step, and brings the request to the human for review.
foundations\decisions.md:3634:foundation step of the first task whose code makes it true — the task the plan assigns, or a task
foundations\decisions.md:3640:hold, and a projected entry no code makes true. The return step reads the projected entries of the
foundations\decisions.md:3641:task's sources as well as the foundation, writes one the code makes true that the foundation step
foundations\decisions.md:3653:    that decision whole in its foundation step, *Approved by* copied from the gate record, and
foundations\decisions.md:3658:  - violates: the return step writes a new decision for a rule a projected entry of the
foundations\decisions.md:3668:foundation step keeps the order a foundation change has: the entry, and an invariant's test, are
foundations\decisions.md:3672:lag behind the code it describes; a return step that searches only the current foundation — a
foundations\decisions.md:3958:foundation in its foundation step, or in its return step where the foundation step missed it, one
foundations\decisions.md:3971:    carries that row, and its cycle writes a decision with that meaning in its foundation step,
```
