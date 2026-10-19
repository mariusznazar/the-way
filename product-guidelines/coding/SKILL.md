---
name: maintain-coding-guidelines
description: Use when a product's code needs coding guidelines written before its first code, its existing code audited for them, an exemplar settled for a kind of code, or its coding guidelines refreshed or extended — leading those matters of a coding-guidelines task's refinement with the human.
---

# Maintain coding guidelines

Leads the matters of coding guidelines in a task's refinement: it recognizes what the product's code
already has, gathers the starting set of standing checks or audits the code, and settles with the
human every standing check, exemplar and invariant the coding guidelines are to carry, so that the
task's cycle can write them from the task document alone. What every file of guidelines holds
stands in `product-guidelines/template.md`; what coding guidelines add, and how the cycle's author
writes their files, in `product-guidelines/coding/template.md`, each rule citing its decision; how
a skill asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/coding/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix. The skill uses no Superpowers method: the-way adopts them for the task cycle
alone (WAY-125). What it takes from outside practice, and what it leaves, WAY-195 names; the steps
below describe it in their own words.

## Where the skill works

It runs inside the refinement of one task whose outcome is coding guidelines — written, refreshed
or extended — or the exemplar of a kind of code, a task the product's backlog holds or one opened
for it (WAY-107). `refine-task` opens or resumes the task through its steps 1 and 2; this skill
takes over at its step 3 for the matters of the coding guidelines and hands back to its step 4.
Neither `refine-task` nor the task cycle changes for it. A product that pinned the-way before this
skill existed reaches it once a task moves the pin, as `installation/README.md` gives it.

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the reports of the research and of the trial run under `.runs/coding/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the files of the coding guidelines with the test cases of their rules; each adopted tool, installed and configured; the one reformatting of the code where the task settles it; the checks of the invariants, by other agents (WAY-69); the changes to the instruction files and to the part map |
| Never writes | the foundation, the coding guidelines, the product's code or any other file git tracks, which it leaves as it found them (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## What reaches the task document

The cycle's author was not in the conversation and reads only the document, so what the skill
writes there is written for a reader who was not in it.

- *To do*:
  - write or extend `guidelines/coding.md`, and `guidelines/coding-<kind>.md` for each kind whose
    exemplar the task settles, from `.the-way/product-guidelines/coding/template.md`, as its section
    "Writing the files" gives, and the test cases of each rule as the section "Test cases of a
    rule" of `.the-way/product-guidelines/template.md` gives them, its limit on the lines of a case
    that open a fence included;
  - install and configure the tool of each standing check the task adopts, at the version, with the
    set and for the parts the task settles, as the coding template's section "The tools of the
    standing checks" gives;
  - where the task brings a formatter to code it would rewrite, reformat the whole of the code once
    (WAY-205);
  - write a check for each new invariant, by agents other than the author of the code it covers
    (WAY-69), each script reading a test case that stands at a new path within the parts it reads,
    as the coding template's item "Test cases of the standing checks" gives;
  - apply `maintain-instruction-files` for the pointer in the product's root `AGENTS.md`, outside
    the block the-way's installer writes: one line naming `guidelines/coding.md` in backticks with
    the condition of changing the product's code, naming no file of a kind and no command of its
    own (WAY-212, WAY-16);
  - through `update-part-map`, give the configuration files of the standing checks to the part of
    the product's map that holds its build configuration, and add each part step 1 found missing
    for code the task brings (WAY-44);
  - for the product's first guidelines: add `guidelines/**` to the files of the part of the map
    whose files direct whoever carries out its tasks, through `update-part-map`, and write the
    product's copies of the two invariants the template of guidelines gives (WAY-167, WAY-170);
  - each item the audit calls for (step 3).
- *Questions to settle*: each choice step 4 settles — every standing check adopted or departed
  from with its reason, each tool, set and edition, the parts, the audit's database and severity,
  the split of the set, each kind's exemplar and the status of its files, the rules a script checks
  of each exemplar, each invariant with its kind of check, and the way the list of rules that block
  is kept — each with the human's words and date as its source.
- *Context*: the trial run's evidence — how many reports each rule gave and what the judging
  agent found of them, with the paths of the output and of its verdicts; what the audit found, each
  `do not copy` file with its file and line, a finding the task does not take up marked deferred
  with its reason; the research's sources, each page with its version; what the audit or the trial
  run could not see.
- *Settlements to record*: `refine-task` step 5 builds them through `find-foundation-entries` —
  the product's decisions, its invariants and the environment facts they rest on, the fact of each
  adopted set's edition among them. A change of the part map is never a row, which is why it stands
  in *To do*.

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a coding-guidelines task of a project plan led by
`lead-project` (WAY-154, WAY-155) — this skill follows that mode's routing. Every question and
every choice shown by its effect go into the conversation turn as `refine-task` routes them, and
the skill ends the turn rather than asking the human. The research agents, the critiques and the
fresh agent that judges the trial run's reports are requested from the project orchestrator, which
starts them, the turn naming the paths of their reports under `.runs/coding/`. The skill starts no
child agent and edits only the task document, its turn and the trial run's output under
`.runs/coding/`.

## 0. Read

- Read both templates of guidelines in full, `product-guidelines/template.md` and
  `product-guidelines/coding/template.md`; `project-level/task/skill/SKILL.md` and
  `project-level/task/template.md`, whose steps and sections this skill drives; the sections "How
  a skill asks" and "Critique before collective review" of `elements/common/way_of_working.md`; and
  `elements/common/critique/SKILL.md`.
- Read the product's root `AGENTS.md` and every file under `guidelines/`.
- Select and read the product's foundation by "Reading the foundation" in
  `elements/common/way_of_working.md` (WAY-150), including the decisions that settle the product's
  technology, and every decision that already adopts a standing check, a set of rules or an
  exemplar, or departs from one.

## 1. Recognize

- Name the parts of the product's map that hold code, the scripts of its build included, however
  small (WAY-208). Before the first code, name the parts the product's plan gives that code; where
  the map holds no part for it yet, its identifier is a question of the task, and *To do* gains
  adding that part, with the files the task creates, through `update-part-map`.
- Find in the product's files what it has for that code — a linter, a formatter, an audit of
  dependencies, each with its configuration and version; kinds of code it already holds files of,
  such as endpoints, migrations or modules; or nothing — and whether it has coding guidelines. Say
  plainly when it has nothing (WAY-210).
- That gives the mode, and modes combine:
  - no code: the starting set of step 2, so that the general file with its standing checks comes
    into being before the first task that writes the product's code (WAY-209);
  - code and no coding guidelines: step 2, and the trial run and the audit of step 3;
  - a task that creates the first file of a kind of code: "A new kind" in step 3;
  - existing coding guidelines, refreshed or extended: step 2, and step 3, which tries the set and
    audits each kind again.
- Extend what exists: rules are added to the linter the product runs, never a second linter beside
  it. A new linter, formatter or audit of dependencies is a technology choice: record it as a
  question of the task, never settle it (WAY-210, WAY-121).

## 2. Starting set

Before the first code, for code that has no coding guidelines yet, and at every refresh or extension
(WAY-209, WAY-210, WAY-211):

- Ask, as one question of assessment, for the human's preferences for the standing checks and their
  sets of rules in the technology that the product's foundation settles; "I do not know" is an
  answer. A tool the human prefers is the one proposed, and no other is offered in its place
  (WAY-211).
- Where the human has none, and at every refresh or extension, research each standing check for
  that technology, giving each to a fresh agent of its own, all at once, with the technology, the
  preferences and the binding sentences of the decisions that settle it: the tools used for it,
  which of them is most used in that technology — the default recommendation (WAY-210) — the sets
  of rules a linter offers with the rules its documentation marks as recommended, and the advisory
  databases an audit reads. Each source is a page with its version, never memory and never a fixed
  list; each report goes to `.runs/coding/<question>.md`, the question's name in lower case with
  hyphens.
- Give one fresh agent, following `critique`, each report with its sources, and ask it to refute
  every claim no source supports — a tool's use, a rule, a difference between tools. Verify each
  observation and give your verdict, correct the report by the verdicts, then end it with the line
  `critique: passed`. Where no fresh agent can run, the research does not go on: stop and say so
  (WAY-211, WAY-120). What the research finds is proposed in step 4, never imposed.
- For a product with no code, the rules proposed to block are those the linter's documentation
  marks as recommended, as the research reads them: there is no code to try them on (WAY-204).

## 3. Trial run and audit

Where the product has code:

- **Trial run** (WAY-204). Run the linter's set — the one the product runs with the rules the
  research of step 2 proposes adding, or the one step 2 proposes — at the version the research or
  the product's files give, on the product's code in a scratch worktree of its commit or in a
  temporary environment, outside its working tree: the tool is installed only there, never into a
  file git tracks, and the scratch worktree is removed afterwards. Its output goes to
  `.runs/coding/`.
- Give one fresh agent that wrote none of that code each report with the code it points to, and
  ask it to judge whether the report leads to a change of code worth making, whether the report is
  technically right or not; its verdicts go beside the output. A rule with one report that leads to
  no such change goes among the examples, and the rest of the set blocks. Where the set cannot run
  there, or no fresh agent can judge, no split is proposed: stop and say so. The split goes to
  step 4 with its evidence.
- In the same place, count the files that break the rules that block and the files the formatter
  would rewrite: where the code breaks those rules, step 4 proposes the pair of invariants of
  WAY-205; where the formatter would rewrite it, the one reformatting of the whole of the code
  (WAY-205).
- **Kinds** (WAY-200, WAY-201). Name the kinds of code the product already holds files of, each
  with its files; the audit covers every one of them. For each kind, judge every file of it the
  product holds, compare them, and propose:
  - its exemplar, with one sentence of what the product gains by it, such as "every new endpoint
    checks its input as this one does";
  - what a script can check of that exemplar — where a file of the kind lies, what it calls, how it
    validates its input — as the kind's rules, the rest of the exemplar standing as an example
    (WAY-198);
  - `do not copy` for each file that breaks a rule the product holds or the task settles, with the
    file and line of the place that breaks it, and `copy` for every other file of the kind.
- **A new kind.** Where the task creates the first file of a kind of code, that file is the kind's
  exemplar, and its file of guidelines comes into being with it (WAY-200, WAY-209): step 4 settles
  the kind's identifier, the path the file takes and the rules a script checks of it.
- A choice found in the product's files — a tool's configuration, a habit its files share — is a
  proposal, never a rule, until the human settles it. An existing choice the human keeps becomes a
  decision whose rationale is the human's words or `unknown`, never one the agent infers (WAY-29).

## 4. Settle with the human

- **How to show.** Show each choice by its effect on the product in plain words — "a change that
  adds a library with a known security hole does not get in", "every new endpoint checks its input
  as the exemplar does" — never by the name of a linter's rule or a value of a tool's
  configuration, with the ways open, their cost and a recommendation. Put every choice to the
  human, a choice the skill recommends included, and after a choice that enters a binding part ask
  the one question "How a skill asks" gives. Ask for decisions, never for single rules: a set of
  rules is adopted whole, its split shown as "this many rules will block a change; these few
  flagged sound code here and stay as examples", each of the few shown by what it flagged. Before
  first speaking of a linter, a formatter or an audit of dependencies, say in plain words what it
  does for the product (WAY-194, WAY-113).
- **What it settles.**
  - for each standing check, the product's decision adopting it or departing from it with its
    reason; the task is not ready without one for each (WAY-202);
  - for the linter, its tool, its set, the set's edition, the parts it reads and the split of the
    set, said together with what the split means later: a fault of one file is fixed in that file,
    and turning a rule off for the whole product takes a change of this decision, approved by the
    human (WAY-203, WAY-204, WAY-207);
  - for the formatter, its tool and its configuration;
  - for the audit of dependencies, its tool, the advisory database it reads and the severity from
    which a vulnerability counts, every severity among the ways (WAY-206);
  - for each kind the product holds files of, and each new kind, its exemplar, the status of each
    of its files and the rules a script checks of the exemplar (WAY-198, WAY-199, WAY-200,
    WAY-201);
  - the product's decision adopting the coding template, and each departure from it by a decision
    with its reason (WAY-193).
- **Invariants.** Every binding rule gets an invariant of the kind the coding template's required
  forms give, and a rule no such invariant can check goes among the examples (WAY-196). Propose,
  each script a command the product declares (WAY-38):
  - for the rule of each standing check, the invariants the coding template's section "What each
    section carries" names for it, with the parts it gives them;
  - for the linter, which way of keeping the list of rules that block applies — its first invariant
    passing the list to the tool, or a second invariant keeping the product's configuration to the
    list — by what the tool allows (WAY-207);
  - where the code breaks the rules that block, the second invariant WAY-205 gives, while the full
    one stands on the list of violated invariants by a foundation change the human accepts
    (WAY-205, WAY-51); its weak point, a renamed file that looks new, is said when it is proposed;
  - for each rule of an exemplar and each further rule of the whole product, an invariant that
    checks it.
- **Weak points.** Name each when its choice is proposed:
  - for a product with no code, that the recommended rules block with no evidence from the
    product's code, and that the first report of one that leads to no change worth making takes it
    among the examples by a change of the decision, which the human approves (WAY-204);
  - for the audit of dependencies, that a vulnerability found in a dependency the product already
    holds gives no signal while no change brings in a version of it, and that a later run on the
    same commit can fail where an earlier one passed, once an advisory is published for a version
    that commit brings in (WAY-206).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" gives (WAY-120).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.

## 5. Hand back

- Check that the task document holds what "What reaches the task document" names, that each
  standing check has its adopting or departing decision among the choices settled (WAY-202), and
  that no choice stands settled without the human's words.
- Hand back to `refine-task` step 4. Its step 5 finds the rows of *Settlements to record* through
  `find-foundation-entries` in task mode, with the task document, this conversation and the
  research and trial-run reports as its source, and its step 6 asks the human to accept the whole
  document.
