# Code contracts for a guidelines form script and skill (read-only research)

Repository: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide` (HEAD `96623ed`, branch
`task/product-guidelines-styleguide`). All paths below are relative to that root. "Fact" = read in
the file at the cited line; "Interpretation" is marked as such.

---

## 1. relation-model

### `relation-model/fingerprint.py` (whole file, 21 lines)

- Public: `LENGTH = 8` (`:11`) and
  `def fingerprint(binding_part: str) -> str:` (`:14`):
  ```python
  normalized = re.sub(r"[ \r\n]+", " ", binding_part).strip(" ")
  return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:LENGTH]
  ```
  (`:16-17`). Only spaces, CR and LF are collapsed; tabs are not (fact; matches WAY-02's "every run
  of spaces and line breaks").
- CLI: `python fingerprint.py < binding_part.txt` reads stdin bytes as UTF-8 (`:20-21`).
- The file does NOT know what a binding part is. Extraction lives in each element's guard:
  - **Decision**: binding sentences = the first paragraph after the `### PREFIX-NN/V — question`
    heading that does not start with `- **` (`elements/decisions/format_guard.py:262-271`, stored as
    `Entry.binding`). Fingerprint = `fingerprint(entry.binding)` (e.g. `:585`, `:882`, `:939`).
    WAY-02/1 (`foundations/decisions.md:38-47`): "for a decision, its binding sentences".
  - **Invariant**: the sentence = the first paragraph after `## <identifier>/<version>` up to the
    first `- **` line (`elements/invariants/format_guard.py:278-285`, `Entry.sentence`).
    Fingerprint = `fingerprint(entry.sentence)` (`:860`, `:1331`). WAY-56/1
    (`foundations/decisions.md:1579-1584`): "the entry's fingerprint covers that sentence alone".
    Invariant `invariant-fingerprint-input/1` (`foundations/invariants.md:1117-1119`).
  - **Environment fact**: `entry_fingerprint(entry)` =
    `fingerprint(entry.sentence + "\n" + value_of(entry, "Holds for")[0])`
    (`elements/environment-facts/format_guard.py:234-239`; WAY-78, `foundations/decisions.md:2187-2189`).
  - **Glossary**: "The definition is the entry's binding part; *Avoid* and *Not* stay outside it.
    Nothing carries its fingerprint (WAY-94)." (`elements/glossary/template.md:145-146`). No
    fingerprint code in `elements/glossary/format_guard.py` (grep: no hit).
  - **Part map**: "The binding part of an entry is one sentence: a part's responsibility, a flow's
    description, a surface's promise." (`elements/part-map/template.md:176-180`, WAY-42). No
    fingerprint code in `elements/part-map/format_guard.py` (grep: no hit); invariant
    `map-fingerprint-input/1` (`foundations/invariants.md:677-679`) speaks of "a script of the-way".
- Other users of `fingerprint` outside the elements: `project-level/readiness_check.py:46-48`
  (`sys.path.insert(0, os.path.join(HERE, "..", "relation-model"))`, `from fingerprint import
  fingerprint`) — `definition_fingerprint(text)` over the text from `## Goal` (`:277-284`);
  `project-level/plan_check.py:68-69,210-215` (line `Definition: <path> — fingerprint <hex>`).
  These are the only precedents of a non-foundation Markdown document carrying a fingerprint.

### `relation-model/identifier.py` (31 lines)

- `IDENTIFIER = r"[a-z0-9]+(?:-[a-z0-9]+)*"` (`:17`), `VERSION = r"[1-9][0-9]*"` (`:19`),
  `CITED = r"%s/%s" % (IDENTIFIER, VERSION)` (`:21`), `is_identifier(text)` (`:24`),
  `is_cited(text)` (`:29`). Docstring: "Only the form lives here: how a reader finds a citation in a
  file ... stays with that reader (WAY-55)." (`:7-9`). Used by `gate/run_tests.py:105-108` and the
  invariants guard (`:70-71`).

---

## 2. Format guards

### `elements/decisions/format_guard.py` (1242 lines)

**Loading / imports**
- `sys.path.insert(0, os.path.join(HERE, "..", "..", "relation-model"))` then
  `from fingerprint import fingerprint` (`:65-66`).
- Shared code loaded by path: `shared = _load("elements_common_guard_shared",
  os.path.join(HERE, "..", "common", "guard_shared.py"))` (`:77-78`); `_load` =
  `importlib.util.spec_from_file_location` (`:69-73`).
- Rules are read from `template.md` beside it (`read_rules(path=TEMPLATE)`, `:139-210`), incl.
  `relation_types: dict  # type -> carries a fingerprint` (`:102`) parsed from the template's
  `- **Relations:** derives from WAY-x@<fingerprint> · narrows WAY-y@<fingerprint> | none`
  (`:172-178`; `elements/decisions/template.md:34`).

**Parsing**
- `detect_prefix(text)` (`:229-232`): first `### ([A-Z][A-Z0-9]*)-\d` heading.
- `split_entries(text, level="### ")` (`:235-247`), `parse_entry(first_line, lines, prefix)`
  (`:250-289`), `parse_log(text, prefix)` → list of `Entry` (`:292-293`).
- `@dataclass Entry: line, heading, kind ("version"|"review"|"unknown"), number, version, date,
  binding, fields (name -> [value, line]), text` (`:216-226`).
- Version heading regex: `^### PREFIX-(\d{2,})/(\d+) — (\S.*)$` (`:253`); review heading
  `^### PREFIX-(\d{2,}) · review (DATE)$` (`:254`).
- Fields: `- **Name:** value` and prose `*Name:* value` (`:275-288`).
- `label_of(entry, prefix)` → `"%s-%02d/%d"` (`:351-354`); `versions_of(entries)` (`:357-358`).

**Relation fingerprint checks**
- `check_relations` (`:591-621`, invariants `relation-type/1`, `relation-fingerprint-presence/1`):
  splits *Relations* on ` · `, requires `(PREFIX-\d{2,})(?:@(\S*))?` after the type (`:612`); a
  type that carries a fingerprint needs `[0-9a-f]+` (`:616-618`, message
  "`%s: `%s` carries no fingerprint`"); one that does not must have none (`:619-621`). Presence only,
  no value comparison here.
- `merged_log(...)` (`:805-875`) builds `{number: (entry, onto_commit_or_None, setter_version)}` of
  the log after a merge onto `--merge-onto` (merge base via `git merge-base HEAD <onto>`, `:885-899`).
