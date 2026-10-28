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

## 2. Design and write the spec

As the designer, writing the spec or revising it, read `design.md` and follow it: how to settle the
design and send your questions, the form of `spec.md`, the four checks before you return, and what
your report holds.

## 3. Review a spec

As the reviewer of a spec or of its revision, read `review.md` and follow it: what to report, what
to skip, and the first line of your report.

## 4. Return

The designer and the reviewer each give the orchestrator their paths, and nothing more (WAY-148).
The boundary is the reviewed spec: return before any plan, slice or code.
