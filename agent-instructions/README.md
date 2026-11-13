# Working on the-way before `main`

This guide applies to work on the-way as the top-level repository while it has no `main` branch.
It does not govern a product that contains the-way as a `.the-way` submodule. `foundations` is the
integration branch. It is not a release of the process. The task-cycle skill is available for
product pilots; one command runs every test of the-way (see "Check the change"). Changes to the-way
itself follow this guide.
When `main` is created, replace this guide with the task-cycle instructions before integrating
another change.

## The form of the foundation

`elements/common/foundation_check.py` checks the identifiers, references, fields and the part of
each file of the foundation of the-way, and `elements/common/migrate_foundation.py` brings a
foundation of the earlier form to the current one.

## Start a change

Start new work on a short task branch from a current, clean `foundations` commit. Keep unrelated
working-tree changes out of that branch and out of its commits.

Before editing, use `foundations/part_map.md` to identify the parts touched and read the decisions
whose *Scope* names those parts. Read the affected invariants and the relevant element templates
and skills. A change to a foundation entry follows the skill for that element.

Edit an existing decision in place, on `main` as before it (WAY-07).

## Make the change

Once a foundation entry the change writes or rewords is settled, its author searches the whole
foundation once for the entries the change touches and corrects them in the same change (WAY-33).
A finding the author cannot settle by correcting an entry, such as two decisions colliding with no
precedence written where what Mariusz accepted does not give the outcome, and a correction that
would change the meaning of an approved decision beyond what the task or the plan's position settles
(WAY-114), go to Mariusz before the change goes on. Where what Mariusz accepted does give the
outcome, the change records the precedence in the decision that prevails, and its request names it
with the passages of what he accepted that give the outcome (WAY-25). There is no second search
before the merge.

When the change is made, take the return step: compare the foundation entries the change edits,
those the task or the plan's position names and those the search found, and the part map, with the
files of the repository, and correct in the same change whatever no longer matches. Unlike the
return step of WAY-11, it does not hunt for behaviour no invariant covers; an invariant is written
only for a rule the change, a decision or Mariusz sets.

## Check the change

Run every test of the-way with one command, from the root:

```
python -B gate/run_tests.py
```

It runs the tests of every directory that holds a `test_*.py` file git tracks, the directories at
the same time, each report printed whole under its directory's name when that directory ends, and
ends with a line counting the tests and naming each directory that failed. `--jobs N` limits how
many directories run at once, and `--jobs 1` runs them one after another; `--slowest N` lists the N
slowest tests of each directory. A new test file in a new directory runs
only once it is added to git (`git add`). The whole run takes about 16 minutes with `--jobs 1`, and
less by default. Run it on the
change as it goes into the request. A run passes when its exit code is 0. While the change is
made, `python -B gate/run_tests.py <directory>` runs the tests of one directory. A change to
`gate/run_tests.py` is also checked with `python -B -m unittest discover -s gate -p "test_*.py"`,
which does not rest on the runner it checks.

The author of the change, or the agent that leads the work, asks an agent that did not make the
change to review it (WAY-10). The reviewer receives the whole diff, the task or the plan's position
the change carries out, and the foundation entries the change touches, and reviews the change
against them. The reviewer decides which of its remarks block. The author makes one fix for them,
and an agent that did not make the change reviews that fix once. A blocking remark still open after
that stops the change and goes to Mariusz; the other remarks go into the lists of the request's
lower part, as `task-cycle/skill/request_template.md` gives.

## Integrate into `foundations`

Open a request to merge the task branch into `foundations`. Its description follows
`task-cycle/skill/request_template.md` (WAY-286). Where no task cycle ran, *Cost* reads `none` and
*Course of the cycle* holds **Task and sources** alone, its other labels reading `none`; the agent
leading the work judges which findings the user of a product or a person working with the process
will feel (WAY-289). Before the request opens, and before each later edit of its description, check
the description and correct it as the template gives, an error you hold wrong included (WAY-290,
WAY-291):

```
python -B task-cycle/request_check.py <description file> --task <document the change carries out>
```

`--task` is the task document the change carries out, or, for a change that carries out a position
of a project plan, the plan that holds that position.

Check the same file for absolute paths and note links as well, and correct what it lists until it
lists nothing, the block in the language of the task document included (WAY-308, WAY-309):

```
python -B task-cycle/private_paths_check.py <description file>
```

Mariusz merges the request; the merge accepts the change and each entry he did not see at the task
document, those its section for the human's decisions puts before him (WAY-114).
Creating `main` is a separate release decision that Mariusz makes; it is not part of integrating a
change.
