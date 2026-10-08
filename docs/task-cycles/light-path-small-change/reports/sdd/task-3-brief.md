### Task 3: `task-cycle/record_template.md` — the cycle in the record (spec §6)

**Files:**
- Modify: `task-cycle/record_template.md:9` (header), `:19-21` (new `## Cycle` section before
  `## Events`), `:46` (Artifacts paragraph), `:76` (Request handoff) — line numbers of `c64a607`.

**Interfaces:**
- Consumes: from Task 2, the names "light cycle", "full cycle", "switch", "executor's report",
  "discarded attempt" and step 4's "the reason for each finding you assessed".
- Produces: the record's `- Cycle:` header line and `## Cycle` section, which step 4 of the skill
  fills; the request-handoff line that step 13's "the cycle taken and its reasons" fills.

- [ ] **Step 1: Make the four edits with the Edit tool**

Old text (3a), line 9:

```text
- Foundation route: <unchanged | entry or invariant-test change; affected entries>
```

New text (3a):

```text
- Foundation route: <unchanged | entry or invariant-test change; affected entries; on the light
  cycle, the time a touch changed it>
- Cycle: <light | full | full after a switch from light>
```

Old text (3b), lines 19–21:

```text
the request; preparing reversible code for it does not authorize executing it.

## Events
```

New text (3b):

```text
the request; preparing reversible code for it does not authorize executing it.

## Cycle

- Choice at start: <light | full> — foundation: <unchanged | changed>; one agent's time to
  implement: <estimate and reason | not assessed>; files read into context: <which, and their
  size | not assessed>
- Foundation touched on the light cycle: <entry, the ruling on whether the touch is simple and
  obvious, and its reason | none>
- Switch to the full cycle: <time, why the change outgrew the light cycle, the executor's report,
  the discarded attempt's last commit and the files it changed | none>

Record the reason for each finding assessed; once one finding fails, the rest may read `not
assessed`. The last commit of a discarded attempt is a historical name, not a link to follow: the
commit is reachable only until the reflog expires. A choice or ruling of a discarded attempt keeps
its row in the questions table, with *Used by* naming the discarded attempt.

## Events
```

Old text (3c), line 46 (line 47 onward unchanged):

```text
Include the frozen task, `spec.md`, `plan.md`, code commits, tests and full agent reports. Name
```

New text (3c):

```text
Include the frozen task, `spec.md` and `plan.md` on the full cycle, code commits, tests and full
agent reports, the report of a discarded light-cycle attempt among them. Name
```

Old text (3d), line 76:

```text
- Request URL and status: <URL and draft/ready/blocked>
```

New text (3d):

```text
- Request URL and status: <URL and draft/ready/blocked>
- Cycle and its reasons: <as the request states them>
```

- [ ] **Step 2: Confirm each base text matched once**

Four successful Edit calls are the evidence. `git diff --numstat -- task-cycle/record_template.md`
expected: `21 2 task-cycle/record_template.md`.

- [ ] **Step 3: Check line lengths, line endings and the structure**

```bash
python -B -c "import sys;[print(f'{p}:{i}:{len(l)}') for p in sys.argv[1:] for i,l in enumerate(open(p,encoding='utf-8').read().split('\n'),1) if len(l)>100]" task-cycle/record_template.md
python -B -c "print('CR present:', '\r' in open('task-cycle/record_template.md',encoding='utf-8',newline='').read())"
grep -n -e '^## ' -e '^- [A-Z]' task-cycle/record_template.md
```

Expected: only the pre-existing table header line (`## Questions and autonomous choices` table,
107 characters, now line 51) is over 100; `CR present: False`; sections in the order header list,
`## Sharpness at start and after the final diff`, `## Cycle`, `## Events`, `## Questions and
autonomous choices`, `## Artifacts`, `## Verification`, `## Return step`, `## Independent
assessment`, `## Request handoff`; the header list holds `Foundation route` then `Cycle`; each
wrapped bullet continues with two spaces.

- [ ] **Step 4: Read the change against the spec and the skill**

```bash
git diff --word-diff=plain c64a607 -- task-cycle/record_template.md
```

Expected: exactly the four places of spec §6, words as there. Check that every slot of the
`## Cycle` section answers a record step 4 or the "Light cycle" section of the skill asks for
(the choice with reasons per finding; the touch ruling; the switch with the report, last commit
and files), and that the full cycle's record differs only by the `Cycle` lines and the Artifacts
wording "on the full cycle".

- [ ] **Step 5: Run the checks and commit**

```bash
python -B gate/run_tests.py task-cycle 2>&1 | tail -2
python -B gate/run_tests.py gate 2>&1 | tail -3
```

Expected: `NO TESTS RAN` (unchecked) and `Ran 96 tests … OK`.

Write this message with the Write tool to `docs/task-cycles/light-path-small-change/commit-msg-t3.txt`:

```text
feat(task-cycle): Record the cycle choice, a foundation touch and a switch in the cycle record

The record template gains a Cycle header line and a Cycle section: the choice at start with the
reason for each finding assessed, a foundation touch on the light cycle with its ruling, and a
switch to the full cycle with the executor's report, the discarded attempt's last commit (a
historical name, reachable only until the reflog expires) and the files it changed. The
foundation route can record the time a touch changed it, the artifacts list spec and plan only on
the full cycle, and the request handoff carries the cycle and its reasons.
```

```bash
git add task-cycle/record_template.md
git commit -F docs/task-cycles/light-path-small-change/commit-msg-t3.txt
git show --stat --format='%h %ae %s' HEAD
git log --oneline c64a607..HEAD
git status --short
```

Expected: three commits on the branch since `c64a607` (Tasks 1–3), each touching only its own
files; `git status --short` shows no tracked change (`.runs/` is ignored). No push.

---

## After the plan (the cycle's steps, not plan tasks)

- Whole-branch review of `c64a607..HEAD` (end of `subagent-driven-development`), then step 10:
  recalculate sharpness from the final diff, rerun `python -B gate/run_tests.py gate`, the tests
  of `elements/decisions` and `elements/invariants`, `installation`, and the three guards; record
  `task-cycle` as unchecked.
- Step 11: the return step, and the one independent assessment (WAY-10,
  `elements/common/critique/SKILL.md`) of the foundation change of Task 1; its record goes in the
  message of the commit that carries its settlement (`agent-instructions/README.md`, "Integrate
  into `foundations`").
- Step 12: swap `<request link>` in both *Approved by* fields for the request URL — a placeholder
  swap that changes no binding part, so no fingerprint moves.
