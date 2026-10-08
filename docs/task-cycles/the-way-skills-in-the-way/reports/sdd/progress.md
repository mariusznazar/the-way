# SDD ledger — plan: .runs/task-cycles/the-way-skills-in-the-way/plan.md

Spec: `.runs/task-cycles/the-way-skills-in-the-way/spec.md` (binding), amendments N1–N5 in `reports/report_04_spec_recheck.md`.
Harness note: subagents cannot write report files ("Subagents should return findings as text"); each agent returns its
report as text and the controller saves it to the report path named in its dispatch.

## Pre-flight scan

| Tasks | Shared file or interface | Produces vs consumes | Finding |
|---|---|---|---|
| 1.5 ↔ 1.7 | `skill-entry-points/1` sentence | 1.5 writes the sentence with literal strings; 1.7 derives every expected value from it | consistent by construction; 1.7 questions go back to 1.5 |
| 1.5 ↔ 2/3 | literal strings in the entry point text | spec §4.2 text (generator, Task 2 code) vs strings 1.5 must name: `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'`, `git rev-parse --show-toplevel`, "If the skill tells you to resolve a link to find the-way, skip that", "with the `the-way-` prefix, never an unprefixed one" | each string occurs verbatim in spec §4.2's text; Ruling P1 below |
| 1.6 ↔ 3 | part-map patterns `.claude/skills/**`, `.agents/skills/**` | 1.6 adds patterns, 3 creates the files | part-map guard red (two "matches no file" errors) from 1.8 to 3, recorded |
| 1.7 ↔ 3 | gate flow test | red from 1.7 until 3 creates entry points | recorded; the test is read-only after 1.8 |
| 2 ↔ 3 | `agent-instructions/test_skill_entry_points.py` | 2 creates, 3 adds `TrackedEntryPoints` | sequential, no conflict |
| 3 ↔ 4 | skill descriptions | 4 changes paragraphs, not frontmatter | entry points stay current; Task 4 step 6 checks `entry points are current` |
| 4 ↔ 6 | "where the-way lies" paragraphs | 6's wrapper sentence points to 4's paragraphs | order 4 → 6 kept |
| 1.5 ↔ 5 | `outbound-link-reach/1` exception vs `## Backlog` text | 5's section names the place of tasks; 1.5's sentence admits only that place | consistent if 1.5 keeps "place of tasks"; checked at 5 |
| 1.3 ↔ 2 | WAY-09 on what `agent-instructions/` holds vs the generator script there | 1.3 search returns a finding | open until 1.3; Ruling deferred to 1.4 |
| Task 0 | — | — | ran: 372 references, 0 stale; fingerprints WAY-09 b829b86a, WAY-27 770078ba, WAY-44 2f2b6227 |
| Task 1 | own text | eight sub-steps, sequential agents, three commits in 1.8 | agrees with itself; 1.8 stages before guards (the part-map guard reads the index) |
| Task 2 | own text | tests written out vs generator code in the plan | the planner ran 11 tests green in a scratch clone |
| Task 3 | own text | generate 22 files, equality test, deliberate break by the reviewer | agrees |
| Task 4 | own text | ten paragraph edits; check greps | agrees |
| Task 5 | own text | `AGENTS.md`, `README.md` | agrees |
| Task 6 | own text | one literal, one test using `NAMES` (exists, `installation/test_install.py:19`) | agrees |

- Ruling P1: the entry point text of spec §4.2 is the source of the literal strings for both the sentence (1.5) and
  the generator (2) — the spec is the binding authority — cost if wrong: a mismatch shows as a red gate test at Task 3
  and returns to the foundation step.

## Progress

