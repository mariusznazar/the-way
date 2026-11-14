# Author report — task `deployment-skill-guide`

**Status:** done

**Commit:** `a900916` on `task/deployment-skill-guide` (base `d40d1cb`), not pushed.

## Files changed

| File | Added / removed |
|---|---|
| `project-level/task/deployment_skill_guide.md` (new) | +336 / 0 |
| `project-level/task/skill/resolve_gaps.md` | +5 / -1 |
| `foundations/decisions.md` (WAY-139, edited in place) | +32 / -6 |

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation form | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Tests of the part | `python -B -m unittest discover -s project-level -p "test_*.py"` | 0 (275 tests, OK) |
| Private paths and note links, the guide and `resolve_gaps.md` | `python -B task-cycle/private_paths_check.py <file>` | 0 for each (0 listed) |
| Private paths, every tracked file (invariant `tracked-file-private-paths`) | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (298 files, 0 listed) |
| Search for the real game address and the sender's mailbox domain (strings taken from the loop2 files) | `grep -rniE` over `project-level` and `foundations/decisions.md` | searched, none found |

Not run: the product's full gate (the orchestrator's). No failing-first run: the change is prose and
no invariant's test is new or changed.

## Own-work check

Requirement most likely not met: the guide carries nothing of loop2's own unmarked, no real address
or mailbox domain, and each fragment is a true excerpt of the one commit.

- The search above found none of the real strings in the committed text (only the GitHub link keeps
  the account name in the repository path, as the task asks).
- I compared every blockquote fragment of the guide with the files of the commit `e54f23c0…` with a
  scratch script (text with whitespace collapsed, markers `[loop2: …]` stripped, the example addresses
  turned back). First run: 31 fragments differed from the source. I rewrote them nearer to the
  source. Second run: 11 left (before a last edit of one word), each explained: the guide's own sample
  wordings for the refusal and the "no notice" answers (marked in the guide as written for it, not
  taken from loop2); the table of exit codes, which keeps rows 0, 5 and 8 only and so is not a
  contiguous passage; the docker command, which the script cut where the next paragraph follows it (a
  script artefact: the line stands whole in the source); and the sentences that say a copy of a secret
  stays outside the server, with the human, which is the adaptation the guide names in "How to read a
  part". No command or number differs.
- WAY-140 against part 5: the guide states that effects outside the repository are the human's and
  reads stay with the agent; see choice 3 for the one clause I left out.

## Foundation step

One entry, WAY-139, edited in place (WAY-07); both rows of *Settlements to record* land in it.

- `row 1` — English: The-way holds, beside the list of what a deployment skill covers, a guide to
  writing such a skill with loop2's as the first example; the guide binds nothing and the check of the
  list points to it from the item it adds.
- `row 1` — Polski: The way trzyma obok listy tego, co obejmuje skill wdrożeniowy, przewodnik po
  pisaniu takiego skilla, z loop2 jako pierwszym przykładem; przewodnik niczego nie wiąże, a wskazuje
  go sprawdzenie listy w punkcie, który dodaje.
- `row 2` — English: The guide shows loop2 by fragments of one commit, with a link to that commit and
  what is loop2's own marked, and shows no real address of the game and no mailbox address of its
  sender, only addresses in `example.com`.
- `row 2` — Polski: Przewodnik pokazuje loop2 fragmentami z jednego commitu, z linkiem do tego commitu
  i z oznaczeniem tego, co właściwe loop2, bez prawdziwego adresu gry i adresu pocztowego nadawcy,
  tylko z adresami w domenie `example.com`.

What changed in the entry: the binding sentences (the guide beside the list; the item and the task
split off point to it, the agent reads it only when it writes or completes a deployment skill);
*Verification* (one `complies` and one `violates` example added); *Rationale* (why the guide, its
price); *Rejected* (the ways not chosen under questions 1 and 2 of the task, each with its cost).
*Scope*, *Based on*, *Relations* and *Origin* stand as they were; I found no reason to add a relation.
The Rationale and Rejected I wrote name no file, script or count.

Search of the whole foundation once (WAY-33), after the entry was settled: searched
`foundations/*.md` and every `.md` and `.py` of the repository for `WAY-139`, `deployment skill`,
`holds no skill` and `loop2-deploy`. Found: four passages of other decisions that cite WAY-139 as the
check of the list (they read it as the check, which is unchanged) and `resolve_gaps.md` (edited).
No other entry states "holds no skill of a product" or the old wording of the sentence; nothing else
needed a correction.

Return step: compared the entry, the part map entry `project-level` (its sentence and `Files:
project-level/**` already cover a guide in `project-level/task/`) and the files; no correction needed.
WAY-09 lists what `project-level/` holds without naming a guide; the task says it stays unchanged, so
I left it (see Problems).

## Choices (with the way rejected and the cost if wrong)