- `check_fingerprints(latest, rules, prefix, report, no_commit=None)` (`:927-963`, invariant
  `relation-fingerprint-value/1`): `current = {number: fingerprint(entry.binding) ...}` (`:939-940`);
  pattern `^(.+?) PREFIX-(\d{2,})@([0-9a-f]+)$` (`:941`); stale → `report.error` with message
  (`:958-963`):
  ```
  "%s%s: `%s` — the current fingerprint of %s-%02d is %s, set by %s, %s"
  ```
  e.g. `ABC-02/1: `derives from ABC-01@798975ff` — the current fingerprint of ABC-01 is 69b731d5, set
  by ABC-01/2, a change of the kind new wording` (`gate/test_wording_reaches_dependants.py:94-95`).
  `raised` = "a change of the kind <kind>" or "whose *Change* names no kind of change" (`:956-957`).
  Line is `None` (printed `0`) when the entry comes from the onto commit, else the *Relations* line.
- Stale fingerprints are compared **only with `--merge-onto`** (`run`, `:1194-1206`); without it a
  `note:` says those checks are not run (`:1202-1206`). `--merge-onto none` → `unchecked`
  (`:1189-1193`, `NO_MERGE_ONTO`).
- Severity: stale reference = **error**. Warnings exist for `TODO` where allowed (`:499`),
  `merge of <request link>` placeholder (`:655`), passed check-by date (`:1002`).
- `check_binding_across_versions` uses `fingerprint(previous.binding) != fingerprint(entry.binding)`
  (`:585`); `same_binding(one, other)` (`:878-882`).

**Base comparison via git**
- `check_against_base(log_path, text, base, prefix, report, top, no_commit=None)` (`:1046-1085`):
  `file_at(base, relative, top)` then requires the log to grow only at the end (`:1068-1074`) and at
  most one version per number added (`:1076-1084`).
- Own git helpers duplicated from shared: `git(arguments, cwd)` (`:1009-1013`), `file_at(commit,
  path, top)` (`:1016-1028`), `find_commit(log_path, option, commit, report)` → repo top or None
  (`:1031-1043`). Note signature differs from `shared.find_commit(top, option, commit, report)`.

**CLI** (`main`, `:1217-1238`; usage in docstring `:13-33`)
```
python <the-way>/elements/decisions/format_guard.py [LOG] [--base REF] [--merge-onto REF]
    [--today YYYY-MM-DD] [--record PATH]
```
- `log` default `foundations/decisions.md` (`:1219`).
- `--base`: "the commit the task branch left the main branch from, to compare the log with; `none`
  where it does not exist, which records those checks as unchecked" (`:1220-1222`).
- `--merge-onto`: "the commit of the main branch a merge is made onto; only with it are the copies of
  a version both logs hold compared, the fingerprints relations carry compared with the current
  binding part, and `TODO` in the log reported as an error; `none` where the main branch does not
  exist, which records those checks as unchecked" (`:1223-1229`).
- `--today` (date for check-by), `--record` JSON Lines (`:1230-1233`).
- stdout reconfigured to UTF-8 (`:1235-1236`).
- **Exit codes**: "0 without errors, 1 with errors, 2 when the log or the template cannot be read or
  the record cannot be written" (`:31-33`; `run` returns `1 if report.errors else 0`, `:1214`).
- `SELECTED_BY` maps each check to the option that selects it for the record (`:60-62`).

### `elements/common/guard_shared.py` (326 lines)

Purpose (`:1-7`): "reading a file and the sections and fields of an entry, reading the rules of form
the elements share from `rules.md` ..., the report of a run and the-way's own record of it (WAY-74),
and the calls to git. A guard loads this module by its path".

- Constants: `NO_COMMIT = "none"` (`:20`), `NO_COMMIT_REASON = "the method takes a commit the gate
  filled in as not existing"` (`:21`), `given_none(option, why)` (`:24-28`), `NO_BASE` /
  `NO_MERGE_ONTO` (`:32-33`), `TODO_WORD` regex (`:38`).
- Files: `read_file(path, report, what)` → text or None after `report.error(None, "cannot read ...")`
  (`:44-52`); `split_sections(text)` over `## ` headings (`:55-61`); `parse_fields(body,
  first_line)` → `{name: [value, line]}` (`:64-78`).
- Template helpers: `TemplateError` (`:84`), `template_section(text, title)` (fence-aware,
  `:88-103`), `markdown_blocks` (`:106-108`), `table_form` (`:111-117`), `read_common(path)`
  (`:125-150`).
- **Report** (`class Report`, `:160-270`): `__init__(path, options=(), program=None,
  selected_by=None)`; `ran(check, *invariants)`, `unchecked(check, reason, description,
  *invariants)`, `fail(...)`, `error(line, message, check=None, invariants=())`, `warning(line,
  message)`, `cannot_check(what, why)`, `notes` list.
  `print(stream)` (`:230-239`) — the output format of every element guard:
  ```
  <path>:<line or 0>: error: <message>
  <path>:<line or 0>: warning: <message>
  unchecked: <what> — <why>
  note: <note>
  <n> error(s), <n> warning(s), <n> unchecked
  ```
  The last line counts `cannot_check` lines, not record verdicts (`:172-177`).
- Record: `start_record(path)` (`:273-276`), `write_record(path, report)` JSON Lines with keys
  `check`, `verdict` (`pass|fail|unchecked`), `invariant`, `description`, `reason` (`:248-282`).
- Git: `git(arguments, cwd, stdin=None)` → (code, out) (`:288-290`); `call_git(...)` → (code, out,
  err), OSError → 127 (`:293-301`); `file_at(commit, path, top)` → `(text, None)` / `(None, None)`
  for absent path / `(None, message)` (`:304-316`); `find_commit(top, option, commit, report)` →
  bool (`:319-326`).

### What a new script can import to get binding parts / fingerprints (interpretation from the code)

