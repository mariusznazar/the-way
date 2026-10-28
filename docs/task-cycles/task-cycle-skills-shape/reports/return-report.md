# Report — return step, task `task-cycle-skills-shape`

**Status:** done with concerns. No entry needed a correction and no entry was written, so there is
no commit. Two concerns lie outside what this step may edit: concern 1 (the product entry point,
`installation/install.py:136`) and concern 2 (a dependency of `task-cycle` that is older than this
change).

## Files and commits

- Files changed: none. Commits: none. Head stays `7369993885567d683ef7b7a8b08933318c21ed4d` on
  `task/task-cycle-skills-shape`, and the worktree is clean. With no commit, the review of the
  return step's range (step 11) has nothing to review.
- Method, read whole from the base copy: `.runs/the-way-base/task-cycle/change/SKILL.md`, and step 11
  of `.runs/the-way-base/task-cycle/skill/SKILL.md:349-364`. I read no element skill, because I
  wrote and corrected no entry.

## Foundation compared with code

| Entry | Compared with | Result |
|---|---|---|
| WAY-125 (changed) | `task-cycle/skill/SKILL.md:61-66` (step 3) and `:124-145` (the handoff paragraph). The tables and pointers of `task-cycle/change/SKILL.md:17-26`, `spec/SKILL.md`, `plan/SKILL.md` and `review/SKILL.md:19-40`. `git grep` across the repository for "what it names, whole", "the files it names", "files it references", "with every file it names" and "read the method" | Matches. Each stage method names its file beside it at the step or variant that needs it. The handoff paragraph says "no handoff tells it to read at the start every file its method names". The only remaining text that says to read every named file is the product entry point (concern 1), and WAY-125's verification does not cover it as written. No correction. |
| WAY-127 (changed) | `agent-instructions/skill_entry_points.py:175-177`, `agent-instructions/test_skill_entry_points.py:53-55`, `.claude/skills/the-way-make-change/SKILL.md:13` and the other 41 entry points (all current, see Checks), `AGENTS.md:9-12` | Matches. The sentence "read a file it names under the same root when the step or variant that names it comes, not all of them at the start" fits the binding sentence and its *complies* line. No correction. |
| WAY-256 (changed) | Every file beside the five skills: `change/{slice,fix,ui_check}.md`, `spec/{design,review}.md`, `plan/too_large.md`, `review/{whole_change,fix}.md`, `skill/{plan_member,spec_review,planning,foundation_step,return_step,blocked_finding,correction}.md`. Also `instruction-files/kind_skill.md:16-21` and the rows of the variant table in `task-cycle/change/SKILL.md:21-26` | Matches. No file beside a skill holds a single instruction behind a pointer. The two single-instruction rows ("whole change" and "correction") are rows 5, 9 and 22 of the example that the task names (To do 5). The parts of `implement-task` that review finding M1 names, step 2 (moving the pin) and step 9 sub-steps 1–5, still stand as they were at `cf11541`, apart from one clause at `:285`. WAY-256 says "Fragments that stand unchanged are not bound by it". So M1 is a layout question, not a mismatch with WAY-256. No correction. |
| WAY-257 | `instruction-files/` unchanged apart from `kind_skill.md` | Matches. No correction. |
| WAY-35 | `kind_skill.md:23-26`, and the exception's wording "would otherwise stand in a file beside the skill" | Matches. A rule of an element's entries still goes to the element's template. No correction. |
| WAY-148 | The handoff paragraph `task-cycle/skill/SKILL.md:124-159`, and `task-cycle/skill/planning.md` ("A slice's handoff") | Matches: the handoff names what the agent reads and copies sections word for word with their address. No correction. |
| WAY-150 | `task-cycle/change/SKILL.md:28-44`, `task-cycle/review/SKILL.md:24-36`, `task-cycle/review/whole_change.md` | Matches. The reviewer of the whole change selects its own reading. Every other agent reads its handoff and names each reach in its report. No correction. |
| WAY-258 | `grep "one instruction" instruction-files/` → `kind_skill.md` only | Matches: the rule stands in one file. No correction. |
| WAY-128 | Its last sentence ("process skills and their entry points answer to WAY-35, WAY-127 and WAY-256") | Still true. No correction. |
| WAY-129 | The changed `AGENTS.md` sentence and the entry points' pointers | The change adds no `@` import. Each pointer names its path in backticks with its condition. No correction. |
| Invariant `skill-entry-points` | `python -B agent-instructions/skill_entry_points.py`. Each entry point leads to its `SKILL.md` in the session's checkout or worktree | Holds. Its test, `gate/test_skills_reach_the_way_sessions.py`, is unchanged. No correction. |
| Part `task-cycle` | `task-cycle/**` covers the 16 new files. I compared the paths of other parts named in `task-cycle/**` at the head with those at `cf11541`: `installation/README.md` 2, `elements/common/way_of_working.md` 2, `product-guidelines/reading.md` 3, a range of `foundations/decisions.md` 1, the same counts at both commits | The change adds no dependency. One older dependency is not allowed by *Depends on* (concern 2). No correction. |
| Part `instruction-files` | `instruction-files/kind_skill.md` | No new file and no new dependency. The part's sentence still holds. No correction. |
| Part `agent-instructions` | `AGENTS.md`, `agent-instructions/skill_entry_points.py` and its test, `.claude/skills/**`, `.agents/skills/**` | No new file and no new dependency. The sentence still holds. No correction. |
| Part `decisions` | `foundations/decisions.md` | The change only edited entries in place. No correction. |

