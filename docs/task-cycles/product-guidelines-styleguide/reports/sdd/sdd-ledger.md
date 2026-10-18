# SDD ledger — plan: .runs/task-cycles/product-guidelines-styleguide/plan-tasks.md

Plan view: `plan-tasks.md` is `plan.md` with `### Slice N —` headings renamed `### Task N —` for this skill's scripts; equality of the reverse rename with `plan.md` verified (diff empty). Briefs trimmed at the first `## ` heading after the task (task 8 otherwise carried the plan's trailing sections).
Spec: `.runs/task-cycles/product-guidelines-styleguide/spec.md` (reviewed); frozen task binds over it. Foundation stage done before Task 1: `96623ed..8ea4679`.
Execution: sequential (Superpowers 6.4.1 forbids parallel implementers; cycle ruling C26). Whole-change review ends as task-cycle "The end of a code review" gives (WAY-161/162), replacing this skill's final adjudication and fix wave.

## Pre-flight scan

| Pair or task | Produces → consumes | Found |
|---|---|---|
| T1 → T2, T3 | templates' fenced skeleton and required-rule headings → form check reads them from its own checkout (C28.1) | consistent; headings verbatim per §4.1 and F4 fixtures |
| T2 ↔ T3 | both change `form_check.py`, `test_form_check.py`; T2 accepts `--merge-onto`, T3 adds the reference checks | consistent; F4 reference tests red between T2 and T3 by plan |
| F4 → T2, T3 | `test_form_check_invariants.py` read-only (WAY-03) | consistent; a needed change returns to the foundation step |
| T1 → T4 | templates → skill names and points to them, restates none | consistent |
| T4 → T5, T6, T7 | skill frontmatter → generator's sibling list | consistent; T4 writes its own 2 entry points via `produce`, 30 stale until T7 by plan |
| T5, T6 → T7 | disjoint files; T7 `--write` must change only its ten | consistent |
| T3, T4, T7 → T8 | form-check commands, skill, green gate → installer `SKILLS` and guidance | consistent |
| T1 | changes 2 templates; checks via `check_instructions.py` on a temp repo | self-consistent |
| T2 | changes script + ordinary tests; F4 tests partly green | self-consistent |
| T3 | changes script + ordinary tests; all `product-guidelines` tests green | self-consistent |
| T4 | changes skill, 2 entry points, README | self-consistent |
| T5–T7 | ten generated files each | self-consistent |
| T8 | changes `install.py`, `installation/README.md`, new test file; `test_install.py` unchanged (WAY-03) | self-consistent |

