# Plan — Wybór technologii, której projekt nie ustalił, wraca do Mariusza zamiast zapaść po cichu w zadaniu

- Task: `.runs/task-cycles/unsettled-technology-returns/task.md`
- Spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`
- Base: `2dbf1e7`

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| (new) How does the step that settles technology run outside a project definition? | decision | row 1 | Slices 1, 2, 3 |
| (new) Who settles a technology choice that no decision or definition settles? | decision | row 2 | Slices 2, 4, 5 |
| (new) How does a task leave a cycle that met a reserved choice, and how does it come back? | decision | this spec | Slices 5, 6 |
| reserved choice | glossary term | this spec | Slices 1, 2, 4, 5, 6 |
| WAY-121 | decision, changed in place | row 3 | Slices 1, 2 |
| WAY-122 | decision, changed in place | row 3 | Slice 1 |
| WAY-123 | decision, changed in place | row 3 | Slice 1 |
| WAY-137 | decision, changed in place | row 3 | Slice 1 |
| WAY-138 | decision, changed in place | row 3 | Slice 1 |
| WAY-135 | decision, changed in place | row 3 | Slices 4, 5 |

## Slices

### Slice 1 — The technology step runs at a task document

- **Goal:** `settle-technology` runs at a task document as the spec's decisions 1 and 4 give. In
  `project-level/technology/SKILL.md` the description, the title, the opening and the sentence on
  where the step writes speak of both documents, and step 0 routes a named task document to the new
  `project-level/technology/task_run.md` and a note with no document to `refine-task`.
  `task_run.md` holds, step by step, only what differs from a run at a definition: *Start*, *List*,
  *Settle*, *Write*, *Close* and *Orchestrated*. `research.md` and `settle.md` say "the document"
  where both runs share a sentence; `research.md` adds the report's head line and the note among
  what the leader gives; `settle.md`'s sub-step 7 gains its pointer. `project-level/task/template.md`
  gains the section *Technology*, with its four markers and nested items, and the three fields
  *Based on*, *Lacks* and *Risks taken* under a settled question, and its sentence on a canonical
  answer reaches them. `elements/decisions/template.md` extends its two rules at lines 59–67 for the
  cycle's writer: row, then the question its *Source* names, then those fields, and a choice that
  changes a decision as an edit in place. `start.md`, `list.md`, `close.md`, `running_product.md` and
  the definition template keep their text. After changing the description, run
  `python -B agent-instructions/skill_entry_points.py --write`, handle any obsolete output paths it
  reports for removal, and commit all of its output; do not edit that output by hand. The
  description stays one line that holds neither `: ` nor ` #`.
