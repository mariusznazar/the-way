# Light Cycle for a Small Change — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **In this cycle:** the execution method is fixed — Superpowers 6.4.1 `subagent-driven-development`
> for Tasks 2 and 3 (fresh implementer and reviewer per task, then one whole-branch review). Task 1
> is the cycle's FOUNDATION STEP: the orchestrator runs it before Tasks 2 and 3, outside
> `subagent-driven-development`, through the element skills `record-decision` and
> `record-invariant` read from this worktree. Questions from any agent go to the orchestrator,
> never to Mariusz.

**Goal:** Add a light cycle to `implement-task` — one executor makes a small change that leaves the
foundation unchanged straight from the task, the same checks run, one review covers the whole — and
change WAY-13 and WAY-125 so the foundation allows it.

**Architecture:** Three commits on `task/light-path-small-change` from base `c64a607`. Task 1 edits
two decisions in place in `foundations/decisions.md` (no `main` branch exists, so entries are edited
in place, `agent-instructions/README.md` "Start a change") and renews one invariant link in
`foundations/invariants.md`. Task 2 edits six places of `task-cycle/skill/SKILL.md`. Task 3 edits
four places of `task-cycle/record_template.md`. Every word of new text comes from the spec; this plan
only fixes line wrapping.

**Tech Stack:** Markdown; Python 3 scripts of the repository (`gate/run_tests.py`, the element
format guards, `relation-model/fingerprint.py`); git in Git Bash (the Bash tool) on Windows.

**Spec:** `docs/task-cycles/light-path-small-change/spec.md`
(sections 4, 6, 7 and 11 are the sources of every wording below). Frozen task:
`.../light-path-small-change/task_frozen.md`. Orchestrator rulings: `.../light-path-small-change/cycle.md`
(Questions table, C2–C7).

## Global Constraints

- Worktree: `C:/Storage/repos/the-way-light-path`, branch `task/light-path-small-change`, base
  `c64a6071384fb57cdb9d7e9db4560ddc43e3b355`. Run every command from the worktree root in Git Bash.
- Files this plan changes, and no others: `foundations/decisions.md`, `foundations/invariants.md`,
  `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`. Nothing under
  `agent-instructions/`, `project-level/`, `installation/` or `elements/` changes (spec §12).
- Text is English. Spelling follows the file: the decision log writes "behaviour" (11 uses, no
  "behavior"); `task-cycle/skill/SKILL.md` writes "behavior". Do not normalise either — a changed
  letter in a binding sentence changes its fingerprint.
- Every new wording is copied from this plan, which copies the spec. If a skill or a reviewer
  wants a different word, stop and return the proposal to the orchestrator; do not edit it in.
- All four files are LF (`git ls-files --eol` shows `i/lf w/lf`, `.gitattributes` `* text=auto
  eol=lf`). Edit with the Edit tool; a script that rewrites a file reads and writes it with
  `newline=''`.
- New and rewrapped lines are at most 100 characters, except line 3 of `task-cycle/skill/SKILL.md`
  (the front-matter `description`), which stays ONE line: `installation/install.py` reads it with
  `^description: (.+)$`.
- Rewrap only the lines that hold a changed word. Leave every neighbouring line untouched, even
  where that leaves a short line (the file already has such lines, e.g. `SKILL.md:96`, `:138`).
- Numbered-step continuation lines keep their indentation: 3 spaces under steps 1–9, 4 spaces
  under steps 10–14 of `SKILL.md`.
- `*Approved by*` of both changed decisions reads exactly `Mariusz, merge of <request link>` — the
  literal placeholder; step 12 of the cycle swaps it for the request URL.
- Fingerprints are computed only from the bytes of a UTF-8 file fed to
  `python -B relation-model/fingerprint.py` with `<` in Git Bash — never from a string piped
  through a PowerShell or cp1252 console (the WAY-13 wording holds em dashes).
