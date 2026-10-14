# Independent assessment source correction

## Change

- Base: `1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`
- Head: `c744b15f4a48d5525e42022a5e364997e2fe1f43`
- Commit: `docs: :memo: align search reads with WAY-150`
- Changed file: `elements/common/way_of_working.md`

The shared foundation search now says: “Read each entry selected or found by the search whole
(WAY-150): a decision's *Rejected* holds an option already weighed and refused, and nowhere else
says so.” This replaces the old whole-entry sentence and its pending-decision parenthesis. WAY-150
already governs selected entries and expands selection when a whole-foundation search finds
another relevant entry. The wording therefore identifies the intended search findings without
restoring an instruction to read every foundation entry. The search's whole-foundation domain,
other search duties, and separate search record remain unchanged. No other TODO or binding meaning
changed.

## Inputs and refreshed selection

Read the frozen task, complete assessment and settlement, this worktree's full
`elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/common/skill/SKILL.md`,
and `foundations/part_map.md`. The map assigns the changed path to `elements-common` and describes
this part's shared foundation-entry rules and workflow. The full `WAY-150/1` entry governs the
selection and whole-entry reading; `WAY-37/1` governs fixing entries that wait for material the
change brings. The full `WAY-33/1` entry governs the whole-foundation search and its evidence.

At revision `1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`, inspection of every current decision
`Scope` field found these 26 `elements-common` matches. Their complete entries are included in the
existing selection evidence at that same revision: 130 current matches across the eight parts,
with 130 identifiers recorded as read and no missing identifiers. The refreshed subset and source
locators are:

| Expected and read decision | Source lines |
|---|---:|
| WAY-09/1 | 234–304 |
| WAY-10/1 | 305–342 |
| WAY-35/1 | 1009–1042 |
| WAY-41/1 | 1152–1177 |
| WAY-54/1 | 1508–1540 |
| WAY-57/1 | 1602–1644 |
| WAY-61/1 | 1728–1781 |
| WAY-64/1 | 1850–1889 |
| WAY-71/1 | 1991–2028 |
| WAY-72/1 | 2029–2054 |
| WAY-74/1 | 2088–2122 |
| WAY-79/1 | 2205–2234 |
| WAY-83/1 | 2344–2371 |
| WAY-97/1 | 2681–2716 |
| WAY-100/1 | 2783–2808 |
| WAY-101/1 | 2809–2831 |
| WAY-102/1 | 2832–2858 |
| WAY-103/1 | 2859–2883 |
| WAY-113/1 | 3176–3211 |
| WAY-114/1 | 3212–3240 |
| WAY-115/1 | 3241–3271 |
| WAY-117/1 | 3300–3328 |
| WAY-120/1 | 3390–3421 |
| WAY-127/1 | 3695–3753 |
| WAY-134/1 | 3967–4014 |
| WAY-150/1 | 4647–4684 |

WAY-33/1 (lines 949–979) and WAY-37/1 (lines 1070–1096) were also read whole as the search and
same-change cleanup rules. The full refreshed evidence is in
[`return-scope-evidence.json`](return-scope-evidence.json); the earlier cycle report records that
the two implementation slices read 109 and 79 entries covering all 130 expected matches in total.
The independent settlement accepts only this one correction; no other assessment observation or
TODO was changed.

## Checks

| Command | Exit | Result and evidence |
|---|---:|---|
| `python -B gate/run_tests.py elements/common --record .runs/task-cycles/selective-document-reading/reports/assessment-fix-elements-common.jsonl` | 1 | `NO TESTS RAN`; there are no tests in this directory. This is unchecked for the source correction, not a passing suite. [Captured stdout/stderr](assessment-fix-elements-common.txt), [JSONL record](assessment-fix-elements-common.jsonl) |
| `python -B gate/run_tests.py gate --record .runs/task-cycles/selective-document-reading/reports/assessment-fix-gate.jsonl` | 0 | 98 tests ran; `OK`. [Captured stdout/stderr](assessment-fix-gate.txt), [JSONL record](assessment-fix-gate.jsonl) |
| `git diff --check` | 0 | No whitespace errors. |
| `rg --text -n '[\x00-\x08\x0B\x0C\x0E-\x1F]' elements/common/way_of_working.md` | 1 | No control-character matches. |

The full critical-flow runner passed. It does not test the prose change directly. No full-gate
claim is made.

## Self-review and remaining concerns

The final source diff is one hunk in the search instruction. The replacement explicitly covers an
entry selected by the search or found by it, cites the existing decision, and retains the reason
for reading `Rejected` whole. The following glossary and waiting-entry searches remain intact, as
do the rule to settle every finding, the repeat search against the integration branch, and the
two-search evidence requirement. The source file remains LF; the commit contains only this one
source path.

No unresolved wording concern remains from the settled assessment. The changed-part runner found
no tests, so behavior of this prose rule is unchecked by an executable test. The affected scoped
review remains the next stage; work stops here before review, archive, or push.

## Receiving-stage read evidence clarification

I did **not** personally complete the 26-entry whole read before the source commit. The earlier
selection evidence records reads by the preceding implementation stages and is not evidence of my
own read in this stage. After commit `c744b15f4a48d5525e42022a5e364997e2fe1f43`, I read each of the
26 `elements-common` Scope matches in the table above, whole, from `foundations/decisions.md` at
revision `1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`. I completed that read on 2026-10-14 between
07:07 and 07:09 UTC. The receiving-stage expected set and actual whole-read set are identical:
WAY-09/1, WAY-10/1, WAY-35/1, WAY-41/1, WAY-54/1, WAY-57/1, WAY-61/1, WAY-64/1, WAY-71/1,
WAY-72/1, WAY-74/1, WAY-79/1, WAY-83/1, WAY-97/1, WAY-100/1, WAY-101/1, WAY-102/1, WAY-103/1,
WAY-113/1, WAY-114/1, WAY-115/1, WAY-117/1, WAY-120/1, WAY-127/1, WAY-134/1, and WAY-150/1.
No expected match was omitted.

For the matched entries' relevant links and the correction's governing rules, I also read WAY-21/1
(lines 623–644), WAY-33/1 (lines 949–979), WAY-37/1 (lines 1070–1096), and WAY-150/1 whole. The
whole reads of the task, common method, shared rules, part map, WAY-150, WAY-33 and WAY-37 were
already completed before commit as recorded above; this clarification concerns the 26 matching
entries, which were read after commit. This additional reading did not reveal a concern or change
the correction's meaning. The source, index, and HEAD remain unchanged.