- **Change:** `project-level/technology/SKILL.md` · `project-level/technology/task_run.md` ·
  `project-level/technology/research.md` · `project-level/technology/settle.md` ·
  `project-level/task/template.md` · `elements/decisions/template.md` ·
  `.claude/skills/the-way-*/SKILL.md` · `.agents/skills/the-way-*/SKILL.md`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:39-44` Questions to settle, Pytanie 1 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:57-61` Questions to settle, Pytanie 4 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:73-77` Questions to settle, Pytanie 7 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:144-147` Out of scope ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:80-154` Decisions, 1. The place in the task document ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:304-402` Decisions, 4. A run at a task beside a run at a definition ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decision From row 1 of *Foundation entries* ·
  WAY-121, WAY-122, WAY-123, WAY-137 and WAY-138 as *Foundation entries* changes them ·
  the glossary term reserved choice of *Foundation entries* ·
  `foundations/decisions.md:6-35` WAY-01 · `foundations/decisions.md:37-66` WAY-02 ·
  `foundations/decisions.md:68-93` WAY-03 · `foundations/decisions.md:95-122` WAY-04 ·
  `foundations/decisions.md:124-151` WAY-05 · `foundations/decisions.md:153-180` WAY-07 ·
  `foundations/decisions.md:212-285` WAY-09 · `foundations/decisions.md:287-318` WAY-10 ·
  `foundations/decisions.md:320-355` WAY-11 · `foundations/decisions.md:357-385` WAY-12 ·
  `foundations/decisions.md:427-448` WAY-14 · `foundations/decisions.md:450-473` WAY-16 ·
  `foundations/decisions.md:475-493` WAY-17 · `foundations/decisions.md:495-521` WAY-18 ·
  `foundations/decisions.md:523-546` WAY-19 · `foundations/decisions.md:548-566` WAY-21 ·
  `foundations/decisions.md:568-591` WAY-22 · `foundations/decisions.md:593-611` WAY-24 ·
  `foundations/decisions.md:613-636` WAY-25 · `foundations/decisions.md:638-666` WAY-26 ·
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:696-723` WAY-28 ·
  `foundations/decisions.md:725-757` WAY-29 · `foundations/decisions.md:759-796` WAY-30 ·
  `foundations/decisions.md:798-817` WAY-32 · `foundations/decisions.md:819-849` WAY-33 ·
  `foundations/decisions.md:851-885` WAY-34 · `foundations/decisions.md:887-910` WAY-35 ·
  `foundations/decisions.md:912-936` WAY-36 · `foundations/decisions.md:938-959` WAY-37 ·
  `foundations/decisions.md:961-985` WAY-38 · `foundations/decisions.md:1059-1092` WAY-44 ·
  `foundations/decisions.md:1219-1239` WAY-52 · `foundations/decisions.md:1241-1257` WAY-53 ·
  `foundations/decisions.md:1259-1281` WAY-54 · `foundations/decisions.md:1283-1307` WAY-55 ·
  `foundations/decisions.md:1367-1395` WAY-60 · `foundations/decisions.md:1397-1431` WAY-61 ·
  `foundations/decisions.md:1523-1544` WAY-65 · `foundations/decisions.md:1590-1617` WAY-71 ·
  `foundations/decisions.md:1619-1640` WAY-72 · `foundations/decisions.md:1642-1671` WAY-73 ·
  `foundations/decisions.md:1820-1845` WAY-84 · `foundations/decisions.md:1847-1872` WAY-85 ·
  `foundations/decisions.md:1874-1903` WAY-86 · `foundations/decisions.md:1905-1928` WAY-89 ·
  `foundations/decisions.md:1930-1960` WAY-90 · `foundations/decisions.md:2012-2039` WAY-95 ·
  `foundations/decisions.md:2061-2089` WAY-97 · `foundations/decisions.md:2091-2116` WAY-99 ·
  `foundations/decisions.md:2118-2140` WAY-100 · `foundations/decisions.md:2142-2160` WAY-101 ·
  `foundations/decisions.md:2162-2186` WAY-102 · `foundations/decisions.md:2188-2208` WAY-103 ·
  `foundations/decisions.md:2210-2247` WAY-104 · `foundations/decisions.md:2249-2270` WAY-106 ·
  `foundations/decisions.md:2272-2293` WAY-107 · `foundations/decisions.md:2295-2321` WAY-108 ·
  `foundations/decisions.md:2323-2341` WAY-109 · `foundations/decisions.md:2343-2362` WAY-110 ·
  `foundations/decisions.md:2364-2388` WAY-111 · `foundations/decisions.md:2390-2415` WAY-112 ·
  `foundations/decisions.md:2417-2448` WAY-113 · `foundations/decisions.md:2450-2474` WAY-114 ·
  `foundations/decisions.md:2476-2502` WAY-115 · `foundations/decisions.md:2504-2526` WAY-116 ·
  `foundations/decisions.md:2528-2557` WAY-117 · `foundations/decisions.md:2559-2593` WAY-118 ·
  `foundations/decisions.md:2595-2621` WAY-120 · `foundations/decisions.md:2623-2694` WAY-121 ·
  `foundations/decisions.md:2696-2750` WAY-122 · `foundations/decisions.md:2752-2788` WAY-123 ·
  `foundations/decisions.md:2790-2835` WAY-124 · `foundations/decisions.md:2837-2874` WAY-125 ·
  `foundations/decisions.md:2876-2916` WAY-126 · `foundations/decisions.md:2918-2982` WAY-127 ·
  `foundations/decisions.md:2984-3031` WAY-128 · `foundations/decisions.md:3033-3054` WAY-129 ·
  `foundations/decisions.md:3056-3091` WAY-130 · `foundations/decisions.md:3093-3120` WAY-131 ·
  `foundations/decisions.md:3122-3155` WAY-132 · `foundations/decisions.md:3157-3186` WAY-133 ·
  `foundations/decisions.md:3188-3266` WAY-134 · `foundations/decisions.md:3392-3427` WAY-137 ·
  `foundations/decisions.md:3429-3472` WAY-138 · `foundations/decisions.md:3474-3508` WAY-139 ·
  `foundations/decisions.md:3510-3559` WAY-140 · `foundations/decisions.md:3582-3628` WAY-142 ·
  `foundations/decisions.md:3630-3662` WAY-143 · `foundations/decisions.md:3664-3697` WAY-144 ·
  `foundations/decisions.md:3699-3740` WAY-145 · `foundations/decisions.md:3742-3777` WAY-146 ·
  `foundations/decisions.md:3779-3806` WAY-147 · `foundations/decisions.md:3868-3926` WAY-150 ·
  `foundations/decisions.md:3928-3960` WAY-151 · `foundations/decisions.md:3962-3988` WAY-152 ·
  `foundations/decisions.md:3990-4020` WAY-153 · `foundations/decisions.md:4022-4057` WAY-154 ·
  `foundations/decisions.md:4059-4091` WAY-155 · `foundations/decisions.md:4093-4123` WAY-156 ·
  `foundations/decisions.md:4399-4441` WAY-165 · `foundations/decisions.md:4443-4472` WAY-166 ·
  `foundations/decisions.md:4544-4594` WAY-168 · `foundations/decisions.md:4702-4740` WAY-172 ·
  `foundations/decisions.md:4778-4827` WAY-174 · `foundations/decisions.md:5840-5875` WAY-214 ·
  `foundations/decisions.md:5878-5919` WAY-215 · `foundations/decisions.md:5922-5945` WAY-216 ·
  `foundations/decisions.md:5948-5968` WAY-217 · `foundations/decisions.md:5971-6005` WAY-218 ·
  `foundations/decisions.md:6093-6120` WAY-225 · `foundations/decisions.md:6294-6335` WAY-230 ·
  `foundations/decisions.md:6655-6699` WAY-238 · `foundations/decisions.md:6804-6851` WAY-242 ·
  `foundations/decisions.md:6970-6993` WAY-247 · `foundations/decisions.md:7269-7326` WAY-256 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:36-44` element-directory-contents ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:86-94` skill-rule-source ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:146-154` generated-overview ·
  `foundations/invariants.md:176-185` project-definition-form ·
  `foundations/invariants.md:187-196` project-readiness-gate ·
  `foundations/invariants.md:198-206` project-technology-record ·
  `foundations/invariants.md:208-220` project-plan-form ·
  `foundations/invariants.md:222-239` project-plan-check ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/invariants.md:261-269` root-claude-md-import ·
  `foundations/invariants.md:281-296` project-plan-state-evidence ·
  `foundations/invariants.md:298-306` project-plan-state-subprocesses ·
  `foundations/part_map.md:77-90` part project-level ·
  `foundations/part_map.md:7-15` part decisions ·
  `foundations/part_map.md:121-134` part agent-instructions ·
  `foundations/glossary.md:7-11` agent's way to the running product ·
  `foundations/glossary.md:97-101` open design choice · `project-level/technology/start.md` ·
  `project-level/technology/list.md` · `project-level/technology/close.md` ·
  `project-level/technology/running_product.md` ·
  `project-level/definition_template.md:148-244` Technology ·
  `elements/common/way_of_working.md:18-36` How a skill asks · `project-level/task/skill/SKILL.md` ·
  `project-level/task/skill/draft.md` ·
  `project-level/task/skill/resolve_gaps.md:10-12` Resolve the gaps ·
  `agent-instructions/skill_entry_points.py:1-27` the form of a description
- **Model:** same — it writes the contract every later slice cites, across the parts `project-level`, `decisions` and `agent-instructions`, and each difference in `task_run.md` has to be worded against WAY-121, WAY-122, WAY-134 and WAY-138.
- **Risk:** none
- **Checks:** the slice changes no script, so no test comes first. `python -B agent-instructions/skill_entry_points.py`
  prints `entry points are current` with exit code 0 · `python -B gate/run_tests.py agent-instructions` ·
  `python -B gate/run_tests.py gate` · `python -B gate/run_tests.py project-level` ·
  `python -B instruction-files/check_instructions.py . --file project-level/technology/task_run.md`
  exits 0 · `git diff --exit-code <slice's base> -- project-level/technology/start.md project-level/technology/list.md project-level/technology/close.md project-level/technology/running_product.md project-level/definition_template.md`
  exits 0
- **Depends on:** the new decision From row 1 · WAY-121 · WAY-122 · WAY-123 · WAY-137 · WAY-138 ·
  reserved choice

### Slice 2 — Refinement sends a reserved choice to the step

