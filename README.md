# the-way

This repository is written in English.

the-way is a process for work on a technology product in which a change of premises or direction
is an ordinary step: it passes through the product's foundation and needs no memory of what is
linked to what. It is built first for its author and aims at anyone who builds a technology
product and adopts the process for their own needs; it is written for the AI agents that carry out
the task cycle too.

## The problem

When every change gets its own specification, the specifications pile up and nobody reads them
again. In one reported case, 238 specifications written over nine months were never reopened, and
the agent could not tell which of them still held
(https://www.alfredo-perez.dev/blog/2026-08-31-i-wrote-238-specs-and-never-read-one-again).
Documentation that nobody keeps up to date only looks like safety.

## The idea

A product keeps one set of foundation files that, on its main branch, describes the product as
it is today, including the rules it does not yet meet. A task that sets out to change the
foundation does so on its branch before the code follows, and both reach the main branch in the
same merge. A task that only brings code into line with an existing rule needs no foundation
change. Rules are checked through invariants, an agent comparison or a human assessment, as
their entries specify; a missing result never counts as a pass.

The process is designed to give a product:

- a foundation that describes its current state and lists the rules it does not yet meet as
  explicit debt;
- references that carry a fingerprint of the wording they rely on, so a change to that wording
  sends those references for review before it is merged;
- decisions whose current answer, approver, reasoning and rejected options remain readable;
- checks selected by the parts a change touches and by the methods written with the rules, where
  a missing verdict never counts as a pass;
- sourced facts about the world and dated predictions that return for review when their
  conditions change.

A product uses one fixed commit of this repository, so a new version of the process reaches the
product only when it moves to a newer commit.

## The five files of a foundation

| File | What it holds | The problem it solves |
|---|---|---|
| `decisions.md` | Choices that bind later work, with their scope, verification, review condition, approver, rationale and rejected options | A later change can read what applies now, who approved it and why, without treating an old option as open. |
| `invariants.md` | Rules the product must keep, each with a method of checking it and links to the decisions or facts it depends on | A rule has a way to be checked; the result comes from a run or a human verdict, not from a status copied into the entry. |
| `part_map.md` | Parts and their files, allowed dependencies, failure modes, critical flows and promises to outsiders | A change can find the rules it reaches and the level of care its affected parts require. |
| `environment_facts.md` | Sourced facts outside the product, each with the range where it holds and a way to check it again | A rule's external premise can be revisited when the world changes. |
| `glossary.md` | Terms used by the foundation, each with one definition and any words or meanings to avoid | A changed meaning reaches the sentences that use the term. |

Where the product does not meet a rule today, `violated_invariants.md` lists it openly as debt,
instead of the rule being weakened.

## What else is here

- `foundations/` — the foundation of the-way itself: the process is built by its own rules.
- `elements/<element>/` — for each file above: the form of an entry, real examples, a Claude Code
  skill that writes an entry, and a script that checks the file.
- `elements/common/` — what the five elements share: the rules of form their entries keep, the way
  of working their skills share, the code their checking scripts share, a script that checks the
  whole foundation — each identifier stands once, each reference names an existing entry, each
  file belongs to one part — and the critique skill, which reads a proposal critically before the
  human sees it.
- `relation-model/` — computes a short fingerprint of an entry's wording, so that anything pointing
  to the entry learns when the wording changed.
- `gate/` — runs the tests and records, for each rule, whether it held.
- `probes/` — scripts that check the environment facts again.
- `installation/` — prepares a product repository to use one pinned commit of the-way; see
  `installation/README.md`.
- `project-level/` — defines a project, settles its technology, breaks it into a plan of tasks, and
  refines its tasks before their implementation cycles.
- `task-cycle/` — orchestrates one ready task through design, implementation, checks, reviews and
  a request for human review; it keeps the cycle record on the task branch, with the time, models
  and tokens of each stage counted from the agents' session transcripts.
- `agent-instructions/`, with `AGENTS.md` and `CLAUDE.md` at the root and the skill entry points in
  `.claude/skills/` and `.agents/skills/` — instructions for agents working on the-way itself, and
  the script that generates those entry points.
- `instruction-files/` — the principles by which instruction files for coding agents are written,
  judged and kept, how Claude Code, Codex and Cursor load them, the skill that applies them, and
  the script that checks instruction files.
- `product-guidelines/` — the form every product's guidelines share, the template of each
  discipline of guidelines with the skill that leads the work on them (the styleguide's in
  `product-guidelines/styleguide/`, the coding guidelines' in `product-guidelines/coding/`), and the
  form check of guidelines.

## Using the skills

Each element's `skill/` directory, `elements/common/skill/` and `elements/common/critique/`, the
project level's skill directories, `task-cycle/skill/`, `instruction-files/`,
`product-guidelines/styleguide/` and `product-guidelines/coding/` hold one skill, named in its
`SKILL.md`.

A Claude Code or Codex session working in a checkout or worktree of the-way finds each of them as
the project skill `the-way-<name>`: `.claude/skills/` holds the entry points Claude Code reads and
`.agents/skills/` the identical ones Codex reads, and each entry point reads its skill from the
checkout or worktree the session works in. They are generated; after adding, renaming or
moving a skill, or changing its description, run:

```bash
python -B agent-instructions/skill_entry_points.py --write
```

and commit what it writes. A product gets the same skills, pointing to its pinned `.the-way`, from
the installer; see `installation/README.md`.
