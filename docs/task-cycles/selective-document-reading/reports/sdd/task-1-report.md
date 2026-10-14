# Slice 1 implementer report

Status: DONE. All specified available suites passed; common remains unchecked because it has no tests.

## Boundary and versions

- Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
- Branch: `task/selective-document-reading`.
- Base/foundation revision: `430e37724a53ea607fd3b6295c5697332b876359`.
- Frozen inputs: `.runs/task-cycles/selective-document-reading/task.md` and `spec.md`, both read
  whole; task-1 brief and slice-1 routing read first. Spec records source revision `52b9d487`.
- Superpowers: installed 6.4.1 implementer prompt read and followed under the routing adaptation.
- Seven tracked paths only; no foundation entries, code, tests, names, descriptions or locations
  changed. No entry-point regeneration required. This ignored report is implementation evidence.
- Commit: `3056064` — Share selective foundation reading across element workflows.
- Commit completed with explicit seven-path staging; no push. Post-commit `git status --short`
  is empty; author email confirmed as the private-repository address. Boundary is the committed
  Slice 1 before root's independent review.

## Implemented

`elements/common/way_of_working.md` replaces unconditional element-file and glossary loading with
one shared `Reading the foundation` section. It retains complete templates/rules/examples, makes
selected foundation entries whole reading units, and covers routing, complete current Scope
inspection, invariant reach, incoming dependents, vocabulary, semantic expansion, operational
selection evidence and refresh. Step 2 explicitly preserves both WAY-33 search timings/records.
Projected mode now refers to the same selection rather than retaining its generic file read.

The six skill readers refer to that shared section. Decisions retain number/version discovery
and empty-log prefix handling. Part-map retains complete routing input and identifier/dependency
searches. Invariants retain writing/check-author duties. Facts retain source/method/mechanical
checks, dependent handling and human verdicts. Glossary retains its entire use/meaning searches
and independent changed-definition use review. Candidate finder retains the whole source and
complete human-selected table, with an explicit all-five-elements duplicate/collision search.

Changed tracked files:

- `elements/common/way_of_working.md`
- `elements/common/skill/SKILL.md`
- `elements/decisions/skill/SKILL.md`
- `elements/part-map/skill/SKILL.md`
- `elements/invariants/skill/SKILL.md`
- `elements/environment-facts/skill/SKILL.md`
- `elements/glossary/skill/SKILL.md`

## Choices, evidence, alternatives and cost

1. Kept selection in one shared section and used short references in element readers. WAY-35
   and WAY-150 and the reviewed spec require one shared method. Duplicated local selection rules
   would be easier to read alone but would drift; the chosen cost is a mandatory shared-file read.
   Leaving the old clauses would retain growing whole-file loading and fail the settled task.
2. Used complete current Scope inspection plus a record/comparison, without adding a selector or
   persisted index. WAY-21 and `decisions-found-for-change/1` require complete matches; the
   existing `latest_scopes` handles wrapped values. A new tool would add parsing/API/tests while
   not deciding semantic collisions; exhaustive inspection costs attention and remains allowed.
3. Explicitly retained WAY-33's pre-merge repeat and separate search record at shared step 2.
   The old step said only the initial search; the spec requires both timings. Leaving the timing
   implicit in a citation could lose the repeat. Repeating it costs one instruction sentence,
   without changing its domain or human settlement duties.
4. Changed projected step 1 too. Its old generic element-file read would otherwise leave a
   second, ambiguous contract. It still asks about no new file and writes no map/foundation.
   Keeping it unchanged costs ambiguity; the reference adds no projected approval step.
5. Named facts' actual decision/invariant dependents explicitly. Their required handling lives
   in existing steps 4 and withdrawal; shared incoming-link inspection supplies discovery. A
   broad unconditional dependent-file read would cost unrelated context; selecting only outgoing
   links could miss the very dependents the fact must update.
6. No new instruction-string tests or production-code TDD. These are Markdown instructions;
   existing tests plus instruction walkthroughs fit the specified validation. String tests would
   constrain phrasing without proving agent behaviour. Runtime reading completeness and measured
   savings remain unchecked, not inferred from prose inspection.
7. Rewrapped two newly changed bullets during self-review for readability; no semantic change.

## Checks and exits

