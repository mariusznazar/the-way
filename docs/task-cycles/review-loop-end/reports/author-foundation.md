# Author report — foundation step (turn 1)

Status: **done** — foundation change committed, boundary reached (no code, no skill or template
edits). Author: general-purpose subagent, claude-opus-5-5, one-author route (WAY-136).

## Input versions

- Base and process pin: `e7f7c3a15c3f80143f9ad582ec785c993cff3779` (`origin/foundations`).
- Frozen task: `.runs/task-cycles/review-loop-end/task.md` (accepted 2026-10-17), rows 1–7 of
  *Settlements to record*, answers to questions 1–9.
- Cycle record `.runs/task-cycles/review-loop-end/cycle.md`, handoff
  `reports/author-foundation-handoff.md`.
- Read whole: `AGENTS.md`, `agent-instructions/README.md`, `task-cycle/skill/SKILL.md`,
  `.claude/skills/the-way-record-decision/SKILL.md`, `elements/decisions/skill/SKILL.md`,
  `elements/decisions/template.md`, `elements/decisions/examples.md` (WAY-03),
  `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/common/skill/SKILL.md` (named by way_of_working's mode list; read for completeness).
- Superpowers 6.4.1 from `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`
  (not the Skill tool): `requesting-code-review/SKILL.md`, `requesting-code-review/code-reviewer.md`,
  `subagent-driven-development/SKILL.md`, `subagent-driven-development/re-review-prompt.md`, whole.
  The task's line references (`code-reviewer.md:43-48`, `:113-120`; SDD `:364`, `:372-373`,
  `:411-427`, `:458-469`) match the files.
- No other element skill was needed: the search found no glossary term, invariant, fact or
  part-map entry to write.

## Selection summary

Full record: [foundation-selection.md](foundation-selection.md). Touched part `task-cycle` (the
changed file `foundations/decisions.md` collects entries; every entry written or edited has *Scope*
`task-cycle`). 56 expected *Scope* matches, all read whole (the whole decision log was read); the
ten decisions the task names are among them; no missing match. Part map and glossary read whole;
relevant `every` invariants read whole, the rest discovered; environment facts inspected, study
facts read, none relevant.

## WAY-33 search — domain, terms, findings

- Domain: all five elements (`decisions.md`, `invariants.md`, `glossary.md`, `part_map.md`,
  `environment_facts.md`, plus `violated_invariants.md`) at `e7f7c3a`, plus incoming fingerprints of
  WAY-125/136 across the whole repository.
- Terms: re-review, fix range, second review, blocked, draft, Critical, Important, Minor,
  non-blocking, widen, out of scope / outside / beyond / past the task, weakest, most likely,
  deliberate break, final review, whole-change / whole-branch review, fix wave, finding, remark, fix,
  repair, round, loop, Declined, ledger, park, reviewer, code review, independent review, test
  first, severity, cost, tokens, stop(s), ask(s) the human, new task.
- Findings, each read whole and settled:
  1. No decision sets the number of review rounds, what follows a failed re-review, which findings
     block, or where Minor / out-of-scope findings go → new questions, new numbers (WAY-19).
  2. WAY-125 adopts SDD "with independent task and final code reviews" and `requesting-code-review`,
     i.e. the four steps the task's *Decisions in play* names as departures → **edited in place**
     (see choices).
  3. WAY-136 defines "the review of the whole change" and is what the new rules serve; it states no
     loop end and already holds three binding sentences → unchanged, linked by `derives from`.
  4. WAY-140 / WAY-101 (human creates tasks outside the repository; product chooses its backlog) →
     WAY-161 derives from WAY-140; WAY-101 cited in rationale.
  5. WAY-11 / WAY-10 (return step and assessment before merge) → WAY-163 derives from both; it moves
     them after the human's decision, never past the merge.
  6. WAY-69 (deliberate break by the reviewer; invariant check by a non-author) → WAY-164's
     rationale and *violates* example keep the weakest-point check apart from both.
  7. WAY-13 (check more sharply, never less), WAY-148 (reports through files), WAY-149, WAY-160
     (full gate) → agree; WAY-164 derives from WAY-148.
  8. WAY-100 (a borrowed practice binds only through a decision naming it) → WAY-161/162/164 derive
     from WAY-100 and name the borrowed harness practice in their rationale, without pointing to it
     (WAY-27).
  9. Part map, `task-cycle` failure mode "the orchestrator stops for an implementation choice it can
     settle … waits for the human before its request" → no collision: a blocked request is the
     request itself, not a pause before it. Possible new failure mode noted under concerns.
  10. Glossary: `verdict`, `correction`, `result` are narrow; the new wording uses "grade" for the
      reviewer's Critical/Important/Minor, "fix" for the repair, "what the check showed" for a check's
      outcome. No new glossary term needed ("finding", "blocking", "grade" are used as the field uses
      them).
  11. Invariants: none derives from WAY-125/136; no commit-testable sentence found (see choices).
  12. Incoming fingerprints of WAY-125 (`7362c7ab`) in WAY-140, WAY-148, WAY-157 → checked against
      the new binding part, still valid, renewed to `18d08c16` (WAY-31). No other file carries it.

