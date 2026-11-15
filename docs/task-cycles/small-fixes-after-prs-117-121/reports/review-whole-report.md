FAIL e9aea956e73cfcf94f94d462b9e28e3a0e3e5330

# Review of the whole change — task `small-fixes-after-prs-117-121`

Range `b6b3416..e9aea95` (five commits, one author, no plan; `git rev-parse HEAD` = `e9aea95`, confirmed).
The route has no plan and no slices, so every blocking finding below comes from no slice: it comes
from the one author's change.

## Findings

### Critical

none

### Important (blocking, within the task)

**I1 — To do 19 is not met for the quotation marks of its own source: `„…”` is not read as a quotation.**
Comes from no slice (no plan); commit `76c2bd2` (code, test) and `52b122b` (template).

- Place: `elements/common/foundation_check.py:164` (`QUOTED = re.compile(r"\"[^\"]*\"|\u201c[^\u201d]*\u201d")`),
  used by `begins_sentence` at `elements/common/foundation_check.py:311-319`; the docstring at
  `elements/common/foundation_check.py:77-79` and the template `elements/decisions/template.md:238-241`
  both name only `"…"` or `“…”`; the test `elements/common/test_foundation_check.py:1149-1165` tries only
  `"…"` and `“…”`.
- What is wrong: the item says a full stop and a space inside a quotation „…” or "…" ends no binding
  sentence. Its source note (`_zadania/the author's task note on the binding sentence and the full stop in a quotation.md`, linked from
  the item) gives as the cases D-216, D-222 and D-345 of loop2, which quote Polish text opened with `„`
  (U+201E) and closed with `”` (U+201D). The pattern accepts only an opening `“` (U+201C), so for every
  case the item was written for, a `decision:` line that quotes from the middle of the quoted string still
  passes as the start of a sentence.
- Evidence: in loop2, `foundations/decisions.md:5070-5071` (D-222) holds
  `\u201eJe\u015bli to konto ma potwierdzony adres, wys\u0142ali\u015bmy na niego odno\u015bnik. Gdy ...\u201d`
  (read as escaped code points). A scratch run of `begins_sentence` from the head commit on
  `A game says „Saved. Next game is ready” when saved.` returned `True` for `Next` (a sentence start),
  while the same text with `“…”` or `"…"` returned `False`.
- Why it matters: the item's one purpose — stop the check accepting a quotation that starts inside a
  quoted example — is not reached for the product it was written for. The author's own-work check
  aimed at To do 1–2, not here, and its mutation list does not include the `„` form.
- Fix: add the `„…”` pair (opening U+201E, closing U+201D) to the pattern, to the docstring and to the
  template's wording, and a third case to the test's loop.

**I2 — Entries written from rows 1, 3 and 5 gained pairs of examples the rows do not give, yet are marked `row <n>`, so the request will not put them before the human — the very gap row 9 closes.**
Comes from no slice (no plan); the entries are in commit `52b122b`, the marks in the author's report.

- Place: the table "Entries written (foundation step)" of
  `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-report.md:45-52` marks WAY-139 `row 1`,
  WAY-344 `row 3` and WAY-60 `row 5`. The rule the change itself writes is at
  `task-cycle/skill/foundation_step.md:30-34`: "a part the writer adds that its row or projected entry does
  not give — a pair of examples, a field the projected entry left `TODO` — makes the entry `the cycle's`,
  save a pair kept only until a test of the same change holds the sentence, and a link written into its
  *Relations* does not; the request puts each entry so marked before the human (WAY-114)".
