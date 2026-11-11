FAIL a5ebc881f3226408d76783424287f3f9dcaf7fc0

# Review of the whole change — weekly process audit (`52f8164..a5ebc88`)

`git rev-parse HEAD` in `the worktree of the task` is
`a5ebc881f3226408d76783424287f3f9dcaf7fc0`, as the handoff gives. The diff judged is `git diff 52f8164..HEAD` (58 files,
+4971 −101); `git log 52f8164..HEAD` holds the 21 commits from `1adca16` to `a5ebc88` (the pair `4c906d7`/`e4085bf`, a copy
of the record added and removed, leaves no file in the diff). The reviewed worktree, its index and its branch were not changed
(`git status --short` empty at the end); every run was made in a detached worktree of `a5ebc88` under the session's
scratchpad, removed at the end, or on temporary directories.

Method: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`, read whole.

Counts: **5 blocking** (Important), **27 Minor**, **4 out of scope** (the lines of Declined to judge).

## Blocking findings

### B1. Important — the agents' working time and the wait for tools are `unknown` in every cycle the process records

Spans slice 2 (`876710c`) and slice 3 (`58ca0de`).

Place: `task-cycle/cycle_stages.py:231-241` (`add_call_notes`), `:782-788` (`wait_totals`), `:838-845` (the summary lines);
`process-audit/audit_count.py:537-538` (`stages_time` reads a line opening with `unknown` as unknown); the step that runs the
script, `task-cycle/skill/SKILL.md:439-443`.

What is wrong. Step 12 has the orchestrator run `cycle_stages.py` on its own live session (`CLAUDE_CODE_SESSION_ID`,
`CODEX_SESSION_ID`). At that moment the transcript holds the tool call that runs the script, and not yet its result. Slice 2
counts such a call as one "with no readable result", which makes the cycle's *Waiting for tools* `unknown — at least …` and
*Working time without waiting for tools* `unknown — at most …`, and the audit reads both as `unknown`. So no cycle made by the
process as written ever gives the two times that *To do* 3 ("czas pracy agentów i czas czekania na narzędzia"), *To do* 7 and
WAY-337 ask for.

Why it matters. The time is one of the three measures the audit exists for (better, cheaper, faster). The safe direction
(`unknown`, not a wrong figure) does not save it: the measure is empty everywhere, with a warning nobody can act on. Slice 2's
executor saw it ("a check run during a cycle will always carry that warning") and called it correct; slice 2 had no review.

Evidence. This cycle's own copy, `git show 4c906d7:docs/task-cycles/weekly-process-audit/stages.md`: "Warnings: … the
orchestrator: 1 tool call(s) with no readable result: their waits are unknown". The count on the-way's history (scratch run
below) gives for that cycle *Working time without waiting for tools* `unknown` and *Waiting for tools* `unknown`, reasons
"`stages.md` gives the … as unknown". No test covers a transcript whose last entry is an open call.

Direction (the author's choice): an open call at the end of a transcript lies outside every working window anyway (a window
ends at the last activity), so it can be counted as ending where the transcript ends, or left out with a note, while an open
call followed by later activity stays `unknown`.

### B2. Important — a findings file named at the end of a sentence is not read, so the share of fix rounds is lost for ordinary prose

From the correction (`b43558a`).

Place: `task-cycle/cycle_stages.py:175` (`FILE_NAMED`) and `:180-197` (`files_named`, the check `not name.endswith(".md")` at
`:188`).

What is wrong. The name is taken as the whole run of `[A-Za-z0-9_.-]`, which swallows a full stop after the path, and the
name is then dropped for not ending in `.md`. Run on the head commit: `files_named("Fix the findings in
reports/review_slice4_findings.md.")` gives `[]`; the same with `,`, `)` or `:` after the path gives the file. WAY-336, which
this change writes, says a turn serves a fix round "when the message that dispatches or resumes it names the round's findings
file by its path in the cycle's `reports/`"; a message ending its sentence with that path names it, and the code does not see
it. By WAY-263 a change whose files fail to do what an entry it writes requires is Important.

Why it matters. The human decided that the share be made in this request so that it has a value; a period after a path is the
most ordinary way to write it, and either message of a round losing the file makes the round named by fewer than two turns, so
the share is `unknown`. Under a record that reads `none`, a turn given `reports/x_findings.md.` also escapes the cross-check
that turns a stray findings file into `unknown`. The test of crafted names (`test_cycle_stages.py:617`) has `.md.bak` and
`.mdx`, no path before a full stop.

Direction: strip trailing dots from the name before the checks (a name ending `.md.` is the file `.md`), with a test.

### B3. Important — no file leads the widening of the list of classes that WAY-332 and settlement row 4 give the audit

From slice 7 (`94a4f4e`), with slice 5 (`c2a0169`) for the refusal; the entry is the Foundation entries' (`1adca16`).

Place: `process-audit/SKILL.md:10-13` ("It changes nothing in any repository and nothing in the register of problems"),
`:120-123` (refused rows "which the user's own tool corrects in the register"), `:142-143` (a wrong register is "the user's own
tool's to make: note it in the result"); `process-audit/audit_count.py:1369-1370` (a class the list lacks refuses the row);
`foundations/decisions.md` WAY-332.

What is wrong. WAY-332 says each problem has "a class from a list that the template of the register starts and the audit
widens"; its *complies* reads "a session of the audit that meets a problem no class fits adds a class to the list" and its
*violates* "the audit refuses a problem for a class the list lacks instead of widening the list". Settlement row 4's source is
"listę startową klas poprawianą w audycie". The skill has no step in which the session meets a problem no class fits and
widens the list: it forbids touching the register and sends a row refused for its class to the user's tool as an error to
correct. The command refuses such a row ("the class is not in the list of classes"), which is the *violates* example, and
nothing downstream turns it into a new class. The template (`process-audit/problem_register.md:53-57`) states the widening
with no actor. By WAY-263, files that fail to do what an entry the change writes requires are Important.

Why it matters. The list of classes is one of the three things whose change starts a series (WAY-338); a list nobody widens
pushes problems into the nearest class, which the template itself forbids, or leaves them refused week after week.

Direction (the author's choice): a matter of the session, where a refused class row or the human's own reading shows a
problem no class fits, puts a new class (name, meaning, date added) before the human and writes it into the note for the
user's tool, or into the register's *Classes* on the human's yes; WAY-329's "gives no problem a class itself" stays kept, since
widening the list assigns no class to a problem.

### B4. Important — `task-cycle/cycle_stages.py` reads untrusted transcript text and the part map records no trust boundary for it

Spans slice 2 (`876710c`) and the correction (`b43558a`). The orchestrator's choice (1), judged and not accepted.

Place: `foundations/part_map.md:100` (`task-cycle`: *Trust boundary* none); `task-cycle/cycle_stages.py:254-272`
(`codex_message_text`), `:464-491` (Claude Code user lines and tool calls), `:180-197` (`files_named`).

What is wrong. WAY-48 records a trust boundary "at the part that holds it, as a pattern of the code files which take in what
the product does not control — … files that come from outside the product, such as one on the user's disk". Session
transcripts lie on the user's disk, the map's own *External context* already marks "session records" untrusted, and this
change makes the script read the free text of the messages that start each turn and turn file names found in it into a
measure of the audit. The cycle's own start answer names `cycle_stages.py` as a boundary; the part map, which this change
edits, does not.

Why it matters. WAY-48: "A change that touches the files of a boundary is checked for crafted input, and its review is aimed
at that risk." The plan marked slice 2 `Risk: none` from the map, so slice 2's changes to the reading of transcripts got no
review of their own — the defect of B1 came through that gap. The next change to the script will be planned the same way.
Before this change the script read token counts, times and agent names; the reading of message text is new.

Direction: add `task-cycle/cycle_stages.py` to the *Trust boundary* of `task-cycle` (one line; the foundation check accepts a
pattern that matches a tracked file).

### B5. Important — the skill and the result define a series more broadly than WAY-338, citing it

Spans slice 6 (`260b650`) and slice 7 (`94a4f4e`). The orchestrator's choice (4), judged: the computation is acceptable, its
account is not.

Place: `process-audit/SKILL.md:43-46` ("**Measures are compared inside a series only** (WAY-338). A series is a run of
versions of the process between which the price list, the register's list of classes and the reviewed files of the-way did not
change."); `process-audit/audit_count.py:1763-1770` (the paragraph of the result, the same, citing WAY-338).

What is wrong. WAY-338 starts a series at "a new price list, or a change of the form of a stage report, of the list of classes
or of the instructions of the reviewer". The count starts one at any change of `task-cycle/change`, `plan`, `review`, `spec`
or `cycle_stages.py` (`TREE_PATHS`, `:236-237`; `Ancestry.changed`, `:1463-1469`). The docstring (`:89-91`) says this is a
deliberately conservative approximation; the skill, which every audit session follows, and the result's paragraph state it as
what a series is, under WAY-338's number, with no word that it is wider. WAY-263: another changed file that restates an entry
the change writes "more broadly" is Important.

Why it matters. A later agent reads the skill's sentence as the rule of WAY-338 and builds on it (the rationale of WAY-263).
The cost of the rule itself is visible: on the-way's own history 20 series for 53 versions; it compares less, never across a
change WAY-338 names inside those paths, and I accept it as the computation.

Direction: say in the skill and in the result's paragraph that the count splits at any change of those files, more often than
WAY-338 requires, so that it compares less; or record the wider rule in WAY-338 through the return step.

## Minor findings

All within the task unless marked otherwise.

### Of this review

- **m1** — `process-audit/audit_count.py:1494-1498` and `:1525-1538` (`analyse`). Two cycles whose records one commit adds
  share one *Record*; the register cannot tell them apart, and a problem naming that commit is shown under both cycles in
  *Problems by cycle* (counted twice, against WAY-333), while *Open issues* counts one cycle. Evidence: a temporary repository
  with one commit adding `docs/task-cycles/a/cycle.md` and `docs/task-cycles/b/cycle.md` and one register row: exit 0, two
  identical rows `| prod | e3abc5f… | foundation-gap | 0 | 1 | 0 | 0 | 0 |`. No such commit in the-way's history (0 doubled
  records among 72 cycles); a bulk import of records or a crafted history gives it. Direction: `unknown` for a *Record* that
  names more than one cycle.
- **m2** — `process-audit/SKILL.md:101-102`: exit `2` "names the file, key, entry or argument that is missing or wrong, never a
  path". The errors of the locations file and of the price list name the path given (`audit_count.py:272-279`, `:611-635`);
  for the default price list that is the absolute path of the checkout. An agent that copies the line into a report carries a
  path the skill says is never there (WAY-320). Direction: name the option instead, or say so in the skill.
- **m3** — `process-audit/audit_count.py:1918` (header "Cycles in which its problem came back") with `:1595` (`len(hit)`),
  repeated at `process-audit/SKILL.md:132-133`. The count includes the cycle where the problem first stood, which did not come
  back; the paragraph above the table says "an open issue's cycles are those its problems stand in", the header says
  otherwise. Direction: "Cycles in which its problems stand".
- **m4** — the words "issue" (sprawa) and "series" carry a meaning of their own in WAY-329, WAY-333, WAY-335, WAY-338,
  `process-audit/SKILL.md` and `process-audit/problem_register.md`, with no glossary entry. Each file that uses them defines
  them inline except WAY-333, WAY-335 and WAY-338, whose readers meet "issue" or "series" undefined; I found no sentence read
  wrongly for lack of an entry. For the return step (WAY-95).
- **m5** — lines left unwrapped after the edit: `foundations/decisions.md:228` (WAY-09) and `task-cycle/skill/SKILL.md:168`,
  each well over the width of the rest of their files. Polish.

### Carried from the slice reviews, graded here (each still present at `a5ebc88`)

- **S3-M1** — `process-audit/audit_count.py:290-296`: an integer of more than 4300 digits in the locations file raises a plain
  `ValueError` that is not caught: exit 1 with a traceback instead of `Error: … is not JSON` and exit 2. Minor: the file is the
  user's own.
- **S3-M2** — `process-audit/audit_count.py:377-384` (`Git.execute`): git inherits `GIT_DIR`, `GIT_WORK_TREE`,
  `GIT_CONFIG_*` and the like, and `log.showSignature` of a repository's configuration; with `GIT_DIR` set, the count of `q` is
  another repository's. Minor: needs a set environment or write access to a named checkout.
- **S3-M3** — `process-audit/audit_count.py:1985-1990`: the refusal to write the result inside a repository covers only the
  repositories read in the run, not the-way's checkout when it is not read; WAY-331 says no repository, the-way's included,
  holds the results.
- **S3fix-M** — `process-audit/audit_count.py:110-112`, the module docstring: "each control character and each bar written as
  `\x..`" does not say that a bar and the literal text `\x7c` come out the same.
- **S4-3** — `process-audit/audit_count.py:937`, `:940`, `:943` (`priced`): a stage or model name from `stages.md` is copied
  whole into the reasons, twice per cycle, with no cap (a 2,000,000-character model name gave a 4 MB result in the slice-4
  review). Size only; `cell()` neutralises the content.
- **S4-4** — `process-audit/audit_count.py:659-662`: a price cell that is neither a number nor `—` (a typo, `1e9`) makes the
  model unpriced instead of refusing the list, and every cycle using it reads "the price list gives no price", pointing away
  from the list.
- **S4-5** — `process-audit/test_audit_count.py:383-391` (`Times.time_rows`): the narrowed time tests no longer notice a stray
  `unknown` of *Process pin* or *Remarks* for the same record (other tests cover those).
- **S4-6** — tests of the trust boundary still missing in part: a stage or model name with a bar, a control character or an
  escape in a reason; a price list with a non-number cell, a doubled or invalid `List date`, an oversized list; a `stages.md`
  whose section appears twice. (The zero-token section and the crafted *Files named* cells now have tests.)
- **S4-7** (out of scope in the slice-4 review; within the task here, since slice 2 is part of it) —
  `task-cycle/cycle_stages.py:882` writes `—` with zero counts for a stage with no usage found, so a stage whose usage was
  not read and a stage with no tokens are the same row; the audit makes the first `unknown` for a subagent and zero for a plain
  orchestrator stretch, which is the right reading in the cases seen.
- **Corr-M1** — `process-audit/audit_count.py:983-1018` (`fix_rounds_share`): the turns naming a findings file have a lower
  bound (two) and no upper one, so a stray later mention adds that turn's cost to the share (97.2 % against 28.9 % in the
  correction review's scratch); with the item `none`, a turn whose cell is `unknown`, or a fix turn given a file without the
  word `findings`, does not trip the cross-check and the share reads `0.0%`. Rests on the record's own word.
- **Corr-M2** — `process-audit/audit_count.py:929-934` (`priced`): only a row named exactly `orchestrator` with the model `—`
  costs nothing; a tokenless `orchestrator while in parallel: …` row, which `cycle_stages.py` creates for a tool call alone
  (`orchestrator_row`, `cycle_stages.py:679-694`), makes the cost of the whole cycle `unknown`. `is_orchestrator_row` exists.
- **Corr-M3** — `task-cycle/cycle_stages.py:254-272` and the first-wins assignments `messages[owner] = …` in `read_codex_agent` (`:315`, `:331`):
  the Codex reader takes the first user message of a turn, which a real rollout fills with the injected `AGENTS.md` text, so the
  prompt's files are not read; the effect is `unknown` (or `0.0%` under a `none` item).
- **Corr-M4** — `process-audit/audit_count.py:999-1000`: the model rows of one `#` are merged and the first row's *Files
  named* kept, with no note where two rows of one number differ in stage name or cell.
- **S5-2** — `process-audit/audit_count.py:1587`: an open issue's days of waiting count from the cycle's first commit, not
  from the commit the problem's *Record* names (the slice's binding choice 5); longer, never shorter, and only for a corrected
  cycle.
- **S5-3** — `process-audit/audit_count.py:1540-1545` and the refused rows: the work and the output are not bounded by the
  register's size (issues × problems scan; 300,000 refused rows gave a 19.4 MB result; a `merge-base` call per distinct pin and
  fix). Linear or quadratic in a register far larger than a real one.
- **S5-4** — untested branches: the ambiguous short hash, the *Problems whose cycle is not read* columns of *Fixed* and
  *Dropped issues*, a short pin resolved by `--disambiguate`, a shallow clone of the-way, a doubled heading or header row of a
  table.
- **S5fix-M1** — `process-audit/audit_count.py:1567-1568`, `:1595-1599`: *Problems with an unknown pin* and *Problems whose
  cycle is not read* stay exact while the columns beside them read `at least n`, against the rule the paragraph above each
  table states.
- **S5fix-M2** — `process-audit/audit_count.py:116-121`, the module docstring: still "what depends on it is `unknown`", with no
  word of *Refused rows* or `at least n`.
- **S6-M1** — `process-audit/audit_count.py:859-866` (`read_plan`): the count of slices is any one figure before the word
  `slices` (`- Plan: reviewed by 2 agents; slices: 8` reads 2); a figure written just before the word would be tighter.
- **S6-M2** — `process-audit/audit_count.py:840-846` (`read_contradiction`): any text holding "open design choice" is `yes`,
  a negation not opening with `none` included; an old-form record with both items `none` whose slice review blocked on a
  foundation entry reads `no` (no such record in the archive).
- **S6-M3** — `process-audit/audit_count.py:1677-1690` (`too_large_of`): Q2 answers `no` on part of a version's plans, with
  `k of m` the only sign of the partial basis.
- **S6-M4** — `process-audit/audit_count.py:113-114`, the docstring's list of git commands omits `diff` (`Ancestry.changed`).

## Declined to judge

- The figures of `process-audit/price_list.md` against the providers' pages: I cannot reach the pages. I checked only that every
  figure, address and date equals `reports/prices_fetched.md` (the orchestrator's choice (5): read by a fetching agent on
  2026-11-11; unverified by me).
- Older archived records of the-way's public history that carry absolute paths in their header lines (slice-3 review): history
  before this task; the command copies none of that text into its result.
- The run time of `remarks_check.HEADING` on a crafted line (correction review): `task-cycle/remarks_check.py` is not changed by
  this task.
- Whether later orchestrators name the findings file in both messages of each round, as `task-cycle/skill/SKILL.md:165-168` now
  asks: the use of the rule in later cycles, not this change's code.

## The orchestrator's choices to judge

1. `cycle_stages.py` not a trust boundary — not accepted: B4.
2. Repositories by keys and their entry `repository`; `problem_register` and `audit_results` under `the-way`; `--locations`;
   the-way's own cycle versioned by its *Target branch and base* — accepted. They follow WAY-320 (keys are repository names; the
   default is the fixed file, the option a test hook, no environment variable) and the register's *Repository* column; the base
   is the commit the worktree started from, the process the cycle read.
