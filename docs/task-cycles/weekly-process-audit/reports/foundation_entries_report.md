# Report — the agent of the plan's Foundation entries

**Status:** done with concerns (the concerns are open points for the orchestrator, none blocks).

## Commits and files

- `1adca16` "Record the decisions of the weekly process audit and add its part to four decisions" —
  `foundations/decisions.md` only: +288 / -8 lines. Base `e3825a82386a61930a86f8517fc0c5f422fc2833`.
- Written through the decisions skill (`elements/decisions/skill/SKILL.md`, `decide_entry.md`, `read.md`,
  `template.md`, `elements/common/rules.md`, `way_of_working.md`). Numbers 327 to 338 were the next free
  ones; no withdrawn number is above 224.

## Entries (meaning in English, then in Polish)

| Entry | Mark | English | Polski |
|---|---|---|---|
| WAY-327 | row 1 | The-way gives the template of the register of problems; the audit reads the register a locations entry names and assigns no class or weight itself; the user's tool fills it and the user adapts the template. | the way daje szablon rejestru problemów; audyt czyta rejestr wskazany wpisem w pliku lokalizacji i sam nie nadaje klasy ani wagi; rejestr wypełnia narzędzie użytkownika, który dostosowuje szablon. |
| WAY-328 | row 2 | The audit is a part of its own, `process-audit`, with the directory `process-audit/`, apart from `task-cycle`. | Audyt jest własną częścią `process-audit` z katalogiem `process-audit/`, osobno od `task-cycle`. |
| WAY-329 | row 3 | The audit's results lie outside every repository, at a place a locations entry names. | Wyniki audytu leżą poza wszystkimi repozytoriami, w miejscu wskazanym wpisem w pliku lokalizacji. |
| WAY-330 | row 4 | A problem has a weight on four levels (no problem, Minor, Important, Critical) and a class from a list the template starts and the audit widens. | Problem ma wagę w czterech poziomach (brak problemu, Minor, Important, Critical) i klasę z listy, którą szablon zaczyna, a audyt poszerza. |
| WAY-331 | row 5 | The audit counts problems, not remarks: a problem reported by several stages of one cycle is one. | Audyt liczy problemy, nie uwagi: problem zgłoszony przez kilka etapów jednego cyklu jest jednym problemem. |
| WAY-332 | row 6 | Whether a fix works is decided by the cycles whose version of the-way holds it against those whose version lacks it, never by date. | O tym, czy poprawka działa, rozstrzygają cykle, których wersja the way ją zawiera, w zestawieniu z tymi, których wersja jej nie ma — nigdy data. |
| WAY-333 | row 7 | How often an issue comes back is material for the human to weigh; the audit sets no priority and ranks nothing from it. | Częstość powrotów sprawy jest materiałem do ważenia przez człowieka; audyt nie nadaje z niej priorytetu ani nie szereguje spraw. |
| WAY-334 | row 8 | Cost is two numbers: cost at constant prices from a dated price list, and the share of fix rounds; no divisor of task size. | Koszt to dwie liczby: koszt w stałych cenach według cennika z datą i udział rund poprawek; bez mianownika wielkości zadania. |
| WAY-335 | row 9 | Time is two measures: agents' working time without the wait for the human, and apart the wait for tools. | Czas to dwie miary: czas pracy agentów bez czekania na człowieka i osobno czas czekania na narzędzia. |
| WAY-336 | row 10 | A new price list, or a change of a stage report's form, of the list of classes or of the reviewer's instructions, starts a new series; measures compare within a series, never week against week. | Nowy cennik albo zmiana formatu raportu etapu, listy klas lub instrukcji recenzenta zaczyna nową serię; miary porównuje się w obrębie serii, nie tydzień do tygodnia. |
| WAY-337 | row 11 | The audit replays no frozen earlier tasks on an old and a new version of the process. | Audyt nie odtwarza zamrożonych dawnych zadań na starej i nowej wersji procesu. |
| WAY-338 | row 12 | The audit runs weekly in a session of its own; the counting runs unattended on the night from Friday to Saturday; a weekly backlog task starts the session. | Audyt odbywa się raz w tygodniu w osobnej sesji; liczenie biegnie bez człowieka w nocy z piątku na sobotę; sesję wyzwala cotygodniowe zadanie w backlogu. |
| WAY-09 (changed) | plan item (To do 1) | The list of the repository's directories gains `process-audit/`; the sentence of what a directory must hold gains the template of the register, the dated price list of models, the counting command and the weekly-session skill; `process-audit` joins its Scope, the list in Verification, a complies example and the Rationale (a pointer to WAY-328). *Rejected* untouched. | Lista katalogów repozytorium zyskuje `process-audit/`, a zdanie o zawartości katalogu — szablon rejestru, cennik modeli z datą, polecenie liczenia i skill sesji tygodniowej; `process-audit` wchodzi do Scope, do listy w Verification, do przykładu complies i do Rationale (odsyłacz do WAY-328). *Rejected* bez zmian. |
| WAY-38, WAY-89, WAY-320 (changed) | plan items | Only *Scope* gains `process-audit`. | Tylko *Scope* zyskuje `process-audit`. |

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` after the commit: exit 1,
  16 errors, every one of the form "`process-audit` names no part" — at WAY-09, WAY-38, WAY-89,
  WAY-320 (4) and WAY-327 to WAY-338 (12). Nothing else is reported; it clears when Slice 1 writes the
  part-map entry. Before my edits the check was not run (the handoff names the run after the commits).
- No tests were run: the change touches only the decision log and the handoff names no other check.
- A search of the new region for the words *should*, *will*, *must* (whole words) found none.

## Own-work check (make-change section 3)

- Requirement most likely not met: the template says *Rejected* of a decision written from a row holds
  only the ways the row's source keeps, and never a way the writer derives from "what the cycle would
  otherwise guess".
- Check: for each entry, compare its *Rejected* with the task's *Questions to settle* and the quoted
  *Source* of the row. Result: rows 1, 2, 3 take the *Not chosen* of their questions; rows 7, 8, 9, 11,
  12 take the way their quoted source names (frequency raising priority by itself; a divisor; the wait
  for the human; the frozen set; the audit inside the weekly review); rows 4, 5, 6, 10 have no way
  in their source, so *Rejected* is `unknown`. The guessed ways of the last column of the
  *Settlements to record* (five levels, a closed list, a date comparison, a week-to-week comparison,
  tokens, a cost per line, "on demand") are in no *Rejected*. The check is by reading; no script.

## Choices (with the way rejected and the cost if wrong)

1. Directory name `process-audit/`, equal to the part's name, as every other part's directory is named.
   Rejected: `audit/`. If wrong: one rename in WAY-09 and WAY-328, and Slice 1's files.
2. WAY-328 (row 2) kept as an entry of its own beside the WAY-09 change, as the plan lists both; it
   `derives from WAY-09` and carries the *Rejected* (the audit inside `task-cycle/`). The WAY-09
   Rationale only points to it. Rejected: leaving row 2 only as the WAY-09 change (the row's rejected
   way would have no entry). If wrong: one entry to merge into WAY-09.
3. Row 8 and row 9 words: "rounds of fixes after review" (the task's "rundy poprawek po recenzji")
   and "the time its agents wait for tools". The task's item 7 (a subagent call is no wait for a tool)
   is left out of WAY-335, since it is a requirement of the task and no settled row; Slice 2 and the
   code define it. If the orchestrator wants it in the decision, WAY-335 gets one sentence (the entry
   would then be marked `the cycle's` in part).
