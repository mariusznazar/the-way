# Principles of instruction files for agents

How to write, judge and maintain the files from which an agent takes its rules of work —
`CLAUDE.md`, `AGENTS.md`, `.claude/rules/`, `.cursor/rules/*.mdc`, skills and hooks — in Claude
Code, Codex and Cursor at once. The skill in `SKILL.md` beside this file applies these principles;
the sources they rest on are listed at the end. Where the-way has adopted a principle by a
decision, the principle names that decision in brackets.

## 1. Ways in and routes

An agent receives rules in two ways: through a **way in** — what brings it into a piece of work —
and along a **route** — the steps of that work, each of which tells it plainly which file to read,
which file to write its output to, and where the work goes next. On a route the model does not
choose; it carries out the step. The choice is concentrated at the way in.

| Who opens the way in | Carriers | When it works | Cost in context |
|---|---|---|---|
| **a human, directly** | invoking `/skill` | always | none until invoked |
| **a human describes the task, the model matches a skill** | a skill chosen by its description, a Cursor rule with only a description | when the request plainly points to the skill; weaker when many options cover similar ground | the description always, the body once chosen |
| **the tool, at session start** | the main file, an `@path` import in Claude Code, a rule without `paths`, a Cursor rule with `alwaysApply: true` | always | in every session |
| **the tool, on an event** | a rule with `paths` or a glob, an instruction file in a subdirectory (event: access to a file); a hook (event: a command being run) | when the event happens | only then |

What follows from this:

- **The main file sketches the surroundings and points to the ways in.** A rule needed during an
  activity does not hang loose waiting for the agent to discover it — it lives on the step of the
  route that needs it.
- **Matching by description fails in two situations.** When many options cover similar ground (an
  orchestrator choosing from a wide pool), a stronger model or a narrower choice helps. When the
  need does not follow from the request, because the agent does not know it lacks some knowledge
  or a local convention, a rule on the step of the route or in the main file helps; a stronger
  model does not.
- **A step of a route points directly and one level deep** (step → file), and the state between
  steps lives in a file, not in the conversation. A file referenced from a referenced file is
  sometimes read only in part, the conversation is summarised when it is compacted, and a skill in
  Codex does not carry over to the next turn unless it is named again — a file survives each of
  these.
- **Loaded is not yet carried out.** A rule present in context is not always followed. What must
  happen every time goes into a CI check, a linter or a check of a step's output, and into a local
  hook only against slips (WAY-133). When a step ends with an output — a document, code — the
  output is checked against what it was meant to contain, and if something is missing the work goes
  back one step. Checking the output catches both a rule that never arrived and a rule that arrived
  but was not followed.

The same line can travel a different way in each of the three tools: `@path` in Claude Code loads
the file at session start, in Cursor it is a hint to the model, in Codex it is plain text; Claude
Code and Cursor load a file in a subdirectory on access to a file there, Codex only on the chain
from the repository root to the directory where the session started. That is why a rule meant for
several tools uses the shared layout (section 4).

## 2. What the main file holds

The main file is the file the tool adds to every session: `CLAUDE.md`, `AGENTS.md`, a Cursor rule
with `alwaysApply: true`, the user's global file. Each of its lines costs context in every session
and — when it is a requirement — extra steps of the agent, because agents carry out instructions.
A line stays when it meets three conditions at once (WAY-128):

1. **it is needed in every session** — or it points to a way in that would not be found otherwise;
2. **the agent cannot read it** from the repository or from general knowledge;
3. **without it the agent makes a mistake** — the test question: would something go wrong if this
   line were removed?

The main file holds three kinds of content:

- **Surroundings the agent cannot see.** Where things lie that are outside the repository or
  outside the obvious place (the backlog, documentation, related repositories), which source wins
  when two places speak of the same thing, unusual features of the environment. Not a description
  of the repository: directory structure, architecture and stack can be read from the code, and
  descriptions of a repository do not shorten the agent's way to the right files.
- **Pointers to ways in.** "Before X, read `path`" or "X is done by the skill `name`" — for
  activities whose way in the agent will not recognise from the request alone. The condition must
  be recognisable at the moment X happens, and the target is given as a path in backticks (WAY-129).
  `@path` in Claude Code is not a pointer; it loads the file into every session (section 4).
- **Rules that always apply**, short and not derivable from the repository: a convention absent
  from the tools' configuration, a command the agent will not guess, a pitfall it trips on.

What the main file does not hold:

- repetitions of the README, configuration, the linter or the framework's documentation — a tool
  enforces them or the agent knows them without the file;
- multi-step procedures — they belong in a skill, and the main file at most points to its way in;
- rules for one part of the code — they belong in a rule pinned to paths or in a file in a
  subdirectory;