- **Goal:** the new `project-level/technology/reserved_choices.md` is the one home of the rule, with
  the content the spec's decision 3 lists under "One home of the rule", "Examples it carries" and
  "The boundary". `refine-task` follows it. `resolve_gaps.md` runs the step at the document in the
  three cases of decision 4, the rule deciding only the first; its sentence at lines 10–12 gains
  decision 1's exception and its sentence at lines 17–18 excepts a reserved choice.
  `find_settlements.md` says that a settled technology question is always shown as a candidate and
  gains decision 1's exception at lines 21–22. `carry_foundation.md` gains decision 1's exception at
  lines 13–15. `final_review.md` checks that no item ends `— open`. `draft.md` gains that a task whose
  blocked request the human closed is a document refined from its text, that the named choice is the
  run's note, and that the refiner keeps the closed request's link under *Context*.
  `project_plan_task.md` says that the run stands at the member's own document and the approved
  definition stays untouched, with the two routes decision 4 gives. Each exception reaches exactly
  the decision a run changes; any other collision goes as those sentences give.
- **Change:** `project-level/technology/reserved_choices.md` ·
  `project-level/task/skill/resolve_gaps.md` · `project-level/task/skill/find_settlements.md` ·
  `project-level/task/skill/carry_foundation.md` · `project-level/task/skill/final_review.md` ·
  `project-level/task/skill/draft.md` · `project-level/task/skill/project_plan_task.md`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:39-44` Questions to settle, Pytanie 1 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:45-50` Questions to settle, Pytanie 2 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:51-56` Questions to settle, Pytanie 3 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:62-66` Questions to settle, Pytanie 5 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:73-77` Questions to settle, Pytanie 7 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:92-92` Context, the return to the plan ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:80-154` Decisions, 1. The place in the task document ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:219-255` Decisions, 3. The rule in the skills and the status of the return, through Where the pointers stand ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:352-361` Decisions, 4, Refinement and Plan members ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:416-420` Decisions, 5, The document ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decisions From row 1 and row 2 of *Foundation entries* ·
  WAY-121 as *Foundation entries* changes it ·
  the glossary term reserved choice of *Foundation entries* ·
  `foundations/decisions.md:6-35` WAY-01 · `foundations/decisions.md:212-285` WAY-09 ·
  `foundations/decisions.md:759-796` WAY-30 · `foundations/decisions.md:912-936` WAY-36 ·
  `foundations/decisions.md:961-985` WAY-38 · `foundations/decisions.md:1905-1928` WAY-89 ·
  `foundations/decisions.md:2118-2140` WAY-100 · `foundations/decisions.md:2142-2160` WAY-101 ·
  `foundations/decisions.md:2162-2186` WAY-102 · `foundations/decisions.md:2249-2270` WAY-106 ·
  `foundations/decisions.md:2272-2293` WAY-107 · `foundations/decisions.md:2295-2321` WAY-108 ·
  `foundations/decisions.md:2323-2341` WAY-109 · `foundations/decisions.md:2343-2362` WAY-110 ·
  `foundations/decisions.md:2364-2388` WAY-111 · `foundations/decisions.md:2390-2415` WAY-112 ·
  `foundations/decisions.md:2417-2448` WAY-113 · `foundations/decisions.md:2450-2474` WAY-114 ·
  `foundations/decisions.md:2476-2502` WAY-115 · `foundations/decisions.md:2504-2526` WAY-116 ·
  `foundations/decisions.md:2528-2557` WAY-117 · `foundations/decisions.md:2559-2593` WAY-118 ·
  `foundations/decisions.md:2595-2621` WAY-120 · `foundations/decisions.md:2623-2694` WAY-121 ·
  `foundations/decisions.md:2696-2750` WAY-122 · `foundations/decisions.md:2752-2788` WAY-123 ·
  `foundations/decisions.md:2790-2835` WAY-124 · `foundations/decisions.md:2876-2916` WAY-126 ·
  `foundations/decisions.md:2918-2982` WAY-127 · `foundations/decisions.md:3188-3266` WAY-134 ·
  `foundations/decisions.md:3268-3313` WAY-135 · `foundations/decisions.md:3392-3427` WAY-137 ·
  `foundations/decisions.md:3429-3472` WAY-138 · `foundations/decisions.md:3474-3508` WAY-139 ·
  `foundations/decisions.md:3510-3559` WAY-140 · `foundations/decisions.md:3582-3628` WAY-142 ·
  `foundations/decisions.md:3630-3662` WAY-143 · `foundations/decisions.md:3664-3697` WAY-144 ·
  `foundations/decisions.md:3699-3740` WAY-145 · `foundations/decisions.md:3742-3777` WAY-146 ·
  `foundations/decisions.md:3779-3806` WAY-147 · `foundations/decisions.md:3868-3926` WAY-150 ·
  `foundations/decisions.md:3928-3960` WAY-151 · `foundations/decisions.md:3962-3988` WAY-152 ·
  `foundations/decisions.md:3990-4020` WAY-153 · `foundations/decisions.md:4022-4057` WAY-154 ·
  `foundations/decisions.md:4059-4091` WAY-155 · `foundations/decisions.md:4093-4123` WAY-156 ·
  `foundations/decisions.md:4399-4441` WAY-165 · `foundations/decisions.md:4443-4472` WAY-166 ·
  `foundations/decisions.md:4702-4740` WAY-172 · `foundations/decisions.md:5003-5041` WAY-185 ·
  `foundations/decisions.md:5043-5084` WAY-186 · `foundations/decisions.md:5665-5703` WAY-210 ·
  `foundations/decisions.md:5705-5737` WAY-211 · `foundations/decisions.md:5840-5875` WAY-214 ·
  `foundations/decisions.md:5878-5919` WAY-215 · `foundations/decisions.md:5922-5945` WAY-216 ·
  `foundations/decisions.md:5948-5968` WAY-217 · `foundations/decisions.md:5971-6005` WAY-218 ·
  `foundations/decisions.md:6008-6040` WAY-219 · `foundations/decisions.md:6143-6164` WAY-227 ·
  `foundations/decisions.md:6294-6335` WAY-230 · `foundations/decisions.md:6655-6699` WAY-238 ·
  `foundations/decisions.md:6804-6851` WAY-242 · `foundations/decisions.md:6970-6993` WAY-247 ·
  `foundations/decisions.md:6995-7029` WAY-248 · `foundations/decisions.md:7031-7067` WAY-249 ·
  `foundations/decisions.md:7269-7326` WAY-256 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:176-185` project-definition-form ·
  `foundations/invariants.md:187-196` project-readiness-gate ·
  `foundations/invariants.md:198-206` project-technology-record ·
  `foundations/invariants.md:208-220` project-plan-form ·
  `foundations/invariants.md:222-239` project-plan-check ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/invariants.md:281-296` project-plan-state-evidence ·
  `foundations/invariants.md:298-306` project-plan-state-subprocesses ·
  `foundations/part_map.md:77-90` part project-level ·
  `foundations/glossary.md:7-11` agent's way to the running product ·
  `foundations/glossary.md:97-101` open design choice · `project-level/task/template.md` ·
  `project-level/technology/SKILL.md` · project-level/technology/task_run.md as Slice 1 makes it ·
  `project-level/technology/list.md:16-22` List the choices · `project-level/task/skill/SKILL.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** the slice changes no script, so no test comes first. `python -B gate/run_tests.py project-level` ·
  `python -B instruction-files/check_instructions.py . --file project-level/technology/reserved_choices.md`
  exits 0 · `git grep -l -F "reserved_choices.md" -- project-level/task/skill/resolve_gaps.md`
  lists that file
- **Depends on:** Slice 1 · the new decisions From row 1 and row 2 · WAY-121 · reserved choice

### Slice 3 — Orchestrated refinement carries a run

- **Goal:** a run reaches the human through an orchestrated round as the spec's decision 4 gives.
  `orchestrated_mode.md`: the refiner writes the request for a run as a *Child-work request* in its
  turn, every question the run would ask goes into the turn, and only the refiner writes the
  document. `conversation_template.md`: *Human material* gains a line for the list to confirm and the
  table of choices, and a request for a run names the choice and its note. `answering.md`: before it
  chooses canonical IDs the answering agent reads these requests too, marks one canonical request
  with its affected tasks where two members name one choice with the same scope, answers no such
  request and prepares no human question for it. `project-level/lead/skill/SKILL.md` step 3: the
  project orchestrator dispatches the research agents, the critiques and the tests the refiner
  requests, one run per canonical request at the document of the affected task with the lowest
  number, and the table goes in the round package with its choices recorded as human answers. The
  refiner's five results stay as they are. The frontmatter of that `SKILL.md` stays, so no entry point
  changes.
- **Change:** `project-level/task/skill/orchestrated_mode.md` ·
  `project-level/lead/conversation_template.md` · `project-level/lead/answering.md` ·
  `project-level/lead/skill/SKILL.md`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:39-44` Questions to settle, Pytanie 1 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:94-94` Context, the conversation file ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:84-103` Decisions, 1, Section Technology and the three fields ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:362-386` Decisions, 4, Orchestrated refinement and One choice in two members of a round ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decision From row 1 of *Foundation entries* · `foundations/decisions.md:212-285` WAY-09 ·
  `foundations/decisions.md:961-985` WAY-38 · `foundations/decisions.md:1905-1928` WAY-89 ·
  `foundations/decisions.md:2118-2140` WAY-100 · `foundations/decisions.md:2142-2160` WAY-101 ·
  `foundations/decisions.md:2162-2186` WAY-102 · `foundations/decisions.md:2249-2270` WAY-106 ·
  `foundations/decisions.md:2272-2293` WAY-107 · `foundations/decisions.md:2295-2321` WAY-108 ·
  `foundations/decisions.md:2323-2341` WAY-109 · `foundations/decisions.md:2343-2362` WAY-110 ·
  `foundations/decisions.md:2364-2388` WAY-111 · `foundations/decisions.md:2390-2415` WAY-112 ·
  `foundations/decisions.md:2417-2448` WAY-113 · `foundations/decisions.md:2450-2474` WAY-114 ·
  `foundations/decisions.md:2476-2502` WAY-115 · `foundations/decisions.md:2504-2526` WAY-116 ·
  `foundations/decisions.md:2528-2557` WAY-117 · `foundations/decisions.md:2559-2593` WAY-118 ·
  `foundations/decisions.md:2595-2621` WAY-120 · `foundations/decisions.md:2623-2694` WAY-121 ·
  `foundations/decisions.md:2696-2750` WAY-122 · `foundations/decisions.md:2752-2788` WAY-123 ·
  `foundations/decisions.md:2790-2835` WAY-124 · `foundations/decisions.md:2876-2916` WAY-126 ·
  `foundations/decisions.md:2918-2982` WAY-127 · `foundations/decisions.md:3188-3266` WAY-134 ·
  `foundations/decisions.md:3392-3427` WAY-137 · `foundations/decisions.md:3429-3472` WAY-138 ·
  `foundations/decisions.md:3474-3508` WAY-139 · `foundations/decisions.md:3510-3559` WAY-140 ·
  `foundations/decisions.md:3582-3628` WAY-142 · `foundations/decisions.md:3630-3662` WAY-143 ·
  `foundations/decisions.md:3664-3697` WAY-144 · `foundations/decisions.md:3699-3740` WAY-145 ·
  `foundations/decisions.md:3742-3777` WAY-146 · `foundations/decisions.md:3779-3806` WAY-147 ·
  `foundations/decisions.md:3868-3926` WAY-150 · `foundations/decisions.md:3928-3960` WAY-151 ·
  `foundations/decisions.md:3962-3988` WAY-152 · `foundations/decisions.md:3990-4020` WAY-153 ·
  `foundations/decisions.md:4022-4057` WAY-154 · `foundations/decisions.md:4059-4091` WAY-155 ·
  `foundations/decisions.md:4093-4123` WAY-156 · `foundations/decisions.md:4399-4441` WAY-165 ·
  `foundations/decisions.md:4443-4472` WAY-166 · `foundations/decisions.md:4702-4740` WAY-172 ·
  `foundations/decisions.md:5840-5875` WAY-214 · `foundations/decisions.md:5878-5919` WAY-215 ·
  `foundations/decisions.md:5922-5945` WAY-216 · `foundations/decisions.md:5948-5968` WAY-217 ·
  `foundations/decisions.md:5971-6005` WAY-218 · `foundations/decisions.md:6294-6335` WAY-230 ·
  `foundations/decisions.md:6655-6699` WAY-238 · `foundations/decisions.md:6804-6851` WAY-242 ·
  `foundations/decisions.md:6970-6993` WAY-247 · `foundations/decisions.md:7269-7326` WAY-256 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:176-185` project-definition-form ·
  `foundations/invariants.md:187-196` project-readiness-gate ·
  `foundations/invariants.md:198-206` project-technology-record ·
  `foundations/invariants.md:208-220` project-plan-form ·
  `foundations/invariants.md:222-239` project-plan-check ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/invariants.md:281-296` project-plan-state-evidence ·
  `foundations/invariants.md:298-306` project-plan-state-subprocesses ·
  `foundations/part_map.md:77-90` part project-level ·
  `foundations/glossary.md:157-161` project orchestrator · `project-level/task/template.md` ·
  `project-level/task/skill/SKILL.md` · `project-level/technology/SKILL.md` ·
  `project-level/technology/settle.md` · `project-level/technology/research.md` ·
  project-level/technology/task_run.md as Slice 1 makes it
- **Model:** cheaper
- **Risk:** none
- **Checks:** the slice changes no script, so no test comes first. `python -B gate/run_tests.py project-level` ·
  `git grep -l -i "child-work request" -- project-level/task/skill/orchestrated_mode.md project-level/lead/conversation_template.md project-level/lead/answering.md`
  lists all three files
- **Depends on:** Slice 1 · the new decision From row 1

### Slice 4 — The stage agents return `reserved`

- **Goal:** the agents of the stages return a reserved choice instead of settling it, as the rows of
  the spec's decision 3 give for these files. `task-cycle/change/SKILL.md`: section 5 gains the case
  and section 6 lists the status `reserved`, whose report holds the choice, where it shows, the limb of
  the rule, what was searched and the ways seen, and no code. `task-cycle/plan/SKILL.md`: section 2
  gains the case and section 5 lists the status. `task-cycle/spec/design.md`: the sentence at lines
  15–16 excepts a reserved choice and the designer returns `reserved` with the same report.
  `task-cycle/spec/SKILL.md`: section 4 names the status only if the wording needs it, which the spec
  leaves to you; left unchanged, say so in your report. `task-cycle/review/SKILL.md`: section 2 gains
  the check that a change taking a reserved choice is a finding, graded Important by the general grade
  of section 3, a missed requirement, with no citation of WAY-263. Each pointer names the moment by
  what the agent sees and points to `project-level/technology/reserved_choices.md`; no method copies
  the rule. No frontmatter changes, so no entry point changes.
- **Change:** `task-cycle/change/SKILL.md` · `task-cycle/plan/SKILL.md` ·
  `task-cycle/spec/design.md` · `task-cycle/spec/SKILL.md` · `task-cycle/review/SKILL.md`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:45-50` Questions to settle, Pytanie 2 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:51-56` Questions to settle, Pytanie 3 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:62-66` Questions to settle, Pytanie 5 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:217-302` Decisions, 3. The rule in the skills and the status of the return ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decision From row 2 of *Foundation entries* · WAY-135 as *Foundation entries* changes it ·
  the glossary term reserved choice of *Foundation entries* ·
  `foundations/decisions.md:6-35` WAY-01 · `foundations/decisions.md:68-93` WAY-03 ·
  `foundations/decisions.md:212-285` WAY-09 · `foundations/decisions.md:287-318` WAY-10 ·
  `foundations/decisions.md:320-355` WAY-11 · `foundations/decisions.md:387-425` WAY-13 ·
  `foundations/decisions.md:450-473` WAY-16 · `foundations/decisions.md:548-566` WAY-21 ·
  `foundations/decisions.md:613-636` WAY-25 · `foundations/decisions.md:638-666` WAY-26 ·
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:696-723` WAY-28 ·
  `foundations/decisions.md:759-796` WAY-30 · `foundations/decisions.md:819-849` WAY-33 ·
  `foundations/decisions.md:851-885` WAY-34 · `foundations/decisions.md:912-936` WAY-36 ·
  `foundations/decisions.md:938-959` WAY-37 · `foundations/decisions.md:961-985` WAY-38 ·
  `foundations/decisions.md:1059-1092` WAY-44 · `foundations/decisions.md:1094-1117` WAY-45 ·
  `foundations/decisions.md:1119-1147` WAY-48 · `foundations/decisions.md:1173-1217` WAY-51 ·
  `foundations/decisions.md:1283-1307` WAY-55 · `foundations/decisions.md:1433-1460` WAY-62 ·
  `foundations/decisions.md:1462-1489` WAY-63 · `foundations/decisions.md:1523-1544` WAY-65 ·
  `foundations/decisions.md:1546-1566` WAY-68 · `foundations/decisions.md:1568-1588` WAY-69 ·
  `foundations/decisions.md:1786-1818` WAY-82 · `foundations/decisions.md:1905-1928` WAY-89 ·
  `foundations/decisions.md:2118-2140` WAY-100 · `foundations/decisions.md:2142-2160` WAY-101 ·
  `foundations/decisions.md:2162-2186` WAY-102 · `foundations/decisions.md:2188-2208` WAY-103 ·
  `foundations/decisions.md:2249-2270` WAY-106 · `foundations/decisions.md:2623-2694` WAY-121 ·
  `foundations/decisions.md:2790-2835` WAY-124 · `foundations/decisions.md:2837-2874` WAY-125 ·
  `foundations/decisions.md:2876-2916` WAY-126 · `foundations/decisions.md:2918-2982` WAY-127 ·
  `foundations/decisions.md:3188-3266` WAY-134 · `foundations/decisions.md:3268-3313` WAY-135 ·
  `foundations/decisions.md:3315-3390` WAY-136 · `foundations/decisions.md:3510-3559` WAY-140 ·
  `foundations/decisions.md:3664-3697` WAY-144 · `foundations/decisions.md:3779-3806` WAY-147 ·
  `foundations/decisions.md:3808-3866` WAY-148 · `foundations/decisions.md:3868-3926` WAY-150 ·
  `foundations/decisions.md:4125-4152` WAY-158 · `foundations/decisions.md:4154-4182` WAY-159 ·
  `foundations/decisions.md:4184-4213` WAY-160 · `foundations/decisions.md:4215-4268` WAY-161 ·
  `foundations/decisions.md:4270-4321` WAY-162 · `foundations/decisions.md:4323-4359` WAY-163 ·
  `foundations/decisions.md:4361-4397` WAY-164 · `foundations/decisions.md:4702-4740` WAY-172 ·
  `foundations/decisions.md:5782-5837` WAY-213 · `foundations/decisions.md:5840-5875` WAY-214 ·
  `foundations/decisions.md:5948-5968` WAY-217 · `foundations/decisions.md:6008-6040` WAY-219 ·
  `foundations/decisions.md:6043-6063` WAY-220 · `foundations/decisions.md:6066-6090` WAY-221 ·
  `foundations/decisions.md:6143-6164` WAY-227 · `foundations/decisions.md:6216-6292` WAY-229 ·
  `foundations/decisions.md:6655-6699` WAY-238 · `foundations/decisions.md:7168-7202` WAY-253 ·
  `foundations/decisions.md:7204-7234` WAY-254 · `foundations/decisions.md:7236-7267` WAY-255 ·
  `foundations/decisions.md:7269-7326` WAY-256 · `foundations/decisions.md:7408-7437` WAY-260 ·
  `foundations/decisions.md:7439-7472` WAY-261 · `foundations/decisions.md:7474-7489` WAY-262 ·
  `foundations/decisions.md:7491-7516` WAY-263 · `foundations/decisions.md:7518-7553` WAY-264 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/part_map.md:92-100` part task-cycle ·
  `foundations/glossary.md:97-101` open design choice · `foundations/glossary.md:139-143` slice ·
  project-level/technology/reserved_choices.md as Slice 2 makes it · `task-cycle/change/slice.md` ·
  `task-cycle/change/fix.md` · `task-cycle/skill/SKILL.md:174-193` the statuses of the stages ·
  `task-cycle/skill/SKILL.md:222-229` an open design choice met while the change is made
- **Model:** cheaper
- **Risk:** none
- **Checks:** the slice changes no script, so no test comes first. `python -B gate/run_tests.py task-cycle` ·
  `git grep -l -F "reserved_choices.md" -- task-cycle/change/SKILL.md task-cycle/plan/SKILL.md task-cycle/spec/design.md task-cycle/review/SKILL.md`
  lists all four files
- **Depends on:** Slice 2 · the new decision From row 2 · WAY-135 · reserved choice

### Slice 5 — The orchestrator stops the cycle on a reserved choice

- **Goal:** no stage of the cycle settles a reserved choice, and a cycle that meets one ends in a
  blocked draft request with no code, as the spec's decisions 2 and 3 give. The new
  `task-cycle/skill/reserved_return.md`, read when it applies as `blocked_finding.md` is, holds the
  four steps of "What the orchestrator does" and decision 2's branch, the order of its commits and its
  request, what does not run, what the request states and the state after a correction.
  `task-cycle/skill/SKILL.md`: the status list; the two sentences at lines 186–188 and 213–214 except
  a reserved choice; step 4 judges it beside the open design choice; a paragraph under "Design and
  execution choice" points to the new file; step 13 points to it. `correction.md`: its recovery
  sentence names the case, and it gains the case of a request a reserved choice blocked, told apart
  by the record's field *Reserved choice*. `record_template.md`: *Discarded attempt* names the reason,
  and *Spec and execution route* gains that field. `planning.md`: the sentence at lines 10–11 sends a
  planner's `reserved` to the same route. The frontmatter of `SKILL.md` stays, so no entry point
  changes.
- **Change:** `task-cycle/skill/reserved_return.md` · `task-cycle/skill/SKILL.md` ·
  `task-cycle/skill/correction.md` · `task-cycle/skill/planning.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:45-50` Questions to settle, Pytanie 2 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:51-56` Questions to settle, Pytanie 3 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:93-93` Context, the mechanism of the stop ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:99-102` Questions carried to cycle ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:156-215` Decisions, 2. The blocked draft request with no code ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:217-302` Decisions, 3. The rule in the skills and the status of the return ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decisions From row 2 and From this spec of *Foundation entries* ·
  WAY-135 as *Foundation entries* changes it ·
  the glossary term reserved choice of *Foundation entries* ·
  `foundations/decisions.md:6-35` WAY-01 · `foundations/decisions.md:68-93` WAY-03 ·
  `foundations/decisions.md:212-285` WAY-09 · `foundations/decisions.md:287-318` WAY-10 ·
  `foundations/decisions.md:320-355` WAY-11 · `foundations/decisions.md:387-425` WAY-13 ·
  `foundations/decisions.md:450-473` WAY-16 · `foundations/decisions.md:548-566` WAY-21 ·
  `foundations/decisions.md:613-636` WAY-25 · `foundations/decisions.md:638-666` WAY-26 ·
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:696-723` WAY-28 ·
  `foundations/decisions.md:759-796` WAY-30 · `foundations/decisions.md:819-849` WAY-33 ·
  `foundations/decisions.md:851-885` WAY-34 · `foundations/decisions.md:912-936` WAY-36 ·
  `foundations/decisions.md:938-959` WAY-37 · `foundations/decisions.md:961-985` WAY-38 ·
  `foundations/decisions.md:1059-1092` WAY-44 · `foundations/decisions.md:1094-1117` WAY-45 ·
  `foundations/decisions.md:1119-1147` WAY-48 · `foundations/decisions.md:1173-1217` WAY-51 ·
  `foundations/decisions.md:1283-1307` WAY-55 · `foundations/decisions.md:1433-1460` WAY-62 ·
  `foundations/decisions.md:1462-1489` WAY-63 · `foundations/decisions.md:1523-1544` WAY-65 ·
  `foundations/decisions.md:1546-1566` WAY-68 · `foundations/decisions.md:1568-1588` WAY-69 ·
  `foundations/decisions.md:1786-1818` WAY-82 · `foundations/decisions.md:1905-1928` WAY-89 ·
  `foundations/decisions.md:2118-2140` WAY-100 · `foundations/decisions.md:2142-2160` WAY-101 ·
  `foundations/decisions.md:2162-2186` WAY-102 · `foundations/decisions.md:2188-2208` WAY-103 ·
  `foundations/decisions.md:2249-2270` WAY-106 · `foundations/decisions.md:2623-2694` WAY-121 ·
  `foundations/decisions.md:2790-2835` WAY-124 · `foundations/decisions.md:2837-2874` WAY-125 ·
  `foundations/decisions.md:2876-2916` WAY-126 · `foundations/decisions.md:2918-2982` WAY-127 ·
  `foundations/decisions.md:3188-3266` WAY-134 · `foundations/decisions.md:3268-3313` WAY-135 ·
  `foundations/decisions.md:3315-3390` WAY-136 · `foundations/decisions.md:3510-3559` WAY-140 ·
  `foundations/decisions.md:3664-3697` WAY-144 · `foundations/decisions.md:3779-3806` WAY-147 ·
  `foundations/decisions.md:3808-3866` WAY-148 · `foundations/decisions.md:3868-3926` WAY-150 ·
  `foundations/decisions.md:3990-4020` WAY-153 · `foundations/decisions.md:4125-4152` WAY-158 ·
  `foundations/decisions.md:4154-4182` WAY-159 · `foundations/decisions.md:4184-4213` WAY-160 ·
  `foundations/decisions.md:4215-4268` WAY-161 · `foundations/decisions.md:4270-4321` WAY-162 ·
  `foundations/decisions.md:4323-4359` WAY-163 · `foundations/decisions.md:4361-4397` WAY-164 ·
  `foundations/decisions.md:4702-4740` WAY-172 · `foundations/decisions.md:5782-5837` WAY-213 ·
  `foundations/decisions.md:5840-5875` WAY-214 · `foundations/decisions.md:5948-5968` WAY-217 ·
  `foundations/decisions.md:6008-6040` WAY-219 · `foundations/decisions.md:6043-6063` WAY-220 ·
  `foundations/decisions.md:6066-6090` WAY-221 · `foundations/decisions.md:6143-6164` WAY-227 ·
  `foundations/decisions.md:6216-6292` WAY-229 · `foundations/decisions.md:6655-6699` WAY-238 ·
  `foundations/decisions.md:7168-7202` WAY-253 · `foundations/decisions.md:7204-7234` WAY-254 ·
  `foundations/decisions.md:7236-7267` WAY-255 · `foundations/decisions.md:7269-7326` WAY-256 ·
  `foundations/decisions.md:7408-7437` WAY-260 · `foundations/decisions.md:7439-7472` WAY-261 ·
  `foundations/decisions.md:7474-7489` WAY-262 · `foundations/decisions.md:7491-7516` WAY-263 ·
  `foundations/decisions.md:7518-7553` WAY-264 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/part_map.md:92-100` part task-cycle ·
  `foundations/glossary.md:61-65` foundation step · `foundations/glossary.md:79-83` human action ·
  `foundations/glossary.md:97-101` open design choice ·
  `foundations/glossary.md:133-137` return step · `foundations/glossary.md:139-143` slice ·
  project-level/technology/reserved_choices.md as Slice 2 makes it ·
  `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/foundation_step.md` ·
  `task-cycle/skill/spec_review.md` ·
  `task-cycle/change/SKILL.md:97-110` When you return without code, as Slice 4 changes it
