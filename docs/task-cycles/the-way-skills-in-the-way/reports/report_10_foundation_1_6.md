# Report 10 — foundation step 1.6, part-map agent (saved by the orchestrator from the returned text)

Wrote two entries in `foundations/part_map.md` following the process root's part-map skill; committed nothing. Part-map
guard (`--base none`) exit 1 with 3 errors: the two accepted pattern errors and the missing flow test. No other file
changed (a guard output file briefly written under `reports/` was deleted to keep the write boundary; scratch helpers only
in the session scratchpad).

## Written

`agent-instructions`, changed in place:

```markdown
## agent-instructions

The part answers for the instructions agents read when they work on this repository, for the
project skill entry points that make the-way's skills visible to sessions on it and the script that
generates them, and for the hooks and the configuration of agents' tools and of CI that direct them.

- **Files:** /AGENTS.md
  /CLAUDE.md
  agent-instructions/**
  .claude/skills/**
  .agents/skills/**
- **Depends on:** decisions · invariants · glossary · part-map · environment-facts ·
  elements-common · project-level · task-cycle · gate
- **Failure modes:**
  - an agent follows stale integration instructions — a change enters the integration branch
    without the required checks or acceptance — high — not detected
  - a skill of the-way has no entry point, or a stale one — a session on the-way uses a personal
    skill of that name or none — high — detected by skill-entry-points
  - the-way's own entry point, loaded from a product's `.the-way`, is followed instead of the
    product's, where the agent knows neither the entry point's path nor the session's start
    directory (Claude Code's documentation states neither is given to the agent, and Codex gives
    no file path for a skill it leaves out of its initial list) — a product entry is written
    against the-way's own foundation — high — not detected
- **Trust boundary:** none
```

Patterns checked with `git check-attr` (`core.ignorecase=false`): `.claude/skills/**` claims
`.claude/skills/the-way-record-decision/SKILL.md`; `.agents/skills/**` claims
`.agents/skills/the-way-update-part-map/SKILL.md`; neither claims `.the-way/.claude/skills/…` or
`agent-instructions/skill_entry_points.py`; today they claim no tracked file and take none from another part.

New critical flow `skills-reach-the-way-sessions` (after `wording-reaches-dependants`), first wording: "Someone adds,
renames or moves a skill of the-way, or changes its description, and a session on the-way that would not find it under
its `the-way-` name is reported before the change reaches the main branch." Criticality high; Parts agent-instructions ·
elements-common · decisions · invariants · glossary · part-map · environment-facts · project-level · task-cycle · gate
(the eight parts holding the 11 `SKILL.md` files, plus `agent-instructions` and `gate`); Invariant skill-entry-points;
Coverage none. Identifier collides with nothing.

## Search findings (WAY-33)

1. Question — gate dependency for its new test: provisional none. *Depends on* records code reliance (WAY-04, WAY-51);
   precedent: `gate` names `decisions · relation-model` because its flow test imports the decisions guard. The new test
   imports no other part's code; the files it reads are the subject under test; that reach is the flow's *Parts* (WAY-45),
   criticality through the flow (WAY-46). Weak point: precedent is mixed (`agent-instructions` names parts it only
   refers to in text).
2. Question — a part that gains a skill later must be added to the flow's *Parts*; with `Coverage: none` nothing reports
   the omission (WAY-47 reports it as unchecked). Known case: `task/instruction-files` adds `instruction-files/skill/SKILL.md`.
   Provisional: whichever branch merges second adds that part to the flow with its entry points; worth a line in the
   request or the return step. Test runs unaffected (`skill-entry-points` names `every`).
3. Link — `installation` not on the flow (no `SKILL.md`; its wrapper sentence not on this flow); its failure mode "a
   project skill resolves to another process version" is the product-side sibling of the new not-detected mode.
4. Link — `generated-overview/1` *Part* `part-map · agent-instructions`: `invariant-part-names` passes; the entry points
   list skill names, no overview; WAY-52 binds only what is generated from the part map.
