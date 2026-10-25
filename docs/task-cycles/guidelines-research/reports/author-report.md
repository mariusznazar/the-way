# Author report

Status: done

Commit: `a6453b7` — `Align guideline research and tool recommendations`

Repository: `C:/Storage/repos/the-way-wt/guidelines-research`

Branch: `task/guidelines-research`

Base: `2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c`

## Change

The three guideline skills research the product's technology for first guidelines where the human has no preference and for every extension, including extensions with a preferred tool. Refreshes use the accepted guidance and the requested update or correction without research. The shared distinction is recorded in WAY-251 and stated at the point where each skill recognizes its mode.

Every new-tool choice stays a human question of the task. Its presentation gives consequences, a recommendation and that recommendation's weak point. A preferred tool stays the recommendation; otherwise, where no difference with a product consequence remains, the simplest and cheapest is recommended. The coding skill no longer defaults to the most-used tool.

Dependent instructions no longer require research reports on paths without research: critique is conditional on research having run, task Context includes research sources only where research ran, and handback accepts any research reports. Coding's trial run uses the set proposed from preferences, research or the requested correction, with the version read from the product or the proposed tool's documentation. For first coding guidelines without code, the tool's documented recommended rules remain the blocking proposal even when a preference supplied the tool and no research ran.

The first styleguide for an existing screen set goes through starting rules as well as its existing audit. No audit, trial-run, invariant or adoption requirement was otherwise changed.

## Changed files

