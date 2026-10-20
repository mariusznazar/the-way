---
name: critique
description: Use when an agent's proposal needs an independent critical reading, when a complete set of proposals will be reviewed together by a human, or when a change to an invariant test or to the foundation needs its independent assessment. Checks purpose, evidence, cost, source fidelity and contradictions before the author gives a verdict.
---

# Critique a proposal

Use this skill to challenge a proposal whether or not the human has expressed doubt. A proposal
may be one entry, document or process change, or a complete set that the human will review
together. This skill advises; it does not approve a proposal or change a human settlement.

## When to use a fresh critic

An agent or the human may invoke an independent critique of any proposal. Invoke it automatically
when the author has finished a set of proposals that the human will review collectively. In either
case use one fresh agent as a second reader. For a set, start after it is complete, including
proposals added as consequences of earlier ones, and before presenting it to the human.
One critic reads the whole set, not one proposal at a time.
For a change to an invariant test or to the foundation, this critique is the change's independent
assessment (WAY-10). Run it on a model other than the author's where one is available. Give it the
diff and the files of the assessed commit — never the task's chronicle or the author's reasoning
— commit messages included: name the assessed commits by hash only — and ask it to name what of
the change can be cut, or that nothing can. In the task cycle its full
report and the author's settlement go in the cycle record's `reports/`; outside the cycle, the
assessment and the settlement of each remark go in short in the message of the commit that carries
the change.

If a fresh agent cannot be started without the author's conversation context, say so and perform
the same checks yourself as interim work. Do not describe that as an independent review. A set
intended for collective human review must then wait for an independent critic.

## Give the critic the material

Give the fresh agent the complete proposal or set, its intended moment of use, the full relevant
sources and applicable rules, and the target file or directory. Ask it to read the target in full
and inspect the history of an existing knowledge rule before proposing another layer. Do not give
it the author's defense or a preferred verdict. Ask for each observation to name what it checked,
where the evidence stands and what would have to change. Ask it to state explicitly when a check
finds no concern. The critic reports observations; the author makes the verdict.

## Check independently

The author and critic each ask:

1. Who benefits, and at what moment would the proposal act? Would it act in the case that prompted
   it?
2. How often has the problem occurred? Measure from available cases or records where possible;
   distinguish real cases from mentions. If it cannot be measured, say so. A future case with a
   concrete recorded example still deserves review even when past frequency is zero.
3. What error might the proposed rule or tool create when applied too widely? Does it repair the
   original problem or move it elsewhere?
4. Is there a cheaper way to achieve the same effect, including an existing rule, a check, a
   template change or a conversation at the point of use? Count the cost of running and maintaining
   the proposal, not only the cost of writing it.

For a change to instructions, a rule, a playbook or another knowledge file, read the whole target,
find when the existing rule entered, and check whether the problem recurred after that rule began
to apply. A recently added rule is a reason to seek evidence before adding another layer.
For a claim about agent behavior, search available session transcripts or run logs, report the
period and count examined, separate true cases from mentions, and give dated examples. If no such
records are accessible, name what you tried; never replace the measurement with an estimate.

For a proposal derived from sources, also check every substantive claim against its source; name
missing answers rather than completing them from memory. For a set, check each item against its
required form and compare items with one another for contradictions and duplicated or missing
settlements. Automated format checks may help, but they do not establish fidelity to a source.

## Settle the review

Verify each observation against the source, target and the human's settled answers. State what
you accept, reject or could not verify. Never silently change a human settlement because a critic
disagrees with it; take the conflict back to the human with the relevant text. Give one explicit
verdict: apply, rewrite (with the full revised wording), or reject. Show the human the corrected
proposal and any remaining open questions. The critic does not write files; the workflow that
called this skill makes accepted changes.
