### Task 2: `task-cycle/skill/SKILL.md` — the light cycle in the skill (spec §4)

**Files:**
- Modify: `task-cycle/skill/SKILL.md:3` (front matter), `:51-55` (step 4), `:83-86` (new section
  before `## Design and plan`), `:88-91` (step 6), `:132-133` (step 9), `:197-198` (step 13) —
  line numbers of `c64a607`; apply the edits bottom-up or by exact text, never by line number.
- Test: none exists for `task-cycle/`; `installation/test_install.py` reads the committed front
  matter.

**Interfaces:**
- Consumes: WAY-13 and WAY-125 as written in Task 1 (cited by number only).
- Produces: the heading `## Light cycle`; the names "light cycle", "full cycle", "executor",
  "switch", "the executor's report", "discarded attempt"; step 4's instruction to record the cycle
  choice "with the reason for each finding you assessed". Task 3's record-template slots name
  the same things.

- [ ] **Step 1: Make the six edits with the Edit tool**

Not changed: steps 1–3, step 5, the foundation-step paragraph, steps 7, 8, 10, 11, 12, 14 and
"Correction after review" (spec §4, last paragraph).

Old text (2a), line 3:

```text
description: Use to take one ready the-way task through autonomous design, planning, implementation, testing, review and a pull or merge request, or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
```

New text (2a) — one line, not wrapped:

```text
description: Use to take one ready the-way task to a reviewable pull or merge request — through autonomous design, planning, implementation, testing and review, or, for a small task that leaves the foundation unchanged, through one agent's implementation, the same checks and one review — or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
```

Old text (2b), lines 51–55 (step 4; line 56 onward unchanged):

```text
4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. Calculate the three sharpness inputs: criticality from
   the touched parts (unknown failure modes count as highest), whether touched files are trust
   boundaries, and whether any operation cannot be undone. Use the full subagent review loop even
   for low criticality. For a trust boundary, add adversarial input checks under WAY-48. Stage but
```

New text (2b):

```text
4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. In the same analysis, choose the light or the full
   cycle as "Light cycle" below gives it, and record the choice with the reason for each finding
   you assessed; once one finding fails, the rest may be recorded as not assessed. Calculate the
   three sharpness inputs: criticality from the touched parts (unknown failure modes count as
   highest), whether touched files are trust boundaries, and whether any operation cannot be
   undone. On the full cycle, use the full subagent review loop even for low criticality. For a
   trust boundary, add adversarial input checks under WAY-48. Stage but
```

Old text (2c), lines 84–86 (the end of the dispatch-contract paragraph and the next heading):

```text
an invariant's check (WAY-69).

## Design and plan
```

New text (2c) — spec §4.3, rewrapped to 100 columns, no word changed:

```text
an invariant's check (WAY-69).

## Light cycle

A task takes the light cycle when the analysis of step 4 finds all three: the task leaves the
foundation unchanged, so the foundation step below would not run for it; one agent can implement
it in about ten minutes; and its implementation needs neither very large files nor very many files
read into context. Every other task takes the full cycle — steps 6 to 9 — exactly as written. The
two cycles differ in how a change is prepared and made, never in the outcome the task has to reach
or the checks run on the finished change (WAY-13, WAY-125); both run inside the foundation route
of step 4. On the light cycle:

- Dispatch one fresh executor with the frozen task, the applicable source paths, the pinned
  foundation and the dispatch contract above. It makes the whole change from the task, without a
  spec or a plan, using Superpowers `test-driven-development` for behavior changes, and commits it.
  Its boundary is the committed change with its focused checks run; it returns before any review.
  It also returns, with its work committed, when the change touches the foundation and when the
  change outgrows a finding of step 4.
- When the change touches the foundation, rule on the touch and record the ruling. The touch is
  simple and obvious when the entry's change follows from the task's required outcome with no
  choice the task leaves open, changes the meaning of no approved decision, contradicts no current
  entry, and writes or changes no invariant or invariant test. On that ruling, record the
  foundation route as changed; the executor then writes the entry through its element's skill, as
  the foundation step below gives an entry the cycle writes, before it continues the code that
  depends on it, and the entry joins the one independent assessment of step 11. Any other touch
  switches the task to the full cycle.
- When the change is made, run step 10 in full. The whole change is its one implementation unit,
  and one Superpowers `requesting-code-review` of the whole change, with the frozen task as its
  requirements, is both that unit's review and the final review: the executor fixes its findings,
  the affected checks run again, and the same reviewer reviews the fix range once. Then continue
  with steps 11 to 14 as written. Where the harness cannot resume the executor after a ruling or
  for fixes, a fresh executor on the same branch, given the task and the ruling or the findings,
  continues in its place.

Switch to the full cycle when the executor, or you from its work, find while the change is being
made or its review findings fixed that it outgrows a finding of step 4 or touches the foundation in
a way that is not simple and obvious. The executor returns a report without code and without a
diff: why the change grew, which files and obstacles it found, and what proved not obvious. Check
that the report holds no code, keep it in `reports/`, and record the attempt's last commit, as a
historical name rather than a link to follow, and the names of the files it changed. Then discard
the attempt, its foundation entries included, by resetting the task branch to the recorded base
commit, record the switch with its reason, and continue at step 6, whose fresh design agent
receives the executor's report beside the frozen task.

## Design and plan
```

Old text (2d), lines 88–91 (step 6; line 92 onward unchanged):

```text
6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. Ask it to use Superpowers `brainstorming`. It
   classifies the task using that skill, then follows its architectural path because this cycle
   requires a written spec and plan for every ready task. Record the classification and this
```

New text (2d):

