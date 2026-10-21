# Working on the-way before `main`

This guide applies to work on the-way as the top-level repository while it has no `main` branch.
It does not govern a product that contains the-way as a `.the-way` submodule. `foundations` is the
integration branch. It is not a release of the process. The task-cycle skill is available for
product pilots; the full gate does not yet exist. Changes to the-way itself follow this guide.
When `main` is created, replace this guide with the task-cycle instructions before integrating
another change.

## While the slimming plan is applied

The-way is being slimmed down one file or skill at a time, by a plan kept in the author's private
notes: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\odchudzanie_radykalne_dane\plan_nanoszenia.md`.
An agent that cannot open it asks the human. Files and foundation entries the plan has not yet
reached still describe the mechanism this guide drops: fingerprints and their renewal, entry
versions, *Approved by* and the request link it waits for, format guards run as a step of a change,
the independent assessment and a second search of the foundation before the merge. A change to
the-way does not apply that mechanism, whatever such a file or entry says. Where a test of the-way
still requires part of it, such as a fingerprint beside a reference in the-way's own foundation,
the change meets the test with the repository's existing tools and does no more. While the plan is
applied, its own rhythm holds: each of its positions is one commit, reviewed as below, and each of
its stages is one request.

## Start a change

Start new work on a short task branch from a current, clean `foundations` commit. Keep unrelated
working-tree changes out of that branch and out of its commits.

Before editing, use `foundations/part_map.md` to identify the parts touched and read the decisions
whose *Scope* names those parts. Read the affected invariants and the relevant element templates
and skills. A change to a foundation entry follows the skill for that element, apart from the
mechanism this guide drops.

Until an entry reaches `main`, edit an existing decision in place (WAY-07). Do not manufacture a
new decision version merely to model the unfinished pre-`main` history.

## Make the change

Once a foundation entry the change writes or rewords is settled, its author searches the whole
foundation once for the entries the change touches and corrects them in the same change (WAY-33).
A finding the author cannot settle by correcting an entry — two decisions colliding with no
precedence written — goes to Mariusz before the change goes on. There is no second search before
the merge.

When the change is made, take the return step: compare each foundation entry the change touched,
and the part map, with the files of the repository, and correct in the same change whatever no
longer matches. Unlike the return step of WAY-11, it does not hunt for behaviour no invariant
covers; an invariant is written only for a rule the change, a decision or Mariusz sets.

## Check the change

Run every test of the-way: from the root, run `python -B gate/run_tests.py <directory>` for each
directory that holds a `test_*.py` file git tracks, without `--record`. In a POSIX shell this lists
those directories:

```
git ls-files | grep -E '(^|/)test_[^/]*\.py$' | xargs -n1 dirname | sort -u
```

The whole run takes about 16 minutes. Run the tests on the change as it goes into the request. A
run passes when its exit code is 0. One run fails for a known reason until the plan removes
`probes/`: `probes/claude-code-project-skills` looks for a sentence that the documentation it reads
no longer holds.

The author of the change, or the agent that leads the work, asks an agent that did not make the
change to review it (WAY-10). The reviewer receives the whole diff, the task or the plan's position
the change carries out, and the foundation entries the change touches, and reviews the change
against them. The reviewer decides which of its remarks block. The author makes one fix for them,
and an agent that did not make the change reviews that fix once; a remark still open after that goes to Mariusz in the
request.

## Integrate into `foundations`

Open a request to merge the task branch into `foundations`. It holds:

- every foundation entry the change alters, each with one sentence on what it changes in meaning;
- every test command run and its exit code;
- what was not checked.

Mariusz merges the request; the merge is the acceptance of the change and of every entry it alters.
Creating `main` is a separate release decision that Mariusz makes; it is not part of integrating a
change.
