# Slice 6 report — the skill `maintain-coding-guidelines` and its entry points

Executor S6 (Claude Code general-purpose subagent, claude-opus-5-5). Worktree `/home/user/the-way`,
branch `claude/gallant-albattani-3k15lc`. BASE `faf43c9`; commits `d5fd8ca`, `aaaab9d`. Python
3.13.16 (`python3`; the repository declares 3.14 — unchecked on 3.14). Not pushed.

## What I implemented

- `product-guidelines/coding/SKILL.md` (new, 258 lines), modelled on
  `product-guidelines/styleguide/SKILL.md`: frontmatter `name: maintain-coding-guidelines` and the
  one-line description of spec §6.1, starting "Use when" (a safe plain YAML scalar: the generator
  accepted it); where the-way lies, the `the-way-` prefix, no Superpowers method (WAY-125), the
  order of the work only with the rules left in the two templates; what it takes from outside
  sources pointed to WAY-195 and described without naming them (no "Open Mercato", "Google" or
  author in the file — WAY-27); "Where the skill works" with the writes/never-writes table (task
  document and reports under `.runs/coding/` only; never the foundation, guidelines, code or any
  tracked file); §6.5 as one sentence (a product with an older pin reaches the skill through the
  task that moves the pin, `installation/README.md`); "What reaches the task document" (§6.4);
  "Orchestrated mode" (§6.3, the fresh judging agent of the trial run requested from the
  orchestrator); steps 0 Read, 1 Recognize, 2 Starting set, 3 Trial run and audit, 4 Settle with
  the human, 5 Hand back (§6.2).
- `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md` and
  `.agents/skills/the-way-maintain-coding-guidelines/SKILL.md`: written in process by
  `slice-6-write-two.py` (copy of the scratch script), which loads `agent-instructions/skill_entry_points.py`,
  calls `produce(discover(ROOT))` and writes only these two paths; never by hand, never `--write`.
  Its `verify` mode confirms both files equal the produced bytes at `aaaab9d`.
- `README.md`: `product-guidelines/coding/` named beside `product-guidelines/styleguide/` in the list
  of directories ("the coding guidelines' in `product-guidelines/coding/`") and in the list of skill
  directories.
- Second commit `aaaab9d`: the no-code mode and "A new kind" now say when the files come into being
  (WAY-209), found while building the requirements table below (row 19 was only implicit).

