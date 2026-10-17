# Author report — foundation step (turn 1)

Status: **done** — foundation change committed (`596a660`), boundary reached: no code, no
template, skill, script or test edits, `foundations/invariants.md` untouched. Author:
general-purpose subagent, claude-opus-5-5, one-author route (WAY-136).

## Input versions

- Base and process pin: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (`origin/foundations`).
- Frozen task: `.runs/task-cycles/agent-path-to-running-product/task.md` (ready for cycle,
  updated 2026-10-18), rows 1–6 of *Settlements to record*, answers to questions 1–6, four
  *Questions carried to cycle*.
- Cycle record `.runs/task-cycles/agent-path-to-running-product/cycle.md` (choices C1–C5),
  handoff `reports/author-foundation-handoff.md`.
- Read whole: `AGENTS.md`, `agent-instructions/README.md`, `task-cycle/skill/SKILL.md` (foundation
  step paragraph and its context, lines 230–310), `.claude/skills/the-way-record-decision/SKILL.md`,
  `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md` (WAY-03 read in the log), `elements/common/rules.md`,
  `elements/common/way_of_working.md`, the whole decision log, the part map, the glossary,
  `project-level/definition_template.md`, `project-level/technology/SKILL.md`,
  `project-level/readiness_check.py`; the gate and resume parts of `project-level/skill/SKILL.md`;
  `project-level/task/skill/SKILL.md:60-99`.
- No other element skill was used: the search found no glossary term, environment fact or
  part-map entry to write; the invariant is left to the two other agents (WAY-69).
- Superpowers: not used in this turn (no method of it applies to a foundation entry).

## Selection summary

Full record: [foundation-selection.md](foundation-selection.md). Touched parts `project-level` and
`decisions` (the changed file `foundations/decisions.md` collects entries; every entry written or
edited has *Scope* `project-level, decisions`). 96 expected *Scope* matches, all read whole (the
whole decision log was read); the eleven decisions the task names are among them; no missing match.
Part map and glossary read whole; the seven `project-level` invariants and the relevant `every`
invariants read whole, the rest discovered; environment facts inspected, none relevant.

## WAY-33 search — domain, terms, findings

- Domain: all five elements (`decisions.md`, `invariants.md`, `glossary.md`, `part_map.md`,
  `environment_facts.md`, plus `violated_invariants.md`) at `77c8a8b`, plus incoming fingerprint
  `740c254e` of WAY-121 across the whole repository (`git grep`).
- Terms: log, logs, logging, observab*, running product, working product, interface, UI, browser,
  terminal, API, seed, fixture, test data, development data, test environment, test server,
  staging, agent works with, works with best, place to run, screen, end-to-end, exploratory,
  production, sandbox, dashboard, visible behaviour, tie/tied; and the identifiers WAY-121, 122,
  123, 137, 138, 118, 139, 140, 143, 100, 04.
