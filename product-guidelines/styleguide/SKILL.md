---
name: maintain-styleguide
description: Use when a product's user interface — its screens, an admin panel added to a backend included — needs a styleguide created before its first screen, audited where screens exist, or refreshed or extended, leading those matters of a styleguide task's refinement with the human.
---

# Maintain a styleguide

Leads the styleguide matters of a styleguide task's refinement: it recognizes what the product's
user interface already has, gathers the starting rules or audits the screens, and settles with the
human every meaning, value and check the styleguide is to carry, so that the task's cycle can write
the styleguide from the task document alone. What every file of guidelines holds stands in
`product-guidelines/template.md`; what a styleguide adds, and how the cycle's author writes its
file, in `product-guidelines/styleguide/template.md`, each rule citing its decision; how a skill
asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/styleguide/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix. The skill uses no Superpowers method: the-way adopts them for the task cycle
alone (WAY-125). What it takes from outside practice, and what it leaves, WAY-175 names; the steps
below describe it in their own words.

## Where the skill works

It runs inside the refinement of one task whose outcome is a styleguide, a task the product's
backlog holds or one opened for it (WAY-107). `refine-task` opens or resumes the task through its
steps 1 and 2; this skill takes over at its step 3 for the styleguide's matters and hands back to
its step 4. Neither `refine-task` nor the task cycle changes for it.

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the research reports under `.runs/styleguide/<part>/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the styleguide's file; the values of design tokens with their sources; the page of every state; the checks of the invariants, by other agents (WAY-69); the changes to the instruction files and to the part map |
| Never writes | the foundation, the styleguide's file, the product's code (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## What reaches the task document

The cycle's author was not in the conversation and reads only the document, so what the skill
writes there is written for a reader who was not in it.

- *To do*:
  - write `guidelines/styleguide-<part>.md` from
    `.the-way/product-guidelines/styleguide/template.md`, as its section "Writing the file" gives,
    and the test cases of each rule as the section "Test cases of a rule" of
    `.the-way/product-guidelines/template.md` gives them (WAY-168), the cases of
    `### No value in place of a design token` read as that section gives for an invariant on the
    list of violated invariants and for the invariant beside it (WAY-190);
  - put the value of each role into the product's file of design tokens with its source, naming for
    each role the value and its source as the human settled them, or the exact address of the
    source and the item in it the value is read from (WAY-182);
  - build the page of every state, or extend it;
  - write a check for each new invariant;
  - apply `maintain-instruction-files` for two changes: a pointer in the product's root
    `AGENTS.md`, outside the block the-way's installer writes, naming
    `guidelines/styleguide-<part>.md` in backticks with the condition of changing a file of
    `<part>`; and the rule against values written in place of design tokens in that part's files,
    standing where that skill places a rule for some files, saying that the product's invariant is
    what keeps it and naming no command of its own (WAY-192);
  - for the product's first guidelines: add `guidelines/**` to the files of the part of the map
    whose files direct whoever carries out its tasks, through `update-part-map`, and write the
    product's copies of the two invariants the template of guidelines gives (WAY-167, WAY-170);
  - where a law or a contract binds the accessibility of the user interface, record at its part,
    through `update-part-map`, the failure mode the human settled for that obligation, its
    detection naming the invariant that rests on the obligation's environment fact (WAY-46);
  - each item an audit charge calls for (step 3).
- *Questions to settle*: each meaning, role, pair, value with its source, rule of states, departure
  from the template and answer on accessibility, each with the human's words and date as its
  source.
- *Context*: the audit's charges with their files and lines, a charge not taken up marked deferred
  with its reason; the research's sources, each page with its version; what the audit could not see.
- *Settlements to record*: `refine-task` step 5 builds them through `find-foundation-entries` —
  the product's decisions, invariants and the environment facts they rest on. A change of the part
  map is never a row, which is why it stands in *To do*.

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a styleguide task of a project plan led by
`lead-project` (WAY-154, WAY-155) — this skill follows that mode's routing. Every question, the
proposal on accessibility and every choice shown through what the user sees go into the
conversation turn as `refine-task` routes them, and the skill ends the turn rather than asking the
human. The research agents and the critiques are requested from the project orchestrator, which
starts them, the turn naming the paths of their reports under `.runs/styleguide/<part>/`. The skill
starts no child agent and edits only the task document and its turn.

