The five skills of the task cycle — `implement-task`, `make-change`, `write-spec`, `plan-task` and `review-change` — are rebuilt in the shape WAY-256 gives. Each `SKILL.md` keeps the overview, the rules that hold across its steps and the pointers. A fragment that only one step or one variant needs now stands in a file beside the skill, and the step that needs it names that file. WAY-125 changes, so a stage agent reads its method's `SKILL.md` whole and any other file the method names only when the step that names it comes. Without this change the move would spare nothing. The entry points of the-way's skills say the same (WAY-127). WAY-256 gains an exception: a fragment that is one instruction stays where its pointer would stand.

Source: the task "the way, seria skilli 1/11: pięć skilli cyklu zadania w kształcie WAY-256, ze zmianą WAY-125" (independent; `Status: ready for cycle`, 2026-10-28; settlement rows accepted 2026-10-28), frozen in the cycle record with its two sources (the example of `make-change` and the series note). Base `foundations` at `cf11541`. Process pin: none — this is the-way itself (route of `agent-instructions/README.md`). As the task asks (To do 7), every agent of the cycle read the methods of its stage from a copy of the-way at `cf11541` in the worktree's ignored `.runs/`, not from this branch.

## Cycle

- Spec: none. Settlement rows 1–3 settle the three foundation changes. To do 3 and acceptance criterion 1 settle the code. The layout of each skill follows from WAY-256 and WAY-257, applied fragment by fragment by the agent that rebuilt it.
- Route: a plan of 11 slices with the foundation entries first, because the work divides along the five skills. Planned in order:
  - the foundation entries (`40f0fd3`, Opus);
  - the exception in `instruction-files/kind_skill.md` (Slice 1, `746da1b`);
  - the generator's sentence, its test and `AGENTS.md` (Slice 2, `61cc5ab`);
  - the 42 entry points in batches of at most ten files, the size limit of a slice (Slices 2–6, last by `--write`, `b898353`);
  - `make-change` (Slice 7, `9b776fe`, Sonnet);
  - `write-spec` (Slice 8, `bf75d1c`);
  - `plan-task` (Slice 9, `00d000e`);
  - `review-change` (Slice 10, `a2456e5`);
  - `implement-task` last, since its handoffs name the stage skills' new files (Slice 11, `7369993`).

  Slices 1–6 ran on Sonnet, and Slices 8–11 and the foundation entries on Opus.
- Review of the whole change, by an agent that made none of it: `PASS 7369993`, 0 blocking. Its own sentence-by-sentence comparison of the five skills found no rule dropped or changed in meaning. Return step: no entry out of line with the code; no commit.
- Please merge with a merge commit that keeps the commits; the record link below holds only then.

## What changed

- `foundations/decisions.md`: WAY-125, WAY-127 and WAY-256 changed in place (below).
- `instruction-files/kind_skill.md`: the one-instruction exception, citing WAY-256.
- `agent-instructions/skill_entry_points.py:175-177` and its test's assertion (`test_skill_entry_points.py:53-54`): the sentence every entry point carries now reads "Read `<skill>` there in full and follow it, and read a file it names under the same root when the step or variant that names it comes, not all of them at the start, never a copy in another checkout or worktree." All 42 entry points were regenerated, one line each. No other Python changed.
- `AGENTS.md:10-12`: the same rule in the paragraph on skills.
- `task-cycle/change/`: step 1 opens with a table of variants, as in the example. Beside it stand `slice.md`, `fix.md` and `ui_check.md`.
- `task-cycle/spec/`: `design.md` for the designer, `review.md` for the spec's reviewer.
- `task-cycle/plan/`: `too_large.md` for a planner after an attempt or a slice proved too large.
- `task-cycle/review/`: `whole_change.md` and `fix.md`. Sections were renumbered (old 6 "Report" is now 4); nothing outside cites the old numbers.
- `task-cycle/skill/`:
  - step 3 and the handoff paragraph carry the change of WAY-125;
  - seven files stand beside the skill: `plan_member.md`, `spec_review.md`, `planning.md`, `foundation_step.md`, `return_step.md`, `blocked_finding.md` and `correction.md`;
  - steps 1–14 keep their numbers;
  - the handoffs of the foundation step and the return step name `foundation_step.md` and `return_step.md`, so those agents no longer open the 6 605-word file (carried question 1);
  - `task-cycle/record_template.md` was judged for its place only — it stays where it is, read at step 5. Its content was not judged (carried question 2).

## Words each agent reads, before and after

Counted with `wc -w` over the files each variant reads from the skill's directory. Before is `SKILL.md` at `cf11541`. After is `SKILL.md` plus the files beside it that the variant's steps name.

