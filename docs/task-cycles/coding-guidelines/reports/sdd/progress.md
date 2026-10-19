# SDD ledger — plan: docs/task-cycles/coding-guidelines/plan.md

Workspace: `reports/sdd/` (C27). Spec: `docs/task-cycles/coding-guidelines/spec.md` (reachable).
Foundation stages done before S1: F1a `a45956f`, F1b `b03c5da`, F2+F3 `05e44b1`, F4 `64344a3`.
Plan refreshed at `64344a3` (C23); `plan-size.md` exit 0, 11/11 fit.

## Pre-flight scan

| Tasks | Shared file or interface | Produces vs consumes | Found |
|---|---|---|---|
| S1 → S2, S3, S4, S5, S6 | `product-guidelines/template.md` (S1 writes; others read) | S1's test-case rule and "Where guidelines go" vs the form check's items (S2–S4), the cycle sentence (S5), the skill (S6) | consistent: all cite spec §5.1; S2–S4 must keep the required form parseable as S1 leaves it |
| S2 → S3 → S4 | `product-guidelines/form_check.py`, `product-guidelines/test_form_check.py` | each adds spec §5.2 items (1,2,6 / 3,4 / 5) on the previous | sequential; F4 tests are the contract; RED list per slice in `reports/f4-check.md` |
| S2 → S3, S4, S6 | `product-guidelines/coding/template.md` (S2 writes) | headings/columns/Status list verbatim as F4 fixtures and spec §4.1–4.2 | S2 must match F4 fixtures exactly (backticked *File*, C32) |
| F4 → S2, S3, S4, S11 | invariant tests (read-only for slices) | fixtures vs code | a slice needing a test change returns to the foundation step |
| S5 → S7 | `task-cycle/skill/SKILL.md` (S5) vs `implement-task` entry point (S7) | entry point holds the frontmatter description only; S5 keeps frontmatter | no conflict |
| S6 → S7–S10 | `product-guidelines/coding/SKILL.md` frontmatter vs 32 entry points' sibling lists | generator output | S10 `--write` touches only its eight paths if S7–S9 done |
| S6, S10 → S11 | skill committed, gate green | installer `SKILLS` entry and `NAMES` (F4) | S11 after S10 |
| S1 | self | template text only; its checks run existing tests and `check_instructions.py` on a temp repo | agrees |
| S2 | self | three files; template + code + moved fixtures | agrees (largest read, ~218k est.) |
| S3, S4 | self | code + ordinary tests | agree |
| S5 | self | one sentence in two steps; frontmatter unchanged | agrees |
| S6 | self | skill + 2 entry points + README; gate red S6→S10 by design | agrees |
| S7–S10 | self | 8 entry points each, generator output | agree |
| S11 | self | installer + README + new test; final full check set | agrees |

No conflict found; no ruling needed before S1.

