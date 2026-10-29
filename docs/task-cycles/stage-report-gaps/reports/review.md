FAIL e95be3b912c09ce1e6f00be167880431a3a26301

# Whole-change review

Range: `d115159c554752601749efa8270ae76fbe02f4df..e95be3b912c09ce1e6f00be167880431a3a26301`.
One-author route; no slices, spec or plan. Blocking: 1 Important; Critical: 0; Minor: 0; out of scope: 0.

## Important — new thread

### 1. Preserve the rejected alternatives and their reasons from the accepted settlement

**Anchor:** `foundations/decisions.md:7430` (WAY-260, Rejected).

**Do wklejenia:** The new decision drops the task's rejected alternative of extending WAY-148, and changes the rejected review condition into “making this temporary or conditional” with a different reason. Preserve the alternatives and costs actually retained under the task's answers: extending the existing handoff decision would mix two purposes, while a review condition needs a measure and an obligation to check it. Remove the unsupported claim about temporary reporting failing to provide a steady basis.

**Why this is reported:** The decision is the durable record of the human's accepted settlement. The task's single accepted row expressly takes its rejected ways from the answers in Questions to settle, and the decision template requires each retained way with the cost or reason kept beside it. WAY-134 requires source fidelity; it does not allow the entry writer to derive alternative choices or reasons from the cost of the chosen way.

The fifth answer keeps the rejected option of changing WAY-148: “już długa decyzja o przekazaniu pracy orkiestratorowi rośnie o drugi cel, a nośnik E23 wskazałby decyzję mówiącą głównie o czym innym”. WAY-260's complete Rejected paragraph contains no counterpart. The fourth answer rejects “warunkowi powrotu w decyzji (miara do ustalenia i obowiązek sprawdzenia w samej decyzji)”. The entry instead says “making this temporary or conditional — the reports would not provide a steady basis for reducing the process's cost.” A condition for reconsidering the scope does not imply temporary reporting or a loss of steady evidence. The new reason is plausible, but is not the reason preserved in the source.

This matters when a later agent considers folding the rule into WAY-148 or revisiting its scope: it would miss an option the human rejected and rely on a reason the human did not give. This is an in-scope missed source-fidelity requirement, not wording polish. Fix the one Rejected paragraph, retaining the existing faithful alternatives and translating the two source alternatives without their private note identifier. For example, the relevant replacement clauses can say: “adding the rule to the handoff decision — that decision would carry a second purpose, while the reason for collecting gaps would point to an entry chiefly about something else; a condition for revisiting the scope — it needs a measure to be settled and an obligation to check it in the decision.” No new human decision is needed to carry the existing source faithfully.

Origin: the one author's commit `e95be3b912c09ce1e6f00be167880431a3a26301`; no slice.

## Minor

None.

## Declined to judge

None. The task's explicitly excluded lesson-map update, measured product cycle and changes to the external extractor were not part of the proposed change; no unrelated behaviour was investigated and then set aside as a finding.

## Coverage and source fidelity

- To do 1: met. The separate item appears beside the unchanged reach account in make-change, review-change, plan-task, spec design and spec review. It admits `none` and includes instructions, dispatch, task, foundation and product code. Make-change's shared report applies to author, slice, fix and correction; the orchestrator's shared contract also applies to foundation and return-step dispatches. The changed fragments are one reporting instruction each and fit WAY-256's single-instruction exception; the spec fragments remain in their existing variant files.
- To do 2: met. The orchestrator reads the searches section even for `done` reports and copies each non-`none` item verbatim, with stage and full path and without merging repeats. The template places these items in its existing Process remarks bullet.
- To do 3 and Settlements to record row 1: the new WAY-260 exists and derives from WAY-148. Its binding meaning implements the accepted row. Its Rejected source fidelity is incomplete as finding 1 explains. No projected entries were carried.
- Acceptance criterion: the template's Process remarks bullet and deeper-indented continuation are inside the external extractor's block. A scratch execution of the actual extraction function retained repeated nested remarks and their separate paths, and a negative control proved that a sibling remark would be excluded. This checks the required record shape, not the behaviour of a future orchestrator. No actual cycle record was read or used.
- No changed invariant tests, executable code, UI, trust-boundary files or irreversible operation. No discipline guidelines are required for the prose-only work under product-guidelines/reading.md. The applicable review-method invariants remain compatible with the diff: foundation element separation, file location, no private outbound links, no new scripts or CI commands. Integration and the return-step record remain the orchestrator's later work, rather than outcomes established by this review.
- WAY-260's reasoning is understandable without the private lesson map; no inaccessible source link was introduced. Existing reach instructions remain semantically unchanged.

