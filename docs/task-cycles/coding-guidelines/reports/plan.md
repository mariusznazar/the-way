# Planner's report — coding-guidelines (step 8)

- Agent: planner (fresh general-purpose subagent, Claude Opus 5.5), skill the-way `plan-task`
  (`task-cycle/plan/SKILL.md` at `235b0b4`), dispatched by `reports/plan-handoff.md`.
- Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc` at `235b0b4`; no tracked
  file changed, nothing committed (`git status --short` empty after the work; `.runs/` is ignored).
- Status: **plan complete; every slice fits**. Boundary reached: the finished plan with its size
  report; no slice made.

## Outputs

- Plan: `docs/task-cycles/coding-guidelines/plan.md`
- Size report: `docs/task-cycles/coding-guidelines/plan-size.md` — command
  `python3 -B task-cycle/slice_size.py docs/task-cycles/coding-guidelines/plan.md` from the
  repository root, Python 3.13.16, exit code 0; the full output is the file itself.
- This report.

## Inputs read

Whole: `task-cycle/plan/SKILL.md`; `task-cycle/skill/SKILL.md`; `task-frozen.md`; `spec.md`;
`reports/design-rulings.md` (C1–C21); `cycle.md`; `agent-instructions/README.md`;
`foundations/part_map.md`; the plan of the previous cycle (`git show cf27d79:docs/task-cycles/product-guidelines-styleguide/plan.md`,
structure only); `product-guidelines/template.md`; `task-cycle/slice_size.py:1-150`.
Read in part, to name each slice's files and ranges: "Reading the foundation" in
`elements/common/way_of_working.md`; `foundations/invariants.md:136-144`, `:1107-1115`,
`:1487-1495`, `:2065-2103`, `:2133-2228`; `foundations/decisions.md:71-93` (WAY-03), `:1907-1936`
(WAY-65), `:4151-4223` (WAY-136); the headings of every decision, invariant and glossary entry
(ranges computed by a script in the scratchpad); `product-guidelines/form_check.py` (docstring,
`read_templates`, `check_parts`, `Foundation`, function list); `product-guidelines/test_form_check_invariants.py:1-230`
and its test list; `product-guidelines/test_form_check.py:130-150`, `:255-290`;
`product-guidelines/styleguide/template.md:1-60`; `installation/install.py:20-45`;
`installation/test_install.py:15-35`, `:70-140`; `installation/README.md:55-137`;
`installation/test_styleguide_installation.py:1-40`; `agent-instructions/skill_entry_points.py`
(docstring, `produce`, `main`); one entry point (`.claude/skills/the-way-plan-task/SKILL.md`);
`gate/test_skills_reach_the_way_sessions.py` (outline); evidence only: `reports/design.md`
(concerns and revision sections), `reports/spec-review.md:195-232`.

## Open design choice (plan-task step 2)

None found. Every entry the change needs stands in a row, the spec's §8 or the rulings. Two points
looked like candidates and are not:

- `installation/test_install.py` is an invariant test file (its test at `:83-97` iterates `NAMES`
  and cites `installation-claude-guidance/1` at `:97`; WAY-65 makes the file an invariant test).
  The spec (§3.1, §6.6) changes `NAMES`; WAY-03 sends that change to the foundation step. This
  is a route for a settled change, not a choice of what to build: the plan puts it in F4.
- The styleguide's template and skill could mention the test cases. The spec's file list names
  neither, the common template's rule binds every discipline (C1) and the form check reports a
  missing pair, so this is a choice of how, listed under *Choices*.

## The plan in short

Foundation stages before any slice (each through the pinned element skill, with WAY-33's search
and the guards): **F1a** WAY-167 and WAY-168 in place, the WAY-31 renewals of WAY-171, WAY-173 and
WAY-188, WAY-193–WAY-202 (WAY-195's public sources re-read); **F1b** WAY-203–WAY-212; **F2** the
glossary terms "exemplar" and "standing check" (and the conditional C2 term) and the two part-map
failure modes; **F3** the carrier edit, the check-form link and the four new invariants, by the
sentence author; **F4** the invariant tests (`product-guidelines/test_form_check_invariants.py`
and `installation/test_install.py` `NAMES`) by a check author who is neither the sentence author
nor an executor of S2, S3, S4 or S11.

| Slice | Goal | Files changed | Estimated tokens read at `235b0b4` | Verdict |
|---|---|---|---|---|
| S1 | common template: coding names, test-case rule, exemption | 1 | 93 406 | fits |
| S2 | coding template + form check reads two forms, non-role tables, carrier per form; fixtures moved off `coding` | 3 | 166 227 | fits |
| S3 | form check: index of kinds, files of a kind (exemplar) | 2 | 133 857 | fits |
| S4 | form check: test cases; filled product end to end | 2 | 155 982 | fits |
| S5 | task-cycle sentence for the reviewer | 1 | 80 943 | fits |
| S6 | skill `maintain-coding-guidelines`, its two entry points, root README | 4 | 150 848 | fits |
| S7 | entry points: critique, define-project, find-foundation-entries, implement-task | 8 | 45 644 | fits |
| S8 | entry points: lead-project, maintain-instruction-files, maintain-styleguide, plan-project | 8 | 45 497 | fits |
| S9 | entry points: plan-task, record-decision, record-environment-fact, record-glossary-term | 8 | 45 738 | fits |
| S10 | entry points: record-invariant, refine-task, settle-technology, update-part-map; `--write`; inventory current | 8 | 45 621 | fits |
| S11 | installer `SKILLS`, README, new installation test; final full check set | 3 | 91 645 | fits |

The sizes are measured on the files at `235b0b4`. The reads the foundation stages and earlier
slices add or move are tabled in the plan with an estimated margin: after them S2 stands at about
211 000 of 250 000 estimated tokens, the least room of any slice; every other slice stays under
about 190 000. The plan names the fallback if S2's re-measured size exceeds the limit.

Execution recommendation: sequential, S1 → … → S11 (Superpowers 6.4.1 `subagent-driven-development`
forbids parallel implementation subagents). Possible parallel work, named for the ruling: S5
beside S2–S4; S6–S9 beside S3–S4; S7, S8 and S9 side by side — all limited by one shared worktree
and index, installation tests that install the committed `HEAD`, and the gate's entry-point test,
red from S6 to S10.

## Checks run by the planner

| Command or manual check | Exit code and result | Output |
|---|---|---|
| `python3 -B task-cycle/slice_size.py docs/task-cycles/coding-guidelines/plan.md` (final) | 0; 11 slices, all `fits` | `plan-size.md` |
| same command on two earlier drafts | 0 each; the first measured S2 at 177 376 tokens, after which its foundation ranges were narrowed (WAY-176–WAY-187 dropped from S2) | not kept (superseded by the final run) |
| `curl -sS -o /dev/null -w "%{http_code}"` on the WAY-195 sources (reachability only, nothing read or quoted) | `raw.githubusercontent.com/open-mercato/open-mercato/4374c48…/AGENTS.md` 200; `research.google/pubs/lessons-from-building-static-analysis-tools-at-google/` 200, its PDF `storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf` 200 (607 313 bytes); `cacm.acm.org` (two URLs) and `dl.acm.org/doi/10.1145/3188720` 403 | stated in the plan, F1a |
| `grep -rn "681d47ff\|47d9d53e"` over tracked `.md` and `.py` files | WAY-167's fingerprint carried by nothing; WAY-168's by `foundations/decisions.md:5631` (WAY-171), `:5720` (WAY-173), `:6246` (WAY-188) and `foundations/invariants.md:2169` (`guidelines-check-carrier`) — as the spec says | manual |
| Python available | `python` and `python3` are 3.13.16; `.python-version` declares 3.14 | manual |

No test, guard or form-check run: the planner changes no tracked file, and the baseline runs are
the orchestrator's (`reports/baseline-*.txt`).

## Choices

Copied whole in the plan's *Choices* table (14 rows): F1 split; `NAMES` in F4; template with code
items 1, 2, 6 in S2; form check in three slices; styleguide files unchanged; root README in S6;
entry points in four batches of eight after S6's own two; S5 before S6; the C12 check in S1 and
end to end in S4; crafted inputs in ordinary tests; the F4 author's inputs; ranges recomputed after
F4; Python 3.13.16.

## Questions for the orchestrator, each with a proposed answer

1. **Who refreshes the foundation ranges and reruns the size script after F4?** The ranges at and
   after `foundations/decisions.md:5439` and `foundations/invariants.md:2163` move with F1a–F3, and
   the new entries' ranges do not exist yet (the script leaves a range beyond its file
   `unchecked`). Proposed: resume this planner for one short turn on the F4 commit — it recomputes
   from headings, adds the tabled reads, reruns the script and updates `plan-size.md`; the
   orchestrator may instead do it mechanically. Evidence: plan, "Ranges" and the table of moving
   reads; `task-cycle/slice_size.py` docstring.
2. **`installation/test_install.py` in F4.** The spec changes `NAMES` "by hand" in the installer
   work; the file holds tests citing `installation-claude-guidance/1` (`:97`, `:382`, `:417`,
   `:429`, `:440`, `:451`), so WAY-03 and WAY-65 make it an invariant-test change. Proposed: F4's
   check author makes it, assessed under WAY-10 with the rest; `installation` tests stay RED from F4
   to S11, recorded. Alternative: leave `NAMES` unchanged as the styleguide cycle did (departs from
   the settled spec).
3. **The F4 check author's inputs.** WAY-69 gives the check's author "the sentence and its method,
   never the code's reasoning". The fixtures need the template's headings, columns and *Status*
   list. Proposed: give it spec §4.1, §4.2 and §5.1 (template forms) besides the sentences and
   methods, never §5.2. Evidence: `task-cycle/skill/SKILL.md:279-283`; spec §9.
4. **Execution ruling** on the plan's *Independence and execution*: proposed sequential order
   S1 → S11 as recommended.

## Concerns for the next dispatches

- **S2 margin.** About 39 000 estimated tokens of room after the foundation stages; the plan
  names how to narrow it, then how to split it, if the re-measure fails.
- **RED windows, all to be recorded, never suppressed:** F4's new tests until S2–S4 (by item) and
  `NAMES` until S11; the gate's and `agent-instructions`' entry-point tests from S6 to S10.
- **Between F1 and F3** the decisions guard is expected to report the level 1 identifiers WAY-167,
  WAY-168, WAY-196, WAY-198, WAY-199, WAY-202 and WAY-212 name as missing invariants — an
  expectation, not observed; rerun after F3.
- **WAY-195's paper:** the ACM pages answer 403 here; a public copy is reachable at the address
  above. The F1a author cites the copy it actually read (spec §8.3 "as read from a public copy").
- **`check_instructions.py` and info strings** were left unverified by the design (`reports/design.md`
  concerns); S1's and S4's checks are the first to observe it.
- **For the request:** `guidelines-check-carrier/1` is edited at its version, so the request shows
  its old and new sentence (WAY-57); WAY-167 and WAY-168 edits are shown for renewed acceptance
  (WAY-07); the C10 weak point and C16 as the spec §9 says.
- Not checkable here, as the spec says: `gate-guidelines-example-evidence/1` (method `TODO`),
  product-side invariants of the template, Python 3.14 behaviour.

## Refresh after the foundation stages (ruling C23)

- Input: HEAD `64344a3` (F1a `a45956f`, F1b `b03c5da`, F2+F3 `05e44b1`, F4 `64344a3`); no tracked
  file changed, nothing committed (`git status --short` empty).
- Ranges recomputed from headings at `64344a3` (same scratch script as before). Lines before
  `foundations/decisions.md:5439` and `foundations/invariants.md:2213` did not move. Moved:
  WAY-167 `5439-5508`, WAY-168 `5510-5578`, WAY-167..171 `5439-5715`, ..172 `5439-5758`,
  ..175 `5439-5921`, WAY-188 `6286-6315`, WAY-188..190 `6286-6386`, WAY-190 `6352-6386`,
  WAY-167..192 now `5439-7262` in S6 (whole run including the new entries). New: WAY-193–212
  `6460-7262` (WAY-196–197 `6633-6713`, WAY-198–200 `6715-6815`, WAY-205 `6974-7015`, WAY-212
  `7223-7262`); invariants `guidelines-check-kind-index` `2213-2221`, `-exemplar` `2223-2231`,
  `-example-files` `2233-2241`, `gate-guidelines-example-evidence` `2243-2251`.
- Reads added: the new decisions to S1 (196, 197, 205), S2 (all), S3 (198–200, 212), S4 and S5
  (197, 205), S6 (all); invariants `2133-2251` to S1–S4, `2243-2251` to S5;
  `reports/f4-check.md` to S2–S4. F4's test files were already named and are now measured as
  F4 left them. The table of later reads keeps only S1's template, S2's coding template and S6's
  skill.
- S2–S4 *Checks* now name the RED list in `reports/f4-check.md` and C32 (*File* cells hold paths
  in backticks).
- Size: `python3 -B task-cycle/slice_size.py docs/task-cycles/coding-guidelines/plan.md`, exit
  code 0, all 11 fit: S1 100 788 · S2 216 324 · S3 164 479 · S4 185 423 · S5 84 860 · S6 176 144 ·
  S7 45 644 · S8 45 497 · S9 45 738 · S10 45 621 · S11 92 718 estimated tokens. Full output:
  `plan-size.md`. No split. S2 keeps the least room (about 32 000 tokens after S1's growth).
