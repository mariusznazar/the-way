## 3. Contradictions between files that load together

None found. Checked: (a) every step names the others by the base's numbers (0 to 7, 7.1 to 7.5),
and every file a pointer names exists (`check_instructions.py` reports no dead path inside
`project-level/skill/`); (b) the opening sentence of `readiness_gate.md` for a dispatched turn says what
`delegated_mode.md` says of step 7 (no direct word to the human, the critique requested through
the conversation, approval written only once recorded through the orchestrator), and nothing more;
(c) the rules moved to "Rules that hold across the steps" no longer stand in the step files, so no
step file gives a second wording of them.

## 4. Proposals that would change the content of a rule

Each is a verdict "remove" or "reword" that the rebuild did not apply, because it changes what the
skill says rather than where it stands (task question 1 and To do 6). A repetition is listed with
its verdict whether or not a change is recommended. At the human's request on request #85
(correction 1), proposals 1, 5 and 6 are applied, and proposal 4 inside this skill only; each says
so under "Applied". Proposals 2 and 3 keep their verdict, keep, and change nothing.

### Proposal 1 - remove the orchestrator's own-edit sentence from the variant's file

Text, base `SKILL.md:36-38`, formerly at the head of the second paragraph of `delegated_mode.md`: "The project orchestrator may make the
initial text edit only when that full text is already before it and needs no other
definition-section or foundation reading; otherwise it delegates the edit."