4. Row 12 says "the user's weekly review" for the row's "przegląd tygodnia", as the-way is public and
   the review of the week is the user's own routine; no other name was invented.
5. *Relations*: WAY-327 derives from WAY-103 and WAY-320; WAY-328 from WAY-09; WAY-329 from WAY-320;
   WAY-330, WAY-331 from WAY-327; the others none. The WAY-103 link is a judgment (adaptable template for
   other users); if the orchestrator reads it as too strong, drop that one relation.
6. Scope of WAY-328 is `process-audit, task-cycle` (so a change to the task cycle's part meets the
   decision); the others `process-audit` alone.

## Concerns

- The word "issue" (Polish "sprawa") is used in WAY-327 and WAY-333 with a meaning of its own: one
  matter that like problems of several cycles make. WAY-327 defines it in its binding sentence. It is
  a candidate for a glossary entry (WAY-95, `the-way-record-glossary-term`); I wrote none, since the
  plan lists none, and ask the orchestrator to decide.
- `README.md` at the repository root lists the repository's directories (line 121); it gains
  `process-audit/` in a later slice (outside this stage's boundary; `README.md` is a file that
  "binds nothing" per the part map, but a reader meets the stale list).
- The invariant `repository-file-location` and `element-directory-contents` derive from WAY-09, and
  their wording points to WAY-09 for the directories; not edited, as they name no directory.
