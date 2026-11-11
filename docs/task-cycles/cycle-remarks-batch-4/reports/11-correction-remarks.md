# The human's remarks on request #97 (2026-11-11, in the session that ran the cycle)

The remarks bind. They are recorded here from the conversation, in their substance; the orchestrator
adds no wish of its own.

## R1. Two improvements of the first group, made in this request

The human asked to make only the first group (of the three the orchestrator had sorted the request's
remaining points into) and said the second topic would not be a separate task. The first group:

1. Add the part `task-cycle` to the *Scope* of the decision WAY-71 (the decision now governs what a
   request shows the human, so a cycle that selects decisions by that part must find it).
2. Put the rule "where the gate fails and its fix changes code, the return step compares that fix's
   range too" into the *violates* example of WAY-160 (not into its *complies* sentence, which the task
   gives word for word).

## R2. `TODO` in *Based on* and *Derives from*: route B, done in this task

The human asked whether this can be done properly in this task, "also what would enter a small
separate task", and, asked "Do you choose route B, including rejecting `TODO` in *Relations* and
*Origin*? If so I release one correction: the two things of group 1 plus this", answered "tak".
Route B, as put to the human:

- The same descriptive form in all three fields where something an entry stands on is missing:
  an invariant's *Rests on*, a decision's *Based on*, an invariant's *Derives from*;
  form `TODO — <what is missing, with its source>`; a bare `TODO` in none of them passes.
- The request shows the human each such gap (item 15 of `request_template.md` covers all three fields).
- Decisions: WAY-71 — the sentence of the task's To do 6 extended to the three fields; WAY-287 — the same
  change; the *complies* example `Based on: TODO — <what is missing>` of WAY-71 stays and becomes true.
- `elements/common/rules.md`: the same extended sentence.
- Templates: the decision template gets the form for *Based on* (the invariants template already has it
  for *Derives from*).
- `elements/common/foundation_check.py`: reads *Based on* and *Derives from* in whole when the value
  begins with `TODO`, as it already does for *Rests on*, rejects a bare `TODO` in each with a hint, and
  rejects `TODO` in the fields where the rule does not allow it (*Relations*, *Origin*), so that the
  script says what the rule says. The-way and loop2 hold no such entry, so nothing there fails.
- Tests for each of these changes.

The reason the human accepted for *Rests on* (a cycle would stop to write a fact outside its task) is
the reason the other two fields get the same form.

## R3. What does not change

Everything the first correction round settled stands: item 15 covers every such gap on the tree after
the change, the order of the gate and the other items of the task.
