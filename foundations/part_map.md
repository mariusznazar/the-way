# Part map

What this repository is made of, and what joins it: which part may depend on which, and what it
promises to the products pinned to its commits. The map says what is allowed; what the code holds
is computed from it.

## decisions — The decision log

The part answers for the decision log: the form of an entry, the tools that write and check one,
and the log of the-way itself.

- **Files:** elements/decisions/**
  foundations/decisions.md
- **Depends on:** relation-model
- **Failure modes:**
  - the guard accepts an entry the template forbids — a wrong entry reaches the main branch, and
    every product pinned to that commit inherits it — high — not detected
- **Trust boundary:** none

## part-map — The part map

The part answers for the part map: the form of an entry, the tools that write and check one, and
the map of the-way itself.

- **Files:** elements/part-map/**
  foundations/part_map.md
- **Depends on:** relation-model
- **Failure modes:**
  - the guard assigns a file to the wrong part, or to none — a change is checked against the
    wrong decisions and at the wrong sharpness — high — not detected
- **Trust boundary:** elements/part-map/format_guard.py

## relation-model — The relation model

The part answers for the fingerprint of an entry and for the references it flags when
that entry changes.

- **Files:** relation-model/**
- **Depends on:** none
- **Failure modes:**
  - a fingerprint changes while the wording does not — every reference to the entry is flagged
    for nothing, and flags raised for nothing are cleared unread — high — not detected
- **Trust boundary:** none

## invariants — Invariants

The part answers for what a product states as an invariant and for how that statement is checked,
and for the invariants of the-way itself.

- **Files:** elements/invariants/**
  foundations/invariants.md
  foundations/violated_invariants.md
- **Depends on:** decisions · part-map · relation-model · environment-facts
- **Failure modes:** none
- **Trust boundary:** none

## glossary — The glossary

The part answers for the words a foundation's rules use, each in one meaning: the form of an entry,
the tools that write and check one, and the glossary of the-way itself.

- **Files:** elements/glossary/**
  foundations/glossary.md
- **Depends on:** decisions · part-map · invariants · environment-facts
- **Failure modes:** none
- **Trust boundary:** none

## environment-facts — Environment facts

The part answers for a product's environment facts.

- **Files:** elements/environment-facts/**
  foundations/environment_facts.md
  probes/**
- **Depends on:** decisions · part-map · invariants · relation-model
- **Failure modes:** none
- **Trust boundary:** none

## task-cycle — The task cycle

The part answers for the steps a task runs through and for how sharply a change is checked along
them.

- **Files:** none
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

## gate — The gate

The part answers for the gate and the clock, and for the tests of critical flows.

- **Files:** gate/**
- **Depends on:** decisions · relation-model
- **Failure modes:**
  - the gate reports a check as passed although it never ran — a change that breaks an invariant
    reaches the main branch, and every product pinned to that commit inherits the gap — high —
    not detected
  - the test runner records a pass, and no fail, for an invariant although a test citing it never
    ran to its end, or failed — a change that breaks an invariant reaches the main branch, and
    every product pinned to that commit inherits the gap — high — detected by test-runner-pass-line
  - a change to the test runner's own path for recording a failed test records that failure as a
    pass, its own tests included — a change that breaks an invariant reaches the main branch, and
    every product pinned to that commit inherits the gap — high — not detected
- **Trust boundary:** none

## repository — The files that serve the whole repository

The part answers for the files that configure the repository itself rather than any one element.

- **Files:** /.gitattributes
  /.gitignore
  /.python-version
- **Depends on:** none
- **Failure modes:**
  - a file is stored with the line endings of whoever wrote it — a later rewrite turns the whole
    file over and buries what actually changed in it — low — not detected
  - an ignore pattern hides a file that should be tracked — it never reaches a commit and no part
    answers for it — low — not detected
- **Trust boundary:** none

## wording-reaches-dependants — A change of a binding part reaches what leans on it

Someone changes the binding sentences of a foundation entry, and every reference that leans on
the old binding part is reported before the change reaches the main branch.

- **Criticality:** high
- **Parts:** relation-model · decisions · gate
- **Invariant:** decision-guard-stale-reference — test: gate/test_wording_reaches_dependants.py
- **Coverage:** none

## entry-format — The form of an entry

The form of an entry changes for a product only when that product moves the commit it pins.

- **Declared at:** not markable — test: elements/decisions/test_format_guard.py

## content-fingerprint — The fingerprint

The same wording gives the same fingerprint.

- **Declared at:** relation-model/fingerprint.py · fingerprint

## decisions-guard-command — The command of the decision guard

The command that runs the guard of a decision log keeps its name, its arguments and its exit
codes.

- **Declared at:** elements/decisions/format_guard.py · main

## run-record-keys — The form of the-way's record of a run

A line of the-way's record of a run keeps its keys and the values each of them takes.

- **Declared at:** not markable — test: elements/decisions/test_format_guard.py

## part-map-guard-command — The command of the map guard

The command that runs the guard of a part map keeps its name, its arguments and its exit codes.

- **Declared at:** elements/part-map/format_guard.py · main

## invariants-guard-command — The command of the invariants guard

The command that runs the guard of a product's invariants keeps its name, its arguments and its
exit codes.

- **Declared at:** elements/invariants/format_guard.py · main

## environment-facts-guard-command — The command of the environment facts guard

The command that runs the guard of a product's environment facts keeps its name, its arguments and
its exit codes.

- **Declared at:** elements/environment-facts/format_guard.py · main

## glossary-guard-command — The command of the glossary guard

The command that runs the guard of a product's glossary keeps its name, its arguments and its exit
codes.

- **Declared at:** elements/glossary/format_guard.py · main

## test-runner-command — The command of the test runner

The command that runs the tests of a directory and records a verdict for each invariant and each
environment fact they cite keeps its name, its arguments, its exit codes and the verdict it records
for each outcome of a test.

- **Declared at:** gate/run_tests.py · main

## Criticality scale

1. low — a failure is seen by the next person who reads the file, and costs a fix
2. high — a wrong entry or a wrong check reaches the main branch, and the products pinned to that
   commit inherit it

## External context

| Partner | Direction | What comes in | Updates with the product |
|---|---|---|---|
| a product pinned to a commit | us → them | — | no |
| git | them → us | trusted | no |
| a command a product declares — a dependency graph, coverage | them → us | untrusted | no |

## Change paths

| Promise level | What a change at this level may do | What it owes the consumer first |
|---|---|---|
| pinned | anything, a break included, since a product takes the change only by moving the commit it pins | a line in the merge request saying what moving the pin changes for a product |

## Files left out on purpose

| File | Why |
|---|---|
| README.md | it binds nothing and only tells a reader what the repository is, so no part answers for it (WAY-09) |

## Withdrawn identifiers

| Identifier | Successors |
|---|---|