- content that changes often — the main file points to its source;
- the history of a rule: dates, the course of an incident, abandoned variants.

**The global file has the highest bar.** Its line costs context in every session in every
repository, so it keeps only what concerns work regardless of the repository. A rule true for one
repository or one kind of work goes into that repository's file or onto the route of that work.

**Length has no threshold.** The thresholds found in sources (60, 200, 300, 500 lines) are rules
of thumb; measurements do not show a single rule getting lost in a longer file. Length is a budget
of cost, and the signal for review is a file that grows while what it covers does not.

## 3. Where a rule lives

A rule's place is set by what should trigger it — not by how many rules an area has or how long
they are (WAY-128). Rules with the same trigger live together; rules with different triggers do not
share a file.

| The rule applies… | It lives | Notes |
|---|---|---|
| in every session | in the main file | the conditions of section 2 |
| when working with certain files | in an instruction file in a subdirectory or in a rule pinned to paths | carriers: section 4 |
| during an activity — starting the environment, committing, reviewing, releasing | on the route of that activity: in the skill that leads it, or in a file that skill tells the agent to read | when the activity has no obvious way in, the main file points to it in one sentence |
| every time, without exception | in a CI check, a linter or a check of a step's output; in a local git hook only against slips | an instruction may explain what the check is for, but does not replace it (WAY-133) |
| as knowledge needed sometimes (documentation, patterns, data) | in a file pointed to from a step of a route or from the main file | one level deep; a model file is pointed to, not pasted |

**Splitting a file makes sense only when it changes the trigger.** Moving a rule into a file that
loads at session start anyway — `@path` in Claude Code, a rule without `paths` — tidies the text
but does not lighten the context. Moving it to where it loads only on an event or on a step of a
route does.

**A rule leaves the file it stands in when its trigger no longer fits that file**: it applies less
often than the file loads, it concerns a narrower part of the code, or it has grown into a
multi-step procedure. One rule with its own trigger may get a file of its own; ten rules with the
main file's trigger stay in the main file.

**A skill carries the procedure, and the files it points to carry the data for it.** Long rules of
an area, checklists and patterns lie in files that a step of the skill tells the agent to read;
the skill itself remains a sequence of steps.

## 4. One layout for three tools

The layout rests on two things that Claude Code, Codex and Cursor do alike: they load `AGENTS.md`
from the repository root at session start, and they carry out the instruction "read the file
`path`". Mechanisms of a single tool are additions, not carriers of a rule. How each tool loads
each file, with versions and the method of checking it: `tool_loading.md`.

| Layer | Shared carrier | Why it reaches every tool | Addition of a single tool |
|---|---|---|---|
| main file | `AGENTS.md` at the root | Codex and Cursor read it in a trusted project; Claude Code when the repository has no `CLAUDE.md` | `CLAUDE.md` only for additions meant for Claude Code alone; its first line is `@AGENTS.md` on its own (WAY-132) |
| ways in and steps of routes | a pointer as a path in backticks: "Before X, read `path`" | it is an instruction, not a loading mechanism — every tool carries it out the same way | — |
| procedures of activities | a skill in `.claude/skills/`; for Codex, a pointer to its `SKILL.md` by path from `AGENTS.md`, or a copy in `.agents/skills/` | Claude Code and Cursor discover this directory themselves; Codex does not read it, so it gets there through the pointer, or reads the copy in `.agents/skills/` (fact `codex-repository-skills`) | — |
| rules for parts of the code | `AGENTS.md` in a subdirectory and a line in the main file: "When working in `x/`, read `x/AGENTS.md`" | Claude Code and Cursor load it on access to a file there; Codex only when the session starts in that directory — the line in the main file closes this gap | a rule with `paths` (Claude Code), a rule with `globs` (Cursor) |
| what must happen every time | CI, a linter, a check of a step's output; a git hook against slips | they work outside the agent (WAY-133) | a Claude Code hook (text injected when a command is run), against slips |
| global file | — (each tool has its own) | — | one copy per tool, kept in step by a check that reports drift between them |

Pitfalls:

- **`@path` only as `@AGENTS.md` alone on the first line of `CLAUDE.md`** (WAY-129, WAY-132).
  Nowhere else does it serve as a pointer: in Claude Code it loads the file into every session, and
  a punctuation mark right after it switches the loading off without a warning; in Codex it is
  plain text.
- **`CLAUDE.local.md` stops Claude Code from reading `AGENTS.md`.**
- **No symbolic links on Windows** — without `core.symlinks` enabled, git checks a link out as a
  one-line text file.
