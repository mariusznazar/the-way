# Final whole-branch review — c64a607..c64d49a (light cycle)

Reviewer: final code reviewer (Superpowers 6.4.1 `requesting-code-review` template), read-only.
Range: c64a6071384fb57cdb9d7e9db4560ddc43e3b355..c64d49ac10baac2fed706314240fad0da6093124
(b977e5f, 3bf1452, c64d49a). Files: `foundations/decisions.md`, `foundations/invariants.md`,
`task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`. Reviewed in one pass over the review
package, plus the HEAD text of the skill in full, every decision binding part whose scope names
`task-cycle` or that speaks of plan, spec, cycle, implementation or foundation step, the glossary
entries *foundation step* and *return step*, the decisions template, and `agent-instructions/README.md`.

## Checks I ran (HEAD c64d49a, Python 3.14, Git Bash, Windows 11)

| Check | Result |
|---|---|
| `python -B gate/run_tests.py gate` | 96 OK (= baseline) |
| `python -B gate/run_tests.py installation` | 16 OK (one-line `description` accepted by the installer) |
| `python -B gate/run_tests.py elements/decisions` | 169 OK (= baseline) |
| `python -B gate/run_tests.py elements/invariants` | 233 OK (= baseline) |
| `python -B gate/run_tests.py task-cycle` | NO TESTS RAN — the part has no tests; its text is unchecked by any test |
| decisions guard `--base none --merge-onto none` (record to scratchpad) | 0 errors, 7 warnings (the baseline 5 + two `<request link>` placeholders at :417 and :3606, as C8 expects), 5 unchecked |
| invariants guard, same flags | 0 errors, 0 warnings, 3 unchecked (= baseline) |
| Fingerprints: binding paragraph of each entry written by Python to a UTF-8 file, fed as bytes to `relation-model/fingerprint.py` | WAY-13 base `c6b33aa9`, head `97b17d59`; WAY-125 base `4c302238`, head `68b2d563`; WAY-100 `e7a74a18` both. Base values equal the carriers at base (positive control). |
| `git grep -E "WAY-1(3|25)@|c6b33aa9|4c302238" c64d49a` | only `decisions.md:3593` (WAY-125 → `WAY-13@97b17d59`) and `invariants.md:262` (`foundation-change-path/1` → `WAY-13@97b17d59`); no stale carrier |
| `git diff --name-only c64a607 c64d49a` | the four files above; **no invariant test, check or other test is written or changed in this branch** |
| Line lengths of added lines | all ≤ 100 except the front-matter `description`, which must be one line |
| `git ls-files --eol` on the four files | `i/lf w/lf`, unchanged |

## Strengths

- The light cycle is placed as a way of *preparing and making* a change inside the foundation route
  of step 4, not as a new WAY-13 path (spec D1). This keeps `foundation-change-path/1`'s sentence
  true without rewording, and WAY-13's "the path chosen by size" in *Rejected* stays valid.
- The four "simple and obvious" conditions are stated identically in the skill
  (`task-cycle/skill/SKILL.md:105-112`) and in WAY-125's binding sentence
  (`foundations/decisions.md:3566-3569`), with the label kept out of the binding part so no glossary
  term is needed (C4). Test-first only for behaviour changes is consistent in WAY-125
  (`decisions.md:3565`, `:3597-3598`) and the skill (`SKILL.md:101`), and matches base step 9.
- Switch and discard say the same thing in the skill (`SKILL.md:121-129`), WAY-125's binding
  sentence and its *Verification* / *Rationale* / *Rejected*: report without code, attempt
  discarded with its entries, fresh design given the report. The record template gives each of these
  a slot (`record_template.md:23-36`).
- WAY-13's new third sentence keeps every safety the rationale relies on: outcome, checks on the
  finished change and the human's decision on irreversible changes all stay out of reach of size.
  The violates example that would have condemned the full cycle for a large task was correctly
  rewritten.
- Dropping D13's agent-written *Rejected* reason (C9, WAY-29) is a justified departure from the
  spec; the switch-and-discard rule in the binding sentence already carries the substance.
- Fingerprints and dependents are complete; versions correctly stay at 1 (no `main`).
- Edits are surgical: exact-text replacements, the rest of the skill untouched.

