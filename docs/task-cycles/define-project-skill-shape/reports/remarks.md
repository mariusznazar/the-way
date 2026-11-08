# The human's remarks on the request — correction 1

Request: https://github.com/mariusznazar/the-way/pull/85, head `a0c56bb` (the code's last commit
`09b0dd0`). The remarks were given in the conversation with the orchestrator on 2026-11-08; they
bind.

## The remark, in the human's words

"a wiesz co, może byś naniósł te 6 drobnych propozycji jeszcze w ramach tego PR'a"
("you know what, maybe you could apply those 6 small proposals within this PR as well")

The orchestrator answered that proposals 2 and 3 carry the verdict "keep" (nothing to apply), that
proposal 4 in full changes WAY-118 and `project-level/definition_template.md`, and that proposal 6
reaches six other skills, not four; and asked which to apply. The human chose the option, word for
word: "1, 5, 6 + 4 w skillu (Recommended)", described as: "Usunąć zdanie orkiestratora, pełna
ścieżka szablonu, „named below…” w 6 innych skillach, „the readiness gate” tylko w plikach tego
skilla. Decyzja WAY-118 i szablon bez zmian (zostaje drobna niespójność słów z nimi)."

## What the correction makes

The proposals stand in `.runs/task-cycles/define-project-skill-shape/reports/assessment.md`,
section 4. This remark widens task To do 3 ("only `project-level/skill/`") for proposal 6 alone.

1. **Proposal 1.** Remove from `project-level/skill/delegated_mode.md` the sentence "The project
   orchestrator may make the initial text edit only when that full text is already before it and
   needs no other definition-section or foundation reading; otherwise it delegates the edit." The
   next sentence ("A subagent always performs step 7, including the whole-foundation collision
   search and all checks.") stays, as the proposal says; make the paragraph read on without it.
2. **Proposal 5.** In `project-level/skill/SKILL.md`, name the template as
   `project-level/definition_template.md` where it now stands bare (the proposal names `:13` and
   `:45`); any other bare mention in the skill's files beside it, the same way.
3. **Proposal 6.** In each other skill of the-way whose `SKILL.md` has files beside it and keeps
   "each skill named below", reword to "each skill named below or in the files beside this skill",
   as `project-level/skill/SKILL.md` now reads. Candidates found by `grep -rl "each skill named
   below" --include=SKILL.md`: `elements/common/skill/SKILL.md`, `product-guidelines/coding/SKILL.md`,
   `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md`,
   `project-level/plan/skill/SKILL.md`, `task-cycle/plan/SKILL.md`. Apply it only where a skill
   named in a file beside that `SKILL.md` makes "below" too narrow; say for each candidate which
   way you went and why. Change nothing else in those files; their `description` stays.
4. **Proposal 4, inside this skill only.** In the files of `project-level/skill/`, where "gate"
   means the readiness gate, write "the readiness gate" (or "readiness gate" where the grammar
   needs it), so that no use stands against the glossary's "gate" (the one command that runs all
   tests). Fixed names stay as they are: the heading text "Delegated definition change and gate"
   (task To do 2 keeps it), "gate record" as the definition template names its section, and any
   quoted name of a section, field or file. Decision WAY-118, `project-level/definition_template.md`
   and `foundations/glossary.md` stay unchanged.

Nothing else changes; proposals 2 and 3 are kept as their verdicts say. After the last change to a
counted file, bring `assessment.md` (proposals now applied, the new places), `word-counts.md` and
the figures of the reports up to date with the author's scripts, and rerun them.
