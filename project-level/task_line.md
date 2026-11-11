# Write a task's line in the backlog

Read by `refine-task` where it makes a task's line or moves it to ready, and by `lead-project` where
it moves a line to ready or brings the dependencies of lines in step with the plan (WAY-154). How a
line is handled — the status of a new line, the move to ready, the form of the dependencies and of
the identifier a dependency names, how a line is found, which fields may change, what to do where
an identifier is already carried — is the rules of the task place, never the-way's and never text
written at the product (WAY-107): find them as `project-level/backlog_place.md` gives, the line
`Task rules`, and read the passages of those rules on a task's line before writing one. Where the
rules give none of the three forms, ask the human once; write no form of your own.

## Make the line

Where the task has no line in the task place, a refiner makes one. This is the one place of the
rule; the files that name it point here.

- **When.** In the turn that first creates the task's document. A refiner of a project round makes
  it in that turn at once, in parallel with the round's other refiners, with no wait for them and no
  queue of writes. Where it cannot be made then — the rules of the task place are not yet known, a
  question to the human stands — or the document exists without a line, as one written before the
  line was made at all does, or a parked task refined again from its text, make it in the first turn
  in which the rules are known and the task has none, and say in that turn's text that the line
  stands unmade until then.
- A new line links the task's document and takes the status the rules give for a task whose
  document is in refinement.
- A task of a project plan carries its identifier and its dependencies, as the two sections below
  give.

## The identifier

The rules give the form of the identifier — its characters, and that it is unambiguous in the whole
place. The-way gives its derivation, so that a refiner can write the identifier of any task before
that task's line exists, from the plan and the task's name in the plan alone: the plan's file name
without its extension, joined by `-` to the task's name in the plan, in lower case, each run of
characters other than lower-case letters and digits, hyphens included, turned into one `-`, none at
either end (WAY-329). The task `forest-on-hex-grid` of the plan file `player-game.md` has the
identifier `player-game-forest-on-hex-grid`. A task that belongs to no plan has no identifier from
the-way; a line of it takes one only where the rules require it.

The derivation is unambiguous only while the plan file names of the place differ, and only while no
two pairs join to the same text: the plan `a-b.md` with the task `c` and the plan `a.md` with the
task `b-c` both give `a-b-c`. The derivation does not check this.

## The dependencies

Take them from the `Depends on` column of the task's row in the plan: each number in it stands for
the task of that number in the plan, whose identifier is derived as above, and the line carries them
in the form the rules give. A row reading `—` gives a line none. The refiner writes them when it
makes the line, and keeps the task's line, and the lines of the tasks it waits on and that wait on
it, in agreement with the plan's dependencies as the rules of the task place give; where those rules
do not say how, it asks the human once. The project orchestrator brings the dependencies in the
lines of the changed rows in step with the plan when a change of the plan alters a `Depends on`
cell.

## Move to ready

At the human's acceptance of the complete task document, move the line to ready as the rules give,
with whatever else the rules say goes with that move. Do it with the writes that accept the document:
by hand, the agent that marks the document ready; in a project round, the project orchestrator,
together with the document's `Status:` and the plan's row, and never a refiner. Where no line stands
at acceptance — one lost, or never made — make it, already ready, as "Make the line" and the two
sections after it give it (identifier and dependencies of a plan task included), and say so in the
record of the acceptance. A change of the line that follows from the task's later states in the plan
(`in cycle`, `done`) is not made here.