- **A local git hook keeps a rule against slips, not against an agent that can turn it off.** One
  switch skips it; a rule an agent must not be able to skip is kept by CI or by the check of a
  step's output (WAY-133).
- **A `.mdc` rule and a rule in `.claude/rules/` work only in their own tool.** A rule that must
  apply everywhere does not live only there.

## 5. How to write a single rule

- **A rule describes behaviour that leaves a trace**: a command used, a file written, the shape of
  an output. Such a rule can be checked in a review and measured in a session (section 6). A
  sentence of intent ("write readable code", "care about quality") leaves no trace — it is turned
  into checkable behaviour or removed.
- **A prohibition says what to do instead.** A bare prohibition leaves the agent asking for the
  way and lengthens the work.
- **A rule says whether it applies with a human present or without one.** The same sentence can be
  right in a conversation where a human decides and too sharp in work the agent does alone — a rule
  from one setting does not carry over to the other without being reworded.
- **A rule names a kind of situation, not the event it came from.** No date, no course of an
  incident, no abandoned variants; an example only when the reach of the rule is unclear without
  one, and then two or three deliberately different ones.
- **Emphasis ("IMPORTANT", "YOU MUST") on one rule per file at most.** Everything emphasised means
  nothing emphasised.
- **A rule has one place.** When two routes need it, it lives in one file and the other route
  points to it.
- **A rule longer than a few sentences is a procedure** — it belongs in a skill or in a file the
  skill tells the agent to read (section 3).
- **A change to a rule replaces its previous wording** where that wording stood; a note added under
  the old sentence leaves two contradicting instructions in the file, and a contradiction gives the
  agent non-determinism, not an error.

## 6. Judging a file and a rule

### Statically — reviewing files without running the agent

