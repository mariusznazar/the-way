# Planner report — task `task-cycle-skills-shape`

- Status: `done with concerns`
- Method: `plan-task` from the base copy, `.runs/the-way-base/task-cycle/plan/SKILL.md`, read whole
- Plan: `.runs/task-cycles/task-cycle-skills-shape/plan.md`
- Size report: `.runs/task-cycles/task-cycle-skills-shape/plan-size.md`
- Size check: `python -B .runs/the-way-base/task-cycle/slice_size.py .runs/task-cycles/task-cycle-skills-shape/plan.md`,
  from the worktree root, exit code 0 — all 11 slices fit (largest: Slice 11, about 70 000
  estimated tokens; most files changed: Slices 3 and 4, 10 each). Nothing failed and nothing was
  left unchecked.
- Nothing written outside `.runs/`; no code, no commit; `git status` of the worktree is clean.

## The plan in brief

- *Foundation entries*: rows 1–3 of *Settlements to record* (changes of WAY-125, WAY-127 and
  WAY-256), written before slice 1 through the base copy's `record-decision`. Where the WAY-33
  search will lead outside the foundation is placed: `AGENTS.md:9-11` and the generator's sentence
  in Slice 2, `instruction-files/kind_skill.md` in Slice 1, the restatement of WAY-125 in
  `task-cycle/skill/SKILL.md:66-70` and `:128-137` in Slice 11. No invariant, term, fact or
  part-map entry: new files lie under `task-cycle/**`, which the part map already assigns.
- Slice 1 — the exception in `instruction-files/kind_skill.md` (*To do* 2).
- Slice 2 — the generator's sentence, its test's assertion (test changed first and seen failing),
  `AGENTS.md:9-11`, and the first six entry points (*To do* 3, acceptance criterion 1).
- Slices 3–6 — the remaining 36 entry points in batches of at most ten files; Slice 6 runs
  `--write` and leaves every entry point current.
- Slices 7–11 — the five skills judged and rebuilt: `make-change` (after the example),
  `write-spec`, `plan-task`, `review-change`, then `implement-task`, whose handoffs name the stage
  skills' new layouts and carry the change of WAY-125 (*To do* 1, 4, 5).
- A section "Common to the rebuild slices" (plan lines 26–87) holds what Slices 7–11 share — the
  method and its exception, the step-1 matters settled, the acceptance the task gives in advance,
  the layout and text rules, the report's contents (*To do* 6) and the common checks, among them a
  runnable sentence comparison for acceptance criterion 2. Each of those slices names it in its
  *Read*, so the orchestrator copies it into their handoffs word for word.

## Open design choice (section 2)

None found. The layout of each skill follows from WAY-256, WAY-257 and row 3 applied fragment by
fragment, as the orchestrator's start answered; the rewording of `AGENTS.md:9-11` and the cutting of
the entry points into batches are choices of how to make what the task settles, listed under
*Choices*.

## Guidelines

None: the-way has no `guidelines/`, and the task's second question settles the selection as empty
(cycle choice C2). No styleguide, so no order-of-work example to follow or depart from.

## Reaches beyond the dispatch

Each read to cut slices or name what a slice reads, not to design the change:

- Foundation entries not named in the handoff, read whole and named in slices' *Read*: WAY-44
  (generated files belong to their generator's part — Slice 2), WAY-129 (a pointer names its file in
  backticks with its condition — Slices 2, 7–11), WAY-136, WAY-161, WAY-162, WAY-164, WAY-219,
  WAY-220, WAY-13, WAY-227, WAY-229, WAY-135 (decisions with *Scope* `task-cycle` the respective
  skills carry; the handoff left the selection to me); invariants `outbound-link-reach` and
  `instruction-file-imports` (*Part* `every`; a rebuilt skill or `AGENTS.md` could break them).
  Found by `grep` over `foundations/decisions.md` and `foundations/invariants.md` for the
  identifiers and the parts `task-cycle`, `instruction-files`, `agent-instructions`.
- `agent-instructions/skill_entry_points.py:140-190` and `agent-instructions/test_skill_entry_points.py`
  (the sentence, the assertion, the test names for the focused unittest command — run once on the
  base: 6 tests, OK).
- `gate/test_skills_reach_the_way_sessions.py:1-60`, `:108-200`: the gate test of
  `skill-entry-points` requires the skill's path in backticks and four fixed phrases
  (`REQUIRED_WORDS`, `PREFIX_WORDS`); the new sentence must keep them, since this file may not change
  (acceptance criterion 1). Named in Slice 2.
