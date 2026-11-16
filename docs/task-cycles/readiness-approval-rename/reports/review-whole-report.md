PASS 79c9bfb95e772cb21810a78fc42607f99d726da0

# Review of the whole change — readiness-approval-rename

Range: `4758840fbaf9562db960965c706d8681c3d23a43..79c9bfb95e772cb21810a78fc42607f99d726da0`, one
commit (`79c9bfb9`), 59 files, +395 −386, one rename (`project-level/skill/readiness_gate.md` →
`project-level/skill/readiness_approval.md`). `git rev-parse HEAD` in the worktree gives the head
named in the handoff. No spec, no plan, no slices: this review is the only one the change gets.

## Blocking findings (Critical, Important)

none

## Minor findings

All four lie within the task unless they say otherwise.

1. **`process-audit/SKILL.md:124` and `process-audit/audit_count.py:25-26` (module docstring) — "every
   key that holds a key `repository`".** Within the task (To do 9). The rename makes both levels of
   the locations file "key", and this sentence now says "key" for both in one breath. Elsewhere the
   change tells the two apart: `project-level/backlog_place.md:25-31` and `process-audit/SKILL.md:106`
   say "repository key" for the outer level, and the new error message at
   `process-audit/audit_count.py:628` says "no repository named in the locations file holds a key
   `repository`". The sentence is still true, but it reads worse than the rest. Suggested wording:
   "every repository key that holds a key `repository`". Nothing breaks if it stays.

2. **Lines not rewrapped after the rename (about 70 added lines over 104 characters in Markdown and
   Python outside the glossary and the skill descriptions).** Within the task. Examples:
   `foundations/decisions.md:201` (WAY-118), `foundations/decisions.md:3805` (WAY-145 *Verification*),
   `project-level/definition_template.md:338` and `:340`, `project-level/lead/skill/definition_change.md:3`
   and `:14`, `project-level/plan/skill/delegated_mode.md:22`, `project-level/readiness_check.py:290`,
   `project-level/test_plan_check.py:334`. The files around them wrap at about 100 columns. No reader
   reads them wrongly and the linter does not object; the only cost is a larger diff for whoever
   rewraps them later.

