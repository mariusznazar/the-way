# Word counts of the six routes

Words are counted as `wc -w` counts them under a UTF-8 locale (`LC_ALL=C.UTF-8 wc -w`): the whitespace-separated tokens of a file, Markdown and frontmatter included. Of a file read by sections, the sections read count, each from its heading to the line before the next heading of the same or a higher level. The state "before" is commit dfd50e5, where `project-level/skill/SKILL.md` is the only file of the skill; the state "after" is the worktree after the last change of a counted file. Every file read beside the skill is the same in both states. `verify_counts.py` beside this file recounts every figure below and in the other reports with counting code of its own.

Rules of the count:

- Skill text is `SKILL.md` and the files beside it that the route reads. Read beside the skill is what question 4 lists: `project-level/definition_template.md` whole (step 0, every route), the section "How a skill asks" of `elements/common/way_of_working.md` (step 0, every route), its section "Reading the foundation" (step 2, route 1 only) and `project-level/lead/conversation_template.md` (routes 3a and 3b). The files of the skills the route calls, the definition and the product's files are outside the count.
- The state "before" has one file for the skill, read whole on every route, so its skill text is the same on every route.
- Route 3a counts `existing_definition.md`: a dispatched turn always works on a definition its conversation file names, and step 0 has that case read the file. The edit itself is counted as question 4 gives route 3a, with no file of another step.
- Route 1 reads neither `existing_definition.md` (no definition is named) nor `delegated_mode.md` (no turn is dispatched).
- Routes 2, 4 and 5 read `existing_definition.md` at step 0 and then the files of the steps they go on to: route 2 steps 5, 6 and 7; route 4 step 7; route 5 steps 6 and 7.
- `readiness_gate.md` counts once on every route. On routes 1, 2 and 5, which pass step 6, a finding of the readiness check at step 6 has it read there, and step 7 does not read it again; without a finding it is read at step 7. Either way the route reads it once.

## The count of the base, and the task's figure

- `project-level/skill/SKILL.md` on the base: 1937 words under a UTF-8 locale, 1929 words with `wc -w` in the C locale, which the Git Bash of this cycle uses while `LANG` is unset. The task's figure is the first. The 8 words between them are standalone em dashes: coreutils 8.32 in the C locale counts no token without a printable ASCII byte, and the file holds 9 em dashes, 8 of them standing alone.
- `project-level/definition_template.md`: 3221 words under a UTF-8 locale (the task's figure), 3190 in the C locale.
- The fragments the task's Need names, on the base:
  - lines 25-51: 314
  - lines 73-125: 540
  - lines 145-183: 495
- Quoted in the proposals of `assessment.md` (proposal 1, removed from `delegated_mode.md` by correction 1):
  - in project-level/skill/SKILL.md before: "The project orchestrator may make the initial text edit only when that full text is already before it and needs no other definition-section or foundation reading; otherwise it delegates the edit.": 31

## The files

### Before

  - project-level/skill/SKILL.md: 1937

### After

  - project-level/skill/SKILL.md: 572
  - project-level/skill/delegated_mode.md: 314
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/idea.md: 82
  - project-level/skill/read_foundation.md: 109
  - project-level/skill/first_write.md: 98
  - project-level/skill/rounds.md: 240
  - project-level/skill/find_entries.md: 108
  - project-level/skill/technology.md: 66
  - project-level/skill/readiness_gate.md: 569

All ten files of the skill after: 2365 words.

### Read beside the skill, the same in both states

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 503
  - project-level/lead/conversation_template.md: 1419

## 1. A definition from an idea, steps 0 to 7

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 3932 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 503

Total of the route: 5869 words.

### After

Skill text, 1844 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/idea.md: 82
  - project-level/skill/read_foundation.md: 109
  - project-level/skill/first_write.md: 98
  - project-level/skill/rounds.md: 240
  - project-level/skill/find_entries.md: 108
  - project-level/skill/technology.md: 66
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 3932 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 503

Total of the route: 5776 words.

## 2. A definition resumed while its entries are found, steps 0, 5, 6, 7

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 5366 words.

### After

Skill text, 1522 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/find_entries.md: 108
  - project-level/skill/technology.md: 66
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 4951 words.

## 3a. A turn lead-project dispatches, the agent reads the delegated mode, step 0 and step 7

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 4848 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - project-level/lead/conversation_template.md: 1419

Total of the route: 6785 words.

### After

Skill text, 1662 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/delegated_mode.md: 314
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 4848 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - project-level/lead/conversation_template.md: 1419

Total of the route: 6510 words.

## 3b. A turn lead-project dispatches, the agent reads every file of the skill

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 4848 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - project-level/lead/conversation_template.md: 1419

Total of the route: 6785 words.

### After

Skill text, 2365 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/delegated_mode.md: 314
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/idea.md: 82
  - project-level/skill/read_foundation.md: 109
  - project-level/skill/first_write.md: 98
  - project-level/skill/rounds.md: 240
  - project-level/skill/find_entries.md: 108
  - project-level/skill/technology.md: 66
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 4848 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208
  - project-level/lead/conversation_template.md: 1419

Total of the route: 7213 words.

## 4. An entry of an approved definition reopened, not dispatched, steps 0 and 7

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 5366 words.

### After

Skill text, 1348 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 4777 words.

## 5. A definition with no Technology section reopened, steps 0, 6, 7

### Before

Skill text, 1937 words:

  - project-level/skill/SKILL.md: 1937

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 5366 words.

### After

Skill text, 1414 words:

  - project-level/skill/SKILL.md: 572
  - project-level/skill/existing_definition.md: 207
  - project-level/skill/technology.md: 66
  - project-level/skill/readiness_gate.md: 569

Read beside the skill, 3429 words:

  - project-level/definition_template.md: 3221
  - elements/common/way_of_working.md section "How a skill asks": 208

Total of the route: 4843 words.

## Summary

| Route | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |
|---|---|---|---|---|---|---|
| 1 | 1937 | 5869 | 1844 | 5776 | -4.8% | -1.6% |
| 2 | 1937 | 5366 | 1522 | 4951 | -21.4% | -7.7% |
| 3a | 1937 | 6785 | 1662 | 6510 | -14.2% | -4.1% |
| 3b | 1937 | 6785 | 2365 | 7213 | +22.1% | +6.3% |
| 4 | 1937 | 5366 | 1348 | 4777 | -30.4% | -11.0% |
| 5 | 1937 | 5366 | 1414 | 4843 | -27.0% | -9.7% |

## The six recorded runs

The task's Context records six runs of the skill: one definition from an idea (route 1), four turns lead-project dispatched (route 3a or 3b) and one entry of an approved definition reopened (route 4). Summed over the six, each dispatched turn counted once by route 3a and once by 3b:

| Reading of the dispatched turns | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |
|---|---|---|---|---|---|---|
| 3a | 11622 | 38375 | 9840 | 36593 | -15.3% | -4.6% |
| 3b | 11622 | 38375 | 12652 | 39405 | +8.9% | +2.7% |

## Against the task's estimates

The task's question 1 estimated the rebuilt skill text by route. Counted, against those estimates (quoted in brackets, not recounted):

- `SKILL.md` alone: 572 words [task: 500-600 words].
- Route 3a, a dispatched turn reading its own steps: 1662 words [task: 1550-1750 words].
- Route 4, an approved definition reopened: 1348 words [task: 1250-1400 words].
- Route 1, a definition from an idea: 1844 words [task: 2350-2550 words]. Only this figure falls outside its estimate, which matches no route counted here, and route 3b, every file of the skill, gives 2365 words.
