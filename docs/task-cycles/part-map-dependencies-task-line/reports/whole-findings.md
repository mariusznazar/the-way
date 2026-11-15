# Findings to fix — whole-change review of `af76148`

Cut word for word from `reports/review-whole-report.md` (first line `FAIL af7614867a6e477088a7831fc170c4b279b6ba21`): the blocking finding, then the Minor findings within the task that the reviewer did not mark outside the task's scope (WAY-161). M-4 and the two out-of-scope items of that report are not fixed.

### Blocking (Important), within the task

**I-1. The sentence of `project-level` in the part map says the part is not responsible for how a
line is made, which WAY-107 as the change rewrites it, `project-level/task_line.md` and
`project-level/backlog_place.md` contradict for the derivation of the identifier.**

- Place: `foundations/part_map.md:82-91` (the sentence of `project-level`): "…and for when
  the line of a task in the product's backlog is written, given its dependencies and moved to ready,
  but not for how a line is made, which the rules of the task place say (WAY-107)."
- What is wrong: after the change, WAY-107 (`foundations/decisions.md:294-314`, the second paragraph) says "The one part
  of a line that the-way gives is the derivation of a task's identifier from its plan and its name
  in the plan", and that derivation is written in `project-level/task_line.md` ("The identifier"),
  a file of this part (`project-level/**`). `project-level/backlog_place.md:18-20` says so too:
  "gives the derivation of a task's identifier from its plan, the one part of a line the-way gives,
  but not how a line is written". The part-map sentence has no such qualification: it says the part
  does not answer for how a line is made, and that the rules of the task place say how. A reader of
  the map who asks which part answers for the identifier of a line, so that a dependency can name a
  task before its line exists, is told none does. The sentence restates WAY-107 more broadly and
  without its qualification, which WAY-263 grades Important for an entry the change writes. The
  task's own item 7 words the exclusion as "a nie za to, jak powstaje", so the defect comes from
  the task's wording; the task's item 7 does not forbid the qualification, and the settlement of
  row 6 (the-way gives the derivation) requires it.
- Why it matters: the part map is what the return step and the next author compare with the code;
  a sentence that denies a responsibility the part holds sends a later change to the wrong place or
  leads to the derivation being removed as out of the part's remit.
- Evidence: the three texts above, read side by side; `git grep -n "derivation" project-level`
  finds the derivation in `task_line.md` only, a file of `project-level`.
- Fix, a clause: say that the part gives the derivation of the identifier of a task of a plan and
  that the rest of how a line is made is the rules of the task place's.
- Slice: not applicable (one commit, no plan).
**M-1. The new sentence in `elements/part-map/template.md` restates the glossary entry in other
words and leaves part of it out.**
`elements/part-map/template.md:91-94` says "A dependency of a part is any reach of it to another
part, not only an import, so *Depends on* names also a part whose skill the part calls or whose
file, form of a file or tag of git its script reads". The entry `dependency of a part`
(`foundations/glossary.md:37-41`) lists a skill that calls "a skill or a file" of the other part,
a script that reads a file, "the form that file is written in, a path or a git tag". The template
omits the path of a file and the file a skill calls. The first clause, "any reach", carries the
meaning, so this is not graded as WAY-263 does for a restatement that changes it; but two lists of
one definition drift. A reference to the term instead of a second list would keep one definition.

**M-2. `blocked-request-line` joins two rules in one sentence.**
`foundations/invariants.md:378-386`: the wording stands in backticks in two files of `task-cycle`,
"and" `task-cycle/record_template.md` has a line beginning with the label. The invariants template
("The sentence") gives one rule to an entry and judges a joined pair as two (WAY-12). A reword of
the label and a reword of the wording are separate breaks. The content agrees with the code and the
test checks both, so Minor (WAY-364). The task's row 2 asks for the first rule only; the label rule
is the author's addition (author's report, Choice 9), for which a reason stands.

**M-3. Bare `dependency` / `allowed dependencies` in running text of the part map's decisions and
skills does not use the glossary term as it is written.**
The term is `dependency of a part` (`foundations/glossary.md:37`); WAY-93 heads an entry with the
term "as the foundation writes it in running text" and WAY-97 says a sentence relies on a term by
using its word. The text writes "a dependency the code holds that the part map does not allow"
(WAY-225, `foundations/decisions.md:2488-2491`, whose binding sentence the task keeps unchanged),
"the allowed dependencies" (`foundations/part_map.md:4`, `elements/part-map/skill/SKILL.md:3,40`)
and the like; only `elements/part-map/template.md:91` writes the term in full. A reader who takes
the field's meaning of the bare word, imports or packages, reads WAY-225 as about imports only, the
very reading the task's Need names. The author's reason for the longer term (Choice 1) is sound
(the bare word also means a task's and a package's dependency); the gap is that no sentence outside
the template uses it. Not graded higher because the sentences are in the context of the part map,
which narrows the reading, and the glossary-entry rule of section 3 gives Minor where no sentence
is cited that a reader reads wrongly in its context.
