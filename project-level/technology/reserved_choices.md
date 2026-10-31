# Reserved choices

Which technology choices the human settles at the step `settle-technology` and which the agent that
meets them makes itself (WAY-266). Read it when the work needs a language, a framework, a library, a
store of data, a way of logging in or a place to run that the task, the spec and the foundation do
not settle. The rule says only what stops a task on its own: a human may run the step for any
choice (WAY-265).

## The rule

- **The test.** A choice is under the rule when settling it later could change how the work is cut
  into tasks, or when it adds something the product has to run, pay for or back up (WAY-121). A
  choice one task can make and change alone is not.
- **Reserved.** A choice under the rule is a reserved choice when no decision of the foundation, no
  approved definition the task carries and no accepted answer of the task document settles it. One
  of these that settles it makes the choice no reserved choice.
- **Where it goes.** Refinement that sees a reserved choice runs `settle-technology` at the task
  document, which is not ready until the human has settled it. In a task's cycle no agent settles
  one, the orchestrator included: the agent that meets it returns the status `reserved` and a
  report with no code, as the method it follows gives.
- **Everything else stays where it is.** A choice not under the rule stays in the cycle: the agent
  that meets it makes it and enters it in the cycle record's questions table. The tools the skills
  of guidelines choose stay on those skills' routes. A missing way to the running product alone
  does not stop a cycle (WAY-219).

## Examples

| Choice | Where it goes |
|---|---|
| a store of data, an error tracker, a framework the product's code is written against, a way of logging in, a place to run | stops: reserved |
| a small library for formatting dates, a test double used only by tests, an override of one dependency | stays with the task |
| a source of icons that adds no fee and that one task can change alone | stays with the task |
| a source of icons that adds something to pay for | stops: reserved |
| a linter, a test tool, a component library chosen by a guidelines skill | stays on that skill's route |

## The boundary

A choice is under the rule or it is not; a choice an agent cannot place is no third kind and
stops nothing on doubt alone. The boundary rests on the agent's judgment, helped by the examples
above, and a choice judged not under the rule stays in the cycle and enters the questions table.
