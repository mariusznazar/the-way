# Plan — Pięć skilli cyklu zadania w kształcie WAY-256, ze zmianą WAY-125 i wyjątkiem dla fragmentu z jedną instrukcją

- Task: `.runs/task-cycles/task-cycle-skills-shape/task.md`
- Spec: none
- Base: `cf11541f039649db3a76aa5aaa2d7cce2cc48f34` (`foundations`)

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| 1 — a stage agent reads its method's `SKILL.md` whole and a file beside the skill only at the step or in the variant that names it (change of WAY-125) | decision (change) | *Settlements to record* row 1 | Slice 11, which writes it into step 3 of "Inputs and authority" and the handoffs of `implement-task`; Slices 7–11, whose moves gain nothing without it |
| 2 — an entry point of a the-way skill has a file the skill names read from the same checkout or worktree when the step that names it comes, not all at the start (change of WAY-127) | decision (change) | *Settlements to record* row 2 | Slice 2 (the generator's sentence, its test, `AGENTS.md`), Slices 3–6 (the regenerated entry points) |
| 3 — a fragment of a step or variant that is one instruction stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too (exception in WAY-256) | decision (change) | *Settlements to record* row 3 | Slice 1 (`instruction-files/kind_skill.md`), Slices 7–11 (each judgment applies it) |

The three are written before slice 1, through the base copy's `record-decision`
(`.runs/the-way-base/elements/decisions/skill/SKILL.md`), into the worktree's
`foundations/decisions.md`. Their search of the whole foundation (WAY-33) will find, outside the
foundation, texts that this plan's slices bring in line, not the writer: `AGENTS.md:9-11` and the
generator's sentence (row 2) — Slice 2; `instruction-files/kind_skill.md` (row 3) — Slice 1; the
restatement of WAY-125 in `task-cycle/skill/SKILL.md:66-70` and `:128-137` (row 1) — Slice 11. A
finding inside the foundation (for example WAY-148, which derives from WAY-125, or WAY-258, which
cites WAY-256) is the writer's, as WAY-33 gives. No invariant, glossary term, environment fact or
part-map entry is written: every file the slices create lies under `task-cycle/**`, which the part
map already assigns, and the invariant `skill-entry-points` does not change (task, *Context*).

## Common to the rebuild slices

This section binds Slices 7–11; each of them names it in its *Read*. Each of those slices judges
one skill of the task cycle and rebuilds it by that judgment (task, *To do* 4).

1. **Method.** `maintain-instruction-files` of the base copy,
   `.runs/the-way-base/instruction-files/SKILL.md`, in the mode judge, for the kind skill — with
   `judging.md`, `kind_skill.md` and `tool_loading.md` of that copy as it names them — never the
   worktree's `instruction-files/`, which Slice 1 changes. Apply it with the exception of
   *Foundation entries* row 3: a fragment of one step or one variant that is one instruction stays in
   `SKILL.md` where its pointer would stand; the bound is one instruction against one pointer.
2. **What step 1 of that method asks of the repository as a whole is settled here, not asked.** The
   tools are Claude Code and Codex (`AGENTS.md:9-10`). Configuration settings and where sessions
   start are not read: the judgment is of one skill, which its agent loads from its handoff or, for
   `implement-task`, through its entry point. Session records are not searched: the ground of each
   row is the decision or the step of the cycle the fragment carries, as the example's column
   "Podstawa" gives it. A "remove" or "reword" proposal names the condition of "When to remove a
   rule" (`judging.md`) it rests on and says that no session records were searched.
3. **Who reads the skill and in which variants** comes from the skill's own text and from the
   places of `task-cycle/skill/SKILL.md` that dispatch it, which the slice's *Read* names.
4. **The table's acceptance is given by the task in advance** (*Questions to settle* 3 and 5), in
   place of the acceptance `judging.md` waits for: carry out without waiting the verdicts "keep" and
   "move" and the rewordings that change no meaning — a pointer's sentence, a row of a table of
   variants, a fragment of one instruction in place of its pointer. A "remove" or "reword" that
   changes a rule's content is a proposal in the report, with no edit.
5. **Layout.** `SKILL.md` keeps its frontmatter unchanged, the picture of the whole, the rules of
   working that hold across its steps and the pointers. A fragment that only one step or one variant
   needs goes to a file beside `SKILL.md`, in the skill's own directory, which that step or variant
   names by its path in backticks with the condition under which to read it (WAY-129), one level
   deep: no file beside the skill points to another. The names of those files are the executor's,
   each named in the report. A skill whose judgment moves nothing stays as it is, its table showing
   why.
6. **Text.** Every sentence of the skill at the base stands after the rebuild, word for word, in
   `SKILL.md` or in a file beside it, except the rewordings of point 4 and what the slice's *Goal*
   changes (acceptance criterion 2). No link into a private note collection enters the skill
   (invariant `outbound-link-reach`): the task's sources are private notes, and none of their paths
   goes into the-way. No script, test or other code is written (task, *Questions to settle* 3;
   *Out of scope*).
7. **Report**, besides what `make-change` asks: (a) the table in the form `judging.md` gives, one row
   per fragment — the fragment with `file:line` at the base, when an agent needs it and whether it
   recognises that moment (WAY-257), the verdict, the reason and the ground; (b) the "remove" and
   "reword" proposals apart, with no edit; (c) for each agent that reads the skill and each variant
   it works in, the words it reads before the rebuild and after it, counted with `wc -w` over the
   files that variant reads, the commands given; (d) the sentence comparison of the checks below,
   each line it prints accounted for; (e) the contradictions found between the skill and the places
   of `task-cycle/skill/SKILL.md` it read, or that none were found.
8. **Checks common to these slices**, with `<dir>` the skill's directory under `task-cycle/` and the
   outputs kept under `.runs/task-cycles/task-cycle-skills-shape/reports/`:
   - the sentence comparison (acceptance criterion 2):
     `git show cf11541:task-cycle/<dir>/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > <slice>-before.txt`,
     the same pipeline over `cat task-cycle/<dir>/*.md` into `<slice>-after.txt`, then
     `comm -3 <slice>-before.txt <slice>-after.txt`; every line it prints is accounted for in the
     report by a row of the table (a rewording that changes no meaning, a pointer, a row of the table
     of variants) or by the slice's *Goal*;
   - for each file beside the skill, `grep -n '<file>' task-cycle/<dir>/SKILL.md` shows it named at
     the step or variant that needs it, and `ls task-cycle/<dir>/` shows every file `SKILL.md`
     names beside it;
   - `git diff cf11541 -- task-cycle/<dir>/SKILL.md` leaves lines 1–4, the frontmatter, unchanged,
     and `python -B agent-instructions/skill_entry_points.py` prints `entry points are current` with
     exit code 0;
   - `grep -rn -E "Storage|The Brain|_zadania|Notes/" task-cycle/<dir>/` prints nothing;
   - `python -B gate/run_tests.py task-cycle` exits 0, and `git diff --check` prints nothing.

## Slices

### Slice 1 — The exception for a one-instruction fragment in the file of skills

- **Goal:** `instruction-files/kind_skill.md`, in its section "Where a fragment of a skill stands",
  says that a fragment only one step or one variant needs, which is one instruction, stays in
  `SKILL.md` where its pointer would stand, since the pointer is an instruction too — the exception
  *Foundation entries* row 3 adds to WAY-256 — citing WAY-256. The rule stands in that file alone
  (WAY-258): `instruction-files/SKILL.md` and the other files of that skill do not change. Process
  prose; no test asserts it.
- **Change:** `instruction-files/kind_skill.md`
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-61` Ustalone (Wzór) ·
  Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:7298-7331` WAY-258 ·
  `instruction-files/SKILL.md:97-151` Where a rule stands
- **Model:** cheaper
- **Risk:** none
- **Checks:** `git diff --stat <base>..HEAD` names `instruction-files/kind_skill.md` alone;
  `grep -n "WAY-256" instruction-files/*.md` shows the exception in `kind_skill.md` only;
  `python -B instruction-files/check_instructions.py .` reports 0 errors;
  `python -B gate/run_tests.py instruction-files` exits 0; `git diff --check` prints nothing.
- **Depends on:** Foundation entries row 3

### Slice 2 — The entry points' sentence on the files a skill names

- **Goal:** the sentence the generator writes into every entry point
  (`agent-instructions/skill_entry_points.py:175-176`, "read the files it names under the same root,
  never a copy in another checkout or worktree") says that a file the skill names is read from the
  same root when the step or variant that names it comes, not all of them at the start, and never
  from a copy in another checkout or worktree (*Foundation entries* row 2; task, *To do* 3 and
  *Questions to settle* 1). The assertion of its test on that sentence
  (`agent-instructions/test_skill_entry_points.py:52-56`, in `DECISION_ENTRY`) holds the new
  sentence; it is changed first and seen failing. The sentence keeps the skill's path in backticks
  and every phrase `gate/test_skills_reach_the_way_sessions.py:32-38` requires, since that test may
  not change (acceptance criterion 1). `AGENTS.md:9-11` ("each reads its skill and the files it
  names from the checkout or worktree the session works in") is reworded to the same rule, which
  the search of row 2 finds; it stays one sentence of the same section. The entry points of
  `critique`, `define-project` and `find-foundation-entries`, in both tools, are written from the
  generator's own `produce(discover(ROOT))`, run in process for those six paths only — never by
  hand and never by `--write`. No other Python changes.
- **Change:** `agent-instructions/skill_entry_points.py` ·
  `agent-instructions/test_skill_entry_points.py` · `AGENTS.md` ·
  `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md` ·
  `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md` ·
  `.claude/skills/the-way-find-foundation-entries/SKILL.md` ·
  `.agents/skills/the-way-find-foundation-entries/SKILL.md`
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:42-44` Questions to settle (the first) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:58-64` Context ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  Foundation entries row 2 (WAY-127 as the foundation step changes it) ·
  `foundations/decisions.md:1059-1093` WAY-44 · `foundations/decisions.md:2963-3011` WAY-128 ·
  `foundations/decisions.md:3012-3034` WAY-129 · `foundations/invariants.md:241-250`
  skill-entry-points · `foundations/invariants.md:56-65` derived-file-content ·
  `foundations/invariants.md:251-260` instruction-file-imports · `foundations/invariants.md:76-85`
  outbound-link-reach · `gate/test_skills_reach_the_way_sessions.py:1-60`
- **Model:** cheaper
- **Risk:** none
- **Checks:** with the assertion changed and the generator not yet,
  `python -B -m unittest discover -s agent-instructions -p "test_skill_entry_points.py" -k EntryPointText -k Writing`
  exits 1 on `test_text_is_the_written_out_form`; after the generator's change it exits 0.
  `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 36
  paths of Slices 3–6 and nothing else. `python -B gate/run_tests.py gate` exits 0.
  `python -B gate/run_tests.py agent-instructions` fails only in
  `test_the_tracked_entry_points_are_what_the_generator_produces` (invariant
  derived-file-content), on those 36 paths, until Slice 6 — an expected state recorded by test
  name, not a failing check of this slice. `git diff <base>..HEAD -- "*.py"` shows only the sentence
  and the assertion. `python -B instruction-files/check_instructions.py .` reports 0 errors.
  `git diff --check` prints nothing.
- **Depends on:** Foundation entries row 2

### Slice 3 — Entry points, first batch

- **Goal:** the entry points of `implement-task`, `lead-project`, `maintain-coding-guidelines`,
  `maintain-instruction-files` and `maintain-styleguide`, in both tools, are what the generator
  produces with Slice 2's sentence, written from `produce(discover(ROOT))` of
  `agent-instructions/skill_entry_points.py`, run in process for these ten paths only — never by
  hand and never by `--write`.
- **Change:** `.claude/skills/the-way-implement-task/SKILL.md` ·
  `.agents/skills/the-way-implement-task/SKILL.md` · `.claude/skills/the-way-lead-project/SKILL.md` ·
  `.agents/skills/the-way-lead-project/SKILL.md` ·
  `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md` ·
  `.agents/skills/the-way-maintain-coding-guidelines/SKILL.md` ·
  `.claude/skills/the-way-maintain-instruction-files/SKILL.md` ·
  `.agents/skills/the-way-maintain-instruction-files/SKILL.md` ·
  `.claude/skills/the-way-maintain-styleguide/SKILL.md` ·
  `.agents/skills/the-way-maintain-styleguide/SKILL.md`
- **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
  foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
  `foundations/invariants.md:56-65` derived-file-content
- **Model:** cheaper
- **Risk:** none
- **Checks:** each pair byte-identical and equal to what `produce` gives for its path;
  `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 26
  paths of Slices 4–6; `git diff --stat <base>..HEAD` names these ten paths alone.
- **Depends on:** Slice 2

### Slice 4 — Entry points, second batch

- **Goal:** the entry points of `maintain-testing-guidelines`, `make-change`, `plan-project`,
  `plan-task` and `record-decision`, in both tools, are what the generator produces with Slice 2's
  sentence, written from `produce(discover(ROOT))` of `agent-instructions/skill_entry_points.py`,
  run in process for these ten paths only — never by hand and never by `--write`.
- **Change:** `.claude/skills/the-way-maintain-testing-guidelines/SKILL.md` ·
  `.agents/skills/the-way-maintain-testing-guidelines/SKILL.md` ·
  `.claude/skills/the-way-make-change/SKILL.md` · `.agents/skills/the-way-make-change/SKILL.md` ·
  `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md` ·
  `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md` ·
  `.claude/skills/the-way-record-decision/SKILL.md` ·
  `.agents/skills/the-way-record-decision/SKILL.md`
- **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
  foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
  `foundations/invariants.md:56-65` derived-file-content
- **Model:** cheaper
- **Risk:** none
- **Checks:** each pair byte-identical and equal to what `produce` gives for its path;
  `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 16
  paths of Slices 5–6; `git diff --stat <base>..HEAD` names these ten paths alone.
- **Depends on:** Slice 3

### Slice 5 — Entry points, third batch

- **Goal:** the entry points of `record-environment-fact`, `record-glossary-term`,
  `record-invariant` and `refine-task`, in both tools, are what the generator produces with Slice
  2's sentence, written from `produce(discover(ROOT))` of `agent-instructions/skill_entry_points.py`,
  run in process for these eight paths only — never by hand and never by `--write`.
- **Change:** `.claude/skills/the-way-record-environment-fact/SKILL.md` ·
  `.agents/skills/the-way-record-environment-fact/SKILL.md` ·
  `.claude/skills/the-way-record-glossary-term/SKILL.md` ·
  `.agents/skills/the-way-record-glossary-term/SKILL.md` ·
  `.claude/skills/the-way-record-invariant/SKILL.md` ·
  `.agents/skills/the-way-record-invariant/SKILL.md` · `.claude/skills/the-way-refine-task/SKILL.md` ·
  `.agents/skills/the-way-refine-task/SKILL.md`
- **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
  foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
  `foundations/invariants.md:56-65` derived-file-content
- **Model:** cheaper
- **Risk:** none
- **Checks:** each pair byte-identical and equal to what `produce` gives for its path;
  `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 8
  paths of Slice 6; `git diff --stat <base>..HEAD` names these eight paths alone.
- **Depends on:** Slice 4

### Slice 6 — Entry points, last batch, by the generator's command

- **Goal:** the entry points of `review-change`, `settle-technology`, `update-part-map` and
  `write-spec`, in both tools, are written by `python -B agent-instructions/skill_entry_points.py
  --write` (task, *To do* 3), which by now changes these eight paths and no other; every entry point
  of the-way is then what the generator produces.
- **Change:** `.claude/skills/the-way-review-change/SKILL.md` ·
  `.agents/skills/the-way-review-change/SKILL.md` ·
  `.claude/skills/the-way-settle-technology/SKILL.md` ·
  `.agents/skills/the-way-settle-technology/SKILL.md` ·
  `.claude/skills/the-way-update-part-map/SKILL.md` ·
  `.agents/skills/the-way-update-part-map/SKILL.md` · `.claude/skills/the-way-write-spec/SKILL.md` ·
  `.agents/skills/the-way-write-spec/SKILL.md`
- **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
  foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
  `foundations/invariants.md:56-65` derived-file-content
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py` prints `entry points are current`
  and exits 0; `python -B gate/run_tests.py agent-instructions` exits 0;
  `python -B gate/run_tests.py gate` exits 0; `git diff --stat <base>..HEAD` names these eight paths
  alone.
- **Depends on:** Slice 5

### Slice 7 — `make-change` judged and rebuilt after the example

- **Goal:** `task-cycle/change/` holds the layout of the example's section „Po przebudowie”
  (task, *To do* 5): `SKILL.md` with the picture of the whole, step 1 opening with the table of
  variants, rows 5, 9 and 22 of the example's table kept in `SKILL.md` as fragments of one
  instruction, and the common part; beside it `slice.md`, `fix.md` and `ui_check.md` holding what
  the example's table moves to each. The example's table is the starting judgment: confirm or
  correct each of its 22 rows against the skill at the base in the form `judging.md` gives, and a
  departure from the example's layout is named in the report with its reason. Everything else as
  "Common to the rebuild slices" gives.
- **Change:** `task-cycle/change/SKILL.md` · `task-cycle/change/slice.md` ·
  `task-cycle/change/fix.md` · `task-cycle/change/ui_check.md`
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone (Wzór;
  Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation step
  changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
  `foundations/decisions.md:3766-3825` WAY-148 · `foundations/decisions.md:3826-3885` WAY-150 ·
  `foundations/decisions.md:4171-4225` WAY-161 · `foundations/decisions.md:4317-4354` WAY-164 ·
  `foundations/decisions.md:5964-5998` WAY-219 · `foundations/decisions.md:3226-3272` WAY-135 ·
  `foundations/decisions.md:3273-3349` WAY-136 · `foundations/decisions.md:6172-6249` WAY-229 · `foundations/invariants.md:76-85`
  outbound-link-reach · `.runs/the-way-base/instruction-files/SKILL.md` ·
  `.runs/the-way-base/instruction-files/judging.md` ·
  `.runs/the-way-base/instruction-files/kind_skill.md` ·
  `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/skill/SKILL.md:128-196`
  Inputs and authority, handoffs and returns · `task-cycle/skill/SKILL.md:259-364` Execute, verify
  and review · `task-cycle/skill/SKILL.md:366-398` The end of a code review ·
  `task-cycle/skill/SKILL.md:450-464` Correction after review
- **Model:** cheaper
- **Risk:** none
- **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `change`.
- **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 6

### Slice 8 — `write-spec` judged and rebuilt

- **Goal:** `task-cycle/spec/` is judged and rebuilt as "Common to the rebuild slices" gives. Its
  agents are the designer of the spec, the designer after a discarded attempt, and the spec's
  reviewer; the dispatch says which (`task-cycle/spec/SKILL.md:18-19`).
- **Change:** `task-cycle/spec/SKILL.md`, and each file beside it in task-cycle/spec/ that the
  judgment creates, named by the executor
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone (Wzór;
  Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation step
  changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
  `foundations/decisions.md:3226-3272` WAY-135 · `foundations/decisions.md:3766-3825` WAY-148 ·
  `foundations/decisions.md:3826-3885` WAY-150 · `foundations/invariants.md:76-85`
  outbound-link-reach · `.runs/the-way-base/instruction-files/SKILL.md` ·
  `.runs/the-way-base/instruction-files/judging.md` ·
  `.runs/the-way-base/instruction-files/kind_skill.md` ·
  `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/skill/SKILL.md:128-196`
  Inputs and authority, handoffs and returns · `task-cycle/skill/SKILL.md:198-220` Design and
  execution choice, steps 6–7
- **Model:** strongest — each verdict judges whether an agent of the cycle recognises the moment a
  fragment is for, and a wrong "move" switches a rule off without a sign (WAY-128), which the
  sentence comparison cannot catch: design judgment over the skill's layout.
- **Risk:** none
- **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `spec`.
- **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 6

### Slice 9 — `plan-task` judged and rebuilt

- **Goal:** `task-cycle/plan/` is judged and rebuilt as "Common to the rebuild slices" gives. Its
  agent is the planner: of a first plan, of a plan after a reviewed spec, after a one-author attempt
  proved too large, and after a slice proved too large (`task-cycle/plan/SKILL.md:21-27`, `:186-196`).
  The form of the plan in step 3 stays in `SKILL.md` word for word: `task-cycle/slice_size.py:10`
  names `task-cycle/plan/SKILL.md` as its place, and acceptance criterion 1 leaves that script as it
  is.
- **Change:** `task-cycle/plan/SKILL.md`, and each file beside it in task-cycle/plan/ that the
  judgment creates, named by the executor
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone (Wzór;
  Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation step
  changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
  `foundations/decisions.md:3273-3349` WAY-136 · `foundations/decisions.md:3766-3825` WAY-148 ·
  `foundations/decisions.md:3826-3885` WAY-150 · `foundations/decisions.md:6172-6249` WAY-229 ·
  `foundations/invariants.md:76-85` outbound-link-reach ·
  `.runs/the-way-base/instruction-files/SKILL.md` ·
  `.runs/the-way-base/instruction-files/judging.md` ·
  `.runs/the-way-base/instruction-files/kind_skill.md` ·
  `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/slice_size.py:1-45` ·
  `task-cycle/skill/SKILL.md:128-196` Inputs and authority, handoffs and returns ·
  `task-cycle/skill/SKILL.md:198-255` Design and execution choice
- **Model:** strongest — each verdict judges whether an agent of the cycle recognises the moment a
  fragment is for, and a wrong "move" switches a rule off without a sign (WAY-128), which the
  sentence comparison cannot catch: design judgment over the skill's layout.
- **Risk:** none
- **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `plan`; and
  `git diff cf11541 -- task-cycle/plan/SKILL.md` shows no line changed inside the fenced form of
  step 3.
- **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 6

### Slice 10 — `review-change` judged and rebuilt

- **Goal:** `task-cycle/review/` is judged and rebuilt as "Common to the rebuild slices" gives. Its
  agents are the reviewers of a slice, of the whole change, of a fix, of the return step's commits,
  of the reconciliation with the target branch and of a correction after the human's remarks; the
  dispatch says which (`task-cycle/review/SKILL.md:20-23`).
- **Change:** `task-cycle/review/SKILL.md`, and each file beside it in task-cycle/review/ that the
  judgment creates, named by the executor
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone (Wzór;
  Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation step
  changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
  `foundations/decisions.md:3766-3825` WAY-148 · `foundations/decisions.md:3826-3885` WAY-150 ·
  `foundations/decisions.md:4171-4225` WAY-161 · `foundations/decisions.md:4226-4278` WAY-162 ·
  `foundations/decisions.md:4317-4354` WAY-164 · `foundations/decisions.md:5999-6021` WAY-220 ·
  `foundations/decisions.md:6022-6048` WAY-221 · `foundations/decisions.md:4081-4109` WAY-158 ·
  `foundations/decisions.md:4279-4316` WAY-163 ·
  `foundations/invariants.md:76-85` outbound-link-reach ·
  `.runs/the-way-base/instruction-files/SKILL.md` ·
  `.runs/the-way-base/instruction-files/judging.md` ·
  `.runs/the-way-base/instruction-files/kind_skill.md` ·
  `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/skill/SKILL.md:128-196`
  Inputs and authority, handoffs and returns · `task-cycle/skill/SKILL.md:279-364` Execute, verify
  and review, steps 9–11 · `task-cycle/skill/SKILL.md:366-419` The end of a code review; Request
  and handoff, step 12 · `task-cycle/skill/SKILL.md:450-464` Correction after review
- **Model:** strongest — each verdict judges whether an agent of the cycle recognises the moment a
  fragment is for, and a wrong "move" switches a rule off without a sign (WAY-128), which the
  sentence comparison cannot catch: design judgment over the skill's layout.
- **Risk:** none
- **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `review`.
- **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 6

### Slice 11 — `implement-task` judged and rebuilt, with the change of WAY-125 in its handoffs

- **Goal:** `task-cycle/skill/` is judged and rebuilt as "Common to the rebuild slices" gives. Its
  readers are the orchestrator — on each route (spec, one author, plan), with or without a move of
  the pin (step 2), to a request ready or blocked, and in the correction after review — and the
  agents that read a paragraph of it whole: of the foundation step and of the return step. Besides
  the rebuild, and as the only change of meaning (task, *To do* 1; *Foundation entries* row 1):
  step 3 of "Inputs and authority" (`task-cycle/skill/SKILL.md:66-70`) and the handoff paragraph
  (`:128-137`) say that a stage agent reads its method's `SKILL.md` whole and a file beside it when
  the step or variant that names it comes; no handoff tells it to read at the start everything its
  method names. Each handoff names the stage's method by its path and, where the rebuilt stage skill
  opens with a table of variants (Slices 7–10), names the variant in that table's words. The
  carried question on the foundation step (`:259-277`) and the return step (step 11, `:349-364`) is
  answered by judging those fragments like any other, by WAY-256 and WAY-257 — who needs each, at
  which step, and whether that agent recognises the moment — with the answer in the table; the
  handoffs of those two stages then name whatever file or paragraph holds them. The carried
  question on `task-cycle/record_template.md` is answered by one row of the table, judging its place
  only (it is read at step 5); its content is neither judged nor changed, and the report says it
  was not judged. Steps keep their numbers 1–14, since `installation/README.md:82` cites step 2.
- **Change:** `task-cycle/skill/SKILL.md`, and each file beside it in task-cycle/skill/ that the
  judgment creates, named by the executor
- **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:66-69` Questions carried to cycle ·
  `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
  `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:37-37` Ustalone (zmiana
  WAY-125) · `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone
  (Wzór; Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation
  step changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
  `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
  `foundations/decisions.md:387-426` WAY-13 · `foundations/decisions.md:3273-3349` WAY-136 ·
  `foundations/decisions.md:3766-3825` WAY-148 · `foundations/decisions.md:3826-3885` WAY-150 ·
  `foundations/decisions.md:6099-6121` WAY-227 · `foundations/decisions.md:6172-6249` WAY-229 ·
  `foundations/invariants.md:46-55` return-step-record · `foundations/invariants.md:76-85`
  outbound-link-reach · `.runs/the-way-base/instruction-files/SKILL.md` ·
  `.runs/the-way-base/instruction-files/judging.md` ·
  `.runs/the-way-base/instruction-files/kind_skill.md` ·
  `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/change/SKILL.md` ·
  `task-cycle/spec/SKILL.md` · `task-cycle/plan/SKILL.md` · `task-cycle/review/SKILL.md` ·
  `installation/README.md:78-82` · the reports of Slices 7–10 (their tables and layouts), which the
  dispatch names by path
- **Model:** strongest — the orchestrator's skill of 6 605 words is laid out anew: each verdict
  judges whether the orchestrator or a stage agent recognises the moment a fragment is for, and its
  handoffs join the layouts of the four stage skills, so a wrong "move" or a handoff that misnames a
  variant reaches every later cycle — design judgment the sentence comparison cannot check.
- **Risk:** none
- **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `skill`, where
  the lines the sentence comparison prints for step 3 and the handoff paragraph are the change of
  meaning this *Goal* names and nothing else; `grep -n -i "whole" task-cycle/skill/*.md` shows no
  sentence telling a stage agent to read at the start everything its method names; for each stage
  skill whose `SKILL.md` opens with a table of variants, `grep -n` of each variant's words in
  `task-cycle/skill/` shows the handoff that names it; `grep -n -E "^[0-9]+\. " task-cycle/skill/SKILL.md`
  lists steps 1–14 in order.
- **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 7 · Slice 8 ·
  Slice 9 · Slice 10

## Coverage

| What the task requires | Slices or entries |
|---|---|
| *To do* 1 — WAY-125 changed; `implement-task` stops telling stage agents to read at the start everything the method names | Foundation entries row 1 · Slice 11 |
| *To do* 2 — WAY-256 and `instruction-files/kind_skill.md` carry the exception for a one-instruction fragment | Foundation entries row 3 · Slice 1 |
| *To do* 3 — the entry points' sentence, its generator and test, all entry points regenerated by `--write` | Foundation entries row 2 · Slice 2 · Slices 3–5 · Slice 6 (runs `--write`, everything current) |
| *To do* 4 — each of the five skills judged with `maintain-instruction-files` and rebuilt | Slices 7, 8, 9, 10, 11 · Common to the rebuild slices, points 1–6 |
| *To do* 5 — `make-change` in the example's layout, rows 5, 9, 22 kept in `SKILL.md` | Slice 7 |
| *To do* 6 — the request gives each skill's table, the words read per agent and variant before and after, "remove"/"reword" as proposals | Common to the rebuild slices, point 7, in the reports of Slices 7–11; the orchestrator carries them into the request |
| *To do* 7 — the cycle's agents read their stages' methods from the base copy | every handoff of the cycle (orchestrator); Slices 7–11 read `maintain-instruction-files` from `.runs/the-way-base/` (Common, point 1) |
| Acceptance criterion 1 — Python changes only in the generator's sentence and its test's assertion | Slice 2 (its `git diff -- "*.py"` check); Slices 3–6 write no Python; Slice 9 leaves `task-cycle/slice_size.py` as is; Common, point 6 |
| Acceptance criterion 2 — no rule of the five skills disappears or changes meaning beyond *To do* 1–3 | Common to the rebuild slices, points 4, 6 and 8 (the sentence comparison) in Slices 7–11; review of the whole change |
| *Settlements to record* row 1 | Foundation entries row 1 |
| *Settlements to record* row 2 | Foundation entries row 2 |
| *Settlements to record* row 3 | Foundation entries row 3 |
| Findings of the WAY-33 search outside the foundation | `AGENTS.md:9-11` and the generator — Slice 2; `kind_skill.md` — Slice 1; `task-cycle/skill/SKILL.md:66-70`, `:128-137` — Slice 11 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The 42 regenerated entry points are cut into Slice 2 (with the generator) and four batches, Slices 3–6, each at most ten files, written from the generator's own `produce` in process; the last batch runs `--write` | One slice with the generator and all 42 files — the size script reports it too large (45 files against a limit of 10); writing them by hand — they would no longer be the generator's output | Four extra dispatches of the cheaper class; `agent-instructions`' tracked-entry-points test fails between Slices 2 and 6 by design, which an orchestrator could take for a failing check if the slice text is not read |
| The entry-point slices come before the rebuilds | After them — the rebuild slices could not show with `skill_entry_points.py` that no description changed | None beyond the order |
| `AGENTS.md:9-11` is reworded in Slice 2 to the rule of row 2 | Leaving it — the root file every session loads would keep "each reads its skill and the files it names", the reading the task removes from the entry points | One line of the root `AGENTS.md` changes that the task does not name; WAY-128 binds a reworded line, and the review of the whole change judges it |
| The skills are rebuilt in the order `make-change`, `write-spec`, `plan-task`, `review-change`, `implement-task` | `implement-task` first — its handoffs would name the stage skills' layouts before they exist | None: the four stage slices are independent of one another |
| `make-change` on the cheaper class, the other four on the strongest | All five on the cheaper class (WAY-229's default) — a wrong verdict on whether an agent recognises a fragment's moment switches the rule off unseen; all five on the strongest — `make-change`'s table and layout are settled by the example | A judgment slice on the strongest class gets no retry (WAY-229); on this harness `same` and `strongest` are one class (C6) |
| Step 1 matters of `maintain-instruction-files` that concern the repository as a whole are settled in the plan (Common, point 2): tools Claude Code and Codex, no configuration or session-start reading, no search of session records — the ground of each row is the decision or step it carries | Each executor asks, or searches session records — questions the orchestrator would answer the same way, and records outside the repository | A "remove" proposal lacks evidence of a mistake; it is only a proposal in the request |
| The files beside Slices 8–11's skills are named in *Change* as "each file beside it that the judgment creates", without paths | Naming the files in the plan — it would settle the layout the judgment is to find (C3 leaves it to the executor) | The size script counts one changed file for each of those slices; the orchestrator's mechanical check sees the new files as within the described *Change* |
| The form of the plan stays in `task-cycle/plan/SKILL.md` | Letting the judgment move it — `task-cycle/slice_size.py:10` names that file as its place, and the script may not change | None: every use of `plan-task` writes a plan |
| `implement-task` keeps its step numbers 1–14 | Renumbering, with `installation/README.md:82` changed — widens the change to the installation part | The rebuild keeps a numbering a cleaner layout might drop |
| Acceptance criterion 2 is checked by a sentence comparison run as a shell pipeline, not committed | A script or test that checks it — new code the task puts out of scope | It catches a lost or changed sentence, not a fragment moved to a file whose pointer an agent would pass by; that stays with the table and the review of the whole change |
| `implement-task` is one slice | Two slices split between "Start and record" and "Design and execution choice" — the judgment of where a fragment stands needs the picture of the whole skill, and both would change `SKILL.md` | The slice returns too large; its report then says where the size lay, and the split line above is the first candidate |
