# Findings to fix — review of the whole change `2754675..c0a0f52`

The review's first line: `FAIL c0a0f5271cf251055b1ec50f32087220da328698` (report:
`.runs/task-cycles/define-project-skill-shape/reports/review_report.md`). Below, in the reviewer's
words, its one blocking finding and, after it, its three Minor findings within the task. None is
marked outside the task's scope. Fix them in one fix; answer with evidence a finding you hold wrong.

## Blocking

**I-1. A readiness-check finding handed back to `define-project` from step 6 no longer finds where
to go — 7.1's routing now stands only in `gate.md`, which step 6 does not name.**

- Place: `project-level/skill/technology.md:7-9` (step 6) with `project-level/skill/gate.md:11-16`
  (7.1); the caller is `project-level/technology/close.md:6-11`, unchanged.
- What is wrong: step 6 runs `settle-technology`. Its last step, `close.md`, runs
  `readiness_check.py <definition> --before-approval` and says: "any other finding goes back to
  `define-project`, which names where." The only place `define-project` names where a finding of
  that check goes is 7.1 ("A finding of condition f goes back to step 5; a finding of condition g,
  or of condition a in "Technology", goes back to step 6; ... any other finding goes back to step
  4"). In the base, 7.1 stood in the one `SKILL.md` the agent had read whole, so the hand-back from
  step 6 found it. After the rebuild, 7.1 stands in `gate.md`, which `SKILL.md` names only at step
  7 and which the agent reads only "once ... reports nothing ... step 7 begins"
  (`technology.md:7-9`). `technology.md` itself names no file for a finding; `SKILL.md` step 6
  holds only "Read `technology.md` beside this skill." So on routes 1, 2 and 5, which all pass step
  6, an agent returned with a finding of condition f, or a `TODO` left in another section, holds no
  text that "names where": it can only guess, or open `gate.md` early on its own initiative. The
  same holds for a finding of `technology.md`'s own run of the check, which the base answered from
  the same 7.1.
- Why it matters: task acceptance criterion 1 ("Żadna reguła nie znika ... każdy fragment stoi po
  przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest
  potrzebny"), criterion 2 (a rewritten pointer must lose no route) and criterion 5 (a fragment
  several steps need reaches each of them). WAY-256 places text that some steps consult "in a file
  beside the skill that each of those steps names, a step after the first having that file read
  unless an earlier step did"; its *Verification* names as a violation "a rule of working that
  three steps keep stands only in the file of the first, so the other two never reach it". 7.1's
  routing is consulted at step 6 (through `close.md`'s hand-back) and at step 7; only step 7 names
  its file. The author's criterion-5 table and route walk (author report, "Walk of routes 1, 3a, 4
  and 5": route 1 "`technology.md` -> `gate.md`", route 5 "`technology.md` -> `gate.md`") pass over
  this hand-back, and the assessment's row for `L137` lists `close.md:10-11` as a caller without
  checking that "which names where" still resolves.
- Evidence: `grep -rn "define-project" project-level/technology/` gives `close.md:10` "`define-project`,
  which names where" and `close.md:11`; `grep -n "step 4\|step 5\|condition" project-level/skill/technology.md`
  finds nothing; `check_pointers.py` checks the jumps of `gate.md` and `existing_definition.md`
  only, so it passes. Manual walk of routes 1, 2 and 5 below.
- What would close it (the author's choice): have step 6 name 7.1's routing where a finding
  arises — e.g. in `technology.md`, "a finding goes where 7.1 sends it (`gate.md` beside this
  file)" — with `SKILL.md` step 6 naming `gate.md` for that case if it is read as a variant there,
  and step 7's pointer not having it read again where step 6 did (WAY-256). The new sentence would
  have to say what it switches off (criterion 2).

## Minor (within the task)

**M-1. "each skill named below" and "The decisions that set its rules are cited below" now reach
into the files beside the skill.** `project-level/skill/SKILL.md:14` and `:19-20`. After the
rebuild `critique`, `find-foundation-entries`, `settle-technology` and `plan-project` are named
only in `gate.md`, `find_entries.md`, `technology.md`, and most decisions are cited there too. An
agent reading `SKILL.md` by path with no entry file (criterion 3's reader) may read "below"
narrowly and call `critique` without the `the-way-` prefix; an entry point covers it ("Where this
skill or a file it reads names another the-way skill"). The author raises the first as proposal 6
of `assessment.md` (series-wide reword); I agree it is not blocking: within the task, Minor.

**M-2. `delegated_mode.md` has no orientation line, and its "this same workflow" now points out of
its own file.** `project-level/skill/delegated_mode.md:1-5`. Every step file opens with "Step N of
the skill `define-project`, whose `SKILL.md` lies beside this file"; the variant file of the
delegated mode does not, and its moved sentence "use this same workflow with file-mediated
routing" no longer stands beside the workflow it means. A reader handed the file alone (the
orchestrators' dispatches name the section, and a critic or orchestrator may be handed the file)
must infer which workflow. The plan-project precedent (`project-level/plan/skill/delegated_mode.md`)
has the same gap. Within the task (criterion 3), Minor: the agent arriving by the pointer in
`SKILL.md` already knows.

**M-3. One line over the file's wrap width.** `project-level/skill/existing_definition.md:6` is 103
characters; every other prose line of the ten files wraps at 100 (only the frontmatter
`description` at `SKILL.md:3` is longer, as on the base). Polish, within the task.
