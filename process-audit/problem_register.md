# Register of problems

This is the template of the register of problems that the audit of the process reads (WAY-330).
Copy it to a place of your own, adapt it to your needs, and let your own tool fill it.

## How the register is kept

- The register lies at a place on your disk outside every repository, which an entry under
  `the-way` in your locations file, `~/.the-way/locations.json`, names (WAY-320). It never lies in a
  repository: it carries the names of your products and what their cycles reported.
- Your own tool fills it: a review of the reports of your cycles, made by an agent or by hand. The
  audit reads the register and gives no problem a class, a weight or a cost of an occurrence itself
  (WAY-330); the one change a session of the audit makes in it is a class added to *Classes*, on
  your yes.
- You adapt the template to your needs: the meaning of a class, the list of classes, the words of
  this text. What the counting command of the audit reads keeps the form the next section gives.
- A problem is a lapse that the process let through in one cycle. A problem that several stages of
  one cycle report is one problem: one row, which names every stage that reported it (WAY-334).
- An issue is the one matter that like problems of several cycles make: the problems that one fix of
  the process would remove belong to one issue.
- A problem has a weight and, apart from it, a cost of an occurrence. The weight says how far the
  problem endangered the change; the cost of an occurrence says what one occurrence of it cost, on
  the five levels of *Costs of an occurrence* (WAY-345). The cost of an occurrence is no cost of a
  cycle, which the count gives in money in its section *Cost*.

## What the counting command reads

The counting command of the audit reads the five tables below: *Classes*, *Weights*, *Costs of an
occurrence*, *Issues* and *Problems*. It finds each table by the heading above it and by its header
row, so keep both as they stand, with the columns in their order. A heading, a table or a column it
needs and cannot find ends the run with an error that names it (WAY-344).

- A table's rows follow its header row and its separator row, with no empty line between them; the
  table ends at the first line that does not start with `|`.
- A cell holds no `|` and no line break.
- A date is written `YYYY-MM-DD`, and a commit as its full hash of forty hexadecimal characters.
- A name of a class or of an issue is lower-case letters, digits and hyphens, and no two rows of
  its table share it.
- Text outside the five tables is not read; write there what you like.

## Classes

| Class | Meaning | Added | Withdrawn |
|---|---|---|---|
| confirmation | a remark that confirms the cycle did what it should; it reports no lapse | start | none |
| check-not-run-or-uncertain | a check that did not run, or whose result is uncertain | start | none |
| ambiguity-settled-by-agent | an ambiguity of the task, the plan or the instructions, which an agent settled by a choice of its own | start | none |
| foundation-gap | a gap in the product's foundation: an entry that the change needed is missing or wrong | start | none |
| known-problem-left | a problem known in the cycle and left without a fix | start | none |
| stale-reference | a reference in a task or a plan to a file, a line, an entry or a name that no longer holds | start | none |
| process-remark | a remark about the process itself: its instructions, its steps or its tools | start | none |

- *Class*: the name by which a problem names its class.
- *Meaning*: what a problem of the class is.
- *Added*: `start` for a class the list holds from the start of the register, or the date the class
  was added.
- *Withdrawn*: `none`, or the date from which no problem is given the class. A withdrawn class keeps
  its row, so that the problems given it earlier stay readable.

The list widens: where a problem fits no class, a session of the audit puts a new class before you —
its name, its meaning and the day it is added — and on your yes adds its row to this table, here in
your register; the problem is never given the nearest class instead (WAY-333). A row of *Problems*
whose class the list lacks is refused by the count until then. A change of what a class means is
written as that class withdrawn and a new class, under a new name, added on the same date. Each date
in *Added* or *Withdrawn* starts a new series of the cost and of no mechanism measure or gate
time, and the audit compares measures only within one series (WAY-339).

## Weights

| Weight | Meaning |
|---|---|
| no problem | the remark shows no lapse: a confirmation, or a remark that proved to be none |
| Minor | as the review of a cycle grades a finding Minor: polish, style, broader coverage that would be nice |
| Important | as the review of a cycle grades a finding Important: the change could not be trusted until it was fixed |
| Critical | as the review of a cycle grades a finding Critical: a bug, a security hole, data loss, broken functionality |

The scale has these four levels and gains no other: Minor, Important and Critical are the grades of
the review of a cycle (WAY-161), and no problem is the level below them (WAY-333). Adapt the
meanings, never the levels.

## Costs of an occurrence

| Cost of an occurrence | Meaning |
|---|---|
| nothing | the occurrence cost nothing: a confirmation, or a remark with no consequence |
| steps | a few steps of one agent within its stage, which the agent put right itself: a repeated command, a wrong path and a search, a repeated read |
| stage | a stage or a large part of it done again, or a large extra reading or checking by the same agent |
| round | an extra run of an agent: a round of fixes, an extra merge with the target branch, a new review, a slice made again |
| human | the human's time: a question, a decision, a manual check, a fix after the merge |

The scale has these five levels, each dearer than the one before, and gains no other (WAY-345). A
problem has the highest level its actual cost reached; what it could have cost is the weight's
business. Adapt the meanings, never the levels.

## Issues

| Issue | What | Fate | Fix |
|---|---|---|---|

- *Issue*: the name by which a problem names its issue.
- *What*: the matter, in one line.
- *Fate*: `open` while no fix is in place, `fixed` once a fix is in the-way, or `dropped` once you
  decide to leave the matter without a fix.
- *Fix*: for a `fixed` issue, the commit of the-way that holds the fix; otherwise `none`. A cycle
  whose version of the-way contains that commit ran with the fix, whatever its date (WAY-335).

## Problems

| Repository | Record | Stages | What | Class | Weight | Cost of an occurrence | Issue |
|---|---|---|---|---|---|---|---|

- *Repository*: the name of the product's repository, as your locations file names it among its
  keys (WAY-320).
- *Record*: the commit that adds the copy of the cycle's record to that repository, as the template
  of the record gives it (`task-cycle/record_template.md`); with *Repository* it names the cycle the
  problem comes from. Where a cycle committed its copy more than once, after a correction, it is the
  commit of the copy that holds the report the problem was found in.
- *Stages*: the stages of the cycle that reported the problem, by the names its record gives them,
  joined by ` · `.
- *What*: the problem, in one line.
- *Class*: the name of a class from *Classes*.
- *Weight*: a level from *Weights*.
- *Cost of an occurrence*: a level from *Costs of an occurrence*, the highest one that the actual
  cost of one occurrence of the problem reached.
- *Issue*: the name of an issue from *Issues*, or `none` while the problem belongs to no issue.