- `task-cycle/slice_size.py:10` names `task-cycle/plan/SKILL.md` as the place of the plan form, so
  Slice 9 keeps the form there.
- `installation/README.md:78-82` cites "step 2 of `task-cycle/skill/SKILL.md`", so Slice 11 keeps
  the step numbers. `installation/install.py:115-140` — see concern 2.
- `agent-instructions/README.md` and `AGENTS.md`, whole (the integration route; the line the WAY-33
  search of row 2 finds).
- The-way's history, for a precedent of regenerating many entry points under the size limit:
  `git show 3b36c02:docs/task-cycles/coding-guidelines/plan.md` (Slices 6–10 there wrote entry
  points in batches of eight from `produce(discover(ROOT))` in process). Slices 3–6 follow it.
- `python -B .runs/the-way-base/instruction-files/check_instructions.py .` on the worktree: 0 errors,
  1 warning (`AGENTS.md:20`, `_zadania\` — a private folder, as the example's note also says; not
  this task's).

## Concerns

1. **The entry points are written in five slices, not by one `--write`.** *To do* 3 says the entry
   points are regenerated by `python -B agent-instructions/skill_entry_points.py --write`. One slice
   doing that changes 45 files against the script's limit of 10, so the plan writes 34 of them from
   the generator's own `produce` in process (Slices 2–5) and runs `--write` for the last eight
   (Slice 6). The end state is byte-for-byte what `--write` gives, and Slice 6's check shows it. Cost:
   four extra cheaper dispatches; between Slices 2 and 6,
   `test_the_tracked_entry_points_are_what_the_generator_produces` fails by design — each slice's
   text says so, so that the retry rule (WAY-229, a failing check of the slice) is not triggered by
   it. If you would rather keep one slice of 45 files against the size script, that is your call at
   the plan's review; I followed the method, which says to split.
2. **The product entry points the installer writes use other words.** `installation/install.py:135`
   writes "Read `.the-way/<path>` in full and follow it." — no instruction to read the files the skill
   names, so nothing there contradicts row 2. `installation/README.md:57` describes those entry
   points as reading "its source skill and referenced files from `.the-way`", which can be read as
   the same "all at the start" the task removes. It lies in `installation`, outside the task; I
   placed no slice on it. Proposed: a process remark in the record, not a change in this request.
3. **Slices 8–11 name their new files without paths.** The layout is the executor's (C3), so
   *Change* reads "`<dir>/SKILL.md`, and each file beside it … that the judgment creates". The size
   script therefore counts one changed file for each; the mechanical check of step 9.3 will see the
   new files as within that wording.
4. **Model classes.** `make-change` is `cheaper` (the example settles its table and layout); the
   other four judgment slices are `strongest`, with reasons. Under WAY-229 an executor of the
   strongest class gets no retry; on this harness `same` and `strongest` are one class (C6), so
   choosing `same` instead would change nothing in practice.
5. **What the sentence comparison cannot see.** It shows every sentence lost, changed or added, so
   acceptance criterion 2's "nothing disappears or changes" is checkable. It does not show a
   fragment moved to a file whose pointer an agent would pass by; that rests on the table's second
   question (WAY-257) and on the review of the whole change.
6. **Slice 11 is the heaviest by work, not by reading** (6 605 words to judge, handoffs joining four
   layouts, the two carried questions). I kept it whole, because the judgment needs the picture of
   the whole skill. If it returns too large, the first split line is between "Start and record" and
   "Design and execution choice".
7. **A section the template does not have.** "Common to the rebuild slices" stands between
   *Foundation entries* and *Slices*. It keeps the shared rules of five slices in one place instead
   of five copies; the size script ignores it, and each slice's *Read* names it by its range
   (`plan.md:26-87`). If you change the plan above that section, recompute the range.
8. **Step 1 of `maintain-instruction-files` is narrowed by the plan** (Common, point 2): the tools,
   the configuration, where sessions start and the search of session records are settled or left
   out, so that executors do not return questions you would answer the same way. As a result, a
   "remove" proposal will carry no evidence of a mistake from records; it stays only a proposal.

## Questions

None waiting. The two carried questions are handled as C3 and C4 bind them (Slice 11's *Goal*),
not settled in the plan.