## 0. Read

- Read both templates of guidelines in full; `project-level/task/skill/SKILL.md` and
  `project-level/task/template.md`, whose steps and sections this skill drives; the sections "How
  a skill asks" and "Critique before collective review" of `elements/common/way_of_working.md`; and
  `elements/common/critique/SKILL.md`.
- Read the product's root `AGENTS.md` and every file under `guidelines/`.
- Select and read the product's foundation by "Reading the foundation" in
  `elements/common/way_of_working.md` (WAY-150), including the decisions that settle the technology
  of the user interface and the agent's way to the running product (WAY-165), and every decision
  that already gives a role its meaning, a value its source or the styleguide a departure.

## 1. Recognize

- Name the user interface: the part of the map whose files draw it. A product whose users reach it
  only through an API or a terminal has no user interface in this sense; say so and end (WAY-183).
  Every other user interface gets a styleguide of its own, however simple, an admin panel added to
  a backend included; where the product has several, the human says which this task covers. Where
  the map holds no part for it yet, as before a first screen, its identifier is a question of the
  task, and *To do* gains adding that part, with the files the task creates, through
  `update-part-map`.
- Read off what the product has for it — a file of design tokens its screens read, one nothing
  reads, shared components, or nothing — whether it has screens, and whether a styleguide exists.
  Say plainly when it has nothing (WAY-185, WAY-175).
- That gives the mode: no screens, the starting rules of step 2; screens and no styleguide, the
  audit of step 3; an existing styleguide, its refresh or extension — step 2, and step 3 where
  screens changed since the styleguide was written.
- Extend what exists. A new library of components or a new way of styling is a technology choice:
  record it as an open question of the task, never settle it (WAY-185, WAY-121).

## 2. Starting rules

Before the first screen, and at every refresh or extension (WAY-184, WAY-186):

- Ask, as one question of assessment, for the human's preferences for styling in the technology of
  the user interface that the product's foundation settles; "I do not know" is an answer.
- Where the human has none, and at every refresh or extension, research the basic rules of a
  styleguide for that technology. Split it into the questions the starting set must answer there —
  how the technology names and pairs colour roles, how it draws focus, how its controls show their
  states — and give each to a fresh agent of its own, all at once, with the technology, the
  preferences and the binding sentences of the decisions that settle it. Each source is a page with
  its version, never memory and never a fixed list; each report goes to
  `.runs/styleguide/<part>/<question>.md`, the question's name in lower case with hyphens.
- Give one fresh agent, following `critique`, each report with its sources, and ask it to refute
  every claim no source supports — a rule, or a difference between ways of following one. Verify
  each observation and give your verdict, correct the report by the verdicts, then end it with the
  line `critique: passed`. Where no fresh agent can run, the research does not go on: stop and say
  so (WAY-186, WAY-120). What the research finds is proposed in step 4, never imposed.
- Add the product's own meanings: from its definition, plan, specs and mockups, describe each
  screen the product announces — what the user sees, the components it is built from, and its
  states with the messages the user reads. A mockup shows what a screen holds; the meaning of a
  colour on it is settled with the human, never read off it (WAY-179).
- The starting set covers the roles, states and focus the announced screens need, so it is wider
  than the first task that uses it (WAY-184).

## 3. Audit

Where the user interface has screens (WAY-187):

- Audit in both directions: from the source of values to the screens that read it — a file of
  design tokens nothing reads is a charge — and from each value on a screen to the design token or
  shared component meant to cover it.
- Ask every time what someone sees without data, straight from a link, after a refresh.
- Where the product's foundation settles the agent's way to the running product, open the screens
  that way; otherwise audit from the code and mark as unchecked what cannot be seen without the
  running product, such as whether focus shows.
