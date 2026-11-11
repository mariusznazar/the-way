# Report — the return step (`make-change`, return step of the planned route)

**Status:** done with concerns

Range: `51cae12..b36014a`, branch `task/weekly-process-audit`, worktree `.runs/worktrees/weekly-process-audit`.

## Commits and files

| Commit | What |
|---|---|
| `b36014a` | Carry the audit's code back into its decisions: WAY-332 (*Verification*), WAY-336 (*Rejected*, one term), WAY-337 (binding sentences, *Scope*, *Verification*, *Rationale*), WAY-341 and WAY-342 (new) |

| File | + | − |
|---|---|---|
| `foundations/decisions.md` | 83 | 13 |

No code, test, part-map, glossary or environment-facts file changed.

## Entries written or changed

| Entry | Mark | Meaning (English) | Znaczenie (po polsku) |
|---|---|---|---|
| WAY-332 (changed: *Verification* only) | row 4 | Each problem has a weight of four levels and a class from a list the template starts and the audit widens; the count refuses a problem whose class the list lacks until a session of the audit, on the human's yes, adds that class to the register's list. | Każdy problem ma wagę w czterech poziomach i klasę z listy, którą zaczyna szablon, a poszerza audyt; liczenie odrzuca problem z klasą spoza listy, dopóki sesja audytu, za zgodą człowieka, nie dopisze tej klasy do listy w rejestrze. |
| WAY-336 (changed: two uses of "the stage report" in *Rejected* become "the report of a cycle's stages") | row 8 (the tie by the findings file as the correction wrote it; meaning unchanged by this step) | A cycle's cost is its cost at constant prices from a dated list and the share of it spent in fix rounds, a turn tied to its round by the findings file its message names; unknown where the tie fails. | Koszt cyklu to koszt w stałych cenach z cennika z datą i udział rund poprawek, a turę wiąże z rundą plik uwag nazwany w jej wiadomości; tam, gdzie powiązania brak — wartość nieznana. |
| WAY-337 (changed: binding sentences, *Scope* gains `task-cycle`, *Verification*, *Rationale*) | the cycle's (row 9, with *To do* 7 and the plan's choice that the working time excludes the wait for tools) | A cycle's time is the agents' working time with neither the wait for the human nor the wait for tools in it, and apart the wait for tools from each tool call to its result; a call that starts a subagent, sends it a message or waits for it is the subagent's work, not a wait. | Czas cyklu to czas pracy agentów bez czekania na człowieka i bez czekania na narzędzia, a osobno czas czekania na narzędzia od wywołania do wyniku; wywołanie, które uruchamia podagenta, pisze do niego albo na niego czeka, to praca podagenta, a nie czekanie. |
| WAY-341 (new) | the cycle's | The audit reads `problem_register` and `audit_results` under `the-way`, and `repository` under the key of each repository whose cycles it reads — every key that holds one unless the user names the keys; the-way's checkout is `repository` under `the-way`, or else the checkout that holds the counting command run. | Audyt czyta z pliku lokalizacji wpisy `problem_register` i `audit_results` pod `the-way` oraz `repository` pod kluczem każdego repozytorium, którego cykle czyta — każdy taki klucz, chyba że użytkownik wskaże, które; checkout the way to `repository` pod `the-way`, a gdy go brak — checkout, w którym leży uruchomione polecenie. |
| WAY-342 (new) | the cycle's | A cycle of the-way itself, whose record pins no commit, ran on the commit its task branch started from, which the record's *Target branch and base* names; a record that names neither leaves the cycle with no known version. | Cykl samego the way, którego zapis nie przypina commita, działał na wersji z commita, od którego wyszła jego gałąź zadania (linia *Target branch and base*); zapis bez żadnego z nich zostawia cykl bez znanej wersji. |

For WAY-337, WAY-341 and WAY-342 the request's section for the human's decisions carries the meaning (WAY-114): no row carries them whole. WAY-341 *Rejected* reads `unknown`: the cycle's record keeps no way weighed against the entries (Q10 names only "each executor choosing its own"). WAY-342 *Rejected* is Q6's "`unknown` for every cycle of the-way".

## Foundation compared with code

Compared with the files at `51cae12`: WAY-329…WAY-340, WAY-09, the *Scope* of WAY-38, WAY-89, WAY-320 and WAY-328; the task's *Decisions in play* (WAY-09, WAY-103, WAY-140, WAY-260, WAY-296, WAY-320); the part map of `process-audit` and `task-cycle` (*Files*, *Depends on*, *Trust boundary*, *External context*); and what the search of the foundation found — WAY-11, WAY-27, WAY-33, WAY-34, WAY-36, WAY-44, WAY-48, WAY-49, WAY-107, WAY-114, WAY-161, WAY-294, the invariants of *Part* `every` (`repository-file-location`, `tracked-file-private-paths`, `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`), the glossary.

