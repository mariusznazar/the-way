---
name: write-spec
description: Use to write the spec of a the-way task whose cycle found an open design choice, or to review such a spec as an agent that did not write it — before any plan or code. Questions go to the cycle's orchestrator, never to the human.
---

# Write a spec

Writes, or reviews, the spec of one task for the cycle `implement-task`, which calls for a spec
only where the task leaves an open design choice (WAY-135). The spec settles that choice before a
plan or code is made. The designer and the reviewer are two different agents; the cycle decides
what follows the review. This skill holds only how the spec is written and reviewed.

This skill lives in `task-cycle/spec/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in; in a product, it is the product's pinned `.the-way`.

## 1. Read

- The dispatch: whether you write or review, the open choice the cycle found, the spec path —
  normally `.runs/task-cycles/<task-slug>/spec.md` — and the report path.
- The frozen task document whole: the spec settles a choice of the whole change.
- What the dispatch names, as the orchestrator selected it (WAY-150): of the task's sources, the
  passages it carries or names; of the foundation, the entries by identifier, each whole; and the
  guideline files, each whole (WAY-213).
- After a discarded attempt, the report of the agent that met the choice. Its code is gone; the
  report says where the choice showed and what that agent found.
- The code the choice depends on, as far as needed to see the ways open — read to design, not to
  write.

Where you need something the dispatch does not name — a passage of a source, a decision, an
invariant, the guidelines of a part it did not cover — reach for it selectively: search for its
identifier or a word and read the passage found, a foundation entry whole, never a whole file of
the foundation, and a guideline file whole (WAY-213). Name each such reach in your report — what,
where and why.

## 2. Settle the design

- Restate what the task requires and, apart from it, what you assume. An assumption that changes
  the design is a question.
- Send your questions to the orchestrator in batches, each question with the answer you recommend
  and what a wrong answer would cost. A batch holds every question you can already see; hold none
  back for later. Write each batch into your report, return with the status `questions` and the
  report's path, and wait to be resumed with the answers (WAY-148); when an answer opens a new
  question, return with it in the next batch and name the answer that opened it. Write the spec once
  no question remains. Where no source answers, the orchestrator picks the smallest reversible
  reading that fulfils the task; never ask the human and never widen the task.
- Weigh two or three ways with their costs and recommend one. Leave out every feature the task does
  not need.
- Divide what you design into units that each do one thing, behind an interface that says what the
  unit does, how it is used and what it depends on.

## 3. Write the spec

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

## 4. Review a spec

As the reviewer, read the spec as the agent who has to plan and build from it without talking to
its author, against the frozen task and the foundation entries the dispatch names. Report only
what would make the build go wrong:

- a requirement of the task the spec drops or changes;
- behaviour the spec invents that the task does not ask for;
- a contradiction with the task, the foundation or itself;
- a place where the builder would have to guess and a wrong guess would matter — the question and
  why the answer changes the build.

Skip wording, style and what the spec leaves to the maker. The first line of your report is
`PASS` or `FAIL`; `FAIL` means at least one finding of the list above. For the review of a revised
spec, say for each earlier finding whether it is resolved, and report only what the revision
broke besides.

## 5. Return

The designer writes the spec to its path and the full report to the dispatch's report path: the
questions sent and their answers, the ways weighed and why the rejected ones lost, the result of
the four checks, and each reach beyond the dispatch, and returns with the status `done`. The
reviewer writes its report, each reach included, to its own path and returns its first line. Each
gives the orchestrator its paths, and nothing more (WAY-148). The boundary is the
reviewed spec: return before any plan, slice or code.
