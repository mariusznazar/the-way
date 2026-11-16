# Author fix report — ci-replaces-local-final-gate

**Status:** done

Reviewed head `b64608400f4fb55bb5508f71e2c4c2aadbcd6a60`. The fix's range: `b646084..1b03ef7`, two commits, not pushed:

- `33c98c2` — the move for WAY-365 (I-4): the pricing of stage rows out of `process-audit/audit_count.py` into `process-audit/stage_pricing.py`, no change of behaviour.
- `1b03ef7` — the other findings (I-1, I-2, I-3, M-1, M-3; M-2 in this report): `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/skill/request_template.md`, `process-audit/test_audit_count.py`.

## Findings, one by one

**I-4 — fixed, `33c98c2`.** Moved: `ModelPrice`, `Prices`, `StageTokens`, `is_orchestrator_row`, `priced`, `cost_at`, `priced_older` and the five constants they use (`UNKNOWN`, `NO_MODEL`, `ORCHESTRATOR`, `MILLION`, `TEXT_CAP`) into `process-audit/stage_pricing.py` (149 lines, nothing runs at import). `audit_count.py` imports the names it still uses (`NO_MODEL`, `TEXT_CAP`, `UNKNOWN`, `ModelPrice`, `Prices`, `StageTokens`, `is_orchestrator_row`, `priced`, `priced_older`) and drops its definitions: 3316 to 3178 lines. The test that builds a copy of the script lists the new module (`test_audit_count.py`, test `test_the_way_without_a_repository_entry_is_this_checkout`). Why this part: it is pure calculation over parsed rows, it reads no file and no git, so it needs no entry in the part map's trust boundary, and it lies in lines the branch `task/audit-answers-contradiction-after-code` (commit `6867078`) does not move (that commit moves the reading of the items *Discarded attempt* and *Review rounds*, and its helpers). Same-line contacts with that branch remain and are trivial to resolve: the import block at the top of `audit_count.py` (I put mine before `sys.path.insert`, three lines from theirs), the lines `NO_MODEL`/`ORCHESTRATOR`, which stand directly before the block that branch deletes, and the tuple of file names in the test `test_the_way_without_a_repository_entry_is_this_checkout`, which both branches edit. I found no part that avoids all three: any new module needs the import and the test's tuple, and the pricing constants stand beside their block. The move commit stands on top of the reviewed commits, not first; the ruling allowed either, and reordering would have rewritten the commits the review judged. A check that nothing else changed: `python -B gate/run_tests.py process-audit` before the move 235 tests OK, after the move 235 tests OK (exit 0 both); ruff on the two files gives only the four reports the base file already gave (RUF059 once, UP037 three times; the base file measured the same way) and no `F401`. One `F401` that the move first caused (`ORCHESTRATOR` imported and unused) I removed before committing the move. The working copy of the script that did the cutting stands in `reports/author-fix-move.py`.

**I-1 — fixed, `1b03ef7`.** Step 10 of `task-cycle/skill/SKILL.md` now has the orchestrator write into *Verification* of the record, before the copy of step 12 is made, a row that says the final gate is the CI run on the request's last head, that the cycle has no local time of it and that its result stands in *Checks* of the request's description. The committed copy therefore holds that row. Step 4 now reads: where the merged copy's *Verification* says the final gate ran in CI, the copy holds no result, so take the list of failing tests from the *Checks* of the merged request's description (its address is in the copy's *Request URL and status*), read through the host's tool; a green run gives an empty list; where no request can be read, step 4's existing fallback applies (run the checks on the base). Step 12 now has the description's *Checks* name, for a red run, the tests that failed, read from the run's log (the review noted that "each check by name" gives only the two jobs). The same is in `task-cycle/record_template.md` (the *Verification* paragraph) and `task-cycle/skill/request_template.md` (*Checks*: the list of failing tests may come from the earlier request; a red run's failed tests). Test: none quotes these sentences (prose of a skill is not tested, `guidelines/testing.md`); `test_request_check.py` and the request check tests passed (task-cycle 534 tests OK).

**I-2 — fixed in part, `1b03ef7`; the rest cannot be done, as the ruling allows.**
- Fixed: the statement "the final gate ran in CI" now stands in the copy that the audit reads (the row of step 10, above), so the audit's pointer "(the record's *Verification* says which)" leads to a record that answers it. `process-audit/SKILL.md` and the audit's messages need no further change.
- Not possible: the time of a fallback local run (step 12, CI gave no result in 30 minutes). It is made after the copy's pair of commits, and repeating the pair would push a new head, which would start the CI run again and turn the fallback into a loop. So its time reaches the original's `gate_times.md` and no copy. What the audit then shows: for that cycle the copy holds `gate_times.md` only if the run of step 2 or 4 wrote it, and it holds only those runs; the fallback run is missing from the gate times, and the copy's *Verification* row says that the final gate is CI. The text of step 10 and of `record_template.md` now says so.