5. Link — WAY-09@16b8026b and `repository-file-location/1`: the patterns place the entry points in `agent-instructions`.
6. Link — `path-pattern-reach/1`: red until the entry points exist (accepted); positive control: the patterns match the
   planned paths.
7. Link — WAY-55, `flow-test-location/1`: the flow test belongs under `gate/` and does not call a body in another part.
8. Link — WAY-48: trust boundary stays `none`; the generator reads the repository's own `SKILL.md` files; the product
   exchange is covered by the existing external-context row.
9. Link — WAY-49: no new surface; `installation-command`'s promise unchanged.
10. Link — WAY-53, `derived-file-content/1`: covered.
11. Link — glossary: "entry point" a fixed compound; `--uses entry` now also lists `part_map.md:174, 187, 189, 190`;
    "a product entry" uses the glossary meaning. Glossary guard 0/0.
12. Note for the `AGENTS.md` implementer — WAY-16: `## Skills` names the generator command (not a check command) and points
    to the gate's tests; it must not offer a check command beside the gate's.
13. Question — the flow sentence says a *session* is reported, the spec means a *skill*. Proposed: "…and a skill that a
    session on the-way would not find under its `the-way-` name is reported before the change reaches the main branch."
    Recommendation: reword before the request.

## Guard output (process root's part-map guard, `--base none`, exit 1)

```
foundations/part_map.md:177: error: pattern `.claude/skills/**` of `agent-instructions` matches no file git tracks
foundations/part_map.md:177: error: pattern `.agents/skills/**` of `agent-instructions` matches no file git tracks
foundations/part_map.md:231: error: skills-reach-the-way-sessions: no test names the flow in a line `# flow: skills-reach-the-way-sessions`
unchecked: the list of parts of `wording-reaches-dependants` — its test leaves no coverage file
unchecked: the list of parts of `skills-reach-the-way-sessions` — its test leaves no coverage file
unchecked: the change path of every promise level in use — the levels sit at the declarations, and no command of the product reports them
unchecked: the dependencies between parts, and new or stale violations — no command of the product reports the dependency graph
unchecked: the list of known violations — --base none: there is no commit the branch left the main branch from
unchecked: the identifiers of the map — --base none: there is no commit the branch left the main branch from
unchecked: the lowering of a part's computed criticality — --base none: there is no commit the branch left the main branch from
3 error(s), 0 warning(s), 7 unchecked
```

Against the baseline (0 errors, 6 unchecked): two accepted pattern errors, the expected missing flow test, one new
unchecked line from `Coverage: none`. LF kept. Invariants guard 0/0, 3 unchecked; glossary guard 0/0, 6 unchecked.

## Polish meaning sentences and criticality

- agent-instructions: Część `agent-instructions` odpowiada teraz także za wskaźniki skilli projektu w `.claude/skills/` i
  `.agents/skills/`, dzięki którym sesja na the-way widzi skille the-way, oraz za skrypt, który je generuje; może
  dodatkowo zależeć od `project-level` i `task-cycle`, a jej nowe awarie to brakujący albo nieaktualny wskaźnik (wykrywa
  go `skill-entry-points`) oraz wskaźnik samego the-way, wczytany z `.the-way` produktu i wykonany zamiast skilla
  produktu, gdy agent nie zna ani ścieżki wskaźnika, ani katalogu startu sesji (niewykrywana).
- skills-reach-the-way-sessions: see the re-wording below (report 10b).
- Computed criticality (WAY-46): unchanged — the guard's own `criticality()` gives an identical result before and after:
  twelve parts high, `repository` low.
- 10b: flow sentence reworded per orchestrator ruling on finding 13: "Someone adds, renames or moves a skill of the-way, or changes its description, and a skill that a session on the-way would not find under its `the-way-` name is reported before the change reaches the main branch." Guard unchanged: 3 errors (two accepted pattern errors, missing flow test), 0 warnings, 7 unchecked; LF; criticality unchanged. Polish sentence unchanged.