Commands were run once for this slice; independent suites ran concurrently. Test runner output
was unittest progress, summary and `OK`, with no warning or failing-test diagnostics for completed
passing suites. No production-code RED/GREEN step applies.

| Command | Exit | Observed result |
|---|---|---|
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests, OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 162 tests, OK |
| `python -B gate/run_tests.py elements/invariants` | 0 | 233 tests, OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | 204 tests, OK |
| `python -B gate/run_tests.py elements/environment-facts` | 0 | 165 tests, OK |
| `python -B gate/run_tests.py elements/common` | 1 | Ran 0 tests; NO TESTS RAN; unchecked, not passed |
| `python -B gate/run_tests.py gate` | 0 | 98 tests, OK |
| `git diff --check` | 0 | no output |
| local read-only Python control-byte scan of all seven changed files | 0 | zero forbidden controls per file |
| local read-only invocation of existing `latest_scopes` on the current full decision log | 0 | complete current expected Scope-match set, inventoried below |

The full gate, automatic actual-read completeness, behavioural execution of this new reading
method and measured savings on a large real project are unchecked. No foundation file changed,
so no foundation-format guard was run in this slice. Root owns final cycle checks and review.
Available suites ran 1,031 tests in total; all passed. The common runner's nonzero no-tests exit
is retained above, and is not included in that passing-test count.

## Walkthroughs against final instructions (inspection, not agent runs)

- Wrapped Scope: current WAY-09/1 has a multiline Scope at `foundations/decisions.md:263`.
  The existing parser's complete-log read returns it for the touched element parts. Shared
  selection step 2 demands wrapped fields and the whole entry even if the task never linked it;
  step 6 compares it with the expected set. A search hit alone is expressly insufficient.
- Entry-collecting file: changing WAY-146 in `foundations/decisions.md` touches project-level by
  its Scope, rather than only decisions by the log's file path. Shared step 1 says to follow the
  changed entries under WAY-44; the complete Scope sweep then finds the project-level decisions.
- No diff and ambiguous ownership: for a proposed integration whose responsibility may belong
  to either of two product parts, shared step 1 maps behaviour, integrations, flows and surfaces,
  includes both uncertain parts and labels any prospective new part. Steps 2/6 inspect and compare
  current Scope matches for both; no empty-diff shortcut exists. This is a designed case, not a
  product session that was executed.
- Incoming dependent and every: current WAY-134/1 carries `derives from WAY-115@eb7ba15c` at
  `foundations/decisions.md:3984`. A WAY-115 change is found by incoming-dependent search in
  shared step 3 even though WAY-115 cannot list it. `file-part-assignment/1` at
  `foundations/invariants.md:697` has `Part: every`, so complete Part inspection includes it
  regardless of an initial narrow part choice. No fingerprint is renewed merely by bulk rewrite.
- Collision outside selected parts/links: for work initially selecting only project-level,
  WAY-27's rule against private reasoning links is outside that decision's Scope. A proposed
  private source link is still searched across all five elements by shared step 5 and finder
  step 1; shared step 2 search settles the finding as a relation, entry change or human question
  before acceptance and repeats before merge. This is source-based inspection, not evidence of
  an executed collision-finding agent.
- Retained obligations: shared step 1 still reads template/rules/examples whole, including the
  named complete examples; finder still reads source whole and shows the whole table. Decision
  question search, numbering/version discovery and empty log handling remain. Fact method,
  failure, verdict and dependent duties remain in steps 3/4 and withdrawal. Glossary's use list,
  every-use reading, meaning search and independent changed-definition review remain intact.

The spec reader table has 13 readers: this slice covers its seven shared/element rows. The six
project/task-cycle rows and plan document-reading method belong to slice 2, not this commit.

## Self-review and concerns

Read the real seven-file diff and compared it with the spec's shared contract and seven reader
rows. No extra tracked path, new gate, parser, index, test or entry found. Mandatory source and
candidate-table duties, fact/verdict/glossary semantics, templates/examples and approvals remain.
The retained unavailable checks above are limits of evidence, not passing results. No unsettled
design choice or remaining implementation defect identified. Independent review is root's next
dispatch; no subagent or reviewer was spawned by this implementer.

## Actual loaded foundation entry inventory

