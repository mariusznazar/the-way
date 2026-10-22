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
it is today, including the rules it does not yet meet. A task that changes the foundation does so
on its own branch, and the foundation change and the code reach the main branch in the same merge;
the human accepts both by merging. A task that only brings code into line with an existing rule
changes no rule; its return step still corrects what the change touches, and the change in which
the rule's test starts to pass clears its *Violated* mark. Each entry says what binds today and is
edited in place; git keeps its history.

The process is designed to give a product:

- a foundation that matches the product: after each change its author compares the entries the
  change touches with the code and corrects them in the same change, and a rule the product does
  not meet today is marked openly;
- references by identifier alone: when an entry changes, its author searches the foundation for
  the entries the change touches and corrects them in the same change, and every reference names
  an entry that exists;
- decisions that say what binds today: each has one place, with its reason and the options it
  rejected, and where two collide, which one prevails is written;
- glossary entries for the words that mean in the product something other than usual; when such a
  meaning changes, the author corrects the texts that use the word;
- rules whose status comes from running their checks, never from a status written by hand: an
  invariant is checked by a test in the product's own suite, and a rule no cheap test can check is
  kept by review;
- the product's tests and a review by an agent that did not make the change, against the task and
  the foundation's sentences, for every change; a change that touches a trust boundary or holds an
  operation that cannot be undone gets a review aimed at that risk, and a human performs that
  operation;
- sources outside the product that a rule rests on, recorded with their address, the passage
  quoted word for word and the date it was read; the foundation says no more than its sources, and
  what is not known stands as unknown or goes to a human as a question;
- promises to someone outside the product — an API, a file format, a command — named in the part
  map with who relies on them, and named in the request of a change that alters them;
- an agent that reads the foundation entries and guidelines of the parts its change touches, and a
  task that names the decisions concerning it.

The foundation holds rules and a description of the product's state that the return step compares
with the code; a detail that changes with every change of the code lives in the code or in a test.

A product uses one pinned commit of this repository, so a new version of the process reaches the
product only when the product moves the pin; `installation/README.md` describes how.

## The five files of a foundation

| File | What it holds | The problem it solves |
|---|---|---|
| `decisions.md` | Choices that bind later work, one entry for each, edited in place, with its scope, the sources it rests on, the decisions it narrows or derives from, the invariants that check it, its rationale and the options it rejected | A later change reads what binds today and why, without treating a rejected option as open; where two decisions collide, the entry says which prevails. |
| `invariants.md` | Rules the product must keep, each one sentence with its method — `test` or `review` — the decisions or sources it derives from, the facts it rests on, the parts in which a change can break it, and the mark *Violated* | A rule is checked by a test in the product's own suite or by review, not by a status written into the entry. |
| `part_map.md` | Parts with their files, the parts each may depend on and its trust boundary, and surfaces: promises to someone outside the product, with who relies on each | A change finds the parts it touches and the rules that reach them; a change at a trust boundary gets a review aimed at that risk, and one that alters a surface is named in its request. |
| `environment_facts.md` | Facts about the world outside the product that a rule rests on, each one sentence with its source: the address, the passage quoted word for word and the date it was read | A rule's outside premise can be compared with its source again when the world changes. |
| `glossary.md` | Words that mean in the product something other than a reader of its field takes them to mean, each with a definition of one sentence and the meanings it no longer carries | A changed meaning reaches the sentences that use the word, through the author of the change. |

Where the product does not meet a rule today, its invariant reads `Violated: yes` openly, instead
of the rule being weakened, and its test stands in the product's suite as an expected failure.
`elements/common/foundation_check.py` checks that every identifier stands once, every reference
names an existing entry, every entry has the fields its template gives, and every file belongs to
one part.

## What else is here

- `foundations/` — the foundation of the-way itself: the process is built by its own rules.
- `elements/<element>/` — for each file above: the form of an entry, the entries of the-way's own
  foundation that show it, and the skill that writes an entry.
- `elements/common/` — what the five elements share: the rules of form their entries keep, the way
  of working their skills share, the script that checks a whole foundation, a script that brings a
  foundation of the earlier form to the current one, the skill that finds candidate entries in a
  source, and the critique skill, which reads a proposal critically before the human sees it.
- `relation-model/` — computes a short fingerprint of a text, with which a project plan notices that
  the project definition it was written from has changed.
- `gate/` — the one command that runs every test of the-way.
- `installation/` — prepares a product repository to use one pinned commit of the-way; see
  `installation/README.md`.
- `project-level/` — defines a project, settles its technology, breaks it into a plan of tasks,
  leads a handed-over plan, and refines its tasks before their implementation cycles.
- `task-cycle/` — takes one ready task to a request for human review on the-way's own methods: a
  spec where the task leaves a design choice open (`write-spec`), a plan of slices where the change
  needs dividing (`plan-task`), the change made by one author or slice by slice (`make-change`),
  each reviewed by an agent that did not make it (`review-change`), the product's full tests and
  the return step. It keeps the cycle record on the task branch, with the time, models and tokens
  of each stage counted from the agents' session transcripts.
- `agent-instructions/`, with `AGENTS.md` and `CLAUDE.md` at the root and the skill entry points in
  `.claude/skills/` and `.agents/skills/` — instructions for agents working on the-way itself, and
  the script that generates those entry points.
- `instruction-files/` — the principles by which instruction files for coding agents are written,
  judged and kept, how Claude Code, Codex and Cursor load them, the skill that applies them, and
  the script that checks instruction files.
- `product-guidelines/` — the form every product's guidelines share, how an agent reads the
  guidelines of the parts it touches, and the template of each discipline of guidelines with the
  skill that leads the work on them (the styleguide's in `product-guidelines/styleguide/`, the
  coding guidelines' in `product-guidelines/coding/`).

## Using the skills

Each element's `skill/` directory, `elements/common/skill/` and `elements/common/critique/`, the
project level's skill directories, `task-cycle/skill/`, `task-cycle/spec/`, `task-cycle/plan/`,
`task-cycle/change/`, `task-cycle/review/`, `instruction-files/`, `product-guidelines/styleguide/`
and `product-guidelines/coding/` hold one skill, named in its `SKILL.md`.

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

## Running the tests

Every test of the-way runs with one command, from the root of the repository:

```bash
python -B gate/run_tests.py
```

It ends with a line counting the tests and naming each directory that failed, and its exit code is 0
only when every test passes. `python -B gate/run_tests.py <directory>` runs the tests of one
directory. The foundation of the-way is checked by one of these tests, and on its own by:

```bash
python -B elements/common/foundation_check.py
```
