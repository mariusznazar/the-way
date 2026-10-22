# Part map

What this repository is made of, and what joins it: which part may depend on which, and what it
promises to the products pinned to its commits. The map says which dependencies are allowed; the
return step of a change compares them with the code.

## decisions

The part answers for the decision log: the form of an entry, the skill that writes one and the
log of the-way itself.

- **Files:** elements/decisions/**
  foundations/decisions.md
- **Depends on:** elements-common
- **Trust boundary:** none

## part-map

The part answers for the part map: the form of an entry, the skill that writes one and the map of
the-way itself.

- **Files:** elements/part-map/**
  foundations/part_map.md
- **Depends on:** elements-common
- **Trust boundary:** none

## relation-model

The part answers for how the fingerprint of an entry is computed from its binding part, and for
the code that tells whether a string has the form of an identifier or of a version.

- **Files:** relation-model/**
- **Depends on:** none
- **Trust boundary:** none

## invariants

The part answers for what a product states as an invariant and for how that statement is checked,
and for the invariants of the-way itself.

- **Files:** elements/invariants/**
  foundations/invariants.md
- **Depends on:** decisions · part-map · relation-model · environment-facts · elements-common
- **Trust boundary:** none

## glossary

The part answers for the words a foundation's rules use, each in one meaning: the form of an entry,
the skill that writes one, and the glossary of the-way itself.

- **Files:** elements/glossary/**
  foundations/glossary.md
- **Depends on:** decisions · part-map · invariants · environment-facts · elements-common
- **Trust boundary:** none

## environment-facts

The part answers for a product's environment facts.

- **Files:** elements/environment-facts/**
  foundations/environment_facts.md
- **Depends on:** decisions · part-map · invariants · relation-model · elements-common
- **Trust boundary:** none

## elements-common

The part answers for rules of form and the way of working shared by foundation-entry skills, the
script that checks a whole foundation's identifiers, references and assignment of files to parts,
the references of a product's guidelines included, the script that migrates a foundation from the
earlier form of the-way, the skill that finds entries in a source, and the critique skill, which
reads a proposal critically before the human sees it.

- **Files:** elements/common/**
- **Depends on:** project-level · decisions · invariants · glossary · part-map · environment-facts
- **Trust boundary:** none

## project-level

The part answers for the form and writing of a project definition, its readiness gate, the
breakdown of an approved definition into a project plan and the check of that plan, and the
refinement of a task before its implementation cycle, whether the task belongs to a project,
uses its settlements as a source, or stands on its own, and for leading a handed-over plan through
refinement and evidence-backed upkeep of task states.

- **Files:** project-level/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · relation-model · product-guidelines
- **Trust boundary:** project-level/readiness_check.py
  project-level/plan_check.py
  project-level/plan_state.py

## task-cycle

The part answers for the steps a task runs through and for the review its change gets along
them.

- **Files:** task-cycle/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · gate · relation-model · product-guidelines
- **Trust boundary:** none

## gate

The part answers for the command that runs every test of the-way, and for the tests of critical
flows.

- **Files:** gate/**
- **Depends on:** none
- **Trust boundary:** none

## repository

The part answers for the files that configure the repository itself rather than any one part.

- **Files:** /.gitattributes
  /.gitignore
  /.python-version
- **Depends on:** none
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
  elements-common · project-level · task-cycle · gate · instruction-files · product-guidelines
- **Trust boundary:** none

## instruction-files

The part answers for the principles by which instruction files for coding agents are written,
judged and kept, for the account of how Claude Code, Codex and Cursor load them, and for the skill
that applies those principles with the script that checks instruction files mechanically.

- **Files:** instruction-files/**
- **Depends on:** decisions · environment-facts · installation
- **Trust boundary:** instruction-files/check_instructions.py

## installation

The part answers for preparing a product repository to use one pinned commit of the-way.

- **Files:** installation/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · product-guidelines
- **Trust boundary:** installation/install.py

## product-guidelines

The part answers for the form every product's guidelines share, for the template of each discipline
of guidelines with the skill that leads the work on them, for the shared reading that selects
guidelines for a change and recognizes what is missing.

- **Files:** product-guidelines/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · instruction-files · task-cycle
- **Trust boundary:** none

## test-runner-command

The command that runs every test of a repository, or the tests of one directory, keeps its name, its
argument and its exit codes.

- **Relied on by:** a product pinned to a commit of the-way

## installation-command

The command that installs a pinned the-way checkout, empty foundation files, project skills, agent
guidance for Claude Code and Codex and a `.runs/` ignore line in a product keeps its preview and
confirmation, replaces no existing file, and adds to an existing file of the working tree only the
`.the-way` section of `.gitmodules`, a marked block at the end of `AGENTS.md` and the `.runs/` line
at the end of `.gitignore`.

- **Relied on by:** a product pinned to a commit of the-way

## project-plan-state-command

The command that reads a project's plan and product repository keeps its name, positional
arguments, evidence-bearing proposals and unchecked observations, exit codes and preservation of
plan and task documents.

- **Relied on by:** a product pinned to a commit of the-way

## External context

| Partner | Direction | What comes in |
|---|---|---|
| a product pinned to a commit | both | untrusted |
| git | them → us | trusted |
| a command a product declares — a dependency graph, coverage | them → us | untrusted |
| a repository or a user's files an agent's instructions are read from — instruction files, tool configuration, session records | them → us | untrusted |

## Files left out on purpose

| File | Why |
|---|---|
| README.md | it binds nothing, so no part answers for it (WAY-09) |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| entry-format | withdrawn: the form of an entry is no surface; a product takes it with the commit it pins | none |
| content-fingerprint | withdrawn: no reference carries a fingerprint | none |
| decisions-guard-command | withdrawn: no format guard checks a product's foundation | none |
| run-record-keys | withdrawn: the-way keeps no record of a run | none |
| part-map-guard-command | withdrawn: no format guard checks a product's foundation | none |
| invariants-guard-command | withdrawn: no format guard checks a product's foundation | none |
| environment-facts-guard-command | withdrawn: no format guard checks a product's foundation | none |
| glossary-guard-command | withdrawn: no format guard checks a product's foundation | none |
| guidelines-form-check-command | withdrawn: no script of the-way checks the form of a product's guidelines (WAY-170) | none |
| wording-reaches-dependants | withdrawn: a critical flow has no entry in the map, and no reference carries a fingerprint | none |
| skills-reach-the-way-sessions | withdrawn: a critical flow has no entry in the map; the invariant skill-entry-points and its test hold it | none |
