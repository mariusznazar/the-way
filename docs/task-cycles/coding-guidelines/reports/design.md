# Design report — coding guidelines (step 6 of the task cycle)

Design agent: Claude Code general-purpose subagent, claude-opus-5-5, one turn. Spec:
[../spec.md](../spec.md). Handoff: [design-handoff.md](design-handoff.md). Nothing tracked was
edited; nothing was committed.

## 1. Inputs read (all at `235b0b4`, branch `claude/gallant-albattani-3k15lc`, = `foundations` tip)

- Frozen task `task-frozen.md` (whole) and `cycle.md`.
- Research (read-only vault copy at `cf7eefd`): `research_open_mercato.md` (whole),
  `research_podejscia.md` (whole), `research_the_way_stan.md` (whole), `research_vault_kurs.md`
  (headings and part A1–A3; parts B–F not read — material, not decisions, per its own preface).
  The styleguide task document `wytyczne_produktu_styleguide.md` was not read: the task quotes what
  it needs from it (Q2a, Q6 anchors), and the styleguide decisions WAY-173..192 carry its outcome.
- the-way: `AGENTS.md`, `agent-instructions/README.md`, `foundations/part_map.md` (whole),
  `elements/common/way_of_working.md` (whole), `foundations/decisions.md` (whole — all 178
  decisions), `foundations/glossary.md` (whole), `foundations/invariants.md` (entries listed in §5),
  `foundations/violated_invariants.md`, headings of `foundations/environment_facts.md`,
  `elements/invariants/template.md` (whole), `elements/glossary/template.md` (to "Avoid").
- Code and templates: `product-guidelines/template.md`, `product-guidelines/styleguide/template.md`,
  `product-guidelines/styleguide/SKILL.md`, `product-guidelines/form_check.py` (whole), the test
  files' docstrings, classes and test names, `test_form_check_invariants.py:461-505`;
  `installation/install.py` (`SKILLS`, `skill_wrapper`, `product_guidance` head),
  `installation/README.md`, `installation/test_styleguide_installation.py` (head);
  `gate/run_tests.py` and `gate/method_script.py` (docstrings); `elements/common/guard_shared.py`
  (`parse_fields`); `elements/decisions/format_guard.py` (binding text attribute);
  `task-cycle/skill/SKILL.md` steps 6–11.
- Reference: the previous cycle's spec, `git show cf27d79:docs/task-cycles/product-guidelines-styleguide/spec.md`
  (structure, §§1–9); its design report was not needed.
- Method: Superpowers 6.4.1 `brainstorming/SKILL.md` and `spec-document-reviewer-prompt.md` from the
  clone at tag `v6.4.1` (`git describe` → `v6.4.1`). `visual-companion.md` not read: no visual
  question arose, so the skill never offers it.

## 2. Classification and how the method ran

**Architectural.** The task adds a discipline with two file forms, a skill, changes the form shared
by all guidelines and the form check's reading of templates (an interface products depend on), and
writes 20 decisions — "changes that restructure how components fit together or alter interfaces
others depend on". When in doubt the skill takes the heavier path; there was no doubt.

Cycle overrides applied: the dialogue partner is the orchestrator; every question the skill would
ask the human was answered from the task, its sources, the foundation or the code, or taken as the
smallest reversible interpretation and marked for orchestrator ruling. The architectural checklist
ran as: explore context (§1); clarifying questions answered from sources (§3); 2–3 approaches per
open choice (§3, §4); design in sections (the spec); design approval taken as provisional
orchestrator go-ahead; spec written to `spec.md` (not `docs/superpowers/specs/`), not committed (the
handoff forbids commits); inline self-review (§8). Stopped before `writing-plans`.

Intent, written back: the outcome, audience (an agent writing a product's code; Mariusz approving
decisions he cannot judge as code), constraints and success are the task's *Need* and *To do*; no
question of purpose was open.

## 3. The seven carried questions