## Progress
S1: dispatched implementer (opus), BASE 64344a3, brief reports/sdd/slice-1-brief.md, report reports/sdd/slice-1-report.md
S1: implementer DONE_WITH_CONCERNS, commit 7976b54 (template.md +63/-8); concern: spec §5.1 "fence-opening line after at most three spaces" vs check_instructions.py fence after any indentation.
Ruling: (C33) a test case's text holds no line that, after any leading whitespace, starts with three backticks or three tildes; the template states it so (S1, before review) and S4's form check reports such a line — why: C12's purpose is that check_instructions.py's fence toggling stays right, and it toggles after any indentation (shown in slice-1-weakest-indented-fence.txt); spec §5.1's "at most three spaces" is CommonMark's rule, narrower than the tool it protects — cost if wrong: a case cannot hold an indented line starting with ``` (rare in code files).
S1: fix for C33 commit 18317a8 (template.md; total since 64344a3 +61/-8); implementer used the Artifact publish tool to edit, which also published a private artifact — reported to the user; contract amended (no Artifact/publishing tools).
S1: task review (sonnet) — Spec ✅, quality Approved, 0 Critical, 0 Important, 4 Minor; report reports/sdd/slice-1-review.md
Task 1: minor (deferred): artifact published by the executor (out of scope; reported to Mariusz)
Task 1: minor (deferred): WAY-197 cited for the bad case's teaching purpose (spec Q7)
Task 1: minor (deferred): rule naming guidelines-form with another invariant — S4 tests to state the case
Task 1: minor (deferred): bare-fence sentence redundant after C33
S1: ⚠️ cannot verify from diff — template promises form-check reports (path limits, tilde/indented fence lines, bare-fence malformed case, >1 MiB unread) — carried to S4's dispatch and review.
Task 1: complete (commits 64344a3..18317a8, review clean)
S2: re-measured before dispatch at 18317a8: 218006 tokens, fits (size-before-S2.txt); dispatched implementer (opus), BASE 18317a8
S2: implementer DONE_WITH_CONCERNS, commit 334ef34 (coding/template.md +253, form_check.py +177/-58, test_form_check.py +327/-8); concerns are observations (stricter separator row incl. styleguides; template states end-state checks; one S4 control green; WAY-207/WAY-200 citations; check name check_tables) — to review.
S2: task review dispatched (opus), package slice-2-review-package.diff (18317a8..334ef34), deliberate breaks for guidelines-check-form and guidelines-check-carrier.
S2: task review (opus) — Spec ✅, Approved, 0/0/6 Minor; 4 deliberate breaks (check-form ×2, carrier ×2) all detected (slice-2-break-*.txt); report slice-2-review.md
Task 2: minor (deferred): two new check_tables error branches untested (form_check.py:876-878, :888-890)
Task 2: minor (deferred): docstring "as Markdown reads a row" overstates (escaped \| split)
Task 2: minor (deferred): coding/template.md:178-180 omits "the form check asks no completeness"
Task 2: minor (deferred): restructured read_roles and its TemplateError lack ordinary tests
Task 2: minor (deferred): ragged docstring line form_check.py:52
Task 2: minor (deferred): TemplateWords message checks for Kind/File always true
S2: ⚠️ template states the copy's end-state checks (coding/template.md:192-198) — carried to S3/S4 review.
Task 2: complete (commits 18317a8..334ef34, review clean)
S3: dispatched implementer (opus), BASE 334ef34
S3: implementer DONE_WITH_CONCERNS, commit 0607656 (form_check.py +216/-3, test_form_check.py +334/-0); KindIndex 5 and Exemplar 5 F4 tests green; 7 ExampleFiles red (S4). Concerns are observations ("git lists" read as tracked; stale fingerprint under guidelines-reference-current/1; 200 KiB File reported as untracked) — to review.
S3: task review dispatched (opus), package slice-3-review-package.diff (334ef34..0607656), breaks for kind-index and exemplar.
S3: task review (opus) — Spec ✅, Approved, 0/0/3 Minor; breaks of kind-index and exemplar detected (slice-3-break-*.txt); executor's concerns accepted on merits.
Task 3: minor (deferred, reviewer: outside the slice): sentence of guidelines-check-kind-index/1 (invariants.md:2215) says "git lists" where it means "git tracks" — for the return step (sentence author) and the request
Task 3: minor (deferred): names_in_backticks re-collapses whitespace per call (form_check.py:572)
Task 3: minor (deferred): no test for a tracked directory as a File of ## Files of this kind, nor a 1 MiB line in the kinds table
Task 3: complete (commits 334ef34..0607656, review clean)
S4: dispatched implementer (opus), BASE 0607656; carried: S1 ⚠️ template promises (path limits, tilde and indented fence lines in a case per C33, bare-fence malformed case, >1 MiB unread), S1 minor 3 (guidelines-form with another invariant), S2/S3 ⚠️ template promise of the copy's checks complete after S4.
S4: implementer DONE_WITH_CONCERNS, commit 1bff1ae (form_check.py +192/-18, test_form_check.py +390/-3); product-guidelines 136 tests exit 0 (all F4 green); e2e on a temp product exit 0; weakest point: line splitting at \r etc. fixed with fuzz evidence. Concerns: guidelines-form-only rule with fenced blocks unchecked (reading); four-backtick closing reported; open block to EOF only ordinary test; tab-indented bare fence closes case like check_instructions — to review.
S4: task review dispatched (opus), package slice-4-review-package.diff (0607656..1bff1ae), break for example-files.
S4: task review (opus) — Spec ✅, Approved by the reviewer for the slice's code; 0 Critical, 1 Important, 7 Minor. Breaks: indented inner fence detected; "guidelines-form beside another invariant exempted" NOT detected by invariant tests (only an ordinary test); open-to-end only ordinary (accepted C32).
Task 4: Important (I1): invariant tests lack the negative subtest — a rule naming guidelines-form beside another invariant with no cases for the other must be reported (test_form_check_invariants.py:1311, :1394); also ordinary test test_form_check.py:1271.
Ruling: (C34) I1 enters the fix loop; the invariant-test part returns to the foundation step and is written by the check author D (WAY-69, WAY-03), the ordinary-test part by the S4 executor; then a scoped re-review by the S4 reviewer, who repeats the undetected break — why: an undetected break is a finding to resolve and invariant tests are closed to executors — cost if wrong: one more round.
Task 4: minor (deferred): docstring wrap form_check.py:82-85
Task 4: minor (deferred): a `- **Name:**` line after the cases counts as a field (form_check.py:978) — fails safe
Task 4: minor (deferred): Fence.closing typed int but may be None; fields parsed twice
Task 4: minor (deferred): executor concerns 1–4 accepted by the reviewer (guidelines-form-only rule with blocks; four-backtick close place; open-to-end ordinary only; tab-indented bare fence, pre-existing)
Task 4: fix round 1/5 dispatched: check author D (invariant subtest), then S4 executor (ordinary test); FIX_BASE 1bff1ae
Task 4: fix round 1 part a — check author D commit dfa9e15 (test_form_check_invariants.py +34/-0), new ExampleFiles test with 5 subtests; product-guidelines 137 OK
Task 4: fix round 1 part b — S4 executor commit d743c2e (test_form_check.py +12/-1), no code change; product-guidelines 137 OK; scoped re-review dispatched (S4 reviewer), FIX_BASE 1bff1ae
Task 4: fix round 1/5 (1 addressed, 0 open; commits 1bff1ae..d743c2e) — re-review: I1 ADDRESSED; repeated break now fails 5 invariant subtests + 2 ordinary (slice-4-fix1-rebreak.txt); no new breakage
Task 4: complete (commits 0607656..d743c2e, review clean)
S5: dispatched implementer (opus), BASE d743c2e
S5: implementer DONE_WITH_CONCERNS, commit faf43c9 (task-cycle/skill/SKILL.md +12/-0); entry points current; task-cycle 41, gate 98 OK. Concerns: step 11 refers to step 10; 'not accepted otherwise' for a case-only change; line 63 'writes only in the task's worktree' vs scratch worktree — to review (sonnet).
S5: task review (sonnet) — Spec ✅, Approved, 0/0/2 Minor
Task 5: minor (deferred): step 11 sentence omits step 10's trigger, reached by "as step 10 gives" (SKILL.md:391-393)
Task 5: minor (deferred, outside the slice): SKILL.md line 63 "writes only in the task's worktree" vs the scratch worktree of step 10 — process remark for the request
Task 5: complete (commits d743c2e..faf43c9, review clean)
S6: dispatched implementer (opus), BASE faf43c9; reads added: product-guidelines/coding/template.md (S2)
S6: implementer DONE_WITH_CONCERNS, commits d5fd8ca (skill 258 lines, 2 entry points, README), aaaab9d (WAY-209 explicit); generator 32 would-change; agent-instructions and gate 1 test each red until S10 by name; part map exit 0. Six how-choices (human picks kinds to audit; no split without trial run or fresh judge) — to review (opus).
S6: task review (opus) — Spec ✅, Approved, 0/0/7 Minor; executor's six choices hold
Task 6: minor (deferred): SKILL.md:181 choice of kinds to audit has no recommendation (should recommend every kind; row 22, Q6) — executor's choice 1 recorded as ruling C35 for the request
Task 6: minor (deferred): SKILL.md:162 "Where the product has code:" vs new-kind mode in a product without code
Task 6: minor (deferred): SKILL.md:98 orchestrated mode writes trial-run output vs refine-task's orchestrated mode
Task 6: minor (deferred): SKILL.md:56 tool version "the task settles" — nothing settles a version (spec gap too)
Task 6: minor (deferred): SKILL.md:164-175 no rerun of the trial when the human picks another tool or set
Task 6: minor (deferred): SKILL.md:38 "any other file git tracks" vs a backlog kept in the repository
Task 6: minor (deferred): SKILL.md:167 "never into a file git tracks" ambiguous for the scratch worktree
Task 6: complete (commits faf43c9..aaaab9d, review clean)
S7: dispatched implementer (sonnet), BASE aaaab9d
S7: implementer DONE, commit d3f35b6 (8 entry points, +1/-1 each); generator 24 would-change; review dispatched (sonnet)
S7: task review (sonnet) — Spec ✅, Approved, 0/0/0
Task 7: complete (commits aaaab9d..d3f35b6, review clean)
S8: dispatched implementer (sonnet), BASE d3f35b6
S8: implementer DONE, commit 90580b4 (8 entry points); generator 16 would-change; review dispatched (sonnet)
S8: task review (sonnet) — Spec ✅, Approved, 0/0/0
Task 8: complete (commits d3f35b6..90580b4, review clean)
S9: dispatched implementer (sonnet), BASE 90580b4
S9: implementer DONE, commit 66424e1 (8 entry points); generator 8 would-change; review dispatched (sonnet)
S9: task review (sonnet) — Spec ✅, Approved, 0/0/0
Task 9: complete (commits 90580b4..66424e1, review clean)
S10: dispatched implementer (sonnet), BASE 66424e1
S10: implementer DONE, commit 8901da0 (8 entry points via --write); entry points current; agent-instructions 18 OK, gate 98 OK; review dispatched (sonnet)
S10: task review (sonnet) — Spec ✅, Approved, 0/0/0
Task 10: complete (commits 66424e1..8901da0, review clean)
S11: dispatched implementer (opus), BASE 8901da0
S11: implementer NEEDS_CONTEXT (no code): test_styleguide_installation.py:92 hard-codes 30 wrappers; the new SKILLS entry makes 32.
Ruling: (C36) change that one assertion to 32 and add installation/test_styleguide_installation.py to S11's change list (4 files) — why: an ordinary test (it cites no invariant), the count follows from the plan's SKILLS entry, the minimal change — cost if wrong: the next skill again touches the line (2*len(SKILLS) rejected as widening).
Ruling: (C37) the non-UTF-8 wrapper case asserts exit != 0 and nothing written; the existing UnicodeDecodeError traceback (all wrappers, pre-existing) is a concern for the request and a separate task — why: the brief changes no other installer text — cost if wrong: a traceback instead of an Error line remains.
S11: implementer resumed with C36, C37
S11: implementer DONE_WITH_CONCERNS, commit 2eabf42 (install.py +1, README +4/-2, new test +164, styleguide test 30->32); installation 35 OK; final set: all suites exit 0 except instruction-files 3 base platform failures; guards 0; form check 0; entry points current; review dispatched (opus) with break of installation-claude-guidance
S11: task review (opus) — Spec ✅, Approved, 0/0/5 Minor; break of installation-claude-guidance/1 (SKILLS entry removed) detected by test citing it (slice-11-break-installation.txt)
Task 11: minor (deferred, outside the task): the break that detected is caught by NAMES assertions inside a test citing installation-claude-guidance/1, whose sentence is about root CLAUDE.md — citation scope for a separate task
Task 11: minor (deferred): slice-11-weakest.txt gaps (empty section; mislabeled wrapper)
Task 11: minor (deferred): crafted test reassigns self.product per subtest (test_coding_guidelines_installation.py:136-140)
Task 11: minor (deferred): non-UTF-8 subtests could assert stderr names the error
Task 11: minor (deferred): carried C37 traceback and C32 NAMES gaps (pre-existing)
Task 11: complete (commits 8901da0..2eabf42, review clean)
Final review: dispatched (opus), package final-review-package.diff (235b0b4..2eabf42), handoff reports/final-review-handoff.md
Final review (opus): With fixes — 0 Critical, 1 Important (I1 = ledger T6-1 raised: skill SKILL.md:180-183 and WAY-201 binding sentence decisions.md:6819-6822 narrow rows 3 and 22 — "kinds the task audits" vs every kind; no recommendation, WAY-194), 29 Minor (M1–M4 new), 3 outside scope; T1-3 resolved by C34.
Ruling: (C38) I1 is blocking (Important, in scope): one fix — WAY-201 reworded to row 22's meaning (each kind the product holds files of) by its author (foundation author A, F1a), dependents renewed; the skill's step 3 recommends auditing every such kind, the human may defer a kind with the reason recorded (S6 executor); then one review of the fix by the final reviewer — why: the row's meaning is Mariusz's (WAY-134), restoring it is no new meaning — cost if wrong: one more foundation commit.
Final fix part a: foundation author A commit 5808fc7 (WAY-201 70344859->d98d2f0e, row 22's meaning); guards 0 errors; elements/decisions 169 OK
Final fix part b: S6 executor commit 5a00041 (SKILL.md +9/-7); entry points current; review of the fix dispatched to the final reviewer (2eabf42..5a00041)
Final review of the fix (opus): I1 ADDRESSED; new Minor N1: the skill lets the human defer a kind while WAY-201 asks a proposal for every kind — non-blocking, goes to the request's Minor list (no fix, "The end of a code review").
Whole-change review complete: no blocking finding survived. Range 235b0b4..5a00041.
Return step (opus): commit 355a240 — guidelines-check-kind-index/1 edited in place ("git lists" -> "git tracks", 2a02b7c1 -> e19f30f2); part map task-cycle Depends on + product-guidelines. Q1: skill's deferral of a kind contradicts WAY-201 (row 22).
Ruling: (C39) revise C38 — the skill drops the deferral of a kind; the audit covers every kind the product holds files of (row 22, WAY-201); S6 executor makes it, followed by one affected code review — why: the deferral was the orchestrator's own addition in C38, an exception row 22 does not give, and the return step found the skill contradicting a binding decision; restoring the row needs no human — cost if wrong: a human who wants to postpone a kind runs its audit anyway or opens another task.
C39: S6 executor commit f34e477 (SKILL.md +8/-10), deferral dropped; entry points current
Return step: check author D verdict — existing kind-index checks match "git tracks"; a control is missing (an untracked kind file is no error).
Ruling: (C40) add D's control test KindIndex.test_a_kind_file_git_does_not_track_is_no_error and rename test_a_row_naming_no_file_git_lists_is_reported to …git_tracks…, by the check author (WAY-69); part of the invariant tests assessed next — why: the edited sentence's "git tracks" is now stated both ways — cost if wrong: one more test.
Assessment I1: foundation author B commit a677bc4 (WAY-203 96f71a98->45e40683, WAY-204 renewed); guards 0 errors
Assessment I2: executor S1 commit 8242720 (styleguide template +10/-2, SKILL +5/-1); product-guidelines 138 OK; entry points current
Assessment I3: check author D commit a839ea7 (+43): open-to-end case test and non-kind File row test; product-guidelines 140 OK. Affected review dispatched (opus, fresh) on 5a00041..a839ea7 with breaks
