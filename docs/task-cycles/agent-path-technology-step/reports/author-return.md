# Author report — return step (turn 3)

Status: done — one entry written and committed (`9587b0d`, on `2fabc67`); no invariant found; no
question for the human.

## Foundation selection refresh

- `git fetch origin`: `origin/foundations` is `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988`, the base — it
  has not moved; `git diff 77c8a8b origin/foundations` is empty.
- Real diff `77c8a8b..2fabc67`: `foundations/decisions.md`, `foundations/invariants.md`,
  `project-level/definition_template.md`, `project-level/technology/SKILL.md`. Touched parts:
  `project-level` (files and entries' Scope), `decisions` (changed entries WAY-121/122/123, new
  WAY-165/166), `invariants` (link of `project-technology-record/1`). Same set as the foundation step;
  the selection recorded in `foundation-selection.md` holds, refreshed with the new entries WAY-165 and
  WAY-166 (Scope `project-level, decisions`) read in place.
- Re-read for this step: `task-cycle/skill/SKILL.md` step 11 (first paragraph), the whole-change review
  (`review.md`), the glossary skill `elements/glossary/skill/SKILL.md`, `elements/glossary/template.md`
  and `elements/glossary/examples.md` (entries `invariant`, `gate`, `foundation`), WAY-40 and WAY-46.

## Candidates found and their classification

| Candidate | Classification | Reason |
|---|---|---|
| "agent's way to the running product" | glossary term — written | Stands in the binding parts of WAY-121, WAY-165 and WAY-166 (7 uses by the guard; also in the template and the skill). A reader of the field would read "an agent's way to the running product" as any means by which an agent gets at the product — a place to run, its deployment and access to the host included. The entries mean the narrower thing: what the agent checks user-visible behaviour through (the logs, interface and development data). The plain reading would put a place to run inside WAY-166's area ("in a choice of an agent's way to the running product"), where WAY-137 governs — the collision the cycle left to the assessment (C8). WAY-95 gives the phrase an entry. |
| "development data" | no entry | Used as the field uses it: data developers and tests use outside production; WAY-165 says what the matter asks, not what the word means. |
| "logs", "interface" | no entry | Field meanings; "as its user does" in WAY-165 is a requirement of the choice, not a meaning of the word. |
| `project-level` failure mode for the three matters (WAY-46) | no change | A matter left off the list is "a technology choice the project needs … missing from the definition's list — the first task chooses it — high — not detected" (`foundations/part_map.md:116-117`): the matter is a choice of the list, and the cycle improvising the access is the first task choosing it. Same detection (`not detected`), same severity; a second line would repeat it. |
| Invariant for WAY-121's exception, WAY-165 or WAY-166 | none | No sentence a commit of the-way makes false without a gate condition, which To do 2 excludes; a check on the wording of the template or the skill would test text, not the step. No code behaviour is uncovered: no executable code changed (`readiness_check.py` untouched, its 250 tests pass). |
| Step 0 resumes with the look on every list before approval; an approved definition does not come back for these matters | no entry — choice-table line | Order of the work of the skill (C10); the second follows from WAY-118 and the unchanged gate (To do 2). |
| "that tie rule serves a place to run alone" (skill 2.5) | no entry | Restates WAY-137's own scope. |
| Environment fact | none | Nothing in the change rests on a fact about the world. |
| New decision | none | Every rule of the text is carried by WAY-121, WAY-165, WAY-166, WAY-123, WAY-137. |

The five Minor findings of the review are not acted on here (WAY-161); they go to the request.

## Entries written

| Entry | Row | Meaning (Polish) |
|---|---|---|
| glossary term `agent's way to the running product` (new, `foundations/glossary.md`, first entry) | none — return-step finding (WAY-11, WAY-95) | „Droga agenta do działającego produktu” to środki, przez które agent sprawdza zachowanie widoczne dla użytkownika w produkcie, gdy ten działa. |

Entry text: "An agent's way to the running product is the means through which an agent checks behaviour a
user sees in a product while it runs." *Avoid* `none`, *Not* `none`. The definition holds no rule:
which matters belong to it stays in WAY-121's binding sentence; the genus "means" is no glossary term.
No use is rewritten: every use already writes the phrase. A new entry has no main-branch uses to
review (WAY-97). The term reads like no identifier of the part map, the invariants or the facts.

## Rows 1–4

| Row | Written in | Agrees with the text |
|---|---|---|
| 1 | WAY-121 sentence 3 (`49d7d2b`) | Yes: template Technology rule (`definition_template.md:167-175`), skill steps 0 and 1. |
| 2 | WAY-165 sentence 1 | Yes: template rule (`:176-179`). |
| 3 | WAY-165 sentences 2–3 | Yes: template rule (`:179-182`); review Minor 4 on "both options" stays a request item. |
| 4 | WAY-166 | Yes: template rule (`:224-228`), skill 2.3 and 2.5; WAY-137 unchanged. |

None missed. No projected entries (independent task).

## Second search of the whole foundation (WAY-33)

- Against: `origin/foundations` = `77c8a8b` (fetched; unmoved), on the branch tree at `9587b0d`.
- Domain: all five elements — `decisions.md`, `invariants.md`, `glossary.md`, `part_map.md`,
  `environment_facts.md`.
- Terms: logs, logging, observability, running product, working product, interface, UI, screen,
  browser, terminal, command line, API, seed, fixture, test data, development data, test environment,
  test server, staging, production, localhost, agent works with, tie, tied, place to run, deploy,
  belongs on the list, rule of belonging, "run, pay for or back up", way to the running product, agent
  can use, cannot use. Output: `return-second-search.txt`.
