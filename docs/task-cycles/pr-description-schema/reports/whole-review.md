FAIL 5b685df72352c3e0a0eea75981cb6e34b900dc09

# Review of the whole change — pr-description-schema

Range `f45ca40..5b685df` on `task/pr-description-schema`, three commits (`609a92f` foundation,
`d1d57db` template, script, tests, `5b685df` the cycle's files and `agent-instructions/README.md`).
One author without a plan; no slice. `git rev-parse HEAD` = `5b685df72352c3e0a0eea75981cb6e34b900dc09`,
the head given.

Counts: blocking 1 (Important), Minor 4, out of scope 1 (a Declined line).

## Findings

### Important

**I-1. For a task document in English, the template and the script require the opposite of what
WAY-288 says: the block must read `none`, while WAY-288 says the top part stands a second time in
the task document's language.**

What a human would see: a request for a task written in English gets no repeated top part, and the
script reports an error if the cycle writes one. That is a sensible rule. But the foundation entry
the change writes says something else, and nothing in the foundation says it.

- `foundations/decisions.md:8641-8642` (WAY-288, written whole from row 3): "A request's description
  is written in English, and its top part stands a second time, in the language of the task
  document, in a collapsed block of the description." No exception for an English task document.
- `task-cycle/skill/request_template.md:76-77` (skeleton: "none where the task document is in
  English") and `:122-124` ("where the task document is in English, the block holds only `none`
  after its summary (WAY-288)"). These cite WAY-288 for a rule WAY-288 does not hold.
- `task-cycle/request_check.py:433-434`: where the task is English and the block holds anything but
  `none`, it reports "the task document is in English; the block reads `none`". The docstring says
  the same at `:34-35`.
- The same unstated exception also reaches two other entries the change writes or changes:
  WAY-114 at `foundations/decisions.md:2461-2462` ("repeated in the human's language in the
  description's collapsed block"), and WAY-290 at `:8703-8704` ("the collapsed block in the task
  document's language"). For an English task document, the files make that block `none`.

Why it matters: WAY-263 grades this Important. The change's files fail to do what an entry the
change writes requires (repeat the top part), and they cite that entry for a rule it does not hold.
The exception changes row 3's meaning. WAY-134 lets the cycle write a row only whole, keeping its
meaning, and `task-cycle/skill/foundation_step.md` says "The writer never writes a row with another
meaning". So the exception cannot go into WAY-288 either. This is the same shape as finding A of
`reports/spec-review-2.md`, which the orchestrator settled in spec D10 A by writing the exception as
a decision of its own (WAY-291, `narrows WAY-290`, marked `the cycle's`). Spec D1 item 6 gives this
exception the same way, but no entry records it. The author's report saw it and passed it to the
orchestrator to weigh for *For you to decide* (`reports/author.md`, *Choices under Left to the
maker*, "WAY-288's binding sentence"). That shows the choice to the human, but after the merge
WAY-288 would still say one thing while the script enforces another. A later reviewer of an
English-task request, judging by WAY-288, has a foundation that contradicts the script.

Evidence: the lines quoted above. The script holds the `none` rule:
`test_request_check.py::LanguageTest::test_an_english_task_with_a_translated_block_is_reported`
passes on HEAD, as part of `python -B gate/run_tests.py task-cycle` (exit 0).

Fix (the smallest form the rules allow): add a decision written from the spec, not from a row.
Something like "What does the block hold where the task document is in English?": `none`, since the
English top part already serves that reader. It `narrows WAY-288`, is marked `the cycle's`, and
stands in this request's *For you to decide* under item 6, as WAY-291 does. Point the template's
`(WAY-288)` at `:124` to it. The other permitted way is to drop the `none` rule from template and
script, so that an English task's block repeats the top part, but that buys the reader nothing.

### Minor

**M-1. A description saved with a UTF-8 byte-order mark fails the state-line check with a message
that points at a line that looks correct.** `task-cycle/request_check.py:460-464` reads with
`encoding="utf-8"`, which keeps U+FEFF, and `:318-326` matches the first line's `strip()`, which
does not remove it. A scratch run of `check("\ufeff" + VALID, POLISH_TASK)` gives
`line 1: the first line gives no state` (probe below). On this Windows setup, PowerShell's
`Out-File` and `Set-Content -Encoding utf8` write that mark, and `gh pr create --body-file` would
publish it. An orchestrator that cannot see what is wrong with line 1 might take the WAY-291 route
and open a draft over a script defect. Reading with `utf-8-sig`, or stripping a leading U+FEFF, would
close it.

**M-2. The skeleton's placeholder heading passes when left in a description.** A description that
keeps `## <…>` with `none` beneath it, as an agent copying the skeleton
(`task-cycle/skill/request_template.md:101-104`) might write it, passes as a task's own section
(`request_check.py:363-364`). Probe: "placeholder heading left", no problem reported. The template's
"none of them where the task has none" can be read as "write `none` under it". The human then sees a
section headed `<…>`. Rejecting the placeholder text as a heading, or rewording the line to "leave
out the heading where the task has none", would close it.

**M-3. WAY-274 counts on the human seeing an addition to a product's logging scope at the merge.
Under the changed WAY-10 and the new WAY-287, the human reads only the decision section, and the
template does not put such an addition there.** `foundations/decisions.md:8120-8121` (WAY-274):
"An agent adds an item ... in the change that brings it, and the human sees it at the merge." The
author's report names this as its one concern and leaves it uncorrected
(`reports/author.md`, *Problems observed*). WAY-274 still holds word for word, since the item stands
in the diff and in *Technical changes*. But what it rests on is weaker: the human merges once
*For you to decide* reads `none` (WAY-287). Adding the case to the template's item list would go
beyond row 2 and To do 3. So it is a matter for the human. I agree with the author's
recommendation: name it in this request's *For you to decide* as a search finding ("make a task of
it?").

**M-4. The template reads marks and meaning sentences from the return step's report, but the return
step's own file does not ask for them.** `task-cycle/skill/request_template.md:173-177` takes item 6
from "the foundation step's and return step's reports" by the mark `the cycle's`.
`task-cycle/skill/foundation_step.md:17-20` now requires the two sentences and the mark.
`task-cycle/skill/return_step.md:8` says only "It writes, as the foundation step writes", and the
return-step agent is not sent to `foundation_step.md`. Most return-step entries are the cycle's
anyway, so the orchestrator can fill the gap. A row the foundation step missed, which the return
step writes whole and which should not appear in *For you to decide*, has no mark to say so. The
task's *Context* puts `return_step.md` in the collective task's area, which explains leaving it
alone. A one-line pointer there later would close it.

## Coverage of the task

| Item | Met by | Judgment |
|---|---|---|
| To do 1 — one template; step 13, *Request handoff*, `correction.md`, `foundation_step.md`, `reserved_return.md`, the README list point to it | `task-cycle/skill/request_template.md`; `SKILL.md` steps 12-13, `:196-197`, `:204-206`, 9.4 stop, `:351-353`; `record_template.md:164-172`; `correction.md:30-33`; `foundation_step.md:15,29`; `reserved_return.md:56-68,78-82`; `blocked_finding.md:11-13`; `agent-instructions/README.md:64-86` | met; grep for the removed field names and "step 13 names/gives under" outside `.runs/`, `docs/` finds none left |
| To do 2 — top part, order: state, what you will see (+ underneath), decisions, cost, how to merge | template skeleton `:51-71`, `:132-197`; script `TOP_HEADINGS`, `UNDERNEATH`, `check_state` | met |
| To do 3 — the decision section's list, `none` | template `:140-190`; WAY-287 | met |
| To do 4 — English, top part repeated in the task document's language in a collapsed block | template `:73-79`, `:120-124`; script block finder and language measure; WAY-288 | met for a non-English task; for an English task see I-1 |
| To do 5 — lower part in fixed order, items opening with a plain sentence, *Course* labels | template `:81-115`, `:125-128`, `:199-237`; script `LOWER_HEADINGS`; WAY-286 | met (labels not script-checked, as spec D1 gives) |
| To do 6 — empty section reads `none` | template `:47-48`; script content check | met |
| To do 7 — orchestrator judges Minor and out-of-scope findings, felt ones go up, all stay below | template item 8 `:183-188`; WAY-289 | met |
| To do 8 — WAY-114, WAY-134, WAY-10 changed | `foundations/decisions.md:2454-2498`, `:3240-3245`, `:289-313` | met in meaning; see I-1 for WAY-114's block clause |
| To do 9 — script checks heading order, content or `none`, block in the task's language; cycle runs it and corrects; tests run by the gate | `task-cycle/request_check.py`; `task-cycle/test_request_check.py` (tracked, run by `gate/run_tests.py task-cycle`); template `:9-43`; step 13 | met |
| Row 1 | WAY-286 | met; `Rejected: unknown` fits — the row's sources keep no rejected way for the layout |
| Row 2 | WAY-287 | met |
| Row 3 | WAY-288 | written whole; the template and script depart from it (I-1) |
| Row 4 | WAY-114, WAY-134, WAY-10 in place; restatements in `elements/common/way_of_working.md:135-137`, `elements/glossary/template.md:48-50`, `elements/decisions/template.md:131-133`, `elements/common/critique/SKILL.md:20-22`, `SKILL.md:204-206`, README `:85-86` | met; WAY-114's *Rejected* gains the three ways of the row's source |
| Row 5 | WAY-289; its rationale answers WAY-161's warning; WAY-161's rationale corrected | met |
| Row 6 | WAY-290, written whole; the exception in WAY-291 (`narrows WAY-290`), per spec D10 A | met |
| Carried question — English headings; *Checks* stays | spec D1; template and script constants; the agreement test | met; it is a choice beyond the task for *For you to decide* (template item 5) |
| *Context* — the digest keeps the "Process remarks" block | `record_template.md:164-172`, the item last in the last section, its wording unchanged | met (scratch check below) |
| *Out of scope* — screenshots' place, weekly review | not touched | respected |

## Source fidelity

- WAY-286 to WAY-290 match rows 1, 2, 3, 5 and 6. Each new entry's *Rejected* takes only the ways
  not chosen that its row's source keeps (row 3: three; row 5: three, from two questions; row 6:
  two), or `unknown` where the source keeps none (rows 1, 2). WAY-291 comes from the spec and
  carries the spec's rejected ways.
- WAY-114's changed binding sentence keeps the gate clause and the question clause word for word in
  meaning. It adds the row case and the merge case as row 4 and the answer "Zmiana dotyczy tylko
  sekcji decyzji" give. WAY-134's third binding sentence and WAY-10's binding sentence change as
  To do 8 gives.
- The test fixtures are written for the tests. They copy no private note, and no file of the change
  links into private notes (`outbound-link-reach`).
- Nothing invented that I found, apart from the unrecorded exception of I-1. The spec chose it, and
  the foundation does not record it.

## Foundation and guidelines read

Parts touched, by the part map: `task-cycle`, `agent-instructions`, `elements-common`, `decisions`,
`glossary`, plus `foundations/decisions.md`'s entries naming those scopes. No trust boundary
(`foundations/part_map.md:97-104`, `:127-140`). Read whole: the invariants of `every` part and of
`agent-instructions` (`foundations/invariants.md:6-160`); the task's *Decisions in play*
(WAY-03, 10, 49, 51, 114, 134, 140, 161, 162, 219, 227, 256, 261, 269); WAY-14, WAY-99, WAY-126,
WAY-172, WAY-263, WAY-268's opening, WAY-274; and every entry the diff writes or changes. I did not
read whole all 144 decisions whose *Scope* names a touched part (see *Searches*). The-way has no
`guidelines/` directory (WAY-215; the task's last answer), so no guideline rules applied.

Invariant tests: none changed. `script-language`, `script-imports` (argparse, re, sys, dataclasses,
pathlib, and io, tempfile, unittest, contextlib in the test) and `script-subprocesses` (none
started) hold for the new files. No surface, no *Violated* mark.

## Reserved choice

None. The script is Python on the standard library, like the other scripts of `task-cycle/`.

## The author's own-work check

It names the digest keeping the "Process remarks" block, a real requirement that no test of the-way
covers, and its scratch check with a negative control would catch a break. It does not reach the
weakest point I found (I-1), which sits in how the foundation entries fit the template. Its
threshold choice was measured on 57 real task documents and four real requests, a fair basis.

## Declined to judge

- The record-first routes (`blocked_finding.md`, the 9.4 stop) commit a record whose *Request URL*
  holds no link yet, so `project-level/plan_state.py` cannot find such a request from the committed
  record. Outside the task: the order was the same before this change, and only `reserved_return.md`
  has a fixed wording for it.

## Checks run

| Command or method | Exit | What it showed |
|---|---|---|
| `git rev-parse HEAD` | 0 | `5b685df72352c3e0a0eea75981cb6e34b900dc09`, the head given |
| `git diff f45ca40..5b685df`, `git log --stat f45ca40..5b685df` | 0 | the three commits, 15 files |
| `python -B gate/run_tests.py task-cycle` | 0 | 92 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | OK |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| `python -B gate/run_tests.py project-level` | 0 | 268 tests OK (fixtures with `## Request handoff`) |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors |
| `git diff --check f45ca40..5b685df` | 0 | no whitespace errors |
| `git ls-files --eol` on the three new files | 0 | `i/lf w/lf` |
| scratch `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\7a4fe94e-3148-4011-bad6-7d83342c594a\scratchpad\review_probe.py` (imports the script and the test fixtures; output `...\scratchpad\review_probe.txt`) | 0 | baseline passes; CRLF passes; BOM gives `line 1: the first line gives no state` (M-1); `## <…>` left in passes (M-2); a `##` line inside a multi-line HTML comment counts as a heading (judged harmless); state with `-` or `Ready` or no spaces round the dash reported; a nested heading in the block ignored; this cycle's frozen task reads `not English`, share 0.007 over 582 words |
| scratch CLI runs of `task-cycle/request_check.py` on a valid and a broken description (`...\scratchpad\out1.txt`, `out2.txt`, `out3.txt`) | 0 / 1 / 2 | exit 0 with a one-line summary; exit 1 with problems in file order and the Polish heading printed intact; exit 2 with `Error:` when `--task` is missing |
| scratch `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\7a4fe94e-3148-4011-bad6-7d83342c594a\scratchpad\digest_probe.py`: the digest's `extract_remark_blocks`, copied out of its source text (not imported, to avoid its imports), run on `record_template.md` with *Request handoff* filled and a lead-in list of two remarks | 0 | one block, both remarks in it, the *Description* line not leaking in; *Request handoff* is still the record's last section |
| manual: each line of the template's variants against WAY-140, WAY-162, WAY-163, WAY-219, WAY-261, WAY-269 and the old texts of step 13, `reserved_return.md`, the 9.4 stop | — | each item the old lists required has a place in the template |
| manual: `grep` over `foundations/*.md` for "at the merge", "by merging", "human who merges", "in its/the request" | — | the hits hold under the changed WAY-114, apart from WAY-274 (M-3); WAY-99's "accepted at the merge" concerns a word still `TODO` on the branch, which no row carries, so it holds |

Not run: the full gate (the orchestrator's run, by the handoff).

## Reaches beyond the handoff

- `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py:202-284`,
  named by the handoff. I copied its function text into a scratch script, read-only, for the digest
  check.
- `foundations/decisions.md` WAY-14 (`:430-451`), WAY-99 (`:2095-2120`), WAY-126 (`:2913-2950`),
  WAY-172 (`:4801-4836`), WAY-263 (`:7618-7643`), WAY-268's opening (`:7798-7810`), WAY-274
  (`:8115-8140`): hits of the search for restatements of WAY-114 and WAY-10.
- `task-cycle/skill/return_step.md` whole: for M-4.
- `elements/common/way_of_working.md:50-75` ("Reading the foundation"): for the selection.

## Searches not found or unclear

- I did not read whole every one of the 144 decisions whose *Scope* names `task-cycle`,
  `agent-instructions`, `elements-common`, `decisions` or `glossary`, as "Reading the foundation"
  asks. I read the task's *Decisions in play*, the changed entries and the hits of targeted
  searches. An entry outside those that restates the request's content went unseen if no search
  word hit it.
- Whether the orchestrator already counts the English-task `none` rule as settled by spec D1 item 6.
  The spec's D10 settled only findings A and B of its review, and neither reaches this rule, so I
  judged it by WAY-134 and WAY-263 (I-1).