| CQ | Way chosen | Ways weighed | Evidence | Cost if wrong | WAY-135 |
|---|---|---|---|---|---|
| 1 — how the test cases are taken from the file and run | a rule naming an invariant holds one fenced block `good <path>` and one `bad <path>`, each the whole text of a file of the product; the gate (later, method `TODO`) or the reviewer (now) puts that file in place in a scratch worktree of the commit and runs the invariant's declared command; the-way's code stays stdlib + git (WAY-38), the tool is the product's command | F1 all disciplines (chosen, **for ruling**); F2 coding only; F3 no form, the reviewer turns each use into a change; a unified diff instead of a whole file (rejected: a diff on a lockfile rots at the next edit and then cannot apply); paths to example files committed in the product (rejected: a bad example in the tree breaks the invariant itself) | row 11 makes the uses test cases for all guidelines; Q12 puts the run in the gate, until then the reviewer; WAY-61 makes such runs evidence about the check, not results; Semgrep/ast-grep/ESLint pair valid and invalid cases (`research_podejscia.md` §5.3) | F1 wrong: styleguide rules carry code blocks they did not need and the existing valid styleguide fixture of the invariant tests is rewritten (an invariant-test change, assessed); F3 wrong: every product's guidelines are rewritten when the gate arrives | open design choice (sets a template rule and WAY-168's content) |
| 2 — which part owns the tools' configuration | the part holding the build configuration (WAY-44: "the files that serve the whole repository — the lockfile and the build configuration — are a part of their own") | the agent-directing part (WAY-44 lists "the configuration of agents' tools and of CI" there) | the configuration decides invariants over every code part and changes with the lockfile's pinned versions; a change there lies on every flow (WAY-45), the sharpness a rule switched off deserves | wrong: changes to linter configuration are checked as agent-instruction changes, lighter where that part is less critical; a product's map can move it | how to make (a reading of WAY-44 in the skill's text), **for ruling** |
| 3 — how a product with the-way installed gets the skill | the existing pin-move task: delete wrappers, rerun the installer at the new commit; the block changes because `product_guidance()` lists `SKILLS`, so the task removes it first | a migration mode of the installer (rejected: new surface for one skill, `installation-command` would change) | `installation/README.md` "Files in the product" | none beyond the documented pin move | how to make |
| 4 — English words | "exemplar", "standing check", "kind of code" (plain, no entry); "false alarm" as a third term **for ruling** | "pattern" (taken twice: WAY-44/167, WAY-179), "reference file" ("reference" is WAY-169's in guidelines), "guard" (last word of "format guard", WAY-94/99), "element" (glossary term), "baseline check" (collides with the audit's baseline) | `foundations/glossary.md`, WAY-94, WAY-95, WAY-99 | a word clashing with a term reads two ways in a sentence a test cites (WAY-99) | open design choice (sets glossary entries), worded through `record-glossary-term` |
| 5 — two file forms in the form check | the coding template holds `## Required form` and `## Required form of a kind`; files `coding.md` and `coding-<kind>.md`; role-table checks run only on a roles table, other tables checked for header, cells and their own rules | one form with optional sections (rejected: the form check could not tell a missing section from a file of the other kind); a field *Kind* in the header (rejected: the name already carries it, WAY-167) | `form_check.py:261-363`, `:837-878` | wrong table columns: a later version of the template, products not yet holding coding files | how to make for the reader; the tables' columns are template rules, open design choices carried by WAY-198/199/212 |
| 6 — rule list vs WAY-86/WAY-60; pinning | one environment fact per adopted edition of a rule set; the blocking rules stand in the adopting decision as "the set minus the rules kept as examples"; a second invariant keeps the configuration to that list (**for ruling**); exact versions in the product's lockfile, run from the product's environment; a tool bump that changes the edition changes the decision and the fact | a fact per rule (rejected: one source edition, one reason to change, WAY-76; dozens of facts with one cause); the list only in the configuration file (rejected: WAY-60 — moving it would take no decision); the list in the method's command (kept as the alternative to the second invariant, per tool) | WAY-86, WAY-76, WAY-73, WAY-60, WAY-61, WAY-191 (fact per WCAG criterion, a catalogue whose requirements are prose, unlike a linter whose rules are executable) | a fact per edition misses a rule renamed between editions only until the version moves, which changes the decision anyway | open design choice (content of WAY-204/207 and the template's rules) |
| 7 — tool output to a verdict per invariant | each invariant's command is a script the product declares that runs the tool and writes the-way's record of a run (WAY-74); no adapter in the-way now | a generic adapter in the-way reading SARIF or exit codes (rejected for now: the gate is another task, and exit codes differ by tool — 2 for a crash in ESLint and Ruff, 127/128 in OSV-Scanner — so a generic mapping would pass a crash as a fail or worse) | WAY-61, WAY-74, WAY-38, WAY-189 ("each checked by a script the product declares") | each product writes three small scripts; a later gate can add an adapter without changing guidelines | how to make (precedent WAY-189) |