```text
6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. After a switch from the light cycle, also give it
   the executor's report, as the findings of a discarded attempt. Ask it to use Superpowers
   `brainstorming`. It classifies the task using that skill, then follows its architectural path
   because the full cycle requires a written spec and plan for every task it runs. Record the
   classification and this
```

Old text (2e), lines 132–133 (step 9; line 134 onward unchanged):

```text
9. Use Superpowers `subagent-driven-development`: fresh implementer and reviewer contexts for
   each meaningful plan task, followed by a whole-branch review. Its boundary is the final review
```

New text (2e):

```text
9. On the full cycle, use Superpowers `subagent-driven-development`: fresh implementer and
   reviewer contexts for each meaningful plan task, followed by a whole-branch review. Its
   boundary is the final review
```

Old text (2f), lines 197–198 (step 13; line 199 onward unchanged):

```text
13. The request contains: task goal and relation, source versions, design and plan links, what
    changed and why, test and review evidence with every check that did not run named, and *What
```

New text (2f):

```text
13. The request contains: task goal and relation, source versions, the cycle taken and its
    reasons — after a switch, its reason and a link to the executor's report — design and plan
    links on the full cycle, what changed and why, test and review evidence with every check that
    did not run named, and *What
```

- [ ] **Step 2: Confirm each base text matched once**

Each Edit call fails unless its old text occurs exactly once; six successful Edit calls are the
evidence. Run `git diff --numstat -- task-cycle/skill/SKILL.md`. Expected:
`62 12 task-cycle/skill/SKILL.md`.

- [ ] **Step 3: Check the front matter and line lengths**

```bash
python -B -c "import re;t=open('task-cycle/skill/SKILL.md',encoding='utf-8',newline='').read();fm=t.split('---')[1];print('description lines:',len(re.findall(r'^description: ',fm,re.M)),'front-matter lines:',len(fm.strip().splitlines()));print('CR present:','\r' in t)"
python -B -c "import sys;[print(f'{p}:{i}:{len(l)}') for p in sys.argv[1:] for i,l in enumerate(open(p,encoding='utf-8').read().split('\n'),1) if len(l)>100]" task-cycle/skill/SKILL.md
```

Expected: `description lines: 1 front-matter lines: 2`, `CR present: False`; the second command
prints only `task-cycle/skill/SKILL.md:3:<length>` (the front matter, one line by design).

- [ ] **Step 4: Check the placement, the step references and the list structure**

```bash
grep -n -e '^## ' -e '^[0-9]\+\. ' task-cycle/skill/SKILL.md
```

Expected order: `## Inputs and authority` (steps 1–3), `## Start and record` (steps 4–5),
`## Light cycle`, `## Design and plan` (steps 6–8), `## Execute, verify and review` (steps 9–11),
`## Request and handoff` (steps 12–14), `## Correction after review`; each step number 1–14 once,
in order. Then read the "Light cycle" section against the file: "step 4" is the start analysis;
"steps 6 to 9" are design, spec review, plan and execution; "the foundation step below" is the
paragraph opening "Before dependent implementation"; "the dispatch contract above" is the
paragraph opening "For every dispatch"; "step 10" is checks and review; "step 11" holds the
independent assessment; "steps 11 to 14" end at the completion report. Read steps 4, 6, 9 and 13
whole and confirm every continuation line keeps the step's indentation (3 spaces for 4, 6, 9;
4 spaces for 13).

- [ ] **Step 5: Read the acceptance criterion (spec §5) in the word diff**

```bash
git diff --word-diff=plain c64a607 -- task-cycle/skill/SKILL.md
```

Read it in full. Expected: exactly six changed places; rewrapping shows no change of words.
Every change a task failing the rule meets is one of: "On the full cycle" (step 4 sentence, step 9),
"the full cycle requires ... every task it runs" (step 6), the record of the cycle choice (step 4),
the request's line naming the cycle (step 13). The post-switch sentence of step 6 applies only after
a switch; the "Light cycle" section is reached only by a task passing all three findings; the
description is metadata. No step, agent, review, check or gate of the full cycle changes. Any other
change is a finding.

- [ ] **Step 6: Run the checks and commit**

```bash
python -B gate/run_tests.py task-cycle 2>&1 | tail -2
python -B gate/run_tests.py gate 2>&1 | tail -3
```

Expected: `task-cycle` exits 1 with `NO TESTS RAN` (recorded as unchecked: the part holds no tests);
`gate` `Ran 96 tests … OK`.

Write this message with the Write tool to `docs/task-cycles/light-path-small-change/commit-msg-t2.txt`:

```text
feat(task-cycle): Add a light cycle for a small task that leaves the foundation unchanged

Step 4 now chooses, in the analysis that settles the foundation route, between the light and the
full cycle and records the reason for each finding assessed. A task takes the light cycle when it
leaves the foundation unchanged, one agent can implement it in about ten minutes, and it needs no
very large or very many files read into context.

On the light cycle one fresh executor makes the whole change from the task, without a spec or a
plan; step 10 runs in full, and one requesting-code-review of the whole change is the unit's and
the final review. A simple and obvious touch of the foundation re-records the route as changed and
goes through the element's skill and the one assessment of step 11; any other touch, or a change
that outgrows a finding, returns a report without code, discards the attempt by resetting the
branch to its base, and restarts at step 6 with that report. Steps 4, 6, 9 and 13 name the full
cycle where only it applies; nothing else in the full cycle changes (WAY-13, WAY-125).
```

```bash
git add task-cycle/skill/SKILL.md
git commit -F docs/task-cycles/light-path-small-change/commit-msg-t2.txt
python -B gate/run_tests.py installation 2>&1 | tail -3
git show --stat --format='%h %ae %s' HEAD
```

Expected: `installation` `Ran 16 tests … OK` (run after the commit: the installer reads the
skill's front matter from a commit); one commit, `<author email>`, one file changed.

---

