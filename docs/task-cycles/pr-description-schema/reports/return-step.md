# Return step report — pr-description-schema

**Status:** done

Change under the return step: `f45ca40..4327974`, reviewed `PASS 4327974`. Return step commit:
`e6f24b0` (`foundations/decisions.md` 3+/3−, `foundations/environment_facts.md` 6+/0−,
`task-cycle/skill/SKILL.md` 6+/5−, `task-cycle/skill/blocked_finding.md` 5+/5−).

## What I compared

- **The entries the change writes or changes, against the files:** WAY-286 to WAY-292, WAY-114,
  WAY-134 and WAY-10, and the corrections to WAY-161, WAY-33, WAY-126 and WAY-97. I compared them
  with `task-cycle/skill/request_template.md`, `task-cycle/request_check.py`, `SKILL.md` steps 12
  and 13, `foundation_step.md`, `correction.md`, `reserved_return.md`, `blocked_finding.md`,
  `record_template.md` and `agent-instructions/README.md`.
- **The entries the task names, against the template:** WAY-03, WAY-49 and WAY-51 (item 7 and
  *Foundation entries*); WAY-140 (item 3 and its variant); WAY-161 (two separate lists); WAY-162 and
  WAY-163 (**Blocking findings left**, *Cost* so far, and the variant naming what did not run);
  WAY-219 and WAY-164 (*Checks* and item 4); WAY-227; WAY-256 (where the template stands, and the
  steps that name it); WAY-261 (*Checks*, findings outside the scope, and the part-recovery rule
  kept in step 13); WAY-269 (the reserved variant, *Foundation entries* `none`).
- **The entries the foundation search found, against the template:** WAY-160 and WAY-274.
- **The part map of the touched parts against their files:** `task-cycle`, `agent-instructions`,
  `decisions`, `elements-common` and `glossary`. The new `task-cycle/request_check.py`,
  `task-cycle/test_request_check.py` and `task-cycle/skill/request_template.md` fall under
  `task-cycle/**`. The part's responsibility ("the steps a task runs through and the review its
  change gets along them") covers them. The script reads two files the cycle writes and runs
  nothing, so it is no trust boundary, and no one outside a product relies on its command, so it
  is no surface. No other part entry changes.

## Mismatches and their corrections (all in `e6f24b0`)

1. **The template's collapsed block rests on a host behaviour the foundation did not hold.** WAY-288
   says the top part stands again "in a collapsed block", and its rationale says the block "stays
   collapsed, so the request opens in English for every other reader". If GitHub stopped
   collapsing `<details>`, that decision would be called into question. The new environment fact
   **github-collapsed-section** records it, from GitHub's docs page on collapsed sections. I checked
   both quoted passages word for word, markup dropped, on the live page and on the closest existing
   archived copy, 2026-10-10, found through the CDX index of captures. WAY-288's *Based on* now
   names it.
