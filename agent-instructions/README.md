# Working on the-way before `main`

This guide applies to work on the-way as the top-level repository while it has no `main` branch.
It does not govern a product that contains the-way as a `.the-way` submodule. `foundations` is the
integration branch. It is not a release of the process. The task-cycle skill is available for
product pilots; the full gate does not yet exist. Changes to the-way itself follow this guide.
When `main` is created, replace this guide with the task-cycle instructions before integrating
another change.

## Start a change

Start new work on a short task branch from a current, clean `foundations` commit. Keep unrelated
working-tree changes out of that branch and out of its commits.

Before editing, use `foundations/part_map.md` to identify the parts touched and read the decisions
whose *Scope* names those parts. Read the affected invariants and the relevant element templates
and skills. A change to a foundation entry follows the skill for that element, including a search
of the whole foundation for unlinked effects (WAY-33).

Until an entry reaches `main`, edit an existing decision in place. Show a change of meaning to
Mariusz for renewed acceptance (WAY-07). Update every fingerprint and dependent entry affected by
a changed binding part (WAY-31). Do not manufacture a new decision version merely to model
the unfinished pre-`main` history.

## Check the change

Run tests for each changed part with `python -B gate/run_tests.py <directory>`. Run the existing
critical-flow tests for every change (WAY-45): they are the tests holding a `flow: <identifier>`
line, and today `python -B gate/run_tests.py gate` runs them. For changed foundation files, run
their element format guards; use `--base none` and, where available, `--merge-onto none` because
there is no `main` commit to compare with. Read the reports, including warnings and `unchecked`
results. Before the request, also run the decisions and invariants guards with
`--merge-onto <the current foundations tip>`. Act on their relation-fingerprint findings and
resolve any operational error that prevents those checks from running; their findings about
copies of a version and about a placeholder request link are expected before `main`.

The available tests and guards are partial checks. Record what ran, what failed and what remained
unchecked in the review material. Never report them as a pass of the full gate. A missing method or
command stays visible as debt rather than being treated as agreement.

## Integrate into `foundations`

Before integration, compare the task branch with the current `foundations` tip. For a foundation
change, search the whole foundation again against that tip (WAY-33), update affected entries and
rerun the checks. A foundation change or a change to an invariant test is assessed once by an
independent agent following `elements/common/critique/SKILL.md` (WAY-10). Its record goes where
`elements/common/critique/SKILL.md` puts it; the record of both foundation searches goes in the
message of the commit that carries the change. Mariusz accepts the change at the merge.

Show the diff, test results, warnings and unchecked work before asking Mariusz to accept the merge.
Merge into `foundations` only after that review. Creating `main` is a separate release decision
that Mariusz makes; it is not part of integrating a change.