1. **Meaning of "a preview of deployments".** WAY-139 gives no definition. The guide's part 2 takes it
   as both seeing what runs and what a deployment did, and trying a change on the server before the
   merge (loop2 has both). Rejected: reading it as a preview environment for each branch only, which
   loop2 does not have, so it would leave the part with no fragment. If the author meant only that,
   part 2's questions need a change; the other parts do not depend on it.
2. **Marking.** Loop2's own text stands inside `[loop2: …]` in a fragment; the rest of a fragment is
   the shape of the answer. Rejected: a separate list of "loop2's own" under each fragment (the task
   asks for the mark in the fragment). Cost if wrong: brackets break a long command; I kept commands in
   code spans with the marker around them.
3. **Left out the exception in "Every server or Cloudflare change is the human's, except deployment
   started by the existing automation".** The guide's fragment keeps the first clause with `…` after
   it. Reason: the exception is loop2's practice of an automated deployment on merge, and showing it
   as a general rule would sit awkwardly beside WAY-140 (every effect outside the repository goes
   through a human action). Rejected: quoting the whole sentence and explaining it. Cost if wrong: a
   reader who opens the loop2 link sees a clause the fragment cut; the `…` marks the cut.
4. **The refusal and the "no notice" answers are the guide's own wording**, in parts 7 and 8, labelled
   as written for the guide, because loop2 settled both items and has no such answer. Rejected:
   inventing a loop2 fragment. Cost if wrong: none for a product; the wording binds nothing.
5. **One commit** for the guide, the step's pointer and the decision; they depend on each other.
6. **Adaptations of the source** beyond markers and the two addresses: the owner's private notes said
   as "outside the server, with the human" (named in the guide), and shortenings marked with `…`.
7. **`<the-way>/project-level/task/deployment_skill_guide.md`** as the name the step gives the agent,
   the form the step already uses for `<the-way>/foundations/decisions.md`.

## Reaches beyond the dispatch

- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md` — read whole: the foundation step
  sends the writer there.
- Invariants `foundation-file-kinds`, `repository-file-location`, `outbound-link-reach`,
  `tracked-file-private-paths` — read whole, to see whether a file in `project-level/task/` and a
  link to loop2 are allowed and which text counts as an absolute path. The paths of the server
  (`/etc/…`, `/var/log/…`) are not listed by the script of WAY-309.
- `task-cycle/private_paths_check.py` (first 140 lines) — to know the patterns before writing the
  fragments.
- `agent-instructions/skill_entry_points.py` — run with `--check` by mistake (no such flag, exit 2);
  not needed, since no skill changed.

## Unread material

- WAY-09, WAY-07, WAY-33, WAY-165, WAY-267, WAY-270, WAY-139, WAY-140: read whole (the log's search
  I did with `grep` and read each entry's range; WAY-140's *Rationale* to its end I read to line
  3984 of the old file, not to the entry's last line).
- Invariants whose *Part* is `project-level` (`project-definition-form`, `project-readiness-gate`,
  `project-technology-record`, `project-plan-form`, `project-plan-check`,
  `project-plan-state-evidence`, `project-plan-state-subprocesses`) and the other invariants of Part
  `every`: seen by title and *Part* only; none concerns a prose file of `project-level/task/`.
- Part map: the entry `project-level` read whole, not the rest of the map.
- `elements/decisions/examples.md`: not read (the change edits one existing entry whose form I had
  before me).
- Loop2 at the commit: `SKILL.md` whole; `references/setup_and_secrets.md` lines 100-210, 329-383 and
  479-621 (not 1-99, 211-328, 384-478); `references/troubleshooting.md` lines 1-40 and 95-184 (not
  41-94, 185-203); `references/backup_and_restore.md`: headings only.

## Searches not found or unclear

- The meaning of "a preview of deployments" in WAY-139: not defined in the entry or in the task;
  chosen as in choice 1.
- A loop2 passage for the human's refusal of an item, or for a deliberate absence of a notice: none
  exists (loop2 settled both), so parts 7 and 8 carry wording of the guide.

## Problems as observed

- WAY-09 says `project-level/` holds "the templates of a project definition, a project plan and a task
  document, the skills that write them and lead a handed-over plan, the readiness check, the plan
  check…"; a guide for writing a product's deployment skill is not in that list. The task says WAY-09
  stays unchanged; the invariant `repository-file-location` is met (the file lies in a directory WAY-09
  names). Evidence: the sentence of WAY-09 quoted above. This may be worth a word from the reviewer or
  the human; I did not guess a rewording.
- The guide is long (336 lines) against the task's "do not copy the whole skill"; it holds 8 parts of
  about 30-60 lines each, and fragments are short excerpts, not the skill. If the reviewer finds it too
  long, the fragments of parts 5 and 8 are the first to cut.