Every `WAY-<n>` that the change's added lines cite in `task-cycle/`, `instruction-files/` and
`AGENTS.md` names an entry of the log, and none of them is withdrawn. I checked this with a loop
over `git diff cf11541..HEAD`.

## Entries written or changed, by kind

- Decisions: none (WAY-125, WAY-127 and WAY-256 were written by the foundation step, `40f0fd3`).
- Invariants: none.
- Environment facts: none. The change rests on no source outside the product that the foundation
  lacks. WAY-256 already rests on `single-rule-compliance` and `instruction-density-accuracy`. The
  task's sources (the series note, the example and the series measure) are private task material,
  not sources the code cites.
- Glossary terms: none. "Fragment", "pointer", "variant" and "entry point" keep their usual meaning,
  as WAY-256 and WAY-127 already use them. "Foundation step" and "return step" are used as their
  entries give.
- Part map: none.
- Projected entries: none (independent task).
- Rows of *Settlements to record*: rows 1–3 were written by the foundation step (WAY-125, WAY-127,
  WAY-256). The return step adds nothing.
- Choices that bind after the merge (WAY-36): none beyond the skills' own text. The variant table
  and the wording a handoff uses to name a variant are text of `implement-task` and `make-change`,
  and they follow WAY-125 and WAY-256.

## Concerns

1. **The product entry point, `installation/install.py:136`. Read only, no edit (handoff).** In a
   product, a session that opens a the-way skill through its project skill reads: "Read
   `.the-way/<path>` in full and follow it. Read the files it references inside `.the-way`." This
   sentence says nothing about when to read those files. `installation/README.md:57` describes the
   same entry point: "reads its source skill and referenced files from `.the-way`".
   - My reading against the entries:
     - WAY-127 binds only the-way's own entry points, so this sentence does not breach it.
     - WAY-125 now says that each stage agent reads a file its method names "only when the step or
       variant that names the file comes". In a product, a stage agent that opens its method
       through `the-way-make-change` (or `-review-change`, `-plan-task`, `-write-spec`) gets the
       installer's sentence, which it may follow by reading `slice.md`, `fix.md` and `ui_check.md`
       all at once. For that path, the code no longer matches WAY-125.
     - The handoff of `implement-task` names the method by its path in `.the-way`. An agent that
       reads that path directly does not meet the sentence. So the mismatch depends on how the
       agent opens its method.
     - For the orchestrator, no entry sets when it reads the files beside `implement-task` in a
       product. WAY-125 speaks of stage agents, and WAY-127 only of the-way. The sentence still
       undoes, for the orchestrator, what the move of `implement-task`'s fragments was meant to
       achieve.
   - Why I made no correction: acceptance criterion 1 allows no other Python change, and the
     handoff limits this step to reporting it. Review finding O1 holds the same point as out of
     scope, and it goes to the request's out-of-scope list as step 13 gives.
   - Recommendation: say in the request, beside O1, that the measured cycle on `loop2` runs in a
     product through this sentence until the installer changes. What happens either way:
     - If nothing is said, the measurement after the merge mixes the gain from the new layout with
       agents that may read every file beside a skill at the start.
     - Saying it costs one line in the request.