**I-3 — fixed, `1b03ef7`.** WAY-160's first paragraph now reads "where CI runs on no request, or the request is left blocked for unfinished code, the orchestrator runs the gate itself on the tree that goes into it, save where that tree is one already run" (the exception covers the request blocked for a reserved choice, whose tree is the base or the commit that moved the pin, whose runs stand, as `reserved_return.md` says). Its *Verification* (complies) gained "a request blocked for a remaining blocking finding says ... not waited for, and the orchestrator ran the gate on the code the request holds". The second paragraph keeps the statement about the description of such a request. I also added, in the second paragraph, one sentence that where CI is the final gate the cycle's record says so before it is copied and names the request that gives the result, and a clause for that in *Verification*, since I-1's fix is a rule the decision should hold (WAY-263); this makes WAY-160 a "the cycle's" part (see Choices).

**M-1 — fixed, `1b03ef7`.** `process-audit/test_audit_count.py`: a comment before the two assertions names the task's row 6 as their source.

**M-2 — done as far as the repository allows.** I did not edit `foundations/environment_facts.md` (`foundations-branch-ruleset`): its source, the ruleset, still says one required check until the human adds the second, so editing it now would state what the source does not. The request-ready text of the human action, to be used in the request's description (English; the document's Polish follows):

> Needed from you: in the ruleset `foundations_tests` of the repository the-way add the required status check `tests-windows` (GitHub Actions) beside `tests`, keeping the bypass for the owner. GitHub offers `tests-windows` for selection only after it has run once, so do it after the first CI run on this request. The name of the Linux check stays `tests`. After you have done it, one fact of the foundation is out of date: `foundations-branch-ruleset` in the environment facts says that the ruleset requires one check, `tests`; read the ruleset again with the two `gh api` commands that the fact holds, and correct the fact in a correction of this request (the decision on CI, WAY-16, rests on that fact).
>
> Do zrobienia przez Ciebie: w regule gałęzi `foundations_tests` repozytorium the-way dodaj wymagane sprawdzenie `tests-windows` (GitHub Actions) obok `tests`, z prawem obejścia dla właściciela. GitHub pokaże `tests-windows` do wyboru dopiero po pierwszym przebiegu, więc zrób to po pierwszym przebiegu CI na tej prośbie. Nazwa sprawdzenia na Linuksie zostaje `tests`. Po tym jednym fakt fundamentu staje się nieaktualny: `foundations-branch-ruleset` w faktach o środowisku mówi, że reguła wymaga jednego sprawdzenia, `tests`; odczytaj regułę ponownie dwoma poleceniami `gh api`, które fakt zawiera, i popraw fakt w korekcie tej prośby (decyzja o CI, WAY-16, na nim stoi).

**M-3 — fixed, `1b03ef7`.** WAY-16 *Rejected*: the two added ways are now written in general terms ("the tests that need the other system run nowhere, and an error that shows only on that system shows only in use"; "CI on one system and, on the machine of the work, only the directories of tests that need the other system"), with the-way's case, the installer's junctions on Windows, as a parenthesis.

## Checks (command, exit code)

| Check | Exit code |
|---|---|
| `python -B gate/run_tests.py process-audit` after the move (235 tests) | 0 |
| `python -B gate/run_tests.py agent-instructions` after the move (37 tests, 2 expected failures as before) | 0 |
| `ruff check --config ruff.toml --no-cache` on `process-audit/stage_pricing.py` and `process-audit/audit_count.py` (the installed Ruff of the main checkout) | 1 — the four reports the base file gives, none new; a first run showed `F401` on `ORCHESTRATOR`, removed before the commit |
| `python -B elements/common/foundation_check.py` on the final tree | 0 (`0 errors`) |
| `python -B gate/run_tests.py task-cycle` on the final tree (534 tests, 1 skipped) | 0 |
| `python -B gate/run_tests.py process-audit` on the final tree (235 tests) | 0 |

The full gate was not run.

## Own-work check (WAY-164)