3. A findings file named by at least two turns — accepted as a lower bound in the safe direction; the missing upper bound is
   Corr-M1.
4. The conservative series rule — the computation accepted; its account in the skill and the result is B5.
5. The prices — not verifiable by me (Declined to judge, first line).

The gaps carried from *Unread material*: slice 7's executor did not read `audit_count.py:600-1560`. I read the file whole and
compared the skill with it: sections, their order, columns, `at least n`, `—` in *Days waiting*, options, exit codes, entry
names, file names and the reasons for `unknown` in matter 1 agree with the code; the mismatches are m2, m3, B3 and B5. Slice 2's
partial read of WAY-148 and the foundation writer's partial reads of WAY-140, WAY-134, WAY-135, WAY-161: I read WAY-140 whole
(nothing in the change performs a human action: no scheduler call, no backlog write; the skill names both as the human's,
`process-audit/SKILL.md:31-32`); WAY-148, WAY-134, WAY-135 and WAY-161 bear on the stage reports and the spec, not on what the
change does, and I read them by title only.

## Coverage of the task

- *To do* 1: part `process-audit`, directory, part-map entry, WAY-09 changed (list, sentence of contents, *Scope*,
  *Verification*, *Rationale*) — met. WAY-328's *Scope* gains `process-audit`, as its rule for a new part asks.
