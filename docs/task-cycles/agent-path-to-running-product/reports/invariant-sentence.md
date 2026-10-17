# Invariant sentence report — `project-technology-record`

Status: done. Commit `4c251dc` on `task/agent-path-to-running-product` (parent `596a660`), not
pushed. `.runs/` not staged.

## Inputs and versions

- Worktree `C:/Storage/repos/the-way-wt/agent-path-to-running-product`, started at `596a660`; task
  base `77c8a8b`.
- Read whole: `.claude/skills/the-way-record-invariant/SKILL.md`, `elements/invariants/skill/SKILL.md`,
  `elements/invariants/template.md`, `elements/invariants/examples.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md`.
- Decisions (whole entries): WAY-121/1 (`d0b060e5`, recomputed), WAY-165/1 (`a179dbe4`, recomputed),
  WAY-118/1, WAY-108/1, and WAY-56/1 (what one sentence may join).
- Current entry `project-technology-record/1` (`foundations/invariants.md:2021`), its neighbours
  `project-definition-form/1`, `project-readiness-gate/1`, the `project-plan-*` entries; part map
  `project-level` (`foundations/part_map.md:96-124`).
- Author report sections "(a)"–"(d)" and "What the decisions now require of
  `project-technology-record`" (`author-foundation.md`), weighed as input.
- `project-level/definition_template.md:148-185` (Technology section form today).
- Orchestrator rulings C6 (fixed English marks `logs:`, `interface:`, `development data:` at the
  start of the item), C7 (a second item with the same mark is not stopped), C8 (row 5 holds wherever
  the readiness check runs on a definition, an approved one included).
- Not read, per WAY-69 and the handoff: `project-level/readiness_check.py` and every test. I only
  located, by grep, the lines that cite the entry (`project-level/test_readiness_check.py:404-495`,
  17 citations of `project-technology-record/1`), as step 4.2 of the skill asks.

## Final sentence (verbatim)

> The project readiness check rejects, before approval, a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds, and rejects a definition, approved or not, whose Technology section holds no choice item whose text begins with `logs:`, none whose text begins with `interface:`, or none whose text begins with `development data:`.

Entry fields:

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl` (unchanged; a command the gate runs — the sentence is about a check the product holds, so its method is a test fed input made up for it, WAY-61)
- **Rests on:** none (unchanged; no outside fact decides the sentence)
- **Derives from:** WAY-121@d0b060e5 (was `WAY-121@740c254e`)
- **Part:** project-level (unchanged)
- **Correction:** none
- Heading stays `## project-technology-record/1`. Fingerprint of the sentence: `c6816839` → `7fb7ab2b`.

## Meaning in Polish

Skrypt gotowości projektu, zanim definicja zostanie zatwierdzona, odrzuca ją, gdy sekcji Technology
brak, czyta `none`, ma wiersz niebędący pozycją wyboru, wybór wciąż otwarty albo wybór niewskazujący
ani decyzji `<PREFIX>-<NN>/<version>`, ani pytania z nagłówka decyzji projektowanej — a niezależnie
od tego, czy definicja jest zatwierdzona, odrzuca ją także wtedy, gdy wśród pozycji wyboru nie ma
żadnej zaczynającej się od `logs:`, żadnej od `interface:` albo żadnej od `development data:` (każdy
z trzech braków osobno).

## What changed from the old sentence and why

Old (`77c8a8b`, `596a660`):

> Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds.

1. **Kept, with the same scope "before approval":** every condition the old sentence rejects. These
   come from WAY-121's first sentence ("Before a project definition goes through its readiness gate,
   a step of its own lists … and settles each one") and its rule that the section records the
   decision that holds each choice. Only the position of "before approval" moved (from the opening
   to after "rejects"), so the second clause can carry its own scope.
2. **Added — the three marks, each separately:** "every list also holds three choices of how an agent
   reaches the running product — its logs, its interface and its development data — each an item of
   its own … marked in English by which of the three it is" and "the readiness gate stops a
   definition whose list lacks one of the three" (WAY-121). The marks are the literal forms of
   ruling C6. "none … , or none … , or none …" makes each missing mark a rejection of its own, so a
   check fed a list lacking only one of them must see a rejection (WAY-121 *Verification*:
   "a single item settles the logs and the interface together" violates).
3. **Added — "approved or not" for the three marks:** "a definition approved before the three were
   required goes back to the step and through the readiness gate again once its product moves the
   commit of the-way it pins and the readiness check first runs on it" (WAY-121; ruling C8; author's
   view (d)). The guarantee rests on the readiness check reporting the missing item when it runs on
   an approved definition, so that clause holds whether or not the definition is approved.
4. **Derives from** renewed to `WAY-121@d0b060e5`. WAY-165 is not added: the sentence depends on
   nothing WAY-165 binds (what each of the three asks and how an agent's use of an option weighs is
   level 2). WAY-108 is not added: the English form of the marks is now bound by WAY-121 itself.

Version: `/1` kept. Per `elements/common/rules.md` "Version", with no main branch the guard compares
nothing and every entry stays at version 1. The meaning does change: with a main branch this would be
a raise, never a correction, since tests citing the entry would need different expected values
(a Technology list with no marks now gives a rejection) — WAY-57.

## Choices, rejected alternatives, cost if wrong

