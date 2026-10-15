# Assessment settlement — cycle identity implementation

Status: DONE — committed implementation boundary reached; affected review and deliberate breaks belong to root.

Base: a9e766d99672bf3c7693ebd4a5519e7fb8d30acf, branch task/lead-project.
Foundation authority: 9ae98fe0b8421c5b486785a462648f51f9c50f08.
Independent check authority: a9e766d99672bf3c7693ebd4a5519e7fb8d30acf.
Final implementation head: 114c68960670e31a878ff00fbdf9ed5c00689089.
Commit: fix: associate cycle evidence with its project task.

## Authority and scope

Read the complete implementation handoff, source ruling, current archive recognition ruling,
independent check contract/report and protected checks. Frozen task, corrected specification,
plan, record/task/plan templates and task-cycle adapter govern this repair. Superpowers 6.4.1
test-driven-development, writing-good-tests and implementer prompt were read from the installed
cache. This is a correction within the one independent assessment, not a new assessment,
feature or design stage. No child agent or next-stage dispatch was started.

Only project-level/plan_state.py and project-level/test_plan_state.py are product writes.
No foundation, invariant test, parser, installer, wrapper or task-cycle source was edited.
The existing UTF-8 stdout correction remains. Private acceptance inputs stay in ignored reports.

Foundation selection refreshed at the base above for the actual touched part project-level.
Complete part map read, including the reader boundary, high false-progress failure and pinned
project-plan-state-command surface. Complete current Scope inspection selected:
WAY-09, WAY-106–124, WAY-126–127, WAY-134, WAY-137–140, WAY-142–147, WAY-150–156 (all /1).
Each matching entry was read whole; output truncation was recovered with additional reads of
WAY-122, WAY-140, WAY-142 and the later entries. Additional linked/explicit entries read include
WAY-21, WAY-33, WAY-36, WAY-38, WAY-89, WAY-100, WAY-125 and WAY-135. Both final reader
invariants, the current project-level/`every` invariant entries, relevant glossary entries and
python-stdlib-modules/1 were read. Searches across the five foundation files for provenance,
cycle trace, archive, reader, plan-local identity, imports and subprocesses found the governing
WAY-153, reader invariants and map boundary; no additional product write follows from this
code correction. This is a selection record, not a claim that the unfinished foundation gate
or TODO methods passed.

## Implementation and obligations

Each live directory and historical commit snapshot is associated separately. Recorded original
Task source must match the supplied plan Document path. Frozen task membership is resolved from
its retained artifact against the original source directory, not against the archive directory
or today's source text. This preserves editorial changes without a byte-equality requirement.
Ordinary record basenames remain supported. Duplicate/unreadable ownership remains unchecked;
explicit different source/plan/task is exposed for reconciliation. Historical record evidence and
PR pointers are accepted only from the same verified snapshot, never borrowed from a later local
record. Source paths, Markdown and record prose are data; the reader still starts only Git.
Fresh integration reachability and previous readiness/state/path/fetch/history checks remain
separate prerequisites for completion. Original source preservation assertions remain in all
command fixtures.

Ordinary positive fixtures now contain genuine Task source/relation, a retained frozen task and
its Project relation. All prior ordinary methods and assertions remain. Independent two-plan
cases retain distinct valid source directories with the same slug/title/number/basenames.

## TDD evidence

Independent RED before production edits:
`python -B -m unittest discover -s project-level -p test_plan_state_invariant.py -v`
exited 1, 27 tests in 42.549s, seven expected failures. The three other-plan cases still proposed
progress/returned success, and the four absent or unanchored provenance cases still advanced.
Full output: identity-implementation-red.txt. The 20 existing/positive cases passed.

Additional focused ordinary RED commands use
`python -B -m unittest discover -s project-level -p test_plan_state.py -k FILTER -v`:

