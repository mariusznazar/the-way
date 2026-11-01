# Designer's report — guidelines-audit-report

Status: done
Spec: `.runs/task-cycles/guidelines-audit-report/spec.md`

## Questions sent and their answers

None. Every choice of the handoff could be settled from the task, the foundation and the files, each
with a recommendation, so no batch was sent. Three readings a reviewer may want to look at first,
because they are mine and not the task's:

1. Decision 6, that WAY-247 needs no `narrows`: the merging, the order and the top are held to be the
   task's, not a discipline's matter. If the review reads them as a discipline's matter, the entry C
   needs `narrows WAY-247`, and a sentence stating the area (WAY-25).
2. Decision 9, the rule of how far between three and five the top goes. The task allows it and does
   not say it.
3. Decision 8, that the list stands in *Context*, against the word "concise" in the task template, and
   that a *To do* item names a cause by its number, against "keep data needed to make a change in its
   item".

## Ways weighed

The spec keeps, under each decision, each way rejected with its reason and the cost if the chosen way
is wrong. In short:

| Choice | Chosen | Lost |
|---|---|---|
| Words of the scale | `weight`: `grave`, `heavy`, `medium`, `light` | critical/high/medium/low (forbidden word, and the advisory severity of WAY-206); severe/serious/moderate/slight (no order of itself); words of the stake (no readable order) |
| Cost of a fix | `Removes:` and `Reaches:` beside the fix, literal values, no score | hours or points; small/medium/large; a free sentence alone; a ratio |
| Finding and cause | `finding`, `cause`, no entry; `charge` retired | `charge` kept beside `finding`; a new word |
| Rows to entries | six new decisions, WAY-187, WAY-201 and WAY-250 changed in place | one decision; changes of the three alone; rows 3 and 4 joined |
| Shared file | `product-guidelines/audit_end.md`, holding all three audits do alike | the scale alone shared; two files |
| One list | the end runs once, at the end of the audit that runs last | a top for each skill; both step 3 first, always; `refine-task` merging |
| Homes in the document | one list in *Context*; fixes in *To do*; decisions in *Questions to settle* | a new section of the template; a table; two lists |
| Top of the list | the larger of three and the `grave` count, then to five while the weight holds | always five; the agent's judgement |
| Deferred `grave` cause | the skill asks and records; a new section of `guideline_findings.md` holds the route, nothing waiting | the route in the shared file; the prerequisite's paragraph as it stands; the skill writing the backlog |

## The four checks

1. Placeholder, `TBD` or empty section: none found on rereading.
2. Contradictions: three found and fixed. Decision 4 said WAY-201 lost a sentence it does not hold.
   Decision 10 had the extra question put in the same turn as the decision it depends on. Decisions 8
   and 11 disagreed on what `Taken:` names for a boundary's cause. A fourth gap fixed: the spec did
   not say what happens to the two `audit.md` files and `kinds.md`, so decision 5 now does.
3. Several independent changes: no. The shared file, the three disciplines' files, one section of
   `guideline_findings.md` and the entries are one change, and they mean nothing apart. The change is
   wide, 19 files, which bears on step 7's judgement of one author or a plan.
4. Two readings: the range of To do 6 (decision 9), which places To do 5 reaches for a cause given by
   a count (decision 13), a cause taken from below the top (decision 13: no mark, To do 5 reaches the
   top alone), and rows 3 to 5 sharing question 7 (under *Foundation entries*: its ways stand in C).

## Reaches beyond the dispatch

- `agent-instructions/README.md`, whole: the root `AGENTS.md` requires it.
- WAY-19, whole, in `foundations/decisions.md`: how a sentence moves between decisions; WAY-51 and
  WAY-215, whole, for the marked invariant and the prerequisite's route; WAY-186, WAY-248, WAY-249 and
  WAY-219 were read as neighbours of ranges or to see a reference, and bear on nothing.
- `project-level/task/skill/SKILL.md`, `orchestrated_mode.md`, `read_sources.md`,
  `project_plan_task.md`, whole; `project-level/lead/conversation_template.md:100-149`;
  `project-level/lead/skill/SKILL.md:140-217`: what `plan change` does and who writes the backlog.
- `elements/common/way_of_working.md:1-50` for "How a skill asks" and the critique's place;
  `elements/common/critique/SKILL.md`; `elements/common/rules.md`, by search, for language.
- `task-cycle/spec/review.md`, to read the spec as its reviewer will.
- `installation/test_testing_guidelines_installation.py:1-60` and a search of `installation/install.py`:
  that `.the-way` is a whole submodule.
- `.runs/task-cycles/guidelines-audit-report/cycle.md:1-40` and the tail of `base-gate.log`.
- The author's rule on searches, `C:\Storage\The Brain\The Brain\.ai\rules\search.md`, which his
  global instructions require before a claim that something is absent. It is about method and carries
  nothing of the task.

## Searches not found or unclear

- How two skills of one joint task follow each other: neither WAY-247 nor any `SKILL.md` says. Decision
  6 settles it for the list alone.
- `elements/glossary/template.md:50-51` has `TODO — decision pending` on when two uses carry two
  meanings. Decision 3 used the sentence as it stands.
- Whether a weight's word should stand in the task document in English or the human's language: the
  template speaks of headings, status values and markers only. Decision 1 treats it as a marker.
- Whether naming the course and lesson in entry A's *Rationale* is a pointer under WAY-27: the
  verification there speaks of *Origin* and of a rationale resting on what is not said. The spec has it
  named with no address and the pattern described. WAY-256 does the same with no name of the course.
- That "moderate" is an advisory value of common tools is from my general knowledge, not from a source
  read here; it is only a side reason against one rejected way.
- No test reads these files: `git grep` over `*.py` for `product-guidelines` hit only `installation/`,
  each by the path of a `SKILL.md`; the same search for the names of the files beside a skill hit
  nothing. Positive control: `SKILL_SOURCE` and `kinds.md` both hit. The hits were opened.
- `README.md`, `installation/README.md`, `project-level/`, `agent-instructions/`: the only hit for
  `audit` is a Python audit hook in `project-level/test_plan_state_subprocesses_invariant.py`, which is
  no such audit.
- `product-guidelines/template.md` and the three disciplines' `template.md` were not read whole, not
  being named. Searches found no `charge` there, and `audit` only in `coding/template.md`: the audit of
  dependencies, and at lines 227-229 the audit that writes the table of a kind's files, read in place,
  which says nothing of how an audit ends.
