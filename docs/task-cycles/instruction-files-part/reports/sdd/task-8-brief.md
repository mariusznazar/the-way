### Task 8: The loading account, with the Cursor measurement (spec §4.4, task point 5)

**Files:**
- Modify: `instruction-files/tool_loading.md` (rewritten)
- Record only (ignored): `$R/reports/cursor_measurement.md`, `$R/reports/cursor_V1.txt` … `cursor_V5.txt`, `$R/reports/cursor_version.txt`

**Interfaces:**
- Consumes: the facts of 1.2; the measurement results of the prototype (`C:\Storage\repos\the-way-instruction-files\.runs\instruction-files-prototype\probes\wyniki_pomiarow.md`) and its research notes (`…\research_notes\`) as material for addresses and descriptions — never as a reference in the file.
- Produces: `tool_loading.md` with a source for every statement, a "Settings that change loading" subsection per tool (the skill of Task 6 reads it), and the answer to task point 5.

- [ ] **Step 1: Build the measurement fixtures** (O2; N4; scratch outside `C:\Storage`, nothing below any `.runs/`; the fixture files hold marker phrases only, and no backslash, so `printf` is safe here)

Run:
```bash
M=/c/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/821bfb3e-7677-4acf-bd0e-ab8a94541c58/scratchpad/cursor-measure && rm -rf "$M" && \
for v in v1 v3 v4; do mkdir -p "$M/$v/outer/repo/sub" && printf '# Repository file\n\nMK-ROOT-7000\n' > "$M/$v/outer/repo/AGENTS.md" && printf 'plain text\n' > "$M/$v/outer/repo/sub/x.txt" && git -C "$M/$v/outer/repo" init -q; done && \
printf '# Outer file\n\nMK-OUTER-7001\n' > "$M/v1/outer/AGENTS.md" && printf '# Outer file\n\nMK-OUTER-7001\n' > "$M/v3/outer/AGENTS.md" && git -C "$M/v3/outer" init -q && \
mkdir -p "$M/v4/elsewhere" && printf '# Outer file\n\nMK-OUTER-7001\n' > "$M/v4/elsewhere/outer-target.md" && \
python -B -c "import os, sys; os.symlink(sys.argv[1], sys.argv[2])" "$(cygpath -w "$M/v4/elsewhere/outer-target.md")" "$(cygpath -w "$M/v4/outer/AGENTS.md")"; echo "link $?"; \
find "$M" -name AGENTS.md | sort; python -B -c "import os, sys; print(os.path.islink(sys.argv[1]))" "$(cygpath -w "$M/v4/outer/AGENTS.md")"
```
Expected: `link 0` (the planner made file links in this scratchpad); five `AGENTS.md` paths; `True`. Where the link cannot be made, V4 is not run and the record says why (spec §4.4).

- [ ] **Step 2: Run one fresh session per variant**

Run (one Bash call; each session may take a minute — give the call a 600000 ms timeout):
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && W=$(pwd)/$R/reports && M=/c/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/821bfb3e-7677-4acf-bd0e-ab8a94541c58/scratchpad/cursor-measure && \
P='List every marker phrase of the form MK-WORD-NUMBER, and the first Markdown heading of every instruction or rules file, that your context holds now. Do not read, open or search any file, and run no command. Answer with that list only, one item per line, or with NONE.' && \
cursor-agent.cmd --version > "$W/cursor_version.txt" 2>&1; cat "$W/cursor_version.txt"; \
run() { (cd "$2" && cursor-agent.cmd -p --mode ask --sandbox enabled --output-format text "$P" > "$W/cursor_$1.txt" 2>&1; echo "$1 exit $?"); }; \
run V1 "$M/v1/outer/repo"; run V2 "$M/v1/outer/repo/sub"; run V3 "$M/v3/outer/repo"; run V4 "$M/v4/outer/repo"; run V5 /c/Storage/repos/the-way-process; \
for v in V1 V2 V3 V4 V5; do echo "== $v"; cat "$W/cursor_$v.txt"; done
```
Expected: `2026.10.01-e373342` (or the release installed then — record it); each run exit 0 with a list. If a run stops on workspace trust, rerun V1–V4 once with `--trust` added (scratch directories), and never pass `--trust` for V5 (`C:\Storage\repos\the-way-process`) — V5 is then not run (open question O-P1 of this plan). A run that fails for login or network is recorded by its message, not retried more than once.

- [ ] **Step 3: Read and record the result** in `$R/reports/cursor_measurement.md` (Write tool): the release, the date, the command, and per variant the markers and headings answered. A variant counts only with its positive control: `MK-ROOT-7000` and `# Repository file` in V1–V4; `# Working in the-way` (the process root's `AGENTS.md`) in V5. Then:

| Variant | Question | `MK-OUTER-7001` / the global file's heading in the answer means |
|---|---|---|
| V1 (start at the repository's root; the file one directory above, outside git) | above the root | Cursor loads an `AGENTS.md` above the repository's root |
| V2 (start in `sub/`) | above the root, from a subdirectory | the same, from a subdirectory |
| V3 (the directory above is itself a git repository) | above, inside an enclosing repository | Cursor walks up into the enclosing repository |
| V4 (the file above is a symbolic link to a file elsewhere) | a linked file above | Cursor follows the link |
| V5 (`C:\Storage\repos\the-way-process`, two directories below `C:\Storage\AGENTS.md`, a link to the user's global file) | the real case | the global file's first heading in V5 and **not** in V1 (the negative control: V1 lies outside `C:\Storage`) — it reaches Cursor through `C:\Storage\AGENTS.md`; in both — it reaches Cursor by another route (user rules), and V5 establishes nothing about the link; in neither — not loaded |

- [ ] **Step 4: Rewrite `instruction-files/tool_loading.md`** with the Write tool, from the prototype's text, by these rules (spec §4.4):
  - The opening paragraph becomes:
```markdown
# How each tool loads instruction files

Each statement below carries its source: `fact <identifier>`, an environment fact of the-way whose
entry in `foundations/environment_facts.md` holds the passage it rests on; the address of the
documentation or the public source it was read at; or *measured*, with what was measured
described where it stands. A statement no source supports says "not established". Loading changes
between versions without notice: before a rule relies on it, check it in the version in use — the
method is at the end.
```
  - Every bullet keeps its statement and ends with its one source in brackets: ``(fact `<id>`)`` where a fact of 1.2 or an existing fact holds it — `claude-code-imports` (`@path` loads the file at launch), `claude-code-agents-md` (`AGENTS.md` only without `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md`; v2.1.277), `claude-code-path-rules` (a rule with `paths`), `claude-code-project-skills` and `claude-code-nested-skills` (where skills load), `codex-agents-md` (the chain from the root to the working directory), `codex-repository-skills` (`.agents/skills`), `cursor-agents-md` (`AGENTS.md` and `CLAUDE.md` at the root); otherwise `(<address>)` — the documentation page the research notes record for that statement (`code.claude.com/docs/en/memory`, `…/skills`, `…/hooks`; `learn.chatgpt.com/docs/agent-configuration/agents-md`, `…/build-skills`; `cursor.com/docs/rules`, `cursor.com/docs/cli/using`; Cursor's public forum thread; the public source of Codex at a commit), opened again where cheap; otherwise `(measured, see below)`.
  - A statement the prototype marks "measured" moves its evidence into a closing section `## Measurements`, one bullet per measurement, each with the tool and release, the date 2026-10-07, the setup (one fresh headless session per variant in its own directory, a marker phrase in each file under test, a file that must load as the positive control; in Claude Code the `InstructionsLoaded` hook's log) and the counts, taken from `wyniki_pomiarow.md`: Claude Code 2.1.293 (`claude -p`) — `@path` followed at once by `.`, `,`, `)` or `:` did not load, without a warning, while a space or the end of the line after it loaded; a subdirectory `CLAUDE.md` and a rule with `paths` did not load at the start and loaded on a read, on a write without an earlier read and on `cat` in Bash; `.agents/skills/` was not read; Codex CLI 0.157.0 (`codex exec`) — a rule in `pkg/AGENTS.md` was followed in 0 of 4 sessions started at the root and in 2 of 2 started in `pkg/`, while the root's rule held in 4 of 4; `.claude/skills/` was not read; Cursor CLI 2026.10.01 (`cursor-agent -p`) — at the start `AGENTS.md`, `CLAUDE.md` and a rule with `alwaysApply: true` loaded, while a file named with `@` in a rule, a rule with only a description, `.claude/rules/`, a subdirectory `AGENTS.md` and glob rules did not; on a read a subdirectory `AGENTS.md` and a glob rule loaded; on a write without a read the glob rule did not. Where a fact now holds a statement the prototype marked measured (`AGENTS.md` alone in Claude Code), the fact is its source and the measurement may stay as a corroborating bullet.
  - Each tool's section gains `### Settings that change loading`, each item with the key to search for and its documentation address: Codex — `project_doc_max_bytes` (32 KiB by default; the documentation says both "combined" and "each" file), `project_doc_fallback_filenames`, `AGENTS.override.md`, `CODEX_HOME`, all at `https://learn.chatgpt.com/docs/agent-configuration/agents-md` (opened again: a key the page does not name is left out and the record says so); Claude Code — the "Project instructions" setting, `claude-md-or-agents-md` by default, written with the key the page gives for it (when the page names no key, the setting's name and that value are what to search for), and `claudeMdExcludes`, at `https://code.claude.com/docs/en/memory`; Cursor — "No setting that changes which instruction files load is found in Cursor's documentation (`https://cursor.com/docs/rules`, `https://cursor.com/docs/cli/using`)."
  - The Cursor section gains a bullet **An `AGENTS.md` above the directory it works in:** worded from Step 3's result, with no path of this machine, as *measured* — for example "loaded in a session started at a repository's root when it stands one directory above, outside git (Cursor CLI <release>, <date>, 1 of 1 session), and in a session started in a subdirectory (1 of 1); <…> when the directory above is itself a git repository; <…> when the file above is a symbolic link to a file elsewhere; in the real case of a link two directories above, its file's first heading <appeared / did not appear>, and it did not appear in a session started outside that directory (the negative control); one fresh `cursor-agent -p --mode ask --sandbox enabled` session per variant, a marker phrase per file, the repository's own `AGENTS.md` as the positive control". **If no variant ran with its positive control**, the bullet reads exactly: "Whether Cursor loads an `AGENTS.md` above the directory it works in is neither documented nor measured." and the record says that task point 5 is unmet; if V1 ran and neither V4 nor V5 did, the bullet states the plain-file result and adds "Whether it follows a linked file there is not established.", and the record says point 5 is met for a plain file and unmet for a linked one.
  - The closing `## Method of checking` keeps its text, with a source on the claim about the `InstructionsLoaded` hook (`code.claude.com/docs/en/hooks`).
  - No date of the prototype's research outside the measurements, no `.runs/`, no path of the user's machine, no private note.

- [ ] **Step 5: Check** — write this read-only script with the Write tool to `.runs/task-cycles/instruction-files-part/reports/sources_check.py` (ignored), then run the commands below:

```python
"""Lists every bullet of a Markdown file that carries no source: a fact, an address, a
measurement, or the words saying none is established. Usage: python -B sources_check.py FILE"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
bullets = re.findall(r"^- .*?(?=^- |^#|^\s*$|\Z)", text, re.M | re.S)
marks = ("(fact `", "(http", "measured", "not established", "neither documented nor measured")
missing = [bullet.splitlines()[0] for bullet in bullets if not any(m in bullet for m in marks)]
print("\n".join(missing))
print(f"{len(bullets)} bullets, {len(missing)} without a source")
sys.exit(1 if missing else 0)
```

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B $R/reports/sources_check.py instruction-files/tool_loading.md; echo "sources $?"; grep -n -i -e "\.runs" -e "/c/" -e "Storage" -e "Mariusz" -e "The Brain" -e "AppData" instruction-files/tool_loading.md; echo "local $?"; for id in $(grep -o '`[a-z0-9]*-[a-z0-9-]*`' instruction-files/tool_loading.md | tr -d '`' | sort -u); do grep -q "^## $id/" foundations/environment_facts.md && echo "fact $id"; done
```
Expected: `0 without a source`, `sources 0` (the planner ran the script on the prototype's file: `18 bullets, 8 without a source`, exit 1 — it finds what it should); `local 1`; the `fact` lines name only facts that exist. The check script is not run on `tool_loading.md`, which is no instruction file.

- [ ] **Step 6: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "docs(instruction-files): Give every loading statement its source, the settings that change loading, and Cursor above the working directory" -m "$S" -- instruction-files/tool_loading.md
```

---