| FILTER | Initial exit | Missing behavior | Evidence file |
|---|---|---|---|
| snapshot | 1 | Foreign integrated snapshot cannot borrow later owned identity/pointer | identity-implementation-snapshot-red.txt |
| duplicate_record | 1 | Duplicate source fields are ambiguous | identity-implementation-duplicate-red.txt |
| frozen_membership | 1 | Frozen task naming another plan is contradictory | identity-implementation-membership-red.txt |
| explicit_record | 1 | Expanded record relation cannot silently disagree with frozen membership | identity-implementation-relation-red.txt |
| quoted_provenance | 1 | Fenced example cannot impersonate header provenance | identity-implementation-quoted-red.txt |
| renumbering | 1 | Old item number must not override stable name/source identity | identity-implementation-renumber-red.txt |
| semicolon | 1 | Existing semicolon approval annotation is not part of source filename | identity-implementation-semicolon-red.txt |
| delimiters | 1 | Literal semicolon/em-dash inside source directories is preserved | identity-implementation-delimiters-red.txt |
| without_recorded | 1 | Same-source non-plan relations are unchecked, not falsely foreign (three subcases) | identity-implementation-membership-unknown-red.txt |
| source_commit | 1 | Template source-commit provenance alternative identifies original task | identity-implementation-source-commit-red.txt |

After the first implementation,
`python -B -m unittest discover -s project-level -p test_plan_state*.py -v` exited 0,
50 tests in 77.230s, identity-implementation-focused.txt. Later relation, quoted-provenance,
renumbering and semicolon focused GREEN runs exited 0 (matching *-green.txt files).
All additional focused GREEN commands exited 0; the same-source classification follows the complete
root ruling identity-membership-ruling.md, read before its focused regression and correction.
The semicolon bug was discovered by the actual acceptance, reproduced first in its new focused
test, and then corrected. No test failure was removed, skipped or reclassified as a pass.

## Broad verification

