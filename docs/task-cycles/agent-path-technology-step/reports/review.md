# Whole-change review — reviewer, turn 1

Method: Superpowers `requesting-code-review` 6.4.1, reviewer template
`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md`,
with the cycle-specific checks of `reports/review-handoff.md`. Read-only on the worktree; no subagent;
one pass over the whole diff, then a second pass per check.

## Reviewed range

- Worktree `C:/Storage/repos/the-way-wt/agent-path-technology-step`, branch `task/agent-path-technology-step`,
  working tree clean.
- Base `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988`, head `2fabc67`: 4 files, +181/−18.
  - `49d7d2b` — `foundations/decisions.md` (+138/−15), `foundations/invariants.md` (+1/−1).
  - `2fabc67` — `project-level/definition_template.md` (+22/−0), `project-level/technology/SKILL.md` (+20/−2).
- Read whole: the diff; frozen task `task.md`; cycle record `cycle.md` (C1–C10); WAY-121 at base and
  head; WAY-122, WAY-123, WAY-137, WAY-164 binding parts; the Technology section of the template and
  steps 0–3 of the skill at head; `elements/decisions/template.md` sections Relations, Review, Approval;
  `agent-instructions/README.md`; part map entries `decisions`, `invariants`, `project-level`; glossary
  term list. Author reports read for context only.

### Strengths

- Clean order and separation: `49d7d2b` touches only the foundation; `2fabc67` only the template and
  the skill, each rule cited to the decision it implements (WAY-121, WAY-165, WAY-166).
- Fingerprints are right. Independently recomputed with `relation-model/fingerprint.py`: WAY-121
  `740c254e` (base) → `ed19d693` (head); all five links to WAY-121 carry `ed19d693`
  (`foundations/decisions.md:3526`, `:3578`, `:5359`, `:5403`, `foundations/invariants.md:2027`); new
  links `WAY-100@e7a74a18` and `WAY-123@f3b45293` are current; 450 decision links in `foundations/*.md`,
  0 stale. No reference to `740c254e` remains outside `.runs/`.
- WAY-121's merge of its first and third sentences (`foundations/decisions.md:3429-3434`) keeps the
  meaning: the old text named the holding decision only in the all-held case, the new one names it for
  every held choice, which is what the template's `held by` marker already required
  (`project-level/definition_template.md:150-153`, `:186-190`). The "settles nothing" exit survives.
- The exception is named as an exception in the binding sentence, in the template and in the skill,
  and the template states both negatives To do 2 needs: "No definition has to hold these matters" and
  that a settled matter is not listed (`project-level/definition_template.md:172-174`).
- WAY-166 is placed well: `narrows WAY-123` with the area in its binding sentence (WAY-25), WAY-137
  untouched, and the skill bounds WAY-137's tie rule to a place to run
  (`project-level/technology/SKILL.md:124`). No contradiction with WAY-137's binding part or its
  *Rejected* ("the same tie-break for every choice").
- Verification examples are concrete and taken from the task's Context (loop2 game, CLI tool with
  sample files, shop with a copy of production fetched by a human — WAY-140).
- Nothing from PR #23 slipped in: no `logs:` / `interface:` / `development data:` markers, no gate
  condition, `readiness_check.py` and every test untouched, no return of approved definitions; the
  only "every definition" in added lines is inside WAY-121's *Rejected*.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None.

#### Minor (Nice to Have)