Task 0: complete (no commits; `.runs/stale_refs.py` written, 372 references, 0 stale)
Task 1: 1.1 facts (report_06), 1.2 watches (report_07), 1.3 decisions (report_08), 1.4 answers (cycle Q7), 1.5 invariants (report_09), 1.6 part map (report_10, sentence reworded), 1.7 check (report_11; question answered: unprefixed names, from the sentence)
Task 1: Ruling: `elements/part-map` OwnMap.test_the_way_map_holds_no_error is red from 1.8 to Task 3 for the same two pattern errors as the part-map guard — the plan listed only the guard; same accepted red state — cost if wrong: none beyond a red element test in two commits, recorded in the request
Task 1: complete (commits c64a607..47dcbe3: 8be6a53 foundations, a1e80e8 watches, 47dcbe3 gate check); checks: guards decisions 0/8w, invariants 0/0, part-map 2 errors (accepted), facts 0/0, glossary 0/0; stale 0 of 378; element tests decisions/invariants/environment-facts/glossary OK, part-map 1 failure (accepted), gate 1 failure (flow test, expected)
Task 2: dispatched implementer (sonnet), BASE 47dcbe3, brief task-2-brief.md, report task-2-report.md
Task 2: implementer DONE, commit a7f42aa; 11/11 agent-instructions, 16/16 installation; review dispatched (opus) on review-47dcbe3..a7f42aa.diff
Task 2: review ✅ spec compliant, quality Approved (§4.2 text compared mechanically: EQUAL)
Task 2: minor (deferred): literal U+FEFF in test_skill_entry_points.py:144 instead of the brief's "﻿" escape
Task 2: minor (deferred): a plain description continuing on the next line is cut to its first line silently; a quoted description gets the suffix after the closing quote (invalid YAML) — skill_entry_points.py:98,114,152; plan-mandated; no current skill triggers it
Task 2: minor (deferred): argparse errors exit 2, outside the documented "0, or 1 with Error:" (skill_entry_points.py:208); plan-mandated
Task 2: minor (deferred): sibling_names([]) raises IndexError (skill_entry_points.py:143)
Task 2: minor (deferred): no test of orphan listing in dry-run mode; no test of the git-failure path
Task 2: minor (deferred): an OSError mid-write leaves earlier files written (docstring promise still accurate)
Task 2: complete (commits 47dcbe3..a7f42aa, review clean)
Task 3: dispatched implementer (sonnet), BASE a7f42aa, brief task-3-brief.md (steps 1–5), report task-3-report.md
Task 3: implementer DONE, commit c12d4dd; agent-instructions 12, gate 98 (skill-entry-points/1 pass), part-map guard 0 errors, installation 16; review + deliberate break dispatched (opus) on review-a7f42aa..c12d4dd.diff
Task 3: review ✅ spec compliant, quality Approved; deliberate break: 13 breaks, all caught (test failed, skill-entry-points/1 fail); restored, final gate 98 OK
Task 3: Ruling: Important 1 (root after Claude Code /cd is the start directory, wrong) is load-bearing and in the spec — amendment R12 appended to spec.md §10; foundation step reopened for WAY-127's sentence, the claude-code-project-skills fact, the skill-entry-points fingerprint and the agent-instructions failure-mode wording; the generator text and its test change in a fix round of Task 2's implementer; entry points regenerated — cost if wrong: one more wording cycle; leaving it: a session moved with /cd into a worktree reads the main checkout's skills, the defect of task point 2
Task 3: minor (deferred): generated paragraphs are one line each while the §4.2 block is soft-wrapped (renders the same; plan-mandated)
Task 3: minor (deferred): TrackedEntryPoints lists every tracked file under the skills directories, wider than the generator, which ignores non-the-way directories (test_skill_entry_points.py:514-519)
Task 3: minor (deferred): the new flow's parts are unchecked (no coverage file), same as wording-reaches-dependants
Task 3: R12 foundation correction committed 972e9ad (fact claude-code-project-skills d58fb91f with the /cd passage, WAY-127 4439a64a, skill-entry-points Derives from renewed, part-map failure mode "working directory" with a bracket that claims only what was checked, watch docstring); guards 0 errors; watch pass; 378 refs 0 stale
Task 3: Ruling: no ${CLAUDE_SKILL_DIR} third product check — the second check (the session's repository pins .the-way) catches the usual product session, and the placeholder would reach Codex as literal text or break the byte-identical copies — cost if wrong: the not-detected failure mode stays as recorded
Task 3: fix round 1/5 dispatched (R12): resume Task 2 implementer with fix-r12-findings.md; FIX_BASE c12d4dd
Task 3: fix round 1 implementer DONE, commit c61cebc (generator text, test text, 22 entry points regenerated); agent-instructions 12, gate 98 with skill-entry-points/1 pass, part-map guard 0/0, installation 16; scoped re-review dispatched (sonnet) on review-c12d4dd..c61cebc.diff
Task 4/5: Ruling: R12 wording applied to the extracted briefs (task-4-brief.md, task-5-brief.md) before dispatch — the spec is the binding authority and the plan's text predates R12 — cost if wrong: one wording correction in Task 4/5
Task 3: fix round 1/5 (1 addressed, 0 open; commits c12d4dd..c61cebc, incl. foundation 972e9ad)
Task 3: complete (commits a7f42aa..c61cebc, review clean after fix round 1)
Task 4: dispatched implementer (sonnet), BASE c61cebc, brief task-4-brief.md (R12 applied), report task-4-report.md
Task 4: implementer DONE, commits 4816161 (elements), dd25a36 (project-level); grep clean, 10 files, entry points current, nine test dirs 0, glossary guard 0/0; review dispatched (sonnet) on review-c61cebc..dd25a36.diff
Task 4: review ✅ spec compliant (ten files, word for word, R12 applied, skill-rule-source intact), quality Approved
Task 4: minor (deferred): "`elements/common/` is there" terse (elements/common/skill/SKILL.md:19-21); ragged wrapping of the briefed paragraphs
Task 4: complete (commits c61cebc..dd25a36, review clean)
Task 5: dispatched implementer (sonnet), BASE dd25a36, brief task-5-brief.md (R12 applied), report task-5-report.md
Task 5: implementer DONE, commit 863d458; AGENTS.md headings ok, 0 junction lines, gate 0, part-map 0/0; concern: Backlog path line over 100 columns (brief verbatim); review dispatched (sonnet) on review-dd25a36..863d458.diff
Task 5: review ✅, Approved; ⚠️ resolved by the controller: "the gate's tests report a skill a session would not see" is true — gate/test_skills_reach_the_way_sessions.py runs under `run_tests.py gate`
Task 5: minor (deferred): AGENTS.md:19 is 105 columns (an unbreakable code-span path, verbatim from the brief)
Task 5: minor (deferred): `## Backlog` names no projects place; WAY-107 lets it stay unnamed (the agent asks)
Task 5: complete (commits dd25a36..863d458, review clean)
Task 6: dispatched implementer (sonnet), BASE 863d458, brief task-6-brief.md, report task-6-report.md
Task 6: implementer DONE, commit bb9f8ad; RED 11 subtests, GREEN installation 17, gate 98
Task 6: review ✅, Approved (WAY-48 position judged correct: literal-only change, no new input)
Task 6: minor (deferred): assertNotIn("global install") guards only the exact old phrase (installation/test_install.py:60); "where it says where the-way lies" is not literal in Task 4's paragraphs
Task 6: complete (commits 863d458..bb9f8ad, review clean)
Final review: With fixes — Important 1 (unparseable YAML frontmatter passes the gate; no failure mode), Important 2 (WAY-27/outbound-link-reach exception keyed on the target, not the place); minors 3–6; ledger triage: none must be fixed except the quoted-description minor (raised to Important 1)
Final review: Ruling: Important 1 fixed on the generator side (refuse a description that is not a safe plain YAML scalar) plus an honest not-detected failure mode in the part map; the invariant and its gate check stay unchanged — changing them would need three new authors (WAY-69) for a gap no current skill triggers, while the generator's refusal and the equality test already stop generated and hand-edited entry points — cost if wrong: a hand-made unparseable entry point passes the gate until agent-instructions' tests run
Final review: Ruling: Important 2 fixed — WAY-27 rule sentence restored, exception as a second sentence keyed on the `## Backlog` section; outbound-link-reach likewise — cost if wrong: one more wording question for Mariusz, which he holds anyway
Final review: Ruling: Minor 3 (stop when the skill file is absent) taken into the code fix; Minor 5 (WAY-127 rejected reason) taken into the foundation fix; Minor 4 accepted (invariant says "that git tracks"); Minor 6 parked — the request carries the pin-move line the `pinned` change path owes; a README sentence would be an installer change the spec excluded — cost if wrong: products read the reason only in the request
Final review: fix wave — foundation dispatch (opus) first, then one code fix dispatch, then one scoped re-review
Final fix wave: foundation committed e374663 (WAY-27 fb27e458, outbound-link-reach 6d9df030, part-map failure mode, WAY-127 rejected reason; 378 refs 0 stale); code fix dispatched to the Task 2 implementer (fix-final-findings.md)
Final fix wave: code commit 76c3f3c (refuse unsafe descriptions, absent-skill stop, \ufeff escape); agent-instructions 13, gate 98 pass, part-map 0/0, installation 17; scoped re-review dispatched
Final fix wave: scoped re-review — Important 1, Important 2, Minor 3, Minor 5 ADDRESSED; no new Critical/Important breakage
Final fix wave: parked — the U+FEFF escape (ledger minor): the fix report says it was done, but the literal BOM is still in agent-instructions/test_skill_entry_points.py (byte search 1 hit, no "﻿") — Ruling: cosmetic (final review triage: not required before merge), no second fix wave in the skill; named in the request — cost if wrong: an editor may drop the invisible character and the case fails loudly
Final fix wave: complete (commits bb9f8ad..76c3f3c)
