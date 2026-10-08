# Design report — light-path-small-change

- Agent: design agent (general-purpose, Opus 5.5), dispatched by the orchestrator under Mariusz's
  delegation; method Superpowers 6.4.1 `brainstorming`, read in full from
  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/brainstorming/SKILL.md`.
- Output: `spec.md` in this run directory (not committed; the directory is ignored). No other file
  written; no repository file edited (worktree `git status` clean after the work).
- Boundary: self-reviewed spec; `writing-plans` not invoked.

## Classification

By the skill's own test the task is **architectural**: it changes how the parts of the cycle fit
together and alters an interface others depend on (the `implement-task` skill pinned by products,
and two decisions). It is not bounded (no single existing flow, two decisions and an invariant link
move) and not a spike. Per the dispatch, the architectural path is followed regardless.

## Exploration (files read, all at c64a607 in `C:/Storage/repos/the-way-light-path`)

- `task_frozen.md` (in full); `cycle.md` (orchestrator's record so far).
- `AGENTS.md`, `agent-instructions/README.md`.
- `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` (in full).
- `foundations/decisions.md`: WAY-01, 03, 07, 08, 09, 10, 11, 12, 13, 14, 17, 25, 26, 27, 28, 29,
  30, 31, 32, 33, 36, 45, 47, 69, 95, 99, 100, 113, 114, 124, 125, 126; headings of all; word searches
  over the whole log (path, size, spec, plan, review, executor, implement-task, route).
- `foundations/invariants.md` (head, lines 200–310 incl. `foundation-change-path/1`, searches for
  task-cycle-related sentences and `WAY-13@`/`WAY-125@`/`WAY-47@`); `foundations/glossary.md` (full);
  `foundations/part_map.md` (full); `foundations/environment_facts.md` (searched).
- `elements/decisions/template.md`, `elements/decisions/skill/SKILL.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md` (full); `elements/invariants/template.md` (link and version
  rules); `elements/common/critique/SKILL.md` (head).
- `--help` of the decisions, invariants, glossary and part-map format guards; `relation-model/fingerprint.py`.
- Outside the foundation: `project-level/task/skill/SKILL.md`, `project-level/task/template.md`,
  `installation/README.md` (references to the cycle's spec/plan).
- Superpowers 6.4.1: `requesting-code-review/SKILL.md` and `code-reviewer.md` (head),
  `test-driven-development/SKILL.md` (head), `subagent-driven-development/SKILL.md` (head and
  structure), `finishing-a-development-branch/SKILL.md` (steps 1–5).
- Fingerprint sanity checks: WAY-13 base binding → `c6b33aa9` (matches the invariant's link);
  WAY-125 base → `4c302238` (no carrier); WAY-47 → `bc0da442`; proposed WAY-13 wording → `97b17d59`.

## Questions

None that no source answers. Every open point was settled as a recorded choice with alternatives and
cost if wrong (spec section 9, D1–D15), as the cycle allows. They are listed below for the
orchestrator's ruling.

## Approaches considered

1. **Two axes (recommended, D1).** WAY-13's "paths" stay the foundation route; the new light/full
   choice is a lighter preparation inside that route. The invariant `foundation-change-path` holds
   unchanged in meaning: a light change that touches the foundation simply has its route re-recorded
   as changed and runs that route's rules. WAY-13's rejected "the path chosen by size" stays true.
   Cost: the light way cannot be called a "path" without confusion, hence D2 ("light cycle").
2. **Light way as a third WAY-13 path.** Size joins the foundation analysis in choosing paths. The
   invariant then reads "the path for tasks that leave the foundation unchanged" ambiguously and point
   3 breaks it unless the invariant gains an exception; WAY-13's rejected "the path chosen by size"
   falls; WAY-47's rationale "light path" clashes. More entries move, more for Mariusz to re-accept.
3. **Separate skill.** Rejected by the task itself (two skills holding the same record, request and
   return-step rules).

## Design (summary; full text in `spec.md`)

- Entry: the orchestrator judges three findings in step 4's analysis (foundation unchanged; about ten
  minutes for one agent; no very large or very many files), records the choice and reasons in a new
  `## Cycle` section of the record.