1. **Step 0's look re-adds a matter the human struck, on every resume**
   - File: `project-level/technology/SKILL.md:37-41`
   - What's wrong: the new bullet runs on every list ("Where it holds a list … add each matter it finds
     missing as an item ending `— open`"), not only on lists written before the change. Step 1 lets the
     human "confirm it, add to it or strike from it" (`SKILL.md:75-76`); a matter the human struck is
     "missing" on the next resume and comes back `— open`, and the list is shown again. The same
     resume then shows the list a second time in the next bullet ("Then show the list, ask whether it
     still holds", `SKILL.md:44`).
   - Why it matters: a human who struck, say, development data for a product that keeps none is asked
     again at each resume of a multi-session step; an agent that skips the second showing may continue
     with a matter the human removed. Effect is an extra question, bounded.
   - Fix: limit the look to lists that do not yet record it, or skip a matter the human struck (record
     the strike as a nested item, which WAY-112 already allows under a choice — but a struck item has
     no line, so a short note in the status line or under the section would be needed); and merge the
     two showings into one ("show the list once, with any matter added, and ask whether it still holds").

2. **"its list stays as approved" reads wider than To do 2**
   - File: `project-level/technology/SKILL.md:40-41`
   - What's wrong: To do 2 says an approved definition does not come back to the step *because of*
     these matters. The sentence "A definition the gate has approved does not come back to this step
     for these matters; its list stays as approved" can also be read as: when an approved definition
     does re-enter the step for another reason (the skill itself foresees re-entry, `SKILL.md:169-171`,
     WAY-118), the look is not taken. The task does not settle that case either way.
   - Why it matters: two agents will act differently on the same definition. Low frequency.
   - Fix: keep the first clause, drop "its list stays as approved", or say explicitly what happens on
     re-entry for another reason — and if the latter, name it as a choice for Mariusz, since no row
     settles it.

3. **WAY-121 *Review when* is the author's, not the task's, and its first branch is not a state of the world**
   - File: `foundations/decisions.md:3465-3468`
   - What's wrong: the task gives no review condition or date; the author changed `none` to two
     conditions and `check by: 2027-03-31`. The template asks *Review when* of a decision resting on a
     prediction (`elements/decisions/template.md:227`), and answer 8's "kolejne znajdują je w fundamencie"
     is a prediction, so a review field is defensible; but its first branch — "a project lists a matter
     … that a decision of the foundation already settles" — describes a violation of WAY-121 itself
     (already a *violates* case of its verification), not a state that tests the prediction. The second
     branch (a cycle finds no way to check although decisions stand) is a fair test of it.
   - Why it matters: source fidelity (check 2) — an invented review rule and date enter an approved
     decision under renewed acceptance; the request must show it to Mariusz as such.
   - Fix: keep only the second branch, and name the field and the date in the request's sentence on
     WAY-121's change of meaning.

4. **WAY-165 "are both options of that choice" can read as a fixed pair**
   - File: `foundations/decisions.md:5353-5354`; mirrored in `project-level/definition_template.md:180-182`
   - What's wrong: row 3 says the matter is asked "bez przesądzania, czy to dane zakładane od zera, czy
     trwałe dedykowane środowisko testowe" — neither is ruled out. "Data set up from scratch and a
     dedicated test environment that persists are both options of that choice" can be read as: every
     comparison of development data offers both — for a CLI tool answered by sample input files, a
     persistent test environment is meaningless, and WAY-122 has options come from research, not from a
     given list. The *violates* example ("leaves out … because the data has to be set up from scratch")
     carries the intended narrower reading, but the binding part is what agents act on.
   - Why it matters: research agents receive the template's Technology section verbatim
     (`SKILL.md` step 2.1); a literal one pads comparisons.
   - Fix: e.g. "Neither data set up from scratch nor a dedicated test environment that persists is ruled
     out as an option of that choice." (changes the WAY-165 fingerprint; no entry relates to WAY-165 yet).

5. **One reason in WAY-121's *Rejected* was rebuilt after its source basis was superseded**
   - File: `foundations/decisions.md:3500-3502`
   - What's wrong: answer 3 rejected "one heading split into as many choices as the product needs" because
     "bramka nie sprawdzi kompletności skryptem, o pominięciu decyduje osąd agenta". Answers 7–8 removed the
     gate check, so the entry keeps only "whether a matter is left out would rest on the agent's judgment
     alone" — which also holds, in part, for the chosen way (the agent judges "behaviour a user sees" and
     "settles for that behaviour"). The remaining reason (three named matters each looked at vs. a heading
     the agent splits at will) is still sound, but it is the author's restatement.
   - Why it matters: a rejection reason the human did not give, readable as weaker than the choice it
     rejects; low.
   - Fix: e.g. "— the agent would decide which matters exist, where three named matters are each looked
     at"; or leave and name it in the request.