The first exact shared Method, `python -B gate/run_tests.py project-level --record
.runs/project-plan-state-evidence.jsonl`, exited 0: 246 tests in 82.758s. Its bytes precede the
semicolon correction and additional regression; retained as
identity-implementation-project-level-superseded.txt, not current evidence.
The first gate run exited 0: 98 tests in 22.446s; retained as
identity-implementation-gate-superseded.txt. It is superseded after the final same-source correction.
Final `python -B gate/run_tests.py gate` exited 0: 98 tests in 27.160s,
identity-implementation-gate.txt, covering final product bytes.
Current entry-point check exited 0 (`entry points are current`), without regeneration.
`git diff --check` exited 0. Final exact shared Method:
`python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
exited 0: 250 tests in 108.425s, identity-implementation-project-level.txt. This covers the
settled final bytes, including both protected checks. All final suite output is clean.
Final current entry-point check and diff --check both exited 0 before the explicit-path commit.

The other three part suites passed at 84cdc87 per the handoff; installation/task-cycle/
agent-instructions product bytes remain unchanged. Those suites were not repeated here.
No full gate, independent affected review or final deliberate-break acceptance is claimed.
Root owns those later reviews and deliberate breaks.

## Actual original loop2 acceptance

Command and original whole plan match acceptance-reader.md/final-fix-acceptance.json; the
disposable clone is .runs/task-cycles/lead-project/acceptance-loop2. Vault rulebook was read
before source access. The helper identity-acceptance-run.py records original plan/definition
SHA-256 and original source repository HEAD/status before/after, runs the CLI with
PYTHONIOENCODING=cp1252, and retains its actual UTF-8 output.

Initial result: overall exit 1; both required mag-w-lesie proposals present. Source plan and
definition hashes and original repository HEAD/status unchanged, matching the original baseline.
Its actual c9644b21ec1d8124937d7e7ac7c8f6c49c6a79d9 cycle.md source and task.md membership match
the original supplied plan/Document cell. Separate acceptance-pr12.json retained; the actual record
contains PR #12 and git merge-base confirms the archive commit is an ancestor of the recorded
PR merge. No PR host command was added to the CLI or reissued by this executor.

The initial run exposed the source delimiter bug described above. Its output/JSON are retained
as identity-implementation-acceptance-initial.txt/.json. Final acceptance repeated on settled final
bytes: exit 0, both required mag-w-lesie proposals present, same source preservation and original
baseline comparisons true. Current output/JSON are identity-implementation-acceptance.txt/.json.
Actual own-cycle source, frozen membership, Document row, PR pointer and independent PR #12
association are retained in the JSON. Task 1/2 receive concrete unchecked reasons and no proposals;
no unknown relationship was promoted into evidence.

Task 1 was independently inspected by root: at 4537daece8958fd68fb239de28ec08c6ceaa4a53,
docs/task-cycles/app-skeleton/cycle.md names the same original Task source as the current Document,
but Task relation is `source only — MVP definition ...`; retained task.md says
`Project relation: source only: MVP loop2 — `definicja_mvp_loop2.md`, approved 2026-10-04`.
Root's identity-membership-ruling.md settles this as unchecked because the same source is known but
current plan membership is not recorded; it is not evidence of a named foreign plan/task. The
classifier correction was made only after a focused RED regression, then GREEN.
Task 2's free-text relation and annotated frozen artifact path are unsupported representations
and may remain explicitly unchecked under root's instruction; no speculative legacy parser added.

## Protected checks

Before and after implementation, SHA-256:

- project-level/test_plan_state_invariant.py:
  1bb9a2a2bad076ec4a424278e3ae2958458c17b7b344209726a081791f50b206
- project-level/test_plan_state_subprocesses_invariant.py:
  01e7262b943a5055e3711e689fffbb8037c0b3d68077cc9b49cb33debcb285c2

Both remain read-only. Their final-byte comparison after the settled correction and again after
the commit matches both before hashes exactly. Product final SHA-256 before commit:
plan_state.py 027a95f1f60c2e185555146015d168f26b39b574a3fe1cee5fe680a39d554970;
test_plan_state.py dc3ea4b029d325d2489398354dd337ff04aa9d768f37fc2c911bc7b3786d095d.

## Choices and costs

| Routine choice | Alternative and its cost | Chosen path's cost/limit |
|---|---|---|
| Lexical original path comparison plus anchored frozen membership | Slug/basename/title comparison repeats the two-plan false positive; resolving/searching moved sources guesses ownership | Moved source paths remain unresolved; no global name or UUID migration |
| Locate frozen task in existing Artifacts table, plain or Markdown path | Require task.md filename excludes independent accepted-task.md and valid alternate names | Unknown/annotated representations remain unchecked rather than guessed |
| Read each historical snapshot separately and limit pointers to owned records | Validate all historical commits from the current tip borrows identity/completion | Additional Git reads and conservative unknown snapshots |
| Honor explicit expanded record plan/name; old item number stays contextual | Make task number identity breaks a stable named task when plan numbering changes | Narrow supported expanded representation; unknown prose stays unchecked |
| Duplicate metadata and quoted headers fail closed | Pick the first convenient field or scrape examples allows unsupported progress | Human lookup for ambiguous records |
| Keep all foreign observations visible and withhold task progress | Ignore contradictory history can hide a collision | A valid own trace alongside a foreign trace still needs reconciliation |
| Same-source non-plan relation remains unchecked under root ruling | Call it foreign overstates the evidence; call it owned invents membership | Existing workflow must reconcile the unresolved historical relation |

No new open design choice or durable foundation rule was needed. Root's same-source/source-only
classification is settled and applied; unknown representations remain deliberately unchecked.

## Self-review and limits

Reviewed own final diff for exact path boundary, per-snapshot provenance, no external frozen-link
reads, live/archived symlinks, data-only prose, pointer association, source preservation, existing
UTF-8 output and Git-only child process behavior. No product third file or protected test was
changed. Parser unknowns deliberately remain visible; this code does not claim to understand
every natural-language annotation. No backlog write, push, merge or outside-product mutation.
The explicit-path commit contains only the two authorized product files. Working tree is clean;
no upstream is configured for task/lead-project, and no push was performed. No final review or
deliberate break was run by this executor. Root receives the committed boundary for its affected
review (84cdc87..114c689) and later invariant acceptance. There are no unresolved implementation
questions; expected unchecked task 1/2 historical relationships are documented above.