What no longer matched, and its correction:

1. **The class list widened by the skill (WAY-332).** Its *violates* read "the audit refuses a problem for a class the list lacks instead of widening the list", which is what the count does (`process-audit/audit_count.py`, reason "the class is not in the list of classes") before the session widens the list (`process-audit/SKILL.md:149-159`). The binding sentence held; the examples now name the count's refusal, the session's new class on the human's yes, and as violations the nearest class given or a refused row left with no class put before the human.
2. **The wait for tools (WAY-337).** The decision left open whether the working time holds the wait for tools, and held no rule for a subagent call; `task-cycle/cycle_stages.py` gives the working time without the wait and counts the calls `Agent`, `Task`, `SendMessage`, `spawn_agent`, `wait_agent`, `send_message`, `followup_task` as no wait, as *To do* 7 asks ("wywołanie podagenta nie jest czekaniem na narzędzie, liczy się jako praca podagenta"). The decision now says both; its *Scope* gains `task-cycle`, the part whose script measures it, as WAY-336's does.
3. **"stage report" in two meanings (WAY-336).** WAY-260, WAY-294, WAY-325, WAY-326 and WAY-338 use it for the report a stage's agent writes; WAY-336's *Rejected* used it for `stages.md`, where "the record and the stage report write times in different forms and zones" is true of `stages.md` and not of an agent's report (WAY-99). The two uses now read "the report of a cycle's stages". No glossary entry: the term has one meaning left in the foundation.
4. **The trust boundary of `cycle_stages.py`.** Matches: `task-cycle` *Trust boundary* names it (`4c77187`), and *External context* marks session records untrusted. Nothing to change.
5. **The tie of a turn to its fix round by the findings file (WAY-336).** Matches the code (`task-cycle/skill/SKILL.md:165-168`, `task-cycle/record_template.md` *Review rounds*, the column *Files named*, `fix_rounds_share`): the share is `0.0%` only under `none`, unknown wherever a round is named by fewer than two turns or otherwise not tied. Nothing to change.
6. **The series rule (WAY-338).** The count splits at more changes than WAY-338 names — any change under `task-cycle/change|plan|review|spec` and of `task-cycle/cycle_stages.py` — so it compares less and never across a change WAY-338 names; that complies with the decision, which says what starts a series and forbids comparison across it. The skill and the result now say the count is wider (B5). Nothing to change in the decision; see *Findings* for a citation in the code.