- The added pairs: WAY-139 `foundations/decisions.md:4372-4374` (complies: "the item that writes into the
  skill the answer a decision gives for how a human learns of a failure, or the record of the human's
  refusal to settle it, points to the guide as well") and `:4382-4383` (violates: "an item that writes into
  the skill the answer for how to read the logs, how long the record lives or how a human learns of a
  failure names no guide"); WAY-344 `:2904-2906` (complies: "the same script, reading a copy of the file at
  the commit the branch left, lists an absent section of that copy on a line `listed:` and keeps its exit
  code") and `:2914-2916` (violates: "a script that checks the form of a file ends with an error at a field
  missing from the copy at the commit the branch left, or passes over it without a word"); WAY-60
  `:1846-1848` and `:1853-1854`. None of rows 1, 3, 5 gives an example, and none of these pairs is kept only
  until a test of this change holds the sentence (WAY-344's test already holds it, and the pair stays).
  WAY-139's sentence also reaches beyond row 1 ("or the record of the human's refusal").
- Why it matters: `task-cycle/skill/request_template.md:295-303` lists under section 6 only entries marked
  `the cycle's`, and says entries "written whole from rows" are not there. With these marks the human
  merges new examples by which agents will judge later changes without having seen them — the exact
  failure AIR-661 describes in the task's *Need* and that row 9 settles. To do 6 requires WAY-139's
  *Verification* to agree with the change, so the pair there is required; what row 9 settles is that it is
  shown.
- Fix: none in the commits. Mark WAY-139, WAY-344 and WAY-60 `the cycle's` in the author's report (or
  have the orchestrator put them under section 6 of the request with their added pairs), as the change's
  own rule gives.

### Minor, within the task

**m1 — WAY-60's new compliance example reads as contradicting itself.**
`foundations/decisions.md:1845-1848`: "an invariant whose condition a decision of the pinned the-way holds
names that decision's number in its sentence, its template giving no field for it, and, where a link to that
decision is due, names it also in *Derives from*". The first half says the template has no field for that
decision; the second puts it in *Derives from*. `elements/invariants/template.md:139-142` says a decision
of the pinned the-way "is no decision entry" of the product's log, and *Derives from* names decision
entries (`:114`), so a product reader is led to put a the-way number where the template gives no place. The
task's own case (`tracked-file-private-paths`, an invariant of the-way citing WAY-309 and WAY-323 of its own
log in its sentence and in *Derives from*) shows the clause without that tension. Suggest the example use a
decision of the product's own log, as the task's source does.

**m2 — WAY-229 now names the Claude Code setting `availableModels` without saying so, and gives no rule for a session with no such list.**
`foundations/decisions.md:5948-5950` and the two steps of `task-cycle/skill/SKILL.md:451-453` and
`:501-503`. WAY-370 (`foundations/decisions.md`, "What does a task cycle do where the session has none of
the-way's agent types?") has the cycle run where "the harness is not Claude Code"; there the orchestrator
finds no `availableModels`, and in Claude Code a session with every model allowed has no list either. The
rationale still says "Classes in general terms survive the release of new models and fit any harness"
(`:6034`). The naming of the setting is what To do 20 asks for, so this is a task-mandated wording with a
gap: suggest "(in Claude Code, the setting `availableModels`; with no such list, every model the session
offers)".

**m3 — WAY-229's rationale states harness behaviour as general from one session.**
`foundations/decisions.md:6030-6033` and `:6059-6060`: "A request for a model outside that list gets the
session's own model". The session record the handoff names
(`the session record that item 20 of the task names (a Claude Code session record of the author's, outside the repository)`, the
three `subagents/*.meta.json` with `"model":"fable"`) shows `pickedEffortModel` `claude-sonnet-5-5`, and every
main-session reply is `claude-sonnet-5-5`; the agent type has no `model` field. So the fallback seen equals
both the session's model and the harness's default for a type without a model; the log cannot tell which
rule applies. Suggest "gets another model, in the observed case the session's own" or citing it as an
environment fact.

**m4 — The plan skill's new run with the switch is not the run WAY-321's binding sentence exempts.**
`task-cycle/plan/SKILL.md:177-181` has a slice's *Checks* run `foundation_check.py --skip-test-citations`.
WAY-321's binding sentence (`foundations/decisions.md:1981-1985`) reports an uncited `test` invariant "in
every run but the one made right after an entry is written". A slice's *Checks* run comes after the
slice's other work, so a reviewer reading WAY-321 literally can call the plan sentence a breach — the kind of
dispute To do 14 removes elsewhere. Row 8 settles the plan sentence and WAY-321 stays unchanged by the task,
so the fix is a clause in the plan sentence saying that run counts as the run after the entry is written,
or naming this case at the next change of WAY-321.

**m5 — The plan sentence names the check by its path in the-way only.**
`task-cycle/plan/SKILL.md:179`: "`elements/common/foundation_check.py`". *Checks* must be "commands that can
actually run in the product" (`:172`); in a product the path is `.the-way/elements/common/foundation_check.py`,
as the same file writes for its script at `:207-208`.

**m6 — No test covers the listing of a base-lacking invariant when a citing file did change.**
`elements/common/foundation_check.py:740-747` lists such an invariant whether or not a citing file changed
(the author's choice 2, and what WAY-344's new sentence requires). All three new tests
(`elements/common/test_foundation_check.py:1584-1608`) keep the citing file unchanged, so moving the base
check after the citing-file filter would pass them. A scratch run on the head with
`tests/test_saving.py` touched gave the listed line and exit 0, so the behaviour is right today; only its
protection is missing.