TDD: not applicable — process prose, no behaviour change and no test asserts it (brief: "process
prose, no test asserts it").

## Checks (at `aaaab9d` unless noted; outputs beside this report)

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B agent-instructions/skill_entry_points.py` | 0 | 0 `would create`, 0 orphan, exactly 32 `would change` — the 16 other skills × 2 directories (list below) | `slice-6-entry-points.txt` |
| in-process byte comparison of the two entry points with `produce(discover(ROOT))` | 0 | both `equal`; the two files are identical (`cmp`) | `slice-6-entry-points-bytes.txt` |
| `python3 -B gate/run_tests.py agent-instructions` | 1 | 18 tests, 1 failure: `test_skill_entry_points.TrackedEntryPoints.test_the_tracked_entry_points_are_what_the_generator_produces` (first stale path `.claude/skills/the-way-critique/SKILL.md`) — expected until S10 | `slice-6-tests-agent-instructions.txt` |
| `python3 -B gate/run_tests.py gate` | 1 | 98 tests, 1 failure: `test_skills_reach_the_way_sessions.SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way` — 16 `.claude` entry points name no `maintain-coding-guidelines` — expected until S10 | `slice-6-tests-gate.txt` |
| `python3 -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | 0 errors, 0 warnings, 7 unchecked (base none and no reporting commands); new files claimed (`product-guidelines/**`, `.claude/skills/**`, `.agents/skills/**`; `README.md` is on the list of files left out on purpose) | `slice-6-part-map-guard.txt` |
| `git diff --check faf43c9..HEAD` | 0 | clean | `slice-6-diff-check.txt` |
| `python3 -B gate/run_tests.py product-guidelines` (extra, at `d5fd8ca`; `aaaab9d` changes only SKILL.md prose) | 0 | 137 tests OK | `slice-6-tests-product-guidelines.txt` |
| `python3 -B product-guidelines/form_check.py --record <scratch>` (extra, at `d5fd8ca`) | 0 | 0/0/0; no `guidelines/` in the-way | `slice-6-form-check.txt` |

The 32 `would change` paths (S7–S10): `.claude/skills/` and `.agents/skills/` each for
`the-way-critique`, `the-way-define-project`, `the-way-find-foundation-entries`,
`the-way-implement-task`, `the-way-lead-project`, `the-way-maintain-instruction-files`,
`the-way-maintain-styleguide`, `the-way-plan-project`, `the-way-plan-task`,
`the-way-record-decision`, `the-way-record-environment-fact`, `the-way-record-glossary-term`,
`the-way-record-invariant`, `the-way-refine-task`, `the-way-settle-technology`,
`the-way-update-part-map`. The only difference is the sibling list gaining
`maintain-coding-guidelines`.

Failed checks: the two expected entry-point tests above, by name; not suppressed. Unchecked: Python
3.14 behaviour; the installer and `installation` tests (S11's).

## Requirements table (rows and *To do* against the sentence that carries each)

Line numbers are of `product-guidelines/coding/SKILL.md` at `aaaab9d`; "template" is
`product-guidelines/coding/template.md`.

| Item | Meaning (short) | Carried by |
|---|---|---|
| row 2 | a product decision designates the exemplar; script-checkable parts become rules with invariants; rest is example | SKILL 186–188 ("what a script can check of that exemplar … as the kind's rules, the rest of the exemplar standing as an example (WAY-198)"); SKILL 220–221 (settles exemplar and its rules); template 181–185 (rules of a kind file; `## Examples` the rest) |
| row 3 | no file of a kind → the task creating the first designates it; several → audit, compare, `copy`/`do not copy`, human approves | SKILL 191–193 ("A new kind … that file is the kind's exemplar … (WAY-200, WAY-209)"); SKILL 180–190 ("judge every file of it the product holds, compare them, and propose" … `do not copy` / `copy`); SKILL 200–204 (every choice put to the human) |
| row 5 | three standing checks required; departure only by a decision with reason; the task ends with an adopting or departing decision for each | SKILL 211–212 ("for each standing check, the product's decision adopting it or departing from it with its reason; the task is not ready without one for each (WAY-202)"); SKILL 252–254 (hand-back check); template 59–62, 166–167 |
| row 8 | split from a trial run judged by an agent that did not write the code; no-code product takes recommended rules (weak point); later false alarm → decision change | SKILL 164–175 (trial run in a scratch worktree or temporary environment; "one fresh agent that wrote none of that code … whether the report leads to a change of code worth making … A rule with one report that leads to no such change goes among the examples"); SKILL 157–158 (no code: recommended rules); SKILL 238–240 (weak point named, decision change approved by the human) |
| row 14 | ask every choice incl. recommended, by effect in plain words, never rule names or config values; decisions, not single rules | SKILL 200–209 ("How to show … never by the name of a linter's rule or a value of a tool's configuration … Put every choice to the human, a choice the skill recommends included … Ask for decisions, never for single rules (WAY-194, WAY-113)") |
| row 18 | every part with code gets coding guidelines; general file names them in *Applies to* | SKILL 116–117 ("Name the parts of the product's map that hold code, the scripts of its build included, however small (WAY-208)"); template 66–67 |
| row 19 | no code → general file before the first task writing code; kind file with the first file of its kind | SKILL 125–126 ("no code: the starting set of step 2, so that the general file with its standing checks comes into being before the first task that writes the product's code (WAY-209)"); SKILL 191–192 ("its file of guidelines comes into being with it (WAY-200, WAY-209)") |
| row 20 | extend what exists; a new tool is the human's question with the default recommendation of the most used tool, from sourced research | SKILL 131–133 ("Extend what exists … A new linter, formatter or audit of dependencies is a technology choice: record it as a question of the task, never settle it (WAY-210, WAY-121)"); SKILL 147 ("which of them is most used in that technology — the default recommendation (WAY-210)") |
| row 21 | tools and sets from human preferences, else research with page and version and critique; again at refresh/extension | SKILL 137–156 (one question of assessment; "Where the human has none, and at every refresh or extension, research …"; "Each source is a page with its version"; critique, `critique: passed`, no critic no research (WAY-211, WAY-120)) |
| row 22 | the audit ends with an exemplar per kind with one sentence of gain, and `do not copy` files with file:line | SKILL 180–190 ("its exemplar, with one sentence of what the product gains by it" … "`do not copy` … with the file and line of the place that breaks it"); SKILL 81–84 (*Context* carries them) |
| *To do* 2 | the skill, on the pattern of `maintain-styleguide`: recognize, extend, new tool as question with default recommendation; preferences, else research and critique; propose for every part with code, before the first code in a no-code product; ask every choice by effect | SKILL 1–25 (frontmatter, the model's form); steps 1–2 (lines 114–158); SKILL 125–126 and 116–117 (WAY-209, WAY-208); SKILL 200–209 (WAY-194) |
| *To do* 3 | exemplar binding, approval of changes, script-checkable rules, audit with statuses and gain sentence, file:line | SKILL 180–193, 220–221 (exemplar, statuses, rules; WAY-198–WAY-201); approval of a changed exemplar stays with WAY-199 and the template 169–180 (the skill settles the designation in the task, SKILL 40–43, 220–221) |
| *To do* 4 | standing checks required, departure by decision, research, adopted set binds by decision, audit of the change only, blocking only without false alarms, split from trial, listed-violation pair, one reformatting, fault fixed in the file, bind from the guidelines task | SKILL 211–219 (adopt/depart each; linter tool, set, edition, parts, split; "a fault of one file is fixed in that file, and turning a rule off for the whole product takes a change of this decision" (WAY-207); audit tool, database, severity with every severity among the ways (WAY-206)); SKILL 164–179 (trial run, WAY-205 pair, one reformatting); SKILL 222–223 (adopting decision, WAY-193); SKILL 229–234 (blocking list kept, C4; WAY-205 pair with its weak point); SKILL 241–244 (audit weak points, C10); template 131–165, 215–242 |
| *To do* 7 | the skill adds to root `AGENTS.md`, outside the installer's block, the pointer to `guidelines/coding.md` with "before changing code"; the general file's table of kind files | SKILL 64–67 ("apply `maintain-instruction-files` for the pointer … one line naming `guidelines/coding.md` in backticks with the condition of changing the product's code, naming no file of a kind and no command of its own (WAY-212, WAY-16)"); template 70–72, 123–130 (the table) |

Rulings named in the dispatch: C5 — SKILL 68–70 (configuration files to the part holding the build
configuration, through `update-part-map`); C10 — SKILL 241–244 (both weak points of WAY-206 named
to the human); C12 — SKILL 61–63 (each script reads a test case at a new path within its parts);
C13 — SKILL 182–183 ("judge every file of it the product holds"); C33 — SKILL 53–55 (the test cases
as the common template's "Test cases of a rule" gives them, "its limit on the lines of a case that
open a fence included"); trial run in a scratch worktree or temporary environment with the fresh
judge started by the orchestrator in orchestrated mode — SKILL 164–169, 95–100.

## Sharpness inputs (from `git diff --numstat faf43c9..HEAD`)

| File | Added | Removed |
|---|---|---|
| `.agents/skills/the-way-maintain-coding-guidelines/SKILL.md` | 15 | 0 |
| `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md` | 15 | 0 |
| `README.md` | 5 | 3 |
| `product-guidelines/coding/SKILL.md` | 258 | 0 |

- Parts touched (by `foundations/part_map.md`): `product-guidelines` (the skill),
  `agent-instructions` (the two entry points). `README.md` is on the map's list of files left out
  on purpose.
- Trust-boundary files touched: none (`product-guidelines/form_check.py` untouched).
- Irreversible operations: none. Invariant tests and foundation files untouched.

## Choices made (how to make what is settled; none left a way open in the task, spec or foundation)

1. **Which kinds the task audits.** The skill names the kinds the product holds files of and the
   human settles which the task audits; a kind left out stays in *Context*, deferred (SKILL
   180–182). Evidence: WAY-201 speaks of "each kind of code it audits"; the styleguide skill lets the
   human say which user interface a task covers. A product with many kinds would otherwise make
   one task audit all of them.
2. **No trial run or no judge → no split.** Where the set cannot run in the scratch place or no
   fresh agent can judge, the skill stops and says so (SKILL 173–174), as research with no critic
   stops (WAY-211/WAY-120 pattern). WAY-204 gives the split only from a trial run for a product
   with code.
3. **Missing parts for code.** Before the first code, where the map holds no part for the code, its
   identifier is a question of the task and *To do* adds the part through `update-part-map` (SKILL
   117–119, 69–70) — the styleguide skill's way for a missing user-interface part; the general
   file's *Applies to* must name parts the map holds.
4. **Modes combine** (SKILL 124): a task creating the first file of a kind in a product with no
   guidelines takes both modes' steps, since a kind file needs the general file (WAY-167,
   `guidelines-check-kind-index`).
5. **Terms of the field explained before use** (SKILL 207–209): from WAY-194's "plain words" and
   K2 (the human is no developer); WAY-174's explicit clause is the styleguide's, so it is cited
   to WAY-194/WAY-113 here.
6. **Trial-run output** goes to `.runs/coding/` with the judge's verdicts beside it; no file name
   fixed (spec §6.2 fixes none).

## Weakest point (WAY-164)

- **Requirement most likely unmet:** spec §6.1 / brief — the skill "holds the order of the work only
  and restates no rule" of the templates (the dispatch adds: nor of WAY-193–WAY-212), while it must
  follow all twenty decisions.
- **Check:** `slice-6-weakest-overlap.py` (method: mechanical, actor: this executor) lists every run
  of 8 or more words the skill shares with `product-guidelines/coding/template.md`,
  `product-guidelines/template.md` and the binding sentences of WAY-193..WAY-212, merged into
  maximal runs; then each run judged by hand.
- **Observed (`slice-6-weakest-overlap.txt`):** with the templates, 5 runs — two are pointers
  ("as the section test cases of a rule"; the part "whose files direct whoever carries out its
  tasks"), three are what the skill settles or shows the human (the exemplar's checkable parts;
  "a fault of one file is fixed in that file", said to the human with the linter's split; the
  audit's tool, database and severity as things to settle). With the decisions, 15 runs, each a
  step the decision gives the skill (e.g. WAY-204's "a rule with one report that leads to no such
  change goes among the examples"), cited to its decision. No rule of form — headings, tables,
  the closed list of *Status*, the shape of a test case, pinned versions, the record of a run — is
  restated; the skill points to the template's sections for them. Verdict: requirement met, with
  the decisions' content appearing as steps cited to them, as the styleguide skill does with
  WAY-183–WAY-192.

## Self-review

- Every spec §6.1–§6.5 item has a place; §6.5 is one sentence (no mechanism, as the spec says).
- Glossary: "exemplar" and "standing check" in their defined senses; "element" only as a division
  of the foundation; no "guard", "pattern" or "surface"; "read off" avoided ("found in the
  product's files").
- Lines wrap at 100 characters; the entry points are generated, not edited.

## Concerns

- Expected red until S10: the two entry-point tests named above (32 stale entry points).
- The S5 review's process remark (task-cycle `SKILL.md` line 63 "writes only in the task's
  worktree" vs a scratch worktree) bears also on this skill's trial run in a scratch worktree of
  the product, though the skill runs in refinement, not in the cycle; noted only.

## Fix round — final review I1 (ruling C38)

Executor S6, resumed. FIX_BASE `5808fc7` (WAY-201 now reads "a proposed exemplar for each kind of
code the product holds files of"); commit `5a00041` (`product-guidelines/coding/SKILL.md` +9/−7).
Python 3.13.16.

- **Finding:** `SKILL.md:180-183` had the human settle which kinds of code the task audits, with no
  recommendation — against WAY-194 (every choice with a recommendation) and rows 3 and 22 (every
  kind).
- **Fix:** step 3 "Kinds" now names the kinds with their files "and recommend[s] auditing every one
  of them. The human may defer a kind, as a choice put to them in step 4; the task document records
  each deferred kind with the human's reason in *Context*." To keep the file consistent, step 4
  "What it settles" gains "each kind the human defers rather than audit, with the reason (…,
  WAY-201)", and "What reaches the task document" → *Context* gains "each kind the human deferred".
  Frontmatter unchanged. This replaces choice 1 of "Choices made" above.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B agent-instructions/skill_entry_points.py` (working tree before the commit; rerun at `5a00041`, same) | 0 | `entry points are current` | `slice-6-fix1-entry-points.txt` |
| `git diff --check` (working tree; rerun `5808fc7..HEAD`, clean) | 0 | clean | `slice-6-fix1-diff-check.txt` |
| weakest-point check on the new sentence | — | see below | `slice-6-fix1-weakest.txt` |

**Weakest point (WAY-164).** Requirement: the deferral is itself a choice that WAY-194 has put to
the human with ways, cost and a recommendation, and it is not left as a silent narrowing of WAY-201.
Check (manual plus grep, by this executor): every mention of choosing, deferring or recommending
kinds in the skill. The old "the human settles which kinds" is gone. The recommendation stands in
step 3 (line 181). The deferral is routed to step 4 (line 182), whose "How to show" gives every
choice its ways, cost and recommendation, and which now lists the deferred kinds among what it
settles (line 222). The reason is recorded in *Context* (lines 82–83). The overlap script
(8-word runs) shows no new shared run with WAY-194, WAY-200 or WAY-201: the new sentence restates
no rule. Remaining note: a deferral, recorded with its reason, still leaves a kind without the
exemplar that WAY-201's sentence proposes for every kind. That is the coordinator's ruling (C38),
not a new choice.

## Fix round 2 — ruling C39 (revises C38)

Executor S6, resumed. FIX_BASE `355a240`. Commit `f34e477` (`product-guidelines/coding/SKILL.md`
+8/−10). Python 3.13.16.

- **Ruling:** WAY-201 (row 22) has the audit end with a proposed exemplar for every kind the product
  holds files of, with no exception, so the deferral added in C38 goes.
- **Change:** step 3 "Kinds" now reads "Name the kinds of code the product already holds files of,
  each with its files; the audit covers every one of them. For each kind, judge every file of it
  the product holds, compare them, and propose:". The C38 recommendation is now a plain statement.
  Step 4's list reads "for each kind the product holds files of, and each new kind, its exemplar,
  the status of each of its files and the rules a script checks of the exemplar (WAY-198, WAY-199,
  WAY-200, WAY-201)". The *Context* line is back to its pre-C38 wording, with no deferred kinds.
  Frontmatter unchanged.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B agent-instructions/skill_entry_points.py` (working tree on `355a240`; rerun at HEAD, same) | 0 | `entry points are current` | `slice-6-fix2-entry-points.txt` |
| `git diff --check` (working tree; rerun `355a240..HEAD`, clean) | 0 | clean | `slice-6-fix2-diff-check.txt` |
| weakest-point check | — | see below | `slice-6-fix2-weakest.txt` |

**Weakest point (WAY-164).** Requirement: no trace of a way to leave a kind un-audited remains. A
step that still let the human choose kinds, or a *Context* or step-4 entry for deferred kinds, would
narrow WAY-201 again. Check (grep by this executor) for `defer`, `audited`, `which kinds`,
`recommend auditing` and `covers every`. The only hits are the description's "existing code audited
for them" (unchanged), the *Context* phrase "a finding the task does not take up marked deferred"
(audit findings, pre-C38 wording, not kinds) and the new "the audit covers every one of them"
(line 181). The overlap script finds no new 8-word run shared with WAY-194, WAY-200 or WAY-201:
nothing is restated.