| # | Choice | Rejected | Cost if wrong |
|---|---|---|---|
| S1 | Two scopes in one sentence: old conditions "before approval", the three marks "approved or not" | "approved or not" for the whole sentence — goes beyond WAY-121, which sends an approved definition back only for the three; it would make the code reject open or unlinked choices in approved definitions and the check test them, with almost no case in practice (an approved definition whose Technology changed already fails its gate-record fingerprint, WAY-118); keeping "Before approval" for all — contradicts WAY-121 row 5 and ruling C8 | if the orchestrator wants one scope, a wording change of this entry before `main`; the check gains or loses the approved-definition cases of the old conditions |
| S2 | The literal marks `logs:`, `interface:`, `development data:` stand in the sentence | "an item marked as the logs, the interface or the development data", with the form left to the template — the check agent gets only the sentence and its method, and the template is neither a foundation entry nor a decision, so a condition deciding the result stands in the sentence (template "The sentence", WAY-60) | a later change of the mark form in the template needs a change of this sentence too (wanted: the meaning changes) |
| S3 | One entry, identifier kept | a new entry for the three marks (e.g. a separate identifier) — the property is one: the Technology record is complete and settled, the "every field of the template" kind WAY-56 lists as complying; the part map's failure mode and WAY-121's level 1 verification already name `project-technology-record` | if the human reads two invariants here, a split before `main`: a new identifier, the part map and WAY-121's verification gain it |
| S4 | "holds no choice item whose text begins with …" | "has exactly one item marked …" — ruling C7: a second item with the same mark is not stopped; "an item containing `logs:`" — the mark stands at the start of the item (C6) | none expected |
| S5 | "choice item" (the template's top-level items) | any line or nested item beginning with a mark — nested items are no choices of the list (template, WAY-112) | low |

## Other invariants found and how they stand

Searched `foundations/invariants.md` for readiness check, readiness gate, Technology, before approval,
gate record, WAY-108/118/121/165 and the `project-*` identifiers. None changed.

- `project-readiness-gate/1` (`foundations/invariants.md:2010`) — "Before approval, … missing or
  unresolved required section …". WAY-118 is unchanged; its "before approval" stays right for its
  own conditions. No change required.
- `project-definition-form/1` (`:1999`) — sections and `Status:` line (WAY-108). Unaffected.
- `project-plan-form/1`, `project-plan-check/1` (`:2031`, `:2048`) — the plan, not the Technology
  list. Unaffected.
- `project-plan-state-evidence/1`, `project-plan-state-subprocesses/1` (`:2105`, `:2123`) — sentences
  unaffected. Their invariant tests may be affected through fixtures (author's concern 1) — a test
  matter, not a sentence matter; not read by me.
- Outside the invariants file (not edited, for the orchestrator): `foundations/part_map.md:114-117` —
  the failure mode "a definition reaches the breakdown with a listed technology choice still open or
  naming no entry … detected by project-technology-record" stays true; the next one, "a technology
  choice the project needs is missing from the definition's list … not detected", is now partly
  detected for the three ways (author's concern 2, a human's call under WAY-46).
  `foundations/decisions.md:3451` WAY-121 *Verification* level 1 names `project-technology-record` —
  still correct.

## Commands, exit codes, output paths

All from the worktree root, Git Bash, after the edit (identical to commit `4c251dc`).

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `.runs/task-cycles/agent-path-to-running-product/reports/invariant-sentence-guard-invariants.txt` | 0 errors, 0 warnings, 3 unchecked |
| `python -B gate/run_tests.py elements/invariants` | 0 | `.runs/task-cycles/agent-path-to-running-product/reports/invariant-sentence-tests-invariants.txt` | 233 tests OK |
| scratch script with `relation-model/fingerprint.py` (first paragraph under each heading; latest version of each decision) | 0 | `.runs/task-cycles/agent-path-to-running-product/reports/invariant-sentence-fingerprint-links.txt` | decisions: 197 links, 0 stale; invariants: 254 links, 0 stale |
| `git diff --check` | 0 | (none) | no whitespace errors |

Warnings: none. Unchecked, named (all from `none` options):
- identifiers, versions, corrections and the list of violated invariants — `--base none`;
- `TODO` in the entries — `--merge-onto none`;
- the fingerprints the links of the entries carry — `--merge-onto none` (covered by the manual
  recomputation above: 0 stale, the one stale link of the author stage is renewed).
- Note line: no `human_verdicts.md`.

Script: `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/48e1b1a6-9666-4b0d-8a29-8efacfa46bee/scratchpad/fp_links.py` (scratchpad, not kept in the repository).

## Changed file

`foundations/invariants.md` — 2 lines added, 2 removed (line 2023 the sentence, line 2027 *Derives
from*). Line endings LF, as stored (`i/lf`).

## Commit

`4c251dc` docs(foundations): require the three ways to the running product in the technology record
(author address checked: private address). No push.

## For the check agent (skill step after 4.4)

Hand to an agent that wrote neither this sentence nor the code: the entry above, its method
`python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`, and the 17
checks citing `project-technology-record/1` in `project-level/test_readiness_check.py:404-495`
(version unchanged at `/1`, meaning changed). The deliberate break is written from the sentence by the
reviewer of the code, not by the check's author (WAY-69).

## Concerns

1. **Two scopes in one sentence (S1).** The handoff's wording reads either way; I scoped "approved or
   not" to the three marks only, as WAY-121 binds. If the orchestrator wants the old conditions on
   approved definitions too, the sentence changes and so does the code.
2. **"text begins with".** I mean the item's text after its list marker (`- `). A check agent could
   read "text" as the whole line; the template change by the code author should state the form
   (`- logs: <name> — …`) so the two agree. Case and a missing space after the colon are not
   addressed by the sentence: `Logs:` does not count; `logs:Name` does.
3. **Approved-definition mode exists only by the author's account.** "approved or not" assumes the
   readiness check runs on approved definitions (author's (d): the run without
   `--before-approval`). I did not read the code to confirm it, per WAY-69.
4. **Citing tests' fixtures.** Existing tests citing this and neighbouring invariants likely use a
   Technology body with no marks; they will now expect rejections (author's concern 1). Not mine to
   change.