- *To do* 2: template — every field per problem (record by repository and commit, stages, class, weight, issue; fate and fix on
  the issue), the seven starting classes, the four weights, the user adapts it — met.
- *To do* 3: per cycle — version, remarks, problems by class and weight once each, cost, share — met in code; the two times — in
  code, but always `unknown` in practice (B1); the share is lost on ordinary prose (B2). Per fixed issue, per open issue (m3 on
  the header), per process version (median, Q1–Q3) — met.
- *To do* 4: dated price list; a new list, a change of the list of classes or of the reviewed files starts a series; no direct
  comparison across series — met in code; its account, B5.
- *To do* 5: the skill — reads the count, shows matters with no priority from frequency, writes the result outside every
  repository — met; the widening of the list of classes it misses is B3.
- *To do* 6: entries under `the-way`, found as the backlog is, the human asked where missing — met (command: `Error:` and exit
  2; skill: step 1 with `project-level/backlog_place.md`).
- *To do* 7: `stages.md` gives the wait for tools apart, a subagent call is the subagent's work — met in form; B1.
- *To do* 8: unattended run — met (`--help`, stdin closed, no prompt; scratch run with `< /dev/null`, exit 0).
- *Settlements to record* 1–12: WAY-329 to WAY-340, one each; their wording agrees with the rows and their quoted sources, and
  *Rejected* holds only ways the sources keep. Row 4 is met in the entry and missed in the skill (B3).
