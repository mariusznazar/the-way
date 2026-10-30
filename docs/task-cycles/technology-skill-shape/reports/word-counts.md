# Words read on the five routes

Words are whitespace-separated tokens of each whole file (`len(text.split())`), Markdown syntax and front matter included. Before is `525cde1dd53c474f56ea0ece289cb60e868aa90d`, after is the task worktree. Each file counts once per route. The script is `.runs/task-cycles/technology-skill-shape/checks/word_counts.py`, run as `python -B .runs/task-cycles/technology-skill-shape/checks/word_counts.py <output>`; it also asserts that the template, the two sections of `way_of_working.md` and the four files of the critique instruction have the same word counts at `525cde1` and in the worktree.

How a section's bounds were taken: from its heading line, included, to the line before the next line that begins with `## ` and stands outside a code fence, or the end of the file. The fence rule matters for `definition_template.md`: its form block and its example show the headings `## Technology` and others inside code fences, and a search of the first line equal to the heading finds the form block and counts 2 words, which the script rejects (it asserts that exactly one heading stands outside the fences). "How a skill asks" and "Reading the foundation" have no fenced headings.

Counting rule of To do 5, as applied:
- The template (whole), the section "How a skill asks" and the section "Reading the foundation" are a fixed addition to each leader route, once, before and after.
- The critique instruction is counted on every leader route before the rebuild, and after it only on the two routes with step 2 (a new list with open choices, a resume with open choices). It is read when the first critique comes (To do 3).
- The research agent reads before the rebuild the whole old `SKILL.md`, after it `research.md`; the section "Technology" of the template is a fixed addition of this route, before and after.

## Words

| Route | Before | After | After minus before |
|---|---:|---:|---:|
| leader, new list, no open choice | 6628 | 5111 | -1517 |
| leader, new list, open choices | 6628 | 6828 | +200 |
| leader, resuming, open choices | 6628 | 6455 | -173 |
| leader, resuming, no open choice | 6628 | 4738 | -1890 |
| research agent | 3276 | 1621 | -1655 |

Files of the skill, words each:

| File | Words |
|---|---:|
| project-level/technology/SKILL.md at 525cde1 | 2122 |
| project-level/technology/SKILL.md | 475 |
| project-level/technology/start.md | 314 |
| project-level/technology/list.md | 373 |
| project-level/technology/running_product.md | 178 |
| project-level/technology/settle.md | 886 |
| project-level/technology/research.md | 467 |
| project-level/technology/close.md | 96 |
| sum of the seven files after | 2789 |

Fixed addition of the leader routes, once:

| Part | Words |
|---|---:|
| project-level/definition_template.md (whole) | 2975 |
| elements/common/way_of_working.md section "How a skill asks" | 208 |
| elements/common/way_of_working.md section "Reading the foundation" | 492 |
| sum | 3675 |

Critique instruction:

| File | Words |
|---|---:|
| elements/common/critique/SKILL.md | 322 |
| elements/common/critique/prepare.md | 145 |
| elements/common/critique/check.md | 294 |
| elements/common/critique/settle.md | 70 |
| sum | 831 |

Fixed addition of the research agent: section "Technology" of project-level/definition_template.md: 1154 words.

Conditional, not in the rows above: list.md if the look adds an item or the human adds or changes one (resuming routes): +373 words.

## Files read on each route

Before, every leader route: `project-level/technology/SKILL.md`, `project-level/definition_template.md` (whole), the section "How a skill asks" and the section "Reading the foundation" of `elements/common/way_of_working.md`, `elements/common/critique/SKILL.md`, `prepare.md`, `check.md` and `settle.md` beside it. Research agent: `project-level/technology/SKILL.md` and the section "Technology" of `project-level/definition_template.md`.

After:
- leader, new list, no open choice: `project-level/technology/SKILL.md`, `start.md`, `list.md`, `running_product.md`, `close.md`, and `project-level/definition_template.md` (whole), the section "How a skill asks" and the section "Reading the foundation" of `elements/common/way_of_working.md`.
- leader, new list, open choices: `project-level/technology/SKILL.md`, `start.md`, `list.md`, `running_product.md`, `settle.md`, `close.md`, `project-level/definition_template.md` (whole), the section "How a skill asks" and the section "Reading the foundation" of `elements/common/way_of_working.md`, and `elements/common/critique/SKILL.md`, `prepare.md`, `check.md` and `settle.md` beside it.
- leader, resuming, open choices: `project-level/technology/SKILL.md`, `start.md`, `running_product.md`, `settle.md`, `close.md`, `project-level/definition_template.md` (whole), the section "How a skill asks" and the section "Reading the foundation" of `elements/common/way_of_working.md`, and `elements/common/critique/SKILL.md`, `prepare.md`, `check.md` and `settle.md` beside it.
- leader, resuming, no open choice: `project-level/technology/SKILL.md`, `start.md`, `running_product.md`, `close.md`, and `project-level/definition_template.md` (whole), the section "How a skill asks" and the section "Reading the foundation" of `elements/common/way_of_working.md`.
- research agent: `project-level/technology/research.md` and the section "Technology" of `project-level/definition_template.md`.

## Reading of the numbers

- Choices made for the counts: the leader does not read `research.md` (it gives its path to each agent, `SKILL.md` says so); `running_product.md` is counted on the two new-list routes, which assume a project with behaviour a user sees (the case of the one real run) and on both resuming routes, where `start.md` reads it whenever a list is written; `list.md` is not counted on the resuming routes, which read it only when the look adds an item or the human adds or changes one at the question whether the list still holds, and the line "Conditional" above gives that addition.
- `close.md` is counted on the resuming route with open choices too: that leader ends in the step "Close" once its last wave is written. The leader with a new list and open choices reads more after the rebuild (the longest route) and every other route reads less. The increase comes from the pointers and the one-line introduction of each file, which Question 7 of the task accepts (procedure of every step in a file beside the skill); the research text, which the old file carried for the leader, no longer reaches the leader's reading.
- The counts are of files, not of an agent's behaviour (Question 4); the series script `skill_carry_cost.py` is not run in this task.