The following inventory identifies the complete entries loaded from the brief's whole-entry
ranges at the base revision; source read output that was truncated was reread in smaller ranges.
The part map and glossary were read whole; all named templates/examples and common rules were
read, with truncated template output reread as whole files. These are actual reads; the separate
Scope parser scan is discovery evidence and does not alone count as reading an entry.

### foundations/decisions.md

WAY-01/1 — What state does the foundation describe? (line 6), WAY-02/1 — How do dependents learn that an entry has changed? (line 38), WAY-03/1 — Who may change an invariant test, and when? (line 71), WAY-04/1 — What makes up a product's foundation, and what in it is derived rather than written by hand? (line 95), WAY-05/1 — How is a decision entry written? (line 137), WAY-07/1 — From when may a decision entry no longer be edited? (line 176), WAY-08/1 — How is an invariant checked? (line 203), WAY-09/1 — What may enter the process repository? (line 234), WAY-10/1 — Who assesses a change to an invariant test or to the foundation? (line 305), WAY-11/1 — How does a task end? (line 343), WAY-12/1 — How is a decision checked? (line 384), WAY-14/1 — Who approves a version of a decision? (line 459), WAY-16/1 — How are the checks of invariants run? (line 480), WAY-17/1 — Which links between foundation entries are mandatory? (line 507), WAY-18/1 — How is a product's decision log kept? (line 531), WAY-19/1 — How are decisions numbered and versioned? (line 563), WAY-20/1 — What kinds of change can a decision undergo? (line 596), WAY-21/1 — What is a decision's scope? (line 623), WAY-22/1 — Is a rule a decision or an invariant? (line 645), WAY-24/1 — How is a decision that rests on a prediction reviewed? (line 673), WAY-25/1 — What settles a collision between two decisions? (line 708), WAY-26/1 — How are trade-off principles and non-goals written? (line 737), WAY-27/1 — Where may this repository point for its reasoning? (line 763), WAY-28/1 — How does the process enter a product that already exists? (line 794), WAY-29/1 — How is a decision recovered from an existing product written? (line 826), WAY-30/1 — What happens when a change contradicts a decision? (line 857), WAY-31/1 — Which links between entries are flagged when the named entry changes? (line 888), WAY-32/1 — What types of relation can a decision name? (line 923), WAY-33/1 — What does the author of a foundation change search for? (line 949), WAY-34/1 — Which version of the process does a product use? (line 980), WAY-35/1 — What does an element's skill hold? (line 1009), WAY-36/1 — Is a rule a decision or does it belong in a plan? (line 1043), WAY-37/1 — What happens to entries that wait for something when it arrives? (line 1070), WAY-38/1 — In what are the scripts of the-way written? (line 1097), WAY-40/1 — What kinds of entry does the part map hold? (line 1127), WAY-41/1 — What identifies an entry of the part map? (line 1152), WAY-42/1 — What is the binding part of a part map entry? (line 1178), WAY-43/1 — Is an entry of the part map versioned? (line 1201), WAY-44/1 — What assigns a file to a part? (line 1228), WAY-45/1 — How does the part map record a critical flow, and when does a change lie on it? (line 1259), WAY-46/1 — How does the criticality of a part arise? (line 1285), WAY-47/1 — How is a critical flow's list of parts checked? (line 1326), WAY-48/1 — How is a trust boundary recorded? (line 1353), WAY-49/1 — How does a product declare a surface, and by what path may it change? (line 1379), WAY-51/1 — What does the main branch hold where the product does not meet an invariant or the part map's allowed dependencies? (line 1423), WAY-52/1 — What is generated from the part map for an agent? (line 1459), WAY-53/1 — How is a derived file compared with what its generator produces? (line 1485), WAY-54/1 — Where does the value of a field in a template come from? (line 1508), WAY-55/1 — Which part of the process holds the gate? (line 1541), WAY-56/1 — How much does one invariant entry hold, and what is its binding part? (line 1572), WAY-57/1 — Is an invariant entry versioned? (line 1602), WAY-58/1 — What does an invariant entry record when it was recovered from what a product does? (line 1645), WAY-60/1 — Where may a condition that decides an invariant stand? (line 1692), WAY-61/1 — How is an invariant's method of checking written, and how is its result read? (line 1728), WAY-62/1 — What does an invariant entry name in the part map? (line 1782), WAY-63/1 — What results does the gate report for invariants, and which make its command fail? (line 1813), WAY-64/1 — Where do invariant and environment fact entries stand, and what identifies one? (line 1850), WAY-65/1 — How does a check cite its invariant, and which files are invariant tests? (line 1890), WAY-68/1 — What happens to a check that gives different verdicts on one commit? (line 1921), WAY-69/1 — Who writes an invariant's sentence, its check and its deliberate break, and what may the check compute for itself? (line 1955), WAY-71/1 — Does every field of a foundation entry appear in every entry, and what may it hold? (line 1991), WAY-72/1 — In what language is a product's foundation written? (line 2029), WAY-73/1 — Which entries name an environment fact? (line 2055), WAY-74/1 — What form does the-way's own record of a run take? (line 2088), WAY-76/1 — How much does one environment fact entry hold? (line 2123), WAY-77/1 — What does an environment fact's *Holds for* name? (line 2152), WAY-78/1 — What is the binding part of an environment fact entry? (line 2182), WAY-79/1 — Is an environment fact entry versioned? (line 2205), WAY-80/1 — What is an environment fact's source? (line 2235), WAY-81/1 — How is an environment fact's method written, and on which release of its tool does a probe's verdict count? (line 2270), WAY-82/1 — When does an environment fact's method run, and what fails its watch? (line 2315), WAY-83/1 — Where does a human verdict stand, and how long is it in force? (line 2344), WAY-84/1 — How is a setting that people of the product change outside its repository written? (line 2372), WAY-85/1 — How is a finding of a study written as an environment fact? (line 2405), WAY-86/1 — How does a catalogue of requirements or a binding rule reach a product? (line 2437), WAY-89/1 — Which version of Python do the scripts of the-way run on, and when does it move? (line 2471), WAY-90/1 — Which citations of a decision's *Based on* become environment fact entries, and how are they named? (line 2500), WAY-93/1 — Where do glossary entries stand, and what identifies one? (line 2533), WAY-94/1 — What does a glossary entry hold, and what is its binding part? (line 2567), WAY-95/1 — Which words take a glossary entry, and in which glossary? (line 2601), WAY-96/1 — How is a glossary definition written? (line 2647), WAY-97/1 — How does a sentence rely on a glossary term, and what does a change to a definition go through? (line 2681), WAY-98/1 — Where is a word of a glossary entry's *Avoid* an error? (line 2717), WAY-99/1 — How does one word keep one meaning in the foundation? (line 2751), WAY-100/1 — When does a method or practice borrowed from elsewhere bind a product? (line 2783), WAY-101/1 — Who chooses the backlog tool used with the-way? (line 2809), WAY-102/1 — What is the-way for? (line 2832), WAY-103/1 — Who is the-way for? (line 2859), WAY-104/1 — How does a product write a word of its domain that the glossary of the-way holds? (line 2884), WAY-105/1 — Which check reports an invariant whose command runs a script that does not exist, and how is that script read? (line 2938), WAY-111/1 — What does the project level read in the current foundation? (line 3117), WAY-113/1 — How does an agent of the-way ask a human decision? (line 3176), WAY-114/1 — What does a human accept of an entry, and when? (line 3212), WAY-115/1 — How are foundation entries found in a project's source? (line 3241), WAY-116/1 — Which foundation entries may a project definition project? (line 3272), WAY-117/1 — How does a foundation entry stand in a project definition before it is written? (line 3300), WAY-119/1 — When may a projected decision leave Review when unresolved at the gate? (line 3363), WAY-120/1 — How does the-way critique an agent's proposal? (line 3390), WAY-121/1 — Where does a project settle the technology it needs? (line 3422), WAY-122/1 — How are the options of a technology choice found and checked before a human sees them? (line 3459), WAY-123/1 — How does a technology choice reach a human who cannot assess the technology? (line 3518), WAY-126/1 — How does a projected entry enter the foundation? (line 3648), WAY-127/1 — How does a session working on the-way itself reach the-way's skills? (line 3695), WAY-134/1 — How does a task carry what its refinement settles for the foundation? (line 3967), WAY-137/1 — What decides between places to run that the simplest and cheapest option leaves tied? (line 4120), WAY-138/1 — Which option of a technology choice is tested for what choosing it could break, and where do the risks found go? (line 4160), WAY-146/1 — What checks a project plan before it is handed over? (line 4494), WAY-150/1 — How do the-way skills choose which product foundation material to read? (line 4647), WAY-151/1 — How much of large project definitions and existing plans does plan-project read? (line 4685)

