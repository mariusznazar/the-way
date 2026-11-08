# Handoff — the one author of the change (task cycle `test-artifacts`)

## Delegation and place

The person who requested this cycle (the maintainer of the-way) has delegated intermediate choices to the cycle's orchestrator; the orchestrator's answers to you are not that person's approval. The human reviews only the request that will open at the end. Do not ask the human anything; send questions to the orchestrator by returning status `questions`.

- Worktree (work only here, on branch `task/test-artifacts`, base `f218b5542ae55b72a95832adde67591365abb72a`): `the worktree's root`
- Do not touch the main checkout `the main checkout of the repository` or any other worktree. Do not read or write `docs/task-cycles/test-artifacts/cycle.md` (the orchestrator's record).
- Do not run the product's gate (`python -B gate/run_tests.py` over everything); the orchestrator runs it. Run focused tests of the directories you change with `python -B gate/run_tests.py <directory>`.
- Report path (write the full report here): `docs/task-cycles/test-artifacts/reports/author_report.md`

## Your stage and method

You are the one author, without a plan, of the whole change. Method: read `task-cycle/change/SKILL.md` whole (in the worktree); your variant is "the whole change as the one author". Read the other files beside it (`ui_check.md`, `fix.md`, `slice.md`) only when its step names them — `ui_check.md` is a file you change, so you read it as a file you change; the change touches a user-interface check rule.

You also do the foundation step: read `task-cycle/skill/foundation_step.md` whole, and write the entries the task carries through the element skills — decisions through `elements/decisions/skill/SKILL.md`, invariants through `elements/invariants/skill/SKILL.md` (each skill selects its own foundation reading as its step 1 gives; the glossary skill `elements/glossary/skill/SKILL.md` only if a word needs an entry). The writing of each entry is on the task branch. Do not take the return step: the orchestrator resumes you for it later.

## The task

Frozen task document (read it whole): `docs/task-cycles/test-artifacts/task.md` (original: the author's private backlog note; approval date of the settlements 2026-11-08). It is in Polish. Its `Project relation:` is `independent`; *Questions carried to cycle*: none; *Human actions*: none.

Task items 1–8 under *To do* and rows 1–7 of *Settlements to record* are your whole scope. Row 7 is an invariant and item 8 its check by script and test: "Przed każdym commitem, który dodaje kopię zapisu cyklu, skrypt the-way sprawdza, że kopia nie zawiera żadnego pliku obrazu, tak jak dziś sprawdza ją pod kątem ścieżek prywatnych". You choose how to make the check — an extension of `task-cycle/private_paths_check.py` or a script of its own — and name that choice in your report; either way `task-cycle/skill/SKILL.md` ("The record before it is committed") must call it before every commit that adds a record copy, and its failing and passing runs are recorded as the invariants skill gives (`invariant: <identifier>` line in the test). Mind that the existing script has its own rules about what it reads (UTF-8/UTF-16, binary files): a file of an image kind is exactly the "binary file" case it now skips, so settle how the new check recognizes an image file (extension, and/or content) and say in the report what it does not catch.

Files expected to change (not a closed list; the search of the foundation and the part map decide): `foundations/decisions.md`, `foundations/invariants.md`, `task-cycle/skill/request_template.md` (it says "with screenshots" for the top part, and must now say where screenshots come from and the "no place settled" item of *For you to decide*), `task-cycle/skill/SKILL.md` (the check before a record commit), `task-cycle/change/ui_check.md`, `task-cycle/record_template.md` if it must name the screenshot rule, `project-level/technology/` documents and `project-level/definition_template.md` (the fourth matter of WAY-121: place for screenshots), plus the script and its test. Keep what other skills and checks (`elements/common/foundation_check.py`, `task-cycle/request_check.py`, `agent-instructions/skill_entry_points.py`) require consistent; run their tests.

Scope boundary: no change in the loop2 repository or any product (task, *Out of scope*, question 8). the-way names no concrete place for screenshots (item 3); do not invent one, not even as an example inside normative text. Point data (paths, URLs) come from the task or the repo, never from memory. Write all prose of skills, templates and decisions in English, in the style of the neighbouring text; follow the repo's decision template exactly (identifier, *Scope*, *Based on*, *Relations*, *Verification*, *Rationale*, *Rejected*, *Origin*), and give each row its entry or tie it to an entry that already states it (WAY-33, WAY-134). Where settlement 4 corrects the wording of WAY-121 ("three matters"), edit WAY-121 in place and correct everything that repeats "three matters" (my grep found: `foundations/decisions.md` lines ~2804 and ~2856 and ~8250, `project-level/definition_template.md:168,186`, `project-level/technology/list.md:12,24`, `project-level/technology/research.md:37`, `project-level/technology/running_product.md:7,8,16,26`, `project-level/technology/start.md:16`, `project-level/technology/task_run.md:73`) — verify, those line numbers are a pointer, not a list. The task's text *Decisions in play* quotes WAY-219 for the case "foundation settles no such way"; this task adds a second, different case (the way exists but the foundation settles no place for screenshots): do not conflate them.

## The answers of the two questions at start

- Trust boundary: no. Irreversible operation: no.
- Open design choice at start: none (the form of the check script is yours to make). Reserved choice: none.
- Route: one author without a plan; your class `same`.

## What to read

Foundation entries, each whole (the entry runs to the next `###` heading in `foundations/decisions.md`, to the next `##` in other foundation files): decisions WAY-219, WAY-286, WAY-308, WAY-309, WAY-121 (the task's *Decisions in play*), and WAY-270, WAY-166, WAY-164, WAY-290, WAY-227; invariants `project-technology-record`, `script-language`, `script-imports`, `script-subprocesses`, `return-step-record`, `derived-file-content`. Entries these link to, as far as the work needs. Part map `foundations/part_map.md` (short, whole). Glossary `foundations/glossary.md` for terms you use (it is short enough to read whole if it is, otherwise search). Guidelines: the-way has no `guidelines/` directory; there are none to read.

Product-side reading for the change: every file you change, whole, before you change it. `task-cycle/skill/SKILL.md` is long; you read it whole because you change it.

## What the report holds

As `task-cycle/change/SKILL.md` section on reports gives it: status, commits, checks with command and exit code, the own-work check (WAY-164), reaches beyond this handoff, concerns, **Searches not found or unclear** (each thing looked for and not found/unclear, or `none`), the choice about the check script, and for each foundation entry one sentence of its meaning in English and one in Polish, marked `row <n>`, `projected` or `the cycle's`. Commit the work (git add by path, never `git add -A`), leaving the worktree clean; commit messages in English per the repo's habit (`git log` shows it). Do not push.
