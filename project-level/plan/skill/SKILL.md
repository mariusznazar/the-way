---
name: plan-project
description: Use when an approved project definition of a product that uses the-way has to be broken into tasks — the breakdown that writes the project plan, a plan to resume from its status line, or a plan to check again after its definition passed the readiness gate anew. Not for a task's plan of slices, and never refines a task.
---

# Plan a project

Leads the breakdown: the step after the readiness gate that turns an approved project definition
into its plan — the tasks, what each depends on, which tasks realize and write each projected
entry, and where each open question is resolved. The form of a plan and the rule of each part stand
in `project-level/plan/template.md`; how a skill asks stands in `elements/common/way_of_working.md`;
this skill holds the order of the work. The decisions that set its rules are cited below.

This skill lives in `project-level/plan/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.

The breakdown reads the product's foundation and the definition and writes nothing in either
(WAY-106). It writes no task document; each task is refined later through `refine-task`.

## 0. Start or resume

- Read `project-level/plan/template.md` in full, and the section "How a skill asks" of
  `elements/common/way_of_working.md`.
- When the human names an existing plan, read it whole and run
  `python -B <the-way>/project-level/plan_check.py <plan>`. A plan whose status reads `draft` goes on
  from the first step its sections leave unfinished; a plan handed over changes only as its
  change log records, and a finding that the definition's fingerprint no longer matches means the
  definition changed after its gate: it goes through `define-project` step 7 again, and the plan is
  checked against it from step 1.
- Otherwise begin with step 1.

## 1. Read

- Read the definition whole, and run `python -B <the-way>/project-level/readiness_check.py
  <definition>`; it must report nothing. A finding returns the definition to `define-project`, and
  the breakdown waits.
- Read the product's `foundations/part_map.md`: *Depends on* tells which work has to come first,
  and a task that would touch a part of the highest criticality together with others is a candidate
  to split. Read the decisions the definition's "Touched parts and decisions" names.
- Read the product's files only as far as the cut needs: what is already there, so that no task
  puts in place what exists.

## 2. Cut the tasks

- Cut the definition's In scope into tasks, each ending with something that can be checked in the
  running product, never with a layer put in place (WAY-143). A large task is split; its size
  chooses nothing else (WAY-13).
- Bring a technical element in with the first task that uses it. Write a preparatory task only for
  work that task cannot start without, and make that task depend on it (WAY-143).
- Give each task its number, its name and its goal in the definition's language, the tasks it
  depends on and the items of In scope it delivers, as the template gives them (WAY-147, WAY-144).
  Every task of a new plan reads `to refine`.
- Never write a task the definition's In scope does not ask for. Something the definition leaves
  out that the cut seems to need is a question for the human in step 5.

## 3. Assign the projected entries

- Give every projected entry of the definition its row: the tasks whose work makes it true, and
  the one of them that writes it into the foundation (WAY-142, WAY-126).
- An entry no task of the cut makes true shows a task missing or an entry the project does not
  need; either is a question for the human in step 5, never an entry left without a row.

## 4. Place the open questions

- Write each open question of the definition, word for word, with the place the definition gives
  it, and give it its place in the plan (WAY-142, WAY-145):
  - a question the definition sends to a task goes to the task of the plan the definition's words
    name; where the cut puts it in another task, write a line in the change log giving the reason;
  - a question the definition sends to the breakdown is answered here, by the human or by a quote
    from the definition or the foundation naming where it stands, or goes to a task with a line in
    the change log giving the reason; never answer it from your own reading of the code.
- A move that changes which task writes a projected entry is a question for the human in step 5
  (WAY-145).
- A question that arises only in the breakdown is a question for the human in step 5, and stands
  with `— definition: none` once answered or placed (WAY-145).

## 5. Write, check and ask

- Write the plan in the definition's directory with the status `draft`, the fingerprint
  `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint` prints, and the
  first line of its change log. Give its full path in the same message.
- Run `python -B <the-way>/project-level/plan_check.py <plan>` and fix each finding; it must report
  nothing before the critique.
- Ask the human, in one round, what steps 2–4 left for the human: questions that arose in the
  breakdown, moves that change which task writes an entry, a task or an entry the definition leaves
  unsettled. Write each answer into the plan, with its line in the change log where it changes the
  plan, before the next question.

## 6. The critique

- Run `critique` once on the plan, with the definition and the product's part map as its sources
  (WAY-120, WAY-146). Ask the critic to judge, besides what that skill checks, what no script tells
  apart: whether each task that is not preparatory ends with something checkable in the running
  product, whether each technical element enters with the first task that uses it, whether each
  question stands where the definition puts it or the change log gives its move, and whether a
  quoted answer settles its question. Never ask it what `plan_check.py` decides.
- Verify each observation, give each a verdict, and correct the plan; a correction that changes a
  human's answer, or which task writes an entry, goes back to the human. If an independent critic
  cannot run, say so and wait; the author's own reading does not stand for it.
- Run `plan_check.py` again; it must report nothing.

## 7. Hand over

- Show the human the whole table of tasks, the questions answered or placed in this breakdown, each
  move from the definition's placement with its reason, and each remark of the critique you
  rejected with why. The human corrects the plan; apply each correction, with its line in the change
  log, and run `plan_check.py` again.
- On the human's word, set the status to `handed over YYYY-MM-DD` and add the line to the change
  log. Tell the human that each task is refined next through `refine-task`, as a member of this
  plan, and that a task enters its cycle under its name (WAY-147).