- Verdict: remove. Needed by the project orchestrator, which holds it in
  `project-level/lead/skill/SKILL.md:206-207` ("You may edit definition text only when its full
  text is already before you and no reading of other definition sections or foundation is needed.
  Otherwise delegate the edit.") and in WAY-156. The agent of the dispatched turn does nothing by
  it: by the time it reads the sentence, the edit has been handed to it.
- Left as it is: every dispatched turn carries 31 words it does not act on, and the rule has three
  wordings (WAY-156, `lead-project`, this file) that a later change can make drift apart; no wrong
  act follows from it today.
- Changed: 31 words fewer in every dispatched turn (routes 3a and 3b). The cost is a review of
  meaning, not of place: a reviewer must confirm that no act of the dispatched agent depends on
  the sentence, and the agent loses the one line that says why the edit reached it. The next
  sentence ("A subagent always performs step 7, including the whole-foundation collision search
  and all checks.") stays: it binds the dispatched agent.
- Recommendation: remove, in a change of its own after this one, so that the rebuild stays a
  change of place only.
- Applied (correction 1): the sentence is gone; the paragraph begins "A subagent always performs
  step 7" (`delegated_mode.md:15`).

### Proposal 2 - the other repetitions between the variant's file and `project-level/lead/skill/SKILL.md:202-219`

| Row | The variant's file (base lines) | `lead-project` | Verdict | Left as it is | Changed |
|---|---|---|---|---|---|
| a | "A subagent always performs step 7, including the whole-foundation collision search and all checks." (base 38-39) | ":207-208 a subagent always performs `define-project` step 7 in delegated mode"; ":209-211 the gate agent performs the whole foundation collision search, checks and corrections" | keep | the dispatched agent knows it may not hand the search back; two wordings of one duty | removing it leaves the agent to infer from `readiness_gate.md` that it runs 7.2 itself |
| b | "the project orchestrator dispatches it and returns observations through files" (base 40) | ":209 You dispatch the gate's independent critique and pass observations back through the files" | keep | the agent knows where the critique's observations arrive | removing it leaves "request the independent critique" with no word on how the result comes back |
| c | "Present the approval material through the project orchestrator and wait for its recorded human approval before writing the fingerprint, gate record and approved Status" (base 43-45) | ":211-212 Present its human approval material yourself and record the human's approval before the gate agent writes approval/fingerprint/record" | keep | each side states its own half of one hand-over | removing it would leave the dispatched agent only `readiness_gate.md`'s opening sentence, which points back to this file |
| d | "Keep the pending gate and next actor visible in the conversation and the definition's actual Status." (base 47-48) | ":202-204 record in the conversation that its gate and subsequent plan recheck are pending" | keep | both write the pending state into the same file, at different times: the orchestrator before the edit, the agent during the turn | removing it leaves the agent's turn without a record of the next actor |
| e | "a fresh plan-project subagent starts at step 0 against this newly approved definition. No task receives `ready for cycle` while that gate or the subsequent plan recheck remains pending" (base 49-51) | ":214-217 dispatch a fresh `plan-project` agent from step 0 ... Keep readiness writes blocked until that recheck ... finish" | keep, or reword the second sentence | the agent writes the next action into the file, so it needs the first sentence; the second binds the orchestrator, and "neither this agent nor the project orchestrator starts task implementation" binds both | a reword to "the next action is a fresh plan-project subagent from step 0" would save about a sentence and lose nothing the agent does; not recommended in this change |

### Proposal 3 - the repetitions between the skill and `project-level/definition_template.md`

The template is read in full at step 0 of every use (task question 1), so a rule of the template
that a step of the skill states again is read twice on every route that reaches that step.

| Row | The skill (base lines, new place) | The template | Verdict | Left as it is | Changed |
|---|---|---|---|---|---|
| a | "Speak the language the human opened in; the definition is written in it, as the template gives." (80; `SKILL.md`, rules) | :31-34, the language of the text | keep | the template says what language the text is in; only the skill says to speak it | removing it leaves the language of the conversation unsaid |
| b | "Find where the product keeps its projects: the `## Backlog` section ..." (94-96; `first_write.md`) | :19-30, the Backlog section | keep | the step says when to look and to ask once; the template gives the form | none worth having |
| c | "`TODO` in every other section but the gate record, which the template gives" (97-99; `first_write.md`) | :351 "Until the gate the section reads `none`" | keep | a pointer, not a second rule | none |
| d | "Background, Success and Risks hold what the human answered: ask for them, as the template gives." (109; `rounds.md`) | :110-112, the same rule (WAY-109) | keep | the step that asks applies the rule where it asks; the template's sentence was read at step 0, before any round | removing it saves one line of step 4 and risks the agent filling Background from the material, the act WAY-109 forbids |
| e | "Never ask for a deadline; the template says how one enters." (118; `rounds.md`) | :117-120 (WAY-110) | keep | as row d | as row d |
| f | "\"Projected foundation changes\" reads `TODO` until then" and "\"Technology\" reads `TODO` until then" (119-122; `rounds.md`) | :104, :152-154, :266-267 | keep | short pointers at the step where the sections are left open | none |
| g | "A new projected decision needs no number and no prefix: ask for none. Keep the identifiers that other projected headings require." (132-133; `find_entries.md`) | :332-333 | keep | "ask for none" is the step's own act, which the template does not give | removing the first half saves a clause; not recommended |
| h | "set the status line to `ready for gate`, as the template gives it" (143; `technology.md`) | :80, the status table | keep | a pointer | none |
| i | "The gate record approves every projected entry; no entry carries a field of approval." (175-176; `readiness_gate.md`) | :335-336, and WAY-118 | keep | the step that writes the gate record carries the rule where it writes | removing it leaves the rule only in the template and the decision |
| j | "A change of the definition after the gate goes through the gate again" (182-183; `SKILL.md`, rules) and "A finding that its fingerprint no longer matches means the definition changed after the gate, and it goes through step 7 again" (62-63; `existing_definition.md`) | :359-362 | keep | the task requires the rule at step 0 and in the dispatched turn (criterion 5) | none |

### Proposal 4 - "the gate" against the glossary

`foundations/glossary.md` defines "gate" as "the one command that runs all of a product's tests".
The skill (and the template, and WAY-118) say "the gate" for the readiness gate: "goes through the
gate again", "the gate record", "Missing independent critique blocks the gate".

- Verdict: not recommended in this change. The same word stands in WAY-118's binding sentences
  and in `definition_template.md`, both outside `project-level/skill/`.
- Left as it is: a reader who takes the glossary's meaning reads "goes through the gate again" as
  "runs the tests again"; in context, after "the readiness gate", no recorded run shows that
  misreading.
- Changed: "the readiness gate" in every place, the decision and the template included, or a
  `Not:` line in the glossary entry naming the readiness gate; either is a change of the
  foundation or of files the task leaves as they are.
- Applied inside this skill only (correction 1): every use of "gate" for the readiness gate in the
  files of `project-level/skill/` reads "the readiness gate" (`SKILL.md:40`;
  `delegated_mode.md:20`, `:24`, `:27`; `existing_definition.md:11`, `:15`;
  `readiness_gate.md:23`, `:24`). Fixed names stay: the heading "Delegated definition change and
  gate" (task To do 2), "gate record" (the template's section), the status `ready for gate` and the
  file name `readiness_gate.md`. WAY-118, `project-level/definition_template.md` and the glossary
  are unchanged, so the skill's words now differ from theirs, as the human accepted.

### Proposal 5 - the path of the template

`SKILL.md:13` and `:45` name `definition_template.md` with no directory; the file lies in
`project-level/`, one directory above the skill, and every other file the skill names now lies
beside it.

- Verdict: reword to `project-level/definition_template.md` (the form
  `project-level/technology/start.md:3` uses).
- Left as it is: an agent may look for the template beside the skill first, as it does for the
  nine files that now stand there, and find nothing; it then finds it in `project-level/`. The base
  had the same name, and `check_instructions.py` reports it on both.
- Changed: two words longer; no rule changes. Proposed rather than applied because the series
  keeps the rebuild to a change of place, and a path written another way is text the reviewer
  would have to weigh.
- Applied (correction 1): `SKILL.md:13` and `:45` name `project-level/definition_template.md`;
  no other file of the skill names the template by a path.

### Proposal 6 - "each skill named below" in the other skills of the series

In this skill the fix of the review's finding M-1 applied it: `SKILL.md:20-21` now reads "each
skill named below or in the files beside this skill is the project skill of that name with the
`the-way-` prefix", and `:14-15` "cited below and in the files beside this skill", since
`find-foundation-entries`, `settle-technology`, `critique` and `plan-project`, and most decisions,
are named in the files beside the skill after the rebuild.

- Verdict: the same reword in `plan-project`, `maintain-styleguide`, `maintain-coding-guidelines`
  and `maintain-testing-guidelines`, which keep "each skill named below" with files beside them;
  outside this task's directory.
- Left as it is: in those skills an agent that reads the skill through an entry point is told the
  prefix by the entry point itself (invariant `skill-entry-points`); one that reads `SKILL.md` by
  its path alone may read "below" narrowly and call a skill named in a file beside it without the
  prefix. The series now words the paragraph two ways.
- Changed: a few words in each of four skills; the meaning of WAY-127's paragraph unchanged.
- Applied (correction 1) in five skills: `elements/common/skill/SKILL.md`,
  `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`,
  `product-guidelines/testing/SKILL.md` and `project-level/plan/skill/SKILL.md`, each of which has
  files beside it that name a skill its `SKILL.md` does not name. Not in `task-cycle/plan/SKILL.md`:
  its one file beside it, `too_large.md`, names no skill, so "below" there is not too narrow.