- **Decision**: load `elements/decisions/format_guard.py` by path (as the invariants guard does:
  `decision_guard = _load("decision_format_guard", os.path.join(HERE, "..", "decisions",
  "format_guard.py"))`, `elements/invariants/format_guard.py:64`), then
  `prefix = decision_guard.detect_prefix(text)`, `entries = decision_guard.parse_log(text, prefix)`,
  latest per number, `decision_guard.fingerprint(entry.binding)`. The invariants guard already
  exposes the two steps: `latest_versions(log_entries)` (`:444-450`) and
  `in_force(latest)` → `{number: fingerprint(entry.binding)}` for entries with binding
  (`:453-456`). A merge-aware variant: `merged_decisions(path, foundation, merge_onto, top, report)`
  (`:1403-1432`) — reads `decisions.md` **beside the invariants file** (`:1410`), so it assumes the
  foundation directory.
  Caveat (fact): loading the decisions guard runs module-level code (`sys.path` insert, `_load` of
  shared) but no checks.
- **Invariant**: load `elements/invariants/format_guard.py` by path; `rules = read_rules()`
  (`:172`, default template and `elements/common/rules.md`), `items = parse_file(text, rules)`
  (`:267-292`), keep `isinstance(item, Entry)`; `Entry(line, identifier, version, sentence, fields,
  strays, text)` (`:213-221`); fingerprint = `fingerprint(entry.sentence)` (invariants guard sets
  `fingerprint = decision_guard.fingerprint`, `:74`). Loading it also loads the decisions and
  part-map guards (`:64-65`); the facts guard is lazy (`:79-83`).
- `FINGERPRINT = r"[0-9a-f]{%d}" % fingerprint_module.LENGTH` (`:88`) is the strict 8-hex form; the
  decisions guard accepts any `[0-9a-f]+` (`:616`, `:941`).

### `elements/invariants/format_guard.py` — links with fingerprints

- CLI: `[FILE] [--base REF] [--merge-onto REF] [--record PATH]` (`:19-20`, `main` `:1661-1680`),
  same exit codes 0/1/2 (`:36-37`).
- `check_links` (`:753-816`, `link-fingerprint-presence/1`): every item of *Rests on* is
  `<fact>@<8 hex>` and of *Derives from* `PREFIX-NN@<8 hex>`; decision must be in force.
- `check_fingerprints(entries, merged, report, no_commit=None, facts=None)` (`:1473-1523`,
  `link-fingerprint-value/1`), message e.g. "`%s: `%s` — the current fingerprint of %s-%s after the
  merge is %s`" (`:1517-1520`). Merge-only, like the decisions guard.
- Version vs fingerprint: `check_against_base` (`:1320-1360`) compares `fingerprint(entry.sentence)`
  with the base copy; a changed sentence needs version +1 or a *Correction* `<old> → <new>`
  (`check_corrections`, `:850-862`).

### Are invariants referenced elsewhere with `id@fp`? (fact)

- No. A repository-wide grep for `<identifier>@<8 hex>` (all `.md`/`.py`, excluding `.runs`) finds
  only decision numbers (`WAY-NN@…`), environment-fact identifiers and test-fixture names
  (`storage-cap`, `storage-events`, …); none of the 210 invariant identifiers.
- Invariants are cited by **identifier and version**: tests by `# invariant: <id>/<version>`
  (`gate/run_tests.py:13-20`); WAY-57/1 (`foundations/decisions.md:1607-1620`): "A check cites its
  invariant by identifier and version ... and fails the gate when that version is not the current
  one, while elsewhere a reference to an invariant's version is historical and never flagged, as
  WAY-02 has it."
- WAY-02/1 (`foundations/decisions.md:38-47`) permits it in general: "everything that depends on it —
  other entries, tests, documents and code comments — refers to that identifier. A reference that
  relies on the entry's current binding part carries its fingerprint (`WAY-17@<fingerprint>`), and
  when the fingerprint changes, a script working on plain text files flags that reference for
  review; a bare identifier and a reference to a version (`WAY-17/2`) are never flagged."
- WAY-31/1 (`foundations/decisions.md:893-898`) names exactly which links are flagged: relations
  `derives from`/`narrows`, an invariant's *Derives from* and *Rests on*; "its *Part* carries none".
  Interpretation: a guideline's `invariant-id@fp` reference would be the first of its kind; WAY-31
  does not list it, so the list of flagged links would need a new decision version or a separate
  decision.

---

## 3. Gate

### `gate/run_tests.py` (838 lines)

- Usage: `python -B gate/run_tests.py DIRECTORY [--record PATH]` (`:4-6`); `--record` must end in
  `.jsonl` (`:9-11`).
- Discovery: "the ones `python -m unittest discover -s DIRECTORY -p "test_*.py"` finds" (`:8`);
  `PATTERN = "test_*.py"` (`:93`); `run()` calls `unittest.TestLoader().discover(start,
  pattern=PATTERN)` (`:777`). Sub-folders without `__init__.py` are not entered, and a citing test
  there gives `fail` (`:50-54`). Hence each directory runs separately: invariants' *Method* lines use
  `gate/run_tests.py agent-instructions | elements/decisions | elements/environment-facts |
  elements/glossary | elements/invariants | elements/part-map | gate | installation | project-level
  | relation-model` (grep of `foundations/invariants.md`).
- Citation: comment line `invariant: <identifier>/<version>` alone on its line **inside the body of
  the test method** (`:13-16`); `fact: <id>/<version>` for facts; a citation at file/class level
  cites nothing and gives a null line (`:55-60`). Regex `CITATION = re.compile(r"#\s*(invariant|fact):\s*(.*?)\s*")`
  (`:113`), value checked against `identifier.CITED` (`:105-108`).
- Exit codes: 0 no failure, 1 a `fail` line or unittest failure, 2 bad directory/record/monitoring/
  interrupt (`:75-80`). "no test found in DIRECTORY" → 1 (`:801-803`).
- `flow:` lines are **not** read by run_tests; they are read by the part-map guard:
  `FLOW_LINE = re.compile(r"^[ \t]*#[ \t]*flow:[ \t]*(.*?)[ \t\r]*$", re.M)`
  (`elements/part-map/format_guard.py:112`), "`# flow: <identifier>` in a file git tracks, never by
  a path in the map" (`:9`), `check_flows` (`:840-866`) reports "no test names the flow in a line
  `# flow: %s`". The-way's own flow tests carry `# flow: wording-reaches-dependants`
  (`gate/test_wording_reaches_dependants.py:15`) and `# flow: skills-reach-the-way-sessions`
  (`gate/test_skills_reach_the_way_sessions.py:17`).

### `gate/test_wording_reaches_dependants.py` (163 lines)