## Entries written or changed

| Identifier | Rows | Meaning (Polish) |
|---|---|---|
| WAY-125/1 (edited in place, binding part changed) | departures behind rows 1, 2, 5, 6 | Cykl nadal przyjmuje metody Superpowers 6.4.1, ale w recenzji całej zmiany kroki tych metod, w których orkiestrator sam rozstrzyga uwagi pozostałe po poprawce, poprawka obejmuje uwagi Minor, uwagi spoza zakresu czekają w rejestrze metody, a wykonawca rozstrzyga listę „Declined to judge”, ustępują WAY-161 i WAY-162. |
| WAY-161/1 (new) | 5, 6 | W recenzji całej zmiany na obu ścieżkach blokują tylko uwagi Critical i Important, których recenzent sam nie oznaczył jako wykraczających poza zakres zadania; recenzja bez uwag blokujących to przejście do requestu bez poprawki, a request wymienia w osobnych pozycjach nienaprawione uwagi Minor i uwagi spoza zakresu (każdą ze słowami recenzenta i miejscem w kodzie), z których nowe zadania wybiera i zakłada człowiek; orkiestrator nie przenosi uwag między tymi rodzajami. |
| WAY-162/1 (new) | 1, 2, 3 | W recenzji całej zmiany i w każdej późniejszej recenzji kodu (przy rozstrzygnięciu niezależnej oceny, przy uzgodnieniu z gałęzią docelową, przy uwagach człowieka do requestu) uwagi blokujące dostają jedną poprawkę i jedną ponowną recenzję; jeśli coś blokującego zostaje — także nowa uwaga Critical lub Important w samej poprawce — trzeciej rundy nie ma, orkiestrator tego nie rozstrzyga ani nie przenosi do rozstrzygnięć oceny, tylko otwiera szkic requestu oznaczony `blocked` z pozostałymi uwagami (miejsce, powód), tym, co próbowała poprawka, kosztem cyklu (czas, modele, tokeny z zapisu etapów) i liczbą rund; pętle poprawek pojedynczych części planu zostają jak w WAY-125 i WAY-136. |
| WAY-163/1 (new) | 4 | Przed otwarciem requestu zablokowanego przez recenzję cykl uruchamia pełną bramkę i zapisuje zapis cyklu z etapami, ale nie wykonuje kroku zwrotnego ani niezależnej oceny na kodzie, którego recenzja nie przyjęła — request nazywa je jako niewykonane, a praca po decyzji człowieka wykonuje je na kodzie, który przeszedł recenzję albo który człowiek przyjął mimo uwagi. |
| WAY-164/1 (new) | 7 | Przed recenzją autor zmiany jednego autora wskazuje wymaganie zadania, a wykonawca każdej części wymaganie swojej części względem zadania, którego jego praca najpewniej nie spełnia, pisze sprawdzenie, które by to złapało, i podaje w raporcie, które wymaganie, jakie sprawdzenie i co ono pokazało; raport czyta recenzent, a request wymienia to w dowodach testów. |
| WAY-140/1, WAY-148/1, WAY-157/1 | — | Bez zmiany znaczenia: odświeżony odcisk relacji do WAY-125 (`7362c7ab` → `18d08c16`). |

Fingerprints: WAY-125 `18d08c16`, WAY-161 `d6d3137b`, WAY-162 `ce2e41f0`, WAY-163 `80d2e584`,
WAY-164 `898c9d56`. *Approved by* of WAY-125 and WAY-161..164: `Mariusz, merge of <request link>`
(WAY-140/148/157 keep theirs: only a relation fingerprint moved, as in earlier renewals).
*Review when* set by the author: WAY-161 (a Minor or out-of-scope finding later left a task
requirement unmet · 2026-12-31), WAY-162 (two of the first five cycles blocked by a remaining
finding · 2026-12-31), WAY-163 `none`, WAY-164 (five cycles and no weakest-point check ever failed
on its work · 2026-12-31). Verification: level 2 with complies/violates for all.

