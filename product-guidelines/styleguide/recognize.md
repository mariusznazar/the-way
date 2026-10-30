# Recognize

- Name the user interface: the part of the map whose files draw it. A product whose users reach it
  only through an API or a terminal has no user interface in this sense; say so and end (WAY-183).
  Every other user interface gets a styleguide of its own, however simple, an admin panel added to
  a backend included; where the product has several, the human says which this task covers. Where
  the map holds no part for it yet, as before a first screen, its identifier is a question of the
  task, and *To do* gains adding that part, with the files the task creates, through
  `update-part-map`.
- Read the product's root `AGENTS.md` and every file under `guidelines/` that `refine-task` did not
  read at its step 1. Of the product's
  foundation, read — besides what `refine-task` selected at its step 1 — the decisions that settle
  the technology of the user interface, and every decision that already gives a role its meaning, a
  value its source or the styleguide a departure (WAY-150).
- Read off what the product has for it — a file of design tokens its screens read, one nothing
  reads, shared components, or nothing — whether it has screens, and whether a styleguide exists.
  Say plainly when it has nothing (WAY-185).
- That gives the mode: no screens, the starting rules of step 2; screens and no styleguide, the
  starting rules of step 2 and the audit of step 3; an existing styleguide, its refresh or
  extension — step 2, and step 3 where screens changed since the styleguide was written.
- Extend what exists. A new library of components or a new way of styling is a technology choice:
  record it as an open question of the task, never settle it (WAY-185, WAY-121).

A refresh updates or corrects accepted guidelines within the scope they already cover,
including adapting them to a new version of a tool the product uses. An extension covers something
new; its research checks whether to use what the product has or something else (WAY-251).
