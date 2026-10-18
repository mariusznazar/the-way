# Planner's report — step 8

- Handoff: [plan-handoff.md](plan-handoff.md); skill `task-cycle/plan/SKILL.md` of this worktree.
- Planner: fresh general-purpose subagent, claude-opus-5-5; nothing dispatched, no code, test or
  entry written.
- Written: [../plan.md](../plan.md), [../plan-size.md](../plan-size.md), this report. Nothing else
  in the worktree changed (`git status --short` empty; `.runs/` is ignored).
- Status: **plan written; every slice fits.** No open design choice found that stops the plan
  (step 2); one entry beyond the spec is listed as following from an existing rule, for the root
  to confirm (concern 1).

## Foundation selection (WAY-150)

- Revision: `foundations` `96623ed7710100fe6e11a0ce3c052fc44d4af52d`, the task branch's base;
  worktree clean when read.
- Touched parts: `decisions`, `glossary`, `part-map`, `invariants` (entries); `agent-instructions`
  (entry points), `installation` (`SKILLS`, guidance, README); the root `README.md`, which the
  map leaves out on purpose; read and not changed: `instruction-files`, `relation-model`,
  `elements-common`, `project-level`, `task-cycle`, `gate`; prospective new part
  `product-guidelines` (critical flow `skills-reach-the-way-sessions` gains it).
- Expected *Scope* matches: a script over the whole log (latest version of each of the 152
  numbers, wrapped *Scope* values joined, no repeal in the log) listed every entry's range and
  *Scope*; every one of the 152 names a touched part (`decisions` alone covers nearly all; the
  rest name `project-level`, `task-cycle`, `installation`, `agent-instructions`,
  `instruction-files`, `elements-common`, `relation-model` or `gate`). Selected: the same 152;
  nothing missing. The script's output is the source of every `foundations/decisions.md` range in
  the plan (heading line to the line before the next heading, trailing blank lines trimmed), so
  each range is a whole entry.
- Read whole by the planner: the frozen task, the spec, `reports/spec-review.md` with its
  re-review, `cycle.md` (C1–C24), `foundations/part_map.md`; decisions WAY-03, WAY-09, WAY-48,
  WAY-49, WAY-69; invariants `foundations/invariants.md:140-205` (the six WAY-09 dependants),
  `:860-915` (surfaces), `:1837-1858`, `:2065-2132`; the glossary entry "surface";
  `task-cycle/slice_size.py`, `agent-instructions/skill_entry_points.py`, `installation/install.py:15-195`,
  `installation/test_install.py:15-140`, `gate/run_tests.py:1-60`, the step "Execute, verify and
  review" of `task-cycle/skill/SKILL.md`, the lead-project cycle's plan in git history as a
  precedent.
- Located only (heading, range, *Scope*, *Part*, *Method*): every other decision and invariant.
  Their meaning was taken from the spec, its review and `reports/foundation-selection.md` (a
  map, not proof); each slice's agent reads the ranges named and expands its selection.
- Incoming links to WAY-09: only the six invariants at `foundations/invariants.md:152-202`
  (`grep "WAY-09@"` over every directory of the-way); no decision names it.