## Carried questions touched

- **New decisions or an addition to WAY-136 (question a):** new decisions WAY-161..164. WAY-19 makes
  a new rule beside an existing decision a new question; WAY-136 answers "when a plan, who makes and
  reviews", not how the review loop ends, and its binding part already has the template's maximum
  of three sentences. The departures from adopted methods go into WAY-125 by an in-place edit.
- **Request list vs "nothing is deferred" (question b):** not a foundation matter. WAY-161 lists the
  *reviewer's findings*; the return-step sentence in `task-cycle/skill/SKILL.md:348-349` concerns
  *foundation entries*. The code step should scope that sentence to foundation entries.
- **Weakest-point check kept as a test (question c):** WAY-164 requires the check and its report,
  and settles nothing about retention, as the cycle record intends.
- **Blocks from later reviews (question d):** WAY-163 is worded by the principle of answer 7 — gate
  and record always; return step and assessment never on code the review has not accepted; the
  request names whichever of the two has not run on that code. This covers a block from the
  settlement review of step 11 (both may already have run) and from step 12.

## Choices, rejected alternatives, cost if wrong

| # | Choice | Rejected | Cost if wrong |
|---|---|---|---|
| F1 | Edit WAY-125 in place (a narrowing written into it), per the handoff and WAY-30: the change of WAY-125's meaning is carried by the accepted task document's *Decisions in play*, so no question to the human before the request. | New decisions carrying `narrows WAY-125` with WAY-125 untouched — equally valid under WAY-25/32 and avoids changing an approved decision and renewing three fingerprints, but a reader of WAY-125 alone would still see the full adopted method. | WAY-125's change of meaning must be shown to Mariusz at the merge (README, WAY-07); if he prefers the `narrows` form, the clause moves into WAY-161/162 relations — a local edit. |
| F2 | Four decisions: rows 5+6 → WAY-161, rows 1+2+3 → WAY-162, row 4 → WAY-163, row 7 → WAY-164; numbered so that the definition of a blocking finding (row 5) comes first. | One decision per row (seven) — rows 1–3 and 5–6 answer one question each, and splitting them would separate a rule from its scope; one decision for rows 1–6 — far over three binding sentences. | Low: renumbering before the merge is cheap. |
| F3 | WAY-161's listing of Minor and out-of-scope findings is scoped to the review of the whole change, as rows 5–6 say; WAY-162 applies "blocking, as WAY-161 grades them" to later reviews (task Context: rows 1–4 use row 5's blocking finding). | Extending the request listing to later reviews — no row says so. | A Minor finding of a later review has no stated route (see concerns). |
| F4 | Level 2 verification for all four; no invariant. Runtime coordination of a cycle cannot be made false by a commit except as prose of the skill, and the handoff forbids a check that merely asserts prose. | An invariant on the skill text — a prose assertion. | None expected; the return step re-asks. |
| F5 | Based on of WAY-161/162 quotes the Superpowers 6.4.1 passages they replace, as an observation (as WAY-125/136 do); the borrowed harness practice is described in rationale, not cited (WAY-27: its source is not reachable from the repository). | Citing the harness's template lines — a pointer readers cannot open. | A changed Superpowers version shows which decisions depend on these passages. |
| F6 | "Requirement of the task" for the task's "punkt zadania" in WAY-164; "grade" for the reviewer's severity; "fix" for the repair; "work on the request's branch after the human's review / decision" for the task's "poprawka po recenzji człowieka" (glossary `correction` is narrow). | Using "verdict"/"correction"/"result". | Wording only. |
| F7 | WAY-125/161..164 get the request-link placeholder; WAY-140/148/157 keep their *Approved by* (fingerprint renewal only), following the renewal precedent of PR #21 (WAY-140). | Placeholder on all seven. | If the human counts a renewal as a change, three placeholders to add. |

## Commands, exit codes, outputs

