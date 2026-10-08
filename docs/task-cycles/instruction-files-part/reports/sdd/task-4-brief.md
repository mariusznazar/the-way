### Task 4: Check script — dead paths by their sentence and place, and no network lookup (fixes A and C; spec §4.5, §4.6)

**Files:**
- Modify: `instruction-files/check_instructions.py` (docstring, imports, constants; new `is_network`, `paragraphs`, `negates_loading`, `says_not_loaded`, `bare_path`, `segments`; `resolve`, `check_file` and `check` replaced whole)
- Test: `instruction-files/test_check_instructions.py` (imports, constants, two new classes in place of one test, one method, one class)

**Interfaces:**
- Consumes: Task 3's names.
- Produces (used by Task 5): `is_network(token) -> bool`; `paragraphs(text)` yielding lists of `(line number, line)`; `negates_loading(sentence) -> bool` (called once per sentence of a paragraph that holds a dead path — the test counts its calls); `says_not_loaded(paragraph) -> callable(number, column) -> bool`; `bare_path(token) -> str`; `segments(token) -> list[str]`; `resolve(token, bases) -> bool` (a new signature: a list of base directories); `check_file(path, shown_as, root, findings, in_repo=True, agents_beside=False) -> str | None`. New messages: `` `<token>` is named in a sentence saying it does not load or exist `` (`INFO`), `` `<token>` is a name relative to a place the sentence gives, and does not resolve from the file, the repository or the home directory `` (`INFO`), `` `<token>` is a network path, not checked `` (`INFO`, `dead-path`), `@<token> is a network path, not checked` (`INFO`, `at-import`), `@<token> imports a file that is not there` (`WARN`).

- [ ] **Step 1: Write the failing tests** in `instruction-files/test_check_instructions.py`:

(a) In the imports, put `import builtins` before `import contextlib`, and `import re` after `import os`.

(b) After the line `DEFECTS = …`, insert:

```python
NETWORK_SPELLINGS = (
    "\\\\host\\share\\x.md",
    "//host/share/x.md",
    "/\\host\\share\\x.md",
    "\\/host/share/x.md",
    "\\\\?\\UNC\\host\\share\\x.md",
    "\\\\.\\pipe\\x.md",
    "\\??\\UNC\\host\\share\\x.md",
)
# What a network spelling becomes on its way to the file system, however it was joined or turned.
NETWORK_TRACE = re.compile(r"host[\\/]share|[\\/]pipe[\\/]")
```

(c) Delete the method `DeadPath.test_relative_path_in_a_file_outside_the_repository_is_only_noted` (fix C replaces what it asserted) and insert after class `DeadPath` the two classes:

```python
class SentenceSaysNotLoaded(CheckTestCase):
    def test_a_file_path_in_a_sentence_wrapped_over_two_lines_is_only_noted(self):
        repo = self.repo({"AGENTS.md": "The old guide `docs/old-guide.md` is\nnot read by any tool.\n"})
        found = dead(repo.findings())
        self.assertEqual([(f.level, f.line) for f in found], [("info", 1)])
        self.assertIn("named in a sentence saying it does not load or exist", found[0].message)

    def test_the_memory_sentence_is_only_noted(self):
        text = ("Który katalog pamięci sesja faktycznie widzi (globalny `~\\.claude\\memory\\` nie\n"
                "ładuje się do żadnej), co płaci się indeksem w każdej sesji.\n")
        repo = self.repo({"AGENTS.md": text}, outside={"global/CLAUDE.md": text})
        found = dead(repo.findings(extra=[os.path.join(repo.base, "global", "CLAUDE.md")]))
        self.assertEqual(sorted((f.level, f.line) for f in found), [("info", 1), ("info", 1)])

    def test_dead_paths_in_sentences_without_the_phrases_stay_warnings(self):
        repo = self.repo({"AGENTS.md": "Read `docs/gone.md` and the notes in `notes/gone/`.\n"
                                       "They load in every session. The cache does not load.\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["warn", "warn"])

    def test_a_sentence_in_one_list_item_does_not_reach_the_next(self):
        repo = self.repo({"AGENTS.md": "- The cache does not load\n- Read `docs/gone.md`\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["warn"])

    def test_crlf_line_ends_still_join_a_wrapped_sentence(self):
        repo = self.repo({"AGENTS.md": b"The old guide `docs/old-guide.md` is\r\nnot read by any tool.\r\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["info"])

    def test_each_sentence_is_tested_once_whatever_the_number_of_paths(self):
        sentences = 300
        lines = []
        for index in range(0, sentences, 2):
            lines.append(" ".join(
                "See " + " ".join(f"`d{number}/p{path}.md`" for path in range(10)) + "."
                for number in (index, index + 1)))
        repo = self.repo({"AGENTS.md": "\n".join(lines) + "\n"})
        with mock.patch.object(check_instructions, "negates_loading",
                               wraps=check_instructions.negates_loading) as tested:
            found = dead(repo.findings())
        self.assertEqual(len(found), sentences * 10)
        self.assertEqual(tested.call_count, sentences)


class OutsideRepository(CheckTestCase):
    def outside_findings(self, text, files=None):
        repo = self.repo(files or {"AGENTS.md": "Rules.\n"}, outside={"global/CLAUDE.md": text})
        return dead(repo.findings(extra=[os.path.join(repo.base, "global", "CLAUDE.md")]))

    def test_a_dead_path_of_two_segments_is_a_warning(self):
        found = self.outside_findings("Repositories are listed in `scripts/locations.json`.\n")
        self.assertEqual([f.level for f in found], ["warn"])

    def test_a_name_of_one_segment_is_only_noted(self):
        found = self.outside_findings("Copy `full_template.md` with `references\\` into `.cursor/`.\n")
        self.assertEqual([f.level for f in found], ["info", "info", "info"])

    def test_a_path_that_exists_from_the_home_directory_or_the_root_is_sound(self):
        write(self.home, "scripts/locations.json", "{}\n")
        found = self.outside_findings("Read `scripts/locations.json` and `docs/a.md`.\n",
                                      {"AGENTS.md": "Rules.\n", "docs/a.md": "x\n"})
        self.assertEqual(found, [])

    def test_a_windows_path_of_two_segments_is_a_warning(self):
        found = self.outside_findings("Decisions stand in `docs\\adr\\`.\n")
        self.assertEqual([f.level for f in found], ["warn"])

    def test_files_alone_are_checked_from_the_home_directory_too(self):
        repo = self.repo({}, outside={"g/CLAUDE.md": "Read `scripts/locations.json`.\n"})
        found = check_instructions.check(None, [os.path.join(repo.base, "g", "CLAUDE.md")])
        self.assertEqual([f.level for f in dead(found)], ["warn"])
```

(d) Append to class `RootLayout` (spec §4.5 edge, A20):

```python
    def test_agents_import_with_no_agents_md_beside_it_is_a_warning_on_any_line(self):
        for text, line in (("@AGENTS.md\n", 1), ("# Claude\n\nRules.\n@AGENTS.md\n", 4)):
            with self.subTest(line=line):
                repo = self.repo({"CLAUDE.md": text})
                found = [f for f in repo.findings() if f.check == "at-import"]
                self.assertEqual([(f.level, f.line) for f in found], [("warn", line)])
                self.assertIn("imports a file that is not there", found[0].message)
```

(e) Insert after class `Discovery`:

```python
class NetworkPaths(CheckTestCase):
    """A network path in a file under review never reaches the file system: on Windows a lookup of
    one reaches the network."""

    FILE_SYSTEM_CALLS = ("os.stat", "os.lstat", "os.scandir", "os.path.exists", "os.path.isfile",
                         "os.path.isdir", "os.path.islink", "os.path.isjunction",
                         "os.path.realpath", "builtins.open")

    def no_network_lookup(self):
        stack = contextlib.ExitStack()
        for name in self.FILE_SYSTEM_CALLS:
            module, attribute = name.rsplit(".", 1)
            real = getattr({"os": os, "os.path": os.path, "builtins": builtins}[module], attribute)

            def guarded(*args, _real=real, _name=name, **kwargs):
                if args and isinstance(args[0], (str, os.PathLike)):
                    if NETWORK_TRACE.search(os.fspath(args[0])):
                        self.fail(f"{_name} was given {os.fspath(args[0])!r}")
                return _real(*args, **kwargs)

            stack.enter_context(mock.patch(name, guarded))
        return stack

    def test_no_spelling_of_a_network_path_reaches_the_file_system(self):
        text = "".join(f"Read `{token}`.\n\nSee @{token} now\n\n" for token in NETWORK_SPELLINGS)
        repo = self.repo({"AGENTS.md": text, "CLAUDE.md": "@AGENTS.md\n" + text},
                         outside={"global.md": text})
        with self.no_network_lookup():
            found = repo.findings(extra=[os.path.join(repo.base, "global.md")])
        noted = [f for f in found if f.level == "info" and "network path, not checked" in f.message]
        self.assertEqual(len(noted), len(NETWORK_SPELLINGS) * 2 * 3)
        self.assertEqual([f for f in found if f.check in ("dead-path", "at-import")
                          and f.level != "info"], [])
```

- [ ] **Step 2: Run them to see them fail**

Run: `cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files 2>&1 | grep -E "^(FAIL|ERROR):|^Ran|^FAILED" | sed 's/ (.*//' | sort | uniq -c`
Expected (planner): `Ran 57 tests`, `FAILED (failures=10, errors=1, skipped=1)` — ERROR `test_each_sentence_is_tested_once_whatever_the_number_of_paths` (no `negates_loading` yet); FAILs `test_a_dead_path_of_two_segments_is_a_warning`, `test_a_file_path_in_a_sentence_wrapped_over_two_lines_is_only_noted`, `test_a_path_that_exists_from_the_home_directory_or_the_root_is_sound`, `test_a_windows_path_of_two_segments_is_a_warning`, `test_agents_import_with_no_agents_md_beside_it_is_a_warning_on_any_line` (two subtests), `test_crlf_line_ends_still_join_a_wrapped_sentence`, `test_files_alone_are_checked_from_the_home_directory_too`, `test_no_spelling_of_a_network_path_reaches_the_file_system`, `test_the_memory_sentence_is_only_noted`. The opposite-failure tests (`test_dead_paths_in_sentences_without_the_phrases_stay_warnings`, `test_a_sentence_in_one_list_item_does_not_reach_the_next`, `test_a_name_of_one_segment_is_only_noted`) pass already and must keep passing.

- [ ] **Step 3: Write the implementation** in `instruction-files/check_instructions.py`:

(a) The last paragraph of the module docstring (it begins "The files it reads are not the-way's") becomes, with "never looks a network path up," added:

```text
The files it reads are not the-way's, so it trusts none of them: it reads at most 1048576 bytes of
a file, opens only regular files, reads no file through a link that leads out of ROOT, follows no
link to a directory, never looks a network path up, and prints every value escaped and cut to 200
characters. It writes nothing and starts no program.
```

(b) Put `import bisect` after `import argparse`.

(c) Put `BLOCK_START = re.compile(r"^\s*([-*+]\s|\d+[.)]\s|#|\|)")` after the `FENCE` line, `SENTENCE_END = re.compile(r"(?<=[.!?])\s+")` after the `AT_IMPORT` line, and after the `LINE_SUFFIX` line:

```python
# Phrases saying that the thing a sentence names does not load, is not read or does not exist,
# in the languages of the instruction files met so far. A file in another language keeps the
# level a dead path has anywhere else.
NOT_LOADED_PHRASES = (
    "does not load", "doesn't load", "is not loaded", "never loads", "is not read",
    "does not read", "does not exist", "doesn't exist",
    "nie ładuje", "nie wczytuje", "nie jest wczytywan", "nie czyta", "nie istnieje",
)
NOT_LOADED = re.compile(
    "|".join(r"\b" + r"\s+".join(re.escape(word) for word in phrase.split())
             for phrase in NOT_LOADED_PHRASES),
    re.IGNORECASE)
```

(d) Insert after `reason`:

```python
def is_network(token):
    """True for a path that a lookup would send over the network: once `/` is read as `\\`, one
    that starts with `\\\\` (UNC, `\\\\?\\UNC\\…`, `\\\\.\\…`) or with `\\??\\`."""
    normal = token.replace("/", "\\")
    return normal.startswith("\\\\") or normal.startswith("\\??\\")
```

(e) Insert after `prose_lines`:

```python
def paragraphs(text):
    """Lists of (line number, line), one list per paragraph of prose: consecutive lines outside
    fenced code blocks, broken at a blank line, a fence, a heading, a list item or a table row."""
    current = []
    last = None
    for number, line in prose_lines(text):
        if not line.strip() or (last is not None and number != last + 1) or BLOCK_START.match(line):
            if current:
                yield current
            current = [(number, line)] if line.strip() else []
        else:
            current.append((number, line))
        last = number
    if current:
        yield current


def negates_loading(sentence):
    """True when SENTENCE says that what it names does not load, is not read or does not exist."""
    return NOT_LOADED.search(sentence) is not None


def says_not_loaded(paragraph):
    """A function of a line number and a column giving whether the sentence there says that what
    it names does not load or exist. The paragraph is joined once, with code spans masked, split
    once into sentences, and each sentence is tested once."""
    starts, joined = [], []
    offset = 0
    for _, line in paragraph:
        starts.append(offset)
        joined.append(CODE_SPAN.sub(lambda match: "x" * len(match.group(0)), line))
        offset += len(line) + 1
    text = " ".join(joined)
    bounds, verdicts = [], []
    position = 0
    for match in SENTENCE_END.finditer(text):
        bounds.append(position)
        verdicts.append(negates_loading(text[position:match.start()]))
        position = match.end()
    bounds.append(position)
    verdicts.append(negates_loading(text[position:]))
    line_start = {number: starts[index] for index, (number, _) in enumerate(paragraph)}

    def lookup(number, column):
        return verdicts[bisect.bisect_right(bounds, line_start[number] + column) - 1]

    return lookup
```

(f) Insert `bare_path` before `is_relative`, and `segments` after it:

```python
def bare_path(token):
    return os.path.expanduser(LINE_SUFFIX.sub("", token).rstrip("/\\"))
```

```python
def segments(token):
    parts = re.split(r"[\\/]", LINE_SUFFIX.sub("", token))
    return [part for part in parts if part not in ("", ".")]
```

(g) Replace `resolve` whole with:

```python
def resolve(token, bases):
    """True when TOKEN, a path that is not a network path, names something that exists: an
    absolute path as it stands, a relative one from any of BASES."""
    path = bare_path(token)
    if os.path.isabs(path) or re.match(r"^[A-Za-z]:", path):
        return os.path.exists(path)
    return any(os.path.exists(os.path.join(base, path)) for base in bases if base)
```

(h) Replace `check_file` whole with:

```python
def check_file(path, shown_as, root, findings, in_repo=True, agents_beside=False):
    """The per-file checks of one instruction file; returns its text, or None when it was not
    read."""
    text = read_text(path, shown_as, findings)
    if text is None:
        return None
    name = os.path.basename(path)
    file_dir = os.path.dirname(path)
    bases = [file_dir, root] if in_repo else [file_dir, root, os.path.expanduser("~")]
    for paragraph in paragraphs(text):
        not_loaded = None
        for number, line in paragraph:
            for match in CODE_SPAN.finditer(line):
                token = match.group(1).strip()
                if not looks_like_path(token):
                    continue
                if is_network(token):
                    findings.append(Finding("info", "dead-path", shown_as, number,
                                            f"`{shown(token)}` is a network path, not checked"))
                    continue
                if resolve(token, bases):
                    continue
                if not_loaded is None:
                    not_loaded = says_not_loaded(paragraph)
                if not_loaded(number, match.start()):
                    findings.append(Finding(
                        "info", "dead-path", shown_as, number,
                        f"`{shown(token)}` is named in a sentence saying it does not load or "
                        "exist"))
                elif not in_repo and is_relative(token) and len(segments(token)) == 1:
                    findings.append(Finding(
                        "info", "dead-path", shown_as, number,
                        f"`{shown(token)}` is a name relative to a place the sentence gives, and "
                        "does not resolve from the file, the repository or the home directory"))
                else:
                    findings.append(Finding("warn", "dead-path", shown_as, number,
                                            f"`{shown(token)}` does not exist"))
    emphasised = []
    for number, line in prose_lines(text):
        bare = CODE_SPAN.sub("", line)
        for match in AT_IMPORT.finditer(bare):
            token = match.group(1)
            if name == "CLAUDE.md" and agents_beside and line.strip() == "@AGENTS.md":
                continue
            if not ("." in token or "/" in token):
                continue
            if token[-1] in TRAILING:
                findings.append(Finding(
                    "error", "at-import", shown_as, number,
                    f"@{shown(token)} — a punctuation mark right after the path stops Claude Code "
                    "from loading it, without a warning"))
            elif is_network(token):
                findings.append(Finding("info", "at-import", shown_as, number,
                                        f"@{shown(token)} is a network path, not checked"))
            elif not resolve(token, [file_dir]):
                findings.append(Finding("warn", "at-import", shown_as, number,
                                        f"@{shown(token)} imports a file that is not there"))
            else:
                findings.append(Finding(
                    "warn", "at-import", shown_as, number,
                    f"@{shown(token)} — Claude Code loads the whole file into every session; Codex "
                    "reads it as plain text; a pointer is a path in backticks"))
        if EMPHASIS.search(line):
            emphasised.append(number)
    if len(emphasised) > 1:
        findings.append(Finding("warn", "emphasis", shown_as, emphasised[0],
                                f"{len(emphasised)} emphasised lines — emphasis on one rule at most"))
    if name != "SKILL.md":
        findings.append(Finding("info", "size", shown_as, 0,
                                f"{len(text.splitlines())} lines, {len(text.split())} words"))
    return text
```

(i) Replace `check` whole with:

```python
def check(root, extra=()):
    """Findings for the instruction files of the repository at ROOT and for EXTRA files. With ROOT
    None, only the EXTRA files are checked."""
    findings = []
    if root is None:
        for path in extra:
            check_file(path, path, None, findings, in_repo=False)
        return findings
    root = os.path.abspath(root)
    files = instruction_files(root, findings)
    present = set(files)
    texts = {}
    seen = set()
    for rel in files:
        path = os.path.join(root, *rel.split("/"))
        seen.add(os.path.realpath(path))
        folder = rel[: -len(os.path.basename(rel))]
        texts[rel] = check_file(path, rel, root, findings,
                                agents_beside=folder + "AGENTS.md" in present)
        if rel.startswith(".cursor/rules/") or "/.cursor/rules/" in rel:
            check_cursor_rule(rel, texts[rel], findings)
    for path in extra:
        if os.path.realpath(path) in seen:
            continue
        check_file(path, path, root, findings, in_repo=False)
    check_layout(root, files, texts, findings)
    return findings
```

- [ ] **Step 4: Run the tests to see them pass, and the script on the user's global file**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files > $R/reports/check_4_tests_instruction_files.txt 2>&1; echo "instruction-files $?"; tail -1 $R/reports/check_4_tests_instruction_files.txt; python -B instruction-files/check_instructions.py --file "C:/Users/Mariusz/.claude/CLAUDE.md" > $R/reports/check_4_global_file.txt; echo "exit $?"; grep -v "INFO  size" $R/reports/check_4_global_file.txt
```
Expected: `0`, `OK (skipped=1)` (57 tests); on the global file, as of planning: `` WARN  dead-path …CLAUDE.md:57 `scripts/locations.json` does not exist ``; `INFO` for `references\`, `full_template.md` and `mini_template.md` ("a name relative to a place the sentence gives…"); `` INFO … `~\.claude\memory\` is named in a sentence saying it does not load or exist ``; `0 error, 1 warn, 5 info`; exit 0. (The global file is the user's and may change; a different result is read against the file at the time, not taken as a defect.) The output holds only the paths and messages, never the file's text.

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "fix(instruction-files): Grade a dead path by its sentence and place, and never look up a network path" -m "$S" -- instruction-files/check_instructions.py instruction-files/test_check_instructions.py
```

---