- Light cycle: one fresh executor from the frozen task, TDD for behaviour changes, commits, returns
  before review; step 10 in full (gate, sharpness checks, critical flows, trust-boundary adversarial
  checks, visible behaviour, deliberate breaks); one `requesting-code-review` of the whole change with
  the frozen task as requirements, fixes by the executor, one scoped re-read of the fix range; steps
  11–14 as written.
- Foundation touch: executor returns; orchestrator rules "simple and obvious" by four conditions (no
  open choice, no change of an approved decision's meaning, no contradiction, no invariant or invariant
  test); simple → route re-recorded as changed, executor writes the entry through its element skill,
  entry joins the one WAY-10 assessment; otherwise switch.
- Switch: report without code or diff; orchestrator checks it, records last commit and file names,
  resets the task branch to base; fresh designer at step 6 with the report; full cycle as written.
- Skill edits: description, step 4 (choice + "On the full cycle" qualifier), new `## Light cycle`
  section, step 6 (post-switch report; "the full cycle requires"), step 9 qualifier, step 13 (cycle and
  reasons in the request). Record template: `Cycle` header line, `## Cycle` section, artifacts and
  request-handoff lines.
- Foundation: WAY-13 binding sentences 1 and 3, verification, rationale, rejected; WAY-125 binding
  sentence 1, relation `derives from WAY-13@97b17d59`, verification, rationale, rejected; both
  *Approved by* → `Mariusz, merge of <request link>`; invariant `foundation-change-path/1` *Derives
  from* fingerprint renewed, sentence and version unchanged. No glossary, part map or fact change.
- Collisions (WAY-33): none left unresolved; the two named in the dispatch are resolved by D1 (the
  invariant) and by the task's own in-place edit of WAY-13 (sentence "size serves only as a signal to
  split it"; guide + WAY-07 + WAY-30, re-accepted at the merge).

## Choices for the orchestrator to rule (provisional)

D1 two axes; D2 "light cycle"/"full cycle" naming (Polish request: "lżejsza ścieżka (light cycle)");
D3 thresholds in the skill only; D4 four-condition "simple and obvious"; D5 orchestrator rules each
touch, executor writes the entry; D6 one review plus one scoped re-read of fixes; D7 switch only during
implementation and review fixes; D8 discard by reset to base; D9 switch-and-discard in WAY-125's
binding sentence; D10 new `derives from WAY-13`; D11 no edit to project-level task docs; D12 ten
minutes as estimate, not timer; D13 one agent-written reason in WAY-125 *Rejected* (flag in request);
D14 fresh executor where the harness cannot resume; D15 corrections after review unchanged.
Each has alternative and cost in spec section 9.

## Spec self-review

- Placeholder scan: no TBD/TODO. Remaining angle-bracket values are deliberate: `<request link>`
  (replaced at step 12 by rule) and template placeholders in the record-template text. The WAY-13
  fingerprint is given concretely (`97b17d59`, verified by extracting the quoted wording from the spec
  and running `relation-model/fingerprint.py`), with a note to recompute if the foundation step
  rewords it.
- Internal consistency: fixed three issues inline — the touch's entry rules named decision-only
  fields for any element (now qualified); the "harness cannot resume" sentence sat in the switch
  paragraph (moved to the review bullet); the Polish meaning sentence of WAY-13 used "ścieżka" for the
  foundation route, which collides with Mariusz's word for the light way (reworded).
- Scope: one implementation plan covers it (two files of `task-cycle/`, two decisions, one invariant
  link).
- Ambiguity: "checks after the change" made explicit as "checks run on the finished change"; "one
  review" pinned to one `requesting-code-review` that is both unit and final review; switch window
  stated (D7); "very large / very many files" left as recorded judgment by design (D3).