| Path | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` | 163 | 94 |
| `product-guidelines/coding/SKILL.md` | 44 | 31 |
| `product-guidelines/styleguide/SKILL.md` | 35 | 18 |
| `product-guidelines/testing/SKILL.md` | 32 | 16 |

No executable code, tests, invariant entries or invariant tests changed. Skill names, descriptions and paths are unchanged, so no generated entry-point write was needed. No writes were made outside this worktree.

## Checks

Commands below ran from the repository root named above.

| Exact command | Exit code | Observation |
|---|---:|---|
| `python -B elements/common/foundation_check.py` | 0 | First check after implementation: `0 errors`. |
| `python -B elements/common/foundation_check.py` | 1 | After paragraph formatting: five entries lacked a recognized `*Rejected:*` line. The formatting had joined the label into the preceding rationale line; the checker identified all five. |
| `python -B elements/common/foundation_check.py` | 0 | After restoring the labels to line starts: `0 errors`. |
| `python -B elements/common/foundation_check.py` | 0 | Final changed files after formatting corrections: `0 errors`. |
| `python -B agent-instructions/skill_entry_points.py` | 0 | Run after initial formatting, after its correction, and on the final files; each reported `entry points are current`. |
| `git diff --check` | 0 | Run during implementation and again on final files; no whitespace errors. |
| `rg -n -C 2 'research\|preferred\|simplest\|refresh\|extension\|New tools' product-guidelines/coding/SKILL.md product-guidelines/styleguide/SKILL.md product-guidelines/testing/SKILL.md` | 0 | The actual command used alternation without backslashes before the bars, shown in the executable block below; read every resulting research-related instruction for the own-work check. |
| `git diff --word-diff=plain -- foundations/decisions.md` | 0 | Read the semantic changes of all seven entries against the task; rationale, rejected choices and verification match the binding text. |
| `git diff --numstat` | 0 | Produced the counts above. |

Exact executable search command (literal bars are alternation inside the quoted pattern):

```powershell
rg -n -C 2 'research|preferred|simplest|refresh|extension|New tools' product-guidelines/coding/SKILL.md product-guidelines/styleguide/SKILL.md product-guidelines/testing/SKILL.md
```

One intermediate PowerShell batch ran formatting, `git diff --check`, the failing foundation check and the passing entry-point check sequentially; the batch exit was 0 because its last command passed. The foundation failure was immediately repeated alone to capture exit 1, then corrected. No failure remains open.

Not run:

- `python -B gate/run_tests.py`: the orchestrator owns the whole-gate run after this handoff, as dispatched.
- Fresh-agent behavioral trials of the three edited skills: no child agents were dispatched by this author; the independent whole-change review follows this return. The scenario check below is a manual instruction walkthrough, not evidence of an executed refinement session.
- Product runtime or UI checks: this change is process prose and changes no product code or UI.
- New tests: none added; assertions on the wording would mirror the implementation rather than check a behavior. No first-failing or invariant-test run applies.

## Own-work check

Most likely missed requirement: removing refresh research while a later step still expects its report, or letting the new recommendation rule override a preferred tool during an extension.

Check: use the exact search command above to locate every related instruction in all three skills; read the full diff and manually trace these cases through recognition, step 2, settling and handback. Expected behavior comes from To do 1–3, all four accepted settlement rows and the task's explicit version-change example.

| Case | Observation in final instructions |
|---|---|
| First guidelines, no preference | Every discipline enters research and critiques its reports before proposing results. Styleguide includes existing screens and keeps their audit. |
| First guidelines, a tool preference | The preferred tool is proposed; research is not required by the first-guidelines branch. Coding still reads the preferred tool's documented recommended rules and version where it needs those facts. |
| Refresh of accepted guidance with no stated preference | The explicit refresh branch says no research; absence of a preference does not trigger the first-guidelines condition. Critique and handback no longer require a nonexistent research report. |
| New major version of an existing tool, same covered scope | WAY-251 and each recognition step classify the update as a refresh; step 2 does no research. Coding's trial run gets the version from product files or the proposed tool's documentation, not an assumed research report. |
| Extension to a new test level or other new scope, preferred tool present | Every-extension research still runs. Recognition gives it the reuse-versus-other-tool question; preferences accompany the research. The preference clause and New tools block retain the preferred tool as the proposal/recommendation. |
| New tool with consequential differences | Each New tools block asks for cost, place of running, upkeep and later switching costs, a recommendation and its weak point; the choice stays in the task for the human. |
| New tool tied on product consequences, no preference | Each skill and WAY-185/210/248 recommend the simplest and cheapest; coding has no popularity default. |

The walkthrough found no remaining unconditional report dependency. Coding's fresh judgment of the trial run and each skill's collective critique remain: those are separate existing obligations, not refresh research.

## Foundation entries and Polish meaning sentences

| Entry | Meaning for the request |
|---|---|
| WAY-185 | Wybór nowej biblioteki komponentów lub sposobu stylowania pozostaje pytaniem zadania dla człowieka, ale dostaje skutki dla produktu, rekomendację i jej słaby punkt; preferencja człowieka ma pierwszeństwo, a bez niej przy remisie wygrywa wariant najprostszy i najtańszy. |
| WAY-186 | Styleguide korzysta z preferencji, przy pierwszych wytycznych bez preferencji i przy każdej rozbudowie robi research, przy odświeżeniu go pomija i nie zastępuje narzędzia preferowanego przez człowieka; istniejące ekrany zachowują audyt obok tej ścieżki. |
| WAY-210 | Nowy linter, formater lub audyt zależności dostaje rekomendację przez skutki dla produktu i słaby punkt zamiast domyślnego wyboru narzędzia najczęściej używanego; preferencja człowieka pozostaje pierwsza, a przy remisie bez preferencji wygrywa wariant najprostszy i najtańszy. |
| WAY-211 | Wytyczne kodowania robią research przy pierwszym zestawie bez preferencji i przy każdej rozbudowie, nie przy odświeżeniu, a wskazane przez człowieka narzędzie pozostaje propozycją. |
| WAY-248 | Nowe narzędzie testów lub biblioteka testów własności pozostaje wyborem człowieka w zadaniu i dostaje skutki dla produktu, rekomendację oraz jej słaby punkt, z pierwszeństwem preferencji i wyborem najprostszego, najtańszego wariantu przy remisie bez preferencji. |
| WAY-249 | Wytyczne testów robią research przy pierwszym zestawie bez preferencji i przy każdej rozbudowie, pomijają go przy odświeżeniu i nie wypierają narzędzia preferowanego przez człowieka. |
| WAY-251 | Odświeżenie aktualizuje albo koryguje przyjęte wytyczne w dotychczasowym zakresie, także przy nowej wersji narzędzia, a rozbudowa obejmuje coś nowego i bada, czy użyć tego, co produkt już ma, czy czegoś innego, zachowując preferencję człowieka. |

## Settlements to entries

| Frozen task row | Entry carrying its whole meaning |
|---|---|
| 1 — research at extension, none at refresh, all three skills | WAY-186, WAY-211, WAY-249 |
| 2 — refresh versus extension and the purpose of extension research | WAY-251; its application is cited by WAY-186, WAY-211, WAY-249 |
| 3 — recommendations through consequences, weak point, simplest/cheapest tie | WAY-185, WAY-210, WAY-248 |
| 4 — preferred tool stays proposed and research does not replace it | WAY-186, WAY-211, WAY-249; recommendation clauses in WAY-185, WAY-210, WAY-248 explicitly preserve that precedence |

## Reaches and choices

- Read WAY-03 beyond the dispatch's named IDs because `elements/decisions/examples.md`, required by `record-decision`, selects it as the decision-entry example.
- Used `the-way-record-decision` and its shared rules, method, template and examples for the six edits and new entry. The remaining templates and references were those the handoff required. No additional foundation change followed from the full-foundation dependency search.
- Added WAY-251 for the independently answerable question of refresh versus extension. Rejected repeating that boundary as a fresh decision in each discipline: it would duplicate the same question and allow the definitions to drift. A shared decision costs one further reference for readers, and the skills also state the boundary where it is needed.
- Did not create glossary terms for refresh and extension: the ordinary distinction of updating existing scope versus covering new scope is preserved, while the task expressly settles the operational classification as a decision. Rejected separate glossary copies of the same rule: they would add a second place to maintain without a different meaning to define.
- C3, clarified by the orchestrator during authorship: apply To do 1, “Trzy skille wytycznych robią research ... przy pierwszych wytycznych dyscypliny (gdy człowiek nie ma preferencji, jak dziś)”, also to a first styleguide for existing screens. Rejected preserving the former WAY-186 audit-only exception: it would violate the explicit shared first-guidelines rule. The accepted task names WAY-186 as changing, and its old exception does not outrank that requirement. Cost: first styleguides with existing screens and no preference now include research as well as audit. No human meaning was inferred beyond the orchestrator's interpretation of the frozen requirement.
- Made preference precedence explicit beside recommendation, so the simplest/cheapest tie rule cannot silently replace a named preferred tool. Rejected relying on the preference clause several sections away: readers could treat the local recommendation rule as unconditional.
- Read the proposed tool's versioned documentation where coding needs its recommended set or version but no research ran. This satisfies the existing WAY-204/211 sourcing obligation without starting a comparison of alternatives. Rejected requiring a research report as the source: a refresh or preference-only path would then be impossible.
- Kept unrelated differences between audits, trial runs, templates and other guideline choices. No plan adaptation, changed invariant test, open question, missing permission, or outstanding failure remains.

The author returns before independent review. The later return step remains with the orchestrator's resumption of this author.
