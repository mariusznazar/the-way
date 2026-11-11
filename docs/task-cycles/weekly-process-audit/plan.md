# Plan — the way: cotygodniowy audyt, czy proces faktycznie staje się lepszy, tańszy i szybszy

- Task: `.runs/task-cycles/weekly-process-audit/task.md`
- Spec: none
- Base: `e3825a82386a61930a86f8517fc0c5f422fc2833`

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Row 1 — the-way gives the template of the register of problems; the audit reads the register a locations entry names; the user's own tool fills it and the user adapts the template | decision | *Settlements to record* row 1 | Slice 1 · Slice 5 · Slice 7 |
| Row 2 — the audit is a part of its own with its own directory, apart from the task cycle | decision | *Settlements to record* row 2 | Slice 1 · Slice 7 |
| Row 3 — the audit's results lie in the user's place outside every repository, named by a locations entry | decision | *Settlements to record* row 3 | Slice 3 · Slice 7 |
| Row 4 — four levels of weight, and a list of classes the template starts and the audit widens | decision | *Settlements to record* row 4 | Slice 1 · Slice 5 · Slice 6 |
| Row 5 — the audit counts problems, not remarks: one problem reported by several stages is one | decision | *Settlements to record* row 5 | Slice 1 · Slice 5 |
| Row 6 — whether a fix works is settled by the cycles whose the-way version holds it, not by a date | decision | *Settlements to record* row 6 | Slice 5 |
| Row 7 — how often an issue comes back is material for the human to weigh; the audit sets no priority from it | decision | *Settlements to record* row 7 | Slice 5 · Slice 7 |
| Row 8 — a cycle's cost is its cost at constant prices from a dated price list and the share of fix rounds in it, with no denominator of task size | decision | *Settlements to record* row 8 | Slice 2 · Slice 4 · Slice 6 |
| Row 9 — a cycle's time is the agents' working time without the wait for the human, and apart the wait for tools | decision | *Settlements to record* row 9 | Slice 2 · Slice 3 |
| Row 10 — a new price list, or a change of a stage report's form, of the list of classes or of the reviewer's instructions, starts a new series; measures compare within a series and a process version | decision | *Settlements to record* row 10 | Slice 4 · Slice 6 · Slice 7 |
| Row 11 — the audit replays no frozen earlier tasks on an old and a new process version | decision | *Settlements to record* row 11 | Slice 7 |
| Row 12 — the audit runs weekly, apart from the weekly review; the counting runs unattended on the night from Friday to Saturday, and a weekly backlog task starts the session | decision | *Settlements to record* row 12 | Slice 3 · Slice 7 |
| WAY-09 changed — the list of the repository's directories gains the audit part's directory, and the sentence of what a directory must hold gains what that one holds | decision | *To do* item 1 | Slice 1 |
| WAY-38 changed — its *Scope* gains `process-audit`, whose command is a script of the-way | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-89 changed — its *Scope* gains `process-audit` | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-320 changed — its *Scope* gains `process-audit`, whose skill and command read the locations file | decision | *To do* item 6, through WAY-21 | Slice 3 · Slice 5 · Slice 7 |

The rows and the changes name the part `process-audit`, whose part-map entry Slice 1 writes with the
first file of its directory (`task-cycle/plan/SKILL.md`: a change to the part map for a file the
change adds belongs to the slice that adds the file). Until Slice 1 is made,
`python -B elements/common/foundation_check.py --skip-test-citations` reports the references to that
part, and only those; after Slice 1 it reports nothing.

## Slices

### Slice 1 — The audit part and the template of its register of problems

