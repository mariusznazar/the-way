# Author's report — guidelines-audit-report

**Status:** done

The change is whole and committed.

## Commits

- `5838d3a` — docs: WAY-280 to WAY-285 settle how an audit of the skills of guidelines ends, and WAY-187, WAY-201 and WAY-250 end with its list
- `ac27d26` — docs: the three audits of guidelines end alike in a shared file, with causes, weights, an order of repair and a top for the human
- `0ee0cd9` — docs: a stopped audit's hand-back says its list holds no order or decision yet

Base `2f51e6c`, branch `task/guidelines-audit-report`, not pushed, tree clean. Foundation first, as the handoff gave; nothing in my reading argued against it.

## Files changed

| File | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` | 241 | 25 |
| `product-guidelines/audit_end.md` (new) | 195 | 0 |
| `product-guidelines/coding/SKILL.md` | 17 | 7 |
| `product-guidelines/coding/hand_back.md` | 14 | 4 |
| `product-guidelines/coding/kinds.md` | 7 | 0 |
| `product-guidelines/coding/settle.md` | 3 | 0 |
| `product-guidelines/coding/task_document.md` | 9 | 6 |
| `product-guidelines/coding/trial_run.md` | 4 | 0 |
| `product-guidelines/styleguide/SKILL.md` | 9 | 4 |
| `product-guidelines/styleguide/audit.md` | 5 | 5 |
| `product-guidelines/styleguide/hand_back.md` | 5 | 0 |
| `product-guidelines/styleguide/settle.md` | 3 | 0 |
| `product-guidelines/styleguide/task_document.md` | 9 | 5 |
| `product-guidelines/testing/SKILL.md` | 16 | 7 |
| `product-guidelines/testing/audit.md` | 13 | 9 |
| `product-guidelines/testing/hand_back.md` | 12 | 2 |
| `product-guidelines/testing/settle.md` | 3 | 0 |
| `product-guidelines/testing/task_document.md` | 8 | 6 |
| `project-level/task/skill/guideline_findings.md` | 14 | 1 |

No skill's description changed, so `skill_entry_points.py --write` was not run. No file the part map names as a trust boundary changed.

## Foundation entries, with the meaning for the request

New, each written from its row whole:

| Entry | Row | Znaczenie |
|---|---|---|
| WAY-280 | 1 | Audyt w trzech skillach wytycznych daje każdej przyczynie jedną wagę (`grave`, `heavy`, `medium`, `light`) na jednej skali opisanej raz w pliku wspólnym, mierzonej skutkiem dla użytkownika albo właściciela i tym, co jest stawką, a nie liczbą miejsc; wagę, scalanie i kolejność the way przejmuje ze skilla audytu obserwowalności z kursu 10xDEVS, a audyt nie staje się osobnym skillem. |
| WAY-281 | 2 | Kilka naruszeń z jednego źródła to jedna przyczyna i jedna naprawa, a przyczyna niesie swoje miejsca; spis obejmuje też granicę zaufania, na której test odmowy jest należny i go nie ma, oraz reguły lintera łamane z jednego powodu, opisane skutkiem, z liczbą plików i bez nazw reguł, a ponowne formatowanie nie jest ustaleniem. |
| WAY-282 | 3 | Audyt kończy się kolejnością naprawy od `grave` w dół, a przy równej wadze pierwsza stoi naprawa, po której znika najwięcej problemu za najmniejszą pracę; zadanie łączące kod i testy ma jedną listę i jedną kolejność, tworzoną na końcu audytu, który biegnie ostatni, a ten może obniżyć albo wycofać przyczynę każdej dyscypliny, nie zmieniając niczego, co człowiek rozstrzygnął dla dyscypliny. |
| WAY-283 | 4 | Pełny spis zostaje w dokumencie zadania, a człowiek dostaje do decyzji górę listy: trzy do pięciu przyczyn na cały audyt, zawsze wszystkie `grave`, przy ponad pięciu `grave` wszystkie i nic więcej, przy mniej niż trzech przyczynach wszystkie; lista `do not copy` stoi poza tym limitem. |
| WAY-284 | 5 | Waga proponuje, człowiek rozstrzyga, które przyczyny z góry listy wchodzą do zadania; przy odłożeniu przyczyny `grave` agent pyta, czy założyć na nią zadanie w backlogu, a zgoda idzie drogą zadania wstępnego, tyle że nic na nie nie czeka; przyczyny spod góry są odkładane razem, chyba że człowiek weźmie którąś do zadania. |
| WAY-285 | 6 | Każda przyczyna z góry listy, zanim trafi do człowieka, jest sprawdzona: prowadzący audyt wraca do jej miejsc i patrzy, czy opisany skutek zachodzi; to, co się nie potwierdzi, obniża albo wycofuje, każde sprawdzenie zapisuje, także to, które przyczynę obniżyło albo wycofało, a czego nie da się zobaczyć bez działającego produktu, zostaje oznaczone jako niesprawdzone. |

Changed in place, under row 4 and its *Decisions in play* (WAY-30):

| Entry | Row | Znaczenie zmiany |
|---|---|---|
| WAY-187 | 4 | Audyt ekranów nadal idzie w obie strony i zadaje stałe pytanie, ale kończy się listą z WAY-283, a każda przyczyna ma jedną z czterech kategorii; limit trzech do pięciu i słowo „charge” znikają. |
| WAY-201 | 4 | Audyt kodu kończy się jak dotąd wzorcami i plikami `do not copy`, a dodatkowo listą z WAY-283; naruszenie o raportach lintera wymienionych po nazwach reguł zostaje. |
| WAY-250 | 4 | Audyt testów kończy się dla każdego poziomu wzorcem, dla każdej granicy zaufania informacją o teście odmowy, a na cały audyt, nie na poziom, listą z WAY-283; odrzucenie „lista zbyt długa, żeby ją zważyć” przechodzi do WAY-283. |

*Rejected* of each new entry holds only the ways the row's question keeps. Each row's weak point stands in its *Rationale*. *Origin* is `none` and *Based on* `none` for all six. WAY-280 names the course and the lesson with no address.

The search of the whole foundation (WAY-33) found no further entry to change: WAY-120, WAY-174, WAY-200, WAY-204, WAY-205, WAY-216, WAY-219, WAY-235, WAY-247 and WAY-251 stand as they are, and nothing in the glossary, the invariants, the part map or the environment facts speaks of these audits. No finding goes to Mariusz. The return step changed nothing further: the part map's `product-guidelines` entry covers the new file by `product-guidelines/**`.

## Checks

Each exit code was captured from the command itself, with its output sent to a file and through no pipe.

| Command | Exit code | At commit |
|---|---:|---|
| `python -B elements/common/foundation_check.py .` | 0 | `0ee0cd9` |
| `python -B gate/run_tests.py elements/common` | 0 | `ac27d26` |
| `python -B gate/run_tests.py agent-instructions` | 0 | `ac27d26` |
| `python -B gate/run_tests.py project-level` | 0 | `ac27d26` |
| `python -B gate/run_tests.py installation`, first run | 1 | moved from `ac27d26` to `0ee0cd9` while it ran |
| `python -B gate/run_tests.py installation`, second run | 0 | `0ee0cd9`, 44 tests |

**The failure and pass of `installation` (WAY-262).** The first run failed one test,
`test_moving_the_pin_to_the_same_process_changes_only_the_gitlink`, at `installation/test_install.py:228`. Its assertion expected a move back to `ac27d26`, and the installer's output named `Process commit: 0ee0cd9`: I committed `0ee0cd9` while that test ran, so the commit it took as the process's changed under it. That is a verified cause, read from the output against the two commits, and no fault of the change. The second run, with `HEAD` the same before and after, passed.

Not run: the directories `gate`, `instruction-files`, `relation-model` and `task-cycle`, which nothing of the change bears on, and the full gate, as below.

No test of the text was written, as the spec's non-goals give and as "Test behaviour, not text" gives for instructions to agents. The full gate was not run: it is the orchestrator's (handoff, WAY-160).

## Own-work check (WAY-164)

- **Requirement most likely not met:** To do 6, the top, since the spec's rule of the top is the one line of the change that can be wrong as arithmetic; and To do 8 with step 5, since the change sends a session across files by quoted section names, and a name that resolves to nothing fails silently.
- **Check:** a one-off script, outside the repository, ran the rule as `audit_end.md` words it on all 715 orders of up to nine causes and asserted To do 6's bounds; and resolved every quoted section name against the headings of `audit_end.md`, and every pointer in the three `SKILL.md` and `hand_back.md`.
- **Showed:** command `python -B <scratchpad>/own_check.py`, exit 0: 715 cases, 0 fails; 0 quoted-section failures, and the positive control matched the 6 quoted names expected. The first run stopped with exit 1 on a path of my script, `coding/audit.md`, which does not exist; that was the script's fault and no check of the change failed.
- **By reading:** I walked a task joining code and tests through the files, tests first and code first, and a joint task with the route of one kind, and each reaches the end the spec gives. The walk found that `hand_back.md`'s first check asks for an order a stopped audit does not have yet; `0ee0cd9` says so in the stopped audit's line.
- **Mutation in the head:** no script of the change exists to mutate. The rule of the top without "while it weighs as much as the one before it" would pull a `light` cause into the top where five exist, which the sample `ghhmml -> ghh` shows it does not.

## Reaches beyond the dispatch

- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/way_of_working.md` and `rules.md`: named by the element's skill for writing an entry.
- `project-level/task/skill/SKILL.md` steps 3 to 6, `resolve_gaps.md` and `read_sources.md`: to word the hand-back to step 3 and "step 1's document conventions".
- `product-guidelines/*/orchestrated_mode.md` and `styleguide/recognize.md`: to confirm that no change is needed there.
- WAY-95, WAY-172, WAY-185, WAY-199, WAY-207, WAY-219 and WAY-242, in part, and WAY-271 to WAY-273 and WAY-277 to WAY-279: the search of WAY-33 and the form of the last entries.
- `C:\Storage\The Brain\The Brain\.ai\rules\`, four files of the human's standing rules on scripts, git, knowledge artifacts and searches, which the global instructions have read before such work. No text of the change names them.

## Searches not found or unclear

- **WAY-13 uses "weight" for a task's process.** It is the ordinary sense, as the spec reads `weight`, so no glossary entry follows; the two meanings do stand in one log.
- **An audit stopped, then the other audit dropped**, which the review of the spec left unreported: no skill then ends the list. Unchanged by this change.

## Choices made

- **`The list` form as a fenced example in `audit_end.md`.** Rejected: prose only, which leaves the labels' nesting to be guessed. Cost if wrong: a few lines of one file.
- **Item form `- 1 — `heavy` — <cause>`.** The spec names the fields and not the punctuation. Rejected: a Markdown numbered list, which would renumber itself and could not hold the unnumbered `Withdrawn:` items in one run. Cost if wrong: one line of one form.
- **`Removes:` and `Reaches:` left out of the entries.** They stand in `audit_end.md`, as the spec's decision 2 gives a field in one file. WAY-282 says "removes most of the problem for the least work". Cost if wrong: a sentence in WAY-282.
- **The stopped audit's list carries `Fix:`, `Removes:` and `Reaches:`,** through "in the form of The list": the audit running last orders by them and does not know the other discipline's fixes. The spec says only "writes its causes".
- **The sentence "The write is `refine-task`'s"** stands in `guideline_findings.md`, so that a skill's table of what it never writes stays true; the spec gives the meaning and left the place open.
- **`Deferred:` naming a plan's task** is written as "the cause's `Deferred:` names it as its reason", the spec's "the cause names it as its reason".
- **WAY-280's *Rationale* describes the course's pattern only as far as the task document does**, since the task forbids reading the course's skill. It says what is adopted and not how the course words it.
- **Wording of *Rejected* in WAY-285 and WAY-281.** Question 6's "zmienia „sam” z pierwotnego zadania" became "it takes the check from the agent leading the audit", and question 5's "zarzuty" became "what the audit names as faults", since `charge` leaves the-way and an entry does not tell how it was reached. The meaning stands.

## Problems

- Several new lines stand at 101 or 102 characters, as lines of the log and of these files already do. No check holds them to a width.
- The focused tests ran on `ac27d26`; `0ee0cd9` changes two Markdown files no test reads, and only `foundation_check.py` ran again after it.
