# Author report — implementation (turn 2)

Status: done — change committed as `2fabc67` on `49d7d2b`; stopped before review.

## Input version

- Input commit `49d7d2b` (foundation step); base `77c8a8b`. Rulings C6–C10 read in the cycle record.
- Read whole: the handoff, Superpowers `test-driven-development` 6.4.1 (from the 6.4.1 cache root),
  the Technology section of `project-level/definition_template.md`, steps 0–3 of
  `project-level/technology/SKILL.md`.

## What changed and why

- `project-level/definition_template.md`, section "Technology" (+22/−0):
  - after the rule of belonging, a rule for WAY-121's exception: where the project brings behaviour a
    user sees in the running product, the logs, the interface and the development data are looked at;
    each matter no foundation decision settles for that behaviour stands on the list as a choice of
    its own, even with nothing added to run, pay for or back up and even where the product has none
    of what the matter names; a matter a decision already settles is not listed (C7); no definition
    has to hold these matters, and a listed one is an ordinary choice with the existing markers
    (To do 2, no new marker) — cited WAY-121;
  - a rule giving what each matter asks, and that data set up from scratch and a persistent dedicated
    test environment are both options — cited WAY-165;
  - after WAY-123's rule and before WAY-137's, WAY-166's weighing rule — cited WAY-166. WAY-137's rule
    is unchanged.
- `project-level/technology/SKILL.md` (+20/−2):
  - step 0: a new bullet, before the open-item and no-open-item branches — whenever "Technology" holds
    a list, take step 1's look at the three matters first, add a missing matter `— open`, and show the
    list again where one was added; an approved definition does not come back for these matters (C10,
    To do 2);
  - step 1: after the rule of belonging, the look at the three matters, only where the project brings
    behaviour a user sees; a matter a decision settles for that behaviour is not listed; a listed one
    is settled like any other choice (WAY-121, WAY-165);
  - step 2.3: in such a choice the comparison says for each option whether an agent can use it, and an
    unusable option stays with the lack "an agent does not check the running product this way"
    (WAY-166);
  - step 2.5: WAY-137's tie rule is said to serve a place to run alone; in such a choice the
    recommendation passes over an option an agent cannot use (WAY-166).
  - The skill keeps its role (order of the work); the rules stand in the template. Its `description`
    is unchanged, so no entry point changes (`skill_entry_points.py` reports them current).

## Files searched and left

Searched `project-level/`, `task-cycle/`, `elements/`, `installation/` for the Technology section's rule
of belonging ("belongs on the list", "choices the project needs", "run, pay for or back up",
"technology choice", "Technology section", "settle-technology"). Found and left unchanged, as none
states the rule in a way the change contradicts:

- `project-level/definition_template.md:104` (section table: "the technology choices the project
  needs, each with the entry that settles it") — still true of every listed item.
- `project-level/definition_template.md:197-198` ("a project whose choices the foundation already
  holds lists each of them `held by`") — about choices of the list; a settled matter is not a choice of
  the list, as the new rule says explicitly.
- `project-level/skill/SKILL.md:121,134,139` (define-project hands technology to step 6) — no rule of
  belonging.
- `project-level/readiness_check.py:27` (condition g) and `project-level/test_readiness_check.py` —
  not to change (To do 2); untouched.
- `elements/decisions/skill/SKILL.md:80`, `elements/decisions/template.md:55` (lacks and risks of a
  chosen option) — unaffected.
- `installation/install.py:34`, `installation/README.md:56`, `installation/test_install.py:27` — the
  skill's path and name only.
- `task-cycle/skill/SKILL.md:339` ("For visible behavior, verify it in the running product as well")
  — the need the change serves; no rule of belonging.

## TDD or manual check

The change is process text with no executable behaviour: the readiness check, the only code that reads
the Technology section, must not change (To do 2), and any test holding the new text would assert
wording, not behaviour. TDD's red–green cycle has nothing to drive, so the text was checked manually
(reading the changed sections whole against rows 1–4, C6–C10 and To do 1–2, and a grep of the added
lines for "must", "always", "every definition", "required", "mandatory" — none) and by the executable
weakest-point check below.

## Weakest-point check (WAY-164)

- Requirement most likely not met: To do 2 — a definition has no mandatory items of the agent's way
  and the readiness gate does not check them. The new template rule sits beside the gate's condition g,
  so wording or a later reading could make the matters required.
- Check: a scratch script (`C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/7c7db354-2a59-4cd6-ae9c-03971825e2f2/scratchpad/weakest_check.py`), run from the worktree
  root, builds definitions with the helpers of `project-level/test_readiness_check.py` for a project
  bringing user-visible behaviour (a playable first map) and runs the real `readiness_check.check`
  before approval and approved: (a) no agent-path matter on the list; (b) the three matters listed
  `held by`; (c) control: one matter `— open`. Expected: no finding for (a) and (b); finding g for (c).
- Actor: author (this agent), on the working tree of `2fabc67` content (run just before the commit,
  same files).
- Observed: (a) no finding in both modes; (b) no finding in both modes; (c) finding g "the choice is
  still open" in both modes; mismatches 0, exit 0. Evidence:
  `.runs/task-cycles/agent-path-technology-step/reports/implementation-weakest-point.txt`.
- Conclusion: the gate requires none of the matters and treats a listed one as any other choice. The
  check does not cover how an agent reads the text — that is left to review.

## Choices, rejected alternatives, cost if wrong

| Choice | Rejected | Cost if wrong |
|---|---|---|
| Template states "a matter a decision of the foundation already settles for that behaviour is not listed" and "no definition has to hold these matters" explicitly | leaving both implicit | Two sentences of template text; without them the `held by` rule of the section could be read as listing settled matters, or the exception as mandatory. |
| Step 0's look runs for every list (open items or none), before the existing branches | only for lists with no open item | A resumed step with open items would continue without the matters; with the chosen order, one extra look per resume. |
| Step 0 says an approved definition does not come back for these matters, without a decision cited | a citation of WAY-118 | It restates what follows from the unchanged gate (To do 2); low. |
| Step 2.5 adds "that tie rule serves a place to run alone" | leaving WAY-137's scope to the template | One clause; it keeps the tie rule from being read into the new choices. |
| No test committed | a new test in `test_readiness_check.py` | That file holds invariant-cited checks (WAY-65), which this stage may not change; the scratch check is recorded instead. |

## Commands, exit codes and outputs

Outputs under `.runs/task-cycles/agent-path-technology-step/reports/`.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B gate/run_tests.py project-level` | 0 | 250 tests OK | `implementation-tests-project-level.txt` |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK | `implementation-tests-gate.txt` |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK | `implementation-tests-agent-instructions.txt` |
| `python -B agent-instructions/skill_entry_points.py` (check mode) | 0 | "entry points are current" | `implementation-skill-entry-points.txt` |
| `git diff --check 77c8a8b..HEAD` | 0 | no output | `implementation-diff-check.txt` |
| weakest-point scratch check | 0 | 0 mismatches | `implementation-weakest-point.txt` |

No failure, warning or `unchecked` in any of these outputs. These are partial checks, not a pass of the
full gate.

## Changed files

`49d7d2b..HEAD`:

| File | Added | Removed |
|---|---|---|
| `project-level/definition_template.md` | 22 | 0 |
| `project-level/technology/SKILL.md` | 20 | 2 |

`77c8a8b..HEAD`:

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 138 | 15 |
| `foundations/invariants.md` | 1 | 1 |
| `project-level/definition_template.md` | 22 | 0 |
| `project-level/technology/SKILL.md` | 20 | 2 |

## Sharpness inputs from the actual diff

- Criticality: `project-level` (high failure modes, among them "a technology choice the project needs
  is missing from the definition's list — not detected"), `decisions` (high), `invariants` (link line
  only).
- Trust-boundary files: none touched (`project-level/readiness_check.py`, `plan_check.py`,
  `plan_state.py` unchanged).
- Irreversible operations: none.

## Unresolved concerns

1. Step 0's look runs on lists of definitions that are still in the step or before the gate; a
   definition with status `ready for gate` returns to `define-project`, not to this skill, so it gets
   the look only if it comes back to the step for another reason. To do 2 asks no more; named for review.
2. Concerns 2–3 of turn 1 (no usable option in a matter; a persistent test environment that is also a
   place to run) stay as C8 rules — no text added for them.