- Commits: `git add <path> …` with explicit paths only — never `git add -A`, `git add .` or
  `git commit -a`. Message in English, `type(scope): Sentence` (e.g. `feat(foundations): …`,
  `feat(task-cycle): …`), written to a file in the session scratchpad with the Write tool and
  committed with `git commit -F <file>`. Author email `<author email>` (already set in the
  worktree's config; check with `git config user.email`). No push.
- `.runs/` is git-ignored; nothing under it is ever added to a commit. Guard outputs and
  `--record` files go under `.runs/`.

## Review Focus

1. **A fingerprint computed from the wrong bytes.** `--merge-onto none` leaves every relation and
   link fingerprint unchecked, so a wrong `WAY-13@…` in WAY-125's *Relations* or in
   `foundation-change-path/1` passes every required check. Expected: both carry `97b17d59`, the
   fingerprint of WAY-13's binding part as written in the file. Pinned in Task 1 Steps 6 and 10
   (fingerprint from the file) and Step 11 (the `--merge-onto c64a607` diagnostic, red before the
   invariant is renewed, green after).
2. **The front-matter `description` broken across lines.** `installation/install.py` copies only the
   first line matching `^description: (.+)$` into every product's installed skill, so a wrapped
   description silently installs a truncated trigger. Expected: line 3 stays one line. Pinned in
   Task 2 Step 3 (one-line check) and Step 6 (installation tests read the committed file).
3. **A changed word hidden in a rewrap, or an unlisted change reaching the full cycle.** The
   acceptance criterion holds only if every change a task failing the rule meets is one listed in
   spec §5. Expected: a word diff of `SKILL.md` against `c64a607` shows only the six hunks of
   Task 2. Pinned in Task 2 Step 5 (word-diff reading) and Task 3 Step 4.
4. **Step references in the new section pointing at the wrong place.** "Light cycle" says "step 4",
   "steps 6 to 9", "step 10", "step 11", "steps 11 to 14", "the foundation step below" and "the
   dispatch contract above"; inserted anywhere but between the dispatch-contract paragraph and
   `## Design and plan`, "below"/"above" lie. Expected: the section sits at that exact spot and
   every number names the step it means. Pinned in Task 2 Step 4.
5. **A list item or numbered step broken by rewrapping.** A continuation line indented wrongly ends
   a Markdown list item or renumbers the steps, and no check renders the file. Expected: steps
   4, 6, 9 and 13 keep their indentation and numbering; the record template's bullets keep a
   two-space continuation. Pinned in Task 2 Step 4 and Task 3 Step 3 (indentation and line-length
   check).

---

## What can and cannot be checked

There is no code with behaviour in this change — only process text and foundation entries — so
Superpowers `test-driven-development` does not apply to any task: no test can fail first against
a sentence of a skill. The checks that actually run are these, with their baselines on `c64a607`
(recorded in `cycle.md`, "Verification"):

| Check | Baseline on c64a607 | Expected after the change |
|---|---|---|
| `python -B gate/run_tests.py gate` (critical flows, WAY-45) | exit 0, 96 OK | exit 0, 96 OK |
| `python -B gate/run_tests.py elements/decisions` | 169 OK | 169 OK |
| `python -B gate/run_tests.py elements/invariants` | 233 OK | 233 OK |
| `python -B gate/run_tests.py task-cycle` | exit 1, `NO TESTS RAN` | exit 1, `NO TESTS RAN` — recorded as unchecked |
| `python -B gate/run_tests.py installation` (reads the committed skill's front matter) | 16 OK | 16 OK |
| decisions guard, `--base none --merge-onto none` | exit 0; 0 errors, 5 warnings, 5 unchecked | exit 0; 0 errors, 7 warnings (the 5 + two placeholder warnings), 5 unchecked |
| invariants guard, `--base none --merge-onto none` | exit 0; 0 errors, 0 warnings, 3 unchecked | unchanged |
| glossary guard, `--base none --merge-onto none` | exit 0; 0 errors, 0 warnings, 5 unchecked | unchanged |

What stays unchecked, to be recorded as unchecked and never as a pass:

- `task-cycle/` holds no tests: the skill and the record template are checked by reading only.
- `--merge-onto none` leaves relation and link fingerprints, `TODO` at the merge and the copies of
  a version unchecked; `--base none` leaves versions and identifiers unchecked. The fingerprints
  are checked by hand (Task 1 Steps 6 and 10) and by the diagnostic (Task 1 Step 11), which is
  recorded as a diagnostic, not a pass.
- The full gate of the-way does not exist yet (`agent-instructions/README.md`): these are partial
  checks.

---

### Task 1: Foundation step — WAY-13/1, WAY-125/1 and `foundation-change-path/1`

Run by the orchestrator (not by a `subagent-driven-development` implementer), through
`record-decision` (`elements/decisions/skill/SKILL.md`) and `record-invariant`
(`elements/invariants/skill/SKILL.md`) read from this worktree, before Tasks 2 and 3.

**Files:**
- Modify: `foundations/decisions.md:390-420` (WAY-13/1, binding part through *Rejected*)
- Modify: `foundations/decisions.md:3549-3558` (WAY-125/1 binding part)
- Modify: `foundations/decisions.md:3575-3590` (WAY-125/1 *Relations* through *Rejected*)
- Modify: `foundations/invariants.md:262` (`foundation-change-path/1` *Derives from*)
- Line numbers are those of `c64a607`; after the WAY-13 edit, every later line moves down by
  eleven (the WAY-13 block grows from 31 to 42 lines), so WAY-125's heading moves from 3547 to
  3558. Edit by exact text, never by line number. Expected `git diff --numstat` for the commit:
  `68 35 foundations/decisions.md`, `1 1 foundations/invariants.md`.

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: WAY-13's new binding part with fingerprint `97b17d59`, carried by WAY-125
  (`derives from WAY-13@97b17d59`) and `foundation-change-path/1` (`WAY-13@97b17d59`); WAY-125's
  new binding part with fingerprint `68b2d563`, carried by nothing. Task 2's "Light cycle" section
  cites WAY-13 and WAY-125 by number only.

- [ ] **Step 1: Read what the element skills require**

Read in full, from the worktree: `elements/common/way_of_working.md`, `elements/common/rules.md`,
`elements/decisions/template.md`, `elements/decisions/skill/SKILL.md`,
`elements/decisions/examples.md` and the decisions it names in `foundations/decisions.md`,
`elements/invariants/template.md`, `elements/invariants/skill/SKILL.md`,
`elements/invariants/examples.md`, `foundations/glossary.md` (whole), `foundations/decisions.md`
(whole) and `foundations/invariants.md` (whole). This is the skills' step 1; it is not optional.

- [ ] **Step 2: Search the whole foundation for unlinked effects (WAY-33)**

Run:

```bash
grep -rn --exclude-dir=.git --exclude-dir=.runs -e 'WAY-13@' -e 'WAY-125@' -e 'WAY-13/' -e 'WAY-125' -e 'foundation-change-path' .
grep -rn --exclude-dir=.git --exclude-dir=.runs -e 'WAY-13[^0-9/@]' -e 'WAY-13$' .
grep -n '^- \*\*Scope:\*\*.*task-cycle' foundations/decisions.md | wc -l
grep -n -i -e 'light path' -e 'light cycle' -e 'full cycle' foundations/ elements/ task-cycle/ project-level/ agent-instructions/ -r
```

Expected (verified on `c64a607`):
- First grep, six lines: `foundations/decisions.md:388` (WAY-13/1 heading), `:403` (its
  *Verification* naming `foundation-change-path`), `:3547` (WAY-125/1 heading),
  `foundations/invariants.md:256` and `:262` (`WAY-13@c6b33aa9`, the only carrier of a WAY-13
  fingerprint), and `task-cycle/skill/SKILL.md:38` ("WAY-125 names the borrowed methods and the
  the-way adapter's stage boundaries" — still true). `WAY-125@` nowhere.
- Second grep, six prose citations of WAY-13 — `elements/part-map/template.md:164` and `:202`,
  `foundations/decisions.md:1274` and `:1279` (WAY-46), `task-cycle/skill/SKILL.md:51` and `:141`
  — all about how sharply a change is checked, which the new WAY-13 keeps unchanged: no edit.
- Third: `31` decisions with *Scope* holding task-cycle.
- Fourth: `light path` at `foundations/decisions.md:1304` (WAY-47 *Rationale*, a different
  meaning — no edit, spec §8 row WAY-47) and in two unrelated fixtures,
  `elements/part-map/test_format_guard.py:76` and `:1224`; `light cycle` and `full cycle` nowhere.

Then read whole, including *Rejected*, every decision the second grep lists (Scope task-cycle) and
WAY-01, 03, 10, 11, 25, 30, 31, 33, 36, 45, 47, 48, 69, 95, 97, 99, 100, 114, 126, and compare each
with the new wordings of Steps 3–9. The expected findings are exactly spec §8's table: no
collision beyond WAY-13 and WAY-125 themselves, and `foundation-change-path/1` needing only its
fingerprint renewed. Check the glossary terms the new wordings use — "foundation", "entry",
"invariant", "invariant test" — keep their glossary meaning; no new term enters a binding part
(the four conditions stand in WAY-125 in place of the label "simple and obvious", ruling C4).
Anything not in spec §8 is a finding: record it in `cycle.md` and resolve it before Step 3 (a
collision without recorded precedence stops the work, WAY-25).

- [ ] **Step 3: Write WAY-13/1 in place (record-decision, steps 3–4.3)**

Replace with the Edit tool. The binding sentences (first paragraph) are spec §7.1 verbatim;
*Verification*, *Approved by*, *Rationale* and *Rejected* are spec §7.1; *Change*, *Scope*,
*Based on*, *Relations*, *Review when* and *Origin* are unchanged. *Rationale* and *Rejected*
stay italic paragraphs after the field list (the log's form, `elements/decisions/template.md:40-41`).

Old text (1a), `foundations/decisions.md:390-420`:

```text
What a task touches, never its size, sets its process: an agent's analysis at the start of the task
settles whether it changes the foundation, which chooses among the paths that merge a change, while
three things set how sharply it is checked — the criticality of the parts it touches, as the part
map computes it, whether it touches the files of a trust boundary, and whether the change can be
undone. Paths that merge a change differ in their steps, never in the outcome a task has to reach,
and only a human sets a task to return knowledge instead of a change, which merges nothing. A task's
size serves only as a signal to split it, an agent may check a change more sharply than the map
computes, never less, and a human decides on every change that cannot be undone.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
    a human's decision;
  - violates: a task gets the heavier path because of the number of lines it changes; a change
    that cannot be undone reaches the main branch without a human's decision; an agent turns a task
    into one that returns knowledge instead of a change without a human setting it so.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-09-30

*Rationale:* size misleads both ways: a rename across many files is easy to undo, a one-line
change to a stored format can destroy every user's data. Paths differ only in steps, because a
weaker outcome would bypass the process; returning knowledge alters what a task delivers, so a
human sets it.
*Rejected:* one cycle for all tasks — how much process a task needs depends on what can go wrong;
the path chosen by size — size misleads; a human approving every diff (DORA) — no fewer failed
changes, and attention spent where it adds nothing.
```

New text (1a):

```text
What a task touches, never its size, sets the path that merges its change and how sharply that
change is checked: an agent's analysis at the start of the task settles whether it changes the
foundation, which chooses among the paths that merge a change, while three things set how sharply
it is checked — the criticality of the parts it touches, as the part map computes it, whether it
touches the files of a trust boundary, and whether the change can be undone. Paths that merge a
change differ in their steps, never in the outcome a task has to reach, and only a human sets a
task to return knowledge instead of a change, which merges nothing. A task's size may lighten how
its change is prepared and made — its spec and plan and the number of agents making it — never the
outcome it has to reach or the checks run on the finished change, and otherwise serves only as a
signal to split it; an agent may check a change more sharply than the map computes, never less, and
a human decides on every change that cannot be undone.

- **Change:** new decision
- **Scope:** task-cycle
- **Based on:** none
- **Relations:** none
- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
    a human's decision; a copy change that touches no foundation entry is made by one agent without
    a spec or a plan and runs the same checks as any change to the parts it touches;
  - violates: a task takes the path for changes that leave the foundation unchanged because it
    changes few lines; a small task skips a check that the parts it touches call for; a change that
    cannot be undone reaches the main branch without a human's decision; an agent turns a task into
    one that returns knowledge instead of a change without a human setting it so.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* size misleads both ways about what can go wrong: a rename across many files is easy to
undo, a one-line change to a stored format can destroy every user's data, so what a task touches,
never its size, sets its path and its checks. Size does tell how much preparation a change needs: a
spec and a plan written ahead of a small change cost more than the change, while the checks on the
finished change stay whole and a human still decides on what cannot be undone. Paths differ only in
steps, because a weaker outcome would bypass the process; returning knowledge alters what a task
delivers, so a human sets it.
*Rejected:* one cycle for all tasks — how much process a task needs depends on what can go wrong;
the path chosen by size — size misleads; a human approving every diff (DORA) — no fewer failed
changes, and attention spent where it adds nothing; keeping a change that cannot be undone, or one
touching a trust boundary's files, from the lighter preparation — it would take the lighter
preparation from small tasks it suits, while a human's decision and checks kept whole already
stop such a change.
```

*Review when* stays `none`: the decision rests on no prediction (the skill's "Set every *Review
when* yourself" is met by keeping it). Record that in `cycle.md`.

- [ ] **Step 4: Run the decisions guard on WAY-13 (way_of_working step 4.3)**

```bash
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --record .runs/decisions.jsonl > docs/task-cycles/light-path-small-change/reports/t1-decisions-guard-way13.txt 2>&1; echo "exit $?"
tail -1 docs/task-cycles/light-path-small-change/reports/t1-decisions-guard-way13.txt
grep -n 'placeholder' docs/task-cycles/light-path-small-change/reports/t1-decisions-guard-way13.txt
```

Expected: `exit 0`; `0 error(s), 6 warning(s), 5 unchecked`; one placeholder warning, at the
*Approved by* line of WAY-13/1 (`foundations/decisions.md:417`). The five check-by warnings of the
baseline remain (WAY-03, 21, 52, 55, 69); compare them by message, not line number — every
warning after WAY-13 moves down by eleven lines (WAY-21 from 586 to 597). The five `unchecked:` lines are identical to
`reports/baseline-decisions-guard.txt`. Any error means the entry broke the form (for example a
binding part of more than three sentences): fix the entry and rerun.

- [ ] **Step 5: Keep WAY-13's meaning sentence for the request**

Record in `cycle.md`, "Request handoff" → "What this request settles":
`WAY-13/1 — Rozmiar zadania może odchudzić przygotowanie i wykonanie zmiany (spec, plan, liczbę
agentów), ale nigdy wyniku zadania ani sprawdzeń gotowej zmiany; to, czy zadanie zmienia
fundament, i ostrość sprawdzeń dalej wyznacza wyłącznie to, czego zadanie dotyka.`
No question goes to Mariusz before the request (ruling C5): the approved task orders the change.

- [ ] **Step 6: Compute WAY-13's fingerprint from the file**

```bash
SCRATCH=docs/task-cycles/light-path-small-change/reports
awk -v h='### WAY-13/1 ' 'index($0,h)==1{f=1;next} f&&/^- \*\*Change:\*\*/{exit} f' foundations/decisions.md > $SCRATCH/t1-way13-binding.txt
python -B relation-model/fingerprint.py < $SCRATCH/t1-way13-binding.txt
```

Expected: `97b17d59`. (The same command on `c64a607` gives `c6b33aa9`.) If it differs, the binding
paragraph differs from spec §7.1 — compare the file with the spec word by word and fix the file;
never carry a different value onward without the orchestrator's ruling.

- [ ] **Step 7: Write WAY-125/1 in place — binding part (record-decision, step 4.4 for WAY-13, steps 3–4.3 for WAY-125)**

Spec §7.2 verbatim. Sentences 2 and 3 are unchanged; the line breaks of sentence 1 change.

Old text (1b), `foundations/decisions.md:3549-3558` at `c64a607`:

```text
The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec,
writing an implementation plan, test-first implementation, subagent execution with independent task
and final code reviews, and preparing a pull or merge request; they apply only to a ready task run
through `implement-task`. The orchestrator answers workflow questions and gives provisional stage
go-aheads under the task owner's delegation, never records these as human approval, controls the
return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the
independent assessment of its foundation change and its return step, and brings the request to the
human for review. Decisions reserved to a human by the foundation remain reserved; when required
code cannot proceed without one, the cycle opens a blocked draft request; a different Superpowers
version requires a reviewed change to the-way before use.
```

New text (1b):

```text
The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec,
writing an implementation plan, test-first implementation, subagent execution with independent task
and final code reviews, and preparing a pull or merge request, only for a ready task run through
`implement-task`, which uses them all unless the orchestrator's analysis at its start finds it
leaving the foundation unchanged and small enough for one agent to make from the task alone: that
agent then makes it, test-first where it changes behaviour, and one final code review covers the
whole change, while a change that proves too large for that agent, or whose touch of the foundation
needs a choice the task leaves open, changes the meaning of an approved decision, contradicts a
current entry or writes or changes an invariant or an invariant test, is discarded and starts again
from a fresh design given the agent's report without its code. The orchestrator answers workflow
questions and gives provisional stage go-aheads under the task owner's delegation, never records
these as human approval, controls the return between stages, keeps agent reports before a borrowed
skill cleans its workspace, runs the independent assessment of its foundation change and its return
step, and brings the request to the human for review. Decisions reserved to a human by the
foundation remain reserved; when required code cannot proceed without one, the cycle opens a
blocked draft request; a different Superpowers version requires a reviewed change to the-way before
use.
```

- [ ] **Step 8: Write WAY-125/1 in place — fields, *Rationale*, *Rejected***

*Change*, *Scope*, *Based on*, *Review when* and *Origin* are unchanged (*Based on* is not touched:
the old text starts at *Relations*). The new *Relations* carries the fingerprint from Step 6.

Old text (1c), `foundations/decisions.md:3575-3590` at `c64a607`:

```text
- **Relations:** derives from WAY-100@e7a74a18
- **Verification:** level 2 — an agent compares a cycle with the decision:
  - complies: agents use the named methods at version 6.4.1, return between stages, and show
    provisional choices in the request without claiming human approval;
  - violates: an agent treats its own spec approval as the owner's approval, skips the request
    review, or silently runs a different Superpowers version.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of https://github.com/mariusznazar/the-way/pull/4

*Rationale:* the borrowed skills provide design, planning, test and review methods, while the-way
must keep control of task sources, binding foundation approvals and the single human review point.
Naming the version makes the dependency visible when the process is pinned in a product.
*Rejected:* adopting the complete Superpowers workflow with its intermediate human gates — it would
interrupt the delegated cycle; copying the skill bodies into the orchestrator — it would create a
second implementation of those methods.
```

New text (1c):

```text
- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-13@97b17d59
- **Verification:** level 2 — an agent compares a cycle with the decision:
  - complies: agents use the named methods at version 6.4.1, return between stages, and show
    provisional choices in the request without claiming human approval; a task found small at its
    start, leaving the foundation unchanged, is made by one agent from the task, test-first where it
    changes behaviour, and its whole change gets one final code review; an attempt that grows too
    large, or whose touch of the foundation writes an invariant, is discarded and the task starts
    again from a fresh design that reads the agent's report;
  - violates: an agent treats its own spec approval as the owner's approval, skips the request
    review, or silently runs a different Superpowers version; a task found small at its start merges
    without a final code review; a spec and a plan are written around an outgrown attempt's code.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* the borrowed skills provide design, planning, test and review methods, while the-way
must keep control of task sources, binding foundation approvals and the single human review point.
Naming the version makes the dependency visible when the process is pinned in a product. A small
change that leaves the foundation unchanged gains nothing from a design, a spec and a plan, so one
agent makes it from the task, while the checks on the finished change and the final review stay
(WAY-13); a change that outgrows that finding starts again rather than having a spec and a plan
written around partial code, and the agent's report passes on what it learned without the shape of
its code.
*Rejected:* adopting the complete Superpowers workflow with its intermediate human gates — it would
interrupt the delegated cycle; copying the skill bodies into the orchestrator — it would create a
second implementation of those methods; a separate skill for small tasks — two skills would hold the
same rules of the record, the request and the return step, while size only lightens one process
(WAY-13); an outgrown attempt kept and completed — a spec and a plan would be written around
partial code; the agent of an outgrown attempt writing the spec and the plan — the spec would carry
the shape of the abandoned code; a task once made by one agent finishing that way whatever it grows
into — the grown change would merge without the design it turned out to need.
```

Then record WAY-125's meaning sentence in `cycle.md` beside WAY-13's:
`WAY-125/1 — Metody Superpowers obowiązują w pełnym cyklu; małe zadanie bez zmiany fundamentu
robi jeden wykonawca, od testów tam, gdzie zmienia zachowanie, z jednym końcowym przeglądem
całości, a zmiana, która przerośnie tę ocenę albo dotknie fundamentu w sposób wymagający otwartego
wyboru, zmiany znaczenia zatwierdzonej decyzji, sprzeczności z wpisem lub inwariantu albo jego
testu, jest odrzucana i zaczyna się od nowa od świeżego projektu z raportem wykonawcy bez kodu.`
Also record, for the request, the six wordings beyond the task's words (spec §7, "Wording beyond the
task's words", items 1–6), D13 among them.

- [ ] **Step 9: Run the decisions guard on WAY-125**

```bash
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --record .runs/decisions.jsonl > docs/task-cycles/light-path-small-change/reports/t1-decisions-guard.txt 2>&1; echo "exit $?"
tail -1 docs/task-cycles/light-path-small-change/reports/t1-decisions-guard.txt
grep -n 'placeholder' docs/task-cycles/light-path-small-change/reports/t1-decisions-guard.txt
```

Expected: `exit 0`; `0 error(s), 7 warning(s), 5 unchecked`; two placeholder warnings, at the
*Approved by* lines of WAY-13/1 (`:417`) and WAY-125/1 (`:3606`). A missing placeholder warning means an *Approved
by* still holds the old value. Any error (e.g. "more than three binding sentences") is the entry's
to fix.

- [ ] **Step 10: Compute WAY-125's fingerprint and renew `foundation-change-path/1` (record-invariant)**

```bash
SCRATCH=docs/task-cycles/light-path-small-change/reports
awk -v h='### WAY-125/1 ' 'index($0,h)==1{f=1;next} f&&/^- \*\*Change:\*\*/{exit} f' foundations/decisions.md > $SCRATCH/t1-way125-binding.txt
python -B relation-model/fingerprint.py < $SCRATCH/t1-way125-binding.txt
grep -rn --exclude-dir=.git --exclude-dir=.runs 'WAY-125@' .
```

Expected: `68b2d563` (base `4c302238`); no carrier of `WAY-125@`, so nothing else follows from it.

Before editing the invariant, run the red half of the diagnostic: it must flag the stale link,
which proves the diagnostic reads it.

```bash
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto c64a607 --record .runs/invariants-diag.jsonl > docs/task-cycles/light-path-small-change/reports/t1-invariants-diag-red.txt 2>&1; echo "exit $?"
grep -n 'WAY-13' docs/task-cycles/light-path-small-change/reports/t1-invariants-diag-red.txt
```

Expected: `exit 1`, `1 error(s), 0 warning(s), 1 unchecked`, the error reading
``foundations/invariants.md:262: error: foundation-change-path/1: `WAY-13@c6b33aa9` — the current
fingerprint of WAY-13 after the merge is 97b17d59``.

Then edit (record-invariant; the sentence is unchanged, the version stays 1 — a renewed link
does not raise it, WAY-31 *Rejected*, and with no main branch every entry stays at version 1,
`elements/common/rules.md` "Version"; *Method* stays `TODO`, so nothing is handed to a check author):

Old text (1d), `foundations/invariants.md:262`:

```text
- **Derives from:** WAY-13@c6b33aa9
```

New text (1d):

```text
- **Derives from:** WAY-13@97b17d59
```

Re-read the invariant's sentence against the new WAY-13: "No change that, against {fork-point},
alters a foundation entry runs on the path for tasks that leave the foundation unchanged." It
still holds: the light cycle is not one of WAY-13's paths (spec D1, §8 row 1). Record this
re-reading in `cycle.md`.

- [ ] **Step 11: Run the guards and the diagnostic**

Required (compare with the baselines in `cycle.md` and `reports/baseline-*.txt`):

```bash
R=docs/task-cycles/light-path-small-change/reports
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --record .runs/decisions.jsonl > $R/t1-decisions-guard.txt 2>&1; echo "decisions exit $?"
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none --record .runs/invariants.jsonl > $R/t1-invariants-guard.txt 2>&1; echo "invariants exit $?"
python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none --record .runs/glossary.jsonl > $R/t1-glossary-guard.txt 2>&1; echo "glossary exit $?"
tail -1 $R/t1-decisions-guard.txt $R/t1-invariants-guard.txt $R/t1-glossary-guard.txt
diff <(grep '^unchecked' $R/baseline-invariants-guard.txt) <(grep '^unchecked' $R/t1-invariants-guard.txt) && echo "invariants unchecked lines identical"
diff <(grep '^unchecked' $R/baseline-glossary-guard.txt) <(grep '^unchecked' $R/t1-glossary-guard.txt) && echo "glossary unchecked lines identical"
diff <(grep '^unchecked' $R/baseline-decisions-guard.txt) <(grep '^unchecked' $R/t1-decisions-guard.txt) && echo "decisions unchecked lines identical"
```

Expected: all three `exit 0`; decisions `0 error(s), 7 warning(s), 5 unchecked`; invariants
`0 error(s), 0 warning(s), 3 unchecked`; glossary `0 error(s), 0 warning(s), 5 unchecked`; the
three "identical" lines printed.

Diagnostic (spec §11.6 — recorded as a diagnostic, never as a pass). The base runs on `c64a607`
gave: decisions `0 error(s), 5 warning(s), 2 unchecked`; invariants `0 error(s), 0 warning(s),
1 unchecked`.

```bash
R=docs/task-cycles/light-path-small-change/reports
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto c64a607 --record .runs/decisions-diag.jsonl > $R/t1-decisions-diag.txt 2>&1; echo "exit $?"
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto c64a607 --record .runs/invariants-diag.jsonl > $R/t1-invariants-diag.txt 2>&1; echo "exit $?"
grep -n 'error' $R/t1-decisions-diag.txt $R/t1-invariants-diag.txt; tail -1 $R/t1-decisions-diag.txt $R/t1-invariants-diag.txt
```

Expected differences from the base runs, each caused by the in-place edits and named as such in
`cycle.md`:
- decisions: `exit 1`, `4 error(s), 7 warning(s), 2 unchecked` — the four errors are
  `:388 WAY-13/1 differs from its copy on c64a607; the log after the merge holds this copy`,
  `:3558` the same for `WAY-125/1`, and at `:417` and `:3606` `*Approved by* is the placeholder
  ..., which a merge onto the main branch does not take`; no error naming a relation fingerprint
  (`WAY-100@e7a74a18` and `WAY-13@97b17d59` both current);
- invariants: `exit 0`, `0 error(s), 0 warning(s), 1 unchecked` — the link `WAY-13@97b17d59` is
  current (the green half of Step 10's red run).

Anything else is a finding: record it and resolve it before committing.

- [ ] **Step 12: Run the tests of the changed parts and the critical flows**

```bash
python -B gate/run_tests.py elements/decisions 2>&1 | tail -3
python -B gate/run_tests.py elements/invariants 2>&1 | tail -3
python -B gate/run_tests.py gate 2>&1 | tail -3
```

Expected: `Ran 169 tests … OK`, `Ran 233 tests … OK`, `Ran 96 tests … OK`. (These tests use fixtures,
not the-way's own entries, so they show that nothing else broke, not that the entries are right.)

- [ ] **Step 13: Commit**

Write this message with the Write tool to `docs/task-cycles/light-path-small-change/commit-msg-t1.txt`:

```text
feat(foundations): Let a task's size lighten how its change is made, never its checks

WAY-13 now says what a task touches, never its size, sets the path that merges its change and how
sharply it is checked, and that size may lighten how a change is prepared and made - its spec and
plan and the number of agents making it - never the outcome or the checks run on the finished
change.

WAY-125 applies the adopted Superpowers methods in full unless the start analysis finds a task
leaving the foundation unchanged and small enough for one agent to make from the task alone: that
agent makes it, test-first where it changes behaviour, under one final code review. A change that
outgrows it, or whose touch of the foundation needs an open choice, changes an approved decision's
meaning, contradicts a current entry or writes an invariant or an invariant test, is discarded and
starts again from a fresh design given the agent's report without its code. WAY-125 now derives
from WAY-13@97b17d59; foundation-change-path carries the same fingerprint, its sentence re-read
against the new WAY-13 and unchanged.

Both decisions change meaning, so their Approved by reads "Mariusz, merge of <request link>" until
the request exists; the merge accepts them again (WAY-07, WAY-14).
```

```bash
git add foundations/decisions.md foundations/invariants.md
git commit -F docs/task-cycles/light-path-small-change/commit-msg-t1.txt
git show --stat --format='%h %ae %s' HEAD
```

Expected: one commit, author `<author email>`, exactly two files changed. Record the commit
hash in `cycle.md` (Artifacts, Events). The one independent assessment of this change (WAY-10) is
the cycle's step 11, after Tasks 2 and 3 — not here.

---

### Task 2: `task-cycle/skill/SKILL.md` — the light cycle in the skill (spec §4)

**Files:**
- Modify: `task-cycle/skill/SKILL.md:3` (front matter), `:51-55` (step 4), `:83-86` (new section
  before `## Design and plan`), `:88-91` (step 6), `:132-133` (step 9), `:197-198` (step 13) —
  line numbers of `c64a607`; apply the edits bottom-up or by exact text, never by line number.
- Test: none exists for `task-cycle/`; `installation/test_install.py` reads the committed front
  matter.

**Interfaces:**
- Consumes: WAY-13 and WAY-125 as written in Task 1 (cited by number only).
- Produces: the heading `## Light cycle`; the names "light cycle", "full cycle", "executor",
  "switch", "the executor's report", "discarded attempt"; step 4's instruction to record the cycle
  choice "with the reason for each finding you assessed". Task 3's record-template slots name
  the same things.

- [ ] **Step 1: Make the six edits with the Edit tool**

Not changed: steps 1–3, step 5, the foundation-step paragraph, steps 7, 8, 10, 11, 12, 14 and
"Correction after review" (spec §4, last paragraph).

Old text (2a), line 3:

```text
description: Use to take one ready the-way task through autonomous design, planning, implementation, testing, review and a pull or merge request, or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
```

New text (2a) — one line, not wrapped:

```text
description: Use to take one ready the-way task to a reviewable pull or merge request — through autonomous design, planning, implementation, testing and review, or, for a small task that leaves the foundation unchanged, through one agent's implementation, the same checks and one review — or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
```

Old text (2b), lines 51–55 (step 4; line 56 onward unchanged):

```text
4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. Calculate the three sharpness inputs: criticality from
   the touched parts (unknown failure modes count as highest), whether touched files are trust
   boundaries, and whether any operation cannot be undone. Use the full subagent review loop even
   for low criticality. For a trust boundary, add adversarial input checks under WAY-48. Stage but
```

New text (2b):

```text
4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. In the same analysis, choose the light or the full
   cycle as "Light cycle" below gives it, and record the choice with the reason for each finding
   you assessed; once one finding fails, the rest may be recorded as not assessed. Calculate the
   three sharpness inputs: criticality from the touched parts (unknown failure modes count as
   highest), whether touched files are trust boundaries, and whether any operation cannot be
   undone. On the full cycle, use the full subagent review loop even for low criticality. For a
   trust boundary, add adversarial input checks under WAY-48. Stage but
```

Old text (2c), lines 84–86 (the end of the dispatch-contract paragraph and the next heading):

```text
an invariant's check (WAY-69).

## Design and plan
```

New text (2c) — spec §4.3, rewrapped to 100 columns, no word changed:

```text
an invariant's check (WAY-69).

## Light cycle

A task takes the light cycle when the analysis of step 4 finds all three: the task leaves the
foundation unchanged, so the foundation step below would not run for it; one agent can implement
it in about ten minutes; and its implementation needs neither very large files nor very many files
read into context. Every other task takes the full cycle — steps 6 to 9 — exactly as written. The
two cycles differ in how a change is prepared and made, never in the outcome the task has to reach
or the checks run on the finished change (WAY-13, WAY-125); both run inside the foundation route
of step 4. On the light cycle:

- Dispatch one fresh executor with the frozen task, the applicable source paths, the pinned
  foundation and the dispatch contract above. It makes the whole change from the task, without a
  spec or a plan, using Superpowers `test-driven-development` for behavior changes, and commits it.
  Its boundary is the committed change with its focused checks run; it returns before any review.
  It also returns, with its work committed, when the change touches the foundation and when the
  change outgrows a finding of step 4.
- When the change touches the foundation, rule on the touch and record the ruling. The touch is
  simple and obvious when the entry's change follows from the task's required outcome with no
  choice the task leaves open, changes the meaning of no approved decision, contradicts no current
  entry, and writes or changes no invariant or invariant test. On that ruling, record the
  foundation route as changed; the executor then writes the entry through its element's skill, as
  the foundation step below gives an entry the cycle writes, before it continues the code that
  depends on it, and the entry joins the one independent assessment of step 11. Any other touch
  switches the task to the full cycle.
- When the change is made, run step 10 in full. The whole change is its one implementation unit,
  and one Superpowers `requesting-code-review` of the whole change, with the frozen task as its
  requirements, is both that unit's review and the final review: the executor fixes its findings,
  the affected checks run again, and the same reviewer reviews the fix range once. Then continue
  with steps 11 to 14 as written. Where the harness cannot resume the executor after a ruling or
  for fixes, a fresh executor on the same branch, given the task and the ruling or the findings,
  continues in its place.

Switch to the full cycle when the executor, or you from its work, find while the change is being
made or its review findings fixed that it outgrows a finding of step 4 or touches the foundation in
a way that is not simple and obvious. The executor returns a report without code and without a
diff: why the change grew, which files and obstacles it found, and what proved not obvious. Check
that the report holds no code, keep it in `reports/`, and record the attempt's last commit, as a
historical name rather than a link to follow, and the names of the files it changed. Then discard
the attempt, its foundation entries included, by resetting the task branch to the recorded base
commit, record the switch with its reason, and continue at step 6, whose fresh design agent
receives the executor's report beside the frozen task.

## Design and plan
```

Old text (2d), lines 88–91 (step 6; line 92 onward unchanged):

```text
6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. Ask it to use Superpowers `brainstorming`. It
   classifies the task using that skill, then follows its architectural path because this cycle
   requires a written spec and plan for every ready task. Record the classification and this
```

New text (2d):

```text
6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. After a switch from the light cycle, also give it
   the executor's report, as the findings of a discarded attempt. Ask it to use Superpowers
   `brainstorming`. It classifies the task using that skill, then follows its architectural path
   because the full cycle requires a written spec and plan for every task it runs. Record the
   classification and this
```

Old text (2e), lines 132–133 (step 9; line 134 onward unchanged):

```text
9. Use Superpowers `subagent-driven-development`: fresh implementer and reviewer contexts for
   each meaningful plan task, followed by a whole-branch review. Its boundary is the final review
```

New text (2e):

```text
9. On the full cycle, use Superpowers `subagent-driven-development`: fresh implementer and
   reviewer contexts for each meaningful plan task, followed by a whole-branch review. Its
   boundary is the final review
```

Old text (2f), lines 197–198 (step 13; line 199 onward unchanged):

```text
13. The request contains: task goal and relation, source versions, design and plan links, what
    changed and why, test and review evidence with every check that did not run named, and *What
```

New text (2f):

```text
13. The request contains: task goal and relation, source versions, the cycle taken and its
    reasons — after a switch, its reason and a link to the executor's report — design and plan
    links on the full cycle, what changed and why, test and review evidence with every check that
    did not run named, and *What
```

- [ ] **Step 2: Confirm each base text matched once**

Each Edit call fails unless its old text occurs exactly once; six successful Edit calls are the
evidence. Run `git diff --numstat -- task-cycle/skill/SKILL.md`. Expected:
`62 12 task-cycle/skill/SKILL.md`.

- [ ] **Step 3: Check the front matter and line lengths**

```bash
python -B -c "import re;t=open('task-cycle/skill/SKILL.md',encoding='utf-8',newline='').read();fm=t.split('---')[1];print('description lines:',len(re.findall(r'^description: ',fm,re.M)),'front-matter lines:',len(fm.strip().splitlines()));print('CR present:','\r' in t)"
python -B -c "import sys;[print(f'{p}:{i}:{len(l)}') for p in sys.argv[1:] for i,l in enumerate(open(p,encoding='utf-8').read().split('\n'),1) if len(l)>100]" task-cycle/skill/SKILL.md
```

Expected: `description lines: 1 front-matter lines: 2`, `CR present: False`; the second command
prints only `task-cycle/skill/SKILL.md:3:<length>` (the front matter, one line by design).

- [ ] **Step 4: Check the placement, the step references and the list structure**

```bash
grep -n -e '^## ' -e '^[0-9]\+\. ' task-cycle/skill/SKILL.md
```

Expected order: `## Inputs and authority` (steps 1–3), `## Start and record` (steps 4–5),
`## Light cycle`, `## Design and plan` (steps 6–8), `## Execute, verify and review` (steps 9–11),
`## Request and handoff` (steps 12–14), `## Correction after review`; each step number 1–14 once,
in order. Then read the "Light cycle" section against the file: "step 4" is the start analysis;
"steps 6 to 9" are design, spec review, plan and execution; "the foundation step below" is the
paragraph opening "Before dependent implementation"; "the dispatch contract above" is the
paragraph opening "For every dispatch"; "step 10" is checks and review; "step 11" holds the
independent assessment; "steps 11 to 14" end at the completion report. Read steps 4, 6, 9 and 13
whole and confirm every continuation line keeps the step's indentation (3 spaces for 4, 6, 9;
4 spaces for 13).

- [ ] **Step 5: Read the acceptance criterion (spec §5) in the word diff**

```bash
git diff --word-diff=plain c64a607 -- task-cycle/skill/SKILL.md
```

Read it in full. Expected: exactly six changed places; rewrapping shows no change of words.
Every change a task failing the rule meets is one of: "On the full cycle" (step 4 sentence, step 9),
"the full cycle requires ... every task it runs" (step 6), the record of the cycle choice (step 4),
the request's line naming the cycle (step 13). The post-switch sentence of step 6 applies only after
a switch; the "Light cycle" section is reached only by a task passing all three findings; the
description is metadata. No step, agent, review, check or gate of the full cycle changes. Any other
change is a finding.

- [ ] **Step 6: Run the checks and commit**

```bash
python -B gate/run_tests.py task-cycle 2>&1 | tail -2
python -B gate/run_tests.py gate 2>&1 | tail -3
```

Expected: `task-cycle` exits 1 with `NO TESTS RAN` (recorded as unchecked: the part holds no tests);
`gate` `Ran 96 tests … OK`.

Write this message with the Write tool to `docs/task-cycles/light-path-small-change/commit-msg-t2.txt`:

```text
feat(task-cycle): Add a light cycle for a small task that leaves the foundation unchanged

Step 4 now chooses, in the analysis that settles the foundation route, between the light and the
full cycle and records the reason for each finding assessed. A task takes the light cycle when it
leaves the foundation unchanged, one agent can implement it in about ten minutes, and it needs no
very large or very many files read into context.

On the light cycle one fresh executor makes the whole change from the task, without a spec or a
plan; step 10 runs in full, and one requesting-code-review of the whole change is the unit's and
the final review. A simple and obvious touch of the foundation re-records the route as changed and
goes through the element's skill and the one assessment of step 11; any other touch, or a change
that outgrows a finding, returns a report without code, discards the attempt by resetting the
branch to its base, and restarts at step 6 with that report. Steps 4, 6, 9 and 13 name the full
cycle where only it applies; nothing else in the full cycle changes (WAY-13, WAY-125).
```

```bash
git add task-cycle/skill/SKILL.md
git commit -F docs/task-cycles/light-path-small-change/commit-msg-t2.txt
python -B gate/run_tests.py installation 2>&1 | tail -3
git show --stat --format='%h %ae %s' HEAD
```

Expected: `installation` `Ran 16 tests … OK` (run after the commit: the installer reads the
skill's front matter from a commit); one commit, `<author email>`, one file changed.

---

### Task 3: `task-cycle/record_template.md` — the cycle in the record (spec §6)

**Files:**
- Modify: `task-cycle/record_template.md:9` (header), `:19-21` (new `## Cycle` section before
  `## Events`), `:46` (Artifacts paragraph), `:76` (Request handoff) — line numbers of `c64a607`.

**Interfaces:**
- Consumes: from Task 2, the names "light cycle", "full cycle", "switch", "executor's report",
  "discarded attempt" and step 4's "the reason for each finding you assessed".
- Produces: the record's `- Cycle:` header line and `## Cycle` section, which step 4 of the skill
  fills; the request-handoff line that step 13's "the cycle taken and its reasons" fills.

- [ ] **Step 1: Make the four edits with the Edit tool**

Old text (3a), line 9:

```text
- Foundation route: <unchanged | entry or invariant-test change; affected entries>
```

New text (3a):

```text
- Foundation route: <unchanged | entry or invariant-test change; affected entries; on the light
  cycle, the time a touch changed it>
- Cycle: <light | full | full after a switch from light>
```

Old text (3b), lines 19–21:

```text
the request; preparing reversible code for it does not authorize executing it.

## Events
```

New text (3b):

```text
the request; preparing reversible code for it does not authorize executing it.

## Cycle

- Choice at start: <light | full> — foundation: <unchanged | changed>; one agent's time to
  implement: <estimate and reason | not assessed>; files read into context: <which, and their
  size | not assessed>
- Foundation touched on the light cycle: <entry, the ruling on whether the touch is simple and
  obvious, and its reason | none>
- Switch to the full cycle: <time, why the change outgrew the light cycle, the executor's report,
  the discarded attempt's last commit and the files it changed | none>

Record the reason for each finding assessed; once one finding fails, the rest may read `not
assessed`. The last commit of a discarded attempt is a historical name, not a link to follow: the
commit is reachable only until the reflog expires. A choice or ruling of a discarded attempt keeps
its row in the questions table, with *Used by* naming the discarded attempt.

## Events
```

Old text (3c), line 46 (line 47 onward unchanged):

```text
Include the frozen task, `spec.md`, `plan.md`, code commits, tests and full agent reports. Name
```

New text (3c):

```text
Include the frozen task, `spec.md` and `plan.md` on the full cycle, code commits, tests and full
agent reports, the report of a discarded light-cycle attempt among them. Name
```

Old text (3d), line 76:

```text
- Request URL and status: <URL and draft/ready/blocked>
```

New text (3d):

```text
- Request URL and status: <URL and draft/ready/blocked>
- Cycle and its reasons: <as the request states them>
```

- [ ] **Step 2: Confirm each base text matched once**

Four successful Edit calls are the evidence. `git diff --numstat -- task-cycle/record_template.md`
expected: `21 2 task-cycle/record_template.md`.

- [ ] **Step 3: Check line lengths, line endings and the structure**

```bash
python -B -c "import sys;[print(f'{p}:{i}:{len(l)}') for p in sys.argv[1:] for i,l in enumerate(open(p,encoding='utf-8').read().split('\n'),1) if len(l)>100]" task-cycle/record_template.md
python -B -c "print('CR present:', '\r' in open('task-cycle/record_template.md',encoding='utf-8',newline='').read())"
grep -n -e '^## ' -e '^- [A-Z]' task-cycle/record_template.md
```

Expected: only the pre-existing table header line (`## Questions and autonomous choices` table,
107 characters, now line 51) is over 100; `CR present: False`; sections in the order header list,
`## Sharpness at start and after the final diff`, `## Cycle`, `## Events`, `## Questions and
autonomous choices`, `## Artifacts`, `## Verification`, `## Return step`, `## Independent
assessment`, `## Request handoff`; the header list holds `Foundation route` then `Cycle`; each
wrapped bullet continues with two spaces.

- [ ] **Step 4: Read the change against the spec and the skill**

```bash
git diff --word-diff=plain c64a607 -- task-cycle/record_template.md
```

Expected: exactly the four places of spec §6, words as there. Check that every slot of the
`## Cycle` section answers a record step 4 or the "Light cycle" section of the skill asks for
(the choice with reasons per finding; the touch ruling; the switch with the report, last commit
and files), and that the full cycle's record differs only by the `Cycle` lines and the Artifacts
wording "on the full cycle".

- [ ] **Step 5: Run the checks and commit**

```bash
python -B gate/run_tests.py task-cycle 2>&1 | tail -2
python -B gate/run_tests.py gate 2>&1 | tail -3
```

Expected: `NO TESTS RAN` (unchecked) and `Ran 96 tests … OK`.

Write this message with the Write tool to `docs/task-cycles/light-path-small-change/commit-msg-t3.txt`:

```text
feat(task-cycle): Record the cycle choice, a foundation touch and a switch in the cycle record

The record template gains a Cycle header line and a Cycle section: the choice at start with the
reason for each finding assessed, a foundation touch on the light cycle with its ruling, and a
switch to the full cycle with the executor's report, the discarded attempt's last commit (a
historical name, reachable only until the reflog expires) and the files it changed. The
foundation route can record the time a touch changed it, the artifacts list spec and plan only on
the full cycle, and the request handoff carries the cycle and its reasons.
```

```bash
git add task-cycle/record_template.md
git commit -F docs/task-cycles/light-path-small-change/commit-msg-t3.txt
git show --stat --format='%h %ae %s' HEAD
git log --oneline c64a607..HEAD
git status --short
```

Expected: three commits on the branch since `c64a607` (Tasks 1–3), each touching only its own
files; `git status --short` shows no tracked change (`.runs/` is ignored). No push.

---

## After the plan (the cycle's steps, not plan tasks)

- Whole-branch review of `c64a607..HEAD` (end of `subagent-driven-development`), then step 10:
  recalculate sharpness from the final diff, rerun `python -B gate/run_tests.py gate`, the tests
  of `elements/decisions` and `elements/invariants`, `installation`, and the three guards; record
  `task-cycle` as unchecked.
- Step 11: the return step, and the one independent assessment (WAY-10,
  `elements/common/critique/SKILL.md`) of the foundation change of Task 1; its record goes in the
  message of the commit that carries its settlement (`agent-instructions/README.md`, "Integrate
  into `foundations`").
- Step 12: swap `<request link>` in both *Approved by* fields for the request URL — a placeholder
  swap that changes no binding part, so no fingerprint moves.
