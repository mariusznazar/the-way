# Assessment-settlement review and final invariant acceptance

Verdict: **WITH FIXES — one Important finding, R2.** The identity correction has no additional correctness finding in the reviewed range. The corrected evidence check is accepted on the recorded identity and freshness breaks. **The subprocess check is not accepted:** its final fixture does not exercise the owned-record path, and a reviewer-derived violation passes both tests. No Critical or Minor findings.

This is the affected code/check review within the existing single independent assessment, not another whole-branch review or assessment. It preserves the previous final-review report and the subsequent scoped UTF-8 correction review for unchanged material. This report does not authorize a PR, merge or cleanup.

## Range, authority and material actually read

Worktree: C:/Storage/repos/the-way-wt/lead-project; branch task/lead-project. Reviewed range:

`84cdc87cc12ce43526cb24a61640e39cf00e950a..114c68960670e31a878ff00fbdf9ed5c00689089`

Three commits: 9ae98fe0b8421c5b486785a462648f51f9c50f08 (foundation), a9e766d99672bf3c7693ebd4a5519e7fb8d30acf (independent evidence check), 114c68960670e31a878ff00fbdf9ed5c00689089 (reader/ordinary tests). Entire diff inspected: five paths, 493 additions and 40 deletions:

- foundations/decisions.md
- foundations/invariants.md
- project-level/test_plan_state_invariant.py
- project-level/plan_state.py
- project-level/test_plan_state.py

Necessary unchanged join inspected in full: project-level/test_plan_state_subprocesses_invariant.py at 2cadf14fd3d21a82f1adee322f1022002b194385. The complete current reader, complete independent evidence check, all ordinary-test changes and foundation changes were read. Current template fields and cycle return-step instructions were checked against their existing authority.

Read the complete identity-review handoff, assessment-settlement, assessment-identity-source-ruling, assessment-identity-foundation, identity-check, final identity-implementation and identity-membership-ruling reports. Retained the previous complete frozen-task/spec/plan readings and inspected current identity settlement additions and affected contracts. Existing review authority remains the worktree instructions/integration route, Superpowers requesting-code-review/template and final-review instructions, user code-review playbook and its delegated document-review playbook. Re-read current task-cycle step 11 and complete WAY-69/149 for the acceptance boundary. The original foundation author, independent check author, covered-code author and this reviewer remain separate; the human's authorship/foundation acceptance is not claimed by this report.

The broad initial report/JSONL read exceeded output limits; the full two foundation/check reports were recovered in a separate read, and JSONL was then parsed structurally. A combined spec-tail output also clipped a small unchanged passage; no finding or absence claim depends on that clipped passage. All five actual diff paths were inspected without relying on a truncated diff.

## Foundation selection and source fidelity

Refreshed complete Scope-field selection, including wrapped fields, for the actual project-level subject. It returns 40 entries, all /1:

WAY-09; WAY-106–124; WAY-126–127; WAY-134; WAY-137–140; WAY-142–147; WAY-150–156.

These entries were read whole in the retained final review, together with the full part map, applicable invariant entries, glossary and linked source-authority rules. A whole-entry comparison with 84cdc87 confirms only WAY-153 changes in this selected set; its complete current entry was read again. The previous broader 88-entry selection remains evidence for unchanged cross-part work rather than being represented as a new review. WAY-69 and WAY-149 were reread whole. The current evidence and subprocess entries were read whole, and their unchanged/changed meanings reconciled with WAY-153. Search across the entire foundation used:

```text
rg -n -i 'task.provenance|task.source|project.relation|task.identity|plan.local|no other task|cycle names its record|unique.*plan|WAY-153@|project-plan-state-evidence|state.reader' foundations
```

Positive controls found WAY-147's plan-local names, WAY-153's reader contract, both invariant references and the map's false-progress failure. Exactly the two incoming WAY-153 invariant references carry the new fingerprint. No new subject requiring another foundation entry was established by this affected review.

The correction preserves plan-local uniqueness. Existing record Task source/Task relation, retained task Project relation and the plan's Document cell establish ownership. It neither adds globally unique names nor requires a particular record basename or current/frozen text equality. The source ruling supersedes C13's path-only identity interpretation without changing the accepted task's scope. Same-source unsupported historical membership remains unchecked; explicitly different sources or supported explicit foreign plan/task relations are conflicts. The existing installed origin/HEAD integration contract and root's rejection of assessment observation 2 are preserved, not redefined here.

