# Return step report — precedence-between-decisions

**Status:** done. No commit: nothing that no longer matches was found that the return step corrects.
Head stays `baa07f4`; the working tree is clean.

## Return step (record items)

- **Foundation compared with code.** Compared with the files of the range `294af7f..baa07f4`:
  - WAY-25 (changed): its binding sentences, *Verification* and *Rejected* against the five copies:
    `elements/decisions/template.md` (Relations and precedence), `agent-instructions/README.md`
    (Make the change), `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/decide_entry.md`,
    `task-cycle/skill/request_template.md` item 6. All five say the same: never settled silently; where
    what the human accepted gives the outcome and the change may write the decision that prevails, the
    change records it there and the request names it with the passages; otherwise stop and ask. The
    source of the passages is the report of the step that wrote the entry, in both the foundation step
    (`the cycle's`, passages kept in the report) and the request item.
  - WAY-134 (changed): the complying example against `elements/decisions/template.md` (rule on
    *Rejected* of a decision written from a row, unchanged on purpose) and `foundation_step.md`
    (`unknown` where the source keeps none). Agree.
  - WAY-293 (changed by the fix, one word "silently"): agrees with WAY-25.
  - Named by the task, read: WAY-30 (a change to a decision is approved with the task document; the new
    WAY-25 route rests on "what the human accepted", which is that approval), WAY-114 (the route to the
    human at the merge, repeated in WAY-25 and in request item 6). Found by the search: WAY-26, WAY-32,
    WAY-172, WAY-268 say why a precedence is recorded or that without one nothing chooses between two
    decisions; the new text does not contradict them.
  - Searched again the whole repository for the old rule ("stops the work", "colliding with no
    precedence", "a human records the precedence"): no place states it any more except the clause
    "otherwise" in the new wording.
  - Result: nothing no longer matches.
- **Decisions.** None to write. The task's *Settlements to record* is `none`; every meaning of the change
  was settled in the task document's questions and is carried by edits of WAY-25 and WAY-134 already made.
  No choice binding after the merge is left that has no entry: the choices the author reported (a
  complying example for the record path, the `the cycle's` mark for a recorded precedence) are wording
  of WAY-25's own rule, not separate rules.
- **Invariants.** None written; no rule that the task, a decision or the human sets as an invariant.
  `foundation-change-merge-route`, `element-directory-contents`, `return-step-record`,
  `skill-rule-source` and `repository-file-location` are not touched by the change in any way that
  makes them false (no file added or moved, the skills still name their template and
  `elements/common/`). `derived-file-content`: no skill description changed, so no generated entry point
  is stale (the `agent-instructions` tests pass at the head of the whole gate run you report).
- **Environment facts.** None: the change rests on no source outside the product.
- **Glossary terms.** None. The change uses "binding sentence", "entry", "foundation step", "return
  step" in the meaning of their entries; "outcome" and "passages" are ordinary words.
- **Part-map changes.** None. All six changed files lie in `decisions`, `task-cycle` and
  `agent-instructions`; no file is added, moved or left unclaimed; no surface or trust boundary changed.
- **Projected entries.** None; the task carries none.
- **Rows of *Settlements to record*.** None; the section is `none`.

## Sentences of meaning for the entries the change wrote or changed

Neither is written by the return step; they are the entries of the author's change and the fix.

- WAY-25 (`the cycle's`). EN: A collision between two decisions with no recorded precedence is never
  settled silently by the agent; where what the human accepted gives the outcome and the change may
  write the prevailing decision, the change records the precedence there and its request quotes the
  passages that give the outcome for the human to accept at the merge, otherwise the agent stops and
  asks. PL: Zderzenia dwóch decyzji bez zapisanego pierwszeństwa agent nie rozstrzyga po cichu; gdy to,
  co człowiek przyjął, daje wynik, a zmiana może zapisać decyzję, która wygrywa, zapisuje w niej
  pierwszeństwo, a jej PR cytuje fragmenty dające wynik do przyjęcia przy scaleniu, w przeciwnym razie
  agent staje i pyta.
- WAY-134 (`the cycle's`). EN: A decision row whose source keeps only ways that answer another part of
  the question gives `unknown` as the decision's rejected options, with no question to the human.
  PL: Wiersz decyzji, którego źródło zachowuje tylko warianty odpowiadające na inną część pytania, daje
  w odrzuconych wariantach decyzji `unknown`, bez pytania do człowieka.
- WAY-293 (word "silently" in the rationale; no change of meaning). EN: its rationale says the agent that
  meets the collision may not settle it silently. PL: jego uzasadnienie mówi, że agent, który trafia na
  zderzenie, nie może go rozstrzygnąć po cichu.

## Mismatch the review put before the return step: WAY-25 *Scope*

- Found: `foundations/decisions.md`, WAY-25 *Scope* is `decisions, task-cycle`; it does not name
  `agent-instructions`, and `agent-instructions/README.md` carries the rule and cites WAY-25.
- Judgment: it is a mismatch in the sense of WAY-21 (a decision's scope names the parts it governs), but
  not one the return step corrects here, for three reasons.
  1. It is not new: at the base commit the same README paragraph already carried the rule of colliding
     decisions (without the citation) and WAY-25's *Scope* did not name the part. The change reworded the
     paragraph and added the citation; it did not make the paragraph subject to WAY-25.
  2. `return_step.md` corrects what no longer matches the change's files. It does not name a scope
     correction, and adding a part to a decision's *Scope* changes which decisions an agent finds for
     every later change in that part, which the task does not settle (its *Settlements to record* is
     `none`).
  3. The task document names the five copies to bring in line and says nothing about *Scope*.
  I did not edit it. Cost of leaving it: an agent that edits only `agent-instructions` files may not
  find WAY-25 through the part map; the README itself cites it. Recommendation: a separate small task
  (or a remark of the request) to decide whether WAY-25 governs `agent-instructions`; if yes, add the
  part to its *Scope* and check the other decisions whose *Scope* is wider than the files that carry them.

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` (at head `baa07f4`) | 0 (`0 errors`) |

No other check run: no file changed in this step. Not run: the whole gate (done by the orchestrator).

## Searches not found or unclear

- none. The WAY-25 *Scope* question above is a judgment I made, listed in its own section.