- End-to-end test of flow `wording-reaches-dependants` (`:1-13`): "The expected fingerprints are
  written out below on purpose. A test does not compute its expected value with the code it checks"
  (`:8-10`). `WORDING`, `CURRENT = "798975ff"`, `SUPERSEDED = "69b731d5"` (`:30-35`).
- Imports: `sys.path.insert(0, os.path.join(ROOT, "elements", "decisions"))`, `import
  format_guard`, `from test_format_guard import BINDING, TODAY, log, version` (`:26-28`) — reuses the
  decisions guard's fixtures (`elements/decisions/test_format_guard.py:24-25,33,71`).
- `guard()` builds a temp git repo, commits the onto log on a branch, runs
  `format_guard.run(path, today=TODAY, stream=output, merge_onto="main"|"onto")` (`:39-66`).
- Each test cites `# invariant: decision-guard-stale-reference/1` in its body (`:79`, `:88`, ...).
- Positive guard of the fixture: `test_the_wording_this_test_stands_on_has_not_changed` (`:68-71`).

### `gate/test_skills_reach_the_way_sessions.py` (279 lines)

- Flow `skills-reach-the-way-sessions` (`:1-17`); finds skills with its own git call
  `git ls-files -z --cached --others --exclude-standard -- ":(glob)**/SKILL.md"`, excluding
  `.claude/` and `.agents/` (`discover`, `:56-67`); imports nothing from the generator (`:9-13`).
  Positive control `CONTROL = ("elements/decisions/skill/SKILL.md", "task-cycle/skill/SKILL.md")`
  (`:47`). Cites `skill-entry-points/1` (`:211-212`). Expected words from the invariant (`:31-41`).

### `gate/method_script.py` (184 lines, briefly)

- Reads which script a method's command runs when its program is a Python interpreter (WAY-105)
  (`:1-22`); `script_of(command)` (`:154`), `tokens_of`, `words_of`. "running the method, looking for
  the script and reporting the result are the gate's, which does not exist yet" (`:7-8`).

---

## 4. Installation

### `installation/install.py` (500 lines)

- SKILLS (`:18-39`), quoted:
  ```python
  ELEMENTS = {
      "decisions": ("record-decision", "decisions.md"),
      "invariants": ("record-invariant", "invariants.md"),
      "glossary": ("record-glossary-term", "glossary.md"),
      "part-map": ("update-part-map", "part_map.md"),
      "environment-facts": ("record-environment-fact", "environment_facts.md"),
  }
  SKILLS = {
      name: f"elements/{element}/skill/SKILL.md"
      for element, (name, _) in ELEMENTS.items()
  }
  SKILLS.update({
      "find-foundation-entries": "elements/common/skill/SKILL.md",
      "define-project": "project-level/skill/SKILL.md",
      "plan-project": "project-level/plan/skill/SKILL.md",
      "lead-project": "project-level/lead/skill/SKILL.md",
      "settle-technology": "project-level/technology/SKILL.md",
      "refine-task": "project-level/task/skill/SKILL.md",
      "implement-task": "task-cycle/skill/SKILL.md",
      "plan-task": "task-cycle/plan/SKILL.md",
      "critique": "elements/common/critique/SKILL.md",
  })
  ```
  Fact: `maintain-instruction-files` (`instruction-files/SKILL.md`) is **not** installed in products,
  though the-way's own entry points include it.
- Entry points: `SKILL_DIRECTORIES = (".claude", ".agents")` (`:41`); `plan()` writes
  `target / directory / "skills" / f"the-way-{name}" / "SKILL.md"` for each (`:304-307`).
  `skill_wrapper(path, name, commit)` (`:110-136`) reads the source from the pinned commit
  (`committed(path, commit)` = `git show commit:path`, `:72-73`), requires the source's `name:` to
  equal the SKILLS key (`:112-114`), writes frontmatter `name: the-way-<name>` and `description:
  <source description> Use this product's pinned the-way commit.` (`:118-121`), the commit hash, the
  submodule checks, "Read `.the-way/<path>` in full and follow it ... here the process root is
  `.the-way`. Do not substitute a global skill." and the sibling sentence naming every SKILLS key
  (`:122-136`, `sibling_names()` `:105-107`).
- AGENTS.md marked block: `BEGIN = "<!-- the-way:begin -->"`, `END = "<!-- the-way:end -->"`
  (`:45-46`); `agents_block()` = `BEGIN\n + product_guidance() + END\n` (`:178-179`).
  `product_guidance()` (`:139-175`) content, in order: "# Pinned the-way process"; submodule init and
  commit check; "Write foundation entries only through the project skills <the five element
  skills>. Use the project skills <all other SKILLS> for their named work." (`:142-155`; the list is
  derived from SKILLS, so adding a skill changes the block); how to run scripts as `.the-way/<path>`
  with examples `python -B .the-way/gate/run_tests.py <directory>` and `python -B
  .the-way/elements/<element>/format_guard.py foundations/<file>`; records under `.runs/`
  (`:156-162`); main branch, `--base`/`--merge-onto`, `none` (`:163-170`); empty part map report
  (`:171-172`); "Nothing runs these checks automatically. Before a merge, run the format guard of
  every changed foundation file and the tests of every changed part ..." (`:173-175`). It names no
  commit (`:140-141`).
- Empty foundation files (`empty_foundations()`, `:76-102`): `decisions.md` ("# Decision log"),
  `invariants.md` (three tables: Withdrawn identifiers, Quarantined invariants, Recovered
  invariants), `glossary.md`, `part_map.md` (Criticality scale, External context, Change paths,
  Files left out on purpose, Withdrawn identifiers), `environment_facts.md` (Withdrawn identifiers).
  Also `CLAUDE.md` = `@AGENTS.md\n` when absent (`:42-43,212-216`), `.gitignore` line `.runs/`
  (`:47-48,251-258`). Nothing else (no guidelines file).
- **Already-installed product / new skills** (fact):
  - Same pin, wrapper file missing → it is created (files that do not exist are written,
    `:476-481`); existing wrapper with different content → `RuntimeError("Existing integration file
    differs: ...")` (`:358-359`).
  - Different pin → refuses: `"Existing .the-way pins {pin}, requested {commit}; moving a pin is a
    separate product task"` (`:316-318`).
  - AGENTS block different from this commit's guidance → refuses: "remove the block from BEGIN to END
    and run again" (`:242-246`).
  - Re-run with nothing to do prints "Already installed; no changes." (`:457-461`).
  - Interpretation: there is no update command; a new skill reaches an installed product only via the
    pin-move task described in `installation/README.md:66-81`, and because SKILLS feeds the AGENTS
    block, that task also has to remove and re-create the block.