2. **`task-cycle` names `installation/README.md`, but *Depends on* does not list `installation`.**
   - Where: `task-cycle/skill/SKILL.md:41` and `:43`, step 2, moving the pin: "run the installer from
     that clone as `installation/README.md` gives", and "the removal `installation/README.md` asks
     for".
   - The part map entry `task-cycle` (`foundations/part_map.md:92-100`) does not list `installation`.
   - Age: the reference dates from `4913b08` ("Move a task's pin as the task branch's first
     commit"). This change does not touch those lines.
   - Rule: the part-map template (`elements/part-map/template.md:90-94`) sends such a dependency to
     the human, and *Depends on* is never rewritten to fit the code. So I made no edit.
   - Recommendation: name it in the request's out-of-scope list for the human to place, with
     the two outcomes:
     - The human allows it: `installation` joins *Depends on* of `task-cycle`. This is one line, and
       `foundation_check.py` must still pass.
     - The human does not allow it: an invariant `Violated: yes` stands until step 2 stops naming
       the installer's README.
     - If nothing is done, the map goes on allowing less than the code does, as it has since
       `4913b08`, and nothing breaks.

## Checks

| Check | Command | Exit |
|---|---|---|
| Foundation | `python -B elements/common/foundation_check.py` → `0 errors` | 0 |
| Entry points | `python -B agent-instructions/skill_entry_points.py` → `entry points are current` | 0 |
| Whitespace, worktree | `git diff --check` | 0 |
| Whitespace, the change's range | `git diff --check cf11541..HEAD` | 0 |
| Clean tree | `git status --short` → empty | 0 |

Not run:

- `gate/run_tests.py <directory>`: my corrections touch no directory. The review ran the focused
  runs on `7369993` for `task-cycle`, `agent-instructions`, `instruction-files` and `gate`.
- The whole `gate/run_tests.py`: that run is the orchestrator's (handoff, WAY-160).

## Own-work check

- **The requirement I most likely miss:** text, anywhere in the repository, that still tells an
  agent to read every file a skill names at the start. That would breach WAY-125 or WAY-127 where
  the foundation now says otherwise.
- **The check:** `git grep -n -i "the files it names\|files it references\|and what it names\|what
  it names, whole\|with every file it names\|referenced files" -- . ':!.runs' ':!docs/task-cycles'`,
  and `git grep` for "method.*whole" and "read the method".
- **What it showed:** only `installation/install.py:136` and `installation/README.md:57` (concern 1).
  `instruction-files/SKILL.md:22` says where the files lie, not when to read them. The
  environment fact quotes a source.

## Reaches beyond the handoff

- **The private example `przyklad_make_change.md`**, rows 5, 9 and 22 and "Po przebudowie" (it lies
  in the task's sources folder). Why: to confirm that the correction row of `make-change`, with its
  two single-instruction sentences, is the layout the task names, rather than a breach of WAY-256's
  boundary.
- **WAY-34, WAY-141 and the decisions whose *Scope* names `installation`**, found by searching for
  "project skill", "entry point" and "files it references". Why: to find whether an entry governs
  the product entry point's sentence. None does, apart from what concern 1 gives.
- **`elements/part-map/template.md:86-94`.** Why: the rule for a dependency the code holds that
  *Depends on* does not allow (concern 2).
- **`foundations/environment_facts.md`, the entry `claude-skill-nested-references`, and
  `instruction-files/SKILL.md:174-177`.** Why: the depth of references. In Claude Code, a file
  beside `implement-task` is two levels from the entry point (entry point → `SKILL.md` → file),
  and the fact says Claude may read such a file only in part. This was already true for
  `record_template.md` before the change, and no entry of `task-cycle` sets a depth. So it is not
  a mismatch, only a risk for the measured cycle to watch. The foundation step reported the same
  risk.
- **`task-cycle/record_template.md:132-150`.** Why: to fill the record's *Return step* fields.

## Problems

None observed beyond the concerns above.