- *Human actions*: both stay with the human; the skill names them and does neither.
- *Out of scope* (the private nightly review): untouched.
- Nothing added that nobody asked for beyond small, stated choices (the *External context* row, `--today`, the note's *Not
  reached*, the reading of the newest earlier note); none is a finding.
- The target branch's rules and this change: the one sentence added to `task-cycle/skill/SKILL.md:165-168` sits in the passage
  that WAY-148's routing rule governs and is a stated exception to it; `task-cycle/record_template.md:52-62` (*Review rounds*)
  agrees with the *Slices* section and with `audit_count.py`'s reader; no other file of `task-cycle/` or `project-level/`
  parses *Review rounds* (search below). WAY-327 bears on the request's description, not on these files.

## Checks run

| Command | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` (reviewed worktree) | 0 | `a5ebc881f3226408d76783424287f3f9dcaf7fc0` |
| `git diff --stat 52f8164..HEAD`; `git log --oneline 52f8164..HEAD`; `git diff 52f8164..HEAD` of `foundations/`, `README.md`, `task-cycle/` and the entry points (read whole) | 0 | 58 files, 21 commits |
| `git worktree add --detach <scratchpad>\rvw a5ebc88` | 0 | detached worktree of the head; removed at the end (`git worktree remove`, exit 0) |
| `python -B gate/run_tests.py process-audit` (detached worktree, background) | 0 | 94 tests OK, 106 s |
| `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` (detached worktree) | 0 | 41 tests OK |
| `python -B elements/common/foundation_check.py` (detached worktree) | 0 | 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (detached worktree) | 0 | 282 files, 0 listed |
| `python -B gate/run_tests.py elements/part-map` (detached worktree) | 0 | 39 tests OK |
| `python -B gate/run_tests.py agent-instructions` (detached worktree) | 0 | 18 tests OK |
| `python -B agent-instructions/skill_entry_points.py` (reviewed worktree, reads only) | 0 | `entry points are current` |
| `python -B process-audit/audit_count.py --locations <temporary> --today 2026-11-11 < /dev/null`, the-way's history as `repository` under `the-way`, the template as the register (scratch p2) | 0 | 72 cycles, 20 series, 130,611 bytes, 12.3 s; 0 doubled *Record* among the cycles; this cycle's copy `4c906d7`: cost 19.405272, both times `unknown` (B1) |
| the same on a temporary repository with one commit adding two records and one register row (scratch p1) | 0 | the problem shown under both cycles (m1) |
| `files_named` on five texts (scratch, `python -B -I -c`) | 0 | a path before a full stop gives `[]` (B2) |
| `git show 4c906d7:docs/task-cycles/weekly-process-audit/stages.md` | 0 | the warning of one call with no readable result (B1) |
| `git grep` of `4c906d7` for drive paths and note links | 0 | none |
| a search of the local transcripts for `server_tool_use` blocks | 0 | only usage counters, no block type the reader would refuse |
| `git status --short` (reviewed worktree, at the end) | 0 | empty |

Not run: the full suite (the cycle's own run, WAY-160); the installation tests (no installer file changed; slice 7 ran them);
a check of the providers' price pages (unreachable for me).

## Reaches beyond the dispatch

- `foundations/part_map.md` whole, `foundations/invariants.md:1-175` and the *Part* lines of the rest, `foundations/glossary.md`
  headings — my own selection by "Reading the foundation".
- `project-level/backlog_place.md` whole — the skill's step 1 sends the session there.
- `task-cycle/skill/SKILL.md:140-184` and the lines naming `cycle_stages` (`:326-334`, `:436-444`),
  `task-cycle/skill/blocked_finding.md:7-15`, `task-cycle/skill/reserved_return.md:49-57` — to see when `stages.md` is
  written (B1).
- `task-cycle/record_template.md` whole — the forms the audit reads.
- `git show 4c906d7` (the record copy committed mid-cycle) — this cycle's real `stages.md` (B1) and a check for paths.
- Local transcripts under `~/.claude/projects/` — block types only (no content quoted), for the reader of tool calls.
- `git log -S "Searches not found or unclear" -- task-cycle` — where WAY-260's report section lives, for B5's judgment.

## Unread material

- Decisions of my selection (*Scope* naming `process-audit`, `task-cycle`, `part-map`, `decisions`, `agent-instructions` or
  `repository`): 182. **Read whole: 26** — WAY-09, WAY-38, WAY-44, WAY-45, WAY-48, WAY-49, WAY-140, WAY-263, WAY-320, WAY-327,
  WAY-328, WAY-329 to WAY-340; WAY-89 and WAY-103 read in their changed *Scope* and binding sentences only (counted by title).
  **By title only: 156.** None of these points by its title to a bearing beyond the ones read: they concern the forms of
  foundation entries, technology, guidelines, requests, project plans and the cycle's stages, which the change does not alter.
- `process-audit/test_audit_count.py`: read by its test names and lines 660-799 (the cost tests); I ran it. `task-cycle/test_cycle_stages.py`:
  read by search; I ran it.
- `task-cycle/cycle_stages.py`: read in the diff of the range and the functions it calls; not whole.
- The reports of the slices with a review of their own (slices 3–6 and the correction, executors' reports): not read; their
  reviews were.
- `plan.md`, `task.md`, the handoff, the reports of the foundation entries and of slices 1, 2 and 7, and the eight review
  reports: read whole.

## Searches not found or unclear

- A step of the process that writes `stages.md` after the orchestrator's session has ended (so that no call is in flight): none
  found; step 12 and its variants run it live.
- A file other than `audit_count.py` that parses the item *Review rounds*: none (search of the worktree outside `.runs/`).
- A decision or file that names who widens the list of classes in practice: WAY-332 says the audit; the template names no
  actor; the skill none.
- A test of `files_named` with a path before a full stop: none.
- Whether the copy of the record committed mid-cycle (`4c906d7`) and its removal (`e4085bf`), now in the branch's history, are
  meant to stay there: unclear; the copy holds no path or note link.