## Author's own-work check

The named weakest point, coverage of all stages and extractable record placement, fits this change. Its manual method can find a missing reporting method and reason about the extractor's indentation contract. Independent inspection confirmed that coverage and the scratch run confirmed the extraction mechanism. The author's method does not establish that a future agent will populate the record correctly; neither does this review claim such a run. The author's source-fidelity check did not catch finding 1. No permanent text-matching test is needed to repair that omission.

## Executed checks

All commands ran from `C:/Storage/repos/the-way/.runs/worktrees/stage-report-gaps` without changing tracked files or the index.

- `git rev-parse HEAD` — exit 0, exactly the dispatched head.
- `git log --oneline d115159c554752601749efa8270ae76fbe02f4df..e95be3b912c09ce1e6f00be167880431a3a26301` — exit 0, one author commit.
- `git diff d115159c554752601749efa8270ae76fbe02f4df..e95be3b912c09ce1e6f00be167880431a3a26301` — exit 0, whole diff inspected.
- `git diff --check d115159c554752601749efa8270ae76fbe02f4df..e95be3b912c09ce1e6f00be167880431a3a26301` — exit 0.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `git status --short` — exit 0, empty, before writing this ignored review report.
- Scratch extraction check below — exit 0, `PASS: repeated nested remarks retained; sibling remark excluded`. It executes only the source fragment holding the extraction helpers, not the external script's scanning or writing workflow. No file is written.

```powershell
@'
from pathlib import Path
from dataclasses import dataclass
import re
source = Path('C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/scripts/cycle_remarks_digest.py').read_text(encoding='utf-8')
fragment = source[source.index('@dataclass\nclass RemarkBlock:'):source.index('\ndef read_record(')]
namespace = {'dataclass': dataclass, 're': re}
exec(fragment, namespace)
extract = namespace['extract_remark_blocks']
record = '- Process remarks on the-way:\n  - author; C:/reports/author.md: Missing instruction.\n  - reviewer; C:/reports/review.md: Missing instruction.\n- Next field: excluded\n'
blocks = extract(record)
assert len(blocks) == 1
assert blocks[0].text.count('Missing instruction.') == 2
assert 'C:/reports/author.md' in blocks[0].text
assert 'C:/reports/review.md' in blocks[0].text
assert 'Next field' not in blocks[0].text
bad_record = record.replace('  - reviewer', '- reviewer')
assert 'C:/reports/review.md' not in extract(bad_record)[0].text
print('PASS: repeated nested remarks retained; sibling remark excluded')
'@ | python -B -
```

Manual checks (command and exit code not applicable): read the frozen task whole; compare each To do item, acceptance criterion and accepted row with the whole diff; compare each rejected option with its task source; trace all changed report positions and the shared orchestrator contract; read selected foundation entries whole and judge their applicability; inspect extractor helpers and compare the placeholder indentation with their termination condition. Results are above.

Skipped: full `python -B gate/run_tests.py`, assigned to the orchestrator; unrelated Python tests, no executable change; future-agent behavioural trial, not run; actual cycle-record extraction, prohibited from reading cycle.md and not required to verify the template shape. None of these is called passed.

## Reaches beyond the dispatch and selection

- `elements/decisions/template.md`, whole: to check the exact source rule for a settlement's Rejected paragraph and its reasons. Linked decisions WAY-19, WAY-29, WAY-35, WAY-114 and WAY-225 were read whole to check numbering, reasoning, element-rule placement and acceptance against the new entry. These were targeted follow-up reads, not a second whole-foundation search.
- Read the unchanged make-change and write-spec method routing and the record template around the changed reporting points to verify that their variants inherit the new instruction. Searched task-cycle report/reach references to establish coverage.
- The external extractor was named by the dispatch; reading and scratch execution of its extraction helpers are not an unannounced dependency. Its workflow and private lesson map were not changed.

## Searches not found or unclear

- I looked for the task's rejected option of extending WAY-148 in WAY-260's Rejected paragraph and did not find it; the task preserves it under the final Questions to settle answer.
- The source of WAY-260's claim that temporary or conditional reporting would not provide a steady basis for reducing cost was unclear: the task instead preserves the cost of defining and checking a condition for revisiting the scope.