| Skill | Agent and variant | Before | After |
|---|---|---|---|
| `implement-task` | orchestrator, one author (with or without a pin move) | 6 605 | 5 498 |
| | orchestrator, spec then one author | 6 605 | 5 667 |
| | orchestrator, planning | 6 605 | 5 952 (6 121 after a spec) |
| | orchestrator, correction session | 6 605 | 5 733 + the route files its work names |
| | add-ons: plan member +113; a blocked question or a finding that the spec contradicts a decision +376; request blocked by a finding +175 | | |
| | writer of foundation entries | 318-word paragraph inside the 6 605-word file | `foundation_step.md`, 376 |
| | agent of the return step | 254 + 318 words inside the same file | 593 (`return_step.md` + `foundation_step.md`) |
| `make-change` | one author | 1 777 | 1 619 |
| | slice (and its retry) | 1 777 | **1 820 (+43)** |
| | fix | 1 777 | 1 696 |
| | correction | 1 777 | 1 619 |
| | change that alters a screen | as above | +90 |
| `write-spec` | designer (new, after a discarded attempt, revising) | 1 066 | 993 |
| | spec's reviewer | 1 066 | 662 |
| `plan-task` | first plan, or after a reviewed spec | 2 178 | 2 089 |
| | after an attempt or slice proved too large | 2 178 | 2 247 |
| `review-change` | slice, return step, reconciliation | 1 860 | 1 478 |
| | fix, correction | 1 860 | 1 698 |
| | whole change | 1 860 | 1 751 |

`record_template.md` (1 901 words, read at step 5) is the same before and after.

`make-change`'s slice variant reads more than before, against the example's estimate of about 1 650. The table of variants costs about 150 words in `SKILL.md` for every agent. Its rows say what each file holds, so the agent can recognise its moment (WAY-257). And the two insets about a slice stay in place under the one-instruction exception.

## Judgment tables

Each skill's table, with its "remove" and "reword" proposals and the count commands, is posted in full as a comment below, one comment per skill. Every row gives:
- the fragment;
- when an agent needs it and whether the agent recognises that moment;
- the verdict, its reason and its ground.

## Proposals ("reword" changes a rule's content, so no file was edited)

1. `implement-task`, step 9 — state the class rules once, in a sentence common to step 9, so that the planned route's sub-steps can move to `planning.md`. That would spare about 616 words of a one-author cycle. Carried decision: WAY-229. The executor lists it as not recommended unless the cost alone is ground enough.
2. `implement-task`, step 2 — let the pin move leave `SKILL.md`, which costs 287 words of every cycle that moves no pin. This needs either the step 2 pointer to name `installation/README.md` beside the new file, or a settlement that a file beside a skill naming a file of the-way outside the skill is not a second level.
3. `plan-task:116-117` and `:170-171` — "*Read* is the whole reading of the slice's agent" would gain "besides its method". With WAY-125 as changed, the agent of a slice reads the files its method's steps name at their step; the added words keep a planner from putting a method's files into *Read*.

No skill had a "remove" proposal. No session records were searched (plan, "Common to the rebuild slices", point 2), so no proposal rests on a mistake seen in agents' work.

## What this request settles

- **WAY-125** (changed; settlement row 1) — Agent etapu czyta w całości `SKILL.md` swojej metody, a każdy plik, który metoda wymienia — także plik obok skilla — dopiero wtedy, gdy przychodzi krok albo wariant, który ten plik wymienia; orkiestrator nadal nie czyta metod, których sam nie prowadzi.
  - Wording wider than row 1: the row speaks of a file beside the skill. The entry reaches every file the method names, because To do 1 says `implement-task` stops telling stage agents to read at the start "wszystko, co metoda wymienia". The stage methods also name files elsewhere (`product-guidelines/reading.md`, `elements/common/way_of_working.md`). If you want row 1's narrower wording, it is a one-phrase edit.
- **WAY-127** (changed; row 2) — Plik wejściowy skilla the way każe czytać plik wymieniony przez skill z tego samego checkoutu albo worktree dopiero wtedy, gdy przychodzi krok, który go wymienia — nie wszystkie pliki naraz na starcie.
- **WAY-256** (changed; row 3) — Fragment kroku albo wariantu, który jest jedną instrukcją i inaczej stałby w pliku obok skilla, zostaje w `SKILL.md` w miejscu, w którym stałby odsyłacz do niego, bo odsyłacz też jest instrukcją; fragment z więcej niż jedną instrukcją nie zostaje tylko dlatego, że każda jest krótka.
  - "Inaczej stałby w pliku obok skilla" keeps the exception off the rules WAY-35 places in an element's template.

WAY-125 and WAY-127 also gained the link `derives from WAY-256`. No row was tied to an entry already stated.