### Recommendations

- The request must show Mariusz WAY-121's change of meaning (README, WAY-07): the exception, the merged
  first sentence, the new *Review when* (Minor 3), and C6's reading "settles for that behaviour" of
  "jak agent do niego dotrze".
- WAY-121's third binding sentence is ~85 words with a trailing "whose answer then says …" attached to
  "the matter"; splitting is impossible under the three-sentence limit, but a comma-free rewrite of the
  last clause ("…, and then answers what an agent uses in its place") would read better. Polish only.

### Assessment

**Ready to merge?** Yes

**Reasoning:** Rows 1–4 and To do 1–2 are written whole with their meaning, fingerprints and relations
are consistent, the readiness check and invariant are untouched and all checks pass; the five Minor
findings are wording and resume-path refinements that do not break any requirement.

## Coverage

| Item | Where written | Judgment |
|---|---|---|
| To do 1 — step looks at logs, interface, development data; lists each as its own choice when the project brings user-visible behaviour and no foundation decision says how an agent reaches it; settled like any other | WAY-121 sentence 3 (`decisions.md:3434-3441`); template `definition_template.md:167-175`; skill step 1 `SKILL.md:56-63`, step 0 `SKILL.md:37-41` | Covered. "for that behaviour" is C6's reading of "do niego"; resume path see Minor 1–2. |
| To do 2 — no mandatory items, gate does not check them, approved definition does not return | template `:172-174` ("No definition has to hold these matters"); skill `SKILL.md:40-41`; `readiness_check.py`, invariant sentence and tests untouched | Covered; Minor 2 on wording reach. |
| Row 1 — three separate matters, own criterion, even with nothing to keep running; product lacking one still gets an answer | WAY-121 sentence 3 and *Verification* (CLI tool with sample files; "one choice" and "keeps no data" as violations); *Rejected* | Covered whole; nothing beyond the row in the binding part. |
| Row 2 — logs and interface questions, "as its user does" with the three examples | WAY-165 sentence 1; template `:176-179` | Covered whole. |
| Row 3 — development data: source and reaching the state; neither from-scratch nor persistent env decided | WAY-165 sentences 2–3; template `:179-182` | Covered; Minor 4 on "are both options". |
| Row 4 — agent's ability to use an option is a consequence; unusable option stays with the named lack; recommendation passes over it; WAY-137 tie rule stays at a place to run | WAY-166 binding; template `:224-228`; skill 2.3 `SKILL.md:107-110`, 2.5 `:124-126`; WAY-137 unchanged | Covered. The WAY-137 clause lives in WAY-166's *Rationale* and in WAY-137's own unchanged scope ("For a place to run"), not in WAY-166's binding part — acceptable, it states a non-change. |
| *Out of scope* | — | Nothing slipped in: no path from task refinement, no test-run skill, no periodic review, no log-content rules (log content is in WAY-165's *Rejected* only). |
| Closed PR #23 | — | Nothing slipped in (see Strengths). |

## Cycle-specific checks

1. Coverage — see table.
2. Source fidelity — invented content found: WAY-121 *Review when* and its date (Minor 3); one rebuilt
   rejection reason (Minor 5). Everything else traces to the task: the adoption sentence and the excluded
   hard limit (Context line 62), all verification examples (Context line 64, answer 6), the rejections of
   answers 2, 3, 7, 8 (superseded answer 4's rejections correctly not carried).
3. Order — confirmed: `49d7d2b` (foundation only) precedes `2fabc67` (template and skill only).
4. Consistency — fingerprints and relations confirmed (Strengths). WAY-121 merged sentence keeps its
   meaning. No contradiction found with WAY-137 (scope "a place to run"), WAY-139 (deployment-time log
   reading), WAY-143, WAY-106 (step writes only into the definition), glossary (`surface` absent from all
   added lines; no *Avoid* word; no glossary term used in another meaning).
5. Sharpness — confirmed from the part map: `project-level` high (failure mode "a technology choice the
   project needs is missing from the definition's list — not detected", `part_map.md:116-117`, the one this
   change addresses and still not detected, as To do 2 requires); `decisions` high (`part_map.md:15-17`);
   `invariants` no failure modes. Trust-boundary files `project-level/readiness_check.py`, `plan_check.py`,
   `plan_state.py` (`part_map.md:132-134`) untouched. No irreversible operation (task branch only).
6. Weakest point — see below.
7. Invariants — confirmed: `foundations/invariants.md` changes one line, `Derives from: WAY-121@740c254e`
   → `@ed19d693`; no file with a `# invariant:` test is in the diff (no test file changed at all). No
   deliberate break is due.

## Weakest-point judgment (WAY-164)

The author named To do 2 and ran the real `readiness_check.check` on three built definitions, before
approval and approved (`implementation-weakest-point.txt`: no finding without the matters, none with
them `held by`, finding g on a matter `— open`; 0 mismatches). The check is correctly built and its
control case shows it can fail. But because `readiness_check.py` is untouched and its 250 tests pass,
its outcome was fixed by construction: it confirms the gate's half of To do 2, which this change could
not have broken. The half of To do 2 that the change could break lies in text — whether the template or
skill makes the matters mandatory or sends an approved definition back — and the author left that to
review. I read it: nothing makes the matters mandatory, and only the wording issue of Minor 2 touches
the return of approved definitions. The requirement more likely to be missed was in the resume path of
To do 1 (step 0, Minor 1–2), which no executable check covers. Judgment: the check is adequate as a
regression control and honestly reported, but weak as a weakest-point choice; it does not hide any
defect, and no further check is needed for merge.

## Declined to judge

- WAY-166 when no option of a matter is usable by an agent — "the recommendation passes over it" then
  leaves none to recommend; row 4 does not settle it (C8). For the executor and Mariusz.
- A persistent test environment as an option of development data is also a place where the product runs:
  my reading finds no collision with WAY-137, whose binding part covers the options of a place-to-run
  choice and "how well" an agent works, not "whether" it can; left to the independent assessment (C8).
- Definitions at status `ready for gate` (not approved) never re-enter the skill, so they miss the look
  (author concern 1) — To do 2 asks no more.
- C6's reading of "jak agent do niego dotrze" as reaching the behaviour, not the product — ruled by the
  orchestrator; for the request.
- WAY-165 reusing the number of closed PR #23's entry (C9) — a request note, not a defect of the log.
- Whether agents apply the criterion ("behaviour a user sees", "settles for that behaviour") consistently
  — level 2 judgment; no executable check is possible without a gate condition, which To do 2 excludes.

## Commands, exit codes and outputs

All from the worktree root, Git Bash, outputs under `.runs/task-cycles/agent-path-technology-step/reports/`.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B gate/run_tests.py project-level` | 0 | 250 tests OK | `review-tests-project-level.txt` |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK | `review-tests-elements-decisions.txt` |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | 0 errors, 8 warnings (WAY-03/21/52/55/69 passed check-by dates, pre-existing; `merge of <request link>` placeholders at lines 3470, 5374, 5414, expected), 5 unchecked (two from `--base none`, three from `--merge-onto none`, among them fingerprints) | `review-guard-decisions.txt` |
| Fingerprint recomputation (scratch script outside the worktree, `relation-model/fingerprint.py`) | 0 | WAY-121 `740c254e`→`ed19d693`; 450 links, 0 stale — covers the guard's unchecked fingerprints | not saved in the worktree (script: `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/7c7db354-2a59-4cd6-ae9c-03971825e2f2/scratchpad/fp_check.py`) |

These are partial checks, not a pass of the full gate.
