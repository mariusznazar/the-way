# Designing a spec

What the designer of a spec does after reading: settles the design, writes `spec.md`, checks it and
returns.

## Settle the design

- Restate what the task requires and, apart from it, what you assume. An assumption that changes
  the design is a question.
- Send your questions to the orchestrator in batches, each question with the answer you recommend
  and what a wrong answer would cost. A batch holds every question you can already see; hold none
  back for later. Write each batch into your report, return with the status `questions` and the
  report's path, and wait to be resumed with the answers (WAY-148); when an answer opens a new
  question, return with it in the next batch and name the answer that opened it. Write the spec once
  no question remains. Where no source answers, the orchestrator picks the smallest reversible
  reading that fulfils the task, except for a reserved choice; never ask the human and never widen
  the task.
- Where the design needs a language, a framework, a library, a store of data, a way of logging in
  or a place to run that the task and the foundation do not settle, read
  `project-level/technology/reserved_choices.md` (in a product,
  `.the-way/project-level/technology/reserved_choices.md`) and follow it. A reserved choice is
  settled by no answer and no smallest reversible reading: write no spec and return the status
  `reserved`, with a report that holds the choice, where it shows, the limb of the rule that
  reserves it, what you searched and the ways you saw.
- Weigh two or three ways with their costs and recommend one. Leave out every feature the task does
  not need.
- Divide what you design into units that each do one thing, behind an interface that says what the
  unit does, how it is used and what it depends on.

## Write the spec

Write `spec.md` in this form:

```markdown
# Spec — <task title>

- Task: <path of the frozen task>
- Open choice: <the choice this spec settles>

## Intent
## Goals and non-goals
## Constraints
## Decisions
## Foundation entries
## Left to the maker
```

- *Intent* — what the change is for, in a few sentences.
- *Goals and non-goals* — what the change achieves, and what it deliberately does not.
- *Constraints* — what binds the design: the task, the foundation, the code as it stands.
- *Decisions* — each choice the spec settles, with the ways rejected and the cost if it is wrong;
  the units and their interfaces where the design adds them.
- *Foundation entries* — each entry the change will write or change, named with its kind and its
  meaning in one sentence; the foundation step or the return step words them.
- *Left to the maker* — what the plan or the change's author decides.

No code: no function body, no test body, no text a file will hold. Name what is to exist and what
it is to do.

Before you return, read the spec again for four things and fix what you find:

1. a placeholder, a `TBD` or a section left empty;
2. two sections that contradict each other, or a decision the task or the foundation contradicts;
3. a scope that is really several independent changes — say so in the report;
4. a requirement that can be read two ways — pick one and write it down.

## Return

The designer writes the spec to its path and the full report to the dispatch's report path: the
questions sent and their answers, the ways weighed and why the rejected ones lost, the result of
the four checks, each reach beyond the dispatch, and **Searches not found or unclear:** each thing
it looked for and did not find or that was unclear — in the instructions, handoff, task, foundation
or product code — or `none`; it returns with the status `done`, or `reserved` as above.
