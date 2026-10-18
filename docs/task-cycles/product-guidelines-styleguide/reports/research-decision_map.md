# Decision map for "product guidelines / styleguide" design

Source checkout: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/foundations/`
(decisions.md 5425 lines, 152 decisions, read whole; invariants.md 2148 lines, 210 entries, read
whole; environment_facts.md 249 lines, 30 facts, read whole; glossary.md and part_map.md read for
the keyword sweep and for terms/parts that bear on the design).

Quotes below are verbatim; wrapped lines are joined with a single space. Text marked
**Interpretation** is mine, not the foundation's.

---

## 1. One line per decision (152)

Format: `WAY-NN | relevance | why | lines in decisions.md`

```
WAY-01 | high | Foundation describes current state; foundation change only in a task's foundation step, merged with code — skill writing entries "before first screen" outside a task collides | 6-36
WAY-02 | high | Fingerprint references (`id@fp`) in documents; flagged on change; bare ids and version refs "never flagged" — form script and stop-the-merge rest on it | 38-69
WAY-03 | low | Invariant tests read-only during implementation; applies to the new invariants' checks in products | 71-93
WAY-04 | high | Closed five-element foundation; derived vs hand-written; guidelines must stay outside yet must not copy rules/state | 95-135
WAY-05 | low | How decision entries are written; new decisions for this change follow it (no file names in authored rationale) | 137-174
WAY-07 | none | Log edit rules before/after main branch | 176-201
WAY-08 | high | Invariant method, deliberate break, human inspection only where nothing repeatable settles it; accessibility example | 203-232
WAY-09 | high | Closed list of repository directories and what each holds; new template/skill/script need a named directory | 234-303
WAY-10 | low | One independent assessment of every foundation change; skill-written product entries go through it | 305-341
WAY-11 | low | Return step; distinguishes product rules (invariants) from replaceable details — bears on what styleguide rules become invariants | 343-382
WAY-12 | high | Decision checked via derived invariants; WCAG adoption decision must name its level-1 invariants | 384-412
WAY-13 | low | Path/checks set by what a task touches; styleguide changes are ordinary tasks | 414-457
WAY-14 | low | Human approves decisions; skill only proposes the WCAG decision | 459-478
WAY-16 | high | One gate command; no separate test/lint commands — form script must run as an invariant method under the gate | 480-505
WAY-17 | high | Mandatory chain fact -> decision -> invariant -> test; WCAG fact -> adoption -> contrast/focus invariants -> checks | 507-529
WAY-18 | high | One decision log per product; styleguide must not hold a second log of design decisions | 531-561
WAY-19 | none | Numbering/versioning | 563-594
WAY-20 | none | Kinds of change | 596-621
WAY-21 | high | Scope names parts from the map; product styleguide decisions are found through the UI part | 623-643
WAY-22 | high | Choice = decision, commit-checkable part = invariant; rules in guideline prose escape the gate | 645-671
WAY-24 | none | Review when for predictions | 673-706
WAY-25 | low | Collisions between decisions; styleguide decisions vs others need recorded precedence | 708-735
WAY-26 | high | Each trade-off principle / non-goal is its own decision — typical "design principles" of a styleguide | 737-761
WAY-27 | low | No pointer to unreachable sources in the-way; new templates/skill may cite public WCAG pages only | 763-792
WAY-28 | high | Entering an existing product: decisions recovered only when a task touches their parts — audit mode collides | 794-824
WAY-29 | high | Recovered decision rationale quoted or `unknown`; agent's rationale goes to human as question — audit mode | 826-855
WAY-30 | low | Contradiction handling; no exception lives only in task docs — relevant to gradual cleanup exceptions | 857-889
WAY-31 | high | Fingerprinted links renewed in the same merge; model for "reference whose entry changed stops the merge" | 891-924
WAY-32 | none | Relation types closed list | 926-950
WAY-33 | low | Whole-foundation search when entries are written; skill inherits via element skills | 952-981
WAY-34 | high | Pinned commit: templates/skills come from the pin; product-scoped invariants belong to each product | 983-1010
WAY-35 | high | Element skill holds only way of working; rules live in templates citing decisions — model for styleguide skill/template | 1012-1044
WAY-36 | high | Rules ending with a piece of work stay in its plan — bears on the `{fork-point}` companion for gradual cleanup | 1046-1073
WAY-37 | low | Entries waiting for something are fixed when it arrives; no entry found waiting for guidelines | 1075-1100
WAY-38 | high | Scripts: Python stdlib only, call product-declared commands via adapter; never parse other languages | 1102-1130
WAY-40 | none | Part map entry kinds | 1132-1155
WAY-41 | none | Part identifiers | 1157-1181
WAY-42 | none | Map binding part | 1183-1204
WAY-43 | none | Map versioning | 1206-1231
WAY-44 | high | Files directing agents form their own part; guidelines live there in a product | 1233-1262
WAY-45 | none | Critical flows | 1264-1288
WAY-46 | high | Obligation from a law enters as a failure mode; relevant if accessibility law (not voluntary WCAG) applies | 1290-1329
WAY-47 | none | Flow coverage | 1331-1356
WAY-48 | none | Trust boundaries | 1358-1382
WAY-49 | none | Surfaces | 1384-1426
WAY-51 | high | Listed debt (violated invariants) — the sanctioned route for gradual cleanup; rule never weakened to fit code | 1428-1462
WAY-52 | high | Generated path-pinned rules for agents; no hand-written rule files copying the map/decisions | 1464-1488
WAY-53 | low | Derived files equal their generator's output — applies if any styleguide part is generated from tokens | 1490-1511
WAY-54 | high | Template marks read off / transcribed / judgment; values read off where a tool gives them — token values in styleguide | 1513-1544
WAY-55 | low | Gate code lives only under gate/; form script is not gate code | 1546-1575
WAY-56 | low | One sentence per invariant | 1577-1605
WAY-57 | low | Invariant versions; references to versions are historical, never flagged | 1607-1648
WAY-58 | low | Recovered invariants list; audit mode must not mark new rules recovered | 1650-1695
WAY-60 | high | Conditions deciding an invariant stand in sentence/foundation/decision; change measured against `{fork-point}` | 1697-1731
WAY-61 | high | Method form; check reads the real data, not made-up input; verdict per entry | 1733-1785
WAY-62 | high | Invariant names parts or `every`; form invariant must reach changes to decisions/invariants | 1787-1816
WAY-63 | low | Result values; a check that sees nothing must be `unchecked` with listed reason | 1818-1853
WAY-64 | none | Where invariant/fact entries stand | 1855-1893
WAY-65 | low | Check cites `invariant: id/version` at smallest unit | 1895-1924
WAY-68 | low | Flaky checks; a browser focus test may flip | 1926-1958
WAY-69 | high | Sentence, check, code by three agents; check must not read expected value from the file it is about | 1960-1994
WAY-71 | none | Field presence none/TODO | 1996-2032
WAY-72 | low | Foundation in English; guidelines are outside, language unsettled (cf. WAY-108) | 2034-2058
WAY-73 | high | Rests on names facts holding a condition; outside-standard threshold with `Rests on: none` violates | 2060-2091
WAY-74 | low | Run record JSONL form; form script as invariant method must write it | 2093-2126
WAY-76 | low | One fact per sentence/source — one WCAG criterion per fact | 2128-2155
WAY-77 | low | Holds for names edition — "WCAG 2.2 (W3C Rec, date)" | 2157-2185
WAY-78 | none | Fact binding part | 2187-2208
WAY-79 | none | Fact versioning | 2210-2238
WAY-80 | high | Fact source: edition address, passage word for word; model memory is no source — WCAG facts | 2240-2273
WAY-81 | low | Fact method: watch of WCAG edition | 2275-2318
WAY-82 | none | When fact methods run | 2320-2347
WAY-83 | low | Human verdict rows — if focus visibility needs a person | 2349-2375
WAY-84 | none | Settings outside repository | 2377-2408
WAY-85 | none | Study findings as facts | 2410-2440
WAY-86 | high | Voluntary catalogue binds only through an adopting decision naming edition, level, area; WCAG is its own example | 2442-2474
WAY-89 | low | Python 3.14 for scripts (form script) | 2476-2503
WAY-90 | low | Based on citations as facts with fingerprints — WCAG adoption decision's Based on | 2505-2536
WAY-93 | high | Glossary term vs part identifier collision warning; exemption only for element directories | 2538-2570
WAY-94 | low | Glossary entry form; glossary terms carry no fingerprint (guideline refs to terms) | 2572-2604
WAY-95 | high | Which words take glossary entries; process words in the-way's glossary — "guidelines" | 2606-2650
WAY-96 | low | Definition shape for the "guidelines" entry | 2652-2684
WAY-97 | high | Sentences use the term, never a paraphrase; glossary entries carry no version/fingerprint | 2686-2720
WAY-98 | none | Avoid counting | 2722-2754
WAY-99 | low | One word one meaning; "view" (WAY-18 log view) vs "view files" in the-way's own text | 2756-2786
WAY-100 | high | Borrowed method binds only via an adopting decision — design tokens, DTCG format, styleguide practice | 2788-2812
WAY-101 | none | Backlog tool | 2814-2835
WAY-102 | high | Change of direction passes through the foundation without memory — the reason for fingerprinted guideline refs | 2837-2862
WAY-103 | low | Skills give agents executable steps | 2864-2887
WAY-104 | high | Product's domain words held by the-way glossary need a qualifier — "guidelines" would become such a word | 2889-2941
WAY-105 | low | Missing-script methods: python -> unchecked, node -> TODO — contrast check in JS reads TODO until written | 2943-2990
WAY-106 | high | Project level writes no foundation entries — "before first screen" mode inside project definition collides | 2992-3016
WAY-107 | high | Product's own paths stay outside the installer's marked AGENTS.md block | 3018-3042
WAY-108 | low | Content in conversation language, structural words English — model for guidelines template | 3044-3073
WAY-109 | low | Material not silently adopted as settlement — research findings for styleguide | 3075-3096
WAY-110 | none | Deadlines | 3098-3120
WAY-111 | low | Project level reads current foundation | 3122-3149
WAY-112 | low | Develop/resume a definition — resumable styleguide conversation analogue | 3151-3179
WAY-113 | high | How to ask: ways, costs, recommendation; one challenge question after a choice enters a binding part | 3181-3215
WAY-114 | high | Question only where agent has no recommendation — styleguide skill explicitly departs | 3217-3244
WAY-115 | low | Candidate table before entries are written | 3246-3275
WAY-116 | low | What a definition may project | 3277-3303
WAY-117 | low | Projected entries stand in definition | 3305-3332
WAY-118 | none | Readiness gate | 3334-3366
WAY-119 | none | Review when deferral | 3368-3393
WAY-120 | high | Critique of proposals/sets; foundation changes go through it | 3395-3425
WAY-121 | high | Technology step; interface matter of agent's way to running product; screen-look projects | 3427-3503
WAY-122 | high | Research discipline for technology options (scoped to project-level) — the skill borrows it | 3505-3562
WAY-123 | high | Options shown by consequences; recommend simplest/cheapest; weak point stated | 3564-3601
WAY-124 | low | Task readiness | 3603-3651
WAY-125 | low | Superpowers adopted only for implement-task — styleguide skill may not use brainstorming without adoption | 3653-3713
WAY-126 | low | Projected entries enter the foundation | 3715-3760
WAY-127 | high | Skill entry points generated; new skill must get them | 3762-3819
WAY-128 | high | What an always-loaded line may hold; rule for some files goes to a file loaded with them | 3821-3861
WAY-129 | high | Pointers by backticked path with condition, no `@` import | 3863-3887
WAY-130 | high | Rule enters an instruction file only for a repeated mistake or carrying a recorded decision | 3889-3927
WAY-131 | low | How to settle whether a rule works | 3929-3959
WAY-132 | high | AGENTS.md carries shared instructions; installer's block left to installer | 3961-3997
WAY-133 | high | Rule that must hold every time needs a mechanism; instruction says what it is for | 3999-4032
WAY-134 | low | Refinement settlements; precedent of `narrows WAY-114` | 4034-4086
WAY-135 | low | Spec where open design choice (this change) | 4088-4137
WAY-136 | low | Plan/one-author; invariant sentence and check by two other agents | 4139-4211
WAY-137 | none | Place-to-run tie-break | 4213-4251
WAY-138 | low | Pre-mortem of recommended option — could be borrowed for styleguide recommendations | 4253-4301
WAY-139 | high | The-way holds no product skill, only a list; "a document ... no step reads it" rejected | 4303-4340
WAY-140 | none | Effects outside repo | 4342-4395
WAY-141 | high | Installer: CLAUDE.md import, writes no `.claude/rules/the-way.md` | 4397-4419
WAY-142 | none | Plan form | 4421-4471
WAY-143 | none | Plan task ends | 4473-4509
WAY-144 | none | Parallel tasks | 4511-4546
WAY-145 | none | Open questions placement | 4548-4592
WAY-146 | none | Plan check | 4594-4632
WAY-147 | none | Task names | 4634-4663
WAY-148 | none | Stage handoffs | 4665-4709
WAY-149 | none | Return-step break timing | 4711-4751
WAY-150 | low | Selective foundation reading by skills — styleguide skill reads UI-part decisions | 4753-4789
WAY-151 | none | plan-project reading | 4791-4826
WAY-152 | none | Project orchestrator | 4828-4857
WAY-153 | none | Plan state evidence | 4859-4899
WAY-154 | none | Refinement exchange | 4901-4937
WAY-155 | none | Answering agent | 4939-4972
WAY-156 | none | Plan change routing | 4974-5007
WAY-157 | none | Waiting | 5009-5036
WAY-158 | none | Diff reading | 5038-5063
WAY-159 | none | Focused checks | 5065-5093
WAY-160 | none | Gate run in cycle | 5095-5123
WAY-161 | none | Review findings | 5125-5189
WAY-162 | none | Blocked review | 5191-5261
WAY-163 | none | Before blocked request | 5263-5304
WAY-164 | none | Author self-check | 5306-5343
WAY-165 | high | Interface matter: how an agent operates the product "as its user does" — needed to check focus visibility | 5345-5390
WAY-166 | low | Agent-usable options in way-to-running-product choices | 5392-5426
```

Counts: high 54, low 49, none 49 (152).

---

## 2. High-relevance decisions — binding text, Rejected/Verification, tensions

### WAY-01 (6-36)
Binding: "On the main branch, the foundation describes the product as it is — its rules, together with the listed debt wherever the product does not yet meet them — and roadmaps and plans do not change it. A task that sets out to change the foundation makes that change in its foundation step, and the code follows; a foundation change in progress lives on the task's branch in the product's repository and reaches the main branch in the same merge as the code that follows it."
Verification violates: "a planned feature is written into the foundation before it is built; the code is merged and the foundation change is left for a later task."
Rejected: "the foundation as a description of the target product — it ages unseen".
TENSION: the skill "writes the product's decisions, invariants, environment facts through element skills" in a mode "before the first screen". **Interpretation:** a product decision such as WCAG adoption or a palette, written before any screen exists and merged on its own, is "a planned feature written into the foundation before it is built". It complies only if the skill runs inside a task's foundation step (entries + the code that follows — e.g. the tokens file — in one merge) or projects entries into a project definition (WAY-106/117). Invariants that are vacuously true before screens exist are not forbidden, but the decision's area ("screens covered", WAY-86) describes a target product.

### WAY-02 (38-69)
Binding: "Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to that identifier. A reference that relies on the entry's current binding part carries its fingerprint (`WAY-17@<fingerprint>`), and when the fingerprint changes, a script working on plain text files flags that reference for review; a bare identifier and a reference to a version (`WAY-17/2`) are never flagged."
Verification: "level 1 — invariants: decision-guard-stale-reference · decision-fingerprint-input · log-reference-target · relation-fingerprint-value · fingerprint-definition."
Rejected: "impact analysis by a language model — nobody knows what it missed; a fingerprint of the whole entry — every rationale fix flags all references".
TENSIONS: (a) WAY-02 already covers "documents", so guidelines' references are within its reach — supports the form script. (b) WAY-02 says the script "flags that reference for review"; the design says a changed reference "stops the merge". WAY-31 does exactly that for relations (merge carries renewed fingerprints), but only for decisions and invariants. **Interpretation:** stopping the merge for guidelines needs a new decision deriving from WAY-02/WAY-31 and an invariant in the product (see WAY-34). (c) "a bare identifier and a reference to a version ... are never flagged" — if the form script requires *every* reference in a guideline to carry a fingerprint, it narrows WAY-02's allowed bare/version references; needs `narrows WAY-02@3ffcbd46` or a rule that only references relying on the binding part are fingerprinted. (d) Glossary terms carry no fingerprint (WAY-94), so guideline references to terms cannot be fingerprint-checked.

### WAY-04 (95-135)
Binding: "A product's foundation has five elements, and the list is closed: invariants, decisions, a glossary of product terms, a part map, and environment facts. A new pattern enters the foundation only as a field or a rule of one of the five, and only when a mechanism keeps it without human memory: a test, a lint, a check that stops a merge, a mandatory relation or configuration. What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state; rules are written by hand: what is allowed, how bad a failure would be and what the product promises, which the code cannot show."
Verification violates: "a hand-written architecture document appears next to the part map; a hand-written list of the product's endpoints kept next to the code".
Rejected: "a hand-written architecture document or diagram — a second copy of the map".
TENSIONS: **Interpretation:** WAY-04 is unchanged and guidelines stay outside the foundation — consistent with the closed list. But (a) the glossary defines "foundation" as "the written record of the rules the product holds itself to, of what those rules stand on and of where the product breaks them" (glossary.md:86) — a guideline that states rules ("no hard-coded values") is, by that definition, part of the foundation; guidelines must hold only how-to and references to rules that live in decisions/invariants. (b) A styleguide that lists token values or components copied from the tokens file is "a hand-written copy of the state" (the rationale: "a hand-written copy of the state goes stale"); token tables must be pointed to or derived (WAY-53), not transcribed.

### WAY-08 (203-232)
Binding: "Every invariant names its method of checking, and its current result comes from running that method, never from a status written by hand. The default method is a test in the broad sense — a code test, an end-to-end test or an exploratory test run by an agent on the working product — and a test counts only when a deliberately introduced break of the invariant makes it fail, in k of n runs, which its method's command sets and records as one verdict, for a test that does not give the same verdict every time. Human inspection is used for assessments that neither an automated check nor a repeatable measurement can settle, and it leaves a trace of who checked and when."
Verification: "complies: a person settles whether an image's text alternative describes it, after the accessibility check marked it incomplete; violates: an invariant that a repeatable measurement can settle is left to human inspection."
Rationale: "even accessibility tools hand uncertain cases to a person."
Bearing: contrast (computable) must be an automated check; "visible focus on every control" needs an end-to-end/exploratory test on the running product (k of n if flaky), human inspection only for the residue.

### WAY-09 (234-303)
Binding (opening): "On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository` — `elements/<element>/` for each foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`, `installation/`, `agent-instructions/`, `instruction-files/`, `project-level/` and `task-cycle/` — ... A directory reaches the main branch only once it holds what its part requires: ..."
Verification violates: "a `tools/` directory for shared scripts reaches the main branch".
Rejected: "one `tools/` directory for everything shared — it matches no part and grows into a store".
Invariant: repository-file-location/1 (quoted in §3).
CONTRADICTION: a guidelines template, a styleguide template, a styleguide skill and a form script must sit in a directory WAY-09 names. None of the listed directories holds "guidelines" (elements/ is for the five elements; `elements/common/` holds "the skills that find entries and that critique proposals"; `instruction-files/` holds the principles of instruction files; `agent-instructions/` is the-way's own instructions). **Interpretation:** either a new WAY-09 version adds a directory (and a part to part_map.md, with the glossary collision of WAY-93), or an existing directory's list in WAY-09 is extended — both need a new WAY-09 version; placing them without it fails repository-file-location.

### WAY-12 (384-412)
Binding: "A decision is checked through the invariants derived from it, which its *Verification* names by the identifiers of their entries, and tests live only with invariants."
Violates: "a decision whose rule a lint check could enforce is left at level 2."
Bearing: the WCAG adoption decision proposed by the skill must name the contrast and focus invariants at level 1, and each must name it in *Derives from* (level-one-decision-invariants, verification-invariant-derivation). "No hard-coded values" is lint-enforceable, so the decision behind it cannot stay level 2.

### WAY-16 (480-505)
Binding: "The gate takes its checks from the methods of checking written in the entries, never from a list written by hand, and one command runs the checks a change calls for together with the product's own tests it calls for — the same command for an agent, for a human and for whatever runs it when a change is merged."
Violates: "the instructions for agents list test and lint commands of their own; the product's tests run under a command of their own beside the gate's."
Invariant: ci-checking-commands/1 "No CI configuration git tracks runs a checking command other than the gate's command."
TENSION: the form script "stops the merge" only legitimately as the method of an invariant the gate runs; a separate CI step or a lint command named in the product's AGENTS.md violates. The AGENTS.md line forbidding hard-coded values must not name its own lint command.

### WAY-17 (507-529)
Binding: "Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional: a decision and an invariant name the environment facts they rest on, an invariant derived from a decision names that decision, and a check names its invariant."
Bearing: WCAG criterion facts -> adoption decision (*Based on*) -> contrast/focus invariants (*Derives from*, *Rests on*) -> checks (`invariant:` lines). Guidelines are the dependent end of their references, so the reference is written in the guideline (consistent).

### WAY-18 (531-561)
Binding: "A product keeps all its decisions in one log, whatever they are about."
Violates: "a separate log for business decisions next to the technical one."
TENSION (**interpretation**): a styleguide template with a section of design decisions carrying their own reasons would be a second log; design choices go to decisions.md, the styleguide references them.

### WAY-21 (623-643)
Binding: "A decision's scope names the parts of the product it governs, taken from the part map, and never file paths, so that the decisions governing a change are found from the files it touches through the part map's rule for assigning files."
Bearing: product styleguide decisions are scoped to the product's UI part(s); agents touching view files find them through the map (and WAY-52 path rules) even without reading the styleguide.

### WAY-22 (645-671)
Binding: "An invariant says nothing about why or what was rejected; a decision is a choice between options, with its rationale, and it binds later choices, including those that cannot be checked on a commit — direction, trade-off principles, non-goals. A rule that records a choice is a decision, and what of it a commit can make false is written as an invariant derived from it; a rule with no choice behind it is an invariant alone."
Violates: "a non-goal that a commit can break is left without a derived invariant".
Rationale: "a checkable rule left only in a decision's prose escapes the gate".
TENSION (**interpretation**): the same holds a fortiori for guideline prose — every guideline sentence a commit can falsify must be an invariant; every choice behind a guideline must be a decision; the guideline keeps only the how and the reference.

### WAY-26 (737-761)
Binding: "Each trade-off principle is a decision of its own, whose binding sentence says which of two good things is chosen when they conflict and whose rationale names the problem it solves. Each non-goal is a decision of its own that says what the product does not do and why."
Violates: "a principle naming one good thing only ("we value quality"); several principles or several non-goals in one entry."
TENSION (**interpretation**): "design principles" are a usual styleguide section; if binding, each is a separate decision, and the styleguide template must not host a principles list.

### WAY-28 (794-824)
Binding: "When the process enters a product that already exists, the existing state is its starting point and needs no justification, and the rules apply to changes from then on. ... Decisions are recovered only when a task touches the parts they govern."
Violates: "an agent recovers from the code decisions for the whole product before any task touches them".
Rationale: "decisions recovered in advance tempt an agent to invent reasons that look like decisions."
TENSION: the "audit of a product with screens" mode. **Interpretation:** an audit that writes decisions about the existing design (palette, type scale, spacing) for the whole UI in advance of tasks contradicts WAY-28, unless it runs as a task that touches the UI part and the human chooses what to keep.

### WAY-29 (826-855)
Binding: "A decision recovered from an existing product records in *Origin* what was searched and what was found, and its rationale and rejected options are quoted from that source, given by a human who knows them, or written as `unknown`. A rationale an agent proposes for a human's decision goes to the human as a question, never into the entry; the rationale of a decision an agent takes in a task is the agent's to write."
Violates: "an agent writes a plausible reason inferred from the code into the entry; an agent lists in *Rejected* the options it infers were weighed."
Bearing: audit mode cannot write "why this palette" from the screens; `unknown` or the human's words.

### WAY-31 (891-924)
Binding: "A relation `derives from` or `narrows` relies on the binding part of the decision it names and carries that decision's fingerprint ..., and an invariant entry's *Derives from* and *Rests on* carry the fingerprint of each entry they name, while its *Part* carries none. A change to the fingerprint of an entry so named reaches the main branch together with every decision that relates to it with a fingerprint and every invariant carrying it, each checked against the new binding part and carrying the new fingerprint."
Violates: "a script renews every old fingerprint in the log or `foundations/invariants.md` with no one reading the entries that carry them."
Rejected: "flags left open on the main branch — an entry in force on unchecked ground".
Bearing: the model for "a reference whose entry changed wording stops the merge". Scope is decisions and invariants only — extending it to guidelines needs a decision. The violates line also forbids a "renew all fingerprints" helper in the form script.

### WAY-34 (983-1010)
Binding: "A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit. A newer version of the process enters a product only through a task in the product that moves the pin."
Verification: "the invariants of this decision belong to each product's foundation, since no commit of the-way decides them".
Rejected: "templates and scripts copied into each product — the copies drift."
TENSIONS (**interpretation**): (a) The invariant "every guideline's fingerprinted reference matches the current entry" is about the product's files, so like WAY-34's own invariants it belongs to each product's foundation — the-way can ship the script but not the invariant entry; who writes that entry into the product (installer installs only "empty foundation files" per the installation-command surface) is open. (b) Installing a copy of the guidelines/styleguide template into the product is a copy; the product's styleguide is an instance, but a template copied verbatim to be filled would drift from the pinned one.

### WAY-35 (1012-1044)
Binding: "An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them, each citing the decision that sets it; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them."
Violates: "the skill restates the list of fields."
Bearing: the styleguide skill is not an element skill (WAY-35 does not bind it), but writing entries "through element skills" complies; by analogy rules of guidelines' form belong in the guidelines template (checked by the form script), each citing its decision, not in the skill.

### WAY-36 (1046-1073)
Binding: "A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work, or in the choices of its cycle record where no plan is written."
TENSION (**interpretation**): a "gradual cleanup" rule that ends when the cleanup ends (a transition between two states) must not become a decision. The `{fork-point}` companion is an invariant, not a decision, and stays true after cleanup ("no change adds a hard-coded value against `{fork-point}`") — compatible as long as it is not phrased as a transition rule.

### WAY-38 (1102-1130)
Binding: "Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, and the commands a product declares in its own repository — a dependency graph, a detector of breaking changes, coverage — reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement."
Rejected: "the scripts parsing other languages themselves — tools that tried gave it up (cargo-semver-checks)."
Invariants: script-imports (rests on python-stdlib-modules), script-subprocesses "No script git tracks starts a program other than git or a command the product declares in its repository."
CONTRADICTION risk (**interpretation**): the form script (Markdown) is fine. But if the-way ships a checker for "no hard-coded values in view files" or for contrast that parses CSS/JSX/Vue/TS, it parses other languages — rejected. Such checks must be the product's own tests in the product's language, or a product-declared linter read through an adapter, reporting `unchecked` where none is declared. A tokens file in JSON can be read with stdlib `json`; tokens in CSS custom properties cannot without parsing CSS.

### WAY-44 (1233-1262)
Binding: "... the files that serve the whole repository — the lockfile and the build configuration — are a part of their own, and the files that only direct whoever carries out its tasks — instructions for agents, skills, hooks and the configuration of agents' tools and of CI — are another. For a file that collects entries about many parts, the parts a change touches follow from the entries it adds or changes, not from the part the file itself belongs to."
Bearing: places guidelines in the product's agent-directing part (as the design says). **Interpretation:** the tokens file is product code (UI part), not guidelines; a styleguide also read by human designers still "directs whoever carries out tasks". In the-way itself the new template/skill/script are not files directing work on the-way, so they do not belong to `agent-instructions` (see WAY-09).

### WAY-46 (1290-1329)
Binding (part): "an obligation from a law or a contract that raises the criticality of a part enters the part map as a failure mode of that part, whose detection names an invariant resting on the environment fact of that obligation."
TENSION with WAY-86 below (**interpretation**): where an accessibility law applies (e.g. a product sold in the EU under an accessibility act referencing a WCAG-based standard), WCAG is not a voluntary adoption but a binding rule: failure mode at the UI part + env fact of the law; the skill must ask which applies instead of always proposing "a WCAG adoption decision".

### WAY-51 (1428-1462)
Binding: "On the main branch the part map holds its allowed dependencies together with a listed debt: ... an invariant the product does not meet stands, by identifier and current version, on the derived list `foundations/violated_invariants.md`. ... A row of either list is added only by a change of the foundation that a human accepts, never by a step of implementation, and the state a product is in when this process enters it goes onto the list of known violations once."
Rejected: "the rule weakened until the code fits it — the foundation describes the accident (WAY-04); ... a rule left out or marked "not checked yet" until met — the gap stops being countable; debt paid by an end date — repaid by weakening the rule; a list any step may grow (Packwerk) — it outgrows the will to empty it".
Bearing: the sanctioned route for an audited product: "no hard-coded values in view files" written whole, listed as violated (human-accepted), plus the `{fork-point}` companion keeping new changes clean. CONTRADICTION if the companion *replaces* the whole rule (rule weakened to fit code) or if the main rule is left out until cleanup ends.

### WAY-52 (1464-1488)
Binding: "From the part map a product generates for its agents only rules pinned to path patterns: a part's responsibility, its allowed dependencies, and the binding sentences of the decisions whose scope names that part, written into the rule channels the tools already read. ... No overview of the repository is generated for an agent."
Rejected: "rule files written by hand — a copy of the map; the whole decision log on every path".
TENSION (**interpretation**): the binding sentences of UI-scoped decisions already reach agents through generated path rules; a styleguide restating them is a hand-written second copy. The styleguide must reference, not restate, and the "no hard-coded values" rule for view files has a native channel (path-pinned rules), not root AGENTS.md.

### WAY-54 (1513-1544)
Binding: "The value of a field is read off the product wherever a tool can read it, and a template asks for what a value follows from rather than for the name of a value; a value that a closed list of the template does not hold is a question to the human, never the nearest value on the list. A template marks where the value of each field comes from, part by part where a field's parts come from different places: read off, where a tool gives the value; transcribed, where a human copies it unchanged from a record outside the product; resting on a judgment, where it is neither."
Violates: "a field that rests on a judgment stands beside fields that are read off, with nothing saying which is which".
TENSION (**interpretation**): scope is the five elements and elements-common, but the sentence speaks of "a template". If applied to the guidelines/styleguide templates, every field must be marked; token values are read off the tokens file (so not written into the styleguide by hand), principles rest on judgment.

### WAY-60 (1697-1731)
Binding: "A condition deciding an invariant stands in its sentence, or where changing it takes a foundation change a human decides, or where a decision in the product's log or the pinned the-way places it. An invariant's sentence names no branch, measures any change it speaks of against `{fork-point}` (WAY-61), while a state it compares may be the one on `{merge-onto}` ... A sentence bounding or equating a quantity measured while the product runs names its bound or tolerance, statistic and population."
Violates: "every request is answered within the limit set in `config.py`"; "a sentence measuring a change against `{merge-onto}`."
CONTRADICTION risk (**interpretation**): (a) "view files" — which files are view files — cannot be defined in the styleguide or a lint config the product edits freely; it must be in the sentence, in the part map (a part's patterns; changing it is a foundation change) or in a decision. (b) "contrast of background/text pairs computed from the tokens file" — which pairs count and the threshold (4.5:1 / 3:1) cannot be set by the tokens file itself; the threshold comes from the WCAG fact/decision, the pair list from the sentence or a decision. (c) The companion "measured against `{fork-point}`" complies.

### WAY-61 (1733-1785)
Binding (part): "A method checks what its sentence is about, as it stands on the commit being checked, so a check fed input made up for it is the method of a sentence about that check, never of one about the data the check reads."
Violates: "a sentence about the real log names as its method the guard's test, which feeds it made-up logs".
Bearing: the contrast invariant's method must read the real tokens file on the commit; the form invariant's method must read the real guidelines and the real decisions/invariants; the form script's own unit tests are not the method.

### WAY-62 (1787-1816)
Binding: "An invariant entry names the parts of the part map where a change can make its sentence false, or `every` where a change to any part can. A change ... reaches an invariant that names `every` or a part the change touches, or whose method names a file the change alters ..."
Violates: "that sentence names `part-map`, so a file added under `gate/` never reaches it".
Bearing (**interpretation**): the product's "guideline references are current" invariant is made false by a change to decisions.md or invariants.md, not only by a change to the guidelines; it must name the decisions and invariants parts too (or its method must name those files), else rewording a decision never reaches it.

### WAY-69 (1960-1994)
Binding: "An invariant's sentence, the check that cites it and the code it covers come from three different agents, and the deliberate break the check is accepted on is written from the sentence by the reviewer of that code, who did not write the check. A check that cites an invariant takes the input it asserts on and the value it expects written out, wherever the code its invariant is about would otherwise compute either; only the side it compares against comes from the run."
Violates: "a test builds its reference by calling the code its invariant is about, and expects that call's message; a test reads the value it expects, at run time, from the file its invariant is about."
TENSION (**interpretation**): (a) the skill that writes the first invariants' sentences must not also write their checks or the UI code. (b) The contrast check must hold the threshold as a literal and must not take it (or a "minimum contrast" token) from the tokens file; it must not compute contrast with the product's own colour utilities if those are what the invariant is about.

### WAY-73 (2060-2091)
Binding: "An invariant's *Rests on* names every environment fact holding a condition that decides whether a commit makes its sentence true, and no other fact. ... A fact that is only a reason for a decision the invariant derives from stands in that decision's *Based on* alone; every environment fact on the main branch is named by an invariant's *Rests on* or by a decision's *Based on* ..."
Violates: "an invariant bounding a page's load time by an outside standard's threshold reads `Rests on: none`."
Bearing: the contrast invariant rests on the WCAG contrast criterion fact (it copies its ratio); focus visibility rests on the focus criterion fact. The-way's environment_facts.md holds no WCAG fact today; these are product facts.

### WAY-80 (2240-2273)
Binding: "Every environment fact entry names its source: an edition with its publisher's own address, or a page without editions with its closest archived copy, giving the place, the passage word for word and the date read ... The sentence says no more than its source, and a model's memory, an agent's paraphrase or a text quoting the source is no source."
Violates: "the source is the model's recollection of a page, or a blog post quoting the RFC".
Bearing: the skill's WCAG facts need the dated W3C edition URL and quoted passages (e.g. success criterion text); with no network the skill must leave `TODO`.

### WAY-86 (2442-2474)
Binding: "A voluntary catalogue of requirements binds a product only through a decision adopting it that names the catalogue, its edition, the level or list taken and the area of the product, and a requirement an invariant takes a condition from is an environment fact. A binding rule — a law, a contract, a licence — needs no adoption: what it requires is an environment fact, and the product is held to it until a human settles, in a decision, that the rule does not apply. An agent that notices a likeness to a requirement nothing has adopted or applied asks a human."
Verification complies: "a decision adopts WCAG, naming its edition, level AA and the screens covered; an invariant taking a criterion's condition rests on that requirement's environment fact".
Violates: "an agent writes an invariant from an ASVS requirement because the code looks like it, with no adopting decision".
Bearing: the proposed WCAG adoption decision is the decision's own complying example. Order matters: the contrast/focus invariants cannot enter before the adoption decision. TENSION: see WAY-46 — if a law applies, no adoption is needed and the framing changes.

### WAY-93 (2538-2570)
Binding: "Terms are a space of their own, and a change that makes a term read like an identifier of the part map, the invariants or the environment facts is a warning, after which one side is renamed where the two name different things; in the-way, a term that names an element raises none against the part whose files include `elements/<identifier>/`."
TENSION (**interpretation**): if the-way adds a part named `guidelines` (for the template/skill/script) and a glossary term "guidelines" (the product document), they read alike and name different things, and the element exemption does not apply → warning and a rename.

### WAY-95 (2606-2650)
Binding: "A word takes a glossary entry when it stands in the binding part of an entry of the foundation or in the rules of an element's template or of the part the elements share, and at least one of its uses ... carries a meaning a reader who knows the product's field would not give it ... The glossary of the-way holds the words of the process, and a product's glossary holds the words of its domain; a product takes the words of the process from the-way at the commit it pins and defines none of them again ..."
Bearing (**interpretation**): "guidelines" in the narrow sense given (hand-written product document outside the foundation, directing agents in one domain) is not the field's plain meaning, so once a binding sentence uses it the-way's glossary needs an entry; products may then not define it (glossary-process-terms).

### WAY-97 (2686-2720)
Binding (part): "A sentence of a foundation entry that speaks of what a glossary term defines uses the term, never a paraphrase of its definition ... A glossary entry carries no version and is edited in place ..."
Bearing: new decisions say "guidelines", not "a product document that directs agents"; guideline references to glossary terms cannot be fingerprint-checked by the form script.

### WAY-100 (2788-2812)
Binding: "A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule."
Violates: "a skill makes an outside planning ritual mandatory because an agent recognizes it, without a decision adopting it."
Bearing: design tokens, a tokens file format (e.g. a community format), "styleguide" practice, Cursor-style scoped rules — each borrowed piece the-way makes mandatory needs an adopting decision; in a product, the skill offers these as proposals.

### WAY-102 (2837-2862)
Binding: "The-way is a process for work on a technology product in which a change of premises or direction is an ordinary step: it passes through the product's foundation and needs no memory of what is linked to what."
Violates: "a change of direction relies on the author remembering which decisions and documents to update."
Bearing: the reason guidelines need fingerprinted references and a merge-stopping check — a hand-written document outside the foundation otherwise relies on memory.

### WAY-104 (2889-2941)
Binding (part): "A word of a product's domain that the glossary of the-way holds at the commit the product pins, or the last word of a term it holds, in any of its forms, is written in the files of the product's `foundations/` with a qualifier ... The product's code, its interface and talk about the product use the word of the domain unchanged."
Bearing (**interpretation**): if "guidelines" (or a multiword term ending in it) enters the-way's glossary, a product whose domain uses "guidelines" (e.g. a clinical or brand product) must qualify it in its foundation. Low practical risk; mention in the glossary entry decision.

### WAY-106 (2992-3016)
Binding: "The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries."
Violates: "the definition writes the future decision into the product's foundation".
TENSION (**interpretation**): if "before the first screen" runs inside defining a project (the natural moment), the skill may only project entries (WAY-117), not write them; writing happens in the first task's foundation step (WAY-126).

### WAY-107 (3018-3042)
Binding: "A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns."
Violates: "puts the product's paths inside the installer's marked block."
Rationale: "Keeping the place outside the generated block lets the product change it without editing the process's installed guidance."
TENSION (**interpretation**): the product's AGENTS.md "points to the styleguide". If the installer writes that pointer (with the styleguide's product path) inside its marked block, it repeats the pattern WAY-107 rejects for the backlog; the pointer belongs outside the block, or the block names a fixed the-way convention path.

### WAY-113 (3181-3215)
Binding: "An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way."
Bearing: the styleguide conversation's questions follow this form (ways, costs, recommendation; one challenge after a choice enters a binding part). No conflict.

### WAY-114 (3217-3244)
Binding: "A human accepts the meaning of a foundation entry, shown as one sentence in the human's language with the entry beside it, while its wording is the agent's: an agent writes the entry and the human accepts it at the merge of the change that holds it, or, for a projected entry, at the readiness gate. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation."
Violates: "an agent asks the human to confirm a choice it already recommends".
Rejected: "acceptance of the whole wording before an entry is written — attention goes to wording while the meaning rarely moves, and each acceptance costs a round".
CONTRADICTION (explicit): the skill "asks even where it has a recommendation". Scope of WAY-114 includes decisions, invariants, glossary, part-map, environment-facts, elements-common, project-level — the skill writes product entries through element skills, so it is bound. Precedent for a departure: WAY-134 carries `narrows WAY-114@04b4f599`. A new decision must `narrows WAY-114@04b4f599` and state the area (styleguide choices of taste/brand where the human's preference is the source). **Interpretation:** questions about guideline content that is not a foundation entry (e.g. tone of examples) are outside WAY-114 entirely; the narrowing is needed only for questions that lead to entries.

### WAY-120 (3395-3425)
Binding: "An agent may invoke critique for any proposal without waiting for the human to express doubt; a completed set for collective human review and every change to an invariant test or to the foundation go through it, and for such a change the critique is its independent assessment (WAY-10). ..."
Bearing: the styleguide's set of proposals (decisions, first invariants, facts) shown together goes through one critique; the product foundation change it produces needs its independent assessment record.

### WAY-121 (3427-3503)
Binding (part): "A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up; a choice one task can make and change alone stays with that task. As an exception to that rule, where the project brings behaviour a user sees in the running product, the step looks at three matters of an agent's way to the running product — its logs, its interface and its development data ..."
Verification complies: "a project that changes only how a screen looks, in a product whose foundation already says how an agent reaches its screens, records that the foundation holds every choice it needs"; violates: "a project that brings a product's first screen leaves out how an agent operates it ..."
TENSION (**interpretation**): a styleguide's tooling choices (CSS framework, component library, token build tool) are technology choices that can change the cut of work — they belong to settle-technology, not to the styleguide skill. "Before the first screen" overlaps with the first project's interface matter; the styleguide skill must read/require that decision rather than settle it.

### WAY-122 (3505-3562)
Binding (part): "The options of each technology choice a project needs come from research of that choice against the project definition, rather than from a fixed list of bundled stacks ... and every option is offered only after a critique that refutes every claimed difference between the options which no source supports."
Rejected: "options from research shown unchecked — the human cannot tell a sound comparison from an invented one".
TENSION (**interpretation**): scope is project-level/decisions and "technology choice"; "researches with WAY-122 discipline" borrows it for a non-technology domain — the binding properties (explicit types, conventions, versioned docs, wide use) do not fit palettes or type scales. A new decision must say which part is taken (research per choice, sourced differences, critique before the human sees options) and derive from WAY-122.

### WAY-123 (3564-3601)
Binding: "The step that settles a project's technology shows the options of each choice by their consequences for the product ... A difference with no consequence for the product decides nothing, and where no difference with a consequence remains, the step recommends the simplest and cheapest option. ... each with its recommendation and the weak point of the option recommended."
Bearing: if borrowed, styleguide options are shown by consequences (maintenance, accessibility, brand fit); "taste" differences without consequence decide nothing — which sits uneasily with asking the human even where the agent recommends (WAY-114 departure). **Interpretation:** the design must say whether brand/taste is a consequence.

### WAY-127 (3762-3819)
Binding: "A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. ..."
Bearing: the new skill needs `python -B agent-instructions/skill_entry_points.py --write`; invariant skill-entry-points (quoted in §3).

### WAY-128 (3821-3861)
Binding: "A line for a file that an agent's tool loads into every session — one the skill of `instruction-files` proposes, or one a change to the-way's repository instruction files adds or rewords — is one that every session needs or that points to work an agent would not otherwise find, that an agent could not read from the repository or from general knowledge, and without which an agent would go wrong. Any other rule the skill proposes or such a change adds stands where what calls for it reaches the agent: a rule for some files in a file the tools load with those files, a rule for an activity in the steps of the skill that carries out that activity or in the file that leads it, and knowledge needed now and then in a file such a step or line points to."
Rationale: "Process skills and their entry points answer to their own decisions (WAY-35, WAY-127), not to this one."
TENSION (**interpretation**): "no hard-coded values in view files" is "a rule for some files" — by WAY-128 it belongs in a path-scoped rule file, not in the root AGENTS.md loaded into every session. WAY-128 formally binds the instruction-files skill and the-way's own files, not the installer's block (WAY-132), but a design that puts the rule in AGENTS.md contradicts the-way's own principle. The styleguide itself fits "knowledge needed now and then in a file such a step or line points to" — complies.

### WAY-129 (3863-3887)
Binding: "The-way's repository instruction files hold no `@` import other than the line `@AGENTS.md` alone at the top of the root `CLAUDE.md`, and the skill of `instruction-files` proposes none other. A pointer the skill proposes, or a change to the-way's repository instruction files adds, names the file to read by its path in backticks with the condition under which to read it."
Violates: "a pointer reads "See @docs/style.md for the style"".
Bearing: the AGENTS.md pointer to the styleguide is a backticked path with a condition ("Before you change a screen, read `…`"), never `@`.

### WAY-130 (3889-3927)
Binding: "The skill of `instruction-files` proposes a rule, and a change to the-way's repository instruction files adds one, only to remove a mistake agents made more than once, found in records of their work, and names that mistake where it proposes or adds the rule, unless the rule carries a decision the repository records or a step of an activity in the file that leads that activity. ..."
Violates: "a rule added "just in case" after one slip recalled from memory".
TENSION (**interpretation**): the AGENTS.md rule forbidding hard-coded values is added before any recorded mistake; it is admissible only because it "carries a decision the repository records" — so the product decision (tokens over literals) must exist before the line is added. Also, by the glossary, a styleguide named by path from root AGENTS.md is itself a "repository instruction file" (see §5), so each of its rules is judged by WAY-128–131 when the instruction-files skill reviews the product; the guideline-to-decision reference requirement is what lets those rules pass WAY-130.

### WAY-132 (3961-3997)
Binding: "The skill of `instruction-files` proposes for a repository whose agents use more than one of Claude Code, Codex and Cursor, and the-way keeps for itself, a root `AGENTS.md` that carries the instructions those tools share and a root `CLAUDE.md`, where there is one, whose first line is `@AGENTS.md` alone and which holds only what Claude Code alone needs. The skill leaves out of this proposal the files and the marked block the-way's installer writes in a product."
Rationale: "What the installer writes in a product answers to the installer's own surface and stays outside this decision."
Bearing: changes to the installer's AGENTS.md block are changes to the `installation-command` surface (part map), not governed by WAY-128–131.

### WAY-133 (3999-4032)
Binding: "Where a rule of an instruction file has to hold every time, the skill of `instruction-files` proposes a mechanism that keeps it without the agent choosing to — a CI check, a linter, a check of a step's output, or a local git hook where the rule guards against slips rather than against an agent that can turn the hook off — and a change to the-way's repository instruction files adds such a rule only with its mechanism. The instruction file then says what the mechanism is for, or carries what the mechanism cannot check."
Violates: "a change adds a rule that has to hold on every commit only as a line of `AGENTS.md`".
Bearing: the AGENTS.md "no hard-coded values" line must come with its invariant's check (run by the gate, WAY-16) and say what it is for; complies only if the invariant exists in the same change.

### WAY-139 (4303-4340)
Binding: "The-way holds no skill of a product, only the list of what a product's deployment skill covers ..."
Rejected: "a document of operations kept beside the product — no step reads it, so it goes stale unread; the list in a template alone — nothing binds the refinement to check it."
Violates: "the list stands only in a template, and the decision points to it."
TENSION (**interpretation**): two precedents. (a) A product document "no step reads" goes stale — the styleguide needs a step that reads it (AGENTS.md pointer, task refinement, path rule) and a check (form script). (b) A list the process requires should stand in a binding sentence, not only in a template — but WAY-142 deliberately keeps columns in the template "so that a change to them needs no new version". The design must say which precedent the guidelines template's required sections follow; with a form script checking the template, WAY-142's route is defensible.

### WAY-141 (4397-4419)
Binding: "When a product has no root `CLAUDE.md`, the installer creates one whose sole line is `@AGENTS.md` ... The installer writes no `.claude/rules/the-way.md`."
Rejected: "a generated rule repeating the installer's block — it duplicates guidance without carrying the product's other instructions".
Invariant: installation-claude-guidance/1 (quoted in §3).
TENSION (**interpretation**): if the design moves the hard-coded-values rule into a path-scoped rule (per WAY-128), the installer may not write it as `.claude/rules/the-way.md`; a differently named installer-written rule file is "a second rule file" (installation part's failure mode: "the installer omits the root Claude import or its warning, or writes a second rule file — Claude Code misses the product's instructions or receives duplicate guidance"). Generated path rules from the map (WAY-52) are the native channel.

### WAY-165 (5345-5390)
Binding (part): "... the interface asks how an agent operates the product as its user does — through a screen in a browser, a call to its API or a command in a terminal — and how it sees what the product answers."
Bearing: the "visible focus on every control" invariant's check needs an agent or test operating the UI as a user (keyboard navigation in a browser); its method depends on the product's interface decision. The styleguide skill should require that decision rather than invent a method.

---

## 3. Invariants (invariants.md)

210 entries, plus three tables at the end (lines 2133-2148): Withdrawn identifiers (2 rows), Quarantined invariants (empty), Recovered invariants (empty).

### 3.1 Invariants whose *Part* names decisions, glossary, part-map, invariants, agent-instructions, installation, repository, elements-common, gate or `every`

(No invariant names a part `instruction-files`; parts `relation-model`, `environment-facts`, `project-level` listed only where combined with the above.)

| Identifier | Part | Gist |
|---|---|---|
| decision-guard-stale-reference/1 | decisions · relation-model | guard reports relations whose fingerprint differs from the named decision's current one on merge |
| decision-fingerprint-input/1 | decisions · relation-model | decision fingerprint = binding sentences only |
| log-reference-target/1 | decisions | every decision number referenced exists |
| foundation-file-kinds/1 | every | every file in `foundations/` holds one element's entries or is named by a template/common part |
| binding-sentence-count/1 | decisions | 1-3 binding sentences |
| binding-sentence-words/1 | decisions | no forbidden words in binding sentences |
| decision-example-numbers/1 | decisions | examples.md decision numbers exist |
| decision-template-change/1 | decisions | template change adds a log version |
| foundation-change-merge-route/1 | every | foundation-altering commits on merge-onto are merges |
| log-existing-lines/1 | decisions | log keeps fork-point lines |
| log-versions-added-per-number/1 | decisions | at most one new version per number |
| log-merge-copies/1 | decisions | shared versions identical with merge-onto |
| invariant-method-form/1 | every | method is program-led command, existing path, or TODO |
| invariant-test-break/1 | every | checks fail on their deliberate break (k of n) |
| repository-file-location/1 | every | tracked files only in WAY-09 directories (quoted below) |
| element-directory-contents/1 | decisions · part-map · invariants · glossary · environment-facts | element dir holds template, examples, skill, guard |
| invariant-example-target/1 | invariants | examples name existing invariants |
| map-example-target/1 | part-map | examples name existing map entries |
| glossary-example-target/1 | glossary | examples name existing terms |
| foundation-change-assessment-record/1 | every | no foundation/invariant-test change without independent assessment record |
| return-step-record/1 | every | every change holds its return-step record |
| decision-verification-level/1 | decisions | level of verification named |
| level-one-decision-invariants/1 | every | level-1 decision has a deriving invariant |
| verification-invariant-derivation/1 | every | level-1 named invariants derive from the decision |
| foundation-change-path/1 | every | foundation-altering change not on no-foundation path |
| decision-approval-record/1 | decisions | Approved by: who + date or merge |
| decision-approver/1 | decisions | approver is Mariusz |
| derived-file-content/1 | every | derived files equal generator output |
| derived-subset-naming/1 | decisions · part-map · invariants · glossary · environment-facts | subset-compared derived files named in template |
| ci-checking-commands/1 | every | CI runs no checking command but the gate's |
| gate-check-source/1 | every | gate checks come from entries' methods |
| view-versions/1 | every | view of decisions in force: latest versions |
| view-links/1 | every | view shows links at both ends |
| decision-heading-form/1 | decisions | heading form |
| decision-version-sequence/1 | decisions | consecutive versions |
| decision-change-kind/1 | decisions | kind of change from list |
| decision-binding-across-versions/1 | decisions | unchanged-sentences/challenge keep sentences |
| repeal-binding-sentences/1 | decisions | repeal has none |
| decision-scope-names/1 | every | scope names are map parts |
| decisions-found-for-change/1 | every | decisions found include all scoped to touched parts |
| review-when-form/1 | decisions | state and date |
| decision-guard-overdue-review/1 | decisions | warns on passed check-by dates |
| review-next-check/1 | decisions | review record next check |
| review-named-version/1 | decisions | named version exists |
| narrows-pairs/1 | decisions | no mutual narrows |
| outbound-link-reach/1 | every | no links to unreachable repos/private notes except Backlog |
| inherited-origin-form/1 | decisions | inherited Origin form |
| inherited-rationale-source/1 | decisions | inherited rationale unknown/quoted/attributed |
| relation-fingerprint-presence/1 | decisions | fingerprint iff derives from/narrows |
| relation-fingerprint-value/1 | decisions · relation-model | relation fingerprints current on merge (quoted below) |
| relation-type/1 | decisions | two relation types |
| foundation-search-record/1 | every | foundation change needs both search records |
| skill-rule-source/1 | decisions · part-map · invariants · glossary · environment-facts | element skill names template + common as rule source |
| script-language/1 | every | every script is Python |
| script-imports/1 | every | stdlib 3.14 or tracked Python only |
| script-subprocesses/1 | every | only git or product-declared commands |
| map-guard-missing-command/1 | part-map | missing declared command = unchecked |
| map-entry-kinds/1 | part-map | part, flow, surface |
| map-section-kinds/1 | part-map | no other sections |
| part-map-file/1 | every | exactly one part map |
| map-identifier-form/1 | part-map | identifier form |
| identifier-holders/1 | part-map · invariants · environment-facts | identifiers unique across map/invariants/facts |
| map-reference-target/1 | every | referenced map ids exist |
| map-withdrawal-successors/1 | part-map | withdrawn ids give why + successors |
| map-identifier-persistence/1 | part-map | fork-point ids persist |
| map-fingerprint-input/1 | part-map · relation-model | map fingerprint = binding sentence |
| map-entry-version/1 | part-map | no versions |
| file-part-assignment/1 | every | each tracked file in exactly one part or left out |
| path-pattern-reach/1 | every | each pattern matches a file |
| left-out-file-assignment/1 | part-map | left-out files match no part |
| flow-part-names/1 | part-map | flow/depends-on parts exist |
| flow-invariant-link/1 | part-map · gate | flows name invariant; test has `flow:` line |
| map-invariant-names/1 | every | map's invariant ids exist |
| failure-mode-severity/1 | part-map | severity named |
| failure-mode-detection/1 | part-map | detection named or "not detected" |
| part-criticality-field/1 | part-map | no hand-written criticality |
| map-guard-unrecorded-criticality/1 | part-map | no failure modes -> highest |
| map-guard-dependency-report/1 | part-map | criticality computation |
| criticality-lowering-report/1 | part-map | reports lowered criticality |
| flow-coverage-parts/1 | every | coverage parts in flow list |
| map-guard-missing-coverage/1 | part-map | no coverage -> unchecked |
| map-guard-test-runs/1 | part-map | guard starts no tests |
| external-exchange-row/1 | part-map | exchange rows complete |
| gate-boundary-change/1 | gate | crafted-input check on boundary changes |
| surface-promise-level/1 | every | surfaces carry promise level |
| surface-declaration/1 | every | surface declarations exist |
| map-withdrawal-date/1 | part-map | no withdrawal dates |
| promise-level-policy/1 | every | each level has policy |
| surface-change-path/1 | part-map | no per-surface path |
| known-violation-coverage/1 | every | disallowed deps listed |
| known-violations-growth/1 | part-map | list subset of fork-point |
| known-violation-currency/1 | every | rows still real |
| known-violation-fields/1 | part-map | row fields |
| known-violation-line-number/1 | part-map | no line numbers |
| generated-pattern-source/1 | part-map | generated rule patterns from part rules |
| generated-overview/1 | part-map · agent-instructions | no generated repository overview |
| flow-test-location/1 | every | flow tests under gate/ |
| invariant-sentence-count/1 | invariants | one sentence |
| invariant-identifier-form/1 | invariants · elements-common | id form |
| invariant-version-number/1 | invariants | version in heading |
| invariant-version-new/1 | invariants | new = version 1 |
| invariant-version-changed/1 | invariants | changed fp -> +1 or correction |
| invariant-version-unchanged/1 | invariants | same fp keeps version |
| invariant-earlier-wording/1 | invariants | no old sentences kept |
| invariant-citation-version/1 | every | `invariant:` lines cite current version |
| invariant-correction-confirmation/1 | invariants | correction confirmed by human |
| invariant-recovered-form/1 | invariants | recovered rows form |
| invariant-recovered-derived/1 | invariants | recovered entries derive from no decision |
| gate-fork-point-evidence/1 | gate | gate reports pass/break on fork-point for new sentences |
| invariant-fingerprint-input/1 | invariants · relation-model | fp = sentence |
| sentence-branch-names/1 | invariants | no "main branch"/"task branch" |
| sentence-gate-values/1 | invariants | brace values on gate list |
| method-gate-values/1 | invariants | command gate values on list |
| gate-verdict-per-entry/1 | gate | verdict per entry/version |
| gate-pass-without-verdict/1 | gate | no pass without verdict |
| gate-method-order/1 | gate | producer methods first |
| invariant-part-names/1 | invariants · part-map | parts exist |
| invariant-part-form/1 | invariants | `every` or parts, not both |
| change-reach/1 | gate | reached invariants |
| gate-result-values/1 | gate | four results |
| gate-unchecked-reason/1 | gate · invariants | listed reasons |
| gate-missing-script/1 | gate | missing script unchecked/error |
| gate-reported-set/1 | gate | reports reached + flow invariants |
| flow-test-run/1 | gate · part-map | flow tests run every change |
| gate-exit-code/1 | gate | exit-code rule |
| invariants-file/1 | every | one invariants file |
| invariant-identifier-persistence/1 | invariants | ids persist |
| invariant-withdrawal-persistence/1 | invariants | withdrawn persist |
| withdrawal-successors/1 | invariants · elements-common | withdrawn row form |
| invariant-citation-target/1 | every | `invariant:` lines name entries |
| data-line-target/1 | every | `data:` files exist |
| invariant-tests-of-change/1 | gate | invariant tests of a change |
| link-fingerprint-presence/1 | invariants | Derives/Rests names carry fp |
| link-fingerprint-value/1 | every | those fps current on merge |
| violated-list-growth/1 | invariants | violated list subset of fork-point |
| violated-position-version/1 | invariants | violated rows at current version |
| quarantine-position-form/1 | invariants | quarantine row form |
| quarantine-flow-invariants/1 | invariants · part-map | no quarantine of flow invariants |
| gate-quarantine-result/1 | gate | quarantine unchecked then error |
| log-entry-field-presence/1 | decisions | all fields |
| log-entry-field-words/1 | decisions | none/TODO only where allowed |
| log-entry-merge-todo/1 | decisions | no TODO on merge |
| map-entry-field-presence/1 | part-map | all fields |
| map-entry-field-words/1 | part-map | none/TODO allowed |
| invariant-entry-field-presence/1 | invariants | all fields |
| invariant-entry-field-words/1 | invariants | none/TODO allowed |
| invariant-entry-merge-todo/1 | invariants · environment-facts | TODO only Method/Rests on |
| run-record-form/1 | decisions · part-map · invariants · glossary · environment-facts · elements-common · gate | JSONL line keys |
| run-record-path/1 | invariants · environment-facts · repository | `.jsonl` paths git-ignored |
| run-record-lines/1 | gate | gate reads only its run's lines |
| test-runner-pass-line/1 | gate | pass line only when test bodies ran |
| python-version-declared/1 | repository | `.python-version` = 3.14 |
| environment-facts-file/1 | every | one facts file |
| fact-citation-version/1 | every | `fact:` lines current version |
| fact-method-form/1 | every | fact method form |
| fact-citation-target/1 | every | `fact:` lines name entries |
| fact-verdict-citation/1 | gate | verdict only from citing command |
| based-on-fact-fingerprint/1 | decisions · environment-facts | Based on facts carry fp |
| based-on-fact-fingerprint-value/1 | decisions · environment-facts | those fps current |
| gate-fact-run/1 | gate | gate runs touched facts' methods |
| fact-clock-exit/1 | gate · environment-facts | clock exit rule |
| human-verdict-invariant-row/1 | invariants | human verdict rows for invariants |
| gate-human-verdict/1 | gate | when human verdicts count |
| fact-dependants/1 | environment-facts · invariants · decisions | every fact is named |
| glossary-file/1 | every | one glossary file |
| glossary-file-sections/1 | glossary | title, paragraph, entries |
| glossary-term-holder/1 | glossary | unique terms |
| glossary-term-collision/1 | glossary | warns term/identifier read alike (element exemption) |
| glossary-process-terms/1 | glossary · installation | product glossary may not define the-way's terms (quoted below) |
| glossary-entry-field-presence/1 | glossary | fields |
| glossary-entry-field-words/1 | glossary | none/TODO allowed |
| glossary-term-use/1 | glossary · decisions · invariants · part-map · environment-facts · elements-common | each term used outside glossary |
| glossary-definition-count/1 | glossary · decisions | one-sentence definition |
| glossary-definition-words/1 | glossary · decisions | no must/forbidden words |
| glossary-entry-version/1 | glossary | no versions |
| glossary-definition-uses/1 | glossary | changed definition lists uses |
| glossary-avoid-growth/1 | every | Avoid words do not grow |
| glossary-avoid-single/1 | glossary | Avoid word in one entry |
| glossary-avoid-term/1 | glossary | Avoid word not a term |
| glossary-avoid-carrier/1 | glossary | Avoid word not a Not carrier |
| glossary-not-target/1 | glossary · decisions · part-map · invariants · environment-facts | Not targets exist |
| glossary-not-quoted-word/1 | glossary · decisions · invariants · part-map · environment-facts · elements-common | Not carriers hold no term; quoted words used |
| glossary-entry-merge-todo/1 | glossary | no TODO on merge |
| skill-entry-points/1 | every | entry points for every SKILL.md (quoted below) |
| instruction-file-imports/1 | every | no `@` imports in the-way's repository instruction files (quoted below) |
| root-claude-md-import/1 | agent-instructions | root CLAUDE.md begins `@AGENTS.md` (quoted below) |
| installation-claude-guidance/1 | installation | installer CLAUDE.md behaviour, no `.claude/rules/the-way.md` (quoted below) |

### 3.2 Whole entries quoted

**repository-file-location/1** (invariants.md:146)
"Where {merge-onto} exists, every file git tracks lies in `foundations/` or in a directory WAY-09 names for a part of the process, belongs to the `repository` or the `agent-instructions` part of the part map, or is the `README.md` at the root."
- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-09@909e9c5c
- **Part:** every
- **Correction:** none

**skill-entry-points/1** (invariants.md:2065)
"Every file named `SKILL.md` that git tracks, or that stands untracked and not ignored by git, outside the `.claude/` and `.agents/` directories at the repository's root, with `<name>` the name its frontmatter gives, has a file `.claude/skills/the-way-<name>/SKILL.md` and a byte-identical file `.agents/skills/the-way-<name>/SKILL.md`, whose frontmatter names `the-way-<name>` and gives a description starting with the description the frontmatter of that `SKILL.md` gives, whose text contains, in backticks, the path of that `SKILL.md` from the repository's root, and contains `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'`, `git rev-parse --show-toplevel` and the words "If the skill tells you to resolve a link to find the-way, skip that", and whose text holds a sentence that names, each in backticks, the name of every such `SKILL.md` and holds the words "with the `the-way-` prefix, never an unprefixed one"; and every directory in `.claude/skills/` or `.agents/skills/` whose name begins with `the-way-` is named `the-way-<name>` for the `<name>` of such a `SKILL.md`."
- **Method:** `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
- **Rests on:** none · **Derives from:** WAY-127@69651fc7 · **Part:** every
Note: a SKILL.md placed in a product styleguide *template* directory of the-way would also trigger this (any tracked `SKILL.md`).

**Installation-related invariants**
- **installation-claude-guidance/1** (invariants.md:2095): "For a product with no root `CLAUDE.md`, the installation command creates that file with `@AGENTS.md` as its sole line; for a product with an existing root `CLAUDE.md`, it preserves the file byte for byte and warns in the installation plan before confirmation when the file has no effective `@AGENTS.md` import; in neither case does it write `.claude/rules/the-way.md`." — Method `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`; Rests on claude-code-imports@5b9359fd; Derives from WAY-141@5d0990a0; Part installation.
- **glossary-process-terms/1** (invariants.md:1847): "The glossary guard, given a product's glossary, reports as an error every entry there whose term, in any of its forms, is a term the glossary of the-way holds at the commit the product pins or the last word of one, or whose *Avoid* lists, in any of its forms, such a term or last word." — Method `python -B gate/run_tests.py elements/glossary --record .runs/glossary-tests.jsonl`; Derives from WAY-95@455377de · WAY-104@b1f1850d; Part glossary · installation.
- Related surface (part_map.md:343, not an invariant): `installation-command` — "The command that installs a pinned the-way checkout, empty foundation files, project skills, agent guidance for Claude Code and Codex and a `.runs/` ignore line in a product keeps its preview and confirmation, replaces no existing file, and adds to an existing file of the working tree only the `.the-way` section of `.gitmodules`, a marked block at the end of `AGENTS.md` and the `.runs/` line at the end of `.gitignore`." Installing guidelines/styleguide templates or a styleguide pointer changes what this surface promises (level `pinned`: anything allowed, owes "a line in the merge request saying what moving the pin changes for a product").

**Instruction-file invariants**
- **instruction-file-imports/1** (invariants.md:2075): "No repository instruction file of the-way holds, outside code spans and fenced code blocks, an `@` that stands at the start of a line or right after whitespace, `(`, `[`, `{`, `"`, `'`, `“`, `‘` or `„` and is followed by a character other than whitespace, except the first line of the root `CLAUDE.md` when it reads `@AGENTS.md` and nothing else; the root `AGENTS.md` or `CLAUDE.md` names by its path a Markdown file that git tracks, one whose name ends in `.md` or `.markdown`, when that file's path from the repository's root, written with `/` or with `\` between directories, stands anywhere in its text with no ASCII letter or digit and none of `.`, `-`, `_`, `/` and `\` right before it, a code span runs from a run of backticks to the next run of as many backticks on the same line, and a fenced code block runs from a line whose first characters other than spaces are three backticks or three tildes to the next such line." — Method `python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl`; Derives from WAY-129@1336c32b; Part every.
  Bearing: if the-way's root AGENTS.md ever names a guidelines template or an example styleguide by path, that file becomes a repository instruction file of the-way and must hold no `@` import (e.g. "@media" in CSS examples outside code spans would trip it).
- **root-claude-md-import/1** (invariants.md:2085): "Where git tracks a `CLAUDE.md` at the repository's root, its text begins with `@AGENTS.md` followed directly by a line break, `\n` or `\r\n`, or by the end of the text." — Method `python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl`; Derives from WAY-132@1242ac75; Part agent-instructions.
- generated-overview/1 (part-map · agent-instructions): "No file generated for an agent holds an overview of the repository's directories."

**decision-guard-stale-reference/1** (invariants.md:6)
"The decision guard, given "{merge-onto}", reports every `derives from` or `narrows` relation, in the latest version of a decision in the log a merge onto that commit leaves, whose fingerprint differs from the current fingerprint there of the decision it names."
- **Method:** `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
- **Rests on:** none · **Derives from:** WAY-02@3ffcbd46 · WAY-31@a14c616c · **Part:** decisions · relation-model
Note: it reports (is about the guard), and the merge stop itself is relation-fingerprint-value. The part map's critical flow `wording-reaches-dependants` names this invariant.

**relation-fingerprint-value/1** (invariants.md:507)
"Where {merge-onto} exists, every fingerprint a relation carries in the latest version of a decision, in the decision log a merge onto {merge-onto} leaves, equals the current fingerprint there of the decision it names."
- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --merge-onto {merge-onto} --record .runs/decisions-merge-onto.jsonl`
- **Rests on:** none · **Derives from:** WAY-02@3ffcbd46 · WAY-31@a14c616c · **Part:** decisions · relation-model
Note: this is the precise pattern for the guidelines form check ("stops the merge"): a `{merge-onto}` comparison, failing when a fingerprint is stale. link-fingerprint-value/1 is the same for invariants' links.

**fingerprint-definition/1** (invariants.md:587)
"The script of `relation-model` gives a text the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that text encoded in UTF-8, after every run of spaces and line breaks is replaced by a single space and both ends are trimmed."
- **Method:** `python -B gate/run_tests.py relation-model --record .runs/relation-model-tests.jsonl`
- **Rests on:** sha-256@6ba272ed · utf-8@6afd686d · **Derives from:** WAY-02@3ffcbd46 · **Part:** relation-model
Note: the form script should call `relation-model/fingerprint.py` (surface `content-fingerprint`, "The same wording gives the same fingerprint.") rather than reimplement it (WAY-02 rejected "one computation per element").

---

## 4. Environment facts (environment_facts.md) — 30 entries, no withdrawn identifiers

| Identifier | Gist | Flag |
|---|---|---|
| git-path-patterns/1 | gitattributes patterns follow .gitignore rules with two exceptions (git 2.55.0) | |
| gitignore-paths/1 | last matching pattern decides; no re-include under excluded dir | |
| sha-256/1 | FIPS 180-4 SHA-256 gives 256-bit digest | |
| utf-8/1 | UTF-8 encodes U+0000..U+10FFFF in 1-4 octets | |
| json-text/1 | RFC 8259 JSON text rules | relevant if tokens file is JSON |
| json-lines/1 | JSON Lines one value per line | run records |
| python-stdlib-modules/1 | stdlib = `sys.stdlib_module_names` of Python 3.14 | PYTHON STDLIB |
| impossiblebench-test-modification/1 | Claude models modify tests; read-only tests help | |
| llm-self-preference/1 | LLMs favour own summaries | |
| llm-design-rationale-expert-overlap/1 | LLM design rationale overlap with experts low precision | bears on audit mode (WAY-29) |
| llm-decision-violation-detection/1 | LLMs detect explicit code-inferable decision violations well | |
| instruction-density-accuracy/1 | 68% accuracy at 500 instructions | bears on loading a long styleguide |
| context-file-effect/1 | context files don't generally help; instructions followed; overviews don't help | TOOLS LOADING INSTRUCTION FILES |
| claude-code-path-rules/1 | Claude Code applies `paths` rules only with matching files | TOOLS LOADING INSTRUCTION FILES |
| visible-scoring-reward-hacking/1 | METR: reward hacking with visible scoring | |
| oracle-in-loop-building/1 | agents with oracle in loop build demos not libraries (Fluent-UI table) | |
| github-private-repository-response/1 | GitHub 404 for private | |
| anthropic-model-states/1 | Active/Legacy/Deprecated/Retired | |
| python-314-bugfix-status/1 | Python 3.14 in bugfix phase | PYTHON |
| python-release-binaries/1 | bugfix phase ships binaries, security doesn't | PYTHON |
| claude-code-project-skills/1 | where Claude Code loads project skills (worktrees, /cd) | TOOLS LOADING SKILLS |
| claude-code-nested-skills/1 | nested `.claude/skills/` load on first file touch | TOOLS LOADING SKILLS |
| codex-repository-skills/1 | Codex scans `.agents/skills` cwd->root | TOOLS LOADING SKILLS |
| codex-skill-paths/1 | Codex skill list includes paths | TOOLS LOADING SKILLS |
| claude-code-imports/1 | `@` imports expanded at launch; code spans skipped | TOOLS LOADING INSTRUCTION FILES |
| claude-code-agents-md/1 | Claude Code reads AGENTS.md only with no CLAUDE.md | TOOLS LOADING INSTRUCTION FILES |
| codex-agents-md/1 | Codex instruction chain root->cwd, one file per dir | TOOLS LOADING INSTRUCTION FILES |
| cursor-agents-md/1 | Cursor CLI reads root AGENTS.md/CLAUDE.md beside `.cursor/rules` | TOOLS LOADING INSTRUCTION FILES |
| single-rule-compliance/1 | structural variables of config files show no detectable effect; compliance drops per function generated | TOOLS LOADING INSTRUCTION FILES |
| agent-run-variance/1 | pass@1 varies 2.2-6.0 pp across runs | |

(30 fact entries in all; the withdrawn-identifiers table is empty.)

WCAG: **no fact about WCAG, contrast, focus or any accessibility standard exists.** Facts the design will need in a product (contrast ratio criterion, focus-visible criterion, the edition) do not exist in the-way and must be written per product from the dated W3C edition (WAY-80), with no network now -> `TODO`.
Python stdlib: python-stdlib-modules/1 (rests script-imports); python-314-bugfix-status/1, python-release-binaries/1 (WAY-89).
Tools loading instruction files/skills: claude-code-path-rules, claude-code-imports, claude-code-agents-md, codex-agents-md, cursor-agents-md, context-file-effect, single-rule-compliance (instruction files); claude-code-project-skills, claude-code-nested-skills, codex-repository-skills, codex-skill-paths (skills). No fact covers Cursor's `.cursor/rules` path scoping or Codex path-scoped rules — a path-scoped "no hard-coded values" rule would rest only on claude-code-path-rules for Claude Code.

---

## 5. Keyword sweep (decisions, invariants, environment_facts, glossary, part_map)

Hits counted case-insensitively, by word where noted.

- styleguide / style guide: 0
- guideline(s): 0
- guide(s) (word): 10 — decisions.md:2492 ("Python Developer's Guide", unrelated); 3839, 3842, 3908, 3912, 3926, 3927, 4014 (WAY-128/130/133: "guide" = the-way's integration guide / a guide no session would find — **related**: "guide" is used for a pointed-to instruction document, a near neighbour of "guidelines"; WAY-99 risk if both words enter binding parts with different meanings); environment_facts.md:160, 162 (Python Developer's Guide, unrelated).
- design system: 0
- token(s): 2 — decisions.md:2406 (secret token, unrelated), 5201 (LLM tokens, unrelated).
- UI (case-sensitive word): 1 — environment_facts.md:131 ("React Fluent-UI data table" in oracle-in-loop-building; unrelated to styleguide but is the only UI-library mention).
- view(s): 10 — decisions.md:125 (WAY-04 rationale "a view derived from it shows accidents as architecture"); 534, 537, 544 x2, 557 (WAY-18 "what is in force today is a view that a script generates from the log"); invariants.md:327, 329, 337, 339 (view-versions, view-links). **Related:** "view" already means the generated view of the decision log in the-way's foundation; "view files" in the-way's own new entries would give "view" a second meaning (WAY-99). Not a glossary term, so no WAY-104 constraint on products.
- screen(s): 10 — decisions.md:658 (WAY-22 "no screen offers a second player"), 2456 (WAY-86 "the screens covered" — WCAG area), 3452 x2, 3456, 3461, 3483 (WAY-121 screens / first screen), 4490, 4613 (plans, "tables no screen reads"), 5349 (WAY-165 "through a screen in a browser"). Related: 2456, 3452-3483, 5349.
- component(s): 0
- accessibility/accessible: 3 — decisions.md:222, 230 (WAY-08 accessibility check / tools — **related**); environment_facts.md:35 ("UTF-16 accessible range", unrelated).
- WCAG: 1 — decisions.md:2456 (WAY-86 complies example — **related**).
- contrast: 2 — environment_facts.md:232, 235 (statistical "contrast", unrelated).
- focus(ed): 4 — decisions.md:5065, 5067, 5091, 5111 ("focused checks", WAY-159/160, unrelated).
- hardcoded / hard-coded: 0
- literal(s): 2 — decisions.md:1632 (WAY-57 "a heading's code literal"), 1975 (WAY-69 "carries its expected wording and fingerprint as literals" — **related** to how a contrast check must hold its threshold).
- role(s): 1 — decisions.md:839 ("the agent's role", unrelated).
- kitchen: 0
- palette: 0
- colour/color(s): 0

Additional glossary finding (not a sweep word, found while reading glossary.md:175-177): **"repository instruction file"** — "A repository instruction file is an instruction file for coding agents that a repository's git tracks under the name `AGENTS.md`, `CLAUDE.md` or `CLAUDE.local.md` in any of its directories, `.claude/` among them, or as a Markdown file its root `AGENTS.md` or `CLAUDE.md` names by its path." A styleguide that the product's root AGENTS.md names by its path is, by this definition, a repository instruction file. Consequences: in the-way, instruction-file-imports would apply to any guidelines file the-way's root AGENTS.md names; in a product, the instruction-files skill judges the styleguide under WAY-128–131. And **"foundation"** (glossary.md:86): "the written record of the rules the product holds itself to ..." — rules written in guidelines would fall under it.

---

## 6. Contradictions and tensions, consolidated

1. **WAY-114 (explicit contradiction).** "a question goes to the human only where the agent has no recommendation"; violates "an agent asks the human to confirm a choice it already recommends". The skill asks even with a recommendation. Needs a new decision `narrows WAY-114@04b4f599` naming the area (precedent: WAY-134 narrows WAY-114).
2. **WAY-01 / WAY-106 / WAY-28 / foundation-change invariants.** The skill writing product entries outside a task's foundation step ("before the first screen" as a standalone conversation; "audit" recovering decisions for the whole UI) conflicts with "reaches the main branch in the same merge as the code that follows it", "it writes no foundation entries" (project level), "Decisions are recovered only when a task touches the parts they govern"; every such change also needs foundation-change-assessment-record and foundation-search-record.
3. **WAY-09 + repository-file-location + WAY-93.** No directory WAY-09 names can hold the guidelines template, styleguide template, skill and form script; a new WAY-09 version and a part in part_map.md are needed; a part `guidelines` beside a glossary term "guidelines" raises the collision warning without the element exemption.
4. **WAY-60 / WAY-69 / WAY-38 / WAY-73.** (Interpretation) "view files", the colour pairs and the contrast threshold cannot be set in the styleguide or the tokens file; the check must hold its threshold as a literal and not read it from the file it checks; the threshold rests on a WCAG fact (none exists); a the-way script that parses CSS/JSX for hard-coded values contradicts WAY-38's rejected option and script-subprocesses — such checks are product tests or product-declared linters.
5. **WAY-128 / WAY-130 / WAY-52 / WAY-107 / WAY-141 / WAY-133.** (Interpretation) "no hard-coded values in view files" is "a rule for some files" — its place is a path-scoped or map-generated rule, not the always-loaded AGENTS.md; added before any mistake, it is admissible only as carrying a recorded decision and with its mechanism; a product path inside the installer's marked block repeats what WAY-107 rejects; the installer may not write `.claude/rules/the-way.md` and must not write a second rule file.
6. **WAY-02 / WAY-31.** WAY-02 lets bare and version references stand unflagged and only "flags" stale ones; stopping the merge for guidelines and requiring fingerprints on every reference narrows WAY-02 and extends WAY-31 beyond decisions/invariants — needs a decision. The product-side invariant belongs to each product's foundation (WAY-34), and must reach changes to decisions.md/invariants.md (WAY-62).
7. **WAY-04 / WAY-22 / WAY-18 / WAY-26 / WAY-52 / glossary "foundation".** (Interpretation) guidelines may hold only how-to and fingerprinted references; any rule, principle (each principle a decision of its own, WAY-26), decision list or copied token values inside them is either a second log, a hand-written copy of state, or — by the glossary's definition — foundation content outside the closed five.
8. **WAY-86 vs WAY-46.** A WCAG adoption decision is right for a voluntary catalogue; where an accessibility law applies, WCAG-derived requirements bind without adoption (fact + failure mode at the part), so the skill must ask which case holds.
9. **WAY-122/123 scope.** Both are scoped to project-level technology choices; "WAY-122 discipline" for styleguide research needs a decision saying which parts carry over (its type/convention/wide-use properties do not fit design choices), and tooling choices (CSS framework, token build) stay with settle-technology (WAY-121).