## 4. The 25 rows

Each row's entry, identifier, relations and verification stand in spec §8.1–§8.2 (decisions), §2
(glossary) and §8.5 (row 13). Summary:

| Row | Kind | Entry | Derives / narrows | Verified by |
|---|---|---|---|---|
| 1 | decision | WAY-167 edited in place | — (no fingerprinted dependents) | level 2; form check through `guidelines-check-form` |
| 2 | decision | WAY-198 | WAY-22, WAY-193 | `guidelines-check-exemplar` |
| 3 | decision | WAY-200 | WAY-198 | level 2 |
| 4 | decision | WAY-199 | WAY-172, WAY-198 | `guidelines-check-exemplar` |
| 5 | decision | WAY-202 | WAY-193 | `guidelines-check-form` |
| 6 | decision | WAY-206 | WAY-202, WAY-60 | level 2 |
| 7 | decision | WAY-203 | WAY-202 | level 2 |
| 8 | decision | WAY-204 | WAY-203 | level 2 |
| 9 | decision | WAY-205 | WAY-51, WAY-60 | level 2 |
| 10 | decision | WAY-196 | narrows WAY-168, derives WAY-08 | `guidelines-check-carrier` (edited) |
| 11 | decision | WAY-168 edited in place | dependents renewed: WAY-171, WAY-173, WAY-188, `guidelines-check-carrier` | `guidelines-check-example-files`, `gate-guidelines-example-evidence` |
| 12 | decision | WAY-197 | WAY-168, WAY-69 | level 2/3 |
| 13 | invariant | `gate-guidelines-example-evidence/1`, method `TODO` | WAY-168 | — |
| 14 | decision | WAY-194 | WAY-113, narrows WAY-114 | level 2 |
| 15 | decision | WAY-212 | WAY-128, WAY-129 | `guidelines-check-kind-index` |
| 16 | decision | WAY-193 | WAY-168, WAY-100 | level 2 |
| 17 | decision | WAY-195 | WAY-100 | level 2 |
| 18 | decision | WAY-208 | WAY-193 | level 2 |
| 19 | decision | WAY-209 | WAY-193 | level 2 |
| 20 | decision | WAY-210 | WAY-193 | level 2 |
| 21 | decision | WAY-211 | WAY-122, WAY-120 | level 2 |
| 22 | decision | WAY-201 | WAY-200 | level 2 |
| 23 | decision | WAY-207 | WAY-172, WAY-193 | level 2 |
| 24 | glossary term | "exemplar" | — | glossary guard |
| 25 | glossary term | "standing check" | — | glossary guard |

Edits in place before `main`: WAY-167, WAY-168 (decisions, README "edit an existing decision in
place", shown for renewed acceptance, WAY-07) and `guidelines-check-carrier` (invariant, version
kept at 1 — precedent: `guidelines-form` reworded at /1 in commit `19d28f8`). WAY-114 is narrowed,
not edited. `guidelines-form/1` is deliberately not reworded (products copy it).

## 5. Foundation selection (WAY-150)

