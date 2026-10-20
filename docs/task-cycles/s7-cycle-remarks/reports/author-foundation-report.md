# Author report — foundation stage

Stage: foundation complete and committed; returned at its boundary. Operational Markdown is left for the next authorized stage.

## Inputs, authorization and reads

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks`; branch `s7-cycle-remarks`.
- Input revision: `f0b5eb131de5d681ee3fcdeb264e9f88778af2ec`; authoritative frozen task: `.runs/task-cycles/s7-cycle-remarks/task.md`, status ready for cycle, accepted settlement rows 1 and 2 (2026-10-21). Source questions 1–3 and To do 1, 2, 7 and 8 carry the meanings written here. The whole task and author handoff were read.
- The existing human acceptance is authority for both meaning changes. No orchestrator choice was represented as human approval. The session's instruction against asking again for an already authorized action applies; the new split into WAY-46 and WAY-224 changes organization, not accepted meaning.
- Read project AGENTS instructions and the worktree's `agent-instructions/README.md`; followed its pre-main edit-in-place route and placeholder request-link convention.
- Used worktree entry points `.agents/skills/the-way-record-decision/SKILL.md` and `.agents/skills/the-way-record-invariant/SKILL.md`, their complete element skills, templates and examples, `elements/common/rules.md` and `elements/common/way_of_working.md`. Read each entry named by those examples whole: WAY-03; log-entry-field-presence, decision-guard-overdue-review, file-part-assignment, fingerprint-definition, return-step-record.
- Read the foundation-stage boundary in `task-cycle/skill/SKILL.md`, the complete `product-guidelines/reading.md` and `relation-model/fingerprint.py`. No delegated operational method was invoked in this stage.
- All five foundation files were read whole, plus `foundations/violated_invariants.md`. Long reads whose output was truncated were reread in smaller ranges, including the missing spans; snippets were not counted as whole entry reads.

## Selection and whole-foundation search

At the input revision, prospective parts were decisions, invariants, part-map, task-cycle, elements-common, project-level and agent-instructions. There are 170 decisions with at least one of those parts in their complete Scope, including wrapped fields, and 174 invariants whose Part names one of them or `every`. The selection was expanded to reading the entire log (209 decision entries), entire invariant file (225 sections), entire part map, glossary and environment facts. This also covers the environment-facts and product-guidelines scope of WAY-46 and the dependent WAY-172. Nothing returned by discovery was silently dropped.

`foundation-selection.json` beside this report records the revision, expected identifiers and source lines, selected/read identifiers, whole-read start/end lines, complete-field discovery, semantic search patterns and each matching section's line numbers. It is discovery evidence, not a second maintained foundation index. Source files remain in Git; the evidence does not copy their contents.

The initial search covered all five elements for approval, acceptance, meaning, contradiction and narrowing; failure modes, candidates, criticality, deferred entries, questions and counterarguments; and return, chronicle, commit messages, fingerprints, brief extraction, plans and cycle records. Whole-entry reading resolved these effects:

- WAY-30 needs explicit precedence and an outgoing `narrows WAY-114` relation. WAY-114 remains the general answer; no duplicate reverse relation or general weakening is required.
- WAY-172 is the only pre-existing fingerprint-bearing decision dependent on WAY-30. It preserves its specific product-guideline rule: new meanings are approved in a task document or blocked request before dependent code; its rejection of approval merely with a cycle plan is still sound. WAY-30 does not make an unapproved plan approved. Only its relation fingerprint and current approval metadata change.
- WAY-46 needs explicit recognition that the accepted task or the human's supplied/accepted answer authorizes recording, regardless of who types it. `Including` preserves direct human recording outside a cycle; these recognized cases are not a newly exhaustive list for the whole product.
- No existing decision answers how the cycle presents an unaccepted failure-mode candidate and applies the answer. WAY-11 requires accepted entries in the same change; an unsettled question is not such an entry. WAY-113 provides the general question rule, and WAY-125 reserves human decisions and the request review. WAY-224 derives from those and WAY-46. It does not overrule them, so no additional `narrows` is justified.
- WAY-134 excludes part-map changes from settlement candidates. The recorded task row is a decision about failure-mode handling, not a proposed map row. No failure mode is invented or inserted by this task.
- WAY-10 already excludes author reasoning from independent assessment, and WAY-31 already requires semantic checking of relation fingerprints. The task's record placement, commit-message exclusion and pre-request guard instructions need operational edits, not new decision meanings.
- WAY-36 and WAY-148 already cover implementation choices without a plan and reuse of borrowed briefs. The temporary heading conversion is local operational adaptation; it is not made into a lasting foundation rule.
- No glossary ambiguity, new external premise, changed part responsibility/file ownership, new failure mode, flow, surface or trust boundary was found. No glossary, environment-fact or map entry needs changing. Existing environment-fact citations were read as stored foundation; this task does not claim to have reverified those external facts.

Guideline selection remains empty: no `guidelines/` directory exists and the change is process Markdown, not UI or program code. No guideline gap or expanded selection is needed. Affected parts retain their existing high criticality; no trust-boundary file is touched.

## Entries and accepted meanings

| Entry | Meaning in Polish | Task authority |
|---|---|---|
| WAY-30/1 | Zmiana decyzji zatwierdzona z dokumentem zadania albo planem, także we wpisie Settlements to record, jest odpowiedzią wymaganą przez WAY-114, więc agent pyta tylko o sens poza tą zgodą, a w tym obszarze WAY-30 ma pierwszeństwo. | Settlement 1, question 1, To do 1–2 |
| WAY-46/1 | Tryb awarii zlecony w dokumencie zadania albo podany lub przyjęty przez człowieka w odpowiedzi na pytanie cyklu jest zapisany przez człowieka niezależnie od tego, kto wpisuje go do pliku. | Human-recording part of settlement 2, question 2, To do 8 |
| WAY-224/1 | Cykl przedstawia znalezionego kandydata na tryb awarii w pytaniach PR z opisem, skutkami, wagą, wykrywaniem, rekomendacją i najsilniejszym kontrargumentem, a przyjętą odpowiedź wpisuje przed scaleniem do otwartego PR; samo pytanie nie jest odłożonym wpisem. | Candidate-routing part of settlement 2, questions 2–3, To do 7 |
| WAY-172/1 | Sens pozostaje bez zmian: odnowiono odcisk podstawy WAY-30 po sprawdzeniu zgodności szczególnej reguły dla wytycznych produktu. | Required dependency upkeep, WAY-31 |

WAY-30 fingerprint changes from `6924312f` to `2141bece`; WAY-46 from `a5f43e40` to `7511b86f`. WAY-172's binding part is byte-for-byte unchanged. WAY-30 names `narrows WAY-114@04b4f599` and states its precedence area. WAY-224 derives from WAY-46, WAY-11, WAY-113 and WAY-125 with current fingerprints.

Every existing incoming invariant reference to WAY-46 was checked against its own complete sentence before renewal:

| Invariant | Semantic check |
|---|---|
| failure-mode-severity/1 | Human authorization does not remove the required severity field. |
| failure-mode-detection/1 | Authorization does not change the invariant-or-explicit-not-detected requirement. |
| part-criticality-field/1 | No manually written criticality is introduced. |
| map-guard-unrecorded-criticality/1 | A part with no recorded modes still receives the highest criticality. |
| map-guard-dependency-report/1 | The own-mode, flow and unseparated-dependent maximum remains unchanged. |
| criticality-lowering-report/1 | Lowering still needs the comparison/report before human acceptance. |

Only Derives from fingerprints change in those six entries. Their sentences, methods, identifiers, versions, Correction fields and tests are unchanged.

## Verification level and author choices

The changed approval semantics and the new candidate-routing rule use level 2: whether the human supplied or accepted the meaning, whether a question repeats that acceptance, and whether a recommendation fairly exposes its strongest counterargument require the task/request/exchange, not just the product commit. A check for phrases in process Markdown would only mirror the implementation and would not decide compliance with those meanings. Existing level-1 invariants continue to cover the commit-verifiable failure-mode fields and criticality computation. No new invariant sentence/check is required, so no separate invariant authors were needed. This is not a claim that a missing automated method excuses a commit-falsifiable requirement.

Choices and costs:

- Record the entire accepted meaning across WAY-46 and new WAY-224. Leaving only the human-recording clarification would lose the accepted routing and correction rule. Packing it into WAY-46 would mix the criticality answer with request workflow and overload its binding sentences. A distinct entry adds a relation to maintain but keeps each question clear; the orchestrator confirmed this is a wording/organization choice within the settled row.
- Keep WAY-114 and WAY-172's binding sentences intact. Changing the general approval rule would expand the task; renewing only WAY-30's dependent fingerprint preserves the specific guideline rule. An implied precedence exception would leave competing instructions for later agents.
- Keep the strongest-counterargument requirement limited to candidate failure modes. Generalizing to every question would settle the expressly excluded broader rule.
- Recognize human authorization without making the typist the decision-maker. Requiring the human to enter the text adds transcription; recording an unaccepted candidate would transfer human judgment to the agent. Deferring an accepted candidate to another task lets current work merge with an incomplete assessment and risks losing it.
- Do not add foundation rules for borrowed-script adaptation or guard invocation details already supported by standing decisions. Such entries would turn this bounded execution choice into a product commitment.

## Checks and evidence

Every file named below is under this report's directory and contains the exact command, actual exit code and full stdout/stderr. The parent supplied the baseline gate evidence; it was not rerun as a baseline.

| Check | Baseline | Post-change |
|---|---|---|
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | exit 0, `baseline-decisions.txt` | exit 0, `post-decisions.txt` |
| `python -B elements/invariants/format_guard.py --base none --merge-onto none` | exit 0, `baseline-invariants.txt` | exit 0, `post-invariants.txt` |
| `python -B elements/part-map/format_guard.py --base none` | exit 0, `baseline-part-map.txt` | exit 0, `post-part-map.txt` |
| `python -B gate/run_tests.py gate` | exit 0, 98 tests, `baseline-gate.txt` (parent) | exit 0, 98 tests, `tests-gate.txt` |
| `python -B gate/run_tests.py elements/decisions` | not separately run | exit 0, 169 tests, `tests-decisions.txt` |
| `python -B gate/run_tests.py elements/invariants` | not separately run | exit 0, 233 tests, `tests-invariants.txt` |
| `python -B gate/run_tests.py elements/part-map` | not separately run | exit 0, 162 tests, `tests-part-map.txt` |

Additional relation checks used `--base none --merge-onto f0b5eb131de5d681ee3fcdeb264e9f88778af2ec`:

- Decisions: exit 1, `relations-decisions.txt`. Exactly seven errors: WAY-30/1, WAY-46/1 and WAY-172/1 differ from their pre-main copies, and those three plus WAY-224/1 have placeholder request links. No relation-fingerprint finding. These expected pre-main errors are retained as errors, not reported as an overall pass.
- Invariants: exit 0, `relations-invariants.txt`; no fingerprint finding.

Warnings and unchecked work remain visible:

- Five existing overdue decision reviews: WAY-03, WAY-21, WAY-52, WAY-55 and WAY-69, each check-by 2026-10-02. They are outside this task and were present in the baseline.
- Four new expected placeholder warnings for the changed/new decisions; replace the placeholders with the actual request link later.
- With `--base none`, the decision guard cannot check main-branch log preservation/version increments or template/new-version history; the invariant guard cannot check historical identifiers, versions, corrections or violated-invariant history.
- With `--merge-onto none`, TODO content, common version copies and relation fingerprints are unchecked. The supplemental relation runs do check fingerprints against the named tip; they do not manufacture a main history.
- Part-map guard: both critical-flow tests leave no coverage file, so their part lists remain unchecked; no command reports change paths for promise levels or the dependency graph, leaving those and new/stale dependency violations unchecked; without a base, known violations, identifier history and criticality lowering are unchecked.
- No `human_verdicts.md` exists and no human verdict is supplied. Existing `surface-promise-level1` debt remains in the violated-invariants file. No full gate exists, and none of these results is called a full-gate pass.

## Stage boundary and next work

Only `foundations/decisions.md` and `foundations/invariants.md` are to be committed in this stage. The source task, vault, integration checkout, operational Markdown and invariant tests are untouched. Reports and temporary scripts are ignored cycle evidence.

The next stage implements To do 2–9, with WAY-224 available for candidate routing. It must preserve the distinction between task-authorized recording and recording the answer as an open-request correction, keep the counterargument requirement local, and keep independently assessed commits named by hashes only. README edits use the previously authorized Change mode of maintain-instruction-files. Read the vault rulebook and skill conventions before skill edits as routed by the handoff.

The orchestrator still owns independent foundation assessment, later return/reconciliation against the current foundations tip, final relation checks against that current tip and replacing request-link placeholders. No new human answer or invariant implementation is outstanding at this foundation boundary.

Commit: `3d0fa8480fdae3af92ca0493b4237bfa0950223d` — `Clarify accepted decision changes and failure-mode questions`.

Changed files: `foundations/decisions.md` +70/-19; `foundations/invariants.md` +6/-6; total +76/-25. `git diff --check` passed before commit. Explicit path staging included only those two files. The initial whole-foundation search is in the commit message; the independent assessment and final reconciliation still belong to their later stages. The post-commit tracked worktree is clean; commit author email is the private-repository address.

All four test commands finished with exit 0 (662 tests total). The three no-main format guards finished with exit 0; the separate merge-onto decision result remains exit 1 with the seven expected errors described above. No unresolved author-stage blocker remains. The existing review deadlines, partial-check limitations and later-stage duties listed above remain open and must not be hidden by the passing tests.
