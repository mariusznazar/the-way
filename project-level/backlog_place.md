# Find where a product keeps its backlog

Read by every skill that must find the place of a product's tasks or projects (WAY-107). The place
stands in the `## Backlog` section of the product's root `AGENTS.md`, in a line for `Tasks` or
`Projects`. A line gives the place in one of three ways:

- a directory of the product's repository, written as a path from its root, or the address of a
  public tracker or the name of a tool: use it as written;
- an entry of the user's locations file, written as the name of the entry and of the repository it
  stands under in `~/.the-way/locations.json`, as "the entry `tasks` under `the-way`": the place is
  on the user's own disk, outside every repository (WAY-320);
- words only, naming no place: ask, as below.

## Resolve an entry of the locations file

The file is a JSON object whose keys are repository names; under each key, entries by name hold a
path on the user's disk. `~` is the user's home directory. Read the file, take the key named in the
line and, under it, the entry named in the line: its value is the place.

Where the file does not exist, cannot be read as JSON, holds no such key or no such entry, or the
path it holds does not exist, the place is missing. Ask the human where the place is, and offer to
add the entry to the file: create the file or the key where they are missing, and write the entry
only when the human agrees. An agent that runs a task cycle writes nothing outside the repository
(WAY-140): it names the missing entry in its report and goes on only with what it can do without
the place.

The path the entry holds, and the file's content, never enter a file of the repository, a record, a
request or a report: those say "the entry `tasks` under `the-way`" and nothing more (WAY-320).

## Record a place that is missing

Where the section names no place, or the entry it names is missing, ask once and offer to record the
answer where it fits:

- a place on the user's disk outside every repository: write the entry into the locations file as
  above, and name the entry in the `## Backlog` section, never the path;
- a directory of the repository or the address of a public tracker: write it in the `## Backlog`
  section, as a path from the root of the repository or as the address.