2. **WAY-292 said more than the script does** (the reviewer's M-5 observed it). The script holds the
   block to `none` only where it can judge the task document as English, which needs at least 20
   words in its title, *Need* and *To do*. WAY-292 now reads: "the form check, wherever it reads the
   task document as English, holds the block to `none`". WAY-292 was written from the spec, not from
   a row, so its wording is the cycle's to correct. WAY-290 has the same limit, but it is a row-6
   entry written whole, and "checks … the collapsed block in the task document's language" still
   names what the script checks, so I left it.
3. **The steps that use the template did not all name it** (WAY-256: a file several steps consult
   is named by each step that uses it). The 9.4 stop, step 12 and `blocked_finding.md` said only
   "as step 13 gives". Each now names `task-cycle/skill/request_template.md`. Step 13,
   `correction.md`, `reserved_return.md` and `foundation_step.md` already named it.

Holds, with no change:
- WAY-286 to WAY-291, WAY-114, WAY-134 and WAY-10, against the template and the script.
- WAY-160: the gate's command and exit code stand under *Checks*.
- WAY-274: the concern stays as M-3 and my first report give it. It is no mismatch with the code,
  since the item stands in the diff and under *Technical changes*.
- M-4: `return_step.md` does not ask for the mark. That is a gap in a file of the collective task's
  area, not an entry that fails to match. The marks of this step's entries stand below.

## Entries written or corrected by the return step

| Entry | Mark | English meaning | Polish meaning |
|---|---|---|---|
| github-collapsed-section (new fact) | the cycle's | In the Markdown GitHub's web interface shows, what stands inside a `<details>` element stays collapsed until the reader expands it. | W Markdownie, który pokazuje GitHub, treść elementu `<details>` jest zwinięta, dopóki czytelnik jej nie rozwinie. |
| WAY-288 (*Based on* gains the fact) | row 3 | The description is in English, and its top part stands a second time, in the task document's language, in a collapsed block; it now names the fact that the block stays collapsed on GitHub. | Opis PR-a jest po angielsku, a górna część stoi drugi raz w języku dokumentu zadania w zwiniętym bloku; decyzja wskazuje teraz fakt, na którym się opiera: GitHub zwija taki blok. |
| WAY-292 (binding sentence corrected) | the cycle's | Where the task document is in English, the block holds `none` instead of a second English copy of the top part, and the form check holds it to `none` wherever it reads the task document as English. | Gdy dokument zadania jest po angielsku, zwinięty blok ma `none` zamiast drugiej, angielskiej kopii górnej części, a skrypt tego pilnuje wszędzie tam, gdzie rozpozna dokument zadania jako angielski. |

The meaning of WAY-288 does not change: only its *Based on* field gains the fact. It stands in
*Foundation entries*. The new fact and the corrected WAY-292 stand in *For you to decide*, item 6.

## The record's *Return step*

- Foundation compared with code:
  - compared: the entries the change writes or changes (WAY-286 to WAY-292, WAY-114, WAY-134,
    WAY-10, WAY-161, WAY-33, WAY-126, WAY-97), those the task names, those the search found
    (WAY-160, WAY-274), and the part map of `task-cycle`, `agent-instructions`, `decisions`,
    `elements-common` and `glossary`;
  - no longer matched: WAY-288 rested on an unrecorded fact; WAY-292 said more than the script
    checks; three steps did not name the template (WAY-256);
  - all three corrected in `e6f24b0`.
- Decisions written or changed:
  - written: WAY-286, WAY-287, WAY-288, WAY-289, WAY-290, WAY-291, WAY-292;
  - changed: WAY-114, WAY-134, WAY-10;
  - corrected: WAY-161, WAY-33, WAY-126, WAY-97;
  - by the return step: WAY-288's *Based on* and WAY-292's binding sentence.
- Invariants written or changed: none.
- Environment facts: github-collapsed-section, the GitHub docs page on collapsed sections, read
  2026-11-05.
- Glossary terms: none. "Top part", "lower part" and "collapsed block" read in their plain meaning,
  and no term is used against its entry.
- Part-map changes: none.
- Projected entries written whole or in part: none.
- Rows of *Settlements to record* written: row 1 WAY-286; row 2 WAY-287; row 3 WAY-288; row 4
  WAY-114, WAY-134 and WAY-10; row 5 WAY-289; row 6 WAY-290.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py .` (after the fact, WAY-288 and WAY-292) | 0 | 0 errors |
| `python -B elements/common/foundation_check.py .` (after the line reflow) | 0 | 0 errors |
| `python -B gate/run_tests.py task-cycle` | 0 | OK |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| manual: both passages of github-collapsed-section searched word for word, tags dropped and whitespace collapsed, in the live page and in the archived copy of 2026-10-10 (scratch script on `curl` downloads) | — | all four found |

Not run: the full gate, which is the orchestrator's.

## Reaches beyond the handoff

- `elements/environment-facts/skill/` (`SKILL.md`, `read.md`, `decide_entry.md`, `draft.md`,
  `write.md`) and `elements/environment-facts/template.md`, to write the fact.
- `reports/whole-review.md` (M-3, M-4) and `reports/whole-review-2.md` (M-5), read to compare those
  findings' observations with the entries.
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections
  and its CDX index on web.archive.org, for the fact's source.

## Searches not found or unclear

none