- **Goal:** The repository holds the directory `process-audit/` of a new part `process-audit`, with
  the template of the register of problems, `process-audit/problem_register.md`, and the part map
  holds the part's entry, written through the-way's skill `update-part-map`. The template gives, for
  each problem: the cycle record it comes from (the repository and the commit that adds the record's
  copy, as `task-cycle/record_template.md` has the copy committed), the stages that reported it, its
  class, its weight, the issue it belongs to, that issue's fate and, for an issue whose fix is in
  place, the commit of the-way that holds the fix. It carries the starting list of classes
  (confirmation; a check not run or uncertain; an ambiguity settled by an agent's choice; a gap in
  the product's foundation; a known problem left; a stale reference in a task or a plan; a remark
  about the process) and the scale of weight (no problem, Minor, Important, Critical — the cycle
  review's scale with a level zero), in a form that the counting command `process-audit/audit_count.py`
  of later slices reads, a change of the list of classes included, since such a change starts a
  new series (Foundation entries row 10). It says that the user's own tool fills the register, that
  the user adapts the template, that one problem reported by several stages is one problem, and that
  the register lies in the user's place a locations entry names, never in a repository. The part's
  entry: its sentence names what the part answers for — the audit of whether the process gets
  better, cheaper and faster across cycles: the register's template, the price list, the counting
  command and the skill of the weekly session; *Files* `process-audit/**`; *Depends on*
  `task-cycle · project-level` (the form of the cycle record, the reading of a locations entry);
  *Trust boundary* none, since the command it will name does not exist yet (Slice 3 names it). The
  template holds no absolute path, no note link and no name of a person or a product. Name in your
  report the shape the template takes.
- **Change:** `process-audit/problem_register.md` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 1 · Foundation entries row 2 · Foundation entries row 4 · Foundation entries row 5 · Foundation
  entries row 10 · Foundation entries WAY-09 changed · `foundations/decisions.md:1044-1165` WAY-40 ·
  WAY-41 · WAY-42 · WAY-44 · `foundations/decisions.md:1192-1220` WAY-48 ·
  `foundations/decisions.md:2309-2329` WAY-103 · `foundations/decisions.md:10321-10384` WAY-320 ·
  `foundations/invariants.md:26-34` repository-file-location · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:146-154` map-reference-target ·
  `task-cycle/record_template.md`
- **Model:** strongest — it settles the shape of the register that users' tools fill and that
  Slice 5 parses.
- **Risk:** none
- **Checks:** after committing, `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B gate/run_tests.py elements/part-map` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0
- **Depends on:** Foundation entries row 1 · row 2 · row 4 · row 5 · row 10 · WAY-09 changed

### Slice 2 — The wait for tools in the stages of a cycle

- **Goal:** `task-cycle/cycle_stages.py` gives in its report, `stages.md`, for each stage the time
  it waited for tools — the time from a tool call to its result in the transcripts of Codex and
  Claude Code; a call that starts a subagent, sends it a message or waits for it is no wait for a
  tool, its time being the subagent's work — and in the summary the cycle's time waiting for tools
  and its working time without it, the two together making the working time the report gives
  today. It also gives each stage's start time and its tokens by model and by kind (input, cached
  input, output), so that the audit can price each stage at its model's price and tie a stage to
  the record's events. A transcript whose tool calls the reader does not recognise gives a
  `Warning:` line as the report does today, never a wait of zero. The docstring says what counts
  as a wait for a tool. Name in your report the tool names you take for a subagent call in each
  tool, and where you read them.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:67-71` Context · Foundation entries row 8 ·
  Foundation entries row 9 · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1991-2014` WAY-89 · `foundations/decisions.md:4141-4208` WAY-148 ·
  `foundations/decisions.md:6711-6788` WAY-229 · `foundations/decisions.md:7743-7775` WAY-255 ·
  `foundations/invariants.md:106-134` script-language · script-imports · script-subprocesses ·
  `task-cycle/skill/SKILL.md:433-441` step 12, the record of stage times
- **Model:** cheaper
- **Risk:** none
- **Checks:** first a failing test: a Claude Code transcript and a Codex rollout, each with one tool
  call and one subagent call in a stage, whose stage's wait for tools counts the tool call and not
  the subagent call ·
  `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` ·
  `python -B task-cycle/cycle_stages.py <the id of one of your own earlier sessions> --output
  <a file outside the repository>` exits 0, with the waits read and its warnings named in the report
- **Depends on:** Foundation entries row 8 · row 9

### Slice 3 — The counting command: the cycles of the named repositories and their times

- **Goal:** `process-audit/audit_count.py` exists. It finds the place of the register of problems
  and the place of the audit's results through entries of the locations file under `the-way`
  (WAY-320; the reading as `project-level/backlog_place.md` gives it), and where the file, the
  key, the entry or its path is missing it names the missing entry in an `Error:` line and exits
  non-zero without asking anything, so that the skill of Slice 7 asks the human. It takes the
  repositories whose cycles it reads as the user names them. It runs with no human: no prompt, git
  with its terminal prompt off, nothing read from stdin, so that a system scheduler can start it on
  the night from Friday to Saturday (Foundation entries row 12). It finds every cycle record
  committed in the history of each repository — the copy under `docs/task-cycles/<task-slug>/` that
  one commit adds and the next removes (`task-cycle/record_template.md`; `project-level/plan_state.py`
  reads such archived copies) — and identifies each cycle by its repository and the commit that adds
  the record, as the register of Slice 1 does. For each cycle it gives: the version of the-way the
  cycle ran on (the record's *Process pin*); the number of its process remarks (the entries under
  *Process remarks on the-way*; it may reuse the cutting of `task-cycle/remarks_check.py`); the
  agents' working time without the wait for tools, and the wait for tools, from the cycle's
  `stages.md` as Slice 2 gives it. A record or a `stages.md` in an earlier form that lacks a value
  gives `unknown` for it, never zero. It writes its result into the place of the audit's results,
  never into a repository, in a form that later slices extend and the skill reads. Every record,
  `stages.md` and the locations file is untrusted input: text from them stays within one line of
  output, as `display` in `project-level/plan_state.py` keeps it; no path taken from them is
  followed beyond what git lists; nothing of them is run. Its tests give crafted input — control
  characters, a record path that leaves its directory, a malformed table, a missing or a doubled
  field. The docstring gives the usage and the exit codes. In the part map, the part's *Trust
  boundary* names `process-audit/audit_count.py`, and its *Depends on* names every part whose file
  the command imports. Name in your report the entries read from the locations file, how the user
  names the repositories, and the shape of the result.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:67-71` Context ·
  `.runs/task-cycles/weekly-process-audit/task.md:77-80` Human actions · Foundation entries row 3 ·
  Foundation entries row 9 · Foundation entries row 12 · Foundation entries WAY-38 changed ·
  Foundation entries WAY-320 changed · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1192-1220` WAY-48 · `foundations/decisions.md:1222-1245` WAY-49 ·
  `foundations/decisions.md:1991-2014` WAY-89 · `foundations/decisions.md:2410-2446` WAY-107 · `foundations/decisions.md:3843-3892` WAY-140 ·
  `foundations/decisions.md:7967-7996` WAY-260 · `foundations/decisions.md:9411-9431` WAY-296 ·
  `foundations/decisions.md:10321-10384` WAY-320 · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:106-134` script-language · script-imports ·
  script-subprocesses · `foundations/invariants.md:328-336` cross-part-imports ·
  `task-cycle/record_template.md` · `task-cycle/remarks_check.py` · `task-cycle/cycle_stages.py` ·
  `project-level/plan_state.py` · `project-level/backlog_place.md` · process-audit/problem_register.md
  as Slice 1 made it
- **Model:** strongest — it sets the shape of the command's result, the entries it reads from the
  locations file and the way it finds cycle records in the history of repositories, on which
  Slices 4 to 7 build.
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records and `stages.md`
  of repositories the user names, and the user's locations file
- **Checks:** first a failing test: a temporary git repository with a commit that adds a record copy
  and the next that removes it, from which the command gives the cycle with its *Process pin* and
  its number of remarks · `python -B gate/run_tests.py process-audit` ·
  `python -B gate/run_tests.py elements/part-map` · after committing,
  `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, as its usage gives, with its exit code and the
  result's first lines in the report
- **Depends on:** Slice 1 · Slice 2 · Foundation entries row 3 · row 9 · row 12 · WAY-38 changed ·
  WAY-320 changed

### Slice 4 — The cost of a cycle at constant prices

- **Goal:** `process-audit/price_list.md` holds the price list with its date: for every model the
  cycles' `stages.md` name, its price per million tokens of input, of cached input and of output,
  each taken from the provider's published price page with the page's address and the date it was
  read, never from memory; a model whose price no page gives stands with no price. The command
  `process-audit/audit_count.py` gives for each cycle its cost at the list's prices and the share of
  that cost spent on rounds of fixes after a review — the fix of a review's blocking findings and
  the review of that fix, as the record's *Review rounds* and *Events* name them, tied to the stages
  of `stages.md` — with no denominator of task size (Foundation entries row 8). A model the list
  lacks, or a `stages.md` without each stage's tokens by model and kind, gives `unknown` with its
  reason, never a cost of zero. The list's date marks the series a cost belongs to, so that a new
  price list starts a new series (Foundation entries row 10). The record and `stages.md` stay
  untrusted input, as in Slice 3, with tests of crafted input. Name in your report how the command
  recognises the stages of a fix round.
- **Change:** `process-audit/price_list.md` · `process-audit/audit_count.py` ·
  `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 8 · Foundation entries row 10 · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1192-1220` WAY-48 · `foundations/invariants.md:106-134` script-language ·
  script-imports · script-subprocesses · `task-cycle/record_template.md` ·
  `task-cycle/cycle_stages.py`
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records and `stages.md`
  of repositories the user names
- **Checks:** first a failing test: a record with one fix round and a `stages.md` whose stages use
  two models, from which the command gives the cost and the share of the fix round at a test price
  list · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, with its exit code in the report
- **Depends on:** Slice 3 · Foundation entries row 8 · row 10

### Slice 5 — Problems and issues from the register

- **Goal:** `process-audit/audit_count.py` reads the register of problems at the place its
  locations entry names (Slice 3), in the form of `process-audit/problem_register.md` (Slice 1), and
  gives: for each cycle, its problems by class and by weight, one problem that several stages
  reported counted once (Foundation entries row 5); for each issue whose fix is in place, the
  problems of that issue in the cycles whose *Process pin* holds the fix's commit — the fix an
  ancestor of the pin in the-way's history — and apart in the cycles whose pin does not hold it,
  never by a date (row 6); for each open issue, the number of cycles in which its problem came back
  and the number of days it has waited. It gives no ranking and no priority from how often an issue
  comes back (row 7). A problem whose cycle no named repository holds, or a pin or a fix commit
  the-way's history lacks, gives `unknown` with its reason. The register is untrusted input, with
  tests of crafted input as in Slice 3. Name in your report which repository of the-way answers
  whether a pin holds a fix, and from what date the days of waiting count.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 1 · Foundation entries row 4 · Foundation entries row 5 · Foundation entries row 6 · Foundation
  entries row 7 · `foundations/decisions.md:1192-1220` WAY-48 ·
  `foundations/decisions.md:10321-10384` WAY-320 · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1991-2014` WAY-89 · `foundations/invariants.md:106-134`
  script-language · script-imports · script-subprocesses ·
  `task-cycle/record_template.md:1-15` Cycle record ·
  process-audit/problem_register.md as Slice 1 made it
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the user's register of problems
- **Checks:** first a failing test: a temporary repository of the-way with a fix commit and two pins,
  one holding it, and a register with one issue whose problem stands in a cycle of each pin, from
  which the command gives the two counts apart · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command with a test register and stdin closed, with its exit code in the report
- **Depends on:** Slice 1 · Slice 4 · Foundation entries row 1 · row 4 · row 5 · row 6 · row 7

### Slice 6 — The measures of each process version, series kept apart

- **Goal:** `process-audit/audit_count.py` gives for each version of the process — the cycles
  grouped by their *Process pin* — the median of the cycle cost at constant prices, and the answers
  to three questions about simplifying the rules of the spec and the plan: did a contradiction with
  the product's settlements come out only after code was written (the record's *Discarded attempt*
  for an open design choice, or a review round whose blocking finding names a foundation entry);
  did more than one in three slices of the plans come back as too large (the record's *Plan* and
  *Slices returned too large*); does the cycle cost fall (the median against the previous version
  in the same series). A series starts anew with a new price list (Slice 4), a change of the
  register's list of classes (Slice 1), and a change, between two pins, of the form of a stage's
  report — in the methods under `task-cycle/change/`, `task-cycle/plan/`, `task-cycle/review/` and
  `task-cycle/spec/` — or of the reviewer's instructions under `task-cycle/review/`; the result never
  compares numbers of two series directly and shows them apart (Foundation entries row 10). An
  answer the records cannot give is `unknown` with its reason. The records stay untrusted input,
  with tests of crafted input. Name in your report how the versions are grouped and how a change of
  a report's form is told from another change of those files.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 4 · Foundation entries row 8 · Foundation entries row 10 · `foundations/decisions.md:1192-1220`
  WAY-48 · `foundations/decisions.md:1018-1042` WAY-38 · `foundations/invariants.md:106-134`
  script-language · script-imports · script-subprocesses · `foundations/glossary.md:97-101` open design choice · `foundations/glossary.md:145-149`
  slice · `task-cycle/record_template.md`
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records of repositories
  the user names