## Notes for later stages

- Guards with `--merge-onto none` leave relation and link fingerprints unchecked; spec section 11
  adds a manual fingerprint check and a diagnostic run with `--merge-onto c64a607` compared against the
  same run on c64a607.
- Process remark candidates for the record: the project-level task template says "the cycle's record
  holds the implementation plan" and "the cycle's plan chooses how", loose once a light cycle has no
  plan (D11); the return step may consider a task-cycle failure mode for a mis-admitted light task
  (failure modes are recorded by a human, WAY-46).

## Revision 1 — after the spec review (`reports/02-spec-review.md`) and the orchestrator's provisional rulings

Read the review in full. Changes to `spec.md`:

- **Issue 1 (accepted):** WAY-125's light clause now reads "test-first where it changes behaviour" in
  the binding sentence, the complies example and the Polish meaning sentence.
- **Issue 2 (option a):** WAY-125's binding sentence states the four conditions instead of "simple
  and obvious": a change "whose touch of the foundation needs a choice the task leaves open, changes
  the meaning of an approved decision, contradicts a current entry or writes or changes an invariant
  or an invariant test, is discarded …". The skill keeps "simple and obvious" as its label, defined by
  the same four conditions (unchanged 3.3 and 4.3). Section 8 row "WAY-95/99, glossary" corrected:
  it names the finding, the resolution and the rejected glossary entry. D4 notes where each lives.
- **R1:** WAY-125 sentence 1 trimmed — dropped "and the request is prepared as for any task" and
  "independent" before "final code review" (both already in the method list). Binding part 246 words
  (base 140; the four conditions added length); 3 sentences by the decisions guard's own
  `count_sentences`.
- **R2:** fingerprints recomputed from UTF-8 files' bytes, and re-extracted from the spec text itself:
  WAY-13 `97b17d59` (unchanged), WAY-125 `68b2d563` (new; base `4c302238`). Cited in 7.1, 7.2, the
  WAY-125 relation, 7.3 and 11.5; 11.5 now says to feed a UTF-8 file's bytes, never a string through a
  non-UTF-8 console.
- **Issue 3 (accepted):** section 7 states the ground (the approved task document orders the WAY-13
  and WAY-125 changes and settles their questions, so it is the approver's answer WAY-30 and WAY-114
  ask for; no pre-request question or blocked draft; meaning shown at the merge) and lists "Wording
  beyond the task's words" (six items: WAY-13 sentence 1; "never the outcome it has to reach"; the
  switch-and-discard clause; the four conditions; the WAY-125 → WAY-13 relation; the D13 reason).
  Section 8 row "WAY-13/1 sentence 3" now cites that ground instead of "goes into the plan".
- **R3:** 11.4 keeps the glossary guard and names all three baselines (glossary 0/0/5 as recorded by
  the orchestrator).
- **R4:** step 13 (4.6) says "a link to the executor's report".
- **R5:** step 4 (4.2), 3.1 and the record template record the reason for each finding assessed; once
  one fails, the rest may read `not assessed`.
- **R6:** section 7 says each entry keeps the log's form (*Rationale* and *Rejected* as italic
  paragraphs after the field list).
- **R7:** the discarded attempt's last commit is called a historical name, not a link to follow, in
  3.4, the skill text (4.3), the record template (section 6) and D8.
- D1–D15 unchanged; D13 stays flagged for the request.

Self-review rerun: no TBD/TODO; placeholders only `<request link>` and the template's slots; both
fingerprints verified against the spec's own quoted wording; no contradiction found between 3.3,
4.3 and 7.2 (same four conditions, label only in the skill) or between section 5 and the edited
4.2/4.6 (the added text is record and request wording, not a full-cycle step); scope unchanged.
Worktree `git status` clean; nothing committed; `writing-plans` not invoked.