- **Model:** same — the stop runs through steps 4, 6, 12 and 13 and the correction, and its one departure from step 12's order of commits has to be worded against WAY-135, WAY-162 and WAY-227.
- **Risk:** none
- **Checks:** the slice changes no script, so no test comes first. `python -B gate/run_tests.py task-cycle` ·
  `python -B instruction-files/check_instructions.py . --file task-cycle/skill/reserved_return.md`
  exits 0 · `git grep -l -F "reserved_return.md" -- task-cycle/skill/SKILL.md` lists that file ·
  `git grep -n -F "smallest reversible" -- task-cycle`, each line read: every sentence that gives the
  smallest reversible reading excepts a reserved choice
- **Depends on:** Slice 2 · Slice 4 · the new decisions From row 2 and From this spec · WAY-135 ·
  reserved choice

### Slice 6 — A task comes back after the human closes the draft

- **Goal:** a task whose blocked request the human closed can return to refinement and start a new
  cycle under the same name, as the spec's decision 5 gives. `project-level/lead/skill/SKILL.md` step 1
  gains the new supported transition, on the human's word, of a row reading `in cycle` or
  `ready for cycle` to `to refine` with a change-log line naming the request, and the removal of that
  one cycle's trace before it, in the four steps and the order decision 5 gives, by name and with no
  `git fetch --prune`. `project-level/plan/template.md` says, beside the states, that a row goes back
  only as `lead-project` gives. `project-level/test_plan_state.py` gains, beside
  `test_conflicting_unfinished_and_abandoned_states_never_advance`, the other half this design rests
  on: with the branch deleted on the host the conflict stays while the remote-tracking ref stands, and
  with that ref and the local branch gone the row reports none. `plan_state.py` does not change and
  the slice alters no invariant test. The frontmatter of `SKILL.md` stays, so no entry point changes.
