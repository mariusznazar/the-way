# SDD ledger — plan: .runs/task-cycles/instruction-files-part/plan.md

Spec: `.runs/task-cycles/instruction-files-part/spec.md` (revision 3, binding). Base 252152a. Task 0 and Task 1 (foundation step, element agents) run under the task-cycle skill's foundation step; Tasks 2–8 under SDD; Task 9 is the cycle's checks with the final review.

## Pre-flight scan

| Tasks | Shared file or interface | Produced vs consumed | Found |
|---|---|---|---|
| 0 → 3, 4, 5 | `instruction-files/check_instructions.py`, `test_check_instructions.py` | 0 copies af585e3 bytes; 3 replaces both whole; 4 and 5 edit 3's names | consistent: 3 "Consumes: the prototype's `Finding(...)`", 4 "Consumes: Task 3's names", 5 "Consumes: Tasks 3–4" |
| 0 → 6 | `instruction-files/SKILL.md` | 0 moves `skill/SKILL.md`; 6 rewrites the body, frontmatter unchanged (plan line 1999) | consistent with Task 2 consuming the frontmatter (line 376) |
| 2 ↔ 6 | entry points generated from `SKILL.md` frontmatter | 6 keeps name and description | consistent; Task 9 reruns the generator's dry run to confirm |
| 0 → 7 | `principles.md` | 0 copies; 7 exact edits and `## Sources` replaced | consistent |
| 0 → 8 | `tool_loading.md` | 0 copies; 8 rewrites with sources and the Cursor result | consistent; 8 consumes the facts of 1.2 |
| 0 → 1.7 | `foundations/part_map.md` | 0 adds the part (P2); 1.7 changes `agent-instructions` and the flow | consistent |
| 1.4 → 6, 7 | decision numbers WAY-128–133 | 6 and 7 cite them | consistent; Global Constraints: later tasks use the numbers 1.4 reports |
| 1.8 ↔ 3–5 | `agent-instructions/test_instruction_files.py` vs the check script | independent by design (WAY-69); the test imports nothing from `instruction-files/` | consistent |
| 6 | `README.md` | only Task 6 | consistent |
| 3 | own text | tests replace the file whole, implementation replaces whole; red counts given | consistent |
| 4 | own text | tests and implementation both name `paragraphs`, `negates_loading`, `is_network` | consistent |
| 5 | own text | `pointed_files`, `check_layout`, `check` replaced whole; tests in `RootLayout`, `Skills`, `PointedFiles` | consistent |
| 8 | own text | writes fixtures in the scratchpad only; V5 in the process root, read-only | consistent with spec §4.4 N4 |
| all | Global Constraints | commits by path; Write/Edit for files holding backslashes | consistent |

