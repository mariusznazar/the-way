# Find where a product keeps its backlog

Read by every skill that must find the place of a product's tasks or projects, or the rules of the
task place (WAY-107). The place stands in the `## Backlog` section of the product's root
`AGENTS.md`, in a line for `Tasks` or `Projects`. A line gives the place in one of three ways:

- a directory of the product's repository, written as a path from its root, or the address of a
  public tracker or the name of a tool: use it as written;
- an entry of the user's locations file, written as the name of the entry and of the repository it
  stands under in `~/.the-way/locations.json`, as "the entry `tasks` under `the-way`" in the section
  of the-way's own `AGENTS.md` (in another product, the product's name stands in place of
  `the-way`): the place is on the user's own disk, outside every repository (WAY-320);
- words only, naming no place: ask, as below.

The rules by which a task's line is written — the status of a new line, its move to ready, the form
of its dependencies — belong to the task place, not to the product or to the-way. A line for
`Task rules` names them as an entry of the locations file, "the entry `task-rules` under `the-way`",
whose value is the path of a file of those rules; `project-level/task_line.md` says how a line is
written by them (WAY-107).

## Resolve an entry of the locations file

The file is a JSON object whose keys are repository names; under each key, entries by name hold a
path on the user's disk. `~` is the user's home directory. Read the file, take the key named in the
line and, under it, the entry named in the line: its value is the place, or the file of rules.

Where the file does not exist, cannot be read as JSON, holds no such key or no such entry, or the
path it holds does not exist, the place, or the file of rules, is missing. Ask the human where it
is, and offer to add the entry to the file: create the file or the key where they are missing, and
write the entry only when the human agrees. An agent that runs a task cycle does not create or
change the locations file (WAY-140): it names the missing entry in its report and goes on only with
what it can do without the place or the rules.

The path the entry holds, and the file's content, never enter a file of the repository, a record, a
request or a report: those name the entry, as "the entry `tasks` under <the product's name>", and
say nothing more (WAY-320).

## Record a place that is missing

Where the section names no place, or the entry it names is missing, ask once and offer to record the
answer where it fits:

- a place on the user's disk outside every repository: write the entry into the locations file as
  above, and name the entry in the `## Backlog` section, never the path;
- a directory of the repository or the address of a public tracker: write it in the `## Backlog`
  section, as a path from the root of the repository or as the address.

The rules of the task place are recorded the same way, in the first form only: where the section has
no `Task rules` line, or the entry it names is missing, ask once and offer to write the entry
`task-rules` into the locations file and its name into the section as the line `Task rules`.
