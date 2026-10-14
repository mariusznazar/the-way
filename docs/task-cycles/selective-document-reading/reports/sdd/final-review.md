# Whole-branch review

Assessed range: `52b9d487efeafe37c46ad2b9f10d60c13a885e63..0c266f3da8cb92204d7788c4bce9065bc2e8b92e`.
Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
This is the Superpowers final code review, not the later independent foundation assessment.
Tracked tree, index, HEAD and branch were left unchanged. Only this report was written.

The implementation preserves the task's two accepted settlements and its completeness requirements.
There is one actionable source-consistency finding. No other correctness finding emerged from the
whole-branch review; the next review should verify the fix, not reopen the whole document design.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

#### 1. Name the actual plan/readiness check instead of adding the forbidden synonym

**Thread:** NEW.

**Anchor:** [foundations/decisions.md:4706](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/foundations/decisions.md#L4706).

**Do wklejenia:** WAY-151 adds an unquoted `checker`, and the glossary guard reports that its count in this file grew from 1 to 2. This example concerns readiness or plan checks; please name those checks directly, because `format guard` means an element's entry-shape script and would identify a different tool here.

**Dlaczego to zgłaszam:** The example is meant to reject verification against a reduced definition
or plan. Its current text is:

> - violates: only nearby rows are inspected and a distant dependency is missed; the checker
>   receives a reduced copy; a new breakdown omits a scope item; the critic's review is bounded
>   by the author's excerpts or leaves some tasks and questions unjudged.

The [glossary definition and Avoid field](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/foundations/glossary.md#L70)
define a format guard as the script of an element checking the shape of its entries, and list
`checker` as a synonym to avoid. [WAY-98](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/foundations/decisions.md#L2717)
counts uses across the foundation, including verification examples, rather than only binding
sentences. The new occurrence is neither quoted nor a restated old version. A focused diagnostic
against the exact review base confirms the increase:

```text
python -B elements/glossary/format_guard.py foundations/glossary.md --base 52b9d487efeafe37c46ad2b9f10d60c13a885e63 --merge-onto none

foundations/glossary.md:0: error: foundations/decisions.md: `checker`, which the *Avoid* of `format guard` lists, stands 2 time(s), 1 on 52b9d487efeafe37c46ad2b9f10d60c13a885e63
unchecked: `TODO` in the entries — --merge-onto none: there is no commit to merge onto
unchecked: the terms with no use after the merge — --merge-onto none: there is no commit to merge onto
note: the-way's own glossary is no product's: its terms are not compared with the glossary of the-way
1 error(s), 0 warning(s), 2 unchecked
```

Exit code: 1. This explicit-base diagnostic detects the introduced growth; it is not a claim that
the repository has a main branch or that its full gate ran. Its two unchecked results remain so.

The semantic distinction matters independently of the counter. The entry's binding text names
readiness and plan checks; [plan_check.py:634](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/project-level/plan_check.py#L634)
reads the plan and its named definition, and
[readiness_check.py:335](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/project-level/readiness_check.py#L335)
reads a project definition. Neither is an element's entry-shape script. Replacing `checker` with
`format guard` mechanically would make the example refer to the wrong object. WAY-95/97 do not
justify widening that term's definition to cover any script that checks something.

Recommended local wording: `a readiness or plan check receives a reduced copy`. It preserves the
intended example, adds no glossary meaning and requires no new glossary entry or decision. Leaving
the text retains a reproducible growth error and ambiguity; correcting this clause costs one
local prose edit and a focused check. The old unquoted occurrence at decisions.md:3067 predates
this branch and is already counted at Base; it is not a reason to add another or to rewrite the
glossary here. The foundation report's claim that no new Avoid spelling was found needs correcting
in the review settlement; the 204 passing glossary tests are not evidence that this corpus
comparison passed. Verification prose does not change WAY-151's binding fingerprint.

### Minor (Nice to Have)

None. Line wrapping preferences do not warrant another document-review iteration.

## Strengths and coverage

- [Shared selection](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/elements/common/way_of_working.md#L59)
  contains a complete current Scope sweep, wrapped fields, latest versions and repeals, malformed
  Scope handling, complete selected entries, expected-versus-selected comparison and refresh.
  Selection begins with the full map and proposed behavior even before a diff; entry-collecting
  files follow WAY-44. Incoming dependents and invariant `Part: every` are explicit. This meets
  the task's decision-selection requirement without falsely implementing its Method TODO.
- All thirteen reader sites use that contract. Element-specific question/identifier discovery,
  number/version discovery, fact-method and dependent duties, invariant check authorship and
  glossary every-use review remain. The common whole templates/rules/examples and candidate
  finder's whole source, complete table and human row selection remain. Searches still span all
  five elements beyond initial parts and links, with WAY-33's two timings and records intact.
- [Plan reading](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/project-level/plan/skill/SKILL.md#L48)
  inventories every scope item, projected heading, exact question, task and assignment before
  choosing resumed work. Complete rows/source units and dependency/meaning expansion address
  distant prerequisites and writers; every item is processed for a new breakdown. Authoritative
  whole originals remain script inputs. The unchanged scripts' whole-file reads and relative
  definition-path handling agree with these instructions.
- [Independent plan critique](https://github.com/mariusznazar/the-way/blob/0c266f3da8cb92204d7788c4bce9065bc2e8b92e/project-level/plan/skill/SKILL.md#L123)
  reads the complete plan and every needed source unit independently of the author's inventory.
  WAY-146's semantic responsibilities, post-correction check and human handover survive. A
  structurally clean layer-only goal, unexplained question move or inadequate answer still needs
  judgment; the script is not represented as proving it.
- WAY-150/151 carry both settlements; WAY-111/115 change the authorized reading obligations and
  preserve human conflict/candidate decisions. WAY-134's binding meaning and fingerprint remain
  unchanged while its WAY-115 reference is renewed. Incoming references to WAY-134 therefore do
  not require renewal. A read-only verification of the actual parsed log confirmed all 151
  current carried relation fingerprints. No executable source or invariant test changed.
- Task-cycle refreshes attach to existing stages. Frozen-task/source obligations, projected-entry
  ownership, approval authority and the independent assessor's filtered package remain intact.
  The part-map responsibilities and skill names/descriptions/locations have not changed; there is
  no unsupported new selector, inventory format or entry-point generation requirement.

## Evidence and checks

Read the frozen task, reviewed spec, final plan, progress ledger, foundation report, slice reports
and reviews, final verification summary, actual changed hunks and their reader context. Consulted
the review playbook and linked bounded-document-review guidance, installed reviewer prompt,
integration instructions, glossary/common rules, relevant decision entries, and the original plan
and readiness scripts. Truncated source output affecting a judgment was recovered in narrower
reads. Reports were evidence, not a substitute for the source at Head.

Personally ran:

- `git diff --stat Base..Head` and `git diff Base..Head` for the exact hashes above: fourteen
  Markdown files, 252 insertions and 69 deletions; no code/test-body change.
- `git diff --check Base..Head`: no whitespace finding.
- `git rev-parse HEAD`: exact assessed Head; `git status --short`: clean tracked working tree.
- Focused `rg` searches across readers for retained whole-foundation/full-source clauses, and
  across foundation sources for the changed decision dependencies and `checker` uses. Existing
  whole-source reads outside plan-project and whole-foundation searches are intentional retained
  duties, not missed conversions.
- The glossary diagnostic above: one introduced error, two unchecked checks.
- `python -B .runs/task-cycles/selective-document-reading/reports/verify_foundation.py`, after
  inspecting its read-only body: 151 relation fingerprints match, zero forbidden control bytes;
  fingerprints WAY-111 e2fd46dc, WAY-115 eb7ba15c, WAY-134 b858b34f, WAY-150 3bd9e695,
  WAY-151 739610de.

Existing execution evidence used, without rerunning the suites:

- [Final verification](../final-verification.md)
  and its JSON source identify stable Head and 1,265 passing tests: decisions 169, map 162,
  invariants 233, glossary 204, facts 165, project-level 193, task-cycle 41, gate 98. Inspected each
  suite's log ending. Common ran zero tests and exited 1 with `NO TESTS RAN`; it is unchecked.
- Decision-guard log: zero errors, nine warnings and five no-main unchecked comparisons. Warnings
  are five existing overdue reviews (WAY-03/21/52/55/69) and the four approval URL placeholders.
  Direct relation inspection supplements only its skipped fingerprint comparison.
- Map-guard log: zero errors/warnings, seven unchecked results: two missing flow coverage files,
  unreported promise-level policy and dependency graph, plus three no-base comparisons. These are
  limitations, not passes.
- Slice walkthroughs are instruction inspections, not executed future-agent sessions. Their
  wrapped Scope, no-diff ownership, incoming dependent, Part every, out-of-selection collision,
  distant plan dependency/writer/question and structurally clean semantic-failure scenarios agree
  with the final clauses. No concrete doubt justified rerunning all suites.

## Recommendations

Apply the single wording fix and retain its glossary diagnostic in the scoped re-review. Correct
the review record's Avoid-spelling claim. Do not widen the glossary or build a selector to fix
this local issue. The shared method plus thin callers is proportionate to the requested behavior;
new literal-text tests would not establish semantic completeness.

Keep later boundary work visible: replace four approval placeholders when the request exists,
perform the second whole-foundation search against the integration tip, complete the independent
foundation assessment and obtain human merge acceptance. This review neither performs nor waives
those stages.

## Declined to judge

- Actual future-agent reading/comprehension and exhaustive semantic collision discovery: no
  executed workflow evidence proves them; instructions and inspection walkthroughs are assessed.
- Real large-project context/token savings: no before/after measurement is supplied, and this task
  promises a reading method, not a savings percentage.
- Completion of the full gate and automatic `decisions-found-for-change/1` Method: existing debt,
  explicitly outside this prose implementation; Method TODO stays visible.
- Future integration reconciliation, second foundation search, independent assessment and human
  acceptance: subsequent stage duties, not missing implementation at this review boundary.
- Repair of the pre-existing unquoted `checker` at decisions.md:3067 and overdue decision reviews:
  outside this change; the introduced occurrence is judged and reported above.

## Assessment

**Ready to merge? With fixes.**

The requested reading behavior and retained completeness/authority safeguards are implemented
coherently. Correct the introduced glossary-use error, verify that small fix, and complete the
already required later integration stages; the existing passing suites do not override this
concrete diagnostic or certify a full gate.
