# Design report — product guidelines, styleguide first

Stage: step 6 of `task-cycle/skill/SKILL.md` (design). Agent: design subagent, claude-opus-5-5.
Handoff: [design-handoff.md](design-handoff.md). Output: [../spec.md](../spec.md). Foundation
selection: [foundation-selection.md](foundation-selection.md).

## Classification

Superpowers 6.4.1 `brainstorming`, read whole from the plugin cache with
`spec-document-reviewer-prompt.md` and `visual-companion.md`. Path: **architectural** — a new
part of the-way (templates, a skill, a script reading a product's files), installer changes and
some 25 foundation entries; no existing flow to change, so not bounded. The visual companion was
not offered: no question was visual, and the human is not in this loop. The human gates were
replaced by returns to the root orchestrator (handoff).

## Sources read, with versions

- the-way at `96623ed7710100fe6e11a0ce3c052fc44d4af52d` (worktree
  `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`): the frozen task; `AGENTS.md`;
  `agent-instructions/README.md`; `elements/common/way_of_working.md`, `elements/common/rules.md`
  (whole); `foundations/part_map.md`, `foundations/glossary.md` (whole); the decisions listed in
  `foundation-selection.md`; `installation/install.py` (whole) and `installation/README.md`;
  `project-level/technology/SKILL.md`, `project-level/task/skill/SKILL.md` (whole);
  `elements/invariants/template.md` (opening and entry form); parts of
  `elements/decisions/format_guard.py`, `elements/common/guard_shared.py`,
  `elements/glossary/format_guard.py`, `agent-instructions/skill_entry_points.py`,
  `instruction-files/check_instructions.py`, `task-cycle/skill/SKILL.md`.
- Research subagents (same model, read-only; their causal readings treated as hypotheses and
  checked where the spec relies on them). Sanitized copies (scratchpad and private-note paths
  replaced by placeholders):
  - [research-decision_map.md](research-decision_map.md) — all 152 decisions, 210 invariants, 30
    facts, keyword sweep;
  - [research-code_contracts.md](research-code_contracts.md) — fingerprint, guards, gate, installer,
    entry points, instruction files, element skills, settle-technology, task-cycle, layout;
  - [research-outside_sources.md](research-outside_sources.md) — m2l5 rows 1–25 and Notatki
    (private notes, read only), the lesson, `loop2-10x` `10x-ui` with its reference, `loop`
    `715026e` `om-ux-shape`/`om-ux-setup`, `loop` `315c443` trial, `loop2` part map.
- The user's skill conventions note (read whole); the repository's layout takes precedence.

## Questions sent to the root and answers (provisional, under the user's delegation)

| # | Question | Answer (root) |
|---|---|---|
| Q1 | Where does the skill run relative to a task (WAY-01, WAY-28, WAY-106)? A refinement / B writes styleguide and entries itself, then hands code to the cycle / C writes everything | **A** (C5): the conversation's meanings reach the task document through `refine-task`'s *Settlements to record*; `refine-task` and `implement-task` unchanged; the template carries the guidance the cycle's author needs; state row 24's mapping |
| Q2 | Part identifier: `product-guidelines` or `guidelines` | `product-guidelines` (C6) |
| Q3 | Product path | `guidelines/<domain>.md`, `guidelines/styleguide-<part>.md`, through `update-part-map` (C7) |
| Q4 | How the product's form invariants get verdicts: fixed identifiers given by the template, or a `--cite` argument | fixed identifiers; record the weak point (C8) |
| Q5 | A required section dropped as `none — <decision>@<fp>` | yes (C9) |
| — | Contradictions 1–5 | WAY-09 edited in place, change of meaning shown at the request; readings 2–4 stated in the spec; 5 settled by Q1 (C10) |

## Choices, with evidence, alternatives and cost if wrong

| Choice | Evidence | Rejected | Cost if wrong |
|---|---|---|---|
| New part `product-guidelines`, directory of the same name (root C6) | WAY-09 lists closed directories; WAY-93 / `glossary-term-collision` warns a term and an identifier read alike, exempting only element directories; `read_alike` in `elements/glossary/format_guard.py:1347` | part `guidelines` (warning, then a rename, or widening WAY-93); folding into `instruction-files` (different failure modes, WAY-09 rationale) | renaming a directory and a part before `main`: low |
| WAY-09 edited in place (root C10) | WAY-07; `agent-instructions/README.md` "edit an existing decision in place" | a new version WAY-09/2 | none before `main` |
| Product path `guidelines/…` in the agent-directing part (root C7) | row 1; WAY-44; `loop2` `agent-workflow` claims no such path | `docs/` (row 1 rejects); the agent part's own directory (differs per product, the form check could not find it) | a convention path baked into the installer guidance and the form check: medium after products adopt it |
| Skill as refinement, cycle writes everything (root C5) | WAY-01 (entries merge with the code that follows), WAY-28, WAY-30, WAY-69, WAY-134; `refine-task` step 5 already turns a conversation into rows | the skill writing entries or code itself | if wrong, a second route for styleguide entries later; the cycle's author lacks conversation detail — mitigated by the fixed *To do* list and the template's "Writing the file" |
| Common form governs every domain; a domain template only adds (**autonomous**) | row 1 ("dalej np. standardy kodowania"); smallest reversible | a closed list of domains the-way has templates for | a product's untemplated guidelines get a weaker check: low |
| Binding rule names ≥1 decision; invariant where there is one; a styleguide rule ≥1 invariant | row 2 with row 18 ("tym styleguide zawęża wiersz 2" only makes sense if row 2 does not require an invariant everywhere); WAY-22 | an invariant required in every domain | a coding-standards rule an agent cannot check would have to become an example: low |
| Fixed product invariant identifiers cited by the script (root C8) | element guards cite the-way's invariant identifiers as literals (`elements/decisions/format_guard.py:429`) | `--cite <id>/<version>` | a product rewording the sentence breaks the citation (weak point, recorded in spec §3) |
| Meanings stand in product decisions, repeated in the styleguide under fingerprints | WAY-60, row 24, row 5; WAY-05 (≤3 binding sentences) | meanings only in the styleguide (a condition outside the foundation, and meanings change without a decision) | two places to read; the fingerprint stops drift |
| Form check checks against the same commit always, the merged foundation with `--merge-onto` | `relation-fingerprint-value`, decisions guard's merged log | same commit only (a parallel task's reworded decision lands unseen) | some complexity in the invariant side (§5.2 rule): medium to build, low to change |
| Bare identifiers in prose not flagged | WAY-02 ("a bare identifier … never flagged") | a fingerprint on every mention (narrows WAY-02) | none |
| No new critical flow (**autonomous**) | WAY-45 flows are chosen; detection already by an invariant | extending `wording-reaches-dependants` | a later gate test: low |
| Size limit 1 MiB (**autonomous**) | WAY-48, guidelines are short | none | a huge styleguide refused: low, a constant |
| Guidelines' prose in English (**autonomous**) | WAY-72 for entries; read side by side | the product's language | a product preferring another language edits a template rule: low |
| Installer guidance line naming the form check | the block already names the format guards; no gate runs checks yet | no line (nothing would run the check before a merge) | the block text changes; pin moves already remove it (README) |
| The skill asks whether a law binds before proposing WCAG | WAY-86's last sentence, WAY-46 | always proposing adoption | none; one question |
| Styleguide not a second glossary term | WAY-95; binding sentences can say "the guidelines of the styleguide domain" | an entry "styleguide" (not a row; an unlisted entry is a cycle failure mode) | a WAY-33 search may still ask for it — concern below |

