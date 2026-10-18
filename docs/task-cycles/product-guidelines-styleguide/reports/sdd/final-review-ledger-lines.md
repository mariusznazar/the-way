Ruling: none needed — the scan found no conflict — cost if wrong: a conflict surfaces in a task review.
Task 1: Ruling: I1 — reword the two items ("code in backticks or fenced code", emphasis) as a note outside the template's rules: how `instruction-files/check_instructions.py` and `instruction-files/principles.md` read a file of guidelines once a product's instruction file points to it (it is then a repository instruction file, glossary), citing those as their source and no decision as a setter — why: no decision of the-way sets them and the slice may not edit `foundations/`; a foundation change for advice the instruction-files principles already give is wider than the task — cost if wrong: products read the note as optional and trip `dead-path` warnings, visible in their check
Task 1: minor (deferred): M1 "nothing of this template is copied" vs invariant copies (template.md:13-14 vs :136-137)
Task 1: minor (deferred): M2 heading "No emphasis words" vs body allowing one rule (template.md:117-118)
Task 1: minor (deferred): M3 "part" used for styleguide divisions beside the map's part (styleguide/template.md:4,73,75)
Task 1: minor (deferred): M4 language rule does not name `## Roles` column headings (template.md:120-124)
Task 1: minor (deferred): M5 "Every background with its text" proposes guidelines-form, whose sentence does not speak of pairs (styleguide/template.md:98-102)
Task 1: minor (deferred): M6 citations: role-meaning invariant's Part lacks WAY-62; non-styleguide file name `<discipline>-<part>` accepted by check but not given by WAY-167
Task 1: ⚠️ resolved — (1) the form check reads the fenced block under `## Required form`, placeholders in `<…>`: interface carried into Task 2's dispatch; (2) `guidelines/<discipline>-<part>.md` accepted by spec §5.3 5a and F4 tests but not given by WAY-167: not a gap of Task 1 (template follows WAY-167); Ruling: Task 2 follows the F4 tests and the spec, and the mismatch goes to the whole-change review as M6 — why: the tests are read-only and the slice may not edit foundations — cost if wrong: a file name the foundation does not give is accepted until the review settles it
Task 2: Ruling: I2's invariant-check gap goes back to the F4 check author (foundation step; the file is read-only for the executor, WAY-03, WAY-69) before the fix round; the executor's fix adds an ordinary test as well — why: an undetected break is a finding of the check, not of the code — cost if wrong: one extra dispatch
Task 2: Ruling: trust-boundary departure accepted — no path from a product's file reaches git; one `git ls-files` call; matching in Python — why: reviewer found no escaping input and it bounds git calls on crafted files; spec §5.4's wording is narrower in effect — cost if wrong: a path form git would resolve differently; reviewer probed files, dirs, trailing `/`, `.` segments, untracked, submodules
Task 2: minor (deferred): M3 unreadable part-map template exits 1 with traceback, not 2 (form_check.py:801-805; two copies of guard_shared error type)
Task 2: minor (deferred): M4 any `:` or `\` in a path refused (form_check.py:599-602)
Task 2: minor (deferred): M5 quadratic de-duplication of guidelines files (form_check.py:701-711)
Task 2: minor (deferred): M6 test calls self.setUp() inside subtest loop (test_form_check.py:365)
Task 2: minor (deferred): M7 missing sections reported at line 0 (form_check.py:428-429)
Task 2: minor (deferred): M8 name test matches discipline prefix + `-`; latent clash if templates `a` and `a-b` both existed (form_check.py:583-589)
Task 2: minor (deferred): M9 setUp() inside loop repeated (test_form_check.py:396)
Task 3: Ruling: implementer concern 1 (1 MiB limit on decision log and invariants file) kept for now and listed as reviewer Minor 3 for the whole-change review and the request — why: loud failure, the-way's log at ~41%, foundation read only when guidelines exist — cost if wrong: a product with a log over 1 MiB gets no reference check until the limit is raised
Task 3: minor (deferred): M1 merge check records `pass` though it never ran when the log is unreadable (form_check.py:1140, 1203-1204)
Task 3: minor (deferred): M2 merge re-checks only references current on the branch; `x@v2` with x added on onto escapes (form_check.py:955-962)
Task 3: minor (deferred): M3 1 MiB limit binds decision log and invariants file; decisions guard reads unbounded; git copies unbounded (form_check.py:560-561, 109)
Task 3: minor (deferred): M4 decision numbers normalised (`ABC-5` = ABC-05; 10+ digits stop being a reference) (form_check.py:133, 445-451)
Task 3: minor (deferred): M5 untested branches at the trust boundary and in the narrowing
Task 3: minor (deferred): M6 PARSE_ERRORS includes AttributeError and TypeError (form_check.py:108)
Task 3: minor (deferred): M7 report's borrowed-function list omits versions_of
Task 3: minor (deferred): M8 file growth 1247 lines (in line with siblings)
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
Task 8: minor (deferred): M1 test_styleguide_installation.py:90 hard-codes 30 wrappers
Task 8: minor (deferred): M2 install.py:158 "always name this repository's file or directory" vs form-check commands naming no folder (:176-178)
Task 8: note for the whole-change review — with --merge-onto the form check prints a "0 error(s)" summary before a file's errors