Scan clean; no ruling needed before execution.
Task 0: complete (commit 8f5459a; part-map agent opus; known reds gate and agent-instructions until Task 2)
Note for Task 8 (from the facts agent, 1.2): code.claude.com/docs/en/memory also documents that Claude Code reads a subdirectory's `AGENTS.md` on the first Read in that subdirectory, and "Not read: AGENTS.local.md, AGENTS.override.md, or anything under a .agents/ directory"; Cursor reading an `AGENTS.md` above the working directory is not on the Cursor page (no fact; tool_loading.md only).
Note for Task 4 (orchestrator): the user's global CLAUDE.md changed on disk during the cycle; it now names `scripts\locations.json` by an absolute path — the planned expected WARN on the global file may no longer appear; record the actual result as a changed input, not a defect.
Task 1: complete (commits 8f5459a..d87d74f: 67d61fa foundations, f401404 watches, d87d74f invariant checks; element agents opus, watch author sonnet; rulings in the cycle record Q14–Q23)
Ruling: single-rule-compliance re-sourced to the arXiv abstract (PDF unreadable by fact_probes) — the abstract states what WAY-133 and WAY-128 rest on — cost: the 67.7% figure leaves the fact.
Ruling: process root recreated at 252152a after it was removed outside this session — same commit the run brief names — cost: a directory the owner may have meant to remove.
Task 2: complete (commits d87d74f..588e0a3, review clean; implementer haiku, reviewer sonnet; trailer and 'entry points are current' verified by the orchestrator)
Task 3: review (opus) — Needs fixes: Critical 1 plan-mandated design (os.walk + realpath follow file links; a link to \host\share reaches the network and, named AGENTS.md, crashes with WinError 64). Ruling: own scandir walk with no link following; file-link chains resolved by os.readlink only (≤8 hops, normpath), network-shaped/absolute-outside/too-long → "link out of the repository", never touched; OSError → read WARN; --file network-shaped → usage error — the spec §4.6 network and no-traceback rows are the authority over the plan's code — cost: more code in the trust boundary than the plan foresaw. Minor 1 (literal U+FEFF/U+202E in tests) and Minor 2 (cut-character rule too loose) fixed in the same round.
Task 3: minor (deferred): shown() may cut through an escape; only MAIN_NAMES directories reported as directories; stat/open race to a FIFO; --file without read permission untested; FIFO test would hang on regression; three blank lines before def check.
Note for Task 5: fix D resolves pointed files' real paths — it must not call realpath/exists on a network-shaped or link target either (same rule as the Task 3 fix).
Task 3: fix round 1/5 (Critical 1 addressed on Windows, Minor 1–2 addressed; new: Critical POSIX file link out read via local_form; Important deep-tree RecursionError; Important tests contact the network creating UNC links (~90 s); Important POSIX directory link out unreported; commits 295e154..c06b237)
Ruling: fix round 2 by a fresh implementer on sonnet — round-1 implementer stopped (its leftover monitors kept notifying); the ruling is design, not transcription — cost: one tier above the original.
Ruling: platform split — Windows readlink chain with network check; POSIX realpath + inside, entry.is_dir() for directory links; explicit-stack walk; offline tests with os.readlink patched; POSIX-only tests skip on Windows, POSIX run recorded unchecked (no Linux Python on this machine; Docker Desktop not started for the cycle) — cost: the POSIX branch is checked by reading and the reviewer's simulation only.
Task 3: minor (deferred): `..` in a Windows link target resolved by text — unverified.
Task 3: fix round 2/5 (findings 1, 2, 4 addressed — 1, 4 by reading; 3 partly: tests offline but blind to a link-following classification; Minor DeepTree 1024-char limit, no POSIX loop test; commits c06b237..96cf68e)
Task 3: fix round 3/5 (4 addressed, 0 open — confirmed on three planted regressions; commits 96cf68e..193f656)
Task 3: minor (deferred): DeepTree cleanup may hit macOS's 256 open-file default (rmtree keeps one fd per level; guard: limit 100, depth 150); check_instructions.py:151 docstring line 106 characters.
Task 3: complete (commits 588e0a3..193f656, review clean after 3 fix rounds; implementers haiku → sonnet, reviewer opus)
Note for Task 4: the script has diverged from the plan's code after three fix rounds — it already has `WINDOWS`, `local_form`, `network_shaped`, an explicit-stack walk and `leads_out`. Task 4's brief adds `is_network(token)`: implement it on top of (or as) `network_shaped`, one rule for tokens and link targets, keeping the brief's name and signature for Task 5. Apply Task 4's edits to the current file by intent, not by replacing whole functions the fixes changed.
Task 4: complete (commits 193f656..fe55716, review clean; implementer sonnet, reviewer opus — 21 network spellings × 16 file-system calls: none reached; fix A linear on 1 MiB)
Task 4: minor (deferred, recommend fixing in the final wave): NOT_LOADED phrases lack a closing word boundary — "is not ready"/"is not readable" match "is not read", turning a really dead path into INFO (against task point 4: a really dead path above INFO); add \b except the deliberate prefix "nie jest wczytywan".
Task 4: minor (deferred): a heading line joins the next prose line into one sentence; "e.g. " splits a sentence; a network-shaped `@` token with no `.` or `/`, or a backtick token with a space, gets no "network path" note (safe, never looked up).
Task 5: review (opus) — Needs fixes: Critical .git link via os.path.exists reaches the network (:497); Critical NUL token ValueError traceback (:504); Minor skipped dirs on written path. Ruling: fix round 1 also takes the base-code gap in resolve (exists follows a link to a network target) — same file, same trust-boundary rule; cost: a broken link token is not reported dead.
Task 5: fix round 1/5 (3 addressed, 1 partly; new Critical `/` path through a directory link looked up (70.8 s); new Important repository under a junction loses dead-path and import checks; commits 0683617..5fe6ed1)
Task 5: minor (deferred, final review): a drive letter mapped to a network share is not network-shaped and can be looked up (predates Task 5); a 1 MiB paragraph of dead paths takes ~29 s with the link-safe walk (linear).
Task 5: fix round 2/5 (2 addressed, 0 open; commits 5fe6ed1..f97cbdd)
Task 5: complete (commits fe55716..f97cbdd, review clean after 2 fix rounds; implementer sonnet, reviewer opus)
Task 5: minor (deferred, final review): an absolute path under a folder where a disk is mounted (readlink gives \?\Volume{…}\, network-shaped) counts as existing; reparse points that are not readable links (OneDrive placeholders, deduplicated files) count as existing; paths climbing above the base walk from the drive root following local links by readlink (safe deviation from fix-2 ruling).
Task 6: review (opus) — Needs fixes: Important SKILL.md:37-39 tells the agent to read network paths / links out the script refuses; Important WAY-130 exception missing (plan/spec gap). Ruling: report, never follow; add the exception; removal wording to WAY-130; Minors 1–5 in the same round.
Note for Task 7: principles.md §7 must say what WAY-130 says on removal — a rule whose mistake can no longer be named is taken out; a named mistake that may no longer happen gets a removal test; and carry WAY-130's exception (a rule carrying a recorded decision or a step of the activity its file leads).
Task 6: fix round 1/5 (5 of 7 resolved; open: Judge threshold sentence lacks WAY-130 exception; new — removal sentence (controller's ruling wording) drops 'added for a mistake'; commits 9c5c722..0adbcc7). Ruling: round 2 also checks the pin on the pinned hash (out-of-scope observation, cheap, more exact) — cost: none.
Task 6: fix round 2/5 (all addressed; commits 0adbcc7..a19a2ec)
Task 6: complete (commits f97cbdd..a19a2ec, review clean after 2 fix rounds; implementer sonnet, reviewer opus)
Task 6: minor (deferred — recommend fixing in the final wave): the skill reads `.the-way/instruction-files/SKILL.md` as checked out, not at the pinned hash — when the submodule's HEAD differs from the pin it follows another copy than the pinned one (WAY-127/WAY-34 intent); pin check gives "move the pin" advice when the pinned commit is merely not fetched (`git submodule update`); Git Bash needs MSYS_NO_PATHCONV=1 for `':/.the-way'` and `<hash>:path` (not said).
Task 7: review (opus) — Needs fixes: Important §6 bullet (spec wording) grounds adding a rule on cost, against WAY-130. Ruling: reviewer's wording; Minors 1–6 in the same round.
Task 7: fix round 1/5 (7 addressed; commits bfd1206..c1669c6)
Task 7: complete (commits a19a2ec..c1669c6, review clean after 1 fix round; implementer sonnet, reviewer opus)
Task 7: minor (deferred): §6 does not list 'add a mechanism' among verdicts needing a repeated mistake (coverage gap); principles.md:248 'a linter, a hook, CI' unqualified (removal context).
Task 8: review (opus) — Needs fixes: Important ×4 (Codex method documented, pin Codex source to a commit, state --trust, codex-skill-paths beyond fact); ⚠️ unsupported skill-directory measurements → rest on facts or 'not established'; Minors 5–11 in the same round.
Task 8: fix round 1/5 (12 addressed; commits 9b6e86f..c60f3ea)
Task 8: complete (commits c1669c6..c60f3ea, review clean after 1 fix round; implementer sonnet, reviewer opus)
Task 8: minor (deferred): "loads at launch" beyond § User-level rules (and `~/.claude/CLAUDE.md` cited to a section that does not name it); "Not read: … anything under a .agents/ directory" should say "as project instructions" beside "`.agents/skills/`: not established"; "in a scratch directory" applied to V5; line 104 prose at 104 columns.
Final review (opus): With fixes — Important ×3 (skill copy vs pin incl. other product; phrase boundary; off-Windows network: Cygwin/MSYS //host, macOS /net/), Minor ×6; 17 deliberate breaks as predicted. Ruling: one fix wave (final-fix-wave.md) — guard Important 3 rather than document — cost: more platform rules in the trust boundary, POSIX unrun. Ruling: WAY-132 Rejected notice clause unchanged (public memory page states it). Ruling: invariant checks' positive control on an untracked CLAUDE.md stays (read-only, WAY-03).
Final fix wave: 8d60f10 — re-review: Important 1, 2 and all Minors fixed; the added "no pin → this copy governs" line accepted; Important 3 partly: off Windows (Cygwin, MSYS2, macOS) link targets are followed (entry.is_dir, realpath, lexists) so a tracked symlink to /net/<host> or //host reaches the host; new Minor: two NetworkShapesOffWindows tests hand `\\host\x.md` and `Z:\share\x.md` to the real lexists on Windows; out of scope: Polish plural forms miss (safe side WARN); reviewer's temp dirs (tmp*, one tmpoumerzxo with /net/evil.example symlinks) left under %TEMP% — hook blocked deletion.
Ruling (breaker, no second wave): Important 3 residual and the two tests carried into the step-11 settlement with the independent assessment's remarks — docstring states that link targets off Windows are not judged (the part map already records the failure mode as not detected); tests stub lexists — cost: the POSIX link guard is a stated limit, not code, until a POSIX run exists.
