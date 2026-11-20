# Working on the-way before `main`

This guide applies to work on the-way as the top-level repository while it has no `main` branch.
It does not govern a product that contains the-way as a `.the-way` submodule. `foundations` is the
integration branch. It is not a release of the process. The task-cycle skill is available for
product pilots; one command runs every test of the-way (see "Check the change"). Changes to the-way
itself follow this guide.
When `main` is created, replace this guide with the task-cycle instructions before integrating
another change.

## The form of the foundation

`elements/common/foundation_check.py` checks the identifiers, references, fields, the lines
`decision:` of the tests and the part of each file of the foundation of the-way; it reports the
decisions that nothing holds, the paragraphs of binding sentences over three sentences or 300 words
and binding sentences over 600 words in all their paragraphs, in a decision a change adds or whose
binding sentences it alters, a different division into paragraphs counting as an alteration for this
report alone, lists the other decisions over those limits, and lists the invariants that read `test`
whose sentence a change rewords while no file citing them changes, all against the commit the branch
left the main branch from; an invariant that reads `test` whose sentence a change rewords and whose
copy at that commit lacks *Method* or *Part* it lists too, naming the field, whether or not a file
citing it changes. The script `elements/common/migrate_foundation.py` brings a foundation of the
earlier form to the current one.

## Start a change

Start new work on a short task branch from a current, clean `foundations` commit. Keep unrelated
working-tree changes out of that branch and out of its commits.

Before editing, use `foundations/part_map.md` to identify the parts touched and read the decisions
whose *Scope* names those parts. Read the affected invariants and the relevant element templates
and skills. A change to a foundation entry follows the skill for that element.

Edit an existing decision in place, on the main branch as before it (WAY-07).

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
slowest tests of each directory. A new test file in a new directory runs only once it is added to
git (`git add`). The whole run takes about 16 minutes with `--jobs 1`, and less by default. Run it
on the change as it goes into the request where no CI run stands for it, as the next paragraph
gives. A run passes when its exit code is 0. While the change is made,
`python -B gate/run_tests.py <directory>` runs the tests of one directory. A change to
`gate/run_tests.py` is also checked with `python -B -m unittest discover -s gate -p "test_*.py"`,
which does not rest on the runner it checks.

The same command runs in CI, on Linux and on Windows, on every pull request into `foundations`
(`.github/workflows/tests.yml`; WAY-16). The two jobs are two checks, `tests` for Linux and
`tests-windows` for Windows; the owner of the repository sets both as required before a merge in the
branch rules of `foundations`, with a bypass for the owner, a setting of the host that no file of
the repository holds, and the host offers a check for that setting only once the check has run on a
request. The tests that need POSIX — links, loops of links, a FIFO — run on Linux, and those that
need Windows — junctions, network paths — run on Windows, so each system checks what the other
cannot. The run of CI on the head of a request whose code is finished is the final gate of the task
cycle (WAY-160), so a change that goes through a task cycle needs no full run of its own before the
request; where CI does not answer within 30 minutes of a push, the cycle runs the command itself. CI
runs no other checking command.

The author of the change, or the agent that leads the work, asks an agent that did not make the
change to review it (WAY-10). The reviewer receives the whole diff, the task or the plan's position
the change carries out, and the foundation entries the change touches, and reviews the change
against them. The reviewer decides which of its remarks block. The author makes one fix for them,
and an agent that did not make the change reviews that fix once. A blocking remark still open after
that stops the change and goes to Mariusz; the other remarks go into the lists of the request's
lower part, as `task-cycle/skill/request_template.md` gives.

## Integrate into `foundations`

Open a request to merge the task branch into `foundations`. Its description follows
`task-cycle/skill/request_template.md`. Where no task cycle ran, *Cost* reads `none` and
*Course of the cycle* holds **Task and sources** alone, its other labels reading `none`; the agent
leading the work judges which findings the user of a product or a person working with the process
will feel (WAY-289). Before the request opens, and before each later edit of its description, check
the description and correct it as the template gives, an error you hold wrong included:

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

Once the request is open, and after each correction, wait for the CI run on its last head, as the
final gate of the change, and put its result into the description under *Checks*; a red result is a
failure of the gate, which the change fixes before the request goes to Mariusz, save a check outside
the task's scope that passes when run again, which the description names with the task that fixes
it (WAY-261). Where the run gives no result within 30 minutes of the push, run the command on the
change yourself and say in the description that CI did not answer and that the gate ran on your
own system. A request left blocked for unfinished code is not waited for
(`task-cycle/skill/SKILL.md`, step 12, WAY-160).

Where the description puts an item of *Fix or let through* before Mariusz and he answers to fix it
in this request, the answer starts one fix by the author and one review of that fix by an agent
that did not make it, the same loop as for the blocking remarks of a review (see "Check the
change"). What stays unfixed after that goes back to him only with the question whether to make a
task of it, which he lets through by merging; the description is edited for the state after the
fix, and checked as above.

Mariusz merges the request; the merge accepts the change and each entry he did not see at the task
document, those its section for the human's decisions puts before him (WAY-114).
Creating `main` is a separate release decision that Mariusz makes; it is not part of integrating a
change.