Current binding fingerprints independently recomputed with WAY-02 whitespace normalization:

| Binding text | Fingerprint | Final authority |
|---|---|---|
| WAY-153/1 | 9874911d | 9ae98fe0b8421c5b486785a462648f51f9c50f08 |
| project-plan-state-evidence/1 | d7b8cc0b | same foundation commit |
| project-plan-state-subprocesses/1 | a4d1867f | sentence unchanged from return-step foundation 4d705b597cb4634f1c58a056558635f63f9cd407; incoming relation refreshed at 9ae98fe |

## R2 — Important — new thread: subprocess check misses the verified-record path

**Do wklejenia**

[C:/Storage/repos/the-way-wt/lead-project/project-level/test_plan_state_subprocesses_invariant.py:106](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/test_plan_state_subprocesses_invariant.py#L106)

Po poprawce przypisywania cyklu do zadania ten test nadal zapisuje wyłącznie `# Cycle record`. Czytnik uznaje taki zapis za niezweryfikowany i pomija obsługę właściwego rekordu, w tym odczyt odnośników do PR. Dlatego oba testy procesów przechodzą także po dodaniu uruchomienia Pythona w `record_pointers`, choć reguła pozwala czytnikowi uruchamiać wyłącznie Git. Uzupełnij dodatni scenariusz o zapisane pochodzenie i zachowany dokument zadania oraz potwierdź, że odczyt rzeczywiście dochodzi do dowodu zakończenia i odnośnika z tego rekordu. Zachowaj kontrolę procesu i scenariusz błędu. Obecne sprawdzenie nie może zostać zaakceptowane na tej próbie naruszenia.

**Dlaczego to zgłaszam**

Odbiorca wyniku testów widzi zielone sprawdzenie „czytnik uruchamia wyłącznie Git”, mimo że dodatkowy program w zwykłej obsłudze poprawnego archiwum pozostaje niewykryty. Mechanizm wynika z konkretnego połączenia zmienionego kodu i niezmienionego sprawdzenia:

1. [test_plan_state_subprocesses_invariant.py:106](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/test_plan_state_subprocesses_invariant.py#L106) tworzy archiwum bez Task source, Task relation i zachowanego dokumentu zadania.
2. [plan_state.py:267](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/plan_state.py#L267) zwraca dla niego `unchecked`. [plan_state.py:311](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/plan_state.py#L311) pomija taki historyczny zapis przed wywołaniem `record_pointers`.
3. [test_plan_state_subprocesses_invariant.py:153](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/test_plan_state_subprocesses_invariant.py#L153) sprawdza kod 0, który zgodnie z kontraktem obejmuje również nieustalone obserwacje. Zmiana zdalnego refa dowodzi prawdziwego pobrania, lecz nie wejścia w obsługę zweryfikowanego rekordu.
4. W kopii dodałem do [plan_state.py:145](https://github.com/mariusznazar/the-way/blob/114c68960670e31a878ff00fbdf9ed5c00689089/project-level/plan_state.py#L145) wykonanie `subprocess.run([sys.executable, "-c", "pass"], check=True)`. Oba chronione testy nadal przeszły: 2 testy, exit 0. To narusza zdanie „Every subprocess the plan-state reader starts runs Git.” na legalnym dodatnim wejściu, bez awarii składni, importu ani konfiguracji.
5. Kontrola dodatnia zachowała dokładnie ten sam zmieniony czytnik i odziedziczoną metodę testu/audyt. Zmieniła tylko dane tymczasowego produktu: prawdziwe Task source/Task relation, tabelę Artifacts i zachowany dokument z prawidłową relacją do planu. Test wtedy wykrył `Non-Git reader subprocess` z `python.exe`, exit 1. Po przywróceniu czytnika ta sama kontrola przeszła, exit 0.

Pozostawienie tego stanu daje fałszywą ochronę przed przyszłym dodaniem programu obsługującego PR lub przetwarzającego zapis cyklu. Naprawa kosztuje uzupełnienie istniejącego dodatniego scenariusza i powtórzenie ograniczonej próby naruszenia; nie wymaga zmiany zdania, kodu produktu, nowego pola ani kolejnej oceny fundamentów. Autor sprawdzenia powinien poprawić dane niezależnie, zachować literalne oczekiwania i wykazać rzeczywiste przejście ścieżki zweryfikowanego rekordu. Ten raport nie wprowadza takiej poprawki do chronionego pliku.

Dowody: [undetected break](identity-review-subprocess-break.txt), [owned-fixture positive control](identity-review-subprocess-owned-control-break.txt), [restored control](identity-review-subprocess-owned-control-clean.txt).

## Product evidence inspected before deliberate breaks

Read the executor's final logs and parsed the exact shared Method record before introducing mutations:

- `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`: executor exit 0, 250 tests in 108.425s, OK; final log identity-implementation-project-level.txt. JSONL has 141 invariant-attributed records, all pass; specifically 27 evidence checks and 2 subprocess checks pass. The 141 rows are not misreported as the full 250-test suite.
- `python -B gate/run_tests.py gate`: executor exit 0, 98 tests in 27.160s, OK; identity-implementation-gate.txt.
- Superseded broad runs were explicitly excluded. Other three part suites have unchanged product inputs since 84cdc87; this affected review did not repeat them or either broad green suite.
- Read final original acceptance output/JSON and final executor report. Exit 0; original whole plan task 3 produces both transitions; archived record commit c9644b21ec1d8124937d7e7ac7c8f6c49c6a79d9 matches the original Document and frozen membership. Record PR #12 association and reachability from merge commit 668baa091a8d89caceeeb070342f3aa3f506e109 are retained separately outside the Git-only reader. Original plan/definition hashes and original repository HEAD/status are unchanged and match the original baseline. Output was collected under PYTHONIOENCODING=cp1252 with the reader's UTF-8 override. No private source paths are reproduced here.
- Tasks 1/2 remain explicitly unchecked for documented unsupported/missing membership representations. This is a disclosed limit, not fabricated progress or a replacement for task 3 acceptance.

The positive product runs establish the pre-break baseline. They do not negate R2 or constitute check acceptance by themselves.

## Reviewer-derived breaks, execution and restoration

All mutations were confined to `.runs/task-cycles/lead-project/identity-review-source-breaks/`, outside archived reports. Copies of project-level and relation-model Python files supply the real local dependency layout. The real reader and both protected checks were never written. Test fixtures create their own temporary Git products; no source product or private plan is mutated.

Exact orchestration is retained outside reports in identity-review-breaks.py and identity-review-process-control.py; the semantic commands and changes are recorded here so source copies/scripts need not be archived. Each source replacement asserts its unique original anchor in the first runner. Each mutation restores reader bytes in a `finally` block.

Commands below ran from the copied project-level directory, using the current Python executable with `-B`. Full command vectors/exits are in identity-review-break-results.json and identity-review-process-control.json.

### Evidence identity boundary

Derived from the final sentence's requirement to establish ownership before proposing progress. In copied `provenance`, insert before its normal implementation:

```python
return "owned", list(paths), []
```

Run:

```text
python -B -m unittest -v test_plan_state_invariant.PlanStateEvidence.test_other_plans_integrated_same_name_cannot_complete_current_task
```

Exit 1, one test in 1.646s. Assertion failed because reader returned 0 instead of conflict 1; actual output proposed `in cycle -> done` from the other plan's integrated same-named record. This is the targeted false completion, not a setup failure. Full output: identity-review-identity-break.txt. Copied reader restored immediately.

### Fresh integration and composed transitions

Derived from the final sentence's freshly fetched integration requirement and two-transition obligation. Replace only the existing `git.run("fetch", "--no-tags", "origin", "+refs/heads/*:refs/remotes/origin/*")` call with `pass`, retaining remote verification and stale ref resolution.

```text
python -B -m unittest -v test_plan_state_invariant.PlanStateEvidence.test_fresh_remote_record_composes_both_transitions
```

Exit 1, one test in 1.606s. The publisher has new identity-bearing integrated evidence while the observer retains its stale ref. Assertion reports both required proposal rows absent; output shows the stale integration and no sufficient trace. This catches the actual loss of fresh evidence/composed transitions. Full output: identity-review-freshness-break.txt. Copied reader restored immediately.

### Every subprocess runs Git

Derived from the complete final sentence, including the successful owned-record path. Insert immediately before the Git grep in `record_pointers`:

```python
subprocess.run([sys.executable, "-c", "pass"], check=True)
```

```text
python -B -m unittest -v test_plan_state_subprocesses_invariant
```

**Exit 0, two tests in 3.153s: undetected break.** Both the success and error scenarios pass. Full output: identity-review-subprocess-break.txt. The reader copy was restored before clean verification. This result creates R2; no alternative easier break was substituted to obtain acceptance.

The independent positive control uses a disposable subclass of the existing subprocess fixture. After its original setup it writes CYCLE_RECORD with the original temporary task source and accepted-task.md, writes the literal TASK, commits those files in the temporary publisher, updates `self.delivered`, and pushes to that temporary local remote. It invokes only the inherited `test_successful_evidence_read_starts_only_git`, preserving its original audit and assertions. Running the same mutation then yields exit 1, one test in 3.055s, explicitly on `python.exe` versus allowed Git executables. Running the same control after byte restoration yields exit 0, one test in 2.656s. No protected test file was edited even in the copy; the subclass is a separate reviewer control, not a proposed replacement check.

No discarded setup, syntax or import attempts occurred in these break runs. Raw diagnostics contain only synthetic temporary fixture paths and the local interpreter, not private product documents.

### Clean final verification

After restoring the original reader bytes, the combined focused command ran the identity case, freshness case and complete protected subprocess module: exit 0, four tests in 7.109s. Full output: identity-review-restored-clean.txt. The owned positive-control clean run also passed as above. Reader-copy bytes equal the actual current product reader; both copied protected checks equal actual product files; actual protected hashes remained unchanged before/after. `git status --short` remained empty. No tracked edit, index change or HEAD change was made.

## Final file hashes and check acceptance

SHA-256 of reviewed final bytes:

| File | SHA-256 |
|---|---|
| foundations/decisions.md | af55d319b598ff1a25bfec61806d97fb31315b5c6a6f3df44be6c40cd81c65aa |
| foundations/invariants.md | 0c112cd3cd13edd7860dabb4512632bb773e5295dff7f4d150319a94b8ae60a5 |
| project-level/plan_state.py | 027a95f1f60c2e185555146015d168f26b39b574a3fe1cee5fe680a39d554970 |
| project-level/test_plan_state.py | dc3ea4b029d325d2489398354dd337ff04aa9d768f37fc2c911bc7b3786d095d |
| project-level/test_plan_state_invariant.py | 1bb9a2a2bad076ec4a424278e3ae2958458c17b7b344209726a081791f50b206 |
| project-level/test_plan_state_subprocesses_invariant.py | 01e7262b943a5055e3711e689fffbb8037c0b3d68077cc9b49cb33debcb285c2 |

**project-plan-state-evidence/1: ACCEPTED for the reviewed final sentence/check/code.** Product pass precedes independently derived identity/freshness failures; restoration and focused clean verification pass. Check authority a9e766d; covered code 114c689; sentence authority 9ae98fe. The earlier pre-identity break is superseded by this evidence.

**project-plan-state-subprocesses/1: NOT ACCEPTED.** Product pass precedes its first return-step acceptance attempt after assessment settlements, but the final 2cadf14 check misses the tested violation in 114c689. WAY-149 requires resolution of the undetected break and affected verification before acceptance. The owned control proves a concrete fixture coverage gap and the audit's ability to detect this actual process when reached. It is diagnostic evidence, not acceptance of the unchanged protected check.

## Other review conclusions and limits

The reader compares anchored original paths and retained plan membership, not titles/numbers/basenames. Historical snapshots are inspected separately; only owned record paths supply pointers, and only owned commits in freshly fetched reachable history can supply done. Contradictory candidates prevent automatic task progress. Duplicate/unreadable/missing provenance fails conservatively. Existing UTF-8 output, argument-array Git execution, document preservation, source/readiness validation and integration-source behavior remain intact in the affected diff. The final independent positives retain alternative record basenames and source editorial changes; negatives distinguish two independently valid same-named plans. No further concrete correctness issue was established in this range.

This review does not claim support for arbitrary legacy prose, moved source paths, cross-platform path spellings, symlink aliases or all natural-language metadata formats. Those remain unresolved rather than grounds to guess ownership. The subprocess audit observes Python process-start events in the reader, not Git's own descendants, unaudited native calls, or the authenticity of an executable merely named Git. Its existing operational-error fixture fails at remote access before an actual fetch; no claim of exhaustively exercising every failure branch is made. Static source/workflow review does not demonstrate that a future agent follows the instructions. No full foundation gate or human approval is asserted.

Outstanding work: R2 only in this affected review. Root owns its settlement, dispatch to the independent check author, affected verification and resumed reviewer acceptance. Stop here; no next-stage dispatch was made by this reviewer.