- Invariants reached and checked against the plan: `invariant-citation-target` (the form check's
  and F4's citations need the entries first, so F3 precedes S2 and F4); `invariant-method-form`
  (commands are not checked for an existing file, so F3 can name `form_check.py` before S2);
  `decision-scope-names`, `level-one-decision-invariants`, `verification-invariant-derivation`
  (decisions, part map and invariants written in one foundation step before the guards run);
  `path-pattern-reach`, `surface-declaration` (the part map reports the missing pattern target
  and file until S1 and S2 — expected); `skill-entry-points` (red from S4 to S7);
  `installation-claude-guidance` (its tests stay untouched, Choice 3).

## Coverage

Every *To do* item 1–11, the five *Questions carried to cycle*, the WAY-100 adoption, the
outcome of spec §1 and all 27 rows of *Settlements to record* map to an entry or slice in the
plan's *Coverage* table; nothing maps to nothing. Rows to entries follow spec §9.1: rows 1–4 →
G1–G4, 5–6 → G7, 7–12 → G8–G13, 13 → G14, 14 → G16, 15 → G15, 16–22 → G17–G23, 23 → G24,
24 → G5, 25 → the glossary term, 26 → G6, 27 → G5 and G24; G26 carries the common form
(finding 24), G25 the WAY-100 adoption.

## Choices, with costs

As the plan's *Choices* table, for the root to copy into the questions table:

1. The six `guidelines-check-*` checks in their own F4 file
   `product-guidelines/test_form_check_invariants.py`; ordinary tests in
   `product-guidelines/test_form_check.py`. Departs from spec §10's "Tests in
   `product-guidelines/test_form_check.py`". Cost: one more file; otherwise the executors would
   edit invariant tests (WAY-03).
2. The form check in two slices (S2 form, S3 references). Cost: S3 may reshape S2; F4's reference
   tests red between them, recorded.
3. Installer tests in a new `installation/test_styleguide_installation.py`; `test_install.py`'s
   `NAMES` unchanged. Departs from spec §8 and §10. Evidence: `installation/test_install.py:57`
   defines `test_preview_apply_rerun_and_preserve_foundation`, which loops over `NAMES` at
   `:83-96` and cites `installation-claude-guidance/1` at `:97` — a change to `NAMES` changes an
   invariant test. Precedent: the lead-project cycle added `installation/test_lead_installation.py`
   and left `NAMES` without `lead-project`. Cost: `NAMES` stays incomplete; some set-up repeated.
4. The skill's two entry points in S4 by the generator's `discover`/`produce`; the other 30 in
   three batches of ten (S5–S7), S7 running `--write`. Cost: three slices; gate red S4–S7.
5. The surface `guidelines-form-check-command` in F2 — see concern 1.
6. The root `README.md` in S4. Cost: one file; otherwise the README omits a directory.
7. S1 templates before S2 (the form check reads their skeleton at run time).
8. S8 last, on a green gate.
9. The end-to-end temporary-product check split across S1 (`check_instructions.py`) and S3 (form
   check with a reworded decision), not a slice of its own.
10. Decision ranges restated after the foundation stage, before S1's dispatch.

## Size check

- Command: `python -B task-cycle/slice_size.py .runs/task-cycles/product-guidelines-styleguide/plan.md`,
  from the worktree root at `96623ed`; **exit code 0**; full output
  `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/plan-size.md`.
- Result: 8 of 8 slices `fits`, none `too large` or `unchecked`. Estimated tokens to read: S1
  106 500, S2 96 431, S3 82 473, S4 153 309, S5–S7 about 45 100 each, S8 87 340; files to change:
  2, 2, 2, 4, 10, 10, 10, 3.
- Not measured: the reads that exist only after an earlier stage (plan section of that name) —
  the 26 new decisions, the 8 new invariants, the F4 check file, the templates, the form check,
  the skill. They are to be added and the script run again before each dispatch. Largest
  margin risk: S4 (153k now; G5–G25 and the two templates may add some 40–60k tokens).
- Foundation stages, measured as slices in a scratch copy (not part of the plan; the script reads
  only `### Slice` headings): F1 215 315 tokens reading `foundations/decisions.md` whole, F2 97 775,
  F3 126 466, F4 50 493 — all `fits`, exit 0. Copy and report:
  `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/3c9695bb-97dd-4f98-b7ec-dff4bae7e82e/scratchpad/foundation_stages.md`,
  `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/3c9695bb-97dd-4f98-b7ec-dff4bae7e82e/scratchpad/foundation_stages_size.md`.

## Unresolved concerns, with proposed answers

1. **An entry beyond the spec: the surface `guidelines-form-check-command`.** Products'
   invariant methods (`python -B .the-way/product-guidelines/form_check.py …`, spec §3.3) and the
   installer's guidance (§8) name the command, which fits the glossary's "surface" ("something of a
   product that someone outside the product relies on and that the product promises to keep",
   `foundations/glossary.md:205`), and each guard command already has one
   (`foundations/part_map.md:295-341`). I judged it an entry the change makes follow under WAY-49,
   not an open design choice: its only content is the promise in words at the one level, `pinned`.
   Proposed answer: keep it in F2. If the root rules it a design choice, the row drops and no slice
   changes. A similar case not added: a surface for the form of guidelines, as `entry-format` is
   for foundation entries (`:283-287`); the `pinned` policy already covers a change of form, so I
   propose none.
2. **Two departures from the spec's letter** (Choices 1 and 3), both from WAY-03. Proposed answer:
   accept them; the alternative for Choice 3 is to change `NAMES` in the foundation step, covered
   by the independent assessment.
3. **F1 is heavy.** 26 new decisions plus three edits, ~215k estimated tokens when the log is read
   whole. Proposed answer: two dispatches of one foundation author (common decisions and edits,
   then G7–G23), as the plan's F1 says; the WAY-33 search by search, not by a second whole read.
4. **WAY-69 for `guidelines-form` and `guidelines-reference-current`.** Their check is
   `form_check.py` itself (S2, S3 executors); the code they cover is a product's `guidelines/`
   files, of which the-way has none. Sentence (F3), check (S2/S3) and covered files (product
   cycles) still come from different agents; the deliberate break is a crafted guidelines file
   written by the S2/S3 reviewer. Proposed answer: record it so in the cycle's author table.
5. **Gate red from S4 to S7** (stale entry points), and F4's reference tests red between S2 and S3
   — expected states the reviewers of those slices must see recorded, not suppressed.
6. **Not in this plan, carried from the design:** the existing gap that `installation`
   *Depends on* lacks `task-cycle`; possible extra glossary entries ("styleguide", "design token")
   if F1–F3's whole-foundation search finds them needed — a finding there returns to the root
   rather than growing a slice; the version-1 literals of the two citations (root C8); C5's
   provisional reading of *To do* 7, shown at the request.
7. **`reports/run_checks.py all` runs `elements/common`**, which holds no test and exits 1
   (checked: `python -B gate/run_tests.py elements/common` exit 1 at the base); the plan's final
   check in S8 names the thirteen directories explicitly instead.

## Turn 2 — restatement at the closed foundation stage (`8ea4679`)

Dispatch: the root's message after F1a `2181273`, F1b `5fde846`, F2+F3 `eb9ff1e`, F4 `8ea4679`;
rulings C25–C28 in `cycle.md`. Written: `plan.md` (rewritten in place), `plan-size.md`, this
section. No other file changed.

### What changed in the plan

- **Ranges.** Every `foundations/decisions.md` range restated at `8ea4679` from a script over the
  whole log (178 entries; heading line to the line before the next heading, trailing blank lines
  trimmed). WAY-01–WAY-08 kept their lines; WAY-09 is now `234-315`; every later entry moved by
  12 lines; the new entries are WAY-167 `5439-5485` … WAY-192 `6334-6368`. A check over the
  restated plan confirmed each named range starts at an entry's heading and ends before the next
  one (0 not whole). `foundations/invariants.md` kept every earlier line (the renewals changed
  only fingerprints); the new entries stand at `:2133-2212` (`guidelines-form` `2133-2142`,
  `guidelines-reference-current` `2143-2152`, `-check-form` `2153-2162`, `-check-carrier`
  `2163-2172`, `-check-colour-pair` `2173-2182`, `-check-reference-target` `2183-2192`,
  `-check-stale-reference` `2193-2202`, `-check-code-path` `2203-2212`).
- **Post-foundation reads added.** S1: WAY-167–WAY-192 whole (`5439-6368`), the eight invariants,
  the F4 file (its fixtures' headings), `cycle.md:89-92` (C25–C28). S2: WAY-168, WAY-170–WAY-171,
  WAY-176, WAY-188–WAY-189, the form invariants, the F4 file, `reports/check-author.md`,
  `cycle.md:92-92` (C28). S3: WAY-169, the reference invariants, the F4 file,
  `reports/check-author.md`, C28. S4: WAY-167, WAY-172–WAY-192, the two guidelines invariants,
  `cycle.md:91-91` (C27). S8: WAY-167, WAY-183. S5–S7: WAY-127 at its new lines.
- **G names replaced** by WAY numbers in every slice, table and coverage row; the mapping stands
  once in the plan's opening.
- **S1 goal** now requires the required-rule headings verbatim, `### Each role in its meaning`
  exactly (`guidelines-check-carrier`, `foundations/invariants.md:2165`, and the F4 fixtures), and
  carries C27: templates cite their decisions (WAY-171); the "fault of one screen" rule follows
  WAY-178 with WAY-172's value-kept-meaning clause.
- **S2/S3 goals** carry C28: templates read from the script's own checkout (1); the F4 line and
  message assertions are the contract (2); withdrawn identifiers count as references (3); `~~~`
  fences are fenced code (4); S2's report states what a no-option run does on a reference error
  (5); the readings of (6).
- **Foundation stages** marked made, with their commits; the deferred-reads table now holds only
  what S1–S4 write (templates, form check, skill). A new *Choices* row records that S2/S3 read the
  F4 file and the check author's report as the contract.

### Size check

`python -B task-cycle/slice_size.py .runs/task-cycles/product-guidelines-styleguide/plan.md`, from
the worktree root at `8ea4679`: **exit code 0**, 8 of 8 `fits`. Estimated tokens: S1 151 972, S2
126 081, S3 105 463, S4 175 171, S5–S7 about 45 100 each, S8 89 909. Full output:
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/plan-size.md`.
Still unmeasured: the templates (for S2–S4), `form_check.py` (S8) and the skill (S5–S8); S4 has
the least margin (about 75k tokens before the limit).

### Concerns

1. S2 and S3 now read `reports/check-author.md`. It describes the fixtures and assertions, not the
   code; C28 (2) makes the assertions the contract. If the root wants the executors to have the
   test file alone, drop that path from both *Read* fields (S2 and S3 both stay well within the
   limit).
2. Ranges are valid only while no slice changes `foundations/`; none does. If the return step or
   a review changes an entry, restate the ranges again before the next dispatch.
