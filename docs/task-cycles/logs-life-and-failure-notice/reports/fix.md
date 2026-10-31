# Report of the fix

**Status:** done. Findings 1-4 fixed, none contested.

## Findings
1. **Alert missing from WAY-270** (`foundations/decisions.md`): the binding part now says the choice is answered by a tool that collects failures, an alert or a deliberate absence; the complying example holds an alert beside the tools and the absence; the *Rationale* says an alert built on the logs may come in a table of its own. No product named; the step's files still name only the deliberate absence. Check: `grep -n "an alert" foundations/decisions.md` shows the three places.
2. **Rationale reason of answer 2**: bounded to a definition ("at a definition the question comes with it; at a task the deployment skill's check carries it (WAY-139)"). Check: the sentence no longer conflicts with the binding part "only where the note touches it".
3. **WAY-139 count**: the list is now seven items, five as before plus "how to read the logs; how long the record lives, between deployments too; and how a human learns of a failure"; the sentence reads "For the two items on the record's life and on a failure", matching `resolve_gaps.md`, which names the same two and says nothing of five.
4. **New list not nested**: `list.md` says a silent decision does not hold the matter and the item stands `— open` with it nested as `running_product.md` gives; `running_product.md` heading is now "The entry nested under an item" and opens with the new-list case before the resumed-list bullets; `task_run.md` adds that, where the note touches a matter of the logs, interface or development data, a silent decision holds nothing and the item stands `— open` with the decision nested as `Changes:` (spec D6 second reading), while "An agent never opens one" still binds a decision that does answer.

## Meaning sentences changed
- WAY-270: Gdy projekt uruchamia produkt poza maszyną, na której powstaje (chyba że definicja albo decyzja fundamentu trzyma go na tej maszynie), i żadna decyzja fundamentu tego nie rozstrzyga, krok technologii stawia na liście, jak człowiek dowiaduje się o awarii, jako osobny wybór poza drogą agenta, z odpowiedzią w postaci narzędzia zbierającego awarie, alertu albo świadomego braku (ten zawsze w porównaniu), a żadna definicja nie musi go mieć, bramka go nie sprawdza i zatwierdzona definicja nie wraca z jego powodu.
- WAY-139: Lista skilla wdrożeniowego ma siedem punktów, w tym osobno czas życia zapisu logów i skąd człowiek dowiaduje się o awarii; dla tych dwóch doprecyzowanie cytuje odpowiedź z decyzji albo zatwierdzonej definicji, w przeciwnym razie pyta człowieka, czy uruchomić krok technologii, a zapisana odmowa pokrywa punkt.
Others unchanged.

## Checks (command, exit code)
- `python -B elements/common/foundation_check.py .` : 0
- `python -B gate/run_tests.py project-level` : 0
- Full gate: not run (the orchestrator's).

## Own-work check
Read three paths. New list (`TODO`): SKILL.md step 1 -> `list.md` (silent decision does not hold; item `— open`, decision nested) -> `running_product.md` (nesting form) -> `settle.md` 1 and `research.md` give the nested decision and its answer as an option -> sub-step 7 names it as the entry rewritten. Resumed list: `start.md` list bullet turns held/projected items open with the nesting, the open-item bullet skips a silent nested projected decision and reuses only an answering report; same tail. Run at a task: `task_run.md` skips the looks, but a matter the note touches with a silent decision is `— open` with it nested; `list.md` applies, `settle.md` 1-6 give the nested decision, and its own *Write* names which decision is changed. Read only; no run.

## Searches not found or unclear
none new; the earlier ones in `author.md` stand.
