# Applying the settlement of the independent assessment

Worktree `C:\Storage\repos\the-way-wt\m1l5-adoptions`, branch `task/m1l5-adoptions`, from d0f6e5b.
Commit: `3a6e0a6 fix(foundations): Settle the independent assessment of the m1l5 adoptions`.
The branch has no upstream. Nothing was pushed.

Line numbers below are those of 3a6e0a6.

## Changes, row by row

| Row | Change | Where |
|---|---|---|
| 4 | WAY-139's list: "rollback, with how many steps it takes and what happens to the data" became "rollback, with its number of steps and what happens to the data"; "a preview of deployments" stays | `foundations/decisions.md:4182-4188` |
| 6 | WAY-140's first sentence gains: "the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task" | `foundations/decisions.md:4221-4224` |
| 6 | The task-cycle skill's exception now points to that clause: "The one exception is the cycle's own record, which WAY-140 names no effect of the task: …" | `task-cycle/skill/SKILL.md:50-52` |
| 9 | WAY-139 *Rationale*: "reaches the agent when it deploys" became "reaches the agent when it prepares a deployment" | `foundations/decisions.md:4212` |
| 11 (cut 1) | "An action placed before the cycle is done before the task is ready (WAY-124)" left WAY-140's binding part. WAY-124 already holds the rule (3545-3546). WAY-124's *Relations* carry `WAY-140@a9310508` | `foundations/decisions.md:4221-4231`, `:3557` |
| 12 (cut 4) | "and checking the code after the action falls to the round of corrections after it" left WAY-140's *Rationale* | `foundations/decisions.md:4255-4256` |
| 13 | New glossary entry `human action` | `foundations/glossary.md:98-103` |
| 13 | WAY-124 and WAY-140 write the whole term wherever they meant it by "action": WAY-124 *Rationale*; WAY-140's binding part, *Verification*, *Rationale* and *Rejected* | `foundations/decisions.md:3576-3577`, `:4221-4264` |
| 14 | WAY-138's complies example: "each marked as having no source" became "each marked as a hypothesis" | `foundations/decisions.md:4148` |
| 14 | Technology skill step 5: "each marked as a hypothesis with no source" became "each marked as a hypothesis" | `project-level/technology/SKILL.md:120` |
| 14 | Definition template: already said "marked as a hypothesis" (216). No change | `project-level/definition_template.md:216` |
| 15 | Decision template, new bullet beside the *Rationale* rule: "In the decision of a technology choice a project settles, the lacks of the option chosen and the risks the human took with it stand in *Rationale*, each risk marked as a hypothesis, never in *Based on* (WAY-138)." | `elements/decisions/template.md:55-57` |
| 15 | The record-decision skill's projected-mode line now points to it: "… stand where the template's "Decision version" puts them, beside its rule for *Rationale*." | `elements/decisions/skill/SKILL.md:77-79` |
| 19 | WAY-140's second sentence gains: "an effect the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft where the document places no human action in the cycle" | `foundations/decisions.md:4224-4228` |
| 20 (cut 5) | "and give that as the reason" left the technology skill | `project-level/technology/SKILL.md:107` |
| 20 (cut 5) | ", with that given as the reason" left WAY-137's complies example | `foundations/decisions.md:4104-4107` |
| 22 | The binding sentences of WAY-137 and WAY-138 did not change. Their copies in the definition template (203-217) stay as they are | — |
| 23 | Task template form: one line per action with no "or none", then the line `<or, in place of the list, the word none>` | `project-level/task/template.md:47-49` |
| cut 2 | The opening restatement "A human action the task document places in the cycle does not stop the cycle midway either: …" left. Step 4 holds the rule, step 13 the request's content | `task-cycle/skill/SKILL.md:19-21` |
| cut 3 | "nor a decision already written" left step 5 of the technology skill. WAY-138 keeps it | `project-level/technology/SKILL.md:111-113` |

### WAY-140's binding part as it now reads

> A task's effect outside the product's repository — on a server, in DNS, on keys or on an
> external account — is a human action, which the task document names and places before the
> cycle or in it, while reading outside the repository stays with the agent and the cycle's record
> of the request and of the task's state in the backlog entry the product names (WAY-107) is no
> effect of the task. For the human actions placed in the cycle, the cycle does what the
> repository allows and opens a blocked draft request listing them, and the human performs them at
> the request; an effect the cycle finds that the task document does not name joins that list for
> the human to place, and the request opens as a blocked draft where the document places no human
> action in the cycle. The human places each human action while the task is refined, on the
> agent's proposal: before the cycle when the cycle's code needs its effect, such as an account, a
> key or a database, and in the cycle when it uses code the cycle writes, such as a deployment or a
> DNS record pointing to a new address.