- WAY-303 says no other periodic review reads the unfixed remarks of merged requests. The audit as
  written reads the register of problems and cycle records, not those remarks, so I saw no collision;
  if the user's tool fills the register from request descriptions, that lies outside the-way.

## Reaches beyond the handoff

- `foundations/decisions.md`: WAY-03 (as the form example named in `examples.md`), WAY-07, WAY-21, WAY-44,
  WAY-135, WAY-161 (the grades Minor/Important/Critical), WAY-325 and WAY-326 (recent entries read for
  form) — each read whole (WAY-135/161 up to the first lines of Verification only: see Unread material).
- A grep of `foundations/` for audit, price, weekly, nightly, "process pin", locations and cost words;
  the passages of WAY-163 (cost in the record), WAY-289-area, WAY-294, WAY-303 and the WAY-309 rationale
  were read where the hits led. The decision of the author's nightly review is not in the foundation.
- `foundations/part_map.md` and `foundations/glossary.md`, whole, to check the part names and the
  vocabulary; `task-cycle/record_template.md` lines 1 to 40 to see what the cycle record names as its
  version (field "Process pin"); `foundations/invariants.md` lines 24 to 36, 106 to 118, 186 to 195 for
  the invariants that derive from WAY-09, WAY-38 and WAY-89.
- A grep for `foundation-review/` across the worktree to find lists of directories (found README.md and
  WAY-09 only).

## Unread material

- The handoff names WAY-103, WAY-140, WAY-320, WAY-260, WAY-296, WAY-135, WAY-134 as "most likely to
  bear". Read whole: WAY-103, WAY-140 up to its Rationale start (lines 3843 to 3880, the rest of its
  Rationale and Rejected unread), WAY-260, WAY-296, WAY-320, WAY-134 (binding sentences and head of the
  entry; its Relations onward unread), WAY-135 (binding sentences and the head of Verification; the rest
  unread). WAY-161 read to the head of Verification. None of the unread remainders bears on a rule I
  wrote (they concern human actions, the spec, and the findings of a review).
- `task-cycle/change/SKILL.md` and `task-cycle/skill/foundation_step.md` were read whole. The plan file
  `plan.md` was not read, as the handoff says.
- WAY-294, WAY-303, WAY-163 and the WAY-309 rationale were read in the passages the grep led to, not whole.

## Searches not found or unclear

- No decision of the foundation defines "the weekly review" or the author's nightly review; it is the
  user's private routine, so WAY-338 names it by description only.
- The task's item 7 (what counts as a wait for a tool) is defined nowhere in the foundation; it is left
  to Slice 2 (see choice 3).
- No glossary entry for "issue" / "series" exists; "series" is used in plain meaning in WAY-336.