## Acceptance criterion (task: "Zadanie, które nie spełnia reguły kciuka, przechodzi pełną ścieżką tak samo jak przed zmianą")

Read the whole SKILL.md diff for what a task failing the rule meets: the extra recording of the
cycle choice in step 4 (`SKILL.md:52-54`), the qualifier "On the full cycle" in steps 4 and 9
(`:57`, `:179`), the reworded "the full cycle requires a written spec and plan for every task it
runs" in step 6 (`:137`), the post-switch clause of step 6 (applies only after a switch), the new
section's opening sentence "Every other task takes the full cycle — steps 6 to 9 — exactly as
written" (`:93-94`), and the request naming the cycle in step 13 (`:245-247`). None changes a
step, an agent, a review, a check or a gate of the full cycle. The template adds a `Cycle:` line, a
`## Cycle` section and a request-handoff line — record content only. **Holds.** This also covers
the Task 3 brief's word-diff reading that the ledger says its implementer did not run: I read the
whole template diff and it matches spec §6 exactly.

## Other foundation entries, element skills and project-level files (point 3)

No current entry contradicts the light cycle. Checked binding parts of WAY-01, 03, 09, 11, 13, 16,
21, 25, 26, 28, 30, 33, 36, 44–48, 51, 55, 57, 62, 63, 65, 68, 69, 82, 101, 103, 106, 124, 125, 126:
WAY-01 ("a task that sets out to change the foundation") does not catch a touch found during
implementation; WAY-03/WAY-69 are respected because an invariant or invariant test is excluded from
a light touch; WAY-30's "brings the change into line, drops the change" stays light, a new wording
switches; WAY-10/WAY-11 are met because the touch's entry joins step 11's one assessment. Element
skills and `elements/common/critique/SKILL.md` assume no spec or plan. `project-level/task/template.md:6,68,73`
and `project-level/task/skill/SKILL.md:67` still say "the cycle's plan chooses how" — loose on the
light cycle, which has no plan, but not wrong in effect (D11); see Minor 4.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

1. **WAY-125 does not confine "touch of the foundation" to the executor's work, so a light cycle
   whose return step writes an invariant reads as one that must be discarded.**
   - File: `foundations/decisions.md:3566-3570` (binding sentence) and `:3598-3600` (*Verification*,
     complies example).
   - What: the binding sentence says "a change … whose touch of the foundation … writes or changes
     an invariant or an invariant test, is discarded and starts again". The skill sends the light
     cycle through step 11 "as written" (`SKILL.md:117-118`), and step 11 (WAY-11) routinely writes
     invariants and their checks for "code behaviour with no invariant over it", with separate
     authors and reviewers. The skill confines the switch to "while the change is being made or its
     review findings fixed" (`SKILL.md:121-122`), but that limit lives only in the skill; the
     decision, which binds and which a level-2 agent compares cycles against, does not carry it.
   - Why it matters: an orchestrator or a verifying agent reading WAY-125 literally would discard
     a finished light cycle after its return step, or judge a correct light cycle a violation of
     WAY-125. Small tasks touching uncovered behaviour are exactly where the return step writes an
     invariant, so this is not an edge case.
   - Fix: scope the clause to the executor's work, e.g. "or whose touch of the foundation while that
     agent makes it needs a choice …", and mirror it in the complies example ("an attempt that grows
     too large, or whose touch of the foundation writes an invariant while it is made"). The
     fingerprint then moves from `68b2d563`; no file carries `WAY-125@`, the independent assessment
     has not run yet, so the cost is one recompute and a guard rerun. If the decision is to stay as
     worded, at least add to the skill's "Light cycle" section one sentence saying that entries the
     return step writes are not a touch and follow step 11 as on any task.

### Minor (Nice to Have)

1. **A switch does not re-record the foundation route.** `SKILL.md:121-129`,
   `record_template.md:9-10`. A non-simple touch switches to the full cycle at step 6, skipping
   step 4, and the record's `Foundation route` slot only provides for a *simple* touch ("on the light
   cycle, the time a touch changed it"). The foundation step still runs (it keys on what the task
   changes), so behaviour is correct, but the record can keep saying `unchanged` for a task whose
   full cycle writes entries — the very fact a future check of `foundation-change-path/1` would read.
   Fix: in the switch paragraph add "re-record the foundation route" and widen the template slot to
   "the time a touch or a switch changed it".