### foundations/invariants.md

decision-guard-stale-reference/1 (line 6), decision-fingerprint-input/1 (line 16), log-reference-target/1 (line 26), foundation-file-kinds/1 (line 36), binding-sentence-count/1 (line 46), binding-sentence-words/1 (line 56), decision-example-numbers/1 (line 66), decision-template-change/1 (line 76), foundation-change-merge-route/1 (line 86), log-existing-lines/1 (line 96), log-versions-added-per-number/1 (line 106), log-merge-copies/1 (line 116), invariant-method-form/1 (line 126), invariant-test-break/1 (line 136), repository-file-location/1 (line 146), element-directory-contents/1 (line 156), invariant-example-target/1 (line 176), map-example-target/1 (line 186), glossary-example-target/1 (line 196), foundation-change-assessment-record/1 (line 206), return-step-record/1 (line 216), decision-verification-level/1 (line 226), level-one-decision-invariants/1 (line 236), verification-invariant-derivation/1 (line 246), foundation-change-path/1 (line 256), decision-approval-record/1 (line 266), decision-approver/1 (line 277), derived-file-content/1 (line 287), derived-subset-naming/1 (line 297), ci-checking-commands/1 (line 307), gate-check-source/1 (line 317), view-versions/1 (line 327), view-links/1 (line 337), decision-heading-form/1 (line 347), decision-version-sequence/1 (line 357), decision-change-kind/1 (line 367), decision-binding-across-versions/1 (line 377), repeal-binding-sentences/1 (line 387), decision-scope-names/1 (line 397), decisions-found-for-change/1 (line 407), review-when-form/1 (line 417), decision-guard-overdue-review/1 (line 427), review-next-check/1 (line 437), review-named-version/1 (line 447), narrows-pairs/1 (line 457), outbound-link-reach/1 (line 467), inherited-origin-form/1 (line 477), inherited-rationale-source/1 (line 487), relation-fingerprint-presence/1 (line 497), relation-fingerprint-value/1 (line 507), relation-type/1 (line 517), foundation-search-record/1 (line 527), skill-rule-source/1 (line 537), script-language/1 (line 547), script-imports/1 (line 557), script-subprocesses/1 (line 567), map-guard-missing-command/1 (line 577), map-entry-kinds/1 (line 597), map-section-kinds/1 (line 607), part-map-file/1 (line 617), map-identifier-form/1 (line 627), identifier-holders/1 (line 637), map-reference-target/1 (line 647), map-withdrawal-successors/1 (line 657), map-identifier-persistence/1 (line 667), map-fingerprint-input/1 (line 677), map-entry-version/1 (line 687), file-part-assignment/1 (line 697), path-pattern-reach/1 (line 707), left-out-file-assignment/1 (line 717), flow-part-names/1 (line 727), flow-invariant-link/1 (line 737), map-invariant-names/1 (line 747), failure-mode-severity/1 (line 757), failure-mode-detection/1 (line 767), part-criticality-field/1 (line 777), map-guard-unrecorded-criticality/1 (line 787), map-guard-dependency-report/1 (line 797), criticality-lowering-report/1 (line 807), flow-coverage-parts/1 (line 817), map-guard-missing-coverage/1 (line 827), map-guard-test-runs/1 (line 837), external-exchange-row/1 (line 847), surface-promise-level/1 (line 867), surface-declaration/1 (line 877), map-withdrawal-date/1 (line 887), promise-level-policy/1 (line 897), surface-change-path/1 (line 907), known-violation-coverage/1 (line 917), known-violations-growth/1 (line 927), known-violation-currency/1 (line 937), known-violation-fields/1 (line 947), known-violation-line-number/1 (line 957), generated-pattern-source/1 (line 967), generated-overview/1 (line 977), flow-test-location/1 (line 987), invariant-sentence-count/1 (line 997), invariant-identifier-form/1 (line 1007), invariant-version-number/1 (line 1017), invariant-version-new/1 (line 1027), invariant-version-changed/1 (line 1037), invariant-version-unchanged/1 (line 1047), invariant-earlier-wording/1 (line 1057), invariant-citation-version/1 (line 1067), invariant-correction-confirmation/1 (line 1077), invariant-recovered-form/1 (line 1087), invariant-recovered-derived/1 (line 1097), invariant-fingerprint-input/1 (line 1117), sentence-branch-names/1 (line 1127), sentence-gate-values/1 (line 1137), method-gate-values/1 (line 1147), invariant-part-names/1 (line 1187), invariant-part-form/1 (line 1197), gate-unchecked-reason/1 (line 1227), flow-test-run/1 (line 1257), invariants-file/1 (line 1277), invariant-identifier-persistence/1 (line 1287), invariant-withdrawal-persistence/1 (line 1297), withdrawal-successors/1 (line 1307), invariant-citation-target/1 (line 1317), data-line-target/1 (line 1327), link-fingerprint-presence/1 (line 1347), link-fingerprint-value/1 (line 1357), violated-list-growth/1 (line 1367), violated-position-version/1 (line 1377), quarantine-position-form/1 (line 1387), quarantine-flow-invariants/1 (line 1397), log-entry-field-presence/1 (line 1417), log-entry-field-words/1 (line 1427), log-entry-merge-todo/1 (line 1437), map-entry-field-presence/1 (line 1447), map-entry-field-words/1 (line 1457), invariant-entry-field-presence/1 (line 1467), invariant-entry-field-words/1 (line 1477), invariant-entry-merge-todo/1 (line 1487), run-record-form/1 (line 1497), run-record-path/1 (line 1507), environment-facts-file/1 (line 1547), fact-identifier-form/1 (line 1557), fact-identifier-persistence/1 (line 1567), fact-withdrawal-persistence/1 (line 1577), fact-withdrawal-successors/1 (line 1587), fact-sentence-count/1 (line 1597), fact-scope-word/1 (line 1607), fact-fingerprint-input/1 (line 1617), fact-version-new/1 (line 1627), fact-version-changed/1 (line 1637), fact-version-unchanged/1 (line 1647), fact-citation-version/1 (line 1657), fact-source-form/1 (line 1667), fact-method-form/1 (line 1677), fact-citation-target/1 (line 1687), based-on-fact-fingerprint/1 (line 1707), based-on-fact-fingerprint-value/1 (line 1717), fact-clock-exit/1 (line 1737), human-verdict-invariant-row/1 (line 1747), human-verdict-fact-row/1 (line 1757), fact-dependants/1 (line 1777), fact-entry-field-presence/1 (line 1787), fact-entry-field-words/1 (line 1797), glossary-file/1 (line 1807), glossary-file-sections/1 (line 1817), glossary-term-holder/1 (line 1827), glossary-term-collision/1 (line 1837), glossary-process-terms/1 (line 1847), glossary-entry-field-presence/1 (line 1859), glossary-entry-field-words/1 (line 1869), glossary-term-use/1 (line 1879), glossary-definition-count/1 (line 1889), glossary-definition-words/1 (line 1899), glossary-entry-version/1 (line 1909), glossary-definition-uses/1 (line 1919), glossary-avoid-growth/1 (line 1929), glossary-avoid-single/1 (line 1939), glossary-avoid-term/1 (line 1949), glossary-avoid-carrier/1 (line 1959), glossary-not-target/1 (line 1969), glossary-not-quoted-word/1 (line 1979), glossary-entry-merge-todo/1 (line 1989), skill-entry-points/1 (line 2065), instruction-file-imports/1 (line 2075)