- CLI: `repo`, `--url`, `--apply` with `y` confirmation (`:405-465`). Errors → `Error: ...`, exit 1
  (`:493-500`).

### `installation/README.md` (136 lines)

- Purpose (`:3-8`); file table (`:46-60`) — line `:56` lists the installed skills by name (manual
  list: "the five foundation entry skills, `find-foundation-entries`, `define-project`,
  `plan-project`, `lead-project`, `settle-technology`, `refine-task`, `implement-task`, `plan-task`,
  and `critique`").
- Pin move path (`:66-81`): "A later process version enters the product through a separate product
  task that moves the gitlink and updates its project skill entry points (WAY-34). In that task, move
  the gitlink and the `.the-way` checkout to the new commit, delete the installed wrappers ..., then
  run the installer from a the-way checkout at the new commit with `--apply`. ... The block in
  `AGENTS.md` stays as it is unless the guidance text changed between the two commits; then the
  installer stops on the block, and the task removes it, markers included, before running the
  installer again."
- Tests: `python -B gate/run_tests.py installation` (`:121-123`); "They install this checkout's
  committed `HEAD`, so uncommitted changes to skills, templates or guards are not exercised until they
  are committed." (`:135-136`).

### Tests in `installation/` about SKILLS (fact)

- `installation/test_install.py:17-29`: hand-written `NAMES` of 13 (path, name) pairs — the five
  element skills, find-foundation-entries, define-project, plan-project, settle-technology,
  refine-task, implement-task, plan-task, critique (no lead-project).
  `test_preview_apply_rerun_and_preserve_foundation` (`:57-109`) asserts for each: both wrappers
  exist and are byte-identical, `name: the-way-<name>`, the commit, `.the-way/<path>`, the submodule
  check, the prefix sentence, and every sibling name in backticks (`:80-93`).
  `test_guidance_names_no_commit_and_covers_the_product_rules` (`:125-142`) asserts every
  `the-way-<name>` of NAMES appears in the guidance and fixed fragments.
  `test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies` (`:116-123`).
- `installation/test_lead_installation.py` (`LEAD_SOURCE = "project-level/lead/skill/SKILL.md"`,
  `:12-14`) covers lead-project separately, incl. `test_different_product_pin_is_not_moved`
  (`:140`).
- No test compares `install.SKILLS` with the set of skills in the repository (grep for
  `install.SKILLS` finds nothing). Interpretation: a new skill added to SKILLS but not to NAMES
  passes all installation tests; the NAMES list and README line 56 must be updated by hand.
- Imports: `sys.path.insert(0, str(SOURCE / "installation"))`, `import install`
  (`test_install.py:14-17`). Tests cite `installation-claude-guidance/1` only.

---

## 5. `agent-instructions/skill_entry_points.py` (246 lines)

- Usage `python -B agent-instructions/skill_entry_points.py [--write]` (`:4-6`); without `--write`
  prints `would create|change <path>`; with it writes UTF-8 LF (`:16-17`, `:227-233`); lists orphans
  `orphan <dir>: ... remove it with git rm -r -- <dir>` (`:234-236`); "entry points are current"
  (`:237-238`). Exit 0, or 1 with `Error: <message>` (`:22`, `:240-242`).
- Discovery: `skill_paths(root)` = `git ls-files -z --cached --others --exclude-standard --
  ":(glob)**/SKILL.md"`, skipping paths under `.claude/` and `.agents/`, kept only if on disk
  (`:69-86`). So any `SKILL.md` anywhere (any directory name, `skill/` subdir or not) is a skill.
- **Name comes from the frontmatter `name:`, not from the directory** (`read_skill`, `:105-126`):
  first `name:`/`description:` between the first two `---` lines (`:89-102`, `FIELD =
  re.compile(r"(name|description):(.*)")` `:43`); name must match `[a-z0-9]+(?:-[a-z0-9]+)*`
  (`:40`, `:122-123`) and must not start with `the-way-` (`:124-125`); description must be one line
  and a safe plain YAML scalar — not starting with any of `-?:,[]{}#&*!|>'"%@\``, no `": "`, no
  `" #"`, not ending with `:` (`:42`, `:115-120`). Duplicate names stop the run (`:135-137`).
- Output: `.claude/skills/the-way-<name>/SKILL.md` and byte-identical `.agents/skills/...`
  (`ENTRY_DIRECTORIES`, `PREFIX = "the-way-"`, `SUFFIX = " Use this checkout's own the-way."`,
  `:37-39`; `produce`, `:186-193`). Text (`entry_point_text`, `:151-183`) names the source path, the
  two product checks, the process-root rule, and all sibling names.
- Tests (`agent-instructions/test_skill_entry_points.py`, imports `sys.path.insert(0, str(HERE))`,
  `import skill_entry_points as generator`, `:20-23`): written-out text (`:90`), ordering of siblings
  (`:102`), excluded paths (`:115`), deleted-on-disk (`:125`), non-ASCII/CRLF (`:133`), error cases
  (`:175`), duplicate names (`:191`), write/rerun (`:202`), dry run (`:226`), orphans (`:236`), and
  `test_the_tracked_entry_points_are_what_the_generator_produces` (`:250-261`) which fails with "run
  python -B agent-instructions/skill_entry_points.py --write and commit what it writes".
- Invariant `skill-entry-points/1` (`foundations/invariants.md:2065-2073`), method `gate/run_tests.py
  gate`, `Derives from: WAY-127@69651fc7`.

---

## 6. `instruction-files/`

### `principles.md` (316 lines) — headings
`# Principles of instruction files for agents` (`:1`); `## 1. Ways in and routes` (`:12`);
`## 2. What the main file holds` (`:54`); `## 3. Where a rule lives` (`:98`); `## 4. One layout for
three tools` (`:126`); `## 5. How to write a single rule` (`:157`); `## 6. Judging a file and a
rule` (`:181`) with `### Statically — ...` (`:183`) and `### In operation — ...` (`:212`);
`## 7. Maintenance` (`:231`) with `### When to add a rule` (`:233`), `### When to remove a rule`
(`:251`), `### Mechanisms that clean up` (`:265`); `## Sources` (`:285`).
Relevant content: a main-file line stays only when (1) needed in every session or points to a way in,
(2) the agent cannot read it, (3) without it the agent errs (WAY-128, `:58-65`); "Pointers to ways in.
'Before X, read `path`' ... the target is given as a path in backticks (WAY-129). `@path` in Claude
Code is not a pointer" (`:73-76`); rules for one part of the code go in a path-pinned rule or
subdirectory file (`:84`); "every time, without exception" → CI check / linter / check of a step's
output (WAY-133) (`:110`, `:40-45`); "knowledge needed sometimes (documentation, patterns, data)" →
"a file pointed to from a step of a route or from the main file", one level deep (`:111`).

### `SKILL.md` (165 lines)
- Frontmatter (`:1-4`): `name: maintain-instruction-files`, `description: Use when an instruction
  file for coding agents — AGENTS.md, CLAUDE.md, .claude/rules, .cursor/rules/*.mdc, a user's global
  instruction file — has to be written, judged, split or cleaned up, or when a rule has to be placed
  in one, such as a rule settled in a review of agent sessions.`
- Structure: `# Maintain instruction files` (`:6`), copy-resolution checks (`:13-40`), `## 1. Read`
  (`:41`), `## 2. Choose the mode` (`:70`), `## Judge` (`:79`), `## Change` (`:115`), `## Place`
  (`:121`), `## Write` (`:136`), `## Mistakes this skill prevents` (`:152`). Lives at the directory
  root, not in a `skill/` subdir.

### `check_instructions.py` (729 lines)
- CLI: `python -B <the-way>/instruction-files/check_instructions.py [ROOT] [--file PATH ...]`
  (`:12-14`, `main` `:696-724`). ROOT defaults to cwd; `--file` adds files outside the repo.
- Output: each finding `LEVEL check file:line message` (printed
  `f"{f.level.upper():5} {f.check} {shown(f.file)}:{f.line} {f.message}"`, sorted error/warn/info,
  `:716-719`), last line `"<n> error, <n> warn, <n> info"` (`:721-722`). Levels: `error`, `warn`,
  `info` (`Finding`, `:92-97`).
- Exit: 1 with an error; 2 when ROOT is not a directory, a `--file` is unreadable/not regular, or
  either is a network path; else 0 (`:18-19`, `:691-724`).
- What files: `instruction_files(root, findings)` (`:214-263`) walks ROOT (skipping
  `SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".runs"}`,
  `:50`, and nested repos) and keeps names for which `is_instruction_name` holds (`:130-137`):
  `MAIN_NAMES = {"AGENTS.md", "CLAUDE.md", "CLAUDE.local.md", "AGENTS.override.md"}` (`:51`),
  `.claude/CLAUDE.md`, `.claude/rules/*.md`, `.cursor/rules/*`, `SKILL.md` under `SKILL_DIRS`
  (`:52`).
- **Following paths named in root AGENTS.md**: yes, but only in backticks. `pointed_files(root,
  texts, files)` (`:568-605`): "The Markdown files the root AGENTS.md or CLAUDE.md names in
  backticks ... each a regular file that leads to a path inside ROOT, outside the skipped directories
  and nested repositories, that is not already an instruction file; each once, one level deep."
  Suffixes `POINTED_SUFFIXES = (".md", ".mdc")` (`:53`); a `:line` suffix is stripped (`:61`,
  `:582`). Docstring: "a file named by its path elsewhere in the text is not followed, though the
  glossary term and the invariant count it" (`:7-10`).
- Checks applied to such a pointed file: the same per-file `check_file(...)` (`:684-686` →
  `:471-541`): `dead-path` (backticked path that does not resolve → `warn`, or `info` in a "does not
  load/exist" sentence), `at-import` (`@path` with `.` or `/`: `error` when punctuation follows,
  else `warn`), `emphasis` (>1 line with IMPORTANT/YOU MUST/... → `warn`), `size` (`info`, not for
  `SKILL.md`). Layout checks (`check_layout`, `:608-656`) apply only to the walked instruction files.
- The glossary term (`foundations/glossary.md:175-177`): "A repository instruction file is an
  instruction file for coding agents that a repository's git tracks under the name `AGENTS.md`,
  `CLAUDE.md` or `CLAUDE.local.md` in any of its directories, `.claude/` among them, or as a Markdown
  file its root `AGENTS.md` or `CLAUDE.md` names by its path." Invariant
  `instruction-file-imports/1` (`foundations/invariants.md:2075-2081`) applies to the-way's own
  repository instruction files and counts a path anywhere in the text (with a precise boundary rule).
  Interpretation: a product's styleguide named from root `AGENTS.md` in backticks becomes a pointed
  file the script checks for dead paths, `@` imports and emphasis.

### `tool_loading.md` (225 lines) — headings
`# How each tool loads instruction files` (`:1`); `## Claude Code` (`:10`) / `### Settings that
change loading` (`:69`); `## Codex` (`:80`) / `### Settings ...` (`:121`); `## Cursor` (`:135`) /
`### Settings ...` (`:177`); `## Method of checking` (`:182`); `## Measurements` (`:194`).

---

## 7. Element skills and hand-offs

Frontmatter (`name` / start of `description`), each at line 2-3 of its file:

| File | name | description (start) |
|---|---|---|
| `elements/decisions/skill/SKILL.md` | record-decision | "Use when a decision has to be written into a product's decision log, foundations/decisions.md — ..." |
| `elements/invariants/skill/SKILL.md` | record-invariant | "Use when a product's invariants file, foundations/invariants.md, has to gain or change an entry — ..." |
| `elements/glossary/skill/SKILL.md` | record-glossary-term | "Use when a product's glossary, foundations/glossary.md, has to gain or change an entry — ..." |
| `elements/part-map/skill/SKILL.md` | update-part-map | "Use when a product's part map, foundations/part_map.md, has to gain or change an entry — ..." |
| `elements/environment-facts/skill/SKILL.md` | record-environment-fact | "Use when a product's environment facts file, foundations/environment_facts.md, has to gain or change an entry — ..." |
| `elements/common/skill/SKILL.md` | find-foundation-entries | "Use when a source has to be searched for what should become entries of a product's foundation — ..." |
| `elements/common/critique/SKILL.md` | critique | "Use when an agent's proposal needs an independent critical reading, ..." |

- Common preamble pattern (fact, e.g. `elements/decisions/skill/SKILL.md:13-18`,
  `project-level/technology/SKILL.md:18-22`, `elements/common/skill/SKILL.md:15-19`): "This skill
  lives in `<dir>` of the-way. In the-way itself, the-way is the checkout or worktree the session
  works in, the directory `git rev-parse --show-toplevel` prints in the session's working directory;
  in a product, it is the product's pinned `.the-way`. ... each skill named below is the project
  skill of that name with the `the-way-` prefix."
- Element skills hold only what is particular to the element; rules live in `template.md` +
  `elements/common/rules.md`, the shared steps in `elements/common/way_of_working.md`
  (`elements/decisions/skill/SKILL.md:8-11`). Decisions skill structure: `## 1. Read` (`:20`),
  `## 2. Decide what the entry is` (`:28`), `## 3. Draft` (`:42`), `## 4. Ask, show, write` (`:56`),
  `## Projected mode` (`:66`), `## Review record` (`:89`). *Verification* level 1 invariants are
  "written through `record-invariant` in step 4.4" (`:47-49`, `:60-64`).
- Hand-off by naming the skill in backticks with what it receives:
  - `project-level/technology/SKILL.md:150-155`: "**Write.** Hand each choice to `record-decision`
    in projected mode, naming the definition, with the consequences that decided it, the other options
    with theirs, the source of each claimed difference for its *Based on*, the lacks ... for its
    *Rationale* ...".
  - `project-level/technology/SKILL.md:112-117`: "Give one fresh agent, following `critique`, the
    whole comparison of a choice ...".
  - `elements/common/skill/SKILL.md:110-111`: each accepted row is handed to "`record-decision`,
    `record-invariant`, `record-glossary-term`, `record-environment-fact` or `update-part-map`".
  - `project-level/technology/SKILL.md:31-32`: "return to `define-project` step 5".
- `elements/common/skill/SKILL.md` purpose (`:6-13`): "Finds in a source what should become entries
  of a product's foundation, puts it before the human as a table of candidates, and hands every
  accepted one to the skill of its element, or, for a task, keeps it as a row of the task document. It
  writes no entry itself." Caller gives source, next reader and mode (projected / task rows)
  (`:22-37`). Headings: `## 1. Read` (`:39`), `## 2. Build the table` (`:57`), `## 3. The human cuts`
  (`:82`), `## 4. Row by row` (`:87`), `## 5. Close` (`:119`).

---

## 8. `project-level/technology/SKILL.md` (settle-technology)

- Frontmatter (`:1-4`): `name: settle-technology`; description "Use when a project definition of a
  product that uses the-way has to settle the technology and architecture choices its project needs
  before the readiness gate — a language, a framework, a library, a store of data, a way of logging
  in, a place to run — or to resume that step from the definition's Technology section."
- Writes only into the definition, never the foundation (WAY-106) (`:24-25`). "The human weighs
  consequences for the product, not technologies (WAY-123)" (`:11-13`).
- Research discipline:
  - Waves: every open choice depending on no open choice researched at once; dependents later
    (WAY-122) (`:83-87`).
  - **Research** (`:89-96`): one fresh agent per choice; "Each finds the options in their
    documentation, starting from what the definition needs of the choice, never from a fixed list of
    stacks, not even as a hint, and gives each option its source: a page of its documentation with its
    version (WAY-122)."
  - **Weigh** (`:97-103`): properties from the template, "citing for each the page it was read from";
    lacks said as what they mean for the product; unmaintained/undocumented options left out with a
    line.
  - **Consequences** (`:104-111`): cost, where it runs, keeping it running, changing it later; "every
    difference claimed between the options cites its source (WAY-123)"; report written to
    `.runs/technology/<choice>.md`.
  - **Critique** (`:112-117`): "Give one fresh agent, following `critique`, the whole comparison ...
    and ask it to refute every claimed difference no source supports. Verify each observation and give
    your verdict; correct the comparison by the verdicts, then end the report with the line `critique:
    passed`. Where no fresh agent can run, neither the research nor the comparison goes on: stop and
    say so (WAY-122, WAY-120)."
  - **Show** (`:118-139`): only after every comparison reads `critique: passed`; recommendation +
    weak point; "A difference with no consequence for the product decides nothing; where none
    remains, recommend the simplest and cheapest option (WAY-123)"; devil's advocate / pre-mortem /
    unknown-unknowns agent on the recommended options (WAY-138); a second critique for contradictions
    across choices; one table per wave: options by consequences, left-out lines, recommendation, weak
    point, risks marked as hypotheses.
  - **Choose** (`:140-149`): "The human chooses each; never choose alone (WAY-123)." "you choose" /
    "I do not know" takes the recommendation; any other answer gets one question against it (WAY-113).
  - **Write** (`:150-158`): hand to `record-decision` in projected mode (see §7).
  - **Close** (`:160-166`): `python -B <the-way>/project-level/readiness_check.py <definition>
    --before-approval`.
- WAY-122/1 binding (`foundations/decisions.md:3505-3520`): options "come from research of that choice
  against the project definition, rather than from a fixed list of bundled stacks ... and every
  option is offered only after a critique that refutes every claimed difference between the options
  which no source supports."

---

## 9. `task-cycle/skill/SKILL.md` (implement-task)

- Frontmatter (`:1-4`): `name: implement-task`; description "Use to take one ready the-way task to a
  reviewable pull or merge request — through a spec where the task leaves an open design choice, one
  author without a plan ... Requires subagents and the Superpowers skills named by this process. The
  human reviews the request, not intermediate steps."
- Headings: `## Inputs and authority` (`:24`), `## Start and record` (`:70`), `## Design and
  execution choice` (`:175`), `## Execute, verify and review` (`:248`), `## The end of a code review`
  (`:394`), `## Request and handoff` (`:445`), `## Correction after review` (`:511`).
- **No mention** of view, UI, interface, screen, style, styleguide or guidelines (grep `-i`); the only
  related line: "For visible behavior, verify it in the running product as well." (`:339-340`).
  Grep for "guideline"/"styleguide" over the whole repo (excl. `.runs`) finds only URLs in
  `probes/sha-256/test_sha_256.py:24-27`.
- Where skills are used: step 2 "Read the product's `AGENTS.md`, process pin and relevant code. Select
  and read the current foundation by 'Reading the foundation' in `elements/common/way_of_working.md`
  (WAY-150)" (`:46-49`); step 3 requires Superpowers 6.4.1 skills and the-way's `plan-task`; "The stage
  agent reads its own method and linked files whole: `brainstorming`, `test-driven-development`,
  `plan-task` or the element skills for foundation work" (`:50-60`). Step 4 determines the foundation
  route (WAY-13) (`:72-`).
- Step 6 (`:186-202`): only an open design choice calls for a spec (WAY-135); a fresh design agent
  uses Superpowers `brainstorming`, follows its architectural path, writes `spec.md` in the working
  cycle record, returns questions to the orchestrator, stops at the reviewed spec before planning;
  questions answered from approved sources, otherwise "the smallest reversible interpretation ... and
  record it as an autonomous choice. Do not silently expand task scope." Provisional go-ahead in place
  of human approval. Step 7 (`:203-209`): another agent reviews the spec; "A spec may name the
  foundation entries the task will write; the foundation step or the return step writes them."
- Related elsewhere: `project-level/definition_template.md:168-177` — the Technology section's three
  matters of an agent's way to the running product: logs, interface, development data ("the interface
  asks how an agent operates the product as its user does — through a screen in a ...").

---

## 10. Directory conventions

| Top-level dir | Holds | Skill location | Tests |
|---|---|---|---|
| `agent-instructions/` | `README.md`, `skill_entry_points.py` | none | `test_instruction_files.py`, `test_skill_entry_points.py` |
| `elements/<element>/` (decisions, invariants, glossary, part-map, environment-facts) | `template.md`, `examples.md` (not environment-facts), `format_guard.py` | `skill/SKILL.md` | `test_format_guard.py` |
| `elements/common/` | `guard_shared.py`, `rules.md`, `way_of_working.md` | `skill/SKILL.md` (find-foundation-entries), `critique/SKILL.md` | none (guard_shared tested through the guards) |
| `foundations/` | the-way's own entries + `violated_invariants.md` | — | — |
| `gate/` | `run_tests.py`, `method_script.py` | none | `test_run_tests.py`, `test_method_script.py`, flow tests `test_wording_reaches_dependants.py`, `test_skills_reach_the_way_sessions.py` |
| `installation/` | `install.py`, `README.md` | none | `test_install.py`, `test_installed_guidance.py`, `test_lead_installation.py` |
| `instruction-files/` | `principles.md`, `tool_loading.md`, `check_instructions.py` | `SKILL.md` at directory root | `test_check_instructions.py` |
| `probes/<fact-id>/` | `test_<fact_id>.py` each; `probes/fact_probes.py` | none | the probe files |
| `project-level/` | `definition_template.md`, `readiness_check.py`, `plan_check.py`, `plan_state.py`; `plan/template.md`, `task/template.md`, `lead/answering.md`, `lead/conversation_template.md` | `skill/SKILL.md` (define-project), `plan/skill/SKILL.md`, `task/skill/SKILL.md`, `lead/skill/SKILL.md`, `technology/SKILL.md` (no `skill/` subdir) | `test_plan_check.py`, `test_plan_state.py`, `test_plan_state_invariant.py`, `test_plan_state_subprocesses_invariant.py`, `test_readiness_check.py` (all at `project-level/` root) |
| `relation-model/` | `fingerprint.py`, `identifier.py` | none | `test_fingerprint.py`, `test_identifier.py` |
| `task-cycle/` | `cycle_stages.py`, `slice_size.py`, `record_template.md` | `skill/SKILL.md` (implement-task), `plan/SKILL.md` (plan-task, no `skill/` subdir) | `test_cycle_stages.py`, `test_slice_size.py` |
| root | `AGENTS.md`, `CLAUDE.md` (`@AGENTS.md`), `README.md`, `.gitattributes` (`* text=auto eol=lf`), `.gitignore`, `.python-version` (`3.14`) | `.claude/skills/the-way-*/`, `.agents/skills/the-way-*/` (generated) | — |

- Test naming: always `test_*.py` (discovery pattern, `gate/run_tests.py:93`); tests sit in the same
  directory as the module (no `tests/` subdir, no `__init__.py`).
- Sibling import convention (fact): `sys.dont_write_bytecode = True` then
  `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` + `import <module>  # noqa: E402`
  (e.g. `elements/decisions/test_format_guard.py:21-22`, `instruction-files/test_check_instructions.py:23-24`,
  `project-level/test_readiness_check.py:22-23`, `gate/test_method_script.py:15-16`), or the
  `pathlib` form `sys.path.insert(0, str(Path(__file__).resolve().parent))`
  (`task-cycle/test_cycle_stages.py:15-17`, `project-level/test_plan_state.py:15`). Cross-directory:
  `sys.path.insert(0, os.path.join(ROOT, "elements", "decisions"))` (`gate/test_wording_reaches_dependants.py:26`).
  Scripts load other guards by path via `importlib.util.spec_from_file_location` under a unique module
  name (`elements/invariants/format_guard.py:57-74`) to avoid the shared module name `format_guard`.
- Fixtures: tests build temporary git repos and write expected fingerprints as literals, with a guard
  test that the fixture wording is unchanged (`gate/test_wording_reaches_dependants.py:8-10,68-71`;
  `elements/invariants/test_format_guard.py:27-34`).
- Placement constraints (fact): WAY-09/1 (`foundations/decisions.md:234-260`) lists the closed set of
  directories on the main branch ("a directory for each part of the process other than `repository` —
  `elements/<element>/` ..., `elements/common/`, `relation-model/`, `gate/`, `installation/`,
  `agent-instructions/`, `instruction-files/`, `project-level/` and `task-cycle/` — with `probes/`
  ...") and what each must hold. The part map (`foundations/part_map.md`) gives every tracked file to a
  part via *Files* globs (e.g. `instruction-files/**` `:221`, `installation/**` `:247`); its guard
  reports unclaimed files. Interpretation: a new top-level directory (e.g. `guidelines/`) needs a new
  WAY-09 version and a new part-map part; a new subdirectory of an existing part (e.g.
  `project-level/guidelines/` or `elements/common/...`) is covered by that part's `**` glob but its
  tests run only if `gate/run_tests.py <that subdirectory>` is invoked separately (no `__init__.py`),
  and a test there that cites an invariant makes `gate/run_tests.py <parent>` record `fail` for it
  ("not run: discovery does not reach its file", `gate/run_tests.py:50-54,518`). No existing part
  keeps tests in a subdirectory.