The template allows one to three binding sentences, and the guard counts three. The backlog
record stays with the cycle: it is "no effect of the task", so it is no human action. A found
effect goes only so far as the table says: it joins the list "for the human to place". Nothing
says the agent places it or makes it.

## Fingerprints

| Entry | Before | After | Carriers |
|---|---|---|---|
| WAY-139 | — | `2c05fe4d` | none in the repository (`git grep "WAY-139@"` finds nothing) |
| WAY-140 | `d02ede05` | `a9310508` | WAY-124 *Relations* (`foundations/decisions.md:3557`), updated; nothing else |
| WAY-124 | `9eaf23e6` | `9eaf23e6` (binding part unchanged) | none |
| WAY-137 | — | `86b2a30d` (unchanged) | none |
| WAY-138 | — | `414f7dbd` (unchanged) | none |

## Glossary choices (record-glossary-term, decided under the delegation)

1. **The definition**: "A human action is an effect of a task outside the product's repository
   that only a human makes."
   - I kept the given meaning: an effect of the task, outside the product's repository, that only
     a human makes.
   - I left two clauses of the given wording out of the definition. The first is "which the task
     document names and places before the cycle or in it". WAY-96 and the template's "The
     definition" keep a rule out of a definition. Naming and placing are rules that WAY-140 sets
     and could change while the word goes on naming the same thing. The clause would also make
     the definition false of an effect the cycle finds: under row 19 that effect joins the list
     unnamed by the task document.
   - The second is "(WAY-140)". No definition in the glossary cites a decision.
2. **Short form "action"**: the foundation also uses "action" plainly, at
   `foundations/decisions.md:2859` and `:3227`, and in a quotation at `:4057`. Under the template's
   rule for a last word standing for the term (WAY-99), I wrote the whole term "human action"
   wherever WAY-124 and WAY-140 meant the term. I did not rewrite the plain uses. After the change,
   `--uses action` lists only those three plain uses.
3. **Avoid**: `none`. No other word for the same thing stands in `foundations/`, the element
   templates or the Markdown files of `elements/common/`. The short form "action" stands in no
   *Avoid* (template, "Uses and a changed definition").
4. **Not**: `none`. Before the change, the word stood only in WAY-124 (3545, 3567), in this
   meaning.
5. **Glossary**: the-way's own, which is the product's in the-way (WAY-95). Placed in
   alphabetical order between `gate` and `invariant`.
6. **Identifier collision**: none. No entry of the part map, the invariants or the environment
   facts reads "human-action".
7. **Step 4.4, a sentence that said what the word is**: WAY-140's first sentence did. It now uses
   the term ("is a human action") and keeps the requirement. Existing decisions mark a term by no
   sign. They use its word plainly, as WAY-135 uses "open design choice", so I added no mark.
8. **No review of uses**: the entry is new on this branch, so step 4's review of a changed
   definition does not apply.

## Format guard and the decision template

`elements/decisions/format_guard.py` `read_rules` parses the "Decision version" section of
`elements/decisions/template.md`:

- the fields from the entry form;
- the `*X* becomes *Y*` rename;
- the `none`/`TODO` table;
- the binding-sentence count and the forbidden words in "Binding sentences".