Ruling: none needed — the scan found no conflict — cost if wrong: a conflict surfaces in a task review.
Task 1: dispatched (BASE 8ea4679, implementer opus, agent af2adeb)
Task 1: implementer DONE_WITH_CONCERNS ddef02a (+364); review dispatched
Task 1: review ddef02a — spec ❌, 1 Important (I1 plan-mandated: two writing rules cite WAY-129/WAY-192, which do not set them), 6 Minor; report task-1-review.md
Task 1: Ruling: I1 — reword the two items ("code in backticks or fenced code", emphasis) as a note outside the template's rules: how `instruction-files/check_instructions.py` and `instruction-files/principles.md` read a file of guidelines once a product's instruction file points to it (it is then a repository instruction file, glossary), citing those as their source and no decision as a setter — why: no decision of the-way sets them and the slice may not edit `foundations/`; a foundation change for advice the instruction-files principles already give is wider than the task — cost if wrong: products read the note as optional and trip `dead-path` warnings, visible in their check
Task 1: minor (deferred): M1 "nothing of this template is copied" vs invariant copies (template.md:13-14 vs :136-137)
Task 1: minor (deferred): M2 heading "No emphasis words" vs body allowing one rule (template.md:117-118)
Task 1: minor (deferred): M3 "part" used for styleguide divisions beside the map's part (styleguide/template.md:4,73,75)
Task 1: minor (deferred): M4 language rule does not name `## Roles` column headings (template.md:120-124)
Task 1: minor (deferred): M5 "Every background with its text" proposes guidelines-form, whose sentence does not speak of pairs (styleguide/template.md:98-102)
Task 1: minor (deferred): M6 citations: role-meaning invariant's Part lacks WAY-62; non-styleguide file name `<discipline>-<part>` accepted by check but not given by WAY-167
Task 1: fix round 1/5 (1 addressed, 0 open — I1 note; commits ddef02a..e62ca49); re-review task-1-rereview-1.md (sonnet)
Task 1: ⚠️ resolved — (1) the form check reads the fenced block under `## Required form`, placeholders in `<…>`: interface carried into Task 2's dispatch; (2) `guidelines/<discipline>-<part>.md` accepted by spec §5.3 5a and F4 tests but not given by WAY-167: not a gap of Task 1 (template follows WAY-167); Ruling: Task 2 follows the F4 tests and the spec, and the mismatch goes to the whole-change review as M6 — why: the tests are read-only and the slice may not edit foundations — cost if wrong: a file name the foundation does not give is accepted until the review settles it
Task 1: complete (commits 8ea4679..e62ca49, review clean after 1 round)
Task 2: dispatched (BASE e62ca49, implementer opus)
Task 2: implementer DONE_WITH_CONCERNS 6496a2f, 2e5d038; review dispatched
Task 2: review 2e5d038 — spec ❌, 2 Important (I1 5a bypass: styleguide-web.md with Discipline `styleguide-web` checked against the common form, form_check.py:579-592,652; I2 absolute-path guard form_check.py:603-604 untested — deliberate break of guidelines-check-code-path undetected), 5 Minor; breaks: 4 of 5 detected; report task-2-review.md
Task 2: Ruling: I2's invariant-check gap goes back to the F4 check author (foundation step; the file is read-only for the executor, WAY-03, WAY-69) before the fix round; the executor's fix adds an ordinary test as well — why: an undetected break is a finding of the check, not of the code — cost if wrong: one extra dispatch
Task 2: Ruling: trust-boundary departure accepted — no path from a product's file reaches git; one `git ls-files` call; matching in Python — why: reviewer found no escaping input and it bounds git calls on crafted files; spec §5.4's wording is narrower in effect — cost if wrong: a path form git would resolve differently; reviewer probed files, dirs, trailing `/`, `.` segments, untracked, submodules
Task 2: minor (deferred): M3 unreadable part-map template exits 1 with traceback, not 2 (form_check.py:801-805; two copies of guard_shared error type)
Task 2: minor (deferred): M4 any `:` or `\` in a path refused (form_check.py:599-602)
Task 2: minor (deferred): M5 quadratic de-duplication of guidelines files (form_check.py:701-711)
Task 2: minor (deferred): M6 test calls self.setUp() inside subtest loop (test_form_check.py:365)
Task 2: minor (deferred): M7 missing sections reported at line 0 (form_check.py:428-429)
Task 2: F4 check correction 8d97ab9 (+33/-1, code-path cases over tracked remainders; break now detected per check author's throwaway run); fix round 1 dispatched to implementer (I1, I2)
Task 2: fix round 1/5 (2 addressed, 0 open — I1 5a, I2 path tests; commits 2e5d038..d79f692 incl. F4 8d97ab9); re-review task-2-rereview-1.md; code-path break repeated and detected (slice-2-break-guidelines-check-code-path-2.txt)
Task 2: minor (deferred): M8 name test matches discipline prefix + `-`; latent clash if templates `a` and `a-b` both existed (form_check.py:583-589)
Task 2: minor (deferred): M9 setUp() inside loop repeated (test_form_check.py:396)
Task 2: complete (commits e62ca49..d79f692, review clean after 1 round)
Task 3: dispatched (BASE d79f692, implementer opus)
Task 3: implementer DONE 10b5f4a (form_check.py +437/-57, test_form_check.py +272/-4; 60 tests green); review dispatched (opus)
Task 3: review 10b5f4a — spec ✅ (2 ⚠️), quality Approved, 0 Critical, 0 Important, 8 Minor; breaks: reference-current, check-reference-target, check-stale-reference all detected (plus two merge-side breaks detected); report task-3-review.md
Task 3: ⚠️ resolved — (1) `guidelines-reference-current` *Part* lacks elements-common and relation-model though its check runs through them: a foundation question, carried to the return step (WAY-62); (2) tightened form checks (log prefix, invariants file) match the sentences: accepted
Task 3: Ruling: implementer concern 1 (1 MiB limit on decision log and invariants file) kept for now and listed as reviewer Minor 3 for the whole-change review and the request — why: loud failure, the-way's log at ~41%, foundation read only when guidelines exist — cost if wrong: a product with a log over 1 MiB gets no reference check until the limit is raised
Task 3: minor (deferred): M1 merge check records `pass` though it never ran when the log is unreadable (form_check.py:1140, 1203-1204)
Task 3: minor (deferred): M2 merge re-checks only references current on the branch; `x@v2` with x added on onto escapes (form_check.py:955-962)
Task 3: minor (deferred): M3 1 MiB limit binds decision log and invariants file; decisions guard reads unbounded; git copies unbounded (form_check.py:560-561, 109)
Task 3: minor (deferred): M4 decision numbers normalised (`ABC-5` = ABC-05; 10+ digits stop being a reference) (form_check.py:133, 445-451)
Task 3: minor (deferred): M5 untested branches at the trust boundary and in the narrowing
Task 3: minor (deferred): M6 PARSE_ERRORS includes AttributeError and TypeError (form_check.py:108)
Task 3: minor (deferred): M7 report's borrowed-function list omits versions_of
Task 3: minor (deferred): M8 file growth 1247 lines (in line with siblings)
Task 3: complete (commits d79f692..10b5f4a, review clean)
Task 4: dispatched (BASE 10b5f4a, implementer opus)
Task 4: implementer DONE_WITH_CONCERNS f248e42 (skill +207, 2 entry points, README +5/-2); review dispatched
Task 4: review f248e42 — spec ❌, 2 Important (I1 missing failure mode at the UI's part when a law or contract binds accessibility, SKILL.md:173-174, spec §6.3, WAY-46; I2 plan-mandated: nothing leads refine-task or lead-project to the skill, reached by description only), 10 Minor; report task-4-review.md
Task 4: Ruling: I2 — keep reach by the skill's description in this task; routing a styleguide task from refine-task (and lead-project) belongs to the separate backlog task "cycle zadania przy zmianie widoku", which owns refine-task's detection and the blocking rule (frozen task *Out of scope*, answer 1); named as a limitation in the request — why: the task forbids changing refine-task's cycle behaviour here and lists that routing out of scope — cost if wrong: until that task lands, an agent may refine a styleguide task without the skill when the description does not match
Task 4: minor (deferred): M1 row 20 — companion never said to be withdrawn once the full invariant holds
Task 4: minor (deferred): M2 row 26 — adopting decision covers the template, not what the skill proposes
Task 4: minor (deferred): M3 SKILL.md:38 "only through the task document" overstates WAY-172 (blocked draft request route missing)
Task 4: minor (deferred): M4 WCAG edition's address and passages not among what reaches the task document
Task 4: minor (deferred): M5 no numbered step to run refine-task steps 1–2 first
Task 4: minor (deferred): M6 no stop when the foundation settles no technology for the UI
Task 4: minor (deferred): M7 part identifier used in report paths while it may be an open question
Task 4: minor (deferred): M8 audit's "ask every time" reads as a question to the human
Task 4: minor (deferred): M9 README.md:71-73 suggests every discipline has a template and a skill
Task 4: minor (deferred): M10 unclear one critic for all research reports or one per report
Task 4: note for the whole-change review — spec §6.2 lists the part-map change under Settlements to record, wrongly (task template :132, find-foundation-entries); research when screens exist but no styleguide does follows spec and To do 8, WAY-186 has no such limit
Task 4: fix round 1/5 (1 addressed, 0 open — I1 failure mode via To do/update-part-map; commits f248e42..784284c); re-review task-4-rereview-1.md (sonnet)
Task 4: complete (commits 10b5f4a..784284c, review clean after 1 round; I2 ruled)
Task 5: dispatched (BASE 784284c, implementer sonnet — generated files)
Task 5: implementer DONE fbf008b (10 files, +1/-1 each); review dispatched (sonnet)
Task 5: review fbf008b — spec ✅, Approved, 0/0/2 Minor (no change required); reviewer briefly detached HEAD and returned it (branch and tree verified by controller)
Task 5: complete (commits 784284c..fbf008b, review clean)
Task 6: dispatched (BASE fbf008b, implementer sonnet)
Task 6: implementer DONE 75636d8 (10 files +1/-1); review dispatched (sonnet)
Task 6: review 75636d8 — spec ✅, Approved, 0/0/2 Minor (report lacks commit hash; loose inference in weakest-point text) — deferred
Task 6: complete (commits fbf008b..75636d8, review clean)
Task 7: dispatched (BASE 75636d8, implementer sonnet)
Task 7: implementer DONE 04920a1 (10 files +1/-1; generator current; agent-instructions 18, gate 98 pass); review dispatched (sonnet)
Task 7: review 04920a1 — spec ✅, Approved, 0/0/1 Minor (output files unverified by reviewer; controller verified they exist); all 32 entry points byte-equal to produce and current
Task 7: complete (commits 75636d8..04920a1, review clean)
Task 8: dispatched (BASE 04920a1, implementer opus — installer is a trust boundary)
Task 8: implementer DONE 2b5bf31, 9dd9880; review dispatched (opus)
Task 8: review 9dd9880 — spec ✅, Approved, 0/0/2 Minor; installer promises held under 5 crafted product files; invariant tests unchanged
Task 8: minor (deferred): M1 test_styleguide_installation.py:90 hard-codes 30 wrappers
Task 8: minor (deferred): M2 install.py:158 "always name this repository's file or directory" vs form-check commands naming no folder (:176-178)
Task 8: note for the whole-change review — with --merge-onto the form check prints a "0 error(s)" summary before a file's errors
Task 8: complete (commits 04920a1..9dd9880, review clean)
Final review 96623ed..9dd9880: Ready with one fix; 0 Critical, 1 Important (guidance names only guidelines/ or foundations/ changes — pin moves and renamed pointed-to files escape; install.py:176-179), 34 Minor, 3 outside scope; report final-review.md. One fix dispatched to the Task 8 executor (task-cycle 'The end of a code review', WAY-162)
Final review fix 896071a: Important 1 ADDRESSED, no new findings (review appended to final-review.md); whole-change review ends with no remaining blocking finding