All run from the worktree root, Git Bash, Python 3.14 (`python -B`), on the committed state
(`0761d6d`) except where noted; full stdout+stderr in this reports directory.

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [foundation-guard-decisions.txt](foundation-guard-decisions.txt) | 0 errors, 10 warnings, 5 unchecked |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | [foundation-guard-invariants.txt](foundation-guard-invariants.txt) | 0 errors, 0 warnings, 3 unchecked |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | [foundation-guard-part-map.txt](foundation-guard-part-map.txt) | 0 errors, 0 warnings, 7 unchecked |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | [foundation-guard-glossary.txt](foundation-guard-glossary.txt) | 0 errors, 0 warnings, 5 unchecked |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 | [foundation-guard-environment-facts.txt](foundation-guard-environment-facts.txt) | 0 errors, 0 warnings, 3 unchecked |
| `python -B gate/run_tests.py elements/decisions` | 0 | [foundation-tests-decisions.txt](foundation-tests-decisions.txt) | 169 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | [foundation-tests-task-cycle.txt](foundation-tests-task-cycle.txt) | 41 tests OK |
| `python -B gate/run_tests.py gate` (critical flows) | 0 | [foundation-tests-gate.txt](foundation-tests-gate.txt) | 98 tests OK |

The four non-decision guards were rerun on the committed state `0761d6d` with the same results.

Warnings, named: five pre-existing (WAY-03, WAY-21, WAY-52, WAY-55, WAY-69: check-by 2026-10-02
passed without a review record — same five on the base); five expected placeholders `merge of
<request link>` (WAY-125, WAY-161, WAY-162, WAY-163, WAY-164).

Unchecked, named (all from `none` options or absent product commands): decisions — lines held on
main and versions per number, template change without a version (`--base none`); `TODO` in the
log, copies of versions both logs hold, fingerprints relations carry (`--merge-onto none`).
Invariants — identifiers, versions, corrections and the violated list (`--base none`); `TODO`,
link fingerprints (`--merge-onto none`). Part map — parts lists of `wording-reaches-dependants`
and `skills-reach-the-way-sessions` (no coverage file); promise-level change paths and the
dependency graph (no product command); known violations, identifiers, criticality lowering
(`--base none`). Glossary — *Avoid* counts, terms reading like identifiers, uses of changed
definitions (`--base none`); `TODO`, terms with no use after the merge (`--merge-onto none`).
Facts — identifiers and versions (`--base none`); fingerprints decisions carry for facts, facts
nothing names after the merge (`--merge-onto none`).

Manual check (not a command of the product): relation fingerprints of the whole log recomputed
with `elements/decisions/format_guard.py`'s parser and `relation-model/fingerprint.py` — actor:
this author, method: parse every version, compare each `WAY-n@fp` in *Relations* with the current
binding fingerprint, observed: 0 stale; evidence: the fingerprints listed above; command-execution
fields: not applicable (scratch script, not kept). This covers the `--merge-onto none` gap for
relation fingerprints only.

Not run: the full required gate (orchestrator, step 10); the second WAY-33 search against the
integration tip and the independent assessment (later stages).

## Changed files (commit range `e7f7c3a..0761d6d`)

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 225 | 8 |

Commit: `0761d6d` docs(foundations): settle the end of the whole-change review loop (author
address checked: private address, as the repository's rule expects). `.runs/` not staged.

## Sharpness inputs from the actual diff

- Criticality: the changed file belongs to part `decisions` (failure mode high, not detected); the
  entries concern part `task-cycle` (three failure modes, all high, not detected). Highest: high.
- Trust-boundary files: none (`decisions` and `task-cycle` declare none).
- Irreversible operations: none (git text change).

## Unresolved concerns for the next dispatch

1. **Later reviews' non-blocking findings.** WAY-162 bounds every later code review with WAY-161's
   grades, but no row says where Minor or out-of-scope findings of those later reviews go;
   WAY-161's request items cover the review of the whole change only. The code step should not
   invent a rule; leaving those reviews' non-blocking findings as today (or asking) is the
   orchestrator's call.
2. **"Place in the code" for a "Declined to judge" line.** Row 6 requires each out-of-scope
   finding with its place in the code; a declined line may concern behaviour with no line in the
   diff. If the code step needs "where the reviewer gives one", that is a value the row does not
   give — a question, not an edit.
3. **WAY-125 meaning change** must appear in the request's *What this request settles* as a changed
   approved decision (README, WAY-07), beside WAY-161..164.
4. **Possible new `task-cycle` failure mode** for the return step: "the orchestrator rules on a
   blocking finding left after the review of the fix and marks the request ready — the human merges
   a change its reviewer did not accept — high — not detected". Failure modes are a human's to
   record (WAY-46), so it is a candidate only; criticality would not change.
5. The SKILL intro (`task-cycle/skill/SKILL.md:16-19`) and step 9's one-author loop
   (`:308-309`), steps 10–13 and the correction section need the code step to follow
   WAY-161..164; `task-cycle/record_template.md` may need a field for review rounds / weakest-point
   evidence. Not touched here, as the handoff requires.