2. **Who writes the switch report when the executor cannot be resumed.** `SKILL.md:117-120` lets a
   fresh executor continue "after a ruling or for fixes"; the switch paragraph (`:123-125`) assumes
   the original executor writes the report. A fresh executor writing it would see the attempt's code
   and could carry its shape. One clause would settle it (e.g. the orchestrator writes the report
   from the executor's last return, or a fresh agent reads the attempt and writes the report without
   code).
3. **WAY-125's light clause names only test-first and the final review.** `decisions.md:3563-3566`.
   "uses them all unless …: that agent then makes it, test-first …, and one final code review covers
   the whole change" can be read as the light cycle not adopting the request-preparation method
   (`finishing-a-development-branch`, used in step 12). Sentence 2 ("brings the request to the human")
   and the skill ("steps 11 to 14 as written") cover it, so the risk is low. Can ride with Important 1
   if that sentence is reworded anyway. The first sentence is also ~150 words; it passes the guard,
   but it is hard to verify against.
4. **Project-level task files assume a plan.** `project-level/task/template.md:6,68,73`,
   `project-level/task/skill/SKILL.md:67`. Accepted as D11; record it as a process remark in the
   cycle record, as the spec says, so it is not lost.

## Triage of the ledger's deferred minors and rulings

| Ledger item | Must fix before merge? | Reason |
|---|---|---|
| Task 2: short orphan lines at the end of steps 4, 6, 9, 13 | No | Cosmetic; the base file already has the same pattern (`SKILL.md:141,143,186,209`); C8 chose to rewrap only changed lines to keep the acceptance diff readable. |
| Task 2: foundation step's "A plan member writes only the entries its plan item assigns" has no light counterpart | No | The light touch writes "as the foundation step below gives an entry the cycle writes" (`SKILL.md:109-110`), which carries that rule; a plan item that assigns entries fails finding 1 anyway. Reading risk only. |
| Task 3: `record_template.md:25` finding 1 has no explicit reason slot | No | The section's own instruction "Record the reason for each finding assessed" (`:32`) covers it, and the route's reason sits in the `Foundation route` header line. |
| Task 3: inline code `not assessed` wraps across a line break (`record_template.md:32-33`) | No | A line ending inside a CommonMark code span renders as a space; output is `not assessed`. |
| Task 3: brief step 4 word-diff reading not run by implementer | No (done here) | Covered by this review's acceptance reading above. |
| Ruling: no tests for text-only Tasks 2–3 | Agreed | Nothing can fail first; confirmed no test file changed. |
| C9: D13 *Rejected* item dropped | Agreed | WAY-29; the request must say it was dropped and why, as C9 records. |

## Declined to judge

- Pre-existing tension between `foundation-change-path/1` and the return step writing entries on a
  task whose route is "unchanged" — present at c64a607, not introduced here.
- Pre-existing tension between WAY-126 ("even where the plan assigns the entry to another task") and
  the skill's "one assigned to another item returns to the plan" — present at base.
- Whether "about ten minutes" and "very large / very many files" are the right thresholds — the task
  owner's choice, kept out of the binding part by D3.
- Where the WAY-10 assessment record goes for this branch (guide: commit message; skill:
  `docs/task-cycles/…/reports/`) — a pending step 11/12 matter, not in the diff; the guide governs.
- Quality of the Polish meaning sentences for the request — not in the diff.
- Whether reviews per plan task count as "checks run on the finished change" under WAY-13 — I read
  them as part of how the change is made; the final review of the whole change stays, which is what
  the task (point 1) asks for.

## Recommendations

- Settle Important 1 before step 11's independent assessment, so the assessed WAY-125 wording is the
  final one and the assessment need not be repeated.
- In the request, list the wording beyond the task's words (spec §7 items 1–5) and the dropped D13
  item, so Mariusz sees what he re-accepts at the merge.

## Assessment

**Ready to merge?** With fixes

**Reasoning:** The skill, record template, WAY-13 and WAY-125 agree on the conditions, test-first
scope and switch-and-discard; fingerprints and dependents are correct; the full cycle is unchanged
apart from recording the choice; no test changed. One binding-wording gap (WAY-125's "touch" not
limited to the executor's work) should be closed before the independent assessment; the rest is
optional polish.
