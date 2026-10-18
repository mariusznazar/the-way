# Author report — foundation step (turn 1)

Status: done — foundation change committed; no code or non-foundation file touched.

## Input versions

- Base and foundation read: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (`origin/foundations`).
- Branch `task/agent-path-technology-step`; commit range `77c8a8b..49d7d2b` (one commit, `49d7d2b`,
  author address checked: private address from the conditional git config).
- Frozen task: `.runs/task-cycles/agent-path-technology-step/task.md` (read whole); cycle record
  `cycle.md` (read whole, choices C1–C5).
- Read whole: `AGENTS.md`, `agent-instructions/README.md`, the foundation-step paragraph of
  `task-cycle/skill/SKILL.md` (lines 250–286), `.claude/skills/the-way-record-decision/SKILL.md`,
  `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md`, `elements/decisions/examples.md` (→ WAY-03),
  `project-level/technology/SKILL.md`, the Technology section of `project-level/definition_template.md`
  (lines 148–221), the Technology checks of `project-level/readiness_check.py` (condition g),
  `foundations/part_map.md`, `foundations/glossary.md`.
- No other element skill was needed: the search found no entry of another kind to write (see below).
- Nothing read from the branch of PR #23.

## Selection summary

Full record: `.runs/task-cycles/agent-path-technology-step/reports/foundation-selection.md`.

- Touched parts: `project-level`, `decisions` (by WAY-44, from the Scope of the changed entries
  WAY-121/122/123 and the new WAY-165/166), and the `invariants` file entry `project-technology-record`
  (Part `project-level`).
- Expected Scope matches: every current decision whose Scope names `project-level` or `decisions`
  (exhaustive scan of 150 numbers, wrapped values joined) — 98 numbers, listed with lines in the
  selection file. Every decision the task names (WAY-04, 100, 106, 121, 122, 123, 137, 138, 139, 140,
  143) is in that set; no missing match.
- Incoming dependents of WAY-121 at base (`740c254e`): WAY-122, WAY-123, `project-technology-record/1`
  — the only three in the repository.

## Search of the whole foundation (WAY-33)

- Domain: all five elements at `77c8a8b` — `decisions.md`, `invariants.md`, `glossary.md`,
  `part_map.md`, `environment_facts.md` (and `violated_invariants.md`, empty).
- Terms: incoming fingerprints of WAY-121/123; log, logs, logging, observability, running product,
  working product, interface, UI, browser, terminal, screen, API, command line, seed, fixture,
  test data, development data, test environment, test server, staging, production, localhost,
  exploratory, agent works with, tie, place to run, belongs on the list, agent reads, visible,
  reach the product, user sees. Every relevant match read whole.
- Findings and how each was settled:
  - No decision sets how an agent reaches the running product; rows 2–4 are new questions (WAY-19);
    row 1 is the exception to WAY-121's rule of belonging (task answer 8) → edit of WAY-121.
  - WAY-137 (tie rule for a place to run): binds a place to run only; unchanged; named in WAY-166's
    *Rationale*.
  - WAY-123: its consequences are listed as cost, where it runs, upkeep, cost of later change; row 4
    adds the agent's use of an option for the three choices → WAY-166 `narrows WAY-123@f3b45293`,
    its binding sentence stating the area.
  - WAY-122, WAY-123: derive from WAY-121; checked against the new binding part, both still valid →
    fingerprint renewed.
  - `project-technology-record/1`: still true of the unchanged readiness check → only *Derives from*
    renewed (C5); sentence, method, version unchanged.
  - WAY-139 (deployment skill reads logs when deploying), WAY-140 (a human makes effects outside the
    repository; reading stays with the agent), WAY-143 (a technical element enters with its first
    task), WAY-08/61 (exploratory test by an agent on the working product), WAY-48/49 (browser storage,
    command-line surfaces), WAY-04 (no new element), WAY-106 (step writes into the definition only):
    agree with the rows; no change, no link needed beyond WAY-121's existing ones.
  - Part map `project-level` failure mode "a technology choice the project needs is missing from the
    definition's list — the first task chooses it — high — not detected" already covers an omitted
    matter, since each matter stands on the list as a choice; no part-map change.
  - Glossary: `surface` is not used for the interface; a grep of the added lines finds no glossary
    term (part, result, entry, verdict, watch, probe, debt, slice, element, mechanics, correction,
    clock, surface, human action) and no *Avoid* word. "development data", "interface", "logs",
    "running product" carry the meaning a reader of the field gives them → no glossary entry.
  - Environment facts: no relevant entry; nothing the new entries rest on is a fact → *Based on*
    `none`.
  - Invariant derivable: none on a commit of the-way without a check by the readiness gate, which
    To do 2 excludes → level 2 for all three decisions.