Everything else matched: WAY-09 (the directory, its contents, *complies*), WAY-38/WAY-89 (standard library, git and Python only), WAY-320 and WAY-27 (no path in a tracked file; entries named), WAY-329 (no class or weight given by the audit), WAY-330, WAY-331 (results refused inside any repository read or the-way's checkout), WAY-333, WAY-334, WAY-339, WAY-340, WAY-103 ("the human", no name), WAY-140 (scheduler and weekly task left to the human), WAY-260/WAY-296 (remarks read through `remarks_check`), WAY-328 (*Scope* holds `process-audit`), and the part map (`process-audit` imports only `task-cycle/remarks_check.py` and its skill reads `project-level/backlog_place.md`, both in *Depends on*; `task-cycle` imports nothing of `process-audit`).

## The choices that bind after the merge

| Choice | Outcome |
|---|---|
| Entries of the locations file (`problem_register`, `audit_results`, `repository` under a product's key) | **WAY-341** (new). WAY-329 and WAY-331 say "an entry" without its name; the names bind every user's own file and both the skill and the command, and the entry `repository` is a checkout's path, a kind of entry WAY-320's sentence did not name (it does not exclude it, so WAY-320 is unchanged). |
| Version of the-way given to a cycle of its own history | **WAY-342** (new). WAY-334 judges by the version a cycle ran on; for the-way's own cycles, the bulk of what the audit reads today, the record pins none, and the reading binds the record's line *Target branch and base* (`task-cycle`). |
| Findings file as the tie of a turn to its round, with at least two turns | Stands in WAY-336: the message names the findings file, "which only the messages of that fix and of the review of that fix do", and the share is unknown "wherever the record and the stages cannot tie each round to the turns that served it" — a round named by fewer than two turns is such a case. |
| Form of `Review rounds` in the record | Stands in WAY-336 ("the cycle's record names each round by that path"); the exact form is the record template's (`task-cycle/record_template.md`), where form belongs. |
| Column *Files named* of the stage report | Stands in WAY-336 (the stages tie each round to its turns); the column is how `cycle_stages.py` carries the tie, described in its docstring. |
| Options of the counting command | No decision: how the command makes what WAY-340 and WAY-341 settle; the scheduled run takes no option, and the docstring and `process-audit/SKILL.md` step 2 give the options. Stays in the questions table (Q10). |
| Conservative series rule | No decision: a way of making WAY-338 that compares less and never across a change it names (above); later work may narrow it without contradicting a decision. Stays in the questions table (Q16 (2)), which the request puts to the human. |
| Reading of the *Plan* item (one figure just before `slices`) | No decision: how the count reads *To do* 3's second question from the record's *Plan* line. Stays in the questions table (Q16 (3)). |

## Environment facts: none

- **Price pages** (`process-audit/price_list.md`): no decision's *Based on* would name them. A changed page calls no decision into question — the list is a dated reading and a new list starts a new series (WAY-338), and the list itself carries each page's address and the date read. A fact stands only while a decision's *Based on* or an invariant's *Rests on* names it (WAY-73; `elements/environment-facts/template.md`, "Which facts are written").
- **Layout of the session files of Claude Code and Codex** (what `cycle_stages.py` reads): `foundations/environment_facts.md` holds no such fact (searched for `transcript`, `jsonl`, `rollout`). No decision rests on the layout: WAY-336 and WAY-337 settle what is measured; a changed layout makes the stage report warn and give `unknown`, which the decisions already allow, and calls neither into question. The script read the transcripts before this change with no fact either. So no fact is written, for the same rule.

## Glossary terms: none

- **"issue"** (sprawa): the field's meaning of the word — a tracked matter that several reports of one problem make, open, fixed or dropped — is the meaning the audit gives it, narrowed to the process. WAY-95's bar for a narrower meaning is a sentence a field reader would read wrongly: in WAY-329, WAY-335, `process-audit/SKILL.md` and `process-audit/problem_register.md` none does (the two files and WAY-329 define it in place; WAY-335 reads the same if "issue" is taken as the tracked problem). Its other use, `task-cycle/review/fix.md:24` ("An issue outside the fix diff is a Minor or out-of-scope note"), is the field's meaning, and no sentence of the files is true in one use and false in the other (WAY-99).
- **"series"**: the field's meaning (statistics) — a run of measurements of one basis, broken where the method of measuring changes, across which numbers are not compared directly — is the one WAY-338 and the skill use; no sentence reads wrongly for it.
- **"stage report"**: corrected in WAY-336 (above), no entry.

## Checks

| Command | Exit | Note |
|---|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` (after writing the entries) | 0 | `0 errors` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests, OK |
| `python -B gate/run_tests.py elements/decisions elements/glossary elements/invariants elements/environment-facts` | 2 | the runner takes one directory (`usage: run_tests.py [-h] [directory]`) |
| `python -B gate/run_tests.py elements/decisions` (and the same for `elements/glossary`, `elements/invariants`, `elements/environment-facts`) | 1 each | `no test found in …`: these directories hold no tests |
| `python -B gate/run_tests.py elements/common` (the tests of the foundation check, run in the background) | 0 | 144 tests, OK |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | 282 files, 0 listed |
| `python -B -m unittest test_audit_count.ProcessPin` (in `process-audit/`) | 0 | 7 tests, OK — the own-work check |

The full suite was not run (the cycle runs it).

## Own-work check

Requirement most likely not met: that the two new decisions say what the code does, since I wrote them from the docstring and the skill rather than from the tests. Check: the pin tests (`ProcessPin`, among them `test_a_cycle_of_the_way_itself_takes_the_commit_of_its_target_base` and `test_a_product_pin_naming_no_commit_is_unknown`) for WAY-342, exit 0; for WAY-341, `process-audit/audit_count.py:191-197` (the three entry names) and `process_pin`/the fallback to the script's checkout, and `process-audit/SKILL.md:66-73` (the skill reads the same three entries). Both decisions match. One wording I corrected before committing: WAY-341's first *violates* said "the counting takes the path of a checkout as an argument", which the option `--locations` (a path to the locations file) could be read against; it now names the repositories being named by their checkouts' paths.

## Findings (the code wrong, the decision right; not changed)

- **Minor** — `task-cycle/cycle_stages.py:64-66`: "The column *Files named* is a form of this report of its own: the reports that hold it start a series of the audit's measures apart from the earlier ones (WAY-338)." WAY-338's "stage report" is the report a stage's agent writes (its rationale: the rise of remarks after WAY-260); the series at a change of `cycle_stages.py` is the count's own wider rule (`process-audit/audit_count.py:91-95`), not WAY-338's. The same use of "stage report" for `stages.md` stands at `process-audit/audit_count.py:60` ("a stage whose usage the stage report could not read") and `:756-757` ("not of the form the stage report gives"). Direction: "the report of the cycle's stages", and cite the count's rule rather than WAY-338.
- **Minor** — WAY-335's *complies* and *To do* 3 ("liczbę cykli, w których problem wrócił") speak of the cycles in which an open issue's problem came back; the count gives "Cycles in which its problems stand" (`process-audit/audit_count.py`, renamed in `51cae12` for m3), the cycle where the problem first stood included, so the figure is the returns plus one wherever that first cycle is counted. I left WAY-335 as the task words it; whether the count or its header should give the returns is for the orchestrator to put before the human.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-11, WAY-27, WAY-30, WAY-33, WAY-34, WAY-36, WAY-37, WAY-44, WAY-48, WAY-49, WAY-95, WAY-96, WAY-97, WAY-99, WAY-107, WAY-114, WAY-294, WAY-295, WAY-321…WAY-327, read whole — the rules of the return step, the elements' rules and the search of the foundation.
- `elements/decisions/` (`template.md`, `examples.md`, `skill/SKILL.md`, `read.md`, `decide_entry.md`), `elements/environment-facts/` (`template.md` and the five skill files), `elements/common/rules.md`, `elements/common/way_of_working.md` steps 1–4 — the element skills the handoff names.
- `foundations/invariants.md:1-135`, the *Part* lines of the rest, `foundations/glossary.md:60-154` and its headings, the whole part map.
- `.runs/task-cycles/weekly-process-audit/cycle.md` (questions table, *Return step*), `reports/review_whole_findings.md`, `reports/whole_fix_report.md`, `reports/correction_handoff.md`, `reports/slice3_handoff.md:150-183` — for the choices and what the correction and the fix changed.
- `git log` of the archived records' *Return step* lines (to see how earlier return steps marked the cycle's entries), and `origin/task/backlog-line-for-plan-tasks:foundations/decisions.md` WAY-329 (a decision marked the cycle's, for its form).

## Unread material

- `elements/glossary/` template and skill files: not read. I wrote no glossary entry and decided against both words on WAY-95 and WAY-99, which I read whole; the element's skill would apply only to an entry written.
- `elements/decisions/examples.md` names WAY-03: not opened; the form was taken from the template and the neighbouring entries.
- `foundations/environment_facts.md`: read by its headings and a search, not each entry whole — enough to find that no fact covers transcripts or price pages.
- `process-audit/audit_count.py` and `task-cycle/cycle_stages.py`: read their docstrings, the constants and the passages named above, not whole; `process-audit/test_audit_count.py` only `ProcessPin`.
- The slice and review reports other than those named under the reaches: not read, as the handoff allows.

## Searches not found or unclear

- `python -B gate/run_tests.py elements/decisions elements/glossary elements/invariants elements/environment-facts`, as the handoff gives it, exits 2: the runner takes one directory, and none of the four holds a test. The tests of the foundation's form are in `elements/common` (`test_foundation_check.py`) and `elements/part-map`.
- Whether WAY-338's "stage report" covers `stages.md`: the orchestrator's correction handoff read it so ("This changes the form of the stage report, which starts a new series (WAY-338)"); the decision's rationale and every other decision read it as an agent's report. I took the latter (see *Findings*).

## Concerns

- The open branch `task/backlog-line-for-plan-tasks` writes its own WAY-329 (a decision marked the cycle's). Whichever request merges second renumbers; this one now holds WAY-329…WAY-342.
- WAY-337 now has `task-cycle` in its *Scope*, as WAY-336 already has; WAY-330's *violates* ("a decision of the audit names the part `task-cycle` as the one it governs") reads against a decision that names `task-cycle` in place of `process-audit`, not beside it, so neither breaks it — but every agent changing `task-cycle` will now read both.

## Questions

none

## Return step (for the cycle record)

- Foundation compared with code: WAY-329…WAY-340, WAY-09, the *Scope* of WAY-38, WAY-89, WAY-320, WAY-328, the task's *Decisions in play*, the part map of `process-audit` and `task-cycle`, and what the search found, compared at `51cae12`; WAY-332's examples (refusal and widening), WAY-337 (no wait for tools in the working time; a subagent call is no wait) and a use of "stage report" for `stages.md` in WAY-336 no longer matched and were corrected in `b36014a`; two Minor findings in the code returned (`reports/return_step_report.md`)
- Decisions written or changed: WAY-341, WAY-342 (new, the cycle's); WAY-337 (changed, the cycle's); WAY-332 (*Verification*, row 4); WAY-336 (*Rejected*, one term) — by the return step, `b36014a`
- Invariants written or changed: none
- Environment facts: none (no decision rests on the price pages or on the layout of the session files; a fact stands only while one does, WAY-73)
- Glossary terms: none ("issue" and "series" are used in their field's meaning, and no sentence reads wrongly, WAY-95; "stage report" used against its meaning corrected in WAY-336)
- Part-map changes: none by the return step (the map matched)
- Projected entries written whole or in part: none (the task carries none)
- Rows of *Settlements to record* written: none by the return step (rows 1–12 stand as WAY-329…WAY-340)
