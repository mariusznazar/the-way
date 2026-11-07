# Return step - find-foundation-entries in the shape of WAY-256

**Status:** done. Nothing needed correcting or writing; no commit. The head is `e9c900a` and the tree is clean, so no counted file changed and the counts stand.

## Foundation compared with code

Compared with the five files of `elements/common/skill/` at `e9c900a`:

- The task's *Decisions in play*:
  - WAY-256: `SKILL.md` keeps the picture of the whole, the caller table, the resume rule, step 3 (one instruction) and the pointers; the procedure of step 1 and of step 2 stands in a file beside the skill each, and each variant's text in a file of its own. No rule of an element's entries moved into a file beside the skill (those stay in the templates, WAY-35). No file beside the skill holds one instruction named by a pointer. A step that names a file does not have it read again where an earlier step did (the variant file is read at step 1 or, for an arrival at a later step without it, before that step). Matches.
  - WAY-265: a variant file that a step's file points to (steps 1 and 2) is named in `SKILL.md` at those steps, with the condition (project definition, task mode). Matches.
  - WAY-257: the judgement table in `reports/assessment.md` shows when each fragment is needed and whether the agent recognises that moment beside each verdict. Matches (a record of the cycle, not a file of the repository).
  - WAY-35: the skill still points to the templates and to `way_of_working.md` for the rules and the way of asking. Matches.
  - WAY-115: the candidate table in both variants has the settlement, kind, source and the concrete choice the next reader would guess; a row without one is rejected; the human cuts before any hand-over; the definition's working table is replaced by the `Candidates:` line at the close. Matches.
  - WAY-134: task mode takes candidates from the task document and the conversation, keeps rows as rows, a settlement that a read entry or a projected entry states is no candidate, the ways not chosen go into the row's *Source*, the cycle writes the entry. Matches.
  - WAY-117: the definition variant leaves the one search of the whole foundation to `define-project` at the readiness gate and writes nothing into the foundation. Matches.
  - WAY-127 and WAY-259: nothing in the change touches an entry point or the installer; `skill_entry_points.py` reports the entry points current; the skill names its files to be read at the step that names them. Matches.
- Part map, entry `elements-common`: responsibility ("the skill that finds entries in a source"), *Files* (`elements/common/**` covers the four new files), *Depends on* (the new files read only templates of `project-level` and `way_of_working.md`, already in the list) and *Trust boundary* (none) all still match. The entry `agent-instructions` is unchanged: no file under `.claude/skills/` or `.agents/skills/` changed.
- Invariants `element-directory-contents`, `skill-rule-source`, `outbound-link-reach`, `derived-file-content`, `foundation-file-kinds`: the first two do not reach this skill (it is not an element's skill and `elements/common/` is not an element directory); the new files hold no link to a private note or an unreachable host (searched for `http`, `C:\` and `Notes/`: no hit); the entry points are current; no file of `foundations/` changed.
- Glossary: the new files use no word in a meaning against its entry. "Variant" and "task mode" are names the base already used or WAY-256 and WAY-265 use without an entry; neither is a word whose field meaning would make a sentence of the product read wrongly (WAY-95), and the words "foundation step" and "return step" are not used in the skill.

## The one search of the whole foundation (WAY-33)

Searched `foundations/*.md` for the skill's name, for `elements/common/skill`, and for "find entries", "candidate table", "working table", "Candidates:", "Settlements to record", "task mode", "projected mode" and "rebuilt". Hits that touch the change: WAY-09 (`elements/common/` holds "the skills that find entries and that critique proposals": matches), WAY-112 (a definition resumes from the candidate table: matches the resume rule, kept as written), WAY-114, WAY-115, WAY-117, WAY-118 (the readiness gate makes the one search: matches the definition variant), WAY-134 and the *Relations* chain from it; WAY-30, WAY-135 and WAY-293 mention "Settlements to record" as a source of the task cycle, not the skill's text; WAY-266 concerns skills of guidelines and the sentence on `refine-task` steps 1 and 2, not this skill. No entry names a section, a step number or a file of the skill that the change moved, and no entry waits for something this change brings (WAY-37). No finding.

## Written or changed

- Foundation compared with code: matches; nothing differs.
- Decisions written or changed: none
- Invariants written or changed: none (and none for behaviour merely because no invariant covers it)
- Environment facts written or changed: none (the change rests on no source outside the product that the foundation lacks)
- Glossary terms written or changed: none
- Part-map changes: none
- Projected entries and rows of *Settlements to record* written: none (the task carries none: `Candidates: 11 shown, 0 accepted`, no projected entry)
- Entries deferred: none

## Checks

| Command (worktree root) | Exit code | Result |
|---|---|---|
| `git status --short` | 0 | empty; head `e9c900a` |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/verify_counts.py` | 0 | 0 problems; task route 1397 / 3554 / 2438 words, definition route 1546 / 4391, five files 2021 |

Not run: the whole gate (the orchestrator runs it on `e9c900a` in a separate checkout).

## Searches not found or unclear

none