A review covers together everything that loads in the same session (the global file, the
repository's file, rules, a skill), because a contradiction between layers cannot be seen when one
file is read alone.

- **Every line of the main file meets the three conditions of section 2.**
- **A verdict to add or reword a rule rests on a mistake found more than once in records of the
  work, or on a decision or step it carries; a verdict to keep, move or remove one may rest on a
  stated cost**; where no such mistake was found, the review says what it searched (WAY-130).
- **Typical defects:**
  - a file swollen with content most sessions do not need;
  - a procedure or specialist knowledge in the main file instead of on a route;
  - a repetition of what a linter or the configuration enforces;
  - a pointer without a condition — it is unclear when to reach for it;
  - a file generated at the start of a project and never changed, though the code changed;
  - two instructions that contradict each other;
  - a rule that has to hold every time, kept only by a hook an agent can switch off.
- **Mechanical checks**, settled without reading the content:
  - every path, skill and command pointed to exists;
  - `@path` appears only as `@AGENTS.md` alone on the first line of `CLAUDE.md`;
  - every `.mdc` rule has a YAML header;
  - a repository relying on `AGENTS.md` has no `CLAUDE.local.md`;
  - every `AGENTS.md` in a subdirectory has a pointing line in the main file;
  - a skill needed in Codex has a pointer in `AGENTS.md` or a copy in `.agents/skills/`;
  - the Markdown files the root `AGENTS.md` or `CLAUDE.md` names in backticks pass the same checks
    (the script follows only those; the glossary term and the invariant count a file named by its
    path anywhere in the text).

### In operation — fresh sessions with the rule and without it

Judging in operation is three separate questions, each with a different cost (WAY-131):

| Question | How to settle it | How many sessions |
|---|---|---|
| **did the rule load** | a marker in the file and evidence from the tool: the `InstructionsLoaded` hook in Claude Code, `codex --ask-for-approval never "Summarize the current instructions."`, a list of markers in Cursor — always with a positive control, a file that must load | one per variant |
| **did the agent follow it** | the trace of behaviour from section 5 | a few, when without the rule the behaviour never happens; dozens to over a hundred, when it happens sometimes and the rule should only make it more frequent |
| **did it help** | whether the mistake the rule was meant to remove stopped coming back | not from test sessions — from watching the work over time (section 7) |

- **A rule that loaded but was not followed is a different defect from a rule that did not load.**
  The first needs a change of wording or a move into enforcement (CI or a check of the
  output; a hook only against slips); the second, a change of carrier.
- **Comparing three sessions with the rule and three without it settles only the first case of the
  second question.** When the behaviour happens without the rule too, such a sample cannot tell the
  rule's effect from the ordinary variation between runs.
- **The model and the tool's version are the same in both variants,** and a result from one model
  is not carried over to another.

## 7. Maintenance

### When to add a rule

- **The signal is repetition, not a single event:** the agent makes the same mistake a second
  time, a review catches something the agent should have known, a human types the same correction
  again. A rule enters only for a mistake found more than once in records of the work; a mistake
  seen once is watched, not ruled (WAY-130). The exception: a rule that carries a decision the
  repository records, or a step of an activity in the file that leads that activity, needs no
  repeated mistake — its reason and its way out are that decision or that work.
- **Rules come from reviewing sessions, not from memory.** A scan of session records reports
  matters, a human verifies and settles them; the rule is written after that critique, when it is
  known which mistake it fixes and why. An incident recalled from memory days later gives no
  material for a rule.
- **Before adding:** the place by its trigger (section 3), the form by section 5, and a check
  whether a rule on the same thing already stands elsewhere — then that one is replaced instead of a
  second one being added.
- **Every rule added against a mistake names that mistake** (WAY-130). A rule for which none can
  be named does not go in; the named mistake is later its way out.

### When to remove a rule

- the agent does it right without the rule (a rule added for a mistake) — settled by a removal
  test: the rule goes, and watching the work shows whether the mistake comes back;
- a tool enforces it (a linter, CI, or a local hook only against slips) — the rule goes or turns into a check;
- it can be read from the repository;
- it points to a path, skill or command that does not exist;
- it was added for a mistake that can no longer be named — it is proposed for removal; when the
  mistake is named but may no longer happen, it is proposed as a removal test. A rule that carries
  a decision or a step of an activity goes with that decision or that step, not by this test.

A long absence of the mistake does not prove the rule is unnecessary — it may mean the rule works.
A removal test settles it, not the calendar.

### Mechanisms that clean up

- **The mechanical checks of section 6 are run by a scan, not by a human** — dead paths and wrong
  syntax come out without reading the content.
- **Size over time:** a file that grows while what it covers does not is accretion; the signal is
  available without reading.
- **A review after a change of model, not by the calendar:** rules written for an older model are
  sometimes unnecessary or too tight for a new one; each rule with a trace then goes through a
  removal test.
- **A review of sessions tells two defects apart:** the rule did not load (change the carrier), or
  it loaded and was not followed (change the wording or move it into a check). A review of session
  records also shows contradictions between layers — the global file, the repository's file, a
  skill and a request — that no file shows on its own.
- **A step after a task that asks whether the instruction files should change has two outcomes:
  adding and withdrawing.** A loop that can only add reproduces accretion; withdrawing is an equal
  outcome of it.
- **An edit to a file replaces the sentence that stands.** An instruction asking an agent for a fix
  says: replace the sentence that stands; if you add one, name the sentence that becomes
  unnecessary.

## Sources

Tool behaviour rests on an environment fact of the-way where one exists, named by its identifier;
the fact's entry in `foundations/environment_facts.md` holds the passage and its address.
Otherwise it rests on the tool's documentation, by address. What was measured is described in
`tool_loading.md`, where each measurement stands.

- Environment facts of tool behaviour: `claude-code-imports`, `claude-code-agents-md`,
  `claude-code-path-rules`, `claude-code-project-skills`, `codex-agents-md`,
  `codex-repository-skills`, `cursor-agents-md`.
- Tool documentation: https://code.claude.com/docs/en/memory, https://code.claude.com/docs/en/skills,
  https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/best-practices,
  https://learn.chatgpt.com/docs/agent-configuration/agents-md,
  https://learn.chatgpt.com/docs/build-skills, https://learn.chatgpt.com/guides/best-practices,
  https://cursor.com/docs/rules, https://cursor.com/docs/skills.
- Studies:
  - https://arxiv.org/abs/2602.11988v3 — context files raise inference cost by over 20% on
    average, their instructions are followed, and repository overviews in them do not help (fact
    `context-file-effect`);
  - https://arxiv.org/abs/2605.10039v1 — file size, instruction position, file architecture and
    contradictions in adjacent files produce no detectable contrast in compliance with a single
    trivial rule after multiple-testing correction, and each additional function generated within
    a session goes with about 5.6% lower odds of compliance per step, though not as a constant
    effect (fact `single-rule-compliance`);
  - https://arxiv.org/abs/2507.11538v1 — accuracy falls as the number of instructions grows (fact
    `instruction-density-accuracy`);
  - https://arxiv.org/abs/2602.07150v3 — identical runs of one agent configuration differ by
    2.2 to 6.0 percentage points in a single run's score (fact `agent-run-variance`);
  - https://arxiv.org/abs/2511.12884v2 — instruction files evolve through frequent small additions;
  - https://arxiv.org/abs/2606.15828v5 — a catalogue of six configuration smells of instruction
    files, drawn from a review of grey literature and from mining, and measured on 100 popular
    open-source repositories.