Requirement most likely not met: no cycle after a CI-gated cycle runs a full local gate on its base for lack of a list (I-1), and the audit's pointer leads to a record that says the final gate ran in CI (I-2). Check: a trace through the text, since the files are prose that no test holds: the row written at step 10 (`SKILL.md`, "write into the record's *Verification* now"), the copy that holds it (`record_template.md`, "The committed copy holds the row of step 10"), and step 4's reading of that row (`SKILL.md`, "Where that *Verification* says that the final gate ran in CI") each stand once, and the field step 4 reads the address from, *Request URL and status*, stands in the record template (line 204). It showed the chain closed in the text. What it did not show: that an orchestrator following it can read the merged request's *Checks* through the host's tool (needs GitHub; step 4's fallback covers a failure); and that the merged description holds the failing tests of a red run (the rule is now in step 12 and the template, nothing checks it).

## Choices (with the way rejected and its cost if wrong)

1. **The source of step 4's list where the final gate was CI: the merged request's *Checks*.** The task's sources give none. Rejected: (a) a repeat of the record's pair of commits after the CI run to bring the result into the copy — it pushes a new head and starts CI again, a loop; (b) the CI run read by a command of the host (`gh run view`) from the merged head — needs a commit-to-run lookup and the log, the description already holds the result; (c) always running the base gate when the previous final gate was CI — the very thing the finding forbids. Cost if wrong: a merged request whose description cannot be read, or lacks the failing tests, sends the next cycle to the existing fallback (a local base run), no wrong pass; a wrong reading would put a wrong list into *Verification*, which a failing check outside the list exposes at step 10/12.
2. **The move commit stands after the reviewed commits**, not first. Rejected: rebuilding the three commits on top of a first move commit — it rewrites the commits the review judged, and the orchestrator's records name them. Cost if wrong: a reviewer who reads WAY-365 as "the first commit that changes the code" finds the order off; the content is the same.
3. **The new module holds five constants** the moved code uses, defined there and imported back, rather than copies in two files. Cost if wrong: `NO_MODEL`/`ORCHESTRATOR` lines meet the other branch's deletion at merge.
4. **WAY-160 gained a sentence about the record that names where the result stands** (not only the I-3 clause), since step 4's reading of it is a rule that a later change could drop. This part is not a row of the task and not a projected entry: it is marked `the cycle's` for the request's list of entries the human did not see: "Where CI is the final gate, the cycle's record says so before it is copied and names the request whose description gives the result, so that the next cycle takes the list of failing tests from there." Cost if wrong: the human rejects the sentence; the skill text stays true without it.

## Foundation entries written or changed in this round

- `WAY-160` — I-3 clause (row 1 and 2 meaning, extended to the blocked request) and the sentence in choice 4 (`the cycle's`); *Verification* complies lines updated. EN: where CI runs on no request or the request is blocked for unfinished code, the orchestrator runs the gate itself; where CI is the final gate, the record says so before it is copied and names the request whose description gives the result. PL: gdy CI nie biegnie na prośbie albo prośba jest zablokowana na niedokończonym kodzie, bramkę uruchamia sam orkiestrator; gdy końcową bramką jest CI, zapis mówi o tym przed skopiowaniem i wskazuje prośbę, której opis podaje wynik.
- `WAY-16` — *Rejected* only (M-3); no meaning changed.

## Reaches beyond the handoff

- `task-cycle/skill/reserved_return.md` read again to word the exception of I-3's clause; `task-cycle/record_template.md` line 204 for the field *Request URL and status*; `guidelines/coding-shared-module.md` (the kind of the new module; it names only `relation-model`, so none applies to `process-audit` and the invariant `shared-module-import-runs-nothing` does not reach it); ruff in ``.runs/quality-venv` of the main checkout` to see the reports.

## Unread material

- The reviewer's full report `reports/review-whole-report.md`: not read; the findings file sufficed.
- I did not open `foundations/part_map.md` (no file entered a trust boundary, and `process-audit/**` covers the new module).
- Everything the handoff names was read: the handoff, the findings file, `fix.md`.

## Searches not found or unclear

- No place in the task or the foundation gives the source of the failing-tests list when the merged cycle's final gate was CI; I chose one (choice 1).
- The ruling on I-4 asks for a part whose lines the other branch does not move and no same-line conflict at merge; I found none without a conflict in the import block and the test's tuple (the report of I-4).
- I could not tell from the handoff whether the move should stand first; I chose after (choice 2).

## Working copies

`.runs/author-fix/` held the logs of the runs, the cutting script `move.py` and a copy of the base `audit_count.py` made to compare ruff reports; the script was copied to `reports/author-fix-move.py`, the directory removed. Nothing remains.