- Findings, each read whole and settled:
  1. No entry settles how an agent reaches the running product → the rows are written (WAY-121
     edited, WAY-165 new).
  2. WAY-137 ("For a place to run, how well an agent works with an option decides nothing else") can
     apply to an option of the three choices that is itself a place the product runs — a lasting
     test environment offered for the development data. Row 6 is the human's precedence for that
     overlap → WAY-165 names `narrows WAY-137@86b2a30d` and states the area in its binding sentences
     (WAY-25, WAY-32). WAY-137 unchanged.
  3. WAY-123 (consequences; simplest and cheapest only where no consequence differs) → row 6 makes
     an agent's use a consequence; no collision; WAY-165 `derives from WAY-123@f3b45293`.
  4. WAY-122 (choices researched apart; rationale: a way of logging in weighed by consequences) →
     three items rather than one cited in WAY-121's rationale; the word "logs" is used, never
     "logging", to keep apart from "a way of logging in".
  5. WAY-108 (markers read by the readiness check keep English forms) → grounds the English mark of
     carried question (a); cited in WAY-121's rationale.
  6. WAY-118 (a changed approved definition goes through the gate again) and WAY-34 (a newer process
     reaches a product when it moves its pin) → row 5; WAY-121 now `derives from WAY-118@5af868b3`,
     WAY-34 cited in rationale.
  7. WAY-100 (a borrowed practice binds only through a decision naming what, where, why) → WAY-121
     `derives from WAY-100@e7a74a18` and names the adopted piece in its rationale. WAY-27 (no
     pointer to an unreachable source) → the lesson is named and what was taken is described; no
     link.
  8. WAY-102 (no reliance on memory) → cited in WAY-121's *Rejected* (manual catch-up), as answer 4
     cites it.
  9. WAY-139 (deployment skill covers "how to read the logs"; checked only for tasks that deploy) →
     no collision; cited in WAY-121's *Rejected* as answer 2 rejects it.
  10. WAY-143 ("a preparatory task sets up logging for the whole product for later use and no task
      depends on it" violates) → no collision: the definition settles the choice, the first task
      using it builds it.
  11. WAY-08 / WAY-61 (exploratory test by an agent on the working product) → agree; the three
      choices are what such a test needs. No link (invariants element).
  12. WAY-140 (effects outside the repository only by a human; reading stays with the agent) → no
      collision with the rows, which ask what an option is, not who makes it; WAY-165 cites the
      setup of a lasting test environment as a human's cost, and its *complies* example cites the
      copy of production as a human action (from the task's Context). See concern 5.
  13. WAY-04 (*Rejected*: "the agent's environment ... as elements of their own") → no collision:
      the three are product decisions, no new element.
  14. Part map, `project-level` failure mode "a technology choice the project needs is missing from
      the definition's list — not detected" → for the three choices it becomes detectable; a
      failure mode is a human's to record (WAY-46), so it is a candidate only (concern 2).
  15. Glossary: "surface" is narrow and not used for the interface; "gate" appears only as
      "readiness gate"/"readiness check", as the log already uses them; "running product",
      "logs", "interface", "development data" keep the meaning a reader of the field gives them and
      take no entry (WAY-95). No new term.
  16. Incoming fingerprint `740c254e` of WAY-121: WAY-122, WAY-123 (renewed, still valid) and
      invariant `project-technology-record` (left stale on purpose, see below). No other file.
  17. Environment facts: none concerns the subject; none named.

## Entries written or changed

| Identifier | Rows | Meaning (Polish) |
|---|---|---|
| WAY-121/1 (edited in place, binding part changed; fingerprint `740c254e` → `d0b060e5`) | 1, 4, 5 | Lista wyborów technologicznych każdej definicji projektu zawsze — niezależnie od reguły, co na nią trafia — ma trzy osobne pozycje drogi agenta do działającego produktu (logi, interfejs, dane deweloperskie), każdą nazwaną w języku definicji i oznaczoną angielskim znacznikiem tego, którą z trzech jest, rozstrzyganą jak każdy wybór własną decyzją projektowaną albo wskazaniem decyzji, która już ją rozstrzyga, i mającą odpowiedź także wtedy, gdy produkt danej rzeczy nie ma; bramka gotowości zatrzymuje definicję bez którejś z nich, a definicja zatwierdzona przed tym wymogiem wraca do kroku technologii i przez bramkę ponownie, gdy po przesunięciu przypięcia the way skrypt bramki pierwszy raz na niej ruszy (np. przy doprecyzowaniu zadania z jej planu). |
| WAY-165/1 (new) | 2, 3, 6 | Pozycja logów pyta, gdzie trafia zapis tego, co działający produkt robi, i jak agent go czyta; pozycja interfejsu — jak agent obsługuje produkt tak, jak robi to jego użytkownik (ekran w przeglądarce, wywołanie API, polecenie w terminalu), i jak widzi, co produkt mu odpowiada; pozycja danych deweloperskich — skąd biorą się dane, na których agent sprawdza zachowanie produktu poza produkcją, i jak dochodzi do potrzebnego stanu danych, bez przesądzania między danymi zakładanymi od zera a trwałym dedykowanym środowiskiem testowym; w tych trzech pozycjach to, czy agent może z opcji korzystać, jest konsekwencją dla produktu (także gdy opcja jest miejscem, w którym produkt działa): opcja bez drogi dla agenta zostaje w porównaniu z brakiem „agent nie sprawdzi w ten sposób działającego produktu”, rekomendacja ją omija, a reguła remisu z WAY-137 zostaje przy wyborze miejsca uruchomienia. |
| WAY-122/1, WAY-123/1 | — | Bez zmiany znaczenia: odświeżony odcisk relacji do WAY-121 (`740c254e` → `d0b060e5`). |

Fingerprints: WAY-121 `d0b060e5`, WAY-165 `a179dbe4`. *Approved by* of WAY-121 and WAY-165:
`Mariusz, merge of <request link>`; WAY-122/123 keep theirs (relation fingerprint only, as in the
precedent of PR #21 and #22). *Review when*, set by the author: WAY-121 — a task cycle of a product
whose definition holds the three choices improvises a way to the running product none of them
gives, or leaves behaviour a user sees unchecked for want of one · 2027-01-31; WAY-165 — a task
cycle under a definition whose three choices were settled by this decision finds an agent cannot
use the option chosen for one · 2027-01-31. Verification: WAY-121 level 1
(`project-technology-record`) plus level 2 with new examples; WAY-165 level 2.

WAY-121 relations now: derives from WAY-106, WAY-116 (unchanged), WAY-118@5af868b3,
WAY-100@e7a74a18 (added). WAY-165: derives from WAY-121@d0b060e5, WAY-123@f3b45293; narrows
WAY-137@86b2a30d.

**Change of meaning of an approved decision:** WAY-121 was approved `Mariusz, 2026-10-04`; its
meaning grows (rows 1, 4, 5). The request must show it as a changed approved decision for renewed
acceptance (README, WAY-07, WAY-114). WAY-121's *Rationale* and *Rejected* keep the old text and
add the new; *Change* stays `new decision` (version 1, before `main`).

## Carried questions

### (a) How the readiness check recognizes the three items — settled

Wording of row 1 (WAY-121): each of the three is "an item of its own named in the definition's
language and marked in English by which of the three it is". The meaning of row 1 is unchanged; the
mark makes row 4 checkable, as WAY-108 already keeps every marker the readiness check reads in
English. Recommended form for the template in turn 2 (the form belongs to the template, not the
decision): the item begins with a fixed English mark followed by a colon — `logs:`,
`interface:`, `development data:` — then the name in the definition's language, then the usual
end marker, e.g.
`- logs: Zapis działania gry i jak agent go czyta — projected: How does an agent read the logs of the running game?`.

Ways weighed:

| Way | Cost | Verdict |
|---|---|---|
| Leading English mark per item (chosen) | one more English token in a list already ending in English markers; a template rule, a regex and tests | recognizable whatever the language, independent of order and of `held by`/`projected` |
| The three items named wholly in English | breaks the template rule that an item names its choice in the definition's language by what the product needs it for; the human loses that reading | rejected; recorded in WAY-121 *Rejected* |
| A third-level subsection holding the three in fixed order | recognition by position breaks silently on reorder; heading lines are today "no choice item" findings, so more parser change | rejected |
| Words of the definition's language matched per language | a word list per language, and a language without a list goes unchecked — the reason WAY-72 rejects per-language word lists | rejected |
| Recognition through the projected question or the `held by` decision | `held by` names only an identifier; the readiness check would have to read the product's decision log | rejected |

Not settled by the decisions (left to the template and check, recommendation given): a second item
carrying the same mark — WAY-121 requires one of each; my recommendation is that the check does not
stop a second one (no row forbids it, and splitting e.g. log storage from log reading may be a real
case). Cost if the sentence agent decides otherwise: a stricter check, no meaning lost.

### (b) Where row 6 stands — settled

In a new decision WAY-165 together with rows 2 and 3, which `narrows WAY-137`. Reasons: WAY-121
holds the template's maximum of three binding sentences already, now carrying rows 1, 4 and 5;
rows 2, 3 and 6 answer one other question — what each of the three asks and what an agent's use of
an option weighs in it — and a new rule beside an existing decision is a new question (WAY-19). Row
6 is placed against WAY-137 by a `narrows` relation rather than by editing WAY-137: the overlap is
real only where an option of the three is a place the product runs (finding 2), WAY-137 keeps its
approved wording, and its own dependents (none carry its fingerprint today) are untouched.
Rejected: row 6 inside WAY-121 (a fourth binding sentence, or a sentence too long to read); a
narrowing edit of WAY-137 (changes another approved decision whose question is about ties between
places to run); no relation (an agent applying WAY-137 literally to a test server would meet an
unrecorded collision, WAY-25). Cost if wrong: moving the sentence is a local edit before `main`.

### (c) How `settle-technology` resumes a definition lacking one of the three — view

Follows from rows 1 and 5, nothing open. Today step 0 sends a list with no open item to step 3,
whose readiness-check finding of condition g "on an item still open goes back to step 2, any other
… to step 1". With the new condition: step 0 should check, besides open items, that each of the
three marks stands; where one is missing, add the missing items as `— open` to the existing list
(keeping every other item and its marker), show the list and ask whether it still holds, then step
2 settles them like any other open choice (WAY-121: "settled like any other choice"), with the
critique, the tests of WAY-138 and the human's choice. For an approved definition: adding items
changes the fingerprinted sections, so the status goes back from `approved`, and after step 6 the
definition goes through step 7 (WAY-118); `define-project` step 0's approved-definition branch
needs a route for this finding to step 6 (today only a fingerprint mismatch routes to step 7), and
the plan is then checked again (plan-project step 0; answer 4).

### (d) Does `project-technology-record` cover the run on an approved definition — view

Yes. WAY-121 now binds that a definition approved before the three were required goes back once the
readiness check first runs on it after the pin moves — that run is the check without
`--before-approval` (task refinement, plan-project step 1, lead-project and the plan-state reader
all run it on approved definitions). The guarantee of row 5 rests entirely on that mode reporting a
missing item; an invariant scoped "Before approval" would let a change that skips the condition for
approved definitions pass unseen. Recommended: the sentence drops "Before approval" (or names both
modes), and the check covers a definition with a gate record as well.

## What the decisions now require of `project-technology-record`

In terms of the decisions (for the sentence agent; the check agent receives only the sentence and
its method):

1. Everything it requires today (WAY-121 S1/S3): the Technology section is present, does not read
   `none`, holds only choice items, none still open, each naming a decision as
   `<PREFIX>-<NN>/<version>` or a question a heading of a projected decision holds.
2. New (rows 1 and 4): the list holds an item marked as the logs, one marked as the interface and
   one marked as the development data; a definition lacking any one of the three is rejected —
   each of the three separately.
3. New (row 5): the rejection holds for an approved definition too (with its gate record), not only
   before approval — see (d).
4. Its *Derives from* becomes `WAY-121@d0b060e5` (now stale at `740c254e`). Its version: with no
   main branch every entry stays at version 1 (`elements/common/rules.md`, "Version"), so the
   heading and the `# invariant: project-technology-record/1` citations keep /1.
5. Not required by any decision, so not for the invariant: what each item asks (WAY-165, level 2),
   whether a second item carries the same mark, that the name before the mark is in the definition's
   language.

## Choices, rejected alternatives, cost if wrong

| # | Choice | Rejected | Cost if wrong |
|---|---|---|---|
| F1 | Rows 1, 4, 5 in WAY-121 by in-place edit (answer 2; README) | a new decision for the three items beside WAY-121 — answer 2 places the sentence in WAY-121 | none expected |
| F2 | Rows 2, 3, 6 in new WAY-165 | all six in WAY-121 — over three binding sentences (template, `binding-sentence-count`); rows 2–3 in WAY-121 and row 6 elsewhere — splits what row 6 weighs from what the choices ask | the handoff expected rows 1–4 in WAY-121; moving rows 2–3 back is a local edit, but WAY-121 would exceed three sentences |
| F3 | Row 5 in WAY-121 next to the gate (row 4), generalized to "once ... the readiness check first runs on it, as the refinement of a task of its plan runs it" | wording row 5 as the refinement alone — the plan-state reader, plan-project and lead-project run the same check on approved definitions and stop too; a version of WAY-118 — changes another approved decision and its four dependents | if the human reads the generalization as more than row 5, the clause narrows to the refinement; the code is the same either way |
| F4 | `narrows WAY-137` from WAY-165, area stated as "even where the option is a place the product runs" | see (b) | low; the clause and relation can go if the human sees no overlap |
| F5 | WAY-121 relations gain WAY-118 and WAY-100 | no new relations — WAY-100 requires the adopting decision to be traceable, and row 5 serves WAY-118 | two more fingerprints to renew if those change |
| F6 | Lesson named by title in WAY-121's rationale with what was taken described; no link (WAY-27); its author's name left out | naming nothing — WAY-100 asks to name what is adopted | an assessor may read the title as a pointer; then describe without the title |
| F7 | *Review when* set on both (failure signal in a task cycle · 2027-01-31) | `none` — the rule rests on a prediction that three answered choices give the cycle's agent its way | a date to review; low |
| F8 | WAY-122/123 keep *Approved by* (relation fingerprint only) | placeholders on them too | if the human counts a renewal as a change, two placeholders to add |
| F9 | Invariant `project-technology-record` left with the stale `WAY-121@740c254e` | renewing the link myself — the handoff and WAY-69 keep `invariants.md` with the two other agents | `link-fingerprint-value` fails at `--merge-onto` until the sentence agent renews it |

## Commands, exit codes, outputs

All run from the worktree root, Git Bash, Python 3.14 (`python -B`); guards on the edited file
before commit, identical to the committed state `596a660` (no edit after the runs). Full
stdout+stderr in this reports directory.

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [foundation-guard-decisions.txt](foundation-guard-decisions.txt) | 0 errors, 7 warnings, 5 unchecked |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | [foundation-guard-invariants.txt](foundation-guard-invariants.txt) | 0 errors, 0 warnings, 3 unchecked |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | [foundation-guard-part-map.txt](foundation-guard-part-map.txt) | 0 errors, 0 warnings, 7 unchecked |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | [foundation-guard-glossary.txt](foundation-guard-glossary.txt) | 0 errors, 0 warnings, 5 unchecked |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 | [foundation-guard-environment-facts.txt](foundation-guard-environment-facts.txt) | 0 errors, 0 warnings, 3 unchecked |
| `python -B gate/run_tests.py elements/decisions` | 0 | [foundation-tests-decisions.txt](foundation-tests-decisions.txt) | 169 tests OK |
| `python -B gate/run_tests.py gate` (critical flows) | 0 | [foundation-tests-gate.txt](foundation-tests-gate.txt) | 98 tests OK |
| `python -B gate/run_tests.py elements/invariants` (extra) | 0 | [foundation-tests-invariants.txt](foundation-tests-invariants.txt) | 233 tests OK |
| `python -B gate/run_tests.py project-level` (extra) | 0 | [foundation-tests-project-level.txt](foundation-tests-project-level.txt) | 250 tests OK |
| `git diff --check` | 0 | (no output) | no whitespace errors |

Warnings, named: five pre-existing (WAY-03, WAY-21, WAY-52, WAY-55, WAY-69: check-by 2026-10-02
passed without a review record — same on the base); two expected placeholders
`merge of <request link>` (WAY-121 line 3469, WAY-165 line 5389).

Unchecked, named (all from `none` options or absent product commands): decisions — lines held on
main and versions per number, template change without a version (`--base none`); `TODO` in the
log, copies of versions both logs hold, fingerprints relations carry (`--merge-onto none`).
Invariants — identifiers, versions, corrections and the violated list (`--base none`); `TODO`,
link fingerprints (`--merge-onto none`) — **this hides the one stale link below**. Part map —
parts lists of `wording-reaches-dependants` and `skills-reach-the-way-sessions` (no coverage
file); promise-level change paths and the dependency graph (no product command); known
violations, identifiers, criticality lowering (`--base none`). Glossary — *Avoid* counts, terms
reading like identifiers, uses of changed definitions (`--base none`); `TODO`, terms with no use
after the merge (`--merge-onto none`). Facts — identifiers and versions (`--base none`);
fingerprints decisions carry for facts, facts nothing names after the merge (`--merge-onto none`).

Manual check (not a command of the product): fingerprint links recomputed with a scratch script
using `relation-model/fingerprint.py` (first paragraph under each heading as the binding part) —
actor: this author; observed on the committed state: 197 `WAY-n@fp` links in the decision log,
**0 stale**; 254 links to decisions in `foundations/invariants.md`, **1 stale**:
`invariants.md:2027` `project-technology-record` *Derives from* `WAY-121@740c254e` (current
`d0b060e5`) — expected, owned by the sentence agent. Baseline at `77c8a8b`: 192 / 0 and 254 / 0.
Script not kept (scratchpad).

Not run: the full required gate (orchestrator); the second WAY-33 search against the integration
tip and the independent assessment (later stages); any check of the code change (turn 2).

## Changed files (commit range `77c8a8b..596a660`)

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 121 | 11 |

Commit: `596a660` docs(foundations): settle the agent's way to the running product (author address
checked: private address). `.runs/` not staged.

## Sharpness inputs from the actual diff

- Criticality: the changed file belongs to part `decisions` (failure mode high, not detected); the
  entries concern `project-level` (eleven failure modes, all high). Highest: high.
- Trust-boundary files: none touched in this commit (`decisions` declares none). The code step will
  touch `project-level/readiness_check.py` (declared trust boundary) — adversarial input checks
  apply then (WAY-48).
- Irreversible operations: none (git text change).

## Unresolved concerns for the next dispatch

1. **Invariant tests of other invariants break once the readiness check requires the three
   items.** `project-level/test_plan_state_invariant.py` (cites `project-plan-state-evidence/1`)
   holds a definition fixture whose Technology section has one item (`:58-60`) and a
   `FINGERPRINT` constant of that definition; `test_plan_state_subprocesses_invariant.py` imports
   it (`:16`, `:120-121`). `plan_state.py:385` runs `readiness_check.check` on the definition, so
   those invariant tests will fail after the code change. `test_readiness_check.py`'s shared
   fixtures (the default Technology body) are used by tests citing `project-readiness-gate` and
   `project-definition-form` too. These files are invariant tests, read-only during implementation
   (WAY-03): their fixtures have to be updated in this foundation stage (by an agent other than
   the code's author, WAY-69), or turn 2 stops on them. `test_plan_state.py` (no invariant
   citation) and `test_plan_check.py` (plan check does not run the readiness check) are ordinary or
   likely unaffected — to verify in turn 2.
2. **Part-map failure mode candidate** (WAY-46: a human's to record): "a definition reaches the
   breakdown without one of the three choices of how an agent reaches the running product — the
   task cycle has no way to check behaviour in the running product — high — detected by
   project-technology-record". Criticality would not change.
3. **WAY-121 change of meaning** must be listed in the request as a changed approved decision
   beside WAY-165 (README, WAY-07).
4. **To do 3** (request line on moving the pin, part map *Change paths*) is the request's, not a
   decision (plan test, WAY-36): moving the pin sends a definition approved without the three
   items back to the technology step and the gate before its next task is refined.
5. **WAY-140 and the agent's own use of a deployed test environment.** WAY-140 lets the agent read
   outside the repository and leaves effects there to a human; whether an agent operating a
   deployed test environment through its interface (creating data while it checks) is such an
   effect is not settled by any entry. The new decisions do not depend on it (they ask what each
   option is and weigh what it costs), but a product choosing a lasting test environment will meet
   the question in its cycles. Not blocking; a question for the human if the orchestrator sees it
   as one.
6. **Mark syntax and duplicates** (carried question a): the template in turn 2 sets the exact
   form; recommendation above (`logs:`, `interface:`, `development data:` leading the item; a
   second item of one mark not stopped).
7. **Skills to adapt in turn 2** beyond the cycle record's list: `define-project` step 0
   (approved-definition branch needs a route for a missing item to step 6, then 7);
   `settle-technology` step 0 and step 1 (add the three to the list, keep the definition's other
   items; see c); the template's Technology section (the always-present items, the mark, the
   exception to the membership rule, WAY-165's questions and the agent-use rule beside WAY-137's);
   `plan-project` step 1 and `lead-project` route a finding back to `define-project` already.