- **Change:** `project-level/lead/skill/SKILL.md` · `project-level/plan/template.md` ·
  `project-level/test_plan_state.py`
- **Read:** `.runs/task-cycles/unsettled-technology-returns/task.md:24-35` To do ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:51-56` Questions to settle, Pytanie 3 ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:99-102` Questions carried to cycle ·
  `.runs/task-cycles/unsettled-technology-returns/task.md:134-142` Settlements to record ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:19-44` Goals and non-goals ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:46-76` Constraints ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:404-469` Decisions, 5. The next cycle of the same task ·
  `.runs/task-cycles/unsettled-technology-returns/spec.md:504-514` Left to the maker ·
  the new decision From this spec of *Foundation entries* ·
  the glossary term reserved choice of *Foundation entries* ·
  `foundations/decisions.md:212-285` WAY-09 · `foundations/decisions.md:961-985` WAY-38 ·
  `foundations/decisions.md:1905-1928` WAY-89 · `foundations/decisions.md:2118-2140` WAY-100 ·
  `foundations/decisions.md:2142-2160` WAY-101 · `foundations/decisions.md:2162-2186` WAY-102 ·
  `foundations/decisions.md:2249-2270` WAY-106 · `foundations/decisions.md:2272-2293` WAY-107 ·
  `foundations/decisions.md:2295-2321` WAY-108 · `foundations/decisions.md:2323-2341` WAY-109 ·
  `foundations/decisions.md:2343-2362` WAY-110 · `foundations/decisions.md:2364-2388` WAY-111 ·
  `foundations/decisions.md:2390-2415` WAY-112 · `foundations/decisions.md:2417-2448` WAY-113 ·
  `foundations/decisions.md:2450-2474` WAY-114 · `foundations/decisions.md:2476-2502` WAY-115 ·
  `foundations/decisions.md:2504-2526` WAY-116 · `foundations/decisions.md:2528-2557` WAY-117 ·
  `foundations/decisions.md:2559-2593` WAY-118 · `foundations/decisions.md:2595-2621` WAY-120 ·
  `foundations/decisions.md:2623-2694` WAY-121 · `foundations/decisions.md:2696-2750` WAY-122 ·
  `foundations/decisions.md:2752-2788` WAY-123 · `foundations/decisions.md:2790-2835` WAY-124 ·
  `foundations/decisions.md:2876-2916` WAY-126 · `foundations/decisions.md:2918-2982` WAY-127 ·
  `foundations/decisions.md:3188-3266` WAY-134 · `foundations/decisions.md:3268-3313` WAY-135 ·
  `foundations/decisions.md:3392-3427` WAY-137 · `foundations/decisions.md:3429-3472` WAY-138 ·
  `foundations/decisions.md:3474-3508` WAY-139 · `foundations/decisions.md:3510-3559` WAY-140 ·
  `foundations/decisions.md:3582-3628` WAY-142 · `foundations/decisions.md:3630-3662` WAY-143 ·
  `foundations/decisions.md:3664-3697` WAY-144 · `foundations/decisions.md:3699-3740` WAY-145 ·
  `foundations/decisions.md:3742-3777` WAY-146 · `foundations/decisions.md:3779-3806` WAY-147 ·
  `foundations/decisions.md:3868-3926` WAY-150 · `foundations/decisions.md:3928-3960` WAY-151 ·
  `foundations/decisions.md:3962-3988` WAY-152 · `foundations/decisions.md:3990-4020` WAY-153 ·
  `foundations/decisions.md:4022-4057` WAY-154 · `foundations/decisions.md:4059-4091` WAY-155 ·
  `foundations/decisions.md:4093-4123` WAY-156 · `foundations/decisions.md:4399-4441` WAY-165 ·
  `foundations/decisions.md:4443-4472` WAY-166 · `foundations/decisions.md:4702-4740` WAY-172 ·
  `foundations/decisions.md:5840-5875` WAY-214 · `foundations/decisions.md:5878-5919` WAY-215 ·
  `foundations/decisions.md:5922-5945` WAY-216 · `foundations/decisions.md:5948-5968` WAY-217 ·
  `foundations/decisions.md:5971-6005` WAY-218 · `foundations/decisions.md:6143-6164` WAY-227 ·
  `foundations/decisions.md:6294-6335` WAY-230 · `foundations/decisions.md:6655-6699` WAY-238 ·
  `foundations/decisions.md:6804-6851` WAY-242 · `foundations/decisions.md:6970-6993` WAY-247 ·
  `foundations/decisions.md:7269-7326` WAY-256 ·
  `foundations/invariants.md:6-14` foundation-file-kinds ·
  `foundations/invariants.md:16-24` foundation-change-merge-route ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/invariants.md:46-54` return-step-record ·
  `foundations/invariants.md:56-64` derived-file-content ·
  `foundations/invariants.md:66-74` ci-checking-commands ·
  `foundations/invariants.md:76-84` outbound-link-reach ·
  `foundations/invariants.md:96-104` script-language ·
  `foundations/invariants.md:106-114` script-imports ·
  `foundations/invariants.md:116-124` script-subprocesses ·
  `foundations/invariants.md:136-144` map-reference-target ·
  `foundations/invariants.md:176-185` project-definition-form ·
  `foundations/invariants.md:187-196` project-readiness-gate ·
  `foundations/invariants.md:198-206` project-technology-record ·
  `foundations/invariants.md:208-220` project-plan-form ·
  `foundations/invariants.md:222-239` project-plan-check ·
  `foundations/invariants.md:241-249` skill-entry-points ·
  `foundations/invariants.md:251-259` instruction-file-imports ·
  `foundations/invariants.md:281-296` project-plan-state-evidence ·
  `foundations/invariants.md:298-306` project-plan-state-subprocesses ·
  `foundations/part_map.md:77-90` part project-level ·
  `foundations/glossary.md:157-161` project orchestrator ·
  `project-level/plan_state.py:72-124` observe · `project-level/plan_state.py:332-431` task_report ·
  `project-level/task/skill/draft.md` ·
  `task-cycle/skill/SKILL.md:110-121` steps 4 and 5, the branch and the record's name ·
  `task-cycle/skill/SKILL.md:360-377` step 12, the record's pair of commits