3. **No permanent test pins the refusal of the old heading and the old status.** Within the task
   (To do 3 and 4; *Questions to settle* 1, whose way not chosen was "the scripts accept both
   headings"). `project-level/test_readiness_check.py` refuses headings and statuses outside the form
   only through general cases (`test_a_section_outside_the_template_is_reported`,
   `test_a_status_off_its_forms_is_reported`, line 166). A later change that adds `Gate record` to
   `SECTIONS` as an alias, or `ready for gate` to `STATUS`, would pass the suite. My one-off check
   (below) shows the head refuses both today. One case each, "`## Gate record` is reported as no
   section of the template" and "`Status: ready for gate` is reported", would hold the human's choice
   in place. Coverage that would be nice, not a defect.

4. **Outside the task — "entry" in a third meaning, an item of a list in a cycle's record.** To do 10
   says that after items 9 and 10 "entry" means only an entry of the foundation. The tracked text
   still uses "entry" for an item of a record's list: `task-cycle/record_template.md:43`, `:57`, `:59`,
   `:63`, `:74`, `:238`, `:265-266`; `task-cycle/skill/SKILL.md:234`, `:386-387`, `:395-396`, `:754-757`,
   `:768`. The task names only the two meanings that the foundation review found (a key of the
   locations file, a task's line in the backlog), and I found no sentence that is true in one of these
   meanings and false in the other, which is the test of WAY-99. So this is no missed requirement of
   this task. Whether the record's "entry" passes the test of WAY-99 is a question for another task,
   or for the next review of the foundation.

## Declined to judge

- Polish texts, loop2's files and its pin, and the request description for products (To do 6): the
  handoff names them as not mine to grade.
- The general-language "gate" at `foundations/decisions.md:769` ("a gate that stopped every change
  until each of them was held") and `:1958` ("a command per invariant that a gate of its own runs").
  Both read true as the command that runs the tests and say nothing about approving a definition.
  They are not in the moved meaning, so left as they are.
- "read off" at `product-guidelines/styleguide/audit.md:22`, `recognize.md:16` and
  `starting_rules.md:21`, and at WAY-204 (`foundations/decisions.md:9373`). These read a value off
  the product's own code or off a run, which is the glossary's meaning. The author's choice 6 to leave
  them stands.

## Against the task

- **To do 1** — `foundations/glossary.md:77`: *Not* of `gate` names the approval of a project
  definition with the quoted word "readiness approval", which does not hold the term. This is the form
  WAY-99 and `elements/glossary/template.md` give. Met.
- **To do 2** — every use in the projected meaning is renamed: the file name, the section headings
  ("7. The readiness approval", "Delegated definition change and readiness approval", "Change of the
  definition and its readiness approval"), the skill descriptions, the script messages and help text,
  and the decisions (WAY-106, 113, 114, 118, 121, 126, 142, 145, 267, 270, 313, 314, 374). Searches
  (below) find no remaining use of `readiness gate`, `gate record`, `ready for gate`, `readiness_gate`,
  `project-readiness-gate`, `definition gate`, `gated` or a bare "gate" in the moved meaning. Every
  "gate" that is left means the test command, the part `gate` or its directory. Met.
- **To do 3, 4** — `project-level/definition_template.md` holds `## Approval record` and
  `awaiting approval`; `readiness_check.py` (`SECTIONS`, `APPROVAL_RECORD`, `STATUS`) and
  `plan_check.py` (`DEFINITION_NEEDS`, `APPROVAL_FINGERPRINT`) read the new names; the tests use them.
  `ready for approval` is not taken. Met.
- **To do 5** — `foundations/invariants.md:217`, WAY-118 *Verification*, and the seven `# invariant:`
  lines of `project-level/test_readiness_check.py` cite `project-readiness-check`, and the foundation
  check reports 0 errors. Met.
- **To do 7** — `foundations/glossary.md:223-227`, `projected entry`: one sentence that names the kinds
  (decision, invariant, glossary term, environment fact, change to the part map), *Not:* none, in the
  form of `elements/glossary/template.md`; `entry` is unchanged. The kinds agree with the subsections
  in `project-level/definition_template.md:321-331`. The wording keeps the meaning of the answer to
  question 2. Met.
- **To do 8** — `project-level/technology/research.md:28-30` ("take from its documentation … the page
  it was taken from"). The extra rewording in WAY-280's rationale ("a weight taken from the effect")
  is a judgment, false in the glossary's meaning of "read off", so it was right to move it, and its
  meaning stays. Met.
- **To do 9** — `AGENTS.md` `## Backlog`, `project-level/backlog_place.md` (heading "Resolve a key of
  the locations file"), `process-audit/SKILL.md`, the docstrings and messages of `audit_count.py`,
  WAY-27, WAY-107, WAY-320 (binding sentence, *Verification* example, *Rationale*, *Rejected*),
  WAY-330, WAY-344, the row of WAY-342. The code names (`entry_path`, `REGISTER_ENTRY` and the
  others) stay, as the task says. Met.
- **To do 10** — WAY-140 (binding sentence and *Verification*), WAY-147 (*Rationale*),
  `task-cycle/record_template.md:228`, `task-cycle/skill/SKILL.md:89` and `:694`,
  `project-level/test_plan_state.py:248`, `foundation-review/with_the_human.md:40-41`. Met (but see
  Minor 4).
- **To do 11** — `python -B agent-instructions/skill_entry_points.py` prints "entry points are current",
  and the six copies are in the commit. Met.
- **Settlements to record 1–6** — row 1: the `gate` *Not*; row 2: `projected entry`; row 3: the
  template and the two scripts; row 4: the invariant; row 5: WAY-320 "each holding keys by name … names
  its key"; row 6: WAY-140 "the task's line in the backlog". All six are written, none as a second
  entry. The answers under *Questions to settle* are kept word for word: `readiness approval`,
  `approval record`, `awaiting approval`, `project-readiness-check`, `key`, "the task's line in the
  backlog".
- **Meaning of each edited decision.** I read whole every decision whose binding sentence the diff
  touches, and the edits are renames that keep the meaning. Author's choice 3, the first clause of
  WAY-118 ("The readiness gate blocks a definition with …" → "The readiness approval is blocked by …"):
  both say that a definition with any of the listed conditions is not approved and does not reach the
  breakdown. The *Verification* ("the script stops an unfinished candidate table") and the code
  (`readiness_check.py` exit 1) agree with the new wording. Meaning kept. Author's choice 5
  (WAY-227 *Rejected*, "intermediate human gates" → "intermediate human approvals") keeps the rejected
  way and agrees with To do 2's outcome that "gate" no longer means a stop for a human.

## Against the foundation and the guidelines

- **Trust boundary (`readiness_check.py`, `plan_check.py`, `audit_count.py`).** Only names, messages
  and docstrings changed. The rules of reading did not. In `audit_count.py` the duplicate-key check,
  `key_object`, `entry_path`, `the_way_checkout` and `repositories` hold the same logic. My crafted
  input at the head (below): an approved definition with `## Gate record` is refused with exit 1, two
  findings ("`## Gate record` is no section of the template" and "the section `## Approval record` is
  missing"), also under `--before-approval` and `--fingerprint`. `Status: ready for gate` is refused
  with exit 1. A definition holding both headings is refused. A lower-case `## approval record` is
  refused. `plan_check` reports `form` against a definition with the old heading. Nothing accepts the
  old forms by accident, and the fingerprint (from `## Goal` up to the heading, the heading left out)
  does not change for a definition whose heading is renamed, as the task's *Context* says.
- **Changed tests, against "Changing an existing test" (`guidelines/testing.md:95-106`).**
  `process-audit/test_audit_count.py`: three expected substrings (`no entry … under` → `no key …
  under`, lines 832 and 880) and four test names. The cause is on the side of the requirement (To do 9
  names the messages of `audit_count.py`; question 7), and the frozen task is the evidence. The
  assertions are not weakened: the same `assert_refused` and the same strength of substring. Two
  `# decision: WAY-344` lines quote WAY-344 as it now reads, which the foundation check accepts. The
  tests of the readiness and plan checks change only their inputs (heading, status, keyword names) and
  the expected message text of the approval record. Their assertions stay as they were. Conforms.
- **Changed invariant tests (named as section 2 asks).** `project-readiness-check`
  (`project-level/test_readiness_check.py`): `Gaps.test_todo_in_a_section_is_reported_with_its_line`,
  `Gaps.test_todo_in_the_binding_sentence_of_a_projected_entry_is_reported`,
  `Gaps.test_an_empty_section_is_reported`, `OpenQuestions.test_a_question_without_its_place_is_reported`,
  `Candidates.test_a_projected_section_without_the_candidates_line_is_reported`,
  `Candidates.test_a_working_table_still_standing_is_reported_before_approval`: the citation line, and
  in the last one the status and keyword of the input. `project-technology-record`:
  `Technology.test_an_open_choice_is_reported_before_approval` (input only). `project-plan-form`
  (`project-level/test_plan_check.py`): four tests renamed and one keyword renamed, assertions
  unchanged. `project-plan-state-evidence` (`project-level/test_plan_state_invariant.py:492`): the
  non-approved status of the break case is now `awaiting approval`, still a status other than
  `approved`. None of these is weakened.
- **Coding guidelines.** No script grows (sizes below), so the rule of size is not reached. The linter
  test passes in `agent-instructions`. The start and end of `readiness_check.py`, `plan_check.py` and
  `audit_count.py` are unchanged. The file the scripts read keeps the same fields under the new names,
  and WAY-344 holds: a missing `## Approval record` is a finding of the form, exit 1.
- **Reserved choice:** none taken.
- **Glossary entry the change writes** (`projected entry`): content agrees with WAY-106, WAY-118,
  WAY-126 and the template of the definition; form agrees with `elements/glossary/template.md`.

## The author's choices 1–8

1. `readiness_approval.md`: fits the step's heading. No remaining reference to the old name. Accepted.
2. Python names in `project-level/`: nothing outside `project-level/` imports them (searched). This
   follows WAY-97. Accepted.
3. Wording of the bare uses: judged above for WAY-118. "The approval agent" in
   `project-level/lead/skill/definition_change.md:14,16` stands where "the gate agent" stood, with the
   same meaning. Accepted.
4. Messages and tests of `audit_count.py`: judged above. Accepted.
5. WAY-227: judged above. Accepted.
6. `read off`: judged above and under Declined to judge. Accepted.
7. Glossary form: accepted. No entry for "readiness approval" is right by WAY-95.
8. *Context* claim about `task-cycle/skill/foundation_step.md`: confirmed. Neither the base nor the
   head holds a locations-key "entry" there.

**Author's own-work check.** The requirement it names (every use of a moved word rewritten, none of
an unmoved one) is where this change is weakest. Its three-way search would catch a miss, and my own
searches (below) found no use that its check missed. The author's report has no walk through the
running product. The change alters only the text of messages and the names a user writes in a
definition, which the tests and my crafted input cover.

## Structure of the code

`python -B task-cycle/change_file_sizes.py 4758840fbaf9562db960965c706d8681c3d23a43 79c9bfb9`: exit 0.
No Python file changes its line count. The files that grew: `foundations/glossary.md` +6,
`project-level/backlog_place.md` +1, `project-level/lead/conversation_template.md` +1,
`project-level/task/skill/final_review.md` +1. The size invariant `function-and-file-size` is marked
violated, so I ran its test without the mark in worktrees of the base and the head. Both fail (exit 1)
with the same list of functions and files over a threshold, so the change pushes nothing over one.
No code is left without a user. No name stopped being true: the code names that still say "entry"
(`entry_path`, `REGISTER_ENTRY`, `RESULTS_ENTRY`, `REPOSITORY_ENTRY`) stay because the task says so.

## Checks run

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py` (without `--write`) — exit 0, "entry points are
  current".
- `python -B agent-instructions/agent_type_copies.py` — exit 0, "agent type copies are current".
- `python -B task-cycle/change_file_sizes.py 4758840fbaf9562db960965c706d8681c3d23a43 79c9bfb9` —
  exit 0.
- `python -B -m unittest agent-instructions/test_size_invariant.py`, the `expectedFailure` mark taken
  off, in a worktree of the base and one of the head — exit 1 in both, outputs the same but for paths
  and time.
- `python -B .runs/review-whole/crafted.py` (crafted input at `readiness_check.main` and
  `plan_check` through the test helpers: the old heading, the old status, both headings, a lower-case
  heading, the old heading under `--before-approval` and `--fingerprint`) — exit 0; results as in
  "Against the foundation". Kept beside this report as `review-whole-crafted.py` and
  `review-whole-crafted-out.txt`.
- `python -B gate/run_tests.py project-level` — exit 0 (279 tests).
- `python -B gate/run_tests.py process-audit` — exit 0 (276 tests)
- `python -B gate/run_tests.py agent-instructions` — exit 0 (50 tests, 2 expected failures of invariants marked violated, as before)
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests)
- `python -B gate/run_tests.py task-cycle` — exit 0 (534 tests, 2 skipped)
- Manual searches by `git grep` over the tracked files (`.runs/`, and `.claude/`/`.agents/` where
  marked, left out): the old phrases in every form; every line holding `gate`/`gates`/`gated`/`gating`
  outside `gate/` and `gate_`, read one by one where not plainly the test command; `entry`/`entries`
  near `locations`, `backlog`, `task-rules`, `tasks`, `projects`, `problem_register`, `audit_results`,
  `repository`, `.json`, and the forms "entry `", "backlog entr", "task's entry", "entries by name";
  `read off` in every form; `Writes to` in scripts (no script reads the renamed record field);
  grammar left behind by a mechanical rename ("approval approved", "a approval", doubled words) —
  none found.
- Not run: the full gate, as the handoff says; `installation/`, `instruction-files/`,
  `product-guidelines/`, `relation-model/`, `gate/` (no file there changed, and no reference to the
  renamed file or words remains in them).

## Reaches beyond the dispatch

- `elements/glossary/template.md` and `elements/glossary/examples.md`, whole — the form of the glossary
  entry the change writes.
- `foundations/part_map.md`, the entries `project-level`, `task-cycle`, `foundation-review`,
  `process-audit` and the table *External context* — the trust boundaries and the touched parts.
- `foundations/invariants.md`, `project-readiness-check`, `project-technology-record`,
  `function-and-file-size` (*Method* and *Violated*) — the invariants the changed tests cite and the
  rule of size.
- `project-level/plan_state.py`, by search — whether this trust boundary reads the renamed heading or
  status itself (it imports the two checks and reads neither by name).
- `task-cycle/test_remarks_check.py:323`, by search — whether a script reads the renamed field of the
  record (none does).

## Working copies

- `.runs/review-whole/wt-base` and `.runs/review-whole/wt-head`: worktrees of the base and the head
  for the size test. Removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-whole/` itself held the saved diffs, the decision index, the crafted-input script and
  its output, the outputs of the test runs and the sizes table. The script and its output were first
  copied beside this report (`review-whole-crafted.py`, `review-whole-crafted-out.txt`). Then the
  whole directory was removed before return. Nothing remains.

## Unread material

Decisions read whole: 23 of the 199 in the index of my selection (38 listed in full, 161 by heading
alone). These are WAY-27, WAY-54, WAY-95, WAY-97, WAY-99, WAY-107, WAY-113, WAY-114, WAY-118, WAY-121,
WAY-126, WAY-140, WAY-142, WAY-145, WAY-227, WAY-267, WAY-270, WAY-280, WAY-313, WAY-314, WAY-320,
WAY-330 and WAY-374. The index came from `decision_index.py` with the sections "Glossary", "Project
definition", "Private paths and notes" and "Project plan", the parts project-level, process-audit,
glossary, invariants, elements-common, task-cycle, foundation-review, repository, agent-instructions,
decisions and part-map, and the decisions in play and those the diff edits.

Decisions that bear on the change and were not read whole:
- WAY-344 — read its binding sentences in the index and its changed *Verification*, *Rationale* and
  *Rejected* passages in the diff. It is a long entry, and the change renames only "entry" → "key" in
  passages about the key `repository`.
- WAY-106, WAY-134, WAY-147 — binding sentences from the index and the changed passages (*Rejected* or
  *Rationale*) from the diff.
- WAY-34 — binding sentence from the index; the change does not touch it.

Guideline files: `guidelines/coding.md` and `guidelines/testing.md` read whole. The files of kinds of
code that `guidelines/coding.md` names (`coding-check.md` and the others) were not read: the change
adds or alters no rule of a check beyond the names of a section and a status.

## Searches not found or unclear

- The task (To do 9) places "the cited question of WAY-342" in WAY-376. In the head it stands as a row
  of the table under `## Withdrawn identifiers` (`foundations/decisions.md:11156`), not in WAY-376. The
  author's report also says WAY-376. The row is the one changed, so this is only a wrong address.
- The task's *Context* names `task-cycle/skill/foundation_step.md` among the files with a
  locations-key "entry". Neither the base nor the head holds one there.
