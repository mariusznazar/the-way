# Findings of the review of the whole change (`whole-change-review-report.md`, `FAIL 9c66ee1`), for the fix

Blocking, in the reviewer's words:

### Important (blocking; within the task; the change is one commit, no plan, so no slice)

**I-1. The new entry and the new text of the skill tell a different thing about an ambiguity of the approved
project definition (WAY-263).**

- Place: `foundations/decisions.md:12895-12896` (WAY-374, second paragraph: "an ambiguity in the approved
  project definition goes back to the definition and its readiness gate (WAY-118)") against
  `project-level/task/skill/resolve_gaps.md:24-25` ("Where the word stands in the approved project definition
  and the answer would change it, the paragraph below on that definition applies").
- What is wrong: the binding sentence of the entry sends every ambiguity of the definition back to the
  definition and its gate, without a condition. The skill sends it there only where the human's answer would
  change the definition, and that is what the paragraph it points to says (`resolve_gaps.md:40-41`: "If the
  answer changes the approved project definition or a projected decision of it, route that change"). The
  entry's sentence is the broader one, and WAY-118, which it cites, makes a pass through the gate follow a
  change ("A change to those sections after approval goes through the gate again"), not an ambiguity. The task
  Q1 answer says "jak dziś daje krok „Resolve the gaps”", i.e. the conditional form; the entry dropped the
  condition while the skill kept it.
- Why it matters: WAY-263 grades a change whose files restate an entry it writes differently, more broadly or
  without a qualification, as Important. An agent comparing the skill with the entry finds a departure; an
  agent following the entry alone may stop and send a task back to the definition for a word it would have
  asked about and settled under *Questions to settle* with the definition's text untouched, which is the cost
  WAY-118 does not impose. It also leaves open whether the word of the definition is asked about at all.
- Evidence: the two quoted passages above; WAY-118 read whole at `foundations/decisions.md:3017-3051`.
- Fix proposed: bring one side to the other in the same words, most simply the entry: "an ambiguity in the
  approved project definition whose resolution changes the definition goes back to the definition and its
  readiness gate (WAY-118)", leaving the skill as it stands.

Minor findings within the task, in the reviewer's words (fixed in the same round, WAY-161):

### Minor (within the task)

- **M-1.** `project-level/task/skill/SKILL.md:42-43` — the inserted words left line 43 at 142 characters
  (the rest of the file wraps at about 100) because the paragraph was not re-wrapped. Re-wrap the paragraph.
- **M-2.** `foundations/decisions.md:12880`, `12883`, `12884`, `12936`, `12939`
  (lines of 102-112 characters among neighbours wrapped at 100): the new entry is not wrapped as the entries
  around it are. Polish only.
- **M-3.** `foundations/decisions.md:12926` (*Rationale*): "the standard WAY-99 sets for a word of the
  foundation". WAY-99's standard is that a sentence the files hold is true in one meaning and false in the
  other; the entry's standard is that a sentence allows both readings and the readings give different
  observable results in the task's scope. They are alike in kind (a sentence standing in the files, none made
  up), not the same standard. The words "after the model of" would say what the task's *Context* says ("bierze
  wzór z testu WAY-99").
- **M-4.** `foundations/decisions.md:12894-12895` and `project-level/task/skill/resolve_gaps.md:21-23` — the
  candidate-for-the-glossary sentence says "a meaning ... a reader who knows the product's field would not
  give the word". WAY-95 adds a qualification for a narrower meaning (an entry only where a reader of the field
  would read a sentence wrongly). The route is a candidate that WAY-95 then judges at the table of settlements
  (WAY-134), and the wording is the task's own (Q4), so nothing is lost, but one clause "(WAY-95 judges it
  there)" would remove the question. Graded Minor because the sentence names WAY-95 and says "candidate".
- **M-5.** `project-level/task/skill/resolve_gaps.md:10-25` — the new paragraph is one block of eight sentences;
  To do 3 asks for the question "według „How a skill asks”" and the paragraph says only "as a question of
  decision" without naming the section (the entry names WAY-113). A reader of the skill alone finds the way
  through "question of decision", which the shared file defines; naming it would match the task word for word.
