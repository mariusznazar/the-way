---
name: critique
description: Use when an agent's proposal needs an independent critical reading, when a complete set of proposals will be reviewed together by a human, or when a proposal derived from sources has to be checked against them. Checks purpose, evidence, cost, source fidelity and contradictions before the author gives a verdict.
---

# Critique a proposal

Use this skill to challenge a proposal whether or not the human has expressed doubt. A proposal
may be one entry, document or process change, or a complete set that the human will review
together. This skill advises; it does not approve a proposal or change a human settlement.
The critic does not write files; the workflow that called this skill makes accepted changes.

## When to use a fresh critic

An agent or the human may invoke an independent critique of any proposal. Invoke it automatically
when the author has finished a set of proposals that the human will review collectively. In either
case use one fresh agent as a second reader. For a set, start after it is complete, including
proposals added as consequences of earlier ones, and before presenting it to the human.
One critic reads the whole set, not one proposal at a time.
The diff of a change to an invariant test or to the foundation takes no critique of its own: the
review of the change by an agent that did not make it reads it, and the human reads it at the merge
(WAY-10).

When invoking a critique, read `prepare.md` beside this skill to start a fresh critic and
handle the case where none is available.

## Give the critic the material

When giving the critic its material, follow `prepare.md` beside this skill.

## Check independently

At the independent check, the author and the critic each read `check.md` beside this skill.

## Settle the review

When settling the review, the author reads `settle.md` beside this skill.
