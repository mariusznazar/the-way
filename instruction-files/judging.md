# Judging instruction files

How the skill judges the files under review, in the mode judge.

## The judgement

Before the table, search the records the human can open — the tools' session records, the
repository's history, review remarks — for the mistakes the fragments are kept or proposed for, the
way step 1 searches session records; ask where the records are when it is not stated.

Output, in this order:

1. The check script's errors and warnings, each with what it means in each tool in use, and its
   `info` lines that say something was not read or not checked.
2. A table with one row per fragment of every file: the quoted fragment with `file:line`, the
   verdict — keep, move, remove or reword — the criterion it stands on, its reason and its ground
   (WAY-257). The criterion, in every row whatever the verdict: when an agent needs the rule and
   whether an agent recognises that moment when it comes, so that the human can disagree with the
   criterion and not only with the verdict. The reason: for keep, the conditions the fragment
   meets — for a line of the main file, the three conditions; for move, the target; for remove,
   the condition that fails or the defect below; for reword, the new wording. The ground: a
   **mistake**, with where it was seen — a session record, a commit, a review remark — or "not
   found in <what was searched>"; or a **cost**, the context the fragment takes in every session,
   with what it saves; or a **carried decision or step**, the decision the repository records or
   the step of an activity that the file leads, named.
3. Contradictions between files that load together.

The table is a batch of decisions; edit nothing until it is accepted.

A proposal to add or reword a rule, or to add a mechanism, is recommended only where "When to add
a rule" lets the rule in; one it does not is listed as not recommended, with the search named. A
verdict to keep, move or remove a rule may rest on a stated cost. Removals are proposed as "When to
remove a rule" below gives.

In a product that uses the-way, the proposals leave out the root `CLAUDE.md` the installer creates,
the block of `AGENTS.md` between `<!-- the-way:begin -->` and `<!-- the-way:end -->`, and the entry points
`.claude/skills/the-way-*` and `.agents/skills/the-way-*` that the-way's installer writes. Where
they differ from the layout the skill gives, the output says so in a note on the installer after
the table, never as a row to apply.

## Typical defects

Besides a breach of a rule of this skill:

- a file swollen with content most sessions do not need;
- a file generated at the start of a project and never changed, though the code changed;
- two instructions that contradict each other.

A catalogue of configuration smells of instruction files, drawn from grey literature and from
mining and measured on popular open-source repositories, stands at
https://arxiv.org/abs/2606.15828v5.

## In operation — fresh sessions with the rule and without it

Judging in operation is three separate questions, each with a different cost (WAY-131):

| Question | How to settle it | How many sessions |
|---|---|---|
| **did the rule load** | a marker in the file and evidence from the tool: the `InstructionsLoaded` hook in Claude Code, `codex --ask-for-approval never "Summarize the current instructions."`, a list of markers in Cursor — always with a positive control, a file that must load | one per variant |
| **did the agent follow it** | the trace of behaviour the rule describes | a few, when without the rule the behaviour never happens; dozens to over a hundred, when it happens sometimes and the rule should only make it more frequent |
| **did it help** | whether the mistake the rule was meant to remove stopped coming back | not from test sessions — from watching the work over time |

- **A rule that loaded but was not followed is a different defect from a rule that did not load.**
  The first needs a change of wording or a move into a mechanism "Where a rule stands" gives; the
  second, a change of carrier.
- **Comparing three sessions with the rule and three without it settles only the first case of the
  second question.** When the behaviour happens without the rule too, such a sample cannot tell the
  rule's effect from the ordinary variation between runs (fact `agent-run-variance`).
- **The model and the tool's version are the same in both variants,** and a result from one model
  is not carried over to another.

## When to remove a rule

- the agent does it right without the rule (a rule added for a mistake) — settled by a removal
  test: the rule goes, and watching the work shows whether the mistake comes back;
- a mechanism enforces it — the rule goes or turns into a check;
- it can be read from the repository;
- it points to a path, skill or command that does not exist;
- it was added for a mistake that can no longer be named — it is proposed for removal; when the
  mistake is named but may no longer happen, it is proposed as a removal test. A rule that carries
  a decision or a step leaves by the way out "When to add a rule" gives it, not by this test.

A long absence of the mistake does not prove the rule is unnecessary — it may mean the rule works.
A removal test settles it, not the calendar.

## Mechanisms that clean up

- **Size over time:** a file that grows while what it covers does not is accretion; the signal is
  available without reading.
- **A review after a change of model, not by the calendar:** rules written for an older model are
  sometimes unnecessary or too tight for a new one; each rule with a trace then goes through a
  removal test.
- **A review of sessions tells the two defects of judging in operation apart,** and shows
  contradictions between layers — the global file, the repository's file, a skill and a request —
  that no file shows on its own.
- **A step after a task that asks whether the instruction files should change has two outcomes:
  adding and withdrawing.** A loop that can only add reproduces accretion; withdrawing is an equal
  outcome of it.
- **An instruction asking an agent for a fix carries the rule on changing a rule and asks it,
  where it adds a sentence, to name the sentence that becomes unnecessary.**
