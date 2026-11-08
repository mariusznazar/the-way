PASS 78c32c7f02e6b6b3148913441a0a3ad58d038a03

# Review of the whole change — technology-choices-as-text

Range `a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5..78c32c7` (one commit, 9 files, +94/-57). `git rev-parse HEAD` is `78c32c7f02e6b6b3148913441a0a3ad58d038a03`, the head given. Worktree clean (`git status --short` empty). Route: one author, no spec, no plan, no slices. Trust boundary: none (markdown only; `readiness_check.py`, `plan_check.py`, `plan_state.py` not in the diff). Irreversible operation: none. No reserved choice is taken (no language, framework, library, store, login or host is settled by the change).

Counts: blocking 0, Minor 4 (all within the task, none out of scope), out-of-scope 0.

## Findings

### Critical
none

### Important
none

### Minor

1. `foundations/decisions.md`, WAY-123 binding sentence 3 (`...a fresh agent has checked, in the message as first shown, that no option stands there...`). The phrase "as first shown" reads as if the message had already been shown to the human, while the same sentence says the check comes before the wave reaches the human. Row 2 says "the check sees only the first message" (the first of the messages, the follow-ups being later); "as first shown" renders that, but ambiguously. Evidence: sentence read against `project-level/technology/settle.md:46-48`, which gives the critique agent "the whole message" before "Then show". Suggested: "in the first message, before it is shown". Within the task (row 2 wording). Not blocking: the Verification line "the first message reaches the human before a fresh agent has checked it" and `settle.md` fix the order, so no reader would do the wrong thing.

2. `foundations/decisions.md`, WAY-123 *Rationale*: "keeps the message short enough to read" and "the one line for each of the others, and for those left out, keeps what was set aside in view". Neither reason is in the task. Q1 gives the cost "wiadomość jest dłuższa" and, in *Not chosen*, "najdłuższa wiadomość" for the table-plus-paragraph variant, which supports the first as an inference; no source gives a reason for keeping the lines of the options left out (row 1 only says they stay). Under the task's source discipline the second reason is the author's addition. The *Verification* line "every option of a choice, those that do not decide it too, is described at full length" and the *Verification* "the first message reaches the human before a fresh agent has checked it" are likewise derived, not stated, by row 1 and row 2; both follow directly from their rows, so I take them as legitimate. Suggested: drop the "keeps what was set aside in view" clause. Within the task.

3. `foundations/decisions.md`, WAY-123 *Rationale*, last sentence: "since the agent that checks sees only the first message, a word of a later follow-up goes unchecked". The template (`elements/decisions/template.md`, *Rationale* and *Rejected*) bars prose that tells "what the process's own tools do or lack today". This is the cost the task itself names (Q1), so it is within the task; it is also close to describing the checker's reach, and `settle.md` gives that same agent the document as well (the author's report names this). Judged Minor because the sentence is the task's own stated cost and `foundation_check.py` passes.

4. Whitespace churn and line length. Added lines of 101 to 113 characters in `foundations/decisions.md` (WAY-123 binding, *Verification*, *Rejected*; WAY-138 *complies*; WAY-267 and the later *Rationale*), `project-level/lead/skill/SKILL.md:133` area, `project-level/task/skill/orchestrated_mode.md:26` area and `project-level/task/template.md:42` (113). The repository states no line width and four old lines also exceed 100, so this is polish. In WAY-165 *violates* the author also re-wrapped a neighbouring unchanged clause ("an approved definition is sent back to the step ... middle of a game") while inserting its new violates example; no meaning changes. Within the task.

## Against the task

To do:

- Point 1: the sentence at `project-level/technology/settle.md:48-53` stands word for word (compared by reading, and the author's scratch check also found it). Met.
- Point 2: the added text "and any option shown by figures or features instead of what it changes for the product, or a word a person who does not know the technology cannot follow without an explanation (WAY-123)" stands after the contradictions clause (`settle.md:46-48`). Met. The author also turned "the table" into "the message" in that clause; point 4 lists `settle.md:46`, so both instructions are followed.
- Point 3: WAY-123 "in one table" to "in one message" (binding sentence 3), "in separate tables" to "in separate messages" (*Verification*), *Rejected* "the tables come one choice at a time" to "the choices reach the human one at a time". The change goes beyond table to message only by the content of rows 1 and 2 (the form of the showing, the fresh agent's check, the *Rejected* variants). I judge that within the task: point 3 plus "Settlements to record" rows 1 and 2 ask for it. The meaning change of an accepted decision (WAY-123) is flagged by the author for the human at the merge; the orchestrator should carry that into the request (WAY-114).
- Point 4: done for `settle.md` (all six listed sites), `task_run.md:84`, `technology/SKILL.md:58`, `definition_template.md:237` and `:255`, `task/template.md:42,134`, `orchestrated_mode.md:26`, `conversation_template.md:101`, `lead/skill/SKILL.md:133`, and in `decisions.md` WAY-138 (three sites), WAY-267 (two), WAY-268 (two, "a message for the human"), WAY-137 and WAY-166. Ordinary tables left alone as the task lists: `reserved_choices.md:22,42`, WAY-268 questions-table hits, `start.md:7`, `definition_template.md:175,270,283`. My own search is below.
  - WAY-137 "the table of consequences scores how well an agent works with each host beside its cost" becomes "the consequences shown to the human score ...". I agree: nothing in `project-level/technology/research.md` or `settle.md` calls the report's comparison a table ("the comparison"), so the table here is what the human gets. Right call.
  - WAY-166 "the table shows the service with no word on whether an agent can use it" becomes "the message shows ...". Same reading, a site of what the human receives. Right call.
- Point 5: the sentence at `task_run.md:55-58` stands word for word, and the replacement of "whatever `list.md` says of the matter it settles" by "though at a definition `list.md` leaves such an item `— open`" is made (`task_run.md:52-54`). Met. The resulting "...holds the choice too, though at a definition ... leaves such an item `— open`: the item opens only on the human's word and then stands `— open`" is as the task gives it.

Questions to settle 1 to 3: settled as the *Answer* fields say (message; option B including the word a person cannot follow; the `task_run.md` correction). *Not chosen* variants are carried into WAY-123 *Rejected* (table, table plus paragraph, the tool-name rule, the check for figures and features alone) with their costs; nothing is invented there.

Settlements to record, rows 1 to 3:

- Row 1 in WAY-123: binding sentence 1 (plain text, words a person can follow, deciding options each by name and by consequence, the others one line each, lines of the options left out) and sentence 3 (one message, one choice after another). The *Rejected* carries the table, the table with a paragraph, and the tool-name rule. Matches the row. Reading "the loss of the comparison of the options across one page" is Q1's cost.
- Row 2 in WAY-123: the fresh agent's check before the wave reaches the human, an agent's judgement, sees the first message only; variant A rejected with its cost. Matches the row (finding 1 for the wording).
- Row 3 in WAY-165: binding sentence 3 extended, *Verification* *complies* and *violates*, and *Rationale* (the reason, "an item that reads as settled gives the human no sign", is the task's *Need*). Matches the row; WAY-267 is untouched except table to message, which row 3 leaves open ("WAY-165 albo WAY-267"). WAY-165 is the entry whose *Verification* already said the item stays held, so it is a defensible home. Still three binding sentences. The rows' meanings are what the entries say, and I found no claim the task does not settle beyond findings 2 and 3.

Against the foundation form: WAY-123 and WAY-165 keep one to three binding sentences, *Verification*, *Rationale*, *Rejected*; no count, no file name, no history of how the decision was reached in prose (the MVP2 story is left out); `foundation_check.py` reports 0 errors.

Contradictions across entries (WAY-33): other entries that mention WAY-123 (WAY-138, WAY-166, WAY-173/WAY-186-area decisions at `decisions.md:5100,5297,5957,7329,8174,8202`, and the `new_tools.md` files of coding, styleguide and testing guidelines) say "by their consequences" and none says the showing is a table. `definition_template.md:237` repeats WAY-123 and says "in one message, one choice after another and in plain text ... a fresh agent has checked that message"; it matches the new text (it omits "as first shown", which is fine). WAY-120 (critique before collective review) is compatible. No remaining entry or file says "table" of the technology showing (search below).

Whether the commit holds only the change: nine files, all of them in the task's reach or found by the sweep (`decisions.md` plus the eight files of `project-level/`); no stray file, no `.runs` file, commit message is English and describes the change.

Own-work check of the author (WAY-164): the requirement it names (point 4, every site and no ordinary table) is the weakest one. Its check was a search of `table`/`tables` in `project-level/` and `foundations/` with every remaining hit read. My own search confirmed it would catch the requirement unmet; I found no site missed.

## Declined to judge

- The candidate tables of `find-foundation-entries` (`decisions.md` WAY-109/WAY-115 area, `project-level/lead/answering.md:54`, `lead/conversation_template.md:95`, `lead/skill/SKILL.md:127`, `task/skill/orchestrated_mode.md:17`): a real table of rows and columns in another step, which the task's list does not touch. Left as is; I agree.
- `foundation-review/with_the_human.md:18` ("Show the full table of the group"): another process, outside the task.
- Whether the critique agent should receive the message as first drafted, or after the author fixes observations: the order of the critique and the fix is outside the task.
- The wording of the author's open question 2 ("tell the agent it sees only the first message, in `settle.md`"): outside the task; the task's point 1 and 2 text is kept word for word.

## Checks I ran

| Check | Command (from the worktree root) | Exit |
|---|---|---|
| Head and range | `git rev-parse HEAD`; `git log --oneline a3206c1..HEAD`; `git diff --stat a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5..78c32c7`; `git status --short` | 0; head matches; one commit; 9 files; clean |
| Foundation form | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| Tests of `project-level` | `python -B gate/run_tests.py project-level` | 0 (271 tests OK) |
| Tests of `elements/common` | `python -B gate/run_tests.py elements/common` | 0 (109 tests OK) |
| Sweep for "table" outside `decisions.md`, outside `.runs` and `*.py` | `git grep -n -i -w -E "tables?" -- . ':!*.py' ':!foundations/decisions.md' ':!.runs'` | 0; every hit is an ordinary table (see below) |
| Sweep for "table" in `decisions.md` | `grep -n -i -w -E "tables?" foundations/decisions.md` | 0; the remaining hits are ordinary tables or WAY-123's own *Rationale* and *Rejected* naming the rejected table |
| Sweep for other forms | `git grep -n -i -E "tabular|columns? of|one table|the table" ...` and `git grep -n -i -E "\bwave\b|shown together|show the options|options by their consequences" ...` | 0; no remaining site of the showing |
| Pairs in the tests | `git grep -n -E "in one table\|table of choices\|the table\|WAY-123" -- '*.py'` | 0; no test checks the wording |
| Line length of added lines | `git diff -U0 a3206c1..78c32c7 \| grep '^+' \| awk ...` | 0; ten added lines of 101 to 113 characters |

I ran no gate and no full suite (the orchestrator does). I did not run `installation` (it needs the cycle's pinned commit, which the author found to fail while it committed during the run, and the change touches nothing it reads).

## Reaches beyond the dispatch (section 1)

- `elements/decisions/template.md`: the entry form (binding sentences, *Rationale* and *Rejected* rules); to judge the entries.
- `decisions.md` WAY-123, WAY-137, WAY-138, WAY-165, WAY-166, WAY-267, WAY-268: read whole, to judge the changed entries and their sites. WAY-113 and WAY-120 are cited in the task's *Decisions in play* and I used their quoted sentences there; I did not read WAY-113 and WAY-120 whole.
- `project-level/technology/start.md` (whole), for "as `start.md` gives" in point 5.
- Search of the repository for the showing in words other than "table" and for citations of WAY-123 (above), to find contradictions.
- `foundations/part_map.md`, `invariants.md` and the guidelines of the parts: not read whole. The change touches only prose and decisions of `project-level` and `decisions`; no invariant is changed (no invariant test named), and the product-guidelines of the-way (`product-guidelines/*/new_tools.md`) cite WAY-123 without the word table.

## Searches not found or unclear

- Task point 4 gives line numbers of `decisions.md` at 52889bc; at base `a3206c1` they have moved (the author also says so). I found every site by heading and quoted words; nothing was missing.
- "Row 2: the check sees only the first message": unclear whether that means the first of the messages or the agent receiving nothing but the message. The author took the first meaning; `settle.md` gives the same agent the document too, so the first reading fits. Finding 1 is about the resulting wording.
- No place found where the task says why the lines of the options left out stay (finding 2). It is a thing the task states, but without a reason.
- Invariants and the part map for `project-level` were not searched for a rule on the form of the showing; I judged the change against the decisions, which hold the matter, and found none.