The new bullet matches none of these patterns, and the guard reads the template unchanged.
`check_template_change` (invariant `decision-template-change`) needs a new version in the log
whenever the template differs from main. With `--base none` that check is unchecked. At the merge,
the log gains WAY-137 to WAY-140. No test pins the template's prose: `elements/decisions` passes.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | 204 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 81 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 41 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK (holds the critical-flow tests) |
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 10 warnings (5 passed check-by on WAY-03, 21, 52, 55, 69; 5 `<request link>` on WAY-124, 137-140), 5 unchecked |
| `python -B elements/glossary/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 5 unchecked (the `none` options) |
| `python -B elements/glossary/format_guard.py --uses "human action"` | 0 | 19 uses, all in WAY-124 and WAY-140 |
| `python -B .runs/task-cycles/m1l5-adoptions/reports/settlement_check_fingerprints.py` | 0 | every relation of WAY-124, 137, 138, 139, 140 carries the current fingerprint; WAY-140's only carrier is current; 0 failures |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current; no `description` changed |

The test output is in `apply-tests-*.txt` in this directory. The edit script is
`settlement_edit_decisions.py` and the commit message is `settlement-commit-message.txt`. These
are partial checks, not a pass of the full gate.

## Concerns

1. **The glossary definition is narrower than the given wording.** I left the naming and placing
   out (glossary choice 1). If the orchestrator wants the clause in, it conflicts with WAY-96, and
   it is false of an effect the cycle finds.
2. **WAY-140's complies example still checks readiness.** It reads "it is not ready until both
   exist" (`foundations/decisions.md:4239-4240`). After cut 1, readiness is WAY-124's rule. The
   example is not false, but it checks a rule that WAY-140 no longer states. No row named it, so I
   left it.
3. **The new clauses have no example and no motive.** Rows 6 and 19 add clauses to WAY-140 that
   no complies or violates example covers and no *Rationale* explains. No row asked for either.
4. **WAY-140 cites WAY-107 in its binding part but carries no relation to it.** If WAY-107's
   binding part changes, nothing flags WAY-140. The log has precedent for both ways, so I added no
   relation.
5. **Other text still spells out the definition.** `project-level/task/template.md:95-99`
   ("named as an action the human performs, since only a human makes such an effect") and
   `project-level/task/skill/SKILL.md:123` (citing WAY-140 for readiness) do. They lie outside
   the files the glossary rules bind (`foundations/`, element templates, `elements/common/`), so I
   left them.
6. **One line of the technology skill is now short.** Removing the words for row 20 leaves
   `project-level/technology/SKILL.md:107` short. I did not reflow step 5, to keep the diff small.

## Coordinator's rulings on the concerns

Commit: `a683701 fix(foundations): Keep WAY-140's examples and motives to its own clauses`, on
top of 3a6e0a6. Line numbers are those of a683701.

| Concern | Ruling | Change | Where |
|---|---|---|---|
| 1 | accepted as written | none | — |
| 2 | fix | WAY-140's complies example reads "names opening the account and creating its key as human actions before the cycle". "and it is not ready until both exist" is gone | `foundations/decisions.md:4240-4241` |
| 3 | fix | *Rationale* gains "An effect the cycle finds goes to the human like a named one, because the cycle may not make it, and the request is where the human meets it." and "The backlog record is the cycle's own account of its request, not something the task's outcome needs, so it stays with the cycle." | `foundations/decisions.md:4259-4264` |
| 3 | fix | complies gains "the cycle itself adds the request link to the task's entry in the product's backlog". violates gains "the cycle finds that its change needs a key the task document does not name and creates the key itself" | `foundations/decisions.md:4244-4245`, `:4249-4250` |
| 4 | fix | *Relations*: `derives from WAY-107@0ffcebe1` | `foundations/decisions.md:4236-4237` |
| 5 | leave | none | — |

Ruling 2 gave the example wording "as the human's actions". I wrote "as human actions": the
glossary rule above (WAY-97, WAY-99) has WAY-140 write the whole term.

WAY-140's binding part did not change (`a9310508`), so WAY-124's relation stays current.

| Command | Exit | Result |
|---|---|---|
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, the 10 expected warnings, 5 unchecked |
| `python -B .runs/task-cycles/m1l5-adoptions/reports/settlement_check_fingerprints.py` | 0 | 0 failures; `WAY-107@0ffcebe1` ok; `WAY-140@a9310508` at 3557 ok |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK |
| `python -B elements/glossary/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 0 warnings |

The edit script is `settlement_edit_rulings.py`, the commit message is
`settlement-commit-message-2.txt`, and the test output is in `apply2-tests-*.txt`.

## Code review of d0f6e5b..a683701: the five fixes

Commit: `d50f3c0 fix(foundations): Settle the independent assessment: human action as a step,
found effects to the request`, on top of a683701. Its body is a summary paragraph followed by
`commit-record.md`, verbatim from `## Independent assessment`. Line numbers are those of
d50f3c0. This section replaces glossary choice 1 and concern 1 above.

| Issue | Change | Where |
|---|---|---|
| 1 | The definition reads "A human action is a step of a task outside the product's repository that a human performs." It holds no rule | `foundations/glossary.md:100` |
| 1 | WAY-140's first sentence: "… is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and …" | `foundations/decisions.md:4221-4225` |
| 2 | "… a human action the cycle finds that the task document does not name joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle." | `foundations/decisions.md:4225-4229` |
| 3 | "The human places each human action the task document names while the task is refined, …" | `foundations/decisions.md:4229-4232` |
| 4 | Binding part (issue 2) and *Rationale*: "A human action the cycle finds goes to the human like a named one, because the cycle may not perform it, …". "make" became "perform", to fit a step | `foundations/decisions.md:4260-4261` |
| 5 | The task template writes "human action" in the placeholder and throughout the section's rule. The heading `## Human actions` is kept | `project-level/task/template.md:47`, `:95-106` |
| copies | The first sentence's change is carried to the task template's rule ("is made only by a human, through a human action this section names (WAY-140)"), the refine-task skill ("Name under *Human actions* the human action through which a human makes each effect …") and task-cycle step 4 ("An effect outside the product repository is made only by a human, through a human action (WAY-140)") | `project-level/task/template.md:95-97`, `project-level/task/skill/SKILL.md:75-79`, `task-cycle/skill/SKILL.md:71-76` |