- **Model:** cheaper
- **Risk:** none
- **Checks:** the test pins behaviour that stands, so it passes when written and no failing run comes
  first; its two halves, one fixture with opposite results, are each other's control, and you name the
  break it catches. `python -B -m unittest discover -s project-level -p "test_plan_state.py"` ·
  `python -B gate/run_tests.py project-level` · `git diff --exit-code <slice's base> -- project-level/plan_state.py project-level/plan_check.py project-level/test_plan_state_invariant.py`
  exits 0
- **Depends on:** Slice 3 · the new decision From this spec · reserved choice

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: a choice the project never settled returns to the human before code stands on it | the new decisions From row 1 and row 2, Slices 1 to 6 |
| To do 1: the step runs outside a definition, with a note; with no task it starts through `refine-task` | Slice 1 |
| To do 2: it reads the task document, keeps its list and progress there, resumes, passes no gate, ends in refinement | Slice 1 |
| To do 3: it settles what the note and the task name, the rest as at a definition; a held choice opens only on the human's word | Slice 1 |
| To do 4: each settled choice stands in the task document with all the cycle needs; the template has its place | Slice 1 |
| To do 5: refinement that sees a reserved choice runs the step; the task is not ready until the human settles it | Slice 2 |
| To do 6: a plan member does the same at its document; in orchestrated refinement the request goes through the conversation, the table in the round package | Slice 2, Slice 3 |
| To do 7: the cycle takes no such choice; report without code, discarded attempt, blocked draft naming the choice | Slice 4, Slice 5 |
| To do 8: after the human closes the draft the document returns to refinement with its answers and rows, and a new cycle starts after acceptance | Slice 2, Slice 6 |
| To do 9: the rule carries boundary examples | Slice 2 |
| To do 10: every other choice stays in the cycle and its questions table; the tools of the guideline skills stay on their routes | Slice 2, Slice 4 |
| Row 1 | the new decision From row 1 |
| Row 2 | the new decision From row 2 |
| Row 3 | WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-135 |
| Question carried: how the blocked draft looks with no code | Slice 5, the new decision From this spec |
| Question carried: how the next cycle names its record, and who moves the plan row back | Slice 6, the new decision From this spec |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Six slices, cut by who reads each text: the step, refinement, the orchestrated round, the stage agents, the orchestrator, the return of a plan row | The orchestrator's four seams, with the stage agents and the orchestrator in one slice and the return of a row inside the cycle's slice | Two slices word one contract apart and drift; the review of the whole change finds it and one fix pays for it |
| `elements/decisions/template.md` in Slice 1, so one agent names the three fields in both templates | A slice of its own for a file of the part `decisions` | Slice 1's agent reads the decisions of a further part; an agent of its own would read most of them for two rules |
| `reserved_choices.md` in Slice 2, where its first reader `resolve_gaps.md` stands, ahead of Slices 4 and 5 that point to it | In Slice 1 beside the step's other files | Slice 1 cannot link the rule by path and speaks of it through the glossary term; the review of the whole change sees the whole |
| `draft.md` in Slice 2 with the rest of `refine-task` | In Slice 6 with the rest of the spec's decision 5 | A reader of Slice 6 alone does not see the document's half of the return; the whole-change review reads both |
| `project-level/lead/skill/SKILL.md` changed by Slices 3 and 6, for steps 3 and 1, Slice 6 depending on Slice 3 | Both in one slice, which would tie the removal of a cycle's trace to the orchestrated round | One more agent reads that file; no text overlaps |
| `task-cycle/skill/planning.md` added to Slice 5, though the spec's table does not list it: its sentence sends what a planner returns to step 6, and a reserved choice is also an open design choice by the glossary | Left as it stands, the status list of `task-cycle/skill/SKILL.md` alone carrying a planner's `reserved` | A planner's report takes the spec's route for a choice the human keeps; if the clause is not needed, one clause too many |
| *Read* names every decision whose *Scope* names a touched part, with the invariants of that part or of `every`, as "Reading the foundation" selects (WAY-150) | Only the entries that bear on the slice's text | Each agent reads more than its text needs, the cost the size report shows; the narrow way would be the breach WAY-150 names |
| The entry points' two directories count in Slice 1 only, the one slice that changes a description | The generator run in every slice that touches a `SKILL.md` | A maker who changes a description in another slice has to run it too, and the gate's tests say so |
| Slice 6's test stands in `project-level/test_plan_state.py`, as the spec names, and cites no invariant | In `project-level/test_plan_state_invariant.py` | It is not read as a test of `project-plan-state-evidence`; that invariant stays unchanged either way |