Touched parts (prospective): product-guidelines, decisions, invariants, glossary, gate (new gate
invariant), installation (`SKILLS`), agent-instructions (entry points), task-cycle (§7 sentence),
part-map (failure modes), instruction-files (WAY-212's relation).

- **Decisions read whole:** all 178 of `foundations/decisions.md`. Every decision whose *Scope*
  names a touched part is therefore read; no *Scope* was missing or malformed.
- **Invariants read whole:** `invariant-method-form`, `invariant-test-break`,
  `repository-file-location`, `element-directory-contents`, `relation-model-directory-contents`,
  `foundation-change-assessment-record`, `return-step-record`, `level-one-decision-invariants`,
  `verification-invariant-derivation`, `derived-file-content`, `derived-subset-naming`,
  `ci-checking-commands`, `gate-check-source`, `skill-rule-source`, `script-language`,
  `script-imports`, `script-subprocesses`, `map-guard-missing-command`, `invariant-recovered-form`,
  `invariant-recovered-derived`, `gate-fork-point-evidence`, `invariant-fingerprint-input`,
  `method-gate-values`, `gate-verdict-per-entry`, `gate-pass-without-verdict`, `gate-method-order`,
  `invariant-part-names`, `invariant-part-form`, `change-reach`, `gate-result-values`,
  `gate-unchecked-reason`, `gate-missing-script`, `gate-reported-set`, `flow-test-run`,
  `gate-exit-code`, `invariant-citation-target`, `data-line-target`, `invariant-tests-of-change`,
  `skill-entry-points`, `instruction-file-imports`, `root-claude-md-import`,
  `installation-claude-guidance`, `project-plan-state-evidence`, `project-plan-state-subprocesses`,
  all eight `guidelines-*`, the withdrawn, quarantined and recovered lists, and the list of violated
  invariants.
- **Discovered only (headings or counts):** the other invariants (213 headings listed; 55 name
  `every` or `product-guidelines` — those not listed above concern the decision log's, map's,
  glossary's and facts' own forms and were judged not reached by this change); the 30 environment
  facts (headings: none on linters, formatters or audits).
- **Glossary:** all 34 terms read.
- **Part map:** whole.
- Expected *Scope* matches vs selection: identical (whole log read). Dependents searched by
  fingerprint: `@681d47ff` (WAY-167) — none; `@47d9d53e` (WAY-168) — WAY-171, WAY-173, WAY-188,
  `guidelines-check-carrier`.

The whole-foundation search of WAY-33 for each entry is the foundation author's in the cycle; this
selection is design input, not that search.

## 6. Items marked for orchestrator ruling

1. **F1** — test cases as whole files in `good <path>` / `bad <path>` blocks, for every discipline,
   enforced by the form check (spec §5.1, §8.4.1). Alternatives F2 (coding only), F3 (no form).
   Cost if wrong: see CQ1.
2. **"false alarm"** as a third glossary term beyond rows 24–25 (spec §2). Alternative: the meaning
   stays in WAY-204's words without an entry (WAY-95 keeps definitions in the glossary). Cost if
   wrong: a term the human did not list as a row (its meaning is the human's, Q14), or a binding
   sentence that defines a word.
3. **Inline suppressions** of a blocking rule count as breaks (spec §4.3, §8.4.3). Alternative:
   suppression allowed with a decision reference. Cost if wrong: either a product cannot silence a
   rare true report it chose to accept (it must change the decision), or a blocking rule is silenced
   file by file, which row 23 forbids in spirit.
4. **The linter's configuration kept to the decision's list by an invariant of its own** (spec
   §4.3 (2)); alternative per tool: the method passes the list. Cost: one more product script.
5. **CQ2** — tools' configuration in the build-configuration part (reading of WAY-44).
6. **Two failure modes** at `product-guidelines` (spec §8.6). Alternative: none.
7. **Review when** of WAY-195 (none), WAY-197, WAY-204, WAY-206, WAY-209 (spec §8.2).
8. **The task-cycle sentence** (spec §7): the reviewer runs the test cases until the gate does.
   Alternative: no change to the cycle — then WAY-197's clause binds nothing an agent reads in a
   product cycle. It is not review of code against guidelines (out of scope).
9. **Kind table design** (spec §4.2–§4.3): `## Files of this kind` with *File | Status | Decision*,
   statuses `exemplar` / `copy` / `do not copy`, exactly one exemplar whose decision names its path
   and kind — the mechanism that makes "another file as exemplar takes approval" (row 4) hold
   without memory. Alternative: a header field naming the exemplar and no check of the decision's
   text. Cost if wrong: a later template version; no product holds such files yet.

No question blocks the rest of the design.

## 7. Rejected alternatives (beyond the task's own)

- A generic exit-code adapter in the-way now (CQ7) — tools' exit codes differ; the gate is another
  task.
- One environment fact per lint rule (CQ6) — WAY-76.
- A diff as the form of a test case (CQ1) — rots on files that change, such as lockfiles.
- Rewording `guidelines-form` to name the new tables and blocks — breaks every product's copy at a
  pin move; its sentence already covers them.
- Rewording `guidelines-check-form` — its generic sentence already covers two forms and required
  rules; only tests and *Derives from* change.
- Editing WAY-171 to list the test-case blocks — WAY-168's edit carries them, and WAY-171's fields
  stay; kept as a concern (§8) in case review prefers the form in WAY-171.
- An inventory of every file of a kind (Open Mercato's ledger) — no row asks for it; it would grow
  with every file.
- `file:line` in the kind file's table — stale at the next edit (WAY-51's rejected line numbers);
  the audit's proposal in the task document carries them (row 22).
- Changing `refine-task` — out of scope (detection goes to the task-cycle-on-guidelines task).

## 8. Concerns and self-review

Self-review (placeholders, consistency, scope, ambiguity) done inline; fixed: `guidelines-check-kind-index`
derives from WAY-212 alone, since WAY-167's verification stays level 2.

Concerns for the spec reviewer and the foundation author:

- **WAY-171's fields.** WAY-171 lists a rule's fields D/I/G/B; the test-case blocks live in the
  rule's text under a template rule citing WAY-168. A reviewer may prefer the form stated in WAY-171
  (an extra edit with dependents `guidelines-form`, `guidelines-check-form` to renew).
- **`guidelines-form` covers the new findings by reading** "rules, rule fields and tables … each with
  the values and the links those templates give it" (spec §5.2 item 7). If review disagrees, the
  choice is between rewording it (breaking copies) or a third invariant of guidelines products copy.
- **The audit's database moves with no commit** (WAY-206): a rerun on one commit can go from
  `pass` to `fail`, which WAY-68 treats as a flipping check; WAY-60 allows a decision to place the
  condition in the named database, but its rationale (movement visible) is only partly kept.
- **`test_form_check.py` uses `guidelines/coding.md` as a discipline with no template**
  (`:142-145`, `:264-277`); those ordinary tests must move to another name, or they fail once the
  coding template exists.
- **`read_templates` raises on any discipline table without role columns** (`form_check.py:349-354`);
  the coding template cannot land before that check is generalized — the plan must order the code
  change with or before the template.
- **Info strings and `check_instructions.py`**: the spec assumes that script treats a fence's
  opening line as code; not verified.
- **Sources of WAY-195** were not re-read by this agent (quoted from the private research with
  their public paths and commit); the foundation author re-reads them (spec §8.3).
- **Python 3.13.16** in the harness against the declared 3.14 (cycle choice O3).

## 9. Unchecked

- No command was run beyond reading (no tests, guards or form check); nothing was implemented.
- Open Mercato's repository and the CACM paper were not opened in this turn.
- `research_vault_kurs.md` parts B–F and the styleguide task document were not read (see §1).
- The visual companion was not used (no visual question).

## Revision after spec review

Turn 2. Inputs: `spec-review.md` (read whole), `design-rulings.md` (C1–C17, read whole). Only
`spec.md` was rewritten and this section appended; nothing tracked edited, nothing committed. The
spec now reads as settled: no "for orchestrator ruling" marker remains (the one "proposal" left, in
§6.2 step 3, is the skill's own word for a palette or choice read off the code, WAY-175/WAY-29).

### Per finding and ruling

| Finding / ruling | Change in `spec.md` |
|---|---|
| C1 (F1) | §5.1 states F1 as settled for every discipline; a test case may be a short new file at a path that does not exist |
| C2 | §2: "false alarm" row says no planned entry, meaning in plain words in WAY-203/204, fallback through the glossary skill listed as new in the request; §1 counts two terms; §8.2 WAY-203/204 meanings reworded in plain words; notes line added |
| C3 + Minor 5 | §4.3 `### Linter` invariant 1 and §4.4: suppressions as breaks, template text citing WAY-203 and WAY-193, binding through adoption |
| C4 | §4.3 `### Linter` invariant 2 gives both ways; §6.2 step 4 settles which with the human |
| C5 | §3.2 and §6.4: through `update-part-map`, to the build-configuration part; the-way fixes no part |
| C6, C7, C8, C9 | "(proposal)" removed from §8.6, §8.2 *Review when*, §7, §4.2–4.3 |
| I-1 / C11 | §5.1 exemption: a rule whose *Invariant* is the product's copy of `guidelines-form` gives descriptions, no blocks; §5.2 item 5 skips such rules; WAY-168's edit (§8.1) carves out "an invariant checking the guidelines' own form"; `guidelines-check-example-files` and the gate invariant say "with test cases" |
| I-1 / C12 | §5.1: short files, 1 MiB limit of the file of guidelines, outer fence three backticks, no fence-opening line inside a case, info string only from an opening fence (§5.2 item 5 reports a fence line inside a case); §4.3 gives the shape of the cases for each standing check and requires the product's scripts to read a short file at a new path; §5.3 adds those crafted inputs |
| I-2 / C10 | §4.3 audit invariant reads the database "when the check runs"; §4.4 says so; WAY-206's meaning (§8.2) names both weak points and that WAY-68 answers a flip unchanged; §6.2 step 4 names the weak point to the human; §9 has the request name it; §10 adds the WAY-61/WAY-68 reading |
| I-3 | §4.3 new bullet: each standing-check invariant's *Part* names the parts holding code and the part holding the build configuration and lockfile; the audit's names the parts of every manifest and lockfile it reads; §10 adds the WAY-62 reading |
| I-4 / C13 | §4.3 `## Files of this kind`: the audit lists every existing file with its status, later files need no row until a refresh, no completeness checked; §5.2 item 4; §6.2 step 1 (refresh audits each kind again) and step 3 (judge every existing file); WAY-200's meaning |
| Minor 1 / C14 | §4.3 new bullet stating what the product's copy of `guidelines-form` carries; §5.2 item 7 gives the reading (a *File* that must exist is a link the template gives; Q15) and keeps `guidelines-form/1` unedited |
| Minor 2 | §3.1: the common template's *Good*/*Bad* "describe" a use; §5.1: blocks after the four fields, in the rule's body; §8.1 notes WAY-171 stays true; §10 adds the WAY-171 line |
| Minor 3 | §3.1: the common template's "Where guidelines go" gains `coding.md` and `coding-<kind>.md` |
| Minor 4 | chosen: the table of kind files stands in WAY-212 alone (§8.1 WAY-167 text names files and what each holds, not the table); WAY-167 stays level 2 |
| Minor 6 | §4.3 and §6.2 step 4: severity is the product's choice with "every severity" open; §8.3 names Open Mercato's `--severity high` among what is left |
| Minor 7 | §4.4: what the fact's sentence holds (the set's membership at the edition) and why it is one fact under WAY-76, against WAY-191's fact per criterion; WAY-204's rationale carries it (§8.2) |
| Minor 8 | §6.2 step 3: trial run in a scratch worktree or temporary environment, tracked files untouched; §6.1 says the skill leaves tracked files as they were; §6.3: the orchestrator also starts the fresh agent judging the trial run |
| Minor 9 | §6.6: the installer's crafted-input check (existing refusals now for the new wrapper path); §9 lists it |
| Minor 10 | §2: the reason for plain "kind" corrected (WAY-176 uses it plainly; WAY-99 applies only to an unusual meaning) |
| Minor 11 | §2: the exemplar's definition keeps what separates it from the plain sense, or the entry records why it qualifies under WAY-95 |
| Minor 12 / C16 | §9: the request says nothing runs product invariants before a gate, apart from a cycle running the methods a change reaches |
| C17 | not mine (`cycle.md`, orchestrator) |
| Observations | §8.4 replaced by "Rulings applied", mapping C1–C16 to sections |

### My own choices in this revision, with cost if wrong

- **Minor 4: the table in WAY-212 alone**, rather than WAY-167 at level 1 naming
  `guidelines-check-kind-index`. Reason: WAY-212's row 15 is the settlement that names the table;
  WAY-167 answers where files stand and what they are named. Cost if wrong: the assessment asks for
  level 1 on WAY-167 — one *Verification* line and one *Derives from* entry on the invariant.
- **WAY-168's edit carves out "an invariant checking the guidelines' own form"** in its binding
  sentence, so that C11's exemption is stated by the decision the template rule cites, not by the
  template alone (WAY-171: a template rule cites a decision that sets it). Cost if wrong: a longer
  sentence; the alternative is a fourth sentence elsewhere.
- **The gate invariant and the cycle sentence say "names with test cases"**, so exempt rules raise
  no "could not be checked" line each time their invariant changes. Cost if wrong: none for the
  gate (method `TODO`); a reviewer reading literally skips exempt rules, which C11 intends.
- **WAY-203/204 worded around "a report leading to no change of code worth making"** in place of a
  term (C2). Cost: longer binding sentences; the glossary skill may still require the entry.
- **The audit's *Part*** names the parts holding manifests and lockfiles; where those lie in the
  build-configuration part, that part. Cost if wrong: in a product with per-package lockfiles in
  code parts, the skill names those parts — the template's wording covers it.
- **§6.6's installer check** is the existing refusals extended to the new path, no new parsing tested.
  Cost: an installer regression on paths specific to this skill would be missed only if refusals
  were path-specific, which they are not.

### Still open

- Nothing blocks the plan. Left to the request and to Mariusz: the audit's flip (C10; he may prefer
  narrowing WAY-68), and every ruling C1–C16 as the orchestrator's provisional choice.
- Left to the foundation author: whether the glossary skill still requires "false alarm" (C2), and
  the exemplar's definition (Minor 11); re-reading the public sources quoted in WAY-195.
- Unverified, as before: how `check_instructions.py` reads an info string on an opening fence (the
  review read its `FENCE` toggle; C12's rule keeps cases free of fence lines, so the toggle stays
  right either way).

## Re-review fixes (C18–C21)

Turn 3. Inputs: "Re-review of the revision" in `spec-review.md` (N-1..N-4) and C18–C21 in
`design-rulings.md`. Only the lines below changed in `spec.md` (line numbers after this turn);
nothing else was touched. Nothing tracked edited, nothing committed.

| Ruling (finding) | `spec.md` lines | Change |
|---|---|---|
| C18 (N-1) | 241-254 | §4.3: a pair for each invariant the rule names; pairs for `### Linter` invariants 2 (configuration file with a blocking rule turned off / exact) and 3 (new file with one report / none) |
| C18 | 298-304 | §5.1: one `good <identifier> <path>` and one `bad <identifier> <path>` block per named invariant other than `guidelines-form`; the method of the invariant the info string names |
| C18 | 310-311 | §5.1: in a rule carrying test cases every fenced block of its body is a case; illustrative code goes to `## Examples` (needed for C21's rule) |
| C18, C21 (N-4) | 361-371 | §5.2 item 5: pair per named invariant; a block naming an invariant the rule does not name is an error; fence-opening line inside a case defined (tilde, backticks with text); any other fenced block of such a rule, as left by a bare fence, reported at its opening line as a malformed test case; a case open to the end reported at its opening line; a rule naming only `guidelines-form` needs no blocks |
| C21 | 319-323 | §5.1: what a bare three-backtick line inside a case does and what the form check reports |
| C18, C21 | 398-406 | §5.3: new crafted inputs (missing identifier, wrong identifier, pair for one of two invariants) and the expected report of each fence case |
| C19 (N-2) | 306-309 | §5.1: cases of a listed invariant read against the commit's own result; the per-file companion (WAY-205, WAY-190) takes the strict reading |
| C19 | 252-254 | §4.3: the same, for `### Linter` invariants 1 and 3 |
| C18, C19 | 519-525 | §7: the reviewer runs the pair whose info string names the invariant; the relative reading for a listed invariant |
| C20 (N-3) | 534-540 | §8.1 WAY-167: keeps the general file's table of kind files with when to read (row 1 whole); level 1 `guidelines-check-kind-index`, deriving from WAY-167 and WAY-212; WAY-212 keeps the pointer and each row's "when to read". Replaces my Minor 4 choice |
| C18, C19 | 542-546 | §8.1 WAY-168: the cases given per named invariant, read against the commit's own result for a listed invariant (in the binding sentence, as C19 allows) |
| C18–C21 | 648-651 | §8.4: four rows mapping the rulings |
| C20 | 658 | §8.5: `guidelines-check-kind-index` derives from WAY-167, WAY-212 |
| C18, C21 | 660 | §8.5: `guidelines-check-example-files` meaning names the pair per invariant and the malformed case |
| C18, C19 | 661 | §8.5: gate invariant reads the pair whose info strings name the entry, and the relative reading for a listed entry |
| C18, C21 | 692-695 | §9: invariant tests for the pair per invariant, a wrong identifier, and a bare fence closing a case early |

My choices, with cost if wrong:

- **C19 placed in WAY-168's binding sentence**, not only its *Verification*: the relative reading
  changes what "passes" means, so it binds. Cost: a longer second sentence; still three sentences.
- **Every fenced block in a rule carrying test cases is a case** (C21's mechanism): it lets the form
  check report the stray block a bare fence leaves without guessing. Cost: a rule cannot hold an
  illustrative code block; it moves to `## Examples`.
- **The shortened `good` block still counts as that invariant's good case**, so a bare fence gives
  one error (the malformed block), not two. Cost: the error message must make clear the case was cut.

Open: none from this turn.