- Findings: the same as at writing, plus the new entries themselves — WAY-137 (place to run; agent
  operates and deploys it), WAY-139 (deployment skill reads logs at deployment), WAY-140 (effects outside
  the repository by a human; the copy of production in WAY-165's example is fetched by a human), WAY-143
  (a technical element enters with its first task), WAY-08/61 (exploratory test on the working
  product). None collides; the new glossary term keeps WAY-166's area apart from WAY-137's. No entry
  merged into `foundations` since the base.

## Questions for the human

None. No entry lacks a recommendation, no approved decision's meaning changes in this step (WAY-121's
change was settled by rows and is listed for the request already), every row holds, and no value is
missing.

## Commands, exit codes and outputs

Outputs under `.runs/task-cycles/agent-path-technology-step/reports/`.

| Command | Exit | Result | Output |
|---|---|---|---|
| `git fetch origin`; `git rev-parse origin/foundations` | 0 | `77c8a8b…` (unmoved) | — |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 5 unchecked | `return-guard-glossary.txt` |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --uses "agent's way to the running product"` | 0 | 7 uses | `return-glossary-uses.txt` |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-18` | 0 | 0 errors, 8 warnings (pre-existing WAY-03/21/52/55/69 check-by dates; three `merge of <request link>` placeholders), 5 unchecked | `return-guard-decisions.txt` |
| `python -B gate/run_tests.py elements/glossary` | 0 | 204 tests OK | `return-tests-elements-glossary.txt` |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK | `return-tests-gate.txt` |
| `python -B gate/run_tests.py project-level` | 0 | 250 tests OK | `return-tests-project-level.txt` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current | `return-skill-entry-points.txt` |
| `git diff --check 77c8a8b..HEAD` | 0 | no output | `return-diff-check.txt` |
| fingerprint count (scratch script, `relation-model/fingerprint.py`) | 0 | 450 links, 0 stale | `return-fingerprint-links.txt` |
| second search grep | 0 | 188 lines | `return-second-search.txt` |

`unchecked`, named: glossary — count of *Avoid* words, terms and identifiers reading alike (checked by
hand: none), uses of changed definitions (`--base none`); `TODO` in entries, terms with no use after
the merge (`--merge-onto none`). Decisions — as in turn 1 (two `--base none`, three `--merge-onto
none`; fingerprints covered by the manual count). Partial checks, not a pass of the full gate.

## Changed files

`2fabc67..HEAD` (`9587b0d`): `foundations/glossary.md` +7/−0.

`77c8a8b..HEAD`: `foundations/decisions.md` +138/−15, `foundations/glossary.md` +7/−0,
`foundations/invariants.md` +1/−1, `project-level/definition_template.md` +22/−0,
`project-level/technology/SKILL.md` +20/−2.

## Unresolved concerns

1. The glossary entry is a foundation change written after the whole-change review; it falls under the
   one independent assessment, which should receive `77c8a8b..9587b0d`.
2. The case "a reader of the field would read the phrase more widely" is a judgment; if the assessor
   finds the plain reading already narrow enough, the entry can go with no other change (no entry
   depends on it by fingerprint).
3. Turn-1 concerns under C8 (no usable option in a matter; test environment vs place to run) are
   unchanged; the new term narrows the second.

## Assessment settlement (turn 4)

Commit `ab60e7f` on `9587b0d`; exactly the four changes marked **Apply** in `assessment-settlement.md`.

- A1 — WAY-166 *Relations*: `derives from WAY-121@ed19d693 · narrows WAY-123@f3b45293 · narrows
  WAY-137@86b2a30d`. WAY-137's fingerprint recomputed with `relation-model/fingerprint.py`: `86b2a30d`,
  as the handoff gave. WAY-137 names no relation to WAY-166, so `narrows-pairs` holds; the guard
  reports no error. No binding sentence changed (WAY-166 stays `4b3a76a4`).
- A5 — WAY-121 *Review when*: "a task cycle finds no way to check behaviour a user sees in the running
  product although decisions on the matters of an agent's way to the running product stand · check by:
  2027-03-31" (first condition dropped; "those matters" spelt out because its antecedent went with it).
  WAY-121's binding fingerprint is unchanged (`ed19d693`); no link renewal.
- A7 — `project-level/technology/SKILL.md` step 0 bullet now reads exactly as the handoff gives.
- A8 — step 2.5: "; that tie rule serves a place to run alone" cut; the sentence ends "(WAY-137).".

Changed files `9587b0d..HEAD`: `foundations/decisions.md` +5/−5, `project-level/technology/SKILL.md`
+3/−4.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-18` | 0 | 0 errors, 8 warnings (WAY-03/21/52/55/69 passed check-by dates, pre-existing; placeholders at lines 3469, 5373, 5414), 5 unchecked (two `--base none`, three `--merge-onto none`) | `settlement-guard-decisions.txt` |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK | `settlement-tests-elements-decisions.txt` |
| `python -B gate/run_tests.py project-level` | 0 | 250 tests OK | `settlement-tests-project-level.txt` |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK | `settlement-tests-gate.txt` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current | `settlement-skill-entry-points.txt` |
| `git diff --check 77c8a8b..HEAD` | 0 | no output | `settlement-diff-check.txt` |
| fingerprint count (scratch script) | 0 | 451 links (one new: WAY-137 in WAY-166), 0 stale | `settlement-fingerprint-links.txt` |

Concern: none. The step 2.5 line "works with best, by the template's rule (WAY-137). In a" is left
short rather than rewrapped, to keep the diff to the cut.