- **Checks:** first a failing test: cycles of two pins in one series and one cycle after a new price
  list, from which the command gives each version's median, compares the first two and does not
  compare across the series · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, with its exit code in the report
- **Depends on:** Slice 4 · Slice 5 · Foundation entries row 4 · row 8 · row 10

### Slice 7 — The skill of the weekly audit session

- **Goal:** `process-audit/SKILL.md`, the skill `audit-process`, leads the weekly audit session with
  the human, a session of its own apart from any weekly review (Foundation entries row 12). It finds
  the place of the audit's results and the register through their locations entries as
  `project-level/backlog_place.md` ("Resolve an entry of the locations file") gives, asking the human
  where an entry is missing; reads the latest result of the counting command
  `process-audit/audit_count.py`; shows the human the issues to weigh — what came back after a fix,
  what still waits and for how long, what each process version's measures and three answers show
  within a series — never giving an issue priority from how often it comes back alone (row 7) and
  never comparing two series directly (row 10); and writes the audit's result into the place of the
  audit's results, never into a repository (row 3). It says that the user's own tool fills the
  register from the template, which the user adapts (row 1); that the counting runs unattended on
  the night from Friday to Saturday, started by a system scheduler the human sets up, and that a
  weekly task the human adds to the backlog starts the session (row 12; both are human actions,
  WAY-140); and that no set of frozen earlier tasks is replayed (row 11). It is written for any
  builder who adopts the-way (WAY-103): "the human", no person's name, no absolute path and no note
  link. Each step every use comes to stays in `SKILL.md` (WAY-256). After writing the skill, run
  `python -B agent-instructions/skill_entry_points.py --write`, handle any obsolete output path it
  reports for removal, and commit all of its output; never edit that output by hand. `README.md`
  names `process-audit/` among the repository's directories and among the directories that hold a
  skill.
