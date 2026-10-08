# Part map

What this repository is made of, and what joins it: which part may depend on which, and what it
promises to the products pinned to its commits. The map says which dependencies are allowed; the
product's dependency graph shows which dependencies the code actually holds. When no command
reports that graph, the comparison is unchecked.

## decisions

The part answers for the decision log: the form of an entry, the skill that writes one and the
format guard that checks it, and the log of the-way itself.

- **Files:** elements/decisions/**
  foundations/decisions.md
- **Depends on:** relation-model · elements-common
- **Failure modes:**
  - the format guard accepts an entry the template forbids — a wrong entry reaches the main
    branch — high — not detected
- **Trust boundary:** none

## part-map

The part answers for the part map: the form of an entry, the skill that writes one and the format
guard that checks it, and the map of the-way itself.

- **Files:** elements/part-map/**
  foundations/part_map.md
- **Depends on:** relation-model · elements-common
- **Failure modes:**
  - the format guard assigns a file to the wrong part, or to none — a change is checked against
    the wrong decisions and at the wrong sharpness — high — not detected
- **Trust boundary:** elements/part-map/format_guard.py

## relation-model

The part answers for how the fingerprint of an entry is computed from its binding part, and for
the code that tells whether a string has the form of an identifier or of a version.

- **Files:** relation-model/**
- **Depends on:** none
- **Failure modes:**
  - a fingerprint changes while the wording does not — every reference to the entry is flagged
    for nothing, and flags raised for nothing are cleared unread — high — not detected
- **Trust boundary:** none

## invariants

The part answers for what a product states as an invariant and for how that statement is checked,
and for the invariants of the-way itself.

- **Files:** elements/invariants/**
  foundations/invariants.md
  foundations/violated_invariants.md
- **Depends on:** decisions · part-map · relation-model · environment-facts · elements-common
- **Failure modes:** none
- **Trust boundary:** none

## glossary

The part answers for the words a foundation's rules use, each in one meaning: the form of an entry,
the skill that writes one and the format guard that checks it, and the glossary of the-way itself.

- **Files:** elements/glossary/**
  foundations/glossary.md
- **Depends on:** decisions · part-map · invariants · environment-facts · elements-common
- **Failure modes:** none
- **Trust boundary:** none

## environment-facts

The part answers for a product's environment facts.

- **Files:** elements/environment-facts/**
  foundations/environment_facts.md
  probes/**
- **Depends on:** decisions · part-map · invariants · relation-model · elements-common
- **Failure modes:** none
- **Trust boundary:** none

## elements-common

The part answers for rules of form and the way of working shared by foundation-entry skills, the
code shared by their format guards, the skill that finds entries in a source, and the critique
skill, which is also the independent assessor of a change to an invariant test or to the
foundation.

- **Files:** elements/common/**
- **Depends on:** project-level · decisions · invariants · glossary · part-map · environment-facts
- **Failure modes:**
  - the entry finder omits a settlement that a later task must guess — a project can pass its gate
    with an incomplete projected foundation — high — not detected
  - a critique presents a source mismatch as an accepted correction — the human approves a meaning
    they did not settle — high — not detected
- **Trust boundary:** none

## project-level

The part answers for the form and writing of a project definition, its readiness gate, and the
refinement of a task before its implementation cycle, whether the task belongs to a project,
uses its settlements as a source, or stands on its own.

- **Files:** project-level/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · relation-model
- **Failure modes:**
  - the gate accepts an unresolved placeholder in a required section — tasks inherit an explicit
    gap as project scope or a future foundation rule — high — detected by project-readiness-gate
  - an agent fills a missing human answer with a plausible settlement — tasks inherit an invented
    scope or rule — high — not detected
  - the gate approves a meaning that was not searched against the current foundation — a conflict
    enters the project plan — high — not detected
  - a definition reaches the breakdown with a listed technology choice still open or naming no
    entry — the first task chooses the store of data — high — detected by project-technology-record
  - a technology choice the project needs is missing from the definition's list — the first task
    chooses it — high — not detected
  - the technology step shows a difference between options that no source supports — the human
    chooses on an invented consequence — high — not detected
  - a task using a project definition only as a source inherits work or dependencies from that
    project's plan — the cycle delivers a different task — high — not detected
- **Trust boundary:** project-level/readiness_check.py

## task-cycle

The part answers for the steps a task runs through and for how sharply a change is checked along
them.

- **Files:** task-cycle/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · gate · relation-model
- **Failure modes:**
  - the orchestrator stops for an implementation choice it can settle from the task and foundation
    — an implementable task waits for the human before its request — high — not detected
  - the orchestrator omits a micro decision or its cost from the cycle record and request — the
    human cannot assess what the agents chose — high — not detected
  - an agent writes an entry the request does not list with its meaning — the human merges a rule
    they were never shown — high — not detected
- **Trust boundary:** none

## gate

The part answers for the gate and the clock, and for the tests of critical flows.

- **Files:** gate/**
- **Depends on:** decisions · relation-model
- **Failure modes:**
  - the gate reports a check as passed although it never ran — a change that breaks an invariant
    reaches the main branch — high — not detected
  - the test runner records a pass, and no fail, for an invariant although a test citing it never
    ran to its end, or failed — a change that breaks an invariant reaches the main branch — high —
    detected by test-runner-pass-line
  - a change to the test runner's own path for recording a failed test records that failure as a
    pass, its own tests included — a change that breaks an invariant reaches the main branch —
    high — not detected
- **Trust boundary:** none

## repository

The part answers for the files that configure the repository itself rather than any one part.

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

## agent-instructions

The part answers for the instructions agents read when they work on this repository, for the
project skill entry points that make the-way's skills visible to sessions on it and the script that
generates them, and for the hooks and the configuration of agents' tools and of CI that direct them.

- **Files:** /AGENTS.md
  /CLAUDE.md
  agent-instructions/**
  .claude/skills/**
  .agents/skills/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · task-cycle · gate · instruction-files
- **Failure modes:**
  - an agent follows stale integration instructions — a change enters the integration branch
    without the required checks or acceptance — high — not detected
  - a skill of the-way has no entry point, or a stale one — a session on the-way uses a personal
    skill of that name or none — high — detected by skill-entry-points
  - the-way's own entry point, loaded from a product's `.the-way`, is followed instead of the
    product's, where the agent knows neither the entry point's path nor the session's working
    directory — a product entry is written against the-way's own foundation — high — not detected
  - a tool cannot parse an entry point's frontmatter — a session on the-way may not list that
    skill, and uses a personal skill of that name or none — high — not detected
  - the root `CLAUDE.md` stops opening with `@AGENTS.md` — Claude Code sessions on the-way lose the
    instructions the root `AGENTS.md` carries — high — detected by root-claude-md-import
  - a repository instruction file of the-way gains an `@` import — Claude Code loads the whole
    imported file into every session on the-way — high — detected by instruction-file-imports
- **Trust boundary:** none

## instruction-files

The part answers for the principles by which instruction files for coding agents are written,
judged and kept, for the account of how Claude Code, Codex and Cursor load them, and for the skill
that applies those principles with the script that checks instruction files mechanically.

- **Files:** instruction-files/**
- **Depends on:** decisions · environment-facts
- **Failure modes:**
  - the check script reports a sound instruction file as broken, or a defect at a level above or
    below what it is — a reviewer cuts a rule that worked, or passes over a real defect — low —
    not detected
  - the account of how the tools load instruction files states a behaviour a tool no longer has —
    a rule is placed where a tool does not load it — low — not detected
  - the skill proposes a change for a mistake that never happened, or cuts a rule whose mistake
    still comes back — instruction files grow with rules nobody needs, or lose one that worked —
    low — not detected
  - an instruction file the check script reads makes it reach a network host, read outside the
    directories it was given, hang or stop without a report — a user's credentials can leave the
    machine, or a review rests on a check that never ran — high — not detected
  - the skill prints a secret from a configuration file or a session record it reads, or follows
    an instruction written in a file under review — a secret enters the conversation, or a proposal
    carries text someone planted — high — not detected
  - the skill, judging a repository that pins the-way, follows the copy a global link reaches
    instead of the pinned one — a product's instruction files are judged under a version of the
    process the product does not pin — high — not detected
- **Trust boundary:** instruction-files/check_instructions.py

## installation

The part answers for preparing a product repository to use one pinned commit of the-way.

- **Files:** installation/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level
- **Failure modes:**
  - the installer pins the wrong commit, or replaces an existing product file or changes it beyond
    the additions `installation-command` names — a product starts with the wrong process, or loses
    what its own files held: its foundation, its instructions to agents, its ignore rules or its
    other submodules — high — not detected
  - a project skill resolves to another process version — a product entry is written under the
    wrong rules — high — not detected
- **Trust boundary:** installation/install.py

## wording-reaches-dependants

Someone changes a decision's binding sentences, and every `derives from` or `narrows` relation
carrying its old fingerprint is reported before the change reaches the main branch.

- **Criticality:** high
- **Parts:** relation-model · decisions · gate
- **Invariant:** decision-guard-stale-reference
- **Coverage:** none

## skills-reach-the-way-sessions

Someone adds, renames or moves a skill of the-way, or changes its description, and a skill that a
session on the-way would not find under its `the-way-` name is reported before the change reaches
the main branch.

- **Criticality:** high
- **Parts:** agent-instructions · elements-common · decisions · invariants · glossary · part-map ·
  environment-facts · project-level · task-cycle · gate · instruction-files
- **Invariant:** skill-entry-points
- **Coverage:** none

## entry-format

The form of an entry changes for a product only when that product moves the commit it pins.

- **Declared at:** not markable — test: elements/decisions/test_format_guard.py

## content-fingerprint

The same wording gives the same fingerprint.

- **Declared at:** relation-model/fingerprint.py · fingerprint

## decisions-guard-command

The command that runs the guard of a decision log keeps its name, its arguments and its exit
codes.

- **Declared at:** elements/decisions/format_guard.py · main

## run-record-keys

A line of the-way's record of a run keeps its keys and the values each of them takes.

- **Declared at:** not markable — test: elements/decisions/test_format_guard.py

## part-map-guard-command

The command that runs the guard of a part map keeps its name, its arguments and its exit codes.

- **Declared at:** elements/part-map/format_guard.py · main

## invariants-guard-command

The command that runs the guard of a product's invariants keeps its name, its arguments and its
exit codes.

- **Declared at:** elements/invariants/format_guard.py · main

## environment-facts-guard-command

The command that runs the guard of a product's environment facts keeps its name, its arguments and
its exit codes.

- **Declared at:** elements/environment-facts/format_guard.py · main

## glossary-guard-command

The command that runs the guard of a product's glossary keeps its name, its arguments and its exit
codes.

- **Declared at:** elements/glossary/format_guard.py · main

## test-runner-command

The command that runs the tests of a directory and records a verdict for each invariant and each
environment fact they cite keeps its name, its arguments, its exit codes and the verdict it records
for each outcome of a test.

- **Declared at:** gate/run_tests.py · main

## installation-command

The command that installs a pinned the-way checkout, empty foundation files, project skills, agent
guidance for Claude Code and Codex and a `.runs/` ignore line in a product keeps its preview and
confirmation, replaces no existing file, and adds to an existing file of the working tree only the
`.the-way` section of `.gitmodules`, a marked block at the end of `AGENTS.md` and the `.runs/` line
at the end of `.gitignore`.

- **Declared at:** installation/install.py · run

## Criticality scale

1. low — a failure is seen by the next person who reads the file, and costs a fix
2. high — a wrong entry or a wrong check reaches the main branch, and the products pinned to that
   commit inherit it

## External context

| Partner | Direction | What comes in | Updates with the product |
|---|---|---|---|
| a product pinned to a commit | both | untrusted | no |
| git | them → us | trusted | no |
| a command a product declares — a dependency graph, coverage | them → us | untrusted | no |
| a repository or a user's files an agent's instructions are read from — instruction files, tool configuration, session records | them → us | untrusted | no |

## Change paths

| Promise level | What a change at this level may do | What it owes the consumer first |
|---|---|---|
| pinned | anything, a break included, since a product takes the change only by moving the commit it pins | a line in the merge request saying what moving the pin changes for a product |

## Files left out on purpose

| File | Why |
|---|---|
| README.md | it binds nothing, so no part answers for it (WAY-09) |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