## Entries written or changed

| Entry | Row(s) | Meaning (Polish) |
|---|---|---|
| WAY-121/1 (edited in place; `740c254e` → `ed19d693`) | 1 | Krok technologii, gdy projekt wnosi zachowanie widoczne dla użytkownika w działającym produkcie, sprawdza trzy sprawy drogi agenta do działającego produktu — logi, interfejs i dane deweloperskie — i każdą, której żadna decyzja fundamentu nie rozstrzyga dla tego zachowania, stawia na liście jako osobny wybór, wyjątkowo od reguły przynależności także wtedy, gdy nic nie dokłada do utrzymania albo produkt danej rzeczy nie ma (odpowiedź mówi wtedy, czego agent używa zamiast niej). |
| WAY-165/1 (new, `97bffb69`) | 2, 3 | Pozycja logów pyta, gdzie trafia zapis tego, co działający produkt robi, i jak agent go czyta; pozycja interfejsu — jak agent obsługuje produkt tak, jak robi to jego użytkownik (ekran w przeglądarce, wywołanie API, polecenie w terminalu), i jak widzi, co produkt mu odpowiada; pozycja danych deweloperskich — skąd są dane, na których agent sprawdza zachowanie produktu poza produkcją, i jak doprowadza je do stanu potrzebnego sprawdzeniu, a dane zakładane od zera i trwałe dedykowane środowisko testowe to obie opcje tego wyboru. |
| WAY-166/1 (new, `4b3a76a4`) | 4 | W wyborach drogi agenta do działającego produktu to, czy agent może z opcji korzystać, jest konsekwencją dla produktu: opcja, z której agent nie skorzysta, zostaje w porównaniu z brakiem „agent nie sprawdzi w ten sposób działającego produktu”, a rekomendacja ją omija; zawęża WAY-123, a reguła remisu z WAY-137 zostaje przy miejscu uruchomienia. |
| WAY-122/1 (relation only) | — | Bez zmiany znaczenia: odnowiony odcisk relacji do WAY-121. |
| WAY-123/1 (relation only) | — | Bez zmiany znaczenia: odnowiony odcisk relacji do WAY-121. |
| `project-technology-record/1` (*Derives from* only) | — | Bez zmiany znaczenia: odnowiony odcisk relacji do WAY-121; zdanie i test bez zmian. |

What else changed in WAY-121, beyond row 1:

- Binding: the first and the third sentence merged into one, without change of meaning ("names the
  decision that already holds it or settles it as a projected decision; a project whose every choice
  the foundation holds thus settles nothing"), to keep three binding sentences.
- *Relations*: `derives from WAY-100@e7a74a18` added (adoption from outside, as WAY-137/138/143 do).
- *Verification* level 2: the existing complying example "a project that changes only how a screen
  looks records that the foundation holds every choice it needs" now adds "in a product whose
  foundation already says how an agent reaches its screens" — without it the example would contradict
  the exception. New complying and violating examples for the exception.
- *Review when*: was `none`; now "a project lists a matter of an agent's way to the running product
  that a decision of the foundation already settles for the behaviour the project brings, or a task
  cycle finds no way to check behaviour a user sees in the running product although decisions on
  those matters stand · check by: 2027-03-31".
- *Approved by*: `Mariusz, 2026-10-04` → `Mariusz, merge of <request link>` (meaning changed, accepted
  again at the merge).
- *Rationale*: why the exception; the adoption (WAY-100): takes from the lesson "Towards Autonomous
  Product Development" the question of how an agent sees the running product through its logs, its
  interface and its development data, applied in the technology step, and leaves out the lesson's
  hard limit (no production database, no root). No reason for leaving it out is given, as the task
  gives none.
- *Rejected*: added the options the task's answers 2, 3, 7, 8 rejected (items in every definition
  checked by the gate; a question in every task's refinement; the rule of belonging alone; a
  requirement beside the list; one choice for all three; one heading split by the agent's judgment;
  the deployment skill's list of WAY-139).

*Approved by* of WAY-165 and WAY-166: `Mariusz, merge of <request link>`; *Review when* `none` (neither
rests on a prediction).

## Placement of rows 2–4 — ways weighed

- Rows 2–3 → new WAY-165, "What does each matter of an agent's way to the running product ask?".
  Weighed: inside WAY-121 — WAY-121 already holds three binding sentences and its question is where
  technology is settled, not what a choice asks (WAY-19: a new rule next to a decision is a new
  question); two decisions, one per row — both rows come from one answer (question 5) to one question,
  and three sentences hold all three matters.
- Row 4 → new WAY-166, narrowing WAY-123. Weighed: a sentence in WAY-137 — changes the question and the
  binding part of an approved decision whose rule the task keeps unchanged, and joins a rule for a
  place to run with a rule for other choices; inside WAY-165 — a different question (how options are
  weighed, not what a choice asks), and it would tie WAY-165 to WAY-123 by `narrows`; inside WAY-123 —
  a general decision would carry an exception for three named choices, and WAY-137 already shows the
  form of a narrower decision against WAY-123.
- `narrows` rather than `derives from` WAY-123: WAY-123's binding sentence enumerates the
  consequences shown; adding the agent's use as a consequence, and passing over an unusable option in
  the recommendation, departs from it in a narrower area. WAY-166 derives from WAY-121, which names the
  matters.

## Carried question — where the check stands in `settle-technology`, and how a pre-change list resumes

View (the skill text is turn 2; the entries' wording does not depend on it beyond "the step looks at
three matters", which places no sub-step):

- Step 1 (List the choices): after listing by the rule of belonging, and only where the project brings
  behaviour a user sees in the running product, look at the logs, the interface and the development
  data; for each, a decision of the foundation that settles it for that behaviour → not listed; a
  projected decision of this definition → `— projected: <question>`; nothing → `— open`, named by what
  the product needs it for. The human confirms the list as today. Step 2 then settles them like any
  other choice, with WAY-166's rule added at weighing (2.3) and recommendation (2.5); WAY-137's tie
  rule stays limited to a place to run. The Technology rules of the template gain the exception and
  WAY-165's questions.
- Resume (step 0): a definition still in the step, or with a Technology list but not yet approved,
  may hold a list written before this change. Whenever step 0 resumes with a list — with or without an
  open item — it runs step 1's look at the three matters against the list first; a matter missing and
  unsettled is added `— open` and the list is shown again (as step 0 already does for open items); with
  nothing to add, step 0 goes on as today. An approved definition never enters the step for these
  matters, and the readiness check and `project-technology-record` stay unchanged, so nothing sends it
  back (To do 2).

## Choices made, rejected alternatives, cost if wrong

| Choice | Rejected | Cost if wrong |
|---|---|---|
| "settles for that behaviour" as the condition of row 1 ("fundament nie ma decyzji, jak agent do niego dotrze") — read as reaching the behaviour the project brings | reaching the running product as a whole | Readings differ only where a decision covers the product but not the project's new behaviour; skill step 1 already treats a decision the project changes as not holding the choice, so they converge in practice. If the human meant the product, one phrase of WAY-121 changes. |
| A matter the foundation settles is not listed (not even `held by`) | listing it `held by` like an ordinary choice | Row 1 lists a matter only when the foundation has no decision; answer 8 says later projects "nic nie wpisują". If `held by` was wanted, a clause of WAY-121 and the skill change. |
| WAY-121's first and third sentences merged | a fourth binding sentence (the guard allows three); the exception as a new decision | Wording only; meaning unchanged — visible in the diff for the assessor. |
| WAY-121 derives from WAY-100 and names the adoption in *Rationale* | adoption named in WAY-165 | Low; WAY-143 shows the same form. |
| *Review when* on WAY-121 (2027-03-31) | `none` | A review at the date that finds nothing — one review record. |
| Scope `project-level, decisions` for WAY-165/166, as WAY-121/122/123/137/138 | `project-level` alone | Selection of later changes to the decisions part reads two more entries; or misses them if narrowed. Low. |
| Level 2 verification for all three | an invariant on the skill's text or a gate condition | A gate condition is excluded by To do 2; a text-presence invariant would check wording, not the step's judgment. |
| WAY-165 reuses number 165 (next free on the base; PR #23's WAY-165 never reached `foundations`) | WAY-167 to avoid the PR #23 number | Readers of closed PR #23 meet a different WAY-165; the log itself is consistent. |

## Commands, exit codes and outputs

All from the worktree root, Git Bash, Python 3.14. Outputs under
`.runs/task-cycles/agent-path-technology-step/reports/`.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-18` | 0 | 0 errors, 8 warnings, 5 unchecked | `guard-decisions.txt` |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 3 unchecked | `guard-invariants.txt` |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` (glossary file unchanged; run because *Avoid* counts span the foundation) | 0 | 0 errors, 0 warnings, 5 unchecked | `guard-glossary.txt` |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK | `tests-elements-decisions.txt` |
| `python -B gate/run_tests.py elements/invariants` | 0 | 233 tests OK | `tests-elements-invariants.txt` |
| `python -B gate/run_tests.py project-level` | 0 | 250 tests OK | `tests-project-level.txt` |
| `python -B gate/run_tests.py gate` (critical flows) | 0 | 98 tests OK | `tests-gate.txt` |
| fingerprint count (throw-away script using `relation-model/fingerprint.py`) | 0 | 450 decision-fingerprint links in the five foundation files, none stale; 5 links to WAY-121, all `ed19d693` | `fingerprint-links.txt` |

Warnings, named:

- WAY-03, WAY-21, WAY-52, WAY-55, WAY-69: check-by date 2026-10-02 passed without a review record
  (pre-existing, not this change).
- Placeholders `merge of <request link>` at WAY-121 (line 3470), WAY-165 (5374), WAY-166 (5414) —
  expected until the request exists.

`unchecked`, named:

- decisions: lines held on the main branch and versions gained per number; a template change without a
  log version (both `--base none`); `TODO` in the log; copies of a version both logs hold; fingerprints
  relations carry (all `--merge-onto none`) — the last is covered by the manual count above.
- invariants: identifiers, versions, corrections and the violated list (`--base none`); `TODO` in
  entries; fingerprints of links (`--merge-onto none`, covered by the manual count); note: no
  `human_verdicts.md`.
- glossary: count of *Avoid* words; terms reading alike; uses of changed definitions (`--base none`);
  `TODO`; terms with no use after the merge (`--merge-onto none`). A grep of the added lines finds no
  *Avoid* word (`checker`, `quality gate`).

These are partial checks, not a pass of the full gate. `decisions-found-for-change` has `Method: TODO`.

## Changed files (commit range `77c8a8b..49d7d2b`)

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 138 | 15 |
| `foundations/invariants.md` | 1 | 1 |

## Sharpness inputs from the actual diff

- Criticality: parts `decisions` and `project-level` (by the changed entries' Scope), both carrying
  high failure modes in the map; `invariants` (one link line; part with no failure modes).
- Trust-boundary files: none touched (`project-level/readiness_check.py` unchanged).
- Irreversible operations: none (git changes on a task branch only; nothing outside the repository).

## Unresolved concerns (for the orchestrator, the critique and the human)

1. Condition of row 1 read as reaching "that behaviour" (see choices); the Polish "do niego" fits the
   product as well.
2. WAY-166 leaves open the case where no option of a choice can be used by an agent: "the
   recommendation passes over it" then leaves no option to recommend, while WAY-123 expects a
   recommendation. The row does not settle it; not written.
3. A persistent dedicated test environment offered for the development data is a place where the
   product runs. WAY-166 governs it as an option of the development-data choice; a separate choice of a
   place to run keeps WAY-137. This is said in WAY-166's *Rationale* only, not as a binding sentence or
   a `narrows WAY-137`; the critique may judge whether the two decisions can be read as colliding.
4. WAY-121's meaning changed (row 1) and its *Approved by* moved from a date to the merge placeholder:
   the request has to show this change of meaning to Mariusz for renewed acceptance (WAY-07, README).
5. No invariant sentence or check changed, so no WAY-69 agents are needed at this step.