Invariant tests altered: none. The changed assertion (`DECISION_ENTRY` in `agent-instructions/test_skill_entry_points.py`) is used by tests that cite no invariant; the test of `derived-file-content` and the gate's test of `skill-entry-points` are unchanged, and both pass. Surfaces altered: none. *Violated* marks set or cleared: none.

## Checks

- `python -B gate/run_tests.py` on `7369993` (final tree), Windows — exit 0; 613 tests in 8 directories, every directory passed. On the base `cf11541`: exit 0, 613 tests.
- `python -B elements/common/foundation_check.py` — exit 0, 0 errors (foundation-entries agent, with a broken reference shown to give 1; reviewer; return step).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, entry points current.
- The changed test assertion was seen failing before the generator changed (exit 1) and passing after it (exit 0). The reviewer repeated this in a scratch worktree.
- Acceptance criterion 2 (no rule lost or changed in meaning) — each of Slices 7–11 ran a sentence comparison of the skill at the base against the skill and its new files, and accounted for every line it printed. The reviewer ran its own comparison over all five skills.
- `git diff --check` — exit 0.

Not checked:
- No fresh agent session has used the rebuilt skills. Whether agents read a file beside a skill when its step comes, and not miss that moment, is untested. The measured cycle on `loop2` is meant to show it.

## Review findings not fixed

Minor findings of the review of the whole change, in the reviewer's words. The full report is linked from the record.

- **M1** — `task-cycle/skill/SKILL.md:37-60` (moving the pin, step 2) and `:253-295` (step 9, sub-steps 1–5 of the planned route) stay in `SKILL.md`, though only one route needs each — "about 900 words … that a one-author cycle with no pin move reads without needing them". The first reason holds; the second "can be met by a meaning-preserving rewording that keeps only the shared class sentence in `SKILL.md`". See proposals 1–2.
- **M2** — "`make-change`'s slice variant now reads more than before: 1 820 words against 1 777". The causes are the descriptive table rows, the stub of section 4 (`task-cycle/change/SKILL.md:93-95`) repeating the table's pointer, and the two insets kept in place.
- **M3** — step 13 of `implement-task` (`task-cycle/skill/SKILL.md:384-385`) says "*Questions*: only those the foundation step allows", but step 13 does not name `foundation_step.md`. The fix it recommends: add "and at step 13" to the read triggers at `:239-241`.
- **M4** — "`make-change`'s table of variants (`task-cycle/change/SKILL.md:19-26`) gives no case for a dispatch that names none of its rows": the agent of the plan's foundation entries and a fresh return-step agent. The base had the same gap. Recommended: a row or one sentence for "a stage your dispatch names that has no row: no file of this table".
- **M5** — wording left by Slice 2:
  - `AGENTS.md:10-12` leaves the short line "session works in. Use only these: a";
  - in the generator's sentence (`agent-instructions/skill_entry_points.py:175-177`, and so in all 42 entry points), "not all of them at the start" has no plural noun before it.

## Findings outside this task's scope

For you to choose which become new tasks:

- **O1 (Important, from the review)** — "Product entry points still say 'Read the files it references inside `.the-way`', with no word on when" — `installation/install.py:136` (`skill_wrapper`), described at `installation/README.md:57`.
  - In a product, the orchestrator reaches `implement-task` through it and may read all seven files beside the skill at the start.
  - The measured cycle on `loop2` runs through this entry point, so until the installer changes, that measurement mixes the gain of the new layout with agents reading everything up front.
  - Acceptance criterion 1 kept it out of this task. The reviewer recommends a task of its own before the measured cycle on `loop2`.
- **O2 (Minor, from the review)** — "The return `review-change` asks for lacks the one-line check result" that `implement-task:170-172` and WAY-148 expect. It was there before this change.
- **From the return step** — `task-cycle/skill/SKILL.md:41` and `:43` point to `installation/README.md`, but the part map's *Depends on* for `task-cycle` does not list `installation`. This predates this change (commit `4913b08`), and the part map's template sends a change of allowed dependencies to the human. Either add `installation` to that line, or keep the map and mark the mismatch.
- **Not judged** — the content of `task-cycle/record_template.md` (carried question 2: its place only).

## Questions

None.

## Other choices

21 other choices of the cycle stand in the questions table of the cycle record, `docs/task-cycles/task-cycle-skills-shape/cycle.md`. Commit RECORD_SHA adds that record. Among them: the entry points cut into five slices by the size limit (C7), and the classes of model (C6, C11).

## Human actions

None. Outside this request (the task's *Out of scope*):
- the measured cycle on `loop2` after the merge;
- pointing rows E16 and E17 of section s01e02 of the Mega.DEV map to WAY-125.