**m7 — The two new descriptions of the listing read more broadly than the code.**
`agent-instructions/README.md:15-17` ("and those whose copy at that commit lacks *Method* or *Part*, naming
the field, both against the commit…") and the row *sentence* of `elements/invariants/template.md:176` ("and
one whose copy at the base lacks *Method* or *Part*") can be read as listing every invariant whose base copy
lacks a field; the code lists only one that reads `test` now and whose sentence was reworded. In the README,
"that commit" also comes before the commit is named, and the joined line is longer than its neighbours.

**m8 — In `resolve_gaps.md` the list of three items now hangs on the sentence about the guide.**
`project-level/task/skill/resolve_gaps.md:91-95`: the colon that introduced the bullets now ends "…since
the guide has a part for each of the three:", so the bullets read as parts of the guide instead of the cases
the check handles. Suggest putting the new sentence after the bullets, or ending it with a full stop and
keeping "(WAY-139):" for the list.

### Minor or other, outside the task's scope

**o1 — The request's section 6 gives one sentence of an entry's meaning, not the pair of examples that made it `the cycle's`.**
`task-cycle/skill/request_template.md:295-297`. Row 9's aim is that the human sees an added pair before
merging; section 6 asks only for "one plain sentence of its meaning", so an entry that is `the cycle's` only
by its pair can still reach the human without the pair. The task carries only items 17 and 18 for this, so
the template's section is outside it. Minor.

## Coverage of the task

| Item / row | Met by | Note |
|---|---|---|
| To do 1 | `gate/test_run_tests.py:40-55, 58-94, 318-322, 402-414` | one empty file per event, read back sorted |
| To do 2 | wait logic unchanged, limit 120 s at `:85` | author's forced serial run failed in 240.6 s; read, not rerun |
| To do 5 | `project-level/task/skill/resolve_gaps.md:91-95` | m8 |
| To do 6 | WAY-139 sentence, *Verification*, *Rationale*, *Rejected* | I2 (mark) |
| To do 7 | the three templates, last item each | wording checked against WAY-172 |
| To do 8 | `foundation_check.py:723-747`, tests `:1578-1608` | m6, m7 |
| To do 9 | WAY-344 `:2857-2860` | I2 (mark) |
| To do 10 | `elements/decisions/template.md:88-89` | text matches the item word for word |
| To do 11 | `task-cycle/skill/foundation_step.md:40-41` | matches |
| To do 12 | WAY-60 `:1832-1834`; invariants template `:86-88` | m1 |
| To do 13 | `project-level/task/template.md:97-99` | word matches `project-level/plan/template.md:100` |
| To do 14 | `task-cycle/plan/SKILL.md:172-177`; WAY-160 rationale `:2811-2813` | |
| To do 15 | WAY-61 *Scope* `:1889` | |
| To do 16 | `task-cycle/plan/SKILL.md:177-181` | m4, m5 |
| To do 17 | `task-cycle/skill/foundation_step.md:30-34` | quoted text present; the author's added clause on *Relations* follows the item's second sentence |
| To do 18 | `elements/decisions/skill/SKILL.md:37-38` | matches |
| To do 19 | code, template, test | **I1** |
| To do 20 | WAY-229 and `task-cycle/skill/SKILL.md:451-453, 501-503` | m2, m3 |
| Rows 1–9 | each written in its *Goes to* place | I2 on the marks of rows 1, 3, 5 |

Items 3 and 4 are withdrawn/moved; nothing was made for them, as the task says.

## Declined to judge

- How loop2's existing `decision:` lines fare once loop2 pins this commit — the task says the item does not
  touch loop2's lines.
- The reconciliation of WAY-344 and `foundation_check.py` with the other task that changes them — the task
  settles that the cycle merged second reconciles them.
- The vault-side check of task statuses that must recognise `dropped — approved by human` — outside the
  repository, the task's *Context* gives it to the advisor or the human.
- The author's commit of six decisions in one commit (`52b122b`) — a matter of commit shape, no effect on
  the tree.

## Checks run

All in a worktree of the head `e9aea95` at `.runs/review-whole/head` unless named otherwise.

| Command | Exit | Result |
|---|---|---|
| `python -B task-cycle/change_file_sizes.py b6b3416 e9aea95` (reviewed worktree, read-only) | 0 | `foundation_check.py` 1003 → 984; new `foundation_source.py` 57; `test_foundation_check.py` 1623 → 1664 (test file, outside the rule); `test_run_tests.py` 552 → 567 |
| `agent-instructions/test_size_invariant.py` with the `expectedFailure` mark taken off, `python -B -m unittest agent-instructions.test_size_invariant`, in base and head worktrees | 1 both (expected: invariant marked violated) | base names 11 functions and 3 files; head the same 11 functions and 2 files — `foundation_check.py: 1003 lines` gone, nothing new. The mark was restored with `git checkout` in both worktrees. |
| `python -B gate/run_tests.py elements/common` | 0 | 245 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 36 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 tests OK (expected failures=2) |
| `python -B gate/run_tests.py project-level` | 0 | 279 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 534 tests OK (skipped=1) |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| scratch: `begins_sentence` of the head on one sentence in `„…”`, `“…”` and `"…"` | 0 | `True`, `False`, `False` — I1 |
| scratch: the test module's `reworded()` with a base lacking *Method* and the citing file touched | 0 | one `listed:` line naming *Method*, `0 errors` — m6 |
| manual: `decision_index.py --sections`, then the index of the selection below | 0 | read |
| manual: loop2 `foundations/decisions.md:5068-5073` read as code points | — | D-222 opens its quotation with U+201E |
| manual: the session record and three `meta.json` files the handoff names | — | `model: fable` requests ran as `claude-sonnet-5-5`; main session all `claude-sonnet-5-5` — m3 |

Not run: the full gate (the orchestrator's run, WAY-160); a serial run of
`test_by_default_every_directory_runs_at_the_same_time` (240 s; the waiting code is unchanged by the fix,
so I read it instead). `relation-model`, `process-audit`, `instruction-files`, `installation`,
`product-guidelines` were not run (no file of theirs changed; `product-guidelines` holds the three changed
templates, whose test checks pointers only — the author reports it ran OK).

## Selection and reaches

- Parts: gate, elements-common, decisions, invariants, project-level, product-guidelines, task-cycle,
  agent-instructions.
- Index: `decision_index.py` with the sections "Decision entries and the decision log", "Invariants",
  "Scripts and the gate", "The course of a task cycle", "Task refinement and readiness", "The running
  product", "Writing and approving guidelines", "The-way's own coding and testing guidelines", `--part`
  for each part above and `--decision` for WAY-139, 344, 60, 61, 229, 160, 134, 172, 173, 17, 321, 62, 142,
  114, 03, 07, 385, 365, 395: 87 listed in full, 131 by heading; the whole index read, and the headings run
  through.
- Guidelines read whole: `guidelines/coding.md`, `guidelines/coding-check.md`,
  `guidelines/coding-shared-module.md` (kind row matches the new imported module), `guidelines/testing.md`.
- Invariants read whole: `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`,
  `gate-exit-code`, `test-method-citation`, `map-reference-target`, `function-and-file-size`.
- Part map: `foundations/part_map.md` lines 60-244 (the touched parts and the surfaces).
- Reaches beyond the dispatch: the task's source note
  `the author's task note on the binding sentence and the full stop in a quotation`
  (the source of To do 19, for source fidelity) and loop2 `foundations/decisions.md:5068-5073` (the quotation
  marks its examples use) — I1; `task-cycle/skill/request_template.md:285-310` (what section 6 shows) — I2, o1;
  `elements/invariants/template.md` whole (the clause's place and *Derives from*) — m1;
  `project-level/task/deployment_skill_guide.md` headings and the refusal passage `:287-306` — WAY-139's added
  refusal case; the session record and `meta.json` files the handoff names — m3; `project-level/plan/template.md:100`
  — To do 13; grep of `project-level/*.py` for task `Status:` readers — no script reads the four values.

## Working copies

- `.runs/review-whole/head` (worktree of `e9aea95`) and `.runs/review-whole/base` (worktree of `b6b3416`):
  removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-whole/` files (the index, the sections list, the run outputs, the size outputs): deleted;
  the directory stands empty. Nothing kept in `reports/` besides this report. Remainder: none.

## Unread material

- Decisions of the index read whole: 11 — WAY-03, WAY-60, WAY-61, WAY-62, WAY-69, WAY-139, WAY-160,
  WAY-172, WAY-229, WAY-321, WAY-344. Read by their binding sentences in the index only, though they bear on
  the change: WAY-134, WAY-114, WAY-17, WAY-12, WAY-142, WAY-173, WAY-385, WAY-365; WAY-368 and WAY-370 read
  as far as their *Verification* and *Scope*.
- Invariants with *Part* `every` or a touched part beyond the eight above (about 40) were not read whole;
  their tests ran in the focused directories above.
- Guideline files: none unread.
- `foundations/glossary.md`: not read (no glossary term is written or changed, and no finding rests on one).

## Searches not found or unclear

- No environment fact or harness document for what a subagent request for a model outside the allowed list
  gets; only the one session record (m3).
- Whether the-way's task cycle is meant to run in Codex with the binding sentence of WAY-229 as it now
  stands — WAY-370 says the cycle runs without its types in another harness, and nothing says how
  `availableModels` reads there (m2).