- **Change:** `process-audit/SKILL.md` · `.claude/skills/the-way-*/SKILL.md` ·
  `.agents/skills/the-way-*/SKILL.md` · `README.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:17-21` Need ·
  `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:77-80` Human actions ·
  `.runs/task-cycles/weekly-process-audit/task.md:110-112` Out of scope · Foundation entries row 1 ·
  Foundation entries row 2 · Foundation entries row 3 · Foundation entries row 7 · Foundation entries
  row 10 · Foundation entries row 11 · Foundation entries row 12 · `foundations/decisions.md:2309-2329`
  WAY-103 · `foundations/decisions.md:2410-2446` WAY-107 · `foundations/decisions.md:2571-2624` WAY-113 ·
  `foundations/decisions.md:3177-3242`
  WAY-127 · `foundations/decisions.md:3843-3892` WAY-140 · `foundations/decisions.md:7776-7885`
  WAY-256 · `foundations/decisions.md:8114-8140` WAY-265 · `foundations/decisions.md:10321-10384`
  WAY-320 · `foundations/glossary.md:79-83` human action · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:261-269` skill-entry-points ·
  `foundation-review/SKILL.md` · `project-level/backlog_place.md` · process-audit/audit_count.py
  and process-audit/problem_register.md as Slices 1 to 6 made them
- **Model:** same — it writes a skill of the process that leads a session with the human and has to
  agree with the command's result, the register and the user's places set by Slices 1 to 6.
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py` lists nothing to create or
  change · `python -B gate/run_tests.py gate` · `python -B gate/run_tests.py agent-instructions` ·
  after committing, `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0
- **Depends on:** Slice 1 · Slice 6 · Foundation entries row 1 · row 2 · row 3 · row 7 · row 10 ·
  row 11 · row 12

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Need: a periodic check whether the process gets better, cheaper and faster and whether a fix removes its problem, as one picture | Slices 3 to 7 |
| To do 1: own part and directory, part-map entry, WAY-09 changed | WAY-09 changed · Slice 1 |
| To do 2: template of the register — fields per problem, starting classes, weight scale, user adapts it | Slice 1 · rows 1, 4, 5 |
| To do 3, per cycle: process version, number of remarks, problems by class and weight once each, cost at constant prices, share of fix rounds, agents' time, wait for tools | Slice 3 (version, remarks, times) · Slice 4 (cost, share) · Slice 5 (problems) |
| To do 3, per issue in place: returns in cycles whose version holds the fix, apart from those without | Slice 5 |
| To do 3, per open issue: cycles it came back in, days waiting | Slice 5 |
| To do 3, per process version: median cost and the three questions | Slice 6 |
| To do 4: dated price list in the part, a new list starts a series; a change of report form, class list or reviewer instructions starts a series; no direct comparison across series | Slice 4 · Slice 6 · row 10 |
| To do 5: the skill of the weekly session — reads the count, shows issues to weigh without priority from frequency, writes the result in the user's place | Slice 7 · rows 3, 7 |
| To do 6: register and results place named by locations entries under `the-way`; found as the backlog is; the human asked where missing | Slice 3 (command) · Slice 5 (register) · Slice 7 (skill) · WAY-320 changed |
| To do 7: `stages.md` gives the wait for tools apart; a subagent call is the subagent's work | Slice 2 |
| To do 8: the counting runs with no human, for a scheduler on the night from Friday to Saturday | Slice 3 |
| Settlement row 1 | Foundation entries row 1 · Slices 1, 5, 7 |
| Settlement row 2 | Foundation entries row 2 · Slice 1 |
| Settlement row 3 | Foundation entries row 3 · Slices 3, 7 |
| Settlement row 4 | Foundation entries row 4 · Slices 1, 5 |
| Settlement row 5 | Foundation entries row 5 · Slices 1, 5 |
| Settlement row 6 | Foundation entries row 6 · Slice 5 |
| Settlement row 7 | Foundation entries row 7 · Slices 5, 7 |
| Settlement row 8 | Foundation entries row 8 · Slices 2, 4, 6 |
| Settlement row 9 | Foundation entries row 9 · Slices 2, 3 |
| Settlement row 10 | Foundation entries row 10 · Slices 4, 6, 7 |
| Settlement row 11 | Foundation entries row 11 · Slice 7 (nothing to build; the skill says it) |
| Settlement row 12 | Foundation entries row 12 · Slices 3, 7 |
| Human actions: schedule the counting; add the weekly backlog task — both in the cycle | no slice performs them (WAY-140); Slice 7's skill names them; the request lists them for the human |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The directory `process-audit/`, the part `process-audit`, the skill `audit-process`, the command `process-audit/audit_count.py`, the template `process-audit/problem_register.md`, the price list `process-audit/price_list.md` | `audit/` and `audit` — too wide beside the review of a foundation, which audits too | a rename across the slices before the merge; after it, a withdrawn part identifier (WAY-41) |
| The part-map entry is written by Slice 1 with the directory's first file, after the *Foundation entries*, so the foundation check reports the references to `process-audit` between the two | the part-map entry among the *Foundation entries* — its *Files* pattern would match no tracked file, another error of the same check, and `task-cycle/plan/SKILL.md` puts the entry with the file | none beyond one commit whose foundation check is known to report those references |
| Slice 3, not Slice 1, names the command in the part's *Trust boundary* | Slice 1 naming it ahead — a pattern that matches no tracked file is an error of the foundation check (WAY-44) | none |
| `stages.md` gains each stage's start time and tokens by model and kind (Slice 2), so that a fix round is priced at its own models and tied to the record's events | the fix rounds' share taken from their share of tokens, priced at the cycle's average — wrong exactly where the cycle runs stages on cheaper and dearer classes (WAY-229) | a wider `stages.md` than needed; or, if the start time cannot tie stages to events, Slice 4 falls back to names and says so |
| The agents' working time excludes the wait for tools, given apart, the two adding up to today's working time | the wait for tools given inside the working time — the task's *Context* names that joining as what item 7 removes | one subtraction in Slice 3 to change |
| A fix round is the fix of a review's blocking findings together with the review of that fix | the fix alone — the review of the fix is cost the fix round causes | the share reads higher or lower by the reviews of fixes; one rule in Slice 4 to change |
| The counting command is one file, made in four slices, each of which gets a review of its own as a trust boundary | one slice — more than one agent and one review of crafted input hold; reading and computing in two files with only the reading as the boundary — the computing still takes untrusted text from records, and the start's answer names the command as the boundary | four reviews of slices on top of the whole-change review |
| The price list is a dated Markdown table in the part | a JSON file — no harder to parse, but the register, the records and every other file of the-way a person reads are Markdown | one parser in Slice 4 to change |
| The audit skill is not added to the skills the installer gives a product (`installation/install.py`) | adding it — the audit reads the cycles of several repositories and the history of the-way, not one product; and `installation/install.py` is a trust boundary of another part | a user who works only in a product finds no audit skill until one line of the installer adds it |
| Slice 2 does not reword step 12 of `task-cycle/skill/SKILL.md` or the README's line on the stages | rewording them — step 12 still says truly what the report records, and `stages.md` itself says what it holds | the whole-change review may ask for one sentence |
| The *Scope* of WAY-38, WAY-89 and WAY-320 gains `process-audit` among the *Foundation entries* | leaving them to the return step — WAY-21 finds a decision only from the parts its *Scope* names, so the slices' own reading of the script rules would rest on a reach | three one-word changes, written once |
