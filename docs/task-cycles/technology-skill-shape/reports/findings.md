# Blocking findings of the whole-change review

From [review.md](review.md), first line `FAIL c2e70f9f1e01e1ebfbeed0ff69352c498b674a8a`, in the reviewer's words.

## 1. A resuming leader whose human changes the list never reaches the rules of the list

**Grade:** Important. Within the task (acceptance criteria 1 and 3).

**Anchor:** `project-level/technology/SKILL.md:33-35`, `project-level/technology/start.md:20`

**To paste:** On a resume with open choices the leader asks whether the list still holds, but it is told to read `list.md` only when the look adds an item. A human who adds or changes an item at that question leaves the leader without the rules for wording and marking it, which stand only in `list.md`.

**Why I report it:** `start.md:20` keeps the old sentence "Then show the list, ask whether it still holds", and the old `SKILL.md:74-75` shows what that answer can be: confirm, add, strike. In the old file the leader had read step 1 whatever it did, so an added item met these rules. After the change the only route to `list.md` from a resume is `SKILL.md:34-35`, "when the look it gives adds an item to the list", repeated at `start.md:15-16`. So the moment "the human adds an item" has no pointer.

What the template still carries for that leader, read whole on every route: the markers, naming by need (`definition_template.md:184-192`) and nested items (`:194`). What only `list.md` carries:

- `list.md:15-17`: a way of logging in is listed as its method, and its library is a choice of its own.
- `list.md:19-22`: a decision that settles the choice in a sentence about something else still holds it; a decision the project changes no longer holds it.
- `list.md:23-24`: writing the list and the status line before asking.
- `list.md:25-29`: why each item is needed, and the question on preferences.

Example: resuming, the human says "add logging in with Google". The leader writes a library as an item, or marks `— open` a choice a foundation decision settles in a sentence about something else, and research starts on it. Nothing reports this: the marker is valid, so `readiness_check.py` passes it.

The author saw the cost in "Choices" item 3 ("a leader that adds an item without reading `list.md` names it badly; the pointer is in `start.md` at that bullet"), but the pointer stands at the look's bullet only. Assessment row `[63-66]` says "A resumed leader that adds an item reads list.md for this rule", which is true of the look alone. `checks/reach.py` asserts only the fragments the criteria name, so it could not catch this.

Criterion 3 names two fragments after a colon. I read them as the cases it must reach, not as a limit on "a fragment needed in more than one place"; criterion 1 asks the same without a list. This is a reach gap on one sub-route, not a lost sentence: the text stands in `list.md`.

Fix, a few words: in `SKILL.md:34-35`, "when the look it gives or the human adds or changes an item", and the same in `start.md:20`, for instance "ask whether it still holds; where the human adds or changes an item, follow the step "List the choices" (`list.md` beside this file) for it". The conditional line of `word-counts.md` then covers that case too.

## 2. The count of the route "leader, resuming, open choices" leaves out `close.md`

**Grade:** Important. Within the task (To do 4). The number goes into the request.

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/word-counts.md:18`, `:66`; `.runs/task-cycles/technology-skill-shape/checks/word_counts.py:74`

**To paste:** The route "leader, resuming, open choices" is counted without `close.md`, though that leader ends in the step "Close" as the leader with a new list does, whose route counts it. The row should read 6427 and -201, not 6331 and -297.

**Why I report it:** To do 4 counts the words in the files read on a route. `SKILL.md:51` sends every leader to `close.md` once the list holds no open choice, and a resume with open choices reaches that state when its last wave is written. `settle.md` does not end the skill. Route "new list, open choices" lists `close.md` (`word_counts.py:73`), the resuming route does not (`:74`), and `word-counts.md` gives no reason for the difference.

My recount: 468 + 293 + 178 + 886 + 96 = 1921, plus 3675 fixed and 831 critique = 6427, against 6628 before = -201. All other rows recount exactly (see Checks). The conclusions in "Reading of the numbers" still hold.

The same route list sits at `checks/reach.py:20`, so the reach check never looked at `close.md` on this route. The figure "297" also stands in `author.md:101`.

Fix: add `close.md` at `word_counts.py:74` and `reach.py:20`, regenerate `word-counts.md`, and correct its file list at `:66`.