## Row-to-entry mapping

See spec §9.1–9.4. In short: rows 1→G1, 2→G2, 3→G3, 4→G4, 24 (+27's approval before code)→G5,
26→G6, 5+6→G7, 7→G8, 8→G9, 9→G10, 10→G11, 11→G12, 12→G13, 13→G14, 15→G15, 14→G16, 16→G17,
17→G18, 18→G19 (`narrows` G2), 19→G20, 20→G21, 21→G22, 22→G23, 23+27→G24 (`narrows WAY-114`),
25→glossary "guidelines"; WAY-100→G25; WAY-09 edited in place; six invariants of the-way
`guidelines-check-*`; part `product-guidelines` and three dependency/flow changes; the six
WAY-09 invariants renewed. Product-side entries (two form invariants, WCAG decision and facts,
first invariants, companion) are written by product tasks, not by this change.

## Contradictions found

1. Task's "new version of WAY-09" vs WAY-07/README — edit in place.
2. Task Q2a cites `om-ux-shape`'s handoff mode for announced screens; no mode enumerates screens —
   workflow step 7 and Shape template taken (`research-outside_sources.md` §D).
3. `guidelines` part vs term (WAY-93) — part `product-guidelines`.
4. Meanings and pairs in the styleguide alone would break WAY-60 and row 24 — product decisions.
5. Entries written outside a task (WAY-01, WAY-28, WAY-106) — refinement/cycle split.
Also noted, not contradictions: WAY-16 (one gate command) keeps the hard-coded rule from naming a
lint command; WAY-128 places that rule in a file loaded with the interface's files, decided by the
instruction-files skill; 10x-ui's example role `surface` is a glossary term of the-way.

## Spec self-review

- Placeholders: none (`TBD`/`TODO` absent). Identifiers G1–G25 are labels; numbers are given at
  writing.
- Consistency: §2 path ↔ §5.2 reading ↔ §8 guidance line agree on `guidelines/`; §3.3 invariant
  identifiers ↔ §5.1 record ↔ §10 tests agree; §6.2 split ↔ §7 row 24 ↔ §6.6 (cycle's author
  applies instruction-files) agree. Fixed during review: G1 *Scope* dropped `agent-instructions`
  (the product's agent part is not the-way's); G6 gained `derives from WAY-34`; level-1
  verification of G2/G3/G4/G7/G19 stated.
- Scope: one plan; no change to `refine-task`, `implement-task`, the elements' guards or WAY-04.
- Ambiguity left for the plan to settle by making, not by choice: exact wording of entries
  (the cycle's); the regular expressions of §5.3.

## Unchecked work and concerns for the spec review and planning

- No command was run against a product; the form check's merge rule for invariants (§5.2) is
  designed, not tried.
- Whether the WAY-33 search of the foundation step will call for a glossary entry "styleguide" or
  "design token" beyond row 25; the spec avoids both, but a reviewer may judge the narrower
  meaning of "styleguide" as needing one — that would be an entry the rows do not list.
- `installation` *Depends on* does not name `task-cycle` today although the installer installs
  `implement-task` and `plan-task` (pre-existing; not fixed here).
- The cycle's recognition of an unsettled meaning (row 24's blocked request) rests on
  `implement-task`'s general stop rule until the task "cycle for view changes" lands.
- The product form invariants cite version 1 as literals (root C8 weak point).
- The skill's prose is checked only by assessment and the row-to-text table, not by tests.

## Revision after spec review

Review: [spec-review.md](spec-review.md) (1 Critical, 11 Important, 12 Minor). Root rulings
recorded as C11–C22 in `cycle.md`, provisional under the user's delegation; the spec marks them
"root, finding N". Every finding was applied; the spec was rewritten whole.

| Finding | Ruling | Change in `spec.md` |
|---|---|---|
| 1 Critical — citing product invariants breaks `invariant-citation-target` | way (a) | §3.3: the-way holds `guidelines-form` and `guidelines-reference-current`, deriving from G4/G26 and G3; products hold copies; §9.3 lists them; §10 runs the invariants guard with `form_check.py` in place and the two methods on the-way itself |
| 2 — `guidelines-form` gets no verdict under `--merge-onto` | two methods | §3.3 two methods; §5.1 which checks each option selects, what `--merge-onto none` records and the resulting result (WAY-65); §10 record tests |
| 3 — `guidelines-form` misses changes to pointed files | *Part* `every` | §3.3 *Part* `every` |
| 4 — `guidelines-check-*` miss changes to borrowed parsers | name the parts | §9.3 *Part* `product-guidelines · decisions · invariants · part-map · elements-common · relation-model`; §5.5 no new flow, reason |
| 5 — "interface" vs WAY-165 | "user interface" | §1 definition and rule; G14 and every sentence; skill description; §11 item 6; no glossary entry (field meaning) |
| 6 — product copies derive from a decision that does not cover them | `Derives from: none` in products | §3.3 *Derives from* |
| 7 — role meanings have no invariant (row 18) | add the rule with an agent-run invariant | §4.1 rule "Each role in its meaning"; §4.2; §5.3 item 3 requires it to name every role decision; §6.3 step 4 proposes it; G20; `guidelines-check-carrier` |
| 8 — `none —` line and prose references escape | every token outside fenced code | §3.2, §3.3 sentence, §5.3 item 7, `guidelines-check-reference-target`/`-stale-reference`; §10 tests in departure line, prose, table, examples |
| 9 — sections neither rule nor example | rule with adopting decision and invariant, or example | §4.1 merged form with required rules; §4.2 per part: kind, carrier, proposed invariant; dropping via `none —` |
| 10 — G5 vs WAY-114 | G5 `narrows WAY-114` with area | §7; §9.1 G5 relations and note on two narrowings in disjoint areas |
| 11 — no orchestrated mode | paragraph | §6.4 |
| 12 — token values have no carrier | *To do* per role value and source | §6.2 *To do*; §4.3; §6.3 step 4 settles value and source; *Questions to settle* holds values |
| 13 — merged order | apply | §4.1 skeleton whole; examples as `###` under `## Examples` |
| 14 — one path per report | apply | §5.1 report per file, merged record |
| 15 — borrowed `merged_log` reports into the form check | apply | §5.1 own discarded report, only run failures carried; §10 test |
| 16 — wrong claims about `check_instructions.py` | apply | §3.2 corrected reason (`@` word with `.` or `/`; `/` in backticks read as a path); classes with `/` in fenced code; §10 expects no `dead-path` |
| 17 — unread files pass silently | apply | §5.2 `warning:` per unread path; §10 tests |
| 18 — tests | apply | §10: file just under the limit; invariant changed or withdrawn only on onto; network test scope and git-call capture |
| 19 — "domain" collides with WAY-95/WAY-104 | another word | "discipline" (no use in `foundations/` or `elements/common/`; checked by search); header *Discipline*; §9.1 wording; §11 item 7 |
| 20 — focus invariant rests on no WCAG fact | apply | §6.3 step 4: derives from the adoption decision, rests on the visible-focus fact |
| 21 — *Scope* of WAY-09, WAY-38, WAY-27 | apply | §2.1 edits in place of *Scope* |
| 22 — pairs pointed to vs written | state the reading | §4.2 "Pairs in code and in writing" |
| 23 — step 0, WAY-27 in the skill, `task-cycle` dependency, *Applies to* unchecked | apply | §6.3 step 0 reads `refine-task` and the task template; §6.1 describes outside sources, names none; §9.4 *Depends on* `task-cycle`; §5.3 item 5 checks *Applies to* and the file name's part against the map |
| 24 — no decision for the common form | one decision; language rule chosen | G26 in §9.1; §3.2 language rule (**autonomous**, below) |
| Unresolved concern (C5 cost) | note it | §1 "Cost the request shows" |

### New autonomous choices in the revision

| Choice | Evidence | Rejected | Cost if wrong |
|---|---|---|---|
| "discipline" for what one guidelines document covers | finding 19; zero uses of the word in `foundations/` and `elements/common/` | "area" (WAY-86 "the area of the product", WAY-25's "area where it prevails"), "subject" (WAY-96's grammatical placeholder), "topic" (WAY-18, WAY-21) | renaming before `main`: low; after, a new meaning takes a new word (WAY-97) |
| G26's language rule: structural words in English, prose in the product's own language, unset by the-way | WAY-108 keeps a definition's headings and markers in English while its content follows the human's language; the form check needs only the structural words | all of a guidelines file in English (binds every product's prose for no reader of the-way's code); the language of the conversation that wrote it (varies from session to session for a living document) | a product may mix languages across its guidelines; a later decision can fix one — low and reversible |
| Required rules as fixed English headings the form check reads (§4.1) | finding 9's ruling; the form check needs a name to find a required rule | a field marking each rule's template origin | renaming a heading is a change of the template and of every product's styleguide at its next pin move: medium, visible |
| Dropped rules use the same `none —` form as dropped sections | root C9 | a separate marker | none |
| The invariant on role meanings runs over the files of the part a change touches | WAY-62 reach; row 18's k of n | over every screen on every change | an agent run per change to the user interface's part: cost in time and model use, shown at the request |

### Self-review of the revision

- Placeholders: none. Rulings cited by finding, not by an invented C-number.
- Consistency checked: §3.3 sentences ↔ §5.3 items (form 1–6, references 7) ↔ §9.3 table ↔ §10
  tests; §4.1 skeleton ↔ §4.2 table ↔ §6.3 step 4 proposals; §5.1 option semantics ↔ §3.3 methods
  ↔ §8 guidance sentence (two runs); "user interface" and "discipline" used throughout.
- Still unchecked: no command run; the fingerprint values of WAY-09 after its edit and of
  WAY-114 for the two `narrows` were not computed (the foundation step computes them).

### Concerns remaining

- The concerns listed above stand, except "possible extra glossary entries" for "interface",
  answered by "user interface". "Styleguide" and "design token" remain possible findings of the
  foundation step's whole-foundation search.
- Fixed required-rule headings in English sit inside a styleguide whose prose may be Polish; the
  form check reads them, a human reader sees mixed language (G26's price).
- `guidelines-reference-current` with `--merge-onto none` (the-way today, a product before its
  first `main`) can never reach `pass`, only `fail` or not-`pass`; the request should name this as
  the expected state before `main` exists, as the README already does for the guards.

### Re-review of the revision (root C23)

The re-review appended to [spec-review.md](spec-review.md) found 23 of 24 findings addressed and finding 19
partly, and nine new issues (1 Important, 8 Minor). All applied:

| Issue | Change in `spec.md` |
|---|---|
| R1 — a value change made a decision | §4.2 rule "A fault of one screen is fixed in its component": a change of a design token's *meaning* is a decision, a change of its value that keeps its meaning is not; the proposed check judges meanings (agent) or keeps every role's name and *Kind* (script); the value for one screen's sake is what the rule forbids. No other passage made a value a decision (searched) |
| R2 — pair rule's code half unchecked | §4.2: the rule speaks of the table; the pair's values in code are held by the contrast rule |
| R3 — role-meaning invariant's reach | §6.3 step 4: its sentence speaks of the state of every file of the part, never a change; its method reads all of them; *Part* the user interface's part and the part holding `foundations/**` |
| R4 — "discipline" in two senses; two names | §1 "the styleguide first"; §6.3 step 2 "the method of research taken from WAY-122"; the discipline's one value is `styleguide`, the header's. "Discipline" kept (finding 19): no collision in the foundation |
| R5 — package names caught as references | §3.2 defines a reference in two forms: a decision number of the log or an identifier of the invariants file, followed by `@` and letters and digits; or any identifier followed by `@` and exactly eight lower-case hex characters. `react@18` is none; a mistyped fingerprint after a real entry is still an error. §3.3 sentence, §5.3 item 7, §9.3, §10 tests follow |
| R6 — drift of translated meanings | §4.2 "Translated meanings": not caught by any check; caught only by a reader, the review of the change, or the role-meaning invariant judging screens against decisions; the price shown at the request; a product wanting it caught writes its prose in English |
| R7 — product copy misses a pin move | §3.3 product *Part* adds the part holding `.the-way` |
| R8 — "the pinned commit" in the-way | §3.3 sentence: "at the commit of the-way the repository uses — the commit checked, in the-way itself; the pinned commit, in a product" |
| R9 — header and file name not tied | §5.3 item 5a; `guidelines-check-form`; §10 test |
| Before-`main` state | §5.1: `guidelines-reference-current` records `pass` beside `unchecked`; expected, named in the request |

Price of R5's choice (**autonomous** in its exact form): a package whose version is eight
lower-case hex characters, or a sample address like `name@deadbeef`, must be fenced; a reference
to an entry neither in the log nor in the invariants file with a wrong-length fingerprint is not
recognised as a reference at all — low, since such a reference names nothing anyway and the
eight-character form still catches it when the length is right.