The first copy fixes the task template's citation of WAY-140 (`:96-97`) that the review named.
The task-cycle skill's found-effect sentence, its step 13 and the record template already said
"listing that effect", so the issue 2 wording needed no copy there.

**WAY-140 fingerprint:** `a9310508` became `6e564611`. WAY-124's *Relations* carry it at
`foundations/decisions.md:3557`, and nothing else carries it. WAY-139 stays `2c05fe4d` and WAY-124
`9eaf23e6`. WAY-140 keeps three binding sentences.

**WAY-97 substitution check:** I put the definition in place of the term in each of the 21 uses
that `--uses "human action"` lists. Every use reads sensibly:
- "a human action whose effect the code needs" becomes "a step … whose effect the code needs";
- "every human action it places before the cycle is done" becomes "every step … is done";
- "a human action the cycle finds" becomes "a step … the cycle finds".

The only remaining uses of bare "action" in the files the guard reads are its three plain uses
(2859, 3227, 4057).

| Command | Exit | Result |
|---|---|---|
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, the 10 expected warnings, 5 unchecked |
| `python -B elements/glossary/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 5 unchecked |
| `python -B .runs/task-cycles/m1l5-adoptions/reports/settlement_check_fingerprints.py` | 0 | 0 failures; `WAY-140@6e564611` at 3557 ok |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | 204 OK |
| `python -B gate/run_tests.py project-level` | 0 | 81 OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 41 OK |
| `python -B gate/run_tests.py gate` | 0 | 98 OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | current; no `description` changed |

The edit script is `settlement_edit_review.py`, the commit message is
`settlement-commit-message-3.txt`, and the test output is in `apply3-tests-*.txt`.

**Concern:** "foundation step" and "return step" also use the genus "step of a task"
(`foundations/glossary.md:86`, `:177`). There it means a stage of the task's process; in "human
action" it means a human's act outside the repository. Both read as the field reads "step", so I
see no WAY-99 conflict. The independent assessment may still ask whether the two definitions
should name each other (WAY-96, neighbouring terms).

## Ruling on the genus "step"

Commit: `5f6c86f fix(foundations): Define a human action as an act, not a step`, on top of d50f3c0.

- `foundations/glossary.md:100` now reads "A human action is an act outside the product's
  repository that a task needs and a human performs." This replaces the definition the section
  above gives. The genus "act" is no glossary term, and the definition holds no rule (WAY-96).
- **WAY-97 substitution check:** I put the definition in place of the term in each of the 21 uses
  again, and every one reads sensibly:
  - "through an act … that a task needs and a human performs, which the task document names and
    places";
  - "an act … the cycle finds that the task document does not name";
  - "an act … whose effect the code needs";
  - "every act … placed before the cycle is done".
- No binding part changed. Fingerprints stay: WAY-140 `6e564611`, WAY-139 `2c05fe4d`, WAY-124
  `9eaf23e6`.
- WAY-140's *Rejected* keeps its plain "a step the human has to take", which is the everyday
  sense and predates the term.

| Command | Exit | Result |
|---|---|---|
| `python -B elements/glossary/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 5 unchecked |
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, the 10 expected warnings, 5 unchecked |
| `python -B gate/run_tests.py elements/glossary` | 0 | 204 OK |
| `python -B gate/run_tests.py gate` | 0 | 98 OK |

## Re-review: refine-task wording

Commit: `b24c5ad style(project-level): Use the whole term human action in refine-task`, on top of
5f6c86f.

- `project-level/task/skill/SKILL.md:75-80`: the 121-character line is rewrapped. "For each
  action" and "An action placed before the cycle" now read "For each human action" and "A human
  action placed before the cycle".
- `project-level/task/skill/SKILL.md:120-128`: "every action placed and every action before the
  cycle done" now reads "every human action placed and every human action before the cycle
  done". I rewrapped the rest of the paragraph.
- The file now has no bare "action" and no body line over 100 characters.

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py project-level` | 0 | 81 OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | current |
