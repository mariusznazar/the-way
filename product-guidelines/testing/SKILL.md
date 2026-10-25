---
name: maintain-testing-guidelines
description: Use when a product's tests need testing guidelines written before its first test, its existing tests audited for them, or its testing guidelines refreshed or extended — leading those matters of a testing-guidelines task's refinement with the human.
---

# Maintain testing guidelines

Leads the matters of testing guidelines in a task's refinement: it recognizes what the product's
tests already have, gathers the starting set of the guidelines or audits the tests, and settles with
the human every level, recipe, exemplar test, exclusion and invariant the testing guidelines are to
carry, so that the task's cycle can write them from the task document alone. What every file of
guidelines holds stands in `product-guidelines/template.md`; what testing guidelines add, and how
the cycle's author writes their file, in `product-guidelines/testing/template.md`, each rule citing
its decision; how a skill asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/testing/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix.

## Where the skill works

It runs inside the refinement of one task whose outcome is testing guidelines — written, refreshed
or extended — or the exemplar test of a level, a task the product's backlog holds or one opened for
it (WAY-107). `refine-task` opens or resumes the task through its steps 1 and 2; this skill takes
over at its step 3 for the matters of the testing guidelines and hands back to its step 4.
Refinement and the task cycle find applicable and missing guidelines through
`product-guidelines/reading.md`; this skill owns settling their testing-guideline meanings. The task
writing the missing file does not wait for its own output (WAY-215). One task may carry the coding
and the testing guidelines together, each skill leading its own matters in that refinement
(WAY-247). A product that pinned the-way before this skill existed reaches it once a task moves the
pin, as `installation/README.md` gives it.

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the reports of the research under `.runs/testing/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the file `guidelines/testing.md`; the test of each new invariant, seen failing once (WAY-08); the changes to the instruction files and to the part map |
| Never writes | the foundation, the testing guidelines, the product's tests, its code or any other file git tracks, which it leaves as it found them (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## What reaches the task document

The cycle's author was not in the conversation and reads only the document, so what the skill
writes there is written for a reader who was not in it.

- *To do*:
  - write or extend `guidelines/testing.md` from `.the-way/product-guidelines/testing/template.md`,
    as its section "Writing the file" gives;
  - write the test of each new invariant in the product's suite, seen failing once (WAY-08,
    WAY-61);
  - apply `maintain-instruction-files` for the pointer in the product's root `AGENTS.md`, outside
    the block the-way's installer writes: one line naming `guidelines/testing.md` in backticks with
    the condition of writing or changing a test, naming no command (WAY-245, WAY-16);
  - through `update-part-map`, add each part step 1 found missing for the tests the product's plan
    gives (WAY-44);
  - for the product's first guidelines: add `guidelines/**` to the files of the part of the map
    whose files direct whoever carries out its tasks, through `update-part-map` (WAY-167);
  - each item the audit calls for (step 3).
- *Questions to settle*: each choice step 4 settles — the adoption of the testing template and each
  departure from it with its reason, the levels and the glossary terms of their names, the
  documents that are sources of expected values, the fields of each recipe that bind, each level's
  exemplar test, each exclusion with its condition of return, the decisions on permissions the rows
  of the authorization table come from, each AI tool the tests use, and each invariant — each with
  the human's words and date as its source.
- *Context*: what the audit found, each charge with its file and line, a charge the task does not
  take up marked deferred with its reason; for each trust boundary, whether a test of its refusal
  exists; the research's sources, each page with its version; what the audit could not see.
- *Settlements to record*: `refine-task` step 5 builds them through `find-foundation-entries` —
  the product's decisions, its invariants and the environment facts they rest on, the fact of each
  AI tool its tests use among them. A change of the part map is never a row, which is why it stands
  in *To do*.

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a testing-guidelines task of a project plan led by
`lead-project` (WAY-154, WAY-155) — this skill follows that mode's routing. Every question and
every choice shown by its effect go into the conversation turn as `refine-task` routes them, and
the skill ends the turn rather than asking the human. The research agents and the critiques are
requested from the project orchestrator, which starts them, the turn naming the paths of their
reports under `.runs/testing/`. The skill starts no child agent and edits only the task document
and its turn.

## 0. Read

- Read both templates of guidelines in full, `product-guidelines/template.md` and
  `product-guidelines/testing/template.md`; `project-level/task/skill/SKILL.md` and
  `project-level/task/template.md`, whose steps and sections this skill drives; the sections "How
  a skill asks" and "Critique before collective review" of `elements/common/way_of_working.md`; and
  `elements/common/critique/SKILL.md`.
- Read the product's root `AGENTS.md` and every file under `guidelines/`.
- Select and read the product's foundation by "Reading the foundation" in
  `elements/common/way_of_working.md` (WAY-150), including the decisions that settle the product's
  technology, every decision that already adopts a test tool, a level, an exemplar test or an
  exclusion, or departs from the testing template, and the trust boundaries its part map records
  (WAY-48).

## 1. Recognize

- Name the parts of the product's map that have tests: the parts whose code its tests check and the
  parts that hold its test files (WAY-246, WAY-248). Before the first test, name the parts the
  product's plan gives tests; where the map holds no part for them yet, its identifier is a question
  of the task, and *To do* gains adding that part, with the files the task creates, through
  `update-part-map`.
- Find in the product's files what it has for those tests — a test tool, with its configuration and
  version; levels; directories of tests; doubles; tests of invariants; or nothing — and whether it
  has testing guidelines. Say plainly when it has nothing (WAY-248).
- That gives the mode, and modes combine:
  - no tests: the starting set of step 2, so that the testing guidelines come into being before the
    first task that writes the product's tests (WAY-244);
  - tests and no testing guidelines: step 2, and the audit of step 3;
  - a task whose required outcome is the first test of a level: "A new level" in step 3;
  - existing testing guidelines, refreshed or extended: step 2, and step 3, which audits each level
    again.
- Extend what exists: the recipes are written for the test tool the product runs, never for a
  second tool beside it. A new test tool or a library of property tests is a technology choice:
  record it as a question of the task, never settle it (WAY-248, WAY-121).

## 2. Starting set

Before the first test, for tests that have no testing guidelines yet, and at every refresh or
extension (WAY-244, WAY-249):

- Ask, as one question of assessment, for the human's preferences for the product's tests in the
  technology that the product's foundation settles — which levels it has, where their files lie,
  what a test replaces and with what; "I do not know" is an answer.
- Where the human has none, research the starting set for that technology. Split it into the
  questions the set must answer there — how the product's test tool lays out and names the tests of
  each level, what it offers in place of a real dependency, how a test is given the clock and the
  seed it runs with — and give each to a fresh agent of its own, all at once, with the technology,
  the preferences and the binding sentences of the decisions that settle it. Each source is a page
  with its version, never memory and never a fixed list; each report goes to
  `.runs/testing/<question>.md`, the question's name in lower case with hyphens.
- Give one fresh agent, following `critique`, each report with its sources, and ask it to refute
  every claim no source supports — a convention of the tool, a rule, a difference between ways of
  testing. Verify each observation and give your verdict, correct the report by the verdicts, then
  end it with the line `critique: passed`. Where no fresh agent can run, the research does not go
  on: stop and say so (WAY-249, WAY-120). What the research finds is proposed in step 4, never
  imposed.

## 3. Audit

Where the product has tests (WAY-250):

- **Levels** (WAY-242, WAY-250). Name the levels the product's tests already stand at, each with its
  tests; the audit covers every one of them. For each level, judge its tests, compare them, and
  propose:
  - its exemplar test, with one sentence of what the product gains by it, such as "every new
    integration test sets up its data through the fixtures as this one does";
  - three to five charges, each with its file and line and one sentence of its effect, measured
    against the rules of the testing template and those the product holds — such as a test that
    builds the value it expects by calling the function under test, so that it passes whatever the
    code gives. A charge the task does not take up stays in *Context*, marked deferred with its
    reason.
- **Trust boundaries** (WAY-250, WAY-235). For each trust boundary of the product's map, say whether
  a test checks its refusal directly, with that test's file and line, or that none does.
- **A new level.** Where the task's required outcome is itself the first test of a level, that test
  becomes the level's exemplar test, and the level's recipe comes into being with it (WAY-242,
  WAY-241): step 4 settles the level, its recipe and that the task's first test of it becomes the
  exemplar, naming no list of tests and no path (WAY-238). Where the level of a task's tests is
  its cycle's choice, the refinement designates no exemplar test: the cycle's author who writes a
  level's first test proposes its designation at a blocked draft request (WAY-242, WAY-172).
- A choice found in the product's tests — a configuration of the test tool, a habit its tests share
  — is a proposal, never a rule, until the human settles it. An existing choice the human keeps
  becomes a decision whose rationale is the human's words or `unknown`, never one the agent infers
  (WAY-29).

## 4. Settle with the human

- **How to show.** Show each choice by its effect on the product in plain words — "the tests of the
  account server talk to a real database, so a broken query turns them red, at the price of a
  slower run", "a change that loosens what a test checks says what changed in the requirement, or
  the review reads it as hiding a fault" — never by the name of a technique or a tool, with the ways
  open, their cost and a recommendation. Put every choice to the human, a choice the skill
  recommends included, and after a choice that enters a binding part ask the one question "How a
  skill asks" gives. Before first using a term of the field — a level of tests, a double, a
  property test — say in plain words what it means (WAY-174, WAY-113).
- **What it settles.**
  - the product's decision adopting the testing template, and each departure from it by a decision
    with its reason (WAY-173);
  - the levels of the product's tests, each with the decision that sets it; for a level whose name
    means in the product something other than in the field, the entry of the product's glossary
    that defines it by the resources its test may touch; and, for each part the guidelines apply to,
    whether its complexity lies in computation or in its connections (WAY-240, WAY-226);
  - the product's documents that are sources of expected values (WAY-232);
  - for each level, the fields of its recipe that bind, each with the decision that carries it, the
    template's defaults adopted or departed from (WAY-241);
  - for each level with tests, its exemplar test, and for a new level of "A new level", that the
    task's first test of it becomes the exemplar (WAY-242);
  - each category the product deliberately does not test, with the decision that gives its reason
    and the condition under which it is tested again; a trust boundary is never one (WAY-237);
  - the product's decisions on permissions from which the rows of the authorization table come
    (WAY-235);
  - each AI tool the product's tests use, with the environment fact of how it behaves at the version
    the product uses (WAY-236).
- **Invariants.** A binding rule gets an invariant where a cheap test checks it on a convention of
  the product's code; a rule no such test checks gets none, and the review of each change it reaches
  compares the change with it (WAY-168). The rule of trust boundaries always gets its invariants
  (WAY-235). Propose, each with a test of the product's suite (WAY-61):
  - for each trust boundary of the product's map, at least one invariant that the boundary refuses
    crafted input or unauthorised access, its test checking the refusal directly, taking the
    expected refusal from the product's decisions on permissions and seen failing once (WAY-235,
    WAY-08); a boundary that is only the configuration of someone else's service stays with the
    review of each change that touches it (WAY-48);
  - where a boundary does not refuse today, its invariant marked violated by a change of the
    foundation the human accepts, until the boundary refuses (WAY-51); its weak point, that until
    then no test guards the boundary and only the review of each change touching it keeps that
    change from letting more through, is said when it is proposed;
  - for each further rule that a cheap test checks, an invariant that checks it (WAY-168).
- **Weak points.** Name each when its choice is proposed:
  - for an exclusion, that it ages unless someone checks its condition of return whenever a change
    reaches its category (WAY-237);
  - for the rule of trust boundaries, that it is only as good as the part map that names the
    boundaries (WAY-235);
  - for property tests, that a simpler version copied from the code makes a property test a mirror
    of it, which only the review catches (WAY-228).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" gives (WAY-120).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.

## 5. Hand back

- Check that the task document holds what "What reaches the task document" names, and that no
  choice stands settled without the human's words.
- Hand back to `refine-task` step 4. Its step 5 finds the rows of *Settlements to record* through
  `find-foundation-entries` in task mode, with the task document, this conversation and the
  research reports as its source, and its step 6 asks the human to accept the whole document.