### Expected current Scope matches for the seven changed files

Touched parts: elements-common, decisions, part-map, invariants, environment-facts, glossary.

WAY-01/1 (Scope line 16), WAY-02/1 (Scope line 51), WAY-03/1 (Scope line 80), WAY-04/1 (Scope line 107), WAY-05/1 (Scope line 150), WAY-07/1 (Scope line 184), WAY-08/1 (Scope line 215), WAY-09/1 (Scope line 263), WAY-10/1 (Scope line 316), WAY-11/1 (Scope line 358), WAY-12/1 (Scope line 394), WAY-14/1 (Scope line 466), WAY-16/1 (Scope line 488), WAY-17/1 (Scope line 515), WAY-18/1 (Scope line 541), WAY-19/1 (Scope line 574), WAY-20/1 (Scope line 604), WAY-21/1 (Scope line 630), WAY-22/1 (Scope line 654), WAY-24/1 (Scope line 684), WAY-25/1 (Scope line 717), WAY-26/1 (Scope line 744), WAY-27/1 (Scope line 771), WAY-28/1 (Scope line 804), WAY-29/1 (Scope line 835), WAY-30/1 (Scope line 868), WAY-31/1 (Scope line 898), WAY-32/1 (Scope line 930), WAY-33/1 (Scope line 958), WAY-34/1 (Scope line 987), WAY-35/1 (Scope line 1018), WAY-36/1 (Scope line 1050), WAY-37/1 (Scope line 1078), WAY-38/1 (Scope line 1106), WAY-40/1 (Scope line 1135), WAY-41/1 (Scope line 1161), WAY-42/1 (Scope line 1185), WAY-43/1 (Scope line 1208), WAY-44/1 (Scope line 1240), WAY-45/1 (Scope line 1268), WAY-46/1 (Scope line 1299), WAY-47/1 (Scope line 1335), WAY-48/1 (Scope line 1363), WAY-49/1 (Scope line 1393), WAY-51/1 (Scope line 1436), WAY-52/1 (Scope line 1468), WAY-53/1 (Scope line 1493), WAY-54/1 (Scope line 1518), WAY-55/1 (Scope line 1550), WAY-56/1 (Scope line 1581), WAY-57/1 (Scope line 1616), WAY-58/1 (Scope line 1660), WAY-60/1 (Scope line 1702), WAY-61/1 (Scope line 1744), WAY-62/1 (Scope line 1791), WAY-63/1 (Scope line 1822), WAY-64/1 (Scope line 1862), WAY-65/1 (Scope line 1900), WAY-68/1 (Scope line 1931), WAY-69/1 (Scope line 1964), WAY-71/1 (Scope line 2001), WAY-72/1 (Scope line 2035), WAY-73/1 (Scope line 2066), WAY-74/1 (Scope line 2098), WAY-76/1 (Scope line 2131), WAY-77/1 (Scope line 2160), WAY-78/1 (Scope line 2190), WAY-79/1 (Scope line 2213), WAY-80/1 (Scope line 2246), WAY-81/1 (Scope line 2283), WAY-82/1 (Scope line 2323), WAY-83/1 (Scope line 2354), WAY-84/1 (Scope line 2382), WAY-85/1 (Scope line 2416), WAY-86/1 (Scope line 2447), WAY-89/1 (Scope line 2478), WAY-90/1 (Scope line 2509), WAY-93/1 (Scope line 2544), WAY-94/1 (Scope line 2577), WAY-95/1 (Scope line 2614), WAY-96/1 (Scope line 2656), WAY-97/1 (Scope line 2693), WAY-98/1 (Scope line 2727), WAY-99/1 (Scope line 2761), WAY-100/1 (Scope line 2790), WAY-101/1 (Scope line 2815), WAY-102/1 (Scope line 2839), WAY-103/1 (Scope line 2866), WAY-104/1 (Scope line 2896), WAY-105/1 (Scope line 2951), WAY-113/1 (Scope line 3186), WAY-114/1 (Scope line 3221), WAY-115/1 (Scope line 3253), WAY-116/1 (Scope line 3281), WAY-117/1 (Scope line 3310), WAY-119/1 (Scope line 3371), WAY-120/1 (Scope line 3401), WAY-121/1 (Scope line 3433), WAY-122/1 (Scope line 3477), WAY-123/1 (Scope line 3529), WAY-126/1 (Scope line 3663), WAY-127/1 (Scope line 3708), WAY-134/1 (Scope line 3982), WAY-137/1 (Scope line 4130), WAY-138/1 (Scope line 4172), WAY-150/1 (Scope line 4659)

Compared with the loaded decision inventory: every expected match is loaded; WAY-111, WAY-146 and WAY-151 were additionally loaded as explicit brief sources. No difference remains. This comparison is a declared-set/read-evidence check, not a pass of the TODO method.