- End with three to five charges, each with its file and line and one sentence of its effect on the
  user, each in one category: a missing design token, a missing shared component, accidental
  architecture, or a meaning — one colour carrying several. A charge the task does not take up
  stays in *Context*, marked deferred with its reason.
- A palette read off the code is a proposal, never a rule, until the human settles it (WAY-175). An
  existing choice the human keeps becomes a decision whose rationale is the human's words or
  `unknown`, never one the agent infers (WAY-29).

## 4. Settle with the human

- **How to show.** Show each choice by what someone using the product sees — "the button that saves
  stands out; the one that deletes is red, and its text white" — never by the names or values of
  design tokens, with the ways open, their cost and a recommendation. Put every choice to the human,
  a choice the skill recommends included, and after a choice that enters a binding part ask the one
  question "How a skill asks" gives. Before first using a term of the field — contrast, focus, a
  state of a control — say in plain words what it means (WAY-174, WAY-113).
- **What it settles.** The roles of the table the styleguide template gives, each row settled with
  the human, its value and the value's source among them; the states of the shared controls; the
  page of every state; the meanings grouped into decisions as that template's section "Pairs,
  meanings and role names" gives; the product's decision adopting the template, and each departure
  from it by a decision with its reason (WAY-173). Ask also what no reading of the code can tell:
  the names the team uses, the exceptions it keeps on purpose (WAY-175).
- **Accessibility.** First ask whether a law or a contract binds the accessibility of the user
  interface: what one requires is an environment fact, and no adoption is needed (WAY-86). Such an
  obligation also stands as a failure mode of the user interface's part, its kind of damage and
  severity given by the human and its detection naming the invariant that rests on that fact; it
  reaches the map through *To do* (WAY-46). Then propose the decision adopting WCAG, recommending
  the newest edition that is a W3C Recommendation when the decision is written, named by its number
  as read on the W3C's page in this session, never from memory, at level AA, for every screen of the
  user interface; propose another way only where the human chooses it, and write nothing the human
  has not accepted (WAY-191, WAY-80). Each success criterion an invariant takes a condition from —
  contrast and visible focus at least — becomes an environment fact, with the edition's address and
  the passage word for word (WAY-191, WAY-76).
- **Which criterion, which ratio.** Put to the human, as a question with a recommendation shown by
  what the user sees — "small text on any background stays readable for someone who sees less
  well" — the criterion of the adopted edition each invariant takes its condition from, and the one
  ratio the contrast script holds every pair of a background and its text to, read from that
  criterion's passage: the stricter one wherever the size of the text on a pair is not known.
  Record both with the facts of WCAG, so that the invariant's condition stands in a decision and
  its fact (WAY-60, WAY-191).
- **Invariants.** Every binding rule gets an invariant of the kind the styleguide template's
  required form gives, and a rule no invariant can check goes among the examples (WAY-188). Propose,
  each script a command the product declares (WAY-38):
  - for each rule the styleguide template requires, the invariant its item under "What each section
    carries" names — among them the first ones WAY-189 gives: by a script, no value written in place
    of a design token, visible focus on every control, and the contrast of every pair of a
    background and its text; by an agent, each role in its meaning;
  - the product's decision that the rule against values written in place of design tokens names,
    which says what counts as such a value, so that the invariant's condition stands in a decision
    (WAY-60);
  - where the human chooses to clean the screens as tasks touch their styles rather than in one
    clean-up, the second invariant WAY-190 gives, while the full one stands on the list of violated
    invariants by a foundation change the human accepts (WAY-190, WAY-51); its weak point, a
    renamed file that looks new, is said when it is proposed;
  - for each further rule of the product, an invariant that checks it.
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" gives (WAY-120).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.

## 5. Hand back

- Check that the task document holds what "What reaches the task document" names, and that no
  meaning stands settled without the human's words.
- Hand back to `refine-task` step 4. Its step 5 finds the rows of *Settlements to record* through
  `find-foundation-entries` in task mode, with the task document, this conversation and the
  research reports as its source, and its step 6 asks the human to accept the whole document.
